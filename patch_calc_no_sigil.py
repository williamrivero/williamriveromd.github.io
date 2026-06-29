#!/usr/bin/env python3
"""Mark calculator guides so they opt out of the hero sigil watermark.

The hero sigil watermark is applied site-wide via `.hero::after` / `.md-hero::after`
in the master CSS (see patch_master_css.py). Calculator pages should NOT show it,
so this script tags each calculator guide's <body> with class="calc-page". The
master CSS then suppresses the sigil for `body.calc-page` heroes.

Calculator pages are the per-tool files (guides/calc-*.html) plus the calculators
index (guides/calculators.html).

Usage:
    python3 patch_calc_no_sigil.py                 # tag all calculator guides
    python3 patch_calc_no_sigil.py --dry-run       # preview without writing
    python3 patch_calc_no_sigil.py --guide calc-kfre.html   # single guide

Idempotent: a guide whose <body> already carries calc-page is skipped. Run after
adding any new calculator guide so its hero stays sigil-free.
"""
import argparse
import re
import sys
from pathlib import Path

GUIDES_DIR = Path(__file__).resolve().parent / "guides"

# <body> with no class, or <body ...> with an existing attribute/class list.
BODY_RE = re.compile(r"<body\b([^>]*)>", re.IGNORECASE)


def is_calculator(path: Path) -> bool:
    name = path.name
    return name == "calculators.html" or name.startswith("calc-")


def add_calc_page_class(attrs: str) -> str:
    """Return the <body> attribute string with calc-page added to its class."""
    class_re = re.compile(r'(\bclass\s*=\s*)(["\'])(.*?)\2', re.IGNORECASE | re.DOTALL)
    m = class_re.search(attrs)
    if m:
        classes = m.group(3).split()
        if "calc-page" in classes:
            return attrs  # already tagged
        classes.append("calc-page")
        new_class = f'{m.group(1)}{m.group(2)}{" ".join(classes)}{m.group(2)}'
        return attrs[: m.start()] + new_class + attrs[m.end():]
    # No class attribute — add one.
    return f'{attrs} class="calc-page"'


def patch_file(path: Path, dry_run: bool) -> bool:
    html = path.read_text(encoding="utf-8")
    m = BODY_RE.search(html)
    if not m:
        print(f"  {path.name:55s} → ⚠ no <body> tag found")
        return False
    new_attrs = add_calc_page_class(m.group(1))
    if new_attrs == m.group(1):
        print(f"  {path.name:55s} → already tagged")
        return False
    new_body = f"<body{new_attrs}>"
    new_html = html[: m.start()] + new_body + html[m.end():]
    if not dry_run:
        path.write_text(new_html, encoding="utf-8")
    print(f"  {path.name:55s} → ✓ calc-page added{' (dry-run)' if dry_run else ''}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="preview changes without writing")
    ap.add_argument("--guide", help="patch a single guide file (name or path)")
    args = ap.parse_args()

    if args.guide:
        path = Path(args.guide)
        if not path.is_absolute() and not path.exists():
            path = GUIDES_DIR / Path(args.guide).name
        if not path.exists():
            print(f"Guide not found: {args.guide}", file=sys.stderr)
            return 1
        targets = [path]
    else:
        targets = sorted(p for p in GUIDES_DIR.glob("*.html") if is_calculator(p))

    patched = 0
    for path in targets:
        if not is_calculator(path):
            print(f"  {path.name:55s} → skipped (not a calculator guide)")
            continue
        if patch_file(path, args.dry_run):
            patched += 1

    print(f"\nSummary:\n  Tagged: {patched}  |  No changes: {len(targets) - patched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
