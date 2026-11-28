#!/usr/bin/env python3
"""Trim the white margin of circular vignette heroes (Nov 28 2026, Dr. Rivero: "why is the white circle so big").

Vignette art made to the v3 spec is a photo disc inside a WHITE border (the circle fills about 84-90% of the
2048 px square). The page already draws its own disc (`.hero-vignette`, border-radius 50%), so that white border
shows as a thick ring. This patcher measures each hero image and, when it has a white margin, adds
`class="hero-vignette vtrim" style="--vt:<scale>"` so CSS scales the picture until the photo fills the disc.
Full-bleed art (no margin) is left alone, and so is `.hero-vignette.zoom`.

Pages: guides/*.html, academy/*.html (paratus/ copies are rebuilt from academy/ by build_paratus.py).
Idempotent; re-measures on every run, so a replaced image gets the right scale.

    python3 patch_vignette_trim.py           # patch
    python3 patch_vignette_trim.py --check   # exit 1 if any page needs a change
"""
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
DIRS = ["guides", "academy"]
CSS = ('<style id="vtrim-css">.hero-vignette.vtrim img{transform:scale(var(--vt,1.14));transform-origin:50% 50%}'
       '@media print{.hero-vignette.vtrim img{transform:none}}</style>')
BLOCK = re.compile(r'<div class="hero-vignette(?: vtrim)?"(?: style="--vt:[0-9.]+")?>(.*?)</div>', re.S)
_cache = {}


def margin_scale(path):
    """Scale that makes the photo disc fill the frame, or None when the image has no white margin."""
    if path in _cache:
        return _cache[path]
    sc = None
    try:
        im = Image.open(path).convert("L")
        w, h = im.size
        im.thumbnail((512, 512))
        sw, sh = im.size
        px = im.load()

        # Walk in from the edge along 16 directions to the first pixel that is not margin white; the disc radius is
        # the median, so a bright sky or ceiling in one direction does not count as margin.
        import math
        cx, cy, half = sw / 2, sh / 2, min(sw, sh) / 2
        radii = []
        for k in range(16):
            a = k * math.pi / 8
            dx, dy = math.cos(a), math.sin(a)
            r = half - 1
            while r > half * 0.5:
                x, y = int(cx + dx * r), int(cy + dy * r)
                if 0 <= x < sw and 0 <= y < sh and px[x, y] < 248:
                    break
                r -= 1
            radii.append(r)
        radii.sort()
        r = (radii[7] + radii[8]) / 2
        m = (half - r) / (2 * half)
        if m >= 0.03:
            sc = round(min(1.35, half / r * 1.02), 3)
    except Exception:
        sc = None
    _cache[path] = sc
    return sc


def image_for(block, page):
    """The largest local file the vignette uses (webp in srcset, else img src)."""
    cands = re.findall(r'(\.\./images/[^\s",]+|/images/[^\s",]+)', block)
    best = None
    for c in cands:
        p = (page.parent / c).resolve() if c.startswith("..") else ROOT / c.lstrip("/")
        if not p.exists() or "/resp/" in str(p):
            continue
        if best is None or (p.suffix == ".webp") > (best.suffix == ".webp"):   # the full-size WebP is the fastest to read
            best = p
    return best


def patch(text, page):
    if 'class="hero-vignette' not in text:
        return text

    def sub(m):
        whole = m.group(0)
        img = image_for(m.group(1), page)
        sc = margin_scale(img) if img else None
        open_tag = f'<div class="hero-vignette vtrim" style="--vt:{sc}">' if sc else '<div class="hero-vignette">'
        return open_tag + whole[whole.index(">") + 1:]
    new = BLOCK.sub(sub, text)
    has = "vtrim" in re.sub(r'<style id="vtrim-css">.*?</style>', "", new, flags=re.S)
    new = re.sub(r'<style id="vtrim-css">.*?</style>\n?', "", new, flags=re.S)
    if has:
        new = new.replace("</head>", CSS + "\n</head>", 1)
    return new


def main():
    check = "--check" in sys.argv
    changed = 0
    for d in DIRS:
        for page in sorted((ROOT / d).glob("*.html")):
            t = page.read_text(encoding="utf-8")
            n = patch(t, page)
            if n != t:
                changed += 1
                if not check:
                    page.write_text(n, encoding="utf-8")
    print(f"vignette trim: {changed} page(s) {'need a change' if check else 'updated'}")
    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
