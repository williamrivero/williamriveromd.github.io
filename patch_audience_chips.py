#!/usr/bin/env python3
"""Rebuild the Patients / Clinicians audience chips on guides/index.html.

The chips on each guide tile say which audience tabs the guide actually has:
  both      -> "Patients" + "Clinicians"  (guide has a Patients & Families tab AND a Clinicians tab)
  patient   -> "Patients" only             (single-audience patient guide)
  clinician -> "Clinicians" only           (single-audience clinician guide)

Detection, per guide file:
  * both:      the page has setMode('patient') and setMode('physician') tab buttons
  * clinician: <body> carries physician-mode, the filename ends in -clinician.html,
               the hero tag says Clinician Reference / Clinicians Only / Clinical
               Reference / Clinical Operations, or the file is in CLINICIAN_PAGES
  * patient:   everything else

It also keeps the sidebar "Clinicians" filter honest: a tile carries the
`clinician` data-tag exactly when the guide has a Clinicians tab (both/clinician).

Run after adding a guide tile, or after adding/removing a guide's audience tabs.
Usage: python3 patch_audience_chips.py [--dry-run] [--report]
"""
import argparse, json, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(ROOT, 'guides', 'index.html')
# Single-tab pages written for clinicians that the automatic rules do not catch
CLINICIAN_PAGES = {
    'dialysis-machine-assignment.html', 'code-blue-acls-dialysis-unit.html',
    'dialyzer-reprocessing-reuse.html', 'nephrology-atlas.html',
    'hemoperfusion-blood-purification.html', 'innovative-technologies-ckd.html',
    'new-therapeutic-agents-ckd.html', 'ketogenic-chrononutrition-ckd.html',
}

def audience(fname):
    p = os.path.join(ROOT, 'guides', fname)
    if not os.path.exists(p):
        return None
    s = open(p, encoding='utf-8').read()
    if "setMode('physician')" in s and "setMode('patient')" in s:
        return 'both'
    bc = (re.search(r'<body([^>]*)>', s) or [0, ''])[1]
    if 'physician-mode' in bc or fname.endswith('-clinician.html') or fname in CLINICIAN_PAGES:
        return 'clinician'
    tag = re.search(r'<div class="hero-tag[^"]*"[^>]*>(.*?)</div>', s, re.S)
    tag = re.sub(r'<span[^>]*lang-hidden.*?</span>', '', tag.group(1), flags=re.S) if tag else ''
    if re.search(r'Clinician Reference|Clinicians Only|Clinical Reference|Clinical Operations', tag) and 'Patient' not in tag:
        return 'clinician'
    return 'patient'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--report', action='store_true')
    a = ap.parse_args()
    s = open(INDEX, encoding='utf-8').read()
    files = sorted(set(re.findall(r'<a href="([^"#/]+\.html)[^"]*" class="guide-tile', s)))
    amap = {f: au for f in files if (au := audience(f))}
    if a.report:
        for f, au in sorted(amap.items(), key=lambda x: (x[1], x[0])):
            print(f'{au:9s} {f}')
    print('audience:', dict(Counter(amap.values())))
    orig = s
    # Static Clinicians chips are superseded by the generated ones
    s = re.sub(r'\n[ \t]*<span class="meta-tag tag-clinician">Clinicians</span>[ \t]*(?=\n)', '', s)
    s = s.replace('<span class="meta-tag tag-clinician">Clinicians</span>', '')
    added = removed = 0
    def fix(m):
        nonlocal added, removed
        href, cls, tags = m.group(1), m.group(2), m.group(3)
        f = href.split('#')[0]
        if f not in amap:
            return m.group(0)
        t = tags.split(); has = 'clinician' in t; want = amap[f] in ('both', 'clinician')
        if want and not has: t.append('clinician'); added += 1
        if has and not want: t = [x for x in t if x != 'clinician']; removed += 1
        return f'<a href="{href}" class="{cls}" data-tags="{" ".join(t)}"'
    s = re.sub(r'<a href="([^"]+)" class="(guide-tile[^"]*)" data-tags="([^"]*)"', fix, s)
    i = s.index('var AUD = '); j = s.index(';\n', i)
    s = s[:i] + 'var AUD = ' + json.dumps(amap, separators=(',', ':')) + s[j:]
    print(f'clinician filter tag: +{added} / -{removed}')
    if s == orig:
        print('no changes'); return
    if a.dry_run:
        print('[dry run] guides/index.html would change'); return
    open(INDEX, 'w', encoding='utf-8').write(s)
    print('updated guides/index.html')

if __name__ == '__main__':
    main()
