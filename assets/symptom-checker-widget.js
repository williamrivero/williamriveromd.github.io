/* ──────────────────────────────────────────────────────────────────
   Symptom Checker floating widget
   ──────────────────────────────────────────────────────────────────
   - Injects a floating 🩺 button on every guide page.
   - Click → opens a fullscreen modal with /guides/symptom-checker.html
     embedded in an iframe (no navigation away).
   - Bails out automatically when loaded on symptom-checker.html itself
     (prevents iframe-of-self loops).
   - Reads the current language from localStorage ('wgmr-lang') so the
     button label matches the site's language toggle.
   - No external dependencies. Vanilla JS.
   ────────────────────────────────────────────────────────────────── */
(function () {
  if (/symptom-checker\.html/i.test(location.pathname)) return;
  if (document.querySelector('.sc-fab')) return;

  var LABELS = {
    en:  { btn: 'Symptom Check', title: 'Symptom Checker', close: 'Close' },
    tl:  { btn: 'Pagsusuri ng Sintomas', title: 'Pagsusuri ng Sintomas', close: 'Isara' },
    ceb: { btn: 'Pagsusi sa Sintomas',   title: 'Pagsusi sa Sintomas',    close: 'Sirado' },
    kap: { btn: 'Pamanyiasat king Sakit', title: 'Pamanyiasat king Sakit', close: 'Isarad' }
  };

  function currentLang() {
    var l = 'en';
    try { l = (localStorage.getItem('wgmr-lang') || 'en').toLowerCase(); } catch (e) {}
    return LABELS[l] ? l : 'en';
  }

  // ── Inject styles ───────────────────────────────────────────────
  var style = document.createElement('style');
  style.textContent = [
    '.sc-fab{position:fixed;bottom:22px;right:22px;z-index:9998;',
      'display:flex;align-items:center;gap:8px;padding:11px 18px 11px 14px;',
      'background:#0f1e2e;color:#fff;border:none;border-radius:30px;',
      'font-family:"DM Sans",sans-serif;font-size:14px;font-weight:600;',
      'letter-spacing:.01em;cursor:pointer;',
      'box-shadow:0 6px 20px rgba(15,30,46,.3),0 2px 6px rgba(15,30,46,.18);',
      'transition:transform .15s,box-shadow .15s,background .15s;}',
    '.sc-fab:hover{background:#1a2e4a;transform:translateY(-1px);',
      'box-shadow:0 10px 28px rgba(15,30,46,.35),0 3px 8px rgba(15,30,46,.22);}',
    '.sc-fab:active{transform:translateY(0);}',
    '.sc-fab-icon{font-size:18px;line-height:1;}',
    '.sc-fab-text{font-size:13px;}',
    '.sc-fab-pulse{position:absolute;top:0;right:0;width:10px;height:10px;',
      'border-radius:50%;background:#d4af4f;box-shadow:0 0 0 0 rgba(212,175,79,.6);',
      'animation:scPulse 2s infinite;}',
    '@keyframes scPulse{0%{box-shadow:0 0 0 0 rgba(212,175,79,.6);}',
      '70%{box-shadow:0 0 0 10px rgba(212,175,79,0);}',
      '100%{box-shadow:0 0 0 0 rgba(212,175,79,0);}}',
    '.sc-modal{position:fixed;inset:0;z-index:9999;background:rgba(8,13,22,.7);',
      'display:none;align-items:center;justify-content:center;padding:24px;',
      'backdrop-filter:blur(2px);}',
    '.sc-modal.open{display:flex;}',
    '.sc-modal-frame{position:relative;width:min(980px,100%);',
      'height:min(92vh,1000px);background:#fff;border-radius:14px;',
      'overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.4);}',
    '.sc-modal-close{position:absolute;top:10px;right:14px;z-index:2;',
      'width:34px;height:34px;border-radius:50%;border:none;',
      'background:rgba(15,30,46,.85);color:#fff;font-size:20px;line-height:1;',
      'cursor:pointer;display:flex;align-items:center;justify-content:center;',
      'transition:background .15s;}',
    '.sc-modal-close:hover{background:#0f1e2e;}',
    '.sc-iframe{width:100%;height:100%;border:0;}',
    '@media (max-width:600px){',
      '.sc-modal{padding:0;}',
      '.sc-modal-frame{width:100%;height:100%;border-radius:0;}',
      '.sc-fab{bottom:16px;right:16px;padding:10px 14px;}',
      '.sc-fab-text{display:none;}',
      '.sc-fab-icon{font-size:20px;}',
    '}',
    '@media print{.sc-fab,.sc-modal{display:none!important;}}',
    'html[data-theme="dark"] .sc-modal-frame{background:#0f1520;}'
  ].join('');
  document.head.appendChild(style);

  // ── Floating button ─────────────────────────────────────────────
  function build() {
    var lang = currentLang();
    var btn = document.createElement('button');
    btn.className = 'sc-fab';
    btn.setAttribute('aria-label', LABELS[lang].title);
    btn.innerHTML =
      '<span class="sc-fab-icon" aria-hidden="true">🩺</span>' +
      '<span class="sc-fab-text">' + LABELS[lang].btn + '</span>' +
      '<span class="sc-fab-pulse" aria-hidden="true"></span>';
    btn.addEventListener('click', openModal);
    document.body.appendChild(btn);

    // Keep the button label in sync with the page's language toggle.
    document.addEventListener('click', function (e) {
      if (e.target && e.target.classList && e.target.classList.contains('lang-btn')) {
        setTimeout(updateLabel, 50);
      }
    });
    window.addEventListener('storage', updateLabel);
  }

  function updateLabel() {
    var lang = currentLang();
    var fab = document.querySelector('.sc-fab');
    if (!fab) return;
    fab.setAttribute('aria-label', LABELS[lang].title);
    var txt = fab.querySelector('.sc-fab-text');
    if (txt) txt.textContent = LABELS[lang].btn;
    var modal = document.querySelector('.sc-modal');
    if (modal) {
      var c = modal.querySelector('.sc-modal-close');
      if (c) c.setAttribute('aria-label', LABELS[lang].close);
    }
  }

  // ── Modal (lazy-created on first open) ─────────────────────────
  var modalEl = null;
  function openModal() {
    var lang = currentLang();
    if (!modalEl) {
      modalEl = document.createElement('div');
      modalEl.className = 'sc-modal';
      modalEl.innerHTML =
        '<div class="sc-modal-frame">' +
          '<button class="sc-modal-close" aria-label="' + LABELS[lang].close + '">×</button>' +
          '<iframe class="sc-iframe" src="symptom-checker.html?embed=1" title="' + LABELS[lang].title + '" loading="lazy"></iframe>' +
        '</div>';
      document.body.appendChild(modalEl);
      modalEl.querySelector('.sc-modal-close').addEventListener('click', closeModal);
      modalEl.addEventListener('click', function (e) {
        if (e.target === modalEl) closeModal();
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modalEl.classList.contains('open')) closeModal();
      });
    }
    modalEl.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    if (!modalEl) return;
    modalEl.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
