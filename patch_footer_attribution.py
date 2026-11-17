#!/usr/bin/env python3
"""
patch_footer_attribution.py — renalcarematters.com

Nov 18 2026 (Dr. Rivero): guides and calculators carry no author panel. The author block
(.dr-card-wrap) is hidden by MASTER_CSS, and every page footer is reduced to
  * the page's safety / use disclaimer (if it has one), and
  * one credit line: <p class="rcm-attrib">© 2026 <a href="https://renalcarematters.com">renalcarematters.com</a></p>
Author names, credentials, specialty lines, booking links, mottoes, footer reference lists
(deprecated, rule 5) and footer nav links are dropped. Hub pages keep their own footers.
Idempotent.

Usage:
    python3 patch_footer_attribution.py
    python3 patch_footer_attribution.py --dry-run
    python3 patch_footer_attribution.py --guide igan-guide.html
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
YEAR = "2026"
SKIP = {"index.html", "calculators.html"}
STD = f'<p class="rcm-attrib">© {YEAR} <a href="https://renalcarematters.com">renalcarematters.com</a></p>'
FOOTER = re.compile(r'(<footer class="guide-footer"[^>]*>)(.*?)(</footer>)', re.S)
DISCLAIMER = re.compile(r"educational|not a substitute|medical advice|decision support|distributed freely|"
                        r"emergency|professional[- ]use|planning use|not a dosing|clinical judg", re.I)
AUTHOR = re.compile(
    r"(?:©|&copy;)?\s*(?:Dr\.?\s*)?(?:William\s+Gregory\s+M\.?|W\.?\s*G\.?\s*M\.?|W\.?)\s*Rivero,?\s*MD"
    r"(?:\s*(?:,|·|&middot;)\s*(?:FPCP|DPSN))*", re.I)
SPECIALTY = re.compile(r"(?:&mdash;|—|·|&middot;)?\s*Internal Medicine\s*(?:·|&middot;)\s*Nephrology\s*(?:·|&middot;)\s*Clinical Nutrition", re.I)
SEP = r"(?:\s*(?:·|&middot;|—|&mdash;|\|)\s*)"


def clean(seg: str) -> str:
    seg = AUTHOR.sub("", seg)
    seg = SPECIALTY.sub("", seg)
    seg = re.sub(r"<a [^>]*>\s*Book[^<]*</a>", "", seg, flags=re.I)
    seg = re.sub(r"(?:©|&copy;)\s*20\d\d(?:\s*[–-]\s*20\d\d)?\s*(?:renalcarematters\.com|<a [^>]*>renalcarematters\.com</a>)?", "", seg)
    seg = re.sub(r"^(?:" + SEP + r")+|(?:" + SEP + r")+$", "", seg.strip())
    seg = re.sub(r"(?:" + SEP + r"){2,}", " · ", seg)
    return seg.strip()


def rebuild(inner: str) -> str:
    inner = re.sub(r"<!--.*?-->", "", inner, flags=re.S)
    inner = re.sub(r"<script\b.*?</script>", "", inner, flags=re.S)
    parts = re.split(r"</?(?:p|div|br|ul|li|nav|section)\b[^>]*>", inner)
    keep = []
    for seg in parts:
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", seg)).strip()
        if not text or not DISCLAIMER.search(text):
            continue
        seg = clean(seg)
        if re.sub(r"<[^>]+>|\s", "", seg) and seg not in keep:
            keep.append(seg)
    body = "".join(f'\n<p class="rcm-disclaimer">{s}</p>' for s in keep)
    return '\n<div class="footer-inner">' + body + "\n" + STD + "\n</div>\n"


def patch(text: str) -> str:
    return FOOTER.sub(lambda m: m.group(1) + rebuild(m.group(2)) + m.group(3), text, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    files = [ROOT / "guides" / a.guide] if a.guide else sorted(
        p for p in (ROOT / "guides").glob("*.html") if p.name not in SKIP)
    n = 0
    for p in files:
        t = p.read_text(encoding="utf-8")
        t2 = patch(t)
        if t2 != t:
            n += 1
            if not a.dry_run:
                p.write_text(t2, encoding="utf-8")
    print(("[dry-run] " if a.dry_run else "") + f"{n} footer(s) updated of {len(files)} page(s)")


if __name__ == "__main__":
    main()
