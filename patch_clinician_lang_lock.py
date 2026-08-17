#!/usr/bin/env python3
"""Install assets/clinician-lang-lock.js on every guide that has language pills.

Clinician (physician) mode is English-only. The master CSS darkens/disables the
non-EN language pills when body.physician-mode is active; this script wires the
matching behaviour by loading clinician-lang-lock.js, which forces the guide to
display English while in clinician mode and restores the visitor's chosen
language when they return to the patient tab.

The tag is inserted before the LAST </body> (so any JS print-popup strings that
contain '</body>' are never touched). Idempotent: a guide already loading the
script is skipped.

Usage:
  python3 patch_clinician_lang_lock.py                 # all eligible guides
  python3 patch_clinician_lang_lock.py --dry-run
  python3 patch_clinician_lang_lock.py --guide igan-guide.html
"""
import argparse, glob, os

TAG = '<script src="../assets/clinician-lang-lock.js" defer></script>'
MARK = 'assets/clinician-lang-lock.js'

def patch(text):
    if MARK in text:
        return text, 'skip (already present)'
    # Only guides that actually have the header language pills need it.
    if 'header-lang' not in text and 'lang-btn-g' not in text:
        return text, 'skip (no language pills)'
    idx = text.rfind('</body>')
    if idx == -1:
        return text, 'skip (no </body>)'
    new = text[:idx] + TAG + '\n' + text[idx:]
    return new, 'patched'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--guide')
    args = ap.parse_args()

    if args.guide:
        files = [os.path.join('guides', os.path.basename(args.guide))]
    else:
        # Calculators are English-only and have no language pills — skip them.
        files = [f for f in sorted(glob.glob('guides/*.html')) if 'calc-' not in f]

    patched = 0
    for f in files:
        if not os.path.exists(f):
            print(f"skip (missing): {f}"); continue
        text = open(f, encoding='utf-8').read()
        new, status = patch(text)
        if status == 'patched':
            patched += 1
            if not args.dry_run:
                open(f, 'w', encoding='utf-8').write(new)
            print(f"{'would patch' if args.dry_run else 'patched'}: {f}")
    print(f"\n{'Would patch' if args.dry_run else 'Patched'} {patched} guide(s).")

if __name__ == '__main__':
    main()
