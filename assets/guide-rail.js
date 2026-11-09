/*!
 * guide-rail.js — renalcarematters.com
 * Slim side rail for content guides (desktop + tablet, ≥ 1024px wide).
 *
 * A thin sticky icon rail on the right edge opens a slide-out drawer with up
 * to three tabs, built from what the guide already has:
 *   References  ← cloned from the References accordion (.ref-section .ref-acc)
 *   Glossary    ← cloned from the Glossary accordion (.glossary-section)
 *   Share       ← rendered by share-buttons.js (window.rcmShare.renderGrid)
 *
 * While the rail is active (≥ 1024px), the end-of-guide References, Glossary and
 * "Share this guide" blocks are hidden; they stay in the page (search engines,
 * print, and phones < 1024px keep using them). In-page links that point into
 * the references or glossary (e.g. citation links to #ref-3) open the drawer
 * on the matching item instead.
 *
 * Language: cloned content keeps its data-lang spans, so the guide's setLang()
 * keeps translating it. Styles are injected here (scoped .rcm-rail / .rcm-drawer)
 * so patch_master_css.py never touches them. Hidden in print.
 * Installed on guides by patch_guide_rail.py (load after share-buttons.js).
 */
(function () {
  'use strict';
  if (window.__rcmRail) return;
  window.__rcmRail = true;

  var MQ = window.matchMedia ? window.matchMedia('(min-width: 1024px)') : { matches: true, addListener: function () {} };

  var I = {
    refs: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><path d="M9 7h7M9 11h5"/>',
    gloss: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    score: '<path d="M3 3v18h18"/><path d="M8 17v-5M13 17V8M18 17v-9"/>',
    share: '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
    close: '<path d="M18 6 6 18M6 6l12 12"/>'
  };
  function svg(d) {
    return '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + d + '</svg>';
  }

  function activeLang() {
    var vis = document.querySelector('[data-lang]:not(.lang-hidden)');
    return (vis && vis.getAttribute('data-lang')) || 'en';
  }
  function langSpans(map) {
    if (!document.querySelector('[data-lang="tl"]')) return map.en;
    var a = activeLang();
    return ['en', 'tl', 'ceb', 'kap'].map(function (l) {
      return '<span data-lang="' + l + '"' + (l === a ? '' : ' class="lang-hidden"') + '>' + map[l] + '</span>';
    }).join('');
  }

  var CSS = [
    '.rcm-rail{position:fixed;right:0;top:50%;transform:translateY(-50%);z-index:900;display:flex;flex-direction:column;gap:2px;padding:6px 0;background:var(--white,#fff);border:1px solid var(--border,#d8dee8);border-right:0;border-radius:12px 0 0 12px;box-shadow:-4px 4px 18px rgba(15,23,42,.10);}',
    '.rcm-rail-btn{position:relative;display:flex;align-items:center;justify-content:center;width:46px;height:46px;border:0;background:transparent;color:#1F3864;cursor:pointer;padding:0;}',
    '.rcm-rail-btn svg{width:20px;height:20px;}',
    '.rcm-rail-btn:hover,.rcm-rail-btn:focus-visible,.rcm-rail-btn.is-on{color:#1A6B72;background:rgba(26,107,114,.09);outline:none;}',
    '.rcm-rail-btn:focus-visible{box-shadow:inset 0 0 0 2px #1A6B72;}',
    '.rcm-rail-btn .rcm-rail-n{position:absolute;top:5px;right:4px;min-width:16px;height:16px;padding:0 4px;border-radius:8px;background:#1A6B72;color:#fff;font:700 9.5px/16px Inter,system-ui,sans-serif;text-align:center;}',
    '.rcm-rail-tip{position:absolute;right:calc(100% + 10px);top:50%;transform:translateY(-50%);background:#1e2a38;color:#fff;font:600 12px/1 Manrope,Inter,system-ui,sans-serif;padding:7px 10px;border-radius:6px;white-space:nowrap;pointer-events:none;opacity:0;transition:opacity .12s;}',
    '.rcm-rail-btn:hover .rcm-rail-tip,.rcm-rail-btn:focus-visible .rcm-rail-tip{opacity:1;}',
    '.rcm-scrim{position:fixed;inset:0;background:rgba(15,23,42,.28);z-index:950;opacity:0;pointer-events:none;transition:opacity .2s;}',
    '.rcm-scrim.is-open{opacity:1;pointer-events:auto;}',
    '.rcm-drawer{position:fixed;top:0;right:0;bottom:0;width:min(460px,92vw);z-index:960;display:flex;flex-direction:column;background:var(--white,#fff);color:var(--text,#1e2a38);box-shadow:-12px 0 36px rgba(15,23,42,.22);transform:translateX(102%);transition:transform .24s ease;visibility:hidden;}',
    '.rcm-drawer.is-open{transform:none;visibility:visible;}',
    '.rcm-drawer-head{display:flex;align-items:center;gap:4px;padding:10px 10px 0 14px;border-bottom:1px solid var(--border,#d8dee8);}',
    '.rcm-tab{border:0;background:transparent;padding:12px 10px 11px;font:700 12px/1 Inter,Manrope,system-ui,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:var(--text-muted,#5b6678);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-1px;}',
    '.rcm-tab[aria-selected="true"]{color:#1A6B72;border-bottom-color:#1A6B72;}',
    '.rcm-tab:focus-visible{outline:2px solid #1A6B72;outline-offset:-2px;}',
    '.rcm-close{margin-left:auto;display:flex;align-items:center;justify-content:center;width:36px;height:36px;border:0;border-radius:50%;background:transparent;color:var(--text-mid,#3d4a5c);cursor:pointer;}',
    '.rcm-close svg{width:18px;height:18px;}',
    '.rcm-close:hover,.rcm-close:focus-visible{background:rgba(15,23,42,.07);outline:none;}',
    '.rcm-pane{flex:1;overflow-y:auto;overscroll-behavior:contain;padding:16px 22px 28px;font-size:13.5px;line-height:1.7;color:var(--text-mid,#3d4a5c);}',
    '.rcm-pane[hidden]{display:none;}',
    '.rcm-pane-title{font:700 15px/1.3 Inter,system-ui,sans-serif;color:var(--text,#1e2a38);margin:0 0 4px;}',
    '.rcm-pane-sub{font-size:12px;color:var(--text-muted,#5b6678);margin:0 0 12px;}',
    '.rcm-pane ol{margin:0!important;padding:0 0 0 22px!important;font-size:13px!important;line-height:1.65!important;}',
    '.rcm-pane ol li{margin:0 0 9px;padding:4px 6px;border-radius:6px;transition:background .3s;}',
    '.rcm-pane li.rcm-hit,.rcm-pane dt.rcm-hit,.rcm-pane dt.rcm-hit+dd{background:rgba(197,90,17,.14);}',
    '.rcm-pane a{color:var(--teal,#1A6B72);word-break:break-word;}',
    '.rcm-pane > div{padding:0!important;}',
    '.rcm-pane .rcm-share-grid{grid-template-columns:1fr 1fr;}',
    '.rcm-pane > .rcm-score-card{margin:0;box-shadow:none;max-width:none;padding:16px 18px!important;}',
    '.rcm-pane .rcm-score-card .ov-list{display:block!important;}',
    'html.rcm-rail-on .ref-section,html.rcm-rail-on .glossary-section,html.rcm-rail-on .rcm-share-panel{display:none!important;}',
    'html[data-theme="dark"] .rcm-rail,body.dark-mode .rcm-rail{background:#1a2535;border-color:#2c3a52;}',
    'html[data-theme="dark"] .rcm-rail-btn,body.dark-mode .rcm-rail-btn{color:#d6deea;}',
    'html[data-theme="dark"] .rcm-rail-btn:hover,html[data-theme="dark"] .rcm-rail-btn.is-on,body.dark-mode .rcm-rail-btn:hover,body.dark-mode .rcm-rail-btn.is-on{color:#7fd3da;background:rgba(127,211,218,.10);}',
    'html[data-theme="dark"] .rcm-drawer,body.dark-mode .rcm-drawer{background:#141d2b;color:#e6ecf5;}',
    'html[data-theme="dark"] .rcm-drawer-head,body.dark-mode .rcm-drawer-head{border-bottom-color:#2c3a52;}',
    'html[data-theme="dark"] .rcm-tab,body.dark-mode .rcm-tab{color:#9ba6b8;}',
    'html[data-theme="dark"] .rcm-tab[aria-selected="true"],body.dark-mode .rcm-tab[aria-selected="true"]{color:#7fd3da;border-bottom-color:#7fd3da;}',
    'html[data-theme="dark"] .rcm-pane,body.dark-mode .rcm-pane{color:#c9d3e1;}',
    'html[data-theme="dark"] .rcm-pane-title,body.dark-mode .rcm-pane-title{color:#e6ecf5;}',
    'html[data-theme="dark"] .rcm-pane-sub,body.dark-mode .rcm-pane-sub{color:#9ba6b8;}',
    'html[data-theme="dark"] .rcm-pane a,body.dark-mode .rcm-pane a{color:#7fd3da;}',
    'html[data-theme="dark"] .rcm-pane dt,body.dark-mode .rcm-pane dt,html[data-theme="dark"] .rcm-pane h4,body.dark-mode .rcm-pane h4{color:#e6ecf5!important;}',
    'html[data-theme="dark"] .rcm-close,body.dark-mode .rcm-close{color:#c9d3e1;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card,body.dark-mode .rcm-pane .rcm-score-card{background:#1a2535!important;border-color:#2c3a52!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .ov-stat,body.dark-mode .rcm-pane .rcm-score-card .ov-stat{border-color:#2c3a52!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .v,body.dark-mode .rcm-pane .rcm-score-card .v{color:#e6ecf5!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .v .u,body.dark-mode .rcm-pane .rcm-score-card .v .u{color:#9ba6b8!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .l,body.dark-mode .rcm-pane .rcm-score-card .l{color:#c9d3e1!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .ov-src,body.dark-mode .rcm-pane .rcm-score-card .ov-src{color:#9ba6b8!important;border-color:#2c3a52!important;}',
    'html[data-theme="dark"] .rcm-pane .rcm-score-card .ov-foot,body.dark-mode .rcm-pane .rcm-score-card .ov-foot{color:#7fd3da!important;}',
    '@media (max-width:1023.98px){.rcm-rail,.rcm-drawer,.rcm-scrim{display:none!important;}}',
    '@media print{.rcm-rail,.rcm-drawer,.rcm-scrim{display:none!important;}html.rcm-rail-on .ref-section,html.rcm-rail-on .glossary-section{display:block!important;}}'
  ].join('\n');

  function init() {
    if (document.querySelector('.rcm-rail')) return;

    var refSec = null;
    Array.prototype.some.call(document.querySelectorAll('.ref-section'), function (s) {
      if (s.querySelector('.ref-acc ol, ol')) { refSec = s; return true; } return false;
    });
    var glossSec = document.querySelector('.glossary-section');
    if (glossSec && !glossSec.querySelector('.glossary-acc')) glossSec = null;
    var canShare = !!window.rcmShare;
    // Clinician Evidence Scorecard (the stat card in the clinician hero), if any.
    var scoreCard = null;
    Array.prototype.some.call(document.querySelectorAll('.hero-cards .ov-card'), function (c) {
      if (c.querySelector('.ov-stat') || /evidence/i.test((c.querySelector('.ov-title') || {}).textContent || '')) { scoreCard = c; return true; }
      return false;
    });
    if (!refSec && !glossSec && !canShare && !scoreCard) return;

    var st = document.createElement('style'); st.id = 'rcm-rail-css'; st.textContent = CSS;
    document.head.appendChild(st);

    var tabs = [];
    if (scoreCard) tabs.push({ k: 'score', en: 'Scorecard', tl: 'Scorecard', ceb: 'Scorecard', kap: 'Scorecard', icon: I.score, clinician: true });
    if (refSec) tabs.push({ k: 'refs', en: 'References', tl: 'Mga Sanggunian', ceb: 'Mga Tinubdan', kap: 'Deng Pikuanan', icon: I.refs,
      n: refSec.querySelectorAll('ol > li').length });
    if (glossSec) tabs.push({ k: 'gloss', en: 'Glossary', tl: 'Glosaryo', ceb: 'Glosaryo', kap: 'Glosaryo', icon: I.gloss });
    if (canShare) tabs.push({ k: 'share', en: 'Share', tl: 'Ibahagi', ceb: 'Ipaambit', kap: 'Ibahagi', icon: I.share });

    // Rail
    var rail = document.createElement('nav');
    rail.className = 'rcm-rail'; rail.setAttribute('aria-label', 'Guide tools');
    rail.innerHTML = tabs.map(function (t) {
      return '<button type="button" class="rcm-rail-btn" data-tab="' + t.k + '" aria-label="' + t.en + '" aria-controls="rcm-pane-' + t.k + '">' +
        svg(t.icon) + (t.n ? '<span class="rcm-rail-n" aria-hidden="true">' + t.n + '</span>' : '') +
        '<span class="rcm-rail-tip">' + langSpans(t) + '</span></button>';
    }).join('');

    // Drawer
    var scrim = document.createElement('div'); scrim.className = 'rcm-scrim';
    var dr = document.createElement('aside');
    dr.className = 'rcm-drawer'; dr.setAttribute('role', 'dialog'); dr.setAttribute('aria-label', 'Guide references, glossary and sharing'); dr.setAttribute('aria-hidden', 'true');
    dr.innerHTML = '<div class="rcm-drawer-head" role="tablist">' + tabs.map(function (t) {
      return '<button type="button" class="rcm-tab" role="tab" id="rcm-tab-' + t.k + '" data-tab="' + t.k + '" aria-selected="false" aria-controls="rcm-pane-' + t.k + '">' + langSpans(t) + '</button>';
    }).join('') + '<button type="button" class="rcm-close" aria-label="Close">' + svg(I.close) + '</button></div>' +
      tabs.map(function (t) { return '<div class="rcm-pane" role="tabpanel" id="rcm-pane-' + t.k + '" aria-labelledby="rcm-tab-' + t.k + '" hidden></div>'; }).join('');

    function strip(node) { // cloned content must not duplicate ids or keep inline color overrides that fight dark mode
      if (node.removeAttribute) node.removeAttribute('id');
      Array.prototype.forEach.call(node.querySelectorAll ? node.querySelectorAll('[id]') : [], function (e) { e.removeAttribute('id'); });
      return node;
    }

    if (scoreCard) {
      var sc = dr.querySelector('#rcm-pane-score');
      sc.innerHTML = '<p class="rcm-pane-title">Evidence Scorecard</p><p class="rcm-pane-sub">Key numbers for clinicians, from this guide</p>';
      var cc = strip(scoreCard.cloneNode(true)); cc.classList.add('rcm-score-card');
      var t0 = cc.querySelector('.ov-head'); if (t0) t0.remove();
      sc.appendChild(cc);
    }
    var refTab = tabs.filter(function (t) { return t.k === 'refs'; })[0];
    if (refSec) {
      var pane = dr.querySelector('#rcm-pane-refs');
      pane.innerHTML = '<p class="rcm-pane-title">' + langSpans(refTab) + '</p><p class="rcm-pane-sub">' + refTab.n + ' sources · APA 7</p>';
      pane.appendChild(strip(refSec.querySelector('ol').cloneNode(true)));
    }
    if (glossSec) {
      var gp = dr.querySelector('#rcm-pane-gloss');
      var gt = tabs.filter(function (t) { return t.k === 'gloss'; })[0];
      gp.innerHTML = '<p class="rcm-pane-title">' + langSpans({ en: 'Glossary &amp; abbreviations', tl: 'Glosaryo at mga daglat', ceb: 'Glosaryo ug mga minubo', kap: 'Glosaryo at deng abbreviation' }) + '</p>';
      var body = glossSec.querySelector('.glossary-acc > div') || glossSec.querySelector('.glossary-acc');
      Array.prototype.forEach.call(body.children, function (c) { if (c.tagName !== 'SUMMARY') gp.appendChild(strip(c.cloneNode(true))); });
    }
    if (canShare) {
      var sp = dr.querySelector('#rcm-pane-share');
      sp.innerHTML = '<p class="rcm-pane-title">' + langSpans({ en: 'Share this guide', tl: 'Ibahagi ang gabay na ito', ceb: 'Ipaambit kini nga giya', kap: 'Ibahagi me ing gabay a iti' }) + '</p>';
      window.rcmShare.renderGrid(sp);
    }

    document.body.appendChild(rail); document.body.appendChild(scrim); document.body.appendChild(dr);

    var lastFocus = null, current = null;
    function select(k) {
      current = k;
      Array.prototype.forEach.call(dr.querySelectorAll('.rcm-tab'), function (b) { b.setAttribute('aria-selected', b.getAttribute('data-tab') === k ? 'true' : 'false'); });
      Array.prototype.forEach.call(dr.querySelectorAll('.rcm-pane'), function (p) { p.hidden = p.id !== 'rcm-pane-' + k; });
      Array.prototype.forEach.call(rail.querySelectorAll('.rcm-rail-btn'), function (b) { b.classList.toggle('is-on', isOpen() && b.getAttribute('data-tab') === k); });
    }
    function isOpen() { return dr.classList.contains('is-open'); }
    function open(k, hit) {
      if (!isOpen()) lastFocus = document.activeElement;
      dr.classList.add('is-open'); scrim.classList.add('is-open'); dr.setAttribute('aria-hidden', 'false');
      select(k);
      var pane = dr.querySelector('#rcm-pane-' + k);
      Array.prototype.forEach.call(pane.querySelectorAll('.rcm-hit'), function (e) { e.classList.remove('rcm-hit'); });
      if (hit) {
        hit.classList.add('rcm-hit');
        setTimeout(function () { hit.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 60);
      } else pane.scrollTop = 0;
      var tab = dr.querySelector('#rcm-tab-' + k); if (tab) tab.focus({ preventScroll: true });
    }
    function close() {
      dr.classList.remove('is-open'); scrim.classList.remove('is-open'); dr.setAttribute('aria-hidden', 'true');
      Array.prototype.forEach.call(rail.querySelectorAll('.rcm-rail-btn'), function (b) { b.classList.remove('is-on'); });
      if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
    }

    rail.addEventListener('click', function (e) {
      var b = e.target.closest('.rcm-rail-btn'); if (!b) return;
      var k = b.getAttribute('data-tab');
      if (isOpen() && current === k) close(); else open(k);
    });
    dr.addEventListener('click', function (e) {
      var t = e.target.closest('.rcm-tab'); if (t) { select(t.getAttribute('data-tab')); return; }
      if (e.target.closest('.rcm-close')) { close(); return; }
      var jump = e.target.closest('#rcm-pane-score a[href^="#"]');
      if (jump) close(); // e.g. "View evidence" -> let the page scroll to that section
    });
    dr.addEventListener('keydown', function (e) {
      var t = e.target.closest('.rcm-tab'); if (!t || (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft')) return;
      var all = Array.prototype.slice.call(dr.querySelectorAll('.rcm-tab'));
      var i = all.indexOf(t) + (e.key === 'ArrowRight' ? 1 : -1);
      var nx = all[(i + all.length) % all.length]; select(nx.getAttribute('data-tab')); nx.focus();
    });
    scrim.addEventListener('click', close);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && isOpen()) close(); });

    // Links into the (hidden) references / glossary open the drawer on that item.
    document.addEventListener('click', function (e) {
      if (!MQ.matches) return;
      var a = e.target.closest('a[href^="#"]'); if (!a || a.closest('.rcm-drawer')) return;
      var id = decodeURIComponent(a.getAttribute('href').slice(1)); if (!id) return;
      var target = document.getElementById(id);
      var m = /^ref-?(\d+)$/i.exec(id);
      if (!target && m && refSec) { // citation link with no matching anchor: open reference N
        e.preventDefault();
        open('refs', dr.querySelectorAll('#rcm-pane-refs ol > li')[+m[1] - 1] || null);
        return;
      }
      if (!target) return;
      var sec = target.closest('.ref-section, .glossary-section');
      if (!sec) return;
      e.preventDefault();
      if (sec === refSec) {
        var li = target.closest('li'), hit = null;
        if (li) {
          var idx = Array.prototype.indexOf.call(refSec.querySelectorAll('ol > li'), li);
          hit = dr.querySelectorAll('#rcm-pane-refs ol > li')[idx] || null;
        }
        open('refs', hit);
      } else if (glossSec && sec === glossSec) {
        open('gloss');
      }
    });

    // The Scorecard tab follows the guide's audience tab: shown only while the
    // clinician card itself is visible (Clinicians mode / clinician-only guides).
    function syncScore() {
      if (!scoreCard) return;
      var on = scoreCard.getClientRects().length > 0;
      var rb = rail.querySelector('[data-tab="score"]'), tb = dr.querySelector('#rcm-tab-score');
      if (rb) rb.style.display = on ? '' : 'none';
      if (tb) tb.style.display = on ? '' : 'none';
      if (!on && current === 'score') { var first = tabs.filter(function (t) { return t.k !== 'score'; })[0]; if (first) select(first.k); else close(); }
    }
    if (scoreCard && window.MutationObserver) {
      new MutationObserver(function () { syncScore(); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });
    }
    function apply() {
      document.documentElement.classList.toggle('rcm-rail-on', MQ.matches);
      if (!MQ.matches && isOpen()) close();
      syncScore();
    }
    apply();
    if (MQ.addEventListener) MQ.addEventListener('change', apply); else MQ.addListener(apply);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
