#!/usr/bin/env python3
"""Audit the clinician hero Summary abstract on dual-mode guides (CLAUDE.md rule 14).

Every guide with a Clinicians tab (id="tab-md") must carry exactly one
<div class="hero-abstract ..."> in its clinician hero, with:
  - a <div class="ha-label">Summary</div> label,
  - 2–3 <p> paragraphs, each opening with a bold lead (<strong>Lead.</strong>),
  - at most 130 English words in total,
  - placement in the hero (before the first content section), not in the body.

Usage:
  python3 audit_hero_abstract.py                 # all dual-mode guides; exits 1 on any problem
  python3 audit_hero_abstract.py --guide igan-guide.html
"""
import argparse, html, pathlib, re, sys

GUIDES = pathlib.Path(__file__).resolve().parent / "guides"
MAX_WORDS = 130


def check(path: pathlib.Path):
    s = path.read_text(encoding="utf-8")
    if 'id="tab-md"' not in s or path.name.startswith("calc-"):
        return None  # not a dual-mode guide
    blocks = list(re.finditer(r'<div class="hero-abstract[^"]*"[^>]*>(.*?)\n\s*</div>\n', s, re.S))
    if not blocks:
        return ["missing hero-abstract"]
    probs = []
    if len(blocks) > 1:
        probs.append(f"{len(blocks)} hero-abstract blocks (expected 1)")
    m = blocks[0]
    body = m.group(1)
    if not re.search(r'<div class="ha-label">\s*Summary\s*</div>', body):
        probs.append('no <div class="ha-label">Summary</div>')
    paras = re.findall(r"<p>(.*?)</p>", body, re.S)
    if not 2 <= len(paras) <= 3:
        probs.append(f"{len(paras)} paragraphs (expected 2–3)")
    for p in paras:
        if not re.match(r"\s*<strong>[^<]+\.</strong>", p):
            probs.append("paragraph without a bold lead (<strong>Lead.</strong>)")
            break
    words = len(html.unescape(re.sub(r"<[^>]+>", " ", " ".join(paras))).split())
    if words > MAX_WORDS:
        probs.append(f"{words} words (max {MAX_WORDS})")
    first_section = s.find('<section class="section"')
    if first_section != -1 and m.start() > first_section:
        # clinician heroes inside a .mode-physician wrapper sit after patient sections;
        # accept if the block is inside a hero / md-hero container
        before = s[:m.start()]
        last_hero = max(before.rfind('<section class="hero'), before.rfind('class="md-hero'))
        last_section = before.rfind('<section class="section"')
        if last_hero < last_section:
            probs.append("abstract is in the body, not the clinician hero")
    return probs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guide")
    a = ap.parse_args()
    files = [GUIDES / a.guide] if a.guide else sorted(GUIDES.glob("*.html"))
    checked = bad = 0
    for f in files:
        r = check(f)
        if r is None:
            continue
        checked += 1
        if r:
            bad += 1
            print(f"✗ {f.name}: " + "; ".join(r))
    print(f"\n=== Clinician hero Summary audit ===\nDual-mode guides checked: {checked}\nWith problems:            {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
