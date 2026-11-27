#!/usr/bin/env python3
"""Academy interactive branching cases (Dr. Rivero, Nov 27 2026). Idempotent.

Case data lives in data/academy-cases/<id>.json (one file per case; "page" names the academy module it belongs
to). Schema, in short:

    { "id", "page", "title", "decisions": N, "intro": "<p>…</p>", "start": "n1",
      "monitor": {time, bp, hr, spo2, …, "rhythm": normal|peaked|st|irregular|wide, "rhythmLabel"},
      "labels": {key: "Monitor label"}, "monitorOrder": [keys],
      "nodes": { "n1": {"scene", "prompt", "short", "vitals", "choices": [
                     {"grade": best|ok|poor|harmful, "text", "feedback", "then", "vitals", "next"}]},
                 "end": {"end": true, "title", "text", "vitals"} },
      "debrief": "<h4>…</h4><ul>…</ul>" }

Every decision node should sit on every path (weaker choices show their consequence in "then" and rejoin), so
each run scores the same number of decisions. Clinical content follows the module text and defers to the unit
protocol and the attending nephrologist; it needs Dr. Rivero's sign-off before publishing.

This patcher:
  1. fingerprints assets/academy-cases.js as assets/academy-cases.<hash>.js (older copies pruned; _headers caches
     /assets/academy-cases.* immutable);
  2. writes an "Interactive case" section (id "sim", between RCM-CASES markers) just before the module's
     Skills checklist (else before the self-assessment), with each case's JSON in a
     <script type="application/json" id="rcm-case-<id>">, plus a nav-strip pill;
  3. tags the script on pages that have a case, and removes all of it from pages that no longer do.

Run after every publish (publish_academy.py does, before build_schola.py, so the script joins the offline list).

    python3 tools/academy/apply_cases.py             # apply
    python3 tools/academy/apply_cases.py --dry-run   # report only
"""
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
DATA = ROOT / "data" / "academy-cases"
NAME = "academy-cases"

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')
BLOCK_RE = re.compile(r"<!-- RCM-CASES-START -->.*?<!-- RCM-CASES-END -->\n\n?", re.S)
PILL_RE = re.compile(r'\n?<a class="nav-pill" href="#sim" data-rcm-sim>[^<]*</a>')
GRADES = {"best", "ok", "poor", "harmful"}


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def validate(c, src):
    errs = []
    for k in ("id", "page", "title", "intro", "start", "nodes"):
        if k not in c:
            errs.append(f"missing {k}")
    nodes = c.get("nodes", {})
    if c.get("start") not in nodes:
        errs.append("start node not found")
    decision = [k for k, n in nodes.items() if n.get("choices")]
    if c.get("decisions") and c["decisions"] != len(decision):
        errs.append(f"decisions={c['decisions']} but {len(decision)} decision nodes")
    for k, n in nodes.items():
        if n.get("end"):
            continue
        ch = n.get("choices") or []
        if len(ch) < 2:
            errs.append(f"{k}: needs 2+ choices")
        if not any(x.get("grade") == "best" for x in ch):
            errs.append(f"{k}: no best choice")
        for x in ch:
            if x.get("grade") not in GRADES:
                errs.append(f"{k}: bad grade {x.get('grade')}")
            nxt = x.get("next") or n.get("next")
            if nxt not in nodes:
                errs.append(f"{k}: next '{nxt}' not found")
            if not x.get("feedback"):
                errs.append(f"{k}: a choice has no feedback")
    if not any(n.get("end") for n in nodes.values()):
        errs.append("no end node")
    if errs:
        raise SystemExit(f"{src.name}: " + "; ".join(errs))


def load_cases():
    by_page = {}
    for f in sorted(DATA.glob("*.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        validate(c, f)
        by_page.setdefault(c["page"], []).append(c)
    return by_page


def section(cases):
    parts = ["<!-- RCM-CASES-START -->",
             '<section class="section rcm-case-wrap" id="sim">',
             '  <div class="section-tag">Interactive case &middot; fictional</div>']
    if len(cases) == 1:
        parts.append(f"  <h2>Interactive case: {html.escape(cases[0]['title'])}</h2>")
    else:
        parts.append("  <h2>Interactive cases</h2>")
    parts.append("  <p>Work through a shift one decision at a time. The bedside monitor changes with what you choose. "
                 "After each choice you see why it is, or is not, the best move; after a weaker one you can try again or carry on "
                 "and see where it leads. Your first choice at each step is scored. The score stays on this device and nothing "
                 "is sent anywhere. Your unit&rsquo;s protocol and the attending nephrologist come first in real practice.</p>")
    for c in cases:
        if len(cases) > 1:
            parts.append(f"  <h3>{html.escape(c['title'])}</h3>")
        data = json.dumps(c, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        parts.append(f'  <div class="rcm-case" data-case="{html.escape(c["id"])}"><noscript><p style="padding:14px">'
                     "This interactive case needs JavaScript. The opening case and case review in this module cover the same ground.</p></noscript></div>")
        parts.append(f'  <script type="application/json" id="rcm-case-{html.escape(c["id"])}">{data}</script>')
    parts += ["</section>", "<!-- RCM-CASES-END -->"]
    return "\n".join(parts) + "\n"


def main():
    dry = "--dry-run" in sys.argv
    by_page = load_cases()
    hashed = fingerprint(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed, missing = 0, [p for p in by_page if not (ACADEMY / p).exists()]
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        text = PILL_RE.sub("", BLOCK_RE.sub("", TAG_RE.sub("", old)))
        cases = by_page.get(f.name)
        if cases:
            anchor = '<section class="section" id="skills"'
            if anchor not in text:
                anchor = '<section class="section" id="quiz"'
            if anchor not in text:
                print(f"  ! {f.name}: no skills or quiz section, case skipped")
            else:
                i = text.index(anchor)
                text = text[:i] + section(cases) + "\n" + text[i:]
                for pill in ('<a class="nav-pill" href="#skills">', '<a class="nav-pill" href="#quiz">'):
                    if pill in text:
                        j = text.index(pill)
                        text = text[:j] + '<a class="nav-pill" href="#sim" data-rcm-sim>Interactive case</a>\n' + text[j:]
                        break
                k = text.rfind("</body>")
                text = text[:k] + tag + "\n" + text[k:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    for p in missing:
        print(f"  ! case page not found: academy/{p}")
    n = sum(len(v) for v in by_page.values())
    print(f"academy cases ({hashed}): {n} case(s) on {len(by_page)} page(s); {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
