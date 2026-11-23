#!/usr/bin/env python3
"""Wire the Physician on Duty track into the shared Academy generator. Idempotent; safe to re-run.

    python3 tools/techcourses/pod/integrate_pod.py [--dry-run]      (run from the repo root)

Run this ONLY when no other session is editing generate_tech_courses.py, tools/techcourses/shared.py, or
tools/academy/publish_academy.py. It makes small, additive changes that leave the technician tracks unchanged:

generate_tech_courses.py
  1. PACKAGES gains "pod".
  2. Each package may ship refs.py (REFS) and figs.py (FIGS); they are merged into the shared tables.
  3. New macro {{call:...}} renders a "Stop and call" box (same style as {{stop:...}}).
  4. A course may set: "icon" (scope-note icon), "no_branch" (leave it out of the technician career-pathway cards),
     "pathways_tag" / "pathways_h2" / "pathways_nav" / "pathways_html" (replace the career-pathways section on its hub),
     "trainers_intro", "trainer_audience", and "academy_meta" (the line under its card on the Academy landing page).
  5. A module row may set "tier" (chip on cards and module pages) and "part" (hub cards are grouped under part headings).
  6. Module counts on the Academy landing page and in the hub's examination sentence count published modules only.
tools/techcourses/shared.py
  6. Physician on Duty leaves the "In preparation" list on the Academy landing page (it becomes a live card).
tools/academy/publish_academy.py
  7. PREFIXES gains "physician-on-duty", so its pages move to academy/ with the others.

Afterward: python3 generate_tech_courses.py --course pod --patch
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DRY = "--dry-run" in sys.argv
done, skipped = [], []


class Patch:
    def __init__(self, rel):
        self.path = ROOT / rel
        self.rel = rel
        self.text = self.old = self.path.read_text(encoding="utf-8")

    def sub(self, label, marker, old, new, count=1):
        """Replace `old` with `new` unless `marker` (text that only exists after patching) is already present."""
        if marker in self.text:
            skipped.append(f"{self.rel}: {label}")
            return
        n = self.text.count(old)
        if n != count:
            raise SystemExit(f"{self.rel}: cannot apply '{label}': expected {count} match(es), found {n}. "
                             f"The file has changed; update integrate_pod.py.")
        self.text = self.text.replace(old, new)
        done.append(f"{self.rel}: {label}")

    def save(self):
        if self.text != self.old and not DRY:
            self.path.write_text(self.text, encoding="utf-8")


# ── generate_tech_courses.py ────────────────────────────────────────────────
g = Patch("generate_tech_courses.py")

g.sub("PACKAGES", '"biomed", "pod"]', 'PACKAGES = ["hd_technician", "water_treatment", "biomed"]',
      'PACKAGES = ["hd_technician", "water_treatment", "biomed", "pod"]')

g.sub("per-course refs and figs", "tc_{_p}_refs",
      'SHARED = load(TC / "shared.py", "tc_shared")\n',
      'SHARED = load(TC / "shared.py", "tc_shared")\n'
      'for _p in PACKAGES:      # optional per-course references (refs.py) and figures (figs.py)\n'
      '    if (TC / _p / "refs.py").exists():\n'
      '        SHARED.REFS.update(load(TC / _p / "refs.py", f"tc_{_p}_refs").REFS)\n'
      '    if (TC / _p / "figs.py").exists():\n'
      '        FIGS.update(load(TC / _p / "figs.py", f"tc_{_p}_figs").FIGS)\n')

g.sub("call macro", 'if kind == "call":',
      '            if kind == "formula":\n',
      '            if kind == "call":\n'
      '                return f\'<div class="tc-stop"><span class="tc-lab">Stop and call</span>{body}</div>\'\n'
      '            if kind == "formula":\n')

g.sub("css", ".tc-part{",
      "@media print{.tc-fig,.tc-viz,.tc-card,.tc-flow li{break-inside:avoid;}}\n\"\"\"",
      "@media print{.tc-fig,.tc-viz,.tc-card,.tc-flow li{break-inside:avoid;}}\n"
      ".tc-part{margin:26px 0 4px;font:700 1.02rem Inter,system-ui,sans-serif;color:var(--text);}\n"
      ".nc-chip-tier{border-color:var(--teal);color:var(--teal);}\n"
      "html[data-theme=\"dark\"] .nc-chip-tier{border-color:#7fd6dd;color:#7fd6dd;}\n\"\"\"")

g.sub("helpers", "def tier_chip(d):",
      "# ───────────────────────── module page ─────────────────────────\n",
      '''def tier_chip(d):
    """Optional tier label on a module (course rows may set "tier")."""
    return f'<span class="nc-chip nc-chip-tier">{d["tier"]}</span>' if d.get("tier") else ""


def grid_html(course, cards):
    """Module cards for a hub. Courses whose rows set "part" get one grid per part, under a heading."""
    if not any(d.get("part") for d in course.mods):
        return '  <div class="nc-modgrid" id="nc-modules">\\n' + "\\n".join(cards) + "\\n  </div>"
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
    return "\\n".join(out)


# ───────────────────────── module page ─────────────────────────
''')

g.sub("scope-note icon", "C.get('icon'", '<div class="alert-icon">🛠️</div>', "<div class=\"alert-icon\">{C.get('icon', '🛠️')}</div>")

g.sub("tier chip on module page", "{tier_chip(d)}\n  </div>\n  <div class=\"alert alert-teal\">",
      "    <span class=\"nc-chip nc-chip-core\">{C['label']}</span>\n  </div>\n  <div class=\"alert alert-teal\">",
      "    <span class=\"nc-chip nc-chip-core\">{C['label']}</span>{tier_chip(d)}\n  </div>\n  <div class=\"alert alert-teal\">")

g.sub("no_branch", 'M.get("no_branch")',
      '        M = c.meta\n        img = ""\n',
      '        M = c.meta\n        if M.get("no_branch") and c is not current:\n            continue\n        img = ""\n')

g.sub("tier chip on planned card", '{tier_chip(d)}<span class="nc-chip">In preparation</span>',
      '<span>Module {n}</span><span class="nc-chip">In preparation</span>',
      '<span>Module {n}</span>{tier_chip(d)}<span class="nc-chip">In preparation</span>')
g.sub("tier chip on live card", '<span>Module {n}</span>{tier_chip(d)}</span>\n',
      '<span class="nc-mod-top"><span>Module {n}</span></span>\n',
      '<span class="nc-mod-top"><span>Module {n}</span>{tier_chip(d)}</span>\n')

g.sub("grouped grid", "{grid_html(course, cards)}",
      '  <div class="nc-modgrid" id="nc-modules">\n{chr(10).join(cards)}\n  </div>', "{grid_html(course, cards)}")

if "def pathways_section(" not in g.text:
    m = re.search(r'<section class="section" id="pathways">.*?</section>', g.text, flags=re.S)
    if not m:
        raise SystemExit("generate_tech_courses.py: career-pathways section not found; update integrate_pod.py.")
    original = m.group(0)
    g.text = g.text.replace(original, "{pathways_section(course, page)}")
    helper = ('def pathways_section(course, page):\n'
              '    """Hub section after "Start here": the technician career pathways, or a course\'s own section."""\n'
              '    C = course.meta\n'
              '    if C.get("pathways_html"):\n'
              '        return (f\'<section class="section" id="pathways">\\n  <div class="section-tag">{C.get("pathways_tag", "Pathways")}</div>\\n\'\n'
              '                f\'  <h2>{C.get("pathways_h2", "How the series is organized")}</h2>\\n{page.render(C["pathways_html"])}\\n</section>\')\n'
              '    return f"""' + original + '"""\n\n\n')
    g.text = g.text.replace("def build_hub(course, built):\n", helper + "def build_hub(course, built):\n")
    done.append("generate_tech_courses.py: pathways section override")
else:
    skipped.append("generate_tech_courses.py: pathways section override")

g.sub("pathways nav label", 'C.get("pathways_nav"', '("pathways", "Career pathways")', '("pathways", C.get("pathways_nav", "Career pathways"))')

g.sub("trainers intro", "C.get('trainers_intro'",
      "<p>A head nurse, chief technician, or training provider can use these modules as the guided-study part of a supervised program. ",
      "<p>{C.get('trainers_intro', 'A head nurse, chief technician, or training provider can use these modules as the guided-study part of a supervised program. ')}")

g.sub("trainer audience", 'C.get("trainer_audience"',
      '"Head nurses, chief technicians, educators, and preceptors", nav, pre, main',
      'C.get("trainer_audience", "Head nurses, chief technicians, educators, and preceptors"), nav, pre, main')

g.sub("academy card meta", 'M.get("academy_meta")',
      'f"{len(c.mods)} modules &middot; skills checklists &middot; trainer page"',
      'M.get("academy_meta") or f"{len(c.mods)} modules &middot; skills checklists &middot; trainer page"')
g.sub("live module count in Academy hero", "len(live_mods(c))",
      'len(c.mods)) for c in get_courses().values()]',
      'len(live_mods(c))) for c in get_courses().values()]')
g.sub("live module count in exam sentence", "all {len(live_mods(course))} modules",
      "It draws questions at random from all {len(course.mods)} modules",
      "It draws questions at random from all {len(live_mods(course))} modules")
g.sub("live_mods helper", "def live_mods(course):",
      "def tier_chip(d):\n",
      'def live_mods(course):\n    """Modules that are published (rows without status "planned")."""\n'
      '    return [d for d in course.mods if d.get("status") != "planned"]\n\n\ndef tier_chip(d):\n')
g.save()

# ── tools/techcourses/shared.py ─────────────────────────────────────────────
s = Patch("tools/techcourses/shared.py")
pat = re.compile(r'\n        \("Physicians", "Physician on Duty in the Dialysis Unit",\n.*?"\),', flags=re.S)
if pat.search(s.text):
    s.text = pat.sub("", s.text, count=1)
    done.append("tools/techcourses/shared.py: Physician on Duty leaves the planned list")
else:
    skipped.append("tools/techcourses/shared.py: Physician on Duty leaves the planned list")
if "physician on duty course" not in s.text:
    old = '"keywords": "renal care academy, '
    if s.text.count(old) == 1:
        s.text = s.text.replace(old, '"keywords": "renal care academy, physician on duty course, ')
        done.append("tools/techcourses/shared.py: Academy keywords")
s.save()

# ── tools/academy/publish_academy.py ────────────────────────────────────────
p = Patch("tools/academy/publish_academy.py")
p.sub("PREFIXES", '"physician-on-duty")',
      '"dialysis-biomedical-technician")', '"dialysis-biomedical-technician", "physician-on-duty")')
p.save()

print(("DRY RUN. " if DRY else "") + f"applied {len(done)}, already present {len(skipped)}")
for x in done:
    print("  +", x)
for x in skipped:
    print("  =", x)
