/* academy-listen.js — "Listen to this module" for Renal Care Academy pages (Nov 26 2026, Dr. Rivero).
 *
 * Reads a module aloud with the device's own voice (Web Speech API, through the vendored easy-speech wrapper,
 * which the build concatenates in front of this file). Free, no server, no audio files, works offline in Schola.
 * Built for learners who cannot or should not look at the screen: people with low vision and people driving.
 *   - one tap plays the whole module straight through (title, every section, figure descriptions, tables);
 *     the quiz and the "read next" links are not read
 *   - big, high-contrast controls: back a section, play/pause, forward a section, speed, voice, close
 *   - the paragraph being read is highlighted and kept in view (unless the reader is scrolling)
 *   - the screen is kept awake while playing (Screen Wake Lock), so playback does not stop when it would dim
 *   - the place is remembered per module (localStorage rcm-tts:<path>); speed and voice are remembered too
 *   - pause is implemented as stop-and-remember, because pause() is unreliable on Android
 * Source file: edit this, then run tools/academy/apply_listen.py (writes assets/academy-listen.<hash>.js).
 */
(function () {
  "use strict";
  var ES = window.EasySpeech;
  if (!ES || !("speechSynthesis" in window) || !document.querySelector("main")) return;

  var PATH = location.pathname.replace(/\.html$/, "");
  var K_POS = "rcm-tts:" + PATH, K_RATE = "rcm-tts-rate", K_VOICE = "rcm-tts-voice";
  var RATES = [0.8, 1, 1.15, 1.3, 1.5, 1.75, 2];
  var SKIP_SECTIONS = { quiz: 1, reading: 1 };
  var reduceMotion = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- text: what to read ---------- */
  var BLOCK = "h1,h2,h3,h4,p,li,figcaption,tr,dt,dd,blockquote", LEAF = "p,li,figcaption,tr,dt,dd,blockquote";
  var UNIT = [
    [/(\d)\s?mL\/min\b/g, "$1 milliliters per minute"], [/(\d)\s?mL\/h\b/g, "$1 milliliters per hour"],
    [/(\d)\s?mL\b/g, "$1 milliliters"], [/(\d)\s?mg\/dL\b/g, "$1 milligrams per deciliter"],
    [/(\d)\s?mmol\/L\b/g, "$1 millimoles per liter"], [/(\d)\s?mEq\/L\b/g, "$1 milliequivalents per liter"],
    [/(\d)\s?g\/dL\b/g, "$1 grams per deciliter"], [/(\d)\s?g\/L\b/g, "$1 grams per liter"],
    [/(\d)\s?mg\b/g, "$1 milligrams"], [/(\d)\s?kg\b/g, "$1 kilograms"], [/(\d)\s?mmHg\b/g, "$1 millimeters of mercury"],
    [/(\d)\s?°C\b/g, "$1 degrees Celsius"], [/(\d)\s?%/g, "$1 percent"]
  ];
  function speakable(s) {
    s = s.replace(/\[\d+(?:[,–-]\s*\d+)*\]/g, "")                // citation markers [3] [2,4]
      .replace(/(\d)\s*[–—-]\s*(\d)/g, "$1 to $2")               // 4–6 -> 4 to 6
      .replace(/\be\.g\.,?/gi, "for example,").replace(/\bi\.e\.,?/gi, "that is,").replace(/\bvs\.?(?=\s)/gi, "versus")
      .replace(/≥/g, " greater than or equal to ").replace(/≤/g, " less than or equal to ")
      .replace(/\s>\s/g, " greater than ").replace(/\s<\s/g, " less than ")
      .replace(/→|⇒/g, " to ").replace(/×/g, " times ").replace(/±/g, " plus or minus ")
      .replace(/[µμ]g\b/g, " micrograms").replace(/·|•|&middot;/g, ", ").replace(/[“”]/g, '"').replace(/[‘’]/g, "'");
    UNIT.forEach(function (u) { s = s.replace(u[0], u[1]); });
    return s.replace(/\s+([,.;:!?])/g, "$1").replace(/\s+/g, " ").trim();
  }
  function visible(el) { return el.getClientRects().length > 0 && !el.closest(".lang-hidden,[hidden],[aria-hidden='true']"); }
  var EXCL = "button,svg,sup,script,style,.nc-cite,.rcn-bm,.rcm-tts-ui,[aria-hidden='true'],.lang-hidden,input,select,textarea";
  function cleanText(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll(EXCL).forEach(function (n) { n.remove(); });
    return (c.textContent || "").replace(/\s+/g, " ").trim();
  }
  // Live text of an element with a map from each character back to its DOM text node, so a spoken sentence or
  // word can be highlighted in place (CSS Custom Highlight API: no change to the page's markup).
  function textMap(el) {
    var str = "", map = [], space = true;
    var w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: function (n) {
      var p = n.parentElement; return p && p !== el && p.closest(EXCL) && el.contains(p.closest(EXCL)) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; } });
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      var t = n.nodeValue;
      for (var i = 0; i < t.length; i++) {
        if (/\s/.test(t[i])) { if (!space) { str += " "; map.push([n, i]); space = true; } }
        else { str += t[i]; map.push([n, i]); space = false; }
      }
    }
    if (str.endsWith(" ")) { str = str.slice(0, -1); map.pop(); }
    return { str: str, map: map };
  }
  function rangeOf(m, a, b) {
    if (!m || a < 0 || b <= a || b > m.map.length) return null;
    var r = document.createRange(), s0 = m.map[a], s1 = m.map[b - 1];
    try { r.setStart(s0[0], s0[1]); r.setEnd(s1[0], s1[1] + 1); } catch (e) { return null; }
    return r;
  }
  function tableRowText(tr) {
    var table = tr.closest("table"), cells = Array.prototype.slice.call(tr.children);
    if (!cells.length || tr.closest("thead") || cells.every(function (c) { return c.tagName === "TH"; }) && tr === table.rows[0]) return "";
    var head = table.tHead && table.tHead.rows[0] || (table.rows[0] && Array.prototype.every.call(table.rows[0].cells, function (c) { return c.tagName === "TH"; }) ? table.rows[0] : null);
    var hs = head ? Array.prototype.map.call(head.cells, cleanText) : [];
    return cells.map(function (c, i) { var t = cleanText(c); return t ? (hs[i] && i > 0 ? hs[i] + ": " : "") + t : ""; })
      .filter(Boolean).join(". ");
  }
  function chunks(text) {                                         // sentences, at most ~220 characters each
    var out = [], parts = text.split(/(?<=[.!?:;])\s+(?=["(]?[A-Z0-9])/);
    parts.forEach(function (p) {
      while (p.length > 240) {
        var cut = p.lastIndexOf(", ", 220); if (cut < 80) cut = p.lastIndexOf(" ", 220); if (cut < 40) cut = 220;
        out.push(p.slice(0, cut + 1)); p = p.slice(cut + 1).trim();
      }
      if (p) out.push(p);
    });
    return out;
  }

  var items = [], sections = [];                                  // items: {el, sec, parts[]}
  function build() {
    items = []; sections = [];
    var h1 = document.querySelector(".hero h1, h1");
    if (h1) items.push({ el: h1, sec: -1, parts: chunks(speakable(cleanText(h1))) });
    var main = document.querySelector("main");
    main.querySelectorAll("section.section").forEach(function (sec) {
      if (SKIP_SECTIONS[sec.id] || !visible(sec)) {
        if (sec.id === "quiz") items.push({ el: sec.querySelector("h2") || sec, sec: sections.length - 1, note: 1,
          parts: ["This module ends with a short quiz. Open it on screen when it is safe to do so. End of module."] });
        return;
      }
      var h2 = sec.querySelector("h2");
      sections.push({ el: sec, title: h2 ? cleanText(h2) : "", first: items.length });
      var si = sections.length - 1;
      sec.querySelectorAll(BLOCK).forEach(function (el) {
        if (!visible(el) || el.closest("form,fieldset,.nc-nextprev,.calc-cards-wrap,.section-tag,.nc-cite,.rcm-tts-ui")) return;
        var tag = el.tagName, text;
        if (tag === "TR") text = tableRowText(el);
        else if (tag === "FIGCAPTION") { var d = el.querySelector(".fig-desc"); text = d ? cleanText(d) : cleanText(el); if (text) text = "Figure. " + text; }
        else {
          if (el.closest("figcaption,tr") || el.querySelector(LEAF)) return; // read leaves only
          text = cleanText(el);
        }
        if (tag === "TR" || tag === "FIGCAPTION") {                 // composite text: paragraph highlight only
          text = speakable(text || "");
          if (text.length > 1) items.push({ el: el, sec: si, parts: chunks(text) });
          return;
        }
        var m = textMap(el);
        if (m.str !== text) m = null;                               // map must match what is read, else no in-text highlight
        var raw = chunks(text), parts = [], spans = [], at = 0;
        raw.forEach(function (r) {
          var a = m ? m.str.indexOf(r, at) : -1;
          if (a >= 0) at = a + r.length;
          var say = speakable(r);
          if (say.length > 1) { parts.push(say); spans.push(a >= 0 ? { a: a, b: a + r.length, same: say === r.trim() } : null); }
        });
        if (parts.length) items.push({ el: el, sec: si, parts: parts, spans: spans, map: m });
      });
    });
    if (!items.some(function (it) { return it.note; })) items.push({ el: null, sec: sections.length - 1, note: 1, parts: ["End of module."] });
  }

  /* ---------- player state ---------- */
  var idx = 0, part = 0, playing = false, token = 0, voice = null, rate = parseFloat(ls(K_RATE)) || 1, ready = null, wake = null;
  var lastUserScroll = 0, ui = null, statusEl, secEl, playBtn, rateBtn, voiceSel;
  ["wheel", "touchmove", "keydown"].forEach(function (ev) { window.addEventListener(ev, function (e) { if (ev !== "keydown" || /Arrow|Page|Home|End|Space/.test(e.code || "")) lastUserScroll = Date.now(); }, { passive: true }); });

  function init() {
    if (!ready) ready = ES.init({ maxTimeout: 5000, interval: 250, quiet: true }).catch(function () { return false; }).then(function () {
      var vs = (ES.voices() || []).filter(function (v) { return /^en([-_]|$)/i.test(v.lang); });
      var score = function (v) { return (/natural|neural|premium|enhanced|siri|google/i.test(v.name) ? 4 : 0) + (/en[-_](US|PH)/i.test(v.lang) ? 2 : 0) + (v.localService ? 1 : 0); };
      vs.sort(function (a, b) { return score(b) - score(a) || a.name.localeCompare(b.name); });
      var saved = ls(K_VOICE);
      voice = vs.filter(function (v) { return v.voiceURI === saved || v.name === saved; })[0] || vs[0] || null;
      return vs;
    });
    return ready;
  }

  function mark() {
    document.querySelectorAll(".rcm-tts-cur").forEach(function (n) { n.classList.remove("rcm-tts-cur"); });
    var it = items[idx]; if (!it || !it.el) return;
    it.el.classList.add("rcm-tts-cur");
    if (Date.now() - lastUserScroll > 6000) {
      var r = it.el.getBoundingClientRect(), vh = innerHeight;
      if (r.top < 70 || r.bottom > vh - 130) it.el.scrollIntoView({ block: "center", behavior: reduceMotion ? "auto" : "smooth" });
    }
    var s = sections[it.sec];
    if (secEl) secEl.textContent = it.sec < 0 ? "Introduction" : (s ? "Section " + (it.sec + 1) + " of " + sections.length + ": " + s.title : "");
  }
  var HL = window.CSS && CSS.highlights && window.Highlight ? CSS.highlights : null;
  function hl(name, range) { if (!HL) return; if (range) HL.set(name, new Highlight(range)); else HL.delete(name); }
  function hlSentence() {
    var it = items[idx], sp = it && it.spans && it.spans[part];
    hl("rcm-tts-word", null);
    hl("rcm-tts-sent", sp ? rangeOf(it.map, sp.a, sp.b) : null);
  }
  function hlWord(ci) {
    var it = items[idx], sp = it && it.spans && it.spans[part];
    if (!sp || !sp.same || typeof ci !== "number") return;
    var str = it.map.str, a = sp.a + ci;
    while (a < sp.b && /\s/.test(str[a])) a++;
    var b = a; while (b < sp.b && !/\s/.test(str[b])) b++;
    while (b > a && /[,.;:!?)"']/.test(str[b - 1])) b--;
    hl("rcm-tts-word", rangeOf(it.map, a, b));
  }
  function save() { ls(K_POS, JSON.stringify({ i: idx, t: Date.now() })); }

  function speakNext() {
    var my = ++token;
    if (!playing) return;
    var it = items[idx];
    if (!it) { finish(); return; }
    if (part >= it.parts.length) { idx++; part = 0; save(); speakNext(); return; }
    if (part === 0) mark();
    hlSentence();
    ES.speak({ text: it.parts[part], voice: voice || undefined, rate: rate, pitch: 1, volume: 1, force: true,
      boundary: function (e) { if (my === token && e && (e.name === "word" || !e.name)) hlWord(e.charIndex); },
      end: function () { if (my !== token) return; part++; speakNext(); },
      error: function (e) { if (my !== token) return; if (e && /interrupted|canceled/.test(e.error || "")) return; part++; speakNext(); }
    }).catch(function () {});
  }
  function play() {
    init().then(function () {
      if (!items.length) build();
      playing = true; setUI(); keepAwake(true); speakNext();
    });
  }
  function stop(keep) { hl("rcm-tts-word", null); playing = false; token++; try { ES.cancel(); } catch (e) {} keepAwake(false); setUI(); if (keep) save(); }
  function finish() { stop(false); idx = 0; part = 0; ls(K_POS, null); mark(); status("Finished. Tap play to listen again."); }
  function jumpSection(d) {
    var cur = items[idx] ? items[idx].sec : -1, target = Math.max(-1, Math.min(sections.length - 1, cur + d));
    if (d < 0 && items[idx] && sections[cur] && idx > sections[cur].first + 1) target = cur;   // back = start of this section first
    idx = target < 0 ? 0 : sections[target].first; part = 0; save();
    if (playing) { token++; try { ES.cancel(); } catch (e) {} setTimeout(speakNext, 60); } else mark();
  }
  function keepAwake(on) {
    if (!("wakeLock" in navigator)) return;
    if (on && !wake) navigator.wakeLock.request("screen").then(function (w) { wake = w; w.addEventListener("release", function () { wake = null; }); }).catch(function () {});
    if (!on && wake) { wake.release().catch(function () {}); wake = null; }
  }
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "visible" && playing) keepAwake(true);
  });
  window.addEventListener("pagehide", function () { if (playing) stop(true); });

  /* ---------- UI ---------- */
  var IC = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z" fill="currentColor"/></svg>',
    prev: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h2v14H6zM19 5.5v13L9 12z" fill="currentColor"/></svg>',
    next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 5h2v14h-2zM5 5.5v13L15 12z" fill="currentColor"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
    head: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 14v-2a8 8 0 0 1 16 0v2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><rect x="3" y="13" width="4.5" height="7" rx="1.6" fill="currentColor"/><rect x="16.5" y="13" width="4.5" height="7" rx="1.6" fill="currentColor"/></svg>'
  };
  function status(t) { if (statusEl) statusEl.textContent = t; }
  function setUI() {
    if (!playBtn) return;
    playBtn.innerHTML = playing ? IC.pause : IC.play;
    playBtn.setAttribute("aria-label", playing ? "Pause" : "Play");
    playBtn.setAttribute("aria-pressed", playing ? "true" : "false");
    status(playing ? "Reading aloud" : "Paused");
    document.body.classList.toggle("rcm-tts-playing", playing);
  }
  function rateLabel() { return (rate === 1 ? "1" : String(rate)) + "×"; }

  function openPlayer() {
    if (!ui) {
      ui = document.createElement("div");
      ui.className = "rcm-tts-ui rcm-tts-bar no-print";
      ui.setAttribute("role", "region");
      ui.setAttribute("aria-label", "Listen to this module");
      ui.innerHTML =
        '<div class="rcm-tts-info"><span class="rcm-tts-status" aria-live="polite">Paused</span><span class="rcm-tts-sec"></span></div>' +
        '<div class="rcm-tts-ctrls">' +
          '<button type="button" class="rcm-tts-b" data-a="prev" aria-label="Previous section">' + IC.prev + '</button>' +
          '<button type="button" class="rcm-tts-b rcm-tts-play" data-a="play" aria-label="Play" aria-pressed="false">' + IC.play + '</button>' +
          '<button type="button" class="rcm-tts-b" data-a="next" aria-label="Next section">' + IC.next + '</button>' +
          '<button type="button" class="rcm-tts-b rcm-tts-rate" data-a="rate" aria-label="Reading speed">' + rateLabel() + '</button>' +
          '<label class="rcm-tts-vl"><span class="rcm-tts-sr">Voice</span><select class="rcm-tts-voice" aria-label="Voice"></select></label>' +
          '<button type="button" class="rcm-tts-b rcm-tts-x" data-a="close" aria-label="Stop and close the player">' + IC.close + '</button>' +
        '</div>';
      document.body.appendChild(ui);
      statusEl = ui.querySelector(".rcm-tts-status"); secEl = ui.querySelector(".rcm-tts-sec");
      playBtn = ui.querySelector(".rcm-tts-play"); rateBtn = ui.querySelector(".rcm-tts-rate"); voiceSel = ui.querySelector(".rcm-tts-voice");
      ui.addEventListener("click", function (e) {
        var b = e.target.closest("button[data-a]"); if (!b) return;
        var a = b.getAttribute("data-a");
        if (a === "play") { if (playing) stop(true); else play(); }
        else if (a === "prev") jumpSection(-1);
        else if (a === "next") jumpSection(1);
        else if (a === "rate") {
          rate = RATES[(RATES.indexOf(rate) + 1) % RATES.length] || 1; ls(K_RATE, String(rate)); rateBtn.textContent = rateLabel();
          rateBtn.setAttribute("aria-label", "Reading speed " + rateLabel());
          if (playing) { token++; try { ES.cancel(); } catch (x) {} setTimeout(speakNext, 60); }
        } else if (a === "close") closePlayer();
      });
      voiceSel.addEventListener("change", function () {
        var vs = ES.voices() || []; voice = vs.filter(function (v) { return v.voiceURI === voiceSel.value; })[0] || voice;
        if (voice) ls(K_VOICE, voice.voiceURI);
        if (playing) { token++; try { ES.cancel(); } catch (x) {} setTimeout(speakNext, 60); }
      });
      init().then(function (vs) {
        (vs || []).forEach(function (v) {
          var o = document.createElement("option"); o.value = v.voiceURI;
          o.textContent = v.name.replace(/\s*\(.*?\)\s*/g, " ").trim() + (/[-_]PH/i.test(v.lang) ? " (Philippines)" : "");
          if (voice && v.voiceURI === voice.voiceURI) o.selected = true;
          voiceSel.appendChild(o);
        });
        if (!vs || !vs.length) { status("This device has no English voice installed."); voiceSel.disabled = true; }
      });
    }
    ui.hidden = false;
    document.body.classList.add("rcm-tts-on");
    build();
    playBtn.focus({ preventScroll: true });
  }
  function closePlayer() {
    stop(true);
    document.querySelectorAll(".rcm-tts-cur").forEach(function (n) { n.classList.remove("rcm-tts-cur"); });
    hl("rcm-tts-sent", null); hl("rcm-tts-word", null);
    if (ui) ui.hidden = true;
    document.body.classList.remove("rcm-tts-on");
    if (launch) launch.focus({ preventScroll: true });
  }

  /* ---------- launch button (in the hero, under the title) ---------- */
  var launch = null;
  function addLaunch() {
    var anchor = document.querySelector(".hero .hero-meta") || document.querySelector(".hero h1");
    if (!anchor) return;
    var saved = null; try { saved = JSON.parse(ls(K_POS) || "null"); } catch (e) {}
    launch = document.createElement("button");
    launch.type = "button";
    launch.className = "rcm-tts-ui rcm-tts-launch no-print";
    launch.innerHTML = IC.head + '<span>' + (saved && saved.i > 0 ? "Resume listening" : "Listen to this module") + '</span>';
    launch.setAttribute("aria-label", (saved && saved.i > 0 ? "Resume listening to" : "Listen to") + " this module, read aloud by your device");
    launch.addEventListener("click", function () {
      openPlayer();
      if (saved && saved.i > 0 && saved.i < items.length) { idx = saved.i; part = 0; } else { idx = 0; part = 0; }
      saved = null;
      play();
    });
    anchor.parentNode.insertBefore(launch, anchor.nextSibling);
  }

  var css = document.createElement("style");
  css.id = "rcm-tts-css";
  css.textContent = [
    ".rcm-tts-launch{display:inline-flex;align-items:center;gap:9px;margin:14px 0 4px;padding:12px 20px 12px 16px;min-height:48px;border-radius:999px;border:2px solid #1F3864;background:#1F3864;color:#fff;font:700 16px/1.1 Inter,Manrope,system-ui,sans-serif;cursor:pointer;box-shadow:0 6px 16px -8px rgba(20,40,75,.55)}",
    ".rcm-tts-launch svg{width:22px;height:22px}.rcm-tts-launch:hover{background:#16294a}",
    ".rcm-tts-launch:focus-visible,.rcm-tts-b:focus-visible,.rcm-tts-voice:focus-visible{outline:3px solid #f0a81e;outline-offset:2px}",
    ".rcm-tts-bar{position:fixed;z-index:100002;left:50%;bottom:16px;transform:translateX(-50%);width:min(640px,calc(100% - 150px));background:#13233f;color:#fff;border-radius:18px;padding:10px 12px;box-shadow:0 14px 40px -10px rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.14);font-family:Inter,Manrope,system-ui,sans-serif}",
    ".rcm-tts-bar[hidden]{display:none}",
    ".rcm-tts-info{display:flex;gap:10px;align-items:baseline;min-width:0;padding:0 4px 8px}",
    ".rcm-tts-status{font:800 12px/1 Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#f3c46a;flex:none}",
    ".rcm-tts-sec{font-size:14px;color:#e6edf8;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}",
    ".rcm-tts-ctrls{display:flex;align-items:center;gap:8px}",
    ".rcm-tts-b{flex:none;display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:14px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);color:#fff;cursor:pointer;font:800 16px/1 Inter,sans-serif}",
    ".rcm-tts-b svg{width:26px;height:26px}.rcm-tts-b:hover{background:rgba(255,255,255,.16)}",
    ".rcm-tts-play{width:64px;height:64px;border-radius:50%;background:#f0a81e;border-color:#f0a81e;color:#13233f}.rcm-tts-play:hover{background:#ffc04a}",
    ".rcm-tts-play svg{width:32px;height:32px}",
    ".rcm-tts-x{margin-left:auto}",
    ".rcm-tts-vl{flex:1;min-width:0}.rcm-tts-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}",
    ".rcm-tts-voice{width:100%;min-width:0;height:52px;border-radius:14px;border:1px solid rgba(255,255,255,.22);background:#1d3157;color:#fff;font:600 15px Inter,sans-serif;padding:0 10px}",
    ".rcm-tts-cur{background:#fff8dc !important;box-shadow:0 0 0 6px #fff8dc;border-radius:4px;color:#1e2a38 !important}",
    "::highlight(rcm-tts-sent){background-color:#ffe38f;color:#1e2a38}",
    "::highlight(rcm-tts-word){background-color:#f0a81e;color:#111}",
    "html[data-theme='dark'] .rcm-tts-cur{background:#2b2717 !important;box-shadow:0 0 0 6px #2b2717;color:#fff6dc !important}",
    "html[data-theme='dark'] ::highlight(rcm-tts-sent){background-color:#6b5414;color:#fff}",
    "html[data-theme='dark'] ::highlight(rcm-tts-word){background-color:#f0a81e;color:#111}",
    "html[data-theme='dark'] .rcm-tts-launch{background:#f0a81e;border-color:#f0a81e;color:#13233f}",
    "body.rcm-tts-on{padding-bottom:140px}",
    "body.rcm-tts-on .rcn-toast,body.rcm-tts-on .rcn-resume{display:none !important}",
    "@media (max-width:640px){.rcm-tts-bar{width:calc(100% - 16px);bottom:8px;padding:10px}",
    "  .rcm-tts-ctrls{flex-wrap:wrap;gap:8px}.rcm-tts-b{width:50px;height:50px}.rcm-tts-play{width:60px;height:60px}",
    "  .rcm-tts-vl{order:9;flex:1 1 100%}.rcm-tts-voice{height:42px;font-size:14px}",
    "  body.rcm-tts-on{padding-bottom:200px}",
    "  body.rcm-tts-on .float-controls,body.rcm-tts-on .float-controls-left,body.rcm-tts-on .scroll-top-btn,body.rcm-tts-on .rcn-fab,body.rcm-tts-on .print-btn{translate:0 -178px !important}}",
    "@media print{.rcm-tts-ui{display:none !important}.rcm-tts-cur{background:none !important;box-shadow:none !important}}"
  ].join("\n");
  document.head.appendChild(css);

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", addLaunch); else addLaunch();
})();
