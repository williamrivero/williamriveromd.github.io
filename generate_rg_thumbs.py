#!/usr/bin/env python3
"""
generate_rg_thumbs.py — williamriveromd.com

For each guide, find its og:image webp companion and generate a small
220×160 thumbnail saved as images/{stem}-rg-thumb.webp.
These are used by the related-guides spotlight cards.

Usage:
    python3 generate_rg_thumbs.py               # generate all missing thumbs
    python3 generate_rg_thumbs.py --dry-run     # preview without writing
    python3 generate_rg_thumbs.py --force       # overwrite existing thumbs
    python3 generate_rg_thumbs.py --guide understanding-ckd.html
"""

import re
import sys
from pathlib import Path
from PIL import Image

GUIDES_DIR = Path(__file__).parent / 'guides'
IMAGES_DIR = Path(__file__).parent / 'images'
THUMB_W, THUMB_H = 220, 160
QUALITY = 82

OG_RE = re.compile(r'og:image.*?content="[^"]*/images/([^"]+)"')


def get_og_image(guide_path: Path) -> Path | None:
    text = guide_path.read_text(encoding='utf-8', errors='ignore')
    m = OG_RE.search(text)
    if not m:
        return None
    img_name = m.group(1)
    # Prefer webp companion over png
    img_path = IMAGES_DIR / img_name
    if img_path.suffix.lower() == '.png':
        webp_path = img_path.with_suffix('.webp')
        if webp_path.exists():
            return webp_path
    if img_path.exists():
        return img_path
    return None


def generate_thumb(src: Path, dest: Path) -> bool:
    try:
        with Image.open(src) as img:
            img = img.convert('RGB')
            w, h = img.size
            # Center crop to target aspect ratio
            target_ratio = THUMB_W / THUMB_H
            src_ratio = w / h
            if src_ratio > target_ratio:
                # wider than target — crop sides
                new_w = int(h * target_ratio)
                left = (w - new_w) // 2
                img = img.crop((left, 0, left + new_w, h))
            else:
                # taller than target — crop top/bottom (keep top 65% — most subjects are upper)
                new_h = int(w / target_ratio)
                top = int(h * 0.10)
                top = min(top, h - new_h)
                img = img.crop((0, top, w, top + new_h))
            img = img.resize((THUMB_W, THUMB_H), Image.LANCZOS)
            img.save(dest, 'WEBP', quality=QUALITY, method=6)
        return True
    except Exception as e:
        print(f'  ERROR generating {dest.name}: {e}')
        return False


def main():
    dry_run = '--dry-run' in sys.argv
    force = '--force' in sys.argv
    single = None
    for i, a in enumerate(sys.argv):
        if a == '--guide' and i + 1 < len(sys.argv):
            single = sys.argv[i + 1]
        elif a.startswith('--guide='):
            single = a.split('=', 1)[1]

    files = [GUIDES_DIR / single] if single else sorted(GUIDES_DIR.glob('*.html'))

    generated, skipped, missing = [], [], []
    for guide in files:
        if not guide.exists():
            print(f'ERROR: {guide} not found')
            continue

        stem = guide.stem
        dest = IMAGES_DIR / f'{stem}-rg-thumb.webp'

        if dest.exists() and not force:
            skipped.append(guide.name)
            continue

        src = get_og_image(guide)
        if not src:
            missing.append(guide.name)
            continue

        if dry_run:
            print(f'[DRY RUN] {guide.name} → {dest.name}  (src: {src.name})')
            generated.append(guide.name)
            continue

        ok = generate_thumb(src, dest)
        if ok:
            size_kb = dest.stat().st_size / 1024
            print(f'  {guide.name} → {dest.name}  {size_kb:.1f}KB')
            generated.append(guide.name)
        else:
            missing.append(guide.name)

    prefix = '[DRY RUN] ' if dry_run else ''
    print(f'\n{prefix}Generated: {len(generated)}  Skipped (exists): {len(skipped)}  No og:image: {len(missing)}')
    if missing:
        print('No og:image found for:', ', '.join(missing[:10]), ('...' if len(missing) > 10 else ''))


if __name__ == '__main__':
    main()
