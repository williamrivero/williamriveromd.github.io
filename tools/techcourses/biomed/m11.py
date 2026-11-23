# -*- coding: utf-8 -*-
"""Biomedical Technician Module 11. Content: deep_a.py / deep_b.py and legacy/; assembled by compose.py."""
import importlib.util
from pathlib import Path
_s = importlib.util.spec_from_file_location("bm_compose", Path(__file__).resolve().parent / "compose.py")
_c = importlib.util.module_from_spec(_s); _s.loader.exec_module(_c)
MODULE = _c.build("11")
