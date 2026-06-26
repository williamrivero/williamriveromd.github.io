#!/usr/bin/env python3
"""
patch_toggle_relocate.py — williamriveromd.com

Relocates the dark/light and mobile/desktop toggle buttons into the right margin
of the language-toggle row, so the guide header is one compact bar instead of two
stacked bars.

Per guide that has both a `.guide-lang-bar` and a `.guide-toggle-bar`:
  1. Moves the two `.toggle-btn` buttons out of `.guide-toggle-bar` into the
     `.guide-lang-bar`, wrapped in `<span class="guide-toggle-inline">` (which the
     master CSS pushes to the right with margin-left:auto).
  2. Removes the now-empty `.guide-toggle-bar`.

Idempotent: a guide already carrying `.guide-toggle-inline` is skipped. Calculator
pages (which have no language bar) are left untouched.

Usage:
    python3 patch_toggle_relocate.py
    python3 patch_toggle_relocate.py --dry-run
    python3 patch_toggle_relocate.py --guide understanding-ckd.html
"""

import re
import argparse
from pathlib import Path

SKIP = {"index.html"}
TOGGLE_BAR_RE = re.compile(
    r'\n?[ \t]*<div class="guide-toggle-bar">\s*(.*?)\s*</div>', re.S
)
LANG_CLOSE_RE = re.compile(r'(<div class="guide-lang-bar">.*?)(\n?[ \t]*</div>)', re.S)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    if '<span class="guide-toggle-inline">' in text:
        return "unchanged (already relocated)"
    if '<div class="guide-lang-bar">' not in text or '<div class="guide-toggle-bar">' not in text:
        return "skip (no lang bar + toggle bar)"

    m = TOGGLE_BAR_RE.search(text)
    if not m:
        return "skip (toggle bar not matched)"
    buttons = m.group(1).strip()
    text = text[:m.start()] + text[m.end():]  # remove the toggle bar

    inline = '\n  <span class="guide-toggle-inline">\n  ' + buttons + '\n  </span>'
    new_text, n = LANG_CLOSE_RE.subn(lambda mm: mm.group(1) + inline + mm.group(2),
                                     text, count=1)
    if not n:
        return "skip (lang bar close not found)"
    text = new_text

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ relocated toggles"


def main():
    ap = argparse.ArgumentParser(description="Relocate header toggles into the lang bar.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="patch a single guide (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    targets = ([guides_dir / args.guide] if args.guide
               else sorted(p for p in guides_dir.glob("*.html") if p.name not in SKIP))

    changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found"); continue
        if path.name in SKIP:
            continue
        status = patch_guide(path, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {changed} guide(s).")


if __name__ == "__main__":
    main()
