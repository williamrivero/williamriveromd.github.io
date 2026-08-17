/*!
 * renalcarematters.com — Image Lightbox v2.1
 *
 * Inline images in guide figures behave like book illustrations:
 *   • Single click / tap   → lightbox (magnified view with caption + abbreviations)
 *   • Double-click / tap   → open full image in a new tab (skip lightbox)
 *   • Click overlay or ×   → close lightbox, return to reading position
 *   • Click lightbox image → close lightbox
 *   • Double-click lb img  → open in new tab
 *   • ESC key              → close lightbox
 *
 * Caption structure expected in each <figure>:
 *   <figcaption>
 *     <p class="fig-desc">Plain-language description of the image.</p>
 *     <dl class="fig-abbrevs">
 *       <dt>UACR</dt><dd>Urine Albumin-to-Creatinine Ratio</dd>
 *       <dt>eGFR</dt><dd>Estimated Glomerular Filtration Rate</dd>
 *     </dl>
 *   </figcaption>
 * Falls back gracefully to raw figcaption text or img alt when
 * the structured markup is absent.
 *
 * v2.1 fixes two bandwidth / correctness bugs from v2.0:
 *   1. The lightbox now uses img.currentSrc (the WebP the browser already
 *      loaded from <picture>) instead of img.getAttribute('src') (the PNG
 *      fallback), so opening the lightbox is a cache hit rather than a
 *      fresh full-size PNG download. Same fix on double-click-open-in-new-
 *      tab, so users don't get magically served a heavier PNG either.
 *   2. Caption extraction now uses .innerText (which respects display:none
 *      set by [data-lang].lang-hidden) instead of .textContent (which
 *      returned every hidden translation sibling concatenated together).
 *      The fig-abbrevs <dt>/<dd> pairs are also cloned rather than string-
 *      copied so their data-lang / lang-hidden attributes carry over and
 *      the site's global CSS hides the inactive languages.
 */
(function () {
  'use strict';

  var DBLCLICK_MS = 280;
  var IMG_SEL = 'figure img, .illus-wrap img';

  // ── Overlay elements (lazily created) ──────────────────────────────────────
  var overlay, lbImg, lbDesc, lbAbbrevs, lbCapPanel;

  // Prefer currentSrc — the URL the browser actually loaded (WebP when the
  // <picture> declared one) — over the src attribute (which is the PNG
  // fallback). Using src would trigger a fresh full-size PNG download even
  // though the WebP is already in the browser's memory cache; that made the
  // lightbox visibly slow and doubled the bandwidth. currentSrc reuses the
  // exact resource the guide already rendered, so the lightbox is instant.
  function bestSrc(img) {
    return img.currentSrc || img.getAttribute('src') || '';
  }

  // Text extraction that honours the site's [data-lang].lang-hidden rule
  // (display:none !important in MASTER_CSS). Using textContent would pick up
  // every hidden translation sibling and concatenate all four languages into
  // one caption; innerText walks only rendered nodes. Falls back to
  // textContent if innerText is empty for any reason (e.g. detached DOM).
  function visibleText(el) {
    if (!el) return '';
    var t = (el.innerText || '').trim();
    if (!t) t = (el.textContent || '').replace(/\s+/g, ' ').trim();
    return t;
  }

  function buildOverlay() {
    if (document.getElementById('img-lb')) {
      overlay    = document.getElementById('img-lb');
      lbImg      = overlay.querySelector('.lb-img');
      lbDesc     = overlay.querySelector('.lb-desc');
      lbAbbrevs  = overlay.querySelector('.lb-abbrevs');
      lbCapPanel = overlay.querySelector('.lb-caption-panel');
      return;
    }

    overlay = document.createElement('div');
    overlay.id        = 'img-lb';
    overlay.className = 'lb-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Image viewer');
    overlay.innerHTML =
      '<button class="lb-close" aria-label="Close image viewer">×</button>' +
      '<div class="lb-body">' +
        '<img class="lb-img" src="" alt="">' +
        '<div class="lb-caption-panel">' +
          '<p class="lb-desc"></p>' +
          '<dl class="lb-abbrevs"></dl>' +
        '</div>' +
      '</div>' +
      '<p class="lb-hint">' +
        'Click to close · Double‑click image to open in new tab' +
      '</p>';

    document.body.appendChild(overlay);
    lbImg      = overlay.querySelector('.lb-img');
    lbDesc     = overlay.querySelector('.lb-desc');
    lbAbbrevs  = overlay.querySelector('.lb-abbrevs');
    lbCapPanel = overlay.querySelector('.lb-caption-panel');

    // Close button
    overlay.querySelector('.lb-close').addEventListener('click', function (e) {
      e.stopPropagation();
      closeLB();
    });

    // Click on overlay background (not on .lb-body content) → close
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeLB();
    });

    // Single click on lightbox image → close; double-click → new tab
    var _lbLastClick = 0;
    lbImg.addEventListener('click', function (e) {
      e.stopPropagation();
      var now = Date.now();
      if (now - _lbLastClick < DBLCLICK_MS) {
        openNewTab(lbImg.currentSrc || lbImg.getAttribute('src'));
        _lbLastClick = 0;
      } else {
        _lbLastClick = now;
        // Single click on lb-img = close and return to reading
        closeLB();
      }
    });
  }

  // ── Open / close ──────────────────────────────────────────────────────────
  function openLB(img) {
    buildOverlay();

    // Use the same resource the browser already loaded (bestSrc → currentSrc
    // when available) so opening the lightbox is a cache hit and adds zero
    // extra bytes. decoding=async + fetchpriority=high tell the browser this
    // paint is now the priority, without blocking the click.
    lbImg.decoding = 'async';
    lbImg.fetchPriority = 'high';
    lbImg.src = bestSrc(img);
    lbImg.alt = img.alt || '';

    // Resolve caption: structured figcaption > raw figcaption > illus-caption > alt
    var cap = null;
    var fig = img.closest('figure');
    if (fig) cap = fig.querySelector('figcaption');
    if (!cap) {
      var wrap = img.closest('.illus-wrap');
      if (wrap) {
        var sib = wrap.nextElementSibling;
        if (sib && (sib.classList.contains('illus-caption') ||
                    sib.tagName === 'FIGCAPTION')) cap = sib;
      }
    }

    var descText = '', hasAbbrevs = false;
    if (cap) {
      var descEl  = cap.querySelector('.fig-desc');
      var abbrEl  = cap.querySelector('.fig-abbrevs');
      descText = descEl ? visibleText(descEl) : visibleText(cap);
      // Copy the abbrevs list by cloning so the DOM keeps its data-lang /
      // lang-hidden attributes; the site's global rule
      // `[data-lang].lang-hidden{display:none!important}` then hides the
      // non-active languages exactly as it does in the guide body.
      if (abbrEl && abbrEl.children.length) {
        lbAbbrevs.innerHTML = '';
        for (var i = 0; i < abbrEl.children.length; i++) {
          lbAbbrevs.appendChild(abbrEl.children[i].cloneNode(true));
        }
        hasAbbrevs = true;
      }
    }
    if (!descText) descText = img.alt || '';

    lbDesc.textContent       = descText;
    lbDesc.style.display     = descText  ? '' : 'none';
    lbAbbrevs.style.display  = hasAbbrevs ? '' : 'none';
    if (!hasAbbrevs) lbAbbrevs.innerHTML = '';
    lbCapPanel.style.display = (descText || hasAbbrevs) ? '' : 'none';

    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLB() {
    if (!overlay) return;
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  function openNewTab(src) {
    if (src) window.open(src, '_blank', 'noopener,noreferrer');
  }

  // ── Inline image: single click → lightbox, double-click → new tab ─────────
  var _timer     = null;
  var _pendingImg = null;

  document.addEventListener('click', function (e) {
    if (overlay && overlay.classList.contains('open')) return; // lb handles its own clicks

    var img = e.target.closest ? e.target.closest(IMG_SEL) : null;
    if (!img) return;

    if (_pendingImg === img) {
      // Second click within DBLCLICK_MS → double-click detected
      clearTimeout(_timer);
      _timer = _pendingImg = null;
      openNewTab(bestSrc(img));
    } else {
      _pendingImg = img;
      _timer = setTimeout(function () {
        _timer = _pendingImg = null;
        openLB(img);
      }, DBLCLICK_MS);
    }
  });

  // Touch: double-tap backup (iOS sometimes fires touchend without two clicks)
  var _lastTap = { el: null, t: 0 };
  document.addEventListener('touchend', function (e) {
    if (overlay && overlay.classList.contains('open')) return;
    var img = e.target.closest ? e.target.closest(IMG_SEL) : null;
    if (!img) return;
    var now = Date.now();
    if (_lastTap.el === img && now - _lastTap.t < 350) {
      e.preventDefault();
      clearTimeout(_timer);
      _timer = _pendingImg = null;
      openNewTab(bestSrc(img));
      _lastTap = { el: null, t: 0 };
    } else {
      _lastTap = { el: img, t: now };
    }
  }, { passive: false });

  // ESC → close
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLB();
  });

  // ── Wire cursor + tooltip on all guide images ──────────────────────────────
  function wireCursors() {
    document.querySelectorAll(IMG_SEL).forEach(function (img) {
      img.style.cursor = 'zoom-in';
      if (!img.title) {
        img.title = 'Click to enlarge · Double-click to open in new tab';
      }
    });
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    buildOverlay();
    wireCursors();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
