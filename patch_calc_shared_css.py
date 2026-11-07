#!/usr/bin/env python3
"""Install the shared calculator component stylesheet on every calculator page.

Why: several calculator pages kept their component CSS (checklist items, hero
cross-links, MDCalc accordions, result cards) inside the FIRST <style> block,
which patch_master_css.py rewrites — so those components rendered unstyled.
This script inserts ONE shared block, <style id="calc-shared-style">, directly
after the first (master) </style>. It is a SECOND block, so patch_master_css.py
never touches it, and it sits BEFORE any page-specific block, so a page's own
rules still win on equal specificity.

It also fixes two layout bugs seen across the library:
  * long unbreakable strings (e.g. "AHA/ACC/AACVPR/AAPA/...") pushing the page
    wider than a phone screen;
  * inline-flex rating/pill rows that never wrap on narrow screens.

Usage:
  python3 patch_calc_shared_css.py                 # all calculators
  python3 patch_calc_shared_css.py --dry-run
  python3 patch_calc_shared_css.py --guide calc-kfre.html
Idempotent: an existing calc-shared-style block is replaced in place.
"""
import argparse, glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
GUIDES = os.path.join(ROOT, 'guides')

SHARED_CSS = r"""<style id="calc-shared-style">
/* Shared calculator components — managed by patch_calc_shared_css.py. Do not edit per page. */
/* Layout safety: long strings wrap, wide tables scroll inside their box, never the page. */
main.container{overflow-wrap:break-word;}
.mdc-acc-body,.calc-disclaimer,.calc-verdict-text,.calc-action-text,.ref-acc li,.disclaimer,.alert-body{overflow-wrap:anywhere;}
.mdc-acc-body table,.calc-wrap table{max-width:100%;}
.mdc-acc-body .table-wrap,.calc-wrap .table-wrap{overflow-x:auto;}
.calc-wrap input,.calc-wrap select,.calc-wrap textarea{max-width:100%;box-sizing:border-box;}
/* Result boxes: master CSS hides .calc-result-box until a page shows it. Pages that reveal it via a
   state class (show / res-ok / res-warn / res-bad) need these rules, which were lost in a master rewrite. */
.calc-result-box.show,.calc-result-box.res-ok,.calc-result-box.res-warn,.calc-result-box.res-bad{display:block;}
/* Hero cross-links */
.hero-xlink{color:#0e4a50;font-weight:600;text-decoration:underline;text-decoration-color:var(--gold-light);text-decoration-thickness:1.5px;text-underline-offset:3px;border-radius:6px;padding:2px 4px;}
.hero-xlink:hover{color:#0b3a40;}
.hero-xlink:focus-visible{outline:2px solid var(--gold-light);outline-offset:2px;}
/* MDCalc-style instructions + accordions */
.mdc-instructions{background:var(--teal-light);border-left:3px solid var(--teal);border-radius:0;padding:14px 18px 12px;margin:22px 0 18px;}
.mdc-instr-label{display:block;font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--teal);margin-bottom:4px;}
.mdc-instructions ol,.mdc-instructions ul{margin:0 0 0 1.1em;padding:0;}
.mdc-instructions p{margin:0;text-align:left;}
.mdc-acc{border:1px solid var(--border);border-radius:10px;margin:10px 0;background:var(--white);}
.mdc-acc>summary{cursor:pointer;list-style:none;padding:15px 20px;font-family:'Inter',sans-serif;font-weight:600;color:var(--navy);font-size:1.06rem;display:flex;align-items:center;justify-content:space-between;gap:12px;}
.mdc-acc>summary::-webkit-details-marker{display:none;}
.mdc-acc>summary::after{content:"+";font-size:1.5rem;line-height:1;color:var(--teal);font-weight:400;flex:none;}
.mdc-acc[open]>summary::after{content:"\2212";}
.mdc-acc[open]>summary{border-bottom:1px solid var(--border);}
.mdc-acc-body{padding:6px 20px 18px;}
.mdc-acc-body p,.calc-wrap p,.calc-result-box p{text-align:left;hyphens:manual;}
/* Checklist scoring items (HAS-BLED, STOP-BANG, CURB-65, ...) */
.check-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px;margin-bottom:16px;}
.check-item{display:flex;align-items:flex-start;gap:10px;background:var(--white);border:1px solid var(--border);border-radius:8px;padding:11px 13px;cursor:pointer;transition:border-color .15s,background .15s;}
.check-item:hover{border-color:var(--teal);}
.check-item input[type="checkbox"],.check-item input[type="radio"]{accent-color:var(--teal);width:16px;height:16px;flex-shrink:0;margin-top:2px;cursor:pointer;}
.check-item-body{flex:1;min-width:0;}
.ci-label{font-size:13.5px;font-weight:600;color:var(--text);line-height:1.4;}
.ci-pts{font-size:11.5px;color:var(--text-muted);margin-top:2px;}
.check-group{margin-bottom:14px;}
/* Rating / pill rows wrap instead of overflowing on phones */
.ipss-opts,.ipss-qol-row,.tx-pills,.qol-row,.likert-row{flex-wrap:wrap;}
/* Result cards built by JS on ~20 pages (GCS, 4Ts, keGFR, NRI, Parkland...) */
.result-card{border-radius:12px;padding:18px 22px;margin-top:16px;border:2px solid var(--border,#e2e6eb);background:var(--white,#fff);}
.result-card.result-normal{background:var(--green-soft,#edf7f2);border-color:var(--green,#2d7a4f);}
.result-card.result-caution{background:var(--amber-soft,#fef9ec);border-color:#d97706;}
.result-card.result-danger{background:var(--red-soft,#fdf0ef);border-color:var(--red,#c0392b);}
.result-label{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text-muted,#6b7a8d);}
.result-value{font-size:30px;font-weight:700;line-height:1.15;margin:2px 0 4px;color:var(--navy,#0f1e2e);}
.result-sublabel{font-size:14px;font-weight:700;color:var(--text,#2c3a4a);}
.result-card.result-normal .result-sublabel{color:var(--green,#2d7a4f);}
.result-card.result-caution .result-sublabel{color:#9a6500;}
.result-card.result-danger .result-sublabel{color:var(--red,#c0392b);}
.result-action{font-size:13.5px;line-height:1.65;color:var(--text-mid,#3a4a5c);margin-top:12px;padding-top:12px;border-top:1px solid rgba(0,0,0,.1);}
html[data-theme="dark"] .result-card{background:rgba(255,255,255,.04);}
html[data-theme="dark"] .result-card.result-normal{background:rgba(45,122,79,.12);}
html[data-theme="dark"] .result-card.result-caution{background:rgba(217,119,6,.12);}
html[data-theme="dark"] .result-card.result-danger{background:rgba(192,57,43,.12);}
html[data-theme="dark"] .result-value{color:var(--text);}
html[data-theme="dark"] .result-action{color:var(--text-mid);border-top-color:rgba(255,255,255,.12);}
html[data-theme="dark"] .result-card.result-normal .result-sublabel{color:#7fdca4;}
html[data-theme="dark"] .result-card.result-caution .result-sublabel{color:#f3c06b;}
html[data-theme="dark"] .result-card.result-danger .result-sublabel{color:#fca5a5;}
/* Dark mode */
html[data-theme="dark"] .hero-xlink{color:#5fd0d8;}
html[data-theme="dark"] .mdc-instructions{background:rgba(26,107,114,.12);}
html[data-theme="dark"] .mdc-acc{background:#141c2a;border-color:#26314a;}
html[data-theme="dark"] .mdc-acc>summary{color:var(--text);}
html[data-theme="dark"] .check-item{background:#1a2535;border-color:#2a3548;}
html[data-theme="dark"] .ci-label{color:var(--text);}
html[data-theme="dark"] .ci-pts{color:#9ba6b8;}
</style>
"""


def _dark_inline_rules():
    """Dark-mode overrides for hard-coded inline colors (light-theme hexes).

    Matches only the `color` property (preceded by start-of-attribute or ';'),
    never background-color/border-color, in both hand-written hex and the
    rgb() form browsers produce when JS sets el.style.color.
    """
    def rgb(h):
        h = h.lstrip('#')
        return 'rgb(%d, %d, %d)' % tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    groups = {
        '#5fd0d8': ['#1a6b72', '#145c63', '#0d4f55'],
        '#dde3eb': ['#1f3864', '#1a3c72', '#0f1e2e', '#0e1929', '#3a4a5c', '#4a5a6a', '#2c3a4a'],
        '#9ba6b8': ['#6b7280', '#6b7a8d'],
        '#c9b3f2': ['#4a2080', '#5b21b6'],
        '#f3c06b': ['#7a4800', '#92400e', '#b45309'],
        '#7fdca4': ['#166534', '#2d7a4f', '#15803d'],
        '#fca5a5': ['#b91c1c', '#991b1b', '#7f1d1d', '#dc2626'],
        '#8cc8f0': ['#0369a1', '#1e40af'],
    }
    out = []
    for new, olds in groups.items():
        sels = []
        for h in olds:
            for v in (h, rgb(h)):
                for pre in ('^="color:', '^="color: ', '*=";color:', '*="; color:', '*=";color: '):
                    sels.append('html[data-theme="dark"] [style%s%s" i]' % (pre, v))
        out.append(',\n'.join(sels) + '{color:%s!important;}' % new)
    return '\n'.join(out)


DARK_EXTRA = r"""
/* Dark mode: default-blue links inside content panels */
html[data-theme="dark"] :is(.calc-wrap,.mdc-acc,.disclaimer,.alert,.qs-intro,.mw-intro,.calc-result-box,.mdc-instructions) a:not([class]){color:#5fd0d8;}
/* Dark mode: hard-coded light inline panel backgrounds */
html[data-theme="dark"] :is([style*="background:#f0" i],[style*="background:#f5" i],[style*="background:#f8" i],[style*="background:#fe" i],[style*="background:#ff" i],[style*="background: #f0" i],[style*="background: #fe" i],[style*="background:#ec" i],[style*="background:#ed" i],[style*="background:#ef" i],[style*="background:white" i],[style*="background-color:#f" i],[style*="background: rgb(2" i]):not(button):not(.calc-result-box):not([style*="color:#fff" i]):not([style*="color:white" i]):not([style*="color: rgb(255, 255, 255)"]){background:rgba(255,255,255,.05)!important;}
/* Dark mode: white text on the bright dark-theme teal is only ~2.9:1; deepen it */
html[data-theme="dark"] :is(.ln-wt-badge,.iief-num,.fs-sbar-letter,.wkt-qnum,.btn-primary,.tb-btn,.prom-tab-btn.active,.prom-calc-btn,.hd-tab.active,.ipss-btn-print,.badge,.btn-calc,.sbirt-tab.active,button.sel,.ln-tab.active,.ln-pill.sel,.tx-tab.active,.tx-btn-primary,.ut-btn.active,.wells-modebtn.active,.quiz-btn,.unit-btn.active,.calc-btn:not(.secondary),.cbtn.active){background-color:#157f87!important;border-color:#157f87!important;color:#fff!important;}
html[data-theme="dark"] .calc-btn.secondary{color:#0f1520;}
html[data-theme="dark"] .fs-sbar-item label{color:var(--text);}
html[data-theme="dark"] [style*="color:var(--navy)" i]{color:var(--text)!important;}
html[data-theme="dark"] .check-item{color:var(--text);}
html[data-theme="dark"] .ipss-q-text{color:var(--text);}
html[data-theme="dark"] :is(button,a)[style*="background:var(--teal)" i]{background:#157f87!important;border-color:#157f87!important;}
"""

SHARED_CSS = SHARED_CSS.replace('</style>\n"""'[:8], DARK_EXTRA + _dark_inline_rules() + '\n</style>', 1)

BLOCK_RE = re.compile(r'<style id="calc-shared-style">.*?</style>\n?', re.S)


def target_files(guide):
    if guide:
        return [os.path.join(GUIDES, guide)]
    return sorted(glob.glob(os.path.join(GUIDES, 'calc-*.html'))) + [os.path.join(GUIDES, 'ckd-dri-calculator.html')]


def patch(path, dry):
    t = open(path, encoding='utf-8').read()
    if BLOCK_RE.search(t):
        new = BLOCK_RE.sub(lambda m: SHARED_CSS, t, count=1)
    else:
        i = t.find('</style>')
        if i < 0:
            return 'no-style'
        i += len('</style>')
        if t[i:i + 1] == '\n':
            i += 1
        new = t[:i] + SHARED_CSS + t[i:]
    if new == t:
        return 'unchanged'
    if not dry:
        open(path, 'w', encoding='utf-8').write(new)
    return 'patched'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    a = ap.parse_args()
    counts = {}
    for f in target_files(a.guide):
        if not os.path.exists(f):
            print('missing', f); continue
        r = patch(f, a.dry_run)
        counts[r] = counts.get(r, 0) + 1
    print(('[DRY RUN] ' if a.dry_run else '') + 'Summary: ' + ', '.join(f'{k}={v}' for k, v in sorted(counts.items())))


if __name__ == '__main__':
    main()
