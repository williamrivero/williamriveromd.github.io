#!/usr/bin/env python3
"""Move <figure class="hero-figure"> back INSIDE <div class="hero-grid">.

A guide that authors the figure as a sibling of the grid (rather than a child)
breaks the hero layout: the disc falls below the copy column instead of
sitting in its grid slot. Per CLAUDE.md rule 4, hero-grid's only allowed
direct children are .hero-copy, .hero-cards, .hero-figure, .hero-toc.

This script:
  1. Finds the <div class="hero-grid"> opener and the next </div> that closes it
     (tracking depth so nested divs don't confuse the matcher).
  2. Locates the FIRST <figure ... hero-figure ...> ... </figure> AFTER that
     closing </div> (but within the next ~6000 chars to avoid running off the
     page).
  3. Lifts the entire figure block, removes it from its outside position, and
     inserts it just BEFORE the closing </div> of hero-grid.

Idempotent: if the figure is already inside the grid, the file is left alone.
"""
import re
import sys
import pathlib

GUIDES_DIR = pathlib.Path(__file__).parent / "guides"


def find_matching_close(src: str, open_pos: int) -> int:
    """Given the index of the opening tag, walk forward to find the matching
    </div>. Returns the start index of the matching </div>."""
    depth = 1
    i = open_pos
    while i < len(src) and depth > 0:
        d_open = src.find("<div", i)
        d_close = src.find("</div>", i)
        if d_close == -1:
            return -1
        if d_open != -1 and d_open < d_close:
            depth += 1
            i = d_open + 4
        else:
            depth -= 1
            close_start = d_close
            i = d_close + 6
    return close_start


FIG_RE = re.compile(
    r'<figure[^>]*\bhero-figure\b[^>]*>.*?</figure>\s*',
    re.DOTALL,
)


def patch(src: str) -> str | None:
    m = re.search(r'<div class="hero-grid"[^>]*>', src)
    if not m:
        return None
    grid_open_end = m.end()
    grid_close_start = find_matching_close(src, grid_open_end)
    if grid_close_start == -1:
        return None
    grid_body = src[grid_open_end:grid_close_start]
    # Already inside?
    if re.search(r'<figure[^>]*\bhero-figure\b', grid_body):
        return None
    # Find figure AFTER the grid close
    after = src[grid_close_start:]
    fm = FIG_RE.search(after, 0, 6000)
    if not fm:
        return None
    figure_block = fm.group(0).rstrip() + "\n"
    abs_start = grid_close_start + fm.start()
    abs_end = grid_close_start + fm.end()
    # Remove the figure from its old position; insert at the END of the grid
    new_src = src[:abs_start] + src[abs_end:]
    # Recompute close position (it shifted by the removed length)
    shift = -(abs_end - abs_start)
    new_close = grid_close_start  # close didn't move (figure was after it)
    return new_src[:new_close] + figure_block + new_src[new_close:]


def main():
    dry = "--dry-run" in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--guide" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]
    targets = sorted(GUIDES_DIR.glob("*.html"))
    if only:
        targets = [GUIDES_DIR / only]
    changed = 0
    for p in targets:
        s = p.read_text(encoding="utf-8")
        out = patch(s)
        if out is None or out == s:
            continue
        changed += 1
        print(f"  {p.name:55s} → {'would move' if dry else 'figure moved into hero-grid'}")
        if not dry:
            p.write_text(out, encoding="utf-8")
    print(f"\nSummary: {changed} file(s) {'would be ' if dry else ''}changed")


if __name__ == "__main__":
    main()
