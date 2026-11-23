#!/usr/bin/env python3
"""One-time asset preparation for the technical-workforce courses (idempotent).

    python3 tools/techcourses/prep_assets.py "/path/to/HD Technicians"

1. Copies each module's Study Guide / Self-Assessment / Answer Key into tools/techcourses/hd_technician/src/NN/.
2. From each Opener.png makes the circular hero (images/<slug>-vignette-hero.png + .webp) and a 640x360 card thumbnail.
3. Copies each Teaching Diagram.png to images/<slug>-teaching-diagram.png (+ .webp).
4. Builds assets/tech-course.js from assets/nursing-course.js (per-course storage key, single-explanation wording).
"""
import importlib.util, shutil, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
TC = ROOT / "tools" / "techcourses"
IMG = ROOT / "images"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def vignette(src, dst, focus=0.5, size=2048, circle=0.88):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    side = min(w, h)
    left = int(max(0, min(w - side, w * focus - side / 2)))
    sq = im.crop((left, 0, left + side, side)) if w >= h else im.crop((0, 0, side, side))
    d = int(size * circle)
    sq = sq.resize((d, d), Image.LANCZOS)
    mask = Image.new("L", (d * 2, d * 2), 0)
    ImageDraw.Draw(mask).ellipse((6, 6, d * 2 - 6, d * 2 - 6), fill=255)
    mask = mask.resize((d, d), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    canvas = Image.new("RGB", (size, size), "white")
    canvas.paste(sq, ((size - d) // 2, (size - d) // 2), mask)
    canvas.save(dst, optimize=True)
    canvas.save(dst.with_suffix(".webp"), quality=84, method=6)


def card(src, dst, focus=0.5):
    if str(src).endswith("-vignette-hero.png"):
        return hero_card(src, dst)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    tw = int(h * 16 / 9)
    if tw <= w:
        left = int(max(0, min(w - tw, w * focus - tw / 2)))
        im = im.crop((left, 0, left + tw, h))
    else:
        th = int(w * 9 / 16)
        top = (h - th) // 2
        im = im.crop((0, top, w, top + th))
    im.resize((640, 360), Image.LANCZOS).save(dst, quality=80, method=6)


def hero_card(src, dst):
    """640x360 card cut from inside the round picture of a circular vignette hero (no white corners)."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    r = 0.88 * min(w, h) / 2 * 0.97          # radius of the picture, less a small margin for the soft edge
    cw, ch = int(2 * r * 16 / (16 ** 2 + 9 ** 2) ** 0.5), int(2 * r * 9 / (16 ** 2 + 9 ** 2) ** 0.5)
    cx, cy = w // 2, h // 2
    im.crop((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2)).resize((640, 360), Image.LANCZOS).save(dst, quality=80, method=6)


def main():
    if len(sys.argv) > 1:
        src_root = Path(sys.argv[1]) / "Modules"
        c = load(TC / "hd_technician" / "course.py", "hdc")
        hub = c.COURSE["hub_slug"]
        for row in c.MODULES:
            mid = row["id"]; slug = f"{hub}-{mid}-{row['slug']}"
            s = src_root / mid
            d = TC / "hd_technician" / "src" / mid
            d.mkdir(parents=True, exist_ok=True)
            for f in ("Study Guide.md", "Self-Assessment.md", "Answer Key.md"):
                shutil.copyfile(s / f, d / f)
            focus = c.FOCUS.get(mid, 0.5) if hasattr(c, "FOCUS") else 0.5
            if (s / "Opener.png").exists():
                vignette(s / "Opener.png", IMG / f"{slug}-vignette-hero.png", focus)
                card(s / "Opener.png", IMG / f"{slug}-card.webp", focus)
            if (s / "Teaching Diagram.png").exists():
                t = IMG / f"{slug}-teaching-diagram.png"
                shutil.copyfile(s / "Teaching Diagram.png", t)
                Image.open(t).convert("RGB").save(t.with_suffix(".webp"), quality=88, method=6)
            print("prepared module", mid)
        first = c.MODULES[0]
        vignette(src_root / "01" / "Opener.png", IMG / f"{hub}-vignette-hero.png", 0.5)
    # card thumbnails cut from existing site illustrations (branch cards, natively authored modules)
    for pkg in ("hd_technician", "water_treatment", "biomed"):
        p = TC / pkg / "course.py"
        if not p.exists():
            continue
        c = load(p, pkg)
        for dst, src, focus in getattr(c, "CARD_CROPS", []):
            if (IMG / src).exists():
                try:
                    card(IMG / src, IMG / dst, focus)
                except OSError as e:   # e.g. a cloud-only file that has not been downloaded
                    print("  ! could not read", src, "-", e)
            else:
                print("  ! missing source image for card:", src)
    # quiz script
    js = (ROOT / "assets" / "nursing-course.js").read_text(encoding="utf-8")
    reps = [
        ("var KEY = 'rcm-nursing-progress';",
         "var KEY = 'rcm-course-' + (document.body.getAttribute('data-course') || 'tech') + '-progress';"),
        ("' Read the rationale under every option, including the ones you did not choose. ' +",
         "' Read the explanation under each best answer, including for the questions you got right. ' +"),
        ("done + ' of 12 self-assessments recorded on this device.';",
         "done + ' of ' + hub.querySelectorAll('a[data-module]').length + ' self-assessments recorded on this device.';"),
        ("/* Nephrology Nursing & Hemodialysis course", "/* Technical-workforce courses (built from nursing-course.js by tools/techcourses/prep_assets.py)"),
    ]
    for a, b in reps:
        if a not in js:
            sys.exit(f"nursing-course.js changed; expected text not found: {a[:50]}")
        js = js.replace(a, b)
    (ROOT / "assets" / "tech-course.js").write_text(js, encoding="utf-8")
    print("wrote assets/tech-course.js")


if __name__ == "__main__":
    main()
