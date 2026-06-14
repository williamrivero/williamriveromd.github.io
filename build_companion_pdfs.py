#!/usr/bin/env python3
"""
Render every companion HTML in downloads/ to its matching PDF (WeasyPrint).

All patient companion handouts share one house style — downloads/_companion-style.css
(canonical reference layout: wgmr-diabetic-diet-guide.html). Each guide is a
standalone downloads/<name>.html that links that stylesheet; this script renders
each one to downloads/<name>.pdf so the whole Downloads set stays visually uniform.

Usage:
    python3 build_companion_pdfs.py                 # render all companion HTMLs
    python3 build_companion_pdfs.py wgmr-gout-uric-acid-guide   # render one (no .html)
    python3 build_companion_pdfs.py --list          # list buildable companions

Requires: weasyprint  (pip install weasyprint)
Files beginning with "_" (e.g. _companion-style.css) are partials and skipped.
"""
import sys
from pathlib import Path

from weasyprint import HTML

ROOT = Path(__file__).parent
DL = ROOT / "downloads"


def companions():
    return sorted(p for p in DL.glob("*.html") if not p.name.startswith("_"))


def build(html_path: Path):
    pdf_path = html_path.with_suffix(".pdf")
    HTML(str(html_path)).write_pdf(str(pdf_path))
    print(f"  ✓ {html_path.name}  →  {pdf_path.name}  ({pdf_path.stat().st_size // 1024} KB)")


def main(argv):
    if "--list" in argv:
        for p in companions():
            print(p.stem)
        return
    names = [a for a in argv if not a.startswith("-")]
    if names:
        targets = [DL / (n if n.endswith(".html") else n + ".html") for n in names]
    else:
        targets = companions()
    print(f"Rendering {len(targets)} companion PDF(s)…")
    for t in targets:
        if not t.exists():
            print(f"  ✗ {t.name} not found")
            continue
        build(t)


if __name__ == "__main__":
    main(sys.argv[1:])
