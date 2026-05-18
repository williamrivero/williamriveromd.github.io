#!/usr/bin/env python3
"""
patch_mode_cls.py — kill the physician-mode layout-shift (CLS) bug.

Several dual-mode guides shipped a restore-on-load snippet at the bottom
of the page:

  (function(){const s=localStorage.getItem(GMODE)||'patient';
               if(s==='physician')setMode('physician');})();

It runs AFTER first paint. For a returning visitor who had picked
clinician mode, it swaps the whole page patient -> physician post-render,
producing the Cloudflare-RUM CLS of 0.364 on
html>body.physician-mode>div.mode-physician.

The fix (same one commit 4d2bc09 applied to four guides): drop the
restore-on-load entirely so every page starts in patient mode — the
default CSS state, zero shift. setMode() still writes the choice to
localStorage, so the in-page tab toggle is unaffected.

Idempotent: a guide with no restore IIFE is left untouched, so it is
safe to re-run after adding new dual-mode guides.

Usage (run from repo root):

  python3 patch_mode_cls.py                       # patch all guides
  python3 patch_mode_cls.py --dry-run             # preview only
  python3 patch_mode_cls.py --guide el-nino-heat-dialysis.html
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
GUIDES_DIR = REPO_ROOT / "guides"

# Matches the whole restore-on-load IIFE, optionally with its own line's
# leading whitespace and trailing newline so the line is removed cleanly.
# Covers: const|var, optional ||'patient', GMODE / GMODE_KEY / 'wgmr-mode'.
RESTORE_IIFE = re.compile(
    r"[ \t]*\(function\(\)\{\s*"
    r"(?:const|var)\s+s\s*=\s*localStorage\.getItem\("
    r"(?:GMODE|GMODE_KEY|'wgmr-mode')\)"
    r"(?:\s*\|\|\s*'patient')?\s*;\s*"
    r"if\s*\(\s*s\s*===\s*'physician'\s*\)\s*setMode\(\s*'physician'\s*\)\s*;\s*"
    r"\}\)\(\)\s*;\s*\n?"
)


def patch_file(path: Path, dry_run: bool) -> str:
    html = path.read_text(encoding="utf-8")
    matches = RESTORE_IIFE.findall(html)
    if not matches:
        return "clean"

    if dry_run:
        snippets = "\n".join(f"  - {m.group(0).strip()}" for m in RESTORE_IIFE.finditer(html))
        return f"WOULD REMOVE {len(matches)} restore IIFE(s)\n{snippets}"

    path.write_text(RESTORE_IIFE.sub("", html), encoding="utf-8")
    return f"removed {len(matches)} restore IIFE(s)"


def main() -> None:
    ap = argparse.ArgumentParser(description="Remove physician-mode restore-on-load (CLS fix)")
    ap.add_argument("--dry-run", action="store_true", help="Preview without writing")
    ap.add_argument("--guide", help="Patch a single guide file (name only)")
    args = ap.parse_args()

    if args.guide:
        targets = [GUIDES_DIR / args.guide]
        if not targets[0].exists():
            sys.exit(f"ERROR: {targets[0]} not found")
    else:
        targets = sorted(GUIDES_DIR.glob("*.html"))

    counts: dict[str, int] = {}
    for path in targets:
        result = patch_file(path, args.dry_run)
        key = result.split("\n", 1)[0]
        counts[key] = counts.get(key, 0) + 1
        if result != "clean":
            print(f"{path.name}: {result}")

    print("\nSummary:")
    for key, n in sorted(counts.items()):
        print(f"  {key}: {n}")


if __name__ == "__main__":
    main()
