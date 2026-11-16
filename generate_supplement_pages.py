#!/usr/bin/env python3
"""
generate_supplement_pages.py: Food Supplements section of the renalcarematters.com Drug Database.

Reads (under --data-dir, default data/drugs/):
  supplements.json                 brand index written by tools/drugdb/build_supplements.py
  supplements/<shard>.json         PH FDA food-supplement registrations (FR numbers)
  supplement-notes/<slug>.json     optional; our kidney notes, rendered ONLY when review_status == "approved"
  generics.json                    drug generics, for cross-links to drug pages
Writes (under --out-dir, default drugs/supplements/):
  <brand-slug>.html                one page per brand (all of its registrations)
  index.html                       searchable Food Supplements index
  search-index.json                [{s, n, i[], co[], r[], cat[], f[], k?}], lazy-loaded here and by the Drug Index
  supp.css, supp.js                section styles and index search

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

SUPP_ASSET_VERSION = "1"
CAT_LABEL = {"probiotic": "Probiotic", "herbal/botanical": "Herbal / botanical", "vitamin/mineral": "Vitamin / mineral",
             "omega-3": "Omega-3", "amino acid/protein": "Amino acid / protein", "ketoanalogue": "Ketoanalogue",
             "fiber/prebiotic": "Fiber / prebiotic", "other": "Other"}
BANNER = ('<div class="ds-banner" role="note"><strong>Registered with the Philippine FDA as a FOOD SUPPLEMENT — no approved '
          'therapeutic claims.</strong> Not a substitute for prescribed treatment.</div>')

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
        drug_dir = out_dir.parent
        self.drug_pages = {f.stem for f in drug_dir.glob("*.html")} - {"index"}
        self.notes_dir = data_dir / "supplement-notes"

    def notes(self, slug):
        return load_json(self.notes_dir / f"{slug}.json") if self.notes_dir.is_dir() else None

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
            if self.drug_ok(exact) and exact not in seen:
                seen.add(exact)
                out.append((exact, self.generics.get(exact, {}).get("name") or exact, "same ingredients"))
            ings = p.get("ingredients") or []
            for i in ings:
                if i == "Diosmin" and "Hesperidin" not in ings:
                    cands = ["diosmin"]
                else:
                    cands = CROSS.get(i, [])
                b = self.best(cands)
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
html[data-theme="dark"] .ds-banner { background: rgba(245,158,11,.12); border-color: #f59e0b; color: #fde7c2; }
html[data-theme="dark"] .ds-banner strong { color: #fff3dc; }
html[data-theme="dark"] .dd-chip.ds-chip-supp { color: #e5e9f0; background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.35); }
html[data-theme="dark"] .dd-chip.ds-chip-kid { color: #fde7c2; background: rgba(245,158,11,.14); border-color: rgba(245,158,11,.5); }
html[data-theme="dark"] .ds-reg { background: #1a2535; border-color: rgba(255,255,255,.14); }
html[data-theme="dark"] .ds-notes { background: rgba(43,168,176,.08); border-color: rgba(43,168,176,.4); }
html[data-theme="dark"] .ds-notes h3 { color: #a5f3fc; }
html[data-theme="dark"] .ds-dl a, html[data-theme="dark"] .ds-druglinks a { color: #7dd3d8; }
html[data-theme="dark"] .ds-raw { color: #9ba6b8; }
html[data-theme="dark"] .ds-tag-k { color: #fde7c2; background: rgba(245,158,11,.16); }
@media (max-width: 640px) { .ds-dl { grid-template-columns: 1fr; } .ds-dl dt { margin-top: 6px; } }
@media print { .ds-banner { border-width: 1px; } }
"""

SUPP_JS = r"""/* Generated by generate_supplement_pages.py: do not edit. */
(function(){
'use strict';
var root=document.getElementById('ds-index'); if(!root)return;
var sq=document.getElementById('ds-q'), res=document.getElementById('ds-results'), info=document.getElementById('ds-info'),
    fc=document.getElementById('ds-f-cat'), ff=document.getElementById('ds-f-form'), fk=document.getElementById('ds-f-k'),
    alpha=document.getElementById('ds-alpha'), stat=document.getElementById('ds-static');
var data=null, loading=null, letter='', LIMIT=300;
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,' ').trim();}
function escH(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
function load(){if(!loading)loading=fetch(root.getAttribute('data-src')).then(function(r){return r.json();}).then(function(j){
  data=j.map(function(d){d.nn=norm(d.n);d.ii=(d.i||[]).map(norm);d.cc=(d.co||[]).map(norm);d.rr=(d.r||[]).map(norm);return d;});})
  .catch(function(){info.textContent='Search is unavailable right now.';});return loading;}
function sc(s,t){if(!s)return 0;if(s===t)return 100;if(s.indexOf(t)===0)return 80;if((' '+s).indexOf(' '+t)>=0)return 60;if(s.indexOf(t)>=0)return 35;return 0;}
function best(arr,t,w){var b=0,v='';(arr||[]).forEach(function(x,i){var s=sc(x,t)*w;if(s>b){b=s;v=i;}});return [b,v];}
function match(d,t){var m=[sc(d.nn,t),'',''];
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
      var sub=(d.i||[]).slice(0,4).join(' · ')+((d.i||[]).length>4?' …':'');
      return '<li><a href="'+encodeURIComponent(d.s)+'.html">'+escH(d.n)+'</a>'+(d.k?' <span class="dd-tag ds-tag-k">Kidney-marketed</span>':'')+why+
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
    ings = p.get("ingredients") or []
    ing_html = (f'<ul class="ds-ings">{"".join(f"<li>{esc(i)}</li>" for i in ings)}</ul>' if ings
                else '<p class="dd-note">Ingredients are not itemized in the FDA record.</p>')
    raw = ws(p.get("ingredients_raw"))
    raw_html = f'<span class="ds-raw">As registered: {esc(raw)}</span>' if raw else ""
    rows = [("FR number", f'{rid} · <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verify on the FDA portal</a>'),
            ("Form", esc(p.get("form", "").capitalize())), ("Company", esc(p.get("company") or "Not listed")),
            ("Issued", esc(us_date_str(p.get("decision_date")) or "Not listed")),
            ("Valid until", esc(us_date_str(p.get("valid_until")) or "Not listed")),
            ("FDA risk class", esc(p.get("risk_type") or "Not listed"))]
    if p.get("application_type"):
        rows.append(("Application", esc(p["application_type"])))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return (f'<article class="ds-reg" id="{rid}"><h3>{esc(p.get("product_name_clean") or p.get("product_name"))}</h3>'
            f'<div><strong>Ingredients</strong>{ing_html}{raw_html}</div><dl class="ds-dl">{dl}</dl></article>')


def brand_page(slug: str, ps: list, sctx: SCtx) -> str:
    ps = sorted(ps, key=lambda p: (p.get("valid_until") or "", p["id"]), reverse=True)
    name = Counter(p["brand"] for p in ps).most_common(1)[0][0]
    cats = sorted({c for p in ps for c in p.get("categories", [])}, key=lambda c: list(CAT_LABEL).index(c) if c in CAT_LABEL else 99)
    kid = any(p.get("kidney_marketed") for p in ps)
    companies = sorted({p["company"] for p in ps if p.get("company")})
    notes = sctx.notes(slug)
    links = sctx.drug_links(ps)
    n = len(ps)
    chips = ['<span class="dd-chip ds-chip-supp">Food supplement</span>']
    if kid:
        chips.append('<span class="dd-chip ds-chip-kid">Kidney-marketed</span>')
    chips.append(cat_chips(cats))
    chips.append(f'<span class="dd-chip">{n:,} registration{"s" if n != 1 else ""}</span>')
    if notes_approved(notes):
        chips.append(f'<a class="dd-chip dd-good" href="#kidney-notes">{KIDNEY_ICON} Kidney notes reviewed</a>')
    all_ings = []
    for p in ps:
        for i in p.get("ingredients") or []:
            if i not in all_ings:
                all_ings.append(i)
    lead_ings = ", ".join(all_ings[:6]) + ("…" if len(all_ings) > 6 else "")
    desc = (f"{name}: food supplement registered with the FDA Philippines (no approved therapeutic claims)"
            + (f". Ingredients: {lead_ings}" if lead_ings else "") + ". FR numbers, validity and kidney notes.")
    canonical = f"{SITE}/drugs/supplements/{slug}.html"
    jsonld = json.dumps({"@context": "https://schema.org", "@type": "WebPage", "@id": canonical, "url": canonical,
                         "name": f"{name} (food supplement)", "dateModified": "__ISO__", "inLanguage": "en",
                         "about": {"@type": "DietarySupplement", "name": name, "activeIngredient": all_ings[:20],
                                   "manufacturer": [{"@type": "Organization", "name": c} for c in companies[:5]]},
                         "publisher": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE}},
                        ensure_ascii=False).replace("</", "<\\/")
    secs = []
    secs.append(("kidney-notes", "Kidney notes", f"""<section class="dd-kidney dd-sec" id="kidney-notes" aria-labelledby="kn-h">
<div class="dd-kidney-head">{KIDNEY_ICON}<div><div class="section-tag">CKD · dialysis · transplant</div><h2 id="kn-h">Kidney notes</h2></div></div>
{render_notes(slug, notes)}</section>"""))
    regs = "".join(reg_card(p, sctx.today) for p in ps)
    secs.append(("registrations", "Registrations", f"""<section class="dd-sec" id="registrations" aria-labelledby="reg-h">
<h2 id="reg-h">FDA Philippines registration{"s" if n != 1 else ""}</h2>
<p class="dd-lead">{n:,} current food-supplement registration{"s" if n != 1 else ""} under the brand {esc(name)}. Registration status changes;
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
    toc = "".join(f'<li><a href="#{sid}">{esc(t)}</a></li>' for sid, t, _ in secs)
    pills = "".join(f'<a class="nav-pill" href="#{sid}">{esc(t)}</a>' for sid, t, _ in secs)
    body = "\n".join(h for _, _, h in secs)
    return (supp_head(f"{name} (food supplement) · Renal Care Matters", desc, canonical, jsonld)
            + '<body class="physician-mode single-mode dd-mono">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a> › <a href="/drugs/supplements/">Food supplements</a></div>
        <div class="hero-tag">Drug Database · Food supplement</div>
        <h1>{esc(name)}</h1>
        <p class="hero-sub dd-classline">{esc(lead_ings) if lead_ings else "Ingredients not itemized in the FDA record."}</p>
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
{BANNER}
{body}
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Data come from the FDA Philippines food-product
registration database and may lag behind the official record. A food-supplement registration means the product may be sold as food;
it is not an approval of safety or efficacy for any disease. Not a substitute for clinical judgment.</div>
</main>
</div>
""" + FOOTER + FLOAT)


def search_entry(slug, ps) -> dict:
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
    return e


def index_page(entries: list[dict], sctx: SCtx) -> str:
    kid = sorted((e for e in entries if e.get("k")), key=lambda e: e["n"].lower())
    klis = "".join(f'<li><a href="{esc(e["s"])}.html">{esc(e["n"])}</a><span class="dd-sub">{esc(" · ".join(e["i"][:4]))}</span></li>' for e in kid)
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
    desc = (f"Search {len(entries):,} food-supplement brands ({n_regs:,} current FDA Philippines registrations) by brand, ingredient, "
            "company or FR number, with kidney-marketed products flagged.")
    return (supp_head("Food supplements · Drug Index · Renal Care Matters", desc, canonical, jsonld)
            + '<body class="physician-mode single-mode dd-index-page">\n' + header(True) + f"""
<section class="hero">
  <div class="container dd-hero-wide">
    <div class="hero-grid"><div class="hero-copy">
        <div class="dd-crumb"><a href="/drugs/">Drug Index</a></div>
        <div class="hero-tag">Drug Database · Food supplements</div>
        <h1>Food supplements</h1>
        <p class="hero-sub">Products registered with the Food and Drug Administration (FDA) Philippines as food supplements (FR numbers),
not as drugs. Search by brand, ingredient, company or FR number.</p>
        <div class="dd-chips"><span class="dd-chip">{len(entries):,} brands</span><span class="dd-chip">{n_regs:,} registrations</span>
<a class="dd-chip ds-chip-kid" href="#kidney-marketed">{len(kid):,} kidney-marketed brands</a></div>
        <div class="hero-meta"><span><strong>Last updated:</strong> <time class="dd-meta-time" datetime="__ISO__">__DATE__</time></span></div>
    </div></div>
  </div>
</section>
<main class="container dd-wide" id="ds-index" data-src="/drugs/supplements/search-index.json">
{BANNER}
<div class="dd-search" role="search">
<label class="dd-hidden" for="ds-q">Search food supplements</label>
<input id="ds-q" type="search" placeholder="Brand, ingredient, company, or FR number (e.g., probiotic, Renadyl)" autocomplete="off" spellcheck="false">
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
<section class="dd-sec" id="kidney-marketed" aria-labelledby="km-h">
<h2 id="km-h">Kidney-marketed supplements</h2>
<p class="dd-note">Brands whose name or registered product name refers to the kidney, urine, uric acid or dialysis, plus ketoanalogue products
and brands on a short curated list. "Kidney-marketed" describes how a product is named, not evidence that it helps the kidney.</p>
<ul class="dd-list ds-list">{klis}</ul>
</section>
</div>
<div class="disclaimer" role="note"><strong>For health professionals.</strong> Data come from the FDA Philippines food-product registration
database and may lag behind the official record; verify a registration on <a href="{FDA_VERIFY_URL}" rel="noopener" target="_blank">verification.fda.gov.ph</a>.
Canceled registrations and registrations past their validity date are not listed. Not a substitute for clinical judgment.</div>
</main>
<script src="/drugs/supplements/supp.js?v={SUPP_ASSET_VERSION}" defer></script>
""" + FOOTER + FLOAT)


CF_FILE_LIMIT = 20000   # Cloudflare Pages per-deployment file cap (Free plan); check the account's plan


def budget_check(out_dir: Path, n_new: int, allow: bool) -> None:
    """Refuse to write a page set that would push the deployment past Cloudflare's file cap."""
    import subprocess
    try:
        files = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True).stdout.splitlines()
    except Exception:
        return
    rel = out_dir.resolve().relative_to(REPO).as_posix() + "/" if out_dir.resolve().is_relative_to(REPO) else None
    other = sum(1 for f in files if not (rel and f.startswith(rel)))
    total = other + n_new
    msg = f"site file count after this build ≈ {total:,} (Cloudflare Pages cap {CF_FILE_LIMIT:,})"
    if total > CF_FILE_LIMIT - 200 and not allow:
        sys.exit("Refusing to build: " + msg + ". Re-run with --allow-over-budget only if the plan allows more files.")
    if total > CF_FILE_LIMIT * 0.85:
        print("  ! " + msg, file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=str(REPO / "data" / "drugs"))
    ap.add_argument("--out-dir", default=str(REPO / "drugs" / "supplements"))
    ap.add_argument("--as-of", help="override today's date (YYYY-MM-DD)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-prune", action="store_true")
    ap.add_argument("--allow-over-budget", action="store_true", help="skip the Cloudflare file-count guard")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    data_dir, out_dir = Path(a.data_dir), Path(a.out_dir)
    sctx = SCtx(data_dir, out_dir, today)
    if not sctx.by_brand:
        sys.exit(f"No supplement data in {data_dir}/supplements/ (run tools/drugdb/build_supplements.py first)")
    budget_check(out_dir, len(sctx.by_brand) + 4, a.allow_over_budget)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_if_changed(out_dir / "supp.css", SUPP_CSS, a.dry_run)
    write_if_changed(out_dir / "supp.js", SUPP_JS, a.dry_run)
    stats, entries = Counter(), []
    for slug in sorted(sctx.by_brand):
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug) or slug == "index":
            print(f"  ! skipping unsafe slug {slug!r}", file=sys.stderr)
            continue
        ps = sctx.by_brand[slug]
        stats[finalize(out_dir / f"{slug}.html", brand_page(slug, ps, sctx), today, a.dry_run, False)] += 1
        entries.append(search_entry(slug, ps))
    entries.sort(key=lambda e: e["n"].lower())
    write_if_changed(out_dir / "search-index.json", json.dumps(entries, ensure_ascii=False, separators=(",", ":")), a.dry_run)
    stats["index-" + finalize(out_dir / "index.html", index_page(entries, sctx), today, a.dry_run, False)] += 1
    if not a.no_prune:
        keep = {e["s"] for e in entries} | {"index"}
        for f in out_dir.glob("*.html"):
            if f.stem in keep:
                continue
            with open(f, encoding="utf-8") as fh:
                if f'content="{GENERATOR_TAG}"' in fh.read(2048):
                    stats["pruned"] += 1
                    if not a.dry_run:
                        f.unlink()
    print(f"{len(entries):,} supplement brand pages · not rendered: {dict(sctx.dropped)} · "
          + " · ".join(f"{k}: {v}" for k, v in sorted(stats.items())) + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
