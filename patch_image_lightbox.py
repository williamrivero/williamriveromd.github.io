#!/usr/bin/env python3
"""
patch_image_lightbox.py

Replaces the <script src="../assets/image-open.js" ...> tag with
<script src="../assets/image-lightbox.js" defer></script> in every guide
that references image-open.js.  Also strips any stale inline zoomable-
dblclick handler injected by patch_zoomable_dblclick.py (superseded).

Usage:
  python3 patch_image_lightbox.py            # patch all guides
  python3 patch_image_lightbox.py --dry-run  # preview without writing
  python3 patch_image_lightbox.py --guide hematuria-blood-in-urine.html
"""

import argparse
import os
import re

GUIDES_DIR = os.path.join(os.path.dirname(__file__), 'guides')

OLD_TAG  = '<script src="../assets/image-open.js" defer></script>'
NEW_TAG  = '<script src="../assets/image-lightbox.js" defer></script>'

# Also remove the inline zoomable-dblclick block injected by the old patch
DBLCLICK_MARKER = 'zoomable-dblclick-handler'


def patch_file(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # 1. Swap script tag
    if OLD_TAG in html:
        html = html.replace(OLD_TAG, NEW_TAG, 1)
        changed = True

    # 2. Remove inline zoomable-dblclick block if present
    if DBLCLICK_MARKER in html:
        # Match <script>/* zoomable-dblclick-handler */...IIFE...</script>
        pattern = r'<script>/\* zoomable-dblclick-handler \*/[\s\S]*?</script>\n?'
        new_html, n = re.subn(pattern, '', html)
        if n:
            html = new_html
            changed = True

    if not changed:
        return 'skip'

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
    return 'patched'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--guide')
    args = parser.parse_args()

    if args.guide:
        files = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        files = sorted(
            os.path.join(GUIDES_DIR, f)
            for f in os.listdir(GUIDES_DIR)
            if f.endswith('.html')
        )

    counts = {'patched': 0, 'skip': 0}
    for path in files:
        result = patch_file(path, dry_run=args.dry_run)
        counts[result] += 1
        if result == 'patched':
            label = '[DRY RUN] would patch' if args.dry_run else 'patched'
            print(f'  {label}: {os.path.basename(path)}')

    print(f"\nDone. patched={counts['patched']}  skipped={counts['skip']}")


if __name__ == '__main__':
    main()
