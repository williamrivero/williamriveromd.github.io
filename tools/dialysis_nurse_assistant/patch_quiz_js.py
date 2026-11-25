#!/usr/bin/env python3
"""Let assets/nursing-course.js use a per-course progress key (idempotent).

A page whose <html> carries data-nc-store="<key>" stores optional progress under that key; every other page keeps the
original 'rcm-nursing-progress' key, so existing courses behave exactly as before. Used by the Dialysis Nurse Assistant /
PCA subtrack (key rcm-dna-progress-v1)."""
from pathlib import Path
p = Path(__file__).resolve().parents[2] / "assets" / "nursing-course.js"
s = p.read_text(encoding="utf-8")
if "data-nc-store" in s:
    print("nursing-course.js already supports data-nc-store"); raise SystemExit
old = "  var KEY = 'rcm-nursing-progress';\n"
new = ("  var KEY = (document.documentElement && document.documentElement.getAttribute('data-nc-store')) || 'rcm-nursing-progress';"
       "  /* per-course key via <html data-nc-store> */\n")
assert old in s, "KEY anchor not found"
p.write_text(s.replace(old, new, 1), encoding="utf-8")
print("patched nursing-course.js (data-nc-store)")
