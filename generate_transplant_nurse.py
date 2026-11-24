#!/usr/bin/env python3
"""Generate the Transplant Nurse subtrack of the Renal Care Academy (Nephrology Nursing).

Pages: hub (transplant-nurse), 12 modules (transplant-nurse-NN-<slug>), end-of-course knowledge check
(transplant-nurse-final-exam). Content lives in tools/transplant_nurse/content/*.py (hand-edited).
The chrome (header, course CSS, quiz markup, glossary, related cards, dr-card) is imported from
generate_nursing_course.py so the subtrack looks and behaves like its parent course.

    python3 generate_transplant_nurse.py              # write pages to guides/, then publish to academy/
    python3 generate_transplant_nurse.py --patch      # also run the /setup-guide patch pipeline on each page
    python3 generate_transplant_nurse.py --check      # validate content only (refs, quiz keys, links)

Never hand-edit academy/transplant-nurse*.html: edit the content files and re-run.
An existing page's article:published_time is carried over, so re-running never re-dates a page.
"""
import argparse, html, importlib.util, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_nursing_course as N  # noqa: E402  (chrome, course CSS, helpers)

GUIDES = ROOT / "guides"
ACADEMY = ROOT / "academy"
CONTENT = ROOT / "tools" / "transplant_nurse" / "content"
DATA = ROOT / "data" / "transplant-nurse"
SITE = "https://renalcarematters.com"
ERRORS = []
BANK_SIZE, DRAW = 15, 5


def err(m):
    ERRORS.append(m)


def load(name):
    spec = importlib.util.spec_from_file_location(f"tn_{name}", CONTENT / f"{name}.py")
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
for mid, slug, title, short, week, hours, comps in C.MODULES:
    m = load(f"m{mid}").MODULE
    m.update(id=mid, slug=f"{COURSE['hub_slug']}-{mid}-{slug}", title=title, short=short, week=week, hours=hours, comps=comps)
    MODS[mid] = m
    ORDER.append(mid)

# ───────────────────────── references ─────────────────────────
def build_refs():
    raw = {}
    for p in (ROOT / "data" / "nursing-course" / "refs_pubmed_raw.json", DATA / "refs_pubmed_raw.json"):
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
/* Transplant Nurse subtrack: visual components (design tokens only, so dark mode holds). */
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
@media (max-width:720px){.tc-sits{grid-template-columns:1fr;}}
@media print{.tc-sit,.tc-card,.tc-flow li{break-inside:avoid;}}
"""

DISCLAIMER = ("Educational self-study for registered nurses. Does not replace physician orders, transplant program "
              "protocols, PhilHealth and DOH issuances, or supervised clinical training and facility sign-off.")


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
        out.append(f"""  <fieldset class="nc-q" data-q="{qi}"{g}>
    <legend><span class="nc-qn">Question {qi} of {len(items)}</span>{q['stem']}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    return "\n".join(out)


CALC_COPY = {
    "calc-tacrolimus-level-check.html": ("Tacrolimus Level Check", "Was it a true trough? Timing, concentration-to-dose ratio and variability across serial levels."),
    "calc-tacrolimus-dosing.html": ("Tacrolimus Dosing &amp; Target Trough", "Typical weight-based starting dose and target trough by time after transplant."),
    "calc-allograft-egfr-trend.html": ("Allograft Kidney Function Trend", "Slope of graft function between two dated results and projected time to a threshold."),
    "calc-drug-interaction-checker.html": ("Drug Interaction Checker", "Screen a medicine list for interactions before routing to the pharmacist."),
    "calc-transplant-prom.html": ("Transplant Adherence and Quality-of-Life Questionnaires", "Basel adherence scale, transplant quality of life, depression and anxiety screens."),
    "calc-donor-esrd-risk.html": ("Living Donor Eligibility and Long-Term Risk", "Eligibility screen and baseline risk of kidney failure for potential donors."),
    "calc-frailty-assessment.html": ("Frailty Assessment", "Structured frailty screen to identify low physiologic reserve."),
    "calc-kfre.html": ("Kidney Failure Risk Equation", "Two- and five-year risk of kidney failure, useful for timing transplant referral."),
    "calc-epts.html": ("Estimated Post-Transplant Survival Score", "United States candidate survival score, for comparison and teaching."),
    "calc-kdpi-kdri.html": ("Donor Kidney Quality Indices", "United States donor profile and risk indices, for comparison and teaching."),
    "calc-dgf-risk.html": ("Delayed Graft Function Risk", "Estimate the risk that a deceased-donor kidney will need early dialysis."),
    "calc-aki-staging.html": ("Acute Kidney Injury Staging", "Stage kidney injury from creatinine and urine output."),
    "calc-dengue-aki-risk.html": ("Dengue Kidney Injury Risk", "Risk of acute kidney injury in dengue."),
    "calc-leptospirosis-aki-risk.html": ("Leptospirosis Kidney Injury Risk", "Risk of acute kidney injury in leptospirosis."),
    "calc-qapi-cqi-toolkit.html": ("Quality Improvement Toolkit", "Aim statements, run charts and improvement cycles."),
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
  <div class="section-tag">Learning objectives &middot; about {m['hours']:g} hours &middot; week {m['week']}</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
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
    parts.append(f"""<section class="section" id="case">
  <div class="section-tag">Practice case &middot; synthetic</div>
  <h2>Case: {c['title']}</h2>
  <div class="nc-case">
{c['html'].strip()}
  </div>
  <p>Before reading on, decide what you would assess, whom you would contact and what you would say, what you would teach, and what would make you escalate. Then compare with the debrief below.</p>
  <div class="nc-acte">
{acte}
  </div>
  <div class="nc-task"><strong>Documentation task.</strong> {c['task']}</div>
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
  <form class="nc-quiz" id="nc-quiz" data-module="tn{mid}" data-draw="{DRAW}" novalidate>
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
    parts.append(f"""<section class="section" id="competencies">
  <div class="section-tag">Competencies</div>
  <h2>What this module builds</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Code</th><th>The learner can</th><th>Course evidence</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
  <p><strong>Performance evidence for this module:</strong> {m['evidence_out']}</p>
  <div class="tn-crit"><strong>Critical error:</strong> {m['critical']}</div>
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
  <p>Back to the <a href="{HUB}">Transplant Nurse subtrack home</a> &middot; the <a href="{PARENT}">Nephrology Nursing course</a> &middot; the entry lesson, <a href="{ENTRY}">Nephrology Nursing Module 11</a>.</p>
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")

    main = tn_expand("\n\n".join(parts), fname)
    nav = [("objectives", "Objectives")] + [(s["id"], s["nav"]) for s in m["sections"]] + \
          [("case", "Case"), ("quiz", "Knowledge check"), ("competencies", "Competencies"), ("practice", "Supervised practice"), ("reading", "Reading")]
    cards = [(HUB, "Subtrack home", COURSE["long_title"], "Syllabus, competencies, assessment and all twelve modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], html.unescape(next_m["sub"]).split(",")[0] + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], html.unescape(prev_m["sub"]).split(",")[0] + "."))
    for f, why in m["readings"][:2]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Assigned reading", N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{m['title']}: Transplant Nurse Module {n}"
    page = N.shell(
        fname, title, m["desc"], m["keywords"], f"Nephrology Nursing &middot; Specialization &middot; Module {n}", m["title"], m["sub"],
        "Registered nurses in kidney transplant ward and clinic work &middot; transplant coordinators &middot; nurse educators",
        nav, bar(f"Module {n}"), main, N.glossary_block(main, m.get("terms", [])), N.related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": "Transplant Nurse (Renal Care Academy)", "url": f"{SITE}/guides/{COURSE['hub_slug']}"},
                      "learningResourceType": "Self-study module with case and knowledge check",
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": m["slug"] + "-vignette-hero", "alt": m["image_alt"]}, disclaimer=DISCLAIMER,
    )
    (GUIDES / fname).write_text(finish(page), encoding="utf-8")
    return fname, cites.list()


# ───────────────────────── hub ─────────────────────────
def read_minutes(m):
    words = len(N.visible_text("".join(s["html"] for s in m["sections"]) + m["case"]["html"]).split())
    return max(10, round(words / 200 / 5) * 5)


def build_hub():
    cites = Cites("hub")
    cards = []
    for mid in ORDER:
        m = MODS[mid]
        cards.append(f"""    <a class="nc-mod" href="{m['slug']}.html" data-module="tn{mid}">
      <span class="nc-mod-top"><span class="nc-mod-step">Week {m['week']}</span><span>Module {int(mid)}</span><span class="nc-chip">{m['hours']:g} h</span><span class="nc-chip">{', '.join(m['comps']) if len(m['comps']) < 8 else 'K1–K8'}</span></span>
      <span class="nc-mod-title">{m['title']}</span>
      <span class="nc-mod-desc">{html.escape(html.unescape(m['sub']), quote=False)}</span>
      <span class="nc-mod-status" aria-live="off"></span>
    </a>""")
    sched = "\n".join(
        f"<tr><td>{m['week']}</td><td><a href=\"{m['slug']}.html\">TN{mid} {m['title']}</a></td><td>{m['hours']:g}</td>"
        f"<td>{', '.join(m['comps']) if len(m['comps']) < 8 else 'K1–K8'}</td><td>{m['evidence_out']}</td></tr>" for m in (MODS[x] for x in ORDER))
    comp_rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES)
    src = "".join(f"[[{k}]]" for k in C.HUB_REFS)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>A specialty subtrack for kidney transplant nursing</h2>
  <p>This subtrack prepares Philippine registered nurses (RN) for supervised work on a kidney transplant ward or in a transplant clinic, and orients them to recipient and living donor coordination. Adult recipient care is the main setting; living donors, deceased donation, adolescents, frail older adults and reproductive care are included. It builds on <a href="{ENTRY}">Module 11 of the Nephrology Nursing course</a>, which introduces transplantation, and goes much further: from referral timing and the immunology of compatibility, through the first postoperative hours, immunosuppression and drug levels, rejection and infection surveillance, to Philippine benefits, privacy and quality improvement.</p>
  <p>Each of the twelve modules follows the same pattern as the parent course: a plain-language mental model, then the physiology, then what the best evidence shows and how certain it is, then what the nurse actually does. Every module has a synthetic practice case with a debrief and a harder second round, a 15-question knowledge check with a rationale for every option, the competencies it builds, supervised-practice prompts, and links to this site&rsquo;s guides and calculators. The subtrack is free, needs no account, and sends nothing you answer to any server.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this subtrack is, and is not</h4>
      <p>It is self-study and simulation preparation. Completing it does not grant clinical privileges, continuing professional development (CPD) credit, or a recognized transplant qualification. Clinical competence is observed and signed off by your facility. Candidacy, listing, allocation, compatibility, dose changes and benefit decisions belong to the authorized transplant team, laboratory, PhilHealth and facility.</p>
    </div>
  </div>
</section>

<section class="section" id="entry">
  <div class="section-tag">Before you begin</div>
  <h2>Entry preparation</h2>
  <p>Complete <a href="{ENTRY}">Nephrology Nursing Module 11: Transplantation and Special Populations</a>, or show equivalent knowledge. Useful refreshers from the parent course are <a href="nephrology-nursing-01-kidney-function-renal-assessment.html">Module 1 (renal assessment)</a>, <a href="nephrology-nursing-04-aki-acute-kidney-support.html">Module 4 (acute kidney injury)</a>, <a href="nephrology-nursing-05-kidney-failure-treatment-choices.html">Module 5 (treatment choices)</a> and <a href="nephrology-nursing-17-teaching-evidence-based-practice.html">Module 17 (teaching)</a>. Facility placement requires verification of your current Professional Regulation Commission (PRC) registration and local orientation.</p>
  <p><strong>Delivery.</strong> Six weeks at two modules a week: about {COURSE['core_hours']} hours of reading, case work and assessed simulation, plus about {COURSE['supervised_hours']} hours of supervised clinical exposure arranged locally. Both allocations are Academy design choices; preceptors may extend exposure until skills are demonstrated safely.</p>
</section>

<section class="section" id="modules">
  <div class="section-tag">The modules</div>
  <h2>Twelve modules in six weeks</h2>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
  <div class="nc-modgrid" id="nc-modules">
{chr(10).join(cards)}
  </div>
  <p style="margin-top:14px;"><strong>When you have finished:</strong> take the <a href="{EXAM}">end-of-course knowledge check</a>, twelve questions, one from each module, drawn at random. The pass mark is {COURSE['pass_correct']} of {COURSE['exam_items']}.</p>
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
  <h2>Schedule and assessment blueprint</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Week</th><th>Module</th><th>Hours</th><th>Competencies</th><th>Required learner work</th></tr></thead>
  <tbody>
{sched}
  <tr><td></td><td><strong>Total</strong></td><td><strong>{sum(MODS[x]['hours'] for x in ORDER):g}</strong></td><td></td><td></td></tr>
  </tbody></table></div>
  <p><strong>Role emphasis during supervised placement.</strong> Ward and clinic nurses complete the whole core, with ward emphasis on Modules 5 to 8. Recipient coordinators emphasize Modules 1, 2, 4 and 9 to 11. Living donor staff emphasize Modules 3, 5 and 9. Dedicated deceased-donation staff need program-specific preparation and appointment. Learners practice simulated referral and handoff before workplace privileges are assigned.</p>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>Three separate records</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Record</th><th>Requirement</th><th>Recorded by</th></tr></thead>
  <tbody>
  <tr><td>Self-study complete</td><td>All modules read and the <a href="{EXAM}">end-of-course knowledge check</a> passed ({COURSE['pass_correct']} of {COURSE['exam_items']} or better).</td><td>The learner, here (optionally saved in this browser only)</td></tr>
  <tr><td>Simulation passed</td><td>All four <a href="{MODS['12']['slug']}.html#marking">capstone OSCE stations</a> passed: at least 32 of 40, at least 7 of 10 per station, no critical error.</td><td>The facilitator</td></tr>
  <tr><td>Facility competency</td><td>Supervised skills observed and signed off at the locally required level.</td><td>The employing facility, in its authorized records</td></tr>
  </tbody></table></div>
  <p>A failed knowledge check leads to targeted review and another practice attempt. Educators making consequential decisions should use parallel versions of the check. Finishing the online flow never records simulation or workplace competency.</p>
  <h3>Suggested supervised exposure</h3>
  <div class="table-wrap"><table>
  <thead><tr><th>Setting</th><th>Hours</th><th>Direct observation targets</th></tr></thead>
  <tbody>
  <tr><td>Recipient evaluation and waiting list</td><td>8</td><td>Checklist review, contact and transfusion escalation</td></tr>
  <tr><td>Living donor or donation pathway</td><td>4</td><td>Separate confidentiality workflow; simulated consent and escalation scenario</td></tr>
  <tr><td>Surgical ward and postoperative recovery</td><td>16</td><td>Handoff, focused assessment, trend documentation and emergency escalation</td></tr>
  <tr><td>Ambulatory follow-up and pharmacy</td><td>8</td><td>Reconciliation, trough workflow, teach-back and abnormal-result ownership</td></tr>
  <tr><td>Benefits, registry and quality</td><td>4</td><td>Current form selection, privacy and audit workflow</td></tr>
  </tbody></table></div>
  <p>Use simulation for rare and sensitive encounters. Obtain permission through normal facility procedures before observing. For each skill record the date, setting, behavior, degree of prompting, assessor initials and follow-up action, using the levels <em>observed</em>, <em>performed with prompts</em>, <em>performed safely under supervision</em>, or <em>facility-approved</em>. Keep patient-level records only in approved systems.</p>
</section>

<section class="section" id="worksheets">
  <div class="section-tag">For educators and preceptors</div>
  <h2>Localize before teaching, and reusable worksheets</h2>
  <p>The public lessons use generic workflows so that learners bring their own center&rsquo;s protocols to practice. Before teaching, record your facility&rsquo;s contacts and backup routes, ward observation and escalation policy, laboratory and drug-level procedures, biopsy observation policy, vaccine and prophylaxis pathways, donor privacy and ethics routes, waitlist authority, benefits contacts, authorized registry users and on-call coverage. Use them in every simulation.</p>
  <div class="tc-cards">
  <div class="tc-card"><b>Referral and escalation SBAR</b>Situation and acuity &middot; baseline and transplant stage &middot; observed trend with times &middot; relevant orders and medication timing &middot; requested decision &middot; receiving person and acknowledgment &middot; next check and owner.</div>
  <div class="tc-card"><b>Medicines and discharge</b>Verified agent and formulation &middot; ordered timing &middot; prescriber source &middot; refill date and supply plan &middot; lab date and timing &middot; teach-back &middot; emergency and backup contacts.</div>
  <div class="tc-card"><b>Benefits review</b>Pathway &middot; current source and date &middot; facility verified &middot; eligibility owner &middot; requirement &middot; present or missing &middot; next action, assignee and due date.</div>
  <div class="tc-card"><b>Quality charter</b>Population &middot; failure description &middot; numerator and denominator &middot; baseline and target &middot; change to test &middot; balancing measure &middot; responsible role and review date.</div>
  </div>
</section>

<section class="section" id="calculators">
  <div class="section-tag">Tools</div>
  <h2>Calculators used in this subtrack</h2>
  <p>The <strong>Tacrolimus Level Check</strong> was built for this subtrack: it tells you whether a sample was a true trough from the dose and draw times, computes the concentration-to-dose ratio, and calculates intrapatient variability from a series of levels. The others are existing site tools linked from the modules.</p>
{calc_cards(['calc-tacrolimus-level-check.html', 'calc-tacrolimus-dosing.html', 'calc-allograft-egfr-trend.html', 'calc-drug-interaction-checker.html', 'calc-transplant-prom.html', 'calc-donor-esrd-risk.html', 'calc-frailty-assessment.html', 'calc-kfre.html'], 'hub').replace('Calculators for this module', 'Calculators')}
</section>

<section class="section" id="careers">
  <div class="section-tag">Careers</div>
  <h2>Roles in the Philippines and abroad</h2>
  <p>In the Philippines, practice rests on current PRC registration under the Philippine Nursing Act, plus employer-specific training, experience and privileges; no separate national transplant-nurse credential was identified in the public sources reviewed. Typical roles are the ward transplant RN, the recipient coordinator, the living donor coordinator and, under designated program authority, the deceased donation coordinator. Abroad, treat registration, specialty certification and employer appointment as three separate steps. <a href="{MODS['12']['slug']}.html#careers">Module 12</a> sets out Philippine and international examples with sources.</p>
</section>

<section class="section" id="sources">
  <div class="section-tag">Evidence and policy register</div>
  <h2>Sources behind this subtrack</h2>
  <p>Desk review dated 24 November 2026. Clinical recommendations are reviewed at least annually; PhilHealth issuances, forms, contracting status and center procedures must be verified before each use. Before release, the clinical content requires review by a transplant nurse educator and a transplant nephrologist, and the Philippine benefits and regulatory content by a benefits or regulatory lead.{cites.render(src)}</p>
</section>"""
    main = tn_expand(main, HUB)
    nav = [("start", "Start here"), ("entry", "Entry"), ("modules", "Modules"), ("outcomes", "Competencies"), ("schedule", "Schedule"),
           ("assessment", "Assessment"), ("worksheets", "For educators"), ("calculators", "Calculators"), ("careers", "Careers"), ("sources", "Sources")]
    related = [(PARENT, "Parent course", "Nephrology Nursing &amp; Hemodialysis", "The 17-module course this subtrack builds on."),
               (ENTRY, "Entry lesson", "Module 11: Transplantation and Special Populations", "The introductory transplant module."),
               (MODS["01"]["slug"] + ".html", "Start", MODS["01"]["title"], "Module 1 of the subtrack."),
               (EXAM, "Knowledge check", "End-of-Course Knowledge Check", "Twelve questions, one per module; pass at 10.")]
    page = N.shell(
        HUB, "Transplant Nurse: Kidney Transplant Nursing Subtrack · Renal Care Academy",
        "A free Philippine-first kidney transplant nursing subtrack of the Renal Care Academy: 12 modules on referral, compatibility, living and deceased donation, perioperative care, immunosuppression, rejection, infection, follow-up, PhilHealth and quality, with cases, knowledge checks and an OSCE capstone.",
        "kidney transplant nursing course Philippines, transplant nurse training, transplant coordinator course, renal care academy, nephrology nursing transplant",
        "Nephrology Nursing &middot; Specialization", "Transplant Nurse",
        "Twelve modules that take a registered nurse from the transplant referral to lifelong follow-up: the physiology behind every task, what the latest evidence shows, and exactly where nursing scope begins and ends.",
        "Philippine registered nurses entering kidney transplant ward or clinic work &middot; transplant coordinators &middot; educators",
        nav, bar("Subtrack home").replace(f'<span class="nc-sep">›</span><a href="{HUB}">{COURSE["title"]}</a><span class="nc-sep">›</span><span>Subtrack home</span>', f'<span class="nc-sep">›</span><span>{COURSE["title"]}</span>'),
        main, N.glossary_block(main, []), N.related_block(related),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": "Kidney transplant nursing subtrack for Philippine registered nurses.",
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE},
                      "hasPart": [{"@type": "LearningResource", "name": MODS[x]["title"], "url": f"{SITE}/guides/{MODS[x]['slug']}"} for x in ORDER],
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "A Filipino transplant nurse reviewing a recipient's medicine schedule with him and his wife at a clinic table."},
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
    main = f"""<section class="section" id="exam">
  <div class="section-tag">End-of-course knowledge check</div>
  <h2>Twelve questions, one from each module</h2>
  <p>Each sitting draws one question at random from each of the twelve modules (a pool of {len(items)} questions), in a shuffled order with shuffled options, so no two sittings are the same. Answer all twelve, then select <strong>Check answers</strong>. The pass mark is <strong>{COURSE['pass_correct']} of {COURSE['exam_items']}</strong>. A rationale appears under every option.</p>
  <p>A pass marks your <strong>self-study as complete</strong>. It does not record simulation or workplace competency, which are assessed by a facilitator and your facility. If you do not pass, review the modules for the questions you missed, then select <strong>New set of questions</strong> for a parallel version.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="tn-final" data-draw="{COURSE['exam_items']}" data-stratify="1" data-pass="{COURSE['pass_correct']}" novalidate>
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
  <p>Prepare for the facilitated <a href="{MODS['12']['slug']}.html">capstone OSCE</a> and arrange the suggested supervised exposure with your nurse manager. Return to the <a href="{HUB}">subtrack home</a>.</p>
</section>"""
    main = tn_expand(main, EXAM)
    page = N.shell(
        EXAM, "End-of-Course Knowledge Check: Transplant Nurse · Renal Care Academy",
        "Twelve-question end-of-course knowledge check for the Renal Care Academy Transplant Nurse subtrack, one question drawn from each module, pass mark 10 of 12, with rationales.",
        "kidney transplant nursing quiz, transplant nurse exam, renal care academy knowledge check",
        "Nephrology Nursing &middot; Specialization", "End-of-Course Knowledge Check",
        "One question from each of the twelve modules, drawn at random each sitting. Pass with 10 of 12.",
        "Learners who have completed the twelve Transplant Nurse modules",
        [("exam", "Knowledge check"), ("next", "Next steps")], bar("Knowledge check"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Subtrack home", COURSE["long_title"], "All modules and assessment details."),
                         (MODS["12"]["slug"] + ".html", "Capstone", MODS["12"]["title"], "The four-station OSCE.")]),
        jsonld_extra={"learningResourceType": "Quiz", "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "A transplant nurse at a desk completing a knowledge check on a laptop."},
        disclaimer=DISCLAIMER,
    )
    (GUIDES / EXAM).write_text(finish(page), encoding="utf-8")
    return EXAM, cites.list()


# ───────────────────────── entry links on the parent course ─────────────────────────
ENTRY_MARK = ("<!-- TN-SUBTRACK-START -->", "<!-- TN-SUBTRACK-END -->")


def _other_specialty_cards():
    """Cards for the other Nephrology Nursing subtracks (tools/academy/nursing_specialties.py)."""
    import importlib.util
    p = ROOT / "tools" / "academy" / "nursing_specialties.py"
    if not p.exists():
        return ""
    spec = importlib.util.spec_from_file_location("_nursing_specialties", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.cards_html()


def entry_blocks():
    m11 = f"""{ENTRY_MARK[0]}
<section class="section" id="transplant-nurse">
  <div class="section-tag">Going further</div>
  <h2>The Transplant Nurse subtrack</h2>
  <p>This module is the entry lesson for the Renal Care Academy&rsquo;s <a href="{HUB}">Transplant Nurse subtrack</a>: twelve modules on referral, compatibility, living and deceased donation, perioperative care, immunosuppression and drug levels, rejection, infection, long-term follow-up, PhilHealth benefits and privacy, quality, and a four-station simulation capstone. Start with <a href="{MODS['01']['slug']}.html">Module 1: {MODS['01']['title']}</a>.</p>
</section>
{ENTRY_MARK[1]}
"""
    hub = f"""{ENTRY_MARK[0]}
<section class="section" id="specialty">
  <div class="section-tag">Specialty subtracks</div>
  <h2>Go deeper after the core</h2>
  <div class="nc-modgrid">
{_other_specialty_cards()}    <a class="nc-mod" href="{HUB}">
      <span class="nc-mod-top"><span class="nc-mod-step">Specialty</span><span>12 modules &middot; about {COURSE['core_hours']} hours</span></span>
      <span class="nc-mod-title">Transplant Nurse</span>
      <span class="nc-mod-desc">Kidney transplant ward and clinic nursing, from referral and compatibility to immunosuppression, rejection and infection surveillance, PhilHealth benefits and a simulation capstone. Entry lesson: Module 11.</span>
    </a>
  </div>
</section>
{ENTRY_MARK[1]}
"""
    landing = f"""{ENTRY_MARK[0]}
    <a class="tc-branch" href="{HUB}">
      <span class="tc-branch-body"><small>Specialty subtrack &middot; registered nurses</small><b>Transplant Nurse</b><span>Kidney transplant ward and clinic nursing: referral, compatibility, living and deceased donation, perioperative care, immunosuppression, rejection and infection surveillance, PhilHealth benefits and privacy, quality, and a simulation capstone. Part of Nephrology Nursing.</span><span><strong>12 modules &middot; knowledge check &middot; OSCE capstone</strong></span></span>
    </a>
{ENTRY_MARK[1]}
"""
    return m11, hub, landing


def wire_parent():
    """Idempotently add the two entry links (Module 11 and a specialty card on the parent hub) in academy/.
    The same blocks are produced by generate_nursing_course.py (SPECIALTY hook) when the parent course is regenerated."""
    m11, hub, landing = entry_blocks()
    done = []
    for fname, block, anchor in ((ENTRY, m11, '<section class="section" id="case">'),
                                 (PARENT, hub, '<section class="section" id="progression">')):
        p = ACADEMY / fname
        if not p.exists():
            err(f"parent page missing: academy/{fname}")
            continue
        s = p.read_text(encoding="utf-8")
        s = re.sub(re.escape(ENTRY_MARK[0]) + r".*?" + re.escape(ENTRY_MARK[1]) + r"\n?", "", s, flags=re.S)
        if anchor not in s:
            err(f"anchor not found in academy/{fname}: {anchor}")
            continue
        s = s.replace(anchor, block + anchor, 1)
        if fname == ENTRY and 'href="#transplant-nurse"' not in s:
            s = s.replace('<a class="nav-pill" href="#case">', '<a class="nav-pill" href="#transplant-nurse">Transplant Nurse subtrack</a>\n<a class="nav-pill" href="#case">', 1)
        if fname == PARENT and 'href="#specialty"' not in s:
            s = s.replace('<a class="nav-pill" href="#progression">', '<a class="nav-pill" href="#specialty">Specialty subtracks</a>\n<a class="nav-pill" href="#progression">', 1)
        p.write_text(s, encoding="utf-8")
        done.append(fname)
    # Academy landing page: Transplant Nurse shown as a subtrack nested under the Nephrology Nursing card
    spec = importlib.util.spec_from_file_location("tn_landing", ROOT / "tools" / "transplant_nurse" / "landing.py")
    L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    r = L.wire(ACADEMY / "index.html")
    if r == "ok":
        done.append("index.html")
    else:
        err(f"academy/index.html: {r}")
    return done


# ───────────────────────── Tacrolimus Level Check calculator ─────────────────────────
CALC = "calc-tacrolimus-level-check.html"
CALC_REFS = ["ekberg2007", "tholking2014", "shuker2015", "txrecip2009"]
CALC_PIPELINE = ["patch_published_time.py", "patch_reading_time.py", "REFS", "patch_hero_meta.py", "patch_share_title.py",
                 "patch_canonical_clean_urls.py", "patch_share_buttons.py", "patch_guide_rail.py", "add_calc_nav_pill.py",
                 "patch_calc_handoff.py", "patch_calc_english_only.py"]
CALC_CARD = """<a class="related-card" href="calc-tacrolimus-level-check.html">
<div class="related-card-tag">Tacrolimus · TDM</div>
<div class="related-card-title">Tacrolimus Level Check: Trough Timing, C/D Ratio &amp; Variability</div>
<div class="related-card-desc">Was it a true trough? Timing check, concentration-to-dose ratio and intrapatient variability from serial levels.</div>
<div class="related-card-arrow">Open →</div></a>
"""


def build_calc():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "transplant_nurse" / "build_calc_tac_level.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    idx = GUIDES / "calculators.html"
    s = idx.read_text(encoding="utf-8")
    if 'href="calc-tacrolimus-level-check.html"' not in s:
        anchor = '<a class="related-card has-thumb" href="calc-dgf-risk.html">'
        if anchor in s:
            idx.write_text(s.replace(anchor, CALC_CARD + anchor, 1), encoding="utf-8")
            print("added the calculator card to calculators.html")
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
    ap.add_argument("--calc", action="store_true", help="(re)build the Tacrolimus Level Check calculator and run its pipeline")
    args = ap.parse_args()
    global GUIDES
    if args.check:
        import tempfile
        GUIDES = Path(tempfile.mkdtemp())
    calc_refs = build_calc() if (args.calc and not args.check) else None
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
