#!/usr/bin/env python3
"""
patch_canonical_clean_urls.py — renalcarematters.com

Switches every page's *canonical* URL to the extensionless form that Cloudflare Pages
actually serves. Pages answers /guides/igan-guide.html with a 308 redirect to
/guides/igan-guide, and /guides/index.html with a redirect to /guides/, so a canonical
or og:url ending in .html points search engines and share previews at a redirect.

What it rewrites (renalcarematters.com URLs only; other hosts are left alone):
  - <link rel="canonical" href="…">
  - <link rel="alternate" hreflang="…" href="…">
  - <meta property="og:url" content="…">, <meta name="twitter:url" content="…">
  - every renalcarematters.com …html URL inside <script type="application/ld+json">
    (url, @id, mainEntityOfPage, breadcrumb item, isPartOf, …)

Mapping:  /x/index.html -> /x/     /index.html -> /     /x/page.html -> /x/page
Fragments and query strings are kept (…/drugs/meropenem.html#drug -> …/drugs/meropenem#drug).

What it does NOT touch: internal <a href> links (they still work through the redirect),
image/PDF URLs, and anything outside the tags above.

Scope: top-level *.html, guides/*.html, downloads/*.html. The generated drug pages
(drugs/, drugs/supplements/, drugs/category/) are born extensionless by
generate_drug_pages.py and generate_supplement_pages.py; pass --include-drugs to patch
already-built pages in place anyway.

Usage:
  python3 patch_canonical_clean_urls.py                 # patch every page in scope
  python3 patch_canonical_clean_urls.py --dry-run       # report, write nothing
  python3 patch_canonical_clean_urls.py --guide igan-guide.html   # one guide (guides/ first, then root)
  python3 patch_canonical_clean_urls.py --check         # exit 1 if any page in scope still needs patching

Idempotent: a page already on extensionless URLs is reported as unchanged.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
HOST_RE = r"https?://(?:www\.)?renalcarematters\.com"
# A renalcarematters.com URL whose path ends in .html, optionally followed by ?query / #fragment.
SITE_HTML_URL = re.compile(HOST_RE + r"(?P<path>/[^\s\"'<>?#]*?\.html)(?P<rest>[?#][^\s\"'<>]*)?")

HEAD_TAG = re.compile(r"<(?:link|meta)\b[^>]*>", re.I)
JSONLD = re.compile(r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)', re.I | re.S)


def clean_path(path: str) -> str:
    """'/guides/index.html' -> '/guides/', '/index.html' -> '/', '/about.html' -> '/about'."""
    if path.endswith("/index.html"):
        return path[: -len("index.html")]
    if path.endswith(".html"):
        return path[: -len(".html")]
    return path


def clean_url(url: str) -> str:
    """Extensionless form of a renalcarematters.com page URL; any other URL is returned unchanged."""
    def sub(m):
        host = re.match(HOST_RE, m.group(0)).group(0)
        return host + clean_path(m.group("path")) + (m.group("rest") or "")
    return SITE_HTML_URL.sub(sub, url)


def _is_url_tag(tag: str) -> str | None:
    """Return the attribute that carries the URL for tags we own, else None."""
    t = tag.lower()
    if t.startswith("<link"):
        if re.search(r'\brel\s*=\s*["\']?canonical\b', t) or re.search(r"\bhreflang\s*=", t):
            return "href"
    elif t.startswith("<meta"):
        if re.search(r'\b(?:property|name)\s*=\s*["\'](?:og:url|twitter:url)["\']', t):
            return "content"
    return None


def patch_html(text: str) -> tuple[str, int]:
    """Return (new_text, number_of_urls_changed)."""
    n = 0

    def fix_tag(m):
        nonlocal n
        tag = m.group(0)
        attr = _is_url_tag(tag)
        if not attr:
            return tag

        def fix_attr(am):
            nonlocal n
            new = clean_url(am.group(2))
            if new != am.group(2):
                n += 1
            return am.group(1) + new + am.group(3)
        return re.sub(r'(\b' + attr + r'\s*=\s*["\'])([^"\']*)(["\'])', fix_attr, tag, count=1, flags=re.I)

    text = HEAD_TAG.sub(fix_tag, text)

    def fix_jsonld(m):
        nonlocal n
        body = m.group(2)

        def fix_url(um):
            nonlocal n
            new = clean_url(um.group(0))
            if new != um.group(0):
                n += 1
            return new
        return m.group(1) + SITE_HTML_URL.sub(fix_url, body) + m.group(3)

    text = JSONLD.sub(fix_jsonld, text)
    return text, n


def targets(args) -> list[Path]:
    if args.guide:
        for cand in (REPO / "guides" / args.guide, REPO / args.guide, REPO / "downloads" / args.guide):
            if cand.is_file():
                return [cand]
        sys.exit(f"not found: {args.guide}")
    files = sorted(REPO.glob("*.html")) + sorted((REPO / "guides").glob("*.html")) + sorted((REPO / "downloads").glob("*.html"))
    if args.include_drugs:
        for sub in ("drugs", "drugs/supplements", "drugs/category"):
            files += sorted((REPO / sub).glob("*.html"))
    return [f for f in files if not re.search(r" \d+\.html$", f.name)]   # skip iCloud "name 2.html" clones


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="report what would change; write nothing")
    ap.add_argument("--check", action="store_true", help="like --dry-run, but exit 1 if anything needs patching")
    ap.add_argument("--guide", help="patch a single file (looked up in guides/, the repo root, then downloads/)")
    ap.add_argument("--include-drugs", action="store_true", help="also patch generated drugs/ pages in place")
    args = ap.parse_args()
    dry = args.dry_run or args.check

    changed = urls = 0
    for f in targets(args):
        old = f.read_text(encoding="utf-8")
        new, n = patch_html(old)
        if new == old:
            continue
        changed += 1
        urls += n
        rel = f.relative_to(REPO).as_posix()
        if args.guide or args.dry_run or changed <= 20:
            print(f"{'would patch' if dry else 'patched'} {rel} ({n} URL{'s' if n != 1 else ''})")
        if not dry:
            f.write_text(new, encoding="utf-8")
    print(f"{'DRY RUN: ' if dry else ''}{changed} file(s), {urls} URL(s) {'to change' if dry else 'changed'}"
          + ("" if changed else " — already extensionless"))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
