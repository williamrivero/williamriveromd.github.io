#!/usr/bin/env python3
"""Restore the "Desktop view" choice before first paint (CLS fix, Nov 27 2026).

Pages with the desktop/mobile toggle restored the saved choice (localStorage
'wgmr-desktop') from a script at the END of <body>, after first paint. Switching
the viewport to width=1024 then re-laid out the whole page, which Cloudflare
recorded as a layout shift of about 0.25 on calculator heroes.

This script puts a tiny synchronous restore right after the viewport <meta>,
so the page is laid out at the chosen width from the start. The old bottom
script still runs, but it then only updates the button labels.

Idempotent: the block sits between DESKTOP-PREPAINT markers and is replaced on
each run.

  python3 patch_desktop_prepaint.py            # all pages with the toggle
  python3 patch_desktop_prepaint.py --dry-run
  python3 patch_desktop_prepaint.py --check    # exit 1 if any page lacks it
  python3 patch_desktop_prepaint.py --guide calc-kfre.html
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
START, END = "<!-- DESKTOP-PREPAINT -->", "<!-- /DESKTOP-PREPAINT -->"
BLOCK = (
    START
    + "<script>try{if(localStorage.getItem('wgmr-desktop')==='1'){"
    "document.documentElement.setAttribute('data-view','desktop');"
    "var v=document.querySelector('meta[name=viewport]');"
    "if(v)v.setAttribute('content','width=1024');}}catch(e){}</script>"
    + END
)
VIEWPORT = re.compile(r"<meta\b[^>]*\bname=[\"']viewport[\"'][^>]*>", re.I)
OLD = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
SKIP_DIRS = {".git", "node_modules", "_site", "graphify-out"}


def pages(guide=None):
    if guide:
        for p in [ROOT / "guides" / guide, ROOT / guide]:
            if p.exists():
                return [p]
        sys.exit(f"not found: {guide}")
    out = []
    for p in ROOT.rglob("*.html"):
        if SKIP_DIRS & set(p.relative_to(ROOT).parts):
            continue
        out.append(p)
    return sorted(out)


def patch(text):
    if "wgmr-desktop" not in text.replace(BLOCK, ""):
        return text, "no-toggle"
    base = OLD.sub("", text)
    m = VIEWPORT.search(base)
    if not m:
        return text, "no-viewport"
    new = base[: m.end()] + "\n" + BLOCK + base[m.end():]
    return new, ("unchanged" if new == text else "patched")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    counts, missing = {}, []
    for p in pages(a.guide):
        text = p.read_text(encoding="utf-8")
        new, status = patch(text)
        counts[status] = counts.get(status, 0) + 1
        if status == "no-viewport":
            missing.append(p.relative_to(ROOT))
        if status == "patched" and not (a.dry_run or a.check):
            p.write_text(new, encoding="utf-8")
    print(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    for m in missing:
        print("  no viewport meta:", m)
    if a.check and counts.get("patched"):
        sys.exit(1)


if __name__ == "__main__":
    main()
