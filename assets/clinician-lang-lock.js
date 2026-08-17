/* clinician-lang-lock.js — renalcarematters.com
 *
 * Clinician (physician) mode is English-only. This script makes the top-nav
 * language pills behave accordingly:
 *   • When physician mode is active, the guide is forced to display English
 *     (so clinician sections, which are authored English-only, never render
 *     blank for a visitor whose last-picked language was TL/CEB/KAP).
 *   • The non-EN pills are darkened + disabled purely by CSS
 *     (body.physician-mode .header-lang .lang-btn-g:not(#glb-en) in master CSS);
 *     this script keeps the *content* in sync with that.
 *   • The visitor's own language choice is preserved: switching back to the
 *     patient tab restores whatever language they had selected.
 *
 * It manipulates the DOM directly (data-lang visibility + pill .active state),
 * so it works regardless of the guide's inline language function name
 * (setLang / setGuideLang). Idempotent and dependency-free.
 */
(function () {
  var LANGS = ['en', 'tl', 'ceb', 'kap'];
  var LANG_KEY = 'wgmr-lang';

  function storedLang() {
    try {
      var v = localStorage.getItem(LANG_KEY);
      return LANGS.indexOf(v) >= 0 ? v : 'en';
    } catch (e) { return 'en'; }
  }

  function applyLangDisplay(lang) {
    // data-lang scheme: toggle the lang-hidden class
    var els = document.querySelectorAll('[data-lang]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      el.classList.toggle('lang-hidden', el.getAttribute('data-lang') !== lang);
    }
    // legacy class scheme (lang-en/lang-tl/...): toggle inline display
    for (var k = 0; k < LANGS.length; k++) {
      var cls = document.querySelectorAll('.lang-' + LANGS[k]);
      for (var n = 0; n < cls.length; n++) {
        cls[n].style.display = (LANGS[k] === lang) ? '' : 'none';
      }
    }
    // active state on the top-nav chips
    for (var j = 0; j < LANGS.length; j++) {
      var b = document.getElementById('glb-' + LANGS[j]);
      if (b) b.classList.toggle('active', LANGS[j] === lang);
    }
  }

  function sync() {
    if (document.body.classList.contains('physician-mode')) {
      applyLangDisplay('en');           // clinician mode → force English
    } else {
      applyLangDisplay(storedLang());   // patient mode → restore user's language
    }
  }

  // Public language setter for the top-nav chips. Many guides' chips call
  // setGuideLang(...) via inline onclick but never define it (only setLang),
  // so the switcher throws "setGuideLang is not defined" and does nothing.
  // Define a global fallback for BOTH names — but only when the guide didn't
  // already define its own (so guides with a working inline setLang/setGuideLang
  // keep theirs untouched). While in clinician mode the language is locked to EN.
  function publicSetLang(lang) {
    if (LANGS.indexOf(lang) < 0) lang = 'en';
    if (document.body.classList.contains('physician-mode')) lang = 'en';
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
    document.documentElement.setAttribute('lang', lang);
    applyLangDisplay(lang);
  }
  if (typeof window.setGuideLang !== 'function') window.setGuideLang = publicSetLang;
  if (typeof window.setLang !== 'function') window.setLang = publicSetLang;

  function init() {
    // React to Patient/Clinician tab toggles (they flip body.physician-mode).
    try {
      var mo = new MutationObserver(function (muts) {
        for (var i = 0; i < muts.length; i++) {
          if (muts[i].attributeName === 'class') { sync(); return; }
        }
      });
      mo.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    } catch (e) { /* MutationObserver unsupported — initial sync still runs */ }
    sync();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
