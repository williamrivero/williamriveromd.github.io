/* Animated hero for the drug database index pages (drugs/, drugs/category/, drugs/supplements/).
   Same family as the guides and calculators index heroes: a slow gradient drift plus faint
   drifting pharmacology tokens (generic names, PK terms, dosing shorthand) and capsule glyphs.
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
    '@keyframes dd-hero-float{0%{transform:translate(var(--x0),var(--y0)) rotate(var(--rot));opacity:0}',
    ' 12%{opacity:var(--op)}88%{opacity:var(--op)}100%{transform:translate(var(--x1),var(--y1)) rotate(var(--rot));opacity:0}}',
    '@media (prefers-reduced-motion:reduce){body.dd-index-page section.hero{animation:none}.dd-hero-tok{animation:none!important;opacity:.14}}',
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
  fx.appendChild(frag);
})();
