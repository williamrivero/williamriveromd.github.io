#!/usr/bin/env python3
"""Refresh explicitly reviewed DailyMed SPL pins when openFDA lacks a full label.

Only named, formulation-checked US NDA/BLA labels are allowed. The required section
and identity checks fail closed; a failed refresh never replaces an existing file.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, re, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
import fetch_fda_labels as fda

ROOT=Path(__file__).resolve().parents[2]
NS={'h':'urn:hl7-org:v3'}
FIELDS={
 '34066-1':'boxed_warning','34067-9':'indications_and_usage',
 '34068-7':'dosage_and_administration','43678-2':'dosage_forms_and_strengths',
 '34070-3':'contraindications','43685-7':'warnings_and_cautions',
 '34071-1':'warnings_and_cautions','34073-7':'drug_interactions',
 '34084-4':'adverse_reactions','43684-0':'use_in_specific_populations',
 '42228-7':'pregnancy','34080-1':'lactation','34080-2':'lactation','77290-5':'lactation','34081-0':'pediatric_use',
 '34082-8':'geriatric_use','34088-5':'overdosage','43679-0':'mechanism_of_action',
 '43682-4':'pharmacokinetics','43681-6':'pharmacodynamics',
 '34090-1':'clinical_pharmacology','34072-9':'warnings_and_cautions','42232-9':'warnings_and_cautions',
}

def node_text(node):
    if node is None:return ''
    # Preserve paragraph/list boundaries, and table cell boundaries as plain text.
    def walk(e):
        out=[e.text or '']
        for c in e:
            out.append(walk(c));out.append(c.tail or '')
            tag=c.tag.rsplit('}',1)[-1]
            if tag in {'paragraph','item','tr','br','title'}:out.append('\n')
            elif tag in {'td','th'}:out.append(' | ')
        return ''.join(out)
    return '\n'.join(re.sub(r'[ \t]+',' ',v).strip() for v in walk(node).splitlines() if v.strip())

def parse_spl(raw,pin,g):
    root=ET.fromstring(raw)
    sid=root.find('h:setId',NS).get('root')
    if sid.lower()!=pin['set_id'].lower():raise ValueError('Unexpected SPL set ID')
    title=node_text(root.find('h:title',NS))
    text=node_text(root).lower()
    for required in pin['verify_text']:
        if required.lower() not in text:raise ValueError('SPL identity/form check failed: '+required)
    # A DailyMed listing alone is not proof of FDA approval.
    apps=[e.get('root','')+e.get('extension','') for e in root.findall('.//h:approval/h:id',NS)]
    if not any(pin['application'] in a for a in apps):raise ValueError('NDA/BLA check failed: '+str(apps))
    label={'set_id':sid,'id':root.find('h:id',NS).get('root'),
           'version':root.find('h:versionNumber',NS).get('value'),
           'effective_time':root.find('h:effectiveTime',NS).get('value'),
           'openfda':{'brand_name':[pin['brand']],'generic_name':[pin['generic']],
                      'substance_name':pin['substances'],'route':pin['routes'],
                      'manufacturer_name':[pin['manufacturer']],
                      'application_number':[pin['application']],
                      'product_type':[pin.get('product_type','HUMAN PRESCRIPTION DRUG')]}}
    for sec in root.findall('.//h:section',NS):
        code=sec.find('h:code',NS)
        key=FIELDS.get(code.get('code','')) if code is not None else None
        if not key:continue
        body=node_text(sec.find('h:text',NS))
        # Parent text is often absent: retain complete nested subsections.
        def child_parts(parent):
            for sub in parent.findall('h:component/h:section',NS):
                yield node_text(sub.find('h:title',NS))
                yield node_text(sub.find('h:text',NS))
                yield from child_parts(sub)
        body='\n\n'.join(p for p in [body,*child_parts(sec)] if p)
        previous=fda.join_text(label.get(key))
        if body and body not in previous:
            # Retain distinct legacy WARNINGS and PRECAUTIONS; discard only
            # truly contained highlight/child copies, never by length alone.
            label[key]=[body if previous in body else previous+'\n\n'+body]
    for key in ['indications_and_usage','dosage_and_administration','warnings_and_cautions','contraindications']:
        if len(fda.join_text(label.get(key))) < (60 if key in {'indications_and_usage','dosage_and_administration'} else 1):raise ValueError('Incomplete prescribing section: '+key)
    rec=fda.build_record(pin['slug'],g,label,1,'reviewed-dailymed-pin',match='verified-spl-pin')
    rec['source'].update(via='DailyMed Structured Product Label (SPL)',
                         spl_url=f"https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{sid}.xml")
    rec['selection'].update(confidence='high',identity_note=pin['reason'],spl_sha256=hashlib.sha256(raw).hexdigest())
    return rec

def reconcile_changes(doc, old, rec):
    """Make the review manifest describe the final pinned record, not a transient openFDA result."""
    slug=rec['slug']
    prior={key:next((e for e in doc.get(key,[]) if e.get('slug')==slug),None)
           for key in ('added','changed','removed')}
    if old == rec and not any(prior.values()):return
    entry={'slug':slug,'name':rec['name'],
           **{key:rec['label'].get(key) for key in
              ('brand_name','application_number','set_id','effective_time')},
           'dailymed_url':rec['source']['dailymed_url']}
    previous=((prior['changed'] or prior['removed'] or {}).get('previous')
              or ({key:old['label'].get(key) for key in ('set_id','effective_time')}
                  if old else None))
    for key in ('added','changed','removed'):
        doc[key]=[e for e in doc.get(key,[]) if e.get('slug')!=slug]
    if prior['added'] or previous is None:
        doc['added'].append(entry)
    elif (prior['removed'] or prior['changed']) and all(
            previous.get(key)==rec['label'].get(key) for key in ('set_id','effective_time')):
        # openFDA removed/replaced a pin and the pin restored its original label.
        return
    else:
        entry['previous']=previous
        doc['changed'].append(entry)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--only',nargs='*');ap.add_argument('--cache-dir',type=Path)
    a=ap.parse_args()
    pins=json.loads((Path(__file__).with_name('dailymed_pins.json')).read_text())['pins']
    generics=json.loads((ROOT/'data/drugs/generics.json').read_text())
    changes_path=ROOT/'data/drugs/labels/_changes.json'
    changes=json.loads(changes_path.read_text()) if changes_path.exists() else {
        'note':'US FDA label changes, including reviewed DailyMed pins.',
        'source':'reviewed-dailymed-pins','added':[],'changed':[],'removed':[]}
    before_changes=json.dumps(changes,sort_keys=True)
    restored=[]
    for pin in pins:
        if a.only and pin['slug'] not in a.only:continue
        url=f"https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{pin['set_id']}.xml"
        cached=a.cache_dir/(pin['set_id']+'.xml') if a.cache_dir else None
        if cached and cached.exists():raw=cached.read_bytes()
        else:
            req=urllib.request.Request(url,headers={'User-Agent':fda.UA})
            with urllib.request.urlopen(req,timeout=45) as r:raw=r.read()
            if cached:cached.parent.mkdir(parents=True,exist_ok=True);cached.write_bytes(raw)
        rec=parse_spl(raw,pin,generics[pin['slug']])
        dest=ROOT/'data/drugs/labels'/(pin['slug']+'.json')
        old=None
        if dest.exists():
            old=json.loads(dest.read_text())
            if old.get('selection',{}).get('spl_sha256')==rec['selection']['spl_sha256']:
                rec['fetched_at']=old.get('fetched_at',rec['fetched_at'])
        reconcile_changes(changes,old,rec)
        dest.write_text(json.dumps(rec,ensure_ascii=False,indent=1)+'\n')
        restored.append(pin['slug'])
        print(pin['slug'],len(rec['sections']),'sections',rec['label']['effective_time'],flush=True)
    if json.dumps(changes,sort_keys=True)!=before_changes:
        changes['generated_at']=dt.datetime.now(fda.MANILA).isoformat(timespec='seconds')
        for key in ('added','changed','removed'):
            changes[key].sort(key=lambda e:e['slug'])
        changes_path.write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
    missing=ROOT/'data/drugs/labels/_missing.json'
    if missing.exists():
        doc=json.loads(missing.read_text())
        if isinstance(doc,dict) and isinstance(doc.get('missing'),list):
            doc['missing']=[x for x in doc['missing'] if x.get('slug') not in restored]
            doc['count']=len(doc['missing'])
            missing.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
