# -*- coding: utf-8 -*-
"""Build guides/calc-social-worker-toolkit.html from the Medical Records Officer toolkit page (house calculator chrome) and
the Social Worker tool sources in tools/techcourses/sw/toolkit/ (main.html, script.html). Idempotent: rebuilds the page from
the template every time. Run from the repo root:  python3 tools/techcourses/sw/build_toolkit.py
Then test:  node tools/test_sw_calcs.cjs"""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TPL = ROOT / "guides" / "calc-medical-records-officer-toolkit.html"
OUT = ROOT / "guides" / "calc-social-worker-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Social Worker Toolkit: 6 Planning Tools for Kidney Care"
DESC = ("Six planning tools for renal social workers: treatment access cost and gap, household health-spending share (SDG 3.8.2 "
        "marks), PhilHealth hemodialysis session balance, referral aging, workload and coverage, and a quality measure rate.")
KEYS = ("renal social worker calculator, dialysis transport cost calculator Philippines, PhilHealth 156 hemodialysis sessions "
        "balance, catastrophic health spending SDG 3.8.2, social work workload calculator, referral follow-up tracker")
OG = "https://renalcarematters.com/images/og/social-worker-toolkit.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_t = re.search(r"<title>(.*?)</title>", s).group(1)
    s = s.replace(old_t, TITLE)
    old_d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_d, DESC)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-medical-records-officer-toolkit", "calc-social-worker-toolkit")
    s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">',
               '<meta property="og:image:alt" content="Renal Care Academy: Social Worker toolkit">', s, count=1)
    stamp = None
    if OUT.exists():   # keep the first publish stamp
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Social Worker · Planning Tools</div>\n'
            '<h1>Social Worker <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Six working tools for the Renal Care Academy Renal Social Worker track. They do arithmetic and display, '
            'not decisions: benefits belong to PhilHealth, assistance to the receiving agencies, and clinical care to the attending '
            'nephrologist. Use no patient names or identifiers. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/social-worker.html" class="hero-xlink">Renal Social Worker track</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">Access cost</a><a class="nav-pill" href="#tool-2">Spending share</a>'
             '<a class="nav-pill" href="#tool-3">Session balance</a><a class="nav-pill" href="#tool-4">Referral aging</a><a class="nav-pill" href="#tool-5">Workload</a>'
             '<a class="nav-pill" href="#tool-6">Quality rate</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', pills, s, count=1, flags=re.S)
    s = re.sub(r'<main class="container dch-calc">.*?</main>', lambda m: (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    s = re.sub(r'<script>\s*/\* ===== MRO-CALC-CORE.*?</script>', lambda m: (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/social-worker.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Renal Social Worker: the study track</div></a>\n'
           '    <a class="related-card" href="calc-phq9.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">PHQ-9 Depression Screen</div></a>\n'
           '    <a class="related-card" href="philhealth-z-packages.html"><div class="related-card-tag">Guide</div><div class="related-card-title">PhilHealth Benefits: HD, PD and Kidney Transplant</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', lambda m: rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/medical-records-officer.html" aria-label="Go to related guide">',
                  '<a href="../academy/social-worker.html" aria-label="Go to related guide">')
    body = s.split("<body", 1)[1].replace("dch-calc", "")
    assert "medical-records-officer" not in body and "MRO-CALC" not in body, "template leftovers"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
