"""Highlights & Notes for Renal Care Academy pages (Dr. Rivero, Nov 25 2026). Idempotent.

Learners select text in a module to highlight it or add a note; notes live in the browser's
localStorage only (no account, no server). The script is assets/academy-notes.js.

This patcher:
  1. writes the fingerprinted copy assets/academy-notes.<hash>.js (and prunes older copies);
     _headers caches /assets/academy-notes.* immutable, so pages must never link the unhashed file;
  2. adds <script src="../assets/academy-notes.<hash>.js" defer> before </body> on the pages in PILOT
     (or on every academy page when PILOT is None), and removes it from pages outside the rollout.

Runs after every publish (publish_academy.py), so generator rebuilds keep it.

    python3 tools/academy/apply_notes.py             # apply the current rollout
    python3 tools/academy/apply_notes.py --dry-run   # report only
    python3 tools/academy/apply_notes.py --all       # one-off: every academy page, ignoring PILOT
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
SRC = ASSETS / "academy-notes.js"

# Rollout: piloted on POD Module 1, then enabled on every academy page (Dr. Rivero, Nov 25 2026):
# modules, hubs, final exams, trainers and the landing page. To limit it again, set PILOT to a set of file names.
PILOT = None

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/academy-notes(?:\.[0-9a-f]{10})?\.js" defer></script>')


def fingerprint(dry):
    data = SRC.read_bytes()
    h = hashlib.sha256(data).hexdigest()[:10]
    name = f"academy-notes.{h}.js"
    if not dry:
        (ASSETS / name).write_bytes(data)
        for old in ASSETS.glob("academy-notes.*.js"):
            if old.name != name:
                old.unlink()
    return name


def main():
    dry = "--dry-run" in sys.argv
    every = "--all" in sys.argv or PILOT is None
    name = fingerprint(dry)
    tag = f'\n<script src="../assets/{name}" defer></script>'
    added = removed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        want = every or f.name in PILOT
        if want:
            i = text.rfind("</body>")
            text = text[:i] + tag.lstrip("\n") + "\n" + text[i:]
        if text != old:
            if want:
                added += 1
            else:
                removed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    scope = "all academy pages" if every else f"{len(PILOT)} pilot page(s)"
    print(f"academy notes ({name}, {scope}): {added} page(s) updated, {removed} removed" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
