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

  /* ---- Vocabulary translation ----
     The WHO ICD-10 dataset uses British medical spellings (anaemia, oedema,
     haemorrhage, hyperkalaemia) and older terminology (chronic renal failure
     rather than chronic kidney disease; renal dialysis rather than
     hemodialysis). Most clinicians type American spellings and modern
     abbreviations. We translate the query so a user typing "anemia in CKD"
     finds anaemia + chronic renal failure rows. ----------------------------*/

  // American → British medical spellings (single-word substitutions)
  const SPELLING_NORM = {
    'anemia':'anaemia','anemic':'anaemic',
    'hyperkalemia':'hyperkalaemia','hypokalemia':'hypokalaemia',
    'hypernatremia':'hypernatraemia','hyponatremia':'hyponatraemia',
    'hypercalcemia':'hypercalcaemia','hypocalcemia':'hypocalcaemia',
    'hyperphosphatemia':'hyperphosphataemia','hypophosphatemia':'hypophosphataemia',
    'hypomagnesemia':'hypomagnesaemia','hypermagnesemia':'hypermagnesaemia',
    'acidemia':'acidaemia','alkalemia':'alkalaemia',
    'uremia':'uraemia','uremic':'uraemic',
    'azotemia':'azotaemia','bacteremia':'bacteraemia',
    'leukemia':'leukaemia','septicemia':'septicaemia',
    'ischemia':'ischaemia','ischemic':'ischaemic',
    'edema':'oedema','edematous':'oedematous',
    'esophagus':'oesophagus','esophageal':'oesophageal',
    'orthopnea':'orthopnoea','dyspnea':'dyspnoea','apnea':'apnoea',
    'diarrhea':'diarrhoea','gonorrhea':'gonorrhoea',
    'menorrhea':'menorrhoea','amenorrhea':'amenorrhoea','dysmenorrhea':'dysmenorrhoea',
    'hemoglobin':'haemoglobin',
    'hemorrhage':'haemorrhage','hemorrhagic':'haemorrhagic','hemorrhoid':'haemorrhoid',
    'hematuria':'haematuria','hematemesis':'haematemesis',
    'hematology':'haematology','hematoma':'haematoma','hematopoietic':'haematopoietic',
    'anesthesia':'anaesthesia','anesthetic':'anaesthetic',
    'pediatric':'paediatric','pediatrics':'paediatrics',
    'fetal':'foetal','fetus':'foetus',
    'celiac':'coeliac','tumor':'tumour','cesarean':'caesarean',
    'gynecology':'gynaecology','gynecologic':'gynaecologic',
  };

  // Abbreviations expanded to WHO-aligned terminology
  // (CKD → "chronic renal failure" because WHO ICD-10 N18 uses "renal failure";
  //  HD → "renal dialysis" because WHO uses "renal dialysis" / "extracorporeal dialysis",
  //  not "hemodialysis" in code titles.)
  const ABBREVIATIONS = {
    'ckd':'chronic renal failure','esrd':'end-stage renal disease','eskd':'end-stage renal disease',
    'aki':'acute renal failure','arf':'acute renal failure','crf':'chronic renal failure',
    'hd':'renal dialysis','pd':'peritoneal dialysis','rrt':'renal dialysis',
    'hemodialysis':'renal dialysis','haemodialysis':'renal dialysis',
    'dm':'diabetes mellitus','t1d':'type 1 diabetes','t2d':'type 2 diabetes',
    't1dm':'type 1 diabetes mellitus','t2dm':'type 2 diabetes mellitus',
    'iddm':'insulin-dependent diabetes','niddm':'non-insulin-dependent diabetes',
    'gdm':'gestational diabetes',
    'htn':'hypertension',
    'mi':'myocardial infarction','stemi':'st elevation myocardial infarction',
    'nstemi':'non-st elevation myocardial infarction',
    'hf':'heart failure','chf':'congestive heart failure',
    'cad':'ischaemic heart','ihd':'ischaemic heart',
    'copd':'chronic obstructive pulmonary',
    'cap':'pneumonia','hap':'pneumonia','vap':'pneumonia',
    'uti':'urinary tract infection',
    'gn':'glomerulonephritis','sle':'systemic lupus erythematosus',
    'dkd':'diabetic kidney',
    'cva':'cerebrovascular','tia':'transient cerebral ischaemic',
    'af':'atrial fibrillation','afib':'atrial fibrillation',
    'pe':'pulmonary embolism','dvt':'phlebitis and thrombophlebitis',
    'gerd':'gastro-oesophageal reflux','aaa':'aortic aneurysm',
    'avf':'arteriovenous fistula','tb':'tuberculosis',
    'hiv':'human immunodeficiency virus','aids':'acquired immunodeficiency',
    'mds':'myelodysplastic',
  };

  const STOPWORDS = new Set([
    'the','a','an','in','on','with','and','or','of','to','for','at','by',
    'is','was','as','that','this','it','from','due','because','since','no',
  ]);

  // Normalize a query string: lowercase, expand abbreviations and American
  // spellings to WHO British. Preserves order; does not alter punctuation
  // semantics other than whitespace collapsing.
  function normalizeQuery(text) {
    const lower = text.toLowerCase().trim();
    if (!lower) return '';
    const parts = lower.split(/(\s+)/);  // preserve spaces
    return parts.map(p => {
      if (/^\s+$/.test(p)) return ' ';
      const alpha = p.replace(/[^a-z]/g, '');
      if (!alpha) return p;
      if (ABBREVIATIONS[alpha]) return p.replace(alpha, ABBREVIATIONS[alpha]);
      if (SPELLING_NORM[alpha]) return p.replace(alpha, SPELLING_NORM[alpha]);
      return p;
    }).join('').replace(/\s+/g, ' ').trim();
  }

  function tokenize(text) {
    return text.split(/[\s,;:./\-()]+/)
      .map(t => t.toLowerCase())
      .filter(t => t.length > 1 && !STOPWORDS.has(t));
  }

  /* ---- Single-mode filter — normalization-aware substring ---- */
  function filter(query) {
    if (!DATA) return [];
    const raw = query.trim().toLowerCase();
    if (!raw) return DATA;
    const norm = normalizeQuery(query);

    // If the raw query is a known abbreviation (AKI, CKD, ESRD, HF, MI, …),
    // the raw 2-4 character form would substring-match unrelated words
    // (anis-AKI-asis, aph-AKI-a, kaw-AKI-, etc.). Search ONLY the expanded
    // form so the user sees the diagnosis codes they actually meant.
    const rawAlpha = raw.replace(/[^a-z]/g, '');
    const isPureAbbreviation =
      !/\s/.test(raw) && ABBREVIATIONS.hasOwnProperty(rawAlpha);
    if (isPureAbbreviation && norm) {
      return DATA.filter(r => r._cl.indexOf(norm) !== -1);
    }

    // Try the normalized form first; if it differs from raw and yields hits,
    // prefer it (handles American → British spelling: anemia → anaemia).
    if (norm && norm !== raw) {
      const normHits = DATA.filter(r => r._cl.indexOf(norm) !== -1 || r._cl.indexOf(raw) !== -1);
      if (normHits.length > 0) return normHits;
    }
    return DATA.filter(r => r._cl.indexOf(raw) !== -1);
  }

  /* ---- Batch-mode ranking ----
     Multi-criteria scoring per row (higher = better):
       Code field
         exact code             → 120
         code startsWith query  → 100
         code contains query    →  55
       Title field (normalized)
         title === query        → 115
         title startsWith query →  92
         title contains query   →  78
       Token AND/OR
         all tokens matched     →  +bonus to ≥ 65
         each matched token     →  +ratio + flat
   --------------------------------- */
  function rankMatches(rawQuery, topN) {
    if (!DATA) return [];
    const q = rawQuery.trim();
    if (!q) return [];

    const qLower = q.toLowerCase();
    const norm = normalizeQuery(q);
    const qTokens = Array.from(new Set(tokenize(norm || qLower)));

    const isCodeLike = /^[a-z]\d/i.test(q.replace(/\s/g, ''));
    const qCodeForm = q.replace(/[^a-z0-9.]/gi, '').toUpperCase();

    if (qTokens.length === 0 && !isCodeLike) return [];

    const scored = [];
    for (let i = 0; i < DATA.length; i++) {
      const r = DATA[i];
      let s = 0;
      const tl = r._tl;
      const codeU = r.c.toUpperCase();

      // Code matching
      if (isCodeLike) {
        if (codeU === qCodeForm) s = Math.max(s, 120);
        else if (codeU.startsWith(qCodeForm)) s = Math.max(s, 100);
        else if (codeU.indexOf(qCodeForm) !== -1) s = Math.max(s, 55);
      }

      // Phrase matching (both raw and normalized)
      if (tl === qLower || tl === norm) s = Math.max(s, 115);
      else if (tl.startsWith(qLower) || (norm && tl.startsWith(norm))) s = Math.max(s, 92);
      else if (tl.indexOf(qLower) !== -1 || (norm && tl.indexOf(norm) !== -1)) s = Math.max(s, 78);

      // Token AND/OR
      if (qTokens.length > 0) {
        let matched = 0;
        for (const tok of qTokens) {
          if (tl.indexOf(tok) !== -1) matched++;
        }
        if (matched > 0) {
          const ratio = matched / qTokens.length;
          const tokScore = ratio * 50 + matched * 5;
          s = Math.max(s, tokScore);
          if (matched === qTokens.length) s = Math.max(s, 65);
        }
      }

      if (s > 0) scored.push({ r, s });
    }

    scored.sort((a, b) => b.s - a.s || a.r.c.localeCompare(b.r.c));
    return scored.slice(0, topN).map(x => x.r);
  }

  function splitBatch(text) {
    return text
      .split(/[\n;]+/)
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
        <div class="icd10-header">
          <div class="icd10-header-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="20" y1="20" x2="16.5" y2="16.5"/></svg>
          </div>
          <div class="icd10-header-text">
            <div class="icd10-header-eyebrow">Interactive Tool · WHO ICD-10</div>
            <div class="icd10-header-title">Search 10,469 ICD-10 Codes</div>
          </div>
          <div class="icd10-header-cta" aria-hidden="true">Try it →</div>
        </div>
        <div class="icd10-mode-tabs" role="tablist">
          <button class="icd10-tab icd10-tab-active" data-mode="single" role="tab" aria-selected="true">Single search</button>
          <button class="icd10-tab" data-mode="batch" role="tab" aria-selected="false">Batch mode</button>
        </div>

        <!-- Single mode -->
        <div class="icd10-pane icd10-pane-single" data-pane="single">
          <div class="icd10-bar">
            <input type="search" class="icd10-input" placeholder="Search ICD-10 — try: anemia in CKD, N18, hyperkalemia, heart failure…" aria-label="Search ICD-10 codes" autocomplete="off" spellcheck="false">
            <button class="icd10-btn icd10-btn-ghost icd10-btn-reset" type="button" data-act="clear-single" aria-label="Clear search" disabled>Clear</button>
            <span class="icd10-count" aria-live="polite"></span>
          </div>
          <div class="icd10-hint">American spellings (<em>anemia</em>, <em>edema</em>, <em>hemodialysis</em>) and abbreviations (<em>CKD</em>, <em>ESRD</em>, <em>HF</em>, <em>MI</em>, <em>HTN</em>, <em>DM</em>) are auto-translated to the WHO ICD-10 vocabulary the dataset uses.</div>
          <div class="icd10-status">Tap the box above to load the ICD-10 dataset (≈ 700&nbsp;KB, one-time).</div>
          <div class="icd10-results"></div>
          <div class="icd10-pager"></div>
        </div>

        <!-- Batch mode -->
        <div class="icd10-pane icd10-pane-batch" data-pane="batch" hidden>
          <label class="icd10-batch-label" for="${cssId(host) + '-batch'}">Paste diagnoses — one per line (or semicolon-separated). Up to ${MAX_BATCH_LINES} at a time. American spellings and abbreviations (CKD, ESRD, HF, MI, HTN, DM) are auto-translated.</label>
          <textarea id="${cssId(host) + '-batch'}" class="icd10-batch-input" rows="6" placeholder="Heart failure with CKD&#10;Anemia in CKD&#10;Hyperkalemia&#10;Community-acquired pneumonia&#10;ESRD on hemodialysis"></textarea>
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

    const clearSingleBtn = paneSingle.querySelector('[data-act="clear-single"]');
    function syncClearState() {
      if (clearSingleBtn) clearSingleBtn.disabled = !input.value;
    }

    let debounce;
    input.addEventListener('input', () => {
      syncClearState();
      clearTimeout(debounce);
      debounce = setTimeout(() => {
        page = 0;
        currentQuery = input.value;
        currentRows = filter(currentQuery);
        renderSingle();
      }, 120);
    });

    clearSingleBtn.addEventListener('click', () => {
      input.value = '';
      currentQuery = '';
      page = 0;
      currentRows = DATA ? DATA : [];
      syncClearState();
      renderSingle();
      input.focus();
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
