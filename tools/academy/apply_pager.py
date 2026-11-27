"""Editorial module pager on every Academy module page (Dr. Rivero, Nov 27 2026: "Option B", chosen over teal cards). Idempotent.

Rewrites the generator's two-card <div class="nc-nextprev"> (previous / next) into:
  * a module rail: one segment per module in the track (modules before this one teal, this one orange), with
    "Module N of T" and "K modules to go" / "Last module";
  * a navy rule, a quiet "previous" link on the left, a hairline divider, and the "next" link on the right with a
    large teal module numeral (a check mark for "Series complete" / "Finish") and an orange "Continue" underline on hover.
The outer div keeps class nc-nextprev and the links keep nc-np, so print hiding and the Listen player's skip list
still apply. Labels from the generator (<small>) are kept as the kicker lines. Track size = files named
<prefix>-NN-*.html with the same prefix. CSS lives in <style id="academy-pager"> in each page's head; colors follow
the page variables (--teal, --text, --border, --white), so Light, Dim, Dark and E-paper all work.
Runs after every publish (publish_academy.py). Never hand-edit academy/*.html.

    python3 tools/academy/apply_pager.py           # patch all module pages
    python3 tools/academy/apply_pager.py --check   # exit 1 if any page is stale
"""
import html as H
import re
import sys
from pathlib import Path

ACADEMY = Path(__file__).resolve().parents[2] / "academy"

CSS = """<style id="academy-pager">
.nc-nextprev.rca-pager{display:block;--pg-num:var(--teal);--pg-go:#c55a11;--pg-rule:var(--navy,#1f3864);--pg-done:var(--teal);--pg-cur:#c55a11;
  border:1px solid var(--border);border-radius:16px;background:var(--white);padding:24px 26px 26px;margin:24px 0 12px;}
html[data-theme="dark"] .nc-nextprev.rca-pager{--pg-go:#f0915a;--pg-cur:#f0915a;--pg-rule:var(--text);}
.rca-pager .rca-rail{display:flex;gap:5px;margin:0 0 9px !important;padding:0 !important;list-style:none;}
.rca-pager .rca-rail li{flex:1;height:6px;border-radius:3px;background:var(--border);margin:0 !important;padding:0;}
.rca-pager .rca-rail li.is-done{background:var(--pg-done);opacity:.85;}
.rca-pager .rca-rail li.is-current{background:var(--pg-cur);}
.rca-pager .rca-rail.is-dense{gap:3px;}
.rca-status{display:flex;justify-content:space-between;gap:12px;margin:0 0 20px;font:600 12px/1.3 Inter,Manrope,system-ui,sans-serif;letter-spacing:.04em;color:var(--text-muted);}
.rca-row{display:grid;grid-template-columns:minmax(0,1fr) 1px minmax(0,2fr);gap:26px;border-top:2px solid var(--pg-rule);padding-top:20px;}
.rca-sep{background:var(--border);}
.rca-pager .nc-np{display:block;border:0;border-radius:6px;background:none;padding:0;text-align:left;color:var(--text);text-decoration:none;}
.rca-pager .nc-np:hover{border-color:transparent;}
.rca-pager .nc-np small{display:flex;align-items:center;gap:6px;margin:0 0 7px;font:700 11px/1.3 Inter,Manrope,system-ui,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted);}
.rca-t{display:block;font-family:Manrope,Inter,system-ui,sans-serif;font-weight:700;color:var(--text);text-wrap:balance;transition:color .2s;}
.rca-prev .rca-t{font-size:16px;line-height:1.4;}
.rca-prev:hover .rca-t{color:var(--teal);}
.rca-pager .rca-next{display:flex;gap:18px;align-items:flex-start;}
.rca-num{flex:none;min-width:1.2em;font:700 56px/.9 Manrope,Inter,system-ui,sans-serif;letter-spacing:-.03em;color:var(--pg-num);font-variant-numeric:tabular-nums;}
.rca-num svg{display:block;width:50px;height:50px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
.rca-body{min-width:0;flex:1;}
.rca-next .rca-t{font-size:20px;line-height:1.3;}
.rca-go{display:inline-flex;align-items:center;gap:6px;margin-top:11px;padding-bottom:2px;border-bottom:2px solid transparent;
  font:700 13px/1.3 Inter,Manrope,system-ui,sans-serif;color:var(--pg-go);transition:border-color .2s,gap .2s;}
.rca-next:hover .rca-go,.rca-next:focus-visible .rca-go{border-color:var(--pg-go);gap:10px;}
.rca-pager .nc-np:focus-visible{outline:2px solid var(--teal);outline-offset:5px;}
@media (max-width:640px){
  .nc-nextprev.rca-pager{padding:20px 18px 22px;}
  .rca-row{grid-template-columns:1fr;gap:18px;}
  .rca-sep{display:none;}
  .rca-pager .rca-next{order:-1;padding-bottom:16px;border-bottom:1px solid var(--border);border-radius:0;}
  .rca-num{font-size:44px;} .rca-num svg{width:40px;height:40px;}
  .rca-next .rca-t{font-size:18px;}
}
@media (prefers-reduced-motion:reduce){.rca-pager *{transition:none !important;}}
</style>"""

STYLE_RE = re.compile(r'\n?<style id="academy-pager">.*?</style>', re.S)
OLD_RE = re.compile(r'<div class="nc-nextprev">\s*(<a class="nc-np"[^>]*>.*?</a>)\s*(<a class="nc-np nc-np-next"[^>]*>.*?</a>)\s*</div>', re.S)
A_RE = re.compile(r'<a ([^>]*)><small>(.*?)</small>(.*?)</a>', re.S)
MOD_RE = re.compile(r'^(.+)-(\d{2})-[^/]*\.html$')
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m7.5 12.5 3 3 6-6.5"/></svg>'


def track_sizes():
    sizes = {}
    for p in ACADEMY.glob("*.html"):
        m = MOD_RE.match(p.name)
        if m:
            sizes.setdefault(m.group(1), set()).add(int(m.group(2)))
    return {k: max(v) for k, v in sizes.items()}


def build(name, prev_a, next_a, sizes):
    m = MOD_RE.match(name)
    prefix, cur = m.group(1), int(m.group(2))
    total = max(sizes.get(prefix, cur), cur)
    pa, na = A_RE.match(prev_a), A_RE.match(next_a)
    if not (pa and na):
        return None
    p_attrs, p_label, p_title = pa.groups()
    n_attrs, n_label, n_title = na.groups()
    p_attrs = p_attrs.replace('class="nc-np"', 'class="nc-np rca-prev"')
    n_attrs = n_attrs.replace('class="nc-np nc-np-next"', 'class="nc-np nc-np-next rca-next"')
    nm = re.search(r'Module\s+(\d+)', n_label)
    if nm:
        num, kicker, go = f"{int(nm.group(1)):02d}", "Next module", "Continue"
    else:
        plain = re.sub(r'\s*(→|&rarr;)\s*$', '', n_label).strip()
        href = re.search(r'href="([^"]*)"', n_attrs)
        href = href.group(1) if href else ""
        go = "Take the final check" if ("exam" in href or "trainer" in href) else "Return to course home"
        num, kicker = CHECK, plain
    segs = "".join('<li class="is-current"></li>' if i == cur else ('<li class="is-done"></li>' if i < cur else "<li></li>")
                   for i in range(1, total + 1))
    left = total - cur
    togo = "Last module" if left <= 0 else (f"{left} module to go" if left == 1 else f"{left} modules to go")
    dense = " is-dense" if total > 20 else ""
    return (f'<div class="nc-nextprev rca-pager">\n'
            f'    <ol class="rca-rail{dense}" aria-hidden="true">{segs}</ol>\n'
            f'    <p class="rca-status"><span>Module {cur} of {total}</span><span>{togo}</span></p>\n'
            f'    <div class="rca-row" role="navigation" aria-label="Module navigation">\n'
            f'      <a {p_attrs}><small>{p_label}</small><span class="rca-t">{p_title.strip()}</span></a>\n'
            f'      <span class="rca-sep" aria-hidden="true"></span>\n'
            f'      <a {n_attrs}><span class="rca-num" aria-hidden="true">{num}</span>'
            f'<span class="rca-body"><small>{kicker}</small><span class="rca-t">{n_title.strip()}</span>'
            f'<span class="rca-go">{go} <span aria-hidden="true">&rarr;</span></span></span></a>\n'
            f'    </div>\n  </div>')


def patch(text, name, sizes):
    m = OLD_RE.search(text)
    if m:
        new = build(name, m.group(1), m.group(2), sizes)
        if new:
            text = text[:m.start()] + new + text[m.end():]
    if 'class="nc-nextprev rca-pager"' in text:
        text = STYLE_RE.sub("", text)
        text = text.replace("</head>", CSS + "\n</head>", 1)
    return text


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    check = "--check" in argv
    sizes = track_sizes()
    changed = 0
    for p in sorted(ACADEMY.glob("*.html")):
        if not MOD_RE.match(p.name):
            continue
        old = p.read_text(encoding="utf-8")
        if "nc-nextprev" not in old:
            continue
        new = patch(old, p.name, sizes)
        if new != old:
            changed += 1
            if not check:
                p.write_text(new, encoding="utf-8")
    print(("stale: " if check else "pager: patched ") + f"{changed} module page(s)")
    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
