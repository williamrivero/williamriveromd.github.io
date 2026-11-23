#!/usr/bin/env python3
"""Fetch PubMed metadata for any reference PMID not yet in data/nursing-course/refs_pubmed_raw.json.

    python3 tools/nursing/fetch_refs.py

Reads PUBMED_REFS in content/common.py and NEW_REFS in every content/mNN_x.py.
Prints each new record so the title, journal and year can be checked by eye.
"""
import importlib.util, json, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "tools/nursing/content"
RAW = ROOT / "data/nursing-course/refs_pubmed_raw.json"

def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

want = dict(load(CONTENT / "common.py").PUBMED_REFS)
for f in sorted(CONTENT.glob("m??_x.py")):
    want.update(getattr(load(f), "NEW_REFS", {}))
raw = json.loads(RAW.read_text(encoding="utf-8"))
missing = sorted({p for p in want.values() if p not in raw})
if not missing:
    print("nothing to fetch"); raise SystemExit
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(missing)
res = json.loads(urllib.request.urlopen(url, timeout=40).read())["result"]
for p in missing:
    a = res[p]
    doi = [x["value"] for x in a["articleids"] if x["idtype"] == "doi"]
    raw[p] = {"authors": [x["name"] for x in a["authors"]], "title": a["title"], "journal": a["fulljournalname"],
              "year": a["pubdate"][:4], "volume": a["volume"], "issue": a["issue"], "pages": a["pages"], "doi": doi[0] if doi else ""}
    print(p, "|", raw[p]["authors"][:1], len(raw[p]["authors"]), "|", a["title"], "|", a["fulljournalname"], a["pubdate"], a["volume"], a["issue"], a["pages"], "|", raw[p]["doi"])
RAW.write_text(json.dumps(raw, indent=1, ensure_ascii=False), encoding="utf-8")
