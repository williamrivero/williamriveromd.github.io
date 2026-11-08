#!/usr/bin/env python3
"""Build guides/search-index.json — extra search terms for the guides index search bar.

The search box on guides/index.html matches a tile's title, teaser and data-text.
That misses terms that are covered inside a guide but not named on its tile
(a drug, a trial, a lab test, a complication). This script reads every guide
linked from the index and collects, from its English content only:

  * strong fields: <title>, meta description/keywords, hero tag, section
    headings (h2–h4), nav-strip pills, glossary terms and definitions, figure
    descriptions and alt text, table headers, bold/strong terms
  * distinctive body words: words used at least MIN_TF times in the body that
    appear in fewer than MAX_DF of all guides (so "kidney" or "patient" does not
    make every guide match, but "tacrolimus" or "leptospirosis" does)

Output: {"<file>.html": "space-separated unique lowercase terms", ...}
The index page fetches it once and searches it alongside the tile text.

Usage: python3 generate_search_index.py [--dry-run] [--guide file.html]
Run after adding or substantially editing a guide (the setup-guide command and
the sitemap GitHub Action run it too).
"""
import argparse, html, json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(ROOT, 'guides', 'index.html')
OUT = os.path.join(ROOT, 'guides', 'search-index.json')
MIN_TF, MAX_DF, MAX_DF_STRONG, MAX_BODY = 3, 0.15, 0.40, 120

STOP = set("""a about above after again against all also am an and any are as at be because been before being below
between both but by can could did do does doing down during each few for from further had has have having he her here
hers him his how i if in into is it its itself just me more most my no nor not now of off on once only or other our
ours out over own same she should so some such than that the their theirs them then there these they this those through
to too under until up very was we were what when where which while who whom why will with would you your yours
yourself yourselves may might must shall also however often usually many much less like well even still yet within
without per via vs versus get gets got make makes made use used uses using one two three four five six seven eight nine
ten first second new back see seen way ways part parts kind type types time times day days week weeks year years month
months people person thing things something someone help helps helped need needs needed keep keeps take takes taken
give gives given show shows shown let lets come comes go goes going know known think say says said around across along
among another every either neither each whether since though although because unless upon toward towards rather quite
really especially example include includes including important common commonly level levels high low higher lower
increase increased decrease decreased reduce reduced risk risks guide guides page section read reading
rivero renalcarematters william gregory infographic schematic algorithm chart timeline bottom top left right panel
figure fig image illustration diagram icon icons label labels arrow arrows box boxes honest disclaimer abbreviations
terms term glossary references reference click tap tab tabs view open close""".split())

def strip_hidden(s):
    # drop TL/CEB/KAP translation siblings (any element carrying lang-hidden)
    for _ in range(3):
        s = re.sub(r'<(span|div|p|li|td|th|h[1-6]|dd|dt|strong|a)\b[^>]*\blang-hidden\b[^>]*>.*?</\1>', ' ', s, flags=re.S)
    return s

def text(x):
    x = re.sub(r'<[^>]+>', ' ', x)
    return html.unescape(x)

def words(t):
    out = []
    for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-+/'’.]*[A-Za-z0-9+]|[A-Za-z0-9]", t):
        w = w.lower().strip(".'’-/")
        if len(w) < 3 and not re.search(r'\d', w): continue
        if w in STOP or re.fullmatch(r'\d+([.,]\d+)?', w): continue
        out.append(w)
        if '-' in w or '/' in w:  # also index the parts: "sglt2-inhibitor" -> sglt2, inhibitor
            out += [p for p in re.split(r'[-/]', w) if len(p) >= 3 and p not in STOP]
    return out

def fields(s):
    s = strip_hidden(s)
    s = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', s, flags=re.S)
    core = []   # always kept: title, meta description/keywords, glossary terms
    m = re.search(r'<title>(.*?)</title>', s, re.S); core.append(m.group(1) if m else '')
    for name in ('description', 'keywords'):
        m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % name, s, re.I); core.append(m.group(1) if m else '')
    core += re.findall(r'<dt\b[^>]*>(.*?)</dt>', s, re.S)
    strong = []  # kept unless the word is common across the library
    pats = [r'<div class="hero-tag[^"]*"[^>]*>(.*?)</div>', r'<h[2-4]\b[^>]*>(.*?)</h[2-4]>',
            r'<a class="nav-pill"[^>]*>(.*?)</a>', r'<dd\b[^>]*>(.*?)</dd>',
            r'<p class="fig-desc"[^>]*>(.*?)</p>', r'<img\b[^>]*\balt="([^"]*)"', r'<th\b[^>]*>(.*?)</th>',
            r'<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>']
    for p in pats:
        strong += re.findall(p, s, re.S)
    b = s.find('<body'); body = s[b:] if b >= 0 else s
    for mk in ('<!-- REFERENCES-ACC-START -->', '<div class="dr-card-wrap"', '<footer'):
        i = body.find(mk)
        if i > 0: body = body[:i]
    return words(text(' '.join(core))), words(text(' '.join(strong))), words(text(body))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    a = ap.parse_args()
    idx = open(INDEX, encoding='utf-8').read()
    files = sorted(set(re.findall(r'<a href="([^"#/]+\.html)[^"]*" class="guide-tile', idx)))
    data = {}
    for f in files:
        p = os.path.join(ROOT, 'guides', f)
        if os.path.exists(p):
            data[f] = fields(open(p, encoding='utf-8').read())
    df = Counter()
    for co, st, bw in data.values():
        df.update(set(bw) | set(st) | set(co))
    n = len(data)
    out = {}
    for f, (co, st, bw) in data.items():
        tf = Counter(bw)
        terms = list(dict.fromkeys(co))
        seen = set(terms)
        for w in st:
            if w not in seen and df[w] / n < MAX_DF_STRONG:
                terms.append(w); seen.add(w)
        k = 0
        for w, c in tf.most_common():
            if k >= MAX_BODY or c < MIN_TF: break
            if df[w] / n < MAX_DF and w not in seen:
                terms.append(w); seen.add(w); k += 1
        out[f] = ' '.join(terms)
    if a.guide:
        print(out.get(a.guide, '(not on the index)')[:3000]); return
    blob = json.dumps(out, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
    print(f'{len(out)} guides, {len(blob)/1024:.0f} KB, median {sorted(len(v.split()) for v in out.values())[len(out)//2]} terms/guide')
    if a.dry_run: return
    old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
    if old == blob: print('search-index.json unchanged'); return
    open(OUT, 'w', encoding='utf-8').write(blob)
    print('wrote guides/search-index.json')

if __name__ == '__main__':
    main()
