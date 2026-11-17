#!/usr/bin/env python3
"""Serve phone-sized copies of guide figures (responsive images).

Lighthouse (Nov 17 2026) showed guide figures shipping at 1024-1536 px (150-190 KB each) to phones that
display them at about 400 px. For every <picture> in a guide whose WebP <source> is a single local file
wider than 900 px, this writes an 800 px copy to images/resp/<name>-800.webp (once; skipped if newer than
the original) and rewrites the source to

    <source srcset="../images/resp/<name>-800.webp 800w, ../images/<name>.webp <W>w" sizes="..." type="image/webp">

so phones download the small copy and desktops keep the full one. The <img> fallback, its src (used by the
lightbox's "open full image") and its width/height are untouched. Idempotent.

  python3 patch_responsive_images.py                 # all guides
  python3 patch_responsive_images.py --dry-run
  python3 patch_responsive_images.py --guide igan-guide.html
"""
import argparse, glob, os, re, sys
from PIL import Image

OUT = "images/resp"
SRC_RE = re.compile(r'<source(\s+)srcset="\.\./images/([^" ,]+\.webp)"(\s+)type="image/webp"\s*/?>')
_size_cache = {}


def width_of(path):
    if path not in _size_cache:
        try:
            _size_cache[path] = Image.open(path).size[0]
        except Exception:
            _size_cache[path] = 0
    return _size_cache[path]


def small_copy(name):
    src = f"images/{name}"
    dst = f"{OUT}/{os.path.splitext(name)[0]}-800.webp"
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im = Image.open(src)
    im = im.convert("RGBA") if im.mode in ("RGBA", "LA", "P") else im.convert("RGB")
    im = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=78, method=6)
    return dst


def patch(path, dry):
    s = open(path, encoding="utf-8").read()
    changed = 0

    def sub(m):
        nonlocal changed
        name = m.group(2)
        full = f"images/{name}"
        w = width_of(full)
        if w <= 900:
            return m.group(0)
        # the figure's display width: heroes are capped at 600 px, content figures fill the ~860 px column
        tail = s[m.end(): m.end() + 900]
        capped = re.search(r"max-width:\s*600px", tail.split("</picture>")[0]) is not None
        sizes = "(max-width: 640px) 100vw, 600px" if capped else "(max-width: 900px) 100vw, 860px"
        if not dry:
            small_copy(name)
        changed += 1
        return (f'<source{m.group(1)}srcset="../{OUT}/{os.path.splitext(name)[0]}-800.webp 800w, '
                f'../images/{name} {w}w" sizes="{sizes}"{m.group(3)}type="image/webp">')

    t = SRC_RE.sub(sub, s)
    if changed and not dry:
        open(path, "w", encoding="utf-8").write(t)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    files = [f"guides/{a.guide}"] if a.guide else sorted(glob.glob("guides/*.html"))
    pages = figs = 0
    for f in files:
        n = patch(f, a.dry_run)
        if n:
            pages += 1
            figs += n
    print(f"{figs} figure(s) on {pages} page(s) {'would be ' if a.dry_run else ''}made responsive")


if __name__ == "__main__":
    sys.exit(main())
