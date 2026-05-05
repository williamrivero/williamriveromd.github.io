#!/usr/bin/env python3
"""
retrofit_and_translate.py
=========================
Retrofits guides that have NO data-lang attributes by:
1. Wrapping translatable text in data-lang="en" spans
2. Translating to Filipino and Cebuano
3. Inserting translated siblings

Usage:
    python3 retrofit_and_translate.py --api-key sk-ant-... --guide acute-kidney-injury-on-ckd.html
    python3 retrofit_and_translate.py --api-key sk-ant-... --all
"""

import os, sys, re, time, argparse
from pathlib import Path
from copy import copy

try:
    import anthropic
except ImportError:
    print("Run: pip3 install anthropic beautifulsoup4"); sys.exit(1)

try:
    from bs4 import BeautifulSoup, Tag, NavigableString
except ImportError:
    print("Run: pip3 install beautifulsoup4"); sys.exit(1)

GUIDES_DIR = Path.home() / "Desktop/williamriveromd/guides"

# Tags whose direct text content should be translated
TRANSLATE_TAGS = {'p', 'h2', 'h3', 'h4', 'li', 'td', 'th', 'div', 'span', 'strong', 'em'}
# Tags to skip entirely
SKIP_TAGS = {'script', 'style', 'code', 'pre', 'svg', 'img', 'input', 'button', 'a'}
# Classes that indicate non-translatable content
SKIP_CLASSES = {'section-tag', 'stat-value', 'stat-label', 'badge', 'pill',
                'lab-val', 'value', 'unit', 'icd', 'code', 'tag'}

SYSTEM_PROMPT = """You are a medical translator for Philippine patient education materials.
Rules:
- Translate naturally for patients
- Keep medical terms in English with brief local explanation on first use
- Never translate: drug names, brand names, numbers, units (mg/mL/g/%), URLs, emails, names
- Filipino: natural Metro Manila Tagalog
- Cebuano: standard Visayan/Bisaya
- Return ONLY the translated text — preserve all HTML tags exactly
- No explanations, no preamble"""


def should_skip(el):
    """Return True if this element should not be translated."""
    if not isinstance(el, Tag):
        return True
    if el.name in SKIP_TAGS:
        return True
    classes = set(el.get('class', []))
    if classes & SKIP_CLASSES:
        return True
    if el.get('data-lang'):
        return True
    return False


def get_translatable_elements(soup):
    """
    Find elements that contain translatable text and are NOT already
    wrapped in data-lang structure.
    Returns list of (element, inner_html) tuples.
    """
    results = []
    seen_ids = set()

    # Target: p, h2, h3, h4 inside .section divs
    # Also: section-tag divs, intro-callout p, alert p, feature-card p
    for el in soup.find_all(['p', 'h2', 'h3', 'h4', 'li', 'div']):
        if should_skip(el):
            continue

        # Skip if already has data-lang children
        if el.find(attrs={"data-lang": True}):
            continue

        # Skip if this element itself has data-lang
        if el.get('data-lang'):
            continue

        # Skip if it's a structural div (has block children)
        if el.name == 'div':
            has_block_children = any(
                isinstance(c, Tag) and c.name in {'div', 'section', 'p', 'h2', 'h3', 'ul', 'ol', 'table'}
                for c in el.children
            )
            if has_block_children:
                continue
            # Only translate specific div classes
            classes = set(el.get('class', []))
            translatable_div_classes = {'section-tag', 'intro-callout', 'alert-teal',
                                         'alert-amber', 'alert-green', 'alert-red',
                                         'feature-text', 'card-body', 'disclaimer'}
            if not (classes & translatable_div_classes) and el.name == 'div':
                continue

        # Get inner HTML
        inner = el.decode_contents().strip()
        if not inner or len(inner) < 3:
            continue

        # Skip if it's pure numbers/symbols
        if re.match(r'^[\d\s\.\,\%\+\-\/\(\)]+$', re.sub(r'<[^>]+>', '', inner)):
            continue

        el_id = id(el)
        if el_id not in seen_ids:
            seen_ids.add(el_id)
            results.append(el)

    return results


def translate_batch(client, texts, lang, context):
    if not texts:
        return []
    lang_name = "Filipino (Tagalog)" if lang == "tl" else "Cebuano (Bisaya)"
    numbered = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts))
    prompt = f"""Translate each item from English to {lang_name}.
Guide: {context}
Return ONLY numbered list, same format.

{numbered}"""
    try:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.content[0].text.strip()
        lines = [re.sub(r"^\d+\.\s*", "", l.strip()) for l in result.split("\n") if l.strip()]
        while len(lines) < len(texts):
            lines.append(texts[len(lines)])
        return lines[:len(texts)]
    except Exception as e:
        print(f"\n    API error: {e}")
        return texts


def retrofit_guide(html, client, guide_name):
    """Retrofit a guide with data-lang structure and translations."""
    soup = BeautifulSoup(html, 'html.parser')

    # Check if already has data-lang
    if soup.find(attrs={"data-lang": "en"}):
        print(f"  Already has data-lang structure — use translate_guides.py instead")
        return html, False

    elements = get_translatable_elements(soup)
    if not elements:
        print(f"  WARN: No translatable elements found")
        return html, False

    print(f"  Found {len(elements)} translatable elements")

    # Get inner HTML for each element
    texts = [el.decode_contents().strip() for el in elements]

    BATCH = 25

    def do_batches(lang):
        result = []
        for i in range(0, len(texts), BATCH):
            chunk = texts[i:i+BATCH]
            b = i//BATCH + 1
            total = (len(texts)-1)//BATCH + 1
            print(f"    {lang}: batch {b}/{total} ({len(chunk)} items)...", end=" ", flush=True)
            translated = translate_batch(client, chunk, lang, guide_name)
            result.extend(translated)
            print("done")
            if i + BATCH < len(texts):
                time.sleep(0.5)
        return result

    print(f"  → Filipino:")
    tl_translations = do_batches("tl")
    print(f"  → Cebuano:")
    ceb_translations = do_batches("ceb")

    # Now wrap each element and insert translations
    # Re-find elements after potential soup modification
    fresh_elements = get_translatable_elements(soup)

    inserted = 0
    for el, tl_text, ceb_text in zip(fresh_elements, tl_translations, ceb_translations):
        tag = el.name
        original_html = el.decode_contents()
        original_classes = el.get('class', [])

        # Add data-lang="en" to the original element
        el['data-lang'] = 'en'

        # Create Filipino sibling
        tl_tag = soup.new_tag(tag)
        tl_tag['data-lang'] = 'tl'
        tl_tag['class'] = original_classes + ['lang-hidden']
        tl_tag.append(BeautifulSoup(tl_text, 'html.parser'))
        el.insert_after(tl_tag)

        # Create Cebuano sibling after Filipino
        ceb_tag = soup.new_tag(tag)
        ceb_tag['data-lang'] = 'ceb'
        ceb_tag['class'] = original_classes + ['lang-hidden']
        ceb_tag.append(BeautifulSoup(ceb_text, 'html.parser'))
        tl_tag.insert_after(ceb_tag)

        inserted += 1

    print(f"  Retrofitted {inserted} elements with data-lang structure")

    updated = str(soup)
    if html.lower().startswith('<!doctype') and not updated.lower().startswith('<!doctype'):
        updated = '<!DOCTYPE html>\n' + updated
    return updated, inserted > 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--guide')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    if not GUIDES_DIR.exists():
        print(f"ERROR: {GUIDES_DIR} not found"); sys.exit(1)

    # Find guides with no data-lang at all
    targets_all = []
    for f in sorted(GUIDES_DIR.glob("*.html")):
        if f.name == 'index.html':
            continue
        c = f.read_text(encoding='utf-8')
        if 'data-lang="en"' not in c and 'data-lang="tl"' not in c:
            targets_all.append(f.name)

    print(f"\nGuides needing retrofit: {len(targets_all)}")
    for f in targets_all:
        print(f"  {f}")

    if args.guide:
        targets = [args.guide]
    elif args.all:
        targets = targets_all
    else:
        print("\nUsage: --guide filename.html | --all")
        return

    client = anthropic.Anthropic(api_key=args.api_key)
    changed = errors = 0

    for i, fname in enumerate(targets, 1):
        path = GUIDES_DIR / fname
        if not path.exists():
            print(f"[{i}/{len(targets)}] NOT FOUND: {fname}"); errors += 1; continue
        title = fname.replace('.html','').replace('-',' ').title()
        print(f"\n[{i}/{len(targets)}] {fname}")
        try:
            html = path.read_text(encoding='utf-8')
            updated, was_changed = retrofit_guide(html, client, title)
            if was_changed and not args.dry_run:
                path.with_suffix('.bak').write_text(html, encoding='utf-8')
                path.write_text(updated, encoding='utf-8')
                print(f"  SAVED ✓")
                changed += 1
            elif was_changed:
                print(f"  DRY RUN — would save")
                changed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()
            errors += 1
        if i < len(targets):
            time.sleep(1)

    print(f"\n=== DONE: {changed} changed · {errors} errors ===")
    if changed > 0 and not args.dry_run:
        print(f"\nPush: cd ~/Desktop/williamriveromd && git add guides/ && git commit -m 'Retrofit {changed} guides with translations' && git push")

if __name__ == "__main__":
    main()
