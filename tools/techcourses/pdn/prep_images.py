#!/usr/bin/env python3
"""Place the Pediatric Dialysis Nurse track images produced in ChatGPT (Stage 2 of the image pipeline).

Drop the PNGs (track art in a subfolder named og-art/), named exactly as the FILE NAME stems in
docs/tech-courses/pediatric-dialysis-nurse-image-prompts.md, into images/incoming/pediatric-dialysis-nurse/ (any depth; .png/.jpg/.webp), then:

    python3 tools/techcourses/pdn/prep_images.py            # place everything found
    python3 tools/techcourses/pdn/prep_images.py --dry-run  # list what would be written
    python3 tools/techcourses/pdn/prep_images.py --report   # which planned images exist / are missing

Outputs:
  <slug>-vignette-hero          -> images/<stem>.png (<=1536 px) + .webp
  pediatric-dialysis-nurse-NN-<figure>     -> images/<stem>.webp + .png (<=1792 px wide)
  *-card                        -> images/<stem>.webp 640 x 360; the course card also writes images/academy/landing/pediatric-dialysis-nurse.webp 960 x 540
  *-og, pediatric-dialysis-nurse-toolkit   -> images/og/<stem>.jpg 1200 x 630, <= 300 KB
  og-art/pediatric-dialysis-nurse          -> images/academy/og-art/pediatric-dialysis-nurse.webp 1536 x 1024
"""
import argparse, importlib.util, io, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
IMG = ROOT / "images"
INBOX = IMG / "incoming" / "pediatric-dialysis-nurse"
HUB = "pediatric-dialysis-nurse"
ART = "academy/og-art/pediatric-dialysis-nurse"


def crop_to(im, ratio):
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio); x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(w / ratio); y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def rgb(im):
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[-1]); return bg
    return im.convert("RGB")


def fit(im, maxw):
    return im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS) if im.width > maxw else im


def jpeg_under(im, path, limit=300 * 1024):
    for q in (88, 84, 80, 76, 72, 68, 64, 60):
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= limit:
            break
    path.write_bytes(buf.getvalue())


def planned():
    spec = importlib.util.spec_from_file_location("swplan", Path(__file__).resolve().parent / "image_plan.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    stems = {f"{HUB}-vignette-hero", f"{HUB}-card", f"{HUB}-og", f"{HUB}-toolkit", ART}
    for n, s in m.SLUGS.items():
        stems |= {f"{HUB}-{n}-{s}-vignette-hero", f"{HUB}-{n}-card", f"{HUB}-{n}-{s}-og"}
    for k in m.FA:
        stems.add(m.FIGS[k][0][:-5])
    for k in m.FB:
        stems.add(m.fb_file(k)[:-5])
    return stems


def place(src, dry):
    stem = src.stem
    im = rgb(Image.open(src))
    if "og-art" in str(src):
        im = crop_to(im, 3 / 2).resize((1536, 1024), Image.LANCZOS)
        out = [(IMG / "academy" / "og-art" / f"{HUB}.webp", "WEBP")]
    elif stem.endswith("-vignette-hero"):
        im = fit(crop_to(im, 1.0), 1536)
        out = [(IMG / f"{stem}.png", "PNG"), (IMG / f"{stem}.webp", "WEBP")]
    elif stem.endswith("-og") or stem == f"{HUB}-toolkit":
        im = crop_to(im, 1200 / 630).resize((1200, 630), Image.LANCZOS)
        p = IMG / "og" / f"{stem}.jpg"
        if not dry:
            p.parent.mkdir(parents=True, exist_ok=True); jpeg_under(im, p)
        return [p]
    elif stem.endswith("-card"):
        im = crop_to(im, 16 / 9)
        res = [(IMG / f"{stem}.webp", im.resize((640, 360), Image.LANCZOS))]
        if stem == f"{HUB}-card":
            res.append((IMG / "academy" / "landing" / f"{HUB}.webp", im.resize((960, 540), Image.LANCZOS)))
        for p, x in res:
            if not dry:
                p.parent.mkdir(parents=True, exist_ok=True); x.save(p, "WEBP", quality=86, method=6)
        return [p for p, _ in res]
    else:   # teaching figure
        im = fit(im, 1792)
        out = [(IMG / f"{stem}.webp", "WEBP"), (IMG / f"{stem}.png", "PNG")]
    for p, fmt in out:
        if not dry:
            p.parent.mkdir(parents=True, exist_ok=True)
            im.save(p, fmt, **({"quality": 88, "method": 6} if fmt == "WEBP" else {"optimize": True}))
    return [p for p, _ in out]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    want = planned()
    if a.report:
        have = {p.stem for p in IMG.glob(f"{HUB}*")} | {p.stem for p in (IMG / "og").glob(f"{HUB}*")}
        if (IMG / "academy" / "og-art" / f"{HUB}.webp").exists():
            have.add(ART)
        missing = sorted(w for w in want if w not in have)
        print(f"{len(want) - len(missing)} of {len(want)} planned images present")
        for m in missing:
            print("  missing:", m)
        return
    if not INBOX.exists():
        sys.exit(f"nothing to do: put the generated files in {INBOX.relative_to(ROOT)}/")
    n = 0
    for src in sorted(INBOX.rglob("*")):
        if src.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        key = ART if "og-art" in str(src) else src.stem
        if key not in want:
            print("  skipped (not in the plan):", src.name); continue
        for p in place(src, a.dry_run):
            print(("  would write " if a.dry_run else "  wrote ") + str(p.relative_to(ROOT))); n += 1
    print(f"{n} file(s) {'planned' if a.dry_run else 'written'}")


if __name__ == "__main__":
    main()
