/* Paratus: Emergency Readiness as an installable, offline app (renalcarematters.com/paratus/, Nov 28 2026).
   Loaded on every /paratus/ page by tools/academy/build_paratus.py (edit this file, then run the build).
   - registers the service worker (/paratus/paratus-sw.js, scope /paratus/)
   - home page (/paratus/): install steps and the one complete offline download
   - installed app: bottom bar (Back · Home · Cards · Practice · Print) and an "offline" badge
   - the emergency cards' own "Save for offline use" (a Schola feature) is hidden: Paratus saves everything at once
   - Megacode Practice Lab on iPhone/iPad Home Screen: a note on running the second display */
(function () {
  'use strict';
  var SAVED = 'paratus-saved', KEY = 'rcm-paratus-offline', MAN = '/paratus/paratus-offline.json', HOME = '/paratus/';
  if (/[?&]thumb=1/.test(location.search)) return;   // the live-view thumbnail inside the practice page stays bare

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/paratus/paratus-sw.js', { scope: '/paratus/' }).catch(function () {});
    });
  }
  function standalone() { return (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true; }
  function ios() { return /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1); }
  function onHome() { return /^\/paratus\/?(index(\.html)?)?$/.test(location.pathname); }
  var display = /[?&]display=1/.test(location.search);
  // Also loaded on the Academy's emergency pages (Nov 28 2026): there it adds only the drawer (download works there;
  // installing happens in /paratus/, because an Academy page installs Schola), below the Schola and Emergency tabs.
  var inApp = location.pathname.indexOf('/paratus') === 0;

  var css = ''
    + '.pa-panel{position:fixed;z-index:100001;top:0;left:0;bottom:0;margin:0;width:min(460px,94vw);box-sizing:border-box;overflow-y:auto;overscroll-behavior:contain;'
    + 'padding:20px 22px calc(24px + env(safe-area-inset-bottom,0px));border:0;border-right:1px solid #f1c4c4;border-radius:0 16px 16px 0;background:linear-gradient(180deg,#fff5f5,#fff);color:#1e2a38;'
    + 'box-shadow:6px 0 28px rgba(15,30,46,.18);transform:translateX(-105%);visibility:hidden;transition:transform .22s ease,visibility 0s linear .22s}'
    + '.pa-panel.pa-open{transform:none;visibility:visible;transition:transform .22s ease}'
    + '.pa-panel .pa-grid{grid-template-columns:1fr}'
    + '.pa-x-close{margin-left:auto;align-self:flex-start;border:0;background:none;font-size:28px;line-height:1;color:#7f1d1d;cursor:pointer;padding:0 4px}'
    + '.pa-scrim{position:fixed;inset:0;z-index:100000;background:rgba(10,18,32,.45);opacity:0;pointer-events:none;transition:opacity .2s}.pa-scrim.pa-open{opacity:1;pointer-events:auto}'
    + '.pa-tab{position:fixed;z-index:9996;left:0;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;padding:12px 7px;border:0;border-radius:0 12px 12px 0;'
    + 'background:#7f1d1d;color:#fff;cursor:pointer;box-shadow:4px 6px 20px rgba(15,30,46,.25)}'
    + '.pa-tab img{border-radius:6px}.pa-tab span{writing-mode:vertical-rl;transform:rotate(180deg);font:700 13px Inter,system-ui,sans-serif;letter-spacing:.04em}.pa-tab:hover{background:#991b1b}'
    + '@media (max-width:640px){.pa-tab{top:auto;left:24px;bottom:calc(100px + env(safe-area-inset-bottom,0px));transform:none;width:44px;height:44px;padding:0;border-radius:50%;justify-content:center}'
    + '.pa-tab span{display:none}.pa-tab img{width:30px;height:30px;border-radius:8px}html.pa-standalone .pa-tab{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px))}}'
    + 'html[data-theme="dark"] .pa-x-close{color:#fca5a5}'
    + '@media print{.pa-tab,.pa-scrim{display:none!important}}'
    + '.pa-panel h2{display:flex;align-items:center;gap:10px;flex-wrap:nowrap;font:800 21px/1.25 Inter,system-ui,sans-serif;margin:0 0 6px;color:#7f1d1d}'
    + '.pa-panel h2 img{width:34px;height:34px;border-radius:9px}'
    + '.pa-lead{font-size:15px;line-height:1.6;margin:0 0 14px;color:#34455f;text-align:left}'
    + '.pa-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}'
    + '.pa-card{border:1px solid #ecd4d4;border-radius:12px;padding:14px 16px;background:#fff}'
    + '.pa-card h3{font:700 15.5px/1.3 Inter,system-ui,sans-serif;margin:0 0 8px;color:#1e2a38}'
    + '.pa-card p,.pa-card li{font-size:14px;line-height:1.6;color:#34455f;text-align:left;margin:0 0 8px}'
    + '.pa-card ol{margin:4px 0 6px 20px;padding:0}'
    + '.pa-btn{display:inline-flex;align-items:center;font:700 14px/1 Inter,system-ui,sans-serif;color:#fff;background:#991b1b;border:1px solid #991b1b;border-radius:9px;padding:11px 15px;margin:2px 8px 8px 0;cursor:pointer}'
    + '.pa-btn:hover{background:#7f1d1d}.pa-btn[disabled]{opacity:.6;cursor:progress}.pa-btn.pa-ghost{color:#991b1b;background:transparent;border-color:rgba(153,27,27,.45)}'
    + '.pa-card progress{width:100%;height:8px;margin:2px 0 10px;accent-color:#991b1b}'
    + '.pa-note{font-size:13px!important;color:#5b6b82!important}'
    + '.pa-warn{max-width:860px;margin:14px auto;font-size:14px;line-height:1.55;color:#6b4200;background:#fff7e6;border:1px solid #f0c674;border-radius:10px;padding:10px 14px}'
    + '.pa-warn a{color:inherit;font-weight:700}'
    + '.pa-ios{font-size:13.5px;line-height:1.55;color:#6b4200;background:#fff7e6;border:1px solid #f0c674;border-radius:10px;padding:10px 12px;margin:10px 0}'
    + '[hidden].pa-x,.pa-x[hidden]{display:none!important}'
    + 'html[data-theme="dark"] .pa-panel{background:#1f1416;border-color:#5b2a2a;color:#eef2fb}'
    + 'html[data-theme="dark"] .pa-panel h2{color:#fca5a5}html[data-theme="dark"] .pa-lead{color:#c9d2e0}'
    + 'html[data-theme="dark"] .pa-card{background:#1a2535;border-color:#3a2d36}html[data-theme="dark"] .pa-card h3{color:#eef2fb}'
    + 'html[data-theme="dark"] .pa-card p,html[data-theme="dark"] .pa-card li{color:#c9d2e0}html[data-theme="dark"] .pa-note{color:#b4bfcf!important}'
    + 'html[data-theme="dark"] .pa-btn.pa-ghost{color:#fca5a5;border-color:#f87171}'
    + 'html[data-theme="dark"] .pa-warn,html[data-theme="dark"] .pa-ios{color:#fde68a;background:#2a1d05;border-color:#6b4f12}'
    + (inApp ? '#eqc-save{display:none!important}' : '')
    + '.pa-tab.pa-acad{transform:translateY(66px)}'
    + '@media (max-width:640px){.pa-tab.pa-acad{transform:none;bottom:calc(212px + env(safe-area-inset-bottom,0px))}html.sch-app .pa-tab.pa-acad{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px))}}'
    + '.pa-open-app{display:inline-flex;align-items:center;font:700 14px/1 Inter,system-ui,sans-serif;color:#fff!important;background:#991b1b;border-radius:9px;padding:11px 15px;margin:2px 8px 8px 0;text-decoration:none!important}'
    + '.pa-open-app:hover{background:#7f1d1d}'
    + 'html.pa-offline body::after{content:"Offline · Paratus is showing saved pages";position:fixed;left:50%;top:10px;transform:translateX(-50%);z-index:9999;'
    + 'font:600 12.5px/1 Inter,system-ui,sans-serif;color:#fff;background:#7a4b00;padding:8px 14px;border-radius:20px;box-shadow:0 4px 14px rgba(0,0,0,.18);pointer-events:none}'
    + 'html.pa-standalone body{padding-bottom:calc(76px + env(safe-area-inset-bottom,0px))}'
    + 'html.pa-standalone .float-controls,html.pa-standalone .float-controls-left,html.pa-standalone .rcn-fab,html.pa-standalone .sc-fab{bottom:calc(76px + env(safe-area-inset-bottom,0px))!important}'
    + 'html.pa-standalone .scroll-top-btn{bottom:calc(132px + env(safe-area-inset-bottom,0px))!important}'
    + '.pa-appbar{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:9998;display:flex;gap:2px;padding:5px;border-radius:999px;background:#7f1d1d;box-shadow:0 6px 22px rgba(15,30,51,.28)}'
    + '.pa-appbar a,.pa-appbar button{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 12px;border:0;border-radius:999px;background:transparent;color:#fff!important;'
    + 'font:600 13px/1 Inter,system-ui,sans-serif;text-decoration:none!important;cursor:pointer;white-space:nowrap;-webkit-tap-highlight-color:transparent}'
    + '.pa-appbar a:active,.pa-appbar button:active,.pa-appbar [aria-current="page"]{background:rgba(255,255,255,.18)}'
    + '.pa-appbar svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}'
    + '@media (max-width:420px){.pa-appbar a,.pa-appbar button{padding:0 9px;font-size:12px}.pa-appbar .pa-lbl-print{display:none}}'
    + '@media print{.pa-appbar,.pa-panel,.pa-warn,.pa-ios{display:none!important}html.pa-offline body::after{display:none}}';
  var st = document.createElement('style'); st.id = 'paratus-style'; st.textContent = css; document.head.appendChild(st);

  function net() { document.documentElement.classList.toggle('pa-offline', navigator.onLine === false && !display && inApp); }
  window.addEventListener('online', net); window.addEventListener('offline', net); net();
  function rec() { try { var r = JSON.parse(localStorage.getItem(KEY) || 'null'); return r && r.v === 1 ? r : null; } catch (e) { return null; } }
  function setRec(r) { try { localStorage.setItem(KEY, JSON.stringify(r)); } catch (e) {} }
  function num(n) { return Number(n).toLocaleString('en-US'); }
  function fmtDate(ms) { try { return new Date(ms).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }); } catch (e) { return ''; } }

  var I = {
    back: '<polyline points="15 18 9 12 15 6"/>',
    home: '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
    cards: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 10h6M7 14h10"/>',
    prac: '<polyline points="2 12 6 12 9 5 13 19 16 12 22 12"/>',
    print: '<polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>'
  };
  function svg(k) { return '<svg viewBox="0 0 24 24" aria-hidden="true">' + I[k] + '</svg>'; }

  function init() {
    if (display) return;   // the second display stays a clean full-screen monitor
    if (!inApp) { panel(); return; }
    var here = location.pathname.replace(/\.html$/, '');
    if (standalone() && !document.querySelector('.pa-appbar')) {
      document.documentElement.classList.add('pa-standalone');
      var bar = document.createElement('nav'); bar.className = 'pa-appbar'; bar.setAttribute('aria-label', 'Paratus navigation');
      bar.innerHTML =
        '<button type="button" data-ab="back" aria-label="Back">' + svg('back') + '<span>Back</span></button>'
        + '<a href="' + HOME + '"' + (onHome() ? ' aria-current="page"' : '') + '>' + svg('home') + '<span>Home</span></a>'
        + '<a href="/paratus/emergency-cards"' + (here === '/paratus/emergency-cards' ? ' aria-current="page"' : '') + '>' + svg('cards') + '<span>Cards</span></a>'
        + '<a href="/paratus/resuscitation-lab-practice"' + (here === '/paratus/resuscitation-lab-practice' ? ' aria-current="page"' : '') + '>' + svg('prac') + '<span>Practice</span></a>'
        + '<button type="button" data-ab="print" aria-label="Print">' + svg('print') + '<span class="pa-lbl-print">Print</span></button>';
      document.body.appendChild(bar);
      bar.querySelector('[data-ab="back"]').addEventListener('click', function () { if (history.length > 1) history.back(); else location.href = HOME; });
      bar.querySelector('[data-ab="print"]').addEventListener('click', function () { window.print(); });
    }
    // the cards page explained Schola saving; in Paratus every card is saved with the app
    var es = document.getElementById('eqc-status');
    if (es) es.textContent = 'In Paratus these cards are saved together with the rest of the app: download Paratus once on its home page, and they open here with no signal.';
    // Megacode Practice Lab in the iPhone / iPad Home Screen app: it cannot open a second window
    var od = document.querySelector('a[href="?display=1"]');
    if (od && standalone() && ios()) {
      var n = document.createElement('p'); n.className = 'pa-ios';
      n.innerHTML = '<b>Second display on iPhone or iPad:</b> the Home Screen app opens one window only, so <b>Open display</b> goes to Safari, which keeps its own storage and does not follow this app. '
        + 'Use the <b>Live view</b> below on this device, or run both the controls and the display in Safari tabs (open renalcarematters.com/paratus/resuscitation-lab-practice there). On a laptop or an Android device, Open display opens a second Paratus window that follows these controls.';
      od.parentNode.insertBefore(n, od.nextSibling);
    }
    panel();
  }

  function panel() {
    var box = document.createElement('aside'); box.className = 'pa-panel no-print'; box.id = 'paratus';
    box.setAttribute('aria-label', 'Paratus: install and download'); box.setAttribute('aria-hidden', 'true');
    box.innerHTML =
      '<h2><img src="/images/app/paratus-192.png" alt="">Paratus: ready without signal<button type="button" class="pa-x-close" aria-label="Close">&times;</button></h2>'
      + '<p class="pa-lead">Paratus (Latin for &ldquo;ready&rdquo;) keeps the Emergency Quick Cards, the Dialysis Team Resuscitation Lab, Disaster Preparedness, the Megacode Practice Lab and the Disaster Drills on this device, for a code, a typhoon or a power cut with no signal. It is separate from Schola, the Academy app.</p>'
      + '<div class="pa-grid">'
      + '<div class="pa-card"><h3>1. Install</h3><p data-pa="hint">Adds a Paratus icon to your home screen or desktop. It opens full screen.</p>'
      + (inApp ? '' : '<a class="pa-open-app" href="/paratus/">Open Paratus</a>')
      + '<button type="button" class="pa-btn pa-x" data-pa="install" hidden>Install Paratus</button>'
      + '<ol class="pa-x" data-pa="ios" hidden><li>Tap the <b>Share</b> button in Safari.</li><li>Choose <b>Add to Home Screen</b>, then <b>Add</b>.</li><li>Open Paratus from the Home Screen and download it there (the Home Screen app and Safari keep separate storage).</li></ol></div>'
      + '<div class="pa-card pa-x" data-pa="off"><h3>2. Download for use without signal</h3><p>Everything in Paratus, in one download, so nothing is missing when it matters.</p>'
      + '<button type="button" class="pa-btn" data-pa="dl">Download Paratus</button><button type="button" class="pa-btn pa-ghost pa-x" data-pa="rm" hidden>Remove download</button>'
      + '<progress class="pa-x" data-pa="bar" hidden></progress><p class="pa-note" data-pa="status" aria-live="polite"></p></div>'
      + '</div>';
    var scrim = document.createElement('div'); scrim.className = 'pa-scrim no-print';
    var tab = document.createElement('button'); tab.type = 'button'; tab.className = 'pa-tab no-print' + (inApp ? '' : ' pa-acad');
    tab.setAttribute('aria-label', 'Open Paratus: install the app and download it for use without signal'); tab.setAttribute('aria-controls', 'paratus'); tab.setAttribute('aria-expanded', 'false');
    tab.innerHTML = '<img src="/images/app/paratus-192.png" alt="" width="26" height="26"><span>Paratus</span>';
    document.body.appendChild(scrim); document.body.appendChild(box); document.body.appendChild(tab);
    function openP() { box.classList.add('pa-open'); scrim.classList.add('pa-open'); box.setAttribute('aria-hidden', 'false'); tab.setAttribute('aria-expanded', 'true'); var x = box.querySelector('.pa-x-close'); if (x) x.focus(); }
    function closeP() { box.classList.remove('pa-open'); scrim.classList.remove('pa-open'); box.setAttribute('aria-hidden', 'true'); tab.setAttribute('aria-expanded', 'false');
      if (location.hash === '#paratus') try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {} }
    tab.addEventListener('click', function () { box.classList.contains('pa-open') ? closeP() : openP(); });
    box.querySelector('.pa-x-close').addEventListener('click', function () { closeP(); tab.focus(); });
    scrim.addEventListener('click', closeP);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && box.classList.contains('pa-open')) { closeP(); tab.focus(); } });
    document.addEventListener('click', function (e) {   // links to #paratus (the Emergency drawer's Get Paratus) open this drawer
      var a = e.target.closest && e.target.closest('a[href$="#paratus"]'); if (!a) return;
      var u = new URL(a.getAttribute('href'), location.href); if (u.pathname.indexOf('/paratus') !== 0) return;
      e.preventDefault(); var erd = document.querySelector('.erd.erd-open .erd-x'); if (erd) erd.click(); openP();
    });
    window.addEventListener('hashchange', function () { if (location.hash === '#paratus') openP(); });
    if (location.hash === '#paratus') setTimeout(openP, 300);
    function q(n) { return box.querySelector('[data-pa="' + n + '"]'); }
    var deferred = null;
    function showInstall() {
      var hint = q('hint'), btn = q('install'), steps = q('ios');
      if (!inApp) {   // an Academy page would install Schola: Paratus installs from its own pages
        btn.hidden = true; steps.hidden = true;
        hint.textContent = ios() ? 'Open Paratus in Safari, then add it to your Home Screen from there (Share, then Add to Home Screen) and download it inside the Home Screen app: Safari, Schola and Paratus each keep their own storage.'
          : 'Open Paratus, then install it from your browser menu (Install app, or Add to Home screen). You can also download it below to use these pages without signal in this browser.';
        return;
      }
      if (standalone()) { btn.hidden = true; steps.hidden = true; hint.textContent = 'You are using the installed Paratus app.'; return; }
      if (ios()) { btn.hidden = true; steps.hidden = false; hint.textContent = 'On iPhone or iPad, add Paratus to your Home Screen:'; return; }
      if (deferred) { btn.hidden = false; hint.textContent = 'Adds a Paratus icon to your home screen or desktop. It opens full screen and works offline.'; }
      else hint.textContent = 'Use your browser menu: Install app, or Add to Home screen. On a computer, look for the install icon in the address bar.';
    }
    if (inApp) window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferred = e; showInstall(); });
    window.addEventListener('appinstalled', function () { deferred = null; showInstall(); });
    showInstall();
    q('install').addEventListener('click', function () { if (!deferred) return; deferred.prompt(); (deferred.userChoice || Promise.resolve()).then(function () { deferred = null; showInstall(); }); });
    if (standalone() && !(rec() && rec().done)) {
      var nb = document.createElement('div'); nb.className = 'pa-warn';
      nb.innerHTML = '<strong>Paratus is not saved on this device yet.</strong> Download it once while you have signal so every page works without it. <a href="#paratus">Download Paratus</a>';
      var mn = document.querySelector('main'); if (onHome() && mn) mn.insertBefore(nb, mn.firstChild);
    }
    var dl = q('dl'), rm = q('rm'), stx = q('status'), bar = q('bar');
    if (!('caches' in window) || !('serviceWorker' in navigator)) { q('off').hidden = true; return; }
    var busy = false, cur = null, LABEL = 'Download Paratus';
    function manifest() { return fetch(MAN, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
    function status() {
      var r = rec(); dl.disabled = busy; rm.disabled = busy; dl.textContent = LABEL;
      if (!r) { stx.textContent = 'Not downloaded on this device yet' + (cur ? ' (about ' + num(Math.max(1, Math.round(cur.all_bytes / 1e6))) + ' MB).' : '.'); rm.hidden = true; return; }
      rm.hidden = false;
      var msg = r.done ? 'Paratus is saved on this device (' + num(r.n) + ' files, ' + fmtDate(r.at) + ').'
        : 'Download interrupted at ' + num(r.n) + ' of ' + num(r.total) + ' files. Tap the button again to resume.';
      if (!r.done) dl.textContent = 'Resume download';
      else if (cur && cur.h !== r.h) { msg += ' Updates are available.'; dl.textContent = 'Update Paratus'; }
      else if (cur) dl.textContent = 'Up to date · check again';
      stx.textContent = msg;
    }
    status();
    if (navigator.onLine !== false) manifest().then(function (m) {
      cur = m; if (!busy) status();
      var r0 = rec(); if (r0 && r0.done && r0.h && m.h !== r0.h && !busy) run();   // keep a saved copy current on its own
    }, function () {});
    function run() {
      if (busy) return;
      if (navigator.onLine === false) { stx.textContent = 'You are offline. Connect to the internet to download.'; return; }
      busy = true; status(); bar.hidden = false; bar.value = 0; stx.textContent = 'Checking what needs downloading…';
      var lock = null; try { if (navigator.wakeLock) navigator.wakeLock.request('screen').then(function (l) { lock = l; }, function () {}); } catch (e) {}
      if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
      var m, c, want = {}, have = {}, todo = [], ok = 0, failed = 0, total = 0;
      manifest().then(function (x) {
        m = x; cur = x; m.files.forEach(function (p) { want[location.origin + p[0]] = p; });
        return caches.open(SAVED);
      }).then(function (cache) { c = cache; return c.keys(); }).then(function (keys) {
        return Promise.all(keys.map(function (k) {
          if (!want[k.url]) return k.url === location.origin + MAN ? null : c.delete(k);
          return c.match(k).then(function (res) { have[k.url] = res && res.headers.get('X-RCM-Hash'); });
        }));
      }).then(function () {
        Object.keys(want).forEach(function (u) { if (have[u] !== want[u][1]) todo.push(u); });
        total = Object.keys(want).length; ok = total - todo.length; bar.max = total; bar.value = ok;
        var i = 0;
        function save() { setRec({ v: 1, n: ok, total: total, at: Date.now(), h: m.h, done: false }); }
        function next() {
          if (i >= todo.length) return Promise.resolve();
          var u = todo[i++], p = want[u];
          return fetch(u, { credentials: 'same-origin', cache: 'no-cache' }).then(function (res) {
            if (!res.ok) throw new Error(res.status);
            var ct = res.headers.get('content-type') || 'application/octet-stream';
            return res.blob().then(function (bl) { return c.put(u, new Response(bl, { headers: { 'Content-Type': ct, 'X-RCM-Hash': p[1] } })); });
          }).then(function () { ok++; if (ok % 25 === 0) save(); }, function () { failed++; })
            .then(function () { bar.value = ok; stx.textContent = 'Saving ' + num(ok) + ' of ' + num(total) + ' files… keep this page open.'; tab.querySelector('span').textContent = 'Saving ' + Math.floor(ok * 100 / total) + '%'; return next(); });
        }
        save();
        return Promise.all([next(), next(), next(), next(), next(), next()]).then(function () {
          return c.put(location.origin + MAN, new Response(JSON.stringify({ small: m.small || {} }), { headers: { 'Content-Type': 'application/json' } }));
        });
      }).then(function () {
        setRec({ v: 1, n: ok, total: total, at: Date.now(), h: failed ? '' : m.h, done: !failed });
        try { navigator.serviceWorker.controller && navigator.serviceWorker.controller.postMessage('paratus-refresh'); } catch (e) {}
        busy = false; bar.hidden = true; status(); tab.querySelector('span').textContent = 'Paratus';
        if (failed) stx.textContent = num(failed) + ' files could not be saved. Tap the button again on a better connection to finish.';
      }).catch(function (err) {
        busy = false; bar.hidden = true; status(); tab.querySelector('span').textContent = 'Paratus';
        stx.textContent = (err && err.msg) || 'The download stopped. Check your connection and tap the button again; files already saved are kept.';
      }).then(function () { try { if (lock) lock.release(); } catch (e) {} });
    }
    dl.addEventListener('click', run);
    rm.addEventListener('click', function () { if (busy) return; caches.delete(SAVED).then(function () { try { localStorage.removeItem(KEY); } catch (e) {} status(); }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
