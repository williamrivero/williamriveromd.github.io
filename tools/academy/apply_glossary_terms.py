"""Tap-to-define glossary terms in Academy modules (Dr. Rivero, Nov 28 2026). Idempotent.

assets/academy-glossary.js (edit this) reads each module's own "Glossary & abbreviations" section in the browser,
underlines (dotted) the first use of each term in every section of the module text, and on a tap shows the definition
with "See in glossary", which opens the side rail Glossary drawer on wide screens (term highlighted) or the accordion
at the end of the page. The HTML files are not changed, so Pagefind, Listen and Notes see the same text as before
(the marks are <span role="button">, not <button>, so Listen still reads the words). Skipped: headings, links, buttons,
the self-assessment (#quiz), the interactive case (#sim), further reading (#reading), forms and citation markers.

This patcher fingerprints the script to assets/academy-glossary.<hash>.js (older copies pruned; _headers caches
/assets/academy-glossary.* immutable) and tags every module page (-NN- in the file name) that has a glossary.
Run after every publish, before build_schola.py (publish_academy.py does).

    python3 tools/academy/apply_glossary_terms.py             # apply
    python3 tools/academy/apply_glossary_terms.py --dry-run   # report only
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-glossary"
TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')
MODULE_RE = re.compile(r"-\d\d-")


def bundle(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    dry = "--dry-run" in argv
    hashed = bundle(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if MODULE_RE.search(f.name) and 'class="glossary-acc"' in text:
            i = text.rfind("</body>")
            text = text[:i] + tag + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy glossary terms ({hashed}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
