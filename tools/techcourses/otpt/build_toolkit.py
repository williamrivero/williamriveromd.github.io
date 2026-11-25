# -*- coding: utf-8 -*-
"""Build guides/calc-renal-rehabilitation-toolkit.html from the Medical Records Officer toolkit page (house calculator
chrome) and the OT/PT tool sources in tools/techcourses/otpt/toolkit/ (main.html, script.html). Idempotent: rebuilds the
page from the template every time. Run from the repo root:  python3 tools/techcourses/otpt/build_toolkit.py"""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TPL = ROOT / "guides" / "calc-medical-records-officer-toolkit.html"
OUT = ROOT / "guides" / "calc-renal-rehabilitation-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Renal Rehabilitation Toolkit: 6 Measurement Tools for OT and PT"
DESC = ("Six measurement tools for occupational and physical therapists in kidney care: six-minute walk percent predicted "
        "(Enright-Sherrill), Short Physical Performance Battery scorer, gait speed and Timed Up and Go log, sit-to-stand change "
        "tracker, weekly activity minutes against the KDIGO 150-minute aim, and a session screen log against your unit's limits.")
KEYS = ("six minute walk percent predicted calculator, SPPB calculator, gait speed calculator, sit to stand test dialysis, "
        "STS60, renal rehabilitation, exercise dialysis physical therapy, occupational therapy kidney")
OG = "https://renalcarematters.com/images/og/renal-rehabilitation-toolkit.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_t = re.search(r"<title>(.*?)</title>", s).group(1)
    s = s.replace(old_t, TITLE)
    old_d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_d, DESC)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-medical-records-officer-toolkit", "calc-renal-rehabilitation-toolkit")
    s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">',
               '<meta property="og:image:alt" content="Renal Care Academy: Renal Rehabilitation Toolkit">', s, count=1)
    stamp = None
    if OUT.exists():   # keep the first publish stamp
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Occupational and Physical Therapist · Measurement Tools</div>\n'
            '<h1>Renal Rehabilitation <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Six working tools for the Renal Care Academy Occupational and Physical Therapist track. They calculate and record; '
            'they do not clear anyone for exercise, change dialysis or diagnose. Exercise parameters come from the referring physician and your '
            'unit&rsquo;s agreed sheet. Use no patient names or identifiers. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/occupational-physical-therapist.html" class="hero-xlink">Occupational and Physical Therapist track</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">6-minute walk</a><a class="nav-pill" href="#tool-2">SPPB</a>'
             '<a class="nav-pill" href="#tool-3">Gait speed</a><a class="nav-pill" href="#tool-4">Sit-to-stand</a><a class="nav-pill" href="#tool-5">Activity minutes</a>'
             '<a class="nav-pill" href="#tool-6">Screen log</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', pills, s, count=1, flags=re.S)
    s = re.sub(r'<main class="container dch-calc">.*?</main>', lambda m: (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    s = re.sub(r'<script>\s*/\* ===== MRO-CALC-CORE.*?</script>', lambda m: (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/occupational-physical-therapist.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Occupational and Physical Therapist: the study track</div></a>\n'
           '    <a class="related-card" href="calc-frailty-assessment.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Frailty Assessment</div></a>\n'
           '    <a class="related-card" href="exercise-guide-ckd.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Exercise and Kidney Disease</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', lambda m: rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/medical-records-officer.html" aria-label="Go to related guide">',
                  '<a href="../academy/occupational-physical-therapist.html" aria-label="Go to related guide">')
    leftovers = s.split("<body", 1)[1].replace("dch-calc", "")
    assert "medical-records-officer" not in leftovers, "template leftovers"
    assert "OTPT-CALC-CORE" in s and 'id="tool-6"' in s, "toolkit sources not inserted"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
