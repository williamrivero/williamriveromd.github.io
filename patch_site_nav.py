#!/usr/bin/env python3
"""
patch_site_nav.py: the site navigation bar, site-wide (Nov 26 2026, Dr. Rivero).

1. Link ORDER in every <nav class="header-nav">, following the menu groups (Dr. Rivero, Nov 28 2026:
   HOME · LEARN · BROADEN · REVIEW · CONNECT):
       (HOME brand) · ACADEMY · PHYSIOLOGY · ATLAS · GUIDES · DRUGS · CALCULATORS · ABOUT
   Each page keeps its own href spelling and its is-current marker; a missing standard link
   is added (root-relative href). Unknown links are kept, after the standard ones.
2. Phone menu: writes assets/site-nav.<hash>.js from the source assets/site-nav.js (prunes old
   copies) and puts ONE synchronous tag right after </nav> inside the header:
       <script src="/assets/site-nav.<hash>.js"></script>
   On screens up to 640 px wide the script swaps the row for a Menu button (top left) with a
   grouped dropdown; wider screens keep the row. Synchronous on purpose: it runs before the
   header paints, so there is no layout shift. If it fails to load, the row stays.

Covers *.html in the repo root, guides/, academy/ and drugs/ (incl. supplements/, category/).
generate_drug_pages.py imports NAV_ORDER / script_tag() from here, so regenerated drug pages
match. The sitemap workflow runs this on every push. Idempotent.

Usage:
    python3 patch_site_nav.py             # write
    python3 patch_site_nav.py --dry-run   # count changes only
    python3 patch_site_nav.py --check     # exit 1 if any page is out of date (no writes)
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "assets" / "site-nav.js"

# key, label, default href (used only when a page lacks that link)
NAV_ORDER = [
    ("academy", "ACADEMY", "/academy/"),
    ("physiology", "PHYSIOLOGY", "/guides/kidney-physiology.html"),
    ("atlas", "ATLAS", "/guides/nephrology-atlas.html"),
    ("guides", "GUIDES", "/guides/"),
    ("drugs", "DRUGS", "/drugs/"),
    ("calculators", "CALCULATORS", "/guides/calculators.html"),
    ("about", "ABOUT", "/about.html"),
]
RANK = {k: i for i, (k, _, _) in enumerate(NAV_ORDER)}

HEADER_RE = re.compile(r'(<header class="site-header"[^>]*>)(.*?)(</header>)', re.S)
NAV_RE = re.compile(r'(<nav class="header-nav"[^>]*>)(.*?)(</nav>)', re.S)
A_RE = re.compile(r'<a\b[^>]*>.*?</a>', re.S)
TAG_RE = re.compile(r'\s*<script src="/assets/site-nav\.[0-9a-f]+\.js"( defer)?></script>')


def asset_hash() -> str:
    return hashlib.sha1(SRC.read_bytes()).hexdigest()[:10]


def asset_name() -> str:
    return f"site-nav.{asset_hash()}.js"


def script_tag() -> str:
    return f'<script src="/assets/{asset_name()}"></script>'


def key_of(href: str):
    h = re.sub(r'[#?].*$', '', href)
    h = re.sub(r'^https?://(www\.)?renalcarematters\.com', '', h)
    base = h.rstrip('/').split('/')[-1].replace('.html', '')
    if base.startswith('calc'):  # calculators.html / calc-*.html
        return 'calculators'
    if base == 'kidney-physiology':
        return 'physiology'
    if base == 'nephrology-atlas':
        return 'atlas'
    if base == 'about':
        return 'about'
    if re.search(r'(^|/)guides/?$', h) or h in ('guides', '/guides/index.html'):
        return 'guides'
    if re.search(r'(^|/)drugs/?$', h) or h.endswith('/drugs/index.html'):
        return 'drugs'
    if re.search(r'(^|/)academy/?$', h) or h.endswith('/academy/index.html'):
        return 'academy'
    return None


def reorder(nav_inner: str) -> str:
    anchors = A_RE.findall(nav_inner)
    known, other, seen = [], [], set()
    for a in anchors:
        m = re.search(r'href="([^"]*)"', a)
        k = key_of(m.group(1)) if m else None
        if k and k not in seen:
            seen.add(k)
            known.append((RANK[k], a))
        else:
            other.append(a)
    for k, label, href in NAV_ORDER:
        if k not in seen:
            known.append((RANK[k], f'<a href="{href}">{label}</a>'))
    known.sort(key=lambda t: t[0])
    return "".join(a for _, a in known) + "".join(other)


def patch_text(text: str, tag: str):
    m = HEADER_RE.search(text)
    if not m:
        return text
    inner = m.group(2)
    nm = NAV_RE.search(inner)
    if not nm or 'href=' not in nm.group(2):
        return text
    inner = TAG_RE.sub('', inner)
    nm = NAV_RE.search(inner)
    new_nav = nm.group(1) + reorder(nm.group(2)) + nm.group(3) + tag
    inner = inner[:nm.start()] + new_nav + inner[nm.end():]
    return text[:m.start()] + m.group(1) + inner + m.group(3) + text[m.end():]


def pages():
    for pat in ("*.html", "guides/*.html", "academy/*.html", "drugs/*.html",
                "drugs/supplements/*.html", "drugs/category/*.html"):
        yield from sorted(ROOT.glob(pat))


def write_asset(dry: bool) -> bool:
    name = asset_name()
    dst = ROOT / "assets" / name
    changed = not dst.exists()
    if not dry:
        if changed:
            dst.write_bytes(SRC.read_bytes())
        for old in (ROOT / "assets").glob("site-nav.*.js"):
            if old.name != name and re.fullmatch(r"site-nav\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
                changed = True
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run or args.check
    tag = script_tag()
    asset_changed = write_asset(dry)
    changed = 0
    for p in pages():
        t = p.read_text(encoding="utf-8")
        n = patch_text(t, tag)
        if n != t:
            changed += 1
            if not dry:
                p.write_text(n, encoding="utf-8")
    print(f"site-nav: {asset_name()}{' (new)' if asset_changed else ''}; pages {'to update' if dry else 'updated'}: {changed}")
    if args.check and (changed or asset_changed):
        sys.exit(1)


if __name__ == "__main__":
    main()
