#!/usr/bin/env python3
"""
fix_setlang_kap.py — williamriveromd.com
Patches the setLang() JavaScript function in all guide pages and index.html
to include 'kap' in the language loop array.

Also patches the lang attribute setter to handle 'kap'.

Usage:
    python3 fix_setlang_kap.py
    python3 fix_setlang_kap.py --dry-run
"""

import re
import sys
import argparse
from pathlib import Path


def find_project_dir(script_path: Path) -> Path:
    candidates = [
        script_path.parent,
        script_path.parent.parent,
        Path.home() / "Desktop" / "williamriveromd",
    ]
    for c in candidates:
        if (c / "guides").is_dir() and (c / "index.html").exists():
            return c
    raise FileNotFoundError("Cannot find williamriveromd project root.")


def patch_file(path: Path, dry_run: bool = False) -> str:
    html = path.read_text(encoding="utf-8")
    original = html
    changes = []

    # ── Patch 1: ['en','tl','ceb'] → ['en','tl','ceb','kap'] ──────────────────
    # Handles various quote/spacing styles
    patterns_1 = [
        (r"\['en','tl','ceb'\]", "['en','tl','ceb','kap']"),
        (r'\["en","tl","ceb"\]', '["en","tl","ceb","kap"]'),
        (r"\[ *'en', *'tl', *'ceb' *\]", "['en','tl','ceb','kap']"),
        (r'\[ *"en", *"tl", *"ceb" *\]', '["en","tl","ceb","kap"]'),
    ]
    for pattern, replacement in patterns_1:
        if re.search(pattern, html) and 'kap' not in re.search(pattern, html).group():
            html = re.sub(pattern, replacement, html)
            changes.append("patched lang array")
            break

    # ── Patch 2: lang attribute setter — add kap handling ─────────────────────
    # Pattern: lang === 'tl' ? 'tl' : lang === 'ceb' ? 'ceb' : 'en'
    old_attr = r"lang === 'tl' \? 'tl' : lang === 'ceb' \? 'ceb' : 'en'"
    new_attr = "lang === 'tl' ? 'tl' : lang === 'ceb' ? 'ceb' : lang === 'kap' ? 'kap' : 'en'"
    if re.search(old_attr, html):
        html = re.sub(old_attr, new_attr, html)
        changes.append("patched lang attribute setter")

    # Also handle simpler version without tl/ceb
    old_attr2 = r"document\.documentElement\.setAttribute\('lang', *lang\)"
    # This is already generic — no patch needed

    # ── Patch 3: homepage button array lb-en/lb-tl/lb-ceb ────────────────────
    old_lb = r"\['lb-en','lb-tl','lb-ceb'\]"
    new_lb = "['lb-en','lb-tl','lb-ceb','lb-kap']"
    if re.search(old_lb, html) and 'lb-kap' not in html:
        html = re.sub(old_lb, new_lb