#!/usr/bin/env python3
"""Generate the Special Dialysis Nurse Roles subtrack of the Renal Care Academy (Nephrology Nursing, By Role).

Pages: hub (special-dialysis-nurse-roles), 14 modules (special-dialysis-nurse-roles-NN-<slug>), end-of-course knowledge check
(special-dialysis-nurse-roles-final-exam). Content lives in tools/special_nurse_roles/content/*.py (hand-edited).
The chrome (header, course CSS, quiz markup, glossary, related cards, dr-card) is imported from
generate_nursing_course.py so the subtrack looks and behaves like its parent course.

    python3 generate_special_dialysis_nurse_roles.py              # write pages to guides/, then publish to academy/
    python3 generate_special_dialysis_nurse_roles.py --patch      # also run the /setup-guide patch pipeline on each page
    python3 generate_special_dialysis_nurse_roles.py --check      # validate content only (refs, quiz keys, links)

Never hand-edit academy/special-dialysis-nurse-roles*.html: edit the content files and re-run.
An existing page's article:published_time is carried over, so re-running never re-dates a page.
"""
import argparse, html, importlib.util, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_nursing_course as N  # noqa: E402  (chrome, course CSS, helpers)

GUIDES = ROOT / "guides"
ACADEMY = ROOT / "academy"
CONTENT = ROOT / "tools" / "special_nurse_roles" / "content"
DATA = ROOT / "data" / "special-dialysis-nurse-roles"
SITE = "https://renalcarematters.com"
ERRORS = []
BANK_SIZE, DRAW = 15, 5


def err(m):
    ERRORS.append(m)


def load(name):
    spec = importlib.util.spec_from_file_location(f"sdnr_{name}", CONTENT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C = load("course")
IMG = load("images")
COURSE = C.COURSE
HUB = COURSE["hub_slug"] + ".html"
EXAM = COURSE["hub_slug"] + "-final-exam.html"
PARENT = COURSE["parent_slug"] + ".html"
ENTRY = COURSE["entry_slug"] + ".html"
N.ABBR.update(C.ABBR)   # the nursing glossary/auto-expansion helpers read this dict

MODS, ORDER = {}, []
for mid, slug, title, short, week, hours, comps, code, split in C.MODULES:
    m = load(f"m{mid}").MODULE
    m.update(id=mid, slug=f"{COURSE['hub_slug']}-{mid}-{slug}", title=title, short=short, week=week, hours=hours, comps=comps,
             code=code, split=split)
    MODS[mid] = m
    ORDER.append(mid)

# ───────────────────────── references ─────────────────────────
def build_refs():
    raw = {}
    for p in (ROOT / "data" / "nursing-course" / "refs_pubmed_raw.json", ROOT / "data" / "transplant-nurse" / "refs_pubmed_raw.json",
              ROOT / "data" / "dialysis-unit-support-staff" / "refs_pubmed_raw.json", DATA / "refs_pubmed_raw.json"):
        if p.exists():
            raw.update(json.loads(p.read_text(encoding="utf-8")))
    refs = {k: N.C.MANUAL_REFS[k] for k in C.SHARED_MANUAL}
    refs.update(C.MANUAL_REFS)
    for key, pmid in C.PUBMED_REFS.items():
        r = raw.get(pmid)
        if not r:
            err(f"reference {key}: PMID {pmid} missing from refs_pubmed_raw.json")
            continue
        authors = N._apa_authors(r["authors"])
        if not authors.endswith("."):
            authors += "."
        title = (C.TITLE_OVERRIDES.get(pmid) or getattr(N.C, "TITLE_OVERRIDES", {}).get(pmid) or r["title"]).rstrip(".")
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
        refs[key] = f"{authors} ({r['year']}). {html.escape(title, quote=False)}{end} <em>{journal}</em>, {tail}.{link}"
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
/* Special Dialysis Nurse Roles subtrack: visual components (design tokens only, so dark mode holds). */
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
.section .tc-scene p.tc-scene-take{border-top:1px dashed var(--border);padding-top:8px;margin:6px 0 0;font-size:14.5px;color:var(--text-mid);}
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
.nc-result-pass{border-color:var(--green) !important;}
.nc-result-fail{border-color:var(--amber) !important;}
.nc-verdict-line{display:block;margin-top:6px;font-weight:700;}
.sd-code{display:inline-block;margin-left:6px;padding:1px 8px;border:1px solid var(--border);border-radius:999px;font:700 .72rem Inter,system-ui,sans-serif;letter-spacing:.05em;color:var(--teal);}
html[data-theme="dark"] .sd-code{color:#7fd6dd;}
.sd-aid{border:1px dashed var(--teal);border-radius:12px;background:var(--white);padding:12px 16px;margin:12px 0;}
.sd-aid ol{margin:6px 0 0;padding-left:22px;font-size:14.5px;line-height:1.6;color:var(--text);}
.sd-aid li{border-bottom:1px dotted var(--border);padding:4px 0;}
.sd-calc{border:1px solid var(--border);border-left:5px solid var(--green);border-radius:0 12px 12px 0;background:var(--green-soft);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
html[data-theme="dark"] .sd-calc{background:#14262a;}
.sd-calc .tc-lab{color:var(--green);}
html[data-theme="dark"] .sd-calc .tc-lab{color:#8fd6a8;}
@media print{.sd-aid,.sd-calc{break-inside:avoid;}}
@media (max-width:720px){.tc-sits{grid-template-columns:1fr;}}
@media print{.tc-sit,.tc-card,.tc-flow li{break-inside:avoid;}}
"""

DISCLAIMER = ("Educational self-study for registered nurses holding or preparing for a special dialysis portfolio. Does not replace "
              "physician orders, unit protocols, DOH and PhilHealth issuances, or supervised training and facility sign-off.")


import audit_acronym_expansion as AUD  # noqa: E402  (the site's first-use audit, so pages are generated compliant)

_SKIP_OPEN = re.compile(r"<(h[1-4]|button|summary|svg)\b", re.I)
_SKIP_CLOSE = re.compile(r"</(h[1-4]|button|summary|svg)>", re.I)


def tn_expand(body_html, page):
    """Expand each acronym at its first use in prose, judged exactly as audit_acronym_expansion.py judges it
    (headings are labels; link text, legends and table cells count as prose)."""
    def text_of(h):
        h = re.sub(r'<dl class="fig-abbrevs".*?</dl>', " ", h, flags=re.S)   # figure abbreviation lists are definitions, not prose
        return AUD.to_text(re.sub(r"<h[1-4]\b.*?</h[1-4]>", " ", h, flags=re.S))
    held = re.findall(r'<dl class="fig-abbrevs".*?</dl>', body_html, flags=re.S)   # never expand inside definitions
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
    """Add the subtrack's second style block and keep the shared nursing-course script."""
    return page.replace('<style id="nursing-course-style">', f'<style id="tn-course-style">{TN_CSS}</style>\n<style id="nursing-course-style">', 1)


def bar(label):
    return f"""<div class="container">
  <div class="nc-bar">
    <a href="renal-care-academy.html">Renal Care Academy</a><span class="nc-sep">›</span><a href="{PARENT}">Nephrology Nursing</a><span class="nc-sep">›</span><a href="{HUB}">{COURSE['title']}</a><span class="nc-sep">›</span><span>{label}</span>
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
    for qi, q in enumerate(items, 1):
        n_correct = sum(1 for o in q["options"] if o[1])
        if n_correct != 1:
            err(f"{label} question {qi}: {n_correct} options keyed correct (must be exactly 1)")
        if len(q["options"]) != 4:
            err(f"{label} question {qi}: expected 4 options")
        opts = []
        for oi, (text, correct, rat) in enumerate(q["options"]):
            oid = f"q{qi}{'abcd'[oi]}"
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if correct else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{text}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span><div class="nc-rat" hidden>{rat}</div></div>
    </div>""")
        g = f' data-group="{q.get("group", group)}"' if (group or q.get("group")) else ""
        if q.get("critical"):
            g += ' data-critical="1"'
        out.append(f"""  <fieldset class="nc-q" data-q="{qi}"{g}>
    <legend><span class="nc-qn">Question {qi} of {len(items)}</span>{q['stem']}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    return "\n".join(out)


CALC_COPY = {
    "calc-dialysis-nurse-portfolio-toolkit.html": ("Dialysis Nurse Portfolio Toolkit", "Honest rates with exclusions and a 95% range, infection rates by access type, treatment-delivery check (URR, minutes, UFR) and hemoglobin trend."),
    "calc-qapi-run-chart-spc.html": ("Run Chart and Statistical Process Control", "Plot a measure over time; find shifts, trends and special-cause signals."),
    "calc-qapi-cqi-toolkit.html": ("Quality Improvement Toolkit", "Aim statements, measures and improvement cycles."),
    "calc-qapi-meeting-wizard.html": ("QAPI Meeting Wizard", "Structure the monthly quality meeting so it ends in owned actions."),
    "calc-access-infection-rate.html": ("Access Infection Rate", "Infections per 1,000 catheter-days or per 100 patient-months, by access type."),
    "calc-access-intervention-burden.html": ("Access Intervention Burden", "Count procedures per access-year to see how much work an access needs."),
    "calc-iron-status-tsat.html": ("Iron Status and TSAT", "Transferrin saturation from serum iron and TIBC, read beside ferritin and inflammation."),
    "calc-dialysis-adequacy-ktv.html": ("Dialysis Adequacy (Kt/V and URR)", "Single-pool Kt/V by the Daugirdas formula and the urea reduction ratio."),
    "calc-ultrafiltration-rate.html": ("Ultrafiltration Rate", "Fluid removal per kilogram per hour from goal, weight and time."),
    "calc-ufr-ceiling.html": ("Ultrafiltration Rate Ceiling", "How much time a planned fluid removal needs to stay under a rate ceiling."),
    "calc-idwg-fluid.html": ("Interdialytic Weight Gain", "Weight gained between sessions as kilograms and percent of dry weight."),
    "calc-kfre.html": ("Kidney Failure Risk Equation", "Two- and five-year risk of kidney failure, used to time options teaching and referral."),
    "calc-dialysis-water-reuse.html": ("Dialysis Water Reuse", "Reverse osmosis reject water volumes and reuse options, for technical context."),
}


def calc_cards(files, label):
    cards = []
    for f in files:
        meta = N.page_meta(f)
        if not meta:
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
                   f'<img class="nc-fig-img" src="../images/{img}" alt="{html.escape(f["alt"])}" width="{w}" height="{h}" loading="lazy" decoding="async"></picture>'
                   f'<figcaption><p class="fig-desc">{f["desc"]}</p>{ab}</figcaption></figure>')
    return "\n".join(out)


def split_txt(m):
    a, b, c = m["split"]
    return f"{a:g} h study &middot; {b:g} h workshop &middot; {c:g} h supervised practice"


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
  <div class="section-tag">Learning objectives &middot; <span class="sd-code">{m['code']}</span> &middot; about {m['hours']:g} hours &middot; week {m['week']}</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
  <p><strong>Time plan.</strong> {split_txt(m)}. The supervised hours are arranged by your unit and recorded in its own competency system; this page records self-study only.</p>
</section>""")
    for s in m["sections"]:
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
  <div class="section-tag">Practice case &middot; synthetic</div>
  <h2>Case: {c['title']}</h2>
  <div class="nc-case">
{cites.render(c['html'].strip())}
  </div>
  <p>Before reading on, decide what you would assess, whom you would contact and what you would say, what you would teach, and what would make you escalate. Then compare with the debrief below.</p>
  <div class="nc-acte">
{acte}
  </div>
{outcome}  <div class="nc-task"><strong>Documentation task.</strong> {c['task']}</div>
  <div class="tn-round"><span class="tc-lab">Second round &middot; what changes</span>{rnd}<br><strong>Submit:</strong> {sub}</div>
</section>""")
    if len(m["quiz"]) < BANK_SIZE:
        err(f"module {mid}: question bank has {len(m['quiz'])} items (must be at least {BANK_SIZE})")
    for q in m["quiz"] + m["exam"]:
        cites.add(q.get("sources", []))
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Knowledge check</div>
  <h2>Check your understanding</h2>
  <p>Each visit draws {DRAW} questions at random from this module&rsquo;s {len(m['quiz'])}-question bank, in a shuffled order. Choose the single best answer for each, then select <strong>Check answers</strong>; a rationale appears under every option. Select <strong>New set of questions</strong> for a different mix. Nothing you select is sent anywhere; scoring happens in your browser and records self-study only.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="sd{mid}" data-draw="{DRAW}" novalidate>
{quiz_fieldsets(m['quiz'], f'module {mid}')}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
  <div class="nc-task"><strong>Reflect.</strong> {m['reflect']}</div>
</section>""")
    rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES if k in m["comps"])
    aid_name, aid_fields = m["job_aid"]
    aid = "\n".join(f"      <li>{x}</li>" for x in aid_fields)
    parts.append(f"""<section class="section" id="competencies">
  <div class="section-tag">Competencies, job aid and portfolio measure</div>
  <h2>What this module builds</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Code</th><th>The learner can</th><th>Course evidence</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
  <p><strong>Performance evidence for this module:</strong> {m['evidence_out']}</p>
  <div class="tn-crit"><strong>Critical error:</strong> {m['critical']}</div>
  <div class="sd-aid"><span class="tc-lab">Job aid &middot; blank training form</span><strong>{aid_name}</strong>
    <ol>
{aid}
    </ol>
    <p style="margin:8px 0 0;font-size:13.5px;color:var(--text-muted);">Print it or copy it into your unit&rsquo;s own form. Use it with fictional data here; real entries belong only in the facility&rsquo;s approved records.</p>
  </div>
  <p><strong>Portfolio measure.</strong> {m['metric']}</p>
</section>""")
    items = "\n".join(f"    <li>{x}</li>" for x in m["practice"]["items"])
    parts.append(f"""<section class="section" id="practice">
  <div class="section-tag">Supervised practice</div>
  <h2>With your preceptor</h2>
  <p>{m['practice']['intro']} These are prompts for supervised learning, not a procedure. Use your center&rsquo;s own protocols, contacts and forms; your preceptor observes and signs off each item on the facility&rsquo;s competency record.</p>
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
    for label, url in m.get("academy", []):
        rd.append(f'    <li><a href="{url}">{label}</a><span>Related Renal Care Academy module.</span></li>')
    for label, url in m.get("external", []):
        rd.append(f'    <li><a href="{url}" target="_blank" rel="noopener">{label}</a><span>Official source (external site).</span></li>')
    np = []
    if prev_m:
        np.append(f'<a class="nc-np" href="{prev_m["slug"]}.html"><small>← Previous &middot; Module {int(prev_m["id"])}</small>{prev_m["title"]}</a>')
    else:
        np.append(f'<a class="nc-np" href="{HUB}"><small>← Subtrack home</small>{COURSE["title"]}</a>')
    if next_m:
        np.append(f'<a class="nc-np nc-np-next" href="{next_m["slug"]}.html"><small>Next &middot; Module {int(next_m["id"])} →</small>{next_m["title"]}</a>')
    else:
        np.append(f'<a class="nc-np nc-np-next" href="{EXAM}"><small>Finish →</small>End-of-course knowledge check</a>')
    parts.append(f"""<section class="section" id="reading">
  <div class="section-tag">Assigned reading</div>
  <h2>Read next on this site</h2>
  <ul class="nc-read">
{chr(10).join(rd)}
  </ul>
{calc_cards(m.get('calcs', []), f'module {mid}')}
  <p>Back to the <a href="{HUB}">Special Dialysis Nurse Roles home</a> &middot; the <a href="{PARENT}">Hemodialysis Nurse core course</a>.</p>
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")

    main = tn_expand("\n\n".join(parts), fname)
    nav = [("objectives", "Objectives")] + [(s["id"], s["nav"]) for s in m["sections"]] + \
          [("case", "Case"), ("quiz", "Knowledge check"), ("competencies", "Competencies"), ("practice", "Supervised practice"), ("reading", "Reading")]
    cards = [(HUB, "Subtrack home", COURSE["long_title"], "Role chooser, syllabus, competencies, assessment and all fourteen modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], html.unescape(next_m["sub"]).split(",")[0] + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], html.unescape(prev_m["sub"]).split(",")[0] + "."))
    for f, why in m["readings"][:2]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Assigned reading", N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{m['title']}: Special Dialysis Nurse Roles Module {n}"
    page = N.shell(
        fname, title, m["desc"], m["keywords"], f"Nephrology Nursing &middot; Role &middot; Module {n}", m["title"], m["sub"],
        m.get("audience", "Registered nurses assigned a special portfolio in a hemodialysis unit &middot; preceptors &middot; nurse educators"),
        nav, bar(f"Module {n}"), main, N.glossary_block(main, m.get("terms", [])), N.related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": "Special Dialysis Nurse Roles (Renal Care Academy)", "url": f"{SITE}/guides/{COURSE['hub_slug']}"},
                      "learningResourceType": "Self-study module with worked scenarios, case and knowledge check",
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": m["slug"] + "-vignette-hero", "alt": m["image_alt"]}, disclaimer=DISCLAIMER,
    )
    (GUIDES / fname).write_text(finish(page), encoding="utf-8")
    return fname, cites.list()


# ───────────────────────── hub ─────────────────────────
TOOLKIT = "calc-dialysis-nurse-portfolio-toolkit.html"


def build_hub():
    cites = Cites("hub")
    cards = []
    for mid in ORDER:
        m = MODS[mid]
        cards.append(f"""    <a class="nc-mod" href="{m['slug']}.html" data-module="sd{mid}">
      <span class="nc-mod-top"><span class="nc-mod-step">Week {m['week']}</span><span>Module {int(mid)} &middot; {m['code']}</span><span class="nc-chip">{m['hours']:g} h</span><span class="nc-chip">{', '.join(m['comps']) if len(m['comps']) < 8 else 'S1–S8'}</span></span>
      <span class="nc-mod-title">{m['title']}</span>
      <span class="nc-mod-desc">{html.escape(html.unescape(m['sub']), quote=False)}</span>
      <span class="nc-mod-status" aria-live="off"></span>
    </a>""")
    sched = "\n".join(
        f"<tr><td>{m['week']}</td><td><a href=\"{m['slug']}.html\">{int(m['id'])}. {m['title']}</a></td><td>{m['code']}</td>"
        f"<td>{m['split'][0]:g}</td><td>{m['split'][1]:g}</td><td>{m['split'][2]:g}</td><td><strong>{m['hours']:g}</strong></td>"
        f"<td>{', '.join(m['comps']) if len(m['comps']) < 8 else 'S1–S8'}</td></tr>" for m in (MODS[x] for x in ORDER))
    tot = [sum(MODS[x]["split"][k] for x in ORDER) for k in range(3)]
    comp_rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES)
    def _mlinks(path):
        return "; ".join(f'<a href="{MODS[x]["slug"]}.html">Module {int(x)}</a>' for x in path)
    chooser = "\n".join(f'<tr><td>{who}</td><td>{_mlinks(path)}</td><td>{sum(MODS[x]["hours"] for x in path):g} h</td></tr>'
                        for who, path in C.PATHWAYS)
    src = "".join(f"[[{k}]]" for k in C.HUB_REFS)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>A role subtrack for the nurse who carries a portfolio</h2>
  <p>Most hemodialysis units ask one nurse to look after vascular access, another to watch infection control, another to teach new staff or keep the registry. The title varies by unit; the work is real. This subtrack prepares Philippine registered nurses (RN) for twelve of those portfolios, after a shared foundation module and before an integrated capstone. One nurse studies the portfolio she has been assigned; nobody is expected to hold all twelve.</p>
  <p>Each module follows the parent course&rsquo;s pattern: a plain-language picture, then the physiology or the system mechanism, then what the best evidence shows and how certain it is, then what the nurse actually does, with two or three worked scenarios from Philippine units. Every module has a practice case with a debrief and a harder second round, a 15-question knowledge check with a rationale for every option, a blank job aid, a portfolio measure, supervised-practice prompts, and links to this site&rsquo;s guides and calculators. The subtrack is free, needs no account, and sends nothing you answer to any server.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this subtrack is, and is not</h4>
      <p>It is self-study and simulation preparation for nurses already working in hemodialysis. Completing it does not appoint you to a role, grant clinical privileges or continuing professional development (CPD) credit, or create a recognized specialist qualification. None of the twelve portfolios is defined as a separate legally required post in the Philippine sources reviewed. Charge nurse and head nurse leadership are covered by their own tracks, not here.</p>
    </div>
  </div>
</section>

<section class="section" id="week">
  <div class="section-tag">What the work looks like</div>
  <h2>A week of portfolio work</h2>
{C.WEEK_HTML.strip()}
</section>

<section class="section" id="chooser">
  <div class="section-tag">Role chooser</div>
  <h2>Which modules should you study?</h2>
  <p>Prerequisites are advice, not locks: every page stays open. Hours include supervised practice arranged by your unit.</p>
  <div class="table-wrap"><table>
  <thead><tr><th>If you are</th><th>Study</th><th>About</th></tr></thead>
  <tbody>
{chooser}
  </tbody></table></div>
</section>

<section class="section" id="entry">
  <div class="section-tag">Before you begin</div>
  <h2>Entry preparation</h2>
  <p>Complete the <a href="{PARENT}">Hemodialysis Nurse core course</a> through <a href="{ENTRY}">Module 12</a>, or show equivalent knowledge; current Professional Regulation Commission (PRC) registration; current basic life support (BLS), and advanced cardiovascular life support (ACLS) where your unit assigns it. These are workplace checks, not website gates. A nurse without a practice placement can complete the reading and simulations but cannot claim observed workplace competence.</p>
  <p>For shift and unit leadership, see the <a href="dialysis-charge-nurse.html">Charge Nurse</a> and <a href="dialysis-head-nurse.html">Head Nurse</a> tracks. For the technical depth behind Module 12, see the <a href="water-treatment-technician.html">Water Treatment Technician</a> and <a href="dialysis-biomedical-technician.html">Biomedical Equipment Technician</a> tracks.</p>
</section>

<section class="section" id="crosswalk">
  <div class="section-tag">Philippine requirements</div>
  <h2>What the rules say, at the level they say it</h2>
  <p>Different sources carry different authority. Read each one in its own terms; never merge a station-based rule with a patient-based one, or treat society guidance as a license condition.</p>
{C.CROSSWALK_HTML.strip()}
</section>

<section class="section" id="modules">
  <div class="section-tag">The modules</div>
  <h2>Fourteen modules in seven weeks</h2>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
  <div class="nc-modgrid" id="nc-modules">
{chr(10).join(cards)}
  </div>
  <p style="margin-top:14px;"><strong>When you have finished:</strong> take the <a href="{EXAM}">end-of-course knowledge check</a>: fourteen questions, one from each module, drawn at random. The pass mark is {COURSE['pass_correct']} of {COURSE['exam_items']}, and every safety-critical question must be answered correctly.</p>
</section>

<section class="section" id="outcomes">
  <div class="section-tag">Exit competencies</div>
  <h2>What you will be able to do</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Code</th><th>The learner can</th><th>Evidence</th></tr></thead>
  <tbody>
{comp_rows}
  </tbody></table></div>
</section>

<section class="section" id="schedule">
  <div class="section-tag">Schedule</div>
  <h2>Syllabus and planned hours</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Week</th><th>Module</th><th>Code</th><th>Study</th><th>Workshop</th><th>Supervised</th><th>Total</th><th>Competencies</th></tr></thead>
  <tbody>
{sched}
  <tr><td></td><td><strong>Total (optional full subtrack)</strong></td><td></td><td><strong>{tot[0]:g}</strong></td><td><strong>{tot[1]:g}</strong></td><td><strong>{tot[2]:g}</strong></td><td><strong>{sum(tot):g}</strong></td><td></td></tr>
  </tbody></table></div>
  <p>Hours are Academy planning estimates, not statutory minima or contact-hour accreditation. Preceptors may extend supervised exposure until the skill is shown safely.</p>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>Three separate records</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Record</th><th>Requirement</th><th>Recorded by</th></tr></thead>
  <tbody>
  <tr><td>Self-study complete</td><td>Modules read and the <a href="{EXAM}">end-of-course knowledge check</a> passed: {COURSE['pass_correct']} of {COURSE['exam_items']} or better, with every safety-critical question correct.</td><td>The learner, here (optionally saved in this browser only)</td></tr>
  <tr><td>Simulation passed</td><td>The four <a href="{MODS['14']['slug']}.html#marking">capstone OSCE stations</a>: at least 32 of 40, at least 7 of 10 per station, no critical error.</td><td>The facilitator</td></tr>
  <tr><td>Facility competency</td><td>Portfolio skills observed and signed off at the locally required level.</td><td>The employing facility, in its authorized records</td></tr>
  </tbody></table></div>
  <p>A missed safety-critical question means more study even when the total is high. Educators making consequential decisions should use parallel versions of the check. Finishing the online flow never records simulation or workplace competency, and a self-ticked checklist never does either.</p>
</section>

<section class="section" id="calculators">
  <div class="section-tag">Tools</div>
  <h2>Calculators used in this subtrack</h2>
  <p>The <strong>Dialysis Nurse Portfolio Toolkit</strong> was built for this subtrack. It turns audit counts into honest percentages with a 95% range, calculates infection rates by access type, checks whether a treatment was delivered as prescribed (urea reduction ratio, minutes, ultrafiltration rate), and shows how fast hemoglobin is changing. It never suggests a dose. The others are existing site tools linked from the modules.</p>
{calc_cards([TOOLKIT, 'calc-qapi-run-chart-spc.html', 'calc-access-infection-rate.html', 'calc-iron-status-tsat.html', 'calc-dialysis-adequacy-ktv.html', 'calc-ultrafiltration-rate.html', 'calc-idwg-fluid.html', 'calc-kfre.html'], 'hub').replace('Calculators for this module', 'Calculators')}
</section>

<section class="section" id="sources">
  <div class="section-tag">Evidence and policy register</div>
  <h2>Sources behind this subtrack</h2>
  <p>Desk review dated 24 November 2026. Clinical content is reviewed at least annually; DOH orders, PhilHealth issuances (especially the 2026 kidney transplantation benefit circular, whose full operative text was not verified for this draft) and unit procedures must be checked before each use. Before release, the clinical content requires review by a Philippine nephrologist and an experienced dialysis nurse educator, with infection prevention, technical, pharmacy, records and transplant reviewers for their modules.{cites.render(src)}</p>
</section>"""
    main = tn_expand(main, HUB)
    nav = [("start", "Start here"), ("week", "A week of portfolio work"), ("chooser", "Role chooser"), ("entry", "Entry"), ("crosswalk", "Philippine rules"),
           ("modules", "Modules"), ("outcomes", "Competencies"), ("schedule", "Syllabus"), ("assessment", "Assessment"), ("calculators", "Calculators"), ("sources", "Sources")]
    related = [(PARENT, "Parent course", "Hemodialysis Nurse", "The core course this subtrack builds on."),
               ("dialysis-head-nurse.html", "By Role", "Head Nurse", "Unit leadership, staffing and the roster."),
               (MODS["01"]["slug"] + ".html", "Start", MODS["01"]["title"], "Module 1 of the subtrack."),
               (EXAM, "Knowledge check", "End-of-Course Knowledge Check", "Fourteen questions, one per module; pass at 12 with all safety-critical items correct.")]
    page = N.shell(
        HUB, "Special Dialysis Nurse Roles: Portfolio Training for Hemodialysis Nurses · Renal Care Academy",
        "A free Philippine-first Renal Care Academy subtrack for hemodialysis nurses who carry a special portfolio: vascular access, infection prevention, education, quality, safety, care coordination, anemia, transplant liaison, records and PhilHealth, water and equipment, and adequacy, with worked scenarios, knowledge checks and an OSCE capstone.",
        "dialysis nurse special roles, vascular access nurse coordinator Philippines, dialysis infection control nurse, dialysis nurse educator preceptor, anemia nurse, dialysis quality improvement nurse, renal care academy",
        "Nephrology Nursing &middot; Role", "Special Dialysis Nurse Roles",
        "Fourteen modules for the hemodialysis nurse who is handed a portfolio: the physiology and the system behind each role, what the evidence actually shows, worked scenarios from Philippine units, and exactly where nursing scope begins and ends.",
        "Philippine registered nurses assigned a special portfolio in a hemodialysis unit &middot; preceptors &middot; nurse educators &middot; head nurses",
        nav, bar("Subtrack home").replace(f'<span class="nc-sep">›</span><a href="{HUB}">{COURSE["title"]}</a><span class="nc-sep">›</span><span>Subtrack home</span>', f'<span class="nc-sep">›</span><span>{COURSE["title"]}</span>'),
        main, N.glossary_block(main, []), N.related_block(related),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": "Special-portfolio training for Philippine hemodialysis nurses.",
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE},
                      "hasPart": [{"@type": "LearningResource", "name": MODS[x]["title"], "url": f"{SITE}/guides/{MODS[x]['slug']}"} for x in ORDER],
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": IMG.HUB_ALT},
        disclaimer=DISCLAIMER,
    )
    (GUIDES / HUB).write_text(finish(page), encoding="utf-8")
    return HUB, cites.list()


# ───────────────────────── end-of-course knowledge check ─────────────────────────
def build_exam():
    cites = Cites("exam")
    items = []
    for mid in ORDER:
        for q in MODS[mid]["exam"]:
            items.append(dict(q, group=f"m{mid}"))
            cites.add(q.get("sources", []))
        if len(MODS[mid]["exam"]) < 2:
            err(f"module {mid}: needs at least 2 exam items for parallel versions")
    n_crit = sum(1 for q in items if q.get("critical"))
    main = f"""<section class="section" id="exam">
  <div class="section-tag">End-of-course knowledge check</div>
  <h2>Fourteen questions, one from each module</h2>
  <p>Each sitting draws one question at random from each of the fourteen modules (a pool of {len(items)} questions, {n_crit} of them marked safety-critical), in a shuffled order with shuffled options, so no two sittings are the same. Answer all fourteen, then select <strong>Check answers</strong>. To pass you need <strong>{COURSE['pass_correct']} of {COURSE['exam_items']}</strong> and <strong>every safety-critical question answered correctly</strong>. A rationale appears under every option.</p>
  <p>A pass marks your <strong>self-study as complete</strong>. It does not record simulation or workplace competency, which are assessed by a facilitator and your facility. If you do not pass, review the modules for the questions you missed, then select <strong>New set of questions</strong> for a parallel version.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="sd-final" data-draw="{COURSE['exam_items']}" data-stratify="1" data-pass="{COURSE['pass_correct']}" data-critical-pass="1" novalidate>
{quiz_fieldsets(items, 'exam')}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
</section>

<section class="section" id="next">
  <div class="section-tag">After the check</div>
  <h2>Next steps</h2>
  <p>Prepare for the facilitated <a href="{MODS['14']['slug']}.html">capstone OSCE</a> and arrange supervised portfolio exposure with your head nurse. Return to the <a href="{HUB}">subtrack home</a>.</p>
</section>"""
    main = tn_expand(main, EXAM)
    page = N.shell(
        EXAM, "End-of-Course Knowledge Check: Special Dialysis Nurse Roles · Renal Care Academy",
        "Fourteen-question end-of-course knowledge check for the Renal Care Academy Special Dialysis Nurse Roles subtrack, one question from each module; pass mark 12 of 14 with every safety-critical item correct.",
        "dialysis nurse special roles quiz, vascular access nurse exam, dialysis infection control nurse quiz, renal care academy knowledge check",
        "Nephrology Nursing &middot; Role", "End-of-Course Knowledge Check",
        "One question from each of the fourteen modules, drawn at random each sitting. Pass with 12 of 14 and every safety-critical question correct.",
        "Learners who have completed the Special Dialysis Nurse Roles modules",
        [("exam", "Knowledge check"), ("next", "Next steps")], bar("Knowledge check"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Subtrack home", COURSE["long_title"], "All modules and assessment details."),
                         (MODS["14"]["slug"] + ".html", "Capstone", MODS["14"]["title"], "The four-station OSCE.")]),
        jsonld_extra={"learningResourceType": "Quiz", "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": IMG.HUB_ALT},
        disclaimer=DISCLAIMER,
    )
    (GUIDES / EXAM).write_text(finish(page), encoding="utf-8")
    return EXAM, cites.list()


# ───────────────────────── entry links ─────────────────────────
MARK = ("<!-- SDNR-START -->", "<!-- SDNR-END -->")


def _strip(s):
    return re.sub(re.escape(MARK[0]) + r".*?" + re.escape(MARK[1]) + r"\n?", "", s, flags=re.S)


def wire_parent():
    """Idempotently link the subtrack from the parent hub (Specialty/role section), the core capstone module, and the
    Academy landing page (By Role column, after Head Nurse and Charge Nurse)."""
    done = []
    # Parent hub: the specialty/role card comes from tools/academy/nursing_specialties.py, rendered by the
    # Transplant Nurse generator's wire_parent(), so re-run it rather than inserting a second block here.
    r = subprocess.run([sys.executable, "-c", "import generate_transplant_nurse as T; print(T.wire_parent())"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0:
        done.append(PARENT + " (via transplant wire)")
    else:
        err(f"transplant wire_parent failed: {(r.stderr or r.stdout).strip()[-300:]}")
    p = ACADEMY / ENTRY
    if p.exists():
        s = _strip(p.read_text(encoding="utf-8"))
        block = f"""{MARK[0]}
<section class="section" id="special-roles">
  <div class="section-tag">Going further</div>
  <h2>Special Dialysis Nurse Roles</h2>
  <p>When your unit hands you a portfolio (access, infection prevention, teaching, quality, safety, coordination, anemia, transplant liaison, records, water and equipment, or adequacy), the Renal Care Academy&rsquo;s <a href="{HUB}">Special Dialysis Nurse Roles</a> subtrack prepares you for it. Start with <a href="{MODS['01']['slug']}.html">Module 1: {MODS['01']['title']}</a>.</p>
</section>
{MARK[1]}
"""
        anchor = '<section class="section" id="reading">'
        if anchor in s:
            s = s.replace(anchor, block + anchor, 1)
            p.write_text(s, encoding="utf-8")
            done.append(ENTRY)
        else:
            err(f"anchor not found in academy/{ENTRY}")
    idx = ACADEMY / "index.html"
    if idx.exists():
        s = _strip(idx.read_text(encoding="utf-8"))
        land = f"""{MARK[0]}
    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/{COURSE['hub_slug']}.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">
      <span class="tc-branch-body"><small>By Role &middot; portfolios</small><b>Special Dialysis Nurse Roles</b><span>For the hemodialysis nurse assigned a portfolio: vascular access, infection prevention, educator and preceptor, patient education, quality, safety and emergencies, care coordination, anemia, transplant liaison, records and PhilHealth, water and equipment, and adequacy.</span><span><strong>14 modules &middot; worked scenarios &middot; portfolio toolkit &middot; OSCE capstone</strong></span></span>
    </a>
{MARK[1]}
"""
        k = s.find('<div class="nn-col" id="nursing-role">')
        if k >= 0:
            end = s.find("\n    </div>\n  </div>", k)
            if end >= 0:
                s = s[:end + 1] + land + s[end + 1:]
                nav = f'{MARK[0]}\n    <a class="acad-track acad-subtrack" href="{HUB}"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="7" r="3"/><path d="M6 21a6 6 0 0 1 12 0"/><path d="M17 4l2-2M19 7h2"/></svg></span><span class="acad-track-t"><strong>Special Dialysis Nurse Roles</strong><small>14 modules</small></span></a>\n{MARK[1]}\n'
                a = s.find('    <a class="acad-track" href="dialysis-head-nurse.html">')
                if a >= 0:
                    e = s.find("\n", s.find("</a>", a)) + 1
                    s = s[:e] + nav + s[e:]
                idx.write_text(s, encoding="utf-8")
                done.append("index.html")
            else:
                err("academy/index.html: end of By Role column not found")
        else:
            err("academy/index.html: By Role column not found")
    return done


# ───────────────────────── Portfolio Toolkit calculator ─────────────────────────
CALC_REFS = ["perla2011", "patel2013", "hd2015", "daugirdas1993", "flythe2011", "anemia2026", "epo_label"]
CALC_PIPELINE = ["patch_published_time.py", "patch_reading_time.py", "REFS", "patch_hero_meta.py", "patch_share_title.py",
                 "patch_canonical_clean_urls.py", "patch_share_buttons.py", "patch_guide_rail.py", "add_calc_nav_pill.py",
                 "patch_calc_handoff.py", "patch_calc_english_only.py"]
CALC_CARD = """<a class="related-card" href="calc-dialysis-nurse-portfolio-toolkit.html">
<div class="related-card-tag">Dialysis Nursing · Quality</div>
<div class="related-card-title">Dialysis Nurse Portfolio Toolkit: Honest Rates, Infection Rates, Treatment Delivery &amp; Hemoglobin Trend</div>
<div class="related-card-desc">Audit percentages with a 95% range, infections by access type, URR, delivered minutes and UFR, and the pace of hemoglobin change.</div>
<div class="related-card-arrow">Open →</div></a>
"""


def build_calc():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "special_nurse_roles" / "build_calc_toolkit.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    idx = GUIDES / "calculators.html"
    s = idx.read_text(encoding="utf-8")
    if 'href="calc-dialysis-nurse-portfolio-toolkit.html"' not in s:
        for anchor in ('<a class="related-card has-thumb" href="calc-dialysis-adequacy-ktv.html">', '<a class="related-card" href="calc-dialysis-support-staff-toolkit.html">',
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
        cmd = ([PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", TOOLKIT]
               if step == "REFS" else [PY, step, "--guide", TOOLKIT])
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  ! {step} failed on {TOOLKIT}: {(r.stderr or r.stdout).strip()[-300:]}")
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


def check_content():
    """Extra checks: objective strings, critical items, unique stems."""
    stems = set()
    for mid in ORDER:
        m = MODS[mid]
        for q in m["quiz"] + m["exam"]:
            if q["stem"] in stems:
                err(f"module {mid}: duplicate stem: {q['stem'][:60]}")
            stems.add(q["stem"])
        if not any(q.get("critical") for q in m["exam"]):
            err(f"module {mid}: no safety-critical exam item")
        for k in ("job_aid", "metric", "case", "second_round", "practice", "readings", "evidence_out", "critical", "reflect"):
            if k not in m:
                err(f"module {mid}: missing {k}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--patch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", help="comma-separated page filenames to patch (with --patch)")
    ap.add_argument("--calc", action="store_true", help="(re)build the Portfolio Toolkit calculator and run its pipeline")
    ap.add_argument("--no-publish", action="store_true", help="leave the pages in guides/ (for batched --patch runs); publish later")
    ap.add_argument("--pipeline-only", help="comma-separated pages already in guides/: run the patch pipeline on them without rebuilding")
    ap.add_argument("--publish-only", action="store_true", help="only move already-patched pages to academy/ and wire the entry links")
    args = ap.parse_args()
    global GUIDES
    if args.pipeline_only:
        run_pipeline(args.pipeline_only.split(","))
        return
    if args.publish_only:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout or r.stderr).strip()[-800:])
        print("entry links:", wire_parent())
        return
    if args.check:
        import tempfile
        GUIDES = Path(tempfile.mkdtemp())
    check_content()
    calc_refs = build_calc() if (args.calc and not args.check) else None
    refs = {}
    for mid in ORDER:
        f, r = build_module(mid)
        refs[f] = r
    f, r = build_hub(); refs[f] = r
    f, r = build_exam(); refs[f] = r
    if calc_refs is not None:
        refs[TOOLKIT] = calc_refs
    elif (DATA / "refs-overrides.json").exists():
        old = json.loads((DATA / "refs-overrides.json").read_text(encoding="utf-8"))
        if TOOLKIT in old:
            refs[TOOLKIT] = old[TOOLKIT]
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
        files = sorted(f for f in refs if f != TOOLKIT) if not args.only else args.only.split(",")
        run_pipeline(files)
    if args.no_publish:
        print("pages left in guides/ (run with --publish-only when all batches are patched)")
        return
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip()[-800:])
    print("entry links:", wire_parent())
    if ERRORS:
        sys.exit(1)


if __name__ == "__main__":
    main()
