# -*- coding: utf-8 -*-
"""Build guides/calc-transplant-coordinator-toolkit.html from the Medical Records Officer toolkit page (house calculator
chrome) and the RTC tool sources in tools/techcourses/rtc/toolkit/ (main.html, script.html). Idempotent: rebuilds the
page from the template every time. Run from the repo root:  python3 tools/techcourses/rtc/build_toolkit.py"""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TPL = ROOT / "guides" / "calc-medical-records-officer-toolkit.html"
OUT = ROOT / "guides" / "calc-transplant-coordinator-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Transplant Coordinator Toolkit: 7 Planning Tools"
DESC = ("Seven planning tools for kidney transplant coordinators: a four-gate readiness board for recipient and donor, "
        "barrier register aging, the PhilHealth 180-day pre-authorization timer, the 60-day claim filing window, an "
        "out-of-pocket gap estimator with the Z Benefits package codes, a medicine supply runway, and a living donor "
        "follow-up planner.")
KEYS = ("transplant coordinator calculator, PhilHealth kidney transplant pre-authorization 180 days, Z Benefits claim 60 days, "
        "Z025A1 Z026A1 package rates, living donor follow-up schedule, immunosuppressant supply runway")
OG = "https://renalcarematters.com/images/og/transplant-coordinator-toolkit.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_t = re.search(r"<title>(.*?)</title>", s).group(1)
    s = s.replace(old_t, TITLE)
    old_d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_d, DESC)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-medical-records-officer-toolkit", "calc-transplant-coordinator-toolkit")
    s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">',
               '<meta property="og:image:alt" content="Renal Care Academy: Transplant Coordinator toolkit">', s, count=1)
    if OUT.exists():   # keep the first publish stamp
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    else:
        stamp = None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Transplant Coordinator · Planning Tools</div>\n'
            '<h1>Transplant Coordinator <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Seven working tools for the Renal Care Academy Renal Transplant Coordinator track. They do date arithmetic, '
            'counts, and displays, not decisions. Medical suitability, ethics review, consent, and benefits belong to their owners under the '
            'current issuances and your program&rsquo;s approved procedures. Use no patient names or identifiers. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/transplant-coordinator.html" class="hero-xlink">Renal Transplant Coordinator track</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">Readiness</a><a class="nav-pill" href="#tool-3">Pre-authorization</a>'
             '<a class="nav-pill" href="#tool-4">Claim window</a><a class="nav-pill" href="#tool-5">Cost gap</a><a class="nav-pill" href="#tool-7">Donor follow-up</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', pills, s, count=1, flags=re.S)
    s = re.sub(r'<main class="container dch-calc">.*?</main>', (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    s = re.sub(r'<script>\s*/\* ===== MRO-CALC-CORE.*?</script>', (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/transplant-coordinator.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Renal Transplant Coordinator: the study track</div></a>\n'
           '    <a class="related-card" href="calc-donor-esrd-risk.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Living Donor Kidney Failure Risk</div></a>\n'
           '    <a class="related-card" href="philhealth-z-packages.html"><div class="related-card-tag">Guide</div><div class="related-card-title">PhilHealth Benefits: HD, PD and Kidney Transplant</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/medical-records-officer.html" aria-label="Go to related guide">',
                  '<a href="../academy/transplant-coordinator.html" aria-label="Go to related guide">')
    assert "medical-records-officer" not in s.split("<body", 1)[1].replace("dch-calc", ""), "template leftovers"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
