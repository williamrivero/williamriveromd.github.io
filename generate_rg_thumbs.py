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

Renal Care Academy pages (academy/*.html) are covered too. Their source image is
the page's own circular hero (images/<stem>-vignette-hero.webp), else its og:image;
trainer, final-exam and educator pages, and any module with no image of its own,
borrow the course home's image so every Related Guides card gets a thumbnail.
"""

import re
import sys
from pathlib import Path
from PIL import Image

GUIDES_DIR = Path(__file__).parent / 'guides'
ACADEMY_DIR = Path(__file__).parent / 'academy'
IMAGES_DIR = Path(__file__).parent / 'images'
THUMB_W, THUMB_H = 220, 160
QUALITY = 82

OG_RE = re.compile(r'og:image.*?content="[^"]*/images/([^"]+)"')


def get_og_image(guide_path: Path) -> Path | None:
    if not guide_path.exists():
        return None
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


# pages with no hero or og:image file of their own: borrow a topic image
SOURCE_OVERRIDES = {
    'dialyzer-reprocessing-technician': 'dialyzer-reprocessing-reuse-hero.webp',
    'calc-reprocessing-technician-toolkit': 'dialyzer-reprocessing-reuse-hero.webp',
    'plant-forward-renal-diet': 'plant-forward-renal-diet-01-filipino-plate.webp',  # og PNG is missing
    'same-event-every-role': 'resuscitation-lab-13-team-code-status-and-debrief-vignette-hero.webp',  # team drill page has no image of its own
}

ACADEMY_SUFFIX_RE = re.compile(r'-(?:trainer|final-exam|educator|\d\d-.+)$')


def get_academy_image(page: Path, depth: int = 0) -> Path | None:
    """Hero image for an academy page, falling back to its course home."""
    stem = page.stem
    if stem in SOURCE_OVERRIDES and (IMAGES_DIR / SOURCE_OVERRIDES[stem]).exists():
        return IMAGES_DIR / SOURCE_OVERRIDES[stem]
    for name in (f'{stem}-vignette-hero.webp', f'{stem}-vignette-hero.png'):
        if (IMAGES_DIR / name).exists():
            return IMAGES_DIR / name
    src = get_og_image(page)
    if src:
        return src
    hub = ACADEMY_SUFFIX_RE.sub('', stem)
    if hub != stem and depth == 0:
        return get_academy_image(page.with_name(hub + '.html'), 1)
    return None


def _vignette_scale(src: Path):
    """White-margin scale of a circular vignette hero (patch_vignette_trim.py), or None."""
    if '-vignette-hero' not in src.name:
        return None
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location('patch_vignette_trim', Path(__file__).parent / 'patch_vignette_trim.py')
        vt = importlib.util.module_from_spec(spec); spec.loader.exec_module(vt)
        return vt.margin_scale(src)
    except Exception:
        return None


def generate_thumb(src: Path, dest: Path) -> bool:
    try:
        sc = _vignette_scale(src)
        with Image.open(src) as img:
            img = img.convert('RGB')
            w, h = img.size
            # Vignette heroes are a photo disc inside a white margin: keep only the square inscribed in the
            # photo circle, so a thumbnail never shows white corners (Nov 28 2026).
            if sc:
                side = int(min(w, h) / sc / 1.4142 * 0.98)      # the square inscribed in the photo disc
                side = min(side, int(min(w, h) / sc))
                cx, cy = w // 2, h // 2
                img = img.crop((cx - side // 2, cy - side // 2, cx + side // 2, cy + side // 2))
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

    if single:
        files = [GUIDES_DIR / single] if (GUIDES_DIR / single).exists() else [ACADEMY_DIR / single]
    else:
        files = sorted(GUIDES_DIR.glob('*.html')) + sorted(
            f for f in ACADEMY_DIR.glob('*.html') if ' ' not in f.name and f.name != 'index.html')

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

        if guide.parent == ACADEMY_DIR:
            src = get_academy_image(guide)
        elif guide.stem in SOURCE_OVERRIDES and (IMAGES_DIR / SOURCE_OVERRIDES[guide.stem]).exists():
            src = IMAGES_DIR / SOURCE_OVERRIDES[guide.stem]
        else:
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
