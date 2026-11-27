# -*- coding: utf-8 -*-
"""Figures for the Attending Pediatric Nephrologist track. key: (file in images/, alt text, caption).
Merged from parts/figs_NN.py. A figure renders only once its image exists in images/."""
import importlib.util as _u
from pathlib import Path as _P

FIGS = {}
for _f in sorted((_P(__file__).resolve().parent / "parts").glob("figs_*.py")):
    _s = _u.spec_from_file_location("apn_" + _f.stem, _f); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
    FIGS.update(_m.FIGS)
