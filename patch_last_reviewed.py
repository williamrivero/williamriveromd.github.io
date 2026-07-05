#!/usr/bin/env python3
"""
patch_last_reviewed.py — williamriveromd.com

Makes "Last Reviewed" dates visible and trustworthy on every guide page,
and signals content freshness to search engines.

Changes per guide:
  1. "Updated" label → "Last Reviewed" (with correct multilingual translations)
  2. Wraps the date value in <time datetime="YYYY-05-01"> with a teal badge
  3. For guides without any date, inserts a new Last Reviewed row in hero-meta
  4. Adds <meta property="article:modified_time"> to <head>
  5. Adds MedicalWebPage JSON-LD schema with dateModified to <head>

Skips: guides/index.html, guides/lab-interpreter.html (no hero-meta).

Usage:
    python3 patch_last_reviewed.py
    python3 patch_last_reviewed.py --dry-run
    python3 patch_last_reviewed.py --guide anemia-management.html
"""

import re
import json
import argparse
from pathlib import Path


SKIP = {"index.html", "lab-interpreter.html"}

# Badge: teal pill on dark hero background, inline styles so patch_master_css.py won't clobber it.
BADGE_TMPL = (
    '<time datetime="{dt}" '
    'style="display:inline-block;background:rgba(26,107,114,.18);'
    'border:1px solid rgba(26,107,114,.5);border-radius:10px;'
    'padding:1px 8px;font-size:12px;letter-spacing:.02em;'
    'color:rgba(255,255,255,.9);">'
    '{label}'
    '</time>'
)

# Canonical single-line replacement span (used for both existing and new rows).
REVIEWED_SPAN = (
    '<span><strong>'
    '<span data-lang="en">Last Reviewed</span>'
    '<span class="lang-hidden" data-lang="tl">Huling Na-review</span>'
    '<span class="lang-hidden" data-lang="ceb">Katapusang Na-review</span>'
    '<span class="lang-hidden" data-lang="kap">Karinan Na-review</span>'
    ':</strong> {badge}</span>'
)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def extract_year(text: str) -> int:
    """Highest 4-digit year ≥ 2024 found in text, else 2025."""
    years = [int(y) for y in re.findall(r'\b(20\d{2})\b', text) if int(y) >= 2024]
    return max(years) if years else 2025


def guess_year(html: str) -> int:
    """For dateless guides: scan early meta section then full file for a relevant year."""
    # Prefer years ≥ 2025 in first 1 KB (title, meta desc, og tags)
    years_early = [int(y) for y in re.findall(r'\b(20\d{2})\b', html[:1000]) if int(y) >= 2025]
    if years_early:
        return max(years_early)
    # Fall back to entire file
    years_all = [int(y) for y in re.findall(r'\b(20\d{2})\b', html) if int(y) >= 2025]
    return max(years_all) if years_all else 2025


def is_updated_start(line: str) -> bool:
    """True if this line opens the hero-meta Updated span."""
    # Two label formats: >Updated< and >Updated:< (colon inside span)
    has_updated = '>Updated<' in line or '>Updated:<' in line or '<strong>Updated:</strong>' in line
    # Exclude "Updated" badges/pills inside the article body
    is_body = any(x in line for x in ('new-badge', 'gc-updated-pill', 'filter-chip', 'jump-pill', 'section-label'))
    return has_updated and not is_body


def patch_guide(path: Path, dry_run: bool = False) -> str:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    # Idempotency: already patched if hero-meta contains a <time datetime= badge.
    hero_m = re.search(r'<div[^>]*class="hero-meta"[^>]*>(.*?)</div>', text, re.DOTALL)
    if hero_m and '<time datetime=' in hero_m.group(1):
        return "unchanged (already patched)"

    lines = text.splitlines(keepends=True)

    # ── Locate the Updated block ──────────────────────────────────────────────
    start_idx = end_idx = None
    for i, raw_line in enumerate(lines):
        line = raw_line.rstrip('\n')
        if is_updated_start(line):
            start_idx = i
            if '</strong>' in line:
                end_idx = i          # single-line
            else:
                for j in range(i + 1, min(i + 20, len(lines))):
                    if '</strong>' in lines[j]:
                        end_idx = j
                        break
            break

    # ── Case A: existing Updated block found → replace it ────────────────────
    if start_idx is not None and end_idx is not None:
        block = ''.join(lines[start_idx: end_idx + 1])
        date_m = re.search(r'</strong>\s*(.+?)\s*</span>', block, re.DOTALL)
        if not date_m:
            return "SKIP: could not extract date from Updated block"

        raw_date = re.sub(r'<[^>]+>', '', date_m.group(1)).strip()
        year = extract_year(raw_date)

        badge = BADGE_TMPL.format(dt=f"{year}-05-01", label=raw_date)
        indent = re.match(r'^(\s*)', lines[start_idx]).group(1)
        replacement = indent + REVIEWED_SPAN.format(badge=badge) + '\n'

        lines = lines[:start_idx] + [replacement] + lines[end_idx + 1:]
        changes.append("label+badge")

    # ── Case B: no Updated block → insert new row into hero-meta ─────────────
    elif start_idx is None:
        hero_meta_idx = None
        for i, raw_line in enumerate(lines):
            if 'class="hero-meta"' in raw_line and '<div' in raw_line:
                hero_meta_idx = i
                break
        if hero_meta_idx is None:
            return "SKIP: no hero-meta div found"

        # Find the closing </div> of hero-meta (first </div> after the opening tag)
        close_idx = None
        for i in range(hero_meta_idx + 1, min(hero_meta_idx + 30, len(lines))):
            if '</div>' in lines[i]:
                close_idx = i
                break
        if close_idx is None:
            return "SKIP: could not find hero-meta closing </div>"

        year = guess_year(text)
        badge = BADGE_TMPL.format(dt=f"{year}-05-01", label=str(year))
        indent = re.match(r'^(\s*)', lines[close_idx]).group(1)
        new_span = indent + REVIEWED_SPAN.format(badge=badge) + '\n'
        lines = lines[:close_idx] + [new_span] + lines[close_idx:]
        changes.append("inserted Last Reviewed row")

    else:
        return "SKIP: malformed Updated block (start found, end not found)"

    text = ''.join(lines)

    # ── Add article:modified_time Open Graph meta tag ─────────────────────────
    if 'article:modified_time' not in text:
        # Derive year from whatever we wrote
        yr_m = re.search(r'datetime="(\d{4})-', text)
        year = int(yr_m.group(1)) if yr_m else 2025
        tz_datetime = f"{year}-05-01T00:00:00+08:00"

        meta_tag = f'<meta property="article:modified_time" content="{tz_datetime}">'
        og_type = re.search(r'(<meta property="og:type"[^>]*/?>)', text)
        if og_type:
            text = text[:og_type.end()] + '\n' + meta_tag + text[og_type.end():]
        else:
            text = text.replace('</head>', meta_tag + '\n</head>', 1)
        changes.append("article:modified_time")

    # ── Add MedicalWebPage JSON-LD ────────────────────────────────────────────
    if 'dateModified' not in text:
        yr_m = re.search(r'datetime="(\d{4})-', text)
        year = int(yr_m.group(1)) if yr_m else 2025
        datetime_val = f"{year}-05-01"

        canonical_m = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        title_m = re.search(r'<meta property="og:title" content="([^"]+)"', text)
        canonical = canonical_m.group(1) if canonical_m else ''
        title = title_m.group(1) if title_m else path.stem.replace('-', ' ').title()

        schema = {
            "@context": "https://schema.org",
            "@type": "MedicalWebPage",
            "name": title,
            "url": canonical,
            "author": {
                "@type": "Physician",
                "name": "William Gregory M. Rivero, MD, FPCP, DPSN",
                "url": "https://renalcarematters.com/",
            },
            "dateModified": datetime_val,
            "datePublished": f"{year}-01-01",
            "inLanguage": "en-PH",
            "audience": {
                "@type": "MedicalAudience",
                "audienceType": "patient",
            },
        }
        ld_block = (
            '<script type="application/ld+json">\n'
            + json.dumps(schema, indent=2, ensure_ascii=False)
            + '\n</script>'
        )
        text = text.replace('</head>', ld_block + '\n</head>', 1)
        changes.append("JSON-LD")

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ " + ", ".join(changes)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--guide", metavar="FILENAME", help="Process one guide (e.g. anemia-management.html)")
    args = parser.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"

    if args.guide:
        files = [guides_dir / args.guide]
    else:
        files = sorted(f for f in guides_dir.glob("*.html") if f.name not in SKIP)

    ok = skipped = 0
    for path in files:
        status = patch_guide(path, dry_run=args.dry_run)
        prefix = "DRY " if args.dry_run else ""
        print(f"{prefix}{path.name}: {status}")
        if status.startswith("✓"):
            ok += 1
        else:
            skipped += 1

    dry_label = "DRY RUN — " if args.dry_run else ""
    print(f"\n{dry_label}Done: {ok} patched, {skipped} skipped/unchanged")


if __name__ == "__main__":
    main()
