#!/usr/bin/env python3
"""patch_calc_fab_links.py — Add "Back to Calculators" and "Related Guides"
floating action buttons to all guides/calc-*.html pages.

• Left side, above print button  (bottom:134px left:24px) → calculators.html
• Right side, above scroll-to-top (bottom:134px right:24px) → #related-guides
"""

import re, glob, os, sys

DRY_RUN = '--dry-run' in sys.argv
SINGLE  = next((a.replace('--guide','').strip() for a in sys.argv if a.startswith('--guide')), None)

# ── NEW CSS (injected right after the existing .print-btn block) ───────────
NEW_CSS = """
  /* ── CALC FAB LINKS ──────────────────────────────────────────────────────── */
  .calc-back-btn,
  .calc-rg-btn {
    position: fixed;
    width: 44px; height: 44px; border-radius: 50%;
    background: var(--navy); color: white;
    border: none; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 16px rgba(0,0,0,.25);
    transition: transform .2s, box-shadow .2s; z-index: 9997;
    text-decoration: none;
  }
  .calc-back-btn {
    bottom: 134px; left: 24px;
  }
  .calc-rg-btn {
    bottom: 134px; right: 24px;
  }
  .calc-back-btn:hover,
  .calc-rg-btn:hover {
    background: #162848; transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(0,0,0,.35);
  }
  .calc-back-btn svg,
  .calc-rg-btn svg { width: 18px; height: 18px; }
  .calc-back-btn .p-tip {
    position: absolute; left: 54px;
    background: rgba(31,56,100,.92); color: white;
    font-size: 12px; font-weight: 500; white-space: nowrap;
    padding: 5px 10px; border-radius: 6px;
    opacity: 0; pointer-events: none; transition: opacity .15s;
  }
  .calc-rg-btn .p-tip {
    position: absolute; right: 54px;
    background: rgba(31,56,100,.92); color: white;
    font-size: 12px; font-weight: 500; white-space: nowrap;
    padding: 5px 10px; border-radius: 6px;
    opacity: 0; pointer-events: none; transition: opacity .15s;
  }
  .calc-back-btn:hover .p-tip,
  .calc-rg-btn:hover .p-tip { opacity: 1; }
"""

# ── NEW HTML ─────────────────────────────────────────────────────────────────
BACK_BTN = """<a href="calculators.html" aria-label="Back to all calculators" class="calc-back-btn">
<span class="p-tip">All Calculators</span>
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">
<polyline points="15 18 9 12 15 6"></polyline>
</svg>
</a>"""

RG_BTN = """<a href="#related-guides" aria-label="Jump to related guides" class="calc-rg-btn">
<span class="p-tip">Related Guides</span>
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">
<polyline points="9 18 15 12 9 6"></polyline>
</svg>
</a>"""


def patch_file(path):
    html = open(path).read()

    # Skip already-patched files
    if 'calc-back-btn' in html:
        return False, 'already patched'

    # ── 1. Inject CSS after the last .print-btn rule ───────────────────────
    # Look for the end of the print-btn section (before scroll-top or SCROLL-TO-TOP comment)
    css_anchor = re.search(
        r'(\.print-btn:hover \.p-tip\s*\{\s*opacity:\s*1\s*;\s*\})',
        html
    )
    if not css_anchor:
        return False, 'CSS anchor not found'

    insert_after = css_anchor.end()
    html = html[:insert_after] + NEW_CSS + html[insert_after:]

    # ── 2. Inject HTML buttons right before <button class="print-btn" ─────
    #       fallback: before scroll-top-btn
    anchor = re.search(r'(<button[^>]+class="print-btn"[^>]*>)', html)
    if not anchor:
        anchor = re.search(r'(<button[^>]+class="scroll-top-btn"[^>]*>)', html)
    if not anchor:
        return False, 'no insertion anchor found'

    pos = anchor.start()
    html = html[:pos] + BACK_BTN + '\n' + RG_BTN + '\n' + html[pos:]

    # ── 3. Also hide the new buttons in @media print ───────────────────────
    html = html.replace(
        '.print-btn, .scroll-top-btn, .guide-footer',
        '.print-btn, .calc-back-btn, .calc-rg-btn, .scroll-top-btn, .guide-footer'
    )

    if DRY_RUN:
        print(f'  [DRY-RUN] would patch: {path}')
        return True, 'dry-run'

    open(path, 'w').write(html)
    return True, 'patched'


# ── Main ──────────────────────────────────────────────────────────────────────
if SINGLE:
    files = [f'guides/{SINGLE}' if not SINGLE.startswith('guides/') else SINGLE]
else:
    files = sorted(glob.glob('guides/calc-*.html'))

patched = skipped = errors = 0
for f in files:
    ok, msg = patch_file(f)
    if ok:
        patched += 1
        print(f'  ✓  {os.path.basename(f)}')
    else:
        skipped += 1
        print(f'  –  {os.path.basename(f)} ({msg})')

print(f'\nDone — patched: {patched}  skipped: {skipped}  errors: {errors}')
