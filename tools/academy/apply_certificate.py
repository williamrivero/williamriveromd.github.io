"""Academy certificate of completion (Dr. Rivero, Nov 27 2026; Bernard Cruz's suggestion). Idempotent.

On a track's end-of-course examination page, a learner who passes (80%, or the page's own "Passed" verdict) can type
the name to print and get a certificate of completion drawn in the browser: save as an image or print / save as PDF.
No login, nothing sent or stored. Self-study certificate, not CPD-accredited (stated on the certificate).

  assets/academy-certificate.js   the script (edit this)

This patcher fingerprints it into assets/academy-certificate.<hash>.js (older copies pruned; _headers caches
/assets/academy-certificate.* immutable) and puts <script src="../assets/academy-certificate.<hash>.js" defer></script>
(with data-study-min = estimated study time: module words at 200 wpm + 40 min exam, nearest half hour)
before </body> on the end-of-course examination pages (*-final-exam.html), or only on the pages in PILOT when it is a set.

Run after every publish (publish_academy.py does, before build_schola.py).

    python3 tools/academy/apply_certificate.py             # apply
    python3 tools/academy/apply_certificate.py --dry-run   # report only
"""
import hashlib, html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-certificate"

# Pilot first (Dr. Rivero previews before rollout). Set to None to cover every end-of-course examination.
PILOT = None   # rolled out to every end-of-course examination (Dr. Rivero, Nov 27 2026)

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js"[^>]*></script>')
WPM = 200          # reading pace, the same as the guides' reading-time badge
EXAM_MIN = 40      # "about one minute per question", as the exam page says


def study_minutes(exam_name):
    """Estimated study time for the track: English words in every module's <main> at WPM, plus the examination."""
    prefix = exam_name[: -len("-final-exam.html")]
    words = 0
    for f in ACADEMY.glob(prefix + "-[0-9][0-9]-*.html"):
        m = re.search(r"<main[^>]*>(.*?)</main>", f.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", m.group(1), flags=re.S)
        t = re.sub(r'<(\w+)[^>]*data-lang="(?:tl|ceb|kap)"[^>]*>.*?</\1>', "", t, flags=re.S)
        words += len(html.unescape(re.sub(r"<[^>]+>", " ", t)).split())
    if not words:
        return 0
    return int(round((words / WPM + EXAM_MIN) / 30.0)) * 30   # nearest half hour


SOURCES = [ASSETS / "vendor" / "qrcode-generator.js", ASSETS / (NAME + ".js")]   # qrcode-generator 1.4.4 (MIT, Kazuhiko Arase)


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
    return name in PILOT if PILOT is not None else name.endswith("-final-exam.html")


def main():
    dry = "--dry-run" in sys.argv
    hashed = bundle(dry)
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if wanted(f.name):
            mins = study_minutes(f.name)
            mods = len(list(ACADEMY.glob(f.name[: -len("-final-exam.html")] + "-[0-9][0-9]-*.html")))
            tag = (f'<script src="../assets/{hashed}"' + (f' data-modules="{mods}"' if mods else "")
                   + (f' data-study-min="{mins}"' if mins else "") + " defer></script>")
            i = text.rfind("</body>")
            text = text[:i] + tag + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy certificate ({hashed}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
