#!/usr/bin/env python3
"""Wire the Renal Care Academy into the rest of the site (idempotent). Replaces tools/nursing/wire_course.py
and tools/techcourses/wire_courses.py, which listed each course inside the Guides index.

    python3 tools/academy/wire_academy.py [--dry-run]

1. guides/index.html: removes the per-course tiles and leaves ONE signpost tile that links to /academy/.
2. related_guides.json: removes entries for academy pages (they are no longer guides).
3. generate_sitemap.py: scans academy/ so its pages are listed under /academy/.
4. generate_nursing_course.py: carries publish stamps over from academy/ and moves pages there after building.

Afterward run: generate_sitemap.py, generate_search_index.py, patch_audience_chips.py, generate_latest_guides.py.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "academy"))
from publish_academy import is_academy  # noqa: E402

DRY = "--dry-run" in sys.argv
changed = []


def save(p, new, old, label):
    if new != old:
        changed.append(label)
        if not DRY:
            p.write_text(new, encoding="utf-8")


# 1. Guides index: one signpost tile
p = ROOT / "guides/index.html"
s = old = p.read_text(encoding="utf-8")
TILE = """<!-- TECH-COURSE-TILES-START -->
        <a href="/academy/" class="guide-tile" data-tags="new dialysis dialysis-staff clinician" data-text="renal care academy staff training course nurse nursing hemodialysis technician water treatment biomedical technician dietitian physician on duty self-study syllabus modules competency checklist">
          <div class="tile-icon read" data-icon="clipboard"></div>
          <div class="tile-body">
            <div class="tile-title">Renal Care Academy</div>
            <div class="tile-meta"><span class="meta-tag tag-new">New</span><span class="meta-tag tag-system-nav">Staff training</span><span class="meta-tag tag-system-nav">Separate section</span></div>
            <div class="tile-teaser">Structured courses for nephrology nurses, hemodialysis technicians, water treatment technicians, and biomedical technicians. Open the Academy.</div>
          </div>
          <span class="tile-arrow">›</span>
        </a>
        <!-- TECH-COURSE-TILES-END -->
"""
s = re.sub(r"<!-- NURSING-COURSE-TILE-START -->.*?<!-- NURSING-COURSE-TILE-END -->\n\s*", "", s, flags=re.S)
if "<!-- TECH-COURSE-TILES-START -->" in s:
    s = re.sub(r"<!-- TECH-COURSE-TILES-START -->.*?<!-- TECH-COURSE-TILES-END -->\n", lambda _m: TILE, s, count=1, flags=re.S)
else:
    m = re.search(r'(<div class="sub-group" id="dial-unit"[^>]*>\s*<div class="sub-head">.*?</div>\n)', s, re.S)
    if not m:
        sys.exit("could not find an insertion point in guides/index.html")
    s = s[:m.end()] + "        " + TILE + s[m.end():]
save(p, s, old, "guides/index.html (single Academy tile)")

# 2. related_guides.json
p = ROOT / "related_guides.json"
rel = json.loads(p.read_text(encoding="utf-8"))
keep = {k: [x for x in v if not is_academy(x)] if isinstance(v, list) else v for k, v in rel.items() if not is_academy(k)}
if keep != rel:
    changed.append(f"related_guides.json (removed {len(rel) - len(keep)} academy entries)")
    if not DRY:
        p.write_text(json.dumps(keep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 3. sitemap generator
p = ROOT / "generate_sitemap.py"
s = old = p.read_text(encoding="utf-8")
if '"academy"' not in s:
    a = 'scan_dirs = [REPO_ROOT, REPO_ROOT / "guides",'
    b = '    if rel_path.startswith("guides/"):\n        return "/" + rel_path, "guide"\n'
    if a not in s or b not in s:
        sys.exit("generate_sitemap.py changed; add academy/ by hand")
    s = s.replace(a, 'scan_dirs = [REPO_ROOT, REPO_ROOT / "guides", REPO_ROOT / "academy",')
    s = s.replace(b, b + '    if rel_path.startswith("academy/"):          # Renal Care Academy (staff training); index.html -> /academy/\n        return "/" + rel_path, "guide"\n')
save(p, s, old, "generate_sitemap.py (scan academy/)")

# 4. nursing generator
p = ROOT / "generate_nursing_course.py"
s = old = p.read_text(encoding="utf-8")
if "publish_academy.py" not in s:
    a = "    p = GUIDES / fname\n    if p.exists():\n        m = re.search(r'<meta property=\"article:published_time\""
    if a not in s:
        sys.exit("generate_nursing_course.py changed; update existing_published by hand")
    s = s.replace(a, "    p = ROOT / \"academy\" / fname          # finished pages live in academy/ (tools/academy/publish_academy.py)\n"
                     "    if not p.exists():\n        p = GUIDES / fname\n    if p.exists():\n        m = re.search(r'<meta property=\"article:published_time\"")
    a = "    if args.patch:\n        run_pipeline(sorted(all_refs))\n"
    if a not in s:
        sys.exit("generate_nursing_course.py changed; add the publish step by hand")
    s = s.replace(a, a + "    if not args.check:\n        r = subprocess.run([sys.executable, str(ROOT / \"tools\" / \"academy\" / \"publish_academy.py\")], cwd=ROOT, capture_output=True, text=True)\n"
                         "        print((r.stdout or r.stderr).strip())\n")
save(p, s, old, "generate_nursing_course.py (academy publish step)")

# 5. retire the old wiring scripts
for rel_path in ("tools/nursing/wire_course.py", "tools/techcourses/wire_courses.py"):
    p = ROOT / rel_path
    if p.exists():
        s = old = p.read_text(encoding="utf-8")
        if "SUPERSEDED" not in s:
            s = s.replace("import ", "import sys as _sys\n_sys.exit(\"SUPERSEDED: courses now live in /academy/. Use tools/academy/wire_academy.py.\")\nimport ", 1)
        save(p, s, old, f"{rel_path} (retired)")

print(("would change: " if DRY else "changed: ") + (", ".join(changed) if changed else "nothing (already wired)"))
