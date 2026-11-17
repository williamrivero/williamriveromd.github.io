/* Animated hero for the drug database index pages (drugs/, drugs/category/, drugs/supplements/).
   Same family as the guides and calculators index heroes: a slow gradient drift plus faint
   drifting pharmacology tokens (generic names, PK terms, dosing shorthand), capsule glyphs and
   pharmacy silhouettes (beaker, syringe, mortar & pestle, inhaler, bottle, IV bag...) at varied speeds.
   Palette follows the "Medicines" category color (rose #9d174d). Respects prefers-reduced-motion.
   Loaded with <script defer src="/assets/drug-hero.js">; activates only on <section class="hero">
   inside <body class="dd-index-page">. */
(function () {
  var body = document.body;
  if (!body || !body.classList.contains('dd-index-page')) return;
  var hero = document.querySelector('section.hero');
  if (!hero) return;

  var css = [
    'body.dd-index-page section.hero{position:relative;overflow:hidden;',
    ' background:linear-gradient(135deg,#fbe9f0 0%,#fdf2f6 46%,#f6e2ec 100%)!important;',
    ' background-size:240% 240%!important;animation:dd-hero-shift 26s ease-in-out infinite alternate;}',
    'html[data-theme="dark"] body.dd-index-page section.hero,body.dark-mode.dd-index-page section.hero{',
    ' background:linear-gradient(135deg,#2a0f1d 0%,#4a1730 48%,#22101a 100%)!important;}',
    '@keyframes dd-hero-shift{0%{background-position:0% 0%}50%{background-position:90% 40%}100%{background-position:100% 100%}}',
    'body.dd-index-page section.hero>.container{position:relative;z-index:2}',
    'body.dd-index-page section.hero h1{color:#5c0f30!important}',
    'body.dd-index-page section.hero .hero-tag{color:#7a1640!important;border-color:rgba(157,23,77,.32)!important}',
    'body.dd-index-page section.hero .hero-sub{color:#4a2a38!important}',
    'html[data-theme="dark"] body.dd-index-page section.hero h1,body.dark-mode.dd-index-page section.hero h1{color:#fff!important}',
    'html[data-theme="dark"] body.dd-index-page section.hero .hero-tag,body.dark-mode.dd-index-page section.hero .hero-tag{color:#fbd5e4!important;border-color:rgba(251,213,228,.45)!important}',
    'html[data-theme="dark"] body.dd-index-page section.hero .hero-sub,body.dark-mode.dd-index-page section.hero .hero-sub{color:rgba(253,236,243,.88)!important}',
    '.dd-hero-fx{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:1}',
    '.dd-hero-tok{position:absolute;top:0;left:0;white-space:nowrap;opacity:0;will-change:transform,opacity;',
    ' font-family:ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;font-weight:600}',
    '.dd-hero-tok.t0{color:#9d174d}.dd-hero-tok.t1{color:#6b3a52}.dd-hero-tok.t2{color:#b8962e}.dd-hero-tok.t3{color:#c2416f}',
    'html[data-theme="dark"] .dd-hero-tok.t0,body.dark-mode .dd-hero-tok.t0{color:#f9a8c9}',
    'html[data-theme="dark"] .dd-hero-tok.t1,body.dark-mode .dd-hero-tok.t1{color:#fdecf3}',
    'html[data-theme="dark"] .dd-hero-tok.t2,body.dark-mode .dd-hero-tok.t2{color:#d4af4f}',
    'html[data-theme="dark"] .dd-hero-tok.t3,body.dark-mode .dd-hero-tok.t3{color:#f472a6}',
    '.dd-hero-cap{display:inline-block;width:2.4em;height:1em;border-radius:.5em;',
    ' background:linear-gradient(90deg,currentColor 0 50%,transparent 50%);border:2px solid currentColor;box-sizing:border-box}',
    '.dd-hero-ico{display:block;width:1em;height:1em;fill:currentColor;transform-origin:50% 50%}',
    '.dd-hero-ico.flip{animation:dd-hero-flip var(--fd) linear infinite}',
    '.dd-hero-ico.rock{animation:dd-hero-rock var(--fd) ease-in-out infinite alternate}',
    '@keyframes dd-hero-flip{from{transform:perspective(200px) rotateY(0deg)}to{transform:perspective(200px) rotateY(360deg)}}',
    '@keyframes dd-hero-rock{from{transform:rotate(-28deg)}to{transform:rotate(28deg)}}',
    '@keyframes dd-hero-drift{0%{transform:translate(var(--x0),var(--y0)) rotate(var(--r0));opacity:0}',
    ' 10%{opacity:var(--op)}90%{opacity:var(--op)}100%{transform:translate(var(--x1),var(--y1)) rotate(var(--r1));opacity:0}}',
    '@keyframes dd-hero-float{0%{transform:translate(var(--x0),var(--y0)) rotate(var(--rot));opacity:0}',
    ' 12%{opacity:var(--op)}88%{opacity:var(--op)}100%{transform:translate(var(--x1),var(--y1)) rotate(var(--rot));opacity:0}}',
    '@media (prefers-reduced-motion:reduce){body.dd-index-page section.hero{animation:none}.dd-hero-tok{animation:none!important;opacity:.14}.dd-hero-tok.ico{display:none}}',
    '@media print{.dd-hero-fx{display:none}}'
  ].join('\n');
  var st = document.createElement('style');
  st.id = 'dd-hero-css';
  st.textContent = css;
  document.head.appendChild(st);

  var fx = document.createElement('div');
  fx.className = 'dd-hero-fx';
  fx.setAttribute('aria-hidden', 'true');
  hero.insertBefore(fx, hero.firstChild);
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var TOKENS = [
    'amlodipine', 'losartan', 'metformin', 'allopurinol', 'apixaban', 'vancomycin',
    'dapagliflozin', 'calcitriol', 'sevelamer', 'epoetin alfa', 'gabapentin', 'colchicine',
    't½', 'Vd', 'Cmax', 'AUC', 'fe (renal)', 'CrCl', 'eGFR', 'mg/kg', 'q12h', 'q24h',
    'post-HD dose', 'CYP3A4', 'P-gp', 'PO', 'IV', 'Rx', 'protein binding', 'dialyzable',
    '◐', '◐', '◐', '◐'
  ];
  var N = 22;
  var frag = document.createDocumentFragment();
  function rnd(a, b) { return a + Math.random() * (b - a); }
  for (var i = 0; i < N; i++) {
    var el = document.createElement('span');
    var tok = TOKENS[(i * 7) % TOKENS.length];
    el.className = 'dd-hero-tok t' + (i % 4);
    if (tok === '◐') {
      var cap = document.createElement('span');
      cap.className = 'dd-hero-cap';
      el.appendChild(cap);
    } else {
      el.textContent = tok;
    }
    el.style.fontSize = rnd(11, 24).toFixed(1) + 'px';
    el.style.top = rnd(-4, 100).toFixed(1) + '%';
    var y0 = rnd(-10, 10);
    el.style.setProperty('--x0', rnd(-12, 8).toFixed(1) + 'vw');
    el.style.setProperty('--x1', rnd(86, 116).toFixed(1) + 'vw');
    el.style.setProperty('--y0', y0.toFixed(1) + 'px');
    el.style.setProperty('--y1', (y0 + rnd(-34, 34)).toFixed(1) + 'px');
    el.style.setProperty('--rot', rnd(-10, 10).toFixed(1) + 'deg');
    el.style.setProperty('--op', rnd(0.10, 0.26).toFixed(2));
    var dur = rnd(18, 36), delay = -rnd(0, dur);
    el.style.animation = 'dd-hero-float ' + dur.toFixed(1) + 's ' + delay.toFixed(1) + 's linear infinite';
    frag.appendChild(el);
  }

  /* Pharmacy silhouettes (24-unit, filled): beaker, syringe, mortar & pestle, inhaler, pill bottle,
     tablet, IV bag, dropper, test tube, capsule pair. Each drifts at its own speed. */
  var ICONS = {
    beaker: 'M8 2h8v2h-1v5.2l5.3 9.2c.9 1.6-.2 3.6-2 3.6H5.7c-1.8 0-2.9-2-2-3.6L9 9.2V4H8V2zm3 2v5.7L8.6 14h6.8L13 9.7V4h-2z',
    syringe: 'M17.7 1.3l5 5-1.4 1.4-1.1-1.1-1.4 1.4 1.4 1.4-1.4 1.4-1.4-1.4-8.5 8.5H6.1l-2.4 2.4-1.4-1.4 2.4-2.4v-2.8l8.5-8.5-1.4-1.4 1.4-1.4 1.4 1.4 1.4-1.4-1.1-1.1 1.4-1.4zM9 13l2 2 1-1-2-2-1 1zm2.5-2.5l2 2 1-1-2-2-1 1z',
    mortar: 'M19.6 1.6l1.8 1.1-5.6 8.3H22v2c0 3.4-2.3 6.3-5.5 7.2l.5 1.8H7l.5-1.8C4.3 19.3 2 16.4 2 13v-2h11.4l6.2-9.4z',
    inhaler: 'M9 1h6v7h3c1.1 0 2 .9 2 2v9c0 1.1-.9 2-2 2h-4l-2 2H4c-1.1 0-2-.9-2-2v-4c0-1.1.9-2 2-2h3v-5c0-1.1.9-2 2-2V1z',
    bottle: 'M7 1h10v3H7V1zm-1 4h12v2.2c1.2.6 2 1.8 2 3.3V21c0 1.1-.9 2-2 2H6c-1.1 0-2-.9-2-2V10.5c0-1.5.8-2.7 2-3.3V5zm2 8v5h8v-5H8z',
    tablet: 'M12 2a10 10 0 110 20 10 10 0 010-20zm-7.9 9h15.8A8 8 0 0012 4a8 8 0 00-7.9 7z',
    ivbag: 'M9 1h6v2h2c1.1 0 2 .9 2 2v11c0 2.2-1.8 4-4 4h-2v1.5h-2V20H9c-2.2 0-4-1.8-4-4V5c0-1.1.9-2 2-2h2V1zm-1 8v2h4V9H8zm0 4v2h6v-2H8z',
    dropper: 'M18.4 1.6l4 4-2.1 2.1-1.4-1.4-1.4 1.4 1.4 1.4-1.4 1.4-1.4-1.4-7 7-1.4 3.5-2.1 1.1-1.4-1.4 1.1-2.1 3.5-1.4 7-7-1.4-1.4 1.4-1.4 1.4 1.4 1.4-1.4-1.4-1.4 2.1-2.1zM4 21.5a1.5 1.5 0 110-.1z',
    tube: 'M8 1h8v2h-1v15a3 3 0 01-6 0V3H8V1zm3 2v6h2V3h-2z',
    capsules: 'M3.5 7.5a4.2 4.2 0 016-6l5 5-6 6-5-5zM14.5 9.5l5 5a4.2 4.2 0 01-6 6l-5-5 6-6z'
  };
  var NAMES = Object.keys(ICONS);
  var NI = 16;
  for (var k = 0; k < NI; k++) {
    var w = document.createElement('span');
    w.className = 'dd-hero-tok ico t' + (k % 4);
    var nm = NAMES[k % NAMES.length];
    /* how each one turns: a third spin end-over-end (flat rotation), a third flip like a coin
       (3D turn about the vertical axis), a third rock back and forth; spin direction and speed vary */
    var mode = k % 3;
    var turn = mode === 1 ? ' flip' : mode === 2 ? ' rock' : '';
    w.innerHTML = '<svg class="dd-hero-ico' + turn + '" viewBox="0 0 24 24"><path d="' + ICONS[nm] + '"/></svg>';
    if (turn) w.firstChild.style.setProperty('--fd', rnd(mode === 1 ? 4 : 2.5, mode === 1 ? 11 : 6).toFixed(1) + 's');
    w.style.fontSize = rnd(18, 46).toFixed(0) + 'px';
    w.style.top = rnd(-6, 96).toFixed(1) + '%';
    var dir = k % 3 === 0 ? -1 : 1;            /* a third drift right-to-left */
    var yi = rnd(-14, 14), r0 = rnd(-25, 25);
    w.style.setProperty('--x0', (dir > 0 ? rnd(-14, 6) : rnd(90, 112)).toFixed(1) + 'vw');
    w.style.setProperty('--x1', (dir > 0 ? rnd(88, 114) : rnd(-16, 4)).toFixed(1) + 'vw');
    w.style.setProperty('--y0', yi.toFixed(1) + 'px');
    w.style.setProperty('--y1', (yi + rnd(-60, 60)).toFixed(1) + 'px');
    w.style.setProperty('--r0', r0.toFixed(0) + 'deg');
    var spin = mode === 0 ? (Math.random() < 0.5 ? -1 : 1) * rnd(360, 900) : rnd(-90, 90);
    w.style.setProperty('--r1', (r0 + spin).toFixed(0) + 'deg');
    w.style.setProperty('--op', rnd(0.08, 0.22).toFixed(2));
    var d = rnd(9, 58), dl = -rnd(0, d);         /* very different speeds: 9 s to almost a minute */
    w.style.animation = 'dd-hero-drift ' + d.toFixed(1) + 's ' + dl.toFixed(1) + 's linear infinite';
    frag.appendChild(w);
  }
  fx.appendChild(frag);
})();
