# -*- coding: utf-8 -*-
"""Real situations and field notes for the Disaster Preparedness and Response, merged from sit_NN.py.
Each scenario: (title, what you see, what is likely going on, what to do, why it matters). All are fictional composites."""
import importlib.util as _u
from pathlib import Path as _P

SITUATIONS = {}
for _f in sorted(_P(__file__).resolve().parent.glob("sit_[0-9][0-9].py")):
    _s = _u.spec_from_file_location("dp_" + _f.stem, _f); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
    SITUATIONS.update(_m.SIT)
