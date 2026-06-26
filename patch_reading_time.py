#!/usr/bin/env python3
"""
patch_reading_time.py — williamriveromd.com

Adds a "Reading time" estimate to every guide's hero (the .hero-meta block,
alongside Author / Specialty / Last Reviewed).

The estimate counts the guide's English body words (translations carried in the
DOM as data-lang="tl/ceb/kap" lang-hidden elements are excluded so the count is
not inflated 4x) and divides by 200 words/minute. The visible value is a small
inline-styled badge; inline styles mean patch_master_css.py will not clobber it
(same technique as the Last Reviewed badge).

Idempotent: a guide that already has a reading-time badge is recomputed/updated
in place. Guides without a .hero-meta block are skipped (e.g. tool pages).

Usage:
    python3 patch_reading_time.py
    python3 patch_reading_time.py --dry-run
    python3 patch_reading_time.py --guide understanding-ckd.html
"""

import re
import argparse
from pathlib import Path

WPM = 200
# The calculators index is a tool listing, not a narrative guide — no byline.
SKIP = {"index.html", "calculators.html"}

BADGE_STYLE = (
    "display:inline-block;background:rgba(184,150,46,.16);"
    "border:1px solid rgba(184,150,46,.5);border-radius:10px;"
    "padding:1px 8px;font-size:12px;letter-spacing:.02em;"
    "color:rgba(255,255,255,.9);"
)

ROW_TMPL = (
    '<span class="hero-readtime"><strong>'
    '<span data-lang="en">Reading time</span>'
    '<span class="lang-hidden" data-lang="tl">Oras ng pagbasa</span>'
    '<span class="lang-hidden" data-lang="ceb">Oras sa pagbasa</span>'
    '<span class="lang-hidden" data-lang="kap">Oras ning pamamasa</span>'
    ':</strong> <time datetime="PT{n}M" style="{style}">~{n} min read</time></span>'
)

# Matches the whole existing row so re-runs refresh the number. The row ends in
# </time></span> (a <time> badge inside the row span) — matching </span></span>
# here would over-run into page body content, so anchor on </time></span>.
ROW_RE = re.compile(r'\n?[ \t]*<span class="hero-readtime">.*?</time></span>', re.S)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def english_word_count(text: str) -> int:
    m = re.search(r"<main\b.*?</main>", text, re.S)
    body = m.group(0) if m else text
    body = re.sub(r"<script\b.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<style\b.*?</style>", " ", body, flags=re.S)
    # Drop non-English translations (lang-hidden inline elements).
    body = re.sub(
        r"<(span|div|p|li|td|th|h\d)\b[^>]*\blang-hidden\b[^>]*>.*?</\1>",
        " ", body, flags=re.S,
    )
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"&[a-z#0-9]+;", " ", body)
    return len(body.split())


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    if '<div class="hero-meta">' not in text:
        return "skip (no hero-meta)"

    words = english_word_count(text)
    minutes = max(1, round(words / WPM))
    row = ROW_TMPL.format(n=minutes, style=BADGE_STYLE)

    # Refresh an existing badge.
    if 'class="hero-readtime"' in text:
        text = ROW_RE.sub("\n" + row, text, count=1)
    else:
        # Insert as the last row, just before the hero-meta closing </div>.
        m = re.search(r'(<div class="hero-meta">.*?)(\n?</div>)', text, re.S)
        if not m:
            return "skip (malformed hero-meta)"
        text = text[:m.start(2)] + "\n" + row + text[m.start(2):]

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return f"✓ ~{minutes} min ({words} words)"


def main():
    ap = argparse.ArgumentParser(description="Add reading-time estimates to guide heroes.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="patch a single guide (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    targets = ([guides_dir / args.guide] if args.guide
               else sorted(p for p in guides_dir.glob("*.html") if p.name not in SKIP))

    changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found"); continue
        if path.name in SKIP:
            continue
        status = patch_guide(path, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {changed} guide(s).")


if __name__ == "__main__":
    main()
