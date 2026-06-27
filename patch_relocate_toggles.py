#!/usr/bin/env python3
"""
patch_relocate_toggles.py — williamriveromd.com

Site-wide convention change: move the language toggle (Lang: EN TL CEB KAP)
INTO the top site-header, between the brand link and the ← All Guides link;
move the Dark/Desktop toggles OUT of the lang bar and into a single floating
circular widget pinned to bottom-right (the iso-uf-sodium-uf-ramping pattern).

For every guide that still uses the old `<div class="guide-lang-bar">`
strip pattern:

  1. Inject a `<div class="header-lang">…</div>` block into the existing
     <header class="site-header"> immediately after the .brand link.
     The block contains the same 4 lang chips (EN/TL/CEB/KAP), with the
     same ids (glb-en/tl/ceb/kap) and the same setGuideLang() onclick,
     so the existing JS keeps working.
  2. Delete the entire `<div class="guide-lang-bar">…</div>` block.
  3. Insert a `<div class="float-controls no-print">` widget just before
     `</body>` that holds the Dark toggle (and Desktop toggle if present).
     The buttons retain id="darkToggle"/"desktopToggle" so toggleDark()/
     toggleDesktop() in the page's existing JS keeps working.
  4. Update toggleDark()/toggleDesktop() in the page's JS so they no longer
     wipe the icon by overwriting textContent — instead they switch icon
     SVG + the floating tooltip text via class flip + title attribute.

The change is idempotent: a guide that already has `<div class="header-lang">`
in its header is skipped (already migrated). Single-tab guides that never
had a lang bar to begin with are also skipped — they get the float widget
via patch_master_css.py / their own bespoke markup.

Usage:
    python3 patch_relocate_toggles.py                # apply to all guides
    python3 patch_relocate_toggles.py --dry-run      # preview
    python3 patch_relocate_toggles.py --guide understanding-ckd.html
"""

import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDES = ROOT / "guides"

# ── HTML SNIPPETS ───────────────────────────────────────────────────────────
HEADER_LANG = (
    '<div class="header-lang">'
    '<span class="lang-lbl">Lang:</span>'
    '<button class="lang-btn-g active" id="glb-en" onclick="setGuideLang(\'en\')">EN</button>'
    '<button class="lang-btn-g" id="glb-tl" onclick="setGuideLang(\'tl\')">TL</button>'
    '<button class="lang-btn-g" id="glb-ceb" onclick="setGuideLang(\'ceb\')">CEB</button>'
    '<button class="lang-btn-g" id="glb-kap" onclick="setGuideLang(\'kap\')">KAP</button>'
    '</div>'
)

FLOAT_DARK_ONLY = (
    '<!-- Floating dark-mode toggle (relocated from the lang-bar strip) -->\n'
    '<div class="float-controls no-print">\n'
    '  <button id="darkToggle" class="float-btn" type="button" onclick="toggleDark()" aria-label="Toggle dark mode" title="Switch to dark mode">\n'
    '    <span class="float-tooltip" id="darkLabel">Dark mode</span>\n'
    '    <svg id="darkIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>\n'
    '  </button>\n'
    '</div>\n'
)

FLOAT_DARK_AND_DESKTOP = (
    '<!-- Floating dark + desktop toggles (relocated from the lang-bar strip) -->\n'
    '<div class="float-controls no-print">\n'
    '  <button id="desktopToggle" class="float-btn" type="button" onclick="toggleDesktop()" aria-label="Toggle desktop/mobile view" title="Force desktop view">\n'
    '    <span class="float-tooltip" id="desktopLabel">Desktop</span>\n'
    '    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>\n'
    '  </button>\n'
    '  <button id="darkToggle" class="float-btn" type="button" onclick="toggleDark()" aria-label="Toggle dark mode" title="Switch to dark mode">\n'
    '    <span class="float-tooltip" id="darkLabel">Dark mode</span>\n'
    '    <svg id="darkIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>\n'
    '  </button>\n'
    '</div>\n'
)

# ── PATTERNS ────────────────────────────────────────────────────────────────
LANG_BAR_RE = re.compile(
    r'\s*<div class="guide-lang-bar">.*?</div>\s*\n',
    re.S
)

HEADER_RE = re.compile(
    r'(<header class="site-header">\s*'
    r'<a [^>]*class="brand"[^>]*>.*?</a>)',
    re.S
)

# The desktop toggle is optional — detect its presence by id="desktopToggle"
# inside the (now-deleted) lang bar.


def patch_guide(path: Path, dry_run: bool = False) -> str:
    """Returns a status string: 'migrated', 'already', 'skip-no-bar'."""
    html = path.read_text(encoding="utf-8")

    # Already migrated?
    if 'class="header-lang"' in html:
        return "already"

    # No lang bar to migrate? (e.g. single-tab guides like iso-uf already
    # had the float widget added manually — those carry no .guide-lang-bar).
    has_lang_bar = '<div class="guide-lang-bar">' in html
    has_float = '<div class="float-controls' in html
    if not has_lang_bar:
        # Single-tab guides without a lang bar: ensure they at least have
        # the float widget — but most already do; if not, this script can't
        # safely add it without knowing whether toggleDark() etc. exists.
        return "skip-no-bar"

    # Detect desktop toggle in the lang bar
    bar_match = LANG_BAR_RE.search(html)
    if not bar_match:
        return "skip-no-bar"
    has_desktop = 'id="desktopToggle"' in bar_match.group(0)

    # 1) Inject .header-lang into the site-header (after the brand link)
    if not HEADER_RE.search(html):
        return "skip-no-header"
    html = HEADER_RE.sub(r'\1' + HEADER_LANG, html, count=1)

    # 2) Delete the lang bar block
    html = LANG_BAR_RE.sub('\n', html, count=1)

    # 3) Insert the float-controls widget just before </body>.
    # Use the LAST </body> in the file (some popup JS strings may embed
    # `</body></html>` literals — those come earlier; the last one is the
    # real closer).
    float_block = FLOAT_DARK_AND_DESKTOP if has_desktop else FLOAT_DARK_ONLY
    last_body_close = html.rfind('</body>')
    if last_body_close == -1:
        return "skip-no-body-close"
    html = html[:last_body_close] + float_block + html[last_body_close:]

    # 4) Fix toggleDark() so it doesn't wipe the SVG icon (the old version
    # often does `el.textContent = on ? 'Light' : 'Dark'` which removes the
    # SVG). Replace any such textContent assignment with a label-text
    # assignment that keeps the SVG intact. We target the function body
    # gently so guides whose toggleDark already updates a separate <span>
    # are unaffected.
    # If the page's toggleDark wipes the wrapping button's text, swap to
    # updating only the .float-tooltip span (id="darkLabel" we set above).
    html = re.sub(
        r"(toggleDark\(\)\s*\{[^}]*?)\bdarkToggle\b\.textContent\s*=\s*on\s*\?\s*'Light'\s*:\s*'Dark';?",
        r"\1document.getElementById('darkLabel').textContent = on ? 'Light mode' : 'Dark mode';\n  document.getElementById('darkToggle').title = on ? 'Switch to light mode' : 'Switch to dark mode';",
        html,
        flags=re.S,
    )

    if not dry_run:
        path.write_text(html, encoding="utf-8")
    return "migrated"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="Single guide filename to patch")
    args = ap.parse_args()

    if args.guide:
        targets = [GUIDES / args.guide]
    else:
        targets = sorted(GUIDES.glob("*.html"))

    counts = {"migrated": 0, "already": 0, "skip-no-bar": 0,
              "skip-no-header": 0, "skip-no-body-close": 0}
    for p in targets:
        status = patch_guide(p, dry_run=args.dry_run)
        counts[status] = counts.get(status, 0) + 1
        if status == "migrated":
            print(f"  ✓ {p.name}")
        elif status not in ("already", "skip-no-bar"):
            print(f"  ! {p.name}: {status}")

    verb = "Would migrate" if args.dry_run else "Migrated"
    print(f"\n{verb}: {counts.get('migrated', 0)}  "
          f"Already: {counts.get('already', 0)}  "
          f"No lang bar (skip): {counts.get('skip-no-bar', 0)}  "
          f"Issues: {counts.get('skip-no-header', 0) + counts.get('skip-no-body-close', 0)}")


if __name__ == "__main__":
    main()
