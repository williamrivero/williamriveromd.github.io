"""Academy page scripts: Highlights & Notes (+ Bookmarks, Resume) and Schola, the Academy app (Dr. Rivero,
Nov 25 2026). Idempotent.

  assets/academy-notes.js   highlights, notes, bookmarks, resume where you left off (localStorage only)
  assets/schola.js          the Schola app: worker registration, install / download panel, track cards, app bar

This patcher:
  1. writes fingerprinted copies assets/<name>.<hash>.js (and prunes older copies); _headers caches them
     immutable, so pages must never link the unhashed files;
  2. puts <script src="../assets/<name>.<hash>.js" defer> before </body> on every academy page (or only the pages
     in PILOT when it is a set), notes first, then Schola;
  3. puts the Schola head block (app manifest, Home Screen icon and title) in every academy page's <head>, replacing
     the site-wide /site.webmanifest and apple-touch-icon links, so "Add to Home Screen" installs Schola.

Runs after every publish (publish_academy.py), so generator rebuilds keep it. Then run
tools/academy/build_schola.py (publish_academy.py does) so the offline file list matches the pages.

    python3 tools/academy/apply_notes.py             # apply
    python3 tools/academy/apply_notes.py --dry-run   # report only
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
SCRIPTS = ["academy-notes", "schola"]          # load order

# Rollout: every academy page (piloted on POD Module 1 first). Set PILOT to a set of file names to limit it.
PILOT = None

HEAD = """<!-- SCHOLA-HEAD -->
<link rel="manifest" href="/academy/schola.webmanifest">
<link rel="apple-touch-icon" sizes="180x180" href="/images/app/schola-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Schola">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<!-- /SCHOLA-HEAD -->"""
HEAD_RE = re.compile(r"\n?<!-- SCHOLA-HEAD -->.*?<!-- /SCHOLA-HEAD -->", re.S)
OLD_HEAD_RE = re.compile(r'\n?<link rel="(?:manifest" href="/site\.webmanifest|apple-touch-icon"[^>]*href="/apple-touch-icon\.png)"[^>]*>')


def tag_re(name):
    return re.compile(r'\n?<script src="[^"]*assets/' + re.escape(name) + r'(?:\.[0-9a-f]{10})?\.js" defer></script>')


def fingerprint(name, dry):
    data = (ASSETS / (name + ".js")).read_bytes()
    out = f"{name}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(name + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(name) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def main():
    dry = "--dry-run" in sys.argv
    hashed = [fingerprint(n, dry) for n in SCRIPTS]
    tags = "\n".join(f'<script src="../assets/{h}" defer></script>' for h in hashed)
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old or "</head>" not in old:
            continue
        text = old
        for n in SCRIPTS:
            text = tag_re(n).sub("", text)
        text = HEAD_RE.sub("", text)
        if PILOT is None or f.name in PILOT:
            text = OLD_HEAD_RE.sub("", text)
            text = text.replace("</head>", HEAD + "\n</head>", 1)
            i = text.rfind("</body>")
            text = text[:i] + tags + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy scripts ({', '.join(hashed)}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
