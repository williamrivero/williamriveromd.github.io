#!/usr/bin/env python3
"""Apply translations back into a guide, byte-exactly (per-language aware).

Inputs:
  guide.html
  translated.json : the job list from i18n_extract.py with the missing-language
                    fields filled in. Each item has:
                      tag, open_tag, missing (subset of tl/ceb/kap),
                      group_outer, en_inner, and a key per missing lang.

For each item, locate group_outer in the source (Nth duplicate handled in
document order) and insert one lang-hidden sibling per missing language,
immediately after the existing sibling group, in canonical tl→ceb→kap order:
    <TAG data-lang="kap" class="lang-hidden">…</TAG>
The sibling clones the EN element's opening tag, swapping data-lang and ensuring
class contains "lang-hidden". Idempotent: an occurrence already followed by the
new sibling is skipped.

Usage: python3 i18n_apply.py guides/<file>.html translated.json [--dry-run]
"""
import json, re, sys

def sibling_open(open_tag, lang):
    t = re.sub(r'data-lang="en"', f'data-lang="{lang}"', open_tag)
    m = re.search(r'class="([^"]*)"', t)
    if m:
        classes = m.group(1).split()
        if 'lang-hidden' not in classes:
            classes.append('lang-hidden')
        t = t[:m.start()] + 'class="' + ' '.join(classes) + '"' + t[m.end():]
    else:
        t = re.sub(r'^(<\w+)', r'\1 class="lang-hidden"', t)
    return t

def main():
    guide = sys.argv[1]
    jobfile = sys.argv[2]
    dry = '--dry-run' in sys.argv
    html = open(guide, encoding='utf-8').read()
    items = json.load(open(jobfile, encoding='utf-8'))

    applied = 0
    errors = []
    for it in items:
        missing = it.get('missing', ['tl', 'ceb', 'kap'])
        for l in missing:
            if not it.get(l):
                errors.append(f"{it['id']}: missing translation field '{l}'")
        if any(e.startswith(it['id'] + ':') for e in errors):
            continue
        tag = it['tag']
        anchor = it['group_outer']
        sibs = ''
        for l in ('tl', 'ceb', 'kap'):
            if l in missing:
                sibs += sibling_open(it['open_tag'], l) + it[l] + f'</{tag}>'
        # find an occurrence of anchor not already followed by the first new sibling
        first_lang = next(l for l in ('tl', 'ceb', 'kap') if l in missing)
        start = 0
        target_pos = -1
        while True:
            p = html.find(anchor, start)
            if p == -1:
                break
            after = html[p + len(anchor): p + len(anchor) + 60]
            if re.match(r'\s*<' + tag + r'\b[^>]*data-lang="' + first_lang + r'"', after):
                start = p + len(anchor); continue
            target_pos = p
            break
        if target_pos == -1:
            errors.append(f"{it['id']}: anchor not found (or already patched): {it['preview'][:60]}")
            continue
        insert_at = target_pos + len(anchor)
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
