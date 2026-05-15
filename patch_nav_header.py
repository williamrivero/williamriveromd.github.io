#!/usr/bin/env python3
"""
patch_nav_header.py
Standardizes the top nav bar (site-header / guide-lang-bar / guide-toggle-bar)
across all guide HTML files.

Usage:
  python3 patch_nav_header.py              # patch all guides
  python3 patch_nav_header.py --dry-run    # preview without writing
  python3 patch_nav_header.py --guide anemia-management.html
"""

import os, re, sys, argparse

GUIDES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guides')

# These files have intentionally different or non-standard nav structures.
SKIP = {
    'index.html',
    'symptom-checker.html',
    'alcohol-drinking-log.html',   # printable form, no standard nav
    'lab-interpreter.html',         # complex interactive tool, custom header
    'kidney-physiology.html',       # WebGL interactive guide, custom nav
}

CANONICAL_BLOCK = '''\

<header class="site-header">
  <a href="https://williamriveromd.com" class="brand">W. G. M. <strong>Rivero</strong>, MD</a>
  <a href="https://williamriveromd.com/guides/index.html" class="back">← All Guides</a>
</header>
<div class="guide-lang-bar">
  <span class="lang-lbl">Lang:</span>
  <button class="lang-btn-g active" id="glb-en" onclick="setGuideLang('en')">EN</button>
  <button class="lang-btn-g" id="glb-tl" onclick="setGuideLang('tl')">TL</button>
  <button class="lang-btn-g" id="glb-ceb" onclick="setGuideLang('ceb')">CEB</button>
  <button class="lang-btn-g" id="glb-kap" onclick="setGuideLang('kap')">KAP</button>
</div>
<div class="guide-toggle-bar">
  <button class="toggle-btn" id="darkToggle" onclick="toggleDark()">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" id="darkIcon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    <span id="darkLabel">Dark</span>
  </button>
  <button class="toggle-btn" id="desktopToggle" onclick="toggleDesktop()">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
    <span id="desktopLabel">Desktop</span>
  </button>
</div>

'''

# Ordered list — first match wins as the "end of nav block" anchor.
END_ANCHOR_PATTERNS = [
    re.compile(r'<div\s+class="audience-tabs"', re.IGNORECASE),
    re.compile(r'<section\b[^>]*\bclass="hero"', re.IGNORECASE),
    re.compile(r'<div\b[^>]*\bclass="hero"', re.IGNORECASE),
    re.compile(r'<main\b', re.IGNORECASE),
    re.compile(r'<section\b[^>]*\bclass="section"', re.IGNORECASE),
]


def is_canonical(block):
    """True when the nav block already matches the canonical structure exactly."""
    # Header tag must have class="site-header" and NO inline style= attribute.
    hm = re.search(r'<header([^>]*)>', block)
    if not hm:
        return False
    hattrs = hm.group(1)
    if 'class="site-header"' not in hattrs or 'style=' in hattrs:
        return False
    # Must contain .brand and .back anchor links.
    if 'class="brand"' not in block or 'class="back"' not in block:
        return False
    # Must have guide-lang-bar that appears BEFORE guide-toggle-bar.
    lang_idx   = block.find('<div class="guide-lang-bar">')
    toggle_idx = block.find('<div class="guide-toggle-bar">')
    if lang_idx < 0 or toggle_idx < 0 or lang_idx >= toggle_idx:
        return False
    # KAP button must use class="lang-btn-g" (not the old "lang-btn").
    # Match the full opening tag so we don't bleed class names from adjacent buttons.
    kap_tag = re.search(r'<button([^>]*id="glb-kap"[^>]*)>', block)
    if not kap_tag:
        kap_tag = re.search(r'<button([^>]*)id="glb-kap"([^>]*)>', block)
    if not kap_tag:
        return False
    full_tag = kap_tag.group(0)
    if 'lang-btn-g' not in full_tag:
        return False
    return True


def find_end_anchor(html, start):
    """Return the position of the nearest end-anchor pattern after `start`."""
    best = None
    for pat in END_ANCHOR_PATTERNS:
        m = pat.search(html, start)
        if m and (best is None or m.start() < best):
            best = m.start()
    return best


def fix_guide(path, dry_run=False):
    fname = os.path.basename(path)

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # ── Locate <body> ──────────────────────────────────────────────────────────
    body_m = re.search(r'<body[^>]*>', html)
    if not body_m:
        return 'error', 'no <body> tag found'
    body_end = body_m.end()

    # ── Locate first <header after <body> ─────────────────────────────────────
    header_m = re.search(r'<header\b', html[body_end:])
    if not header_m:
        return 'error', 'no <header> tag after <body>'
    header_start = body_end + header_m.start()

    # ── Locate end anchor (first element that follows the nav block) ──────────
    end_pos = find_end_anchor(html, header_start)
    if end_pos is None:
        return 'error', 'could not find end anchor (hero/main/audience-tabs)'

    nav_block = html[header_start:end_pos]

    # ── Already canonical? ─────────────────────────────────────────────────────
    if is_canonical(nav_block):
        return 'ok', None

    # ── Replace nav block with canonical ──────────────────────────────────────
    new_html = html[:body_end] + CANONICAL_BLOCK + html[end_pos:]

    if new_html == original:
        return 'ok', None

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
    return 'updated', None


def main():
    parser = argparse.ArgumentParser(description='Standardize guide nav bars')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing files')
    parser.add_argument('--guide', metavar='FILENAME',
                        help='Process a single guide (filename only, not path)')
    args = parser.parse_args()

    if args.guide:
        targets = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        targets = sorted(
            os.path.join(GUIDES_DIR, f)
            for f in os.listdir(GUIDES_DIR)
            if f.endswith('.html') and f not in SKIP
        )

    updated, skipped, errors = [], [], []

    for path in targets:
        status, msg = fix_guide(path, dry_run=args.dry_run)
        fname = os.path.basename(path)
        if status == 'updated':
            updated.append(fname)
        elif status == 'ok':
            skipped.append(fname)
        else:
            errors.append((fname, msg))

    prefix = '[DRY RUN] ' if args.dry_run else ''
    print(f'\n{prefix}Nav header patch results:')
    print(f'  Updated : {len(updated)}')
    for f in updated:
        print(f'    {f}')
    print(f'  Already correct : {len(skipped)}')
    if errors:
        print(f'  Errors  : {len(errors)}')
        for f, e in errors:
            print(f'    {f}: {e}')


if __name__ == '__main__':
    main()
