#!/usr/bin/env python3
"""Verify a translated guide against its pre-translation baseline.

Checks:
  1. ENGLISH PRESERVED — stripping every tl/ceb/kap element from the current
     file yields text identical to the baseline's English/neutral text (so no
     English was altered, dropped, or added).
  2. patient-missing — every patient-facing data-lang="en" element now has
     tl/ceb/kap siblings (0 = complete).

Usage:
  python3 verify_guide.py guides/<file>.html scratch_i18n/baseline/<file>.txt
  python3 snapshot: python3 verify_guide.py --snapshot guides/<file>.html scratch_i18n/baseline/<file>.txt
"""
import re, sys
from bs4 import BeautifulSoup

def neutral(path):
    s = BeautifulSoup(open(path, encoding='utf-8').read(), 'lxml')
    for e in s.find_all(attrs={'data-lang': lambda v: v in ('tl','ceb','kap')}):
        e.decompose()
    for e in s.find_all(class_=lambda c: c and set(c) & {'lang-tl','lang-ceb','lang-kap'}):
        e.decompose()
    # the top-nav language chips are chrome, not content; strip so a guide that
    # had chips added after baseline still compares equal
    for e in s.find_all(class_='header-lang'):
        e.decompose()
    return ' '.join(s.get_text(' ').split())

def patient_missing(path):
    s = BeautifulSoup(open(path, encoding='utf-8').read(), 'lxml')
    m = 0
    for el in s.find_all(attrs={'data-lang': 'en'}):
        if any({'mode-physician','physician-mode'} & set(a.get('class') or []) for a in el.parents):
            continue
        have = {x.get('data-lang') for x in el.parent.find_all(attrs={'data-lang': True}, recursive=False)}
        if not all(l in have for l in ('tl','ceb','kap')):
            m += 1
    return m

if __name__ == '__main__':
    if sys.argv[1] == '--snapshot':
        guide, base = sys.argv[2], sys.argv[3]
        open(base, 'w').write(neutral(guide))
        print(f"baseline snapshot: {base} ({len(open(base).read())} chars)")
    else:
        guide, base = sys.argv[1], sys.argv[2]
        a = open(base, encoding='utf-8').read()
        b = neutral(guide)
        ok = (a == b)
        print("ENGLISH PRESERVED" if ok else "ENGLISH CHANGED (FAIL)")
        if not ok:
            import difflib
            diff = [d for d in difflib.unified_diff(a.split(), b.split(), lineterm='')][:40]
            print('\n'.join(diff))
        print("patient-missing:", patient_missing(guide))
