#!/usr/bin/env python3
"""
patch_guide_rail.py — renalcarematters.com

Installs the side rail (`assets/guide-rail.js`) on every content guide:

    <script src="../assets/guide-rail.<hash>.js" defer></script>

The script is FINGERPRINTED (Nov 18 2026): edit the unhashed source assets/guide-rail.js, then run
this patcher. It writes assets/guide-rail.<sha1[:10]>.js, prunes older copies and points every page
at the new name, so Cloudflare can never serve a stale rail (it did: a 4 h edge cache kept the
pre-calculator rail live for hours). _headers caches /assets/guide-rail.* immutable. The sitemap
workflow runs this on every push.

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
import hashlib
import re
from pathlib import Path

from patch_symptom_widget import find_project_dir
from patch_share_buttons import eligible as _share_eligible


def eligible(name: str) -> bool:
    # Content guides plus every calculator (Nov 18 2026: Author / References / Share in the rail);
    # the calculators index has no references or author panel, so it stays out.
    return _share_eligible(name) and name != "calculators.html"

SRC_NAME = "guide-rail.js"
SHARE_TAG = '<script src="../assets/share-buttons.js" defer></script>'
TAG_RE = re.compile(r'<script src="\.\./assets/guide-rail(?:\.[0-9a-f]{10})?\.js" defer></script>')
MARK = "assets/guide-rail"
TAG = None  # set by fingerprint()


def fingerprint(assets: Path, dry_run: bool) -> str:
    """Write assets/guide-rail.<hash>.js from the unhashed source, prune older copies; return the tag."""
    raw = (assets / SRC_NAME).read_bytes()
    name = f"guide-rail.{hashlib.sha1(raw).hexdigest()[:10]}.js"
    if not dry_run:
        out = assets / name
        if not out.exists() or out.read_bytes() != raw:
            out.write_bytes(raw)
        for old in assets.glob("guide-rail.*.js"):
            if old.name != name and re.fullmatch(r"guide-rail\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return f'<script src="../assets/{name}" defer></script>'


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    found = TAG_RE.findall(text)
    if found:
        if found == [TAG]:
            return "unchanged (current)"
        seen = []  # keep the first tag (now current), drop any duplicates
        new = TAG_RE.sub(lambda m: "" if seen else (seen.append(1) or TAG), text)
        if not dry_run:
            path.write_text(new, encoding="utf-8")
        return "✓ updated to current fingerprint"
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
    root = find_project_dir(Path(__file__).resolve())
    guides_dir = root / "guides"
    global TAG
    TAG = fingerprint(root / "assets", args.dry_run or args.report)
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
