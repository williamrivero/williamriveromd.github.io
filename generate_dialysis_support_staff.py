#!/usr/bin/env python3
"""Renal Care Academy · Ancillary Staff Track · Dialysis Unit Support Staff (orderlies and EVS aides).

Pages: hub (dialysis-unit-support-staff), 15 modules (dialysis-unit-support-staff-NN-<slug>), end-of-course knowledge
check (dialysis-unit-support-staff-final-exam), and the Support Staff Toolkit calculator (guides/calc-dialysis-support-staff-toolkit.html).
Content lives in tools/dialysis_support_staff/content/*.py (hand-edited). Patterned on generate_transplant_nurse.py.

    python3 generate_dialysis_support_staff.py              # write pages to guides/, then publish to academy/
    python3 generate_dialysis_support_staff.py --patch      # also run the /setup-guide patch pipeline on each page
    python3 generate_dialysis_support_staff.py --check      # validate content only (refs, quiz keys, links)
    python3 generate_dialysis_support_staff.py --calc       # (re)build the Support Staff Toolkit and run its pipeline

Never hand-edit academy/dialysis-unit-support-staff*.html: edit the content files and re-run.
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
CONTENT = ROOT / "tools" / "dialysis_support_staff" / "content"
DATA = ROOT / "data" / "dialysis-unit-support-staff"
SITE = "https://renalcarematters.com"
ERRORS = []
BANK_SIZE, DRAW = 15, 5


def err(m):
    ERRORS.append(m)


def load(name):
    spec = importlib.util.spec_from_file_location(f"duss_{name}", CONTENT / f"{name}.py")
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
for mid, slug, title, short, week, (g_h, p_h), comps, pathway in C.MODULES:
    m = load(f"m{mid}").MODULE
    m.update(id=mid, slug=f"{COURSE['hub_slug']}-{mid}-{slug}", title=title, short=short, week=week, hours=g_h + p_h,
             guided=g_h, practice_h=p_h, comps=comps, pathway=pathway)
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
/* Dialysis Unit Support Staff subtrack: visual components (design tokens only, so dark mode holds). */
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

DISCLAIMER = ("Educational self-study for dialysis unit support staff. Does not replace your employer&rsquo;s written task list, "
              "the unit&rsquo;s infection prevention, waste and safety procedures, product labels, DOH and DOLE requirements, "
              "or supervised practice and sign-off.")


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
    <a href="renal-care-academy.html">Renal Care Academy</a><span class="nc-sep">›</span><a class="nc-group" href="renal-care-academy.html#track-ancillary">Ancillary Staff Track</a><span class="nc-sep">›</span><a href="{HUB}">{COURSE['title']}</a><span class="nc-sep">›</span><span>{label}</span>
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
    "calc-dialysis-support-staff-toolkit.html": ("Dialysis Support Staff Toolkit", "Label dilution and contact-time planner, station turnover time budget, safe lift check and cleaning or hand hygiene audit tally."),
    "calc-qapi-cqi-toolkit.html": ("Quality Improvement Toolkit", "Aim statements, run charts and improvement cycles for the unit team."),
    "calc-qapi-run-chart-spc.html": ("Run Chart", "Plot an audit result over time and see whether a change is real."),
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
  <div class="section-tag">Learning objectives &middot; about {m['hours']:g} hours ({m['guided']:g} guided, {m['practice_h']:g} practice) &middot; day {m['week']} &middot; {m['pathway']}</div>
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
    outcome = (f'  <div class="tc-scene tn-outcome"><span class="tc-lab">How it played out &middot; fictional</span>\n{c["outcome"].strip()}\n  </div>\n'
               if c.get("outcome") else "")
    parts.append(f"""<section class="section" id="case">
  <div class="section-tag">Practice case &middot; synthetic</div>
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
    for q in m["quiz"] + m["exam"]:
        cites.add(q.get("sources", []))
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Knowledge check</div>
  <h2>Check your understanding</h2>
  <p>Each visit draws {DRAW} questions at random from this module&rsquo;s {len(m['quiz'])}-question bank, in a shuffled order. Choose the single best answer for each, then select <strong>Check answers</strong>; a rationale appears under every option. Select <strong>New set of questions</strong> for a different mix. Nothing you select is sent anywhere; scoring happens in your browser and records self-study only.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="duss{mid}" data-draw="{DRAW}" novalidate>
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
  <p>Back to the <a href="{HUB}">Support Staff course home</a> &middot; the <a href="{PARENT}">Nephrology Nursing course</a> &middot; the infection prevention lesson nurses study, <a href="{ENTRY}">Nephrology Nursing Module 7</a>.</p>
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")

    main = tn_expand("\n\n".join(parts), fname)
    nav = [("objectives", "Objectives")] + [(s["id"], s["nav"]) for s in m["sections"]] + \
          [("case", "Case"), ("quiz", "Knowledge check"), ("competencies", "Competencies"), ("practice", "Supervised practice"), ("reading", "Reading")]
    cards = [(HUB, "Subtrack home", COURSE["long_title"], "Syllabus, pathways, assessment and all fifteen modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], html.unescape(next_m["sub"]).split(",")[0] + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], html.unescape(prev_m["sub"]).split(",")[0] + "."))
    for f, why in m["readings"][:2]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Assigned reading", N.D.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{m['title']}: Dialysis Support Staff Module {n}"
    page = N.shell(
        fname, title, m["desc"], m["keywords"], f"Ancillary Staff Track &middot; Module {n} of {len(MODS)}", m["title"], m["sub"],
        "Dialysis unit orderlies, environmental service aides, utility workers and contracted cleaners &middot; their supervisors and preceptors",
        nav, bar(f"Module {n}"), main, N.glossary_block(main, m.get("terms", [])), N.related_block(cards),
        jsonld_extra={"isPartOf": {"@type": "Course", "name": "Dialysis Unit Support Staff (Renal Care Academy)", "url": f"{SITE}/guides/{COURSE['hub_slug']}"},
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
        cards.append(tile(f"""    <a class="nc-mod" href="{m['slug']}.html" data-module="duss{mid}">""", f"""      <span class="nc-mod-top"><span class="nc-mod-step">Day {m['week']}</span><span>Module {int(mid)}</span><span class="nc-chip">{m['hours']:g} h</span><span class="nc-chip">{', '.join(m['comps']) if len(m['comps']) < 8 else 'S1–S8'}</span></span>
      <span class="nc-mod-title">{m['title']}</span>
      <span class="nc-mod-desc">{html.escape(html.unescape(m['sub']), quote=False)}</span>
      <span class="nc-mod-status" aria-live="off"></span>""", m['slug']))
    sched = "\n".join(
        f"<tr><td>{m['week']}</td><td><a href=\"{m['slug']}.html\">DUSS-{mid} {m['title']}</a></td><td>{m['guided']:g}</td><td>{m['practice_h']:g}</td>"
        f"<td>{m['hours']:g}</td><td>{m['pathway']}</td><td>{m['evidence_out']}</td></tr>" for m in (MODS[x] for x in ORDER))
    tg = sum(MODS[x]['guided'] for x in ORDER); tp = sum(MODS[x]['practice_h'] for x in ORDER)
    comp_rows = "\n".join(f"<tr><td><strong>{k}</strong></td><td>{s}</td><td>{e}</td></tr>" for k, s, e in C.COMPETENCIES)
    src = "".join(f"[[{k}]]" for k in C.HUB_REFS)
    n_mod = len(ORDER)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>A nonclinical track that works alongside nursing</h2>
  <p>This track is for the people who keep a hemodialysis unit clean, safe and moving: orderlies, environmental service (EVS) aides, utility workers, porters and contracted cleaners. It sits in the Ancillary Staff Track and links closely to the Nephrology Nursing course, because nurses direct the patient care that your work supports. That link does not make you a nurse or a nursing assistant, and nothing here authorizes nursing, machine or water-system work.</p>
  <p>The {n_mod} modules explain the reason behind every task before the task itself. Why does dried blood matter if you cannot see it? Why does a disinfectant need to stay wet? Why does a patient faint after dialysis, and why should you never lift a person alone? Each module opens with a plain picture, then explains what is really happening, then says how strong the evidence is, then shows exactly what you do and what you leave to others. Every module has a fictional case set in a Philippine unit, a debrief, a harder second round, a 15-question knowledge check with a reason for every answer, and a checklist to practice with your preceptor.</p>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this track is, and is not</h4>
      <p>It is education and practice preparation. Finishing it does not prove competence, grant permission for any task, or carry Department of Health (DOH), Philippine Health Insurance Corporation (PhilHealth), Philippine Society of Nephrology (PSN) or Professional Regulation Commission continuing professional development (CPD) recognition, or basic life support certification. Your employer authorizes tasks after observed practice. Hours and pass marks are Academy proposals, not national minimums. {COURSE['status']}.</p>
    </div>
  </div>
</section>

<section class="section" id="day">
  <div class="section-tag">What the work looks like</div>
  <h2>A day in the San Isidro Dialysis Unit</h2>
{C.DAY_HTML.strip()}
</section>

<section class="section" id="pathways">
  <div class="section-tag">Two pathways</div>
  <h2>Environmental service aide or orderly</h2>
  <div class="tc-cards">
  <div class="tc-card"><b>Environmental service aide</b>All {n_mod} modules. Practice emphasis: hand hygiene and protective equipment, aseptic habits, product literacy, zone and station cleaning, spills, waste, linen, hazards and records. Patient movement is recognition, route preparation and calling for help. Station and machine-surface cleaning are conditional assignments.</div>
  <div class="tc-card"><b>Orderly</b>All {n_mod} modules and the same environmental foundations, plus observed escort and transfer practice for the duties in your job description, always under the nurse&rsquo;s plan. Environmental tasks only if they are in your job and signed off.</div>
  </div>
  <p>Neither pathway includes needles, catheters, dressings, medicines, blood or bloodlines, vital signs or weighing for treatment decisions, machine controls or alarms, dialyzer reprocessing, concentrate preparation, or water-room work. Prior experience allows a diagnostic check, not exemption from critical observed skills. Contracted staff receive the same unit induction and sign-offs as directly hired staff. <a href="{MODS['01']['slug']}.html#pathways">Module 1</a> has the full duty and scope matrix.</p>
</section>

<section class="section" id="entry">
  <div class="section-tag">Before you begin</div>
  <h2>Entry and readiness</h2>
  <p>Before practical work, complete your employer&rsquo;s induction, an occupational health review that fits your actual duties (including your hepatitis B vaccination record), and chemical, protective-equipment and manual-handling orientation. Covered workers also need the occupational safety and health seminar required by Philippine law; this track does not replace it. Recommended readiness: you can understand safety instructions and labels in English or Filipino with help, tell someone about an urgent problem, and take part in hands-on practice. Ask for reasonable accommodations if you need them.</p>
  <p><strong>Delivery.</strong> About {tg:g} hours of guided learning and {tp:g} hours of practice or simulation, {tg + tp:g} hours in all. At eight scheduled hours a day (excluding breaks) this fits about eight days, followed by observed practice at work until each assigned skill is demonstrated. Never shorten a wet contact time, a patient&rsquo;s recovery or your own rest breaks to meet a timetable.</p>
</section>

<section class="section" id="modules">
  <div class="section-tag">The modules</div>
  <h2>{n_mod} modules</h2>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
  <div class="nc-modgrid" id="nc-modules">
{chr(10).join(cards)}
  </div>
  <p style="margin-top:14px;"><strong>When you have finished:</strong> take the <a href="{EXAM}">end-of-course knowledge check</a>, {COURSE['exam_items']} questions, one from each module, drawn at random. The pass mark is {COURSE['pass_correct']} of {COURSE['exam_items']}.</p>
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
  <h2>Syllabus and hours</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Day</th><th>Module</th><th>Guided</th><th>Practice</th><th>Total</th><th>Pathway</th><th>Required learner work</th></tr></thead>
  <tbody>
{sched}
  <tr><td></td><td><strong>Total</strong></td><td><strong>{tg:g}</strong></td><td><strong>{tp:g}</strong></td><td><strong>{tg + tp:g}</strong></td><td></td><td></td></tr>
  </tbody></table></div>
  <p>Hours are Academy design proposals. They are not a promise that anyone is competent after a fixed time, and they do not equal any statutory training requirement.</p>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>Two separate records</h2>
  <div class="table-wrap"><table>
  <thead><tr><th>Record</th><th>Requirement</th><th>Recorded by</th></tr></thead>
  <tbody>
  <tr><td>Academy self-study completion</td><td>All modules read and the <a href="{EXAM}">end-of-course knowledge check</a> passed ({COURSE['pass_correct']} of {COURSE['exam_items']} or better).</td><td>The learner, here (optionally saved in this browser only)</td></tr>
  <tr><td>Employer-verified task competence</td><td>The six <a href="{MODS['15']['slug']}.html#stations">capstone stations</a> passed with no critical failure, and each authorized high-risk task observed as satisfactory on at least two separate occasions (more if performance varies).</td><td>The employer, on signed printable forms in its own records</td></tr>
  </tbody></table></div>
  <p>Critical failures are never averaged away. A failed action leads to explanation, demonstration, practice and reassessment with an equivalent scenario; until then the task stays under direct supervision or outside authorization. Repeated difficulty leads to a tailored plan, not automatic dismissal. This website cannot check identity or observe your hands, so nothing you do online records workplace competence.</p>
</section>

<section class="section" id="educators">
  <div class="section-tag">For educators and preceptors</div>
  <h2>Localize before teaching</h2>
  <p>The lessons use generic workflows on purpose. Before teaching, gather your unit&rsquo;s map, the approved task cards and safety data sheets, the product list with dilution and wet contact time, the waste color chart and route, the linen procedure, the exposure hotline and after-hours route, the emergency codes and exits, the transport aids actually available, and the written task list for each worker. Use them in every simulation. Use training props: a harmless spill substitute, mock sharps, empty sample containers and fluorescent marker gel. Never use real blood or real sharps for teaching.</p>
  <div class="tc-cards">
  <div class="tc-card"><b>Six capstone stations</b>Hand hygiene and doffing &middot; product card and station turnover &middot; spill and exposure &middot; waste and linen &middot; escort and transfer (orderly) &middot; emergency activation with handoff.</div>
  <div class="tc-card"><b>Stop, Tell, Stay</b>Stop the task or keep the person safe &middot; tell the nurse or supervisor what you saw, where, and when &middot; stay until someone takes over.</div>
  <div class="tc-card"><b>Task authorization record</b>Task &middot; procedure and version &middot; training date &middot; observation 1 and 2 with dates &middot; assessor &middot; authorized, restricted or not assigned &middot; review trigger.</div>
  <div class="tc-card"><b>Refresher</b>Annual focused review and observation, and immediate retraining after an incident, a product or process change, a long absence or a poor audit.</div>
  </div>
</section>

<section class="section" id="calculators">
  <div class="section-tag">Tools</div>
  <h2>The Support Staff Toolkit</h2>
  <p>Built for this track. It has four tools: a <strong>label dilution and contact-time planner</strong> that uses only the numbers printed on your product&rsquo;s label; a <strong>station turnover time budget</strong> that shows whether the gap between shifts leaves time for full wet contact; a <strong>safe lift check</strong> using the revised NIOSH (National Institute for Occupational Safety and Health) lifting equation for boxes, jugs and bins; and an <strong>audit tally</strong> for fluorescent-marker cleaning checks and hand hygiene observations.</p>
{calc_cards(['calc-dialysis-support-staff-toolkit.html', 'calc-qapi-run-chart-spc.html'], 'hub').replace('Calculators for this module', 'Calculators')}
</section>

<section class="section" id="sources">
  <div class="section-tag">Evidence and policy register</div>
  <h2>Sources behind this track</h2>
  <p>Desk review dated 24 November 2026. Before publication or workplace use, the unit&rsquo;s clinical head, nurse educator, IPC, EVS, waste, safety and transport leads should review the wording, and the current DOH licensing circular and assessment tool, current PSN infection-control updates and current PhilHealth provisions should be obtained and reconciled. Local product cards and waste plans always govern.{cites.render(src)}</p>
</section>"""
    main = tn_expand(main, HUB)
    nav = [("start", "Start here"), ("day", "A day in the unit"), ("pathways", "Pathways"), ("entry", "Entry"), ("modules", "Modules"),
           ("outcomes", "Competencies"), ("schedule", "Schedule"), ("assessment", "Assessment"), ("educators", "For educators"),
           ("calculators", "Toolkit"), ("sources", "Sources")]
    related = [(PARENT, "Partner course", "Nephrology Nursing &amp; Hemodialysis", "The nursing course that directs the care this work supports."),
               (ENTRY, "Related lesson", "Nephrology Nursing Module 7: Vascular Access and Infection Prevention", "How nurses prevent infection at the chairside."),
               (MODS["01"]["slug"] + ".html", "Start", MODS["01"]["title"], "Module 1 of the course."),
               (EXAM, "Knowledge check", "End-of-Course Knowledge Check", f"{COURSE['exam_items']} questions, one per module; pass at {COURSE['pass_correct']}.")]
    page = N.shell(
        HUB, "Dialysis Unit Support Staff: Orderlies and EVS Aides · Renal Care Academy",
        f"A free Philippine-first training track in the Renal Care Academy&rsquo;s Ancillary Staff Track, for dialysis unit orderlies and environmental service aides: {n_mod} modules on scope, dignity, how germs travel, hand hygiene, aseptic habits, cleaning products, station turnover, spills and sharps, health care waste, linen, patient transport, safe lifting, emergencies and records.",
        "dialysis unit orderly training, environmental service aide dialysis, hospital housekeeping infection control Philippines, health care waste segregation training, patient transport orderly course, renal care academy",
        "Ancillary Staff Track &middot; Course home", "Dialysis Unit Support Staff",
        f"{n_mod} modules for orderlies and environmental service aides: the reason behind every cleaning, waste and transport task, what the evidence shows, and exactly where your role begins and ends.",
        "Orderlies, environmental service aides, utility workers and contracted cleaners in hemodialysis units &middot; their supervisors and preceptors",
        nav, bar("Subtrack home").replace(f'<span class="nc-sep">›</span><a href="{HUB}">{COURSE["title"]}</a><span class="nc-sep">›</span><span>Subtrack home</span>', f'<span class="nc-sep">›</span><span>{COURSE["title"]}</span>'),
        main, N.glossary_block(main, []), N.related_block(related),
        jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": "Nonclinical training track for dialysis unit orderlies and environmental service aides.",
                      "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE},
                      "hasPart": [{"@type": "LearningResource", "name": MODS[x]["title"], "url": f"{SITE}/guides/{MODS[x]['slug']}"} for x in ORDER],
                      "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "An environmental service aide and an orderly in a bright hemodialysis unit, one wiping a dialysis chair arm, the other steadying an empty wheelchair."},
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
    n_mod = len(ORDER)
    main = f"""<section class="section" id="exam">
  <div class="section-tag">End-of-course knowledge check</div>
  <h2>{COURSE['exam_items']} questions, one from each module</h2>
  <p>Each sitting draws one question at random from each of the {n_mod} modules (a pool of {len(items)} questions), in a shuffled order with shuffled options. Answer all of them, then select <strong>Check answers</strong>. The pass mark is <strong>{COURSE['pass_correct']} of {COURSE['exam_items']}</strong>. A reason appears under every option.</p>
  <p>A pass marks your <strong>Academy self-study as complete</strong>. It is not employer-verified competence and does not authorize any task. If you do not pass, review the modules for the questions you missed, then select <strong>New set of questions</strong> for a parallel version.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="duss-final" data-draw="{COURSE['exam_items']}" data-stratify="1" data-pass="{COURSE['pass_correct']}" novalidate>
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
  <p>Prepare for the six <a href="{MODS['15']['slug']}.html#stations">capstone stations</a> and arrange observed practice of your assigned tasks with your supervisor. Return to the <a href="{HUB}">course home</a>.</p>
</section>"""
    main = tn_expand(main, EXAM)
    page = N.shell(
        EXAM, "End-of-Course Knowledge Check: Dialysis Unit Support Staff · Renal Care Academy",
        f"{COURSE['exam_items']}-question end-of-course knowledge check for the Renal Care Academy Dialysis Unit Support Staff course, one question drawn from each module, pass mark {COURSE['pass_correct']} of {COURSE['exam_items']}, with reasons for every answer.",
        "dialysis orderly quiz, environmental service aide test, dialysis housekeeping knowledge check, renal care academy",
        "Ancillary Staff Track &middot; Examination", "End-of-Course Knowledge Check",
        f"One question from each of the {n_mod} modules, drawn at random each sitting. Pass with {COURSE['pass_correct']} of {COURSE['exam_items']}.",
        "Learners who have completed the Dialysis Unit Support Staff modules",
        [("exam", "Knowledge check"), ("next", "Next steps")], bar("Knowledge check"), main, N.glossary_block(main, []),
        N.related_block([(HUB, "Subtrack home", COURSE["long_title"], "All modules, pathways and assessment details."),
                         (MODS["15"]["slug"] + ".html", "Capstone", MODS["15"]["title"], "The six practical stations.")]),
        jsonld_extra={"learningResourceType": "Quiz", "lastReviewed": COURSE["review_date"]},
        hero_img={"file": COURSE["hub_slug"] + "-vignette-hero", "alt": "A dialysis unit aide completing a knowledge check on a phone in a staff room."},
        disclaimer=DISCLAIMER,
    )
    (GUIDES / EXAM).write_text(finish(page), encoding="utf-8")
    return EXAM, cites.list()


# ───────────────────────── entry links on the parent course ─────────────────────────
ENTRY_MARK = ("<!-- DUSS-SUBTRACK-START -->", "<!-- DUSS-SUBTRACK-END -->")


def entry_blocks():
    m07 = f"""{ENTRY_MARK[0]}
<section class="section" id="support-staff">
  <div class="section-tag">For the whole team</div>
  <h2>Training the support staff who share your infection prevention work</h2>
  <p>Orderlies and environmental service aides clean the stations, carry the waste and move the patients you care for. The Renal Care Academy&rsquo;s <a href="{HUB}">Dialysis Unit Support Staff course</a> gives them the reasons behind the tasks: {len(ORDER)} modules on scope, hand hygiene, aseptic habits, product labels and wet contact time, station turnover after clinical clearance, spills and exposures, health care waste, linen, patient transport and safe lifting. Use it to onboard new support staff and to keep the clinical and environmental phases of turnover distinct.</p>
</section>
{ENTRY_MARK[1]}
"""
    return m07


def wire_parent():
    """Idempotently add the entry block to Nephrology Nursing Module 7 in academy/. The specialty card on the parent hub
    comes from tools/academy/nursing_specialties.py (rendered by generate_transplant_nurse.entry_blocks())."""
    done = []
    p = ACADEMY / ENTRY
    if not p.exists():
        err(f"parent page missing: academy/{ENTRY}")
        return done
    s = p.read_text(encoding="utf-8")
    s = re.sub(re.escape(ENTRY_MARK[0]) + r".*?" + re.escape(ENTRY_MARK[1]) + r"\n?", "", s, flags=re.S)
    anchor = '<section class="section" id="case">'
    if anchor not in s:
        err(f"anchor not found in academy/{ENTRY}: {anchor}")
        return done
    s = s.replace(anchor, entry_blocks() + anchor, 1)
    if 'href="#support-staff"' not in s:
        s = s.replace('<a class="nav-pill" href="#case">', '<a class="nav-pill" href="#support-staff">Support staff track</a>\n<a class="nav-pill" href="#case">', 1)
    s = s.replace('href="#support-staff">Support staff subtrack</a>', 'href="#support-staff">Support staff track</a>')
    p.write_text(s, encoding="utf-8")
    done.append(ENTRY)
    return done


# ───────────────────────── Support Staff Toolkit calculator ─────────────────────────
CALC = "calc-dialysis-support-staff-toolkit.html"
CALC_REFS = ["west2019", "rutala2019", "cdc_station", "waters1993", "niosh1994", "waters2007", "carling2006", "mitchell2019", "who2009"]
CALC_PIPELINE = ["patch_published_time.py", "patch_reading_time.py", "REFS", "patch_hero_meta.py", "patch_share_title.py",
                 "patch_canonical_clean_urls.py", "patch_share_buttons.py", "patch_guide_rail.py", "add_calc_nav_pill.py",
                 "patch_calc_handoff.py", "patch_calc_english_only.py"]
CALC_CARD = """<a class="related-card" href="calc-dialysis-support-staff-toolkit.html">
<div class="related-card-tag">Dialysis unit · Support staff</div>
<div class="related-card-title">Dialysis Support Staff Toolkit</div>
<div class="related-card-desc">Label dilution and wet contact time, station turnover time budget, safe lift check, and cleaning and hand hygiene audit tally.</div>
<div class="related-card-arrow">Open →</div></a>
"""


def build_calc():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "dialysis_support_staff" / "build_calc_toolkit.py")], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout or r.stderr).strip())
    idx = GUIDES / "calculators.html"
    if idx.exists():
        s = idx.read_text(encoding="utf-8")
        if f'href="{CALC}"' not in s:
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
