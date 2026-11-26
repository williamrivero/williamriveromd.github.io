/* Site navigation menu for phones (renalcarematters.com, Nov 26 2026, Dr. Rivero).
 *
 * Edit THIS file, then run `python3 patch_site_nav.py`: it writes the fingerprinted copy
 * assets/site-nav.<hash>.js and points every page at it. Never link this unhashed file.
 *
 * Pages load the script synchronously right after </nav> inside <header class="site-header">,
 * so it runs before the header is painted (no layout shift). On screens up to 640 px wide the
 * row of links is replaced by a Menu button in the top-left corner that opens a grouped
 * dropdown (Learn / Tools / Train). Wider screens keep the centered row. If the script fails
 * to load (an old saved page offline), the page keeps its scrolling row, so nothing breaks.
 */
(function () {
  "use strict";
  var scripts = document.getElementsByTagName("script");
  var me = document.currentScript || scripts[scripts.length - 1];
  var header = (me && me.closest && me.closest(".site-header")) || document.querySelector(".site-header");
  if (!header || header.getAttribute("data-rcm-nav")) return;
  var nav = header.querySelector(".header-nav");
  if (!nav) return;
  header.setAttribute("data-rcm-nav", "1");

  var PHONE = "(max-width: 640px)";
  // Icon tiles in category colors (Dr. Rivero chose this style, Nov 26 2026). Groups (Dr. Rivero): Orient · Learn ·
  // Consult (calculators, drugs) · Train, then About on its own. Colors: Learn teal, Consult orange, Train purple; Orient/About gold.
  var ITEMS = {
    home:        { label: "Home",        hint: "Renal Care Matters",       icon: '<path d="M3.5 10.5 12 3.5l8.5 7V20a1 1 0 0 1-1 1H15v-6H9v6H4.5a1 1 0 0 1-1-1z"/>' },
    guides:      { label: "Guides",      hint: "For patients and clinicians", icon: '<path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H19v15H6.5A1.5 1.5 0 0 0 5 19.5z"/><path d="M5 19.5A1.5 1.5 0 0 0 6.5 21H19v-3"/><path d="M9 7.5h6M9 11h6"/>' },
    physiology:  { label: "Physiology",  hint: "How the kidney works",      icon: '<path d="M9.2 3C5.5 3 3.2 6.8 3.2 11.6S5.6 21 9.2 21c2.3 0 3.4-1.5 3.4-3.3 0-2-1.6-3-1.6-5.4s1.6-3.3 1.6-5.4C12.6 4.6 11.3 3 9.2 3z"/><path d="M11.4 12.4h4.8a3 3 0 0 1 3 3V21"/>' },
    atlas:       { label: "Atlas",       hint: "Visual atlas",             icon: '<rect x="3" y="4.5" width="18" height="15" rx="2"/><circle cx="15.5" cy="9.5" r="1.6"/><path d="m3.5 17 5.2-5.2 4.3 4.3 2.5-2.5 5 5"/>' },
    calculators: { label: "Calculators", hint: "Clinical calculators",     icon: '<rect x="5" y="2.8" width="14" height="18.4" rx="2.2"/><path d="M8.5 6.8h7"/><path d="M8.6 11h.01M12 11h.01M15.4 11h.01M8.6 14.4h.01M12 14.4h.01M15.4 14.4h.01M8.6 17.8h.01M12 17.8h.01M15.4 17.8h.01" stroke-width="2.6"/>' },
    drugs:       { label: "Drugs",       hint: "Drug Index",               icon: '<path d="M10.4 3.9a5 5 0 0 1 7.1 7.1l-6.9 6.9a5 5 0 0 1-7.1-7.1z"/><path d="m7 7.3 6.9 6.9"/>' },
    academy:     { label: "Academy",     hint: "Training for every role in kidney care", icon: '<path d="m2.5 9 9.5-4.8L21.5 9 12 13.8z"/><path d="M6.5 11.2v4.6c0 1.5 2.5 3 5.5 3s5.5-1.5 5.5-3v-4.6"/><path d="M21.5 9v5.5"/>' },
    about:       { label: "About",       hint: "Clinics, schedules and appointments", icon: '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>' }
  };
  // wide = full-width row card; others pair up two per row
  var GROUPS = [
    { id: "base",  title: "Orient",  items: [["home", 1]] },
    { id: "learn", title: "Learn", items: [["guides", 1], ["physiology", 0], ["atlas", 0]] },
    { id: "tools", title: "Consult", items: [["calculators", 0], ["drugs", 0]] },
    { id: "train", title: "Train", items: [["academy", 1]] },
    { id: "base",  title: null,    items: [["about", 1]] }
  ];

  function keyOf(href) {
    var p;
    try { p = new URL(href, location.href).pathname; } catch (e) { return null; }
    p = p.replace(/\.html$/, "");
    if (/\/guides\/calc/.test(p)) return "calculators";
    if (/\/guides\/kidney-physiology$/.test(p)) return "physiology";
    if (/\/guides\/nephrology-atlas$/.test(p)) return "atlas";
    if (/^\/guides(\/|$)/.test(p)) return "guides";
    if (/^\/drugs(\/|$)/.test(p)) return "drugs";
    if (/^\/academy(\/|$)/.test(p)) return "academy";
    if (/^\/about$/.test(p)) return "about";
    if (p === "/" || p === "/index") return "home";
    return null;
  }

  // Links on this page, by key (keeps each page's own hrefs)
  var hrefs = {};
  var brand = header.querySelector(".brand");
  hrefs.home = brand ? brand.getAttribute("href") : "/";
  var currentKey = null;
  Array.prototype.forEach.call(nav.querySelectorAll("a[href]"), function (a) {
    var k = keyOf(a.getAttribute("href"));
    if (!k || k === "home" || hrefs[k]) return;
    hrefs[k] = a.getAttribute("href");
    if (a.classList.contains("is-current")) currentKey = k;
  });
  if (!currentKey) currentKey = keyOf(location.href);

  var F = "Inter,system-ui,-apple-system,'Segoe UI',sans-serif";
  var css = [
    ".rcm-nav-btn,.rcm-nav-cur,.rcm-nav-panel,.rcm-nav-scrim{display:none}",
    "@media " + PHONE + "{",
    ".site-header.rcm-nav{justify-content:flex-start!important;gap:10px!important;padding:0 8px 0 6px!important}",
    ".site-header.rcm-nav>.brand,.site-header.rcm-nav>.header-nav{display:none!important}",
    ".site-header.rcm-nav>.header-lang{margin-left:auto}",
    // Menu button: icon + small word, no box
    ".rcm-nav .rcm-nav-btn{display:inline-flex;align-items:center;gap:7px;height:44px;padding:0 10px;margin:0;border:0;border-radius:12px;",
    "background:transparent;color:#fff;font:600 13px/1 " + F + ";letter-spacing:.04em;cursor:pointer;flex-shrink:0;",
    "-webkit-tap-highlight-color:transparent;transition:background .15s}",
    ".rcm-nav .rcm-nav-btn:hover,.rcm-nav.rcm-open .rcm-nav-btn{background:rgba(255,255,255,.08)}",
    ".rcm-nav .rcm-nav-btn:focus-visible{outline:2px solid #e3c26a;outline-offset:1px}",
    ".rcm-nav .rcm-nav-btn svg{width:24px;height:24px;display:block}",
    ".rcm-nav .rcm-nav-btn .rcm-x{display:none}",
    ".rcm-nav.rcm-open .rcm-nav-btn,.rcm-nav.rcm-open>.header-lang{position:relative;z-index:3}",
    ".rcm-nav.rcm-open .rcm-nav-cur{z-index:3}",
    ".rcm-nav.rcm-open .rcm-nav-btn .rcm-bars{display:none}",
    ".rcm-nav.rcm-open .rcm-nav-btn .rcm-x{display:block}",
    // current section: small gold pill, centered
    ".rcm-nav .rcm-nav-cur{display:inline-flex;align-items:center;gap:6px;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);",
    "padding:5px 11px 5px 9px;border-radius:999px;border:1px solid rgba(227,194,106,.42);background:rgba(227,194,106,.1);",
    "color:#ecd08a;font:700 11.5px/1 " + F + ";letter-spacing:.12em;text-transform:uppercase;white-space:nowrap;pointer-events:none}",
    ".rcm-nav .rcm-nav-cur svg{width:14px;height:14px}",
    ".rcm-nav.rcm-has-lang .rcm-nav-cur{display:none}",
    // panel
    ".rcm-nav.rcm-open .rcm-nav-panel{display:block;position:absolute;top:100%;left:0;right:0;z-index:2;",
    "background:radial-gradient(120% 60% at 0% 0%,rgba(94,194,198,.16),transparent 60%),radial-gradient(90% 50% at 100% 100%,rgba(185,163,227,.13),transparent 60%),linear-gradient(170deg,#21406f 0%,#1b3561 50%,#162c52 100%);",
    "border-top:1px solid rgba(255,255,255,.08);border-radius:0 0 20px 20px;box-shadow:0 22px 44px rgba(3,10,25,.45);",
    "max-height:calc(100vh - 56px);max-height:calc(100dvh - 56px);overflow-y:auto;padding:12px 12px 16px;overscroll-behavior:contain;",
    "animation:rcmNavIn .2s cubic-bezier(.2,.8,.2,1)}",
    "@keyframes rcmNavIn{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}",
    ".rcm-nav.rcm-open .rcm-nav-scrim{display:block;position:fixed;inset:0;z-index:1;background:rgba(6,12,24,.5);",
    "-webkit-backdrop-filter:blur(2px);backdrop-filter:blur(2px);animation:rcmFade .2s ease}",
    "@keyframes rcmFade{from{opacity:0}to{opacity:1}}",
    ".rcm-nav-panel .rsn-g{--g:#ecd08a}",
    ".rcm-nav-panel .rsn-g[data-g=learn]{--g:#5ec2c6}",
    ".rcm-nav-panel .rsn-g[data-g=tools]{--g:#f2a36b}",
    ".rcm-nav-panel .rsn-g[data-g=train]{--g:#b9a3e3}",
    ".rcm-nav-panel .rsn-g+.rsn-g{margin-top:12px}",
    ".rcm-nav-panel .rsn-gt{display:flex;align-items:center;gap:10px;margin:2px 4px 8px;color:var(--g);",
    "font:800 11px/1 " + F + ";letter-spacing:.18em;text-transform:uppercase}",
    ".rcm-nav-panel .rsn-gt:after{content:'';flex:1;height:1px;background:linear-gradient(90deg,color-mix(in srgb,var(--g) 45%,transparent),transparent)}",
    ".rcm-nav-panel .rsn-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}",
    ".rcm-nav-panel a.rsn-card{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:9px;padding:12px;",
    "border-radius:14px;text-decoration:none;color:#fff;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.09);",
    "-webkit-tap-highlight-color:transparent;transition:background .15s,border-color .15s,transform .15s;",
    "animation:rcmCardIn .28s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 28ms)}",
    "@keyframes rcmCardIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}",
    ".rcm-nav-panel a.rsn-card.rsn-wide{grid-column:1/-1;flex-direction:row;align-items:center;gap:12px}",
    ".rcm-nav-panel a.rsn-card:hover{background:rgba(255,255,255,.09);border-color:color-mix(in srgb,var(--g) 40%,transparent)}",
    ".rcm-nav-panel a.rsn-card:active{transform:scale(.98)}",
    ".rcm-nav-panel a.rsn-card:focus-visible{outline:2px solid var(--g);outline-offset:2px}",
    ".rcm-nav-panel .rsn-ic{flex:0 0 auto;display:grid;place-items:center;width:38px;height:38px;border-radius:11px;color:var(--g);",
    "background:color-mix(in srgb,var(--g) 17%,transparent);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--g) 30%,transparent)}",
    ".rcm-nav-panel .rsn-ic svg{width:21px;height:21px}",
    ".rcm-nav-panel .rsn-tx{display:flex;flex-direction:column;gap:3px;min-width:0}",
    ".rcm-nav-panel .rsn-nl{font:700 15.5px/1.2 " + F + ";letter-spacing:.005em}",
    ".rcm-nav-panel .rsn-nh{font:500 12.5px/1.35 Manrope," + F + ";color:rgba(255,255,255,.74)}",
    ".rcm-nav-panel a.rsn-card[aria-current]{background:linear-gradient(135deg,rgba(227,194,106,.16),rgba(227,194,106,.05));border-color:rgba(227,194,106,.6)}",
    ".rcm-nav-panel a.rsn-card[aria-current] .rsn-nl{color:#ecd08a}",
    ".rcm-nav-panel a.rsn-card[aria-current]:after{content:'You are here';position:absolute;top:10px;right:10px;",
    "font:700 9.5px/1 " + F + ";letter-spacing:.1em;text-transform:uppercase;color:#ecd08a}",
    ".rcm-nav-panel a.rsn-card:not(.rsn-wide)[aria-current]:after{content:'';width:7px;height:7px;border-radius:50%;background:#ecd08a;top:12px;right:12px}",
    "}",
    "@media (prefers-reduced-motion:reduce){.rcm-nav-panel,.rcm-nav-panel a.rsn-card,.rcm-nav-scrim{animation:none!important;transition:none!important}}",
    "html[data-shade=epaper] .rcm-nav-panel,html[data-shade=epaper] .rcm-nav-panel a.rsn-card,html[data-shade=epaper] .rcm-nav-scrim{animation:none!important;backdrop-filter:none!important}",
    "@media print{.rcm-nav-btn,.rcm-nav-cur,.rcm-nav-panel,.rcm-nav-scrim{display:none!important}}"
  ].join("");
  if (!document.getElementById("rcm-site-nav-css")) {
    var st = document.createElement("style");
    st.id = "rcm-site-nav-css";
    st.textContent = css;
    (document.head || header).appendChild(st);
  }

  var SVG = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"';
  var btn = document.createElement("button");
  btn.type = "button";
  btn.className = "rcm-nav-btn";
  btn.setAttribute("aria-expanded", "false");
  btn.setAttribute("aria-controls", "rcm-nav-panel");
  btn.innerHTML = '<svg class="rcm-bars" ' + SVG + '><path d="M4 7h16M4 12h11M4 17h16"/></svg>' +
    '<svg class="rcm-x" ' + SVG + '><path d="M6 6l12 12M18 6L6 18"/></svg><span>Menu</span>';

  // a div, not <nav>: some pages style every nav element (e.g. the About page's legacy fixed bar)
  var panel = document.createElement("div");
  panel.className = "rcm-nav-panel";
  panel.id = "rcm-nav-panel";
  panel.setAttribute("role", "navigation");
  panel.setAttribute("aria-label", "Site menu");
  var n = 0;
  GROUPS.forEach(function (g) {
    var items = g.items.filter(function (it) { return it[0] === "home" || hrefs[it[0]]; });
    if (!items.length) return;
    var box = document.createElement("div");
    box.className = "rsn-g";
    box.setAttribute("data-g", g.id);
    if (g.title) {
      var t = document.createElement("div");
      t.className = "rsn-gt";
      t.textContent = g.title;
      box.appendChild(t);
    }
    var grid = document.createElement("div");
    grid.className = "rsn-grid";
    items.forEach(function (it) {
      var k = it[0], d = ITEMS[k];
      var a = document.createElement("a");
      a.className = "rsn-card" + (it[1] ? " rsn-wide" : "");
      a.href = hrefs[k] || "/";
      a.style.setProperty("--i", n++);
      if (k === currentKey) a.setAttribute("aria-current", "page");
      a.innerHTML = '<span class="rsn-ic"><svg ' + SVG + '>' + d.icon + '</svg></span>' +
        '<span class="rsn-tx"><span class="rsn-nl"></span><span class="rsn-nh"></span></span>';
      a.querySelector(".rsn-nl").textContent = d.label;
      a.querySelector(".rsn-nh").textContent = d.hint;
      grid.appendChild(a);
    });
    box.appendChild(grid);
    panel.appendChild(box);
  });

  var scrim = document.createElement("div");
  scrim.className = "rcm-nav-scrim";

  header.insertBefore(btn, header.firstChild);
  if (currentKey && ITEMS[currentKey] && currentKey !== "home") {
    var cur = document.createElement("span");
    cur.className = "rcm-nav-cur";
    cur.setAttribute("aria-hidden", "true");
    cur.innerHTML = '<svg ' + SVG + '>' + ITEMS[currentKey].icon + '</svg><span></span>';
    cur.lastChild.textContent = ITEMS[currentKey].label;
    header.appendChild(cur);
  }
  header.appendChild(scrim);
  header.appendChild(panel);
  if (header.querySelector(".header-lang")) header.classList.add("rcm-has-lang");
  header.classList.add("rcm-nav");
  if (getComputedStyle(header).position === "static") header.style.position = "relative";

  var savedZ = null;
  function setOpen(open, focusBtn) {
    if (open === header.classList.contains("rcm-open")) return;
    header.classList.toggle("rcm-open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.lastChild.textContent = open ? "Close" : "Menu";
    if (open) {
      savedZ = header.style.zIndex;
      header.style.zIndex = "10000";   // above the floating buttons (up to 9999)
      var first = panel.querySelector("a");
      if (first) first.focus({ preventScroll: true });
    } else {
      header.style.zIndex = savedZ || "";
      if (focusBtn) btn.focus({ preventScroll: true });
    }
  }
  btn.addEventListener("click", function () { setOpen(!header.classList.contains("rcm-open")); });
  scrim.addEventListener("click", function () { setOpen(false); });
  panel.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && header.classList.contains("rcm-open")) setOpen(false, true);
  });
  var mq = window.matchMedia ? window.matchMedia(PHONE) : null;
  if (mq) {
    var onChange = function () { if (!mq.matches) setOpen(false); };
    if (mq.addEventListener) mq.addEventListener("change", onChange); else if (mq.addListener) mq.addListener(onChange);
  }
  window.addEventListener("pageshow", function () { setOpen(false); });
})();
