# -*- coding: utf-8 -*-
"""References for the Nephrology Fellow / Resident / Medical Intern track (APA 7), keyed ntr<module>_<n>.
Merged from parts/refs_NN.py (one file per module). Journal entries built from PubMed metadata, November 2026."""
import importlib.util as _u
from pathlib import Path as _P

REFS = {}
for _f in sorted((_P(__file__).resolve().parent / "parts").glob("refs_*.py")):
    _s = _u.spec_from_file_location("ntr_" + _f.stem, _f); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
    REFS.update(_m.REFS)
