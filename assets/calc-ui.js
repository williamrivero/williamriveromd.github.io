/* Calculator UI layer (Nov 18 2026), paired with assets/calc-ui.css. Loaded on every calculator page by
   build_calc_app.py as a fingerprinted copy (assets/calc-ui.<hash>.js). Adds, without touching any
   calculator's own logic:
   1. a single Units row (consecutive .unit-toggle-wrap blocks grouped into .cu-units);
   2. a folded "Formula, sources & limitations" note for long .calc-disclaimer paragraphs;
   3. collapsible calculators on pages with two or more: each shows only its numbered title until tapped
      (a #hash link, or "Expand all", opens them);
   4. a "Sample data" button per calculator that fills the empty-looking fields with the page's own
      example values (the "e.g." placeholders), marks them amber, and a "Clear" button that restores
      the previous values. Sample values are never saved to the shared patient store
      (wgmr-rx-patient, assets/calc-handoff.js). Vanilla JS, no dependencies. */
(function () {
  'use strict';
  var d = document, KEY = 'wgmr-rx-patient';
  function $$(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function vis(e) { return !!(e && e.getClientRects().length); }
  // Calculator units: the standard cards, plus pages built with their own tool boxes (ketoanalogue plan
  // check, magnesium replacement) and any box marked data-calc-unit (dialysis prescription).
  var UNIT = '.calc-wrap, .calc-card, .kapc-tool, .mgc-panel, [data-calc-unit]';
  var CHEV = '<svg class="cx-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>';
  var ICON_SAMPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-2.5L14 9V3"/><path d="M7 15h10"/></svg>';
  var ICON_CLEAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>';

  function init() {
    var main = d.querySelector('main') || d.body;
    var units = $$(UNIT, main).filter(function (u) {
      return !u.parentElement.closest(UNIT);
    });

    // 1. Units row
    units.forEach(function (u) {
      var run = [];
      Array.prototype.slice.call(u.children).concat([null]).forEach(function (c) {
        if (c && c.classList.contains('unit-toggle-wrap')) { run.push(c); return; }
        if (run.length > 1) {
          var row = d.createElement('div'); row.className = 'cu-units';
          run[0].parentNode.insertBefore(row, run[0]);
          run.forEach(function (x) { row.appendChild(x); });
        }
        run = [];
      });
    });

    // 2. Folded formula / sources note
    $$('p.calc-disclaimer', main).forEach(function (p) {
      if (p.closest('details') || (p.textContent || '').length < 140) return;
      var det = d.createElement('details'); det.className = 'cu-fine';
      det.innerHTML = '<summary>Formula, sources &amp; limitations</summary>';
      p.parentNode.insertBefore(det, p); det.appendChild(p);
    });
    window.addEventListener('beforeprint', function () {
      $$('details.cu-fine').forEach(function (x) { x.setAttribute('open', ''); });
    });

    // 4. Sample data (before collapsing, so the bar sits inside each card)
    var roots = units.length ? units : $$('#calculator, #toolkit', main).slice(0, 1);
    roots.forEach(addSample);

    // 3. Collapse
    if (units.length > 1) collapse(main, units);
  }

  /* ── Collapsible calculators ─────────────────────────────────────────── */
  function collapse(main, units) {
    var heads = $$('h2, h3', main).filter(function (h) { return !h.closest(UNIT + ', .cx-unit'); });
    var made = [];
    units.forEach(function (u, i) {
      var prev = units[i - 1], h = null;
      // A non-standard box that opens with its own heading (h2/h3) is titled by it, not by a heading above it.
      var own = !u.matches('.calc-wrap, .calc-card') && u.firstElementChild && /^H[23]$/.test(u.firstElementChild.tagName) ? u.firstElementChild : null;
      if (!own) heads.forEach(function (x) {
        var before = x.compareDocumentPosition(u) & Node.DOCUMENT_POSITION_FOLLOWING;
        var afterPrev = !prev || (prev.compareDocumentPosition(x) & Node.DOCUMENT_POSITION_FOLLOWING);
        if (before && afterPrev) h = x;
      });
      var top = u;
      if (h) { while (top.parentNode && top.parentNode !== h.parentNode) top = top.parentNode; }
      if (!h || top.parentNode !== h.parentNode) { h = null; top = u; }
      var box = d.createElement('div'); box.className = 'cx-unit';
      var head;
      if (h) {
        head = h;
        h.parentNode.insertBefore(box, h);
        var body = d.createElement('div'); body.className = 'cx-body';
        var n = h.nextSibling;
        box.appendChild(h); box.appendChild(body);
        while (n) { var nx = n.nextSibling; body.appendChild(n); if (n === top) break; n = nx; }
      } else if (own) {
        head = own;
        $$('.mgc-step', own).forEach(function (x) { x.remove(); });
        // drop a hand-typed number ("1 — spKt/V") since the index adds its own
        if (own.firstChild && own.firstChild.nodeType === 3) own.firstChild.nodeValue = own.firstChild.nodeValue.replace(/^\s*\d+\s*[—–·.-]\s*/, '');
        own.style.color = ''; own.style.margin = '';
        u.parentNode.insertBefore(box, u);
        var b3 = d.createElement('div'); b3.className = 'cx-body';
        box.appendChild(own); box.appendChild(b3); b3.appendChild(u);
      } else {
        head = d.createElement('h3');
        var lead = u.querySelector('h3, h4, .calc-title');
        head.textContent = lead ? lead.textContent : 'Calculator ' + (i + 1);
        u.parentNode.insertBefore(box, u);
        var b2 = d.createElement('div'); b2.className = 'cx-body';
        box.appendChild(head); box.appendChild(b2); b2.appendChild(u);
      }
      var title = d.createElement('span'); title.className = 'cx-title';
      while (head.firstChild) title.appendChild(head.firstChild);
      head.classList.add('cx-head');
      head.setAttribute('role', 'button'); head.setAttribute('tabindex', '0'); head.setAttribute('aria-expanded', 'false');
      head.innerHTML = '<span class="cx-num">' + (i + 1) + '</span>';
      head.appendChild(title); head.insertAdjacentHTML('beforeend', CHEV);
      if (head.id && !box.id) { box.id = head.id; head.removeAttribute('id'); }
      head.addEventListener('click', function () { toggle(box); });
      head.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(box); }
      });
      made.push(box);
    });

    var bar = d.createElement('div'); bar.className = 'cx-bar';
    bar.innerHTML = '<span>' + made.length + ' calculators · tap one to open</span><button type="button">Expand all</button>';
    made[0].parentNode.insertBefore(bar, made[0]);
    var btn = bar.querySelector('button');
    btn.addEventListener('click', function () {
      var open = !made.every(function (b) { return b.classList.contains('cx-open'); });
      made.forEach(function (b) { set(b, open); });
    });
    function sync() {
      btn.textContent = made.every(function (b) { return b.classList.contains('cx-open'); }) ? 'Collapse all' : 'Expand all';
    }
    function set(b, open) {
      b.classList.toggle('cx-open', open);
      b.querySelector('.cx-head').setAttribute('aria-expanded', open ? 'true' : 'false');
      sync();
    }
    function toggle(b) { set(b, !b.classList.contains('cx-open')); }
    function openFor(hash) {
      if (!hash || hash.length < 2) return;
      var t; try { t = d.getElementById(decodeURIComponent(hash.slice(1))); } catch (e) { return; }
      if (!t) return;
      var hit = made.filter(function (b) { return b === t || b.contains(t) || t.contains(b); });
      if (!hit.length) return;
      hit.forEach(function (b) { set(b, true); });
      setTimeout(function () { (t.contains(hit[0]) ? hit[0] : t).scrollIntoView({ block: 'start' }); }, 30);
    }
    openFor(location.hash);
    window.addEventListener('hashchange', function () { openFor(location.hash); });
    d.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (a) openFor(a.getAttribute('href'));
    });
    window.addEventListener('beforeprint', function () { made.forEach(function (b) { set(b, true); }); });
  }

  /* ── Sample data ─────────────────────────────────────────────────────── */
  function exampleOf(inp) {
    var p = (inp.getAttribute('placeholder') || '').trim().replace(/\u2212/g, '-').replace(/^e\.g\.\s*\+/i, 'e.g. '), m;
    if ((m = p.match(/^(?:e\.?\s?g\.?|eg|ex\.?)[:\s]*(-?[\d,]*\.?\d+)/i))) return m[1].replace(/,/g, '');
    if (/^-?\d+(\.\d+)?$/.test(p) && Number(p) !== 0) return p;   // a bare 0 is a default, not an example
    return null;
  }
  function fields(root) {
    var out = [], dates = [], defSel = [];
    $$('input, select', root).forEach(function (e) {
      if (e.disabled || e.readOnly || !vis(e)) return;
      if (e.closest('.cs-bar')) return;
      var t = (e.type || '').toLowerCase();
      if (e.tagName === 'SELECT') {
        var opts = Array.prototype.slice.call(e.options).filter(function (o) { return o.value !== '' && !o.disabled; });
        var mid = opts.length ? opts[opts.length > 2 ? Math.floor((opts.length - 1) / 2) : 0].value : null;
        if (e.value === '' && mid != null) out.push({ el: e, v: mid });
        else if (mid != null && opts.length > 2 && e.selectedIndex <= 0 && e.value !== mid) defSel.push({ el: e, v: mid });
      } else if (t === 'number' || t === 'text' || t === 'tel' || t === '') {
        var v = exampleOf(e); if (v != null) out.push({ el: e, v: v });
      } else if (t === 'date' && !e.value) {
        dates.push(e);
      } else if (t === 'radio') {
        var g = e.name && root.querySelectorAll('input[type=radio][name="' + e.name + '"]');
        if (g && !Array.prototype.some.call(g, function (r) { return r.checked; }) && g[0] === e) out.push({ el: e, radio: true });
      }
    });
    // dates: today, except a baseline / earlier / start date, which gets one year ago
    dates.forEach(function (e) {
      var lab = ((e.closest('.calc-field') || e.parentNode).textContent || '') + ' ' + e.id;
      var dt = new Date();
      if (/baseline|previous|prior|earlier|first|start|initial|creat|old/i.test(lab)) dt.setFullYear(dt.getFullYear() - 1);
      var pad = function (n) { return (n < 10 ? '0' : '') + n; };
      out.push({ el: e, v: dt.getFullYear() + '-' + pad(dt.getMonth() + 1) + '-' + pad(dt.getDate()) });
    });
    // score-type calculators (no numbers to fill): move pre-set selects to a middle answer
    if (!out.some(function (f) { return f.el.tagName === 'INPUT'; })) out = out.concat(defSel);
    if (!out.length) {
      $$('input[type=checkbox]', root).filter(vis).slice(0, 2).forEach(function (c) { if (!c.checked) out.push({ el: c, check: true }); });
    }
    return out;
  }
  function fire(e) {
    e.dispatchEvent(new Event('input', { bubbles: true }));
    e.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function runButton(root) {
    var b = $$('button, input[type=button], input[type=submit]', root).filter(function (x) {
      return vis(x) && /\b(calculate|compute|run|estimate|assess|score|check|interpret|analy[sz]e|evaluate|predict|classify|plot|generate|get|recommend|recommendation|decide)\b/i.test(x.textContent || x.value || '') &&
        !/\b(reset|clear|print|pdf|copy|share)\b/i.test(x.textContent || x.value || '') && !x.closest('.cs-bar');
    })[0];
    if (b) b.click();
  }
  function addSample(root) {
    if (!fields(root).length) return;
    // planners built around many dates (catheter timelines, intervention logs) have no meaningful sample
    if ($$('input[type=date]', root).length > 3) return;
    // the page already offers its own worked examples
    if ($$('button', root).some(function (b) { return /^\s*(example|sample|try an example|load example)/i.test(b.textContent || ''); })) return;
    var bar = d.createElement('div'); bar.className = 'cs-bar';
    bar.innerHTML = '<span class="cs-note" hidden>Sample values, not a real patient</span>' +
      '<button type="button" class="cs-btn cs-fill" title="Fill this calculator with example values">' + ICON_SAMPLE + 'Sample data</button>' +
      '<button type="button" class="cs-btn cs-clear" hidden>' + ICON_CLEAR + 'Clear sample</button>';
    // in a card: at the top; in a plain section: just above the first block that holds a field
    var at = root.firstChild;
    if (!root.matches('.calc-wrap, .calc-card')) {
      at = Array.prototype.slice.call(root.children).filter(function (c) { return c.querySelector('input, select'); })[0] || root.firstChild;
    }
    root.insertBefore(bar, at);
    var fillBtn = bar.querySelector('.cs-fill'), clr = bar.querySelector('.cs-clear'), note = bar.querySelector('.cs-note');
    var marked = [];
    fillBtn.addEventListener('click', function () {
      var keep = null; try { keep = localStorage.getItem(KEY); } catch (e) {}
      var list = fields(root), round = 0;
      // fill in two passes: a select can reveal more fields
      while (list.length && round < 3) {
        list.forEach(function (f) {
          var e = f.el;
          if (f.radio || f.check) { marked.push({ el: e, prevChecked: e.checked }); e.checked = true; }
          else { marked.push({ el: e, prev: e.value }); e.value = f.v; }
          e.setAttribute('data-rcm-sample', '');
          fire(e);
        });
        round++; list = fields(root).filter(function (f) { return !f.el.hasAttribute('data-rcm-sample'); });
      }
      runButton(root);
      try { if (keep == null) localStorage.removeItem(KEY); else localStorage.setItem(KEY, keep); } catch (e) {}
      clr.hidden = false; note.hidden = false; fillBtn.hidden = true;
    });
    clr.addEventListener('click', function () {
      var keep = null; try { keep = localStorage.getItem(KEY); } catch (e) {}
      marked.reverse().forEach(function (m) {
        if (!m.el.hasAttribute('data-rcm-sample')) return;
        if ('prevChecked' in m) m.el.checked = m.prevChecked; else m.el.value = m.prev;
        m.el.removeAttribute('data-rcm-sample'); fire(m.el);
      });
      marked = [];
      runButton(root);
      try { if (keep == null) localStorage.removeItem(KEY); else localStorage.setItem(KEY, keep); } catch (e) {}
      clr.hidden = true; note.hidden = true; fillBtn.hidden = false;
    });
    // a field the user edits is theirs again
    root.addEventListener('input', function (e) { if (e.isTrusted && e.target.removeAttribute) e.target.removeAttribute('data-rcm-sample'); }, true);
    root.addEventListener('change', function (e) { if (e.isTrusted && e.target.removeAttribute) e.target.removeAttribute('data-rcm-sample'); }, true);
  }

  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init); else init();
})();
