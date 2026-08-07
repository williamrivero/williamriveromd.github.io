#!/usr/bin/env python3
"""Remove redundant Kapampangan spans that were malformed-nested INSIDE Cebuano
spans. These are leftovers from an earlier authoring pass: the real kap content
was opened inside the ceb span (e.g.
   <span data-lang="ceb">PREFIX<span data-lang="kap">…</span>SUFFIX</span> )
instead of as a proper sibling. A correct kap sibling now exists after the ceb
span, so the nested copy is dead weight (hidden by the language toggle). This
strips exactly those nested kap spans, byte-exactly, leaving the surrounding
Cebuano text intact.

Usage: python3 i18n_cleanup_nested_kap.py guides/<file>.html [--dry-run]
"""
import re, sys

def raw_spans(html):
    """Yield (start, end, attrs) for EVERY <span>…</span> incl. nested."""
    out = []
    open_re = re.compile(r'<span\b([^>]*)>')
    tok = re.compile(r'<span\b[^>]*>|</span>')
    i = 0
    while True:
        m = open_re.search(html, i)
        if not m:
            break
        start = m.start(); attrs = m.group(1)
        if attrs.rstrip().endswith('/'):
            i = m.end(); continue
        depth = 1; j = m.end()
        while depth > 0:
            t = tok.search(html, j)
            if not t:
                j = len(html); break
            if t.group(0).startswith('</'):
                depth -= 1; j = t.end()
                if depth == 0:
                    out.append((start, j, attrs))
            else:
                depth += 1; j = t.end()
        i = m.end()
    return out

def main():
    f = sys.argv[1]
    dry = '--dry-run' in sys.argv
    html = open(f, encoding='utf-8').read()
    spans = raw_spans(html)
    ceb = [(s, e) for (s, e, a) in spans if 'data-lang="ceb"' in a]
    kap = [(s, e) for (s, e, a) in spans if 'data-lang="kap"' in a]

    # a kap span is "nested in ceb" if strictly inside some ceb range
    to_remove = []
    for (ks, ke) in kap:
        for (cs, ce) in ceb:
            if cs < ks and ke < ce:
                to_remove.append((ks, ke))
                break

    if not to_remove:
        print(f"{f}: nothing to remove")
        return

    # also swallow a single run of whitespace immediately before each removal
    ranges = []
    for (ks, ke) in sorted(set(to_remove)):
        s = ks
        while s > 0 and html[s-1] in ' \t\r\n':
            s -= 1
        # keep exactly one preceding space if the char after removal isn't
        # whitespace/tag-close (so words don't glue together)
        ranges.append((s, ke))

    # remove back-to-front
    new = html
    for (s, e) in sorted(ranges, reverse=True):
        # insert a single space if removal would join two word chars
        before = new[s-1] if s > 0 else ''
        after = new[e] if e < len(new) else ''
        joiner = ' ' if (before and after and before not in '> \t\r\n' and after not in '< \t\r\n') else ''
        new = new[:s] + joiner + new[e:]

    if dry:
        print(f"{f}: would remove {len(ranges)} nested kap span(s)")
    else:
        open(f, 'w', encoding='utf-8').write(new)
        print(f"{f}: removed {len(ranges)} nested kap span(s)")

if __name__ == '__main__':
    main()
