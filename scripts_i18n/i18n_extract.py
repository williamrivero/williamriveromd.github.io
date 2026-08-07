#!/usr/bin/env python3
"""Extract untranslated PATIENT-facing English spans from a guide.

A target = a <span data-lang="en">…</span> that (a) is NOT immediately followed
by a data-lang="tl" sibling, and (b) is NOT inside a clinician-only
(physician-mode / mode-physician) block. Clinician content stays English-only.

Outputs a JSON job file: [{id, en_inner, preview}] in document order, where
en_inner is the EXACT raw inner HTML from source (so apply is byte-exact).

Usage: python3 i18n_extract.py guides/<file>.html > job.json
"""
import json, re, sys
from bs4 import BeautifulSoup

def raw_tags(html, tag):
    """Depth-aware scan of every <tag ...>...</tag>; yields (start,end,attrs_str,inner)."""
    out = []
    i = 0
    open_re = re.compile(r'<' + tag + r'\b([^>]*)>')
    tok = re.compile(r'<' + tag + r'\b[^>]*>|</' + tag + r'>')
    while True:
        m = open_re.search(html, i)
        if not m:
            break
        start = m.start()
        attrs = m.group(1)
        if attrs.rstrip().endswith('/'):  # self-closing, no inner
            i = m.end(); continue
        depth = 1
        j = m.end()
        while depth > 0:
            t = tok.search(html, j)
            if not t:
                j = len(html); break
            if t.group(0).startswith('</'):
                depth -= 1
                j = t.end()
                if depth == 0:
                    inner = html[m.end():t.start()]
                    out.append((start, j, attrs, inner))
            else:
                depth += 1
                j = t.end()
        i = j
    return out

def norm(s):
    return ' '.join(re.sub(r'<[^>]+>', ' ', s).split())

def main():
    f = sys.argv[1]
    html = open(f, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'lxml')

    # target set: (tag, normalized text) of untranslated patient EN elements
    targets = []
    for el in soup.find_all(attrs={'data-lang': 'en'}):
        parent = el.parent
        have = {s.get('data-lang') for s in parent.find_all(attrs={'data-lang': True}, recursive=False)}
        if all(l in have for l in ('tl', 'ceb', 'kap')):
            continue
        if any(('mode-physician' in (a.get('class') or []) or 'physician-mode' in (a.get('class') or []))
               for a in el.parents):
            continue
        targets.append((el.name, norm(el.decode_contents())))

    # raw index per tag: normalized-inner -> list of (open_tag, inner, outer) (doc order)
    raw_by_tag = {}
    for tag in {t for t, _ in targets}:
        d = {}
        for (s, e, a, inner) in raw_tags(html, tag):
            if 'data-lang="en"' in a:
                open_tag = html[s:s + html[s:e].index('>') + 1]
                outer = html[s:e]
                d.setdefault(norm(inner), []).append((open_tag, inner, outer))
        raw_by_tag[tag] = d

    job = []
    used = {}
    for i, (tag, t) in enumerate(targets):
        cands = raw_by_tag.get(tag, {}).get(t)
        if not cands:
            print(f"WARN: no raw match for target #{i} <{tag}>: {t[:70]}", file=sys.stderr)
            continue
        key = (tag, t)
        k = used.get(key, 0)
        open_tag, inner, outer = cands[k] if k < len(cands) else cands[-1]
        used[key] = k + 1
        job.append({"id": f"s{i}", "tag": tag, "open_tag": open_tag,
                    "en_outer": outer, "en_inner": inner, "preview": t[:110]})

    json.dump(job, sys.stdout, ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
