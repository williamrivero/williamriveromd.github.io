/* Renal Care Academy search (Dr. Rivero, Nov 28 2026). Source file: edit this, then run
   python3 tools/academy/apply_search.py (fingerprints it and tags every academy page).
   The index (academy/pagefind/) is built by Pagefind from the Academy pages; it is plain static files, so it works
   offline once Schola has saved it. Nothing typed here is sent anywhere. */
(function () {
  "use strict";
  if (window.__rcmSearch) return;
  window.__rcmSearch = true;

  var BASE = "/academy/pagefind/";
  var KIND_LABEL = { "": "All", "Module": "Modules", "Track home": "Track homes", "Trainer page": "Trainer pages", "Emergency": "Emergency" };
  var PAGE = 10;
  var pf = null, loading = null, dlg = null, input, list, status, trackSel, kindBar, moreBtn;
  var lastFocus = null, kind = "", results = [], shown = 0, seq = 0;

  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  var ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" width="16" height="16"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M20 20l-4.2-4.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>';

  var CSS = '' +
    '.rcm-srch-pill{display:inline-flex;align-items:center;gap:6px;cursor:pointer;font:inherit;font-size:13px;font-weight:700;' +
    'color:var(--navy,#1f3864)!important;background:var(--bg,#f4f6f9);border:1px solid var(--border,#d6dde6)!important;}' +
    '.rcm-srch-pill:hover{background:var(--white,#fff);}' +
    '.rcm-srch-fab{position:fixed;right:24px;bottom:80px;z-index:9990;width:44px;height:44px;border-radius:50%;border:1px solid var(--border,#d6dde6);' +
    'background:var(--white,#fff);color:var(--navy,#1f3864);display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.18);}' +
    '.rcm-srch-fab svg{width:20px;height:20px;}' +
    '.rcm-srch{position:fixed;inset:0;z-index:2147483000;display:none;background:rgba(10,18,30,.55);}' +
    '.rcm-srch.open{display:block;}' +
    '.rcm-srch-box{position:absolute;left:50%;top:6vh;transform:translateX(-50%);width:min(720px,94vw);max-height:86vh;display:flex;flex-direction:column;' +
    'background:var(--white,#fff);color:var(--text,#1e2a38);border-radius:16px;box-shadow:0 24px 60px rgba(0,0,0,.35);overflow:hidden;font-family:Manrope,Inter,system-ui,sans-serif;}' +
    '.rcm-srch-top{display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid var(--border,#d6dde6);}' +
    '.rcm-srch-top svg{width:20px;height:20px;color:var(--teal,#1a6b72);flex:none;}' +
    '.rcm-srch-top input{flex:1;min-width:0;border:0;outline:0;background:transparent;color:inherit;font:500 17px/1.3 inherit;font-family:inherit;}' +
    '.rcm-srch-x{border:0;background:var(--bg,#f4f6f9);color:var(--text-muted,#5b6778);border-radius:8px;padding:6px 10px;font:600 13px inherit;font-family:inherit;cursor:pointer;}' +
    '.rcm-srch-f{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:10px 16px;border-bottom:1px solid var(--border,#d6dde6);}' +
    '.rcm-srch-f button{border:1px solid var(--border,#d6dde6);background:transparent;color:var(--text-muted,#5b6778);border-radius:999px;padding:4px 11px;font:600 12.5px inherit;font-family:inherit;cursor:pointer;}' +
    '.rcm-srch-f button[aria-pressed="true"]{background:var(--teal,#1a6b72);border-color:var(--teal,#1a6b72);color:#fff;}' +
    'html[data-theme="dark"] .rcm-srch-f button[aria-pressed="true"]{background:#0e4a50;border-color:#0e4a50;}' +
    '.rcm-srch-f select{margin-left:auto;max-width:100%;border:1px solid var(--border,#d6dde6);background:var(--white,#fff);color:inherit;border-radius:8px;padding:5px 8px;font:500 13px inherit;font-family:inherit;}' +
    '.rcm-srch-st{padding:8px 16px;font-size:13px;color:var(--text-muted,#5b6778);}' +
    '.rcm-srch-list{list-style:none;margin:0;padding:0 8px 8px;overflow-y:auto;}' +
    '.rcm-srch-r{border-radius:12px;padding:10px 10px;margin:2px 0;}' +
    '.rcm-srch-r:hover,.rcm-srch-r:focus-within{background:var(--bg,#f4f6f9);}' +
    '.rcm-srch-k{font:700 11px/1.3 Inter,system-ui,sans-serif;letter-spacing:.05em;text-transform:uppercase;color:var(--teal,#1a6b72);}' +
    '.rcm-srch-k .rcm-srch-off{margin-left:6px;color:#b45309;text-transform:none;letter-spacing:0;font-weight:600;}' +
    '.rcm-srch-t{display:block;margin:2px 0 3px;font:700 16px/1.3 Inter,system-ui,sans-serif;color:var(--navy,#1f3864);text-decoration:none;}' +
    'html[data-theme="dark"] .rcm-srch-t{color:var(--text,#e6ebf2);}' +
    '.rcm-srch-t:hover{text-decoration:underline;}' +
    '.rcm-srch-e{font-size:14px;line-height:1.5;color:var(--text-mid,#3d4a5c);margin:0;}' +
    '.rcm-srch-e mark,.rcm-srch-sub mark{background:#fde68a;color:#1e2a38;border-radius:3px;padding:0 1px;}' +
    '.rcm-srch-subs{list-style:none;margin:6px 0 0;padding:0 0 0 12px;border-left:3px solid var(--border,#d6dde6);}' +
    '.rcm-srch-sub{margin:4px 0;font-size:13.5px;line-height:1.45;}' +
    '.rcm-srch-sub a{font-weight:700;color:var(--teal,#1a6b72);text-decoration:none;}' +
    '.rcm-srch-sub a:hover{text-decoration:underline;}' +
    '.rcm-srch-sub span{color:var(--text-mid,#3d4a5c);}' +
    '.rcm-srch-more{margin:6px 8px 12px;padding:10px;border-radius:10px;border:1px solid var(--border,#d6dde6);background:transparent;color:var(--teal,#1a6b72);font:700 14px inherit;font-family:inherit;cursor:pointer;}' +
    '.rcm-srch-foot{padding:8px 16px;border-top:1px solid var(--border,#d6dde6);font-size:12px;color:var(--text-muted,#5b6778);}' +
    '@media (max-width:640px){.rcm-srch-box{top:0;left:0;transform:none;width:100vw;height:100%;max-height:none;border-radius:0;}' +
    '.rcm-srch-f select{margin-left:0;flex-basis:100%;}}' +
    '@media print{.rcm-srch,.rcm-srch-pill,.rcm-srch-fab{display:none!important;}}';

  function addCss() {
    var st = document.createElement("style");
    st.id = "rcm-srch-css";
    st.textContent = CSS;
    document.head.appendChild(st);
  }

  function load() {
    if (pf) return Promise.resolve(pf);
    if (!loading) {
      loading = import(BASE + "pagefind.js").then(function (m) {
        pf = m;
        return Promise.resolve(m.options ? m.options({ excerptLength: 26 }) : null).then(function () {
          if (m.init) m.init();
          return m;
        });
      }).catch(function (e) { loading = null; throw e; });
    }
    return loading;
  }

  function build() {
    dlg = document.createElement("div");
    dlg.className = "rcm-srch rcn-ui";
    dlg.setAttribute("role", "dialog");
    dlg.setAttribute("aria-modal", "true");
    dlg.setAttribute("aria-label", "Search the Academy");
    var chips = Object.keys(KIND_LABEL).map(function (k) {
      return '<button type="button" data-k="' + esc(k) + '" aria-pressed="' + (k === "" ? "true" : "false") + '">' + KIND_LABEL[k] + "</button>";
    }).join("");
    dlg.innerHTML = '<div class="rcm-srch-box">' +
      '<div class="rcm-srch-top">' + ICON + '<input type="search" placeholder="Search every track and module" aria-label="Search the Academy" autocomplete="off" spellcheck="false" enterkeyhint="search">' +
      '<button type="button" class="rcm-srch-x" aria-label="Close search">Esc</button></div>' +
      '<div class="rcm-srch-f" role="group" aria-label="Filter results">' + chips +
      '<select aria-label="Track"><option value="">All tracks</option></select></div>' +
      '<div class="rcm-srch-st" aria-live="polite"></div>' +
      '<ol class="rcm-srch-list"></ol>' +
      '<button type="button" class="rcm-srch-more" hidden>Show more results</button>' +
      '<div class="rcm-srch-foot">Searches the Academy only. Works offline once Schola has saved the Academy. Nothing you type is sent anywhere.</div>' +
      "</div>";
    document.body.appendChild(dlg);
    input = dlg.querySelector("input");
    list = dlg.querySelector(".rcm-srch-list");
    status = dlg.querySelector(".rcm-srch-st");
    trackSel = dlg.querySelector("select");
    kindBar = dlg.querySelector(".rcm-srch-f");
    moreBtn = dlg.querySelector(".rcm-srch-more");
    dlg.addEventListener("click", function (e) { if (e.target === dlg) close(); });
    dlg.querySelector(".rcm-srch-x").addEventListener("click", close);
    input.addEventListener("input", function () { ss("rcm-srch-q", input.value); run(); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") { var a = list.querySelector("a"); if (a) { e.preventDefault(); a.click(); } }
      if (e.key === "ArrowDown") { var f = list.querySelector("a"); if (f) { e.preventDefault(); f.focus(); } }
    });
    kindBar.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-k]"); if (!b) return;
      kind = b.getAttribute("data-k");
      kindBar.querySelectorAll("button[data-k]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      run();
    });
    trackSel.addEventListener("change", run);
    moreBtn.addEventListener("click", function () { render(shown + PAGE); });
    dlg.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { e.preventDefault(); close(); return; }
      if (e.key === "Tab") {                                   // keep focus inside the dialog
        var f = dlg.querySelectorAll("input,button:not([hidden]),select,a[href]");
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  function fillTracks() {
    load().then(function (m) { return m.filters ? m.filters() : {}; }).then(function (f) {
      var t = (f && f.track) || {};
      var names = Object.keys(t).sort(function (a, b) { return a === "Renal Care Academy" ? 1 : b === "Renal Care Academy" ? -1 : a.localeCompare(b); });
      trackSel.innerHTML = '<option value="">All tracks</option>' + names.map(function (n) { return '<option>' + esc(n) + "</option>"; }).join("");
      var saved = ss("rcm-srch-t"); if (saved && t[saved] !== undefined) trackSel.value = saved;
    }).catch(function () {});
  }

  function open() {
    if (!dlg) { build(); fillTracks(); }
    lastFocus = document.activeElement;
    dlg.classList.add("open");
    document.documentElement.style.overflow = "hidden";
    var q = ss("rcm-srch-q");
    if (q && !input.value) input.value = q;
    setTimeout(function () { input.focus(); input.select(); }, 30);
    status.textContent = "Loading the search index…";
    load().then(function () { status.textContent = input.value.trim() ? "" : "Type a word or phrase, for example: blood leak alarm, Kt/V, PhilHealth claim, hand hygiene."; if (input.value.trim()) run(); })
      .catch(function () { status.textContent = navigator.onLine ? "Search could not load. Reload the page and try again." : "Search is not saved on this device yet. Open Schola and tap Download all (or save a track) while you have signal."; });
  }
  function close() {
    if (!dlg) return;
    dlg.classList.remove("open");
    document.documentElement.style.overflow = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function filters() {
    var f = {};
    if (kind) f.kind = kind;
    if (trackSel.value) f.track = trackSel.value;
    ss("rcm-srch-t", trackSel.value || "");
    return f;
  }

  function run() {
    var q = input.value.trim(), my = ++seq;
    if (!q) { list.innerHTML = ""; moreBtn.hidden = true; status.textContent = "Type a word or phrase to search."; return; }
    load().then(function (m) {
      var p = m.debouncedSearch ? m.debouncedSearch(q, { filters: filters() }, 180) : m.search(q, { filters: filters() });
      return p;
    }).then(function (res) {
      if (my !== seq || !res) return;                         // a newer search replaced this one
      results = res.results || [];
      list.innerHTML = "";
      shown = 0;
      status.textContent = results.length ? results.length + (results.length === 1 ? " page" : " pages") + " found" :
        "No matches. Try fewer words, another spelling, or All tracks.";
      render(PAGE);
    }).catch(function () {});
  }

  function savedKey(url) {
    var p = url.split("#")[0];
    if (p === "/academy/" || p === "/academy/index.html") return "/academy/";
    return p.replace(/\.html$/, "");
  }
  function markOffline(li, url) {
    if (navigator.onLine || !window.caches) return;
    caches.open("schola-saved").then(function (c) { return c.match(savedKey(url)); }).then(function (r) {
      if (r) return;
      var k = li.querySelector(".rcm-srch-k");
      if (k) k.insertAdjacentHTML("beforeend", '<span class="rcm-srch-off">· not saved for offline</span>');
    }).catch(function () {});
  }

  function render(upto) {
    var my = seq, slice = results.slice(shown, upto);
    shown = Math.min(upto, results.length);
    moreBtn.hidden = shown >= results.length;
    Promise.all(slice.map(function (r) { return r.data(); })).then(function (rows) {
      if (my !== seq) return;
      rows.forEach(function (d) {
        var meta = d.meta || {};
        var where = [meta.kind === "Module" && meta.mod ? "Module " + meta.mod : meta.kind, meta.track].filter(Boolean).join(" · ");
        var subs = (d.sub_results || []).filter(function (s) { return s.url !== d.url && s.title && s.title !== meta.title; }).slice(0, 3);
        var li = document.createElement("li");
        li.className = "rcm-srch-r";
        li.innerHTML = '<div class="rcm-srch-k">' + esc(where) + "</div>" +
          '<a class="rcm-srch-t" href="' + esc(d.url) + '">' + esc(meta.title || d.url) + "</a>" +
          (subs.length ? "" : '<p class="rcm-srch-e">' + (d.excerpt || "") + "</p>") +
          (subs.length ? '<ul class="rcm-srch-subs">' + subs.map(function (s) {
            return '<li class="rcm-srch-sub"><a href="' + esc(s.url) + '">' + esc(s.title) + "</a> <span>" + (s.excerpt || "") + "</span></li>";
          }).join("") + "</ul>" : "");
        list.appendChild(li);
        markOffline(li, d.url);
      });
    }).catch(function () {});
  }

  function sameDocJump(e) {                                  // a result on this page: close the dialog, then jump
    var a = e.target.closest("a[href]"); if (!a || !dlg.contains(a)) return;
    var u = new URL(a.href, location.href);
    if (u.pathname.replace(/\.html$/, "") === location.pathname.replace(/\.html$/, "") && u.hash) { close(); }
  }

  function mount() {
    addCss();
    var pills = document.querySelector(".nav-strip .nav-pills");
    if (pills) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "nav-pill rcm-srch-pill rcn-ui";
      b.setAttribute("aria-label", "Search the Academy");
      b.innerHTML = ICON + "<span>Search</span>";
      b.addEventListener("click", open);
      pills.insertBefore(b, pills.firstChild);
    } else {
      var f = document.createElement("button");
      f.type = "button";
      f.className = "rcm-srch-fab rcn-ui";
      f.setAttribute("aria-label", "Search the Academy");
      f.title = "Search the Academy";
      f.innerHTML = ICON;
      f.addEventListener("click", open);
      document.body.appendChild(f);
    }
    // the landing page carries a search field in its HTML (apply_search.py), so the hero never shifts when this loads
    document.querySelectorAll("[data-rcm-search]").forEach(function (h) { h.addEventListener("click", open); });
    document.addEventListener("keydown", function (e) {
      var t = e.target, typing = t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
      if ((e.key === "/" && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) || ((e.ctrlKey || e.metaKey) && (e.key === "k" || e.key === "K"))) {
        if (dlg && dlg.classList.contains("open")) return;
        e.preventDefault();
        open();
      }
    });
    document.addEventListener("click", function (e) { if (dlg && dlg.classList.contains("open")) sameDocJump(e); }, true);
    if (/[?&]search=/.test(location.search)) {                // /academy/?search=hyperkalemia opens the dialog with that query
      var q = new URLSearchParams(location.search).get("search");
      if (q) { ss("rcm-srch-q", q); open(); }
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
  else mount();
})();
