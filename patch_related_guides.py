#!/usr/bin/env python3
"""
Fix related-guides CSS/HTML inconsistencies across all guides.

Issue 1: Remove .related-guides { ... } override from second <style> block.
         These overrides strip max-width:860px and margin:auto, causing the
         section to bleed full-width.

Issue 2: Replace class="related-grid" with class="related-cards" in HTML.
         Master CSS defines .related-cards; .related-grid has no grid styling.

Usage:
    python3 patch_related_guides.py --dry-run      # preview changes
    python3 patch_related_guides.py                # apply changes
    python3 patch_related_guides.py --guide foo.html  # single guide
"""

import os
import re
import sys
from pathlib import Path

GUIDES_DIR = Path(__file__).parent / 'guides'


def fix_guide(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # ── Issue 2: related-grid → related-cards ─────────────────────────────────
    if 'class="related-grid"' in content:
        content = content.replace('class="related-grid"', 'class="related-cards"')
        changes.append('related-grid → related-cards')

    # ── Issue 1: remove .related-guides override from second <style> block ────
    # Locate all <style>…</style> blocks (master CSS is the first one)
    style_re = re.compile(r'(<style>)(.*?)(</style>)', re.DOTALL | re.IGNORECASE)
    style_matches = list(style_re.finditer(content))

    if len(style_matches) >= 2:
        second = style_matches[1]
        second_body = second.group(2)

        # Match .related-guides { ... } — no nested braces in any of these rules
        rg_re = re.compile(
            r'[ \t]*\.related-guides\s*\{[^}]*\}\n?',
            re.DOTALL
        )
        new_body, n_subs = rg_re.subn('', second_body)

        if n_subs:
            # Collapse runs of 4+ blank lines left behind by the removal
            new_body = re.sub(r'\n{4,}', '\n\n\n', new_body)
            content = (
                content[:second.start()] +
                second.group(1) + new_body + second.group(3) +
                content[second.end():]
            )
            changes.append('removed .related-guides override from second <style>')

    if content != original:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return changes

    return []


def main():
    dry_run = '--dry-run' in sys.argv
    single = next((a.split('--guide=')[-1] for a in sys.argv if a.startswith('--guide=')), None)
    if not single:
        for i, a in enumerate(sys.argv):
            if a == '--guide' and i + 1 < len(sys.argv):
                single = sys.argv[i + 1]
                break

    if single:
        files = [GUIDES_DIR / single]
    else:
        files = sorted(GUIDES_DIR.glob('*.html'))

    fixed, unchanged = [], []
    for fp in files:
        if not fp.exists():
            print(f'ERROR: {fp} not found')
            continue
        changes = fix_guide(fp, dry_run=dry_run)
        if changes:
            prefix = '[DRY RUN] ' if dry_run else ''
            print(f'{prefix}{fp.name}: {" | ".join(changes)}')
            fixed.append(fp.name)
        else:
            unchanged.append(fp.name)

    prefix = '[DRY RUN] ' if dry_run else ''
    print(f'\n{prefix}Fixed: {len(fixed)}  Unchanged: {len(unchanged)}')
    if fixed and dry_run:
        print('Run without --dry-run to apply.')


if __name__ == '__main__':
    main()
