#!/usr/bin/env python3
"""
patch_nav_about.py — williamriveromd.com

Adds an "ABOUT" link (→ /about.html) to the end of the standard header-nav
(CALCULATORS · PHYSIOLOGY · ATLAS · ALL GUIDES) across every guides/*.html
page that uses it — guide pages, calculators.html, calc-*.html, and
guides/index.html itself. Idempotent: a file that already links to
/about.html from its header is left untouched.

A handful of pages predate the standard 4-item header-nav convention and
use a bespoke header instead. They are intentionally left untouched here
(hand-patched separately, since each needs a different fix):
  - kidney-physiology.html                 (icon-only mini nav)
  - calc-transfusion-hgb.html               (single "back" link, no header-nav)
  - symptom-checker.html
  - ckd-skin-darkening-body-changes.html    (bespoke inline-styled single link)
  - alcohol-drinking-log.html
  - bp-log-blank.html
  - bp-monitoring-log.html                  (printable forms — no header at all)

Usage:
    python3 patch_nav_about.py
    python3 patch_nav_about.py --dry-run
    python3 patch_nav_about.py --guide understanding-ckd.html
    python3 patch_nav_about.py --report
"""

import re
import argparse
from pathlib import Path

NAV_RE = re.compile(r'(<a href="/guides/"[^>]*>ALL GUIDES</a>)(\s*</nav>)')
ABOUT_LINK = '<a href="/about.html">ABOUT</a>'

SKIP = {
    "kidney-physiology.html",
    "calc-transfusion-hgb.html",
    "symptom-checker.html",
    "ckd-skin-darkening-body-changes.html",
    "alcohol-drinking-log.html",
    "bp-log-blank.html",
    "bp-monitoring-log.html",
}


def patch_text(text: str):
    new_text, n = NAV_RE.subn(rf'\1{ABOUT_LINK}\2', text, count=1)
    return new_text, n > 0


def main():
    ap = argparse.ArgumentParser(description="Add an ABOUT link to the standard header-nav across guides/*.html")
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--guide", help="single filename (relative to guides/) to patch")
    ap.add_argument("--report", action="store_true", help="audit coverage only, no writes")
    args = ap.parse_args()

    guides_dir = Path(__file__).resolve().parent / "guides"
    files = [guides_dir / args.guide] if args.guide else sorted(guides_dir.glob("*.html"))

    changed, already, skipped, no_match = [], [], [], []
    for path in files:
        if not path.exists():
            print(f"  (missing: {path.name})")
            continue
        if path.name in SKIP:
            skipped.append(path.name)
            continue
        text = path.read_text(encoding="utf-8")
        if 'href="/about.html"' in text:
            already.append(path.name)
            continue
        new_text, ok = patch_text(text)
        if not ok:
            no_match.append(path.name)
            continue
        changed.append(path.name)
        if not args.dry_run and not args.report:
            path.write_text(new_text, encoding="utf-8")

    verb = "Would patch" if (args.dry_run or args.report) else "Patched"
    print(f"{verb}: {len(changed)}")
    print(f"Already had ABOUT: {len(already)}")
    print(f"Skipped (bespoke header, fixed by hand): {len(skipped)}")
    if no_match:
        print(f"No standard nav match found ({len(no_match)}) — investigate:")
        for n in no_match:
            print(f"  {n}")
    if args.dry_run:
        print("\n[dry-run] no files written")
    elif args.report:
        print("\n[report] no files written")


if __name__ == "__main__":
    main()
