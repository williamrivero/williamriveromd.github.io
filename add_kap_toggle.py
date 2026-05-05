#!/usr/bin/env python3
"""
add_kap_toggle.py — williamriveromd.com
Adds the KAP (Kapampangan) language toggle button to:
  - All guide HTML files (guides/*.html)
  - index.html (homepage nav bar)

Run BEFORE translate_guides.py --all --lang kap

Usage:
    python3 add_kap_toggle.py
    python3 add_kap_toggle.py --dry-run
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
    raise FileNotFoundError(
        "Cannot find williamriveromd project root. "
        "Run this script from ~/Desktop/williamriveromd/"
    )


def add_kap_to_guide(path: Path, dry_run: bool = False) -> str:
    """
    Inserts KAP button after the CEB button in guide-toggle-bar.
    Returns status string.
    """
    html = path.read_text(encoding="utf-8")

    if "glb-kap" in html:
        return "already has KAP"

    # Pattern: find the CEB button (various quote styles / spacing)
    pattern = re.compile(
        r'(<button[^>]*id=["\']glb-ceb["\'][^>]*>[^<]*</button>)',
        re.IGNORECASE,
    )
    match = pattern.search(html)
    if not match:
        return "WARN: CEB button not found — skipped"

    kap_btn = "\n      <button id=\"glb-kap\" class=\"lang-btn\" onclick=\"setLang('kap')\">KAP</button>"
    new_html = html[:match.end()] + kap_btn + html[match.end():]

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")
    return "✓ added KAP button"


def add_kap_to_index(path: Path, dry_run: bool = False) -> str:
    """
    Inserts KAP pill button after the CEB button in the homepage nav bar.
    Returns status string.
    """
    html = path.read_text(encoding="utf-8")

    if "lb-kap" in html:
        return "already has KAP"

    # Homepage uses lb-ceb (not glb-ceb)
    pattern = re.compile(
        r'(<button[^>]*id=["\']lb-ceb["\'][^>]*>[^<]*</button>)',
        re.IGNORECASE,
    )
    match = pattern.search(html)
    if not match:
        return "WARN: lb-ceb button not found — skipped"

    kap_btn = "\n          <button id=\"lb-kap\" class=\"lang-btn\" onclick=\"setLang('kap')\">KAP</button>"
    new_html = html[:match.end()] + kap_btn + html[match.end():]

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")
    return "✓ added KAP button"


def patch_setlang_function(path: Path, dry_run: bool = False) -> str:
    """
    Checks if setLang() hard-codes language names for active button styling.
    If it references lb-en/lb-tl/lb-ceb by name, adds lb-kap.
    Most guide implementations are generic loops — no patch needed.
    Returns status string.
    """
    html = path.read_text(encoding="utf-8")

    # Check if setLang hard-codes the 3 homepage buttons
    if "lb-en" in html and "lb-tl" in html and "lb-ceb" in html and "lb-kap" not in html:
        # Likely has explicit button ID references — patch the active-state logic
        # Pattern: the line that resets all 3 buttons then sets the active one
        pattern = re.compile(
            r"(document\.getElementById\s*\(\s*['\"]lb-ceb['\"]\s*\))",
        )
        if pattern.search(html):
            # Add lb-kap alongside lb-ceb in any classList operations
            new_html = re.sub(
                r"(\[(['\"])lb-en\2\s*,\s*(['\"])lb-tl\3\s*,\s*(['\"])lb-ceb\4\])",
                r"['lb-en','lb-tl','lb-ceb','lb-kap']",
                html,
            )
            if new_html != html:
                if not dry_run:
                    path.write_text(new_html, encoding="utf-8")
                return "✓ patched setLang button array"
    return "no JS patch needed"


def main():
    parser = argparse.ArgumentParser(
        description="Add KAP toggle button to all williamriveromd.com pages"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files",
    )
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        project_dir = find_project_dir(script_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    guides_dir = project_dir / "guides"
    index_path = project_dir / "index.html"

    print(f"Project: {project_dir}")
    print(f"Dry run: {args.dry_run}\n")

    # 1. Homepage index.html
    status = add_kap_to_index(index_path, args.dry_run)
    js_status = patch_setlang_function(index_path, args.dry_run)
    print(f"index.html          → {status} | {js_status}")

    # 2. guides/index.html (guide library page)
    guides_index = guides_dir / "index.html"
    if guides_index.exists():
        status = add_kap_to_guide(guides_index, args.dry_run)
        print(f"guides/index.html   → {status}")

    # 3. All guide files
    guide_files = sorted(f for f in guides_dir.glob("*.html") if f.name != "index.html")
    added = 0
    skipped = 0
    warned = 0

    for guide in guide_files:
        status = add_kap_to_guide(guide, args.dry_run)
        if "✓" in status:
            added += 1
            print(f"  {guide.name:50s} → {status}")
        elif "already" in status:
            skipped += 1
        else:
            warned += 1
            print(f"  {guide.name:50s} → {status}")

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:")
    print(f"  KAP button added:    {added}")
    print(f"  Already had KAP:     {skipped}")
    print(f"  Warnings:            {warned}")

    if not args.dry_run and added > 0:
        print(
            "\nNext step — run the translation script to fill in Kapampangan content:\n"
            "  python3 translate_guides.py --api-key sk-ant-... --all --lang kap"
        )
    elif args.dry_run:
        print("\nRe-run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
