#!/usr/bin/env python3
"""make_calc_shell.py — scaffold a standalone calculator page from a source guide.

Usage:
    python3 make_calc_shell.py <source_guide.html> <dest_file.html>

Copies the source guide verbatim (so the master CSS and every working inline
<script> — setLang, dark/desktop toggles, and the calculator's own JS — come
along intact), then replaces the entire <main>…</main> body with a single
<!--CALC_MAIN--> marker for the author/agent to fill in with the MDCalc-style
standalone layout (When to Use · Calculator · Formula · Evidence · Pearls).

It also rewires the language buttons from the broken `setGuideLang(...)` to the
actually-defined `setLang(...)` so the lang toggle works on the new page.

This is a scaffolding helper, not an idempotent patch script — run it once per
new calculator page, then hand-edit the head metadata, nav pills, hero, the
<!--CALC_MAIN--> body, and the related-guides block.
"""
import re
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    if not src.exists():
        sys.exit(f"source not found: {src}")
    html = src.read_text(encoding="utf-8")

    # Collapse the whole <main>…</main> body to a single fill-in marker.
    new_main = '<main class="container">\n<!--CALC_MAIN-->\n</main>'
    html, n = re.subn(r"<main\b[^>]*>.*?</main>", new_main, html,
                      count=1, flags=re.DOTALL)
    if n != 1:
        sys.exit("could not find a <main>…</main> block to replace")

    # Wire language buttons to the function that actually exists.
    html = html.replace('onclick="setGuideLang(', 'onclick="setLang(')

    dest.write_text(html, encoding="utf-8")
    print(f"wrote {dest} (main replaced, lang buttons rewired)")


if __name__ == "__main__":
    main()
