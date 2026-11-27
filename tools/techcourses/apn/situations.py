# -*- coding: utf-8 -*-
"""Real situations and field tips for the Attending Pediatric Nephrologist modules, seen from the attending's place.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters). All fictional.
Merged from parts/sit_NN.py."""
import importlib.util as _u
from pathlib import Path as _P

SITUATIONS = {}
for _f in sorted((_P(__file__).resolve().parent / "parts").glob("sit_*.py")):
    _s = _u.spec_from_file_location("apn_" + _f.stem, _f); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
    SITUATIONS[_f.stem.split("_")[1]] = _m.SIT
