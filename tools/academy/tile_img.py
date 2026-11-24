"""Module-tile thumbnails for the hand-built Academy tracks (nursing, support staff, special nurse roles, transplant).

The generated technician tracks already show a 16:9 picture on each module tile (generate_tech_courses.card_img). This
gives the hand-built generators the same tile: if images/<stem>-card.webp exists, the tile gets the picture and the
tc-mod body wrapper; otherwise it is left exactly as before. Cards are cut from each module's vignette hero with
tools/techcourses/prep_assets.card() (640 x 360 WebP).
"""
from pathlib import Path

IMAGES = Path(__file__).resolve().parents[2] / "images"

TILE_CSS = (".nc-mod.tc-mod{padding:0;overflow:hidden;}"
            ".tc-mod-img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;background:var(--bg);}"
            ".tc-mod-body{display:flex;flex-direction:column;gap:6px;padding:12px 16px 14px;}")


def tile_img(stem):
    f = f"{stem}-card.webp"
    if (IMAGES / f).exists():
        return (f'<img class="tc-mod-img nc-fig-img" src="../images/{f}" alt="" loading="lazy" decoding="async" '
                f'width="640" height="360">')
    return ""


def tile(a_open, inner, stem):
    """a_open: the opening <a class="nc-mod" ...> tag; inner: the tile's spans (no closing tag)."""
    img = tile_img(stem)
    if not img:
        return f"{a_open}\n{inner}\n    </a>"
    a_open = a_open.replace('class="nc-mod"', 'class="nc-mod tc-mod"', 1)
    return f'{a_open}{img}\n      <span class="tc-mod-body">{inner.strip()}</span>\n    </a>'
