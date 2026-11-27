/* Renal Care Academy: preceptor sign-off on the learner's device (Nov 27 2026, Dr. Rivero).
   Every skills checklist (module "Skills checklist" / "With your preceptor" lists, and the trainer and
   educator pages' printable tables) can be completed on the learner's phone: the learner hands the phone
   to the preceptor, who starts a sign-off with their initials and the date, taps a rating for each step
   (each tap is stamped with those initials and that date), and signs the checklist off. Critical steps
   must all be at the passing rating before sign-off. The record can be printed or shared as text.

   Storage: localStorage only, key rcm-skills:<track>/<NN>|<scale> (module page and trainer page share
   one record for the same module), else rcm-skills:<page>#<heading>|<scale>. No account, no network,
   works offline. A device-local study record, not tamper-proof: the unit's competency form is the
   authority (said on screen).

   Source file: edit assets/academy-skills.js, then run tools/academy/apply_skills.py, which writes the
   fingerprinted copy (assets/academy-skills.<hash>.js) and tags every academy page with a checklist.
   Never link the unhashed file. */
(function () {
  'use strict';
  if (window.__rcmSkills) return;
  window.__rcmSkills = true;

  var ROOT = document.querySelector('main.container') || document.querySelector('main') || document.body;
  var LS = null;
  try { LS = window.localStorage; LS.setItem('rcm-sk-test', '1'); LS.removeItem('rcm-sk-test'); } catch (e) { LS = null; }
  if (!LS) return;

  var PREFIX = 'rcm-skills:';
  var FILE = (location.pathname.split('/').pop() || 'index').replace(/\.html$/, '') || 'index';
  var MOD = FILE.match(/^(.+?)-(\d\d)-/);
  var TRACK = MOD ? MOD[1] : FILE.replace(/-(trainer|educator)$/, '');
  var IDLE_MS = 15 * 60 * 1000;     // preceptor mode ends after 15 minutes without a tap
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  /* ── Helpers ─────────────────────────────────────────────────────────── */
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function btn(cls, text, act, extra) {
    var b = el('button', 'rcm-sk-btn ' + (cls || ''), text);
    b.type = 'button';
    b.setAttribute('data-sk', act);
    if (extra) for (var k in extra) b.setAttribute(k, extra[k]);
    return b;
  }
  function norm(s) { return (s || '').replace(/\s+/g, ' ').trim(); }
  function words(s) { return norm(s).toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').split(' ').filter(function (w) { return w.length > 2; }); }
  function similar(a, b) {
    if (norm(a).toLowerCase() === norm(b).toLowerCase()) return true;
    var A = words(a), B = words(b);
    if (!A.length || !B.length) return false;
    var small = A.length <= B.length ? A : B, big = A.length <= B.length ? B : A, hit = 0;
    small.forEach(function (w) { if (big.indexOf(w) >= 0) hit++; });
    return hit / small.length >= 0.8 && small.length / big.length >= 0.5;
  }
  function slug(s) { return norm(s).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60); }
  function today() {
    var d = new Date();
    return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
  }
  function fmtDate(iso) {                       // American style: Nov 27, 2026
    var m = /^(\d{4})-(\d\d)-(\d\d)$/.exec(iso || '');
    return m ? MONTHS[+m[2] - 1] + ' ' + (+m[3]) + ', ' + m[1] : (iso || '');
  }
  function fmtShort(iso) {                      // 11/27/26
    var m = /^(\d{4})-(\d\d)-(\d\d)$/.exec(iso || '');
    return m ? (+m[2]) + '/' + (+m[3]) + '/' + m[1].slice(2) : (iso || '');
  }
  function cleanInitials(s) { return norm(s).replace(/[^A-Za-z.\- ]/g, '').toUpperCase().slice(0, 8); }
  function validDate(iso) {
    if (!/^\d{4}-\d\d-\d\d$/.test(iso || '')) return false;
    var t = Date.parse(iso + 'T00:00:00');
    return !isNaN(t) && t <= Date.now() + 36e5 * 24 && t > Date.parse('2020-01-01T00:00:00');
  }
  function stepText(cell) {
    var c = cell.cloneNode(true);
    Array.prototype.forEach.call(c.querySelectorAll('.tc-crit,.rcm-sk-ui,.rcn-ui,sup'), function (n) { n.remove(); });
    return norm(c.textContent);
  }
  function pageTitle() {
    var h = document.querySelector('.hero h1') || document.querySelector('h1');
    return norm(h ? h.textContent : document.title);
  }
  function toast(msg) {
    var t = document.querySelector('.rcm-sk-toast');
    if (!t) { t = el('div', 'rcm-sk-ui rcn-ui rcm-sk-toast no-print'); t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg;
    t.classList.add('on');
    clearTimeout(toast.t);
    toast.t = setTimeout(function () { t.classList.remove('on'); }, 3200);
  }

  /* ── Rating scales ───────────────────────────────────────────────────── */
  var SAT = [{ l: 'Satisfactory', ic: '✓', pass: true, tone: 'ok' }, { l: 'Needs practice', ic: '↻', tone: 'warn' }, { l: 'Not observed', ic: '–', tone: 'off' }];
  var SIGN = [{ l: 'Signed off', ic: '✓', pass: true, tone: 'ok' }, { l: 'Needs practice', ic: '↻', tone: 'warn' }];

  function tableSpec(table) {
    var ths = table.querySelectorAll('thead th');
    if (ths.length < 2 || !table.querySelector('tbody tr')) return null;
    var labs = Array.prototype.slice.call(ths, 1).map(function (th) { return norm(th.textContent); });
    var low = labs.map(function (s) { return s.toLowerCase(); });
    if (low[0] === 'satisfactory') {
      var opts = [];
      for (var i = 0; i < low.length; i++) {
        var o = SAT.filter(function (s) { return s.l.toLowerCase() === low[i]; })[0];
        if (!o) return null;
        opts.push(Object.assign({ col: i + 1 }, o));
      }
      return { id: 'sat', kind: 'rate', opts: opts };
    }
    if (low.length === 2 && low[0] === 'done' && low[1] === 'not done') {
      return { id: 'done', kind: 'rate', opts: [{ l: 'Done', ic: '✓', pass: true, tone: 'ok', col: 1 }, { l: 'Not done', ic: '✗', tone: 'warn', col: 2 }] };
    }
    if (low.every(function (s) { return /^\d+$/.test(s); })) {
      var max = Math.max.apply(null, low.map(Number));
      return {
        id: 'n' + low.join(''), kind: 'rate', scored: true,
        opts: low.map(function (s, k) { var v = +s; return { l: 'Score ' + s, short: s, ic: s, pass: v === max, tone: v === max ? 'ok' : (v === 0 ? 'off' : 'warn'), col: k + 1 }; })
      };
    }
    if (low.some(function (s) { return /date,\s*initials/.test(s); })) {
      return {
        id: 'cols', kind: 'cols',
        cols: low.map(function (s, k) {
          return { col: k + 1, l: labs[k].replace(/\s*\(date,\s*initials\)\s*/i, ''), kind: /date,\s*initials/.test(s) ? 'stamp' : (/comment|note/.test(s) ? 'note' : 'skip') };
        })
      };
    }
    return null;
  }
  function listSpec(ul) {
    var sec = ul.closest('section');
    var txt = sec ? sec.textContent.toLowerCase() : '';
    return /satisfactory/.test(txt) ? { id: 'sat', kind: 'rate', opts: SAT.map(function (o, k) { return Object.assign({ col: k }, o); }) }
                                    : { id: 'sign', kind: 'rate', opts: SIGN.map(function (o, k) { return Object.assign({ col: k }, o); }) };
  }

  function headingFor(node) {
    for (var n = node; n && n !== ROOT; n = n.parentElement) {
      for (var p = n.previousElementSibling; p; p = p.previousElementSibling) {
        if (/^H[2-4]$/.test(p.tagName)) return p;
        if (p.classList && (p.classList.contains('table-wrap') || p.tagName === 'UL' || p.tagName === 'TABLE')) break;   // the previous checklist's territory
      }
      if (n.tagName === 'SECTION') { var h = n.querySelector('h2,h3'); return h || null; }
    }
    return null;
  }

  /* ── Find the checklists ─────────────────────────────────────────────── */
  var lists = [];
  var usedBases = {};
  function addList(node, kind, spec) {
    var host = kind === 'table' && node.parentElement && node.parentElement.classList.contains('table-wrap') ? node.parentElement : node;
    var rows = kind === 'ul' ? Array.prototype.slice.call(node.children).filter(function (c) { return c.tagName === 'LI'; })
                             : Array.prototype.slice.call(node.querySelectorAll('tbody tr')).filter(function (tr) { return tr.children.length > 1; });
    if (!rows.length) return;
    var h = headingFor(host);
    var title = h ? norm(h.textContent) : pageTitle();
    var base, mm;
    if (MOD) base = TRACK + '/' + MOD[2];
    else if ((mm = /^Module\s+(\d+)\b/i.exec(title))) base = TRACK + '/' + ('0' + mm[1]).slice(-2);
    else base = FILE + '#' + (slug(title) || 'checklist');
    if (usedBases[base + spec.id]) base += '-' + (++usedBases[base + spec.id]); else usedBases[base + spec.id] = 1;
    var steps = rows.map(function (r) {
      var first = kind === 'ul' ? r : r.children[0];
      return { row: r, text: stepText(first), crit: !!first.querySelector('.tc-crit') };
    });
    var L = { node: node, host: host, kind: kind, spec: spec, steps: steps, title: title, key: PREFIX + base + '|' + spec.id, n: lists.length };
    L.critCount = steps.filter(function (s) { return s.crit; }).length;
    lists.push(L);
  }
  Array.prototype.forEach.call(ROOT.querySelectorAll('ul.nc-check'), function (ul) { addList(ul, 'ul', listSpec(ul)); });
  Array.prototype.forEach.call(ROOT.querySelectorAll('table'), function (t) {
    var head = t.tHead ? t.tHead.textContent : '';
    if (!(t.classList.contains('nc-sign') || t.querySelector('tr.nc-sign') || /date,\s*initials/i.test(head))) return;
    var s = tableSpec(t);
    if (s) addList(t, 'table', s);
  });
  if (!lists.length) return;

  /* ── Storage ─────────────────────────────────────────────────────────── */
  function blank() { return {}; }
  function load(L) {
    var rec;
    try { rec = JSON.parse(LS.getItem(L.key) || 'null'); } catch (e) { rec = null; }
    rec = rec && typeof rec === 'object' ? rec : {};
    var saved = Array.isArray(rec.steps) ? rec.steps.slice() : [];
    var used = [], out = L.steps.map(function () { return null; });
    // 1) same or nearly the same wording (module page and trainer page word a few steps differently)
    L.steps.forEach(function (s, i) {
      for (var k = 0; k < saved.length; k++) {
        if (used.indexOf(k) < 0 && saved[k] && similar(saved[k].t, s.text)) { out[i] = saved[k]; used.push(k); return; }
      }
    });
    // 2) same number of steps: what is left keeps its place, flagged as reworded
    if (saved.length === L.steps.length) {
      out.forEach(function (o, i) {
        if (!o && used.indexOf(i) < 0 && saved[i] && hasData(saved[i])) { out[i] = Object.assign({}, saved[i], { chg: 1 }); used.push(i); }
      });
    }
    L.orphans = (Array.isArray(rec.orphans) ? rec.orphans : []).concat(saved.filter(function (s, k) { return used.indexOf(k) < 0 && s && hasData(s); }));
    L.data = out.map(function (o) { return o || blank(); });
    L.sign = rec.sign && rec.sign.by ? rec.sign : null;
    L.learner = rec.learner || '';
  }
  function hasData(s) { return s && (s.r != null || (s.c && Object.keys(s.c).length) || s.n); }
  function anyData(L) { return !!L.sign || L.data.some(hasData) || (L.orphans && L.orphans.length); }
  function persist(L) {
    try {
      if (!anyData(L)) { LS.removeItem(L.key); return true; }
      var steps = L.data.map(function (d, i) { var o = Object.assign({}, d, { t: L.steps[i].text }); return o; });
      LS.setItem(L.key, JSON.stringify({
        v: 1, title: L.title, page: pageTitle(), url: location.pathname, scale: L.spec.id,
        steps: steps, orphans: L.orphans && L.orphans.length ? L.orphans : undefined,
        sign: L.sign || undefined, learner: L.learner || undefined, upd: Date.now()
      }));
      return true;
    } catch (e) {
      toast('Could not save: this browser’s storage is full or blocked.');
      return false;
    }
  }
  function refresh(L) { load(L); render(L); }
  lists.forEach(load);

  // Another tab (the trainer page open beside the module) changed a record: show it here too.
  window.addEventListener('storage', function (e) {
    if (!e.key || e.key.indexOf(PREFIX) !== 0) return;
    lists.forEach(function (L) { if (L.key === e.key) refresh(L); });
  });

  /* ── Preceptor mode ──────────────────────────────────────────────────── */
  var session = null;    // { n: list index, by: initials, d: ISO date, at: last tap }
  var ui = {};           // per-list transient panel state: 'start' | 'sign' | 'clear'
  function active(L) { return session && session.n === L.n; }
  function touch() { if (session) session.at = Date.now(); }
  function endSession(msg) {
    if (!session) return;
    var L = lists[session.n];
    session = null;
    render(L);
    if (msg) toast(msg);
  }
  setInterval(function () { if (session && Date.now() - session.at > IDLE_MS) endSession('Preceptor mode ended after 15 minutes without a tap.'); }, 30000);
  document.addEventListener('visibilitychange', function () {
    if (!document.hidden && session && Date.now() - session.at > IDLE_MS) endSession('Preceptor mode ended after 15 minutes without a tap.');
  });

  /* ── Status ──────────────────────────────────────────────────────────── */
  function rated(L, i) {
    var d = L.data[i];
    return L.spec.kind === 'cols' ? !!(d.c && Object.keys(d.c).length) : d.r != null;
  }
  function passed(L, i) {
    var d = L.data[i];
    if (L.spec.kind === 'cols') return rated(L, i);
    var o = d.r != null && L.spec.opts[d.r];
    return !!(o && o.pass);
  }
  function critLeft(L) {
    var out = [];
    L.steps.forEach(function (s, i) { if (s.crit && !passed(L, i)) out.push(i); });
    return out;
  }
  function notPassed(L) {
    var out = [];
    L.steps.forEach(function (s, i) { if (!passed(L, i)) out.push(i); });
    return out;
  }
  function statusText(L) {
    var n = L.steps.length, r = 0;
    L.steps.forEach(function (s, i) { if (rated(L, i)) r++; });
    var t = r + ' of ' + n + ' step' + (n === 1 ? '' : 's') + (L.spec.kind === 'cols' ? ' signed' : ' rated');
    var c = critLeft(L).length;
    if (L.critCount && L.spec.kind !== 'cols') t += c ? ' · ' + c + ' critical step' + (c === 1 ? '' : 's') + ' still to pass' : ' · all critical steps passed';
    return t;
  }
  function optLabel(L, r) { var o = L.spec.opts[r]; return o ? o.l : ''; }

  /* ── Rendering ───────────────────────────────────────────────────────── */
  function clearUI(L) {
    Array.prototype.forEach.call(L.host.parentNode.querySelectorAll('.rcm-sk-panel[data-n="' + L.n + '"]'), function (p) { p.remove(); });
    Array.prototype.forEach.call(L.node.querySelectorAll('.rcm-sk-ui'), function (p) { p.remove(); });
    L.steps.forEach(function (s) { s.row.classList.remove('rcm-sk-ok', 'rcm-sk-warn', 'rcm-sk-off', 'rcm-sk-live'); });
    L.node.classList.remove('rcm-sk-on', 'rcm-sk-signed');
  }

  function render(L) {
    clearUI(L);
    var live = active(L) && !L.sign;
    if (active(L)) L.node.classList.add('rcm-sk-on');
    if (L.sign) L.node.classList.add('rcm-sk-signed');
    L.host.parentNode.insertBefore(panel(L), L.host);
    L.steps.forEach(function (s, i) {
      var d = L.data[i];
      if (live) s.row.classList.add('rcm-sk-live');
      if (L.spec.kind === 'rate' && d.r != null && L.spec.opts[d.r]) s.row.classList.add('rcm-sk-' + L.spec.opts[d.r].tone);
      if (L.kind === 'ul') renderListStep(L, s, i, live);
      else if (L.spec.kind === 'rate') renderRateRow(L, s, i, live);
      else renderColsRow(L, s, i, live);
    });
  }

  function stampText(by, d, short) { return [by, short ? fmtShort(d) : fmtDate(d)].filter(Boolean).join(' · '); }

  function renderListStep(L, s, i, live) {
    var d = L.data[i];
    var box = el('div', 'rcm-sk-ui rcn-ui rcm-sk-step');
    if (live) {
      var g = el('div', 'rcm-sk-seg');
      g.setAttribute('role', 'group');
      g.setAttribute('aria-label', 'Rate step ' + (i + 1));
      g.style.gridTemplateColumns = 'repeat(' + L.spec.opts.length + ',minmax(0,1fr))';
      L.spec.opts.forEach(function (o, k) {
        var b = btn('rcm-sk-opt rcm-sk-t-' + o.tone, '', 'rate', { 'data-n': L.n, 'data-i': i, 'data-r': k, 'aria-pressed': d.r === k ? 'true' : 'false' });
        b.appendChild(el('span', 'rcm-sk-ic', o.ic));
        b.appendChild(el('span', 'rcm-sk-lab', o.l));
        g.appendChild(b);
      });
      box.appendChild(g);
    }
    if (d.r != null) {
      var st = el('div', 'rcm-sk-stamp rcm-sk-t-' + (L.spec.opts[d.r] || {}).tone);
      st.appendChild(el('b', null, optLabel(L, d.r)));
      st.appendChild(document.createTextNode(' · ' + stampText(d.by, d.d)));
      if (d.chg) st.appendChild(el('span', 'rcm-sk-chg', ' (rated when this step was worded differently)'));
      box.appendChild(st);
    }
    if (box.childNodes.length) s.row.appendChild(box);
  }

  function renderRateRow(L, s, i, live) {
    var d = L.data[i];
    L.spec.opts.forEach(function (o, k) {
      var td = s.row.children[o.col];
      if (!td) return;
      var on = d.r === k;
      var wrap = el(live ? 'button' : 'span', 'rcm-sk-ui rcn-ui rcm-sk-cell rcm-sk-t-' + o.tone + (on ? ' on' : ''));
      if (live) {
        wrap.type = 'button';
        wrap.setAttribute('data-sk', 'rate');
        wrap.setAttribute('data-n', L.n); wrap.setAttribute('data-i', i); wrap.setAttribute('data-r', k);
        wrap.setAttribute('aria-pressed', on ? 'true' : 'false');
        wrap.setAttribute('aria-label', o.l + ', step ' + (i + 1));
      }
      if (on) {
        wrap.appendChild(el('span', 'rcm-sk-ic', o.ic));
        wrap.appendChild(el('small', null, stampText(d.by, d.d, true)));
      } else if (live) {
        wrap.appendChild(el('span', 'rcm-sk-ic rcm-sk-ghost', L.spec.scored ? o.short : '○'));
      }
      if (on || live) td.appendChild(wrap);
    });
    if (d.chg) s.row.children[0].appendChild(el('span', 'rcm-sk-ui rcn-ui rcm-sk-chg', ' (rated when this step was worded differently)'));
  }

  function renderColsRow(L, s, i, live) {
    var d = L.data[i];
    L.spec.cols.forEach(function (c) {
      var td = s.row.children[c.col];
      if (!td || c.kind === 'skip') return;
      if (c.kind === 'stamp') {
        var st = d.c && d.c[c.col];
        var w = el(live ? 'button' : 'span', 'rcm-sk-ui rcn-ui rcm-sk-cell rcm-sk-t-ok' + (st ? ' on' : ''));
        if (live) {
          w.type = 'button';
          w.setAttribute('data-sk', 'stamp');
          w.setAttribute('data-n', L.n); w.setAttribute('data-i', i); w.setAttribute('data-c', c.col);
          w.setAttribute('aria-pressed', st ? 'true' : 'false');
          w.setAttribute('aria-label', c.l + ', step ' + (i + 1));
        }
        if (st) { w.appendChild(el('span', 'rcm-sk-ic', '✓')); w.appendChild(el('small', null, stampText(st.by, st.d, true))); }
        else if (live) w.appendChild(el('span', 'rcm-sk-ic rcm-sk-ghost', '○'));
        if (st || live) td.appendChild(w);
      } else if (c.kind === 'note') {
        if (live) {
          var ta = el('textarea', 'rcm-sk-ui rcn-ui rcm-sk-note');
          ta.rows = 2; ta.value = d.n || '';
          ta.setAttribute('data-n', L.n); ta.setAttribute('data-i', i);
          ta.setAttribute('aria-label', 'Preceptor comment, step ' + (i + 1));
          ta.maxLength = 300;
          td.appendChild(ta);
        } else if (d.n) {
          var p = el('span', 'rcm-sk-ui rcn-ui rcm-sk-notetext', d.n);
          if (d.nby) p.appendChild(el('small', null, ' (' + stampText(d.nby, d.nd, true) + ')'));
          td.appendChild(p);
        }
      }
    });
  }

  function panel(L) {
    var p = el('div', 'rcm-sk-ui rcn-ui rcm-sk-panel' + (active(L) ? ' rcm-sk-pmode' : ''));
    p.setAttribute('data-n', L.n);
    p.setAttribute('aria-live', 'polite');
    var head = el('div', 'rcm-sk-head');
    head.appendChild(el('span', 'rcm-sk-badge', active(L) ? 'Preceptor mode' : 'Sign-off on this device'));
    head.appendChild(el('span', 'rcm-sk-status', statusText(L)));
    p.appendChild(head);
    var row = el('div', 'rcm-sk-row');
    var mode = ui[L.n];

    if (L.sign) {
      var s = el('p', 'rcm-sk-signed-line');
      s.appendChild(el('b', null, '✔ Signed off'));
      s.appendChild(document.createTextNode(' by ' + L.sign.by + ' on ' + fmtDate(L.sign.d) + (L.learner ? ' · Learner: ' + L.learner : '')));
      p.appendChild(s);
    }

    if (active(L)) {
      var who = el('p', 'rcm-sk-who');
      who.appendChild(document.createTextNode('Stamping as '));
      who.appendChild(el('b', null, session.by));
      who.appendChild(document.createTextNode(' on ' + fmtDate(session.d) + '. '));
      who.appendChild(document.createTextNode(L.sign ? 'This checklist is signed off and locked.' :
        (L.spec.kind === 'cols' ? 'Tap a box to stamp it; tap again to remove the stamp.' : 'Tap a rating for each step you observed.')));
      p.appendChild(who);
      if (mode === 'sign' && !L.sign) p.appendChild(signForm(L));
      else {
        if (L.sign) row.appendChild(btn('rcm-sk-quiet', 'Reopen checklist', 'reopen', { 'data-n': L.n }));
        else row.appendChild(btn('rcm-sk-go', 'Sign off checklist', 'signform', { 'data-n': L.n }));
        row.appendChild(btn('', 'Done: hand back to learner', 'end', { 'data-n': L.n }));
        p.appendChild(row);
      }
      return p;
    }

    if (mode === 'start') { p.appendChild(startForm(L)); return p; }
    if (mode === 'clear') {
      var c = el('p', 'rcm-sk-warnline', 'Erase every rating, stamp and sign-off on this checklist from this device? This cannot be undone.');
      p.appendChild(c);
      row.appendChild(btn('rcm-sk-danger', 'Erase', 'clearyes', { 'data-n': L.n }));
      row.appendChild(btn('rcm-sk-quiet', 'Keep it', 'cancel', { 'data-n': L.n }));
      p.appendChild(row);
      return p;
    }
    if (!L.sign) row.appendChild(btn('rcm-sk-go', 'Preceptor: start sign-off', 'startform', { 'data-n': L.n }));
    else row.appendChild(btn('rcm-sk-quiet', 'Preceptor: open', 'startform', { 'data-n': L.n }));
    if (anyData(L)) {
      row.appendChild(btn('', 'Print record', 'print', { 'data-n': L.n }));
      row.appendChild(btn('', navigator.share ? 'Share' : 'Copy as text', 'share', { 'data-n': L.n }));
      row.appendChild(btn('rcm-sk-quiet', 'Clear', 'clear', { 'data-n': L.n }));
    }
    p.appendChild(row);
    var note = el('p', 'rcm-sk-note-line',
      'Hand your phone to your preceptor. Ratings, initials and dates are saved on this device only. This is a study record, not proof: your unit’s competency form is the authority.');
    if (L.orphans && L.orphans.length) note.textContent += ' ' + L.orphans.length + ' earlier rating' + (L.orphans.length === 1 ? ' is' : 's are') + ' kept for steps no longer on this checklist (shown on the printed record).';
    p.appendChild(note);
    return p;
  }

  function startForm(L) {
    var f = el('form', 'rcm-sk-form');
    f.setAttribute('data-n', L.n);
    f.noValidate = true;
    f.innerHTML =
      '<div class="rcm-sk-fields">' +
      '<label>Preceptor initials<input name="by" autocomplete="off" autocapitalize="characters" maxlength="8" required placeholder="e.g. WR"></label>' +
      '<label>Date<input name="d" type="date" required></label>' +
      '</div>' +
      '<label class="rcm-sk-check"><input name="ok" type="checkbox" required> I am the preceptor, and I am observing this learner perform these steps.</label>' +
      '<p class="rcm-sk-err" hidden></p>' +
      '<div class="rcm-sk-row"><button type="submit" class="rcm-sk-btn rcm-sk-go">Start sign-off</button>' +
      '<button type="button" class="rcm-sk-btn rcm-sk-quiet" data-sk="cancel" data-n="' + L.n + '">Cancel</button></div>' +
      '<p class="rcm-sk-note-line">Each tap is stamped with these initials and this date. Preceptor mode ends when you tap Done or after 15 minutes without a tap.</p>';
    f.elements.d.value = today();
    f.elements.d.max = today();
    var last = (function () { try { return LS.getItem('rcm-sk-last') || ''; } catch (e) { return ''; } })();
    if (last) f.elements.by.value = last;
    setTimeout(function () { try { f.elements.by.focus({ preventScroll: true }); } catch (e) {} }, 30);
    return f;
  }

  function signForm(L) {
    var f = el('form', 'rcm-sk-form rcm-sk-signform');
    f.setAttribute('data-n', L.n);
    f.noValidate = true;
    var cl = L.spec.kind === 'cols' ? [] : critLeft(L);
    var html = '';
    if (cl.length) {
      html += '<p class="rcm-sk-warnline"><b>Not yet.</b> Every critical step must be ' + (L.spec.opts.filter(function (o) { return o.pass; })[0] || {}).l + ' before sign-off. Still to pass:</p><ol class="rcm-sk-left">' +
        cl.map(function (i) { return '<li value="' + (i + 1) + '"></li>'; }).join('') + '</ol>' +
        '<div class="rcm-sk-row"><button type="button" class="rcm-sk-btn rcm-sk-quiet" data-sk="cancel" data-n="' + L.n + '">Back to the checklist</button></div>';
      f.innerHTML = html;
      Array.prototype.forEach.call(f.querySelectorAll('.rcm-sk-left li'), function (li, k) { li.textContent = L.steps[cl[k]].text; });
      return f;
    }
    var np = notPassed(L).length;
    html += '<label>Learner name (optional)<input name="learner" autocomplete="off" maxlength="60"></label>';
    if (np) html += '<p class="rcm-sk-warnline">' + np + ' step' + (np === 1 ? ' is' : 's are') + ' not ' + (L.spec.kind === 'cols' ? 'stamped' : 'at the passing rating') + '. ' + (np === 1 ? 'It stays' : 'They stay') + ' on the record as rated.</p>';
    html += '<label class="rcm-sk-check"><input name="ok" type="checkbox" required> I, ' + '<b class="rcm-sk-by"></b>, observed this learner and sign off this checklist on ' + fmtDate(session.d) + '.</label>' +
      '<div class="rcm-sk-row"><button type="submit" class="rcm-sk-btn rcm-sk-go">Sign off</button>' +
      '<button type="button" class="rcm-sk-btn rcm-sk-quiet" data-sk="cancel" data-n="' + L.n + '">Cancel</button></div>';
    f.innerHTML = html;
    f.querySelector('.rcm-sk-by').textContent = session.by;
    f.elements.learner.value = L.learner || '';
    return f;
  }

  // The Personal Study Record (academy-study-record.js) keeps one sign-off date per module in localStorage
  // rcm-skills {track:{NN:"YYYY-MM-DD"}}: an on-device sign-off fills it, so the learner does not type it again.
  function syncStudyRecord(L, oldSign) {
    var m = /^rcm-skills:([^|#]+)\/(\d\d)\|/.exec(L.key);
    if (!m) return;
    var all;
    try { all = JSON.parse(LS.getItem('rcm-skills') || '{}') || {}; } catch (e) { all = {}; }
    var t = all[m[1]] = all[m[1]] || {};
    if (L.sign) t[m[2]] = L.sign.d;
    else if (oldSign && t[m[2]] === oldSign.d) delete t[m[2]];
    else return;
    try { LS.setItem('rcm-skills', JSON.stringify(all)); } catch (e) { return; }
    var box = document.querySelector('.rcm-sr-sign input[type=date]');
    if (box && MOD && m[1] === TRACK && m[2] === MOD[2]) box.value = L.sign ? L.sign.d : '';
  }

  /* ── Actions ─────────────────────────────────────────────────────────── */
  function listOf(t) { var n = +t.getAttribute('data-n'); return lists[n]; }

  ROOT.addEventListener('click', function (e) {
    var b = e.target.closest('[data-sk]');
    if (!b || !ROOT.contains(b)) return;
    var L = listOf(b);
    if (!L) return;
    var act = b.getAttribute('data-sk');
    e.preventDefault();
    if (act === 'rate' || act === 'stamp') {
      if (!active(L) || L.sign) return;
      if (Date.now() - session.at > IDLE_MS) { endSession('Preceptor mode ended after 15 minutes without a tap.'); return; }
      touch();
      var i = +b.getAttribute('data-i'), d = L.data[i];
      if (act === 'rate') {
        var r = +b.getAttribute('data-r');
        if (d.r === r) L.data[i] = {};                             // tap the chosen rating again to clear it
        else L.data[i] = { r: r, by: session.by, d: session.d, at: Date.now() };
      } else {
        var c = b.getAttribute('data-c');
        d.c = d.c || {};
        if (d.c[c]) delete d.c[c]; else d.c[c] = { by: session.by, d: session.d, at: Date.now() };
        delete d.chg;
      }
      persist(L);
      var y = b.getBoundingClientRect().top;
      render(L);
      var nb = L.node.querySelector('[data-sk="' + act + '"][data-i="' + i + '"]');   // keep the row where the finger is
      if (nb) window.scrollBy(0, nb.getBoundingClientRect().top - y);
      return;
    }
    if (act === 'startform') { ui[L.n] = 'start'; render(L); return; }
    if (act === 'cancel') { ui[L.n] = null; render(L); return; }
    if (act === 'end') { ui[L.n] = null; endSession('Preceptor mode ended. Hand the phone back to the learner.'); return; }
    if (act === 'signform') { touch(); ui[L.n] = 'sign'; render(L); return; }
    if (act === 'reopen') {
      touch();
      var was = L.sign;
      L.sign = null; persist(L); syncStudyRecord(L, was); ui[L.n] = null; render(L);
      toast('Checklist reopened. Ratings are kept; sign it off again when ready.');
      return;
    }
    if (act === 'clear') { ui[L.n] = 'clear'; render(L); return; }
    if (act === 'clearyes') {
      var had = L.sign;
      LS.removeItem(L.key); ui[L.n] = null; refresh(L); syncStudyRecord(L, had); toast('Checklist record erased from this device.');
      return;
    }
    if (act === 'print') { printRecord(L); return; }
    if (act === 'share') { shareRecord(L); return; }
  });

  ROOT.addEventListener('submit', function (e) {
    var f = e.target.closest('.rcm-sk-form');
    if (!f) return;
    e.preventDefault();
    var L = listOf(f);
    if (!L) return;
    if (f.classList.contains('rcm-sk-signform')) {
      if (!active(L)) return;
      if (!f.elements.ok.checked) { toast('Tick the box to confirm the sign-off.'); return; }
      if (L.spec.kind !== 'cols' && critLeft(L).length) return;
      touch();
      L.learner = norm(f.elements.learner ? f.elements.learner.value : '').slice(0, 60);
      L.sign = { by: session.by, d: session.d, at: Date.now() };
      persist(L); syncStudyRecord(L); ui[L.n] = null; render(L);
      toast('Signed off. The date is on your Personal Study Record too.');
      return;
    }
    var by = cleanInitials(f.elements.by.value), d = f.elements.d.value, err = f.querySelector('.rcm-sk-err');
    var problem = by.replace(/[^A-Z]/g, '').length < 2 ? 'Enter your initials (at least two letters).'
                : !validDate(d) ? 'Enter today’s date, or the date you observed the learner (not a future date).'
                : !f.elements.ok.checked ? 'Tick the box to confirm you are the preceptor.' : '';
    if (problem) { err.textContent = problem; err.hidden = false; return; }
    try { LS.setItem('rcm-sk-last', by); } catch (x) {}
    var prev = session && lists[session.n];
    session = { n: L.n, by: by, d: d, at: Date.now() };
    ui[L.n] = null;
    if (prev && prev !== L) render(prev);
    render(L);
  });

  ROOT.addEventListener('change', function (e) {
    var ta = e.target.closest && e.target.closest('textarea.rcm-sk-note');
    if (!ta) return;
    var L = listOf(ta);
    if (!L || !active(L) || L.sign) return;
    touch();
    var d = L.data[+ta.getAttribute('data-i')], v = norm(ta.value).slice(0, 300);
    if (v) { d.n = v; d.nby = session.by; d.nd = session.d; } else { delete d.n; delete d.nby; delete d.nd; }
    persist(L);
  });

  /* ── Record: text and print ──────────────────────────────────────────── */
  function rowSummary(L, i) {
    var d = L.data[i];
    if (L.spec.kind === 'cols') {
      var parts = [];
      L.spec.cols.forEach(function (c) { var st = d.c && d.c[c.col]; if (c.kind === 'stamp' && st) parts.push(c.l + ': ' + stampText(st.by, st.d)); });
      if (d.n) parts.push('Comment: ' + d.n);
      return parts.length ? parts.join('; ') : 'Not yet signed';
    }
    return d.r != null ? optLabel(L, d.r) + ' (' + stampText(d.by, d.d) + ')' : 'Not rated';
  }
  function recordText(L) {
    var out = ['Renal Care Academy · Skills checklist', pageTitle(), L.title, location.origin + location.pathname, ''];
    out.push(L.sign ? 'Signed off by ' + L.sign.by + ' on ' + fmtDate(L.sign.d) : 'Not yet signed off (' + statusText(L) + ')');
    if (L.learner) out.push('Learner: ' + L.learner);
    out.push('');
    L.steps.forEach(function (s, i) {
      out.push((i + 1) + '. ' + (s.crit ? '[CRITICAL] ' : '') + s.text);
      out.push('   ' + rowSummary(L, i));
    });
    out.push('', 'Saved on the learner’s device; the unit’s competency form is the authority.');
    return out.join('\n');
  }
  function shareRecord(L) {
    var text = recordText(L);
    if (navigator.share) {
      navigator.share({ title: 'Skills checklist: ' + L.title, text: text }).catch(function () {});
      return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { toast('Record copied. Paste it into a message or email.'); },
        function () { toast('Could not copy. Use Print record instead.'); });
      return;
    }
    toast('Copying is not available here. Use Print record instead.');
  }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function printRecord(L) {
    var old = document.querySelector('.rcm-sk-printout');
    if (old) old.remove();
    var cols = L.spec.kind === 'cols'
      ? L.spec.cols.filter(function (c) { return c.kind !== 'skip'; })
      : [{ l: 'Rating' }, { l: 'Initials' }, { l: 'Date' }];
    var rows = L.steps.map(function (s, i) {
      var d = L.data[i], cells;
      if (L.spec.kind === 'cols') {
        cells = cols.map(function (c) {
          if (c.kind === 'note') return esc(d.n || '');
          var st = d.c && d.c[c.col];
          return st ? '✓ ' + esc(st.by) + ', ' + esc(fmtDate(st.d)) : '';
        });
      } else {
        cells = d.r != null ? [esc(optLabel(L, d.r)), esc(d.by), esc(fmtDate(d.d))] : ['', '', ''];
      }
      return '<tr><td>' + (i + 1) + '</td><td>' + (s.crit ? '<b class="crit">Critical</b> ' : '') + esc(s.text) + '</td><td>' + cells.join('</td><td>') + '</td></tr>';
    }).join('');
    var orph = (L.orphans || []).map(function (o) {
      return '<li>' + esc(o.t) + ': ' + esc(o.r != null ? optLabel(L, o.r) + ' (' + stampText(o.by, o.d) + ')' : 'stamped') + '</li>';
    }).join('');
    var box = el('div', 'rcm-sk-printout');
    box.innerHTML =
      '<p class="k">Renal Care Academy · Skills checklist record</p>' +
      '<h1>' + esc(L.title) + '</h1>' +
      '<p>' + esc(pageTitle()) + '<br>' + esc(location.origin + location.pathname) + '</p>' +
      '<p class="sig">' + (L.sign ? '<b>Signed off</b> by ' + esc(L.sign.by) + ' on ' + esc(fmtDate(L.sign.d)) : '<b>Not yet signed off</b> (' + esc(statusText(L)) + ')') +
      (L.learner ? '<br>Learner: ' + esc(L.learner) : '') + '</p>' +
      '<table><thead><tr><th>#</th><th>Observable step</th><th>' + cols.map(function (c) { return esc(c.l); }).join('</th><th>') + '</th></tr></thead><tbody>' + rows + '</tbody></table>' +
      (orph ? '<p><b>Earlier ratings for steps no longer on this checklist</b></p><ul>' + orph + '</ul>' : '') +
      '<p class="lines">Learner signature ______________________ &nbsp; Preceptor signature ______________________</p>' +
      '<p class="foot">Recorded on the learner’s device (no account). A study record, not proof of competence: the unit’s own competency form is the authority. Printed ' + esc(fmtDate(today())) + '.</p>';
    document.body.appendChild(box);
    document.body.classList.add('rcm-sk-printing');
    var mql = window.matchMedia ? window.matchMedia('print') : null, seen = false;
    var done = function () {
      document.body.classList.remove('rcm-sk-printing');
      box.remove();
      window.removeEventListener('afterprint', done);
      if (mql && mql.removeEventListener) mql.removeEventListener('change', onMq);
    };
    var onMq = function (m) { if (m.matches) seen = true; else if (seen) done(); };   // browsers that never fire afterprint
    window.addEventListener('afterprint', done);
    if (mql && mql.addEventListener) mql.addEventListener('change', onMq);
    setTimeout(function () { window.print(); }, 60);
  }

  /* ── Styles ──────────────────────────────────────────────────────────── */
  var css =
    '.rcm-sk-panel{margin:14px 0 10px;padding:12px 14px;border:1px solid var(--border,#e2e6eb);border-left:4px solid var(--teal,#1a6b72);border-radius:12px;background:var(--teal-light,#e1f5f0);font-size:14.5px;line-height:1.5;}' +
    '.rcm-sk-panel.rcm-sk-pmode{border-left-color:var(--gold,#b8962e);background:var(--amber-soft,#fffbeb);}' +
    '.rcm-sk-pmode .rcm-sk-badge{color:var(--amber,#92400e);}' +
    '.rcm-sk-head{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:center;}' +
    '.rcm-sk-badge{font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--teal,#1a6b72);}' +
    '.rcm-sk-status{color:var(--text-mid,#2c3a4a);font-weight:600;}' +
    '.rcm-sk-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;}' +
    '.rcm-sk-btn{font:inherit;font-size:14px;font-weight:600;min-height:40px;padding:7px 14px;border-radius:999px;border:1px solid var(--border,#cfd6de);background:var(--white,#fff);color:var(--text,#1a202c);cursor:pointer;}' +
    '.rcm-sk-btn:focus-visible,.rcm-sk-cell:focus-visible{outline:3px solid var(--gold,#b8962e);outline-offset:2px;}' +
    '.rcm-sk-go{background:var(--teal,#1a6b72);border-color:var(--teal,#1a6b72);color:#fff;}' +
    '.rcm-sk-quiet{background:transparent;}' +
    '.rcm-sk-danger{background:var(--red,#b91c1c);border-color:var(--red,#b91c1c);color:#fff;}' +
    '.rcm-sk-note-line{margin:10px 0 0;font-size:13px;color:var(--text-muted,#4a5568);}' +
    '.rcm-sk-who{margin:8px 0 0;}' +
    '.rcm-sk-signed-line{margin:8px 0 0;color:var(--green,#166534);}' +
    '.rcm-sk-warnline{margin:8px 0 0;color:var(--amber,#92400e);}' +
    '.rcm-sk-err{margin:8px 0 0;color:var(--red,#b91c1c);font-weight:600;}' +
    '.rcm-sk-form{margin-top:8px;}' +
    '.rcm-sk-form label{display:block;font-weight:600;font-size:13.5px;color:var(--text-mid,#2c3a4a);}' +
    '.rcm-sk-fields{display:flex;flex-wrap:wrap;gap:10px 14px;}' +
    '.rcm-sk-fields label{flex:1 1 140px;}' +
    '.rcm-sk-form input[type=text],.rcm-sk-form input:not([type]),.rcm-sk-form input[type=date]{display:block;width:100%;box-sizing:border-box;margin-top:4px;font:inherit;font-size:16px;padding:8px 10px;border:1px solid var(--border,#cfd6de);border-radius:8px;background:var(--white,#fff);color:var(--text,#1a202c);}' +
    '.rcm-sk-form input[name=by]{text-transform:uppercase;letter-spacing:.08em;}' +
    '.rcm-sk-form .rcm-sk-check{display:flex;gap:8px;align-items:flex-start;margin-top:10px;font-weight:500;}' +
    '.rcm-sk-check input{width:20px;height:20px;margin:1px 0 0;flex:none;}' +
    '.rcm-sk-left{margin:6px 0 0 20px;padding:0;font-size:14px;}' +
    '.rcm-sk-signform>label{margin-top:4px;}' +
    /* steps in a module list */
    '.nc-check li.rcm-sk-ok::before{background:var(--green,#166534);border-color:var(--green,#166534);}' +
    '.nc-check li.rcm-sk-ok::after{content:"✓";position:absolute;left:2px;top:9px;width:20px;line-height:20px;text-align:center;color:#fff;font-size:13px;font-weight:700;}' +
    '.nc-check li.rcm-sk-warn::before{border-color:var(--amber,#92400e);background:var(--amber-soft,#fffbeb);}' +
    '.nc-check li.rcm-sk-off::before{border-style:dashed;}' +
    '.rcm-sk-step{margin-top:6px;}' +
    '.rcm-sk-seg{display:grid;gap:6px;max-width:520px;}' +
    '.rcm-sk-opt{display:flex;align-items:center;justify-content:center;gap:5px;min-height:40px;padding:5px 8px;font-size:13.5px;line-height:1.15;border-radius:10px;}' +
    '.rcm-sk-opt .rcm-sk-ic{font-weight:700;}' +
    '.rcm-sk-opt[aria-pressed=true].rcm-sk-t-ok{background:var(--green,#166534);border-color:var(--green,#166534);color:#fff;}' +
    '.rcm-sk-opt[aria-pressed=true].rcm-sk-t-warn{background:var(--amber,#92400e);border-color:var(--amber,#92400e);color:#fff;}' +
    '.rcm-sk-opt[aria-pressed=true].rcm-sk-t-off{background:var(--text-muted,#4a5568);border-color:var(--text-muted,#4a5568);color:#fff;}' +
    '.rcm-sk-stamp{margin-top:4px;font-size:13px;color:var(--text-muted,#4a5568);}' +
    '.rcm-sk-stamp.rcm-sk-t-ok b{color:var(--green,#166534);}.rcm-sk-stamp.rcm-sk-t-warn b{color:var(--amber,#92400e);}' +
    '.rcm-sk-chg{font-size:12px;font-style:italic;color:var(--text-faint,#5c6a7e);}' +
    /* steps in a table */
    '.rcm-sk-cell{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;width:100%;min-height:40px;padding:4px 2px;margin:0;border:0;background:transparent;color:inherit;font:inherit;line-height:1.15;text-align:center;}' +
    'button.rcm-sk-cell{cursor:pointer;border-radius:8px;}' +
    'button.rcm-sk-cell:hover{background:var(--teal-light,#e1f5f0);}' +
    '.rcm-sk-cell .rcm-sk-ic{font-size:18px;font-weight:700;}' +
    '.rcm-sk-cell small{font-size:11px;color:var(--text-muted,#4a5568);white-space:nowrap;}' +
    '.rcm-sk-cell.on.rcm-sk-t-ok .rcm-sk-ic{color:var(--green,#166534);}.rcm-sk-cell.on.rcm-sk-t-warn .rcm-sk-ic{color:var(--amber,#92400e);}' +
    '.rcm-sk-ghost{color:var(--text-faint,#9ba6b8);font-weight:400!important;}' +
    'table.rcm-sk-on td{padding-top:2px;padding-bottom:2px;}' +
    'tr.rcm-sk-ok>td:first-child{box-shadow:inset 4px 0 0 var(--green,#166534);}' +
    'tr.rcm-sk-warn>td:first-child{box-shadow:inset 4px 0 0 var(--amber,#92400e);}' +
    '.rcm-sk-note{width:100%;min-width:120px;box-sizing:border-box;font:inherit;font-size:14px;padding:4px 6px;border:1px solid var(--border,#cfd6de);border-radius:6px;background:var(--white,#fff);color:var(--text,#1a202c);}' +
    '.rcm-sk-notetext small{color:var(--text-muted,#4a5568);}' +
    '.rcm-sk-toast{position:fixed;left:50%;bottom:84px;transform:translateX(-50%) translateY(20px);max-width:min(92vw,460px);padding:10px 16px;border-radius:12px;background:var(--navy,#1f3864);color:#fff;font-size:14px;line-height:1.4;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;z-index:10050;}' +
    '.rcm-sk-toast.on{opacity:1;transform:translateX(-50%) translateY(0);}' +
    '.rcm-sk-printout{display:none;}' +
    '@media (max-width:640px){.rcm-sk-panel{padding:10px 12px;}.rcm-sk-btn{font-size:13.5px;padding:7px 12px;}.rcm-sk-opt{flex-direction:column;gap:1px;min-height:48px;font-size:12.5px;padding:4px 4px;}.rcm-sk-opt .rcm-sk-ic{font-size:16px;}}' +
    '@media print{' +
      '.rcm-sk-panel,.rcm-sk-toast,.rcm-sk-ghost,.rcm-sk-note{display:none!important;}' +
      'button.rcm-sk-cell:not(.on),.rcm-sk-opt{display:none!important;}' +
      '.nc-check li.rcm-sk-ok::before,.nc-check li.rcm-sk-ok::after{-webkit-print-color-adjust:exact;print-color-adjust:exact;}' +
      'body.rcm-sk-printing>*:not(.rcm-sk-printout){display:none!important;}' +
      'body.rcm-sk-printing .rcm-sk-printout{display:block!important;color:#000;background:#fff;font:11pt/1.4 Inter,Arial,sans-serif;}' +
      '.rcm-sk-printout .k{font-size:9pt;letter-spacing:.06em;text-transform:uppercase;margin:0;}' +
      '.rcm-sk-printout h1{font-size:15pt;margin:4px 0 6px;}' +
      '.rcm-sk-printout table{width:100%;border-collapse:collapse;margin:10px 0;}' +
      '.rcm-sk-printout th,.rcm-sk-printout td{border:1px solid #888;padding:4px 6px;vertical-align:top;text-align:left;font-size:10pt;}' +
      '.rcm-sk-printout tr{break-inside:avoid;}' +
      '.rcm-sk-printout .crit{font-size:8pt;text-transform:uppercase;color:#b00;}' +
      '.rcm-sk-printout .lines{margin-top:28px;}' +
      '.rcm-sk-printout .foot{font-size:8.5pt;color:#444;}' +
    '}';
  var st = document.createElement('style');
  st.id = 'rcm-sk-css';
  st.textContent = css;
  document.head.appendChild(st);

  lists.forEach(render);
})();
