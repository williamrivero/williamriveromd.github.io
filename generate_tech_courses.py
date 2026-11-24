#!/usr/bin/env python3
"""Generate the dialysis technical-workforce courses (hub, trainer page, modules for each course).

Courses (tools/techcourses/<package>/course.py):
    hd_technician     Dialysis Technician                guides/hemodialysis-technician*.html
    water_treatment   Water Treatment System Technician  guides/water-treatment-technician*.html
    biomed            Dialysis Biomedical Technician     guides/dialysis-biomedical-technician*.html

The pages reuse the Nephrology Nursing course chrome (header, course CSS, quiz markup) by importing
generate_nursing_course.py, and add figure components (site illustrations, flow strips, term cards).

    python3 generate_tech_courses.py                 # write all pages + docs
    python3 generate_tech_courses.py --course biomed # one course
    python3 generate_tech_courses.py --patch         # write, then run the /setup-guide patch pipeline
    python3 generate_tech_courses.py --check         # validate content only

Never hand-edit the generated pages: edit tools/techcourses/** and re-run.
"""
import argparse, html, importlib.util, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_nursing_course as N  # noqa: E402  (chrome, CSS, helpers)

GUIDES = ROOT / "guides"
IMAGES = ROOT / "images"
TC = ROOT / "tools" / "techcourses"
DATA = ROOT / "data" / "tech-courses"
DOCS = ROOT / "docs" / "tech-courses"
SITE = "https://renalcarematters.com"
PACKAGES = ["hd_technician", "water_treatment", "biomed", "pod", "renal_dietitian", "dch", "pd_nurse", "philhealth_claims", "uom", "an", "mro", "head_nurse"]
ERRORS = []
CRIT = '<span class="tc-crit">Critical</span>'


def err(m):
    ERRORS.append(m)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FIGS = load(TC / "figs.py", "tc_figs").FIGS
_AC = load(TC / "academy_figs.py", "tc_academy_figs") if (TC / "academy_figs.py").exists() else None
if _AC:
    FIGS.update(_AC.FIGS)
PLACE = _AC.PLACE if _AC else {}
HERO_ALT = getattr(_AC, "HERO_ALT", {}) if _AC else {}


def placed(slug, section):
    """Figure macros for the produced Academy figures placed in this section (tools/techcourses/academy_figs.py)."""
    return "".join(f"\n{{{{fig:{k}}}}}\n" for sec, k in PLACE.get(slug, []) if sec == section)


def place_after_first_para(html_text, figs):
    """Insert figure macros after the first paragraph of a section, or at its start when it has none early on."""
    if not figs:
        return html_text
    i = html_text.find("</p>")
    if 0 <= i < 1600:
        return html_text[:i + 4] + figs + html_text[i + 4:]
    return figs + html_text
SHARED = load(TC / "shared.py", "tc_shared")
for _p in PACKAGES:      # optional per-course references (refs.py) and figures (figs.py)
    if (TC / _p / "refs.py").exists():
        SHARED.REFS.update(load(TC / _p / "refs.py", f"tc_{_p}_refs").REFS)
    if (TC / _p / "figs.py").exists():
        FIGS.update(load(TC / _p / "figs.py", f"tc_{_p}_figs").FIGS)
for _p in PACKAGES:      # optional per-course abbreviations (abbr.py)
    if (TC / _p / "abbr.py").exists():
        SHARED.ABBR.update(load(TC / _p / "abbr.py", f"tc_{_p}_abbr").ABBR)
N.ABBR.update(SHARED.ABBR)          # same dict object the nursing helpers read

# ───────────────────────── styles ─────────────────────────
TECH_CSS = """
/* Technical-workforce courses: figures and visual components (tokens only; dark mode holds). */
.tc-fig{margin:18px 0;border:1px solid var(--border);border-radius:14px;background:var(--white);overflow:hidden;}
.tc-fig img{display:block;width:100%;height:auto;}
.tc-fig figcaption{padding:10px 16px;font-size:13.5px;line-height:1.55;color:var(--text-mid);border-top:1px solid var(--border);}
.tc-fig figcaption b{color:var(--text);}
.tc-fig-narrow{max-width:560px;margin-left:auto;margin-right:auto;}
.tc-viz{margin:18px 0;border:1px solid var(--border);border-radius:14px;background:var(--bg);padding:14px 16px;}
.tc-viz-title{font:700 .78rem Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);margin:0 0 10px;}
html[data-theme="dark"] .tc-viz-title,html[data-theme="dark"] .tc-lab{color:#7fd6dd;}
.tc-flow{display:flex;flex-wrap:wrap;gap:8px;align-items:stretch;list-style:none;margin:0;padding:0;counter-reset:tc;}
.tc-flow li{flex:1 1 150px;border:1px solid var(--border);border-top:4px solid var(--teal);border-radius:10px;background:var(--white);padding:10px 12px;font-size:14px;line-height:1.5;color:var(--text-mid);counter-increment:tc;}
.tc-flow li b{display:block;color:var(--text);font-size:14.5px;margin-bottom:2px;}
.tc-flow li b::before{content:counter(tc) ". ";color:var(--teal);}
.tc-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;}
.tc-card{border:1px solid var(--border);border-left:4px solid var(--teal);border-radius:10px;background:var(--white);padding:10px 14px;font-size:14px;line-height:1.55;color:var(--text-mid);}
.tc-card b{display:block;color:var(--text);margin-bottom:2px;}
.tc-plain{border-left:4px solid var(--teal);background:var(--teal-light);border-radius:0 12px 12px 0;padding:12px 16px;margin:14px 0;font-size:15.5px;line-height:1.65;color:var(--text);}
html[data-theme="dark"] .tc-plain{background:#0a2830;}
.tc-lab{display:block;font:700 .72rem Inter,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:3px;}
.tc-keyp{border:1px solid var(--green);border-radius:12px;background:var(--green-soft);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
.tc-stop{border:1px solid var(--red);border-left-width:5px;border-radius:12px;background:var(--white);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.6;color:var(--text);}
.tc-stop .tc-lab{color:var(--red);}
html[data-theme="dark"] .tc-keyp{background:#1a2535;}
.tc-crit{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--red);border:1px solid var(--red);border-radius:999px;padding:0 8px;margin-right:6px;vertical-align:1px;}
.tc-hours{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0;}
.tc-branches{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:14px 0;}
.tc-branch{display:flex;flex-direction:column;border:2px solid var(--border);border-radius:14px;background:var(--white);text-decoration:none;color:var(--text);overflow:hidden;}
.tc-branch:hover{border-color:var(--teal);}
.tc-branch[aria-current="page"]{border-color:var(--teal);box-shadow:0 0 0 3px var(--teal-light);}
html[data-theme="dark"] .tc-branch[aria-current="page"]{box-shadow:0 0 0 3px #0a2830;}
.tc-branch img,.tc-mod-img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;background:var(--bg);}
.tc-syl-lessons{margin:0;padding-left:1.15em;font-size:.92em;line-height:1.45;min-width:15em;}.tc-syl-lessons li{margin:0 0 .15em;}
.tc-branch-body{padding:12px 16px 14px;display:flex;flex-direction:column;gap:4px;}
.tc-branch small{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);font-weight:700;}
.tc-branch b{font-family:Inter,system-ui,sans-serif;font-size:1.02rem;}
.tc-branch span{font-size:14px;line-height:1.55;color:var(--text-mid);}
.nc-mod.tc-mod{padding:0;overflow:hidden;}
.tc-mod-body{display:flex;flex-direction:column;gap:6px;padding:12px 16px 14px;}
.tc-soon{opacity:.75;}
.tc-sits{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0;}
.tc-sit{border:1px solid var(--border);border-top:4px solid var(--amber);border-radius:12px;background:var(--white);padding:12px 16px 10px;}
.tc-sit h3{margin:0 0 6px;font-family:Inter,system-ui,sans-serif;font-size:1rem;line-height:1.35;color:var(--text);}
.tc-sit dl{margin:0;}
.tc-sit dt{font:700 .7rem Inter,system-ui,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:var(--text-muted);margin-top:8px;}
.tc-sit dt.tc-sit-do{color:var(--teal);}
html[data-theme="dark"] .tc-sit dt.tc-sit-do{color:#7fd6dd;}
.tc-sit dd{margin:2px 0 0;font-size:14.5px;line-height:1.6;color:var(--text-mid);}
.tc-tips{margin:4px 0 0;padding-left:20px;line-height:1.65;}
@media (max-width:720px){.tc-sits{grid-template-columns:1fr;}}
@media print{.tc-sit{break-inside:avoid;}}
.tc-q-list{margin:8px 0 0;padding-left:22px;line-height:1.65;}
.tc-formula{border:1px dashed var(--border);border-radius:12px;background:var(--bg);padding:12px 16px;margin:12px 0;font-size:15px;line-height:1.6;}
.tc-tracks{grid-template-columns:repeat(2,minmax(0,1fr));}
div.tc-branch.tc-soon{border-style:dashed;}
@media (max-width:720px){.tc-branches{grid-template-columns:1fr;}}
@media print{.tc-fig,.tc-viz,.tc-card,.tc-flow li{break-inside:avoid;}}
.tc-part{margin:26px 0 4px;font:700 1.02rem Inter,system-ui,sans-serif;color:var(--text);}
.nc-chip-tier{border-color:var(--teal);color:var(--teal);}
html[data-theme="dark"] .nc-chip-tier{border-color:#7fd6dd;color:#7fd6dd;}
"""


# ───────────────────────── figure + macro rendering ─────────────────────────
_DIMS = json.loads((TC / "img_dims.json").read_text()) if (TC / "img_dims.json").exists() else {}


def _img_size(path):
    """Pixel size for width/height attributes. Falls back to tools/techcourses/img_dims.json for
    files that exist but cannot be read here (for example cloud-only files not yet downloaded)."""
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        d = _DIMS.get(Path(path).name)
        return tuple(d) if d else None


def img_tag(file, alt, eager=False):
    """<picture> for images/<file>; file may be .png or .webp. Returns None when the file is missing."""
    p = IMAGES / file
    if not p.exists():
        return None
    size = _img_size(p)
    wh = f' width="{size[0]}" height="{size[1]}"' if size else ""
    src = ""
    webp = p.with_suffix(".webp")
    if p.suffix != ".webp" and webp.exists():
        src = f'<source srcset="../images/{webp.name}" type="image/webp">'
    load_attr = 'loading="eager"' if eager else 'loading="lazy" decoding="async"'
    return f'<picture>{src}<img class="nc-fig-img" src="../images/{file}" alt="{html.escape(html.unescape(alt))}"{wh} {load_attr}></picture>'


class Page:
    """Per-page state: figure numbering and the numbered source list."""

    def __init__(self, label):
        self.label = label
        self.nfig = 0
        self.refs = []       # html strings, in order of first use
        self._idx = {}

    def ref(self, key_or_url, label=None):
        if key_or_url in self._idx:
            return self._idx[key_or_url]
        if key_or_url in SHARED.REFS:
            text = SHARED.REFS[key_or_url]
        elif label is not None:
            text = fmt_link_ref(label, key_or_url)
        else:
            err(f"{self.label}: unknown reference key [[{key_or_url}]]")
            return 0
        self.refs.append(text)
        self._idx[key_or_url] = len(self.refs)
        return len(self.refs)

    def sup(self, n):
        return f'<sup class="nc-cite"><a href="#ref-{n}" data-ref="{n}" aria-label="Reference {n}">{n}</a></sup>' if n else ""

    def figure(self, key, caption=None, cls=""):
        if key not in FIGS:
            err(f"{self.label}: unknown figure key {key}")
            return ""
        file, alt, cap = FIGS[key]
        tag = img_tag(file, alt)
        if not tag:
            return f"<!-- figure pending: images/{file} -->"
        self.nfig += 1
        cap = caption or cap
        return (f'<figure class="tc-fig{(" " + cls) if cls else ""}">{tag}'
                f'<figcaption><b>Figure {self.nfig}.</b> {cap}</figcaption></figure>')

    def render(self, text):
        """Expand {{macro:...}} blocks and [[ref]] citations."""
        def macro(m):
            kind, _, body = m.group(1).partition(":")
            body = body.strip()
            if kind == "fig":
                key, _, cap = body.partition("|")
                return self.figure(key.strip(), cap.strip() or None)
            if kind == "fignarrow":
                key, _, cap = body.partition("|")
                return self.figure(key.strip(), cap.strip() or None, "tc-fig-narrow")
            if kind in ("flow", "cards"):
                title, *items = [x.strip() for x in body.split("|")]
                out = []
                for it in items:
                    h, _, t = it.partition("::")
                    if kind == "flow":
                        out.append(f"<li><b>{h.strip()}</b>{t.strip()}</li>")
                    else:
                        out.append(f'<div class="tc-card"><b>{h.strip()}</b>{t.strip()}</div>')
                inner = (f'<ol class="tc-flow">{"".join(out)}</ol>' if kind == "flow"
                         else f'<div class="tc-cards">{"".join(out)}</div>')
                self.nfig += 1
                return (f'<div class="tc-viz" role="group" aria-label="{html.escape(html.unescape(title))}">'
                        f'<p class="tc-viz-title">Figure {self.nfig} &middot; {title}</p>{inner}</div>')
            if kind == "plain":
                return f'<div class="tc-plain"><span class="tc-lab">In plain words</span>{body}</div>'
            if kind == "key":
                return f'<div class="tc-keyp"><span class="tc-lab">Remember</span>{body}</div>'
            if kind == "stop":
                return f'<div class="tc-stop"><span class="tc-lab">Stop and report</span>{body}</div>'
            if kind == "call":
                return f'<div class="tc-stop"><span class="tc-lab">Stop and call</span>{body}</div>'
            if kind == "formula":
                return f'<div class="tc-formula">{body}</div>'
            err(f"{self.label}: unknown macro {kind}")
            return ""
        text = re.sub(r"\{\{(.+?)\}\}", macro, text, flags=re.S)
        return re.sub(r"\[\[([a-z0-9_]+)\]\]", lambda m: self.sup(self.ref(m.group(1))), text)


def fmt_link_ref(label, url):
    label = html.escape(label, quote=False)
    if " · " in label:
        pub, title = label.split(" · ", 1)
        head = f"{pub}. <em>{title}</em>."
    else:
        head = f"<em>{label}</em>."
    return f'{head} Retrieved {SHARED.RETRIEVED}, from <a href="{html.escape(url)}">{html.escape(url, quote=False)}</a>'


# ───────────────────────── Markdown source (HD Technician) ─────────────────────────
def md_inline(s, page):
    s = html.escape(s, quote=False)
    cites = []

    def link(m):
        label, url = html.unescape(m.group(1)), html.unescape(m.group(2))
        if not url.startswith("http"):
            return label if not url.endswith(".md") else ""
        cites.append(page.sup(page.ref(url, label)))
        return f"\x00{len(cites) - 1}\x00"
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\x00\s*·\s*\x00", "\x00\x00", s)
    s = re.sub(r"\s+\x00", "\x00", s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: cites[int(m.group(1))], s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s.strip()


def md_blocks(lines, page, fig_file=None):
    """Convert a list of Markdown lines to HTML blocks. Returns list of (kind, html, raw_first_line)."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("!["):
            m = re.match(r"!\[(.*?)\]\((.*?)\)", ln)
            cap = ""
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"\*Figure \d+\.", lines[j]):
                cap = re.sub(r"^\*Figure \d+\.\s*|\*$", "", lines[j].strip())
                i = j
            tag = img_tag(fig_file, m.group(1)) if fig_file else None
            if tag:
                page.nfig += 1
                out.append(("fig", f'<figure class="tc-fig">{tag}<figcaption><b>Figure {page.nfig}.</b> {md_inline(cap, page)}</figcaption></figure>', ln))
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            body = [r for r in rows[2:]]
            th = "".join(f"<th>{md_inline(c, page)}</th>" for c in rows[0])
            trs = "\n".join("<tr>" + "".join(f"<td>{md_inline(c, page)}</td>" for c in r) + "</tr>" for r in body)
            out.append(("table", f'<div class="table-wrap"><table>\n<thead><tr>{th}</tr></thead>\n<tbody>\n{trs}\n</tbody></table></div>', rows))
            continue
        if re.match(r"\d+\. ", ln) or ln.startswith("- "):
            ordered = not ln.startswith("- ")
            pat = r"\d+\. " if ordered else r"- "
            items = []
            while i < len(lines) and (re.match(pat, lines[i]) or (lines[i].startswith("   ") and items)):
                if re.match(pat, lines[i]):
                    items.append(re.sub("^" + pat, "", lines[i]).strip())
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            tag = "ol" if ordered else "ul"
            out.append((tag, f"<{tag}>\n" + "\n".join(f"<li>{md_inline(x, page)}</li>" for x in items) + f"\n</{tag}>", items))
            continue
        if ln.startswith("> "):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(md_inline(lines[i][1:].strip(), page))
                i += 1
            out.append(("formula", '<div class="tc-formula">' + "<br>".join(q) + "</div>", q))
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(\||!\[|- |\d+\. |> |#)", lines[i]):
            para.append(lines[i])
            i += 1
        if not para:
            i += 1
            continue
        raw = " ".join(p.strip() for p in para)
        htmlp = "<br>".join(md_inline(p, page) for p in para if md_inline(p, page))
        if htmlp:
            out.append(("p", f"<p>{htmlp}</p>", raw))
    return out


DEBRIEF_PAT = re.compile(r"\*\*(Case debrief|Example handoff|Example teach-back|Example entry)")


def parse_md_module(src, mid, meta, page):
    """Normalize a Study Guide + Self-Assessment + Answer Key into the module schema."""
    sg = (src / "Study Guide.md").read_text(encoding="utf-8").replace(" ", " ").splitlines()
    sections, cur = [], None
    pre = []
    for ln in sg:
        if ln.startswith("## "):
            cur = [ln[3:].strip(), []]
            sections.append(cur)
        elif cur is None:
            pre.append(ln)
        else:
            cur[1].append(ln)
    m = {"objectives": [], "sections": [], "debrief": [], "case": {"title": "", "html": "", "questions": []},
         "skills": {"title": "", "intro": "", "items": [], "placement": ""}}
    alt = next((re.match(r"!\[(.*?)\]", l).group(1) for l in pre if l.startswith("![")), "")
    m["image_alt"] = alt
    fig_file = f"{meta['slug']}-teaching-diagram.png"
    enrich = meta.get("enrich", {})
    navs = enrich.get("navs", [])
    m["big"] = page.render(enrich.get("big", "") + placed(meta["slug"], "bigpicture"))
    k = 0
    for head, lines in sections:
        if head.lower().startswith("learning objectives"):
            m["objectives"] = [md_inline(re.sub(r"^\d+\.\s*", "", l), page) for l in lines if re.match(r"\d+\. ", l)]
        elif head.lower().startswith("opening case"):
            m["case"]["title"] = head.split("·", 1)[1].strip() if "·" in head else meta["case_title"]
            for kind, h, raw in md_blocks(lines, page):
                if kind == "ul":
                    m["case"]["questions"] = [md_inline(x, page) for x in raw]
                elif kind == "p" and raw.lower().startswith("before reading on"):
                    m["case"]["questions"] = ["What would you pause?", "Whom would you contact?", "Where would you document the event?"]
                else:
                    m["case"]["html"] += h + "\n"
        elif head.lower().startswith("skills checklist"):
            m["skills"]["title"] = head.split("·", 1)[1].strip() if "·" in head else "Shift-start verification and handoff"
            for kind, h, raw in md_blocks(lines, page):
                if kind == "table":
                    for r in raw[2:]:
                        t = r[0]
                        crit = "**Critical.**" in t
                        m["skills"]["items"].append((md_inline(t.replace("**Critical.**", "").strip(), page), crit))
                elif kind == "ul":
                    for t in raw:
                        t = t.replace("☐", "").strip()
                        crit = "**Critical.**" in t
                        m["skills"]["items"].append((md_inline(t.replace("**Critical.**", "").strip(), page), crit))
                elif kind == "p":
                    if re.search(r"Learner[:*\s_]", raw) or raw.startswith("["):
                        continue
                    if "Placement activity" in raw or raw.startswith("During placement"):
                        m["skills"]["placement"] = md_inline(re.sub(r"\*\*Placement activity\.\*\*\s*", "", raw), page)
                    elif raw.startswith("**Sign-off"):
                        continue
                    else:
                        m["skills"]["intro"] += " " + md_inline(re.sub(r"\*\*Materials[:.]?\*\*\s*[—:]?\s*", "Materials: ", raw), page)
        else:
            k += 1
            title = re.sub(r"^\d+\.\s*", "", head)
            pre_html = page.render(enrich.get("pre", {}).get(k, ""))
            blocks = md_blocks(lines, page, fig_file)
            body = []
            for kind, h, raw in blocks:
                if kind == "p" and DEBRIEF_PAT.match(raw):
                    m["debrief"].append(h)
                elif kind == "p" and raw.startswith("["):
                    continue
                else:
                    body.append(h)
            post_html = page.render(enrich.get("post", {}).get(k, "") + placed(meta["slug"], f"part{k}"))
            m["sections"].append({"id": f"part{k}", "nav": navs[k - 1] if k - 1 < len(navs) else title[:22],
                                  "tag": f"Lesson &middot; part {k}", "h2": md_inline(title, page),
                                  "html": pre_html + "\n" + "\n".join(body) + "\n" + post_html})
            # added lessons (enrich["extra"]): whole sections placed after this numbered section
            for after, xid, xnav, xh2, xhtml in enrich.get("extra", []):
                if after == k:
                    m["sections"].append({"id": xid, "nav": xnav, "tag": "Lesson &middot; in practice",
                                          "h2": xh2, "html": page.render(place_after_first_para(xhtml, placed(meta["slug"], xid)))})
    for text, crit in enrich.get("skills_extra", []):
        m["skills"]["items"].append((text, crit))
    # quiz
    qa = (src / "Self-Assessment.md").read_text(encoding="utf-8")
    key = {}
    for ln in (src / "Answer Key.md").read_text(encoding="utf-8").splitlines():
        r = re.match(r"\|\s*(\d+)\s*\|\s*([A-D])\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|", ln)
        if r:
            key[int(r.group(1))] = (r.group(2), r.group(3), r.group(4))
    quiz = []
    for qm in re.finditer(r"^(\d+)\. \*\*(.+?)\*\*\s*\n((?:\s+[A-D]\. .*\n?){4})", qa, re.M):
        n = int(qm.group(1))
        opts = re.findall(r"^\s+([A-D])\. (.*?)\s*$", qm.group(3), re.M)
        if n not in key:
            err(f"{page.label}: no answer key for question {n}")
            continue
        ans, rat, obj = key[n]
        quiz.append({"stem": md_inline(qm.group(2), page), "options": [md_inline(o[1], page) for o in opts],
                     "answer": "ABCD".index(ans), "why": md_inline(rat, page), "objective": obj})
    for stem, opts, ans, why in enrich.get("quiz_extra", []):
        quiz.append({"stem": stem, "options": list(opts), "answer": ans, "why": why, "objective": ""})
    m["quiz"] = quiz
    for f in ("terms", "readings", "calcs"):
        m[f] = enrich.get(f, [])
    return m


# ───────────────────────── course loading ─────────────────────────
class Course:
    def __init__(self, pkg):
        self.pkg = pkg
        self.dir = TC / pkg
        c = load(self.dir / "course.py", f"tc_{pkg}")
        self.meta = c.COURSE
        self.hub = self.meta["hub_slug"]
        self.trainer = self.hub + "-trainer"
        sit = self.dir / "situations.py"
        self.situations = load(sit, f"tc_{pkg}_sit").SITUATIONS if sit.exists() else {}
        self.mods = []
        for row in c.MODULES:
            d = dict(row)
            d["slug"] = f"{self.hub}-{d['id']}-{d['slug']}"
            d["course"] = self
            self.mods.append(d)

    def build_mod(self, d):
        page = Page(d["slug"])
        if d.get("status") == "planned":
            return None, page
        if "src" in d:          # Markdown-sourced module
            m = parse_md_module(self.dir / "src" / d["id"], d["id"], d, page)
        else:                   # natively authored module (tools/techcourses/<pkg>/mNN.py)
            raw = load(self.dir / f"m{d['id']}.py", f"tc_{self.pkg}_m{d['id']}").MODULE
            m = dict(raw)
            m["big"] = page.render(raw.get("big", "") + placed(d["slug"], "bigpicture"))
            m["case"] = dict(raw["case"])
            m["case"]["html"] = page.render(raw["case"]["html"])
            secs = [dict(zip(("id", "nav", "h2", "html"), x)) if isinstance(x, tuple) else x for x in raw["sections"]]
            m["sections"] = [dict(x, html=page.render(place_after_first_para(x["html"], placed(d["slug"], x["id"]))),
                                  tag=x.get("tag", f"Lesson &middot; part {i}"))
                             for i, x in enumerate(secs, 1)]
            m["debrief"] = [page.render(x) for x in raw.get("debrief", [])]
            m["skills"] = dict(raw["skills"])
            m["quiz"] = [dict(zip(("stem", "options", "answer", "why"), q)) if isinstance(q, tuple) else dict(q) for q in raw["quiz"]]
            m["objectives"] = [page.render(o) for o in raw["objectives"]]
            m["image_alt"] = raw.get("image_alt", "")
        m.update({k: v for k, v in d.items() if k not in ("enrich",)})
        extra = self.situations.get(d["id"], {})          # tools/techcourses/<pkg>/situations.py
        m["scenarios"], m["tips"] = extra.get("scenarios", []), extra.get("tips", [])
        return m, page


COURSES = {}


def get_courses():
    if not COURSES:
        for p in PACKAGES:
            if (TC / p / "course.py").exists():
                COURSES[p] = Course(p)
    return COURSES


# ───────────────────────── page shell ─────────────────────────
ACADEMY_DIR = ROOT / "academy"
LANDING_MARK = "<!-- ACADEMY-LANDING: hand-maintained, not regenerated by generate_tech_courses.py -->"
ACADEMY_PAGE = "renal-care-academy.html"      # becomes academy/index.html (tools/academy/publish_academy.py)
ACADEMY_CRUMB = f'<a href="{ACADEMY_PAGE}">Renal Care Academy</a><span class="nc-sep">›</span>'


def course_crumb(C):
    """Academy crumb, plus the parent course when the track is a subtrack (course.py "parent": (href, title, blurb))."""
    p = C.get("parent")
    return ACADEMY_CRUMB + (f'<a href="{p[0]}">{p[1]}</a><span class="nc-sep">›</span>' if p else "")


def hub_crumb(C):
    """Course-home crumb: a subtrack names itself after its parent, like the Transplant Nurse pages."""
    return course_crumb(C) + (f'<span>{C["title"]}</span><span class="nc-spacer"></span>' if C.get("parent") else "")


def published(fname):
    """Carry over a page's publish stamp; finished pages live in academy/, drafts in guides/."""
    p = ACADEMY_DIR / ("index.html" if fname == ACADEMY_PAGE else fname)
    if p.exists():
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', p.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return N.existing_published(fname)


def shell(course, fname, title, desc, keywords, hero_tag, h1, sub, audience, nav, pre_main, main, glossary, related,
          body_class="", jsonld_extra=None, hero_file=None, hero_alt="", hero_html=None):
    slug = fname[:-5]
    url = f"{SITE}/guides/{slug}"
    pub = published(fname)
    pub_meta = f'\n<meta property="article:published_time" content="{pub}">' if pub else ""
    og_img = None
    for cand in (f"images/og/{slug}-vignette-hero.jpg", f"images/{slug}-vignette-hero.png",
                 f"images/og/{course.hub}-vignette-hero.jpg", f"images/{course.hub}-vignette-hero.png",
                 "images/hero-cat-dialysis.webp"):
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
        "audience": {"@type": "MedicalAudience", "audienceType": course.meta["audience_type"]},
        "about": {"@type": "MedicalSpecialty", "name": "Nephrology"},
        "isAccessibleForFree": True,
    }
    if jsonld_extra:
        ld.update(jsonld_extra)
    figure = ""
    if hero_file and (IMAGES / f"{hero_file}.png").exists():
        f = hero_file
        webp = f'<source srcset="../images/{f}.webp" type="image/webp">' if (IMAGES / f"{f}.webp").exists() else ""
        size = _img_size(IMAGES / f"{f}.png") or (2048, 2048)
        figure = f"""
      <figure class="hero-figure">
        <div class="hero-vignette">
          <picture>
            {webp}
            <img src="../images/{f}.png" alt="{html.escape(html.unescape(hero_alt))}" width="{size[0]}" height="{size[1]}" fetchpriority="high" loading="eager">
          </picture>
        </div>
      </figure>"""
    pills = "\n".join(f'<a class="nav-pill" href="#{i}">{t}</a>' for i, t in nav)
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
{N.FONTS}
<style>
/* master CSS is written here by patch_master_css.py */
</style>
<style id="nursing-course-style">{N.COURSE_CSS}</style>
<style id="tech-course-style">{TECH_CSS}</style>
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>

<body class="physician-mode single-mode{(' ' + body_class) if body_class else ''}" data-course="{course.pkg}">

<!-- ═══ SITE HEADER ═════════════════════════════ -->
{N.HEADER}

<!-- ═══ HERO ════════════════════════════════════ -->
{hero_html or f'''<div class="hero">
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
</div>'''}

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
      <p style="margin-top:8px;font-size:12px;color:var(--text-muted);font-style:italic;">{course.meta['disclaimer']}</p>
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

{N.FLOATING}
<!-- ═══ SCRIPTS ══════════════════════════════════════════════════════════ -->
<script>{N.INLINE_JS}</script>
<script src="../assets/tech-course.js" defer></script>
</body>
</html>
"""


def hours_chips(d):
    h = d.get("hours")
    if not h:
        return ""
    return (f'<span class="nc-chip">Classroom {h[0]} h</span><span class="nc-chip">Skills lab {h[1]} h</span>'
            f'<span class="nc-chip">Supervised placement {h[2]} h</span>')


def card_img(d):
    """Thumbnail for a module card: <slug>-card.webp, else a named site image."""
    for f in (f"{d['slug']}-card.webp", d.get("card_img", "")):
        if f and (IMAGES / f).exists():
            return f'<img class="tc-mod-img nc-fig-img" src="../images/{f}" alt="" loading="lazy" decoding="async" width="640" height="360">'
    return ""


def live_mods(course):
    """Modules that are published (rows without status "planned")."""
    return [d for d in course.mods if d.get("status") != "planned"]


def tier_chip(d):
    """Optional tier label on a module (course rows may set "tier")."""
    return f'<span class="nc-chip nc-chip-tier">{d["tier"]}</span>' if d.get("tier") else ""


def grid_html(course, cards):
    """Module cards for a hub. Courses whose rows set "part" get one grid per part, under a heading."""
    if not any(d.get("part") for d in course.mods):
        return '  <div class="nc-modgrid" id="nc-modules">\n' + "\n".join(cards) + "\n  </div>"
    out, cur, first = [], None, True
    for d, card in zip(course.mods, cards):
        if d.get("part") != cur:
            if cur is not None:
                out.append("  </div>")
            cur = d.get("part")
            out.append(f'  <h3 class="tc-part">{cur}</h3>')
            out.append('  <div class="nc-modgrid"' + (' id="nc-modules"' if first else "") + ">")
            first = False
        out.append(card)
    out.append("  </div>")
    return "\n".join(out)


# ───────────────────────── module page ─────────────────────────
def build_module(course, d, built):
    m, page = built
    C = course.meta
    fname = d["slug"] + ".html"
    n = int(d["id"])
    live = [x for x in course.mods if x.get("status") != "planned"]
    i = live.index(d)
    prev_m = live[i - 1] if i > 0 else None
    next_m = live[i + 1] if i < len(live) - 1 else None
    hub = course.hub + ".html"
    parts = []
    obj = "\n".join(f"    <li>{o}</li>" for o in m["objectives"])
    parts.append(f"""<section class="section" id="objectives">
  <div class="section-tag">Learning objectives</div>
  <h2>After this module you should be able to</h2>
  <ul class="nc-obj">
{obj}
  </ul>
  <div class="tc-hours">{hours_chips(d)}</div>
  <div class="tc-keyp"><span class="tc-lab">Pre-test</span>Before you read, <a href="#quiz">answer the {min(C.get("draw", 5), len(m["quiz"]))} self-assessment questions</a> and note your score. After the module, select <strong>New set of questions</strong> and compare. The difference is what you learned; the questions you still miss are what to reread.</div>
</section>""")
    if m.get("big"):
        parts.append(f"""<section class="section" id="bigpicture">
  <div class="section-tag">Start here</div>
  <h2>The big picture, in plain words</h2>
{m['big']}
</section>""")
    c = m["case"]
    qs = "\n".join(f"    <li>{q}</li>" for q in c.get("questions", []))
    parts.append(f"""<section class="section" id="case">
  <div class="section-tag">Opening case &middot; fictional</div>
  <h2>Case: {c['title']}</h2>
  <div class="nc-case">
{c['html'].strip()}
  </div>
  <p><strong>Before reading on, decide:</strong></p>
  <ul class="tc-q-list">
{qs}
  </ul>
  <p>Keep your answers in mind. The lesson gives you what you need, and the case review near the end shows one sound response.</p>
</section>""")
    for s in m["sections"]:
        parts.append(f"""<section class="section" id="{s['id']}">
  <div class="section-tag">{s['tag']}</div>
  <h2>{s['h2']}</h2>
{s['html'].strip()}
</section>""")
    if m.get("scenarios"):
        sc = []
        for title, see, think, do, why in m["scenarios"]:
            sc.append(f"""  <article class="tc-sit">
    <h3>{title}</h3>
    <dl>
      <dt>What you see</dt><dd>{see}</dd>
      <dt>What is likely going on</dt><dd>{think}</dd>
      <dt class="tc-sit-do">What to do</dt><dd>{do}</dd>
      <dt>Why it matters</dt><dd>{why}</dd>
    </dl>
  </article>""")
        tips = ""
        if m.get("tips"):
            tips = ('\n  <div class="tc-keyp"><span class="tc-lab">Field notes</span><ul class="tc-tips">'
                    + "".join(f"<li>{t}</li>" for t in m["tips"]) + "</ul></div>")
        parts.append(f"""<section class="section" id="situations">
  <div class="section-tag">On the floor</div>
  <h2>Real situations: problems and solutions</h2>
  <p>These are fictional but typical. For each one, cover the answer, decide what you would do, then compare. Where a step depends on local rules, your unit&rsquo;s procedure and your supervisor&rsquo;s direction come first.</p>
  <div class="tc-sits">
{chr(10).join(sc)}
  </div>{tips}
</section>""")
    if m.get("debrief"):
        parts.append(f"""<section class="section" id="debrief">
  <div class="section-tag">Case review</div>
  <h2>Back to the case: {c['title']}</h2>
{chr(10).join(m['debrief'])}
</section>""")
    sk = m["skills"]
    items = "\n".join(f"    <li>{CRIT if crit else ''}{t}</li>" for t, crit in sk["items"])
    placement = f'\n  <div class="nc-task"><strong>Placement activity.</strong> {sk["placement"]}</div>' if sk.get("placement") else ""
    if sk["items"]:
        parts.append(f"""<section class="section" id="skills">
  <div class="section-tag">Skills lab &middot; with your preceptor</div>
  <h2>Skills checklist: {sk['title']}</h2>
  <p>{sk.get('intro', '').strip()} Your preceptor rates each step as satisfactory, needs practice, or not observed. Steps marked <span class="tc-crit">Critical</span> must all be satisfactory before sign-off. This checklist supports supervised learning; your unit&rsquo;s own procedure and competency form are the authority. A printable version of every checklist is on the <a href="{course.trainer}.html#checklists">trainer page</a>.</p>
  <ul class="nc-check">
{items}
  </ul>{placement}
</section>""")
    # quiz (one explanation per question, shown under the best answer)
    bank = m["quiz"]
    draw = min(C.get("draw", 5), len(bank))
    qh = []
    for qi, q in enumerate(bank, 1):
        if len(q["options"]) != 4:
            err(f"{d['slug']} question {qi}: expected 4 options")
        opts = []
        for oi, text in enumerate(q["options"]):
            oid = f"q{qi}{'abcd'[oi]}"
            correct = oi == q["answer"]
            rat = f'<div class="nc-rat" hidden>{q["why"]}</div>' if correct else ""
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if correct else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{text}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span>{rat}</div>
    </div>""")
        qh.append(f"""  <fieldset class="nc-q" data-q="{qi}">
    <legend><span class="nc-qn">Question {qi} of {len(bank)}</span>{q['stem']}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    parts.append(f"""<section class="section" id="quiz">
  <div class="section-tag">Self-assessment</div>
  <h2>Check your understanding</h2>
  <p>Each visit draws {draw} questions at random from this module&rsquo;s {len(bank)}-question bank. Choose the single best answer for each, then select <strong>Check answers</strong>; an explanation appears under the best answer. Select <strong>New set of questions</strong> for a different mix. A good target is {C.get('mastery', '4 of 5')} on two different sets. Nothing you select is sent anywhere; scoring happens in your browser.</p>
  <form class="nc-quiz" id="nc-quiz" data-module="{d['id']}" data-draw="{draw}" novalidate>
{chr(10).join(qh)}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my self-assessment result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
</section>""")
    rd = []
    for f, why in m.get("readings", []):
        meta = N.page_meta(f)
        if not meta:
            err(f"{d['slug']}: assigned reading not found: guides/{f}")
            continue
        rd.append(f'    <li><a href="{f}">{SHARED.READING_TITLES.get(f) or html.escape(meta[0], quote=False)}</a><span>{why}</span></li>')
    calc = []
    for f in m.get("calcs", []):
        base, _, anchor = f.partition("#")
        meta = N.page_meta(base)
        if not meta:
            err(f"{d['slug']}: calculator not found: guides/{f}")
            continue
        ctitle, cdesc = SHARED.CALCS.get(f) or N.D.CALCS.get(f) or (html.escape(meta[0], quote=False), "")
        if anchor and f not in SHARED.CALCS:      # one tool inside a multi-calculator page: title it from its own heading
            mh = re.search(r'<section class="calc" id="' + re.escape(anchor) + r'"[^>]*>\s*<h2[^>]*>(.*?)</h2>',
                           (GUIDES / base).read_text(encoding="utf-8"), re.S)
            if not mh:
                err(f"{d['slug']}: calculator anchor not found: guides/{f}")
                continue
            ctitle, cdesc = re.sub(r"<[^>]+>", "", mh.group(1)).strip(), html.escape(meta[0], quote=False)
        calc.append(f"""  <a href="{f}" class="calc-card">
    <div class="calc-card-icon">⌬</div>
    <div class="calc-card-body">
      <div class="calc-card-title">{ctitle}</div>
      <div class="calc-card-desc">{cdesc}</div>
    </div>
    <span class="calc-card-arrow">Open →</span>
  </a>""")
    calc_html = ('<div class="calc-cards-wrap">\n  <div class="calc-cards-label">Calculators for this module</div>\n'
                 + "\n".join(calc) + "\n</div>") if calc else ""
    np = []
    np.append(f'<a class="nc-np" href="{prev_m["slug"]}.html"><small>← Previous &middot; Module {int(prev_m["id"])}</small>{prev_m["title"]}</a>'
              if prev_m else f'<a class="nc-np" href="{hub}"><small>← Course home</small>{C["title"]}</a>')
    np.append(f'<a class="nc-np nc-np-next" href="{next_m["slug"]}.html"><small>Next &middot; Module {int(next_m["id"])} →</small>{next_m["title"]}</a>'
              if next_m else f'<a class="nc-np nc-np-next" href="{hub}"><small>Series complete →</small>Back to the course home</a>')
    rd_html = f'  <ul class="nc-read">\n{chr(10).join(rd)}\n  </ul>' if rd else ""
    parts.append(f"""<section class="section" id="reading">
  <div class="section-tag">Go deeper</div>
  <h2>Read next on this site</h2>
{rd_html}
{calc_html}
  <div class="nc-nextprev">
    {np[0]}
    {np[1]}
  </div>
</section>""")
    main = N.auto_expand("\n\n".join(parts), fname)
    total = len(course.mods)
    pre = f"""<div class="container">
  <div class="nc-bar">
    {course_crumb(C)}<a href="{hub}">{C['title']}</a><span class="nc-sep">›</span><span>Module {n} of {total}</span>
    <span class="nc-spacer"></span>
    <span class="nc-chip nc-chip-core">{C['label']}</span>{tier_chip(d)}
  </div>
  <div class="alert alert-teal">
    <div class="alert-icon">{C.get('icon', '🛠️')}</div>
    <div class="alert-body">
      <h4>{C['label']}</h4>
      <p>{C['scope_note']}</p>
    </div>
  </div>
</div>"""
    nav = [("objectives", "Objectives")] + ([("bigpicture", "Big picture")] if m.get("big") else []) + [("case", "Case")] + \
          [(s["id"], s["nav"]) for s in m["sections"]] + ([("situations", "Real situations")] if m.get("scenarios") else []) + \
          ([("debrief", "Case review")] if m.get("debrief") else []) + \
          ([("skills", "Skills checklist")] if m["skills"]["items"] else []) + [("quiz", "Self-assessment"), ("reading", "Go deeper")]
    cards = [(hub, "Course home", C["title"], f"Syllabus and all {total} modules.")]
    if next_m:
        cards.append((next_m["slug"] + ".html", "Next module", next_m["title"], next_m["sub"].split(". ")[0].rstrip(".") + "."))
    if prev_m:
        cards.append((prev_m["slug"] + ".html", "Previous module", prev_m["title"], prev_m["sub"].split(". ")[0].rstrip(".") + "."))
    for f, why in m.get("readings", [])[:3]:
        meta = N.page_meta(f)
        if meta:
            cards.append((f, "Go deeper", SHARED.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    title = f"{d['title']}: {C['short']} Module {n}"
    desc = d.get("desc") or f"Module {n} of the {C['title']} study series: {html.unescape(d['sub'])}"
    pg = shell(course, fname, title, desc[:300], d.get("keywords", C["keywords"]),
               f"{C['tag']} &middot; Module {n} of {total}", d["title"], d["sub"], C["audience"],
               nav, pre, main, glossary(main, m.get("terms", [])), N.related_block(cards),
               jsonld_extra={"isPartOf": {"@type": "Course", "name": C["title"], "url": f"{SITE}/guides/{course.hub}"},
                             "learningResourceType": "Study module with case, skills checklist and self-assessment",
                             "lastReviewed": C["review_date"]},
               hero_file=d.get("hero_file") or d["slug"] + "-vignette-hero", hero_alt=HERO_ALT.get(d["slug"]) or m.get("image_alt") or d["title"])
    (GUIDES / fname).write_text(N.merge_cites(pg), encoding="utf-8")
    return fname, page.refs


def glossary(body_html, terms):
    """Abbreviations found on the page plus the module's plain-language terms."""
    used = N.abbr_used(body_html)
    dt = 'style="font-weight:700;color:var(--text);"'
    rows = []
    for tok in used:
        exp, note = N.ABBR[tok]
        rows.append(f'    <dt {dt}>{tok}</dt><dd style="margin:0;">{exp[0].upper() + exp[1:]}{"." if not note else " &mdash; " + note}</dd>')
    trows = [f'    <dt {dt}>{t}</dt><dd style="margin:0;">{x}</dd>' for t, x in terms]
    h4 = ('<h4 style="font-family:Inter,system-ui,sans-serif;font-size:13px;font-weight:700;letter-spacing:.04em;'
          'text-transform:uppercase;color:var(--text-muted);margin:8px 0 4px;">')
    dl = '<dl style="display:grid;grid-template-columns:max-content 1fr;column-gap:14px;row-gap:4px;margin:0 0 16px;">'
    a_html = f"  {h4}Abbreviations</h4>\n  {dl}\n" + "\n".join(rows) + "\n  </dl>\n" if rows else ""
    t_html = f"  {h4}Terms in plain words</h4>\n  {dl}\n" + "\n".join(trows) + "\n  </dl>\n" if trows else ""
    if not (rows or trows):
        return ""
    return f"""<!-- GLOSSARY-START -->
<section class="glossary-section" style="max-width:860px;margin:8px auto 0;padding:0 32px;">
<details class="glossary-acc" style="border:1px solid var(--border);border-radius:12px;background:var(--white);overflow:hidden;">
<summary style="cursor:pointer;list-style:none;padding:15px 20px;font-family:Inter,system-ui,sans-serif;font-weight:600;font-size:15px;color:var(--text);display:flex;align-items:center;gap:10px;">
<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;color:var(--teal);"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
<span data-lang="en">Glossary &amp; abbreviations</span><span class="lang-hidden" data-lang="tl">Talahulugan at mga daglat</span><span class="lang-hidden" data-lang="ceb">Talaan sa mga pulong ug daglat</span><span class="lang-hidden" data-lang="kap">Talatinigan ampo reng daglat</span>
<span style="margin-left:auto;font-weight:500;font-size:12px;color:var(--text-muted);">terms used on this page</span>
</summary>
<div style="padding:6px 26px 20px 26px;font-size:13.5px;line-height:1.7;color:var(--text-mid);">
{a_html}{t_html}</div>
</details>
</section>
<!-- GLOSSARY-END -->"""


# ───────────────────────── hub page ─────────────────────────
def branches_html(current):
    out = []
    for pkg, c in get_courses().items():
        M = c.meta
        if M.get("no_branch") and c is not current:
            continue
        img = ""
        f = M.get("branch_img", "")
        if f and (IMAGES / f).exists():
            img = f'<img class="nc-fig-img" src="../images/{f}" alt="" loading="lazy" decoding="async" width="640" height="360">'
        cur = ' aria-current="page"' if c is current else ""
        out.append(f"""    <a class="tc-branch" href="{c.hub}.html"{cur}>{img}
      <span class="tc-branch-body"><small>{M['branch_role']}</small><b>{M['title']}</b><span>{M['branch_blurb']}</span></span>
    </a>""")
    return '<div class="tc-branches">\n' + "\n".join(out) + "\n  </div>"


def pathways_section(course, page):
    """Hub section after "Start here": the technician career pathways, or a course's own section."""
    C = course.meta
    if C.get("pathways_html"):
        return (f'<section class="section" id="pathways">\n  <div class="section-tag">{C.get("pathways_tag", "Pathways")}</div>\n'
                f'  <h2>{C.get("pathways_h2", "How the series is organized")}</h2>\n{page.render(C["pathways_html"])}\n</section>')
    return f"""<section class="section" id="pathways">
  <div class="section-tag">Renal Technicians</div>
  <h2>One foundation, three technical roles</h2>
  <p>A dialysis unit depends on three kinds of technical staff, grouped in the Academy as Renal Technicians. Most people start at the chairside as a dialysis technician. From there, two specialist branches open up: the water room and the workshop. The three study series share the same format, so you can move between them.</p>
  {branches_html(course)}
{page.render(C.get('pathway_note', ''))}
</section>"""


def build_hub(course, built):
    C = course.meta
    fname = course.hub + ".html"
    page = Page(fname)
    cards, syl = [], []
    has_hours = any(d.get("hours") for d in course.mods)
    for d in course.mods:
        m = built[d["id"]][0]
        n = int(d["id"])
        if m is None:
            cards.append(f"""    <div class="nc-mod tc-mod tc-soon">{card_img(d)}
      <span class="tc-mod-body"><span class="nc-mod-top"><span>Module {n}</span>{tier_chip(d)}<span class="nc-chip">In preparation</span></span>
      <span class="nc-mod-title">{d['title']}</span>
      <span class="nc-mod-desc">{d['sub']}</span></span>
    </div>""")
            syl.append(f"<tr><td>{n}</td><td>{d['title']}</td><td></td><td>{d.get('case_title', '—')}</td><td>In preparation</td><td></td></tr>")
            continue
        cards.append(f"""    <a class="nc-mod tc-mod" href="{d['slug']}.html" data-module="{d['id']}">{card_img(d)}
      <span class="tc-mod-body"><span class="nc-mod-top"><span>Module {n}</span>{tier_chip(d)}</span>
      <span class="nc-mod-title">{d['title']}</span>
      <span class="nc-mod-desc">{d['sub']}</span>
      <span class="nc-mod-status" aria-live="off"></span></span>
    </a>""")
        h = d.get("hours")
        hrs = f"<td>{h[0]}</td><td>{h[1]}</td><td>{h[2]}</td>" if has_hours and h else ("<td>—</td><td>—</td><td>—</td>" if has_hours else "")
        lessons = "".join(f"<li>{x['h2']}</li>" for x in m["sections"])
        nsit = len(m.get("scenarios") or [])
        extras = f"{len(m['quiz'])} questions" + (f" &middot; {nsit} real situations" if nsit else "")
        syl.append(f"<tr><td>{n}</td><td><a href=\"{d['slug']}.html\">{d['title']}</a></td>"
                   f"<td><ol class=\"tc-syl-lessons\">{lessons}</ol></td><td>{m['case']['title']}</td>"
                   f"<td>{m['skills']['title'] or 'Five practical stations'}</td><td>{extras}</td>{hrs}</tr>")
    if has_hours:
        tot = [sum(d["hours"][k] for d in course.mods if d.get("hours")) for k in range(3)]
        syl.append(f"<tr><td></td><td><strong>Total</strong></td><td></td><td></td><td></td><td></td><td><strong>{tot[0]}</strong></td><td><strong>{tot[1]}</strong></td><td><strong>{tot[2]}</strong></td></tr>")
    hrs_head = "<th>Classroom (h)</th><th>Skills lab (h)</th><th>Placement (h)</th>" if has_hours else ""
    live_n = sum(1 for d in course.mods if built[d["id"]][0] is not None)
    main = f"""<section class="section" id="start">
  <div class="section-tag">Start here</div>
  <h2>{C['start_h2']}</h2>
{page.render(C['start_html'])}
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>What this series is, and is not</h4>
      <p>{page.render(C['is_not'])}</p>
    </div>
  </div>
</section>

{pathways_section(course, page)}

<section class="section" id="modules">
  <div class="section-tag">Modules</div>
  <h2>{C['modules_h2']}</h2>
  <p>{C['modules_intro']}</p>
  <div class="nc-progress" id="nc-progress" hidden><span class="nc-progress-text"></span><button type="button" class="nc-btn nc-btn-ghost">Clear saved progress</button></div>
{grid_html(course, cards)}
</section>

<section class="section" id="how">
  <div class="section-tag">How each module works</div>
  <h2>The same seven steps every time</h2>
{page.render(SHARED.HOW_HTML)}
</section>

<section class="section" id="syllabus">
  <div class="section-tag">Syllabus</div>
  <h2>The series at a glance</h2>
  <p>{C['syllabus_note']}</p>
  <div class="table-wrap"><table>
  <thead><tr><th>No.</th><th>Module</th><th>Lessons</th><th>Opening case</th><th>Skills checklist</th><th>Practice</th>{hrs_head}</tr></thead>
  <tbody>
{chr(10).join(syl)}
  </tbody></table></div>
</section>

<section class="section" id="assessment">
  <div class="section-tag">Assessment</div>
  <h2>Self-assessment is not sign-off</h2>
{page.render(C['assessment_html'])}
  <p><strong>End-of-course examination.</strong> When you have finished every module, take the <a href="{course.hub}-final-exam.html">end-of-course examination</a>. It draws questions at random from all {len(live_mods(course))} modules, so no two sittings are the same.</p>
</section>

<section class="section" id="sources">
  <div class="section-tag">Curriculum sources</div>
  <h2>What the series is built on</h2>
{page.render(C['sources_html'])}
</section>

<section class="section" id="trainers">
  <div class="section-tag">For trainers and preceptors</div>
  <h2>Using the series in a training program</h2>
  <p>{C.get('trainers_intro', 'A head nurse, chief technician, or training provider can use these modules as the guided-study part of a supervised program. ')}The <a href="{course.trainer}.html">trainer and preceptor page</a> gathers the proposed hours, completion criteria, and every skills checklist in one printable place. These are proposals for a provider to adapt and validate on its own equipment; they are not requirements of any regulator.</p>
</section>"""
    nav = [("start", "Start here"), ("pathways", C.get("pathways_nav", "Career pathways")), ("modules", "Modules"), ("how", "How it works"),
           ("syllabus", "Syllabus"), ("assessment", "Assessment"), ("sources", "Sources"), ("trainers", "For trainers")]
    # optional extra course-home sections (course.py HUB_SECTIONS): each is placed before an existing section id
    for x in C.get("hub_sections", []):
        block = (f'<section class="section" id="{x["id"]}">\n  <div class="section-tag">{x["tag"]}</div>\n'
                 f'  <h2>{x["h2"]}</h2>\n{page.render(x["html"])}\n</section>\n\n')
        anchor = f'<section class="section" id="{x["before"]}">'
        if anchor not in main:
            err(f"{fname}: hub section {x['id']} has unknown 'before' id {x['before']}")
            continue
        main = main.replace(anchor, block + anchor, 1)
        ids = [i for i, _ in nav]
        nav.insert(ids.index(x["before"]) if x["before"] in ids else len(nav), (x["id"], x["nav"]))
    main = N.auto_expand(main, fname)
    live = [d for d in course.mods if built[d["id"]][0] is not None]
    rel = [(live[0]["slug"] + ".html", "Module 1", live[0]["title"], "Begin here.")] if live else []
    if C.get("parent"):
        rel.insert(0, (C["parent"][0], "Parent course", C["parent"][1], C["parent"][2]))
    rel.append((course.trainer + ".html", "Trainers", "Trainer and Preceptor Resource", "Hours, completion criteria, and printable checklists."))
    rel.append((course.hub + "-final-exam.html", "Examination", "End-of-Course Examination", "Questions drawn at random from every module."))
    for pkg, c in get_courses().items():
        if c is not course:
            rel.append((c.hub + ".html", "Related series", c.meta["title"], c.meta["branch_blurb"]))
    for f, why in C.get("related", []):
        meta = N.page_meta(f)
        if meta:
            rel.append((f, "Related guide", SHARED.READING_TITLES.get(f) or html.escape(meta[0], quote=False), why))
    pre = f"""<div class="container">
  <div class="nc-bar">{hub_crumb(C)}<span class="nc-chip nc-chip-core">{C['label']}</span><span class="nc-chip">{len(course.mods)} modules</span><span class="nc-chip">Free &middot; no account</span><span class="nc-chip">English</span></div>
</div>"""
    pg = shell(course, fname, C["page_title"], C["desc"], C["keywords"], f"{C['tag']} &middot; Course home", C["h1"], C["sub"],
               C["audience"], nav, pre, main,
               glossary(main, [("Preceptor", "An experienced staff member who supervises a learner at work and judges whether a skill was done safely."),
                               ("Competency sign-off", "A written record that a preceptor watched you perform a skill correctly on the unit&rsquo;s own equipment."),
                               ("Scope of practice", "The tasks you are trained, assigned, and legally allowed to do in your role.")]),
               N.related_block(rel),
               jsonld_extra={"@type": ["MedicalWebPage", "Course"], "description": C["desc"],
                             "provider": {"@type": "Organization", "name": "Renal Care Matters", "url": SITE + "/"},
                             "educationalLevel": C["level"], "numberOfCredits": 0,
                             "hasPart": [{"@type": "LearningResource", "name": d["title"], "url": f"{SITE}/guides/{d['slug']}"} for d in live]},
               hero_file=C.get("hero_file") or course.hub + "-vignette-hero", hero_alt=C.get("hero_alt", C["title"]))
    (GUIDES / fname).write_text(N.merge_cites(pg), encoding="utf-8")
    return fname, page.refs


# ───────────────────────── end-of-course examination ─────────────────────────
def build_exam(course, built):
    C = course.meta
    fname = course.hub + "-final-exam.html"
    page = Page(fname)
    bank, rows = [], []
    for d in course.mods:
        m = built[d["id"]][0]
        if m is None:
            continue
        rows.append(f'<tr><td>{int(d["id"])}</td><td><a href="{d["slug"]}.html">{d["title"]}</a></td><td>{len(m["quiz"])}</td></tr>')
        for q in m["quiz"]:
            bank.append((d, q))
    draw = min(C.get("exam_draw", 30), len(bank))
    passmark = -(-draw * 8 // 10)
    qh = []
    for qi, (d, q) in enumerate(bank, 1):
        opts = []
        for oi, text in enumerate(q["options"]):
            oid = f"q{qi}{'abcd'[oi]}"
            correct = oi == q["answer"]
            rat = (f'<div class="nc-rat" hidden>{q["why"]} <a href="{d["slug"]}.html">Module {int(d["id"])}</a>.</div>'
                   if correct else "")
            opts.append(f"""    <div class="nc-opt">
      <div class="nc-opt-row"><input type="radio" name="q{qi}" id="{oid}" value="{'abcd'[oi]}" data-correct="{1 if correct else 0}" aria-describedby="{oid}-fb"><label for="{oid}">{text}</label></div>
      <div id="{oid}-fb"><span class="nc-verdict"></span>{rat}</div>
    </div>""")
        qh.append(f"""  <fieldset class="nc-q" data-q="{qi}">
    <legend><span class="nc-qn">Question {qi}</span>{q['stem']}</legend>
{chr(10).join(opts)}
  </fieldset>""")
    main = f"""<section class="section" id="about">
  <div class="section-tag">Before you begin</div>
  <h2>How this examination works</h2>
  <p>This examination covers the whole {C['title']} series. Each sitting draws <strong>{draw} questions at random</strong> from a bank of {len(bank)}, in random order, with the answer choices shuffled. Choose the single best answer for each question, then select <strong>Check answers</strong>.</p>
  <div class="tc-cards">
    <div class="tc-card"><b>When to take it</b>After you have finished every module and reviewed the questions you missed.</div>
    <div class="tc-card"><b>How to take it</b>In one sitting, without notes. Allow about one minute per question.</div>
    <div class="tc-card"><b>Proposed pass mark</b>{passmark} of {draw} best answers (80 percent). Your trainer may set a different mark.</div>
    <div class="tc-card"><b>If you fall short</b>Each explanation names its module. Reread those modules, then select <strong>New set of questions</strong>.</div>
  </div>
  <div class="tc-stop"><span class="tc-lab">What a pass means</span>A pass shows that you know the material. It does not show that you can do the work. Competence is demonstrated on your unit&rsquo;s own equipment and signed off by a preceptor.</div>
  <div class="table-wrap"><table>
  <thead><tr><th>No.</th><th>Module</th><th>Questions in the bank</th></tr></thead>
  <tbody>
{chr(10).join(rows)}
<tr><td></td><td><strong>Total</strong></td><td><strong>{len(bank)}</strong></td></tr>
  </tbody></table></div>
</section>

<section class="section" id="quiz">
  <div class="section-tag">Examination</div>
  <h2>End-of-course examination</h2>
  <form class="nc-quiz" id="nc-quiz" data-module="exam" data-draw="{draw}" novalidate>
{chr(10).join(qh)}
    <label class="nc-remember"><input type="checkbox" id="nc-remember"><span>Remember my result on this device (optional). Stored only in this browser; untick to erase it.</span></label>
    <div class="nc-actions">
      <button type="submit" class="nc-btn">Check answers</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-retry hidden>Try these again</button>
      <button type="button" class="nc-btn nc-btn-ghost" data-nc-newset>New set of questions</button>
    </div>
    <div class="nc-result" id="nc-result" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
</section>"""
    main = N.auto_expand(main, fname)
    nav = [("about", "Before you begin"), ("quiz", "Examination")]
    rel = [(course.hub + ".html", "Course home", C["title"], "Syllabus and all modules."),
           (course.trainer + ".html", "Trainers", "Trainer and Preceptor Resource", "Completion criteria and printable checklists.")]
    pre = f"""<div class="container">
  <div class="nc-bar">{course_crumb(C)}<a href="{course.hub}.html">{C['title']}</a><span class="nc-sep">›</span><span>End-of-course examination</span></div>
</div>"""
    title = f"{C['title']}: End-of-Course Examination"
    desc = (f"A randomized end-of-course examination for the {C['title']} study series on Renal Care Matters: "
            f"{draw} questions drawn from a bank of {len(bank)}, with an explanation for every best answer.")
    pg = shell(course, fname, title, desc, C["keywords"], f"{C['tag']} &middot; Examination", "End-of-Course <em>Examination</em>",
               f"{draw} questions drawn at random from all {len(rows)} modules of the {C['title']} series.",
               C["audience"], nav, pre, main, glossary(main, []), N.related_block(rel))
    (GUIDES / fname).write_text(pg, encoding="utf-8")
    return fname, page.refs


# ───────────────────────── trainer page ─────────────────────────
def build_trainer(course, built):
    C = course.meta
    fname = course.trainer + ".html"
    page = Page(fname)
    blocks = []
    for d in course.mods:
        m = built[d["id"]][0]
        if m is None:
            continue
        sk = m["skills"]
        if not sk["items"]:
            continue
        rows = "\n".join(f"<tr><td>{CRIT if crit else ''}{t}</td><td></td><td></td><td></td></tr>" for t, crit in sk["items"])
        blocks.append(f"""  <h3 class="nc-print-break">Module {int(d['id'])}: {d['title']}</h3>
  <p><strong>{sk['title']}.</strong> {sk.get('intro', '').strip()}</p>
  <div class="table-wrap"><table class="nc-sign">
  <thead><tr><th>Observable step</th><th>Satisfactory</th><th>Needs practice</th><th>Not observed</th></tr></thead>
  <tbody>
{rows}
  </tbody></table></div>
  <p>Learner ____________________ &nbsp; Preceptor ____________________ &nbsp; Date __________</p>""")
    main = f"""<section class="section" id="program">
  <div class="section-tag">Program design</div>
  <h2>{C['trainer_h2']}</h2>
{page.render(C['trainer_html'])}
</section>

<section class="section" id="completion">
  <div class="section-tag">Completion</div>
  <h2>Proposed completion criteria</h2>
{page.render(C['completion_html'])}
  <p><strong>Written examination.</strong> The <a href="{course.hub}-final-exam.html">end-of-course examination</a> draws {C.get("exam_draw", 30)} questions at random from the question banks of all modules. A proposed pass mark is 80 percent, with missed questions reviewed against their modules before a second sitting. For a supervised sitting, the learner takes it on a unit device with the preceptor present and the preceptor records the score.</p>
</section>

<section class="section" id="checklists">
  <div class="section-tag">Printable</div>
  <h2>Skills checklists for every module</h2>
  <p>Print this page for a full set. Each checklist starts on a new sheet. Steps marked <span class="tc-crit">Critical</span> must all be satisfactory before sign-off; a missed critical step is repeated with the preceptor. Replace any step that does not match your equipment or approved procedure.</p>
{chr(10).join(blocks)}
</section>"""
    main = N.auto_expand(main, fname)
    nav = [("program", "Program design"), ("completion", "Completion"), ("checklists", "Checklists")]
    rel = [(course.hub + ".html", "Course home", C["title"], "Syllabus and all modules."),
           ("dialysis-qapi-vs-cqi.html", "Related guide", "Dialysis Center Quality Management", "Where staff training fits in the unit quality program.")]
    pre = f"""<div class="container">
  <div class="nc-bar">{course_crumb(C)}<a href="{course.hub}.html">{C['title']}</a><span class="nc-sep">›</span><span>Trainer and preceptor resource</span></div>
</div>"""
    title = f"{C['title']}: Trainer and Preceptor Resource"
    desc = f"Proposed program hours, completion criteria, and printable skills checklists for the {C['title']} study series on Renal Care Matters."
    pg = shell(course, fname, title, desc, C["keywords"], f"{C['tag']} &middot; For trainers", "Trainer and Preceptor <em>Resource</em>",
               f"Program structure, completion criteria, and printable skills checklists for the {C['title']} series.",
               C.get("trainer_audience", "Head nurses, chief technicians, educators, and preceptors"), nav, pre, main, glossary(main, []), N.related_block(rel),
               body_class="nc-educator")
    (GUIDES / fname).write_text(N.merge_cites(pg), encoding="utf-8")
    return fname, page.refs


# ───────────────────────── academy landing page ─────────────────────────
class _Academy:
    pkg, hub = "academy", "renal-care-academy"
    meta = {"audience_type": "Dialysis and nephrology staff",
            "disclaimer": ("Educational study material for kidney care staff. Does not replace physician orders, approved unit procedures, "
                           "manufacturer instructions, regulatory requirements, or supervised training.")}


# ───────────────────────── Academy landing hero ─────────────────────────
# Same family as the Calculators and Drug Index heroes: an animated color wash, a chip tag, the title, a short
# subtitle and stat chips, with training words and study icons drifting behind the copy. Styles and script live
# inside the hero block, so patch_master_css.py (first <style> only) never touches them.
ACADEMY_HERO_CSS = r"""
body .hero.acad-hero{position:relative;overflow:hidden;padding:56px 0 48px;
  background:linear-gradient(135deg,#dcefe8 0%,#eef7f2 46%,#f5efdc 100%) !important;background-size:240% 240% !important;
  color:#24504a !important;animation:acad-shift 26s ease-in-out infinite alternate;}
html[data-theme="dark"] body .hero.acad-hero{background:linear-gradient(135deg,#0c2624 0%,#15403b 48%,#2a2a14 100%) !important;color:rgba(232,246,241,.88) !important;}
@keyframes acad-shift{0%{background-position:0% 0%;}50%{background-position:85% 40%;}100%{background-position:100% 100%;}}
.acad-hero::before,.acad-hero::after{display:none !important;}
.acad-hero > .container{position:relative;z-index:2;}
.acad-hero .hero-tag{display:inline-block;color:#1d5a52 !important;border:1px solid rgba(26,107,114,.38) !important;background:rgba(255,255,255,.55);}
.acad-hero h1{color:#123a36 !important;margin:14px 0 10px;}
.acad-hero h1 em{color:#8a5f00 !important;font-style:italic;}
.acad-hero .hero-sub{color:#2f5752 !important;max-width:640px;}
.acad-stats{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 0;}
.acad-stat{display:inline-flex;align-items:baseline;gap:6px;padding:6px 12px;border-radius:999px;font-size:.84rem;
  background:rgba(255,255,255,.62);border:1px solid rgba(26,107,114,.22);color:#24504a;}
.acad-stat b{font-family:'Inter',sans-serif;font-size:1rem;color:#123a36;}
.acad-tracks{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:18px 0 0;}
@media (max-width:900px){.acad-tracks{grid-template-columns:1fr 1fr;}}
.acad-track{display:flex;align-items:center;gap:10px;padding:11px 14px;border-radius:12px;text-decoration:none !important;
  background:rgba(255,255,255,.72);border:1px solid rgba(26,107,114,.2);color:#123a36 !important;
  box-shadow:0 2px 10px rgba(18,58,54,.06);transition:transform .2s,box-shadow .2s,background .2s;}
.acad-track:hover{transform:translateY(-2px);background:#fff;box-shadow:0 8px 22px rgba(18,58,54,.14);}
.acad-track-ico{flex:0 0 34px;height:34px;border-radius:9px;display:flex;align-items:center;justify-content:center;background:#1a6b72;color:#fff;}
.acad-track-ico svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;}
.acad-track-t{display:flex;flex-direction:column;line-height:1.3;min-width:0;}
.acad-track-t strong{font-size:.9rem;}
.acad-track-t small{font-size:.76rem;color:#3d635e;}
html[data-theme="dark"] .acad-hero .hero-tag{color:rgba(232,246,241,.92) !important;border-color:rgba(127,214,196,.42) !important;background:rgba(255,255,255,.06);}
html[data-theme="dark"] .acad-hero h1{color:#fff !important;}
html[data-theme="dark"] .acad-hero h1 em{color:#e6bf62 !important;}
html[data-theme="dark"] .acad-hero .hero-sub{color:rgba(232,246,241,.84) !important;}
html[data-theme="dark"] .acad-stat{background:rgba(255,255,255,.07);border-color:rgba(127,214,196,.25);color:rgba(232,246,241,.86);}
html[data-theme="dark"] .acad-stat b{color:#fff;}
html[data-theme="dark"] .acad-track{background:rgba(255,255,255,.07);border-color:rgba(127,214,196,.22);color:#fff !important;box-shadow:none;}
html[data-theme="dark"] .acad-track:hover{background:rgba(255,255,255,.13);}
html[data-theme="dark"] .acad-track-ico{background:#0e4a50;}
html[data-theme="dark"] .acad-track-t small{color:rgba(232,246,241,.74);}
/* floating layer: training words drift across, study icons rise */
.acad-float{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:1;}
.acad-w,.acad-i{position:absolute;top:0;left:0;opacity:0;will-change:transform,opacity;}
.acad-w{font-family:'Inter',sans-serif;font-weight:600;white-space:nowrap;letter-spacing:.01em;}
.acad-i svg{display:block;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;}
.acad-c0{color:#1a6b72;} .acad-c1{color:#3d635e;} .acad-c2{color:#a8791a;} .acad-c3{color:#2e7d6a;}
html[data-theme="dark"] .acad-c0{color:#7fd6c4;} html[data-theme="dark"] .acad-c1{color:#e8f6f1;}
html[data-theme="dark"] .acad-c2{color:#e6bf62;} html[data-theme="dark"] .acad-c3{color:#9fe0b8;}
@keyframes acad-drift{0%{transform:translate(var(--x0),var(--y0)) rotate(var(--r));opacity:0;}12%,88%{opacity:var(--op);}
  100%{transform:translate(var(--x1),var(--y1)) rotate(var(--r));opacity:0;}}
@keyframes acad-rise{0%{transform:translate(var(--x0),0) rotate(var(--r));opacity:0;}15%,80%{opacity:var(--op);}
  100%{transform:translate(var(--x1),var(--rise)) rotate(var(--r2));opacity:0;}}
@media (max-width:640px){body .hero.acad-hero{padding:38px 0 34px;}.acad-tracks{grid-template-columns:1fr 1fr;}.acad-track-ico{display:none;}}
@media (prefers-reduced-motion:reduce){body .hero.acad-hero{animation:none;}.acad-w,.acad-i{animation:none !important;opacity:.14;}}
@media print{.acad-float{display:none;}body .hero.acad-hero{background:#fff !important;color:#000 !important;}}
"""

ACADEMY_HERO_JS = r"""
(function(){
  var wrap=document.querySelector('.acad-float');
  if(!wrap)return;
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WORDS=['Module 1','Learning objectives','Pre-test','Post-test','Quiz 5/5 ✓','Skills checklist',
    'Return demonstration','Competency sign-off','Case study','Syllabus','Trainer notes','A · B · C · D',
    'Hand hygiene','Aseptic technique','Water log','Kt/V','Pre-dialysis check','Logbook','Review','Practice',
    'Step 1 → 2 → 3','Supervised practice'];
  var I='<svg viewBox="0 0 24 24" width="SZ" height="SZ">';
  var ICONS=[
    '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.6 2.7 3 6 3s6-1.4 6-3v-5"/><path d="M22 9v6"/>',
    '<path d="M2 5c3-1.3 6.5-1.3 10 1 3.5-2.3 7-2.3 10-1v14c-3-1.3-6.5-1.3-10 1-3.5-2.3-7-2.3-10-1z"/><path d="M12 6v14"/>',
    '<path d="M4 20l4-1L19 8l-3-3L5 16z"/><path d="M14 6l3 3"/>',
    '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="m8.5 12 2 2 4-4"/><path d="M8.5 17h7"/>',
    '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
    '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/><path d="m7 12 3-3 3 2 4-4"/>'
  ];
  function rnd(a,b){return a+Math.random()*(b-a);}
  var small=window.innerWidth<640, frag=document.createDocumentFragment(), i, el;
  var NW=small?9:16, NI=small?6:11;
  for(i=0;i<NW;i++){
    el=document.createElement('span');
    el.className='acad-w acad-c'+(i%4);
    el.textContent=WORDS[i%WORDS.length];
    el.style.fontSize=rnd(11,22).toFixed(1)+'px';
    el.style.top=rnd(-2,96)+'%';
    var y0=rnd(-10,10);
    el.style.setProperty('--x0',rnd(-14,6)+'vw'); el.style.setProperty('--x1',rnd(88,118)+'vw');
    el.style.setProperty('--y0',y0+'px'); el.style.setProperty('--y1',(y0+rnd(-30,30))+'px');
    el.style.setProperty('--r',rnd(-6,6).toFixed(1)+'deg'); el.style.setProperty('--op',rnd(.12,.28).toFixed(2));
    var d=rnd(18,36); if(!still) el.style.animation='acad-drift '+d.toFixed(1)+'s '+(-rnd(0,d)).toFixed(1)+'s linear infinite';
    else { el.style.transform='translate('+rnd(0,85)+'vw,0)'; }
    frag.appendChild(el);
  }
  for(i=0;i<NI;i++){
    el=document.createElement('span');
    el.className='acad-i acad-c'+((i+1)%4);
    var sz=Math.round(rnd(18,40));
    el.innerHTML=I.replace(/SZ/g,sz)+ICONS[i%ICONS.length]+'</svg>';
    el.style.top='100%';
    var x=rnd(2,96);
    el.style.setProperty('--x0',x+'vw'); el.style.setProperty('--x1',(x+rnd(-6,6))+'vw');
    el.style.setProperty('--rise',-(rnd(320,520))+'px');
    el.style.setProperty('--r',rnd(-14,14).toFixed(0)+'deg'); el.style.setProperty('--r2',rnd(-14,14).toFixed(0)+'deg');
    el.style.setProperty('--op',rnd(.14,.3).toFixed(2));
    var dd=rnd(14,26); if(!still) el.style.animation='acad-rise '+dd.toFixed(1)+'s '+(-rnd(0,dd)).toFixed(1)+'s ease-in-out infinite';
    else { el.style.top=rnd(10,80)+'%'; el.style.transform='translate('+x+'vw,0)'; }
    frag.appendChild(el);
  }
  wrap.appendChild(frag);
})();
"""

TRACK_ICONS = {
    "nephrology-nursing": '<path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/><path d="M12 9v5"/><path d="M9.5 11.5h5"/>',
    "hemodialysis-technician": '<path d="M12 3s5 5.6 5 9.5a5 5 0 0 1-10 0C7 8.6 12 3 12 3z"/><path d="M9.5 13.5a2.5 2.5 0 0 0 2.5 2.5"/>',
    "water-treatment-technician": '<path d="M3 7h18"/><path d="M5 7v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7"/><path d="M8 11h8M8 15h5"/><path d="M12 3v4"/>',
    "attending-nephrologist": '<path d="M6 3v6a6 6 0 0 0 12 0V3"/><path d="M12 15v2a4 4 0 0 0 8 0v-3"/><circle cx="20" cy="12" r="2"/>',
    "dialysis-clinical-head": '<path d="M3 21h18"/><path d="M5 21V10l7-5 7 5v11"/><path d="M9 21v-6h6v6"/><path d="M12 8v3M10.5 9.5h3"/>',
    "dialysis-unit-manager": '<rect x="4" y="4" width="16" height="17" rx="2"/><path d="M9 3h6v3H9z"/><path d="M8 11h8M8 15h5"/>',
    "peritoneal-dialysis-nurse": '<path d="M12 3s5 5.6 5 9.5a5 5 0 0 1-10 0C7 8.6 12 3 12 3z"/><path d="M8 20h8"/>',
    "philhealth-claims": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3v3h6V3"/><path d="M8.5 13l2.5 2.5 4.5-5"/>',
    "medical-records-officer": '<path d="M4 4h6l2 2h8v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><path d="M8 12h8M8 16h5"/>',
    "renal-dietitian": '<path d="M7 3v8a3 3 0 0 0 6 0V3"/><path d="M10 3v18"/><path d="M17 3c-1.7 1.2-2.5 3.2-2.5 6 0 2 1 3 2.5 3v9"/>',
    "dialysis-head-nurse": '<path d="M8 3h8v4a4 4 0 0 1-8 0z"/><path d="M12 11v3"/><path d="M5 21a7 7 0 0 1 14 0"/><path d="M10.5 5h3M12 3.5v3"/>',
    "dialysis-biomedical-technician": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
}


def academy_hero(A, tracks):
    """tracks: [(href, short title, module count)]"""
    total = sum(n for _, _, n in tracks)
    links = "\n".join(
        f'    <a class="acad-track" href="{h}"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">'
        f'{TRACK_ICONS.get(h[:-5], TRACK_ICONS["nephrology-nursing"])}</svg></span>'
        f'<span class="acad-track-t"><strong>{t}</strong><small>{n} modules</small></span></a>' for h, t, n in tracks)
    return f"""<style id="acad-hero-style">{ACADEMY_HERO_CSS}</style>
<section class="hero acad-hero">
  <div class="acad-float" aria-hidden="true"></div>
  <div class="container">
    <div class="hero-tag">Staff Training &middot; Dialysis &amp; Nephrology</div>
    <h1>Renal Care <em>Academy</em></h1>
    <p class="hero-sub">{A['sub']}</p>
    <div class="acad-stats"><span class="acad-stat"><b>{len(tracks)}</b> tracks</span><span class="acad-stat"><b>{total}</b> modules</span><span class="acad-stat">Quizzes &amp; skills checklists</span><span class="acad-stat">Free &middot; no account</span><span class="acad-stat">English</span></div>
    <nav class="acad-tracks" aria-label="Academy tracks">
{links}
    </nav>
  </div>
</section>
<script>{ACADEMY_HERO_JS}</script>"""


def build_academy():
    fname = ACADEMY_PAGE
    page = Page(fname)
    A = SHARED.ACADEMY

    def track(href, img, role, title, blurb, meta_line, live=True):
        pic = f'<img class="nc-fig-img" src="../images/{img}" alt="" loading="lazy" decoding="async" width="640" height="360">' if img and (IMAGES / img).exists() else ""
        body = f'<span class="tc-branch-body"><small>{role}</small><b>{title}</b><span>{blurb}</span><span><strong>{meta_line}</strong></span></span>'
        if live:
            return f'    <a class="tc-branch" href="{href}">{pic}\n      {body}\n    </a>'
        return f'    <div class="tc-branch tc-soon">{pic}\n      {body}\n    </div>'
    cards, tech = [track(*A["nursing"])], []
    for pkg, c in get_courses().items():
        M = c.meta
        card = track(c.hub + ".html", M.get("branch_img", ""), M["branch_role"], M["title"], M["branch_blurb"],
                     M.get("academy_meta") or f"{len(c.mods)} modules &middot; skills checklists &middot; trainer page")
        (tech if M.get("tag") == "Renal Technicians" else cards).append(card)
    tech_block = (f'  <h3 id="renal-technician-program">Renal Technician Program</h3>\n'
                  f'  <p>Three technician tracks in one program, written in the same format. Most people start at the chairside as a '
                  f'dialysis technician; two specialist branches lead to the water room and the biomedical workshop.</p>\n'
                  f'  <div class="tc-branches tc-tracks">\n{chr(10).join(tech)}\n  </div>\n') if tech else ""
    soon = [track("", "", role, title, blurb, "In preparation", live=False) for role, title, blurb in A["planned"]]
    soon_block = (f'  <h3>In preparation</h3>\n  <div class="tc-branches tc-tracks">\n{chr(10).join(soon)}\n  </div>\n') if soon else ""
    main = f"""<section class="section" id="about">
  <div class="section-tag">Renal Care Academy</div>
  <h2>Training for the people who deliver kidney care</h2>
{page.render(A['about_html'])}
</section>

<section class="section" id="tracks">
  <div class="section-tag">Tracks</div>
  <h2>Choose your role</h2>
  <p>Each track is a complete study series with its own course home, syllabus, and trainer page.</p>
  <div class="tc-branches tc-tracks">
{chr(10).join(cards)}
  </div>
{tech_block}{soon_block}</section>

<section class="section" id="how">
  <div class="section-tag">How the Academy works</div>
  <h2>The same format in every track</h2>
{page.render(A['how_html'])}
</section>

<section class="section" id="limits">
  <div class="section-tag">Please read</div>
  <h2>What the Academy is, and is not</h2>
  <div class="alert alert-amber">
    <div class="alert-icon">⚠️</div>
    <div class="alert-body">
      <h4>Study material, not certification</h4>
      <p>{page.render(A['is_not'])}</p>
    </div>
  </div>
  <p>Looking for patient and clinician reading instead? The <a href="index.html">guide library</a>, the <a href="calculators.html">calculators</a>, and the <a href="/drugs/">drug index</a> are separate sections of this site, and Academy modules link to them as further reading.</p>
</section>"""
    main = N.auto_expand(main, fname)
    nav = [("about", "About"), ("tracks", "Tracks"), ("how", "How it works"), ("limits", "What it is not")]
    rel = [(c.hub + ".html", "Track", c.meta["title"], c.meta["branch_blurb"]) for c in get_courses().values()]
    rel.insert(0, (A["nursing"][0], "Track", A["nursing"][3], A["nursing"][4]))
    pre = ""
    n_nurse = int(re.match(r"(\d+)", A["nursing"][5]).group(1))
    hero_tracks = [(A["nursing"][0], "Nephrology Nursing", n_nurse)]
    short = {"hemodialysis-technician": "Dialysis Technician", "water-treatment-technician": "Water Treatment Technician",
             "dialysis-biomedical-technician": "Biomedical Technician", "renal-dietitian": "Renal Dietitian", "dialysis-clinical-head": "Dialysis Clinical Head", "philhealth-claims": "PhilHealth Claims", "dialysis-unit-manager": "Unit Manager",
             "attending-nephrologist": "Attending Nephrologist", "medical-records-officer": "Medical Records Officer", "dialysis-head-nurse": "Head Nurse"}
    hero_tracks += [(c.hub + ".html", short.get(c.hub, c.meta["title"]), len(live_mods(c))) for c in get_courses().values()]
    desc = A["desc"]
    pg = shell(_Academy, fname, "Renal Care Academy: Training for Dialysis and Nephrology Staff", desc, A["keywords"],
               "Renal Care Academy", "Renal Care <em>Academy</em>", A["sub"], A["audience"], nav, pre, main,
               glossary(main, []), N.related_block(rel),
               jsonld_extra={"@type": ["MedicalWebPage", "CollectionPage"], "description": desc},
               hero_html=academy_hero(A, hero_tracks))
    (GUIDES / fname).write_text(N.merge_cites(pg), encoding="utf-8")
    return fname, page.refs


# ───────────────────────── docs ─────────────────────────
def write_docs(all_refs, built_all):
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    (DATA / "refs-overrides.json").write_text(json.dumps(all_refs, indent=1, ensure_ascii=False), encoding="utf-8")
    lines = ["# Quiz key register (technical-workforce courses)", "",
             "Generated by generate_tech_courses.py. One row per scored item for clinical and technical review.", ""]
    manifest = []
    for pkg, course in get_courses().items():
        lines += [f"# {course.meta['title']}", ""]
        for d in course.mods:
            m = built_all[pkg][d["id"]][0]
            hero = f"{d.get('hero_file') or d['slug'] + '-vignette-hero'}.png"
            manifest.append({"course": pkg, "module": d["id"], "title": d["title"], "page": f"guides/{d['slug']}.html",
                             "hero": f"images/{hero}", "hero_status": "present" if (IMAGES / hero).exists() else "pending production",
                             "page_status": "planned" if m is None else "built",
                             "hero_brief": d.get("hero_brief", "")})
            if m is None:
                continue
            lines += [f"## Module {int(d['id'])}: {d['title']}", "", "| Q | Stem | Keyed answer | Explanation | Objective |", "|---|---|---|---|---|"]
            for qi, q in enumerate(m["quiz"], 1):
                strip = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).replace("|", "/")
                lines.append(f"| {qi} | {strip(q['stem'])} | {strip(q['options'][q['answer']])} | {strip(q['why'])} | {q.get('objective', '')} |")
            lines.append("")
    (DOCS / "QUIZ-KEY-REGISTER.md").write_text("\n".join(lines), encoding="utf-8")
    (DOCS / "image-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")


def run_pipeline(files):
    PY = N.pipeline_python()
    for f in files:
        for step in N.PIPELINE:
            if step == "REFS":
                cmd = [PY, "patch_references_accordion.py", "--overrides", str(DATA / "refs-overrides.json"), "--guide", f]
            else:
                cmd = [PY, step, "--guide", f]
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  ! {step} failed on {f}: {(r.stderr or r.stdout).strip()[-300:]}")
        print(f"  patched {f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", choices=PACKAGES)
    ap.add_argument("--patch", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    all_refs, built_all, written = {}, {}, []
    refs_path = DATA / "refs-overrides.json"
    if refs_path.exists():
        all_refs = json.loads(refs_path.read_text(encoding="utf-8"))
    for pkg, course in get_courses().items():
        built = {d["id"]: course.build_mod(d) for d in course.mods}
        built_all[pkg] = built
        for d in course.mods:
            m = built[d["id"]][0]
            if m is None:
                continue
            for q in m["quiz"]:
                if not (0 <= q["answer"] < 4):
                    err(f"{d['slug']}: bad answer index")
            if len(m["quiz"]) < course.meta.get("draw", 5):
                err(f"{d['slug']}: question bank smaller than the draw")
        if args.check or (args.course and args.course != pkg):
            continue
        for d in course.mods:
            if built[d["id"]][0] is None:
                continue
            f, refs = build_module(course, d, built[d["id"]]); all_refs[f] = refs; written.append(f)
        f, refs = build_hub(course, built); all_refs[f] = refs; written.append(f)
        f, refs = build_trainer(course, built); all_refs[f] = refs; written.append(f)
        f, refs = build_exam(course, built); all_refs[f] = refs; written.append(f)
    if not args.check:
        # The Academy landing page (academy/index.html) is now maintained by hand: five staff groups, nursing by
        # specialization and by role, onboarding tables, track images. Rebuilding it here would erase all of that,
        # so the generator leaves it alone while the marker is present. Add a new track to the landing page by hand.
        landing = ROOT / "academy" / "index.html"
        if landing.exists() and LANDING_MARK in landing.read_text(encoding="utf-8"):
            print("academy/index.html is hand-maintained (marker found); landing page not regenerated")
        else:
            f, refs = build_academy(); all_refs[f] = refs; written.append(f)
        write_docs(all_refs, built_all)
        print(f"wrote {len(written)} pages to guides/")
    if ERRORS or N.ERRORS:
        print("\nCONTENT ERRORS:")
        for e in ERRORS:
            print("  -", e)
        if ERRORS:
            sys.exit(1)
    if args.patch:
        run_pipeline(sorted(written))
    if not args.check:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "academy" / "publish_academy.py")], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout or r.stderr).strip())
        if (ROOT / "generate_transplant_nurse.py").exists():   # keep the Transplant Nurse entry links
            r2 = subprocess.run([sys.executable, "-c", "import generate_transplant_nurse as T; print('transplant-nurse entry links:', T.wire_parent())"], cwd=ROOT, capture_output=True, text=True)
            print((r2.stdout or r2.stderr).strip()[-300:])


if __name__ == "__main__":
    main()
