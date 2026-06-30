#!/usr/bin/env python3
"""
validate_hero_grid.py — williamriveromd.com

Scan every guide for misplaced direct children of <div class="hero-grid">.

The grid's flex layout only fires when its direct children are the canonical
set: hero-copy / hero-cards / hero-figure / hero-toc. Any other element
(intro-callout, urgent-banner, translation-notice, stray h1/p, etc.) becomes
an extra grid column under `grid-template-columns: 1fr auto`, which starves
.hero-copy to near-zero width and balloons the hero height. See the
mass-fix commit on Jun 27 2026 (cardiovascular-death-dialysis, el-nino,
filipino-nephrologist, green-nephrology, leptospirosis, sodium-salt-reduction).

Usage:
    python3 validate_hero_grid.py             # report all guides with issues
    python3 validate_hero_grid.py --strict    # exit 1 if any issues found
"""
import re, sys
from pathlib import Path

VOIDS = {'br','hr','img','input','meta','link','source','area','base',
         'col','embed','param','track','wbr','use','path','line','rect',
         'circle','polyline','polygon','ellipse','stop'}
VALID = re.compile(r'\bhero-copy\b|\bhero-cards\b|\bhero-figure\b|\bhero-toc\b')

# Guides with an intentional non-canonical hero structure that renders fine.
SKIP_FILES = {
    # Full-width banner image wrapped in a plain <div> with inline margin-top
    # (not a circular vignette). copy is 446px in practice — render-verified OK.
    'living-with-dialysis.html',
}

def hero_children(h):
    m = re.search(r'<div class="hero-grid"[^>]*>', h)
    if not m: return None
    i = m.end(); depth = 1; out = []
    while i < len(h) and depth > 0:
        if h.startswith('<!--', i):
            j = h.find('-->', i); i = j+3 if j>=0 else len(h); continue
        if h[i] != '<': i += 1; continue
        if h[i+1:i+2] == '/':
            tm = re.match(r'</(\w+)>', h[i:])
            if tm: depth -= 1; i += len(tm.group(0)); continue
        tm = re.match(r'<(\w+)([^>]*)>', h[i:])
        if tm:
            tag = tm.group(1).lower(); attrs = tm.group(2)
            cm = re.search(r'class="([^"]*)"', attrs)
            cls = cm.group(1) if cm else ''
            if depth == 1 and tag not in VOIDS and not attrs.rstrip().endswith('/'):
                out.append((tag, cls))
            if tag not in VOIDS and not attrs.rstrip().endswith('/'):
                depth += 1
            i += len(tm.group(0)); continue
        i += 1
    return out

def figure_outside_grid(h):
    """Return True when a guide has <figure ... hero-figure ...> sitting
    AFTER its hero-grid's closing </div> instead of inside the grid.
    That breaks the layout: the disc falls below the copy column rather
    than into its grid slot."""
    m = re.search(r'<div class="hero-grid"[^>]*>', h)
    if not m: return False
    i = m.end(); depth = 1
    while i < len(h) and depth > 0:
        o = h.find('<div', i); c = h.find('</div>', i)
        if c == -1: return False
        if o != -1 and o < c: depth += 1; i = o + 4
        else: depth -= 1; close_at = c; i = c + 6
    body = h[m.end():close_at]
    if re.search(r'<figure[^>]+\bhero-figure\b', body): return False
    # No figure inside; check the next ~6000 chars after grid for a stray one
    return bool(re.search(r'<figure[^>]+\bhero-figure\b', h[close_at:close_at+6000]))


def main():
    strict = '--strict' in sys.argv
    issues = []
    outside = []
    for f in sorted(Path('guides').glob('*.html')):
        if f.name in SKIP_FILES: continue
        src = f.read_text(encoding='utf-8')
        kids = hero_children(src)
        if kids:
            bad = [(t,c) for (t,c) in kids if not VALID.search(c)]
            if bad: issues.append((f.name, bad))
        if figure_outside_grid(src):
            outside.append(f.name)
    ok = True
    if issues:
        ok = False
        print(f'⚠ {len(issues)} guide(s) with misplaced hero-grid children:')
        for name, bad in issues:
            print(f'  {name:48s} {bad}')
    if outside:
        ok = False
        print(f'\n⚠ {len(outside)} guide(s) with <figure class="hero-figure"> OUTSIDE the hero-grid')
        print('  (run `python3 fix_hero_figure_placement.py` to move them in):')
        for name in outside:
            print(f'  {name}')
    if ok:
        print('✓ All hero-grids have only valid direct children, and every hero-figure sits inside its grid.')
        return 0
    return 1 if strict else 0

if __name__ == '__main__':
    sys.exit(main())
