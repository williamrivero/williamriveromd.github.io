#!/usr/bin/env python3
"""Renal Care Academy · Renal Patients and Care Partners (a patient and family track beside the staff tracks).

Pages (written to guides/, patched, then moved to academy/ by tools/academy/publish_academy.py):
  patients-care-partners.html                 course home with pathways and the module grid
  patients-care-partners-NN-<slug>.html       32 modules (NN 01-32; stable curriculum IDs C01-C12, K01-K03, H01-H04,
                                              P01-P03, T01-T03, S01-S02, A01-A03, F01-F02 are shown on each page)
  patients-care-partners-final-check.html     pathway-based final knowledge check (no certificate: deliberately not
                                              named *-final-exam.html, so apply_certificate.py leaves it alone)
  patients-care-partners-urgent-help.html     when to get urgent help (readable without onboarding)
  patients-care-partners-worksheets.html      23 printable A4 worksheets (blank; nothing is saved)
  patients-care-partners-facilitators.html    educator guide: teach-back record, referral form, capstone stations
Content: tools/patients_care_partners/content/ (curriculum.json is canonical; course.py, refs.py, distractors.py,
images.py, worksheets.json). Built from Blueprint v2.0 (November 28, 2026). Clinical content is a draft pending
Dr. Rivero's sign-off.

    python3 generate_patients_care_partners.py            # write pages, publish to academy/, wire the landing callout
    python3 generate_patients_care_partners.py --patch    # also run the /setup-guide patch pipeline on each page
    python3 generate_patients_care_partners.py --check    # validate content only
    python3 generate_patients_care_partners.py --calc     # (re)build guides/calc-patient-care-partner-toolkit.html

Never hand-edit academy/patients-care-partners*.html: edit the content files and re-run.
"""
import argparse, html, importlib.util, json, random, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_nursing_course as N  # noqa: E402  (site chrome, course CSS, helpers)
sys.path.insert(0, str(ROOT / "tools" / "academy"))
from tile_img import tile  # noqa: E402

GUIDES, ACADEMY = ROOT / "guides", ROOT / "academy"
CONTENT = ROOT / "tools" / "patients_care_partners" / "content"
DATA = ROOT / "data" / "patients-care-partners"
SITE = "https://renalcarematters.com"
ERRORS = []


def err(m):
    ERRORS.append(m)


def load(name):
    spec = importlib.util.spec_from_file_location(f"pcp_{name}", CONTENT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C = load("course")
REFS = load("refs").REFS
DIS = load("distractors").D
IMG = load("images")
CUR = json.loads((CONTENT / "curriculum.json").read_text(encoding="utf-8"))
WS = json.loads((CONTENT / "worksheets.json").read_text(encoding="utf-8"))
N.ABBR.update(C.ABBR)

HUB = C.HUB + ".html"
FINAL = C.HUB + "-final-check.html"
URGENT = C.HUB + "-urgent-help.html"
WORKSHEETS = C.HUB + "-worksheets.html"
FACIL = C.HUB + "-facilitators.html"
SRC = {s["id"]: s for s in CUR["sources"]}
PATHS = CUR["pathways"]

MODS, ORDER = {}, []
for i, raw in enumerate(CUR["modules"], 1):
    m = dict(raw)
    m["nn"] = f"{i:02d}"
    m["page"] = f"{C.HUB}-{m['nn']}-{m['slug']}"
    MODS[m["id"]] = m
    ORDER.append(m["id"])
CERT_LABEL = {"strong": "Strong evidence", "moderate": "Moderate evidence", "limited": "Limited evidence", "policy": "Policy fact (dated)"}
CERT_CLS = {"strong": "pcp-c-strong", "moderate": "pcp-c-mod", "limited": "pcp-c-lim", "policy": "pcp-c-pol"}


# ───────────────────────── citations ─────────────────────────
class Cites:
    def __init__(self, label):
        self.label, self.order = label, []

    def add(self, keys):
        for k in keys:
            k = k.lower()
            if k not in REFS:
                err(f"{self.label}: no APA reference for {k}")
            elif k not in self.order:
                self.order.append(k)

    def sup(self, keys):
        self.add(keys)
        ns = sorted(self.order.index(k.lower()) + 1 for k in keys if k.lower() in REFS)
        return "".join(f'<sup class="nc-cite"><a href="#ref-{n}" data-ref="{n}" aria-label="Reference {n}">{n}</a></sup>' for n in ns)

    def list(self):
        return [REFS[k] for k in self.order]


# ───────────────────────── CSS (second style block survives patch_master_css.py) ─────────────────────────
PCP_CSS = """
/* Renal Patients and Care Partners: visual components (design tokens only, so Dim, Dark and E-paper hold). */
.tc-lab{display:block;font:700 .72rem Inter,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:3px;}
html[data-theme="dark"] .tc-lab{color:#7fd6dd;}
.tc-plain{border-left:4px solid var(--teal);background:var(--teal-light);border-radius:0 12px 12px 0;padding:12px 16px;margin:14px 0;font-size:15.5px;line-height:1.65;color:var(--text);}
html[data-theme="dark"] .tc-plain{background:#0a2830;}
.tc-keyp{border:1px solid var(--green);border-radius:12px;background:var(--green-soft);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
html[data-theme="dark"] .tc-keyp{background:#1a2535;}
.tc-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin:14px 0;}
.tc-card{border:1px solid var(--border);border-left:4px solid var(--teal);border-radius:10px;background:var(--white);padding:10px 14px;font-size:14.5px;line-height:1.55;color:var(--text-mid);}
.tc-card b{display:block;color:var(--text);margin-bottom:2px;}
.pcp-urgent{display:flex;gap:12px;align-items:center;text-decoration:none;background:var(--red-soft);border:1px solid rgba(185,28,28,.25);border-left:5px solid var(--red);border-radius:12px;padding:10px 14px;margin:10px 0 0;color:var(--text);}
.pcp-urgent b{display:block;font:800 15.5px/1.25 Inter,system-ui,sans-serif;color:var(--red);}
.pcp-urgent span.t{display:block;font-size:14px;line-height:1.45;color:var(--text-mid);}
html[data-theme="dark"] .pcp-urgent b{color:#ff9b9b;}
.pcp-scene{border:1px solid var(--border);border-left:5px solid var(--amber);border-radius:0 12px 12px 0;background:var(--amber-soft);padding:12px 16px 10px;margin:14px 0;}
.pcp-scene .tc-lab{color:#7a4f00;}
.section .pcp-scene p{margin:0 0 8px;font-size:15.5px;line-height:1.65;color:var(--text);text-align:left;hyphens:manual;}
html[data-theme="dark"] .pcp-scene{background:#2a2216;border-color:#4a3c22;border-left-color:#d9a441;}
html[data-theme="dark"] .pcp-scene .tc-lab{color:#f2c46b;}
.pcp-cert{display:inline-block;margin-left:8px;padding:1px 9px;border-radius:999px;font:700 11px Inter,system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;border:1px solid currentColor;vertical-align:2px;}
.pcp-c-strong{color:var(--green);} .pcp-c-mod{color:var(--teal);} .pcp-c-lim{color:#8a5a00;} .pcp-c-pol{color:var(--purple,#4B3280);}
html[data-theme="dark"] .pcp-c-lim{color:#f2c46b;} html[data-theme="dark"] .pcp-c-pol{color:#b9a6ff;}
.pcp-ask{list-style:none;margin:10px 0;padding:0;display:grid;gap:8px;}
.pcp-ask li{border:1px dashed var(--border);border-radius:10px;padding:9px 12px 9px 40px;position:relative;background:var(--white);font-size:15px;line-height:1.5;color:var(--text);}
.pcp-ask li::before{content:"?";position:absolute;left:12px;top:8px;width:20px;height:20px;border-radius:50%;background:var(--teal);color:#fff;font:800 13px/20px Inter,system-ui,sans-serif;text-align:center;}
.pcp-paths{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin:14px 0;}
.pcp-path{display:block;text-decoration:none;border:1px solid var(--border);border-top:4px solid var(--teal);border-radius:12px;background:var(--white);padding:12px 14px;color:var(--text-mid);font-size:14.5px;line-height:1.5;}
.pcp-path b{display:block;color:var(--text);font-size:15.5px;margin-bottom:3px;}
.pcp-path small{display:block;margin-top:6px;color:var(--text-muted);font-weight:600;}
.pcp-path:hover{border-color:var(--teal);}
.pcp-crit-tag{display:inline-block;margin-left:6px;padding:0 7px;border-radius:999px;font:700 10.5px Inter,system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--red);border:1px solid var(--red);vertical-align:middle;}
html[data-theme="dark"] .pcp-crit-tag{color:#ff9b9b;border-color:#ff9b9b;}
.pcp-ws{border:1px solid var(--border);border-radius:12px;background:var(--white);padding:14px 18px;margin:16px 0;break-inside:avoid;}
.pcp-ws h3{margin:0 0 4px;}
.pcp-ws .pcp-line{border-bottom:1px solid var(--text-muted);height:34px;margin:2px 0 10px;}
.pcp-ws label{display:block;font-size:14.5px;font-weight:600;color:var(--text);margin-top:8px;}
.tc-part{margin:28px 0 6px;}
.pcp-chooser{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 14px;}
.pcp-chooser label{display:flex;gap:6px;align-items:center;border:1px solid var(--border);border-radius:999px;padding:6px 12px;background:var(--white);font-size:14.5px;cursor:pointer;}
.pcp-fq{border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin:12px 0;background:var(--white);}
.pcp-fq legend{font-weight:700;font-size:15.5px;line-height:1.45;color:var(--text);padding:0 4px;}
.pcp-fq label{display:flex;gap:8px;align-items:flex-start;margin:6px 0;font-size:15px;line-height:1.5;color:var(--text);}
.pcp-fq .pcp-why{margin-top:6px;font-size:14px;line-height:1.5;color:var(--text-mid);}
.pcp-fq.pcp-right{border-color:var(--green);} .pcp-fq.pcp-wrong{border-color:var(--amber);}
.pcp-result{border:2px solid var(--border);border-radius:12px;padding:12px 16px;margin:14px 0;font-size:15.5px;line-height:1.6;}
.pcp-result.pass{border-color:var(--green);} .pcp-result.notyet{border-color:var(--amber);}
@media (max-width:640px){.pcp-ws{padding:12px;}}
@media print{.pcp-urgent{display:block;}.nc-quiz,.pcp-chooser,.pcp-noprint{display:none !important;}.pcp-ws{border:1px solid #999;page-break-inside:avoid;}.pcp-ws + .pcp-ws{page-break-before:always;}}
"""


def finish(page):
    page = page.replace('<style id="nursing-course-style">', f'<style id="pcp-course-style">{PCP_CSS}</style>\n<style id="nursing-course-style">', 1)
    team = "nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero"
    if team in page:
        og = ROOT / "images" / "og" / f"{C.HUB}-og.jpg"
        fb = f"{SITE}/images/og/{og.name}" if og.exists() else f"{SITE}/images/og/academy/academy-index.jpg"
        page = re.sub(r"https://renalcarematters\.com/images/(?:og/)?" + team + r"\.(?:jpg|png)", fb, page)
    page = re.sub(r"<html([^>]*)>", lambda m: m.group(0) if "data-nc-store" in m.group(1) else f'<html{m.group(1)} data-nc-store="{C.STORE_KEY}">', page, count=1)
    return N.merge_cites(page)


def og_for(page, stem):
    """Point og:image / twitter:image at the share card images/og/<stem>-og.jpg (1200 x 630) when it exists."""
    og = ROOT / "images" / "og" / f"{stem}-og.jpg"
    if not og.exists():
        return page
    url = f"{SITE}/images/og/{og.name}"
    page = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*"', lambda m: m.group(1) + url + '"', page)
    if 'property="og:image:width"' not in page:
        page = page.replace(f'<meta property="og:image" content="{url}">',
                            f'<meta property="og:image" content="{url}">\n<meta property="og:image:width" content="1200">'
                            '\n<meta property="og:image:height" content="630">\n<meta property="og:image:type" content="image/jpeg">', 1)
    return page


def urgent_link():
    return (f'<a class="pcp-urgent" href="{URGENT}"><span aria-hidden="true" style="font-size:22px">&#128680;</span><span><b>When to get urgent help</b>'
            f'<span class="t">Severe breathlessness, chest pain, fainting, heavy bleeding, new confusion: get emergency help now. '
            f'No website or chat is watched in real time.</span></span></a>')


def bar(label, link_hub=True):
    crumbs = (f'<a href="renal-care-academy.html">Renal Care Academy</a><span class="nc-sep">›</span>'
              + (f'<a href="{HUB}">{C.TITLE}</a><span class="nc-sep">›</span><span>{label}</span>' if link_hub else f'<span>{C.TITLE}</span>'))
    return f"""<div class="container">
  <div class="nc-bar">
    {crumbs}
  </div>
  <div class="alert alert-teal">
    <div class="alert-icon">🤝</div>
    <div class="alert-body">
      <h4>For patients and care partners</h4>
      <p>{C.SCOPE_NOTE}</p>
    </div>
  </div>
  {urgent_link()}
</div>"""


import audit_acronym_expansion as AUD  # noqa: E402
_SKIP_OPEN = re.compile(r"<(h[1-4]|button|summary|svg|legend)\b", re.I)
_SKIP_CLOSE = re.compile(r"</(h[1-4]|button|summary|svg|legend)>", re.I)


def expand(body_html, page):
    """Expand each acronym at its first use in prose, judged as audit_acronym_expansion.py judges it."""
    def text_of(h):
        return AUD.to_text(re.sub(r"<h[1-4]\b.*?</h[1-4]>", " ", h, flags=re.S))
    acros = (AUD.GLOBAL_ACRONYMS | set(N.ABBR)) - AUD.EXEMPT
    for a in sorted(acros, key=lambda x: (-len(x), x)):
        r = AUD.first_use_expanded(text_of(body_html), a)
        if r is None or r:
            continue
        exp = N.ABBR.get(a, (None,))[0]
        if not exp:
            err(f"{page}: no expansion known for {a}")
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
            mm = pat.search(seg)
            if mm:
                parts[i] = seg[:mm.start()] + f"{exp}{mm.group(1)} ({a}{mm.group(1)})" + seg[mm.end():]
                done = True
        body_html = "".join(parts)
    return body_html


def esc(t):
    """Curriculum text is plain text: escape it, then restore curly quotes and dashes as entities."""
    t = html.escape(t, quote=False)
    return t.replace("’", "&rsquo;").replace("‘", "&lsquo;").replace("“", "&ldquo;").replace("”", "&rdquo;")


def para(t):
    return f"<p>{esc(t)}</p>"


# ───────────────────────── quiz ─────────────────────────
def options(q):
    """Four options: the curriculum's three (IDs a-c) plus the reviewed distractor (d). Graded by data-correct, not position."""
    opts = [(o["id"], o["text"]) for o in q["options"]]
    if q["id"] not in DIS:
        err(f"{q['id']}: no fourth option in distractors.py")
    else:
        opts.append(("d", DIS[q["id"]]))
    if len({t for _, t in opts}) != len(opts):
        err(f"{q['id']}: duplicate option text")
    return opts


def quiz_html(m):
    out = []
    for qi, q in enumerate(m["quiz"], 1):
        opts = []
        for oi, (oid_, text) in enumerate(options(q)):
            oid = f"q{qi}{'abcd'[oi]}"
            ok = oid_ == q["correctOptionId"]
            rat = f'<div class="nc-rat" hidden>{esc(q["rationale"])}</div>' if ok else ""
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if ok else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{esc(text)}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span>{rat}</div>
    </div>""")
        crit = ' data-critical="1"' if q["safetyCritical"] else ""
        tag = '<span class="pcp-crit-tag">Safety question</span>' if q["safetyCritical"] else ""
        out.append(f"""  <fieldset class="nc-q" data-q="{qi}"{crit}>
    <legend><span class="nc-qn">Question {qi} of {len(m['quiz'])}</span>{esc(q['stem'])}{tag}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    n = len(m["quiz"])
    return f"""  <form class="nc-quiz" id="nc-quiz" data-module="pcp{m['nn']}" data-draw="{n}" data-pass="{n - 1}" data-critical-pass novalidate>
{chr(10).join(out)}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>Shuffle and try again</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>"""


# ───────────────────────── figures, tools ─────────────────────────
def figure_html(code, section):
    """The module's teaching figures for one section (images/<hub>-NN-<key>.png/.webp, plan in image_plan.py)."""
    out = []
    for f in IMG.FIGURES:
        if f["code"] != code or f["section"] != section:
            continue
        stem = f"{C.HUB}-{MODS[code]['nn']}-{f['key']}"
        png, webp = ROOT / "images" / f"{stem}.png", ROOT / "images" / f"{stem}.webp"
        if not (png.exists() or webp.exists()):
            out.append(f"<!-- figure pending: images/{stem}.png -->")
            continue
        try:
            from PIL import Image
            with Image.open(png if png.exists() else webp) as im:
                w, h = im.size
        except Exception:
            w, h = (1672, 941)
        src = f'<source srcset="../images/{webp.name}" type="image/webp">' if webp.exists() else ""
        img = png.name if png.exists() else webp.name
        out.append(f'<figure class="nc-fig nc-fig-wide" id="fig-{stem[len(C.HUB) + 1:]}"><picture>{src}'
                   f'<img class="nc-fig-img" src="../images/{img}" alt="{html.escape(f["alt"])}" width="{w}" height="{h}" loading="lazy" decoding="async"></picture>'
                   f'<figcaption><p class="fig-desc"><b>{esc(f["caption"])}.</b> {esc(f["alt"])}</p></figcaption></figure>')
    return "\n".join(out)


CALC_COPY = {
    "CALC-RESULTS-TREND": ("My results trend log", "Type your dated eGFR or urine albumin results and see the trend to discuss with your team."),
    "CALC-SODIUM-LABEL": ("Food label sodium counter", "Multiply sodium per serving by servings eaten, and total a day of packaged foods."),
    "CALC-FLUID-LOG": ("My fluid counter", "Count drinks, soups and ice against the amount your own team gave you."),
    "CALC-IDWG": ("Between-session weight gain", "Kilograms gained since your last session, and the share of your target weight."),
    "CALC-HD-SESSIONS": ("PhilHealth hemodialysis session counter", "Sessions left of the 156 in a calendar year, and when they would run out."),
    "CALC-TX-DOSE-CLOCK": ("Transplant medicine clock and refill planner", "Your dose times on a clock, and the date to ask for a refill."),
    "CALC-MED-SCHEDULER": ("Medicine schedule builder (Med Scheduler)", "Build a printable daily schedule from your own prescription."),
}


def tool_cards(m):
    k = m["media"].get("calculator")
    if not k:
        return ""
    title, desc = CALC_COPY[k]
    if k == "CALC-MED-SCHEDULER":
        href = C.MED_SCHEDULER
    else:
        href = f"{C.TOOLKIT}#{C.CALC_ANCHOR[k]}"
        if not (GUIDES / C.TOOLKIT).exists():
            err(f"{m['id']}: toolkit page missing; run with --calc first")
    return f"""<div class="calc-cards-wrap">
  <div class="calc-cards-label">A tool for this module</div>
  <a href="{href}" class="calc-card">
    <div class="calc-card-icon">⌬</div>
    <div class="calc-card-body">
      <div class="calc-card-title">{title}</div>
      <div class="calc-card-desc">{desc} You type in your own team&rsquo;s numbers; the tool never sets a target, and nothing you type leaves your device.</div>
    </div>
    <span class="calc-card-arrow">Open →</span>
  </a>
</div>"""


# ───────────────────────── module page ─────────────────────────
def build_module(code):
    m = MODS[code]
    fname = m["page"] + ".html"
    cites = Cites(f"module {code}")
    i = ORDER.index(code)
    prev_m = MODS[ORDER[i - 1]] if i else None
    next_m = MODS[ORDER[i + 1]] if i < len(ORDER) - 1 else None
    path = m["pathway"]
    parts = []
    obj = "\n".join(f"    <li>{esc(o)}</li>" for o in m["objectives"])
    pre = ", ".join(MODS[p]["id"] for p in m["prerequisites"]) or "none"
    parts.append(f"""<section class="section" id="objectives">
  <div class="section-tag">Module {code} &middot; about {m['minutes']} minutes &middot; {C.PATH_LABEL[path]}</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
  <p style="font-size:14px;color:var(--text-muted)">Suggested earlier modules: {pre}. You may read any module in any order; the suggestion only helps the lessons build on each other.</p>
</section>""")
    parts.append(f"""<section class="section" id="picture">
  <div class="section-tag">Start here</div>
  <h2>The everyday picture</h2>
  <div class="tc-plain"><span class="tc-lab">In plain words</span>{esc(m['everydayPicture'])}</div>
{figure_html(code, "picture")}
</section>""")
    for li, les in enumerate(m["lessons"], 1):
        parts.append(f"""<section class="section" id="lesson-{li}">
  <div class="section-tag">Lesson {li} of 3</div>
  <h2>{esc(les['title'])}</h2>
{para(les['body'])}
{figure_html(code, f"lesson-{li}")}
</section>""")
    sit = m["realSituation"]
    parts.append(f"""<section class="section" id="situation">
  <div class="section-tag">A real situation &middot; fictional</div>
  <h2>{esc(sit['title'])}</h2>
  <div class="pcp-scene"><span class="tc-lab">What happened</span><p>{esc(sit['body'])}</p></div>
  <p><strong>Before reading on:</strong> what would you do, and whom would you call?</p>
  <div class="tc-keyp"><span class="tc-lab">What happened next, and why it matters</span>{esc(sit['debrief'])}</div>
</section>""")
    ev = m["whatResearchShows"]
    parts.append(f"""<section class="section" id="research">
  <div class="section-tag">What the research shows</div>
  <h2>How sure are we? <span class="pcp-cert {CERT_CLS[ev['certainty']]}">{CERT_LABEL[ev['certainty']]}</span></h2>
  <p>{esc(ev['text'])}{cites.sup(m['sourceIds'])}</p>
</section>""")
    asks = "\n".join(f"    <li>{esc(a)}</li>" for a in m["askYourTeam"])
    parts.append(f"""<section class="section" id="ask">
  <div class="section-tag">Bring to your next visit</div>
  <h2>Questions to ask your team</h2>
  <ul class="pcp-ask">
{asks}
  </ul>
{tool_cards(m)}
</section>""")
    ws = next((w for w in WS if w["id"] == m["worksheet"]), None)
    wlink = f' Worksheet <a href="{WORKSHEETS}#{m["worksheet"].lower()}">{m["worksheet"]}: {esc(ws["title"])}</a> is ready to print.' if ws else ""
    parts.append(f"""<section class="section" id="practice">
  <div class="section-tag">Practice and teach back</div>
  <h2>Try it, then say it in your own words</h2>
  <p><strong>Practice.</strong> {esc(m['activity'])}{wlink} Use invented details when practicing; keep your real health information on paper, not online.</p>
  <div class="tc-keyp"><span class="tc-lab">Teach back</span>{esc(m['teachBack'])} If a nurse educator is with you, they can record this on the <a href="{FACIL}#teach-back">teach-back record</a>. Reading and quizzes never count as a hands-on skill check.</div>
</section>""")
    n_crit = sum(1 for q in m["quiz"] if q["safetyCritical"])
    crit_note = (f" Questions marked <em>Safety question</em> ({n_crit} here) must be answered correctly before the module counts as complete; the explanation shows you why." if n_crit else "")
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Check your understanding</div>
  <h2>Three quick questions</h2>
  <p>Choose the best answer for each, then select <strong>Check answers</strong>. An explanation appears under the best answer. Try again as often as you like.{crit_note} Nothing you select is sent anywhere.</p>
{quiz_html(m)}
</section>""")
    rd = []
    for f, why in C.READINGS.get(code, []):
        meta = N.page_meta(f)
        if not meta:
            err(f"module {code}: reading not found: guides/{f}")
            continue
        rd.append(f'    <li><a href="{f}">{N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False)}</a><span>{why}</span></li>')
    np = [f'<a class="nc-np" href="{prev_m["page"]}.html"><small>← Previous &middot; {prev_m["id"]}</small>{esc(prev_m["title"])}</a>' if prev_m
          else f'<a class="nc-np" href="{HUB}"><small>← Course home</small>{C.TITLE}</a>',
          f'<a class="nc-np nc-np-next" href="{next_m["page"]}.html"><small>Next &middot; {next_m["id"]} →</small>{esc(next_m["title"])}</a>' if next_m
          else f'<a class="nc-np nc-np-next" href="{FINAL}"><small>Finish →</small>Final knowledge check</a>']
    rd_html = f"  <ul class=\"nc-read\">\n{chr(10).join(rd)}\n  </ul>" if rd else ""
    parts.append(f"""<section class="section" id="reading">
  <div class="section-tag">Keep going</div>
  <h2>Read next on this site</h2>
{rd_html}
  <p>Choose your own path on the <a href="{HUB}#pathways">course home</a>. Review status: {C.STATUS}. Last checked {C.REVIEW_HUMAN}.</p>
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")
    main = expand("\n\n".join(parts), fname)
    nav = [("objectives", "Goals"), ("picture", "Picture"), ("lesson-1", "Lesson 1"), ("lesson-2", "Lesson 2"), ("lesson-3", "Lesson 3"),
           ("situation", "Real situation"), ("research", "Research"), ("ask", "Ask your team"), ("practice", "Practice"),
           ("quiz", "Check"), ("reading", "Keep going")]
    cards = [(HUB, "Course home", C.TITLE, "All pathways and modules.")]
    if next_m:
        cards.append((next_m["page"] + ".html", "Next module", esc(next_m["title"]), esc(next_m["objectives"][0]) + "."))
    if prev_m:
        cards.append((prev_m["page"] + ".html", "Previous module", esc(prev_m["title"]), esc(prev_m["objectives"][0]) + "."))
    for f, why in C.READINGS.get(code, [])[:2]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Read next", N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    hero_stem, hero_alt = f"{m['page']}-vignette-hero", IMG.HERO_ALT[code]
    desc = f"Module {code} of the Renal Care Academy course for patients and care partners: {m['title']}. {m['objectives'][0]}."
    page = N.shell(
        fname, f"{m['title']}: Patients and Care Partners Module {code}", esc(desc)[:300],
        "kidney patient education Philippines, dialysis patient course, care partner training kidney, " + m["title"].lower(),
        f"{C.GROUP} &middot; {C.PATH_LABEL[path]} &middot; Module {code}", esc(m["title"]), esc(re.split(r"(?<=[.!?])\s", m["everydayPicture"], maxsplit=1)[0]),
        "People living with kidney disease and the people who support them",
        nav, bar(f"Module {code}"), main, N.glossary_block(main, []), N.related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": C.TITLE + " (Renal Care Academy)", "url": f"{SITE}/guides/{C.HUB}"},
                      "audience": {"@type": "PeopleAudience", "audienceType": "Patients and caregivers"},
                      "learningResourceType": "Patient education module", "lastReviewed": C.REVIEW_DATE},
        hero_img={"file": hero_stem, "alt": hero_alt}, disclaimer=C.DISCLAIMER,
    )
    page = og_for(page, m["page"])
    (GUIDES / fname).write_text(finish(page), encoding="utf-8")
    return fname, cites.list()


# ───────────────────────── course home ─────────────────────────
def path_modules(p):
    return list(dict.fromkeys(PATHS[p]["modules"]))


def build_hub():
    cites = Cites("hub")
    # pathways (path finder): educational choices only, no diagnosis
    pcards = []
    core_min = sum(MODS[x]["minutes"] for x in path_modules("core"))
    for p in C.PATH_ORDER:
        mods = path_modules(p)
        mins = sum(MODS[x]["minutes"] for x in mods) + (0 if p == "core" else core_min)
        tag = ("Everyone starts here" if p == "core" else f"Shared foundations + {', '.join(mods)}")
        pcards.append(f'<a class="pcp-path" href="#path-{p}"><b>{C.PATH_ICON[p]} {C.PATH_LABEL[p]}</b>{C.PATH_BLURB[p]}<small>{tag} &middot; about {mins // 60} h {mins % 60:02d} min</small></a>')
    grids = []
    seen = set()
    for p in C.PATH_ORDER:
        mods = [x for x in path_modules(p) if x not in seen] if p != "home-hd" else []
        note = ""
        if p == "home-hd":
            note = (f'<p>The home hemodialysis orientation uses the hemodialysis modules ({", ".join(path_modules("hd"))}) and '
                    f'<a href="{MODS["P03"]["page"]}.html">P03</a> for organizing a home routine. P03 is not a home hemodialysis technical module: '
                    'device-specific training and readiness are decided by an authorized program.</p>')
        cards = []
        for x in mods:
            m = MODS[x]
            seen.add(x)
            ncrit = sum(1 for q in m["quiz"] if q["safetyCritical"])
            cards.append(tile(f'    <a class="nc-mod" href="{m["page"]}.html" data-module="pcp{m["nn"]}">',
                              f"""      <span class="nc-mod-top"><span>{m['id']}</span><span class="nc-chip">{m['minutes']} min</span>{'<span class="nc-chip">Safety questions</span>' if ncrit else ''}</span>
      <span class="nc-mod-title">{esc(m['title'])}</span>
      <span class="nc-mod-desc">{esc(m['objectives'][0])}.</span>
      <span class="nc-mod-status" aria-live="off"></span>""", f"{C.HUB}-{m['nn']}"))
        grid = ('  <div class="nc-modgrid"' + (' id="nc-modules"' if p == "core" else "") + ">\n" + "\n".join(cards) + "\n  </div>") if cards else ""
        grids.append(f'  <h3 class="tc-part" id="path-{p}">{C.PATH_ICON[p]} {C.PATH_LABEL[p]}</h3>\n  <p>{C.PATH_BLURB[p]}</p>\n{note}{grid}')
    src_keys = ["s28", "s29", "s33", "s32", "s34", "s37", "s36", "s38", "s39", "s04", "s09", "s14", "s23", "s43"]
    srcs = cites.sup(src_keys)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>Understand your care, one short lesson at a time</h2>
  <p>This course is for people living with kidney disease and for the people who support them: a spouse, a son or daughter, a friend, a paid helper. Start with the shared foundations, then choose the pathway that fits your treatment or the person you support. Each module takes about 15 minutes: five minutes of reading, five of practice, and five explaining it back in your own words.</p>
  <p>Every module follows the same path. It opens with an everyday picture, shows where the picture stops being true, explains how the body really works, and only then gives the practical rule. A realistic Filipino situation shows the rule in action, and a short &ldquo;What the research shows&rdquo; box says honestly how strong the evidence is. You leave each module with questions to bring to your next visit.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this course is, and is not</h4>
      <p>{C.IS_NOT} {C.STATUS}.</p>
    </div>
  </div>
</section>

<section class="section" id="pathways">
  <div class="section-tag">Find my learning path</div>
  <h2>Choose the path that fits you</h2>
  <p>Choosing a path selects lessons, not treatment. It does not ask for your diagnosis, laboratory values or any identifier, and you can change it any time. Care partners add the pathway of the person they support. You can read any module, in any order, whenever you need it.</p>
  <div class="pcp-paths">
{chr(10).join(pcards)}
  </div>
</section>

<section class="section" id="modules">
  <div class="section-tag">Modules</div>
  <h2>{len(ORDER)} modules in nine pathways</h2>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
{chr(10).join(grids)}
</section>

<section class="section" id="how">
  <div class="section-tag">How each module works</div>
  <h2>The same steps every time</h2>
  <div class="tc-cards">
    <div class="tc-card"><b>1. The everyday picture</b>A familiar image, then where it stops being true.</div>
    <div class="tc-card"><b>2. Three short lessons</b>How the body works, then what to do.</div>
    <div class="tc-card"><b>3. A real situation</b>A fictional Filipino story with what happened next.</div>
    <div class="tc-card"><b>4. What the research shows</b>The evidence in plain words, with how sure we are.</div>
    <div class="tc-card"><b>5. Questions to ask your team</b>Bring them to your next visit.</div>
    <div class="tc-card"><b>6. Practice and teach back</b>A worksheet, then explain it in your own words.</div>
    <div class="tc-card"><b>7. Three quick questions</b>With explanations, as many tries as you like.</div>
  </div>
  <p>Every module page can be read aloud with the Listen button, highlighted and annotated on your own device, and saved for use with no signal in the Schola app. Ask for help with reading, hearing, eyesight or language; an educator can go through any module with you and check your answers out loud.</p>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Checking what you learned</div>
  <h2>Learning, not testing</h2>
  <p>Each module ends with three questions and explanations. When you have finished your pathway, the <a href="{FINAL}">final knowledge check</a> builds a set from the modules you studied: the first question of every shared-foundation module, every safety question from your pathway, and more questions up to 20 (it shows the real number when your path has more or fewer). It passes at 80 percent with every safety question correct; a missed safety question shows you the right answer and the reason. There is no time limit, and an educator may read the questions with you.</p>
  <p>Finishing gives you a printable <strong>self-reported learning summary</strong>, never a certificate or a qualification. Hands-on skills, such as peritoneal dialysis exchanges, are taught and checked only by your treatment team, on their own records.</p>
</section>

<section class="section" id="toolkit">
  <div class="section-tag">Take-home toolkit</div>
  <h2>Worksheets and tools</h2>
  <div class="tc-cards">
    <div class="tc-card"><b><a href="{WORKSHEETS}">23 printable worksheets</a></b>Goals and care team card, results questions, medicine list, meal plan, urgent help card, disruption plan, visit agenda and more. Print them blank; nothing is saved online.</div>
    <div class="tc-card"><b><a href="{C.TOOLKIT}">Patient and Care Partner Toolkit</a></b>Six small tools: results trend log, food label sodium counter, fluid counter, between-session weight gain, PhilHealth session counter, and a transplant medicine clock. You type your own team&rsquo;s numbers.</div>
    <div class="tc-card"><b><a href="{URGENT}">When to get urgent help</a></b>The warning signs and the 30-second call, on one page you can save for use with no signal.</div>
    <div class="tc-card"><b><a href="{FACIL}">For nurses and educators</a></b>How to run the course, teach-back records, a referral form for supervised training, and seven practice stations.</div>
  </div>
</section>

<section class="section" id="partners">
  <div class="section-tag">For care partners</div>
  <h2>Helping without taking over</h2>
  <p>A care partner is someone the patient chooses. The patient decides what you help with and what you may know; being family does not by itself give access to records. Start with the shared foundations, add the pathway of the person you support, then the three care-partner modules: <a href="{MODS['A01']['page']}.html">A01</a> on supporting choices, <a href="{MODS['A02']['page']}.html">A02</a> on organizing the practical load, and <a href="{MODS['A03']['page']}.html">A03</a> on looking after yourself. Helping with daily life never authorizes clinical procedures: any home dialysis task needs training and assessment by the home team.</p>
</section>

<section class="section" id="sources">
  <div class="section-tag">What the course is built on</div>
  <h2>Sources and review</h2>
  <p>The modules draw on international guidelines (KDIGO 2024, KDOQI vascular access 2019 and nutrition 2020, ISPD peritonitis 2022), large studies and systematic reviews (Global Burden of Disease 2023, DOPPS, Cochrane reviews of decision aids and of conservative care), surveillance data from the CDC, Philippine policy (PhilHealth circulars, the DOH dialysis licensing order), and patient resources from NIDDK and NICE.{srcs} Each module lists its own sources. Evidence was checked on November 28, 2026. PhilHealth amounts and dates change: confirm them with your facility. PhilHealth Circular 2026-0019 on transplants was published on November 21, 2026, with an expected effective date of December 6, 2026 calculated from its 15-day clause.</p>
  <p><strong>Review status.</strong> {C.STATUS}. Philippine CKD and dialysis counts quoted in the modules are press-reported and will be replaced with Philippine Renal Disease Registry figures when available. Translations into Filipino, Cebuano and Kapampangan are planned and will appear only after independent review.</p>
</section>"""
    main = expand(main, HUB)
    nav = [("start", "Start here"), ("pathways", "Find my path"), ("modules", "Modules"), ("how", "How it works"),
           ("assessment", "Checking learning"), ("toolkit", "Toolkit"), ("partners", "Care partners"), ("sources", "Sources")]
    related = [(MODS["C01"]["page"] + ".html", "Start", MODS["C01"]["title"], "Module C01: your goals and your care team."),
               (URGENT, "Urgent help", "When to Get Urgent Help", "Warning signs and the 30-second call."),
               (WORKSHEETS, "Worksheets", "Printable Patient Worksheets", "23 blank A4 forms for your visits."),
               (FINAL, "Final check", "Final Knowledge Check", "Built from the modules on your path.")]
    hero_stem, hero_alt = IMG.HUB_HERO, IMG.HERO_ALT["hub"]
    page = N.shell(
        HUB, "Renal Patients and Care Partners · Renal Care Academy",
        "A free course for people living with kidney disease and their care partners in the Philippines: 32 short modules in nine pathways on results, choices, medicines, food, fluid, infection, emergencies, PhilHealth, dialysis, transplant and conservative care.",
        "kidney patient education Philippines, dialysis patient course, CKD patient learning, care partner kidney course, caregiver dialysis training, PhilHealth hemodialysis patient guide, renal care academy patients",
        f"{C.GROUP} &middot; Course home", "Renal Patients and <em>Care Partners</em>",
        "Understand your care, prepare your questions, and build confidence one short lesson at a time. Start with shared foundations, then choose the pathway that fits your treatment or the person you support.",
        "People living with kidney disease, their families and care partners, and the nurses and educators who teach them",
        nav, bar("Course home", link_hub=False), main, N.glossary_block(main, []), N.related_block(related),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": "Patient and care-partner education in kidney care.",
                      "audience": {"@type": "PeopleAudience", "audienceType": "Patients and caregivers"},
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE},
                      "hasPart": [{"@type": "LearningResource", "name": MODS[x]["title"], "url": f"{SITE}/guides/{MODS[x]['page']}"} for x in ORDER],
                      "lastReviewed": C.REVIEW_DATE},
        hero_img={"file": hero_stem, "alt": hero_alt}, disclaimer=C.DISCLAIMER,
    )
    page = og_for(page, C.HUB)
    (GUIDES / HUB).write_text(finish(page), encoding="utf-8")
    return HUB, cites.list()


# ───────────────────────── final knowledge check ─────────────────────────
FINAL_JS = r"""
(function(){
  var D = JSON.parse(document.getElementById('pcp-final-data').textContent);
  var form = document.getElementById('pcp-final'), box = document.getElementById('pcp-final-qs'), res = document.getElementById('pcp-final-result');
  function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML;}
  function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
  function assigned(paths){var ids=D.paths.core.slice();paths.forEach(function(p){ids=ids.concat(D.paths[p]);});return ids.filter(function(x,i){return ids.indexOf(x)===i;});}
  var current=[];
  function build(){
    var paths=Array.prototype.map.call(form.querySelectorAll('input[name=path]:checked'),function(x){return x.value;});
    var ids=assigned(paths), pool=[], req=[];
    ids.forEach(function(mid){D.mods[mid].forEach(function(q,qi){pool.push(q);if((D.core.indexOf(mid)>=0&&qi===0)||q.c)req.push(q);});});
    var reqIds=req.map(function(q){return q.id;}), rest=shuffle(pool.filter(function(q){return reqIds.indexOf(q.id)<0;}));
    var n=Math.max(req.length,Math.min(20,pool.length));
    current=shuffle(req.concat(rest.slice(0,n-req.length)));
    box.innerHTML=current.map(function(q,i){
      var opts=shuffle(q.o.slice()).map(function(o){return '<label><input type="radio" name="'+q.id+'" value="'+o[0]+'"> <span>'+esc(o[1])+'</span></label>';}).join('');
      return '<fieldset class="pcp-fq" data-id="'+q.id+'"><legend>'+(i+1)+'. '+esc(q.s)+(q.c?' <span class="pcp-crit-tag">Safety question</span>':'')+' <small style="color:var(--text-muted)">('+q.m+')</small></legend>'+opts+'<div class="pcp-why" hidden></div></fieldset>';
    }).join('');
    document.getElementById('pcp-final-count').textContent=current.length+' questions from '+ids.length+' modules';
    form.querySelector('[data-grade]').hidden=false; res.innerHTML=''; res.className='pcp-result'; res.hidden=true;
    box.scrollIntoView({behavior:'smooth',block:'start'});
  }
  function grade(){
    if(!current.length)return;
    var right=0, critMiss=0, missed=[];
    current.forEach(function(q){
      var fs=box.querySelector('fieldset[data-id="'+q.id+'"]'), pick=fs.querySelector('input:checked'), ok=pick&&pick.value===q.k;
      fs.classList.toggle('pcp-right',!!ok); fs.classList.toggle('pcp-wrong',!ok);
      var w=fs.querySelector('.pcp-why'); w.hidden=false;
      w.innerHTML=(ok?'<strong>Right.</strong> ':'<strong>Best answer:</strong> '+esc(q.o.filter(function(o){return o[0]===q.k;})[0][1])+'. ')+esc(q.r);
      if(ok)right++; else {missed.push(q.m); if(q.c)critMiss++;}
    });
    var pct=Math.round(100*right/current.length), pass=pct>=80&&critMiss===0;
    res.hidden=false; res.className='pcp-result '+(pass?'pass':'notyet');
    res.innerHTML='<strong>'+right+' of '+current.length+' ('+pct+'%).</strong> '+(pass?'Passed: your self-study is complete for this path.':(critMiss?'Not yet: '+critMiss+' safety question'+(critMiss>1?'s':'')+' missed. Read the explanations above, review the module, then build a new set.':'Not yet: the pass mark is 80%. Review the modules below, then build a new set.'))+
      (missed.length?'<br>Modules to review: '+missed.filter(function(x,i){return missed.indexOf(x)===i;}).join(', ')+'.':'')+
      '<br><button type="button" class="nc-btn nc-btn-ghost pcp-noprint" id="pcp-summary">Print my self-reported learning summary</button>';
    document.getElementById('pcp-summary').onclick=function(){
      var w=window.open('','_blank'); if(!w)return;
      var paths=Array.prototype.map.call(form.querySelectorAll('input[name=path]:checked'),function(x){return x.parentNode.textContent.trim();});
      w.document.write('<html><head><title>Self-reported learning summary</title></head><body style="font-family:system-ui,sans-serif;max-width:720px;margin:24px auto;line-height:1.55"><h1 style="font-size:22px">Self-reported learning summary</h1><p><b>Self-reported educational completion. Not a certificate, qualification or treatment authorization.</b></p><p>Course: Renal Patients and Care Partners (Renal Care Academy)<br>Pathways: Shared foundations'+(paths.length?', '+esc(paths.join(', ')):'')+'<br>Final knowledge check: '+right+' of '+current.length+' ('+pct+'%) &middot; '+(pass?'passed':'not yet passed')+'<br>Date: '+new Date().toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'})+'</p><p>Name (optional): ______________________________</p><p>Educator teach-back review (optional): name ____________________ date __________</p><p style="font-size:12px;color:#555">Practical skills, including any home dialysis task, are assessed only by the treatment service on its own records. renalcarematters.com/academy</p></body></html>');
      w.document.close(); w.focus(); w.print();
    };
    res.scrollIntoView({behavior:'smooth',block:'center'});
  }
  form.querySelector('[data-build]').addEventListener('click',build);
  form.querySelector('[data-grade]').addEventListener('click',grade);
})();
"""


def build_final():
    data = {"core": path_modules("core"), "paths": {p: path_modules(p) for p in PATHS}, "mods": {}}
    for code in ORDER:
        m = MODS[code]
        data["mods"][code] = [{"id": q["id"], "m": code, "s": q["stem"], "c": q["safetyCritical"], "k": q["correctOptionId"],
                               "r": q["rationale"], "o": [[a, t] for a, t in options(q)]} for q in m["quiz"]]
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    chooser = "\n".join(f'    <label><input type="checkbox" name="path" value="{p}"> {C.PATH_ICON[p]} {C.PATH_LABEL[p]}</label>'
                        for p in C.PATH_ORDER if p != "core")
    main = f"""<section class="section" id="check">
  <div class="section-tag">Final knowledge check</div>
  <h2>Build a check from the modules you studied</h2>
  <p>Tick the pathways you studied (you may tick several, for example hemodialysis and transplant, or a care partner supporting someone on peritoneal dialysis). The shared foundations are always included. The check uses the first question of each shared-foundation module, every safety question from your modules, and more questions from your modules up to 20. If your path has more required questions than that, all of them are shown and the real number is displayed. No question is repeated, and no question comes from a pathway you did not choose.</p>
  <p>The pass mark is 80 percent with every safety question correct. There is no time limit. Nothing is sent anywhere, and nothing is stored after you close the page.</p>
  <form id="pcp-final" novalidate onsubmit="return false">
  <div class="pcp-chooser" role="group" aria-label="Pathways I studied">
{chooser}
  </div>
  <button type="button" class="nc-btn" data-build>Build my check</button>
  <p id="pcp-final-count" style="font-weight:700;margin:10px 0 0" aria-live="polite"></p>
  <div id="pcp-final-qs"></div>
  <button type="button" class="nc-btn" data-grade hidden>Check my answers</button>
  <div class="pcp-result" id="pcp-final-result" role="status" aria-live="polite" hidden></div>
  </form>
  <script type="application/json" id="pcp-final-data">{data_json}</script>
  <script>{FINAL_JS}</script>
</section>

<section class="section" id="after">
  <div class="section-tag">After the check</div>
  <h2>What a pass means</h2>
  <p>A pass means your self-study for that path is complete. It is not a certificate, a qualification or permission to do any treatment yourself. If you are on peritoneal dialysis or exploring home treatment, your home team trains you, watches you practice and decides when you are ready. Back to the <a href="{HUB}">course home</a>.</p>
</section>"""
    main = expand(main, FINAL)
    hero_stem, hero_alt = IMG.HUB_HERO, IMG.HERO_ALT["hub"]
    page = N.shell(
        FINAL, "Final Knowledge Check: Renal Patients and Care Partners · Renal Care Academy",
        "Build a final knowledge check from the modules on your own pathway: shared foundations plus hemodialysis, peritoneal dialysis, transplant, conservative care, care partner or family modules. Pass at 80% with every safety question correct.",
        "kidney patient quiz, dialysis patient knowledge check, care partner quiz, renal care academy patients",
        f"{C.GROUP} &middot; Final knowledge check", "Final Knowledge <em>Check</em>",
        "Choose your pathways, answer the questions, read the explanations. No time limit, no certificate: a self-reported learning summary you can print.",
        "Patients and care partners who finished their pathway", [("check", "Knowledge check"), ("after", "After the check")],
        bar("Final knowledge check"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Course home", C.TITLE, "All pathways and modules."), (URGENT, "Urgent help", "When to Get Urgent Help", "Warning signs and the 30-second call.")]),
        jsonld_extra={"learningResourceType": "Quiz", "lastReviewed": C.REVIEW_DATE},
        hero_img={"file": hero_stem, "alt": hero_alt}, disclaimer=C.DISCLAIMER,
    )
    (GUIDES / FINAL).write_text(finish(og_for(page, FINAL[:-5])), encoding="utf-8")
    return FINAL, []


# ───────────────────────── urgent help ─────────────────────────
def build_urgent():
    c08, h02, p02 = MODS["C08"], MODS["H02"], MODS["P02"]
    cites = Cites("urgent")
    main = f"""<section class="section" id="now">
  <div class="section-tag">Get emergency help now</div>
  <h2>These signs cannot wait for a clinic callback</h2>
  <ul class="nc-obj">
    <li>Severe or worsening breathlessness, or being unable to lie flat</li>
    <li>Chest pain or pressure</li>
    <li>Fainting or collapse</li>
    <li>New confusion, severe drowsiness, or trouble speaking</li>
    <li>New weakness of the face, an arm or a leg</li>
    <li>Heavy or spurting bleeding from a dialysis access that does not stop with firm pressure</li>
    <li>A seizure</li>
    <li>Thoughts of harming yourself, or feeling unable to stay safe</li>
  </ul>
  <p>In the dialysis unit, call staff at once. Outside the unit, use your local emergency service or go to the nearest emergency department. <strong>No website, quiz or chat is watched in real time.</strong></p>
</section>

<section class="section" id="call">
  <div class="section-tag">The 30-second call</div>
  <h2>Say four things</h2>
  <div class="tc-cards">
    <div class="tc-card"><b>Where</b>Your location, with a landmark.</div>
    <div class="tc-card"><b>What</b>What is happening, and when it started.</div>
    <div class="tc-card"><b>Kidney treatment</b>Hemodialysis, peritoneal dialysis, transplant, or kidney disease without dialysis.</div>
    <div class="tc-card"><b>Bleeding?</b>Whether there is active bleeding.</div>
  </div>
  <p>Bring the medicine and allergy list and the unit contact card if you can. Tell emergency staff that a fistula or graft arm should not be used for blood pressure or drips. Your own emergency numbers belong on the <a href="{WORKSHEETS}#w07">urgent help card (W07)</a>, filled in with your treatment team; this page never lists numbers because they differ by place.</p>
</section>

<section class="section" id="same-day">
  <div class="section-tag">Call your team the same day</div>
  <h2>Problems that need your team today</h2>
  <div class="tc-cards">
    <div class="tc-card"><b>Fistula or graft buzz changed or gone</b>Call the unit now, day or night. Clots are easier to treat early (<a href="{h02['page']}.html">H02</a>).</div>
    <div class="tc-card"><b>Cloudy peritoneal dialysis fluid</b>Call the PD team now, even if you feel fairly well, and keep the bag (<a href="{p02['page']}.html">P02</a>).</div>
    <div class="tc-card"><b>Redness, pus, fever or chills</b>At any access or exit site, or shaking chills during dialysis (<a href="{MODS['C07']['page']}.html">C07</a>).</div>
    <div class="tc-card"><b>A missed or delayed dialysis</b>Call the unit or backup unit and follow your written plan (<a href="{MODS['C11']['page']}.html">C11</a>).</div>
    <div class="tc-card"><b>Running out of anti-rejection medicine</b>Call the transplant team or pharmacist now (<a href="{MODS['T02']['page']}.html">T02</a>).</div>
  </div>
  <p>Learn more in <a href="{c08['page']}.html">Module C08: {esc(c08['title'])}</a>.</p>
</section>"""
    main = expand(main, URGENT)
    page = N.shell(
        URGENT, "When to Get Urgent Help: Kidney Patients and Care Partners · Renal Care Academy",
        "The warning signs that need emergency help now for people with kidney disease, on dialysis or with a transplant, the 30-second call, and the problems to report to your team the same day.",
        "dialysis emergency signs, kidney patient when to go to emergency, fistula no thrill, cloudy PD fluid, dialysis bleeding emergency",
        f"{C.GROUP} &middot; Urgent help", "When to Get <em>Urgent Help</em>",
        "Know the signs. Make the call. Then tell your kidney team.",
        "People living with kidney disease and their care partners", [("now", "Emergency now"), ("call", "The call"), ("same-day", "Same day")],
        bar("Urgent help"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Course home", C.TITLE, "All pathways and modules."), (c08["page"] + ".html", "Module C08", esc(c08["title"]), "The full lesson.")]),
        jsonld_extra={"lastReviewed": C.REVIEW_DATE}, hero_img=None, disclaimer=C.DISCLAIMER,
    )
    (GUIDES / URGENT).write_text(finish(og_for(page, URGENT[:-5])), encoding="utf-8")
    return URGENT, cites.list()


# ───────────────────────── worksheets ─────────────────────────
def build_worksheets():
    used = {}
    for code in ORDER:
        used.setdefault(MODS[code]["worksheet"], []).append(code)
    blocks = []
    for w in WS:
        fields = "".join(f'<label>{esc(f)}</label><div class="pcp-line"></div>' for f in w["fields"])
        mods = ", ".join(f'<a href="{MODS[c]["page"]}.html" class="pcp-noprint">{c}</a>' for c in used.get(w["id"], []))
        blocks.append(f'<div class="pcp-ws" id="{w["id"].lower()}"><h3>{w["id"]}. {esc(w["title"])}</h3>'
                      f'<p style="font-size:13.5px;color:var(--text-muted)">Used in: {mods or "the facilitator guide"} &middot; Fill in on paper with your care team. Do not post completed forms online.</p>{fields}'
                      f'<p style="font-size:12px;color:var(--text-muted)">Renal Care Academy &middot; Patients and Care Partners &middot; renalcarematters.com</p></div>')
    main = f"""<section class="section" id="how-to">
  <div class="section-tag">Printable worksheets</div>
  <h2>Print, write by hand, bring to your visit</h2>
  <p>These 23 forms go with the modules. Print the whole page (each form starts on a new A4 page) or one form at a time. They are blank on purpose: write your real details on paper with your care team, and keep completed forms private. Contact cards must be completed with your treatment service; this site never supplies local phone numbers.</p>
  <p class="pcp-noprint"><button type="button" class="nc-btn" onclick="window.print()">Print all worksheets</button></p>
</section>

<section class="section" id="forms">
  <div class="section-tag">The forms</div>
  <h2>Worksheets W01 to W23</h2>
{chr(10).join(blocks)}
</section>"""
    page = N.shell(
        WORKSHEETS, "Printable Patient Worksheets: Renal Patients and Care Partners · Renal Care Academy",
        "23 blank printable A4 worksheets for kidney patients and care partners: goals and care team, results questions, medicine list, meals, monitoring, urgent help card, benefits questions, disruption plan, visit agenda, dialysis day, transplant routine, support roster and more.",
        "kidney patient worksheet printable, dialysis medicine list template, care partner roster, kidney visit agenda",
        f"{C.GROUP} &middot; Worksheets", "Printable <em>Worksheets</em>",
        "Blank forms to complete on paper with your care team. Nothing is saved online.",
        "Patients, care partners and their educators", [("how-to", "How to use"), ("forms", "Worksheets")],
        bar("Worksheets"), main, N.glossary_block(main, []), N.related_block([(HUB, "Course home", C.TITLE, "All pathways and modules.")]),
        jsonld_extra={"lastReviewed": C.REVIEW_DATE}, hero_img=None, disclaimer=C.DISCLAIMER,
    )
    (GUIDES / WORKSHEETS).write_text(finish(og_for(page, WORKSHEETS[:-5])), encoding="utf-8")
    return WORKSHEETS, []


# ───────────────────────── facilitators ─────────────────────────
def build_facilitators():
    cites = Cites("facilitators")
    rows = "\n".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in C.STATIONS)
    tb = "\n".join(f"<tr><td>{MODS[x]['id']}</td><td>{esc(MODS[x]['teachBack'])}</td><td></td><td></td><td></td></tr>" for x in ORDER)
    main = f"""<section class="section" id="running">
  <div class="section-tag">For nurses and educators</div>
  <h2>Running the course with patients and families</h2>
  <p>The modules work chairside, in a clinic group, or at home with a family. A practical plan is four to six weeks, one or two short sessions several days a week. Start with a quick welcome session on the care-team card, infection and access (C07) and urgent help (C08), then let each person continue at their own pace. Avoid long screen time during a tiring treatment. Offer to read aloud, check answers orally, and use the Listen button for people with low vision or low literacy. Never label anyone &ldquo;noncompliant&rdquo;; find the barrier instead.</p>
  <p>Before teaching, localize: your unit&rsquo;s contact numbers and after-hours route, written emergency instructions for bleeding and other treatment-specific problems, the backup unit, and your own fluid, food and medicine practices. Those individual numbers come from the treating team, never from the course.{cites.sup(['s32', 's17'])}</p>
</section>

<section class="section" id="teach-back">
  <div class="section-tag">Teach-back record</div>
  <h2>Educator teach-back record</h2>
  <p>Status for each module: <em>not assessed</em>, <em>needs support</em>, <em>demonstrated</em>, or <em>not applicable</em> with a reason. Online quiz results can never set a teach-back status.</p>
  <div class="table-wrap"><table class="pcp-record">
  <thead><tr><th>Module</th><th>Teach-back prompt</th><th>Status</th><th>Educator and date</th><th>Notes</th></tr></thead>
  <tbody>
{tb}
  </tbody></table></div>
</section>

<section class="section" id="referral">
  <div class="section-tag">Referral</div>
  <h2>Referral for supervised practical training</h2>
  <p>Use when a learner on peritoneal dialysis, exploring home hemodialysis, or with a new helper needs hands-on training. The treatment service keeps its own training and readiness records; this course never substitutes for them.</p>
  <div class="pcp-ws"><label>Learner (patient or care partner)</label><div class="pcp-line"></div><label>Treatment and equipment</label><div class="pcp-line"></div><label>Modules completed and teach-back status</label><div class="pcp-line"></div><label>Reason for referral (new treatment, new helper, after infection or hospital stay, equipment change, unsure)</label><div class="pcp-line"></div><label>Referred to (home team) and date</label><div class="pcp-line"></div><label>Educator</label><div class="pcp-line"></div></div>
</section>

<section class="section" id="stations">
  <div class="section-tag">Capstone practice</div>
  <h2>Seven practice stations</h2>
  <p>Use fictional cases. Judge the action and the explanation, not reading speed. A missed critical action means pause, explain, rehearse and reassess. The peritoneal dialysis station is for PD learners and their care partners only; others get an equivalent case from their own pathway.</p>
  <div class="table-wrap"><table>
  <thead><tr><th>Station</th><th>Prompt</th><th>Required actions</th><th>Critical miss</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
</section>"""
    main = expand(main, FACIL)
    page = N.shell(
        FACIL, "For Nurses and Educators: Renal Patients and Care Partners · Renal Care Academy",
        "How nurses and educators can run the Renal Care Academy course for patients and care partners: delivery plan, localization, teach-back record, referral for supervised practical training and seven capstone practice stations.",
        "patient education dialysis nurse educator, teach-back record kidney, dialysis patient education program",
        f"{C.GROUP} &middot; For educators", "For Nurses and <em>Educators</em>",
        "Run the course chairside, in groups or at home, keep a teach-back record, and refer for hands-on training.",
        "Renal nurse educators, dialysis nurses and patient educators", [("running", "Running it"), ("teach-back", "Teach-back record"), ("referral", "Referral"), ("stations", "Stations")],
        bar("For educators"), main, N.glossary_block(main, []), N.related_block([(HUB, "Course home", C.TITLE, "All pathways and modules.")]),
        jsonld_extra={"lastReviewed": C.REVIEW_DATE}, hero_img=None, disclaimer=C.DISCLAIMER,
    )
    (GUIDES / FACIL).write_text(finish(og_for(page, C.HUB)), encoding="utf-8")
    return FACIL, cites.list()


# ───────────────────────── checks, pipeline ─────────────────────────
def check():
    if len(ORDER) != 32:
        err(f"expected 32 modules, found {len(ORDER)}")
    qids = [q["id"] for c in ORDER for q in MODS[c]["quiz"]]
    if len(qids) != len(set(qids)):
        err("duplicate question IDs")
    for c in ORDER:
        m = MODS[c]
        for k in m["sourceIds"]:
            if k.lower() not in REFS:
                err(f"{c}: source {k} has no APA reference")
        if m["practicalEvidence"]["status"] != "not-assessed" or m["practicalEvidence"]["clinicalAuthorization"]:
            err(f"{c}: practical evidence must stay not-assessed")
        if m["worksheet"] not in {w["id"] for w in WS}:
            err(f"{c}: worksheet {m['worksheet']} not found")
        for q in m["quiz"]:
            if sum(1 for a, _ in options(q) if a == q["correctOptionId"]) != 1:
                err(f"{q['id']}: answer key does not match exactly one option")
    for f in IMG.FIGURES:
        if f["code"] not in MODS:
            err(f"images.py: {f['id']} names unknown module {f['code']}")
    banned = [r"\b\d+(\.\d+)?\s*(ml|mL|liters?)\s*(a|per)\s*day\b", r"\bmg/dL\b", r"\bmmol/L\b", r"\bmEq/L\b", r"\b\d{2,3}\s*/\s*\d{2,3}\s*mmHg\b"]
    blob = json.dumps(CUR["modules"])
    for pat in banned:
        if re.search(pat, blob):
            err(f"curriculum contains an individual clinical target matching {pat}")


PIPELINE = list(N.PIPELINE)


def run_pipeline(files):
    PY = N.pipeline_python()
    for f in files:
        for step in PIPELINE:
            cmd = ([PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", f]
                   if step == "REFS" else [PY, step, "--guide", f])
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  ! {step} failed on {f}: {(r.stderr or r.stdout).strip()[-300:]}")
        print(f"  patched {f}", flush=True)


def build_calc():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "patients_care_partners" / "build_toolkit.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--patch", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--calc", action="store_true")
    ap.add_argument("--no-publish", action="store_true", help="write and patch in guides/ only; do not move to academy/")
    args = ap.parse_args()
    global GUIDES
    if args.calc and not args.check:
        build_calc()
    check()
    if args.check:
        import tempfile, shutil
        real = GUIDES
        GUIDES = Path(tempfile.mkdtemp())
        if (real / C.TOOLKIT).exists():
            shutil.copy(real / C.TOOLKIT, GUIDES / C.TOOLKIT)
    refs = {}
    for code in ORDER:
        f, r = build_module(code); refs[f] = r
    for fn in (build_hub, build_final, build_urgent, build_worksheets, build_facilitators):
        f, r = fn(); refs[f] = r
    if ERRORS:
        print("\nCONTENT ERRORS:")
        for e in ERRORS:
            print("  -", e)
        sys.exit(1)
    if args.check:
        print(f"content OK: {len(refs)} pages")
        return
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "refs-overrides.json").write_text(json.dumps(refs, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(refs)} pages to guides/")
    if args.patch:
        run_pipeline(sorted(refs))
    if args.no_publish:
        return
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip()[-2000:])
    for script in ("tools/patients_care_partners/wire_landing.py", "tools/academy/apply_track_colors.py"):   # Patients column under Administrative
        r = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout or r.stderr).strip())
    if ERRORS:
        for e in ERRORS:
            print("  -", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
