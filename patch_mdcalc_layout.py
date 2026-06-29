#!/usr/bin/env python3
"""patch_mdcalc_layout.py — restructure standalone calculator pages into the
MDCalc-style reading order.

Target order inside <main>:
    1. Instructions  (always-visible banner, right under the title)
    2. ▸ When to Use        (collapsible)
    3. ▸ Pearls & Pitfalls  (collapsible)
    4. ▸ Why Use It         (collapsible, omitted if the page has no #why)
    5. Calculator interface + result   (the #calculator section, unchanged)
    6. ▸ Next Steps         (collapsible)
    7. ▸ Evidence & References (collapsible — Formula + references merged)
    8. Advice block         (the existing disclaimer, always visible)

The page's existing sections (#when #why #pearls #instructions #formula
#evidence #calculator) are reused verbatim — only their order and chrome
change. A small dedicated <style> block (.mdc-*) is injected once; it is kept
separate from the master CSS so patch_master_css.py never strips it.

Idempotent: a page already carrying `class="mdc-acc"` is skipped.

Usage:
    python3 patch_mdcalc_layout.py [--dry-run] [--guide calc-foo.html]
"""
import re
import sys
import glob
import os

MDC_STYLE = """<style id="mdc-style">
/* MDCalc-style layout for standalone calculator pages */
.mdc-instructions{background:var(--teal-light);border-left:3px solid var(--teal);border-radius:8px;padding:14px 18px 12px;margin:22px 0 18px;}
.mdc-instr-label{display:block;font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--teal);margin-bottom:4px;}
.mdc-instructions ol,.mdc-instructions ul{margin:0 0 0 1.1em;padding:0;}
.mdc-instructions p{margin:0;}
.mdc-acc{border:1px solid var(--border);border-radius:10px;margin:10px 0;background:var(--white);}
.mdc-acc>summary{cursor:pointer;list-style:none;padding:15px 20px;font-family:'Lora',serif;font-weight:600;color:var(--navy);font-size:1.06rem;display:flex;align-items:center;justify-content:space-between;gap:12px;}
.mdc-acc>summary::-webkit-details-marker{display:none;}
.mdc-acc>summary::after{content:"+";font-size:1.5rem;line-height:1;color:var(--teal);font-weight:400;flex:none;}
.mdc-acc[open]>summary::after{content:"\\2212";}
.mdc-acc>summary:hover{background:var(--bg);border-radius:10px;}
.mdc-acc[open]>summary{border-bottom:1px solid var(--border);border-radius:10px 10px 0 0;}
.mdc-acc-body{padding:6px 20px 18px;}
.mdc-acc-body>h3.mdc-sub{font-family:'Lora',serif;font-size:1rem;color:var(--navy);margin:16px 0 8px;}
.mdc-acc-body>h3.mdc-sub:first-child{margin-top:6px;}
.mdc-acc#nextsteps>summary{color:var(--teal);}
/* Calculate buttons — the .calc-btn/.calc-run/.tool-btn classes had no master-CSS
   rule, so they rendered as tiny default browser buttons. Make them prominent and
   theme-stable (solid teal + white, fixed hex so dark mode doesn't wash them out). */
.calc-btn,.calc-run,.tool-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;margin:16px 0 6px;padding:13px 30px;background:#1a6b72;color:#fff;border:none;border-radius:10px;font-family:'DM Sans',sans-serif;font-size:1.02rem;font-weight:700;letter-spacing:.01em;cursor:pointer;box-shadow:0 2px 10px rgba(26,107,114,.30);transition:background .18s,box-shadow .18s,transform .05s;}
.calc-btn:hover,.calc-run:hover,.tool-btn:hover{background:#155a60;box-shadow:0 5px 16px rgba(26,107,114,.40);}
.calc-btn:active,.calc-run:active,.tool-btn:active{transform:translateY(1px);box-shadow:0 2px 8px rgba(26,107,114,.30);}
@media(max-width:600px){.calc-btn,.calc-run,.tool-btn{width:100%;}}
/* Legacy .tool-* widget system — a few decision-aid calculators were lifted with
   this guide-specific markup but without its CSS, so the inputs rendered bare.
   Restyle here (CSS variables for dark-mode safety; radio options as chips). */
.tool-box{background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:22px 24px;margin:16px 0;}
.tool-box>h3{font-family:'Lora',serif;font-size:1.05rem;font-weight:600;color:var(--navy);margin:0 0 6px;}
.tool-box .tool-sub{font-size:13px;color:var(--text-muted);margin:0 0 18px;line-height:1.5;}
.two-col-inputs{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
@media(max-width:520px){.two-col-inputs{grid-template-columns:1fr;}}
.tool-label{display:block;font-size:13px;font-weight:600;color:var(--text);margin:14px 0 5px;}
.tool-input,.tool-select{width:100%;padding:10px 12px;border:1px solid var(--border);border-radius:8px;font-family:'DM Sans',sans-serif;font-size:14px;color:var(--text);background:var(--white);box-sizing:border-box;}
.tool-select{cursor:pointer;}
.tool-input:focus,.tool-select:focus{outline:none;border-color:var(--teal);box-shadow:0 0 0 3px rgba(26,107,114,.13);}
.radio-group{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 2px;}
.radio-item{display:inline-flex;align-items:center;gap:7px;padding:9px 16px;border:1px solid var(--border);border-radius:8px;font-size:14px;color:var(--text-mid);cursor:pointer;background:var(--white);transition:border-color .15s;}
.radio-item:hover{border-color:var(--teal);}
.radio-item input{accent-color:var(--teal);margin:0;}
.tool-result{display:none;margin-top:18px;padding:16px 20px;border-radius:10px;border:1px solid var(--border);background:var(--white);}
.tool-result.show{display:block;}
html[data-theme="dark"] .tool-box>h3{color:var(--text);}
/* Non-standard unit-toggle markup (.ut-btn / .unit-toggle-row / .unit-toggle-lbl
   / .ut-sep) that a few calculators used instead of the master .unit-btn system —
   style them to match the polished segmented control. */
.unit-toggle-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:2px 0 16px;}
.unit-toggle-lbl{font-size:12px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:.04em;}
.ut-sep{width:1px;height:18px;background:var(--border);display:inline-block;}
.ut-btn{padding:6px 14px;border:1px solid var(--border);background:var(--white);color:var(--text-mid);font-family:'DM Sans',sans-serif;font-size:.85rem;font-weight:600;cursor:pointer;border-radius:6px;transition:border-color .15s,background .15s,color .15s;}
.ut-btn:hover{border-color:var(--teal);}
.ut-btn.active{background:#1a6b72;border-color:#1a6b72;color:#fff;}
/* Accessible hero cross-links: high-contrast white text + gold underline (link
   affordance not by colour alone), visible focus ring, larger hit area. The
   hero is dark in both themes, so white works throughout. */
.hero-xlink{color:#fff;font-weight:600;text-decoration:underline;text-decoration-color:var(--gold-light);text-decoration-thickness:1.5px;text-underline-offset:3px;border-radius:6px;padding:2px 4px;}
.hero-xlink:hover{color:var(--gold-light);}
.hero-xlink:focus-visible{outline:2px solid var(--gold-light);outline-offset:2px;}
/* Dark mode: --navy is NOT remapped, so every element the master CSS colors with
   var(--navy) renders dark-on-dark. Some source guides also shipped an older
   master CSS missing these overrides — so recolor them all here (this block is
   injected last and applies to all calculator pages regardless of CSS version). */
html[data-theme="dark"] .mdc-acc>summary,
html[data-theme="dark"] .mdc-acc-body>h3.mdc-sub,
html[data-theme="dark"] .section h2,
html[data-theme="dark"] .section h3,
html[data-theme="dark"] .alert-body h4,
html[data-theme="dark"] .feature-card h4,
html[data-theme="dark"] .step-body h4,
html[data-theme="dark"] .ladder-body h4,
html[data-theme="dark"] .tl-body h4,
html[data-theme="dark"] .disclaimer strong,
html[data-theme="dark"] .lab-table td:first-child,
html[data-theme="dark"] .drug-table td:first-child,
html[data-theme="dark"] .compare-cell strong,
html[data-theme="dark"] .cart-cell strong,
html[data-theme="dark"] .calc-metric-card .cmv,
html[data-theme="dark"] .n-val,
html[data-theme="dark"] .n-value{color:var(--text)!important;}
html[data-theme="dark"] .calc-verdict-text,
html[data-theme="dark"] .calc-action-text{color:var(--text-mid)!important;}
html[data-theme="dark"] .mdc-acc#nextsteps>summary{color:var(--teal)!important;}
html[data-theme="dark"] .mdc-instructions{border-left-color:var(--teal);}
</style>
"""

NEXT_STEPS = """<p><strong>Use the result to support — not replace — clinical judgment.</strong></p>
<ul style="margin:8px 0 0 1.1em;padding:0;line-height:1.8;">
<li>Interpret the value against the targets shown in the calculator and the Evidence section below, in the context of the full clinical picture.</li>
<li>Trend serial measurements rather than acting on a single result; confirm abnormal or unexpected values before changing management.</li>
<li>Apply the relevant KDIGO / specialty-guideline threshold and document the indication.</li>
<li>Escalate or refer to nephrology when results are out of range, rapidly changing, or discordant with the clinical picture — and discuss the implications with the patient.</li>
</ul>"""

NAV = """<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#instructions">Instructions</a>
<a class="nav-pill" href="#when">When to Use</a>
<a class="nav-pill" href="#pearls">Pearls &amp; Pitfalls</a>
<a class="nav-pill" href="#calculator">Calculator</a>
<a class="nav-pill" href="#nextsteps">Next Steps</a>
<a class="nav-pill" href="#evidence">Evidence</a>
</div>
</nav>"""


def section(html, sid):
    """Return (full_match, inner) for <section ... id="sid">…</section>."""
    m = re.search(r'<section class="section" id="%s">(.*?)</section>' % sid,
                  html, re.S)
    return (m.group(0), m.group(1)) if m else (None, None)


def body_of(inner):
    """Strip the leading section-tag div and first <h2> from a section body."""
    if inner is None:
        return None
    b = re.sub(r'^\s*<div class="section-tag">.*?</div>\s*', '', inner, count=1, flags=re.S)
    b = re.sub(r'^\s*<h2>.*?</h2>\s*', '', b, count=1, flags=re.S)
    return b.strip()


def acc(aid, label, body):
    return ('<details class="mdc-acc" id="%s">\n<summary>%s</summary>\n'
            '<div class="mdc-acc-body">\n%s\n</div>\n</details>') % (aid, label, body)


def transform(path, dry):
    h = open(path, encoding="utf-8").read()
    if 'class="mdc-acc"' in h:
        return False  # already transformed

    instr = body_of(section(h, 'instructions')[1])
    when = body_of(section(h, 'when')[1])
    why = body_of(section(h, 'why')[1])
    pearls = body_of(section(h, 'pearls')[1])
    formula = body_of(section(h, 'formula')[1])
    evidence = body_of(section(h, 'evidence')[1])
    calc_full = section(h, 'calculator')[0]
    if not (instr and when and pearls and formula and evidence and calc_full):
        print("  SKIP (missing core sections):", os.path.basename(path))
        return False

    # advice block = the existing trailing disclaimer
    adv = re.search(r'<div class="disclaimer">.*?</div>', h, re.S)
    advice = adv.group(0) if adv else ''

    parts = []
    parts.append('<div class="mdc-instructions"><span class="mdc-instr-label">Instructions</span>\n%s\n</div>' % instr)
    parts.append(acc('when', 'When to Use', when))
    parts.append(acc('pearls', 'Pearls &amp; Pitfalls', pearls))
    if why:
        parts.append(acc('why', 'Why Use It', why))
    parts.append(calc_full)
    parts.append(acc('nextsteps', 'Next Steps', NEXT_STEPS))
    ev_body = ('<h3 class="mdc-sub">Formula &amp; Equations</h3>\n%s\n'
               '<h3 class="mdc-sub">Evidence &amp; References</h3>\n%s' % (formula, evidence))
    parts.append(acc('evidence', 'Evidence &amp; References', ev_body))
    if advice:
        parts.append(advice)

    new_main = '<main class="container">\n\n' + "\n\n".join(parts) + '\n\n</main>'
    h2 = re.sub(r'<main\b[^>]*>.*?</main>', lambda _m: new_main, h, count=1, flags=re.S)

    # swap nav strip
    h2 = re.sub(r'<nav class="nav-strip">.*?</nav>', lambda _m: NAV, h2, count=1, flags=re.S)

    # inject the dedicated style once, just before </head>
    if 'id="mdc-style"' not in h2:
        h2 = h2.replace('</head>', MDC_STYLE + '</head>', 1)

    if h2 == h:
        print("  no change:", os.path.basename(path))
        return False
    if not dry:
        open(path, 'w', encoding="utf-8").write(h2)
    print(("  would patch " if dry else "  patched ") + os.path.basename(path))
    return True


def main():
    dry = '--dry-run' in sys.argv
    one = None
    if '--guide' in sys.argv:
        one = sys.argv[sys.argv.index('--guide') + 1]
    root = os.path.join(os.path.dirname(__file__), 'guides')
    files = [os.path.join(root, one)] if one else sorted(glob.glob(os.path.join(root, 'calc-*.html')))
    n = 0
    for f in files:
        if transform(f, dry):
            n += 1
    print(f"{'(dry-run) ' if dry else ''}{n} file(s) patched")


if __name__ == "__main__":
    main()
