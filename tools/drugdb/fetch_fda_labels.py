#!/usr/bin/env python3
"""Fetch the best US FDA drug label (openFDA) for every generic in the drug database.

Workstream B of the renalcarematters.com Drug Database.

Input   data/drugs/generics.json   {slug: {name, ingredients[], products, categories[]}}
Output  data/drugs/labels/<slug>.json   one file per matched generic
        data/drugs/labels/_missing.json slugs with no matching US label
        data/drugs/labels/_changes.json slugs added or changed in this run (weekly review list)

Two sources:
  --source api   openFDA search API, one paged query per generic (fine for a few hundred)
  --source bulk  openFDA bulk download (all label partitions, streamed); no daily cap
  --source auto  (default) api for <= 200 generics, bulk otherwise

Matching: a label matches a generic when every label substance (openfda.substance_name,
falling back to openfda.generic_name) is one of the generic's ingredients and every
ingredient is present. A substance matches an ingredient when the ingredient's words are
all in the substance name and every extra word is a salt/hydrate word
("amlodipine" ~ "AMLODIPINE BESYLATE", "dapagliflozin" ~ "DAPAGLIFLOZIN PROPANEDIOL").
Biosimilar suffixes ("EPOETIN ALFA-EPBX") do NOT match the reference product's generic.

Ranking (default --prefer recent, as specified): human Rx before OTC, then the newest
effective_time, then the innovator (application_number NDA/BLA) on a tie.
--prefer innovator puts NDA/BLA before effective_time.

Incremental: a slug whose stored set_id + effective_time is unchanged is not rewritten.
The section text is copied verbatim from the label; nothing is paraphrased.

Standard library only; uses ijson for streaming in bulk mode when it is installed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_GENERICS = REPO / "data" / "drugs" / "generics.json"
DEFAULT_OUT = REPO / "data" / "drugs" / "labels"

API = "https://api.fda.gov/drug/label.json"
DOWNLOAD_MANIFEST = "https://api.fda.gov/download.json"
UA = "RenalCareMattersDrugDB/1.0 (+https://renalcarematters.com)"
MANILA = dt.timezone(dt.timedelta(hours=8))
SCHEMA_VERSION = 1

# Words that may follow (or precede) an ingredient name in an FDA substance name without
# changing the active moiety: counter-ions, esters used as salts, hydrates, forms.
SALT_WORDS = set("""
acetate acetonide anhydrous arginine aspartate benzathine benzoate besylate besilate bicarbonate
bisulfate bitartrate bromide butyrate calcium camsylate carbonate chloride citrate cypionate
decanoate diacetate dihydrate dihydrochloride dimesylate dimaleate dipotassium dipropionate
disodium disoproxil edisylate enanthate erbumine esylate estolate ethanolate ethylsuccinate
fumarate gluceptate gluconate glycinate hcl hemifumarate hemihydrate hemisulfate heptahydrate
hexahydrate hyclate hydrobromide hydrochloride hydrogen hydroxide iodide isethionate lactate
lactobionate lysine magnesium maleate malate mandelate medoxomil megluminate meglumine mesilate
mesylate methylbromide methylsulfate monohydrate mononitrate monosodium napsylate nitrate oxalate
pamoate pentahydrate phosphate potassium propanediol propionate saccharate salicylate sesquihydrate
sodium stearate succinate sulfate sulphate tartrate tebutate teoclate tetrahydrate tosylate
trifenatate trihydrate trometamol tromethamine valerate xinafoate zinc amorphous crystalline
""".split())

SECTION_FIELDS = [
    "boxed_warning",
    "indications_and_usage",
    "dosage_and_administration",
    "dosage_forms_and_strengths",
    "contraindications",
    "warnings_and_cautions",
    "drug_interactions",
    "adverse_reactions",
    "use_in_specific_populations",
    "pregnancy",
    "lactation",
    "overdosage",
    "mechanism_of_action",
    "pharmacokinetics",
]
# label field -> our field, used when the primary field is absent
FALLBACKS = {
    "warnings_and_cautions": ["warnings", "precautions"],
    "lactation": ["nursing_mothers"],
}
META_FIELDS = ["brand_name", "manufacturer_name", "application_number", "route",
               "product_type", "generic_name", "substance_name", "product_ndc", "rxcui"]

RENAL_HEAD = (r"(?:Patients\s+with\s+)?(?:Renal\s+Impairment|Renal\s+Insufficiency|"
              r"Impaired\s+Renal\s+Function|Renal\s+Disease|Kidney\s+Impairment)")
OTHER_POP_HEADS = (r"Hepatic\s+Impairment|Hepatic\s+Insufficiency|Impaired\s+Hepatic|Geriatric|"
                   r"Pediatric|Elderly|Gender|Sex\b|Race\b|Ethnicity|Body\s+Weight|Obesity|Age\b|"
                   r"Drug\s+Interaction|Drug-Drug|Pregnan|Lactation|Nursing|Smok|Heart\s+Failure|"
                   r"Cardiac|Patients\s+with\s+(?!Renal|Kidney|End)")


# --------------------------------------------------------------------------- matching
def tokens(s: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", s.lower()) if t]


def substance_matches(ingredient: str, substance: str) -> bool:
    it, st = tokens(ingredient), tokens(substance)
    if not it or not st:
        return False
    iset, sset = set(it), set(st)
    if not iset <= sset:
        return False
    return (sset - iset) <= SALT_WORDS


def label_substances(label: dict) -> list[str]:
    of = label.get("openfda") or {}
    subs = of.get("substance_name") or []
    if subs:
        return [s for s in subs if s.strip()]
    names = of.get("generic_name") or []
    out: list[str] = []
    for n in names:
        for part in re.split(r",|\s+and\s+|/|\+", n, flags=re.I):
            if part.strip():
                out.append(part.strip())
    return out


def label_matches(ingredients: list[str], substances: list[str]) -> bool:
    if not substances or not ingredients:
        return False
    # every substance must be one of the ingredients (no extras)
    for s in substances:
        if not any(substance_matches(i, s) for i in ingredients):
            return False
    # every ingredient must be present
    for i in ingredients:
        if not any(substance_matches(i, s) for s in substances):
            return False
    return True


class Matcher:
    """Inverted index ingredient word -> generic slugs, for scanning the bulk files."""

    def __init__(self, generics: dict):
        self.generics = generics
        self.index: dict[str, set[str]] = {}
        for slug, g in generics.items():
            for ing in g["ingredients"]:
                words = [t for t in tokens(ing) if t not in SALT_WORDS] or tokens(ing)
                for w in words:
                    self.index.setdefault(w, set()).add(slug)

    def match(self, label: dict) -> list[str]:
        subs = label_substances(label)
        if not subs:
            return []
        cands: set[str] = set()
        for s in subs:
            for w in tokens(s):
                cands |= self.index.get(w, set())
        return [slug for slug in cands
                if label_matches(self.generics[slug]["ingredients"], subs)]


# --------------------------------------------------------------------------- ranking
def first(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


def product_rank(label: dict) -> int:
    pt = " ".join((label.get("openfda") or {}).get("product_type") or []).upper()
    if "PRESCRIPTION" in pt:
        return 0
    if "OTC" in pt:
        return 1
    return 2


def is_innovator(label: dict) -> bool:
    apps = (label.get("openfda") or {}).get("application_number") or []
    return any(a.upper().startswith(("NDA", "BLA")) for a in apps)


def rank_key(label: dict, prefer: str):
    eff = str(label.get("effective_time") or "0")
    inn = 0 if is_innovator(label) else 1
    # sort ascending: smaller is better; negate date via string trick
    eff_key = "".join(chr(255 - ord(c)) for c in eff.ljust(8, "0"))
    if prefer == "innovator":
        return (product_rank(label), inn, eff_key, label.get("id", ""))
    return (product_rank(label), eff_key, inn, label.get("id", ""))


def is_human(label: dict) -> bool:
    pt = " ".join((label.get("openfda") or {}).get("product_type") or []).upper()
    return (not pt) or "HUMAN" in pt


# --------------------------------------------------------------------------- extraction
def join_text(v) -> str:
    if isinstance(v, list):
        return "\n\n".join(x.strip() for x in v if isinstance(x, str) and x.strip())
    return (v or "").strip() if isinstance(v, str) else ""


def extract_renal_from_populations(text: str) -> str:
    # PLR labels: "8.6 Renal Impairment ..." up to the next "8.x " heading
    m = re.search(r"(?:^|\s)(8\.\d+)\s+" + RENAL_HEAD, text)
    if m:
        start = m.start(1)
        nxt = re.search(r"\s8\.\d+\s+[A-Z]", text[m.end():])
        end = m.end() + nxt.start() if nxt else len(text)
        return text[start:end].strip()
    return ""


def extract_renal_from_pk(text: str) -> str:
    # A title-case heading inside clinical pharmacology / pharmacokinetics.
    m = re.search(r"(?:^|[.:)\]]\s+|\n\s*|\s{2,})(" + RENAL_HEAD + r")(?=\s*[:.\-–—]|\s+[A-Z(])", text)
    if not m:
        return ""
    start = m.start(1)
    rest = text[m.end(1):]
    nxt = re.search(r"(?:[.:)\]]\s+|\n\s*|\s{2,})(?:" + OTHER_POP_HEADS + r")[^.]{0,60}?[:.]|\s1[2-9]\.\d+\s+[A-Z]|\s1[3-9]\s+[A-Z]{3}",
                    rest)
    end = m.end(1) + (nxt.start() + 1 if nxt else min(len(rest), 4000))
    return text[start:end].strip()


def build_record(slug: str, g: dict, label: dict, n_candidates: int, prefer: str) -> dict:
    of = label.get("openfda") or {}
    sections: dict[str, str] = {}
    section_sources: dict[str, str] = {}
    for f in SECTION_FIELDS:
        txt = join_text(label.get(f))
        src = f
        if not txt:
            for alt in FALLBACKS.get(f, []):
                txt = join_text(label.get(alt))
                if txt:
                    src = alt
                    break
        if txt:
            sections[f] = txt
            if src != f:
                section_sources[f] = src

    renal: list[dict] = []
    if join_text(label.get("renal_impairment")):
        renal.append({"source": "renal_impairment", "text": join_text(label.get("renal_impairment"))})
    pop = join_text(label.get("use_in_specific_populations"))
    if pop:
        t = extract_renal_from_populations(pop)
        if t:
            renal.append({"source": "use_in_specific_populations", "text": t})
    for f in ("pharmacokinetics", "clinical_pharmacology"):
        t = extract_renal_from_pk(join_text(label.get(f)))
        if t and not any(t in r["text"] or r["text"] in t for r in renal):
            renal.append({"source": f, "text": t})
            break
    if renal:
        sections["renal_impairment"] = "\n\n".join(r["text"] for r in renal)

    set_id = label.get("set_id", "")
    meta = {
        "set_id": set_id,
        "id": label.get("id", ""),
        "version": label.get("version", ""),
        "effective_time": label.get("effective_time", ""),
        "brand_name": first(of.get("brand_name")),
        "manufacturer_name": first(of.get("manufacturer_name")),
        "application_number": first(of.get("application_number")),
        "route": of.get("route") or [],
        "product_type": first(of.get("product_type")),
        "generic_name": first(of.get("generic_name")),
        "substance_name": of.get("substance_name") or [],
        "innovator": is_innovator(label),
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": slug,
        "name": g.get("name", slug),
        "ingredients": g["ingredients"],
        "source": {
            "publisher": "U.S. Food and Drug Administration",
            "via": "openFDA drug label endpoint",
            "dailymed_url": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={set_id}" if set_id else "",
            "api_url": f"{API}?search=set_id:%22{set_id}%22" if set_id else "",
            "license_note": "U.S. government work; label text reproduced verbatim.",
        },
        "selection": {"candidates": n_candidates, "rule": prefer},
        "label": meta,
        "sections": sections,
        "section_sources": section_sources,
        "renal_impairment_sources": renal,
        "fetched_at": dt.datetime.now(MANILA).isoformat(timespec="seconds"),
    }


# --------------------------------------------------------------------------- network
def http_get(url: str, retries: int = 5, timeout: int = 120) -> bytes:
    delay = 2.0
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return b""
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    return b""


class Api:
    def __init__(self, key: str | None, min_interval: float):
        self.key = key
        self.min_interval = min_interval
        self.last = 0.0
        self.requests = 0

    def get(self, params: dict) -> dict:
        wait = self.min_interval - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        if self.key:
            params = {**params, "api_key": self.key}
        url = API + "?" + urllib.parse.urlencode(params, safe=':+"()')
        self.last = time.time()
        self.requests += 1
        raw = http_get(url)
        return json.loads(raw) if raw else {}


def api_candidates(api: Api, g: dict, max_pages: int) -> list[dict]:
    clauses = []
    for ing in g["ingredients"]:
        words = [t for t in tokens(ing) if t not in SALT_WORDS] or tokens(ing)
        phrase = " ".join(words)
        clauses.append(f'(openfda.substance_name:"{phrase}"+openfda.generic_name:"{phrase}")')
    search = "+AND+".join(clauses)
    out: list[dict] = []
    for page in range(max_pages):
        data = api.get({"search": search, "limit": 100, "skip": page * 100})
        res = data.get("results") or []
        out.extend(res)
        total = (data.get("meta") or {}).get("results", {}).get("total", 0)
        if len(res) < 100 or (page + 1) * 100 >= total:
            break
    return out


def run_api(generics: dict, args) -> tuple[dict, dict]:
    api = Api(os.environ.get("OPENFDA_API_KEY") or None, args.min_interval)
    best: dict[str, dict] = {}
    counts: dict[str, int] = {}
    for n, (slug, g) in enumerate(sorted(generics.items()), 1):
        try:
            labels = api_candidates(api, g, args.max_pages)
        except Exception as e:  # keep going; record as a miss with the reason
            print(f"[{n}/{len(generics)}] {slug}: ERROR {e}", file=sys.stderr)
            counts[slug] = -1
            continue
        good = [l for l in labels if is_human(l) and label_matches(g["ingredients"], label_substances(l))]
        counts[slug] = len(good)
        if good:
            best[slug] = min(good, key=lambda l: rank_key(l, args.prefer))
        print(f"[{n}/{len(generics)}] {slug}: {len(labels)} returned, {len(good)} matched")
    print(f"openFDA requests: {api.requests}")
    return best, counts


def iter_bulk_labels(path: Path):
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.endswith(".json"):
                continue
            with z.open(name) as fh:
                try:
                    import ijson  # type: ignore
                    yield from ijson.items(fh, "results.item", use_float=True)
                except ImportError:
                    data = json.load(io.TextIOWrapper(fh, encoding="utf-8"))
                    yield from data.get("results", [])
                    del data


def run_bulk(generics: dict, args) -> tuple[dict, dict]:
    manifest = json.loads(http_get(DOWNLOAD_MANIFEST))
    parts = manifest["results"]["drug"]["label"]["partitions"]
    print(f"bulk: {len(parts)} partitions, export date "
          f"{manifest['results']['drug']['label'].get('export_date')}")
    matcher = Matcher(generics)
    best: dict[str, dict] = {}
    counts: dict[str, int] = {s: 0 for s in generics}
    seen = 0
    with tempfile.TemporaryDirectory() as td:
        for i, p in enumerate(parts, 1):
            url = p["file"]
            dest = Path(td) / f"part{i}.zip"
            t0 = time.time()
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as out:
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    out.write(chunk)
            for label in iter_bulk_labels(dest):
                seen += 1
                if not is_human(label):
                    continue
                for slug in matcher.match(label):
                    counts[slug] += 1
                    cur = best.get(slug)
                    if cur is None or rank_key(label, args.prefer) < rank_key(cur, args.prefer):
                        best[slug] = label
            dest.unlink()
            print(f"bulk part {i}/{len(parts)} done in {time.time() - t0:.0f}s; "
                  f"{seen} labels scanned, {len(best)} generics matched so far", flush=True)
    return best, counts


# --------------------------------------------------------------------------- output
def write_if_changed(path: Path, obj: dict, ignore: tuple[str, ...] = ()) -> bool:
    if path.exists():
        try:
            old = json.loads(path.read_text(encoding="utf-8"))
            strip = lambda d: {k: v for k, v in d.items() if k not in ignore}
            if strip(old) == strip(obj):
                return False
        except Exception:
            pass
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--generics-file", default=str(DEFAULT_GENERICS))
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT))
    ap.add_argument("--source", choices=["auto", "api", "bulk"], default="auto")
    ap.add_argument("--prefer", choices=["recent", "innovator"], default="recent",
                    help="tie-break order after Rx>OTC (default: newest effective_time first)")
    ap.add_argument("--only", nargs="*", help="limit to these slugs")
    ap.add_argument("--force", action="store_true", help="rewrite every file even if unchanged")
    ap.add_argument("--max-pages", type=int, default=10, help="API pages (x100) per generic")
    ap.add_argument("--min-interval", type=float, default=0.3, help="seconds between API calls")
    args = ap.parse_args()

    gpath = Path(args.generics_file)
    if not gpath.is_absolute():
        gpath = (Path.cwd() / gpath).resolve()
    generics = json.loads(gpath.read_text(encoding="utf-8"))
    generics = {k: v for k, v in generics.items() if v.get("ingredients")}
    if args.only:
        generics = {k: v for k, v in generics.items() if k in set(args.only)}
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    source = args.source
    if source == "auto":
        source = "api" if len(generics) <= 200 else "bulk"
    print(f"{len(generics)} generics from {gpath.name}; source={source}; prefer={args.prefer}")
    best, counts = (run_api if source == "api" else run_bulk)(generics, args)

    added, changed, unchanged, missing = [], [], 0, []
    for slug, g in sorted(generics.items()):
        label = best.get(slug)
        if label is None:
            missing.append({"slug": slug, "name": g.get("name", slug), "ingredients": g["ingredients"],
                            "reason": "fetch error" if counts.get(slug) == -1 else "no matching US FDA human label"})
            continue
        path = out_dir / f"{slug}.json"
        old_meta = None
        if path.exists():
            try:
                old_meta = json.loads(path.read_text(encoding="utf-8")).get("label", {})
            except Exception:
                old_meta = None
        new_key = (label.get("set_id", ""), label.get("effective_time", ""))
        if old_meta and (old_meta.get("set_id"), old_meta.get("effective_time")) == new_key and not args.force:
            unchanged += 1
            continue
        rec = build_record(slug, g, label, counts.get(slug, 0), args.prefer)
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entry = {"slug": slug, "name": g.get("name", slug), "brand_name": rec["label"]["brand_name"],
                 "set_id": new_key[0], "effective_time": new_key[1],
                 "dailymed_url": rec["source"]["dailymed_url"]}
        if old_meta is None:
            added.append(entry)
        elif (old_meta.get("set_id"), old_meta.get("effective_time")) != new_key:
            entry["previous"] = {"set_id": old_meta.get("set_id"), "effective_time": old_meta.get("effective_time")}
            changed.append(entry)
        # (forced rewrite of an unchanged label is not a review item)

    now = dt.datetime.now(MANILA).isoformat(timespec="seconds")
    # merge misses: when running a subset (--only), keep misses for slugs not in this run
    mpath = out_dir / "_missing.json"
    if args.only and mpath.exists():
        prev = json.loads(mpath.read_text(encoding="utf-8")).get("missing", [])
        missing = [m for m in prev if m["slug"] not in generics] + missing
        missing.sort(key=lambda m: m["slug"])
    write_if_changed(mpath, {"generated_at": now, "generics_file": gpath.name, "count": len(missing),
                             "missing": missing}, ignore=("generated_at",))
    write_if_changed(out_dir / "_changes.json", {
        "generated_at": now,
        "note": "US FDA labels added or changed in the latest run; for Dr. Rivero's weekly review.",
        "source": source, "added": added, "changed": changed,
    }, ignore=("generated_at",))

    total = len(generics)
    hits = total - len(missing)
    print(f"matched {hits}/{total} ({100 * hits / max(total, 1):.0f}%); added {len(added)}, "
          f"changed {len(changed)}, unchanged {unchanged}, missing {len(missing)}")
    for m in missing:
        print(f"  missing: {m['slug']} ({m['reason']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
