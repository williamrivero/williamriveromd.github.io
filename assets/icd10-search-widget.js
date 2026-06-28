/* ───────────────────────────────────────────────────────────────────────────
   icd10-search-widget.js — WHO ICD-10 lookup, vanilla JS, lazy-loaded
   ----------------------------------------------------------------------------
   Two modes:
     · Single — type a single query, paginated table of matches
     · Batch  — paste multiple diagnoses (newline- or comma-separated);
                returns ranked top-N matches per query line, grouped

   Mount any element with class .icd10-search-mount and the script injects
   the widget. The dataset (/assets/icd10-who.json, ~700 KB) is fetched on
   first user interaction (focus/click), not on page load — so host page
   LCP is unaffected.

   Optional data-* attributes:
     data-page-size="25"        — rows per page in single mode (default 25)
     data-batch-top="8"         — top-N matches per line in batch mode (default 8)
     data-data-url="..."        — override JSON URL (default /assets/icd10-who.json)
     data-chapters-url="..."    — override chapters URL (default /assets/icd10-chapters.json)
     data-compact="true"        — hide the chapter column in single mode
   ─────────────────────────────────────────────────────────────────────────── */

(function () {
  'use strict';

  if (window.__icd10SearchWidgetLoaded) return;
  window.__icd10SearchWidgetLoaded = true;

  const DEFAULT_DATA = '/assets/icd10-who.json';
  const DEFAULT_CHAPS = '/assets/icd10-chapters.json';
  const DEFAULT_PAGE = 25;
  const DEFAULT_BATCH_TOP = 8;
  const MAX_BATCH_LINES = 30;

  /* ---- Shared dataset cache (one fetch per page) ---- */
  let DATA = null;        // [{c, t, _ch, _cl, _tl}]
  let DATA_PROMISE = null;

  function fetchData(dataUrl, chapsUrl) {
    if (DATA_PROMISE) return DATA_PROMISE;
    DATA_PROMISE = Promise.all([
      fetch(dataUrl).then(r => r.json()),
      fetch(chapsUrl).then(r => r.json()),
    ]).then(([rows, chaps]) => {
      const codePrefix = (code) => code.replace(/[^A-Z0-9]/g, '').slice(0, 3);
      const inRange = (prefix, range) => {
        const [lo, hi] = range.split('-');
        return prefix >= lo && prefix <= hi;
      };
      const cache = new Map();
      DATA = rows.map(r => {
        const p = codePrefix(r.c);
        let chName = cache.get(p);
        if (chName === undefined) {
          const ch = chaps.find(c => inRange(p, c.r));
          chName = ch ? ch.n : '';
          cache.set(p, chName);
        }
        const cl = (r.c + ' ' + r.t).toLowerCase();
        const tl = r.t.toLowerCase();
        return { c: r.c, t: r.t, _ch: chName, _cl: cl, _tl: tl };
      });
      return DATA;
    }).catch(err => {
      console.error('[icd10-search] dataset load failed', err);
      DATA_PROMISE = null;
      throw err;
    });
    return DATA_PROMISE;
  }

  /* ---- Single-mode filter (substring, sorted by relevance) ---- */
  function filter(query) {
    if (!DATA) return [];
    const q = query.trim().toLowerCase();
    if (!q) return DATA;
    return DATA.filter(r => r._cl.indexOf(q) !== -1);
  }

  /* ---- Batch-mode ranking ----
     For each query line, score every dataset row and return the top-N.
     Scoring (higher = better):
       title === q              → 110
       title startsWith q       → 85
       code startsWith q (UC)   → 80
       title word startsWith q  → 70
       title contains q         → 50
       code contains q (UC)     → 35
   --------------------------------- */
  function rankMatches(rawQuery, topN) {
    if (!DATA) return [];
    const q = rawQuery.trim().toLowerCase();
    if (!q) return [];
    const qUC = q.toUpperCase();
    const out = [];
    for (let i = 0; i < DATA.length; i++) {
      const r = DATA[i];
      let s = 0;
      if (r._tl === q) s = 110;
      else if (r._tl.startsWith(q)) s = 85;
      else if (r.c.toUpperCase().startsWith(qUC)) s = 80;
      else if (r._tl.indexOf(' ' + q) !== -1) s = 70;
      else if (r._tl.indexOf(q) !== -1) s = 50;
      else if (r.c.toUpperCase().indexOf(qUC) !== -1) s = 35;
      if (s > 0) out.push({ r, s });
    }
    out.sort((a, b) => b.s - a.s || a.r.c.localeCompare(b.r.c));
    return out.slice(0, topN).map(x => x.r);
  }

  function splitBatch(text) {
    return text
      .split(/[\n,;]+/)
      .map(s => s.trim())
      .filter(s => s.length > 0);
  }

  /* ---- Highlight helper ---- */
  function highlight(text, query) {
    if (!query) return escapeHtml(text);
    const q = query.trim();
    if (!q) return escapeHtml(text);
    const escQ = q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const re = new RegExp('(' + escQ + ')', 'ig');
    return escapeHtml(text).replace(re, '<mark class="icd10-hl">$1</mark>');
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[c]));
  }

  /* ---- Render a single widget instance ---- */
  function mount(host) {
    const pageSize = parseInt(host.dataset.pageSize, 10) || DEFAULT_PAGE;
    const batchTop = parseInt(host.dataset.batchTop, 10) || DEFAULT_BATCH_TOP;
    const dataUrl = host.dataset.dataUrl || DEFAULT_DATA;
    const chapsUrl = host.dataset.chaptersUrl || DEFAULT_CHAPS;
    const compact = host.dataset.compact === 'true';

    host.innerHTML = `
      <div class="icd10-widget">
        <div class="icd10-mode-tabs" role="tablist">
          <button class="icd10-tab icd10-tab-active" data-mode="single" role="tab" aria-selected="true">Single search</button>
          <button class="icd10-tab" data-mode="batch" role="tab" aria-selected="false">Batch mode</button>
        </div>

        <!-- Single mode -->
        <div class="icd10-pane icd10-pane-single" data-pane="single">
          <div class="icd10-bar">
            <input type="search" class="icd10-input" placeholder="Search ICD-10 — try: anemia, N18, hyperkalemia, dialysis…" aria-label="Search ICD-10 codes" autocomplete="off" spellcheck="false">
            <span class="icd10-count" aria-live="polite"></span>
          </div>
          <div class="icd10-status">Tap the box above to load the ICD-10 dataset (≈ 700&nbsp;KB, one-time).</div>
          <div class="icd10-results"></div>
          <div class="icd10-pager"></div>
        </div>

        <!-- Batch mode -->
        <div class="icd10-pane icd10-pane-batch" data-pane="batch" hidden>
          <label class="icd10-batch-label" for="${cssId(host) + '-batch'}">Paste diagnoses — one per line, or comma-separated. Up to ${MAX_BATCH_LINES} at a time.</label>
          <textarea id="${cssId(host) + '-batch'}" class="icd10-batch-input" rows="6" placeholder="Heart failure with CKD&#10;Anemia in CKD&#10;Hyperkalemia&#10;Pneumonia&#10;ESRD on hemodialysis"></textarea>
          <div class="icd10-batch-actions">
            <button class="icd10-btn icd10-btn-primary" type="button" data-act="match">Match ICD-10 codes</button>
            <button class="icd10-btn icd10-btn-ghost" type="button" data-act="clear">Clear</button>
            <span class="icd10-batch-hint">Top ${batchTop} per line, ranked by relevance.</span>
          </div>
          <div class="icd10-batch-status"></div>
          <div class="icd10-batch-results"></div>
        </div>

        <p class="icd10-footnote">WHO ICD-10 (international classification) — <strong>10,469 codes</strong>. PhilHealth's grouper is built on this dataset. For production claims, confirm against your hospital's official ICD-10-PH list.</p>
      </div>
    `;

    /* ---- Mode toggle ---- */
    const tabs = host.querySelectorAll('.icd10-tab');
    const paneSingle = host.querySelector('[data-pane="single"]');
    const paneBatch = host.querySelector('[data-pane="batch"]');
    tabs.forEach(t => t.addEventListener('click', () => {
      tabs.forEach(x => {
        x.classList.toggle('icd10-tab-active', x === t);
        x.setAttribute('aria-selected', x === t ? 'true' : 'false');
      });
      const mode = t.dataset.mode;
      paneSingle.hidden = mode !== 'single';
      paneBatch.hidden = mode !== 'batch';
      ensureLoaded();
    }));

    /* ---- Single-mode logic ---- */
    const input = paneSingle.querySelector('.icd10-input');
    const status = paneSingle.querySelector('.icd10-status');
    const countEl = paneSingle.querySelector('.icd10-count');
    const results = paneSingle.querySelector('.icd10-results');
    const pager = paneSingle.querySelector('.icd10-pager');

    let currentRows = [];
    let page = 0;
    let currentQuery = '';

    function renderSingle() {
      const total = currentRows.length;
      const pageCount = Math.max(1, Math.ceil(total / pageSize));
      if (page >= pageCount) page = pageCount - 1;
      if (page < 0) page = 0;
      const start = page * pageSize;
      const end = Math.min(start + pageSize, total);
      const slice = currentRows.slice(start, end);

      countEl.textContent = total === 0
        ? 'No matches'
        : `${total.toLocaleString()} match${total === 1 ? '' : 'es'}`;

      if (slice.length === 0) {
        results.innerHTML = `<div class="icd10-empty">No codes match that search. Try a different term, or a 3-character code prefix like <code>N18</code>.</div>`;
        pager.innerHTML = '';
        return;
      }

      const colChapter = compact ? '' : '<th>Chapter</th>';
      const rowChapter = (r) => compact ? '' : `<td class="icd10-chapter">${escapeHtml(r._ch || '—')}</td>`;
      const rowsHtml = slice.map(r => `
        <tr>
          <td class="icd10-code">${highlight(r.c, currentQuery)}</td>
          <td class="icd10-title">${highlight(r.t, currentQuery)}</td>
          ${rowChapter(r)}
        </tr>
      `).join('');

      results.innerHTML = `
        <div class="icd10-table-wrap">
          <table class="icd10-table">
            <thead><tr><th class="icd10-code-col">Code</th><th>Title</th>${colChapter}</tr></thead>
            <tbody>${rowsHtml}</tbody>
          </table>
        </div>
      `;

      pager.innerHTML = pageCount > 1 ? `
        <button class="icd10-page-btn" data-act="prev" ${page === 0 ? 'disabled' : ''}>‹ Prev</button>
        <span class="icd10-page-info">Page ${page + 1} of ${pageCount.toLocaleString()} — showing ${start + 1}–${end}</span>
        <button class="icd10-page-btn" data-act="next" ${page === pageCount - 1 ? 'disabled' : ''}>Next ›</button>
      ` : '';
    }

    pager.addEventListener('click', (e) => {
      const btn = e.target.closest('.icd10-page-btn');
      if (!btn) return;
      if (btn.dataset.act === 'prev') page--;
      if (btn.dataset.act === 'next') page++;
      renderSingle();
      results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });

    let debounce;
    input.addEventListener('input', () => {
      clearTimeout(debounce);
      debounce = setTimeout(() => {
        page = 0;
        currentQuery = input.value;
        currentRows = filter(currentQuery);
        renderSingle();
      }, 120);
    });

    /* ---- Batch-mode logic ---- */
    const batchInput = paneBatch.querySelector('.icd10-batch-input');
    const batchStatus = paneBatch.querySelector('.icd10-batch-status');
    const batchResults = paneBatch.querySelector('.icd10-batch-results');
    const btnMatch = paneBatch.querySelector('[data-act="match"]');
    const btnClear = paneBatch.querySelector('[data-act="clear"]');

    function runBatch() {
      const raw = batchInput.value;
      const lines = splitBatch(raw);
      if (lines.length === 0) {
        batchStatus.innerHTML = `<span class="icd10-status-msg">Paste at least one diagnosis above, then tap "Match ICD-10 codes".</span>`;
        batchResults.innerHTML = '';
        return;
      }
      if (lines.length > MAX_BATCH_LINES) {
        batchStatus.innerHTML = `<span class="icd10-status-msg icd10-status-warn">Too many lines — please limit to ${MAX_BATCH_LINES}. Only the first ${MAX_BATCH_LINES} will be matched.</span>`;
      } else {
        batchStatus.innerHTML = `<span class="icd10-status-msg">${lines.length} ${lines.length === 1 ? 'diagnosis' : 'diagnoses'} matched. Top ${batchTop} ranked candidates per line.</span>`;
      }
      const items = lines.slice(0, MAX_BATCH_LINES);

      const html = items.map((q, idx) => {
        const matches = rankMatches(q, batchTop);
        const rowsHtml = matches.length
          ? matches.map(r => `
              <tr>
                <td class="icd10-code">${highlight(r.c, q)}</td>
                <td class="icd10-title">${highlight(r.t, q)}</td>
                ${compact ? '' : `<td class="icd10-chapter">${escapeHtml(r._ch || '—')}</td>`}
              </tr>
            `).join('')
          : `<tr><td colspan="${compact ? 2 : 3}" class="icd10-batch-no">No matching codes. Try a more specific term (e.g. <code>anemia in CKD</code> instead of <code>tired</code>).</td></tr>`;
        return `
          <div class="icd10-batch-group">
            <div class="icd10-batch-q">
              <span class="icd10-batch-q-num">#${idx + 1}</span>
              <span class="icd10-batch-q-text">${escapeHtml(q)}</span>
              <span class="icd10-batch-q-count">${matches.length} of top ${batchTop}</span>
            </div>
            <div class="icd10-table-wrap">
              <table class="icd10-table">
                <thead><tr><th class="icd10-code-col">Code</th><th>Title</th>${compact ? '' : '<th>Chapter</th>'}</tr></thead>
                <tbody>${rowsHtml}</tbody>
              </table>
            </div>
          </div>
        `;
      }).join('');

      batchResults.innerHTML = html;
    }

    btnMatch.addEventListener('click', () => {
      ensureLoaded().then(runBatch);
    });
    btnClear.addEventListener('click', () => {
      batchInput.value = '';
      batchStatus.innerHTML = '';
      batchResults.innerHTML = '';
      batchInput.focus();
    });

    /* ---- Dataset lazy-load ---- */
    let loadStarted = false;
    function ensureLoaded() {
      if (loadStarted && DATA_PROMISE) return DATA_PROMISE;
      loadStarted = true;
      status.textContent = 'Loading ICD-10 dataset…';
      return fetchData(dataUrl, chapsUrl).then(() => {
        status.style.display = 'none';
        // Initial render in single mode after load
        if (!paneSingle.hidden) {
          currentRows = DATA;
          renderSingle();
        }
        return DATA;
      }).catch(() => {
        status.textContent = 'Could not load the ICD-10 dataset. Refresh the page to retry.';
        status.className = 'icd10-status icd10-status-err';
      });
    }

    input.addEventListener('focus', ensureLoaded, { once: true });
    input.addEventListener('click', ensureLoaded, { once: true });
    batchInput.addEventListener('focus', ensureLoaded, { once: true });
  }

  function cssId(el) {
    if (!el.id) el.id = 'icd10-' + Math.random().toString(36).slice(2, 9);
    return el.id;
  }

  function initAll() {
    document.querySelectorAll('.icd10-search-mount').forEach((host) => {
      if (host.dataset._icd10Mounted) return;
      host.dataset._icd10Mounted = '1';
      mount(host);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
