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
  // Order (Dr. Rivero, Nov 27 2026): Train · Learn · Assess (calculators, drugs; was "Consult", then "Look up") · Connect (About, Review = rate the site). Colors: Learn teal, Assess orange, Train purple; Orient/About gold.
  var ITEMS = {
    home:        { label: "Home",        hint: "Renal Care Matters",       icon: '<path d="M3.5 10.5 12 3.5l8.5 7V20a1 1 0 0 1-1 1H15v-6H9v6H4.5a1 1 0 0 1-1-1z"/>' },
    guides:      { label: "Guides",      hint: "For patients and clinicians", icon: '<path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H19v15H6.5A1.5 1.5 0 0 0 5 19.5z"/><path d="M5 19.5A1.5 1.5 0 0 0 6.5 21H19v-3"/><path d="M9 7.5h6M9 11h6"/>' },
    physiology:  { label: "Physiology",  hint: "How the kidney works",      icon: '<path d="M9.2 3C5.5 3 3.2 6.8 3.2 11.6S5.6 21 9.2 21c2.3 0 3.4-1.5 3.4-3.3 0-2-1.6-3-1.6-5.4s1.6-3.3 1.6-5.4C12.6 4.6 11.3 3 9.2 3z"/><path d="M11.4 12.4h4.8a3 3 0 0 1 3 3V21"/>' },
    atlas:       { label: "Atlas",       hint: "Visual atlas",             icon: '<rect x="3" y="4.5" width="18" height="15" rx="2"/><circle cx="15.5" cy="9.5" r="1.6"/><path d="m3.5 17 5.2-5.2 4.3 4.3 2.5-2.5 5 5"/>' },
    calculators: { label: "Calculators", hint: "Clinical calculators",     icon: '<rect x="5" y="2.8" width="14" height="18.4" rx="2.2"/><path d="M8.5 6.8h7"/><path d="M8.6 11h.01M12 11h.01M15.4 11h.01M8.6 14.4h.01M12 14.4h.01M15.4 14.4h.01M8.6 17.8h.01M12 17.8h.01M15.4 17.8h.01" stroke-width="2.6"/>' },
    drugs:       { label: "Drugs",       hint: "Drug Index",               icon: '<path d="M10.4 3.9a5 5 0 0 1 7.1 7.1l-6.9 6.9a5 5 0 0 1-7.1-7.1z"/><path d="m7 7.3 6.9 6.9"/>' },
    academy:     { label: "Academy",     hint: "Training for every role in kidney care", icon: '<path d="m2.5 9 9.5-4.8L21.5 9 12 13.8z"/><path d="M6.5 11.2v4.6c0 1.5 2.5 3 5.5 3s5.5-1.5 5.5-3v-4.6"/><path d="M21.5 9v5.5"/>' },
    about:       { label: "About",       hint: "Clinics, schedules and appointments", icon: '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>' },
    review:      { label: "Review",      hint: "Rate the site",           icon: '<path d="M12 3.2l2.6 5.5 6 .7-4.5 4.1 1.2 6L12 16.6l-5.3 2.9 1.2-6-4.5-4.1 6-.7z"/>' }
  };
  // wide = full-width row card; others pair up two per row
  var GROUPS = [
    { id: "base",  title: "Orient",  items: [["home", 1]] },
    { id: "train", title: "Train", items: [["academy", 1]] },
    { id: "learn", title: "Learn", items: [["guides", 1], ["physiology", 0], ["atlas", 0]] },
    { id: "tools", title: "Assess", items: [["calculators", 0], ["drugs", 0]] },
    { id: "connect", title: "Connect", items: [["about", 0], ["review", 0]] }
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
    if (/^\/review(-admin)?$/.test(p)) return "review";
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
  if (!hrefs.review) hrefs.review = "/review.html";   // not in the desktop row; menu only
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
    ".rcm-nav .rcm-beacon{--bc:236,208,138;position:relative;display:block;width:24px;height:24px;flex:0 0 24px}",
    ".rcm-nav.rcm-open .rcm-beacon{--bc:255,106,61}",
    ".rcm-nav .rcm-beacon b{position:absolute;left:50%;top:50%;width:9px;height:9px;margin:-4.5px 0 0 -4.5px;border-radius:50%;",
    "background:rgb(var(--bc));box-shadow:0 0 0 2px rgba(var(--bc),.18),0 0 10px rgba(var(--bc),.55);transition:background .2s,box-shadow .2s}",
    ".rcm-nav .rcm-beacon i{position:absolute;left:50%;top:50%;width:9px;height:9px;margin:-4.5px 0 0 -4.5px;border-radius:50%;",
    "border:1.5px solid rgba(var(--bc),.75);opacity:0;animation:rcmBeacon 2.8s cubic-bezier(.15,.55,.35,1) infinite}",
    ".rcm-nav .rcm-beacon i+i{animation-delay:1.4s}",
    "@keyframes rcmBeacon{0%{transform:scale(1);opacity:.8}75%{opacity:.08}100%{transform:scale(2.7);opacity:0}}",
    ".rcm-nav.rcm-open .rcm-nav-btn,.rcm-nav.rcm-open>.header-lang{position:relative;z-index:3}",
    ".rcm-nav.rcm-open .rcm-nav-cur{z-index:3}",
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
    "}",
    ".rsn-host .rsn-g{--g:#ecd08a}",
    ".rsn-host .rsn-g[data-g=learn]{--g:#5ec2c6}",
    ".rsn-host .rsn-g[data-g=tools]{--g:#f2a36b}",
    ".rsn-host .rsn-g[data-g=train]{--g:#b9a3e3}",
    ".rsn-host .rsn-g[data-g=connect]{--g:#ecd08a}",
    ".rsn-host .rsn-g+.rsn-g{margin-top:12px}",
    ".rsn-host .rsn-gt{display:flex;align-items:center;gap:10px;margin:2px 4px 8px;color:var(--g);",
    "font:800 11px/1 " + F + ";letter-spacing:.18em;text-transform:uppercase}",
    ".rsn-host .rsn-gt:after{content:'';flex:1;height:1px;background:linear-gradient(90deg,color-mix(in srgb,var(--g) 45%,transparent),transparent)}",
    ".rsn-host .rsn-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}",
    ".rsn-host a.rsn-card{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:9px;padding:12px;",
    "border-radius:14px;text-decoration:none;color:#fff;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.09);",
    "-webkit-tap-highlight-color:transparent;transition:background .15s,border-color .15s,transform .15s;",
    "animation:rcmCardIn .28s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i) * 28ms)}",
    "@keyframes rcmCardIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}",
    ".rsn-host a.rsn-card.rsn-wide{grid-column:1/-1;flex-direction:row;align-items:center;gap:12px}",
    ".rsn-host a.rsn-card:hover{background:rgba(255,255,255,.09);border-color:color-mix(in srgb,var(--g) 40%,transparent)}",
    ".rsn-host a.rsn-card:active{transform:scale(.98)}",
    ".rsn-host a.rsn-card:focus-visible{outline:2px solid var(--g);outline-offset:2px}",
    ".rsn-host .rsn-ic{flex:0 0 auto;display:grid;place-items:center;width:38px;height:38px;border-radius:11px;color:var(--g);",
    "background:color-mix(in srgb,var(--g) 17%,transparent);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--g) 30%,transparent)}",
    ".rsn-host .rsn-ic svg{width:21px;height:21px}",
    ".rsn-host .rsn-tx{display:flex;flex-direction:column;gap:3px;min-width:0}",
    ".rsn-host .rsn-nl{font:700 15.5px/1.2 " + F + ";letter-spacing:.005em}",
    ".rsn-host .rsn-nh{font:500 12.5px/1.35 Manrope," + F + ";color:rgba(255,255,255,.74)}",
    ".rsn-host a.rsn-card[aria-current]{background:linear-gradient(135deg,rgba(227,194,106,.16),rgba(227,194,106,.05));border-color:rgba(227,194,106,.6)}",
    ".rsn-host a.rsn-card[aria-current] .rsn-nl{color:#ecd08a}",
    ".rsn-host a.rsn-card[aria-current]:after{content:'You are here';position:absolute;top:10px;right:10px;",
    "font:700 9.5px/1 " + F + ";letter-spacing:.1em;text-transform:uppercase;color:#ecd08a}",
    ".rsn-host a.rsn-card:not(.rsn-wide)[aria-current]:after{content:'';width:7px;height:7px;border-radius:50%;background:#ecd08a;top:12px;right:12px}",
    ".rsn-host .rsn-tracks{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:8px}",
    ".rsn-host a.rsn-trk{display:flex;align-items:center;gap:8px;padding:9px 10px;border-radius:11px;text-decoration:none;color:#fff;",
    "font:600 13px/1.25 " + F + ";background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);transition:background .15s}",
    ".rsn-host a.rsn-trk:hover{background:rgba(255,255,255,.09)}",
    ".rsn-host a.rsn-trk:focus-visible{outline:2px solid var(--g);outline-offset:2px}",
    ".rsn-host a.rsn-trk i{flex:0 0 8px;width:8px;height:8px;border-radius:50%;background:var(--t)}",
    // Desktop / tablet (wider than 640 px): category bar with dropdowns (Dr. Rivero, Nov 26 2026)
    ".rcm-dnav{display:none}",
    "@keyframes rcmDpIn{from{opacity:0;margin-top:-6px}to{opacity:1;margin-top:0}}",
    "@media (min-width: 641px){",
    ".site-header .header-nav.rcm-d{overflow:visible!important;gap:4px!important}",
    ".site-header .header-nav.rcm-d>a{display:none!important}",
    ".rcm-dnav{display:flex;align-items:center;gap:4px}",
    ".rcm-dg{position:relative}",
    ".rcm-dt{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 11px;margin:0;border:0;border-radius:10px;background:transparent;",
    "color:rgba(255,255,255,.78);font:600 .78rem/1 " + F + ";letter-spacing:.08em;text-transform:uppercase;cursor:pointer;white-space:nowrap;transition:color .15s,background .15s}",
    ".rcm-dt svg{width:14px;height:14px;transition:transform .2s;opacity:.8}",
    ".rcm-dt:hover,.rcm-dg.open .rcm-dt{color:#fff;background:rgba(255,255,255,.09)}",
    ".rcm-dg.open .rcm-dt svg{transform:rotate(180deg)}",
    ".rcm-dg.cur .rcm-dt{color:#e3c26a}",
    ".rcm-dt:focus-visible{outline:2px solid #e3c26a;outline-offset:1px}",
    ".rcm-dp{display:none;position:absolute;top:calc(100% + 9px);left:50%;transform:translateX(calc(-50% + var(--dx,0px)));width:min(400px,calc(100vw - 24px));",
    "padding:12px;border-radius:18px;border:1px solid rgba(255,255,255,.1);z-index:20;text-align:left;",
    "background:radial-gradient(120% 70% at 0% 0%,rgba(94,194,198,.16),transparent 60%),radial-gradient(90% 60% at 100% 100%,rgba(185,163,227,.13),transparent 60%),linear-gradient(170deg,#21406f 0%,#1b3561 50%,#162c52 100%);",
    "box-shadow:0 24px 50px rgba(3,10,25,.45)}",
    ".rcm-dp:before{content:'';position:absolute;left:0;right:0;top:-12px;height:12px}",
    ".rcm-dg.open .rcm-dp{display:block;animation:rcmDpIn .18s cubic-bezier(.2,.8,.2,1)}",
    ".rcm-dp .rsn-gt{margin-top:2px}",
    // the dropdowns live inside .header-nav, whose link styles (uppercase, nowrap, small type) must not leak in
    ".site-header .header-nav .rcm-dp a{text-transform:none!important;letter-spacing:normal!important;white-space:normal!important;font-size:14px;line-height:1.3;opacity:1}",
    ".site-header .header-nav .rcm-dp a.rsn-trk{font:600 13px/1.25 " + F + "!important;color:#fff!important}",
    ".site-header .header-nav .rcm-dp a.rsn-card{color:#fff!important}",
    ".site-header .header-nav .rcm-dp a.rsn-card[aria-current] .rsn-nl{color:#ecd08a}",
    "}",
    "@media (prefers-reduced-motion:reduce){.rcm-nav-panel,.rsn-host a.rsn-card,.rcm-nav-scrim,.rcm-dg.open .rcm-dp{animation:none!important;transition:none!important}",
    ".rcm-nav .rcm-beacon i{animation:none!important;opacity:.45;transform:scale(2)}.rcm-nav .rcm-beacon i+i{display:none}}",
    "html[data-shade=epaper] .rcm-nav .rcm-beacon i{animation:none!important;opacity:.45;transform:scale(2)}html[data-shade=epaper] .rcm-nav .rcm-beacon i+i{display:none}",
    "html[data-shade=epaper] .rcm-nav-panel,html[data-shade=epaper] .rsn-host a.rsn-card,html[data-shade=epaper] .rcm-nav-scrim,html[data-shade=epaper] .rcm-dp{animation:none!important;backdrop-filter:none!important}",
    "@media print{.rcm-nav-btn,.rcm-nav-cur,.rcm-nav-panel,.rcm-nav-scrim,.rcm-dnav{display:none!important}}"
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
  // Beacon (Dr. Rivero, Nov 26 2026): a gold dot with two slow rings pulsing out, in place of the bars;
  // while the menu is open it stays, recolored red-orange, beside the word Close (no X)
  btn.innerHTML = '<span class="rcm-bars rcm-beacon" aria-hidden="true"><i></i><i></i><b></b></span>' +
    '<span>Menu</span>';

  // a div, not <nav>: some pages style every nav element (e.g. the About page's legacy fixed bar)
  var panel = document.createElement("div");
  panel.className = "rcm-nav-panel";
  panel.id = "rcm-nav-panel";
  panel.setAttribute("role", "navigation");
  panel.setAttribute("aria-label", "Site menu");
  // Academy tracks (anchors on the Academy landing page), listed under Train in both menus
  var TRACKS = [["track-nursing", "Nephrology Nursing", "#5ec2c6"], ["track-physicians", "Renal Care Physicians", "#8fb0e8"],
    ["renal-technician-program", "Renal Technicians", "#f2a36b"], ["track-ancillary", "Ancillary Staff", "#7fd39a"],
    ["track-administrative", "Administrative Staff", "#b9a3e3"],
    ["/academy/emergency-readiness", "Emergency Readiness", "#f0938a"]];   // Dr. Rivero, Nov 28 2026: sixth pill
  var n = 0;
  function buildGroup(g, withTitle) {
    var items = g.items.filter(function (it) { return it[0] === "home" || hrefs[it[0]]; });
    if (!items.length) return null;
    var box = document.createElement("div");
    box.className = "rsn-g";
    box.setAttribute("data-g", g.id);
    if (g.title && withTitle) {
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
    if (g.id === "train") {
      var tl = document.createElement("div");
      tl.className = "rsn-tracks";
      TRACKS.forEach(function (tr) {
        var a = document.createElement("a");
        a.className = "rsn-trk";
        a.href = tr[0].charAt(0) === "/" ? tr[0] : "/academy/#" + tr[0];
        a.style.setProperty("--t", tr[2]);
        a.innerHTML = "<i></i><span></span>";
        a.lastChild.textContent = tr[1];
        tl.appendChild(a);
      });
      box.appendChild(tl);
    }
    return box;
  }
  panel.classList.add("rsn-host");
  GROUPS.forEach(function (g) { var box = buildGroup(g, true); if (box) panel.appendChild(box); });

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

  /* ---------- desktop / tablet: category bar with dropdowns ---------- */
  var CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6"/></svg>';
  var dnav = document.createElement("div");
  dnav.className = "rcm-dnav";
  var dgroups = [], closeTimer = null, hoverOpenedAt = 0, hoverable = !!(window.matchMedia && window.matchMedia("(hover: hover)").matches);
  GROUPS.forEach(function (g, gi) {
    if (g.title === "Orient") return;                 // the HOME brand link covers Orient on wide screens
    n = 0;                                             // card entrance stagger restarts in each dropdown
    var body = buildGroup(g, false);
    if (!body) return;
    var wrap = document.createElement("div");
    wrap.className = "rcm-dg";
    var keys = g.items.map(function (it) { return it[0]; });
    if (currentKey && keys.indexOf(currentKey) >= 0) wrap.classList.add("cur");
    var t = document.createElement("button");
    t.type = "button";
    t.className = "rcm-dt";
    t.setAttribute("aria-expanded", "false");
    t.setAttribute("aria-controls", "rcm-dp-" + gi);
    t.innerHTML = "<span></span>" + CHEV;
    t.firstChild.textContent = g.title;
    var dp = document.createElement("div");
    dp.className = "rcm-dp rsn-host";
    dp.id = "rcm-dp-" + gi;
    dp.setAttribute("role", "navigation");
    dp.setAttribute("aria-label", g.title);
    dp.appendChild(body);
    wrap.appendChild(t);
    wrap.appendChild(dp);
    dnav.appendChild(wrap);
    dgroups.push(wrap);
    t.addEventListener("click", function () {
      // a click right after the hover opened it keeps it open (otherwise hover + click would toggle it shut)
      if (wrap.classList.contains("open") && Date.now() - hoverOpenedAt < 600) return;
      openD(wrap.classList.contains("open") ? null : wrap);
    });
    if (hoverable) {
      wrap.addEventListener("mouseenter", function () {
        clearTimeout(closeTimer);
        if (!wrap.classList.contains("open")) { hoverOpenedAt = Date.now(); openD(wrap); }
      });
      wrap.addEventListener("mouseleave", function () { clearTimeout(closeTimer); closeTimer = setTimeout(function () { openD(null); }, 220); });
    }
    wrap.addEventListener("focusout", function (e) { if (!wrap.contains(e.relatedTarget)) { if (wrap.classList.contains("open")) openD(null); } });
  });
  var dZ = null;
  function openD(w) {
    dgroups.forEach(function (x) {
      var on = x === w;
      x.classList.toggle("open", on);
      x.querySelector(".rcm-dt").setAttribute("aria-expanded", on ? "true" : "false");
    });
    if (w) {
      if (dZ === null) { dZ = header.style.zIndex; header.style.zIndex = "100010"; }
      var dp = w.querySelector(".rcm-dp");
      dp.style.setProperty("--dx", "0px");
      var r = dp.getBoundingClientRect(), vw = document.documentElement.clientWidth, dx = 0;
      if (r.right > vw - 12) dx = vw - 12 - r.right;
      if (r.left + dx < 12) dx = 12 - r.left;
      dp.style.setProperty("--dx", Math.round(dx) + "px");
    } else if (dZ !== null) { header.style.zIndex = dZ || ""; dZ = null; }
  }
  if (dgroups.length) {
    nav.appendChild(dnav);
    nav.classList.add("rcm-d");
    document.addEventListener("click", function (e) { if (!dnav.contains(e.target)) openD(null); });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      var open = dnav.querySelector(".rcm-dg.open");
      if (open) { openD(null); open.querySelector(".rcm-dt").focus({ preventScroll: true }); }
    });
  }

  var savedZ = null;
  function setOpen(open, focusBtn) {
    if (open === header.classList.contains("rcm-open")) return;
    header.classList.toggle("rcm-open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.lastChild.textContent = open ? "Close" : "Menu";
    if (open) {
      savedZ = header.style.zIndex;
      header.style.zIndex = "100010";   // above floating buttons, the side rail and Academy notes tips (up to 100003)
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
    var onChange = function () { if (!mq.matches) setOpen(false); else openD(null); };
    if (mq.addEventListener) mq.addEventListener("change", onChange); else if (mq.addListener) mq.addListener(onChange);
  }
  window.addEventListener("pageshow", function () { setOpen(false); });
})();
