#!/usr/bin/env python3
"""
fix_setlang_kap.py — williamriveromd.com
Patches the setLang() JavaScript function in all guide pages and index.html
to include 'kap' in the language loop array, preventing KAP toggle from
blanking out page content.

Problems fixed:
  1. ['en','tl','ceb'] forEach loop -> ['en','tl','ceb','kap']
  2. lang === 'tl' ? ... : 'en' ternary -> adds kap branch
  3. ['lb-en','lb-tl','lb-ceb'] homepage button array -> adds 'lb-kap'

Usage:
    python3 fix_setlang_kap.py
    python3 fix_setlang_kap.py --dry-run
"""

import re
import sys
import argparse
from pathlib import Path


def find_project_dir(script_path):
    candidates = [
        script_path.parent,
        script_path.parent.parent,
        Path.home() / "Desktop" / "williamriveromd",
    ]
    for c in candidates:
        if (c / "guides").is_dir() and (c / "index.html").exists():
            return c
    raise FileNotFoundError("Cannot find williamriveromd project root.")


def patch_file(path, dry_run=False):
    html = path.read_text(encoding="utf-8")
    changes = []

    # Patch 1: forEach lang array
    p1_patterns = [
        (r"\['en'\s*,\s*'tl'\s*,\s*'ceb'\]", "['en','tl','ceb','kap']"),
        (r'\["en"\s*,\s*"tl"\s*,\s*"ceb"\]', '["en","tl","ceb","kap"]'),
    ]
    for pattern, replacement in p1_patterns:
        match = re.search(pattern, html)
        if match and 'kap' not in match.group():
            html = re.sub(pattern, replacement, html)
            changes.append("lang forEach array")
            break

    # Patch 2: lang attribute ternary
    p2_old = r"lang\s*===\s*'tl'\s*\?\s*'tl'\s*:\s*lang\s*===\s*'ceb'\s*\?\s*'ceb'\s*:\s*'en'"
    p2_new = "lang === 'tl' ? 'tl' : lang === 'ceb' ? 'ceb' : lang === 'kap' ? 'kap' : 'en'"
    if re.search(p2_old, html) and "lang === 'kap'" not in html:
        html = re.sub(p2_old, p2_new, html)
        changes.append("lang ternary")

    # Patch 3: homepage lb- button array
    p3_old = r"\['lb-en'\s*,\s*'lb-tl'\s*,\s*'lb-ceb'\]"
    p3_new = "['lb-en','lb-tl','lb-ceb','lb-kap']"
    if re.search(p3_old, html) and 'lb-kap' not in html:
        html = re.sub(p3_old, p3_new, html)
        changes.append("lb- button array")

    if not changes:
        return "no changes"

    if not dry_run:
        path.write_text(html, encoding="utf-8")

    prefix = "[DRY] " if dry_run else ""
    return prefix + "OK: " + " + ".join(changes)


def main():
    parser = argparse.ArgumentParser(
        description="Patch setLang() to include KAP in all pages"
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--guide", help="Patch a single guide file only")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        project_dir = find_project_dir(script_path)
    except FileNotFoundError as e:
        print("ERROR: " + str(e))
        sys.exit(1)

    guides_dir = project_dir / "guides"
    index_path = project_dir / "index.html"

    print("Project: " + str(project_dir))
    print("Dry run: " + str(args.dry_run) + "\n")

    if args.guide:
        path = guides_dir / args.guide
        if not path.exists():
            print("ERROR: " + str(path) + " not found")
            sys.exit(1)
        result = patch_file(path, args.dry_run)
        print(args.guide + ": " + result)
        return

    patched = 0
    skipped = 0

    if index_path.exists():
        result = patch_file(index_path, args.dry_run)
        if "no changes" not in result:
            patched += 1
            print("  index.html" + " " * 50 + " -> " + result)
        else:
            skipped += 1

    for f in sorted(guides_dir.glob("*.html")):
        result = patch_file(f, args.dry_run)
        if "no changes" not in result:
            patched += 1
            print("  " + f.name.ljust(55) + " -> " + result)
        else:
            skipped += 1

    print("")
    if args.dry_run:
        print("[DRY RUN] Summary:")
    else:
        print("Summary:")
    print("  Patched: " + str(patched) + "  |  Already correct: " + str(skipped))

    if not args.dry_run and patched > 0:
        print("\nNext step:")
        print("  git add .")
        print('  git commit -m "Fix setLang() KAP support across all guides"')
        print("  git push")
    elif args.dry_run:
        print("\nRe-run without --dry-run to apply.")


if __name__ == "__main__":
    main()
