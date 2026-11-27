# -*- coding: utf-8 -*-
"""Validate NTR module files. Usage: python3 check.py [NN ...]   (run from anywhere)"""
import ast, importlib.util as u, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
calcs = set(open(H / "calcs.txt").read().split())
guides = set(open(H / "guides.txt").read().split())
academy = set(open(H / "academy.txt").read().split())
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
        P = json.load(open(H / "parts" / f"imgplan_{nn}.json"))
    except Exception as e:
        print(f"m{nn}: LOAD ERROR {e}"); bad += 1; continue
    for k in ("image_alt", "objectives", "big", "case", "sections", "debrief", "skills", "quiz", "terms", "readings", "calcs"):
        if k not in M: errs.append(f"missing key {k}")
    blob = json.dumps(M)
    for key in set(re.findall(r"\[\[([a-z0-9_]+)\]\]", blob)):
        if key not in R: errs.append(f"unknown ref [[{key}]]")
    for key in R:
        if not key.startswith(f"ntr{nn}_"): errs.append(f"ref key {key} must start ntr{nn}_")
        if "[[" + key + "]]" not in blob: errs.append(f"ref {key} defined but never cited")
        if "<em>" not in R[key] or ("http" not in R[key]): errs.append(f"ref {key} not APA-like (needs <em> and a link)")
    for key in set(re.findall(r"\{\{fig(?:narrow)?:([a-z0-9_]+)", blob)):
        if key not in F: errs.append(f"unknown fig {key}")
    for key, v in F.items():
        if not key.startswith(f"ntr{nn}_"): errs.append(f"fig key {key} must start ntr{nn}_")
        if not v[0].startswith(f"nephrology-trainee-{nn}-"): errs.append(f"fig file {v[0]} must start nephrology-trainee-{nn}-")
        if "{{fig:" + key not in blob and "{{fignarrow:" + key not in blob: errs.append(f"fig {key} defined but not placed")
    if set(F) != {x.get("key") for x in P.get("figures", [])}: errs.append("imgplan figures keys must match FIGS keys")
    for k in ("hero", "figures", "card"):
        if k not in P: errs.append(f"imgplan missing {k}")
    if len(F) < 2: errs.append("need >=2 figures")
    q = M.get("quiz", [])
    if len(q) != 5: errs.append(f"quiz has {len(q)} items, need 5")
    for i, it in enumerate(q):
        if len(it) != 4 or len(it[1]) != 4 or not 0 <= it[2] <= 3: errs.append(f"quiz {i+1} malformed")
    obj = M.get("objectives", [])
    if len(obj) != 3: errs.append("need 3 objectives")
    else:
        for o, lab in zip(obj, ("Intern:", "Resident:", "Fellow:")):
            if not o.startswith(f"<strong>{lab}</strong>"): errs.append(f"objective must start <strong>{lab}</strong>")
    if len(M.get("case", {}).get("questions", [])) != 3: errs.append("case needs 3 questions")
    if len(M.get("debrief", [])) != 3: errs.append("debrief needs 3 paragraphs (one per case question)")
    for c in M.get("calcs", []):
        if c not in calcs: errs.append(f"calc not on site: {c}")
    if not M.get("calcs"): errs.append("no calculators linked")
    for g, _ in M.get("readings", []):
        if g not in guides and g not in academy: errs.append(f"reading not on site: {g}")
    if len(S.get("scenarios", [])) < 3: errs.append("need >=3 situations")
    for s in S.get("scenarios", []):
        if len(s) != 5: errs.append("situation needs 5 fields")
    if len(S.get("tips", [])) < 3: errs.append("need >=3 tips")
    secs = M.get("sections", [])
    if len(secs) < 4: errs.append("need >=4 sections")
    for s in secs:
        if len(s) != 4: errs.append("section tuple must be (id, nav, h2, html)")
    if len(set(s[0] for s in secs)) != len(secs): errs.append("duplicate section ids")
    if "In children" not in blob and nn not in ("01", "33", "34", "35"): errs.append("no 'In children' panel")
    for w in ("colour", "behaviour", "haemo", "anaemi", "paediatr", "centre", "litre", "W Rivero", "oesoph", "oedema", "programme", "favour", "organis", "recognis", "analyse"):
        if w.lower() in blob.lower(): errs.append(f"British/forbidden spelling: {w}")
    words = len(re.sub(r"<[^>]+>", " ", blob).split())
    if words < 3200: errs.append(f"too short: ~{words} words (target 4,000-5,500)")
    print(f"m{nn}: {'OK' if not errs else 'ERRORS'}  ~{words} words, {len(R)} refs, {len(F)} figs")
    for e in errs: print("    -", e)
    bad += bool(errs)
sys.exit(1 if bad else 0)
