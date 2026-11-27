# -*- coding: utf-8 -*-
"""Validate APN module files. Usage: python3 check.py [NN ...]"""
import ast, importlib.util as u, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
REF = H.parent / "ref"
calcs = set(open(REF / "calcs.txt").read().split()); guides = set(open(REF / "guides.txt").read().split())
def load(p, n):
    s = u.spec_from_file_location(n, p); m = u.module_from_spec(s); s.loader.exec_module(m); return m
rows = json.load(open(H / "_rows.json"))
ids = sys.argv[1:] or [r[0] for r in rows]
bad = 0
for nn in ids:
    errs = []
    f = H / f"m{nn}.py"
    if not f.exists():
        print(f"m{nn}: MISSING"); bad += 1; continue
    ast.parse(f.read_text())
    try:
        M = load(f, f"m{nn}").MODULE
        R = load(H / "parts" / f"refs_{nn}.py", f"r{nn}").REFS
        F = load(H / "parts" / f"figs_{nn}.py", f"f{nn}").FIGS
        S = load(H / "parts" / f"sit_{nn}.py", f"s{nn}").SIT
    except Exception as e:
        print(f"m{nn}: LOAD ERROR {e}"); bad += 1; continue
    for k in ("image_alt", "objectives", "big", "case", "sections", "debrief", "skills", "quiz", "terms", "readings", "calcs"):
        if k not in M: errs.append(f"missing key {k}")
    blob = json.dumps(M)
    for key in set(re.findall(r"\[\[([a-z0-9_]+)\]\]", blob)):
        if key not in R: errs.append(f"unknown ref [[{key}]]")
    for key in R:
        if not key.startswith(f"apn{nn}_"): errs.append(f"ref key {key} must start apn{nn}_")
        if key not in blob: errs.append(f"ref {key} defined but never cited")
    for key in set(re.findall(r"\{\{fig(?:narrow)?:([a-z0-9_]+)", blob)):
        if key not in F: errs.append(f"unknown fig {key}")
    for key, v in F.items():
        if not key.startswith(f"apn{nn}_"): errs.append(f"fig key {key} must start apn{nn}_")
        if not v[0].startswith(f"attending-pediatric-nephrologist-{nn}-"): errs.append(f"fig file {v[0]} must start attending-pediatric-nephrologist-{nn}-")
        if "{{fig:" + key not in blob and "{{fignarrow:" + key not in blob: errs.append(f"fig {key} defined but not placed")
    q = M.get("quiz", [])
    if len(q) != 5: errs.append(f"quiz has {len(q)} items, need 5")
    for i, it in enumerate(q):
        if len(it) != 4 or len(it[1]) != 4 or not 0 <= it[2] <= 3: errs.append(f"quiz {i+1} malformed")
    if len(M.get("objectives", [])) != 3: errs.append("need 3 objectives")
    if len(M.get("case", {}).get("questions", [])) != 3: errs.append("case needs 3 questions")
    if len(M.get("debrief", [])) != 3: errs.append("debrief needs 3 paragraphs (one per case question)")
    for c in M.get("calcs", []):
        if c not in calcs and c != "calc-pediatric-nephrotic-course.html": errs.append(f"calc not on site: {c}")
    for g, _ in M.get("readings", []):
        if g not in guides and not g.startswith("attending-pediatric-nephrologist") and not g.startswith("attending-nephrologist"): errs.append(f"reading not on site: {g}")
    if len(S.get("scenarios", [])) < 3: errs.append("need >=3 situations")
    for s in S.get("scenarios", []):
        if len(s) != 5: errs.append("situation needs 5 fields")
    if len(S.get("tips", [])) < 3: errs.append("need >=3 tips")
    secs = M.get("sections", [])
    if len(secs) < 3: errs.append("need >=3 sections")
    for s in secs:
        if len(s) != 4: errs.append("section tuple must be (id, nav, h2, html)")
    if len(set(s[0] for s in secs)) != len(secs): errs.append("duplicate section ids")
    for w in ("colour", "behaviour", "haemo", "anaemi", "paediatr", "centre", "litre", "W Rivero", "oesoph", "oedema", "programme", "favour"):
        if w.lower() in blob.lower(): errs.append(f"British/forbidden spelling: {w}")
    words = len(re.sub(r"<[^>]+>", " ", blob).split())
    print(f"m{nn}: {'OK' if not errs else 'ERRORS'}  ~{words} words, {len(R)} refs, {len(F)} figs")
    for e in errs: print("    -", e)
    bad += bool(errs)
sys.exit(1 if bad else 0)
