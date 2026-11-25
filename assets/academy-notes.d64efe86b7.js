/* Renal Care Academy: Highlights & Notes, Bookmarks and Resume (Nov 2026).
   Learners select text in a module to highlight it or attach a note. Everything is stored in
   this browser's localStorage only: no account, no network requests, works offline. A "My notes"
   drawer lists the notes on the page, links to other modules that have notes, and exports them
   (Markdown, print / save as PDF, JSON backup and restore).
   Bookmarks: a ribbon button on every section heading; bookmarks are listed in the same drawer.
   Resume: the reading position is saved as you scroll (as a text anchor, so it survives layout
   changes); reopening a module offers "Pick up where you left off", and the Academy landing page
   and track hubs offer "Continue" for the last module read.

   Source file: edit assets/academy-notes.js, then run tools/academy/apply_notes.py, which writes
   the fingerprinted copy (assets/academy-notes.<hash>.js) and points the Academy pages at it.
   Never link the unhashed file. */
(function () {
  'use strict';
  if (window.__rcmNotes) return;
  window.__rcmNotes = true;

  var ROOT = document.querySelector('main.container') || document.querySelector('main');
  if (!ROOT || !window.localStorage) return;

  var PREFIX = 'rcm-notes:';
  var PAGE = location.pathname.replace(/\.html$/, '').replace(/\/$/, '/index');
  var KEY = PREFIX + PAGE;
  var COLORS = [
    { id: 'y', name: 'Yellow' },
    { id: 'g', name: 'Green' },
    { id: 'b', name: 'Blue' },
    { id: 'p', name: 'Pink' }
  ];
  var CTX = 40;          // characters of context saved before and after each highlight
  var SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEXTAREA: 1, INPUT: 1, SELECT: 1, BUTTON: 1, svg: 1, SVG: 1 };
  var coarse = window.matchMedia && matchMedia('(pointer: coarse)').matches;

  /* ── Storage ─────────────────────────────────────────────────────────── */
  function pageTitle() {
    var h = document.querySelector('.hero h1') || document.querySelector('h1');
    return (h ? h.textContent : document.title).replace(/\s+/g, ' ').trim();
  }
  function loadRec() {
    try { return JSON.parse(localStorage.getItem(KEY) || 'null') || {}; } catch (e) { return {}; }
  }
  function load() { var d = loadRec(); return Array.isArray(d.notes) ? d.notes : []; }
  var notes = load();
  var marks = Array.isArray(loadRec().bm) ? loadRec().bm : [];   // bookmarks: [{id, title, at}]
  function save() {
    try {
      if (!notes.length && !marks.length) localStorage.removeItem(KEY);
      else localStorage.setItem(KEY, JSON.stringify({ v: 1, title: pageTitle(), url: location.pathname, notes: notes, bm: marks }));
      return true;
    } catch (e) {
      toast('Could not save: this browser’s storage is full or blocked.');
      return false;
    }
  }

  /* ── Text index of the module body ───────────────────────────────────── */
  var idx;   // { nodes: [Text], starts: [int], text: string }
  function skipped(el) {
    for (; el && el !== ROOT; el = el.parentNode) {
      if (el.nodeType === 1 && (SKIP[el.nodeName] || (el.classList && el.classList.contains('rcn-ui')))) return true;
    }
    return false;
  }
  function buildIndex() {
    var nodes = [], starts = [], parts = [], pos = 0;
    var w = document.createTreeWalker(ROOT, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) { return skipped(n.parentNode) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; }
    });
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      nodes.push(n); starts.push(pos); parts.push(n.data); pos += n.data.length;
    }
    idx = { nodes: nodes, starts: starts, text: parts.join('') };
    return idx;
  }
  function pointToOffset(node, off) {
    var i;
    if (node.nodeType === 3) {
      i = idx.nodes.indexOf(node);
      if (i >= 0) return idx.starts[i] + Math.min(off, node.data.length);
    }
    var ref = node.nodeType === 3 ? node : (off < node.childNodes.length ? node.childNodes[off] : null);
    for (i = 0; i < idx.nodes.length; i++) {
      var t = idx.nodes[i];
      if (ref) {
        if (t === ref || (ref.compareDocumentPosition(t) & (Node.DOCUMENT_POSITION_FOLLOWING | Node.DOCUMENT_POSITION_CONTAINED_BY))) return idx.starts[i];
      } else if ((node.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING) && !node.contains(t)) {
        return idx.starts[i];
      }
    }
    return idx.text.length;
  }

  /* ── Wrapping and unwrapping highlights ──────────────────────────────── */
  function wrap(note, start, end) {
    buildIndex();
    var first = null, segs = [];
    for (var i = 0; i < idx.nodes.length; i++) {
      var ns = idx.starts[i], node = idx.nodes[i], ne = ns + node.data.length;
      if (ne <= start || ns >= end) continue;
      segs.push([node, Math.max(start, ns) - ns, Math.min(end, ne) - ns]);
    }
    segs.forEach(function (s) {
      var node = s[0], a = s[1], b = s[2];
      if (!/\S/.test(node.data.slice(a, b))) return;          // whitespace between blocks: leave alone
      if (b < node.data.length) node.splitText(b);
      if (a > 0) node = node.splitText(a);
      var m = document.createElement('mark');
      m.className = 'rcn-hl rcn-' + note.color + (note.text ? ' rcn-has-note' : '');
      m.setAttribute('data-rcn', note.id);
      m.setAttribute('tabindex', '0');
      m.setAttribute('role', 'button');
      m.setAttribute('aria-label', note.text ? 'Highlight with note: ' + note.text.slice(0, 80) : 'Highlight. Open to add a note');
      node.parentNode.insertBefore(m, node);
      m.appendChild(node);
      if (!first) first = m;
    });
    markLast(note.id);
    return first;
  }
  function marksFor(id) { return ROOT.querySelectorAll('mark.rcn-hl[data-rcn="' + id + '"]'); }
  function markLast(id) {
    var ms = marksFor(id);
    for (var i = 0; i < ms.length; i++) ms[i].classList.toggle('rcn-last', i === ms.length - 1);
  }
  function unwrap(id) {
    var parents = [];
    Array.prototype.forEach.call(marksFor(id), function (m) {
      var p = m.parentNode;
      while (m.firstChild) p.insertBefore(m.firstChild, m);
      p.removeChild(m);
      parents.push(p);
    });
    parents.forEach(function (p) { p.normalize(); });
  }
  function restyle(note) {
    Array.prototype.forEach.call(marksFor(note.id), function (m) {
      m.className = 'rcn-hl rcn-' + note.color + (note.text ? ' rcn-has-note' : '');
      m.setAttribute('aria-label', note.text ? 'Highlight with note: ' + note.text.slice(0, 80) : 'Highlight. Open to add a note');
    });
    markLast(note.id);
  }

  /* ── Re-anchoring saved highlights after the page loads ─────────────── */
  function commonSuffix(a, b) { var n = 0; while (n < a.length && n < b.length && a[a.length - 1 - n] === b[b.length - 1 - n]) n++; return n; }
  function commonPrefix(a, b) { var n = 0; while (n < a.length && n < b.length && a[n] === b[n]) n++; return n; }
  function locate(note) {
    var text = idx.text, q = note.quote, best = -1, bestScore = -1, from = 0, at;
    if (!q) return -1;
    while ((at = text.indexOf(q, from)) !== -1) {
      var score = commonSuffix(text.slice(Math.max(0, at - CTX), at), note.prefix || '') +
                  commonPrefix(text.slice(at + q.length, at + q.length + CTX), note.suffix || '') -
                  Math.min(Math.abs(at - (note.pos || 0)) / 5000, 10);
      if (score > bestScore) { bestScore = score; best = at; }
      from = at + 1;
    }
    return best;
  }
  function restoreAll() {
    buildIndex();
    notes.slice().sort(function (a, b) { return (a.pos || 0) - (b.pos || 0); }).forEach(function (n) {
      var at = locate(n);
      n.orphan = at < 0;
      if (at >= 0) { wrap(n, at, at + n.quote.length); buildIndex(); }
    });
  }

  /* ── Section label for a highlight (for the notes list and export) ──── */
  function sectionOf(el) {
    var s = el && el.closest ? el.closest('section[id]') : null;
    if (!s) return '';
    var h = s.querySelector('h2, h3');
    if (!h) return '';
    var en = h.querySelector('[data-lang="en"]');
    return (en || h).textContent.replace(/\s+/g, ' ').trim();
  }

  /* ── UI building blocks ──────────────────────────────────────────────── */
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var ICON_PEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>';
  var ICON_NOTE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';

  var toastTimer;
  function toast(msg) {
    if (bar && bar.classList.contains('rcn-show')) return;
    var t = document.querySelector('.rcn-toast');
    if (!t) { t = el('div', 'rcn-ui rcn-toast'); t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg;
    t.classList.add('rcn-show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove('rcn-show'); }, 3200);
  }

  /* Selection toolbar */
  var bar = el('div', 'rcn-ui rcn-bar no-print');
  bar.setAttribute('role', 'toolbar');
  bar.setAttribute('aria-label', 'Highlight selected text');
  COLORS.forEach(function (c) {
    var b = el('button', 'rcn-sw rcn-sw-' + c.id);
    b.type = 'button';
    b.title = 'Highlight ' + c.name.toLowerCase();
    b.setAttribute('aria-label', 'Highlight ' + c.name.toLowerCase());
    b.setAttribute('data-color', c.id);
    bar.appendChild(b);
  });
  var noteBtn = el('button', 'rcn-bar-note', ICON_NOTE + '<span>Note</span>');
  noteBtn.type = 'button';
  noteBtn.setAttribute('aria-label', 'Highlight and add a note');
  bar.appendChild(noteBtn);
  document.body.appendChild(bar);
  bar.addEventListener('mousedown', function (e) { e.preventDefault(); });   // keep the selection

  var pending = null;   // { start, end, rect }
  function hideBar() { bar.classList.remove('rcn-show'); pending = null; }
  function checkSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount) { hideBar(); return; }
    var r = sel.getRangeAt(0);
    if (!ROOT.contains(r.commonAncestorContainer) || skipped(r.commonAncestorContainer.nodeType === 1 ? r.commonAncestorContainer : r.commonAncestorContainer.parentNode)) { hideBar(); return; }
    buildIndex();
    var s = pointToOffset(r.startContainer, r.startOffset), e = pointToOffset(r.endContainer, r.endOffset);
    var raw = idx.text.slice(s, e);
    var lead = raw.length - raw.replace(/^\s+/, '').length, trail = raw.length - raw.replace(/\s+$/, '').length;
    s += lead; e -= trail;
    if (e - s < 2) { hideBar(); return; }
    var rects = r.getClientRects(), rect = rects.length ? rects[0] : r.getBoundingClientRect();
    pending = { start: s, end: e };
    var tt = document.querySelector('.rcn-toast');
    if (tt) tt.classList.remove('rcn-show');
    bar.classList.add('rcn-show');
    var bw = bar.offsetWidth, bh = bar.offsetHeight;
    if (coarse) {
      /* Touch screens: the system Copy / Look Up menu can open above or below the selection,
         so dock the bar to the edge of the screen away from the selection instead. */
      var vv = window.visualViewport, vh = vv ? vv.height : window.innerHeight, vt = vv ? vv.offsetTop : 0;
      var vw = vv ? vv.width : window.innerWidth, vl = vv ? vv.offsetLeft : 0;
      var last = rects.length ? rects[rects.length - 1] : rect;
      var nearBottom = last.bottom - vt > vh * 0.62;
      bar.classList.toggle('rcn-dock-top', nearBottom);
      bar.style.left = Math.max(vl + 8, vl + vw / 2 - bw / 2) + 'px';
      var ab = document.querySelector('.sch-appbar'), abh = ab ? ab.offsetHeight : 0;   // Schola app bar
      bar.style.top = (nearBottom ? vt + 12 : vt + vh - bh - 18 - abh) + 'px';
      return;
    }
    var x = Math.max(8, Math.min(window.innerWidth - bw - 8, rect.left + rect.width / 2 - bw / 2));
    var y = rect.top - bh - 10;
    if (y < 8) y = (rects.length ? rects[rects.length - 1] : rect).bottom + 10;
    if (y + bh > window.innerHeight - 8) y = Math.max(8, rect.top - bh - 10);
    bar.style.left = x + 'px';
    bar.style.top = y + 'px';
  }
  if (window.visualViewport) window.visualViewport.addEventListener('resize', function () { if (pending) checkSelection(); });
  var selTimer;
  document.addEventListener('selectionchange', function () {
    clearTimeout(selTimer);
    selTimer = setTimeout(checkSelection, coarse ? 450 : 220);
  });
  window.addEventListener('scroll', function () { if (pending) checkSelection(); }, { passive: true });

  function createFrom(color, openEditor) {
    if (!pending) return;
    var n = {
      id: 'n' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
      color: color,
      text: '',
      quote: idx.text.slice(pending.start, pending.end),
      prefix: idx.text.slice(Math.max(0, pending.start - CTX), pending.start),
      suffix: idx.text.slice(pending.end, pending.end + CTX),
      pos: pending.start,
      created: new Date().toISOString()
    };
    var m = wrap(n, pending.start, pending.end);
    n.section = sectionOf(m);
    notes.push(n);
    save();
    window.getSelection().removeAllRanges();
    hideBar();
    refreshCount();
    if (openEditor && m) openPop(n.id, m);
  }
  bar.addEventListener('click', function (e) {
    var sw = e.target.closest('[data-color]');
    if (sw) createFrom(sw.getAttribute('data-color'), false);
    else if (e.target.closest('.rcn-bar-note')) createFrom('y', true);
  });

  /* Note editor popover (opens on a highlight) */
  var pop = el('div', 'rcn-ui rcn-pop no-print');
  pop.setAttribute('role', 'dialog');
  pop.setAttribute('aria-label', 'Edit highlight');
  pop.innerHTML =
    '<div class="rcn-pop-row"><div class="rcn-pop-sw"></div><button type="button" class="rcn-x" aria-label="Close">×</button></div>' +
    '<textarea class="rcn-ta" rows="4" placeholder="Add your note (saved on this device only)"></textarea>' +
    '<div class="rcn-pop-row rcn-pop-foot"><button type="button" class="rcn-del">Remove highlight</button><button type="button" class="rcn-done">Done</button></div>';
  var popSw = pop.querySelector('.rcn-pop-sw'), ta = pop.querySelector('.rcn-ta');
  COLORS.forEach(function (c) {
    var b = el('button', 'rcn-sw rcn-sw-' + c.id);
    b.type = 'button';
    b.setAttribute('aria-label', c.name);
    b.title = c.name;
    b.setAttribute('data-color', c.id);
    popSw.appendChild(b);
  });
  document.body.appendChild(pop);
  var popId = null, saveTimer;
  function find(id) { for (var i = 0; i < notes.length; i++) if (notes[i].id === id) return notes[i]; return null; }
  function openPop(id, anchor) {
    var n = find(id);
    if (!n) return;
    popId = id;
    ta.value = n.text || '';
    Array.prototype.forEach.call(popSw.children, function (b) { b.classList.toggle('rcn-on', b.getAttribute('data-color') === n.color); });
    pop.classList.add('rcn-show');
    var r = anchor.getBoundingClientRect(), pw = pop.offsetWidth, ph = pop.offsetHeight;
    var x = Math.max(8, Math.min(window.innerWidth - pw - 8, r.left));
    var y = r.bottom + 10;
    if (y + ph > window.innerHeight - 8) y = Math.max(8, r.top - ph - 10);
    pop.style.left = x + 'px';
    pop.style.top = y + 'px';
    if (!coarse || !n.text) ta.focus({ preventScroll: true });
  }
  function commit() {
    var n = find(popId);
    if (!n) return;
    var v = ta.value.replace(/\s+$/, '');
    if (v !== (n.text || '')) { n.text = v; n.updated = new Date().toISOString(); restyle(n); save(); renderList(); }
  }
  function closePop() { if (popId) { clearTimeout(saveTimer); commit(); } pop.classList.remove('rcn-show'); popId = null; }
  ta.addEventListener('input', function () { clearTimeout(saveTimer); saveTimer = setTimeout(commit, 500); });
  pop.addEventListener('click', function (e) {
    var sw = e.target.closest('[data-color]');
    if (sw) {
      var n = find(popId);
      if (!n) return;
      n.color = sw.getAttribute('data-color');
      restyle(n); save(); renderList();
      Array.prototype.forEach.call(popSw.children, function (b) { b.classList.toggle('rcn-on', b === sw); });
    } else if (e.target.closest('.rcn-x') || e.target.closest('.rcn-done')) {
      closePop();
    } else if (e.target.closest('.rcn-del')) {
      var id = popId;
      pop.classList.remove('rcn-show'); popId = null;
      remove(id);
    }
  });
  function remove(id) {
    unwrap(id);
    notes = notes.filter(function (n) { return n.id !== id; });
    save(); refreshCount(); renderList();
  }

  ROOT.addEventListener('click', function (e) {
    var m = e.target.closest && e.target.closest('mark.rcn-hl');
    if (!m) return;
    var sel = window.getSelection();
    if (sel && !sel.isCollapsed) return;
    openPop(m.getAttribute('data-rcn'), m);
  });
  ROOT.addEventListener('keydown', function (e) {
    var m = e.target.closest && e.target.closest('mark.rcn-hl');
    if (m && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); openPop(m.getAttribute('data-rcn'), m); }
  });
  document.addEventListener('mousedown', function (e) {
    if (popId && !pop.contains(e.target) && !(e.target.closest && e.target.closest('mark.rcn-hl'))) closePop();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (popId) closePop();
    else if (drawer.classList.contains('rcn-show')) closeDrawer();
    else hideBar();
  });

  /* "My notes" drawer */
  var drawer = el('aside', 'rcn-ui rcn-drawer no-print');
  drawer.setAttribute('aria-label', 'My notes');
  drawer.innerHTML =
    '<div class="rcn-dh"><div><div class="rcn-dt">My notes &amp; bookmarks</div><div class="rcn-ds">Saved on this device and browser only</div></div>' +
    '<button type="button" class="rcn-x" aria-label="Close my notes">×</button></div>' +
    '<div class="rcn-bms"></div>' +
    '<div class="rcn-list" tabindex="-1"></div>' +
    '<div class="rcn-other"></div>' +
    '<div class="rcn-actions">' +
    '<button type="button" data-act="md">Export (.md)</button>' +
    '<button type="button" data-act="print">Print / PDF</button>' +
    '<button type="button" data-act="backup">Back up all</button>' +
    '<button type="button" data-act="restore">Restore</button>' +
    '<button type="button" data-act="clear" class="rcn-danger">Delete this page\u2019s notes &amp; bookmarks</button>' +
    '</div><input type="file" accept="application/json,.json" class="rcn-file" hidden>';
  document.body.appendChild(drawer);
  var bmList = drawer.querySelector('.rcn-bms');
  var list = drawer.querySelector('.rcn-list'), other = drawer.querySelector('.rcn-other'), fileIn = drawer.querySelector('.rcn-file');

  function ordered() {
    return notes.slice().sort(function (a, b) {
      var ma = marksFor(a.id)[0], mb = marksFor(b.id)[0];
      if (ma && mb) return ma.compareDocumentPosition(mb) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
      if (ma) return -1;
      if (mb) return 1;
      return (a.pos || 0) - (b.pos || 0);
    });
  }
  function renderList() {
    if (!drawer.classList.contains('rcn-show')) return;
    var items = ordered(), html = '', last = null;
    renderBookmarks();
    if (!items.length) {
      html = '<div class="rcn-sec">Highlights &amp; notes</div><p class="rcn-empty">No highlights yet. Select any text in this module, then pick a color or tap <b>Note</b>.</p>';
    }
    items.forEach(function (n) {
      var sec = n.section || '';
      if (sec !== last) { html += '<div class="rcn-sec">' + esc(sec || 'Module') + '</div>'; last = sec; }
      var q = n.quote.length > 220 ? n.quote.slice(0, 217) + '…' : n.quote;
      html += '<div class="rcn-item rcn-b-' + n.color + (n.orphan ? ' rcn-orphan' : '') + '" data-id="' + n.id + '">' +
        '<button type="button" class="rcn-go" ' + (n.orphan ? 'disabled' : '') + '>“' + esc(q) + '”</button>' +
        (n.text ? '<div class="rcn-nt">' + esc(n.text).replace(/\n/g, '<br>') + '</div>' : '') +
        (n.orphan ? '<div class="rcn-warn">This passage changed when the module was updated. Your note is kept here.</div>' : '') +
        '<div class="rcn-meta">' + new Date(n.updated || n.created).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) +
        ' <button type="button" class="rcn-edit"' + (n.orphan ? ' hidden' : '') + '>Edit</button>' +
        ' <button type="button" class="rcn-rm">Delete</button></div></div>';
    });
    list.innerHTML = html;
    var pages = otherPages();
    other.innerHTML = pages.length
      ? '<div class="rcn-sec">Your notes &amp; bookmarks in other modules</div>' + pages.map(function (p) {
          return '<a href="' + esc(p.url) + '">' + esc(p.title) + ' <span>' + p.count + '</span></a>';
        }).join('')
      : '';
  }
  function otherPages() {
    var out = [];
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k.indexOf(PREFIX) !== 0 || k === KEY) continue;
        var d = JSON.parse(localStorage.getItem(k) || 'null');
        var cnt = d ? (d.notes || []).length + (d.bm || []).length : 0;
        if (cnt) out.push({ url: d.url || k.slice(PREFIX.length), title: d.title || k.slice(PREFIX.length), count: cnt });
      }
    } catch (e) {}
    return out.sort(function (a, b) { return a.url < b.url ? -1 : 1; });
  }
  list.addEventListener('click', function (e) {
    var item = e.target.closest('.rcn-item');
    if (!item) return;
    var id = item.getAttribute('data-id'), m = marksFor(id)[0];
    if (e.target.closest('.rcn-rm')) {
      if (confirmInline(e.target, 'Delete?')) remove(id);
      return;
    }
    if (!m) return;
    if (coarse) closeDrawer();
    m.scrollIntoView({ behavior: 'smooth', block: 'center' });
    Array.prototype.forEach.call(marksFor(id), function (x) { x.classList.remove('rcn-flash'); void x.offsetWidth; x.classList.add('rcn-flash'); });
    if (e.target.closest('.rcn-edit')) setTimeout(function () { openPop(id, m); }, 450);
  });
  /* Two-tap confirm instead of a blocking browser dialog */
  function confirmInline(btn, label) {
    if (btn.getAttribute('data-armed')) return true;
    var old = btn.textContent;
    btn.setAttribute('data-armed', '1');
    btn.textContent = label;
    btn.classList.add('rcn-armed');
    setTimeout(function () { btn.removeAttribute('data-armed'); btn.textContent = old; btn.classList.remove('rcn-armed'); }, 3000);
    return false;
  }

  function openDrawer() { closePop(); hideBar(); drawer.classList.add('rcn-show'); renderList(); list.focus({ preventScroll: true }); }
  function closeDrawer() { drawer.classList.remove('rcn-show'); }
  drawer.querySelector('.rcn-x').addEventListener('click', closeDrawer);

  /* Exports */
  function download(name, type, body) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([body], { type: type }));
    a.download = name;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  }
  function slug() { return PAGE.split('/').pop() || 'academy'; }
  function today() { return new Date().toISOString().slice(0, 10); }
  function toMarkdown() {
    var out = ['# My notes: ' + pageTitle(), '', 'Renal Care Academy · ' + location.origin + location.pathname, 'Exported ' + new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }), ''];
    var last = null;
    ordered().forEach(function (n) {
      if ((n.section || '') !== last) { last = n.section || ''; out.push('## ' + (last || 'Module'), ''); }
      out.push('> ' + n.quote.replace(/\s+/g, ' '));
      if (n.text) out.push('', n.text);
      out.push('');
    });
    return out.join('\n');
  }
  function printNotes() {
    var last = null, body = '';
    ordered().forEach(function (n) {
      if ((n.section || '') !== last) { last = n.section || ''; body += '<h2>' + esc(last || 'Module') + '</h2>'; }
      body += '<blockquote class="c-' + n.color + '">' + esc(n.quote) + '</blockquote>' + (n.text ? '<p>' + esc(n.text).replace(/\n/g, '<br>') + '</p>' : '');
    });
    var html = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>My notes: ' + esc(pageTitle()) + '</title><style>' +
      'body{font:15px/1.55 "Nunito Sans",Arial,sans-serif;color:#1b2430;max-width:720px;margin:32px auto;padding:0 20px}' +
      'h1{font:700 22px Manrope,Arial,sans-serif;color:#1F3864;margin:0 0 4px}.sub{color:#5a6677;font-size:13px;margin:0 0 20px}' +
      'h2{font:700 15px Manrope,Arial,sans-serif;color:#1A6B72;border-bottom:1px solid #d8e0e8;padding-bottom:4px;margin:22px 0 10px}' +
      'blockquote{margin:10px 0 4px;padding:6px 12px;border-left:4px solid #e3b505;background:#fff8d6}' +
      '.c-g{border-color:#3e9b57;background:#e3f4e6}.c-b{border-color:#3b82c4;background:#e2eefa}.c-p{border-color:#d0558c;background:#fbe3ee}' +
      'p{margin:4px 0 12px 16px}footer{margin-top:28px;font-size:12px;color:#7a8594}' +
      '@media print{body{margin:0}blockquote{-webkit-print-color-adjust:exact;print-color-adjust:exact}}</style></head><body>' +
      '<h1>' + esc(pageTitle()) + '</h1><p class="sub">My notes · Renal Care Academy · ' + new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }) + '</p>' +
      (body || '<p>No notes on this page.</p>') + '<footer>' + esc(location.origin + location.pathname) + '</footer>' +
      '<script>window.onload=function(){setTimeout(function(){window.print()},300)}<\/script></body></html>';
    var w = window.open('', '_blank');
    if (w) { w.document.open(); w.document.write(html); w.document.close(); }
    else download('my-notes-' + slug() + '.html', 'text/html', html);
  }
  function backup() {
    var all = {};
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k.indexOf(PREFIX) === 0) all[k] = JSON.parse(localStorage.getItem(k));
      }
    } catch (e) {}
    download('renal-care-academy-notes-' + today() + '.json', 'application/json',
      JSON.stringify({ kind: 'rcm-academy-notes', v: 1, exported: new Date().toISOString(), pages: all }, null, 1));
  }
  function restore(file) {
    var r = new FileReader();
    r.onload = function () {
      try {
        var d = JSON.parse(r.result), pages = d && d.kind === 'rcm-academy-notes' ? d.pages : null, added = 0;
        if (!pages) throw new Error('not a notes backup');
        Object.keys(pages).forEach(function (k) {
          if (k.indexOf(PREFIX) !== 0 || !pages[k] || !Array.isArray(pages[k].notes)) return;
          var cur = null;
          try { cur = JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) {}
          var have = {}, merged = cur && cur.notes ? cur.notes.slice() : [];
          merged.forEach(function (n) { have[n.id] = 1; });
          pages[k].notes.forEach(function (n) { if (n && n.id && n.quote && !have[n.id]) { merged.push(n); added++; } });
          var bms = cur && cur.bm ? cur.bm.slice() : [], hb = {};
          bms.forEach(function (b) { hb[b.id] = 1; });
          (pages[k].bm || []).forEach(function (b) { if (b && b.id && !hb[b.id]) { bms.push(b); added++; } });
          localStorage.setItem(k, JSON.stringify({ v: 1, title: pages[k].title || (cur && cur.title), url: pages[k].url || (cur && cur.url), notes: merged, bm: bms }));
        });
        Array.prototype.forEach.call(ROOT.querySelectorAll('mark.rcn-hl'), function (m) { unwrap(m.getAttribute('data-rcn')); });
        notes = load();
        marks = loadRec().bm || [];
        restoreAll(); syncRibbons(); refreshCount(); renderList();
        toast(added ? 'Restored ' + added + ' note' + (added === 1 ? '' : 's') + '.' : 'Nothing new to restore.');
      } catch (e) { toast('That file is not a Renal Care Academy notes backup.'); }
    };
    r.readAsText(file);
  }
  drawer.querySelector('.rcn-actions').addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]');
    if (!b) return;
    var act = b.getAttribute('data-act');
    if (act === 'md') { if (!notes.length) return toast('No notes on this page yet.'); download('my-notes-' + slug() + '.md', 'text/markdown', toMarkdown()); }
    else if (act === 'print') { if (!notes.length) return toast('No notes on this page yet.'); printNotes(); }
    else if (act === 'backup') backup();
    else if (act === 'restore') fileIn.click();
    else if (act === 'clear') {
      if (!notes.length && !marks.length) return;
      if (!confirmInline(b, 'Tap again to delete all ' + (notes.length + marks.length))) return;
      notes.slice().forEach(function (n) { unwrap(n.id); });
      notes = []; marks = []; save(); syncRibbons(); refreshCount(); renderList();
      toast('Deleted this page’s notes.');
    }
  });
  fileIn.addEventListener('change', function () { if (fileIn.files[0]) restore(fileIn.files[0]); fileIn.value = ''; });

  /* Floating "My notes" button: top of the left-hand stack (above Print and Download) */
  var fab = el('button', 'rcn-ui rcn-fab no-print', ICON_PEN + '<span class="rcn-tip">My notes &amp; bookmarks</span><span class="rcn-count" hidden></span>');
  fab.type = 'button';
  fab.setAttribute('aria-label', 'My notes, highlights and bookmarks');
  fab.addEventListener('click', function () { drawer.classList.contains('rcn-show') ? closeDrawer() : openDrawer(); });
  document.body.appendChild(fab);
  function placeFab() {
    var top = window.innerHeight - 24;
    Array.prototype.forEach.call(document.querySelectorAll('.print-btn, .dl-fab, .float-controls-left'), function (b) {
      var r = b.getBoundingClientRect();
      if (r.width && r.left < window.innerWidth / 2 && getComputedStyle(b).position === 'fixed') top = Math.min(top, r.top);
    });
    fab.style.bottom = (window.innerHeight - top + 12) + 'px';
  }
  placeFab();
  window.addEventListener('resize', placeFab);
  window.addEventListener('load', placeFab);
  function refreshCount() {
    var c = fab.querySelector('.rcn-count');
    var n = notes.length + marks.length;
    c.textContent = n > 99 ? '99+' : String(n);
    c.hidden = !n;
  }


  /* ── Bookmarks: a ribbon on every section heading ────────────────────── */
  var ICON_BM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';
  function headingOf(s) { return s.querySelector(':scope > h2, :scope > h3'); }
  function headingText(h) {
    var en = h.querySelector('[data-lang="en"]');
    return (en || h).textContent.replace(/\s+/g, ' ').trim();
  }
  var sections = Array.prototype.filter.call(ROOT.querySelectorAll('section[id]'), headingOf);
  function isMarked(id) { for (var i = 0; i < marks.length; i++) if (marks[i].id === id) return true; return false; }
  sections.forEach(function (s) {
    var b = el('button', 'rcn-ui rcn-rib no-print', ICON_BM);
    b.type = 'button';
    b.setAttribute('data-sec', s.id);
    headingOf(s).appendChild(b);
  });
  function syncRibbons() {
    Array.prototype.forEach.call(ROOT.querySelectorAll('.rcn-rib'), function (b) {
      var on = isMarked(b.getAttribute('data-sec'));
      b.classList.toggle('rcn-on', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.setAttribute('aria-label', on ? 'Remove bookmark' : 'Bookmark this section');
      b.title = on ? 'Remove bookmark' : 'Bookmark this section';
    });
  }
  ROOT.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.rcn-rib');
    if (!b) return;
    e.preventDefault();
    var id = b.getAttribute('data-sec'), s = document.getElementById(id);
    if (isMarked(id)) {
      marks = marks.filter(function (m) { return m.id !== id; });
      toast('Bookmark removed.');
    } else {
      marks.push({ id: id, title: headingText(headingOf(s)), at: new Date().toISOString() });
      toast('Bookmarked. Find it under the orange pen button.');
    }
    save(); syncRibbons(); refreshCount(); renderList();
  });
  function renderBookmarks() {
    var order = {};
    sections.forEach(function (s, i) { order[s.id] = i; });
    var bms = marks.slice().sort(function (a, b) { return (order[a.id] || 0) - (order[b.id] || 0); });
    bmList.innerHTML = '<div class="rcn-sec">Bookmarks</div>' + (bms.length ? bms.map(function (m) {
      var gone = !document.getElementById(m.id);
      return '<div class="rcn-bm" data-sec="' + esc(m.id) + '">' + ICON_BM +
        '<button type="button" class="rcn-bm-go"' + (gone ? ' disabled' : '') + '>' + esc(m.title) + '</button>' +
        '<button type="button" class="rcn-bm-x" aria-label="Remove bookmark">×</button></div>';
    }).join('') : '<p class="rcn-empty">Tap the ribbon next to any section title to bookmark it.</p>');
  }
  bmList.addEventListener('click', function (e) {
    var row = e.target.closest('.rcn-bm');
    if (!row) return;
    var id = row.getAttribute('data-sec');
    if (e.target.closest('.rcn-bm-x')) {
      marks = marks.filter(function (m) { return m.id !== id; });
      save(); syncRibbons(); refreshCount(); renderList();
      return;
    }
    var s = document.getElementById(id);
    if (!s) return;
    if (coarse) closeDrawer();
    scrollToEl(headingOf(s) || s);
  });
  syncRibbons();

  /* ── Resume where you left off ────────────────────────────────────────── */
  var POS_KEY = 'rcm-pos:' + PAGE, LAST_KEY = 'rcm-last';
  var FILE = PAGE.split('/').pop();
  var isModule = /-\d{2}-/.test(FILE);
  var isHub = !isModule && !/final-exam|trainer/.test(FILE);
  function topOffset() {
    var off = 0;
    Array.prototype.forEach.call(document.querySelectorAll('.site-header, .nav-strip, .audience-tabs'), function (e) {
      var cs = getComputedStyle(e), r = e.getBoundingClientRect();
      if ((cs.position === 'sticky' || cs.position === 'fixed') && r.bottom > 0 && r.top < 200) off = Math.max(off, r.bottom);
    });
    return off + 14;
  }
  function scrollToEl(target, smooth) {
    function go(b) { window.scrollTo({ top: target.getBoundingClientRect().top + window.pageYOffset - topOffset(), behavior: b }); }
    go(smooth === false ? 'auto' : 'smooth');
    setTimeout(function () { go('auto'); }, 800);   // images above may finish loading and shift the page
  }
  var BLOCKS = 'p, li, h2, h3, h4, figure, table, blockquote, .tc-card, .tc-sit';
  function readingAnchor() {
    var line = topOffset() + 8, els = ROOT.querySelectorAll(BLOCKS), pick = null;
    for (var i = 0; i < els.length; i++) {
      var r = els[i].getBoundingClientRect();
      if (r.height && r.bottom > line && /\S/.test(els[i].textContent)) { pick = els[i]; break; }
    }
    if (!pick) return null;
    buildIndex();
    var off = pointToOffset(pick, 0);
    var sec = pick.closest('section[id]');
    var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    return {
      quote: idx.text.slice(off, off + 60), prefix: idx.text.slice(Math.max(0, off - CTX), off), pos: off,
      sec: sec && headingOf(sec) ? headingText(headingOf(sec)) : '',
      pct: Math.min(100, Math.round(window.pageYOffset / max * 100)), at: new Date().toISOString()
    };
  }
  function elementAt(offset) {
    for (var i = 0; i < idx.nodes.length; i++) {
      if (idx.starts[i] + idx.nodes[i].data.length > offset) {
        var e = idx.nodes[i].parentNode;
        return (e.closest && e.closest(BLOCKS)) || e;
      }
    }
    return null;
  }
  function resumeTo(p) {
    buildIndex();
    var at = locate({ quote: p.quote, prefix: p.prefix, suffix: '', pos: p.pos });
    var target = at >= 0 ? elementAt(at) : null;
    if (target) scrollToEl(target, false);
    else window.scrollTo(0, Math.round(p.pct / 100 * (document.documentElement.scrollHeight - window.innerHeight)));
  }
  function readJSON(k) { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) { return null; } }
  var userScrolled = false, posTimer;
  function savePos() {
    if (!userScrolled) return;
    var a = readingAnchor();
    if (!a) return;
    try {
      localStorage.setItem(POS_KEY, JSON.stringify(a));
      if (isModule) localStorage.setItem(LAST_KEY, JSON.stringify({ url: location.pathname, title: pageTitle(), sec: a.sec, pct: a.pct, at: a.at }));
    } catch (e) {}
  }
  ['wheel', 'touchmove', 'keydown', 'mousedown'].forEach(function (ev) {
    window.addEventListener(ev, function () { userScrolled = true; }, { passive: true });
  });
  window.addEventListener('scroll', function () { clearTimeout(posTimer); posTimer = setTimeout(savePos, 800); }, { passive: true });
  window.addEventListener('pagehide', savePos);
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') savePos(); });

  var resumeBar = el('div', 'rcn-ui rcn-resume no-print');
  resumeBar.setAttribute('role', 'region');
  resumeBar.setAttribute('aria-label', 'Resume reading');
  document.body.appendChild(resumeBar);
  function showResume(html, onGo, label) {
    resumeBar.innerHTML = '<div class="rcn-rs-txt">' + html + '</div>' +
      '<button type="button" class="rcn-rs-go">' + (label || 'Resume') + '</button>' +
      '<button type="button" class="rcn-x rcn-rs-x" aria-label="Dismiss">×</button>';
    resumeBar.classList.add('rcn-show');
    resumeBar.querySelector('.rcn-rs-go').addEventListener('click', function () { resumeBar.classList.remove('rcn-show'); onGo(); });
    resumeBar.querySelector('.rcn-rs-x').addEventListener('click', function () { resumeBar.classList.remove('rcn-show'); });
    var start = window.pageYOffset;
    window.addEventListener('scroll', function hide() {
      if (Math.abs(window.pageYOffset - start) > window.innerHeight * 1.5) {
        resumeBar.classList.remove('rcn-show');
        window.removeEventListener('scroll', hide);
      }
    }, { passive: true });
  }
  (function offerResume() {
    var saved = readJSON(POS_KEY);
    if (location.hash === '#rcm-resume') {
      try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
      if (saved) setTimeout(function () { resumeTo(saved); }, 300);
      return;
    }
    if (isModule && saved && !location.hash && saved.pct >= 5 && saved.pct < 97 && window.pageYOffset < 200) {
      showResume('<b>Pick up where you left off?</b><span>' + (saved.sec ? esc(saved.sec) + ' · ' : '') + saved.pct + '% through</span>',
        function () { resumeTo(saved); });
      return;
    }
    var last = readJSON(LAST_KEY);
    if (isHub && last && last.url && last.url !== location.pathname && last.pct < 97 &&
        Date.now() - new Date(last.at).getTime() < 60 * 864e5) {
      showResume('<b>Continue: ' + esc(last.title) + '</b><span>' + (last.sec ? esc(last.sec) + ' · ' : '') + last.pct + '% through</span>',
        function () { location.href = last.url + '#rcm-resume'; }, 'Continue');
    }
  })();

  /* ── Styles ──────────────────────────────────────────────────────────── */
  var css = '' +
    'mark.rcn-hl{color:inherit;border-radius:2px;padding:0 1px;cursor:pointer;box-decoration-break:clone;-webkit-box-decoration-break:clone;transition:box-shadow .2s}' +
    'mark.rcn-y{background:rgba(255,214,10,.45)}mark.rcn-g{background:rgba(72,187,99,.33)}mark.rcn-b{background:rgba(66,153,225,.30)}mark.rcn-p{background:rgba(236,72,153,.26)}' +
    'html[data-theme="dark"] mark.rcn-y{background:rgba(255,214,10,.30)}html[data-theme="dark"] mark.rcn-g{background:rgba(72,187,99,.32)}html[data-theme="dark"] mark.rcn-b{background:rgba(96,165,250,.32)}html[data-theme="dark"] mark.rcn-p{background:rgba(244,114,182,.30)}' +
    'mark.rcn-hl:focus-visible{outline:2px solid #1A6B72;outline-offset:1px}' +
    'mark.rcn-has-note.rcn-last::after{content:"";display:inline-block;width:.62em;height:.62em;margin-left:2px;vertical-align:super;border-radius:50% 50% 50% 0;background:#C55A11}' +
    'mark.rcn-flash{box-shadow:0 0 0 3px rgba(197,90,17,.55)}' +
    '.rcn-ui{font-family:"Nunito Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;font-size:14px;line-height:1.4;color:#1b2430}' +
    '.rcn-ui button{font:inherit;cursor:pointer}' +
    '.rcn-bar,.rcn-pop{position:fixed;z-index:100002;display:none;background:#fff;border:1px solid rgba(31,56,100,.18);border-radius:12px;box-shadow:0 10px 30px rgba(15,30,46,.22)}' +
    '.rcn-bar.rcn-show,.rcn-pop.rcn-show{display:flex}' +
    '.rcn-bar{align-items:center;gap:6px;padding:6px 8px}' +
    '.rcn-sw{width:28px;height:28px;border-radius:50%;border:2px solid rgba(0,0,0,.08);padding:0}' +
    '.rcn-sw-y{background:#ffd60a}.rcn-sw-g{background:#48bb63}.rcn-sw-b{background:#4299e1}.rcn-sw-p{background:#ec4899}' +
    '.rcn-sw.rcn-on{box-shadow:0 0 0 2px #fff,0 0 0 4px #1F3864}' +
    '.rcn-bar-note{display:flex;align-items:center;gap:5px;border:0;border-left:1px solid rgba(31,56,100,.15);background:none;color:#1F3864;font-weight:700;padding:4px 4px 4px 10px;margin-left:2px}' +
    '.rcn-bar-note svg{width:17px;height:17px}' +
    '@media (pointer:coarse){.rcn-bar{gap:12px;padding:10px 14px;border-radius:16px;box-shadow:0 12px 36px rgba(15,30,46,.32)}.rcn-sw{width:38px;height:38px}.rcn-bar-note{font-size:16px;padding:6px 4px 6px 14px}.rcn-bar-note svg{width:20px;height:20px}}' +
    '.rcn-pop{flex-direction:column;gap:8px;padding:10px;width:min(340px,calc(100vw - 16px))}' +
    '.rcn-pop-row{display:flex;align-items:center;justify-content:space-between;gap:8px}.rcn-pop-sw{display:flex;gap:8px}' +
    '.rcn-ta{width:100%;box-sizing:border-box;resize:vertical;min-height:84px;border:1px solid rgba(31,56,100,.25);border-radius:8px;padding:8px;font:15px/1.45 inherit;font-family:inherit;color:inherit;background:#fff}' +
    '.rcn-ta:focus{outline:2px solid #1A6B72;outline-offset:0}' +
    '.rcn-x{border:0;background:none;font-size:24px;line-height:1;color:#5a6677;padding:0 4px}' +
    '.rcn-del{border:0;background:none;color:#C00000;padding:6px 0}' +
    '.rcn-done{border:0;background:#1A6B72;color:#fff;border-radius:8px;padding:7px 16px;font-weight:700}' +
    '.rcn-drawer{position:fixed;z-index:100001;top:0;right:0;bottom:0;width:min(390px,94vw);background:#fff;box-shadow:-12px 0 36px rgba(15,30,46,.22);transform:translateX(105%);transition:transform .22s ease;display:flex;flex-direction:column}' +
    '.rcn-drawer.rcn-show{transform:none}' +
    '.rcn-dh{display:flex;justify-content:space-between;align-items:flex-start;padding:16px 16px 12px;border-bottom:1px solid rgba(31,56,100,.12);background:#1F3864;color:#fff}' +
    '.rcn-dh .rcn-x{color:#fff}.rcn-dt{font:800 18px Manrope,system-ui,sans-serif}.rcn-ds{font-size:12px;opacity:.8;margin-top:2px}' +
    '.rcn-list{flex:1;overflow:auto;padding:6px 16px 12px;outline:none}' +
    '.rcn-sec{font:700 11px Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#1A6B72;margin:14px 0 6px}' +
    '.rcn-item{border-left:4px solid #ffd60a;background:rgba(31,56,100,.035);border-radius:0 8px 8px 0;padding:8px 10px;margin-bottom:8px}' +
    '.rcn-b-g{border-color:#48bb63}.rcn-b-b{border-color:#4299e1}.rcn-b-p{border-color:#ec4899}' +
    '.rcn-go{display:block;text-align:left;border:0;background:none;padding:0;color:inherit;font-style:italic}' +
    '.rcn-go:disabled{cursor:default;opacity:.75}' +
    '.rcn-nt{margin-top:6px;white-space:normal}' +
    '.rcn-warn{margin-top:6px;font-size:12px;color:#C55A11}' +
    '.rcn-meta{margin-top:6px;font-size:12px;color:#6b7686;display:flex;gap:10px;align-items:center}' +
    '.rcn-meta button{border:0;background:none;padding:0;color:#1A6B72;font-weight:700;font-size:12px}.rcn-meta .rcn-rm{color:#C00000}' +
    '.rcn-armed{text-decoration:underline}' +
    '.rcn-empty{color:#5a6677;margin:18px 0}' +
    '.rcn-other{padding:0 16px;max-height:28vh;overflow:auto}.rcn-other:empty{display:none}' +
    '.rcn-other a{display:flex;justify-content:space-between;gap:8px;padding:5px 0;color:#1F3864;text-decoration:none;border-bottom:1px dashed rgba(31,56,100,.15);font-size:13px}' +
    '.rcn-other a span{background:#1A6B72;color:#fff;border-radius:9px;padding:0 7px;font-size:11px;align-self:center}' +
    '.rcn-actions{display:flex;flex-wrap:wrap;gap:6px;padding:12px 16px 16px;border-top:1px solid rgba(31,56,100,.12)}' +
    '.rcn-actions button{border:1px solid rgba(31,56,100,.22);background:#fff;color:#1F3864;border-radius:8px;padding:6px 10px;font-size:13px;font-weight:600}' +
    '.rcn-actions .rcn-danger{color:#C00000;border-color:rgba(192,0,0,.3)}' +
    '.rcn-fab{position:fixed;left:24px;bottom:136px;z-index:9998;width:44px;height:44px;border-radius:50%;border:0;background:#C55A11;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(0,0,0,.25);transition:transform .2s,box-shadow .2s}' +
    '.rcn-fab:hover{transform:scale(1.1);box-shadow:0 6px 20px rgba(0,0,0,.35)}.rcn-fab svg{width:19px;height:19px}' +
    '.rcn-tip{position:absolute;left:54px;background:rgba(31,56,100,.92);color:#fff;font-size:12px;font-weight:500;white-space:nowrap;padding:5px 10px;border-radius:6px;opacity:0;pointer-events:none;transition:opacity .15s}' +
    '.rcn-fab:hover .rcn-tip{opacity:1}' +
    '.rcn-count{position:absolute;top:-5px;right:-5px;min-width:18px;height:18px;border-radius:9px;background:#1F3864;border:2px solid #fff;color:#fff;font:700 10px/14px Inter,system-ui,sans-serif;text-align:center;padding:0 3px;box-sizing:border-box}' +
    '.rcn-rib{display:inline-flex;align-items:center;justify-content:center;vertical-align:middle;width:30px;height:30px;margin-left:8px;border:0;border-radius:8px;background:none;color:#8a96a8;cursor:pointer;opacity:.6;transition:opacity .15s,color .15s}' +
    '.rcn-rib svg{width:18px;height:18px}h2:hover .rcn-rib,h3:hover .rcn-rib,.rcn-rib:focus-visible{opacity:1}' +
    '.rcn-rib.rcn-on{opacity:1;color:#C55A11}.rcn-rib.rcn-on svg{fill:#C55A11}' +
    '@media (pointer:coarse){.rcn-rib{width:38px;height:38px;opacity:.85}}' +
    '.rcn-bms{padding:0 16px}.rcn-bm{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px dashed rgba(31,56,100,.15)}' +
    '.rcn-bm>svg{width:16px;height:16px;flex:none;color:#C55A11;fill:#C55A11}' +
    '.rcn-bm-go{flex:1;text-align:left;border:0;background:none;padding:2px 0;color:#1F3864;font-weight:600}.rcn-bm-go:disabled{opacity:.6}' +
    '.rcn-bm-x{border:0;background:none;color:#6b7686;font-size:20px;line-height:1;padding:0 4px}' +
    '.rcn-resume{position:fixed;z-index:100000;left:50%;bottom:22px;transform:translate(-50%,24px);opacity:0;pointer-events:none;display:flex;align-items:center;gap:12px;background:#1F3864;color:#fff;border-radius:14px;padding:10px 10px 10px 16px;box-shadow:0 12px 36px rgba(15,30,46,.35);width:max-content;max-width:min(94vw,560px);transition:opacity .2s,transform .2s}' +
    '.rcn-resume.rcn-show{opacity:1;transform:translate(-50%,0);pointer-events:auto}' +
    '.rcn-rs-txt{display:flex;flex-direction:column;min-width:0}.rcn-rs-txt b{font-weight:700}.rcn-rs-txt span{font-size:12.5px;opacity:.85;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
    '.rcn-rs-go{border:0;background:#C55A11;color:#fff;border-radius:10px;padding:9px 16px;font-weight:700;flex:none}' +
    '.rcn-resume .rcn-x{color:#fff;opacity:.85}' +
    '@media (pointer:coarse){.rcn-rs-go{padding:12px 18px;font-size:16px}}' +
    'html[data-theme="dark"] .rcn-bm-go{color:#e2b95f}html[data-theme="dark"] .rcn-resume{background:#0f1826;border:1px solid rgba(255,255,255,.14)}' +
    '@media print{.rcn-rib{display:none!important}}' +
    '.rcn-toast{position:fixed;z-index:100003;left:50%;bottom:24px;transform:translate(-50%,20px);opacity:0;pointer-events:none;background:#1F3864;color:#fff;padding:10px 16px;border-radius:10px;box-shadow:0 10px 30px rgba(15,30,46,.3);transition:opacity .2s,transform .2s;max-width:min(92vw,460px);text-align:center}' +
    '.rcn-toast.rcn-show{opacity:1;transform:translate(-50%,0)}' +
    '@media (pointer:coarse){.rcn-toast{bottom:auto;top:calc(env(safe-area-inset-top,0px) + 16px);transform:translate(-50%,-20px)}}' +
    'html[data-theme="dark"] .rcn-ui{color:#e6ebf2}' +
    'html[data-theme="dark"] .rcn-bar,html[data-theme="dark"] .rcn-pop,html[data-theme="dark"] .rcn-drawer{background:#162131;border-color:rgba(255,255,255,.14)}' +
    'html[data-theme="dark"] .rcn-ta,html[data-theme="dark"] .rcn-actions button{background:#0f1826;color:#e6ebf2;border-color:rgba(255,255,255,.2)}' +
    'html[data-theme="dark"] .rcn-bar-note,html[data-theme="dark"] .rcn-other a{color:#e2b95f}' +
    'html[data-theme="dark"] .rcn-item{background:rgba(255,255,255,.05)}' +
    'html[data-theme="dark"] .rcn-sec,html[data-theme="dark"] .rcn-meta button{color:#6cc3c9}' +
    'html[data-theme="dark"] .rcn-meta,html[data-theme="dark"] .rcn-empty{color:#9aa6b6}' +
    'html[data-theme="dark"] .rcn-dh{background:#0f1826}' +
    '@media print{.rcn-ui{display:none!important}mark.rcn-hl{-webkit-print-color-adjust:exact;print-color-adjust:exact}mark.rcn-has-note.rcn-last::after{display:none}}';
  var st = document.createElement('style');
  st.id = 'rcn-css';
  st.textContent = css;
  document.head.appendChild(st);

  /* ── Start ───────────────────────────────────────────────────────────── */
  restoreAll();
  if (notes.some(function (n) { return n.orphan; })) toast('Some notes could not be placed because the module text changed. They are kept in My notes.');
  refreshCount();
  try {
    if (!localStorage.getItem('rcm-notes-tip')) {
      setTimeout(function () { toast('Tip: select any text to highlight it or add a note. Notes stay on this device.'); }, 1500);
      localStorage.setItem('rcm-notes-tip', '1');
    }
  } catch (e) {}
})();
