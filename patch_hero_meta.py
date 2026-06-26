#!/usr/bin/env python3
"""
patch_hero_meta.py — williamriveromd.com

Reworks the hero-meta byline on every guide:

  - REMOVES the "Author: W Rivero, MD, FPCP, DPSN" row (the author is already
    credited in the signature/dr-card block at the end of every guide).
  - ADDS a "Published" row showing the guide's publish date (from the immutable
    article:published_time stamp).
  - ADDS a "References" row showing how many sources the guide was built on
    (the count of items in the accordion References section).

Both new rows are multilingual and inline-styled (so patch_master_css.py will
not clobber them) and are inserted at the top of .hero-meta, where the author
line used to be. Idempotent — re-running refreshes the date and the reference
count in place.

Skipped: pages without a .hero-meta block. The References row is omitted for a
guide that has no accordion References section (e.g. pure interactive tools).

Usage:
    python3 patch_hero_meta.py
    python3 patch_hero_meta.py --dry-run
    python3 patch_hero_meta.py --guide understanding-ckd.html
"""

import re
import argparse
from datetime import datetime
from pathlib import Path

# The calculators index is a tool listing, not a narrative guide — no byline.
SKIP = {"index.html", "calculators.html"}

TEAL_BADGE = (
    "display:inline-block;background:rgba(26,107,114,.18);"
    "border:1px solid rgba(26,107,114,.5);border-radius:10px;"
    "padding:1px 8px;font-size:12px;letter-spacing:.02em;color:rgba(255,255,255,.9);"
)
SLATE_BADGE = (
    "display:inline-block;background:rgba(120,134,150,.18);"
    "border:1px solid rgba(120,134,150,.5);border-radius:10px;"
    "padding:1px 8px;font-size:12px;letter-spacing:.02em;color:rgba(255,255,255,.9);"
)

PUBLISHED_ROW = (
    '<span class="hero-published"><strong>'
    '<span data-lang="en">Published</span>'
    '<span class="lang-hidden" data-lang="tl">Nailathala</span>'
    '<span class="lang-hidden" data-lang="ceb">Gipatik</span>'
    '<span class="lang-hidden" data-lang="kap">Pepalwal</span>'
    ':</strong> <time datetime="{iso}" style="{badge}">{label}</time></span>'
)

REFS_ROW = (
    '<span class="hero-refcount"><strong>'
    '<span data-lang="en">References</span>'
    '<span class="lang-hidden" data-lang="tl">Mga Sanggunian</span>'
    '<span class="lang-hidden" data-lang="ceb">Mga Tinubdan</span>'
    '<span class="lang-hidden" data-lang="kap">Reng Reperensya</span>'
    ':</strong> <span style="{badge}">{n}</span></span>'
)

# English-only rows for calculators.
PUBLISHED_ROW_EN = (
    '<span class="hero-published"><strong>Published:</strong> '
    '<time datetime="{iso}" style="{badge}">{label}</time></span>'
)
REFS_ROW_EN = (
    '<span class="hero-refcount"><strong>References:</strong> '
    '<span style="{badge}">{n}</span></span>'
)


def is_calc(name: str) -> bool:
    return name.startswith("calc-") or name == "ckd-dri-calculator.html"


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def split_top_level_spans(inner: str):
    """Yield ('span', html) / ('text', html) for the direct children of hero-meta,
    walking nested <span> correctly."""
    rows, i, n = [], 0, len(inner)
    while i < n:
        start = inner.find('<span', i)
        if start == -1:
            if inner[i:].strip():
                rows.append(('text', inner[i:]))
            break
        if inner[i:start].strip():
            rows.append(('text', inner[i:start]))
        depth, j = 0, start
        while j < n:
            if inner.startswith('<span', j):
                depth += 1
                j = inner.find('>', j) + 1
            elif inner.startswith('</span>', j):
                depth -= 1
                j += len('</span>')
                if depth == 0:
                    break
            else:
                j += 1
        rows.append(('span', inner[start:j]))
        i = j
    return rows


def is_author_row(span_html: str) -> bool:
    """A hero-meta row that credits the author (any of the legacy formats)."""
    return bool(re.search(r'rivero|curated by', span_html, re.I))


def is_managed_row(span_html: str) -> bool:
    return 'hero-published' in span_html or 'hero-refcount' in span_html


def is_specialty_row(span_html: str) -> bool:
    """The 'Specialty:' hero row — dropped to save header space (the specialty is
    credited in the signature/dr-card block)."""
    return bool(re.search(r'>\s*Specialty\s*:?\s*<', span_html, re.I))


def is_last_reviewed_row(span_html: str) -> bool:
    """A 'Last Reviewed' row — dropped from the hero (replaced by a conditional
    'Last updated' row managed by patch_last_updated.py)."""
    return bool(re.search(r'Last Reviewed|Huling Na-review|Katapusang Na-review', span_html, re.I))


def is_stray_reading_row(span_html: str) -> bool:
    """A duplicate/legacy reading-time row that is NOT the managed hero-readtime
    badge (some guides were authored with their own 'Reading time'/'Read time'
    row before the patch was introduced)."""
    if 'hero-readtime' in span_html:
        return False
    return bool(re.search(r'Reading time|Read time', span_html, re.I))


def ref_count(text: str) -> int:
    m = re.search(r'REFERENCES-ACC-START.*?REFERENCES-ACC-END', text, re.S)
    return len(re.findall(r'<li\b', m.group(0))) if m else 0


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    hm = re.search(r'(<div class="hero-meta">)(.*?)(</div>)', text, re.S)
    if not hm:
        return "skip (no hero-meta)"

    # 1. Drop the author byline (any legacy format) and any prior managed rows.
    kept = []
    for kind, html in split_top_level_spans(hm.group(2)):
        if kind != 'span':
            continue  # whitespace between rows — re-normalized below
        if (is_author_row(html) or is_managed_row(html)
                or is_last_reviewed_row(html) or is_stray_reading_row(html)
                or is_specialty_row(html)):
            continue
        kept.append(html.strip())

    # 2. Build the new Published + References rows (prepended, where author was).
    calc = is_calc(path.name)
    pub_tmpl = PUBLISHED_ROW_EN if calc else PUBLISHED_ROW
    refs_tmpl = REFS_ROW_EN if calc else REFS_ROW
    new_rows = []
    pm = re.search(r'<meta property="article:published_time" content="([^"]+)"', text)
    if pm:
        try:
            dt = datetime.fromisoformat(pm.group(1))
            label = dt.strftime("%b %-d, %Y")
            new_rows.append(pub_tmpl.format(iso=pm.group(1), label=label, badge=TEAL_BADGE))
        except ValueError:
            pass
    n = ref_count(text)
    if n:
        new_rows.append(refs_tmpl.format(n=n, badge=SLATE_BADGE))

    inner = "\n" + "\n".join(new_rows + kept) + "\n"
    text = text[:hm.start()] + hm.group(1) + inner + hm.group(3) + text[hm.end():]

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    bits = []
    if pm:
        bits.append("published")
    if n:
        bits.append(f"{n} refs")
    return "✓ " + ", ".join(bits or ["author removed"])


def main():
    ap = argparse.ArgumentParser(description="Rework hero-meta byline (author → published + refs).")
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
