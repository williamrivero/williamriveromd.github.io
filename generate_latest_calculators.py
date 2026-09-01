#!/usr/bin/env python3
"""
generate_latest_calculators.py — williamriveromd.com

Regenerates the "Latest calculators" carousel at the top of the calculators
index (guides/calculators.html) — a horizontally-scrolling row of cards for the
most recently *published* calculator pages, each with its Open Graph share image
peeking on the right edge. Mirrors the "Latest guides" strip but for the
calculator library.

Recency comes from each calculator's immutable <meta property="article:published_time">
stamp (set by patch_published_time.py). Newest first.

The block (a self-contained <style> + section, using `lc-`-prefixed classes so it
never collides with the page CSS and survives patch_master_css.py) is written
between the markers
    <!-- LATEST-CALCS-START --> … <!-- LATEST-CALCS-END -->
just above `<main class="container">`. latest_calculators.json is written
alongside as the ordered data. Idempotent.

Usage:
    python3 generate_latest_calculators.py
    python3 generate_latest_calculators.py --dry-run
    python3 generate_latest_calculators.py --count 16
"""

import re
import json
import argparse
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None


def image_dims(project_dir: Path, rel_thumb: str):
    """Return (width, height) of a thumb image referenced as '../images/x.webp'
    (relative to guides/), read straight off the file on disk. Returns None if
    Pillow is unavailable or the file can't be opened."""
    if Image is None or not rel_thumb:
        return None
    path = project_dir / "images" / rel_thumb.rsplit("/", 1)[-1]
    if not path.exists():
        return None
    try:
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None

START = "<!-- LATEST-CALCS-START -->"
END = "<!-- LATEST-CALCS-END -->"
ANCHOR = '<main class="container">'

STYLE = """<style>
.lc-section{padding:18px 0 4px;}
.lc-label{font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:10px;}
.lc-strip{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px;scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain;}
.lc-strip::-webkit-scrollbar{display:none;}
.lc-card{flex:0 0 248px;scroll-snap-align:start;min-height:120px;position:relative;overflow:hidden;border-radius:10px;background:linear-gradient(135deg,#1f3864 0%,#16294a 100%);padding:12px 96px 12px 14px;text-decoration:none;display:flex;flex-direction:column;justify-content:center;transition:transform .18s,box-shadow .18s;}
.lc-card:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(15,30,51,.3);}
.lc-thumb{position:absolute;top:0;right:0;width:92px;height:100%;object-fit:cover;opacity:.85;-webkit-mask-image:linear-gradient(to right,transparent,#000 60%);mask-image:linear-gradient(to right,transparent,#000 60%);pointer-events:none;}
.lc-eyebrow{font-size:.6rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5fc8d1;margin-bottom:3px;display:flex;align-items:center;gap:5px;}
.lc-dot{width:6px;height:6px;border-radius:50%;background:#5fc8d1;box-shadow:0 0 0 3px rgba(95,200,209,.22);flex:none;}
.lc-title{font-size:.85rem;font-weight:600;color:#fff;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.lc-desc{font-size:.7rem;color:rgba(255,255,255,.72);line-height:1.4;margin-top:4px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.lc-date{font-size:.65rem;color:rgba(255,255,255,.55);margin-top:4px;}
</style>"""

# The calculators index lists calc-*.html plus the standalone DRI calculator.
def is_calculator(name: str) -> bool:
    if name == "calculators.html":
        return False
    return name.startswith("calc-") or name == "ckd-dri-calculator.html"


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def meta(text: str, prop: str) -> str:
    m = re.search(rf'<meta (?:property|name)="{re.escape(prop)}"\s+content="([^"]*)"', text)
    return m.group(1).strip() if m else ""


def clean_title(text: str, stem: str) -> str:
    title = meta(text, "twitter:title") or meta(text, "og:title")
    if not title:
        tm = re.search(r"<title>(.*?)</title>", text, re.S)
        title = tm.group(1).strip() if tm else stem.replace("-", " ").title()
    title = re.split(r"\s+[–—-]\s+W\.?\s*Rivero", title)[0].strip()
    return title


def local_thumb(project_dir: Path, og_image: str, stem: str) -> str:
    base = og_image.rsplit("/", 1)[-1] if og_image else f"{stem}-og.png"
    images = project_dir / "images"
    stem_no_ext = base.rsplit(".", 1)[0]
    if (images / f"{stem_no_ext}.webp").exists():
        return f"../images/{stem_no_ext}.webp"
    if (images / base).exists():
        return f"../images/{base}"
    for cand in (f"{stem}-og.webp", f"{stem}-og.png", f"{stem}-rg-thumb.webp"):
        if (images / cand).exists():
            return f"../images/{cand}"
    return f"../images/{base}"


def category_colors(index_text: str) -> dict:
    """Map each calculator filename → its grid section's --sec-color hex."""
    colors = {}
    sections = re.split(r'(?=<section\b)', index_text)
    for sec in sections:
        cm = re.search(r'--sec-color:\s*(#[0-9a-fA-F]{3,6})', sec)
        if not cm:
            continue
        color = cm.group(1)
        for hm in re.finditer(r'href="(calc-[a-z0-9-]+\.html|ckd-dri-calculator\.html)"', sec):
            colors.setdefault(hm.group(1), color)
    return colors


# Map each section's `id=` / `data-filter=` to the corresponding hero-cat-*.webp.
# Only entries that have an actual image on disk count as a usable fallback.
_CATEGORY_TO_THUMB = {
    "function": "hero-cat-kidney-function",
    "pharmacology": "hero-cat-pharmacology",
    "risk": "hero-cat-ckd-risk",
    "dialysis": "hero-cat-dialysis",
    "transplant": "hero-cat-transplant",
    "electrolytes": "hero-cat-electrolytes",
    "minerals": "hero-cat-minerals-anemia",
    "cardiometabolic": "hero-cat-cardiometabolic",
    "endocrine": "hero-cat-endocrine",
    "nutrition": "hero-cat-nutrition",
    "geriatric": "hero-cat-geriatric",
    "pediatric": "hero-cat-pediatric",
    "screening": "hero-cat-screening",
    "proms": "hero-cat-proms",
    "aki": "hero-cat-aki",
    "critical-care": "hero-cat-critical-care",
    "pulmonary": "hero-cat-pulmonary",
    "oncology": "hero-cat-oncology",
    "rheumatology": "hero-cat-rheumatology",
    "stones": "hero-cat-stones",
    "other-tools": "hero-cat-other-tools",
}


def category_thumbs(project_dir: Path, index_text: str) -> dict:
    """Map each calculator filename → a category fallback thumb (webp), so
    a calc without its own og:image still shows up in the Latest carousel."""
    images = project_dir / "images"
    out = {}
    for sm in re.finditer(
        r'<section class="section"\s+id="([^"]+)"(.*?)(?=<section class="section"|<!--\s*CALC-RESULTS-END|</main>)',
        index_text,
        flags=re.S,
    ):
        sec_id, body = sm.group(1), sm.group(2)
        stem = _CATEGORY_TO_THUMB.get(sec_id)
        if not stem:
            continue
        cand_webp = images / f"{stem}.webp"
        cand_png = images / f"{stem}.png"
        path = (
            f"../images/{stem}.webp" if cand_webp.exists()
            else f"../images/{stem}.png" if cand_png.exists()
            else None
        )
        if not path:
            continue
        for hm in re.finditer(r'href="(calc-[a-z0-9-]+\.html|ckd-dri-calculator\.html)"', body):
            out.setdefault(hm.group(1), path)
    return out


def collect(project_dir: Path, colors: dict, fallbacks: dict):
    guides_dir = project_dir / "guides"
    rows = []
    for path in guides_dir.glob("*.html"):
        if not is_calculator(path.name):
            continue
        text = path.read_text(encoding="utf-8")
        pub = meta(text, "article:published_time")
        if not pub:
            # A calculator with no published_time has no anchor for "Latest" —
            # genuinely skip until it gets a stamp from patch_published_time.py.
            continue
        og_image = meta(text, "og:image")
        try:
            dt = datetime.fromisoformat(pub)
        except ValueError:
            continue
        desc = meta(text, "twitter:description") or meta(text, "og:description") or meta(text, "description")
        # Trim to a tight 1–2 line blurb (~100 chars max).
        if len(desc) > 110:
            desc = desc[:107].rsplit(" ", 1)[0] + "…"
        # Resolve a thumb: own og:image first, else the category hero fallback,
        # else skip the thumb (the gradient bg still reads cleanly). A missing
        # og:image must NOT keep a brand-new calculator out of the strip.
        if og_image:
            thumb = local_thumb(project_dir, og_image, path.stem)
            alt = meta(text, "og:image:alt") or path.stem.replace("-", " ")
        else:
            thumb = fallbacks.get(path.name, "")
            alt = path.stem.replace("-", " ")
        dims = image_dims(project_dir, thumb)
        rows.append({
            "file": path.name,
            "published": pub,
            "dt": dt,
            "title": clean_title(text, path.stem),
            "desc": desc,
            "thumb": thumb,
            "thumb_w": dims[0] if dims else None,
            "thumb_h": dims[1] if dims else None,
            "alt": alt,
            "color": colors.get(path.name, "#1f3864"),
        })
    rows.sort(key=lambda r: (r["dt"], r["file"]), reverse=True)
    return rows


def card_html(r) -> str:
    label = r["dt"].strftime("%b %-d, %Y")
    alt = (r["alt"] or "").replace('"', "&quot;")
    c = r["color"]
    # Tint the card by its category colour (same hue family as the grid cards).
    bg = f"background:linear-gradient(135deg,color-mix(in srgb,{c} 30%,#16294a) 0%,#14233f 100%);"
    dot = f"background:{c};box-shadow:0 0 0 3px color-mix(in srgb,{c} 30%,transparent);"
    desc_html = (
        f'        <span class="lc-desc">{r["desc"]}</span>\n' if r.get("desc") else ""
    )
    dim_attrs = (
        f' width="{r["thumb_w"]}" height="{r["thumb_h"]}"'
        if r.get("thumb_w") and r.get("thumb_h") else ""
    )
    thumb_html = (
        f'        <img class="lc-thumb" src="{r["thumb"]}" alt="{alt}" loading="lazy" decoding="async"{dim_attrs}>\n'
        if r.get("thumb") else ""
    )
    return (
        f'      <a href="{r["file"]}" class="lc-card" style="{bg}">\n'
        f'        <span class="lc-eyebrow"><span class="lc-dot" style="{dot}"></span>New calculator</span>\n'
        f'        <span class="lc-title">{r["title"]}</span>\n'
        f'{desc_html}'
        f'        <span class="lc-date"><time datetime="{r["published"]}">{label}</time></span>\n'
        f'{thumb_html}'
        f'      </a>'
    )


def build_block(rows) -> str:
    cards = "\n".join(card_html(r) for r in rows)
    return (
        f"{START}\n"
        "<!-- Generated by generate_latest_calculators.py — do not hand-edit. -->\n"
        f"{STYLE}\n"
        '<section class="lc-section"><div class="container">\n'
        '  <div class="lc-label">Latest calculators</div>\n'
        '  <div class="lc-strip">\n'
        f"{cards}\n"
        '  </div>\n'
        '</div></section>\n'
        f"{END}"
    )


def main():
    ap = argparse.ArgumentParser(description="Regenerate the Latest-calculators carousel.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--count", type=int, default=12, help="number of cards (default 12)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    index_path = project_dir / "guides" / "calculators.html"

    index_text = index_path.read_text(encoding="utf-8")
    colors = category_colors(index_text)
    fallbacks = category_thumbs(project_dir, index_text)
    rows = collect(project_dir, colors, fallbacks)
    featured = rows[: args.count]
    print(f"Latest {len(featured)} calculator(s):")
    for r in featured:
        print(f"  {r['dt'].strftime('%Y-%m-%d %H:%M')}  {r['file']}")

    block = build_block(featured)
    text = index_path.read_text(encoding="utf-8")

    if START in text and END in text:
        new_text = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text,
                          count=1, flags=re.S)
    else:
        if ANCHOR not in text:
            raise SystemExit(f"Cannot find anchor {ANCHOR!r} in calculators.html.")
        new_text = text.replace(ANCHOR, block + "\n" + ANCHOR, 1)
        print(f"  (markers absent — inserted block before {ANCHOR})")

    data = [{"file": r["file"], "title": r["title"], "published": r["published"],
             "thumb": r["thumb"]} for r in rows]

    if new_text == text:
        print("\ncalculators.html unchanged.")
    elif args.dry_run:
        print("\n[dry-run] would update guides/calculators.html")
    else:
        index_path.write_text(new_text, encoding="utf-8")
        print("\n✓ updated guides/calculators.html")

    if not args.dry_run:
        (project_dir / "latest_calculators.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
