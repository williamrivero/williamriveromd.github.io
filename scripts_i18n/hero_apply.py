import json, sys
trans=json.load(open('scratch_i18n/hero_titles.trans.json',encoding='utf-8'))
applied=0; errs=[]
for it in trans:
    f='guides/'+it['file']; html=open(f,encoding='utf-8').read()
    en=it['en_inner']
    target=en+'</h1>'
    if html.count(target)!=1:
        errs.append(f"{it['file']}: target count={html.count(target)} (need exactly 1)"); continue
    spans=('<span data-lang="en">'+en+'</span>'
           +'<span data-lang="tl" class="lang-hidden">'+it['tl']+'</span>'
           +'<span data-lang="ceb" class="lang-hidden">'+it['ceb']+'</span>'
           +'<span data-lang="kap" class="lang-hidden">'+it['kap']+'</span>')
    html=html.replace(target, spans+'</h1>',1)
    open(f,'w',encoding='utf-8').write(html); applied+=1
print("applied:",applied)
for e in errs: print("  ERR",e)
