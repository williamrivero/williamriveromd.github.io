#!/usr/bin/env python3
"""Validate the Renal Dietitian package (standard library only). Run from the repo root or this folder:
    python3 tools/techcourses/renal_dietitian/verify.py [--sitemap sitemap.xml]
Checks module schema against generate_tech_courses.py, citations, figure keys, situations, linked pages,
answer-key balance, American English spelling, and voice rules (VOICE.md)."""
import argparse, collections, importlib.util, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--sitemap"); args = ap.parse_args()
def load(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
C = load(HERE / "course.py", "c"); R = load(HERE / "refs.py", "r").REFS; F = load(HERE / "figs.py", "f").FIGS
SIT = load(HERE / "situations.py", "s").SITUATIONS; A = load(HERE / "abbr.py", "a").ABBR
err, warn = [], []
pos = collections.Counter(); nq = 0; minutes = 0
text_all = ""
for d in C.MODULES:
    mid = d["id"]; M = load(HERE / f"m{mid}.py", f"m{mid}").MODULE; minutes += d["minutes"]
    blob = repr(M); text_all += blob
    for k in ("objectives", "big", "case", "sections", "debrief", "skills", "quiz", "terms", "readings", "calcs", "image_alt"):
        if k not in M: err.append(f"m{mid}: missing {k}")
    if len(M["sections"]) < 3: err.append(f"m{mid}: fewer than 3 sections")
    for sec in M["sections"]:
        if not (isinstance(sec, tuple) and len(sec) == 4): err.append(f"m{mid}: section must be (id, nav, h2, html)")
    if not any(c for _, c in M["skills"]["items"]): err.append(f"m{mid}: no critical skill")
    if len(M["quiz"]) != 15: err.append(f"m{mid}: quiz has {len(M['quiz'])} items, expected 15")
    for i, q in enumerate(M["quiz"], 1):
        stem, opts, ans, why = q
        if len(opts) != 4 or len(set(opts)) != 4: err.append(f"m{mid} q{i}: need 4 distinct options")
        if ans not in range(4): err.append(f"m{mid} q{i}: bad answer index")
        pos[ans] += 1; nq += 1
    for k in re.findall(r"\[\[([a-z0-9_]+)\]\]", blob):
        if k not in R: err.append(f"m{mid}: unknown reference {k}")
    for k in re.findall(r"\{\{fig:([a-z0-9_]+)", blob):
        if k not in F: err.append(f"m{mid}: unknown figure {k}")
    if mid not in SIT: err.append(f"m{mid}: no situations")
    links = [f for f, _ in M["readings"]] + list(M["calcs"])
    if args.sitemap:
        site = set(re.findall(r"guides/([a-z0-9-]+)", Path(args.sitemap).read_text()))
        for f in links:
            if f[:-5] not in site: err.append(f"m{mid}: linked page not on site: {f}")
for k in re.findall(r"\[\[([a-z0-9_]+)\]\]", repr(C.COURSE)):
    if k not in R: err.append(f"course: unknown reference {k}")
unused = set(R) - set(re.findall(r"\[\[([a-z0-9_]+)\]\]", text_all + repr(C.COURSE)))
if unused: warn.append(f"unused references: {sorted(unused)}")
# answer balance: no position should carry more than 40% of keys
for p, n in pos.items():
    if n / nq > 0.40: warn.append(f"answer position {'ABCD'[p]} carries {n}/{nq} keys; run quizutil.balance()")
plain = re.sub(r"<[^>]+>", " ", text_all + repr(C.COURSE) + repr(SIT))
brit = re.findall(r"\b(licence|defence|practise|analyse|haemo\w*|anaem\w*|oedema|diarrhoea|paediat\w*|colour\w*|behaviour\w*|centre\w*|litre\w*|fibre\w*|programme|judgement|ageing|whilst|amongst|modelled|labelled|counselled|\w+isation|organis\w+|individualis\w+|recognis\w+|minimis\w+)\b", plain, re.I)
if brit: err.append(f"British spellings: {sorted(set(brit))}")
for w in ("honestly", "genuinely", "straightforward", "don't", "can't", "won't", "isn't", "doesn't"):
    if re.search(r"\b" + re.escape(w) + r"\b", plain, re.I): err.append(f"voice: avoid '{w}'")
print(f"{len(C.MODULES)} modules, {minutes} study minutes, {nq} questions, {len(R)} references, {len(F)} figures, "
      f"{sum(len(v['scenarios']) for v in SIT.values())} situations, {len(A)} abbreviations")
print("answer positions:", {"ABCD"[k]: v for k, v in sorted(pos.items())})
for w in warn: print("WARN", w)
for e in err: print("ERROR", e)
sys.exit(1 if err else 0)
