#!/usr/bin/env python3
"""Cap each guide's hero (LCP) image at a max display width and center it.

Hero images are the per-guide ``<img fetchpriority="high" loading="eager">``
elements. Many were displayed at ``width:100%`` of the ~860px content column,
which left square (1:1) and portrait (2:3) heroes looking magnified — a square
hero rendered ~796px tall. This script rewrites each hero's inline ``style`` to
a canonical, centered, width-capped form while preserving the aspect ratio:

    width:100%;height:auto;max-width:600px;display:block;margin:<top> auto <bot> auto;
    [border-radius:...;][box-shadow:...;]

It is idempotent (a hero already in canonical form is skipped) and it canonically
repairs the missing-semicolon merge bugs (e.g. ``height:automax-width:100%``) and
duplicate declarations seen in the hand-authored inline styles.

Banners that use ``object-fit:cover`` (deliberate fixed-height, full-bleed crops)
are left untouched — they are not magnified and capping them would shrink an
intentional design.

Usage:
    python3 patch_hero_maxwidth.py                       # patch all guides
    python3 patch_hero_maxwidth.py --dry-run             # preview only
    python3 patch_hero_maxwidth.py --guide diabetes-kidneys.html
"""
import argparse
import glob
import os
import re
import sys

MAX_WIDTH = "600px"
GUIDES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides")

# Matches a full <img ...> start tag that carries fetchpriority="high".
HERO_IMG_RE = re.compile(r'<img\b[^>]*?fetchpriority="high"[^>]*?>', re.IGNORECASE)
STYLE_RE = re.compile(r'style="([^"]*)"', re.IGNORECASE)


def parse_style(style):
    """Parse an inline style string into an ordered dict, last value winning.

    Repairs the missing-semicolon merge bug by inserting a separator whenever a
    bare ``auto`` is glued directly to the next property name (e.g.
    ``height:automax-width`` -> ``height:auto;max-width``).
    """
    repaired = re.sub(r'auto(?=[A-Za-z-])', 'auto;', style)
    props = {}
    for chunk in repaired.split(";"):
        chunk = chunk.strip()
        if not chunk or ":" not in chunk:
            continue
        key, val = chunk.split(":", 1)
        props[key.strip().lower()] = val.strip()
    return props


def vertical_margins(props):
    """Return (top, bottom) margins, preserving any author-set vertical spacing."""
    top = bot = "0"
    if "margin" in props:
        parts = props["margin"].split()
        if len(parts) == 1:
            top = bot = parts[0]
        elif len(parts) == 2:
            top = bot = parts[0]
        elif len(parts) >= 3:
            top, bot = parts[0], parts[2]
    if "margin-top" in props:
        top = props["margin-top"]
    if "margin-bottom" in props:
        bot = props["margin-bottom"]
    return top, bot


def canon_style(style):
    """Return the canonical hero style, or None if this hero should be skipped."""
    if "object-fit" in style.lower():
        return None  # deliberate fixed-height banner — leave alone
    props = parse_style(style)
    top, bot = vertical_margins(props)
    out = [
        "width:100%",
        "height:auto",
        f"max-width:{MAX_WIDTH}",
        "display:block",
        f"margin:{top} auto {bot} auto",
    ]
    if "border-radius" in props:
        out.append("border-radius:" + props["border-radius"])
    if "box-shadow" in props:
        out.append("box-shadow:" + props["box-shadow"])
    return ";".join(out) + ";"


def patch_tag(tag):
    """Return (new_tag, status) where status is 'patched', 'skipped', or 'nostyle'."""
    m = STYLE_RE.search(tag)
    if not m:
        return tag, "nostyle"
    new_style = canon_style(m.group(1))
    if new_style is None:
        return tag, "skipped"
    if new_style == m.group(1):
        return tag, "skipped"
    new_tag = tag[: m.start()] + f'style="{new_style}"' + tag[m.end():]
    return new_tag, "patched"


def process_file(path, dry_run):
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    changed = False
    statuses = []

    def repl(match):
        nonlocal changed
        new_tag, status = patch_tag(match.group(0))
        statuses.append(status)
        if status == "patched":
            changed = True
        return new_tag

    new_html = HERO_IMG_RE.sub(repl, html)
    name = os.path.basename(path)
    if not statuses:
        return "no-hero"
    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
    if changed:
        print(f"  patched  {name}")
        return "patched"
    if "skipped" in statuses:
        print(f"  skipped  {name} (banner or already capped)")
    return "skipped"


def main():
    ap = argparse.ArgumentParser(description="Cap hero images at a max width, centered.")
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--guide", help="single guide filename, e.g. diabetes-kidneys.html")
    args = ap.parse_args()

    if args.guide:
        paths = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        paths = sorted(glob.glob(os.path.join(GUIDES_DIR, "*.html")))

    patched = skipped = nohero = 0
    for path in paths:
        if not os.path.exists(path):
            print(f"  MISSING  {path}", file=sys.stderr)
            continue
        result = process_file(path, args.dry_run)
        if result == "patched":
            patched += 1
        elif result == "skipped":
            skipped += 1
        elif result == "no-hero":
            nohero += 1

    verb = "would patch" if args.dry_run else "patched"
    print(f"\n{verb} {patched} guide(s); skipped {skipped}; {nohero} with no hero image.")


if __name__ == "__main__":
    main()
