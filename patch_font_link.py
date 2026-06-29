#!/usr/bin/env python3
"""
patch_font_link.py — williamriveromd.com

Idempotently rewrites the Google Fonts stylesheet <link> in the <head> of
every guide, calculator, and the homepage so the site loads the new theme
fonts (Inter, Manrope, Nunito Sans) and drops the old ones (Lora, DM Sans).

What it does per file
---------------------
- Finds the single <link ... href="...fonts.googleapis.com/css2...">
  stylesheet tag (the one that actually requests the font CSS). Handles both
  &amp; and & entity forms, single/double quotes, and self-closing or not.
- Replaces that whole tag with the canonical line (below). Idempotent: a file
  already on the canonical line is counted "already-ok" and not rewritten.
- A bare <link rel="preconnect" href="https://fonts.googleapis.com"> tag (no
  /css2 query) is left untouched — only the stylesheet request is rewritten.
- A file with no fonts.googleapis.com/css2 stylesheet link is reported under
  "no-fonts-link" and left unchanged (never inject blindly).

Target files
------------
- guides/*.html  (this INCLUDES calc-*.html and guides/index.html)
- index.html
- ckd-dri-calculator.html

downloads/ is never touched.

Usage
-----
    python3 patch_font_link.py
    python3 patch_font_link.py --dry-run
    python3 patch_font_link.py --guide anemia-management.html
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

# Canonical stylesheet link to enforce (ampersands as HTML entities, as in the files).
CANONICAL_LINK = (
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Manrope:wght@300;400;500;600;700;800&amp;'
    'family=Inter:wght@500;600;700;800&amp;'
    'family=Nunito+Sans:ital,wght@0,400;0,500;0,600;1,400&amp;'
    'display=swap" rel="stylesheet"/>'
)

# Matches a single <link ...> tag whose href points at the Google Fonts CSS API
# (.../css2...). The /css2 requirement excludes bare preconnect links. Quotes may
# be single or double; the tag may be self-closing or not.
FONT_LINK_RE = re.compile(
    r'<link\b[^>]*href=["\']https://fonts\.googleapis\.com/css2[^>]*>',
    re.IGNORECASE,
)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def patch_file(path: Path, dry_run: bool = False) -> tuple[str, str]:
    """Patch one file. Returns (status, detail).

    status is one of: "changed", "already-ok", "no-fonts-link".
    """
    text = path.read_text(encoding="utf-8")
    matches = FONT_LINK_RE.findall(text)

    if not matches:
        return "no-fonts-link", ""

    # Replace every matching stylesheet link with the canonical line.
    new_text = FONT_LINK_RE.sub(CANONICAL_LINK, text)

    if new_text == text:
        return "already-ok", ""

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    # Build a concise per-tag diff detail for reporting.
    detail_lines = []
    for old in matches:
        if old != CANONICAL_LINK:
            detail_lines.append(f"    - {old}")
            detail_lines.append(f"    + {CANONICAL_LINK}")
    detail = "\n".join(detail_lines)
    return "changed", detail


# Pages that use their OWN font stack (Cormorant/DM Sans/DM Mono/Lora) and are
# NOT on the themed master CSS — must keep their existing font link.
EXCLUDE = {"index.html", "guides/index.html", "guides/nephrology-atlas.html"}


def collect_files(project_dir: Path, guide: str | None) -> list[Path]:
    if guide:
        return [project_dir / "guides" / guide]

    files = sorted(project_dir.glob("guides/*.html"))
    for extra in ("index.html", "ckd-dri-calculator.html"):
        p = project_dir / extra
        if p.exists():
            files.append(p)
    return [
        f for f in files
        if f.relative_to(project_dir).as_posix() not in EXCLUDE
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing",
    )
    parser.add_argument(
        "--guide",
        metavar="FILENAME",
        help="Process one file under guides/ (e.g. anemia-management.html)",
    )
    args = parser.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    files = collect_files(project_dir, args.guide)

    changed = already_ok = 0
    no_link: list[str] = []
    prefix = "DRY " if args.dry_run else ""

    for path in files:
        if not path.exists():
            print(f"{prefix}{path.name}: MISSING (skipped)")
            continue
        rel = path.relative_to(project_dir).as_posix()
        status, detail = patch_file(path, dry_run=args.dry_run)
        if status == "changed":
            changed += 1
            print(f"{prefix}{rel}: ✓ font link rewritten")
            if args.dry_run and detail:
                print(detail)
        elif status == "already-ok":
            already_ok += 1
            print(f"{prefix}{rel}: already-ok")
        else:  # no-fonts-link
            no_link.append(rel)
            print(f"{prefix}{rel}: no fonts link (unchanged)")

    total = changed + already_ok + len(no_link)
    dry_label = "DRY RUN — " if args.dry_run else ""
    print(
        f"\n{dry_label}Summary: {changed} changed, {already_ok} already-ok, "
        f"{len(no_link)} no-fonts-link, {total} total"
    )
    if no_link:
        print("  Files with no fonts link:")
        for rel in no_link:
            print(f"      {rel}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
