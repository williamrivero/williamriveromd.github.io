"""Schola: the Renal Care Academy as an installable, offline web app (Dr. Rivero, Nov 25 2026). Idempotent.

Writes
  academy/schola.webmanifest     app name "Schola", scope /academy/, icons images/app/schola-*.png
  academy/schola-sw.js           service worker: saved copy when there is no signal, small figure copies offline
  academy/schola-offline.json    what to save, per track: [path, content hash, bytes] for every page and every
                                 figure/asset those pages actually display, plus the shared shell (landing page,
                                 scripts, theme files, icons) and a map from large figure copies to the small one saved

Learners save one track at a time (its hub, modules, final exam and trainer page) or every track at once
(Dr. Rivero chose "per track + Download all"). Only the figure a phone displays is saved: the smallest candidate of
each <picture>/<img srcset> (the PNG fallback inside a WebP <picture> is never fetched by browsers, so it is skipped).
The worker serves that small copy when a larger one is requested without signal. assets/schola.js (loaded on every
academy page by apply_notes.py) draws the install / download panel and does the downloads.

    python3 tools/academy/build_schola.py            # run after every academy publish (publish_academy.py and CI do)
    python3 tools/academy/build_schola.py --report   # per-track sizes, no writes

A file missing from the working copy (a sparse checkout) is sized from `git ls-tree -l` and hashed by its git blob id.
"""
import hashlib, html, json, os, re, subprocess, sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
BASE = "https://renalcarematters.com/academy/"
REPORT = "--report" in sys.argv

ICONS = ["/images/app/schola-180.png", "/images/app/schola-192.png", "/images/app/schola-512.png",
         "/images/app/schola-maskable-192.png", "/images/app/schola-maskable-512.png"]

# ── file facts: content hash + size, from disk or from git ─────────────────────────────────────────────────
_git = None


def git_facts():
    global _git
    if _git is None:
        _git = {}
        try:
            out = subprocess.run(["git", "ls-tree", "-r", "-l", "HEAD"], cwd=ROOT, capture_output=True, text=True,
                                 env=dict(os.environ, GIT_NO_LAZY_FETCH="1")).stdout
            for line in out.splitlines():
                meta, path = line.split("\t", 1)
                parts = meta.split()
                if len(parts) == 4 and parts[3].isdigit():
                    _git["/" + path] = (parts[2][:12], int(parts[3]))
        except Exception:
            pass
        tsv = os.environ.get("SCHOLA_SIZES")            # optional path<TAB>size list for sparse checkouts
        if tsv and os.path.exists(tsv):
            for line in open(tsv, encoding="utf-8"):
                p, s = line.rstrip("\n").split("\t")
                key = "/" + p
                h = _git.get(key, (hashlib.sha1(key.encode()).hexdigest()[:12], 0))[0]
                _git.setdefault(key, (h, int(s)))
                if _git[key][1] == 0:
                    _git[key] = (h, int(s))
    return _git


def facts(path):
    """(hash, bytes) for a site path like /images/x.webp, or None if the file does not exist."""
    f = ROOT / path.lstrip("/")
    if f.is_file():
        b = f.read_bytes()
        return hashlib.sha1(b).hexdigest()[:12], len(b)
    return git_facts().get(path)


# ── what each page displays ────────────────────────────────────────────────────────────────────────────────
def page_key(name):
    return "/academy/" if name == "index.html" else "/academy/" + name[:-5]


def site_path(ref, page_url):
    ref = html.unescape(ref.strip())
    if not ref or "'" in ref or "+" in ref or ref.startswith(("data:", "#", "mailto:", "tel:", "javascript:")):
        return None
    u = urlparse(urljoin(page_url, ref))
    if u.netloc and u.netloc != "renalcarematters.com":
        return None
    return u.path


def candidates(srcset):
    out = []
    for part in srcset.split(","):
        bits = part.strip().split()
        if not bits:
            continue
        w = 10 ** 9
        if len(bits) > 1 and bits[1].endswith("w") and bits[1][:-1].isdigit():
            w = int(bits[1][:-1])
        out.append((w, bits[0]))
    return [r for _, r in sorted(out)]


PICTURE_RE = re.compile(r"<picture\b.*?</picture>", re.S | re.I)
SOURCE_RE = re.compile(r"<source\b[^>]*>", re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ATTR = lambda name: re.compile(r'\b' + name + r'\s*=\s*"([^"]*)"', re.I)
SRC, SRCSET, HREF, REL, TYPE = ATTR("src"), ATTR("srcset"), ATTR("href"), ATTR("rel"), ATTR("type")
SCRIPT_RE = re.compile(r'<script\b[^>]*\bsrc\s*=\s*"([^"]+)"', re.I)
LINK_RE = re.compile(r"<link\b[^>]*>", re.I)
URL_RE = re.compile(r"url\(\s*['\"]?((?:\.\./|/)[^'\")\s]+)['\"]?\s*\)")
THEME_RE = re.compile(r"/assets/theme[-a-z]*\.[0-9a-f]{10}\.(?:js|css)")


def resources(text, page_url, small):
    """Site paths a page displays (smallest figure candidates only) and large->small figure pairs."""
    need = set()

    def pick(srcset_value, extra=()):
        cands = [site_path(c, page_url) for c in candidates(srcset_value)]
        cands = [c for c in cands if c]
        if not cands:
            return
        need.add(cands[0])
        for big in list(cands[1:]) + [e for e in extra if e]:
            if big != cands[0]:
                small.setdefault(big, cands[0])

    body = text
    for pic in PICTURE_RE.findall(text):
        body = body.replace(pic, "")
        srcs = SOURCE_RE.findall(pic)
        imgs = IMG_RE.findall(pic)
        fallback = [site_path(SRC.search(i).group(1), page_url) for i in imgs if SRC.search(i)]
        if srcs:
            for s in srcs:
                m = SRCSET.search(s)
                if m:
                    pick(m.group(1), fallback)
        else:
            for i in imgs:
                m = SRCSET.search(i) or SRC.search(i)
                if m:
                    pick(m.group(1))
    for i in IMG_RE.findall(body):
        m = SRCSET.search(i)
        s = SRC.search(i)
        if m:
            pick(m.group(1), [site_path(s.group(1), page_url)] if s else [])
        elif s:
            p = site_path(s.group(1), page_url)
            if p:
                need.add(p)
    for s in SCRIPT_RE.findall(text):
        p = site_path(s, page_url)
        if p:
            need.add(p)
    for l in LINK_RE.findall(text):
        rel = (REL.search(l).group(1) if REL.search(l) else "").lower()
        h = HREF.search(l)
        if h and ("stylesheet" in rel or rel in ("icon", "apple-touch-icon", "manifest")):
            p = site_path(h.group(1), page_url)
            if p:
                need.add(p)
    for u in URL_RE.findall(text):
        p = site_path(u, page_url)
        if p:
            need.add(p)
    need.update(THEME_RE.findall(text))
    return need


# ── tracks ─────────────────────────────────────────────────────────────────────────────────────────────────
SHARED_PAGES = ("index.html", "review-deck.html")


def hub_names(names):
    return [n[:-5] for n in names if n not in SHARED_PAGES and not re.search(r"-\d{2}-|final-exam|trainer", n)]


def track_of(name, hubs):
    stem = name[:-5]
    best = ""
    for h in hubs:
        if (stem == h or stem.startswith(h + "-")) and len(h) > len(best):
            best = h
    return best or None


def h1_text(text):
    m = re.search(r"<h1\b[^>]*>(.*?)</h1>", text, re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", m.group(1)) if m else ""
    t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    return re.sub(r"(\w[-/]) (?=\w)", r"\1", t)          # "Physician-on-<wbr>Duty" reads as one word


def main():
    names = sorted(p.name for p in ACADEMY.glob("*.html") if not re.search(r" \d+\.html$", p.name))   # skip iCloud "page 2.html" copies
    hubs = hub_names(names)
    texts = {n: (ACADEMY / n).read_text(encoding="utf-8") for n in names}
    small = {}
    page_res = {}
    for n in names:
        page_res[n] = resources(texts[n], BASE + n, small)

    files = {}                                     # path -> (hash, bytes)

    def add(path):
        if path in files:
            return True
        f = facts(path)
        if f is None:
            return False
        files[path] = f
        return True

    missing = set()
    shared = set()
    # landing page + its resources are shared by every download
    for n in [x for x in SHARED_PAGES if x in page_res]:   # landing page + review deck (Nov 27 2026)
        key = page_key(n)
        files[key] = facts("/academy/" + n)
        shared.add(key)
        for r in page_res[n]:
            (shared.add(r) if add(r) else missing.add(r))
    for icon in ICONS:
        if add(icon):
            shared.add(icon)

    # landing page order of tracks
    order = {h: i for i, h in enumerate(dict.fromkeys(re.findall(r'href="(?:\./)?([a-z0-9-]+)\.html"', texts.get("index.html", ""))))}
    tracks = {}
    for n in names:
        if n in SHARED_PAGES:
            continue
        t = track_of(n, hubs)
        if not t:
            t = n[:-5]
        tr = tracks.setdefault(t, {"id": t, "title": "", "pages": 0, "paths": set()})
        key = page_key(n)
        files[key] = facts("/academy/" + n)
        tr["paths"].add(key)
        tr["pages"] += 1
        if n[:-5] == t:
            tr["title"] = h1_text(texts[n]) or t
        for r in page_res[n]:
            (tr["paths"].add(r) if add(r) else missing.add(r))

    ordered = sorted(files)
    index = {p: i for i, p in enumerate(ordered)}
    out_tracks = []
    for t in sorted(tracks.values(), key=lambda x: (order.get(x["id"], 10 ** 6), x["title"] or x["id"])):
        paths = sorted(t["paths"] - shared)
        h = hashlib.sha1("".join(files[p][0] for p in paths).encode()).hexdigest()[:12]
        out_tracks.append({"id": t["id"], "title": t["title"] or t["id"], "pages": t["pages"],
                           "bytes": sum(files[p][1] for p in paths), "h": h,
                           "files": [index[p] for p in paths]})
    shared_idx = sorted(index[p] for p in shared)
    shared_bytes = sum(files[p][1] for p in shared)
    all_bytes = sum(b for _, b in files.values())
    small = {k: v for k, v in small.items() if v in files and k != v}
    doc = {
        "v": 1,
        "files": [[p, files[p][0], files[p][1]] for p in ordered],
        "shared": shared_idx, "shared_bytes": shared_bytes, "all_bytes": all_bytes,
        "tracks": out_tracks, "small": small,
    }
    doc["h"] = hashlib.sha1(json.dumps(doc, sort_keys=True).encode()).hexdigest()[:12]

    if REPORT:
        for t in out_tracks:
            print(f"{t['title'][:46]:46s} {t['pages']:3d} pages {t['bytes'] / 1e6:7.1f} MB")
        print(f"shared {shared_bytes / 1e6:.1f} MB · everything {all_bytes / 1e6:.1f} MB · {len(files)} files"
              f" · {len(out_tracks)} tracks · {len(missing)} referenced files not found")
        return

    (ACADEMY / "schola-offline.json").write_text(json.dumps(doc, separators=(",", ":")), encoding="utf-8")
    (ACADEMY / "schola.webmanifest").write_text(json.dumps(MANIFEST, indent=1) + "\n", encoding="utf-8")
    sw = SW_JS.replace("__V__", hashlib.sha1(SW_JS.encode()).hexdigest()[:10])
    (ACADEMY / "schola-sw.js").write_text(sw, encoding="utf-8")
    print(f"schola: {len(out_tracks)} tracks, {len(files)} files, everything {all_bytes / 1e6:.0f} MB"
          + (f"; {len(missing)} referenced files not found: {sorted(missing)[:5]}" if missing else ""))


MANIFEST = {
    "id": "/academy/",
    "name": "Schola · Renal Care Academy",
    "short_name": "Schola",
    "description": "Free, structured training for every role in kidney care, saved for study without signal.",
    "start_url": "/academy/?source=schola",
    "scope": "/academy/",
    "display": "standalone",
    "background_color": "#1F3864",
    "theme_color": "#1F3864",
    "icons": [
        {"src": "/images/app/schola-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/schola-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/schola-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/schola-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}

SW_JS = r"""/* Schola service worker (Renal Care Academy app). Generated by tools/academy/build_schola.py: do not edit.
   Pages: network first; after 4 s without an answer, or with no signal, the saved copy (Save this track /
   Download all), else a recently opened copy, else a short "not saved" page. Figures, scripts and styles: the
   saved copy first, else the network; with no signal a large figure falls back to the small copy that was saved. */
var V = '__V__', SAVED = 'schola-saved', RECENT = 'schola-recent', MAN = '/academy/schola-offline.json';
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });

function key(u) {
  var p = u.pathname;
  if (p === '/academy' || p === '/academy/index' || p === '/academy/index.html') return '/academy/';
  if (p.indexOf('/academy/') === 0) p = p.replace(/\.html$/, '');
  return p;
}
var small = null;
function smallMap() {
  if (small) return Promise.resolve(small);
  return caches.open(SAVED).then(function (c) { return c.match(MAN); })
    .then(function (r) { return r ? r.json() : {}; })
    .then(function (m) { small = (m && m.small) || {}; return small; })
    .catch(function () { small = {}; return small; });
}
self.addEventListener('message', function (e) { if (e.data === 'schola-refresh') small = null; });

function offlinePage() {
  var body = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    + '<title>Not saved for offline use</title><style>body{font:17px/1.55 system-ui,-apple-system,"Segoe UI",Arial,sans-serif;margin:0;'
    + 'background:#1F3864;color:#fff;display:flex;min-height:100vh;align-items:center;justify-content:center;padding:24px;box-sizing:border-box}'
    + 'main{max-width:420px;text-align:center}h1{font-size:24px;margin:0 0 8px}p{opacity:.9}a{display:inline-block;margin-top:14px;'
    + 'background:#C55A11;color:#fff;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:12px}</style></head><body><main>'
    + '<h1>This page is not saved yet</h1><p>You are offline, and this page is not part of a track you saved in Schola. '
    + 'When you have signal again, open the track and tap <b>Save this track</b>.</p><a href="/academy/">Go to the Academy</a></main></body></html>';
  return new Response(body, { headers: { 'Content-Type': 'text/html; charset=utf-8' } });
}
function remember(k, resp) {
  caches.open(RECENT).then(function (c) {
    return c.put(k, resp).then(function () { return c.keys(); }).then(function (ks) {
      for (var i = 0; i < ks.length - 40; i++) c.delete(ks[i]);
    });
  }).catch(function () {});
}
function saved(k) {
  return caches.open(SAVED).then(function (c) { return c.match(k); }).then(function (r) {
    return r || caches.open(RECENT).then(function (c) { return c.match(k); });
  });
}

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var u = new URL(req.url);
  if (u.origin !== self.location.origin) return;
  if (u.pathname === '/academy/schola-sw.js' || u.pathname === MAN) return;
  var k = key(u);
  if (req.mode === 'navigate') {
    if (k.indexOf('/academy/') !== 0) return;
    e.respondWith(new Promise(function (resolve) {
      var done = false;
      function finish(r) { if (!done) { done = true; resolve(r); } }
      function fallback(failed) {
        if (done) return;
        saved(k).then(function (r) {
          if (r) finish(r);
          else if (failed) finish(offlinePage());
        }).catch(function () { if (failed) finish(offlinePage()); });
      }
      fetch(req).then(function (r) {
        if (r && r.ok && r.type === 'basic') remember(k, r.clone());
        finish(r);
      }).catch(function () { fallback(true); });
      setTimeout(function () { fallback(false); }, 4000);
    }));
    return;
  }
  e.respondWith(caches.open(SAVED).then(function (c) {
    return c.match(k).then(function (hit) {
      if (hit) return hit;
      return fetch(req).catch(function () {
        return smallMap().then(function (m) { return m[k] ? c.match(m[k]) : null; })
          .then(function (r) { return r || Response.error(); });
      });
    });
  }));
});
"""

if __name__ == "__main__":
    main()
