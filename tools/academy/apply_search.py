"""Academy-wide search with Pagefind (Dr. Rivero, Nov 28 2026). Idempotent.

Pagefind (https://pagefind.app, MIT) builds a static search index: a few hundred small files that the browser
fetches on demand. No server, no account, nothing sent anywhere, and because the index is plain files it is saved
with Schola (academy/schola-offline.json "shared"), so search also works with no signal.

  assets/academy-search.js     the search dialog (edit this); fingerprinted to assets/academy-search.<hash>.js
  academy/pagefind/            the index (generated; never hand-edit). pagefind.js + wasm + chunks + fragments

What is indexed: the landing page, track homes, modules, trainer / educator pages, the emergency quick cards, the
Emergency Readiness, Resuscitation Lab and Disaster Preparedness homes, and the team drill. Not indexed: final
exams, placement pre-tests, practice labs and the review deck (they hold the question banks), and drafts.
Inside a page: the hero title and subtitle plus <main>, without the self-assessment (#quiz), the interactive case
(#sim), forms, citation markers, the module pager and buttons. Each section's id is copied to its first heading,
so a result can open the exact section (Pagefind "sub results").

Filters: track (the subtrack name as shown in the landing hero) and kind (Module, Track home, Trainer page,
Emergency, Academy). Meta: track, kind, module number.

This patcher:
  1. builds academy/pagefind/ (needs `pip install 'pagefind[extended]'`; without it the index is left as it is and a
     note is printed: CI builds it on every push, see .github/workflows/sitemap.yml);
  2. fingerprints assets/academy-search.js (older copies pruned; _headers caches /assets/academy-search.* immutable);
  3. puts <script src="../assets/academy-search.<hash>.js" defer></script> before </body> on every academy page.

Run after every publish, before build_schola.py (publish_academy.py does), so the index joins the offline list.

    python3 tools/academy/apply_search.py              # index + tag
    python3 tools/academy/apply_search.py --no-index   # tag only
    python3 tools/academy/apply_search.py --dry-run    # report only
"""
import asyncio, hashlib, html, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
OUT = ACADEMY / "pagefind"
NAME = "academy-search"
TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js" defer></script>')

SKIP = re.compile(r"(-final-exam|-pretest|-practice|-draft| \d+)\.html$|^review-deck\.html$|^verify\.html$")
EMERGENCY = ("emergency-cards", "emergency-readiness", "resuscitation-lab", "disaster-preparedness")
EXCLUDE = ["#quiz", "#sim", "form", "button", "script", "style", "noscript", "template", "sup.nc-cite", ".nc-cite",
           ".nc-nextprev", ".rcm-tts-ui", ".rcm-sk-ui", ".rcn-ui", ".rcm-share", ".rcm-share-slot", "[aria-hidden='true']",
           ".lang-hidden", ".acad-tracks"]


def text_of(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment or "")
    t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    return re.sub(r"(\w[-/]) (?=\w)", r"\1", t)


def hero_names():
    """Subtrack names as shown in the landing hero tiles (the names learners know)."""
    s = (ACADEMY / "index.html").read_text(encoding="utf-8")
    i = s.find('class="acad-tracks acad-cols')
    out = {}
    for m in re.finditer(r'<a class="acad-track[^"]*" href="([a-z0-9-]+)\.html"[^>]*>.*?<strong>(.*?)</strong>', s[i:i + 60000], re.S):
        out[m.group(1)] = text_of(m.group(2).replace("<wbr>", "")).replace("/", " / ").replace("  ", " ")
    return out


def hubs(names):
    return [n[:-5] for n in names if not re.search(r"-\d{2}-|final-exam|trainer|educator|-pretest\.html$|-practice\.html$", n)
            and n not in ("index.html", "review-deck.html", "same-event-every-role.html", "emergency-cards.html")]


def track_of(stem, hub_list):
    best = ""
    for h in hub_list:
        if (stem == h or stem.startswith(h + "-")) and len(h) > len(best):
            best = h
    return best or None


def kind_of(stem):
    if stem == "index" or stem == "same-event-every-role":
        return "Academy"
    if any(stem.startswith(e) for e in EMERGENCY):
        return "Emergency" if not re.search(r"-\d\d-", stem) else "Module"
    if re.search(r"-\d\d-", stem):
        return "Module"
    if stem.endswith("-trainer") or stem.endswith("-educator"):
        return "Trainer page"
    return "Track home"


def record(page, names, hub_list):
    """The HTML handed to Pagefind for one page: title, subtitle and <main>, with filters and meta."""
    stem = page.stem
    s = page.read_text(encoding="utf-8")
    m = re.search(r"<main\b[^>]*>(.*)</main>", s, re.S)
    if not m:
        return []
    body = m.group(1)
    # copy each section's id onto its first heading, so results can link to the section
    def sec(mm):
        block, sid = mm.group(0), mm.group(1)
        return re.sub(r"<(h[23])(?![^>]*\bid=)([^>]*)>", lambda h: f'<{h.group(1)} id="{sid}"{h.group(2)}>', block, count=1)
    body = re.sub(r'<section\b[^>]*\bid="([^"]+)"[^>]*>.*?(?=<section\b|$)', sec, body, flags=re.S)
    h1 = re.search(r"<h1\b[^>]*>(.*?)</h1>", s, re.S)
    sub = re.search(r'<p class="(?:hero-sub|hero-tagline)"[^>]*>(.*?)</p>', s, re.S)
    title = text_of(h1.group(1)) if h1 else stem
    track_id = track_of(stem, hub_list)
    track = names.get(track_id) or (text_of(re.search(r"<h1\b[^>]*>(.*?)</h1>", (ACADEMY / (track_id + ".html")).read_text(encoding="utf-8"), re.S).group(1))
                                      if track_id and (ACADEMY / (track_id + ".html")).exists() else "Renal Care Academy")
    if kind_of(stem) == "Academy":
        track = "Renal Care Academy"
    if stem == "emergency-cards":
        track = "Emergency quick cards"
    kind = kind_of(stem)
    num = re.search(r"-(\d\d)-", stem)
    mod = str(int(num.group(1))) if num else ""
    meta = (f'<span data-pagefind-meta="track">{html.escape(track)}</span>'
            f'<span data-pagefind-meta="kind">{kind}</span>'
            + (f'<span data-pagefind-meta="mod">{mod}</span>' if mod else "")
            + f'<span data-pagefind-filter="track">{html.escape(track)}</span>'
            f'<span data-pagefind-filter="kind">{kind}</span>')
    doc = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body>'
           f'<main data-pagefind-body><div data-pagefind-ignore="index">{meta}</div><h1>{html.escape(title)}</h1>'
           + (f"<p>{sub.group(1)}</p>" if sub else "") + body + "</main></body></html>")
    url = "/academy/" if stem == "index" else f"/academy/{stem}.html"
    out = [(url, doc)]
    if stem == "emergency-cards":
        # one record per card, so "blood leak alarm" finds that card, not a long page that mentions everything
        cards = list(re.finditer(r'<article class="eqc[^"]*" id="([a-z-]+)"[^>]*>(.*?)</article>', body, re.S))
        for c in cards:
            h = re.search(r"<h2\b[^>]*>(.*?)</h2>", c.group(2), re.S)
            ct = text_of(h.group(1)) if h else c.group(1)
            cdoc = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(ct)}</title></head><body>'
                    f'<main data-pagefind-body><div data-pagefind-ignore="index">' + meta.replace(">Academy<", ">Emergency<") + '</div>'
                    f'<h1>{html.escape(ct)}</h1>{c.group(2)}</main></body></html>')
            out.append((f"/academy/emergency-cards.html#{c.group(1)}", cdoc))
        body_wo = body
        for c in reversed(cards):
            body_wo = body_wo[:c.start()] + body_wo[c.end():]
        out[0] = (url, doc.replace(body, body_wo))
    return out


async def build_index(pages, names, hub_list):
    from pagefind.index import PagefindIndex, IndexConfig
    tmp = OUT.with_name("pagefind.tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    cfg = IndexConfig(exclude_selectors=EXCLUDE, force_language="en", output_path=str(tmp))
    n = 0
    async with PagefindIndex(config=cfg) as index:
        for p in pages:
            for url, doc in record(p, names, hub_list) or []:
                await index.add_html_file(content=doc, url=url)
                n += 1
        await index.write_files(output_path=str(tmp))
    shutil.rmtree(OUT, ignore_errors=True)
    tmp.rename(OUT)
    for junk in OUT.glob("pagefind-ui*"):          # we ship our own dialog, not the default UI
        junk.unlink()
    for junk in ("pagefind-highlight.js", "pagefind-modular-ui.js", "pagefind-modular-ui.css", "pagefind-component-ui.js",
                 "pagefind-component-ui.css"):
        (OUT / junk).unlink(missing_ok=True)
    return n


def bundle(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


HERO_START, HERO_END = "<!-- ACADEMY-SEARCH-HERO-START -->", "<!-- ACADEMY-SEARCH-HERO-END -->"
HERO_CSS = """.rcm-srch-hero{display:flex;align-items:center;gap:10px;width:100%;max-width:560px;margin:16px 0 4px;padding:12px 16px;border-radius:14px;cursor:text;border:1px solid rgba(31,56,100,.25);background:rgba(255,255,255,.92);color:#3d4a5c;font:500 15px/1.3 Manrope,Inter,system-ui,sans-serif;text-align:left;box-shadow:0 2px 10px rgba(18,58,54,.10);}.rcm-srch-hero svg{width:18px;height:18px;flex:none;color:#1a6b72;}.rcm-srch-hero kbd{margin-left:auto;font:600 11px/1 Inter,system-ui,sans-serif;padding:3px 6px;border-radius:5px;border:1px solid #c9d3df;color:#5b6778;}html[data-theme="dark"] .rcm-srch-hero{background:rgba(20,28,42,.9);color:#c9d3df;border-color:#3a4a62;}.rcm-srch-hero kbd{display:none;}@media (hover:hover) and (pointer:fine){.rcm-srch-hero kbd{display:inline-block;}}@media print{.rcm-srch-hero{display:none!important;}}"""
HERO = (HERO_START + '<style id="rcm-srch-hero-css">' + HERO_CSS + '</style>'
        '<button type="button" class="rcm-srch-hero rcn-ui" data-rcm-search aria-label="Search the Academy">'
        '<svg viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2.2"/>'
        '<path d="M20 20l-4.2-4.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'
        '<span>Search every track and module</span><kbd>/</kbd></button>' + HERO_END)


def landing_field(text):
    """A search field under the landing hero subtitle, in the HTML itself (no layout shift when the script loads)."""
    text = re.sub(re.escape(HERO_START) + r".*?" + re.escape(HERO_END), "", text, flags=re.S)
    m = re.search(r'<p class="hero-tagline"[^>]*>.*?</p>', text, re.S)
    return text[:m.end()] + HERO + text[m.end():] if m else text


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    dry = "--dry-run" in argv
    names = sorted(p.name for p in ACADEMY.glob("*.html"))
    pages = [ACADEMY / n for n in names if not SKIP.search(n)]
    if not dry and "--no-index" not in argv:
        try:
            import pagefind  # noqa: F401
            n = asyncio.run(build_index(pages, hero_names(), hubs(names)))
            files = sum(1 for _ in OUT.rglob("*") if _.is_file())
            size = sum(_.stat().st_size for _ in OUT.rglob("*") if _.is_file())
            print(f"academy search index: {n} pages, {files} files, {size / 1e6:.1f} MB")
        except ImportError:
            print("academy search: pagefind not installed (pip install 'pagefind[extended]'); index left as it is")
    hashed = bundle(dry)
    tag = f'<script src="../assets/{hashed}" defer></script>'
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", old)
        if f.name == "index.html":
            text = landing_field(text)
        i = text.rfind("</body>")
        text = text[:i] + tag + "\n" + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy search ({hashed}): {changed} page(s) tagged" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
