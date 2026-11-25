"""Larger reading type for every Renal Care Academy page (Dr. Rivero, Nov 25 2026). Idempotent.

The Academy pages set their font sizes in px across the master CSS and the course CSS, so one rule scales the
reading area instead: CSS zoom on the content blocks (main, the pre-main callouts, glossary, references and
related guides) plus the hero subtitle and meta. The header, nav strip, floating buttons and the side rail are not
zoomed. Runs after every publish (publish_academy.py), so generator rebuilds keep it.

    python3 tools/academy/apply_type_scale.py
"""
import re
from pathlib import Path

ACADEMY = Path(__file__).resolve().parents[2] / "academy"

CSS = """<style id="academy-type">
/* Larger reading type for the Academy: about 18 px body text on computers, 17.5 px on phones */
body > main, body > div.container, body > .glossary-section, body > .ref-section, body > .related-guides { zoom: 1.125; }
.hero .hero-sub, .hero .hero-meta, .hero .hero-abstract { zoom: 1.12; }
@media (max-width: 640px) {
  body > main, body > div.container, body > .glossary-section, body > .ref-section, body > .related-guides { zoom: 1.09; }
  .hero .hero-sub, .hero .hero-meta, .hero .hero-abstract { zoom: 1.08; }
}
@media print {
  body > main, body > div.container, body > .glossary-section, body > .ref-section, body > .related-guides,
  .hero .hero-sub, .hero .hero-meta, .hero .hero-abstract { zoom: 1; }
}
</style>"""

BLOCK_RE = re.compile(r'\n?<style id="academy-type">.*?</style>', re.S)


def apply(text):
    text = BLOCK_RE.sub("", text)
    return text.replace("</head>", CSS + "\n</head>", 1)


def main():
    n = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</head>" not in old:
            continue
        new = apply(old)
        if new != old:
            f.write_text(new, encoding="utf-8")
            n += 1
    print(f"academy type scale: {n} page(s) updated")


if __name__ == "__main__":
    main()
