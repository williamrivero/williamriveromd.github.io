#!/usr/bin/env python3
"""Insert the standard top-nav language chips into patient guides that have
multilingual content but no switcher UI (so their translations are unreachable).

The chips call setGuideLang(...) which is now globally defined by
assets/clinician-lang-lock.js (loaded on every guide), so no inline setLang is
required. Chips are inserted immediately after the header brand link.

Only targets patient guides: skips calculators, printable logs, the
index/atlas/physiology/calculators special pages, and clinician-only guides
(physician-mode single-mode) which are English-only by policy. Also skips guides
with little/no translation content. Idempotent.

Usage:
  python3 patch_add_lang_switcher.py [--dry-run] [--guide <file>]
"""
import argparse, glob, os, re

CHIPS = ('<div class="header-lang"><span class="lang-lbl">Lang:</span>'
         '<button class="lang-btn-g active" id="glb-en" onclick="setGuideLang(\'en\')">EN</button>'
         '<button class="lang-btn-g" id="glb-tl" onclick="setGuideLang(\'tl\')">TL</button>'
         '<button class="lang-btn-g" id="glb-ceb" onclick="setGuideLang(\'ceb\')">CEB</button>'
         '<button class="lang-btn-g" id="glb-kap" onclick="setGuideLang(\'kap\')">KAP</button></div>')

SKIP_EXACT = {'guides/index.html','guides/calculators.html','guides/nephrology-atlas.html',
              'guides/kidney-physiology.html','guides/ckd-dri-calculator.html'}

def eligible(f, html):
    if 'calc-' in f or f in SKIP_EXACT: return False
    if 'id="glb-tl"' in html: return False               # already has chips
    b = re.search(r'<body([^>]*)>', html); bc = b.group(1) if b else ''
    if 'physician-mode' in bc and 'single-mode' in bc: return False  # clinician-only, English
    if 'class="brand"' not in html: return False
    # must actually carry translation content
    tl = html.count('data-lang="tl"') + html.count('class="lang-tl"')
    if tl < 4: return False
    return True

def patch(html):
    # insert chips right after the brand anchor's closing </a>
    m = re.search(r'(<a\b[^>]*class="brand"[^>]*>.*?</a>)', html, re.S)
    if not m: return html, False
    end = m.end()
    return html[:end] + CHIPS + html[end:], True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    a = ap.parse_args()
    files = [os.path.join('guides', os.path.basename(a.guide))] if a.guide else \
            [f for f in sorted(glob.glob('guides/*.html')) if 'calc-' not in f]
    n = 0
    for f in files:
        html = open(f, encoding='utf-8').read()
        if not eligible(f, html):
            if a.guide: print(f"skip (not eligible): {f}")
            continue
        new, ok = patch(html)
        if ok:
            n += 1
            if a.dry_run: print(f"would add chips: {f}")
            else: open(f, 'w', encoding='utf-8').write(new); print(f"added chips: {f}")
    print(f"\n{'Would add' if a.dry_run else 'Added'} chips to {n} guide(s).")

if __name__ == '__main__':
    main()
