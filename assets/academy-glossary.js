/* Tap-to-define glossary terms in Academy modules (Dr. Rivero, Nov 28 2026). Source file: edit this, then run
   python3 tools/academy/apply_glossary_terms.py (fingerprints it and tags every module page).
   Reads the page's own "Glossary & abbreviations" section, marks the first use of each term in every section of the
   module, and on a tap shows the definition with a link to the term in the glossary (the side rail drawer on wide
   screens, the accordion at the end of the page otherwise). Nothing is changed in the HTML file and nothing is sent. */
(function () {
  "use strict";
  if (window.__rcmGloss) return;
  window.__rcmGloss = true;

  var CSS = '' +
    '.rcm-gl{text-decoration:underline dotted;text-decoration-color:var(--teal,#1a6b72);text-decoration-thickness:1.5px;text-underline-offset:3px;cursor:help;border-radius:3px;}' +
    '.rcm-gl:hover,.rcm-gl:focus-visible,.rcm-gl[aria-expanded="true"]{background:color-mix(in srgb,var(--teal,#1a6b72) 14%,transparent);outline:none;}' +
    '.rcm-glp{position:absolute;z-index:100015;width:min(340px,calc(100vw - 24px));background:var(--white,#fff);color:var(--text,#1e2a38);' +
    'border:1px solid var(--border,#d6dde6);border-top:3px solid var(--teal,#1a6b72);border-radius:12px;box-shadow:0 12px 32px rgba(0,0,0,.22);' +
    'padding:12px 14px 10px;font:14px/1.5 Manrope,Inter,system-ui,sans-serif;text-align:left;}' +
    '.rcm-glp b{display:block;font:700 15px/1.3 Inter,system-ui,sans-serif;color:var(--navy,#1f3864);margin:0 22px 4px 0;}' +
    'html[data-theme="dark"] .rcm-glp b{color:var(--text,#e6ebf2);}' +
    '.rcm-glp p{margin:0;color:var(--text-mid,#3d4a5c);}' +
    '.rcm-glp-x{position:absolute;top:6px;right:6px;width:28px;height:28px;border:0;border-radius:8px;background:transparent;color:var(--text-muted,#5b6778);font-size:18px;line-height:1;cursor:pointer;}' +
    '.rcm-glp-f{display:flex;align-items:center;gap:10px;margin-top:9px;padding-top:8px;border-top:1px solid var(--border,#d6dde6);font-size:12.5px;}' +
    '.rcm-glp-f a{font-weight:700;color:var(--teal,#1a6b72);text-decoration:none;}' +
    '.rcm-glp-f a:hover{text-decoration:underline;}' +
    '.rcm-gl-flash{animation:rcmglf 2.2s ease-out 1;border-radius:4px;}' +
    '@keyframes rcmglf{0%,40%{background:#fde68a;color:#1e2a38;}100%{background:transparent;}}' +
    '@media (max-width:640px){.rcm-glp{position:fixed;left:8px!important;right:8px;bottom:8px;top:auto!important;width:auto;}}' +
    '@media print{.rcm-gl{text-decoration:none!important;background:none!important;}.rcm-glp{display:none!important;}}';

  var SKIP = "a,button,input,select,textarea,label,summary,code,pre,sup,svg,script,style,h1,h2,h3,h4,h5,h6,.section-tag," +
    ".nc-cite,.rcm-gl,#quiz,#sim,form,.nc-nextprev,.rcm-tts-ui,.rcm-sk-ui,.rcn-ui,.rcm-share,[aria-hidden='true'],.lang-hidden,.acad-tracks,.rcn-hl";

  function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  function readGlossary() {
    var sec = document.querySelector(".glossary-section .glossary-acc");
    if (!sec) return [];
    var out = [];
    sec.querySelectorAll("dl").forEach(function (dl) {
      dl.querySelectorAll("dt").forEach(function (dt, i) {
        var dd = dt.nextElementSibling;
        while (dd && dd.tagName !== "DD") dd = dd.nextElementSibling;
        if (!dd) return;
        var label = (dt.textContent || "").replace(/\s+/g, " ").trim();
        if (!label) return;
        if (!dt.id) dt.id = "gl-" + label.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60) + "-" + i;
        var forms = [];
        var m = /^(.*?)\s*\(([^)]+)\)\s*(.*)$/.exec(label);          // "Dry weight (target weight)", "Arteriovenous fistula (AVF)"
        if (m) { forms.push((m[1] + (m[3] ? " " + m[3] : "")).trim()); forms.push(m[2].trim()); }
        else forms = label.split(/\s*,\s*/);                            // "C3, C4"
        forms = forms.filter(function (f) { return f.length >= 2 && !/^(the|a|an|and|or)$/i.test(f); });
        if (forms.length) out.push({ label: label, forms: forms, def: dd.innerHTML, dt: dt });
      });
    });
    return out;
  }

  function isAbbr(f) { return !/\s/.test(f) && /[A-Z]/.test(f) && f.length <= 12 && f.replace(/[^A-Z]/g, "").length >= Math.min(2, f.length); }

  function mark(terms) {
    var abbr = {}, words = {}, A = [], W = [];
    terms.forEach(function (t) {
      t.forms.forEach(function (f) {
        if (isAbbr(f)) { if (!abbr[f]) { abbr[f] = t; A.push(f); } }
        else { var k = f.toLowerCase(); if (!words[k]) { words[k] = t; W.push(f); } }
      });
    });
    if (!A.length && !W.length) return 0;
    var byLen = function (a, b) { return b.length - a.length; };
    A.sort(byLen); W.sort(byLen);
    var reA = A.length ? new RegExp("(" + A.map(esc).join("|") + ")", "g") : null;
    var reW = W.length ? new RegExp("(" + W.map(function (w) { return esc(w).replace(/-/g, "[-‐‑]"); }).join("|") + ")((?:e?s)?)", "gi") : null;
    var WORD = /[A-Za-z0-9À-ɏ]/;
    function edges(text, i, len) { return !(i > 0 && WORD.test(text.charAt(i - 1))) && !WORD.test(text.charAt(i + len) || ""); }
    var count = 0;
    document.querySelectorAll("main section.section").forEach(function (sec) {
      if (sec.id === "quiz" || sec.id === "sim" || sec.id === "reading") return;
      var seen = {}, nodes = [];
      var walker = document.createTreeWalker(sec, NodeFilter.SHOW_TEXT, {
        acceptNode: function (n) {
          if (!n.nodeValue || n.nodeValue.trim().length < 2) return NodeFilter.FILTER_REJECT;
          var p = n.parentElement;
          return p && !p.closest(SKIP) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
        }
      });
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach(function (node) {
        var text = node.nodeValue, hits = [], m;
        if (reA) { reA.lastIndex = 0; while ((m = reA.exec(text))) if (edges(text, m.index, m[0].length)) hits.push({ i: m.index, len: m[0].length, t: abbr[m[1]] }); }
        if (reW) { reW.lastIndex = 0; while ((m = reW.exec(text))) if (edges(text, m.index, m[0].length)) hits.push({ i: m.index, len: m[0].length, t: words[m[1].toLowerCase().replace(/[‐‑]/g, "-")] }); }
        hits.sort(function (a, b) { return a.i - b.i || b.len - a.len; });
        var keep = [], end = -1;
        hits.forEach(function (h) {
          if (!h.t || h.i < end || seen[h.t.label]) return;
          seen[h.t.label] = 1; keep.push(h); end = h.i + h.len;
        });
        for (var k = keep.length - 1; k >= 0; k--) {                    // wrap from the end so earlier offsets stay valid
          var h = keep[k];
          var mid = node.splitText(h.i);
          mid.splitText(h.len);
          var span = document.createElement("span");
          span.className = "rcm-gl";
          span.setAttribute("role", "button");
          span.setAttribute("tabindex", "0");
          span.setAttribute("aria-haspopup", "dialog");
          span.setAttribute("aria-expanded", "false");
          span.dataset.gl = h.t.dt.id;
          mid.parentNode.insertBefore(span, mid);
          span.appendChild(mid);
          count++;
        }
      });
    });
    return count;
  }

  var pop = null, owner = null, byId = {};
  function closePop() {
    if (pop) { pop.remove(); pop = null; }
    if (owner) { owner.setAttribute("aria-expanded", "false"); owner = null; }
  }
  function openPop(span) {
    var t = byId[span.dataset.gl];
    if (!t) return;
    if (owner === span) { closePop(); return; }
    closePop();
    owner = span;
    span.setAttribute("aria-expanded", "true");
    pop = document.createElement("div");
    pop.className = "rcm-glp rcn-ui";
    pop.setAttribute("role", "dialog");
    pop.setAttribute("aria-label", "Definition: " + t.label);
    pop.innerHTML = '<button type="button" class="rcm-glp-x" aria-label="Close">×</button><b></b><p></p>' +
      '<div class="rcm-glp-f"><a href="#' + t.dt.id + '">See in glossary →</a></div>';
    pop.querySelector("b").textContent = t.label;
    pop.querySelector("p").innerHTML = t.def;
    pop.querySelectorAll("p [style]").forEach(function (e) { e.removeAttribute("style"); });
    document.body.appendChild(pop);
    var r = span.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight;
    var left = Math.max(12, Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - w - 12));
    var top = r.bottom + 8 + h > window.innerHeight && r.top - h - 8 > 60 ? window.scrollY + r.top - h - 8 : window.scrollY + r.bottom + 8;
    pop.style.left = left + "px";
    pop.style.top = top + "px";
    pop.querySelector(".rcm-glp-x").addEventListener("click", function () { var o = owner; closePop(); if (o) o.focus(); });
    pop.querySelector("a").addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); closePop(); goGlossary(t); });
    pop.querySelector(".rcm-glp-x").focus({ preventScroll: true });
  }

  function flash(el) {
    if (!el) return;
    el.classList.remove("rcm-gl-flash"); void el.offsetWidth; el.classList.add("rcm-gl-flash");
    setTimeout(function () { el.classList.remove("rcm-gl-flash"); }, 2400);
  }
  function goGlossary(t) {
    var railBtn = document.querySelector('.rcm-rail-btn[data-tab="gloss"]');
    if (document.documentElement.classList.contains("rcm-rail-on") && railBtn) {   // wide screens: the side rail drawer
      var drawer = document.querySelector(".rcm-drawer");
      if (!(drawer && drawer.classList.contains("is-open"))) railBtn.click();
      else { var tab = document.querySelector('.rcm-tab[data-tab="gloss"]'); if (tab) tab.click(); }
      setTimeout(function () {
        var hit = null;
        document.querySelectorAll("#rcm-pane-gloss dt").forEach(function (d) { if (!hit && d.textContent.replace(/\s+/g, " ").trim() === t.label) hit = d; });
        if (hit) { hit.scrollIntoView({ block: "center", behavior: "smooth" }); flash(hit); }
      }, 120);
      return;
    }
    var acc = t.dt.closest("details");                                  // otherwise: the accordion at the end of the page
    if (acc) acc.open = true;
    t.dt.scrollIntoView({ block: "center", behavior: "smooth" });
    flash(t.dt);
  }

  function init() {
    var terms = readGlossary();
    if (!terms.length) return;
    terms.forEach(function (t) { byId[t.dt.id] = t; });
    var st = document.createElement("style");
    st.id = "rcm-gl-css";
    st.textContent = CSS;
    document.head.appendChild(st);
    mark(terms);
    document.addEventListener("click", function (e) {
      var span = e.target.closest && e.target.closest(".rcm-gl");
      if (span) {
        var sel = window.getSelection && window.getSelection();
        if (sel && !sel.isCollapsed && String(sel).length > 1) return;       // selecting text for a highlight or note
        e.preventDefault();
        openPop(span);
        return;
      }
      if (pop && !pop.contains(e.target)) closePop();
    });
    document.addEventListener("keydown", function (e) {
      var span = e.target.closest && e.target.closest(".rcm-gl");
      if (span && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); openPop(span); return; }
      if (e.key === "Escape" && pop) { var o = owner; closePop(); if (o) o.focus(); }
    });
    window.addEventListener("resize", closePop);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else setTimeout(init, 0);
})();
