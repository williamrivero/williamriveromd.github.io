# -*- coding: utf-8 -*-
"""Add the Occupational and Physical Therapist track to the hand-maintained Academy landing page (academy/index.html).
Idempotent: every insertion sits between OTPT markers and is replaced on re-run; the hero stat counts are bumped only on
the first insertion. Run from the repo root:  python3 tools/techcourses/otpt/wire_landing.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANDING = ROOT / "academy" / "index.html"
HUB = "occupational-physical-therapist.html"
ICON = '<circle cx="12" cy="4.5" r="2"/><path d="M12 7v6l-3 7"/><path d="M12 13l3 7"/><path d="M8 10h8"/>'

BLOCKS = {
    "HERO": ('<a class="acad-track" href="dialysis-unit-support-staff.html"',
             f'        <a class="acad-track" href="{HUB}" data-family="ancillary"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON}</svg></span>'
             '<span class="acad-track-t"><strong>Occupational and Physical Therapist</strong><small>20 modules</small></span></a>'),
    "BRANCH": ('<a class="tc-branch" href="dialysis-unit-support-staff.html">',
               f'    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/occupational-physical-therapist.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">\n'
               '      <span class="tc-branch-body"><small>Occupational and physical therapists</small><b>Occupational and Physical Therapist</b><span>Renal rehabilitation '
               'for licensed OTs and PTs: why kidney failure makes movement expensive, safe screening and escalation, access protection, function testing, exercise during '
               'and around dialysis, fatigue, falls, home and community access, transplant prehabilitation, and PhilHealth rehabilitation pathways.</span>'
               '<span><strong>20 modules &middot; OT and PT pathways &middot; a six-tool rehabilitation toolkit &middot; eight practical stations &middot; end-of-course exam</strong></span></span>\n    </a>'),
    "QUAL": ('<tr><td><a href="dialysis-unit-support-staff.html">Dialysis Unit Support Staff</a></td>',
             f'<tr><td><a href="{HUB}">Occupational and Physical Therapist</a></td><td><ul class="acad-qual">'
             '<li>Physical therapists: PRC-registered under RA 5680; treatment requires a physician&rsquo;s prescription (Sec. 12). <span class=q-src>RA 5680</span></li>'
             '<li>Occupational therapists: PRC-registered under RA 11241, a separate profession with its own scope; works on referral. <span class=q-src>RA 11241</span></li>'
             '<li>The DOH and PSN dialysis rules list no renal OT or PT position, staffing ratio or renal therapist certificate. <span class=q-src>DOH, PSN</span></li></ul></td></tr>'),
    "ONBOARD": ('<tr><td>Orderly, utility worker, or environmental services aide</td>',
                f'<tr><td>Occupational or physical therapist new to renal care</td><td><a href="{HUB}">Occupational and Physical Therapist</a></td>'
                '<td>Modules 1&ndash;5: role and referral, kidney disease and function, screening, access, assessment</td><td>Practical stations; end-of-course exam</td></tr>'),
    "RELATED": ('<a class="related-card has-thumb" href="dialysis-head-nurse.html">',
                f'    <a class="related-card has-thumb" href="{HUB}">\n      <div class="related-card-tag">Track</div>\n'
                '      <div class="related-card-title">Occupational and Physical Therapist</div>\n'
                '      <div class="related-card-desc">Renal rehabilitation for licensed OTs and PTs: screening and escalation, access protection, function testing, exercise during and around dialysis, falls, home access, and transplant prehabilitation.</div>\n'
                '      <div class="related-card-arrow">Read →</div>\n'
                '          <img class="related-card-thumb" src="../images/occupational-physical-therapist-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160"></a>'),
}


def main():
    s = LANDING.read_text(encoding="utf-8")
    first = "<!-- OTPT-HERO-START -->" not in s
    for key, (anchor, block) in BLOCKS.items():
        start, end = f"<!-- OTPT-{key}-START -->", f"<!-- OTPT-{key}-END -->"
        s = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", s, flags=re.S)
        i = s.find(anchor)
        if i < 0:
            raise SystemExit(f"anchor not found for {key}: {anchor}")
        line_start = s.rfind("\n", 0, i) + 1
        s = s[:line_start] + f"{start}\n{block}\n{end}\n" + s[line_start:]
    if first:
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> subtracks</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> modules</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 20}{m.group(3)}", s, count=1)
        s = re.sub(r'(<div class="acad-col" data-family="ancillary"><div class="acad-col-h">Ancillary staff<small>)(\d+)(</small>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        old = "the medical records officer who keeps the record that proves it,"
        if old in s:
            s = s.replace(old, old + " the occupational and physical therapists who restore movement and daily life,", 1)
    LANDING.write_text(s, encoding="utf-8")
    print("landing wired (first insertion)" if first else "landing re-wired")


if __name__ == "__main__":
    main()
