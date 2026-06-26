#!/usr/bin/env python3
"""
patch_symptom_widget.py — williamriveromd.com

Installs the floating Symptom-Checker widget on every content guide.

The widget is `assets/symptom-checker-widget.js` — a vanilla-JS floating 🩺
button that opens the symptom checker in a modal iframe (it self-disables on
symptom-checker.html). Guides load it with a single deferred <script> tag placed
just before the final </body>:

    <script src="../assets/symptom-checker-widget.js" defer></script>

This script:
  - inserts that tag before the **last** </body> (so print-popup JS strings like
    '</body></html>' are never touched), and
  - repairs the legacy broken path `../js/symptom-checker-widget.js` →
    `../assets/symptom-checker-widget.js`.

Idempotent: a guide that already loads the widget from `assets/` is skipped.

Skipped (not narrative guides): the guides index, the symptom checker itself,
calculators (`calc-*` + the calculators index + ckd-dri-calculator), the
pure interpreter/atlas tools, and printable log/blank sheets.

Usage:
    python3 patch_symptom_widget.py
    python3 patch_symptom_widget.py --dry-run
    python3 patch_symptom_widget.py --report          # list coverage, no writes
    python3 patch_symptom_widget.py --guide hmo-ckd-coverage.html
"""

import argparse
from pathlib import Path

TAG = '<script src="../assets/symptom-checker-widget.js" defer></script>'
GOOD = 'assets/symptom-checker-widget.js'
BROKEN = '../js/symptom-checker-widget.js'

SKIP_EXACT = {
    "index.html", "symptom-checker.html", "calculators.html",
    "ckd-dri-calculator.html", "dyslipidemia-management-tool.html",
    "nephrology-atlas.html", "prostate-panel-interpreter.html",
}
SKIP_PREFIX = ("calc-",)
SKIP_SUFFIX = ("-log.html", "-log-blank.html", "-blank.html")


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def eligible(name: str) -> bool:
    if name in SKIP_EXACT:
        return False
    if name.startswith(SKIP_PREFIX):
        return False
    if name.endswith(SKIP_SUFFIX):
        return False
    return True


def patch_guide(path: Path, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    original = text

    # Repair the legacy broken path first.
    if BROKEN in text:
        text = text.replace(BROKEN, "../assets/symptom-checker-widget.js")
        if not dry_run:
            path.write_text(text, encoding="utf-8")
        return "✓ fixed broken path"

    if GOOD in text:
        return "unchanged (already installed)"

    idx = text.rfind("</body>")
    if idx == -1:
        return "skip (no </body>)"
    text = text[:idx] + TAG + "\n" + text[idx:]

    if text == original:
        return "unchanged"
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return "✓ installed"


def main():
    ap = argparse.ArgumentParser(description="Install the floating symptom-checker widget.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", action="store_true", help="list coverage only")
    ap.add_argument("--guide", help="patch a single guide (filename in guides/)")
    args = ap.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"
    targets = ([guides_dir / args.guide] if args.guide
               else sorted(guides_dir.glob("*.html")))

    changed, missing = 0, []
    for path in targets:
        if not path.exists():
            print(f"  ! {path.name}: not found"); continue
        if not args.guide and not eligible(path.name):
            continue
        if args.report:
            text = path.read_text(encoding="utf-8")
            has = GOOD in text and BROKEN not in text
            print(f"  {'has ' if has else '——  '}  {path.name}")
            if not has:
                missing.append(path.name)
            continue
        status = patch_guide(path, args.dry_run)
        if status.startswith("✓"):
            changed += 1
            print(f"  {status}  {path.name}")

    if not args.report:
        verb = "Would update" if args.dry_run else "Updated"
        print(f"\n{verb} {changed} guide(s).")
    elif missing:
        print(f"\n{len(missing)} eligible guide(s) without the widget.")


if __name__ == "__main__":
    main()
