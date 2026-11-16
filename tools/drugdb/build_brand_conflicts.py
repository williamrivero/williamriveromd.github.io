#!/usr/bin/env python3
"""List brand names registered under two or more UNRELATED generics, for Dr. Rivero's review.

Reads data/drugs/registry/*.json and writes data/drugs/_brand_conflicts.json:
  {as_of, description, counts, conflicts: [{brand, groups: [{slugs[], ingredients[], products: [
      {registration_number, generic_name, brand_name, dosage_strength_form, manufacturer, classification,
       issuance_date, expiry_date}]}]}]}

Brand names are compared case-, accent-, space- and punctuation-insensitively ("ELAVIL", "Elavil" match).
Generics under one brand are grouped when they share an ingredient (a combination and its single-ingredient
parent, e.g. losartan and losartan + hydrochlorothiazide, are one group). Registry spelling variants and
typos (chlorpheniramine/chlorphenamine, "atorvastation") and same-substance families (iron/ferrous salts)
also count as shared, so they are not reported as conflicts. A brand is a conflict only when
two or more groups remain, i.e. at least two generics with no ingredient in common. Placeholder brands
("None", "Unbranded", "N/A", blank) and brands that are just a generic's own name are skipped.
"""
import argparse, glob, json, os, re, sys, unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PLACEHOLDER = {"", "none", "unbranded", "na", "n a", "no brand", "no brand name", "generic", "nil", "not applicable",
               "without brand", "-", "brandless", "none stated", "not indicated"}


# words that say nothing about which substance it is
STOP = set("""solution injection with and in of plus for the hydrochloride hcl hydrochlorid sodium potassium calcium
extended release modified tablet tablets capsule syrup suspension cream oral topical sterile water dextrose
sulfate sulphate acetate phosphate chloride bromide citrate maleate base anhydrous monohydrate dihydrate trihydrate
heptahydrate equivalent as mg g ml mcg iu low high""".split())
# spelling families the registry uses interchangeably
SYN = {"chlorpheniramine": "chlorphenamine", "colecalciferol": "cholecalciferol", "iron": "ferrous", "ferric": "ferrous",
       "acetaminophen": "paracetamol", "albuterol": "salbutamol", "ciclosporin": "cyclosporine",
       "cyclosporin": "cyclosporine", "vitamins": "vitamin", "multivitamins": "vitamin", "multivitamin": "vitamin",
       "minerals": "mineral", "aciclovir": "acyclovir", "frusemide": "furosemide", "sultamicillin": "ampicillin",
       "ketoanalogues": "ketoanalogue", "ketoanalogs": "ketoanalogue", "valproate": "valproic", "fusidate": "fusidic",
       "thiamazole": "methimazole", "glycerin": "glycerol", "methylcobalamin": "mecobalamin",
       "methylcobalamine": "mecobalamin", "amoxiclav": "amoxicillin", "lodine": "iodine"}
# extra family tokens: B vitamins written as names or as "vitamin B1/B6/B12"
FAMILY = {"thiamine": "vitamin", "pyridoxine": "vitamin", "cyanocobalamin": "vitamin", "mecobalamin": "vitamin",
          "cholecalciferol": "vitamin", "ascorbic": "vitamin"}


JUNK = re.compile(r"^(generic-name|drp-|dr-|powder-for-|solution-for-|unknown)")


def tokens(ingredient):
    out = set()
    for w in re.split(r"[^a-z0-9]+", key(ingredient)):
        if len(w) >= 4 and w not in STOP and not w.isdigit():
            w = SYN.get(w, w)
            out.add(w)
            if w in FAMILY:
                out.add(FAMILY[w])
    return out or {key(ingredient)}


def related(a_ings, b_ings):
    """True when two generics plausibly share an ingredient: identical, same spelling family, or a typo
    (similar tokens, e.g. atorvastatin / atorvastation, clotrimazole / clotimazole)."""
    if set(a_ings) & set(b_ings):
        return True
    ta = set().union(*(tokens(i) for i in a_ings)) if a_ings else set()
    tb = set().union(*(tokens(i) for i in b_ings)) if b_ings else set()
    if ta & tb:
        return True
    for x in ta:
        for y in tb:
            if x[:2] == y[:2] and SequenceMatcher(None, x, y).ratio() >= 0.8:
                return True
    return False


def key(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[®™©]", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=os.path.join(REPO, "data", "drugs"))
    a = ap.parse_args()
    products = []
    for f in sorted(glob.glob(os.path.join(a.data_dir, "registry", "*.json"))):
        products += json.load(open(f, encoding="utf-8"))
    generic_keys = {key(i) for p in products for i in (p.get("ingredients") or [])}
    generic_keys |= {key(p.get("generic_name")) for p in products}
    by_brand = defaultdict(list)
    for p in products:
        k = key(p.get("brand_name"))
        if k in PLACEHOLDER or k.startswith("none ") or k in generic_keys or len(k) < 2:
            continue
        by_brand[k].append(p)

    conflicts = []
    for k, ps in sorted(by_brand.items()):
        slugs = {}
        for p in ps:
            slugs.setdefault(p["generic_slug"], set(p.get("ingredients") or [p["generic_slug"]]))
        if len(slugs) < 2:
            continue
        # union-find over slugs that share at least one ingredient
        parent = {s: s for s in slugs}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        sl = sorted(slugs)
        for i, s in enumerate(sl):
            for t in sl[i + 1:]:
                if related(sorted(slugs[s]), sorted(slugs[t])):
                    parent[find(s)] = find(t)
        groups = defaultdict(list)
        for s in sl:
            groups[find(s)].append(s)
        if len(groups) < 2:
            continue
        out_groups = []
        for members in sorted(groups.values()):
            ings = sorted(set().union(*(slugs[m] for m in members)))
            prods = [{f: p.get(f) for f in ("registration_number", "generic_name", "brand_name", "dosage_strength_form",
                                             "manufacturer", "classification", "issuance_date", "expiry_date")}
                     for p in sorted(ps, key=lambda x: x["registration_number"]) if p["generic_slug"] in members]
            out_groups.append({"slugs": members, "ingredients": ings, "products": prods})
        display = max((p.get("brand_name") or "" for p in ps), key=lambda b: sum(1 for q in ps if q.get("brand_name") == b))
        c = {"brand": display.strip(), "brand_key": k, "unrelated_generics": len(out_groups), "groups": out_groups}
        junk = [m for g in out_groups for m in g["slugs"] if JUNK.search(m)]
        if junk:
            c["note"] = "Registry generic_name looks malformed for " + ", ".join(junk) + " (likely a data-entry error, not a second generic)."
        conflicts.append(c)
    conflicts.sort(key=lambda c: (-c["unrelated_generics"], c["brand_key"]))
    out = {
        "as_of": date.today().isoformat(),
        "built_by": "tools/drugdb/build_brand_conflicts.py",
        "description": ("Brand names registered with FDA Philippines under two or more generics that share no "
                        "ingredient. Some are legitimate (umbrella brands, different companies reusing a name); "
                        "others may be registry data-entry errors. For review only; not rendered on the site."),
        "counts": {"brands_checked": len(by_brand), "conflicts": len(conflicts),
                   "products_involved": sum(len(g["products"]) for c in conflicts for g in c["groups"])},
        "conflicts": conflicts,
    }
    path = os.path.join(a.data_dir, "_brand_conflicts.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"brands checked {len(by_brand)}  conflicts {len(conflicts)}  -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
