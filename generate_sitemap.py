#!/usr/bin/env python3
"""
generate_sitemap.py
Regenerates sitemap.xml from the HTML files actually present in the repo,
so the sitemap can never silently drift out of sync with the guides again.

What it does
------------
- Discovers every indexable page: the homepage, the /guides/ index, all
  guides/*.html, downloads/*.html, and other top-level *.html pages.
- Skips pages that should NOT be indexed: anything under a px/ path
  (matches robots.txt "Disallow: /guides/px/"), 404.html, and any file
  containing <meta name="robots" content="...noindex...">.
- Preserves the existing <lastmod>/<changefreq>/<priority> for URLs that
  are already in sitemap.xml, so deliberate per-page tuning (e.g. the
  0.8 clinician guides, the yearly 0.5 drinking log) is never clobbered.
- Applies sensible defaults only to brand-new pages.
- Drops entries whose files no longer exist (dead-link cleanup).
- Emits a deterministic ordering so future diffs stay small.

Usage
-----
    python3 generate_sitemap.py              # rewrite sitemap.xml
    python3 generate_sitemap.py --dry-run    # show what would change, write nothing

Run it before every deploy (or wire it into CI) and the sitemap stays
correct with zero manual maintenance.
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SITE = "https://www.williamriveromd.com"
SITEMAP_PATH = REPO_ROOT / "sitemap.xml"

# Defaults applied ONLY to pages not already present in sitemap.xml.
DEFAULTS = {
    "home": ("weekly", "1.0"),
    "guides_index": ("weekly", "0.9"),
    "guide": ("monthly", "0.7"),
    "download": ("monthly", "0.6"),
    "toplevel": ("monthly", "0.7"),
}

NOINDEX_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]*content=["\'][^"\']*noindex', re.I
)
EXISTING_ENTRY_RE = re.compile(
    r"<loc>(?P<loc>.*?)</loc>\s*"
    r"<lastmod>(?P<lastmod>.*?)</lastmod>\s*"
    r"<changefreq>(?P<changefreq>.*?)</changefreq>\s*"
    r"<priority>(?P<priority>.*?)</priority>",
    re.S,
)

# Files that exist on disk but must never appear in the sitemap.
EXCLUDE_NAMES = {"404.html"}


def is_noindex(path: Path) -> bool:
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:4000]
    except OSError:
        return False
    return bool(NOINDEX_RE.search(head))


def classify(rel_path: str) -> tuple[str, str] | None:
    """Return (url_path, kind) for an indexable file, or None to skip."""
    parts = rel_path.split("/")
    if "px" in parts:                       # robots.txt Disallow: /guides/px/
        return None
    name = parts[-1]
    if name in EXCLUDE_NAMES:
        return None

    if rel_path == "index.html":
        return "/", "home"
    if rel_path == "guides/index.html":
        return "/guides/", "guides_index"
    if rel_path.startswith("guides/"):
        return "/" + rel_path, "guide"
    if rel_path.startswith("downloads/"):
        return "/" + rel_path, "download"
    if "/" not in rel_path:                  # other top-level .html page
        return "/" + rel_path, "toplevel"
    return None


def discover_pages() -> list[tuple[str, str]]:
    """Walk the repo and return sorted (url_path, kind) for indexable pages."""
    found: list[tuple[str, str]] = []
    scan_dirs = [REPO_ROOT, REPO_ROOT / "guides", REPO_ROOT / "downloads"]
    seen: set[str] = set()
    for base in scan_dirs:
        if not base.is_dir():
            continue
        for entry in sorted(base.glob("*.html")):
            rel = entry.relative_to(REPO_ROOT).as_posix()
            if rel in seen:
                continue
            seen.add(rel)
            classified = classify(rel)
            if classified is None:
                continue
            if is_noindex(entry):
                continue
            url_path, kind = classified
            found.append((url_path, kind))
    return found


def load_existing() -> dict[str, dict[str, str]]:
    """Map full URL -> {lastmod, changefreq, priority} from the current sitemap."""
    if not SITEMAP_PATH.exists():
        return {}
    text = SITEMAP_PATH.read_text(encoding="utf-8")
    out: dict[str, dict[str, str]] = {}
    for m in EXISTING_ENTRY_RE.finditer(text):
        out[m.group("loc").strip()] = {
            "lastmod": m.group("lastmod").strip(),
            "changefreq": m.group("changefreq").strip(),
            "priority": m.group("priority").strip(),
        }
    return out


def sort_key(item: tuple[str, str]) -> tuple[int, str]:
    url_path, kind = item
    order = {
        "home": 0,
        "guides_index": 1,
        "toplevel": 2,
        "guide": 3,
        "download": 4,
    }
    return (order.get(kind, 9), url_path)


def build_sitemap() -> tuple[str, list[str], list[str]]:
    """Return (xml_text, added_urls, removed_urls)."""
    today = datetime.date.today().isoformat()
    existing = load_existing()
    pages = sorted(discover_pages(), key=sort_key)

    current_urls = {f"{SITE}{p}" for p, _ in pages}
    added = sorted(u for u in current_urls if u not in existing)
    removed = sorted(u for u in existing if u not in current_urls)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url_path, kind in pages:
        loc = f"{SITE}{url_path}"
        prev = existing.get(loc)
        if prev:  # preserve human-tuned values
            lastmod = prev["lastmod"]
            changefreq = prev["changefreq"]
            priority = prev["priority"]
        else:
            changefreq, priority = DEFAULTS[kind]
            lastmod = today
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n", added, removed


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing sitemap.xml",
    )
    args = parser.parse_args()

    xml_text, added, removed = build_sitemap()
    total = xml_text.count("<loc>")

    label = "DRY RUN — " if args.dry_run else ""
    print(f"{label}{total} URLs in sitemap")
    if added:
        print(f"  + {len(added)} added:")
        for u in added:
            print(f"      {u}")
    if removed:
        print(f"  - {len(removed)} removed (file no longer exists):")
        for u in removed:
            print(f"      {u}")
    if not added and not removed:
        print("  (no additions or removals — sitemap already in sync)")

    if args.dry_run:
        return 0

    old = SITEMAP_PATH.read_text(encoding="utf-8") if SITEMAP_PATH.exists() else ""
    if old == xml_text:
        print("sitemap.xml unchanged.")
        return 0
    SITEMAP_PATH.write_text(xml_text, encoding="utf-8")
    print(f"Wrote {SITEMAP_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
