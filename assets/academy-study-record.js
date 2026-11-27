/* Renal Care Academy: Personal Study Record (Dr. William Gregory Rivero, Nov 27 2026).
 *
 * A printable, one-page A4 summary a learner can hand to the head nurse or preceptor: modules finished (best module quiz
 * and the date it was passed), active time on each module page, the end-of-course examination result, and the date the
 * preceptor signed off each module's skills (or competency) checklist. It is NOT called a certificate and says so, in
 * keeping with the Academy disclaimer: self-study, not CPD units, competence is signed off on the learner's own unit.
 *
 * Two places:
 *   track hub    <script type="application/json" id="rcm-study-modules">{track, name, store, exam, modules:[[NN, title, file, skills, pass]]}</script>
 *                draws the "Personal study record" panel in #rcm-sr-app (section #study-record, written by the patcher):
 *                a module list with editable sign-off dates, a name box and "Make my study record".
 *   module page  (file name <track>-NN-*.html with a #skills or #competencies section) adds a small "Preceptor sign-off"
 *                date box at the end of that section.
 * Data (all localStorage, nothing leaves the device):
 *   rcm-cert-progress   module quiz results + _exam (academy-progress.js / academy-certificate.js), read only
 *   rcm-cert-time       active seconds per module page (academy-progress.js), read only
 *   <course store>      results the course script remembered ("Remember my result"), read only
 *   rcm-skills          { "<track>": { "NN": "YYYY-MM-DD" } }  sign-off dates typed by the learner (this script)
 * Edit this file; tools/academy/apply_study_record.py fingerprints and tags it.
 */
(function () {
  "use strict";
  var SKEY = "rcm-skills";
  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  function get(k, dflt) { try { var v = JSON.parse(localStorage.getItem(k) || "null"); return v == null ? dflt : v; } catch (e) { return dflt; } }
  function put(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function shortDate(s) { var p = String(s || "").split("-"); return p.length === 3 ? SHORT[+p[1] - 1] + " " + +p[2] + ", " + p[0] : ""; }
  function longDate(d) { return MONTHS[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear(); }
  function validDate(s) { return /^\d{4}-\d\d-\d\d$/.test(s || "") && s <= iso(new Date()) && s >= "2020-01-01"; }
  function dur(sec) {
    if (!sec) return "—";
    var m = Math.round(sec / 60); if (m < 1) return "<1 min";
    var h = Math.floor(m / 60); m = m % 60;
    return h ? h + " h " + ("0" + m).slice(-2) + " min" : m + " min";
  }
  function skills(track) { return (get(SKEY, {}) || {})[track] || {}; }
  function setSkill(track, nn, date) {
    var o = get(SKEY, {}) || {}, t = o[track] || (o[track] = {});
    if (date) t[nn] = date; else delete t[nn];
    if (!Object.keys(t).length) delete o[track];
    return put(SKEY, o);
  }

  var css = document.createElement("style");
  css.textContent = [
    ".rcm-sr-sign{margin:18px 0 0;padding:14px 16px;border:1px dashed #1a6b72;border-radius:12px;background:#f2f8f8;color:#1e2a38}",
    ".rcm-sr-sign b{font:800 15px Inter,sans-serif;color:#1a6b72}.rcm-sr-sign p{margin:4px 0 10px!important;font-size:14px;line-height:1.55;text-align:left!important;hyphens:none!important}",
    ".rcm-sr-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}",
    ".rcm-sr-row input[type=date],.rcm-sr input[type=date]{font:600 14.5px Inter,sans-serif;padding:6px 9px;border-radius:8px;border:1px solid #9aa3b2;background:#fff;color:#1e2a38}",
    ".rcm-sr-btn{font:700 14px Inter,sans-serif;padding:8px 15px;border-radius:999px;border:2px solid #1a6b72;background:#1a6b72;color:#fff;cursor:pointer}",
    ".rcm-sr-btn.ghost{background:transparent;color:#1a6b72}.rcm-sr-msg{font-size:13px;color:#2e6b3e;font-weight:700}",
    ".rcm-sr-sign a,.rcm-sr a{color:#1a6b72}",
    ".rcm-sr{border:1px solid #b9d6d8;border-radius:14px;background:#f7fbfb;padding:16px 18px;color:#1e2a38}",
    ".rcm-sr-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:0 0 14px}",
    ".rcm-sr-stat{background:#fff;border:1px solid #d6e6e7;border-radius:10px;padding:10px 12px}",
    ".rcm-sr-stat .n{font:800 22px/1.1 Inter,sans-serif;color:#1f3864}.rcm-sr-stat .l{font-size:12.5px;color:#5a6678;margin-top:3px;line-height:1.35}",
    ".rcm-sr details{border-top:1px solid #d6e6e7;padding-top:8px;margin-bottom:12px}.rcm-sr summary{cursor:pointer;font:700 14.5px Inter,sans-serif;color:#1f3864}",
    ".rcm-sr-tbl{width:100%;border-collapse:collapse;margin-top:8px;font-size:13.5px}",
    ".rcm-sr-tbl th{text-align:left;font:700 11.5px Inter,sans-serif;letter-spacing:.05em;text-transform:uppercase;color:#5a6678;padding:6px 6px;border-bottom:2px solid #d6e6e7}",
    ".rcm-sr-tbl td{padding:6px;border-bottom:1px solid #e6eef0;vertical-align:middle}.rcm-sr-tbl td.ok{color:#2e6b3e;font-weight:700}.rcm-sr-tbl td.try{color:#b45309}",
    ".rcm-sr-tbl input[type=date]{font-size:13px!important;padding:4px 6px!important}",
    ".rcm-sr-make{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}",
    ".rcm-sr-make input[type=text]{flex:1 1 220px;min-width:0;font:600 15px Inter,sans-serif;padding:8px 11px;border-radius:9px;border:1px solid #9aa3b2;background:#fff;color:#1e2a38}",
    ".rcm-sr-note{margin:10px 0 0!important;font-size:12.5px!important;color:#5a6678;text-align:left!important;hyphens:none!important;line-height:1.5}",
    ".rcm-sr-tbl td.t{white-space:nowrap}@media (max-width:640px){.rcm-sr-tbl .t{display:none}}",
    "html[data-theme='dark'] .rcm-sr,html[data-theme='dark'] .rcm-sr-sign{background:#14262a;border-color:#2f5a5f;color:#e3ecee}",
    "html[data-theme='dark'] .rcm-sr-stat{background:#0f1d21;border-color:#2f5a5f}html[data-theme='dark'] .rcm-sr-stat .n{color:#9fd8dc}",
    "html[data-theme='dark'] .rcm-sr-sign b,html[data-theme='dark'] .rcm-sr summary{color:#7fd0d6}html[data-theme='dark'] .rcm-sr a,html[data-theme='dark'] .rcm-sr-sign a{color:#7fd0d6}",
    "html[data-theme='dark'] .rcm-sr-stat .l,html[data-theme='dark'] .rcm-sr-note,html[data-theme='dark'] .rcm-sr-tbl th{color:#a9b8bc}",
    "html[data-theme='dark'] .rcm-sr-tbl td,html[data-theme='dark'] .rcm-sr-tbl th,html[data-theme='dark'] .rcm-sr details{border-color:#2a4448}",
    "html[data-theme='dark'] .rcm-sr-btn{background:#7fd0d6;border-color:#7fd0d6;color:#10202a}html[data-theme='dark'] .rcm-sr-btn.ghost{background:transparent;color:#7fd0d6}",
    "html[data-theme='dark'] .rcm-sr-tbl td.ok,html[data-theme='dark'] .rcm-sr-msg{color:#6fcf8e}",
    ".rcm-srm{position:fixed;inset:0;z-index:2147483000;background:rgba(10,18,32,.78);display:flex;align-items:center;justify-content:center;padding:16px}",
    ".rcm-srm-box{background:#fff;border-radius:14px;max-width:760px;width:100%;max-height:100%;overflow:auto;padding:14px;box-shadow:0 20px 50px rgba(0,0,0,.4)}",
    ".rcm-srm-title{font:800 17px Inter,sans-serif;color:#1f3864;margin:2px 2px 10px}",
    ".rcm-srm img{display:block;width:100%;height:auto;border:1px solid #d6dae1;border-radius:6px}",
    ".rcm-srm-act{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end;margin-top:12px}",
    "#rcm-sr-print{display:none}",
    "@media print{.rcm-sr-sign,.rcm-sr{display:none!important}",
    "html.rcm-sr-printing body>*:not(#rcm-sr-print){display:none!important}",
    "html.rcm-sr-printing #rcm-sr-print{display:block!important}html.rcm-sr-printing #rcm-sr-print img{display:block;width:100%;height:auto}}"
  ].join("\n");
  document.head.appendChild(css);

  var data = null;
  try { data = JSON.parse((document.getElementById("rcm-study-modules") || {}).textContent || "null"); } catch (e) {}
  if (data && document.getElementById("rcm-sr-app")) hub(data);
  else modulePage();

  /* ---------- module page: preceptor sign-off date for this module's checklist ---------- */
  function modulePage() {
    var m = location.pathname.split("/").pop().replace(/\.html$/, "").match(/^(.+?)-(\d\d)-/);
    var sec = document.getElementById("skills") || document.getElementById("competencies");
    if (!m || !sec) return;
    var track = m[1], nn = m[2], comp = sec.id === "competencies";
    var hubHref = track + ".html#study-record";
    var box = document.createElement("form");   // a form, so Listen does not read it aloud
    box.className = "rcm-sr-sign";
    box.setAttribute("onsubmit", "return false");
    var what = comp ? "competency checklist" : "skills checklist";
    box.innerHTML = '<b>Preceptor sign-off for your study record</b>' +
      '<p>When your preceptor has signed this module&rsquo;s ' + what + ' on your unit&rsquo;s form, enter the date here. It appears on your ' +
      '<a href="' + esc(hubHref) + '">Personal Study Record</a>. It is saved on this device only, and the signed form stays the official record.</p>' +
      '<div class="rcm-sr-row"><label>Signed off on <input type="date" max="' + iso(new Date()) + '" min="2020-01-01" aria-label="Date the ' + what + ' was signed off"></label>' +
      '<button type="button" class="rcm-sr-btn ghost" data-a="clear">Clear</button><span class="rcm-sr-msg" aria-live="polite"></span></div>';
    sec.appendChild(box);
    var input = box.querySelector("input"), msg = box.querySelector(".rcm-sr-msg");
    input.value = skills(track)[nn] || "";
    input.addEventListener("change", function () {
      var v = input.value;
      if (v && !validDate(v)) { msg.style.color = "#b42318"; msg.textContent = "Please choose a date that is not in the future."; return; }
      msg.style.color = "";
      msg.textContent = setSkill(track, nn, v) ? (v ? "Saved." : "Cleared.") : "Could not save on this device.";
    });
    box.querySelector('[data-a="clear"]').addEventListener("click", function () {
      input.value = ""; setSkill(track, nn, ""); msg.style.color = ""; msg.textContent = "Cleared.";
    });
  }

  /* ---------- track hub ---------- */
  function collect(d) {
    var cert = (get("rcm-cert-progress", {}) || {})[d.track] || {};
    var tm = (get("rcm-cert-time", {}) || {})[d.track] || {};
    var course = d.store ? get(d.store, null) : null;
    var sk = skills(d.track);
    var out = { list: [], done: 0, taken: 0, secs: 0, signed: 0, withSkills: 0, exam: cert._exam || null };
    d.modules.forEach(function (m) {
      var nn = m[0], r = cert[nn] || null, pass = +m[4] || 0;
      var c = course && course.modules && course.modules[nn];
      if (c && c.total) {   // a result the course script remembered, if better than the recorded one
        var cp = +c.score >= (pass || Math.ceil(c.total * 0.8));
        if (!r || (cp && !r.p) || (cp === !!r.p && c.score / c.total > r.s / r.t))
          r = { s: +c.score, t: +c.total, p: cp, d: String(c.date || "").slice(0, 10) };
      }
      var sec = +tm[nn] || 0, sd = m[3] ? (validDate(sk[nn]) ? sk[nn] : "") : null;
      if (r) out.taken++; if (r && r.p) out.done++; out.secs += sec;
      if (m[3]) { out.withSkills++; if (sd) out.signed++; }
      out.list.push({ nn: nn, title: m[1], href: m[2], r: r, sec: sec, skills: !!m[3], sd: sd });
    });
    if (!out.exam && course && course.modules && course.modules.exam && course.modules.exam.total) {
      var e = course.modules.exam;
      if (+e.score >= Math.ceil(e.total * 0.8)) out.exam = { s: +e.score, t: +e.total, d: String(e.date || "").slice(0, 10), m: 0 };
    }
    return out;
  }

  function trackName(d) {
    if (d.name) return d.name;
    var cur = document.querySelector(".nc-bar .nc-cur"), h1 = document.querySelector("h1");
    return ((cur || h1 || {}).textContent || "").replace(/\s+/g, " ").trim();
  }

  function hub(d) {
    var app = document.getElementById("rcm-sr-app");
    var NAMEKEY = "rcm-sr-name";
    function render() {
      var pr = collect(d), ex = pr.exam, total = pr.list.length;
      app.className = "rcm-sr";
      app.innerHTML =
        '<div class="rcm-sr-stats">' +
        stat(pr.done + " / " + total, "module quizzes passed") +
        (d.exam ? stat(ex ? Math.round(100 * ex.s / ex.t) + "%" : "—", ex ? "examination passed " + shortDate(ex.d) : "examination not yet passed") : "") +
        (pr.withSkills ? stat(pr.signed + " / " + pr.withSkills, "checklists signed off") : "") +
        stat(pr.secs ? dur(pr.secs) : "—", "time on module pages") +
        '</div><details' + (pr.taken || pr.signed ? " open" : "") + '><summary>Module by module (tap a date to record a sign-off)</summary>' +
        '<div class="table-wrap"><table class="rcm-sr-tbl"><thead><tr><th>Module</th><th class="t">Time</th><th>Quiz</th><th>Sign-off</th></tr></thead><tbody>' +
        pr.list.map(function (m) {
          var r = m.r, ok = r && r.p;
          return '<tr><td><a href="' + esc(m.href) + '">' + +m.nn + ". " + esc(m.title) + '</a></td><td class="t">' + dur(m.sec) + '</td>' +
            '<td class="' + (ok ? "ok" : r ? "try" : "") + '">' + (r ? r.s + "/" + r.t + (ok ? " ✓ " + shortDate(r.d) : " · not yet passed") : "not taken") + '</td>' +
            '<td>' + (m.skills ? '<input type="date" data-nn="' + esc(m.nn) + '" max="' + iso(new Date()) + '" min="2020-01-01" value="' + esc(m.sd || "") +
              '" aria-label="Sign-off date, module ' + +m.nn + '">' : '<span style="color:#5a6678">no checklist</span>') + '</td></tr>';
        }).join("") + '</tbody></table></div></details>' +
        '<form class="rcm-sr-make" onsubmit="return false"><input type="text" maxlength="70" autocomplete="name" placeholder="Full name, e.g. Juan Dela Cruz" aria-label="Name for the study record">' +
        '<button type="button" class="rcm-sr-btn">Make my study record</button></form>' +
        '<p class="rcm-sr-note">Quiz results, the examination result and time are recorded by this browser as you study. Sign-off dates are the ones you enter, ' +
        'from the checklist your preceptor signed. Everything stays on this device; on iPhone and iPad, the Home Screen app and Safari keep separate records. ' +
        'This record is not a certificate and not CPD units.</p>';
      Array.prototype.forEach.call(app.querySelectorAll("input[type=date]"), function (inp) {
        inp.addEventListener("change", function () {
          if (inp.value && !validDate(inp.value)) { inp.value = skills(d.track)[inp.getAttribute("data-nn")] || ""; return; }
          setSkill(d.track, inp.getAttribute("data-nn"), inp.value);
          render(); app.querySelector("details").open = true;
        });
      });
      var nameIn = app.querySelector(".rcm-sr-make input"), btn = app.querySelector(".rcm-sr-make button");
      try { nameIn.value = sessionStorage.getItem(NAMEKEY) || ""; } catch (e) {}
      var go = function () {
        var nm = nameIn.value.replace(/\s+/g, " ").trim();
        if (nm.length < 2) { nameIn.focus(); nameIn.setAttribute("aria-invalid", "true"); return; }
        try { sessionStorage.setItem(NAMEKEY, nm); } catch (e) {}   // this visit only
        openRecord(nm, d, collect(d));
      };
      btn.addEventListener("click", go);
      nameIn.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); go(); } });
    }
    function stat(n, l) { return '<div class="rcm-sr-stat"><div class="n">' + esc(n) + '</div><div class="l">' + esc(l) + '</div></div>'; }
    render();
    window.addEventListener("pageshow", function (e) { if (e.persisted) render(); });
  }

  /* ---------- drawing: one A4 portrait page ---------- */
  var W = 2000, H = 2828;
  var NAVY = "#1b2f55", TEAL = "#1a6b72", GOLD = "#b08a2e", INK = "#1e2a38", MUTED = "#5a6678", GREEN = "#2e6b3e", AMBER = "#b45309";
  var SANS = "Inter, Manrope, 'Helvetica Neue', Arial, sans-serif", SERIF = "Georgia, 'Times New Roman', 'Noto Serif', serif";

  function spaced(ctx, text, x, y, gap) {
    var w = 0, i; for (i = 0; i < text.length; i++) w += ctx.measureText(text[i]).width + (i ? gap : 0);
    var cx = x - w / 2, al = ctx.textAlign; ctx.textAlign = "left";
    for (i = 0; i < text.length; i++) { ctx.fillText(text[i], cx, y); cx += ctx.measureText(text[i]).width + gap; }
    ctx.textAlign = al;
  }
  function fit(ctx, text, maxW, size, weight, family) {
    var s = size; do { ctx.font = weight + " " + s + "px " + family; if (ctx.measureText(text).width <= maxW) break; s -= 2; } while (s > 16);
  }
  function wrap(ctx, text, x, y, maxW, lineH) {
    var words = text.split(" "), line = "", n = 0;
    words.forEach(function (w) {
      var t = line ? line + " " + w : w;
      if (ctx.measureText(t).width > maxW && line) { ctx.fillText(line, x, y + n++ * lineH); line = w; } else line = t;
    });
    if (line) ctx.fillText(line, x, y + n++ * lineH);
    return n;
  }
  function ellipsize(ctx, text, maxW) {
    if (ctx.measureText(text).width <= maxW) return text;
    while (text.length > 4 && ctx.measureText(text + "…").width > maxW) text = text.slice(0, -1);
    return text.replace(/[\s,:;]+$/, "") + "…";
  }

  function draw(canvas, info, d, pr) {
    var ctx = canvas.getContext("2d"); canvas.width = W; canvas.height = H;
    ctx.fillStyle = "#fffdf8"; ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = TEAL; ctx.lineWidth = 12; ctx.strokeRect(36, 36, W - 72, H - 72);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2; ctx.strokeRect(60, 60, W - 120, H - 120);
    ctx.save(); ctx.translate(W / 2, H / 2); ctx.rotate(-0.95);   // faint watermark: never mistaken for a certificate
    ctx.fillStyle = "rgba(26,107,114,.05)"; ctx.font = "800 170px " + SANS; ctx.textAlign = "center"; ctx.fillText("NOT A CERTIFICATE", 0, 0); ctx.restore();

    ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = NAVY; ctx.font = "700 26px " + SANS; spaced(ctx, "RENAL CARE ACADEMY", W / 2, 150, 5);
    ctx.font = "400 76px " + SERIF; ctx.fillText("Personal Study Record", W / 2, 250);
    var tag = "SELF-STUDY RECORD · NOT A CERTIFICATE";
    ctx.font = "800 22px " + SANS; var tw = ctx.measureText(tag).width + tag.length * 2.4 + 56;
    ctx.fillStyle = TEAL; ctx.beginPath();
    if (ctx.roundRect) ctx.roundRect(W / 2 - tw / 2, 282, tw, 42, 21); else ctx.rect(W / 2 - tw / 2, 282, tw, 42);
    ctx.fill(); ctx.fillStyle = "#fff"; spaced(ctx, tag, W / 2, 311, 2.4);

    // who, what, when
    var L = 130, R = W - 130;
    ctx.textAlign = "left";
    function field(x, y, label, value, maxW) {
      ctx.fillStyle = MUTED; ctx.font = "700 19px " + SANS; spaced2(label, x, y);
      ctx.fillStyle = INK; fit(ctx, value, maxW, 34, "600", SANS); ctx.fillText(value, x, y + 44);
    }
    function spaced2(t, x, y) { ctx.save(); ctx.textAlign = "left"; var cx = x; for (var i = 0; i < t.length; i++) { ctx.fillText(t[i], cx, y); cx += ctx.measureText(t[i]).width + 2; } ctx.restore(); }
    field(L, 400, "LEARNER", info.name, 1000);
    field(1200, 400, "DATE PRINTED", info.date, 670);
    field(L, 500, "TRACK", info.track + " · " + pr.list.length + " modules", 1740);

    // summary boxes
    var boxes = [[pr.done + " of " + pr.list.length, "module quizzes passed"]];
    if (d.exam) boxes.push(pr.exam ? [pr.exam.s + " of " + pr.exam.t + " (" + Math.round(100 * pr.exam.s / pr.exam.t) + "%)",
      "examination passed " + shortDate(pr.exam.d) + (pr.exam.m ? " · " + pr.exam.m + " min" : "")] : ["Not yet passed", "end-of-course examination"]);
    if (pr.withSkills) boxes.push([pr.signed + " of " + pr.withSkills, "checklists signed off"]);
    boxes.push([pr.secs ? dur(pr.secs) : "—", "active time on module pages"]);
    var bw = (R - L - 24 * (boxes.length - 1)) / boxes.length, by = 590;
    boxes.forEach(function (b, i) {
      var x = L + i * (bw + 24);
      ctx.fillStyle = "#f1f7f7"; ctx.strokeStyle = "#b9d6d8"; ctx.lineWidth = 2;
      ctx.beginPath(); if (ctx.roundRect) ctx.roundRect(x, by, bw, 128, 14); else ctx.rect(x, by, bw, 128); ctx.fill(); ctx.stroke();
      ctx.textAlign = "center"; ctx.fillStyle = NAVY; fit(ctx, b[0], bw - 30, 40, "800", SANS); ctx.fillText(b[0], x + bw / 2, by + 60);
      ctx.fillStyle = MUTED; fit(ctx, b[1], bw - 24, 20, "500", SANS); ctx.fillText(b[1], x + bw / 2, by + 100);
    });

    // module table
    var top = 770, cols = { time: R - 690, quiz: R - 520, passed: R - 290, sign: R - 16 };
    var n = pr.list.length, footTop = 2330, rowH = Math.max(40, Math.min(62, Math.floor((footTop - 60 - top - 46) / Math.max(n, 1))));
    var fs = rowH < 46 ? 20 : 23;
    ctx.fillStyle = NAVY; ctx.fillRect(L, top, R - L, 46);
    ctx.fillStyle = "#fff"; ctx.font = "700 18px " + SANS; ctx.textAlign = "left"; ctx.fillText("MODULE", L + 16, top + 30);
    ctx.textAlign = "right";
    ctx.fillText("TIME", cols.time, top + 30); ctx.fillText("QUIZ", cols.quiz, top + 30);
    ctx.fillText("PASSED ON", cols.passed, top + 30); ctx.fillText("CHECKLIST SIGN-OFF", cols.sign, top + 30);
    pr.list.forEach(function (m, i) {
      var y = top + 46 + i * rowH, r = m.r, ok = r && r.p, ty = y + rowH / 2 + fs * 0.36;
      if (i % 2) { ctx.fillStyle = "rgba(26,107,114,.06)"; ctx.fillRect(L, y, R - L, rowH); }
      ctx.strokeStyle = "rgba(27,47,85,.14)"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(L, y + rowH); ctx.lineTo(R, y + rowH); ctx.stroke();
      ctx.textAlign = "center"; ctx.font = "800 " + (fs + 2) + "px " + SANS;
      ctx.fillStyle = ok ? GREEN : r ? AMBER : "#9aa3b2"; ctx.fillText(ok ? "✓" : r ? "!" : "○", L + 24, ty);
      ctx.textAlign = "left"; ctx.fillStyle = INK; ctx.font = "600 " + fs + "px " + SANS;
      ctx.fillText(ellipsize(ctx, +m.nn + ". " + m.title, cols.time - 150 - (L + 50)), L + 50, ty);
      ctx.textAlign = "right"; ctx.font = "500 " + fs + "px " + SANS;
      ctx.fillStyle = m.sec ? INK : MUTED; ctx.fillText(dur(m.sec), cols.time, ty);
      ctx.fillStyle = r ? INK : MUTED; ctx.font = "600 " + fs + "px " + SANS; ctx.fillText(r ? r.s + "/" + r.t : "—", cols.quiz, ty);
      ctx.fillStyle = ok ? INK : r ? AMBER : MUTED; ctx.font = (ok ? "500 " : "italic 500 ") + fs + "px " + SANS;
      ctx.fillText(ok ? shortDate(r.d) : r ? "Not yet passed" : "Not taken", cols.passed, ty);
      ctx.fillStyle = m.sd ? INK : MUTED; ctx.font = (m.sd ? "500 " : "italic 500 ") + fs + "px " + SANS;
      ctx.fillText(!m.skills ? "No checklist" : m.sd ? shortDate(m.sd) : "Not recorded", cols.sign, ty);
    });

    // reviewer box (blank lines for a hand signature; nothing typed or stored)
    var ry = footTop;
    ctx.strokeStyle = "#b9d6d8"; ctx.lineWidth = 2; ctx.fillStyle = "#f7fbfb";
    ctx.beginPath(); if (ctx.roundRect) ctx.roundRect(L, ry, R - L, 210, 14); else ctx.rect(L, ry, R - L, 210); ctx.fill(); ctx.stroke();
    ctx.textAlign = "left"; ctx.fillStyle = TEAL; ctx.font = "800 22px " + SANS; ctx.fillText("Reviewed by the head nurse, preceptor or supervisor", L + 28, ry + 46);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.5;
    [[L + 28, 760, "Name"], [L + 830, 560, "Signature"], [L + 1430, R - L - 1458, "Date"]].forEach(function (f) {
      ctx.beginPath(); ctx.moveTo(f[0], ry + 150); ctx.lineTo(f[0] + f[1], ry + 150); ctx.stroke();
      ctx.fillStyle = MUTED; ctx.font = "500 19px " + SANS; ctx.fillText(f[2], f[0], ry + 182);
    });

    // footer
    ctx.textAlign = "center"; ctx.fillStyle = MUTED; ctx.font = "400 20px " + SANS;
    wrap(ctx, "This personal study record is not a certificate of completion and does not confer CPD units. Quiz results, the examination result " +
      "and active time (reading, scrolling or listening) were recorded automatically in the learner's own browser; checklist sign-off dates were " +
      "entered by the learner from the checklist the preceptor signed, so please check them against the unit's competency form. Competence is " +
      "demonstrated on the learner's own unit and signed off under the unit's policy. Nothing on this page was sent to or stored by the website.",
      W / 2, 2610, R - L - 40, 30);
  }

  var modal = null;
  function fileName(info) {
    return "Study-record-" + info.track.replace(/[^A-Za-z0-9]+/g, "-") + "-" + info.name.replace(/[^A-Za-z0-9]+/g, "-") + ".png";
  }
  function openRecord(name, d, pr) {
    var info = { name: name, track: trackName(d), date: longDate(new Date()) };
    var ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
    ready.then(function () {
      var canvas = document.createElement("canvas");
      draw(canvas, info, d, pr);
      var url = canvas.toDataURL("image/png"), file = fileName(info);
      if (modal) modal.remove();
      modal = document.createElement("div");
      modal.className = "rcm-srm"; modal.setAttribute("role", "dialog"); modal.setAttribute("aria-modal", "true"); modal.setAttribute("aria-label", "Your personal study record");
      modal.innerHTML = '<div class="rcm-srm-box"><div class="rcm-srm-title">Your personal study record</div>' +
        '<img alt="Personal study record (not a certificate) for ' + esc(name) + ', ' + esc(info.track) + ': ' + pr.done + ' of ' + pr.list.length +
        ' module quizzes passed" src="' + url + '"><div class="rcm-srm-act">' +
        '<button type="button" class="rcm-sr-btn" data-a="print">Print or save as PDF</button>' +
        '<button type="button" class="rcm-sr-btn ghost" data-a="save">Save image</button>' +
        '<button type="button" class="rcm-sr-btn ghost" data-a="close">Close</button></div></div>';
      document.body.appendChild(modal);
      modal.querySelector('[data-a="print"]').focus();
      modal.addEventListener("click", function (e) {
        var a = e.target === modal ? "close" : (e.target.closest("[data-a]") || { getAttribute: function () { return ""; } }).getAttribute("data-a");
        if (a === "close") close();
        else if (a === "save") save(canvas, url, file);
        else if (a === "print") printIt(url);
      });
    });
  }
  function close() { if (modal) { modal.remove(); modal = null; } }
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal) close(); });
  function save(canvas, url, file) {
    if (canvas.toBlob && navigator.canShare && window.File) {
      canvas.toBlob(function (blob) {
        var f = new File([blob], file, { type: "image/png" });
        if (navigator.canShare({ files: [f] })) navigator.share({ files: [f], title: "Personal study record" }).catch(function () {});
        else download(url, file);
      }, "image/png");
    } else download(url, file);
  }
  function download(url, file) { var a = document.createElement("a"); a.href = url; a.download = file; document.body.appendChild(a); a.click(); a.remove(); }
  var pageStyle = null;
  function printIt(url) {
    var holder = document.getElementById("rcm-sr-print");
    if (!holder) { holder = document.createElement("div"); holder.id = "rcm-sr-print"; document.body.appendChild(holder); }
    if (!pageStyle) { pageStyle = document.createElement("style"); document.head.appendChild(pageStyle); }
    pageStyle.textContent = "@media print{@page{size:A4 portrait;margin:8mm}}";
    holder.innerHTML = '<img alt="">';
    var img = holder.querySelector("img");
    img.onload = function () { document.documentElement.classList.add("rcm-sr-printing"); setTimeout(function () { window.print(); }, 50); };
    img.src = url;
  }
  window.addEventListener("afterprint", function () {
    document.documentElement.classList.remove("rcm-sr-printing");
    if (pageStyle) pageStyle.textContent = "";
  });
})();
