#!/usr/bin/env python3
"""Strip the author byline suffix from page titles used for sharing.

When a guide is shared (Facebook, Viber, X, Messenger ...), the link preview
shows the page title. Titles used to end with an author suffix such as
"… · W Rivero, MD", "… – W Rivero, MD", "… | Dr. W Rivero, MD" or
"… — Dr. Rivero". Site policy (Nov 11 2026): no author name in share titles;
the author is credited in the signature block at the end of each guide.

Touches, in every site HTML page:
  <title>, og:title, twitter:title, and JSON-LD "headline".
Never touches the author JSON-LD, the dr-card, or any visible body text.

Hub pages whose title would become too generic get " · Renal Care Matters"
instead (see HUB_SUFFIX).

Usage:
  python3 patch_share_title.py              # all pages
  python3 patch_share_title.py --dry-run    # report only
  python3 patch_share_title.py --guide igan-guide.html
Idempotent.
"""
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SKIP_DIRS = {"node_modules", ".git", "blueprints", "docs", "image-prompts", "graphify-out"}
HUB_SUFFIX = {"guides/index.html", "guides/calculators.html", "404.html"}
BRAND = "Renal Care Matters"

# Separator, optional "Dr.", optional W / William (+ G./Gregory + M.), "Rivero", optional ", MD"
SUFFIX = re.compile(
    r"\s*(?:·|\||—|–|-)\s*(?:Dr\.?\s*)?"
    r"(?:W(?:illiam)?\.?\s*(?:G(?:regory)?\.?\s*(?:M\.?\s*)?)?)?"
    r"Rivero(?:,?\s*MD)?\s*$"
)

FIELDS = [
    re.compile(r"(<title>)([^<]*)(</title>)"),
    re.compile(r'(<meta\s+(?:property|name)="og:title"\s+content=")([^"]*)(")'),
    re.compile(r'(<meta\s+(?:property|name)="twitter:title"\s+content=")([^"]*)(")'),
    re.compile(r'("headline"\s*:\s*")([^"]*)(")'),
]


def clean(title, hub):
    new = SUFFIX.sub("", title)
    if hub and BRAND not in new:
        new = f"{new} · {BRAND}"
    return new


def patch(path, dry):
    rel = path.relative_to(ROOT).as_posix()
    hub = rel in HUB_SUFFIX
    text = path.read_text(encoding="utf-8")
    changes = []

    def repl(m):
        old = m.group(2)
        new = clean(old, hub) if (SUFFIX.search(old) or hub) else old
        if new != old:
            changes.append((old, new))
        return m.group(1) + new + m.group(3)

    out = text
    for rx in FIELDS:
        out = rx.sub(repl, out)
    if out != text:
        if not dry:
            path.write_text(out, encoding="utf-8")
        print(f"{'[dry] ' if dry else ''}{rel}: {len(changes)} field(s) — {changes[0][1]!r}")
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    if a.guide:
        files = [ROOT / "guides" / a.guide]
    else:
        files = [p for p in ROOT.rglob("*.html")
                 if not (set(p.relative_to(ROOT).parts[:-1]) & SKIP_DIRS)]
    n = sum(patch(p, a.dry_run) for p in sorted(files))
    print(f"{'Would update' if a.dry_run else 'Updated'} {n} page(s).")


if __name__ == "__main__":
    main()
