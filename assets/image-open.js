/*!
 * williamriveromd.com — open full image in a new tab on double-click / double-tap.
 * Replaces the legacy ".zoomable" hover-zoom. Applies to in-page guide figures
 * (and any image still carrying the .zoomable class). Idempotent and dependency-free.
 */
(function () {
  function fullSrc(img) {
    // Prefer the <img src> (usually the PNG fallback / original); fall back to the loaded source.
    return img.getAttribute('src') || img.currentSrc || img.src || '';
  }
  function openImage(img) {
    var src = fullSrc(img);
    if (src) window.open(src, '_blank', 'noopener');
  }
  function wire(img) {
    if (img.dataset.dblopen === '1') return; // avoid double-binding
    img.dataset.dblopen = '1';
    if (!img.title) img.title = 'Double-tap or double-click to open the full image';
    // Desktop: double-click
    img.addEventListener('dblclick', function (e) {
      e.preventDefault();
      openImage(img);
    });
    // Touch: double-tap (two taps within 350 ms)
    var lastTap = 0;
    img.addEventListener('touchend', function (e) {
      var now = Date.now();
      if (now - lastTap < 350) {
        e.preventDefault();
        openImage(img);
      }
      lastTap = now;
    }, { passive: false });
  }
  function init() {
    document.querySelectorAll('main figure img, img.zoomable').forEach(wire);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
