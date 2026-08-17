#!/usr/bin/env python3
"""
patch_favicon_svg.py — williamriveromd.com

Adds the SVG favicon link (<link rel="icon" type="image/svg+xml"
href="/brand/favicon.svg">) right after the existing 32x32 PNG favicon
link on every page site-wide. Browsers that support SVG favicons prefer
it over the ico/png fallbacks, giving a crisper tab icon at any pixel
density; the ico/png/apple-touch-icon links stay in place for browsers
that don't support SVG favicons — no page needs its favicon *files*
touched, since favicon.ico / favicon-16x16.png / favicon-32x32.png /
apple-touch-icon.png / android-chrome-*.png already carry the new brand
mark in place (same filenames every page references).

Idempotent: a page that already links brand/favicon.svg is skipped.
Pages with no favicon-32x32 link at all (the downloads/ companion PDFs)
are left untouched — they aren't browsed directly.

Usage:
    python3 patch_favicon_svg.py
    python3 patch_favicon_svg.py --dry-run
    python3 patch_favicon_svg.py --guide understanding-ckd.html
    python3 patch_favicon_svg.py --report
"""

import re
import argparse
from pathlib import Path

ROOT = Path(__file__).parent
FAV32_RE = re.compile(
    r'(<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32\.png">)'
)
SVG_LINK = '<link rel="icon" type="image/svg+xml" href="/brand/favicon.svg">'
ALREADY_RE = re.compile(r'brand/favicon\.svg')


def find_html_files():
    return sorted(p for p in ROOT.rglob("*.html") if "node_modules" not in p.parts)


def patch_file(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    if ALREADY_RE.search(text):
        return "already-patched"
    if not FAV32_RE.search(text):
        return "no-favicon-link"
    new_text = FAV32_RE.sub(lambda m: m.group(1) + "\n" + SVG_LINK, text, count=1)
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return "patched"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="single file, relative to repo root")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    if args.guide:
        files = [ROOT / args.guide]
    else:
        files = find_html_files()

    counts = {}
    for f in files:
        if not f.exists():
            print(f"skip (missing): {f}")
            continue
        status = patch_file(f, args.dry_run or args.report)
        counts[status] = counts.get(status, 0) + 1
        if status == "patched" and (args.dry_run or args.report or args.guide):
            print(f"{'[dry-run] ' if args.dry_run else ''}patched: {f.relative_to(ROOT)}")

    print("\nSummary:")
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
