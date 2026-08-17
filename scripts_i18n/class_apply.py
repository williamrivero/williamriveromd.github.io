#!/usr/bin/env python3
"""Apply class-scheme translations: insert missing lang-tl/lang-ceb/lang-kap
sibling spans after each group. Byte-exact anchor on group_outer.

Usage: python3 class_apply.py guides/<file>.html translated.json [--dry-run]
"""
import json, re, sys

def main():
    guide=sys.argv[1]; jf=sys.argv[2]; dry='--dry-run' in sys.argv
    html=open(guide,encoding='utf-8').read()
    items=json.load(open(jf,encoding='utf-8'))
    applied=0; errors=[]
    for it in items:
        miss=it['missing']
        for l in miss:
            if not it.get(l): errors.append(f"{it['id']}: missing {l}")
        if any(e.startswith(it['id']+':') for e in errors): continue
        sibs=''
        for l in ('tl','ceb','kap'):
            if l in miss:
                sibs+=f'<span class="lang-{l}" style="display:none;">{it[l]}</span>'
        anchor=it['group_outer']; first=next(l for l in ('tl','ceb','kap') if l in miss)
        start=0; pos=-1
        while True:
            p=html.find(anchor,start)
            if p==-1: break
            after=html[p+len(anchor):p+len(anchor)+60]
            if re.match(r'\s*<span\b[^>]*\blang-'+first+r'\b', after):
                start=p+len(anchor); continue
            pos=p; break
        if pos==-1:
            errors.append(f"{it['id']}: anchor not found: {it['preview'][:50]}"); continue
        at=pos+len(anchor); html=html[:at]+sibs+html[at:]; applied+=1
    if errors:
        print("ERRORS:"); [print("  "+e) for e in errors]
        sys.exit(1)
    if dry: print(f"[dry-run] would apply {applied} to {guide}")
    else: open(guide,'w',encoding='utf-8').write(html); print(f"applied {applied} to {guide}")

if __name__=='__main__': main()
