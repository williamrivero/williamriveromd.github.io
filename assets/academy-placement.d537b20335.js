/* Renal Care Academy placement pre-test (Dr. William Gregory Rivero, Nov 27 2026).
   Edit this file, then run python3 tools/academy/apply_placement.py (it fingerprints and tags it).
   Three modes: the pre-test page (#rcm-pt-data), a track hub (#rcm-pt-hub), a module page (script data-track/data-mod).
   Results: localStorage "rcm-placement" {track:{mods:{NN:{s,t,at,q:[i..],a:[i..]}}}}. Nothing leaves the device. */
(function () {
  "use strict";
  var KEY = "rcm-placement";
  var me = document.currentScript;

  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } }
  function save(all) { try { localStorage.setItem(KEY, JSON.stringify(all)); return true; } catch (e) { return false; } }
  function trackRec(all, t) { all[t] = all[t] || {}; all[t].mods = all[t].mods || {}; return all[t]; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function json(id) { var el = document.getElementById(id); if (!el) return null; try { return JSON.parse(el.textContent); } catch (e) { return null; } }
  function fmtDate(ms) { try { return new Date(ms).toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" }); } catch (e) { return ""; } }
  function fmtWhen(ms) { try { return new Date(ms).toLocaleString("en-US", { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" }); } catch (e) { return ""; } }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function modNum(nn) { return String(parseInt(nn, 10)); }

  /* status of one module: req | out | study | none */
  function status(always, r, mastery) {
    if (always) return "req";
    if (!r || !r.t) return "none";
    return r.s / r.t >= mastery - 1e-9 ? "out" : "study";
  }

  var CSS = [
    ".rcm-pt-card{border:1px solid var(--border);border-radius:14px;background:var(--white);padding:18px 20px;margin:14px 0;}",
    ".rcm-pt-card h3{font-family:Inter,system-ui,sans-serif;font-size:18px;margin:0 0 8px;color:var(--text);}",
    ".rcm-pt-muted{color:var(--text-mid);font-size:14.5px;line-height:1.55;}",
    ".rcm-pt-note{font-size:13.5px;color:var(--text-muted);}",
    ".rcm-pt-chip{display:inline-block;font:700 11.5px/1 Inter,system-ui,sans-serif;letter-spacing:.03em;text-transform:uppercase;border-radius:999px;padding:5px 9px;white-space:nowrap;}",
    ".rcm-pt-chip.out{background:var(--green-soft);color:var(--green);}",
    ".rcm-pt-chip.study{background:var(--amber-soft);color:var(--amber);}",
    ".rcm-pt-chip.req{background:var(--purple-soft);color:var(--purple);}",
    ".rcm-pt-chip.none{background:var(--bg);color:var(--text-muted);border:1px solid var(--border);}",
    ".rcm-pt-list{list-style:none;margin:10px 0 0;padding:0;}",
    ".rcm-pt-list li{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-top:1px solid var(--border);}",
    ".rcm-pt-list li:first-child{border-top:0;}",
    ".rcm-pt-list .rcm-pt-num{flex:0 0 34px;font:800 15px/1.4 Inter,system-ui,sans-serif;color:var(--teal);}",
    ".rcm-pt-list .rcm-pt-body{flex:1;min-width:0;}",
    ".rcm-pt-list .rcm-pt-body a,.rcm-pt-banner a{font-weight:600;color:var(--teal);text-decoration:underline;text-underline-offset:2px;}",
    ".rcm-pt-list .rcm-pt-why{display:block;font-size:13px;color:var(--text-muted);margin-top:2px;}",
    ".rcm-pt-pick{display:flex;gap:10px;align-items:flex-start;padding:7px 0;cursor:pointer;}",
    ".rcm-pt-pick input{margin-top:4px;width:18px;height:18px;flex:0 0 18px;}",
    ".rcm-pt-row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:14px;}",
    ".rcm-pt-bar{height:8px;border-radius:99px;background:var(--bg);border:1px solid var(--border);overflow:hidden;margin:6px 0 14px;}",
    ".rcm-pt-bar span{display:block;height:100%;background:var(--teal);}",
    ".rcm-pt-q{border:1px solid var(--border);border-radius:12px;padding:14px 16px;margin:12px 0;background:var(--white);}",
    ".rcm-pt-q legend{font-weight:600;line-height:1.5;padding:0 4px;color:var(--text);}",
    ".rcm-pt-q label{display:flex;gap:10px;align-items:flex-start;padding:7px 4px;border-radius:8px;cursor:pointer;line-height:1.5;}",
    ".rcm-pt-q label:hover{background:var(--bg);}",
    ".rcm-pt-q input{margin-top:5px;flex:0 0 auto;}",
    ".rcm-pt-rv .ok{color:var(--green);font-weight:700;}",
    ".rcm-pt-rv .bad{color:var(--red);font-weight:700;}",
    ".rcm-pt-rv .rat{font-size:13.5px;color:var(--text-mid);margin:2px 0 6px 0;}",
    ".rcm-pt-rv details{margin:8px 0 0;}",
    ".rcm-pt-rv summary{cursor:pointer;font-size:14px;color:var(--teal);font-weight:600;}",
    ".rcm-pt-sum{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:12px 0;}",
    ".rcm-pt-sum div{border:1px solid var(--border);border-radius:12px;padding:10px 12px;background:var(--bg);}",
    ".rcm-pt-sum b{display:block;font:800 24px/1.1 Inter,system-ui,sans-serif;color:var(--teal);}",
    ".rcm-pt-sum span{font-size:13px;color:var(--text-mid);}",
    ".rcm-pt-badge{margin-left:8px;}",
    ".rcm-pt-banner{border:1px solid var(--border);border-left:5px solid var(--green);border-radius:10px;background:var(--white);padding:12px 16px;margin:14px 0;font-size:15px;line-height:1.55;}",
    ".rcm-pt-banner.study{border-left-color:var(--amber);}",
    ".rcm-pt-banner.req{border-left-color:var(--purple);}",
        ".rcm-pt-printhead{display:none;}",
    "@media print{body>*:not(main){display:none!important}.rcm-pt-noprint,.rcm-pt-row,.rcm-pt-rv details{display:none!important}.rcm-pt-printhead{display:block}.rcm-pt-card{break-inside:avoid;border-color:#999}}"
  ].join("\n");
  function addCss() {
    if (document.getElementById("rcm-pt-css")) return;
    var s = el("style"); s.id = "rcm-pt-css"; s.textContent = CSS; document.head.appendChild(s);
  }

  /* ── pre-test page ──────────────────────────────────────────────────────────────────────────────────────── */
  function pretestPage(D, root) {
    var M = D.mods, pct = Math.round(D.mastery * 100), retakeMs = D.retake * 3600 * 1000;
    var all = load(), rec = trackRec(all, D.track);
    var queue = [], qi = 0;

    function res(m) { return rec.mods[m.n]; }
    function canRetake(m) { var r = res(m); return !r || Date.now() - (r.at || 0) >= retakeMs; }
    function draw(n, k) { var a = []; for (var i = 0; i < n; i++) a.push(i); for (var j = a.length - 1; j > 0; j--) { var x = Math.floor(Math.random() * (j + 1)), t = a[j]; a[j] = a[x]; a[x] = t; } return a.slice(0, Math.min(k, n)); }
    function counts() {
      var c = { out: 0, study: 0, req: 0, none: 0 };
      M.forEach(function (m) { c[status(m.a, res(m), D.mastery)]++; });
      return c;
    }
    function top() { try { root.scrollIntoView({ behavior: "smooth", block: "start" }); } catch (e) { window.scrollTo(0, 0); } }

    function render() {
      var c = counts();
      if (c.out + c.study === 0) return renderStart();
      renderResults();
    }

    function testable(onlyEligible) {
      return M.filter(function (m) { return m.q && (!onlyEligible || (status(m.a, res(m), D.mastery) !== "out" && canRetake(m))); });
    }

    function renderStart() {
      root.innerHTML = "";
      var card = el("div", "rcm-pt-card");
      var test = testable(false), req = M.filter(function (m) { return m.a; });
      card.innerHTML = "<h3>Choose the modules to test</h3><p class='rcm-pt-muted'>All " + test.length +
        " testable modules are ticked. Untick any you already know you want to study; you can test them later. " +
        "Allow about a minute per question.</p>";
      var box = el("div");
      test.forEach(function (m) {
        var lab = el("label", "rcm-pt-pick");
        lab.innerHTML = "<input type='checkbox' checked value='" + m.n + "'><span><b>Module " + modNum(m.n) + "</b> · " + esc(m.t) +
          " <span class='rcm-pt-note'>(" + Math.min(D.per, m.q.length) + " questions)</span></span>";
        box.appendChild(lab);
      });
      card.appendChild(box);
      var info = el("p", "rcm-pt-muted");
      var row = el("div", "rcm-pt-row");
      var go = el("button", "nc-btn"); go.type = "button";
      function upd() {
        var picked = box.querySelectorAll("input:checked"), q = 0;
        Array.prototype.forEach.call(picked, function (i) { var m = byN(i.value); q += Math.min(D.per, m.q.length); });
        go.textContent = picked.length ? "Start the pre-test (" + picked.length + " module" + (picked.length > 1 ? "s" : "") + ", " + q + " questions)" : "Tick at least one module";
        go.disabled = !picked.length;
      }
      box.addEventListener("change", upd); upd();
      go.addEventListener("click", function () {
        var ns = Array.prototype.map.call(box.querySelectorAll("input:checked"), function (i) { return i.value; });
        start(ns.map(byN));
      });
      row.appendChild(go); card.appendChild(row); card.appendChild(info);
      root.appendChild(card);
      if (req.length) {
        var rc = el("div", "rcm-pt-card");
        rc.innerHTML = "<h3>Always required (" + req.length + ")</h3><p class='rcm-pt-muted'>Everyone studies these, however experienced.</p>";
        rc.appendChild(listOf(req, false));
        root.appendChild(rc);
      }
    }

    function byN(n) { for (var i = 0; i < M.length; i++) if (M[i].n === n) return M[i]; return null; }

    function start(mods) { queue = mods; qi = 0; renderModule(); top(); }

    function renderModule() {
      var m = queue[qi];
      if (!m) { renderResults(true); top(); return; }
      var pick = draw(m.q.length, D.per);
      root.innerHTML = "";
      var card = el("div", "rcm-pt-card");
      card.innerHTML = "<div class='rcm-pt-note'>Module " + (qi + 1) + " of " + queue.length + " in this sitting</div>" +
        "<div class='rcm-pt-bar'><span style='width:" + Math.round(qi / queue.length * 100) + "%'></span></div>" +
        "<h3>Module " + modNum(m.n) + " · " + esc(m.t) + "</h3><p class='rcm-pt-muted'>Choose the single best answer. " +
        "Answers are shown after this module is scored.</p>";
      var form = el("form"); form.noValidate = true;
      pick.forEach(function (bi, k) {
        var q = m.q[bi], fs = el("fieldset", "rcm-pt-q");
        var lg = el("legend", null, (k + 1) + ". " + q[0]); fs.appendChild(lg);
        q[1].forEach(function (o, oi) {
          var lab = el("label"); var id = "pt" + k + "o" + oi;
          lab.innerHTML = "<input type='radio' name='q" + k + "' value='" + oi + "' id='" + id + "'><span>" + o[0] + "</span>";
          fs.appendChild(lab);
        });
        form.appendChild(fs);
      });
      var row = el("div", "rcm-pt-row");
      var sub = el("button", "nc-btn"); sub.type = "submit"; sub.textContent = qi + 1 < queue.length ? "Score this module and go on" : "Score this module and see my results";
      var stop = el("button", "nc-btn nc-btn-ghost"); stop.type = "button"; stop.textContent = "Stop here (results so far are saved)";
      row.appendChild(sub); row.appendChild(stop); form.appendChild(row);
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var answers = pick.map(function (bi, k) { var c = form.querySelector("input[name='q" + k + "']:checked"); return c ? +c.value : -1; });
        var blank = answers.filter(function (a) { return a < 0; }).length;
        if (blank && !window.confirm(blank + " question" + (blank > 1 ? "s are" : " is") + " unanswered and will count as wrong. Score this module anyway?")) return;
        var s = 0; pick.forEach(function (bi, k) { var o = m.q[bi][1][answers[k]]; if (o && o[1]) s++; });
        all = load(); rec = trackRec(all, D.track);
        rec.mods[m.n] = { s: s, t: pick.length, m: D.mastery, at: Date.now(), q: pick, a: answers };
        if (!save(all)) window.alert("This browser would not save the result (private mode or storage full).");
        qi++; renderModule(); top();
      });
      stop.addEventListener("click", function () { renderResults(); top(); });
      card.appendChild(form);
      root.appendChild(card);
    }

    function listOf(mods, withResult) {
      var ul = el("ul", "rcm-pt-list");
      mods.forEach(function (m) {
        var st = status(m.a, res(m), D.mastery), r = res(m), li = el("li");
        var chip = { out: "Optional · placed out", study: "Study", req: "Required", none: "Not tested" }[st];
        var why = m.a ? esc(D.cats[m.a] || "") : (r && r.t ? "Pre-test " + r.s + " of " + r.t + " (" + Math.round(r.s / r.t * 100) + "%) on " + fmtDate(r.at) : "");
        if (st === "study" && !canRetake(m)) why += ". Retake from " + fmtWhen(r.at + retakeMs);
        li.innerHTML = "<span class='rcm-pt-num'>" + modNum(m.n) + "</span><span class='rcm-pt-body'><a href='" + esc(m.f) + "'>" + esc(m.t) + "</a>" +
          (why ? "<span class='rcm-pt-why'>" + why + "</span>" : "") + "</span>" + (withResult === false && st === "req" ? "" : "<span class='rcm-pt-chip " + st + "'>" + chip + "</span>");
        if (withResult && r && r.q && m.q) li.querySelector(".rcm-pt-body").appendChild(review(m, r));
        ul.appendChild(li);
      });
      return ul;
    }

    function review(m, r) {
      var d = el("details", "rcm-pt-rv"); d.appendChild(el("summary", null, "Review my answers"));
      r.q.forEach(function (bi, k) {
        var q = m.q[bi]; if (!q) return;
        var mine = q[1][r.a[k]], right = null; q[1].forEach(function (o) { if (o[1]) right = o; });
        var ok = mine && mine[1];
        var p = el("div");
        p.innerHTML = "<p style='margin:10px 0 2px'>" + (k + 1) + ". " + q[0] + "</p>" +
          "<div><span class='" + (ok ? "ok" : "bad") + "'>" + (ok ? "✓ Right" : "✗ " + (mine ? "You chose: " + mine[0] : "Not answered")) + "</span></div>" +
          (ok ? "" : "<div><span class='ok'>Best answer:</span> " + right[0] + "</div>") +
          (right && right[2] ? "<div class='rat'>" + right[2] + "</div>" : "");
        d.appendChild(p);
      });
      return d;
    }

    function renderResults(justFinished) {
      all = load(); rec = trackRec(all, D.track);
      var c = counts(), need = M.filter(function (m) { var s = status(m.a, res(m), D.mastery); return s !== "out"; });
      root.innerHTML = "";
      var head = el("div", "rcm-pt-printhead");
      head.innerHTML = "<h2>Placement pre-test result · " + esc(D.name || D.track) + "</h2><p>Renal Care Academy · printed " + fmtDate(Date.now()) +
        ". Self-assessment on the learner's own device; not a certificate. Mastery to place out: " + pct + "%.</p>";
      root.appendChild(head);
      var card = el("div", "rcm-pt-card");
      card.innerHTML = "<h3>" + (justFinished ? "Done. Here is your study path" : "Your study path") + "</h3>" +
        "<div class='rcm-pt-sum'><div><b>" + c.out + "</b><span>optional: placed out</span></div><div><b>" + c.study + "</b><span>to study</span></div>" +
        "<div><b>" + c.req + "</b><span>always required</span></div>" + (c.none ? "<div><b>" + c.none + "</b><span>not tested yet</span></div>" : "") + "</div>" +
        "<p class='rcm-pt-muted'>Study the modules marked <b>Study</b>, <b>Required</b> and <b>Not tested</b>, in order. " +
        "For the certificate you still pass every module quiz; for a module marked <b>Optional</b>, open it and go straight to its self-assessment.</p>";
      var row = el("div", "rcm-pt-row");
      var first = need[0];
      if (first) { var a = el("a", "nc-btn", "Start with Module " + modNum(first.n)); a.href = first.f; row.appendChild(a); }
      var more = testable(true);
      if (more.length) {
        var b = el("button", "nc-btn nc-btn-ghost"); b.type = "button";
        b.textContent = (c.none ? "Test more modules" : "Retake eligible modules") + " (" + more.length + ")";
        b.addEventListener("click", function () { renderPick(more); top(); }); row.appendChild(b);
      }
      var pr = el("button", "nc-btn nc-btn-ghost"); pr.type = "button"; pr.textContent = "Print my result";
      pr.addEventListener("click", function () { window.print(); }); row.appendChild(pr);
      var rs = el("button", "nc-btn nc-btn-ghost"); rs.type = "button"; rs.textContent = "Start over";
      rs.addEventListener("click", function () {
        if (!window.confirm("Delete your pre-test results for this track on this device?")) return;
        all = load(); delete all[D.track]; save(all); rec = trackRec(all, D.track); renderStart(); top();
      });
      row.appendChild(rs);
      card.appendChild(row);
      root.appendChild(card);
      var lc = el("div", "rcm-pt-card");
      lc.innerHTML = "<h3>Every module</h3>";
      lc.appendChild(listOf(M, true));
      root.appendChild(lc);
      var sig = el("div", "rcm-pt-printhead");
      sig.innerHTML = "<p style='margin-top:28px'>Reviewed by the head nurse, preceptor or supervisor: ______________________________ &nbsp; Date: ____________</p>";
      root.appendChild(sig);
    }

    function renderPick(mods) {
      root.innerHTML = "";
      var card = el("div", "rcm-pt-card");
      card.innerHTML = "<h3>Choose the modules to test</h3><p class='rcm-pt-muted'>Modules not yet tested, and modules below " + pct +
        "% whose " + D.retake + "-hour wait has passed. A retake draws a fresh set of questions where the bank allows.</p>";
      var box = el("div");
      mods.forEach(function (m) {
        var lab = el("label", "rcm-pt-pick");
        lab.innerHTML = "<input type='checkbox' checked value='" + m.n + "'><span><b>Module " + modNum(m.n) + "</b> · " + esc(m.t) + "</span>";
        box.appendChild(lab);
      });
      card.appendChild(box);
      var row = el("div", "rcm-pt-row");
      var go = el("button", "nc-btn", "Start"); go.type = "button";
      go.addEventListener("click", function () {
        var ns = Array.prototype.map.call(box.querySelectorAll("input:checked"), function (i) { return byN(i.value); });
        if (ns.length) start(ns);
      });
      var back = el("button", "nc-btn nc-btn-ghost", "Back to my results"); back.type = "button";
      back.addEventListener("click", function () { renderResults(); top(); });
      row.appendChild(go); row.appendChild(back); card.appendChild(row);
      root.appendChild(card);
    }

    render();
  }

  /* ── track hub ──────────────────────────────────────────────────────────────────────────────────────────── */
  function hubPage(H) {
    var r = (load()[H.track] || {}).mods || {};
    var c = { out: 0, study: 0, req: 0, none: 0 }, tested = 0;
    H.mods.forEach(function (m) { var st = status(m[3], r[m[0]], H.mastery); c[st]++; if (r[m[0]] && !m[3]) tested++; });
    if (!tested) return;
    var app = document.getElementById("rcm-pt-hub-app");
    if (app) {
      app.innerHTML = "<div class='rcm-pt-card'><h3>Your pre-test result</h3><div class='rcm-pt-sum'>" +
        "<div><b>" + c.out + "</b><span>optional: placed out</span></div><div><b>" + c.study + "</b><span>to study</span></div>" +
        "<div><b>" + c.req + "</b><span>always required</span></div>" + (c.none ? "<div><b>" + c.none + "</b><span>not tested yet</span></div>" : "") +
        "</div><div class='rcm-pt-row'><a class='nc-btn' href='" + esc(H.page) + "'>See my study path</a></div></div>";
    }
    var label = { out: "Optional", study: "Study", req: "Required" };
    H.mods.forEach(function (m) {
      var st = status(m[3], r[m[0]], H.mastery);
      if (!label[st]) return;
      Array.prototype.forEach.call(document.querySelectorAll(".nc-mod[href='" + m[2] + "'] .nc-mod-top"), function (top) {
        if (top.querySelector(".rcm-pt-badge")) return;
        var b = el("span", "rcm-pt-chip rcm-pt-badge " + st, label[st]);
        b.title = st === "out" ? "Placed out by the pre-test: reading is optional" : st === "req" ? "Required for every learner" : "On your study path";
        top.appendChild(b);
      });
    });
  }

  /* ── module page ────────────────────────────────────────────────────────────────────────────────────────── */
  function modulePage(track, nn) {
    var t = load()[track];
    if (!t || !t.mods) return;
    var r = t.mods[nn];
    var page = track + "-pretest.html";
    var b;
    if (r && r.t && r.s / r.t >= (r.m || 0.8) - 1e-9) {
      b = el("div", "rcm-pt-banner",
        "<b>You placed out of this module</b> on " + fmtDate(r.at) + " (pre-test " + r.s + " of " + r.t + "). Reading it is optional for you. " +
        "The certificate still needs this module&rsquo;s quiz: <a href='#quiz'>go to the self-assessment</a> · <a href='" + page + "'>my study path</a>");
    } else if (r && r.t) {
      b = el("div", "rcm-pt-banner study",
        "<b>On your study path.</b> Your pre-test score for this module was " + r.s + " of " + r.t + ". <a href='" + page + "'>My study path</a>");
    } else {
      return;   // required or untested: no banner
    }
    var hero = document.querySelector(".hero .container, .hero");
    var meta = hero && hero.querySelector(".hero-meta");
    if (meta) meta.parentNode.insertBefore(b, meta.nextSibling);
    else if (hero) hero.appendChild(b);
    else { var main = document.querySelector("main"); if (main) main.insertBefore(b, main.firstChild); }
  }

  function init() {
    var D = json("rcm-pt-data"), root = document.getElementById("rcm-pt-app");
    if (D && root) { addCss(); return pretestPage(D, root); }
    var H = json("rcm-pt-hub");
    if (H) { addCss(); return hubPage(H); }
    if (me && me.getAttribute("data-track")) { addCss(); modulePage(me.getAttribute("data-track"), me.getAttribute("data-mod")); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
