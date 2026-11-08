#!/usr/bin/env python3
"""Audit the clinician "Evidence Snapshot" card (CLAUDE.md rule 7).

Checks every <div class="ov-card"> in guides/*.html:
  * at most 4 stat rows (.ov-stat)
  * each value (.v, unit span excluded) is at most 8 characters
  * each description (.l) is at most 100 characters
  * no <br> inside a value (values never wrap; put the unit in <span class="u">)
  * no guideline-name-only value (KDIGO, KDOQI, ADA, WHO ...) — those belong in
    the .ov-src source line, not in a .v

Usage:
  python3 audit_evidence_snapshot.py                 # whole library; exits 1 on any failure
  python3 audit_evidence_snapshot.py --guide f.html  # one guide
"""
import argparse, glob, html, os, re, sys

MAX_ROWS, MAX_V, MAX_L = 4, 8, 100
GUIDELINE = re.compile(r'^(KDIGO|KDOQI|ADA|WHO|AHA|ACC|ISRNM|IDSA|ISPD|ASAM|AAN|Banff|EuDial|PhilCAT|CombAT|MTOPS)\b')
STAT = re.compile(r'<div class="ov-stat">\s*<span class="v">((?:(?!</span><span class="l">).)*?)</span>\s*'
                  r'<span class="l">(.*?)</span>\s*</div>', re.S)

def text(x):
    return html.unescape(re.sub(r'<[^>]+>', '', x)).strip()

def audit(path):
    s = open(path, encoding='utf-8').read()
    problems = []
    for n, card in enumerate(re.findall(r'<div class="ov-card">(.*?)</aside>', s, re.S)):
        rows = STAT.findall(card)
        if len(rows) > MAX_ROWS:
            problems.append(f'card {n}: {len(rows)} rows (max {MAX_ROWS})')
        for v, l in rows:
            if re.search(r'<br\s*/?>', v):
                problems.append(f'card {n}: <br> in value {text(v)!r}')
            vv = text(re.sub(r'<span class="u">.*?</span>', '', v))
            if len(vv) > MAX_V:
                problems.append(f'card {n}: value too long {vv!r} ({len(vv)} > {MAX_V})')
            if GUIDELINE.match(vv):
                problems.append(f'card {n}: guideline name as value {vv!r} (use .ov-src)')
            ll = text(l)
            if len(ll) > MAX_L:
                problems.append(f'card {n}: description {len(ll)} chars (max {MAX_L}): {ll[:50]}…')
    return problems

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--guide')
    a = ap.parse_args()
    root = os.path.dirname(os.path.abspath(__file__))
    files = [os.path.join(root, 'guides', a.guide)] if a.guide else sorted(glob.glob(os.path.join(root, 'guides', '*.html')))
    bad = 0; cards = 0
    for f in files:
        cards += open(f, encoding='utf-8').read().count('<div class="ov-card">')
        p = audit(f)
        if p:
            bad += 1
            print(f'✗ {os.path.basename(f)}')
            for x in p: print('   ', x)
    print(f'\nEvidence Snapshot audit: {cards} card(s) checked, {bad} guide(s) with problems')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
