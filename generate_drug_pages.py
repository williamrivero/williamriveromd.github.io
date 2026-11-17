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
ASSET_VERSION = "23"   # bump when drugdb.css / drugdb.js change shape (cache-busting query)
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
@media print { .dd-app, .dd-app-chip { display: none !important; } html.dd-offline body::after { display: none; } }
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
         k:document.getElementById('dd-f-k'),p:document.getElementById('dd-f-p'),h:document.getElementById('dd-f-h'),l:document.getElementById('dd-f-l'),e:document.getElementById('dd-f-e'),
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
  function drugFacets(){return !!(F.c.value||F.r.value||F.f.value||F.k.checked||F.p.checked||F.h.checked||F.l.checked||(F.e&&F.e.checked));}
  function facetPass(d){
    if(F.t&&(F.t.value==='s'||F.t.value==='m'))return false;
    if(F.c.value&&d.c!==F.c.value)return false;
    if(F.r.value&&!((d.r||0)&(+F.r.value)))return false;
    if(F.f.value&&(d.f||[]).indexOf(F.f.value)<0)return false;
    return !(F.k.checked&&!d.k)&&!(F.p.checked&&!d.p)&&!(F.h.checked&&!d.h)&&!(F.l.checked&&!d.l)&&!(F.e&&F.e.checked&&!d.e);
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
    if(F.k.checked&&!d.k)return false; if(F.p.checked&&!d.p)return false; if(F.h.checked&&!d.h)return false; if(F.l.checked&&!d.l)return false; if(F.e&&F.e.checked&&!d.e)return false;
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
    if(d.k)o.push('<span class="dd-tag KD">Kidney dosing</span>');if(d.l)o.push('<span class="dd-tag US">US label</span>');if(d.e)o.push('<span class="dd-tag US">EU SmPC</span>');return o.join(' ');}
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
      info.textContent=out.length?(out.length>200?'Showing the first 200 of '+out.length.toLocaleString('en-US')+' matches':out.length.toLocaleString('en-US')+(out.length===1?' match':' matches')):'No generic, brand, class, product or supplement matches.';
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
var box=document.getElementById('dd-app');
function standalone(){return (window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true;}
function ios(){return /iphone|ipad|ipod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);}
function q(n){return box?box.querySelector('[data-app="'+n+'"]'):null;}
function showInstall(){
  var hint=q('hint'),btn=q('install');if(!hint)return;
  if(standalone()){btn.hidden=true;hint.textContent='You are using the installed Drug Index app.';
    ['iossteps','iosnote'].forEach(function(k){var e=q(k);if(e)e.hidden=true;});return;}
  if(deferred&&!ios()){btn.hidden=false;hint.textContent='Adds a Drug Index icon to your home screen or desktop. It opens full screen and works offline.';return;}
  btn.hidden=true;
  if(ios()){hint.textContent='On iPhone or iPad, add the Drug Index to your Home Screen:';var o=q('iossteps');if(o)o.hidden=false;
    var n=q('iosnote');if(n)n.hidden=false;}
}
window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();deferred=e;showInstall();});
window.addEventListener('appinstalled',function(){deferred=null;showInstall();});
if(!box)return;
showInstall();
q('install').addEventListener('click',function(){if(!deferred)return;deferred.prompt();
  (deferred.userChoice||Promise.resolve()).then(function(){deferred=null;showInstall();});});

var btns=Array.prototype.slice.call(box.querySelectorAll('[data-app="dl"]')),rm=q('rm'),st=q('status'),bar=q('bar');
if(!('caches' in window)||!('serviceWorker' in navigator)){q('off').hidden=true;return;}
var MAN='/drugs/offline-manifest.json',busy=false,cur=null;
var LABEL={all:'Download all drugs',kidney:'Kidney-dosing drugs only'};
function rec(){try{return JSON.parse(localStorage.getItem(KEY)||'null');}catch(e){return null;}}
function setRec(r){try{localStorage.setItem(KEY,JSON.stringify(r));}catch(e){}}
function fmtDate(ms){try{return new Date(ms).toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'});}catch(e){return '';}}
function num(n){return Number(n).toLocaleString('en-US');}
function manifest(){return fetch(MAN,{cache:'no-cache'}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json();});}
function status(){
  var r=rec();
  btns.forEach(function(b){b.disabled=busy;b.textContent=LABEL[b.getAttribute('data-set')];});
  rm.disabled=busy;
  if(!r||r.v!==2){st.textContent=r&&r.n?'Saved pages from an earlier download are kept; download again to include every drug.':'Nothing downloaded yet.';rm.hidden=!(r&&r.n);return;}
  rm.hidden=false;
  var what=r.set==='all'?'All drugs':'Kidney-dosing drugs';
  var msg=r.done?what+' saved on this device ('+num(r.n)+' pages, '+fmtDate(r.at)+').'
               :what+': download interrupted at '+num(r.n)+' of '+num(r.total)+' pages. Tap the button again to resume.';
  var b=box.querySelector('[data-app="dl"][data-set="'+r.set+'"]');
  if(cur&&r.done){if(cur.h!==r.h){msg+=' Updates are available.';if(b)b.textContent='Update '+(r.set==='all'?'all drugs':'kidney-dosing drugs');}
                  else if(b)b.textContent=(r.set==='all'?'All drugs':'Kidney-dosing drugs')+': up to date';}
  else if(!r.done&&b)b.textContent='Resume download';
  st.textContent=msg;
  if(navigator.storage&&navigator.storage.estimate)navigator.storage.estimate().then(function(x){
    if(x&&x.usage&&!busy)st.textContent=msg+' Using about '+num(Math.max(1,Math.round(x.usage/1e6)))+' MB on this device.';}).catch(function(){});
}
status();
if(navigator.onLine!==false)manifest().then(function(m){cur=m;if(!busy)status();},function(){});

function run(set){
  if(busy)return;
  if(navigator.onLine===false){st.textContent='You are offline. Connect to the internet to download.';return;}
  busy=true;status();bar.hidden=false;bar.value=0;st.textContent='Checking what needs downloading…';
  var lock=null;try{if(navigator.wakeLock)navigator.wakeLock.request('screen').then(function(l){lock=l;},function(){});}catch(e){}
  if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(function(){});
  var m,c,want={},have={},todo=[],ok=0,failed=0,total=0;
  manifest().then(function(x){
    m=x;cur=x;
    m.pages.forEach(function(p){if(set==='all'||p[3])want[location.origin+'/drugs/'+p[0]]=p;});
    return caches.open(SAVED);
  }).then(function(cache){
    c=cache;return c.keys();
  }).then(function(keys){                       // what is already saved, and at which version
    return Promise.all(keys.map(function(k){
      if(!want[k.url])return c.delete(k);         // not in this set (or no longer published)
      return c.match(k).then(function(res){have[k.url]=res&&res.headers.get('X-RCM-Hash');});
    }));
  }).then(function(){
    Object.keys(want).forEach(function(u){if(have[u]!==want[u][1])todo.push(u);});
    total=Object.keys(want).length;ok=total-todo.length;
    var need=todo.reduce(function(a,u){return a+want[u][2];},0);
    var room=(navigator.storage&&navigator.storage.estimate)?navigator.storage.estimate():Promise.resolve(null);
    return room.then(function(e){
      if(e&&e.quota&&e.quota-e.usage<need*1.15)throw {msg:'Not enough free storage for this download (about '+num(Math.ceil(need/1e6))+' MB needed). Free some space, or download the kidney-dosing drugs only.'};
      bar.max=total;bar.value=ok;
      if(!todo.length)return;
      var i=0;
      function save(){setRec({v:2,set:set,n:ok,total:total,at:Date.now(),h:m.h,done:false});}
      function next(){
        if(i>=todo.length)return Promise.resolve();
        var u=todo[i++],p=want[u];
        return fetch(u,{credentials:'same-origin',cache:'no-cache'}).then(function(res){
          if(!res.ok)throw new Error(res.status);
          return res.blob().then(function(bl){return c.put(u,new Response(bl,{headers:{'Content-Type':'text/html; charset=utf-8','X-RCM-Hash':p[1]}}));});
        }).then(function(){ok++;if(ok%40===0)save();},function(){failed++;})
          .then(function(){bar.value=ok;st.textContent='Saving '+num(ok)+' of '+num(total)+' pages… keep this page open.';return next();});
      }
      save();
      return Promise.all([next(),next(),next(),next(),next(),next()]);
    });
  }).then(function(){
    setRec({v:2,set:set,n:ok,total:total,at:Date.now(),h:failed?'':m.h,done:!failed});
    busy=false;bar.hidden=true;status();
    if(failed)st.textContent=num(failed)+' pages could not be saved. Tap the button again on a better connection to finish.';
  }).catch(function(err){
    busy=false;bar.hidden=true;status();
    st.textContent=(err&&err.msg)||'The download stopped. Check your connection and tap the button again; pages already saved are kept.';
  }).then(function(){try{if(lock)lock.release();}catch(e){}});
}
btns.forEach(function(b){b.addEventListener('click',function(){run(b.getAttribute('data-set'));});});
rm.addEventListener('click',function(){if(busy)return;caches.delete(SAVED).then(function(){try{localStorage.removeItem(KEY);}catch(e){}status();});});
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
                out.append(f"<p>{esc(para.strip())}</p>")
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
<link rel="apple-touch-icon" sizes="180x180" href="/images/app/drug-index-180.png">
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
<link rel="stylesheet" href="/drugs/drugdb.css?v={ASSET_VERSION}">
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
<script src="/drugs/drugdb.js?v=""" + ASSET_VERSION + """" defer></script>
</body>
</html>
"""


# ═════════════════════════════════════════════════════════════════════════════
# Installable app (PWA): manifest, service worker, offline page
# ═════════════════════════════════════════════════════════════════════════════
APP_MARK = '<link rel="manifest" href="/drugs/app.webmanifest">'
APP_ICON_TAG = '<link rel="apple-touch-icon" sizes="180x180" href="/images/app/drug-index-180.png">'   # iPhone home-screen icon (full-bleed; iOS rounds the corners)
LEGACY_ICON_TAG = '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'   # what page hashes were computed with
APP_HEAD = (APP_MARK + '\n<meta name="mobile-web-app-capable" content="yes">\n'
            '<meta name="apple-mobile-web-app-capable" content="yes">\n'
            '<meta name="apple-mobile-web-app-title" content="Drug Index">\n'
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
            "<script>if('serviceWorker'in navigator)addEventListener('load',function(){navigator.serviceWorker"
            ".register('/drugs/sw.js',{scope:'/drugs/'}).catch(function(){});});</script>\n")

APP_MANIFEST = {
    "id": "/drugs/",
    "name": "Drug Index · Renal Care Matters",
    "short_name": "Drug Index",
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
        {"src": "/images/app/drug-index-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/drug-index-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/drug-index-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/drug-index-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/drug-index-180.png", "sizes": "180x180", "type": "image/png", "purpose": "any"},
    ],
    "shortcuts": [
        {"name": "Kidney dosing", "short_name": "Kidney dosing", "url": "/drugs/?view=kidney",
         "icons": [{"src": "/images/app/drug-index-192.png", "sizes": "192x192", "type": "image/png"}]},
        {"name": "Food supplements & medical nutrition", "short_name": "Supplements", "url": "/drugs/supplements/",
         "icons": [{"src": "/images/app/drug-index-192.png", "sizes": "192x192", "type": "image/png"}]},
    ],
}

SW_JS = r"""/* Generated by generate_drug_pages.py; do not edit. Offline support for the Drug Index app (/drugs/). */
'use strict';
var V='__V__';
var SHELL='rcm-drugs-shell-'+V,PAGES='rcm-drugs-pages',SAVED='rcm-drugs-saved',DATA='rcm-drugs-data',ASSETS='rcm-drugs-assets';
var SHELL_URLS=__SHELL__;            // must all load, or the install is retried later
var OPTIONAL_SHELL=__OPTIONAL__;     // nice to have offline
var CORE_PAGES=['/drugs/','/drugs/offline','/drugs/supplements/'];
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
function nav(e){
  var key=pageKey(e.request.url);
  var net=fetch(e.request.url,{credentials:'same-origin'}).then(function(res){
    return clean(res).then(function(cr){
      if(res.ok&&(res.headers.get('content-type')||'').indexOf('text/html')>=0)keep(e,store(key,cr.clone()));
      return cr;});});
  return caches.match(key).then(function(hit){
    if(!hit)return net.catch(offline);
    keep(e,net.catch(function(){}));
    var slow=new Promise(function(r){setTimeout(function(){r(hit);},3500);});   // weak signal: show the saved copy
    return Promise.race([net.then(function(r){return r.ok?r:hit;},function(){return hit;}),slow]);
  });
}
function swr(e,name,max){var r=e.request;return caches.open(name).then(function(c){return c.match(r).then(function(hit){
  var net=fetch(r).then(function(res){if(res.ok){c.put(r,res.clone());if(max)trim(name,max);}return res;});
  if(hit){keep(e,net.catch(function(){}));return hit;}
  return net.catch(function(){return Response.error();});});});}
function cacheFirst(r){return caches.match(r).then(function(hit){return hit||fetch(r).then(function(res){
  if(res.ok){var c=res.clone();caches.open(SHELL).then(function(s){s.put(r,c);});}return res;},
  function(){return caches.match(r,{ignoreSearch:true}).then(function(h){return h||Response.error();});});});}   // offline: any saved version
function networkFirst(e,name){var r=e.request;return fetch(r).then(function(res){
  if(res.ok){var c=res.clone();keep(e,caches.open(name).then(function(ca){return ca.put(r,c);}));}return res;},
  function(){return caches.match(r).then(function(h){return h||Response.error();});});}

self.addEventListener('fetch',function(e){
  var r=e.request;if(r.method!=='GET')return;
  var u=new URL(r.url);
  if(r.mode==='navigate'){if(u.origin===self.location.origin&&u.pathname.indexOf('/drugs/')===0)e.respondWith(nav(e));return;}
  if(u.origin===self.location.origin){
    if(u.pathname==='/drugs/offline-manifest.json')return e.respondWith(networkFirst(e,DATA));   // must be current for updates
    if(u.pathname.indexOf('/drugs/')===0&&/\.json$/.test(u.pathname))return e.respondWith(swr(e,DATA,0));
    if(/[?&]v=/.test(u.search))return e.respondWith(cacheFirst(r));
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
    shell = [f"/drugs/drugdb.css?v={ASSET_VERSION}", f"/drugs/drugdb.js?v={ASSET_VERSION}"]
    optional = ["/assets/drug-hero.js?v=3"] + ([f"/drugs/supplements/supp.css?v={sv}", f"/drugs/supplements/supp.js?v={sv}"] if sv else [])
    data = ["/drugs/search-index.json", "/drugs/search-extra.json", "/drugs/supplements/search-index.json",
            f"/drugs/browse.json?v={ASSET_VERSION}", f"/drugs/browse-brands.json?v={ASSET_VERSION}"]
    assets = ["/assets/share-buttons.js", "/drugs/app.webmanifest", "/images/app/drug-index-192.png", "/favicon.ico",
              "/favicon-32x32.png", "/images/app/drug-index-180.png"]
    js = (SW_JS.replace("__SHELL__", json.dumps(shell)).replace("__OPTIONAL__", json.dumps(optional))
          .replace("__DATA__", json.dumps(data)).replace("__ASSETS__", json.dumps(assets)))
    v = hashlib.sha1((js + offline_page()).encode("utf-8")).hexdigest()[:10]   # new offline page -> new worker
    return js.replace("__V__", v)



def offline_manifest(entries: list[dict], out_dir: Path) -> dict:
    """Pages the app can download for offline use: every generic page except high-confidence variant
    spellings (their products are on the main page). Hash = the page's content hash, so updates fetch
    only pages whose content changed."""
    pages = []
    for e in entries:
        if e.get("mh"):
            continue
        f = out_dir / f"{e['s']}.html"
        if not f.exists():
            continue
        with open(f, encoding="utf-8") as fh:
            m = _HASH_RE.search(fh.read(4096))
        pages.append([e["s"], m.group(1)[:10] if m else "", f.stat().st_size, 1 if (e.get("k") and not e.get("m")) else 0])
    h = hashlib.sha1(json.dumps(pages, separators=(",", ":")).encode("utf-8")).hexdigest()[:12]
    return {"v": 1, "h": h, "pages": pages}


def offline_sizes(man: dict) -> dict:
    """Rounded sizes for the index panel (stored size, and download size at ~25% after compression)."""
    def mb(rows):
        b = sum(r[2] for r in rows)
        return {"n": len(rows), "store": max(5, int(round(b / 1e6 / 5.0)) * 5), "dl": max(1, int(round(b * 0.25 / 1e6 / 5.0)) * 5)}
    rows = man.get("pages", [])
    return {"all": mb(rows), "kidney": mb([r for r in rows if r[3]])}

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
  all.forEach(function(ks){ks.forEach(function(r){var p=new URL(r.url).pathname,m=p.match(/^\\/drugs\\/(?:supplements\\/)?([a-z0-9][a-z0-9-]*)$/);
    if(!m||seen[p]||m[1]==='offline'||m[1]==='view'||m[1]==='index')return;seen[p]=1;
    var t=(!/supplements/.test(p)&&names[m[1]])||m[1].replace(/-/g,' ');items.push({p:p,t:t.charAt(0).toUpperCase()+t.slice(1),s:p.indexOf('/supplements/')>0});});});
  items.sort(function(a,b){return a.t.localeCompare(b.t);});
  N.textContent=items.length?items.length+' page'+(items.length===1?'':'s')+' available offline.':'No drug pages are saved yet. Open the Drug Index while online to save pages as you browse.';
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
        reviewed.append(f'Dosing, interaction, adverse-effect and monitoring summary{": reviewed by " + esc(by) if by else ""}'
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


_HEAD_WORD = r"(?:[A-Z][\w'’/&-]*|of|and|in|with|the|for|or|to|on|by|at|a|an|\([^)]{1,40}\))"


def split_numbered(text: str, num: str) -> tuple[str, list[tuple[str, str]]]:
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
        head = re.sub(r"\s+[A-Z]{3,}\b.*$", "", head).strip() or head
        words = head.split()
        if rest[:1].islower() and len(words) > 1:      # the last capitalized word starts the body sentence
            while len(words) > 1:
                w = words.pop()
                if w[:1].isupper():
                    break
        while len(words) > 1 and words[-1] in ("of", "and", "in", "with", "the", "for", "or", "to", "on", "by", "at", "a", "an"):
            words.pop()
        if len(words) > 1 and words[-1].lower() in {w.lower() for w in words[:-1]}:
            words.pop()
        head = " ".join(words) or after[:60]
        out.append((f"{m.group(1)} {head[:90]}", chunk))
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
        pre, subs = split_numbered(v, num)
        if not subs:
            return acc(title, render_label_value(v), aid=aid)
        html_ = f'<div class="dd-labgroup"{f" id={chr(34)}{aid}{chr(34)}" if aid else ""}><div class="dd-labgroup-h">{esc(title)} {LABEL_CHIP}</div>'
        if pre and len(pre) > 20:
            html_ += f'<div class="dd-labpre">{esc(pre if len(pre) < 1400 else pre[:1400].rsplit(" ", 1)[0] + " …")}</div>'
        html_ += "".join(f'<details class="dd-acc dd-acc-sm"><summary><span>{esc(h)}</span></summary>'
                         f'<div class="dd-acc-body"><p>{esc(c)}</p></div></details>' for h, c in subs)
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
                                                          ("max_dose", "Maximum dose")) if pr.get(k) not in (None, "", [])]
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
                ("disp", "Dispensing category"), ("kidney", "Kidney dosing"), ("pn", "Parenteral nutrition")]
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
    core = {"v": 1, "g": G, "class": cls, "area": areas, "disp": disp, "kidney": kid,
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
    off = off or {"all": {"n": 0, "store": 5, "dl": 5}, "kidney": {"n": 0, "store": 5, "dl": 5}}
    oa, ok_ = off["all"], off["kidney"]
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
        <div class="dd-chips"><span class="dd-chip">{len(entries):,} generics</span><span class="dd-chip">{n_products:,} PH products</span>
<a class="dd-chip" href="/drugs/category/">Browse {n_cats:,} drug classes</a>{supp_chip}<a class="dd-chip dd-app-chip no-print" href="#dd-app">Install app · use offline</a></div>
        <div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
    </div></div>
  </div>
</section>
<main class="container dd-wide" id="dd-index" data-src="/drugs/search-index.json" data-extra="/drugs/search-extra.json"{' data-supp="/drugs/supplements/search-index.json"' if supp_n else ''}>
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
<h2 id="dd-app-h">Use the Drug Index as an app</h2>
<div class="dd-app-grid">
<div class="dd-app-card">
<h3>Install on your phone or computer</h3>
<p data-app="hint">Add the Drug Index to your home screen from your browser menu (<strong>Install app</strong> or <strong>Add to Home Screen</strong>).
It opens full screen, like an app.</p>
<button type="button" class="dd-btn" data-app="install" hidden>Install the app</button>
<ol class="dd-app-ios" data-app="iossteps" hidden>
<li>Open this page in <strong>Safari</strong> (on iOS 16.4 or later, Chrome and Edge also work).</li>
<li>Tap the <strong>Share</strong> button <span aria-hidden="true">(the square with an arrow pointing up)</span>.</li>
<li>Scroll down and tap <strong>Add to Home Screen</strong>, then <strong>Add</strong>.</li>
<li>Open <strong>Drug Index</strong> from your Home Screen. It runs full screen, like an app.</li>
</ol>
</div>
<div class="dd-app-card" data-app="off">
<h3>Offline use</h3>
<p>Once loaded, search and the browse lists work without signal, and every drug page you open is kept on this device.
To have drug pages ready before you need them, download them:</p>
<div class="dd-app-opt"><button type="button" class="dd-btn" data-app="dl" data-set="all">Download all drugs</button>
<span class="dd-app-meta">{oa["n"]:,} drugs · about {oa["dl"]} MB to download, {oa["store"]} MB on the device</span></div>
<div class="dd-app-opt"><button type="button" class="dd-btn dd-btn-ghost" data-app="dl" data-set="kidney">Kidney-dosing drugs only</button>
<span class="dd-app-meta">{ok_["n"]:,} drugs with approved kidney dosing · about {ok_["dl"]} MB to download</span></div>
<p class="dd-app-warn" data-app="iosnote" hidden><strong>iPhone and iPad:</strong> add the Drug Index to your Home Screen first, then open it
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


def finalize(path: Path, template: str, today: dt.date, dry: bool, force_date: bool) -> str:
    """Fill hash/date placeholders. Keeps the previous date when content is unchanged.
    Returns 'new' | 'changed' | 'same'."""
    hashed = (template.replace(APP_HEAD, "").replace(f"?v={ASSET_VERSION}", f"?v={HASH_ASSET_VERSION}")
              .replace(APP_ICON_TAG, LEGACY_ICON_TAG))
    h = hashlib.sha1(hashed.encode("utf-8")).hexdigest()[:16]
    when, state = today, "new"
    if path.exists():
        with open(path, encoding="utf-8") as fh:
            headtxt = fh.read(4096)
        m, d = _HASH_RE.search(headtxt), _ISO_RE.search(headtxt)
        if m and m.group(1) == h and not force_date:
            # same content: rewrite only when the app tags or asset versions are missing, keeping the old date
            if APP_MARK in headtxt and APP_ICON_TAG in headtxt and (f"?v={ASSET_VERSION}" in headtxt
                                        or f"?v={ASSET_VERSION}" in path.read_text(encoding="utf-8")):
                return "same"
            if d:
                when = dt.date.fromisoformat(d.group(1))
            state = "chrome"
        else:
            state = "changed"
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
    ap.add_argument("--no-prune", action="store_true", help="keep generated pages whose slug is no longer in the data")
    ap.add_argument("--as-of", help="override today's date (YYYY-MM-DD) for 'Last updated' and validity checks")
    ap.add_argument("--from-api-sample", metavar="FILE", help="derive a synthetic registry from a raw PH FDA API response")
    ap.add_argument("--build", action="store_true", help="with --from-api-sample: also generate pages")
    a = ap.parse_args()

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
    write_if_changed(out_dir / "drugdb.css", build_css(), a.dry_run)
    write_if_changed(out_dir / "drugdb.js", DRUG_JS, a.dry_run)
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
    bcore, bbrands = browse_data(entries, groups, ctx)
    write_if_changed(out_dir / "browse.json", json.dumps(bcore, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    write_if_changed(out_dir / "browse-brands.json", json.dumps(bbrands, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    man = offline_manifest(entries, out_dir)
    write_if_changed(out_dir / "offline-manifest.json", json.dumps(man, separators=(",", ":")), a.dry_run)
    stats["index-" + finalize(out_dir / "index.html", index_page(entries, ctx, len(groups), offline_sizes(man)), today, a.dry_run, False)] += 1
    cdir = out_dir / "category"
    cdir.mkdir(exist_ok=True)
    stats["catindex-" + finalize(cdir / "index.html", category_index_page(groups), today, a.dry_run, False)] += 1
    cat_keep = {"index"}
    for c, items in groups.items():
        cs = cat_slug(c)
        cat_keep.add(cs)
        stats["cat-" + finalize(cdir / f"{cs}.html", category_page(c, items), today, a.dry_run, False)] += 1

    if not a.no_prune and only is None:
        keep = {e["s"] for e in entries} | {"index", "offline"}
        for d, kp in ((out_dir, keep), (cdir, cat_keep)):
            for f in d.glob("*.html"):
                if f.stem in kp:
                    continue
                with open(f, encoding="utf-8") as fh:
                    if f'content="{GENERATOR_TAG}"' in fh.read(2048):
                        stats["pruned"] += 1
                        if not a.dry_run:
                            f.unlink()

    print(f"{len(ctx.products):,} products · {len(entries):,} generic pages · "
          + " · ".join(f"{k}: {v}" for k, v in sorted(stats.items()))
          + f" · {time.time() - t0:.1f}s" + (" (dry run)" if a.dry_run else ""))
    cs_ = getattr(ctx, "comp_stats", {})
    if cs_:
        print(f"  component cross-reference on {len(cs_):,} combination pages "
              f"({sum(1 for n, k in cs_.values() if k):,} with an approved single-agent kidney strip)")


if __name__ == "__main__":
    main()
