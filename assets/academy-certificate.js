/* Renal Care Academy: certificate of completion (Dr. Rivero, Nov 27 2026).
 *
 * On a track's end-of-course examination page: when the learner passes (80% or the page's own "Passed" verdict),
 * a "Get your certificate" panel appears under the result. The learner types the name to print; the certificate is
 * drawn in the browser (canvas) and can be saved as an image or printed / saved as PDF.
 * No account or login. The certificate is registered at /api/certs (name, track, date, score), so its QR code opens
 * /verify?c=<code>; offline or when registration fails, the learner still gets an unregistered copy without a QR code.
 * It is a self-study certificate of completion, NOT CPD-accredited, and says so on its face.
 *
 * Edit this file; tools/academy/apply_certificate.py bundles it after assets/vendor/qrcode-generator.js (MIT) and
 * fingerprints the bundle (assets/academy-certificate.<hash>.js) and tags
 * the end-of-course examination pages.
 */
(function () {
  "use strict";
  var result = document.getElementById("nc-result");
  var form = document.getElementById("nc-quiz");
  if (!result || !form) return;

  var PASS = 0.8;
  var DISTINCTION = 0.95;   // 38 of 40 or better: "with distinction"
  var MEDAL = '<svg class="rcm-cert-medal" viewBox="0 0 64 64" aria-hidden="true"><path d="M20 4h10l6 18h-10z" fill="#1a6b72"/><path d="M44 4H34l-6 18h10z" fill="#1b2f55"/>' +
    '<circle cx="32" cy="40" r="20" fill="#d2ad52" stroke="#9c7422" stroke-width="2"/><circle cx="32" cy="40" r="14" fill="none" stroke="#fff3c4" stroke-width="1.5"/>' +
    '<path d="M32 30l3 6.2 6.8.9-5 4.7 1.3 6.7L32 45.3l-6.1 3.2 1.3-6.7-5-4.7 6.8-.9z" fill="#fff8e1"/></svg>';
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // A short burst of confetti over the panel (skipped for reduced motion and E-paper).
  function celebrate(host) {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches || document.documentElement.getAttribute("data-shade") === "epaper") return;
    var cv = document.createElement("canvas"), r = host.getBoundingClientRect();
    cv.className = "rcm-confetti"; cv.setAttribute("aria-hidden", "true");
    var dpr = Math.min(2, window.devicePixelRatio || 1), w = innerWidth, h = innerHeight;
    cv.width = w * dpr; cv.height = h * dpr; document.body.appendChild(cv);
    var ctx = cv.getContext("2d"); ctx.scale(dpr, dpr);
    var cols = ["#d2ad52", "#f3dc94", "#1a6b72", "#1b2f55", "#c55a11", "#4fb3b8"], ps = [];
    var ox = Math.max(40, Math.min(w - 40, r.left + r.width / 2)), oy = Math.max(60, Math.min(h - 60, r.top + 40));
    for (var i = 0; i < 140; i++) {
      var a = -Math.PI / 2 + (Math.random() - 0.5) * 2.2, v = 7 + Math.random() * 9;
      ps.push({ x: ox, y: oy, vx: Math.cos(a) * v, vy: Math.sin(a) * v, s: 5 + Math.random() * 6, r: Math.random() * 6,
                vr: (Math.random() - 0.5) * 0.4, c: cols[i % cols.length] });
    }
    var t0 = performance.now();
    (function tick(t) {
      var el = t - t0; ctx.clearRect(0, 0, w, h);
      ps.forEach(function (p) {
        p.vy += 0.32; p.vx *= 0.99; p.x += p.vx; p.y += p.vy; p.r += p.vr;
        ctx.save(); ctx.globalAlpha = Math.max(0, 1 - el / 2600); ctx.translate(p.x, p.y); ctx.rotate(p.r);
        ctx.fillStyle = p.c; ctx.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); ctx.restore();
      });
      if (el < 2600) requestAnimationFrame(tick); else cv.remove();
    })(t0);
  }
  var API = "/api/certs", VERIFY = "https://renalcarematters.com/verify?c=";
  var me = document.currentScript;
  var STUDY_MIN = me ? +me.getAttribute("data-study-min") || 0 : 0;

  // Time on the examination: from the first answer to "Check answers" (a new set of questions restarts it).
  var started = 0, examMin = 0;
  form.addEventListener("change", function () { if (!started) started = Date.now(); });
  form.addEventListener("submit", function () { if (started) examMin = Math.max(1, Math.round((Date.now() - started) / 60000)); }, true);
  form.addEventListener("click", function (e) { if (e.target.closest("[data-nc-newset]")) { started = 0; examMin = 0; } });
  function hm(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return (h ? h + (h === 1 ? " hour" : " hours") : "") + (h && m ? " " : "") + (m ? m + " minutes" : "");
  }
  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    "November", "December"];

  function txt(el) { return el ? (el.textContent || "").replace(/\s+/g, " ").trim() : ""; }

  // Track name: the last link in the breadcrumb (the track hub), e.g. "Dialysis Technician".
  function trackName() {
    var links = document.querySelectorAll(".nc-bar a");
    var a = links[links.length - 1];
    return a && a.getAttribute("href") !== "./" ? txt(a) : txt(document.querySelector("h1"));
  }
  function moduleCount() {
    var given = me ? +me.getAttribute("data-modules") || 0 : 0;   // module pages counted by the patcher
    if (given) return given;
    var n = 0;
    document.querySelectorAll("#about table tbody tr").forEach(function (r) {
      if (/^\s*\d+\s*$/.test(txt(r.cells[0]))) n++;   // numbered module rows only, not the Total row
    });
    return n;
  }

  // Did the learner pass? Use the page's own verdict when it gives one (nursing exams have safety-critical items).
  function passed() {
    var t = txt(result);
    if (/not yet passed/i.test(t)) return null;
    var m = t.match(/(\d+)\s+of\s+(\d+)/);
    if (!m) return null;
    var score = +m[1], total = +m[2];
    if (!total) return null;
    if (/\bpassed\b/i.test(t) || score / total >= PASS) return { score: score, total: total };
    return null;
  }

  /* ---------- module quiz progress (recorded by academy-progress.js on each module page) ---------- */
  var PKEY = "rcm-cert-progress";
  var TRACK = location.pathname.split("/").pop().replace(/\.html$/, "").replace(/-final-exam$/, "");
  var MODS = [];
  try { MODS = JSON.parse((document.getElementById("rcm-cert-modules") || {}).textContent || "[]"); } catch (e) {}
  function pload() { try { return JSON.parse(localStorage.getItem(PKEY) || "{}") || {}; } catch (e) { return {}; } }
  function psave(o) { try { localStorage.setItem(PKEY, JSON.stringify(o)); } catch (e) {} }
  // Module results the course script remembered on this device before the certificate existed.
  (function importRemembered() {
    try {
      var store = document.documentElement.getAttribute("data-nc-store") ||
        (document.body.getAttribute("data-course") ? "rcm-course-" + document.body.getAttribute("data-course") + "-progress" : "");
      var prev = store && JSON.parse(localStorage.getItem(store) || "null");
      if (!prev || !prev.modules) return;
      var o = pload(), t = o[TRACK] || (o[TRACK] = {}), changed = false;
      Object.keys(prev.modules).forEach(function (k) {
        var mm = k.match(/(\d\d)$/), r = prev.modules[k];
        if (!mm || k === "exam" || !r || !r.total || t[mm[1]]) return;
        t[mm[1]] = { s: +r.score, t: +r.total, p: +r.score >= Math.ceil(r.total * 0.8), d: String(r.date || "").slice(0, 10) };
        changed = true;
      });
      if (changed) psave(o);
    } catch (e) {}
  })();
  function progress() {
    var t = pload()[TRACK] || {}, done = 0;
    var list = MODS.map(function (m) { var r = t[m[0]]; if (r && r.p) done++; return { nn: m[0], title: m[1], href: m[2], r: r }; });
    return { list: list, done: done, total: list.length, all: !list.length || done === list.length, exam: t._exam || null };
  }
  function recordExam(p) {
    var o = pload(), t = o[TRACK] || (o[TRACK] = {}), old = t._exam;
    if (!old || p.score / p.total > old.s / old.t || (p.score / p.total === old.s / old.t && examMin && (!old.m || examMin < old.m)))
      t._exam = { s: p.score, t: p.total, d: today().iso, m: examMin || (old && old.m) || 0 };
    psave(o);
  }

  function today() {
    var d = new Date();
    return { text: MONTHS[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear(),
             iso: d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) };
  }

  // A short certificate code from the name, track, date and score (SHA-256, first 8 hex digits).
  function code(name, track, iso, score, total) {
    var raw = [name.toLowerCase(), track, iso, score + "/" + total].join("|");
    var initials = track.split(/\s+/).map(function (w) { return w.charAt(0); }).join("").toUpperCase().replace(/[^A-Z]/g, "").slice(0, 4) || "X";
    var fallback = function () {
      var h = 5381; for (var i = 0; i < raw.length; i++) h = ((h << 5) + h + raw.charCodeAt(i)) >>> 0;
      return Promise.resolve(("00000000" + h.toString(16)).slice(-8));
    };
    var p = (window.crypto && crypto.subtle && window.TextEncoder)
      ? crypto.subtle.digest("SHA-256", new TextEncoder().encode(raw)).then(function (buf) {
          return Array.prototype.map.call(new Uint8Array(buf).slice(0, 4), function (b) { return ("0" + b.toString(16)).slice(-2); }).join("");
        }, fallback)
      : fallback();
    return p.then(function (hex) { return "RCA-" + initials + "-" + iso.replace(/-/g, "").slice(2) + "-" + hex.toUpperCase(); });
  }

  /* ---------- drawing ---------- */
  var W = 2000, H = 1414;   // A4 landscape proportions
  var NAVY = "#1b2f55", TEAL = "#1a6b72", GOLD = "#b08a2e", GOLD2 = "#d9b862", INK = "#1e2a38", MUTED = "#5a6678";
  var SANS = "Inter, Manrope, 'Helvetica Neue', Arial, sans-serif";
  var SERIF = "Georgia, 'Times New Roman', 'Noto Serif', serif";

  function fit(ctx, text, maxW, size, weight, family) {
    var s = size;
    do { ctx.font = weight + " " + s + "px " + family; if (ctx.measureText(text).width <= maxW) break; s -= 2; } while (s > 18);
    return s;
  }
  function wrap(ctx, text, x, y, maxW, lineH) {
    var words = text.split(" "), line = "", lines = [];
    words.forEach(function (w) {
      var t = line ? line + " " + w : w;
      if (ctx.measureText(t).width > maxW && line) { lines.push(line); line = w; } else line = t;
    });
    if (line) lines.push(line);
    lines.forEach(function (l, i) { ctx.fillText(l, x, y + i * lineH); });
    return lines.length;
  }
  // Letter-spaced text, centered on x.
  function spaced(ctx, text, x, y, gap) {
    var w = 0, i;
    for (i = 0; i < text.length; i++) w += ctx.measureText(text[i]).width + (i ? gap : 0);
    var cx = x - w / 2, al = ctx.textAlign; ctx.textAlign = "left";
    for (i = 0; i < text.length; i++) { ctx.fillText(text[i], cx, y); cx += ctx.measureText(text[i]).width + gap; }
    ctx.textAlign = al;
    return w;
  }
  // Text set around a circle (top arc), centered at angle -90°.
  function arcText(ctx, text, cx, cy, r, gap) {
    var widths = [], total = 0, i;
    for (i = 0; i < text.length; i++) { widths.push(ctx.measureText(text[i]).width); total += widths[i] + gap; }
    var a = -Math.PI / 2 - total / r / 2;
    ctx.save(); ctx.textAlign = "center"; ctx.textBaseline = "middle";
    for (i = 0; i < text.length; i++) {
      var aw = (widths[i] + gap) / r;
      ctx.save(); ctx.translate(cx + r * Math.cos(a + aw / 2), cy + r * Math.sin(a + aw / 2)); ctx.rotate(a + aw / 2 + Math.PI / 2);
      ctx.fillText(text[i], 0, 0); ctx.restore();
      a += aw;
    }
    ctx.restore();
  }
  // Interlaced sine waves along a straight edge (guilloche band).
  function wave(ctx, x1, y1, x2, y2, amp, period) {
    var len = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / len, uy = (y2 - y1) / len, nx = -uy, ny = ux;
    [0, Math.PI].forEach(function (ph) {
      ctx.beginPath();
      for (var t = 0; t <= len; t += 2) {
        var o = amp * Math.sin(2 * Math.PI * t / period + ph);
        var px = x1 + ux * t + nx * o, py = y1 + uy * t + ny * o;
        t ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
      }
      ctx.stroke();
    });
  }
  // Guilloche rosette: elliptical petals that all pass through the center, so it has no hollow disc.
  function rosette(ctx, cx, cy, R, n, alpha) {
    ctx.save(); ctx.translate(cx, cy); ctx.strokeStyle = "rgba(176,138,46," + alpha + ")"; ctx.lineWidth = 1.3;
    for (var i = 0; i < n; i++) {
      ctx.rotate(2 * Math.PI / n);
      ctx.beginPath(); ctx.ellipse(R / 2, 0, R / 2, R * 0.16, 0, 0, 2 * Math.PI); ctx.stroke();
    }
    ctx.restore();
  }
  function diamond(ctx, x, y, r, fill, stroke) {
    ctx.beginPath(); ctx.moveTo(x, y - r); ctx.lineTo(x + r, y); ctx.lineTo(x, y + r); ctx.lineTo(x - r, y); ctx.closePath();
    ctx.fillStyle = fill; ctx.fill(); if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 2; ctx.stroke(); }
  }
  function goldGrad(ctx, x, y, r) {
    var g = ctx.createRadialGradient(x - r * 0.3, y - r * 0.35, r * 0.1, x, y, r);
    g.addColorStop(0, "#f3dc94"); g.addColorStop(0.55, "#d2ad52"); g.addColorStop(1, "#9c7422");
    return g;
  }

  function seal(ctx, cx, cy, year) {
    var R = 104;
    // ribbon tails
    ctx.fillStyle = NAVY;
    [[-1], [1]].forEach(function (s) {
      var k = s[0];
      ctx.beginPath(); ctx.moveTo(cx + k * 30, cy + 40); ctx.lineTo(cx + k * 78, cy + 168); ctx.lineTo(cx + k * 56, cy + 150);
      ctx.lineTo(cx + k * 40, cy + 176); ctx.lineTo(cx + k * 4, cy + 58); ctx.closePath(); ctx.fill();
    });
    ctx.fillStyle = TEAL;
    [[-1], [1]].forEach(function (s) {
      var k = s[0];
      ctx.beginPath(); ctx.moveTo(cx + k * 22, cy + 52); ctx.lineTo(cx + k * 56, cy + 150); ctx.lineTo(cx + k * 40, cy + 176);
      ctx.lineTo(cx + k * 10, cy + 70); ctx.closePath(); ctx.fill();
    });
    // scalloped gold edge
    ctx.save(); ctx.shadowColor = "rgba(60,40,0,.28)"; ctx.shadowBlur = 14; ctx.shadowOffsetY = 4;
    ctx.beginPath();
    for (var i = 0; i <= 96; i++) {
      var a = i / 96 * 2 * Math.PI, rr = i % 2 ? R - 7 : R;
      i ? ctx.lineTo(cx + rr * Math.cos(a), cy + rr * Math.sin(a)) : ctx.moveTo(cx + rr, cy);
    }
    ctx.closePath(); ctx.fillStyle = goldGrad(ctx, cx, cy, R); ctx.fill(); ctx.restore();
    ctx.strokeStyle = "rgba(255,248,220,.85)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(cx, cy, R - 16, 0, 2 * Math.PI); ctx.stroke();
    ctx.strokeStyle = "rgba(110,80,20,.55)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(cx, cy, R - 21, 0, 2 * Math.PI); ctx.stroke();
    // navy center
    ctx.fillStyle = NAVY; ctx.beginPath(); ctx.arc(cx, cy, 56, 0, 2 * Math.PI); ctx.fill();
    ctx.strokeStyle = GOLD2; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, 50, 0, 2 * Math.PI); ctx.stroke();
    ctx.fillStyle = "#4a3410"; ctx.font = "700 15px " + SANS;
    arcText(ctx, "RENAL CARE ACADEMY", cx, cy, R - 36, 3.2);
    // lower arc: draw rotated by 180° so it reads left-to-right along the bottom
    ctx.save(); ctx.translate(cx, cy); ctx.rotate(Math.PI);
    ctx.font = "700 13px " + SANS; arcTextInner(ctx, "· SELF-STUDY ·", 0, 0, R - 36, 3); ctx.restore();
    ctx.fillStyle = "#f3dc94"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.font = "700 34px " + SERIF; ctx.fillText("RCA", cx, cy - 8);
    ctx.font = "600 15px " + SANS; ctx.fillText(String(year), cx, cy + 24);
    ctx.textBaseline = "alphabetic";
  }
  // Bottom arc text: drawn on the top arc of a canvas rotated 180°, characters flipped so they stand upright.
  function arcTextInner(ctx, text, cx, cy, r, gap) {
    var widths = [], total = 0, i;
    for (i = 0; i < text.length; i++) { widths.push(ctx.measureText(text[i]).width); total += widths[i] + gap; }
    var a = -Math.PI / 2 + total / r / 2;
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    for (i = 0; i < text.length; i++) {
      var aw = (widths[i] + gap) / r;
      ctx.save(); ctx.translate(cx + r * Math.cos(a - aw / 2), cy + r * Math.sin(a - aw / 2)); ctx.rotate(a - aw / 2 - Math.PI / 2);
      ctx.fillText(text[i], 0, 0); ctx.restore();
      a -= aw;
    }
  }

  function draw(canvas, d) {
    var ctx = canvas.getContext("2d");
    canvas.width = W; canvas.height = H;
    // paper
    var bg = ctx.createRadialGradient(W / 2, H / 2, 200, W / 2, H / 2, 1200);
    bg.addColorStop(0, "#fffdf6"); bg.addColorStop(1, "#f4ecd8");
    ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
    rosette(ctx, W / 2, 640, 540, 72, 0.07);

    // frame: navy outer, gold rules, guilloche band, corner diamonds
    ctx.strokeStyle = NAVY; ctx.lineWidth = 20; ctx.strokeRect(30, 30, W - 60, H - 60);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.5; ctx.strokeRect(56, 56, W - 112, H - 112);
    ctx.strokeStyle = "rgba(176,138,46,.75)"; ctx.lineWidth = 1.3;
    var b = 74;
    wave(ctx, b, b, W - b, b, 9, 26); wave(ctx, b, H - b, W - b, H - b, 9, 26);
    wave(ctx, b, b, b, H - b, 9, 26); wave(ctx, W - b, b, W - b, H - b, 9, 26);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.5; ctx.strokeRect(92, 92, W - 184, H - 184);
    ctx.lineWidth = 1; ctx.strokeRect(100, 100, W - 200, H - 200);
    [[b, b], [W - b, b], [b, H - b], [W - b, H - b]].forEach(function (c) { diamond(ctx, c[0], c[1], 20, NAVY, GOLD2); diamond(ctx, c[0], c[1], 7, GOLD2); });

    ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    // academy line with rules
    ctx.fillStyle = NAVY; ctx.font = "700 26px " + SANS;
    var aw = spaced(ctx, "RENAL CARE ACADEMY", W / 2, 196, 7);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(W / 2 - aw / 2 - 150, 187); ctx.lineTo(W / 2 - aw / 2 - 30, 187);
    ctx.moveTo(W / 2 + aw / 2 + 30, 187); ctx.lineTo(W / 2 + aw / 2 + 150, 187); ctx.stroke();
    diamond(ctx, W / 2 - aw / 2 - 158, 187, 5, GOLD); diamond(ctx, W / 2 + aw / 2 + 158, 187, 5, GOLD);
    ctx.fillStyle = MUTED; ctx.font = "500 21px " + SANS;
    spaced(ctx, "RENALCAREMATTERS.COM", W / 2, 232, 4);

    // title
    ctx.fillStyle = NAVY; ctx.font = "400 104px " + SERIF;
    spaced(ctx, "CERTIFICATE", W / 2, 360, 16);
    ctx.fillStyle = GOLD; ctx.font = "italic 400 50px " + SERIF;
    ctx.fillText("of Completion", W / 2, 428);

    ctx.fillStyle = MUTED; ctx.font = "italic 400 34px " + SERIF;
    ctx.fillText("This is to certify that", W / 2, 510);

    // name
    ctx.fillStyle = INK;
    var ns = fit(ctx, d.name, 1360, 96, "italic 700", SERIF);
    ctx.font = "italic 700 " + ns + "px " + SERIF; ctx.fillText(d.name, W / 2, 610);
    var g = ctx.createLinearGradient(W / 2 - 560, 0, W / 2 + 560, 0);
    g.addColorStop(0, "rgba(176,138,46,0)"); g.addColorStop(0.15, GOLD); g.addColorStop(0.85, GOLD); g.addColorStop(1, "rgba(176,138,46,0)");
    ctx.strokeStyle = g; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(W / 2 - 560, 648); ctx.lineTo(W / 2 + 560, 648); ctx.stroke();
    diamond(ctx, W / 2, 648, 8, GOLD);

    ctx.fillStyle = INK; ctx.font = "400 32px " + SANS;
    var course = "has completed the " + (d.modules ? d.modules + "-module " : "") + "self-study course" +
      (d.studyMin ? " (an estimated " + d.studyMin + " minutes of study)" : "");
    fit(ctx, course, 1500, 32, "400", SANS); ctx.fillText(course, W / 2, 718);
    ctx.fillStyle = NAVY;
    var ts = fit(ctx, d.track, 1500, 60, "800", SANS);
    ctx.font = "800 " + ts + "px " + SANS; ctx.fillText(d.track, W / 2, 796);
    ctx.fillStyle = INK; ctx.font = "400 30px " + SANS;
    var what = "and passed its end-of-course examination with " + d.score + " of " + d.total + " best answers (" +
      Math.round(100 * d.score / d.total) + "%)" + (d.examMin ? " in " + d.examMin + (d.examMin === 1 ? " minute." : " minutes.") : ".");
    wrap(ctx, what, W / 2, 856, 1420, 42);
    if (d.score / d.total >= DISTINCTION) {
      ctx.fillStyle = GOLD; ctx.font = "italic 700 34px " + SERIF; ctx.fillText("— with Distinction —", W / 2, 904);
    }

    // bottom left: date and study time
    function field(x, y, value, label) {
      ctx.fillStyle = INK; fit(ctx, value, 440, 32, "600", SANS); ctx.fillText(value, x, y);
      ctx.strokeStyle = "rgba(27,47,85,.35)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(x - 220, y + 18); ctx.lineTo(x + 220, y + 18); ctx.stroke();
      ctx.fillStyle = MUTED; ctx.font = "600 19px " + SANS; spaced(ctx, label.toUpperCase(), x, y + 50, 2.5);
    }
    var LX = 470, RX = W - 470;
    if (d.signoff) {
      field(LX, 960, d.date, "Date completed");
      // Blank line for a hand signature on the printed copy (about 13 mm of writing space above it).
      ctx.strokeStyle = INK; ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(LX - 250, 1150); ctx.lineTo(LX + 250, 1150); ctx.stroke();
      ctx.fillStyle = MUTED; ctx.font = "600 18px " + SANS; spaced(ctx, "PRECEPTOR SIGNATURE OVER PRINTED NAME", LX, 1178, 1.6);
      ctx.font = "500 18px " + SANS; ctx.fillText("Unit and date signed: ______________________", LX, 1208);
    } else {
      field(LX, 1010, d.date, "Date completed");
    }

    // center seal
    seal(ctx, W / 2, 1052, d.iso.slice(0, 4));

    // bottom right: QR + code, or code only
    var qr = d.verified ? qrMatrix(VERIFY + d.code) : null;
    if (qr) {
      var size = 150, x = RX - size / 2, y = 918, n = qr.length, cell = size / n;
      ctx.fillStyle = "#ffffff"; ctx.fillRect(x - 8, y - 8, size + 16, size + 16);
      ctx.strokeStyle = GOLD; ctx.lineWidth = 2; ctx.strokeRect(x - 8, y - 8, size + 16, size + 16);
      ctx.fillStyle = "#111827";
      for (var r = 0; r < n; r++) for (var c = 0; c < n; c++)
        if (qr[r][c]) ctx.fillRect(Math.floor(x + c * cell), Math.floor(y + r * cell), Math.ceil(cell), Math.ceil(cell));
      ctx.fillStyle = INK; ctx.font = "700 24px " + SANS; ctx.fillText(d.code, RX, 1118);
      ctx.fillStyle = MUTED; ctx.font = "600 19px " + SANS; spaced(ctx, "SCAN TO VERIFY", RX, 1148, 2.5);
    } else {
      field(RX, 990, d.code, "Certificate code");
      ctx.fillStyle = MUTED; ctx.font = "italic 400 20px " + SERIF; ctx.fillText("Not registered for online verification", RX, 1074);
    }

    // fine print
    ctx.fillStyle = MUTED; ctx.font = "400 20px " + SANS;
    wrap(ctx, "Self-study certificate of completion, issued on passing the online end-of-course examination. Not CPD-accredited. " +
      "Competence is demonstrated on the learner's own unit and signed off by a preceptor." +
      (qr ? " Verify at renalcarematters.com/verify." : ""), W / 2, 1252, 1480, 30);
  }

  /* ---------- record of module results (page 2 of the completion packet, or the progress record) ---------- */
  var SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  function shortDate(iso) {
    var p = String(iso || "").split("-");
    return p.length === 3 ? SHORT[+p[1] - 1] + " " + +p[2] + ", " + p[0] : "";
  }
  function ellipsize(ctx, text, maxW) {
    if (ctx.measureText(text).width <= maxW) return text;
    while (text.length > 4 && ctx.measureText(text + "…").width > maxW) text = text.slice(0, -1);
    return text.replace(/[\s,:;]+$/, "") + "…";
  }

  // mode "complete": issued with the certificate (code, QR). mode "progress": not a certificate.
  function drawRecord(canvas, d, pr, mode) {
    var ctx = canvas.getContext("2d"), done = mode === "complete";
    canvas.width = W; canvas.height = H;
    var bg = ctx.createRadialGradient(W / 2, H / 2, 200, W / 2, H / 2, 1200);
    bg.addColorStop(0, "#fffdf6"); bg.addColorStop(1, "#f4ecd8");
    ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = NAVY; ctx.lineWidth = 16; ctx.strokeRect(30, 30, W - 60, H - 60);
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.5; ctx.strokeRect(58, 58, W - 116, H - 116);
    ctx.lineWidth = 1; ctx.strokeRect(66, 66, W - 132, H - 132);
    if (!done) {   // diagonal watermark so a progress record can never pass for a certificate
      ctx.save(); ctx.translate(W / 2, H / 2 + 60); ctx.rotate(-0.32);
      ctx.fillStyle = "rgba(180,83,9,.075)"; ctx.font = "800 150px " + SANS; ctx.textAlign = "center";
      ctx.fillText("NOT A CERTIFICATE", 0, 0); ctx.restore();
    }

    ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.fillStyle = NAVY; ctx.font = "700 24px " + SANS; spaced(ctx, "RENAL CARE ACADEMY", W / 2, 140, 6);
    ctx.fillStyle = NAVY; ctx.font = "400 62px " + SERIF;
    ctx.fillText(done ? "Record of Module Results" : "Progress Record", W / 2, 222);
    if (done) {
      ctx.fillStyle = GOLD; ctx.font = "italic 400 28px " + SERIF;
      ctx.fillText("Issued with certificate " + d.code, W / 2, 268);
    } else {
      var tag = "IN PROGRESS · NOT A CERTIFICATE";
      ctx.font = "800 22px " + SANS; var tw = ctx.measureText(tag).width + 26 * 2.4 + 48;
      ctx.fillStyle = "#b45309"; ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(W / 2 - tw / 2, 240, tw, 40, 20); else ctx.rect(W / 2 - tw / 2, 240, tw, 40);
      ctx.fill(); ctx.fillStyle = "#ffffff"; spaced(ctx, tag, W / 2, 268, 2.4);
    }

    // who and what
    ctx.fillStyle = INK; ctx.font = "italic 700 40px " + SERIF; ctx.fillText(d.name, W / 2, 334);
    ctx.fillStyle = MUTED; ctx.font = "500 24px " + SANS;
    ctx.fillText(d.track + " · " + pr.total + "-module self-study course" + (d.studyMin ? " · an estimated " + d.studyMin + " minutes of study" : ""), W / 2, 372);
    ctx.fillStyle = INK; ctx.font = "600 25px " + SANS;
    var ex = pr.exam;
    var summary = pr.done + " of " + pr.total + " module quizzes passed · End-of-course examination: " +
      (ex ? ex.s + " of " + ex.t + " (" + Math.round(100 * ex.s / ex.t) + "%), " + shortDate(ex.d) + (ex.m ? ", " + ex.m + " min" : "") : "not yet passed");
    fit(ctx, summary, W - 300, 25, "600", SANS); ctx.fillText(summary, W / 2, 414);

    // table: one column up to 16 modules, two columns beyond
    var n = pr.list.length, cols = n > 16 ? 2 : 1, per = Math.ceil(n / cols), x0 = 120, tw2 = W - 240, gap = 40;
    var cw = (tw2 - gap * (cols - 1)) / cols, rowH = Math.min(46, Math.floor(700 / Math.max(per, 1))), top = 452;
    for (var c = 0; c < cols; c++) {
      var cx = x0 + c * (cw + gap);
      ctx.fillStyle = NAVY; ctx.fillRect(cx, top, cw, 38);
      ctx.fillStyle = "#ffffff"; ctx.font = "700 17px " + SANS; ctx.textAlign = "left";
      ctx.fillText("MODULE", cx + 14, top + 25);
      ctx.textAlign = "right"; ctx.fillText("QUIZ", cx + cw - 196, top + 25); ctx.fillText(done ? "PASSED ON" : "STATUS", cx + cw - 14, top + 25);
      for (var i = 0; i < per; i++) {
        var m = pr.list[c * per + i]; if (!m) break;
        var y = top + 38 + i * rowH, r = m.r, ok = r && r.p;
        if (i % 2) { ctx.fillStyle = "rgba(176,138,46,.08)"; ctx.fillRect(cx, y, cw, rowH); }
        ctx.strokeStyle = "rgba(27,47,85,.14)"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(cx, y + rowH); ctx.lineTo(cx + cw, y + rowH); ctx.stroke();
        var ty = y + rowH / 2 + 7, fs = rowH < 40 ? 18 : 20;
        ctx.textAlign = "center"; ctx.font = "800 " + (fs + 2) + "px " + SANS;
        ctx.fillStyle = ok ? "#2e6b3e" : r ? "#b45309" : "#9aa3b2"; ctx.fillText(ok ? "✓" : r ? "!" : "○", cx + 22, ty);
        ctx.textAlign = "left"; ctx.fillStyle = INK; ctx.font = "600 " + fs + "px " + SANS;
        var label = ellipsize(ctx, +m.nn + ". " + m.title, cw - 300); ctx.fillText(label, cx + 44, ty);
        ctx.textAlign = "right"; ctx.font = "600 " + fs + "px " + SANS; ctx.fillStyle = ok ? INK : MUTED;
        ctx.fillText(r ? r.s + "/" + r.t : "—", cx + cw - 196, ty);
        ctx.fillStyle = ok ? INK : r ? "#b45309" : MUTED; ctx.font = (ok ? "500 " : "italic 500 ") + fs + "px " + SANS;
        ctx.fillText(ok ? shortDate(r.d) : r ? "Not yet passed" : "Not taken", cx + cw - 14, ty);
      }
    }

    // footer
    ctx.textAlign = "center"; ctx.fillStyle = MUTED; ctx.font = "400 19px " + SANS;
    var foot = done
      ? "Module quiz results recorded on the learner's device when each quiz was passed (best result shown). Self-study; not CPD-accredited. " +
        "Competence is demonstrated on the learner's own unit and signed off by a preceptor." + (d.verified ? " Verify at renalcarematters.com/verify." : "")
      : "Progress record printed " + d.date + ". This is not a certificate of completion: the certificate is issued only after every module quiz " +
        "and the end-of-course examination are passed. Results are recorded on the learner's device.";
    var qr = done && d.verified ? qrMatrix(VERIFY + d.code) : null;
    wrap(ctx, foot, qr ? W / 2 - 80 : W / 2, 1268, qr ? 1460 : 1640, 28);
    if (qr) {
      var size = 100, qx = W - 136 - size, qy = 1206, nq = qr.length, cell = size / nq;
      ctx.fillStyle = "#fff"; ctx.fillRect(qx - 6, qy - 6, size + 12, size + 12);
      ctx.fillStyle = "#111827";
      for (var a = 0; a < nq; a++) for (var b = 0; b < nq; b++)
        if (qr[a][b]) ctx.fillRect(Math.floor(qx + b * cell), Math.floor(qy + a * cell), Math.ceil(cell), Math.ceil(cell));
    }
  }

  // QR code (qrcode-generator, MIT, bundled ahead of this script): returns a boolean matrix, quiet zone included.
  function qrMatrix(text) {
    if (typeof qrcode !== "function") return null;
    var q = qrcode(0, "M"); q.addData(text); q.make();
    var n = q.getModuleCount(), pad = 2, m = [];
    for (var r = -pad; r < n + pad; r++) {
      var row = [];
      for (var c = -pad; c < n + pad; c++) row.push(r >= 0 && c >= 0 && r < n && c < n && q.isDark(r, c));
      m.push(row);
    }
    return m;
  }

  /* ---------- UI ---------- */
  var panel = null, modal = null;
  var css = document.createElement("style");
  css.textContent = [
    ".rcm-cert{margin-top:14px;padding:16px 18px;border-radius:12px;border:1px solid #b8892b;background:#fff8e6;color:#1e2a38}",
    ".rcm-cert h3{margin:0;font:800 20px/1.25 Inter,Manrope,sans-serif;color:#1f3864}",
    ".rcm-cert-hd{display:flex;align-items:center;gap:12px;margin-bottom:10px}.rcm-cert-medal{width:54px;height:54px;flex:none;animation:rcmPop .6s cubic-bezier(.2,1.6,.4,1) both}",
    ".rcm-cert-kicker{font:800 12.5px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8a6312;margin-bottom:4px}",
    ".rcm-cert{animation:rcmRise .5s ease-out both;box-shadow:0 10px 28px rgba(176,138,46,.22)}",
    "@keyframes rcmPop{0%{transform:scale(.2) rotate(-20deg);opacity:0}100%{transform:none;opacity:1}}",
    "@keyframes rcmRise{0%{transform:translateY(10px);opacity:0}100%{transform:none;opacity:1}}",
    "@media (prefers-reduced-motion:reduce){.rcm-cert,.rcm-cert-medal{animation:none}}",
    ".rcm-confetti{position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483001}",
    "html[data-theme='dark'] .rcm-cert-kicker{color:#f3c46a}",
    ".rcm-cert p{text-align:left!important;hyphens:none!important;margin:0 0 10px;font-size:14.5px;line-height:1.55}",
    ".rcm-cert-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}",
    ".rcm-cert input[type=text]{flex:1 1 240px;min-width:0;font:600 16px Inter,sans-serif;padding:10px 12px;border-radius:10px;border:1px solid #9aa3b2;background:#fff;color:#1e2a38}",
    ".rcm-cert button,.rcm-certm button{font:700 15px Inter,sans-serif;padding:10px 16px;border-radius:999px;border:2px solid #1f3864;background:#1f3864;color:#fff;cursor:pointer}",
    ".rcm-certm button.ghost{background:transparent;color:#1f3864}",
    ".rcm-cert-check{margin:0 0 18px;border:1px solid #d9c592;border-radius:12px;background:#fffbef;color:#1e2a38}",
    ".rcm-cert-check summary{display:flex;gap:12px;align-items:center;padding:12px 14px;cursor:pointer;list-style:none}",
    ".rcm-cert-check summary::-webkit-details-marker{display:none}",
    ".rcm-cert-check b{font:800 15.5px Inter,sans-serif;color:#1f3864}.rcm-cc-sub{font-size:13.5px;color:#5a6678}",
    ".rcm-cc-ring{width:34px;height:34px;flex:none;border-radius:50%;background:conic-gradient(#2e6b3e calc(var(--p)*1%),#e6e0cc 0)}",
    ".rcm-cert-check ol{margin:0;padding:4px 14px 6px 14px;list-style:none;border-top:1px solid #eadfbf}",
    ".rcm-cert-check li{display:grid;grid-template-columns:22px 1fr auto;gap:8px;align-items:baseline;padding:6px 0;border-bottom:1px solid #f0e8d2;font-size:14px}",
    ".rcm-cert-check li:last-child{border-bottom:0}.rcm-cc-mk{font-weight:800;color:#2e6b3e;text-align:center}.rcm-cert-check li.try .rcm-cc-mk{color:#b45309}",
    ".rcm-cc-sc{font-size:12.5px;color:#5a6678;white-space:nowrap}.rcm-cert-check li.ok .rcm-cc-sc{color:#2e6b3e;font-weight:700}",
    ".rcm-cert a,.rcm-cert-check a{color:#1a6b72}html[data-theme='dark'] .rcm-cert a,html[data-theme='dark'] .rcm-cert-check a{color:#7fd0d6}",
    ".rcm-cc-note{hyphens:none!important;margin:0!important;padding:8px 14px 12px;font-size:12.5px!important;color:#5a6678;text-align:left!important}",
    ".rcm-cc-prog{display:flex;flex-wrap:wrap;gap:8px;padding:10px 14px 0}",
    ".rcm-cc-prog input{flex:1 1 200px;min-width:0;font:600 15px Inter,sans-serif;padding:8px 11px;border-radius:9px;border:1px solid #9aa3b2;background:#fff;color:#1e2a38}",
    ".rcm-cc-prog button{font:700 14px Inter,sans-serif;padding:8px 14px;border-radius:999px;border:2px solid #1f3864;background:#fff;color:#1f3864;cursor:pointer}",
    "html[data-theme='dark'] .rcm-cc-prog button{background:transparent;border-color:#f3c46a;color:#f3c46a}",
    ".rcm-cert-left{margin:0 0 8px 18px;padding:0;font-size:14.5px;line-height:1.6}.rcm-cert-saved{margin:0 0 18px}",
    "html[data-theme='dark'] .rcm-cert-check{background:#221f15;border-color:#6b5a2c;color:#e8e2d4}",
    "html[data-theme='dark'] .rcm-cert-check b{color:#f3c46a}html[data-theme='dark'] .rcm-cc-sub,html[data-theme='dark'] .rcm-cc-sc,html[data-theme='dark'] .rcm-cc-note{color:#b9b2a2}",
    "html[data-theme='dark'] .rcm-cert-check ol,html[data-theme='dark'] .rcm-cert-check li{border-color:#3a3322}",
    "html[data-theme='dark'] .rcm-cc-mk,html[data-theme='dark'] .rcm-cert-check li.ok .rcm-cc-sc{color:#6fcf8e}html[data-theme='dark'] .rcm-cc-ring{background:conic-gradient(#6fcf8e calc(var(--p)*1%),#3a3322 0)}",
    "@media print{.rcm-cert-check,.rcm-cert-saved{display:none!important}}",
    ".rcm-cert-opt{display:flex;gap:8px;align-items:flex-start;margin-top:10px;font-size:14px;line-height:1.45;cursor:pointer}",
    ".rcm-cert-opt input{width:18px;height:18px;flex:none;margin:1px 0 0;padding:0;accent-color:#1f3864}",
    ".rcm-cert-ts{margin-top:10px}.rcm-cert-ts:empty{display:none}.rcm-cert-msg{margin:10px 0 0!important;font-weight:600}",
    ".rcm-cert button:disabled{opacity:.6;cursor:wait}",
    ".rcm-cert small{display:block;margin-top:8px;color:#5a6678;font-size:12.5px;line-height:1.5}",
    "html[data-theme='dark'] .rcm-cert{background:#2a2414;border-color:#8a6a24;color:#e8e2d4}",
    "html[data-theme='dark'] .rcm-cert button{background:#f3c46a;border-color:#f3c46a;color:#1e2a38}",
    "html[data-theme='dark'] .rcm-cert h3{color:#f3c46a}html[data-theme='dark'] .rcm-cert small{color:#b9b2a2}",
    ".rcm-certm{position:fixed;inset:0;z-index:2147483000;background:rgba(10,18,32,.78);display:flex;align-items:center;justify-content:center;padding:16px}",
    ".rcm-certm-box{background:#fff;border-radius:14px;max-width:980px;width:100%;max-height:100%;overflow:auto;padding:14px;box-shadow:0 20px 50px rgba(0,0,0,.4)}",
    ".rcm-certm img{display:block;width:100%;height:auto;border:1px solid #d6dae1;border-radius:6px}",
    ".rcm-certm-title{font:800 17px Inter,sans-serif;color:#1f3864;margin:2px 2px 10px}",
    ".rcm-certm-pg{margin:0 0 12px}.rcm-certm-pg figcaption{font:600 12.5px Inter,sans-serif;color:#5a6678;margin-top:5px;text-align:center}",
    ".rcm-certm-act{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end;margin-top:12px}",
    "#rcm-cert-print{display:none}",
    "@media print{html.rcm-cert-printing body>*:not(#rcm-cert-print){display:none!important}",
    "html.rcm-cert-printing #rcm-cert-print{display:block!important}html.rcm-cert-printing #rcm-cert-print img{display:block;width:100%;height:auto;break-after:page;page-break-after:always}",
    "html.rcm-cert-printing #rcm-cert-print img:last-child{break-after:auto;page-break-after:auto}",
    "@page{size:A4 landscape;margin:8mm}.rcm-cert{display:none!important}}"
  ].join("\n");
  document.head.appendChild(css);

  // Online registration: GET /api/certs says whether verification is available (and the Turnstile key).
  var cfg = null;
  function config() {
    if (cfg) return cfg;
    cfg = fetch(API, { cache: "no-store" }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
    return cfg;
  }
  var tsWidget = null;
  function turnstile(holder, key) {
    if (!key || tsWidget !== null) return;
    tsWidget = -1;
    window.rcmCertTs = function () {
      try { tsWidget = window.turnstile.render(holder, { sitekey: key, size: "flexible", theme: "auto" }); } catch (e) { tsWidget = null; }
    };
    var sc = document.createElement("script");
    sc.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=rcmCertTs";
    sc.async = true; document.head.appendChild(sc);
  }
  function tsToken() {
    try { if (tsWidget !== null && tsWidget !== -1 && window.turnstile) return window.turnstile.getResponse(tsWidget) || ""; } catch (e) {}
    return "";
  }
  var issued = {};   // name|score|total -> {code, issued}, so tapping twice reuses the same certificate

  function register(d) {
    var k = d.name + "|" + d.score + "|" + d.total;
    if (issued[k]) return Promise.resolve(issued[k]);
    return config().then(function (c) {
      if (!c || !c.ready) return null;
      return fetch(API, {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ name: d.name, track: d.track, exam: location.pathname.split("/").pop().replace(/\.html$/, ""),
          modules: d.modules, modules_passed: progress().done, score: d.score, total: d.total, exam_min: d.examMin, study_min: d.studyMin,
          turnstile: tsToken(), website: "" })
      }).then(function (r) { return r.json().then(function (j) { return r.ok ? j : { error: j.error || "server" }; }); });
    }).then(function (j) {
      if (j && j.code) issued[k] = j;
      return j;
    }, function () { return null; });
  }

  function isoText(iso) {
    var p = iso.split("-");
    return MONTHS[+p[1] - 1] + " " + +p[2] + ", " + p[0];
  }

  function showPanel(p, host) {
    if (panel) panel.remove();
    panel = document.createElement("div");
    panel.className = "rcm-cert";
    panel.innerHTML =
      '<div class="rcm-cert-hd">' + MEDAL + '<div><div class="rcm-cert-kicker">Congratulations!</div>' +
      '<h3>You passed the ' + esc(trackName()) + ' course</h3></div></div>' +
      '<p>' + p.score + ' of ' + p.total + ' best answers (' + Math.round(100 * p.score / p.total) + '%)' +
      (p.score / p.total >= DISTINCTION ? ', <strong>with distinction</strong>' : '') + '. You have earned your certificate of completion. ' +
      'Type your name the way you want it printed, then tap <strong>Make my certificate</strong>.</p>' +
      '<div class="rcm-cert-row"><input type="text" maxlength="70" autocomplete="name" placeholder="Full name, e.g. Juan Dela Cruz" aria-label="Name to print on the certificate">' +
      '<button type="button">Make my certificate</button></div>' +
      '<label class="rcm-cert-opt"><input type="checkbox"> Add a preceptor sign-off line (optional; signed by hand on the printed copy)</label>' +
      '<div class="rcm-cert-ts"></div>' +
      '<p class="rcm-cert-msg" role="status" hidden></p>' +
      '<small>To make the certificate verifiable, your name, the track, the date and your score are saved with its code on ' +
      'renalcarematters.com; anyone who scans its QR code sees them. To have your record removed, use Report a correction ' +
      'on any guide. This is a self-study certificate, not CPD units.</small>';
    (host || result).appendChild(panel);
    celebrate(panel);
    var input = panel.querySelector("input"), btn = panel.querySelector("button"), msg = panel.querySelector(".rcm-cert-msg");
    config().then(function (c) { if (c && c.turnstile) turnstile(panel.querySelector(".rcm-cert-ts"), c.turnstile); });
    function say(t) { msg.textContent = t; msg.hidden = !t; }
    function go() {
      var name = input.value.replace(/\s+/g, " ").trim();
      if (name.length < 2) { input.focus(); input.setAttribute("aria-invalid", "true"); return; }
      input.removeAttribute("aria-invalid");
      btn.disabled = true; say("Making your certificate…");
      var t = today(), track = trackName();
      var d = { name: name, track: track, modules: moduleCount(), score: p.score, total: p.total,
                studyMin: STUDY_MIN, examMin: examMin, date: t.text, iso: t.iso,
                signoff: panel.querySelector(".rcm-cert-opt input").checked };
      register(d).then(function (j) {
        btn.disabled = false;
        if (j && j.code) {
          say(""); d.code = j.code; d.verified = true; d.date = isoText(j.issued); openCert(d); return;
        }
        if (j && j.error === "human_check") { say("Please complete the human check above, then tap Make my certificate again."); return; }
        if (j && j.error === "limit") say("Too many certificates from this connection today, so this copy is not registered for verification.");
        else say("Could not reach the site to register the certificate, so this copy has no QR code. Connect to the internet and tap again for a verifiable one.");
        code(name, track, t.iso, p.score, p.total).then(function (c) { d.code = c; d.verified = false; openCert(d); });
      });
    }
    btn.addEventListener("click", go);
    input.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); go(); } });
  }

  // pages: [{canvas, label, file, alt}] drawn and shown together; saved one by one, printed together.
  function openPacket(title, pages) {
    var ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
    ready.then(function () {
      pages.forEach(function (pg) { pg.draw(pg.canvas); pg.url = pg.canvas.toDataURL("image/png"); });
      if (modal) modal.remove();
      modal = document.createElement("div");
      modal.className = "rcm-certm";
      modal.setAttribute("role", "dialog"); modal.setAttribute("aria-modal", "true"); modal.setAttribute("aria-label", title);
      modal.innerHTML = '<div class="rcm-certm-box"><div class="rcm-certm-title">' + esc(title) + '</div>' +
        pages.map(function (pg, i) {
          return '<figure class="rcm-certm-pg"><img alt="' + esc(pg.alt) + '" src="' + pg.url + '"><figcaption>Page ' + (i + 1) + ' of ' + pages.length + ': ' + esc(pg.label) + '</figcaption></figure>';
        }).join("") + '<div class="rcm-certm-act">' +
        pages.map(function (pg, i) { return '<button type="button" data-a="save" data-i="' + i + '">Save ' + esc(pg.label.toLowerCase()) + '</button>'; }).join("") +
        '<button type="button" data-a="print">Print or save as PDF' + (pages.length > 1 ? " (both pages)" : "") + '</button>' +
        '<button type="button" class="ghost" data-a="close">Close</button></div></div>';
      document.body.appendChild(modal);
      modal.querySelector('[data-a="save"]').focus();
      modal.addEventListener("click", function (e) {
        var a = e.target.closest("[data-a]"); if (e.target === modal) a = { getAttribute: function () { return "close"; } };
        if (!a) return;
        var act = a.getAttribute("data-a"), pg = pages[+a.getAttribute("data-i") || 0];
        if (act === "close") { modal.remove(); modal = null; }
        else if (act === "save") save(pg.canvas, pg.url, pg.file);
        else if (act === "print") printCert(pages.map(function (x) { return x.url; }));
      });
      document.addEventListener("keydown", function esc2(e) {
        if (e.key === "Escape" && modal) { modal.remove(); modal = null; document.removeEventListener("keydown", esc2); }
      });
    });
  }
  function fileName(kind, d) {
    return kind + "-" + d.track.replace(/[^A-Za-z0-9]+/g, "-") + "-" + d.name.replace(/[^A-Za-z0-9]+/g, "-") + ".png";
  }
  // Completion packet: the certificate and the record of module results.
  function openCert(d) {
    var pr = progress();
    openPacket("Your completion packet", [
      { canvas: document.createElement("canvas"), label: "Certificate", file: fileName("Certificate", d),
        alt: "Certificate of completion for " + d.name + ", " + d.track + ", " + d.date + ", code " + d.code,
        draw: function (c) { draw(c, d); } },
      { canvas: document.createElement("canvas"), label: "Module record", file: fileName("Module-record", d),
        alt: "Record of module results for " + d.name + ", " + d.track,
        draw: function (c) { drawRecord(c, d, pr, "complete"); } }
    ]);
  }
  // Incomplete packet: a progress record only, clearly marked as not a certificate.
  function openProgress(name) {
    var pr = progress(), t = today();
    var d = { name: name, track: trackName(), studyMin: STUDY_MIN, date: t.text, iso: t.iso };
    openPacket("Your progress record", [
      { canvas: document.createElement("canvas"), label: "Progress record", file: fileName("Progress-record", d),
        alt: "Progress record (not a certificate) for " + name + ", " + d.track + ": " + pr.done + " of " + pr.total + " module quizzes passed",
        draw: function (c) { drawRecord(c, d, pr, "progress"); } }
    ]);
  }

  function save(canvas, url, file) {
    // Phones: the share sheet lets the learner save to Photos or Files; elsewhere a normal download.
    if (canvas.toBlob && navigator.canShare && window.File) {
      canvas.toBlob(function (blob) {
        var f = new File([blob], file, { type: "image/png" });
        if (navigator.canShare({ files: [f] })) {
          navigator.share({ files: [f], title: "Certificate of completion" }).catch(function () {});
        } else download(url, file);
      }, "image/png");
    } else download(url, file);
  }
  function download(url, file) {
    var a = document.createElement("a"); a.href = url; a.download = file;
    document.body.appendChild(a); a.click(); a.remove();
  }
  function printCert(urls) {
    var holder = document.getElementById("rcm-cert-print");
    if (!holder) { holder = document.createElement("div"); holder.id = "rcm-cert-print"; document.body.appendChild(holder); }
    holder.innerHTML = urls.map(function () { return '<img alt="">'; }).join("");
    var imgs = holder.querySelectorAll("img"), left = imgs.length;
    Array.prototype.forEach.call(imgs, function (img, i) {
      img.onload = function () {
        if (--left) return;
        document.documentElement.classList.add("rcm-cert-printing");
        setTimeout(function () { window.print(); }, 50);
      };
      img.src = urls[i];
    });
  }
  window.addEventListener("afterprint", function () { document.documentElement.classList.remove("rcm-cert-printing"); });

  /* ---------- certificate checklist on the examination page ---------- */
  var check = null;
  function renderCheck() {
    var pr = progress();
    if (!pr.total) return pr;
    if (!check) {
      check = document.createElement("details");
      check.className = "rcm-cert-check";
      form.parentNode.insertBefore(check, form);
    }
    check.open = !pr.all;
    check.innerHTML = '<summary><span class="rcm-cc-ring" style="--p:' + Math.round(100 * pr.done / pr.total) + '"></span>' +
      '<span><b>Certificate checklist</b><br><span class="rcm-cc-sub">' +
      (pr.all ? "All " + pr.total + " module quizzes passed. Pass this examination to earn your certificate."
              : pr.done + " of " + pr.total + " module quizzes passed on this device. Pass all of them and this examination to earn your certificate.") +
      '</span></span></summary><ol>' + pr.list.map(function (m) {
        var r = m.r, ok = r && r.p;
        return '<li class="' + (ok ? "ok" : r ? "try" : "") + '"><span class="rcm-cc-mk" aria-hidden="true">' + (ok ? "✓" : r ? "!" : "") + '</span>' +
          '<a href="' + esc(m.href) + '#quiz">Module ' + +m.nn + ': ' + esc(m.title) + '</a>' +
          '<span class="rcm-cc-sc">' + (r ? r.s + "/" + r.t + (ok ? "" : ", not yet passed") : "not taken") + '</span></li>';
      }).join("") + '</ol>' + (pr.all ? '' :
        '<div class="rcm-cc-prog"><input type="text" maxlength="70" autocomplete="name" placeholder="Full name" aria-label="Name for the progress record">' +
        '<button type="button">Print a progress record</button></div>') + '<p class="rcm-cc-note">Each module quiz is passed at its own pass mark (80% unless the module says otherwise). ' +
      'Progress is saved in this browser on this device only; on iPhone and iPad, the Home Screen app and Safari keep separate progress.</p>';
    var pi = check.querySelector(".rcm-cc-prog input"), pb = check.querySelector(".rcm-cc-prog button");
    if (pb) {
      var go = function () {
        var nm = pi.value.replace(/\s+/g, " ").trim();
        if (nm.length < 2) { pi.focus(); pi.setAttribute("aria-invalid", "true"); return; }
        openProgress(nm);
      };
      pb.addEventListener("click", go);
      pi.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); go(); } });
    }
    return pr;
  }

  function showLocked(p, host) {
    if (panel) panel.remove();
    var pr = progress();
    panel = document.createElement("div");
    panel.className = "rcm-cert rcm-cert-locked";
    var left = pr.list.filter(function (m) { return !(m.r && m.r.p); });
    panel.innerHTML = '<div class="rcm-cert-hd">' + MEDAL + '<div><div class="rcm-cert-kicker">' + (p ? "Well done!" : "Keep going") + '</div>' +
      '<h3>' + (p ? "You passed the examination" : "Your course progress") + '</h3></div></div>' +
      '<p>' + p.score + ' of ' + p.total + ' best answers (' + Math.round(100 * p.score / p.total) + '%). ' +
      'One step left: your certificate unlocks when every module quiz is passed. Still to pass (' + left.length + '):</p>' +
      '<ul class="rcm-cert-left">' + left.map(function (m) {
        return '<li><a href="' + esc(m.href) + '#quiz">Module ' + +m.nn + ': ' + esc(m.title) + '</a></li>';
      }).join("") + '</ul>' +
      '<p>Need to show your progress to a preceptor? Print a progress record (it is not a certificate).</p>' +
      '<div class="rcm-cert-row"><input type="text" maxlength="70" autocomplete="name" placeholder="Full name, e.g. Juan Dela Cruz" aria-label="Name for the progress record">' +
      '<button type="button">Make my progress record</button></div>' +
      '<small>Your examination pass is saved on this device, so come back here after the module quizzes. The progress record stays on this device.</small>';
    (host || result).appendChild(panel);
    var pin = panel.querySelector("input"), pbtn = panel.querySelector("button");
    function goProg() {
      var nm = pin.value.replace(/\s+/g, " ").trim();
      if (nm.length < 2) { pin.focus(); pin.setAttribute("aria-invalid", "true"); return; }
      pin.removeAttribute("aria-invalid"); openProgress(nm);
    }
    pbtn.addEventListener("click", goProg);
    pin.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); goProg(); } });
  }

  function offer(p, host) {
    if (progress().all) showPanel(p, host); else showLocked(p, host);
  }

  /* Watch the examination result: offer the certificate after a pass, remove it when a new set is drawn. */
  var busy = false;
  new MutationObserver(function () {
    if (busy) return;
    if (panel && !document.body.contains(panel)) panel = null;
    var p = passed();
    if (p && !(panel && result.contains(panel))) { busy = true; recordExam(p); renderCheck(); offer(p); busy = false; }
    else if (!p && panel && result.contains(panel)) { panel.remove(); panel = null; }
  }).observe(result, { childList: true, characterData: true, subtree: true });

  // A pass saved earlier on this device: offer the certificate (or the remaining modules) under the checklist.
  var saved = renderCheck().exam;
  var savedHost = null;
  function offerSaved() {
    var pr = progress();
    if (!pr.exam || (panel && result.contains(panel))) return;
    if (!savedHost) { savedHost = document.createElement("div"); savedHost.className = "rcm-cert-saved"; form.parentNode.insertBefore(savedHost, form); }
    examMin = examMin || pr.exam.m || 0;
    offer({ score: pr.exam.s, total: pr.exam.t }, savedHost);
  }
  if (saved) offerSaved();
  // Back from a module tab: refresh the checklist, and unlock the certificate if the last quiz is now passed.
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) return;
    var was = panel && panel.classList.contains("rcm-cert-locked");
    var pr = renderCheck();
    if (was && pr.all) {
      var host = panel.parentNode, ex = pr.exam;
      if (host === result) { var p = passed(); if (p) showPanel(p); }
      else if (ex) showPanel({ score: ex.s, total: ex.t }, host);
    }
  });
})();
