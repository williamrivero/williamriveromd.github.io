#!/usr/bin/env python3
"""
add_calc_nav_pill.py — inject a floating bottom-center navigation pill into
every calculator page (guides/calc-*.html plus guides/ckd-dri-calculator.html).

The pill is a rounded, two-part widget:
  • left half  → left chevron, links to the calculators index
  • right half → right chevron, links to that calculator's primary related guide
    (the first real guide found in the page's "Related Guides" block; falls back
     to understanding-ckd.html if none is present).

Idempotent: a previously injected pill (between the CALC-NAV-PILL markers) is
stripped and re-inserted on every run, so the right-hand target refreshes if a
page's Related Guides change. Safe to re-run after adding new calculators.

Usage:
  python3 add_calc_nav_pill.py                       # apply to all calculator pages
  python3 add_calc_nav_pill.py --dry-run             # preview without writing
  python3 add_calc_nav_pill.py --guide calc-kfre.html  # single page
"""
import argparse, glob, os, re

GUIDES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guides')
INDEX_URL = 'https://renalcarematters.com/guides/calculators.html'
FALLBACK_GUIDE = 'understanding-ckd.html'

START = '<!-- CALC-NAV-PILL-START -->'
END = '<!-- CALC-NAV-PILL-END -->'

# Explicit right-hand targets for calculators whose Related Guides block lists
# only other calculators (no content guide to auto-detect).
OVERRIDES = {
    'calc-winters-formula.html': 'metabolic-acidosis-ckd.html',
}


def is_guide(href):
    """True if href points to a real content guide (not a calculator/index/tool)."""
    h = href.split('#')[0].split('?')[0]
    if not h.endswith('.html'):
        return False
    if h.startswith('http') or h.startswith('/') or h.startswith('../'):
        return False
    base = os.path.basename(h)
    if base.startswith('calc-'):
        return False
    if base in ('calculators.html', 'symptom-checker.html'):
        return False
    return True


def related_guide(html):
    """First real guide linked in the page's Related Guides block, or None."""
    i = html.find('class="related-guides"')
    seg = html
    if i != -1:
        j = html.find('<footer', i)
        seg = html[i:j if j != -1 else len(html)]
    for h in re.findall(r'class="related-card[^"]*"\s+href="([^"]+)"', seg):
        if is_guide(h):
            return os.path.basename(h.split('#')[0])
    return None


def build_block(target):
    return f'''{START}
<style id="calc-nav-pill-style">
.calc-nav-pill{{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);display:flex;align-items:stretch;z-index:9997;background:#1f3864;border-radius:999px;box-shadow:0 6px 22px rgba(15,30,51,.32);border:1px solid rgba(255,255,255,.14);}}
.calc-nav-pill>a,.calc-nav-pill>.cnp-print{{position:relative;display:flex;align-items:center;justify-content:center;width:58px;height:44px;color:#fff;text-decoration:none;transition:background .18s;background:none;border:none;cursor:pointer;}}
.calc-nav-pill>a:first-child{{border-radius:999px 0 0 999px;}}
.calc-nav-pill>a:last-child{{border-radius:0 999px 999px 0;}}
.calc-nav-pill>a:hover,.calc-nav-pill>.cnp-print:hover{{background:#2a4a7f;}}
.calc-nav-pill>a:first-child:hover{{border-radius:999px 0 0 999px;}}
.calc-nav-pill>a:last-child:hover{{border-radius:0 999px 999px 0;}}
.calc-nav-pill>a:focus-visible,.calc-nav-pill>.cnp-print:focus-visible{{outline:2px solid #d4af4f;outline-offset:-3px;}}
.calc-nav-pill .cnp-div{{width:1px;background:rgba(255,255,255,.22);align-self:stretch;}}
.calc-nav-pill svg{{width:20px;height:20px;}}
.cnp-tip{{position:absolute;bottom:52px;left:50%;transform:translateX(-50%);background:rgba(15,30,51,.92);color:#fff;font-size:11.5px;font-weight:500;white-space:nowrap;padding:5px 10px;border-radius:6px;opacity:0;pointer-events:none;transition:opacity .15s;}}
.calc-nav-pill>a:hover .cnp-tip,.calc-nav-pill>.cnp-print:hover .cnp-tip{{opacity:1;}}
html[data-theme="dark"] .calc-nav-pill{{background:#1a2535;border-color:#2a3548;}}
html[data-theme="dark"] .calc-nav-pill>a:hover,html[data-theme="dark"] .calc-nav-pill>.cnp-print:hover{{background:#243349;}}
.print-fab,.print-btn,.calc-back-btn,.calc-rg-btn{{display:none!important;}}
@media print{{.calc-nav-pill{{display:none!important;}}}}
</style>
<nav class="calc-nav-pill" id="calc-nav-pill" aria-label="Calculator navigation">
<a href="{INDEX_URL}" aria-label="Back to all calculators"><span class="cnp-tip">All Guides</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg></a>
<span class="cnp-div"></span>
<button class="cnp-print" onclick="window.print()" aria-label="Print this page"><span class="cnp-tip">Print</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg></button>
<span class="cnp-div"></span>
<a href="{target}" aria-label="Go to related guide"><span class="cnp-tip">Related Guide</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg></a>
</nav>
{END}'''


SYMPTOM_CHECKER_RE = re.compile(
    r'\n?[ \t]*<script\s+src="[^"]*symptom-checker-widget\.js"[^>]*>\s*</script>[ \t]*'
)


def strip_existing(html):
    return re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', html, flags=re.DOTALL)


def process(path, dry):
    html = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    tgt = OVERRIDES.get(name) or related_guide(html)
    target = tgt or FALLBACK_GUIDE
    fb = '' if tgt else ' (FALLBACK)'
    cleaned = SYMPTOM_CHECKER_RE.sub('', strip_existing(html))
    # Insert before the LAST </body> — earlier ones may live inside JS strings
    # (e.g. win.document.write('</body></html>') for print popups).
    idx = cleaned.rfind('</body>')
    if idx == -1:
        print(f'  {os.path.basename(path):42s} → SKIP (no </body>)')
        return False
    new = cleaned[:idx] + build_block(target) + '\n' + cleaned[idx:]
    changed = new != html
    status = 'updated' if START in html else 'added'
    print(f'  {os.path.basename(path):42s} → {"[DRY] " if dry else ""}{status} · right→{target}{fb}')
    if not dry and changed:
        open(path, 'w', encoding='utf-8').write(new)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    a = ap.parse_args()
    if a.guide:
        files = [os.path.join(GUIDES_DIR, os.path.basename(a.guide))]
    else:
        files = sorted(glob.glob(os.path.join(GUIDES_DIR, 'calc-*.html')))
        dri = os.path.join(GUIDES_DIR, 'ckd-dri-calculator.html')
        if os.path.exists(dri):
            files.append(dri)
    n = sum(process(f, a.dry_run) for f in files)
    print(f'\n{"[DRY RUN] " if a.dry_run else ""}Summary: {n} page(s) '
          f'{"would be " if a.dry_run else ""}changed of {len(files)}.')


if __name__ == '__main__':
    main()
