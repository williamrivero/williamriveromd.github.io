#!/usr/bin/env python3
"""
patch_nav_pills_toggle.py
=========================
Replaces the old three-bar header structure (guide-lang-bar + guide-toggle-bar
with Dark/Desktop buttons + separate audience-tabs) with the cleaner thyroid-ckd
nav-pill style: a single guide-toggle-bar containing Patient | Clinician pill
buttons on the left and LANG buttons on the right.

Affected guides: all guides that have <div class="audience-tabs"> in their HTML.

Usage:
    python3 patch_nav_pills_toggle.py              # patch all affected guides
    python3 patch_nav_pills_toggle.py --dry-run    # preview, no writes
    python3 patch_nav_pills_toggle.py --guide anemia-management.html
"""

import re, sys, os, argparse

GUIDES_DIR = os.path.join(os.path.dirname(__file__), 'guides')

NEW_TOGGLE_BAR = '''\
<div class="guide-toggle-bar">
  <div style="display:flex;align-items:center;gap:8px;">
    <button class="toggle-btn active" id="tab-pt" onclick="setMode('patient')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
      <span data-lang="en">Patient</span><span data-lang="tl" class="lang-hidden">Pasyente</span><span data-lang="ceb" class="lang-hidden">Pasyente</span><span data-lang="kap" class="lang-hidden">Pasyente</span>
    </button>
    <button class="toggle-btn" id="tab-md" onclick="setMode('physician')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a5 5 0 1 0 0 10A5 5 0 0 0 12 2z"/><path d="M12 14c-5 0-9 2.5-9 5v1h18v-1c0-2.5-4-5-9-5z"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="16" y1="11" x2="22" y2="11"/></svg>
      <span data-lang="en">Clinician</span><span data-lang="tl" class="lang-hidden">Klinisyan</span><span data-lang="ceb" class="lang-hidden">Klinisyan</span><span data-lang="kap" class="lang-hidden">Klinisyan</span>
    </button>
  </div>
  <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
    <span class="lang-label">LANG:</span>
    <button class="lang-btn active" id="glb-en" onclick="setLang(\'en\')">EN</button>
    <button class="lang-btn" id="glb-tl" onclick="setLang(\'tl\')">TL</button>
    <button class="lang-btn" id="glb-ceb" onclick="setLang(\'ceb\')">CEB</button>
    <button class="lang-btn" id="glb-kap" onclick="setLang(\'kap\')">KAP</button>
  </div>
</div>'''


def patch(html: str) -> tuple[str, list[str]]:
    """Return (patched_html, list_of_changes). Empty list = nothing to do."""
    changes = []

    # 1. Remove <div class="guide-lang-bar">...</div>
    #    This div contains only span + button elements (no nested divs), so the
    #    first </div> closes it.
    pat_lang_bar = re.compile(
        r'<div class="guide-lang-bar">.*?</div>\s*\n',
        re.DOTALL
    )
    m = pat_lang_bar.search(html)
    if m:
        html = pat_lang_bar.sub('', html, count=1)
        changes.append('removed guide-lang-bar')

    # 2. Replace <div class="guide-toggle-bar">...</div> (Dark+Desktop buttons)
    #    with the new combined Patient|Clinician + LANG toggle bar.
    #    The old toggle-bar has no nested divs, so first </div> closes it.
    pat_toggle = re.compile(
        r'<div class="guide-toggle-bar">.*?</div>',
        re.DOTALL
    )
    m = pat_toggle.search(html)
    if m:
        html = pat_toggle.sub(NEW_TOGGLE_BAR, html, count=1)
        changes.append('replaced guide-toggle-bar')
    else:
        # Some guides have the lang-bar removed (step 1 also stripped it) —
        # bail if we can't find the toggle-bar to replace.
        return html, changes

    # 3. Remove <div class="audience-tabs">...</div> (two-level close)
    pat_aud = re.compile(
        r'\s*<div class="audience-tabs">.*?</div>\s*</div>',
        re.DOTALL
    )
    m = pat_aud.search(html)
    if m:
        html = pat_aud.sub('', html, count=1)
        changes.append('removed audience-tabs')

    return html, changes


def process_file(path: str, dry_run: bool) -> bool:
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    # Quick pre-check
    if '<div class="audience-tabs">' not in original:
        return False

    patched, changes = patch(original)

    if not changes:
        return False

    if patched == original:
        return False

    fname = os.path.basename(path)
    print(f'  {fname}: {", ".join(changes)}')

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(patched)

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--guide', help='single guide filename, e.g. anemia-management.html')
    args = parser.parse_args()

    if args.guide:
        candidates = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        candidates = sorted(
            os.path.join(GUIDES_DIR, f)
            for f in os.listdir(GUIDES_DIR)
            if f.endswith('.html') and ' 2' not in f
        )

    mode = 'DRY RUN' if args.dry_run else 'PATCHING'
    print(f'\n{mode} — nav-pills toggle bar\n{"="*48}')
    patched_count = 0
    for path in candidates:
        if process_file(path, args.dry_run):
            patched_count += 1

    print(f'\n{"="*48}')
    print(f'{"Would patch" if args.dry_run else "Patched"}: {patched_count} files')


if __name__ == '__main__':
    main()
