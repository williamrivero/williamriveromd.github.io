#!/usr/bin/env python3
"""Install the course figures and write tools/nursing/content/figures.py (where each figure goes).

    python3 tools/nursing/build_figures.py [source_folder]

Copies <file>.png and <file>.webp from the source folder (default: ~/Documents/Nephrology Nursing/Module images)
into images/, reads pixel sizes, and maps each figure in docs/nursing-course/image-prompts-manifest.json to its
page and section. The hub hero (H-0) is installed but not listed: the generator shows a hero automatically when
images/<slug>-vignette-hero.png exists. Re-run after replacing any figure.
"""
import json, re, shutil, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Documents/Nephrology Nursing/Module images"
MAN = []
for _m in ("image-prompts-manifest.json", "image-prompts-addendum-manifest.json", "image-prompts-addendum2-manifest.json",
           "image-prompts-addendum3-manifest.json", "image-prompts-addendum4-manifest.json"):
    _p = ROOT / "docs/nursing-course" / _m
    if _p.exists():
        MAN += json.loads(_p.read_text(encoding="utf-8"))
OUT = ROOT / "tools/nursing/content/figures.py"

figs, missing = [], []
for f in MAN:
    name = f["file"].replace("images/", "")
    stem = name.rsplit(".", 1)[0]
    png, webp = SRC / f"{stem}.png", SRC / f"{stem}.webp"
    if not png.exists():
        missing.append(name); continue
    for p in (png, webp):
        if p.exists() and p.resolve() != (ROOT / "images" / p.name).resolve():
            shutil.copy2(p, ROOT / "images" / p.name)
    if f["id"] == "H-0" or f["id"].endswith("-H0") or "hero" in f["placement"].lower():
        continue  # heroes: the generator shows images/<slug>-vignette-hero.png automatically
    w, h = Image.open(png).size
    pl = f["placement"]
    if pl.startswith("Hub"):
        page = "hub"
    elif pl.startswith("Educator"):
        page = "educator"
    else:
        page = re.match(r"Module (\d+)", pl).group(1).zfill(2)
    sec = re.search(r"section `([^`]+)`", pl).group(1)
    figs.append({"id": f["id"], "page": page, "section": sec, "stem": stem, "w": w, "h": h,
                 "alt": f["alt"], "caption": f["caption"]})

lines = ["# -*- coding: utf-8 -*-",
         '"""Course figures: written by tools/nursing/build_figures.py from the image manifest. Do not hand-edit;',
         'change the manifest (or the caption here, then keep it in the manifest too) and re-run."""',
         "FIGURES = ["]
for x in figs:
    lines.append("    " + json.dumps(x, ensure_ascii=False) + ",")
lines.append("]")
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"installed {len(figs)} figures plus heroes; listed {len(figs)} in {OUT.relative_to(ROOT)}")
if missing:
    print("MISSING in source folder:", missing)
