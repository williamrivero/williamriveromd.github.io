# -*- coding: utf-8 -*-
"""Build guides/calc-resuscitation-lab-toolkit.html from the Medical Records Officer toolkit page (house calculator chrome) and
the Resuscitation Lab tool sources in tools/techcourses/resus/toolkit/ (main.html, script.html). Idempotent: rebuilds the page
from the template every time. Run from the repo root:  python3 tools/techcourses/resus/build_toolkit.py
Then test:  node tools/test_resus_toolkit.cjs    """
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TPL = ROOT / "guides" / "calc-medical-records-officer-toolkit.html"
OUT = ROOT / "guides" / "calc-resuscitation-lab-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Resuscitation Lab Toolkit: Compression Fraction, Megacode Timeline, Pediatric Dose Trainer"
DESC = ("Five drill tools for dialysis resuscitation teams: CPR interruption and compression-fraction analyzer, megacode timeline "
        "analyzer, pediatric resuscitation dose-and-volume trainer, oxygen cylinder duration planner, and drill role rotation.")
KEYS = ("chest compression fraction calculator, CPR pause analyzer, megacode timeline, pediatric epinephrine dose trainer 0.01 mg/kg, "
        "pediatric defibrillation J/kg, oxygen cylinder duration calculator, mock code role rotation, dialysis unit resuscitation drill")
OG = "https://renalcarematters.com/images/og/calc-resuscitation-lab-toolkit-og.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_t = re.search(r"<title>(.*?)</title>", s).group(1)
    s = s.replace(old_t, TITLE)
    old_d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_d, DESC)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-medical-records-officer-toolkit", "calc-resuscitation-lab-toolkit")
    s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">',
               '<meta property="og:image:alt" content="Renal Care Academy: Resuscitation Lab toolkit">', s, count=1)
    s = re.sub(r'<meta name="robots" content="noindex"><!-- RL-DRAFT -->\n?', "", s)   # signed off Nov 28 2026
    stamp = None
    if OUT.exists():   # keep the first publish stamp
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Emergency Readiness · Drill Tools</div>\n'
            '<h1>Resuscitation Lab <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Five drill and teaching tools for the Dialysis Team Resuscitation Lab: measure CPR pauses and compression '
            'fraction, analyze a megacode timeline, practice pediatric dose and volume arithmetic, plan oxygen for transfer, and rotate '
            'drill roles. They do arithmetic, not clinical decisions. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/resuscitation-lab.html" class="hero-xlink">Resuscitation Lab course</a> &nbsp;·&nbsp; '
            '<a href="../academy/resuscitation-lab-practice.html" class="hero-xlink">Practice Lab</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">CPR fraction</a><a class="nav-pill" href="#tool-2">Timeline</a>'
             '<a class="nav-pill" href="#tool-3">Pediatric trainer</a><a class="nav-pill" href="#tool-4">Oxygen</a><a class="nav-pill" href="#tool-5">Rotation</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', pills, s, count=1, flags=re.S)
    s = re.sub(r'<main class="container dch-calc">.*?</main>', lambda m: (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    s = re.sub(r'<script>\s*/\* ===== MRO-CALC-CORE.*?</script>', lambda m: (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/resuscitation-lab.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Dialysis Team Resuscitation Lab</div></a>\n'
           '    <a class="related-card" href="calc-pediatric-dialysis-nurse-toolkit.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Pediatric Dialysis Nurse Toolkit (extracorporeal volume)</div></a>\n'
           '    <a class="related-card" href="code-blue-acls-dialysis-unit.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Code Blue and ACLS in a Dialysis Unit</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', lambda m: rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/medical-records-officer.html" aria-label="Go to related guide">',
                  '<a href="../academy/resuscitation-lab.html" aria-label="Go to related guide">')
    body = s.split("<body", 1)[1].replace("dch-calc", "")
    assert "medical-records-officer" not in body and "MRO-CALC" not in body, "template leftovers"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
