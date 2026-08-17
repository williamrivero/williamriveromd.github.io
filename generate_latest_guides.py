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

The script ALSO keeps the site's guide/calculator counts in sync everywhere
they're hand-displayed, so they never drift the way "141 guides" did (the real
count was 145 while three different stale numbers — 130, 135, 141 — sat in
different meta tags). It recomputes the true counts from source (guide-tile
count in guides/index.html, minus the downloads-only tiles; related-card count
in guides/calculators.html) and patches: the guides/index.html hero stat, its
mobile-filter and sidebar-filter "All N" labels, its og/twitter meta copy,
calculators.html's og:image:alt, and the root index.html hero stat fallback
(the data-target the JS count-up animation uses before its own live sync
fetch resolves). It also patches the two guides/index.html numbers no JS ever
rewrites — the search-box placeholder and the results-count fallback — and
every static cf-count filter chip on calculators.html ("All tools", plus each
category), which otherwise go one short the moment a calculator is added.
Runs automatically as part of `main()` — no separate flag.

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

# Editing artifacts that must never reach the live strip. A hand-saved backup
# keeps its article:published_time, so without this it outranks real guides and
# publishes a card pointing at a stale, unlinked copy (this happened with
# epilepsy-seizures-ckd.hero-backup-20260623.html).
SKIP_CONTAINS = (".hero-backup-", ".backup-", ".bak", " 2.html", "-copy.html", "-samples.html")

# Guides whose og:image crops badly under the strip's live CSS crop (a large
# title block on one side of a wide OG card, flagged by hand) — prefer the
# pre-cropped {stem}-rg-thumb.webp instead. Guides using a square
# circular-vignette hero get this automatically (see local_thumb below); add a
# guide here only if its OG card is confirmed to crop awkwardly too.
PREFER_RG_THUMB = {
    "dialysis-water-treatment-systems",
    "dialysis-cramps-stasis-pigmentation",
}


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
    if any(frag in name for frag in SKIP_CONTAINS):
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
    """Relative path (from guides/) to the thumb image; prefer a .webp sibling.

    The live CSS crop (`object-fit:cover`, no explicit object-position) shows
    the visual CENTER of whatever og:image is used — not necessarily the
    right-edge "peek" the strip intends. A square circular-vignette hero
    always crops awkwardly under that treatment, so it's swapped for the
    purpose-built {stem}-rg-thumb.webp (a pre-cropped 220x160 frame already
    generated by generate_rg_thumbs.py) automatically. A handful of wide OG
    cards with a large title block on one side crop just as awkwardly —
    those are flagged individually in PREFER_RG_THUMB above.
    """
    base = og_image.rsplit("/", 1)[-1] if og_image else f"{stem}-og.png"
    images = project_dir / "images"
    stem_no_ext = base.rsplit(".", 1)[0]
    if stem_no_ext.endswith("-vignette-hero") or stem in PREFER_RG_THUMB:
        rg_thumb = images / f"{stem}-rg-thumb.webp"
        if rg_thumb.exists():
            return f"../images/{stem}-rg-thumb.webp"
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


def count_true_guides(index_html: str) -> int:
    """Guide-tile count in guides/index.html, minus tiles tagged "download"
    (those point to PDF companions in downloads/, or a printable blank log —
    not readable web guides). This is the site's own definition of "a guide",
    already used by the homepage's stat-sync JS."""
    tiles = re.findall(r'<a\b[^>]*class="[^"]*\bguide-tile\b[^"]*"[^>]*>', index_html)
    count = 0
    for t in tiles:
        m = re.search(r'data-tags="([^"]*)"', t)
        tags = m.group(1).lower() if m else ""
        if "download" not in tags:
            count += 1
    return count


def count_true_calculators(calculators_html: str) -> int:
    """related-card tile count in guides/calculators.html — every calc-*.html
    page plus the handful of non-prefixed interactive tools (e.g.
    dyslipidemia-management-tool.html) that are listed the same way."""
    return len(re.findall(r'<a class="related-card[^"]*" href="[^"]*"', calculators_html))


def count_true_specialties(index_html: str) -> int:
    """Distinct guide-section categories (nephrology, internal, nutrition, …)."""
    return len(set(re.findall(r'<div class="guide-section"[^>]*data-section="([^"]+)"', index_html)))


def sync_calc_filter_chips(calc_text: str) -> tuple[str, int]:
    """Recompute every cf-count chip on guides/calculators.html from the grid.

    The category filter chips ("Dialysis 23", "All tools 197") are static HTML —
    only the Favorites chip is JS-driven — so adding a calculator to a section
    silently leaves both that section's chip and the "All tools" chip one short.
    Counts come from the real grid: <a class="related-card"> inside each
    <section id="…">, with the Latest-calculators carousel excluded so its
    cards are never double-counted.
    """
    body = re.sub(r'<!-- LATEST-CALCS-START -->.*?<!-- LATEST-CALCS-END -->',
                  '', calc_text, flags=re.DOTALL)
    per_section = {}
    for m in re.finditer(r'<section class="section" id="([a-z-]+)"[^>]*>(.*?)</section>',
                         body, re.DOTALL):
        n = len(re.findall(r'<a class="related-card', m.group(2)))
        if n:
            per_section[m.group(1)] = n
    per_section['all'] = sum(per_section.values())

    changed = 0

    # Every capture group is re-emitted, including the data-filter attribute
    # itself — dropping it would silently disable the category filter buttons.
    # The Favorites chip carries an id and is written by JS, so it is skipped.
    pattern = (r'(data-filter=")([a-z-]+)(")'
               r'(?![^>]*id="cf-fav-count")'
               r'((?:(?!</button>).)*?<span class="cf-count">)(\d+)(</span>)')

    def repl2(m):
        nonlocal changed
        a, key, b, mid, old, tail = m.groups()
        true = per_section.get(key)
        if true is None or str(true) == old:
            return m.group(0)
        changed += 1
        return f'{a}{key}{b}{mid}{true}{tail}'

    calc_text = re.sub(pattern, repl2, calc_text)
    return calc_text, changed


def sync_library_stats(project_dir: Path, guides_index_text: str, dry_run: bool) -> str:
    """Patch every hand-displayed guide/calculator count to the true, freshly
    computed values. Returns the (possibly) updated guides/index.html text;
    also patches guides/calculators.html and root index.html in place."""
    calc_path = project_dir / "guides" / "calculators.html"
    root_index_path = project_dir / "index.html"
    calc_text = calc_path.read_text(encoding="utf-8")

    guide_count = count_true_guides(guides_index_text)
    calc_count = count_true_calculators(calc_text)
    spec_count = count_true_specialties(guides_index_text)

    print(f"\nTrue counts: {guide_count} guides, {calc_count} calculators, {spec_count} specialties")

    text = guides_index_text
    text, n1 = re.subn(
        r'(<span class="stat-num">)\d+(</span><span class="stat-label">Guides</span>)',
        rf'\g<1>{guide_count}\g<2>', text)
    text, n2 = re.subn(
        r'(<span class="stat-num">)\d+(</span><span class="stat-label">Calculators</span>)',
        rf'\g<1>{calc_count}\g<2>', text)
    text, n3 = re.subn(
        r'(<span class="stat-num">)\d+(</span><span class="stat-label">Specialties</span>)',
        rf'\g<1>{spec_count}\g<2>', text)
    text, n4 = re.subn(r'(data-filter="all">All )\d+', rf'\g<1>{guide_count}', text)
    text, n5 = re.subn(
        r'(All guides<span class="count">)\d+(</span>)',
        rf'\g<1>{guide_count}\g<2>', text)
    text, n6 = re.subn(
        r'\d+( evidence-based guides on CKD)', rf'{guide_count}\g<1>', text)
    text, n7 = re.subn(
        r'\d+( evidence-based guides, )\d+( calculators)',
        rf'{guide_count}\g<1>{calc_count}\g<2>', text)
    # The search box placeholder is a static attribute — no JS ever rewrites it,
    # so a stale number here is visible to every visitor until it is patched.
    text, n8 = re.subn(
        r'(placeholder=.Search )\d+( guides)', rf'\g<1>{guide_count}\g<2>', text)
    # The results-count span IS recomputed by refreshCounts() on load, but the
    # static value is what a no-JS or slow-JS visitor sees first — keep it true.
    text, n9 = re.subn(
        r'(<span class="results-count" id="results-count">)\d+(</span>)',
        rf'\g<1>{guide_count}\g<2>', text)
    changed = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
    print(f"guides/index.html: {changed} stat/meta reference(s) synced" if changed else "guides/index.html: stats already in sync")

    new_calc_text, cn1 = re.subn(
        r'\d+( evidence-based nephrology calculators)', rf'{calc_count}\g<1>', calc_text)
    cn2 = sync_calc_filter_chips(new_calc_text)
    new_calc_text = cn2[0]
    cn1 += cn2[1]
    print(f"guides/calculators.html: {cn1} reference(s) synced" if cn1 else "guides/calculators.html: already in sync")

    root_text = root_index_path.read_text(encoding="utf-8")
    # Both the data-target attribute AND the visible digits between the tags
    # need updating — the real number is baked into the static HTML itself
    # (not just a JS-animation target) so no-JS/slow-JS visitors never see a
    # stale count either.
    new_root_text, rn1 = re.subn(
        r'(<div class="rcm-stat-num" id="stat-guides" data-target=")\d+(">)\d+(</div>)',
        rf'\g<1>{guide_count}\g<2>{guide_count}\g<3>', root_text)
    new_root_text, rn2 = re.subn(
        r'(<div class="rcm-stat-num" id="stat-specialties" data-target=")\d+(">)\d+(</div>)',
        rf'\g<1>{spec_count}\g<2>{spec_count}\g<3>', new_root_text)
    new_root_text, rn3 = re.subn(
        r'(<div class="rcm-stat-num" id="stat-calculators" data-target=")\d+(">)\d+(</div>)',
        rf'\g<1>{calc_count}\g<2>{calc_count}\g<3>', new_root_text)
    new_root_text, rn4 = re.subn(
        r'(<span id="stat-specialties-inline">)\d+(</span>)', rf'\g<1>{spec_count}\g<2>', new_root_text)
    new_root_text, rn5 = re.subn(
        r'(<span id="stat-calculators-inline">)\d+(</span>)', rf'\g<1>{calc_count}\g<2>', new_root_text)
    new_root_text, rn6 = re.subn(
        r'(<span id="stat-calculators-inline2">)\d+(</span>)', rf'\g<1>{calc_count}\g<2>', new_root_text)
    new_root_text, rn8 = re.subn(
        r'\d+( physician-written guides and )\d+( interactive tools)',
        rf'{guide_count}\g<1>{calc_count}\g<2>', new_root_text)
    rn = rn1 + rn2 + rn3 + rn4 + rn5 + rn6 + rn8
    print(f"index.html: {rn} hero stat fallback(s) synced" if rn else "index.html: stats already in sync")

    if not dry_run:
        if new_calc_text != calc_text:
            calc_path.write_text(new_calc_text, encoding="utf-8")
        if new_root_text != root_text:
            root_index_path.write_text(new_root_text, encoding="utf-8")
    elif cn1 or rn:
        print("[dry-run] would update guides/calculators.html and/or index.html")

    return text


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

    new_text = sync_library_stats(project_dir, new_text, args.dry_run)

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
