/* Renal Care Academy: module quiz progress for the certificate of completion (Dr. Rivero, Nov 27 2026).
 *
 * On a module page (file name <track>-NN-<slug>.html) it records the learner's best end-of-module quiz result in
 * localStorage "rcm-cert-progress" = { "<track>": { "NN": { s: score, t: total, p: passed, d: "YYYY-MM-DD" } } }.
 * The end-of-course examination page (academy-certificate.js) unlocks the certificate only when every module quiz of
 * the track is passed on this device. A module quiz is passed at its own pass mark (data-pass) or 80%, and never when
 * the page itself says "Not yet passed" (safety-critical questions missed).
 * Nothing leaves the device. Edit this file; tools/academy/apply_certificate.py fingerprints and tags it.
 */
(function () {
  "use strict";
  var KEY = "rcm-cert-progress";
  var m = location.pathname.split("/").pop().replace(/\.html$/, "").match(/^(.+?)-(\d\d)-/);
  var form = document.getElementById("nc-quiz"), result = document.getElementById("nc-result");
  if (!m || !form || !result) return;
  var track = m[1], nn = m[2];

  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } }
  function save(o) { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2);
  }
  function passMark(total) {
    var p = +form.getAttribute("data-pass");
    return p > 0 ? p : Math.ceil(total * 0.8);
  }
  function record(score, total, verdictFail) {
    if (!total) return;
    var passed = !verdictFail && score >= passMark(total);
    var o = load(), t = o[track] || (o[track] = {}), old = t[nn];
    // Keep the best result; a pass is never overwritten by a later lower score.
    if (!old || (passed && !old.p) || (passed === !!old.p && score / total > old.s / old.t)) {
      t[nn] = { s: score, t: total, p: passed, d: today() };
      save(o);
    }
  }

  // Results the course script already remembered on this device ("Remember my result"), counted once.
  try {
    var store = document.documentElement.getAttribute("data-nc-store") ||
      (document.body && document.body.getAttribute("data-course") ? "rcm-course-" + document.body.getAttribute("data-course") + "-progress" : "");
    var prev = store && JSON.parse(localStorage.getItem(store) || "null");
    var r = prev && prev.modules && prev.modules[form.getAttribute("data-module")];
    if (r && r.total) record(+r.score, +r.total, false);
  } catch (e) {}

  var last = "";
  new MutationObserver(function () {
    var t = (result.textContent || "").replace(/\s+/g, " ");
    var mm = t.match(/(\d+)\s+of\s+(\d+)/);
    if (!mm || t === last) return;
    last = t;
    record(+mm[1], +mm[2], /not yet passed/i.test(t));
  }).observe(result, { childList: true, characterData: true, subtree: true });
})();
