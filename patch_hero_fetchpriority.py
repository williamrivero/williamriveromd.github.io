#!/usr/bin/env python3
"""
patch_hero_fetchpriority.py — make every guide's hero (LCP) image load fast.

The first content <img> in each guide is the Largest Contentful Paint
element. Shipping it with loading="lazy" delays LCP (observed: one guide
at 3.4 s on Philippine mobile). This script rewrites that first <img> so
the browser fetches it immediately:

  - adds  fetchpriority="high"
  - sets  loading="eager"   (replacing loading="lazy" if present)

It is idempotent: a guide whose hero already has fetchpriority is skipped,
so it is safe to re-run after adding new guides.

Usage (run from repo root):

  python3 patch_hero_fetchpriority.py                       # patch all guides
  python3 patch_hero_fetchpriority.py --dry-run             # preview only
  python3 patch_hero_fetchpriority.py --guide understanding-ckd.html
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
GUIDES_DIR = REPO_ROOT / "guides"

IMG_TAG = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
LOADING_ATTR = re.compile(r'\s+loading\s*=\s*(["\']?)(lazy|eager)\1', re.IGNORECASE)


def patch_tag(tag: str) -> str | None:
    """Return the rewritten <img> tag, or None if no change is needed."""
    if re.search(r"\bfetchpriority\s*=", tag, re.IGNORECASE):
        return None
    tag = LOADING_ATTR.sub("", tag)
    return re.sub(
        r"<img\b",
        '<img fetchpriority="high" loading="eager"',
        tag,
        count=1,
        flags=re.IGNORECASE,
    )


def patch_file(path: Path, dry_run: bool) -> str:
    html = path.read_text(encoding="utf-8")
    m = IMG_TAG.search(html)
    if not m:
        return "no <img> found"

    original = m.group(0)
    patched = patch_tag(original)
    if patched is None:
        return "already patched"

    if dry_run:
        return f"WOULD PATCH\n  - {original}\n  + {patched}"

    path.write_text(html[: m.start()] + patched + html[m.end() :], encoding="utf-8")
    return "patched"


def main() -> None:
    ap = argparse.ArgumentParser(description="High-priority hero image loading for guides")
    ap.add_argument("--dry-run", action="store_true", help="Preview without writing")
    ap.add_argument("--guide", help="Patch a single guide file (name only)")
    args = ap.parse_args()

    if args.guide:
        targets = [GUIDES_DIR / args.guide]
        if not targets[0].exists():
            sys.exit(f"ERROR: {targets[0]} not found")
    else:
        targets = sorted(GUIDES_DIR.glob("*.html"))

    counts: dict[str, int] = {}
    for path in targets:
        result = patch_file(path, args.dry_run)
        key = result.split("\n", 1)[0]
        counts[key] = counts.get(key, 0) + 1
        if result != "already patched":
            print(f"{path.name}: {result}")

    print("\nSummary:")
    for key, n in sorted(counts.items()):
        print(f"  {key}: {n}")


if __name__ == "__main__":
    main()
