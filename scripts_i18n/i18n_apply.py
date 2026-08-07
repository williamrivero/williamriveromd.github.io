#!/usr/bin/env python3
"""Apply translations back into a guide, byte-exactly.

Inputs:
  guide.html
  translated.json : [{id, tag, open_tag, en_outer, en_inner, tl, ceb, kap}, ...]
                    (the job file from i18n_extract.py with tl/ceb/kap filled in)

For each item, locate en_outer in the source (must appear >=1 time; the Nth
duplicate is handled in document order) and insert three lang-hidden sibling
elements immediately after it:
    <TAG data-lang="tl" class="lang-hidden">…</TAG>  (+ ceb, kap)
The sibling clones the EN element's attributes, swapping data-lang and ensuring
class contains "lang-hidden".

Usage: python3 i18n_apply.py guides/<file>.html translated.json [--dry-run]
"""
import json, re, sys

def sibling_open(open_tag, lang):
    """Build the sibling opening tag for `lang` from the EN element's open tag."""
    # swap data-lang value
    t = re.sub(r'data-lang="en"', f'data-lang="{lang}"', open_tag)
    # ensure a class attribute containing lang-hidden
    m = re.search(r'class="([^"]*)"', t)
    if m:
        classes = m.group(1).split()
        if 'lang-hidden' not in classes:
            classes.append('lang-hidden')
        t = t[:m.start()] + 'class="' + ' '.join(classes) + '"' + t[m.end():]
    else:
        # inject class right after <tag
        t = re.sub(r'^(<\w+)', r'\1 class="lang-hidden"', t)
    return t

def main():
    guide = sys.argv[1]
    jobfile = sys.argv[2]
    dry = '--dry-run' in sys.argv
    html = open(guide, encoding='utf-8').read()
    items = json.load(open(jobfile, encoding='utf-8'))

    # process in document order of first occurrence to keep duplicate handling sane
    # track a search cursor per distinct en_outer
    applied = 0
    errors = []
    # We must handle duplicates: build ordered occurrence lists.
    # Strategy: for each item, find en_outer; if it already is followed by its tl
    # sibling, skip (idempotent). Insert after the first not-yet-patched occurrence.
    for it in items:
        for l in ('tl', 'ceb', 'kap'):
            if l not in it or it[l] is None or it[l] == '':
                errors.append(f"{it['id']}: missing {l}")
        if errors and errors[-1].startswith(it['id']):
            continue
        outer = it['en_outer']
        tag = it['tag']
        # build the three siblings
        sibs = ''
        for l in ('tl', 'ceb', 'kap'):
            sibs += sibling_open(it['open_tag'], l) + it[l] + f'</{tag}>'
        # find an occurrence of outer that is NOT already followed by the tl sibling
        start = 0
        target_pos = -1
        while True:
            p = html.find(outer, start)
            if p == -1:
                break
            after = html[p + len(outer): p + len(outer) + 40]
            if re.match(r'\s*<' + tag + r'\b[^>]*data-lang="tl"', after):
                start = p + len(outer)  # already patched here, look further
                continue
            target_pos = p
            break
        if target_pos == -1:
            errors.append(f"{it['id']}: en_outer not found (or all already patched): {it['preview'][:60]}")
            continue
        insert_at = target_pos + len(outer)
        html = html[:insert_at] + sibs + html[insert_at:]
        applied += 1

    if errors:
        print("ERRORS:")
        for e in errors:
            print("  " + e)
        print(f"\n{applied} applied, {len(errors)} errors — NOT writing.", file=sys.stderr)
        sys.exit(1)

    if dry:
        print(f"[dry-run] would apply {applied} insertions to {guide}")
    else:
        open(guide, 'w', encoding='utf-8').write(html)
        print(f"applied {applied} insertions to {guide}")

if __name__ == '__main__':
    main()
