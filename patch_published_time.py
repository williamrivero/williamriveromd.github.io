#!/usr/bin/env python3
"""
patch_published_time.py — williamriveromd.com

Date- and time-stamps every guide with the moment it was *made and published*.

Policy: **all guides, from here on, must carry a published timestamp.** This
script records that timestamp as an immutable, machine-readable Open Graph
`article:published_time` meta tag in <head> and aligns the JSON-LD
`datePublished` value to match. It is the recency signal that drives the
"Latest Guides" strip on guides/index.html (see generate_latest_guides.py).

The published time is, in order of preference:
  1. An existing <meta property="article:published_time"> — never overwritten
     (a publish date is immutable once set).
  2. The guide's first-commit (add) datetime in git, converted to Manila time
     (+08:00) — the truthful "when it was made" for already-committed guides.
  3. datetime.now() in +08:00 — for a brand-new guide not yet committed.

Changes per guide (only when article:published_time is absent):
  1. Inserts <meta property="article:published_time" content="YYYY-MM-DDTHH:MM:SS+08:00">
     immediately before article:modified_time (or after og:type / before </head>).
  2. Rewrites the JSON-LD "datePublished" placeholder (e.g. "2026-01-01") to the
     real published date, when a MedicalWebPage block is present.

Idempotent: a guide that already has article:published_time is left untouched.

Usage:
    python3 patch_published_time.py
    python3 patch_published_time.py --dry-run
    python3 patch_published_time.py --guide hmo-ckd-coverage.html
"""

import re
import argparse
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

MANILA = timezone(timedelta(hours=8))

# Stamp every guide page. (calc-*, calculators, symptom-checker etc. are guides
# too and benefit from a publish date; only the directory index is skipped.)
SKIP = {"index.html"}


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def git_first_added_map(project_dir: Path) -> dict:
    """Map 'guides/<file>.html' -> first-add datetime (Manila tz) in ONE git pass."""
    result = {}
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--name-only",
             "--pretty=format:COMMIT %aI", "--", "guides/*.html"],
            cwd=str(project_dir), capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return result

    cur = None
    for line in out.splitlines():
        if line.startswith("COMMIT "):
            cur = line[len("COMMIT "):].strip()
        elif cur and line.startswith("guides/") and line.endswith(".html"):
            # git log is newest→oldest, so overwriting leaves the OLDEST (original)
            # add commit as the final value — exactly the "when it was made" date.
            result[line] = cur
    return result


def to_manila(iso: str) -> datetime:
    dt = datetime.fromisoformat(iso)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(MANILA)


def patch_guide(path: Path, published: datetime, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    if 'article:published_time' in text:
        return "unchanged (already stamped)"

    stamp = published.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    pub_date = published.strftime("%Y-%m-%d")
    meta_tag = f'<meta property="article:published_time" content="{stamp}">'

    # Insert before article:modified_time, else after og:type, else before </head>.
    mod = re.search(r'\n[ \t]*<meta property="article:modified_time"[^>]*>', text)
    og_type = re.search(r'(<meta property="og:type"[^>]*/?>)', text)
    if mod:
        text = text[:mod.start()] + '\n' + meta_tag + text[mod.start():]
    elif og_type:
        text = text[:og_type.end()] + '\n' + meta_tag + text[og_type.end():]
    else:
        text = text.replace('</head>', meta_tag + '\n</head>', 1)

    # Align JSON-LD datePublished placeholder to the real published date.
    text = re.sub(
        r'("datePublished":\s*")\d{4}-\d{2}-\d{2}(")',
        rf'\g<1>{pub_date}\g<2>',
        text,
    )

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return f"✓ published {stamp}"


def main():
    ap = argparse.ArgumentParser(description="Stamp guides with article:published_time.")
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--guide", help="patch a single guide (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    added = git_first_added_map(project_dir)

    if args.guide:
        targets = [guides_dir / args.guide]
    else:
        targets = sorted(p for p in guides_dir.glob("*.html") if p.name not in SKIP)

    now_manila = datetime.now(MANILA)
    changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found")
            continue
        if path.name in SKIP:
            continue
        rel = f"guides/{path.name}"
        if rel in added:
            published = to_manila(added[rel])
        else:
            published = now_manila  # brand-new, uncommitted guide
        status = patch_guide(path, published, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    verb = "Would stamp" if args.dry_run else "Stamped"
    print(f"\n{verb} {changed} guide(s).")


if __name__ == "__main__":
    main()
