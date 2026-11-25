#!/usr/bin/env python3
"""Build guides/calc-dialysis-owner-toolkit.html (Dialysis Unit Owner course calculators).

Starts from the Dialysis Clinical Head toolkit page (same chrome, calc-ui layer and dark-mode styles) and replaces its
metadata, hero, body and calculator script with the owner tools in this folder:
  owner_main.html  -> <main> body (eight calculators)
  owner_core.js    -> pure functions (tested by test_owner_calc.cjs)
  owner_ui.js      -> bindings
Run from the repository root:  python3 tools/techcourses/duo/build_owner_toolkit.py
Then run the calculator patch scripts listed in CLAUDE.md (english-only, calc app, nav pill, handoff, rail, share)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SRC = ROOT / "guides" / "calc-dialysis-clinical-head-toolkit.html"
DST = ROOT / "guides" / "calc-dialysis-owner-toolkit.html"
SLUG = "calc-dialysis-owner-toolkit"
TITLE = "Dialysis Unit Owner Toolkit: 8 Calculators"
DESC = ("Eight calculators for owners and governing boards of hemodialysis units: contribution margin and break-even, cost per "
        "treatment with step costs, physical versus safely staffed capacity, staffing FTE with relief, cash tied in receivables "
        "and runway, loan payment and DSCR, capital payback and NPV, and the patient's yearly share after the PhilHealth package.")
KEYS = ("dialysis break-even calculator, hemodialysis cost per treatment, dialysis unit owner finance, PhilHealth 6350 per session, "
        "dialysis capacity station sessions, debt service coverage ratio clinic loan, dialysis working capital")


def sub1(pat, rep, s, flags=re.S):
    out, n = re.subn(pat, lambda m: rep, s, count=1, flags=flags)
    if n != 1:
        sys.exit(f"pattern not found: {pat[:60]}")
    return out


def main():
    h = SRC.read_text(encoding="utf-8")
    old_t = "Dialysis Clinical Head Toolkit: 12 Calculators"
    h = h.replace(old_t, TITLE)
    h = h.replace("calc-dialysis-clinical-head-toolkit", SLUG)
    h = re.sub(r'(<meta (?:property="og:description"|name="twitter:description"|name="description") content=")[^"]*"',
               lambda m: m.group(1) + DESC + '"', h)
    h = sub1(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{KEYS}">', h)
    h = re.sub(r'<meta property="article:(?:published|modified)_time" content="[^"]*">\n?', "", h)
    h = re.sub(r'"date(?:Published|Modified)": "[^"]*",\s*', "", h)
    og = "https://renalcarematters.com/images/og/calc-dialysis-owner-toolkit.jpg"
    h = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*"', lambda m: m.group(1) + og + '"', h)
    h = re.sub(r'<meta property="og:image:width" content="\d+">', '<meta property="og:image:width" content="1200">', h)
    h = re.sub(r'<meta property="og:image:height" content="\d+">', '<meta property="og:image:height" content="630">', h)
    h = h.replace("A dialysis unit head and nurse reviewing a unit plan together",
                  "Dialysis Unit Owner Toolkit: eight calculators for break-even, capacity, cash, loan coverage, and the patient's share")
    hero = """<section class="hero">
<div class="container">
<div class="hero-tag">Renal Care Academy · Dialysis Unit Owner · Governance Tools</div>
<h1>Dialysis Unit Owner <em>Toolkit</em></h1>
<p class="hero-sub">Eight working tools for the Renal Care Academy Dialysis Unit Owner course: the money behind a safe unit. They do arithmetic, not decisions. A number here never overrides a clinical or technical hold, a staffing rule, or the attending nephrologist. Nothing you enter leaves this page.</p>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; <a href="../academy/dialysis-unit-owner.html" class="hero-xlink">Dialysis Unit Owner course</a></p>
</div>
</section>
<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#c1">Break-even</a><a class="nav-pill" href="#c3">Capacity</a><a class="nav-pill" href="#c5">Cash</a><a class="nav-pill" href="#c6">DSCR</a><a class="nav-pill" href="#c8">Patient share</a>
</div>
</nav>
"""
    h = sub1(r'<section class="hero">.*?</nav>\n', hero, h)
    h = sub1(r'<main class="container dch-calc">.*?</main>', (HERE / "owner_main.html").read_text(encoding="utf-8"), h)
    rel = """<!-- RELATED-GUIDES-START -->
<div class="related-guides" id="related-guides">
  <h2>Related</h2>
  <div class="related-cards">
    <a class="related-card" href="../academy/dialysis-unit-owner.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Dialysis Unit Owner: the course</div></a>
    <a class="related-card" href="calc-dialysis-clinical-head-toolkit.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Dialysis Clinical Head Toolkit</div></a>
    <a class="related-card" href="calculators.html"><div class="related-card-tag">Tools</div><div class="related-card-title">All Calculators &amp; Tools</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""
    h = sub1(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", rel, h)
    core = (HERE / "owner_core.js").read_text(encoding="utf-8") + "\n" + (HERE / "owner_ui.js").read_text(encoding="utf-8")
    h = sub1(r"<script>\s*/\* ===== DCH-CALC-CORE.*?</script>", "<script>\n" + core + "</script>", h)
    if "DCH" in re.sub(r"dch-calc", "", h).replace("DCH-", ""):
        print("note: leftover DCH token(s) remain; review")
    DST.write_text(h, encoding="utf-8")
    print(f"wrote {DST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
