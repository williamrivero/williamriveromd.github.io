/* Renal Care Academy · Resuscitation Lab Practice Lab (Nov 2026). DRAFT pending clinical sign-off.
   Three tools on academy/resuscitation-lab-practice.html, built by tools/academy/apply_resus_lab.py:
     1. Algorithm recognition trainer (items in #rl-rec-data): practice, timed round, repeat my misses.
     2. Timed megacode runner (cases in #rl-cases-data, the same files the module pages use).
     3. Facilitator recorder with a shared monitor display (?display=1 opens the display; BroadcastChannel keeps it in step).
   Nothing is sent anywhere. Results stay on this device (localStorage "rcm-resus-rec", "rcm-resus-mc").
   Deterministic: every transition, answer and score comes from the reviewed data files; nothing is generated. */
(function () {
  "use strict";
  if (typeof document === "undefined") return;
  var REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function $(s, r) { return (r || document).querySelector(s); }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function json(id) { var n = document.getElementById(id); try { return n ? JSON.parse(n.textContent) : null; } catch (e) { return null; } }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || "null"); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  function mmss(s) { s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function epaper() { return document.documentElement.getAttribute("data-shade") === "epaper"; }

  /* ── rhythm drawing (same shapes as academy-cases.js) ── */
  function wave(shape, t, hr) {
    var g = function (c, w, a) { return a * Math.exp(-Math.pow((t - c) / w, 2)); };
    if (shape === "sine") { var rr = 60 / Math.max(25, hr); return 0.42 * Math.sin(2 * Math.PI * t / rr) + 0.2; }
    if (shape === "svt") return g(0.2, 0.012, -0.1) + g(0.22, 0.012, 0.85) + g(0.24, 0.012, -0.18) + g(0.34, 0.04, 0.16);
    if (shape === "wide") return g(0.08, 0.025, 0.1) + g(0.24, 0.045, 0.75) + g(0.32, 0.04, -0.25);
    var y = shape === "irregular" ? 0.02 * Math.sin(t * 40) : g(0.08, 0.025, 0.12);
    y += g(0.2, 0.012, -0.12) + g(0.22, 0.012, 0.9) + g(0.24, 0.012, -0.2);
    if (shape === "peaked") y += g(0.42, 0.035, 0.62); else if (shape === "longqt") y += g(0.62, 0.075, 0.2); else y += g(0.44, 0.06, 0.22);
    return y;
  }
  function cont(shape, T, hr) {
    if (shape === "asystole") return 0.012 * Math.sin(T * 4.4) + 0.006 * Math.sin(T * 23);
    if (shape === "torsades") {      // polymorphic VT: wide complexes whose height swells, narrows to a waist and flips polarity
      var ph = 2 * Math.PI * T * Math.max(150, hr || 240) / 60, env = Math.sin(2 * Math.PI * T / 3.0);
      return 0.62 * env * (0.78 * Math.sin(ph) + 0.22 * Math.sin(2 * ph + 0.6)) + 0.2;
    }
    var amp = 0.62 + 0.38 * Math.sin(T * 1.3);
    return amp * (0.24 * Math.sin(T * 33.3) + 0.17 * Math.sin(T * 44.6 + 1) + 0.1 * Math.sin(T * 23.2 + 2)) + 0.2;
  }
  var CONT = { vf: 1, asystole: 1, torsades: 1 };
  var BEATS = { torsades: 1 };   // continuous on the screen, but the QRS counter still counts (and can beep)
  /* Pleth: one arterial pulse, u = fraction of the cardiac cycle since the pulse reached the finger */
  function plethWave(u) {
    if (u < 0) return 0;
    if (u < 0.13) return 0.5 - 0.5 * Math.cos(Math.PI * u / 0.13);
    var d = u - 0.13;
    return Math.exp(-d * 3.1) * (1 - 0.2 * Math.exp(-Math.pow((u - 0.37) / 0.045, 2))) + 0.11 * Math.exp(-Math.pow((u - 0.45) / 0.06, 2));
  }
  /* Strip(canvas[, plethCanvas]): ECG sweep, optionally with a pleth trace that follows each beat.
     Gain is fixed in CSS pixels (like mm/mV on a monitor), so a taller canvas gives more room, never taller waves. */
  function Strip(canvas, pc) {
    var ctx = canvas.getContext && canvas.getContext("2d"), pctx = pc && pc.getContext && pc.getContext("2d");
    var shape = "normal", hr = 70, raf = 0, x = 0, prevY = null, beatT = -1, next = 0, last = 0, artT = 0, animating = false;
    var pa = 0, pPrev = null, pT = -1, pRR = 0.85, pCarry = 0, pVal = 0, pending = [], hooks = {}, syncOn = false, marks = [];
    var ECG_GAIN = 88, PL_GAIN = 64;
    function fit(cv, c) {
      var r = window.devicePixelRatio || 1, w = cv.clientWidth || 320, h = cv.clientHeight || 70;
      cv.width = Math.round(w * r); cv.height = Math.round(h * r); c.setTransform(r, 0, 0, r, 0, 0);
      c.fillStyle = "#0b1220"; c.fillRect(0, 0, w, h); return [w, h];
    }
    function size() { var d = fit(canvas, ctx); if (pctx) fit(pc, pctx); x = 0; prevY = null; pPrev = null; return d; }
    function eg(h) { var g = Math.min(h * 0.6, ECG_GAIN); return [g, h / 2 + g / 3]; }           // gain, baseline (0.7h on small strips, as before)
    function pg(h) { var g = Math.min(h * 0.62, PL_GAIN); return [g, h / 2 + g / 2]; }
    function plethAt(now) {
      while (pending.length && now >= pending[0][0]) { var q = pending.shift(); pCarry = pVal; pT = q[0]; pRR = Math.min(1.3, Math.max(0.34, q[1])); if (pa && hooks.pulse) hooks.pulse(0); }
      if (pT < 0) return 0;
      var dt = now - pT; pVal = plethWave(dt / pRR) + pCarry * Math.exp(-dt * 9); return pVal;
    }
    function plethY(v, h, now) {
      var g = pg(h);
      if (!pa) return g[1] - g[0] * 0.03 * (Math.sin(now * 7.1) + 0.6 * Math.sin(now * 19.3));          // no pulse: near-flat line
      return g[1] - v * g[0] * pa;
    }
    function still() {
      var d = size(), w = d[0], h = d[1], rr = 60 / Math.max(25, hr), py = null, G = eg(h);
      ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.7;
      for (var px = 0; px < w; px++) {
        var t = px / 80, k = shape === "irregular" ? (t % (rr * (0.7 + 0.6 * Math.abs(Math.sin(Math.floor(t / rr) * 7.3))))) : t % rr;
        var y = G[1] - (CONT[shape] ? cont(shape, t, hr) : wave(shape, k, hr)) * G[0];
        ctx.beginPath(); ctx.moveTo(px - 1, py == null ? y : py); ctx.lineTo(px, y); ctx.stroke(); py = y;
      }
      if (!pctx) return;
      var pw = pc.clientWidth || w, ph = pc.clientHeight || 60, qy = null; pctx.strokeStyle = "#22d3ee"; pctx.lineWidth = 2;
      for (var qx = 0; qx < pw; qx++) {
        var tt = qx / 80, u = ((tt - 0.22) % rr + rr) % rr / Math.min(1.3, rr), yy = plethY(plethWave(u), ph, tt);
        pctx.beginPath(); pctx.moveTo(qx - 1, qy == null ? yy : qy); pctx.lineTo(qx, yy); pctx.stroke(); qy = yy;
      }
    }
    function frame(ts) {
      if (!last) last = ts; var dt = Math.min(0.05, (ts - last) / 1000); last = ts;
      var w = canvas.clientWidth, h = canvas.clientHeight, steps = Math.max(1, Math.round(dt * 80)), G = eg(h);
      var ph = pctx ? pc.clientHeight : 0, pw = pctx ? pc.clientWidth : 0;
      for (var i = 0; i < steps; i++) {
        var now = ts / 1000 + i / 80;
        if (beatT < 0 || now >= next) {
          beatT = now; var rr = 60 / Math.max(25, hr); if (shape === "irregular") rr *= 0.6 + Math.random() * 0.8; next = now + rr;
          if (!CONT[shape] || BEATS[shape]) {
            pending.push([now + 0.42, rr]);                                                       // the QRS peaks 0.22 s into the cycle; the pulse reaches the finger ~0.2 s later
            if (hooks.qrs) hooks.qrs(i / 80 + 0.22);                                             // QRS beep, scheduled at the R wave
            if (syncOn && !CONT[shape]) marks.push(x + 18);                                       // sync sense marker over the coming R wave (0.22 s × 80 px/s)
          }
        }
        var y = G[1] - (CONT[shape] ? cont(shape, now, hr) : wave(shape, now - beatT, hr)) * G[0];
        if (artT && now < artT + 1.2) { var a = now - artT; y = a < 0.05 ? G[1] - G[0] * 1.1 : a < 0.1 ? G[1] + G[0] * 0.45 : G[1] - G[0] * 0.42 * Math.exp(-(a - 0.1) * 4); }
        ctx.fillStyle = "#0b1220"; ctx.fillRect(x, 0, 8, h); ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.7;
        ctx.beginPath(); ctx.moveTo(x - 1, prevY == null ? y : prevY); ctx.lineTo(x, y); ctx.stroke(); prevY = y;
        if (marks.length && x >= marks[0] + 6) {   // drawn just behind the sweep so the eraser does not wipe it
          var mx = marks.shift(); if (mx <= w) { var top = Math.max(7, G[1] - G[0] * 0.9 - 12);
            ctx.fillStyle = "#ffffff"; ctx.beginPath(); ctx.moveTo(mx - 5, top - 7); ctx.lineTo(mx + 5, top - 7); ctx.lineTo(mx, top); ctx.closePath(); ctx.fill(); }
        }
        if (pctx && x <= pw) {
          var v = plethAt(now), yy = plethY(v, ph, now);
          if (artT && now < artT + 0.8) yy += (Math.random() - 0.5) * pg(ph)[0] * 0.8;
          pctx.fillStyle = "#0b1220"; pctx.fillRect(x, 0, 8, ph); pctx.strokeStyle = "#22d3ee"; pctx.lineWidth = 2;
          pctx.beginPath(); pctx.moveTo(x - 1, pPrev == null ? yy : pPrev); pctx.lineTo(x, yy); pctx.stroke(); pPrev = yy;
        }
        x++;
        if (x > w) { x = 0; prevY = null; pPrev = null; marks = marks.filter(function (m) { return m > w; }).map(function (m) { return m - w - 1; }); }
      }
      raf = requestAnimationFrame(frame);
    }
    // redraw at the real size whenever the canvas is resized (full screen, rotation), so nothing is stretched
    if (ctx && window.ResizeObserver) {
      var lw = 0, lh = 0;
      var ro = new ResizeObserver(function () {
        var w = canvas.clientWidth, h = canvas.clientHeight + (pc ? pc.clientHeight : 0);
        if (w === lw && h === lh) return; lw = w; lh = h;
        if (animating) size(); else if (lw) still();
      });
      ro.observe(canvas); if (pc) ro.observe(pc);
    }
    return {
      set: function (s, rate, animate, plethAmp) {
        if (!ctx) return; shape = s || "normal"; hr = +rate || 70;
        pa = CONT[shape] && !BEATS[shape] ? 0 : plethAmp == null ? 0.85 : Math.max(0, Math.min(1, plethAmp));
        if (raf) { cancelAnimationFrame(raf); raf = 0; }
        if (!animate || REDUCED || epaper()) { animating = false; still(); return; }
        animating = true; size(); last = 0; beatT = -1; pending = []; marks = []; pT = -1; pVal = 0; pCarry = 0; raf = requestAnimationFrame(frame);
      },
      stop: function () { if (raf) cancelAnimationFrame(raf); raf = 0; animating = false; },
      shock: function () { artT = performance.now() / 1000; },
      on: function (h) { hooks = h || {}; },
      sync: function (on) { syncOn = !!on; marks = []; }
    };
  }

  /* ════════════ 1. Recognition trainer ════════════ */
  function Recognition(host, data) {
    var items = data.items, TAGS = data.tags, state = store("rcm-resus-rec") || { miss: {}, tags: {}, best: 0, done: 0 };
    var queue = [], idx = 0, mode = "practice", answers = [], timer = 0, left = 0, orderPick = [];
    var TYPE = { pick: "Choose the algorithm and first action", strip: "Rhythm strip with findings", missing: "Find the missing assessment", order: "Arrange the steps", unsafe: "Spot the unsafe action", evolve: "The patient changes" };
    host.innerHTML = "";
    var ctl = el("div", "rl-ctl");
    ctl.innerHTML = '<fieldset class="rl-fs"><legend>Mode</legend>' +
      '<label><input type="radio" name="rl-mode" value="practice" checked> Practice (feedback after each item)</label>' +
      '<label><input type="radio" name="rl-mode" value="timed"> Timed round (10 items, 30 seconds each)</label>' +
      '<label><input type="radio" name="rl-mode" value="misses"> Repeat my misses</label></fieldset>' +
      '<fieldset class="rl-fs"><legend>Case sets</legend>' +
      '<label><input type="checkbox" name="rl-set" value="adult" checked> Adult</label>' +
      '<label><input type="checkbox" name="rl-set" value="pediatric" checked> Pediatric</label>' +
      '<label><input type="checkbox" name="rl-set" value="dialysis" checked> Dialysis-specific</label></fieldset>' +
      '<button type="button" class="rl-btn rl-go">Start</button> <span class="rl-meta"></span>';
    host.appendChild(ctl);
    var stage = el("div", "rl-stage"); host.appendChild(stage);
    function meta() {
      var tops = Object.keys(state.tags).sort(function (a, b) { return state.tags[b] - state.tags[a]; }).slice(0, 2);
      $(".rl-meta", ctl).innerHTML = state.done ? "Items answered on this device: <b>" + state.done + "</b>. Best timed round: <b>" + state.best + "/10</b>." +
        (tops.length ? " Most missed: " + tops.map(function (t) { return TAGS[t]; }).join("; ") + "." : "") : "";
    }
    meta();
    function pickSet() {
      var sets = Array.prototype.map.call(ctl.querySelectorAll('input[name="rl-set"]:checked'), function (c) { return c.value; });
      return items.filter(function (it) { return it.set.some(function (s) { return sets.indexOf(s) >= 0; }); });
    }
    $(".rl-go", ctl).addEventListener("click", function () {
      mode = ctl.querySelector('input[name="rl-mode"]:checked').value;
      var pool = pickSet();
      if (mode === "misses") pool = pool.filter(function (it) { return state.miss[it.id]; });
      if (!pool.length) { stage.innerHTML = '<p class="rl-note">' + (mode === "misses" ? "No missed items yet on this device. Try a practice round first." : "Choose at least one case set.") + "</p>"; return; }
      queue = shuffle(pool).slice(0, mode === "timed" ? 10 : 12); idx = 0; answers = []; show();
    });
    function show() {
      clearInterval(timer);
      if (idx >= queue.length) return finish();
      var it = queue[idx]; orderPick = [];
      stage.innerHTML = "";
      var card = el("div", "rl-card");
      card.appendChild(el("div", "rl-top", '<span class="rl-type">' + TYPE[it.type] + '</span><span class="rl-count">Item ' + (idx + 1) + " of " + queue.length + "</span>" + (mode === "timed" ? '<span class="rl-timer" aria-live="off"></span>' : "")));
      card.appendChild(el("p", "rl-stem", it.stem));
      if (it.strip) {
        var cv = el("canvas", "rl-strip"); cv.setAttribute("role", "img"); cv.setAttribute("aria-label", "Rhythm strip. The patient findings are given in text below the strip.");
        card.appendChild(cv); setTimeout(function () { Strip(cv).set(it.strip.rhythm, it.strip.rate, false); }, 0);
        card.appendChild(el("p", "rl-find", "<b>At the patient:</b> " + it.findings));
      }
      var opts = el("div", "rl-opts" + (it.type === "order" ? " rl-order" : ""));
      var order = shuffle(it.options.map(function (_, i) { return i; }));
      order.forEach(function (i) {
        var b = el("button", "rl-opt", it.options[i]); b.type = "button"; b.dataset.i = i;
        b.addEventListener("click", function () { choose(it, i, b); });
        opts.appendChild(b);
      });
      card.appendChild(opts);
      if (it.type === "order") {
        var row = el("div", "rl-orow", '<span class="rl-oseq">Tap the steps in order.</span> ');
        var chk = el("button", "rl-btn", "Check order"); chk.type = "button"; chk.addEventListener("click", function () { checkOrder(it); });
        var rs = el("button", "rl-btn rl-ghost", "Reset"); rs.type = "button"; rs.addEventListener("click", function () { show(); });
        row.appendChild(chk); row.appendChild(rs); card.appendChild(row);
      }
      card.appendChild(el("div", "rl-fb")); stage.appendChild(card);
      if (mode === "timed") {
        left = 30; tick();
        timer = setInterval(function () { left--; tick(); if (left <= 0) { clearInterval(timer); record(it, null, false); idx++; show(); } }, 1000);
      }
      var first = card.querySelector(".rl-opt"); if (first && idx > 0) first.focus();
    }
    function tick() { var t = $(".rl-timer", stage); if (t) { t.textContent = left + " s"; t.classList.toggle("warn", left <= 10); } }
    function record(it, choice, ok) {
      answers.push({ it: it, choice: choice, ok: ok }); state.done++;
      if (ok) { if (state.miss[it.id]) delete state.miss[it.id]; }
      else { state.miss[it.id] = (state.miss[it.id] || 0) + 1; state.tags[it.tag] = (state.tags[it.tag] || 0) + 1; }
      store("rcm-resus-rec", state);
    }
    function lock(card) { Array.prototype.forEach.call(card.querySelectorAll(".rl-opt, .rl-orow .rl-btn"), function (b) { b.disabled = true; }); }
    function choose(it, i, btn) {
      var card = $(".rl-card", stage);
      if (it.type === "order") {
        if (orderPick.indexOf(i) >= 0) return;
        orderPick.push(i); btn.classList.add("picked"); btn.setAttribute("data-n", orderPick.length);
        $(".rl-oseq", card).textContent = "Your order: " + orderPick.map(function (k) { return it.options[k]; }).join(" → ");
        return;
      }
      var ok = i === it.answer; record(it, i, ok);
      if (mode === "timed") { clearInterval(timer); idx++; show(); return; }
      lock(card);
      Array.prototype.forEach.call(card.querySelectorAll(".rl-opt"), function (b) { var k = +b.dataset.i; if (k === it.answer) b.classList.add("right"); else if (k === i) b.classList.add("wrong"); });
      feedback(card, it, ok, it.why[i] + (ok ? "" : " <b>Best:</b> " + it.options[it.answer] + ". " + it.why[it.answer]));
    }
    function checkOrder(it) {
      var card = $(".rl-card", stage);
      if (orderPick.length !== it.options.length) { $(".rl-oseq", card).textContent = "Tap all " + it.options.length + " steps first."; return; }
      var ok = orderPick.every(function (k, n) { return k === it.answer[n]; }); record(it, orderPick.slice(), ok);
      if (mode === "timed") { clearInterval(timer); idx++; show(); return; }
      lock(card);
      feedback(card, it, ok, "<b>Correct order:</b> " + it.answer.map(function (k) { return it.options[k]; }).join(" → ") + ". " + it.why);
    }
    function feedback(card, it, ok, text) {
      var fb = $(".rl-fb", card);
      fb.innerHTML = '<p class="rl-verdict ' + (ok ? "ok" : "no") + '">' + (ok ? "Correct." : "Not quite.") + "</p><p>" + text + "</p>" +
        (ok ? "" : '<p class="rl-tag">Common error: ' + TAGS[it.tag] + "</p>") +
        '<p class="rl-mod">Taught in <a href="' + modHref(it.mod) + '">Module ' + it.mod + "</a>.</p>";
      var nx = el("button", "rl-btn", idx + 1 < queue.length ? "Next item" : "See results"); nx.type = "button";
      nx.addEventListener("click", function () { idx++; show(); }); fb.appendChild(nx); nx.focus();
    }
    function finish() {
      clearInterval(timer);
      var right = answers.filter(function (a) { return a.ok; }).length;
      if (mode === "timed" && right > (state.best || 0)) { state.best = right; store("rcm-resus-rec", state); }
      var miss = answers.filter(function (a) { return !a.ok; });
      var tags = {}; miss.forEach(function (a) { tags[a.it.tag] = (tags[a.it.tag] || 0) + 1; });
      var h = '<div class="rl-card"><h3>' + right + " of " + answers.length + " correct</h3>";
      if (mode === "timed") {
        h += "<ol class=\"rl-review\">" + answers.map(function (a) {
          var it = a.it, best = it.type === "order" ? it.answer.map(function (k) { return it.options[k]; }).join(" → ") : it.options[it.answer];
          return "<li class=\"" + (a.ok ? "ok" : "no") + "\"><b>" + (a.ok ? "Correct" : (a.choice === null ? "Time ran out" : "Missed")) + ":</b> " + it.stem + "<br><small>Best: " + best + ". " + (it.type === "order" ? it.why : it.why[it.answer]) + "</small></li>";
        }).join("") + "</ol>";
      }
      if (miss.length) h += "<p><b>Patterns to work on:</b> " + Object.keys(tags).map(function (t) { return TAGS[t] + " (" + tags[t] + ")"; }).join("; ") + ". Use <i>Repeat my misses</i> to practice them.</p>";
      h += '<p class="rl-note">Recognition practice is an educational result on this device only. It is not a certification or a competence assessment.</p></div>';
      stage.innerHTML = h; meta();
    }
    function modHref(n) { var a = document.querySelector('a[data-rl-mod="' + n + '"]'); return a ? a.getAttribute("href") : "resuscitation-lab.html"; }
  }

  /* ════════════ 2. Timed megacode runner ════════════ */
  function Megacode(host, cases) {
    var C = null, cur = "", clock = 0, t0 = 0, nodeStart = 0, timer = 0, log = [], strip = null, mon = {};
    var GR = { best: 2, ok: 1, poor: 0, harmful: 0 };
    host.innerHTML = "";
    var pick = el("div", "rl-ctl");
    pick.innerHTML = '<label class="rl-lab">Megacode <select class="rl-case">' + cases.map(function (c, i) { return '<option value="' + i + '">' + c.title + " (Module " + parseInt(c.page.split("-")[2], 10) + ")</option>"; }).join("") + "</select></label> " +
      '<button type="button" class="rl-btn rl-mc-go">Start timed megacode</button> <a class="rl-mc-guided" href="#">Run it guided in its module instead</a>';
    host.appendChild(pick);
    var stage = el("div", "rl-stage"); host.appendChild(stage);
    var sel = $(".rl-case", pick);
    function syncGuided() { var c = cases[+sel.value]; $(".rl-mc-guided", pick).setAttribute("href", c.page + "#sim"); }
    sel.addEventListener("change", syncGuided); syncGuided();
    $(".rl-mc-go", pick).addEventListener("click", function () { start(cases[+sel.value]); });
    var worked = false;
    host._worked = function (id) {   // sample case: the whole megacode played at its best choice, ending on the full debrief
      if (!host._start(id)) return;
      worked = true; clearInterval(timer);
      var id2 = C.start, t = 0, guard = 0;
      while (C.nodes[id2] && !C.nodes[id2].end && guard++ < 40) {
        var n = C.nodes[id2], best = n.choices.filter(function (c) { return c.grade === "best"; })[0], took = 9 + (guard * 7) % 11;
        t += took; log.push({ id: id2, prompt: n.prompt, short: n.short, choice: best, best: best, t: t, took: took });
        if (n.vitals) setMon(n.vitals); if (best.vitals) setMon(best.vitals);
        id2 = best.next;
      }
      t0 = Date.now() - (t + 8) * 1000;
      if (C.nodes[id2]) { if (C.nodes[id2].vitals) setMon(C.nodes[id2].vitals); finish(C.nodes[id2]); }
    };
    host._start = function (id) {   // sample case: start one megacode by id
      for (var i = 0; i < cases.length; i++) if (cases[i].id === id) { sel.value = i; syncGuided(); start(cases[i]); return true; }
      return false;
    };
    function start(c) {
      C = c; log = []; mon = {}; worked = false; clearInterval(timer); if (strip) strip.stop();
      stage.innerHTML = "";
      var box = el("div", "rl-card rl-mc");
      box.innerHTML = '<div class="rl-top"><span class="rl-type">Timed megacode</span><span class="rl-clock">0:00</span></div><div class="rl-intro">' + c.intro + '</div>' +
        '<div class="rl-mon"><div class="rl-mon-grid"></div><canvas class="rl-mstrip" role="img" aria-label="Monitor rhythm strip"></canvas><div class="rl-mon-lab"></div></div>' +
        '<div class="rl-scene"></div><div class="rl-node"></div>';
      stage.appendChild(box);
      strip = Strip($(".rl-mstrip", box)); setMon(c.monitor);
      t0 = Date.now(); clock = setInterval(function () { $(".rl-clock", box).textContent = mmss((Date.now() - t0) / 1000); }, 500);
      go(c.start, null);
    }
    function setMon(v) {
      if (!v) return; var box = $(".rl-mc", stage), grid = $(".rl-mon-grid", box);
      for (var k in v) if (v.hasOwnProperty(k) && ["rhythm", "rhythmLabel", "alarm", "stripRate"].indexOf(k) < 0) mon[k] = v[k];
      if (v.rhythm) mon.rhythm = v.rhythm; if (v.stripRate) mon.stripRate = v.stripRate; if (v.rhythmLabel) mon.rhythmLabel = v.rhythmLabel; if (v.alarm) mon.alarm = v.alarm;
      var order = C.monitorOrder || Object.keys(mon), labels = Object.assign({ time: "Time", bp: "BP", hr: "Pulse", spo2: "SpO₂", rr: "Resp" }, C.labels || {});
      grid.innerHTML = order.filter(function (k) { return mon[k] !== undefined; }).map(function (k) {
        return '<div class="rl-mc-c' + ((mon.alarm || []).indexOf(k) >= 0 ? " alarm" : "") + '"><span>' + (labels[k] || k) + "</span><b>" + mon[k] + "</b></div>";
      }).join("");
      $(".rl-mon-lab", box).textContent = mon.rhythmLabel || "";
      strip.set(mon.rhythm || "normal", parseFloat(mon.hr) || mon.stripRate || 70, true);
    }
    function go(id, prev) {
      clearInterval(timer);
      var n = C.nodes[id], box = $(".rl-mc", stage);
      if (n.vitals) setMon(n.vitals);
      if (n.end) return finish(n);
      $(".rl-scene", box).innerHTML = n.scene || "";
      var nd = $(".rl-node", box); nd.innerHTML = '<p class="rl-prompt"><b>' + (n.short || "") + "</b> " + n.prompt + '</p><p class="rl-budget"></p>';
      var opts = el("div", "rl-opts");
      shuffle(n.choices).forEach(function (ch) {
        var b = el("button", "rl-opt", ch.text); b.type = "button";
        b.addEventListener("click", function () { decide(id, ch); }); opts.appendChild(b);
      });
      nd.appendChild(opts);
      var budget = (C.lab && C.lab.budget) || 30, leftS = budget; nodeStart = Date.now();
      var bud = $(".rl-budget", nd); bud.textContent = "Decide within " + leftS + " seconds.";
      timer = setInterval(function () {
        leftS--; bud.textContent = leftS > 0 ? "Decide within " + leftS + " seconds." : "Time is up: the team hesitated.";
        bud.classList.toggle("warn", leftS <= 10);
        if (leftS <= 0) { clearInterval(timer); var best = n.choices.filter(function (c) { return c.grade === "best"; })[0]; decide(id, best, true); }
      }, 1000);
      var f = opts.querySelector(".rl-opt"); if (f) f.focus();
    }
    function decide(id, ch, timedOut) {
      clearInterval(timer);
      var n = C.nodes[id];
      log.push({ id: id, prompt: n.prompt, short: n.short, choice: timedOut ? null : ch, best: n.choices.filter(function (c) { return c.grade === "best"; })[0], t: (Date.now() - t0) / 1000, took: (Date.now() - nodeStart) / 1000 });
      if (ch.vitals) setMon(ch.vitals);
      var box = $(".rl-mc", stage);
      $(".rl-scene", box).innerHTML = timedOut ? "<p><i>No decision in time. The facilitator moves the scenario on.</i></p>" : (ch.then || "");
      setTimeout(function () { go(ch.next, id); }, ch.then || timedOut ? 1600 : 300);
    }
    function finish(n) {
      clearInterval(clock); clearInterval(timer);
      var box = $(".rl-mc", stage), max = log.length * 2;
      var score = log.reduce(function (a, l) { return a + (l.choice ? GR[l.choice.grade] : 0); }, 0);
      var harmful = log.filter(function (l) { return l.choice && l.choice.grade === "harmful"; });
      var res = store("rcm-resus-mc") || {}; var prev = res[C.id] || 0; if (!worked && score > prev) { res[C.id] = score; store("rcm-resus-mc", res); }
      var h = '<div class="rl-end">' + (worked ? '<p class="rl-note rl-sample-note"><b>Worked sample.</b> Every decision below was taken at its best choice, with the time it took and the reasoning, so you can see a complete run and its debrief. It is not saved as your score. Press <b>Run it again</b> to play it yourself against the clock.</p>' : "") +
        "<h3>" + (n.title || "End") + "</h3>" + n.text +
        '<p class="rl-score">Decisions: <b>' + score + " of " + max + "</b> points in " + mmss((Date.now() - t0) / 1000) + (worked ? "" : ". Best on this device: " + Math.max(prev, score) + " of " + max) + ".</p>" +
        (harmful.length ? '<p class="rl-crit">Safety-critical choice' + (harmful.length > 1 ? "s" : "") + ": repeat this megacode until each is corrected. A high score never makes up for a safety-critical error.</p>" : "") +
        '<h4>Timeline</h4><ol class="rl-review">' + log.map(function (l) {
          var c = l.choice, g = c ? c.grade : "timeout";
          return '<li class="' + (g === "best" ? "ok" : "no") + '"><b>' + mmss(l.t) + "</b> " + l.prompt + "<br><small>" + (c ? (worked ? "Best choice: " : "You chose: ") + c.text + " (" + g + ", " + Math.round(l.took) + " s)" : "Time ran out") + "</small>" +
            '<div class="rl-why">' + (c ? c.feedback : "") + (g !== "best" ? "<p><b>Best:</b> " + l.best.text + "</p>" + l.best.feedback : "") + "</div></li>";
        }).join("") + "</ol>" + (C.debrief || "") +
        '<p class="rl-note">Simulation success is an educational result, not a prediction of patient survival. Copy the timeline into the <a href="../guides/calc-resuscitation-lab-toolkit.html#tool-2">megacode timeline analyzer</a> during a facilitated drill.</p>' +
        '<button type="button" class="rl-btn rl-again">Run it again</button></div>';
      $(".rl-node", box).innerHTML = ""; $(".rl-scene", box).innerHTML = h;
      $(".rl-again", box).addEventListener("click", function () { start(C); });
    }
  }

  /* ════════════ 3. Facilitator recorder + shared display ════════════ */
  var EVENTS = [["recognition", "Recognition"], ["compressions start", "Compressions on"], ["compressions stop", "Compressions off"], ["pads on", "Pads on"], ["rhythm check", "Rhythm check"],
    ["shock", "Shock"], ["epinephrine", "Epinephrine"], ["amiodarone", "Antiarrhythmic"], ["airway", "Airway"], ["circuit stopped", "Fluid removal off"], ["blood returned", "Blood returned"],
    ["blood clamped", "Blood clamped"], ["leader handover", "Leader handover"], ["ROSC", "ROSC"], ["handover", "Handover"], ["end", "End"]];
  var ROLES = ["Leader", "Compressor 1", "Compressor 2", "Airway", "Defibrillator and drugs", "Circuit nurse", "Recorder and timer", "Watcher", "Runner"];
  var CH = window.BroadcastChannel ? new BroadcastChannel("rcm-resus-display") : null;
  function Recorder(host) {
    var start = 0, tick = 0, log = [], monState = { rhythm: "normal", rate: 72, hr: "72", bp: "128/76", spo2: "97", label: "Sinus rhythm" };
    host.innerHTML = "";
    var roles = el("div", "rl-card");
    roles.innerHTML = "<h3>Roles for this drill</h3><p class=\"rl-note\">Initials only. Small teams combine roles; the watcher never joins the arrest. Print for role cards.</p><div class=\"rl-roles\">" +
      ROLES.map(function (r) { return '<label>' + r + '<input type="text" maxlength="12" data-role="' + r + '"></label>'; }).join("") + "</div>" +
      '<button type="button" class="rl-btn rl-ghost rl-cards">Print role cards</button>';
    host.appendChild(roles);
    var rec = el("div", "rl-card");
    rec.innerHTML = '<div class="rl-top"><span class="rl-type">Recorder</span><span class="rl-clock">0:00</span></div>' +
      '<div class="rl-rbar"><button type="button" class="rl-btn rl-start">Start clock</button> <button type="button" class="rl-btn rl-ghost rl-undo">Undo last</button> <button type="button" class="rl-btn rl-ghost rl-reset">Reset</button></div>' +
      '<div class="rl-evs">' + EVENTS.map(function (e) { return '<button type="button" class="rl-ev" data-ev="' + e[0] + '">' + e[1] + "</button>"; }).join("") + "</div>" +
      '<ol class="rl-log" aria-live="polite"></ol><div class="rl-sum"></div>' +
      '<div class="rl-rbar"><button type="button" class="rl-btn rl-copy">Copy log</button> <a href="../guides/calc-resuscitation-lab-toolkit.html#tool-2" class="rl-btn rl-ghost">Open timeline analyzer</a></div>' +
      '<p class="rl-note">Data source for this log: observer timestamps. Buttons record time only; they do not measure compression depth or ventilation quality.</p>';
    host.appendChild(rec);
    var disp = el("div", "rl-card");
    disp.innerHTML = "<h3>Shared monitor display</h3><p class=\"rl-note\">Open the display on a second screen or a tablet beside the manikin. You change the rhythm and numbers here, privately; the display follows on the same device and browser.</p>" +
      '<div class="rl-roles"><label>Rhythm<select class="rl-d-r"><option value="normal">Sinus / organized</option><option value="svt">Narrow fast regular</option><option value="irregular">Irregular (AF)</option><option value="wide">Wide (VT or slow wide)</option><option value="peaked">Peaked T waves</option><option value="sine">Sine wave</option><option value="pea">Organized, no pulse (PEA)</option><option value="longqt">Long QT (sinus)</option><option value="torsades">Torsades de pointes</option><option value="vf">Ventricular fibrillation</option><option value="asystole">Asystole</option></select></label>' +
      '<label>Electrical rate<input type="number" class="rl-d-rate" value="72" min="20" max="320"></label><label>Pulse shown<input type="text" class="rl-d-hr" value="72"></label>' +
      '<label>BP shown<input type="text" class="rl-d-bp" value="128/76"></label><label>SpO₂ shown<input type="text" class="rl-d-sp" value="97"></label><label>Label<input type="text" class="rl-d-lab" value="Sinus rhythm"></label></div>' +
      '<p class="rl-note rl-d-hint">Choosing a rhythm fills in typical teaching values for it. Change any of them to fit your scenario, then press <b>Update display</b>; the display does not change until you do.</p>' +
      '<label class="rl-chk"><input type="checkbox" class="rl-d-showlab" checked> Show the label on the display (turn off when learners must name the rhythm themselves)</label>' +
      '<label class="rl-chk"><input type="checkbox" class="rl-d-defib"> Show a defibrillator on the display (energy selector, sync, charge, shock)</label>' +
      '<button type="button" class="rl-btn rl-d-send">Update display</button> <a class="rl-btn rl-ghost" href="?display=1" target="_blank" rel="noopener">Open display</a>' +
      '<p class="rl-note">On the display, tap <b>Full screen</b> to hide the browser bars. Out-of-range values turn yellow or red and the alarm bar names the problem, as on a bedside monitor; the limits are simulation defaults, not clinical thresholds. Energy on the simulated defibrillator follows the device manufacturer and your unit protocol. A shock on the display is logged in the recorder when its clock is running; the rhythm changes only when you change it here.</p>' +
      '<canvas class="rl-mstrip" role="img" aria-label="Preview of the display rhythm"></canvas>';
    host.appendChild(disp);
    var prev = Strip($(".rl-mstrip", disp));
    function send() {
      monState = { rhythm: $(".rl-d-r", disp).value, rate: +$(".rl-d-rate", disp).value || 72, hr: $(".rl-d-hr", disp).value, bp: $(".rl-d-bp", disp).value, spo2: $(".rl-d-sp", disp).value, label: $(".rl-d-lab", disp).value, showLabel: $(".rl-d-showlab", disp).checked, defib: $(".rl-d-defib", disp).checked };
      prev.set(monState.rhythm, monState.rate, true); store("rcm-resus-display", monState); if (CH) CH.postMessage(monState);
    }
    $(".rl-d-send", disp).addEventListener("click", send);
    // typical teaching values per rhythm (simulation defaults, not clinical targets); "—" = no reading
    var PRESET = {
      normal:    [72, "72", "128/76", "97", "Sinus rhythm"],
      svt:       [180, "180", "104/68", "96", "Narrow complex tachycardia (SVT)"],
      irregular: [130, "118", "112/70", "95", "Atrial fibrillation, rapid"],
      wide:      [170, "170", "86/54", "93", "Wide complex tachycardia (VT with a pulse)"],
      peaked:    [66, "66", "122/74", "96", "Peaked T waves (high potassium)"],
      sine:      [48, "48", "76/40", "88", "Sine wave (severe high potassium)"],
      pea:       [46, "—", "—", "—", "PEA: organized rhythm, no pulse"],
      longqt:    [58, "58", "118/70", "97", "Sinus rhythm, long QT"],
      torsades:  [240, "—", "—", "—", "Torsades de pointes (polymorphic VT)"],
      vf:        [300, "—", "—", "—", "Ventricular fibrillation"],
      asystole:  ["", "—", "—", "—", "Asystole"]
    };
    $(".rl-d-r", disp).addEventListener("change", function () {
      var v = PRESET[this.value]; if (!v) return;
      $(".rl-d-rate", disp).value = v[0]; $(".rl-d-hr", disp).value = v[1]; $(".rl-d-bp", disp).value = v[2];
      $(".rl-d-sp", disp).value = v[3]; $(".rl-d-lab", disp).value = v[4];
      prev.set(this.value, +v[0] || 72, true);   // preview only; the shared display waits for Update display
    });
    $(".rl-d-defib", disp).addEventListener("change", send);
    $(".rl-d-showlab", disp).addEventListener("change", function () {   // changes only the label's visibility, not unsent values
      var cur = store("rcm-resus-display") || monState; cur.showLabel = this.checked; monState.showLabel = this.checked;
      store("rcm-resus-display", cur); if (CH) CH.postMessage(cur);
    });
    var saved = store("rcm-resus-display"); if (saved && saved.defib) $(".rl-d-defib", disp).checked = true;
    if (saved && saved.showLabel === false) $(".rl-d-showlab", disp).checked = false;
    var lastShock = 0;
    function fromDisplay(m) {   // a shock on the display goes into the drill log while the clock runs
      if (!m || m.type !== "defib" || m.ev !== "shock" || !start || m.t === lastShock) return;
      lastShock = m.t;
      log.push({ t: now(), ev: "shock" }); render();
    }
    if (CH) CH.addEventListener("message", function (e) { fromDisplay(e.data); });
    window.addEventListener("storage", function (e) { if (e.key === "rcm-resus-defib") fromDisplay(store("rcm-resus-defib")); });
    setTimeout(function () { prev.set("normal", 72, true); }, 0);
    function now() { return start ? (Date.now() - start) / 1000 : 0; }
    function render() {
      $(".rl-log", rec).innerHTML = log.map(function (l) { return "<li><b>" + mmss(l.t) + "</b> " + l.ev + "</li>"; }).join("");
      $(".rl-sum", rec).innerHTML = summary();
    }
    function summary() {
      if (!log.length) return "";
      function first(e) { for (var i = 0; i < log.length; i++) if (log[i].ev === e) return log[i].t; return null; }
      var t0 = first("recognition"); if (t0 === null) t0 = 0;
      var cs = first("compressions start"), endT = (first("ROSC") !== null ? first("ROSC") : (first("end") !== null ? first("end") : log[log.length - 1].t));
      var on = 0, run = null, pauses = [], pFrom = null;
      log.forEach(function (l) {
        if (cs === null || l.t < cs || l.t > endT) return;
        if (l.ev === "compressions start" && run === null) { if (pFrom !== null) pauses.push(l.t - pFrom); run = l.t; pFrom = null; }
        else if (l.ev === "compressions stop" && run !== null) { on += l.t - run; run = null; pFrom = l.t; }
      });
      if (run !== null) on += endT - run;
      var win = cs === null ? 0 : endT - cs, epi = log.filter(function (l) { return l.ev === "epinephrine"; }).map(function (l) { return l.t; });
      function r(x) { return x === null ? "&mdash;" : mmss(x - t0); }
      return "<p>First compression <b>" + r(cs) + "</b> &middot; pads <b>" + r(first("pads on")) + "</b> &middot; first shock <b>" + r(first("shock")) + "</b> &middot; first epinephrine <b>" + r(epi.length ? epi[0] : null) + "</b> &middot; fluid removal off <b>" + r(first("circuit stopped")) + "</b></p>" +
        "<p>Compression fraction " + (win > 0 ? "<b>" + Math.round(100 * on / win) + "%</b>" : "&mdash;") + " &middot; longest pause <b>" + (pauses.length ? Math.round(Math.max.apply(null, pauses)) : 0) + " s</b>" +
        (epi.length > 1 ? " &middot; epinephrine intervals " + epi.slice(1).map(function (t, i) { return mmss(t - epi[i]); }).join(", ") : "") + "</p>";
    }
    $(".rl-start", rec).addEventListener("click", function () {
      if (start) return; start = Date.now(); this.textContent = "Clock running";
      tick = setInterval(function () { $(".rl-clock", rec).textContent = mmss(now()); }, 500);
    });
    Array.prototype.forEach.call(rec.querySelectorAll(".rl-ev"), function (b) {
      b.addEventListener("click", function () {
        if (!start) { start = Date.now(); $(".rl-start", rec).textContent = "Clock running"; tick = setInterval(function () { $(".rl-clock", rec).textContent = mmss(now()); }, 500); }
        log.push({ t: now(), ev: b.dataset.ev }); render();
      });
    });
    $(".rl-undo", rec).addEventListener("click", function () { log.pop(); render(); });
    $(".rl-reset", rec).addEventListener("click", function () { log = []; start = 0; clearInterval(tick); $(".rl-clock", rec).textContent = "0:00"; $(".rl-start", rec).textContent = "Start clock"; render(); });
    $(".rl-copy", rec).addEventListener("click", function () {
      var txt = log.map(function (l) { return mmss(l.t).padStart(5, "0") + " " + l.ev; }).join("\n"), btn = this;
      function done() { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy log"; }, 1500); }
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(done, function () { window.prompt("Copy the log:", txt); }); else window.prompt("Copy the log:", txt);
    });
    host._sample = function () {   // sample case: a finished drill log (fictional), so the summary shows what a debrief starts from
      var R = ["AM", "JD", "KL", "BS", "PR", "CN", "RT", "LV", "EG"];
      Array.prototype.forEach.call(roles.querySelectorAll("input[data-role]"), function (inp, i) { inp.value = R[i] || ""; });
      var L = [[0, "recognition"], [15, "compressions start"], [25, "circuit stopped"], [40, "pads on"], [43, "compressions stop"], [45, "rhythm check"],
        [50, "shock"], [53, "compressions start"], [150, "leader handover"], [173, "compressions stop"], [175, "rhythm check"], [179, "shock"],
        [181, "compressions start"], [200, "epinephrine"], [240, "airway"], [301, "compressions stop"], [303, "rhythm check"], [310, "ROSC"], [570, "handover"], [585, "end"]];
      clearInterval(tick); start = Date.now() - 585000;
      log = L.map(function (x) { return { t: x[0], ev: x[1] }; }); render();
      $(".rl-clock", rec).textContent = "9:45"; $(".rl-start", rec).textContent = "Sample loaded";
      var note = $(".rl-sample-note", rec);
      if (!note) { note = el("p", "rl-note rl-sample-note"); $(".rl-sum", rec).parentNode.insertBefore(note, $(".rl-sum", rec)); }
      note.innerHTML = "<b>Worked sample drill (fictional): collapse at Station 7.</b> The recorder tapped twenty actions. How the facilitator reads the summary below in the debrief:" +
        "<ul><li><b>What went well:</b> compressions at 0:15 while the circuit nurse stopped fluid removal at 0:25; pads at 0:40 and the first shock at 0:50; compressions restarted within 3 seconds of each shock; epinephrine at 3:20, after the second shock.</li>" +
        "<li><b>Compression fraction 91%:</b> above the guideline&rsquo;s 60% floor, which is a floor, not a goal.</li>" +
        "<li><b>To improve:</b> the longest pause, 10 seconds around the first shock, sits at the limit; the course asks for pauses under 10 seconds. Charge the defibrillator during compressions so the pause holds only the rhythm check and the shock.</li>" +
        "<li><b>Then:</b> the physician-on-duty took over leadership at 2:30, pulse returned (ROSC) at 5:10, and the patient was handed over at 9:30.</li></ul>" +
        "Copy the log into the timeline analyzer for the written debrief, then press <b>Reset</b> to record your own drill.";
      $(".rl-d-r", disp).value = "vf"; $(".rl-d-rate", disp).value = 300; $(".rl-d-hr", disp).value = "—"; $(".rl-d-bp", disp).value = "—"; $(".rl-d-sp", disp).value = "—";
      $(".rl-d-lab", disp).value = "Ventricular fibrillation"; send();
      rec.scrollIntoView({ behavior: "smooth", block: "start" });
    };
    $(".rl-reset", rec).addEventListener("click", function () { var n = $(".rl-sample-note", rec); if (n) n.remove(); });
    $(".rl-cards", roles).addEventListener("click", function () { printCards(); });
  }

  /* ════════════ 4. Role rotation planner + 5. role cards ════════════ */
  var ROT_ROLES = [["Leader", "lead"], ["Defibrillator and drugs", "drugs"], ["Circuit nurse", "nurse"], ["Airway", "nurse"], ["Watcher", "nurse"],
    ["Compressor 1", "all"], ["Compressor 2", "all"], ["Recorder and timer", "all"], ["Runner", "all"]];
  var SHOW = ["Leader", "Compressor 1", "Compressor 2", "Airway", "Defibrillator and drugs", "Circuit nurse", "Recorder and timer", "Watcher", "Runner"];
  function initials(v) { var seen = {}; return String(v || "").split(/[,;\s]+/).map(function (x) { return x.trim().toUpperCase().slice(0, 8); }).filter(function (x) { if (!x || seen[x]) return false; seen[x] = 1; return true; }); }
  // fill order and weight: what a small team keeps when roles must combine (Module 13: leader + drugs, compressor + airway, circuit + recorder; the watcher is never combined)
  var FILL = { "Leader": 1000, "Compressor 1": 900, "Watcher": 850, "Circuit nurse": 800, "Defibrillator and drugs": 500, "Compressor 2": 400, "Recorder and timer": 300, "Airway": 250, "Runner": 200 };
  function plan(all, lead, drugs, nurse, drills) {
    var el2 = { all: all, lead: lead.length ? lead : all, drugs: drugs.length ? drugs : (lead.length ? lead : all), nurse: nurse.length ? nurse : all };
    var full = all.length >= ROT_ROLES.length;
    // enough people: fill the scarcest roles first so every role is filled; too few: keep what a small team keeps
    var order = ROT_ROLES.slice().sort(function (x, y) { return full ? (el2[x[1]].length - el2[y[1]].length) || (FILL[y[0]] - FILL[x[0]]) : FILL[y[0]] - FILL[x[0]]; });
    var cnt = {}, last = {}, out = [];
    all.forEach(function (p) { cnt[p] = {}; last[p] = null; });
    function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
    for (var d = 0; d < drills; d++) {
      var R = rng(1009 * (d + 1) + all.length * 31), best = null, bestS = -1e9;
      for (var trial = 0; trial < 300; trial++) {
        var used = {}, row = {}, sc = 0, jit = trial ? 6 : 0;
        order.forEach(function (rr) {
          var role = rr[0], pick = null, ps = -1e9;
          var free = el2[rr[1]].filter(function (p) { return !used[p]; });
          if (trial && free.length && R() < 0.35) { pick = free[Math.floor(R() * free.length)]; ps = (cnt[pick][role] ? 0 : 12) - 3 * (cnt[pick][role] || 0) - (last[pick] === role ? 9 : 0); }
          else free.forEach(function (p) {
            var v = (cnt[p][role] ? 0 : 12) - 3 * (cnt[p][role] || 0) - (last[p] === role ? 9 : 0) + R() * jit;
            if (v > ps) { ps = v; pick = p; }
          });
          if (pick) { used[pick] = 1; row[role] = pick; sc += FILL[role] + ps; } else row[role] = null;
        });
        if (sc > bestS) { bestS = sc; best = row; }
      }
      all.forEach(function (p) { last[p] = null; });
      Object.keys(best).forEach(function (r) { var p = best[r]; if (p) { cnt[p][r] = (cnt[p][r] || 0) + 1; last[p] = r; } });
      out.push(best);
    }
    var cov = all.map(function (p) {
      var scope = ROT_ROLES.filter(function (rr) { return el2[rr[1]].indexOf(p) >= 0; }).map(function (rr) { return rr[0]; });
      return { p: p, scope: scope, held: scope.filter(function (r) { return cnt[p][r]; }), not: scope.filter(function (r) { return !cnt[p][r]; }) };
    });
    return { rows: out, cov: cov };
  }
  function Rotation(host) {
    var KEY = "rcm-resus-rotation", st = store(KEY) || {};
    host.innerHTML = "";
    var box = el("div", "rl-card");
    box.innerHTML = '<div class="rl-rot-in">' +
      '<label>Everyone in the drills (initials)<input type="text" class="rr-all" placeholder="e.g. AM, JD, KL, BS, PR, CN, RT, LV, EG"></label>' +
      '<label>Who may lead (unit protocol)<input type="text" class="rr-lead" placeholder="e.g. AM, PR"></label>' +
      '<label>Medicines and manual defibrillator (ACLS-current)<input type="text" class="rr-drugs" placeholder="e.g. AM, PR, CN"></label>' +
      '<label>Nurses and physicians (airway, circuit, watcher)<input type="text" class="rr-nurse" placeholder="e.g. AM, PR, CN, LV, KL"></label>' +
      '<label>Number of drills<input type="number" class="rr-n" min="1" max="24" value="6"></label></div>' +
      '<div class="rl-rbar"><button type="button" class="rl-btn rr-go">Build the rotation</button> <button type="button" class="rl-btn rl-ghost rr-demo">Try a sample team</button> <button type="button" class="rl-btn rl-ghost rr-print">Print the rotation</button></div>' +
      '<p class="rl-note">Initials only; they stay on this device. A blank scope box means everyone may hold those roles. Everyone in the drills is assumed BLS-trained.</p><div class="rr-out" aria-live="polite"></div>';
    host.appendChild(box);
    var f = { all: $(".rr-all", box), lead: $(".rr-lead", box), drugs: $(".rr-drugs", box), nurse: $(".rr-nurse", box), n: $(".rr-n", box) }, out = $(".rr-out", box), res = null;
    Object.keys(f).forEach(function (k) { if (st[k] != null) f[k].value = st[k]; });
    function build() {
      var all = initials(f.all.value), n = Math.max(1, Math.min(24, parseInt(f.n.value, 10) || 6));
      var keep = {}; Object.keys(f).forEach(function (k) { keep[k] = f[k].value; }); store(KEY, keep);
      if (all.length < 2) { out.innerHTML = '<p class="rl-verdict no">Enter at least two people.</p>'; return; }
      var bad = [];
      ["lead", "drugs", "nurse"].forEach(function (k) { initials(f[k].value).forEach(function (p) { if (all.indexOf(p) < 0) bad.push(p); }); });
      res = plan(all, initials(f.lead.value).filter(function (p) { return all.indexOf(p) >= 0; }), initials(f.drugs.value).filter(function (p) { return all.indexOf(p) >= 0; }),
        initials(f.nurse.value).filter(function (p) { return all.indexOf(p) >= 0; }), n);
      var h = (bad.length ? '<p class="rl-verdict no">Not in the drill list, so left out: ' + bad.join(", ") + ".</p>" : "") +
        (all.length < SHOW.length ? '<p class="rl-note">' + all.length + " people for " + SHOW.length + " roles: the roles marked &ldquo;combine&rdquo; are combined as in Module 13 (for example compressor 2 with airway, the recorder with the runner). The watcher is filled early, because the watcher is never combined with the arrest.</p>" : "") +
        '<div class="rl-rot-wrap"><table class="rl-rot-t"><thead><tr><th>Drill</th>' + SHOW.map(function (r) { return "<th>" + r + "</th>"; }).join("") + "</tr></thead><tbody>" +
        res.rows.map(function (row, i) { return '<tr data-i="' + i + '"><td><b>' + (i + 1) + "</b></td>" + SHOW.map(function (r) { return row[r] ? "<td>" + row[r] + "</td>" : '<td class="cmb">combine</td>'; }).join("") + "</tr>"; }).join("") +
        "</tbody></table></div>" +
        '<div class="rl-rbar"><label class="rl-lab">Drill <select class="rr-pick">' + res.rows.map(function (_, i) { return '<option value="' + i + '">' + (i + 1) + "</option>"; }).join("") + "</select></label>" +
        ' <button type="button" class="rl-btn rr-send">Send these roles to the recorder</button></div>' +
        "<h4>Coverage after " + n + " drill" + (n > 1 ? "s" : "") + "</h4><ul class=\"rl-cov\">" + res.cov.map(function (c) {
          return "<li><b>" + c.p + "</b>: " + c.held.length + " of " + c.scope.length + " roles in scope" + (c.not.length ? "; not yet: " + c.not.join(", ") : "; every role in scope practiced") + ".</li>";
        }).join("") + "</ul>" + (res.cov.some(function (c) { return c.not.length; }) ? '<p class="rl-note">Not everyone can hold every role in ' + n + " drill" + (n > 1 ? "s" : "") + ": each person holds one role per drill. Extend the series (for example one drill a month for a year) and the planner keeps filling the gaps.</p>" : "");
      out.innerHTML = h;
      var pick = $(".rr-pick", out);
      function mark() { Array.prototype.forEach.call(out.querySelectorAll("tbody tr"), function (tr) { tr.classList.toggle("sel", tr.getAttribute("data-i") === pick.value); }); }
      pick.addEventListener("change", mark); mark();
      $(".rr-send", out).addEventListener("click", function () {
        var row = res.rows[+pick.value];
        Array.prototype.forEach.call(document.querySelectorAll("#rl-recorder input[data-role]"), function (inp) {
          var r = inp.getAttribute("data-role"); inp.value = row[r] || "";
        });
        var fr = document.getElementById("facilitator"); if (fr) fr.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
    $(".rr-go", box).addEventListener("click", build);
    $(".rr-demo", box).addEventListener("click", function () {
      f.all.value = "AM, JD, KL, BS, PR, CN, RT, LV, EG"; f.lead.value = "AM, PR"; f.drugs.value = "AM, PR, CN"; f.nurse.value = "AM, PR, CN, LV, KL"; f.n.value = 6; build();
    });
    $(".rr-print", box).addEventListener("click", function () { if (!res) build(); document.body.classList.add("rl-print-rot"); window.print(); setTimeout(function () { document.body.classList.remove("rl-print-rot"); }, 500); });
    if (st.all) build();
  }
  function printCards() {
    var v = {};
    Array.prototype.forEach.call(document.querySelectorAll("#rl-recorder input[data-role]"), function (inp) { v[inp.getAttribute("data-role")] = inp.value.trim(); });
    Array.prototype.forEach.call(document.querySelectorAll(".rl-rc"), function (c) {
      var r = c.getAttribute("data-role"), b = c.querySelector("[data-held]"); if (!b) return;
      var t = r === "Compressors 1 and 2" ? [v["Compressor 1"], v["Compressor 2"]].filter(Boolean).join(" / ") : (/^Everyone/.test(r) ? "All" : v[r]);
      b.innerHTML = t ? t.replace(/[<>&]/g, "") : "&nbsp;";
    });
    document.body.classList.add("rl-print-rc"); window.print(); setTimeout(function () { document.body.classList.remove("rl-print-rc"); }, 500);
  }

  function DisplayMode() {
    document.body.classList.add("rl-display-mode");
    var ENERGY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 70, 85, 100, 120, 150, 170, 200, 300, 360];
    var wrap = el("div", "rl-display rl-mon2");
    wrap.innerHTML =
      '<div class="m-top"><span class="m-lab"></span><span class="m-alarm" role="status" aria-live="assertive"></span><span class="m-clock"></span>' +
      '<button type="button" class="m-tap" hidden>Tap for sound</button><button type="button" class="m-beep" title="Beep source: QRS (ECG), pulse oximeter, or off"></button><button type="button" class="m-fs">Full screen</button></div>' +
      '<div class="m-main"><div class="m-waves"><div class="m-ecg"><span class="m-lead">II &nbsp;&times;1</span><canvas class="rl-dstrip"></canvas></div>' +
        '<div class="m-ecg m-pl"><span class="m-lead">Pleth</span><span class="m-plno" hidden>NO PULSE</span><canvas class="rl-dpleth" role="img" aria-label="Pulse oximeter waveform"></canvas></div></div>' +
      '<div class="m-par">' +
        '<div class="m-box m-hr"><span class="m-k">HR <small>bpm</small></span><b class="m-v"></b><span class="m-lim">50 &ndash; 120</span></div>' +
        '<div class="m-box m-sp"><span class="m-k">SpO&#8322; <small>%</small></span><b class="m-v"></b><span class="m-sub">PR <i class="m-pr"></i></span></div>' +
        '<div class="m-box m-bp"><span class="m-k">NIBP <small>mmHg</small></span><b class="m-v"></b><span class="m-sub m-map"></span></div>' +
      '</div></div>' +
      '<div class="m-defib" hidden><div class="m-dstat">Defibrillator &middot; <b class="m-dst">READY</b></div>' +
        '<label>Energy <select class="m-j">' + ENERGY.map(function (j) { return '<option value="' + j + '"' + (j === 150 ? " selected" : "") + ">" + j + " J</option>"; }).join("") + "</select></label>" +
        '<button type="button" class="m-b m-sync" aria-pressed="false">Sync</button><button type="button" class="m-b m-charge">Charge</button>' +
        '<button type="button" class="m-b m-shock" disabled>Shock</button><button type="button" class="m-b m-disarm" disabled>Disarm</button>' +
        '<span class="m-count"></span><button type="button" class="m-b m-snd" aria-pressed="true">Sound on</button></div>' +
      '<p class="m-note">Training display &middot; not a medical device &middot; alarm limits are simulation defaults</p>';
    document.body.appendChild(wrap);
    var strip = Strip($(".rl-dstrip", wrap), $(".rl-dpleth", wrap)), cur = {}, flash = !(REDUCED || epaper());
    // clock
    function clock() { var d = new Date(); $(".m-clock", wrap).textContent = d.toLocaleTimeString("en-US", { hour: "numeric", minute: "2-digit" }); }
    clock(); setInterval(clock, 10000);
    // full screen (Fullscreen API; iPhone Safari has none: open from the Schola app instead)
    var fsb = $(".m-fs", wrap), root = document.documentElement;
    var canFS = !!(root.requestFullscreen || root.webkitRequestFullscreen);
    function isFS() { return !!(document.fullscreenElement || document.webkitFullscreenElement); }
    function toggleFS() {
      if (!canFS) { fsb.textContent = "Use the Schola app for full screen"; return; }
      if (isFS()) { (document.exitFullscreen || document.webkitExitFullscreen).call(document); return; }
      var p = (root.requestFullscreen || root.webkitRequestFullscreen).call(root, { navigationUI: "hide" });
      if (p && p.catch) p.catch(function () {});
      try { if (screen.orientation && screen.orientation.lock) screen.orientation.lock("landscape").catch(function () {}); } catch (e) {}
    }
    function fsLabel() { fsb.textContent = isFS() ? "Exit full screen" : "Full screen"; wrap.classList.toggle("m-isfs", isFS()); }
    fsb.addEventListener("click", toggleFS);
    document.addEventListener("fullscreenchange", fsLabel); document.addEventListener("webkitfullscreenchange", fsLabel);
    document.addEventListener("keydown", function (e) { if ((e.key === "f" || e.key === "F") && !(e.target.closest && e.target.closest("select, input"))) toggleFS(); });
    if (!canFS && navigator.standalone) fsb.hidden = true;
    var idle = 0; document.addEventListener("pointermove", function () { wrap.classList.remove("m-idle"); clearTimeout(idle); idle = setTimeout(function () { wrap.classList.add("m-idle"); }, 4000); });
    // values and alarms
    function num(v) { var n = parseFloat(String(v).replace(/[^0-9.\-]/g, "")); return isNaN(n) ? null : n; }
    function lvl(v, lo2, lo1, hi1, hi2) { if (v === null) return ""; if (v < lo2 || v > hi2) return "red"; if (v < lo1 || v > hi1) return "yel"; return ""; }
    function setBox(cls, txt, level) { var b = $(cls, wrap); $(".m-v", b).textContent = txt; b.classList.remove("red", "yel"); if (level) b.classList.add(level); }
    function apply(m) {
      if (!m || m.type) return; cur = m;
      var showLab = m.showLabel !== false;     // the facilitator can hide the label so learners name the rhythm
      $(".m-lab", wrap).textContent = showLab ? m.label || "" : "";
      var alarms = [], arrest = m.rhythm === "vf" || m.rhythm === "asystole";
      // HR is counted from the ECG, as a monitor does
      var hr = m.rhythm === "vf" ? null : m.rhythm === "asystole" ? 0 : (+m.rate || null), hl = arrest ? "red" : lvl(hr, 40, 50, 120, 140);
      setBox(".m-hr", m.rhythm === "vf" ? "---" : hr === null ? "---" : String(hr), hl);
      if (m.rhythm === "vf") alarms.push(["red", "VFIB / VTACH"]); else if (m.rhythm === "asystole") alarms.push(["red", "ASYSTOLE"]);
      else if (m.rhythm === "torsades") alarms.push(["red", "VTACH"]);
      else if (hl) alarms.push([hl, "HR " + hr + (hr < 50 ? " LOW" : " HIGH")]);
      if (m.rhythm === "longqt") alarms.push(["yel", "QTc HIGH"]);
      else if (m.rhythm === "sine" || m.rhythm === "peaked" || m.rhythm === "wide") alarms.push(["yel", showLab && m.label ? m.label.toUpperCase() : "ARRHYTHMIA"]);
      var sp = num(m.spo2), sl = sp === null ? "yel" : lvl(sp, 85, 90, 100, 101);
      setBox(".m-sp", sp === null ? "--" : String(sp), sl);
      var pr = num(m.hr); $(".m-pr", wrap).textContent = pr === null ? "--" : String(pr);
      if (sp === null) alarms.push(["yel", "SpO₂ NO PULSE"]); else if (sl) alarms.push([sl, "SpO₂ " + sp + " LOW"]);
      var bp = String(m.bp || ""), sys = num(bp.split("/")[0]), dia = num(bp.split("/")[1]), bl = sys === null ? "yel" : lvl(sys, 80, 90, 180, 200);
      setBox(".m-bp", sys === null ? "---/---" : bp.replace(/\s/g, ""), bl);
      $(".m-map", wrap).textContent = sys !== null && dia !== null ? "MAP " + Math.round((sys + 2 * dia) / 3) : "";
      if (sys === null) alarms.push(["yel", "NIBP NO READING"]); else if (bl) alarms.push([bl, "NIBP " + sys + (sys < 90 ? " LOW" : " HIGH")]);
      // pleth: flat when there is no pulse (arrest rhythm, or SpO₂ shown as "--"); smaller when the pressure is low
      var amp = arrest || sp === null ? 0 : sys === null ? 0.8 : Math.max(0.22, Math.min(1, (sys - 30) / 90));
      strip.set(m.rhythm, m.rate, true, amp);
      $(".m-plno", wrap).hidden = !!amp;
      alarms.sort(function (a, b) { return (b[0] === "red") - (a[0] === "red"); });
      var al = $(".m-alarm", wrap); al.className = "m-alarm" + (alarms.length ? " " + alarms[0][0] : ""); al.textContent = alarms.map(function (a) { return a[1]; }).join("  ·  ");
      wrap.classList.toggle("m-flash", flash && alarms.some(function (a) { return a[0] === "red"; }));
      $(".m-defib", wrap).hidden = !m.defib;
    }
    // simulated defibrillator
    var st = "ready", shocks = 0, armT = 0, actx = null, sound = true;
    var out = null;   // a compressor before the speakers lets the loud alerts play loud without clipping
    function ac() {
      if (!actx) {
        actx = new (window.AudioContext || window.webkitAudioContext)();
        out = actx.createDynamicsCompressor(); out.threshold.value = -10; out.knee.value = 6; out.ratio.value = 8; out.attack.value = 0.002; out.release.value = 0.12;
        out.connect(actx.destination);
      }
      if (actx.state === "suspended" && actx.resume) actx.resume();
      return actx;
    }
    function tone(f, ms, vol, type, at) {
      if (!sound) return; try { var a = ac(), o = a.createOscillator(), g = a.createGain(), t0 = a.currentTime + (at || 0), t1 = t0 + ms / 1000;
        o.type = type || "sine"; o.frequency.value = f; g.gain.setValueAtTime(0.0001, t0); g.gain.exponentialRampToValueAtTime(vol || 0.06, t0 + 0.008);
        g.gain.setValueAtTime(vol || 0.06, Math.max(t0 + 0.009, t1 - 0.02)); g.gain.exponentialRampToValueAtTime(0.0001, t1);
        o.connect(g); g.connect(out); o.start(t0); o.stop(t1 + 0.01); } catch (e) {}
    }
    function burst(ms, vol) {   // the shock's discharge "thump": a band-passed noise burst
      if (!sound) return; try { var a = ac(), n = Math.round(a.sampleRate * ms / 1000), buf = a.createBuffer(1, n, a.sampleRate), d = buf.getChannelData(0);
        for (var i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 2);
        var src = a.createBufferSource(), bp = a.createBiquadFilter(), g = a.createGain(); src.buffer = buf; bp.type = "bandpass"; bp.frequency.value = 900; bp.Q.value = 0.7; g.gain.value = vol;
        src.connect(bp); bp.connect(g); g.connect(out); src.start(); } catch (e) {}
    }
    // loud cues for the two moments everyone in the room must hear
    function syncBeep(on) { if (on) { tone(1200, 90, 0.5, "square"); tone(1200, 90, 0.5, "square", 0.14); } else tone(700, 120, 0.4, "square"); }
    function shockSound() { burst(260, 1.4); tone(220, 280, 0.6, "square"); tone(880, 160, 0.35, "square", 0.02); }
    function refuseSound() { for (var k = 0; k < 3; k++) tone(330, 160, 0.55, "square", k * 0.22); }
    var dst = $(".m-dst", wrap), bCh = $(".m-charge", wrap), bSh = $(".m-shock", wrap), bDis = $(".m-disarm", wrap), sel = $(".m-j", wrap), bSy = $(".m-sync", wrap);
    function J() { return +sel.value; }
    function show(state, text) {
      st = state; dst.textContent = text; $(".m-defib", wrap).className = "m-defib m-" + state;
      bCh.disabled = state === "charging"; bSh.disabled = state !== "charged"; bDis.disabled = state !== "charged" && state !== "charging";
      $(".m-count", wrap).textContent = shocks ? "Shocks: " + shocks : "";
    }
    bSy.addEventListener("click", function () { var on = bSy.getAttribute("aria-pressed") !== "true"; bSy.setAttribute("aria-pressed", on); bSy.classList.toggle("on", on); bSy.textContent = on ? "Sync on" : "Sync"; syncBeep(on); strip.sync(on); });
    $(".m-snd", wrap).addEventListener("click", function () { sound = !sound; this.setAttribute("aria-pressed", sound); this.textContent = sound ? "Sound on" : "Sound off"; tapHint(); });
    // beep tone, as on a monitor/defibrillator: QRS beep follows the ECG (keeps beeping in PEA, silent in VF/asystole);
    // pulse beep follows the oximeter (silent without a pulse), its pitch falling as SpO₂ falls
    var BEEPS = { qrs: "Beep: QRS", pulse: "Beep: pulse ox", off: "Beep: off" }, beep = store("rcm-resus-beep") || "qrs", bb = $(".m-beep", wrap);
    if (!BEEPS[beep]) beep = "qrs";
    function beepLabel() { bb.textContent = BEEPS[beep]; bb.setAttribute("aria-label", BEEPS[beep] + ". Tap to change."); tapHint(); }
    bb.addEventListener("click", function () { beep = beep === "qrs" ? "pulse" : beep === "pulse" ? "off" : "qrs"; store("rcm-resus-beep", beep); beepLabel(); });
    var unlocked = false, tapB = $(".m-tap", wrap);
    function tapHint() { tapB.hidden = unlocked || !sound || beep === "off"; }
    function unlock() { if (unlocked) return; try { ac(); unlocked = true; } catch (e) {} tapHint(); }
    document.addEventListener("pointerdown", unlock, true); document.addEventListener("keydown", unlock, true);
    strip.on({
      qrs: function (at) { if (unlocked && beep === "qrs") tone(980, 55, 0.28, "triangle", at); },
      pulse: function (at) {
        if (!unlocked || beep !== "pulse") return;
        var sp = num(cur.spo2); if (sp === null) return;
        tone(880 * Math.pow(2, -Math.max(0, Math.min(40, 100 - sp)) / 12), 70, 0.28, "triangle", at);   // about one semitone lower per 1% below 100
      }
    });
    beepLabel();
    sel.addEventListener("change", function () { if (st === "charged" || st === "charging") { clearTimeout(armT); show("ready", "DISARMED: ENERGY CHANGED"); } });
    bCh.addEventListener("click", function () {
      clearTimeout(armT); show("charging", "CHARGING " + J() + " J");
      var k = 0, iv = setInterval(function () { tone(500 + k * 60, 90, 0.04); k++; }, 250);
      armT = setTimeout(function () {
        clearInterval(iv); show("charged", "CHARGED " + J() + " J · PRESS SHOCK"); tone(1100, 400, 0.07);
        armT = setTimeout(function () { show("ready", "DISARMED: NOT DELIVERED IN 60 S"); }, 60000);
      }, 2500);
    });
    bDis.addEventListener("click", function () { clearTimeout(armT); show("ready", "DISARMED"); });
    bSh.addEventListener("click", function () {
      if (st !== "charged") return; clearTimeout(armT);
      var syncOn = bSy.getAttribute("aria-pressed") === "true";
      if (syncOn && (cur.rhythm === "vf" || cur.rhythm === "asystole" || cur.rhythm === "torsades")) { show("charged", cur.rhythm === "torsades" ? "SYNC: R WAVES NOT RELIABLY DETECTED · SHOCK NOT DELIVERED" : "SYNC: NO R WAVE DETECTED · SHOCK NOT DELIVERED"); refuseSound(); return; }
      shocks++; strip.shock(); shockSound();
      if (flash) { wrap.classList.add("m-zap"); setTimeout(function () { wrap.classList.remove("m-zap"); }, 160); }
      show("ready", "SHOCK DELIVERED " + J() + " J" + (syncOn ? " (SYNC)" : ""));
      var msg = { type: "defib", ev: "shock", j: J(), sync: syncOn, t: Date.now() };
      if (CH) CH.postMessage(msg); store("rcm-resus-defib", msg);
    });
    show("ready", "READY");
    apply(store("rcm-resus-display") || { rhythm: "normal", rate: 72, hr: "72", bp: "128/76", spo2: "97", label: "Sinus rhythm" });
    if (CH) CH.onmessage = function (e) { apply(e.data); };
    window.addEventListener("storage", function (e) { if (e.key === "rcm-resus-display") apply(store("rcm-resus-display")); });
  }

  function init() {
    if (/[?&]display=1/.test(location.search)) { DisplayMode(); return; }
    var rec = document.getElementById("rl-rec"), mc = document.getElementById("rl-mc"), fr = document.getElementById("rl-recorder");
    var rd = json("rl-rec-data"), cd = json("rl-cases-data");
    if (rec && rd) Recognition(rec, rd);
    if (mc && cd) Megacode(mc, cd);
    if (fr) Recorder(fr);
    Sample(rd, mc, fr);
    var rot = document.getElementById("rl-rot"); if (rot) Rotation(rot);
    var pr = document.querySelector(".rl-print-rc"); if (pr) pr.addEventListener("click", printCards);
  }

  /* Sample case (#sample): a worked recognition item, then buttons that start a megacode and load a sample drill log */
  function Sample(rd, mc, fr) {
    var box = document.getElementById("rl-sample-item");
    if (box && rd) {
      var TYPE = { pick: "Choose the algorithm and first action", strip: "Rhythm strip with findings", missing: "Find the missing assessment", order: "Arrange the steps", unsafe: "Spot the unsafe action", evolve: "The patient changes" };
      var byId = {}; rd.items.forEach(function (x) { byId[x.id] = x; });
      var h = "";
      ["r01", "r11", "r28", "r30", "r35", "r41"].forEach(function (id, k) {
        var it = byId[id]; if (!it) return;
        h += '<div class="rl-sw"><div class="rl-type">Worked item ' + (k + 1) + " &middot; " + TYPE[it.type] + "</div>" + '<p class="rl-stem">' + it.stem + "</p>";
        if (it.strip) h += '<canvas class="rl-strip rl-sw-strip" data-r="' + it.strip.rhythm + '" data-rate="' + it.strip.rate + '" role="img" aria-label="Rhythm strip"></canvas><p class="rl-find"><b>At the patient:</b> ' + it.findings + "</p>";
        if (it.type === "order") {
          h += '<p class="rl-find"><b>Answer:</b> ' + it.answer.map(function (i) { return it.options[i]; }).join(" &rarr; ") + '.</p><p class="rl-why">' + it.why + "</p>";
        } else {
          h += '<ol class="rl-sopts">' + it.options.map(function (o, i) {
            var right = i === it.answer;
            return "<li" + (right ? ' class="ok"' : "") + "><b>" + o + "</b>" + (right ? (it.type === "unsafe" ? " (the unsafe one)" : " (best)") : "") + " &mdash; " + (it.why[i] || "") + "</li>";
          }).join("") + "</ol>";
        }
        if (rd.tags[it.tag]) h += '<p class="rl-tag">Common error it trains against: ' + rd.tags[it.tag] + ". Taught in Module " + it.mod + ".</p>";
        h += "</div>";
      });
      box.innerHTML = h;
      Array.prototype.forEach.call(box.querySelectorAll(".rl-sw-strip"), function (cv) { Strip(cv).set(cv.getAttribute("data-r"), +cv.getAttribute("data-rate"), false); });
    }
    Array.prototype.forEach.call(document.querySelectorAll("[data-rl-sample]"), function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-rl-sample");
        if (k === "mc" && mc && mc._start) { mc._start(b.getAttribute("data-case") || "rl05-station-7"); mc.scrollIntoView({ behavior: "smooth", block: "start" }); }
        if (k === "mcw" && mc && mc._worked) { mc._worked(b.getAttribute("data-case") || "rl05-station-7"); mc.scrollIntoView({ behavior: "smooth", block: "start" }); }
        if (k === "log" && fr && fr._sample) fr._sample();
        if (k === "rec") { var r = document.getElementById("recognition"); if (r) r.scrollIntoView({ behavior: "smooth", block: "start" }); }
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
