#!/usr/bin/env python3
"""Extract untranslated PATIENT-facing English elements from a guide.

A target = an element with data-lang="en" that is missing one or more of its
tl/ceb/kap sibling translations, and is NOT inside a clinician-only
(physician-mode / mode-physician) block. Clinician content stays English-only.

Handles BOTH full gaps (no tl/ceb/kap at all) and partial gaps (e.g. tl+ceb
present but kap missing). For each target it records:
  id, tag, open_tag  — the EN element's opening tag (to clone siblings)
  en_inner           — English inner HTML to translate
  missing            — which of tl/ceb/kap are absent, in canonical order
  group_outer        — EXACT raw HTML from the EN element through its last
                       existing consecutive same-tag data-lang sibling
                       (new siblings are inserted immediately after this).

Outputs the job list as JSON on stdout.

Usage: python3 i18n_extract.py guides/<file>.html > job.json
"""
import html as _html, json, re, sys
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
        if attrs.rstrip().endswith('/'):
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
                    out.append((start, j, attrs, html[m.end():t.start()]))
            else:
                depth += 1
                j = t.end()
        # advance just past THIS open tag (not past the whole element) so nested
        # same-tag elements (e.g. a data-lang span inside a wrapper span) are
        # also emitted.
        i = m.end()
    return out

def norm(s):
    # strip tags, decode entities (so raw "&nbsp;" matches bs4's decoded space),
    # then collapse whitespace
    return ' '.join(_html.unescape(re.sub(r'<[^>]+>', ' ', s)).split())

def extend_group(html, tag, end):
    """From position `end` (just after the EN element), consume consecutive
    same-tag data-lang (tl/ceb/kap) siblings; return the new end index."""
    sib_open = re.compile(r'\s*<' + tag + r'\b[^>]*data-lang="(tl|ceb|kap)"[^>]*>')
    tok = re.compile(r'<' + tag + r'\b[^>]*>|</' + tag + r'>')
    pos = end
    while True:
        m = sib_open.match(html, pos)
        if not m:
            break
        depth = 1
        j = m.end()
        while depth > 0:
            t = tok.search(html, j)
            if not t:
                return pos
            if t.group(0).startswith('</'):
                depth -= 1; j = t.end()
            else:
                depth += 1; j = t.end()
        pos = j
    return pos

def main():
    f = sys.argv[1]
    html = open(f, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'lxml')

    targets = []  # (tag, norm_text, missing)
    for el in soup.find_all(attrs={'data-lang': 'en'}):
        parent = el.parent
        have = {s.get('data-lang') for s in parent.find_all(attrs={'data-lang': True}, recursive=False)}
        if all(l in have for l in ('tl', 'ceb', 'kap')):
            continue
        if any(('mode-physician' in (a.get('class') or []) or 'physician-mode' in (a.get('class') or []))
               for a in el.parents):
            continue
        missing = [l for l in ('tl', 'ceb', 'kap') if l not in have]
        targets.append((el.name, norm(el.decode_contents()), missing))

    # raw index per tag: normalized-inner -> list of (open_tag, inner, group_outer) doc order
    raw_by_tag = {}
    for tag in {t for t, _, _ in targets}:
        d = {}
        for (s, e, a, inner) in raw_tags(html, tag):
            if 'data-lang="en"' in a:
                open_tag = html[s:s + html[s:e].index('>') + 1]
                grp_end = extend_group(html, tag, e)
                d.setdefault(norm(inner), []).append((open_tag, inner, html[s:grp_end]))
        raw_by_tag[tag] = d

    job = []
    used = {}
    for i, (tag, t, missing) in enumerate(targets):
        cands = raw_by_tag.get(tag, {}).get(t)
        if not cands:
            print(f"WARN: no raw match for target #{i} <{tag}>: {t[:70]}", file=sys.stderr)
            continue
        key = (tag, t)
        k = used.get(key, 0)
        open_tag, inner, group_outer = cands[k] if k < len(cands) else cands[-1]
        used[key] = k + 1
        job.append({"id": f"s{i}", "tag": tag, "open_tag": open_tag,
                    "missing": missing, "group_outer": group_outer,
                    "en_inner": inner, "preview": t[:110]})

    json.dump(job, sys.stdout, ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
