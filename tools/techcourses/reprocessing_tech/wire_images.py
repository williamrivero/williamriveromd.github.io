#!/usr/bin/env python3
"""Checks which Reprocessing Technician modules have all their images in the production folder, and wires them.

    python3 tools/techcourses/reprocessing_tech/wire_images.py --status            # report completeness only
    python3 tools/techcourses/reprocessing_tech/wire_images.py --wire 01 02 hub    # copy + derive assets for those units

A module is complete when its hero (<slug>-vignette-hero.png) and both figures (figs.py, as .webp or .png) exist.
Wiring copies the hero (.png + .webp) and figures (.webp) into images/, and cuts the 640x360 card thumbnail from the hero;
the hub also gets images/academy/landing/<hub>.webp (960x540). Run from the repo root. Source folder: SRC below or --src."""
import argparse, importlib.util, shutil, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SRC = Path("/Volumes/Storage/Renal Care Academy/Reprocessing Technician/images")
IMG = ROOT / "images"


def load(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


C = load(HERE / "course.py", "rt_course"); F = load(HERE / "figs.py", "rt_figs").FIGS
HUB = C.HUB


def units():
    u = {"hub": {"hero": f"{HUB}-vignette-hero", "figs": []}}
    for row in C._ROWS:
        mid, slug = row[0], row[1]
        u[mid] = {"hero": f"{HUB}-{mid}-{slug}-vignette-hero",
                  "figs": [v[0][:-5] for k, v in F.items() if k.startswith(f"rt{mid}_")]}
    return u


def have(src, base):
    return any((src / f"{base}{ext}").exists() for ext in (".png", ".webp"))


def card(hero_png, out, size=(640, 360), inner=0.62):
    im = Image.open(hero_png).convert("RGB"); w, h = im.size
    side = int(min(w, h) * inner); cx, cy = w // 2, h // 2
    box_w, box_h = side, int(side * size[1] / size[0])
    crop = im.crop((cx - box_w // 2, cy - box_h // 2, cx + box_w // 2, cy + box_h // 2)).resize(size, Image.LANCZOS)
    crop.save(out, quality=84, method=6)


def to_webp(src, dst):
    if src.suffix == ".webp":
        shutil.copy2(src, dst)
    else:
        Image.open(src).convert("RGB").save(dst, quality=86, method=6)


def wire(src, uid, u):
    hb = u["hero"]
    png = src / f"{hb}.png"
    if png.exists():
        shutil.copy2(png, IMG / png.name)
    web = src / f"{hb}.webp"
    to_webp(web if web.exists() else png, IMG / f"{hb}.webp")
    heropng = IMG / png.name if png.exists() else IMG / f"{hb}.webp"
    if uid == "hub":
        (IMG / "academy" / "landing").mkdir(parents=True, exist_ok=True)
        card(heropng, IMG / "academy" / "landing" / f"{HUB}.webp", (960, 540))
        card(heropng, IMG / f"{HUB}-card.webp")
    else:
        card(heropng, IMG / f"{HUB}-{uid}-card.webp")
    for fb in u["figs"]:
        s = src / f"{fb}.webp"
        to_webp(s if s.exists() else src / f"{fb}.png", IMG / f"{fb}.webp")
    print("wired", uid)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--src", default=str(SRC)); ap.add_argument("--status", action="store_true")
    ap.add_argument("--wire", nargs="*", default=[]); a = ap.parse_args(); src = Path(a.src); U = units()
    for uid, u in U.items():
        need = [u["hero"]] + u["figs"]; miss = [b for b in need if not have(src, b)]
        print(f"{uid}: {'COMPLETE' if not miss else 'missing ' + ', '.join(miss)}")
    for uid in a.wire:
        u = U[uid]; need = [u["hero"]] + u["figs"]
        if any(not have(src, b) for b in need):
            sys.exit(f"{uid} is not complete")
        wire(src, uid, u)


if __name__ == "__main__":
    main()
