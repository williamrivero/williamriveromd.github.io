#!/usr/bin/env python3
"""
patch_nav_academy.py — renalcarematters.com

Adds an "ACADEMY" link (-> /academy/, the Renal Care Academy staff-training section) right after DRUGS in the
standard header-nav across guides/*.html, plus drugs/index.html and about.html when they use the same nav.
Idempotent. Pages with bespoke headers (see patch_nav_drugs.py) are left untouched.

    python3 patch_nav_academy.py [--dry-run] [--report] [--guide name.html]
"""
import argparse, re
from pathlib import Path

NAV_RE = re.compile(r'(<nav class="header-nav"[^>]*>(?:(?!</nav>).)*?<a href="/drugs/"[^>]*>DRUGS</a>)', re.S)
LINK = '<a href="/academy/">ACADEMY</a>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--guide")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    files = [root / "guides" / args.guide] if args.guide else sorted((root / "guides").glob("*.html")) + [root / "drugs" / "index.html", root / "about.html"]
    changed, already, no_match = [], [], []
    for p in files:
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        if re.search(r'<nav class="header-nav"[^>]*>(?:(?!</nav>).)*href="/academy/"', t, re.S):
            already.append(p.name); continue
        new, n = NAV_RE.subn(lambda m: m.group(1) + LINK, t, count=1)
        if not n:
            no_match.append(p.name); continue
        changed.append(p.name)
        if not (args.dry_run or args.report):
            p.write_text(new, encoding="utf-8")
    print(f"{'Would patch' if (args.dry_run or args.report) else 'Patched'}: {len(changed)}; already had ACADEMY: {len(already)}; no standard nav: {len(no_match)}")
    if args.report and no_match:
        print("  no standard nav:", ", ".join(no_match[:40]))


if __name__ == "__main__":
    main()
