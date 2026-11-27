/* Renal Care Academy: interactive branching cases (Dr. Rivero, Nov 27 2026).

   Each case lives in the page as <script type="application/json" id="rcm-case-<id>"> next to an empty
   <div class="rcm-case" data-case="<id>">, both written by tools/academy/apply_cases.py from
   data/academy-cases/*.json. This script turns them into a decision-by-decision simulation:

     - a bedside monitor (time, blood pressure, pulse, oxygen, extra readings, a moving rhythm strip)
     - at each decision point, 3-4 choices; each choice is graded best / acceptable / poor / harmful
     - feedback explains the physiology; after a weaker choice the learner can try again or carry on
       and see what that choice leads to
     - the first choice at each point is scored; the end screen shows the path taken and a debrief

   Vanilla JS, no network. The only thing stored is the best score per case, on this device
   (localStorage "rcm-case:<id>"). Edit this file; apply_cases.py fingerprints it as
   assets/academy-cases.<hash>.js. */
(function () {
  "use strict";

  var GRADE = {
    best: { pts: 2, label: "Best choice", cls: "best" },
    ok: { pts: 1, label: "Acceptable, not the best", cls: "ok" },
    poor: { pts: 0, label: "Weak choice", cls: "poor" },
    harmful: { pts: 0, label: "Unsafe choice", cls: "harm" }
  };
  var REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function store(id, v) {
    try {
      if (v === undefined) return JSON.parse(localStorage.getItem("rcm-case:" + id) || "null");
      localStorage.setItem("rcm-case:" + id, JSON.stringify(v));
    } catch (e) { return null; }
  }
  var decoder = document.createElement("textarea");
  function decode(s) { if (s.indexOf("&") < 0) return s; decoder.innerHTML = s; return decoder.value; }
  function epaper() { return document.documentElement.getAttribute("data-shade") === "epaper"; }

  /* ── Styles (design tokens, so light / dim / dark / e-paper follow the page) ── */
  function css() {
    if (document.getElementById("rcm-case-css")) return;
    var s = el("style");
    s.id = "rcm-case-css";
    s.textContent = [
      ".rcm-case{border:1px solid var(--border);border-radius:14px;background:var(--white);overflow:hidden;margin:18px 0 8px;box-shadow:0 1px 3px rgba(15,23,42,.06)}",
      ".rcm-case-top{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:1px solid var(--border);background:var(--bg)}",
      ".rcm-case-top b{font-family:Inter,system-ui,sans-serif;font-size:15px;color:var(--text)}",
      ".rcm-case-step{font-size:13px;color:var(--text-muted);font-variant-numeric:tabular-nums}",
      ".rcm-case-prog{flex-basis:100%;height:4px;border-radius:2px;background:var(--border);overflow:hidden}",
      ".rcm-case-prog i{display:block;height:100%;width:0;background:var(--teal);transition:width .35s}",
      /* monitor: always a dark screen, like the real thing */
      ".rcm-mon{background:#0b1220;color:#e6edf6;padding:12px 14px 10px;font-family:Inter,system-ui,sans-serif}",
      ".rcm-mon-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(104px,1fr));gap:8px}",
      ".rcm-mon-c{background:#111b2e;border:1px solid #1f2d47;border-radius:10px;padding:7px 9px;min-height:58px;transition:background .4s}",
      ".rcm-mon-c .k{font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:#9fb0c8}",
      ".rcm-mon-c .v{font-size:22px;font-weight:700;font-variant-numeric:tabular-nums;line-height:1.15;margin-top:2px;word-break:break-word}",
      ".rcm-mon-c .v small{font-size:12px;font-weight:500;color:#9fb0c8;margin-left:3px}",
      ".rcm-mon-c.txt .v{font-size:15px;font-weight:600}",
      ".rcm-mon-c.hr .v{color:#5ee08a}.rcm-mon-c.bp .v{color:#ff8a8a}.rcm-mon-c.spo2 .v{color:#6cc8ff}",
      ".rcm-mon-c.alarm{border-color:#ff5c5c;background:#3a1218}",
      ".rcm-mon-c.alarm .v{color:#ffd2d2}",
      ".rcm-mon-c.flash{background:#24406b}",
      ".rcm-mon-strip{display:flex;align-items:center;gap:10px;margin-top:9px}",
      ".rcm-mon-strip canvas{flex:1;width:100%;height:46px;display:block;background:#0b1220;border-top:1px solid #1f2d47}",
      ".rcm-mon-strip span{font-size:11px;color:#9fb0c8;white-space:nowrap}",
      ".rcm-case-body{padding:16px 16px 18px}",
      ".rcm-case-body .rcm-scene{font-size:16px;line-height:1.65;color:var(--text)}",
      ".rcm-case-body .rcm-scene p{margin:0 0 10px}",
      ".rcm-case p.rcm-case-q,.rcm-case .rcm-fb p,.rcm-case .rcm-ill,.rcm-case .rcm-best{text-align:left !important;hyphens:manual !important}",
      ".rcm-case-q{font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:17px;color:var(--text);margin:12px 0 10px}",
      ".rcm-case ul.rcm-choices,.rcm-case ul.rcm-path{display:grid;gap:8px;margin:0 !important;padding:0 !important;list-style:none !important}",
      ".rcm-case ul.rcm-choices>li,.rcm-case ul.rcm-path>li{margin:0 !important;list-style:none !important}",
      ".rcm-case ul.rcm-choices>li::before,.rcm-case ul.rcm-path>li::before,.rcm-case ul.rcm-choices>li::marker,.rcm-case ul.rcm-path>li::marker{content:none !important;display:none !important}",
      ".rcm-choice{display:flex;gap:10px;align-items:flex-start;width:100%;text-align:left;font:inherit;font-size:15.5px;line-height:1.5;color:var(--text);background:var(--white);border:1.5px solid var(--border);border-radius:10px;padding:11px 13px;cursor:pointer;transition:border-color .15s,background .15s}",
      ".rcm-choice:hover:not([disabled]),.rcm-choice:focus-visible{border-color:var(--teal);background:var(--teal-light);outline:none}",
      ".rcm-choice .ltr{flex:0 0 26px;height:26px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;background:var(--bg);border:1px solid var(--border);color:var(--text-mid)}",
      ".rcm-choice[disabled]{cursor:default;opacity:.55}",
      ".rcm-choice.picked{opacity:1;border-width:2px}",
      ".rcm-choice.picked.best{border-color:var(--green)}.rcm-choice.picked.ok{border-color:var(--amber)}",
      ".rcm-choice.picked.poor,.rcm-choice.picked.harm{border-color:var(--red)}",
      ".rcm-fb{margin-top:12px;border-radius:10px;padding:12px 14px;border-left:5px solid;font-size:15.5px;line-height:1.6;color:var(--text)}",
      ".rcm-fb.best{background:var(--green-soft);border-color:var(--green)}",
      ".rcm-fb.ok{background:var(--amber-soft);border-color:var(--amber)}",
      ".rcm-fb.poor,.rcm-fb.harm{background:var(--red-soft);border-color:var(--red)}",
      ".rcm-fb .g{display:block;font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:13px;letter-spacing:.03em;text-transform:uppercase;margin-bottom:4px}",
      ".rcm-fb.best .g{color:var(--green)}.rcm-fb.ok .g{color:var(--amber)}.rcm-fb.poor .g,.rcm-fb.harm .g{color:var(--red)}",
      ".rcm-fb p{margin:0 0 8px}.rcm-fb p:last-child{margin:0}",
      ".rcm-fb .then{margin-top:8px;padding-top:8px;border-top:1px dashed var(--border);color:var(--text-mid)}",
      ".rcm-acts{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}",
      ".rcm-btn{font:inherit;font-weight:600;font-size:15px;border-radius:999px;padding:9px 18px;cursor:pointer;border:1.5px solid var(--teal);background:var(--teal);color:#fff}",
      ".rcm-btn.sec{background:transparent;color:var(--teal)}",
      "html[data-theme=\"dark\"] .rcm-btn{background:#0e4a50;border-color:#2ba8b0}",
      "html[data-theme=\"dark\"] .rcm-btn.sec{background:transparent;color:#7fd3d9}",
      ".rcm-btn:focus-visible{outline:3px solid var(--gold-light);outline-offset:2px}",
      ".rcm-intro-note{font-size:13.5px;color:var(--text-muted);margin-top:10px}",
      ".rcm-best{font-size:13.5px;color:var(--text-muted);margin-top:6px}",
      ".rcm-end h3{font-family:Inter,system-ui,sans-serif;font-size:20px;margin:0 0 6px;color:var(--text)}",
      ".rcm-score{display:flex;align-items:center;gap:14px;margin:6px 0 14px}",
      ".rcm-score .ring{flex:0 0 74px;height:74px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Inter,system-ui,sans-serif;font-weight:800;font-size:20px;color:var(--text);background:conic-gradient(var(--teal) calc(var(--p)*1%),var(--border) 0)}",
      ".rcm-score .ring span{background:var(--white);width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center}",
      ".rcm-case ul.rcm-path{margin:8px 0 14px !important;gap:6px}",
      ".rcm-path li{display:flex;gap:10px;align-items:flex-start;font-size:14.5px;line-height:1.5;border:1px solid var(--border);border-radius:9px;padding:8px 10px;background:var(--bg);color:var(--text)}",
      ".rcm-path .rcm-pdot{flex:0 0 auto;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.03em;border-radius:999px;padding:2px 8px;margin-top:2px;color:#fff}",
      ".rcm-path .rcm-pdot.best{background:#166534}.rcm-path .rcm-pdot.ok{background:#92400e}.rcm-path .rcm-pdot.poor,.rcm-path .rcm-pdot.harm{background:#b91c1c}",
      ".rcm-debrief{border-top:1px solid var(--border);margin-top:12px;padding-top:12px;font-size:15.5px;line-height:1.65;color:var(--text)}",
      ".rcm-debrief h4{font-family:Inter,system-ui,sans-serif;font-size:15px;margin:12px 0 4px;color:var(--text)}",
      ".rcm-debrief p{margin:0 0 8px}",
      ".rcm-debrief ul{margin:4px 0 8px 20px;padding:0}",
      ".rcm-case .rcm-ill{font-size:12.5px;color:var(--text-muted);margin:10px 0 0}",
      "@media (max-width:640px){.rcm-mon-c .v{font-size:19px}.rcm-case-body{padding:14px 12px 16px}.rcm-choice{font-size:15px}}",
      "@media print{.rcm-case-wrap{display:none !important}}"
    ].join("\n");
    document.head.appendChild(s);
  }

  /* ── Rhythm strip: a simple drawn trace whose rate follows the pulse ── */
  function Strip(canvas) {
    var ctx = canvas.getContext && canvas.getContext("2d");
    var shape = "normal", hr = 80, x = 0, last = 0, raf = 0, nextBeat = 0, beatT = -1, rnd = 1, prevY = null;
    function size() {
      var r = window.devicePixelRatio || 1, w = canvas.clientWidth || 300, h = canvas.clientHeight || 46;
      canvas.width = Math.round(w * r); canvas.height = Math.round(h * r);
      ctx.setTransform(r, 0, 0, r, 0, 0); ctx.fillStyle = "#0b1220"; ctx.fillRect(0, 0, w, h); x = 0; prevY = null;
      trace(w, h);
    }
    function trace(w, h) {
      var rr = 60 / Math.max(25, hr), py = null;
      ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.6;
      for (var px = 0; px < w; px++) {
        var k = (px / 70) % rr, y = h * 0.72 - wave(k) * h * 0.62;
        ctx.beginPath(); ctx.moveTo(px - 1, py == null ? y : py); ctx.lineTo(px, y); ctx.stroke(); py = y;
      }
    }
    // y offset (0..1, up) for time t seconds after a beat
    function wave(t) {
      var g = function (c, w, a) { return a * Math.exp(-Math.pow((t - c) / w, 2)); };
      var y = g(0.08, 0.025, 0.12);                                   // P
      if (shape === "irregular") y = 0.02 * Math.sin(t * 40);         // no P, fibrillatory baseline
      y += g(0.2, 0.012, -0.12) + g(0.22, 0.012, 0.9) + g(0.24, 0.012, -0.2); // QRS
      if (shape === "wide") y = g(0.08, 0.025, 0.1) + g(0.24, 0.045, 0.75) + g(0.32, 0.04, -0.25);
      if (shape === "peaked") y += g(0.42, 0.035, 0.62);              // tall narrow T
      else if (shape === "st") y += (t > 0.27 && t < 0.38 ? -0.12 : 0) + g(0.47, 0.06, 0.12);
      else if (shape !== "wide") y += g(0.44, 0.06, 0.22);
      return y;
    }
    function frame(ts) {
      if (!last) last = ts;
      var dt = Math.min(0.05, (ts - last) / 1000); last = ts;
      var w = canvas.clientWidth, h = canvas.clientHeight, speed = 70;  // px per second
      var steps = Math.max(1, Math.round(dt * speed));
      for (var i = 0; i < steps; i++) {
        var now = ts / 1000 + i / speed;
        if (beatT < 0 || now >= nextBeat) {
          beatT = now;
          var rr = 60 / Math.max(25, hr);
          if (shape === "irregular") { rnd = 0.6 + Math.random() * 0.8; rr *= rnd; }
          nextBeat = now + rr;
        }
        var y = h * 0.72 - wave(now - beatT) * h * 0.62;
        ctx.fillStyle = "#0b1220"; ctx.fillRect(x, 0, 8, h);
        ctx.strokeStyle = "#5ee08a"; ctx.lineWidth = 1.6; ctx.beginPath();
        ctx.moveTo(x - 1, prevY == null ? y : prevY); ctx.lineTo(x, y); ctx.stroke();
        prevY = y; x += 1;
        if (x > w) { x = 0; prevY = null; }
      }
      raf = window.requestAnimationFrame(frame);
    }
    function still() { size(); }   // reduced motion / e-paper: size() draws the trace once
    return {
      set: function (newHr, newShape) {
        if (!ctx) return;
        hr = +newHr || hr; shape = newShape || "normal";
        if (REDUCED || epaper()) { still(); return; }
        if (!raf) { size(); raf = window.requestAnimationFrame(frame); } else if (newShape) { size(); }
      },
      stop: function () { if (raf) window.cancelAnimationFrame(raf); raf = 0; },
      resize: function () { if (ctx && raf) size(); else if (ctx) still(); }
    };
  }

  /* ── One case ── */
  function Case(host, data) {
    var id = data.id, nodes = data.nodes, mon = {}, cellEls = {}, alarms = [], strip = null, monEl, body, topStep, prog, cur, path = [], scored = {};
    var decisionTotal = data.decisions || Object.keys(nodes).filter(function (k) { return nodes[k].choices; }).length;
    var MON_ORDER = data.monitorOrder || ["time", "bp", "hr", "spo2"];
    var LABELS = { time: "Time", bp: "BP", hr: "Pulse", spo2: "SpO₂", rr: "Resp", temp: "Temp", uf: "Fluid removal", pump: "Blood pump", glucose: "Glucose", ecg: "ECG", k: "Potassium", line: "Venous line" };
    var UNITS = { bp: "mm Hg", hr: "/min", spo2: "%", rr: "/min", temp: "°C" };

    function alarm(k, v) {
      var n = parseFloat(String(v));
      if (k === "bp") return n && n < 90 || n >= 180;
      if (k === "hr") return n && (n < 50 || n > 120);
      if (k === "spo2") return n && n < 92;
      return false;
    }
    function renderMonitor(vals, first) {
      if (vals.alarm) alarms = vals.alarm.slice();
      for (var k in vals) if (Object.prototype.hasOwnProperty.call(vals, k)) {
        if (k === "rhythm" || k === "rhythmLabel" || k === "alarm" || k === "stripRate") continue;
        var changed = mon[k] !== undefined && mon[k] !== vals[k];
        mon[k] = vals[k];
        if (!cellEls[k]) {
          var c = el("div", "rcm-mon-c " + (/^(time|bp|hr|spo2|rr|temp)$/.test(k) ? k : "txt"));
          c.innerHTML = '<div class="k"></div><div class="v"></div>';
          c.querySelector(".k").textContent = (data.labels && data.labels[k]) || LABELS[k] || k;
          cellEls[k] = c;
          var order = MON_ORDER.indexOf(k);
          monEl.grid.appendChild(c);
          if (order >= 0) { // keep the vital signs first and in order
            var kids = Array.prototype.slice.call(monEl.grid.children);
            kids.sort(function (a, b) {
              var ka = keyOf(a), kb = keyOf(b), ia = MON_ORDER.indexOf(ka), ib = MON_ORDER.indexOf(kb);
              return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib);
            });
            kids.forEach(function (n) { monEl.grid.appendChild(n); });
          }
        }
        var v = cellEls[k].querySelector(".v");
        v.textContent = vals[k] == null ? "—" : decode(String(vals[k]));
        if (UNITS[k] && vals[k] != null && /^[0-9./ ]+$/.test(String(vals[k]))) { var sm = el("small"); sm.textContent = UNITS[k]; v.appendChild(sm); }
        cellEls[k].classList.toggle("alarm", alarm(k, vals[k]) || alarms.indexOf(k) >= 0);
        if (changed && !first && !REDUCED) flash(cellEls[k]);
      }
      if (vals.alarm) for (var a in cellEls) cellEls[a].classList.toggle("alarm", alarm(a, mon[a]) || alarms.indexOf(a) >= 0);
      if (vals.stripRate) mon.stripRate = vals.stripRate;
      if (strip && (vals.rhythm || vals.hr || vals.stripRate)) {
        mon.rhythm = vals.rhythm || mon.rhythm || "normal";
        strip.set(parseFloat(mon.hr) || parseFloat(mon.stripRate) || 80, mon.rhythm);
      }
      if (vals.rhythmLabel && monEl.rlab) monEl.rlab.textContent = vals.rhythmLabel;
    }
    function keyOf(n) { for (var k in cellEls) if (cellEls[k] === n) return k; return ""; }
    function flash(c) { c.classList.add("flash"); setTimeout(function () { c.classList.remove("flash"); }, 700); }

    function build() {
      host.innerHTML = "";
      var top = el("div", "rcm-case-top");
      var t = el("b"); t.textContent = data.title; top.appendChild(t);
      topStep = el("span", "rcm-case-step"); top.appendChild(topStep);
      prog = el("div", "rcm-case-prog"); prog.appendChild(el("i")); top.appendChild(prog);
      host.appendChild(top);
      monEl = el("div", "rcm-mon"); monEl.setAttribute("aria-label", data.monitorTitle || "Bedside monitor");
      monEl.grid = el("div", "rcm-mon-grid"); monEl.appendChild(monEl.grid);
      if (data.strip !== false) {
        var st = el("div", "rcm-mon-strip"), cv = el("canvas"); cv.setAttribute("aria-hidden", "true");
        monEl.rlab = el("span"); monEl.rlab.textContent = "Rhythm strip";
        st.appendChild(cv); st.appendChild(monEl.rlab); monEl.appendChild(st);
        strip = Strip(cv);
      }
      host.appendChild(monEl);
      body = el("div", "rcm-case-body"); body.setAttribute("aria-live", "polite");
      host.appendChild(body);
      if (strip) window.addEventListener("resize", function () { strip.resize(); });
    }

    function step(keepLabel) {
      var done = Object.keys(scored).length;
      if (!keepLabel) topStep.textContent = cur && nodes[cur] && nodes[cur].end ? "Case complete" : "Decision " + Math.min(done + 1, decisionTotal) + " of " + decisionTotal;
      prog.firstChild.style.width = Math.round(100 * done / decisionTotal) + "%";
    }

    function intro() {
      cur = null; path = []; scored = {}; mon = {}; cellEls = {}; alarms = [];
      if (strip) strip.stop();
      build();
      renderMonitor(data.monitor || {}, true);
      topStep.textContent = decisionTotal + " decisions";
      var sc = el("div", "rcm-scene", data.intro);
      body.appendChild(sc);
      if (data.illustrative !== false) body.appendChild(el("p", "rcm-ill", data.note || "Fictional patient. Values are illustrative, not targets; your unit&rsquo;s protocol and the attending nephrologist&rsquo;s orders come first."));
      var best = store(id);
      if (best && best.max) { var b = el("p", "rcm-best"); b.textContent = "Your best on this device: " + best.score + " of " + best.max + " (" + best.plays + (best.plays === 1 ? " run" : " runs") + ")."; body.appendChild(b); }
      var acts = el("div", "rcm-acts"), go = el("button", "rcm-btn", "Start the case");
      go.type = "button"; go.addEventListener("click", function () { show(data.start, true); });
      acts.appendChild(go); body.appendChild(acts);
    }

    function show(nid, focus) {
      cur = nid; var n = nodes[nid];
      if (!n) return;
      if (n.vitals) renderMonitor(n.vitals);
      body.innerHTML = "";
      if (n.end) return finish(n);
      step();
      if (n.scene) body.appendChild(el("div", "rcm-scene", n.scene));
      var q = el("p", "rcm-case-q"); q.innerHTML = n.prompt; body.appendChild(q);
      var list = el("ul", "rcm-choices"); list.setAttribute("role", "list");
      var order = n.choices.map(function (c, i) { return i; });
      if (!n.fixedOrder) for (var i = order.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var tmp = order[i]; order[i] = order[j]; order[j] = tmp; }
      order.forEach(function (ci, pos) {
        var c = n.choices[ci], li = el("li"), b = el("button", "rcm-choice");
        b.type = "button";
        b.innerHTML = '<span class="ltr" aria-hidden="true">' + "ABCDE".charAt(pos) + "</span><span></span>";
        b.lastChild.innerHTML = c.text;
        b.addEventListener("click", function () { choose(n, nid, c, b, list); });
        li.appendChild(b); list.appendChild(li);
      });
      body.appendChild(list);
      if (focus) { var hdr = host.querySelector(".rcm-case-top"); if (hdr && hdr.getBoundingClientRect().top < 0) hdr.scrollIntoView({ block: "start", behavior: REDUCED ? "auto" : "smooth" }); q.setAttribute("tabindex", "-1"); q.focus({ preventScroll: true }); }
    }

    function choose(n, nid, c, btn, list) {
      var g = GRADE[c.grade] || GRADE.poor, first = !scored[nid];
      if (first) { scored[nid] = c.grade; path.push({ node: nid, prompt: n.short || n.prompt, choice: c.text, grade: c.grade }); }
      Array.prototype.forEach.call(list.querySelectorAll(".rcm-choice"), function (x) { x.disabled = true; });
      btn.classList.add("picked", g.cls);
      if (c.vitals) renderMonitor(c.vitals);
      var fb = el("div", "rcm-fb " + g.cls);
      fb.setAttribute("role", "status");
      fb.innerHTML = '<span class="g"></span>' + c.feedback + (c.then ? '<div class="then">' + c.then + "</div>" : "");
      fb.querySelector(".g").textContent = g.label + (first ? "" : " (practice: not scored)");
      body.appendChild(fb);
      var acts = el("div", "rcm-acts");
      var nextId = c.next || n.next;
      if (c.grade !== "best" && !n.noRetry) {
        var again = el("button", "rcm-btn sec", "Try another option");
        again.type = "button";
        again.addEventListener("click", function () {
          if (c.vitals && n.vitals) renderMonitor(n.vitals);
          fb.remove(); acts.remove();
          Array.prototype.forEach.call(list.querySelectorAll(".rcm-choice"), function (x) { x.disabled = false; x.classList.remove("picked", "best", "ok", "poor", "harm"); });
          btn.disabled = true;
        });
        acts.appendChild(again);
      }
      var cont = el("button", "rcm-btn", nextId && nodes[nextId] && nodes[nextId].end ? "See how it ends" : "Continue");
      cont.type = "button";
      cont.addEventListener("click", function () { show(nextId, true); });
      acts.appendChild(cont);
      body.appendChild(acts);
      fb.setAttribute("tabindex", "-1"); fb.focus({ preventScroll: true });
      if (fb.getBoundingClientRect().bottom > window.innerHeight) fb.scrollIntoView({ block: "nearest", behavior: REDUCED ? "auto" : "smooth" });
      step(true);
    }

    function finish(n) {
      var max = Math.max(1, path.length) * 2, score = 0, harm = 0;
      path.forEach(function (p) { score += (GRADE[p.grade] || GRADE.poor).pts; if (p.grade === "harmful") harm++; });
      var pct = Math.round(100 * score / max);
      step(); prog.firstChild.style.width = "100%";
      var prev = store(id) || { plays: 0, score: -1 };
      store(id, { score: Math.max(prev.score, score), max: max, plays: (prev.plays || 0) + 1, d: new Date().toISOString().slice(0, 10) });
      var wrap = el("div", "rcm-end");
      var verdict = harm ? "An unsafe step was taken. Review it below." : pct >= 85 ? "Sound, safe management." : pct >= 60 ? "Safe, with room to sharpen." : "Several steps need another look.";
      wrap.innerHTML = '<h3></h3><div class="rcm-scene"></div><div class="rcm-score"><div class="ring" style="--p:' + pct + '"><span>' + pct + '%</span></div><div><b></b><br><span></span></div></div>';
      wrap.querySelector("h3").textContent = n.title || "How it ended";
      wrap.querySelector(".rcm-scene").innerHTML = n.text || "";
      wrap.querySelector(".rcm-score b").textContent = "Decision score: " + score + " of " + max;
      wrap.querySelector(".rcm-score > div:last-child > span").textContent = verdict;
      var h = el("p", "rcm-case-q", "Your path"); wrap.appendChild(h);
      var ul = el("ul", "rcm-path");
      path.forEach(function (p) {
        var g = GRADE[p.grade] || GRADE.poor, li = el("li");
        li.innerHTML = '<span class="rcm-pdot ' + g.cls + '"></span><span></span>';
        li.firstChild.textContent = p.grade === "best" ? "Best" : p.grade === "ok" ? "Fair" : p.grade === "harmful" ? "Unsafe" : "Weak";
        li.lastChild.innerHTML = "<b>" + strip_(p.prompt) + "</b> " + p.choice;
        ul.appendChild(li);
      });
      wrap.appendChild(ul);
      if (data.debrief) wrap.appendChild(el("div", "rcm-debrief", data.debrief));
      var acts = el("div", "rcm-acts"), again = el("button", "rcm-btn", "Run the case again"), up = el("button", "rcm-btn sec", "Back to the start of the module case");
      again.type = "button"; again.addEventListener("click", function () { intro(); var t = host.querySelector(".rcm-case-top"); if (t) t.scrollIntoView({ block: "start" }); });
      up.type = "button"; up.addEventListener("click", function () { var c = document.getElementById("case"); if (c) c.scrollIntoView({ block: "start" }); });
      acts.appendChild(again); if (document.getElementById("case")) acts.appendChild(up);
      wrap.appendChild(acts);
      body.appendChild(wrap);
      var hd = wrap.querySelector("h3"); hd.setAttribute("tabindex", "-1"); hd.focus({ preventScroll: true });
      var top = host.querySelector(".rcm-case-top"); if (top && top.getBoundingClientRect().top < 0) top.scrollIntoView({ block: "start", behavior: REDUCED ? "auto" : "smooth" });
    }
    function strip_(s) { var d = el("div"); d.innerHTML = s; return (d.textContent || "").replace(/\s+/g, " ").trim().replace(/[<>&]/g, ""); }

    intro();
  }

  function init() {
    var hosts = document.querySelectorAll(".rcm-case[data-case]");
    if (!hosts.length) return;
    css();
    Array.prototype.forEach.call(hosts, function (h) {
      var src = document.getElementById("rcm-case-" + h.getAttribute("data-case"));
      if (!src) return;
      try { Case(h, JSON.parse(src.textContent)); }
      catch (e) { h.innerHTML = '<p style="padding:14px">This interactive case could not load. Please reload the page.</p>'; }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
