#!/usr/bin/env python3
"""
check_footer_reference_dup.py — williamriveromd.com

Guards against the footer-References duplication bug: a guide's References
must render in exactly ONE place — the collapsible accordion
(<!-- REFERENCES-ACC-START --> ... <!-- REFERENCES-ACC-END -->) placed
immediately before .dr-card-wrap. Per CLAUDE.md rule 5, the old
<p>References: A · B · C</p> line inside <footer class="guide-footer"> is
DEPRECATED and must not also render — when both exist, the citations show
up twice on the page (accordion + a giant paragraph in the footer).

This script detects any guide where both the accordion and a footer
`<p>References:` line are present, and can strip the footer line.

The accordion is self-sourcing once built: patch_references_accordion.py
preserves an existing accordion's <ol> across re-runs, so deleting the
footer sourcing line does not lose any citations already rendered.

Usage:
    python3 check_footer_reference_dup.py                # report only, exit 1 if any found
    python3 check_footer_reference_dup.py --fix           # strip the footer line from every guide found
    python3 check_footer_reference_dup.py --guide foo.html
    python3 check_footer_reference_dup.py --guide foo.html --fix
"""
import re
import sys
from pathlib import Path

GUIDES = Path(__file__).parent / "guides"
SKIP_EXACT = {"index.html", "calculators.html"}

ACC_RE = re.compile(r'<!-- REFERENCES-ACC-START -->.*?<!-- REFERENCES-ACC-END -->', re.DOTALL)
FOOTER_REF_RE = re.compile(r'\n?[ \t]*<p>References:.*?</p>\n?', re.DOTALL)
FOOTER_TAG_RE = re.compile(r'<footer class="guide-footer">.*?</footer>', re.DOTALL)


def has_footer_ref_line(src: str) -> bool:
    m = FOOTER_TAG_RE.search(src)
    if not m:
        return bool(FOOTER_REF_RE.search(src))
    return bool(re.search(r'<p>References:', m.group(0)))


def check_file(path: Path, fix: bool) -> str:
    src = path.read_text(encoding="utf-8")
    has_accordion = bool(ACC_RE.search(src))
    has_footer_line = has_footer_ref_line(src)

    if not (has_accordion and has_footer_line):
        return "ok"

    if not fix:
        return "DUPLICATE"

    new_src, n = FOOTER_REF_RE.subn("\n", src)
    if n:
        path.write_text(new_src, encoding="utf-8")
        return f"FIXED ({n} line removed)"
    return "DUPLICATE (fix found nothing to remove — check manually)"


def main():
    fix = "--fix" in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--guide" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]
            if not only.endswith(".html"):
                only += ".html"

    targets = [GUIDES / only] if only else sorted(GUIDES.glob("*.html"))

    duplicates = []
    fixed = []
    examined = 0

    for p in targets:
        if p.name in SKIP_EXACT or not p.exists():
            continue
        examined += 1
        result = check_file(p, fix)
        if result == "DUPLICATE":
            duplicates.append(p.name)
        elif result.startswith("FIXED"):
            fixed.append(p.name)

    print("=== Footer-References duplication check ===")
    print(f"Examined:  {examined} guide(s)")
    if fix:
        print(f"Fixed:     {len(fixed)}")
        for n in fixed:
            print(f"  ✓ {n}")
    else:
        print(f"Duplicates found: {len(duplicates)}")
        for n in duplicates:
            print(f"  ✗ {n}  (accordion + footer <p>References:> both present)")
        if duplicates:
            print("\nRun with --fix to strip the deprecated footer line from these guides.")

    return 1 if (duplicates and not fix) else 0


if __name__ == "__main__":
    sys.exit(main())
