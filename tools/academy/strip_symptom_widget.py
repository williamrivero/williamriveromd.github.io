"""No Symptom Checker on Renal Care Academy pages (Dr. Rivero, Nov 25 2026). Idempotent.

The floating Symptom Checker is a patient tool; the Academy is staff training. The course generators write
their pages into guides/, where the shared patch pipeline (patch_symptom_widget.py) adds the widget to every
narrative page; this strips the tag again after publish_academy.py moves the pages to academy/.

    python3 tools/academy/strip_symptom_widget.py
"""
import re
from pathlib import Path

ACADEMY = Path(__file__).resolve().parents[2] / "academy"
TAG_RE = re.compile(r'\n?[ \t]*<script[^>]*src="[^"]*symptom-checker-widget\.js"[^>]*></script>')


def main():
    n = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        new = TAG_RE.sub("", old)
        if new != old:
            f.write_text(new, encoding="utf-8")
            n += 1
    print(f"academy symptom checker: removed from {n} page(s)")


if __name__ == "__main__":
    main()
