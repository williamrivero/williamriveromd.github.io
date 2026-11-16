#!/usr/bin/env python3
"""Normalize the PH FDA crawl into data/drugs/registry.json and data/drugs/generics.json.

Input (from the crawler, run on a Philippine connection):
  --crawl-dir DIR  containing ph-fda-drugs.json, ph-fda-pipil.json, ph-fda-vat-exempt.json
Output:
  data/drugs/registry/<a-z|0>.json  sharded list of products (Cloudflare 25 MB file cap), each with generic_slug + ingredients[] + pi_links[] + vat_exempt
  data/drugs/generics.json   {slug: {name, ingredients[], products, categories[], rx, otc}}
Slug rule (shared contract): lowercase base ingredient names (parenthetical salts / "as ..." removed,
trailing salt words removed unless the salt IS the drug, e.g. potassium chloride), combinations sorted
alphabetically and joined with "-".
"""
import argparse, json, os, re, unicodedata
from collections import Counter, defaultdict

SALT_WORDS = set("""hydrochloride hcl dihydrochloride sodium potassium calcium magnesium besilate besylate mesilate mesylate
maleate fumarate succinate tartrate bitartrate citrate acetate sulfate sulphate phosphate bromide hydrobromide chloride
nitrate lactate gluconate malate tosilate tosylate camsylate dipropionate propionate valerate butyrate furoate
monohydrate dihydrate trihydrate hemihydrate sesquihydrate anhydrous hyclate pamoate embonate trometamol tromethamine
meglumine disodium dipotassium hemifumarate erbumine arginine lysine olamine axetil pivoxil medoxomil cilexetil
proxetil etabonate decanoate enanthate cypionate palmitate stearate xinafoate bisulfate hydrogen hemisulfate
mononitrate dinitrate carbonate oxalate saccharinate""".split())
# words that are themselves the active moiety when they come first
LEADING_ACTIVE = set("""sodium potassium calcium magnesium ferrous ferric zinc lithium aluminum aluminium iron copper
selenium chromium manganese ammonium silver bismuth barium cobalt""".split())
SPLIT = re.compile(r"\s*(?:\+|/(?!\s*\d)| and |, (?=[A-Z])|;)\s*", re.I)

def ascii_fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()

def base_ingredient(part):
    p = ascii_fold(part)
    p = re.sub(r"\([^)]*\)", " ", p)            # (as besilate), (equivalent to ...)
    p = re.sub(r"\[[^\]]*\]", " ", p)
    p = re.sub(r"\bequivalent to\b.*$", " ", p, flags=re.I)
    p = re.sub(r"\b\d[\d.,]*\s*(mg|mcg|g|iu|ml|%|units?)\b.*$", " ", p, flags=re.I)
    p = re.sub(r"^\s*[\d.,]+\s*%?\s*", " ", p)          # leading "10% Dextrose", "4.25 ..."
    words = [w for w in re.split(r"[^A-Za-z0-9\-']+", p.lower()) if w]
    if not words: return ""
    if words[0] not in LEADING_ACTIVE:
        while len(words) > 1 and words[-1] in SALT_WORDS:
            words.pop()
    return " ".join(words).strip("-' ")

SYNONYMS = {"potassium clavulanate": "clavulanic acid", "clavulanate potassium": "clavulanic acid",
            "clavulanate": "clavulanic acid", "paracetamol": "paracetamol", "acetaminophen": "paracetamol",
            "salbutamol": "salbutamol", "albuterol": "salbutamol", "vitamin b1": "thiamine",
            "vitamin c": "ascorbic acid", "co-trimoxazole": "sulfamethoxazole + trimethoprim"}
COMBO_ALIASES = {"co-amoxiclav": ["amoxicillin", "clavulanic acid"], "co-trimoxazole": ["sulfamethoxazole", "trimethoprim"],
                 "cotrimoxazole": ["sulfamethoxazole", "trimethoprim"], "ampicillin sulbactam": ["ampicillin", "sulbactam"]}
def is_veterinary(rec):
    rn = (rec.get("registration_number") or "").upper()
    txt = " ".join(str(rec.get(k) or "") for k in ("generic_name", "pharmacologic_category", "classification")).lower()
    return rn.startswith("VR") or "veterinary" in txt or "(vet)" in txt or " vet " in f" {txt} "

def ingredients_of(generic_name):
    g = ascii_fold(generic_name or "")
    m = re.search(r"\(([^()]*\+[^()]*)\)", g)       # "Co-amoxiclav (Amoxicillin + Clavulanic Acid)"
    if m: g = m.group(1)
    g = re.sub(r"\((?:as|equiv|equivalent|e\.q\.|eq\.)[^)]*\)", " ", g, flags=re.I)
    parts = [SYNONYMS.get(b, b) for b in (base_ingredient(x) for x in SPLIT.split(g) if x and x.strip())]
    exp = []
    for p in parts:
        exp.extend(COMBO_ALIASES.get(p, [p]))
    parts = exp
    out = []
    for p in parts:
        if p and p not in out: out.append(p)
    return sorted(out)

def slug_of(ings):
    s = "-".join(re.sub(r"[^a-z0-9]+", "-", i).strip("-") for i in ings)
    return re.sub(r"-{2,}", "-", s)[:120] or "unknown"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--crawl-dir", required=True)
    ap.add_argument("--out-dir", default=os.path.join(os.path.dirname(__file__), "..", "..", "data", "drugs"))
    a = ap.parse_args()
    os.makedirs(a.out_dir, exist_ok=True)
    drugs = json.load(open(os.path.join(a.crawl_dir, "ph-fda-drugs.json")))
    pipil = json.load(open(os.path.join(a.crawl_dir, "ph-fda-pipil.json"))) if os.path.exists(os.path.join(a.crawl_dir, "ph-fda-pipil.json")) else []
    vat = json.load(open(os.path.join(a.crawl_dir, "ph-fda-vat-exempt.json"))) if os.path.exists(os.path.join(a.crawl_dir, "ph-fda-vat-exempt.json")) else []
    pi_by_rn = defaultdict(list)
    for r in pipil:
        rn = (r.get("registration_number") or "").strip()
        if rn and r.get("file_link"):
            e = {"version": r.get("version"), "file_link": r.get("file_link")}
            if e not in pi_by_rn[rn]: pi_by_rn[rn].append(e)
    vat_slugs = {slug_of(ingredients_of(v.get("generic_name"))) for v in vat}
    products, gen = [], defaultdict(lambda: {"name": Counter(), "ingredients": None, "products": 0,
                                             "categories": Counter(), "rx": 0, "otc": 0})
    vet = 0
    for rn, r in sorted(drugs.items()):
        if is_veterinary(dict(r, registration_number=rn)):
            vet += 1; continue
        ings = ingredients_of(r.get("generic_name"))
        if not ings: continue
        slug = slug_of(ings)
        p = {k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
        p["registration_number"] = rn
        p["generic_slug"] = slug
        p["ingredients"] = ings
        p["pi_links"] = pi_by_rn.get(rn, [])
        p["vat_exempt"] = slug in vat_slugs
        products.append(p)
        g = gen[slug]
        g["name"][re.sub(r"\s+", " ", r.get("generic_name") or "").strip()] += 1
        g["ingredients"] = ings
        g["products"] += 1
        if r.get("pharmacologic_category"): g["categories"][r["pharmacologic_category"].strip()] += 1
        cls = (r.get("classification") or "").lower()
        if "rx" in cls or "prescription" in cls: g["rx"] += 1
        elif "otc" in cls or "over" in cls or "household" in cls: g["otc"] += 1
    generics = {}
    for slug, g in sorted(gen.items()):
        # display name: title-cased base ingredients joined with " + "
        disp = " + ".join(i[:1].upper() + i[1:] for i in g["ingredients"])
        generics[slug] = {"name": disp, "ingredients": g["ingredients"], "products": g["products"],
                          "registered_names": [n for n, _ in g["name"].most_common(5)],
                          "categories": [c for c, _ in g["categories"].most_common(3)],
                          "rx": g["rx"], "otc": g["otc"], "vat_exempt": slug in vat_slugs}
    # Cloudflare Pages caps files at 25 MB, so the registry is sharded by the slug's first character.
    shard_dir = os.path.join(a.out_dir, "registry"); os.makedirs(shard_dir, exist_ok=True)
    for f in os.listdir(shard_dir):
        if f.endswith(".json"): os.remove(os.path.join(shard_dir, f))
    shards = defaultdict(list)
    for p in products:
        c = p["generic_slug"][0]
        shards[c if c.isalpha() else "0"].append(p)
    for c, lst in shards.items():
        json.dump(lst, open(os.path.join(shard_dir, f"{c}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    old = os.path.join(a.out_dir, "registry.json")
    if os.path.exists(old): os.remove(old)
    json.dump(generics, open(os.path.join(a.out_dir, "generics.json"), "w"), ensure_ascii=False, indent=1)
    print(f"veterinary skipped {vet}  products {len(products)}  generics {len(generics)}  with PI {sum(1 for p in products if p['pi_links'])}  VAT-exempt generics {sum(1 for g in generics.values() if g['vat_exempt'])}")

if __name__ == "__main__":
    main()
