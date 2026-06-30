#!/usr/bin/env python3
"""Audit each guide's footer references line for APA-7 conformance.

The site's reference policy (CLAUDE.md §5 + /setup-guide §5):

    Every citation in the footer <p>References: ...</p> line must be APA 7:
        Author, A. A., ..., & Author, Z. Z. (Year). Sentence-case title.
        <em>Journal Name</em>, <em>Volume</em>(Issue), pages.
        <a href="https://doi.org/...">https://doi.org/...</a>

This audit script does NOT mutate any guide. It scans every `guides/*.html`,
extracts the footer references line, splits it on `·`, and classifies each
citation:

    APA          — has a (Year), at least one <em>, a year-paren author block,
                   and a DOI link. (Heuristic; not a parser.)
    LEGACY       — short-form like "Smith 2023 (Nature)" — needs migration.
    EMPTY        — guide has no footer references line (calculators, pure
                   interactive tools — documented exception).

It then prints a per-guide summary and a totals line; a `--list-legacy`
flag emits the legacy short-form citations themselves so the next migration
batch can be planned.

Usage:
    python3 audit_references_apa.py                 # site-wide audit
    python3 audit_references_apa.py --guide foo.html
    python3 audit_references_apa.py --list-legacy   # also print legacy citation strings
    python3 audit_references_apa.py --json out.json # machine-readable
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

GUIDES_DIR = Path(__file__).parent / "guides"

FOOTER_RE = re.compile(r'<p>\s*References\s*:?\s*(.*?)</p>', re.S | re.I)
HEROMETA_RE = re.compile(
    r'<strong>\s*Guidelines\s*:?\s*</strong>\s*(.*?)</span>', re.S | re.I
)
SPLIT_RE = re.compile(r'\s*(?:&middot;|·|&#183;)\s*')

# APA-shaped heuristic: must include (4-digit-year) AND a DOI link AND at least one <em> tag
APA_YEAR_RE = re.compile(r'\(\d{4}\)\.?\s')
APA_DOI_RE = re.compile(r'doi\.org', re.I)
APA_EM_RE = re.compile(r'<em>', re.I)


ACC_LI_RE = re.compile(
    r'<!--\s*REFERENCES-ACC-START\s*-->(.*?)<!--\s*REFERENCES-ACC-END\s*-->',
    re.S | re.I,
)
LI_RE = re.compile(r'<li[^>]*>(.*?)</li>', re.S | re.I)


def extract_footer(text: str) -> str:
    """Return raw inner-HTML of the footer references line (no tag stripping)."""
    m = FOOTER_RE.search(text)
    if m and m.group(1).strip():
        return m.group(1)
    m = re.search(
        r'<p>\s*<strong>\s*References\s*</strong>\s*</p>\s*<p>(.*?)</p>',
        text, re.S | re.I,
    )
    if m and m.group(1).strip():
        return m.group(1)
    m = HEROMETA_RE.search(text)
    if m and m.group(1).strip():
        return m.group(1)
    return ""


def extract_accordion_items(text: str) -> list[str]:
    """Extract <li> entries from the rendered/handauthored references accordion."""
    m = ACC_LI_RE.search(text)
    if not m:
        return []
    return [re.sub(r"\s+", " ", li).strip() for li in LI_RE.findall(m.group(1))]


def classify(citation: str) -> str:
    has_year = bool(APA_YEAR_RE.search(citation))
    has_doi = bool(APA_DOI_RE.search(citation))
    has_em = bool(APA_EM_RE.search(citation))
    # All three signals → APA-shaped. Missing any → legacy short-form.
    if has_year and has_doi and has_em:
        return "APA"
    return "LEGACY"


def audit_guide(path: Path) -> dict:
    text = path.read_text()
    parts: list[str] = []
    source = "none"
    raw = extract_footer(text)
    if raw.strip():
        source = "footer"
        parts = SPLIT_RE.split(raw)
    else:
        # Fall back to hand-authored accordion <li> items
        items = extract_accordion_items(text)
        if items:
            source = "accordion"
            parts = items
    parts = [re.sub(r"\s+", " ", p).strip() for p in parts]
    parts = [p for p in parts if p and p.lower() not in ("references", "guidelines")]
    if not parts:
        return {"file": path.name, "source": "none", "status": "EMPTY", "total": 0, "apa": 0, "legacy": 0, "legacy_items": []}
    apa = sum(1 for c in parts if classify(c) == "APA")
    legacy = [c for c in parts if classify(c) == "LEGACY"]
    return {
        "file": path.name,
        "source": source,
        "status": "ALL_APA" if (apa and not legacy) else ("PARTIAL" if (apa and legacy) else "LEGACY"),
        "total": len(parts),
        "apa": apa,
        "legacy": len(legacy),
        "legacy_items": legacy,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--guide", help="Audit a single guide filename (e.g. ai-in-nephrology-practice.html)")
    ap.add_argument("--list-legacy", action="store_true",
                    help="Print each legacy short-form citation, grouped by guide")
    ap.add_argument("--json", metavar="FILE", help="Write the audit as JSON to FILE")
    args = ap.parse_args()

    if args.guide:
        guides = [GUIDES_DIR / args.guide]
    else:
        guides = sorted(GUIDES_DIR.glob("*.html"))

    results = []
    for g in guides:
        if not g.exists():
            print(f"!! not found: {g.name}", file=sys.stderr)
            continue
        results.append(audit_guide(g))

    # Per-guide table
    totals = {"ALL_APA": 0, "PARTIAL": 0, "LEGACY": 0, "EMPTY": 0}
    legacy_total = 0
    apa_total = 0
    for r in results:
        totals[r["status"]] += 1
        legacy_total += r["legacy"]
        apa_total += r["apa"]
        flag = {
            "ALL_APA": "✓",
            "PARTIAL": "~",
            "LEGACY":  "✗",
            "EMPTY":   "·",
        }[r["status"]]
        src = r.get("source", "none")[:8]
        print(f"  {flag} {r['file']:60s}  src={src:<9}  apa={r['apa']:>3}  legacy={r['legacy']:>3}  total={r['total']:>3}")

    print()
    print(f"Totals:  {len(results)} guide(s) scanned")
    print(f"   ALL_APA  : {totals['ALL_APA']}")
    print(f"   PARTIAL  : {totals['PARTIAL']}")
    print(f"   LEGACY   : {totals['LEGACY']}")
    print(f"   EMPTY    : {totals['EMPTY']}  (calculators / pure tools — exempt)")
    print(f"   citations: {apa_total} APA · {legacy_total} legacy needing migration")

    if args.list_legacy:
        print("\nLegacy short-form citations needing APA migration:")
        for r in results:
            if r["legacy_items"]:
                print(f"\n— {r['file']}")
                for c in r["legacy_items"]:
                    print(f"    · {c}")

    if args.json:
        Path(args.json).write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"\nWrote {args.json}")


if __name__ == "__main__":
    main()
