#!/usr/bin/env python3
"""Generate the Nephrology Nursing & Hemodialysis course (hub, educator page, 12 modules).

Content lives in tools/nursing/content/*.py (hand-edited). This script renders it into
guides/nephrology-nursing*.html using the house guide scaffold, then (with --patch) runs
the same per-guide patch pipeline as /setup-guide so the pages carry the master CSS,
references accordion, share bar, side rail, reading time and the rest.

    python3 generate_nursing_course.py              # write pages + docs
    python3 generate_nursing_course.py --patch      # write pages, then run the patch pipeline
    python3 generate_nursing_course.py --check      # validate content only (links, refs, quiz keys)
    python3 generate_nursing_course.py --patch --reset-published   # on go-live day: re-stamp the publish date

Never hand-edit guides/nephrology-nursing*.html: edit the content files and re-run.
An existing page's article:published_time is carried over, so re-running never re-dates a page.
"""
import argparse, html, importlib.util, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "guides"
CONTENT = ROOT / "tools" / "nursing" / "content"
DATA = ROOT / "data" / "nursing-course"
DOCS = ROOT / "docs" / "nursing-course"
TEMPLATE = GUIDES / "dialysis-qapi-vs-cqi.html"   # chrome (header, floating buttons) is copied from here
SITE = "https://renalcarematters.com"


def load(name):
    spec = importlib.util.spec_from_file_location(name, CONTENT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C = load("common")
D = load("display")
# course figures (tools/nursing/build_figures.py writes content/figures.py from the image manifest)
FIGS = load("figures").FIGURES if (CONTENT / "figures.py").exists() else []


def place_figures(page, key):
    """Insert each figure listed for this page at the end of its section (in manifest order)."""
    for f in [x for x in FIGS if x["page"] == key]:
        if not (ROOT / "images" / f"{f['stem']}.webp").exists():
            continue
        opener = f'<section class="section" id="{f["section"]}">'
        i = page.find(opener)
        if i < 0:
            err(f"figure {f['id']}: section '{f['section']}' not found on page {key}")
            continue
        j = page.find("</section>", i)
        shape = "nc-fig-tall" if f["h"] > f["w"] * 1.2 else ("nc-fig-card" if f["h"] > f["w"] * 0.66 else "nc-fig-wide")
        alt = html.escape(html.unescape(f["alt"]))
        fig = (f'<figure class="nc-fig {shape}" id="fig-{f["id"].lower()}">'
               f'<picture><source srcset="../images/{f["stem"]}.webp" type="image/webp">'
               f'<img class="nc-fig-img" src="../images/{f["stem"]}.png" alt="{alt}" width="{f["w"]}" height="{f["h"]}" loading="lazy" decoding="async"></picture>'
               f'<figcaption>{f["caption"]}</figcaption></figure>\n')
        page = page[:j] + fig + page[j:]
    return page
COURSE, MODULES, ABBR = C.COURSE, C.MODULES, C.ABBR
MODS = {}
for _id, _slug, _title, _short, _neph, _hd in MODULES:
    m = load(f"m{_id}").MODULE
    m.update(id=_id, slug=f"{COURSE['hub_slug']}-{_id}-{_slug}", title=_title, short=_short, neph=_neph, hd=_hd)
    # optional expansion file mNN_x.py: extra objectives, sections (inserted after a named
    # section), quiz items, glossary terms, review flags, and PubMed references
    for _xf in sorted(CONTENT.glob(f"m{_id}_x*.py")):   # mNN_x.py, mNN_x2.py, ...
        _x = load(_xf.stem)
        m["objectives"] = m["objectives"] + list(getattr(_x, "OBJECTIVES", []))
        for _sec in getattr(_x, "EXTRA", []):
            _ids = [s["id"] for s in m["sections"]]
            if _sec["id"] in _ids:
                raise SystemExit(f"{_xf.name}: duplicate section id {_sec['id']}")
            _at = _ids.index(_sec["after"]) + 1 if _sec.get("after") in _ids else len(_ids)
            m["sections"].insert(_at, _sec)
        m["quiz"] = m["quiz"] + list(getattr(_x, "QUIZ", []))
        m["terms"] = m.get("terms", []) + list(getattr(_x, "TERMS", []))
        m["flags"] = m.get("flags", []) + list(getattr(_x, "FLAGS", []))
        C.PUBMED_REFS.update(getattr(_x, "NEW_REFS", {}))
    # optional question-bank file mNN_q.py: more self-assessment items for the module's bank
    if (CONTENT / f"m{_id}_q.py").exists():
        _q = load(f"m{_id}_q")
        m["quiz"] = m["quiz"] + list(getattr(_q, "QUIZ", []))
        C.PUBMED_REFS.update(getattr(_q, "NEW_REFS", {}))
    # optional competency file mNN_c.py: COMPETENCIES (thread, statement, level, evidence) and MILESTONE
    m["competencies"], m["milestone"] = [], ""
    for _cf in sorted(CONTENT.glob(f"m{_id}_c*.py")):   # mNN_c.py, mNN_c2.py, ... (later files add competencies)
        _c = load(_cf.stem)
        m["competencies"] += list(getattr(_c, "COMPETENCIES", []))
        m["milestone"] = m["milestone"] or getattr(_c, "MILESTONE", "")
    MODS[_id] = m
ORDER = list(C.PATH_ORDER["neph"])   # default order and previous/next follow the Nephrology Nursing path
BANK_SIZE = 15   # minimum questions per module bank (banks may grow)
DRAW = 5         # questions shown per page load, drawn at random from the bank
_PLAIN = {"CKD": "Chronic Kidney Disease", "AKI": "Acute Kidney Injury", "HD": "Hemodialysis", "PD": "Peritoneal Dialysis", "CRRT": "Continuous Renal Replacement Therapy"}
for _m in MODS.values():
    # spelled-out title for navigation cards and tables (the page <h1> keeps the short form)
    _m["plain"] = re.sub(r"\b(CKD|AKI|HD|PD|CRRT)\b", lambda x: _PLAIN[x.group(1)], _m["title"])
ERRORS = []


def err(msg):
    ERRORS.append(msg)


# ───────────────────────── references ─────────────────────────
def _apa_author(name):
    parts = name.split(" ")
    if len(parts) >= 2 and re.fullmatch(r"[A-Z]{1,4}", parts[-1]):
        initials = " ".join(f"{c}." for c in parts[-1])
        return f"{' '.join(parts[:-1])}, {initials}"
    return name  # collective author


def _apa_authors(names):
    a = [_apa_author(n) for n in names]
    if not a:
        return ""
    if len(a) == 1:
        return a[0]
    if len(a) <= 20:
        return ", ".join(a[:-1]) + ", &amp; " + a[-1]
    return ", ".join(a[:19]) + ", ... " + a[-1]


def _pages(p):
    p = p.strip()
    m = re.fullmatch(r"(S?)(\d+)-(S?)(\d+)", p)
    if m:
        pre1, a, pre2, b = m.groups()
        if len(b) < len(a):
            b = a[: len(a) - len(b)] + b
        return f"{pre1}{a}–{pre2 or pre1}{b}"
    return p


def _issue(i):
    i = i.replace("_suppl_", ", Suppl. ").replace(" Suppl ", ", Suppl. ")
    return i


def build_refs():
    raw_path = DATA / "refs_pubmed_raw.json"
    raw = json.loads(raw_path.read_text(encoding="utf-8")) if raw_path.exists() else {}
    refs = dict(C.MANUAL_REFS)
    for key, pmid in C.PUBMED_REFS.items():
        r = raw.get(pmid)
        if not r:
            err(f"reference {key}: PMID {pmid} missing from refs_pubmed_raw.json")
            continue
        authors = C.GROUP_AUTHORS.get(pmid) or _apa_authors(r["authors"])
        if not authors.endswith("."):
            authors += "."
        title = C.TITLE_OVERRIDES.get(pmid, r["title"]).rstrip(".")
        journal = C.JOURNALS.get(r["journal"])
        if not journal:
            err(f"reference {key}: no full journal name for '{r['journal']}'")
            journal = r["journal"]
        vol = f"<em>{r['volume']}</em>" if r["volume"] else ""
        iss = f"({_issue(r['issue'])})" if r["issue"] else ""
        pages = _pages(r["pages"])
        doi = r.get("doi", "")
        link = (f' <a href="https://doi.org/{doi}">https://doi.org/{doi}</a>' if doi
                else f' <a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/">https://pubmed.ncbi.nlm.nih.gov/{pmid}/</a>')
        tail = ", ".join(x for x in [f"{vol}{iss}", pages] if x)
        refs[key] = f"{authors} ({r['year']}). {html.escape(title, quote=False)}{"" if title[-1:] in "?!" else "."} <em>{journal}</em>, {tail}.{link}"
    return refs


REFS = build_refs()


def number_refs(mod):
    """Order references by first appearance in the lesson, then quiz sources."""
    order = []
    blob = "".join(s["html"] for s in mod["sections"])
    for k in re.findall(r"\[\[([a-z0-9_]+)\]\]", blob):
        if k not in order:
            order.append(k)
    for q in mod["quiz"]:
        for k in q["sources"]:
            if k not in order:
                order.append(k)
    for k in order:
        if k not in REFS:
            err(f"module {mod['id']}: unknown reference key [[{k}]]")
    return [k for k in order if k in REFS]


def cite(text, order):
    def sub(m):
        k = m.group(1)
        if k not in order:
            return ""
        n = order.index(k) + 1
        return f'<sup class="nc-cite"><a href="#ref-{n}" data-ref="{n}" aria-label="Reference {n}">{n}</a></sup>'
    return merge_cites(re.sub(r"\[\[([a-z0-9_]+)\]\]", sub, text))


def merge_cites(h):
    """Join back-to-back citations into one superscript, "12,13". (A CSS sibling rule cannot do this:
    it also fires when words separate two citations.)"""
    return re.sub(r'</a></sup>\s*<sup class="nc-cite"><a', '</a>,<a', h)


# ───────────────────────── helpers ─────────────────────────
def visible_text(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", h))


def abbr_used(body_html):
    txt = visible_text(body_html)
    used = []
    for tok in ABBR:
        if re.search(r"(?<![A-Za-z0-9\-])" + re.escape(tok) + r"(?![A-Za-z0-9])", txt):
            used.append(tok)
    return sorted(used, key=str.lower)


def auto_expand(body_html, page):
    """Safety net for the first-use acronym rule: if an abbreviation is used but never
    introduced with its expansion, expand its first occurrence in running text. Headings,
    links, legends, table headers and module-card titles are never rewritten."""
    txt = visible_text(body_html)
    skip_open = re.compile(r"<(a|h[1-4]|legend|th|button)\b", re.I)
    skip_close = re.compile(r"</(a|h[1-4]|legend|th|button)>", re.I)
    for tok in abbr_used(body_html):
        exp = ABBR[tok][0]
        if re.search(re.escape(f"({tok})"), txt) or re.search(re.escape(tok) + r"\s*\(", txt):
            continue
        pat = re.compile(r"(?<![A-Za-z0-9\-])" + re.escape(tok) + r"(?![A-Za-z0-9])")
        parts = re.split(r"(<[^>]+>)", body_html)
        done, depth = False, 0
        for i, seg in enumerate(parts):
            if seg.startswith("<"):
                if skip_open.match(seg):
                    depth += 1
                elif skip_close.match(seg):
                    depth = max(0, depth - 1)
                continue
            if done or depth:
                continue
            if pat.search(seg):
                parts[i] = pat.sub(f"{exp} ({tok})", seg, count=1)
                done = True
        if done:
            body_html = "".join(parts)
            print(f"  [auto-expanded] {page}: {tok}")
        else:
            print(f"  [NOT expanded: only in headings/links] {page}: {tok}")
    return body_html


def page_meta(fname):
    """(title, description) of an existing guide or calculator page."""
    p = GUIDES / fname
    if not p.exists():
        return None
    s = p.read_text(encoding="utf-8", errors="ignore")[:20000]
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    title = html.unescape(t.group(1)).strip() if t else fname
    title = re.split(r"\s+[·|—–]\s+(?:Renal Care Matters|W\.? ?G?\.? ?M?\.? ?Rivero|Dr\.).*$", title)[0].strip()
    desc = html.unescape(d.group(1)).strip() if d else ""
    return title, desc


def template_chunk(start_pat, end_pat):
    s = TEMPLATE.read_text(encoding="utf-8")
    m = re.search(start_pat + r".*?" + end_pat, s, re.S)
    if not m:
        raise SystemExit(f"template chunk not found: {start_pat}")
    return m.group(0)


HEADER = template_chunk(r'<header class="site-header">', r"</header>")
# site-wide header brand is "HOME" (some older templates still carry the name)
HEADER = re.sub(r'<a class="brand" href="https://renalcarematters.com">.*?</a>',
                '<a href="https://renalcarematters.com" class="brand">HOME</a>', HEADER, flags=re.S)
FLOATING = template_chunk(r"<!-- ═══ FLOATING BUTTONS", r"(?=<!-- ═══ SCRIPTS)")
FONTS = template_chunk(r'<link rel="preconnect" href="https://fonts.googleapis.com">', r"<!-- /FONTS-ASYNC -->")

COURSE_CSS = """
/* Nephrology Nursing & Hemodialysis course — guide-specific styles (second <style> block so
   patch_master_css.py never strips them). Tokens only, so light and dark mode both hold. */
.nc-bar{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin:14px 0 4px;font-size:13.5px;color:var(--text-mid);}
.nc-bar a{color:var(--teal);font-weight:600;text-decoration:none;}
.nc-bar a:hover{text-decoration:underline;}
.nc-bar .nc-sep{color:var(--text-faint);}
.nc-bar .nc-spacer{flex:1 1 auto;}
.nc-chip{display:inline-block;font-size:11.5px;font-weight:700;letter-spacing:.03em;padding:2px 10px;border-radius:999px;border:1px solid var(--border);background:var(--bg);color:var(--text-mid);}
.nc-chip-core{background:var(--teal-light);border-color:var(--teal);color:var(--teal);}
html[data-theme="dark"] .nc-chip-core{background:#0a2830;color:#7fd6dd;border-color:#2c7f88;}
.nc-obj{margin:6px 0 0;padding-left:22px;}
.nc-obj li{margin:6px 0;line-height:1.6;}
.section ul:not(.nc-obj){line-height:1.65;}
.nc-case{border:1px solid var(--border);border-left:4px solid var(--teal);border-radius:12px;background:var(--white);padding:16px 20px;margin:14px 0;}
.nc-case h3{margin:0 0 6px;font-family:Inter,system-ui,sans-serif;font-size:1.02rem;color:var(--text);}
.nc-acte{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0;}
.nc-acte-card{border:1px solid var(--border);border-radius:12px;background:var(--white);padding:12px 16px;}
.nc-acte-card h4{margin:0 0 4px;font-family:Inter,system-ui,sans-serif;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);}
html[data-theme="dark"] .nc-acte-card h4{color:#7fd6dd;}
.nc-acte-card div{font-size:14.5px;line-height:1.6;color:var(--text-mid);}
.nc-task{border:1px dashed var(--border);border-radius:12px;padding:12px 16px;margin:12px 0;background:var(--bg);font-size:14.5px;line-height:1.6;color:var(--text-mid);}
.nc-task strong{color:var(--text);}
/* calculator cards: same component and look as the guides (patch_calc_cards.py) */
.calc-cards-wrap{max-width:860px;margin:28px auto 8px;padding:0;box-sizing:border-box;}
.calc-cards-label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--teal);margin-bottom:12px;}
a.calc-card{display:flex;align-items:center;gap:14px;background:rgba(26,107,114,.07);border:1px solid rgba(26,107,114,.2);border-radius:12px;padding:14px 16px;text-decoration:none;color:inherit;margin-bottom:10px;transition:border-color .18s,box-shadow .18s;}
a.calc-card:hover{border-color:var(--teal);box-shadow:0 2px 14px rgba(26,107,114,.14);}
a.calc-card *{text-decoration:none;}
.calc-card-icon{width:36px;height:36px;flex:none;background:var(--teal);color:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;font-weight:700;line-height:1;}
.calc-card-body{flex:1;min-width:0;}
.calc-card-title{font-size:.88rem;font-weight:700;color:var(--teal);margin-bottom:2px;}
.calc-card-desc{font-size:.78rem;color:var(--text-mid,#4b5563);line-height:1.4;}
.calc-card-arrow{flex:none;font-size:.8rem;font-weight:700;color:var(--teal);white-space:nowrap;padding-left:8px;}
html[data-theme="dark"] a.calc-card{background:rgba(26,107,114,.16);border-color:rgba(26,107,114,.4);}
html[data-theme="dark"] .calc-card-title,html[data-theme="dark"] .calc-card-arrow{color:#5ad2be;}
html[data-theme="dark"] .calc-card-desc{color:var(--text-mid);}
html[data-theme="dark"] .calc-card-icon{background:#0e4a50;}
.nc-fig{margin:22px auto 6px;max-width:100%;}
.nc-fig img{display:block;width:100%;height:auto;border-radius:12px;border:1px solid var(--border);background:#fff;}
.nc-fig-card{max-width:780px;}
.nc-fig-tall{max-width:560px;}
.nc-fig figcaption{font-size:0.9rem;line-height:1.5;color:var(--text-muted);margin-top:8px;}
.nc-quiz{margin:10px 0 0;}
.nc-q{border:1px solid var(--border);border-radius:12px;background:var(--white);padding:14px 18px 10px;margin:0 0 16px;min-width:0;}
.nc-q legend{font-family:Inter,system-ui,sans-serif;font-weight:600;font-size:1rem;line-height:1.5;color:var(--text);padding:0 6px;float:left;width:100%;margin-bottom:8px;}
.nc-q legend + *{clear:both;}
.nc-qn{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);font-weight:700;margin-bottom:2px;}
.nc-q.nc-missing{border-color:var(--amber);box-shadow:0 0 0 2px var(--amber-soft);}
.nc-opt{border:1px solid var(--border);border-radius:10px;padding:10px 12px;margin:8px 0;background:var(--bg);}
.nc-opt-row{display:flex;gap:10px;align-items:flex-start;}
.nc-opt input{flex:none;width:20px;height:20px;margin:3px 0 0;accent-color:var(--teal);}
.nc-opt label{flex:1;font-size:15px;line-height:1.55;color:var(--text);cursor:pointer;}
.nc-opt input:focus-visible{outline:3px solid var(--teal);outline-offset:2px;}
.nc-opt-correct{border-color:var(--green);border-left-width:5px;}
.nc-opt-chosen-wrong{border-color:var(--red);border-left-width:5px;}
.nc-verdict{display:block;font-size:13px;font-weight:700;margin:6px 0 0 30px;color:var(--text);}
.nc-verdict:empty{display:none;}
.nc-rat{margin:4px 0 2px 30px;font-size:14px;line-height:1.6;color:var(--text-mid);}
.nc-actions{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:6px 0 12px;}
.nc-btn{font:600 15px Inter,system-ui,sans-serif;border-radius:10px;border:1px solid #0e4a50;background:#0e4a50;color:#fff;padding:10px 20px;cursor:pointer;min-height:44px;}
.nc-btn:hover{background:#0b3b40;}
.nc-btn:focus-visible{outline:3px solid var(--teal);outline-offset:3px;}
.nc-btn-ghost{background:var(--white);color:var(--text);border-color:var(--border);}
.nc-btn-ghost:hover{background:var(--bg);}
.nc-remember{display:flex;gap:8px;align-items:flex-start;font-size:13.5px;line-height:1.5;color:var(--text-mid);margin:0 0 12px;}
.nc-remember input{width:18px;height:18px;margin-top:2px;accent-color:var(--teal);}
.nc-result{border-radius:12px;font-size:15px;line-height:1.6;color:var(--text);}
.nc-result:empty{display:none;}
.nc-result-warn{background:var(--amber-soft);border:1px solid var(--amber);padding:12px 16px;}
.nc-result-done{background:var(--green-soft);border:1px solid var(--green);padding:12px 16px;}
html[data-theme="dark"] .nc-result-warn,html[data-theme="dark"] .nc-result-done{background:#1a2535;}
.nc-result:focus{outline:3px solid var(--teal);outline-offset:2px;}
.nc-check{list-style:none;margin:10px 0 0;padding:0;}
.nc-check li{position:relative;padding:6px 0 6px 30px;line-height:1.55;border-bottom:1px solid var(--border);}
.nc-check li::before{content:"";position:absolute;left:2px;top:9px;width:16px;height:16px;border:2px solid var(--text-muted);border-radius:4px;}
.nc-read{list-style:none;margin:8px 0 0;padding:0;}
.nc-read li{padding:9px 0;border-bottom:1px solid var(--border);line-height:1.55;}
.nc-read a{font-weight:600;color:var(--teal);}
.nc-read span{display:block;font-size:14px;color:var(--text-mid);}
.nc-nextprev{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:10px 0;}
.nc-np{display:block;border:1px solid var(--border);border-radius:12px;background:var(--white);padding:12px 16px;text-decoration:none;color:var(--text);}
.nc-np:hover{border-color:var(--teal);}
.nc-np small{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);font-weight:700;}
.nc-np-next{text-align:right;}
.section .table-wrap a,.nc-task a{color:var(--teal);font-weight:600;}
.nc-cite a{text-decoration:none;font-weight:700;color:var(--teal);padding:0 1px;}
/* hub */
.nc-paths{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:14px 0;}
.nc-path{text-align:left;border:2px solid var(--border);border-radius:14px;background:var(--white);padding:14px 18px;cursor:pointer;font:inherit;color:var(--text);min-height:44px;}
.nc-path[aria-pressed="true"]{border-color:var(--teal);box-shadow:0 0 0 3px var(--teal-light);}
html[data-theme="dark"] .nc-path[aria-pressed="true"]{box-shadow:0 0 0 3px #0a2830;}
.nc-path:focus-visible{outline:3px solid var(--teal);outline-offset:3px;}
.nc-path b{display:block;font-family:Inter,system-ui,sans-serif;font-size:1.02rem;margin-bottom:4px;}
.nc-path span{display:block;font-size:14px;line-height:1.55;color:var(--text-mid);}
.nc-pathnote{font-size:14px;color:var(--text-mid);margin:4px 0 12px;}
.nc-modgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:8px 0 0;}
.nc-mod{display:flex;flex-direction:column;gap:6px;border:1px solid var(--border);border-radius:14px;background:var(--white);padding:14px 16px;text-decoration:none;color:var(--text);}
.nc-mod:hover{border-color:var(--teal);box-shadow:0 2px 14px rgba(26,107,114,.12);}
.nc-mod-top{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);font-weight:700;}
.nc-mod-title{font-family:Inter,system-ui,sans-serif;font-weight:600;font-size:1.02rem;line-height:1.35;}
.nc-mod-desc{font-size:14px;line-height:1.55;color:var(--text-mid);}
.nc-mod-status{font-size:12.5px;font-weight:700;color:var(--text-muted);}
.nc-mod-done{color:var(--green);}
#nc-modules[data-path="neph"] .nc-emph-hd,#nc-modules[data-path="hd"] .nc-emph-neph{display:none;}
.nc-progress{display:flex;flex-wrap:wrap;gap:10px;align-items:center;border:1px solid var(--border);border-radius:12px;padding:10px 14px;margin:10px 0;background:var(--bg);font-size:14px;color:var(--text-mid);}
.nc-progress[hidden],.nc-btn[hidden],.nc-rat[hidden],.nc-q[hidden]{display:none !important;}
.nc-sign td{height:34px;}
.nc-box{display:inline-block;width:15px;height:15px;border:2px solid var(--text-muted);border-radius:3px;vertical-align:-2px;}
@media (max-width:720px){
  .nc-acte,.nc-nextprev,.nc-paths,.nc-modgrid{grid-template-columns:1fr;}
  .nc-np-next{text-align:left;}
}
.nc-psn td{vertical-align:top;font-size:14.5px;}
.nc-plain{list-style:disc;padding-left:1.2em;}
.nc-osce{border:1px solid var(--border);border-radius:12px;padding:6px 16px 10px;margin:16px 0;background:var(--white);break-inside:avoid;}
.nc-osce-min{font-size:.75rem;font-weight:600;color:var(--text-muted);margin-left:8px;}
.nc-osce-crit{margin:6px 0 0;}
ul.nc-osce-crit{padding-left:1.2em;color:var(--text-mid);}
.nc-osce-note{font-size:14px;color:var(--text-muted);}
/* competencies */
.nc-lv{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.02em;border-radius:999px;padding:2px 9px;white-space:nowrap;border:1px solid transparent;}
.nc-lv-K{background:#eef1f5;color:#43536a;border-color:#d5dbe4;}
.nc-lv-S{background:#fdf3dd;color:#8a5a00;border-color:#f1d899;}
.nc-lv-D{background:#e3f2f1;color:#13636a;border-color:#b6dcd9;}
.nc-lv-I{background:#1f3864;color:#fff;border-color:#1f3864;}
html[data-theme="dark"] .nc-lv-K{background:#243042;color:#c9d3e1;border-color:#34445c;}
html[data-theme="dark"] .nc-lv-S{background:#3a2e12;color:#f3cf7a;border-color:#5a4718;}
html[data-theme="dark"] .nc-lv-D{background:#12393b;color:#7fd6dd;border-color:#1d5a5d;}
html[data-theme="dark"] .nc-lv-I{background:#cfe0ff;color:#0f1e2e;border-color:#cfe0ff;}
.nc-lv-legend{list-style:none;margin:10px 0 14px;padding:0;display:grid;gap:6px;font-size:14px;color:var(--text-mid);line-height:1.5;}
.nc-lv-legend li .nc-lv{margin-right:6px;}
.nc-milestone{border:1px solid var(--border);border-left:4px solid var(--teal);border-radius:12px;background:var(--white);padding:12px 16px;margin:12px 0;line-height:1.6;}
.nc-comp td{vertical-align:top;}
.nc-pm th,.nc-pm td{text-align:center;padding:6px 4px;}
.nc-pm th[scope="row"],.nc-pm thead th:first-child{text-align:left;min-width:190px;font-weight:600;}
.nc-pm-mod a{color:var(--teal);font-weight:700;text-decoration:none;}
.nc-pm-cell .nc-lv{padding:2px 7px;}
.nc-pm-none{color:var(--text-faint);}
.nc-h3{font-family:Inter,system-ui,sans-serif;font-size:1.02rem;margin:22px 0 6px;color:var(--text);}
.nc-milestones{margin:8px 0 0;padding-left:1.2em;line-height:1.65;}
.nc-milestones li{margin-bottom:6px;}
@media print{
  .nc-bar,.nc-actions,.nc-remember,.nc-nextprev,.nc-paths,.nc-progress,.nav-strip{display:none !important;}
  .nc-q,.nc-case,.nc-acte-card,.nc-mod{break-inside:avoid;box-shadow:none !important;}
  .nc-opt{background:#fff !important;}
  .nc-print-break{break-before:page;}
  .nc-sign td{height:40px;}
  body.nc-educator .section{break-inside:auto;}
}
"""

INLINE_JS = """
const DARK_KEY = 'wgmr-dark';
function toggleDark() {
  const on = document.documentElement.getAttribute('data-theme') !== 'dark';
  document.documentElement.setAttribute('data-theme', on ? 'dark' : '');
  const lbl = document.getElementById('darkLabel');
  if (lbl) lbl.textContent = on ? 'Light' : 'Dark';
  try { localStorage.setItem(DARK_KEY, on ? '1' : '0'); } catch (e) {}
}
(function() {
  try {
    if (localStorage.getItem(DARK_KEY) === '1') {
      document.documentElement.setAttribute('data-theme', 'dark');
      const lbl = document.getElementById('darkLabel');
      if (lbl) lbl.textContent = 'Light';
    }
  } catch (e) {}
})();
(function() {
  var b = document.getElementById('scrollTopBtn');
  if (!b) return;
  window.addEventListener('scroll', function() { b.classList.toggle('visible', window.scrollY > 300); }, { passive: true });
})();
// English-only course: language stub keeps shared scripts happy
const GLANG_KEY = 'wgmr-lang';
function setGuideLang(lang) { try { localStorage.setItem(GLANG_KEY, lang); } catch (e) {} }
"""


def glossary_block(body_html, terms):
    used = abbr_used(body_html)
    dt = 'style="font-weight:700;color:var(--text);"'
    rows = []
    for tok in used:
        exp, note = ABBR[tok]
        text = exp[0].upper() + exp[1:] + ("." if not note else f" &mdash; {note}")
        rows.append(f'    <dt {dt}>{tok}</dt><dd style="margin:0;">{text}</dd>')
    trows = [f'    <dt {dt}>{t}</dt><dd style="margin:0;">{d}</dd>' for t, d in terms]
    h4 = ('<h4 style="font-family:Inter,system-ui,sans-serif;font-size:13px;font-weight:700;letter-spacing:.04em;'
          'text-transform:uppercase;color:var(--text-muted);margin:8px 0 4px;">')
    dl = '<dl style="display:grid;grid-template-columns:max-content 1fr;column-gap:14px;row-gap:4px;margin:0 0 16px;">'
    terms_html = f"  {h4}Terms</h4>\n  {dl}\n" + "\n".join(trows) + "\n  </dl>\n" if trows else ""
    return f"""<!-- GLOSSARY-START -->
<section class="glossary-section" style="max-width:860px;margin:8px auto 0;padding:0 32px;">
<details class="glossary-acc" style="border:1px solid var(--border);border-radius:12px;background:var(--white);overflow:hidden;">
<summary style="cursor:pointer;list-style:none;padding:15px 20px;font-family:Inter,system-ui,sans-serif;font-weight:600;font-size:15px;color:var(--text);display:flex;align-items:center;gap:10px;">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;color:var(--teal);"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
<span data-lang="en">Glossary &amp; abbreviations</span><span class="lang-hidden" data-lang="tl">Talahulugan at mga daglat</span><span class="lang-hidden" data-lang="ceb">Talaan sa mga pulong ug daglat</span><span class="lang-hidden" data-lang="kap">Talatinigan ampo reng daglat</span>
<span style="margin-left:auto;font-weight:500;font-size:12px;color:var(--text-muted);">terms used on this page</span>
</summary>
<div style="padding:6px 26px 20px 26px;font-size:13.5px;line-height:1.7;color:var(--text-mid);">
  {h4}Abbreviations</h4>
  {dl}
{chr(10).join(rows)}
  </dl>
{terms_html}</div>
</details>
</section>
<!-- GLOSSARY-END -->"""


def related_block(cards):
    out = ['<!-- RELATED-GUIDES-START -->', '<div class="related-guides">', '  <h2>Related Guides</h2>', '  <div class="related-cards">']
    for href, tag, title, desc in cards:
        slug = href[:-5]
        thumb = ROOT / "images" / f"{slug}-rg-thumb.webp"
        cls, img = "related-card", ""
        if thumb.exists():
            cls = "related-card has-thumb"
            img = f'\n      <img class="related-card-thumb" src="../images/{slug}-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160">'
        out.append(f'    <a class="{cls}" href="{href}">\n      <div class="related-card-tag">{tag}</div>\n'
                   f'      <div class="related-card-title">{title}</div>\n      <div class="related-card-desc">{desc}</div>\n'
                   f'      <div class="related-card-arrow">Read →</div>{img}</a>')
    out += ['  </div>', '</div>', '<!-- RELATED-GUIDES-END -->']
    return "\n".join(out)


RESET_PUBLISHED = False


def existing_published(fname):
    if RESET_PUBLISHED:
        return None
    p = ROOT / "academy" / fname          # finished pages live in academy/ (tools/academy/publish_academy.py)
    if not p.exists():
        p = GUIDES / fname
    if p.exists():
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', p.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return None


def shell(fname, title, desc, keywords, hero_tag, h1, sub, audience, nav, pre_main, main, glossary, related,
          body_class="", jsonld_extra=None, hero_img=None, disclaimer=None):
    slug = fname[:-5]
    url = f"{SITE}/guides/{slug}"
    pub = existing_published(fname)
    pub_meta = f'\n<meta property="article:published_time" content="{pub}">' if pub else ""
    og_img = None
    # share image: this page's hero (patch_og_images.py writes the <=300 KB JPEG into images/og/),
    # else the Module 12 team picture for the hub and educator page, else the dialysis category image
    team = f"{COURSE['hub_slug']}-12-philippine-practice-quality-capstone-vignette-hero"
    for cand in (f"images/og/{slug}-vignette-hero.jpg", f"images/{slug}-vignette-hero.png",
                 f"images/og/{team}.jpg", f"images/{team}.png", "images/hero-cat-dialysis.webp"):
        if (ROOT / cand).exists():
            og_img = f"{SITE}/{cand}"
            break
    og_tags = ""
    if og_img:
        og_tags = (f'\n<meta property="og:image" content="{og_img}">\n<meta property="og:image:alt" content="{html.escape(title)}">'
                   f'\n<meta name="twitter:image" content="{og_img}">')
    ld = {
        "@context": "https://schema.org", "@type": "MedicalWebPage", "name": title, "url": url,
        "author": {"@type": "Physician", "name": "William Gregory M. Rivero, MD, FPCP, DPSN", "url": SITE + "/"},
        "inLanguage": "en-PH",
        "audience": {"@type": "MedicalAudience", "audienceType": "Registered nurses"},
        "about": {"@type": "MedicalSpecialty", "name": "Nephrology nursing"},
        "isAccessibleForFree": True,
    }
    if jsonld_extra:
        ld.update(jsonld_extra)
    figure = ""
    if hero_img and (ROOT / "images" / f"{hero_img['file']}.png").exists():
        f = hero_img["file"]
        webp = f'<source srcset="../images/{f}.webp" type="image/webp">' if (ROOT / "images" / f"{f}.webp").exists() else ""
        figure = f"""
      <figure class="hero-figure">
        <div class="hero-vignette">
          <picture>
            {webp}
            <img src="../images/{f}.png" alt="{html.escape(html.unescape(hero_img['alt']))}" width="2048" height="2048" fetchpriority="high" loading="eager">
          </picture>
        </div>
      </figure>"""
    pills = "\n".join(f'<a class="nav-pill" href="#{i}">{t}</a>' for i, t in nav)
    disc = disclaimer or ("Educational self-study for registered nurses. Does not replace physician orders, approved unit "
                          "procedures, manufacturer instructions, DOH licensing requirements, or supervised clinical training.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="keywords" content="{html.escape(keywords)}">
<meta name="author" content="W Rivero, MD, FPCP, DPSN">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/svg+xml" href="/brand/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0f1e33">
<meta property="og:type" content="article">{pub_meta}
<meta property="og:site_name" content="Renal Care Matters">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_PH">{og_tags}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
{FONTS}
<style>
/* master CSS is written here by patch_master_css.py */
</style>
<style id="nursing-course-style">{COURSE_CSS}</style>
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>

<body class="physician-mode single-mode{(' ' + body_class) if body_class else ''}">

<!-- ═══ SITE HEADER ═════════════════════════════ -->
{HEADER}

<!-- ═══ HERO ════════════════════════════════════ -->
<div class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-copy">
        <div class="hero-tag">{hero_tag}</div>
        <h1>{h1}</h1>
        <p class="hero-sub">{sub}</p>
        <div class="hero-meta">
<span><strong>Audience:</strong> {audience}</span>
</div>
      </div><!-- /.hero-copy -->{figure}
    </div><!-- /.hero-grid -->
  </div>
</div>

<!-- ═══ SECTION NAVIGATION ═════════════════════════ -->
<nav class="nav-strip">
<div class="nav-pills">
{pills}
</div>
</nav>

{pre_main}

<!-- ═══ MAIN CONTENT ════════════════════════════════ -->
<main class="container">
{main}
</main>

{glossary}

<!-- DR CARD -->
<div class="dr-card-wrap">
  <div class="dr-card">
    <div class="dr-avatar">
      <picture>
        <source srcset="../images/avatar-128.webp" type="image/webp">
        <img decoding="async" style="width:100%;height:auto;display:block;" src="../images/avatar-128.png" alt="Dr. William Gregory M. Rivero, MD" loading="lazy" width="80" height="80">
      </picture>
    </div>
    <div class="dr-card-body">
      <h4>William Gregory Rivero, MD, FPCP, DPSN</h4>
      <p>Internal Medicine &middot; Nephrology &middot; Nutrition &middot; Philippines &middot; PRC 0105184</p>
      <p style="margin-top:8px;font-size:12px;color:var(--text-muted);font-style:italic;">{disc}</p>
    </div>
    <div class="dr-qr">
      <a href="https://www.seriousmd.com/doc/williamrivero" target="_blank" rel="noopener" aria-label="Scan QR code to save Dr. Rivero's contact information"><img src="../images/dr-rivero-contact-qr.svg" alt="QR code — scan to save Dr. Rivero's contact info" width="80" height="80" loading="lazy"></a>
      <p class="dr-qr-label">Scan and save</p>
    </div>
  </div>
</div>

{related}

<footer class="guide-footer">
<div class="footer-inner">
<p class="rcm-attrib">© 2026 <a href="https://renalcarematters.com">renalcarematters.com</a></p>
</div>
</footer>

{FLOATING}
<!-- ═══ SCRIPTS ══════════════════════════════════════════════════════════ -->
<script>{INLINE_JS}</script>
<script src="../assets/nursing-course.js" defer></script>
</body>
</html>
"""


def role_chip(m, long=False):
    out = []
    for key, label in (("neph", "Nephrology Nursing path"), ("hd", "Hemodialysis Nursing path")):
        core = m[key] == "core"
        txt = f"{label}: {'emphasized' if core else ('advanced, after the capstone' if m[key] == 'advanced' else 'foundation')}"
        out.append(f'<span class="nc-chip{" nc-chip-core" if core else ""}">{txt}</span>')
    return " ".join(out)


# ───────────────────────── competencies ─────────────────────────
LEVELS = "KSDI"


def level_chip(code, short=False):
    name, note = C.COMPETENCY_LEVELS[code]
    return f'<span class="nc-lv nc-lv-{code}" title="{html.escape(html.unescape(name))}: {html.escape(html.unescape(note))}">{code if short else name}</span>'


def check_competencies(m):
    for i, c in enumerate(m["competencies"], 1):
        if c.get("thread") not in C.COMPETENCY_THREADS:
            err(f"module {m['id']} competency {i}: unknown thread {c.get('thread')}")
        if c.get("level") not in C.COMPETENCY_LEVELS:
            err(f"module {m['id']} competency {i}: unknown level {c.get('level')}")
        for e in c.get("evidence", []):
            if e not in C.COMPETENCY_EVIDENCE:
                err(f"module {m['id']} competency {i}: unknown evidence label {e}")


def level_legend():
    items = "".join(f"<li>{level_chip(k)} {v[1]}</li>" for k, v in C.COMPETENCY_LEVELS.items())
    return f'<ul class="nc-lv-legend">{items}</ul>'


def competency_section(m):
    if not m["competencies"]:
        return ""
    check_competencies(m)
    rows = "\n".join(
        f'<tr><td>{c["statement"]}</td><td>{C.COMPETENCY_THREADS[c["thread"]]}</td><td>{level_chip(c["level"])}</td>'
        f'<td>{", ".join(c.get("evidence", []))}</td></tr>' for c in m["competencies"])
    ms = f'<div class="nc-milestone"><strong>Milestone.</strong> {m["milestone"]}</div>' if m["milestone"] else ""
    return f"""<section class="section" id="competencies">
  <div class="section-tag">Competencies</div>
  <h2>What this module builds</h2>
  {ms}
  <p>Each competency names an observable ability, the level this module aims for, and how that level is confirmed. Levels follow Miller&rsquo;s pyramid. Self-study reaches <em>knows</em>; the higher levels are reached only when an educator or preceptor verifies them, and they are recorded on the <a href="{COURSE['educator_slug']}.html#checklist">competency checklist</a>.</p>
  {level_legend()}
  <div class="table-wrap"><table class="nc-comp">
  <thead><tr><th style="width:50%;">Competency</th><th>Thread</th><th>Target level</th><th>Verified by</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
</section>"""


def progression_section():
    mods = [MODS[i] for i in ORDER if MODS[i]["competencies"]]
    if not mods:
        return ""
    head = "".join(f'<th class="nc-pm-mod"><a href="{m["slug"]}.html" title="{html.escape(html.unescape(m["plain"]))}">{int(m["id"])}</a></th>' for m in mods)
    body = []
    for key, label in C.COMPETENCY_THREADS.items():
        cells, best = [], -1
        for m in mods:
            lv = [LEVELS.index(c["level"]) for c in m["competencies"] if c["thread"] == key]
            if lv:
                best = max(best, max(lv))
                cells.append(f'<td class="nc-pm-cell">{level_chip(LEVELS[max(lv)], short=True)}</td>')
            else:
                cells.append('<td class="nc-pm-cell nc-pm-none"><span aria-hidden="true">&middot;</span></td>')
        top = level_chip(LEVELS[best]) if best >= 0 else ""
        body.append(f"<tr><th scope=\"row\">{label}</th>{''.join(cells)}<td>{top}</td></tr>")
    ms = "\n".join(f'<li><a href="{m["slug"]}.html">Module {int(m["id"])}</a> &middot; {m["milestone"]}</li>' for m in mods if m["milestone"])
    return f"""<section class="section" id="progression">
  <div class="section-tag">Competency progression</div>
  <h2>How competence builds from module to module</h2>
  <p>Twelve competency threads run through the course. Each cell shows the highest level a module aims for in that thread; the last column is the level reached by the end of the course. Read across a row to see a skill grow, for example from explaining fluid assessment in Module 1 to completing full treatment assessments on your own, after sign-off, in Module 9. Each module page lists its competencies in full, and the <a href="{COURSE['educator_slug']}.html#checklist">educator checklist</a> records them.</p>
  {level_legend()}
  <div class="table-wrap"><table class="nc-pm">
  <thead><tr><th>Thread</th>{head}<th>By the end</th></tr></thead>
  <tbody>
{chr(10).join(body)}
  </tbody></table></div>
  <h3 class="nc-h3">Milestones</h3>
  <ol class="nc-milestones">
{ms}
  </ol>
</section>
"""


# ───────────────────────── PSN alignment and OSCE bank (educator page) ─────────────────────────
def _mlink(ref):
    """'09:hd-drugs' or '09' -> link to the module (and section)."""
    mid, _, sec = ref.partition(":")
    if mid not in MODS:
        err(f"educator_psn: unknown module {mid}")
        return html.escape(ref)
    m = MODS[mid]
    nav = next((x['nav'] for x in m['sections'] if x['id'] == sec), sec) if sec else ""
    for _a, _x in (("HDF", "hemodiafiltration"), ("CRRT", "continuous kidney replacement therapy"), ("HD", "hemodialysis"),
                   ("PD", "peritoneal dialysis"), ("CKD", "kidney disease"), ("AKI", "acute kidney injury")):
        nav = re.sub(rf"\b{_a}\b", _x, nav)
    label = f"Module {int(mid)}" + (f" &middot; {nav}" if sec else "")
    if sec and sec not in [x["id"] for x in m["sections"]]:
        err(f"educator_psn: module {mid} has no section {sec}")
    return f'<a href="{m["slug"]}.html{"#" + sec if sec else ""}">{label}</a>'


def psn_sections():
    if not (CONTENT / "educator_psn.py").exists():
        return ""
    E = load("educator_psn")
    cov = {"full": ("Covered", "D"), "extends": ("Covered and extended", "I"), "partial": ("Partly covered", "S")}
    rows = []
    for r in E.ALIGNMENT:
        where = ", ".join(_mlink(x) for x in (r.get("sections") or r.get("modules") or []))
        lab, code = cov.get(r.get("coverage", ""), (r.get("coverage", ""), "K"))
        rows.append(f'<tr><td>{r["area"]}</td><td>{where or "&mdash;"}</td><td><span class="nc-lv nc-lv-{code}">{lab}</span></td><td>{r.get("note", "")}</td></tr>')
    sch = E.BLENDED_SCHEDULE
    days = []
    for d in sch["days"]:
        blocks = "".join(
            f'<li><strong>{b.get("time_hint", "").capitalize()}.</strong> {b["activity"]}'
            + (f' Modules: {", ".join(_mlink(x) for x in b.get("modules", []))}.' if b.get("modules") else "")
            + (f' Stations: {", ".join(b.get("stations", []))}.' if b.get("stations") else "") + "</li>" for b in d["blocks"])
        days.append(f'<h3 class="nc-h3">Day {d["day"]}: {d["focus"]}</h3><ul class="nc-read nc-plain">{blocks}</ul>')
    st = []
    for x in E.OSCE_STATIONS:
        chk = "".join(f'<tr class="nc-sign"><td>{c}</td><td></td><td></td></tr>' for c in x["checklist"])
        crit = "".join(f"<li>{c}</li>" for c in x.get("critical", []))
        mods = ", ".join(_mlink(m) for m in x.get("modules", []))
        st.append(f"""  <div class="nc-osce">
  <h3 class="nc-h3">Station {x["id"]}: {x["title"]} <span class="nc-osce-min">{x["minutes"]} minutes</span></h3>
  <p><strong>Task.</strong> {x["task"]} <strong>Setup.</strong> {x["setup"]} <strong>Study:</strong> {mods}.</p>
  <div class="table-wrap"><table>
  <thead><tr><th style="width:62%;">Observable step</th><th>Done</th><th>Not done</th></tr></thead>
  <tbody>
{chk}
  </tbody></table></div>
  <p class="nc-osce-crit"><strong>Critical errors (any one fails the station):</strong></p><ul class="nc-osce-crit">{crit}</ul>
  <p class="nc-osce-note">{x.get("examiner_note", "")}</p>
  </div>""")
    return f"""<section class="section" id="psn">
  <div class="section-tag">Philippine Society of Nephrology</div>
  <h2>How the modules align with the PSN Basic Course for Renal Nurses</h2>
  <p>The PSN offers face-to-face basic training for renal nurses. The table below groups the content such training usually covers into broad areas, in our own words, and points to the modules and sections that teach each one, so a nurse can prepare before a course and review after it. The grouping is ours; it does not reproduce any PSN program, it does not mean the PSN has reviewed or endorsed these modules, and completing them does not replace PSN training or certification.</p>
  <div class="table-wrap"><table class="nc-psn">
  <thead><tr><th>Content area</th><th>Where to study it here</th><th>Coverage</th><th>Notes</th></tr></thead>
  <tbody>
{chr(10).join(rows)}
  </tbody></table></div>
  <h3 class="nc-h3">A suggested three-day blended schedule</h3>
  <p>One way a provider could pair the self-study modules with a three-day face-to-face course. It is a suggestion, not a PSN schedule.</p>
  <p><strong>Before the course.</strong> {sch["pre"]}</p>
  {"".join(days)}
  <p><strong>After the course.</strong> {sch["after"]}</p>
  <p><strong>Pretests and post-tests.</strong> {E.PRE_POST}</p>
</section>

<section class="section nc-print-break" id="osce">
  <div class="section-tag">Printable</div>
  <h2>Objective structured clinical examination (OSCE) station bank</h2>
  <p>Each station lists the task, the setup, the observable steps, and the critical errors. Steps follow the modules and the unit&rsquo;s approved procedures; the examiner replaces any step that differs from local protocol before use. Run stations on a simulation arm, mannequin, or unconnected machine, never on a patient.</p>
{chr(10).join(st)}
</section>

"""


# ───────────────────────── module page ─────────────────────────
def build_module(mid):
    m = MODS[mid]
    fname = m["slug"] + ".html"
    n = int(mid)
    order = number_refs(m)
    i = ORDER.index(mid)
    prev_m = MODS[ORDER[i - 1]] if i > 0 else None
    next_m = MODS[ORDER[i + 1]] if i < len(ORDER) - 1 else None
    hub = COURSE["hub_slug"] + ".html"

    parts = []
    obj = "\n".join(f"    <li>{o}</li>" for o in m["objectives"])
    parts.append(f"""<section class="section" id="objectives">
  <div class="section-tag">Learning objectives</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
</section>""")
    for s in m["sections"]:
        parts.append(f"""<section class="section" id="{s['id']}">
  <div class="section-tag">{s['tag']}</div>
  <h2>{s['h2']}</h2>
{cite(s['html'].strip(), order)}
</section>""")
    # case
    c = m["case"]
    acte = "\n".join(f'    <div class="nc-acte-card"><h4>{k}</h4><div>{v}</div></div>' for k, v in c["acte"].items())
    parts.append(f"""<section class="section" id="case">
  <div class="section-tag">Nursing case &middot; fictional</div>
  <h2>Case: {c['title']}</h2>
  <div class="nc-case">
{c['html'].strip()}
  </div>
  <p>Before reading on, decide what you would assess, what you would communicate and to whom, what you would teach, and what would make you escalate. Then compare with the outline below.</p>
  <div class="nc-acte">
{acte}
  </div>
  <div class="nc-task"><strong>Documentation task.</strong> {c['task']}</div>
</section>""")
    # quiz: the whole bank is in the page; assets/nursing-course.js shows DRAW at random
    if len(m["quiz"]) < BANK_SIZE and not os.environ.get("NC_DRAFT"):  # NC_DRAFT=1 while a bank is being written
        err(f"module {mid}: question bank has {len(m['quiz'])} items (must be at least {BANK_SIZE})")
    qs = []
    for qi, q in enumerate(m["quiz"], 1):
        n_correct = sum(1 for o in q["options"] if o[1])
        if n_correct != 1:
            err(f"module {mid} question {qi}: {n_correct} options keyed correct (must be exactly 1)")
        if len(q["options"]) != 4:
            err(f"module {mid} question {qi}: expected 4 options")
        opts = []
        for oi, (text, correct, rat) in enumerate(q["options"]):
            oid = f"q{qi}{'abcd'[oi]}"
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if correct else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{text}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span><div class="nc-rat" hidden>{rat}</div></div>
    </div>""")
        qs.append(f"""  <fieldset class="nc-q" data-q="{qi}">
    <legend><span class="nc-qn">Question {qi} of {len(m['quiz'])}</span>{q['stem']}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Self-assessment</div>
  <h2>Check your understanding</h2>
  <p>Each visit draws {DRAW} questions at random from this module&rsquo;s {len(m['quiz'])}-question bank, in a shuffled order. Choose the single best answer for each, then select <strong>Check answers</strong>; a rationale appears under every option. Reload the page or select <strong>New set of questions</strong> for a different mix. Nothing you select is sent anywhere; scoring happens in your browser.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="{mid}" data-draw="{DRAW}" novalidate>
{chr(10).join(qs)}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my self-assessment result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
  <div class="nc-task"><strong>Reflect.</strong> {m['reflect']}</div>
</section>""")
    parts.append(competency_section(m))
    # practice
    items = "\n".join(f"    <li>{x}</li>" for x in m["practice"]["items"])
    parts.append(f"""<section class="section" id="practice">
  <div class="section-tag">Supervised practice</div>
  <h2>With your preceptor</h2>
  <p>{m['practice']['intro']} These are prompts for supervised learning, not a procedure. Your preceptor observes and signs off each item on the unit&rsquo;s own competency form; the <a href="{COURSE['educator_slug']}.html#checklist">educator page</a> has a printable version.</p>
  <ul class="nc-check">
{items}
  </ul>
</section>""")
    # reading
    rd = []
    for f, why in m["readings"]:
        meta = page_meta(f)
        if not meta:
            err(f"module {mid}: assigned reading not found: guides/{f}")
            continue
        rd.append(f'    <li><a href="{f}">{D.READING_TITLES.get(f) or html.escape(meta[0], quote=False)}</a><span>{why}</span></li>')
    for label, url in m.get("external", []):
        rd.append(f'    <li><a href="{url}" target="_blank" rel="noopener">{label}</a><span>Primary source (external site).</span></li>')
    calc = []
    for f in m.get("calcs", []):
        meta = page_meta(f)
        if not meta:
            err(f"module {mid}: calculator not found: guides/{f}")
            continue
        if f not in D.CALCS:
            err(f"module {mid}: calculator {f} has no display title in display.py")
            continue
        ctitle, d = D.CALCS[f]
        calc.append(f"""  <a href="{f}" class="calc-card">
    <div class="calc-card-icon">⌬</div>
    <div class="calc-card-body">
      <div class="calc-card-title">{ctitle}</div>
      <div class="calc-card-desc">{d}</div>
    </div>
    <span class="calc-card-arrow">Open →</span>
  </a>""")
    calc_html = ""
    if calc:
        calc_html = ('<div class="calc-cards-wrap">\n  <div class="calc-cards-label">Calculators for this module</div>\n'
                     + "\n".join(calc) + "\n</div>")
    np = []
    if prev_m:
        np.append(f'<a class="nc-np" href="{prev_m["slug"]}.html"><small>← Previous &middot; Module {int(prev_m["id"])}</small>{prev_m["plain"]}</a>')
    else:
        np.append(f'<a class="nc-np" href="{hub}"><small>← Course home</small>{COURSE["title"]}</a>')
    if next_m:
        np.append(f'<a class="nc-np nc-np-next" href="{next_m["slug"]}.html"><small>Next &middot; Module {int(next_m["id"])} →</small>{next_m["plain"]}</a>')
    else:
        np.append(f'<a class="nc-np nc-np-next" href="{hub}"><small>Series complete →</small>Back to the course home</a>')
    parts.append(f"""<section class="section" id="reading">
  <div class="section-tag">Assigned reading</div>
  <h2>Read next on this site</h2>
  <ul class="nc-read">
{chr(10).join(rd)}
  </ul>
{calc_html}
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")

    main = auto_expand("\n\n".join(parts), fname)
    pre = f"""<div class="container">
  <div class="nc-bar">
    <a href="{hub}">{COURSE['title']}</a><span class="nc-sep">›</span><span>{"Advanced module " + str(n) if m["neph"] == "advanced" else f"Module {n}"}</span>
    <span class="nc-spacer"></span>
    {role_chip(m)}
  </div>
  <div class="alert alert-teal">
    <div class="alert-icon">🩺</div>
    <div class="alert-body">
      <h4>{COURSE['label']}</h4>
      <p>{C.SCOPE_NOTE}</p>
    </div>
  </div>
</div>"""
    nav = [("objectives", "Objectives")] + [(s["id"], s["nav"]) for s in m["sections"]] + \
          [("case", "Nursing case"), ("quiz", "Self-assessment")] + ([("competencies", "Competencies")] if m["competencies"] else []) + [("practice", "Supervised practice"), ("reading", "Reading")]
    cards = [(hub, "Course home", COURSE["title"], "Syllabus, both learner paths, and all modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], html.unescape(next_m["sub"]).split(".")[0] + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], html.unescape(prev_m["sub"]).split(".")[0] + "."))
    for f, why in m["readings"][:3]:
        meta = page_meta(f)
        if meta:
            cards.append((f, "Assigned reading", D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{m['title']}: Nephrology Nursing Module {n}"
    page = shell(
        fname, title, m["desc"], m["keywords"],
        (f"Nursing Education &middot; Advanced module {n}" if m["neph"] == "advanced" else f"Nursing Education &middot; Module {n}"), m["title"], m["sub"],
        "Registered nurses entering nephrology or hemodialysis practice &middot; nurse educators and preceptors",
        nav, pre, main, glossary_block(main, m.get("terms", [])), related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": COURSE["title"], "url": f"{SITE}/guides/{COURSE['hub_slug']}"},
                      "learningResourceType": "Self-study module with case and self-assessment",
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": m["slug"] + "-vignette-hero", "alt": m["image"]["alt"]},
    )
    page = place_figures(page, mid)
    (GUIDES / fname).write_text(page, encoding="utf-8")
    return fname, [REFS[k] for k in order]


# ───────────────────────── hub page ─────────────────────────
HUB_REFS = ["doh2012", "psn2024", "ra9173", "anna7", "ckd2024", "hd2015", "va2019", "ispd2022", "txcand2020", "iso23500_3"]


def read_minutes(mid):
    m = MODS[mid]
    words = len(visible_text("".join(s["html"] for s in m["sections"]) + m["case"]["html"] + " ".join(m["objectives"])).split())
    return max(10, round(words / 200) + 10)  # reading + case and the self-assessment


def build_hub():
    fname = COURSE["hub_slug"] + ".html"
    edu = COURSE["educator_slug"] + ".html"
    order = HUB_REFS
    cards = []
    for mid in ORDER:
        m = MODS[mid]
        first = html.unescape(m["sub"])
        emph = []
        if m["neph"] == "advanced":
            emph.append('<span class="nc-chip nc-emph-neph">Advanced</span>')
        elif m["neph"] == "core":
            emph.append('<span class="nc-chip nc-chip-core nc-emph-neph">Emphasized on this path</span>')
        else:
            emph.append('<span class="nc-chip nc-emph-neph">Foundation</span>')
        if m["hd"] == "advanced":
            emph.append('<span class="nc-chip nc-emph-hd">Advanced</span>')
        elif m["hd"] == "core":
            emph.append('<span class="nc-chip nc-chip-core nc-emph-hd">Emphasized on this path</span>')
        else:
            emph.append('<span class="nc-chip nc-emph-hd">Foundation</span>')
        cards.append(f"""    <a class="nc-mod" href="{m['slug']}.html" data-module="{mid}" data-order-neph="{C.PATH_ORDER['neph'].index(mid)}" data-order-hd="{C.PATH_ORDER['hd'].index(mid)}">
      <span class="nc-mod-top"><span class="nc-mod-step">Step {C.PATH_ORDER['neph'].index(mid) + 1}</span><span>Module {int(mid)}</span>{''.join(emph)}</span>
      <span class="nc-mod-title">{m['plain']}</span>
      <span class="nc-mod-desc">{html.escape(first, quote=False)}</span>
      <span class="nc-mod-status" aria-live="off"></span>
    </a>""")
    syl = []
    for mid in ORDER:
        m = MODS[mid]
        syl.append(f"<tr><td>{int(mid)}</td><td><a href=\"{m['slug']}.html\">{m['plain']}</a></td>"
                   f"<td>{m['case']['title']}</td><td>About {read_minutes(mid)} min</td>"
                   f"<td>{'Emphasized' if m['neph']=='core' else 'Foundation'}</td><td>{'Emphasized' if m['hd']=='core' else 'Foundation'}</td></tr>")
    xw = []
    for mid in ORDER:
        m = MODS[mid]
        x = m["crosswalk"]
        xw.append(f"<tr><td>{int(mid)}. {m['short']}</td><td>{x['ph']}</td><td>{x['anna']}</td><td>{x['edtna']}</td><td>{x['nncc']}</td></tr>")

    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>A study series for nurses entering kidney care</h2>
  <p>This series is written for Philippine-licensed registered nurses who are starting work in a nephrology ward, a chronic kidney disease (CKD) clinic, or a hemodialysis (HD) unit, and for the educators and preceptors who train them. It has sixteen core modules, which run from kidney assessment and glomerular disease through acute kidney injury (AKI), hemodialysis, living well on dialysis, peritoneal dialysis (PD), transplantation, palliative care, and patient teaching to quality improvement, and an advanced Module 13 on continuous kidney replacement in the intensive care unit and hemodiafiltration, studied after the capstone. Each one explains the reasoning first and the task second: what the kidney or the machine is doing, what the evidence supports, and what that means for the nurse at the bedside or chairside.</p>
  <p>Every module has the same parts: learning objectives; an original lesson that moves from a plain mental model to physiology, evidence, and practice; a fictional nursing case organized around what to assess, communicate, teach, and escalate; a self-assessment that draws questions at random from a fifteen-question bank, with a rationale for every option; a supervised-practice prompt for use with a preceptor; and assigned reading from this site&rsquo;s guides and calculators. The series is free, needs no account, and sends nothing you answer to any server.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this series is, and is not</h4>
      <p>It is self-study. It is not a certificate of training in renal dialysis nursing under the Department of Health (DOH) licensing rules, it carries no Continuing Professional Development (CPD) units, and a self-assessment score does not attest to clinical competence. Competence is shown in supervised practice and signed off by a clinical preceptor or training provider.{cite('[[doh2012]][[psn2024]]', order)}</p>
    </div>
  </div>
</section>

<section class="section" id="paths">
  <div class="section-tag">Two learner paths</div>
  <h2>Choose the path that matches your work</h2>
  <p>Both paths use the same sixteen core modules and end with the same advanced module. They differ in order and in which modules deserve the most time. Select a path to reorder the module list below.</p>
  <div class="nc-paths" role="group" aria-label="Learner path">
    <button type="button" class="nc-path" data-nc-path="neph" aria-pressed="true" data-note="Nephrology Nursing path: modules in numerical order, with most time on assessment, CKD, acute kidney injury, treatment choices, peritoneal dialysis, and transplantation.">
      <b>Nephrology Nursing</b>
      <span>For ward, clinic, and consult nurses. Emphasizes assessment, CKD and its complications, acute kidney injury, treatment choices, peritoneal dialysis, transplantation, and care over the long term.</span>
    </button>
    <button type="button" class="nc-path" data-nc-path="hd" aria-pressed="false" data-note="Hemodialysis Nursing path: Module 1, then Modules 6 to 9 on prescription, access, water, and the treatment session, followed by the remaining foundations.">
      <b>Hemodialysis Nursing</b>
      <span>For nurses entering a dialysis unit. Starts with the shared foundation, then goes straight to prescription, vascular access, water and equipment safety, monitoring during treatment, and emergency response.</span>
    </button>
  </div>
  <p class="nc-pathnote" id="nc-path-note" role="status" aria-live="polite">Nephrology Nursing path: modules in numerical order, with most time on assessment, CKD, acute kidney injury, treatment choices, peritoneal dialysis, and transplantation.</p>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
  <div class="nc-modgrid" id="nc-modules" data-path="neph">
{chr(10).join(cards)}
  </div>
</section>

<section class="section" id="syllabus">
  <div class="section-tag">Syllabus</div>
  <h2>The modules at a glance</h2>
  <p>Study time is an estimate for reading the lesson, working the case, and completing the self-assessment. It does not include supervised practice.</p>
  <div class="table-wrap"><table>
  <thead><tr><th>No.</th><th>Module</th><th>Nursing case</th><th>Self-study time</th><th>Nephrology path</th><th>Hemodialysis path</th></tr></thead>
  <tbody>
{chr(10).join(syl)}
  </tbody></table></div>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>How self-assessment and sign-off differ</h2>
  <p>The questions at the end of each module are formative. They are case-based, have one best answer, and explain why each of the other options is weaker, because understanding why a tempting answer is wrong is most of the learning. You can retry as often as you like. If you tick the box on a module page, your result is remembered in that browser only, so you can see where you left off; untick it and it is erased.</p>
  <p>Skills are a different matter. Cannulating a fistula, connecting a catheter, testing water, or responding to a collapse cannot be learned or judged from a screen. Each module therefore ends with prompts for supervised practice, and the educator page gathers them into a printable checklist that a preceptor completes on the unit&rsquo;s own equipment and procedures.</p>
</section>

<section class="section" id="sources">
  <div class="section-tag">Curriculum sources</div>
  <h2>What the series is built on</h2>
  <p>The scope follows Philippine practice expectations and internationally recognized nephrology nursing curricula. Philippine sources define what is required locally: the Philippine Nursing Act, the DOH licensing order for dialysis facilities, and the Philippine Society of Nephrology (PSN) 2024 guidelines, which describe a structured nurse training program of three months or more.{cite('[[ra9173]][[doh2012]][[psn2024]]', order)} International curricula were used to check that nothing important was left out: the American Nephrology Nurses Association (ANNA) core curriculum, the post-basic curriculum of the European Dialysis and Transplant Nurses Association/European Renal Care Association (EDTNA/ERCA), and the examination domains of the Nephrology Nursing Certification Commission (NNCC).{cite('[[anna7]]', order)} Clinical statements are supported by current guidelines, chiefly Kidney Disease: Improving Global Outcomes (KDIGO), the Kidney Disease Outcomes Quality Initiative (KDOQI), and the International Society for Peritoneal Dialysis (ISPD), and each module lists its own references.{cite('[[ckd2024]][[hd2015]][[va2019]][[ispd2022]][[txcand2020]][[iso23500_3]]', order)}</p>
  <div class="table-wrap"><table>
  <thead><tr><th>Module</th><th>Philippine source or expectation</th><th>ANNA core curriculum area</th><th>EDTNA/ERCA area</th><th>NNCC domain</th></tr></thead>
  <tbody>
{chr(10).join(xw)}
  </tbody></table></div>
  <p>The international columns map topics, not requirements; United States and European credentials do not apply to Philippine licensure. Mapping to NNCC domains uses domain names only, because the published examination weights were being revised during 2026.</p>
</section>

<section class="section" id="educators">
  <div class="section-tag">For educators and preceptors</div>
  <h2>Using the series in a training program</h2>
  <p>A head nurse or training provider can use these modules as the guided-study component of a supervised program. The <a href="{edu}">educator and preceptor page</a> sets out a proposed twelve-week structure, suggested hours, completion criteria, practical stations, an optional final-examination blueprint, and a printable competency checklist. Those are proposals for a provider to adapt and validate; they are not requirements of any regulator.</p>
  <ul class="nc-read">
    <li><a href="{edu}">Educator and preceptor resource</a><span>Proposed program structure, practical stations, and the printable competency checklist.</span></li>
    <li><a href="dialysis-qapi-vs-cqi.html">Dialysis center quality management</a><span>How staff training and competency fit into the unit&rsquo;s quality program.</span></li>
  </ul>
</section>"""
    main = main.replace('<section class="section" id="syllabus">', progression_section() + '<section class="section" id="syllabus">', 1)
    main = auto_expand(main, fname)
    nav = [("start", "Start here"), ("paths", "Learner paths"), ("progression", "Competency map"), ("syllabus", "Syllabus"), ("assessment", "Assessment"),
           ("sources", "Curriculum sources"), ("educators", "For educators")]
    cards_rel = [(MODS["01"]["slug"] + ".html", "Module 1", MODS["01"]["title"], "Begin with kidney function and focused renal assessment."),
                 (MODS["06"]["slug"] + ".html", "Module 6", MODS["06"]["title"], "The first module of the hemodialysis sequence."),
                 (edu, "Educators", "Educator and Preceptor Resource", "Program structure, stations, and competency checklist."),
                 ("dialysis-water-treatment-systems.html", "Related guide", "Hemodialysis Water Treatment Systems", "Assigned reading for Module 8."),
                 ("code-blue-acls-dialysis-unit.html", "Related guide", "Cardiac Arrest Response in a Dialysis Unit", "Assigned reading for Module 9."),
                 ("dialysis-qapi-vs-cqi.html", "Related guide", "Dialysis Center Quality Management", "Assigned reading for Module 12.")]
    pre = f"""<div class="container">
  <div class="nc-bar"><span class="nc-chip nc-chip-core">{COURSE['label']}</span><span class="nc-chip">16 core modules + 1 advanced</span><span class="nc-chip">Free &middot; no account</span><span class="nc-chip">English</span></div>
</div>"""
    title = "Nephrology Nursing & Hemodialysis: A Self-Study Series for Registered Nurses"
    desc = ("A free 16-module self-study series, with an advanced module, for registered nurses entering nephrology or hemodialysis practice in the Philippines: "
            "kidney assessment, CKD, AKI, treatment choices, hemodialysis prescription, vascular access, water safety, emergencies, "
            "peritoneal dialysis, transplantation, quality improvement, and continuous therapy and hemodiafiltration, each with a nursing case and self-assessment.")
    page = shell(
        fname, title, desc,
        "nephrology nursing course Philippines, hemodialysis nurse training, dialysis nursing self-study, renal nurse education, dialysis nurse competency, nephrology nursing syllabus",
        "Nursing Education &middot; Course home", "Nephrology Nursing &amp; <em>Hemodialysis</em>",
        "A twelve-module study series for registered nurses, from kidney assessment and chronic kidney disease to safe hemodialysis care. Each module includes a nursing case and a self-assessment with answer rationales.",
        "Registered nurses entering nephrology or hemodialysis practice &middot; head nurses, educators, and preceptors",
        nav, pre, main, glossary_block(main, [("Preceptor", "An experienced nurse who supervises and assesses a learner in clinical practice."),
                                              ("Formative assessment", "A check on learning that guides study and does not count toward a grade or credential.")]),
        related_block(cards_rel),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": desc,
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE + "/"},
                      "educationalLevel": "Post-registration nursing", "numberOfCredits": 0,
                      "hasPart": [{"@type": "LearningResource", "name": MODS[i]["title"], "url": f"{SITE}/guides/{MODS[i]['slug']}"} for i in ORDER]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero",
                  "alt": "Senior Filipino nurse educator explains an unconnected dialyzer to two newer nurses inside a bright hemodialysis unit."},
    )
    page = place_figures(page, "hub")
    (GUIDES / fname).write_text(page, encoding="utf-8")
    return fname, [REFS[k] for k in order]


# ───────────────────────── educator page ─────────────────────────
EDU_REFS = ["doh2012", "psn2024", "ra9173", "anna7", "figueiredo2016", "patel2013"]


def build_educator():
    fname = COURSE["educator_slug"] + ".html"
    hub = COURSE["hub_slug"] + ".html"
    order = EDU_REFS
    chk = []
    for mid in ORDER:
        m = MODS[mid]
        items = [f'{c["statement"]} {level_chip(c["level"])}' for c in m["competencies"] if c["level"] in "SDI"] or m["practice"]["items"]
        rows = "\n".join(f'<tr class="nc-sign"><td>{x}</td><td></td><td></td><td></td></tr>' for x in items)
        chk.append(f"""  <h3 style="font-family:Inter,system-ui,sans-serif;font-size:1rem;margin:22px 0 6px;color:var(--text);">Module {int(mid)}: {m['plain']}</h3>
  <div class="table-wrap"><table>
  <thead><tr><th style="width:52%;">Competency and target level</th><th>Simulation or teach-back (date, initials)</th><th>Patient care (date, initials)</th><th>Preceptor comments</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>""")
    main = f"""<section class="section" id="purpose">
  <div class="section-tag">Purpose</div>
  <h2>Two different things: a public series and a provider-led program</h2>
  <p>The public modules are self-study. Any nurse can read them, and they can go live independently once their content has been clinically reviewed. A provider-led training program is a separate undertaking. It needs a named training provider, prerequisites, supervised clinical placement, preceptors, practical assessment, and whatever recognition the provider seeks from regulators. This page offers a starting design for such a program. Everything on it is a proposal for a provider to adapt; nothing here has been accepted by the Department of Health (DOH), the Professional Regulation Commission (PRC), or the Philippine Society of Nephrology (PSN), and no Continuing Professional Development (CPD) units are attached.</p>
  <p>What the Philippine sources do require is narrower. The DOH licensing order requires each hemodialysis (HD) nurse to hold a certificate of training in the nursing care of renal dialysis patients from a competent training provider, together with Basic Life Support (BLS) training, and each shift to have at least one nurse with Advanced Cardiovascular Life Support (ACLS) training.{cite('[[doh2012]]', order)} The PSN 2024 guidelines describe a structured training program of three months or more and list its topics, without fixing a number of hours.{cite('[[psn2024]]', order)} The scope of nursing practice itself is set by the Philippine Nursing Act.{cite('[[ra9173]]', order)}</p>
</section>

<section class="section" id="structure">
  <div class="section-tag">Proposed structure</div>
  <h2>Twelve instructional weeks over at least three months</h2>
  <p>The proposal below totals 480 hours. That figure is a course-design choice informed by an example of a 480-hour competency program listed with the PRC; it is not a regulatory minimum, and a provider should confirm what its own regulators and receiving facilities accept. If the PSN duration is adopted, the twelve instructional weeks are scheduled across at least three calendar months.</p>
  <div class="table-wrap"><table>
  <thead><tr><th>Component</th><th>Proposed hours</th><th>What it contains</th></tr></thead>
  <tbody>
  <tr><td>Guided study</td><td>96</td><td>The core modules with facilitated discussion of each case and self-assessment; assigned reading</td></tr>
  <tr><td>Skills laboratory and simulation</td><td>48</td><td>Machine setup on unconnected equipment, access examination and cannulation on models, catheter connection, water testing, emergency scenarios</td></tr>
  <tr><td>Supervised clinical learning</td><td>336</td><td>Direct patient care with a preceptor; observed care and simulation are documented separately</td></tr>
  <tr><td><strong>Total</strong></td><td><strong>480</strong></td><td></td></tr>
  </tbody></table></div>
  <p><strong>Clinical emphasis by path.</strong> For the Hemodialysis Nursing path: complete treatment encounters from pre-assessment to discharge, observation of the water system with the technician, and inpatient HD where available. For the Nephrology Nursing path: a renal ward or CKD clinic, HD exposure, and observational exposure to peritoneal dialysis (PD) and transplantation where a program exists. The provider sets the number of encounters and validates each competency on its own equipment and procedures.</p>
</section>

<section class="section" id="completion">
  <div class="section-tag">Proposed completion criteria</div>
  <h2>What finishing the program could require</h2>
  <ul>
    <li>A score of at least 80% on a separate written examination set by the provider. The public self-assessments are formative and are not that examination.</li>
    <li>A passing case presentation or quality audit (the capstone in Module 12).</li>
    <li>Every safety-critical practical step demonstrated without prompting.</li>
    <li>Preceptor sign-off of the competency checklist, with simulation and observed patient care recorded separately.</li>
    <li>Current BLS for all, and ACLS as the facility&rsquo;s staffing plan requires.</li>
  </ul>
</section>

<section class="section" id="blueprint">
  <div class="section-tag">Optional examination blueprint</div>
  <h2>A 60-item final, weighted by path</h2>
  <p>If a provider writes a final examination, these weights reflect the emphasis of each path. They are course weights proposed for this series. They are not the weights of any certification examination and should be mapped separately if a learner is also preparing for one.</p>
  <div class="table-wrap"><table>
  <thead><tr><th>Hemodialysis Nursing path</th><th>Items</th><th>Nephrology Nursing path</th><th>Items</th></tr></thead>
  <tbody>
  <tr><td>Chronic HD (Modules 6, 7, 9)</td><td>30</td><td>CKD and its complications (Modules 1 to 3)</td><td>20</td></tr>
  <tr><td>Adult kidney disease (Modules 1 to 3, 5)</td><td>15</td><td>Acute kidney injury (Module 4)</td><td>10</td></tr>
  <tr><td>Acute kidney injury and acute HD (Module 4)</td><td>9</td><td>HD (Modules 6 to 9)</td><td>12</td></tr>
  <tr><td>Water and dialysate (Module 8)</td><td>6</td><td>PD and transplantation (Modules 10, 11)</td><td>10</td></tr>
  <tr><td></td><td></td><td>Conservative care, special populations, professional practice (Modules 5, 11, 12)</td><td>8</td></tr>
  <tr><td><strong>Total</strong></td><td><strong>60</strong></td><td><strong>Total</strong></td><td><strong>60</strong></td></tr>
  </tbody></table></div>
</section>

<section class="section" id="stations">
  <div class="section-tag">Practical stations and capstone</div>
  <h2>Observed stations</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Hemodialysis Nursing path</th><th>Nephrology Nursing path</th></tr></thead>
  <tbody>
  <tr><td>1. Prescription verification and machine checks</td><td>1. CKD assessment and care plan</td></tr>
  <tr><td>2. Access examination and aseptic connection</td><td>2. Acute kidney injury recognition and escalation</td></tr>
  <tr><td>3. Emergency during treatment</td><td>3. Treatment-options counseling with teach-back</td></tr>
  <tr><td>4. Water-safety failure with handoff</td><td>4. PD or transplant scenario</td></tr>
  </tbody></table></div>
  <p><strong>Capstone.</strong> A fictional or fully de-identified renal case, or a small quality audit with a measurable follow-up outcome, presented to the preceptor and unit team. Audits of observed practice with feedback were part of the prevention bundle associated with fewer access-related bloodstream infections in a multicenter collaborative, and structured training with reassessment is recommended for PD teaching.{cite('[[patel2013]][[figueiredo2016]]', order)}</p>
</section>

{psn_sections()}<section class="section nc-print-break" id="checklist">
  <div class="section-tag">Printable</div>
  <h2>Preceptor competency checklist</h2>
  <p>Print this section (use the print button). The rows are each module&rsquo;s competencies at the <em>shows how</em> level and above, with the target level beside each. A <em>does, independent</em> item is signed only after the supervised level has been observed and the unit&rsquo;s policy allows it. The statements describe what to observe; the steps themselves come from the unit&rsquo;s approved procedures and the manufacturer&rsquo;s instructions. Record simulation and patient care separately. Transfer the result to the facility&rsquo;s own competency form if one exists.</p>
  <div class="table-wrap"><table>
  <tbody>
  <tr class="nc-sign"><td style="width:25%;"><strong>Learner</strong></td><td></td><td style="width:20%;"><strong>PRC license no.</strong></td><td></td></tr>
  <tr class="nc-sign"><td><strong>Preceptor</strong></td><td></td><td><strong>Unit</strong></td><td></td></tr>
  <tr class="nc-sign"><td><strong>Path</strong></td><td><span class="nc-box"></span> Hemodialysis Nursing &nbsp; <span class="nc-box"></span> Nephrology Nursing</td><td><strong>Start and end dates</strong></td><td></td></tr>
  </tbody></table></div>
{chr(10).join(chk)}
  <h3 style="font-family:Inter,system-ui,sans-serif;font-size:1rem;margin:22px 0 6px;color:var(--text);">Final sign-off</h3>
  <div class="table-wrap"><table>
  <tbody>
  <tr class="nc-sign"><td style="width:40%;">Written examination score (provider-set)</td><td></td></tr>
  <tr class="nc-sign"><td>Capstone presented (title, date)</td><td></td></tr>
  <tr class="nc-sign"><td>Life-support training current (BLS, ACLS; expiry)</td><td></td></tr>
  <tr class="nc-sign"><td>Preceptor name, signature, date</td><td></td></tr>
  <tr class="nc-sign"><td>Head nurse or medical director, signature, date</td><td></td></tr>
  </tbody></table></div>
</section>

<section class="section" id="review">
  <div class="section-tag">Before public or provider use</div>
  <h2>Clinical review and open dependencies</h2>
  <p>High-risk content should be read by the appropriate reviewer before a provider relies on it: emergency sequences and vascular access by a senior HD nurse and nephrologist; water limits and machine checks by the unit&rsquo;s technician or biomedical engineer; isolation policy by infection control; medicines by a pharmacist; and pediatric, pregnancy, and transplant content by the relevant specialist nurse or physician. International curricula, including the American Nephrology Nurses Association (ANNA) core curriculum, were used to check coverage only.{cite('[[anna7]]', order)} Regulatory statements should be rechecked against the latest DOH issuances before each intake.</p>
  <ul class="nc-read">
    <li><a href="{hub}">Course home</a><span>Syllabus, learner paths, and all modules.</span></li>
  </ul>
</section>"""
    main = auto_expand(main, fname)
    nav = [("purpose", "Purpose"), ("structure", "Structure"), ("completion", "Completion"), ("blueprint", "Exam blueprint"),
           ("stations", "Stations")] + ([("psn", "PSN alignment"), ("osce", "OSCE bank")] if (CONTENT / "educator_psn.py").exists() else []) + [("checklist", "Checklist"), ("review", "Review")]
    pre = f"""<div class="container">
  <div class="nc-bar"><a href="{hub}">{COURSE['title']}</a><span class="nc-sep">›</span><span>Educator and preceptor resource</span></div>
</div>"""
    title = "Nephrology Nursing & Hemodialysis: Educator and Preceptor Resource"
    desc = ("Educator syllabus for the Nephrology Nursing & Hemodialysis series: a proposed 12-week, 480-hour provider-led program, "
            "completion criteria, practical stations, a 60-item examination blueprint, and a printable preceptor competency checklist.")
    page = shell(
        fname, title, desc,
        "dialysis nurse training program Philippines, hemodialysis nurse competency checklist, nephrology nursing preceptor, renal nurse training syllabus, 480 hours dialysis training",
        "Nursing Education &middot; For educators", "Educator and <em>Preceptor</em> Resource",
        "A proposed structure for a provider-led program built on the public modules, with practical stations and a printable competency checklist. Proposals to adapt, not regulatory requirements.",
        "Head nurses &middot; nurse educators &middot; clinical preceptors &middot; training providers &middot; medical directors",
        nav, pre, main, glossary_block(main, [("Preceptor", "An experienced nurse who supervises and assesses a learner in clinical practice."),
                                              ("Competency", "An observable ability to perform a task safely to a defined standard.")]),
        related_block([(hub, "Course home", COURSE["title"], "Syllabus, both learner paths, and all modules."),
                       ("dialysis-qapi-vs-cqi.html", "Related guide", "Dialysis Center Quality Management", "Staff training and competency within the quality program."),
                       ("nephrology-workforce-crisis-or-opportunity.html", "Related guide", "Workforce Issues in Nephrology", "Context on the kidney-care workforce.")]),
        body_class="nc-educator",
    )
    page = place_figures(page, "educator")
    (GUIDES / fname).write_text(page, encoding="utf-8")
    return fname, [REFS[k] for k in order]


# ───────────────────────── docs ─────────────────────────
def write_docs(all_refs):
    DOCS.mkdir(parents=True, exist_ok=True)
    # quiz key register
    lines = ["# Quiz key register", "",
             f"Generated by generate_nursing_course.py. Review date {COURSE['review_date']}. One row per scored item: "
             "the teaching objective, the keyed answer, the supporting sources, and any dependency on policy, orders, "
             "manufacturer instructions, or a standard edition.", ""]
    for mid in ORDER:
        m = MODS[mid]
        lines += [f"## Module {int(mid)}: {m['title']}", "", "| Q | Objective tested | Keyed answer | Sources | Dependency flag |", "|---|---|---|---|---|"]
        for qi, q in enumerate(m["quiz"], 1):
            key = next(html.unescape(re.sub(r"<[^>]+>", "", o[0])) for o in q["options"] if o[1])
            lines.append(f"| {qi} | {html.unescape(q['objective'])} | {key} | {', '.join(q['sources'])} | {html.unescape(q['flag']) or '—'} |")
        lines += ["", "Module review flags:"] + [f"- {html.unescape(f)}" for f in m["flags"]] + [""]
    (DOCS / "QUIZ-KEY-REGISTER.md").write_text("\n".join(lines), encoding="utf-8")
    # crosswalk
    lines = ["# Curriculum crosswalk", "",
             "Each module mapped to Philippine program or practice sources, ANNA core curriculum areas, EDTNA/ERCA "
             "post-basic curriculum areas, and NNCC examination domains. International columns map topics only.", "",
             "| Module | Philippine source or expectation | ANNA | EDTNA/ERCA | NNCC | Nephrology path | HD path |", "|---|---|---|---|---|---|---|"]
    for mid in ORDER:
        m = MODS[mid]; x = m["crosswalk"]
        lines.append(f"| {int(mid)}. {m['title']} | {x['ph']} | {x['anna']} | {x['edtna']} | {x['nncc']} | {m['neph']} | {m['hd']} |")
    (DOCS / "CURRICULUM-CROSSWALK.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    usage = {}
    for fname, cites in all_refs.items():
        for c in cites:
            for k, v in REFS.items():
                if v == c:
                    usage.setdefault(k, []).append(fname)
    (DATA / "refs-used.json").write_text(json.dumps(usage, indent=1), encoding="utf-8")
    (DATA / "refs-overrides.json").write_text(json.dumps(all_refs, indent=1, ensure_ascii=False), encoding="utf-8")
    manifest = []
    for mid in ORDER:
        m = MODS[mid]; im = m["image"]
        final = f"{m['slug']}-vignette-hero"
        manifest.append({
            "module": mid, "work_id": im["file"], "module_title": m["title"], "page": f"guides/{m['slug']}.html",
            "placement": "hero circular vignette (figure.hero-figure > .hero-vignette), right of the title on desktop",
            "final_filename": f"{final}.png",
            "master": f"images/{final}.png", "master_spec": "2048x2048 PNG, sRGB; circle 85-90% of canvas with white margin; no text",
            "derivatives": [f"images/{final}.webp (same pixels, WebP)",
                            f"images/resp/{final}-800.webp (made by patch_responsive_images.py)",
                            f"images/og/{m['slug']}-og.jpg (1200x630 share card, made by patch_og_images.py)",
                            f"images/{m['slug']}-rg-thumb.webp (220x160 related-card thumb, generate_rg_thumbs.py)"],
            "alt": html.unescape(im["alt"]), "archetype": im["archetype"], "reviewer": im["reviewer"],
            "status": "present" if (ROOT / "images" / f"{final}.png").exists() else "pending production",
        })
    (DOCS / "image-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")


PIPELINE = [
    "patch_master_css.py", "patch_font_link.py", "patch_hero_fetchpriority.py", "patch_hero_fullwidth.py",
    "patch_hero_maxwidth.py", "patch_image_lightbox.py", "patch_symptom_widget.py", "patch_share_buttons.py",
    "patch_guide_rail.py", "patch_mode_cls.py", "patch_signature_position.py", "patch_last_reviewed.py",
    "patch_published_time.py", "patch_reading_time.py", "REFS", "patch_hero_meta.py", "patch_share_title.py",
    "patch_canonical_clean_urls.py", "patch_responsive_images.py", "patch_og_images.py",
]


def pipeline_python():
    """Some house patchers use 3.10+ syntax; macOS ships 3.9 as python3."""
    import shutil
    if sys.version_info >= (3, 10):
        return sys.executable
    for name in ("python3.13", "python3.12", "python3.11", "python3.10"):
        found = shutil.which(name) or (f"/opt/homebrew/bin/{name}" if Path(f"/opt/homebrew/bin/{name}").exists() else None)
        if found:
            return found
    return sys.executable


def run_pipeline(files):
    PY = pipeline_python()
    for f in files:
        for step in PIPELINE:
            if step == "REFS":
                cmd = [PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", f]
            else:
                cmd = [PY, step, "--guide", f]
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  ! {step} failed on {f}: {(r.stderr or r.stdout).strip()[-400:]}")
        print(f"  patched {f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--patch", action="store_true", help="run the per-guide patch pipeline after writing")
    ap.add_argument("--check", action="store_true", help="validate only; write nothing")
    ap.add_argument("--reset-published", action="store_true",
                    help="drop the carried-over publish stamps so patch_published_time.py stamps the real go-live moment")
    args = ap.parse_args()
    global RESET_PUBLISHED
    RESET_PUBLISHED = args.reset_published
    all_refs = {}
    if args.check:
        for mid in ORDER:
            number_refs(MODS[mid])
            for f, _ in MODS[mid]["readings"]:
                if not (GUIDES / f).exists():
                    err(f"module {mid}: missing reading {f}")
            for f in MODS[mid].get("calcs", []):
                if not (GUIDES / f).exists():
                    err(f"module {mid}: missing calculator {f}")
    else:
        for mid in ORDER:
            f, cites = build_module(mid)
            all_refs[f] = cites
        f, cites = build_hub(); all_refs[f] = cites
        f, cites = build_educator(); all_refs[f] = cites
        write_docs(all_refs)
        print(f"wrote {len(all_refs)} pages to guides/ and docs to {DOCS.relative_to(ROOT)}/")
    if ERRORS:
        print("\nCONTENT ERRORS:")
        for e in ERRORS:
            print("  -", e)
        sys.exit(1)
    if args.patch:
        run_pipeline(sorted(all_refs))
    if not args.check:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout or r.stderr).strip())
        # keep the Transplant Nurse subtrack entry links (Module 11 section, specialty card on the hub)
        if (ROOT / "generate_transplant_nurse.py").exists():
            r = subprocess.run([sys.executable, "-c", "import generate_transplant_nurse as T; print('transplant-nurse entry links:', T.wire_parent())"], cwd=ROOT, capture_output=True, text=True)
            print((r.stdout or r.stderr).strip()[-300:])


if __name__ == "__main__":
    main()
