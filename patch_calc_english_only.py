#!/usr/bin/env python3
"""
patch_calc_english_only.py — williamriveromd.com

Calculators are English-only. This strips the multilingual machinery and the
Tagalog/Cebuano/Kapampangan translation spans from every calculator page:

  1. Removes the `setLang`/`wgmr-lang` <script> block (the on-load language
     restore would otherwise hide the English spans and — with the translations
     gone — blank the calculator for a visitor whose last-used language wasn't
     English).
  2. Removes every translation element `<… data-lang="tl|ceb|kap" …>…</…>`
     (depth-aware, so nested markup is removed cleanly), leaving the English
     `data-lang="en"` content in place and visible.

Idempotent. Targets guides/calc-*.html and guides/ckd-dri-calculator.html.

Usage:
    python3 patch_calc_english_only.py
    python3 patch_calc_english_only.py --dry-run
    python3 patch_calc_english_only.py --guide calc-kfre.html
"""

import re
import argparse
from pathlib import Path

# The setLang/lang-restore script block (whole <script> … </script>).
SETLANG_RE = re.compile(
    r"\n?<script>\s*const LANG_KEY\s*=\s*'wgmr-lang';.*?</script>", re.S
)
# Opening tag of any element carrying a non-English data-lang.
LANG_OPEN = re.compile(
    r'<(span|div|p|li|td|th|a|strong|em|h[1-6])\b[^>]*\bdata-lang="(?:tl|ceb|kap)"[^>]*>',
    re.I,
)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def is_calculator(name: str) -> bool:
    return name.startswith("calc-") or name == "ckd-dri-calculator.html"


# On-load language-restore IIFE (the actual blanking risk). Handles both the
# LANG_KEY and GLANG_KEY variants, single- or multi-line.
LANG_IIFE_RE = re.compile(
    r"\n?\(function\(\)\s*\{[^{}]*localStorage\.getItem\(G?LANG_KEY\)[^{}]*"
    r"setLang\([^)]*\)[^{}]*\}\)\(\);",
)
LANG_CONST_RE = re.compile(r"\n?[ \t]*(?://[^\n]*\n[ \t]*)?const \w+\s*=\s*'wgmr-lang';")
# A lang-restore statement embedded inside another IIFE (e.g. a shared dark/
# desktop restorer): `const lang=localStorage.getItem(KEY)||'en';if(lang!=='en')setLang(lang);`
LANG_LINE_RE = re.compile(
    r"\n?[ \t]*(?:const|let|var)\s+lang\s*=\s*localStorage\.getItem\(\w+\)\s*\|\|\s*'en';"
    r"\s*if\s*\(\s*lang\s*!==\s*'en'\s*\)\s*setLang\([^)]*\);"
)


def strip_setlang_pieces(html: str):
    """Remove an embedded setLang() (function, const, on-load restore) that is not
    in its own <script> block."""
    changed = False
    html, n = LANG_IIFE_RE.subn("", html)
    changed = changed or bool(n)
    html, n = LANG_LINE_RE.subn("", html)
    changed = changed or bool(n)
    # function setLang(...) { ... } — brace-matched so nested {} are handled.
    fn = re.compile(r"\n?function setLang\([^)]*\)\s*\{")
    m = fn.search(html)
    while m:
        depth, k = 1, html.index("{", m.start()) + 1
        while k < len(html) and depth > 0:
            c = html[k]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            k += 1
        html = html[:m.start()] + html[k:]
        changed = True
        m = fn.search(html)
    html, n = LANG_CONST_RE.subn("", html)
    changed = changed or bool(n)
    return html, changed


def strip_translation_elements(html: str):
    """Remove every <tag data-lang="tl|ceb|kap">…</tag> with correct nesting."""
    removed = 0
    while True:
        m = LANG_OPEN.search(html)
        if not m:
            break
        tag = m.group(1).lower()
        open_re = re.compile(r'<' + tag + r'\b', re.I)
        close = '</' + tag + '>'
        start, j, depth = m.start(), m.end(), 1
        while j < len(html) and depth > 0:
            no = open_re.search(html, j)
            nc = html.find(close, j)
            if nc == -1:
                j = len(html)
                break
            if no and no.start() < nc:
                depth += 1
                j = no.end()
            else:
                depth -= 1
                j = nc + len(close)
        html = html[:start] + html[j:]
        removed += 1
    return html, removed


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    new_text, n = SETLANG_RE.subn("", text)
    if n:
        text = new_text
        changes.append("removed setLang block")
    # Handle setLang embedded mid-script (not its own block) and any dangling
    # lang-restore statements / 'wgmr-lang' consts left behind.
    if "setLang" in text or "'wgmr-lang'" in text:
        text, did = strip_setlang_pieces(text)
        if did:
            changes.append("removed embedded setLang")

    text, removed = strip_translation_elements(text)
    if removed:
        changes.append(f"stripped {removed} translation span(s)")

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ " + ", ".join(changes)


def main():
    ap = argparse.ArgumentParser(description="Make calculators English-only.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="patch a single calculator (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    targets = ([guides_dir / args.guide] if args.guide
               else sorted(p for p in guides_dir.glob("*.html") if is_calculator(p.name)))

    changed = 0
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found"); continue
        if not is_calculator(path.name):
            continue
        status = patch_guide(path, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {changed} calculator(s).")


if __name__ == "__main__":
    main()
