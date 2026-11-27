# -*- coding: utf-8 -*-
"""Add the Attending Pediatric Nephrologist track to the hand-maintained Academy landing page (academy/index.html).
Idempotent: every insertion sits between APN markers and is replaced on re-run; the hero stat counts are bumped only on
the first insertion. Run from the repo root:  python3 tools/techcourses/apn/wire_landing.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANDING = ROOT / "academy" / "index.html"
HUB = "attending-pediatric-nephrologist.html"
N = 29
ICON = '<circle cx="12" cy="6" r="3"/><path d="M7 21v-4a5 5 0 0 1 10 0v4"/><path d="M9 13h6"/><path d="M4 10l2 2M20 10l-2 2"/>'

BLOCKS = {
    "HERO": ('<a class="acad-track" href="vascular-surgeon.html"',
             f'        <a class="acad-track" href="{HUB}" data-family="physicians"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON}</svg></span>'
             f'<span class="acad-track-t"><strong>Attending Pediatric Nephrologist</strong><small>{N} modules</small></span></a>'),
    "BRANCH": ('<a class="tc-branch" href="vascular-surgeon.html">',
               f'    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/attending-pediatric-nephrologist.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">\n'
               '      <span class="tc-branch-body"><small>Attending pediatric nephrologists</small><b>Attending Pediatric Nephrologist</b><span>For pediatric nephrologists and '
               'fellows: the growing kidney, fluid and electrolyte emergencies, hypertension, CAKUT and UTI, nephrotic and nephritic disease, HUS, neonatal and pediatric '
               'AKI, CKRT, CKD and growth, peritoneal dialysis and hemodialysis in children, transplantation, medicines, safeguarding and PhilHealth.</span>'
               f'<span><strong>{N} modules &middot; seven on dialysis &middot; a capstone &middot; calculators in every module &middot; end-of-course exam</strong></span></span>\n    </a>'),
    "QUAL": ('<tr><td><a href="vascular-surgeon.html">Vascular Surgeon</a></td>',
             f'<tr><td><a href="{HUB}">Attending Pediatric Nephrologist</a></td><td><ul class="acad-qual">'
             '<li>PRC-licensed, with pediatrics credentials and pediatric nephrology training and certification through PNSP and the specialty board; adult nephrology status is not a substitute. <span class=q-src>PNSP</span></li>'
             '<li>Hospital privileges delineated by age and size, modality and procedure; PhilHealth professional accreditation where required (the pediatric PD package names the attending pediatric nephrologist). <span class=q-src>PhilHealth</span></li></ul></td></tr>'),
    "ONBOARD": ('<tr><td>Access surgeon, new to a dialysis network</td>',
                f'<tr><td>Pediatric nephrologist starting an attending post</td><td><a href="{HUB}">Attending Pediatric Nephrologist</a></td>'
                '<td>Modules 1&ndash;4, 16 and 20&ndash;25: responsibility, assessment, fluids and electrolyte emergencies, CKRT, and pediatric PD and HD</td><td>Scenario stations; end-of-course exam</td></tr>'),
    "RELATED": ('<a class="related-card has-thumb" href="attending-nephrologist.html">',
                f'    <a class="related-card has-thumb" href="{HUB}">\n      <div class="related-card-tag">Track</div>\n'
                '      <div class="related-card-title">Attending Pediatric Nephrologist</div>\n'
                '      <div class="related-card-desc">For pediatric nephrologists: the growing kidney, glomerular and structural disease, AKI and CKRT, CKD and growth, PD and HD in children, transplant and safeguarding.</div>\n'
                '      <div class="related-card-arrow">Read →</div>\n'
                '          <img class="related-card-thumb" src="../images/attending-pediatric-nephrologist-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160"></a>'),
}


def main():
    s = LANDING.read_text(encoding="utf-8")
    first = "<!-- APN-BRANCH-START -->" not in s  # the hero markers are dropped when the tiles are regrouped
    for key, (anchor, block) in BLOCKS.items():
        start, end = f"<!-- APN-{key}-START -->", f"<!-- APN-{key}-END -->"
        s = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", s, flags=re.S)
        if key == "HERO" and f'class="acad-track" href="{HUB}"' in s:
            continue  # already present (regrouped by apply_track_colors.py)
        i = s.find(anchor)
        if i < 0:
            raise SystemExit(f"anchor not found for {key}: {anchor}")
        line_start = s.rfind("\n", 0, i) + 1
        s = s[:line_start] + f"{start}\n{block}\n{end}\n" + s[line_start:]
    if first:
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> subtracks</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> modules</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + N}{m.group(3)}", s, count=1)
        s = re.sub(r'(<div class="acad-col" data-family="physicians"><div class="acad-col-h">Physicians<small>)(\d+)(</small>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        old = "to the attending nephrologist,"
        if old in s:
            s = s.replace(old, "to the attending nephrologist and the attending pediatric nephrologist,", 1)
    LANDING.write_text(s, encoding="utf-8")
    print("landing wired (first insertion)" if first else "landing re-wired")


if __name__ == "__main__":
    main()
