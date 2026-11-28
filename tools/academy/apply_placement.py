#!/usr/bin/env python3
"""Academy placement pre-test (Dr. William Gregory Rivero, Nov 27 2026: "a transferee with 5 years of HD experience
takes a pre-test and is shown only the modules they need"; mastery 80%; always-required modules proposed by Claude,
listed in data/academy-placement.json). Idempotent.

  assets/academy-placement.js      the script (edit this)
  data/academy-placement.json      mastery, questions per module, retake wait, always-required modules per track

For every track hub (academy/<track>.html with <track>-NN-*.html modules) this patcher:
  1. writes academy/<track>-pretest.html (noindex; built on the hub's head, header and footer, like the review deck
     on the landing page) holding the pre-test app and, as JSON (#rcm-pt-data), every testable module's self-assessment
     bank harvested from the module pages (stem, options, correct flag, rationale), so it works offline in Schola;
  2. puts a "Placement pre-test" section (#pretest, between PRETEST markers) right after #start on the hub, a "Pre-test"
     nav pill after "Start here", the module list as JSON (#rcm-pt-hub) and the script tag (it shows the learner's
     result and badges the module cards: Optional / Study / Required);
  3. tags every module page with the script (data-track, data-mod): a placed-out module shows a banner that reading it
     is optional and links to its quiz (the certificate still needs every module quiz: the module gate is unchanged).
It fingerprints the script as assets/academy-placement.<hash>.js (older copies pruned; _headers caches
/assets/academy-placement.* immutable). Results stay in localStorage `rcm-placement` on the device; nothing is sent.
Run after every publish (publish_academy.py does, after apply_study_record.py and before apply_review.py, which skips
the pre-test pages so the start-of-shift drill never interrupts them).

    python3 tools/academy/apply_placement.py             # apply
    python3 tools/academy/apply_placement.py --dry-run   # report only
"""
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
CONFIG = ROOT / "data" / "academy-placement.json"
NAME = "academy-placement"
SUFFIX = "-pretest.html"
SITE = "https://renalcarematters.com/academy/"

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js"[^>]*></script>')
HUBJSON_RE = re.compile(r'\n?<script type="application/json" id="rcm-pt-hub">.*?</script>', re.S)
SEC_RE = re.compile(r'\n?<!-- PRETEST-START -->.*?<!-- PRETEST-END -->', re.S)
PILL_RE = re.compile(r'\n?<a class="nav-pill" href="#pretest">Pre-test</a>')
MOD_RE = re.compile(r"-(\d\d)-")


def is_copy(name):
    return bool(re.search(r" \d+(\.[^.]+)?$", name))


def modules_of(hub):
    return sorted(f for f in ACADEMY.glob(hub.stem + "-[0-9][0-9]-*.html") if not is_copy(f.name))


def is_hub(f):
    n = f.name
    if n.startswith("patients-care-partners"):   # patient track: no staff study record or placement pre-test
        return False
    return not (MOD_RE.search(n) or n.endswith(("-final-exam.html", "-trainer.html", SUFFIX)) or is_copy(n)) \
        and bool(modules_of(f))


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def title_of(text, stem):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S) or re.search(r"<title>(.*?)</title>", text, re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else stem
    return re.sub(r":\s*[^:]*Module \d+$", "", re.sub(r"\s+", " ", t))


def track_name(hub_text):
    m = re.search(r'<span class="nc-cur">(.*?)</span>', hub_text, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def bank(text, fname):
    """The module's self-assessment bank: [[stem_html, [[option_html, correct, rationale_html], ...]], ...]."""
    i = text.find('id="nc-quiz"')
    if i < 0:
        return []
    form = text[i:text.find("</form>", i)]
    out = []
    for fs in re.findall(r'<fieldset class="nc-q".*?</fieldset>', form, re.S):
        leg = re.search(r"<legend>(.*?)</legend>", fs, re.S)
        if not leg:
            continue
        stem = clean(re.sub(r'<span class="nc-qn">.*?</span>', "", leg.group(1), flags=re.S))
        opts = []
        for blk in re.split(r'<div class="nc-opt">', fs)[1:]:
            c = re.search(r'data-correct="(\d)"', blk)
            lab = re.search(r"<label[^>]*>(.*?)</label>", blk, re.S)
            if not (c and lab):
                continue
            rat = re.search(r'<div class="nc-rat"[^>]*>(.*?)</div>', blk, re.S)
            opts.append([clean(lab.group(1)), int(c.group(1)), clean(rat.group(1)) if rat else ""])
        if len(opts) >= 2 and sum(o[1] for o in opts) == 1:
            out.append([stem, opts])
        else:
            print(f"  skipped a malformed question in {fname}", file=sys.stderr)
    return out


def load_config():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    for k in ("mastery", "per_module", "retake_hours", "categories", "tracks"):
        if k not in cfg:
            sys.exit(f"{CONFIG}: missing '{k}'")
    for t, v in cfg["tracks"].items():
        for nn, cat in v.get("always", {}).items():
            if cat not in cfg["categories"]:
                sys.exit(f"{CONFIG}: {t} module {nn}: unknown category '{cat}'")
    return cfg


def track_data(hub, hub_text, cfg):
    always = cfg["tracks"].get(hub.stem, {}).get("always", {})
    mods = []
    for f in modules_of(hub):
        t = f.read_text(encoding="utf-8")
        nn = MOD_RE.search(f.name[len(hub.stem):]).group(1)
        m = {"n": nn, "t": title_of(t, f.stem), "f": f.name}
        if nn in always:
            m["a"] = always[nn]
        else:
            m["q"] = bank(t, f.name)
            if not m["q"]:          # no bank to test it: treat as required rather than silently skippable
                m["a"] = "capstone" if "capstone" in m["t"].lower() else "orient"
                del m["q"]
        mods.append(m)
    unknown = sorted(set(always) - {m["n"] for m in mods})
    if unknown:
        sys.exit(f"{CONFIG}: {hub.stem}: no module(s) {', '.join(unknown)}")
    return {"track": hub.stem, "name": track_name(hub_text), "hub": hub.name, "page": hub.stem + SUFFIX,
            "mastery": cfg["mastery"], "per": cfg["per_module"], "retake": cfg["retake_hours"],
            "cats": cfg["categories"], "mods": mods}


def jsonify(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


# ── the pre-test page ──────────────────────────────────────────────────────────────────────────────────────────
def sub_meta(head, title, desc, url):
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", head, count=1, flags=re.S)
    for prop, val in (("og:title", title), ("twitter:title", title), ("og:description", desc),
                      ("twitter:description", desc), ("og:url", url)):
        head = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % re.escape(prop),
                      lambda m: m.group(1) + html.escape(val) + m.group(2), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + html.escape(desc) + m.group(2),
                  head, count=1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head, count=1)
    og = ROOT / "images" / "og" / (url.rstrip("/").rsplit("/", 1)[-1] + "-og.jpg")   # a dedicated share card, when one exists
    if og.exists():
        img = "https://renalcarematters.com/images/og/" + og.name
        head = re.sub(r'(<meta (?:property|name)="(?:og:image|twitter:image)" content=")[^"]*(")', lambda m: m.group(1) + img + m.group(2), head)
        head = re.sub(r'(<meta property="og:image:(?:width|height)" content=")[^"]*(")', lambda m: m.group(1) + ("1200" if "width" in m.group(0) else "630") + m.group(2), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    head = re.sub(r'<meta name="robots"[^>]*>\s*', "", head)
    return head.replace("</head>", '<meta name="robots" content="noindex, follow">\n</head>', 1)


PAGE_CSS = """<style id="rcm-pt-page">
.rcm-pt-hero{padding:34px 0 22px;}
.rcm-pt-hero h1{margin:10px 0 6px;}
.rcm-pt-hero .hero-tagline{font-size:17px;color:var(--text-mid);margin:0;}
.rcm-pt-main{max-width:880px;margin:0 auto;padding:10px 32px 40px;}
.rcm-pt-main h2{font-family:Inter,system-ui,sans-serif;}
.rcm-pt-how{font-size:15.5px;line-height:1.65;color:var(--text-mid);}
.rcm-pt-how li{margin:4px 0;}
@media (max-width:640px){.rcm-pt-main{padding:8px 16px 32px;}}
</style>"""


def page_main(d):
    n_test = sum(1 for m in d["mods"] if "q" in m)
    n_req = len(d["mods"]) - n_test
    pct = round(d["mastery"] * 100)
    track = html.escape(d["name"] or d["track"])
    return f"""
<!-- ═══ HERO ════════════════════════════════════ -->
<section class="hero rcm-pt-hero">
  <div class="container">
    <div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span><a href="{d['hub']}">{track}</a><span class="nc-sep">›</span><span>Placement pre-test</span></div>
    <h1>Placement pre-test</h1>
    <p class="hero-tagline">Already experienced? Show what you know, and study only the modules you need</p>
  </div>
</section>
{PAGE_CSS}
<main class="container rcm-pt-main">
  <div id="rcm-pt-app" aria-live="polite"><p class="rcm-pt-how">Loading the pre-test…</p>
    <noscript><p>The pre-test needs JavaScript.</p></noscript></div>
  <section class="rcm-pt-how rcm-pt-noprint" id="how">
    <h2>How the pre-test works</h2>
    <ul>
      <li><b>Who it is for:</b> transferees and experienced hires starting this role in a new unit. New to the role? Skip
        the pre-test and take the modules in order.</li>
      <li><b>What it asks:</b> up to {d['per']} questions for each of the {n_test} testable modules, drawn at random from
        that module&rsquo;s own question bank. You can test every module in one sitting or choose some now and the rest
        later; each module&rsquo;s result is saved as soon as you finish it.</li>
      <li><b>Placing out:</b> score {pct}% or better on a module and it becomes <b>optional</b> reading for you. Below
        {pct}%, the module stays on your study path. Answers and rationales are shown only after each module is scored,
        and a module can be retaken {d['retake']} hours after the last try.</li>
      <li><b>Always required:</b> {n_req} module{'s' if n_req != 1 else ''} in this track cannot be placed out of:
        unit orientation, infection prevention, emergencies, water and machine safety, and the capstone with its
        checklist sign-off. Experience elsewhere does not tell anyone how <em>this</em> unit does these things.</li>
      <li><b>The certificate still needs every module quiz.</b> For a module you placed out of, open it and go straight to
        its self-assessment at the end; you do not have to read it first.</li>
      <li><b>Privacy:</b> your answers and results stay in this browser on this device. Nothing is sent anywhere. Your
        head nurse or preceptor decides how your onboarding goes; print your result to show them.</li>
    </ul>
  </section>
</main>
"""


def build_page(hub_text, d):
    track = d["name"] or d["track"]
    title = f"Placement pre-test · {track} · Renal Care Academy"
    desc = (f"Experienced in this role? Take the {track} placement pre-test: short checks from each module's question "
            f"bank show which modules you can treat as optional. Stored only on your device.")
    head, rest = hub_text.split("</head>", 1)
    head = sub_meta(head + "</head>", title, desc, SITE + d["track"] + "-pretest")
    body_open = rest[:rest.index("</header>") + len("</header>")]
    tail = rest[rest.index('<footer class="guide-footer">'):]
    tail = re.sub(r'<button class="print-btn".*?</button>\s*', "", tail, count=1, flags=re.S)
    tail = re.sub(r'\n?<script type="application/json"[^>]*>.*?</script>', "", tail, flags=re.S)
    tail = re.sub(r'\n?<script src="[^"]*assets/(academy-|tech-course|nursing-course|guide-rail|share-buttons|image-lightbox|'
                  r'symptom)[^"]*"[^>]*></script>', "", tail)
    tail = re.sub(r'\n?<script src="[^"]*(tech-course|nursing-course)[^"]*"[^>]*></script>', "", tail)
    return head + body_open + "\n" + page_main(d) + "\n" + tail


# ── the hub section ───────────────────────────────────────────────────────────────────────────────────────────
CAT_SHORT = {"orient": "unit orientation", "infection": "infection prevention", "emergency": "emergencies",
             "water": "water and machine safety", "medication": "medication safety", "safeguarding": "safeguarding",
             "privacy": "privacy and records", "capstone": "the capstone"}
HUB_CSS = ('<style id="rcm-pt-hub-css">#pretest .nc-btn{display:inline-block;text-decoration:none;line-height:1.35}'
           '#pretest #rcm-pt-hub-app p{margin:18px 0 12px}#pretest .rcm-pt-note{margin-top:12px}</style>')


def required_sentence(d):
    req = [m for m in d["mods"] if "q" not in m]
    if not req:
        return ""
    cats = []
    for k in CAT_SHORT:                      # fixed order, only the categories this track uses
        if any(m.get("a") == k for m in req):
            cats.append(CAT_SHORT[k])
    lst = cats[0] if len(cats) == 1 else ", ".join(cats[:-1]) + (", and " if len(cats) > 2 else " and ") + cats[-1]
    verb = "is" if len(req) == 1 else "are"
    return (f" {len(req)} of the {len(d['mods'])} modules ({lst}) {verb} required for everyone, "
            f"whatever their experience.")


def hub_section(d):
    pct = round(d["mastery"] * 100)
    return f"""
<!-- PRETEST-START -->
<section class="section" id="pretest">
  {HUB_CSS}
  <div class="section-tag">Experienced hires</div>
  <h2>Placement pre-test</h2>
  <p>Transferring from another unit, or already experienced in this role? Take the placement pre-test: a short check of
    up to {d['per']} questions for each module, drawn from that module&rsquo;s own question bank. Score {pct}% or better and
    the module becomes optional reading for you, so you study only what you need.{required_sentence(d)}</p>
  <div id="rcm-pt-hub-app"><p><a class="nc-btn" href="{d['page']}">Take the placement pre-test</a></p></div>
  <p class="rcm-pt-note">Results stay on this device. The certificate still needs every module quiz; for a module you
    placed out of, go straight to its self-assessment.</p>
</section>
<!-- PRETEST-END -->
"""


def add_section(text, sec):
    i = text.find('<section class="section" id="start"')
    if i > 0:
        j = text.find("</section>", i)
        if j > 0:
            j += len("</section>")
            return text[:j] + "\n" + sec.strip("\n") + text[j:]
    k = text.find("<main")
    k = text.find(">", k) + 1 if k > 0 else -1
    return text[:k] + "\n" + sec.strip("\n") + text[k:] if k > 0 else text


def add_pill(text):
    m = re.search(r'<a class="nav-pill" href="#start">[^<]*</a>', text)
    if not m:
        return text
    return text[:m.end()] + '\n<a class="nav-pill" href="#pretest">Pre-test</a>' + text[m.end():]


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def put_before_body(text, add):
    i = text.rfind("</body>")
    return text[:i] + add + "\n" + text[i:]


def write(path, text, dry):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == text:
        return 0
    if not dry:
        path.write_text(text, encoding="utf-8")
    return 1


def main():
    dry = "--dry-run" in sys.argv
    cfg = load_config()
    hashed = fingerprint(dry)
    src = f"../assets/{hashed}"
    changed = hubs = mods = 0
    for hub in sorted(f for f in ACADEMY.glob("*.html") if is_hub(f)):
        old = hub.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        base = PILL_RE.sub("", SEC_RE.sub("", HUBJSON_RE.sub("", TAG_RE.sub("", old))))
        d = track_data(hub, base, cfg)
        # pre-test page
        page = put_before_body(build_page(base, d),
                               f'<script type="application/json" id="rcm-pt-data">{jsonify(d)}</script>\n'
                               f'<script src="{src}" defer></script>')
        changed += write(ACADEMY / d["page"], page, dry)
        # hub
        lite = {k: d[k] for k in ("track", "name", "page", "mastery", "cats")}
        lite["mods"] = [[m["n"], m["t"], m["f"], m.get("a", "")] for m in d["mods"]]
        text = add_pill(add_section(base, hub_section(d)))
        text = put_before_body(text, f'<script type="application/json" id="rcm-pt-hub">{jsonify(lite)}</script>\n'
                                     f'<script src="{src}" defer></script>')
        changed += write(hub, text, dry)
        hubs += 1
        # module pages
        for m in d["mods"]:
            f = ACADEMY / m["f"]
            o = f.read_text(encoding="utf-8")
            t = TAG_RE.sub("", o)
            if "</body>" in t:
                t = put_before_body(t, f'<script src="{src}" data-track="{d["track"]}" data-mod="{m["n"]}" defer></script>')
                changed += write(f, t, dry)
                mods += 1
    # pre-test pages of tracks that no longer exist
    for p in ACADEMY.glob("*" + SUFFIX):
        if not (ACADEMY / (p.name[:-len(SUFFIX)] + ".html")).exists():
            print(f"  orphan pre-test page (hub gone): {p.name}; remove it by hand")
    print(f"academy placement pre-test ({hashed}): {hubs} track(s), {mods} module page(s); {changed} file(s) updated"
          + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
