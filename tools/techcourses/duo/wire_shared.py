#!/usr/bin/env python3
"""Idempotent edits the Dialysis Unit Owner track needs in shared files, kept in one place so a parallel session that rewrites
a shared file cannot silently drop them.

    python3 tools/techcourses/duo/wire_shared.py            # apply to the working tree
    python3 tools/techcourses/duo/wire_shared.py --stage    # stage HEAD + these edits only (other sessions' edits stay unstaged)
    python3 tools/techcourses/duo/wire_shared.py --check    # exit 1 if any edit is missing from the working tree

Files: generate_tech_courses.py (PACKAGES, track icon), tools/academy/publish_academy.py (prefix), build_academy_og.py (share
card), guides/calculators.html (toolkit card), academy/index.html (hero tile, family count, stat chips, administrative card,
qualifications, onboarding, career move, related card)."""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HUB = "dialysis-unit-owner"
MODULES = 24
ICON = '<path d="M3 21h18"/><path d="M4 10h16"/><path d="M12 3l8 5H4z"/><path d="M6 10v9M10 10v9M14 10v9M18 10v9"/>'


def gen(s):
    m = re.search(r'^PACKAGES = \[(.*)\]$', s, re.M)
    if '"duo"' not in m.group(1):
        s = s[:m.end() - 1] + ', "duo"]' + s[m.end():]
    if f'"{HUB}":' not in s:
        s = s.replace('    "dialysis-biomedical-technician":', f"    \"{HUB}\": '{ICON}',\n    \"dialysis-biomedical-technician\":", 1)
    return s


def pub(s):
    if f'"{HUB}"' not in s:
        s = re.sub(r'(PREFIXES = \(.*?)\)\n', lambda m: m.group(1) + f', "{HUB}")\n', s, count=1, flags=re.S)
    return s


def og(s):
    if f'"{HUB}":' not in s:
        i = s.find('    "philhealth-claims":')
        s = s[:i] + (f'    "{HUB}": ("academy/{HUB}.html", "administrative", "Dialysis Unit Owner",\n'
                     '                            "GOVERNANCE AND STEWARDSHIP", "24 modules · 8 owner calculators · capstone"),\n') + s[i:]
    return s


CALC_CARD = '''<a class="related-card has-thumb" href="calc-dialysis-owner-toolkit.html">
<div class="related-card-tag">New · Unit Owner · Governance</div>
<div class="related-card-title">Dialysis Unit Owner Toolkit</div>
<div class="related-card-desc">Eight governance tools: contribution and break-even (rejects a negative contribution), cost per treatment with step costs, physical versus safely staffed capacity, FTE with relief, cash tied in receivables and runway, loan payment and DSCR, payback and NPV, and the patient&rsquo;s yearly share with no co-payment for covered sessions.</div>
<div class="related-card-arrow">Open →</div>

          <img class="related-card-thumb" src="../images/calc-dialysis-owner-toolkit-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160"></a>
'''


def calcs(s):
    if "calc-dialysis-owner-toolkit.html" not in s:
        i = s.find('<a class="related-card has-thumb" href="calc-dialysis-shift-coverage.html">')
        s = s[:i] + CALC_CARD + s[i:]
    return s


def after(s, anchor, block, end="</a>"):
    i = s.find(anchor)
    if i < 0:
        raise SystemExit(f"anchor not found: {anchor[:70]}")
    j = s.find(end, i) + len(end)
    return s[:j] + block + s[j:]


def after_row(s, anchor, row):
    i = s.find(anchor)
    if i < 0:
        raise SystemExit(f"anchor not found: {anchor[:70]}")
    j = s.find("</tr>", i) + 5
    return s[:j] + "\n" + row + s[j:]


def landing(s):
    if f'class="acad-track" href="{HUB}.html"' not in s:
        s = after(s, '<a class="acad-track" href="philhealth-claims.html" data-family="administrative">',
                  f'\n        <a class="acad-track" href="{HUB}.html" data-family="administrative"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON}</svg></span><span class="acad-track-t"><strong>Dialysis Unit Owner</strong><small>{MODULES} modules</small></span></a>')
        s = re.sub(r'(<div class="acad-col" data-family="administrative"><div class="acad-col-h">Administrative<small>)(\d+)(</small>)',
                   lambda m: f"{m.group(1)}{int(m.group(2)) + 1}{m.group(3)}", s, count=1)
        s = re.sub(r'<b>(\d+)</b> subtracks</span><span class="acad-stat"><b>(\d+)</b> modules',
                   lambda m: f'<b>{int(m.group(1)) + 1}</b> subtracks</span><span class="acad-stat"><b>{int(m.group(2)) + MODULES}</b> modules', s, count=1)
    old = "<p>The people who keep a unit licensed, staffed, and paid: the operations manager and the PhilHealth liaison and claims team.</p>"
    if old in s:
        s = s.replace(old, "<p>The people who keep a unit licensed, staffed, paid, and governed: the operations manager, the PhilHealth liaison and claims team, and the owners and boards who answer for the whole service.</p>", 1)
    if f'<a class="tc-branch" href="{HUB}.html">' not in s:
        s = after(s, '<a class="tc-branch" href="philhealth-claims.html">', f'''
    <a class="tc-branch" href="{HUB}.html"><img class="nc-fig-img" src="../images/academy/landing/{HUB}.webp" alt="" loading="lazy" decoding="async" width="960" height="540">
      <span class="tc-branch-body"><small>Owners and boards</small><b>Dialysis Unit Owner</b><span>For owners, investors, and boards of dialysis units: the owner&rsquo;s authority and its limits, kidney care for non-clinicians, licensing, protected clinical leadership, ethics, capital, safe capacity, workforce, water and infection, PhilHealth stewardship, claims integrity, money, quality, privacy, continuity, and responsible exit.</span><span><strong>{MODULES} modules &middot; 8 owner calculators &middot; a capstone &middot; end-of-course exam</strong></span></span>
    </a>''')
    if f'<tr><td><a href="{HUB}.html">Dialysis Unit Owner</a></td>' not in s:
        s = after_row(s, '<tr><td><a href="philhealth-claims.html">PhilHealth Liaison/Claims Officer</a></td><td><ul class="acad-qual">',
                      f'<tr><td><a href="{HUB}.html">Dialysis Unit Owner</a></td><td><ul class="acad-qual"><li>No owner degree, license, or training credential was found in the DOH or PSN hemodialysis rules. Legal eligibility to own and the facility&rsquo;s license need separate verification with counsel and the CHD. <span class=q-src>DOH, PSN</span></li><li>Owning a unit confers no clinical or technical authority; an owner who also practices needs that role&rsquo;s own credentials and appointment. The course&rsquo;s entry expectations are Academy recommendations only.</li></ul></td></tr>')
    if "<tr><td>Owner, investor, or board member</td>" not in s:
        s = after_row(s, "<tr><td>PhilHealth liaison, claims officer, or clerk</td>",
                      f'<tr><td>Owner, investor, or board member</td><td><a href="{HUB}.html">Dialysis Unit Owner</a></td><td>Modules 1, 2, 5, and 8: authority and its limits, the patient&rsquo;s week, ethics, safe capacity</td><td>Portfolio; capstone with a clinical reviewer; end-of-course exam</td></tr>')
    if "<tr><td>Clinician, manager, or family member</td><td>Owner or board member" not in s:
        s = after_row(s, "<tr><td>Head nurse</td><td>Unit operations manager or unit manager</td>",
                      f'<tr><td>Clinician, manager, or family member</td><td>Owner or board member of a dialysis unit</td><td><a href="{HUB}.html">Dialysis Unit Owner</a>, with <a href="dialysis-clinical-head.html">Dialysis Clinical Head</a> Module 1 for the clinical side</td></tr>')
    if f'<a class="related-card has-thumb" href="{HUB}.html">' not in s:
        s = after(s, '<a class="related-card has-thumb" href="dialysis-unit-manager.html">', f'''
    <a class="related-card has-thumb" href="{HUB}.html">
      <div class="related-card-tag">Track</div>
      <div class="related-card-title">Dialysis Unit Owner</div>
      <div class="related-card-desc">For owners, investors, and boards: authority and its limits, licensing, ethics, safe capacity, workforce, water and infection, PhilHealth stewardship, money, quality, privacy, continuity, and responsible exit. 24 modules and 8 owner calculators.</div>
      <div class="related-card-arrow">Read →</div>
          <img class="related-card-thumb" src="../images/{HUB}-rg-thumb.webp" alt="" loading="lazy" decoding="async" width="220" height="160"></a>''')
    return s


EDITS = {"generate_tech_courses.py": gen, "tools/academy/publish_academy.py": pub, "build_academy_og.py": og,
         "guides/calculators.html": calcs, "academy/index.html": landing}


def strip_unpublished_related():
    """Drop Related cards on the Owner pages that point to Academy pages not yet in git (another session's unpublished track).
    The next regeneration after that track is committed restores them."""
    tracked = set(git("ls-files", "academy").decode().split())
    for page in sorted((ROOT / "academy").glob(f"{HUB}*.html")):
        s = page.read_text(encoding="utf-8")
        def keep(m):
            href = m.group(1)
            if href.startswith(("../", "http")) or href.startswith(HUB) or f"academy/{href}" in tracked:
                return m.group(0)
            return ""
        new = re.sub(r'\n    <a class="related-card has-thumb" href="([^"]+)">.*?</a>', keep, s, flags=re.S)
        if new != s:
            page.write_text(new, encoding="utf-8")
            print(f"removed unpublished related card(s) from {page.name}")


def git(*a, inp=None):
    return subprocess.run(["git", *a], cwd=ROOT, input=inp, capture_output=True, check=True).stdout


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    bad = 0
    if mode == "":
        strip_unpublished_related()
    for rel, fn in EDITS.items():
        p = ROOT / rel
        if mode == "--stage":
            head = git("show", f"HEAD:{rel}").decode("utf-8")
            new = fn(head)
            if rel == "academy/index.html":     # carry the rebuilt landing share card (build_academy_og.py --only academy-index --patch)
                cur = p.read_text(encoding="utf-8")
                for pat in (r'<meta property="og:image" content="[^"]*">', r'<meta name="twitter:image" content="[^"]*">'):
                    m = re.search(pat, cur)
                    if m:
                        new = re.sub(pat, lambda _: m.group(0), new, count=1)
            if new != head:
                blob = git("hash-object", "-w", "--stdin", inp=new.encode("utf-8")).decode().strip()
                mode_bits = git("ls-files", "-s", rel).decode().split()[0]
                git("update-index", "--cacheinfo", f"{mode_bits},{blob},{rel}")
                print(f"staged {rel}")
        else:
            cur = p.read_text(encoding="utf-8")
            new = fn(cur)
            if new != cur:
                if mode == "--check":
                    print(f"missing edits: {rel}"); bad += 1
                else:
                    p.write_text(new, encoding="utf-8"); print(f"updated {rel}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
