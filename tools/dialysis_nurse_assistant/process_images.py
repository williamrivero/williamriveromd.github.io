#!/usr/bin/env python3
"""Place the Dialysis Nurse Assistant / PCA images produced from docs/dialysis-nurse-assistant/GPT-IMAGE-PROMPTS.md.

    python3 tools/dialysis_nurse_assistant/process_images.py "<folder with the PNGs>" [--dry-run]

For every file named in image-manifest.json that is present in the folder:
  hero      -> images/<stem>.png + .webp, and images/<stem minus -vignette-hero>-card.webp (640 x 360 module tile)
  figure    -> images/<stem>.png + .webp
  og-track-art -> images/academy/og-art/<slug>.png, then build_academy_og.py --only <slug> --patch
  og-calculator -> images/<file> + .webp (the toolkit builder points og:image at it)
  landing-tile  -> images/academy/landing/<slug>.webp, 960 x 540 from the center band
Afterwards run: generate_dialysis_nurse_assistant.py --calc --patch, generate_rg_thumbs.py, patch_rg_card_thumbs.py, patch_og_images.py.
"""
import json, shutil, subprocess, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "images"
SLUG = "dialysis-nurse-assistant"


def webp(src, dst, max_w=None):
    im = Image.open(src).convert("RGB")
    if max_w and im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(dst, "WEBP", quality=84, method=6)


def card(src, dst, w=640, h=360):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    ch = round(W * h / w)
    top = max(0, (H - ch) // 2)
    im.crop((0, top, W, top + ch)).resize((w, h), Image.LANCZOS).save(dst, "WEBP", quality=82, method=6)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src_dir, dry = Path(sys.argv[1]), "--dry-run" in sys.argv
    man = json.loads((ROOT / "docs" / SLUG / "image-manifest.json").read_text(encoding="utf-8"))
    done, missing = [], []
    for item in man:
        f = src_dir / item["file"]
        if not f.exists():
            missing.append(item["file"]); continue
        k = item["kind"]
        if dry:
            done.append(f"{k}: {f.name}"); continue
        if k in ("hero", "figure", "og-calculator"):
            shutil.copy2(f, IMG / f.name)
            webp(f, IMG / (f.stem + ".webp"), 2048 if k == "hero" else 1792)
            if k == "hero":
                card(f, IMG / (f.stem.replace("-vignette-hero", "") + "-card.webp"))
        elif k == "og-track-art":
            d = IMG / "academy" / "og-art"; d.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, d / f.name)
            r = subprocess.run([sys.executable, "build_academy_og.py", "--art", str(d), "--only", SLUG, "--patch"], cwd=ROOT, capture_output=True, text=True)
            print((r.stdout or r.stderr).strip()[-300:])
        elif k == "landing-tile":
            d = IMG / "academy" / "landing"; d.mkdir(parents=True, exist_ok=True)
            card(f, d / f"{SLUG}.webp", 960, 540)
        done.append(f"{k}: {f.name}")
    print(f"{'would place' if dry else 'placed'} {len(done)} image(s); {len(missing)} not in the folder yet")
    for x in done:
        print("  ", x)


if __name__ == "__main__":
    main()
