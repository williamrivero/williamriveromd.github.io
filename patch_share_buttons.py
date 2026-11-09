#!/usr/bin/env python3
"""
patch_share_buttons.py — renalcarematters.com

Installs the journal-style share bar (`assets/share-buttons.js`) on every
content guide. Guides load it with a single deferred <script> tag placed just
before the final </body>:

    <script src="../assets/share-buttons.js" defer></script>

The script renders, at load time:
  - a compact icon row (Facebook, X, LinkedIn, Bluesky, WhatsApp, Viber on
    phones, Email, Copy link, plus the phone's own share sheet) under the hero
    byline (.hero-meta), and
  - a labeled "Share this guide" panel where the guide content ends (before the
    glossary, else the references accordion, else the signature card).

All markup and styles come from the JS (scoped .rcm-share classes), so nothing
is written into the guide body and patch_master_css.py never clobbers it.

Eligibility is the same as the floating Symptom-Checker widget (narrative
guides only — no index, calculators, interpreter/atlas tools, or printable
logs); the rule set is imported from patch_symptom_widget.py so the two stay
in lockstep.

Idempotent: a guide that already loads the script is skipped. Inserts before
the **last** </body> so JS print-popup strings ('</body></html>') are never
touched.

Usage:
    python3 patch_share_buttons.py
    python3 patch_share_buttons.py --dry-run
    python3 patch_share_buttons.py --report          # list coverage, no writes
    python3 patch_share_buttons.py --guide igan-guide.html
"""

import argparse
from pathlib import Path

from patch_symptom_widget import eligible, find_project_dir

TAG = '<script src="../assets/share-buttons.js" defer></script>'
MARK = "assets/share-buttons.js"


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    if MARK in text:
        return "unchanged (already installed)"
    idx = text.rfind("</body>")
    if idx == -1:
        return "⚠ no </body> — skipped"
    text = text[:idx] + TAG + "\n" + text[idx:]
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ installed"


def main() -> None:
    ap = argparse.ArgumentParser(description="Install the share bar on every content guide.")
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--report", action="store_true", help="list guides missing the share bar")
    ap.add_argument("--guide", help="patch a single guide (filename in guides/)")
    args = ap.parse_args()

    guides_dir = find_project_dir(Path(__file__).resolve()) / "guides"
    if args.guide:
        files = [guides_dir / args.guide]
    else:
        files = sorted(p for p in guides_dir.glob("*.html") if eligible(p.name))

    if args.report:
        missing = [p.name for p in files if MARK not in p.read_text(encoding="utf-8")]
        print(f"{len(files) - len(missing)}/{len(files)} eligible guides have the share bar.")
        for name in missing:
            print(f"  missing: {name}")
        return

    counts = {}
    for p in files:
        result = patch_guide(p, args.dry_run)
        counts[result] = counts.get(result, 0) + 1
        if result != "unchanged (already installed)":
            print(f"{p.name}: {result}")
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    print(("[dry-run] " if args.dry_run else "") + summary)


if __name__ == "__main__":
    main()
