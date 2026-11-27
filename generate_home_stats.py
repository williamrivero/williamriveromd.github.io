#!/usr/bin/env python3
"""Homepage "By the numbers" strip (Nov 27 2026, Dr. Rivero).

Writes the block between <!-- HOME-PROOF-START --> and <!-- HOME-PROOF-END --> at the end of the
"Why you can trust it" section of index.html. Every number is counted from the site itself:

  references   <li> items in every guide/calculator References accordion (guides/*.html)
  drug index   generic medicine pages and PH FDA product registrations (the Drug Index hero chips)
  academy      tracks, subtracks and modules (the Academy landing chips) + quiz/exam questions
               (.nc-q items in academy module pages and final-exam banks)
  freshness    guides first published, or modified (JSON-LD dateModified), in the current Manila month

Two numbers are live and appear only once there is data: certificates of completion
(GET /api/certs?stats=1, a count with no names) and the reader rating (GET /api/reviews, approved
ratings only). Each shows only at 5 or more. The section is far below the first screen, so revealing
them causes no visible layout shift.

  python3 generate_home_stats.py            # update index.html
  python3 generate_home_stats.py --check    # exit 1 if the block is out of date
"""
import argparse
import datetime
import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
START, END = "<!-- HOME-PROOF-START -->", "<!-- HOME-PROOF-END -->"
MIN_LIVE = 5


def num(s):
    return int(s.replace(",", ""))


def counts():
    manila = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
    month = manila.strftime("%Y-%m")
    refs = fresh = 0
    for f in glob.glob(str(ROOT / "guides" / "*.html")):
        s = open(f, encoding="utf-8").read()
        m = re.search(r'<details[^>]*class="[^"]*\bref-acc\b[^"]*".*?</details>', s, re.S)
        if m:
            refs += len(re.findall(r"<li\b", m.group(0)))
        pub = re.search(r'article:published_time" content="(\d{4}-\d\d)', s)
        mod = re.search(r'"dateModified":\s*"(\d{4}-\d\d)', s)
        if (pub and pub.group(1) == month) or (mod and mod.group(1) == month):
            fresh += 1
    d = (ROOT / "drugs" / "index.html").read_text(encoding="utf-8")
    generics = num(re.search(r'class="dd-chip">([\d,]+) generics', d).group(1))
    products = num(re.search(r'class="dd-chip">([\d,]+) PH products', d).group(1))
    a = (ROOT / "academy" / "index.html").read_text(encoding="utf-8")
    chip = lambda label: num(re.search(r'<span class="acad-stat"><b>([\d,]+)</b> ' + label + "</span>", a).group(1))
    questions = 0
    for f in glob.glob(str(ROOT / "academy" / "*.html")):
        name = Path(f).name
        if re.search(r"-\d\d-", name) or name.endswith("final-exam.html"):
            questions += len(re.findall(r'class="nc-q[ "]', open(f, encoding="utf-8").read()))
    return dict(refs=refs, fresh=fresh, month=manila.strftime("%B"), generics=generics, products=products,
                tracks=chip("tracks"), subtracks=chip("subtracks"), modules=chip("modules"), questions=questions)


def block(c):
    f = lambda n: f"{n:,}"
    cell = lambda n, label, sub="", extra="": (
        f'<div class="hp-cell"{extra}><div class="hp-num">{n}</div><div class="hp-label">{label}</div>'
        + (f'<div class="hp-sub">{sub}</div>' if sub else "") + "</div>")
    cells = [
        cell(f(c["refs"]), "references cited", "in the guides and calculators"),
        cell(f(c["generics"]), "medicines in the Drug Index", f'{f(c["products"])} FDA Philippines product registrations'),
        cell(f(c["modules"]), "Renal Care Academy modules",
             f'{c["tracks"]} tracks · {c["subtracks"]} subtracks · {f(c["questions"])} quiz and exam questions'),
        cell(f(c["fresh"]), f'guides added or updated in {c["month"]}', "kept current as guidelines change"),
        cell("", "certificates of completion earned", "in the Renal Care Academy", ' id="hp-certs" hidden'),
        cell("", "average reader rating", "", ' id="hp-rating" hidden'),
    ]
    apps = [("/drugs/#dd-app", "Dosis", "drugs"), ("/guides/calculators#calc-app", "Calculo", "calculators"),
            ("/academy/#schola", "Schola", "Academy")]
    return (START + """
<style id="home-proof-css">
.hp{grid-column:1/-1;margin-top:8px}
.hp-head{font-size:12px;font-weight:700;letter-spacing:.18em;color:#1A6B72;margin:0 0 16px}
.hp-grid{display:grid;grid-template-columns:1fr;gap:2px;background:#EEE9DE;border:1px solid #EEE9DE;border-radius:20px;overflow:hidden}
.hp-cell{background:#fff;padding:clamp(20px,2.6vw,28px)}
@media (min-width:560px){.hp-grid{grid-template-columns:repeat(2,1fr)}}
@media (min-width:900px){.hp-grid{grid-template-columns:repeat(4,1fr)}
.hp-grid:has(#hp-certs:not([hidden])),.hp-grid:has(#hp-rating:not([hidden])){grid-template-columns:repeat(5,1fr)}
.hp-grid:has(#hp-certs:not([hidden])):has(#hp-rating:not([hidden])){grid-template-columns:repeat(3,1fr)}}
.hp-cell[hidden]{display:none}
.hp-num{font-family:'Newsreader',serif;font-weight:400;font-size:clamp(34px,4.4vw,48px);line-height:1;color:#1A6B72;letter-spacing:-.02em}
.hp-label{font-size:14.5px;font-weight:700;color:#16294a;margin-top:8px}
.hp-sub{font-size:13.5px;line-height:1.45;color:#566072;margin-top:4px}
.hp-foot{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px 24px;margin-top:18px}
.hp-apps{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:14.5px;color:#4C5768}
.hp-apps a{display:inline-flex;align-items:center;gap:6px;padding:7px 13px;border:1px solid #DCE6E4;border-radius:999px;background:#fff;color:#16294a;font-weight:600;text-decoration:none}
.hp-apps a:hover{border-color:#1A6B72;color:#1A6B72}
.hp-apps small{font-weight:500;color:#566072}
.hp-free{font-size:15px;font-weight:700;color:#16294a;letter-spacing:.02em}
</style>
<div class="hp reveal" aria-label="By the numbers">
  <p class="hp-head">BY THE NUMBERS</p>
  <div class="hp-grid">
    """ + "\n    ".join(cells) + """
  </div>
  <div class="hp-foot">
    <div class="hp-apps"><span>3 apps that work offline:</span>""" + "".join(
        f'<a href="{h}">{n} <small>{w}</small></a>' for h, n, w in apps) + """</div>
    <div class="hp-free">Free · no account · no ads</div>
  </div>
</div>
<script>
(function(){
  var MIN = """ + str(MIN_LIVE) + """;
  function show(id, n, label, sub){ var el = document.getElementById(id); if (!el) return;
    el.querySelector('.hp-num').textContent = n; if (label) el.querySelector('.hp-label').textContent = label;
    if (sub) { var s = el.querySelector('.hp-sub'); if (!s) { s = document.createElement('div'); s.className = 'hp-sub'; el.appendChild(s); } s.textContent = sub; }
    el.hidden = false; }
  fetch('/api/certs?stats=1').then(function(r){ return r.ok ? r.json() : null; }).then(function(d){
    if (d && d.issued >= MIN) show('hp-certs', d.issued.toLocaleString('en-US'), d.issued === 1 ? 'certificate of completion earned' : null);
  }).catch(function(){});
  fetch('/api/reviews').then(function(r){ return r.ok ? r.json() : null; }).then(function(d){
    if (d && d.count >= MIN && d.average) show('hp-rating', d.average.toFixed(1) + ' of 5', null,
      'from ' + d.count.toLocaleString('en-US') + ' readers who rated the site');
  }).catch(function(){});
})();
</script>
""" + END)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    s = INDEX.read_text(encoding="utf-8")
    new_block = block(counts())
    if START in s:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: new_block, s, flags=re.S)
    else:  # first run: last item inside the Why you can trust it section's grid
        anchor = re.search(r'(<section class="rcm-evidence">.*?)(\n  </div>\n</section>)', s, re.S)
        new = s[:anchor.end(1)] + "\n    " + new_block + s[anchor.end(1):]
    if a.check:
        sys.exit(0 if new == s else 1)
    if new != s:
        INDEX.write_text(new, encoding="utf-8")
    print("home stats:", counts())


if __name__ == "__main__":
    main()
