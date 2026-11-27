/* Renal Care Academy: "Updated since you read it" flags (Dr. William Gregory Rivero, Nov 27 2026).
 *
 * Shows a learner which modules they already finished have changed since. Everything is worked out on the device:
 *   finished  = this browser holds a quiz result for the module, in "rcm-cert-progress" (academy-progress.js) or in the
 *               course's own "Remember my result" store (rcm-course-<course>-progress). The finish date is the newest
 *               date in either record.
 *   flagged   = the module has an update dated AFTER that finish date that the learner has not yet acknowledged.
 *   seen      = localStorage "rcm-updates-seen" = { "<module file>": "YYYY-MM-DD" } (date of the newest update acknowledged).
 * Learners who never finished a module see nothing: they will read the current version anyway.
 *
 * The page carries its own data, written by tools/academy/apply_updates.py from data/academy-updates.json:
 *   module page:  <script type="application/json" id="rcm-updates">{"page": file, "updates": [{date, note, anchor?}]}</script>
 *   track hub:    <script type="application/json" id="rcm-updates">{"hub": true, "modules": {file: [dates…]}}</script>
 * Nothing leaves the device. Edit this file; apply_updates.py fingerprints and tags it.
 */
(function () {
  "use strict";
  var data;
  try { data = JSON.parse((document.getElementById("rcm-updates") || {}).textContent || "null"); } catch (e) { return; }
  if (!data) return;

  var SEEN = "rcm-updates-seen", MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  function get(key) { try { return JSON.parse(localStorage.getItem(key) || "null"); } catch (e) { return null; } }
  function seenMap() { return get(SEEN) || {}; }
  function markSeen(file, date) {
    var s = seenMap();
    if (!s[file] || s[file] < date) { s[file] = date; try { localStorage.setItem(SEEN, JSON.stringify(s)); } catch (e) {} }
  }
  function nice(d) {   // "2026-11-27" -> "Nov 27, 2026"
    var p = (d || "").split("-");
    return p.length === 3 ? MONTHS[+p[1] - 1] + " " + (+p[2]) + ", " + p[0] : d;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  var cert = get("rcm-cert-progress") || {};
  var store = document.documentElement.getAttribute("data-nc-store") ||
    (document.body && document.body.getAttribute("data-course") ? "rcm-course-" + document.body.getAttribute("data-course") + "-progress" : "");
  var course = (store && get(store)) || {};

  /* Newest date this device recorded the learner finishing the module (its quiz), or "" if never. */
  function finished(file, moduleKey) {
    var m = file.replace(/\.html$/, "").match(/^(.+?)-(\d\d)-/), best = "";
    var c = m && cert[m[1]] && cert[m[1]][m[2]];
    if (c && c.d) best = c.d;
    var r = course.modules && course.modules[moduleKey || (m && m[2])];
    if (r && r.date && r.date > best) best = r.date;
    return best;
  }
  function pending(file, dates, moduleKey) {
    var done = finished(file, moduleKey);
    if (!done) return [];
    var ack = seenMap()[file] || "";
    return dates.filter(function (d) { return d > done && d > ack; });
  }

  var css = document.createElement("style");
  css.textContent =
    ".rcm-upd{border:1px solid #e3b48c;border-left:5px solid #C55A11;background:#fff7f0;border-radius:12px;padding:14px 18px;margin:0 0 22px}" +
    ".rcm-upd-k{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:#C55A11;margin:0 0 4px}" +
    ".rcm-upd p{margin:0 0 8px;line-height:1.55}.rcm-upd ul{margin:0 0 10px 20px;padding:0}.rcm-upd li{margin:0 0 6px;line-height:1.55}" +
    ".rcm-upd-d{font-weight:700;white-space:nowrap}.rcm-upd a{color:#C55A11;font-weight:600}" +
    ".rcm-upd button{font:inherit;font-size:14px;font-weight:600;border:1px solid #C55A11;color:#C55A11;background:transparent;border-radius:999px;padding:5px 14px;cursor:pointer}" +
    ".rcm-upd button:hover{background:#C55A11;color:#fff}" +
    ".rcm-upd-pill{display:inline-block;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;font-weight:700;color:#fff;background:#C55A11;border-radius:999px;padding:2px 9px;vertical-align:middle;margin-left:8px}" +
    ".nc-mod-top .rcm-upd-pill{margin-left:auto}" +
    ".rcm-upd-sum{font-size:14.5px;margin:0 0 10px;color:#9a4510;font-weight:600}" +
    "html[data-theme=\"dark\"] .rcm-upd{background:#2a1d14;border-color:#7a4a28;border-left-color:#e07a35}" +
    "html[data-theme=\"dark\"] .rcm-upd-k,html[data-theme=\"dark\"] .rcm-upd a,html[data-theme=\"dark\"] .rcm-upd-sum{color:#f0a066}" +
    "html[data-theme=\"dark\"] .rcm-upd button{border-color:#f0a066;color:#f0a066}" +
    "html[data-theme=\"dark\"] .rcm-upd button:hover{background:#f0a066;color:#1b1b1b}" +
    "html[data-theme=\"dark\"] .rcm-upd-pill{background:#e07a35;color:#1b1b1b}" +
    "html[data-theme=\"dark\"][data-shade=\"dim\"] .rcm-upd{background:#3a2a1f;border-color:#8a5a36}" +
    "@media print{.rcm-upd,.rcm-upd-pill,.rcm-upd-sum{display:none}}";
  document.head.appendChild(css);

  /* ---------- module page: banner with what changed ---------- */
  if (data.page && data.updates) {
    var form = document.getElementById("nc-quiz");
    var key = form && form.getAttribute("data-module");
    var due = pending(data.page, data.updates.map(function (u) { return u.date; }), key);
    if (!due.length) return;
    var newest = due.reduce(function (a, b) { return a > b ? a : b; });
    var items = data.updates.filter(function (u) { return due.indexOf(u.date) >= 0; })
      .sort(function (a, b) { return a.date < b.date ? 1 : -1; });

    var box = document.createElement("aside");
    box.className = "rcm-upd";
    box.setAttribute("role", "note");
    box.innerHTML =
      '<div class="rcm-upd-k">Updated since you read it</div>' +
      "<p>This module changed after you finished it on " + esc(nice(finished(data.page, key))) + ". What is new:</p>" +
      "<ul>" + items.map(function (u) {
        var go = u.anchor && document.getElementById(u.anchor) ? ' <a href="#' + esc(u.anchor) + '" data-upd-go>Go to it</a>' : "";
        return '<li><span class="rcm-upd-d">' + esc(nice(u.date)) + ":</span> " + esc(u.note) + go + "</li>";
      }).join("") + "</ul>" +
      '<button type="button">Got it</button>';

    function done() { markSeen(data.page, newest); box.remove(); pills.forEach(function (p) { p.remove(); }); }
    box.querySelector("button").addEventListener("click", done);
    Array.prototype.forEach.call(box.querySelectorAll("[data-upd-go]"), function (a) {
      a.addEventListener("click", function () { markSeen(data.page, newest); setTimeout(function () { box.remove(); }, 0); });
    });

    // An "Updated" pill on each changed section's heading, until acknowledged.
    var pills = [];
    items.forEach(function (u) {
      var sec = u.anchor && document.getElementById(u.anchor);
      var h = sec && (sec.matches("h2,h3") ? sec : sec.querySelector("h2,h3"));
      if (h && !h.querySelector(".rcm-upd-pill")) {
        var p = document.createElement("span");
        p.className = "rcm-upd-pill"; p.textContent = "Updated";
        h.appendChild(p); pills.push(p);
      }
    });

    var main = document.querySelector("main") || document.body;
    var first = main.querySelector("section.section, section[id]");
    if (first) first.parentNode.insertBefore(box, first); else main.insertBefore(box, main.firstChild);
    return;
  }

  /* ---------- track hub: flag on each finished module that changed ---------- */
  if (data.hub && data.modules) {
    var count = 0, grid = null;
    Array.prototype.forEach.call(document.querySelectorAll("a.nc-mod[data-module][href]"), function (card) {
      var file = card.getAttribute("href").split("/").pop().split("#")[0];
      var dates = data.modules[file];
      if (!dates || !pending(file, dates, card.getAttribute("data-module")).length) return;
      var top = card.querySelector(".nc-mod-top") || card;
      if (top.querySelector(".rcm-upd-pill")) return;
      var p = document.createElement("span");
      p.className = "rcm-upd-pill";
      p.textContent = "Updated since you read it";
      top.appendChild(p);
      count++;
      grid = grid || card.parentNode;
    });
    if (count && grid) {
      var s = document.createElement("p");
      s.className = "rcm-upd-sum";
      s.textContent = count === 1 ? "1 module you finished has been updated. Look for the orange flag."
        : count + " modules you finished have been updated. Look for the orange flags.";
      grid.parentNode.insertBefore(s, grid);
    }
  }
})();
