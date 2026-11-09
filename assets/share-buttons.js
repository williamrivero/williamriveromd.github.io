/*!
 * share-buttons.js — renalcarematters.com
 * Share bar for every content guide (journal-style, like NEJM / KDIGO / ASN).
 *
 *  - Compact icon row placed under the hero byline (.hero-meta), or under the
 *    first <h1> when a guide has no byline.
 *  - Labeled "Share this guide" panel where the guide content ends (before the
 *    glossary, else the references accordion, else the signature card).
 *
 * Networks: Facebook, X, LinkedIn, Bluesky, WhatsApp, Viber (touch devices
 * only; it needs the app), Email, Copy link, plus the system share sheet where
 * the browser supports it (most phones).
 * Shares the page's canonical URL. Styles are injected here (scoped .rcm-share
 * classes) so patch_master_css.py never touches them. Hidden in print.
 * Installed on guides by patch_share_buttons.py. Icon paths: Simple Icons (CC0).
 */
(function () {
  'use strict';
  if (window.__rcmShare) return;
  window.__rcmShare = true;

  var ICON = {
    facebook: 'M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z',
    x: 'M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z',
    linkedin: 'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z',
    bluesky: 'M5.202 2.857C7.954 4.922 10.913 9.11 12 11.358c1.087-2.247 4.046-6.436 6.798-8.501C20.783 1.366 24 .213 24 3.883c0 .732-.42 6.156-.667 7.037-.856 3.061-3.978 3.842-6.755 3.37 4.854.826 6.089 3.562 3.422 6.299-5.065 5.196-7.28-1.304-7.847-2.97-.104-.305-.152-.448-.153-.327 0-.121-.05.022-.153.327-.568 1.666-2.782 8.166-7.847 2.97-2.667-2.737-1.432-5.473 3.422-6.3-2.777.473-5.899-.308-6.755-3.369C.42 10.04 0 4.615 0 3.883c0-3.67 3.217-2.517 5.202-1.026',
    whatsapp: 'M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z',
    viber: 'M11.4 0C9.473.028 5.333.344 3.02 2.467 1.302 4.187.696 6.7.633 9.817.57 12.933.488 18.776 6.12 20.36h.003l-.004 2.416s-.037.977.61 1.177c.777.242 1.234-.5 1.98-1.302.407-.44.972-1.084 1.397-1.58 3.85.326 6.812-.416 7.15-.525.776-.252 5.176-.816 5.892-6.657.74-6.02-.36-9.83-2.34-11.546-.596-.55-3.006-2.3-8.375-2.323 0 0-.395-.025-1.037-.017zm.058 1.693c.545-.004.88.017.88.017 4.542.02 6.717 1.388 7.222 1.846 1.675 1.435 2.53 4.868 1.906 9.897v.002c-.604 4.878-4.174 5.184-4.832 5.395-.28.09-2.882.737-6.153.524 0 0-2.436 2.94-3.197 3.704-.12.12-.26.167-.352.144-.13-.033-.166-.188-.165-.414l.02-4.018c-4.762-1.32-4.485-6.292-4.43-8.895.054-2.604.543-4.738 1.996-6.173 1.96-1.773 5.474-2.018 7.11-2.03zm.38 2.602c-.167 0-.303.135-.304.302 0 .167.133.303.3.305 1.624.01 2.946.537 4.028 1.592 1.073 1.046 1.62 2.468 1.633 4.334.002.167.14.3.307.3.166-.002.3-.138.3-.304-.014-1.984-.618-3.596-1.816-4.764-1.19-1.16-2.692-1.753-4.447-1.765zm-3.96.695c-.19-.032-.4.005-.616.117l-.01.002c-.43.247-.816.562-1.146.932-.002.004-.006.004-.008.008-.267.323-.42.638-.46.948-.008.046-.01.093-.007.14 0 .136.022.27.065.4l.013.01c.135.48.473 1.276 1.205 2.604.42.768.903 1.5 1.446 2.186.27.344.56.673.87.984l.132.132c.31.308.64.6.984.87.686.543 1.418 1.027 2.186 1.447 1.328.733 2.126 1.07 2.604 1.206l.01.014c.13.042.265.064.402.063.046.002.092 0 .138-.008.31-.036.627-.19.948-.46.004 0 .003-.002.008-.005.37-.33.683-.72.93-1.148l.003-.01c.225-.432.15-.842-.18-1.12-.004 0-.698-.58-1.037-.83-.36-.255-.73-.492-1.113-.71-.51-.285-1.032-.106-1.248.174l-.447.564c-.23.283-.657.246-.657.246-3.12-.796-3.955-3.955-3.955-3.955s-.037-.426.248-.656l.563-.448c.277-.215.456-.737.17-1.248-.217-.383-.454-.756-.71-1.115-.25-.34-.826-1.033-.83-1.035-.137-.165-.31-.265-.502-.297zm4.49.88c-.158.002-.29.124-.3.282-.01.167.115.312.282.324 1.16.085 2.017.466 2.645 1.15.63.688.93 1.524.906 2.57-.002.168.13.306.3.31.166.003.305-.13.31-.297.025-1.175-.334-2.193-1.067-2.994-.74-.81-1.777-1.253-3.05-1.346h-.024zm.463 1.63c-.16.002-.29.127-.3.287-.008.167.12.31.288.32.523.028.875.175 1.113.422.24.245.388.62.416 1.164.01.167.15.295.318.287.167-.008.295-.15.287-.317-.03-.644-.215-1.178-.58-1.557-.367-.378-.893-.574-1.52-.607h-.018z'
  };
  var svg = function (d, stroke) {
    return stroke
      ? '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + d + '</svg>'
      : '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor"><path d="' + d + '"/></svg>';
  };
  var MAIL = svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>', true);
  var LINK = svg('<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/>', true);
  var MORE = svg('<path d="M12 3v12"/><path d="m7 8 5-5 5 5"/><path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/>', true);
  var CHECK = svg('<path d="m5 12 5 5 9-10"/>', true);

  function meta(sel) { var m = document.querySelector(sel); return m ? (m.getAttribute('content') || m.getAttribute('href') || '') : ''; }
  var url = meta('link[rel="canonical"]') || (location.origin + location.pathname);
  var title = (meta('meta[property="og:title"]') || document.title || '').replace(/\s+/g, ' ').trim();
  var eu = encodeURIComponent(url), et = encodeURIComponent(title);
  var touch = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;

  var NETS = [
    { k: 'facebook', n: 'Facebook', c: '#1565D8', h: 'https://www.facebook.com/sharer/sharer.php?u=' + eu },
    { k: 'x', n: 'X', c: '#000000', h: 'https://x.com/intent/post?url=' + eu + '&text=' + et },
    { k: 'linkedin', n: 'LinkedIn', c: '#0A66C2', h: 'https://www.linkedin.com/sharing/share-offsite/?url=' + eu },
    { k: 'bluesky', n: 'Bluesky', c: '#0066CC', h: 'https://bsky.app/intent/compose?text=' + encodeURIComponent(title + ' ' + url) },
    { k: 'whatsapp', n: 'WhatsApp', c: '#157A3E', h: 'https://wa.me/?text=' + encodeURIComponent(title + ' ' + url) },
    { k: 'viber', n: 'Viber', c: '#5E4BD8', h: 'viber://forward?text=' + encodeURIComponent(title + ' ' + url), app: true, touchOnly: true },
    { k: 'email', n: 'Email', c: '#1F3864', h: 'mailto:?subject=' + et + '&body=' + encodeURIComponent(title + '\n\n' + url), app: true, icon: MAIL },
    { k: 'copy', n: 'Copy link', c: '#1A6B72', icon: LINK }
  ].filter(function (n) { return !n.touchOnly || touch; });

  var CSS = [
    '.rcm-share{display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin:12px 0 0;}',
    '.rcm-share-lbl{font:700 0.68rem/1 Inter,Manrope,system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:inherit;opacity:.8;margin-right:4px;}',
    '.rcm-share-btn,.rcm-share-btn:visited{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;border:1px solid rgba(31,56,100,.22);background:rgba(255,255,255,.6);color:#1F3864!important;cursor:pointer;padding:0;text-decoration:none;transition:background .15s,color .15s,border-color .15s;position:relative;}',
    '.rcm-share-btn svg{width:16px;height:16px;}',
    '.rcm-share-btn:hover,.rcm-share-btn:focus-visible{background:var(--rcm-c);border-color:var(--rcm-c);color:#fff!important;outline:none;}',
    '.rcm-share-btn:focus-visible{box-shadow:0 0 0 3px rgba(26,107,114,.35);}',
    '.rcm-share-tip{position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);background:#1e2a38;color:#fff;font:600 .7rem/1 Manrope,system-ui,sans-serif;padding:5px 8px;border-radius:5px;white-space:nowrap;pointer-events:none;}',
    '.rcm-share-panel{max-width:860px;margin:28px auto 8px;padding:0 20px;}',
    '.rcm-share-panel h2{font:700 .8rem/1.2 Inter,Manrope,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--text,#1e2a38);margin:0 0 12px;padding-bottom:10px;border-bottom:2px solid var(--border,#d8dee8);}',
    '.rcm-share-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;}',
    '.rcm-share-big{display:flex;align-items:center;justify-content:center;gap:9px;min-height:42px;padding:0 14px;border:0;border-radius:6px;background:var(--rcm-c);color:#fff!important;font:700 .78rem/1 Manrope,Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;text-decoration:none!important;cursor:pointer;transition:filter .15s,transform .15s;}',
    '.rcm-share-big svg{width:17px;height:17px;flex:none;}',
    '.rcm-share-big:hover,.rcm-share-big:focus-visible{filter:brightness(1.12);transform:translateY(-1px);outline:none;}',
    '.rcm-share-big:focus-visible{box-shadow:0 0 0 3px rgba(26,107,114,.4);}',
    '.rcm-share-big.is-copied{background:#2E6B3E;}',
    'html[data-theme="dark"] .rcm-share-btn,body.dark-mode .rcm-share-btn{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.25);color:#e6ecf5!important;}',
    'html[data-theme="dark"] .rcm-share-btn:hover,body.dark-mode .rcm-share-btn:hover{color:#fff!important;}',
    'html[data-theme="dark"] .rcm-share-panel h2,body.dark-mode .rcm-share-panel h2{color:#e6ecf5;border-bottom-color:#2c3a52;}',
    'html[data-theme="dark"] .rcm-share-big[data-net="x"],body.dark-mode .rcm-share-big[data-net="x"]{background:#000;box-shadow:inset 0 0 0 1px #3a4458;}',
    '@media (max-width:520px){.rcm-share-grid{grid-template-columns:1fr 1fr;}.rcm-share-big{font-size:.72rem;padding:0 10px;}}',
    '@media print{.rcm-share,.rcm-share-panel{display:none!important;}}'
  ].join('\n');

  function langSpans(map) {
    // Mirror the guide's 4-language pattern; show whichever language is active now.
    var active = 'en';
    var vis = document.querySelector('[data-lang]:not(.lang-hidden)');
    if (vis) active = vis.getAttribute('data-lang') || 'en';
    if (!document.querySelector('[data-lang="tl"]')) return map.en;
    return ['en', 'tl', 'ceb', 'kap'].map(function (l) {
      return '<span data-lang="' + l + '"' + (l === active ? '' : ' class="lang-hidden"') + '>' + map[l] + '</span>';
    }).join('');
  }

  function popup(href) {
    var w = 620, h = 560;
    var left = (window.screenX || 0) + Math.max(0, (window.outerWidth - w) / 2);
    var top = (window.screenY || 0) + Math.max(0, (window.outerHeight - h) / 3);
    var win = window.open(href, 'rcmshare', 'noopener,noreferrer,width=' + w + ',height=' + h + ',left=' + left + ',top=' + top);
    if (!win) window.open(href, '_blank', 'noopener');
  }

  function copy(btn) {
    var done = function () {
      if (btn.classList.contains('rcm-share-big')) {
        var old = btn.innerHTML;
        btn.classList.add('is-copied'); btn.innerHTML = CHECK + 'Link copied';
        setTimeout(function () { btn.classList.remove('is-copied'); btn.innerHTML = old; }, 1800);
      } else {
        var tip = document.createElement('span'); tip.className = 'rcm-share-tip'; tip.textContent = 'Link copied';
        btn.appendChild(tip); setTimeout(function () { tip.remove(); }, 1600);
      }
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(url).then(done, function () { fallback(); });
    } else fallback();
    function fallback() {
      var ta = document.createElement('textarea'); ta.value = url; ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-1000px;opacity:0;';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { window.prompt('Copy this link:', url); }
      ta.remove();
    }
  }

  function wire(root) {
    root.addEventListener('click', function (e) {
      var b = e.target.closest('[data-net]'); if (!b) return;
      var net = b.getAttribute('data-net');
      if (net === 'copy') { e.preventDefault(); copy(b); return; }
      if (net === 'native') {
        e.preventDefault();
        navigator.share({ title: title, url: url }).catch(function () {});
        return;
      }
      var n = NETS.filter(function (x) { return x.k === net; })[0];
      if (n && !n.app) { e.preventDefault(); popup(n.h); }
    });
  }

  function item(n, big) {
    var icon = n.icon || svg(ICON[n.k]);
    var tag = n.h ? 'a' : 'button';
    var attrs = n.h ? ' href="' + n.h.replace(/"/g, '&quot;') + '"' + (n.app ? '' : ' target="_blank" rel="noopener noreferrer"') : ' type="button"';
    var label = n.k === 'copy' ? 'Copy link' : (n.k === 'native' ? 'More sharing options' : 'Share on ' + n.n);
    if (n.k === 'email') label = 'Share by email';
    return '<' + tag + attrs + ' class="' + (big ? 'rcm-share-big' : 'rcm-share-btn') + '" data-net="' + n.k + '" style="--rcm-c:' + n.c + '" aria-label="' + label + '"' + (big ? '' : ' title="' + label + '"') + '>' + icon + (big ? n.n : '') + '</' + tag + '>';
  }

  function init() {
    if (document.querySelector('.rcm-share, .rcm-share-panel')) return;
    var st = document.createElement('style'); st.id = 'rcm-share-css'; st.textContent = CSS;
    document.head.appendChild(st);

    var list = NETS.slice();
    if (touch && navigator.share) list.push({ k: 'native', n: 'More', c: '#475569', icon: MORE });

    // 1) Compact icon row under each hero byline (dual heroes get one each).
    var anchors = document.querySelectorAll('.hero-meta');
    if (!anchors.length) { var h1 = document.querySelector('h1'); if (h1) anchors = [h1]; }
    Array.prototype.forEach.call(anchors, function (a) {
      var bar = document.createElement('div');
      bar.className = 'rcm-share'; bar.setAttribute('role', 'group'); bar.setAttribute('aria-label', 'Share this guide');
      bar.innerHTML = '<span class="rcm-share-lbl">' + langSpans({ en: 'Share', tl: 'Ibahagi', ceb: 'Ipaambit', kap: 'Ibahagi' }) + '</span>' +
        list.map(function (n) { return item(n, false); }).join('');
      a.parentNode.insertBefore(bar, a.nextSibling);
      wire(bar);
    });

    // 2) Labeled panel where the guide content ends: before the glossary,
    //    else the references accordion, else the signature card.
    var sig = document.querySelector('.glossary-acc') || document.querySelector('.ref-acc') || document.querySelector('.dr-card-wrap');
    if (sig) {
      var p = document.createElement('section');
      p.className = 'rcm-share-panel'; p.setAttribute('aria-label', 'Share this guide');
      p.innerHTML = '<h2>' + langSpans({ en: 'Share this guide', tl: 'Ibahagi ang gabay na ito', ceb: 'Ipaambit kini nga giya', kap: 'Ibahagi me ing gabay a iti' }) + '</h2>' +
        '<div class="rcm-share-grid">' + list.map(function (n) { return item(n, true); }).join('') + '</div>';
      sig.parentNode.insertBefore(p, sig);
      wire(p);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
