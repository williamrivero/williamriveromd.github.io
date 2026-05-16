#!/usr/bin/env python3
"""
fix_spelling_us.py — Replace British English spellings with US English
across all guides/*.html files (except practical-outpatient-algorithms.html
and index.html which are excluded).

Case-preserving: lowercase→lowercase, Title→Title, UPPER→UPPER.
Writes back only if content changed.
"""

import re
import glob
import os

# List of (british, us) pairs — order matters for overlapping patterns
REPLACEMENTS = [
    # Medical terms
    ("oedema", "edema"),
    ("anaemia", "anemia"),
    ("haemoglobin", "hemoglobin"),
    ("haematuria", "hematuria"),
    ("haemolysis", "hemolysis"),
    ("haemolytic", "hemolytic"),
    ("haemorrhagic", "hemorrhagic"),
    ("haemorrhage", "hemorrhage"),
    ("hypovolaemia", "hypovolemia"),
    ("uraemic", "uremic"),
    ("uraemia", "uremia"),
    ("hypokalaemia", "hypokalemia"),
    ("hyperkalaemia", "hyperkalemia"),
    ("hypocalcaemia", "hypocalcemia"),
    ("hypercalcaemia", "hypercalcemia"),
    ("hypophosphataemia", "hypophosphatemia"),
    ("hyperphosphataemia", "hyperphosphatemia"),
    ("foetal", "fetal"),
    ("foetus", "fetus"),
    ("paediatric", "pediatric"),
    ("gynaecolog", "gynecolog"),
    ("orthopaedic", "orthopedic"),
    ("litre", "liter"),
    ("haemopoietic", "hematopoietic"),
    # Common words
    ("colour", "color"),
    ("behaviour", "behavior"),
    ("favour", "favor"),
    ("honour", "honor"),
    ("labour", "labor"),
    ("neighbour", "neighbor"),
    ("centre", "center"),
    ("fibre", "fiber"),
    ("defence", "defense"),
    ("licence", "license"),
    ("programme", "program"),
    ("grey", "gray"),
    ("practise", "practice"),
    # -ise → -ize verbs
    ("organise", "organize"),
    ("recognise", "recognize"),
    ("prioritise", "prioritize"),
    ("hospitalise", "hospitalize"),
    ("dialyse", "dialyze"),
    ("catheterise", "catheterize"),
    ("stabilise", "stabilize"),
    ("normalise", "normalize"),
    ("minimise", "minimize"),
    ("maximise", "maximize"),
    ("realise", "realize"),
    ("characterise", "characterize"),
    ("analyse", "analyze"),
    ("specialise", "specialize"),
    ("utilise", "utilize"),
    ("emphasise", "emphasize"),
    ("mobilise", "mobilize"),
    ("immunise", "immunize"),
    ("authorise", "authorize"),
    ("summarise", "summarize"),
    ("optimise", "optimize"),
    ("customise", "customize"),
    ("finalise", "finalize"),
]

SKIP_FILES = {"practical-outpatient-algorithms.html", "index.html"}


def make_case_preserving_repl(us_word):
    """Return a repl function that mirrors the case of the matched text."""
    def repl(m):
        matched = m.group(0)
        if matched.isupper():
            return us_word.upper()
        elif matched.istitle() or (matched[0].isupper() and matched[1:].islower()):
            return us_word.capitalize()
        else:
            return us_word
    return repl


def build_patterns():
    """Build list of (compiled_pattern, repl_fn) tuples."""
    patterns = []
    for british, us in REPLACEMENTS:
        # re.IGNORECASE so we catch Oedema, OEDEMA, oedema
        pat = re.compile(re.escape(british), re.IGNORECASE)
        patterns.append((pat, make_case_preserving_repl(us)))
    return patterns


def process_file(path, patterns):
    """Apply all replacements to a single file. Returns (changed, count)."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    text = original
    total_hits = 0
    for pat, repl_fn in patterns:
        new_text, n = pat.subn(repl_fn, text)
        total_hits += n
        text = new_text

    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True, total_hits
    return False, total_hits


def main():
    guides_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides")
    html_files = sorted(glob.glob(os.path.join(guides_dir, "*.html")))

    patterns = build_patterns()

    changed_files = []
    total_replacements = 0

    for path in html_files:
        basename = os.path.basename(path)
        if basename in SKIP_FILES:
            print(f"  SKIP  {basename}")
            continue

        changed, count = process_file(path, patterns)
        if changed:
            changed_files.append((basename, count))
            total_replacements += count
            print(f"  CHANGED  {basename}  ({count} replacements)")
        else:
            print(f"  unchanged  {basename}")

    print()
    print("=" * 60)
    print(f"Files changed : {len(changed_files)} / {len(html_files) - len(SKIP_FILES)}")
    print(f"Total replacements: {total_replacements}")
    if changed_files:
        print()
        print("Changed files:")
        for name, count in changed_files:
            print(f"  {name}  ({count})")


if __name__ == "__main__":
    main()
