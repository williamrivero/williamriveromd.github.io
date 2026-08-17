#!/usr/bin/env python3
"""Scheme-aware translation audit for patient-facing guides.

Handles BOTH translation schemes used on the site:
  * data-lang scheme:  <span data-lang="en">…</span> + tl/ceb/kap siblings
  * class scheme:      <span class="lang-en">…</span> + lang-tl/ceb/kap siblings

Detects three problems, patient-facing content only (clinician mode-physician
blocks are English-only by policy and skipped):
  A. data-lang structural gap  (an en element missing a tl/ceb/kap sibling)
  B. class structural gap       (a lang-en element missing a lang-xx sibling)
  C. bare body                  (a patient body text block in NEITHER scheme)

Calculators/tools are English-only by policy and excluded from the "needs
translation" verdict, but still listed for completeness.
"""
import glob, re, sys
from bs4 import BeautifulSoup

EXCLUDE_EXACT = {
    'guides/index.html','guides/calculators.html',
    'guides/nephrology-atlas.html','guides/kidney-physiology.html',
    'guides/ckd-dri-calculator.html',
    'guides/bp-log-blank.html','guides/bp-monitoring-log.html','guides/alcohol-drinking-log.html',
    'guides/ckd-recipe-analyzer.html','guides/nephrologist-interpreter.html',
    'guides/dyslipidemia-management-tool.html',
}
BLOCK_TAGS={'p','h1','h2','h3','h4','h5','li','td','th','dd','blockquote','figcaption','caption'}

def anc_has(el, pred):
    for a in el.parents:
        if pred(a): return True
    return False

def in_physician(el):
    return anc_has(el, lambda a: bool({'mode-physician','physician-mode'} & set(a.get('class') or [])))

def in_chrome(el):
    def pred(a):
        if a.name in ('header','footer','nav'): return True
        return bool(set(a.get('class') or []) & {
            'site-header','header-nav','nav-strip','guide-footer','dr-card','dr-card-wrap',
            'related-guides','hero-meta','float-controls','ref-acc','glossary-acc','ref-section'})
    return anc_has(el, pred)

def classify(html, f):
    if 'calc-' in f or f in EXCLUDE_EXACT: return 'tool'
    bc = (re.search(r'<body([^>]*)>', html) or re.match('','')).group(1) if re.search(r'<body([^>]*)>',html) else ''
    if 'physician-mode' in bc and 'single-mode' in bc: return 'clinician-only'
    if 'id="tab-pt"' in html: return 'patient-dual'
    return 'patient-single'

def lang_of(el):
    if el.get('data-lang'): return ('data', el.get('data-lang'))
    for c in (el.get('class') or []):
        if c in ('lang-en','lang-tl','lang-ceb','lang-kap'): return ('class', c.split('-')[1])
    return None

def sibling_langs(el, scheme):
    langs=set()
    for s in el.parent.find_all(recursive=False):
        l=lang_of(s)
        if l and l[0]==scheme: langs.add(l[1])
    return langs

def analyze(f):
    html=open(f,encoding='utf-8').read()
    kind=classify(html,f)
    soup=BeautifulSoup(html,'lxml')
    dgap={'tl':0,'ceb':0,'kap':0}; cgap={'tl':0,'ceb':0,'kap':0}
    # A. data-lang gaps
    for el in soup.find_all(attrs={'data-lang':'en'}):
        if in_physician(el): continue
        have=sibling_langs(el,'data')
        for l in ('tl','ceb','kap'):
            if l not in have: dgap[l]+=1
    # B. class gaps
    for el in soup.find_all(class_='lang-en'):
        if in_physician(el): continue
        have=sibling_langs(el,'class')
        for l in ('tl','ceb','kap'):
            if l not in have: cgap[l]+=1
    # C. bare body blocks (patient-facing leaf text not in any scheme)
    bare=0; bare_samples=[]
    for el in soup.find_all(BLOCK_TAGS):
        if in_physician(el) or in_chrome(el): continue
        if any(getattr(d,'name',None) in BLOCK_TAGS for d in el.descendants): continue  # not leaf
        txt=el.get_text(' ',strip=True)
        if len(txt)<4 or not re.search(r'[A-Za-z]{3}',txt): continue
        # in a scheme if self/ancestor/descendant carries data-lang or lang-xx
        def has_scheme(x):
            if x.get('data-lang'): return True
            if set(x.get('class') or []) & {'lang-en','lang-tl','lang-ceb','lang-kap'}: return True
            return False
        covered = has_scheme(el) or anc_has(el,has_scheme) or any(
            has_scheme(d) for d in el.descendants if getattr(d,'name',None))
        if not covered:
            bare+=1
            if len(bare_samples)<3: bare_samples.append(txt[:70])
    return kind, dgap, cgap, bare, bare_samples

def main():
    only=sys.argv[1:]
    rows=[]
    for f in sorted(glob.glob('guides/*.html')):
        if only and not any(o in f for o in only): continue
        rows.append((f,)+analyze(f))
    need=[]
    print(f"{'guide':46}{'kind':15}{'dGap':>6}{'cGap':>6}{'bareBody':>9}")
    for f,kind,dg,cg,bare,samp in rows:
        d=sum(dg.values()); c=sum(cg.values())
        problem = (kind.startswith('patient')) and (d>0 or c>0 or bare>0)
        if problem or d>0 or c>0 or bare>0:
            mark=' <== NEEDS TRANSLATION' if problem else ''
            print(f"{f:46}{kind:15}{d:>6}{c:>6}{bare:>9}{mark}")
            if problem:
                need.append((f,kind,dg,cg,bare,samp))
    from collections import Counter
    print("\nClasses:", dict(Counter(r[1] for r in rows)))
    if need:
        print(f"\n*** {len(need)} PATIENT guide(s) need translation work: ***")
        for f,kind,dg,cg,bare,samp in need:
            det=[]
            if sum(dg.values()): det.append(f"data-lang gaps tl/ceb/kap={dg['tl']}/{dg['ceb']}/{dg['kap']}")
            if sum(cg.values()): det.append(f"class gaps tl/ceb/kap={cg['tl']}/{cg['ceb']}/{cg['kap']}")
            if bare: det.append(f"bare-English body blocks={bare} (e.g. {samp[0]!r})")
            print(f"  {f}  [{kind}]\n      " + "\n      ".join(det))
    else:
        print("\nNo patient-facing translation gaps found.")

if __name__=='__main__':
    main()
