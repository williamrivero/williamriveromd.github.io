#!/usr/bin/env python3
"""
patch_hero_fullwidth.py — make every guide's LCP (hero) image full-width.

Finds the first content image in each guide (identified by fetchpriority="high",
or the first <img> after <main if not yet patched) and:
  1. Strips max-width from the enclosing <figure>'s inline style.
  2. Removes centering margins (auto) from the figure.
  3. Standardises figure margin to "margin:24px 0".
  4. Ensures the img itself has width:100%;height:auto;display:block.

Safe to re-run (idempotent). Run after patch_hero_fetchpriority.py.

Usage:
  python3 patch_hero_fullwidth.py              # all guides
  python3 patch_hero_fullwidth.py --dry-run    # preview only
  python3 patch_hero_fullwidth.py --guide understanding-ckd.html
"""

import glob
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
GUIDES_DIR = REPO_ROOT / "guides"
DRY_RUN = "--dry-run" in sys.argv
SINGLE = next((a for a in sys.argv[1:] if not a.startswith("--")), None)


def strip_max_width(style: str) -> str:
    """Remove max-width:... declaration from an inline style string."""
    return re.sub(r'max-width\s*:\s*[^;]+;?\s*', '', style).strip().strip(';')


def strip_auto_margin(style: str) -> str:
    """Replace margin values that include 'auto' with a simple vertical margin."""
    # e.g. "margin:24px auto 32px" -> "margin:24px 0"
    def _replace(m):
        val = m.group(1)
        if 'auto' in val:
            return 'margin:24px 0'
        return m.group(0)
    return re.sub(r'margin\s*:\s*([^;]+)', _replace, style)


def normalise_img_style(style: str) -> str:
    """Ensure the img has width:100%, height:auto, display:block.
    Only ADD missing properties; do not modify existing ones to avoid
    clobbering other properties like border-radius or box-shadow.
    """
    props_to_add = []
    if not re.search(r'\bwidth\s*:', style):
        props_to_add.append('width:100%')
    if not re.search(r'\bheight\s*:', style):
        props_to_add.append('height:auto')
    if not re.search(r'\bdisplay\s*:', style):
        props_to_add.append('display:block')
    if props_to_add:
        base = style.rstrip('; ')
        style = base + (';' if base else '') + ';'.join(props_to_add)
    return style


def patch(html: str, filename: str):
    # Find the hero img (fetchpriority="high" or first img after <main>)
    main_pos = html.find('<main')
    if main_pos == -1:
        main_pos = 0

    img_m = re.search(r'<img\b[^>]*fetchpriority\s*=\s*["\']high["\'][^>]*>', html[main_pos:], re.I)
    if not img_m:
        img_m = re.search(r'<img\b[^>]*>', html[main_pos:], re.I)
    if not img_m:
        return html, False

    img_abs_start = main_pos + img_m.start()

    # ── 1. Fix the enclosing <figure> ──────────────────────────────────────────
    search_window = html[max(0, img_abs_start - 400):img_abs_start]
    fig_m = re.search(r'<figure([^>]*)>(?=[^<]*$)', search_window)  # last figure before img
    if not fig_m:
        # Try a broader search
        fig_m = list(re.finditer(r'<figure([^>]*)>', search_window))
        fig_m = fig_m[-1] if fig_m else None

    changed = False
    if fig_m:
        fig_attrs_orig = fig_m.group(1)
        style_m = re.search(r'\s+style="([^"]*)"', fig_attrs_orig)
        if style_m:
            orig_style = style_m.group(1)
            new_style = strip_max_width(orig_style)
            new_style = strip_auto_margin(new_style)
            # Ensure margin:24px 0 exists
            if not re.search(r'margin\s*:', new_style):
                new_style = ('margin:24px 0;' + new_style).strip('; ')
            new_style = re.sub(r';\s*;', ';', new_style).strip('; ')

            if new_style != orig_style:
                fig_abs_start = max(0, img_abs_start - 400) + fig_m.start()
                old_fig_tag = '<figure' + fig_attrs_orig + '>'
                new_fig_tag = '<figure style="' + new_style + '">' if new_style else '<figure>'
                html = html[:fig_abs_start] + html[fig_abs_start:].replace(old_fig_tag, new_fig_tag, 1)
                changed = True
        else:
            # No style attribute — add one
            fig_abs_start = max(0, img_abs_start - 400) + fig_m.start()
            old_fig_tag = '<figure' + fig_attrs_orig + '>'
            new_fig_tag = '<figure style="margin:24px 0">'
            html = html[:fig_abs_start] + html[fig_abs_start:].replace(old_fig_tag, new_fig_tag, 1)
            changed = True

    # ── 2. Fix the img style ──────────────────────────────────────────────────
    # Re-locate the img after potential figure change
    img_m2 = re.search(r'<img\b[^>]*fetchpriority\s*=\s*["\']high["\'][^>]*>', html[main_pos:], re.I)
    if not img_m2:
        img_m2 = re.search(r'<img\b[^>]*>', html[main_pos:], re.I)
    if img_m2:
        img_tag_orig = img_m2.group(0)
        sty_m = re.search(r'\s+style="([^"]*)"', img_tag_orig)
        if sty_m:
            orig_img_style = sty_m.group(1)
            new_img_style = normalise_img_style(orig_img_style)
            if new_img_style != orig_img_style:
                new_img_tag = img_tag_orig.replace(sty_m.group(0), f' style="{new_img_style}"')
                img_abs = main_pos + img_m2.start()
                html = html[:img_abs] + new_img_tag + html[img_abs + len(img_tag_orig):]
                changed = True
        else:
            # Add style attribute
            img_abs = main_pos + img_m2.start()
            img_tag_orig = img_m2.group(0)
            new_img_tag = img_tag_orig.replace('<img ', '<img style="width:100%;height:auto;display:block;" ', 1)
            html = html[:img_abs] + new_img_tag + html[img_abs + len(img_tag_orig):]
            changed = True

    return html, changed


def main():
    if SINGLE:
        paths = [GUIDES_DIR / SINGLE]
    else:
        paths = sorted(GUIDES_DIR.glob("*.html"))

    updated = skipped = 0
    for path in paths:
        if path.name == "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        patched, changed = patch(html, path.name)
        if changed:
            updated += 1
            print(f"  PATCH  {path.name}")
            if not DRY_RUN:
                path.write_text(patched, encoding="utf-8")
        else:
            skipped += 1

    label = "DRY RUN — " if DRY_RUN else ""
    print(f"\n{label}{updated} updated, {skipped} already correct/skipped.")


if __name__ == "__main__":
    main()
