#!/usr/bin/env python3
"""Build data/drugs/pnf.json from official Philippine National Formulary (PNF) and PhilHealth GAMOT sources.

Inputs (all under tools/drugdb/sources/):
  raw/PNF-EML_11022022.txt     pdftotext -layout of the PNF Essential Medicines List, 8th ed. (as of Nov 2, 2022),
                               hosted by PhilHealth (fetched by .github/workflows/drugdb-fetch-pnf-prices.yml)
  pnf_additions.json           medicines added to the PNF after Nov 2022, transcribed from PhilHealth advisories
                               PA2024-0026, PA2025-0013 and PA2025-0060 (each row keeps its DOH Department Circular)
  gamot_list.json              PhilHealth GAMOT List (PC2025-0013 Annex A.i, plus later circulars)

Output: data/drugs/pnf.json
  {slug: {in_pnf: bool, pnf_names: [...], pnf_entries: [{dosage_form_strength, restriction_notes, source,
          source_date}], philhealth_gamot: bool|null, gamot_source: str|null}}

Slugs come from tools/drugdb/build_registry.py (ingredients_of / slug_of) so keys match generics.json.
Usage:  python3 tools/drugdb/build_pnf.py [--report]
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_registry import ingredients_of, slug_of  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(HERE, "sources")
PNF_TXT = os.path.join(SRC, "raw", "PNF-EML_11022022.txt")
PNF_SOURCE = "PNF Essential Medicines List, 8th ed. (as of November 2, 2022), DOH; https://www.philhealth.gov.ph/partners/providers/pdf/PNF-EML_11022022.pdf"
PNF_DATE = "2022-11-02"

CODE_NOTES = {
    "1": "Specific expertise, diagnostic precision, or special equipment required for proper use (PNF code 1)",
    "2": "Limited indications or narrow spectrum of activity (PNF code 2)",
    "A1": "Dangerous drug: DOH Official Prescription Form (yellow Rx), S2 license, no refill (PNF code A1)",
    "A2": "Contains controlled chemicals: personalized prescription with S2 license, no refill (PNF code A2)",
    "B": "List B: in vivo bioequivalence studies required (PNF code B)",
}
# Reserve antimicrobials (PNF EML, "Reserve Antimicrobials" annex)
RESERVE = {"aztreonam", "cefepime", "colistin", "ertapenem", "linezolid", "meropenem", "vancomycin",
           "amphotericin b", "micafungin", "voriconazole"}
RESERVE_NOTE = "Reserve antimicrobial (PNF)"

# PNF spellings that differ from the PH FDA registry spelling (checked against generics.json)
SPELLING = {
    "lumefantrin": "lumefantrine", "anastrazole": "anastrozole", "polymixin b": "polymyxin b",
    "tenofuvir": "tenofovir", "dapirivine": "dapivirine", "flouride": "fluoride",
}
# PNF headings that are cross-references or not medicines
SKIP_NAME = re.compile(r"\(see\b|^vitamin intravenous", re.I)

ROUTE = re.compile(r"^(?:[A-Z][A-Za-z.\-/ ]{0,40}?|Inj)\s*:\s*")
MARKERS = re.compile(r"\((?:\s*(?:1|2|A1|A2|B)\s*,?)+\)|\(1\b|[●⊗+]$")


def clean_name(name):
    """Strip PNF code markers and notes from a heading; return (name, codes, reserve)."""
    codes = set()
    for m in re.finditer(r"\(([^()]*)\)", name):
        toks = [t.strip() for t in m.group(1).split(",")]
        if toks and all(t in CODE_NOTES for t in toks):
            codes.update(toks)
    reserve = "reserve antimicrobial" in name.lower()
    n = re.sub(r"\((?:\s*(?:1|2|A1|A2|B)\s*,?\s*)+\)", " ", name)
    n = re.sub(r"\(\s*1\s*$", " ", n)                       # "Vecuronium (as bromide) (1" (cut off)
    n = re.sub(r"\(Inj\.?\s*-\s*\*Reserve.*$", " ", n, flags=re.I)
    n = re.sub(r"\*Reserve Antimicrobial", " ", n, flags=re.I)
    n = n.replace("●", " ").replace("⊗", " ").replace("‐", "-")
    n = re.sub(r"\s+", " ", n).strip(" ,")
    return n, codes, reserve


def form_codes(text):
    codes = set()
    for m in re.finditer(r"\(([^()]*)\)", text):
        toks = [t.strip() for t in m.group(1).split(",")]
        if toks and all(t in CODE_NOTES for t in toks):
            codes.update(toks)
    return codes


def usage_notes(text):
    """Parenthetical program/facility restrictions written into a form line."""
    out = []
    for m in re.finditer(r"\(([^()]{12,})\)", text):
        t = m.group(1)
        if re.search(r"\b(only|restricted|program|for use|use by|maintenance therapy|available under)\b", t, re.I):
            out.append(re.sub(r"\s+", " ", t).strip())
    return out


def tidy_form(text):
    t = re.sub(r"\((?:\s*(?:1|2|A1|A2|B)\s*,?\s*)+\)", " ", text)
    t = t.replace("⊗", "").replace("●", "").replace("‐", "-")
    return re.sub(r"\s+", " ", t).strip(" ;")


def split_cols(line):
    """PNF lines: name column from col 0, forms column after a gap of >=2 spaces (starting col >= 20)."""
    if not line.strip():
        return None, None, 0
    indent = len(line) - len(line.lstrip(" "))
    if indent >= 8:
        return None, line.strip(), indent
    s = line.strip()
    m = re.search(r"\s{2,}", s)
    if m and m.end() + indent >= 20:
        return s[:m.start()].strip(), s[m.end():].strip(), indent
    # single-space join like "Atropine (as sulfate) (1, 2)    Oral: 600" handled above; "Artemether (B)    Oral: 20 mg"
    m = re.search(r"\s(Oral|Inj\.?|Inhalation|Rectal|Topical|Ointment|Cream|Lotion|Gel|Eye Drops|Ear Drops|Nasal|Vaginal)\b.*?:", s)
    if m and m.start() >= 6:
        return s[:m.start()].strip(), s[m.start():].strip(), indent
    return s, None, indent


def parse_pnf(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip().startswith("Active Ingredient"))
    end = next(i for i, l in enumerate(lines) if "FREQUENTLY ASKED QUESTIONS" in l)
    entries = []          # [{name, codes, reserve, routes: [{route, items: [str]}]}]
    cur = None
    name_open = False     # previous line was part of the name block

    def add_form(text, indent):
        nonlocal cur
        if cur is None or not text:
            return
        rm = ROUTE.match(text)
        if rm and not re.match(r"^\d", text):
            route = rm.group(0).strip().rstrip(":").strip()
            rest = text[rm.end():].strip()
            cur["routes"].append({"route": route, "items": [], "item_indent": None})
            if rest:
                cur["routes"][-1]["items"].append(rest)
            return
        if not cur["routes"]:
            cur["routes"].append({"route": "", "items": [], "item_indent": None})
        r = cur["routes"][-1]
        starts_item = bool(re.match(r"^[⊗●]?\s*\d", text)) or (r["item_indent"] is not None and indent <= r["item_indent"])
        if not r["items"] or starts_item:
            if r["items"] and r["item_indent"] is None:
                r["item_indent"] = indent
            r["items"].append(text)
        else:
            r["items"][-1] += " " + text

    for raw in lines[start:end]:
        line = raw.replace("\f", "")
        st = line.strip()
        if not st or st.startswith(("Active Ingredient", "Route of Administration", "Pharmaceutical Forms")):
            name_open = False if not st else name_open
            continue
        if re.fullmatch(r"[A-Z]", st) or re.fullmatch(r"\d{1,3}", st):
            name_open = False
            continue
        if st.startswith("*Reserve Antimicrobial") and len(st) < 40:
            continue
        left, right, indent = split_cols(line)
        if left is not None:
            new_entry = True
            if cur is not None and name_open:
                # continuation of a wrapped name: no route on the right, or name still has an open paren
                unbalanced = cur["raw"].count("(") > cur["raw"].count(")")
                lower = left[:1].islower() or left.startswith(("(", "+", "-"))
                right_is_cont = right is None or not ROUTE.match(right or "")
                if unbalanced or lower or cur["raw"].rstrip().endswith(("+", "-", ",", "/")) or (right_is_cont and right is not None and not re.match(r"^\d", right)):
                    new_entry = False
                elif right is None and not cur["routes"]:
                    new_entry = False
            if new_entry:
                cur = {"raw": left, "routes": []}
                entries.append(cur)
            else:
                cur["raw"] += " " + left
            name_open = True
            if right:
                add_form(right, 40)
        else:
            name_open = False
            add_form(right, indent)
    return entries


def build(args):
    generics = json.load(open(os.path.join(REPO, "data", "drugs", "generics.json")))
    out = {}

    def rec(slug):
        return out.setdefault(slug, {"in_pnf": True, "pnf_names": [], "pnf_entries": [],
                                     "philhealth_gamot": False, "gamot_source": None})

    def to_slug(name):
        n = name
        for a, b in SPELLING.items():
            n = re.sub(r"\b%s\b" % re.escape(a), b, n, flags=re.I)
        return slug_of(ingredients_of(n)), ingredients_of(n)

    unmatched = []
    for e in parse_pnf(PNF_TXT):
        name, codes, reserve = clean_name(e["raw"])
        if not name or SKIP_NAME.search(e["raw"]):
            continue
        slug, ings = to_slug(name)
        if slug == "unknown":
            continue
        if any(i in RESERVE for i in ings) and len(ings) == 1:
            reserve = True
        r = rec(slug)
        if name not in r["pnf_names"]:
            r["pnf_names"].append(name)
        if slug not in generics:
            unmatched.append((slug, name))
        items = [(rt["route"], it) for rt in e["routes"] for it in rt["items"]] or [("", "")]
        for route, item in items:
            c = codes | form_codes(item)
            notes = [CODE_NOTES[k] for k in ("1", "2", "A1", "A2", "B") if k in c]
            if reserve:
                notes.append(RESERVE_NOTE)
            notes += usage_notes(item)
            dfs = tidy_form(f"{route}: {item}" if route and item else (item or route))
            r["pnf_entries"].append({"dosage_form_strength": dfs, "restriction_notes": notes,
                                     "source": PNF_SOURCE, "source_date": PNF_DATE})

    adds = json.load(open(os.path.join(SRC, "pnf_additions.json")))
    for a in adds["items"]:
        slug, ings = to_slug(a["generic"])
        r = rec(slug)
        if a["generic"] not in r["pnf_names"]:
            r["pnf_names"].append(a["generic"])
        if slug not in generics:
            unmatched.append((slug, a["generic"]))
        src = adds["sources"][a["source"]]
        r["pnf_entries"].append({"dosage_form_strength": a["dosage_form_strength"],
                                 "restriction_notes": a.get("restriction_notes", []),
                                 "source": f'{src["title"]}; {a["department_circular"]} (included {a["date_of_inclusion"]}); {src["url"]}',
                                 "source_date": a["date_of_inclusion"]})

    gam = json.load(open(os.path.join(SRC, "gamot_list.json")))
    gamot_missing = []
    for g in gam["items"]:
        slug, _ = to_slug(g["generic"])
        if slug not in out:
            gamot_missing.append(slug)
            out[slug] = {"in_pnf": None, "pnf_names": [], "pnf_entries": [], "philhealth_gamot": True,
                         "gamot_source": None}
        out[slug]["philhealth_gamot"] = True
        out[slug]["gamot_source"] = gam["sources"][g["source"]]["title"]
        if g.get("note"):
            out[slug]["gamot_note"] = g["note"]

    result = {"_meta": {
        "description": "Philippine National Formulary (PNF) Essential Medicines List status and PhilHealth GAMOT coverage, keyed by generic slug.",
        "pnf_as_of": adds["as_of"], "pnf_base_edition": PNF_SOURCE, "gamot_as_of": gam["as_of"],
        "built_by": "tools/drugdb/build_pnf.py", "see": "data/drugs/SOURCES.md",
        "note": "Absence from this file means the generic was not found in the PNF sources listed; it does not prove exclusion from the live ePNF (pnf.doh.gov.ph).",
        "counts": {"generics": len(out), "in_pnf": sum(1 for v in out.values() if v["in_pnf"]),
                   "philhealth_gamot": sum(1 for v in out.values() if v["philhealth_gamot"]),
                   "matched_to_generics_json": sum(1 for k in out if k in generics)}}}
    result.update(dict(sorted(out.items())))
    path = os.path.join(REPO, "data", "drugs", "pnf.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(json.dumps(result["_meta"]["counts"]))
    if args.report:
        print(f"\n{len(set(unmatched))} PNF slugs not in generics.json:")
        for s, n in sorted(set(unmatched)):
            print(f"  {s:45s} <- {n}")
        print("GAMOT items not found in PNF parse:", gamot_missing)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="list PNF names that do not match a registry generic")
    build(ap.parse_args())
