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
    ".rcm-certm-act{display:flex;flex-wrap:wrap;gap:8px;justify-content:flex-end;margin-top:12px}",
    "#rcm-cert-print{display:none}",
    "@media print{html.rcm-cert-printing body>*:not(#rcm-cert-print){display:none!important}",
    "html.rcm-cert-printing #rcm-cert-print{display:block!important}html.rcm-cert-printing #rcm-cert-print img{width:100%;height:auto}",
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
          modules: d.modules, score: d.score, total: d.total, exam_min: d.examMin, study_min: d.studyMin,
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

  function showPanel(p) {
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
    result.appendChild(panel);
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

  function openCert(d) {
    var canvas = document.createElement("canvas");
    var ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
    ready.then(function () {
      draw(canvas, d);
      var url = canvas.toDataURL("image/png");
      var file = "Certificate-" + d.track.replace(/[^A-Za-z0-9]+/g, "-") + "-" + d.name.replace(/[^A-Za-z0-9]+/g, "-") + ".png";
      if (modal) modal.remove();
      modal = document.createElement("div");
      modal.className = "rcm-certm";
      modal.setAttribute("role", "dialog"); modal.setAttribute("aria-modal", "true"); modal.setAttribute("aria-label", "Your certificate");
      modal.innerHTML = '<div class="rcm-certm-box"><img alt=""><div class="rcm-certm-act">' +
        '<button type="button" data-a="save">Save image</button>' +
        '<button type="button" data-a="print">Print or save as PDF</button>' +
        '<button type="button" class="ghost" data-a="close">Close</button></div></div>';
      var img = modal.querySelector("img");
      img.src = url; img.alt = "Certificate of completion for " + d.name + ", " + d.track + ", " + d.date + ", code " + d.code;
      document.body.appendChild(modal);
      modal.querySelector('[data-a="save"]').focus();
      modal.addEventListener("click", function (e) {
        var a = e.target.closest("[data-a]"); if (e.target === modal) a = { getAttribute: function () { return "close"; } };
        if (!a) return;
        var act = a.getAttribute("data-a");
        if (act === "close") { modal.remove(); modal = null; }
        else if (act === "save") save(canvas, url, file);
        else if (act === "print") printCert(url);
      });
      document.addEventListener("keydown", function esc(e) {
        if (e.key === "Escape" && modal) { modal.remove(); modal = null; document.removeEventListener("keydown", esc); }
      });
    });
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
  function printCert(url) {
    var holder = document.getElementById("rcm-cert-print");
    if (!holder) { holder = document.createElement("div"); holder.id = "rcm-cert-print"; document.body.appendChild(holder); }
    holder.innerHTML = '<img alt="Certificate of completion">';
    var img = holder.querySelector("img");
    img.onload = function () {
      document.documentElement.classList.add("rcm-cert-printing");
      setTimeout(function () { window.print(); }, 50);
    };
    img.src = url;
  }
  window.addEventListener("afterprint", function () { document.documentElement.classList.remove("rcm-cert-printing"); });

  /* Watch the examination result: offer the certificate after a pass, remove it when a new set is drawn. */
  var busy = false;
  new MutationObserver(function () {
    if (busy) return;
    if (panel && !result.contains(panel)) panel = null;
    var p = passed();
    if (p && !panel) { busy = true; showPanel(p); busy = false; }
    else if (!p && panel) { panel.remove(); panel = null; }
  }).observe(result, { childList: true, characterData: true, subtree: true });
})();
