#!/usr/bin/env python3
"""
patch_kdigo2026.py — williamriveromd.com
Applies two sets of updates across all guide HTML files:

1. KDIGO 2026 Anemia Terminology
   - "Absolute Iron Deficiency" → "Systemic Iron Deficiency"
   - "absolute iron deficiency" → "systemic iron deficiency"
   - "Functional Iron Deficiency" → "Iron-Restricted Erythropoiesis"
   - "functional iron deficiency" → "iron-restricted erythropoiesis"
   - "functional deficiency" → "iron-restricted erythropoiesis"
   - KDIGO 2024 badge in anemia calculator → KDIGO 2026
   - "assess for functional deficiency" → "assess for iron-restricted erythropoiesis"

2. Brand name corrections (Philippines)
   - epoetin alfa → Eposino (brand)
   - epoetin beta → Recormon (brand)
   - "iron sucrose (Ferrofer / Anema)" → "iron sucrose (Ferrofer)"
   - "iron sucrose (Ferrofer/Anema)" → "iron sucrose (Ferrofer)"
   - "Ferrofer / Anema" → "Ferrofer"
   - "Ferrofer/Anema" → "Ferrofer"
   - "Anema" standalone brand context → removed
   - epoetin / erythropoietin brand fixes

Usage:
    python3 patch_kdigo2026.py
    python3 patch_kdigo2026.py --dry-run
    python3 patch_kdigo2026.py --guide anemia-management.html
"""

import re
import sys
import argparse
from pathlib import Path


def find_project_dir(script_path: Path) -> Path:
    candidates = [
        script_path.parent,
        script_path.parent.parent,
        Path.home() / "Desktop" / "williamriveromd",
    ]
    for c in candidates:
        if (c / "guides").is_dir() and (c / "index.html").exists():
            return c
    raise FileNotFoundError("Cannot find williamriveromd project root.")


# ── Replacement rules ──────────────────────────────────────────────────────────
# Each tuple: (pattern, replacement, flags, description)
# Ordered from most specific to least specific to avoid partial replacements

REPLACEMENTS = [

    # ── KDIGO 2026 Terminology ──────────────────────────────────────────────

    # Calculator badge: KDIGO 2024 → KDIGO 2026 (only in anemia context)
    (
        r"'KDIGO 2024'",
        "'KDIGO 2026'",
        0,
        "Calculator badge: KDIGO 2024 → KDIGO 2026"
    ),
    (
        r'"KDIGO 2024"',
        '"KDIGO 2026"',
        0,
        "Calculator badge double-quote variant"
    ),

    # Exact capitalized term (title case in headings/labels)
    (
        r"Absolute Iron Deficiency",
        "Systemic Iron Deficiency",
        0,
        "Title case: Absolute → Systemic Iron Deficiency"
    ),
    (
        r"Functional Iron Deficiency",
        "Iron-Restricted Erythropoiesis",
        0,
        "Title case: Functional → Iron-Restricted Erythropoiesis"
    ),

    # Lowercase body text
    (
        r"absolute iron deficiency",
        "systemic iron deficiency",
        re.IGNORECASE,
        "Lowercase: absolute iron deficiency → systemic iron deficiency"
    ),
    (
        r"functional iron deficiency",
        "iron-restricted erythropoiesis",
        re.IGNORECASE,
        "Lowercase: functional iron deficiency → iron-restricted erythropoiesis"
    ),

    # Partial phrases in calculator verdict/action text
    (
        r"assess for functional deficiency before supplementing",
        "assess for iron-restricted erythropoiesis before supplementing",
        0,
        "Calculator verdict: functional deficiency phrase"
    ),
    (
        r"consider functional iron deficiency from inflammation",
        "consider iron-restricted erythropoiesis from inflammation (hepcidin-mediated)",
        0,
        "Calculator action: functional deficiency from inflammation"
    ),
    (
        r"the functional deficiency is confirmed",
        "iron-restricted erythropoiesis is confirmed",
        0,
        "Calculator action: functional deficiency confirmed"
    ),
    (
        r"Oral iron is not effective for functional deficiency",
        "Oral iron is not effective for iron-restricted erythropoiesis",
        0,
        "Calculator action: oral iron not effective"
    ),
    (
        r"TSAT will fall and functional deficiency will develop",
        "TSAT will fall and iron-restricted erythropoiesis will develop",
        0,
        "Calculator verdict: depleting stores"
    ),

    # ── Brand Name Corrections ──────────────────────────────────────────────

    # Iron sucrose brand — remove Anema, keep Ferrofer only
    (
        r"iron sucrose \(Ferrofer\s*/\s*Anema\)",
        "iron sucrose (Ferrofer)",
        re.IGNORECASE,
        "Iron sucrose: remove Anema, keep Ferrofer"
    ),
    (
        r"IV iron sucrose \(Ferrofer\s*/\s*Anema\)",
        "IV iron sucrose (Ferrofer)",
        re.IGNORECASE,
        "IV iron sucrose brand fix"
    ),
    (
        r"Ferrofer\s*/\s*Anema",
        "Ferrofer",
        re.IGNORECASE,
        "Ferrofer/Anema → Ferrofer standalone"
    ),

    # Epoetin alfa → Eposino
    (
        r"epoetin alfa\s*\([^)]*\)",
        "epoetin alfa (Eposino)",
        re.IGNORECASE,
        "Epoetin alfa: replace any existing brand with Eposino"
    ),
    (
        r"epoetin\s*alfa(?!\s*\()",
        "epoetin alfa (Eposino)",
        re.IGNORECASE,
        "Epoetin alfa without brand: add Eposino"
    ),

    # Epoetin beta → Recormon
    (
        r"epoetin beta\s*\([^)]*\)",
        "epoetin beta (Recormon)",
        re.IGNORECASE,
        "Epoetin beta: replace any existing brand with Recormon"
    ),
    (
        r"epoetin\s*beta(?!\s*\()",
        "epoetin beta (Recormon)",
        re.IGNORECASE,
        "Epoetin beta without brand: add Recormon"
    ),

    # Eprex and other alfa brands → Eposino
    (
        r"\(Eprex\)",
        "(Eposino)",
        re.IGNORECASE,
        "Eprex → Eposino"
    ),
    (
        r"Eprex(?!\w)",
        "Eposino",
        re.IGNORECASE,
        "Eprex standalone → Eposino"
    ),

    # NeoRecormon → Recormon
    (
        r"NeoRecormon",
        "Recormon",
        re.IGNORECASE,
        "NeoRecormon → Recormon"
    ),
]


def apply_patches(html: str, filename: str, verbose: bool = False) -> tuple[str, list[str]]:
    """Apply all replacement rules to html. Returns (new_html, list_of_changes)."""
    changes = []
    for pattern, replacement, flags, description in REPLACEMENTS:
        if flags:
            new_html = re.sub(pattern, replacement, html, flags=flags)
        else:
            new_html = re.sub(pattern, replacement, html)
        if new_html != html:
            count = len(re.findall(pattern, html, flags=flags if flags else 0))
            changes.append(f"  [{count}x] {description}")
            html = new_html
    return html, changes


def patch_file(path: Path, dry_run: bool = False, verbose: bool = False) -> str:
    html = path.read_text(encoding="utf-8")
    new_html, changes = apply_patches(html, path.name, verbose)

    if not changes:
        return "no changes needed"

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")

    summary = f"{'[DRY] ' if dry_run else ''}✓ {len(changes)} change(s)"
    if verbose:
        summary += "\n" + "\n".join(changes)
    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Patch KDIGO 2026 terminology and brand names across all guides"
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--guide", help="Patch a single guide file only")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show each change")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        project_dir = find_project_dir(script_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    guides_dir = project_dir / "guides"
    print(f"Project: {project_dir}")
    print(f"Dry run: {args.dry_run}\n")

    if args.guide:
        path = guides_dir / args.guide
        if not path.exists():
            print(f"ERROR: {path} not found")
            sys.exit(1)
        result = patch_file(path, args.dry_run, verbose=True)
        print(f"{args.guide}: {result}")
        return

    # Patch all guides
    files = sorted(f for f in guides_dir.glob("*.html"))
    changed = 0
    skipped = 0

    for f in files:
        result = patch_file(f, args.dry_run, args.verbose)
        if "no changes" in result:
            skipped += 1
        else:
            changed += 1
            print(f"  {f.name:55s} → {result}")

    # Also patch index.html
    index = project_dir / "index.html"
    if index.exists():
        result = patch_file(index, args.dry_run, args.verbose)
        if "no changes" not in result:
            changed += 1
            print(f"  index.html{' ':45s} → {result}")

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:")
    print(f"  Files updated:      {changed}")
    print(f"  No changes needed:  {skipped}")

    if not args.dry_run and changed > 0:
        print("\nNext step — push to live:")
        print("  git add .")
        print('  git commit -m "Apply KDIGO 2026 anemia terminology + brand name corrections"')
        print("  git push")
    elif args.dry_run:
        print("\nRe-run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
