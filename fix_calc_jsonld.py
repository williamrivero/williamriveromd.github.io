#!/usr/bin/env python3
"""fix_calc_jsonld.py — align the JSON-LD block on standalone calculator pages.

The calculator pages are scaffolded from a source guide (make_calc_shell.py),
so their inline JSON-LD still carries the source guide's name/url/dates. This
rewrites, for every guides/calc-*.html, the JSON-LD "name" (from the page
<title>, minus the trailing " – W. G. M. Rivero, MD"), "url" (from the page's
<link rel="canonical">), and the date fields to the review date. Idempotent.

Usage:
    python3 fix_calc_jsonld.py [--dry-run]
"""
import re
import sys
from pathlib import Path

REVIEW_DATE = "2026-06-01"


def fix(path: Path, dry: bool) -> bool:
    html = path.read_text(encoding="utf-8")
    m_title = re.search(r"<title>(.*?)</title>", html, re.S)
    m_canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not m_title or not m_canon or "application/ld+json" not in html:
        return False
    name = re.sub(r"\s*[–\-·]\s*W\.\s*G\.\s*M\.\s*Rivero,?\s*MD\s*$", "",
                  m_title.group(1).strip())
    # JSON-LD strings are not HTML — use literal characters, not entities.
    name = name.replace("&amp;", "&")
    url = m_canon.group(1).strip()

    orig = html
    html = re.sub(r'("name":\s*)"[^"]*"', r'\1"%s"' % name, html, count=1)
    html = re.sub(r'("url":\s*)"https://www\.williamriveromd\.com/guides/[^"]*"',
                  r'\1"%s"' % url, html, count=1)
    html = re.sub(r'("dateModified":\s*)"[^"]*"', r'\1"%s"' % REVIEW_DATE, html, count=1)
    html = re.sub(r'("datePublished":\s*)"[^"]*"', r'\1"%s"' % REVIEW_DATE, html, count=1)
    if html == orig:
        return False
    if not dry:
        path.write_text(html, encoding="utf-8")
    print(("would fix " if dry else "fixed ") + path.name + f"  → {name}")
    return True


def main():
    dry = "--dry-run" in sys.argv
    root = Path(__file__).parent / "guides"
    n = 0
    for p in sorted(root.glob("calc-*.html")):
        if fix(p, dry):
            n += 1
    print(f"{'(dry-run) ' if dry else ''}{n} file(s) updated")


if __name__ == "__main__":
    main()
