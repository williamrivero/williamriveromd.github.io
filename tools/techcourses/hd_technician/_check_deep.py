# -*- coding: utf-8 -*-
"""Validate a deep_NN.py additions file. Usage: python3 _check_deep.py deep_01.py [more files]"""
import html
import os
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
os.environ["TC_LENIENT"] = "1"


def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


figs = load(HERE.parent / "figs.py", "figs_chk")
FIGS = max((v for k, v in vars(figs).items() if isinstance(v, dict) and not k.startswith("__")), key=len)
REFS = load(HERE.parent / "shared.py", "shared_chk").REFS
course = load(HERE / "course.py", "course_chk")
KINDS = {"fig", "fignarrow", "flow", "cards", "plain", "key", "stop", "formula"}
BAD_IDS = {"quiz", "case", "skills", "situations", "debrief", "objectives", "bigpicture", "reading"}


def check(path):
    probs = []
    mid = re.search(r"(\d\d)", Path(path).name).group(1)
    add = load(HERE / path, "deep_chk_" + mid).ADD
    e = course._E[mid]
    nsec = len(e.get("navs", []))
    used = set(re.findall(r"\{\{fig(?:narrow)?:(\w+)", " ".join(
        [e.get("big", "")] + list(e.get("pre", {}).values()) + list(e.get("post", {}).values()))))
    words, ids, newfigs = 0, set(), []
    for item in add.get("extra", []):
        if len(item) != 5:
            probs.append("extra item is not a 5-tuple"); continue
        after, xid, nav, h2, body = item
        if not (isinstance(after, int) and 1 <= after <= max(nsec, 1)):
            probs.append(f"{xid}: after={after} outside 1..{nsec}")
        if not re.fullmatch(r"[a-z]+", xid) or xid in BAD_IDS or xid.startswith("part") or xid in ids:
            probs.append(f"bad or duplicate id: {xid}")
        ids.add(xid)
        if len(html.unescape(nav)) > 22:
            probs.append(f"{xid}: nav label longer than 22 characters")
        if re.search(r"[^\x00-\x7F]", body + nav + h2):
            probs.append(f"{xid}: non-ASCII character {set(re.findall(r'[^\x00-\x7F]', body + nav + h2))}")
        if re.search(r"<h[1-6]", body):
            probs.append(f"{xid}: heading tag inside section")
        if "{{" in re.sub(r"\{\{(.+?)\}\}", "", body, flags=re.S) or body.count("{{") != body.count("}}"):
            probs.append(f"{xid}: unbalanced macro braces")
        for m in re.finditer(r"\{\{(.+?)\}\}", body, flags=re.S):
            kind, _, rest = m.group(1).partition(":")
            if kind not in KINDS:
                probs.append(f"{xid}: unknown macro {kind}")
            if kind in ("fig", "fignarrow"):
                k = rest.partition("|")[0].strip()
                newfigs.append(k)
                if k not in FIGS:
                    probs.append(f"{xid}: unknown figure key {k}")
                if k in used:
                    probs.append(f"{xid}: figure {k} already used in this module")
            if kind in ("flow", "cards"):
                parts = [x.strip() for x in rest.split("|")]
                for it in parts[1:]:
                    if "::" not in it or it.count("::") != 1:
                        probs.append(f"{xid}: {kind} item without exactly one '::' -> {it[:50]}")
                if len(parts) < 3:
                    probs.append(f"{xid}: {kind} with fewer than 2 items")
        for r in re.findall(r"\[\[([^\]]+)\]\]", body):
            if r not in REFS:
                probs.append(f"{xid}: unknown reference key {r}")
        for tag in ("table", "tr", "td", "th", "thead", "tbody", "div", "p", "ul", "li", "strong"):
            if len(re.findall(rf"<{tag}[ >]", body)) != body.count(f"</{tag}>"):
                probs.append(f"{xid}: unbalanced <{tag}>")
        words += len(re.sub(r"<[^>]+>|\{\{\w+:|\}\}|\||::", " ", html.unescape(body)).split())
    if len(newfigs) > 2 or len(set(newfigs)) != len(newfigs):
        probs.append("more than 2 figures or a repeated figure")
    answers = []
    for q in add.get("quiz_extra", []):
        if len(q) != 4 or len(q[1]) != 4 or not (0 <= q[2] < 4):
            probs.append(f"bad quiz item: {str(q[0])[:50]}")
        else:
            answers.append(q[2])
        if re.search(r"[^\x00-\x7F]", " ".join([q[0], q[3]] + list(q[1]))):
            probs.append(f"non-ASCII in quiz: {q[0][:40]}")
    if answers and max(answers.count(i) for i in range(4)) > max(3, len(answers) // 2 + 1):
        probs.append(f"correct answers too often in the same position: {answers}")
    for s in add.get("skills_extra", []):
        if len(s) != 2 or not isinstance(s[1], bool):
            probs.append("bad skills item")
    n = len(add.get("extra", []))
    print(f"{path}: {n} sections, {words} words, {len(add.get('quiz_extra', []))} quiz, "
          f"{len(add.get('skills_extra', []))} skills, answer positions {answers}")
    if not (3 <= n <= 5):
        probs.append("need 3 to 5 sections")
    if words < 1500:
        probs.append("fewer than 1,500 words of new lesson text")
    for p in probs:
        print("  PROBLEM:", p)
    return not probs


if __name__ == "__main__":
    ok = all([check(a) for a in sys.argv[1:]])
    print("OK" if ok else "FIX THE PROBLEMS ABOVE")
    sys.exit(0 if ok else 1)
