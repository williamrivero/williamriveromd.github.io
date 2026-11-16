#!/usr/bin/env python3
"""Build data/drugs/controlled.json: Philippine dangerous-drug (S2) and controlled-precursor status per generic.

Input
  tools/drugdb/sources/ddb_schedules.tsv   hand-curated rows, one per scheduled substance with medical use, each
                                            citing the DDB list or Board Regulation that schedules it
  data/drugs/generics.json                  generic slugs + ingredients (from build_registry.py)
  data/drugs/registry/*.json                products (to report dosage forms per matched generic)
  data/drugs/pnf.json                       PNF A1/A2 codes, cross-checked (never merged)
Output
  data/drugs/controlled.json  {as_of, sources[], items: {slug: {category, schedule, rx_form, notes, source_ids[],
                               substances[], combination, review[]}}, unmatched_substances[], pnf_crosscheck[]}

Matching: a TSV row matches a generic when one of its "match" patterns occurs at a word start in any of the
generic's ingredient names (so "ephedrine" does not match pseudoephedrine, and "ketamine" does not match
esketamine). A combination containing a scheduled substance inherits the substance's status, because
BR 1 s.2014 Sec. 4(1) subjects preparations to the same controls as the controlled substance they contain unless
the Board exempts them. When a combination holds both a dangerous drug and a controlled precursor, the dangerous
drug wins (BR 4 s.2005 Sec. 3 states the same for ephedrine/pseudoephedrine combined with a dangerous drug).
Nothing here is inferred from memory: every rule text below paraphrases the cited section.
"""
import argparse, csv, glob, json, os, re, sys
from collections import defaultdict
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
TSV = os.path.join(HERE, "sources", "ddb_schedules.tsv")

S2 = "S2 — Dangerous drug"
CP = "Controlled precursor / essential chemical"

# id -> source record (rendered as links by generate_drug_pages.py via "title" + "url")
SOURCES = [
    {"id": "ddb-list-2026", "title": "DDB, Updated Lists of Scheduled Controlled Substances (as of 20 July 2026)",
     "issuance": "DDB consolidated list, DDB-LEGAL, 20 July 2026", "date": "2026-07-20",
     "url": "https://ddb.gov.ph/wp-content/uploads/2026/08/2026_7-Updated-Lists-of-controlled-substances.pdf"},
    {"id": "ra9165", "title": "Republic Act No. 9165, Comprehensive Dangerous Drugs Act of 2002",
     "issuance": "RA 9165, Sec. 3(j) (dangerous drugs), Secs. 18-19 (prescriptions), Sec. 93 (reclassification)",
     "date": "2002-06-07", "url": "https://ddb.gov.ph/wp-content/uploads/2022/01/RA-9165.pdf"},
    {"id": "br1-2014", "title": "DDB Board Regulation No. 1, s. 2014 (amending BR 3 s. 2003: licensing, prescriptions, exemptions)",
     "issuance": "Board Regulation No. 1, Series of 2014", "date": "2014-06-19",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2014/BD.REG1.14.pdf"},
    {"id": "br3-2020", "title": "DDB Board Regulation No. 3, s. 2020 (CBD drug products; defines Philippine Schedules 1-4)",
     "issuance": "Board Regulation No. 3, Series of 2020", "date": "2020-09-24",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2020/BOARD_REG_NO._3_S._2020.pdf"},
    {"id": "br1-2020", "title": "DDB Board Regulation No. 1, s. 2020 (immediate adoption of UN scope-of-control changes)",
     "issuance": "Board Regulation No. 1, Series of 2020", "date": "2020-06-18",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2020/2020-BRD._REG.__1_-_Immediate_Adoption_of_Changes_in_the_Scope_of_Control_of_Substance_Pursuant_to_the_Three_3_United_Nation_International_Drug_Conve.pdf"},
    {"id": "br10-2025", "title": "DDB Board Regulation No. 10, s. 2025 (temporary authorization of ordinary prescriptions for dangerous drugs)",
     "issuance": "Board Regulation No. 10, Series of 2025", "date": "2025-06-26",
     "url": "https://ddb.gov.ph/wp-content/uploads/2025/07/BOARD-REGULATION-NO.-10-SERIES-OF-2025_Preemptive-Response-to-Emerging-Public-Health-Concerns-through-Temporary-Authorization-of-Ordinary-Prescriptions-for-Dangerous-Drugs-2.pdf"},
    {"id": "br5-2026", "title": "DDB Board Regulation No. 5, s. 2026 (ordinary prescriptions for dangerous drugs extended to June 30, 2027)",
     "issuance": "Board Regulation No. 5, Series of 2026", "date": "2026-06-23",
     "url": "https://ddb.gov.ph/wp-content/uploads/2026/06/Board-Regulation-No.-5-Series-of-2026.pdf"},
    {"id": "br3-2005", "title": "DDB Board Regulation No. 3, s. 2005 (inclusion of ketamine)",
     "issuance": "Board Regulation No. 3, Series of 2005", "date": "2005-07-19",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2005/Bd.%20Reg.%203%2005.pdf"},
    {"id": "br4-2005", "title": "DDB Board Regulation No. 4, s. 2005 (ephedrine and pseudoephedrine reclassified as dangerous drugs)",
     "issuance": "Board Regulation No. 4, Series of 2005", "date": "2005-07-19",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2005/Bd.%20Reg.%204%2005.pdf"},
    {"id": "br1-2018", "title": "DDB Board Regulation No. 1, s. 2018 (amending BR 4 s. 2005: isomers, halogenated and alkylated forms)",
     "issuance": "Board Regulation No. 1, Series of 2018", "date": "2018-01-24",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2018/2018_Board_Regulation_No._1_-__RECLASSIFYING_EPHEDRINE_AND_PSUEDOEPHERINE.pdf"},
    {"id": "br2-2013", "title": "DDB Board Regulation No. 2, s. 2013 (inclusion of methylephedrine)",
     "issuance": "Board Regulation No. 2, Series of 2013", "date": "2013-09-12",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2013/BD.REG2%2013.pdf"},
    {"id": "br1-2010", "title": "DDB Board Regulation No. 1, s. 2010 (inclusion of nalbuphine hydrochloride)",
     "issuance": "Board Regulation No. 1, Series of 2010", "date": "2010-12-16",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2010/BD.REG1%20%2010.pdf"},
    {"id": "br5-2021", "title": "DDB Board Regulation No. 5, s. 2021 (ordinary triplicate prescription for esketamine nasal spray)",
     "issuance": "Board Regulation No. 5, Series of 2021", "date": "2021-07-29",
     "url": "https://ddb.gov.ph/images/Board_Regulation/2021/BOARD_REG_NO._5_S._2021.pdf"},
]

# Shared sentence on the 2025-2027 temporary authorization (BR 10 s.2025 Secs. 2-6; BR 5 s.2026 Sec. 3)
TEMP = ("Until June 30, 2027, S-2 licensed practitioners may use an ordinary prescription in triplicate instead of the "
        "special form (one dangerous drug per prescription, \"NO REFILL\", up to 30 days; 60 days for Philippine "
        "Schedule 4 drugs in epilepsy and dystonia) (BR 10 s.2025, extended by BR 5 s.2026).")
STD = ("PDEA S-2 license required. DOH Special Prescription Form for dangerous drugs (yellow), in triplicate, one "
       "dangerous drug per prescription, no refill, up to a 30-day supply (BR 1 s.2014 Sec. 31(2), 31(6)(d)). ")
RULES = {
    "DD_STANDARD": STD + TEMP,
    "DD_SCH4": ("PDEA S-2 license required. Oral FDA-registered Philippine Schedule 4 preparations: ordinary prescription "
                "in triplicate (BR 1 s.2014 Sec. 4(4)(a)); other forms: DOH Special Prescription Form (yellow) "
                "(Sec. 31(2)). No refill; up to a 30-day supply, 60 days for epilepsy and dystonia (Sec. 31(6)(d)-(e)). "
                + TEMP),
    "DD_SCH5": ("PDEA S-2 license required. Philippine Schedule 5 (BR 1 s.2014 Sec. 2(2)): oral FDA-registered "
                "preparations by ordinary prescription in triplicate (Sec. 4(4)(a)); other forms on the DOH Special "
                "Prescription Form (yellow) (Sec. 31(2)); Schedule 5 drugs are \"prescribed as necessary\" "
                "(Sec. 31(6)(f)). No refill. " + TEMP),
    "DD_EPHEDRINES": ("PDEA S-2 license required. Never sold over the counter or distributed as physician's samples "
                      "(BR 4 s.2005 Sec. 4). Philippine Schedule 5 (BR 1 s.2014 Sec. 2(2)): oral FDA-registered "
                      "preparations by ordinary prescription in triplicate (Sec. 4(4)(a)); injectables on the DOH Special "
                      "Prescription Form (yellow). " + TEMP),
    "DD_KETAMINE": (STD + "BR 3 s.2005 Sec. 2: a preparation prescribed by a licensed practitioner is excepted from "
                    "Sec. 1 if each vial holds not more than 50 mg/mL x 10 mL and the single prescription is for at most "
                    "1.5 g (three vials) per day for not more than 30 days. " + TEMP),
    "DD_ESKETAMINE": ("PDEA S-2 license required. Esketamine single-use nasal spray device for treatment-resistant "
                      "depression: ordinary prescription in triplicate (BR 5 s.2021); all other regulatory measures apply."),
    "DD_NALBUPHINE": ("Prescribed only by a practitioner with a valid S-2 license on the DOH special prescription form, "
                      "maximum 40 mg nalbuphine hydrochloride per prescription (BR 1 s.2010 Sec. 2). " + TEMP),
    "DD_BUPRENORPHINE": ("PDEA S-2 license required. Buprenorphine patches (Philippine Schedule 3): ordinary prescription "
                         "in triplicate bearing the S-2 license (BR 1 s.2014 Sec. 4(2)(b)); other forms on the DOH Special "
                         "Prescription Form (yellow). " + TEMP),
    "DD_CBD": ("Only S-2 licensed physicians who are members of neurology specialty divisions or societies may prescribe, "
               "on the DOH Special Prescription Form; DDB authorization is required with the FDA Compassionate Special "
               "Permit application (BR 3 s.2020 Secs. 3-5)."),
    "CP_ORAL_EXEMPT": ("FDA-registered oral preparations are exempt from all DDB regulatory requirements except "
                       "registration and licensing of the importer, exporter and manufacturer; prescription and dispensing "
                       "follow FDA rules (BR 1 s.2014 Sec. 4(5)). Parenteral preparations are not covered by this exemption "
                       "(Sec. 4(2)(c)(i)); prescribing a drug preparation containing a controlled chemical otherwise "
                       "requires a PDEA S-2 license (Sec. 6(3))."),
    "CP_PERMANGANATE": ("Compounded galenical solutions intended as disinfectant, antibacterial or antifungal agents are "
                        "exempt from all DDB regulatory requirements except registration and licensing of the importer, "
                        "exporter and manufacturer (BR 1 s.2014 Sec. 4(5))."),
}

# Substance-level exemptions for combination products, as the regulations state them
COMBO_NOTES = {
    "DD_EPHEDRINES": ("BR 4 s.2005 Sec. 2 exempts a preparation from classification as a dangerous drug only if it is "
                      "compounded to present negligible abuse risk, the ephedrine/pseudoephedrine cannot be readily "
                      "extracted, it contains enough other non-narcotic active ingredient to prevent potentiation, it has "
                      "no narcotic or psychotropic substance, and it is not injectable. BR 1 s.2018 later amended Sec. 1 to "
                      "cover \"any material, compound, mixture or preparation containing the same\" and did not restate "
                      "Sec. 2. Whether a given combination holds a DDB exemption is product-specific (BR 1 s.2014 Sec. 4(9)); "
                      "the OTC ban in Sec. 4 applies regardless."),
    "DD_SCH4": ("BR 1 s.2014 Sec. 4(2)(a) lets the Board exempt a Schedule 4/5 preparation from specific controls only "
                "if it is non-parenteral, contains one dangerous drug, the drug cannot be readily recovered, and the "
                "exemption serves a medical purpose; no exemption is listed for this combination."),
}
DEFAULT_COMBO_NOTE = ("Combination preparations are subject to the same controls as the dangerous drug they contain "
                      "unless the Board exempts them (BR 1 s.2014 Sec. 4(1)).")


def load_rows():
    rows = []
    with open(TSV, encoding="utf-8") as f:
        lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    for r in csv.DictReader(lines, delimiter="\t"):
        r = {k: (v or "").strip() for k, v in r.items()}
        if r["rule"] not in RULES:
            sys.exit(f"unknown rule {r['rule']!r} for {r['substance']}")
        r["patterns"] = [re.compile(r"(?<![a-z])" + re.escape(m.strip()).replace(r"\ ", r"[\s-]+"))
                         for m in r["match"].split(";") if m.strip()]
        r["source_ids"] = [s for s in r["source_ids"].split(";") if s]
        rows.append(r)
    return rows


def pnf_codes(pnf):
    out = {}
    for slug, v in pnf.items():
        if slug.startswith("_") or not isinstance(v, dict):
            continue
        codes = set()
        for e in v.get("pnf_entries") or []:
            for n in e.get("restriction_notes") or []:
                m = re.search(r"PNF code (A1|A2)", n)
                if m:
                    codes.add(m.group(1))
        out[slug] = sorted(codes)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default=os.path.join(REPO, "data", "drugs"))
    ap.add_argument("--as-of", default="2026-07-20", help="date of the DDB consolidated list used")
    a = ap.parse_args()
    rows = load_rows()
    src_ids = {s["id"] for s in SOURCES}
    for r in rows:
        bad = [s for s in r["source_ids"] if s not in src_ids]
        if bad:
            sys.exit(f"{r['substance']}: unknown source ids {bad}")
    generics = json.load(open(os.path.join(a.data_dir, "generics.json"), encoding="utf-8"))
    forms = defaultdict(set)
    for f in glob.glob(os.path.join(a.data_dir, "registry", "*.json")):
        for p in json.load(open(f, encoding="utf-8")):
            forms[p["generic_slug"]].add(re.sub(r"\s+", " ", p.get("dosage_strength_form") or "").strip())

    items, matched_rows = {}, set()
    for slug, g in sorted(generics.items()):
        ings = [i.lower() for i in (g.get("ingredients") or [])]
        hits = []
        for r in rows:
            if any(pat.search(i) for i in ings for pat in r["patterns"]):
                hits.append(r)
        if not hits:
            continue
        for r in hits:
            matched_rows.add(r["substance"])
        dd = [r for r in hits if r["kind"] == "DD"]
        lead = dd or hits
        combo = len(ings) > 1
        sids = []
        for r in lead:
            for s in r["source_ids"]:
                if s not in sids:
                    sids.append(s)
        notes = [r["note"] for r in lead if r["note"]]
        review = []
        if combo:
            rule = lead[0]["rule"]
            notes.append(COMBO_NOTES.get(rule, DEFAULT_COMBO_NOTE) if lead[0]["kind"] == "DD" else
                         "The precursor exemption for oral FDA-registered preparations applies to combinations as well "
                         "(BR 1 s.2014 Sec. 4(5)).")
            if rule == "DD_EPHEDRINES":
                review.append("Combination containing ephedrine/pseudoephedrine: confirm whether the product holds a DDB "
                              "certificate of exemption (BR 4 s.2005 Sec. 2) before treating it as S2.")
        if dd and len(hits) > len(dd):
            notes.append("Also contains a controlled precursor (" + ", ".join(r["substance"] for r in hits if r["kind"] == "CP")
                         + "); the dangerous-drug controls govern the preparation.")
        rset = {r["rule"] for r in lead}
        if "CP_ORAL_EXEMPT" in rset:
            par = sorted(f for f in forms.get(slug, ()) if re.search(r"inject|ampul|ampoule|vial|parenteral|i\.?v\b|i\.?m\b", f, re.I))
            if par:
                review.append("Registered parenteral form(s) fall outside the oral-preparation exemption: " + "; ".join(par[:4]))
        if any(r["substance"] == "Carisoprodol" for r in lead):
            review.append("Carisoprodol was added to 1971 Schedule IV on the DDB list dated 6 December 2025; registered "
                          "products may still carry their earlier Rx classification. Confirm the PDEA/FDA implementation date.")
        if "DD_ESKETAMINE" in rset:
            review.append("BR 5 s.2021 covers only the single-use nasal spray device; other esketamine forms would take the "
                          "standard dangerous-drug rules.")
        rx_form = " ".join(dict.fromkeys(RULES[r["rule"]] for r in lead))
        items[slug] = {
            "category": S2 if dd else CP,
            "schedule": "; ".join(dict.fromkeys(r["schedule"] for r in lead)),
            "rx_form": rx_form,
            "notes": " ".join(notes),
            "source_ids": sids,
            "substances": [r["substance"] for r in hits],
            "combination": combo,
        }
        if review:
            items[slug]["review"] = review

    # PNF cross-check (reported, never merged)
    pnf = json.load(open(os.path.join(a.data_dir, "pnf.json"), encoding="utf-8"))
    codes = pnf_codes(pnf)
    cross = []

    def status_of(slug):
        """DD / CP / '' for a PNF slug, matched against the curated rows directly (the PNF lists generics that may
        have no registered product, so generics.json is not consulted)."""
        name = slug.replace("-", " ")
        kinds = {r["kind"] for r in rows if any(p.search(name) for p in r["patterns"])}
        return "S2" if "DD" in kinds else ("CP" if "CP" in kinds else "")

    for slug, cs in sorted(codes.items()):
        mine = status_of(slug)
        if "A1" in cs and mine != "S2":
            cross.append({"slug": slug, "pnf": cs, "ddb": mine or None,
                          "issue": "PNF marks A1 (dangerous drug) but the substance is not on the DDB consolidated list "
                                   "as of " + a.as_of + " or in any DDB Board Regulation used here."})
        elif "A2" in cs and mine == "CP":
            cross.append({"slug": slug, "pnf": cs, "ddb": mine,
                          "issue": "PNF A2 says personalized prescription with S2 license; BR 1 s.2014 Sec. 4(5) exempts "
                                   "FDA-registered oral preparations from DDB requirements (prescribing per FDA rules). "
                                   "The PNF note may predate or not reflect that exemption."})
        elif "A2" in cs and mine != "CP":
            cross.append({"slug": slug, "pnf": cs, "ddb": mine or None,
                          "issue": "PNF marks A2 (controlled chemical) but no DDB controlled-precursor listing matched."})
        elif mine == "S2" and "A1" not in cs or (mine == "CP" and not cs):
            cross.append({"slug": slug, "pnf": cs, "ddb": mine,
                          "issue": "Listed in the PNF without an A1/A2 code although the DDB controls it "
                                   "(PNF additions lists may omit codes)."})
        if slug in items and mine and items[slug]["category"] != (S2 if mine == "S2" else CP):
            cross.append({"slug": slug, "pnf": cs, "ddb": mine, "issue": "internal mismatch"})

    unmatched = [r["substance"] for r in rows if r["substance"] not in matched_rows]
    out = {
        "as_of": a.as_of,
        "built": date.today().isoformat(),
        "built_by": "tools/drugdb/build_controlled.py from tools/drugdb/sources/ddb_schedules.tsv",
        "description": ("Philippine dangerous-drug (S2) and controlled-precursor status by generic, from the Dangerous "
                        "Drugs Board's consolidated schedules and Board Regulations. Generics not listed here follow "
                        "their FDA Philippines registration classification (Rx / OTC / HR). Not legal advice; confirm "
                        "with PDEA and the DDB."),
        "see": "data/drugs/SOURCES.md",
        "sources": SOURCES,
        "counts": {"generics": len(items), "s2": sum(1 for x in items.values() if x["category"] == S2),
                   "precursor": sum(1 for x in items.values() if x["category"] == CP),
                   "substances_curated": len(rows), "substances_matched": len(matched_rows)},
        "items": items,
        "unmatched_substances": unmatched,
        "pnf_crosscheck": cross,
    }
    path = os.path.join(a.data_dir, "controlled.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"controlled generics {len(items)} (S2 {out['counts']['s2']}, precursor {out['counts']['precursor']}); "
          f"substances matched {len(matched_rows)}/{len(rows)}; PNF cross-check issues {len(cross)} -> {path}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
