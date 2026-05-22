#!/usr/bin/env python3
"""
patch_dr_card.py — Standardise the dr-card signature block across all guides.

Changes made to every guide that has a dr-card:
  1. Remove the existing dr-card from its current position (anywhere inside main
     or elsewhere in the page).
  2. Insert a new, standardised dr-card directly before <!-- RELATED-GUIDES-START -->.
  3. The new card shows the actual avatar photo (photo-contact.webp/jpg), a
     vCard QR code (dr-rivero-contact-qr.svg) instead of the exposed email
     address, and a direct booking link.

Usage:
  python3 patch_dr_card.py            # patch all guides
  python3 patch_dr_card.py --dry-run  # preview only
  python3 patch_dr_card.py --guide understanding-ckd.html
"""

import glob
import os
import re
import sys

GUIDES_DIR = os.path.join(os.path.dirname(__file__), 'guides')
DRY_RUN = '--dry-run' in sys.argv
SINGLE = None
for a in sys.argv[1:]:
    if not a.startswith('--'):
        SINGLE = a

# ---------------------------------------------------------------------------
# New standardised dr-card HTML
# ---------------------------------------------------------------------------
NEW_DR_CARD = '''\
<!-- DR CARD -->
<div class="dr-card-wrap">
<div class="dr-card">
<div class="dr-avatar"><picture><source srcset="../images/photo-contact.webp" type="image/webp"><img src="../images/photo-contact.jpg" alt="Dr. W. G. M. Rivero, MD" width="64" height="64" loading="lazy"></picture></div>
<div class="dr-card-body">
<h4><a href="https://www.williamriveromd.com" style="color:white;text-decoration:none;">W. G. M. Rivero, MD, FPCP, DPSN</a></h4>
<p><span data-lang="en">Specialist in Internal Medicine, Nephrology, and Clinical Nutrition. Practicing integrative and evidence-based nephrology across Quezon City, Pampanga, and Bulacan.</span><span data-lang="tl" class="lang-hidden">Espesyalista sa Panloob na Medisina, Nefrolohiya, at Klinikal na Nutrisyon. Nagpapraktis ng integratibo at ebidensya-batay na nefrolohiya sa Quezon City, Pampanga, at Bulacan.</span><span data-lang="ceb" class="lang-hidden">Espesyalista sa Internal nga Medisina, Nefrolohiya, ug Klinikal nga Nutrisyon. Nagpraktis og integratibo ug ebidensya-base nga nefrolohiya sa Quezon City, Pampanga, ug Bulacan.</span><span data-lang="kap" class="lang-hidden">Espesyalista king Panloob na Medisina, Nefrolohiya, at Klinikal na Nutrisyon. Nagpapraktis ning integratibo at ebidensya-base na nefrolohiya sa Quezon City, Pampanga, at Bulacan.</span></p>
<p class="dr-creds">PRC 0105184 &middot; <a href="https://www.seriousmd.com/doc/williamrivero" target="_blank" rel="noopener" style="color:rgba(255,255,255,.7);">Book an Appointment &rarr;</a></p>
</div>
<div class="dr-qr">
<a href="https://www.seriousmd.com/doc/williamrivero" target="_blank" rel="noopener" aria-label="Scan QR code to save Dr. Rivero's contact information"><img src="../images/dr-rivero-contact-qr.svg" alt="QR code — scan to save Dr. Rivero's contact info" width="80" height="80" loading="lazy"></a>
<p class="dr-qr-label"><span data-lang="en">Scan and save</span><span data-lang="tl" class="lang-hidden">I-scan at i-save</span><span data-lang="ceb" class="lang-hidden">I-scan ug i-save</span><span data-lang="kap" class="lang-hidden">I-scan at i-save</span></p>
</div>
</div>
</div>
'''

# Anchors tried in priority order — first match wins
ANCHORS = [
    '<!-- RELATED-GUIDES-START -->',
    '<!-- RELATED GUIDES',
    '<div class="related-guides"',
    '<footer class="guide-footer"',
    '</main>',
]


def find_anchor(html):
    """Return the index of the best related-guides anchor, or -1."""
    for a in ANCHORS:
        idx = html.find(a)
        if idx != -1:
            return idx
    return -1


def find_dr_card_bounds(html):
    """Return (start, end) character indices of the full dr-card block.

    The block may be preceded by an optional <!-- DR CARD --> comment.
    Detects both class="dr-card" elements and inline-style navy flex divs
    used in some older guides.
    Returns (None, None) if no dr-card found.
    """
    # Pattern 1: class-based dr-card
    m = re.search(r'<div[^>]+class=["\']dr-card["\']', html)
    # Pattern 2: inline-style navy flex div (older guides without CSS class)
    if not m:
        m = re.search(
            r'<div[^>]+background\s*:\s*var\(--navy\)[^>]*display\s*:\s*flex[^>]*>',
            html)

    if not m:
        return None, None

    card_open = m.start()

    # Check for preceding comment (allow up to 200 chars of whitespace/newlines)
    prefix = html[max(0, card_open - 200):card_open]
    comment_m = re.search(r'<!--\s*DR CARD\s*-->\s*$', prefix)
    start = card_open - len(comment_m.group(0)) if comment_m else card_open

    # Walk forward counting <div ...> / </div> to find the matching close
    pos = m.end()
    depth = 1
    while depth > 0 and pos < len(html):
        next_open = re.search(r'<div[\s>]', html[pos:])
        next_close = re.search(r'</div>', html[pos:])
        if not next_close:
            break
        if next_open and next_open.start() < next_close.start():
            depth += 1
            pos += next_open.end()
        else:
            depth -= 1
            if depth == 0:
                pos += next_close.end()
            else:
                pos += next_close.end()

    return start, pos


def patch(html, filename):
    if 'dr-card' not in html:
        return html, False

    anchor_pos = find_anchor(html)
    if anchor_pos == -1:
        print(f'  SKIP {filename}: no related-guides anchor found')
        return html, False

    start, end = find_dr_card_bounds(html)

    # Check whether the new standardised card is already in the right place
    if start is not None:
        gap = html[end:anchor_pos].strip()
        already_correct = (gap == '' and '<!-- DR CARD -->' in html[start:end + 5])
        if already_correct:
            print(f'  OK   {filename}: already standardised')
            return html, False

        # 1. Remove old dr-card block (strip one optional leading newline)
        remove_start = start
        if remove_start > 0 and html[remove_start - 1] == '\n':
            remove_start -= 1
        html = html[:remove_start] + html[end:]

        # 2. Re-locate anchor after removal
        anchor_pos = find_anchor(html)
        if anchor_pos == -1:
            print(f'  WARN {filename}: anchor vanished after card removal — skipping')
            return html, False
    else:
        # No existing dr-card found — just insert the new one
        print(f'  INSERT (no existing card) {filename}')

    # 3. Insert new dr-card immediately before the anchor, with a blank line
    html = html[:anchor_pos] + NEW_DR_CARD + '\n' + html[anchor_pos:]

    return html, True


def main():
    if SINGLE:
        paths = [os.path.join(GUIDES_DIR, SINGLE)]
    else:
        paths = sorted(glob.glob(os.path.join(GUIDES_DIR, '*.html')))

    changed = 0
    for path in paths:
        fname = os.path.basename(path)
        if fname == 'index.html':
            continue
        with open(path, encoding='utf-8') as f:
            original = f.read()

        patched, did_change = patch(original, fname)

        if did_change:
            changed += 1
            print(f'  PATCH {fname}')
            if not DRY_RUN:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(patched)

    print(f'\n{"DRY RUN — " if DRY_RUN else ""}{changed} guide(s) updated.')


if __name__ == '__main__':
    main()
