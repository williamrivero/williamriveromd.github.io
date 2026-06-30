#!/usr/bin/env python3
"""
generate_latest_guides.py — williamriveromd.com

Regenerates the "Latest guides" strip on guides/index.html: a row of cards for
the most recently *published* content guides, each with the guide's Open Graph
(OG) share image peeking out on the right edge of the card.

Recency is driven entirely by the immutable <meta property="article:published_time">
stamp that patch_published_time.py writes into every guide (date + time, +08:00).
Newest first. Run patch_published_time.py before this script so brand-new guides
carry a timestamp.

The strip is written between the markers
    <!-- LATEST-GUIDES-START --> … <!-- LATEST-GUIDES-END -->
in guides/index.html, placed just above the mobile filter bar / "Continue
reading" rail. If the markers are missing they are auto-inserted before the
"<!-- MOBILE FILTER BAR -->" comment. The script also writes latest_guides.json
(the ordered data it used). Idempotent.

Usage:
    python3 generate_latest_guides.py
    python3 generate_latest_guides.py --dry-run
    python3 generate_latest_guides.py --count 6
"""

import re
import json
import argparse
from datetime import datetime
from pathlib import Path

START = "<!-- LATEST-GUIDES-START -->"
END = "<!-- LATEST-GUIDES-END -->"
ANCHOR = "<!-- MOBILE FILTER BAR -->"

# Category palette — same hues as each section's `.section-color-bar` in the
# index. Used as solid (not CSS-var) hex so the card gradient resolves even
# when the variable isn't defined in the rendering scope.
SECTION_COLORS = {
    "nephrology":   "#1a6b72",   # teal
    "internal":     "#c55a11",   # orange
    "perspectives": "#1f3864",   # deep navy (essay/opinion gravitas)
    "nutrition":    "#2e6b3e",   # green
    "lifestyle":    "#7c3aed",   # violet
    "advanced":     "#6b46c1",   # purple
    "dialysis":     "#1f3864",   # navy
    "philippines":  "#c2410c",   # amber-orange
    "download":     "#92710a",   # gold
}
DEFAULT_CARD_COLOR = "#1a6b72"

# Pages that are not patient-education *guides* (calculators, printables, tools,
# the directory itself). Excluded from the Latest-guides strip.
SKIP_EXACT = {
    "index.html", "calculators.html", "ckd-dri-calculator.html",
    "symptom-checker.html", "lab-interpreter-guide.html", "lab-interpreter.html",
    "nephrology-atlas.html",
}
SKIP_PREFIX = ("calc-",)
SKIP_SUFFIX = ("-log.html", "-log-blank.html", "-blank.html")


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def is_guide(name: str) -> bool:
    if name in SKIP_EXACT:
        return False
    if name.startswith(SKIP_PREFIX):
        return False
    if name.endswith(SKIP_SUFFIX):
        return False
    return True


def meta(text: str, prop: str) -> str:
    m = re.search(
        rf'<meta (?:property|name)="{re.escape(prop)}"\s+content="([^"]*)"', text
    )
    return m.group(1).strip() if m else ""


def clean_title(text: str, stem: str) -> str:
    title = meta(text, "twitter:title") or meta(text, "og:title")
    if not title:
        tm = re.search(r"<title>(.*?)</title>", text, re.S)
        title = tm.group(1).strip() if tm else stem.replace("-", " ").title()
    # Drop the author byline suffix ("… – W Rivero, MD").
    title = re.split(r"\s+[–—-]\s+W\.?\s*Rivero", title)[0].strip()
    return title


def local_thumb(project_dir: Path, og_image: str, stem: str) -> str:
    """Relative path (from guides/) to the thumb image; prefer a .webp sibling."""
    base = og_image.rsplit("/", 1)[-1] if og_image else f"{stem}-og.png"
    images = project_dir / "images"
    stem_no_ext = base.rsplit(".", 1)[0]
    webp = images / f"{stem_no_ext}.webp"
    if webp.exists():
        return f"../images/{stem_no_ext}.webp"
    if (images / base).exists():
        return f"../images/{base}"
    # Last resort: the conventional OG card.
    for cand in (f"{stem}-og.webp", f"{stem}-og.png"):
        if (images / cand).exists():
            return f"../images/{cand}"
    return f"../images/{base}"


def file_to_section(index_html: str) -> dict:
    """Walk guides/index.html and map each tiled guide file → its data-section.

    Splits the document on the `<div class="guide-section" data-section="…">`
    opening tag and reads tiles out of each chunk. Simpler than the original
    lookahead regex (which was matching only the first chunk in practice)."""
    out = {}
    parts = re.split(
        r'<div class="guide-section"[^>]*data-section="([^"]+)"[^>]*>',
        index_html,
    )
    # re.split returns [pre, key1, body1, key2, body2, …]
    # Tiles can have href before class or after, and the class attribute may
    # carry extra tokens (e.g. "guide-tile dual"). Match either order with
    # \bguide-tile\b inside the class string.
    tile_re = re.compile(
        r'<a\s+(?=[^>]*class="[^"]*\bguide-tile\b[^"]*")[^>]*href="([^"]+)"|'
        r'<a\s+(?=[^>]*href="([^"]+)")[^>]*class="[^"]*\bguide-tile\b[^"]*"',
    )
    for i in range(1, len(parts), 2):
        ds, body = parts[i], parts[i + 1] if i + 1 < len(parts) else ""
        for m in tile_re.finditer(body):
            href = m.group(1) or m.group(2)
            if href:
                out.setdefault(href, ds)
    return out


def collect(project_dir: Path):
    guides_dir = project_dir / "guides"
    index_html = (guides_dir / "index.html").read_text(encoding="utf-8")
    file_section = file_to_section(index_html)
    rows = []
    for path in guides_dir.glob("*.html"):
        if not is_guide(path.name):
            continue
        text = path.read_text(encoding="utf-8")
        pub = meta(text, "article:published_time")
        og_image = meta(text, "og:image")
        if not pub or not og_image:
            continue
        try:
            dt = datetime.fromisoformat(pub)
        except ValueError:
            continue
        section = file_section.get(path.name, "")
        rows.append({
            "file": path.name,
            "published": pub,
            "dt": dt,
            "title": clean_title(text, path.stem),
            "thumb": local_thumb(project_dir, og_image, path.stem),
            "alt": meta(text, "og:image:alt"),
            "section": section,
            "color": SECTION_COLORS.get(section, DEFAULT_CARD_COLOR),
        })
    # Newest first; tie-break by filename for determinism.
    rows.sort(key=lambda r: (r["dt"], r["file"]), reverse=True)
    return rows


def card_html(r) -> str:
    dt = r["dt"]
    # Visible label is date-only for a clean card; the full date+time lives in the
    # <time datetime="…"> attribute and in the guide's article:published_time meta.
    label = dt.strftime("%b %-d, %Y")
    alt = (r["alt"] or "").replace('"', "&quot;")
    return (
        f'      <a href="{r["file"]}" class="latest-card" style="--card-color:{r["color"]}">\n'
        f'        <span class="latest-eyebrow"><span class="latest-dot"></span>New guide</span>\n'
        f'        <span class="latest-title">{r["title"]}</span>\n'
        f'        <span class="latest-date"><time datetime="{r["published"]}">{label}</time></span>\n'
        f'        <img class="latest-thumb" src="{r["thumb"]}" alt="{alt}" loading="lazy" decoding="async">\n'
        f'      </a>'
    )


def build_block(rows) -> str:
    cards = "\n".join(card_html(r) for r in rows)
    return (
        f"{START}\n"
        '<!-- Generated by generate_latest_guides.py — do not hand-edit. -->\n'
        '<div class="latest-path">\n'
        '  <div class="latest-path-inner">\n'
        '    <div class="latest-label">Latest guides</div>\n'
        '    <div class="latest-strip">\n'
        f"{cards}\n"
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        f"{END}"
    )


def main():
    ap = argparse.ArgumentParser(description="Regenerate the Latest-guides strip.")
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--count", type=int, default=12, help="number of cards (default 12; the strip scrolls horizontally)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    index_path = project_dir / "guides" / "index.html"

    rows = collect(project_dir)
    featured = rows[: args.count]

    print(f"Latest {len(featured)} guide(s):")
    for r in featured:
        print(f"  {r['dt'].strftime('%Y-%m-%d %H:%M')}  {r['file']}")

    block = build_block(featured)
    text = index_path.read_text(encoding="utf-8")

    if START in text and END in text:
        new_text = re.sub(
            re.escape(START) + r".*?" + re.escape(END), block, text, count=1, flags=re.S
        )
    else:
        if ANCHOR not in text:
            raise SystemExit(f"Cannot find anchor {ANCHOR!r} to insert the strip.")
        new_text = text.replace(ANCHOR, block + "\n\n" + ANCHOR, 1)
        print(f"  (markers absent — inserted block before {ANCHOR})")

    # Write the ordered data alongside, for reference / other consumers.
    data = [
        {"file": r["file"], "title": r["title"], "published": r["published"],
         "thumb": r["thumb"], "section": r.get("section", ""),
         "color": r.get("color", DEFAULT_CARD_COLOR)}
        for r in rows
    ]

    if new_text == text:
        print("\nindex.html unchanged.")
    elif args.dry_run:
        print("\n[dry-run] would update guides/index.html")
    else:
        index_path.write_text(new_text, encoding="utf-8")
        print("\n✓ updated guides/index.html")

    if not args.dry_run:
        (project_dir / "latest_guides.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
