# -*- coding: utf-8 -*-
"""Build guides/calc-patient-care-partner-toolkit.html from the Social Worker toolkit page (house calculator chrome) and the
tool sources in tools/patients_care_partners/toolkit/ (main.html, script.html). Idempotent. Run from the repo root:
    python3 tools/patients_care_partners/build_toolkit.py      then test:  node tools/test_pcp_calcs.cjs
Design rule: every target (fluid amount, sodium target, target weight) is typed by the learner from their own team's plan;
no tool supplies a clinical target."""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TPL = ROOT / "guides" / "calc-social-worker-toolkit.html"
OUT = ROOT / "guides" / "calc-patient-care-partner-toolkit.html"
SRC = Path(__file__).resolve().parent / "toolkit"

TITLE = "Patient and Care Partner Toolkit: 6 Kidney Care Tools"
DESC = ("Six small tools for people with kidney disease and their care partners: results trend log, food label sodium counter, "
        "fluid counter using your own team's amount, weight gain between hemodialysis sessions, PhilHealth hemodialysis session "
        "counter, and a transplant medicine clock with refill planner. No tool sets a clinical target.")
KEYS = ("kidney patient tools, eGFR trend tracker, food label sodium calculator Philippines, dialysis fluid counter, interdialytic "
        "weight gain calculator, PhilHealth 156 hemodialysis sessions counter, transplant medicine refill planner")
OG = "https://renalcarematters.com/images/og/calc-patient-care-partner-toolkit-og.jpg"


def main():
    s = TPL.read_text(encoding="utf-8")
    old_title = re.search(r"<title>(.*?)</title>", s).group(1)
    old_desc = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    s = s.replace(old_title, TITLE)       # <title>, og:title, twitter:title and the JSON-LD name (Nov 28 2026: only <title> was swapped)
    s = s.replace(old_desc, DESC)         # description, og:description, twitter:description, JSON-LD
    s = re.sub(r'"audience": \{\s*"@type": "MedicalAudience",\s*"audienceType": "clinician"\s*\}',
               '"audience": {"@type": "PeopleAudience", "audienceType": "Patients and caregivers"}', s, count=1)
    s = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{KEYS}">', s, count=1)
    s = s.replace("calc-social-worker-toolkit", "calc-patient-care-partner-toolkit")
    if (ROOT / "images" / "og" / "calc-patient-care-partner-toolkit-og.jpg").exists():
        s = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{OG}">', s, count=1)
        s = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{OG}">', s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content=".*?">', '<meta property="og:image:alt" content="Renal Care Academy: Patient and Care Partner Toolkit">', s, count=1)
    stamp = None
    if OUT.exists():
        m = re.search(r'<meta property="article:published_time" content="([^"]+)"', OUT.read_text(encoding="utf-8"))
        stamp = m.group(1) if m else None
    stamp = stamp or datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    s = re.sub(r'<meta property="article:published_time" content="[^"]+">', f'<meta property="article:published_time" content="{stamp}">', s, count=1)
    hero = ('<section class="hero">\n<div class="container">\n<div class="hero-tag">Renal Care Academy · Patients &amp; Care Partners · Tools</div>\n'
            '<h1>Patient and Care Partner <em>Toolkit</em></h1>\n'
            '<p class="hero-sub">Six small tools that do arithmetic, not decisions. Any target, such as a fluid amount, a sodium target or a '
            'target weight, comes from your own kidney team and is typed in by you. Use no names or identifiers. Nothing you enter leaves this page.</p>\n'
            '<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; '
            '<a href="../academy/patients-care-partners.html" class="hero-xlink">Renal Patients and Care Partners course</a></p>\n</div>\n</section>')
    s = re.sub(r'<section class="hero">.*?</section>', lambda m: hero, s, count=1, flags=re.S)
    pills = ('<nav class="nav-strip">\n<div class="nav-pills">\n<a class="nav-pill" href="#tool-1">Results trend</a><a class="nav-pill" href="#tool-2">Label sodium</a>'
             '<a class="nav-pill" href="#tool-3">Fluid counter</a><a class="nav-pill" href="#tool-4">Weight gain</a><a class="nav-pill" href="#tool-5">Session counter</a>'
             '<a class="nav-pill" href="#tool-6">Medicine clock</a>\n</div>\n</nav>')
    s = re.sub(r'<nav class="nav-strip">.*?</nav>', lambda m: pills, s, count=1, flags=re.S)
    s, k = re.subn(r'<main class="container[^"]*">.*?</main>', lambda m: (SRC / "main.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    assert k == 1, "main block not found in template"
    s, k = re.subn(r'<script>\s*/\* ===== SW-CALC-CORE.*?</script>', lambda m: (SRC / "script.html").read_text(encoding="utf-8").strip(), s, count=1, flags=re.S)
    assert k == 1, "calculator script not found in template"
    rel = ('<div class="related-cards">\n'
           '    <a class="related-card" href="../academy/patients-care-partners.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Renal Patients and Care Partners: the course</div></a>\n'
           '    <a class="related-card" href="sodium-salt-reduction-ckd.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Salt reduction in kidney disease</div></a>\n'
           '    <a class="related-card" href="philhealth-z-packages.html"><div class="related-card-tag">Guide</div><div class="related-card-title">PhilHealth Benefits: HD, PD and Kidney Transplant</div></a>\n'
           '  </div>')
    s = re.sub(r'<div class="related-cards">.*?</div>\s*</div>\s*<!-- RELATED-GUIDES-END -->', lambda m: rel + '\n</div>\n<!-- RELATED-GUIDES-END -->', s, count=1, flags=re.S)
    s = s.replace('<a href="../academy/social-worker.html" aria-label="Go to related guide">', '<a href="../academy/patients-care-partners.html" aria-label="Go to related guide">')
    body = s.split("<body", 1)[1]
    assert "social-worker" not in body and "SW-CALC" not in body and "Social Worker" not in body, "template leftovers"
    OUT.write_text(s, encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
