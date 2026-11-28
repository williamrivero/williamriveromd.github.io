"""Paratus: Emergency Readiness as its own installable, offline web app (Nov 28 2026). Idempotent.

Separate from Schola: a browser allows one offline app (service worker) per address, and Schola owns /academy/,
so Paratus lives at /paratus/ with copies of the emergency pages made from the generated academy pages on every run.
Copies keep the academy page's canonical (pointing to the original) and are noindex, so search engines see one page.

Includes: Emergency Readiness (also /paratus/ itself), the Emergency Quick Cards, every Resuscitation Lab and
Disaster Preparedness page (modules, pretest, final exam, trainer, Megacode Practice Lab, Disaster Drills), the two
practice tools they link to (TOOLS) and every figure, script, style and PDF those pages use. The second display of the
Megacode Practice Lab (?display=1) is the same page, so it is saved too.

Writes
  paratus/*.html                   copies (SCHOLA-HEAD / CALC-APP block -> PARATUS-HEAD, schola.js, academy search and
                                   calc-app.js removed, assets/paratus.<hash>.js added, links outside Paratus -> /academy/ or /guides/)
  paratus/paratus.webmanifest      app "Paratus", scope /paratus/
  paratus/paratus-sw.js            service worker: pages network first (4 s) then the saved copy; assets saved copy first
  paratus/paratus-offline.json     every file: [path, content hash, bytes], plus large->small figure map
  assets/paratus.<hash>.js         fingerprinted copy of assets/paratus.js (old copies pruned)

    python3 tools/academy/build_paratus.py          # after every academy publish (publish_academy.py and CI run it)
    python3 tools/academy/build_paratus.py --report  # sizes only
"""
import hashlib, importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY, GUIDES, OUT, ASSETS = ROOT / "academy", ROOT / "guides", ROOT / "paratus", ROOT / "assets"
BASE = "https://renalcarematters.com/paratus/"
REPORT = "--report" in sys.argv

_spec = importlib.util.spec_from_file_location("build_schola", Path(__file__).with_name("build_schola.py"))
BS = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(BS)

PAGE_RE = re.compile(r"^(emergency-readiness|emergency-cards|resuscitation-lab(-.+)?|disaster-preparedness(-.+)?)\.html$")
TOOLS = ["calc-resuscitation-lab-toolkit.html", "calc-dialysis-continuity-planner.html"]
ICONS = ["/images/app/paratus-180.png", "/images/app/paratus-192.png", "/images/app/paratus-512.png",
         "/images/app/paratus-maskable-192.png", "/images/app/paratus-maskable-512.png"]

HEAD = """<!-- PARATUS-HEAD -->
<link rel="manifest" href="/paratus/paratus.webmanifest">
<link rel="apple-touch-icon" sizes="180x180" href="/images/app/paratus-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Paratus">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="robots" content="noindex">
<!-- /PARATUS-HEAD -->"""
STRIP = [re.compile(r"\n?<!-- SCHOLA-HEAD -->.*?<!-- /SCHOLA-HEAD -->", re.S),
         re.compile(r"\n?<!-- CALC-APP-START -->.*?<!-- CALC-APP-END -->", re.S),
         re.compile(r'\n?<meta name="robots"[^>]*>', re.I),
         re.compile(r'\n?<link rel="(?:manifest|apple-touch-icon)"[^>]*>', re.I),
         re.compile(r'\n?<script src="[^"]*assets/(?:schola|academy-search|paratus)(?:\.[0-9a-f]{10})?\.js" defer></script>'),
         re.compile(r'\n?<script src="[^"]*assets/calc-app\.js[^"]*" defer></script>')]
HREF_RE = re.compile(r'(\bhref=")([^"]+)(")')


def pages():
    names = sorted(p.name for p in ACADEMY.glob("*.html") if PAGE_RE.match(p.name) and not re.search(r" \d+\.html$|-draft\.html$", p.name))
    return names, [t for t in TOOLS if (GUIDES / t).is_file()]


def fingerprint():
    src = ASSETS / "paratus.js"
    b = src.read_bytes(); h = hashlib.sha1(b).hexdigest()[:10]
    name = f"paratus.{h}.js"
    for old in ASSETS.glob("paratus.*.js"):
        if old.name != name:
            old.unlink()
    (ASSETS / name).write_bytes(b)
    return name


def rewrite(text, included, js):
    for r in STRIP:
        text = r.sub("", text)
    text = text.replace("</head>", HEAD + "\n</head>", 1)

    def link(m):
        url = m.group(2)
        if url.startswith(("http:", "https:", "mailto:", "tel:", "#", "/", "javascript:", "data:", "?")):
            return m.group(0)
        path, _, frag = url.partition("#")
        frag = "#" + frag if frag else ""
        if path in ("index.html", "./", "./index.html"):
            return m.group(1) + "../academy/" + frag + m.group(3)
        if re.fullmatch(r"[a-z0-9-]+\.html", path):
            return m.group(1) + (path if path in included else "../academy/" + path) + frag + m.group(3)
        g = re.fullmatch(r"\.\./guides/([a-z0-9-]+\.html)", path)
        if g and g.group(1) in included:
            return m.group(1) + g.group(1) + frag + m.group(3)
        return m.group(0)
    text = HREF_RE.sub(link, text)
    i = text.rfind("</body>")
    return text[:i] + f'<script src="../assets/{js}" defer></script>\n' + text[i:]


def main():
    names, tools = pages()
    included = set(names) | set(tools) | {"index.html"}
    js = fingerprint() if not REPORT else "paratus.js"
    copies = {}
    for n in names:
        copies[n] = rewrite((ACADEMY / n).read_text(encoding="utf-8"), included, js)
    for t in tools:
        copies[t] = rewrite((GUIDES / t).read_text(encoding="utf-8"), included, js)
    copies["index.html"] = copies["emergency-readiness.html"]

    small, files, missing = {}, {}, set()

    def add(p):
        if p in files:
            return True
        f = BS.facts(p)
        if f is None:
            missing.add(p); return False
        files[p] = f; return True

    for n, text in copies.items():
        key = "/paratus/" if n == "index.html" else "/paratus/" + n[:-5]
        b = text.encode("utf-8"); files[key] = (hashlib.sha1(b).hexdigest()[:12], len(b))
        for r in BS.resources(text, BASE + n, small):
            if not r.startswith("/paratus/"):
                add(r)
        for pdf in re.findall(r'href="(\.\./downloads/[^"#]+\.pdf)"', text):
            add(BS.site_path(pdf, BASE + n))
    for icon in ICONS:
        add(icon)
    small = {k: v for k, v in small.items() if v in files and k != v}
    ordered = sorted(files)
    doc = {"v": 1, "files": [[p, files[p][0], files[p][1]] for p in ordered], "small": small,
           "all_bytes": sum(b for _, b in files.values())}
    doc["h"] = hashlib.sha1(json.dumps(doc, sort_keys=True).encode()).hexdigest()[:12]
    if REPORT:
        print(f"paratus: {len(copies)} pages, {len(files)} files, {doc['all_bytes'] / 1e6:.1f} MB; missing {sorted(missing)[:5]}")
        return
    OUT.mkdir(exist_ok=True)
    keep = set(copies) | {"paratus.webmanifest", "paratus-sw.js", "paratus-offline.json"}
    for old in OUT.glob("*.html"):
        if old.name not in keep:
            old.unlink()
    for n, text in copies.items():
        f = OUT / n
        if not f.exists() or f.read_text(encoding="utf-8") != text:
            f.write_text(text, encoding="utf-8")
    # the Academy's own emergency pages carry the Paratus drawer too (download there; install in /paratus/)
    for n in names:
        f = ACADEMY / n; t = f.read_text(encoding="utf-8")
        u = re.sub(r'\n?<script src="/assets/paratus(?:\.[0-9a-f]{10})?\.js" defer></script>', "", t)
        i = u.rfind("</body>"); u = u[:i] + f'<script src="/assets/{js}" defer></script>\n' + u[i:]
        if u != t:
            f.write_text(u, encoding="utf-8")
    (OUT / "paratus-offline.json").write_text(json.dumps(doc, separators=(",", ":")), encoding="utf-8")
    (OUT / "paratus.webmanifest").write_text(json.dumps(MANIFEST, indent=1) + "\n", encoding="utf-8")
    (OUT / "paratus-sw.js").write_text(SW_JS.replace("__V__", hashlib.sha1(SW_JS.encode()).hexdigest()[:10]), encoding="utf-8")
    print(f"paratus ({js}): {len(copies)} pages, {len(files)} files, {doc['all_bytes'] / 1e6:.1f} MB"
          + (f"; {len(missing)} referenced files not found: {sorted(missing)[:5]}" if missing else ""))


MANIFEST = {
    "id": "/paratus/",
    "name": "Paratus · Emergency Readiness",
    "short_name": "Paratus",
    "description": "Emergency quick cards, the Dialysis Team Resuscitation Lab, Disaster Preparedness and the practice labs, saved for use without signal.",
    "start_url": "/paratus/?source=paratus",
    "scope": "/paratus/",
    "display": "standalone",
    "background_color": "#7f1d1d",
    "theme_color": "#7f1d1d",
    "icons": [
        {"src": "/images/app/paratus-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/paratus-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        {"src": "/images/app/paratus-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
        {"src": "/images/app/paratus-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}

SW_JS = r"""/* Paratus service worker (Emergency Readiness app). Generated by tools/academy/build_paratus.py: do not edit.
   Pages under /paratus/: network first; after 4 s without an answer, or with no signal, the saved copy (Download
   Paratus), else a recently opened copy, else a short "not saved" page. Query strings (the ?display=1 second display)
   use the same saved page. Figures, scripts and styles: the saved copy first, else the network; with no signal a large
   figure falls back to the small copy that was saved. */
var V = '__V__', SAVED = 'paratus-saved', RECENT = 'paratus-recent', MAN = '/paratus/paratus-offline.json';
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });
function key(u) {
  var p = u.pathname;
  if (p === '/paratus' || p === '/paratus/index' || p === '/paratus/index.html') return '/paratus/';
  if (p.indexOf('/paratus/') === 0) p = p.replace(/\.html$/, '');
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
self.addEventListener('message', function (e) { if (e.data === 'paratus-refresh') small = null; });
function offlinePage() {
  var body = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    + '<title>Not saved for offline use</title><style>body{font:17px/1.55 system-ui,-apple-system,"Segoe UI",Arial,sans-serif;margin:0;'
    + 'background:#7f1d1d;color:#fff;display:flex;min-height:100vh;align-items:center;justify-content:center;padding:24px;box-sizing:border-box}'
    + 'main{max-width:420px;text-align:center}h1{font-size:24px;margin:0 0 8px}p{opacity:.92}a{display:inline-block;margin-top:14px;'
    + 'background:#fff;color:#7f1d1d;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:12px}</style></head><body><main>'
    + '<h1>This page is not saved yet</h1><p>You are offline, and Paratus has not been downloaded on this device. '
    + 'When you have signal again, open Paratus and tap <b>Download Paratus</b>.</p><a href="/paratus/">Open Paratus</a></main></body></html>';
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
  if (u.pathname === '/paratus/paratus-sw.js' || u.pathname === MAN || u.pathname.indexOf('/api/') === 0) return;
  var k = key(u);
  if (req.mode === 'navigate' || (req.destination === 'iframe' && k.indexOf('/paratus/') === 0)) {
    if (k.indexOf('/paratus/') !== 0) return;
    e.respondWith(new Promise(function (resolve) {
      var done = false;
      function finish(r) { if (!done) { done = true; resolve(r); } }
      function fallback(failed) {
        if (done) return;
        saved(k).then(function (r) { if (r) finish(r); else if (failed) finish(offlinePage()); })
          .catch(function () { if (failed) finish(offlinePage()); });
      }
      fetch(req).then(function (r) {
        if (r && r.ok && r.type === 'basic') remember(k, r.clone());
        finish(r);
      }).catch(function () { fallback(true); });
      setTimeout(function () { fallback(false); }, 4000);
    }));
    return;
  }
  if (req.cache === 'no-cache' || req.cache === 'reload' || req.cache === 'no-store') {
    e.respondWith(fetch(req).catch(function () {
      return caches.open(SAVED).then(function (c) { return c.match(k); }).then(function (r) { return r || Response.error(); });
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
