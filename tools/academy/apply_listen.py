"""Academy "Listen to this module" player (Dr. Rivero, Nov 26 2026). Idempotent.

Reads modules aloud with the device's own voice (Web Speech API), for learners with low vision and learners who are
driving. Free: no server, no audio files, works offline in Schola.

  assets/vendor/easy-speech.iife.js   easy-speech 2.4.0 (MIT, Jan Küster), cross-browser speechSynthesis wrapper,
                                      vendored unmodified (license: assets/vendor/easy-speech.LICENSE.txt)
  assets/academy-listen.js            the player (edit this)

This patcher:
  1. concatenates the two into a fingerprinted assets/academy-listen.<hash>.js (older copies pruned; _headers caches
     /assets/academy-listen.* immutable), so pages never link the unhashed source;
  2. puts <script src="../assets/academy-listen.<hash>.js" defer></script> before </body> on module pages (file names
     with -NN-), or only on the pages in PILOT when it is a set.

Run after every publish (publish_academy.py does, before build_schola.py, so the script joins the offline list).

    python3 tools/academy/apply_listen.py             # apply
    python3 tools/academy/apply_listen.py --dry-run   # report only
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-listen"
SOURCES = [ASSETS / "vendor" / "easy-speech.iife.js", ASSETS / "academy-listen.js"]

# Pilot first (Dr. Rivero previews before rollout). Set to None to cover every module page.
PILOT = {"dialysis-charge-nurse-01-taking-charge.html"}

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')
MODULE_RE = re.compile(r"-\d\d-")


def bundle(dry):
    data = b"\n;\n".join(p.read_bytes() for p in SOURCES)
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def wanted(name):
    return name in PILOT if PILOT is not None else bool(MODULE_RE.search(name))


def main():
    dry = "--dry-run" in sys.argv
    hashed = bundle(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if wanted(f.name):
            i = text.rfind("</body>")
            text = text[:i] + tag + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy listen ({hashed}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
