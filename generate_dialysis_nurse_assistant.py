#!/usr/bin/env python3
"""Renal Care Academy · Nephrology Nursing Track · By Role · Dialysis Nurse Assistant / Patient Care Assistant (PCA).

Pages: hub (dialysis-nurse-assistant), 12 modules (dialysis-nurse-assistant-NN-<slug>), the end-of-course knowledge check
(dialysis-nurse-assistant-final-exam), and the Patient Care Assistant Toolkit (guides/calc-dialysis-nurse-assistant-toolkit.html).
Content lives in tools/dialysis_nurse_assistant/content/*.py (hand-edited), built from Blueprint v2
(/Volumes/Storage/Renal Care Academy/Dialysis Nurse Assistant/BLUEPRINT-v2.md). Patterned on generate_dialysis_support_staff.py.

    python3 generate_dialysis_nurse_assistant.py              # write pages to guides/, then publish to academy/
    python3 generate_dialysis_nurse_assistant.py --patch      # also run the /setup-guide patch pipeline on each page
    python3 generate_dialysis_nurse_assistant.py --check      # validate content only (refs, quiz keys, links)
    python3 generate_dialysis_nurse_assistant.py --calc       # (re)build the Patient Care Assistant Toolkit and run its pipeline

Never hand-edit academy/dialysis-nurse-assistant*.html: edit the content files and re-run.
"""
import argparse, html, importlib.util, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_nursing_course as N  # noqa: E402  (chrome, course CSS, helpers)
sys.path.insert(0, str(Path(__file__).resolve().parent / "tools" / "academy"))
from tile_img import tile  # noqa: E402  (module-tile thumbnails)

GUIDES = ROOT / "guides"
ACADEMY = ROOT / "academy"
CONTENT = ROOT / "tools" / "dialysis_nurse_assistant" / "content"
DATA = ROOT / "data" / "dialysis-nurse-assistant"
SITE = "https://renalcarematters.com"
ERRORS = []
BANK_SIZE = 10


def err(m):
    ERRORS.append(m)


def load(name):
    spec = importlib.util.spec_from_file_location(f"dna_{name}", CONTENT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C = load("course")
IMG = load("images")
COURSE = C.COURSE
DRAW, MOD_PASS = COURSE["module_draw"], COURSE["module_pass"]
HUB = COURSE["hub_slug"] + ".html"
EXAM = COURSE["hub_slug"] + "-final-exam.html"
PARENT = COURSE["parent_slug"] + ".html"
ENTRY = COURSE["entry_slug"] + ".html"
CALC = "calc-dialysis-nurse-assistant-toolkit.html"
N.ABBR.update(C.ABBR)   # the nursing glossary/auto-expansion helpers read this dict

MODS, ORDER = {}, []
for mid, slug, title, short, week, (s_h, sim_h, w_h), comps, pathway in C.MODULES:
    m = load(f"m{mid}").MODULE
    m.update(id=mid, slug=f"{COURSE['hub_slug']}-{mid}-{slug}", title=title, short=short, week=week, hours=s_h + sim_h + w_h,
             study=s_h, sim=sim_h, work=w_h, comps=comps, pathway=pathway)
    MODS[mid] = m
    ORDER.append(mid)


# ───────────────────────── references ─────────────────────────
def build_refs():
    raw = {}
    for p in (ROOT / "data" / "nursing-course" / "refs_pubmed_raw.json", ROOT / "data" / "dialysis-unit-support-staff" / "refs_pubmed_raw.json",
              DATA / "refs_pubmed_raw.json"):
        if p.exists():
            raw.update(json.loads(p.read_text(encoding="utf-8")))
    refs = dict(C.MANUAL_REFS)
    for key, pmid in C.PUBMED_REFS.items():
        r = raw.get(pmid)
        if not r:
            err(f"reference {key}: PMID {pmid} missing from refs_pubmed_raw.json")
            continue
        authors = N._apa_authors(r["authors"])
        if not authors.endswith("."):
            authors += "."
        title = C.TITLE_OVERRIDES.get(pmid, r["title"]).rstrip(".")
        journal = C.JOURNALS.get(r["journal"]) or N.C.JOURNALS.get(r["journal"])
        if not journal:
            err(f"reference {key}: no full journal name for '{r['journal']}'")
            journal = r["journal"]
        vol = f"<em>{r['volume']}</em>" if r["volume"] else ""
        iss = f"({N._issue(r['issue'])})" if r["issue"] else ""
        pages = N._pages(r["pages"])
        doi = r.get("doi", "")
        link = (f' <a href="https://doi.org/{doi}">https://doi.org/{doi}</a>' if doi
                else f' <a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/">https://pubmed.ncbi.nlm.nih.gov/{pmid}/</a>')
        tail = ", ".join(x for x in [f"{vol}{iss}", pages] if x)
        end = "" if title[-1:] in "?!" else "."
        t = title if "&" in title else html.escape(title, quote=False)
        refs[key] = f"{authors} ({r['year']}). {t}{end} <em>{journal}</em>, {tail}.{link}"
    return refs


REFS = build_refs()


class Cites:
    """Numbered citations for one page, in order of first use."""

    def __init__(self, label):
        self.label, self.order = label, []

    def scan(self, text):
        for k in re.findall(r"\[\[([a-z0-9_]+)\]\]", text):
            if k not in REFS:
                err(f"{self.label}: unknown reference key [[{k}]]")
            elif k not in self.order:
                self.order.append(k)

    def add(self, keys):
        for k in keys:
            if k not in REFS:
                err(f"{self.label}: unknown reference key {k}")
            elif k not in self.order:
                self.order.append(k)

    def render(self, text):
        self.scan(text)

        def sub(m):
            k = m.group(1)
            if k not in self.order:
                return ""
            n = self.order.index(k) + 1
            return f'<sup class="nc-cite"><a href="#ref-{n}" data-ref="{n}" aria-label="Reference {n}">{n}</a></sup>'
        return N.merge_cites(re.sub(r"\[\[([a-z0-9_]+)\]\]", sub, text))

    def list(self):
        return [REFS[k] for k in self.order]


# ───────────────────────── extra CSS (second style block survives patch_master_css.py) ─────────────────────────
TN_CSS = """
/* Dialysis Nurse Assistant / PCA subtrack: visual components (design tokens only, so dark mode holds). */
.tc-flow{display:flex;flex-wrap:wrap;gap:8px;align-items:stretch;list-style:none;margin:14px 0;padding:0;counter-reset:tc;}
.tc-flow li{flex:1 1 150px;border:1px solid var(--border);border-top:4px solid var(--teal);border-radius:10px;background:var(--white);padding:10px 12px;font-size:14px;line-height:1.5;color:var(--text-mid);counter-increment:tc;}
.tc-flow li b{display:block;color:var(--text);font-size:14.5px;margin-bottom:2px;}
.tc-flow li b::before{content:counter(tc) ". ";color:var(--teal);}
.tc-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:14px 0;}
.tc-card{border:1px solid var(--border);border-left:4px solid var(--teal);border-radius:10px;background:var(--white);padding:10px 14px;font-size:14px;line-height:1.55;color:var(--text-mid);}
.tc-card b{display:block;color:var(--text);margin-bottom:2px;}
.tc-plain{border-left:4px solid var(--teal);background:var(--teal-light);border-radius:0 12px 12px 0;padding:12px 16px;margin:14px 0;font-size:15.5px;line-height:1.65;color:var(--text);}
html[data-theme="dark"] .tc-plain{background:#0a2830;}
.tc-lab{display:block;font:700 .72rem Inter,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:3px;}
html[data-theme="dark"] .tc-lab{color:#7fd6dd;}
.tc-scene{border:1px solid var(--border);border-left:5px solid var(--amber);border-radius:0 12px 12px 0;background:var(--amber-soft);padding:12px 16px 10px;margin:16px 0;}
.tc-scene .tc-lab{color:#7a4f00;}
.section .tc-scene p{margin:0 0 8px;font-size:15px;line-height:1.65;color:var(--text);text-align:left;hyphens:manual;}
html[data-theme="dark"] .tc-scene{background:#2a2216;border-color:#4a3c22;border-left-color:#d9a441;}
html[data-theme="dark"] .tc-scene .tc-lab{color:#f2c46b;}
@media print{.tc-scene{break-inside:avoid;background:#fff;}}
.tc-keyp{border:1px solid var(--green);border-radius:12px;background:var(--green-soft);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
html[data-theme="dark"] .tc-keyp{background:#1a2535;}
.tc-stop{border:1px solid var(--red);border-left-width:5px;border-radius:12px;background:var(--white);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
.tc-stop .tc-lab{color:var(--red);}
html[data-theme="dark"] .tc-stop .tc-lab{color:#ff9b9b;}
.tc-formula{border:1px dashed var(--border);border-radius:12px;background:var(--bg);padding:12px 16px;margin:12px 0;font-size:15px;line-height:1.6;color:var(--text);}
.tc-sits{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0;}
.tc-sit{border:1px solid var(--border);border-top:4px solid var(--amber);border-radius:12px;background:var(--white);padding:12px 16px 10px;}
.tc-sit h3{margin:0 0 6px;font-family:Inter,system-ui,sans-serif;font-size:1rem;line-height:1.35;color:var(--text);}
.tc-sit dl{margin:0;}
.tc-sit dt{font:700 .7rem Inter,system-ui,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:var(--text-muted);margin-top:8px;}
.tc-sit dt.tc-sit-do{color:var(--teal);}
html[data-theme="dark"] .tc-sit dt.tc-sit-do{color:#7fd6dd;}
.tc-sit dd{margin:2px 0 0;font-size:14.5px;line-height:1.6;color:var(--text-mid);}
.tn-round{border:1px solid var(--border);border-left:5px solid var(--purple,#4B3280);border-radius:12px;background:var(--white);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
.tn-crit{border:1px solid var(--red);border-radius:12px;padding:10px 14px;margin:10px 0;font-size:14.5px;line-height:1.6;color:var(--text);background:var(--white);}
.tn-crit strong{color:var(--red);}
html[data-theme="dark"] .tn-crit strong{color:#ff9b9b;}
.table-wrap caption{caption-side:top;text-align:left;font:600 .85rem Inter,system-ui,sans-serif;color:var(--text-muted);padding:0 0 6px;}
.dna-crit-tag{display:inline-block;margin-left:6px;padding:0 7px;border-radius:999px;font:700 10.5px Inter,system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--red);border:1px solid var(--red);vertical-align:middle;}
html[data-theme="dark"] .dna-crit-tag{color:#ff9b9b;border-color:#ff9b9b;}
.dna-record{border:1px solid var(--border);border-radius:12px;padding:12px 16px;margin:12px 0;background:var(--white);}
.dna-record td{height:28px;}
.nc-result-pass{border-color:var(--green) !important;}
.nc-result-fail{border-color:var(--amber) !important;}
.nc-verdict-line{display:block;margin-top:6px;font-weight:700;}
@media (max-width:720px){.tc-sits{grid-template-columns:1fr;}}
@media print{.tc-sit,.tc-card,.tc-flow li,.dna-record{break-inside:avoid;}.nc-quiz{display:none;}}
"""

DISCLAIMER = ("Educational self-study for supervised Dialysis Nurse Assistants / Patient Care Assistants. Does not replace your "
              "employer&rsquo;s written job description and competency record, the RN&rsquo;s delegation, unit procedures and device "
              "instructions, a practical basic life support course, DOH and PSN requirements, or supervised practice and sign-off.")


import audit_acronym_expansion as AUD  # noqa: E402  (the site's first-use audit, so pages are generated compliant)

_SKIP_OPEN = re.compile(r"<(h[1-4]|button|summary|svg)\b", re.I)
_SKIP_CLOSE = re.compile(r"</(h[1-4]|button|summary|svg)>", re.I)


def tn_expand(body_html, page):
    """Expand each acronym at its first use in prose, judged exactly as audit_acronym_expansion.py judges it."""
    def text_of(h):
        h = re.sub(r'<dl class="fig-abbrevs".*?</dl>', " ", h, flags=re.S)
        return AUD.to_text(re.sub(r"<h[1-4]\b.*?</h[1-4]>", " ", h, flags=re.S))
    held = re.findall(r'<dl class="fig-abbrevs".*?</dl>', body_html, flags=re.S)
    for i, blk in enumerate(held):
        body_html = body_html.replace(blk, f"<!--FIGABBR{i}-->", 1)
    acros = (AUD.GLOBAL_ACRONYMS | set(N.ABBR)) - AUD.EXEMPT
    for a in sorted(acros, key=lambda x: (-len(x), x)):
        r = AUD.first_use_expanded(text_of(body_html), a)
        if r is None or r:
            continue
        exp = N.ABBR.get(a, (None,))[0]
        if not exp:
            err(f"{page}: no expansion known for {a}; expand it in the content")
            continue
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(s?)(?![A-Za-z0-9])")
        parts = re.split(r"(<[^>]+>)", body_html)
        depth, done = 0, False
        for i, seg in enumerate(parts):
            if seg.startswith("<"):
                if _SKIP_OPEN.match(seg):
                    depth += 1
                elif _SKIP_CLOSE.match(seg):
                    depth = max(0, depth - 1)
                continue
            if depth or done:
                continue
            m = pat.search(seg)
            if m:
                plural = m.group(1)
                parts[i] = seg[:m.start()] + f"{exp}{plural} ({a}{plural})" + seg[m.end():]
                done = True
        body_html = "".join(parts)
    for i, blk in enumerate(held):
        body_html = body_html.replace(f"<!--FIGABBR{i}-->", blk, 1)
    return body_html


def finish(page):
    """Second style block, and the course-isolated progress key read by assets/nursing-course.js."""
    page = page.replace('<style id="nursing-course-style">', f'<style id="tn-course-style">{TN_CSS}</style>\n<style id="nursing-course-style">', 1)
    team = f"{SITE}/images/og/nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero.jpg"
    if team in page or "nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero.png" in page:
        card = ROOT / "images" / "og" / "academy" / f"{COURSE['hub_slug']}.jpg"
        fb = f"{SITE}/images/og/academy/{card.name}" if card.exists() else f"{SITE}/images/og/academy/academy-index.jpg"
        page = re.sub(r"https://renalcarematters\.com/images/(?:og/)?nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero\.(?:jpg|png)", fb, page)
    page = re.sub(r"<html([^>]*)>", lambda m: m.group(0) if "data-nc-store" in m.group(1) else f'<html{m.group(1)} data-nc-store="{COURSE["store_key"]}">', page, count=1)
    return page


def bar(label):
    return f"""<div class="container">
  <div class="nc-bar">
    <a href="renal-care-academy.html">Renal Care Academy</a><span class="nc-sep">›</span><a class="nc-group" href="renal-care-academy.html#track-nursing">Nephrology Nursing Track</a><span class="nc-sep">›</span><a class="nc-group" href="renal-care-academy.html#nursing-role">By Role</a><span class="nc-sep">›</span><a href="{HUB}">{COURSE['title']}</a><span class="nc-sep">›</span><span>{label}</span>
  </div>
  <div class="alert alert-teal">
    <div class="alert-icon">🩺</div>
    <div class="alert-body">
      <h4>{COURSE['label']}</h4>
      <p>{C.SCOPE_NOTE}</p>
    </div>
  </div>
</div>"""


def quiz_fieldsets(items, label, group=None):
    out = []
    stems = set()
    for qi, q in enumerate(items, 1):
        n_correct = sum(1 for o in q["options"] if o[1])
        if n_correct != 1:
            err(f"{label} question {qi}: {n_correct} options keyed correct (must be exactly 1)")
        if len(q["options"]) != 4:
            err(f"{label} question {qi}: expected 4 options")
        rats = [o[2] for o in q["options"]]
        if len(set(rats)) != len(rats):
            err(f"{label} question {qi}: rationales must differ per option")
        if q["stem"] in stems:
            err(f"{label} question {qi}: duplicate stem")
        stems.add(q["stem"])
        opts = []
        for oi, (text, correct, rat) in enumerate(q["options"]):
            oid = f"q{qi}{'abcd'[oi]}"
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if correct else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{text}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span><div class="nc-rat" hidden>{rat}</div></div>
    </div>""")
        g = q.get("group", group)
        g = f' data-group="{g}"' if g else ""
        crit = ' data-critical="1"' if q.get("critical") else ""
        tag = '<span class="dna-crit-tag">Safety-critical</span>' if q.get("critical") else ""
        out.append(f"""  <fieldset class="nc-q" data-q="{qi}"{g}{crit}>
    <legend><span class="nc-qn">Question {qi} of {len(items)}</span>{q['stem']}{tag}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    return "\n".join(out)


CALC_COPY = {
    CALC: ("Patient Care Assistant Toolkit", "Net weight with wheelchair tare and weight gain, standing blood pressure check, timed counts and temperature."),
    "calc-dialysis-support-staff-toolkit.html": ("Dialysis Support Staff Toolkit", "Label dilution and wet contact time, station turnover budget, safe lift check and audit tally."),
    "calc-qapi-run-chart-spc.html": ("Run Chart", "Plot an audit result over time and see whether a change is real."),
}


def calc_cards(files, label):
    cards = []
    for f in files:
        if f != CALC and not N.page_meta(f):
            err(f"{label}: calculator not found: guides/{f}")
            continue
        if f not in CALC_COPY:
            err(f"{label}: add display copy for {f} to CALC_COPY")
            continue
        title, desc = CALC_COPY[f]
        cards.append(f"""  <a href="{f}" class="calc-card">
    <div class="calc-card-icon">⌬</div>
    <div class="calc-card-body">
      <div class="calc-card-title">{title}</div>
      <div class="calc-card-desc">{desc}</div>
    </div>
    <span class="calc-card-arrow">Open →</span>
  </a>""")
    if not cards:
        return ""
    return '<div class="calc-cards-wrap">\n  <div class="calc-cards-label">Calculators for this module</div>\n' + "\n".join(cards) + "\n</div>"


def quiz_form(module_key, items, label, draw, extra_attrs=""):
    return f"""  <form class="nc-quiz" id="nc-quiz" data-module="{module_key}" data-draw="{draw}"{extra_attrs} novalidate>
{quiz_fieldsets(items, label)}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my result on this device (optional). Stored only in this browser, separately from other Academy courses; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>"""


def figure_html(mid, section):
    """In-body teaching figures from content/images.py, placed only when the image file exists."""
    out = []
    for f in IMG.FIGURES:
        if f["mid"] != mid or f["section"] != section:
            continue
        png, webp = ROOT / "images" / f"{f['stem']}.png", ROOT / "images" / f"{f['stem']}.webp"
        if not (png.exists() or webp.exists()):
            continue
        try:
            from PIL import Image
            with Image.open(png if png.exists() else webp) as im:
                w, h = im.size
        except Exception:
            w, h = (1792, 1024)
        src = f'<source srcset="../images/{webp.name}" type="image/webp">' if webp.exists() else ""
        img = png.name if png.exists() else webp.name
        shape = "nc-fig-tall" if h > w * 1.2 else ("nc-fig-card" if h > w * 0.66 else "nc-fig-wide")
        ab = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in f["abbrevs"])
        ab = f'<dl class="fig-abbrevs">{ab}</dl>' if ab else ""
        out.append(f'<figure class="nc-fig {shape}" id="fig-{f["id"].lower()}"><picture>{src}'
                   f'<img class="nc-fig-img" src="../images/{img}" alt="{html.escape(html.unescape(f["alt"]))}" width="{w}" height="{h}" loading="lazy" decoding="async"></picture>'
                   f'<figcaption><p class="fig-desc">{f["desc"]}</p>{ab}</figcaption></figure>')
    return "\n".join(out)


def check_figures():
    seen = set()
    for f in IMG.FIGURES:
        if f["id"] in seen or f["stem"] in seen:
            err(f"images.py: duplicate figure {f['id']}")
        seen |= {f["id"], f["stem"]}
        m = MODS.get(f["mid"])
        if not m or f["section"] not in {s["id"] for s in m["sections"]}:
            err(f"images.py: {f['id']} points at a missing section {f['mid']}/{f['section']}")
        if f["goal"] not in ("Understand", "Apply", "Appreciate"):
            err(f"images.py: {f['id']} has no teaching purpose")


# ───────────────────────── module page ─────────────────────────
def build_module(mid):
    m = MODS[mid]
    fname = m["slug"] + ".html"
    n = int(mid)
    cites = Cites(f"module {mid}")
    i = ORDER.index(mid)
    prev_m = MODS[ORDER[i - 1]] if i > 0 else None
    next_m = MODS[ORDER[i + 1]] if i < len(ORDER) - 1 else None

    parts = []
    obj = "\n".join(f"    <li>{o}</li>" for o in m["objectives"])
    parts.append(f"""<section class="section" id="objectives">
  <div class="section-tag">Learning objectives &middot; about {m['hours']:g} hours ({m['study']:g} study, {m['sim']:g} simulation, {m['work']:g} supervised workplace) &middot; week {m['week']} &middot; {m['pathway']}</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
</section>""")
    ids = set()
    for s in m["sections"]:
        if s["id"] in ids:
            err(f"module {mid}: duplicate section id {s['id']}")
        ids.add(s["id"])
        parts.append(f"""<section class="section" id="{s['id']}">
  <div class="section-tag">{s['tag']}</div>
  <h2>{s['h2']}</h2>
{cites.render(s['html'].strip())}
{figure_html(mid, s['id'])}
</section>""")
    c = m["case"]
    acte = "\n".join(f'    <div class="nc-acte-card"><h4>{k}</h4><div>{v}</div></div>' for k, v in c["acte"].items())
    rnd, sub = m["second_round"]
    outcome = (f'  <div class="tc-scene tn-outcome"><span class="tc-lab">How it played out &middot; fictional</span>\n{c["outcome"].strip()}\n  </div>\n'
               if c.get("outcome") else "")
    parts.append(f"""<section class="section" id="case">
  <div class="section-tag">Practice case &middot; fictional</div>
  <h2>Case: {c['title']}</h2>
  <div class="nc-case">
{c['html'].strip()}
  </div>
  <p>Before reading on, decide what you would notice, whom you would tell and what you would say, what you would do within your role, and what would make you call for help at once. Then compare with the debrief below.</p>
  <div class="nc-acte">
{acte}
  </div>
{outcome}  <div class="nc-task"><strong>Documentation task.</strong> {c['task']}</div>
  <div class="tn-round"><span class="tc-lab">Second round &middot; what changes</span>{rnd}<br><strong>Submit:</strong> {sub}</div>
</section>""")
    if len(m["quiz"]) < BANK_SIZE:
        err(f"module {mid}: question bank has {len(m['quiz'])} items (must be at least {BANK_SIZE})")
    if len(m["exam"]) != 4 or sorted(q.get("half") for q in m["exam"]) != ["a", "a", "b", "b"]:
        err(f"module {mid}: needs exactly 4 exam items, two marked half 'a' and two 'b'")
    for q in m["quiz"] + m["exam"]:
        cites.add(q.get("sources", []))
    n_crit = sum(1 for q in m["quiz"] if q.get("critical"))
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Knowledge check</div>
  <h2>Check your understanding</h2>
  <p>Each visit draws {DRAW} questions at random from this module&rsquo;s {len(m['quiz'])}-question bank, in a shuffled order with shuffled options. Choose the single best answer for each, then select <strong>Check answers</strong>; a reason appears under every option. The target is {MOD_PASS} of {DRAW} with every question marked <em>safety-critical</em> answered correctly ({n_crit} of the {len(m['quiz'])} are). Select <strong>New set of questions</strong> for a different mix. Nothing you select is sent anywhere; scoring happens in your browser and records self-study only. It never shows that you are competent at work.</p>
{quiz_form(f"dna{mid}", m['quiz'], f'module {mid}', DRAW, f' data-pass="{MOD_PASS}" data-critical-pass')}
  <div class="nc-task"><strong>Reflect.</strong> {m['reflect']}</div>
</section>""")
    rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES if k in m["comps"])
    parts.append(f"""<section class="section" id="competencies">
  <div class="section-tag">Competencies</div>
  <h2>What this module builds</h2>
  <div class="table-wrap"><table>
  <caption>Course competencies addressed in this module</caption>
  <thead><tr><th scope="col">Code</th><th scope="col">The learner can</th><th scope="col">Course evidence</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
  <p><strong>Performance evidence for this module:</strong> {m['evidence_out']}</p>
  <div class="tn-crit"><strong>Critical failure:</strong> {m['critical']}</div>
</section>""")
    items = "\n".join(f"    <li>{x}</li>" for x in m["practice"]["items"])
    parts.append(f"""<section class="section" id="practice">
  <div class="section-tag">Supervised practice</div>
  <h2>With your preceptor</h2>
  <p>{m['practice']['intro']} These are prompts for supervised learning, not a procedure. Use your center&rsquo;s own procedures, device instructions, contacts and forms; your preceptor observes and signs off each item on the facility&rsquo;s competency record. Proposed evidence: at least three satisfactory observations across two shifts for each workplace skill that applies to you.</p>
  <ul class="nc-check">
{items}
  </ul>
</section>""")
    rd = []
    for f, why in m["readings"]:
        meta = N.page_meta(f)
        if not meta:
            err(f"module {mid}: assigned reading not found: guides/{f}")
            continue
        rd.append(f'    <li><a href="{f}">{N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False)}</a><span>{why}</span></li>')
    np = []
    if prev_m:
        np.append(f'<a class="nc-np" href="{prev_m["slug"]}.html"><small>← Previous &middot; Module {int(prev_m["id"])}</small>{prev_m["title"]}</a>')
    else:
        np.append(f'<a class="nc-np" href="{HUB}"><small>← Subtrack home</small>{COURSE["long_title"]}</a>')
    if next_m:
        np.append(f'<a class="nc-np nc-np-next" href="{next_m["slug"]}.html"><small>Next &middot; Module {int(next_m["id"])} →</small>{next_m["title"]}</a>')
    else:
        np.append(f'<a class="nc-np nc-np-next" href="{EXAM}"><small>Finish →</small>End-of-course knowledge check</a>')
    parts.append(f"""<section class="section" id="reading">
  <div class="section-tag">Assigned reading</div>
  <h2>Read next on this site</h2>
  <p>Cross-track and patient-guide reading is background, not practical training for the assistant role.</p>
  <ul class="nc-read">
{chr(10).join(rd)}
  </ul>
{calc_cards(m.get('calcs', []), f'module {mid}')}
  <p>Back to the <a href="{HUB}">Nurse Assistant / PCA course home</a> &middot; the <a href="{PARENT}">Nephrology Nursing course</a>, where nurses learn the clinical reasoning behind the care you support.</p>
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")

    main = tn_expand("\n\n".join(parts), fname)
    nav = [("objectives", "Objectives")] + [(s["id"], s["nav"]) for s in m["sections"]] + \
          [("case", "Case"), ("quiz", "Knowledge check"), ("competencies", "Competencies"), ("practice", "Supervised practice"), ("reading", "Reading")]
    cards = [(HUB, "Subtrack home", COURSE["long_title"], "Role, syllabus, assessment and all twelve modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], html.unescape(next_m["sub"]).split(",")[0] + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], html.unescape(prev_m["sub"]).split(",")[0] + "."))
    for f, why in m["readings"][:2]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Assigned reading", N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{m['title']}: Dialysis Nurse Assistant Module {n}"
    page = N.shell(
        fname, title, m["desc"], m["keywords"], f"Nephrology Nursing Track &middot; By Role &middot; Module {n} of {len(MODS)}", m["title"], m["sub"],
        "Dialysis Nurse Assistants and Patient Care Assistants in adult hemodialysis &middot; their preceptors and nurse educators",
        nav, bar(f"Module {n}"), main, N.glossary_block(main, m.get("terms", [])), N.related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": "Dialysis Nurse Assistant / Patient Care Assistant (Renal Care Academy)", "url": f"{SITE}/guides/{COURSE['hub_slug']}"},
                      "learningResourceType": "Self-study module with case and knowledge check",
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": m["slug"] + "-vignette-hero", "alt": m["image_alt"]}, disclaimer=DISCLAIMER,
    )
    (GUIDES / fname).write_text(finish(page), encoding="utf-8")
    return fname, cites.list()


# ───────────────────────── hub ─────────────────────────
def build_hub():
    cites = Cites("hub")
    cards = []
    for mid in ORDER:
        m = MODS[mid]
        cards.append(tile(f"""    <a class="nc-mod" href="{m['slug']}.html" data-module="dna{mid}">""", f"""      <span class="nc-mod-top"><span class="nc-mod-step">Week {m['week']}</span><span>Module {int(mid)}</span><span class="nc-chip">{m['hours']:g} h</span><span class="nc-chip">{', '.join(m['comps']) if len(m['comps']) < 6 else 'P1–P12'}</span></span>
      <span class="nc-mod-title">{m['title']}</span>
      <span class="nc-mod-desc">{html.escape(html.unescape(m['sub']), quote=False)}</span>
      <span class="nc-mod-status" aria-live="off"></span>""", m['slug']))
    sched = "\n".join(
        f"<tr><td>{m['week']}</td><td><a href=\"{m['slug']}.html\">DNA-{mid} {m['title']}</a></td><td>{m['study']:g}</td><td>{m['sim']:g}</td><td>{m['work']:g}</td>"
        f"<td>{m['hours']:g}</td><td>{m['evidence_out']}</td></tr>" for m in (MODS[x] for x in ORDER))
    ts = sum(MODS[x]['study'] for x in ORDER); tsim = sum(MODS[x]['sim'] for x in ORDER); tw = sum(MODS[x]['work'] for x in ORDER)
    total = ts + tsim + tw
    if total != 120:
        err(f"hub: proposed hours total {total}, expected 120")
    comp_rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES)
    src = "".join(f"[[{k}]]" for k in C.HUB_REFS)
    n_mod = len(ORDER)
    n_bank = sum(len(MODS[x]["quiz"]) for x in ORDER)
    n_pool = sum(len(MODS[x]["exam"]) for x in ORDER)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>A supervised support role beside the dialysis nurse</h2>
  <p>This subtrack is for the Dialysis Nurse Assistant, also called the Patient Care Assistant (PCA): the supervised support worker who greets patients, weighs them, takes the observations the registered nurse (RN) assigns, prepares supplies, helps with comfort and movement, keeps the access in view, cleans external surfaces, carries sealed specimens and keeps honest records. It sits in the Nephrology Nursing Track under <strong>By Role</strong>. It is not a registered-nurse specialty, it is not a shortened nursing program, and it is not equivalent to a dialysis technician. In this course, PCA always means Patient Care Assistant; the United States Patient Care Technician (PCT) is a different role.</p>
  <p>Each of the {n_mod} modules follows the same path: a plain picture first, then the physiology behind it, then what the evidence actually shows (and does not show), then exactly what you do, what you report and what you never do. Every module has worked bedside scenarios, a full fictional case set in a Philippine unit with a debrief and a harder second round, a {BANK_SIZE}-question knowledge check with a reason under every option, and a checklist to practice with your preceptor. Three modules connect to the new <a href="{CALC}">Patient Care Assistant Toolkit</a>.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this subtrack is, and is not</h4>
      <p>It is education and practice preparation. Finishing it does not prove competence, grant permission for any task, or carry Department of Health (DOH), Philippine Society of Nephrology (PSN), Philippine Health Insurance Corporation (PhilHealth), Technical Education and Skills Development Authority (TESDA) or Professional Regulation Commission (PRC) recognition or continuing professional development (CPD) units. There is no national Philippine PCA license. Basic life support (BLS) needs its own practical course. Your employer authorizes tasks after observed practice. Hours and pass marks are Academy design proposals, not national minimums. {COURSE['status']}.</p>
    </div>
  </div>
</section>

<section class="section" id="day">
  <div class="section-tag">What the work looks like</div>
  <h2>A day at the San Isidro Dialysis Center</h2>
{C.DAY_HTML.strip()}
</section>

<section class="section" id="role">
  <div class="section-tag">The role</div>
  <h2>Observe and do, report at once, never</h2>
  <p>The RN assesses the patient, chooses which tasks to delegate, gives the instructions and reviews what you find. You accept only tasks within your verified competence and report completion or difficulty. The table below is the boundary this course teaches; your employer&rsquo;s written job description may be narrower, and applicable law always governs.</p>
{C.ROLE_TABLE.strip()}
  <p><strong>Conditional tasks.</strong> Machine preparation assistance, point-of-care testing, and carrying medicines or blood products need a separate written local endorsement, device-specific training, an observed assessment and named authorization. Carrying a medicine is not giving it; carrying blood is not transfusing it. A quiz score never unlocks any of these. <a href="{MODS['01']['slug']}.html">Module 1</a> explains delegation and safe refusal.</p>
</section>

<section class="section" id="entry">
  <div class="section-tag">Before you begin</div>
  <h2>Entry, readiness and the Philippine anchor</h2>
  <p>Anyone may read this subtrack. For the Philippine workplace pathway, the PSN guidelines describe nursing assistants as BS Nursing graduates awaiting registration, BS Nursing undergraduates who have completed at least the second year, and BS Midwifery graduates; employers verify these records.[[psn2024]] A completed nursing degree without PRC registration does not authorize registered nursing practice. Before placement, this program proposes an occupational health review (including hepatitis B vaccination and immunity, decided by occupational health), employer induction, and a current practical BLS course from a recognized provider.</p>
  <p><strong>Delivery.</strong> {total:g} proposed hours: {ts:g} guided study, {tsim:g} simulation and skills lab, and {tw:g} supervised workplace learning. A suggested six-week part-time sequence covers two modules a week. The workplace blocks of Modules 1 to 4 are observation only. BLS, induction and any optional local endorsements are additional. Placement extends until competence is shown; experienced assistants may have a preceptor-led gap assessment, but seniority never waives a safety demonstration.</p>
</section>

<section class="section" id="modules">
  <div class="section-tag">The modules</div>
  <h2>{n_mod} modules</h2>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
  <div class="nc-modgrid" id="nc-modules">
{chr(10).join(cards)}
  </div>
  <p style="margin-top:14px;"><strong>When you have finished:</strong> take the <a href="{EXAM}">end-of-course knowledge check</a>: {COURSE['exam_items']} questions, two from each module, drawn from a pool of {n_pool}. The pass mark is {COURSE['pass_correct']} of {COURSE['exam_items']} with no safety-critical question missed.</p>
</section>

<section class="section" id="outcomes">
  <div class="section-tag">Exit competencies</div>
  <h2>What you will be able to do</h2>
  <div class="table-wrap"><table>
  <caption>Twelve exit competencies</caption>
  <thead><tr><th scope="col">Code</th><th scope="col">The learner can</th><th scope="col">Evidence</th></tr></thead>
  <tbody>
{comp_rows}
  </tbody></table></div>
</section>

<section class="section" id="schedule">
  <div class="section-tag">Syllabus</div>
  <h2>Syllabus and proposed hours</h2>
  <div class="table-wrap"><table>
  <caption>Proposed hours per module (study, simulation, supervised workplace)</caption>
  <thead><tr><th scope="col">Week</th><th scope="col">Module</th><th scope="col">Study</th><th scope="col">Simulation</th><th scope="col">Workplace</th><th scope="col">Total</th><th scope="col">Observable evidence</th></tr></thead>
  <tbody>
{sched}
  <tr><td></td><td><strong>Total</strong></td><td><strong>{ts:g}</strong></td><td><strong>{tsim:g}</strong></td><td><strong>{tw:g}</strong></td><td><strong>{total:g}</strong></td><td>BLS is additional</td></tr>
  </tbody></table></div>
  <p>Hours are teaching allocations, not a claim that every skill takes the same time to master, and not a statutory training requirement.</p>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>Three separate records</h2>
  <div class="table-wrap"><table>
  <caption>Completion labels and who records them</caption>
  <thead><tr><th scope="col">Label</th><th scope="col">Requirement</th><th scope="col">Recorded by</th></tr></thead>
  <tbody>
  <tr><td>Self-study complete</td><td>All modules read; the <a href="{EXAM}">end-of-course knowledge check</a> passed ({COURSE['pass_correct']} of {COURSE['exam_items']}, no safety-critical item missed). Module checks: {MOD_PASS} of {DRAW} with every safety-critical item right; {n_bank} module items in all.</td><td>The learner, here (optionally saved in this browser only)</td></tr>
  <tr><td>Simulation requirements met</td><td>The six capstone stations in <a href="{MODS['12']['slug']}.html#stations">Module 12</a>, every critical criterion met without a prompt</td><td>Faculty, on an offline record</td></tr>
  <tr><td>Workplace competencies verified for listed tasks</td><td>At least three satisfactory observations of each applicable skill across at least two shifts; more if performance varies</td><td>The employer, on its own signed records</td></tr>
  </tbody></table></div>
  <p>Never describe a browser score as &ldquo;certified PCA,&rdquo; &ldquo;PSN-accredited,&rdquo; &ldquo;DOH-approved&rdquo; or &ldquo;competent to practice independently.&rdquo; Critical failures are never averaged away: they lead to feedback, practice and reassessment with an equivalent scenario.</p>
</section>

<section class="section" id="staffing">
  <div class="section-tag">Regulation</div>
  <h2>Staffing rules, and a discrepancy to keep visible</h2>
  <p>The DOH licensing rules require dialysis nurses to be PRC-registered with renal-care training and BLS, with at least one nurse per shift holding current advanced cardiovascular life support (ACLS), and set a maximum of one nurse to four HD stations.[[doh2012]] The PSN guidelines discuss one nurse to six patients when a nursing assistant is present.[[psn2024]] The two use different denominators and come from different authorities. This course does not offer a staffing calculator and does not treat the PSN wording as permission to staff above the DOH limit; written confirmation from the DOH licensing authority would be needed before relying on any exception. An assistant never counts as a registered nurse.</p>
  <p>Evidence from hospital wards supports keeping that line: in 243 European hospitals, replacing one professional nurse with one nursing assistant per 25 patients was associated with 21% higher odds of surgical death (observational data).[[aiken2017]] PhilHealth&rsquo;s hemodialysis circulars set coverage and quality standards; they are financing and quality policies, not a scope or credential for assistants.[[phic2024_23]][[phic2024_29]]</p>
</section>

<section class="section" id="international">
  <div class="section-tag">International comparison</div>
  <h2>Three systems, and why nothing transfers automatically</h2>
  <div class="table-wrap"><table>
  <caption>Comparable roles abroad</caption>
  <thead><tr><th scope="col">Country</th><th scope="col">Role and source</th><th scope="col">What transfers</th><th scope="col">What does not</th></tr></thead>
  <tbody>
  <tr><td>United States</td><td>Dialysis Patient Care Technician (PCT): high-school diploma, RN-directed approved training, state rules, certification within 18 months for new hires (42 Code of Federal Regulations &sect;494.140)[[cfr494]]</td><td>Competency-based training, structured supervision</td><td>PCT duties such as cannulation, United States certification and its 18-month rule</td></tr>
  <tr><td>United Kingdom</td><td>National Health Service (NHS) employer job descriptions for dialysis healthcare assistants (HCA): observations, weights, movement help, preparation, cleaning; some trained posts do more</td><td>Dignity, delegated care, escalation, local competency records</td><td>NHS bands, advanced procedural duties, employment eligibility</td></tr>
  <tr><td>Singapore</td><td>Government healthcare-assistant framework: basic care and monitoring under trained nurses</td><td>Basic care, teamwork, quality participation</td><td>Dialysis-specific authorization or cross-border recognition</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="educators">
  <div class="section-tag">For educators and preceptors</div>
  <h2>Localize before teaching, and keep a printable record</h2>
  <p>The lessons use generic workflows on purpose. Before teaching, gather the unit&rsquo;s written job description and competency record for assistants, its escalation contacts and emergency codes, the identification policy, the scales and their tare labels, the observation devices and cuff sizes, the approved disinfectants with dilution and contact time, the waste chart, the specimen procedure, the documentation and correction policy, and the disaster and outage plans. Use them in every simulation. Use training props: moulage blood, mock sharps, empty specimen tubes, fluorescent gel. Never use real blood or real sharps for teaching.</p>
  <div class="dna-record">
  <div class="table-wrap"><table>
  <caption>Printable competency record (template; not a certificate). Mark each entry O (observation), S (simulation) or P (supervised patient contact).</caption>
  <thead><tr><th scope="col">Skill</th><th scope="col">Procedure and version</th><th scope="col">Date 1 &middot; O/S/P &middot; assessor</th><th scope="col">Date 2 &middot; O/S/P &middot; assessor</th><th scope="col">Date 3 &middot; O/S/P &middot; assessor</th><th scope="col">Authorized / restricted / not assigned</th></tr></thead>
  <tbody>
  <tr><td>Identification and weight with tare</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Assigned observations and escalation</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Station readiness and supply check</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Access observation and alarm relay</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Transfer and departure handover</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Station cleaning and waste</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Records and specimen transport</td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody></table></div>
  </div>
  <p>Refresh at least yearly, and immediately after an incident, a new device or procedure, a long absence or a poor audit. Medical director, head nurse, infection prevention lead and compliance officer each sign off their part of the content before local use.</p>
</section>

<section class="section" id="calculators">
  <div class="section-tag">Tools</div>
  <h2>The Patient Care Assistant Toolkit</h2>
  <p>Built for this subtrack. Three tools check the numbers an assistant is asked to measure: a <strong>weight and tare check</strong> (net weight, pounds to kilograms, gain since the last session and your unit&rsquo;s report threshold); a <strong>standing blood pressure check</strong> against the consensus definition of orthostatic hypotension; and a <strong>timed count and temperature converter</strong>. Every tool ends in a report to the RN; none suggests a treatment change.</p>
{calc_cards([CALC, 'calc-dialysis-support-staff-toolkit.html', 'calc-qapi-run-chart-spc.html'], 'hub').replace('Calculators for this module', 'Calculators')}
</section>

<section class="section" id="sources">
  <div class="section-tag">Evidence and policy register</div>
  <h2>Sources behind this subtrack</h2>
  <p>Evidence checked 25 November 2026 (Blueprint v2). Peer-reviewed studies were retrieved through PubMed; each module cites its own. Before publication or workplace use, the unit&rsquo;s medical director, head nurse, infection prevention lead and compliance officer should review the wording, and the current HFSRB assessment tool and staffing interpretation, current PhilHealth circulars and any PSN revision of the assistant role should be obtained and reconciled. Local procedures and device instructions always govern.{cites.render(src)}</p>
</section>"""
    main = tn_expand(main, HUB)
    nav = [("start", "Start here"), ("day", "A day in the unit"), ("role", "The role"), ("entry", "Entry"), ("modules", "Modules"),
           ("outcomes", "Competencies"), ("schedule", "Syllabus"), ("assessment", "Assessment"), ("staffing", "Staffing rules"),
           ("international", "Abroad"), ("educators", "For educators"), ("calculators", "Toolkit"), ("sources", "Sources")]
    related = [(PARENT, "Parent course", "Nephrology Nursing &amp; Hemodialysis", "The nursing course whose care this role supports."),
               (ENTRY, "Related lesson", "Nephrology Nursing Module 9: the HD session and complication response", "How nurses respond to problems during a session."),
               (MODS["01"]["slug"] + ".html", "Start", MODS["01"]["title"], "Module 1 of the subtrack."),
               (EXAM, "Knowledge check", "End-of-Course Knowledge Check", f"{COURSE['exam_items']} questions, two per module; pass at {COURSE['pass_correct']}.")]
    page = N.shell(
        HUB, "Dialysis Nurse Assistant / Patient Care Assistant (PCA) · Renal Care Academy",
        f"A free Philippine-first training subtrack in the Renal Care Academy&rsquo;s Nephrology Nursing Track (By Role) for the Dialysis Nurse Assistant / Patient Care Assistant (PCA): {n_mod} modules on scope and delegation, kidney failure, dignity and privacy, infection prevention, weights and observations, station readiness, access protection, emergencies, safe mobility and departure, cleaning, records and specimens, quality and disasters, with a toolkit.",
        "dialysis nurse assistant training Philippines, patient care assistant dialysis, PCA dialysis course, dialysis nursing assistant, dialysis assistant duties, nursing aide hemodialysis, renal care academy",
        "Nephrology Nursing Track &middot; By Role &middot; Course home", "Dialysis Nurse Assistant / PCA",
        f"{n_mod} modules for the supervised support worker in hemodialysis: the reason behind every task, what the evidence shows, worked scenarios and calculators, and exactly where the role begins and ends.",
        "Dialysis Nurse Assistants and Patient Care Assistants in adult hemodialysis &middot; their preceptors, nurse educators and head nurses",
        nav, bar("Subtrack home").replace(f'<span class="nc-sep">›</span><a href="{HUB}">{COURSE["title"]}</a><span class="nc-sep">›</span><span>Subtrack home</span>', f'<span class="nc-sep">›</span><span>{COURSE["title"]}</span>'),
        main, N.glossary_block(main, []), N.related_block(related),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": "Supervised support-role training for Dialysis Nurse Assistants / Patient Care Assistants in hemodialysis.",
                      "alternateName": ["Dialysis Nursing Assistant", "Patient Care Assistant", "PCA", "Dialysis assistant"],
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE},
                      "hasPart": [{"@type": "LearningResource", "name": MODS[x]["title"], "url": f"{SITE}/guides/{MODS[x]['slug']}"} for x in ORDER],
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "A dialysis nurse assistant weighing an older patient on a wheelchair scale while a registered nurse looks on in a bright Philippine dialysis unit."},
        disclaimer=DISCLAIMER,
    )
    track = ROOT / "images" / "og" / "academy" / f"{COURSE['hub_slug']}.jpg"
    if track.exists():
        page = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*"', lambda m: f'{m.group(1)}{SITE}/images/og/academy/{track.name}"', page)
    (GUIDES / HUB).write_text(finish(page), encoding="utf-8")
    return HUB, cites.list()


# ───────────────────────── end-of-course knowledge check ─────────────────────────
def build_exam():
    cites = Cites("exam")
    items = []
    for mid in ORDER:
        for q in MODS[mid]["exam"]:
            items.append(dict(q, group=f"m{mid}{q['half']}"))
            cites.add(q.get("sources", []))
    n_mod = len(ORDER)
    groups = len({q["group"] for q in items})
    if groups != COURSE["exam_items"]:
        err(f"exam: {groups} groups but {COURSE['exam_items']} items drawn")
    main = f"""<section class="section" id="exam">
  <div class="section-tag">End-of-course knowledge check</div>
  <h2>{COURSE['exam_items']} questions, two from each module</h2>
  <p>Each sitting draws two questions from each of the {n_mod} modules (a pool of {len(items)}), in a shuffled order with shuffled options. Answer all of them, then select <strong>Check answers</strong>. The pass mark is <strong>{COURSE['pass_correct']} of {COURSE['exam_items']}</strong> (80%, rounded up), and every question marked <em>safety-critical</em> must be answered correctly; a missed safety-critical question means &ldquo;not yet passed&rdquo; whatever the total. A reason appears under every option.</p>
  <p>A pass marks your <strong>Academy self-study as complete</strong>. It is not simulation sign-off or employer-verified competence, and it does not authorize any task. These are formative questions, not a secure examination. If you do not pass, review the modules for the questions you missed, then select <strong>New set of questions</strong>.</p>
{quiz_form("dna-final", items, 'exam', COURSE['exam_items'], f' data-stratify="1" data-pass="{COURSE["pass_correct"]}" data-critical-pass')}
</section>

<section class="section" id="next">
  <div class="section-tag">After the check</div>
  <h2>Next steps</h2>
  <p>Prepare for the six <a href="{MODS['12']['slug']}.html#stations">capstone stations</a> with your faculty, and arrange observed practice of your assigned tasks with your preceptor. Return to the <a href="{HUB}">course home</a>.</p>
</section>"""
    main = tn_expand(main, EXAM)
    page = N.shell(
        EXAM, "End-of-Course Knowledge Check: Dialysis Nurse Assistant / PCA · Renal Care Academy",
        f"{COURSE['exam_items']}-question end-of-course knowledge check for the Renal Care Academy Dialysis Nurse Assistant / Patient Care Assistant subtrack: two questions from each module, pass mark {COURSE['pass_correct']} of {COURSE['exam_items']} with every safety-critical item correct, with reasons for every answer.",
        "dialysis nurse assistant quiz, patient care assistant test, PCA dialysis knowledge check, renal care academy",
        "Nephrology Nursing Track &middot; By Role &middot; Examination", "End-of-Course Knowledge Check",
        f"Two questions from each of the {n_mod} modules, drawn at random each sitting. Pass with {COURSE['pass_correct']} of {COURSE['exam_items']} and every safety-critical question correct.",
        "Learners who have completed the Dialysis Nurse Assistant / PCA modules",
        [("exam", "Knowledge check"), ("next", "Next steps")], bar("Knowledge check"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Subtrack home", COURSE["long_title"], "All modules, the role and assessment details."),
                         (MODS["12"]["slug"] + ".html", "Capstone", MODS["12"]["title"], "The six practical stations.")]),
        jsonld_extra={"learningResourceType": "Quiz", "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "A dialysis nurse assistant completing a knowledge check on a phone in a staff room."},
        disclaimer=DISCLAIMER,
    )
    (GUIDES / EXAM).write_text(finish(page), encoding="utf-8")
    return EXAM, cites.list()


# ───────────────────────── entry links ─────────────────────────
MARK = ("<!-- DNA-START -->", "<!-- DNA-END -->")


def _strip(s):
    return re.sub(re.escape(MARK[0]) + r".*?" + re.escape(MARK[1]) + r"\n?", "", s, flags=re.S)


LMARK = ("<!-- DNA-ROW-START -->", "<!-- DNA-ROW-END -->")
NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
       "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two",
       "twenty-three", "twenty-four", "twenty-five"]


def wire_landing_content(s):
    """Landing-page prose and tables for this subtrack (idempotent): the nursing track paragraph, the subtrack count in
    words (kept equal to the stat chip), and one row each in the qualifications, onboarding and career-move tables."""
    s = re.sub(re.escape(LMARK[0]) + r".*?" + re.escape(LMARK[1]) + r"\n?", "", s, flags=re.S)
    old_p = "and Special Dialysis Nurse Roles, for the nurse who holds a portfolio.</p>"
    new_p = ("and Special Dialysis Nurse Roles, for the nurse who holds a portfolio. Beside them sits the "
             "<a href=\"dialysis-nurse-assistant.html\">Dialysis Nurse Assistant / Patient Care Assistant (PCA)</a> subtrack, for the "
             "supervised support worker who weighs, observes, prepares and reports on the nurse&rsquo;s delegation; it is a support role, "
             "not a nursing specialty.</p>")
    if "dialysis-nurse-assistant.html\">Dialysis Nurse Assistant / Patient Care Assistant (PCA)</a> subtrack" not in s:
        s = s.replace(old_p, new_p, 1)
    m = re.search(r'acad-stat"><b>(\d+)</b> subtracks', s)
    if m and int(m.group(1)) < len(NUM):
        n = int(m.group(1))
        for w in NUM[n - 3:n]:
            s = re.sub(rf"\b(Five tracks and|with) {w} subtracks", rf"\1 {NUM[n]} subtracks", s)
    rows = {
        '<tr><td><a href="dialysis-charge-nurse.html">Charge Nurse</a></td>':
            f'{LMARK[0]}<tr><td><a href="{HUB}">Dialysis Nurse Assistant / PCA</a></td><td><ul class="acad-qual">'
            + "".join(f"<li>{x}</li>" for x in _qual_items()) + f'</ul></td></tr>{LMARK[1]}\n',
        '<tr><td>Head nurse, new or promoted</td>':
            f'{LMARK[0]}<tr><td>Dialysis nurse assistant or patient care assistant</td><td><a href="{HUB}">Dialysis Nurse Assistant / PCA</a></td>'
            f'<td>Modules 1, 4, 5, and 7: role and delegation, infection prevention, weights and observations, the access</td>'
            f'<td>Practical BLS; observed sign-off on each delegated task; six capstone stations; end-of-course knowledge check</td></tr>{LMARK[1]}\n',
        '<tr><td>Head nurse</td><td>Unit operations manager or unit manager</td>':
            f'{LMARK[0]}<tr><td>Dialysis nurse assistant who passes the nursing board</td><td>Hemodialysis staff nurse</td>'
            f'<td><a href="nephrology-nursing.html">Hemodialysis Nurse</a>, from Module 1; the assistant modules do not count toward it</td></tr>{LMARK[1]}\n',
    }
    for anchor, row in rows.items():
        i = s.find(anchor)
        if i < 0:
            err(f"academy/index.html: table anchor not found: {anchor[:60]}")
            continue
        if anchor.startswith('<tr><td><a href="dialysis-charge-nurse.html">'):   # after the Charge Nurse row
            j = s.find("</tr>", i) + len("</tr>")
            j = s.find("\n", j) + 1
            s = s[:j] + row + s[j:]
        else:                                                                     # before the anchor row
            s = s[:i] + row + s[i:]
    return s


def _qual_items():
    spec = importlib.util.spec_from_file_location("acad_qual_dna", ROOT / "tools" / "academy" / "qualifications.py")
    q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
    return q.QUAL[COURSE["hub_slug"]][1]


def wire_parent():
    """Idempotently link the subtrack from the parent hub (role card via tools/academy/nursing_specialties.py, rendered by
    generate_transplant_nurse.wire_parent()), from Nephrology Nursing Module 9, and from the Academy landing page
    (By Role column and the track links, after Charge Nurse)."""
    done = []
    r = subprocess.run([sys.executable, "-c", "import generate_transplant_nurse as T; print(T.wire_parent())"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0:
        done.append(PARENT + " (via transplant wire)")
    else:
        err(f"transplant wire_parent failed: {(r.stderr or r.stdout).strip()[-300:]}")
    p = ACADEMY / ENTRY
    if p.exists():
        s = _strip(p.read_text(encoding="utf-8"))
        block = f"""{MARK[0]}
<section class="section" id="nurse-assistant">
  <div class="section-tag">For the whole team</div>
  <h2>Working with a Dialysis Nurse Assistant</h2>
  <p>Many units add supervised assistants who weigh patients, take the observations you delegate, prepare supplies, keep the access in view and help with transfers and departure. The Renal Care Academy&rsquo;s <a href="{HUB}">Dialysis Nurse Assistant / PCA</a> subtrack trains them to report early and to stay inside the role, so that your assessment stays yours. Use it to orient new assistants and to agree what you delegate, how they report, and what they never do.</p>
</section>
{MARK[1]}
"""
        anchor = '<section class="section" id="reading">'
        if anchor in s:
            s = s.replace(anchor, block + anchor, 1)
            if 'href="#nurse-assistant"' not in s:
                s = s.replace('<a class="nav-pill" href="#reading">', '<a class="nav-pill" href="#nurse-assistant">Nurse assistant</a>\n<a class="nav-pill" href="#reading">', 1)
            p.write_text(s, encoding="utf-8")
            done.append(ENTRY)
        else:
            err(f"anchor not found in academy/{ENTRY}")
    idx = ACADEMY / "index.html"
    if idx.exists():
        s = _strip(idx.read_text(encoding="utf-8"))
        land = f"""{MARK[0]}
    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/{COURSE['hub_slug']}.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">
      <span class="tc-branch-body"><small>By Role &middot; supervised support</small><b>Dialysis Nurse Assistant / PCA</b><span>For the supervised assistant beside the dialysis nurse: role and delegation, kidney failure, dignity and privacy, infection prevention, weights and observations, station readiness, access protection, emergencies, safe departure, cleaning, records and specimens, quality and disasters.</span><span><strong>{len(ORDER)} modules &middot; worked scenarios &middot; assistant toolkit &middot; six-station capstone</strong></span></span>
    </a>
{MARK[1]}
"""
        k = s.find('<div class="nn-col" id="nursing-role">')
        if k >= 0:
            end = s.find("\n    </div>\n  </div>", k)
            if end >= 0:
                s = s[:end + 1] + land + s[end + 1:]
                nav = (f'{MARK[0]}\n    <a class="acad-track acad-subtrack" href="{HUB}"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">'
                       f'<circle cx="9" cy="7" r="3"/><path d="M3 21a6 6 0 0 1 12 0"/><path d="M16 11h6M19 8v6"/></svg></span>'
                       f'<span class="acad-track-t"><strong>Dialysis Nurse Assistant / PCA</strong><small>{len(ORDER)} modules</small></span></a>\n{MARK[1]}\n')
                a = s.find('    <a class="acad-track" href="dialysis-charge-nurse.html">')
                if a < 0:
                    a = s.find('    <a class="acad-track" href="dialysis-head-nurse.html">')
                if a >= 0:
                    e = s.find("\n", s.find("</a>", a)) + 1
                    s = s[:e] + nav + s[e:]
                s = wire_landing_content(s)
                idx.write_text(s, encoding="utf-8")
                done.append("index.html")
            else:
                err("academy/index.html: end of By Role column not found")
        else:
            err("academy/index.html: By Role column not found")
    return done


# ───────────────────────── Patient Care Assistant Toolkit ─────────────────────────
CALC_REFS = ["kalantar2009", "saran2003", "freeman2011", "kallioinen2017", "sjoding2020"]
CALC_PIPELINE = ["patch_published_time.py", "patch_reading_time.py", "REFS", "patch_hero_meta.py", "patch_share_title.py",
                 "patch_canonical_clean_urls.py", "patch_share_buttons.py", "patch_guide_rail.py", "add_calc_nav_pill.py",
                 "patch_calc_handoff.py", "patch_calc_english_only.py"]
CALC_CARD = """<a class="related-card" href="calc-dialysis-nurse-assistant-toolkit.html">
<div class="related-card-tag">Dialysis unit · Nurse assistant</div>
<div class="related-card-title">Patient Care Assistant Toolkit</div>
<div class="related-card-desc">Net weight with wheelchair tare and weight gain, standing blood pressure check, and timed counts and temperature.</div>
<div class="related-card-arrow">Open →</div></a>
"""


def build_calc():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "dialysis_nurse_assistant" / "build_calc_toolkit.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    idx = GUIDES / "calculators.html"
    if idx.exists():
        s = idx.read_text(encoding="utf-8")
        if f'href="{CALC}"' not in s:
            for anchor in ('<a class="related-card" href="calc-dialysis-support-staff-toolkit.html">',
                           '<a class="related-card has-thumb" href="calc-dgf-risk.html">'):
                if anchor in s:
                    idx.write_text(s.replace(anchor, CALC_CARD + anchor, 1), encoding="utf-8")
                    print("added the calculator card to calculators.html")
                    break
            else:
                err("calculators.html: anchor for the new card not found")
    return [REFS[k] for k in CALC_REFS]


def run_calc_pipeline():
    PY = N.pipeline_python()
    for step in CALC_PIPELINE:
        cmd = ([PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", CALC]
               if step == "REFS" else [PY, step, "--guide", CALC])
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  ! {step} failed on {CALC}: {(r.stderr or r.stdout).strip()[-300:]}")
    for cmd in (["build_calc_app.py"], ["generate_latest_calculators.py"]):
        r = subprocess.run([PY] + cmd, cwd=ROOT, capture_output=True, text=True)
        print(f"  {cmd[0]}: {'ok' if r.returncode == 0 else (r.stderr or r.stdout).strip()[-300:]}")


# ───────────────────────── pipeline ─────────────────────────
PIPELINE = [s for s in N.PIPELINE]


def run_pipeline(files):
    PY = N.pipeline_python()
    for f in files:
        for step in PIPELINE:
            if step == "REFS":
                cmd = [PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", f]
            else:
                cmd = [PY, step, "--guide", f]
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  ! {step} failed on {f}: {(r.stderr or r.stdout).strip()[-300:]}")
        print(f"  patched {f}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--patch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", help="comma-separated page filenames to patch (with --patch)")
    ap.add_argument("--calc", action="store_true", help="(re)build the Patient Care Assistant Toolkit and run its pipeline")
    args = ap.parse_args()
    global GUIDES
    if args.check:
        import tempfile
        GUIDES = Path(tempfile.mkdtemp())
    calc_refs = build_calc() if (args.calc and not args.check) else None
    check_figures()
    refs = {}
    for mid in ORDER:
        f, r = build_module(mid)
        refs[f] = r
    f, r = build_hub(); refs[f] = r
    f, r = build_exam(); refs[f] = r
    if calc_refs is not None:
        refs[CALC] = calc_refs
    elif (DATA / "refs-overrides.json").exists():
        old = json.loads((DATA / "refs-overrides.json").read_text(encoding="utf-8"))
        if CALC in old:
            refs[CALC] = old[CALC]
    if not args.check:
        DATA.mkdir(parents=True, exist_ok=True)
        (DATA / "refs-overrides.json").write_text(json.dumps(refs, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {len(refs)} pages to guides/")
    if ERRORS:
        print("\nCONTENT ERRORS:")
        for e in ERRORS:
            print("  -", e)
        if args.check:
            sys.exit(1)
    if args.check:
        print("content OK")
        return
    if args.calc:
        run_calc_pipeline()
    if args.patch:
        files = sorted(f for f in refs if f != CALC) if not args.only else args.only.split(",")
        run_pipeline(files)
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    print("entry links:", wire_parent())
    if ERRORS:
        sys.exit(1)


if __name__ == "__main__":
    main()
