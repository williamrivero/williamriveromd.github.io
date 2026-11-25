"""Schola (Renal Care Academy app) Home Screen icons, in the flat style of Dosis and Calculo:
an open book in cream with a gold bookmark ribbon on a deep navy rounded square.

    python3 tools/academy/make_schola_icons.py     # writes images/app/schola-*.png
"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parents[2] / "images" / "app"
BG = (31, 56, 100)        # navy #1F3864 (Renal Care Physicians / Academy navy)
PAGE = (246, 243, 236)    # cream, as in the Dosis and Calculo glyphs
SPINE = (26, 107, 114)    # teal #1A6B72
RIBBON = (200, 150, 40)   # gold, as in Dosis
LINES = (196, 205, 216)


def glyph(d, s, scale):
    """Open book centered in an s x s canvas; scale = share of the canvas the book spans."""
    w = s * scale
    cx, cy = s / 2, s / 2 + s * 0.03
    h = w * 0.62
    top, bot = cy - h / 2, cy + h / 2
    dip = h * 0.10                       # pages curve down toward the spine
    left = [(cx - w / 2, top), (cx - w * 0.04, top + dip), (cx - w * 0.04, bot + dip * 0.4), (cx - w / 2, bot - dip * 0.2)]
    right = [(cx + w * 0.04, top + dip), (cx + w / 2, top), (cx + w / 2, bot - dip * 0.2), (cx + w * 0.04, bot + dip * 0.4)]
    d.polygon(left, fill=PAGE)
    d.polygon(right, fill=PAGE)
    d.rectangle([cx - w * 0.04, top + dip, cx + w * 0.04, bot + dip * 0.4], fill=SPINE)
    lw = max(2, int(s * 0.018))
    for i in range(4):                   # text lines on both pages
        y = top + h * (0.24 + i * 0.16)
        d.line([(cx - w * 0.42, y), (cx - w * 0.12, y + dip * 0.55)], fill=LINES, width=lw)
        d.line([(cx + w * 0.12, y + dip * 0.55), (cx + w * 0.42, y)], fill=LINES, width=lw)
    rx = cx + w * 0.24                   # bookmark ribbon hanging from the right page
    rw = w * 0.10
    d.polygon([(rx, top - h * 0.02), (rx + rw, top - h * 0.02), (rx + rw, bot + h * 0.20),
               (rx + rw / 2, bot + h * 0.10), (rx, bot + h * 0.20)], fill=RIBBON)


def icon(size, rounded, scale):
    s = size * 4                         # draw large, then downsample for smooth edges
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if rounded:
        d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=BG)
    else:
        d.rectangle([0, 0, s, s], fill=BG)
    glyph(d, s, scale)
    return im.resize((size, size), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    icon(512, True, 0.66).save(OUT / "schola-512.png")
    icon(192, True, 0.66).save(OUT / "schola-192.png")
    icon(180, False, 0.62).convert("RGB").save(OUT / "schola-180.png")          # iOS rounds it itself
    icon(512, False, 0.52).save(OUT / "schola-maskable-512.png")                # glyph inside the 80% safe zone
    icon(192, False, 0.52).save(OUT / "schola-maskable-192.png")
    print("schola icons written to", OUT)


if __name__ == "__main__":
    main()
