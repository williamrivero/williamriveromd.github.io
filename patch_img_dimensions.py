#!/usr/bin/env python3
"""
patch_img_dimensions.py — williamriveromd.com
Fixes wrong width/height attributes on <img> tags in all guides/*.html.

Problem: Many images have HTML width×height attrs that don't match the
actual image dimensions (e.g. a 1024×1024 square declared as 1400×787).
This causes incorrect aspect-ratio space reservation → layout shift (CLS).
All affected images already use CSS width:100%;height:auto so correcting
the attrs only changes the reserved layout slot, not the visual output.

What this script does:
  1. Reads actual image dimensions from images/ using Pillow.
  2. For each <img> in every guide, if the declared ratio differs from the
     actual ratio by more than 3%, updates width & height to actual values.
  3. Skips avatar / logo / QR images (CSS controls their display size).
  4. Skips images that are already correctly scaled (same ratio, different
     scale factor — intentional retina serving).
  5. Adds width/height attrs to images that currently have none.

Safe to re-run (idempotent — only writes files that changed).
"""

import re, sys
from pathlib import Path
from PIL import Image as PILImage

GUIDES_DIR = Path('guides')
IMAGES_DIR = Path('images')

# These images are controlled purely by CSS — don't touch their attrs
SKIP_NAMES = {
    'photo-contact.jpg', 'photo-contact.webp',
    'dr-rivero-contact-qr.svg',
    'sjbdc-logo.webp', 'sjrc-logo.webp', 'rcuona-logo.webp',
}

# Ratio-mismatch threshold: flag if |actual_ratio - declared_ratio| / actual > this
RATIO_THRESHOLD = 0.03  # 3%

_dim_cache = {}

def get_dims(src: str):
    norm = src.replace('../images/', 'images/').split('?')[0]
    if norm in _dim_cache:
        return _dim_cache[norm]
    fp = Path(norm)
    if not fp.exists():
        _dim_cache[norm] = (None, None)
        return None, None
    try:
        with PILImage.open(fp) as img:
            _dim_cache[norm] = img.size
            return img.size
    except Exception:
        _dim_cache[norm] = (None, None)
        return None, None


def fix_img_tag(m: re.Match) -> str:
    """Return corrected <img ...> tag string."""
    full   = m.group(0)
    attrs  = m.group(1)

    src_m = re.search(r'\bsrc=["\']([^"\']+)["\']', attrs)
    if not src_m:
        return full

    src  = src_m.group(1)
    fname = Path(src.replace('../images/', '').split('?')[0]).name
    if fname in SKIP_NAMES:
        return full

    aw, ah = get_dims(src)
    if aw is None:
        return full

    w_m = re.search(r'\bwidth=(["\']?)(\d+)\1', attrs)
    h_m = re.search(r'\bheight=(["\']?)(\d+)\1', attrs)

    dw = int(w_m.group(2)) if w_m else None
    dh = int(h_m.group(2)) if h_m else None

    # Decide whether to update
    if dw is not None and dh is not None:
        actual_ratio = aw / ah if ah else 0
        decl_ratio   = dw / dh if dh else 0
        delta = abs(actual_ratio - decl_ratio) / actual_ratio if actual_ratio else 0
        if delta <= RATIO_THRESHOLD:
            return full  # ratio is fine (may be intentional retina scale)
        # Wrong ratio — update to actual dimensions
        new_w, new_h = aw, ah
    else:
        # No attrs at all — add them
        new_w, new_h = aw, ah

    # Apply the fix
    new_attrs = attrs
    if w_m:
        new_attrs = new_attrs[:w_m.start()] + f'width="{new_w}"' + new_attrs[w_m.end():]
        # Recalculate h_m position after w replacement
        h_m2 = re.search(r'\bheight=(["\']?)(\d+)\1', new_attrs)
        if h_m2:
            new_attrs = new_attrs[:h_m2.start()] + f'height="{new_h}"' + new_attrs[h_m2.end():]
        else:
            # Insert height after width attr
            new_attrs = new_attrs.replace(f'width="{new_w}"',
                                          f'width="{new_w}" height="{new_h}"', 1)
    elif h_m:
        new_attrs = new_attrs[:h_m.start()] + f'height="{new_h}"' + new_attrs[h_m.end():]
        # Insert width before height
        new_attrs = new_attrs.replace(f'height="{new_h}"',
                                      f'width="{new_w}" height="{new_h}"', 1)
    else:
        # No width or height — append before the closing >
        # Insert just before the end of attrs
        new_attrs = new_attrs.rstrip() + f' width="{new_w}" height="{new_h}"'

    return f'<img{new_attrs}>'


def patch_guide(html_path: Path, dry_run: bool = False) -> int:
    """Patch one guide file. Returns number of images changed."""
    content = html_path.read_text(encoding='utf-8', errors='replace')

    fixed  = re.sub(r'<img\b([^>]*)>', fix_img_tag, content,
                    flags=re.IGNORECASE | re.DOTALL)

    if fixed == content:
        return 0

    # Count changes
    changes = sum(1 for a, b in zip(
        re.findall(r'<img\b[^>]*>', content, re.IGNORECASE|re.DOTALL),
        re.findall(r'<img\b[^>]*>', fixed,   re.IGNORECASE|re.DOTALL),
    ) if a != b)

    if not dry_run:
        html_path.write_text(fixed, encoding='utf-8')
    return changes


def main():
    dry_run = '--dry-run' in sys.argv
    target  = None
    for arg in sys.argv[1:]:
        if arg.startswith('--guide='):
            target = arg.split('=', 1)[1]

    guides = ([GUIDES_DIR / target] if target
              else sorted(GUIDES_DIR.glob('*.html')))

    total_guides = 0
    total_imgs   = 0

    for g in guides:
        if not g.exists():
            print(f'NOT FOUND: {g}')
            continue
        n = patch_guide(g, dry_run=dry_run)
        if n:
            total_guides += 1
            total_imgs   += n
            status = '[DRY RUN]' if dry_run else '[PATCHED]'
            print(f'{status} {g.name}: {n} image(s) corrected')

    label = 'Would patch' if dry_run else 'Patched'
    print(f'\n{label} {total_imgs} image attr(s) across {total_guides} guide(s).')

if __name__ == '__main__':
    main()
