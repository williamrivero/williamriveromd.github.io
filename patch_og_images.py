#!/usr/bin/env python3
"""Make every page's share (Open Graph) image small enough for Messenger and WhatsApp previews.

Messenger and WhatsApp often show no link preview when og:image is a large PNG (several of
ours were 0.5-3 MB). For each HTML page whose og:image is a local file over 300 KB, this
writes a JPEG copy to images/og/<stem>.jpg (1200 x 630 when the source is ~1.91:1, otherwise
the source aspect at <= 1200 px wide), at or under 300 KB, then points og:image and
twitter:image at it and sets og:image:width / og:image:height / og:image:type.

Idempotent: pages already pointing at images/og/*.jpg are skipped.

  python3 patch_og_images.py                      # all pages (root, guides/, downloads/)
  python3 patch_og_images.py --dry-run
  python3 patch_og_images.py --guide igan-guide.html
  python3 patch_og_images.py --image images/og-drug-index.png   # convert one image, print new path
"""
import argparse, glob, os, re, sys
from PIL import Image

SITE = "https://renalcarematters.com/"
LIMIT = 300 * 1024
OUT_DIR = "images/og"


def convert(src):
    """Return the repo-relative path of a <=300 KB JPEG made from src (creates it if needed)."""
    stem = os.path.splitext(os.path.basename(src))[0]
    dst = f"{OUT_DIR}/{stem}.jpg"
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    os.makedirs(OUT_DIR, exist_ok=True)
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    w, h = im.size
    if abs(w / h - 1200 / 630) < 0.05:
        im = im.resize((1200, 630), Image.LANCZOS)
    elif w > 1200:
        im = im.resize((1200, round(h * 1200 / w)), Image.LANCZOS)
    for q in (86, 82, 78, 74, 70, 65, 60, 55):
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(dst) <= LIMIT:
            break
    return dst


def set_meta(s, prop, val, attr="property"):
    pat = re.compile(rf'<meta {attr}="{re.escape(prop)}" content="[^"]*">')
    tag = f'<meta {attr}="{prop}" content="{val}">'
    if pat.search(s):
        return pat.sub(tag, s, count=1)
    anchor = re.search(r'<meta property="og:image" content="[^"]*">', s)
    return s[:anchor.end()] + "\n" + tag + s[anchor.end():] if anchor else s


def patch(path, dry):
    s = open(path, encoding="utf-8").read()
    m = re.search(r'<meta property="og:image" content="' + re.escape(SITE) + r'([^"?#]+)[^"]*">', s)
    if not m:
        return None
    rel = m.group(1)
    if rel.startswith(OUT_DIR + "/") or not os.path.exists(rel) or os.path.getsize(rel) <= LIMIT:
        return None
    if dry:
        return (path, rel, "(dry run)")
    new = convert(rel)
    w, h = Image.open(new).size
    url = SITE + new
    s2 = re.sub(r'(<meta property="og:image" content=")[^"]*(">)', rf"\g<1>{url}\g<2>", s, count=1)
    s2 = re.sub(r'(<meta (?:name|property)="twitter:image" content=")[^"]*(">)', rf"\g<1>{url}\g<2>", s2)
    s2 = set_meta(s2, "og:image:type", "image/jpeg")
    s2 = set_meta(s2, "og:image:height", str(h))
    s2 = set_meta(s2, "og:image:width", str(w))
    if s2 != s:
        open(path, "w", encoding="utf-8").write(s2)
    return (path, rel, f"{new} {w}x{h} {os.path.getsize(new)//1024} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    ap.add_argument("--image")
    a = ap.parse_args()
    if a.image:
        print(convert(a.image))
        return
    files = [f"guides/{a.guide}"] if a.guide else sorted(glob.glob("*.html") + glob.glob("guides/*.html") + glob.glob("downloads/*.html"))
    n = 0
    for f in files:
        r = patch(f, a.dry_run)
        if r:
            n += 1
            print(" -> ".join(r))
    print(f"{n} page(s) {'would be ' if a.dry_run else ''}updated")


if __name__ == "__main__":
    sys.exit(main())
