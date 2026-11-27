#!/usr/bin/env python3
"""Academy preceptor sign-off on the learner's device (Dr. Rivero, Nov 27 2026). Idempotent.

  assets/academy-skills.js   the sign-off layer (edit this): the preceptor starts a sign-off with initials and
                             a date, taps a rating for each step of a skills checklist (each tap stamped with
                             those initials and that date), and signs it off once every critical step passes.
                             Stored in localStorage only (rcm-skills:<track>/<NN>|<scale>); print and share.

Checklists it recognizes: module ul.nc-check lists (Satisfactory / Needs practice / Not observed when the
section mentions "satisfactory", else Signed off / Needs practice) and tables marked table.nc-sign or tr.nc-sign,
or with "(date, initials)" header columns, whose header is
Satisfactory / Needs practice / Not observed, Done / Not done, a numeric score (0 / 1 / 2), or has
"(date, initials)" columns. Other nc-sign tables are left alone.

This patcher:
  1. fingerprints it as assets/academy-skills.<hash>.js (older copies pruned; _headers caches
     /assets/academy-skills.* immutable);
  2. tags it on every academy page that has such a checklist (or only the pages in PILOT).

Run after every publish (publish_academy.py does, before build_schola.py).

    python3 tools/academy/apply_skills.py             # apply
    python3 tools/academy/apply_skills.py --dry-run   # report only
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-skills"
PILOT = None   # e.g. {"hemodialysis-technician-01-dialysis-unit-technician-role.html", "hemodialysis-technician-trainer.html"}

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')
WANT_RE = re.compile(r'<ul class="nc-check"|class="nc-sign"|\(date, initials\)')


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def wanted(name, text):
    if PILOT is not None and name not in PILOT:
        return False
    return bool(WANT_RE.search(text))


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    dry = "--dry-run" in argv
    hashed = fingerprint(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed = tagged = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if wanted(f.name, text):
            k = text.rfind("</body>")
            text = text[:k] + tag + "\n" + text[k:]
            tagged += 1
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy preceptor sign-off ({hashed}): {tagged} page(s) tagged, {changed} updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
