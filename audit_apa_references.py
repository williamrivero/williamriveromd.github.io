#!/usr/bin/env python3
"""Audit every guide's References block for APA-7 compliance.

Per CLAUDE.md rule 5, the collapsible accordion
(<!-- REFERENCES-ACC-START --> ... <!-- REFERENCES-ACC-END -->) is the only
rendered References location, and every <li> inside its <ol> must be APA 7
format:

    Author, A. A., Author, B. B., & Author, C. C. (Year). Sentence-case
    title. <em>Journal Name</em>, <em>Volume</em>(Issue), pages.
    <a href="https://doi.org/…">https://doi.org/…</a>

This script scans each guide and reports compliance per citation, using
five lightweight heuristics:

  ITAL    — at least one <em> tag (italic journal name + volume)
  DOI     — a doi.org link (preferred) OR another http URL
  YEAR    — a (YYYY) year in parens
  AUTH    — an "Author, X." style author block before the year, OR an
            "& Lastname, X. Y." for multi-author cites, OR a corporate/
            group author ending in an acronym in parens right before the
            year, e.g. "... (KDIGO) CKD Work Group. (2024)."
  PAGES   — page range "NN-NN" or "NN–NN" or e-locator "eNNNN"

A citation gets a PASS if ITAL + DOI + YEAR + AUTH are all present.
Pure interactive tools (calculators, symptom-checker, label scanner,
interpreters, blank logs) and the guides index are excluded.

Usage:
    python3 audit_apa_references.py
    python3 audit_apa_references.py --details        # show every failing citation
    python3 audit_apa_references.py --guide <slug>   # one guide

Exits 1 if any non-compliant guide is found (CI-friendly).
"""
import re, sys, pathlib

GUIDES = pathlib.Path(__file__).parent / "guides"

# Exclude pure tools / non-narrative pages — they have no citable sources.
SKIP_PREFIX = ("calc-",)
SKIP_EXACT = {
    "index.html", "calculators.html", "ckd-dri-calculator.html",
    "symptom-checker.html", "lab-interpreter-guide.html",
    "ckd-label-scanner.html", "ckd-recipe-analyzer.html",
    "dyslipidemia-management-tool.html",
    # Printable handouts / logs
    "bp-log-blank.html", "bp-monitoring-log.html",
    "alcohol-drinking-log.html",
    # Atlas / physiology reference pages
    "nephrology-atlas.html", "kidney-physiology.html",
}
SKIP_SUFFIX = ("-log.html", "-log-blank.html", "-blank.html")


def is_guide(name):
    if name in SKIP_EXACT: return False
    if name.startswith(SKIP_PREFIX): return False
    if name.endswith(SKIP_SUFFIX): return False
    return True


ACC_OL_RE = re.compile(
    r'<!-- REFERENCES-ACC-START -->.*?<ol[^>]*>(.*?)</ol>',
    re.DOTALL,
)
LI_RE = re.compile(r'<li>(.*?)</li>', re.DOTALL)


def get_citations(src):
    """Return the list of citation strings from the References accordion, or []."""
    m = ACC_OL_RE.search(src)
    if not m: return []
    return [li.strip() for li in LI_RE.findall(m.group(1)) if li.strip()]


def check_apa(cite):
    """Run five APA heuristics; return dict of bool flags + overall pass."""
    flags = {
        'ITAL':  bool(re.search(r'<em>[^<]+</em>', cite)),
        'DOI':   bool(re.search(r'doi\.org/', cite, re.I)),
        'URL':   bool(re.search(r'https?://', cite)),
        'YEAR':  bool(re.search(r'\(\s*(19|20)\d{2}\s*[a-z]?\)', cite)),
        'AUTH':  bool(re.search(r'[A-Z][a-zA-Z\-]+,\s+[A-Z]\.', cite)) or
                 bool(re.search(r'\([A-Z]{2,8}\)[^()]{0,60}\.\s*\(\s*(19|20)\d{2}', cite)),
        'PAGES': bool(re.search(r'\b\d+[–-]\d+\b|e\d{4,}', cite)),
    }
    # Pass = italics + (DOI or URL) + year + at least one Author, X. block.
    flags['PASS'] = flags['ITAL'] and (flags['DOI'] or flags['URL']) and \
                    flags['YEAR'] and flags['AUTH']
    return flags


def main():
    details = '--details' in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == '--guide' and i+1 < len(sys.argv):
            only = sys.argv[i+1].replace('.html', '') + '.html'

    targets = sorted(GUIDES.glob('*.html'))
    if only:
        targets = [GUIDES / only]

    compliant, noncomp, missing, examined = [], [], [], 0
    fail_samples = {}

    for p in targets:
        if not is_guide(p.name): continue
        examined += 1
        src = p.read_text(encoding='utf-8')
        cites = get_citations(src)
        if not cites:
            missing.append(p.name)
            continue
        rows = [(c, check_apa(c)) for c in cites]
        ok = sum(1 for _, fl in rows if fl['PASS'])
        total = len(rows)
        if ok == total:
            compliant.append((p.name, total))
        else:
            noncomp.append((p.name, ok, total))
            if details:
                fail_samples[p.name] = [
                    (c, fl) for c, fl in rows if not fl['PASS']
                ]

    print(f"\n=== APA-7 References audit ===")
    print(f"Examined:           {examined} guides")
    print(f"Compliant (all ✓):  {len(compliant)}")
    print(f"Non-compliant:      {len(noncomp)}")
    print(f"No accordion found:  {len(missing)}")

    if noncomp:
        print(f"\n--- NON-COMPLIANT (need APA conversion) ---")
        for n, ok, tot in sorted(noncomp, key=lambda r: r[1] - r[2]):
            print(f"  {ok}/{tot:>3}  {n}")

    if missing and len(missing) <= 40:
        print(f"\n--- NO REFERENCES ACCORDION FOUND ---")
        for n in missing:
            print(f"  (sources may be inline / from hero Guidelines line)  {n}")

    if details and fail_samples:
        print(f"\n--- FAILING CITATION SAMPLES ---")
        for name, rows in list(fail_samples.items())[:8]:
            print(f"\n{name}:")
            for c, fl in rows[:3]:
                missing_flags = [k for k in ('ITAL','DOI','URL','YEAR','AUTH','PAGES') if not fl[k]]
                print(f"  missing {missing_flags}")
                print(f"    {c[:180]}")

    return 0 if not noncomp else 1


if __name__ == '__main__':
    sys.exit(main())
