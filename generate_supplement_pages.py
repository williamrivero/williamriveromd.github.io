#!/usr/bin/env python3
"""
generate_supplement_pages.py: Food Supplements section of the renalcarematters.com Drug Database.

Reads (under --data-dir, default data/drugs/):
  supplements.json                 brand index written by tools/drugdb/build_supplements.py
  supplements/<shard>.json         PH FDA food-supplement and FSMP registrations (FR numbers)
  supplement-notes/<slug>.json     optional; our kidney notes, rendered ONLY when review_status == "approved"
  generics.json                    drug generics, for cross-links to drug pages
Writes (under --out-dir, default drugs/supplements/):
  <brand-slug>.html                one page per brand (all of its registrations)
  index.html                       searchable Food Supplements index
  search-index.json                [{s, n, i[], co[], r[], cat[], f[], k?}], lazy-loaded here and by the Drug Index
  supp.css, supp.js                section styles and index search

Foods for special medical purposes (FSMP, type "fsmp": renal formulas such as Nepro, Kidneypro, Fresubin Renal and
Nephrisol, plus other medical nutrition) get their own banner, chips, a Variants table (LP/HP) for renal formulas and a
"Renal nutrition formulas" list on the index. Renal FSMP brands always get a static page.
Foods for special dietary use (FSDU, type "fsdu": e.g. Glucerna, Efione Nu Reno, Efione Nu Lopo) get their own banner and chip;
renal FSDU products join the renal list and always get a static page too.
Other food registrations (type "other": milk supplements, nutrition drinks, RUSF, snacks) get a neutral food-product banner and
chip, never the food-supplement banner. A brand with several types shows one banner and chip per type present, a per-registration
"Registered as" row, and a hero line from its most common type (ties: the type of the most recent registration).
The Kidney notes section renders only for kidney-marketed brands, renal formulas and brands with a supplement-notes file.

Registrations past their validity date (as of --as-of / today) or canceled are never rendered.
Shares the page chrome, hash-aware writer and drugdb.css/js with generate_drug_pages.py.

Usage:
  python3 generate_supplement_pages.py
  python3 generate_supplement_pages.py --as-of 2026-11-17 --dry-run
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import generate_drug_pages as gdp
from generate_drug_pages import (SITE, FDA_VERIFY_URL, GENERATOR_TAG, EXT_ICON, KIDNEY_ICON, FOOTER, FLOAT,
                                 esc, ws, header, head, finalize, write_if_changed, load_json, us_date_str, parse_date)

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / "tools" / "drugdb"))
from build_registry import ingredients_of, slug_of  # noqa: E402  (drug slug rule, shared contract)
from build_supplements import slugify  # noqa: E402
from build_related_guides import supp_keys  # noqa: E402  (same keys the related-guides builder scored)

SUPP_ASSET_VERSION = "5"
CAT_LABEL = {"probiotic": "Probiotic", "herbal/botanical": "Herbal / botanical", "vitamin/mineral": "Vitamin / mineral",
             "omega-3": "Omega-3", "amino acid/protein": "Amino acid / protein", "ketoanalogue": "Ketoanalogue",
             "fiber/prebiotic": "Fiber / prebiotic", "fsmp": "Medical nutrition (FSMP)", "fsdu": "Special dietary food (FSDU)",
             "food": "Other food registration", "other": "Other"}
FSMP_TAG_LABEL = {"renal": "Renal formula", "diabetes": "Diabetes", "high-protein": "High protein", "peptide": "Peptide-based",
                  "pediatric": "Infant / pediatric", "general": "General medical nutrition"}
VARIANT_LABEL = {"LP": "LP · lower protein, for CKD not on dialysis", "HP": "HP · higher protein, for dialysis"}
VARIANT_SHORT = {"LP": "Lower protein (LP)", "HP": "Higher protein (HP)"}
BANNER_FSMP = ('<div class="ds-banner ds-banner-fsmp" role="note"><strong>Registered with the Philippine FDA as a FOOD FOR SPECIAL MEDICAL '
               'PURPOSES</strong> — for the dietary management of patients under medical supervision. Use with a physician\'s or '
               'dietitian\'s guidance; it is a food, not a drug.</div>')
BANNER_FSDU = ('<div class="ds-banner ds-banner-fsmp ds-banner-fsdu" role="note"><strong>Registered with the Philippine FDA as a FOOD FOR '
               'SPECIAL DIETARY USE</strong> — a food formulated for a particular dietary need; not a medicine.</div>')
BANNER = ('<div class="ds-banner" role="note"><strong>Registered with the Philippine FDA as a FOOD SUPPLEMENT — no approved '
          'therapeutic claims.</strong> Not a substitute for prescribed treatment.</div>')
BANNER_OTHER = ('<div class="ds-banner ds-banner-food" role="note"><strong>Registered with the Philippine FDA as a food product</strong>; '
                'check the registration details for its stated use.</div>')
TYPE_LABEL = {"fsmp": "Food for special medical purposes (FSMP)", "fsdu": "Food for special dietary use (FSDU)",
              "supplement": "Food supplement", "other": "Other food registration"}

# Drug generics too vague to be a useful cross-link
VAGUE_SLUGS = {"minerals-vitamins", "minerals", "multivitamins", "amino-acids", "iron-vitamins", "phospholipids", "vitamins",
               "herbs", "calcium", "iron", "magnesium"}
# canonical supplement ingredient -> candidate drug slugs (the one with most PH products wins)
CROSS = {
    "Ketoanalogues of essential amino acids": ["alpha-ketoanalogues-essential-amino-acids", "ketoanalogues-essential-amino-acids",
                                               "essential-amino-acids-ketoanalogues", "essential-amino-acid-ketoanalogues"],
    "Diosmin": ["diosmin-hesperidin", "diosmin"],
    "Vitamin D3 (cholecalciferol)": ["cholecalciferol", "colecalciferol"],
    "Vitamin C": ["ascorbic-acid"],
    "N-acetylcysteine": ["acetylcysteine"],
    "Zinc": ["zinc"],
    "Milk thistle (Silybum marianum)": ["silymarin"],
    "Alpha-lipoic acid": ["thioctic-acid"],
    "Coenzyme Q10": ["ubidecarenone"],
    "Glutathione": ["glutathione"],
    "L-carnitine": ["levocarnitine", "l-carnitine"],
    "Vitamin B9 (folate)": ["folic-acid"],
    "Vitamin B12 (cobalamin)": ["mecobalamin", "cyanocobalamin", "methylcobalamin"],
    "Vitamin B1 (thiamine)": ["thiamine"],
    "Saccharomyces boulardii": ["saccharomyces-boulardii"],
    "Bacillus clausii": ["bacillus-clausii"],
    "Psyllium (Plantago ovata)": ["ispaghula"],
    "Omega-3 fatty acids (fish oil)": ["omega-3-acid-ethyl-esters", "omega-3-fatty-acids"],
}


def load_supplements(data_dir: Path):
    idx = load_json(data_dir / "supplements.json", {}) or {}
    products = []
    sdir = data_dir / "supplements"
    if sdir.is_dir():
        for f in sorted(sdir.glob("*.json")):
            if f.name.startswith("_"):
                continue
            products.extend(load_json(f, []) or [])
    return idx, products


def live(p, today) -> bool:
    if p.get("canceled"):
        return False
    v = parse_date(p.get("valid_until"))
    return v is None or v >= today


def notes_approved(n) -> bool:
    return isinstance(n, dict) and n.get("review_status") == "approved"


def is_fsmp(p) -> bool:
    return p.get("type") == "fsmp"


def is_fsdu(p) -> bool:
    return p.get("type") == "fsdu"


def is_med(p) -> bool:
    """A medical or special dietary food (FSMP or FSDU): registered use, no ingredient list."""
    return p.get("type") in ("fsmp", "fsdu")


def ptype(p) -> str:
    """fsmp | fsdu | supplement (a stated food supplement) | other (other food registration)."""
    t = p.get("type") or "supplement"
    return t if t in TYPE_LABEL else "supplement"


def is_supp(p) -> bool:
    return ptype(p) == "supplement"


def is_other(p) -> bool:
    return ptype(p) == "other"


def recency(p) -> str:
    return (p.get("decision_date") or "") + "|" + (p.get("valid_until") or "") + "|" + p.get("id", "")


def dominant_type(ps) -> str:
    """The brand's most common registration type; a tie goes to the type with the most recent registration."""
    c = Counter(ptype(p) for p in ps)
    top = max(c.values())
    tied = [t for t in c if c[t] == top]
    return max(tied, key=lambda t: max(recency(p) for p in ps if ptype(p) == t))


def banner_for(ps) -> str:
    f, d = any(is_fsmp(p) for p in ps), any(is_fsdu(p) for p in ps)
    s, o = any(is_supp(p) for p in ps), any(is_other(p) for p in ps)
    return ((BANNER_FSMP if f else "") + (BANNER_FSDU if d else "") + (BANNER if s else "")
            + (BANNER_OTHER if o else "")) or BANNER


def food_name(p) -> str:
    t = ws(p.get("product_name_clean") or p.get("product_name"))
    if not t.isupper():
        return t
    t = t[:1] + t[1:].lower()
    return re.sub(r"\(([a-z]{2,5}(?:-[a-z]{2,5})?)\)", lambda m: "(" + m.group(1).upper() + ")", t)  # keep (LNS-SQ), (RUSF)


def subtitle(ps) -> str:
    """Hero line from the brand's dominant registration type (ties: the most recent registration's type)."""
    dt_ = dominant_type(ps)
    tp = sorted((p for p in ps if ptype(p) == dt_), key=recency, reverse=True)
    if dt_ in ("fsmp", "fsdu"):
        return fsmp_summary(tp)
    if dt_ == "other":
        p = tp[0]
        return use_text(p) or food_name(p)
    ings = []
    for p in tp:
        for i in p.get("ingredients") or []:
            if i not in ings:
                ings.append(i)
    return ", ".join(ings[:6]) + ("…" if len(ings) > 6 else "")


def kidney_section_ok(ps, notes) -> bool:
    """Kidney notes section only for kidney-marketed brands, renal formulas, or brands with notes on file."""
    return bool(notes) or any(p.get("kidney_marketed") or p.get("renal_formula") for p in ps)


def use_text(p) -> str:
    """'For the dietary management of …' / 'For people on dialysis' as registered ('' if none)."""
    if p.get("use_label"):
        return p["use_label"]
    return ("For the dietary management of " + p["fsmp_use"]) if p.get("fsmp_use") else ""


def med_kind(ps) -> str:
    """Hero/description wording for an all-FSMP / all-FSDU / mixed medical-food brand."""
    f, d = any(is_fsmp(p) for p in ps), any(is_fsdu(p) for p in ps)
    return "fsmp" if f and not d else "fsdu" if d and not f else "both"


def fsmp_summary(ps) -> str:
    """One line for the hero: renal formula + variants, else the registered use."""
    fs = [p for p in ps if is_med(p)]
    vs = sorted({p["variant"] for p in fs if p.get("variant")})
    if any(p.get("renal_formula") for p in fs):
        if vs == ["HP", "LP"]:
            return "Renal nutrition formula: LP (lower protein, CKD not on dialysis) and HP (higher protein, dialysis) variants"
        if vs:
            return "Renal nutrition formula: " + VARIANT_LABEL[vs[0]].split(" · ", 1)[1].replace(", for", " formula for")
        uses = [use_text(p) for p in fs if use_text(p)]
        return "Renal nutrition formula" + (f": {uses[0][0].lower() + uses[0][1:]}" if uses else "")
    uses = [use_text(p) for p in fs if use_text(p)]
    k = med_kind(fs)
    lead = {"fsmp": "Medical nutrition", "fsdu": "Special dietary food", "both": "Medical and special dietary nutrition"}[k]
    if uses:
        u = Counter(uses).most_common(1)[0][0]
        return f"{lead}: {u[0].lower() + u[1:]}"
    return {"fsmp": "Medical nutrition (FSMP)", "fsdu": "Special dietary food (FSDU)", "both": "Medical nutrition (FSMP, FSDU)"}[k]


class SCtx:
    def __init__(self, data_dir: Path, out_dir: Path, today: dt.date):
        self.data_dir, self.today = data_dir, today
        self.index, prods = load_supplements(data_dir)
        self.by_brand: dict[str, list] = defaultdict(list)
        self.dropped = Counter()
        for p in prods:
            if live(p, today):
                self.by_brand[p["brand_slug"]].append(p)
            else:
                self.dropped["expired" if not p.get("canceled") else "canceled"] += 1
        self.generics = load_json(data_dir / "generics.json", {}) or {}
        self.related_guides = load_json(data_dir / "related_guides.json", {}) or {}   # tools/drugdb/build_related_guides.py
        drug_dir = out_dir.parent
        self.drug_pages = {f.stem for f in drug_dir.glob("*.html")} - {"index"}
        self.notes_dir = data_dir / "supplement-notes"
        # variant generic spellings -> main molecule page (tools/drugdb/build_aliases.py; high confidence only)
        al = load_json(data_dir / "aliases.json", {}) or {}
        self.alias_main = {v: e["main"] for v, e in al.items()
                           if isinstance(e, dict) and e.get("confidence") == "high" and e.get("main")}

    def notes(self, slug):
        return load_json(self.notes_dir / f"{slug}.json") if self.notes_dir.is_dir() else None

    def guides_for(self, slug, ps, limit=3) -> list:
        """Related guides for a brand: its own name in a guide (strongest), then its top ingredients and categories."""
        rg = self.related_guides
        best: dict[str, int] = {}
        for f, sc in (rg.get("supplement_brands") or {}).get(slug, []):
            best[f] = max(best.get(f, 0), sc + 1000)
        for k in supp_keys(ps):
            for f, sc in (rg.get("supplement_keys") or {}).get(k, []):
                best[f] = max(best.get(f, 0), sc)
        return [[f, sc] for f, sc in sorted(best.items(), key=lambda x: (-x[1], x[0]))[:limit]]

    def drug_ok(self, slug) -> bool:
        return slug in self.drug_pages and slug not in VAGUE_SLUGS

    def best(self, cands):
        ok = [c for c in cands if self.drug_ok(c)]
        return max(ok, key=lambda c: (self.generics.get(c, {}).get("products", 0), c)) if ok else None

    def drug_links(self, products) -> list[tuple[str, str, str]]:
        """[(slug, display name, why)] for drug pages that share this supplement's ingredients."""
        out, seen = [], set()
        for p in products:
            exact = slug_of(ingredients_of(p.get("ingredients_raw") or ""))
            exact = self.alias_main.get(exact, exact)
            if self.drug_ok(exact) and exact not in seen:
                seen.add(exact)
                out.append((exact, self.generics.get(exact, {}).get("name") or exact, "same ingredients"))
            ings = p.get("ingredients") or []
            for i in ings:
                if i == "Diosmin" and "Hesperidin" not in ings:
                    cands = ["diosmin"]
                else:
                    cands = CROSS.get(i, [])
                b = self.best([self.alias_main.get(c, c) for c in cands])
                if b and b not in seen:
                    seen.add(b)
                    out.append((b, self.generics.get(b, {}).get("name") or b, "contains " + i.split(" (")[0]))
        return out[:6]


# ─────────────────────────────────────────────────────────────────────────────
SUPP_CSS = r"""/* Generated by generate_supplement_pages.py: do not edit. */
.ds-banner { border: 2px solid #b45309; background: #fff7e6; color: #4a2800; border-radius: 12px; padding: 14px 18px;
  font-size: 15px; line-height: 1.55; margin: 0 0 22px; }
.ds-banner strong { color: #4a2800; }
.dd-chip.ds-chip-supp { color: #3d4656; background: #eceff3; border-color: rgba(61,70,86,.4); }
.dd-chip.ds-chip-kid { color: #4a2800; background: #fdf3dc; border-color: rgba(146,64,14,.4); }
.ds-ings { margin: 6px 0 0; padding-left: 20px; }
.ds-ings li { margin: 2px 0; }
.ds-raw { display: block; font-size: 12px; color: var(--text-muted); margin-top: 4px; }
.ds-reg { border: 1px solid var(--border); border-radius: 12px; padding: 14px 18px; margin: 0 0 14px; background: var(--white); }
.ds-reg h3 { font-family: 'Inter', sans-serif; font-size: 16px; margin: 0 0 8px; color: var(--text); }
.ds-dl { display: grid; grid-template-columns: max-content 1fr; gap: 4px 16px; margin: 10px 0 0; font-size: 14px; }
.ds-dl dt { font-weight: 700; color: var(--text-mid); }
.ds-dl dd { margin: 0; color: var(--text); overflow-wrap: anywhere; }
.ds-dl a { color: #1a6b72; font-weight: 600; }
.ds-notes { border: 1px solid rgba(14,74,80,.35); background: #f1f8f7; border-radius: 12px; padding: 16px 20px; }
.ds-notes h3 { font-family: 'Inter', sans-serif; font-size: 15px; margin: 14px 0 6px; color: #0e4a50; }
.ds-notes p, .ds-notes li { font-size: 14.5px; line-height: 1.6; color: var(--text); }
.ds-notes .ds-bottom { font-weight: 700; }
.ds-druglinks { list-style: none; padding: 0; margin: 0; }
.ds-druglinks li { padding: 6px 0; border-bottom: 1px solid var(--border); }
.ds-druglinks a { color: #1a6b72; font-weight: 700; text-decoration: none; }
.ds-druglinks .dd-sub { margin-left: 8px; }
.ds-facets { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin: 10px 0 4px; }
.ds-facets select { min-height: 40px; }
.ds-list li .dd-sub { display: block; font-size: 12.5px; color: var(--text-muted); font-weight: 400; }
.ds-tag-k { color: #4a2800; background: #fdf3dc; }
.ds-more { margin: 10px 0; }
.ds-banner-fsmp { border-color: #1a6b72; background: #eef7f7; color: #0b3a3f; }
.ds-banner-fsmp strong { color: #0b3a3f; }
.ds-banner-fsmp + .ds-banner { margin-top: -10px; }
.ds-banner-food { border-color: #5b6577; background: #f3f5f8; color: #1e2a38; }
.ds-banner-food strong { color: #1e2a38; }
.ds-banner + .ds-banner-food { margin-top: -10px; }
.dd-chip.ds-chip-fsmp { color: #0b3a3f; background: #e3f2f2; border-color: rgba(26,107,114,.45); }
.ds-tag-f { color: #0b3a3f; background: #e3f2f2; }
.ds-vtable { width: 100%; border-collapse: collapse; font-size: 14px; margin: 8px 0 4px; }
.ds-vtable th, .ds-vtable td { text-align: left; vertical-align: top; padding: 8px 10px; border-bottom: 1px solid var(--border); }
.ds-vtable th { font-weight: 700; color: var(--text-mid); background: var(--bg); }
.ds-vtable a { color: #1a6b72; font-weight: 600; white-space: nowrap; }
.ds-vwrap { overflow-x: auto; }
html[data-theme="dark"] .ds-banner { background: rgba(245,158,11,.12); border-color: #f59e0b; color: #fde7c2; }
html[data-theme="dark"] .ds-banner strong { color: #fff3dc; }
html[data-theme="dark"] .dd-chip.ds-chip-supp { color: #e5e9f0; background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.35); }
html[data-theme="dark"] .dd-chip.ds-chip-kid { color: #fde7c2; background: rgba(245,158,11,.14); border-color: rgba(245,158,11,.5); }
html[data-theme="dark"] .ds-reg { background: #1a2535; border-color: rgba(255,255,255,.14); }
html[data-theme="dark"] .ds-notes { background: rgba(43,168,176,.08); border-color: rgba(43,168,176,.4); }
html[data-theme="dark"] .ds-notes h3 { color: #a5f3fc; }
html[data-theme="dark"] .ds-dl a, html[data-theme="dark"] .ds-druglinks a { color: #7dd3d8; }
html[data-theme="dark"] .ds-raw { color: #9ba6b8; }
html[data-theme="dark"] .ds-banner-fsmp { background: rgba(43,168,176,.10); border-color: #2ba8b0; color: #d4f1f2; }
html[data-theme="dark"] .ds-banner-fsmp strong { color: #ecfbfb; }
html[data-theme="dark"] .ds-banner-food { background: rgba(255,255,255,.06); border-color: #8b96a8; color: #e5e9f0; }
html[data-theme="dark"] .ds-banner-food strong { color: #ffffff; }
html[data-theme="dark"] .dd-chip.ds-chip-fsmp { color: #c9f0f1; background: rgba(43,168,176,.14); border-color: rgba(43,168,176,.5); }
html[data-theme="dark"] .ds-tag-f { color: #c9f0f1; background: rgba(43,168,176,.16); }
html[data-theme="dark"] .ds-vtable th { background: #1a2535; color: #cbd3df; }
html[data-theme="dark"] .ds-vtable a { color: #7dd3d8; }
html[data-theme="dark"] .ds-tag-k { color: #fde7c2; background: rgba(245,158,11,.16); }
@media (max-width: 640px) { .ds-dl { grid-template-columns: 1fr; } .ds-dl dt { margin-top: 6px; }
  .ds-vtable thead { display: none; }
  .ds-vtable, .ds-vtable tbody, .ds-vtable tr, .ds-vtable th, .ds-vtable td { display: block; width: 100%; }
  .ds-vtable tr { border: 1px solid var(--border); border-radius: 10px; margin: 0 0 10px; overflow: hidden; }
  .ds-vtable th[scope="row"] { background: var(--bg); }
  .ds-vtable td { border-bottom: 0; padding: 6px 10px; }
  .ds-vtable td::before { content: attr(data-l); display: block; font-size: 12px; font-weight: 700; color: var(--text-mid); }
  .ds-vtable a { display: inline-block; margin: 0 8px 2px 0; } }
@media print { .ds-banner { border-width: 1px; } }
"""

SUPP_JS = r"""/* Generated by generate_supplement_pages.py: do not edit. */
(function(){
'use strict';
function href(d){return d.p?encodeURIComponent(d.s)+'.html':'view.html?b='+encodeURIComponent(d.s);}

function renderView(v){
  function escH(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  var MON=['January','February','March','April','May','June','July','August','September','October','November','December'];
  function usd(s){var m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(s||'');return m?MON[+m[2]-1]+' '+(+m[3])+', '+m[1]:'';}
  var CAT={'probiotic':'Probiotic','herbal/botanical':'Herbal / botanical','vitamin/mineral':'Vitamin / mineral','omega-3':'Omega-3',
    'amino acid/protein':'Amino acid / protein','ketoanalogue':'Ketoanalogue','fiber/prebiotic':'Fiber / prebiotic','fsmp':'Medical nutrition (FSMP)','fsdu':'Special dietary food (FSDU)','food':'Other food registration'};
  var b=(new URLSearchParams(location.search).get('b')||'').toLowerCase(), lead=document.getElementById('dsv-lead');
  function fail(msg){lead.innerHTML=msg+' Search the <a href="/drugs/supplements/">food supplements index</a>.';}
  if(!/^[a-z0-9][a-z0-9-]{0,79}$/.test(b)){fail('No brand was given.');return;}
  var RET={};try{RET=JSON.parse(v.getAttribute('data-retired')||'{}');}catch(e){}
  if(RET[b]){location.replace((v.getAttribute('data-static')||'').split(',').indexOf(RET[b])>=0?RET[b]+'.html':'view.html?b='+encodeURIComponent(RET[b]));return;}
  var split=(v.getAttribute('data-split')||'').split(',').filter(Boolean), c=/[a-z]/.test(b[0])?b[0]:'0';
  var shard=(split.indexOf(c)>=0)?c+(/[a-z0-9]/.test(b[1]||'')?b[1]:'0'):c, today=v.getAttribute('data-today')||'';
  fetch(v.getAttribute('data-base')+shard+'.json').then(function(r){if(!r.ok)throw 0;return r.json();}).then(function(all){
    var ps=all.filter(function(p){return p.brand_slug===b&&!p.canceled&&(!p.valid_until||!today||p.valid_until>=today);});
    if(!ps.length){fail('No current registration was found for this brand.');return;}
    ps.sort(function(x,y){return (y.valid_until||'').localeCompare(x.valid_until||'')||y.id.localeCompare(x.id);});
    var name=ps[0].brand, ings=[], cats=[], cos=[], kid=false, ren=false, TC={}, LAST={};
    var TL={fsmp:'Food for special medical purposes (FSMP)',fsdu:'Food for special dietary use (FSDU)',supplement:'Food supplement',other:'Other food registration'};
    function ty(p){return TL[p.type]?p.type:'supplement';}
    function rc(p){return (p.decision_date||'')+'|'+(p.valid_until||'')+'|'+p.id;}
    function ut(p){return p.use_label||(p.fsmp_use?'For the dietary management of '+p.fsmp_use:'');}
    function fn(p){var t=p.product_name_clean||p.product_name||'';return t===t.toUpperCase()?t.charAt(0)+t.slice(1).toLowerCase():t;}
    ps.forEach(function(p){var t=ty(p);TC[t]=(TC[t]||0)+1;if(!LAST[t]||rc(p)>LAST[t])LAST[t]=rc(p);
      if(t==='supplement')(p.ingredients||[]).forEach(function(i){if(ings.indexOf(i)<0)ings.push(i);});
      (p.categories||[]).forEach(function(x){if(cats.indexOf(x)<0&&x!=='other'&&x!=='fsmp'&&x!=='fsdu'&&x!=='food')cats.push(x);});
      if(p.renal_formula)ren=true; if(p.company&&cos.indexOf(p.company)<0)cos.push(p.company); if(p.kidney_marketed)kid=true;});
    /* dominant registration type: most common; a tie goes to the type with the most recent registration */
    var dom=Object.keys(TC).sort(function(x,y){return TC[y]-TC[x]||(LAST[y]>LAST[x]?1:-1);})[0];
    var nfs=TC.fsmp||0, nds=TC.fsdu||0, med=dom==='fsmp'||dom==='fsdu', allF=(nfs+nds)===ps.length;
    var tp=ps.filter(function(p){return ty(p)===dom;}).sort(function(x,y){return rc(y).localeCompare(rc(x));});
    document.getElementById('dsv-bf').hidden=!nfs; document.getElementById('dsv-bd').hidden=!nds;
    document.getElementById('dsv-bs').hidden=!TC.supplement; document.getElementById('dsv-bo').hidden=!TC.other;
    var mf=tp.filter(function(p){return p.type===dom;}), kl=nds&&!nfs?'special dietary food, FSDU':nfs&&!nds?'medical nutrition, FSMP':'medical nutrition, FSMP and FSDU';
    document.title=name+' ('+(med?kl:dom==='other'?'food product':'food supplement')+') · Renal Care Matters';
    document.getElementById('dsv-tag').textContent='Drug Database · '+(med?(nds&&!nfs?'Special dietary food (FSDU)':nfs&&!nds?'Medical nutrition (FSMP)':'Medical nutrition (FSMP, FSDU)'):dom==='other'?'Food product':'Food supplement');
    document.getElementById('dsv-name').textContent=name;
    var sub;
    if(med){var mu=[];mf.forEach(function(p){var u=ut(p);if(u&&mu.indexOf(u)<0)mu.push(u);});
      sub=(ren?'Renal nutrition formula':(dom==='fsdu'?'Special dietary food':'Medical nutrition'))+(mu.length?': '+mu[0].charAt(0).toLowerCase()+mu[0].slice(1):'');}
    else if(dom==='other')sub=ut(tp[0])||fn(tp[0]);
    else sub=ings.length?ings.slice(0,6).join(', ')+(ings.length>6?'…':''):'Ingredients not itemized in the FDA record.';
    document.getElementById('dsv-ings').textContent=sub;
    document.getElementById('dsv-co').textContent=cos.slice(0,3).join('; ')+(cos.length>3?'; and others':'')||'Not listed';
    document.getElementById('dsv-chips').innerHTML=(nfs?'<span class="dd-chip ds-chip-fsmp">Medical nutrition (FSMP)</span>':'')+(nds?'<span class="dd-chip ds-chip-fsmp">Special dietary food (FSDU)</span>':'')+
      (TC.supplement?'<span class="dd-chip ds-chip-supp">Food supplement</span>':'')+(TC.other?'<span class="dd-chip ds-chip-supp">Other food registration</span>':'')+
      (ren?'<span class="dd-chip ds-chip-kid">Renal formula</span>':'')+(kid?'<span class="dd-chip ds-chip-kid">Kidney-marketed</span>':'')+
      cats.map(function(x){return '<span class="dd-chip">'+escH(CAT[x]||x)+'</span>';}).join('')+'<span class="dd-chip">'+ps.length+' registration'+(ps.length===1?'':'s')+'</span>';
    /* kidney notes: only for kidney-marketed brands, renal formulas, or brands with notes on file */
    var hasN=(v.getAttribute('data-notes')||'').split(',').indexOf(b)>=0, showK=kid||ren||hasN;
    ['kidney-notes','dsv-kn-pill','dsv-kn-toc'].forEach(function(id){var el=document.getElementById(id);if(el)el.hidden=!showK;});
    var n=ps.length, ks=Object.keys(TC), SH={fsmp:'FSMP',fsdu:'FSDU',supplement:'food supplement',other:'other food registration'};
    lead.textContent=n+' current '+(allF?(nds&&!nfs?'FSDU':nfs&&!nds?'FSMP':'FSMP/FSDU')+' registration'+(n===1?'':'s'):ks.length===1?(dom==='other'?'food-product':'food-supplement')+' registration'+(n===1?'':'s'):
      'registrations ('+ks.sort(function(x,y){return TC[y]-TC[x]||(x<y?-1:1);}).map(function(t){return TC[t]+' '+SH[t]+(TC[t]>1&&(t==='supplement'||t==='other')?'s':'');}).join(', ')+')')+
      ' under the brand '+name+'. Registration status changes; confirm a product\'s current status on the FDA verification portal using its FR number.';
    var vu=v.getAttribute('data-verify'), VL={LP:'LP · lower protein, for CKD not on dialysis',HP:'HP · higher protein, for dialysis'};
    document.getElementById('dsv-regs').innerHTML=ps.map(function(p){
      var t=ty(p), f=t==='fsmp'||t==='fsdu', o=t==='other';
      var il=f?'<p class="dd-note">The FDA record names the product type and its registered use, not the full composition. Check the product label for protein, energy, potassium, phosphorus, sodium and fluid per serving.</p>':
        o?'<p class="dd-note">The FDA record names the food product, not its composition. Check the product label for protein, energy, potassium, phosphorus, sodium and sugar per serving.</p>':
        (p.ingredients||[]).length?'<ul class="ds-ings">'+p.ingredients.map(function(i){return '<li>'+escH(i)+'</li>';}).join('')+'</ul>':'<p class="dd-note">Ingredients are not itemized in the FDA record.</p>';
      var raw=p.ingredients_raw?'<span class="ds-raw">As registered: '+escH(p.ingredients_raw)+'</span>':'';
      var rows=[['FR number',escH(p.id)+' · <a href="'+escH(vu)+'" rel="noopener" target="_blank">verify on the FDA portal</a>']];
      if(p.brand_registered&&p.brand_registered.toLowerCase()!==(p.brand||'').toLowerCase())rows.push(['Registered brand',escH(p.brand_registered)]);
      if(f&&p.variant)rows.push(['Variant',escH(VL[p.variant]||p.variant)]);
      rows.push(['Registered as',TL[t]]);
      if(f)rows.push(['Registered use',ut(p)?escH(ut(p)):'Not stated in the FDA record']);
      else if(o&&ut(p))rows.push(['Stated use',escH(ut(p))]);
      if((f||o)&&p.flavor)rows.push(['Flavor',escH(p.flavor)]);
      rows.push(['Form',((f||o)&&(!p.form||p.form==='other'))?'Not stated in the FDA record':escH((p.form||'').charAt(0).toUpperCase()+(p.form||'').slice(1))],['Company',escH(p.company||'Not listed')],
        ['Issued',escH(usd(p.decision_date)||'Not listed')],['Valid until',escH(usd(p.valid_until)||'Not listed')],['FDA risk class',escH(p.risk_type||'Not listed')]);
      if(p.application_type)rows.push(['Application',escH(p.application_type)]);
      return '<article class="ds-reg" id="'+escH(p.id)+'"><h3>'+escH(p.product_name_clean||p.product_name)+'</h3><div><strong>'+(f||o?'Composition':'Ingredients')+'</strong>'+il+raw+'</div><dl class="ds-dl">'+
        rows.map(function(r){return '<dt>'+r[0]+'</dt><dd>'+r[1]+'</dd>';}).join('')+'</dl></article>';}).join('');
  }).catch(function(){fail('Registration data could not be loaded right now.');});
}
var view=document.getElementById('ds-view'); if(view)renderView(view);
var root=document.getElementById('ds-index'); if(!root)return;
var sq=document.getElementById('ds-q'), res=document.getElementById('ds-results'), info=document.getElementById('ds-info'),
    fc=document.getElementById('ds-f-cat'), ff=document.getElementById('ds-f-form'), fk=document.getElementById('ds-f-k'),
    alpha=document.getElementById('ds-alpha'), stat=document.getElementById('ds-static');
var data=null, loading=null, letter='', LIMIT=300;
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();}
function escH(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function load(){if(!loading)loading=fetch(root.getAttribute('data-src')).then(function(r){return r.json();}).then(function(j){
  data=j.map(function(d){d.nn=norm(d.n);d.ii=(d.i||[]).map(norm);d.cc=(d.co||[]).map(norm);d.rr=(d.r||[]).map(norm);d.aa=(d.a||[]).map(norm);return d;});})
  .catch(function(){info.textContent='Search is unavailable right now.';});return loading;}
function sc(s,t){if(!s)return 0;if(s===t)return 100;if(s.indexOf(t)===0)return 80;if((' '+s).indexOf(' '+t)>=0)return 60;if(s.indexOf(t)>=0)return 35;return 0;}
function best(arr,t,w){var b=0,v='';(arr||[]).forEach(function(x,i){var s=sc(x,t)*w;if(s>b){b=s;v=i;}});return [b,v];}
function match(d,t){var m=[sc(d.nn,t),'',''];
  var k=best(d.aa,t,.97);if(k[0]>m[0])m=[k[0],'registered as',d.a[k[1]]];
  var a=best(d.ii,t,.9);if(a[0]>m[0])m=[a[0],'ingredient',d.i[a[1]]];
  var c=best(d.cc,t,.6);if(c[0]>m[0])m=[c[0],'company',d.co[c[1]]];
  var r=best(d.rr,t,.95);if(r[0]>m[0])m=[r[0],'FR no.',d.r[r[1]]];
  return m[0]?m:null;}
function pass(d){if(fc.value&&(d.cat||[]).indexOf(fc.value)<0)return false;if(ff.value&&(d.f||[]).indexOf(ff.value)<0)return false;
  if(fk.checked&&!d.k)return false;if(letter){var c=(d.n||'?')[0].toLowerCase();if((c>='a'&&c<='z'?c:'0')!==letter)return false;}return true;}
function run(){
  var t=norm(sq.value), on=!!(t||fc.value||ff.value||fk.checked||letter);
  if(!on){res.hidden=true;res.innerHTML='';info.textContent='';stat.hidden=false;return;}
  load().then(function(){if(!data)return;var out=[];
    data.forEach(function(d){if(!pass(d))return;if(!t){out.push([d,0]);return;}var m=match(d,t);if(m)out.push([d,m[0],m[1],m[2]]);});
    out.sort(function(a,b){return b[1]-a[1]||a[0].n.localeCompare(b[0].n);});
    res.innerHTML=out.slice(0,LIMIT).map(function(o){var d=o[0];
      var why=o[2]?'<span class="dd-why">'+escH(o[2])+': '+escH(o[3])+'</span>':'';
      var sub=(d.i||[]).length?(d.i||[]).slice(0,4).join(' · ')+((d.i||[]).length>4?' …':''):(d.u||'');
      return '<li><a href="'+href(d)+'">'+escH(d.n)+'</a>'+(d.t?' <span class="dd-tag ds-tag-f">'+(d.mk==='fsdu'?'FSDU':d.mk==='both'?'FSMP · FSDU':'FSMP')+'</span>':'')+(d.rf?' <span class="dd-tag ds-tag-k">Renal formula</span>':'')+(d.k?' <span class="dd-tag ds-tag-k">Kidney-marketed</span>':'')+(d.of&&!d.sp&&!d.t?' <span class="dd-tag">Food product</span>':'')+why+
        '<span class="dd-sub">'+escH(sub)+'</span></li>';}).join('');
    res.hidden=false;stat.hidden=true;
    info.textContent=out.length?(out.length>LIMIT?'Showing the first '+LIMIT+' of '+out.length.toLocaleString('en-US')+' brands':out.length.toLocaleString('en-US')+(out.length===1?' brand':' brands')):'No supplement matches.';
  });
}
var tm=null; sq.addEventListener('input',function(){clearTimeout(tm);tm=setTimeout(run,90);});
sq.addEventListener('focus',load,{once:true});
[fc,ff,fk].forEach(function(el){el.addEventListener('change',run);});
document.getElementById('ds-clear').addEventListener('click',function(){sq.value='';fc.value='';ff.value='';fk.checked=false;setL('');run();});
function setL(L){letter=L;Array.prototype.forEach.call(alpha.querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-l')===(L||'all')?'true':'false');});}
alpha.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var l=b.getAttribute('data-l');setL(l==='all'?'':l);run();});
var qp=new URLSearchParams(location.search); if(qp.get('q')){sq.value=qp.get('q');run();}
if(qp.get('k')==='1'){fk.checked=true;run();}
if(qp.get('cat')){fc.value=qp.get('cat');run();}
})();
"""


def supp_head(title, desc, canonical, jsonld) -> str:
    return head(title, desc, canonical, jsonld, "__HASH__").replace(
        "</head>", f'<link rel="stylesheet" href="/drugs/supplements/supp.css?v={SUPP_ASSET_VERSION}">\n</head>')


def cat_chips(cats) -> str:
    return "".join(f'<span class="dd-chip">{esc(CAT_LABEL.get(c, c))}</span>' for c in cats if c != "other")


def render_notes(slug: str, notes) -> str:
    if not notes_approved(notes):
        return '<p class="dd-kidney-pending">Kidney-specific notes from renalcarematters.com: in preparation.</p>'
    def lst(v):
        v = v if isinstance(v, list) else ([v] if v else [])
        return "".join(f"<li>{esc(ws(x if isinstance(x, str) else x.get('text', '')))}</li>" for x in v if x)
    parts = ['<div class="ds-notes">']
    if notes.get("summary"):
        parts.append(f'<p>{esc(ws(notes["summary"]))}</p>')
    if notes.get("variants"):
        parts.append(f'<h3>What each variant is for</h3><ul>{lst(notes["variants"])}</ul>')
    if notes.get("guideline"):
        parts.append(f'<h3>How it fits the KDOQI 2020 nutrition guideline</h3><ul>{lst(notes["guideline"])}</ul>')
    if notes.get("evidence"):
        parts.append(f'<h3>Evidence</h3><ul>{lst(notes["evidence"])}</ul>')
    if notes.get("cautions"):
        parts.append(f'<h3>Cautions in kidney disease</h3><ul>{lst(notes["cautions"])}</ul>')
    if notes.get("bottom_line"):
        parts.append(f'<h3>Bottom line</h3><p class="ds-bottom">{esc(ws(notes["bottom_line"]))}</p>')
    srcs = notes.get("sources") or []
    if srcs:
        items = []
        for s in srcs:
            if isinstance(s, str):
                items.append(f"<li>{esc(s)}</li>"); continue
            doi = ws(s.get("doi"))
            url = gdp.safe_url(s.get("url")) or (f"https://doi.org/{doi}" if doi else "")
            link = f' <a href="{esc(url)}" rel="noopener" target="_blank">{esc(url)}</a>' if url else ""
            items.append(f'<li>{esc(ws(s.get("citation")))}{link}</li>')
        parts.append(f'<h3>Sources</h3><ol class="dd-srclist">{"".join(items)}</ol>')
    rv = f'Reviewed by {esc(notes.get("reviewed_by") or "renalcarematters.com")}' + (
        f' on {esc(us_date_str(notes.get("reviewed_date")))}' if notes.get("reviewed_date") else "")
    parts.append(f'<p class="dd-note">{rv}. <span class="dd-src dd-src-ours">renalcarematters.com, reviewed</span></p></div>')
    return "".join(parts)


def reg_card(p, today) -> str:
    rid = esc(p["id"])
    fs = is_med(p)
    ings = p.get("ingredients") or []
    if fs:
        ing_html = ('<p class="dd-note">The FDA record names the product type and its registered use, not the full composition. '
                    'Check the product label for protein, energy, potassium, phosphorus, sodium and fluid per serving.</p>')
        ing_head = "Composition"
    elif is_other(p):
        ing_html = ('<p class="dd-note">The FDA record names the food product, not its composition. Check the product label for '
                    'protein, energy, potassium, phosphorus, sodium and sugar per serving.</p>')
        ing_head = "Composition"
    else:
        ing_html = (f'<ul class="ds-ings">{"".join(f"<li>{esc(i)}</li>" for i in ings)}</ul>' if ings
                    else '<p class="dd-note">Ingredients are not itemized in the FDA record.</p>')
        ing_head = "Ingredients"
    raw = ws(p.get("ingredients_raw"))
    raw_html = f'<span class="ds-raw">As registered: {esc(raw)}</span>' if raw else ""
    form = p.get("form", "")
    rows = [("FR number", f'{rid} · <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verify on the FDA portal</a>')]
    if p.get("brand_registered") and p["brand_registered"].lower() != (p.get("brand") or "").lower():
        rows.append(("Registered brand", esc(p["brand_registered"])))
    if fs and p.get("variant"):
        rows.append(("Variant", esc(VARIANT_LABEL[p["variant"]])))
    rows.append(("Registered as", esc(TYPE_LABEL[ptype(p)])))
    if fs:
        rows.append(("Registered use", esc(use_text(p)) if use_text(p) else "Not stated in the FDA record"))
    elif is_other(p) and use_text(p):
        rows.append(("Stated use", esc(use_text(p))))
    if (fs or is_other(p)) and p.get("flavor"):
        rows.append(("Flavor", esc(p["flavor"])))
    nf = fs or is_other(p)
    rows += [("Form", esc(form.capitalize()) if form and not (nf and form == "other") else "Not stated in the FDA record"),
            ("Company", esc(p.get("company") or "Not listed")),
            ("Issued", esc(us_date_str(p.get("decision_date")) or "Not listed")),
            ("Valid until", esc(us_date_str(p.get("valid_until")) or "Not listed")),
            ("FDA risk class", esc(p.get("risk_type") or "Not listed"))]
    if p.get("application_type"):
        rows.append(("Application", esc(p["application_type"])))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return (f'<article class="ds-reg" id="{rid}"><h3>{esc(p.get("product_name_clean") or p.get("product_name"))}</h3>'
            f'<div><strong>{ing_head}</strong>{ing_html}{raw_html}</div><dl class="ds-dl">{dl}</dl></article>')


def reg_lead(n, tcount, mk, all_fsmp) -> str:
    """'11 current registrations (10 FSDU, 1 other food registration)'."""
    noun = f'registration{"s" if n != 1 else ""}'
    if all_fsmp:
        return f'{n:,} current {({"fsmp": "FSMP", "fsdu": "FSDU", "both": "FSMP/FSDU"}[mk])} {noun}'
    if len(tcount) == 1:
        return f'{n:,} current {"food-supplement" if "supplement" in tcount else "food-product"} {noun}'
    short = {"fsmp": "FSMP", "fsdu": "FSDU", "supplement": "food supplement", "other": "other food registration"}
    parts = ", ".join(f'{c:,} {short[t]}{"s" if c != 1 and t in ("supplement", "other") else ""}'
                      for t, c in sorted(tcount.items(), key=lambda x: (-x[1], x[0])))
    return f"{n:,} current {noun} ({parts})"


def brand_page(slug: str, ps: list, sctx: SCtx) -> str:
    ps = sorted(ps, key=lambda p: (p.get("valid_until") or "", p["id"]), reverse=True)
    name = Counter(p["brand"] for p in ps).most_common(1)[0][0]
    cats = sorted({c for p in ps for c in p.get("categories", [])}, key=lambda c: list(CAT_LABEL).index(c) if c in CAT_LABEL else 99)
    kid = any(p.get("kidney_marketed") for p in ps)
    companies = sorted({p["company"] for p in ps if p.get("company")})
    notes = sctx.notes(slug)
    links = sctx.drug_links(ps)
    n = len(ps)
    fs_ps = [p for p in ps if is_med(p)]
    fsmp, all_fsmp = bool(fs_ps), len(fs_ps) == n
    has_s, has_o = any(is_supp(p) for p in ps), any(is_other(p) for p in ps)
    dom = dominant_type(ps)
    tcount = Counter(ptype(p) for p in ps)
    has_f, has_d = any(is_fsmp(p) for p in ps), any(is_fsdu(p) for p in ps)
    mk = med_kind(fs_ps) if fs_ps else ""
    renal = any(p.get("renal_formula") for p in ps)
    variants = sorted({p["variant"] for p in fs_ps if p.get("variant")})
    tags = [t for t in FSMP_TAG_LABEL if any(t in (p.get("fsmp_tags") or []) for p in fs_ps)]
    chips = []
    if has_f:
        chips.append('<span class="dd-chip ds-chip-fsmp">Medical nutrition (FSMP)</span>')
    if has_d:
        chips.append('<span class="dd-chip ds-chip-fsmp">Special dietary food (FSDU)</span>')
    if has_s:
        chips.append('<span class="dd-chip ds-chip-supp">Food supplement</span>')
    if has_o:
        chips.append('<span class="dd-chip ds-chip-supp">Other food registration</span>')
    if renal:
        chips.append('<span class="dd-chip ds-chip-kid">Renal formula</span>')
    if kid:
        chips.append('<span class="dd-chip ds-chip-kid">Kidney-marketed</span>')
    chips.extend(f'<span class="dd-chip">{esc(FSMP_TAG_LABEL[t])}</span>' for t in tags
                 if t not in ("renal", "general") and not (t == "high-protein" and variants))
    chips.extend(f'<span class="dd-chip">{esc(VARIANT_SHORT[v])}</span>' for v in variants)
    chips.append(cat_chips([c for c in cats if c not in ("fsmp", "fsdu", "food")]))
    chips.append(f'<span class="dd-chip">{n:,} registration{"s" if n != 1 else ""}</span>')
    if notes_approved(notes):
        chips.append(f'<a class="dd-chip dd-good" href="#kidney-notes">{KIDNEY_ICON} Kidney notes reviewed</a>')
    all_ings = []
    for p in ps:
        for i in p.get("ingredients") or []:
            if i not in all_ings:
                all_ings.append(i)
    lead_ings = subtitle(ps)
    reg_kind = {"fsmp": "food for special medical purposes (FSMP)", "fsdu": "food for special dietary use (FSDU)",
                "both": "food for special medical purposes (FSMP) and food for special dietary use (FSDU)"}.get(mk, "")
    notes_tail = " and kidney notes" if kidney_section_ok(ps, notes) else ""
    if all_fsmp:
        desc = (f"{name}: {reg_kind} registered with the FDA Philippines. {lead_ings}. "
                f"FR numbers, variants, validity{notes_tail}.")
    elif dom in ("fsmp", "fsdu"):
        desc = (f"{name}: {reg_kind} and other food products registered with the FDA Philippines. {lead_ings}. "
                f"FR numbers, validity{notes_tail}.")
    elif dom == "other":
        desc = (f"{name}: food product registered with the FDA Philippines" + (f". {lead_ings}" if lead_ings else "")
                + f". FR numbers, validity{notes_tail}.")
    else:
        desc = (f"{name}: food supplement registered with the FDA Philippines (no approved therapeutic claims)"
                + (f". Ingredients: {lead_ings}" if lead_ings else "") + f". FR numbers, validity{notes_tail}.")
    kind = ({"fsmp": "medical nutrition, FSMP", "fsdu": "special dietary food, FSDU", "both": "medical nutrition, FSMP and FSDU"}[mk]
            if dom in ("fsmp", "fsdu") else "food product" if dom == "other" else "food supplement")
    canonical = f"{SITE}/drugs/supplements/{slug}"  # extensionless (Cloudflare 308)
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebPage", "@id": canonical, "url": canonical,
                         "name": f"{name} ({kind})", "dateModified": "__ISO__", "inLanguage": "en",
                         "about": ({"@type": "Product", "name": name,
                                    "category": (reg_kind[:1].upper() + reg_kind[1:].split(" (")[0]) if reg_kind and dom in ("fsmp", "fsdu") else "Food product",
                                    "manufacturer": [{"@type": "Organization", "name": c} for c in companies[:5]]} if dom != "supplement" else
                                   {"@type": "DietarySupplement", "name": name, "activeIngredient": all_ings[:20],
                                    "manufacturer": [{"@type": "Organization", "name": c} for c in companies[:5]]}),
                         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE}},
                        ensure_ascii=False).replace("</", "<\\/")
    secs = []
    if kidney_section_ok(ps, notes):
        secs.append(("kidney-notes", "Kidney notes", f"""<section class="dd-kidney dd-sec" id="kidney-notes" aria-labelledby="kn-h">
<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">CKD · dialysis · transplant</div><h2 id="kn-h">Kidney notes</h2></div></div>
{render_notes(slug, notes)}</section>"""))
    if renal and fs_ps:
        rows = []
        for v in (variants or [None]):
            vp = [p for p in fs_ps if p.get("variant") == v] if variants else fs_ps
            if not vp:
                continue
            uses = sorted({use_text(p) for p in vp if use_text(p)}, key=len)
            uses = [u for u in uses if not any(u != w and (w.startswith(u) or re.sub(r"\bpatients?\b", "patients", u) ==
                                                                          re.sub(r"\bpatients?\b", "patients", w)) for w in uses if len(w) >= len(u))]
            flv = sorted({p["flavor"] for p in vp if p.get("flavor")})
            frs = " ".join(f'<a href="#{esc(p["id"])}">{esc(p["id"])}</a>' for p in vp)
            rows.append(f'<tr><th scope="row">{esc(VARIANT_LABEL[v]) if v else "Single formula"}</th>'
                        f'<td data-l="Registered use">{esc("; ".join(uses[:2])) if uses else "Not stated in the FDA record"}</td>'
                        f'<td data-l="Flavor">{esc(", ".join(flv)) or "Not stated"}</td><td data-l="FR numbers">{frs}</td></tr>')
        unl = [p for p in fs_ps if not p.get("variant")] if variants else []
        if unl:
            frs = " ".join(f'<a href="#{esc(p["id"])}">{esc(p["id"])}</a>' for p in unl)
            rows.append(f'<tr><th scope="row">Variant not stated</th><td data-l="Registered use">{esc("; ".join(sorted({use_text(p) for p in unl if use_text(p)})[:2])) or "Not stated in the FDA record"}</td>'
                        f'<td data-l="Flavor">{esc(", ".join(sorted({p["flavor"] for p in unl if p.get("flavor")}))) or "Not stated"}</td><td data-l="FR numbers">{frs}</td></tr>')
        vnote = ("LP and HP are the manufacturer's labels for the lower-protein and higher-protein versions, as registered. "
                 if variants else "")
        secs.append(("variants", "Variants", f"""<section class="dd-sec" id="variants" aria-labelledby="var-h">
<h2 id="var-h">Variants and registered use</h2>
<p class="dd-note">{vnote}Per-serving protein, energy, potassium, phosphorus, sodium and fluid differ between versions and change with
reformulation: check the product label.</p>
<div class="ds-vwrap"><table class="ds-vtable"><thead><tr><th scope="col">Variant</th><th scope="col">Registered use</th>
<th scope="col">Flavor</th><th scope="col">FR numbers</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>"""))
    regs = "".join(reg_card(p, sctx.today) for p in ps)
    secs.append(("registrations", "Registrations", f"""<section class="dd-sec" id="registrations" aria-labelledby="reg-h">
<h2 id="reg-h">FDA Philippines registration{"s" if n != 1 else ""}</h2>
<p class="dd-lead">{reg_lead(n, tcount, mk, all_fsmp)} under the brand {esc(name)}. Registration status changes;
confirm a product's current status on the FDA verification portal using its FR number.</p>
<p><a class="dd-btn" href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">Verify on PH FDA portal {EXT_ICON}</a></p>
{regs}</section>"""))
    if links:
        lis = "".join(f'<li><a href="/drugs/{esc(s)}.html">{esc(nm)}</a><span class="dd-sub">{esc(why)}</span></li>' for s, nm, why in links)
        secs.append(("drug-pages", "Related drug pages", f"""<section class="dd-sec" id="drug-pages" aria-labelledby="dp-h">
<h2 id="dp-h">Related drug pages</h2>
<p class="dd-note">Registered drug products that share an ingredient with this supplement. A drug registration carries approved indications
and labeling; a food supplement does not, and its content and quality are not verified in the same way.</p>
<ul class="ds-druglinks">{lis}</ul></section>"""))
    _gp = sctx.guides_for(slug, ps)
    _rc = []
    for k in supp_keys(ps):
        for f in (sctx.related_guides.get("supplement_key_calculators") or {}).get(k, []):
            if f not in _rc:
                _rc.append(f)
    _rc = _rc[:3]
    rgh = gdp.related_guides_html(_gp, sctx.related_guides, 3, calcs=_rc, what="this product or its main ingredients")
    if rgh:
        _rt, _rn = gdp.related_title(_gp, _rc, 3)
        secs.append(("related-guides", _rn, f"""<section class="dd-sec" id="related-guides" aria-labelledby="rg-h">
<h2 id="rg-h">{_rt}</h2>
{rgh}</section>"""))
    toc = "".join(f'<li><a href="#{sid}">{esc(t)}</a></li>' for sid, t, _ in secs)
    pills = "".join(f'<a class="nav-pill" href="#{sid}">{esc(t)}</a>' for sid, t, _ in secs)
    body = "\n".join(h for _, _, h in secs)
    hero_tag = ({"fsmp": "Medical nutrition (FSMP)", "fsdu": "Special dietary food (FSDU)", "both": "Medical nutrition (FSMP, FSDU)"}[mk]
                if dom in ("fsmp", "fsdu") else "Food product" if dom == "other" else "Food supplement")
    disc = (("A food-for-special-medical-purposes registration means the product may be sold as a food for the dietary management of "
             "patients under medical supervision; it is not a drug approval.") if all_fsmp and mk == "fsmp" else
            ("A food-for-special-dietary-use registration means the product may be sold as a food formulated for a particular dietary "
             "need; it is not a drug approval.") if all_fsmp and mk == "fsdu" else
            ("These registrations allow sale as foods for special medical purposes or for special dietary use; neither is a drug "
             "approval.") if all_fsmp else
            ("These registrations allow sale as foods" + (" (including foods for special medical purposes or special dietary use)" if fsmp else "")
             + "; none is a drug approval or an approval of safety or efficacy for any disease.") if (fsmp or has_o) else
            "A food-supplement registration means the product may be sold as food; it is not an approval of safety or efficacy for any disease.")
    return (supp_head(f"{name} ({kind}) · Renal Care Matters", desc, canonical, jsonld)
            + '<body class="physician-mode single-mode dd-mono">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a> › <a href="/drugs/supplements/">Food supplements</a></div>
        <div class="hero-tag">Drug Database · {hero_tag}</div>
        <h1>{esc(name)}</h1>
        <p class="hero-sub dd-classline">{esc(lead_ings) if lead_ings else ("Ingredients not itemized in the FDA record." if dom == "supplement" else "Composition not stated in the FDA record.")}</p>
        <div class="dd-chips">{"".join(chips)}</div>
        <div class="hero-meta"><span><strong>Company:</strong> {esc("; ".join(companies[:3]) + ("; and others" if len(companies) > 3 else "")) or "Not listed"}</span>
<span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span>
<span><strong>Audience:</strong> Licensed health professionals</span></div>
      </div>
    </div>
  </div>
</section>
<nav class="nav-strip dd-pills" aria-label="Sections"><div class="nav-pills">{pills}</div></nav>
<div class="dd-layout">
<nav class="dd-toc" aria-label="On this page"><div class="dd-toc-h">On this page</div><ol>{toc}</ol></nav>
<main class="dd-main" id="main">
{banner_for(ps)}
{body}
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Data come from the FDA Philippines food-product
registration database and may lag behind the official record. {disc} Not a substitute for clinical judgment.</div>
</main>
</div>
""" + FOOTER + FLOAT)


def viewer_page(sctx: "SCtx", static=()) -> str:
    """One page for every brand without a static page: view.html?b=<brand-slug> renders it in the browser."""
    notes_slugs = ",".join(sorted(f.stem for f in sctx.notes_dir.glob("*.json"))) if sctx.notes_dir.is_dir() else ""
    retired = json.dumps(sctx.index.get("retired") or {}, separators=(",", ":"))
    static_slugs = ",".join(sorted(x for x in (sctx.index.get("retired") or {}).values() if x in static))
    shards = {b.get("shard", "") for b in (sctx.index.get("brands") or {}).values()}
    split = ",".join(sorted({x[0] for x in shards if len(x) == 2}))
    canonical = f"{SITE}/drugs/supplements/view"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebPage", "@id": canonical, "url": canonical,
                         "name": "Food supplement · Drug Index", "inLanguage": "en"}).replace("</", "<\\/")
    page = (supp_head("Food supplement · Renal Care Matters",
                      "FDA Philippines food registration: ingredients or registered use, FR number, company and validity.", canonical, jsonld)
            .replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex,follow">'))
    return (page + '<body class="physician-mode single-mode dd-mono">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a> › <a href="/drugs/supplements/">Food supplements</a></div>
        <div class="hero-tag" id="dsv-tag">Drug Database · Food supplement</div>
        <h1 id="dsv-name">Food supplement</h1>
        <p class="hero-sub dd-classline" id="dsv-ings"></p>
        <div class="dd-chips" id="dsv-chips"></div>
        <div class="hero-meta"><span><strong>Company:</strong> <span id="dsv-co">…</span></span>
<span><strong>Audience:</strong> Licensed health professionals</span></div>
      </div>
    </div>
  </div>
</section>
<nav class="nav-strip dd-pills" aria-label="Sections"><div class="nav-pills"><a class="nav-pill" id="dsv-kn-pill" href="#kidney-notes" hidden>Kidney notes</a><a class="nav-pill" href="#registrations">Registrations</a></div></nav>
<div class="dd-layout">
<nav class="dd-toc" aria-label="On this page"><div class="dd-toc-h">On this page</div><ol><li id="dsv-kn-toc" hidden><a href="#kidney-notes">Kidney notes</a></li><li><a href="#registrations">Registrations</a></li></ol></nav>
<main class="dd-main" id="ds-view" data-base="/data/drugs/supplements/" data-split="{split}" data-today="__ISO__" data-verify="{FDA_VERIFY_URL}"
 data-notes="{esc(notes_slugs)}" data-retired="{esc(retired)}" data-static="{esc(static_slugs)}">
<div id="dsv-bf" hidden>{BANNER_FSMP}</div><div id="dsv-bd" hidden>{BANNER_FSDU}</div><div id="dsv-bs" hidden>{BANNER}</div><div id="dsv-bo" hidden>{BANNER_OTHER}</div>
<section class="dd-kidney dd-sec" id="kidney-notes" aria-labelledby="kn-h" hidden>
<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">CKD · dialysis · transplant</div><h2 id="kn-h">Kidney notes</h2></div></div>
<p class="dd-kidney-pending">Kidney-specific notes from renalcarematters.com: in preparation.</p></section>
<section class="dd-sec" id="registrations" aria-labelledby="reg-h">
<h2 id="reg-h">FDA Philippines registrations</h2>
<p class="dd-lead" id="dsv-lead" aria-live="polite">Loading registrations…</p>
<p><a class="dd-btn" href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">Verify on PH FDA portal {EXT_ICON}</a></p>
<div id="dsv-regs"></div>
</section>
<noscript><p class="dd-placeholder">This page needs JavaScript. Search the <a href="/drugs/supplements/">food supplements index</a> or verify a product on
<a href="{FDA_VERIFY_URL}">verification.fda.gov.ph</a>.</p></noscript>
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Data come from the FDA Philippines food-product
registration database and may lag behind the official record. A food registration (food supplement, food for special medical purposes or
special dietary use, or other food product) means the product may be sold as food; it is not an approval of safety or efficacy for any disease.
Not a substitute for clinical judgment.</div>
</main>
</div>
<script src="/drugs/supplements/supp.js?v={SUPP_ASSET_VERSION}" defer></script>
""" + FOOTER + FLOAT)


def search_entry(slug, ps, static: bool = True, sctx=None) -> dict:
    name = Counter(p["brand"] for p in ps).most_common(1)[0][0]
    ings = []
    for p in ps:
        for i in p.get("ingredients") or []:
            short = re.sub(r"\s*\([^)]*\)\s*$", "", i) if "(" in i and not i.startswith("Vitamin") else i
            if short not in ings:
                ings.append(short)
    e = {"s": slug, "n": name, "i": ings[:10], "co": sorted({p["company"] for p in ps if p.get("company")})[:4],
         "r": [p["id"] for p in ps][:12], "cat": sorted({c for p in ps for c in p.get("categories", [])}),
         "f": sorted({p.get("form", "other") for p in ps})}
    if any(p.get("kidney_marketed") for p in ps):
        e["k"] = 1
    fs = [p for p in ps if is_med(p)]
    if fs:
        e["t"] = "m" if len(fs) == len(ps) else "b"      # m = FSMP/FSDU only, b = also food-supplement registrations
        e["mk"] = med_kind(fs)                           # fsmp | fsdu | both
        if any(p.get("renal_formula") for p in fs):
            e["rf"] = 1
        vs = sorted({p["variant"] for p in fs if p.get("variant")})
        if vs:
            e["v"] = vs
        e["u"] = subtitle(ps) if dominant_type(ps) in ("fsmp", "fsdu") else fsmp_summary(fs)
    aka = sorted({p["brand_registered"] for p in ps if p.get("brand_registered") and p["brand_registered"].lower() != name.lower()})
    if aka:
        e["a"] = aka                                     # other registered brand names (brand families), searchable
    if any(is_supp(p) for p in ps):
        e["sp"] = 1                                      # has a stated food-supplement registration
    if any(is_other(p) for p in ps):
        e["of"] = 1                                      # has an other food registration
    if not ings and "u" not in e:
        e["u"] = subtitle(ps)
    if static:
        e["p"] = 1
    return e


def index_page(entries: list[dict], sctx: SCtx) -> str:
    kid = sorted((e for e in entries if e.get("k")), key=lambda e: e["n"].lower())
    ren = sorted((e for e in entries if e.get("rf")), key=lambda e: e["n"].lower())
    rlis = "".join(f'<li><a href="{esc(e["s"]) + ".html" if e.get("p") else "view.html?b=" + esc(e["s"])}">{esc(e["n"])}</a>'
                   + (' <span class="dd-tag ds-tag-f">FSDU</span>' if e.get("mk") == "fsdu" else "")
                   + "".join(f' <span class="dd-tag ds-tag-f">{v}</span>' for v in e.get("v", []))
                   + f'<span class="dd-sub">{esc(e.get("u", ""))}</span></li>' for e in ren)
    n_fsmp = sum(1 for e in entries if e.get("mk") in ("fsmp", "both"))
    n_fsdu = sum(1 for e in entries if e.get("mk") in ("fsdu", "both"))
    klis = "".join(f'<li><a href="{esc(e["s"]) + ".html" if e.get("p") else "view.html?b=" + esc(e["s"])}">{esc(e["n"])}</a><span class="dd-sub">{esc(" · ".join(e["i"][:4]))}</span></li>' for e in kid)
    cats = Counter(c for e in entries for c in e["cat"])
    cat_opts = "".join(f'<option value="{esc(c)}">{esc(CAT_LABEL.get(c, c))} ({cats[c]:,})</option>' for c in CAT_LABEL if cats.get(c))
    forms = Counter(f for e in entries for f in e["f"])
    form_opts = "".join(f'<option value="{esc(f)}">{esc(f.capitalize())} ({n:,})</option>' for f, n in sorted(forms.items()))
    n_regs = sum(len(v) for v in sctx.by_brand.values())
    letters = ["0"] + [chr(c) for c in range(ord("a"), ord("z") + 1)]
    btns = '<button type="button" data-l="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-l="{l}" aria-pressed="false" aria-label="{"Names starting with a number or symbol" if l == "0" else "Letter " + l.upper()}">{"#" if l == "0" else l.upper()}</button>'
        for l in letters)
    canonical = f"{SITE}/drugs/supplements/"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "@id": canonical, "url": canonical,
                         "name": "Food supplements · Drug Index", "dateModified": "__ISO__", "inLanguage": "en",
                         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE}}).replace("</", "<\\/")
    desc = (f"Search {len(entries):,} food-supplement and medical-nutrition (FSMP) brands ({n_regs:,} current FDA Philippines registrations) "
            "by brand, ingredient, company or FR number, with renal nutrition formulas and kidney-marketed products flagged.")
    return (supp_head("Food supplements & medical nutrition · Drug Index · Renal Care Matters", desc, canonical, jsonld)
            + '<body class="physician-mode single-mode dd-index-page">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid"><div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a></div>
        <div class="hero-tag">Drug Database · Food supplements</div>
        <h1>Food supplements &amp; medical nutrition</h1>
        <p class="hero-sub">Products registered with the Food and Drug Administration (FDA) Philippines as food supplements or as foods for
special medical purposes (FSMP, such as renal nutrition formulas) or for special dietary use (FSDU), with FR numbers, not as drugs. Search by brand, ingredient, company or FR number.</p>
        <div class="dd-chips"><span class="dd-chip">{len(entries):,} brands</span><span class="dd-chip">{n_regs:,} registrations</span>
<a class="dd-chip ds-chip-fsmp" href="#renal-formulas">{len(ren):,} renal nutrition formulas</a>
<a class="dd-chip ds-chip-fsmp" href="?cat=fsmp">{n_fsmp:,} medical-nutrition (FSMP) brands</a>
<a class="dd-chip ds-chip-fsmp" href="?cat=fsdu">{n_fsdu:,} special dietary food (FSDU) brands</a>
<a class="dd-chip ds-chip-kid" href="#kidney-marketed">{len(kid):,} kidney-marketed brands</a></div>
        <div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
    </div></div>
  </div>
</section>
<main class="container dd-wide" id="ds-index" data-src="/drugs/supplements/search-index.json">
{BANNER}
<p class="dd-note">Foods for special medical purposes (FSMP) carry a different registration: for the dietary management of patients under medical
supervision. Foods for special dietary use (FSDU) are foods formulated for a particular dietary need, such as diabetes or dialysis; not medicines.
Food products registered under neither heading and not as food supplements (milk supplements, adult nutrition drinks, ready-to-use
supplementary foods) are marked "Other food registration".</p>
<div class="dd-search" role="search">
<label class="dd-hidden" for="ds-q">Search food supplements</label>
<input id="ds-q" type="search" placeholder="Brand, ingredient, company, or FR number (e.g., probiotic, Renadyl, Nepro)" autocomplete="off" spellcheck="false">
</div>
<div class="ds-facets" role="group" aria-label="Filters">
<label><span class="dd-hidden">Category</span><select id="ds-f-cat"><option value="">All categories</option>{cat_opts}</select></label>
<label><span class="dd-hidden">Form</span><select id="ds-f-form"><option value="">All forms</option>{form_opts}</select></label>
<label class="dd-check"><input type="checkbox" id="ds-f-k"> Kidney-marketed only</label>
<button type="button" class="dd-btn dd-btn-ghost" id="ds-clear">Clear</button>
</div>
<nav class="dd-alpha" id="ds-alpha" aria-label="Filter by first letter">{btns}</nav>
<p class="dd-note" id="ds-info" aria-live="polite"></p>
<ul class="dd-list ds-list" id="ds-results" hidden></ul>
<div id="ds-static">
<section class="dd-sec" id="renal-formulas" aria-labelledby="rf-h">
<h2 id="rf-h">Renal nutrition formulas</h2>
<p class="dd-note">Registered as foods for special medical purposes (FSMP) or, where marked, foods for special dietary use (FSDU), for
kidney disease or dialysis. LP marks the lower-protein version (CKD not on dialysis) and HP the higher-protein version (dialysis), as registered. Check the product label for
protein, potassium, phosphorus and fluid per serving. More medical nutrition: choose "Medical nutrition (FSMP)" or "Special dietary food
(FSDU)" under Category.</p>
<ul class="dd-list ds-list">{rlis}</ul>
</section>
<section class="dd-sec" id="kidney-marketed" aria-labelledby="km-h">
<h2 id="km-h">Kidney-marketed food supplements</h2>
<p class="dd-note">Brands whose name or registered product name refers to the kidney, urine, uric acid or dialysis, plus ketoanalogue products
and brands on a short curated list. "Kidney-marketed" describes how a product is named, not evidence that it helps the kidney.</p>
<ul class="dd-list ds-list">{klis}</ul>
</section>
</div>
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Data come from the FDA Philippines food-product registration
database and may lag behind the official record. Verify a registration on <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verification.fda.gov.ph</a>.
Canceled registrations and registrations past their validity date are not listed. Not a substitute for clinical judgment.</div>
</main>
<script src="/drugs/supplements/supp.js?v={SUPP_ASSET_VERSION}" defer></script>
""" + FOOTER + FLOAT)


SITE_FILE_BUDGET = 17500   # Dr. Rivero: stay on the Cloudflare Pages Free plan (20,000-file cap) with headroom
FIXED_FILES = ("index.html", "view.html", "search-index.json", "supp.css", "supp.js")
ALLOWLIST = REPO / "tools" / "drugdb" / "supplement_pages_allowlist.txt"


def read_allowlist() -> list[str]:
    if not ALLOWLIST.exists():
        return []
    out = []
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.append(slugify(line))
    return out


def site_file_count(out_dir: Path, data_dir: Path) -> int:
    """Files the deployment will hold apart from the generated supplement pages: tracked files outside
    drugs/supplements/ and data/drugs/supplements/, plus the supplement data shards as they are on disk now."""
    import subprocess
    files = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True).stdout.splitlines()
    def rel(d):
        try:
            return d.resolve().relative_to(REPO).as_posix().rstrip("/") + "/"
        except ValueError:
            return None
    skip = [x for x in (rel(out_dir), rel(REPO / "data" / "drugs" / "supplements")) if x]
    n = sum(1 for f in files if not any(f.startswith(x) for x in skip))
    sd = REPO / "data" / "drugs" / "supplements"
    return n + (sum(1 for f in sd.glob("*.json")) if sd.is_dir() else 0)


def plan_static(sctx: "SCtx", out_dir: Path, data_dir: Path, budget_total: int) -> tuple[set, dict]:
    """Choose which brands get a static page: (a) renal FSMP formulas (always), kidney-marketed or with approved notes,
    then (c) the allowlist and every other FSMP/FSDU brand, then (b) brands with >= 3 active registrations by registration count; capped so the
    site stays within budget_total files."""
    base = site_file_count(out_dir, data_dir) + len(FIXED_FILES)
    cap = max(0, budget_total - base)
    by = sctx.by_brand
    renal = sorted((s for s, ps in by.items() if any(p.get("renal_formula") for p in ps)), key=lambda s: (-len(by[s]), s))
    a = renal + sorted((s for s, ps in by.items() if s not in renal and (any(p.get("kidney_marketed") for p in ps)
                                                                       or notes_approved(sctx.notes(s)))),
                       key=lambda s: (-len(by[s]), s))
    c = [s for s in read_allowlist() if s in by]
    c += sorted((s for s, ps in by.items() if any(is_med(p) for p in ps) and s not in c), key=lambda s: (-len(by[s]), s))
    b = sorted((s for s, ps in by.items() if len(ps) >= 3), key=lambda s: (-len(by[s]), s))
    chosen, order = [], []
    for s in a + c + b:
        if s not in chosen:
            chosen.append(s)
    static = chosen[:cap]
    info = {"site_files_without_supp_pages": base, "budget": budget_total, "page_cap": cap, "renal_fsmp": len(renal), "kidney": len(a),
            "allowlist": len(c), "multi_registration": len(b), "eligible": len(chosen), "static": len(static),
            "dropped_for_budget": chosen[cap:]}
    if chosen[cap:]:
        lost_a = [x for x in chosen[cap:] if x in a]
        print(f"  ! file budget: {len(chosen) - cap} eligible brands get the viewer instead of a static page"
              + (f" (including {len(lost_a)} kidney-marketed)" if lost_a else ""), file=sys.stderr)
    return set(static), info


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=str(REPO / "data" / "drugs"))
    ap.add_argument("--out-dir", default=str(REPO / "drugs" / "supplements"))
    ap.add_argument("--as-of", help="override today's date (YYYY-MM-DD)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-prune", action="store_true")
    ap.add_argument("--budget", type=int, default=SITE_FILE_BUDGET, help="max total site files (default %(default)s)")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    data_dir, out_dir = Path(a.data_dir), Path(a.out_dir)
    sctx = SCtx(data_dir, out_dir, today)
    if not sctx.by_brand:
        sys.exit(f"No supplement data in {data_dir}/supplements/ (run tools/drugdb/build_supplements.py first)")
    static, plan = plan_static(sctx, out_dir, data_dir, a.budget)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_if_changed(out_dir / "supp.css", SUPP_CSS, a.dry_run)
    write_if_changed(out_dir / "supp.js", SUPP_JS, a.dry_run)
    stats, entries = Counter(), []
    for slug in sorted(sctx.by_brand):
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug) or slug == "index":
            print(f"  ! skipping unsafe slug {slug!r}", file=sys.stderr)
            continue
        ps = sctx.by_brand[slug]
        if slug in static:
            stats[finalize(out_dir / f"{slug}.html", brand_page(slug, ps, sctx), today, a.dry_run, False)] += 1
        entries.append(search_entry(slug, ps, slug in static, sctx))
    entries.sort(key=lambda e: e["n"].lower())
    write_if_changed(out_dir / "search-index.json", json.dumps(entries, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    stats["index-" + finalize(out_dir / "index.html", index_page(entries, sctx), today, a.dry_run, False)] += 1
    stats["view-" + finalize(out_dir / "view.html", viewer_page(sctx, static), today, a.dry_run, False)] += 1
    if not a.no_prune:
        keep = set(static) | {"index", "view"}
        for f in out_dir.glob("*.html"):
            if f.stem in keep:
                continue
            with open(f, encoding="utf-8") as fh:
                if f'content="{GENERATOR_TAG}"' in fh.read(2048):
                    stats["pruned"] += 1
                    if not a.dry_run:
                        f.unlink()
    if not a.dry_run:
        (data_dir / "supplements" / "_pages.json").write_text(json.dumps(dict(plan, as_of=today.isoformat(),
            static_brands=sorted(static)), ensure_ascii=False, indent=1), encoding="utf-8")
    total = site_file_count(out_dir, data_dir) + len(static) + len(FIXED_FILES)
    print(f"static pages {len(static):,} of {len(entries):,} brands (cap {plan['page_cap']:,}) · site files ≈ {total:,} "
          f"(budget {a.budget:,}) · not rendered: {dict(sctx.dropped)} · "
          + " · ".join(f"{k}: {v}" for k, v in sorted(stats.items())) + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
