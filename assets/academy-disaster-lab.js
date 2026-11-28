/* Disaster Preparedness and Response: practice page tools (Renal Care Academy, Nov 28 2026, DRAFT).
   1. Tabletop simulator: injects on a clock, a recorder taps the team's actions, a timeline at the end (no individual scoring).
   2. Call-down drill timer: counts call outcomes only (no names, no numbers); share reached at 2, 6 and 24 hours.
   3. Evacuation and patient-accounting sheet: printed blank from the chair count; nothing stored.
   Data: <script type="application/json" id="dp-tt-data"> (data/academy-disaster/tabletop.json), written by
   tools/academy/apply_resus_lab.py. Fingerprinted as assets/academy-disaster-lab.<hash>.js. */
(function () {
  "use strict";
  var D;
  try { D = JSON.parse(document.getElementById("dp-tt-data").textContent); } catch (e) { return; }
  var REDUCED = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
  function btn(txt, cls, fn) { var b = el("button", "dpl-btn" + (cls ? " " + cls : ""), txt); b.type = "button"; b.addEventListener("click", fn); return b; }
  function mmss(s) { s = Math.max(0, Math.floor(s)); return (s / 60 | 0) + ":" + ("0" + s % 60).slice(-2); }
  function hm(ms) { var m = Math.floor(ms / 60000); return (m / 60 | 0) + " h " + ("0" + m % 60).slice(-2) + " min"; }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || "null"); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }

  var css = el("style"); css.id = "dpl-css";
  css.textContent = [
    ".dpl{border:1px solid var(--border);border-radius:14px;background:var(--white);padding:16px 18px;margin:12px 0;color:var(--text)}",
    ".dpl-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0}",
    ".dpl-btn{font:700 14px/1 Inter,system-ui,sans-serif;border:1px solid var(--border);background:var(--white);color:var(--text);border-radius:999px;padding:9px 14px;cursor:pointer;min-height:40px}",
    ".dpl-btn:hover{border-color:var(--teal)}.dpl-btn.pri{background:#0e4a50;border-color:#0e4a50;color:#fff}.dpl-btn.warn{border-color:#b91c1c;color:#b91c1c}",
    ".dpl-btn.on{background:#e7f3f1;border-color:#1f7a4d;color:#14532d}",
    "html[data-theme=\"dark\"] .dpl-btn.on{background:#173a2b;color:#d1fae5;border-color:#34d399}",
    "html[data-theme=\"dark\"] .dpl-btn.warn{color:#fca5a5;border-color:#fca5a5}",
    ".dpl select,.dpl input[type=number],.dpl input[type=text]{font:500 16px/1.2 Inter,system-ui,sans-serif;border:1px solid var(--border);border-radius:10px;padding:8px 10px;background:var(--white);color:var(--text)}",
    ".dpl-clock{font:800 28px/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;min-width:96px}",
    ".dpl-setting{font-size:15px;color:var(--text-mid);margin:6px 0 10px}",
    ".dpl-inj{border:1px solid var(--border);border-left:5px solid #c2410c;border-radius:12px;padding:12px 14px;margin:10px 0}",
    ".dpl-inj h4{margin:0 0 6px;font:800 13px/1.2 Inter,system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--text-mid)}",
    ".dpl-inj p{margin:0 0 8px;font-size:16px;line-height:1.45}",
    ".dpl-acts{display:flex;flex-wrap:wrap;gap:6px}",
    ".dpl-acts .dpl-btn{font-weight:600;font-size:13.5px;border-radius:10px;text-align:left;line-height:1.25}",
    ".dpl-big{position:fixed;inset:0;z-index:100020;background:#0f1e2e;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:6vw}",
    ".dpl-big b{font:800 3.2vw/1.2 Inter,system-ui,sans-serif;color:#fdba74;margin-bottom:2vw}.dpl-big span{font:700 4.4vw/1.25 Inter,system-ui,sans-serif}",
    ".dpl-big i{position:absolute;top:2vw;right:3vw;font:800 3vw/1 Inter,system-ui,sans-serif;font-style:normal}",
    ".dpl-big button{position:absolute;bottom:3vw;right:3vw}",
    ".dpl-tl{width:100%;border-collapse:collapse;font-size:14px;margin-top:10px}.dpl-tl th,.dpl-tl td{border:1px solid var(--border);padding:7px 9px;vertical-align:top;text-align:left}",
    ".dpl-tl .miss{color:#b45309}html[data-theme=\"dark\"] .dpl-tl .miss{color:#fcd34d}",
    ".dpl-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;margin:10px 0}",
    ".dpl-stat{border:1px solid var(--border);border-radius:12px;padding:10px}.dpl-stat b{display:block;font:800 22px/1.1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums}.dpl-stat span{font-size:13px;color:var(--text-mid)}",
    ".dpl-note{font-size:13.5px;color:var(--text-mid);margin:8px 0 0}",
    ".dpl-sheet table{width:100%;border-collapse:collapse;font-size:14px}.dpl-sheet th,.dpl-sheet td{border:1px solid #475569;padding:6px 8px;text-align:center}.dpl-sheet td:first-child{font-weight:700}",
    ".dpl-sheet .box{display:inline-block;width:16px;height:16px;border:1.5px solid #475569;border-radius:3px}",
    ".dpl-sheet .line{display:inline-block;min-width:200px;border-bottom:1px solid #475569;height:18px}",
    ".dpl-sheet h3{margin:0 0 6px}.dpl-sheet p{margin:4px 0;font-size:14px}",
    "@media print{body.dpl-printing *{visibility:hidden}body.dpl-printing .dpl-sheet,body.dpl-printing .dpl-sheet *{visibility:visible}body.dpl-printing .dpl-sheet{position:absolute;left:0;top:0;width:100%;border:0;padding:0}body.dpl-printing .dpl-sheet .dpl-row{display:none}}"
  ].join("\n");
  document.head.appendChild(css);

  /* ── 1. Tabletop simulator ── */
  (function tabletop() {
    var host = document.getElementById("dp-tt"); if (!host) return;
    var box = el("div", "dpl"), sel = el("select"), clock = el("span", "dpl-clock", "0:00"), auto = el("input");
    sel.setAttribute("aria-label", "Scenario");
    D.scenarios.forEach(function (s, i) { var o = el("option", null, s.title + " (Module " + s.module + ")"); o.value = i; sel.appendChild(o); });
    auto.type = "checkbox"; auto.checked = true; auto.id = "dpl-auto";
    var lab = el("label"); lab.htmlFor = "dpl-auto"; lab.appendChild(auto); lab.appendChild(document.createTextNode(" Release injects on the clock"));
    var setting = el("p", "dpl-setting"), feed = el("div"), out = el("div");
    var S = null, timer = null;
    var bStart = btn("Start", "pri", start), bNext = btn("Release next inject", "", next), bEnd = btn("End and show timeline", "warn", finish), bBig = btn("Shared display", "", big);
    var r1 = el("div", "dpl-row"); r1.appendChild(sel); r1.appendChild(lab);
    var r2 = el("div", "dpl-row"); [clock, bStart, bNext, bBig, bEnd].forEach(function (x) { r2.appendChild(x); });
    box.appendChild(r1); box.appendChild(setting); box.appendChild(r2); box.appendChild(feed); box.appendChild(out);
    box.appendChild(el("p", "dpl-note", "The facilitator reads each inject aloud; the team decides out loud; the recorder taps each action as it is said. Nothing leaves this device, and no individual is scored."));
    host.appendChild(box);
    function sc() { return D.scenarios[+sel.value]; }
    function showSetting() { setting.textContent = sc().setting + " Planned length: about " + sc().minutes + " minutes."; }
    sel.addEventListener("change", function () { if (!S) showSetting(); }); showSetting();
    function now() { return S ? (S.paused ? S.acc : S.acc + (Date.now() - S.t0) / 1000) : 0; }
    function start() {
      if (!S) { S = { sc: sc(), acc: 0, t0: Date.now(), paused: false, rel: [], log: [] }; sel.disabled = true; out.innerHTML = ""; feed.innerHTML = ""; release(); }
      else if (S.paused) { S.t0 = Date.now(); S.paused = false; }
      else { S.acc = now(); S.paused = true; }
      bStart.textContent = S.paused ? "Resume" : "Pause";
      if (!timer) timer = setInterval(tick, 500);
    }
    function tick() {
      if (!S) return; var t = now(); clock.textContent = mmss(t);
      if (auto.checked && !S.paused) { var n = S.rel.length; if (n < S.sc.injects.length && t >= S.sc.injects[n].t * 60) release(); }
      paintBig();
    }
    function next() { if (!S) { start(); return; } release(); }
    function release() {
      var n = S.rel.length; if (n >= S.sc.injects.length) return;
      var inj = S.sc.injects[n], at = now(); S.rel.push(at);
      var card = el("div", "dpl-inj"); card.appendChild(el("h4", null, "Inject " + (n + 1) + " · " + mmss(at)));
      card.appendChild(el("p", null, inj.text));
      var acts = el("div", "dpl-acts");
      inj.actions.forEach(function (a) {
        var b = btn(a, "", function () {
          if (b.classList.contains("on")) return;
          b.classList.add("on"); b.textContent = "✓ " + a + " · " + mmss(now() - at);
          S.log.push({ i: n, a: a, t: now() });
        });
        acts.appendChild(b);
      });
      var other = el("input"); other.type = "text"; other.placeholder = "Other action said (no names)"; other.setAttribute("aria-label", "Other action");
      other.addEventListener("keydown", function (e) { if (e.key === "Enter" && other.value.trim()) { S.log.push({ i: n, a: "Other: " + other.value.trim(), t: now() }); other.value = ""; other.placeholder = "Recorded. Another?"; } });
      acts.appendChild(other);
      card.appendChild(acts); feed.insertBefore(card, feed.firstChild);
      if (!REDUCED) card.scrollIntoView({ block: "nearest" });
      paintBig();
    }
    var bigEl = null;
    function big() {
      if (bigEl) { bigEl.remove(); bigEl = null; return; }
      bigEl = el("div", "dpl-big"); bigEl.setAttribute("role", "dialog"); bigEl.setAttribute("aria-label", "Shared display");
      bigEl.appendChild(el("i")); bigEl.appendChild(el("b")); bigEl.appendChild(el("span"));
      bigEl.appendChild(btn("Close", "", big));
      document.body.appendChild(bigEl); paintBig();
      document.addEventListener("keydown", function esc(e) { if (e.key === "Escape" && bigEl) { big(); document.removeEventListener("keydown", esc); } });
    }
    function paintBig() {
      if (!bigEl) return; var n = S ? S.rel.length : 0;
      bigEl.querySelector("i").textContent = mmss(now());
      bigEl.querySelector("b").textContent = n ? "Inject " + n + " of " + S.sc.injects.length : (S ? "" : sc().title);
      bigEl.querySelector("span").textContent = n ? S.sc.injects[n - 1].text : sc().setting;
    }
    function finish() {
      if (!S) return; clearInterval(timer); timer = null;
      var tb = el("table", "dpl-tl"), lines = [S.sc.title + " — tabletop timeline (exercise clock)"];
      tb.innerHTML = "<thead><tr><th>Inject</th><th>Actions recorded (time after inject)</th><th>Not recorded</th><th>Teaching point</th></tr></thead>";
      var body = el("tbody");
      S.sc.injects.forEach(function (inj, i) {
        var tr = el("tr"), relAt = S.rel[i];
        var td1 = el("td"); td1.textContent = (i + 1) + ". " + (relAt == null ? "(not released) " : mmss(relAt) + " ") + inj.text;
        var got = S.log.filter(function (l) { return l.i === i; });
        var td2 = el("td"); td2.textContent = got.length ? got.map(function (l) { return l.a + " (" + mmss(l.t - relAt) + ")"; }).join("; ") : "—";
        var said = got.map(function (l) { return l.a; });
        var miss = relAt == null ? [] : inj.actions.filter(function (a) { return said.indexOf(a) < 0; });
        var td3 = el("td", "miss"); td3.textContent = miss.length ? miss.join("; ") : "—";
        var td4 = el("td"); td4.textContent = inj.point;
        [td1, td2, td3, td4].forEach(function (x) { tr.appendChild(x); }); body.appendChild(tr);
        lines.push("", "Inject " + (i + 1) + " at " + (relAt == null ? "not released" : mmss(relAt)) + ": " + inj.text,
          "  Recorded: " + td2.textContent, "  Not recorded: " + td3.textContent, "  Teaching point: " + inj.point);
      });
      tb.appendChild(body); out.innerHTML = "";
      out.appendChild(el("h3", null, "Timeline for the hot wash")); out.appendChild(tb);
      out.appendChild(el("p", "dpl-note", "Use it to write the one-page after-action report (Module 12): objectives met or not, what worked, what failed, actions with owner and date, next rehearsal. \u201cNot recorded\u201d means the recorder did not tap it, not that the team failed: discuss it."));
      var row = el("div", "dpl-row");
      row.appendChild(btn("Copy timeline", "pri", function () {
        var txt = lines.join("\n");
        if (navigator.clipboard) navigator.clipboard.writeText(txt).then(function () { this.textContent = "Copied"; }.bind(this)); else window.prompt("Copy the timeline:", txt);
      }));
      row.appendChild(btn("New exercise", "", function () { S = null; sel.disabled = false; clock.textContent = "0:00"; feed.innerHTML = ""; out.innerHTML = ""; bStart.textContent = "Start"; showSetting(); }));
      out.appendChild(row);
    }
  })();

  /* ── 2. Call-down drill timer ── */
  (function calldown() {
    var host = document.getElementById("dp-call"); if (!host) return;
    var KEY = "rcm-dp-calldown", ST = D.callStates || ["Reached", "Message left", "No answer", "Wrong number", "Not able to come"];
    var box = el("div", "dpl"), total = el("input"), stats = el("div", "dpl-stats"), row = el("div", "dpl-row"), ctl = el("div", "dpl-row"), msg = el("p", "dpl-note");
    total.type = "number"; total.min = 1; total.max = 2000; total.placeholder = "e.g. 58"; total.setAttribute("aria-label", "Number of people on the call list");
    var r0 = el("div", "dpl-row"); var l0 = el("label", null, "People on the list "); l0.appendChild(total); r0.appendChild(l0);
    r0.appendChild(btn("Start the drill", "pri", function () {
      var n = parseInt(total.value, 10); if (!(n > 0)) { msg.textContent = "Enter how many people are on the call list."; return; }
      var s = store(KEY); if (s && !window.confirm("Start a new drill? The current counts will be cleared.")) return;
      store(KEY, { start: Date.now(), total: n, ev: [] }); paint();
    }));
    box.appendChild(r0);
    ST.forEach(function (name) { row.appendChild(btn(name, name === "Reached" ? "pri" : "", function () { var s = store(KEY); if (!s) { msg.textContent = "Start the drill first."; return; } s.ev.push([Date.now() - s.start, name]); store(KEY, s); paint(); })); });
    box.appendChild(el("p", "dpl-note", "Tap one outcome per call. Only counts and times are kept on this device: no names, no numbers."));
    box.appendChild(row); box.appendChild(stats);
    ctl.appendChild(btn("Undo last", "", function () { var s = store(KEY); if (s && s.ev.length) { s.ev.pop(); store(KEY, s); paint(); } }));
    ctl.appendChild(btn("Clear", "warn", function () { if (window.confirm("Clear this drill's counts?")) { store(KEY, null); paint(); } }));
    box.appendChild(ctl); box.appendChild(msg); host.appendChild(box);
    function stat(v, l) { var d = el("div", "dpl-stat"); d.appendChild(el("b", null, v)); d.appendChild(el("span", null, l)); return d; }
    function paint() {
      var s = store(KEY); stats.innerHTML = ""; msg.textContent = "";
      if (!s) { stats.appendChild(stat("—", "No drill running")); return; }
      total.value = s.total;
      var el_ = Date.now() - s.start, cnt = {}; ST.forEach(function (k) { cnt[k] = 0; }); s.ev.forEach(function (e) { cnt[e[1]] = (cnt[e[1]] || 0) + 1; });
      function within(h) { return s.ev.filter(function (e) { return e[1] === "Reached" && e[0] <= h * 3600000; }).length; }
      function pct(n) { return Math.round(100 * n / s.total) + "%"; }
      stats.appendChild(stat(hm(el_), "Since start"));
      stats.appendChild(stat(cnt["Reached"] + " / " + s.total, "Reached (" + pct(cnt["Reached"]) + ")"));
      [2, 6, 24].forEach(function (h) { stats.appendChild(stat(el_ >= h * 3600000 || within(h) ? pct(within(h)) : "…", "Reached within " + h + " h")); });
      stats.appendChild(stat(String(cnt["Wrong number"] || 0), "Wrong numbers to fix"));
      stats.appendChild(stat(String(cnt["No answer"] || 0), "No answer"));
      stats.appendChild(stat(String(cnt["Not able to come"] || 0), "Not able to come"));
      msg.textContent = "The 24-hour figure is your unit's own measure; no external standard is claimed. Fix every wrong number before typhoon season.";
    }
    paint(); setInterval(paint, 60000);
  })();

  /* ── 3. Evacuation and patient-accounting sheet ── */
  (function evac() {
    var host = document.getElementById("dp-evac"); if (!host) return;
    var box = el("div", "dpl dpl-sheet"), n = el("input"), area = el("div");
    n.type = "number"; n.min = 1; n.max = 60; n.value = 12; n.setAttribute("aria-label", "Number of stations");
    var r = el("div", "dpl-row"); var l = el("label", null, "Stations "); l.appendChild(n); r.appendChild(l);
    r.appendChild(btn("Make the sheet", "pri", make));
    r.appendChild(btn("Print", "", function () { if (!area.firstChild) make(); document.body.classList.add("dpl-printing"); window.print(); setTimeout(function () { document.body.classList.remove("dpl-printing"); }, 500); }));
    box.appendChild(r); box.appendChild(area); host.appendChild(box);
    function make() {
      var k = Math.max(1, Math.min(60, parseInt(n.value, 10) || 12)), h = [];
      h.push("<h3>Evacuation and patient accounting</h3>");
      h.push("<p>Date <span class=\"line\" style=\"min-width:120px\"></span> &nbsp; Shift <span class=\"line\" style=\"min-width:80px\"></span></p>");
      h.push("<p>Incident lead <span class=\"line\"></span> &nbsp; Census nurse <span class=\"line\"></span></p>");
      h.push("<p>Assembly point <span class=\"line\" style=\"min-width:320px\"></span></p>");
      h.push("<table><thead><tr><th>Station</th><th>Walks alone</th><th>Walks with help</th><th>Wheelchair</th><th>Stretcher</th><th>Assigned helper</th><th>Off by staff (time)</th><th>Out ✓</th></tr></thead><tbody>");
      for (var i = 1; i <= k; i++) h.push("<tr><td>" + i + "</td><td><span class=\"box\"></span></td><td><span class=\"box\"></span></td><td><span class=\"box\"></span></td><td><span class=\"box\"></span></td><td></td><td></td><td><span class=\"box\"></span></td></tr>");
      h.push("<tr><td>Staff</td><td colspan=\"6\" style=\"text-align:left\">Count: ____ of ____</td><td><span class=\"box\"></span></td></tr>");
      h.push("<tr><td>Visitors</td><td colspan=\"6\" style=\"text-align:left\">Count: ____ of ____</td><td><span class=\"box\"></span></td></tr></tbody></table>");
      h.push("<p>Mobility categories and helpers are set at the start of every shift. Staff take patients off with the blood rule; patients never disconnect themselves. A missing name is reported at once to the incident lead and the firefighters; nobody re-enters. This sheet is a unit record under the Data Privacy Act; it is printed blank and nothing is stored online.</p>");
      area.innerHTML = h.join("");
    }
    make();
  })();
})();
