#!/usr/bin/env python3
"""
generate_drug_pages.py — static generator for the renalcarematters.com Drug Database.

Reads (all under --data-dir, default data/drugs/):
  registry/<c>.json        PH FDA products, sharded by first character of generic_slug
                           (a–z, plus "0" for non-letters). Each shard is a list of products.
                           A legacy single registry.json is also accepted if no shards exist.
  generics.json            {slug: {name, ingredients[], products, categories[], ...}}
  labels/<slug>.json       optional — US FDA label sections (DailyMed / openFDA), verbatim
  pnf.json                 optional — Philippine National Formulary status
  prices.json              optional — reference prices (e.g. DPRI)
  prices-retail.json       optional — {slug: [{chain, product, price, unit, url, checked_date}]}
  pharmacies.json          optional — [{id, name, search_url_template ("{q}"), enabled}]
  renal/<slug>.json        optional — our kidney-dosing guidance; rendered ONLY when
                           review_status == "approved"

Writes (under --out-dir, default drugs/):
  <slug>.html              one clinician page per generic
  index.html               Drug Index (A–Z filter + client-side brand/generic search)
  search-index.json        compact search index: [{"s": slug, "n": name, "b": [brands], "c": category}]
  drugdb.css               MASTER_CSS (from patch_master_css.py) + drug-page CSS
  drugdb.js                shared page JS (theme toggle, product-table filter/sort, index search)

A page is rewritten only when its content changes; its "Last updated" date is the date of the
last real content change (kept in a content-hash meta tag), so weekly runs do not churn every file.

Usage:
  python3 generate_drug_pages.py                         # full build
  python3 generate_drug_pages.py --only amlodipine,losartan
  python3 generate_drug_pages.py --dry-run               # count changes, write nothing
  python3 generate_drug_pages.py --no-prune              # keep pages for slugs no longer present
  python3 generate_drug_pages.py --data-dir /tmp/x/data/drugs --out-dir /tmp/x/drugs
  python3 generate_drug_pages.py --from-api-sample sample.json --data-dir /tmp/x/data/drugs
        # derive a synthetic sharded registry + generics.json from a raw PH FDA API response
        # (cdrr / cdrr_PIPIL / vat_exempt keys); add --build to also generate pages from it
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "tools" / "drugdb"))
import eu_smpc_render as eu_r  # noqa: E402  (EU SmPC text for generics with no US label)
import synonyms as SYN  # noqa: E402  (INN / USAN / BAN name synonyms: search, "Also known as", component links)

REPO = Path(__file__).resolve().parent
SITE = "https://renalcarematters.com"
GENERATOR_TAG = "generate_drug_pages.py"
FDA_VERIFY_URL = "https://verification.fda.gov.ph"
OG_IMAGE = f"{SITE}/images/og/og-drug-index.jpg"   # 1200x630 share card, JPEG <300 KB for Messenger/WhatsApp (patch_og_images.py)
FONTS = ("https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&amp;"
         "family=Inter:wght@500;600;700;800&amp;family=Nunito+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap")
ASSET_VERSION = "29"   # bump when drugdb.css / drugdb.js change shape (cache-busting query)
HASH_ASSET_VERSION = "22"   # version used inside page content hashes, so an asset-only bump does not change every page's "Last updated" date

esc = lambda s: html.escape("" if s is None else str(s), quote=True)


# ═════════════════════════════════════════════════════════════════════════════
# Small helpers
# ═════════════════════════════════════════════════════════════════════════════
def ws(s) -> str:
    """Collapse whitespace (the registry has embedded newlines in categories)."""
    return re.sub(r"\s+", " ", str(s or "")).strip()


_DATE_FMTS = ("%d %B %Y", "%d %b %Y", "%B %d, %Y", "%b %d, %Y", "%Y-%m-%d", "%Y%m%d",
              "%m/%d/%Y", "%d-%b-%Y", "%d-%B-%Y", "%Y-%m-%dT%H:%M:%S")


def parse_date(s) -> dt.date | None:
    if not s:
        return None
    s = ws(s).rstrip(".")
    s = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", s)
    for f in _DATE_FMTS:
        try:
            return dt.datetime.strptime(s, f).date()
        except ValueError:
            continue
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    if m:
        return dt.date.fromisoformat(m.group(1))
    return None


def us_date(d: dt.date | None, short=False) -> str:
    if not d:
        return ""
    return d.strftime(("%b " if short else "%B ") + f"{d.day}, %Y")


def us_date_str(s, short=False) -> str:
    d = parse_date(s)
    return us_date(d, short) if d else ws(s)


def classify(c) -> str:
    """Normalize the many registry spellings to Rx / OTC / HR (or the raw text). Accepts a product dict
    (uses its normalized "dispensing" field when present) or a classification string."""
    if isinstance(c, dict):
        d = ws(c.get("dispensing")).upper()
        if d in ("RX", "OTC", "HR"):
            return {"RX": "Rx"}.get(d, d)
        c = c.get("classification")
    t = ws(c).lower()
    if not t:
        return ""
    if "household" in t or "hone remedy" in t or "(hr)" in t or t == "hr":
        return "HR"
    if "otc" in t or "over-the" in t or "over the" in t:
        return "OTC"
    if "rx" in t or "prescri" in t:
        return "Rx"
    return ws(c)


CLASS_LABEL = {"Rx": "Prescription (Rx)", "OTC": "Over-the-counter (OTC)", "HR": "Household remedy (HR)"}


_NO_BRAND = {"", "n/a", "na", "none", "unbranded", "un-branded", "non-branded", "-", "--", "not applicable", "no brand", "no brand name", "generic"}


def _brand_key(b: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", b.lower()).strip()


def brand_list(products, generic_name: str = "", ranked: bool = False) -> list[str]:
    """Distinct PH brand names (case-insensitive; the most common registered spelling is kept). Blank, "N/A" and
    brand == generic name are excluded. ranked=True: most products first, then A–Z; otherwise A–Z."""
    seen: dict[str, dict[str, int]] = {}
    gk = _brand_key(generic_name)
    for p in products:
        b = ws(p.get("brand_name"))
        k = _brand_key(b)
        if not k or b.lower().strip(" .") in _NO_BRAND or k == gk or k == _brand_key(ws(p.get("generic_name"))):
            continue
        seen.setdefault(k, {}).setdefault(b, 0)
        seen[k][b] += 1
    rows = [(sum(v.values()), max(v.items(), key=lambda kv: (kv[1], kv[0]))[0]) for v in seen.values()]
    if ranked:
        rows.sort(key=lambda r: (-r[0], r[1].lower(), r[1]))
    else:
        rows.sort(key=lambda r: (r[1].lower(), r[1]))
    return [b for _, b in rows]


def safe_url(u) -> str:
    u = ws(u)
    return u if re.match(r"^https?://", u, re.I) else ""


def load_json(path: Path, default=None):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as e:
        print(f"  ! could not parse {path}: {e}", file=sys.stderr)
        return default


def unwrap(dataset):
    """Accept {"source", "as_of", "items": {...}} or a bare {slug: ...} mapping."""
    if not isinstance(dataset, dict):
        return {}, {}
    if isinstance(dataset.get("_meta"), dict):
        return dataset["_meta"], {k: v for k, v in dataset.items() if k != "_meta"}
    if isinstance(dataset.get("items"), dict):
        meta = {k: v for k, v in dataset.items() if k != "items"}
        return meta, dataset["items"]
    meta = {k: dataset[k] for k in ("source", "source_url", "as_of", "edition") if k in dataset
            and not isinstance(dataset[k], (dict, list))}
    return meta, {k: v for k, v in dataset.items() if k not in meta}


def peso(v) -> str:
    try:
        return "₱" + f"{float(str(v).replace(',', '').replace('₱', '').strip()):,.2f}"
    except (TypeError, ValueError):
        return ws(v)


# ═════════════════════════════════════════════════════════════════════════════
# --from-api-sample: derive a synthetic registry from a raw PH FDA API response
# ═════════════════════════════════════════════════════════════════════════════
SALT_WORDS = {
    "potassium", "sodium", "calcium", "magnesium", "hydrochloride", "hcl", "besilate", "besylate",
    "mesylate", "mesilate", "maleate", "medoxomil", "cilexetil", "arginine", "erbumine",
    "tert-butylamine", "dihydrate", "monohydrate", "trihydrate", "hemihydrate", "anhydrous",
    "sulfate", "sulphate", "phosphate", "citrate", "tartrate", "bitartrate", "fumarate",
    "hemifumarate", "succinate", "acetate", "bromide", "hydrobromide", "chloride", "nitrate",
    "camsylate", "dipropionate", "propionate", "valerate", "furoate", "lactate", "gluconate", "trometamol",
    "tromethamine", "disodium", "dihydrochloride", "salt", "base",
}


def ingredient_base(name: str) -> str:
    s = re.sub(r"\(.*?\)", " ", name.lower())
    s = re.sub(r"\bas\s+\w+", " ", s)
    words = [w.strip(".;") for w in re.split(r"[\s,]+", s) if w.strip(".;")]
    base = list(words)
    while len(base) > 1 and base[-1] in SALT_WORDS:
        base.pop()
    if len(base) == 1 and base[0] in SALT_WORDS:
        base = words          # e.g. "potassium chloride" stays as is
    return " ".join(base).strip()


def split_ingredients(generic_name: str) -> list[str]:
    parts = re.split(r"\s*\+\s*|\s+/\s*|\s*/\s+|(?<=[a-z\)])/(?=[A-Za-z])|\s+and\s+", ws(generic_name), flags=re.I)
    return [p for p in (ingredient_base(x) for x in parts) if p]


def slug_for(ingredients: list[str]) -> str:
    parts = sorted({re.sub(r"[^a-z0-9]+", "-", i.lower()).strip("-") for i in ingredients})
    return "-".join(p for p in parts if p)[:120].strip("-")


def derive_from_api_sample(sample_path: Path, data_dir: Path) -> None:
    raw = load_json(sample_path)
    if not isinstance(raw, dict) or "cdrr" not in raw:
        sys.exit(f"{sample_path}: not a PH FDA API response (no 'cdrr' key)")
    pis = defaultdict(list)
    for r in raw.get("cdrr_PIPIL") or []:
        if r.get("registration_number") and safe_url(r.get("file_link")):
            pis[ws(r["registration_number"])].append({"version": ws(r.get("version")), "file_link": r["file_link"]})
    vat = set()
    for r in raw.get("vat_exempt") or []:
        vat.add(slug_for(split_ingredients(r.get("generic_name", ""))))
    shards, generics = defaultdict(list), {}
    for p in raw["cdrr"]:
        ings = split_ingredients(p.get("generic_name", ""))
        slug = slug_for(ings)
        if not slug:
            continue
        rec = {k: (ws(v) if isinstance(v, str) else v) for k, v in p.items()}
        rec.update(generic_slug=slug, ingredients=sorted(set(ings)),
                   pi_links=pis.get(ws(p.get("registration_number")), []),
                   vat_exempt=slug in vat)
        shards[slug[0] if slug[0].isalpha() else "0"].append(rec)
        g = generics.setdefault(slug, {"name": " + ".join(i.capitalize() for i in sorted(set(ings))),
                                       "ingredients": sorted(set(ings)), "products": 0,
                                       "registered_names": [], "categories": []})
        g["products"] += 1
        if ws(p.get("generic_name")) not in g["registered_names"]:
            g["registered_names"].append(ws(p.get("generic_name")))
        cat = ws(p.get("pharmacologic_category"))
        if cat and cat not in g["categories"]:
            g["categories"].append(cat)
    (data_dir / "registry").mkdir(parents=True, exist_ok=True)
    for k, rows in shards.items():
        with open(data_dir / "registry" / f"{k}.json", "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False)
    with open(data_dir / "generics.json", "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(generics.items())), fh, ensure_ascii=False, indent=1)
    print(f"Derived {sum(map(len, shards.values()))} products / {len(generics)} generics "
          f"into {data_dir}/registry/*.json + generics.json")


# ═════════════════════════════════════════════════════════════════════════════
# CSS — MASTER_CSS (single source of truth) + drug-page rules, with body.dark-mode aliases
# ═════════════════════════════════════════════════════════════════════════════
DARK = 'html[data-theme="dark"]'


def _split_top_commas(sel: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in sel:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def add_body_dark_aliases(css: str) -> str:
    """For every selector using html[data-theme="dark"], add an equivalent body.dark-mode selector,
    so the pages honor both dark-mode conventions used across the site."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)

    def fix(m):
        lead, prelude = m.group(1), m.group(2)
        if DARK not in prelude or prelude.lstrip().startswith("@"):
            return m.group(0)
        parts = _split_top_commas(prelude)
        extra = []
        for p in parts:
            if DARK in p:
                q = re.sub(r'html\[data-theme="dark"\]\s+body(?=[.\[:#])', "body.dark-mode", p)
                q = re.sub(r'html\[data-theme="dark"\]\s+body\b', "body.dark-mode", q)
                q = q.replace(DARK, "body.dark-mode")
                extra.append(q)
        return lead + ",".join(parts + extra) + "{"
    return re.sub(r"(^|[{};])([^{};]+)\{", fix, css)


DRUG_CSS = r"""
/* ── Drug Database (generate_drug_pages.py) ─────────────────────────────── */
.container.dd-wide { max-width: 1180px; }
.dd-crumb { font-size: 12.5px; margin-bottom: 10px; color: #46516b; }
.dd-crumb a { color: #1f3864; font-weight: 600; text-decoration: none; }
.dd-crumb a:hover { text-decoration: underline; }
.dd-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 2px 0 16px; }
.dd-chip { display: inline-block; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600;
  letter-spacing: .02em; color: #1f3864; background: rgba(31,56,100,.08);
  border: 1px solid rgba(31,56,100,.28); border-radius: 20px; padding: 4px 12px; }
.dd-chip.dd-rx { color: #7a1d1d; background: #fdecec; border-color: rgba(185,28,28,.35); }
.dd-chip.dd-otc { color: #14532d; background: #e8f7ee; border-color: rgba(22,101,52,.35); }
.dd-chip.dd-good { color: #0e4a50; background: #e1f5f0; border-color: rgba(14,74,80,.35); }
.hero-meta .dd-meta-time { font-weight: 600; color: #1f3864; }
.dd-sched { flex-basis: 100%; display: flex; align-items: flex-start; gap: 8px; margin: 0; font-size: 13.5px; line-height: 1.45; color: #3c4a5e; }
.dd-sched > span { max-width: 64ch; }
.dd-sched svg { flex: none; width: 18px; height: 18px; margin-top: 1px; fill: none; stroke: #1a6b72; stroke-width: 1.9; stroke-linecap: round; stroke-linejoin: round; }
.dd-sched strong { color: #1e2a38; }
.dd-sched time { font-weight: 700; color: #1e2a38; background: none !important; padding: 0 !important; box-shadow: none !important; }
.hero-meta:has(.dd-sched) { flex-wrap: wrap !important; display: flex; align-items: center; row-gap: 10px !important; }
html .hero-meta .dd-sched time, html[data-theme="dark"] .hero-meta .dd-sched time { background: transparent !important; }
.hero-meta .dd-sched { width: 100%; }
.dd-lead { font-size: 15px; color: var(--text-mid); margin: 0 0 18px; }
.section .dd-note, .dd-note { font-size: 13px; color: var(--text-muted); line-height: 1.6; text-align: left; }
.dd-btn { display: inline-flex; align-items: center; gap: 6px; font-family: 'Inter', sans-serif;
  font-size: 13px; font-weight: 600; text-decoration: none; color: #fff; background: #1f3864;
  border: 1px solid #1f3864; border-radius: 8px; padding: 8px 14px; margin: 4px 8px 4px 0; }
.dd-btn:hover { background: #0e2547; }
.dd-btn.dd-btn-ghost { color: #1f3864; background: transparent; border-color: rgba(31,56,100,.45); }
.dd-btn.dd-btn-ghost:hover { background: rgba(31,56,100,.06); }
.dd-btn svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 2; }
.dd-toolbar { display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: center; margin: 18px 0 12px; }
.dd-toolbar input[type=search], .dd-toolbar select, .dd-search input {
  font: inherit; font-size: 14px; color: var(--text); background: var(--white);
  border: 1px solid #8a96a8; border-radius: 8px; padding: 8px 12px; min-height: 40px; }
.dd-sort-sel { display: none; }
.dd-toolbar input[type=search] { flex: 1 1 260px; min-width: 0; }
.dd-toolbar label.dd-check { font-size: 13.5px; color: var(--text-mid); display: inline-flex; gap: 6px; align-items: center; }
.dd-count { font-size: 13px; color: var(--text-muted); margin-left: auto; }
.dd-table-wrap { border: 1px solid var(--border); border-radius: 12px; overflow-x: auto; background: var(--white); }
table.dd-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
.dd-table th { position: sticky; top: 0; background: #eef2f8; color: #1f3864; text-align: left;
  font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: .03em;
  padding: 0; border-bottom: 1px solid var(--border); white-space: nowrap; }
.dd-table th button { all: unset; cursor: pointer; display: block; padding: 10px 12px; width: 100%; box-sizing: border-box; }
.dd-table th button:focus-visible { outline: 2px solid #1a6b72; outline-offset: -2px; }
.dd-table th button::after { content: " \2195"; opacity: .45; }
.dd-table th[aria-sort=ascending] button::after { content: " \2191"; opacity: 1; }
.dd-table th[aria-sort=descending] button::after { content: " \2193"; opacity: 1; }
.dd-table td { padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text-mid); }
.dd-table tbody tr:last-child td { border-bottom: none; }
.dd-table tbody tr:hover td { background: var(--bg); }
.dd-table .dd-brand { font-weight: 700; color: var(--text); }
.dd-sub { display: block; font-size: 12px; color: var(--text-muted); margin-top: 2px; }
.dd-reg { font-family: 'Inter', sans-serif; font-size: 12.5px; white-space: nowrap; }
.dd-tag { display: inline-block; font-size: 11px; font-weight: 700; border-radius: 6px; padding: 1px 7px; white-space: nowrap; }
.dd-tag.Rx { color: #7a1d1d; background: #fdecec; }
.dd-tag.OTC { color: #14532d; background: #e8f7ee; }
.dd-tag.HR { color: #5b3a00; background: #fdf3dc; }
.dd-past { display: inline-block; font-size: 11px; font-weight: 600; color: #7a1d1d; }
.dd-table a { color: #1a6b72; font-weight: 600; }
.dd-empty { padding: 18px; font-size: 14px; color: var(--text-muted); }
.dd-acc { border: 1px solid var(--border); border-radius: 12px; margin: 12px 0; background: var(--white); }
.dd-acc > summary { cursor: pointer; list-style: none; padding: 14px 18px; font-family: 'Inter', sans-serif;
  font-weight: 600; font-size: 15.5px; color: var(--navy); display: flex; justify-content: space-between; gap: 12px; }
.dd-acc > summary::-webkit-details-marker { display: none; }
.dd-acc > summary::after { content: "+"; font-size: 20px; line-height: 1; color: #1a6b72; }
.dd-acc[open] > summary::after { content: "\2212"; }
.dd-acc > summary:focus-visible { outline: 2px solid #1a6b72; outline-offset: 2px; border-radius: 12px; }
.dd-acc .dd-acc-body { padding: 4px 18px 16px; border-top: 1px solid var(--border); font-size: 14.5px; color: var(--text-mid); }
.section .dd-acc-body p, .dd-acc-body p { text-align: left; hyphens: manual; margin: 10px 0; white-space: pre-line; font-size: 14.5px; }
.dd-acc-body ul, .dd-acc-body ol { margin: 8px 0 8px 22px; }
.dd-acc-body table { border-collapse: collapse; margin: 10px 0; font-size: 13px; }
.dd-acc-body td, .dd-acc-body th { border: 1px solid var(--border); padding: 4px 8px; }
.dd-acc.dd-boxed { border: 2px solid #b91c1c; }
.dd-acc.dd-boxed > summary { color: #7a1d1d; }
.dd-attrib { background: #eef2f8; border: 1px solid rgba(31,56,100,.18); border-radius: 10px; padding: 12px 16px;
  font-size: 13px; color: var(--text-mid); line-height: 1.6; margin: 14px 0 6px; }
.dd-attrib a { color: #1a6b72; font-weight: 600; }
.dd-placeholder { background: var(--bg); border: 1px dashed #8a96a8; border-radius: 10px; padding: 14px 18px;
  font-size: 14px; color: var(--text-muted); }
.dd-renal-table td:first-child { font-weight: 600; color: var(--text); white-space: nowrap; }
.dd-pharm { display: flex; flex-wrap: wrap; gap: 4px 0; margin: 10px 0 4px; }
/* Browse-by segmented control (Drug Index) */
.dd-browse-wrap { display: flex; align-items: center; gap: 10px; margin: 18px 0 4px; min-width: 0; }
.dd-browse-l { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase;
  color: var(--text-muted); white-space: nowrap; }
.dd-browse { position: relative; display: flex; gap: 4px; padding: 4px; border: 1px solid var(--border); border-radius: 12px; background: #eef2f8;
  overflow-x: auto; scrollbar-width: thin; -webkit-overflow-scrolling: touch; max-width: 100%; }
.dd-browse button { font-family: 'Inter', sans-serif; font-size: 13.5px; font-weight: 700; white-space: nowrap; border: 0; cursor: pointer;
  background: transparent; color: #1f3864; padding: 8px 14px; border-radius: 9px; min-height: 38px; }
.dd-browse button:hover { background: rgba(31,56,100,.08); }
.dd-browse button[aria-selected=true] { background: #1f3864; color: #fff; box-shadow: 0 1px 3px rgba(15,30,51,.25); }
.dd-browse button:focus-visible { outline: 3px solid #1a6b72; outline-offset: 1px; }
.dd-vnote { margin: 14px 0 6px; }
.dd-vg { content-visibility: auto; contain-intrinsic-size: auto 60px; border-bottom: 1px solid var(--border); }
.dd-vletter { contain-intrinsic-size: auto 1200px; border: 0; }
.dd-vletter h2 { font-family: 'Inter', sans-serif; font-size: 22px; color: var(--navy); margin: 28px 0 8px; }
details.dd-vg > summary { cursor: pointer; list-style: none; display: flex; align-items: baseline; gap: 8px; padding: 12px 4px;
  font-family: 'Inter', sans-serif; font-weight: 700; font-size: 15.5px; color: var(--navy); }
details.dd-vg > summary::-webkit-details-marker { display: none; }
details.dd-vg > summary::before { content: "▸"; color: #1a6b72; transition: transform .15s; display: inline-block; }
details.dd-vg[open] > summary::before { transform: rotate(90deg); }
.dd-vg-n { font-size: 12px; font-weight: 700; color: #0e4a50; background: #e1f2f1; border-radius: 999px; padding: 1px 9px; }
.dd-vg-link { margin: 0 0 6px; font-size: 13.5px; }
.dd-vg-link a { color: #0e4a50; font-weight: 700; }
details.dd-vg > ul.dd-list { padding: 0 4px 12px 22px; }
@media (max-width: 640px) {
  .dd-browse-wrap { flex-direction: column; align-items: stretch; gap: 6px; }
  .dd-browse { border-radius: 10px; }
}
.dd-alpha { display: flex; flex-wrap: wrap; gap: 6px; margin: 16px 0 6px; }
.dd-alpha[hidden] { display: none; }
.dd-alpha button { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; min-width: 36px; min-height: 36px;
  border-radius: 8px; border: 1px solid rgba(31,56,100,.3); background: var(--white); color: #1f3864; cursor: pointer; }
.dd-alpha button[aria-pressed=true] { background: #1f3864; color: #fff; border-color: #1f3864; }
.dd-alpha button:disabled { opacity: .4; cursor: default; }
.dd-search { display: flex; gap: 10px; margin: 18px 0 4px; }
.dd-search input { flex: 1; font-size: 16px; min-height: 46px; }
.dd-letter h2 { font-family: 'Inter', sans-serif; font-size: 22px; color: var(--navy); margin: 28px 0 8px;
  border-bottom: 1px solid var(--border); padding-bottom: 6px; }
ul.dd-list { list-style: none; margin: 0; padding: 0; columns: 2 320px; column-gap: 32px; }
ul.dd-list li { overflow-wrap: anywhere; break-inside: avoid; padding: 7px 0; border-bottom: 1px solid var(--border); font-size: 14px; }
ul.dd-list a { color: #1a6b72; font-weight: 700; text-decoration: none; }
ul.dd-list a:hover { text-decoration: underline; }
.dd-res-brand { font-weight: 700; color: var(--text); }
mark.dd-hl { background: #fff1b8; color: inherit; border-radius: 3px; padding: 0 1px; }
.dd-results { margin: 14px 0; }
.disclaimer a, .dd-acc-body a, .dd-kidney a, .dd-note a { color: #1a6b72; font-weight: 600; word-break: break-word; }
/* Monograph layout (section order modeled on clinical drug monographs) */
.container.dd-hero-wide { max-width: 1240px; }
.dd-layout { max-width: 1240px; margin: 0 auto; padding: 0 32px; display: grid; grid-template-columns: 210px minmax(0, 1fr); gap: 40px; }
.dd-toc { position: sticky; top: 72px; align-self: start; max-height: calc(100vh - 90px); overflow: auto; padding: 24px 0; }
.dd-toc-h { font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 8px; }
.dd-toc ol { list-style: none; margin: 0; padding: 0; border-left: 2px solid var(--border); }
.dd-toc a { display: block; padding: 5px 12px; margin-left: -2px; border-left: 2px solid transparent; font-size: 13.5px; color: var(--text-mid); text-decoration: none; }
.dd-toc a:hover { color: #1f3864; background: var(--bg); }
.dd-toc a[aria-current] { border-left-color: #1a6b72; color: #0e4a50; font-weight: 700; }
.dd-main { min-width: 0; padding-top: 20px; }
body.dd-mono .nav-strip.dd-pills { display: none; }
.dd-sec { padding: 26px 0; border-bottom: 1px solid var(--border); scroll-margin-top: 72px; }
.dd-sec:last-child { border-bottom: 0; }
.dd-sec > h2 { font-family: 'Inter', sans-serif; font-size: 22px; font-weight: 700; color: var(--navy); margin: 0 0 12px; }
.dd-sec h3 { font-family: 'Inter', sans-serif; font-size: 16px; color: var(--navy); margin: 16px 0 8px; }
.dd-sec p { text-align: left; hyphens: manual; }
.dd-kidney.dd-sec { padding: 22px 24px 18px; margin: 18px 0; border-bottom: 1px solid #cfe6e6; }
.dd-kidney-inline { margin: 6px 0 10px; padding: 12px 16px; }
.dd-kidney-table tr.dd-kgroup th { background: #1a6b72; color: #fff; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; width: auto; padding: 7px 14px; }
ul.dd-uselist { margin: 4px 0 8px 20px; padding: 0; }
ul.dd-uselist li { margin: 3px 0; font-size: 15px; color: var(--text-mid); }
.dd-src-ours { color: #0e4a50; border-color: rgba(14,74,80,.35); background: #e1f5f0; }
.dd-boxed-alert { border: 2px solid #b91c1c; background: #fff5f5; border-radius: 12px; padding: 14px 18px; margin: 4px 0 14px; }
.dd-boxed-h { font-family: 'Inter', sans-serif; font-weight: 800; color: #7a1d1d; text-transform: uppercase; letter-spacing: .06em; font-size: 13px; margin-bottom: 6px; }
.dd-boxed-body { max-height: 280px; overflow: auto; font-size: 14px; color: #3b0d0d; }
.dd-boxed-body p { margin: 6px 0; white-space: pre-line; }
.dd-twocol { display: grid; grid-template-columns: 1fr 1fr; gap: 0 28px; }
.dd-pk-hi { background: #eef2f8; border-left: 4px solid #1f3864; border-radius: 8px; padding: 6px 14px; margin: 6px 0 10px; }
.dd-pk-hi p { font-size: 14px; color: var(--text-mid); margin: 6px 0; }
.dd-tables { overflow-x: auto; }
.dd-tables table { font-size: 12.5px; }
pre.dd-pre { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; line-height: 1.45; white-space: pre; margin: 8px 0; padding: 10px 12px; background: #f4f6f9; border: 1px solid var(--border); border-radius: 8px; color: var(--text); }
.dd-eu-h { font-weight: 700; color: var(--navy); margin: 12px 0 4px; }
.dd-src-eu { color: #1e3a8a; border-color: rgba(30,58,138,.35); background: #e8edfb; }
.dd-pi-links ul { margin-top: 6px; }
ol.dd-refs { margin: 4px 0 12px 20px; font-size: 13.5px; color: var(--text-mid); }
ol.dd-refs li { margin: 4px 0; overflow-wrap: anywhere; }
ol.dd-refs a { color: #1a6b72; }
.dd-sev { display: inline-block; font-size: 11.5px; font-weight: 700; border-radius: 6px; padding: 1px 8px; white-space: nowrap; }
.dd-sev-avoid { color: #fff; background: #b91c1c; }
.dd-sev-adjust { color: #5b3a00; background: #fde68a; }
.dd-sev-minor { color: #1f3864; background: #e3e8f2; }
.dd-usbrand { font-size: 13.5px; color: #34455f; margin: -4px 0 8px; }
.dd-alias { border: 2px solid #1a6b72; background: #e6f4f4; color: #12333a; border-radius: 12px; padding: 12px 16px; margin: 4px 0 12px;
  font-size: 14.5px; line-height: 1.5; max-width: 720px; }
.dd-alias p { margin: 0 0 6px; }
.dd-alias-soft { border-width: 1px; border-style: dashed; background: #f3f7fa; }
.dd-alias-soft p { margin: 0; }
.dd-alias a { color: #0e4a50; font-weight: 700; }
.dd-alias-go { display: inline-block; text-decoration: none; border-bottom: 2px solid currentColor; }
.dd-alias-sub { font-weight: 500; }
.dd-aka { font-size: 14px; color: #34455f; margin: -2px 0 8px; line-height: 1.5; }
.dd-aka > span { font-weight: 700; color: #1e2a38; margin-right: 2px; }
.dd-aka strong { color: #0e4a50; font-weight: 700; }
/* Component information (combination with no label of its own) */
.dd-comp-intro { font-size: 15px; color: var(--text-mid); margin: 0 0 10px; }
ul.dd-comp-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
.dd-comp { border: 1px solid var(--border); border-left: 4px solid #1a6b72; border-radius: 10px; padding: 10px 14px; background: var(--white); }
.dd-comp-none { border-left-color: #8a96a8; color: var(--text-mid); font-size: 14.5px; }
.dd-comp-h { font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 700; }
.dd-comp-h a { color: #0e4a50; }
.dd-comp-h .dd-sub, .dd-comp-none .dd-sub { font-family: 'Manrope', sans-serif; font-weight: 500; font-size: 12.5px; color: var(--text-mid); }
.dd-comp-n { font-weight: 700; color: var(--text); }
.dd-comp-use { font-size: 14.5px; color: var(--text-mid); margin: 6px 0 4px; }
.dd-comp-kid { margin-top: 8px; padding: 8px 12px; background: #f2f9f9; border: 1px solid #cfe6e6; border-radius: 10px; }
.dd-comp-kh { display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 700; color: #0e4a50; }
.dd-comp-kh .dd-kidney-ico { width: 18px; height: 18px; flex: none; }
.dd-comp-kid .dd-note { font-size: 12.5px; margin: 4px 0 0; }
.dd-comp-kid .dd-acc { margin: 6px 0; }
.dd-comp-caveat { margin: 12px 0 0; padding: 10px 14px; font-size: 14px; color: #5b3a00; background: #fffbeb; border: 1px solid #e8c27a; border-radius: 10px; }
.dd-also { font-size: 14px; color: var(--text-mid); margin: 6px 0 10px; }
.dd-also a { color: #0e4a50; font-weight: 600; }
.dd-varnote { display: block; font-size: 11.5px; font-weight: 700; color: #7a3d00; margin-top: 3px; }
.dd-varnote a { color: inherit; }
.dd-arrow { font-weight: 600; color: #0e4a50; white-space: nowrap; }
.hero-sub.dd-classline { font-size: 14.5px; }
.dd-chip.dd-hr { color: #5b3a00; background: #fdf3dc; border-color: rgba(146,64,14,.35); }
.dd-chip.dd-s2 { color: #fff; background: #991b1b; border-color: #991b1b; }
.dd-chip.dd-cp { color: #4a2800; background: #fcd34d; border-color: #b45309; }
a.dd-chip { text-decoration: none; display: inline-flex; align-items: center; gap: 5px; }
a.dd-chip .dd-kidney-ico { width: 14px; height: 14px; }
.dd-dispnote { font-size: 12.5px; color: #34455f; margin: -8px 0 12px; }
.dd-dispnote a { color: #1f3864; font-weight: 600; }
.dd-tag.S2 { color: #fff; background: #991b1b; }
.dd-tag.CP { color: #4a2800; background: #fcd34d; }
.dd-tag.PNF { color: #0e4a50; background: #e1f5f0; }
.dd-tag.KD { color: #fff; background: #1a6b72; }
.dd-tag.US { color: #1f3864; background: #e3e8f2; }
.dd-tag.SUP { color: #3d4656; background: #eceff3; border: 1px solid rgba(61,70,86,.35); }
.dd-tag.SUPK { color: #4a2800; background: #fdf3dc; }
.dd-tag.HEP { color: #3b2a66; background: #efe9fb; }
.dd-tag.NX { color: #fff; background: #9a3412; }
.dd-chip.dd-nxchip { color: #7c2d12; background: #fff1e8; border-color: rgba(154,52,18,.4); }
.dd-nx-item { border: 1px solid var(--border); border-left: 4px solid #c2410c; border-radius: 12px; padding: 14px 16px; margin: 0 0 14px; background: var(--white); }
.dd-nx-h { font-size: 15px; margin: 0 0 8px; }
.dd-nx-ms { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; }
.dd-nx-m { font-family: 'Inter', sans-serif; font-size: 12.5px; font-weight: 700; color: #7c2d12; background: #fff1e8; border-radius: 999px; padding: 3px 10px; }
.dd-nx-do { margin: 0 0 10px; padding-left: 20px; }
.dd-nx-do li { margin: 2px 0; }
.dd-nx-note { font-size: 14px; color: var(--text-mid); margin: 0 0 10px; }
.dd-nx-q { margin: 0; padding: 10px 14px; border-left: 3px solid var(--border); background: var(--bg); font-size: 14.5px; color: var(--text-mid); border-radius: 0 8px 8px 0; }
.dd-nx-q cite { display: block; margin-top: 6px; font-style: normal; font-size: 12.5px; color: var(--text-muted); }
.dd-nx-q cite a { color: #0e4a50; font-weight: 600; }
/* Favorites + interaction checker */
.dd-favbtn { cursor: pointer; font: inherit; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600; }
.dd-favbtn.is-on { color: #6b4a00; background: #fff5d6; border-color: rgba(146,113,10,.45); }
.dd-favstar { font-size: 14px; line-height: 1; }
.dd-chip.dd-ixbtn, .dd-chip.dd-ixchip { color: #fff; background: #1a6b72; border-color: #1a6b72; }
.dd-favs { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 0 0 12px; }
.dd-ix-pick { border: 1px solid var(--border); border-radius: 14px; background: var(--white); padding: 16px; margin: 0 0 18px; }
.dd-ix-add { position: relative; }
.dd-ix-l { display: block; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 14px; margin: 0 0 6px; color: var(--text); }
#dd-ix-q { width: 100%; box-sizing: border-box; font-size: 16px; padding: 12px 14px; border: 1.5px solid var(--border); border-radius: 10px; background: var(--white); color: var(--text); }
#dd-ix-q:focus { outline: 3px solid rgba(26,107,114,.35); border-color: #1a6b72; }
.dd-ix-sug { position: absolute; z-index: 30; left: 0; right: 0; top: 100%; margin: 4px 0 0; padding: 4px; list-style: none; background: var(--white);
  border: 1px solid var(--border); border-radius: 10px; box-shadow: 0 10px 28px rgba(15,23,42,.16); max-height: 340px; overflow: auto; }
.dd-ix-sug li { padding: 10px 12px; border-radius: 8px; cursor: pointer; font-size: 15px; }
.dd-ix-sug li[aria-selected="true"], .dd-ix-sug li:hover { background: #e1f5f0; }
.dd-ix-arrow { color: var(--text-muted); }
.dd-ix-have { font-size: 12px; color: #0e4a50; font-weight: 700; }
.dd-ix-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 0; }
.dd-ix-chips:empty { display: none; }
.dd-ix-chip { display: inline-flex; align-items: center; gap: 2px; padding: 4px 4px 4px 12px; border-radius: 999px; background: #e1f5f0; border: 1px solid rgba(14,74,80,.3); font-size: 14.5px; font-weight: 600; }
.dd-ix-chip a { color: #0e4a50; text-decoration: none; }
.dd-ix-chip button { border: 0; background: none; cursor: pointer; min-width: 32px; min-height: 32px; border-radius: 999px; font-size: 15px; color: #0e4a50; }
.dd-ix-chip button:hover { background: rgba(14,74,80,.12); }
.dd-ix-star.is-on { color: #92710a; }
.dd-ix-quick { margin: 10px 0 0; }
.dd-ix-qrow, .dd-favs { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin: 6px 0; }
.dd-ix-ql { font-family: 'Inter', sans-serif; font-size: 12.5px; font-weight: 700; color: var(--text-muted); margin-right: 4px; }
.dd-ix-qchips { display: flex; flex-wrap: wrap; gap: 6px; }
.dd-ix-q { font: inherit; font-size: 13.5px; padding: 6px 12px; border-radius: 999px; border: 1px solid var(--border); background: var(--bg); color: var(--text); cursor: pointer; text-decoration: none; min-height: 32px; box-sizing: border-box; display: inline-flex; align-items: center; }
.dd-ix-q:hover { border-color: #1a6b72; }
.dd-ix-q.is-on { color: var(--text-muted); cursor: default; }
.dd-ix-qgo { font-weight: 700; color: #0e4a50; }
.dd-ix-paste { margin: 12px 0 0; }
.dd-ix-paste summary { cursor: pointer; font-weight: 600; color: #0e4a50; }
.dd-ix-paste textarea { width: 100%; box-sizing: border-box; margin: 8px 0; font: inherit; font-size: 15px; padding: 10px; border: 1.5px solid var(--border); border-radius: 10px; background: var(--white); color: var(--text); }
.dd-ix-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px; margin: 14px 0 0; }
.dd-ix-k { font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.dd-ix-k select { font: inherit; font-size: 15px; padding: 8px 10px; border-radius: 8px; border: 1.5px solid var(--border); background: var(--white); color: var(--text); }
.dd-ix-btns { display: inline-flex; gap: 6px; flex-wrap: wrap; }
.dd-ix-sum { font-size: 16px; margin: 0 0 14px; display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }
.dd-ix-sumg { display: inline-flex; flex-wrap: wrap; gap: 6px; align-items: center; font-weight: 700; }
.dd-ix-g { display: inline-block; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 800; letter-spacing: .02em; padding: 3px 9px; border-radius: 6px; vertical-align: middle; white-space: nowrap; }
.dd-ix-g.g-ci { color: #fff; background: #7f1d1d; }
.dd-ix-g.g-avoid { color: #fff; background: #b91c1c; }
.dd-ix-g.g-adjust { color: #4a2800; background: #fcd34d; }
.dd-ix-g.g-minor { color: #1f3864; background: #e3e8f2; }
.dd-ix-card { border: 1px solid var(--border); border-radius: 12px; background: var(--white); padding: 14px 16px; margin: 0 0 14px; }
.dd-ix-card > ul:not(.dd-msw-list) { margin: 6px 0 0; padding-left: 1.35em; }
.dd-ix-card > ul:not(.dd-msw-list) > li { margin: 4px 0; padding-left: 2px; }
.dd-ix-card h2 { font-size: 18px; margin: 0 0 8px; }
.dd-ix-pairs > h2 { font-size: 18px; margin: 18px 0 10px; }
.dd-ix-pair h3 { font-size: 16.5px; margin: 0 0 8px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.dd-ix-row1 { border-top: 1px solid var(--border); padding: 8px 0 2px; }
.dd-ix-row1:first-of-type { border-top: 0; padding-top: 0; }
.dd-ix-row1 p { margin: 4px 0; font-size: 15px; }
.dd-ix-src { color: var(--text-mid); }
.dd-ix-kidney { border-left: 4px solid #1a6b72; }
.dd-ix-kidney ul { margin: 0; padding-left: 18px; }
.dd-ix-kidney li { margin: 6px 0; }
.dd-ix-tw { color: #7f1d1d; }
.dd-ix-ktab { border-collapse: collapse; margin: 6px 0 0; width: 100%; }
.dd-ix-ktab th, .dd-ix-ktab td { text-align: left; padding: 6px 8px; border-top: 1px solid var(--border); font-size: 14.5px; vertical-align: top; }
.dd-ix-ktab th { font-weight: 600; width: 40%; }
.dd-ix-ktab th a { color: var(--text); }
.dd-ix-kt { display: inline-block; padding: 2px 8px; border-radius: 6px; font-weight: 700; font-size: 13.5px; }
.dd-ix-kt.k-none { color: #14532d; background: #dcfce7; }
.dd-ix-kt.k-adjust { color: #4a2800; background: #fdf3dc; }
.dd-ix-kt.k-avoid { color: #7f1d1d; background: #fde2e2; }
.dd-ix-kt.k-nodata, .dd-ix-kt.k-hide { color: #374151; background: #eceff3; }
.dd-ix-kn { color: var(--text-muted); font-size: 14px; }
.dd-ix-card .dd-sub { display: inline; margin: 0; }
.dd-ix-card a { color: #0e4a50; font-weight: 600; }
.dd-ix-also summary { cursor: pointer; font-weight: 700; }
.dd-ix-also h3 { font-size: 15px; margin: 12px 0 4px; }
.dd-ix-also ul { margin: 0; padding-left: 18px; }
.dd-ix-also li { margin: 4px 0; font-size: 14.5px; }
.dd-ix-about { margin: 26px 0 0; }
.dd-ix-about h2 { font-size: 18px; }
.dd-ix-legend { list-style: none; padding: 0; margin: 0 0 12px; }
.dd-ix-legend li { margin: 6px 0; display: flex; gap: 10px; align-items: baseline; }
.dd-ix-legend .dd-ix-g { min-width: 132px; text-align: center; }
@media print { .dd-ix-pick, .dd-ix-about, .dd-favs { display: none !important; } .dd-ix-card { break-inside: avoid; } }
/* Med Scheduler */
.dd-ms-aht { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; margin: 8px 0 2px; font-size: 14px; }
.dd-ms-aht select { font: inherit; padding: 5px 8px; border-radius: 8px; border: 1px solid var(--border); background: var(--white); color: var(--text); }
.dd-ms-ahtnote { margin: 2px 0 0; font-size: 12.5px; }
.dd-ms-grid { display: grid; grid-template-columns: 1fr; gap: 0 18px; }
@media (min-width: 1000px) { .dd-ms-grid { grid-template-columns: minmax(300px, 2fr) 3fr; align-items: start; } }
.dd-ms-routine h2, .dd-ms-meds h2 { font-size: 17px; margin: 0 0 10px; }
.dd-ms-times { display: flex; flex-wrap: wrap; gap: 10px 14px; margin: 0 0 10px; }
.dd-ms-times label { display: flex; flex-direction: column; font-size: 13px; font-weight: 600; color: var(--text-mid); gap: 4px; }
.dd-ms-times input, .dd-ms-tab input, .dd-ms-tab select { font: inherit; font-size: 15px; padding: 7px 8px; border: 1.5px solid var(--border); border-radius: 8px; background: var(--white); color: var(--text); }
.dd-ms-hd { border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px 10px; margin: 6px 0 0; }
.dd-ms-hd legend { font-weight: 700; font-size: 14px; padding: 0 4px; }
.dd-ms-hd > label { margin-right: 14px; font-size: 15px; }
.dd-ms-hdbox { margin: 10px 0 0; }
.dd-ms-preset { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; }
.dd-ms-days { display: flex; flex-wrap: wrap; gap: 4px 12px; margin: 0 0 10px; }
.dd-ms-day { font-size: 14.5px; }
.dd-ms-list { margin: 12px 0 0; overflow-x: auto; }
.dd-ms-tab { width: 100%; border-collapse: collapse; }
.dd-ms-tab th, .dd-ms-tab td { text-align: left; padding: 6px 6px; border-top: 1px solid var(--border); font-size: 14.5px; vertical-align: middle; }
.dd-ms-tab thead th { font-size: 12.5px; color: var(--text-muted); border-top: 0; }
.dd-ms-tab tbody th a { color: var(--text); }
.dd-ms-tab input { width: 9em; }
.dd-ms-out { margin: 16px 0 0; }
.dd-ms-days2 { display: grid; grid-template-columns: 1fr; gap: 14px; }
@media (min-width: 900px) { .dd-ms-days2 { grid-template-columns: 1fr 1fr; } }
.dd-ms-tt { width: 100%; border-collapse: collapse; }
.dd-ms-tt th, .dd-ms-tt td { text-align: left; vertical-align: top; padding: 8px 6px; border-top: 1px solid var(--border); }
.dd-ms-tt tr:first-child th, .dd-ms-tt tr:first-child td { border-top: 0; }
.dd-ms-tt th { width: 34%; }
.dd-ms-time { display: block; font-family: 'Inter', sans-serif; font-weight: 800; font-size: 16px; font-variant-numeric: tabular-nums; }
.dd-ms-tt ul { margin: 0; padding: 0; list-style: none; }
.dd-ms-tt li { margin: 2px 0 4px; font-size: 15.5px; }
.dd-ms-dose { color: var(--text-mid); }
.dd-ms-warn { border-left: 4px solid #b91c1c; }
.dd-msw-list { list-style: none; margin: 0; padding: 0; }
.dd-msw, .dd-msw-pr { display: grid; grid-template-columns: minmax(150px, 220px) 1fr; gap: 4px 18px; padding: 12px 0; border-top: 1px solid var(--border); }
.dd-msw-list > li:first-child { border-top: 0; padding-top: 4px; }
.dd-msw-pr { grid-template-columns: 150px 1fr; }
.dd-msw-n { font-family: 'Inter', sans-serif; font-weight: 800; font-size: 15.5px; color: var(--text); }
.dd-msw-r p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--text); }
.dd-msw-tags { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-top: 6px; }
.dd-msw-tag { font-family: 'Inter', sans-serif; font-size: 11.5px; font-weight: 700; letter-spacing: .02em; padding: 2px 8px; border-radius: 999px; border: 1px solid; }
.dd-msw-tag.t-label { color: #0e4a50; background: #e1f5f0; border-color: rgba(14,74,80,.3); }
.dd-msw-tag.t-practice { color: #5b2a86; background: #f3ecfc; border-color: rgba(91,42,134,.3); }
.dd-msw-tag.t-you { color: #1f3864; background: #e8eef9; border-color: rgba(31,56,100,.3); }
.dd-msw-tag.t-evid { color: #7a3d00; background: #fff1de; border-color: rgba(122,61,0,.3); }
.dd-pc-head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px 16px; }
.dd-pc-head h3 { margin: 0; }
.dd-pc-head label { font-size: 14px; font-weight: 600; color: var(--text-mid); display: flex; align-items: center; gap: 8px; }
.dd-pc-head input { width: 5.5em; font: inherit; font-size: 15px; padding: 6px 8px; border: 1.5px solid var(--border); border-radius: 8px; background: var(--white); color: var(--text); }
.dd-pc-burden { margin: 10px 0 8px; font-size: 15px; }
.dd-pc-tab { width: 100%; border-collapse: collapse; font-size: 14.5px; }
.dd-pc-tab th { text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .05em; color: var(--text-muted); padding: 6px 8px; border-bottom: 1.5px solid var(--border); }
.dd-pc-tab td { padding: 7px 8px; border-bottom: 1px solid var(--border); vertical-align: top; }
.dd-pc-tab .dd-pc-num { font-variant-numeric: tabular-nums; white-space: nowrap; }
.dd-pc-note { margin: 8px 0 0; font-size: 13px; }
@media (max-width: 560px) { .dd-pc-tab th:nth-child(3), .dd-pc-tab td:nth-child(3) { display: none; } }
.dd-ms-samples { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-top: 12px; font-size: 14px; color: var(--text-mid); }
.dd-ms-use { display: block; margin-top: 6px; font-size: 13px; font-weight: 600; color: var(--text-mid); }
.dd-ms-use select { margin-left: 6px; font-size: 13.5px; padding: 4px 6px; }
.dd-msw-tag.t-std { color: #4b5563; background: #f1f3f6; border-color: rgba(75,85,99,.25); }
.dd-msw-by { font-size: 12.5px; color: var(--text-muted); }
.dd-msw-r .dd-ms-src { margin-top: 6px; }
.dd-msw-blk { margin-top: 22px; padding-top: 14px; border-top: 2px solid var(--border); }
.dd-msw-blk h4 { margin: 0 0 4px; font-size: 16px; }
.dd-msw-b { padding-top: 1px; }
.dd-msw-b .dd-ix-g { display: inline-block; min-width: 0; }
.dd-msw-pt { font-size: 15px; line-height: 1.5; color: var(--text); }
.dd-msw-d { display: block; color: var(--text-mid); margin-top: 2px; }
.dd-msw-st { display: inline-block; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 800; padding: 3px 9px; border-radius: 6px; }
.dd-msw-st.st-ok { color: #14532d; background: #dcf5e4; }
.dd-msw-st.st-no { color: #fff; background: #b91c1c; }
.dd-msw-st.st-warn { color: #5b3a00; background: #fdf3dc; }
.dd-msw-more { margin: 10px 0 0; font-weight: 700; }
@media (max-width: 640px) { .dd-msw, .dd-msw-pr { grid-template-columns: 1fr; gap: 4px; } }
.dd-ms-src summary { cursor: pointer; font-size: 13px; color: #0e4a50; display: inline; }
.dd-ms-src blockquote { margin: 6px 0; padding: 8px 12px; background: var(--bg); border-left: 3px solid var(--border); font-size: 14px; }
.dd-ms-src cite { display: block; font-style: normal; font-size: 12.5px; color: var(--text-muted); margin-top: 4px; }
.dd-ms-text { width: 100%; box-sizing: border-box; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13.5px; padding: 10px; border: 1.5px solid var(--border); border-radius: 10px; background: var(--white); color: var(--text); margin: 0 0 8px; }
/* Med Scheduler patient sheet: hidden on screen, the only thing printed once a schedule exists */
.mss { display: none; }
@media print {
  @page { margin: 12mm 12mm 14mm; }
  body.dd-ms-page:has(#ms-sheet) :is(body, main, #ms-out) > *:not(:has(#ms-sheet)):not(#ms-sheet) { display: none !important; }
  body.dd-ms-page:has(#ms-sheet) main { padding: 0 !important; margin: 0 !important; max-width: none !important; width: auto !important; }
  body.dd-ms-page:has(#ms-sheet) { background: #fff !important; }
  .dd-ms-page .site-header, .dd-ms-page .hero, .dd-ms-page footer.guide-footer, .dd-ms-page .float-controls, .dd-ms-page .float-controls-left, .dd-ms-page .print-btn { display: none !important; }
  .mss { display: block !important; color: #1e2a38 !important; font-family: 'Manrope', 'Inter', system-ui, sans-serif; font-size: 10.5pt; line-height: 1.35;
    -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .mss * { color: inherit; }
  .mss-head { display: flex; justify-content: space-between; align-items: flex-end; gap: 12px; border-bottom: 2.5pt solid #1a6b72; padding: 0 0 6pt; margin: 0 0 8pt; }
  .mss-kicker { font: 700 8pt 'Inter', sans-serif; letter-spacing: .12em; text-transform: uppercase; color: #1a6b72 !important; }
  .mss h1 { font: 800 19pt/1.1 'Inter', sans-serif; margin: 2pt 0 0; color: #13283f !important; }
  .mss-date { font-size: 9.5pt; color: #4b5a6e !important; white-space: nowrap; }
  .mss-fields { display: flex; gap: 18pt; margin: 4pt 0 6pt; font-size: 10pt; font-weight: 600; }
  .mss-fields div { flex: 1; display: flex; gap: 6pt; align-items: flex-end; }
  .mss-fields span { flex: 1; border-bottom: .75pt solid #8592a3; height: 13pt; }
  .mss-routine { margin: 0 0 10pt; font-size: 9.5pt; color: #3c4a5e !important; background: #eef6f6; border-radius: 4pt; padding: 5pt 8pt; }
  .mss-day { margin: 0 0 12pt; break-inside: avoid; }
  .mss h2 { font: 800 12.5pt 'Inter', sans-serif; margin: 0 0 4pt; color: #13283f !important; break-after: avoid; }
  .mss h2 span { font-weight: 600; font-size: 10pt; color: #1a6b72 !important; margin-left: 4pt; }
  .mss-tt { width: 100%; border-collapse: collapse; table-layout: fixed; }
  .mss-tt thead th { font: 700 8pt 'Inter', sans-serif; letter-spacing: .06em; text-transform: uppercase; text-align: left; color: #fff !important;
    background: #1a6b72 !important; padding: 4pt 6pt; }
  .mss-tt td { padding: 3pt 6pt; vertical-align: top; border-bottom: .5pt solid #d5dde6; }
  .mss-tt tr.mss-first td { border-top: 1pt solid #aebccb; }
  .mss-tt tbody tr { break-inside: avoid; }
  .mss-c-time { width: 22%; }
  .mss-c-how { width: 26%; color: #3c4a5e !important; font-size: 9.5pt; }
  td.mss-c-time { background: #f3f7f9 !important; }
  td.mss-c-time b { display: block; font: 800 12pt 'Inter', sans-serif; font-variant-numeric: tabular-nums; color: #13283f !important; }
  td.mss-c-time span { display: block; font-size: 8.5pt; color: #4b5a6e !important; margin-top: 1pt; }
  .mss-tt td b { font-weight: 700; }
  .mss-dose { color: #3c4a5e !important; }
  .mss-box { display: inline-block; width: 9pt; height: 9pt; border: .9pt solid #5b6b80; border-radius: 2pt; margin: 0 6pt -1pt 0; }
  .mss-other { margin: 0 0 10pt; break-inside: avoid; }
  .mss-pcs { margin: 0 0 10pt; break-inside: avoid; }
  .mss-pc td { padding: 2pt 6pt; font-size: 9.5pt; }
  .mss-pc thead th { padding: 3pt 6pt; }
  .mss-pcs h2 { margin-bottom: 3pt; }
  .mss-pc td.mss-num { white-space: nowrap; }
  .mss-pcb { margin: 4pt 0 0; font-size: 9.5pt; }
  .mss-other ul { margin: 0; padding-left: 14pt; }
  .mss-other li { margin: 2pt 0; }
  .mss-foot { border-top: .75pt solid #aebccb; padding-top: 4pt; margin-top: 4pt; font-size: 9pt; color: #3c4a5e !important; break-inside: avoid; }
  .mss-foot p { margin: 0 0 3pt; }
  .mss-src { color: #6b7789 !important; font-size: 8pt; white-space: nowrap; }
}
.dd-partof { font-size: 13.5px; margin: 6px 0 8px; color: var(--text-mid); }
.dd-rg { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }
.dd-rg a { display: flex; gap: 12px; align-items: flex-start; height: 100%; box-sizing: border-box; padding: 12px 14px; border: 1px solid var(--border);
  border-radius: 12px; background: var(--white); color: var(--text); text-decoration: none; }
.dd-rg a:hover, .dd-rg a:focus-visible { border-color: #1a6b72; box-shadow: 0 2px 10px rgba(26,107,114,.15); }
.dd-rg img { width: 72px; height: 72px; object-fit: cover; border-radius: 8px; flex: none; background: var(--bg); }
.dd-rg .dd-rg-k { display: block; font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #5b6b80; margin-bottom: 2px; }
.dd-rg .dd-rc-ico { width: 44px; height: 44px; padding: 10px; box-sizing: border-box; border-radius: 10px; flex: none; background: #e6f2f3; color: #0e4a50;
  fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.dd-rg .dd-rc-ico path { stroke-width: 2.6; }
.dd-rg .dd-rg-t { display: block; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 14.5px; color: #0e4a50; line-height: 1.35; }
.dd-rg .dd-rg-d { display: block; font-size: 13px; line-height: 1.5; color: var(--text-mid); margin-top: 4px;
  display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.dd-partof a { color: #0e4a50; font-weight: 700; }
.dd-partof .dd-sub-inline { color: var(--text-mid); font-size: 12.5px; }
.dd-tag.FSMP { color: #0b3a3f; background: #e3f2f2; border: 1px solid rgba(26,107,114,.4); }
.dd-facets { display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center; margin: 10px 0 4px; }
.dd-facets select { font: inherit; font-size: 14px; color: var(--text); background: var(--white); border: 1px solid #8a96a8; border-radius: 8px; padding: 7px 10px; min-height: 40px; max-width: 320px; }
.dd-facets > label:not(.dd-check) { flex: 0 1 260px; min-width: 0; max-width: 100%; }
.dd-facets > label:not(.dd-check) select { width: 100%; }
.dd-facets .dd-check { font-size: 14px; color: var(--text-mid); display: inline-flex; gap: 6px; align-items: center; }
.dd-facets .dd-check .dd-kidney-ico { width: 16px; height: 16px; color: #0e4a50; }
ul.dd-results li[aria-selected=true] { background: #eef2f8; outline: 2px solid #1a6b72; outline-offset: -2px; }
.dd-why { display: block; font-size: 12.5px; color: var(--text-mid); }
.dd-mbr { display: block; font-size: 13px; line-height: 1.55; color: var(--text-mid); margin-top: 2px; overflow-wrap: anywhere; }
.dd-mbr .dd-mbr-l { font-weight: 600; color: var(--text-mid); }
ul.dd-list .dd-mbr a { color: #0e4a50; font-weight: 600; text-decoration: underline; text-decoration-color: rgba(14,74,80,.35); text-underline-offset: 2px; }
ul.dd-list .dd-mbr a:hover { text-decoration-color: currentColor; }
.dd-mbr .dd-mbr-s { color: var(--text-muted); }
.dd-tags { display: block; margin-top: 3px; }
.dd-tags .dd-tag { margin-right: 3px; }
@media (max-width: 1023px) {
  .dd-layout { grid-template-columns: 1fr; padding: 0 20px; gap: 0; }
  .dd-toc { display: none; }
  body.dd-mono .nav-strip.dd-pills { display: block; }
  .dd-sec { scroll-margin-top: 112px; }
}
@media (max-width: 640px) {
  .dd-layout { padding: 0 16px; }
  .dd-twocol { grid-template-columns: 1fr; }
  .dd-kidney.dd-sec { padding: 16px 14px; }
  .dd-facets > label:not(.dd-check) { flex: 1 1 100%; }
  .dd-facets select { max-width: 100%; }
}
@media print { .dd-toc { display: none !important; } .dd-layout { display: block; } }
.dd-labgroup { margin: 8px 0; }
.dd-labgroup-h { font-family: 'Inter', sans-serif; font-weight: 700; font-size: 14px; color: var(--navy); margin: 6px 0; }
.dd-labpre { font-size: 14px; line-height: 1.6; color: var(--text-mid); background: var(--bg); border: 1px solid var(--border); border-radius: 10px; padding: 10px 14px; margin: 6px 0 8px; }
.dd-acc.dd-acc-sm { margin: 6px 0; border-radius: 10px; }
.dd-acc.dd-acc-sm > summary { font-size: 14px; padding: 10px 14px; }
.dd-acc.dd-acc-sm .dd-acc-body p { font-size: 14px; }
/* Kidney strip */
.dd-kstrip { display: grid; grid-template-columns: repeat(auto-fill, minmax(118px, 1fr)); gap: 8px; margin: 10px 0 8px; }
.dd-ktile { display: flex; flex-direction: column; gap: 2px; min-height: 86px; padding: 9px 10px; border-radius: 10px; text-decoration: none;
  border: 1px solid; border-top-width: 5px; background: var(--white); }
.dd-ktile:focus-visible { outline: 3px solid #1f3864; outline-offset: 2px; }
.dd-kt-h { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 800; letter-spacing: .03em; color: #1e2a38; }
.dd-kt-s { font-size: 13px; line-height: 1.3; color: #1e2a38; font-weight: 600; }
.dd-kt-l { margin-top: auto; font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; }
.dd-lv-none { border-color: #86c29b; border-top-color: #15803d; background: #f0fdf4; } .dd-lv-none .dd-kt-l { color: #166534; }
.dd-lv-adjust { border-color: #e8c27a; border-top-color: #d97706; background: #fffbeb; } .dd-lv-adjust .dd-kt-l { color: #92400e; }
.dd-lv-avoid { border-color: #f0a3a3; border-top-color: #b91c1c; background: #fff1f1; } .dd-lv-avoid .dd-kt-l { color: #991b1b; }
.dd-lv-nodata { border-color: #c5cbd5; border-top-color: #6b7280; background: #f5f6f8; } .dd-lv-nodata .dd-kt-l { color: #4a5568; }
dl.dd-kgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin: 6px 0; background: var(--white);
  border: 1px solid #cfe6e6; border-radius: 10px; overflow: hidden; }
.dd-kcell { padding: 8px 12px; border-bottom: 1px solid #e3efef; border-right: 1px solid #e3efef; scroll-margin-top: 120px; }
.dd-kcell:target { background: #fff7d6; }
.dd-kcell dt { font-size: 11.5px; font-weight: 700; color: #0e4a50; text-transform: uppercase; letter-spacing: .04em; }
.dd-kcell dd { margin: 2px 0 0; font-size: 13.5px; line-height: 1.5; color: var(--text-mid); }
ul.dd-kfoot { list-style: none; margin: 8px 0 0; padding: 0; font-size: 13px; color: var(--text-mid); }
ul.dd-kfoot li { margin: 3px 0; }
ul.dd-kfoot strong { color: #0e4a50; margin-right: 4px; }
.dd-kidney .dd-acc { margin: 8px 0; }
table.dd-pk tr.dd-pk-renal th, table.dd-pk tr.dd-pk-renal td { background: #e9f6f5; }
.dd-pk-kid { font-size: 10.5px; font-weight: 700; color: #fff; background: #1a6b72; border-radius: 5px; padding: 0 5px; margin-left: 4px; text-transform: uppercase; }
@media (max-width: 640px) {
  .dd-kstrip { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; }
  .dd-ktile { min-height: 92px; padding: 7px 6px; }
  .dd-kt-s { font-size: 11.5px; } .dd-kt-h { font-size: 11px; } .dd-kt-l { font-size: 9.5px; }
  dl.dd-kgrid { grid-template-columns: 1fr; }
}
/* Brands line under the h1 */
.dd-brands { font-size: 14px; line-height: 1.7; color: #34455f; margin: -4px 0 10px; }
.dd-brands strong { color: #1f3864; }
.dd-brands a.dd-brand-link { color: #1f3864; text-decoration: none; border-bottom: 1px dotted rgba(31,56,100,.5); font-weight: 600; }
.dd-brands a.dd-brand-link:hover { border-bottom-style: solid; }
.dd-brands-more { display: inline; }
.dd-brands-more > summary { display: inline; cursor: pointer; list-style: none; font-weight: 700; color: #0e4a50; margin-left: 6px; }
.dd-brands-more > summary::-webkit-details-marker { display: none; }
.dd-brands-more[open] > summary { display: none; }
.dd-brands-rest::before { content: " · "; }
.dd-brands-acc > summary { cursor: pointer; list-style: none; display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px; }
.dd-brands-acc > summary::-webkit-details-marker { display: none; }
.dd-brands-acc > summary::before { content: "▸"; font-size: 12px; color: #0e4a50; transition: transform .15s; display: inline-block; }
.dd-brands-acc[open] > summary::before { transform: rotate(90deg); }
.dd-brands-preview { color: #4a5a72; overflow: hidden; text-overflow: ellipsis; }
.dd-brands-hint { font-size: 12px; font-weight: 700; color: #0e4a50; text-decoration: underline dotted; }
.dd-brands-acc[open] .dd-brands-preview { display: none; }
.dd-brands-acc[open] .dd-brands-hint { font-size: 0; }
.dd-brands-acc[open] .dd-brands-hint::after { content: "Hide"; font-size: 12px; }
.dd-brands-all { margin-top: 6px; }
.dd-prod-acc { border: 1px solid var(--border); border-radius: 12px; margin: 12px 0; background: var(--white); }
.dd-prod-acc > summary { cursor: pointer; list-style: none; padding: 14px 18px; font-family: 'Inter', sans-serif;
  font-weight: 600; font-size: 15.5px; color: var(--navy); display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.dd-prod-acc > summary::-webkit-details-marker { display: none; }
.dd-prod-acc > summary::after { content: "+"; font-size: 20px; line-height: 1; color: #1a6b72; }
.dd-prod-acc[open] > summary::after { content: "\2212"; }
.dd-prod-acc > summary:focus-visible { outline: 2px solid #1a6b72; outline-offset: 2px; border-radius: 12px; }
.dd-prod-acc[open] > summary { border-bottom: 1px solid var(--border); }
.dd-prod-acc > .dd-toolbar, .dd-prod-acc > .dd-table-wrap { margin-left: 14px; margin-right: 14px; }
.dd-prod-acc > :last-child { margin-bottom: 14px; }
.dd-prod-acc-n { font-size: 12px; font-weight: 700; color: #0e4a50; background: #e6f2f3; border-radius: 999px; padding: 2px 9px; margin-left: 8px; }
@media print { .dd-prod-acc > summary { display: none; } }
/* At a glance card */
.dd-glance { margin: 36px 0 0; background: var(--white); border: 1px solid #c9d3e3; border-top: 4px solid #1f3864;
  border-radius: 14px; padding: 18px 22px 8px; box-shadow: 0 1px 3px rgba(31,56,100,.06); }
.dd-glance h2 { font-family: 'Inter', sans-serif; font-size: 20px; color: var(--navy); margin: 0 0 6px; }
.dd-glance-dl { margin: 0; }
.dd-glance-row { display: grid; grid-template-columns: 190px 1fr; gap: 16px; padding: 11px 0; border-top: 1px solid var(--border); }
.dd-glance-row:first-child { border-top: 0; }
.dd-glance dt { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; color: #1f3864; padding-top: 2px; }
.dd-glance dd { margin: 0; font-size: 14.5px; line-height: 1.6; color: var(--text-mid); }
.dd-glance a { color: #1a6b72; font-weight: 600; }
ul.dd-glance-list { margin: 0 0 4px 18px; padding: 0; }
ul.dd-glance-list li { margin: 2px 0; }
.dd-src { display: inline-block; font-size: 11px; font-weight: 600; color: var(--text-muted); background: var(--bg);
  border: 1px solid var(--border); border-radius: 6px; padding: 0 6px; margin-left: 2px; white-space: normal; }
.dd-glance-sub { display: block; font-size: 12.5px; color: var(--text-muted); margin-top: 3px; }
.dd-sev { font-size: 11px; font-weight: 700; color: #7a1d1d; background: #fdecec; border-radius: 6px; padding: 0 6px; }
ul.dd-srclist { margin: 4px 0 8px 18px; }
ul.dd-srclist li { margin: 2px 0; overflow-wrap: anywhere; }
@media (max-width: 640px) {
  .dd-glance { padding: 14px 16px 6px; }
  .dd-glance-row { grid-template-columns: 1fr; gap: 4px; }
}
.dd-hidden { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.dd-letter.dd-kempty, .dd-letter.dd-hidden { display: none !important; }
/* render off-screen letter groups lazily (big win on phones; the index lists 2,300+ generics) */
.dd-letter { content-visibility: auto; contain-intrinsic-size: auto 1200px; }
#dd-alpha.dd-hidden { display: none !important; }
/* Kidney dosing panel */
.dd-kidney { margin: 36px 0 8px; padding: 22px 24px 18px; background: #f2f9f9; border: 1px solid #cfe6e6;
  border-left: 6px solid #1a6b72; border-radius: 14px; }
.dd-kidney-head { display: flex; gap: 14px; align-items: center; margin-bottom: 10px; }
.dd-kidney-head .section-tag { margin-bottom: 2px; color: #0e4a50; }
.dd-kidney h2 { font-family: 'Inter', sans-serif; font-size: 24px; color: var(--navy); margin: 0; }
.dd-kidney-ico { width: 22px; height: 22px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; flex: none; }
.dd-kidney-head .dd-kidney-ico { width: 44px; height: 44px; padding: 9px; border-radius: 12px; background: #1a6b72; color: #fff; }
.dd-kidney-sum { font-size: 15px; color: var(--text-mid); margin: 6px 0 12px; }
.dd-kidney-sub { font-family: "Inter", sans-serif; font-size: 16px; font-weight: 700; color: var(--text); margin: 18px 0 8px; }
table.dd-kidney-table { width: 100%; border-collapse: collapse; font-size: 14px; background: var(--white); border-radius: 10px; overflow: hidden; }
.dd-kidney-table th { text-align: left; width: 34%; padding: 10px 14px; color: #0e4a50; font-weight: 700; background: #e1f2f1; border-bottom: 1px solid #cfe6e6; vertical-align: top; }
.dd-kidney-table td { padding: 10px 14px; color: var(--text-mid); border-bottom: 1px solid #cfe6e6; }
.dd-kidney-table tr:last-child th, .dd-kidney-table tr:last-child td { border-bottom: 0; }
.dd-kidney-label { background: var(--white); border: 1px solid #cfe6e6; border-radius: 10px; padding: 6px 16px 8px; max-height: 420px; overflow: auto; }
.dd-kidney-label p { font-size: 14px; color: var(--text-mid); margin: 8px 0; white-space: pre-line; text-align: left; }
.dd-kidney-src { font-size: 11.5px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #0e4a50; margin-top: 8px; }
.dd-kidney .dd-note { margin-top: 10px; }
.dd-kidney-pending { font-size: 13.5px; font-weight: 600; color: #0e4a50; margin: 10px 0 0; }
/* Parenteral nutrition brand kidney notes (data/drugs/pn-notes) */
.dd-tag.KN { color: #fff; background: #0e4a50; text-decoration: none; }
.dd-tag.KN:hover, .dd-tag.KN:focus-visible { background: #1a6b72; text-decoration: underline; }
.dd-pnn { background: var(--white); border: 1px solid #cfe6e6; border-radius: 12px; padding: 14px 18px 10px; margin: 16px 0 0; scroll-margin-top: 90px; }
.dd-pnn-h { font-family: 'Inter', sans-serif; font-size: 19px; color: var(--navy); margin: 0 0 6px; }
.dd-pnn .dd-kidney-sub { font-size: 15px; margin: 14px 0 6px; }
.dd-pnn .dd-uselist li { font-size: 14px; color: var(--text-mid); }
table.dd-pncomp { font-size: 13.5px; }
table.dd-pncomp th[scope=row] { text-align: left; font-weight: 600; color: var(--text); white-space: nowrap; }
table.dd-pncomp td { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
.dd-pn-na { font-size: 12px; font-style: italic; color: var(--text-muted); }
.dd-pn-bottom { font-weight: 600; color: var(--text); background: #e1f2f1; border-radius: 8px; padding: 10px 14px; margin: 4px 0 8px; }
@media print {
  .dd-pnn { break-inside: auto; border-color: #999; }
  .dd-pnn-h, .dd-pnn .dd-kidney-sub { break-after: avoid; }
  table.dd-pncomp tr { break-inside: avoid; }
  .dd-pn-bottom { background: none; border: 1px solid #999; }
}
.dd-chip.dd-kchip { display: inline-flex; align-items: center; gap: 6px; color: #fff; background: #0e4a50; border-color: #0e4a50; }
.dd-chip.dd-kchip .dd-kidney-ico { width: 15px; height: 15px; }
.dd-kbadge { display: inline-flex; vertical-align: middle; margin-left: 6px; color: #0e4a50; background: #e1f2f1; border-radius: 6px; padding: 2px; }
.dd-kbadge .dd-kidney-ico { width: 15px; height: 15px; }
.dd-kfilter { display: inline-flex; align-items: center; gap: 8px; font-size: 14px; color: var(--text-mid); margin: 8px 0 0; }
.dd-kfilter .dd-kidney-ico { width: 17px; height: 17px; color: #0e4a50; }
@media (max-width: 760px) {
  .dd-table thead { display: none; }
  .dd-table, .dd-table tbody, .dd-table tr, .dd-table td { display: block; width: 100%; }
  .dd-table tr { border-bottom: 1px solid var(--border); padding: 8px 0; }
  .dd-table td { border: 0; padding: 4px 14px; display: grid; grid-template-columns: 112px 1fr; gap: 10px; }
  .dd-table td::before { content: attr(data-label); font-size: 11.5px; font-weight: 700; color: var(--text-muted);
    text-transform: uppercase; letter-spacing: .04em; padding-top: 2px; }
  .dd-table td > div:empty, .dd-table td:has(> div:empty) { display: none; }
  .dd-count { margin-left: 0; width: 100%; }
  .dd-toolbar .dd-sort-sel { display: block; flex: 1 1 100%; }
  .dd-toolbar select { flex: 1 1 100%; }
  .container.dd-wide { padding: 0 16px; }
}
@media print {
  .dd-toolbar, .dd-alpha, .dd-browse-wrap, .dd-search, .float-controls, .print-btn, .scroll-top-btn, .nav-strip { display: none !important; }
  .dd-acc .dd-acc-body { display: block !important; }
}
/* Dark mode (aliased to body.dark-mode by the generator) */
html[data-theme="dark"] .dd-crumb { color: rgba(238,242,251,.78); }
html[data-theme="dark"] .dd-crumb a { color: #dbe6f5; }
html[data-theme="dark"] .dd-chip { color: #eef2fb; background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.3); }
html[data-theme="dark"] .dd-chip.dd-rx { color: #fecaca; background: rgba(248,113,113,.14); border-color: rgba(248,113,113,.45); }
html[data-theme="dark"] .dd-chip.dd-otc { color: #bbf7d0; background: rgba(74,222,128,.12); border-color: rgba(74,222,128,.4); }
html[data-theme="dark"] .dd-chip.dd-good { color: #a5f3fc; background: rgba(43,168,176,.14); border-color: rgba(43,168,176,.45); }
html[data-theme="dark"] .hero-meta .dd-meta-time { color: #eef2fb; }
html[data-theme="dark"] .dd-sched { color: #c9d3e1; }
html[data-theme="dark"] .dd-sched strong, html[data-theme="dark"] .dd-sched time { color: #eef2fb; }
html[data-theme="dark"] .dd-sched svg { stroke: #7dd3dc; }
html[data-theme="dark"] .dd-btn { background: #2a4a80; border-color: #4a6aa0; color: #fff; }
html[data-theme="dark"] .dd-btn:hover { background: #335a98; }
html[data-theme="dark"] .dd-btn.dd-btn-ghost { background: transparent; color: #dbe6f5; border-color: rgba(219,230,245,.4); }
html[data-theme="dark"] .dd-toolbar input[type=search], html[data-theme="dark"] .dd-toolbar select,
html[data-theme="dark"] .dd-search input { background: #1a2535; color: var(--text); border-color: #4a5a72; }
html[data-theme="dark"] .dd-table-wrap, html[data-theme="dark"] .dd-acc { background: #1a2535; border-color: #2a3548; }
html[data-theme="dark"] .dd-table th { background: #22304a; color: #dbe6f5; border-color: #2a3548; }
html[data-theme="dark"] .dd-table td { border-color: #2a3548; color: var(--text-mid); }
html[data-theme="dark"] .dd-table tbody tr:hover td { background: #202d40; }
html[data-theme="dark"] .dd-table a, html[data-theme="dark"] .dd-attrib a, html[data-theme="dark"] ul.dd-list a { color: #7fd3da; }
html[data-theme="dark"] .dd-tag.Rx { color: #fecaca; background: rgba(248,113,113,.16); }
html[data-theme="dark"] .dd-tag.OTC { color: #bbf7d0; background: rgba(74,222,128,.14); }
html[data-theme="dark"] .dd-tag.HR { color: #fde68a; background: rgba(251,191,36,.14); }
html[data-theme="dark"] .dd-past { color: #fca5a5; }
html[data-theme="dark"] .dd-acc > summary { color: #eef2fb; }
html[data-theme="dark"] .dd-acc > summary::after { color: #7fd3da; }
html[data-theme="dark"] .dd-acc .dd-acc-body { border-color: #2a3548; }
html[data-theme="dark"] .dd-acc.dd-boxed { border-color: #f87171; }
html[data-theme="dark"] .dd-acc.dd-boxed > summary { color: #fecaca; }
html[data-theme="dark"] .dd-attrib { background: #16233a; border-color: #2c3a52; }
html[data-theme="dark"] pre.dd-pre { background: #141c2a; border-color: #2c3a52; color: var(--text); }
html[data-theme="dark"] .dd-eu-h { color: var(--text); }
html[data-theme="dark"] .dd-src-eu { color: #dbe6f5; background: #22304a; border-color: #4a5a72; }
html[data-theme="dark"] .dd-placeholder { background: #141c2a; border-color: #4a5a72; }
html[data-theme="dark"] .dd-alpha button { background: #1a2535; color: #dbe6f5; border-color: #3a4a62; }
html[data-theme="dark"] .dd-browse { background: #141c2a; border-color: #3a4a62; }
html[data-theme="dark"] .dd-browse button { color: #dbe6f5; }
html[data-theme="dark"] .dd-browse button:hover { background: rgba(219,230,245,.08); }
html[data-theme="dark"] .dd-browse button[aria-selected=true] { background: #dbe6f5; color: #0f1520; }
html[data-theme="dark"] .dd-browse button:focus-visible { outline-color: #7fd3da; }
html[data-theme="dark"] .dd-browse-l { color: #9ba6b8; }
html[data-theme="dark"] .dd-vg { border-color: #2a3548; }
html[data-theme="dark"] details.dd-vg > summary, html[data-theme="dark"] .dd-vletter h2 { color: #eef2fb; }
html[data-theme="dark"] details.dd-vg > summary::before { color: #7fd3da; }
html[data-theme="dark"] .dd-vg-n { background: #16323a; color: #a5eef2; }
html[data-theme="dark"] .dd-vg-link a { color: #7fd3da; }
html[data-theme="dark"] .dd-alpha button[aria-pressed=true] { background: #dbe6f5; color: #0f1520; border-color: #dbe6f5; }
html[data-theme="dark"] .dd-letter h2 { color: #eef2fb; border-color: #2a3548; }
html[data-theme="dark"] ul.dd-list li { border-color: #2a3548; }
html[data-theme="dark"] mark.dd-hl { background: #5c4a00; color: #fff; }
html[data-theme="dark"] .dd-attrib, html[data-theme="dark"] .dd-acc-body { color: var(--text-mid); }
html[data-theme="dark"] .disclaimer a, html[data-theme="dark"] .dd-acc-body a, html[data-theme="dark"] .dd-kidney a,
html[data-theme="dark"] .dd-note a { color: #7fd3da; }
html[data-theme="dark"] .dd-labgroup-h { color: #eef2fb; }
html[data-theme="dark"] .dd-labpre { background: #141c2a; border-color: #2a3548; }
html[data-theme="dark"] .dd-kt-h, html[data-theme="dark"] .dd-kt-s { color: #eef2fb; }
html[data-theme="dark"] .dd-lv-none { background: #0e2a1c; border-color: #2f6b45; border-top-color: #4ade80; } html[data-theme="dark"] .dd-lv-none .dd-kt-l { color: #86efac; }
html[data-theme="dark"] .dd-lv-adjust { background: #2a1d05; border-color: #6b4f12; border-top-color: #fbbf24; } html[data-theme="dark"] .dd-lv-adjust .dd-kt-l { color: #fde68a; }
html[data-theme="dark"] .dd-lv-avoid { background: #2a1212; border-color: #7a2a2a; border-top-color: #f87171; } html[data-theme="dark"] .dd-lv-avoid .dd-kt-l { color: #fecaca; }
html[data-theme="dark"] .dd-lv-nodata { background: #1a2230; border-color: #3a4658; border-top-color: #9ba6b8; } html[data-theme="dark"] .dd-lv-nodata .dd-kt-l { color: #c9d3e1; }
html[data-theme="dark"] dl.dd-kgrid { background: #1a2535; border-color: #23414a; }
html[data-theme="dark"] .dd-kcell { border-color: #23414a; }
html[data-theme="dark"] .dd-kcell:target { background: #3a3110; }
html[data-theme="dark"] .dd-kcell dt, html[data-theme="dark"] ul.dd-kfoot strong { color: #a5eef2; }
html[data-theme="dark"] table.dd-pk tr.dd-pk-renal th, html[data-theme="dark"] table.dd-pk tr.dd-pk-renal td { background: #10323a; }
html[data-theme="dark"] .dd-pk-kid { background: #0e4a50; color: #e6fbfc; }
html[data-theme="dark"] .dd-toc a { color: #c9d3e1; }
html[data-theme="dark"] .dd-toc a:hover { background: #1a2535; color: #fff; }
html[data-theme="dark"] .dd-toc a[aria-current] { color: #7fd3da; border-left-color: #7fd3da; }
html[data-theme="dark"] .dd-toc ol { border-color: #2a3548; }
html[data-theme="dark"] .dd-sec { border-color: #2a3548; }
html[data-theme="dark"] .dd-sec > h2, html[data-theme="dark"] .dd-sec h3 { color: #eef2fb; }
html[data-theme="dark"] .dd-kidney-table tr.dd-kgroup th { background: #0e4a50; color: #e6fbfc; }
html[data-theme="dark"] .dd-src-ours { color: #a5f3fc; background: #10323a; border-color: #23414a; }
html[data-theme="dark"] .dd-boxed-alert { background: #2a1515; border-color: #f87171; }
html[data-theme="dark"] .dd-boxed-h { color: #fecaca; }
html[data-theme="dark"] .dd-boxed-body { color: #fde2e2; }
html[data-theme="dark"] .dd-pk-hi { background: #16233a; border-left-color: #6f8fd0; }
html[data-theme="dark"] ol.dd-refs a { color: #7fd3da; }
html[data-theme="dark"] .dd-sev-avoid { background: #b91c1c; color: #fff; }
html[data-theme="dark"] .dd-sev-adjust { background: #5c4a00; color: #fde68a; }
html[data-theme="dark"] .dd-sev-minor { background: #22304a; color: #dbe6f5; }
html[data-theme="dark"] .dd-usbrand, html[data-theme="dark"] .dd-dispnote { color: rgba(238,242,251,.82); }
html[data-theme="dark"] .dd-alias { background: #10303a; border-color: #4fb3bb; color: #e6f2f4; }
html[data-theme="dark"] .dd-alias-soft { background: #16233a; }
html[data-theme="dark"] .dd-alias a, html[data-theme="dark"] .dd-also a, html[data-theme="dark"] .dd-arrow { color: #7fd3da; }
html[data-theme="dark"] .dd-varnote { color: #f6c27a; }
html[data-theme="dark"] .dd-dispnote a { color: #dbe6f5; }
html[data-theme="dark"] .dd-chip.dd-hr { color: #fde68a; background: rgba(251,191,36,.14); border-color: rgba(251,191,36,.4); }
html[data-theme="dark"] .dd-chip.dd-s2 { color: #fff; background: #b91c1c; border-color: #f87171; }
html[data-theme="dark"] .dd-chip.dd-cp { color: #2a1900; background: #fbbf24; border-color: #fbbf24; }
html[data-theme="dark"] .dd-tag.PNF { color: #a5f3fc; background: #10323a; }
html[data-theme="dark"] .dd-tag.KD { color: #e6fbfc; background: #0e4a50; }
html[data-theme="dark"] .dd-tag.NX { color: #ffe8dc; background: #7c2d12; }
html[data-theme="dark"] .dd-chip.dd-nxchip { color: #fed7c3; background: rgba(234,88,12,.16); border-color: rgba(251,146,60,.5); }
html[data-theme="dark"] .dd-nx-item { background: #1a2535; border-color: rgba(255,255,255,.14); border-left-color: #fb923c; }
html[data-theme="dark"] .dd-nx-m { color: #fed7c3; background: rgba(234,88,12,.18); }
html[data-theme="dark"] .dd-nx-q { background: rgba(255,255,255,.04); border-left-color: rgba(255,255,255,.25); color: #d4dbe7; }
html[data-theme="dark"] .dd-nx-q cite { color: #9ba6b8; }
html[data-theme="dark"] .dd-nx-q cite a { color: #7dd3dc; }
html[data-theme="dark"] .dd-ix-pick, html[data-theme="dark"] .dd-ix-card, html[data-theme="dark"] .dd-ix-sug { background: #1a2535; border-color: rgba(255,255,255,.14); }
html[data-theme="dark"] #dd-ix-q, html[data-theme="dark"] .dd-ix-k select, html[data-theme="dark"] .dd-ix-paste textarea { background: #0f1724; color: #e6ebf3; border-color: rgba(255,255,255,.22); }
html[data-theme="dark"] .dd-ix-sug li[aria-selected="true"], html[data-theme="dark"] .dd-ix-sug li:hover { background: rgba(43,168,176,.18); }
html[data-theme="dark"] .dd-ix-chip { background: rgba(43,168,176,.16); border-color: rgba(43,168,176,.45); }
html[data-theme="dark"] .dd-ix-chip a, html[data-theme="dark"] .dd-ix-chip button, html[data-theme="dark"] .dd-ix-qgo,
html[data-theme="dark"] .dd-ix-paste summary, html[data-theme="dark"] .dd-ix-have { color: #a5f3fc; }
html[data-theme="dark"] .dd-ix-star.is-on { color: #fcd34d; }
html[data-theme="dark"] .dd-ix-q { background: rgba(255,255,255,.06); color: #e6ebf3; border-color: rgba(255,255,255,.22); }
html[data-theme="dark"] .dd-ix-q.is-on { color: #9ba6b8; }
html[data-theme="dark"] .dd-ix-g.g-ci { background: #991b1b; }
html[data-theme="dark"] .dd-ix-g.g-minor { color: #e3e8f2; background: #34455f; }
html[data-theme="dark"] .dd-ix-tw { color: #fecaca; }
html[data-theme="dark"] .dd-ix-ktab th a { color: #e6ebf3; }
html[data-theme="dark"] .dd-ix-card a { color: #7dd3dc; }
html[data-theme="dark"] .dd-ms-times input, html[data-theme="dark"] .dd-ms-tab input, html[data-theme="dark"] .dd-ms-tab select, html[data-theme="dark"] .dd-ms-text { background: #0f1724; color: #e6ebf3; border-color: rgba(255,255,255,.22); }
html[data-theme="dark"] .dd-ms-hd { border-color: rgba(255,255,255,.18); }
html[data-theme="dark"] .dd-ms-tab tbody th a { color: #e6ebf3; }
html[data-theme="dark"] .dd-ms-src summary { color: #7dd3dc; }
html[data-theme="dark"] .dd-msw-tag.t-label { color: #a7f3e6; background: rgba(20,120,110,.22); border-color: rgba(167,243,230,.3); }
html[data-theme="dark"] .dd-msw-tag.t-practice { color: #e2cffb; background: rgba(124,58,237,.22); border-color: rgba(226,207,251,.3); }
html[data-theme="dark"] .dd-msw-tag.t-you { color: #c7d7f5; background: rgba(59,90,160,.28); border-color: rgba(199,215,245,.3); }
html[data-theme="dark"] .dd-msw-tag.t-evid { color: #fcd9a8; background: rgba(180,83,9,.25); border-color: rgba(252,217,168,.3); }
html[data-theme="dark"] .dd-msw-tag.t-std { color: #d1d5db; background: rgba(255,255,255,.07); border-color: rgba(209,213,219,.25); }
html[data-theme="dark"] .dd-msw-st.st-ok { color: #bbf7d0; background: rgba(22,101,52,.35); }
html[data-theme="dark"] .dd-msw-st.st-warn { color: #fde68a; background: rgba(146,64,14,.35); }
html[data-theme="dark"] .dd-ms-src blockquote { background: rgba(255,255,255,.04); border-left-color: rgba(255,255,255,.25); }
html[data-theme="dark"] .dd-ms-warn { border-left-color: #f87171; }
html[data-theme="dark"] .dd-ix-kt.k-none { color: #bbf7d0; background: rgba(34,197,94,.16); }
html[data-theme="dark"] .dd-ix-kt.k-adjust { color: #fde68a; background: rgba(245,158,11,.16); }
html[data-theme="dark"] .dd-ix-kt.k-avoid { color: #fecaca; background: rgba(239,68,68,.18); }
html[data-theme="dark"] .dd-ix-kt.k-nodata, html[data-theme="dark"] .dd-ix-kt.k-hide { color: #d4dbe7; background: rgba(255,255,255,.08); }
html[data-theme="dark"] .dd-ix-kidney { border-left-color: #2ba8b0; }
html[data-theme="dark"] .dd-favbtn.is-on { color: #fde68a; background: rgba(245,158,11,.16); border-color: rgba(245,158,11,.45); }
html[data-theme="dark"] .dd-chip.dd-ixbtn, html[data-theme="dark"] .dd-chip.dd-ixchip { color: #e6fbfc; background: #0e4a50; border-color: #0e4a50; }
html[data-theme="dark"] .dd-tag.US { color: #dbe6f5; background: #22304a; }
html[data-theme="dark"] .dd-tag.SUP { color: #e5e9f0; background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.3); }
html[data-theme="dark"] .dd-tag.SUPK { color: #fde7c2; background: rgba(245,158,11,.16); }
html[data-theme="dark"] .dd-tag.HEP { color: #e6dcff; background: rgba(139,92,246,.2); }
html[data-theme="dark"] .dd-tag.KN { color: #e6fbfc; background: #0e4a50; border: 1px solid #2ba8b0; }
html[data-theme="dark"] .dd-pnn { background: #1a2535; border-color: #23414a; }
html[data-theme="dark"] .dd-pnn-h { color: #eef2fb; }
html[data-theme="dark"] .dd-pn-bottom { background: #10323a; color: #eef2fb; }
html[data-theme="dark"] .dd-pn-na { color: #9ba6b8; }
html[data-theme="dark"] .dd-partof a { color: #7fd3da; }
html[data-theme="dark"] .dd-rg a { background: #1a2535; border-color: rgba(255,255,255,.14); color: #e5e9f0; }
html[data-theme="dark"] .dd-rg a:hover, html[data-theme="dark"] .dd-rg a:focus-visible { border-color: #7fd3da; }
html[data-theme="dark"] .dd-rg .dd-rg-t { color: #a5f3fc; }
html[data-theme="dark"] .dd-rg .dd-rg-k { color: #aeb9c8; }
html[data-theme="dark"] .dd-rg .dd-rc-ico { background: #0e4a50; color: #e6fbfc; }
html[data-theme="dark"] .dd-rg .dd-rg-d { color: #cbd3df; }
html[data-theme="dark"] .dd-tag.FSMP { color: #c9f0f1; background: rgba(43,168,176,.16); border-color: rgba(43,168,176,.45); }
html[data-theme="dark"] .dd-tag.S2 { color: #fff; background: #b91c1c; }
html[data-theme="dark"] .dd-tag.CP { color: #2a1900; background: #fbbf24; }
html[data-theme="dark"] .dd-facets select { background: #1a2535; color: var(--text); border-color: #4a5a72; }
html[data-theme="dark"] .dd-facets .dd-check .dd-kidney-ico { color: #7fd3da; }
html[data-theme="dark"] ul.dd-list .dd-mbr a { color: #7fd3da; text-decoration-color: rgba(127,211,218,.45); }
html[data-theme="dark"] ul.dd-results li[aria-selected=true] { background: #1e3040; outline-color: #7fd3da; }
html[data-theme="dark"] .dd-brands { color: rgba(238,242,251,.82); }
html[data-theme="dark"] .dd-brands strong, html[data-theme="dark"] .dd-brands a.dd-brand-link { color: #eef2fb; border-bottom-color: rgba(238,242,251,.5); }
html[data-theme="dark"] .dd-brands-more > summary { color: #7fd3da; }
html[data-theme="dark"] .dd-brands-acc > summary::before, html[data-theme="dark"] .dd-brands-hint { color: #7fd3da; }
html[data-theme="dark"] .dd-brands-preview { color: rgba(238,242,251,.78); }
html[data-theme="dark"] .dd-prod-acc { background: #1a2535; border-color: #3a4a63; }
html[data-theme="dark"] .dd-prod-acc > summary { color: #eef2fb; }
html[data-theme="dark"] .dd-prod-acc > summary::after { color: #7fd3da; }
html[data-theme="dark"] .dd-prod-acc-n { background: #0e4a50; color: #eef2fb; }
html[data-theme="dark"] .dd-glance { background: #1a2535; border-color: #2c3a52; border-top-color: #6f8fd0; box-shadow: none; }
html[data-theme="dark"] .dd-glance h2 { color: #eef2fb; }
html[data-theme="dark"] .dd-glance-row { border-color: #2a3548; }
html[data-theme="dark"] .dd-glance dt { color: #b9c9ea; }
html[data-theme="dark"] .dd-glance a { color: #7fd3da; }
html[data-theme="dark"] .dd-src { background: #141c2a; border-color: #2c3a52; color: #b4bfcf; }
html[data-theme="dark"] .dd-sev { color: #fecaca; background: rgba(248,113,113,.16); }
html[data-theme="dark"] .dd-kidney { background: #10232a; border-color: #23414a; border-left-color: #2ba8b0; }
html[data-theme="dark"] .dd-kidney h2 { color: #eef2fb; }
html[data-theme="dark"] .dd-kidney-head .section-tag, html[data-theme="dark"] .dd-kidney-src,
html[data-theme="dark"] .dd-kidney-pending { color: #7fd3da; }
html[data-theme="dark"] .dd-kidney-head .dd-kidney-ico { background: #0e4a50; color: #e6fbfc; }
html[data-theme="dark"] table.dd-kidney-table, html[data-theme="dark"] .dd-kidney-label { background: #1a2535; border-color: #23414a; }
html[data-theme="dark"] .dd-kidney-table th { background: #16323a; color: #a5eef2; border-color: #23414a; }
html[data-theme="dark"] .dd-kidney-table td { border-color: #23414a; }
html[data-theme="dark"] .dd-chip.dd-kchip { background: #0e4a50; border-color: #2ba8b0; color: #fff; }
html[data-theme="dark"] .dd-kbadge { background: #16323a; color: #a5eef2; }
html[data-theme="dark"] .dd-kfilter .dd-kidney-ico { color: #7fd3da; }
html[data-theme="dark"] .dd-aka { color: rgba(238,242,251,.82); }
html[data-theme="dark"] .dd-aka > span { color: #eef2fb; }
html[data-theme="dark"] .dd-aka strong { color: #a5eef2; }
html[data-theme="dark"] .dd-comp { background: #1a2535; border-color: #2c3a52; border-left-color: #2ba8b0; }
html[data-theme="dark"] .dd-comp-none { border-left-color: #6b7a90; }
html[data-theme="dark"] .dd-comp-h a { color: #7fd3da; }
html[data-theme="dark"] .dd-comp-h .dd-sub, html[data-theme="dark"] .dd-comp-none .dd-sub { color: #b4bfcf; }
html[data-theme="dark"] .dd-comp-kid { background: #10232a; border-color: #23414a; }
html[data-theme="dark"] .dd-comp-kh { color: #a5eef2; }
html[data-theme="dark"] .dd-comp-kh .dd-kidney-ico { color: #a5eef2; }
html[data-theme="dark"] .dd-comp-caveat { color: #fde68a; background: #2a1d05; border-color: #6b4f12; }

/* Readability (Nov 17 2026): 16 px body text, ~72-character lines, darker text, more line spacing */
.dd-sec p, .dd-sec li, .dd-acc .dd-acc-body, .section .dd-acc-body p, .dd-acc-body p, .dd-acc-body li, .dd-labpre,
.dd-lead, .dd-kidney-sum, ul.dd-uselist li, .dd-comp-intro { font-size: 16px; line-height: 1.7; color: var(--text); }
.dd-sec p, .dd-sec ul, .dd-sec ol, .dd-acc-body p, .dd-acc-body ul, .dd-acc-body ol, .dd-labpre, .dd-lead,
.dd-kidney-sum, .dd-comp-intro { max-width: 72ch; }
.dd-acc-body p { margin: 0 0 12px; }
.dd-acc-body p:first-child { margin-top: 12px; }
.dd-acc-body li, .dd-labpre li, .dd-sec li { margin: 0 0 6px; }
.dd-labpre { padding: 12px 18px; }
.dd-labpre ul { margin: 0; padding-left: 20px; }
.dd-labpre p { margin: 0 0 8px; }
.dd-acc > summary span { line-height: 1.4; }
.dd-note { font-size: 14px; line-height: 1.6; }

/* Installed app: bottom app bar (no browser toolbar in standalone mode) */
html.dd-standalone body { padding-bottom: calc(76px + env(safe-area-inset-bottom, 0px)); }
.dd-appbar { position: fixed; left: 50%; transform: translateX(-50%); bottom: calc(12px + env(safe-area-inset-bottom, 0px));
  z-index: 9000; display: flex; gap: 2px; padding: 5px; border-radius: 999px; background: #1f3864;
  box-shadow: 0 6px 22px rgba(15,30,51,.28); }
.dd-appbar a, .dd-appbar button { display: inline-flex; align-items: center; gap: 6px; min-height: 44px; padding: 0 14px;
  border: 0; border-radius: 999px; background: transparent; color: #fff; font: 600 13.5px/1 'Inter', sans-serif;
  text-decoration: none; cursor: pointer; white-space: nowrap; -webkit-tap-highlight-color: transparent; }
.dd-appbar a:active, .dd-appbar button:active, .dd-appbar [aria-current="page"] { background: rgba(255,255,255,.16); }
.dd-appbar svg { width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
html.dd-standalone .print-btn, html.dd-standalone .float-controls {
  bottom: calc(76px + env(safe-area-inset-bottom, 0px)); }
html.dd-standalone .scroll-top-btn { bottom: calc(132px + env(safe-area-inset-bottom, 0px)); }   /* stacked above the dark-mode button */
@media (max-width: 380px) { .dd-appbar a, .dd-appbar button { padding: 0 11px; font-size: 12.5px; } }
html[data-theme="dark"] .dd-appbar { background: #0e4a50; }
@media print { .dd-appbar { display: none !important; } }

/* [hidden] must win over display rules on app controls */
.dd-app [hidden], .dd-app-cta[hidden], .dd-appbar [hidden] { display: none !important; }
/* Hero call-to-action: install the app */
.dd-app-cta { display: inline-flex; align-items: center; gap: 12px; margin: 2px 0 18px; padding: 11px 16px 11px 14px;
  border-radius: 14px; color: #fff; text-decoration: none; background: linear-gradient(135deg, #1a6b72 0%, #0e4a50 100%);
  box-shadow: 0 6px 18px rgba(14,74,80,.30), inset 0 1px 0 rgba(255,255,255,.14); transition: transform .15s, box-shadow .15s; }
.dd-app-cta:hover { transform: translateY(-1px); box-shadow: 0 10px 24px rgba(14,74,80,.36), inset 0 1px 0 rgba(255,255,255,.14); }
.dd-app-cta:focus-visible { outline: 3px solid #b8860b; outline-offset: 3px; }
.dd-app-cta > svg:first-child { flex: none; width: 34px; height: 34px; padding: 6px; border-radius: 10px; background: rgba(255,255,255,.16);
  fill: none; stroke: #fff; stroke-width: 1.9; stroke-linecap: round; stroke-linejoin: round; }
.dd-app-cta-t { display: flex; flex-direction: column; gap: 2px; line-height: 1.2; }
.dd-app-cta-t strong { font: 700 15px/1.2 'Inter', sans-serif; letter-spacing: .005em; }
.dd-app-cta-t small { font: 500 12.5px/1.3 'Manrope', sans-serif; color: #e6fbfc; }
.dd-app-cta-arr { flex: none; width: 18px; height: 18px; fill: none; stroke: #fff; stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; opacity: .85; }
html[data-theme="dark"] .dd-app-cta { background: linear-gradient(135deg, #0e4a50 0%, #0a363b 100%); box-shadow: 0 6px 18px rgba(0,0,0,.35); }
@media print { .dd-app-cta { display: none !important; } }
/* Clinical tools: Interaction checker + Med Scheduler cards in the index hero */
.dd-tools { display: grid; grid-template-columns: repeat(2, minmax(0, 340px)); gap: 14px; margin: 4px 0 20px; }
.dd-tool { position: relative; display: flex; align-items: center; gap: 14px; padding: 16px 16px 16px 14px; border-radius: 16px;
  color: #fff; text-decoration: none; overflow: hidden; isolation: isolate;
  box-shadow: 0 10px 26px -8px var(--tool-sh), inset 0 1px 0 rgba(255,255,255,.18); transition: transform .16s, box-shadow .16s; }
.dd-tool::after { content: ""; position: absolute; z-index: -1; right: -38px; top: -46px; width: 140px; height: 140px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,.20), rgba(255,255,255,0) 70%); }
.dd-tool-ix { background: linear-gradient(135deg, #b0275f 0%, #7a1240 100%); --tool-sh: rgba(122,18,64,.55); }
.dd-tool-ms { background: linear-gradient(135deg, #3b4fb8 0%, #22307a 100%); --tool-sh: rgba(34,48,122,.55); }
.dd-tool:hover { transform: translateY(-2px); box-shadow: 0 16px 32px -8px var(--tool-sh), inset 0 1px 0 rgba(255,255,255,.18); }
.dd-tool:focus-visible { outline: 3px solid #b8860b; outline-offset: 3px; }
.dd-tool-ico { flex: none; display: grid; place-items: center; width: 50px; height: 50px; border-radius: 14px;
  background: rgba(255,255,255,.16); box-shadow: inset 0 0 0 1px rgba(255,255,255,.22); }
.dd-tool-ico svg { width: 32px; height: 32px; fill: none; stroke: #fff; stroke-width: 1.9; stroke-linecap: round; stroke-linejoin: round; }
.dd-tool-ico .dd-tool-dot { fill: #ffd57a; stroke: none; }
.dd-tool-t { display: flex; flex-direction: column; gap: 3px; min-width: 0; line-height: 1.2; }
.dd-tool-t strong { font: 800 17px/1.2 'Inter', sans-serif; letter-spacing: -.005em; }
.dd-tool-t small { font: 500 13px/1.35 'Manrope', sans-serif; color: #fff; opacity: .92; }
.dd-tool-arr { flex: none; margin-left: auto; width: 20px; height: 20px; fill: none; stroke: #fff; stroke-width: 2.4;
  stroke-linecap: round; stroke-linejoin: round; transition: transform .16s; }
.dd-tool:hover .dd-tool-arr { transform: translateX(3px); }
html[data-theme="dark"] .dd-tool-ix { background: linear-gradient(135deg, #8f1d4c 0%, #5c0d30 100%); }
html[data-theme="dark"] .dd-tool-ms { background: linear-gradient(135deg, #2f3f94 0%, #1a245c 100%); }
@media (max-width: 640px) { .dd-tools { grid-template-columns: 1fr; gap: 10px; } .dd-tool { padding: 14px 14px 14px 12px; } }
@media (prefers-reduced-motion: reduce) { .dd-tool, .dd-tool-arr { transition: none; } .dd-tool:hover { transform: none; } }
@media print { .dd-tools { display: none !important; } }

/* Installable app + offline panel (index) */
.dd-app { margin: 34px 0 22px; padding: 22px; border: 1px solid var(--border); border-radius: 14px; background: var(--white); }
.dd-app h2 { font-family: 'Inter', sans-serif; font-size: 20px; margin: 0 0 14px; color: var(--navy); }
.dd-app-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.dd-app-card { border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px; background: var(--bg); }
.dd-app-card h3 { font-family: 'Inter', sans-serif; font-size: 15.5px; margin: 0 0 8px; color: var(--text); }
.dd-app-card p { font-size: 14px; line-height: 1.6; color: var(--text-mid); margin: 0 0 10px; }
.dd-app-card progress { width: 100%; height: 8px; margin: 2px 0 10px; accent-color: #1a6b72; }
.dd-btn[disabled] { opacity: .6; cursor: progress; }
.dd-app-opt { display: flex; flex-wrap: wrap; align-items: center; gap: 2px 10px; margin: 0 0 8px; }
.dd-app-opt .dd-btn { margin: 2px 0; }
.dd-app-meta { font-size: 13px; color: var(--text-muted); }
.dd-app-setup { margin: 0 0 14px; }
.dd-app-setup a { color: inherit; font-weight: 700; }
.dd-app-ios { margin: 4px 0 6px 20px; padding: 0; font-size: 14px; line-height: 1.6; color: var(--text-mid); }
.dd-app-ios li { margin: 0 0 4px; }
.dd-app-warn { font-size: 13.5px; line-height: 1.55; color: #6b4200; background: #fff7e6; border: 1px solid #f0c674;
  border-radius: 10px; padding: 10px 12px; margin: 6px 0 10px; }
html[data-theme="dark"] .dd-app-ios { color: #c9d2e0; }
html[data-theme="dark"] .dd-app-warn { color: #fde68a; background: #2a1d05; border-color: #6b4f12; }
html[data-theme="dark"] .dd-app-meta { color: #b4bfcf; }
.dd-off-h { font-family: 'Inter', sans-serif; font-size: 18px; margin: 26px 0 6px; }
html.dd-offline body::after { content: "Offline · showing saved pages"; position: fixed; left: 50%; top: 10px; transform: translateX(-50%);
  z-index: 9999; font: 600 12.5px/1 'Inter', sans-serif; color: #fff; background: #7a4b00; padding: 8px 14px; border-radius: 20px;
  box-shadow: 0 4px 14px rgba(0,0,0,.18); pointer-events: none; }
html[data-theme="dark"] .dd-app { background: #1a2535; border-color: #2c3a52; }
html[data-theme="dark"] .dd-app h2 { color: #eef2fb; }
html[data-theme="dark"] .dd-app-card { background: #141e2c; border-color: #2c3a52; }
html[data-theme="dark"] .dd-app-card h3 { color: #eef2fb; }
html[data-theme="dark"] .dd-app-card p { color: #c9d2e0; }
@media print { .dd-app { display: none !important; } html.dd-offline body::after { display: none; } }
"""


def build_css() -> str:
    sys.path.insert(0, str(REPO))
    try:
        from patch_master_css import MASTER_CSS  # single source of truth for the guide look
    except Exception as e:  # pragma: no cover
        sys.exit(f"Cannot import MASTER_CSS from patch_master_css.py: {e}")
    return ("/* Generated by generate_drug_pages.py — MASTER_CSS from patch_master_css.py + drug-page rules. "
            "Do not edit; re-run the generator. */\n" + add_body_dark_aliases(MASTER_CSS + DRUG_CSS))


# ═════════════════════════════════════════════════════════════════════════════
# JS — shared by every drug page and the index (no external libraries)
# ═════════════════════════════════════════════════════════════════════════════
DRUG_JS = r"""/* Generated by generate_drug_pages.py — do not edit. */
/* Drug Index hero: next weekly update (Mondays from 01:47 Asia/Manila = Sunday 17:47 UTC; the CI schedule) */
(function(){var el=document.getElementById('dd-next-upd');if(!el)return;try{
  var now=new Date(),d=new Date(Date.UTC(now.getUTCFullYear(),now.getUTCMonth(),now.getUTCDate(),17,47,0));
  d.setUTCDate(d.getUTCDate()+((7-d.getUTCDay())%7));if(d<=now)d.setUTCDate(d.getUTCDate()+7);
  el.setAttribute('datetime',d.toISOString());
  el.textContent=d.toLocaleDateString('en-US',{timeZone:'Asia/Manila',weekday:'long',month:'long',day:'numeric'});
  el.parentNode.hidden=false;}catch(e){}})();
(function(){
'use strict';
var DARK_KEY='wgmr-dark';
var MOON='<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';
var SUN='<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>';
function applyDark(on){
  document.documentElement.setAttribute('data-theme',on?'dark':'light');
  document.body.classList.toggle('dark-mode',on);
  var b=document.getElementById('darkToggle'),l=document.getElementById('darkLabel'),i=document.getElementById('darkIcon');
  if(b)b.classList.toggle('active',on); if(l)l.textContent=on?'Light mode':'Dark mode'; if(i)i.innerHTML=on?SUN:MOON;
}
window.toggleDark=function(){var on=document.documentElement.getAttribute('data-theme')!=='dark';try{localStorage.setItem(DARK_KEY,on?'1':'0');}catch(e){}applyDark(on);};
try{applyDark(localStorage.getItem(DARK_KEY)==='1'||document.documentElement.getAttribute('data-theme')==='dark');}catch(e){}

var top=document.getElementById('scrollTopBtn');
if(top)window.addEventListener('scroll',function(){top.classList.toggle('visible',window.scrollY>300);},{passive:true});

function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();}

/* ── Open a label accordion when linked to (e.g. "Full indications") ── */
function openFromHash(h){var el=h&&document.getElementById(h.replace(/^#/,''));if(!el)return;
  for(var p=el;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}}
document.addEventListener('click',function(e){var a=e.target.closest('a[href^="#"]');if(a&&a.getAttribute('href').length>1)openFromHash(a.getAttribute('href'));});
openFromHash(location.hash);

/* ── Product table: text filter, class filter, hide-past-validity, column sort ── */
var tbl=document.getElementById('dd-products');
if(tbl){
  var body=tbl.tBodies[0], rows=Array.prototype.slice.call(body.rows);
  var q=document.getElementById('dd-q'), cls=document.getElementById('dd-class'),
      past=document.getElementById('dd-past'), cnt=document.getElementById('dd-count'),
      empty=document.getElementById('dd-empty');
  rows.forEach(function(r){r._t=norm(r.textContent);});
  function filter(){
    var terms=norm(q&&q.value).split(' ').filter(Boolean), c=cls?cls.value:'', hp=past&&past.checked, n=0;
    rows.forEach(function(r){
      var ok=(!c||r.getAttribute('data-class')===c)&&(!hp||r.getAttribute('data-past')!=='1');
      for(var i=0;ok&&i<terms.length;i++)if(r._t.indexOf(terms[i])<0)ok=false;
      r.hidden=!ok; if(ok)n++;
    });
    if(cnt)cnt.textContent='Showing '+n.toLocaleString('en-US')+' of '+rows.length.toLocaleString('en-US')+' products';
    if(empty)empty.hidden=n!==0;
  }
  [q,cls,past].forEach(function(el){if(el)el.addEventListener(el===q?'input':'change',filter);});
  var ths=tbl.tHead.rows[0].cells, sortSel=document.getElementById('dd-sort');
  function sortBy(idx,dir){
    Array.prototype.forEach.call(ths,function(o){o.removeAttribute('aria-sort');});
    ths[idx].setAttribute('aria-sort',dir===1?'ascending':'descending');
    var key=function(r){var td=r.cells[idx];return td.getAttribute('data-sort')||td.textContent.trim().toLowerCase();};
    rows.sort(function(a,b){var x=key(a),y=key(b);return x<y?-dir:x>y?dir:0;});
    var f=document.createDocumentFragment(); rows.forEach(function(r){f.appendChild(r);}); body.appendChild(f);
    if(sortSel)sortSel.value=idx+':'+dir;
  }
  Array.prototype.forEach.call(ths,function(th,idx){
    var btn=th.querySelector('button'); if(!btn)return;
    btn.addEventListener('click',function(){sortBy(idx,th.getAttribute('aria-sort')==='ascending'?-1:1);});
  });
  if(sortSel)sortSel.addEventListener('change',function(){var v=sortSel.value.split(':');sortBy(+v[0],+v[1]);});
  filter();
  /* ?brand=<name> (from the Drug Index brand view): filter the products table to that brand */
  try{var qb=new URLSearchParams(location.search).get('brand');
    if(qb&&q){q.value=qb;var acc0=document.getElementById('dd-prod-acc');if(acc0)acc0.open=true;filter();
      var sec0=document.getElementById('products');if(sec0)setTimeout(function(){sec0.scrollIntoView({block:'start'});},0);}}catch(e){}
  document.addEventListener('click',function(e){
    var a=e.target.closest('a.dd-brand-link'); if(!a||!q)return;
    e.preventDefault();
    if(cls)cls.value=''; if(past)past.checked=false;
    var acc=document.getElementById('dd-prod-acc'); if(acc)acc.open=true;
    q.value=a.getAttribute('data-brand'); filter();
    var sec=document.getElementById('products'); if(sec)sec.scrollIntoView({behavior:'smooth',block:'start'});
    try{history.replaceState(null,'','#products');}catch(err){}
  });
}

/* ── Products table collapsed by default when >2 products: open on #products links and for print ── */
(function(){
  var acc=document.getElementById('dd-prod-acc'); if(!acc)return;
  function chk(){ if(location.hash==='#products'||location.hash==='#dd-products')acc.open=true; }
  chk(); window.addEventListener('hashchange',chk);
  window.addEventListener('beforeprint',function(){acc.open=true;});
})();

/* ── Monograph: highlight the current section in the sticky table of contents ── */
var toc=document.querySelector('.dd-toc');
if(toc&&'IntersectionObserver' in window){
  var links={};Array.prototype.forEach.call(toc.querySelectorAll('a'),function(a){links[a.getAttribute('href').slice(1)]=a;});
  var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){
    Object.keys(links).forEach(function(k){links[k].removeAttribute('aria-current');});
    var a=links[en.target.id]; if(a)a.setAttribute('aria-current','true');}});},{rootMargin:'-20% 0px -70% 0px'});
  Object.keys(links).forEach(function(k){var el=document.getElementById(k);if(el)io.observe(el);});
}

/* ── Category list filter ── */
var cq=document.getElementById('dd-cq');
if(cq){var cl=document.querySelectorAll('#dd-catlist li');cq.addEventListener('input',function(){var t=norm(cq.value);
  Array.prototype.forEach.call(cl,function(li){li.hidden=!!t&&norm(li.getAttribute('data-n')).indexOf(t)<0;});});}

/* ── Drug Index: faceted instant search (ARIA combobox) over search-index.json (+ lazy search-extra.json) ── */
var idx=document.getElementById('dd-index');
if(idx){
  var az=document.getElementById('dd-az'), alpha=document.getElementById('dd-alpha'), letters=Array.prototype.slice.call(document.querySelectorAll('.dd-letter'));
  var sq=document.getElementById('dd-sq'), res=document.getElementById('dd-results'), info=document.getElementById('dd-sinfo');
  var F={c:document.getElementById('dd-f-class'),r:document.getElementById('dd-f-rx'),f:document.getElementById('dd-f-form'),
         k:document.getElementById('dd-f-k'),n:document.getElementById('dd-f-n'),p:document.getElementById('dd-f-p'),h:document.getElementById('dd-f-h'),l:document.getElementById('dd-f-l'),e:document.getElementById('dd-f-e'),
         t:document.getElementById('dd-f-type')};
  if(!F.t)delete F.t;
  var data=null, extra=null, supp=null, loading=null, active=-1, letter='all';
  function escH(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function hl(text,t){var i=text.toLowerCase().indexOf(t);if(!t||i<0)return escH(text);return escH(text.slice(0,i))+'<mark class="dd-hl">'+escH(text.slice(i,i+t.length))+'</mark>'+escH(text.slice(i+t.length));}
  function load(){
    if(!loading)loading=fetch(idx.getAttribute('data-src')).then(function(r){return r.json();}).then(function(j){
      data=j.map(function(d){d.nn=norm(d.n);return d;});
      fetch(idx.getAttribute('data-extra')).then(function(r){return r.json();}).then(function(x){extra={};x.forEach(function(e){extra[e.s]=e;});if(sq.value)run();}).catch(function(){});
      /* food supplements: separate lazy file, merged into results with a "Supplement" badge */
      if(idx.getAttribute('data-supp'))fetch(idx.getAttribute('data-supp')).then(function(r){return r.json();}).then(function(x){
        supp=x.map(function(d){return {s:d.s,n:d.n,i:d.i,co:d.co,r:d.r,a:d.a,cat:d.cat,k:d.k,p:d.p,t:d.t,mk:d.mk,rf:d.rf,v:d.v,u:d.u,sp:d.sp,of:d.of,sup:1,nn:norm(d.n)};});if(sq.value||(F.t&&(F.t.value==='s'||F.t.value==='m')))run();}).catch(function(){});
    }).catch(function(){info.textContent='Search is unavailable right now. Use the A–Z list below.';});
    return loading;
  }
  function score(s,t){if(!s)return 0;if(s===t)return 100;if(s.indexOf(t)===0)return 80;if((' '+s).indexOf(' '+t)>=0)return 60;if(s.indexOf(t)>=0)return 35;return 0;}
  var FIELDS=[['n','generic',1],['y','also known as',.99],['i','ingredient',.95],['yi','ingredient',.9],['z','',.94],['b','brand',.97],['u','US brand',.9],['cl','class',.7],['x','indication',.6]];
  function smatch(d,t){
    var best=score(d.nn,t)*.97,lab=best?'supplement':'',val=d.n;
    [['a','registered as',.95],['i','ingredient',.85],['r','FR no.',.9],['co','company',.5]].forEach(function(f){(d[f[0]]||[]).forEach(function(x){var s=score(norm(x),t)*f[2];if(s>best){best=s;lab=f[1];val=x;}});});
    return best?{s:best,lab:lab,val:val}:null;
  }
  function match(d,t,raw){
    if(d.sup)return smatch(d,t);
    var best=0,lab='',val='';
    FIELDS.forEach(function(f){var v=d[f[0]];if(!v)return;var arr=Array.isArray(v)?v:[v];
      arr.forEach(function(x){var s=score(norm(x),t)*f[2];if(s>best){best=s;lab=f[1];val=x;}});});
    if(extra&&extra[d.s]&&best<60){var e=extra[d.s];
      (e.r||[]).forEach(function(x){var s=score(norm(x),t)*.9;if(s>best){best=s;lab='reg. no.';val=x;}});
      var mi=[];(e.m||[]).forEach(function(x,j){var s=score(norm(x),t)*.5;if(s>0)mi.push(j);if(s>best){best=s;lab='company';val=x;}});
      if(lab==='company')return {s:best,lab:lab,val:val,mi:mi};}
    return best?{s:best,lab:lab,val:val}:null;
  }
  function drugFacets(){return !!(F.c.value||F.r.value||F.f.value||F.k.checked||(F.n&&F.n.checked)||F.p.checked||F.h.checked||F.l.checked||(F.e&&F.e.checked));}
  function facetPass(d){
    if(F.t&&(F.t.value==='s'||F.t.value==='m'))return false;
    if(F.c.value&&d.c!==F.c.value)return false;
    if(F.r.value&&!((d.r||0)&(+F.r.value)))return false;
    if(F.f.value&&(d.f||[]).indexOf(F.f.value)<0)return false;
    return !(F.k.checked&&!d.k)&&!(F.n&&F.n.checked&&!d.nx)&&!(F.p.checked&&!d.p)&&!(F.h.checked&&!d.h)&&!(F.l.checked&&!d.l)&&!(F.e&&F.e.checked&&!d.e);
  }
  function pass(d){
    var ty=F.t?F.t.value:'';
    if(d.sup){if(ty==='d'||drugFacets())return false;
      if(ty==='s'&&d.t==='m')return false; if(ty==='m'&&!d.t)return false;
      if(letter!=='all'){var c0=(d.n||'?')[0].toLowerCase();if((c0>='a'&&c0<='z'?c0:'0')!==letter)return false;}return true;}
    if(ty==='s'||ty==='m')return false;
    if(F.c.value&&d.c!==F.c.value)return false;
    if(F.r.value&&!((d.r||0)&(+F.r.value)))return false;
    if(F.f.value&&(d.f||[]).indexOf(F.f.value)<0)return false;
    if(F.k.checked&&!d.k)return false; if(F.n&&F.n.checked&&!d.nx)return false; if(F.p.checked&&!d.p)return false; if(F.h.checked&&!d.h)return false; if(F.l.checked&&!d.l)return false; if(F.e&&F.e.checked&&!d.e)return false;
    if(letter!=='all'){var c=(d.n||'?')[0].toLowerCase();if((c>='a'&&c<='z'?c:'0')!==letter)return false;}
    return true;
  }
  function filtersOn(){return drugFacets()||!!(F.t&&F.t.value);}
  function chips(d){var o=[];if(d.sup){var MK=d.mk==='fsdu'?'Special dietary food (FSDU)':d.mk==='both'?'Medical nutrition (FSMP, FSDU)':'Medical nutrition (FSMP)';
    /* sp = stated food supplement, of = other food registration (older index entries carry neither: a supplement) */
    if(d.t==='m')o.push('<span class="dd-tag FSMP">'+MK+'</span>');
    if(d.t!=='m'&&(d.sp||!d.of))o.push('<span class="dd-tag SUP">Supplement</span>');
    if(d.of)o.push('<span class="dd-tag SUP">Food product</span>');
    if(d.t==='b')o.push('<span class="dd-tag FSMP">'+(d.mk==='fsdu'?'FSDU':d.mk==='both'?'FSMP · FSDU':'FSMP')+'</span>');if(d.rf)o.push('<span class="dd-tag SUPK">Renal formula</span>');
    (d.v||[]).forEach(function(v){o.push('<span class="dd-tag FSMP">'+escH(v)+'</span>');});if(d.k)o.push('<span class="dd-tag SUPK">Kidney-marketed</span>');return o.join(' ');}
    var r=d.r||0;
    if(r&8)o.push('<span class="dd-tag S2">S2</span>');if(r&16)o.push('<span class="dd-tag CP">Precursor</span>');
    if(r&1)o.push('<span class="dd-tag Rx">Rx</span>');if(r&2)o.push('<span class="dd-tag OTC">OTC</span>');if(r&4)o.push('<span class="dd-tag HR">HR</span>');
    if(d.p)o.push('<span class="dd-tag PNF">PNF</span>');if(d.h)o.push('<span class="dd-tag PNF">GAMOT</span>');
    if(d.k)o.push('<span class="dd-tag KD">Kidney dosing</span>');if(d.nx)o.push('<span class="dd-tag NX">Kidney injury risk</span>');if(d.l)o.push('<span class="dd-tag US">US label</span>');if(d.e)o.push('<span class="dd-tag US">EU SmPC</span>');return o.join(' ');}
  /* company search: that company's brands under the generic (search-extra "mb": refs into d.b; ref<0 = unbranded reg. no.) */
  function coBrands(d,o,slug){var e=extra&&extra[d.s];if(!o.mi||!e||!e.mb)return '';var seen={},refs=[];
    o.mi.forEach(function(j){(e.mb[j]||[]).forEach(function(r){if(!seen[r]){seen[r]=1;refs.push(r);}});});
    if(!refs.length)return '';refs.sort(function(a,b){return (a<0)-(b<0)||(a<0?b-a:a-b);});
    var MAX=12,base=encodeURIComponent(slug)+'.html?brand=',lk=refs.slice(0,MAX).map(function(r){
      if(r>=0){var b=(d.b||[])[r];return b?'<a href="'+base+encodeURIComponent(b)+'#products">'+escH(b)+'</a>':'';}
      var rn=(e.r||[])[-r-1];return rn?'<a href="'+base+encodeURIComponent(rn)+'#products">(unbranded, '+escH(rn)+')</a>':'';}).filter(Boolean);
    if(!lk.length)return '';
    return '<span class="dd-mbr"><span class="dd-mbr-l">Brands:</span> '+lk.join('<span class="dd-mbr-s" aria-hidden="true"> · </span>')+
      (refs.length>MAX?' <a class="dd-mbr-more" href="'+encodeURIComponent(slug)+'.html#products">+'+(refs.length-MAX)+' more</a>':'')+'</span>';}
  function setActive(i){var opts=res.querySelectorAll('[role=option]');if(!opts.length){active=-1;sq.removeAttribute('aria-activedescendant');return;}
    active=Math.max(0,Math.min(i,opts.length-1));Array.prototype.forEach.call(opts,function(o,j){o.setAttribute('aria-selected',j===active?'true':'false');});
    sq.setAttribute('aria-activedescendant',opts[active].id);opts[active].scrollIntoView({block:'nearest'});}
  function run(){
    if(view!=='generic'){runView();return;}
    var raw=sq.value.trim(), t=norm(raw);
    if(!t&&!filtersOn()){res.hidden=true;res.innerHTML='';info.textContent='';sq.setAttribute('aria-expanded','false');az.hidden=false;
      letters.forEach(function(s){s.hidden=!(letter==='all'||s.getAttribute('data-l')===letter);});return;}
    load().then(function(){
      if(!data)return;
      var out=[];
      (supp?data.concat(supp):data).forEach(function(d){if(!pass(d))return;if(!t){out.push({d:d,s:0});return;}var m=match(d,t,raw);if(m)out.push({d:d,s:d.sup?m.s*.95:m.s,lab:m.lab,val:m.val,mi:m.mi});});
      out.sort(function(a,b){return b.s-a.s||a.d.n.localeCompare(b.d.n);});
      var shown=out.slice(0,200), tl=raw.toLowerCase();
      res.innerHTML=shown.map(function(o,i){var d=o.d;
        var why=(o.lab&&o.lab!=='generic')?'<span class="dd-why">'+escH(o.lab)+': '+hl(o.val,tl)+'</span>':'';
        if(d.sup){why=(o.lab&&o.lab!=='supplement')?'<span class="dd-why">'+escH(o.lab)+': '+hl(o.val,tl)+'</span>':'';
          return '<li role="option" id="dd-opt-'+i+'" aria-selected="false"><a href="supplements/'+(d.p?encodeURIComponent(d.s)+'.html':'view.html?b='+encodeURIComponent(d.s))+'">'+(o.lab==='supplement'?hl(d.n,tl):escH(d.n))+'</a>'+why+
          '<span class="dd-sub">'+escH((d.i||[]).length?(d.i||[]).slice(0,4).join(' · '):(d.u||''))+'</span><span class="dd-tags">'+chips(d)+'</span></li>';}
        if(d.m&&d.mh)return '<li role="option" id="dd-opt-'+i+'" aria-selected="false"><a href="'+encodeURIComponent(d.m)+'.html">'+(o.lab==='generic'?hl(d.n,tl):escH(d.n))+' <span class="dd-arrow">&rarr; '+escH(d.mn)+'</span></a>'+why+
          coBrands(d,o,d.m)+'<span class="dd-sub">Registered under a variant spelling of '+escH(d.mn)+'; opens the main monograph</span></li>';
        return '<li role="option" id="dd-opt-'+i+'" aria-selected="false"><a href="'+encodeURIComponent(d.s)+'.html">'+(o.lab==='generic'?hl(d.n,tl):escH(d.n))+'</a>'+why+coBrands(d,o,d.s)+
          '<span class="dd-sub">'+escH(d.c||'')+(d.m?' · Did you mean <a href="'+encodeURIComponent(d.m)+'.html">'+escH(d.mn)+'</a>?':'')+'</span><span class="dd-tags">'+chips(d)+'</span></li>';}).join('');
      res.hidden=false; az.hidden=true; sq.setAttribute('aria-expanded',out.length?'true':'false'); active=-1;
      info.innerHTML=out.length?(out.length>200?'Showing the first 200 of '+out.length.toLocaleString('en-US')+' matches':out.length.toLocaleString('en-US')+(out.length===1?' match':' matches')):'No generic, brand, class, product or supplement matches. A product missing here may not be registered with the Food and Drug Administration (FDA) Philippines. '+'Check it on <a href="https://verification.fda.gov.ph" rel="noopener" target="_blank">verification.fda.gov.ph</a> using the name or the registration number on the label.';
    });
  }
  /* ── Browse by: generic (A–Z, server-rendered) / brand / class / area / dispensing / kidney (lazy browse*.json) ── */
  var tabs=Array.prototype.slice.call(document.querySelectorAll('#dd-browse [role=tab]')), vbox=document.getElementById('dd-view');
  var VIEWS=tabs.map(function(b){return b.getAttribute('data-v');}), view='generic', bcore=null, bbr=null, bySlug={}, built={};
  function getJSON(u){return fetch(u).then(function(r){if(!r.ok)throw new Error(r.status);return r.json();});}
  function needData(v){
    var p=[load()];
    if(v==='brand'){if(!bbr)p.push(getJSON(vbox.getAttribute('data-brands')).then(function(j){bbr=j;}));}
    else if(!bcore)p.push(getJSON(vbox.getAttribute('data-src')).then(function(j){bcore=j;}));
    return Promise.all(p).then(function(){if(data&&!bySlug.__ok){data.forEach(function(d){bySlug[d.s]=d;});bySlug.__ok=1;}});
  }
  var KB='<span class="dd-kbadge" title="Has approved kidney dosing guidance">'+(document.querySelector('#dd-az .dd-kbadge')||{innerHTML:''}).innerHTML+'</span>';
  function gli(slug){var d=bySlug[slug];if(!d)return '';
    return '<li data-s="'+escH(slug)+'"><a href="'+encodeURIComponent(slug)+'.html">'+escH(d.n)+'</a>'+(d.k?KB:'')+(d.c?'<span class="dd-sub">'+escH(d.c)+'</span>':'')+'</li>';}
  function grp(title,ids,G,extra,open){
    var lis=ids.map(function(i){return gli(G[i]);}).join('');
    return '<details class="dd-vg"'+(open?' open':'')+' data-open="'+(open?1:0)+'"><summary><span class="dd-vg-t">'+escH(title)+'</span> <span class="dd-vg-n" data-n="'+ids.length+'">'+ids.length.toLocaleString('en-US')+'</span></summary>'+(extra||'')+'<ul class="dd-list">'+lis+'</ul></details>';
  }
  function build(v){
    var h='';
    if(v==='brand'){
      var G=bbr.g, by={};
      bbr.b.forEach(function(r){var c=(r[0]||'?')[0].toLowerCase();c=(c>='a'&&c<='z')?c:'0';(by[c]=by[c]||[]).push(r);});
      Object.keys(by).sort().forEach(function(L){
        h+='<section class="dd-vg dd-vletter" data-l="'+L+'"><h2>'+(L==='0'?'#':L.toUpperCase())+'</h2><ul class="dd-list dd-blist">'+by[L].map(function(r){
          var s=G[r[1]], d=bySlug[s]||{n:s};
          return '<li data-s="'+escH(s)+'" data-t="'+escH(norm(r[0]+' '+d.n))+'"><a href="'+encodeURIComponent(s)+'.html?brand='+encodeURIComponent(r[0])+'#products">'+escH(r[0])+
            ' <span class="dd-arrow">&rarr; '+escH(d.n)+'</span></a><span class="dd-sub">'+escH(r[2]||'')+(r[3]?' · registered as '+escH(r[3]):'')+'</span></li>';}).join('')+'</ul></section>';});
      h='<p class="dd-note dd-vnote">'+bbr.b.length.toLocaleString('en-US')+' Philippine brands. Each brand opens its generic page with the products table filtered to that brand.</p>'+h;
    }else{
      var G=bcore.g;
      if(v==='class')h='<p class="dd-note dd-vnote">'+bcore['class'].length.toLocaleString('en-US')+' drug classes (US FDA established pharmacologic class where a US label exists, else the FDA Philippines category).</p>'+
        bcore['class'].map(function(c){return grp(c[0],c[2],G,'<p class="dd-vg-link"><a href="category/'+encodeURIComponent(c[1])+'.html">Open the '+escH(c[0])+' class page &rarr;</a></p>',false);}).join('');
      if(v==='area')h='<p class="dd-note dd-vnote">Coarse body-system groups from keyword rules over each drug\'s class (not WHO ATC). Each generic is listed once.</p>'+
        bcore.area.map(function(a){return grp(a[0],a[1],G,'',false);}).join('');
      if(v==='disp')h='<p class="dd-note dd-vnote">From the FDA Philippines classification and the Dangerous Drugs Board lists. A generic with products in more than one category appears in each.</p>'+
        bcore.disp.map(function(a){return grp(a[0],a[2],G,'',false);}).join('');
      if(v==='kidney')h='<p class="dd-note dd-vnote">Generics with kidney guidance reviewed by renalcarematters.com, grouped by the most restrictive level across eGFR bands and dialysis.</p>'+
        bcore.kidney.map(function(a){return grp(a[0],a[2],G,'',true);}).join('')+'<p class="dd-note">'+escH(bcore.kidneyNote)+'</p>';
      if(v==='nephrotox'&&bcore.nx)h='<p class="dd-note dd-vnote">'+(bcore.nxN||0).toLocaleString('en-US')+' generics whose US label (or drug-class label) warns of kidney injury, grouped by mechanism. A generic can appear under more than one mechanism. Reviewed by renalcarematters.com.</p>'+
        bcore.nx.map(function(a){return grp(a[0],a[2],G,'',false);}).join('')+'<p class="dd-note">Not tagged: drugs whose kidney warnings are about use in kidney disease (for example metformin, gadolinium) or about volume depletion, rhabdomyolysis or tumor lysis, and ACE inhibitors, ARBs and SGLT2 inhibitors, which protect the kidney. A drug without this tag is not necessarily safe for the kidneys.</p>';
      if(v==='pn'&&bcore.pn){var PT=bcore.pn.t,PR=bcore.pn.r;
        h='<p class="dd-note dd-vnote">'+PR.length.toLocaleString('en-US')+' intravenous nutrition products registered with FDA Philippines, sorted by product type. Each opens its generic page with the products table filtered to that brand. Product types only; no dosing guidance.</p>'+
        PT.map(function(t){var rs=PR.filter(function(r){return r[2]===t[0];});if(!rs.length)return '';
          return '<details class="dd-vg" open data-open="1"><summary><span class="dd-vg-t">'+escH(t[1])+'</span> <span class="dd-vg-n" data-n="'+rs.length+'">'+rs.length.toLocaleString('en-US')+'</span></summary><ul class="dd-list dd-blist">'+rs.map(function(r){
            var s=G[r[1]],d=bySlug[s]||{n:s},tag=(r[4]==='renal'?'<span class="dd-tag SUPK">Renal formula</span>':r[4]==='hepatic'?'<span class="dd-tag HEP">Hepatic formula</span>':'')+(r[7]?'<a class="dd-tag KN" href="'+encodeURIComponent(s)+'.html#'+escH(r[7])+'" aria-label="Kidney notes for '+escH(r[0])+'">Kidney notes</a>':'');
            return '<li data-s="'+escH(s)+'" data-t="'+escH(norm(r[0]+' '+d.n+' '+(r[3]||'')+' '+t[1]+(r[4]?' '+r[4]+' formula':'')+(r[6]&&r[6]!==r[0]?' '+r[6]:'')))+'"><a href="'+encodeURIComponent(s)+'.html?brand='+encodeURIComponent(r[6]||r[0])+'#products">'+escH(r[0])+
              ' <span class="dd-arrow">&rarr; '+escH(d.n)+'</span></a>'+(tag?'<span class="dd-tags">'+tag+'</span>':'')+'<span class="dd-sub">'+escH([r[3],r[5]].filter(Boolean).join(' · '))+'</span></li>';}).join('')+'</ul></details>';}).join('');}
    }
    var div=document.createElement('div');div.className='dd-vbody';div.setAttribute('data-v',v);div.innerHTML=h;
    div.querySelectorAll('li').forEach(function(li){if(!li.hasAttribute('data-t')){var d=bySlug[li.getAttribute('data-s')];li._d=d;}});
    vbox.appendChild(div); built[v]=div; return div;
  }
  function runView(){
    var raw=sq.value.trim(), t=norm(raw), v=view;
    res.hidden=true; res.innerHTML=''; sq.setAttribute('aria-expanded','false'); az.hidden=true;
    needData(v).then(function(){
      if(view!==v)return;
      var div=built[v]||build(v), on=!!t||drugFacets()||(F.t&&(F.t.value==='s'||F.t.value==='m'));
      Object.keys(built).forEach(function(k){built[k].hidden=k!==v;});
      var shown=0,total=0;
      div.querySelectorAll('.dd-vg').forEach(function(g){
        var n=0,lis=g.querySelectorAll('li');
        if(g.classList.contains('dd-vletter')&&letter!=='all'&&g.getAttribute('data-l')!==letter){g.hidden=true;total+=lis.length;return;}
        lis.forEach(function(li){var d=bySlug[li.getAttribute('data-s')]||{},ok=facetPass(d);
          if(ok&&t)ok=li.hasAttribute('data-t')?li.getAttribute('data-t').indexOf(t)>=0:!!match(d,t);
          li.hidden=!ok;if(ok)n++;});
        total+=lis.length; shown+=n; g.hidden=!n;
        var c=g.querySelector('.dd-vg-n');if(c)c.textContent=(n===lis.length?'':n.toLocaleString('en-US')+' of ')+lis.length.toLocaleString('en-US');
        if(g.tagName==='DETAILS'){if(on&&n){if(!g.open){g.open=true;g._auto=1;}}else if(!on&&g._auto){g.open=false;g._auto=0;}}
      });
      info.textContent=on?(shown?shown.toLocaleString('en-US')+' of '+total.toLocaleString('en-US')+' entries match':'Nothing in this view matches the search or filters.'):'';
    }).catch(function(){info.textContent='This view could not be loaded. Use the generic A–Z list.';});
  }
  function setView(v,focus,save){
    if(VIEWS.indexOf(v)<0)v='generic';
    view=v;
    tabs.forEach(function(b){var on=b.getAttribute('data-v')===v;b.setAttribute('aria-selected',on?'true':'false');b.tabIndex=on?0:-1;if(on&&focus)b.focus();
      if(on){var bar=b.parentNode;if(b.offsetLeft<bar.scrollLeft||b.offsetLeft+b.offsetWidth>bar.scrollLeft+bar.clientWidth)bar.scrollLeft=b.offsetLeft-12;}});
    vbox.setAttribute('aria-labelledby','dd-tab-'+v);
    vbox.hidden=v==='generic'; alpha.hidden=!(v==='generic'||v==='brand');
    if(v==='generic'){Object.keys(built).forEach(function(k){built[k].hidden=true;});}
    if(save){try{localStorage.setItem('wgmr-drug-view',v);}catch(e){}
      try{var u=new URL(location.href);if(v==='generic')u.searchParams.delete('view');else u.searchParams.set('view',v);history.replaceState(null,'',u.pathname+u.search+u.hash);}catch(e){}}
    if(v==='generic'){info.textContent='';run();}else runView();
  }
  tabs.forEach(function(b,i){
    b.addEventListener('click',function(){setView(b.getAttribute('data-v'),false,true);});
    b.addEventListener('keydown',function(e){var j=-1;
      if(e.key==='ArrowRight'||e.key==='ArrowDown')j=(i+1)%tabs.length;else if(e.key==='ArrowLeft'||e.key==='ArrowUp')j=(i-1+tabs.length)%tabs.length;
      else if(e.key==='Home')j=0;else if(e.key==='End')j=tabs.length-1;
      if(j>=0){e.preventDefault();setView(tabs[j].getAttribute('data-v'),true,true);}});
  });
  var timer=null;
  sq.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,90);});
  sq.addEventListener('focus',load,{once:true});
  sq.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();setActive(active+1);}
    else if(e.key==='ArrowUp'){e.preventDefault();setActive(active-1);}
    else if(e.key==='Enter'&&active>=0){var o=res.querySelectorAll('[role=option] a')[active];if(o){e.preventDefault();location.href=o.href;}}
    else if(e.key==='Escape'){sq.value='';run();}
  });
  Object.keys(F).forEach(function(k){F[k].addEventListener('change',run);});
  document.getElementById('dd-f-clear').addEventListener('click',function(){Object.keys(F).forEach(function(k){if(F[k].type==='checkbox')F[k].checked=false;else F[k].value='';});sq.value='';letter='all';setLetter('all');run();});
  function setLetter(L){letter=L;Array.prototype.forEach.call(alpha.querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===L?'true':'false');});
    letters.forEach(function(s){s.hidden=!(L==='all'||s.getAttribute('data-l')===L);});}
  alpha.addEventListener('click',function(e){var b=e.target.closest('button');if(!b||b.disabled)return;setLetter(b.getAttribute('data-l'));run();
    try{history.replaceState(null,'',b.getAttribute('data-l')==='all'?location.pathname:'#letter-'+b.getAttribute('data-l'));}catch(err){}});
  var h=(location.hash.match(/^#letter-([a-z0])$/i)||[])[1]; if(h)setLetter(h.toLowerCase());
  var v0=null;try{v0=new URLSearchParams(location.search).get('view')||localStorage.getItem('wgmr-drug-view');}catch(e){}
  if(v0&&v0!=='generic'&&VIEWS.indexOf(v0)>=0)setView(v0,false,false);
  else if(sq.value)run();
}
})();

/* Installable app + offline downloads */
(function(){
'use strict';
var SAVED='rcm-drugs-saved',KEY='wgmr-drug-offline',deferred=null;
function net(){document.documentElement.classList.toggle('dd-offline',navigator.onLine===false);}
window.addEventListener('online',net);window.addEventListener('offline',net);net();
function standalone(){return (window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true;}
/* Installed app has no browser toolbar: add Back / Drug Index / Search */
if(standalone()&&!document.querySelector('.dd-appbar')){
  document.documentElement.classList.add('dd-standalone');
  var onIndex=location.pathname==='/drugs/'||location.pathname==='/drugs/index.html';
  var bar=document.createElement('nav');bar.className='dd-appbar no-print';bar.setAttribute('aria-label','App navigation');
  bar.innerHTML='<button type="button" data-ab="back" aria-label="Back"><svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg><span>Back</span></button>'
   +'<a href="/drugs/" data-ab="home"'+(onIndex?' aria-current="page"':'')+'><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg><span>Drug Index</span></a>'
   +'<a href="/drugs/#search" data-ab="search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg><span>Search</span></a>';
  document.body.appendChild(bar);
  bar.querySelector('[data-ab="back"]').addEventListener('click',function(){
    if(history.length>1)history.back();else location.href='/drugs/';});
  bar.querySelector('[data-ab="search"]').addEventListener('click',function(e){
    var sq=document.getElementById('dd-sq')||document.getElementById('ds-q');
    if(sq){e.preventDefault();sq.scrollIntoView({block:'center'});sq.focus();}});
}
if(location.hash==='#search'){var sq0=document.getElementById('dd-sq');if(sq0){sq0.scrollIntoView({block:'center'});try{sq0.focus();}catch(e){}}}
var box=document.getElementById('dd-app');
function ios(){return /iphone|ipad|ipod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);}
function q(n){return box?box.querySelector('[data-app="'+n+'"]'):null;}
function showInstall(){
  var hint=q('hint'),btn=q('install');if(!hint)return;
  if(standalone()){btn.hidden=true;hint.textContent='You are using the installed Dosis app.';
    ['iossteps','iosnote'].forEach(function(k){var e=q(k);if(e)e.hidden=true;});return;}
  if(deferred&&!ios()){btn.hidden=false;hint.textContent='Adds a Dosis icon to your home screen or desktop. It opens full screen and works offline.';return;}
  btn.hidden=true;
  if(ios()){hint.textContent='On iPhone or iPad, add Dosis to your Home Screen:';var o=q('iossteps');if(o)o.hidden=false;
    var n=q('iosnote');if(n)n.hidden=false;}
}
window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();deferred=e;showInstall();});
window.addEventListener('appinstalled',function(){deferred=null;showInstall();});
if(!box)return;
showInstall();
q('install').addEventListener('click',function(){if(!deferred)return;deferred.prompt();
  (deferred.userChoice||Promise.resolve()).then(function(){deferred=null;showInstall();});});

var dl=q('dl'),rm=q('rm'),st=q('status'),bar=q('bar');
if(!('caches' in window)||!('serviceWorker' in navigator)){q('off').hidden=true;return;}
var MAN='/drugs/offline-manifest.json',busy=false,cur=null,LABEL='Download the complete Drug Index';
function rec(){try{var r=JSON.parse(localStorage.getItem(KEY)||'null');return r&&r.v===3?r:null;}catch(e){return null;}}
function setRec(r){try{localStorage.setItem(KEY,JSON.stringify(r));}catch(e){}}
function fmtDate(ms){try{return new Date(ms).toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'});}catch(e){return '';}}
function num(n){return Number(n).toLocaleString('en-US');}
function manifest(){return fetch(MAN,{cache:'no-cache'}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json();});}
function status(){
  var r=rec();dl.disabled=busy;rm.disabled=busy;dl.textContent=LABEL;
  if(!r){st.textContent='Not downloaded on this device yet.';rm.hidden=true;return;}
  rm.hidden=false;
  var msg=r.done?'The complete Drug Index is saved on this device ('+num(r.n)+' pages, '+fmtDate(r.at)+').'
               :'Download interrupted at '+num(r.n)+' of '+num(r.total)+' pages. Tap the button again to resume.';
  if(!r.done)dl.textContent='Resume download';
  else if(cur&&cur.h!==r.h){msg+=' Updates are available.';dl.textContent='Update the Drug Index';}
  else if(cur)dl.textContent='Up to date · check again';
  st.textContent=msg;
  if(navigator.storage&&navigator.storage.estimate)navigator.storage.estimate().then(function(x){
    if(x&&x.usage&&!busy)st.textContent=msg+' Using about '+num(Math.max(1,Math.round(x.usage/1e6)))+' MB on this device.';}).catch(function(){});
}
status();
if(navigator.onLine!==false)manifest().then(function(m){cur=m;if(!busy)status();},function(){});

function run(){
  if(busy)return;
  if(navigator.onLine===false){st.textContent='You are offline. Connect to the internet to download.';return;}
  busy=true;status();bar.hidden=false;bar.value=0;st.textContent='Checking what needs downloading…';
  var lock=null;try{if(navigator.wakeLock)navigator.wakeLock.request('screen').then(function(l){lock=l;},function(){});}catch(e){}
  if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(function(){});
  var m,c,want={},have={},todo=[],ok=0,failed=0,total=0;
  manifest().then(function(x){
    m=x;cur=x;m.pages.forEach(function(p){want[location.origin+p[0]]=p;});
    return caches.open(SAVED);
  }).then(function(cache){c=cache;return c.keys();
  }).then(function(keys){
    return Promise.all(keys.map(function(k){
      if(!want[k.url])return c.delete(k);         // no longer published
      return c.match(k).then(function(res){have[k.url]=res&&res.headers.get('X-RCM-Hash');});
    }));
  }).then(function(){
    Object.keys(want).forEach(function(u){if(have[u]!==want[u][1])todo.push(u);});
    total=Object.keys(want).length;ok=total-todo.length;
    var need=todo.reduce(function(a,u){return a+want[u][2];},0);
    var room=(navigator.storage&&navigator.storage.estimate)?navigator.storage.estimate():Promise.resolve(null);
    return room.then(function(e){
      if(e&&e.quota&&e.quota-e.usage<need*1.15)throw {msg:'Not enough free storage on this device (about '+num(Math.ceil(need/1e6))+' MB more is needed). Free some space and tap the button again.'};
      bar.max=total;bar.value=ok;
      if(!todo.length)return;
      var i=0;
      function save(){setRec({v:3,n:ok,total:total,at:Date.now(),h:m.h,done:false});}
      function next(){
        if(i>=todo.length)return Promise.resolve();
        var u=todo[i++],p=want[u],json=/\.json$/.test(u);
        return fetch(u,{credentials:'same-origin',cache:'no-cache'}).then(function(res){
          if(!res.ok)throw new Error(res.status);
          return res.blob().then(function(bl){return c.put(u,new Response(bl,{headers:{
            'Content-Type':json?'application/json':'text/html; charset=utf-8','X-RCM-Hash':p[1]}}));});
        }).then(function(){ok++;if(ok%40===0)save();},function(){failed++;})
          .then(function(){bar.value=ok;st.textContent='Saving '+num(ok)+' of '+num(total)+' pages… keep this page open.';return next();});
      }
      save();
      return Promise.all([next(),next(),next(),next(),next(),next()]);
    });
  }).then(function(){
    setRec({v:3,n:ok,total:total,at:Date.now(),h:failed?'':m.h,done:!failed});
    busy=false;bar.hidden=true;status();
    if(failed)st.textContent=num(failed)+' pages could not be saved. Tap the button again on a better connection to finish.';
  }).catch(function(err){
    busy=false;bar.hidden=true;status();
    st.textContent=(err&&err.msg)||'The download stopped. Check your connection and tap the button again; pages already saved are kept.';
  }).then(function(){try{if(lock)lock.release();}catch(e){}});
}
dl.addEventListener('click',run);
var cta=document.getElementById('dd-app-cta');
if(cta&&standalone()){var rr=rec();if(rr&&rr.done)cta.hidden=true;else{cta.querySelector('strong').textContent='Set up offline use';
  cta.querySelector('small').textContent='Download the complete Drug Index once';}}
/* In the installed app, prompt until offline use is set up */
if(standalone()){var r0=rec();if(!r0||!r0.done){var main=document.getElementById('dd-index');
  if(main){var nb=document.createElement('div');nb.className='dd-app-warn dd-app-setup';
    nb.innerHTML='<strong>Offline use is not set up yet.</strong> Download the complete Drug Index once so every page opens without signal. <a href="#dd-app">Set up offline use</a>';
    main.insertBefore(nb,main.firstChild);}}}
rm.addEventListener('click',function(){if(busy)return;caches.delete(SAVED).then(function(){try{localStorage.removeItem(KEY);}catch(e){}status();});});
})();
"""

# Med Scheduler (Nov 2026)
DRUG_JS += r"""
(function(){
'use strict';
var root=document.getElementById('dd-ms');if(!root)return;
var $=function(id){return document.getElementById(id);};
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function nrm(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();}
function rd(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v;}catch(e){return d;}}
function wr(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
var IDX=null,IX=null,MS=null,BY={},MEDS=[],DICT=null,act=-1;
var FREQ=[['od','Once daily'],['bid','Twice daily'],['tid','Three times daily'],['qid','Four times daily'],['qam','Every morning'],['qpm','Every evening'],['hs','At bedtime'],
  ['q12','Every 12 hours'],['q8','Every 8 hours'],['q6','Every 6 hours'],['posthd','After each dialysis'],['tiw','3 times a week'],['weekly','Once a week'],['q2w','Every 2 weeks'],['monthly','Once a month'],['prn','As needed']];
var SLOTS=[['','Auto'],['W','On waking'],['PB','Before breakfast'],['B','Breakfast'],['MM','Mid-morning'],['L','Lunch'],['MA','Mid-afternoon'],['PD','Before dinner'],['D','Dinner'],['E','Evening'],['HS','Bedtime']];
var SLOTNAME={W:'on waking',PB:'before breakfast',B:'with breakfast',MM:'mid-morning',L:'with lunch',MA:'mid-afternoon',PD:'before dinner',D:'with dinner',E:'evening',HS:'at bedtime',POST:'after dialysis'};
var DAILY={od:1,bid:2,tid:3,qid:4,qam:1,qpm:1,hs:1,q12:2,q8:3,q6:4};
function load(){return Promise.all([root.getAttribute('data-src'),root.getAttribute('data-ix'),root.getAttribute('data-ms')].map(function(u){return fetch(u).then(function(r){return r.json();});}))
  .then(function(a){IDX=a[0];IX=a[1];MS=a[2];IDX.forEach(function(d){d.nn=nrm(d.n);BY[d.s]=d;});});}
function nm(s){return (BY[s]&&BY[s].n)||s.replace(/-/g,' ');}
/* ── routine ── */
function mins(v){var m=/^(\d\d):(\d\d)$/.exec(v||'');return m?(+m[1])*60+(+m[2]):null;}
function fmt(t){t=((t%1440)+1440)%1440;var h=Math.floor(t/60),m=t%60,ap=h<12?'AM':'PM';h=h%12||12;return h+':'+(m<10?'0':'')+m+' '+ap;}
var RK='wgmr-ms-routine';
function routine(){var dx=(root.querySelector('input[name=ms-dx]:checked')||{}).value||'none';
  return {wake:mins($('ms-wake').value),bf:mins($('ms-bf').value),lu:mins($('ms-lu').value),di:mins($('ms-di').value),bed:mins($('ms-bed').value),
    dx:dx,days:[].map.call(root.querySelectorAll('[data-hdday]:checked'),function(x){return +x.value;}),hs:mins($('ms-hs').value),he:mins($('ms-he').value),hold:$('ms-hold').checked,aht:($('ms-aht')||{}).value||'auto'};}
function saveRoutine(){var r={};['ms-wake','ms-bf','ms-lu','ms-di','ms-bed','ms-hs','ms-he'].forEach(function(i){r[i]=$(i).value;});
  r.dx=(root.querySelector('input[name=ms-dx]:checked')||{}).value;r.days=routine().days;r.hold=$('ms-hold').checked;r.aht=$('ms-aht').value;wr(RK,r);}
function restoreRoutine(){var r=rd(RK,null);if(!r)return;['ms-wake','ms-bf','ms-lu','ms-di','ms-bed','ms-hs','ms-he'].forEach(function(i){if(r[i])$(i).value=r[i];});
  if(r.dx){var x=root.querySelector('input[name=ms-dx][value="'+r.dx+'"]');if(x)x.checked=true;}
  (r.days||[]).forEach(function(d){var x=root.querySelector('[data-hdday][value="'+d+'"]');if(x)x.checked=true;});$('ms-hold').checked=!!r.hold;if(r.aht)$('ms-aht').value=r.aht;}
function paintHD(){$('ms-hdbox').hidden=((root.querySelector('input[name=ms-dx]:checked')||{}).value!=='hd');}
root.addEventListener('change',function(e){if(e.target.closest('.dd-ms-routine')){paintHD();saveRoutine();}});
root.querySelectorAll('[data-preset]').forEach(function(b){b.addEventListener('click',function(){var p=b.getAttribute('data-preset').split(',');
  root.querySelectorAll('[data-hdday]').forEach(function(x){x.checked=p.indexOf(x.value)>=0;});saveRoutine();});});
/* ── medicines list ── */
function rule(s){var g=IX.g[s]||{},ms=g.m||[s];for(var i=0;i<ms.length;i++)if(MS.r[ms[i]])return MS.r[ms[i]];return null;}
/* calcium salts: purpose decides timing (binder with meals; supplement between meals) */
function caCfg(){return (MS.pu||{}).calcium||null;}
function isCa(s){var C=caCfg();if(!C)return false;var rx=new RegExp(C.match),ms=(IX.g[s]||{}).m||[s];return ms.some(function(x){return rx.test(x);});}
function caUse(m){return m.use||(m.freq==='tid'||m.freq==='qid'?'binder':'supplement');}
function ruleM(m){var r=rule(m.s);if(!isCa(m.s))return r;var C=caCfg(),u=caUse(m),p=C[u],o={};for(var k in (r||{}))o[k]=r[k];
  o.meal=p.meal;delete o.tod;o.evid={note:p.note,by:C.by,cites:p.cites};o.use=p.label;return o;}
function addMed(s,o){if(!BY[s])return false;o=o||{};MEDS.push({s:s,dose:o.dose||'',freq:o.freq||'od',slot:o.slot||'',note:o.note||'',use:o.use||''});paintList();return true;}
function paintList(){var box=$('ms-list');
  if(!MEDS.length){box.innerHTML='<p class="dd-note">No medicines yet. Add them above or paste a prescription.</p>';return;}
  box.innerHTML='<table class="dd-ms-tab"><thead><tr><th>Medicine</th><th>Dose</th><th>How often</th><th>Timing</th><th><span class="dd-hidden">Remove</span></th></tr></thead><tbody>'+MEDS.map(function(m,i){
    var r=ruleM(m),hint=r?(r.meal==='with'?'with food':r.meal==='before'?'before meals':r.meal==='empty'?'empty stomach':r.meal==='between'?'between meals':r.meal==='after'?'after meals':r.tod?r.tod:r.hd==='unit'?'given at the dialysis unit':r.hd==='after'?'after dialysis':''):'';
    var use=isCa(m.s)?'<label class="dd-ms-use">Used as <select class="ms-in" data-i="'+i+'" data-k="use"><option value="binder"'+(caUse(m)==='binder'?' selected':'')+'>Phosphate binder (with meals)</option><option value="supplement"'+(caUse(m)==='supplement'?' selected':'')+'>Calcium supplement (between meals)</option></select></label>':'';
    if(!hint&&MS.hdAfter.indexOf(m.s)>=0)hint='after dialysis on dialysis days';
    return '<tr><th scope="row"><a href="'+encodeURIComponent(m.s)+'.html">'+esc(nm(m.s))+'</a>'+(hint?'<span class="dd-sub"> · '+(r&&r.quote?'label: ':'')+esc(hint)+'</span>':'')+use+'</th>'+
      '<td><input class="ms-in" data-i="'+i+'" data-k="dose" value="'+esc(m.dose)+'" placeholder="e.g. 50 mg, 1 tab" aria-label="Dose for '+esc(nm(m.s))+'"></td>'+
      '<td><select class="ms-in" data-i="'+i+'" data-k="freq" aria-label="How often">'+FREQ.map(function(f){return '<option value="'+f[0]+'"'+(f[0]===m.freq?' selected':'')+'>'+f[1]+'</option>';}).join('')+'</select></td>'+
      '<td><select class="ms-in" data-i="'+i+'" data-k="slot" aria-label="Timing">'+SLOTS.map(function(f){return '<option value="'+f[0]+'"'+(f[0]===m.slot?' selected':'')+'>'+f[1]+'</option>';}).join('')+'</select></td>'+
      '<td><button type="button" class="dd-ix-x" data-rm="'+i+'" aria-label="Remove '+esc(nm(m.s))+'">✕</button></td></tr>';}).join('')+'</tbody></table>';}
$('ms-list').addEventListener('input',function(e){var t=e.target;if(!t.classList.contains('ms-in'))return;MEDS[+t.getAttribute('data-i')][t.getAttribute('data-k')]=t.value;});
$('ms-list').addEventListener('change',function(e){var t=e.target;if(!t.classList.contains('ms-in'))return;MEDS[+t.getAttribute('data-i')][t.getAttribute('data-k')]=t.value;if(t.getAttribute('data-k')==='use'||t.getAttribute('data-k')==='freq')paintList();});
$('ms-list').addEventListener('click',function(e){var b=e.target.closest('[data-rm]');if(b){MEDS.splice(+b.getAttribute('data-rm'),1);paintList();}});
$('ms-clear').addEventListener('click',function(){MEDS=[];paintList();$('ms-out').innerHTML='';});
/* ── typeahead ── */
var q=$('dd-ix-q'),sug=$('dd-ix-sug');
function matches(v){var t=nrm(v);if(t.length<2)return [];var res=[];
  IDX.forEach(function(d){var sc=0,via='';if(d.nn.indexOf(t)===0)sc=100;else if((' '+d.nn).indexOf(' '+t)>=0)sc=70;
    (d.b||[]).forEach(function(b){var bn=nrm(b);var s2=bn===t?95:bn.indexOf(t)===0?85:0;if(s2>sc){sc=s2;via=b;}});
    (d.y||[]).forEach(function(y){var s2=nrm(y).indexOf(t)===0?80:0;if(s2>sc){sc=s2;via=y;}});
    if(sc)res.push({d:d,s:sc-(d.n.length/100),via:via});});res.sort(function(a,b){return b.s-a.s;});return res.slice(0,8);}
function showSug(){var m=matches(q.value);act=-1;if(!m.length){sug.hidden=true;q.setAttribute('aria-expanded','false');return;}
  sug.innerHTML=m.map(function(o,i){return '<li role="option" id="ms-o'+i+'" data-s="'+esc(o.d.s)+'" aria-selected="false">'+(o.via?'<strong>'+esc(o.via)+'</strong> <span class="dd-ix-arrow">→ '+esc(o.d.n)+'</span>':'<strong>'+esc(o.d.n)+'</strong>')+'</li>';}).join('');
  sug.hidden=false;q.setAttribute('aria-expanded','true');}
function pick(s){if(s){addMed(s);q.value='';sug.hidden=true;q.setAttribute('aria-expanded','false');q.focus();}}
q.addEventListener('input',function(){if(IDX)showSug();});
q.addEventListener('keydown',function(e){var o=sug.querySelectorAll('[role=option]');
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){if(!o.length)return;e.preventDefault();act=(act+(e.key==='ArrowDown'?1:-1)+o.length)%o.length;
    [].forEach.call(o,function(x,i){x.setAttribute('aria-selected',i===act?'true':'false');});q.setAttribute('aria-activedescendant',o[act].id);}
  else if(e.key==='Enter'){e.preventDefault();if(o.length)pick(o[Math.max(act,0)].getAttribute('data-s'));}
  else if(e.key==='Escape'){sug.hidden=true;}});
sug.addEventListener('mousedown',function(e){var li=e.target.closest('[role=option]');if(li){e.preventDefault();pick(li.getAttribute('data-s'));}});
document.addEventListener('click',function(e){if(!e.target.closest('.dd-ix-add'))sug.hidden=true;});
/* ── paste: medicine name + dose + frequency from the sig ── */
function dict(){if(DICT)return DICT;DICT={};var mx=1;IDX.forEach(function(d){function put(x,w){var k=nrm(x);if(k.length<4)return;if(!DICT[k]||w>DICT[k].w)DICT[k]={s:d.s,w:w};mx=Math.max(mx,k.split(' ').length);}
  put(d.n,3);(d.y||[]).forEach(function(y){put(y,2);});(d.b||[]).forEach(function(b){put(b,1);});});DICT.__mx=Math.min(mx,6);return DICT;}
function sig(line){var L=line.toLowerCase(),o={freq:'od',slot:''};
  var st=line.match(/(\d+(?:,\d{3})*(?:\.\d+)?\s*(?:mg|mcg|µg|g|iu|units?|u|ml|meq)(?:\s*\/\s*\d+(?:\.\d+)?\s*(?:mg|mcg|ml))?)/i),qt=line.match(/((?:\d+(?:\.\d+)?|½|1\/2|one|two|half)\s*(?:tabs?|tablets?|caps?|capsules?|sachets?|puffs?|drops?|ml|units?))/i);
  o.dose=[st&&st[1],qt&&qt[1]].filter(Boolean).join(', ');
  if(/\bprn\b|as needed/.test(L))o.freq='prn';
  else if(/post[- ]?(hd|dialysis)|after (each )?(hd|dialysis)/.test(L))o.freq='posthd';
  else if(/q\s*2\s*w|every (2|two) weeks/.test(L))o.freq='q2w';
  else if(/monthly|once a month|q\s*4\s*w/.test(L))o.freq='monthly';
  else if(/weekly|once a week|\bq\s*wk\b/.test(L))o.freq='weekly';
  else if(/\btiw\b|3x\s*(a|\/)?\s*w|thrice (a )?week|three times (a|per) week|\bmwf\b|\btths?\b/.test(L))o.freq='tiw';
  else if(/\bqid\b|four times|4x a day/.test(L))o.freq='qid';
  else if(/\btid\b|three times|3x a day|with (each|every) meal|with meals/.test(L))o.freq='tid';
  else if(/\bbid\b|twice|2x a day|\bq\s*12\s*h/.test(L))o.freq=/q\s*12/.test(L)?'q12':'bid';
  else if(/\bq\s*8\s*h/.test(L))o.freq='q8';else if(/\bq\s*6\s*h/.test(L))o.freq='q6';
  else if(/\bhs\b|bedtime|at night/.test(L))o.freq='hs';
  else if(/\bqam\b|every morning|in the morning/.test(L))o.freq='qam';
  else if(/\bqpm\b|every evening|in the evening/.test(L))o.freq='qpm';
  if(/binder|phosph|with (each |every )?meals?|\bac\b|\bpc\b/.test(L))o.use='binder';else if(/supplement|between meals|empty stomach|calcium repl/.test(L))o.use='supplement';
  if(/before breakfast|empty stomach/.test(L))o.slot='PB';
  else if(/(after|with) breakfast/.test(L))o.slot='B';
  else if(/(after|with) lunch/.test(L))o.slot='L';
  else if(/before (dinner|supper)/.test(L))o.slot='PD';
  else if(/(after|with) (dinner|supper)/.test(L))o.slot='D';
  return o;}
var SAMPLES={hd:{dx:'hd',days:[0,2,4],hs:'06:00',he:'10:00',hold:true,rx:['Sevelamer 800 mg 1 tab TID with meals','Calcium carbonate 500 mg 1 tab BID between meals (calcium supplement)','Calcitriol 0.25 mcg 1 cap post-HD','Levothyroxine 50 mcg 1 tab OD before breakfast','Amlodipine 10 mg 1 tab OD','Losartan 50 mg 1 tab OD','Carvedilol 6.25 mg 1 tab BID','Atorvastatin 40 mg 1 tab OD','Folic acid 5 mg 1 tab OD','Epoetin alfa 4,000 IU SC 3x a week','Iron sucrose 100 mg IV weekly']},
  ckd:{dx:'none',rx:['Losartan 100 mg 1 tab OD','Amlodipine 5 mg 1 tab OD','Furosemide 40 mg 1 tab every morning','Dapagliflozin 10 mg 1 tab OD','Atorvastatin 20 mg 1 tab OD','Sodium bicarbonate 650 mg 1 tab TID','Calcium carbonate 500 mg 1 tab TID with meals (binder)','Ferrous sulfate 325 mg 1 tab OD','Febuxostat 40 mg 1 tab OD','Levothyroxine 50 mcg 1 tab OD before breakfast']}};
root.addEventListener('click',function(e){var b=e.target.closest('[data-ms-sample]');if(!b)return;var S=SAMPLES[b.getAttribute('data-ms-sample')];
  var rd=root.querySelector('input[name=ms-dx][value='+S.dx+']');if(rd)rd.checked=true;
  if(S.dx==='hd'){root.querySelectorAll('[data-hdday]').forEach(function(x){x.checked=S.days.indexOf(+x.value)>=0;});$('ms-hs').value=S.hs;$('ms-he').value=S.he;$('ms-hold').checked=S.hold;$('ms-aht').value='auto';}
  paintHD();saveRoutine();MEDS=[];$('dd-ix-ta').value=S.rx.join('\n');$('dd-ix-parse').click();$('ms-build').click();});
$('dd-ix-parse').addEventListener('click',function(){var D=dict(),added=[],miss=[];
  $('dd-ix-ta').value.split(/\n|;/).forEach(function(line){var w=nrm(line).split(' ').filter(Boolean);if(!w.length)return;var f=null;
    for(var i=0;i<w.length&&!f;i++)for(var n=Math.min(D.__mx,w.length-i);n>=1;n--){var k=w.slice(i,i+n).join(' ');if(D[k]){f=D[k].s;break;}}
    if(f){addMed(f,sig(line));added.push(nm(f));}else if(/[a-z]{3}/i.test(line))miss.push(line.trim().slice(0,40));});
  $('dd-ix-pmsg').textContent=(added.length?'Read '+added.length+': '+added.join(', ')+'. Check the dose and frequency columns. ':'')+(miss.length?'Not recognized: '+miss.join('; ')+'.':'');});
/* ── the optimizer ── */
function slotTimes(R,hd){var T={W:R.wake,PB:Math.max(R.wake,R.bf-45),B:R.bf,MM:R.bf+150,L:R.lu,MA:Math.round((R.lu+R.di)/2),PD:R.di-45,D:R.di,
  E:Math.min(R.di+120,Math.round((R.di+R.bed)/2)),HS:R.bed};
  if(hd){T.POST=R.he+30;Object.keys(T).forEach(function(k){if(k!=='POST'&&T[k]>=R.hs-30&&T[k]<R.he+30)T[k]=k==='PB'?R.he+15:T.POST;});}
  return T;}
function options(m,r){var n=DAILY[m.freq]||0;if(!n)return [];
  if(m.slot)return [[m.slot].concat(n>1?({2:['D'],3:['L','D'],4:['L','D','HS']})[n].filter(function(x){return x!==m.slot;}).slice(0,n-1):[])];
  var meal=r&&r.meal,tod=r&&r.tod;
  if(m.freq==='hs'||tod==='bedtime')return [['HS']];
  if(m.freq==='qam')return [['B'],['W'],['MM']];
  if(m.freq==='qpm')return [['D'],['E'],['HS']];
  if(m.freq==='q8'||m.freq==='q6')return [['@'+m.freq]];
  if(meal==='between')return ({1:[['MM'],['MA'],['HS']],2:[['MM','MA'],['MM','HS'],['MA','HS']],3:[['MM','MA','HS']],4:[['W','MM','MA','HS']]})[n];
  if(n===1){if(r&&r.slot)return [[r.slot]];
    if(meal==='empty'&&tod==='morning')return [['PB'],['MM']];
    if(meal==='empty'||meal==='before')return [['PB'],['PD']];
    if(meal==='with'||meal==='after')return [['B'],['D'],['L']];
    if(tod==='evening')return [['D'],['E'],['HS']];if(tod==='morning')return [['B'],['W'],['MM']];
    return [['B'],['D'],['L'],['HS'],['W'],['MM'],['MA'],['E']];}
  if(n===2){if(meal==='empty'||meal==='before')return [['PB','PD']];
    if(meal==='with'||meal==='after')return [['B','D']];return [['B','D'],['W','E'],['MM','HS'],['PB','HS']];}
  if(n===3)return meal==='empty'||meal==='before'?[['PB','L','PD']]:[['B','L','D']];
  return [['B','L','D','HS']];}
function fixedTimes(m,R,T){var step=m.freq==='q8'?480:360,k=m.freq==='q8'?3:4,a=[];for(var i=0;i<k;i++)a.push(R.wake+i*step);return a;}
function sepRows(A,B){/* approved rows from A's lists that name B, with any stated spacing */var ga=IX.g[A]||{},gb=IX.g[B]||{},out=[];
  (ga.ow||[]).forEach(function(o){IX.rows.forEach(function(r,i){if(r[0]!==o||r[7])return;var hm=(r[5]||[]).some(function(x){return (gb.m||[]).indexOf(x)>=0;}),
    hc=(r[6]||[]).some(function(x){return (gb.c||[]).indexOf(x)>=0;})||((r[6]||[]).indexOf('alloral')>=0&&gb.o);if(hm||hc)out.push(i);});});return out;}
var ABS=/absorpt|absorb|bind|chelat|separate|apart|spacing/i;
function build(){var R=routine(),out=$('ms-out');
  if([R.wake,R.bf,R.lu,R.di,R.bed].some(function(x){return x==null;})){out.innerHTML='<p class="dd-note">Enter all the times of the patient\'s day.</p>';return;}
  if(!MEDS.length){out.innerHTML='<p class="dd-note">Add at least one medicine.</p>';return;}
  var hdOn=R.dx==='hd'&&R.days.length&&R.hs!=null&&R.he!=null&&R.he>R.hs;
  /* practice default (W. G. M. Rivero, MD, Nov 20 2026): with an early session (ends 30+ min before lunch) and the hold on,
     blood-pressure medicines go at one fixed time every day: once daily after lunch or after dinner (chosen), twice daily
     after lunch + bedtime, alpha blockers at bedtime. A time written in the sig still wins. */
  /* shift: early = ends 30+ min before lunch, afternoon = ends 30+ min before dinner, evening = later. Auto time: after lunch,
     after dinner, bedtime (after the session). Twice daily (after lunch + bedtime) only for the early shift. */
  var shift=!hdOn||!R.hold?'':R.he<=R.lu-30?'early':R.he<=R.di-30?'afternoon':'evening';
  var ahtSlot=R.aht&&R.aht!=='auto'?R.aht:({early:'L',afternoon:'D',evening:'HS'})[shift];
  function ahtFixed(m){if(!shift||m.slot||((IX.g[m.s]||{}).c||[]).indexOf('antihtn')<0)return null;
    var mols=(IX.g[m.s]||{}).m||[m.s];if(mols.some(function(x){return /azosin$/.test(x);})&&(DAILY[m.freq]===1))return [['HS']];
    if(m.freq==='od'||m.freq==='qam'||m.freq==='qpm')return [[ahtSlot]];
    if((m.freq==='bid'||m.freq==='q12')&&shift==='early')return [['L','HS']];return null;}
  /* interactions among the list */
  var hard=[],soft=[],other=[],seenRow={};
  MEDS.forEach(function(a,i){MEDS.forEach(function(b,j){if(i===j)return;sepRows(a.s,b.s).forEach(function(ri){var key=ri+'|'+[i,j].sort().join(',');if(seenRow[key])return;seenRow[key]=1;
    var r=IX.rows[ri],sp=MS.sep[String(ri)];
    if(sp)hard.push({i:i,j:j,before:sp[0],after:sp[1],row:r});
    else if(ABS.test(r[3]+' '+r[4]))soft.push({i:i,j:j,row:r});
    else other.push({i:i,j:j,row:r});});});});
  function plan(hd){var T=slotTimes(R,hd),place=[],conf=[],notes={};
    function times(k,opt){var m=MEDS[k];if(!opt)return [];if(opt[0]&&opt[0][0]==='@')return fixedTimes(m,R,T);return opt.map(function(s){return T[s];});}
    function viol(k,tk,pl){var v=0,s=0;hard.forEach(function(h){var other=h.i===k?h.j:h.j===k?h.i:-1;if(other<0||!pl[other])return;
        var ownerIsK=h.i===k,ta=ownerIsK?tk:pl[other].t,tb=ownerIsK?pl[other].t:tk;
        ta.forEach(function(x){tb.forEach(function(y){var ok=x<=y?(h.before!=null&&y-x>=h.before*60&&(x<y||h.before===0)):(h.after!=null&&x-y>=h.after*60);if(!ok)v++;});});});
      soft.forEach(function(h){var other=h.i===k?h.j:h.j===k?h.i:-1;if(other<0||!pl[other])return;tk.forEach(function(x){pl[other].t.forEach(function(y){if(Math.abs(x-y)<60)s++;});});});
      return [v,s];}
    var antiH=function(s){return ((IX.g[s]||{}).c||[]).indexOf('antihtn')>=0;};
    var order=MEDS.map(function(m,k){var r=ruleM(m),opts=options(m,r),f=ahtFixed(m);if(f)opts=f;return {k:k,r:r,opts:opts,fx:!!f};});
    /* dialysis-day moves */
    order.sort(function(a,b){return a.opts.length-b.opts.length;});
    var pl={};
    order.forEach(function(o){var m=MEDS[o.k];if(!o.opts.length)return;var best=null;
      o.opts.forEach(function(opt,oi){var tk=times(o.k,opt);
        if(hd&&!o.fx){var after=(o.r&&o.r.hd==='after')||MS.hdAfter.indexOf(m.s)>=0,hold=R.hold&&antiH(m.s);
          if(after||hold){var idx=-1,bestd=1e9;tk.forEach(function(x,ii){var d=Math.abs(x-R.he);if(d<bestd){bestd=d;idx=ii;}});
            if(after&&idx>=0)tk[idx]=T.POST;
            if(hold){/* hold only doses due in the 4 hours before the session or during it; never stack two doses of one medicine */
              tk=tk.map(function(x){return x>=R.hs-240&&x<R.he+30?T.POST:x;}).sort(function(p,q){return p-q;});
              var gap=tk.length>=3?180:240,lim=Math.max(T.HS,T.POST);
              for(var z=1;z<tk.length;z++)if(tk[z]-tk[z-1]<gap)tk[z]=tk[z-1]+gap;
              if(tk.length>1&&tk[tk.length-1]>lim){var st=(lim-tk[0])/(tk.length-1);tk=tk.map(function(x,ii){return Math.round((tk[0]+st*ii)/15)*15;});}}}}
        var vs=viol(o.k,tk,pl),used={};Object.keys(pl).forEach(function(z){pl[z].t.forEach(function(x){used[x]=1;});});
        var fresh=tk.filter(function(x){return !used[x];}).length,score=vs[0]*1000+vs[1]*50+fresh*5+oi;
        if(!best||score<best.score)best={score:score,t:tk,opt:opt,v:vs[0],s:vs[1]};});
      pl[o.k]=best;});
    hard.forEach(function(h){if(!pl[h.i]||!pl[h.j])return;var bad=false;pl[h.i].t.forEach(function(x){pl[h.j].t.forEach(function(y){
        var ok=x<=y?(h.before!=null&&y-x>=h.before*60&&(x<y||h.before===0)):(h.after!=null&&x-y>=h.after*60);if(!ok)bad=true;});});
      if(bad)conf.push(h);});
    return {T:T,pl:pl,conf:conf};}
  var P0=plan(false),P1=hdOn?plan(true):null;
  /* render */
  function table(P,title){var rows={};MEDS.forEach(function(m,k){var p=P.pl[k];if(!p)return;p.t.forEach(function(t){(rows[t]=rows[t]||[]).push(k);});});
    var ts=Object.keys(rows).map(Number).sort(function(a,b){return a-b;});
    function lab(t){if(P.T.POST===t)return 'after dialysis';for(var k in P.T)if(P.T[k]===t&&SLOTNAME[k])return SLOTNAME[k];return '';}
    return '<section class="dd-ix-card dd-ms-day"><h3>'+esc(title)+'</h3><table class="dd-ms-tt"><tbody>'+ts.map(function(t){
      return '<tr><th scope="row"><span class="dd-ms-time">'+fmt(t)+'</span><span class="dd-sub">'+esc(lab(t))+'</span></th><td><ul>'+rows[t].map(function(k){var m=MEDS[k];
        return '<li><strong>'+esc(nm(m.s))+'</strong>'+(m.dose?' <span class="dd-ms-dose">'+esc(m.dose)+'</span>':'')+'</li>';}).join('')+'</ul></td></tr>';}).join('')+'</tbody></table></section>';}
  var dayNames=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],hdDays=R.days.map(function(d){return dayNames[d];}).join(', ');
  var h='';
  var conflicts=(P0.conf.concat(P1?P1.conf:[])),cseen={},clist=[];conflicts.forEach(function(c){var k=[c.i,c.j].sort().join('-');if(cseen[k])return;cseen[k]=1;clist.push(c);});
  if(clist.length)h+='<div class="dd-ix-card dd-ms-warn"><h3>Spacing the routine cannot meet</h3><ul>'+clist.map(function(c){return '<li><strong>'+esc(nm(MEDS[c.i].s))+' and '+esc(nm(MEDS[c.j].s))+':</strong> '+esc(c.row[4])+' Move one of them with the timing menu, or adjust the routine. Each rule is in the source text shown under Why each medicine is where it is.</li>';}).join('')+'</ul></div>';
  h+='<div class="dd-ms-days2">'+table(P0,hdOn?'Non-dialysis days':'Every day')+(P1?table(P1,'Dialysis days ('+hdDays+'; session '+fmt(R.hs)+' to '+fmt(R.he)+')'):'')+'</div>';
  var non=MEDS.filter(function(m){return !DAILY[m.freq];});
  var unit=MEDS.filter(function(m){var r=ruleM(m);return r&&r.hd==='unit'&&DAILY[m.freq];});
  if(non.length||unit.length){var FN={};FREQ.forEach(function(f){FN[f[0]]=f[1];});
    h+='<section class="dd-ix-card"><h3>Not daily, or given at the dialysis unit</h3><ul>'+non.concat(unit).map(function(m){var r=ruleM(m);
      return '<li><strong>'+esc(nm(m.s))+'</strong>'+(m.dose?' '+esc(m.dose):'')+': '+esc(m.freq==='posthd'?'after each dialysis'+(hdOn?' ('+hdDays+')':''):FN[m.freq].toLowerCase())+(r&&r.hd==='unit'?' · given at the dialysis unit':'')+'</li>';}).join('')+'</ul></section>';}
  /* pill count: per dose (from the Dose column), per day and for N days, counted day by day on the real calendar */
  function qty(m){var s=(m.dose||'').toLowerCase(),q=s.match(/(\d+(?:\.\d+)?|½|1\/2|one|two|three|half)\s*(tabs?|tablets?|caps?|capsules?|sachets?|softgels?|puffs?)\b/);
    if(!q)return {n:1,u:'tab',assumed:true,known:false};
    var N={'½':.5,'1/2':.5,half:.5,one:1,two:2,three:3}[q[1]];var n=N!=null?N:parseFloat(q[1]);
    var u=/^cap/.test(q[2])?'cap':/^sachet/.test(q[2])?'sachet':/^softgel/.test(q[2])?'softgel':/^puff/.test(q[2])?'puff':'tab';return {n:n,u:u,known:true};}
  function countable(m){var r=ruleM(m);if(r&&r.hd==='unit')return false;var s=(m.dose||'').toLowerCase();
    if(/\b(iu|units?|ml)\b/.test(s)&&!/\b(tabs?|tablets?|caps?|capsules?|sachets?|softgels?)\b/.test(s))return false;return true;}
  function dosesOn(m,k,mon0,isHD){if(m.freq==='prn')return 0;
    if(DAILY[m.freq]){var P=isHD&&P1?P1:P0,p=P.pl[k];return p?p.t.length:0;}
    if(m.freq==='posthd')return isHD?1:0;
    if(m.freq==='tiw')return hdOn?(isHD?1:0):([0,2,4].indexOf(mon0)>=0?1:0);
    if(m.freq==='weekly')return mon0===0?1:0;return 0;}
  function pillRows(N){var start=new Date();start.setHours(12,0,0,0);
    return MEDS.map(function(m,k){var q=qty(m),cnt=countable(m),doses=0,dNon=null,dHD=null;
      for(var i=0;i<N;i++){var d=new Date(start.getTime()+i*864e5),mon0=(d.getDay()+6)%7,isHD=hdOn&&R.days.indexOf(mon0)>=0;doses+=dosesOn(m,k,mon0,isHD);}
      if(m.freq==='q2w')doses=Math.ceil(N/14);else if(m.freq==='monthly')doses=Math.ceil(N/30);
      if(DAILY[m.freq]){dNon=(P0.pl[k]?P0.pl[k].t.length:0);dHD=P1?(P1.pl[k]?P1.pl[k].t.length:0):null;}
      return {m:m,q:q,cnt:cnt,doses:doses,dNon:dNon,dHD:dHD,total:cnt?doses*q.n:null};});}
  function plural(u,n){return n===1?u:u+'s';}
  function fmtN(n){return (Math.round(n*10)/10).toLocaleString('en-US');}
  function pillTable(N,forPrint){var rows=pillRows(N),assumed=false,perNon=0,perHD=0;
    var body=rows.map(function(o){var m=o.m,q=o.q;if(o.cnt&&!q.known)assumed=true;
      if(o.cnt&&o.dNon!=null)perNon+=o.dNon*q.n;if(o.cnt&&o.dHD!=null)perHD+=o.dHD*q.n;
      if(o.cnt&&m.freq==='posthd'&&hdOn)perHD+=q.n;
      var per=o.cnt?fmtN(q.n)+' '+plural(q.u,q.n)+(q.known?'':'*'):(m.dose?esc(m.dose):'1 dose');
      var day=m.freq==='prn'?'as needed':o.dNon!=null?(o.dHD!=null&&o.dHD!==o.dNon?o.dNon+' (dialysis days '+o.dHD+')':String(o.dNon)):(m.freq==='posthd'?'after each dialysis':(FREQ.filter(function(f){return f[0]===m.freq;})[0]||['',''])[1].toLowerCase());
      var tot=m.freq==='prn'?'as needed':o.cnt?'<b>'+fmtN(o.total)+'</b> '+plural(q.u,o.total)+(q.known?'':'*'):'<b>'+o.doses+'</b> '+plural('dose',o.doses)+(ruleM(m)&&ruleM(m).hd==='unit'?' at the unit':'');
      return '<tr><td><b>'+esc(nm(m.s))+'</b></td><td>'+per+'</td><td>'+day+'</td><td class="'+(forPrint?'mss-num':'dd-pc-num')+'">'+tot+'</td></tr>';}).join('');
    var burden='Pills a day: <b>'+fmtN(perNon)+'</b>'+(hdOn?' on days without dialysis, <b>'+fmtN(perHD)+'</b> on dialysis days':'')+'.';
    return {html:'<table class="'+(forPrint?'mss-tt mss-pc':'dd-pc-tab')+'"><thead><tr><th>Medicine</th><th>Per dose</th><th>Doses a day</th><th>For '+N+' days</th></tr></thead><tbody>'+body+'</tbody></table>',
      burden:burden,assumed:assumed};}
  var PCN=+(localStorage.getItem('wgmr-ms-pcdays')||30)||30;
  function pcCard(){var p=pillTable(PCN,false);return '<p class="dd-pc-burden">'+p.burden+'</p>'+p.html+
    '<p class="dd-sub dd-pc-note">'+(p.assumed?'* No tablet or capsule count in the Dose column, so 1 per dose is assumed; type it there (e.g., "2 tabs") and build again. ':'')+
    'Counted on the calendar from today, using the dialysis days set above. Injections and medicines given at the dialysis unit are counted as doses, not pills.</p>';}
  h+='<section class="dd-ix-card dd-pc no-print"><div class="dd-pc-head"><h3>Pill count</h3><label>Days to cover <input type="number" id="ms-pcdays" min="1" max="365" value="'+PCN+'" inputmode="numeric"></label></div><div id="ms-pcbody">'+pcCard()+'</div></section>';
  /* why each placement */
  var why=MEDS.map(function(m,k){var r=ruleM(m),bits=[],tags=[];
    function cap(x){return x.charAt(0).toUpperCase()+x.slice(1);}
    if(r){if(r.use)bits.push('used as '+r.use.toLowerCase());if(r.meal)bits.push({with:'take with food',before:'take before meals',empty:'take on an empty stomach',between:'take between meals',after:'take after meals'}[r.meal]);
      if(r.tod&&!r.practice)bits.push('take in the '+r.tod);if(r.evid)tags.push(['evid','Evidence']);if(r.hd==='unit')bits.push('given at the dialysis unit');if(r.hd==='after')bits.push('dose after dialysis');
      if(r.quote)tags.push(['label','Label']);
      if(r.practice){bits.push('at bedtime, '+r.practice.replace(/^Bedtime by local practice, /,'').replace(/\.$/,''));tags.push(['practice','Practice default']);}}
    if(MS.hdAfter.indexOf(m.s)>=0&&!(r&&r.hd==='after')){bits.push('dose after dialysis on dialysis days');tags.push(['label','Kidney dosing']);}
    if(m.slot||m.freq==='hs'||m.freq==='qam'||m.freq==='qpm'){bits.unshift(m.freq==='hs'&&!m.slot?'at bedtime, as written in the prescription':m.freq==='qam'&&!m.slot?'in the morning, as written in the prescription':m.freq==='qpm'&&!m.slot?'in the evening, as written in the prescription':'time written in the prescription');tags.unshift(['you','Set by you']);}
    else if(ahtFixed(m)){bits.push('same time every day, after the dialysis session ('+shift+' shift)');tags.push(['practice','Practice default']);}
    if(!bits.length){bits.push('no timing rule; placed at a standard time');tags.push(['std','Standard time']);}
    var seen={};tags=tags.filter(function(x){if(seen[x[1]])return false;seen[x[1]]=1;return true;});
    var src=r&&r.quote?'<details class="dd-ms-src"><summary>Show label text</summary><blockquote>'+esc(r.quote)+'<cite>'+(r.url?'<a href="'+esc(r.url)+'" rel="noopener">'+esc(r.brand)+'</a>':esc(r.brand))+'</cite></blockquote></details>':'';
    if(r&&r.evid)src+='<details class="dd-ms-src"><summary>Show evidence</summary><blockquote>'+esc(r.evid.note)+r.evid.cites.map(function(c){return '<cite>'+esc(c.t)+' <a href="https://doi.org/'+esc(c.doi)+'" rel="noopener">doi:'+esc(c.doi)+'</a></cite>';}).join('')+'</blockquote></details>';
    var by='';
    return '<li class="dd-msw"><div class="dd-msw-n">'+esc(nm(m.s))+'</div><div class="dd-msw-r"><p>'+esc(cap(bits.join('; ')))+(r&&r.note?' <span class="dd-sub">'+esc(r.note)+'</span>':'')+'</p>'+
      '<div class="dd-msw-tags">'+tags.map(function(x){return '<span class="dd-msw-tag t-'+x[0]+'">'+x[1]+'</span>';}).join('')+by+'</div>'+src+'</div></li>';}).join('');
  function apart(x){return [P0,P1].every(function(P){if(!P)return true;var a=P.pl[x.i],c=P.pl[x.j];if(!a||!c)return true;return a.t.every(function(u){return c.t.every(function(v){return Math.abs(u-v)>=60;});});});}
  function pair(x,j){return '<strong>'+esc(nm(MEDS[x.i].s))+'</strong> '+j+' <strong>'+esc(nm(MEDS[x.j].s))+'</strong>';}
  function row(badge,body){return '<li class="dd-msw-pr"><div class="dd-msw-b">'+badge+'</div><div class="dd-msw-pt">'+body+'</div></li>';}
  var pseen={};
  var hardList=hard.filter(function(x){var k=[x.i,x.j].sort().join('-');if(pseen[k])return false;pseen[k]=1;return true;}).map(function(x){var bad=cseen[[x.i,x.j].sort().join('-')];
    return row('<span class="dd-msw-st '+(bad?'st-no':'st-ok')+'">'+(bad?'Not met':'Met')+'</span>',pair(x,'and')+'<span class="dd-msw-d">'+esc(x.row[4])+(bad?' See the warning at the top.':'')+'</span>');}).join('');
  var softList=soft.map(function(x){var ok=apart(x);
    return row('<span class="dd-msw-st '+(ok?'st-ok':'st-warn')+'">'+(ok?'Separated':'Same time')+'</span>',pair(x,'and')+'<span class="dd-msw-d">'+esc(x.row[4])+(ok?'':' Could not be separated in this routine.')+'</span>');}).join('');
  var GR={ci:'Contraindicated',avoid:'Avoid',adjust:'Adjust or monitor',minor:'Minor'},oseen={},otherList=other.filter(function(x){var k=[x.i,x.j].sort()+x.row[2];if(oseen[k])return false;oseen[k]=1;return true;})
    .sort(function(a,b){return ['ci','avoid','adjust','minor'].indexOf(a.row[1])-['ci','avoid','adjust','minor'].indexOf(b.row[1]);})
    .map(function(x){return row('<span class="dd-ix-g g-'+esc(x.row[1])+'">'+GR[x.row[1]]+'</span>',pair(x,'+')+'<span class="dd-msw-d">'+esc(x.row[3])+' '+esc(x.row[4])+'</span>');}).join('');
  h+='<section class="dd-ix-card dd-msw-card no-print"><h3>Why each medicine is where it is</h3><ul class="dd-msw-list">'+why+'</ul>'+
    (hardList?'<div class="dd-msw-blk"><h4>Spacing between medicines</h4><ul class="dd-msw-list">'+hardList+'</ul></div>':'')+
    (softList?'<div class="dd-msw-blk"><h4>Absorption interactions</h4><ul class="dd-msw-list">'+softList+'</ul></div>':'')+
    (otherList?'<div class="dd-msw-blk"><h4>Interactions timing cannot fix</h4><ul class="dd-msw-list">'+otherList+'</ul><p class="dd-msw-more"><a href="interactions.html?d='+MEDS.map(function(m){return encodeURIComponent(m.s);}).join(',')+'">Open these medicines in the Interaction checker &rarr;</a></p></div>':'')+'</section>';
  /* SeriousMD text */
  function txt(P,title){var rows={};MEDS.forEach(function(m,k){var p=P.pl[k];if(p)p.t.forEach(function(t){(rows[t]=rows[t]||[]).push(nm(m.s)+(m.dose?' '+m.dose:''));});});
    return title+'\n'+Object.keys(rows).map(Number).sort(function(a,b){return a-b;}).map(function(t){var l='';if(P.T.POST===t)l='after dialysis';else for(var kk in P.T)if(P.T[kk]===t&&SLOTNAME[kk]){l=SLOTNAME[kk];break;}
      return '  '+fmt(t)+(l?' ('+l+')':'')+': '+rows[t].join('; ');}).join('\n');}
  var text='OPTIMIZED MEDICATION INTAKE SCHEDULE\n'+txt(P0,hdOn?'Non-dialysis days:':'Daily:')+(P1?'\n'+txt(P1,'Dialysis days ('+hdDays+', session '+fmt(R.hs)+' to '+fmt(R.he)+'):'):'')+
    (non.length||unit.length?'\nOther: '+non.concat(unit).map(function(m){return nm(m.s)+(m.dose?' '+m.dose:'')+' '+(m.freq==='posthd'?'after each dialysis':(FREQ.filter(function(f){return f[0]===m.freq;})[0]||['',''])[1].toLowerCase());}).join('; '):'');
  text+='\nPill count for '+PCN+' days: '+pillRows(PCN).filter(function(o){return o.m.freq!=='prn';}).map(function(o){return nm(o.m.s)+' '+(o.cnt?fmtN(o.total)+' '+plural(o.q.u,o.total):o.doses+' '+plural('dose',o.doses));}).join('; ');
  h+='<section class="dd-ix-card no-print"><h3>Text for the prescription remarks</h3><textarea class="dd-ms-text" rows="8" readonly>'+esc(text)+'</textarea>'+
    '<div class="dd-ix-btns"><button type="button" class="dd-btn" id="ms-copy">Copy text</button> <button type="button" class="dd-btn dd-btn-ghost" id="ms-print">Print patient sheet</button></div></section>';
  /* patient print sheet (print only) */
  function how(m){var r=ruleM(m);if(!r)return '';var a=[];
    if(r.meal)a.push({with:'with food',before:'before meals',empty:'on an empty stomach',between:'between meals',after:'after meals'}[r.meal]);
    return a.join(', ');}
  function sheetTable(P,title,sub){var rows={};MEDS.forEach(function(m,k){var p=P.pl[k];if(!p)return;p.t.forEach(function(t){(rows[t]=rows[t]||[]).push(k);});});
    var ts=Object.keys(rows).map(Number).sort(function(a,b){return a-b;});
    function lab(t){if(P.T.POST===t)return 'after dialysis';for(var k in P.T)if(P.T[k]===t&&SLOTNAME[k])return SLOTNAME[k];return '';}
    return '<section class="mss-day"><h2>'+esc(title)+(sub?' <span>'+esc(sub)+'</span>':'')+'</h2><table class="mss-tt"><thead><tr><th class="mss-c-time">Time</th><th>Medicine and dose</th><th class="mss-c-how">How to take</th></tr></thead><tbody>'+
      ts.map(function(t){return rows[t].map(function(k,ii){var m=MEDS[k];
        return '<tr class="'+(ii===0?'mss-first':'')+'">'+(ii===0?'<td class="mss-c-time" rowspan="'+rows[t].length+'"><b>'+fmt(t)+'</b><span>'+esc(lab(t))+'</span></td>':'')+
          '<td><span class="mss-box" aria-hidden="true"></span><b>'+esc(nm(m.s))+'</b>'+(m.dose?' <span class="mss-dose">'+esc(m.dose)+'</span>':'')+'</td><td class="mss-c-how">'+esc(how(m))+'</td></tr>';}).join('');}).join('')+
      '</tbody></table></section>';}
  var today=new Date(),dstr=today.toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'});
  var routineLine='Wakes '+fmt(R.wake)+' · Breakfast '+fmt(R.bf)+' · Lunch '+fmt(R.lu)+' · Dinner '+fmt(R.di)+' · Bedtime '+fmt(R.bed);
  var sheet='<div id="ms-sheet" class="mss" aria-hidden="true"><header class="mss-head"><div><div class="mss-kicker">Renal Care Matters</div><h1>My medication schedule</h1></div>'+
    '<div class="mss-date">Prepared '+esc(dstr)+'</div></header>'+
    '<div class="mss-fields"><div>Name <span></span></div><div>Prepared by <span></span></div></div>'+
    '<p class="mss-routine">'+esc(routineLine)+(hdOn?'<br><b>Hemodialysis:</b> '+esc(hdDays)+', '+fmt(R.hs)+' to '+fmt(R.he):'')+'</p>'+
    sheetTable(P0,hdOn?'On days without dialysis':'Every day','')+(P1?sheetTable(P1,'On dialysis days',hdDays):'')+
    (non.length||unit.length?'<section class="mss-other"><h2>Other medicines</h2><ul>'+non.concat(unit).map(function(m){var r=ruleM(m),FN={};FREQ.forEach(function(f){FN[f[0]]=f[1];});
      return '<li><b>'+esc(nm(m.s))+'</b>'+(m.dose?' '+esc(m.dose):'')+': '+esc(m.freq==='posthd'?'after each dialysis':FN[m.freq].toLowerCase())+(r&&r.hd==='unit'?', given at the dialysis unit':'')+'</li>';}).join('')+'</ul></section>':'')+
    '<section class="mss-pcs" id="mss-pc">'+(function(){var p=pillTable(PCN,true);return '<h2>Pill count <span>for '+PCN+' days</span></h2>'+p.html+'<p class="mss-pcb">'+p.burden+'</p>';})()+'</section>'+
    '<footer class="mss-foot"><p>Take each medicine at the time shown and tick the box when taken. Do not stop or change a medicine without asking your doctor. <span class="mss-src">Med Scheduler · renalcarematters.com</span></p></footer></div>';
  out.innerHTML=h+sheet;
  $('ms-copy').addEventListener('click',function(){var b=this;(navigator.clipboard?navigator.clipboard.writeText(text):Promise.reject()).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy text';},1600);},function(){out.querySelector('.dd-ms-text').select();});});
  $('ms-print').addEventListener('click',function(){window.print();});
  $('ms-pcdays').addEventListener('input',function(){var v=Math.round(+this.value);if(!(v>=1&&v<=365))return;PCN=v;try{localStorage.setItem('wgmr-ms-pcdays',String(v));}catch(e){}
    $('ms-pcbody').innerHTML=pcCard();var ta=out.querySelector('.dd-ms-text');if(ta)ta.value=ta.value.replace(/\nPill count for [^\n]*$/,'')+'\nPill count for '+PCN+' days: '+pillRows(PCN).filter(function(o){return o.m.freq!=='prn';}).map(function(o){return nm(o.m.s)+' '+(o.cnt?fmtN(o.total)+' '+plural(o.q.u,o.total):o.doses+' '+plural('dose',o.doses));}).join('; ');var p=pillTable(PCN,true),sec=$('mss-pc');if(sec)sec.innerHTML='<h2>Pill count <span>for '+PCN+' days</span></h2>'+p.html+'<p class="mss-pcb">'+p.burden+'</p>';});
  out.scrollIntoView({behavior:'smooth',block:'start'});
}
$('ms-build').addEventListener('click',build);
load().then(function(){restoreRoutine();paintHD();
  var u=new URL(location.href);(u.searchParams.get('d')||'').split(',').filter(Boolean).forEach(function(s){addMed(s);});paintList();
}).catch(function(){$('ms-out').innerHTML='<p class="dd-note">The scheduler could not load its data. Check the connection, or open the Drug Index app once while online.</p>';});
})();
"""

# Favorites (device only) + Interaction checker (Nov 2026)
DRUG_JS += r"""
(function(){
'use strict';
var FAV='wgmr-drug-favs',REC='wgmr-drug-recent',KF='wgmr-ix-kidney';
function rd(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v;}catch(e){return d;}}
function wr(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
function favs(){var f=rd(FAV,[]);return Array.isArray(f)?f.filter(function(x){return typeof x==='string'&&/^[a-z0-9-]+$/.test(x);}):[];}
function isFav(s){return favs().indexOf(s)>=0;}
function toggleFav(s){var f=favs(),i=f.indexOf(s);if(i>=0)f.splice(i,1);else f.unshift(s);wr(FAV,f.slice(0,200));document.dispatchEvent(new CustomEvent('rcm-favs'));return i<0;}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function nrm(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();}
/* drug page: Favorite button */
Array.prototype.forEach.call(document.querySelectorAll('.dd-favbtn[data-fav]'),function(b){
  var s=b.getAttribute('data-fav');
  function paint(){var on=isFav(s);b.setAttribute('aria-pressed',on?'true':'false');b.classList.toggle('is-on',on);
    b.querySelector('.dd-favstar').textContent=on?'★':'☆';b.lastChild.textContent=on?' Favorite (saved)':' Favorite';}
  b.hidden=false;paint();b.addEventListener('click',function(){toggleFav(s);paint();});
  document.addEventListener('rcm-favs',paint);
});
/* index: favorites row (names from the search index) */
var fr=document.getElementById('dd-favs');
if(fr){
  var names=null;
  function paintIdx(){var f=favs();if(!f.length){fr.hidden=true;return;}
    function go(){fr.hidden=false;document.getElementById('dd-favlist').innerHTML=f.map(function(s){
      return '<a class="dd-ix-q" href="'+encodeURIComponent(s)+'.html">'+esc((names&&names[s])||s.replace(/-/g,' '))+'</a>';}).join('')+
      '<a class="dd-ix-q dd-ix-qgo" href="interactions.html?d='+f.slice(0,20).map(encodeURIComponent).join(',')+'">Check favorites together &rarr;</a>';}
    go();if(!names)fetch('/drugs/search-index.json').then(function(r){return r.json();}).then(function(j){names={};j.forEach(function(d){names[d.s]=d.n;});go();}).catch(function(){});}
  paintIdx();document.addEventListener('rcm-favs',paintIdx);
}
var root=document.getElementById('dd-ix');
if(!root)return;
var $=function(id){return document.getElementById(id);};
var q=$('dd-ix-q'),sug=$('dd-ix-sug'),selBox=$('dd-ix-sel'),out=$('dd-ix-out'),kf=$('dd-ix-kf');
var IDX=null,IX=null,BY={},SEL=[],act=-1,DICT=null;
var GR={ci:['Contraindicated','g-ci',4],avoid:['Avoid','g-avoid',3],adjust:['Adjust or monitor','g-adjust',2],minor:['Minor','g-minor',1]};
function load(){
  return Promise.all([fetch(root.getAttribute('data-src')).then(function(r){return r.json();}),
                      fetch(root.getAttribute('data-ix')).then(function(r){return r.json();})]).then(function(a){
    IDX=a[0];IX=a[1];IDX.forEach(function(d){d.nn=nrm(d.n);BY[d.s]=d;});});
}
function nm(s){return (BY[s]&&BY[s].n)||s.replace(/-/g,' ');}
/* ── selection ── */
function add(s,quiet){if(!BY[s]||SEL.indexOf(s)>=0)return false;SEL.push(s);
  var r=rd(REC,[]);r=[s].concat(r.filter(function(x){return x!==s;})).slice(0,12);wr(REC,r);if(!quiet)update();return true;}
function remove(s){SEL=SEL.filter(function(x){return x!==s;});update();}
function paintSel(){
  selBox.innerHTML=SEL.length?SEL.map(function(s){var f=isFav(s);
    return '<span class="dd-ix-chip"><a href="'+encodeURIComponent(s)+'.html">'+esc(nm(s))+'</a>'+
      '<button type="button" class="dd-ix-star'+(f?' is-on':'')+'" data-star="'+esc(s)+'" aria-pressed="'+f+'" aria-label="'+(f?'Remove ':'Add ')+esc(nm(s))+(f?' from':' to')+' favorites">'+(f?'★':'☆')+'</button>'+
      '<button type="button" class="dd-ix-x" data-rm="'+esc(s)+'" aria-label="Remove '+esc(nm(s))+'">✕</button></span>';}).join(''):'';
  var f=favs().filter(function(s){return BY[s];}),r=rd(REC,[]).filter(function(s){return BY[s];});
  function chips(list){return list.map(function(s){var on=SEL.indexOf(s)>=0;return '<button type="button" class="dd-ix-q'+(on?' is-on':'')+'" data-add="'+esc(s)+'"'+(on?' disabled':'')+'>'+(on?'✓ ':'+ ')+esc(nm(s))+'</button>';}).join('');}
  $('dd-ix-favrow').hidden=!f.length;$('dd-ix-fav').innerHTML=chips(f)+(f.length>1?'<button type="button" class="dd-ix-q dd-ix-qgo" data-addall="fav">Add all favorites</button>':'');
  $('dd-ix-recrow').hidden=!r.length;$('dd-ix-rec').innerHTML=chips(r);
}
document.addEventListener('rcm-favs',function(){paintSel();});
root.addEventListener('click',function(e){
  var t=e.target.closest('button');if(!t)return;
  if(t.hasAttribute('data-rm'))remove(t.getAttribute('data-rm'));
  else if(t.hasAttribute('data-star')){toggleFav(t.getAttribute('data-star'));}
  else if(t.hasAttribute('data-add')){add(t.getAttribute('data-add'));}
  else if(t.getAttribute('data-addall')==='fav'){favs().forEach(function(s){add(s,true);});update();}
});
/* ── typeahead: generic names, Philippine brands, other names ── */
function matches(v){var t=nrm(v);if(t.length<2)return [];var res=[];
  IDX.forEach(function(d){var sc=0,lab='',via='';
    if(d.nn.indexOf(t)===0)sc=100;else if((' '+d.nn).indexOf(' '+t)>=0)sc=70;
    (d.b||[]).forEach(function(b){var bn=nrm(b);var s2=bn===t?95:bn.indexOf(t)===0?85:0;if(s2>sc){sc=s2;via=b;}});
    (d.y||[]).forEach(function(y){var yn=nrm(y);var s2=yn.indexOf(t)===0?80:0;if(s2>sc){sc=s2;via=y;}});
    if(sc)res.push({d:d,s:sc-(d.n.length/100)+(d.k?1:0),via:via});});
  res.sort(function(a,b){return b.s-a.s;});return res.slice(0,8);}
function showSug(){var m=matches(q.value);act=-1;
  if(!m.length){sug.hidden=true;q.setAttribute('aria-expanded','false');sug.innerHTML='';return;}
  sug.innerHTML=m.map(function(o,i){return '<li role="option" id="dd-ix-o'+i+'" data-s="'+esc(o.d.s)+'" aria-selected="false">'+
    (o.via?'<strong>'+esc(o.via)+'</strong> <span class="dd-ix-arrow">→ '+esc(o.d.n)+'</span>':'<strong>'+esc(o.d.n)+'</strong>')+
    (SEL.indexOf(o.d.s)>=0?' <span class="dd-ix-have">added</span>':'')+'</li>';}).join('');
  sug.hidden=false;q.setAttribute('aria-expanded','true');}
function pick(s){if(s){add(s);q.value='';sug.hidden=true;q.setAttribute('aria-expanded','false');q.focus();}}
q.addEventListener('input',function(){if(IDX)showSug();});
q.addEventListener('keydown',function(e){var o=sug.querySelectorAll('[role=option]');
  if(e.key==='ArrowDown'||e.key==='ArrowUp'){if(!o.length)return;e.preventDefault();act=(act+(e.key==='ArrowDown'?1:-1)+o.length)%o.length;
    Array.prototype.forEach.call(o,function(x,i){x.setAttribute('aria-selected',i===act?'true':'false');});q.setAttribute('aria-activedescendant',o[act].id);o[act].scrollIntoView({block:'nearest'});}
  else if(e.key==='Enter'){e.preventDefault();if(o.length)pick(o[Math.max(act,0)].getAttribute('data-s'));}
  else if(e.key==='Escape'){sug.hidden=true;q.setAttribute('aria-expanded','false');}});
sug.addEventListener('mousedown',function(e){var li=e.target.closest('[role=option]');if(li){e.preventDefault();pick(li.getAttribute('data-s'));}});
document.addEventListener('click',function(e){if(!e.target.closest('.dd-ix-add'))sug.hidden=true;});
/* ── paste a list: longest generic/brand/other-name match per line ── */
function dict(){if(DICT)return DICT;DICT={};var mx=1;
  IDX.forEach(function(d){function put(x,w){var k=nrm(x);if(k.length<4)return;if(!DICT[k]||w>DICT[k].w)DICT[k]={s:d.s,w:w};mx=Math.max(mx,k.split(' ').length);}
    put(d.n,3);(d.y||[]).forEach(function(y){put(y,2);});(d.b||[]).forEach(function(b){put(b,1);});});
  DICT.__mx=Math.min(mx,6);return DICT;}
$('dd-ix-parse').addEventListener('click',function(){var D=dict(),added=[],miss=[];
  $('dd-ix-ta').value.split(/\n|;/).forEach(function(line){var w=nrm(line).split(' ').filter(Boolean);if(!w.length)return;var found=null;
    for(var i=0;i<w.length&&!found;i++)for(var n=Math.min(D.__mx,w.length-i);n>=1;n--){var k=w.slice(i,i+n).join(' ');if(D[k]){found=D[k].s;break;}}
    if(found){if(add(found,true))added.push(nm(found));}else if(/[a-z]{3}/i.test(line))miss.push(line.trim().slice(0,40));});
  update();$('dd-ix-pmsg').textContent=(added.length?'Added '+added.length+': '+added.join(', ')+'. ':'')+(miss.length?'Not recognized: '+miss.join('; ')+'.':'');});
/* ── state in the URL; kidney function remembered on this device ── */
function sync(){var u=new URL(location.href);u.searchParams.delete('add');u.searchParams.delete('fav');
  if(SEL.length)u.searchParams.set('d',SEL.join(','));else u.searchParams.delete('d');
  if(kf.value)u.searchParams.set('k',kf.value);else u.searchParams.delete('k');
  history.replaceState(null,'',u.pathname+(u.searchParams.toString()?'?'+u.searchParams.toString().replace(/%2C/g,','):''));}
kf.addEventListener('change',function(){wr(KF,kf.value);update();});
$('dd-ix-clear').addEventListener('click',function(){SEL=[];update();q.focus();});
$('dd-ix-print').addEventListener('click',function(){window.print();});
$('dd-ix-share').addEventListener('click',function(){var b=this;sync();
  (navigator.clipboard?navigator.clipboard.writeText(location.href):Promise.reject()).then(function(){b.textContent='Link copied';setTimeout(function(){b.textContent='Copy link';},1800);},
   function(){window.prompt('Copy this link',location.href);});});
/* ── the check ── */
function inter(a,b){return (a||[]).filter(function(x){return (b||[]).indexOf(x)>=0;});}
function rowHits(A,B){var ga=IX.g[A],gb=IX.g[B],hits=[];if(!ga||!gb)return hits;
  (ga.ow||[]).forEach(function(o){IX.rows.forEach(function(r,i){if(r[0]!==o||r[7])return;
    var hitM=inter(r[5],gb.m),hitC=inter(r[6],gb.c||[]);if(r[6].indexOf('alloral')>=0&&gb.o)hitC.push('alloral');
    if(hitM.length||hitC.length)hits.push({i:i,a:A,b:B,m:hitM,c:hitC});});});return hits;}
function badge(g){var x=GR[g]||GR.adjust;return '<span class="dd-ix-g '+x[1]+'">'+x[0]+'</span>';}
function kband(){var v=kf.value;return v;}
function update(){if(!IX)return;sync();paintSel();
  var sel=SEL.slice(),checked=sel.filter(function(s){return IX.g[s]&&!IX.g[s].loc;}),local=sel.filter(function(s){return IX.g[s]&&IX.g[s].loc;});
  if(!sel.length){out.innerHTML='<p class="dd-note">Add two or more medicines to check them together. Add one to see its kidney dosing and listed interactions.</p>';return;}
  var pairs={},seen={};
  checked.forEach(function(A){checked.forEach(function(B){if(A===B)return;rowHits(A,B).forEach(function(h){var key=[A,B].sort().join('|');
    var dk=key+'#'+IX.rows[h.i][2]+IX.rows[h.i][3];if(seen[dk])return;seen[dk]=1;(pairs[key]=pairs[key]||[]).push(h);});});});
  var list=Object.keys(pairs).map(function(k){var hs=pairs[k],top=Math.max.apply(null,hs.map(function(h){return GR[IX.rows[h.i][1]][2];}));
    return {k:k,hs:hs,top:top};}).sort(function(a,b){return b.top-a.top;});
  var cnt={4:0,3:0,2:0,1:0};list.forEach(function(p){cnt[p.top]++;});
  var h='';
  /* summary */
  h+='<div class="dd-ix-sum"><strong>'+sel.length+' medicine'+(sel.length>1?'s':'')+'</strong> · '+(checked.length>1?(list.length?list.length+' interacting pair'+(list.length>1?'s':''):'no interaction found in the reviewed lists'):'add another medicine to check pairs')+
    (list.length?' <span class="dd-ix-sumg">'+[4,3,2,1].filter(function(n){return cnt[n];}).map(function(n){var g=['','minor','adjust','avoid','ci'][n];return badge(g)+' '+cnt[n];}).join(' ')+'</span>':'')+'</div>';
  /* kidney checks */
  var kh=[];
  var dup={};checked.forEach(function(s){(IX.g[s].m||[]).forEach(function(m){(dup[m]=dup[m]||[]).push(s);});});
  Object.keys(dup).forEach(function(m){if(dup[m].length>1)kh.push('<li><strong>Same ingredient in '+dup[m].length+' products:</strong> '+esc(m.replace(/-/g,' '))+' ('+dup[m].map(function(s){return esc(nm(s));}).join(', ')+'). Check the total daily dose.</li>');});
  var nxs=checked.filter(function(s){return IX.nx[s];});
  if(nxs.length>1)kh.push('<li><strong>'+nxs.length+' medicines with a kidney injury warning:</strong> '+nxs.map(function(s){return '<a href="'+encodeURIComponent(s)+'.html#kidney-injury">'+esc(nm(s))+'</a> <span class="dd-sub">('+IX.nx[s].map(function(m){return esc(IX.nxl[m]||m);}).join(', ')+')</span>';}).join('; ')+'. Their US labels advise care with other kidney toxins; monitor serum creatinine.</li>');
  function inCls(s,k){return (IX.g[s].c||[]).indexOf(k)>=0;}
  var ns=checked.filter(function(s){return inCls(s,'nsaid');}),ra=checked.filter(function(s){return inCls(s,'ace')||inCls(s,'arb');}),di=checked.filter(function(s){return inCls(s,'diuretic');});
  if(ns.length&&ra.length&&di.length)kh.push('<li class="dd-ix-tw"><strong>"Triple whammy":</strong> an NSAID ('+ns.map(nm).map(esc).join(', ')+'), an ACE inhibitor or ARB ('+ra.map(nm).map(esc).join(', ')+') and a diuretic ('+di.map(nm).map(esc).join(', ')+') together. See the graded interactions below for what the monographs advise.</li>');
  /* kidney dosing at the chosen status */
  var kb=kband(),krows='';
  if(kb){var lab={ge60:'60 or more','30_59':'30 to 59','15_29':'15 to 29',lt15:'below 15',hd:'hemodialysis',pd:'peritoneal dialysis',crrt:'CRRT'}[kb];
    sel.forEach(function(s){var srcs=[];if(IX.k[s])srcs.push([s,IX.k[s]]);else (IX.g[s]&&IX.g[s].m||[]).forEach(function(m){if(m!==s&&IX.k[m])srcs.push([m,IX.k[m]]);});
      if(!srcs.length){krows+='<tr><th scope="row"><a href="'+encodeURIComponent(s)+'.html#kidney-dosing">'+esc(nm(s))+'</a></th><td class="dd-ix-kn">No reviewed kidney dosing yet; see the label text on the drug page.</td></tr>';return;}
      srcs.forEach(function(x){var kd=x[1],cell=null,rng='';
        if(kb==='hd'||kb==='pd'||kb==='crrt'){if(kd[kb]){cell=kd[kb];rng=kb.toUpperCase();}}
        else (kd.b||[]).forEach(function(b){if(b[0]===kb){cell=[b[2],b[3]];rng=b[1];}});
        var who=esc(nm(s))+(x[0]!==s?' <span class="dd-sub">('+esc(nm(x[0]))+' component)</span>':'');
        krows+='<tr><th scope="row"><a href="'+encodeURIComponent(x[0])+'.html#kidney-dosing">'+who+'</a></th>'+(cell?'<td><span class="dd-ix-kt k-'+esc(cell[1])+'">'+esc(cell[0])+'</span> <span class="dd-sub">'+esc(rng)+'</span></td>':'<td class="dd-ix-kn">No band for this level in the reviewed dosing.</td>')+'</tr>';});});
    kh.push('<li class="dd-ix-kdose"><strong>Kidney dosing ('+esc(lab)+'):</strong><table class="dd-ix-ktab"><tbody>'+krows+'</tbody></table></li>');}
  if(kh.length)h+='<section class="dd-ix-card dd-ix-kidney"><h2>Kidney checks</h2><ul>'+kh.join('')+'</ul>'+(kb?'':'<p class="dd-note">Choose the kidney function above to see each medicine\'s kidney dosing.</p>')+'</section>';
  else if(!kb)h+='<p class="dd-note dd-ix-khint">Choose the kidney function above to see each medicine\'s kidney dosing.</p>';
  /* graded pairs */
  if(list.length){h+='<section class="dd-ix-pairs"><h2>Interactions</h2>';
    list.forEach(function(p){var ab=p.k.split('|');
      h+='<article class="dd-ix-card dd-ix-pair">'+'<h3>'+badge(['','minor','adjust','avoid','ci'][p.top])+' '+esc(nm(ab[0]))+' + '+esc(nm(ab[1]))+'</h3>';
      p.hs.sort(function(x,y){return GR[IX.rows[y.i][1]][2]-GR[IX.rows[x.i][1]][2];}).forEach(function(hh){var r=IX.rows[hh.i];
        h+='<div class="dd-ix-row1">'+(p.hs.length>1?badge(r[1])+' ':'')+'<p class="dd-ix-src">From the <a href="'+encodeURIComponent(r[0])+'.html#interactions">'+esc(nm(r[0]))+'</a> monograph: <em>'+esc(r[2])+'</em>'+
          (hh.c.length&&!hh.m.length?' <span class="dd-sub">('+esc(nm(hh.b))+' is in this group: '+hh.c.map(function(c){return esc(IX.cls[c]||c);}).join(', ')+')</span>':'')+'</p>'+
          '<p><strong>What happens:</strong> '+esc(r[3])+'</p><p><strong>What to do:</strong> '+esc(r[4])+'</p></div>';});
      h+='</article>';});h+='</section>';}
  /* also check: food, alcohol, tests; rows that matched nothing */
  var also='',other='';
  checked.forEach(function(s){var a=[],o=[];(IX.g[s].ow||[]).forEach(function(ow){IX.rows.forEach(function(r){if(r[0]!==ow)return;
      if(r[7])a.push(r);else if(!r[5].length&&!r[6].length)o.push(r);});});
    function li(r){return '<li>'+badge(r[1])+' <em>'+esc(r[2])+'</em>: '+esc(r[4])+'</li>';}
    if(a.length)also+='<h3>'+esc(nm(s))+'</h3><ul>'+a.map(li).join('')+'</ul>';
    if(o.length)other+='<h3>'+esc(nm(s))+'</h3><ul>'+o.map(li).join('')+'</ul>';});
  if(also)h+='<details class="dd-ix-card dd-ix-also" open><summary>Also check: food, alcohol, lab tests and procedures</summary>'+also+'</details>';
  if(other)h+='<details class="dd-ix-card dd-ix-also"><summary>Other listed interactions (drugs not in the Philippine registry or not matched automatically)</summary>'+other+'</details>';
  /* coverage notes */
  var noList=checked.filter(function(s){return !(IX.g[s].ow||[]).length;});
  var notes=[];
  if(noList.length&&checked.length>1)notes.push('No reviewed interaction list yet for '+noList.map(nm).map(esc).join(', ')+'; pairs with these are found only from the other drug\'s list.');
  if(local.length)notes.push('Not checked (applied to the skin, eye, ear or nose): '+local.map(nm).map(esc).join(', ')+'.');
  notes.push('No result does not mean no interaction. Check the full prescribing information.');
  h+='<p class="dd-note dd-ix-cov">'+notes.join(' ')+'</p>';
  h+='<p class="no-print"><a class="dd-ix-q dd-ix-qgo" href="med-scheduler.html?d='+sel.map(encodeURIComponent).join(',')+'">Schedule these medicines in the Med Scheduler &rarr;</a></p>';
  out.innerHTML=h;
}
load().then(function(){
  var u=new URL(location.href),d=(u.searchParams.get('d')||'').split(',').filter(Boolean);
  d.forEach(function(s){add(s,true);});(u.searchParams.get('add')||'').split(',').filter(Boolean).forEach(function(s){add(s,true);});
  var k=u.searchParams.get('k')||rd(KF,'');
  if(!k){var p=rd('wgmr-rx-patient',{}),e=parseFloat(p&&p.egfr);if(e>0)k=e>=60?'ge60':e>=30?'30_59':e>=15?'15_29':'lt15';}
  if(k&&kf.querySelector('option[value="'+k+'"]'))kf.value=k;
  update();
}).catch(function(){out.innerHTML='<p class="dd-note">The checker could not load its data. Check the connection, or open the Drug Index app once while online.</p>';});
})();
"""



# ═════════════════════════════════════════════════════════════════════════════
# Label sanitizer (only used when a label section is delivered as HTML)
# ═════════════════════════════════════════════════════════════════════════════
class _Sanitizer(HTMLParser):
    ALLOWED = {"p", "br", "ul", "ol", "li", "b", "strong", "i", "em", "sub", "sup", "table", "thead",
               "tbody", "tr", "td", "th", "caption", "h4", "h5", "h6", "span", "div", "dl", "dt", "dd"}
    DROP = {"script", "style", "iframe", "object", "embed"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.DROP:
            self.skip += 1
        elif not self.skip and tag in self.ALLOWED:
            keep = [(k, v) for k, v in attrs if k in ("colspan", "rowspan") and v and v.isdigit()]
            self.out.append(f"<{tag}" + "".join(f' {k}="{v}"' for k, v in keep) + ">")

    def handle_endtag(self, tag):
        if tag in self.DROP:
            self.skip = max(0, self.skip - 1)
        elif not self.skip and tag in self.ALLOWED and tag != "br":
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(esc(data))


def sanitize_html(s: str) -> str:
    p = _Sanitizer()
    p.feed(s)
    p.close()
    return "".join(p.out)



# ═════════════════════════════════════════════════════════════════════════════
# Readability helpers for verbatim label text (words are never changed: only spacing
# inside "( 5.1 )" cross-references, "B 12" → "B12", and where paragraphs/list items break)
# ═════════════════════════════════════════════════════════════════════════════
def tidy_label(t: str) -> str:
    t = re.sub(r"\(\s*(\d+(?:\.\d+)*(?:\s*,\s*\d+(?:\.\d+)*)*)\s*\)",
               lambda m: "(" + re.sub(r"\s*,\s*", ", ", m.group(1).strip()) + ")", t)
    t = re.sub(r"(?<=[^\s(])\((\d+\.\d)", r" (\1", t)          # "warning.(5.1)" → "warning. (5.1)"
    t = re.sub(r"\bB\s+12\b", "B12", t)
    t = re.sub(r"(\d)\s*m\s+2\b", "\\1 m\u00b2", t)                     # "1.73 m 2" → "1.73 m²" (lost superscript)
    t = re.sub(r"\s+([,;:.)\]])(?=[\s,;:.)\]]|$)", r"\1", t)        # "m² ," → "m²,"; "(4) ]." → "(4)]."
    t = re.sub(r"([\[(])\s+", r"\1", t)                             # "[ see" → "[see"
    return t


_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(•])")


_RUNIN = re.compile(r"(?<=[.!?])\s+(?=[A-Z][^.!?\u2014]{2,60}?\s\u2014\s)")


def label_paras(t: str, min_chars: int = 320) -> str:
    """Long verbatim passage → short paragraphs (2–4 sentences); run-in subheadings ('Age 65 or greater — …')
    start their own paragraph in bold; '•' runs → a bulleted list."""
    t = tidy_label(ws(t))
    if not t:
        return ""
    blocks = _RUNIN.split(t)
    if len(blocks) > 1:
        out = []
        for b in blocks:
            m = re.match(r"([A-Z][^.!?\u2014]{2,60}?)\s\u2014\s(.*)$", b)
            if m:
                inner = label_paras(m.group(2), min_chars)
                inner = re.sub(r"^<p>", f"<p><strong>{esc(m.group(1))}</strong> \u2014 ", inner, count=1) if inner.startswith("<p>") \
                    else f"<p><strong>{esc(m.group(1))}</strong></p>" + inner
                out.append(inner)
            else:
                out.append(label_paras(b, min_chars))
        return "".join(out)
    parts = [x.strip() for x in re.split(r"\s*[•●▪]\s+", t)]
    lead, items = parts[0], [x for x in parts[1:] if x]
    out, buf, n = [], [], 0
    for snt in _SENT_SPLIT.split(lead):
        buf.append(snt)
        n += len(snt)
        if n >= min_chars and len(buf) >= 2:
            out.append(f"<p>{esc(' '.join(buf))}</p>")
            buf, n = [], 0
    if buf:
        out.append(f"<p>{esc(' '.join(buf))}</p>")
    if items:
        out.append("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>")
    return "".join(out)


def highlights_html(t: str) -> str:
    """Label 'highlights' preamble: one list item per cross-referenced point, e.g. '… abnormalities. (5.2)'."""
    t = tidy_label(ws(t))
    bits = re.split(r"(\(\d+\.\d+(?:, \d+\.\d+)*\))\s+", t)
    items = [(bits[i] + (" " + bits[i + 1] if i + 1 < len(bits) else "")).strip() for i in range(0, len(bits), 2)]
    items = [x for x in items if x]
    if len(items) >= 2:
        return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"
    return label_paras(t)


def render_label_value(v) -> str:
    """Verbatim text → escaped paragraphs; {"html": ...} → whitelisted HTML."""
    if v is None:
        return ""
    if isinstance(v, dict):
        if v.get("html"):
            return sanitize_html(v["html"])
        v = v.get("text") or v.get("paragraphs") or ""
    items = v if isinstance(v, list) else [v]
    out = []
    for item in items:
        if isinstance(item, dict):
            out.append(render_label_value(item))
            continue
        for para in re.split(r"\n\s*\n", str(item).strip()):
            if para.strip():
                out.append(label_paras(para) if len(para) > 600 and "\n" not in para.strip()
                           else f"<p>{esc(tidy_label(para.strip()))}</p>")
    return "".join(out)


# Display order; each entry: (heading, [accepted keys in priority order])
LABEL_SECTIONS = [
    ("Boxed warning", ["boxed_warning"]),
    ("Indications and usage", ["indications_and_usage", "indications"]),
    ("Dosage and administration", ["dosage_and_administration", "dosage"]),
    ("Contraindications", ["contraindications"]),
    ("Warnings and precautions", ["warnings_and_cautions", "warnings_and_precautions", "warnings", "precautions"]),
    ("Drug interactions", ["drug_interactions"]),
    ("Adverse reactions", ["adverse_reactions"]),
    ("Pregnancy", ["pregnancy", "teratogenic_effects", "pregnancy_or_breast_feeding"]),
    ("Lactation", ["lactation", "nursing_mothers"]),
    ("Pediatric use", ["pediatric_use"]),
    ("Geriatric use", ["geriatric_use"]),
    ("Use in specific populations", ["use_in_specific_populations"]),
]


def label_meta(label: dict) -> dict:
    """Attribution fields from either the workstream-B schema (source{}, label{}) or a flat/openFDA record."""
    lm = label.get("label") if isinstance(label.get("label"), dict) else {}
    src = label.get("source")
    sd = src if isinstance(src, dict) else {}
    of = label.get("openfda") if isinstance(label.get("openfda"), dict) else {}
    set_id = ws(lm.get("set_id") or label.get("set_id") or (of.get("spl_set_id") or [""])[0])
    date = lm.get("effective_time") or label.get("version_date") or label.get("effective_date") or label.get("effective_time")
    title = ws(label.get("title") or label.get("spl_title") or " · ".join(x for x in (ws(lm.get("brand_name")), ws(lm.get("manufacturer_name"))) if x))
    url = safe_url(sd.get("dailymed_url") or label.get("url")) or (
        f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={set_id}" if set_id else "")
    via = ws(sd.get("via")) if sd else ws(src)
    return {"set_id": set_id, "version": ws(lm.get("version") or label.get("version")),
            "date": us_date_str(date) if date else "", "title": title, "url": url,
            "via": "DailyMed/openFDA" if not via else ("DailyMed/openFDA" if "openfda" in via.lower() else via)}


def label_sections(label: dict) -> dict:
    secs = label.get("sections") if isinstance(label.get("sections"), dict) else label
    return secs if isinstance(secs, dict) else {}


# ═════════════════════════════════════════════════════════════════════════════
# Data loading
# ═════════════════════════════════════════════════════════════════════════════
def load_registry(data_dir: Path) -> list[dict]:
    shard_dir = data_dir / "registry"
    products = []
    if shard_dir.is_dir():
        for f in sorted(shard_dir.glob("*.json")):
            rows = load_json(f, [])
            if isinstance(rows, dict):
                rows = rows.get("products") or []
            products.extend(rows)
    else:
        legacy = load_json(data_dir / "registry.json", [])
        products = legacy.get("products", []) if isinstance(legacy, dict) else legacy
    # reviewed dispensing corrections for single registrations (e.g. an ARB coded OTC), keyed by registration number
    ov = load_json(data_dir / "dispensing_overrides.json", {}) or {}
    ov = ov.get("items", {}) if isinstance(ov, dict) else {}
    for p in products:
        o = ov.get(ws(p.get("registration_number")).upper())
        if isinstance(o, dict) and ws(o.get("dispensing")) in ("Rx", "OTC", "HR"):
            p["dispensing"] = ws(o["dispensing"])
    # brand names confirmed by Dr. Rivero for registrations the FDA lists without a brand (FDA value wins once present)
    bo = load_json(data_dir / "brand_overrides.json", {}) or {}
    bo = bo.get("items", {}) if isinstance(bo, dict) else {}
    for p in products:
        o = bo.get(ws(p.get("registration_number")).upper())
        cur = ws(p.get("brand_name"))
        if isinstance(o, dict) and ws(o.get("brand_name")) and (not cur or cur.lower().strip(" .") in _NO_BRAND):
            p["brand_name"] = ws(o["brand_name"])
            p["brand_note"] = ws(o.get("note")) or "Brand per distributor; the FDA record lists no brand."
    return [p for p in products if not ws(p.get("registration_number")).upper().startswith("VR-")]


class Ctx:
    def __init__(self, data_dir: Path, today: dt.date):
        self.data_dir, self.today = data_dir, today
        self.generics = load_json(data_dir / "generics.json", {}) or {}
        self.related_guides = load_json(data_dir / "related_guides.json", {}) or {}   # tools/drugdb/build_related_guides.py
        self.products = load_registry(data_dir)
        self.by_slug: dict[str, list] = defaultdict(list)
        for p in self.products:
            s = ws(p.get("generic_slug"))
            if s:
                self.by_slug[s].append(p)
        for s, ps in self.by_slug.items():   # products whose slug is missing from generics.json
            if s not in self.generics:
                self.generics[s] = {"name": ws(ps[0].get("generic_name")) or s, "ingredients": ps[0].get("ingredients", []),
                                    "products": len(ps), "categories": sorted({ws(p.get("pharmacologic_category")) for p in ps} - {""})}
                print(f"  ! slug {s!r} not in generics.json; using registry data", file=sys.stderr)
        self.pnf_meta, self.pnf = unwrap(load_json(data_dir / "pnf.json", {}))
        self.price_meta, self.prices = unwrap(load_json(data_dir / "prices.json", {}))
        self.retail_meta, self.retail = unwrap(load_json(data_dir / "prices-retail.json", {}))
        ph = load_json(data_dir / "pharmacies.json", []) or []
        ph = ph if isinstance(ph, list) else ph.get("pharmacies", [])
        self.pharmacies = []
        for x in ph:
            if not (isinstance(x, dict) and x.get("enabled") is True and safe_url(x.get("search_url_template"))):
                continue
            lt = ws(x.get("link_type")) or ("search" if "{q}" in x["search_url_template"] else "home")
            if lt == "search" and "{q}" not in x["search_url_template"]:
                continue
            self.pharmacies.append(dict(x, link_type=lt))
        self.labels_dir, self.renal_dir = data_dir / "labels", data_dir / "renal"
        self.nephrotox = load_json(data_dir / "nephrotox.json", {}) or {}   # tools/drugdb/build_nephrotox.py
        self._nx = {}
        # variant / misspelled generic names -> main molecule page (tools/drugdb/build_aliases.py)
        self.aliases: dict[str, dict] = {}
        self.variants_of: dict[str, list[str]] = defaultdict(list)
        for v, e in sorted((load_json(data_dir / "aliases.json", {}) or {}).items()):
            m = ws((e or {}).get("main")) if isinstance(e, dict) else ""
            if (v.startswith("_") or not m or m == v or v not in self.generics or m not in self.generics
                    or not self.by_slug.get(v) or not self.by_slug.get(m)):
                continue
            self.aliases[v] = {"main": m, "high": ws(e.get("confidence")) == "high", "reason": ws(e.get("reason"))}
        for v, e in list(self.aliases.items()):
            if e["main"] in self.aliases:          # never chain; a main must not itself be a variant
                del self.aliases[v]
        for v, e in self.aliases.items():
            self.variants_of[e["main"]].append(v)
        cj = load_json(data_dir / "controlled.json", {}) or {}
        self._controlled = cj.get("items", {}) if isinstance(cj, dict) else {}
        srcs = cj.get("sources") if isinstance(cj, dict) else None
        self.controlled_sources = {}
        for x in srcs or []:
            if isinstance(x, dict):
                self.controlled_sources[ws(x.get("id"))] = x

    def label(self, slug):
        return load_json(self.labels_dir / f"{slug}.json") if self.labels_dir.is_dir() else None

    def single_slug(self, ingredient: str) -> str:
        """Single-agent page for a combination component (exact name, then synonym/salt-folded name);
        variant spellings resolve to their main page. '' when there is no page."""
        if not hasattr(self, "_single"):
            exact: dict[str, list[str]] = defaultdict(list)
            canon: dict[str, list[str]] = defaultdict(list)
            for s, g in self.generics.items():
                ings = [ws(i) for i in (g.get("ingredients") or []) if ws(i)]
                if len(ings) != 1 or not self.by_slug.get(s):
                    continue
                a = self.aliases.get(s)
                t = a["main"] if a and a["high"] else s
                for n in (ings[0], ws(g.get("name"))):
                    exact[SYN.norm(n)].append(t)
                    canon[SYN.canonical(n)].append(t)

            def best(c):   # prefer a labeled page, then reviewed kidney dosing, then the most products
                return max(sorted(set(c)), key=lambda x: (x not in self.aliases, bool(_lab(self.label(x)) or self.eu(x)),
                                                          renal_approved(self.renal(x)), len(self.by_slug.get(x, []))))
            self._single = ({k: best(v) for k, v in exact.items()}, {k: best(v) for k, v in canon.items()})
        ex, ca = self._single
        return ex.get(SYN.norm(ingredient)) or ca.get(SYN.canonical(ingredient)) or ""

    def controlled(self, slug):
        it = self._controlled.get(slug)
        return it if isinstance(it, dict) else None

    def summary(self, slug):
        d = self.data_dir / "summary"
        return load_json(d / f"{slug}.json") if d.is_dir() else None

    def renal(self, slug):
        return load_json(self.renal_dir / f"{slug}.json") if self.renal_dir.is_dir() else None

    def nx(self, slug):
        """Kidney injury risk tags (data/drugs/nephrotox.json, approved only) for a generic:
        {"items": [(ingredient, key, rec)], "partial": bool} or None. Ingredient names match a tag key exactly or
        as a prefix (longest key wins). Only generics with at least one systemic (oral, injected, rectal) product are
        tagged; "partial" = some products are applied to skin, eye, ear or nose, or inhaled."""
        if slug in self._nx:
            return self._nx[slug]
        res, doc = None, self.nephrotox
        if doc.get("review_status") == "approved":
            keys = doc.get("ingredients") or {}
            items = []
            for ing in (self.generics.get(slug) or {}).get("ingredients") or []:
                il = ws(ing).lower()
                best = max((k for k in keys if il == k or il.startswith(k + " ")), key=len, default=None)
                if best and best not in [b for _, b, _ in items]:
                    items.append((ing, best, keys[best]))
            if items:
                fg = [(form_group(ws(p.get("dosage_strength_form"))), ws(p.get("dosage_strength_form")))
                      for p in self.by_slug.get(slug, [])]
                local = [d for f, d in fg if f not in NX_SYSTEMIC or NX_LOCAL.search(d)]
                # a liquid or unclassified product with no oral wording counts as systemic only on a page with no
                # local products (e.g. "0.3% w/v Sterile Suspension" among eye drops is an eye product)
                sysm = [f for f, d in fg if f in NX_SYSTEMIC and not NX_LOCAL.search(d)
                        and (f not in ("oral liquid", "other") or NX_ORAL.search(d) or not local)]
                if sysm or not fg:
                    res = {"items": items, "partial": len(sysm) < len(fg)}
        self._nx[slug] = res
        return res

    def intl(self, slug):
        """Non-US regulator product information metadata (labels-intl/<slug>.json) for generics without a US label."""
        d = self.data_dir / "labels-intl"
        return load_json(d / f"{slug}.json") if d.is_dir() else None

    def eu(self, slug):
        """EU SmPC (EMA) record (labels-eu/<slug>.json); used only when the generic has no US label."""
        d = self.data_dir / "labels-eu"
        e = load_json(d / f"{slug}.json") if d.is_dir() else None
        return e if eu_r.usable(e) else None


# ═════════════════════════════════════════════════════════════════════════════
# Page chrome
# ═════════════════════════════════════════════════════════════════════════════
NAV = [("CALCULATORS", "/guides/calculators.html"), ("PHYSIOLOGY", "/guides/kidney-physiology.html"),
       ("ATLAS", "/guides/nephrology-atlas.html"), ("GUIDES", "/guides/"), ("DRUGS", "/drugs/"), ("ABOUT", "/about.html")]


def header(current_drugs: bool) -> str:
    links = "".join(f'<a href="{u}" class="is-current" aria-current="page">{t}</a>' if (t == "DRUGS" and current_drugs)
                    else f'<a href="{u}">{t}</a>' for t, u in NAV)
    return ('<header class="site-header">\n  <a href="https://renalcarematters.com" class="brand">HOME</a>\n'
            f'  <nav class="header-nav" aria-label="Site">{links}</nav>\n</header>\n')


def head(title, desc, canonical, jsonld, content_hash, keywords="", robots="index, follow") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
{APP_HEAD}<script>try{{if(localStorage.getItem('wgmr-dark')==='1')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}</script>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{f'<meta name="keywords" content="{esc(keywords)}">' if keywords else ''}
<meta name="robots" content="{robots}">
<meta name="generator" content="{GENERATOR_TAG}">
<meta name="rcm-content-hash" content="{content_hash}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/app/dosis-180.png">
<meta name="theme-color" content="#0f1e33">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Renal Care Matters">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Drug Index · Every Philippine-registered drug, with kidney dosing · renalcarematters.com">
<meta property="og:locale" content="en_PH">
<meta property="article:modified_time" content="__ISO__">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONTS}" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="__DRUGDB_CSS__">
<script type="application/ld+json">{jsonld}</script>
<script type="speculationrules">{{"prefetch":[{{"where":{{"and":[{{"href_matches":"/*"}},{{"not":{{"href_matches":"*.json"}}}}]}},"eagerness":"moderate"}}],"prerender":[{{"urls":["/guides/","/drugs/","/"],"eagerness":"moderate"}}]}}</script>
</head>
"""


FOOTER = f"""
<footer class="guide-footer">
<div class="footer-inner">
<p><strong>Data sources.</strong> Philippine product registrations: Food and Drug Administration Philippines
(<a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verification.fda.gov.ph</a>). US prescribing information:
US FDA-approved labeling via DailyMed and openFDA (public domain). renalcarematters.com does not sell medicines and is not
affiliated with the Philippine FDA, the US FDA, or any pharmacy.</p>
<p>&copy; {dt.date.today().year} W Rivero, MD, FPCP, DPSN &middot; <a href="https://renalcarematters.com">renalcarematters.com</a></p>
</div>
</footer>
"""

FLOAT = """
<button aria-label="Print this page" class="print-btn no-print" onclick="window.print()" type="button">
<span class="p-tip">Print / Save PDF</span>
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect height="8" width="12" x="6" y="14"></rect></svg>
</button>
<button class="scroll-top-btn no-print" id="scrollTopBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Scroll to top" type="button">
<span class="p-tip">Back to top</span>
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>
<div class="float-controls no-print">
<button id="darkToggle" class="float-btn" type="button" onclick="toggleDark()" aria-label="Toggle dark mode" title="Switch to dark mode">
<span class="float-tooltip" id="darkLabel">Dark mode</span>
<svg id="darkIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
</button>
</div>
<script src="/assets/drug-hero.js?v=3" defer></script>
<script src="/assets/share-buttons.js" defer></script>
<script src="__DRUGDB_JS__" defer></script>
</body>
</html>
"""


# ═════════════════════════════════════════════════════════════════════════════
# Installable app (PWA): manifest, service worker, offline page
# ═════════════════════════════════════════════════════════════════════════════
APP_MARK = '<link rel="manifest" href="/drugs/app.webmanifest">'
APP_ICON_TAG = '<link rel="apple-touch-icon" sizes="180x180" href="/images/app/dosis-180.png">'   # iPhone home-screen icon (full-bleed; iOS rounds the corners)
LEGACY_ICON_TAG = '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'   # what page hashes were computed with
APP_HEAD = (APP_MARK + '\n<meta name="mobile-web-app-capable" content="yes">\n'
            '<meta name="apple-mobile-web-app-capable" content="yes">\n'
            '<meta name="apple-mobile-web-app-title" content="Dosis">\n'
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
            "<script>if('serviceWorker'in navigator)addEventListener('load',function(){navigator.serviceWorker"
            ".register('/drugs/sw.js',{scope:'/drugs/'}).catch(function(){});});</script>\n")

APP_MANIFEST = {
    "id": "/drugs/",
    "name": "Dosis · Drug Index",
    "short_name": "Dosis",
    "description": "Philippine-registered drugs with kidney dosing and US FDA prescribing information, for health professionals.",
    "start_url": "/drugs/",
    "scope": "/drugs/",
    "display": "standalone",
    "orientation": "any",
    "background_color": "#ffffff",
    "theme_color": "#0f1e33",
    "lang": "en",
    "dir": "ltr",
    "categories": ["medical", "health", "reference"],
    "icons": [
        {"src": "/images/app/dosis-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/dosis-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/dosis-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/dosis-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/dosis-180.png", "sizes": "180x180", "type": "image/png", "purpose": "any"},
    ],
    "shortcuts": [
        {"name": "Kidney dosing", "short_name": "Kidney dosing", "url": "/drugs/?view=kidney",
         "icons": [{"src": "/images/app/dosis-192.png", "sizes": "192x192", "type": "image/png"}]},
        {"name": "Food supplements & medical nutrition", "short_name": "Supplements", "url": "/drugs/supplements/",
         "icons": [{"src": "/images/app/dosis-192.png", "sizes": "192x192", "type": "image/png"}]},
    ],
}

SW_JS = r"""/* Generated by generate_drug_pages.py; do not edit. Offline support for Dosis, the Drug Index app (/drugs/). */
'use strict';
var V='__V__';
var SHELL='rcm-drugs-shell-'+V,PAGES='rcm-drugs-pages',SAVED='rcm-drugs-saved',DATA='rcm-drugs-data',ASSETS='rcm-drugs-assets';
var SHELL_URLS=__SHELL__;            // must all load, or the install is retried later
var OPTIONAL_SHELL=__OPTIONAL__;     // nice to have offline
var CORE_PAGES=['/drugs/','/drugs/offline','/drugs/supplements/','/drugs/interactions','/drugs/med-scheduler'];
var DATA_URLS=__DATA__;
var ASSET_URLS=__ASSETS__;
var MAX_PAGES=300,MAX_ASSETS=400;

function pageKey(u){u=new URL(u,self.location.origin);var p=u.pathname;
  if(/\/index\.html$/.test(p))p=p.slice(0,-10);else if(/\.html$/.test(p))p=p.slice(0,-5);return u.origin+p;}
function clean(res){return res.blob().then(function(b){return new Response(b,{status:res.status,statusText:res.statusText,
  headers:{'Content-Type':res.headers.get('content-type')||'text/html; charset=utf-8'}});});}
function trim(name,max){return caches.open(name).then(function(c){return c.keys().then(function(k){
  if(k.length<=max)return;return Promise.all(k.slice(0,k.length-max).map(function(r){return c.delete(r);}));});});}
function getInto(name,urls,keyFn,html){return caches.open(name).then(function(c){return Promise.all(urls.map(function(u){
  return fetch(u,{cache:'reload',credentials:'same-origin'}).then(function(r){if(!r.ok)return;
    return (html?clean(r):Promise.resolve(r)).then(function(x){return c.put(keyFn?keyFn(u):u,x);});}).catch(function(){});}));});}

self.addEventListener('install',function(e){
  e.waitUntil(caches.open(SHELL).then(function(c){return c.addAll(SHELL_URLS.map(function(u){return new Request(u,{cache:'reload'});}));})
    .then(function(){return Promise.all([getInto(SHELL,OPTIONAL_SHELL),getInto(SHELL,CORE_PAGES,pageKey,true),
      getInto(DATA,DATA_URLS),getInto(ASSETS,ASSET_URLS)]);})
    .then(function(){return self.skipWaiting();}));
});
self.addEventListener('activate',function(e){
  var keep={};DATA_URLS.forEach(function(u){keep[new URL(u,self.location.origin).href]=1;});
  e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k.indexOf('rcm-drugs-shell-')===0&&k!==SHELL;})
      .map(function(k){return caches.delete(k);}));})
    .then(function(){return caches.open(DATA).then(function(c){return c.keys().then(function(ks){   // drop data files from older versions
      return Promise.all(ks.filter(function(r){return /[?&]v=/.test(r.url)&&!keep[r.url];}).map(function(r){return c.delete(r);}));});});})
    .then(function(){return self.clients.claim();}));
});

function keep(e,p){try{e.waitUntil(p);}catch(x){}return p;}   // Safari: never throw if the event already settled
function offline(){return caches.match(pageKey('/drugs/offline')).then(function(h){return h||new Response(
  '<!DOCTYPE html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Offline</title>'
  +'<p style="font-family:sans-serif;padding:24px">You are offline, and this page has not been saved on this device. <a href="/drugs/">Drug Index</a></p>',
  {status:503,headers:{'Content-Type':'text/html; charset=utf-8'}});});}
function store(key,res){                 // refresh the copy wherever it lives; new pages go to the rolling cache
  return caches.open(SHELL).then(function(s){return s.match(key).then(function(h){if(h)return s.put(key,res);
    return caches.open(SAVED).then(function(sv){return sv.match(key).then(function(h2){if(h2)return sv.put(key,res);
      return caches.open(PAGES).then(function(p){return p.put(key,res).then(function(){return trim(PAGES,MAX_PAGES);});});});});});});}
/* A saved page keeps the layout file names it was saved with, and the offline manifest only notices content
   changes. Point every saved copy at the current drugdb.<hash>.css/js (and drop the rolled-back foldable
   viewport-fit) as it is served, so no device keeps an old layout (Nov 23 2026). */
function fresh(hit){
  if(!hit||(hit.headers.get('content-type')||'').indexOf('text/html')<0)return Promise.resolve(hit);
  return hit.clone().text().then(function(t){
    var u=t.replace(/\/drugs\/drugdb\.[0-9a-f]{6,}\.css/g,SHELL_URLS[0]).replace(/\/drugs\/drugdb\.[0-9a-f]{6,}\.js/g,SHELL_URLS[1])
           .replace(/,\s*viewport-fit=cover/g,'');
    if(u===t)return hit;
    var h=new Headers(hit.headers);h.delete('content-length');
    return new Response(u,{status:hit.status,statusText:hit.statusText,headers:h});
  },function(){return hit;});
}
function nav(e){
  var key=pageKey(e.request.url);
  var net=fetch(e.request.url,{credentials:'same-origin'}).then(function(res){
    return clean(res).then(function(cr){
      if(res.ok&&(res.headers.get('content-type')||'').indexOf('text/html')>=0)keep(e,store(key,cr.clone()));
      return cr;});});
  return caches.match(key).then(fresh).then(function(hit){
    if(!hit)return net.catch(offline);
    keep(e,net.catch(function(){}));
    var slow=new Promise(function(r){setTimeout(function(){r(hit);},3500);});   // weak signal: show the saved copy
    return Promise.race([net.then(function(r){return r.ok?r:hit;},function(){return hit;}),slow]);
  });
}
function swr(e,name,max){var r=e.request;return caches.open(name).then(function(c){return c.match(r).then(function(h){return h||caches.match(r);}).then(function(hit){
  var net=fetch(r).then(function(res){if(res.ok){c.put(r,res.clone());if(max)trim(name,max);}return res;});
  if(hit){keep(e,net.catch(function(){}));return hit;}
  return net.catch(function(){return Response.error();});});});}
function cacheFirst(r){return caches.match(r).then(function(hit){return hit||fetch(r).then(function(res){
  if(res.ok){var c=res.clone();caches.open(SHELL).then(function(s){s.put(r,c);});}return res;},
  function(){return caches.match(r,{ignoreSearch:true}).then(function(h){return h||anyVersion(r);});});});}   // offline: any saved version
function anyVersion(r){   // drugdb.<hash>.css/js: serve whichever version this device has saved
  var m=new URL(r.url).pathname.match(/^\/drugs\/drugdb\.[^./]+\.(css|js)$/);if(!m)return Response.error();
  return caches.keys().then(function(ns){return Promise.all(ns.map(function(n){return caches.open(n).then(function(c){return c.keys();});}));})
    .then(function(all){var hit=null;all.forEach(function(ks){ks.forEach(function(k){var p=new URL(k.url).pathname;
      if(new RegExp('^/drugs/drugdb(\\.[^./]+)?\\.'+m[1]+'$').test(p))hit=k;});});return hit?caches.match(hit):Response.error();});}
function networkFirst(e,name){var r=e.request;return fetch(r).then(function(res){
  if(res.ok){var c=res.clone();keep(e,caches.open(name).then(function(ca){return ca.put(r,c);}));}return res;},
  function(){return caches.match(r).then(function(h){return h||Response.error();});});}

self.addEventListener('fetch',function(e){
  var r=e.request;if(r.method!=='GET')return;
  var u=new URL(r.url);
  if(r.mode==='navigate'){if(u.origin===self.location.origin&&u.pathname.indexOf('/drugs/')===0)e.respondWith(nav(e));return;}
  if(u.origin===self.location.origin){
    if(u.pathname==='/drugs/offline-manifest.json'||u.pathname==='/drugs/interactions.json'||u.pathname==='/drugs/med-scheduler.json')return e.respondWith(networkFirst(e,DATA));   // must match the current page logic
    if(u.pathname.indexOf('/drugs/')===0&&/\.json$/.test(u.pathname))return e.respondWith(swr(e,DATA,0));
    if(u.pathname.indexOf('/data/drugs/supplements/')===0&&/\.json$/.test(u.pathname))return e.respondWith(swr(e,DATA,0));
    if(/[?&]v=/.test(u.search)||/^\/drugs\/drugdb\.[^./]+\.(css|js)$/.test(u.pathname))return e.respondWith(cacheFirst(r));
    if(/^\/(assets|images|brand)\//.test(u.pathname)||/\.(png|ico|svg|webp|jpe?g|webmanifest)$/.test(u.pathname))
      return e.respondWith(swr(e,ASSETS,MAX_ASSETS));
    return;
  }
  if(u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com')e.respondWith(swr(e,ASSETS,MAX_ASSETS));
});
"""


def supp_asset_version() -> str:
    m = re.search(r'^SUPP_ASSET_VERSION = "([^"]+)"', (REPO / "generate_supplement_pages.py").read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else ""


def build_sw() -> str:
    sv = supp_asset_version()
    da = drugdb_assets()
    shell = [da["css_url"], da["js_url"]]
    optional = ["/assets/drug-hero.js?v=3"] + ([f"/drugs/supplements/supp.css?v={sv}", f"/drugs/supplements/supp.js?v={sv}"] if sv else [])
    data = ["/drugs/search-index.json", "/drugs/search-extra.json", "/drugs/supplements/search-index.json", "/drugs/interactions.json", "/drugs/med-scheduler.json",
            f"/drugs/browse.json?v={ASSET_VERSION}", f"/drugs/browse-brands.json?v={ASSET_VERSION}"]
    assets = ["/assets/share-buttons.js", "/drugs/app.webmanifest", "/images/app/dosis-192.png", "/favicon.ico",
              "/favicon-32x32.png", "/images/app/dosis-180.png"]
    js = (SW_JS.replace("__SHELL__", json.dumps(shell)).replace("__OPTIONAL__", json.dumps(optional))
          .replace("__DATA__", json.dumps(data)).replace("__ASSETS__", json.dumps(assets)))
    v = hashlib.sha1((js + offline_page()).encode("utf-8")).hexdigest()[:10]   # new offline page -> new worker
    return js.replace("__V__", v)



def offline_manifest(out_dir: Path) -> dict:
    """Everything the app downloads for offline use: every drug page (variant spellings included), the drug-class
    pages, the supplement and medical-nutrition pages, and the supplement data the brand viewer reads.
    Rows: [path, content hash, bytes]. Updates and resumed downloads fetch only rows whose hash changed."""
    rows = []

    def add(path: str, f: Path):
        with open(f, "rb") as fh:
            raw = fh.read()
        m = _HASH_RE.search(raw[:4096].decode("utf-8", "ignore")) if f.suffix == ".html" else None
        rows.append([path, (m.group(1) if m else hashlib.sha1(raw).hexdigest())[:10], len(raw)])

    for f in sorted(out_dir.glob("*.html")):
        if f.stem not in ("index", "offline"):
            add(f"/drugs/{f.stem}", f)
    for sub in ("category", "supplements"):
        for f in sorted((out_dir / sub).glob("*.html")):
            add(f"/drugs/{sub}/" if f.stem == "index" else f"/drugs/{sub}/{f.stem}", f)
    for dj in ("interactions.json", "med-scheduler.json"):
        if (out_dir / dj).exists():
            add(f"/drugs/{dj}", out_dir / dj)
    sdata = REPO / "data" / "drugs" / "supplements"
    for f in sorted(sdata.glob("*.json")):
        if not f.name.startswith("_"):
            add(f"/data/drugs/supplements/{f.name}", f)
    h = hashlib.sha1(json.dumps(rows, separators=(",", ":")).encode("utf-8")).hexdigest()[:12]
    return {"v": 3, "h": h, "pages": rows}


def offline_sizes(man: dict) -> dict:
    """Rounded sizes for the index panel (stored size, and download size at ~25% after compression)."""
    rows = man.get("pages", [])
    b = sum(r[2] for r in rows)
    return {"n": len(rows), "drugs": sum(1 for r in rows if r[0].count("/") == 2),
            "store": max(5, int(round(b / 1e6 / 5.0)) * 5), "dl": max(5, int(round(b * 0.25 / 1e6 / 5.0)) * 5)}

def offline_page() -> str:
    canonical = f"{SITE}/drugs/offline"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebPage", "@id": canonical, "url": canonical,
                         "name": "Offline · Drug Index", "inLanguage": "en"})
    return (head("Offline · Drug Index · Renal Care Matters", "This page is not saved on this device yet.", canonical, jsonld,
                 "__HASH__", robots="noindex, nofollow")
            + '<body class="physician-mode single-mode">\n' + header(True) + """
<section class="hero"><div class="container dd-hero-wide"><div class="hero-grid"><div class="hero-copy">
<div class="hero-tag">Drug Index · Offline</div>
<h1>You are offline</h1>
<p class="hero-sub">This page has not been saved on this device yet. Pages you have opened before, and any you downloaded for offline use,
are listed below.</p>
</div></div></div></section>
<main class="container dd-wide">
<p><button type="button" class="dd-btn" onclick="location.reload()">Try again</button>
<a class="dd-btn dd-btn-ghost" href="/drugs/">Drug Index</a></p>
<h2 class="dd-off-h">Saved on this device</h2>
<p class="dd-note" id="dd-off-n">Checking saved pages&hellip;</p>
<ul class="dd-list" id="dd-off-list"></ul>
</main>
<script>
(function(){var L=document.getElementById('dd-off-list'),N=document.getElementById('dd-off-n');
if(!('caches' in window)){N.textContent='This browser does not keep pages for offline use.';return;}
var seen={},items=[],names={};
fetch('/drugs/search-index.json').then(function(r){return r.json();}).then(function(d){d.forEach(function(e){names[e.s]=e.n;});},function(){})
.then(function(){return Promise.all(['rcm-drugs-saved','rcm-drugs-pages'].map(function(n){return caches.open(n).then(function(c){return c.keys();});}));}).then(function(all){
  var dl=all[0].length,app=(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true,
      ios=/iphone|ipad|ipod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  all.forEach(function(ks){ks.forEach(function(r){var p=new URL(r.url).pathname,m=p.match(/^\\/drugs\\/(?:supplements\\/)?([a-z0-9][a-z0-9-]*)$/);
    if(!m||seen[p]||m[1]==='offline'||m[1]==='view'||m[1]==='index')return;seen[p]=1;
    var t=(!/supplements/.test(p)&&names[m[1]])||m[1].replace(/-/g,' ');items.push({p:p,t:t.charAt(0).toUpperCase()+t.slice(1),s:p.indexOf('/supplements/')>0});});});
  items.sort(function(a,b){return a.t.localeCompare(b.t);});
  N.textContent=items.length?items.length+' page'+(items.length===1?'':'s')+' available offline.':'No drug pages are saved yet. Open the Drug Index while online to save pages as you browse.';
  if(!dl){var w=document.createElement('p');w.className='dd-app-warn';
    w.innerHTML='<strong>No downloads in '+(app?'this app':'this browser')+' yet.</strong> '+(ios&&app
      ?'On iPhone and iPad, the Home Screen app keeps its own storage: pages downloaded in a Safari tab do not carry over. Connect to the internet, open Dosis from your Home Screen, go to <strong>Dosis: use the Drug Index as an app</strong> and tap <strong>Download the complete Drug Index</strong>.'
      :'Connect to the internet, open the Drug Index and tap <strong>Download the complete Drug Index</strong> under <strong>Dosis: use the Drug Index as an app</strong>.');
    N.parentNode.insertBefore(w,N);}
  items.forEach(function(it){var li=document.createElement('li'),a=document.createElement('a');a.href=it.p;a.textContent=it.t+(it.s?' (supplement)':'');li.appendChild(a);L.appendChild(li);});
}).catch(function(){N.textContent='Could not read saved pages.';});})();
</script>
""" + FOOTER + FLOAT.replace('<script src="/assets/share-buttons.js" defer></script>\n', ''))


EXT_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'


# ═════════════════════════════════════════════════════════════════════════════
# Drug page sections
# ═════════════════════════════════════════════════════════════════════════════
def product_sort_key(p):
    b = ws(p.get("brand_name")).lower()
    return (b == "", b, ws(p.get("dosage_strength_form")).lower(), ws(p.get("registration_number")))


def render_products(slug, g, products, today, also: str = "") -> str:
    rows, classes = [], {}
    for p in sorted(products, key=product_sort_key):
        c = classify(p)
        classes[c] = classes.get(c, 0) + 1
        exp = parse_date(p.get("expiry_date"))
        past = bool(exp and exp < today)
        brand = ws(p.get("brand_name")) or "(no brand name)"
        reg_name = ws(p.get("generic_name"))
        var_slug = p.get("_variant_of_main")
        mfr = ws(p.get("manufacturer"))
        country = ws(p.get("country_of_origin"))
        dist_bits = []
        if ws(p.get("distributor")):
            dist_bits.append(esc(ws(p["distributor"])))
        for role in ("importer", "trader"):
            v = ws(p.get(role))
            if v and v != ws(p.get("distributor")):
                dist_bits.append(f'<span class="dd-sub">{role.capitalize()}: {esc(v)}</span>')
        pis = [x for x in (p.get("pi_links") or []) if isinstance(x, dict) and safe_url(x.get("file_link"))]
        pi_html = "<br>".join(
            f'<a href="{esc(x["file_link"])}" rel="noopener nofollow" target="_blank">{esc(x.get("version") or "Package insert")}</a>'
            for x in pis)
        vat = '<span class="dd-sub">VAT-exempt</span>' if p.get("vat_exempt") else ""
        rows.append(
            f'<tr data-class="{esc(c)}" data-past="{1 if past else 0}">'
            f'<td data-label="Brand"><div><span class="dd-brand">{esc(brand)}</span>'
            + (f'<span class="dd-sub">{esc(reg_name)}</span>' if reg_name else "")
            + (f'<span class="dd-sub">{esc(ws(p["brand_note"]))}</span>' if ws(p.get("brand_note")) else "")
            + (f'<span class="dd-varnote"><a href="{esc(var_slug)}.html" title="Registered under the variant spelling {esc(reg_name or var_slug)}">Variant spelling</a></span>'
               if var_slug else "") + "</div></td>"
            f'<td data-label="Strength &amp; form"><div>{esc(ws(p.get("dosage_strength_form")))}'
            + (f'<span class="dd-sub">{esc(ws(p.get("packaging")))}</span>' if ws(p.get("packaging")) else "") + "</div></td>"
            f'<td data-label="Dispensing" data-sort="{esc(c)}"><div><span class="dd-tag {esc(c) if c in CLASS_LABEL else ""}" '
            f'title="{esc(ws(p.get("classification")))}">{esc(c or "—")}</span>{vat}</div></td>'
            f'<td data-label="Manufacturer"><div>{esc(mfr) or "—"}' + (f'<span class="dd-sub">{esc(country)}</span>' if country else "") + "</div></td>"
            f'<td data-label="Distributor"><div>{"".join(dist_bits) or "—"}</div></td>'
            f'<td data-label="Reg. no." class="dd-reg"><div>{esc(ws(p.get("registration_number")))}</div></td>'
            f'<td data-label="Valid until" data-sort="{exp.isoformat() if exp else ""}"><div>{esc(us_date_str(p.get("expiry_date"), True)) or "—"}'
            + ('<span class="dd-sub dd-past">Past listed date</span>' if past else "") + "</div></td>"
            f'<td data-label="Package insert"><div>{pi_html}</div></td></tr>')
    opts = "".join(f'<option value="{esc(c)}">{esc(CLASS_LABEL.get(c, c))} ({n})</option>'
                   for c, n in sorted(classes.items(), key=lambda kv: -kv[1]) if c)
    n = len(products)
    heads = ["Brand", "Strength &amp; form", "Dispensing", "Manufacturer / country", "Distributor", "Reg. no.", "Valid until", "Package insert"]
    th = "".join(f'<th scope="col"><button type="button">{h}</button></th>' if h != "Package insert"
                 else f'<th scope="col"><span style="display:block;padding:10px 12px">{h}</span></th>' for h in heads)
    return f"""
<section class="section" id="products">
<div class="section-tag">Philippine products</div>
<h2>Registered products in the Philippines</h2>
<p class="dd-lead">{n:,} product{'s' if n != 1 else ''} registered with the Food and Drug Administration (FDA) Philippines list
{esc(g['name'])} as the generic name{" (including products registered under a variant spelling)" if also else ""}. Registration status changes; confirm a product's current status on the FDA portal before relying on it.</p>
{also}
<p><a class="dd-btn" href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">Verify on PH FDA portal {EXT_ICON}</a></p>
{'<details class="dd-prod-acc" id="dd-prod-acc"><summary><span>All registered products<span class="dd-prod-acc-n">' + f"{n:,}" + '</span></span></summary>' if n > 2 else ''}
<div class="dd-toolbar no-print" role="search">
<label class="dd-hidden" for="dd-q">Filter products</label>
<input id="dd-q" type="search" placeholder="Filter by brand, strength, manufacturer, or registration no." autocomplete="off">
{f'<label class="dd-hidden" for="dd-class">Dispensing category</label><select id="dd-class"><option value="">All dispensing categories</option>{opts}</select>' if len(classes) > 1 else ''}
<label class="dd-hidden" for="dd-sort">Sort products</label>
<select id="dd-sort" class="dd-sort-sel"><option value="0:1">Sort: brand A–Z</option><option value="0:-1">Sort: brand Z–A</option>
<option value="6:-1">Sort: validity, latest first</option><option value="6:1">Sort: validity, earliest first</option>
<option value="3:1">Sort: manufacturer A–Z</option><option value="5:1">Sort: registration no.</option></select>
<label class="dd-check"><input id="dd-past" type="checkbox"> Hide registrations past their listed validity date</label>
<span class="dd-count" id="dd-count" aria-live="polite">{n:,} products</span>
</div>
<div class="dd-table-wrap">
<table class="dd-table" id="dd-products">
<caption class="dd-hidden">Philippine FDA-registered products for {esc(g['name'])}</caption>
<thead><tr>{th}</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
<div class="dd-empty" id="dd-empty" hidden>No products match these filters.</div>
</div>
{'</details>' if n > 2 else ''}
<p class="dd-note" style="margin-top:10px">Source: FDA Philippines product registration database. "Valid until" is the registration validity date
listed by the FDA; a past date may mean a renewal is pending. Package insert links point to files published by the FDA.</p>
</section>
"""


KIDNEY_ICON = ('<svg class="dd-kidney-ico" viewBox="0 0 24 24" aria-hidden="true">'  # pair of kidneys (Nov 17 2026: old glyph read as a stone)
               '<path d="M7 3C4.2 3 2 6.6 2 11.5S4.4 21 7.4 21c2.2 0 3.6-1.6 3.1-3.6-.4-1.7-1.9-2.8-1.9-4.9s1.5-3.2 1.9-4.9C11 5.3 9.4 3 7 3z"/><path d="M17 3c2.8 0 5 3.6 5 8.5S19.6 21 16.6 21c-2.2 0-3.6-1.6-3.1-3.6.4-1.7 1.9-2.8 1.9-4.9s-1.5-3.2-1.9-4.9C13 5.3 14.6 3 17 3z"/></svg>')
RENAL_KW = re.compile(r"renal|kidney|creatinine clearance|\bCrCl\b|\beGFR\b|\bGFR\b|dialys|hemodial|haemodial|ESRD|ESKD|nephro", re.I)


def renal_approved(renal) -> bool:
    return isinstance(renal, dict) and ws(renal.get("review_status")).lower() == "approved"


def label_renal_excerpt(label) -> tuple[str, str]:
    """Verbatim renal text from the US label: renal_impairment, else the renal parts of dosage_and_administration.
    Returns (html, which-section)."""
    if not isinstance(label, dict):
        return "", ""
    if isinstance(label.get("labels"), list) and label["labels"]:
        label = label["labels"][0]
    secs = label_sections(label)
    for k in ("renal_impairment", "use_in_renal_impairment"):
        if secs.get(k):
            body = render_label_value(secs[k])
            if body:
                return body, "Renal impairment"
    da = secs.get("dosage_and_administration") or secs.get("dosage")
    if not da:
        return "", ""
    if isinstance(da, dict):
        da = da.get("text") or re.sub(r"<[^>]+>", " ", da.get("html") or "")
    texts = da if isinstance(da, list) else [da]
    picked = []
    for t in texts:
        for para in re.split(r"\n\s*\n|\n", str(t)):
            para = para.strip()
            if not para or not RENAL_KW.search(para):
                continue
            if len(para) > 700:   # long run-on openFDA text: keep only the renal sentences, verbatim
                sents = [x for x in re.split(r"(?<=[.;])\s+(?=[A-Z0-9])", para) if RENAL_KW.search(x)]
                picked.extend(sents)
            else:
                picked.append(para)
    if not picked:
        return "", ""
    return "".join(f"<p>{esc(x)}</p>" for x in picked), "Dosage and administration (renal excerpts)"


def kidney_chip(renal) -> str:
    """Hero chip text, from APPROVED guidance only (explicit field; never inferred)."""
    if not renal_approved(renal):
        return ""
    return ws(renal.get("chip") or renal.get("kidney_status") or renal.get("summary_chip"))


def _entries(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _linkify_source(src: str) -> str:
    """'Title; https://url' → escaped title with the URL as a link."""
    m = re.search(r"(https?://\S+)\s*$", src)
    if not m:
        return esc(src)
    title = src[:m.start()].rstrip(" ;,")
    return f'{esc(title)}; <a href="{esc(m.group(1))}" rel="noopener" target="_blank">{esc(m.group(1))}</a>'


def render_price_block(slug, g, ctx: Ctx) -> str:
    parts = []
    # Government price references (DOH DPRI, PhilHealth GAMOT fixed fees) — not retail prices
    pe = [e for e in _entries(ctx.prices.get(slug)) if isinstance(e, dict)]
    if pe:
        TYPES = {"dpri_range": "DPRI procurement range", "dpri_reference": "DPRI reference price",
                 "philhealth_gamot_fixed_fee": "PhilHealth GAMOT fixed fee"}
        trs, srcs = [], {}
        for e in sorted(pe, key=lambda e: (ws(e.get("price_type")), _num(ws(e.get("dosage_form_strength"))), ws(e.get("dosage_form_strength")))):
            lo, hi = e.get("price_low", e.get("price")), e.get("price_high", e.get("price_low", e.get("price")))
            price = peso(lo) if lo == hi or hi is None else f"{peso(lo)}–{peso(hi)}"
            ref = e.get("reference_price")
            src = ws(e.get("source"))
            if src:
                srcs.setdefault(src, us_date_str(e.get("source_date") or e.get("as_of")))
            trs.append(f'<tr><td>{esc(e.get("dosage_form_strength") or e.get("product") or e.get("description") or "")}</td>'
                       f'<td>{esc(price)}{"<span class=dd-sub>Reference " + esc(peso(ref)) + "</span>" if ref not in (None, "") and e.get("price_type") == "dpri_range" else ""}</td>'
                       f'<td>{esc(e.get("unit") or "")}</td><td>{esc(TYPES.get(ws(e.get("price_type")), ws(e.get("price_type"))))}</td></tr>')
        notes = []
        for e in pe:
            for n in e.get("notes") or []:
                if ws(n) and ws(n) not in notes:
                    notes.append(ws(n))
        src_html = "".join(f"<li>{_linkify_source(k)}{', as of ' + esc(v) if v else ''}</li>" for k, v in srcs.items())
        parts.append('<h3>Government price references</h3><div class="table-wrap"><table class="drug-table"><thead><tr>'
                     f'<th>Preparation</th><th>Price (PHP)</th><th>Unit</th><th>Type</th></tr></thead><tbody>{"".join(trs)}</tbody></table></div>'
                     + (f'<p class="dd-note">{esc(" ".join(notes))}</p>' if notes else "")
                     + f'<p class="dd-note">These are government procurement and reimbursement references, not retail prices. Sources:</p><ul class="dd-note dd-srclist">{src_html}</ul>')
    # Formulary (PNF / PhilHealth GAMOT)
    pnf = ctx.pnf.get(slug)
    if isinstance(pnf, dict) and (pnf.get("in_pnf") or pnf.get("listed") or pnf.get("philhealth_gamot") is not None):
        rows, srcs = [], {}
        if pnf.get("in_pnf") or pnf.get("listed"):
            names = "; ".join(map(ws, pnf.get("pnf_names") or []))
            rows.append(f"<tr><td>Philippine National Formulary</td><td>Listed{' as ' + esc(names) if names else ''}</td></tr>")
        for e in pnf.get("pnf_entries") or []:
            if not isinstance(e, dict):
                continue
            notes = "; ".join(map(ws, e.get("restriction_notes") or []))
            rows.append(f'<tr><td>PNF listing</td><td>{esc(e.get("dosage_form_strength"))}'
                        + (f'<span class="dd-sub">Restrictions: {esc(notes)}</span>' if notes else "") + "</td></tr>")
            if ws(e.get("source")):
                srcs.setdefault(ws(e["source"]), us_date_str(e.get("source_date")))
        if pnf.get("philhealth_gamot") is not None:
            g_ = "Yes" if pnf["philhealth_gamot"] else "No"
            if pnf.get("philhealth_gamot") and pnf.get("gamot_listed_since"):
                g_ += f" (listed since {us_date_str(pnf['gamot_listed_since'])})"
            rows.append(f"<tr><td>PhilHealth GAMOT</td><td>{esc(g_)}</td></tr>")
            if ws(pnf.get("gamot_source")):
                srcs.setdefault(ws(pnf["gamot_source"]), "")
        if pnf.get("konsulta_yakap"):
            rows.append("<tr><td>PhilHealth YAKAP (formerly Konsulta)</td><td>Yes</td></tr>")
        src_html = "".join(f"<li>{_linkify_source(k)}{', as of ' + esc(v) if v else ''}</li>" for k, v in srcs.items())
        parts.append('<h3>Formulary and coverage</h3>'
                     f'<div class="table-wrap"><table class="drug-table"><tbody>{"".join(rows)}</tbody></table></div>'
                     + (f'<p class="dd-note">Sources:</p><ul class="dd-note dd-srclist">{src_html}</ul>' if src_html else ""))
    # Retail checks + pharmacy deep links
    re_rows = [e for e in _entries(ctx.retail.get(slug)) if isinstance(e, dict)]
    if re_rows:
        trs = "".join(
            f'<tr><td>{esc(e.get("chain"))}</td><td>{esc(e.get("product"))}</td><td>{esc(peso(e.get("price")))}</td>'
            f'<td>{esc(e.get("unit") or "")}</td><td>{esc(us_date_str(e.get("checked_date"), True))}</td>'
            f'<td>{f"<a href={chr(34)}{esc(safe_url(e.get(chr(117)+chr(114)+chr(108))))}{chr(34)} rel={chr(34)}noopener nofollow{chr(34)} target=_blank>View</a>" if safe_url(e.get("url")) else ""}</td></tr>'
            for e in re_rows)
        parts.append('<h3>Prices seen at pharmacy chains</h3><div class="table-wrap"><table class="drug-table"><thead><tr><th>Chain</th>'
                     f'<th>Product</th><th>Price</th><th>Unit</th><th>Checked</th><th>Link</th></tr></thead><tbody>{trs}</tbody></table></div>')
    if ctx.pharmacies:
        from urllib.parse import quote
        q = quote(g["name"].split(" + ")[0] if len(g["name"]) > 60 else g["name"], safe="")
        btns = []
        for x in ctx.pharmacies:
            nm, lt, tpl = ws(x.get("name") or x.get("id")), x["link_type"], x["search_url_template"]
            if lt == "search":
                url, lab = tpl.replace("{q}", q), f"Search {nm}"
            elif lt == "store_locator":
                url, lab = tpl, f"{nm} branches"
            else:
                url, lab = tpl, nm
            btns.append(f'<a class="dd-btn dd-btn-ghost" href="{esc(url)}" rel="noopener nofollow" target="_blank">{esc(lab)} {EXT_ICON}</a>')
        parts.append(f'<h3>Check availability</h3><div class="dd-pharm">{"".join(btns)}</div>')
    if not parts:
        return ""
    if re_rows or ctx.pharmacies:
        parts.append('<p class="dd-note">Prices and stock vary by branch; renalcarematters.com does not sell medicines or receive '
                     'payment from pharmacies.</p>')
    return ('<section class="section" id="price">\n<div class="section-tag">Price &amp; availability</div>\n'
            '<h2>Price, formulary, and availability</h2>\n' + "\n".join(parts) + "\n</section>\n")


# ═════════════════════════════════════════════════════════════════════════════
# "At a glance" card (class, indications, mechanism, PH availability, formulary)
# ═════════════════════════════════════════════════════════════════════════════
_ACRONYM = re.compile(r"^[A-Z0-9][A-Z0-9-]*[A-Z0-9]$|[a-z][A-Z]|^[A-Z]{2,}")


def sentence_case(t: str) -> str:
    """Lowercase ordinary words, keep acronyms/mixed-case tokens (ACE, HMG-CoA, NSAID), capitalize the first letter."""
    words = ws(t).split(" ")
    out = []
    for w in words:
        core = re.sub(r"[^A-Za-z0-9-]", "", w)
        out.append(w if (core and _ACRONYM.search(core)) else w.lower())
    r = " ".join(out)
    return r[:1].upper() + r[1:] if r else r


def ph_categories(products, g) -> list[str]:
    """PH FDA pharmacologic categories, de-duplicated case-insensitively, collapsed to the most specific variant,
    most frequent first, sentence case."""
    counts: dict[str, int] = {}
    shown: dict[str, str] = {}
    for c in [p.get("pharmacologic_category") for p in products] or (g.get("categories") or []):
        c = ws(c).rstrip(" .;")
        if not c:
            continue
        k = re.sub(r"[^a-z0-9]+", " ", c.lower()).strip()
        k = " ".join(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in k.split())
        counts[k] = counts.get(k, 0) + 1
        shown.setdefault(k, c)
    keys = sorted(counts, key=lambda k: (-counts[k], k))
    kept: list[str] = []
    for k in keys:
        if any(o != k and o.startswith(k) for o in counts):      # a more specific variant exists
            continue
        kept.append(k)
    # fold counts of generic prefixes into their specific variant for ordering
    score = {k: counts[k] + sum(counts[o] for o in counts if o != k and k.startswith(o)) for k in kept}
    kept.sort(key=lambda k: (-score[k], k))
    return [sentence_case(shown[k]) for k in kept]


def us_classes(label) -> dict:
    if not isinstance(label, dict):
        return {}
    lm = label.get("label") if isinstance(label.get("label"), dict) else {}
    of = label.get("openfda") if isinstance(label.get("openfda"), dict) else {}
    out = {}
    for k in ("epc", "moa", "pe", "cs"):
        v = lm.get(f"pharm_class_{k}") or of.get(f"pharm_class_{k}") or []
        v = [re.sub(r"\s*\[(EPC|MoA|PE|CS|Chemical/Ingredient)\]\s*$", "", ws(x)) for x in (v if isinstance(v, list) else [v])]
        v = list(dict.fromkeys(x for x in v if x))
        if v:
            out[k] = v
    return out


_SECT_HEAD = re.compile(r"^\s*\d+(\.\d+)?\s+(INDICATIONS\s*(AND|&)\s*USAGE|MECHANISM OF ACTION|Mechanism of Action)\s*", re.I)
_SENT_END = re.compile(r"(?<!\be\.g)(?<!\bi\.e)(?<!\bvs)(?<![A-Z])\.\s+(?=[A-Z(•])")


def _first_sentence(t: str, limit=240) -> str:
    t = ws(t)
    m = _SENT_END.search(t)
    if m:
        t = t[:m.start() + 1]
    if len(t) > limit:
        t = t[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return t


def _section_text(label, keys) -> str:
    if not isinstance(label, dict):
        return ""
    secs = label_sections(label)
    for k in keys:
        v = secs.get(k)
        if isinstance(v, list):
            v = "\n\n".join(map(str, v))
        if isinstance(v, dict):
            v = v.get("text") or re.sub(r"<[^>]+>", " ", v.get("html") or "")
        if v and ws(v):
            return str(v)
    return ""


def indication_items(label) -> list[str]:
    """Compact, verbatim-derived list of indications from indications_and_usage."""
    raw = _section_text(label, ("indications_and_usage", "indications"))
    if not raw:
        return []
    t = _SECT_HEAD.sub("", ws(raw))
    t = re.split(r"\bLimitations? of Use\b", t)[0]
    items: list[str] = []

    def add(x):
        x = ws(x).strip(" •o:;,-")
        x = re.sub(r"^(o|•)\s+", "", x)
        if len(x) < 3:
            return
        x = _first_sentence(x, 220)
        if x.lower() not in {i.lower() for i in items}:
            items.append(x)

    # (a) Highlights style: "... ( 1.1 )" markers
    marks = list(re.finditer(r"\(\s*1(?:\.\d+)?\s*\)", t))
    if marks:
        prev = 0
        for m in marks:
            seg = t[prev:m.start()]
            prev = m.end()
            if "•" in seg:
                seg = seg.rsplit("•", 1)[1]
            elif ":" in seg[:200] and re.search(r"indicated[^:]{0,80}:", seg):
                seg = re.split(r"indicated[^:]{0,80}:", seg, maxsplit=1)[1]
            add(seg)
        if items:
            return items[:8]
    # (b) bullet list
    if "•" in t:
        for seg in t.split("•")[1:]:
            seg = re.split(r"\s\d\.\d+\s+[A-Z]", seg)[0]        # stop at the next numbered subsection
            seg = re.sub(r"\s+o\s+", "; ", seg)
            add(seg)
        if items:
            return items[:8]
    # (c) numbered subsections "1.1 Hypertension ..."
    for m in re.finditer(r"(?:^|\s)1\.(\d+)\s+((?:[A-Z][\w'’/-]*|of|and|in|with|the|for|or|to|\([^)]{1,40}\))(?:\s+(?:[A-Z][\w'’/-]*|of|and|in|with|the|for|or|to|\([^)]{1,40}\))){0,8})", t):
        head = re.sub(r"\s+[A-Z]{3,}\b.*$", "", m.group(2))      # cut at an ALL-CAPS brand name
        add(head)
    if items:
        return items[:8]
    # (d) "indicated for: The management of … The management of …" (repeated lead phrase)
    m = re.search(r"indicated[^:]{0,80}:\s*", t)
    if m:
        after = t[m.end():]
        lead = " ".join(after.split()[:3])
        if lead and after.count(lead) >= 2:
            for seg in after.split(lead)[1:]:
                add(lead + seg)
            if items:
                return items[:8]
    # (e) first sentence of the section
    add(t)
    return items[:1]


def mechanism_text(label) -> str:
    raw = _section_text(label, ("mechanism_of_action",))
    if not raw:
        return ""
    t = _SECT_HEAD.sub("", ws(raw.split("\n\n")[0]))
    t = re.sub(r"^\s*12\.1\s+Mechanism of Action\s*", "", t, flags=re.I)
    sents, rest = [], t
    for _ in range(2):
        m = _SENT_END.search(rest)
        if not m:
            sents.append(rest)
            break
        sents.append(rest[:m.start() + 1])
        rest = rest[m.end():]
    out = " ".join(x.strip() for x in sents if x.strip())
    return out if len(out) <= 520 else out[:520].rsplit(" ", 1)[0] + "…"


_UNIT = r"(?:mg|mcg|µg|μg|g|kg|mL|ml|L|IU|I\.U\.|units?|U|%|mmol|mEq|mOsm|million|billion|CFU|ppm)"
_STRENGTH = re.compile(r"\d[\d.,]*\s*" + _UNIT + r"\b(?:\s*(?:/|per)\s*(?:\d[\d.,]*\s*)?(?:" + _UNIT + r"|tablet|capsule|dose|actuation|spray|drop|sachet|vial|ampule|kg|hr|h|24 hours)\b)?", re.I)
_FORM_FIX = {"tab": "tablet", "tabs": "tablet", "cap": "capsule", "caps": "capsule"}


def _norm_form(form: str) -> str:
    k = ws(form.lower())
    k = re.sub(r"\b(film|enteric|sugar)\s*-?\s*coated\b", r"\1-coated", k)
    k = re.sub(r"\b(extended|sustained|prolonged|modified|delayed|controlled)\s*-?\s*release[ds]?\b", r"\1-release", k)
    k = re.sub(r"\borally\s+disintegrating\b", "orally disintegrating", k)
    k = re.sub(r"\btab[a-z]{0,4}\b", "tablet", k)          # tab, tabs, tablets, tabelt, tabler
    k = re.sub(r"\bcaps?\b|\bcapsules\b", "capsule", k)
    k = re.sub(r"\b(capsule|sachet|vial|ampule|ampoule|suppositor(?:y|ies)|patch|lozenge|granule)s\b", r"\1", k)
    return _FORM_FIX.get(k, k)


def _norm_strength(s: str) -> str:
    s = re.sub(r"(\d)\s*(?=[A-Za-zµμ%])", r"\1 ", ws(s))
    s = re.sub(r"\s*/\s*", "/", s)
    s = re.sub(r"\bml\b", "mL", s)
    return s


def _num(s):
    m = re.search(r"\d[\d.,]*", s)
    try:
        return float(m.group(0).replace(",", "")) if m else 0.0
    except ValueError:
        return 0.0


def available_forms(products) -> list[tuple[str, list[str], int]]:
    """[(form, [strengths], n_products)] from dosage_strength_form, most common form first."""
    forms: dict[str, dict] = {}
    for p in products:
        dsf = ws(p.get("dosage_strength_form"))
        if not dsf:
            continue
        ms = list(_STRENGTH.finditer(dsf))
        if ms:
            strength = dsf[ms[0].start():ms[-1].end()]
            form = dsf[ms[-1].end():]
            if not ws(form):
                form = dsf[:ms[0].start()]
        else:
            strength, form = "", dsf
        form = ws(re.sub(r"^[\s,/+-]+|[\s.,;]+$", "", form))
        form = re.sub(r"\(.*?\)", "", form).strip()
        if not form or len(form) > 60 or re.search(r"\d", form):
            continue
        key = _norm_form(form)
        f = forms.setdefault(key, {"label": sentence_case(key), "strengths": {}, "n": 0})
        f["n"] += 1
        if strength:
            st = _norm_strength(strength)
            f["strengths"].setdefault(st.lower(), st)
    out = []
    for key, f in sorted(forms.items(), key=lambda kv: (-kv[1]["n"], kv[0])):
        sts = sorted(f["strengths"].values(), key=lambda x: (_num(x), x))
        out.append((f["label"], sts, f["n"]))
    return out


def _price_range(entries, kind) -> str:
    rows = [e for e in entries if isinstance(e, dict) and ws(e.get("price_type")).startswith(kind)
            and isinstance(e.get("price_low"), (int, float))]
    if not rows:
        return ""
    by_unit: dict[str, list] = {}
    for e in rows:
        by_unit.setdefault(ws(e.get("unit")) or "per unit", []).append(e)
    unit, rs = max(by_unit.items(), key=lambda kv: len(kv[1]))
    lo = min(e["price_low"] for e in rs)
    hi = max(e.get("price_high") if isinstance(e.get("price_high"), (int, float)) else e["price_low"] for e in rs)
    rng = peso(lo) if lo == hi else f"{peso(lo)}–{peso(hi)}"
    return f"{rng} {unit}"


def summary_approved(summ) -> bool:
    return isinstance(summ, dict) and ws(summ.get("review_status")).lower() == "approved"


DISCLAIMER = """
<section class="section" id="disclaimer">
<div class="disclaimer" role="note"><strong>For health professionals.</strong> This page is a reference compiled from public
regulatory sources for licensed health professionals in the Philippines. Verify every product detail against the current
Philippine package insert and the FDA Philippines registration record. Information here is not a substitute for clinical
judgment and does not replace the prescribing information approved for the specific product you dispense or prescribe.
<br><br>Last updated: <time datetime="__ISO__">__DATE__</time>.</div>
</section>
"""


def render_brand_line(brands: list[str], shown: int = 3) -> str:
    """Philippine brand names under the generic name, collapsed by default (Dr. Rivero, Nov 17 2026):
    the summary shows the count and the first few brands; expanding lists every brand."""
    if not brands:
        return '<p class="dd-brands"><strong>Brands:</strong> none registered under a distinct brand name (generic name only).</p>'
    link = lambda b: f'<a class="dd-brand-link" href="#products" data-brand="{esc(b)}">{esc(b)}</a>'
    preview = ", ".join(esc(b) for b in brands[:shown]) + ("…" if len(brands) > shown else "")
    n = len(brands)
    return (f'<details class="dd-brands dd-brands-acc"><summary><strong>Brands ({n:,})</strong>'
            f'<span class="dd-brands-preview"> {preview}</span><span class="dd-brands-hint">Show all</span></summary>'
            f'<div class="dd-brands-all">{" · ".join(link(b) for b in brands)}</div></details>')


# ═════════════════════════════════════════════════════════════════════════════
# Monograph layout (Lexi-style section ORDER only; all content from US labels, PH registry,
# PNF/DPRI and our approved JSON — no third-party compendium text)
# ═════════════════════════════════════════════════════════════════════════════
SEVERITY_SCALE = {  # our own interaction severity scale (see DRUGDB-CONTRACT.md)
    "avoid": ("Avoid", "dd-sev-avoid"),
    "adjust or monitor": ("Adjust or monitor", "dd-sev-adjust"),
    "adjust": ("Adjust or monitor", "dd-sev-adjust"),
    "monitor": ("Adjust or monitor", "dd-sev-adjust"),
    "minor": ("Minor", "dd-sev-minor"),
}
LABEL_CHIP = '<span class="dd-src">US FDA label</span>'
OURS_CHIP = '<span class="dd-src dd-src-ours">renalcarematters.com, reviewed</span>'


def _lab(label):
    if isinstance(label, dict) and isinstance(label.get("labels"), list) and label["labels"]:
        return label["labels"][0]
    return label if isinstance(label, dict) else None


def label_html(label, *keys) -> str:
    """Rendered verbatim label text for the first non-empty key; *_table keys are sanitized HTML."""
    lab = _lab(label)
    if not lab:
        return ""
    secs = label_sections(lab)
    for k in keys:
        v = secs.get(k)
        if not v:
            continue
        if k.endswith("_table"):
            vv = v if isinstance(v, list) else [v]
            h = "".join(sanitize_html(str(x)) for x in vv if str(x).strip())
            if h:
                return f'<div class="dd-tables">{h}</div>'
            continue
        h = render_label_value(v)
        if h:
            return h
    return ""


def acc(title: str, body: str, open_=False, src=LABEL_CHIP, aid="") -> str:
    if not body:
        return ""
    return (f'<details class="dd-acc"{f" id={chr(34)}{aid}{chr(34)}" if aid else ""}{" open" if open_ else ""}>'
            f'<summary><span>{esc(title)} {src}</span></summary><div class="dd-acc-body">{body}</div></details>')


def _subsections(text: str, num: str, head_re: str) -> list[str]:
    """Verbatim 'N.x Heading …' chunks whose heading matches head_re."""
    heads = list(re.finditer(r"(?:^|\s)(" + num + r"\.\d+)\s+(?=[A-Z])", text or ""))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        chunk = text[h.start(1):end].strip()
        if re.match(num + r"\.\d+\s+[^.]{0,90}?(" + head_re + r")", chunk, re.I):
            out.append(chunk)
    return out


def hepatic_text(label) -> str:
    lab = _lab(label)
    if not lab:
        return ""
    secs = label_sections(lab)
    if secs.get("hepatic_impairment"):
        return render_label_value(secs["hepatic_impairment"])
    pop = ws(secs.get("use_in_specific_populations") if isinstance(secs.get("use_in_specific_populations"), str) else "")
    found = []
    m = re.search(r"(?:^|\s)(8\.\d+)\s+(?:Patients\s+with\s+)?(?:Hepatic\s+Impairment|Hepatic\s+Insufficiency|Impaired\s+Hepatic)", pop)
    if m:
        nxt = re.search(r"\s8\.\d+\s+[A-Z]|\s10\s+OVERDOSAGE", pop[m.end():])
        found.append(pop[m.start(1):m.end() + nxt.start() if nxt else len(pop)].strip())
    da = secs.get("dosage_and_administration")
    found += _subsections(da if isinstance(da, str) else "", "2", r"\bHepatic\b|\bLiver\b")
    return "".join(f"<p>{esc(x)}</p>" for x in found)


def administration_text(label) -> str:
    lab = _lab(label)
    if not lab:
        return ""
    da = label_sections(lab).get("dosage_and_administration")
    chunks = _subsections(da if isinstance(da, str) else "", "2",
                          r"Administration|Preparation|Reconstitution|Dilution|Infusion|Instructions for Use|Compatib")
    return "".join(f"<p>{esc(x)}</p>" for x in chunks)


def _sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.;])\s+(?=[A-Z(\[])", ws(text)) if x.strip()]


def pick_sentences(label, keys, pattern, limit=8) -> list[str]:
    lab = _lab(label)
    if not lab:
        return []
    secs, out = label_sections(lab), []
    rx = re.compile(pattern, re.I)
    for k in keys:
        v = secs.get(k)
        if isinstance(v, list):
            v = " ".join(map(str, v))
        if not isinstance(v, str):
            continue
        for snt in _sentences(v):
            if rx.search(snt) and 20 < len(snt) < 600 and snt not in out:
                out.append(snt)
                if len(out) >= limit:
                    return out
    return out


CYP_RE = r"\bCYP\s?\d[A-Z]?\d*|P-gp\b|P-glycoprotein|\bOATP\d|\bBCRP\b|\bOCT\d\b|\bMATE\d?|\bUGT\d|\bOAT\d\b"
PK_RE = r"half[-\u2010\u2011\u2012\u2013\s]?life|\bt\s?½|\bt1/2\b|excreted|excretion|eliminated in (the )?urine|renal clearance|urinary"


LEVELS = {"none": ("No change", "dd-lv-none"), "adjust": ("Adjust / caution", "dd-lv-adjust"),
          "avoid": ("Avoid", "dd-lv-avoid"), "nodata": ("No data", "dd-lv-nodata")}


def _kval(v) -> tuple[str, str, str]:
    """(full text, short, level) from a plain string/bool/list or a {text, short, level} object."""
    if isinstance(v, dict):
        t = v.get("text") or v.get("recommendation") or ""
        return (ws(t) if not isinstance(t, list) else "; ".join(map(ws, t)), ws(v.get("short")), ws(v.get("level")).lower())
    if isinstance(v, bool):
        return ("Yes" if v else "No", "", "")
    if isinstance(v, list):
        return ("; ".join(map(ws, v)), "", "")
    return (ws(v), "", "")


def _band_label(rng: str) -> str:
    rng = ws(rng)
    if rng and not re.search(r"egfr|crcl|gfr|clearance|dialys|crrt|hd\b|pd\b", rng, re.I):
        rng = f"eGFR {rng}"
    return rng


def kidney_block(renal: dict, pfx: str, children: bool = False) -> str:
    """Compact kidney dosing: a color-coded strip (only from approved short/level fields) with the full text
    in an expander, or, without short/level, a dense two-column grid of the full text."""
    tiles = []   # (key, tile label, row label, full, short, level)
    for i, b in enumerate(renal.get("bands") or []):
        if isinstance(b, dict) and (b.get("range") or b.get("recommendation") or b.get("text")):
            full, short, lvl = _kval(b)
            rl = _band_label(b.get("range"))
            # keep the measure the source uses (CrCl stays CrCl; never relabel Cockcroft-Gault CrCl as eGFR)
            m = re.match(r"^\s*(eGFR/CrCl|eGFR|CrCl)\s*", rl, flags=re.I)
            meas = m.group(1) if m else "eGFR"
            tl = re.sub(r"^\s*(eGFR/CrCl|eGFR|CrCl)\s*", "", rl, flags=re.I) or rl
            tl = f"{meas} " + tl if tl and tl[0] in "<>≥≤0123456789" else tl
            tiles.append((f"{pfx}-b{i}", tl, rl, full, short, lvl))
    for k, tl, rl in (("hd", "HD", "Hemodialysis (intermittent)"), ("pd", "PD", "Peritoneal dialysis"),
                      ("crrt", "CRRT", "CRRT"), ("pirrt", "PIRRT", "PIRRT / SLED")):
        if renal.get(k) not in (None, "", []):
            full, short, lvl = _kval(renal[k])
            if full or short:
                tiles.append((f"{pfx}-{k}", tl, rl, full, short, lvl))
    foot = []
    for k, lab in (("dialyzable", "Dialyzable?"), ("monitoring", "Monitoring")):
        if renal.get(k) not in (None, "", []):
            foot.append(f'<li><strong>{lab}</strong> {esc(_kval(renal[k])[0])}</li>')
    foot_html = f'<ul class="dd-kfoot">{"".join(foot)}</ul>' if foot else ""
    grid = ('<dl class="dd-kgrid">' + "".join(f'<div class="dd-kcell" id="{key}"><dt>{esc(rl)}</dt><dd>{esc(full)}</dd></div>'
                                             for key, tl, rl, full, short, lvl in tiles) + "</dl>") if tiles else ""
    has_strip = any(short and lvl in LEVELS for *_, short, lvl in tiles)
    if not has_strip:
        return grid + foot_html
    strip = []
    for key, tl, rl, full, short, lvl in tiles:
        if lvl == "hide":   # band not applicable to this drug: no tile; full text stays in the details grid
            continue
        lab, cls = LEVELS.get(lvl, LEVELS["nodata"])
        sh = short[:40] if short else "See details"
        strip.append(f'<a class="dd-ktile {cls}" href="#{key}" data-open="{pfx}-full"><span class="dd-kt-h">{esc(tl)}</span>'
                     f'<span class="dd-kt-s">{esc(sh)}</span><span class="dd-kt-l">{lab}</span></a>')
    return (f'<div class="dd-kstrip" role="list" aria-label="{"Children: " if children else ""}kidney dosing summary">'
            + "".join(f'<div role="listitem">{x}</div>' for x in strip) + "</div>"
            + f'<details class="dd-acc dd-kfull" id="{pfx}-full"><summary><span>Show full dosing details</span></summary>'
            + f'<div class="dd-acc-body">{grid}</div></details>' + foot_html)


def _intl_date(v) -> str:
    """'2025-01-29' -> 'January 29, 2025'; '2025-03' -> 'March 2025'; '2004' -> '2004'."""
    v = ws(v)
    if re.fullmatch(r"\d{4}-\d{2}", v):
        return dt.date.fromisoformat(v + "-01").strftime("%B %Y")
    return us_date_str(v) if v else ""


def intl_source(label, intl) -> dict:
    """Source metadata of a non-US regulator document, used only when the generic has no US label."""
    if _lab(label) or not isinstance(intl, dict) or not isinstance(intl.get("source"), dict):
        return {}
    src = intl["source"]
    agency = ws(src.get("agency_short")) or ws(src.get("agency"))
    return {"agency": agency, "agency_full": ws(src.get("agency")) or agency, "document": ws(src.get("document")),
            "url": safe_url(src.get("url")), "date": _intl_date(src.get("version_date"))} if agency else {}


def intl_attrib_line(isrc: dict) -> str:
    if not isrc:
        return ""
    return (f'<p class="dd-note dd-intl-src"><strong>Source:</strong> {esc(isrc["agency"])} product information'
            + (f' ({esc(isrc["date"])})' if isrc["date"] else "") + ". This generic has no US FDA label.</p>")


def render_kidney_section(label, renal, intl=None, eu=None) -> str:
    """'Dosing: Altered kidney function' — approved renalcarematters.com guidance, else verbatim label text."""
    head_ = ('<section class="dd-kidney dd-sec" id="kidney-dosing" aria-labelledby="kidney-h">\n'
             f'<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">CKD · dialysis · CRRT</div>'
             '<h2 id="kidney-h">Dosing: Altered kidney function</h2></div></div>\n')
    if renal_approved(renal):
        out = [head_]
        if renal.get("summary"):
            out.append(f'<p class="dd-kidney-sum">{esc(renal["summary"])}</p>')
        if ws(renal.get("kidney_function_basis")):   # which measure the bands use (CrCl vs eGFR), shown above the strip
            out.append(f'<p class="dd-note dd-kbasis"><strong>Kidney function measure:</strong> '
                       f'{esc(renal["kidney_function_basis"])}</p>')
        out.append(kidney_block(renal, "kd"))
        ped = renal.get("pediatric") if isinstance(renal.get("pediatric"), dict) else {}
        if ped.get("renal") or any(ped.get(k) for k in ("hd", "pd", "crrt", "pirrt")):
            out.append('<details class="dd-acc dd-kchildren"><summary><span>Children (kidney dosing)</span></summary>'
                       '<div class="dd-acc-body">' + kidney_block(dict(ped, bands=ped.get("renal") or []), "kdc", children=True)
                       + '<p class="dd-note">Pediatric eGFR: bedside Schwartz equation, 0.413 &times; height (cm) / serum creatinine '
                       '(mg/dL). Weight-based doses should not exceed the adult maximum.</p></div></details>')
        by, on = ws(renal.get("reviewed_by")), us_date_str(renal.get("reviewed_date") or renal.get("reviewed_on"))
        out.append('<p class="dd-note">renalcarematters.com guidance' + (f", reviewed by {esc(by)}" if by else "")
                   + (f" on {esc(on)}" if on else "") + '. Sources are listed under <a href="#references">References</a>. '
                   "Use with the product's package insert and the patient's current kidney function.</p>")
        out.append(intl_attrib_line(intl_source(label, intl)))
        rb, which = label_renal_excerpt(label)
        if rb:
            out.append(acc(f"US label text: {which}", rb))
        elif eu and not _lab(label) and eu_r.renal_html(eu):
            out.append(f'<details class="dd-acc"><summary><span>EU SmPC text: renal impairment {eu_r.EU_CHIP}</span></summary>'
                       f'<div class="dd-acc-body">{eu_r.renal_html(eu)}</div></details>')
        return "\n".join(out) + "\n</section>\n"
    body, which = label_renal_excerpt(label)
    out = [head_]
    if body:
        lab = _lab(label)
        srcs = [ws(r.get("source")) for r in (lab.get("renal_impairment_sources") or []) if isinstance(r, dict)]
        if which == "Renal impairment" and srcs:
            which = "Renal impairment (" + ", ".join(dict.fromkeys(x.replace("_", " ") for x in srcs if x)) + ")"
        out.append(f'<div class="dd-kidney-label"><div class="dd-kidney-src">From the US FDA label · {esc(which)}</div>{body}</div>')
    elif eu and not _lab(label) and eu_r.renal_html(eu):
        out.append(f'<div class="dd-kidney-label">{eu_r.renal_html(eu)}</div><p class="dd-note dd-intl-src">Source: '
                   f'{eu_r.attribution_text(eu)}, reproduced with acknowledgment of the source (verbatim). '
                   'This generic has no US FDA label.</p>')
    elif eu and not _lab(label):
        out.append('<p class="dd-note">The EU SmPC (EMA) for this generic has no separate kidney-specific text. See '
                   '<a href="#smpc-4-2">SmPC 4.2</a> and <a href="#smpc-5-2">5.2</a> below, and the Philippine package insert.</p>')
    else:
        out.append('<p class="dd-note">No kidney-specific text is available from the US label for this generic yet. '
                   'Check the Philippine package insert in the products table.</p>')
    out.append('<p class="dd-kidney-pending">Kidney-specific guidance from renalcarematters.com: in preparation.</p>')
    return "\n".join(out) + "\n</section>\n"


CLINICAL_ORDER = [
    "component-info",
    "use", "contraindications",
    "dosing-adult", "kidney-dosing", "kidney-injury", "pn-kidney-notes", "dosing-hepatic", "dosing-pediatric", "dosing-older",
    "administration", "dosage-forms",
    "warnings", "interactions", "adverse-reactions", "monitoring",
    "pregnancy", "breastfeeding", "overdose",
    "mechanism", "pharmacodynamics", "pharmacokinetics",
    "formulary", "related-guides", "references",
]


def sec(sid: str, title: str, body: str, nav: str = "") -> tuple[str, str, str] | None:
    if not body or not body.strip():
        return None
    return (sid, nav or title, f'<section class="dd-sec" id="{sid}" aria-labelledby="{sid}-h">'
                               f'<h2 id="{sid}-h">{esc(title)}</h2>{body}</section>')


CALC_ICON = ('<svg class="dd-rc-ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="2.5" width="14" height="19" rx="2.5"/>'
             '<rect x="8" y="5.5" width="8" height="3.5" rx=".8"/><path d="M8.5 12.5h.01M12 12.5h.01M15.5 12.5h.01M8.5 15.5h.01M12 15.5h.01'
             'M15.5 15.5h.01M8.5 18.5h.01M12 18.5h.01M15.5 18.5h.01"/></svg>')


def related_guides_html(picks, rg: dict, limit: int = 4, calcs=None, what: str = "this medicine") -> str:
    """Cards for renalcarematters.com guides that discuss this drug, then related calculators
    (data/drugs/related_guides.json: "drugs"/"guides" from the guide scan; "drug_calculators"/"calculators" from
    tools/drugdb/related_calculators.json)."""
    gm = (rg or {}).get("guides") or {}
    cm = (rg or {}).get("calculators") or {}
    lis = []
    for f, _score in (picks or [])[:limit]:
        m = gm.get(f)
        if not m:
            continue
        img = (f'<img src="{esc(m["img"])}" alt="" loading="lazy" decoding="async" width="72" height="72">' if m.get("img") else "")
        desc = ('<span class="dd-rg-d">' + esc(m["d"]) + "</span>") if m.get("d") else ""
        lis.append(f'<li><a href="{esc(m["url"])}">{img}<span><span class="dd-rg-k">Guide</span><span class="dd-rg-t">{esc(m["t"])}</span>{desc}</span></a></li>')
    cls = []
    for f in (calcs or [])[:3]:
        m = cm.get(f)
        if not m:
            continue
        desc = ('<span class="dd-rg-d">' + esc(m["d"]) + "</span>") if m.get("d") else ""
        cls.append(f'<li><a class="dd-rc" href="{esc(m["url"])}">{CALC_ICON}<span><span class="dd-rg-k">Calculator</span>'
                   f'<span class="dd-rg-t">{esc(m["t"])}</span>{desc}</span></a></li>')
    if not lis and not cls:
        return ""
    lead = ("Guides and calculators on renalcarematters.com" if lis and cls else
            "Guides on renalcarematters.com" if lis else "Calculators on renalcarematters.com")
    return (f'<p class="dd-note">{lead} for {esc(what)}, for patients and clinicians.</p>'
            f'<ul class="dd-rg">{"".join(lis + cls)}</ul>')


def related_title(picks, calcs, limit: int = 4) -> tuple[str, str]:
    """Section title and TOC label: "Related guides", "Related calculators" or "Related guides & calculators"."""
    g, c = bool((picks or [])[:limit]), bool(calcs)
    t = "Related guides & calculators" if g and c else "Related calculators" if c else "Related guides"
    return t, t


def references_html(slug, label, renal, summ, ctx: Ctx, intl=None, pn_notes_=None) -> str:
    items = []
    lab = _lab(label)
    if lab:
        m = label_meta(lab)
        items.append(f'U.S. Food and Drug Administration. {esc(m["title"] or "Prescribing information")}'
                     f' [US FDA-approved label{", version " + esc(m["version"]) if m["version"] else ""}'
                     f'{", " + esc(m["date"]) if m["date"] else ""}]. Via {esc(m["via"])}.'
                     + (f' <a href="{esc(m["url"])}" rel="noopener" target="_blank">{esc(m["url"])}</a>' if m["url"] else ""))
    for alt in alternate_labels(label):
        m = label_meta(alt)
        items.append(f'U.S. Food and Drug Administration. {esc(m["title"] or "Prescribing information")}'
                     f' [US FDA-approved label{", version " + esc(m["version"]) if m["version"] else ""}'
                     f'{", " + esc(m["date"]) if m["date"] else ""}]. Via {esc(m["via"])}.'
                     + (f' <a href="{esc(m["url"])}" rel="noopener" target="_blank">{esc(m["url"])}</a>' if m["url"] else ""))
    eu = ctx.eu(slug) if not lab else None
    if eu:
        items.append(eu_r.reference(eu))
    isrc = intl_source(label, intl)
    if isrc and (renal_approved(renal) or summary_approved(summ)):
        items.append(f'{esc(isrc["agency_full"])}. {esc(isrc["document"] or "Product information")}'
                     f' [{esc(isrc["agency"])} product information{", " + esc(isrc["date"]) if isrc["date"] else ""}; no US FDA label].'
                     + (f' <a href="{esc(isrc["url"])}" rel="noopener" target="_blank">{esc(isrc["url"])}</a>' if isrc["url"] else ""))
    items.append(f'Food and Drug Administration Philippines. Verification portal (product registrations). '
                 f'<a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">{FDA_VERIFY_URL}</a>')
    seen = set()
    pnf = ctx.pnf.get(slug)
    if isinstance(pnf, dict):
        for e in pnf.get("pnf_entries") or []:
            if isinstance(e, dict) and ws(e.get("source")) and ws(e["source"]) not in seen:
                seen.add(ws(e["source"]))
                items.append(_linkify_source(ws(e["source"])))
        if ws(pnf.get("gamot_source")) and ws(pnf["gamot_source"]) not in seen:
            seen.add(ws(pnf["gamot_source"]))
            items.append(_linkify_source(ws(pnf["gamot_source"])))
    for e in _entries(ctx.prices.get(slug)):
        if isinstance(e, dict) and ws(e.get("source")) and ws(e["source"]) not in seen:
            seen.add(ws(e["source"]))
            items.append(_linkify_source(ws(e["source"])))

    def ours(srcs):
        for r in srcs or []:
            if isinstance(r, dict):
                doi, url = ws(r.get("doi")), safe_url(r.get("url"))
                link = f"https://doi.org/{doi}" if doi else url
                t = esc(r.get("citation") or r.get("title") or "")
                if t or link:
                    items.append(t + (f' <a href="{esc(link)}" rel="noopener" target="_blank">{esc(link)}</a>' if link else ""))
            elif ws(r):
                items.append(esc(r))
    reviewed = []
    if renal_approved(renal):
        ped = renal.get("pediatric") if isinstance(renal.get("pediatric"), dict) else {}
        ours(list(renal.get("sources") or renal.get("references") or []) + [x for x in (ped.get("sources") or [])
                                                                            if x not in (renal.get("sources") or [])])
        by, on = ws(renal.get("reviewed_by")), us_date_str(renal.get("reviewed_date"))
        reviewed.append(f'Kidney and pediatric dosing{": reviewed by " + esc(by) if by else ""}{" on " + esc(on) if on else ""}.')
    if summary_approved(summ):
        ours(summ.get("sources"))
        by, on = ws(summ.get("reviewed_by")), us_date_str(summ.get("reviewed_date"))
        parts = [w for k, w in (("usual_adult_dose", "dosing"), ("key_interactions", "interaction"),
                                ("adverse_effects", "adverse-effect"), ("monitoring", "monitoring")) if summ.get(k)]
        what = (", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else (parts[0] if parts else "clinical"))
        reviewed.append(f'{what[:1].upper() + what[1:]} summary{": reviewed by " + esc(by) if by else ""}'
                        f'{" on " + esc(on) if on else ""}.')
    for n in pn_notes_ or []:
        ours(n.get("sources"))
        by, on = ws(n.get("reviewed_by")), us_date_str(n.get("reviewed_date"))
        reviewed.append(f'Parenteral nutrition kidney notes ({esc(n.get("brand"))}){": reviewed by " + esc(by) if by else ""}'
                        f'{" on " + esc(on) if on else ""}.')
    out = '<ol class="dd-refs">' + "".join(f"<li>{x}</li>" for x in dict.fromkeys(items)) + "</ol>"
    if reviewed:
        out += '<p class="dd-note"><strong>renalcarematters.com content:</strong> ' + " ".join(reviewed) + "</p>"
    else:
        out += ('<p class="dd-note">This page shows official label and registry text only; no renalcarematters.com '
                'clinical summary has been approved for it yet.</p>')
    out += ('<div class="disclaimer" role="note"><strong>For health professionals.</strong> This page is a reference compiled '
            'from public regulatory sources for licensed health professionals in the Philippines. Verify every product detail '
            'against the current Philippine package insert and the FDA Philippines registration record. Information here is not '
            'a substitute for clinical judgment and does not replace the prescribing information approved for the specific '
            'product you dispense or prescribe.<br><br>Last updated: <time datetime="__ISO__">__DATE__</time>.</div>')
    return out


def controlled_kind(ci) -> str:
    """'S2' (dangerous drug) | 'CP' (controlled precursor) | '' from a controlled.json item."""
    if not isinstance(ci, dict):
        return ""
    t = (ws(ci.get("category")) + " " + ws(ci.get("schedule"))).lower()
    if "precursor" in t or "essential chemical" in t:
        return "CP"
    if "dangerous" in t or "s2" in t or "schedule" in t:
        return "S2"
    return ""


def dispensing_chips(classes: set, ci, ctx: "Ctx") -> tuple[str, str]:
    """(chips html, notes html) for the hero: Rx / OTC / HR for every category present, plus S2 / precursor."""
    chips = []
    for c, lab, cls in (("Rx", "Rx · Prescription drug", "dd-rx"), ("OTC", "OTC · Over-the-counter", "dd-otc"),
                        ("HR", "HR · Household remedy", "dd-hr")):
        if c in classes:
            chips.append(f'<span class="dd-chip {cls}">{lab}</span>')
    kind = controlled_kind(ci)
    note = ""
    if kind:
        srcs = []
        for sid in ci.get("source_ids") or []:
            x = ctx.controlled_sources.get(ws(sid))
            if x:
                t, u = ws(x.get("title") or x.get("name") or sid), safe_url(x.get("url"))
                srcs.append(f'<a href="{esc(u)}" rel="noopener" target="_blank">{esc(t)}</a>' if u else esc(t))
        tip = "; ".join(x for x in (ws(ci.get("schedule")), ws(ci.get("rx_form")), ws(ci.get("notes"))) if x)
        if kind == "S2":
            chips.insert(0, f'<span class="dd-chip dd-s2" title="{esc(tip)}">S2 · Dangerous drug — PDEA S2 license required; see prescription rules below</span>')
        else:
            chips.insert(0, f'<span class="dd-chip dd-cp" title="{esc(tip)}">Controlled precursor</span>')
        if tip or srcs:
            note = (f'<p class="dd-dispnote">{esc(tip)}' + (f'{" " if tip else ""}Source: {"; ".join(srcs)}.' if srcs else "") + "</p>")
    return "".join(chips), note


def syn_ingredients(slug: str, g: dict, ctx: Ctx) -> list[str]:
    """Ingredient names used for synonym lookup; a high-confidence variant spelling uses its main page's
    (e.g. "Hyoscine (as butylbromide)" takes hyoscine butylbromide's names, not scopolamine's)."""
    a = ctx.aliases.get(slug)
    src = ctx.generics.get(a["main"], g) if a and a["high"] else g
    return [ws(i) for i in (src.get("ingredients") or []) if ws(i)]


def index_entry(slug: str, g: dict, ctx: Ctx, label=None, renal=None) -> tuple[dict, dict]:
    """(core search record, extra record with manufacturers and registration numbers)."""
    products = ctx.by_slug.get(slug, [])
    name = ws(g.get("name")) or slug
    if label is None:
        label = ctx.label(slug)
    if renal is None:
        renal = ctx.renal(slug)
    uc = us_classes(label)
    ph = ph_categories(products, g)
    lm = (_lab(label) or {}).get("label") if isinstance((_lab(label) or {}).get("label"), dict) else {}
    brands = brand_list(products, name)
    ub = ws(lm.get("brand_name"))
    if ub and (_brand_key(ub) in {_brand_key(b) for b in brands} or _brand_key(ub) == _brand_key(name)):
        ub = ""
    classes = {classify(p) for p in products} - {""}
    pnf = ctx.pnf.get(slug) if isinstance(ctx.pnf.get(slug), dict) else {}
    forms = sorted({form_group(f) for f, _, _ in available_forms(products)} - {""})
    inds = [re.sub(r"\s+", " ", x)[:90] for x in indication_items(label)] if label else []
    e = {"s": slug, "n": name, "c": class_group(uc, ph)}
    al = ctx.aliases.get(slug)
    if al:   # variant spelling: search results and A-Z rows point to the main molecule
        e["m"] = al["main"]
        e["mn"] = ws(ctx.generics[al["main"]].get("name")) or al["main"]
        if al["high"]:
            e["mh"] = 1
    ing = [ws(i) for i in (g.get("ingredients") or []) if ws(i)]
    if len(ing) > 1:
        e["i"] = ing
    syn = SYN.search_terms(syn_ingredients(slug, g, ctx) or [name], name)
    if syn["own"]:
        e["y"] = syn["own"]          # other nonproprietary names of this product (acetaminophen for paracetamol)
    if syn["ing"]:
        e["yi"] = syn["ing"]         # other names of its components (combinations)
    if syn["miss"]:
        e["z"] = syn["miss"]         # search-only misspellings / misnomers; never displayed
    if brands:
        e["b"] = brands
    if ub:
        e["u"] = ub
    cl = list(dict.fromkeys((uc.get("epc") or []) + (uc.get("moa") or []) + ph[:3]))
    if cl:
        e["cl"] = cl
    if inds:
        e["x"] = inds[:6]
    if forms:
        e["f"] = forms
    ck = controlled_kind(ctx.controlled(slug))
    rx = ((1 if "Rx" in classes else 0) | (2 if "OTC" in classes else 0) | (4 if "HR" in classes else 0)
          | (8 if ck == "S2" else 0) | (16 if ck == "CP" else 0))
    if rx:
        e["r"] = rx
    if pnf.get("in_pnf"):
        e["p"] = 1
    if pnf.get("philhealth_gamot") is True:
        e["h"] = 1
    if renal_approved(renal):
        e["k"] = 1
    if ctx.nx(slug):
        e["nx"] = 1
    if _lab(label):
        e["l"] = 1
    elif ctx.eu(slug):
        e["e"] = 1
    rg = sorted({ws(p.get("registration_number")) for p in products if ws(p.get("registration_number"))})
    mf, mb = company_brands(products, name, brands, rg)
    x = {"s": slug, "m": mf, "r": rg}
    if any(mb):
        x["mb"] = mb
    return e, x


COMPANY_FIELDS = ("manufacturer", "distributor", "importer")


def company_brands(products, generic_name: str, brands: list[str], regnos: list[str]) -> tuple[list[str], list[list[int]]]:
    """(companies, brand refs per company) for the Drug Index search-extra file, so a search by company name
    (manufacturer, distributor or importer) can list that company's brands under each generic.
    companies ("m"): every manufacturer, distributor and importer (case-insensitive dedupe, A-Z).
    refs ("mb"): index-aligned with companies. A ref i >= 0 points into the core record's brand list "b"
    (brand_list(): case-insensitive dedupe, most common spelling); a ref < 0 is a product with no brand (blank,
    None, Unbranded or the generic name itself), pointing at registration number r[-ref - 1] of this extra record;
    the index page shows it as "(unbranded, DRP-19166)". Integer refs keep search-extra.json small."""
    bidx = {_brand_key(b): i for i, b in enumerate(brands)}
    ridx = {r: i for i, r in enumerate(regnos)}
    names: dict[str, Counter] = {}
    refs: dict[str, set] = {}
    for p in products:
        bi = bidx.get(_brand_key(ws(p.get("brand_name"))))
        if bi is None:
            ri = ridx.get(ws(p.get("registration_number")))
            ref = None if ri is None else -ri - 1
        else:
            ref = bi
        for k in COMPANY_FIELDS:
            c = ws(p.get(k))
            if not c:
                continue
            ck = c.lower()
            names.setdefault(ck, Counter())[c] += 1
            if ref is not None:
                refs.setdefault(ck, set()).add(ref)
    keys = sorted(names, key=lambda ck: (names[ck].most_common(1)[0][0].lower(), ck))
    mf = [names[ck].most_common(1)[0][0] for ck in keys]
    # brands A-Z (their order in "b"), then unbranded registration numbers
    mb = [sorted(refs.get(ck) or (), key=lambda r: (r < 0, r if r >= 0 else -r)) for ck in keys]
    return mf, mb


FORM_GROUPS = [
    ("injection", r"inject|infusion|vial|ampul|ampoul|i\.v\.|intravenous|parenteral|for solution for|pre-?filled|syringe|lyophili"),
    ("inhalation", r"inhal|nebul|respule|aerosol|rotacap|turbuhaler|evohaler"),
    ("eye/ear/nose", r"ophth|eye|otic|ear|nasal"),
    ("topical", r"cream|ointment|gel|lotion|topical|patch|transdermal|shampoo|soap|spray|powder for topical|emulsion"),
    ("suppository", r"suppos|rectal|enema|vaginal|pessar|ovule"),
    ("oral liquid", r"syrup|suspension|solution|elixir|drops|liquid|oral emulsion|granules for|powder for oral|sachet"),
    ("capsule", r"capsule"),
    ("tablet", r"tablet|caplet|lozenge|troche"),
]


NX_ORAL = re.compile(r"oral|syrup|sachet|granule|elixir|infusion|inject|intravenous|\bi\.?v\b|for reconstitution", re.I)
NX_SYSTEMIC = {"injection", "oral liquid", "capsule", "tablet", "suppository", "other"}
NX_LOCAL = re.compile(r"vaginal|pessar|ovule|ophth|opth|ophtal|\beyes?\b|otic|\bear\b|nasal|topical|cream|ointment|\bgel\b|lotion|"
                      r"astringent|wash|gargle|mouth|shampoo|(?<!oral )\bdrops\b", re.I)


def render_nephrotox(nx: dict, ctx: "Ctx", combo: bool) -> str:
    """'Kidney injury risk' section: per tagged ingredient, mechanism, what to do, and the verbatim US label quote."""
    mechs = ctx.nephrotox.get("mechanisms") or {}
    out = []
    for ing, key, r in nx["items"]:
        ml = [m for m in r.get("mech") or [] if m in mechs]
        chips = "".join(f'<span class="dd-nx-m">{esc(mechs[m]["label"])}</span>' for m in ml)
        acts = "".join(f'<li>{esc(mechs[m]["action"])}</li>' for m in ml)
        lab = r.get("brand") or r.get("label")
        cite = (f'US label: <a href="{esc(r["url"])}" rel="noopener">{esc(lab)}</a>' if r.get("url") else f"US label: {esc(lab)}")
        cite += f' ({esc(r.get("manufacturer"))})' if r.get("manufacturer") else ""
        cite += f', {esc(r.get("section") or "")}'
        cls = ('<p class="dd-note">This drug has no US label of its own; the warning is the class statement in '
               'the US labels of this drug class.</p>') if r.get("tier") == "class" else ""
        out.append('<div class="dd-nx-item">'
                   + (f'<h3 class="dd-nx-h">{esc(ing[:1].upper() + ing[1:])}</h3>' if combo else "")
                   + f'<div class="dd-nx-ms">{chips}</div><ul class="dd-nx-do">{acts}</ul>'
                   + (f'<p class="dd-nx-note">{esc(r["note"])}</p>' if r.get("note") else "")
                   + f'<blockquote class="dd-nx-q">{esc(r.get("quote") or "")}<cite>{cite}</cite></blockquote>{cls}</div>')
    part = ('<p class="dd-note">Applies to the oral and injected products, not to products applied to the skin, eye, '
            'ear or nose.</p>') if nx.get("partial") else ""
    return ('<div class="dd-nx">' + "".join(out) + part
            + '<p class="dd-note">Kidney injury tags come from US label warnings and are reviewed by renalcarematters.com. '
              'A drug without this tag is not necessarily safe for the kidneys. Avoiding kidney toxins also protects '
              'residual kidney function in patients on dialysis. <a href="/drugs/?view=nephrotox">All drugs with a kidney '
              'injury warning</a>.</p></div>')


def form_group(form: str) -> str:
    f = form.lower()
    for name, rx in FORM_GROUPS:
        if re.search(rx, f):
            return name
    return "other"


def class_group(uc: dict, ph: list[str]) -> str:
    if uc.get("epc"):
        return sentence_case(uc["epc"][0])
    return ph[0] if ph else ""


def cat_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:80] or "other"


PK_ROWS = [("bioavailability", "Bioavailability", False), ("onset", "Onset", False), ("peak", "Time to peak", False),
           ("half_life", "Half-life", False), ("half_life_eskd", "Half-life in kidney failure (ESKD)", True),
           ("vd", "Volume of distribution", False), ("protein_binding", "Protein binding", False),
           ("metabolism", "Metabolism (CYP, transporters)", False), ("active_metabolites", "Active metabolites", False),
           ("excretion_renal_pct", "Renal excretion", True), ("dialyzability", "Dialyzability", True)]


def render_pk_table(summ) -> str:
    pk = summ.get("pk") if isinstance(summ, dict) and isinstance(summ.get("pk"), dict) else {}
    rows = []
    for k, lab, renal_row in PK_ROWS:
        v = pk.get(k)
        if v in (None, "", []):
            continue
        v = "; ".join(map(ws, v)) if isinstance(v, list) else ws(v)
        if k == "excretion_renal_pct" and re.fullmatch(r"\d+(\.\d+)?", v):
            v += "% unchanged in urine"
        rows.append(f'<tr{" class=" + chr(34) + "dd-pk-renal" + chr(34) if renal_row else ""}><th scope="row">{esc(lab)}'
                    + (' <span class="dd-pk-kid">kidney</span>' if renal_row else "") + f"</th><td>{esc(v)}</td></tr>")
    if not rows:
        return ""
    return ('<h3>Key PK parameters</h3><div class="table-wrap"><table class="drug-table dd-pk"><tbody>' + "".join(rows)
            + f"</tbody></table></div>{OURS_CHIP}")


_HEAD_WORD = (r"(?:[A-Z][\w'’/&-]*,?|\d+,?|of|and|in|with|the|for|or|to|on|by|at|a|an|during|from|into|after|before|"
              r"without|within|between|versus|vs\.?|per|via|as|than|following|including|due|associated|related|induced|"
              r"difficile[\w-]*|\([^)]{1,40}\))")


_BODY_STARTERS = {"Assess", "Discontinue", "Initiate", "Monitor", "Administer", "Take", "Obtain", "Measure",
                  "Before", "If", "The", "Do", "Avoid", "Consider", "Reduce", "Start", "Evaluate", "Instruct",
                  "Inform", "Advise", "Swallow", "Dilute", "Reconstitute", "Inspect", "Infuse", "Inject", "In"}


def split_numbered(text: str, num: str, name_words: frozenset = frozenset()) -> tuple[str, list[tuple[str, str]]]:
    """Split a run-on label section into (preamble, [(heading, verbatim chunk)]) at 'N.x Heading' markers."""
    text = ws(text)
    marks = [m for m in re.finditer(r"(?:^|\s)(" + num + r"\.\d+)\s+(?=[A-Z])", text)]
    if len(marks) < 2:
        return "", []
    pre = text[:marks[0].start()].strip()
    pre = re.sub(r"^\s*" + num + r"\s+(?:DOSAGE\s*(?:AND|&)\s*ADMINISTRATION|WARNINGS\s*(?:AND|&)\s*PRECAUTIONS|WARNINGS|"
                 r"ADVERSE\s+REACTIONS|DRUG\s+INTERACTIONS)\b\s*", "", pre)   # drop the section title only
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        chunk = text[m.start(1):end].strip()
        after = chunk[len(m.group(1)):].strip()
        hm = re.match(_HEAD_WORD + r"(?:\s+" + _HEAD_WORD + r"){0,13}", after)
        head = hm.group(0) if hm else after[:60]
        rest = after[len(head):].lstrip()
        capped = re.sub(r"\s+[A-Z]{5,}\b.*$", "", head).strip()      # an all-caps brand name starts the body
        cut_found = bool(capped) and capped != head
        head = capped or head
        words = head.split()
        if not cut_found and rest[:1].islower() and len(words) > 1:      # the last capitalized word starts the body sentence
            while len(words) > 1:
                w = words.pop()
                if w[:1].isupper():
                    break
        while len(words) > 1 and words[-1] in ("of", "and", "in", "with", "the", "for", "or", "to", "on", "by", "at", "a", "an"):
            words.pop()
        if len(words) > 1 and words[-1].lower() in {w.lower() for w in words[:-1]}:
            words.pop()
        stems: set = set()
        for i, w in enumerate(words):        # the body often starts by restating a title word or the drug name
            if i >= 2 and w[:1].isupper() and (
                    (len(w) >= 6 and w.lower()[:6] in stems) or w in _BODY_STARTERS
                    or (w.lower() in name_words and words[i - 1] not in ("of", "for", "on", "with", "to", "and", "by", "from"))
                    or w in ("Table", "Drug/Substance", "Drug/Drug")):
                words = words[:i]
                break
            stems.add(w.lower()[:6])
        while len(words) > 1 and words[-1] in ("of", "and", "in", "with", "the", "for", "or", "to", "on", "by", "at", "a", "an"):
            words.pop()
        head = tidy_label(" ".join(words).rstrip(",")) or after[:60]
        if len(head) > 90:
            head = head[:90].rsplit(" ", 1)[0] + "…"
        out.append((f"{m.group(1)} {head}", chunk))
    return pre, out


def label_split(label, keys, num, title, open_pre=True, aid="") -> str:
    """Label section as a short preamble (open) + one collapsed accordion per numbered subsection; falls back to
    a single collapsed accordion when the text has no numbered subsections."""
    lab = _lab(label)
    if not lab:
        return ""
    secs = label_sections(lab)
    for k in keys:
        v = secs.get(k)
        if isinstance(v, list):
            v = "\n\n".join(map(str, v))
        if not isinstance(v, str) or not v.strip():
            continue
        nm = " ".join(str(x) for x in ((label or {}).get("name", ""), *((label or {}).get("ingredients") or [])) if x)
        pre, subs = split_numbered(v, num, frozenset(w.lower() for w in re.findall(r"[A-Za-z]{4,}", nm)))
        if not subs:
            return acc(title, render_label_value(v), aid=aid)
        html_ = f'<div class="dd-labgroup"{f" id={chr(34)}{aid}{chr(34)}" if aid else ""}><div class="dd-labgroup-h">{esc(title)} {LABEL_CHIP}</div>'
        if pre and len(pre) > 20:
            html_ += f'<div class="dd-labpre">{highlights_html(pre if len(pre) < 1400 else pre[:1400].rsplit(" ", 1)[0] + " …")}</div>'
        html_ += "".join(f'<details class="dd-acc dd-acc-sm"><summary><span>{esc(h)}</span></summary>'
                         f'<div class="dd-acc-body">{label_paras(c)}</div></details>' for h, c in subs)
        return html_ + "</div>"
    return ""


def alternate_labels(label) -> list[dict]:
    """Secondary US labels stored by the fetcher (e.g. the IV acyclovir label beside the oral one)."""
    if not isinstance(label, dict):
        return []
    return [a for a in label.get("alternate_labels") or [] if isinstance(a, dict) and isinstance(a.get("sections"), dict)]


def alt_section_id(alt: dict, i: int) -> str:
    role = re.sub(r"[^a-z0-9]+", "-", ws(alt.get("role")).lower()).strip("-") or str(i + 1)
    return f"us-label-{role}"


def render_alternate_label(alt: dict, i: int) -> tuple[str, str, str] | None:
    """'US label: intravenous' section: verbatim text of a secondary US label, same helpers as the primary."""
    m = label_meta(alt)
    sid = alt_section_id(alt, i)
    title = ws(alt.get("heading")) or f"US label: {ws(alt.get('role')) or 'alternate'}"
    body = [f'<div class="dd-attrib"><strong>Second US label for this generic</strong>'
            + (f" ({esc(m['title'])})" if m["title"] else "")
            + (f', set ID <a href="{esc(m["url"])}" rel="noopener" target="_blank">{esc(m["set_id"])}</a>' if m["set_id"] and m["url"] else "")
            + (f", version date {esc(m['date'])}" if m["date"] else "")
            + ". Reproduced verbatim. The rest of this page quotes the primary US label.</div>"]
    body.append(acc("Indications and usage (US label)", label_html(alt, "indications_and_usage"), aid=f"{sid}-indications"))
    body.append(label_split(alt, ("dosage_and_administration",), "2", "Dosage and administration (US label)", aid=f"{sid}-dosing"))
    rb, which = label_renal_excerpt(alt)
    if rb:
        body.append(acc(f"Kidney dosing: {which} (US label)", rb, open_=True))
    body.append(acc("Dosage forms and strengths (US label)", label_html(alt, "dosage_forms_and_strengths")))
    body.append(label_split(alt, ("warnings_and_cautions", "warnings_and_precautions", "warnings", "precautions"), "5",
                            "Warnings and precautions (US label)"))
    body.append(label_split(alt, ("adverse_reactions",), "6", "Adverse reactions (US label)"))
    body.append(acc("Pediatric use (US label)", label_html(alt, "pediatric_use")))
    body.append(acc("Pharmacokinetics (US label)", label_html(alt, "pharmacokinetics")))
    html_ = "".join(x for x in body if x)
    if "dd-acc" not in html_ and "dd-labgroup" not in html_:
        return None
    return sec(sid, title, html_, title)


def alias_banner(slug: str, ctx: "Ctx") -> str:
    """Banner under the brand line of a variant-spelling page, pointing to the main molecule page."""
    a = ctx.aliases.get(slug)
    if not a:
        return ""
    m = a["main"]
    mn = ws(ctx.generics[m].get("name")) or m
    if a["high"]:
        return (f'<div class="dd-alias" role="note"><p>This entry appears to be <strong>{esc(mn)}</strong> registered under a '
                f'variant spelling.</p><a class="dd-alias-go" href="{esc(m)}.html">See the main {esc(mn)} monograph '
                '<span class="dd-alias-sub">(kidney dosing, prescribing information, all brands)</span> &rarr;</a></div>')
    return (f'<div class="dd-alias dd-alias-soft" role="note"><p>Did you mean <a href="{esc(m)}.html"><strong>{esc(mn)}</strong></a>? '
            'This generic name looks like a variant spelling of it.</p></div>')


def also_registered(slug: str, ctx: "Ctx") -> str:
    """'Also registered under: ...' line for a main page with variant spellings."""
    vs = ctx.variants_of.get(slug) or []
    if not vs:
        return ""
    def item(v):
        n = len(ctx.by_slug.get(v, []))
        reg = (ctx.generics[v].get("registered_names") or [ctx.generics[v].get("name") or v])[0]
        soft = "" if ctx.aliases[v]["high"] else ", possible match"
        return f'<a href="{esc(v)}.html">{esc(ws(reg))}</a> ({n:,} product{"s" if n != 1 else ""}{soft})'
    hi = [v for v in vs if ctx.aliases[v]["high"]]
    return (f'<p class="dd-also"><strong>Also registered under:</strong> {" · ".join(item(v) for v in vs)}'
            + ('. Products registered under these spellings are included in the table and marked.' if hi else '.') + '</p>')


def aka_line(ingredients: list[str], name: str, own: list[str] | None = None) -> tuple[str, list[str]]:
    """'Also known as: acetaminophen (US name)' under the title, plus the plain names for JSON-LD/keywords."""
    syn = SYN.display_synonyms(ingredients or [name], name, own)
    if not syn:
        return "", []
    items = [f'<strong>{esc(d["name"])}</strong> ({esc(d["label"])}{", for " + esc(d["for"]) if d["for"] else ""})' for d in syn]
    return f'<p class="dd-aka"><span>Also known as:</span> {" · ".join(items)}</p>', [d["name"] for d in syn]


FDC_CAVEAT = ("Fixed-dose combinations may not allow the dose changes advised for each component; check the strength and "
              "use the single agents if a component needs adjusting.")


def component_section(slug: str, ingredients: list[str], ctx: Ctx) -> tuple[str, int, int]:
    """'Component information' for a combination with no US/EU label of its own: per component a link to its
    single-agent page, its use (US label, else our approved summary) and, only when that component's kidney
    record is approved, its compact kidney strip. Returns (html, components linked, kidney strips shown)."""
    rows, linked, strips = [], 0, 0
    for i, ing in enumerate(ingredients):
        cs = ctx.single_slug(ing)
        if not cs or cs == slug:
            rows.append(f'<li class="dd-comp dd-comp-none"><span class="dd-comp-n">{esc(ing)}</span> '
                        '<span class="dd-sub">no separate page</span></li>')
            continue
        linked += 1
        cg = ctx.generics.get(cs, {})
        cn = ws(cg.get("name")) or cs
        cl = ctx.label(cs)
        use, src = "", ""
        inds = indication_items(cl) if _lab(cl) else []
        if inds:
            use, src = inds[0], LABEL_CHIP
        else:
            cm = ctx.summary(cs)
            d = [x for x in ((cm.get("usual_adult_dose") or []) if summary_approved(cm) else []) if isinstance(x, dict)]
            if d and ws(d[0].get("indication")):
                use, src = ws(d[0]["indication"]), OURS_CHIP
        if len(use) > 220:
            use = use[:217].rsplit(" ", 1)[0] + "…"
        body = [f'<div class="dd-comp-h"><a href="{esc(cs)}.html">{esc(cn)}</a>'
                + (f' <span class="dd-sub">listed as {esc(ing)}</span>' if SYN.norm(ing) != SYN.norm(cn) else "") + "</div>"]
        if use:
            body.append(f'<p class="dd-comp-use"><strong>Use:</strong> {esc(use)} {src}</p>')
        cr = ctx.renal(cs)
        if renal_approved(cr):
            kb = kidney_block(cr, f"kc{i}")
            if kb:
                strips += 1
                body.append(f'<div class="dd-comp-kid"><div class="dd-comp-kh">{KIDNEY_ICON}Kidney dosing: {esc(cn)} (single-agent)'
                            f'</div>{kb}<p class="dd-note">From the <a href="{esc(cs)}.html#kidney-dosing">{esc(cn)} monograph</a> '
                            f'(renalcarematters.com, reviewed).</p></div>')
        rows.append(f'<li class="dd-comp">{"".join(body)}</li>')
    if not linked:
        return "", 0, 0
    html_ = ('<p class="dd-comp-intro">No US or EU label exists for this exact combination, so information is shown for each '
             'component.</p>' + f'<ul class="dd-comp-list">{"".join(rows)}</ul>'
             + f'<p class="dd-comp-caveat" role="note"><strong>Note:</strong> {FDC_CAVEAT}</p>')
    return html_, linked, strips


def page_for(slug: str, g: dict, ctx: Ctx) -> tuple[str, dict, dict]:
    products = list(ctx.by_slug.get(slug, []))
    for v in ctx.variants_of.get(slug) or []:       # main page lists products registered under variant spellings
        if ctx.aliases[v]["high"]:
            products += [dict(p, _variant_of_main=v) for p in ctx.by_slug.get(v, [])]
    alias = ctx.aliases.get(slug)
    name = ws(g.get("name")) or slug
    label = ctx.label(slug)
    lab = _lab(label)
    renal = ctx.renal(slug)
    summ = ctx.summary(slug)
    summ_ok = summary_approved(summ)
    pnf = ctx.pnf.get(slug) if isinstance(ctx.pnf.get(slug), dict) else {}
    classes = {classify(p) for p in products} - {""}
    brands = brand_list(products, name)
    brands_ranked = brand_list(products, name, ranked=True)
    uc = us_classes(label)
    ph = ph_categories(products, g)
    cat = class_group(uc, ph)
    ingredients = [ws(i) for i in (g.get("ingredients") or []) if ws(i)]
    entry, extra = index_entry(slug, g, ctx, label, renal)
    eu = ctx.eu(slug) if not lab else None     # EU SmPC (EMA): only for generics with no US label
    aka_html, aka_names = aka_line(syn_ingredients(slug, g, ctx), name, ingredients or [name])
    comp_html, comp_n, comp_k = ("", 0, 0)
    if len(ingredients) > 1 and not lab and not eu and not (alias and alias["high"]):
        comp_html, comp_n, comp_k = component_section(slug, ingredients, ctx)
    if comp_html:
        ctx.__dict__.setdefault("comp_stats", {})[slug] = (comp_n, comp_k)

    # ── header: chips + class line + US brand note
    chips = []
    kc = kidney_chip(renal)
    if kc:
        chips.append(f'<span class="dd-chip dd-kchip">{KIDNEY_ICON}{esc(kc)}</span>')
    dchips, dnote = dispensing_chips(classes, ctx.controlled(slug), ctx)
    chips.append(dchips)
    chips.append(f'<span class="dd-chip">{len(products):,} PH product{"s" if len(products) != 1 else ""}</span>')
    if pnf.get("in_pnf"):
        chips.append('<span class="dd-chip dd-good">PNF-listed</span>')
    if pnf.get("philhealth_gamot") is True:
        chips.append('<span class="dd-chip dd-good">PhilHealth GAMOT</span>')
    vat_n = sum(1 for p in products if p.get("vat_exempt"))
    if vat_n:
        chips.append(f'<span class="dd-chip dd-good">VAT-exempt{"" if vat_n == len(products) else " (some products)"}</span>')
    if renal_approved(renal):
        chips.append(f'<a class="dd-chip dd-good" href="#kidney-dosing">{KIDNEY_ICON} Kidney dosing reviewed</a>')
    if ctx.nx(slug):
        chips.append('<a class="dd-chip dd-nxchip" href="#kidney-injury">Kidney injury risk</a>')
    chips.append(f'<button type="button" class="dd-chip dd-favbtn no-print" data-fav="{esc(slug)}" aria-pressed="false" hidden>'
                 '<span class="dd-favstar" aria-hidden="true">☆</span> Favorite</button>'
                 f'<a class="dd-chip dd-ixbtn no-print" href="/drugs/interactions.html?add={esc(slug)}">Check interactions</a>')
    if pn_notes_for(slug, ctx):
        chips.append(f'<a class="dd-chip dd-good" href="#pn-kidney-notes">{KIDNEY_ICON} PN kidney notes reviewed</a>')
    cls_line = []
    if uc.get("epc"):
        cls_line.append(f'{esc("; ".join(uc["epc"]))}{" (" + esc("; ".join(uc["moa"])) + ")" if uc.get("moa") else ""} '
                        '<span class="dd-src">US FDA class</span>')
    if ph:
        cls_line.append(f'{esc("; ".join(ph[:2]))}{"; and others" if len(ph) > 2 else ""} <span class="dd-src">PH FDA category</span>')
    if len(ingredients) > 1:
        cls_line.append("Fixed-dose combination.")
    us_brand = entry.get("u", "")

    # ── boxed warning + label attribution (top of page)
    top = []
    bw = label_html(label, "boxed_warning")
    if bw:
        top.append(f'<div class="dd-boxed-alert" role="alert" id="boxed-warning"><div class="dd-boxed-h">Boxed warning '
                   f'{LABEL_CHIP}</div><div class="dd-boxed-body">{bw}</div></div>')
    if lab:
        m = label_meta(lab)
        top.append(f'<div class="dd-attrib"><strong>Label text on this page:</strong> US FDA-approved label via {esc(m["via"])}'
                   + (f', set ID <a href="{esc(m["url"])}" rel="noopener" target="_blank">{esc(m["set_id"])}</a>' if m["set_id"] and m["url"] else "")
                   + (f", version date {esc(m['date'])}" if m["date"] else "")
                   + (f" ({esc(m['title'])})" if m["title"] else "")
                   + ". Reproduced verbatim. <strong>Philippine-approved indications and doses may differ: check the PH package insert.</strong></div>")
    elif eu:
        top.append(eu_r.attribution(eu))
    elif eu_r.has_links(ctx.intl(slug)):
        top.append(eu_r.links_html(ctx.intl(slug)))
    else:
        top.append('<div class="dd-placeholder">US label not yet available for this generic. Check the Philippine package insert '
                   '(linked in the products table where the FDA has published one).</div>')

    S = []
    # 1b. Component cross-reference (combination with no label of its own)
    if comp_html:
        S.append(sec("component-info", "Component information", comp_html, "Components"))
    # 2. Use
    inds = indication_items(label)
    use = ""
    if inds:
        use = ('<ul class="dd-uselist">' + "".join(f"<li>{esc(i)}</li>" for i in inds) + f"</ul>{LABEL_CHIP}"
               + acc("Full indications and usage", label_html(label, "indications_and_usage"), aid="label-indications-and-usage"))
    use = use or eu_r.section(eu, "4.1", open_=True)
    S.append(sec("use", "Use: Labeled indications", use, "Use"))
    # 3. Dosing: Adult
    adult = ""
    dose = [d for d in (summ.get("usual_adult_dose") if summ_ok else []) or [] if isinstance(d, dict)]
    if dose:
        adult = ('<ul class="dd-uselist">' + "".join(
            f'<li>{"<strong>" + esc(d.get("indication")) + ":</strong> " if ws(d.get("indication")) else ""}{esc(d.get("dose"))}</li>'
            for d in dose) + f"</ul>{OURS_CHIP}")
    adult += label_split(label, ("dosage_and_administration",), "2", "Dosage and administration (US label)",
                         aid="label-dosage-and-administration")
    adult += eu_r.section(eu, "4.2")
    S.append(sec("dosing-adult", "Dosing: Adult", adult, "Adult dosing"))
    # 4. Kidney
    ks = render_kidney_section(label, renal, ctx.intl(slug), eu)
    if comp_html and not renal_approved(renal):
        ks = ks.replace('<p class="dd-kidney-pending">', '<p class="dd-note">Kidney dosing for each component (single-agent) '
                        'is shown under <a href="#component-info">Component information</a>.</p>\n<p class="dd-kidney-pending">', 1)
    S.append(("kidney-dosing", "Kidney dosing", ks))
    nx = ctx.nx(slug)
    if nx:
        S.append(sec("kidney-injury", "Kidney injury risk", render_nephrotox(nx, ctx, len(ingredients) > 1)))
    # 4b. Parenteral nutrition brand kidney notes (data/drugs/pn-notes, approved only)
    pnn = pn_notes_for(slug, ctx)
    if pnn:
        S.append(("pn-kidney-notes", "PN kidney notes", render_pn_notes(pnn)))
    # 5. Hepatic
    hep = hepatic_text(label)
    S.append(sec("dosing-hepatic", "Dosing: Hepatic impairment",
                 (f"{hep}{LABEL_CHIP}" if hep else eu_r.subsection(eu, "hepatic", "Hepatic impairment")), "Hepatic"))
    # 6. Pediatric
    ped = ""
    if renal_approved(renal) and isinstance(renal.get("pediatric"), dict):
        pr = renal["pediatric"]
        rows = [(lab, _kval(pr.get(k))[0]) for k, lab in (("approved_ages", "Approved ages"), ("usual_dose", "Usual dose"),
                                                          ("max_dose", "Maximum dose"), ("neonates", "Neonates")) if pr.get(k) not in (None, "", [])]
        notes = pr.get("notes") if isinstance(pr.get("notes"), list) else ([pr["notes"]] if pr.get("notes") else [])
        if rows or notes:
            ped = ('<dl class="dd-kgrid">' + "".join(f'<div class="dd-kcell"><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for a, b in rows)
                   + "</dl>" + "".join(f'<p class="dd-note">{esc(n)}</p>' for n in notes if ws(n))
                   + '<p class="dd-note">Kidney dosing in children: see <a href="#kidney-dosing">Dosing: Altered kidney function</a>.</p>'
                   + OURS_CHIP)
    ped += acc("Pediatric use (US label)", label_html(label, "pediatric_use"), open_=not ped)
    ped += eu_r.subsection(eu, "pediatric", "Pediatric population")
    S.append(sec("dosing-pediatric", "Dosing: Pediatric", ped, "Pediatric"))
    # 7. Older adult
    S.append(sec("dosing-older", "Dosing: Older adult", acc("Geriatric use (US label)", label_html(label, "geriatric_use"), open_=True)
                 or eu_r.subsection(eu, "elderly", "Older adults"), "Older adult"))
    # 8. Dosage forms
    forms = available_forms(products)
    df = ""
    if forms:
        df += ('<h3>Philippines</h3><ul class="dd-uselist">' + "".join(
            f'<li><strong>{esc(f)}</strong>{": " + esc(", ".join(st[:10])) + (", …" if len(st) > 10 else "") if st else ""}</li>'
            for f, st, n in forms[:10]) + "</ul>"
            + (f'<p class="dd-note">and {len(forms) - 10} more forms; see the products table.</p>' if len(forms) > 10 else ""))
    df += render_products(slug, g, products, ctx.today, also_registered(slug, ctx))
    us_df = label_html(label, "dosage_forms_and_strengths")
    if us_df:
        df += "<h3>United States (label)</h3>" + acc("Dosage forms and strengths (US label)", us_df)
    S.append(sec("dosage-forms", "Dosage forms", df, "Dosage forms"))
    # 9. Administration
    adm = administration_text(label)
    S.append(sec("administration", "Administration", f"{adm}{LABEL_CHIP}" if adm else "", "Administration"))
    # 9b. Secondary US labels (e.g. "US label: intravenous" for acyclovir, whose primary label is oral)
    for i, alt in enumerate(alternate_labels(label)):
        S.append(render_alternate_label(alt, i))
    # 10. Adverse reactions
    ar = ""
    ae = summ.get("adverse_effects") if summ_ok and isinstance(summ.get("adverse_effects"), dict) else {}
    if ae.get("common") or ae.get("serious"):
        ar += ('<div class="dd-twocol">'
               + (f'<div><h3>Common</h3><ul class="dd-uselist">{"".join(f"<li>{esc(x)}</li>" for x in ae.get("common") or [])}</ul></div>' if ae.get("common") else "")
               + (f'<div><h3>Serious</h3><ul class="dd-uselist">{"".join(f"<li>{esc(x)}</li>" for x in ae.get("serious") or [])}</ul></div>' if ae.get("serious") else "")
               + f"</div>{OURS_CHIP}")
    ar += label_split(label, ("adverse_reactions",), "6", "Adverse reactions (US label)")
    ar += acc("Adverse reaction frequency tables (US label)", label_html(label, "adverse_reactions_table"))
    ar += eu_r.section(eu, "4.8")
    S.append(sec("adverse-reactions", "Adverse reactions", ar, "Adverse reactions"))
    # 11. Contraindications
    ci = ""
    if summ_ok and summ.get("contraindications"):
        ci = '<ul class="dd-uselist">' + "".join(f"<li>{esc(x)}</li>" for x in summ["contraindications"]) + f"</ul>{OURS_CHIP}"
    lci = label_html(label, "contraindications")
    ci += (acc("Contraindications (US label)", lci) if ci else (f"{lci}{LABEL_CHIP}" if lci else ""))
    ci += eu_r.section(eu, "4.3", open_=not ci)
    S.append(sec("contraindications", "Contraindications", ci, "Contraindications"))
    # 12. Warnings/Precautions
    wp = ""
    if bw:
        wp += '<p class="dd-note">The boxed warning is shown at the <a href="#boxed-warning">top of this page</a>.</p>'
    wp += label_split(label, ("warnings_and_cautions", "warnings_and_precautions", "warnings", "precautions"), "5",
                      "Warnings and precautions (US label)", aid="label-warnings-and-precautions")
    wp += eu_r.section(eu, "4.4")
    S.append(sec("warnings", "Warnings/Precautions", wp if ("dd-acc" in wp or "dd-labgroup" in wp) else "", "Warnings"))
    # 13. Interactions
    di = ""
    ki = [d for d in (summ.get("key_interactions") if summ_ok else []) or [] if isinstance(d, dict)]
    if ki:
        trs = []
        for d in ki:
            sv = SEVERITY_SCALE.get(ws(d.get("severity")).lower(), (ws(d.get("severity")) or "—", "dd-sev-minor"))
            trs.append(f'<tr><td><strong>{esc(d.get("drug_or_class"))}</strong></td><td><span class="dd-sev {sv[1]}">{esc(sv[0])}</span></td>'
                       f'<td>{esc(d.get("effect"))}</td><td>{esc(d.get("action"))}</td></tr>')
        di += ('<div class="table-wrap"><table class="drug-table dd-ix"><thead><tr><th>Drug or class</th><th>Severity</th><th>Effect</th>'
               f'<th>What to do</th></tr></thead><tbody>{"".join(trs)}</tbody></table></div>'
               '<p class="dd-note">Severity scale (renalcarematters.com): <strong>Avoid</strong>: do not combine; '
               '<strong>Adjust or monitor</strong>: change the dose or monitor closely; <strong>Minor</strong>: usually no action.</p>'
               f"{OURS_CHIP}")
    di += label_split(label, ("drug_interactions",), "7", "Drug interactions (US label)")
    di += eu_r.section(eu, "4.5")
    cyp = pick_sentences(label, ("pharmacokinetics", "drug_interactions", "clinical_pharmacology"), CYP_RE)
    if cyp:
        di += acc("Metabolism and transporters (CYP, P-gp, OATP; US label)", "".join(f"<p>{esc(x)}</p>" for x in cyp))
    S.append(sec("interactions", "Drug interactions", di if ("dd-acc" in di or "dd-labgroup" in di or ki) else "", "Interactions"))
    # 14. Pregnancy; Breastfeeding
    S.append(sec("pregnancy", "Pregnancy considerations", acc("Pregnancy (US label)", label_html(label, "pregnancy", "teratogenic_effects"), open_=True)
                 or eu_r.section(eu, "4.6"), "Pregnancy"))
    S.append(sec("breastfeeding", "Breastfeeding considerations", acc("Lactation (US label)", label_html(label, "lactation", "nursing_mothers"), open_=True)
                 or ('<p class="dd-note">Breastfeeding is covered in <a href="#smpc-4-6">SmPC 4.6 Fertility, pregnancy and lactation</a>, '
                     'under Pregnancy considerations above.</p>' if eu_r.section(eu, "4.6") else ""), "Breastfeeding"))
    # 15. Monitoring
    mon = []
    if renal_approved(renal) and ws(renal.get("monitoring")):
        mon.append(f"<li>{esc(renal['monitoring'])} <span class=\"dd-sub\">Kidney</span></li>")
    if summ_ok:
        for x in summ.get("monitoring") or []:
            if ws(x):
                mon.append(f"<li>{esc(x)}</li>")
    S.append(sec("monitoring", "Monitoring parameters", (f'<ul class="dd-uselist">{"".join(mon)}</ul>{OURS_CHIP}' if mon else ""), "Monitoring"))
    # 16. Mechanism; Pharmacokinetics
    moa = label_html(label, "mechanism_of_action")
    S.append(sec("overdose", "Overdose", eu_r.section(eu, "4.9"), "Overdose"))
    S.append(sec("mechanism", "Mechanism of action", (f"{moa}{LABEL_CHIP}" if moa else eu_r.section(eu, "5.1")), "Mechanism"))
    S.append(sec("pharmacodynamics", "Pharmacodynamics",
                 acc("Pharmacodynamics (US label)", label_html(label, "pharmacodynamics")), "Pharmacodynamics"))
    pk_full = label_html(label, "pharmacokinetics")
    pk = render_pk_table(summ) if summ_ok else ""
    hi = pick_sentences(label, ("pharmacokinetics",), PK_RE, limit=5)
    if hi:
        pk += ('<div class="dd-pk-hi"><div class="dd-kidney-src">Half-life and elimination (verbatim, US label)</div>'
               + "".join(f"<p>{esc(x)}</p>" for x in hi) + "</div>")
    pk += acc("Pharmacokinetics (US label)", pk_full)
    pk += eu_r.section(eu, "5.2")
    S.append(sec("pharmacokinetics", "Pharmacokinetics", pk, "Pharmacokinetics"))
    # 17. Formulary & pricing
    fp = render_price_block(slug, g, ctx)
    if fp:
        fp = re.sub(r'^\s*<section class="section" id="price">\s*<div class="section-tag">.*?</div>\s*<h2>.*?</h2>', "", fp, flags=re.S)
        fp = re.sub(r"</section>\s*$", "", fp.strip())
    S.append(sec("formulary", "Formulary and pricing (Philippines)", fp, "Formulary & pricing"))
    # 18. Related guides (site guides that discuss this drug); 19. References
    _rp = (ctx.related_guides.get("drugs") or {}).get(slug)
    _rc = (ctx.related_guides.get("drug_calculators") or {}).get(slug)
    _rt, _rn = related_title(_rp, _rc)
    S.append(sec("related-guides", _rt, related_guides_html(_rp, ctx.related_guides, calcs=_rc), _rn))
    S.append(sec("references", "References", references_html(slug, label, renal, summ, ctx, ctx.intl(slug), pnn), "References"))

    S = [x for x in S if x]
    # Clinical reading order (Dr. Rivero, Nov 17 2026): what it is for → who must not get it → how much (adult, then
    # kidney, liver, children, older adults) → how to give it and what is available → what to watch for → special
    # situations → background pharmacology → formulary, related reading, references.
    _rank = {sid: i for i, sid in enumerate(CLINICAL_ORDER)}
    S.sort(key=lambda x: _rank.get(x[0], len(CLINICAL_ORDER)))
    # on a combination with a component cross-reference, "Kidney dosing" in the TOC opens the per-component strips
    href = lambda sid: "component-info" if (sid == "kidney-dosing" and comp_html and not renal_approved(renal)) else sid
    toc = "".join(f'<li><a href="#{href(sid)}">{esc(nav)}</a></li>' for sid, nav, _ in S)
    pills = "".join(f'<a class="nav-pill" href="#{href(sid)}">{esc(nav)}</a>' for sid, nav, _ in S)

    # extensionless: Cloudflare Pages 308-redirects /drugs/<slug>.html to /drugs/<slug> (see patch_canonical_clean_urls.py)
    canonical = f"{SITE}/drugs/{slug}"
    # a high-confidence variant spelling consolidates to the main page (canonical + noindex; dropped from the sitemap)
    head_canon = f"{SITE}/drugs/{alias['main']}" if alias and alias["high"] else canonical
    robots = "noindex, follow" if alias and alias["high"] else "index, follow"
    rxstat = "https://schema.org/PrescriptionOnly" if classes == {"Rx"} else ("https://schema.org/OTC" if classes and "Rx" not in classes else None)
    drug = {"@type": "Drug", "@id": canonical + "#drug", "name": name, "nonProprietaryName": name, "url": canonical}
    if cat:
        drug["drugClass"] = {"@type": "DrugClass", "name": cat}
    if ingredients:
        drug["activeIngredient"] = ", ".join(ingredients)
    if rxstat:
        drug["prescriptionStatus"] = rxstat
    if brands or aka_names:
        drug["alternateName"] = list(dict.fromkeys(aka_names + brands_ranked[:25]))
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "MedicalWebPage", "@id": canonical, "url": canonical, "name": f"{name}: Philippine products and prescribing information",
         "dateModified": "__ISO__", "inLanguage": "en", "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"},
         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE,
                       "logo": {"@type": "ImageObject", "url": f"{SITE}/android-chrome-512x512.png"}},
         "about": {"@id": canonical + "#drug"}}, drug]}, ensure_ascii=False).replace("</", "<\\/")
    title = f"{name}: Philippine Brands, Dosing & Prescribing Information"
    if len(title) > 95:
        title = f"{name[:60].rstrip()}…: PH Brands & Prescribing Info"
    brand_txt = ", ".join(brands_ranked[:6]) + ("…" if len(brands) > 6 else "")
    desc = (f"{name}{' (' + cat + ')' if cat else ''}: {len(products):,} FDA Philippines-registered products"
            + (f" including {brand_txt}" if brands else "") + ". Kidney dosing, US FDA label text, PNF and price references.")
    body = (head(title, desc[:300], head_canon, jsonld, "__HASH__", keywords=", ".join(dict.fromkeys([name] + aka_names + brands_ranked[:20])), robots=robots)
            + '<body class="physician-mode single-mode dd-mono">\n' + header(False) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a>{f' › <a href="/drugs/category/{cat_slug(cat)}.html">{esc(cat)}</a>' if cat else ''}</div>
        <div class="hero-tag">Drug Database · Clinicians</div>
        <h1>{esc(name)}</h1>
        {aka_html}
        {render_brand_line(brands_ranked)}
        {alias_banner(slug, ctx)}
        {pn_partof(slug, ctx)}
        {f'<p class="dd-usbrand">US brand (reference label): <strong>{esc(us_brand)}</strong>; not a Philippine-registered brand.</p>' if us_brand else ''}
        <p class="hero-sub dd-classline">{"<br>".join(cls_line)}</p>
        <div class="dd-chips">{''.join(chips)}</div>
        {dnote}
        <div class="hero-meta">
<span><strong>Dispensing:</strong> {esc(" · ".join(CLASS_LABEL.get(c, c) for c in sorted(classes)) or "not stated")}{" · " + ("Dangerous drug (S2)" if controlled_kind(ctx.controlled(slug)) == "S2" else "Controlled precursor") if controlled_kind(ctx.controlled(slug)) else ""}</span>
<span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span>
<span><strong>Audience:</strong> Licensed health professionals</span>
</div>
      </div>
    </div>
  </div>
</section>

<nav class="nav-strip dd-pills" aria-label="Sections"><div class="nav-pills">{pills}</div></nav>

<div class="dd-layout">
<nav class="dd-toc" aria-label="On this page"><div class="dd-toc-h">On this page</div><ol>{toc}</ol></nav>
<main class="dd-main" id="main">
{''.join(top)}
{chr(10).join(h for _, _, h in S)}
</main>
</div>
""" + FOOTER + FLOAT)
    return body, entry, extra


# ═════════════════════════════════════════════════════════════════════════════
# Index, search index, and category pages
# ═════════════════════════════════════════════════════════════════════════════
def letter_of(name: str) -> str:
    c = (name or "?")[:1].lower()
    return c if "a" <= c <= "z" else "0"


KIDNEY_BADGE = ('<span class="dd-kbadge" title="Has approved kidney dosing guidance">' + KIDNEY_ICON
                + '<span class="dd-hidden">Kidney dosing guidance</span></span>')


def _entry_li(e: dict, prefix: str = "") -> str:
    sub = " · ".join(x for x in (e.get("c", ""), ", ".join(e.get("b", [])[:3]) + ("…" if len(e.get("b", [])) > 3 else "")) if x)
    if e.get("m") and e.get("mh"):   # high-confidence variant spelling: the row goes to the main molecule
        return (f'<li class="dd-varli"><a href="{prefix}{esc(e["m"])}.html">{esc(e["n"])} <span class="dd-arrow">&rarr; {esc(e["mn"])}</span></a>'
                f'<span class="dd-sub">Variant spelling of {esc(e["mn"])}{" · " + esc(", ".join(e.get("b", [])[:3])) if e.get("b") else ""}</span></li>')
    did = (f'<span class="dd-sub">Did you mean <a href="{prefix}{esc(e["m"])}.html">{esc(e["mn"])}</a>?</span>' if e.get("m") else "")
    return (f'<li{" data-k=" + chr(34) + "1" + chr(34) if e.get("k") else ""}><a href="{prefix}{esc(e["s"])}.html">{esc(e["n"])}</a>'
            + (KIDNEY_BADGE if e.get("k") else "") + (f'<span class="dd-sub">{esc(sub)}</span>' if sub else "") + did + "</li>")


def category_groups(entries) -> dict[str, list[dict]]:
    """Group by class slug; every entry's "c" is rewritten to the group's most common spelling."""
    by: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if e.get("c"):
            by[cat_slug(e["c"])].append(e)
    groups: dict[str, list[dict]] = {}
    for items in by.values():
        cnt: dict[str, int] = {}
        for e in items:
            cnt[e["c"]] = cnt.get(e["c"], 0) + 1
        name = max(cnt.items(), key=lambda kv: (kv[1], kv[0]))[0]
        for e in items:
            e["c"] = name
        groups[name] = items
    return groups


# ═════════════════════════════════════════════════════════════════════════════
# "Browse by" views on the Drug Index (lazy JSON: browse.json + browse-brands.json)
# ═════════════════════════════════════════════════════════════════════════════
def _load_areas():
    import importlib.util
    spec = importlib.util.spec_from_file_location("therapeutic_areas", REPO / "tools" / "drugdb" / "therapeutic_areas.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


BROWSE_VIEWS = [("generic", "Generic name"), ("brand", "Brand name"), ("class", "Drug class"), ("area", "Therapeutic area"),
                ("disp", "Dispensing category"), ("kidney", "Kidney dosing"), ("nephrotox", "Kidney injury risk"), ("pn", "Parenteral nutrition")]
KIDNEY_GROUPS = [("avoid", "Avoid or contraindicated at low kidney function"), ("adjust", "Dose adjustment or caution needed"),
                 ("none", "No dose adjustment needed"), ("nodata", "Reviewed: no kidney dosing data")]
DISP_GROUPS = [(1, "Rx · Prescription drugs"), (2, "OTC · Over-the-counter"), (4, "HR · Household remedies"),
               (8, "S2 · Dangerous drugs (Dangerous Drugs Board)"), (16, "Controlled precursors and essential chemicals")]


def kidney_level(renal) -> str:
    """Most restrictive tile level across an APPROVED renal file's bands and dialysis entries ('' if none)."""
    if not renal_approved(renal):
        return ""
    lv = set()
    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get("level"), str):
                lv.add(x["level"].lower())
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(renal.get("bands"))
    walk({k: renal.get(k) for k in ("hd", "pd", "crrt", "pirrt")})
    for k, _ in KIDNEY_GROUPS:
        if k in lv:
            return k
    return "nodata"


def _strength_summary(products) -> str:
    """Short '100 mg, 300 mg · tablet' line: up to three strengths and the dosage-form groups."""
    st, fm = [], []
    for p in products:
        t = ws(p.get("dosage_strength_form"))
        m = _STRENGTH.search(t)
        if m:
            x = re.sub(r"\s+", " ", m.group(0)).strip()
            if x.lower() not in (y.lower() for y in st):
                st.append(x)
        f = form_group(t)
        if f != "other" and f not in fm:
            fm.append(f)
    st.sort(key=lambda x: (_num(x), x))
    out = ", ".join(st[:3]) + ("…" if len(st) > 3 else "")
    return " · ".join(x for x in (out, ", ".join(fm[:2])) if x)


# Parenteral nutrition group (tools/drugdb/pn_products.json; product types only, no clinical content)
PN_FILE = REPO / "tools" / "drugdb" / "pn_products.json"
_PN_ORAL = re.compile(r"\boral\b|tablet|capsule|granule|syrup|sachet|lozenge|chewable|suspension\b(?!.*infus)", re.I)


def pn_index(ctx: "Ctx") -> dict:
    """{"types": [[key, label]], "rows": [{name, link, slug, type, detail, badge, prods}], "slugs": set}.
    Membership and sub-types come from pn_products.json (see its _doc); rows are one per (brand, main generic page),
    unbranded products one per registration number. Cached on ctx."""
    if getattr(ctx, "_pn", None) is not None:
        return ctx._pn
    cfg = load_json(PN_FILE, {}) or {}
    inc, exc = set(cfg.get("include_generics") or []), set(cfg.get("exclude_generics") or [])
    exc_reg = {ws(x) for x in (cfg.get("exclude_registrations") or [])}
    cre = re.compile(cfg.get("include_category_regex") or r"(?!)", re.I)
    bmap = {_brand_key(k): v for k, v in (cfg.get("brands") or {}).items()}
    rmap = cfg.get("registrations") or {}
    gdef = cfg.get("generic_defaults") or {}
    types = [list(t) for t in (cfg.get("subtypes") or [])] or [["other", "Other parenteral nutrition"]]
    tkeys = {t[0] for t in types}
    rows: dict[tuple, dict] = {}
    slugs: set = set()
    for slug, ps in ctx.by_slug.items():
        if slug in exc:
            continue
        al = ctx.aliases.get(slug)
        target = al["main"] if al and al["high"] else slug
        if target in exc:
            continue
        gname = ws(ctx.generics.get(slug, {}).get("name"))
        for p in ps:
            b, rn = ws(p.get("brand_name")), ws(p.get("registration_number"))
            if rn in exc_reg:
                continue
            bk = _brand_key(b)
            info = bmap.get(bk) or rmap.get(rn)
            if not (slug in inc or info or cre.search(ws(p.get("pharmacologic_category")))):
                continue
            if _PN_ORAL.search(ws(p.get("dosage_strength_form"))):
                continue                                  # oral amino acids / vitamins / ketoanalogues are not PN
            info = info or gdef.get(slug) or gdef.get(target) or {}
            no_brand = (not bk or b.lower().strip(" .") in _NO_BRAND or bk == _brand_key(gname)
                        or bk == _brand_key(ws(p.get("generic_name"))))
            key = (rn if no_brand else bk, target)
            r = rows.setdefault(key, {"names": Counter(), "slug": target, "prods": [],
                                      "type": info.get("type") if info.get("type") in tkeys else "other",
                                      "detail": ws(info.get("detail")), "badge": info.get("badge") or "",
                                      "unbranded": rn if no_brand else ""})
            r["names"][b] += 1
            r["prods"].append(p)
            slugs.update({slug, target})
    notes = pn_notes(ctx)
    out = []
    for r in rows.values():
        name = f"(unbranded, {r['unbranded']})" if r["unbranded"] else r["names"].most_common(1)[0][0]
        nt = None if r["unbranded"] else next((notes[_brand_key(n)] for n in r["names"] if _brand_key(n) in notes), None)
        out.append(dict(r, name=name, link=r["unbranded"] or name, note=nt))
    order = {t[0]: i for i, t in enumerate(types)}
    out.sort(key=lambda r: (order.get(r["type"], 99), r["name"].lower().lstrip("("), r["slug"]))
    ctx._pn = {"types": types, "rows": out, "slugs": slugs}
    return ctx._pn


PN_NOTES_DIR = "pn-notes"


def pn_notes(ctx: "Ctx") -> dict:
    """Approved PN brand kidney notes (data/drugs/pn-notes/<brand-slug>.json), keyed by brand key.
    Only review_status == "approved" notes are returned (Dr. Rivero's sign-off). Cached on ctx."""
    if getattr(ctx, "_pn_notes", None) is not None:
        return ctx._pn_notes
    out = {}
    d = Path(ctx.data_dir) / PN_NOTES_DIR
    for f in sorted(d.glob("*.json")) if d.is_dir() else []:
        n = load_json(f, {}) or {}
        if isinstance(n, dict) and ws(n.get("review_status")).lower() == "approved" and ws(n.get("brand")):
            n.setdefault("slug", f.stem)
            out[_brand_key(n["brand"])] = n
    ctx._pn_notes = out
    return out


def pn_notes_for(slug: str, ctx: "Ctx") -> list[dict]:
    """Approved PN notes for the brands filed under this generic page (one per brand, PN-view order)."""
    seen, out = set(), []
    for r in pn_index(ctx)["rows"]:
        n = r.get("note")
        if n and r["slug"] == slug and n["slug"] not in seen:
            seen.add(n["slug"])
            out.append(n)
    return out


def _pn_num(v) -> str:
    if isinstance(v, float):
        return f"{v:g}"
    return ws(v)


def render_pn_notes(notes: list[dict]) -> str:
    """'Parenteral nutrition: kidney notes' — one block per approved brand note."""
    if not notes:
        return ""
    def lst(v):
        v = v if isinstance(v, list) else ([v] if v else [])
        return "".join(f"<li>{esc(ws(x))}</li>" for x in v if ws(x))
    out = ['<section class="dd-kidney dd-sec dd-pnsec" id="pn-kidney-notes" aria-labelledby="pn-kidney-notes-h">\n'
           f'<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">Parenteral nutrition · CKD · AKI · KRT</div>'
           '<h2 id="pn-kidney-notes-h">Parenteral nutrition: kidney notes</h2></div></div>\n'
           '<p class="dd-kidney-sum">Brand-specific kidney notes for the parenteral nutrition products filed under this generic: '
           'composition from the manufacturer SmPC or package insert, its kidney-related text, and how the product fits the '
           'guideline. Sources are listed under <a href="#references">References</a>.</p>']
    if len(notes) > 1:
        out.append('<p class="dd-note dd-pn-jump">Brands: ' + " · ".join(
            f'<a href="#pn-{esc(n["slug"])}">{esc(n["brand"])}</a>' for n in notes) + "</p>")
    for n in notes:
        sid = f'pn-{esc(n["slug"])}'
        b = [f'<article class="dd-pnn" id="{sid}" aria-labelledby="{sid}-h"><h3 class="dd-pnn-h" id="{sid}-h">Kidney notes: {esc(n["brand"])}</h3>']
        if ws(n.get("summary")):
            b.append(f'<p class="dd-kidney-sum">{esc(ws(n["summary"]))}</p>')
        comp = [c for c in (n.get("composition") or []) if isinstance(c, dict)]
        if comp:
            keys = list(dict.fromkeys(k for c in comp for k in c if k != "presentation"))
            head = "".join(f'<th scope="col">{esc(c.get("presentation") or "")}</th>' for c in comp)
            rows = "".join(f'<tr><th scope="row">{esc(k)}</th>' + "".join(
                f'<td>{esc(_pn_num(c.get(k))) if c.get(k) not in (None, "") else "<span class=dd-pn-na>not shown</span>"}</td>'
                for c in comp) + "</tr>" for k in keys)
            b.append('<h4 class="dd-kidney-sub">Composition</h4><div class="table-wrap"><table class="drug-table dd-pncomp">'
                     f'<thead><tr><th scope="col">Per presentation</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
        if n.get("composition_notes"):
            b.append(f'<ul class="dd-uselist dd-pn-cnotes">{lst(n["composition_notes"])}</ul>')
        if ws(n.get("nutrient_numbers")) and comp:
            b.append(f'<p class="dd-note">{esc(ws(n["nutrient_numbers"]))}</p>')
        if n.get("dosing_limits"):
            b.append(f'<h4 class="dd-kidney-sub">Dose and rate limits</h4><ul class="dd-uselist">{lst(n["dosing_limits"])}</ul>')
        if n.get("kidney_notes"):
            b.append(f'<h4 class="dd-kidney-sub">Kidney notes</h4><ul class="dd-uselist">{lst(n["kidney_notes"])}</ul>')
        if n.get("guideline"):
            gh = ws(n.get("guideline_heading")) or "How it fits the guideline"
            b.append(f'<h4 class="dd-kidney-sub">{esc(gh)}</h4><ul class="dd-uselist">{lst(n["guideline"])}</ul>')
        if ws(n.get("bottom_line")):
            b.append(f'<h4 class="dd-kidney-sub">Bottom line</h4><p class="dd-pn-bottom">{esc(ws(n["bottom_line"]))}</p>')
        if n.get("withheld"):
            b.append(f'<h4 class="dd-kidney-sub">Not shown here</h4><ul class="dd-uselist">{lst(n["withheld"])}</ul>')
        by, on = ws(n.get("reviewed_by")), us_date_str(n.get("reviewed_date"))
        b.append('<p class="dd-note">renalcarematters.com notes' + (f", reviewed by {esc(by)}" if by else "")
                 + (f" on {esc(on)}" if on else "") + f'. Check the current Philippine package insert before use. {OURS_CHIP}</p></article>')
        out.append("".join(b))
    return "\n".join(out) + "\n</section>\n"


def pn_partof(slug: str, ctx: "Ctx") -> str:
    if slug not in pn_index(ctx)["slugs"]:
        return ""
    return ('<p class="dd-partof">Part of: <a href="/drugs/?view=pn">Parenteral nutrition products</a> '
            '<span class="dd-sub-inline">(Drug Index, by product type)</span></p>')


def browse_data(entries: list[dict], groups: dict, ctx: Ctx) -> tuple[dict, dict]:
    """Compact data for the non-default Browse-by views. Rows reference generics by index into "g"
    (the page JS reads names and filter facets from search-index.json)."""
    main = [e for e in entries if not e.get("mh")]          # high-confidence variant spellings are folded into their main page
    gi = {e["s"]: i for i, e in enumerate(main)}
    G = [e["s"] for e in main]
    # brands: every PH brand -> its generic page (variant spellings -> main molecule, spelling noted)
    by_key: dict[tuple, dict] = {}
    for slug in G + [v for v, a in ctx.aliases.items() if a["high"]]:
        target = ctx.aliases[slug]["main"] if slug in ctx.aliases and ctx.aliases[slug]["high"] else slug
        if target not in gi:
            continue
        g = ctx.generics.get(slug, {})
        gname = ws(g.get("name"))
        for p in ctx.by_slug.get(slug, []):
            b = ws(p.get("brand_name"))
            k = _brand_key(b)
            if (not k or b.lower().strip(" .") in _NO_BRAND or k == _brand_key(gname)
                    or k == _brand_key(ws(p.get("generic_name")))):
                continue
            r = by_key.setdefault((k, target), {"names": {}, "prods": [], "var": set()})
            r["names"][b] = r["names"].get(b, 0) + 1
            r["prods"].append(p)
            if slug != target:
                r["var"].add(ws(p.get("generic_name")) or gname)
    brands = []
    for (k, target), r in by_key.items():
        name = max(r["names"].items(), key=lambda kv: (kv[1], kv[0]))[0]
        row = [name, gi[target], _strength_summary(r["prods"])]
        if r["var"]:
            row.append(sorted(r["var"])[0])
        brands.append(row)
    brands.sort(key=lambda r: (r[0].lower(), G[r[1]]))
    # drug class (same grouping and slugs as the class pages)
    cls = []
    for name, items in sorted(groups.items(), key=lambda kv: kv[0].lower()):
        ids = sorted({gi[e["s"]] for e in items if e["s"] in gi})
        if ids:
            cls.append([name, cat_slug(name), ids])
    # therapeutic area (tools/drugdb/therapeutic_areas.py)
    TA = _load_areas()
    area: dict[str, list[int]] = defaultdict(list)
    for e in main:
        area[TA.assign(e)[0]].append(gi[e["s"]])
    areas = [[a, area[a]] for a in TA.ORDER if area.get(a)]
    # dispensing category
    disp = [[lab, bit, [gi[e["s"]] for e in main if (e.get("r") or 0) & bit]] for bit, lab in DISP_GROUPS]
    disp = [d for d in disp if d[2]]
    # kidney dosing (approved guidance only)
    kg: dict[str, list[int]] = defaultdict(list)
    for e in main:
        lv = kidney_level(ctx.renal(e["s"]))
        if lv:
            kg[lv].append(gi[e["s"]])
    kid = [[lab, k, kg[k]] for k, lab in KIDNEY_GROUPS if kg.get(k)]
    n_k = sum(len(x[2]) for x in kid)
    # parenteral nutrition: [brand, generic index, sub-type, detail, badge, strengths, link term]
    PN = pn_index(ctx)
    pn_rows = [[r["name"], gi[r["slug"]], r["type"], r["detail"], r["badge"], _strength_summary(r["prods"]), r["link"]]
               + ([f'pn-{r["note"]["slug"]}'] if r.get("note") else [])
               for r in PN["rows"] if r["slug"] in gi]
    nmech = ctx.nephrotox.get("mechanisms") or {}
    ng: dict[str, list[int]] = defaultdict(list)
    for e in main:
        nx = ctx.nx(e["s"])
        for m in dict.fromkeys(m for _, _, r in (nx or {}).get("items", []) for m in r.get("mech") or []):
            ng[m].append(gi[e["s"]])
    nxv = [[nmech[m]["label"], m, ng[m]] for m in nmech if ng.get(m)]
    core = {"v": 1, "g": G, "class": cls, "area": areas, "disp": disp, "kidney": kid, "nx": nxv,
            "nxN": len({i for x in nxv for i in x[2]}),
            "pn": {"t": PN["types"], "r": pn_rows},
            "kidneyNote": f"The other {len(G) - n_k:,} generics show US label kidney text only, where the label has it; "
                          "reviewed kidney guidance is being added."}
    return core, {"v": 1, "g": G, "b": brands}


def index_page(entries: list[dict], ctx: Ctx, n_cats: int, off: dict | None = None) -> str:
    groups = defaultdict(list)
    for e in sorted(entries, key=lambda e: e["n"].lower()):
        groups[letter_of(e["n"])].append(e)
    letters = ["0"] + [chr(c) for c in range(ord("a"), ord("z") + 1)]
    btns = '<button type="button" data-l="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-l="{l}" aria-pressed="false"{"" if groups.get(l) else " disabled"} '
        f'aria-label="{"Names starting with a number or symbol" if l == "0" else "Letter " + l.upper()}">{"#" if l == "0" else l.upper()}</button>'
        for l in letters)
    secs = "".join(f'<section class="dd-letter" id="letter-{l}" data-l="{l}"><h2>{"#" if l == "0" else l.upper()}</h2>'
                   f'<ul class="dd-list">{"".join(_entry_li(e) for e in groups[l])}</ul></section>' for l in letters if groups.get(l))
    cg = category_groups(entries)
    cat_opts = "".join(f'<option value="{esc(c)}">{esc(c)} ({len(v)})</option>'
                       for c, v in sorted(cg.items(), key=lambda kv: kv[0].lower()) if len(v) >= 2)
    form_opts = "".join(f'<option value="{f}">{f.capitalize()}</option>' for f, _ in FORM_GROUPS[::-1]) + '<option value="other">Other</option>'
    n_products = len(ctx.products)
    supp_n = len(load_json(REPO / "drugs" / "supplements" / "search-index.json", []) or [])
    _supp = load_json(REPO / "drugs" / "supplements" / "search-index.json", []) or []
    fsmp_n = sum(1 for e in _supp if e.get("t"))
    fsdu_n = sum(1 for e in _supp if e.get("mk") in ("fsdu", "both"))
    fsmp_only = sum(1 for e in _supp if e.get("t") and e.get("mk", "fsmp") in ("fsmp", "both"))
    supp_chip = ((f'<a class="dd-chip" href="/drugs/supplements/">{supp_n - fsmp_n:,} food-supplement brands</a>'
                  + (f'<a class="dd-chip" href="/drugs/supplements/?cat=fsmp">{fsmp_only:,} medical-nutrition (FSMP) brands</a>' if fsmp_only else "")
                  + (f'<a class="dd-chip" href="/drugs/supplements/?cat=fsdu">{fsdu_n:,} special dietary food (FSDU) brands</a>' if fsdu_n else ""))
                 if supp_n else "")
    oa = off or {"n": 0, "drugs": 0, "store": 5, "dl": 5}
    canonical = f"{SITE}/drugs/"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "@id": canonical, "url": canonical,
                         "name": "Drug Index · Renal Care Matters", "dateModified": "__ISO__", "inLanguage": "en",
                         "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"},
                         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE}}).replace("</", "<\\/")
    desc = (f"Search {len(entries):,} generics and {n_products:,} FDA Philippines-registered drug products by brand, generic, class, "
            "indication, manufacturer or registration number, with kidney dosing and US FDA prescribing information.")
    return (head("Drug Index · Renal Care Matters", desc, canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode dd-index-page">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid"><div class="hero-copy">
        <div class="hero-tag">Drug Database · Clinicians</div>
        <h1>Drug Index</h1>
        <p class="hero-sub">Every drug product registered with the Food and Drug Administration (FDA) Philippines, grouped by generic name.
Search by brand, generic, class, indication, manufacturer or registration number.</p>
        <nav class="dd-tools no-print" aria-label="Clinical tools">
<a class="dd-tool dd-tool-ix" href="/drugs/interactions.html"><span class="dd-tool-ico"><svg viewBox="0 0 32 32" aria-hidden="true"><rect x="3" y="11" width="17" height="8" rx="4" transform="rotate(-35 11.5 15)"/><path d="M8.6 18.6 13.4 11.6"/><rect x="12" y="13" width="17" height="8" rx="4" transform="rotate(35 20.5 17)"/><circle cx="16" cy="16" r="2.3" class="dd-tool-dot"/></svg></span><span class="dd-tool-t"><strong>Interaction checker</strong><small>Graded pairs, kidney checks, paste a prescription</small></span><svg class="dd-tool-arr" viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
<a class="dd-tool dd-tool-ms" href="/drugs/med-scheduler.html"><span class="dd-tool-ico"><svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="14" cy="15" r="10"/><path d="M14 9v6l4 3"/><rect x="19" y="20" width="11" height="6" rx="3" transform="rotate(-35 24.5 23)"/></svg></span><span class="dd-tool-t"><strong>Med Scheduler</strong><small>Timetable around meals, bedtime and dialysis</small></span><svg class="dd-tool-arr" viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        </nav>
        <div class="dd-chips"><span class="dd-chip">{len(entries):,} generics</span><span class="dd-chip">{n_products:,} PH products</span>
<a class="dd-chip" href="/drugs/category/">Browse {n_cats:,} drug classes</a>{supp_chip}</div>
        <a class="dd-app-cta no-print" href="#dd-app" id="dd-app-cta"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M12 7v7"/><path d="m9 11 3 3 3-3"/><path d="M10.5 18.5h3"/></svg><span class="dd-app-cta-t"><strong>Install Dosis, the Drug Index app</strong><small>Works offline, even with no signal</small></span><svg class="dd-app-cta-arr" viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg></a>
        <div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span>
        <p class="dd-sched"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="m9.5 15 2 2 3.5-3.5"/></svg>
<span><strong>Updated weekly:</strong> every Monday morning, Philippine time (starts at 1:47 AM). US and EU label text is refreshed and every page is rebuilt.<span class="dd-sched-next" hidden> Next update: <time id="dd-next-upd"></time>.</span></span></p></div>
    </div></div>
  </div>
</section>
<main class="container dd-wide" id="dd-index" data-src="/drugs/search-index.json" data-extra="/drugs/search-extra.json"{' data-supp="/drugs/supplements/search-index.json"' if supp_n else ''}>
<div class="dd-favs no-print" id="dd-favs" hidden><span class="dd-ix-ql">★ Favorites</span><div class="dd-ix-qchips" id="dd-favlist"></div></div>
<div class="dd-search" role="search">
<label class="dd-hidden" for="dd-sq">Search the drug index</label>
<input id="dd-sq" type="search" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="dd-results"
 placeholder="{'Brand, generic, class, indication, supplement, or reg. no. (e.g., Norvasc)' if supp_n else 'Brand, generic, class, indication, manufacturer, or reg. no. (e.g., Norvasc)'}" autocomplete="off" spellcheck="false">
</div>
<div class="dd-facets" role="group" aria-label="Filters">
{'<label><span class="dd-hidden">Type</span><select id="dd-f-type"><option value="">Type: drugs and food supplements</option><option value="d">Type: drugs</option><option value="s">Type: food supplements</option><option value="m">Type: medical nutrition (FSMP, FSDU)</option></select></label>' if supp_n else ''}
<label><span class="dd-hidden">Drug class</span><select id="dd-f-class"><option value="">All drug classes</option>{cat_opts}</select></label>
<label><span class="dd-hidden">Dispensing category</span><select id="dd-f-rx"><option value="">All dispensing categories</option><option value="1">Rx · Prescription drug</option><option value="2">OTC · Over-the-counter</option><option value="4">HR · Household remedy</option><option value="8">S2 · Dangerous drug</option><option value="16">Controlled precursor</option></select></label>
<label><span class="dd-hidden">Dosage form</span><select id="dd-f-form"><option value="">All dosage forms</option>{form_opts}</select></label>
<label class="dd-check"><input type="checkbox" id="dd-f-k"> {KIDNEY_ICON} Has kidney dosing</label>
<label class="dd-check"><input type="checkbox" id="dd-f-n"> Kidney injury risk</label>
<label class="dd-check"><input type="checkbox" id="dd-f-p"> PNF-listed</label>
<label class="dd-check"><input type="checkbox" id="dd-f-h"> PhilHealth GAMOT</label>
<label class="dd-check"><input type="checkbox" id="dd-f-l"> Has US label</label>
<label class="dd-check"><input type="checkbox" id="dd-f-e"> Has EU SmPC</label>
<button type="button" class="dd-btn dd-btn-ghost" id="dd-f-clear">Clear</button>
</div>
<p class="dd-note" id="dd-sinfo" aria-live="polite"></p>
<ul class="dd-results dd-list" id="dd-results" role="listbox" aria-label="Search results" hidden></ul>
<div class="dd-browse-wrap no-print"><span class="dd-browse-l" id="dd-browse-l">Browse by</span>
<div class="dd-browse" id="dd-browse" role="tablist" aria-labelledby="dd-browse-l">{"".join(
    f'<button type="button" role="tab" id="dd-tab-{v}" data-v="{v}" aria-controls="{"dd-az" if v == "generic" else "dd-view"}" '
    f'aria-selected="{"true" if v == "generic" else "false"}" tabindex="{0 if v == "generic" else -1}">{lab}</button>'
    for v, lab in BROWSE_VIEWS)}</div></div>
<nav class="dd-alpha" id="dd-alpha" aria-label="Filter by first letter">{btns}</nav>
<div id="dd-az" role="tabpanel" aria-labelledby="dd-tab-generic">{secs}</div>
<div id="dd-view" role="tabpanel" aria-labelledby="dd-tab-generic" hidden data-src="/drugs/browse.json?v={ASSET_VERSION}" data-brands="/drugs/browse-brands.json?v={ASSET_VERSION}"></div>
<section class="dd-app no-print" id="dd-app" aria-labelledby="dd-app-h">
<h2 id="dd-app-h">Dosis: use the Drug Index as an app</h2>
<div class="dd-app-grid">
<div class="dd-app-card">
<h3>Install on your phone or computer</h3>
<p data-app="hint">Add Dosis to your home screen from your browser menu (<strong>Install app</strong> or <strong>Add to Home Screen</strong>).
It opens full screen, like an app.</p>
<button type="button" class="dd-btn" data-app="install" hidden>Install the app</button>
<ol class="dd-app-ios" data-app="iossteps" hidden>
<li>In <strong>Safari</strong>, tap the <strong>&#8801;</strong> icon at the left end of the address bar (iPad) or the <strong>&#8943;</strong> button
(iPhone). On versions before iOS 26, tap the <strong>Share</strong> button (a square with an arrow pointing up) and skip to step 3.</li>
<li>Tap <strong>Share</strong>.</li>
<li>Tap <strong>Add to Home Screen</strong>. If you don't see it, scroll down or tap <strong>View More</strong>.</li>
<li>Keep <strong>Open as Web App</strong> switched on, then tap <strong>Add</strong>.</li>
<li>Open <strong>Dosis</strong> from your Home Screen, tap <strong>Set up offline use</strong>, then <strong>Download the complete Drug
Index</strong>. Download inside the Home Screen app, not in a Safari tab: the two keep separate storage, and only the app's copy works offline.</li>
</ol>
</div>
<div class="dd-app-card" data-app="off">
<h3>Offline use</h3>
<p>Once loaded, search and the browse lists work without signal, and every drug page you open is kept on this device.
For reliable use where there is no signal (wards, basements, the dialysis unit), download the complete Drug Index once:</p>
<div class="dd-app-opt"><button type="button" class="dd-btn" data-app="dl">Download the complete Drug Index</button>
<span class="dd-app-meta">Every drug, drug class and supplement page · about {oa["dl"]} MB to download, {oa["store"]} MB on the device</span></div>
<p class="dd-app-warn" data-app="iosnote" hidden><strong>iPhone and iPad:</strong> add Dosis to your Home Screen first, then open it
from there and download. Safari and the Home Screen app keep separate storage, so pages downloaded in a Safari tab do not carry over,
and Safari may clear them after a week without a visit. The Home Screen app keeps them.</p>
<p class="dd-note" data-app="status" aria-live="polite"></p>
<progress data-app="bar" max="1" value="0" hidden></progress>
<button type="button" class="dd-btn dd-btn-ghost" data-app="rm" hidden>Remove downloaded pages</button>
<p class="dd-note">Use Wi-Fi for the full set and keep this page open while it downloads. If it stops, tap the button again: pages
already saved are kept. Updates download only the pages that changed. Saved pages also refresh each time you open them online;
check a page's "Last updated" date before relying on it offline, and verify doses against the current Philippine package insert.</p>
</div>
</div>
</section>
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Product data come from the FDA Philippines registration
database and may lag behind the official record; verify on <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verification.fda.gov.ph</a>
and the current Philippine package insert. Not a substitute for clinical judgment.</div>
</main>
""" + FOOTER + FLOAT)


def category_page(cat: str, items: list[dict]) -> str:
    slug = cat_slug(cat)
    canonical = f"{SITE}/drugs/category/{slug}"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "@id": canonical, "url": canonical,
                         "name": f"{cat} · Drug Index", "dateModified": "__ISO__", "inLanguage": "en"}, ensure_ascii=False).replace("</", "<\\/")
    lis = "".join(_entry_li(e, "/drugs/") for e in sorted(items, key=lambda e: e["n"].lower()))
    return (head(f"{cat}: drugs in this class · Renal Care Matters", f"{len(items)} generics in the class {cat}, with Philippine brands, kidney dosing and US FDA label text.",
                 canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode">\n' + header(True) + f"""
<section class="hero"><div class="container dd-hero-wide"><div class="hero-grid"><div class="hero-copy">
<div class="dd-crumb"><a href="/drugs/">Drug Index</a> › <a href="/drugs/category/">Drug classes</a></div>
<div class="hero-tag">Drug class</div>
<h1>{esc(cat)}</h1>
<p class="hero-sub">{len(items):,} generic{'s' if len(items) != 1 else ''} in this class. Class names come from the US FDA established
pharmacologic class when a US label is available, otherwise from the FDA Philippines pharmacologic category.</p>
<div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
</div></div></div></section>
<main class="container dd-wide"><ul class="dd-list dd-catlist">{lis}</ul></main>
""" + FOOTER + FLOAT)


IX_ORAL = {"tablet", "capsule", "oral liquid"}


def route_flags(ctx: "Ctx", slug: str) -> tuple[bool, bool]:
    """(taken by mouth, every product applied locally: skin, eye, ear, nose, vagina)."""
    fg = [(form_group(ws(p.get("dosage_strength_form"))), ws(p.get("dosage_strength_form"))) for p in ctx.by_slug.get(slug, [])]
    oral = any(f in IX_ORAL and not NX_LOCAL.search(d) for f, d in fg)
    local = bool(fg) and all(f not in NX_SYSTEMIC or NX_LOCAL.search(d) for f, d in fg)
    return oral, local


def interactions_data(ctx: "Ctx", entries: list[dict]) -> tuple[dict, dict]:
    """drugs/interactions.json for the interaction checker (tools/drugdb/interactions.py) plus approved kidney tiles
    and kidney injury mechanisms per generic."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("ixmod", REPO / "tools" / "drugdb" / "interactions.py")
    ix = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ix)
    spec2 = importlib.util.spec_from_file_location("mrs", REPO / "tools" / "drugdb" / "merge_renal_short.py")
    mrs = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(mrs)
    slugs = [e["s"] for e in entries]
    flags = {s: route_flags(ctx, s) for s in slugs}
    data, rep = ix.build(ctx, slugs, None, lambda s: flags[s][0], lambda s: flags[s][1])
    K, NXM = {}, {}
    for s in slugs:
        r = ctx.renal(s)
        if renal_approved(r):
            b = []
            for band in r.get("bands") or []:
                k = mrs.band_key(band.get("range", "")) if isinstance(band, dict) else None
                if k and band.get("short"):
                    b.append([k[5:], ws(band.get("range")), band["short"], band.get("level") or "nodata"])
            kd = {"b": b}
            for m in ("hd", "pd", "crrt"):
                v = r.get(m)
                if isinstance(v, dict) and v.get("short"):
                    kd[m] = [v["short"], v.get("level") or "nodata"]
            if b or len(kd) > 1:
                K[s] = kd
        nx = ctx.nx(s)
        if nx:
            NXM[s] = list(dict.fromkeys(m for _, _, rr in nx["items"] for m in rr.get("mech") or []))
    data["k"], data["nx"] = K, NXM
    data["nxl"] = {k: v["label"] for k, v in (ctx.nephrotox.get("mechanisms") or {}).items()}
    data["owners"] = sorted({r[0] for r in data["rows"]})
    return data, rep


def interactions_page(n_owners: int, n_rows: int) -> str:
    canonical = f"{SITE}/drugs/interactions"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebApplication", "@id": canonical, "url": canonical,
                         "name": "Interaction checker · Drug Index", "applicationCategory": "HealthApplication",
                         "dateModified": "__ISO__", "inLanguage": "en",
                         "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"}}).replace("</", "<\\/")
    kopts = "".join(f'<option value="{v}">{l}</option>' for v, l in (
        ("", "Not specified"), ("ge60", "eGFR or CrCl 60 or more"), ("30_59", "eGFR or CrCl 30 to 59"),
        ("15_29", "eGFR or CrCl 15 to 29"), ("lt15", "Below 15, not on dialysis"), ("hd", "Hemodialysis"),
        ("pd", "Peritoneal dialysis"), ("crrt", "CRRT")))
    return (head("Interaction checker · Renal Care Matters",
                 "Check a list of medicines for drug interactions, kidney injury risks and kidney dosing, graded by severity. "
                 "Philippine brands and generics.", canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode dd-index-page dd-ix-page">\n' + header(True) + f"""
<section class="hero"><div class="container dd-hero-wide"><div class="hero-grid"><div class="hero-copy">
<div class="dd-crumb"><a href="/drugs/">Drug Index</a></div>
<div class="hero-tag">Drug Database · Clinicians</div>
<h1>Interaction checker</h1>
<p class="hero-sub">Add the medicines a patient takes, by Philippine brand or generic name. The checker grades each interaction, flags kidney risks, and shows kidney dosing for the patient's kidney function.</p>
<div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
</div></div></div></section>
<main class="container dd-wide" id="dd-ix" data-src="/drugs/search-index.json" data-ix="/drugs/interactions.json">
<div class="dd-ix-pick">
<div class="dd-ix-add" role="search">
<label for="dd-ix-q" class="dd-ix-l">Add a medicine</label>
<input id="dd-ix-q" type="search" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="dd-ix-sug"
 placeholder="Brand or generic (e.g., Norvasc, losartan)" autocomplete="off" spellcheck="false">
<ul id="dd-ix-sug" class="dd-ix-sug" role="listbox" aria-label="Matching medicines" hidden></ul>
</div>
<div id="dd-ix-sel" class="dd-ix-chips" aria-live="polite"></div>
<div class="dd-ix-quick" id="dd-ix-quick">
<div class="dd-ix-qrow" id="dd-ix-favrow" hidden><span class="dd-ix-ql">★ Favorites</span><div id="dd-ix-fav" class="dd-ix-qchips"></div></div>
<div class="dd-ix-qrow" id="dd-ix-recrow" hidden><span class="dd-ix-ql">Recent</span><div id="dd-ix-rec" class="dd-ix-qchips"></div></div>
</div>
<details class="dd-ix-paste"><summary>Paste a medication list</summary>
<label class="dd-hidden" for="dd-ix-ta">Medication list</label>
<textarea id="dd-ix-ta" rows="5" placeholder="One medicine per line, as written on the prescription:&#10;Losartan 50 mg 1 tab OD&#10;Norvasc 10 mg OD&#10;Sevelamer 800 mg TID with meals"></textarea>
<button type="button" class="dd-btn" id="dd-ix-parse">Add these medicines</button> <span class="dd-note" id="dd-ix-pmsg" aria-live="polite"></span>
</details>
<div class="dd-ix-row">
<label class="dd-ix-k">Kidney function <select id="dd-ix-kf">{kopts}</select></label>
<span class="dd-ix-btns"><button type="button" class="dd-btn dd-btn-ghost" id="dd-ix-share">Copy link</button>
<button type="button" class="dd-btn dd-btn-ghost" id="dd-ix-print">Print</button>
<button type="button" class="dd-btn dd-btn-ghost" id="dd-ix-clear">Clear all</button></span>
</div>
</div>
<div id="dd-ix-out" class="dd-ix-out" aria-live="polite"><p class="dd-note">Add two or more medicines to check them together. Add one to see its kidney dosing and listed interactions.</p></div>
<section class="dd-ix-about" aria-labelledby="dd-ix-about-h">
<h2 id="dd-ix-about-h">How interactions are graded</h2>
<ul class="dd-ix-legend">
<li><span class="dd-ix-g g-ci">Contraindicated</span> The source says the combination must not be used.</li>
<li><span class="dd-ix-g g-avoid">Avoid</span> Avoid the combination; use only with specialist reason and close monitoring.</li>
<li><span class="dd-ix-g g-adjust">Adjust or monitor</span> Usually usable with a dose change, spacing, or monitoring.</li>
<li><span class="dd-ix-g g-minor">Minor</span> Small or uncommon effect; awareness is enough for most patients.</li>
</ul>
<p>Each interaction is quoted from a drug monograph reviewed by renalcarematters.com, built on US FDA labels and PubMed-verified literature. Reviewed interaction lists now cover {n_owners:,} drugs ({n_rows:,} interactions). A pair is found when either drug's list names the other drug or its class, so <strong>no result does not mean no interaction</strong>; check the full prescribing information.</p>
<p>Kidney checks use the reviewed kidney dosing and the kidney injury tags on each drug page. Favorites and recent medicines are saved only on this device.</p>
</section>
</main>
""" + FOOTER + FLOAT)


def scheduler_data(ctx: "Ctx", ixd: dict) -> dict:
    """drugs/med-scheduler.json: timing rules by molecule (data/drugs/timing.json, label-sourced), generics whose APPROVED
    hemodialysis entry says to dose after dialysis, and separation windows linked to approved interaction rows."""
    tj = load_json(ctx.data_dir / "timing.json", {}) or {}
    rules = {}
    if tj.get("review_status") == "approved":
        for k, v in (tj.get("rules") or {}).items():
            rules[ctx.single_slug(k) or k.replace(" ", "-")] = v
    hd_after = []
    for s in ixd["g"]:
        r = ctx.renal(s)
        if renal_approved(r):
            v = r.get("hd")
            txt = v.get("text") if isinstance(v, dict) else v
            lvl = (v.get("level") or "") if isinstance(v, dict) else ""
            if lvl in ("avoid", "nodata", "hide") or (txt and re.search(r"\bno (supplement|supplemental dose)\b|not dialyzable|does not make it safe", txt, re.I)):
                continue
            if txt and re.search(r"after (each |every )?(HD|hemodialysis|dialysis)|post-?HD|post-?dialysis|following (each )?(HD|hemodialysis|dialysis)", txt, re.I):
                hd_after.append(s)
    sep = {}
    for owner, prefix, before, after in tj.get("separations") or []:
        for i, row in enumerate(ixd["rows"]):
            if row[0] == owner and row[2].startswith(prefix):
                sep[str(i)] = [before, after]
    pu = (tj.get("purpose") or {}) if tj.get("review_status") == "approved" else {}
    return {"v": 1, "r": rules, "hdAfter": sorted(hd_after), "sep": sep, "pu": pu}


def scheduler_page() -> str:
    canonical = f"{SITE}/drugs/med-scheduler"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebApplication", "@id": canonical, "url": canonical,
                         "name": "Med Scheduler · Drug Index", "applicationCategory": "HealthApplication",
                         "dateModified": "__ISO__", "inLanguage": "en",
                         "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"}}).replace("</", "<\\/")
    days = "".join(f'<label class="dd-ms-day"><input type="checkbox" value="{i}" data-hdday> {d}</label>'
                   for i, d in enumerate(("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")))
    return (head("Med Scheduler · Renal Care Matters",
                 "Build a daily medication schedule around a patient's meals, bedtime and dialysis days, with each timing "
                 "rule taken from the US label. For clinicians; prints a simple patient sheet.", canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode dd-index-page dd-ms-page">\n' + header(True) + f"""
<section class="hero no-print"><div class="container dd-hero-wide"><div class="hero-grid"><div class="hero-copy">
<div class="dd-crumb"><a href="/drugs/">Drug Index</a> · <a href="/drugs/interactions.html">Interaction checker</a></div>
<div class="hero-tag">Drug Database · Clinicians</div>
<h1>Med Scheduler</h1>
<p class="hero-sub">Set the patient's day (meals, bedtime, dialysis), add the medicines, and get a timetable for dialysis and non-dialysis days that respects food rules and dose spacing. Print a simple sheet for the patient.</p>
<div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
</div></div></div></section>
<main class="container dd-wide" id="dd-ms" data-src="/drugs/search-index.json" data-ix="/drugs/interactions.json" data-ms="/drugs/med-scheduler.json">
<div class="dd-ms-grid no-print">
<section class="dd-ix-pick dd-ms-routine" aria-labelledby="dd-ms-r-h">
<h2 id="dd-ms-r-h">1. The patient's day</h2>
<div class="dd-ms-times">
<label>Wakes <input type="time" id="ms-wake" value="06:00"></label>
<label>Breakfast <input type="time" id="ms-bf" value="07:00"></label>
<label>Lunch <input type="time" id="ms-lu" value="12:00"></label>
<label>Dinner <input type="time" id="ms-di" value="18:30"></label>
<label>Bedtime <input type="time" id="ms-bed" value="21:30"></label>
</div>
<fieldset class="dd-ms-hd"><legend>Dialysis</legend>
<label><input type="radio" name="ms-dx" value="none" checked> None</label>
<label><input type="radio" name="ms-dx" value="hd"> Hemodialysis</label>
<div class="dd-ms-hdbox" id="ms-hdbox" hidden>
<div class="dd-ms-preset"><button type="button" class="dd-ix-q" data-preset="0,2,4">Mon · Wed · Fri</button><button type="button" class="dd-ix-q" data-preset="1,3,5">Tue · Thu · Sat</button></div>
<div class="dd-ms-days">{days}</div>
<div class="dd-ms-times"><label>Session starts <input type="time" id="ms-hs" value="06:00"></label><label>Ends <input type="time" id="ms-he" value="10:00"></label></div>
<label class="dd-check"><input type="checkbox" id="ms-hold"> Hold blood-pressure medicines until after dialysis on dialysis days</label>
<label class="dd-ms-aht">Give once-daily blood-pressure medicines at the same time every day
<select id="ms-aht"><option value="auto">By shift (recommended)</option><option value="L">After lunch</option><option value="D">After dinner</option><option value="HS">At bedtime</option></select></label>
<p class="dd-sub dd-ms-ahtnote">By shift: morning session, after lunch; midday or afternoon session, after dinner; evening session, at bedtime. Twice-daily agents (morning session): after lunch and at bedtime. Alpha blockers: bedtime. A time in the sig always wins.</p>
</div>
</fieldset>
</section>
<section class="dd-ix-pick dd-ms-meds" aria-labelledby="dd-ms-m-h">
<h2 id="dd-ms-m-h">2. Medicines</h2>
<div class="dd-ix-add" role="search">
<label for="dd-ix-q" class="dd-ix-l">Add a medicine</label>
<input id="dd-ix-q" type="search" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="dd-ix-sug"
 placeholder="Brand or generic (e.g., Renvela, losartan)" autocomplete="off" spellcheck="false">
<ul id="dd-ix-sug" class="dd-ix-sug" role="listbox" aria-label="Matching medicines" hidden></ul>
</div>
<details class="dd-ix-paste" open><summary>Paste a prescription</summary>
<label class="dd-hidden" for="dd-ix-ta">Prescription</label>
<textarea id="dd-ix-ta" rows="6" placeholder="One medicine per line, with its sig:&#10;Levothyroxine 50 mcg 1 tab OD before breakfast&#10;Sevelamer 800 mg 1 tab TID with meals&#10;Losartan 50 mg 1 tab BID&#10;Calcitriol 0.25 mcg 1 cap post-HD"></textarea>
<button type="button" class="dd-btn" id="dd-ix-parse">Read the prescription</button> <span class="dd-note" id="dd-ix-pmsg" aria-live="polite"></span>
<div class="dd-ms-samples"><span>Try a sample prescription:</span>
<button type="button" class="dd-btn dd-btn-ghost" data-ms-sample="hd">Hemodialysis patient</button>
<button type="button" class="dd-btn dd-btn-ghost" data-ms-sample="ckd">CKD, not on dialysis</button></div>
</details>
<div id="ms-list" class="dd-ms-list" aria-live="polite"></div>
<div class="dd-ix-row"><span class="dd-ix-btns">
<button type="button" class="dd-btn" id="ms-build">Build the schedule</button>
<button type="button" class="dd-btn dd-btn-ghost" id="ms-clear">Clear medicines</button></span></div>
</section>
</div>
<div id="ms-out" class="dd-ms-out" aria-live="polite"></div>
<section class="dd-ix-about no-print" aria-labelledby="ms-about-h">
<h2 id="ms-about-h">How the schedule is built</h2>
<p>Meal and time-of-day rules come from each medicine's US label (shown with each placement). Dose spacing, such as levothyroxine 4 hours from phosphate binders, comes from the reviewed interaction lists. Medicines dosed after dialysis follow the reviewed kidney dosing. The scheduler meets every rule it can with the fewest dose times and lists any rule it cannot meet. Medicines with no label timing rule are placed at standard times and can be moved with the timing menu. A few placements follow local practice and are tagged <strong>Practice default</strong>: statins at bedtime, and blood-pressure medicines at one fixed time every day when the hold toggle is on. Placements tagged <strong>Evidence</strong> cite the study behind them: oral iron in the morning on an empty stomach, and calcium with meals as a phosphate binder or between meals as a calcium supplement. The sample prescriptions are fictional. Review the schedule before giving it to the patient.</p>
</section>
</main>
""" + FOOTER + FLOAT)


def category_index_page(groups: dict[str, list[dict]]) -> str:
    canonical = f"{SITE}/drugs/category/"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "@id": canonical, "url": canonical,
                         "name": "Drug classes · Drug Index", "dateModified": "__ISO__", "inLanguage": "en"}).replace("</", "<\\/")
    lis = "".join(f'<li data-n="{esc(c.lower())}"><a href="{cat_slug(c)}.html">{esc(c)}</a> <span class="dd-sub">{len(v):,} generic{"s" if len(v) != 1 else ""}</span></li>'
                  for c, v in sorted(groups.items(), key=lambda kv: kv[0].lower()))
    return (head("Drug classes · Renal Care Matters", f"Browse {len(groups):,} drug classes in the Philippine drug index.", canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode dd-index-page">\n' + header(True) + f"""
<section class="hero"><div class="container dd-hero-wide"><div class="hero-grid"><div class="hero-copy">
<div class="dd-crumb"><a href="/drugs/">Drug Index</a></div>
<div class="hero-tag">Drug Database · Clinicians</div>
<h1>Browse by drug class</h1>
<p class="hero-sub">{len(groups):,} classes. US FDA established pharmacologic class when a US label is available, otherwise the FDA Philippines category.</p>
<div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
</div></div></div></section>
<main class="container dd-wide" id="dd-cats">
<div class="dd-search"><label class="dd-hidden" for="dd-cq">Filter classes</label><input id="dd-cq" type="search" placeholder="Filter classes (e.g., calcium channel)" autocomplete="off"></div>
<ul class="dd-list" id="dd-catlist">{lis}</ul>
</main>
""" + FOOTER + FLOAT)


# ═════════════════════════════════════════════════════════════════════════════
# Change-aware writer
# ═════════════════════════════════════════════════════════════════════════════
_HASH_RE = re.compile(r'<meta name="rcm-content-hash" content="([0-9a-f]+)">')
_ISO_RE = re.compile(r'<meta property="article:modified_time" content="(\d{4}-\d{2}-\d{2})">')



# ═════════════════════════════════════════════════════════════════════════════
# Fingerprinted shared assets: /drugs/drugdb.<hash>.css and .js. A new name cannot be
# edge-cached with old content while a deploy propagates (that happened twice with ?v=),
# so the files can be cached for a year. Pages carry placeholders filled in finalize().
# ═════════════════════════════════════════════════════════════════════════════
_ASSETS = {}


def drugdb_assets() -> dict:
    if not _ASSETS:
        css, js = build_css(), DRUG_JS
        _ASSETS.update({
            "css": css, "js": js,
            "css_url": f"/drugs/drugdb.{hashlib.sha1(css.encode('utf-8')).hexdigest()[:10]}.css",
            "js_url": f"/drugs/drugdb.{hashlib.sha1(js.encode('utf-8')).hexdigest()[:10]}.js",
        })
    return _ASSETS


def fill_assets(text: str) -> str:
    a = drugdb_assets()
    return text.replace("__DRUGDB_CSS__", a["css_url"]).replace("__DRUGDB_JS__", a["js_url"])

KEEP_DATES = False   # --keep-dates: presentation-only rebuild keeps each page's "Last updated" date


def finalize(path: Path, template: str, today: dt.date, dry: bool, force_date: bool) -> str:
    """Fill hash/date placeholders. Keeps the previous date when content is unchanged.
    Returns 'new' | 'changed' | 'same'."""
    legacy = (template.replace("__DRUGDB_CSS__", f"/drugs/drugdb.css?v={ASSET_VERSION}")
              .replace("__DRUGDB_JS__", f"/drugs/drugdb.js?v={ASSET_VERSION}"))
    hashed = (legacy.replace(APP_HEAD, "").replace(f"?v={ASSET_VERSION}", f"?v={HASH_ASSET_VERSION}")
              .replace(APP_ICON_TAG, LEGACY_ICON_TAG))
    template = fill_assets(template)
    css_url = drugdb_assets()["css_url"]
    js_url = drugdb_assets()["js_url"]
    h = hashlib.sha1(hashed.encode("utf-8")).hexdigest()[:16]
    when, state = today, "new"
    if path.exists():
        with open(path, encoding="utf-8") as fh:
            headtxt = fh.read(4096)
        m, d = _HASH_RE.search(headtxt), _ISO_RE.search(headtxt)
        if m and m.group(1) == h and not force_date:
            # same content: rewrite only when the app tags or asset versions are missing, keeping the old date
            # (both fingerprinted asset URLs must be current: a JS-only change must still repoint the page,
            #  because the previous drugdb.<hash>.js is pruned)
            body_txt = None
            def _has(u):
                nonlocal body_txt
                if u in headtxt:
                    return True
                if body_txt is None:
                    body_txt = path.read_text(encoding="utf-8")
                return u in body_txt
            if APP_HEAD in headtxt and APP_ICON_TAG in headtxt and _has(css_url) and _has(js_url):
                return "same"
            if d:
                when = dt.date.fromisoformat(d.group(1))
            state = "chrome"
        else:
            state = "changed"
            if KEEP_DATES and d:          # layout-only rebuild: the clinical content did not change
                when = dt.date.fromisoformat(d.group(1))
    out = (template.replace("__HASH__", h).replace("__ISO__", when.isoformat()).replace("__DATE__", us_date(when)))
    if not dry:
        tmp = path.with_suffix(path.suffix + ".tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(out)
        os.replace(tmp, path)
    return state


def write_if_changed(path: Path, content: str, dry: bool) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    if not dry:
        path.write_text(content, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=str(REPO / "data" / "drugs"))
    ap.add_argument("--out-dir", default=str(REPO / "drugs"))
    ap.add_argument("--only", help="comma-separated slugs to (re)build; index and search index are still rebuilt")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--keep-dates", action="store_true",
                    help="layout/wording-of-presentation change only: rewrite pages but keep their Last updated dates")
    ap.add_argument("--no-prune", action="store_true", help="keep generated pages whose slug is no longer in the data")
    ap.add_argument("--as-of", help="override today's date (YYYY-MM-DD) for 'Last updated' and validity checks")
    ap.add_argument("--from-api-sample", metavar="FILE", help="derive a synthetic registry from a raw PH FDA API response")
    ap.add_argument("--build", action="store_true", help="with --from-api-sample: also generate pages")
    a = ap.parse_args()
    global KEEP_DATES
    KEEP_DATES = a.keep_dates

    data_dir, out_dir = Path(a.data_dir), Path(a.out_dir)
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    if a.from_api_sample:
        derive_from_api_sample(Path(a.from_api_sample), data_dir)
        if not a.build:
            return

    import time
    t0 = time.time()
    ctx = Ctx(data_dir, today)
    if not ctx.generics:
        sys.exit(f"No generics found in {data_dir}/generics.json")
    out_dir.mkdir(parents=True, exist_ok=True)
    da = drugdb_assets()
    write_if_changed(out_dir / "drugdb.css", da["css"], a.dry_run)
    write_if_changed(out_dir / "drugdb.js", da["js"], a.dry_run)
    write_if_changed(REPO / da["css_url"].lstrip("/"), da["css"], a.dry_run)
    write_if_changed(REPO / da["js_url"].lstrip("/"), da["js"], a.dry_run)
    if not a.dry_run:   # drop older fingerprinted copies (pages always reference the current pair)
        for f in list(out_dir.glob("drugdb.*.css")) + list(out_dir.glob("drugdb.*.js")):
            if "/drugs/" + f.name not in (da["css_url"], da["js_url"]):
                f.unlink()
    write_if_changed(out_dir / "app.webmanifest", json.dumps(APP_MANIFEST, ensure_ascii=False, indent=1) + "\n", a.dry_run)
    write_if_changed(out_dir / "sw.js", build_sw(), a.dry_run)
    finalize(out_dir / "offline.html", offline_page(), today, a.dry_run, False)

    only = set(s.strip() for s in a.only.split(",")) if a.only else None
    stats = defaultdict(int)
    entries, extras = [], []
    for slug in sorted(ctx.generics):
        g = ctx.generics[slug]
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
            print(f"  ! skipping unsafe slug {slug!r}", file=sys.stderr)
            continue
        if not ctx.by_slug.get(slug):
            stats["no-products"] += 1
            continue
        if only is not None and slug not in only:
            e, x = index_entry(slug, g, ctx)
        else:
            html_, e, x = page_for(slug, g, ctx)
            stats[finalize(out_dir / f"{slug}.html", html_, today, a.dry_run, False)] += 1
        entries.append(e)
        extras.append(x)

    entries.sort(key=lambda e: e["n"].lower())
    groups = category_groups(entries)
    write_if_changed(out_dir / "search-index.json", json.dumps(entries, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    write_if_changed(out_dir / "search-extra.json", json.dumps(extras, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    ixd, ixr = interactions_data(ctx, entries)
    ixjson = json.dumps(ixd, ensure_ascii=False, separators=(",", ":"))
    write_if_changed(out_dir / "interactions.json", ixjson, a.dry_run)
    ixv = hashlib.sha1(ixjson.encode("utf-8")).hexdigest()[:10]
    stats["ix-" + finalize(out_dir / "interactions.html", interactions_page(len(ixd["owners"]), len(ixd["rows"])),
                           today, a.dry_run, False)] += 1
    print(f"  interaction checker: {len(ixd['rows'])} rows from {len(ixd['owners'])} drugs; "
          f"{ixr['matched']} matched to drugs or classes, {ixr['nondrug']} food/lab/procedure, {len(ixr['unmatched'])} other")
    msjson = json.dumps(scheduler_data(ctx, ixd), ensure_ascii=False, separators=(",", ":"))
    write_if_changed(out_dir / "med-scheduler.json", msjson, a.dry_run)
    stats["ms-" + finalize(out_dir / "med-scheduler.html", scheduler_page(), today, a.dry_run, False)] += 1
    bcore, bbrands = browse_data(entries, groups, ctx)
    write_if_changed(out_dir / "browse.json", json.dumps(bcore, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    write_if_changed(out_dir / "browse-brands.json", json.dumps(bbrands, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    stats["index-" + finalize(out_dir / "index.html", index_page(entries, ctx, len(groups), offline_sizes(offline_manifest(out_dir))),
                              today, a.dry_run, False)] += 1
    cdir = out_dir / "category"
    cdir.mkdir(exist_ok=True)
    stats["catindex-" + finalize(cdir / "index.html", category_index_page(groups), today, a.dry_run, False)] += 1
    cat_keep = {"index"}
    for c, items in groups.items():
        cs = cat_slug(c)
        cat_keep.add(cs)
        stats["cat-" + finalize(cdir / f"{cs}.html", category_page(c, items), today, a.dry_run, False)] += 1

    if not a.no_prune and only is None:
        keep = {e["s"] for e in entries} | {"index", "offline", "interactions", "med-scheduler"}
        for d, kp in ((out_dir, keep), (cdir, cat_keep)):
            for f in d.glob("*.html"):
                if f.stem in kp:
                    continue
                with open(f, encoding="utf-8") as fh:
                    if f'content="{GENERATOR_TAG}"' in fh.read(2048):
                        stats["pruned"] += 1
                        if not a.dry_run:
                            f.unlink()

    if only is None or (out_dir / "offline-manifest.json").exists():   # last, so every page's final hash is listed
        write_if_changed(out_dir / "offline-manifest.json", json.dumps(offline_manifest(out_dir), separators=(",", ":")), a.dry_run)

    print(f"{len(ctx.products):,} products · {len(entries):,} generic pages · "
          + " · ".join(f"{k}: {v}" for k, v in sorted(stats.items()))
          + f" · {time.time() - t0:.1f}s" + (" (dry run)" if a.dry_run else ""))
    cs_ = getattr(ctx, "comp_stats", {})
    if cs_:
        print(f"  component cross-reference on {len(cs_):,} combination pages "
              f"({sum(1 for n, k in cs_.values() if k):,} with an approved single-agent kidney strip)")


if __name__ == "__main__":
    main()
