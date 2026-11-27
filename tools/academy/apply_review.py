#!/usr/bin/env python3
"""Academy spaced-repetition review deck (Dr. Rivero, Nov 27 2026). Idempotent.

  assets/academy-review.js   the deck (edit this): captures missed self-assessment questions on this device,
                             schedules them in five Leitner boxes (1, 3, 7, 14, 30 days), runs review rounds,
                             and shows a "due today" card on the Academy landing page

This patcher:
  1. fingerprints it as assets/academy-review.<hash>.js (older copies pruned; _headers caches
     /assets/academy-review.* immutable);
  2. writes academy/review-deck.html (the deck page, built on the landing page's head, header and footer);
  3. tags the script on every academy page (Nov 27 2026: hubs and trainers too, so the start-of-shift drill
     can be served on whichever Academy page a learner opens first; the script itself skips final exams).

Run after every publish (publish_academy.py does, before build_schola.py, which also saves the deck page offline).

    python3 tools/academy/apply_review.py             # apply
    python3 tools/academy/apply_review.py --dry-run   # report only
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
NAME = "academy-review"
PAGE = "review-deck.html"
URL = "https://renalcarematters.com/academy/review-deck"
TITLE = "Review deck · Renal Care Academy"
DESC = ("Your spaced-repetition review deck: the self-assessment questions you missed come back after 1, 3, 7, 14 "
        "and 30 days until they stick. Stored only on your device.")

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def sub_meta(head):
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, count=1, flags=re.S)
    for prop, val in (("og:title", TITLE), ("twitter:title", TITLE), ("og:description", DESC), ("twitter:description", DESC), ("og:url", URL)):
        head = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + val + m.group(2), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + DESC + m.group(2), head, count=1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + URL + m.group(2), head, count=1)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)   # landing's structured data
    if 'name="robots"' not in head:
        head = head.replace("</head>", '<meta name="robots" content="noindex, follow">\n</head>', 1)
    return head


MAIN = """
<!-- ═══ HERO ════════════════════════════════════ -->
<section class="hero rcm-rv-hero">
  <div class="container">
    <div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span><span>Review deck</span></div>
    <h1>Your review deck</h1>
    <p class="hero-tagline">The questions you miss come back until they stick</p>
  </div>
</section>
<style id="rcm-rv-page">
.rcm-rv-hero{padding:34px 0 22px;}
.rcm-rv-hero h1{margin:10px 0 6px;}
.rcm-rv-hero .hero-tagline{font-size:17px;color:var(--text-mid);margin:0;}
.rcm-rv-main{max-width:860px;margin:0 auto;padding:10px 32px 40px;}
.rcm-rv-main h2{font-family:Inter,system-ui,sans-serif;}
.rcm-rv-main h3{font-family:Inter,system-ui,sans-serif;font-size:16px;margin:22px 0 22px;color:var(--text);}
.rcm-rv-how{font-size:15.5px;line-height:1.65;color:var(--text-mid);}
@media (max-width:640px){.rcm-rv-main{padding:8px 16px 32px;}}
</style>
<main class="container rcm-rv-main">
  <div id="rcm-review-app" aria-live="polite"><p class="rcm-rv-how">Loading your deck…</p>
    <noscript><p>The review deck needs JavaScript.</p></noscript></div>
  <section class="rcm-rv-how" id="how">
    <h2>How it works</h2>
    <p>Every time you check a module self-assessment or a final examination, each question you missed is copied here. Reviewing at growing intervals is one of the most reliable ways to make learning last: a card you answer right moves up one box and comes back later (after 1, 3, 7, 14, then 30 days). A card you miss goes back to box 1 and returns tomorrow. Five right answers in a row and it counts as learned.</p>
    <p>A <b>shift drill</b> of five questions takes about three minutes. When cards are due, it is served automatically on the first Academy page you open at the start of each shift (8 or more hours after the last one); &ldquo;Not this shift&rdquo; waits for the next, and the setting at the top of this page turns it off. Answering a deck question correctly in a module&rsquo;s own self-assessment also counts as a review.</p>
    <p>This is study practice, not an assessment, and it is not recorded for any certificate.</p>
  </section>
</main>
"""


def build_page():
    land = (ACADEMY / "index.html").read_text(encoding="utf-8")
    head, rest = land.split("</head>", 1)
    head = sub_meta(head + "</head>")
    body_open = rest[:rest.index("</header>") + len("</header>")]
    tail = rest[rest.index('<footer class="guide-footer">'):]
    tail = re.sub(r'<button class="print-btn".*?</button>\s*', "", tail, count=1, flags=re.S)   # no floating print on the deck
    tail = re.sub(r'\n?<script src="[^"]*assets/(academy-|schola|tech-course|guide-rail|share-buttons|image-lightbox)[^"]*" defer></script>', "", tail)
    return head + body_open + "\n" + MAIN + "\n" + tail


def wanted(name, text):
    # every academy page: capture needs #nc-quiz, the shift drill needs any page; never the emergency quick cards
    # (a quiz pop-up must not cover an action card during an emergency)
    return name != "emergency-cards.html"


def main():
    dry = "--dry-run" in sys.argv
    hashed = fingerprint(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    page = build_page()
    i = page.rfind("</body>")
    page = page[:i] + tag + "\n" + page[i:]
    dst = ACADEMY / PAGE
    changed = 0
    if not dst.exists() or dst.read_text(encoding="utf-8") != page:
        changed += 1
        if not dry:
            dst.write_text(page, encoding="utf-8")
    for f in sorted(ACADEMY.glob("*.html")):
        if f.name == PAGE:
            continue
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if wanted(f.name, text):
            k = text.rfind("</body>")
            text = text[:k] + tag + "\n" + text[k:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy review deck ({hashed}): {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
