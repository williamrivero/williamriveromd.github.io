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
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent
SITE = "https://renalcarematters.com"
GENERATOR_TAG = "generate_drug_pages.py"
FDA_VERIFY_URL = "https://verification.fda.gov.ph"
OG_IMAGE = f"{SITE}/images/hero-cat-pharmacology.png"
FONTS = ("https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&amp;"
         "family=Inter:wght@500;600;700;800&amp;family=Nunito+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap")
ASSET_VERSION = "1"   # bump when drugdb.css / drugdb.js change shape (cache-busting query)

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


def classify(c: str) -> str:
    """Normalize the many registry spellings to Rx / OTC / HR (or the raw text)."""
    t = ws(c).lower()
    if not t:
        return ""
    if "household" in t or "hone remedy" in t or "(hr)" in t:
        return "HR"
    if "otc" in t or "over-the" in t or "over the" in t:
        return "OTC"
    if "rx" in t or "prescri" in t:
        return "Rx"
    return ws(c)


CLASS_LABEL = {"Rx": "Prescription (Rx)", "OTC": "Over-the-counter (OTC)", "HR": "Household remedy (HR)"}


def brand_list(products) -> list[str]:
    """Distinct brand names, case-insensitive, sorted; keeps the most common spelling."""
    seen: dict[str, dict[str, int]] = {}
    for p in products:
        b = ws(p.get("brand_name"))
        if b:
            seen.setdefault(b.lower(), {}).setdefault(b, 0)
            seen[b.lower()][b] += 1
    return [max(v.items(), key=lambda kv: (kv[1], kv[0]))[0] for _, v in sorted(seen.items())]


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
.dd-alpha { display: flex; flex-wrap: wrap; gap: 6px; margin: 16px 0 6px; }
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
.dd-hidden { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.dd-letter.dd-kempty, .dd-letter.dd-hidden { display: none !important; }
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
table.dd-kidney-table { width: 100%; border-collapse: collapse; font-size: 14px; background: var(--white); border-radius: 10px; overflow: hidden; }
.dd-kidney-table th { text-align: left; width: 34%; padding: 10px 14px; color: #0e4a50; font-weight: 700; background: #e1f2f1; border-bottom: 1px solid #cfe6e6; vertical-align: top; }
.dd-kidney-table td { padding: 10px 14px; color: var(--text-mid); border-bottom: 1px solid #cfe6e6; }
.dd-kidney-table tr:last-child th, .dd-kidney-table tr:last-child td { border-bottom: 0; }
.dd-kidney-label { background: var(--white); border: 1px solid #cfe6e6; border-radius: 10px; padding: 6px 16px 8px; max-height: 420px; overflow: auto; }
.dd-kidney-label p { font-size: 14px; color: var(--text-mid); margin: 8px 0; white-space: pre-line; text-align: left; }
.dd-kidney-src { font-size: 11.5px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #0e4a50; margin-top: 8px; }
.dd-kidney .dd-note { margin-top: 10px; }
.dd-kidney-pending { font-size: 13.5px; font-weight: 600; color: #0e4a50; margin: 10px 0 0; }
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
  .dd-toolbar, .dd-alpha, .dd-search, .float-controls, .print-btn, .scroll-top-btn, .nav-strip { display: none !important; }
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
html[data-theme="dark"] .dd-placeholder { background: #141c2a; border-color: #4a5a72; }
html[data-theme="dark"] .dd-alpha button { background: #1a2535; color: #dbe6f5; border-color: #3a4a62; }
html[data-theme="dark"] .dd-alpha button[aria-pressed=true] { background: #dbe6f5; color: #0f1520; border-color: #dbe6f5; }
html[data-theme="dark"] .dd-letter h2 { color: #eef2fb; border-color: #2a3548; }
html[data-theme="dark"] ul.dd-list li { border-color: #2a3548; }
html[data-theme="dark"] mark.dd-hl { background: #5c4a00; color: #fff; }
html[data-theme="dark"] .dd-attrib, html[data-theme="dark"] .dd-acc-body { color: var(--text-mid); }
html[data-theme="dark"] .disclaimer a, html[data-theme="dark"] .dd-acc-body a, html[data-theme="dark"] .dd-kidney a,
html[data-theme="dark"] .dd-note a { color: #7fd3da; }
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
}

/* ── Drug Index: A–Z filter + brand/generic search over search-index.json ── */
var idx=document.getElementById('dd-index');
if(idx){
  var letters=Array.prototype.slice.call(document.querySelectorAll('.dd-letter'));
  var alpha=document.getElementById('dd-alpha'), sq=document.getElementById('dd-sq'),
      res=document.getElementById('dd-results'), info=document.getElementById('dd-sinfo'), data=null, loading=null;
  function setLetter(L){
    Array.prototype.forEach.call(alpha.querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===L?'true':'false');});
    letters.forEach(function(s){s.hidden=!(L==='all'||s.getAttribute('data-l')===L);});
  }
  alpha.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(!b||b.disabled)return;
    if(sq.value){sq.value='';search();}
    setLetter(b.getAttribute('data-l'));
    try{history.replaceState(null,'',b.getAttribute('data-l')==='all'?location.pathname:'#letter-'+b.getAttribute('data-l'));}catch(e){}
  });
  var h=(location.hash.match(/^#letter-([a-z0])$/i)||[])[1]; if(h)setLetter(h.toLowerCase());
  function load(){
    if(!loading)loading=fetch(idx.getAttribute('data-src')).then(function(r){return r.json();}).then(function(j){
      data=j.map(function(d){return {s:d.s,n:d.n,c:d.c||'',k:d.k||0,b:d.b||[],nn:norm(d.n),nb:(d.b||[]).map(norm)};});
    }).catch(function(){info.textContent='Search is unavailable right now. Use the A–Z list below.';});
    return loading;
  }
  function hl(text,t){var i=text.toLowerCase().indexOf(t);if(!t||i<0)return escH(text);return escH(text.slice(0,i))+'<mark class="dd-hl">'+escH(text.slice(i,i+t.length))+'</mark>'+escH(text.slice(i+t.length));}
  function escH(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  var timer=null, KB=(document.querySelector('.dd-kbadge')||{outerHTML:''}).outerHTML;
  function search(){
    var raw=sq.value.trim(), t=norm(raw);
    if(!t){res.hidden=true;res.innerHTML='';info.textContent='';letters.forEach(function(s){s.classList.remove('dd-hidden');});alpha.classList.remove('dd-hidden');return;}
    load().then(function(){
      if(!data)return;
      var out=[];
      var konlyOn=konly&&konly.checked;
      data.forEach(function(d){
        if(konlyOn&&!d.k)return;
        var score=0, brand=null;
        if(d.nn===t)score=100; else if(d.nn.indexOf(t)===0)score=80; else if((' '+d.nn).indexOf(' '+t)>=0)score=60; else if(d.nn.indexOf(t)>=0)score=40;
        for(var i=0;i<d.nb.length;i++){var b=d.nb[i],s=0;
          if(b===t)s=95; else if(b.indexOf(t)===0)s=75; else if((' '+b).indexOf(' '+t)>=0)s=55; else if(b.indexOf(t)>=0)s=35;
          if(s>score){score=s;brand=d.b[i];}}
        if(score)out.push({d:d,score:score,brand:brand});
      });
      out.sort(function(a,b){return b.score-a.score||a.d.n.localeCompare(b.d.n);});
      var shown=out.slice(0,150), tl=raw.toLowerCase();
      res.innerHTML='<ul class="dd-list">'+shown.map(function(o){
        var d=o.d;
        return '<li><a href="'+encodeURIComponent(d.s)+'.html">'+(o.brand?'<span class="dd-res-brand">'+hl(o.brand,tl)+'</span> → '+escH(d.n):hl(d.n,tl))+'</a>'+(d.k?KB:'')+
          (d.c?'<span class="dd-sub">'+escH(d.c)+'</span>':'')+'</li>';}).join('')+'</ul>';
      res.hidden=false;
      info.textContent=out.length?(out.length>150?'Showing the top 150 of '+out.length.toLocaleString('en-US')+' matches':out.length+(out.length===1?' match':' matches')):'No generic or brand matches “'+raw+'”.';
      letters.forEach(function(s){s.classList.add('dd-hidden');}); alpha.classList.add('dd-hidden');
    });
  }
  var konly=document.getElementById('dd-konly');
  function applyK(){var on=konly&&konly.checked;
    Array.prototype.forEach.call(document.querySelectorAll('.dd-letter li'),function(li){li.hidden=on&&!li.hasAttribute('data-k');});
    letters.forEach(function(s){s.classList.toggle('dd-kempty',on&&!s.querySelector('li[data-k]'));});
    if(sq.value)search();}
  if(konly)konly.addEventListener('change',applyK);
  sq.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(search,120);});
  sq.addEventListener('focus',load,{once:true});
  if(sq.value)search();
}
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
    ("Use in specific populations", ["use_in_specific_populations"]),
]


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
    return [p for p in products if not ws(p.get("registration_number")).upper().startswith("VR-")]


class Ctx:
    def __init__(self, data_dir: Path, today: dt.date):
        self.data_dir, self.today = data_dir, today
        self.generics = load_json(data_dir / "generics.json", {}) or {}
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

    def label(self, slug):
        return load_json(self.labels_dir / f"{slug}.json") if self.labels_dir.is_dir() else None

    def renal(self, slug):
        return load_json(self.renal_dir / f"{slug}.json") if self.renal_dir.is_dir() else None


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


def head(title, desc, canonical, jsonld, content_hash, keywords="") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script>try{{if(localStorage.getItem('wgmr-dark')==='1')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}</script>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{f'<meta name="keywords" content="{esc(keywords)}">' if keywords else ''}
<meta name="robots" content="index, follow">
<meta name="generator" content="{GENERATOR_TAG}">
<meta name="rcm-content-hash" content="{content_hash}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0f1e33">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Renal Care Matters">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:alt" content="Renal Care Matters Drug Database">
<meta property="og:locale" content="en_PH">
<meta property="article:modified_time" content="__ISO__">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet"/>
<link rel="stylesheet" href="/drugs/drugdb.css?v={ASSET_VERSION}">
<script type="application/ld+json">{jsonld}</script>
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
<script src="/drugs/drugdb.js?v=""" + ASSET_VERSION + """" defer></script>
</body>
</html>
"""

EXT_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'


# ═════════════════════════════════════════════════════════════════════════════
# Drug page sections
# ═════════════════════════════════════════════════════════════════════════════
def product_sort_key(p):
    b = ws(p.get("brand_name")).lower()
    return (b == "", b, ws(p.get("dosage_strength_form")).lower(), ws(p.get("registration_number")))


def render_products(slug, g, products, today) -> str:
    rows, classes = [], {}
    for p in sorted(products, key=product_sort_key):
        c = classify(p.get("classification"))
        classes[c] = classes.get(c, 0) + 1
        exp = parse_date(p.get("expiry_date"))
        past = bool(exp and exp < today)
        brand = ws(p.get("brand_name")) or "(no brand name)"
        reg_name = ws(p.get("generic_name"))
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
            + (f'<span class="dd-sub">{esc(reg_name)}</span>' if reg_name else "") + "</div></td>"
            f'<td data-label="Strength &amp; form"><div>{esc(ws(p.get("dosage_strength_form")))}'
            + (f'<span class="dd-sub">{esc(ws(p.get("packaging")))}</span>' if ws(p.get("packaging")) else "") + "</div></td>"
            f'<td data-label="Class" data-sort="{esc(c)}"><div><span class="dd-tag {esc(c) if c in CLASS_LABEL else ""}" '
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
    heads = ["Brand", "Strength &amp; form", "Class", "Manufacturer / country", "Distributor", "Reg. no.", "Valid until", "Package insert"]
    th = "".join(f'<th scope="col"><button type="button">{h}</button></th>' if h != "Package insert"
                 else f'<th scope="col"><span style="display:block;padding:10px 12px">{h}</span></th>' for h in heads)
    return f"""
<section class="section" id="products">
<div class="section-tag">Philippine products</div>
<h2>Registered products in the Philippines</h2>
<p class="dd-lead">{n:,} product{'s' if n != 1 else ''} registered with the Food and Drug Administration (FDA) Philippines list
{esc(g['name'])} as the generic name. Registration status changes; confirm a product's current status on the FDA portal before relying on it.</p>
<p><a class="dd-btn" href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">Verify on PH FDA portal {EXT_ICON}</a></p>
<div class="dd-toolbar no-print" role="search">
<label class="dd-hidden" for="dd-q">Filter products</label>
<input id="dd-q" type="search" placeholder="Filter by brand, strength, manufacturer, or registration no." autocomplete="off">
{f'<label class="dd-hidden" for="dd-class">Classification</label><select id="dd-class"><option value="">All classifications</option>{opts}</select>' if len(classes) > 1 else ''}
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
<p class="dd-note" style="margin-top:10px">Source: FDA Philippines product registration database. "Valid until" is the registration validity date
listed by the FDA; a past date may mean a renewal is pending. Package insert links point to files published by the FDA.</p>
</section>
"""


def render_label(slug, g, label) -> str:
    head_ = """
<section class="section" id="label">
<div class="section-tag">Prescribing information</div>
<h2>Prescribing information (US FDA label)</h2>
"""
    if not label:
        return head_ + """<div class="dd-placeholder">Label not yet available. US prescribing information for this generic has not been
added to the database yet. Check the Philippine package insert in the product table above.</div>
</section>
"""
    if isinstance(label.get("labels"), list) and label["labels"]:
        label = label["labels"][0]
    secs = label_sections(label)
    of = label.get("openfda") if isinstance(label.get("openfda"), dict) else {}
    set_id = ws(label.get("set_id") or (of.get("spl_set_id") or [""])[0] if isinstance(of.get("spl_set_id"), list) else label.get("set_id"))
    ver = ws(label.get("version"))
    vdate = label.get("version_date") or label.get("effective_date") or label.get("effective_time")
    vdate_s = us_date_str(vdate) if vdate else ""
    title = ws(label.get("title") or label.get("spl_title") or "")
    url = safe_url(label.get("url")) or (f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={set_id}" if set_id else "")
    src = ws(label.get("source")) or "DailyMed/openFDA"
    attrib = (f'<div class="dd-attrib"><strong>Source:</strong> US FDA-approved label via {esc(src)}'
              + (f', set ID <a href="{esc(url)}" rel="noopener" target="_blank">{esc(set_id)}</a>' if set_id and url else (f", set ID {esc(set_id)}" if set_id else ""))
              + (f", version {esc(ver)}" if ver else "")
              + (f", version date {esc(vdate_s)}" if vdate_s else "") + "."
              + (f" Label: {esc(title)}." if title else "")
              + " Text is reproduced verbatim; renal-impairment text appears in the Kidney dosing panel above. <strong>Philippine-approved indications may differ: check the PH package insert.</strong></div>")
    accs, first = [], True
    used = set()
    for heading, keys in LABEL_SECTIONS:
        if heading == "Use in specific populations" and "Pregnancy" in used:
            continue
        body = ""
        for k in keys:
            if secs.get(k):
                body = render_label_value(secs[k])
                if body:
                    break
        if not body:
            continue
        used.add(heading)
        boxed = heading == "Boxed warning"
        open_ = " open" if (boxed or first) else ""
        if not boxed:
            first = False
        accs.append(f'<details class="dd-acc{" dd-boxed" if boxed else ""}"{open_}><summary>{esc(heading)}</summary>'
                    f'<div class="dd-acc-body">{body}</div></details>')
    if not accs:
        return head_ + attrib + '<div class="dd-placeholder">Label not yet available for the sections shown here.</div>\n</section>\n'
    return head_ + attrib + "\n" + "\n".join(accs) + "\n</section>\n"


KIDNEY_ICON = ('<svg class="dd-kidney-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 3C5.4 3 3 6.6 3 11.2 3 16.6 5.6 21 9 21'
               'c2.3 0 3.4-1.7 3.4-3.6 0-1.6-.9-2.5-.9-4.1 0-1.4 1.4-1.9 1.4-3.6 0-1.6-1.1-2.3-1.1-3.6C11.8 4.4 10.6 3 8.5 3z"/>'
               '<path d="M15.5 3c3.1 0 5.5 3.6 5.5 8.2 0 5.4-2.6 9.8-6 9.8"/><path d="M12.5 12h3.5"/></svg>')
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


def render_kidney_panel(label, renal) -> str:
    head_ = ('<section class="dd-kidney" id="kidney-dosing" aria-labelledby="kidney-h">\n'
             f'<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">Kidney dosing · CKD and dialysis</div>'
             '<h2 id="kidney-h">Kidney dosing</h2></div></div>\n')
    if renal_approved(renal):
        rows = []
        for b in renal.get("bands") or []:
            if isinstance(b, dict) and (b.get("range") or b.get("recommendation")):
                rng = ws(b.get("range"))
                if rng and not re.search(r"egfr|crcl|gfr|clearance", rng, re.I):
                    rng = f"eGFR/CrCl {rng}"
                rows.append((rng, b.get("recommendation")))
        for key, lab in (("hd", "Hemodialysis"), ("pd", "Peritoneal dialysis"), ("crrt", "CRRT"),
                         ("dialyzable", "Dialyzable?"), ("monitoring", "Nephrotoxicity / kidney monitoring")):
            v = renal.get(key)
            if v in (None, "", []):
                continue
            if isinstance(v, bool):
                v = "Yes" if v else "No"
            if isinstance(v, list):
                v = "; ".join(map(ws, v))
            rows.append((lab, v))
        trs = "".join(f'<tr><th scope="row">{esc(a)}</th><td>{esc(b)}</td></tr>' for a, b in rows)
        out = [head_]
        if renal.get("summary"):
            out.append(f'<p class="dd-kidney-sum">{esc(renal["summary"])}</p>')
        if trs:
            out.append(f'<table class="dd-kidney-table"><caption class="dd-hidden">Kidney dosing by kidney function and dialysis modality</caption><tbody>{trs}</tbody></table>')
        srcs = []
        for r in renal.get("sources") or renal.get("references") or []:
            if isinstance(r, dict):
                doi, url = ws(r.get("doi")), safe_url(r.get("url"))
                link = f"https://doi.org/{doi}" if doi else url
                srcs.append(f'<li>{esc(r.get("citation") or r.get("title") or "")}'
                            + (f' <a href="{esc(link)}" rel="noopener" target="_blank">{esc(link)}</a>' if link else "") + "</li>")
            elif ws(r):
                srcs.append(f"<li>{esc(r)}</li>")
        if srcs:
            out.append('<details class="dd-acc"><summary>Sources</summary><div class="dd-acc-body"><ol>' + "".join(srcs) + "</ol></div></details>")
        by, on = ws(renal.get("reviewed_by")), us_date_str(renal.get("reviewed_date") or renal.get("reviewed_on"))
        out.append('<p class="dd-note">renalcarematters.com guidance'
                   + (f", reviewed by {esc(by)}" if by else "") + (f" on {esc(on)}" if on else "")
                   + ". Use with the product's package insert and the patient's current kidney function.</p>")
        return "\n".join(out) + "\n</section>\n"
    # No approved guidance: verbatim US label text (if any) + neutral note. Never invent dosing.
    body, which = label_renal_excerpt(label)
    out = [head_]
    if body:
        lab = label["labels"][0] if isinstance(label.get("labels"), list) and label["labels"] else label
        set_id = ws(lab.get("set_id"))
        vdate = us_date_str(lab.get("version_date") or lab.get("effective_date") or lab.get("effective_time"))
        out.append(f'<div class="dd-kidney-label"><div class="dd-kidney-src">From the US FDA label · {esc(which)}</div>{body}</div>')
        out.append('<p class="dd-note">Verbatim text from the US FDA-approved label via DailyMed/openFDA'
                   + (f", set ID {esc(set_id)}" if set_id else "") + (f", version date {esc(vdate)}" if vdate else "")
                   + ". Philippine-approved labeling may differ: check the PH package insert.</p>")
    else:
        out.append('<p class="dd-note">No kidney-specific text is available from the US label for this generic yet. '
                   'Check the Philippine package insert in the product table below.</p>')
    out.append('<p class="dd-kidney-pending">Kidney-specific guidance from renalcarematters.com: in preparation.</p>')
    return "\n".join(out) + "\n</section>\n"


def _entries(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def render_price_block(slug, g, ctx: Ctx) -> str:
    parts = []
    # Reference prices (e.g. DPRI)
    pe = [e for e in _entries(ctx.prices.get(slug)) if isinstance(e, dict)]
    if pe:
        src = ws(pe[0].get("source") or ctx.price_meta.get("source")) or "Reference price list"
        asof = us_date_str(pe[0].get("as_of") or ctx.price_meta.get("as_of"))
        surl = safe_url(pe[0].get("source_url") or ctx.price_meta.get("source_url"))
        trs = "".join(f'<tr><td>{esc(e.get("product") or e.get("description") or e.get("strength_form") or "")}</td>'
                      f'<td>{esc(peso(e.get("price")))}</td><td>{esc(e.get("unit") or "")}</td></tr>' for e in pe)
        parts.append('<h3>Reference prices</h3><div class="table-wrap"><table class="drug-table"><thead><tr><th>Product / strength</th>'
                     f'<th>Price</th><th>Unit</th></tr></thead><tbody>{trs}</tbody></table></div>'
                     f'<p class="dd-note">Source: {f"<a href={chr(34)}{esc(surl)}{chr(34)} rel=noopener target=_blank>{esc(src)}</a>" if surl else esc(src)}'
                     f'{", as of " + esc(asof) if asof else ""}.</p>')
    # Formulary
    pnf = ctx.pnf.get(slug)
    if isinstance(pnf, dict) and (pnf.get("listed", True)):
        rows = []
        for k, lab in (("edition", "Edition"), ("section", "Section"), ("category", "Category"), ("dosage_forms", "Listed forms"),
                       ("restrictions", "Restrictions"), ("remarks", "Remarks"), ("philhealth", "PhilHealth")):
            v = pnf.get(k)
            if v in (None, "", []):
                continue
            if isinstance(v, bool):
                v = "Yes" if v else "No"
            if isinstance(v, list):
                v = "; ".join(map(ws, v))
            rows.append(f"<tr><td>{lab}</td><td>{esc(v)}</td></tr>")
        src = ws(pnf.get("source") or ctx.pnf_meta.get("source")) or "Philippine National Formulary"
        asof = us_date_str(pnf.get("as_of") or ctx.pnf_meta.get("as_of"))
        parts.append('<h3>Philippine National Formulary</h3><p>Listed in the Philippine National Formulary (PNF).</p>'
                     + (f'<div class="table-wrap"><table class="drug-table"><tbody>{"".join(rows)}</tbody></table></div>' if rows else "")
                     + f'<p class="dd-note">Source: {esc(src)}{", as of " + esc(asof) if asof else ""}.</p>')
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


DISCLAIMER = """
<section class="section" id="disclaimer">
<div class="disclaimer" role="note"><strong>For health professionals.</strong> This page is a reference compiled from public
regulatory sources for licensed health professionals in the Philippines. Verify every product detail against the current
Philippine package insert and the FDA Philippines registration record. Information here is not a substitute for clinical
judgment and does not replace the prescribing information approved for the specific product you dispense or prescribe.
<br><br>Last updated: <time datetime="__ISO__">__DATE__</time>.</div>
</section>
"""


def page_for(slug: str, g: dict, ctx: Ctx) -> tuple[str, dict]:
    products = ctx.by_slug.get(slug, [])
    name = ws(g.get("name")) or slug
    cats = []
    for c in (g.get("categories") or []):
        c = ws(c)
        if c and c.lower().rstrip(".") not in {x.lower().rstrip(".") for x in cats}:
            cats.append(c.rstrip("."))
    cat = cats[0] if cats else ""
    classes = {classify(p.get("classification")) for p in products} - {""}
    brands = brand_list(products)
    vat_n = sum(1 for p in products if p.get("vat_exempt"))
    label = ctx.label(slug)
    renal = ctx.renal(slug)
    pnf = ctx.pnf.get(slug)

    chips = []
    if classes == {"Rx"}:
        chips.append('<span class="dd-chip dd-rx">Prescription only (Rx)</span>')
    elif classes == {"OTC"}:
        chips.append('<span class="dd-chip dd-otc">Over-the-counter (OTC)</span>')
    elif classes:
        chips.append(f'<span class="dd-chip">{esc(" · ".join(sorted(classes)))} products</span>')
    kc = kidney_chip(renal)
    if kc:
        chips.insert(0, f'<span class="dd-chip dd-kchip">{KIDNEY_ICON}{esc(kc)}</span>')
    chips.append(f'<span class="dd-chip">{len(products):,} PH product{"s" if len(products) != 1 else ""}</span>')
    chips.append(f'<span class="dd-chip">{len(brands):,} brand name{"s" if len(brands) != 1 else ""}</span>')
    if isinstance(pnf, dict) and pnf.get("listed", True):
        chips.append('<span class="dd-chip dd-good">PNF-listed</span>')
        if pnf.get("philhealth") is True:
            chips.append('<span class="dd-chip dd-good">PhilHealth-covered</span>')
    if vat_n:
        chips.append(f'<span class="dd-chip dd-good">VAT-exempt{"" if vat_n == len(products) else " (some products)"}</span>')

    ingredients = [ws(i) for i in (g.get("ingredients") or []) if ws(i)]
    combo = len(ingredients) > 1
    sub = (f"{esc(' / '.join(cats[:2]))}{' and others' if len(cats) > 2 else ''}." if cats else "") + (" Fixed-dose combination." if combo else "")
    price_html = render_price_block(slug, g, ctx)
    kidney_html = render_kidney_panel(label, renal)
    pills = [("#kidney-dosing", "Kidney dosing"), ("#products", "Philippine products"), ("#label", "Prescribing information")]
    if price_html:
        pills.append(("#price", "Price &amp; availability"))
    pills.append(("#disclaimer", "Disclaimer"))

    canonical = f"{SITE}/drugs/{slug}.html"
    rxstat = "https://schema.org/PrescriptionOnly" if classes == {"Rx"} else ("https://schema.org/OTC" if classes and "Rx" not in classes else None)
    drug = {"@type": "Drug", "name": name, "nonProprietaryName": name, "url": canonical}
    if cat:
        drug["drugClass"] = {"@type": "DrugClass", "name": cat}
    if ingredients:
        drug["activeIngredient"] = ", ".join(ingredients)
    if rxstat:
        drug["prescriptionStatus"] = rxstat
    if brands:
        drug["alternateName"] = brands[:25]
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "MedicalWebPage", "@id": canonical, "url": canonical, "name": f"{name}: Philippine products and prescribing information",
         "dateModified": "__ISO__", "inLanguage": "en", "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"},
         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE,
                       "logo": {"@type": "ImageObject", "url": f"{SITE}/android-chrome-512x512.png"}},
         "about": {"@id": canonical + "#drug"}},
        dict(drug, **{"@id": canonical + "#drug"})]}, ensure_ascii=False).replace("</", "<\\/")

    title = f"{name}: Philippine Brands, Products & Prescribing Information"
    if len(title) > 95:
        title = f"{name[:60].rstrip()}…: PH Products & Prescribing Info"
    brand_txt = ", ".join(brands[:6]) + ("…" if len(brands) > 6 else "")
    desc = (f"{name}{' (' + cat + ')' if cat else ''}: {len(products):,} FDA Philippines-registered products"
            + (f" including {brand_txt}" if brands else "") + ". Registration numbers, manufacturers, package inserts, and US FDA label text.")
    body = (head(title, desc[:300], canonical, jsonld, "__HASH__", keywords=", ".join([name] + brands[:20]))
            + '<body class="physician-mode single-mode">\n' + header(False)
            + f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a> › {esc(name[:1].upper())}</div>
        <div class="hero-tag">Drug Database · Clinicians</div>
        <h1>{esc(name)}</h1>
        <p class="hero-sub">{sub}</p>
        <div class="dd-chips">{''.join(chips)}</div>
        <div class="hero-meta">
<span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span>
<span><strong>Audience:</strong> Licensed health professionals</span>
</div>
      </div>
    </div>
  </div>
</section>

<nav class="nav-strip" aria-label="On this page"><div class="nav-pills">{''.join(f'<a class="nav-pill" href="{h}">{t}</a>' for h, t in pills)}</div></nav>

<main>
<div class="container">
{kidney_html}
</div>
<div class="container dd-wide">
{render_products(slug, g, products, ctx.today)}
</div>
<div class="container">
{render_label(slug, g, label)}
{price_html}
{DISCLAIMER}
</div>
</main>
""" + FOOTER + FLOAT)
    entry = {"s": slug, "n": name, "b": brands, "c": cat}
    if renal_approved(renal):
        entry["k"] = 1
    return body, entry


# ═════════════════════════════════════════════════════════════════════════════
# Index page
# ═════════════════════════════════════════════════════════════════════════════
def letter_of(name: str) -> str:
    c = (name or "?")[:1].lower()
    return c if "a" <= c <= "z" else "0"


KIDNEY_BADGE = ('<span class="dd-kbadge" title="Has approved kidney dosing guidance">' + KIDNEY_ICON
                + '<span class="dd-hidden">Kidney dosing guidance</span></span>')


def index_page(entries: list[dict], ctx: Ctx) -> str:
    groups = defaultdict(list)
    for e in sorted(entries, key=lambda e: e["n"].lower()):
        groups[letter_of(e["n"])].append(e)
    letters = ["0"] + [chr(c) for c in range(ord("a"), ord("z") + 1)]
    btns = '<button type="button" data-l="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-l="{l}" aria-pressed="false"{"" if groups.get(l) else " disabled"} '
        f'aria-label="{"Names starting with a number or symbol" if l == "0" else "Letter " + l.upper()}">{"#" if l == "0" else l.upper()}</button>'
        for l in letters)
    secs = []
    for l in letters:
        if not groups.get(l):
            continue
        lis = "".join(
            f'<li{" data-k=" + chr(34) + "1" + chr(34) if e.get("k") else ""}><a href="{esc(e["s"])}.html">{esc(e["n"])}</a>'
            + (KIDNEY_BADGE if e.get("k") else "")
            + (f'<span class="dd-sub">{esc(e["c"])}' + (f' · {esc(", ".join(e["b"][:3]))}{"…" if len(e["b"]) > 3 else ""}' if e["b"] else "") + "</span>"
               if (e["c"] or e["b"]) else "") + "</li>" for e in groups[l])
        secs.append(f'<section class="dd-letter" id="letter-{l}" data-l="{l}"><h2>{"#" if l == "0" else l.upper()}</h2>'
                    f'<ul class="dd-list">{lis}</ul></section>')
    n_products = len(ctx.products)
    canonical = f"{SITE}/drugs/"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "@id": canonical, "url": canonical,
                         "name": "Drug Index · Renal Care Matters", "dateModified": "__ISO__", "inLanguage": "en",
                         "audience": {"@type": "MedicalAudience", "audienceType": "Clinician"},
                         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE}}).replace("</", "<\\/")
    desc = (f"Search {len(entries):,} generics and {n_products:,} FDA Philippines-registered drug products by brand or generic name, "
            "with registration details, package inserts, and US FDA prescribing information.")
    return (head("Drug Index · Renal Care Matters", desc, canonical, jsonld, "__HASH__")
            + '<body class="physician-mode single-mode">\n' + header(True) + f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="hero-tag">Drug Database · Clinicians</div>
        <h1>Drug Index</h1>
        <p class="hero-sub">Every drug product registered with the Food and Drug Administration (FDA) Philippines, grouped by generic name.
Search by brand or generic; each page lists the Philippine products and the US FDA prescribing information.</p>
        <div class="dd-chips"><span class="dd-chip">{len(entries):,} generics</span><span class="dd-chip">{n_products:,} PH products</span></div>
        <div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
      </div>
    </div>
  </div>
</section>
<main class="container dd-wide" id="dd-index" data-src="/drugs/search-index.json">
<div class="dd-search" role="search">
<label class="dd-hidden" for="dd-sq">Search by brand or generic name</label>
<input id="dd-sq" type="search" placeholder="Search a brand or generic name (e.g., Norvasc, amlodipine)" autocomplete="off" spellcheck="false">
</div>
<label class="dd-check dd-kfilter"><input id="dd-konly" type="checkbox"{"" if any(e.get("k") for e in entries) else " disabled"}> {KIDNEY_ICON} Has kidney dosing guidance ({sum(1 for e in entries if e.get("k")):,})</label>
<p class="dd-note" id="dd-sinfo" aria-live="polite"></p>
<div class="dd-results" id="dd-results" hidden></div>
<nav class="dd-alpha" id="dd-alpha" aria-label="Filter by first letter">{btns}</nav>
{''.join(secs)}
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Product data come from the FDA Philippines registration
database and may lag behind the official record; verify on <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verification.fda.gov.ph</a>
and the current Philippine package insert. Not a substitute for clinical judgment.</div>
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
    h = hashlib.sha1(template.encode("utf-8")).hexdigest()[:16]
    when, state = today, "new"
    if path.exists():
        with open(path, encoding="utf-8") as fh:
            headtxt = fh.read(4096)
        m, d = _HASH_RE.search(headtxt), _ISO_RE.search(headtxt)
        if m and m.group(1) == h and not force_date:
            return "same"
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

    only = set(s.strip() for s in a.only.split(",")) if a.only else None
    stats = defaultdict(int)
    entries = []
    for slug in sorted(ctx.generics):
        g = ctx.generics[slug]
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
            print(f"  ! skipping unsafe slug {slug!r}", file=sys.stderr)
            continue
        if not ctx.by_slug.get(slug):
            stats["no-products"] += 1
            continue
        if only is not None and slug not in only:
            products = ctx.by_slug[slug]
            entries.append({"s": slug, "n": ws(g.get("name")) or slug,
                            "b": brand_list(products),
                            "c": ws((g.get("categories") or [""])[0])})
            if renal_approved(ctx.renal(slug)):
                entries[-1]["k"] = 1
            continue
        html_, entry = page_for(slug, g, ctx)
        entries.append(entry)
        stats[finalize(out_dir / f"{slug}.html", html_, today, a.dry_run, False)] += 1

    # search index (compact, one object per generic)
    si = json.dumps(sorted(entries, key=lambda e: e["n"].lower()), ensure_ascii=False, separators=(",", ":"))
    write_if_changed(out_dir / "search-index.json", si, a.dry_run)
    stats["index-" + finalize(out_dir / "index.html", index_page(entries, ctx), today, a.dry_run, False)] += 1

    if not a.no_prune and only is None:
        keep = {e["s"] for e in entries} | {"index"}
        for f in out_dir.glob("*.html"):
            if f.stem in keep:
                continue
            with open(f, encoding="utf-8") as fh:
                if f'content="{GENERATOR_TAG}"' in fh.read(2048):
                    stats["pruned"] += 1
                    if not a.dry_run:
                        f.unlink()

    print(f"{len(ctx.products):,} products · {len(entries):,} generic pages · "
          + " · ".join(f"{k}: {v}" for k, v in sorted(stats.items()))
          + f" · {time.time() - t0:.1f}s" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
