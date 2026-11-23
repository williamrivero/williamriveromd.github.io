# -*- coding: utf-8 -*-
"""Builds the twelve Biomedical Technician modules from deep_a.py / deep_b.py plus sections reused from legacy/ (the
original six modules). Each mNN.py is a two-line stub that calls build("NN")."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


NEW = {}
NEW.update(_load(HERE / "deep_a.py", "bm_deep_a").NEW)
NEW.update(_load(HERE / "deep_b.py", "bm_deep_b").NEW)
_LEG = {}


def legacy(mid):
    if mid not in _LEG:
        _LEG[mid] = _load(HERE / "legacy" / f"m{mid}.py", f"bm_legacy_{mid}").MODULE
    return _LEG[mid]


def _pick(value, field):
    """('L', id) -> that field of a legacy module; anything else is used as written."""
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "L":
        return legacy(value[1])[field]
    return value


def build(mid):
    n = NEW[mid]
    base = dict(legacy(n["keep"])) if "keep" in n else {}
    m = {}
    for f in ("objectives", "big", "terms", "readings", "calcs", "image_alt"):
        m[f] = n.get(f, base.get(f, [] if f in ("objectives", "terms", "readings", "calcs") else ""))
    for f in ("case", "debrief", "skills"):
        m[f] = _pick(n.get(f, base.get(f)), f)
    secs = []
    for s in n["sections"]:
        if s[0] == "L" and len(s) == 3:
            hit = [x for x in legacy(s[1])["sections"] if x[0] == s[2]]
            if not hit:
                raise SystemExit(f"biomed module {mid}: legacy section {s[1]}/{s[2]} not found")
            secs.append(hit[0])
        else:
            secs.append(s)
    ids = [s[0] for s in secs]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"biomed module {mid}: duplicate section ids {ids}")
    m["sections"] = secs
    quiz = []
    for lid, idxs in n.get("quiz_keep", []):
        quiz += [legacy(lid)["quiz"][i] for i in idxs]
    m["quiz"] = quiz + list(n.get("quiz", []))
    return m
