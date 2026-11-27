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
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-certificate"

# Pilot first (Dr. Rivero previews before rollout). Set to None to cover every end-of-course examination.
PILOT = None   # rolled out to every end-of-course examination (Dr. Rivero, Nov 27 2026)

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js"[^>]*></script>')
PROG = "academy-progress"   # module-quiz recorder on every module page of a track that has a final exam
PROG_RE = re.compile(r'\n?<script src="[^"]*assets/' + PROG + r'\.[0-9a-f]{10}\.js" defer></script>')
LIST_RE = re.compile(r'\n?<script type="application/json" id="rcm-cert-modules">.*?</script>', re.S)


def module_pages(exam_name):
    return sorted(ACADEMY.glob(exam_name[: -len("-final-exam.html")] + "-[0-9][0-9]-*.html"))


def module_list(exam_name):
    """[[NN, title, file]] for the exam page's certificate checklist."""
    out = []
    for f in module_pages(exam_name):
        t = f.read_text(encoding="utf-8")
        m = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S) or re.search(r"<title>(.*?)</title>", t, re.S)
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else f.stem
        title = re.sub(r":\s*[^:]*Module \d+$", "", re.sub(r"\s+", " ", title))
        out.append([re.search(r"-(\d\d)-", f.name).group(1), title, f.name])
    return out
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


def fingerprint(name, dry):
    data = (ASSETS / (name + ".js")).read_bytes()
    out = f"{name}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(name + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(name) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


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
    prog = fingerprint(PROG, dry)
    exams = [f.name for f in ACADEMY.glob("*-final-exam.html") if wanted(f.name)]
    module_files = {p.name for e in exams for p in module_pages(e)}
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = PROG_RE.sub("", LIST_RE.sub("", TAG_RE.sub("", old)))
        if f.name in module_files:
            i = text.rfind("</body>")
            text = text[:i] + f'<script src="../assets/{prog}" defer></script>' + "\n" + text[i:]
        if wanted(f.name):
            mins = study_minutes(f.name)
            mods = len(module_pages(f.name))
            tag = (f'<script src="../assets/{hashed}"' + (f' data-modules="{mods}"' if mods else "")
                   + (f' data-study-min="{mins}"' if mins else "") + " defer></script>")
            lst = json.dumps(module_list(f.name), ensure_ascii=False).replace("</", "<\\/")
            tag = f'<script type="application/json" id="rcm-cert-modules">{lst}</script>\n' + tag
            i = text.rfind("</body>")
            text = text[:i] + tag + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy certificate ({hashed}, {prog}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
