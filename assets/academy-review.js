/* Renal Care Academy: spaced-repetition review deck (Dr. Rivero, Nov 27 2026).

   1. On every page with a self-assessment (#nc-quiz: module quizzes and final exams), after "Check answers"
      each question the learner missed is copied into a review deck on this device. A question already in
      the deck that is answered correctly again counts as a review.
   2. /academy/review-deck shows the questions that are due, one at a time (a 5-question "shift drill" or
      a full review of up to 10). A right answer moves the card up one box and pushes it further out
      (1, 3, 7, 14, 30 days); after the last box it counts as learned and leaves the deck. A wrong answer
      sends it back to box 1, due tomorrow (Leitner system).
   3. The Academy landing page shows a "due today" card when anything is due.
   4. Shift drill: the first Academy page opened in a new shift (8+ hours after the last offer) serves the five
      most overdue cards in a dialog, when any are due (Dr. Rivero, Nov 27 2026). Off switch on the deck page.

   Stored only in localStorage "rcm-review" (no account, no network), like notes and bookmarks. Edit this
   file; tools/academy/apply_review.py fingerprints it as assets/academy-review.<hash>.js. */
(function () {
  "use strict";
  var KEY = "rcm-review", DAY = 864e5, BOXES = [1, 3, 7, 14, 30], MAX_CARDS = 800;
  var DECK_URL = "/academy/review-deck";

  function load() {
    try { var d = JSON.parse(localStorage.getItem(KEY) || "null"); if (d && d.cards) return d; } catch (e) {}
    return { v: 1, cards: {}, learned: 0, log: {} };
  }
  function save(d) {
    try { localStorage.setItem(KEY, JSON.stringify(d)); return true; } catch (e) { return false; }
  }
  function today0(t) { var d = new Date(t || Date.now()); d.setHours(0, 0, 0, 0); return d.getTime(); }
  function dueAt(box) { return today0() + BOXES[Math.min(box, BOXES.length) - 1] * DAY; }
  function isDue(c) { return c.due <= today0() + DAY - 1; }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function txt(n) { return n ? (n.textContent || "").replace(/\s+/g, " ").trim() : ""; }
  function fmtDate(t) { return new Date(t).toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" }); }
  function counts(d) {
    var n = 0, due = 0, next = 0, byBox = [0, 0, 0, 0, 0];
    Object.keys(d.cards).forEach(function (k) {
      var c = d.cards[k]; n++; if (isDue(c)) due++; else if (!next || c.due < next) next = c.due;
      byBox[Math.min(c.b, 5) - 1]++;
    });
    return { n: n, due: due, next: next, byBox: byBox };
  }
  function logDay(d, right) {
    var k = new Date().toISOString().slice(0, 10), e = d.log[k] || [0, 0];
    e[0]++; if (right) e[1]++; d.log[k] = e;
    var keys = Object.keys(d.log).sort(); while (keys.length > 60) delete d.log[keys.shift()];
  }

  /* ── Shared styles (design tokens) ── */
  function css() {
    if (document.getElementById("rcm-rv-css")) return;
    var s = el("style"); s.id = "rcm-rv-css";
    s.textContent = [
      ".rcm-rv-note{margin-top:10px;font-size:14.5px;line-height:1.55;color:var(--text-mid)}",
      ".rcm-rv-note a{font-weight:600}",
      ".rcm-rv-card{border:1px solid var(--border);border-left:5px solid var(--purple);border-radius:12px;background:var(--white);padding:14px 16px;margin:16px 0;display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;justify-content:space-between}",
      ".rcm-rv-card b{font-family:Inter,system-ui,sans-serif;font-size:16px;color:var(--text)}",
      ".rcm-rv-card span{font-size:14px;color:var(--text-muted)}",
      ".rcm-rv-btn{font:inherit;font-weight:600;font-size:15px;border-radius:999px;padding:9px 18px;cursor:pointer;border:1.5px solid var(--teal);background:var(--teal);color:#fff;text-decoration:none !important;display:inline-block}",
      ".rcm-rv-btn.sec{background:transparent;color:var(--teal)}",
      ".rcm-rv-btn.warn{background:transparent;color:var(--red);border-color:var(--red)}",
      ".rcm-rv-btn[disabled]{opacity:.5;cursor:default}",
      "html[data-theme=\"dark\"] .rcm-rv-btn{background:#0e4a50;border-color:#2ba8b0;color:#fff}",
      "html[data-theme=\"dark\"] .rcm-rv-btn.sec{background:transparent;color:#7fd3d9}",
      "html[data-theme=\"dark\"] .rcm-rv-btn.warn{background:transparent;color:var(--red);border-color:var(--red)}",
      ".rcm-rv-btn:focus-visible{outline:3px solid var(--gold-light);outline-offset:2px}",
      ".rcm-rv-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:8px 0 14px}",
      ".rcm-rv-stat{border:1px solid var(--border);border-radius:12px;background:var(--white);padding:10px 12px}",
      ".rcm-rv-stat .v{font-family:Inter,system-ui,sans-serif;font-weight:800;font-size:26px;color:var(--text);font-variant-numeric:tabular-nums}",
      ".rcm-rv-stat .k{font-size:13px;color:var(--text-muted)}",
      ".rcm-rv-boxes{display:flex;gap:6px;align-items:flex-end;height:64px;margin:6px 0 4px}",
      ".rcm-rv-boxes div{flex:1;background:var(--teal-light);border:1px solid var(--border);border-radius:6px 6px 0 0;position:relative;min-height:4px}",
      ".rcm-rv-boxes div i{position:absolute;top:-18px;left:0;right:0;text-align:center;font-style:normal;font-size:12px;color:var(--text-muted)}",
      ".rcm-rv-boxl{display:flex;gap:6px;font-size:11.5px;color:var(--text-muted);text-align:center}.rcm-rv-boxl span{flex:1}",
      ".rcm-rv-acts{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}",
      ".rcm-rv-q{border:1px solid var(--border);border-radius:14px;background:var(--white);padding:16px;margin:14px 0}",
      ".rcm-rv-meta{font-size:13px;color:var(--text-muted);margin-bottom:6px}",
      ".rcm-rv-meta a{color:var(--teal)}",
      ".rcm-rv-stem{font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:17.5px;line-height:1.45;color:var(--text);margin:4px 0 12px}",
      ".rcm-rv-opts{display:grid;gap:8px}",
      ".rcm-rv-opt{text-align:left;font:inherit;font-size:15.5px;line-height:1.5;color:var(--text);background:var(--white);border:1.5px solid var(--border);border-radius:10px;padding:11px 13px;cursor:pointer}",
      ".rcm-rv-opt:hover:not([disabled]),.rcm-rv-opt:focus-visible{border-color:var(--teal);background:var(--teal-light);outline:none}",
      ".rcm-rv-opt[disabled]{cursor:default}",
      ".rcm-rv-opt.right{border-color:var(--green);background:var(--green-soft)}",
      ".rcm-rv-opt.wrong{border-color:var(--red);background:var(--red-soft)}",
      ".rcm-rv-fb{margin-top:12px;border-radius:10px;padding:11px 13px;font-size:15px;line-height:1.6;color:var(--text);background:var(--bg);border:1px solid var(--border)}",
      ".rcm-rv-fb b{display:block;margin-bottom:3px}",
      ".rcm-rv-prog{font-size:13px;color:var(--text-muted);font-variant-numeric:tabular-nums}",
      ".rcm-rv-list details{border:1px solid var(--border);border-radius:10px;background:var(--white);margin:6px 0}",
      ".rcm-rv-list summary{cursor:pointer;padding:10px 12px;font-size:14.5px;color:var(--text)}",
      ".rcm-rv-list .body{padding:0 12px 12px;font-size:14px;color:var(--text-mid)}",
      ".rcm-rv-list .tag{font-size:12px;color:var(--text-muted);margin-left:6px}",
      ".rcm-rv-empty{border:1px dashed var(--border);border-radius:12px;padding:16px;color:var(--text-mid);background:var(--white)}",
      "@media print{.rcm-rv-card,.rcm-rv-acts{display:none !important}}"
    ].join("\n");
    document.head.appendChild(s);
  }

  /* ── 1. Capture from self-assessments ── */
  function moduleTitle() { return txt(document.querySelector("h1")); }
  function trackName() {
    var a = document.querySelectorAll(".nc-bar a"); return a.length ? txt(a[a.length - 1]) : "";
  }
  function snapshot(q) {
    var leg = q.querySelector("legend"), stem = "";
    if (leg) { var c = leg.cloneNode(true), qn = c.querySelector(".nc-qn"); if (qn) qn.remove(); stem = txt(c); }
    var opts = [];
    Array.prototype.forEach.call(q.querySelectorAll(".nc-opt"), function (o) {
      if (o.classList.contains("rcm-x-none")) return;   // "No answer (time ran out)"
      var inp = o.querySelector("input"), lab = o.querySelector("label"), rat = o.querySelector(".nc-rat");
      opts.push([txt(lab), inp && inp.getAttribute("data-correct") === "1" ? 1 : 0, txt(rat)]);
    });
    return { s: stem, o: opts };
  }
  function capture(form) {
    var d = load(), missed = 0, reviewed = 0, path = location.pathname.replace(/\.html$/, "");
    var title = moduleTitle(), track = trackName(), now = Date.now();
    Array.prototype.forEach.call(form.querySelectorAll("fieldset.nc-q.nc-checked"), function (q) {
      if (q.hidden) return;
      var chosen = q.querySelector("input:checked");
      if (!chosen) return;
      var right = chosen.getAttribute("data-correct") === "1", key = path + "#q" + (q.getAttribute("data-q") || "");
      var c = d.cards[key];
      if (!right) {
        var snap = snapshot(q);
        if (!snap.s || snap.o.length < 2) return;
        if (c) { c.b = 1; c.n = (c.n || 0) + 1; c.due = dueAt(1); c.s = snap.s; c.o = snap.o; }
        else d.cards[key] = { u: path, m: title, t: track, s: snap.s, o: snap.o, b: 1, due: dueAt(1), n: 1, r: 0, a: now };
        missed++;
      } else if (c && isDue(c)) {
        promote(d, key, c); reviewed++;
      }
    });
    trim(d);
    var ok = save(d);
    return { missed: missed, reviewed: reviewed, ok: ok, d: d };
  }
  function promote(d, key, c) {
    c.r = (c.r || 0) + 1;
    if (c.b >= BOXES.length) { delete d.cards[key]; d.learned = (d.learned || 0) + 1; return "learned"; }
    c.b++; c.due = dueAt(c.b); return "up";
  }
  function trim(d) {
    var keys = Object.keys(d.cards);
    if (keys.length <= MAX_CARDS) return;
    keys.sort(function (a, b) { return d.cards[b].b - d.cards[a].b || d.cards[a].a - d.cards[b].a; });
    keys.slice(0, keys.length - MAX_CARDS).forEach(function (k) { delete d.cards[k]; });
  }
  function hookQuiz() {
    var form = document.getElementById("nc-quiz");
    if (!form) return;
    form.addEventListener("submit", function () {
      setTimeout(function () {   // let the course script grade first
        if (!form.querySelector("fieldset.nc-q.nc-checked")) return;
        var r = capture(form), res = document.getElementById("nc-result");
        if (!res || (!r.missed && !r.reviewed)) return;
        css();
        var old = res.parentNode.querySelector(".rcm-rv-note"); if (old) old.remove();
        var p = el("p", "rcm-rv-note"), c = counts(r.d), bits = [];
        if (r.missed) bits.push((r.missed === 1 ? "The question you missed was" : "The " + r.missed + " questions you missed were") + " added to your review deck. They come back tomorrow, then at longer intervals until they stick.");
        if (r.reviewed) bits.push(r.reviewed + (r.reviewed === 1 ? " deck question" : " deck questions") + " answered correctly moved up a box.");
        if (!r.ok) bits.push("(This browser could not save the deck.)");
        p.textContent = bits.join(" ") + " ";
        var a = el("a", null, "Open the review deck (" + c.n + (c.n === 1 ? " card" : " cards") + ")"); a.href = DECK_URL;
        p.appendChild(a);
        res.insertAdjacentElement("afterend", p);
      }, 0);
    });
  }

  /* ── 3. Landing page reminder ── */
  function landing() {
    if (!/^\/academy\/?(index(\.html)?)?$/.test(location.pathname)) return;
    var d = load(), c = counts(d);
    if (!c.due) return;
    css();
    var main = document.querySelector("main.container") || document.querySelector("main");
    if (!main) return;
    var box = el("div", "rcm-rv-card"), t = el("div");
    var b = el("b", null, c.due === 1 ? "1 question is due for review today" : c.due + " questions are due for review today");
    var s = el("span", null, "From the self-assessments you missed. A five-question drill takes about three minutes.");
    t.appendChild(b); t.appendChild(el("br")); t.appendChild(s);
    var a = el("a", "rcm-rv-btn", "Review now"); a.href = DECK_URL + "#drill";
    box.appendChild(t); box.appendChild(a);
    main.insertBefore(box, main.firstChild);
  }

  /* ── Drill engine (shared by the deck page and the shift pop-up) ──
     opts.onExit(msg) runs when the round ends or the learner stops; opts.exitLabel names the stop button. */
  function makeDrill(root, opts) {
    var session = null, d = load();
    function start(keys, practice) {
      d = load();
      session = { keys: keys.slice(), i: 0, right: 0, again: [], practice: !!practice, total: keys.length };
      ask();
    }
    function ask() {
      root.innerHTML = "";
      if (session.i >= session.keys.length) {
        if (session.again.length) { session.keys = session.keys.concat(session.again); session.again = []; session.retry = true; }
        else return done();
      }
      var k = session.keys[session.i], c = d.cards[k];
      if (!c) { session.i++; return ask(); }
      var q = el("div", "rcm-rv-q");
      q.appendChild(el("div", "rcm-rv-prog", (session.i < session.total ? "Question " + (session.i + 1) + " of " + session.total : "Second try") + (session.practice ? " · practice, not scored" : " · Box " + c.b)));
      var meta = el("div", "rcm-rv-meta"); meta.textContent = (c.t ? c.t + " · " : "") + c.m + " · ";
      var a = el("a", null, "open module"); a.href = c.u + "#quiz"; meta.appendChild(a); q.appendChild(meta);
      var stem = el("p", "rcm-rv-stem", c.s); stem.setAttribute("tabindex", "-1"); q.appendChild(stem);
      var box = el("div", "rcm-rv-opts"), order = c.o.map(function (o, i) { return i; });
      for (var i = order.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = order[i]; order[i] = order[j]; order[j] = t; }
      order.forEach(function (oi) {
        var b = el("button", "rcm-rv-opt", c.o[oi][0]); b.type = "button";
        b.addEventListener("click", function () { answer(k, c, oi, box, q, b); });
        box.appendChild(b);
      });
      q.appendChild(box); root.appendChild(q);
      var quit = el("button", "rcm-rv-btn sec", opts.exitLabel || "Stop and go back"); quit.type = "button";
      quit.addEventListener("click", function () { opts.onExit(session.i ? "Stopped. Your answers so far are saved." : ""); });
      var acts = el("div", "rcm-rv-acts"); acts.appendChild(quit); root.appendChild(acts);
      stem.focus({ preventScroll: true });
      if (q.getBoundingClientRect().top < 0) q.scrollIntoView({ block: "start" });
    }
    function answer(k, c, oi, box, q, btn) {
      var right = c.o[oi][1] === 1, btns = box.querySelectorAll(".rcm-rv-opt"), rat = "";
      Array.prototype.forEach.call(btns, function (b) { b.disabled = true; });
      c.o.forEach(function (o) { if (o[1]) { rat = o[2]; Array.prototype.forEach.call(btns, function (b) { if (b.textContent === o[0]) b.classList.add("right"); }); } });
      if (!right) btn.classList.add("wrong");
      var fb = el("div", "rcm-rv-fb"), head = el("b"), dd = load(), live = dd.cards[k], note = "";
      if (!session.practice && !session.retry && live) {
        if (right) { var res = promote(dd, k, live); session.right++; note = res === "learned" ? "Learned: it leaves the deck." : "Moves to box " + live.b + ", due " + fmtDate(live.due) + "."; }
        else { live.b = 1; live.n = (live.n || 0) + 1; live.due = dueAt(1); session.again.push(k); note = "Back to box 1. You will see it again at the end of this round and tomorrow."; }
        logDay(dd, right); save(dd); d = dd;
      } else if (!right && !session.retry && session.practice) { note = "Practice only: the deck is unchanged."; }
      head.textContent = (right ? "Correct. " : "Not the best answer. ") + note;
      fb.appendChild(head);
      if (rat) fb.appendChild(el("span", null, rat));
      q.appendChild(fb);
      var next = el("button", "rcm-rv-btn", "Next"); next.type = "button";
      next.addEventListener("click", function () { session.i++; ask(); });
      var acts = el("div", "rcm-rv-acts"); acts.appendChild(next); q.appendChild(acts);
      next.focus({ preventScroll: true });
    }
    function done() {
      opts.onExit(session.practice ? "Practice round finished." :
        "Round finished: " + session.right + " of " + session.total + " right on the first try.", true);
    }
    return { start: start };
  }

  /* ── 4. Shift drill pop-up ──
     The first Academy page a learner opens in a new shift (8 or more hours after the last offer) serves the five
     most overdue cards in a dialog, if any are due. "Not this shift" (or Esc) waits for the next shift. Never on a
     final examination, the deck page, while printing, or when the learner turned it off on the deck page.
     State: localStorage "rcm-review-shift" {at: last offer time, off: 1 when turned off}; kept out of the deck
     backup on purpose (it belongs to the device, not the deck). */
  var SHIFT_KEY = "rcm-review-shift", SHIFT_GAP = 8 * 36e5;
  function shiftState() { try { return JSON.parse(localStorage.getItem(SHIFT_KEY) || "{}") || {}; } catch (e) { return {}; } }
  function setShift(o) { try { localStorage.setItem(SHIFT_KEY, JSON.stringify(o)); } catch (e) {} }
  function dueKeys(d) {
    return Object.keys(d.cards).filter(function (k) { return isDue(d.cards[k]); })
      .sort(function (a, b) { return d.cards[a].due - d.cards[b].due || d.cards[a].b - d.cards[b].b; });
  }
  function shiftDrill() {
    var p = location.pathname;
    if (/final-exam|review-deck/.test(p) || /[?&]print\b/.test(location.search)) return;
    var st = shiftState(), now = Date.now();
    if (st.off || (st.at && now - st.at < SHIFT_GAP && st.at <= now)) return;
    var d = load(), keys = dueKeys(d);
    if (!keys.length) return;
    setShift({ at: now });   // claim this shift first, so another tab does not offer it too
    css(); shiftCss();
    var prev = document.activeElement;
    var scrim = el("div", "rcm-sd-scrim"), dlg = el("div", "rcm-sd");
    dlg.setAttribute("role", "dialog"); dlg.setAttribute("aria-modal", "true"); dlg.setAttribute("aria-labelledby", "rcm-sd-h");
    var head = el("div", "rcm-sd-head"), h = el("h2", null, "Start-of-shift drill"); h.id = "rcm-sd-h";
    var x = el("button", "rcm-sd-x", "×"); x.type = "button"; x.setAttribute("aria-label", "Not this shift");
    head.appendChild(h); head.appendChild(x);
    var body = el("div", "rcm-sd-body");
    dlg.appendChild(head); dlg.appendChild(body); scrim.appendChild(dlg); document.body.appendChild(scrim);
    document.documentElement.classList.add("rcm-sd-open");
    function close() {
      scrim.remove(); document.documentElement.classList.remove("rcm-sd-open");
      document.removeEventListener("keydown", onKey, true);
      if (prev && prev.focus) try { prev.focus({ preventScroll: true }); } catch (e) {}
    }
    function onKey(e) {
      if (e.key === "Escape") { e.preventDefault(); close(); return; }
      if (e.key !== "Tab") return;
      var f = dlg.querySelectorAll("button:not([disabled]),a[href],select,input");
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    document.addEventListener("keydown", onKey, true);
    x.addEventListener("click", close);
    scrim.addEventListener("click", function (e) { if (e.target === scrim) close(); });
    var n = Math.min(5, keys.length), round = keys.slice(0, n);
    function intro() {
      body.innerHTML = "";
      body.appendChild(el("p", "rcm-sd-lead", (keys.length === 1 ? "1 question you missed is" : keys.length + " questions you missed are") +
        " due for review. " + ["", "One question", "Two questions", "Three questions", "Four questions", "Five questions"][n] +
        ", about " + Math.max(1, Math.round(n * 0.6)) + (n * 0.6 < 1.5 ? " minute" : " minutes") + ", before you start."));
      var acts = el("div", "rcm-rv-acts");
      var go = el("button", "rcm-rv-btn", "Start the drill"); go.type = "button";
      var later = el("button", "rcm-rv-btn sec", "Not this shift"); later.type = "button";
      go.addEventListener("click", function () { drill.start(round); });
      later.addEventListener("click", close);
      acts.appendChild(go); acts.appendChild(later); body.appendChild(acts);
      var foot = el("p", "rcm-sd-foot");
      foot.appendChild(document.createTextNode("Served once a shift from your "));
      var a = el("a", null, "review deck"); a.href = DECK_URL; foot.appendChild(a);
      foot.appendChild(document.createTextNode(", stored only on this device. "));
      var off = el("button", "rcm-sd-link", "Stop these pop-ups"); off.type = "button";
      off.addEventListener("click", function () {
        setShift({ at: Date.now(), off: 1 });
        body.innerHTML = "";
        body.appendChild(el("p", "rcm-sd-lead", "Shift drills are off on this device. Your deck still collects missed questions; turn the drills back on from the review deck page."));
        var ok = el("button", "rcm-rv-btn", "Close"); ok.type = "button"; ok.addEventListener("click", close);
        var w = el("div", "rcm-rv-acts"); w.appendChild(ok); body.appendChild(w); ok.focus();
      });
      foot.appendChild(off);
      body.appendChild(foot);
      go.focus({ preventScroll: true });
    }
    var drill = makeDrill(body, {
      exitLabel: "Stop for now",
      onExit: function (msg, finished) {
        body.innerHTML = "";
        var left = dueKeys(load()).length;
        body.appendChild(el("p", "rcm-sd-lead", (msg || "Stopped.") + (finished && left ? " " + left + (left === 1 ? " more card is" : " more cards are") + " due today on the review deck." : "")));
        var acts = el("div", "rcm-rv-acts");
        var back = el("button", "rcm-rv-btn", /academy\/?(index(\.html)?)?$/.test(p) ? "Back to the Academy" : "Back to this page"); back.type = "button";
        back.addEventListener("click", close);
        var deck = el("a", "rcm-rv-btn sec", "Open the review deck"); deck.href = DECK_URL;
        acts.appendChild(back); acts.appendChild(deck); body.appendChild(acts);
        back.focus({ preventScroll: true });
      }
    });
    intro();
  }
  function shiftCss() {
    if (document.getElementById("rcm-sd-css")) return;
    var s = el("style"); s.id = "rcm-sd-css";
    s.textContent = [
      "html.rcm-sd-open,html.rcm-sd-open body{overflow:hidden}",
      ".rcm-sd-scrim{position:fixed;inset:0;z-index:100010;background:rgba(10,20,40,.55);display:flex;align-items:center;justify-content:center;padding:16px}",
      ".rcm-sd{background:var(--bg,#fff);color:var(--text);border-radius:16px;border-top:6px solid var(--purple,#4B3280);box-shadow:0 18px 50px rgba(0,0,0,.35);width:min(640px,100%);max-height:calc(100vh - 32px);max-height:calc(100dvh - 32px);overflow:auto;padding:4px 20px 18px}",
      ".rcm-sd-head{display:flex;align-items:center;justify-content:space-between;gap:12px;position:sticky;top:0;background:inherit;padding:12px 0 4px;z-index:1}",
      ".rcm-sd-head h2{font-family:Inter,system-ui,sans-serif;font-size:19px;margin:0;color:var(--text)}",
      ".rcm-sd-x{font:inherit;font-size:26px;line-height:1;background:none;border:0;color:var(--text-muted);cursor:pointer;padding:4px 8px;border-radius:8px}",
      ".rcm-sd-x:focus-visible,.rcm-sd-link:focus-visible{outline:3px solid var(--gold-light);outline-offset:2px}",
      ".rcm-sd-lead{font-size:16px;line-height:1.6;color:var(--text-mid);margin:8px 0 4px}",
      ".rcm-sd-foot{font-size:13.5px;color:var(--text-muted);margin:6px 0 0;line-height:1.55}",
      ".rcm-sd-foot a,.rcm-sd .rcm-rv-meta a{color:var(--teal)}",
      "html[data-theme=\"dark\"] .rcm-sd-foot a,html[data-theme=\"dark\"] .rcm-sd-link,html[data-theme=\"dark\"] .rcm-sd .rcm-rv-meta a{color:#7fd3d9}",
      ".rcm-sd-link{font:inherit;background:none;border:0;padding:0;color:var(--teal);text-decoration:underline;cursor:pointer}",
      ".rcm-sd .rcm-rv-q{margin:8px 0}",
      "@media (max-width:640px){.rcm-sd-scrim{align-items:flex-end;padding:0}.rcm-sd{border-radius:16px 16px 0 0;max-height:92vh;max-height:92dvh;padding:2px 16px 16px}}",
      "@media print{.rcm-sd-scrim{display:none !important}}"
    ].join("\n");
    document.head.appendChild(s);
  }

  /* ── 2. The review deck page ── */
  function deckPage(root) {
    css();
    var d, session = null, filter = "";
    function trackList() {
      var seen = {}; Object.keys(d.cards).forEach(function (k) { var t = d.cards[k].t || "Other"; seen[t] = (seen[t] || 0) + 1; });
      return seen;
    }
    function pool(onlyDue) {
      return Object.keys(d.cards).filter(function (k) {
        var c = d.cards[k]; return (!filter || (c.t || "Other") === filter) && (!onlyDue || isDue(c));
      }).sort(function (a, b) { return d.cards[a].due - d.cards[b].due || d.cards[a].b - d.cards[b].b; });
    }
    function home(msg) {
      d = load(); session = null; root.innerHTML = "";
      var c = counts(d), dueKeys = pool(true);
      if (msg) root.appendChild(el("p", "rcm-rv-note", msg));
      var st = el("div", "rcm-rv-stats");
      [[c.due, "Due today"], [c.n, "In your deck"], [d.learned || 0, "Learned"], [streak(), "Days reviewed (last 7)"]].forEach(function (x) {
        var b = el("div", "rcm-rv-stat"); b.appendChild(el("div", "v", String(x[0]))); b.appendChild(el("div", "k", x[1])); st.appendChild(b);
      });
      root.appendChild(st);
      if (!c.n) {
        var e = el("div", "rcm-rv-empty");
        e.innerHTML = "<b>Your deck is empty.</b> Take any module&rsquo;s self-assessment. Every question you miss is added here automatically and comes back tomorrow, then after 3, 7, 14 and 30 days, until you answer it right five times in a row.";
        root.appendChild(e);
        root.appendChild(privacy());
        return;
      }
      var tl = trackList(), names = Object.keys(tl);
      if (names.length > 1) {
        var lab = el("label", "rcm-rv-note", "Show: "), sel = el("select");
        sel.appendChild(new Option("All tracks (" + c.n + ")", ""));
        names.sort().forEach(function (n) { sel.appendChild(new Option(n + " (" + tl[n] + ")", n)); });
        sel.value = filter; sel.addEventListener("change", function () { filter = sel.value; home(); });
        sel.style.cssText = "font:inherit;padding:6px 8px;border-radius:8px;border:1px solid var(--border);background:var(--white);color:var(--text)";
        lab.appendChild(sel); root.appendChild(lab);
      }
      var acts = el("div", "rcm-rv-acts");
      var drill = el("button", "rcm-rv-btn", "Shift drill: 5 questions"); drill.type = "button"; drill.id = "drill";
      var full = el("button", "rcm-rv-btn sec", "Review all due (up to 10)"); full.type = "button";
      if (!dueKeys.length) { drill.disabled = true; full.disabled = true; }
      drill.addEventListener("click", function () { start(dueKeys.slice(0, 5)); });
      full.addEventListener("click", function () { start(dueKeys.slice(0, 10)); });
      acts.appendChild(drill); acts.appendChild(full);
      if (!dueKeys.length) {
        var early = el("button", "rcm-rv-btn sec", "Practice early (not scored)"); early.type = "button";
        early.addEventListener("click", function () { start(pool(false).slice(0, 5), true); });
        acts.appendChild(early);
        root.appendChild(el("p", "rcm-rv-note", "Nothing is due" + (filter ? " in this track" : "") + " today." + (c.next ? " The next card is due on " + fmtDate(c.next) + "." : "")));
      }
      root.appendChild(acts);
      root.appendChild(el("h3", null, "Boxes"));
      var bx = el("div", "rcm-rv-boxes"), mx = Math.max.apply(null, c.byBox.concat([1]));
      c.byBox.forEach(function (n) { var b = el("div"); b.style.height = Math.max(6, Math.round(58 * n / mx)) + "px"; var i = el("i", null, String(n)); b.appendChild(i); bx.appendChild(b); });
      root.appendChild(bx);
      var bl = el("div", "rcm-rv-boxl"); ["Box 1 · 1 day", "Box 2 · 3 days", "Box 3 · 7 days", "Box 4 · 14 days", "Box 5 · 30 days"].forEach(function (t) { bl.appendChild(el("span", null, t)); });
      root.appendChild(bl);
      root.appendChild(shiftSetting());
      root.appendChild(manage());
      root.appendChild(privacy());
      if (location.hash === "#drill" && dueKeys.length) { history.replaceState(null, "", location.pathname); start(dueKeys.slice(0, 5)); }
    }
    function streak() {
      var n = 0; for (var i = 0; i < 7; i++) { var k = new Date(Date.now() - i * DAY).toISOString().slice(0, 10); if (d.log && d.log[k]) n++; } return n;
    }
    function manage() {
      var wrap = el("div", "rcm-rv-list"), det = el("details"), sum = el("summary", null, "Manage your deck");
      det.appendChild(sum);
      var body = el("div", "body");
      pool(false).forEach(function (k) {
        var c = d.cards[k], row = el("details"), s = el("summary");
        s.textContent = c.s; var tag = el("span", "tag", "Box " + c.b + " · due " + (isDue(c) ? "today" : fmtDate(c.due))); s.appendChild(tag);
        row.appendChild(s);
        var b = el("div", "body"), from = el("p");
        from.textContent = (c.t ? c.t + " · " : "") + c.m + " ";
        var a = el("a", null, "Open module"); a.href = c.u + "#quiz"; from.appendChild(a);
        var rm = el("button", "rcm-rv-btn warn", "Remove from deck"); rm.type = "button";
        rm.addEventListener("click", function () { var dd = load(); delete dd.cards[k]; save(dd); home("Removed from your deck."); });
        b.appendChild(from); b.appendChild(rm); row.appendChild(b); body.appendChild(row);
      });
      var tools = el("div", "rcm-rv-acts");
      var exp = el("button", "rcm-rv-btn sec", "Back up deck (file)"); exp.type = "button";
      exp.addEventListener("click", function () {
        var blob = new Blob([JSON.stringify(load())], { type: "application/json" }), a = el("a");
        a.href = URL.createObjectURL(blob); a.download = "renal-care-academy-review-deck.json"; document.body.appendChild(a); a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
      });
      var imp = el("button", "rcm-rv-btn sec", "Restore from file"); imp.type = "button";
      var file = el("input"); file.type = "file"; file.accept = "application/json,.json"; file.hidden = true;
      imp.addEventListener("click", function () { file.click(); });
      file.addEventListener("change", function () {
        var f = file.files && file.files[0]; if (!f) return;
        var rd = new FileReader();
        rd.onload = function () {
          try {
            var inc = JSON.parse(rd.result), cur = load(), n = 0;
            if (!inc || !inc.cards) throw 0;
            Object.keys(inc.cards).forEach(function (k) { if (!cur.cards[k]) { cur.cards[k] = inc.cards[k]; n++; } });
            cur.learned = Math.max(cur.learned || 0, inc.learned || 0); save(cur);
            home(n + (n === 1 ? " card" : " cards") + " restored.");
          } catch (e) { home("That file is not a review deck backup."); }
        };
        rd.readAsText(f);
      });
      var clr = el("button", "rcm-rv-btn warn", "Clear the whole deck"); clr.type = "button";
      clr.addEventListener("click", function () {
        if (clr.getAttribute("data-armed")) { save({ v: 1, cards: {}, learned: 0, log: {} }); home("Your review deck was cleared."); return; }
        clr.setAttribute("data-armed", "1"); clr.textContent = "Tap again to clear every card";
        setTimeout(function () { clr.removeAttribute("data-armed"); clr.textContent = "Clear the whole deck"; }, 4000);
      });
      tools.appendChild(exp); tools.appendChild(imp); tools.appendChild(file); tools.appendChild(clr);
      body.appendChild(tools);
      det.appendChild(body); wrap.appendChild(det);
      return wrap;
    }
    function shiftSetting() {
      var st = shiftState(), lab = el("label", "rcm-rv-note"), cb = el("input");
      cb.type = "checkbox"; cb.checked = !st.off; cb.style.cssText = "margin-right:8px;width:18px;height:18px;vertical-align:-3px";
      cb.addEventListener("change", function () { var o = shiftState(); if (cb.checked) delete o.off; else o.off = 1; setShift(o); });
      lab.appendChild(cb);
      lab.appendChild(document.createTextNode("Serve a 5-question drill at the start of each shift (the first Academy page I open 8 or more hours after the last one, when cards are due)"));
      lab.style.display = "block";
      return lab;
    }
    function privacy() {
      return el("p", "rcm-rv-note", "Your deck stays in this browser on this device. Nothing is sent anywhere. On iPhone and iPad the Schola Home Screen app keeps a separate deck from Safari. Use Back up and Restore to move it.");
    }
    var drill = makeDrill(root, { onExit: function (msg) { home(msg); } });
    function start(keys, practice) { d = load(); drill.start(keys, practice); }
    home();
  }

  function init() {
    hookQuiz();
    landing();
    setTimeout(shiftDrill, 700);   // after the page's own prompts (resume, update flags) have drawn
    var root = document.getElementById("rcm-review-app");
    if (root) deckPage(root);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
