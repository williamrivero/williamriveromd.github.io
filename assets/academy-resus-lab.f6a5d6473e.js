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
    if (shape === "peaked") y += g(0.42, 0.035, 0.62); else y += g(0.44, 0.06, 0.22);
    return y;
  }
  function cont(shape, T) {
    if (shape === "asystole") return 0.012 * Math.sin(T * 4.4) + 0.006 * Math.sin(T * 23);
    var amp = 0.62 + 0.38 * Math.sin(T * 1.3);
    return amp * (0.24 * Math.sin(T * 33.3) + 0.17 * Math.sin(T * 44.6 + 1) + 0.1 * Math.sin(T * 23.2 + 2)) + 0.2;
  }
  var CONT = { vf: 1, asystole: 1 };
  function Strip(canvas) {
    var ctx = canvas.getContext && canvas.getContext("2d"), shape = "normal", hr = 70, raf = 0, x = 0, prevY = null, beatT = -1, next = 0, last = 0;
    function size() {
      var r = window.devicePixelRatio || 1, w = canvas.clientWidth || 320, h = canvas.clientHeight || 70;
      canvas.width = Math.round(w * r); canvas.height = Math.round(h * r); ctx.setTransform(r, 0, 0, r, 0, 0);
      ctx.fillStyle = "#0b1220"; ctx.fillRect(0, 0, w, h); x = 0; prevY = null; return [w, h];
    }
    function still() {
      var d = size(), w = d[0], h = d[1], rr = 60 / Math.max(25, hr), py = null;
      ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.7;
      for (var px = 0; px < w; px++) {
        var t = px / 80, k = shape === "irregular" ? (t % (rr * (0.7 + 0.6 * Math.abs(Math.sin(Math.floor(t / rr) * 7.3))))) : t % rr;
        var y = h * 0.7 - (CONT[shape] ? cont(shape, t) : wave(shape, k, hr)) * h * 0.6;
        ctx.beginPath(); ctx.moveTo(px - 1, py == null ? y : py); ctx.lineTo(px, y); ctx.stroke(); py = y;
      }
    }
    function frame(ts) {
      if (!last) last = ts; var dt = Math.min(0.05, (ts - last) / 1000); last = ts;
      var w = canvas.clientWidth, h = canvas.clientHeight, steps = Math.max(1, Math.round(dt * 80));
      for (var i = 0; i < steps; i++) {
        var now = ts / 1000 + i / 80;
        if (beatT < 0 || now >= next) { beatT = now; var rr = 60 / Math.max(25, hr); if (shape === "irregular") rr *= 0.6 + Math.random() * 0.8; next = now + rr; }
        var y = h * 0.7 - (CONT[shape] ? cont(shape, now) : wave(shape, now - beatT, hr)) * h * 0.6;
        ctx.fillStyle = "#0b1220"; ctx.fillRect(x, 0, 8, h); ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.7;
        ctx.beginPath(); ctx.moveTo(x - 1, prevY == null ? y : prevY); ctx.lineTo(x, y); ctx.stroke(); prevY = y; x++;
        if (x > w) { x = 0; prevY = null; }
      }
      raf = requestAnimationFrame(frame);
    }
    return {
      set: function (s, rate, animate) {
        if (!ctx) return; shape = s || "normal"; hr = +rate || 70;
        if (raf) { cancelAnimationFrame(raf); raf = 0; }
        if (!animate || REDUCED || epaper()) { still(); return; }
        size(); last = 0; beatT = -1; raf = requestAnimationFrame(frame);
      },
      stop: function () { if (raf) cancelAnimationFrame(raf); raf = 0; }
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
    function start(c) {
      C = c; log = []; mon = {}; clearInterval(timer); if (strip) strip.stop();
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
      var res = store("rcm-resus-mc") || {}; var prev = res[C.id] || 0; if (score > prev) { res[C.id] = score; store("rcm-resus-mc", res); }
      var h = '<div class="rl-end"><h3>' + (n.title || "End") + "</h3>" + n.text +
        '<p class="rl-score">Decisions: <b>' + score + " of " + max + "</b> points in " + mmss((Date.now() - t0) / 1000) + ". Best on this device: " + Math.max(prev, score) + " of " + max + ".</p>" +
        (harmful.length ? '<p class="rl-crit">Safety-critical choice' + (harmful.length > 1 ? "s" : "") + ": repeat this megacode until each is corrected. A high score never makes up for a safety-critical error.</p>" : "") +
        '<h4>Timeline</h4><ol class="rl-review">' + log.map(function (l) {
          var c = l.choice, g = c ? c.grade : "timeout";
          return '<li class="' + (g === "best" ? "ok" : "no") + '"><b>' + mmss(l.t) + "</b> " + l.prompt + "<br><small>" + (c ? "You chose: " + c.text + " (" + g + ", " + Math.round(l.took) + " s)" : "Time ran out") + "</small>" +
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
      '<div class="rl-roles"><label>Rhythm<select class="rl-d-r"><option value="normal">Sinus / organized</option><option value="svt">Narrow fast regular</option><option value="irregular">Irregular (AF)</option><option value="wide">Wide (VT or slow wide)</option><option value="peaked">Peaked T waves</option><option value="sine">Sine wave</option><option value="vf">Ventricular fibrillation</option><option value="asystole">Asystole</option></select></label>' +
      '<label>Electrical rate<input type="number" class="rl-d-rate" value="72" min="20" max="260"></label><label>Pulse shown<input type="text" class="rl-d-hr" value="72"></label>' +
      '<label>BP shown<input type="text" class="rl-d-bp" value="128/76"></label><label>SpO₂ shown<input type="text" class="rl-d-sp" value="97"></label><label>Label<input type="text" class="rl-d-lab" value="Sinus rhythm"></label></div>' +
      '<button type="button" class="rl-btn rl-d-send">Update display</button> <a class="rl-btn rl-ghost" href="?display=1" target="_blank" rel="noopener">Open display</a>' +
      '<canvas class="rl-mstrip" role="img" aria-label="Preview of the display rhythm"></canvas>';
    host.appendChild(disp);
    var prev = Strip($(".rl-mstrip", disp));
    function send() {
      monState = { rhythm: $(".rl-d-r", disp).value, rate: +$(".rl-d-rate", disp).value || 72, hr: $(".rl-d-hr", disp).value, bp: $(".rl-d-bp", disp).value, spo2: $(".rl-d-sp", disp).value, label: $(".rl-d-lab", disp).value };
      prev.set(monState.rhythm, monState.rate, true); store("rcm-resus-display", monState); if (CH) CH.postMessage(monState);
    }
    $(".rl-d-send", disp).addEventListener("click", send);
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
    $(".rl-cards", roles).addEventListener("click", function () { document.body.classList.add("rl-print-roles"); window.print(); setTimeout(function () { document.body.classList.remove("rl-print-roles"); }, 500); });
  }

  function DisplayMode() {
    document.body.classList.add("rl-display-mode");
    var wrap = el("div", "rl-display"); wrap.innerHTML = '<div class="rl-dgrid"><div><span>Pulse</span><b class="d-hr"></b></div><div><span>BP</span><b class="d-bp"></b></div><div><span>SpO₂</span><b class="d-sp"></b></div></div><canvas class="rl-dstrip"></canvas><div class="d-lab"></div><p class="rl-dnote">Training display. Not a medical device.</p>';
    document.body.appendChild(wrap);
    var s = Strip($(".rl-dstrip", wrap));
    function apply(m) { if (!m) return; $(".d-hr", wrap).textContent = m.hr; $(".d-bp", wrap).textContent = m.bp; $(".d-sp", wrap).textContent = m.spo2; $(".d-lab", wrap).textContent = m.label; s.set(m.rhythm, m.rate, true); }
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
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
