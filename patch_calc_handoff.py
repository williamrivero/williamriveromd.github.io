#!/usr/bin/env python3
"""
patch_calc_handoff.py — williamriveromd.com

Installs the shared combined-calculator input handoff (assets/calc-handoff.js)
on every calculator page, so the common patient inputs (age, sex, weight, height,
serum creatinine, eGFR) carry across the whole calculator library — enter them
once and every related calculator is prefilled.

Per calculator page it:
  1. Removes any legacy per-page <!-- RX-HANDOFF-START -->…<!-- RX-HANDOFF-END -->
     block (superseded by the shared, self-activating asset).
  2. Inserts <script src="../assets/calc-handoff.js" defer></script> before the
     last </body> (so print-popup '</body>' strings are untouched).

Idempotent. Targets guides/calc-*.html and guides/ckd-dri-calculator.html.

Usage:
    python3 patch_calc_handoff.py
    python3 patch_calc_handoff.py --dry-run
    python3 patch_calc_handoff.py --guide calc-cockcroft-gault.html
"""

import re
import argparse
from pathlib import Path

TAG = '<script src="../assets/calc-handoff.js" defer></script>'
MARK = 'assets/calc-handoff.js'
LEGACY_RE = re.compile(r'\n?<!-- RX-HANDOFF-START -->.*?<!-- RX-HANDOFF-END -->', re.S)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def is_calculator(name: str) -> bool:
    return name.startswith("calc-") or name == "ckd-dri-calculator.html"


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    if LEGACY_RE.search(text):
        text = LEGACY_RE.sub("", text)
        changes.append("removed legacy RX-HANDOFF")

    if MARK not in text:
        idx = text.rfind("</body>")
        if idx == -1:
            return "skip (no </body>)"
        text = text[:idx] + TAG + "\n" + text[idx:]
        changes.append("installed calc-handoff")

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ " + ", ".join(changes)


def main():
    ap = argparse.ArgumentParser(description="Install the shared calculator input handoff.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="patch a single calculator (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    targets = ([guides_dir / args.guide] if args.guide
               else sorted(p for p in guides_dir.glob("*.html") if is_calculator(p.name)))

    changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found"); continue
        if not is_calculator(path.name):
            continue
        status = patch_guide(path, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {changed} calculator(s).")


if __name__ == "__main__":
    main()
