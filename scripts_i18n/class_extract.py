#!/usr/bin/env python3
"""Extract class-scheme (lang-en/lang-tl/...) gaps from a guide.

For each patient-facing element with class="lang-en" that is missing one or more
of its lang-tl/lang-ceb/lang-kap siblings, capture the exact raw sibling group
and the missing languages. Output JSON job on stdout.
"""
import json, re, sys
from bs4 import BeautifulSoup

def raw_spans(html):
    out=[]; i=0
    opn=re.compile(r'<span\b([^>]*)>'); tok=re.compile(r'<span\b[^>]*>|</span>')
    while True:
        m=opn.search(html,i)
        if not m: break
        s=m.start(); attrs=m.group(1)
        if attrs.rstrip().endswith('/'): i=m.end(); continue
        depth=1; j=m.end()
        while depth>0:
            t=tok.search(html,j)
            if not t: j=len(html); break
            if t.group(0).startswith('</'):
                depth-=1; j=t.end()
                if depth==0: out.append((s,j,attrs,html[m.end():t.start()]))
            else: depth+=1; j=t.end()
        i=m.end()
    return out

def norm(s): return ' '.join(re.sub(r'<[^>]+>',' ',s).split())

def main():
    f=sys.argv[1]
    html=open(f,encoding='utf-8').read()
    soup=BeautifulSoup(html,'lxml')
    # targets: patient-facing lang-en elements missing siblings
    targets=[]
    for el in soup.find_all(class_='lang-en'):
        if any({'mode-physician','physician-mode'}&set(a.get('class')or[]) for a in el.parents): continue
        have={c for s in el.parent.find_all(recursive=False) for c in (s.get('class')or []) if c in ('lang-tl','lang-ceb','lang-kap')}
        miss=[l.split('-')[1] for l in ('lang-tl','lang-ceb','lang-kap') if l not in have]
        if miss and el.name=='span':
            targets.append((norm(el.decode_contents()), miss))
    # raw index of lang-en spans
    raw=[(s,e,a,inner) for (s,e,a,inner) in raw_spans(html) if 'lang-en' in a]
    idx={}
    for (s,e,a,inner) in raw:
        # capture group: extend over following lang-(tl|ceb|kap) spans
        grp_end=e
        m=re.compile(r'\s*<span\b[^>]*\blang-(tl|ceb|kap)\b[^>]*>').match(html,grp_end)
        while m:
            # find close of this sibling span (depth-aware)
            depth=1; j=m.end(); tok=re.compile(r'<span\b[^>]*>|</span>')
            while depth>0:
                t=tok.search(html,j)
                if not t: break
                if t.group(0).startswith('</'): depth-=1; j=t.end()
                else: depth+=1; j=t.end()
            grp_end=j
            m=re.compile(r'\s*<span\b[^>]*\blang-(tl|ceb|kap)\b[^>]*>').match(html,grp_end)
        idx.setdefault(norm(inner),[]).append((inner, html[s:grp_end]))
    job=[]; used={}
    for i,(t,miss) in enumerate(targets):
        cands=idx.get(t)
        if not cands:
            print(f"WARN no raw match: {t[:60]}",file=sys.stderr); continue
        k=used.get(t,0); inner,group=cands[k] if k<len(cands) else cands[-1]; used[t]=k+1
        job.append({'id':f's{i}','en_inner':inner,'missing':miss,'group_outer':group,'preview':t[:90]})
    json.dump(job,sys.stdout,ensure_ascii=False,indent=1)

if __name__=='__main__': main()
