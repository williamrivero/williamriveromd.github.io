#!/usr/bin/env python3
"""
patch_guide_rail.py — renalcarematters.com

Installs the side rail (`assets/guide-rail.js`) on every content guide:

    <script src="../assets/guide-rail.js" defer></script>

On screens >= 1024px wide the rail is a slim sticky icon strip on the right edge
that slides out References, Glossary & abbreviations, and Share in a drawer
(built from the guide's own accordions + share-buttons.js). The end-of-guide
References / Glossary / "Share this guide" blocks are then hidden on screen but
kept in the page for phones (< 1024px), print, and search engines.

The tag goes immediately AFTER the share-buttons.js tag (the rail's Share tab
uses window.rcmShare), or before the last </body> if that tag is missing.
Eligibility = the Symptom-Checker widget's rules (imported). Idempotent.

Usage:
    python3 patch_guide_rail.py
    python3 patch_guide_rail.py --dry-run
    python3 patch_guide_rail.py --report
    python3 patch_guide_rail.py --guide igan-guide.html
"""

import argparse
from pathlib import Path

from patch_symptom_widget import eligible, find_project_dir

TAG = '<script src="../assets/guide-rail.js" defer></script>'
MARK = "assets/guide-rail.js"
SHARE_TAG = '<script src="../assets/share-buttons.js" defer></script>'


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    if MARK in text:
        return "unchanged (already installed)"
    i = text.rfind(SHARE_TAG)
    if i != -1:
        j = i + len(SHARE_TAG)
        text = text[:j] + "\n" + TAG + text[j:]
    else:
        k = text.rfind("</body>")
        if k == -1:
            return "⚠ no </body> — skipped"
        text = text[:k] + TAG + "\n" + text[k:]
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ installed"


def main() -> None:
    ap = argparse.ArgumentParser(description="Install the side rail on every content guide.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--guide")
    args = ap.parse_args()
    guides_dir = find_project_dir(Path(__file__).resolve()) / "guides"
    files = [guides_dir / args.guide] if args.guide else sorted(
        p for p in guides_dir.glob("*.html") if eligible(p.name))
    if args.report:
        missing = [p.name for p in files if MARK not in p.read_text(encoding="utf-8")]
        print(f"{len(files) - len(missing)}/{len(files)} eligible guides have the side rail.")
        for n in missing:
            print(f"  missing: {n}")
        return
    counts = {}
    for p in files:
        r = patch_guide(p, args.dry_run)
        counts[r] = counts.get(r, 0) + 1
    print(("[dry-run] " if args.dry_run else "") + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
