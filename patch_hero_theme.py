#!/usr/bin/env python3
"""DRAFT — restructure a guide's hero into the new themed two-column layout.

The already-themed reference is ``guides/epilepsy-seizures-ckd.html``. Its hero
uses a ``hero-grid`` that splits the hero into a left ``hero-copy`` column
(hero-tag, h1, hero-sub, hero-meta) and a right slot holding the patient
portrait (``figure.hero-figure > div.hero-vignette > picture/img``) and a
clinician "Jump to" card panel (``aside.hero-cards``).

Almost every other in-scope guide instead has a single, shared
``<section class="hero">`` whose ``<div class="container">`` holds the hero copy
directly (hero-tag, h1, hero-sub, hero-meta), sometimes with an inline hero
``<figure>``/``<picture>`` after the copy. This script rewrites that single hero
into the themed grid:

    <section class="hero"><div class="container">
      <!-- HERO-THEME START -->
      <div class="hero-grid">
        <div class="hero-copy"> ...original tag/h1/sub/meta... </div>
        <aside class="hero-aside">
          <figure class="hero-figure mode-patient"><div class="hero-vignette">
            ...relocated <picture>/<img>...
          </div></figure>
          <aside class="hero-cards mode-physician"> ...auto Jump-to panel... </aside>
        </aside>
      </div>
      <!-- HERO-THEME END -->
    </div></section>

Design decisions / honest scope notes
--------------------------------------
* This is a DRAFT. It transforms ONLY the first ``<section class="hero">`` of a
  guide and ONLY when that hero contains a single ``<div class="container">``
  whose direct children are the recognisable hero-copy pieces. Anything that
  does not match cleanly is SKIPPED and reported — never rewritten — so the
  script can never emit malformed HTML.
* The patient figure is the hero's existing inline ``<figure>`` (or bare
  ``<picture>``), if any. It is moved into ``figure.hero-figure.mode-patient >
  div.hero-vignette``. If the hero has no inline image, no patient figure is
  emitted (the aside then holds only the clinician card).
* The clinician card is an auto-generated "Jump to" panel built from the guide's
  ``<section id="md-...">`` anchors (heading text becomes the link label). If a
  guide has no ``md-*`` sections, the panel is built from the page's other
  ``<section id="...">`` anchors; if there are none of those either, the
  clinician card is omitted and only the figure (if any) remains.
* Idempotency: the rewritten block is wrapped in
  ``<!-- HERO-THEME START -->`` / ``<!-- HERO-THEME END -->`` markers. A hero
  that already carries a ``hero-grid`` (the two reference guides) or the markers
  is skipped as already-themed.

Usage:
    python3 patch_hero_theme.py                       # all in-scope guides
    python3 patch_hero_theme.py --dry-run             # preview only
    python3 patch_hero_theme.py --guide understanding-ckd.html
"""
import argparse
import glob
import os
import re
import sys
from html import unescape

GUIDES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides")

# Guides intentionally out of scope.
EXCLUDE_EXACT = {"index.html", "nephrology-atlas.html"}
EXCLUDE_PREFIX = ("calc-",)

START_MARKER = "<!-- HERO-THEME START -->"
END_MARKER = "<!-- HERO-THEME END -->"

# First <section class="hero" ...> ... </section> (non-greedy, dot-all).
HERO_SECTION_RE = re.compile(
    r'<section class="hero"[^>]*>(?P<body>.*?)</section>', re.IGNORECASE | re.DOTALL
)
# A single top-level <div class="container"> ... </div> inside the hero body.
CONTAINER_RE = re.compile(
    r'(?P<open><div class="container"[^>]*>)(?P<inner>.*)(?P<close></div>)',
    re.IGNORECASE | re.DOTALL,
)
# Recognised hero-copy openers.
HERO_TAG_RE = re.compile(r'<div class="hero-tag"', re.IGNORECASE)
H1_RE = re.compile(r'<h1\b', re.IGNORECASE)
HERO_SUB_RE = re.compile(r'<p class="hero-sub"', re.IGNORECASE)
HERO_META_RE = re.compile(r'<div class="hero-meta"', re.IGNORECASE)
# An inline hero figure or bare picture that carries the LCP image.
FIGURE_RE = re.compile(r'<figure\b.*?</figure>', re.IGNORECASE | re.DOTALL)
PICTURE_RE = re.compile(r'<picture\b.*?</picture>', re.IGNORECASE | re.DOTALL)


def matched_block(html, open_re, tag_name):
    """Return (start, end) span of the first ``tag_name`` element, brace-matched.

    Handles nesting of identical tags so a hero-copy ``<div>`` that contains
    nested ``<div>``s is captured in full. Returns None if not found or if the
    tags are unbalanced (defensive — caller then skips the guide).
    """
    m = open_re.search(html)
    if not m:
        return None
    start = m.start()
    open_pat = re.compile(r'<' + tag_name + r'\b', re.IGNORECASE)
    close_pat = re.compile(r'</' + tag_name + r'>', re.IGNORECASE)
    depth = 0
    pos = start
    token = re.compile(r'<' + tag_name + r'\b|</' + tag_name + r'>', re.IGNORECASE)
    for t in token.finditer(html, start):
        if t.group(0).startswith('</'):
            depth -= 1
            if depth == 0:
                return (start, t.end())
        else:
            depth += 1
    return None


def first_heading_text(section_html):
    """Plain-text label from a section's first <h2>/<h3>, English span preferred."""
    m = re.search(r'<h[23]\b[^>]*>(.*?)</h[23]>', section_html, re.IGNORECASE | re.DOTALL)
    if not m:
        return None
    inner = m.group(1)
    # Prefer the English-language span when the heading is multilingual.
    en = re.search(r'data-lang="en"[^>]*>(.*?)</span>', inner, re.IGNORECASE | re.DOTALL)
    if en:
        inner = en.group(1)
    text = re.sub(r'<[^>]+>', '', inner)
    text = unescape(text).strip()
    text = re.sub(r'\s+', ' ', text)
    return text or None


def collect_anchors(html):
    """Return [(anchor_id, label)] for clinician jump-to links.

    Prefers ``id="md-..."`` sections; falls back to any ``<section id="...">``.
    """
    md = []
    other = []
    for m in re.finditer(r'<section\b[^>]*\bid="([^"]+)"[^>]*>', html, re.IGNORECASE):
        sid = m.group(1)
        # Grab a slice of this section to read its heading.
        seg = html[m.start(): m.start() + 4000]
        label = first_heading_text(seg) or sid.replace("-", " ").title()
        (md if sid.startswith("md-") else other).append((sid, label))
    return md if md else other


def build_jump_card(anchors, limit=8):
    """Build the clinician 'Jump to' aside.hero-cards, or '' if no anchors."""
    if not anchors:
        return ""
    rows = []
    for i, (sid, label) in enumerate(anchors[:limit], start=1):
        n = f"{i:02d}"
        rows.append(
            '<a class="hero-toc-list-a" href="#%s">'
            '<span class="hero-toc-num">%s</span>'
            '<span class="hero-toc-label">%s</span>'
            '<span class="hero-toc-arrow">'
            '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round">'
            '<polyline points="9 6 15 12 9 18"/></svg></span></a>'
            % (sid, n, label)
        )
    return (
        '<aside class="hero-cards mode-physician">\n'
        '<div class="ov-card">\n'
        '<div class="ov-head">'
        '<span class="ov-ico"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round">'
        '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/>'
        '<line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/>'
        '<line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>'
        '</svg></span>'
        '<span class="ov-title">Jump to Clinical Sections</span></div>\n'
        '<div class="hero-toc-list">\n'
        + "\n".join(rows)
        + '\n</div>\n</div>\n</aside>'
    )


def build_figure(picture_or_figure_html):
    """Wrap the relocated picture/img as figure.hero-figure.mode-patient."""
    # If we were given a full <figure>, pull out its inner <picture>/<img>.
    pic = PICTURE_RE.search(picture_or_figure_html)
    if pic:
        inner = pic.group(0)
    else:
        img = re.search(r'<img\b.*?>', picture_or_figure_html, re.IGNORECASE | re.DOTALL)
        inner = img.group(0) if img else picture_or_figure_html
    return (
        '<figure class="hero-figure mode-patient" style="margin:0">\n'
        '<div class="hero-vignette">\n'
        + inner.strip()
        + '\n</div>\n</figure>'
    )


def transform_hero(html):
    """Core transform.

    Returns (new_html, status). status is one of:
      'patched'        — hero rewritten into the themed grid
      'already'        — already themed (hero-grid / markers present)
      'no-hero'        — no <section class="hero">
      'skip:<reason>'  — hero present but did not match the safe pattern
    """
    sec = HERO_SECTION_RE.search(html)
    if not sec:
        return html, "no-hero"

    hero_full = sec.group(0)
    if "hero-grid" in hero_full or START_MARKER in hero_full:
        return html, "already"

    body = sec.group("body")

    cont = CONTAINER_RE.search(body)
    if not cont:
        return html, "skip:no-container"
    # Reject heroes whose container holds more than one container-like wrapper
    # (anything we don't model) by requiring exactly one container open tag.
    if body.count('<div class="container"') != 1:
        return html, "skip:multi-container"

    inner = cont.group("inner")

    # Locate hero-copy pieces. hero-tag and hero-meta are optional in a few
    # guides, but h1 and hero-sub must be present for a safe transform.
    tag_span = matched_block(inner, HERO_TAG_RE, "div")
    meta_span = matched_block(inner, HERO_META_RE, "div")
    h1_span = matched_block(inner, H1_RE, "h1")
    sub_span = matched_block(inner, HERO_SUB_RE, "p")

    if h1_span is None or sub_span is None:
        return html, "skip:missing-h1-or-sub"
    if meta_span is None:
        return html, "skip:missing-meta"

    # The hero-copy is everything from the first copy element through the end of
    # the hero-meta block. Everything after meta (typically an inline figure) is
    # the relocatable tail.
    copy_start = min(s for s in (tag_span, h1_span, sub_span, meta_span)
                     if s is not None)[0]
    copy_end = meta_span[1]

    # Guard: ordering must be sane (meta after h1 after, etc.) — if a hero-sub
    # or h1 appears after meta, the structure is unusual; skip.
    if h1_span[0] >= copy_end or sub_span[0] >= copy_end:
        return html, "skip:unexpected-order"

    head = inner[:copy_start]          # whitespace / decorative bg before copy
    hero_copy_inner = inner[copy_start:copy_end]
    tail = inner[copy_end:]            # may contain an inline figure/picture

    # Relocate an inline figure/picture from the tail (or, rarely, from head).
    figure_html = ""
    fig_m = FIGURE_RE.search(tail) or PICTURE_RE.search(tail)
    if fig_m:
        figure_html = build_figure(fig_m.group(0))
        tail = tail[:fig_m.start()] + tail[fig_m.end():]

    # Whatever remains in head/tail must be only whitespace/comments — otherwise
    # we'd silently drop content. If not, skip defensively.
    leftover = re.sub(r'<!--.*?-->', '', head + tail, flags=re.DOTALL).strip()
    if leftover:
        return html, "skip:unmodeled-content"

    # Build the clinician jump-to card from document anchors.
    anchors = collect_anchors(html)
    jump_card = build_jump_card(anchors)

    aside_parts = []
    if figure_html:
        aside_parts.append(figure_html)
    if jump_card:
        aside_parts.append(jump_card)
    aside_inner = "\n".join(aside_parts)

    new_inner = (
        "\n" + START_MARKER + "\n"
        '<div class="hero-grid">\n'
        '<div class="hero-copy">\n'
        + hero_copy_inner.strip("\n")
        + "\n</div>\n"
        + ('<aside class="hero-aside">\n' + aside_inner + "\n</aside>\n"
           if aside_inner else "")
        + "</div>\n"
        + END_MARKER + "\n"
    )

    new_container = cont.group("open") + new_inner + cont.group("close")
    new_body = body[:cont.start()] + new_container + body[cont.end():]
    new_hero = hero_full[:sec.start("body") - sec.start()] \
        + new_body \
        + hero_full[sec.end("body") - sec.start():]

    new_html = html[:sec.start()] + new_hero + html[sec.end():]
    return new_html, "patched"


def in_scope(name):
    if name in EXCLUDE_EXACT:
        return False
    return not any(name.startswith(p) for p in EXCLUDE_PREFIX)


def process_file(path, dry_run):
    name = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    new_html, status = transform_hero(html)
    if status == "patched":
        if not dry_run:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_html)
        print(f"  patched  {name}")
    elif status == "already":
        print(f"  already  {name} (themed)")
    elif status == "no-hero":
        print(f"  no-hero  {name}")
    else:
        print(f"  SKIP     {name} ({status[5:]})")
    return status


def main():
    ap = argparse.ArgumentParser(
        description="DRAFT: restructure guide heroes into the themed grid layout."
    )
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--guide", help="single guide filename, e.g. understanding-ckd.html")
    args = ap.parse_args()

    if args.guide:
        paths = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        paths = [p for p in sorted(glob.glob(os.path.join(GUIDES_DIR, "*.html")))
                 if in_scope(os.path.basename(p))]

    tally = {}
    for path in paths:
        if not os.path.exists(path):
            print(f"  MISSING  {path}", file=sys.stderr)
            continue
        status = process_file(path, args.dry_run)
        key = status.split(":", 1)[0]
        tally[key] = tally.get(key, 0) + 1

    verb = "would patch" if args.dry_run else "patched"
    print(
        f"\n{verb} {tally.get('patched', 0)}; already {tally.get('already', 0)}; "
        f"skipped {tally.get('skip', 0)}; no-hero {tally.get('no-hero', 0)}."
    )


if __name__ == "__main__":
    main()
