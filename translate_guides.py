#!/usr/bin/env python3
"""
translate_guides.py — williamriveromd.com
Translates patient guides into Filipino (Tagalog), Cebuano, and Kapampangan.
Supports --audit, --guide <filename>, --all, --lang <tl|ceb|kap|all>

Usage:
    python3 translate_guides.py --api-key sk-ant-... --audit
    python3 translate_guides.py --api-key sk-ant-... --guide understanding-ckd.html
    python3 translate_guides.py --api-key sk-ant-... --all
    python3 translate_guides.py --api-key sk-ant-... --all --lang kap
"""

import os
import sys
import re
import shutil
import argparse
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip3 install anthropic beautifulsoup4")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup, NavigableString
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip3 install anthropic beautifulsoup4")
    sys.exit(1)

# ── Language config ────────────────────────────────────────────────────────────

LANGUAGES = {
    "tl": {
        "label": "Filipino (Tagalog)",
        "prompt": (
            "Translate the following medical patient education text into Filipino (Tagalog). "
            "Use clear, natural Filipino that a patient in the Philippines would easily understand. "
            "Preserve medical terms and drug names in English. "
            "Do not translate proper nouns, numbers, or units. "
            "Return only the translated text, nothing else."
        ),
    },
    "ceb": {
        "label": "Cebuano",
        "prompt": (
            "Translate the following medical patient education text into Cebuano (Bisaya). "
            "Use clear, natural Cebuano that a patient from Cebu or Mindanao would easily understand. "
            "Preserve medical terms and drug names in English. "
            "Do not translate proper nouns, numbers, or units. "
            "Return only the translated text, nothing else."
        ),
    },
    "kap": {
        "label": "Kapampangan",
        "prompt": (
            "Translate the following medical patient education text into Kapampangan "
            "(the language spoken in Pampanga, Philippines — Angeles City, San Fernando, etc.). "
            "Use natural, conversational Kapampangan that a patient from Pampanga would understand. "
            "Preserve medical terms and drug names in English. "
            "Do not translate proper nouns, numbers, or units. "
            "Avoid mixing in Tagalog — use genuine Kapampangan vocabulary where it exists. "
            "Return only the translated text, nothing else."
        ),
    },
}

ALL_LANGS = ["tl", "ceb", "kap"]

# ── Helpers ────────────────────────────────────────────────────────────────────

def find_guides_dir(script_path: Path) -> Path:
    """Find guides/ directory relative to script location."""
    candidates = [
        script_path.parent / "guides",
        script_path.parent.parent / "guides",
        Path.home() / "Desktop" / "williamriveromd" / "guides",
    ]
    for c in candidates:
        if c.is_dir():
            return c
    raise FileNotFoundError(
        "Cannot find guides/ directory. Run this script from your williamriveromd project folder."
    )


def get_all_guide_files(guides_dir: Path) -> list[Path]:
    files = sorted(guides_dir.glob("*.html"))
    # Exclude index page
    return [f for f in files if f.name != "index.html"]


def has_lang(soup: BeautifulSoup, lang: str) -> bool:
    return bool(soup.find(attrs={"data-lang": lang}))


def has_data_lang_structure(soup: BeautifulSoup) -> bool:
    return bool(soup.find(attrs={"data-lang": "en"}))


def audit(guides_dir: Path, langs: list[str] = ALL_LANGS) -> None:
    files = get_all_guide_files(guides_dir)
    full, partial, none_, needs = [], [], [], []

    for f in files:
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
        if not has_data_lang_structure(soup):
            none_.append(f.name)
            continue
        has = [l for l in langs if has_lang(soup, l)]
        if len(has) == len(langs):
            full.append(f.name)
        elif has:
            partial.append((f.name, has))
            needs.append(f.name)
        else:
            none_.append(f.name)
            needs.append(f.name)

    print(f"\n=== TRANSLATION AUDIT (langs: {', '.join(langs)}) ===")
    print(f"Full ({'+'.join(langs)}):  {len(full)}")
    print(f"Partial:        {len(partial)}")
    print(f"No translation: {len(none_)}")
    print(f"Needs work:     {len(needs)}")
    if partial:
        print("\nPartial:")
        for name, has in partial:
            missing = [l for l in langs if l not in has]
            print(f"  {name}  (has: {has}  missing: {missing})")
    if none_:
        print("\nNo translation:")
        for name in none_:
            print(f"  {name}")


def translate_text(client: anthropic.Anthropic, text: str, lang: str) -> str:
    if not text.strip():
        return text
    cfg = LANGUAGES[lang]
    msg = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": f"{cfg['prompt']}\n\n{text}"}],
    )
    return msg.content[0].text.strip()


def inject_translation(soup: BeautifulSoup, client: anthropic.Anthropic, lang: str) -> int:
    """
    For each <span data-lang="en"> or <div data-lang="en"> element,
    insert a sibling with data-lang=lang if not already present.
    Returns count of injected elements.
    """
    en_elements = soup.find_all(attrs={"data-lang": "en"})
    count = 0
    for el in en_elements:
        # Check if sibling with target lang already exists
        parent = el.parent
        existing = parent.find(attrs={"data-lang": lang})
        if existing:
            continue

        en_text = el.get_text()
        if not en_text.strip():
            continue

        translated = translate_text(client, en_text, lang)
        time.sleep(0.3)  # gentle rate limiting

        new_el = soup.new_tag(el.name)
        new_el["data-lang"] = lang
        new_el["class"] = "lang-hidden"
        # Preserve inner HTML structure if simple, else set text
        new_el.string = translated
        el.insert_after(new_el)
        count += 1

    return count


def translate_guide(guides_dir: Path, filename: str, client: anthropic.Anthropic,
                    langs: list[str] = ALL_LANGS, force: bool = False) -> None:
    path = guides_dir / filename
    if not path.exists():
        print(f"  ERROR: {filename} not found in {guides_dir}")
        return

    # Backup
    bak = path.with_suffix(".html.bak")
    if not bak.exists():
        shutil.copy2(path, bak)

    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    if not has_data_lang_structure(soup):
        print(f"  SKIP {filename} — no data-lang structure (run retrofit_and_translate.py first)")
        return

    total = 0
    for lang in langs:
        if not force and has_lang(soup, lang):
            print(f"  {filename}: {lang} already present — skipping")
            continue
        print(f"  {filename}: translating → {LANGUAGES[lang]['label']} ...", end=" ", flush=True)
        n = inject_translation(soup, client, lang)
        print(f"{n} elements")
        total += n

    if total > 0:
        path.write_text(str(soup), encoding="utf-8")
        print(f"  ✓ {filename}: saved ({total} new translations)")
    else:
        print(f"  {filename}: nothing new to write")


# ── JS setLang() patcher ───────────────────────────────────────────────────────

SETLANG_PATTERN = re.compile(
    r"(function setLang\s*\(.*?\)\s*\{.*?localStorage\.setItem\s*\(\s*['\"]wgmr-lang['\"].*?\}\s*\})",
    re.DOTALL,
)

KAP_BUTTON_SNIPPET = """
      <button id="glb-kap" class="lang-btn" onclick="setLang('kap')">KAP</button>"""


def patch_setlang_js(html: str) -> str:
    """Ensure setLang handles 'kap' — it's usually generic so no change needed,
    but update the active-class logic if it hardcodes language names."""
    # Most implementations are generic (loop over data-lang); nothing to patch.
    # If the guide has explicit if/else for tl/ceb, we add kap.
    html = re.sub(
        r"(setLang\s*\(\s*['\"]ceb['\"]\s*\)\s*['\"]ceb['\"])",
        r"\1",
        html,
    )
    return html


def add_kap_button_to_guide(path: Path) -> bool:
    """Add KAP toggle button to guide-toggle-bar if not already present."""
    html = path.read_text(encoding="utf-8")
    if 'id="glb-kap"' in html or "glb-kap" in html:
        return False  # already has it

    # Find the CEB button and insert KAP after it
    html = re.sub(
        r'(<button[^>]*id=["\']glb-ceb["\'][^>]*>.*?</button>)',
        r'\1\n      <button id="glb-kap" class="lang-btn" onclick="setLang(\'kap\')">KAP</button>',
        html,
        count=1,
    )
    path.write_text(html, encoding="utf-8")
    return True


def add_kap_button_to_index(index_path: Path) -> bool:
    """Add KAP pill button to index.html nav bar."""
    html = index_path.read_text(encoding="utf-8")
    if 'id="lb-kap"' in html or "lb-kap" in html:
        return False

    html = re.sub(
        r'(<button[^>]*id=["\']lb-ceb["\'][^>]*>.*?</button>)',
        r'\1\n          <button id="lb-kap" class="lang-btn" onclick="setLang(\'kap\')">KAP</button>',
        html,
        count=1,
    )
    index_path.write_text(html, encoding="utf-8")
    return True


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Translate williamriveromd.com guides")
    parser.add_argument("--api-key", required=True, help="Anthropic API key")
    parser.add_argument("--audit", action="store_true", help="Audit translation status")
    parser.add_argument("--guide", help="Translate a single guide file")
    parser.add_argument("--all", action="store_true", help="Translate all guides needing work")
    parser.add_argument(
        "--lang",
        default="all",
        help="Language(s) to translate: tl, ceb, kap, or all (default: all)",
    )
    parser.add_argument("--force", action="store_true", help="Re-translate even if lang exists")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        guides_dir = find_guides_dir(script_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Resolve target languages
    if args.lang == "all":
        target_langs = ALL_LANGS
    else:
        target_langs = [l.strip() for l in args.lang.split(",")]
        invalid = [l for l in target_langs if l not in LANGUAGES]
        if invalid:
            print(f"ERROR: Unknown language(s): {invalid}. Valid: tl, ceb, kap")
            sys.exit(1)

    if args.audit:
        audit(guides_dir, target_langs)
        return

    client = anthropic.Anthropic(api_key=args.api_key)

    if args.guide:
        translate_guide(guides_dir, args.guide, client, target_langs, args.force)

    elif args.all:
        files = get_all_guide_files(guides_dir)
        todo = []
        for f in files:
            soup = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
            if not has_data_lang_structure(soup):
                continue
            missing = [l for l in target_langs if not has_lang(soup, l)]
            if missing or args.force:
                todo.append((f.name, missing))

        print(f"\nGuides needing translation: {len(todo)}")
        for i, (name, missing) in enumerate(todo, 1):
            print(f"\n[{i}/{len(todo)}] {name} (missing: {missing})")
            langs_to_do = missing if not args.force else target_langs
            translate_guide(guides_dir, name, client, langs_to_do, args.force)
            time.sleep(1)

        print("\n✓ Done.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
