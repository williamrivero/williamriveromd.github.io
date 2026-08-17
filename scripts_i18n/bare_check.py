#!/usr/bin/env python3
"""Report bare (untranslated) patient PROSE blocks in a guide — the completion
gate for translation. Excludes content that is acceptably English by policy:
clinician (mode-physician), chrome (header/nav/footer/dr-card/related/hero-meta),
References/Sources sections and citation lists, glossary headword <dt>, figure
captions, and the table-of-contents jump nav. Short scientific/label headings
(<=24 chars, no sentence punctuation) are reported separately as 'labels'.

Usage: python3 bare_check.py guides/<file>.html
Exit 0 if no real prose gaps (labels/references are fine); prints counts+samples.
"""
import re, sys
from bs4 import BeautifulSoup

PROSE={'p','h1','h2','h3','h4','li','blockquote'}
BLOCK={'p','h1','h2','h3','h4','li','td','th','dd','blockquote'}
CHROME={'site-header','header-nav','nav-strip','guide-footer','dr-card','dr-card-wrap',
        'related-guides','hero-meta','ref-acc','glossary-acc','ref-section','glossary-sec',
        'audience-tabs','toc','float-controls',
        # embedded interactive tools/calculators are English-only by policy
        'calc-wrap','calc','calculator','tool-wrap','symptom-checker'}

def inphys(el):
    # check the element itself AND its ancestors (a mode-physician class can sit
    # directly on the flagged element, not only on a parent)
    for a in [el] + list(el.parents):
        if {'mode-physician','physician-mode'} & set(a.get('class') or []):
            return True
    return False

def in_refs_section(el):
    sec=el.find_parent('section')
    while sec:
        sid=(sec.get('id') or '').lower()
        if 'ref' in sid or 'source' in sid or 'citation' in sid: return True
        h=sec.find(['h2','h3'])
        if h:
            ht=h.get_text(' ',strip=True).lower()
            if ht.startswith(('references','sources','mga sanggunian','mga tinubdan','reng reperensya')):
                return True
        sec=sec.find_parent('section')
    return False

def in_excl(el):
    for a in el.parents:
        if a.name in ('header','footer','nav'): return True
        if set(a.get('class')or[]) & CHROME: return True
        if a.name=='details': return True
    if el.find_parent('figcaption'): return True
    if in_refs_section(el): return True
    return False

def hs(x):
    return bool(x.get('data-lang')) or bool(set(x.get('class')or[])&{'lang-en','lang-tl','lang-ceb','lang-kap'})

def main():
    f=sys.argv[1]
    s=BeautifulSoup(open(f,encoding='utf-8').read(),'lxml')
    prose=[]; labels=[]
    for el in s.find_all(PROSE):
        if inphys(el) or in_excl(el): continue
        if any(getattr(d,'name',None) in BLOCK for d in el.descendants): continue
        t=el.get_text(' ',strip=True)
        if len(t)<8 or not re.search(r'[A-Za-z]{3}',t): continue
        # inline cross-reference navigation (e.g. "→ See also: …", "→ See full guide: …")
        if t.startswith('→') or re.match(r'(See also|See full guide)\b', t): continue
        # clinician-only footnotes (annotated with ⚕/⚕) are English by policy
        if t[:1] in ('⚕', '⚖', '⚕', '⚖'): continue
        # bare image filenames used as figure placeholders
        if re.fullmatch(r'[\w-]+\.(png|webp|jpg|jpeg|svg)', t): continue
        # citation/reference lines (Author AB et al. … Journal Year;vol)
        if re.search(r'\bet al\.', t) and re.search(r'\b(19|20)\d\d\b', t): continue
        if hs(el) or any(hs(a) for a in el.parents) or any(hs(d) for d in el.descendants if getattr(d,'name',None)):
            continue
        # classify: short label-like heading vs real prose
        if el.name in ('h2','h3','h4') and len(t)<=24 and not re.search(r'[.!?,:]', t):
            labels.append((el.name,t))
        else:
            prose.append((el.name,t[:80]))
    print(f"REAL-PROSE-GAPS: {len(prose)}   (acceptable labels: {len(labels)})")
    for b in prose[:12]: print("   PROSE", b)
    for b in labels[:6]: print("   label", b)
    sys.exit(1 if prose else 0)

if __name__=='__main__': main()
