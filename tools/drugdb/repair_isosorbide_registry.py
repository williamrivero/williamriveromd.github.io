"""Generate a narrowly scoped isosorbide migration proposal; never writes source."""
import argparse,copy,hashlib,json,re
from collections import Counter
from pathlib import Path
EXACT={'isosorbide mononitrate':('isosorbide-mononitrate','isosorbide mononitrate'),'isosorbide dinitrate':('isosorbide-dinitrate','isosorbide dinitrate')}
def normalized(text):return re.sub(r'\s+',' ',text.strip()).lower()
def derive(rows,ingredient):
    names=Counter(re.sub(r'\s+',' ',p['generic_name']).strip() for p in rows)
    cats=Counter(p['pharmacologic_category'].strip() for p in rows if p.get('pharmacologic_category'))
    ds=Counter(p.get('dispensing') for p in rows)
    return {'name':ingredient.capitalize(),'ingredients':[ingredient],'products':len(rows),'registered_names':[n for n,_ in names.most_common(5)],'categories':[c for c,_ in cats.most_common(3)],'rx':ds['Rx'],'otc':ds['OTC']+ds['HR'],'hr':ds['HR'],'dispensing':[d for d in ['Rx','OTC','HR'] if ds[d]],'vat_exempt':any(p.get('vat_exempt') for p in rows)}
def transform(rows,generics,aliases,additional,issues):
    orig=copy.deepcopy(rows);rows=copy.deepcopy(rows);g=copy.deepcopy(generics);a=copy.deepcopy(aliases);m=copy.deepcopy(additional);issues=copy.deepcopy(issues)
    targets=Counter();changed=[]
    for p in rows:
        if p.get('generic_slug')!='isosorbide':continue
        key=normalized(p.get('generic_name',''))
        if key not in EXACT:raise ValueError('Unrecognized mixed heading: '+p.get('generic_name',''))
        slug,ingredient=EXACT[key];p['generic_slug']=slug;p['ingredients']=[ingredient];targets[slug]+=1;changed.append(p['registration_number'])
    if targets!={'isosorbide-mononitrate':33,'isosorbide-dinitrate':26}:raise ValueError('Baseline differs; review exact names/counts: '+str(targets))
    for slug,ingredient in EXACT.values():
        if slug in generics:raise ValueError('Target already exists; review migration instead of replacing: '+slug)
        g[slug]=derive([p for p in rows if p['generic_slug']==slug],ingredient)
    # Keep the historical URL as an explicit disambiguation hub, not the bare chemical.
    g['isosorbide']={'name':'Isosorbide: choose the medicine','ingredients':[],'products':0,'registered_names':[],'categories':['Nitrate vasodilators'],'rx':0,'otc':0,'hr':0,'dispensing':[],'vat_exempt':False}
    a['isosorbide-mononitrate']={'main':'isosorbide-5-mononitrate','reason':'synonym','confidence':'high','note':'Exact mononitrate ingredient; distinct from isosorbide dinitrate. Raw registered names and product release forms retained.'}
    if 'isosorbide' in a:raise ValueError('Historical heading must not redirect to a single active')
    m['isosorbide']={'enabled':True,'kind':'registry_hub','name':g['isosorbide']['name'],'ingredients':[],'categories':['Nitrate vasodilators'],'source_url':'https://verification.fda.gov.ph','source_label':'FDA Philippines verification portal','reference_label':'Ingredient selection','heading':'Choose the exact ingredient','note':'Isosorbide mononitrate and isosorbide dinitrate have different doses and formulations. Open the ingredient shown on the product label, then check its strength, route and release formulation before prescribing.','targets':[{'slug':'isosorbide-5-mononitrate','label':'Isosorbide mononitrate (including 5-mononitrate)'},{'slug':'isosorbide-dinitrate','label':'Isosorbide dinitrate'}],'checked_date':'2026-11-25'}
    issues.setdefault('entries',{}).pop('isosorbide',None)
    assert len(rows)==len(orig)
    for before,after in zip(orig,rows):
        delta={k for k in set(before)|set(after) if before.get(k)!=after.get(k)}
        assert delta<= {'generic_slug','ingredients'}
        if before.get('generic_slug')!='isosorbide':assert before==after
    for key in generics:
        if key!='isosorbide':assert generics[key]==g[key]
    for key in aliases:assert aliases[key]==a[key]
    assert sum(v['products'] for v in g.values())==sum(v['products'] for v in generics.values())
    report={'changed_rows':len(changed),'new_counts':dict(targets),'preserved_row_fields':'all except generic_slug and ingredients','registration_numbers':changed,'canonical_mononitrate_products':33+generics['isosorbide-5-mononitrate']['products']+generics['isosorbide-mononitrte']['products'],'historical_hub_products':0,'vat_note':'Existing row VAT flags preserved; no fresh VAT eligibility verification or claim.'}
    return rows,g,a,m,issues,report

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,default=Path(__file__).resolve().parents[2]/'data/drugs');ap.add_argument('--out',type=Path,required=True);x=ap.parse_args()
    if x.source.resolve()==x.out.resolve() or x.source.resolve() in x.out.resolve().parents:raise ValueError('Output must be outside source')
    names=['registry/i.json','generics.json','aliases.json','additional_monographs.json','registry_issues.json'];docs=[json.loads((x.source/n).read_text()) for n in names]
    results=transform(*docs);x.out.mkdir(parents=True,exist_ok=True)
    for n,d in zip(names,results[:5]):p=x.out/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
    report=results[-1];report['source_sha256']={n:hashlib.sha256((x.source/n).read_bytes()).hexdigest()for n in names};(x.out/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['registration_numbers','source_sha256']},indent=2))
if __name__=='__main__':main()
