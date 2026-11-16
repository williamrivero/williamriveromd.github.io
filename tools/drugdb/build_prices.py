#!/usr/bin/env python3
"""Build data/drugs/prices.json from official Philippine government price references.

Inputs (tools/drugdb/sources/):
  raw/DPRI-<edition>.txt               pdftotext -layout of a DOH Drug Price Reference Index booklet
                                       (currently the 2021, 9th edition, hosted by DOH CHD-CAR)
  gamot_fixed_fee_pc2025-0013.tsv      PhilHealth GAMOT fixed fee schedule (PC2025-0013 Annex A.2), hand-transcribed
  dpri_<edition>.tsv  (optional)       a newer DPRI edition exported from dpri.doh.gov.ph on a Philippine connection,
                                       columns: drugname, price_low, price_high[, reference_price] (see SOURCES.md)

Output: data/drugs/prices.json
  {slug: [{dosage_form_strength, price_low, price_high, unit, currency: "PHP", price_type, source, source_date,
           reference_price?, notes?}]}
price_type: "dpri_range" (DOH procurement price range, lowest-highest), "dpri_reference" (single DOH reference
price, no range published), or "philhealth_gamot_fixed_fee" (PhilHealth reimbursement per unit dispensed).
These are public-procurement and reimbursement benchmarks, not retail drugstore prices.

Usage: python3 tools/drugdb/build_prices.py [--report]
No drugstore or MIMS data is used (their terms forbid scraping).
"""
import argparse, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pnf_price_slugs import Resolver, REPO  # noqa: E402

SRC = os.path.join(HERE, "sources")
DPRI_2021 = {
    "txt": os.path.join(SRC, "raw", "DPRI-2021-as-of-9-17-2021.txt"),
    "source": "DOH Drug Price Reference Index (DPRI) 2021, 9th edition (as of September 17, 2021); https://caro.doh.gov.ph/wp-content/uploads/2021/09/2021DPRI-as-of-9-17-2021.pdf",
    "date": "2021-09-17",
}
GAMOT = {
    "tsv": os.path.join(SRC, "gamot_fixed_fee_pc2025-0013.tsv"),
    "source": "PhilHealth Circular No. 2025-0013, Annex A.2 GAMOT Fixed Fee Schedule; https://www.philhealth.gov.ph/circulars/2025/PC2025-0013.pdf",
    "date": "2025-07-28",
}
MARK_NOTES = {
    "*": "Reference price based on the DOH Central Office Bids and Awards Committee procurement price 2020",
    "◊": "Reference price based on the Maximum Wholesale Price (MWP); excluded from the 10% inflation allowance",
    "**": "Excluded from the maximum 10% inflation allowance",
}
UNIT_WORDS = ["prefilled syringe", "pre-filled syringe", "pre-filled pen", "suppository", "sachet", "tablet", "capsule",
              "ampule", "ampul", "vial", "bottle", "bag", "tube", "syringe", "pen", "cartridge", "nebule", "patch",
              "inhaler", "canister", "dispenser", "kit", "pack", "jar", "can", "lozenge", "ovule", "implant", "ring",
              "device", "pouch", "cassette", "piece"]
NUM = r"\d{1,3}(?:,\d{3})*\.\d{2}"


def unit_of(text):
    t = text.lower()
    best = None
    for w in UNIT_WORDS:
        for m in re.finditer(r"\b%ss?\b" % re.escape(w), t):
            if best is None or m.start() > best[0]:
                best = (m.start(), w)
    if not best:
        return "per unit"
    w = {"ampul": "ampule", "pre-filled syringe": "prefilled syringe", "pre-filled pen": "prefilled pen"}.get(best[1], best[1])
    return f"per {w}"


def split_name(desc):
    """'Amikacin (as Sulfate) 100 mg powder Vial' -> ('Amikacin (as Sulfate)', '100 mg powder Vial')."""
    depth = 0
    for i, ch in enumerate(desc):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0 and ch.isdigit() and i > 0 and desc[i - 1] in " ":
            # "Insulin 70/30" and "Dextrose 5%" style names keep their first number in the name only if
            # nothing but the name precedes; otherwise the number starts the strength
            return desc[:i].strip(" ,"), desc[i:].strip()
    # forms without a leading number, e.g. "Timolol Eye Drops 0.5%" handled above; "Vaccine, BCG ..." etc.
    return desc.strip(), ""


def parse_dpri(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(lines) if re.match(r"^\s*1\.\s+\S", l))
    blocks, cur = [], None
    for l in lines[start:]:
        if re.match(r"^\s*\d+\.\s+\S", l) and re.match(r"^\s*(\d+)\.", l):
            cur = [l]
            blocks.append(cur)
        elif cur is not None:
            s = l.strip()
            if (not s or re.fullmatch(r"[A-Z]|◊", s) or "P a g e" in s
                    or s.startswith(("*", "◊", "Health Facilities", "All Prices", "Drugname", "(GIDA", "The Reference"))):
                continue                                          # page furniture and footnotes
            cur.append(l)
    out = []
    for b in blocks:
        no = int(re.match(r"^\s*(\d+)\.", b[0]).group(1))
        left_parts, rng, ref = [], [], []
        for i, l in enumerate(b):
            body = re.sub(r"^\s*\d+\.\s+", lambda m: " " * len(m.group(0)), l) if i == 0 else l
            m = re.search(r"\S.*?(?=\s{3,}|$)", body)
            text_end = 0
            if m and m.start() < 40 and not re.match(NUM + r"\s*$", m.group(0).strip()):
                left_parts.append(m.group(0).strip())
                text_end = m.end()
            for t in re.finditer(NUM, body[text_end:]):
                t_start = t.start() + text_end
                (rng if t_start < 84 else ref).append(float(t.group(0).replace(",", "")))
        desc = re.sub(r"\s+", " ", " ".join(left_parts)).strip()
        right = " ".join(b)
        marks = [k for k in ("**", "◊") if k in right]
        if "**" not in marks and re.search(r"\d\*", right):
            marks.append("*")
        nums = rng + ref
        if not nums:
            continue
        rec = {"no": no, "desc": desc, "reference": ref[-1] if ref else nums[-1], "marks": marks}
        if len(rng) >= 2:
            rec["low"], rec["high"] = rng[0], rng[1]
        out.append(rec)
    return out


FORM_TAIL = re.compile(r"\s+(eye drops solution|eye drops|ear drops|eye ointment|ophthalmic ointment|cream|ointment|lotion|"
                       r"gel|tablet|capsule|syrup|suspension|solution|lyophilized powder|powder)\s*$", re.I)


def dpri_name(desc):
    """Generic name part of a DPRI drug description, with list-style prefixes and dosage-form words removed."""
    name, _ = split_name(desc)
    for pat, rep in [(r"^Vaccine, (.*)$", r"\1 Vaccine"), (r"^I\.V\. Fluids, (.*)$", r"\1"),
                     (r"^Serum, (.*?)( \(.*)?$", r"\1 serum"), (r"^Insulin, (.*)$", r"\1 Insulin"),
                     (r"^Immunoglobulin, (Normal, Human.*)$", r"Immunoglobulin Normal, Human"),
                     (r"^Immunoglobulin, (\w+)(.*)$", r"\1 Immunoglobulin"), (r"^Multivitamins.*", "Multivitamins")]:
        if re.match(pat, name):
            name = re.sub(pat, rep, name)
            break
    prev = None
    while prev != name:
        prev, name = name, FORM_TAIL.sub("", name)
    return name


def main(args):
    res = Resolver()
    prices, unmatched = {}, []

    def add(name, entry):
        primary, matches = res.resolve(name)
        if primary == "unknown":
            unmatched.append(name)
            return
        if primary not in res.generics:
            unmatched.append(f"{primary} <- {name}")
        for slug in [primary] + [m for m in matches if m != primary]:
            prices.setdefault(slug, []).append(dict(entry))

    n_dpri = 0
    for r in parse_dpri(DPRI_2021["txt"]):
        name = dpri_name(r["desc"])
        e = {"dosage_form_strength": r["desc"], "price_low": r.get("low", r["reference"]),
             "price_high": r.get("high", r["reference"]), "unit": unit_of(r["desc"]), "currency": "PHP",
             "price_type": "dpri_range" if "low" in r else "dpri_reference", "reference_price": r["reference"],
             "source": DPRI_2021["source"], "source_date": DPRI_2021["date"]}
        notes = [MARK_NOTES[m] for m in r["marks"]]
        if "low" in r:
            notes.append("Range = lowest-highest procurement price (highest usable only in GIDA areas); reference_price = 2021 DPRI ceiling (median)")
        e["notes"] = notes
        add(name, e)
        n_dpri += 1

    n_gamot = 0
    for line in open(GAMOT["tsv"], encoding="utf-8"):
        if not line[:1].isdigit():
            continue
        no, mol, prep, fee, kons = line.rstrip("\n").split("\t")
        fee = float(fee)
        e = {"dosage_form_strength": prep, "price_low": fee, "price_high": fee, "unit": unit_of(prep), "currency": "PHP",
             "price_type": "philhealth_gamot_fixed_fee", "source": GAMOT["source"], "source_date": GAMOT["date"],
             "notes": ["PhilHealth GAMOT fixed fee paid to the accredited GAMOT pharmacy per unit dispensed"]}
        add(mol, e)
        n_gamot += 1

    # optional newer DPRI exports (e.g. dpri_2026.tsv fetched on a Philippine connection)
    for path in sorted(glob.glob(os.path.join(SRC, "dpri_*.tsv"))):
        meta = {}
        for line in open(path, encoding="utf-8"):
            if line.startswith("#"):
                k, _, v = line[1:].partition(":")
                meta[k.strip()] = v.strip()
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 3 or cols[0] == "drugname":
                continue
            desc, lo, hi = cols[0], float(cols[1].replace(",", "")), float(cols[2].replace(",", ""))
            name = dpri_name(desc)
            add(name, {"dosage_form_strength": desc, "price_low": lo, "price_high": hi, "unit": unit_of(desc),
                       "currency": "PHP", "price_type": "dpri_range", "source": meta.get("source", os.path.basename(path)),
                       "source_date": meta.get("date", "")})

    for v in prices.values():
        v.sort(key=lambda e: (e["source_date"]), reverse=True)
    result = {"_meta": {
        "description": "Philippine government medicine price references keyed by generic slug: DOH Drug Price Reference Index (procurement) and PhilHealth GAMOT fixed fees (reimbursement). Not retail prices.",
        "sources": [DPRI_2021["source"], GAMOT["source"]],
        "as_of": {"dpri": DPRI_2021["date"], "philhealth_gamot": GAMOT["date"]},
        "built_by": "tools/drugdb/build_prices.py", "see": "data/drugs/SOURCES.md",
        "counts": {"generics": len(prices), "dpri_rows": n_dpri, "gamot_rows": n_gamot,
                   "matched_to_generics_json": sum(1 for k in prices if k in res.generics)}}}
    result.update(dict(sorted(prices.items())))
    with open(os.path.join(REPO, "data", "drugs", "prices.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(json.dumps(result["_meta"]["counts"]))
    if args.report:
        print(f"{len(unmatched)} rows not matched to a registry generic:")
        for u in sorted(set(unmatched)):
            print("  ", u)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    main(ap.parse_args())
