"""Paratus app icons (Nov 28 2026): a white ECG trace with a heartbeat spike over a deep red field, with a thin white ring,
drawn with Pillow. Writes images/app/paratus-{180,192,512}.png (rounded) and paratus-maskable-{192,512}.png (full bleed,
artwork inside the 80% safe zone).    python3 tools/academy/make_paratus_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parents[2] / "images" / "app"
S = 1024


def art(maskable):
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    top, bot = (185, 28, 28), (127, 29, 29)
    for y in range(S):                                     # vertical red gradient
        t = y / (S - 1)
        d.line([(0, y), (S, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,))
    if not maskable:                                       # rounded app-icon square
        mask = Image.new("L", (S, S), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
        im.putalpha(mask)
    k = 0.78 if maskable else 0.92                         # keep the drawing inside the maskable safe zone
    c = S / 2

    def P(x, y):
        return (c + (x - c) * k, c + (y - c) * k)
    r = S * 0.36                                           # thin ring
    d.ellipse([P(c - r, c - r), P(c + r, c + r)], outline=(255, 205, 205, 255), width=int(S * 0.014))
    pts = [(150, 540), (360, 540), (410, 470), (450, 540), (490, 540), (540, 250), (600, 790), (650, 540), (700, 540),
           (745, 480), (790, 540), (874, 540)]
    d.line([P(x, y) for x, y in pts], fill=(255, 255, 255, 255), width=int(S * 0.058), joint="curve")
    for x, y in pts[1:-1]:                                 # round every joint
        rr = S * 0.029 * k * 0.98
        cx, cy = P(x, y)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(255, 255, 255, 255))
    for x, y in (pts[0], pts[-1]):
        rr = S * 0.029 * k
        cx, cy = P(x, y)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(255, 255, 255, 255))
    return im


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    a, m = art(False), art(True)
    for n in (180, 192, 512):
        a.resize((n, n), Image.LANCZOS).save(OUT / f"paratus-{n}.png", optimize=True)
    for n in (192, 512):
        m.resize((n, n), Image.LANCZOS).convert("RGB").save(OUT / f"paratus-maskable-{n}.png", optimize=True)
    print("paratus icons written")


if __name__ == "__main__":
    main()
