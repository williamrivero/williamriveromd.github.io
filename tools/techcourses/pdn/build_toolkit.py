# -*- coding: utf-8 -*-
"""Build guides/calc-pediatric-dialysis-nurse-toolkit.html from the Medical Records Officer toolkit page (house calculator chrome) and
the Pediatric Dialysis Nurse tool sources in tools/techcourses/pdn/toolkit/ (main.html, script.html). Idempotent: rebuilds the page from
the template every time. Run from the repo root:  python3 tools/techcourses/pdn/build_toolkit.py
Then test:  node tools/test_pdn_calcs.cjs"""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TPL = ROOT / "guides" / "calc-medical-records-officer-toolkit.html"
OUT = ROOT / "guides" / "calc-pediatric-dialysis-nurse-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Pediatric Dialysis Nurse Toolkit: 6 Order-Verification Tools"
DESC = ("Six order-verification tools for pediatric dialysis nurses: body surface area and PD fill volume per square meter, "
        "extracorporeal volume as a share of blood volume, blood flow per kg and per m2, fluid removal rate, percent fluid overload, and infection rates.")
KEYS = ("pediatric dialysis calculator, PD fill volume mL/m2, extracorporeal volume 10% blood volume children, pediatric hemodialysis blood flow, "
        "ultrafiltration rate mL/kg/h child, percent fluid overload CRRT, peritonitis rate per patient-year ISPD 2024 pediatric")
OG = "https://renalcarematters.com/images/og/pediatric-dialysis-nurse-toolkit.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_t = re.search(r"<title>(.*?)</title>", s).group(1)
    s = s.replace(old_t, TITLE)
    old_d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_d, DESC)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-medical-records-officer-toolkit", "calc-pediatric-dialysis-nurse-toolkit")
    s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">',
               '<meta property="og:image:alt" content="Renal Care Academy: Pediatric Dialysis Nurse toolkit">', s, count=1)
    stamp = None
    if OUT.exists():   # keep the first publish stamp
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Pediatric Dialysis Nurse · Verification Tools</div>\n'
            '<h1>Pediatric Dialysis Nurse <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Six order-verification tools for the Renal Care Academy Pediatric Dialysis Nurse track. They check arithmetic against a '
            'written order and show published reference ranges; they never decide whether a value is safe for a child. That decision belongs to the '
            'pediatric nephrologist. Use no patient names or identifiers. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/pediatric-dialysis-nurse.html" class="hero-xlink">Pediatric Dialysis Nurse track</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">BSA and fill</a><a class="nav-pill" href="#tool-2">Circuit volume</a>'
             '<a class="nav-pill" href="#tool-3">Blood flow</a><a class="nav-pill" href="#tool-4">Fluid removal</a><a class="nav-pill" href="#tool-5">Fluid overload</a>'
             '<a class="nav-pill" href="#tool-6">Infection rates</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', pills, s, count=1, flags=re.S)
    s = re.sub(r'<main class="container dch-calc">.*?</main>', lambda m: (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    s = re.sub(r'<script>\s*/\* ===== MRO-CALC-CORE.*?</script>', lambda m: (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/pediatric-dialysis-nurse.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Pediatric Dialysis Nurse: the study track</div></a>\n'
           '    <a class="related-card" href="calc-pediatric-egfr.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Pediatric eGFR (bedside CKiD)</div></a>\n'
           '    <a class="related-card" href="ckd-children-young-adults.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Kidney Disease in Children and Young Adults</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', lambda m: rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/medical-records-officer.html" aria-label="Go to related guide">',
                  '<a href="../academy/pediatric-dialysis-nurse.html" aria-label="Go to related guide">')
    body = s.split("<body", 1)[1].replace("dch-calc", "")
    assert "medical-records-officer" not in body and "MRO-CALC" not in body, "template leftovers"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
