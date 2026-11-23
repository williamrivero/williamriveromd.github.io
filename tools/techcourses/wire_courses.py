#!/usr/bin/env python3
"""Wire the technical-workforce courses into the site (idempotent).

    python3 tools/techcourses/wire_courses.py [--dry-run]

1. guides/index.html: one tile per course hub, after the nursing course tile (TECH-COURSE-TILES markers).
2. related_guides.json: entries for every course page.
3. generate_latest_guides.py: skip module and trainer pages (hubs still appear in the Latest strip).

Run generate_sitemap.py, generate_search_index.py, patch_audience_chips.py and generate_latest_guides.py afterward.
"""
import sys as _sys
_sys.exit("SUPERSEDED: courses now live in /academy/. Use tools/academy/wire_academy.py.")
import html, importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TC = ROOT / "tools" / "techcourses"
DRY = "--dry-run" in sys.argv
START, END = "<!-- TECH-COURSE-TILES-START -->", "<!-- TECH-COURSE-TILES-END -->"
PACKAGES = ["hd_technician", "water_treatment", "biomed"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


courses = [load(TC / p / "course.py", p) for p in PACKAGES if (TC / p / "course.py").exists()]
changed, tiles, rel_new, prefixes = [], [], {}, []
hubs = [c.COURSE["hub_slug"] + ".html" for c in courses]
for c in courses:
    C = c.COURSE
    hub = C["hub_slug"]
    prefixes.append(hub + "-")
    live = [m for m in c.MODULES if m.get("status") != "planned"]
    files = [f"{hub}-{m['id']}-{m['slug']}.html" for m in live]
    words = " ".join([C["keywords"].replace(",", " ")] + [html.unescape(m["title"]) + " " + html.unescape(m["sub"]) for m in live])
    data_text = html.escape(re.sub(r"\s+", " ", words))
    tiles.append(f"""        <a href="{hub}.html" class="guide-tile" data-tags="new dialysis dialysis-staff clinician" data-text="{data_text}">
          <div class="tile-icon read" data-icon="clipboard"></div>
          <div class="tile-body">
            <div class="tile-title">{C['title']}</div>
            <div class="tile-meta"><span class="meta-tag tag-new">New</span><span class="meta-tag tag-system-nav">Technicians</span><span class="meta-tag tag-system-nav">{len(c.MODULES)}-module course</span></div>
            <div class="tile-teaser">{C['branch_blurb']} View the syllabus and start learning.</div>
          </div>
          <span class="tile-arrow">›</span>
        </a>""")
    rel_new[hub + ".html"] = files[:2] + [hub + "-trainer.html"] + [h for h in hubs if h != hub + ".html"] + [f for f, _ in C.get("related", [])][:2]
    rel_new[hub + "-trainer.html"] = [hub + ".html", "dialysis-qapi-vs-cqi.html"]
    for i, f in enumerate(files):
        arr = [hub + ".html"]
        if i + 1 < len(files):
            arr.append(files[i + 1])
        if i > 0:
            arr.append(files[i - 1])
        rel_new[f] = arr

block = START + "\n" + "\n".join(tiles) + "\n        " + END + "\n"
p = ROOT / "guides/index.html"
s = p.read_text(encoding="utf-8")
if START in s:
    new = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n", lambda _m: block, s, count=1, flags=re.S)
else:
    anchor = "<!-- NURSING-COURSE-TILE-END -->\n"
    if anchor in s:
        i = s.index(anchor) + len(anchor)
    else:
        m = re.search(r'(<div class="sub-group" id="dial-unit"[^>]*>\s*<div class="sub-head">.*?</div>\n)', s, re.S)
        if not m:
            sys.exit("could not find an insertion point in guides/index.html")
        i = m.end()
    new = s[:i] + "        " + block + s[i:]
if new != s:
    changed.append("guides/index.html (course tiles)")
    if not DRY:
        p.write_text(new, encoding="utf-8")

p = ROOT / "related_guides.json"
rel = json.loads(p.read_text(encoding="utf-8"))
before = json.dumps(rel, sort_keys=True)
rel.update(rel_new)
if json.dumps(rel, sort_keys=True) != before:
    changed.append(f"related_guides.json ({len(rel_new)} entries)")
    if not DRY:
        p.write_text(json.dumps(rel, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

p = ROOT / "generate_latest_guides.py"
s = p.read_text(encoding="utf-8")
m = re.search(r"SKIP_PREFIX = \((.*?)\)", s)
if not m:
    sys.exit("generate_latest_guides.py: SKIP_PREFIX not found")
missing = [x for x in prefixes if f'"{x}"' not in m.group(1)]
if missing:
    inner = m.group(1).rstrip().rstrip(",") + ", " + ", ".join(f'"{x}"' for x in missing)
    s = s[:m.start()] + f"SKIP_PREFIX = ({inner})" + s[m.end():]
    changed.append("generate_latest_guides.py (skip course sub-pages)")
    if not DRY:
        p.write_text(s, encoding="utf-8")

print(("would change: " if DRY else "changed: ") + (", ".join(changed) if changed else "nothing (already wired)"))
