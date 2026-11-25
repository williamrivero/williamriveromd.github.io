/* theme.js — Auto / Light / Dim / Dark / E-paper appearance for renalcarematters.com
 *
 * Source file. Pages load the fingerprinted copy (theme.<hash>.js) written by
 * patch_theme_modes.py, which also inlines the pre-paint bootstrap in <head>.
 *
 *   Light → no data-theme (or data-theme="light")
 *   Dim   → html[data-theme="dark"][data-shade="dim"]   (+ theme-dim.<hash>.css)
 *   Dark  → html[data-theme="dark"]
 *   E-paper → html[data-shade="epaper"], light base (+ theme-epaper.<hash>.css); manual only, Auto never picks it
 *   Auto  → system dark setting wins; otherwise by local time of day:
 *           Light 06:00–17:59 · Dim 18:00–21:59 · Dark 22:00–05:59
 *
 * The existing dark toggle button on every page (#darkToggle and variants)
 * now cycles Auto → Light → Dim → Dark → E-paper. The legacy 'wgmr-dark' key is kept in
 * sync so older per-page scripts agree with the resolved theme.
 * Never move the bootstrap to the bottom of the page (flash + CLS).
 */
(function () {
  'use strict';
  var KEY = 'wgmr-theme-mode';
  var MODES = ['auto', 'light', 'dim', 'dark', 'epaper'];
  var NAMES = { auto: 'Auto', light: 'Light', dim: 'Dim', dark: 'Dark', epaper: 'E-paper' };
  var TOGGLES = '#darkToggle,#darkToggleF,#darkToggle2,#floatDarkBtn,#dark-toggle,[onclick*="toggleDark"]';
  var d = document.documentElement;

  var ICONS = {
    light: '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>',
    dim: '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor" stroke="none" opacity=".55"/>',
    dark: '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
    epaper: '<rect x="5" y="2.5" width="14" height="19" rx="2"/><line x1="8.5" y1="7.5" x2="15.5" y2="7.5"/><line x1="8.5" y1="11" x2="15.5" y2="11"/><line x1="8.5" y1="14.5" x2="13" y2="14.5"/>',
    auto: '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor" stroke="none" opacity=".25"/><path d="M9 16l3-8 3 8M10.1 13.4h3.8"/>'
  };

  function ls(k, v) {
    try {
      if (v === undefined) return localStorage.getItem(k);
      localStorage.setItem(k, v);
    } catch (e) { return null; }
  }
  function getMode() {
    var m = ls(KEY);
    return MODES.indexOf(m) >= 0 ? m : 'auto';
  }
  function systemDark() {
    try { return window.matchMedia('(prefers-color-scheme: dark)').matches; } catch (e) { return false; }
  }
  function byClock() {
    var h = new Date().getHours();
    return h >= 6 && h < 18 ? 'light' : (h >= 18 && h < 22 ? 'dim' : 'dark');
  }
  function resolve(m) {
    if (m !== 'auto') return m;
    return systemDark() ? 'dark' : byClock();
  }

  function ensureDimCss() {
    if (document.getElementById('rc-dim-css') || !window.__RC_DIM_CSS) return;
    var l = document.createElement('link');
    l.id = 'rc-dim-css';
    l.rel = 'stylesheet';
    l.href = window.__RC_DIM_CSS;
    document.head.appendChild(l);
  }

  function ensureEpaperCss() {
    if (document.getElementById('rc-epaper-css') || !window.__RC_EPAPER_CSS) return;
    var l = document.createElement('link');
    l.id = 'rc-epaper-css';
    l.rel = 'stylesheet';
    l.href = window.__RC_EPAPER_CSS;
    document.head.appendChild(l);
  }
  function isDark(t) { return t === 'dim' || t === 'dark'; }

  function inSync(t) {
    var dark = d.getAttribute('data-theme') === 'dark';
    var shade = d.getAttribute('data-shade') || '';
    if (t === 'light') return !dark && !shade;
    if (t === 'epaper') return !dark && shade === 'epaper';
    return dark && (shade === 'dim') === (t === 'dim');
  }

  function setAttrs(t, m) {
    if (!isDark(t)) {
      if (d.getAttribute('data-theme') === 'dark') d.setAttribute('data-theme', 'light');
      if (t === 'epaper') d.setAttribute('data-shade', 'epaper'); else d.removeAttribute('data-shade');
    } else {
      d.setAttribute('data-theme', 'dark');
      if (t === 'dim') d.setAttribute('data-shade', 'dim'); else d.removeAttribute('data-shade');
    }
    d.setAttribute('data-theme-mode', m);
  }

  function updateUi(m, t) {
    var label = m === 'auto' ? 'Auto · ' + NAMES[t] : NAMES[m];
    var tip = 'Appearance: ' + label + '. Tap to change (Auto → Light → Dim → Dark → E-paper).';
    var btns = document.querySelectorAll(TOGGLES);
    for (var i = 0; i < btns.length; i++) {
      var b = btns[i];
      b.setAttribute('title', tip);
      b.setAttribute('aria-label', tip);
      b.classList.toggle('active', isDark(t));
      var svg = b.querySelector('svg');
      if (svg) svg.innerHTML = ICONS[m === 'auto' ? 'auto' : t];
      var span = b.querySelector('.float-tooltip,[id^="darkLabel"]');
      if (span) span.textContent = label;
      else if (!svg && b.textContent.trim().length < 24) b.textContent = label;
    }
    var lbls = document.querySelectorAll('#darkLabel');
    for (var j = 0; j < lbls.length; j++) lbls[j].textContent = label;
  }

  function apply() {
    var m = getMode(), t = resolve(m);
    if (t === 'dim') ensureDimCss();
    if (t === 'epaper') ensureEpaperCss();
    // Let page-specific dark handlers run their side effects (icons, charts,
    // body classes) — then enforce the resolved attributes on top.
    if (typeof window.applyDark === 'function') {
      try { window.applyDark(isDark(t)); } catch (e) {}
    }
    setAttrs(t, m);
    ls('wgmr-dark', isDark(t) ? '1' : '0');
    ls('wgmr-dk', isDark(t) ? '1' : '0');
    updateUi(m, t);
    if (window.__rcLast && typeof window.rcRender === 'function') {
      try { window.rcRender(window.__rcLast); } catch (e) {}
    }
    try { document.dispatchEvent(new CustomEvent('rc-themechange', { detail: { mode: m, theme: t } })); } catch (e) {}
    return t;
  }

  var toastTimer;
  function toast(m, t) {
    var el = document.getElementById('rc-theme-toast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'rc-theme-toast';
      el.setAttribute('role', 'status');
      el.setAttribute('aria-live', 'polite');
      el.style.cssText = 'position:fixed;left:50%;bottom:84px;transform:translateX(-50%);z-index:2147483000;' +
        'padding:10px 18px;border-radius:999px;font:600 14px/1.3 Inter,system-ui,sans-serif;' +
        'background:rgba(20,28,42,.94);color:#fff;box-shadow:0 6px 24px rgba(0,0,0,.25);' +
        'pointer-events:none;opacity:0;transition:opacity .2s;max-width:90vw;text-align:center';
      document.body.appendChild(el);
    }
    var why = m !== 'auto' ? '' : (systemDark() ? ' (your phone is in dark mode)' :
      t === 'light' ? ' (daytime)' : t === 'dim' ? ' (evening)' : ' (night)');
    el.textContent = 'Appearance: ' + NAMES[m] + (m === 'auto' ? ' — ' + NAMES[t] + ' now' + why : '');
    el.style.opacity = '1';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.style.opacity = '0'; }, 2200);
  }

  function setMode(m) {
    if (MODES.indexOf(m) < 0) return;
    ls(KEY, m);
    var t = apply();
    toast(m, t);
  }
  function cycle() {
    var m = getMode();
    setMode(MODES[(MODES.indexOf(m) + 1) % MODES.length]);
  }

  // Intercept the legacy dark toggles before their inline onclick runs.
  document.addEventListener('click', function (e) {
    var b = e.target && e.target.closest && e.target.closest(TOGGLES);
    if (!b) return;
    e.preventDefault();
    e.stopImmediatePropagation();
    e.stopPropagation();
    cycle();
  }, true);

  // Legacy entry points some pages call directly.
  window.toggleDark = cycle;
  window.rcTheme = { get: getMode, set: setMode, cycle: cycle, resolve: function () { return resolve(getMode()); } };

  // Re-assert if an older page script flips data-theme after load.
  try {
    new MutationObserver(function () {
      var t = resolve(getMode());
      if (!inSync(t)) setAttrs(t, getMode());
    }).observe(d, { attributes: true, attributeFilter: ['data-theme', 'data-shade'] });
  } catch (e) {}

  // Auto mode follows the clock and the system setting live.
  function refreshIfAuto() { if (getMode() === 'auto' && !inSync(resolve('auto'))) apply(); }
  setInterval(refreshIfAuto, 60000);
  document.addEventListener('visibilitychange', function () { if (!document.hidden) refreshIfAuto(); });
  try {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    (mq.addEventListener ? mq.addEventListener.bind(mq, 'change') : mq.addListener.bind(mq))(refreshIfAuto);
  } catch (e) {}
  window.addEventListener('storage', function (e) { if (e.key === KEY) apply(); });

  apply();
  document.addEventListener('DOMContentLoaded', function () { window.toggleDark = cycle; apply(); });
  window.addEventListener('load', function () { window.toggleDark = cycle; updateUi(getMode(), resolve(getMode())); });
})();
