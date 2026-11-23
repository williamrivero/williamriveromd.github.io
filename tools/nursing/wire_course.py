#!/usr/bin/env python3
"""Wire the Nephrology Nursing & Hemodialysis course into the site (idempotent).

    python3 tools/nursing/wire_course.py            # apply
    python3 tools/nursing/wire_course.py --dry-run  # report only

1. guides/index.html: one course tile at the top of Dialysis > "Dialysis Unit Operations & Safety"
   (between NURSING-COURSE-TILE markers). Only the hub gets a tile; modules are reached from the hub,
   and their titles and key terms are folded into the tile's data-text so index search finds them.
2. related_guides.json: entries for the 14 course pages.
3. generate_latest_guides.py: skip module and educator pages so 13 cards do not flood the
   "Latest guides" strip (the hub still appears).

Run generate_sitemap.py, generate_search_index.py, patch_audience_chips.py and
generate_latest_guides.py afterward.
"""
import sys as _sys
_sys.exit("SUPERSEDED: courses now live in /academy/. Use tools/academy/wire_academy.py.")
import importlib.util, json, re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DRY = "--dry-run" in sys.argv
START, END = "<!-- NURSING-COURSE-TILE-START -->", "<!-- NURSING-COURSE-TILE-END -->"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools/nursing/content" / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


C = load("common")
hub = C.COURSE["hub_slug"] + ".html"
edu = C.COURSE["educator_slug"] + ".html"
mods = []
for mid, slug, title, short, _n, _h in C.MODULES:
    m = load(f"m{mid}").MODULE
    mods.append((mid, f"{C.COURSE['hub_slug']}-{mid}-{slug}.html", title, m["keywords"]))

words = ["nephrology nursing hemodialysis nurse education course self-study registered nurse RN dialysis nurse training "
         "syllabus modules quiz self-assessment nursing case preceptor competency checklist renal nurse Philippines"]
for _mid, _f, title, kw in mods:
    words.append(title)
    words.append(kw.replace(",", " "))
data_text = html.escape(re.sub(r"\s+", " ", " ".join(words)))

tile = f"""{START}
        <a href="{hub}" class="guide-tile" data-tags="new dialysis dialysis-staff clinician" data-text="{data_text}">
          <div class="tile-icon read" data-icon="clipboard"></div>
          <div class="tile-body">
            <div class="tile-title">Nephrology Nursing &amp; Hemodialysis</div>
            <div class="tile-meta"><span class="meta-tag tag-new">New</span><span class="meta-tag tag-system-nav">Registered Nurses</span><span class="meta-tag tag-system-nav">12-module course</span></div>
            <div class="tile-teaser">{C.COURSE['card_teaser']} {C.COURSE['card_cta']}</div>
          </div>
          <span class="tile-arrow">›</span>
        </a>
        {END}
"""

changed = []

# 1. index tile
p = ROOT / "guides/index.html"
s = p.read_text(encoding="utf-8")
if START in s:
    new = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n", tile, s, count=1, flags=re.S)
else:
    m = re.search(r'(<div class="sub-group" id="dial-unit"[^>]*>\s*<div class="sub-head">.*?</div>\n)', s, re.S)
    if not m:
        sys.exit("could not find the dial-unit sub-group in guides/index.html")
    new = s[:m.end()] + "        " + tile + s[m.end():]
if new != s:
    changed.append("guides/index.html (course tile)")
    if not DRY:
        p.write_text(new, encoding="utf-8")

# 2. related_guides.json
p = ROOT / "related_guides.json"
rel = json.loads(p.read_text(encoding="utf-8"))
before = json.dumps(rel, sort_keys=True)
files = [f for _mid, f, _t, _k in mods]
rel[hub] = [files[0], files[5], edu, "dialysis-water-treatment-systems.html", "code-blue-acls-dialysis-unit.html", "dialysis-qapi-vs-cqi.html"]
rel[edu] = [hub, "dialysis-qapi-vs-cqi.html", "nephrology-workforce-crisis-or-opportunity.html"]
for i, f in enumerate(files):
    m = load(f"m{mods[i][0]}").MODULE
    arr = [hub]
    if i + 1 < len(files):
        arr.append(files[i + 1])
    if i > 0:
        arr.append(files[i - 1])
    arr += [r[0] for r in m["readings"][:3]]
    rel[f] = arr
if json.dumps(rel, sort_keys=True) != before:
    changed.append("related_guides.json (14 entries)")
    if not DRY:
        p.write_text(json.dumps(rel, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 3. Latest-guides strip: hub only
p = ROOT / "generate_latest_guides.py"
s = p.read_text(encoding="utf-8")
old = 'SKIP_PREFIX = ("calc-",)'
new_line = ('SKIP_PREFIX = ("calc-", "nephrology-nursing-")  # nursing course: modules + educator page are reached '
            'from the hub (nephrology-nursing.html), which still appears in the strip')
if old in s:
    changed.append("generate_latest_guides.py (skip course sub-pages)")
    if not DRY:
        p.write_text(s.replace(old, new_line), encoding="utf-8")
elif '"nephrology-nursing-"' not in s:
    sys.exit("generate_latest_guides.py: SKIP_PREFIX not found; add 'nephrology-nursing-' by hand")

print(("would change: " if DRY else "changed: ") + (", ".join(changed) if changed else "nothing (already wired)"))
