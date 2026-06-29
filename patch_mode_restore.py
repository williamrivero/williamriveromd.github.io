#!/usr/bin/env python3
"""
patch_mode_restore.py — restore physician mode on refresh, without CLS.

History: dual-mode guides originally restored clinician mode with a
bottom-of-page IIFE that ran AFTER first paint, swapping the whole page
patient -> physician post-render (Cloudflare-RUM CLS 0.364).
patch_mode_cls.py stripped those restorers, which fixed the layout shift
but made every refresh fall back to the Patients tab.

This script restores persistence the safe way: a tiny synchronous inline
script injected immediately after the opening <body> tag. It applies the
physician-mode class BEFORE the browser paints anything, so the first
paint is already the clinician view — zero layout shift. Tab button
active-state syncing (a color-only change) is deferred to
DOMContentLoaded.

Each guide stores its mode under its own localStorage key (e.g.
'wgmr-mode', 'wgmr-igan-mode'); the key is extracted from the guide's own
setMode() source and inlined literally.

Idempotent: guides already carrying the pre-paint restorer are skipped.
Run after adding any new dual-mode guide (after patch_mode_cls.py).

Usage (run from repo root):

  python3 patch_mode_restore.py                  # patch all dual-mode guides
  python3 patch_mode_restore.py --dry-run        # preview only
  python3 patch_mode_restore.py --guide igan-guide.html
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
GUIDES_DIR = REPO_ROOT / "guides"

MARKER = "pre-paint physician-mode restore"

SNIPPET = (
    "\n<script>/* {marker} — class applied before first paint, zero CLS.\n"
    "   Do NOT move this to the bottom of the page or convert it into a\n"
    "   post-paint restore — that reintroduces the CLS bug patch_mode_cls.py\n"
    "   exists to kill. See CLAUDE.md. */\n"
    "try{{if(localStorage.getItem('{key}')==='physician'){{"
    "document.body.classList.add('physician-mode');"
    "document.addEventListener('DOMContentLoaded',function(){{"
    "var p=document.getElementById('tab-pt'),m=document.getElementById('tab-md');"
    "if(p)p.classList.remove('active');if(m)m.classList.add('active');}});}}}}"
    "catch(e){{}}</script>\n"
)

BODY_TAG = re.compile(r"<body[^>]*>")


def find_mode_key(html):
    """Extract the guide's mode localStorage key from its own JS."""
    m = re.search(r"GMODE(?:_KEY)?\s*=\s*'([^']+)'", html)
    if m:
        return m.group(1)
    m = re.search(r"localStorage\.setItem\(\s*'([^']+)'\s*,\s*(?:mode|m)\s*\)", html)
    if m:
        return m.group(1)
    return None


def patch_guide(path, dry_run=False):
    html = path.read_text(encoding="utf-8")

    if 'id="tab-md"' not in html:
        return "not dual-mode"
    if MARKER in html:
        return "already patched"

    key = find_mode_key(html)
    if not key:
        return "SKIP: mode key not found"

    m = BODY_TAG.search(html)
    if not m:
        return "SKIP: no <body> tag"

    snippet = SNIPPET.format(marker=MARKER, key=key)
    html = html[: m.end()] + snippet + html[m.end():]

    if not dry_run:
        path.write_text(html, encoding="utf-8")
    return f"patched (key: {key})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    args = ap.parse_args()

    files = (
        [GUIDES_DIR / args.guide]
        if args.guide
        else sorted(GUIDES_DIR.glob("*.html"))
    )
    counts = {}
    for f in files:
        if f.name == "index.html":
            continue
        if not f.exists():
            sys.exit(f"error: {f} not found")
        result = patch_guide(f, args.dry_run)
        counts[result.split(" (")[0]] = counts.get(result.split(" (")[0], 0) + 1
        if "not dual-mode" not in result:
            print(f"  {f.name}: {result}")
    print("\nSummary:", ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    if args.dry_run:
        print("(dry run — nothing written)")


if __name__ == "__main__":
    main()
