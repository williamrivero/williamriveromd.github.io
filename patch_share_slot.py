#!/usr/bin/env python3
"""Reserve the hero share row's space before first paint (CLS fix, Nov 27 2026).

assets/share-buttons.js is deferred, so its hero icon row arrived after the page
had painted and pushed the hero text down (Cloudflare: CLS 0.44 on the calculators
index, where the row sits under the title). This script writes an empty
placeholder exactly where the script puts the row:

    <div class="rcm-share-slot" aria-hidden="true"></div>

after every .hero-meta (or, with none, after the first <h1> / its .hero-tagline:
the same anchors the script uses). A small <style> right after the first slot sizes it
to the row's height: one line (34 px) on wider screens, two lines (74 px) on phones,
where the row wraps. The script fills the slot instead of inserting a new element,
so nothing moves.

Covers guides/ and academy/ (pages that load share-buttons.js). Idempotent.

  python3 patch_share_slot.py              # guides/ + academy/
  python3 patch_share_slot.py --dry-run
  python3 patch_share_slot.py --check      # exit 1 if any page needs a change
  python3 patch_share_slot.py --guide calculators.html
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DIRS = ["guides", "academy"]
MARK = "share-buttons"
SLOT = '<div class="rcm-share-slot" aria-hidden="true"></div>'
CSS = (
    '<style id="rcm-share-slot-css">'
    ".rcm-share-slot:empty{display:block;margin:12px 0 0;height:34px}"
    "@media (max-width:420px){.rcm-share-slot:empty{height:74px}}"
    "@media (max-width:480px) and (hover:none){.rcm-share-slot:empty{height:74px}}"
    ".rcm-share+.rcm-share-slot:empty{display:none}"
    "@media print{.rcm-share-slot:empty{display:none}}"
    "</style>"
)
OLD_SLOT = re.compile(r'\n?<div class="(?:rcm-share )?rcm-share-slot" aria-hidden="true"></div>')
OLD_CSS = re.compile(r'<style id="rcm-share-slot-css">.*?</style>', re.S)
HERO_META = re.compile(r'<(\w+)\b[^>]*\bclass="[^"]*(?<![\w-])hero-meta(?![\w-])[^"]*"[^>]*>')
H1 = re.compile(r"<h1\b[^>]*>", re.I)
TAGLINE = re.compile(r'\s*(?:<!--.*?-->\s*)*<p\b[^>]*\bclass="[^"]*(?<![\w-])hero-tagline(?![\w-])', re.S)
# Regions the browser does not turn into live elements
DEAD = re.compile(r"<(script|style|template|textarea)\b.*?</\1>|<!--.*?-->", re.S | re.I)


def element_end(text, start, tag):
    """Index just past the closing tag matching the opening tag at start."""
    pat = re.compile(r"<(/?)" + tag + r"\b[^>]*>", re.I)
    depth = 0
    for m in pat.finditer(text, start):
        if m.group(0).endswith("/>"):
            continue
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    return -1


def anchors(text):
    dead = [(m.start(), m.end()) for m in DEAD.finditer(text)]
    live = lambda i: not any(a <= i < b for a, b in dead)
    ends = []
    for m in HERO_META.finditer(text):
        if live(m.start()):
            e = element_end(text, m.start(), m.group(1))
            if e > 0:
                ends.append(e)
    # nested .hero-meta inside another one: keep the outer ends only
    ends = sorted(set(ends))
    if ends:
        return ends
    for m in H1.finditer(text):
        if not live(m.start()):
            continue
        e = element_end(text, m.start(), "h1")
        if e < 0:
            return []
        t = TAGLINE.match(text, e)
        if t:
            p0 = text.find("<p", e)
            e2 = element_end(text, p0, "p")
            if e2 > 0:
                e = e2
        return [e]
    return []


def patch(text):
    if MARK not in text:
        return text, "no-share"
    base = OLD_SLOT.sub("", OLD_CSS.sub("", text))
    pts = anchors(base)
    if not pts:
        return text, "no-anchor"
    out, prev = [], 0
    for i, e in enumerate(pts):
        out.append(base[prev:e])
        out.append("\n" + SLOT + (CSS if i == 0 else ""))
        prev = e
    out.append(base[prev:])
    new = "".join(out)
    return new, ("unchanged" if new == text else "patched")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    files = []
    for d in DIRS:
        files += sorted((ROOT / d).glob("*.html"))
    if a.guide:
        files = [f for f in files if f.name == a.guide]
    counts, odd = {}, []
    for f in files:
        text = f.read_text(encoding="utf-8")
        new, st = patch(text)
        counts[st] = counts.get(st, 0) + 1
        if st == "no-anchor":
            odd.append(f.relative_to(ROOT))
        if st == "patched" and not (a.dry_run or a.check):
            f.write_text(new, encoding="utf-8")
    print(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    for o in odd:
        print("  no hero anchor:", o)
    if a.check and counts.get("patched"):
        sys.exit(1)


if __name__ == "__main__":
    main()
