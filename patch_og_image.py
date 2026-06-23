#!/usr/bin/env python3
"""
patch_og_image.py — guarantee every guide ships a 1200x630 social-share (OG) card
with correct Open Graph / Twitter metadata.

For each guides/*.html the script:
  1. Resolves the best available source image (current og:image -> first in-page
     content image -> site hero fallback).
  2. Renders a dedicated 1200x630 card at images/<slug>-og.png:
       - landscape/wide sources are cover-cropped (full bleed, centered),
       - square/portrait sources are letterbox-padded on their own average colour
         so multi-panel infographics are not sliced apart.
  3. Repoints og:image + twitter:image at that card and sets/normalises
     og:image:width=1200, og:image:height=630, og:image:alt,
     twitter:image:alt and twitter:card=summary_large_image.

A guide whose og:image already resolves to an existing, exactly-1200x630 file is
left as-is (only missing width/height/alt/twitter tags are back-filled). The
script is idempotent and never touches in-page hero files (cards are separate
<slug>-og.png derivatives).

Usage:
    python3 patch_og_image.py                 # patch all guides
    python3 patch_og_image.py --dry-run       # preview without writing
    python3 patch_og_image.py --guide anemia-management.html   # single guide

Requires: pip install pillow
"""
import argparse
import glob
import os
import re
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

ROOT = os.path.dirname(os.path.abspath(__file__))
GUIDES = os.path.join(ROOT, "guides")
IMAGES = os.path.join(ROOT, "images")
BASE_URL = "https://www.williamriveromd.com"
TARGET = (1200, 630)
FALLBACK_SOURCE = os.path.join(IMAGES, "photo-hero.jpg")


# ── meta-tag helpers ────────────────────────────────────────────────────────
def find_meta(html, key, attr="property"):
    """Return (match, content) for <meta {attr}="{key}" content="...">, tolerant
    of whitespace, attribute order and self-closing slashes."""
    pat = re.compile(
        r'<meta\s+' + attr + r'=(["\'])' + re.escape(key) + r'\1\s+content=(["\'])(.*?)\2\s*/?>',
        re.IGNORECASE | re.DOTALL,
    )
    m = pat.search(html)
    return (m, m.group(3)) if m else (None, None)


def self_closing(html):
    """Whether this file's meta tags predominantly self-close (<meta .../>)."""
    metas = re.findall(r'<meta\b[^>]*?(/?)>', html)
    closed = sum(1 for s in metas if s == "/")
    return closed * 2 > len(metas)


def local_for(url):
    """Map an og:image URL / src to a local images/ path, else None."""
    if not url:
        return None
    url = url.split("?")[0]
    if "/images/" in url:
        return os.path.join(IMAGES, url.split("/images/")[-1])
    if url.startswith("images/"):
        return os.path.join(ROOT, url)
    if url.startswith("../images/"):
        return os.path.join(IMAGES, url.split("../images/")[-1])
    return None


def first_content_image(html):
    """First in-page image (img src or <source> srcset) that exists on disk and
    is not an avatar/QR/logo/icon chrome asset."""
    skip = ("avatar", "qr", "logo", "icon", "favicon", "apple-touch")
    for m in re.finditer(r'(?:src|srcset)=(["\'])(.*?)\1', html):
        raw = m.group(2).split(",")[0].strip().split(" ")[0]
        if "images/" not in raw:
            continue
        if any(s in raw.lower() for s in skip):
            continue
        p = local_for(raw)
        if p and os.path.exists(p) and p.lower().rsplit(".", 1)[-1] in ("png", "jpg", "jpeg", "webp"):
            return p
    return None


# ── image rendering ─────────────────────────────────────────────────────────
def render_card(src_path, out_path):
    """Render a 1200x630 card from src_path. Cover-crop wide sources; pad
    square/portrait sources on their own average colour."""
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        sw, sh = im.size
        ratio = sw / sh
        tw, th = TARGET
        if ratio >= 1.3:  # landscape-ish -> cover crop, centered
            scale = max(tw / sw, th / sh)
            nw, nh = round(sw * scale), round(sh * scale)
            im2 = im.resize((nw, nh), Image.LANCZOS)
            left = (nw - tw) // 2
            top = (nh - th) // 2
            card = im2.crop((left, top, left + tw, top + th))
        else:  # square/portrait -> contain + pad (preserve whole image)
            bg = im.resize((1, 1), Image.LANCZOS).getpixel((0, 0))
            scale = min(tw / sw, th / sh)
            nw, nh = max(1, round(sw * scale)), max(1, round(sh * scale))
            im2 = im.resize((nw, nh), Image.LANCZOS)
            card = Image.new("RGB", TARGET, bg)
            card.paste(im2, ((tw - nw) // 2, (th - nh) // 2))
        card.save(out_path, "PNG", optimize=True)


def is_correct(path):
    if not path or not os.path.exists(path):
        return False
    try:
        with Image.open(path) as im:
            return im.size == TARGET
    except Exception:
        return False


# ── tag rewriting ───────────────────────────────────────────────────────────
def derive_alt(html):
    for key, attr in (("og:image:alt", "property"), ("og:title", "property"),
                      ("twitter:title", "name")):
        _, val = find_meta(html, key, attr)
        if val:
            return val if "·" in val or key == "og:image:alt" else val + " · williamriveromd.com"
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r"\s*·.*$", "", m.group(1).strip()) + " · williamriveromd.com"
    return "williamriveromd.com"


def set_content(html, key, value, attr="property"):
    """Replace the content of an existing meta tag; return (html, changed, found)."""
    m, cur = find_meta(html, key, attr)
    if not m:
        return html, False, False
    if cur == value:
        return html, False, True
    full = m.group(0)
    new = re.sub(r'(content=(["\'])).*?\2', lambda mm: mm.group(1) + value + mm.group(2),
                 full, count=1, flags=re.DOTALL)
    return html[:m.start()] + new + html[m.end():], True, True


def insert_after(html, anchor_key, lines, attr="property"):
    """Insert meta lines immediately after the anchor meta tag."""
    m, _ = find_meta(html, anchor_key, attr)
    if not m:
        return html, False
    indent = re.match(r'[ \t]*', html[html.rfind("\n", 0, m.start()) + 1:m.start()]).group(0)
    block = "".join("\n" + indent + ln for ln in lines)
    return html[:m.end()] + block + html[m.end():], True


def insert_after_re(html, pattern, lines):
    """Insert meta lines after the first tag matching a raw regex (fallback
    anchor for pages that carry no Open Graph / Twitter tags at all)."""
    m = re.search(pattern, html, re.IGNORECASE)
    if not m:
        return html, False
    indent = re.match(r'[ \t]*', html[html.rfind("\n", 0, m.start()) + 1:m.start()]).group(0)
    block = "".join("\n" + indent + ln for ln in lines)
    return html[:m.end()] + block + html[m.end():], True


def patch_html(html, og_url, alt):
    sc = "/>" if self_closing(html) else ">"

    def meta(prop, content, attr="property"):
        return f'<meta {attr}="{prop}" content="{content}"{sc}'

    changed = False

    # og:image (+ width/height/alt) -------------------------------------------
    m_img, _ = find_meta(html, "og:image")
    if m_img:
        html, c, _ = set_content(html, "og:image", og_url); changed |= c
        # ensure width/height/alt exist right after og:image
        miss = []
        for k, v in (("og:image:width", "1200"), ("og:image:height", "630"),
                     ("og:image:alt", alt)):
            mk, cur = find_meta(html, k)
            if mk:
                html, c, _ = set_content(html, k, v); changed |= c
            else:
                miss.append(meta(k, v))
        if miss:
            html, c = insert_after(html, "og:image", miss); changed |= c
    else:
        block = [meta("og:image", og_url), meta("og:image:width", "1200"),
                 meta("og:image:height", "630"), meta("og:image:alt", alt)]
        placed = False
        for anchor in ("og:url", "og:description", "og:title", "og:type"):
            html, ok = insert_after(html, anchor, block)
            if ok:
                changed = placed = True
                break
        if not placed:
            # Page carries no Open Graph tags — seed a minimal set after canonical/title.
            for pat in (r'<link\s+rel=["\']canonical["\'][^>]*?/?>',
                        r'</title>', r'<meta\s+charset[^>]*?/?>'):
                html, ok = insert_after_re(html, pat, block)
                if ok:
                    changed = True
                    break

    # twitter:image (+ alt + card) --------------------------------------------
    m_tw, _ = find_meta(html, "twitter:image", "name")
    if m_tw:
        html, c, _ = set_content(html, "twitter:image", og_url, "name"); changed |= c
        if not find_meta(html, "twitter:image:alt", "name")[0]:
            html, c = insert_after(html, "twitter:image",
                                   [meta("twitter:image:alt", alt, "name")], "name"); changed |= c
        else:
            html, c, _ = set_content(html, "twitter:image:alt", alt, "name"); changed |= c
    else:
        block = [meta("twitter:card", "summary_large_image", "name"),
                 meta("twitter:image", og_url, "name"),
                 meta("twitter:image:alt", alt, "name")]
        placed = False
        for anchor in ("twitter:card", "twitter:description", "twitter:title"):
            html, ok = insert_after(html, anchor, block[1:] if anchor == "twitter:card" else block, "name")
            if ok:
                changed = placed = True
                break
        if not placed:
            # No Twitter tags at all — anchor the full block on the og:image:alt line.
            for anchor in ("og:image:alt", "og:image"):
                html, ok = insert_after(html, anchor, block)
                if ok:
                    changed = True
                    break
    # ensure twitter:card
    if not find_meta(html, "twitter:card", "name")[0]:
        html, c = insert_after(html, "twitter:image",
                               [meta("twitter:card", "summary_large_image", "name")], "name")
        changed |= c

    return html, changed


# ── driver ──────────────────────────────────────────────────────────────────
def process(path, dry):
    name = os.path.basename(path)
    slug = name[:-5]
    html = open(path, encoding="utf-8").read()

    _, og = find_meta(html, "og:image")
    cur_local = local_for(og)

    card_name = f"{slug}-og.png"
    card_path = os.path.join(IMAGES, card_name)
    card_url = f"{BASE_URL}/images/{card_name}"

    # Already a correct 1200x630 card -> keep image, just back-fill tags.
    if is_correct(cur_local):
        new_html, changed = patch_html(html, og, derive_alt(html))
        if changed and not dry:
            open(path, "w", encoding="utf-8").write(new_html)
        return ("tags" if changed else "ok", name, og)

    # Pick a source image to render the card from.
    src = cur_local if (cur_local and os.path.exists(cur_local)) else None
    if not src:
        src = first_content_image(html)
    if not src:
        src = FALLBACK_SOURCE if os.path.exists(FALLBACK_SOURCE) else None
    if not src:
        return ("NO-SOURCE", name, og)

    if not dry:
        render_card(src, card_path)
    new_html, _ = patch_html(html, card_url, derive_alt(html))
    if not dry:
        open(path, "w", encoding="utf-8").write(new_html)
    return ("built", name, f"{os.path.basename(src)} -> {card_name}")


def main():
    ap = argparse.ArgumentParser(description="Patch guides to 1200x630 OG cards.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="single guide filename, e.g. anemia-management.html")
    args = ap.parse_args()

    if args.guide:
        files = [os.path.join(GUIDES, args.guide)]
    else:
        files = sorted(glob.glob(os.path.join(GUIDES, "*.html")))

    counts = {}
    for f in files:
        status, name, detail = process(f, args.dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status not in ("ok",):
            print(f"[{status:>9}] {name}  {detail}")
    print("\nSummary:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())),
          "(dry-run)" if args.dry_run else "")


if __name__ == "__main__":
    main()
