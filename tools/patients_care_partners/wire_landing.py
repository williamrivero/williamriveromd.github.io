# -*- coding: utf-8 -*-
"""Add the Renal Patients and Care Partners track to the hand-maintained Academy landing page (academy/index.html).

Dr. Rivero, Nov 28 2026: "Put the hero tile below the Administrative under Patients." The hero tile carries
data-family="patients"; tools/academy/apply_track_colors.py stacks the Patients column under the Administrative column.
The Tracks section gets its own "Patients & Care Partners Track" heading (which is how apply_track_colors.py learns the
family) and a course card. Idempotent: every insertion sits between PCP markers and is replaced on re-run; the counts
(tracks, subtracks, modules) are bumped only on the first insertion. Run from the repo root:

    python3 tools/patients_care_partners/wire_landing.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "academy" / "index.html"
HUB = "patients-care-partners.html"
N = 32
ICON = ('<circle cx="8" cy="7" r="2.5"/><circle cx="16" cy="7" r="2.5"/><path d="M3 20v-2a5 5 0 0 1 5-5h1"/>'
        '<path d="M21 20v-2a5 5 0 0 0-5-5h-1"/><path d="M12 20s-3-1.8-3-4a1.6 1.6 0 0 1 3-.9 1.6 1.6 0 0 1 3 .9c0 2.2-3 4-3 4z"/>')

HERO = (f'        <a class="acad-track" href="{HUB}" data-family="patients"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON}</svg></span>'
        f'<span class="acad-track-t"><strong>Renal Patients &amp; Care Partners</strong><small>{N} modules</small></span></a>')

TRACK = f"""  <h3 id="track-patients">Patients &amp; Care Partners Track</h3>
  <p>For the people kidney care is for: patients at every stage and the family members and friends who support them. Short lessons in plain words, real Filipino situations, and questions to bring to the next visit. It builds understanding, not self-treatment: any target, dose or machine setting comes from your own kidney team.</p>
  <div class="tc-branches tc-tracks">
    <a class="tc-branch" href="{HUB}"><img class="nc-fig-img" src="../images/academy/landing/patients-care-partners.webp" alt="" loading="lazy" decoding="async" width="960" height="540" onerror="this.remove()">
      <span class="tc-branch-body"><small>Patients, families and care partners</small><b>Renal Patients &amp; Care Partners</b><span>For people living with kidney disease and the people who support them: your test results, treatment choices, medicines, food, fluid, infection and access care, emergencies, PhilHealth, hemodialysis, peritoneal dialysis, transplant, conservative care, and caring for someone without burning out.</span><span><strong>{N} short modules &middot; nine pathways &middot; a toolkit and printable worksheets &middot; free, no account</strong></span></span>
    </a>
  </div>"""

TEXT = [  # (old, new): counts and wording that name the tracks
    ("Renal Care Academy is the free staff-training section of Renal Care Matters,",
     "Renal Care Academy is the free training section of Renal Care Matters,"),
    ("Five tracks, one for each group of staff in a dialysis unit, with twenty-seven subtracks between them.",
     "Six tracks: five for the staff of a dialysis unit and one for patients and their care partners, with twenty-eight subtracks between them."),
    ("Five tracks and twenty-seven subtracks for nephrology nurses, renal care physicians, renal technicians, ancillary staff, and administrative staff,",
     "Six tracks and twenty-eight subtracks for nephrology nurses, renal care physicians, renal technicians, ancillary staff, administrative staff, and patients and care partners,"),
]


def strip(s, key):
    start, end = f"<!-- PCP-{key}-START -->", f"<!-- PCP-{key}-END -->"
    return re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", s, flags=re.S), start, end


def main():
    s = LANDING.read_text(encoding="utf-8")
    first = "<!-- PCP-TRACK-START -->" not in s
    # retire the earlier callout (generate_patients_care_partners.py, Nov 28 2026 morning)
    s = re.sub(r"<!-- PCP-START -->.*?<!-- PCP-END -->\n?", "", s, flags=re.S)

    # hero tile: after the last Administrative tile (apply_track_colors.py regroups and drops the markers)
    s, start, end = strip(s, "HERO")
    if f'class="acad-track" href="{HUB}"' not in s:
        nav = re.search(r'<nav class="acad-tracks[^"]*"[^>]*>.*?</nav>', s, re.S)
        if not nav:
            raise SystemExit("hero track nav not found")
        tiles = list(re.finditer(r'<a class="acad-track[^"]*"[^>]*data-family="administrative"[^>]*>.*?</a>', nav.group(0), re.S))
        at = nav.start() + (tiles[-1].end() if tiles else nav.group(0).rfind("</nav>"))
        s = s[:at] + f"\n{start}\n{HERO}\n{end}" + s[at:]

    # Tracks section: after the Administrative Staff Track's card grid
    s, start, end = strip(s, "TRACK")
    i = s.find('<h3 id="track-administrative">')
    j = s.find("</section>", i)
    if i < 0 or j < 0:
        raise SystemExit("Administrative Staff Track heading not found")
    s = s[:j] + f"{start}\n{TRACK}\n{end}\n" + s[j:]

    for old, new in TEXT:
        s = s.replace(old, new)
    if first:
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> tracks</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> subtracks</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        s = re.sub(r'(<span class="acad-stat"><b>)(\d+)(</b> modules</span>)', lambda m: f"{m.group(1)}{int(m.group(2)) + N}{m.group(3)}", s, count=1)
    LANDING.write_text(s, encoding="utf-8")
    print("landing wired (first insertion)" if first else "landing re-wired")


if __name__ == "__main__":
    main()
