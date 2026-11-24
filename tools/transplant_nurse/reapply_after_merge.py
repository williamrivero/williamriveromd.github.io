#!/usr/bin/env python3
"""Re-apply the Transplant Nurse edits to shared files after taking the upstream version (Python 3.9+).
Usage: python3 reapply_after_merge.py <repo-root> <tn-commit>
Reads the TN-SUBTRACK blocks from the given commit and inserts them into the current upstream files."""
import re, subprocess, sys
from pathlib import Path
root, tn = Path(sys.argv[1]), sys.argv[2]
START, END = "<!-- TN-SUBTRACK-START -->", "<!-- TN-SUBTRACK-END -->"
BLK = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
def show(path):
    return subprocess.run(["git", "show", f"{tn}:{path}"], cwd=root, capture_output=True, text=True, check=True).stdout
def first(s, *cands):
    for c in cands:
        if c and c in s:
            return c
    return None
out = []
pages = {
    "academy/nephrology-nursing-11-transplantation-special-populations.html": (['<section class="section" id="case">'],
        ('<a class="nav-pill" href="#case">', '<a class="nav-pill" href="#transplant-nurse">Transplant Nurse subtrack</a>\n')),
    "academy/nephrology-nursing.html": (['<section class="section" id="progression">'],
        ('<a class="nav-pill" href="#progression">', '<a class="nav-pill" href="#specialty">Specialty subtracks</a>\n')),
    "academy/index.html": (['    <a class="tc-branch" href="hemodialysis-technician.html">', '    <a class="tc-branch" href="dialysis-technician.html">'], None),
}
for rel, (anchors, pill) in pages.items():
    mine = show(rel)
    blocks = BLK.findall(mine)
    p = root / rel
    s = BLK.sub("", p.read_text(encoding="utf-8"))
    a = first(s, *anchors)
    if rel == "academy/index.html" and not a:
        m = re.search(r'^ *<a class="tc-branch" href="[^"]*technician[^"]*">', s, re.M)
        a = m.group(0) if m else None
    if not a or not blocks:
        out.append(f"FAIL {rel}: anchor={bool(a)} blocks={len(blocks)}"); continue
    s = s.replace(a, blocks[0] + a, 1)
    if pill and pill[1].split('">')[0] not in s:
        s = s.replace(pill[0], pill[1] + pill[0], 1)
    if rel == "academy/index.html" and 'href="transplant-nurse.html"><span class="acad-track-ico"' not in s:
        m = re.search(r'^    <a class="acad-track" href="transplant-nurse\.html">.*?</a>\n', mine, re.M | re.S)
        n = re.search(r'^    <a class="acad-track" href="[^"]*technician[^"]*">', s, re.M)
        if m and n:
            s = s.replace(n.group(0), m.group(0) + n.group(0), 1)
        else:
            out.append(f"WARN {rel}: nav track link not placed")
    p.write_text(s, encoding="utf-8")
    out.append(f"ok {rel} (anchor: {a.strip()[:60]})")
# generator hooks
HOOK = {"generate_nursing_course.py": ("r", "        "), "generate_tech_courses.py": ("r2", "        ")}
for rel, (var, ind) in HOOK.items():
    p = root / rel; s = p.read_text(encoding="utf-8")
    if "generate_transplant_nurse" in s:
        out.append(f"ok {rel} (hook present)"); continue
    m = re.search(r'\n( +)r = subprocess\.run\(\[sys\.executable, str\(ROOT / "tools" / "academy" / "publish_academy\.py"\)\][^\n]*\n\1print\(\(r\.stdout or r\.stderr\)\.strip\(\)\)\n', s)
    if not m:
        out.append(f"FAIL {rel}: publish hook anchor not found"); continue
    i = m.group(1)
    hook = (f'{i}if (ROOT / "generate_transplant_nurse.py").exists():   # keep the Transplant Nurse entry links\n'
            f'{i}    {var} = subprocess.run([sys.executable, "-c", "import generate_transplant_nurse as T; print(\'transplant-nurse entry links:\', T.wire_parent())"], cwd=ROOT, capture_output=True, text=True)\n'
            f'{i}    print(({var}.stdout or {var}.stderr).strip()[-300:])\n')
    s = s[:m.end()] + hook + s[m.end():]
    p.write_text(s, encoding="utf-8"); out.append(f"ok {rel} (hook added)")
p = root / "tools/academy/publish_academy.py"; s = p.read_text(encoding="utf-8")
if '"transplant-nurse"' not in s:
    s2 = re.sub(r'(PREFIXES = \([^)]*?)(,?\s*)\)', lambda m: m.group(1) + ', "transplant-nurse")', s, count=1)
    p.write_text(s2, encoding="utf-8"); out.append("ok publish_academy.py (prefix added)" if s2 != s else "FAIL publish_academy.py")
# calculators index card
p = root / "guides/calculators.html"; s = p.read_text(encoding="utf-8")
if 'href="calc-tacrolimus-level-check.html"' not in s:
    mine = show("guides/calculators.html")
    m = re.search(r'<a class="related-card" href="calc-tacrolimus-level-check\.html">.*?</a>\n', mine, re.S)
    a = '<a class="related-card has-thumb" href="calc-dgf-risk.html">'
    if m and a in s:
        p.write_text(s.replace(a, m.group(0) + a, 1), encoding="utf-8"); out.append("ok calculators.html (card added)")
    else:
        out.append("FAIL calculators.html card")
print("\n".join(out))
