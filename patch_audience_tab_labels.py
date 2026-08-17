#!/usr/bin/env python3
"""Normalize the patient/clinician audience-tab labels so both carry all four
data-lang spans (EN/TL/CEB/KAP).

The dual-mode toggle tabs ("Patients & Families" / "Clinicians") were shipped
either as bare text or as an English-only <span data-lang="en">…</span>, so the
labels stayed in English when a visitor picked Tagalog, Cebuano, or Kapampangan.
This patcher rewrites each tab button's inner content to the canonical
four-language span block. Idempotent: re-running produces the same output.

Usage:
  python3 patch_audience_tab_labels.py                 # all dual-mode guides
  python3 patch_audience_tab_labels.py --dry-run       # preview, no writes
  python3 patch_audience_tab_labels.py --guide igan-guide.html
"""
import argparse, glob, os, re, sys

PT = {
    'en':  'Patients &amp; Families',
    'tl':  'Mga Pasyente at Pamilya',
    'ceb': 'Mga Pasyente ug Pamilya',
    'kap': 'Reng Pasyente at Pamilya',
}
MD = {
    'en':  'Clinicians',
    'tl':  'Mga Kliniko',
    'ceb': 'Mga Kliniko',
    'kap': 'Reng Kliniko',
}

def build_inner(trans):
    parts = [f'<span data-lang="en">{trans["en"]}</span>']
    for l in ('tl', 'ceb', 'kap'):
        parts.append(f'<span data-lang="{l}" class="lang-hidden">{trans[l]}</span>')
    return ''.join(parts)

# Anchor on the stable id (id="tab-pt" / id="tab-md"); class varies across
# guides (aud-tab vs toggle-btn). INNER captured non-greedily.
RE_PT = re.compile(r'(<button [^>]*id="tab-pt"[^>]*>)(.*?)(</button>)', re.S)
RE_MD = re.compile(r'(<button [^>]*id="tab-md"[^>]*>)(.*?)(</button>)', re.S)

def patch_html(html):
    changed = False
    def repl(trans):
        inner = build_inner(trans)
        def _f(m):
            nonlocal changed
            new = m.group(1) + inner + m.group(3)
            if new != m.group(0):
                changed = True
            return new
        return _f
    html = RE_PT.sub(repl(PT), html, count=1)
    html = RE_MD.sub(repl(MD), html, count=1)
    return html, changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    args = ap.parse_args()

    if args.guide:
        files = [os.path.join('guides', os.path.basename(args.guide))]
    else:
        files = [f for f in sorted(glob.glob('guides/*.html')) if 'calc-' not in f]

    touched = 0
    for f in files:
        if not os.path.exists(f):
            print(f"skip (missing): {f}"); continue
        html = open(f, encoding='utf-8').read()
        if 'id="tab-pt"' not in html and 'id="tab-md"' not in html:
            continue  # not a dual-mode guide
        new, changed = patch_html(html)
        if changed:
            touched += 1
            if args.dry_run:
                print(f"would patch: {f}")
            else:
                open(f, 'w', encoding='utf-8').write(new)
                print(f"patched: {f}")
    print(f"\n{'Would patch' if args.dry_run else 'Patched'} {touched} guide(s).")

if __name__ == '__main__':
    main()
