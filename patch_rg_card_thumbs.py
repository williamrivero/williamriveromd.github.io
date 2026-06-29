#!/usr/bin/env python3
"""
patch_rg_card_thumbs.py — williamriveromd.com

For each guide, scan every .related-card anchor and inject a thumbnail
image if images/{linked-guide-stem}-rg-thumb.webp exists.

Changes made to each qualifying card:
  - Adds 'has-thumb' to the class list
  - Appends <img class="related-card-thumb" ...> inside the anchor (before </a>)

Safe to re-run — already-patched cards are detected by the presence of
class="related-card-thumb" and skipped.

Usage:
    python3 patch_rg_card_thumbs.py               # apply to all guides
    python3 patch_rg_card_thumbs.py --dry-run     # preview
    python3 patch_rg_card_thumbs.py --guide understanding-ckd.html
"""

import re
import sys
from pathlib import Path

GUIDES_DIR = Path(__file__).parent / 'guides'
IMAGES_DIR = Path(__file__).parent / 'images'

# Matches the opening <a> tag of a related-card (single or multi-line)
CARD_OPEN_RE = re.compile(
    r'(<a\b[^>]*class="([^"]*\brelated-card\b[^"]*)"[^>]*href="([^"#][^"]*\.html)"[^>]*>)',
    re.IGNORECASE
)

# Matches </a> that closes the related-card (first one after the opening)
CARD_CLOSE = '</a>'


def thumb_path_for(href: str) -> Path | None:
    stem = Path(href).stem
    p = IMAGES_DIR / f'{stem}-rg-thumb.webp'
    return p if p.exists() else None


def patch_card(match_open: re.Match, after_open: str) -> tuple[str, str, bool]:
    """Return (new_open_tag, new_body_before_close, was_changed)."""
    full_open = match_open.group(1)
    classes = match_open.group(2)
    href = match_open.group(3)

    # Skip if already patched
    if 'related-card-thumb' in after_open:
        return full_open, '', False

    thumb = thumb_path_for(href)
    if not thumb:
        return full_open, '', False

    # Add has-thumb class
    if 'has-thumb' not in classes:
        new_classes = classes.strip() + ' has-thumb'
        new_open = full_open.replace(f'class="{classes}"', f'class="{new_classes}"')
    else:
        new_open = full_open

    img_src = f'../images/{thumb.name}'
    img_tag = (
        f'\n          <img class="related-card-thumb" src="{img_src}"'
        f' alt="" loading="lazy" decoding="async">'
    )
    return new_open, img_tag, True


def patch_guide(filepath: Path, dry_run: bool = False) -> list[str]:
    content = filepath.read_text(encoding='utf-8')
    original = content
    changes = []

    # Process each related-card match
    result = []
    pos = 0
    for m in CARD_OPEN_RE.finditer(content):
        # Copy everything up to the opening tag
        result.append(content[pos:m.start()])
        pos = m.end()

        # Find the closing </a>
        close_idx = content.find(CARD_CLOSE, pos)
        if close_idx == -1:
            result.append(m.group(0))
            continue

        body = content[pos:close_idx]  # content between open and </a>

        new_open, img_tag, changed = patch_card(m, body)
        result.append(new_open)
        result.append(body)
        if changed:
            result.append(img_tag)
            changes.append(Path(m.group(3)).stem)
        result.append(CARD_CLOSE)
        pos = close_idx + len(CARD_CLOSE)

    result.append(content[pos:])
    new_content = ''.join(result)

    if new_content != original:
        if not dry_run:
            filepath.write_text(new_content, encoding='utf-8')
        return changes
    return []


def main():
    dry_run = '--dry-run' in sys.argv
    single = None
    for i, a in enumerate(sys.argv):
        if a == '--guide' and i + 1 < len(sys.argv):
            single = sys.argv[i + 1]
        elif a.startswith('--guide='):
            single = a.split('=', 1)[1]

    files = [GUIDES_DIR / single] if single else sorted(GUIDES_DIR.glob('*.html'))

    patched, unchanged = [], []
    for fp in files:
        if not fp.exists():
            print(f'ERROR: {fp} not found')
            continue
        changes = patch_guide(fp, dry_run=dry_run)
        if changes:
            prefix = '[DRY RUN] ' if dry_run else ''
            print(f'{prefix}{fp.name}: added thumbs for {len(changes)} card(s) → {", ".join(changes[:4])}{"..." if len(changes) > 4 else ""}')
            patched.append(fp.name)
        else:
            unchanged.append(fp.name)

    prefix = '[DRY RUN] ' if dry_run else ''
    print(f'\n{prefix}Patched: {len(patched)}  Unchanged: {len(unchanged)}')


if __name__ == '__main__':
    main()
