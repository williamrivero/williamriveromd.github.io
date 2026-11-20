/* Calculo: the calculators as an installable app (renalcarematters.com).
   Loaded on every calculator page and the calculators index by build_calc_app.py.
   - registers the service worker (guides/calc-sw.js, scope /guides/calc)
   - in the installed app: bottom bar (Back · All calculators · Search · Print) in place of the page pill
   - calculators index: install steps and the one complete offline download (#calc-app panel, #calc-app-cta) */
(function () {
  'use strict';
  var SAVED = 'rcm-calc-saved', KEY = 'wgmr-calc-offline', MAN = '/guides/calc-offline-manifest.json';
  var INDEX = '/guides/calculators';

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('/guides/calc-sw.js', { scope: '/guides/calc' }).catch(function () {});
    });
  }

  function standalone() { return (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true; }
  function ios() { return /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1); }
  function onIndex() { return /^\/guides\/calculators(\.html)?$/.test(location.pathname); }

  var css = ''
    + '.ca-hidden,[data-ca][hidden],.ca-cta[hidden]{display:none!important}'
    + '.ca-cta{display:inline-flex;align-items:center;gap:12px;margin:14px 0 4px;padding:11px 16px 11px 14px;border-radius:14px;color:#fff!important;text-decoration:none!important;'
    + 'background:linear-gradient(135deg,#4338ca 0%,#312e81 100%);box-shadow:0 6px 18px rgba(49,46,129,.32),inset 0 1px 0 rgba(255,255,255,.14);transition:transform .15s,box-shadow .15s}'
    + '.ca-cta:hover{transform:translateY(-1px);box-shadow:0 10px 24px rgba(49,46,129,.4)}'
    + '.ca-cta:focus-visible{outline:3px solid #b8860b;outline-offset:3px}'
    + '.ca-cta>svg:first-child{flex:none;width:34px;height:34px;padding:6px;border-radius:10px;background:rgba(255,255,255,.16);fill:none;stroke:#fff;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}'
    + '.ca-cta-t{display:flex;flex-direction:column;gap:2px;line-height:1.2}'
    + '.ca-cta-t strong{font:700 15px/1.2 Inter,system-ui,sans-serif;color:#fff}'
    + '.ca-cta-t small{font:500 12.5px/1.3 Manrope,system-ui,sans-serif;color:#e0e7ff}'
    + '.ca-cta-arr{flex:none;width:18px;height:18px;fill:none;stroke:#fff;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;opacity:.85}'
    + '.ca-panel{margin:34px 0 22px;padding:22px;border:1px solid var(--border,#dfe6f0);border-radius:14px;background:var(--white,#fff)}'
    + '.ca-panel h2{font:700 20px/1.3 Inter,system-ui,sans-serif;margin:0 0 14px;color:#312e81}'
    + '.ca-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}'
    + '.ca-card{border:1px solid var(--border,#dfe6f0);border-radius:12px;padding:16px 18px;background:var(--bg,#f9fafb)}'
    + '.ca-card h3{font:700 15.5px/1.3 Inter,system-ui,sans-serif;margin:0 0 8px;color:var(--text,#1e2a38)}'
    + '.ca-card p,.ca-card li{font-size:14px;line-height:1.6;color:var(--text-mid,#34455f);text-align:left}'
    + '.ca-card p{margin:0 0 10px}'
    + '.ca-card ol{margin:4px 0 6px 20px;padding:0}.ca-card li{margin:0 0 4px}'
    + '.ca-btn{display:inline-flex;align-items:center;font:600 13.5px/1 Inter,system-ui,sans-serif;color:#fff;background:#3730a3;border:1px solid #3730a3;border-radius:8px;padding:10px 14px;margin:2px 8px 8px 0;cursor:pointer}'
    + '.ca-btn:hover{background:#312e81}.ca-btn[disabled]{opacity:.6;cursor:progress}'
    + '.ca-btn.ca-ghost{color:#3730a3;background:transparent;border-color:rgba(55,48,163,.45)}'
    + '.ca-meta{display:block;font-size:13px;color:var(--text-muted,#5b6b82);margin:0 0 8px}'
    + '.ca-note{font-size:13px;color:var(--text-muted,#5b6b82);line-height:1.6}'
    + '.ca-warn{font-size:13.5px;line-height:1.55;color:#6b4200;background:#fff7e6;border:1px solid #f0c674;border-radius:10px;padding:10px 12px;margin:6px 0 10px}'
    + '.ca-warn a{color:inherit;font-weight:700}'
    + '.ca-card progress{width:100%;height:8px;margin:2px 0 10px;accent-color:#3730a3}'
    + 'html[data-theme="dark"] .ca-panel{background:#1a2535;border-color:#2c3a52}'
    + 'html[data-theme="dark"] .ca-panel h2{color:#c7d2fe}'
    + 'html[data-theme="dark"] .ca-card{background:#141e2c;border-color:#2c3a52}'
    + 'html[data-theme="dark"] .ca-card h3{color:#eef2fb}'
    + 'html[data-theme="dark"] .ca-card p,html[data-theme="dark"] .ca-card li{color:#c9d2e0}'
    + 'html[data-theme="dark"] .ca-meta,html[data-theme="dark"] .ca-note{color:#b4bfcf}'
    + 'html[data-theme="dark"] .ca-btn.ca-ghost{color:#c7d2fe;border-color:#6366f1}'
    + 'html[data-theme="dark"] .ca-warn{color:#fde68a;background:#2a1d05;border-color:#6b4f12}'
    + 'html[data-theme="dark"] .ca-cta{background:linear-gradient(135deg,#3730a3 0%,#1e1b4b 100%)}'
    + 'html.ca-offline body::after{content:"Offline · showing saved calculators";position:fixed;left:50%;top:10px;transform:translateX(-50%);z-index:9999;'
    + 'font:600 12.5px/1 Inter,system-ui,sans-serif;color:#fff;background:#7a4b00;padding:8px 14px;border-radius:20px;box-shadow:0 4px 14px rgba(0,0,0,.18);pointer-events:none}'
    + 'html.ca-standalone .calc-nav-pill{display:none!important}'
    + 'html.ca-standalone #desktopToggle,html.ca-standalone .float-controls-left,html.ca-standalone [onclick="toggleDesktop()"]{display:none!important}'
    + 'html.ca-standalone body{padding-bottom:calc(76px + env(safe-area-inset-bottom,0px))}'
    + 'html.ca-standalone .float-controls,html.ca-standalone .float-controls-left,html.ca-standalone .sc-fab{bottom:calc(76px + env(safe-area-inset-bottom,0px))!important}'
    + 'html.ca-standalone .scroll-top-btn{bottom:calc(132px + env(safe-area-inset-bottom,0px))!important}'
    + '.ca-appbar{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:9998;display:flex;gap:2px;padding:5px;border-radius:999px;background:#312e81;box-shadow:0 6px 22px rgba(15,30,51,.28)}'
    + '.ca-appbar a,.ca-appbar button{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 13px;border:0;border-radius:999px;background:transparent;color:#fff!important;'
    + 'font:600 13px/1 Inter,system-ui,sans-serif;text-decoration:none!important;cursor:pointer;white-space:nowrap;-webkit-tap-highlight-color:transparent}'
    + '.ca-appbar a:active,.ca-appbar button:active,.ca-appbar [aria-current="page"]{background:rgba(255,255,255,.16)}'
    + '.ca-appbar svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}'
    + '@media (max-width:400px){.ca-appbar a,.ca-appbar button{padding:0 10px;font-size:12px}.ca-appbar .ca-lbl-print{display:none}}'
    + '@media print{.ca-appbar,.ca-panel,.ca-cta{display:none!important}html.ca-offline body::after{display:none}}';
  var st = document.createElement('style'); st.id = 'calc-app-style'; st.textContent = css; document.head.appendChild(st);

  function net() { document.documentElement.classList.toggle('ca-offline', navigator.onLine === false); }
  window.addEventListener('online', net); window.addEventListener('offline', net); net();

  function rec() { try { var r = JSON.parse(localStorage.getItem(KEY) || 'null'); return r && r.v === 1 ? r : null; } catch (e) { return null; } }
  function setRec(r) { try { localStorage.setItem(KEY, JSON.stringify(r)); } catch (e) {} }

  function focusSearch() {
    var sq = document.getElementById('cf-search');
    if (sq) { sq.scrollIntoView({ block: 'center' }); try { sq.focus(); } catch (e) {} return true; }
    return false;
  }

  function init() {
    /* Installed app: one bottom bar instead of the browser toolbar and the page pill */
    if (standalone() && !document.querySelector('.ca-appbar')) {
      document.documentElement.classList.add('ca-standalone');
      var bar = document.createElement('nav'); bar.className = 'ca-appbar'; bar.setAttribute('aria-label', 'Calculo navigation');
      bar.innerHTML =
        '<button type="button" data-ab="back" aria-label="Back"><svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg><span>Back</span></button>'
        + '<a href="' + INDEX + '" data-ab="home"' + (onIndex() ? ' aria-current="page"' : '') + '><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M16 11h0M8 15h2M12 15h2M8 18h2M12 18h2"/></svg><span>All calculators</span></a>'
        + '<a href="' + INDEX + '#search" data-ab="search" aria-label="Search calculators"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg><span>Search</span></a>'
        + (onIndex() ? '' : '<button type="button" data-ab="print" aria-label="Print"><svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg><span class="ca-lbl-print">Print</span></button>');
      document.body.appendChild(bar);
      bar.querySelector('[data-ab="back"]').addEventListener('click', function () { if (history.length > 1) history.back(); else location.href = INDEX; });
      bar.querySelector('[data-ab="search"]').addEventListener('click', function (e) { if (focusSearch()) e.preventDefault(); });
      var pb = bar.querySelector('[data-ab="print"]'); if (pb) pb.addEventListener('click', function () { window.print(); });
    }
    if (location.hash === '#search') focusSearch();

    /* Calculators index: hero button + panel */
    var cta = document.getElementById('calc-app-cta');
    var box = document.getElementById('calc-app');
    if (cta && standalone()) {
      var r0 = rec();
      if (r0 && r0.done) cta.hidden = true;
      else { cta.querySelector('strong').textContent = 'Set up offline use'; cta.querySelector('small').textContent = 'Download every calculator once'; }
    }
    if (!box) return;
    function q(n) { return box.querySelector('[data-ca="' + n + '"]'); }
    var deferred = null;
    function showInstall() {
      var hint = q('hint'), btn = q('install'), steps = q('iossteps'), note = q('iosnote');
      if (standalone()) { btn.hidden = true; steps.hidden = true; note.hidden = true; hint.textContent = 'You are using the installed Calculo app.'; return; }
      if (ios()) { btn.hidden = true; steps.hidden = false; note.hidden = false; hint.textContent = 'On iPhone or iPad, add Calculo to your Home Screen:'; return; }
      if (deferred) { btn.hidden = false; hint.textContent = 'Adds a Calculo icon to your home screen or desktop. It opens full screen and works offline.'; }
    }
    window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferred = e; showInstall(); });
    window.addEventListener('appinstalled', function () { deferred = null; showInstall(); });
    showInstall();
    q('install').addEventListener('click', function () {
      if (!deferred) return; deferred.prompt();
      (deferred.userChoice || Promise.resolve()).then(function () { deferred = null; showInstall(); });
    });
    if (standalone()) {
      var r1 = rec();
      if (!r1 || !r1.done) {
        var main = document.querySelector('main');
        if (main) {
          var nb = document.createElement('div'); nb.className = 'ca-warn';
          nb.innerHTML = '<strong>Offline use is not set up yet.</strong> Download every calculator once so they all work without signal. <a href="#calc-app">Set up offline use</a>';
          main.insertBefore(nb, main.firstChild);
        }
      }
    }

    var dl = q('dl'), rm = q('rm'), stx = q('status'), bar2 = q('bar');
    if (!('caches' in window) || !('serviceWorker' in navigator)) { q('off').hidden = true; return; }
    var busy = false, cur = null, LABEL = 'Download every calculator';
    function fmtDate(ms) { try { return new Date(ms).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }); } catch (e) { return ''; } }
    function num(n) { return Number(n).toLocaleString('en-US'); }
    function manifest() { return fetch(MAN, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
    function status() {
      var r = rec(); dl.disabled = busy; rm.disabled = busy; dl.textContent = LABEL;
      if (!r) { stx.textContent = 'Not downloaded on this device yet.'; rm.hidden = true; return; }
      rm.hidden = false;
      var msg = r.done ? 'Every calculator is saved on this device (' + num(r.n) + ' files, ' + fmtDate(r.at) + ').'
        : 'Download interrupted at ' + num(r.n) + ' of ' + num(r.total) + ' files. Tap the button again to resume.';
      if (!r.done) dl.textContent = 'Resume download';
      else if (cur && cur.h !== r.h) { msg += ' Updates are available.'; dl.textContent = 'Update Calculo'; }
      else if (cur) dl.textContent = 'Up to date · check again';
      stx.textContent = msg;
      if (navigator.storage && navigator.storage.estimate) navigator.storage.estimate().then(function (x) {
        if (x && x.usage && !busy) stx.textContent = msg + ' This site uses about ' + num(Math.max(1, Math.round(x.usage / 1e6))) + ' MB on this device.';
      }).catch(function () {});
    }
    status();
    // Saved calculators update themselves (Nov 18 2026): when the set on this device is complete but the site has
    // changed since, fetch just the changed files in the background, so the app never keeps showing old pages.
    if (navigator.onLine !== false) manifest().then(function (m) {
      cur = m; if (!busy) status();
      var r0 = rec(); if (r0 && r0.done && r0.h && m.h !== r0.h && !busy) run();
    }, function () {});

    function run() {
      if (busy) return;
      if (navigator.onLine === false) { stx.textContent = 'You are offline. Connect to the internet to download.'; return; }
      busy = true; status(); bar2.hidden = false; bar2.value = 0; stx.textContent = 'Checking what needs downloading…';
      var lock = null; try { if (navigator.wakeLock) navigator.wakeLock.request('screen').then(function (l) { lock = l; }, function () {}); } catch (e) {}
      if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
      var m, c, want = {}, have = {}, todo = [], ok = 0, failed = 0, total = 0;
      manifest().then(function (x) {
        m = x; cur = x; m.files.forEach(function (p) { want[location.origin + p[0]] = p; });
        return caches.open(SAVED);
      }).then(function (cache) { c = cache; return c.keys(); }).then(function (keys) {
        return Promise.all(keys.map(function (k) {
          if (!want[k.url]) return c.delete(k);
          return c.match(k).then(function (res) { have[k.url] = res && res.headers.get('X-RCM-Hash'); });
        }));
      }).then(function () {
        Object.keys(want).forEach(function (u) { if (have[u] !== want[u][1]) todo.push(u); });
        total = Object.keys(want).length; ok = total - todo.length;
        var need = todo.reduce(function (a, u) { return a + want[u][2]; }, 0);
        var room = (navigator.storage && navigator.storage.estimate) ? navigator.storage.estimate() : Promise.resolve(null);
        return room.then(function (e) {
          if (e && e.quota && e.quota - e.usage < need * 1.15) throw { msg: 'Not enough free storage on this device (about ' + num(Math.ceil(need / 1e6)) + ' MB more is needed). Free some space and tap the button again.' };
          bar2.max = total; bar2.value = ok;
          if (!todo.length) return;
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
              .then(function () { bar2.value = ok; stx.textContent = 'Saving ' + num(ok) + ' of ' + num(total) + ' files… keep this page open.'; return next(); });
          }
          save();
          return Promise.all([next(), next(), next(), next(), next(), next()]);
        });
      }).then(function () {
        setRec({ v: 1, n: ok, total: total, at: Date.now(), h: failed ? '' : m.h, done: !failed });
        busy = false; bar2.hidden = true; status();
        if (failed) stx.textContent = num(failed) + ' files could not be saved. Tap the button again on a better connection to finish.';
      }).catch(function (err) {
        busy = false; bar2.hidden = true; status();
        stx.textContent = (err && err.msg) || 'The download stopped. Check your connection and tap the button again; files already saved are kept.';
      }).then(function () { try { if (lock) lock.release(); } catch (e) {} });
    }
    dl.addEventListener('click', run);
    rm.addEventListener('click', function () { if (busy) return; caches.delete(SAVED).then(function () { try { localStorage.removeItem(KEY); } catch (e) {} status(); }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
