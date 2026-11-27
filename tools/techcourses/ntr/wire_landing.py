# -*- coding: utf-8 -*-
"""Add the Nephrology Fellow / Resident / Medical Intern track to the hand-maintained Academy landing page (academy/index.html).
Idempotent: every insertion sits between NTR markers and is replaced on re-run; the hero stat counts are bumped only on
the first insertion. Run from the repo root:  python3 tools/techcourses/ntr/wire_landing.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANDING = ROOT / "academy" / "index.html"
HUB = "nephrology-trainee.html"
N = 36
TITLE = "Nephrology Fellow / Resident / Medical Intern"
ICON = '<path d="M4 19V8l8-4 8 4v11"/><path d="M9 19v-5h6v5"/><path d="M12 8v3M10.5 9.5h3"/>'

BLOCKS = {
    "HERO": ('<a class="acad-track" href="vascular-surgeon.html"',
             f'        <a class="acad-track" href="{HUB}" data-family="physicians"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON}</svg></span>'
             f'<span class="acad-track-t"><strong>Nephrology Fellow / Resident / Intern</strong><small>{N} modules</small></span></a>'),
    "BRANCH": ('<a class="tc-branch" href="vascular-surgeon.html">',
               f'    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/nephrology-trainee.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">\n'
               f'      <span class="tc-branch-body"><small>Fellows, residents and interns</small><b>{TITLE}</b><span>For adult and pediatric nephrology fellows, '
               'internal medicine and pediatric residents, and medical interns: physiology and the renal consult, fluids and electrolytes, AKI including tropical causes, '
               'ICU dialysis, CKD and kidney protection, glomerular disease, hemodialysis, PD, transplant, supportive care and Philippine practice.</span>'
               f'<span><strong>{N} modules &middot; six pathways, adult and pediatric &middot; calculators in every module &middot; end-of-course exam</strong></span></span>\n    </a>'),
    "QUAL": ('<tr><td><a href="vascular-surgeon.html">Vascular Surgeon</a></td>',
             f'<tr><td><a href="{HUB}">{TITLE}</a></td><td><ul class="acad-qual">'
             '<li>Interns: one-year post-graduate internship in an APMC-accredited hospital, under direct supervision of a registered physician; not yet licensed. <span class=q-src>PRC</span></li>'
             '<li>Residents: PRC-licensed, appointed to a PCP- or PPS-accredited residency; renal duties per the rotation and the attending&rsquo;s plan. <span class=q-src>PCP &middot; PPS</span></li>'
             '<li>Fellows: appointed to a PSN- (adult) or PNSP-accredited (pediatric) training institution. A paid POD shift requires the DOH and PSN POD qualifications for that unit. <span class=q-src>PSN &middot; PNSP &middot; DOH</span></li></ul></td></tr>'),
    "ONBOARD": ('<tr><td>Access surgeon, new to a dialysis network</td>',
                f'<tr><td>Intern, resident or fellow starting a renal rotation</td><td><a href="{HUB}">{TITLE}</a></td>'
                '<td>Modules 1&ndash;9 and 25: scope and supervision, physiology, the consult, urine, fluids, sodium, potassium, acid-base, AKI and HD emergencies</td><td>Pathway modules; scenario stations; end-of-course exam</td></tr>'),
    "RELATED": ('<a class="related-card has-thumb" href="attending-nephrologist.html">',
                f'    <a class="related-card has-thumb" href="{HUB}">\n      <div class="related-card-tag">Track</div>\n'
                f'      <div class="related-card-title">{TITLE}</div>\n'
                '      <div class="related-card-desc">For physicians in training: the renal consult, fluids and electrolytes, AKI, CKD, glomerular disease, dialysis, transplant and Philippine practice, in six pathways.</div>\n'
                '      <div class="related-card-arrow">Read →</div>\n'
                '          <img class="related-card-thumb" src="../images/nephrology-trainee-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160"></a>'),
}


def main():
    s = LANDING.read_text(encoding="utf-8")
    first = "<!-- NTR-BRANCH-START -->" not in s  # the hero markers are dropped when the tiles are regrouped
    for key, (anchor, block) in BLOCKS.items():
        start, end = f"<!-- NTR-{key}-START -->", f"<!-- NTR-{key}-END -->"
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
    LANDING.write_text(s, encoding="utf-8")
    print("landing wired (first insertion)" if first else "landing re-wired")


if __name__ == "__main__":
    main()
