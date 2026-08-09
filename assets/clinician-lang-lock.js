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
    var els = document.querySelectorAll('[data-lang]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      el.classList.toggle('lang-hidden', el.getAttribute('data-lang') !== lang);
    }
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
