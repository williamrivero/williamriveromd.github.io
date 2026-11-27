/* Schola: the Renal Care Academy as an installable, offline web app (Nov 2026).
   Registers the worker (academy/schola-sw.js), draws the Schola panel on the Academy landing page (install,
   Download all, save / update / remove each track) and a "Save this track" card on every track hub, saves files
   into the 'schola-saved' cache from academy/schola-offline.json (each copy tagged with its content hash, so
   updates and resumed downloads fetch only what is missing or changed), and adds a bottom app bar (Back, Academy,
   Track) in the installed app, which has no browser toolbar.

   Source file: edit assets/schola.js, then run tools/academy/apply_notes.py (fingerprints it as
   assets/schola.<hash>.js and points every academy page at it). Never link the unhashed file. */
(function () {
  'use strict';
  if (window.__schola) return;
  window.__schola = true;

  var SW = '/academy/schola-sw.js', MAN = '/academy/schola-offline.json', CACHE = 'schola-saved', STATE = 'schola-state';
  var standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
  var ios = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var hasCache = 'caches' in window;

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register(SW, { scope: '/academy/' }).catch(function () {});
  }

  var path = location.pathname.replace(/\.html$/, '');
  if (path === '/academy' || path === '/academy/index') path = '/academy/';
  var isLanding = path === '/academy/';
  var file = path.split('/').pop();
  var isModule = /-\d{2}-/.test(file);
  var isHub = !isLanding && !isModule && !/final-exam|trainer/.test(file);

  /* ── helpers ──────────────────────────────────────────────────────────── */
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function mb(b) { return b >= 1e9 ? (b / 1e9).toFixed(1) + ' GB' : b >= 1e7 ? Math.round(b / 1e6) + ' MB' : (b / 1e6).toFixed(1) + ' MB'; }
  function date(s) { try { return new Date(s).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }); } catch (e) { return ''; } }
  function state() { try { return JSON.parse(localStorage.getItem(STATE) || '{}') || {}; } catch (e) { return {}; } }
  function setState(s) { try { localStorage.setItem(STATE, JSON.stringify(s)); } catch (e) {} }
  function savedTracks() { return state().tracks || {}; }

  var man = null;
  function getManifest() {
    if (man) return Promise.resolve(man);
    return fetch(MAN, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error('manifest'); return r.json(); })
      .catch(function () {
        return hasCache ? caches.open(CACHE).then(function (c) { return c.match(MAN); }).then(function (r) { return r ? r.json() : null; }) : null;
      })
      .then(function (m) { man = m; return m; });
  }
  function track(id) { for (var i = 0; i < man.tracks.length; i++) if (man.tracks[i].id === id) return man.tracks[i]; return null; }
  function trackOfPage() {
    var idx = -1;
    for (var i = 0; i < man.files.length; i++) if (man.files[i][0] === path) { idx = i; break; }
    if (idx < 0) return null;
    for (var j = 0; j < man.tracks.length; j++) if (man.tracks[j].files.indexOf(idx) >= 0) return man.tracks[j];
    return null;
  }
  function filesFor(ids) {
    var seen = {}, out = [];
    function add(i) { if (!seen[i]) { seen[i] = 1; out.push(man.files[i]); } }
    man.shared.forEach(add);
    ids.forEach(function (id) { var t = track(id); if (t) t.files.forEach(add); });
    return out;
  }
  function updateSize(t) {
    var s = savedTracks()[t.id];
    return s && s.h !== t.h;
  }

  /* ── downloading ──────────────────────────────────────────────────────── */
  var busy = false;
  function download(ids, progress) {
    if (busy) return Promise.reject(new Error('busy'));
    busy = true;
    if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
    var list = filesFor(ids), cache;
    return caches.open(CACHE).then(function (c) {
      cache = c;
      return Promise.all(list.map(function (f) {
        return c.match(f[0]).then(function (r) { return r && r.headers.get('X-RCM-Hash') === f[1] ? null : f; });
      }));
    }).then(function (todo) {
      todo = todo.filter(Boolean);
      var total = todo.reduce(function (a, f) { return a + f[2]; }, 0), done = 0, n = 0, errors = 0, next = 0;
      progress(0, total, 0, todo.length);
      function worker() {
        if (next >= todo.length) return Promise.resolve();
        var f = todo[next++];
        return fetch(f[0], { cache: 'no-cache', credentials: 'same-origin' }).then(function (r) {
          if (!r.ok) throw new Error(r.status);
          var type = r.headers.get('Content-Type') || '';
          return r.blob().then(function (b) {
            return cache.put(f[0], new Response(b, { headers: { 'Content-Type': type, 'X-RCM-Hash': f[1] } }));
          });
        }).catch(function () { errors++; }).then(function () {
          done += f[2]; n++;
          progress(done, total, n, todo.length);
          return worker();
        });
      }
      var pool = [];
      for (var i = 0; i < 6; i++) pool.push(worker());
      return Promise.all(pool).then(function () {
        return fetch(MAN, { cache: 'no-cache' }).then(function (r) { return r.ok ? cache.put(MAN, r) : null; }).catch(function () {});
      }).then(function () {
        if (navigator.serviceWorker && navigator.serviceWorker.controller) navigator.serviceWorker.controller.postMessage('schola-refresh');
        if (errors) throw new Error(errors + ' file' + (errors === 1 ? '' : 's') + ' could not be saved. Tap the button again to finish.');
        var s = state(); s.tracks = s.tracks || {};
        ids.forEach(function (id) { var t = track(id); if (t) s.tracks[id] = { h: t.h, at: new Date().toISOString(), bytes: t.bytes, title: t.title }; });
        setState(s);
      });
    }).then(function () { busy = false; }, function (e) { busy = false; throw e; });
  }
  function removeTrack(id) {
    var s = state(), keepIds = Object.keys(s.tracks || {}).filter(function (k) { return k !== id; });
    var keep = {};
    if (keepIds.length) filesFor(keepIds).forEach(function (f) { keep[f[0]] = 1; });
    var drop = filesFor([id]).filter(function (f) { return !keep[f[0]]; });
    return caches.open(CACHE).then(function (c) {
      return Promise.all(drop.map(function (f) { return c.delete(f[0]); })).then(function () { if (!keepIds.length) return c.delete(MAN); });
    }).then(function () { delete s.tracks[id]; setState(s); });
  }

  /* ── install ──────────────────────────────────────────────────────────── */
  var deferred = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferred = e; renderAll(); });
  window.addEventListener('appinstalled', function () { deferred = null; renderAll(); });
  function installHTML() {
    if (standalone) return '<p class="sch-ok">You are using the installed Schola app.</p>';
    if (deferred) return '<button type="button" class="sch-btn sch-install">Install Schola</button>';
    if (ios) return '<div class="sch-ios"><b>Install on iPhone or iPad:</b> tap <span class="sch-share" aria-label="Share">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="M8 7l4-4 4 4"/><path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg></span> ' +
      '<b>Share</b>, then <b>Add to Home Screen</b>. Open Schola from your Home Screen, then save tracks <b>inside the app</b>: ' +
      'Safari tabs and the Home Screen app keep separate storage, and Safari may clear a tab’s saved files after a week without use.</div>';
    return '<p class="sch-muted">To install, use your browser’s menu: <b>Install app</b> or <b>Add to Home screen</b>.</p>';
  }

  /* ── landing panel ────────────────────────────────────────────────────── */
  var panel = null, card = null, notice = '', scrim = null, tab = null;
  function openDrawer() {
    if (!panel) return;
    panel.classList.add('sch-open'); scrim.classList.add('sch-open');
    panel.setAttribute('aria-hidden', 'false'); tab.setAttribute('aria-expanded', 'true');
    var b = panel.querySelector('.sch-close'); if (b) b.focus({ preventScroll: true });
  }
  function closeDrawer() {
    if (!panel) return;
    panel.classList.remove('sch-open'); scrim.classList.remove('sch-open');
    panel.setAttribute('aria-hidden', 'true'); tab.setAttribute('aria-expanded', 'false');
    if (location.hash === '#schola') try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
  }
  function progressUI(host) {
    var p = host.querySelector('.sch-prog');
    return function (done, total, n, count) {
      p.hidden = false;
      var pct = total ? Math.round(done / total * 100) : 100;
      p.querySelector('.sch-bar i').style.width = pct + '%';
      if (tab) tab.querySelector('span').textContent = count && done < total ? 'Saving ' + pct + '%' : 'Schola';
      p.querySelector('.sch-ptxt').textContent = count ? 'Saving ' + n + ' of ' + count + ' files · ' + mb(done) + ' of ' + mb(total) : 'Checking saved files…';
    };
  }
  function run(host, ids, label) {
    notice = '';
    host.querySelector('.sch-msg').textContent = '';
    Array.prototype.forEach.call(host.querySelectorAll('button'), function (b) { b.disabled = true; });
    download(ids, progressUI(host)).then(function () {
      if (tab) tab.querySelector('span').textContent = 'Schola';
      notice = label + ' saved. It works without signal now.';
      renderAll();
    }, function (e) {
      if (tab) tab.querySelector('span').textContent = 'Schola';
      notice = e && e.message && e.message !== 'busy' ? e.message : 'A download is already running.';
      renderAll();
    });
  }
  function renderPanel() {
    if (!panel || !man) return;
    var saved = savedTracks(), ids = man.tracks.map(function (t) { return t.id; });
    var savedIds = ids.filter(function (id) { return saved[id]; });
    var stale = savedIds.filter(function (id) { return updateSize(track(id)); });
    var rows = man.tracks.map(function (t) {
      var s = saved[t.id], status, btns;
      if (s && s.h !== t.h) { status = '<span class="sch-up">Update available</span>'; btns = '<button type="button" class="sch-mini" data-save="' + t.id + '">Update</button>'; }
      else if (s) { status = '<span class="sch-saved">Saved ' + esc(date(s.at)) + '</span>'; btns = ''; }
      else { status = ''; btns = '<button type="button" class="sch-mini" data-save="' + t.id + '">Save</button>'; }
      if (s) btns += '<button type="button" class="sch-mini sch-rm" data-rm="' + t.id + '">Remove</button>';
      return '<li><a href="/academy/' + t.id + '">' + esc(t.title) + '</a><span class="sch-size">' + mb(t.bytes) + '</span>' + status + '<span class="sch-acts">' + btns + '</span></li>';
    }).join('');
    var allLabel = savedIds.length === ids.length && !stale.length ? 'Everything is saved'
      : savedIds.length ? 'Save the rest' : 'Download all tracks';
    panel.querySelector('.sch-body').innerHTML = TOOLS +
      '<div class="sch-install-row">' + installHTML() + '</div>' +
      '<div class="sch-all"><button type="button" class="sch-btn" data-all' + (savedIds.length === ids.length && !stale.length ? ' disabled' : '') + '>' + allLabel +
      '</button><span class="sch-muted">Every track · about ' + mb(man.all_bytes) + '</span>' +
      (stale.length ? '<button type="button" class="sch-btn sch-alt" data-upd>Update ' + stale.length + ' saved track' + (stale.length === 1 ? '' : 's') + '</button>' : '') + '</div>' +
      '<div class="sch-prog" hidden><div class="sch-bar"><i></i></div><div class="sch-ptxt"></div></div><p class="sch-msg" role="status">' + esc(notice) + '</p>' +
      '<details class="sch-tracks"' + (savedIds.length ? ' open' : '') + '><summary>Save one track at a time (' + man.tracks.length + ' tracks' +
      (savedIds.length ? ', ' + savedIds.length + ' saved' : '') + ')</summary><ul>' + rows + '</ul></details>' +
      '<p class="sch-note">Saved tracks, notes, highlights and bookmarks stay on this device only. On iPhone and iPad the Home Screen app keeps ' +
      'its own notes, separate from Safari: use <b>Back up all</b> and <b>Restore</b> in My notes to move them.</p>';
    estimate();
  }
  function estimate() {
    var host = panel || card;
    if (!host || !navigator.storage || !navigator.storage.estimate) return;
    navigator.storage.estimate().then(function (x) {
      var n = host.querySelector('.sch-store');
      if (!n) { n = el('p', 'sch-muted sch-store'); host.querySelector('.sch-body').appendChild(n); }
      n.textContent = 'Storage used by this site on this device: ' + mb(x.usage || 0) + (x.quota ? ' of about ' + mb(x.quota) + ' available' : '') + '.';
    }).catch(function () {});
  }

  /* Study tools on every academy page, explained once on the landing page */
  function tool(svg, title, text) {
    return '<li><span class="sch-ti">' + svg + '</span><span><b>' + title + '</b> ' + text + '</span></li>';
  }
  var SVG = function (d) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + '</svg>'; };
  var TOOLS = '<div class="sch-tools"><h3>Study tools in every module</h3><ul>' +
    tool(SVG('<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'), 'Highlights and notes.',
      'Select any text, then pick a color or tap Note. The orange pen button lists them, with export and print.') +
    tool(SVG('<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>'), 'Bookmarks.',
      'Tap the ribbon beside a section title. Your bookmarks are listed under the orange pen button too.') +
    tool(SVG('<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/>'), 'Pick up where you left off.',
      'Reopen a module, or this page, and tap Resume or Continue to return to where you stopped reading.') +
    tool(SVG('<path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M5 21h14"/>'), 'Study offline.',
      'Install Schola below and save a track, or every track, to read with no signal.') +
    '</ul><p class="sch-muted">All of this stays on your device: no account, nothing is sent anywhere.</p></div>';

  /* ── hub card ─────────────────────────────────────────────────────────── */
  function renderCard() {
    if (!card || !man) return;
    var t = trackOfPage();
    if (!t) { card.hidden = true; return; }
    var s = savedTracks()[t.id], html;
    if (s && s.h !== t.h) html = '<b>Saved for offline use</b> · an update is ready <button type="button" class="sch-btn" data-save="' + t.id + '">Update</button>';
    else if (s) html = '<b>Saved for offline use</b> · ' + esc(date(s.at)) + ' <button type="button" class="sch-mini sch-rm" data-rm="' + t.id + '">Remove</button>';
    else html = '<b>Study without signal.</b> Save this track (' + t.pages + ' pages, ' + mb(t.bytes) + ') to this device. ' +
      '<button type="button" class="sch-btn" data-save="' + t.id + '">Save this track</button>';
    card.querySelector('.sch-body').innerHTML = '<div class="sch-cardrow">' + html + '</div>' +
      (!standalone ? '<p class="sch-muted">Tip: <a href="/academy/#schola">install Schola</a>, the Academy app, ' + (ios ? 'and save tracks inside it.' : 'to open saved tracks like an app.') + '</p>' : '') +
      '<div class="sch-prog" hidden><div class="sch-bar"><i></i></div><div class="sch-ptxt"></div></div><p class="sch-msg" role="status">' + esc(notice) + '</p>';
  }
  function renderAll() { renderPanel(); renderCard(); }

  function onClick(e) {
    var host = e.currentTarget, b = e.target.closest('button');
    if (!b || b.disabled) return;
    if (b.classList.contains('sch-install') && deferred) {
      deferred.prompt();
      deferred.userChoice.then(function () { deferred = null; renderAll(); });
      return;
    }
    if (b.hasAttribute('data-all')) return run(host, man.tracks.map(function (t) { return t.id; }), 'Every track');
    if (b.hasAttribute('data-upd')) {
      var ids = Object.keys(savedTracks()).filter(function (id) { var t = track(id); return t && updateSize(t); });
      return run(host, ids, 'Updates');
    }
    var id = b.getAttribute('data-save');
    if (id) { var t = track(id); return run(host, [id], t ? t.title : 'Track'); }
    id = b.getAttribute('data-rm');
    if (id) {
      if (!b.getAttribute('data-armed')) {
        b.setAttribute('data-armed', '1'); b.textContent = 'Tap again to remove';
        setTimeout(function () { b.removeAttribute('data-armed'); b.textContent = 'Remove'; }, 3000);
        return;
      }
      removeTrack(id).then(renderAll);
    }
  }

  var ICON = '<img src="/images/app/schola-192.png" alt="" width="44" height="44">';
  function mount() {
    var main = document.querySelector('main.container') || document.querySelector('main');
    if (!main || !hasCache) return;
    if (isLanding) {
      /* Left drawer, opened by a tab on the left edge (Dr. Rivero: not the first thing you see when scrolling) */
      panel = el('aside', 'sch-panel sch-drawer no-print');
      panel.id = 'schola';
      panel.setAttribute('aria-label', 'Schola, the Academy app');
      panel.setAttribute('aria-hidden', 'true');
      panel.innerHTML = '<div class="sch-head">' + ICON + '<div><h2>Schola: the Academy as an app</h2>' +
        '<p>Install it on your phone, tablet or computer, and save tracks to study where there is no signal.</p></div>' +
        '<button type="button" class="sch-close" aria-label="Close">\u00d7</button></div><div class="sch-body"></div>';
      scrim = el('div', 'sch-scrim no-print');
      tab = el('button', 'sch-tab no-print', ICON.replace('width="44" height="44"', 'width="26" height="26"') + '<span>Schola</span>');
      tab.type = 'button';
      tab.setAttribute('aria-label', 'Open Schola: study tools, install the app, save tracks offline');
      tab.setAttribute('aria-controls', 'schola');
      document.body.appendChild(scrim);
      document.body.appendChild(panel);
      document.body.appendChild(tab);
      panel.addEventListener('click', onClick);
      panel.querySelector('.sch-close').addEventListener('click', closeDrawer);
      scrim.addEventListener('click', closeDrawer);
      tab.addEventListener('click', function () { panel.classList.contains('sch-open') ? closeDrawer() : openDrawer(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && panel.classList.contains('sch-open')) closeDrawer(); });
      window.addEventListener('hashchange', function () { if (location.hash === '#schola') openDrawer(); });
      if (location.hash === '#schola') setTimeout(openDrawer, 300);
    } else if (isHub) {
      card = el('div', 'sch-card no-print');
      card.innerHTML = '<div class="sch-cicon">' + ICON + '</div><div class="sch-body"></div>';
      main.insertBefore(card, main.firstChild);
      card.addEventListener('click', onClick);
    }
    getManifest().then(function (m) {
      if (!m) { if (panel) panel.hidden = true; if (card) card.hidden = true; return; }
      renderAll();
      appBar();
    });
  }

  /* ── installed app: bottom bar (no browser toolbar there) ─────────────── */
  function appBar() {
    if (!standalone || document.querySelector('.sch-appbar')) return;
    document.documentElement.classList.add('sch-app');
    var t = man ? trackOfPage() : null;
    var bar = el('nav', 'sch-appbar no-print');
    bar.setAttribute('aria-label', 'App navigation');
    bar.innerHTML =
      '<button type="button" data-back><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>Back</button>' +
      '<a href="/academy/"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>Academy</a>' +
      '<button type="button" data-print><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>Print</button>' +
      (t && !isHub ? '<a href="/academy/' + t.id + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/></svg>Track</a>' : '');
    bar.querySelector('[data-print]').addEventListener('click', function () { window.print(); });
    bar.querySelector('[data-back]').addEventListener('click', function () { if (history.length > 1) history.back(); else location.href = '/academy/'; });
    document.body.appendChild(bar);
    setTimeout(function () { window.dispatchEvent(new Event('resize')); }, 50);   // re-place the notes button
  }
  if (standalone) document.documentElement.classList.add('sch-app');

  /* ── styles ───────────────────────────────────────────────────────────── */
  var css = '' +
    '.sch-panel,.sch-card{font-family:"Nunito Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;color:#1b2430;border:1px solid rgba(31,56,100,.16);border-radius:16px;background:#fff;box-shadow:0 6px 22px rgba(15,30,46,.07)}' +
    '.sch-panel{padding:20px 22px;margin:8px 0 28px}' +
    '.sch-drawer{position:fixed;z-index:100001;top:0;left:0;bottom:0;margin:0;width:min(460px,94vw);border-radius:0 16px 16px 0;overflow-y:auto;overscroll-behavior:contain;' +
      'transform:translateX(-105%);visibility:hidden;transition:transform .22s ease,visibility 0s linear .22s;padding-bottom:calc(24px + env(safe-area-inset-bottom,0px))}' +
    '.sch-drawer.sch-open{transform:none;visibility:visible;transition:transform .22s ease}' +
    '.sch-drawer .sch-head{position:sticky;top:-20px;background:inherit;padding:20px 0 12px;margin:-20px 0 12px;z-index:1}' +
    '.sch-close{margin-left:auto;align-self:flex-start;border:0;background:none;font-size:28px;line-height:1;color:#5a6677;cursor:pointer;padding:0 4px}' +
    '.sch-scrim{position:fixed;inset:0;z-index:100000;background:rgba(10,18,32,.45);opacity:0;pointer-events:none;transition:opacity .2s}.sch-scrim.sch-open{opacity:1;pointer-events:auto}' +
    '.sch-tab{position:fixed;z-index:9996;left:0;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;' +
      'padding:12px 7px;border:0;border-radius:0 12px 12px 0;background:#1F3864;color:#fff;cursor:pointer;box-shadow:4px 6px 20px rgba(15,30,46,.25)}' +
    '.sch-tab img{border-radius:6px}.sch-tab span{writing-mode:vertical-rl;transform:rotate(180deg);font:700 13px Inter,system-ui,sans-serif;letter-spacing:.04em}' +
    '.sch-tab:hover{background:#26467c}' +
    '@media (max-width:640px){.sch-tab{top:auto;left:24px;bottom:calc(100px + env(safe-area-inset-bottom,0px));transform:none;width:44px;height:44px;padding:0;border-radius:50%;justify-content:center}' +
      '.sch-tab span{display:none}.sch-tab img{width:30px;height:30px;border-radius:8px}html.sch-app .sch-tab{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px))}}' +
    'html[data-theme="dark"] .sch-close{color:#a9b4c2}html[data-theme="dark"] .sch-tab{background:#26467c}' +
    '.sch-head{display:flex;gap:14px;align-items:center;margin-bottom:12px}.sch-head img,.sch-cicon img{border-radius:11px;flex:none}' +
    '.sch-head h2{font:800 21px/1.2 Inter,Manrope,system-ui,sans-serif;color:#1F3864;margin:0 0 3px}.sch-head p{margin:0;color:#4a5568;font-size:15px}' +
    '.sch-tools{background:#f5f8fb;border-radius:12px;padding:12px 16px;margin:4px 0 14px}.sch-tools h3{font:800 15px Inter,system-ui,sans-serif;color:#1F3864;margin:0 0 8px}' +
    '.sch-tools ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px 18px}' +
    '.sch-tools li{display:flex;gap:10px;font-size:14px;line-height:1.45;color:#2c3a4a}.sch-tools b{color:#1F3864}' +
    '.sch-ti{flex:none;width:30px;height:30px;border-radius:8px;background:#C55A11;color:#fff;display:flex;align-items:center;justify-content:center}.sch-ti svg{width:16px;height:16px}' +
    'html[data-theme="dark"] .sch-tools{background:#0f1826}html[data-theme="dark"] .sch-tools h3,html[data-theme="dark"] .sch-tools b{color:#e2b95f}html[data-theme="dark"] .sch-tools li{color:#d5dce6}' +
    '.sch-btn{border:0;background:#C55A11;color:#fff;border-radius:10px;padding:10px 18px;font:700 15px Inter,system-ui,sans-serif;cursor:pointer}' +
    '.sch-btn:disabled{background:#9aa6b6;cursor:default}.sch-btn.sch-alt{background:#1A6B72}' +
    '.sch-mini{border:1px solid rgba(31,56,100,.25);background:#fff;color:#1F3864;border-radius:8px;padding:5px 10px;font:600 13px Inter,system-ui,sans-serif;cursor:pointer}' +
    '.sch-mini.sch-rm{color:#C00000;border-color:rgba(192,0,0,.3)}.sch-mini:disabled{opacity:.5}' +
    '.sch-all{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin:12px 0 6px}' +
    '.sch-muted{color:#5a6677;font-size:14px;margin:6px 0}.sch-ok{color:#2E6B3E;font-weight:700;margin:4px 0}' +
    '.sch-ios{background:#f3f6fa;border-radius:10px;padding:10px 12px;font-size:14px;line-height:1.5}' +
    '.sch-share svg{width:16px;height:16px;vertical-align:-3px}' +
    '.sch-prog{margin:10px 0}.sch-bar{height:8px;border-radius:4px;background:#e6ebf1;overflow:hidden}.sch-bar i{display:block;height:100%;width:0;background:#C55A11;transition:width .2s}' +
    '.sch-ptxt{font-size:13px;color:#5a6677;margin-top:5px}.sch-msg{font-size:14px;font-weight:600;color:#1A6B72;margin:6px 0}.sch-msg:empty{display:none}' +
    '.sch-tracks{margin-top:10px}.sch-tracks summary{cursor:pointer;font-weight:700;color:#1F3864;padding:6px 0}' +
    '.sch-tracks ul{list-style:none;margin:6px 0 0;padding:0}' +
    '.sch-tracks li{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;padding:8px 0;border-top:1px solid rgba(31,56,100,.1)}' +
    '.sch-tracks li a{flex:1 1 220px;color:#1F3864;font-weight:600;text-decoration:none}.sch-size{color:#5a6677;font-size:13px;min-width:58px}' +
    '.sch-saved{color:#2E6B3E;font-size:13px;font-weight:700}.sch-up{color:#C55A11;font-size:13px;font-weight:700}.sch-acts{display:flex;gap:6px}' +
    '.sch-note{font-size:13px;color:#5a6677;margin:12px 0 0;line-height:1.5}' +
    '.sch-card[hidden],.sch-panel[hidden]{display:none!important}.sch-card{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;margin:6px 0 24px}.sch-card .sch-body{flex:1;min-width:0}' +
    '.sch-cardrow{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;font-size:15px}.sch-cardrow .sch-btn,.sch-cardrow .sch-mini{margin-left:auto}' +
    '.sch-card a{color:#1A6B72;font-weight:700}' +
    '.sch-appbar{position:fixed;z-index:9990;left:0;right:0;bottom:0;display:flex;justify-content:space-around;background:#1F3864;padding:6px 8px calc(6px + env(safe-area-inset-bottom,0px));box-shadow:0 -6px 20px rgba(0,0,0,.2)}' +
    '.sch-appbar a,.sch-appbar button{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;color:#fff;text-decoration:none;background:none;border:0;font:600 12px Inter,system-ui,sans-serif;padding:4px;cursor:pointer}' +
    '.sch-appbar svg{width:22px;height:22px}' +
    'html.sch-app body{padding-bottom:calc(66px + env(safe-area-inset-bottom,0px))}' +
    'html.sch-app .print-btn,html.sch-app .dl-fab,html.sch-app .float-controls,html.sch-app .float-controls-left,html.sch-app .scroll-top-btn{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px))}' +
    'html.sch-app .rcn-fab{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px))}' +
    'html.sch-app .rcn-resume{bottom:calc(82px + env(safe-area-inset-bottom,0px))}' +
    'html[data-theme="dark"] .sch-panel,html[data-theme="dark"] .sch-card{background:#162131;border-color:rgba(255,255,255,.12);color:#e6ebf2}' +
    'html[data-theme="dark"] .sch-head h2,html[data-theme="dark"] .sch-tracks summary,html[data-theme="dark"] .sch-tracks li a{color:#e2b95f}' +
    'html[data-theme="dark"] .sch-head p,html[data-theme="dark"] .sch-muted,html[data-theme="dark"] .sch-note,html[data-theme="dark"] .sch-size,html[data-theme="dark"] .sch-ptxt{color:#a9b4c2}' +
    'html[data-theme="dark"] .sch-mini{background:#0f1826;color:#e6ebf2;border-color:rgba(255,255,255,.2)}html[data-theme="dark"] .sch-ios{background:#0f1826}' +
    'html[data-theme="dark"] .sch-msg,html[data-theme="dark"] .sch-card a{color:#6cc3c9}html[data-theme="dark"] .sch-saved,html[data-theme="dark"] .sch-ok{color:#7fd19a}' +
    'html[data-theme="dark"] .sch-tracks li{border-color:rgba(255,255,255,.1)}html[data-theme="dark"] .sch-bar{background:#2a3648}' +
    '@media print{.sch-panel,.sch-card,.sch-appbar,.sch-tab,.sch-scrim{display:none!important}}';
  var st = document.createElement('style');
  st.id = 'schola-css';
  st.textContent = css;
  document.head.appendChild(st);

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
