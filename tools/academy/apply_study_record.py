"""Academy Personal Study Record (Dr. William Gregory Rivero, Nov 27 2026). Idempotent.

A printable one-page summary for the learner to hand to the head nurse: modules finished (best module quiz and the date
passed), active time per module page, the end-of-course examination result, and the date the preceptor signed off each
module's skills (or competency) checklist. Not called a certificate, in keeping with the Academy disclaimer.

  assets/academy-study-record.js   the script (edit this)

This patcher fingerprints it into assets/academy-study-record.<hash>.js (older copies pruned; _headers caches
/assets/academy-study-record.* immutable) and:
  * on every track hub (academy/<track>.html that has <track>-NN-*.html modules): puts a "Personal study record" section
    (#study-record, between STUDY-RECORD markers) right after #assessment (else before #sources, else before </main>),
    a "Study record" nav pill after the Assessment pill, the module list as JSON (#rcm-study-modules) and the script tag;
  * on every module page with a #skills or #competencies section: the script tag (it adds the sign-off date box).
Run after every publish (publish_academy.py does, after apply_certificate.py and before build_schola.py).

    python3 tools/academy/apply_study_record.py             # apply
    python3 tools/academy/apply_study_record.py --dry-run   # report only
"""
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-study-record"

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')
LIST_RE = re.compile(r'\n?<script type="application/json" id="rcm-study-modules">.*?</script>', re.S)
SEC_RE = re.compile(r'\n?<!-- STUDY-RECORD-START -->.*?<!-- STUDY-RECORD-END -->', re.S)
PILL_RE = re.compile(r'\n?<a class="nav-pill" href="#study-record">Study record</a>')
MOD_RE = re.compile(r"-(\d\d)-")


def is_copy(name):
    return bool(re.search(r" \d+(\.[^.]+)?$", name))


def modules_of(hub):
    return sorted(f for f in ACADEMY.glob(hub.stem + "-[0-9][0-9]-*.html") if not is_copy(f.name))


def has_checklist(text):
    return 'id="skills"' in text or 'id="competencies"' in text


def store_key(text):
    m = re.search(r'<html[^>]*data-nc-store="([^"]+)"', text)
    if m:
        return m.group(1)
    m = re.search(r'<body[^>]*data-course="([^"]+)"', text)
    if m:
        return f"rcm-course-{m.group(1)}-progress"
    if "nursing-course.js" in text:
        return "rcm-nursing-progress"
    return ""


def title_of(text, stem):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S) or re.search(r"<title>(.*?)</title>", text, re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else stem
    return re.sub(r":\s*[^:]*Module \d+$", "", re.sub(r"\s+", " ", t))


def track_name(hub_text, stem):
    m = re.search(r'<span class="nc-cur">(.*?)</span>', hub_text, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def payload(hub, hub_text):
    mods, store = [], ""
    for f in modules_of(hub):
        t = f.read_text(encoding="utf-8")
        store = store or store_key(t)
        pm = re.search(r'id="nc-quiz"[^>]*data-pass="(\d+)"', t) or re.search(r'data-pass="(\d+)"[^>]*id="nc-quiz"', t)
        mods.append([MOD_RE.search(f.name).group(1), title_of(t, f.stem), f.name, 1 if has_checklist(t) else 0,
                     int(pm.group(1)) if pm else 0])
    return {"track": hub.stem, "name": track_name(hub_text, hub.stem), "store": store,
            "exam": (ACADEMY / (hub.stem + "-final-exam.html")).exists(), "modules": mods}


def section(n_checklists):
    sign = ("Each module with a skills or competency checklist has a <strong>Preceptor sign-off</strong> box at the end of "
            "that section; enter the date your preceptor signed it, or enter it in the table below. " if n_checklists else "")
    return f"""
<!-- STUDY-RECORD-START -->
<section class="section" id="study-record">
  <div class="section-tag">Your record</div>
  <h2>Personal study record</h2>
  <p>Need to show your head nurse or preceptor how far you have gone? Make a one-page study record: the modules you
    finished, your best quiz score and the date you passed each, the time you spent on each module page, your
    end-of-course examination result, and the date each checklist was signed off. {sign}Print it or save it as a PDF.</p>
  <p>It is a record of your own self-study, <strong>not a certificate</strong> and not CPD units, and it stays on this
    device. Your signed checklists and the unit&rsquo;s competency form remain the official record.</p>
  <div id="rcm-sr-app"><noscript>The study record needs JavaScript.</noscript></div>
</section>
<!-- STUDY-RECORD-END -->
"""


def add_section(text, sec):
    i = text.find('id="assessment"')
    if i > 0:
        j = text.find("</section>", i)
        if j > 0:
            j += len("</section>")
            return text[:j] + "\n" + sec.strip("\n") + text[j:]
    for marker in ('<section class="section" id="sources"', "</main>"):
        k = text.find(marker)
        if k > 0:
            return text[:k] + sec.strip("\n") + "\n" + text[k:]
    return text


def add_pill(text):
    pill = '<a class="nav-pill" href="#assessment">Assessment</a>'
    return text.replace(pill, pill + '\n<a class="nav-pill" href="#study-record">Study record</a>', 1)


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def is_hub(f):
    n = f.name
    if n.startswith("patients-care-partners"):   # patient track: no staff study record or placement pre-test
        return False
    return not (MOD_RE.search(n) or n.endswith(("-final-exam.html", "-trainer.html")) or is_copy(n)) and bool(modules_of(f))


def main():
    dry = "--dry-run" in sys.argv
    hashed = fingerprint(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed = hubs = mods = 0
    for f in sorted(ACADEMY.glob("*.html")):
        if is_copy(f.name):
            continue
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = PILL_RE.sub("", SEC_RE.sub("", LIST_RE.sub("", TAG_RE.sub("", old))))
        add = ""
        if is_hub(f):
            data = payload(f, text)
            text = add_pill(add_section(text, section(sum(m[3] for m in data["modules"]))))
            lst = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
            add = f'<script type="application/json" id="rcm-study-modules">{lst}</script>\n' + tag
            hubs += 1
        elif MOD_RE.search(f.name) and has_checklist(text):
            add = tag
            mods += 1
        if add:
            i = text.rfind("</body>")
            text = text[:i] + add + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy study record ({hashed}): {hubs} hub(s), {mods} module page(s); {changed} page(s) updated"
          + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
