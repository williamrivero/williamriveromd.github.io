<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>html,body{margin:0;background:#000;}canvas{display:block;}</style></head>
<body><canvas id="c" width="1280" height="720"></canvas>
<script>
var TL = null; // set by the recorder: {scenes, amp, fps}
var c = document.getElementById('c'), x = c.getContext('2d');
var W = 1280, H = 720;
var TEAL = '#1a6b72', DTEAL = '#0e4a50', NAVY = '#1f3864', GOLD = '#b8860b', INK = '#1e2a38';
var F = 'Inter, system-ui, sans-serif';

function rr(X, Y, w, h, r) { x.beginPath(); x.moveTo(X + r, Y); x.arcTo(X + w, Y, X + w, Y + h, r); x.arcTo(X + w, Y + h, X, Y + h, r); x.arcTo(X, Y + h, X, Y, r); x.arcTo(X, Y, X + w, Y, r); x.closePath(); }
function box(X, Y, w, h, r, fill, stroke, lw) { rr(X, Y, w, h, r); if (fill) { x.fillStyle = fill; x.fill(); } if (stroke) { x.strokeStyle = stroke; x.lineWidth = lw || 2; x.stroke(); } }
function txt(s, X, Y, size, color, weight, align) { x.font = (weight || 600) + ' ' + size + 'px ' + F; x.fillStyle = color; x.textAlign = align || 'left'; x.textBaseline = 'middle'; x.fillText(s, X, Y); }
function ease(u) { u = Math.max(0, Math.min(1, u)); return u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2; }
function pop(u) { u = Math.max(0, Math.min(1, u)); var c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(u - 1, 3) + c1 * Math.pow(u - 1, 2); }
function fadeIn(lt, at, d) { return Math.max(0, Math.min(1, (lt - at) / (d || .4))); }

/* ---------- waveforms ---------- */
function sinus(u) {            // u = phase in a beat, 0..1
  var y = 0;
  y += 0.12 * Math.exp(-Math.pow((u - 0.12) / 0.03, 2));          // P
  y -= 0.12 * Math.exp(-Math.pow((u - 0.25) / 0.008, 2));         // Q
  y += 1.0 * Math.exp(-Math.pow((u - 0.27) / 0.012, 2));          // R
  y -= 0.25 * Math.exp(-Math.pow((u - 0.295) / 0.012, 2));        // S
  y += 0.25 * Math.exp(-Math.pow((u - 0.5) / 0.05, 2));           // T
  return y;
}
function vf(t) { return 0.45 * Math.sin(t * 2 * Math.PI * 4.6) * (0.7 + 0.3 * Math.sin(t * 1.3)) + 0.2 * Math.sin(t * 2 * Math.PI * 6.9 + 1) + 0.12 * Math.sin(t * 2 * Math.PI * 2.1); }
function ecgAt(kind, t, hr) { if (kind === 'vf') return vf(t); var p = 60 / (hr || 72); return sinus((t % p) / p); }
function capAt(t, rr, v) {     // capnogram, height 0..1 scaled by v (0..1)
  var p = 60 / rr, u = (t % p) / p, y;
  if (u < 0.38) y = 0; else if (u < 0.46) y = 0.93 * (1 - Math.pow(1 - (u - 0.38) / 0.08, 3)); else if (u < 0.9) y = 0.93 + 0.07 * (u - 0.46) / 0.44;
  else if (u < 0.95) { var f = (u - 0.9) / 0.05; y = 1 - f * f * (3 - 2 * f); } else y = 0;
  return y * v;
}
/* draw a sweeping trace: fn(time)->value, in box; the sweep head is at time T */
function trace(X, Y, w, h, T, fn, color, gain, span) {
  span = span || w / 110; var head = (T % span) / span * w;
  x.save(); rr(X, Y, w, h, 8); x.clip();
  x.strokeStyle = color; x.lineWidth = 2.4; x.lineJoin = 'round';
  x.beginPath(); var first = true;
  for (var px = 0; px <= w; px += 1) {
    if (px > head && px < head + 14) { first = true; continue; }   // eraser gap
    var tt = px <= head ? T - (head - px) / w * span : T - span + (px - head) / w * span, v = 0, dt = span / w;
    for (var k = 0; k < 5; k++) { var vv = fn(tt + dt * k / 5); if (Math.abs(vv) > Math.abs(v)) v = vv; }   // keep narrow spikes
    var y = Y + h * 0.6 - v * gain;
    if (first) { x.moveTo(X + px, y); first = false; } else x.lineTo(X + px, y);
  }
  x.stroke(); x.restore();
}
/* a small bedside monitor */
function monitor(X, Y, w, h, T, st) {
  box(X, Y, w, h, 18, '#0b0f17', '#2b3444', 3);
  var pad = 14, top = Y + 12;
  if (st.alarm) { box(X + pad, top, w - 2 * pad - 4, 30, 8, st.alarmColor || '#c1121f'); txt(st.alarm, X + w / 2, top + 15, 15, st.alarmColor === '#f2c200' ? '#111' : '#fff', 800, 'center'); }
  var gx = X + pad, gw = w * 0.66 - pad, gy = top + 40, rows = st.capno ? 3 : 2, gh = (h - 66) / rows - 6;
  box(gx, gy, gw, gh, 8, '#0f1724'); trace(gx, gy, gw, gh, T, function (t) { return ecgAt(st.rhythm, t, st.hr); }, '#5ee08a', gh * 0.55);
  box(gx, gy + gh + 6, gw, gh, 8, '#0f1724');
  if (st.rhythm === 'vf') { x.strokeStyle = '#22d3ee'; x.lineWidth = 2; x.beginPath(); x.moveTo(gx + 6, gy + gh + 6 + gh * 0.7); x.lineTo(gx + gw - 6, gy + gh + 6 + gh * 0.7); x.stroke(); }
  else trace(gx, gy + gh + 6, gw, gh, T, function (t) { var p = 60 / st.hr, u = ((t - 0.2) % p + p) % p / p; return u < 0.2 ? Math.sin(u / 0.2 * Math.PI / 2) : Math.exp(-(u - 0.2) * 4.5) * (1 + 0.15 * Math.exp(-Math.pow((u - 0.42) / 0.05, 2))); }, '#22d3ee', gh * 0.5);
  if (st.capno) { var cy = gy + 2 * (gh + 6); box(gx, cy, gw, gh, 8, '#0f1724'); trace(gx, cy, gw, gh, T, function (t) { return capAt(t, st.rr || 10, (st.co2fn ? st.co2fn(t) : st.co2) / 50); }, '#fbbf24', gh * 0.8); }
  // numbers
  var nx = X + w * 0.66 + 6, nw = w * 0.34 - pad - 6, items = [['HR', st.hrShown, '#4ade80'], ['SpO₂', st.spo2, '#22d3ee']];
  if (st.capno) items.push(['EtCO₂', st.co2Shown, '#fbbf24']);
  var ih = (h - 66) / items.length - 6;
  items.forEach(function (it, i) {
    var iy = gy + i * (ih + 6); box(nx, iy, nw, ih, 8, '#0f1724');
    txt(it[0], nx + 10, iy + 16, 13, it[2], 700); txt(it[1], nx + 10, iy + ih * 0.62, Math.min(44, ih * 0.5), it[2], 800);
  });
}

/* ---------- the cartoon guide (an original character) ---------- */
function guide(T, amp, mode, lt) {
  var bx = 210, by = 620 + Math.sin(T * 2.2) * 3;     // feet line
  x.save();
  // shadow
  x.fillStyle = 'rgba(15,30,46,.12)'; x.beginPath(); x.ellipse(bx, 640, 120, 16, 0, 0, Math.PI * 2); x.fill();
  // body (scrubs)
  var SCRUB = '#24406e'; x.fillStyle = SCRUB; rr(bx - 100, by - 252, 200, 252, 64); x.fill();
  x.fillStyle = '#182d52'; x.beginPath(); x.moveTo(bx - 34, by - 245); x.lineTo(bx, by - 200); x.lineTo(bx + 34, by - 245); x.closePath(); x.fill();   // V-neck
  // badge
  box(bx + 30, by - 185, 42, 26, 5, '#fff'); x.fillStyle = TEAL; x.fillRect(bx + 36, by - 177, 30, 4); x.fillRect(bx + 36, by - 169, 20, 4);
  // stethoscope
  x.strokeStyle = '#9fb0c6'; x.lineWidth = 6; x.lineCap = 'round'; x.beginPath(); x.moveTo(bx - 50, by - 238); x.quadraticCurveTo(bx - 60, by - 150, bx - 20, by - 140); x.stroke();
  x.fillStyle = '#94a3b8'; x.beginPath(); x.arc(bx - 16, by - 138, 10, 0, Math.PI * 2); x.fill();
  // arms
  var skin = '#b87a4e';
  x.strokeStyle = SCRUB; x.lineWidth = 36;
  x.beginPath(); x.moveTo(bx - 80, by - 210); x.quadraticCurveTo(bx - 120, by - 120, bx - 95, by - 70); x.stroke();       // left arm down
  x.fillStyle = skin; x.beginPath(); x.arc(bx - 93, by - 62, 17, 0, Math.PI * 2); x.fill();
  var ang;   // right arm: wave in the intro, point toward the content otherwise
  if (mode === 'wave') ang = -0.95 + Math.sin(T * 7) * 0.22; else ang = -0.55 + Math.sin(T * 1.6) * 0.06;
  var sx = bx + 80, sy = by - 210, ex = sx + Math.cos(ang) * 70, ey = sy + Math.sin(ang) * 70 + 40, hx = ex + Math.cos(ang - 0.2) * 70, hy = ey + Math.sin(ang - 0.2) * 70;
  x.strokeStyle = SCRUB; x.beginPath(); x.moveTo(sx, sy); x.lineTo(ex, ey); x.stroke();
  x.strokeStyle = skin; x.lineWidth = 26; x.beginPath(); x.moveTo(ex, ey); x.lineTo(hx, hy); x.stroke();
  x.fillStyle = skin; x.beginPath(); x.arc(hx, hy, 18, 0, Math.PI * 2); x.fill();
  // neck + head
  x.fillStyle = skin; x.fillRect(bx - 24, by - 282, 48, 42);
  var hy0 = by - 350 + Math.sin(T * 2.2 + .6) * 2, tilt = Math.sin(T * 1.3) * 0.04 + amp * 0.03;
  x.translate(bx, hy0); x.rotate(tilt);
  // hair back
  // face
  x.fillStyle = skin; x.beginPath(); x.moveTo(-76, -10); x.quadraticCurveTo(-80, -86, 0, -86); x.quadraticCurveTo(80, -86, 76, -10);
  x.quadraticCurveTo(78, 62, 40, 86); x.quadraticCurveTo(0, 102, -40, 86); x.quadraticCurveTo(-78, 62, -76, -10); x.closePath(); x.fill();
  // ears
  x.beginPath(); x.ellipse(-76, 16, 12, 18, 0, 0, Math.PI * 2); x.ellipse(76, 16, 12, 18, 0, 0, Math.PI * 2); x.fill();
  // fringe
  x.fillStyle = '#1a1410'; x.beginPath(); x.moveTo(-80, 4); x.quadraticCurveTo(-92, -70, -30, -96); x.quadraticCurveTo(30, -112, 74, -78); x.quadraticCurveTo(92, -50, 80, 4);
  x.lineTo(72, 4); x.quadraticCurveTo(70, -30, 52, -44); x.quadraticCurveTo(10, -30, -30, -50); x.quadraticCurveTo(-62, -36, -70, 4); x.closePath(); x.fill();
  x.fillRect(-80, -6, 9, 30); x.fillRect(71, -6, 9, 30);   // sideburns
  x.strokeStyle = 'rgba(255,255,255,.12)'; x.lineWidth = 3; x.beginPath(); x.moveTo(-28, -94); x.quadraticCurveTo(-34, -70, -30, -52); x.stroke();   // part
  x.fillStyle = 'rgba(40,30,25,.10)'; x.beginPath(); x.moveTo(-60, 40); x.quadraticCurveTo(-50, 92, 0, 96); x.quadraticCurveTo(50, 92, 60, 40); x.quadraticCurveTo(0, 74, -60, 40); x.fill();   // stubble shadow
  // eyes (blink every ~3.7 s)
  var blink = ((T % 3.7) < 0.13) ? 0.12 : 1;
  x.fillStyle = '#1e1b18';
  [-30, 30].forEach(function (ex2) { x.beginPath(); x.ellipse(ex2, 8, 10, 13 * blink, 0, 0, Math.PI * 2); x.fill(); });
  x.fillStyle = '#fff'; if (blink > .5) [-27, 33].forEach(function (ex2) { x.beginPath(); x.arc(ex2, 3, 3.5, 0, Math.PI * 2); x.fill(); });
  // brows lift a little when speaking
  x.strokeStyle = '#1a1410'; x.lineWidth = 8; x.lineCap = 'round';
  [-1, 1].forEach(function (s) { x.beginPath(); x.moveTo(s * 18, -16 - amp * 4); x.quadraticCurveTo(s * 31, -21 - amp * 5, s * 46, -18 - amp * 4); x.stroke(); });
  // cheeks
  x.fillStyle = 'rgba(200,110,90,.14)'; x.beginPath(); x.ellipse(-46, 36, 13, 8, 0, 0, Math.PI * 2); x.ellipse(46, 36, 13, 8, 0, 0, Math.PI * 2); x.fill();
  // mouth: smile when quiet, opens with the voice
  var open = Math.min(1, amp * 1.25);
  if (open < 0.08) { x.strokeStyle = '#6b2b2b'; x.lineWidth = 5; x.beginPath(); x.arc(0, 40, 20, 0.2 * Math.PI, 0.8 * Math.PI); x.stroke(); }
  else {
    x.fillStyle = '#5a1f22'; x.beginPath(); x.ellipse(0, 50, 14 + open * 8, 4 + open * 15, 0, 0, Math.PI * 2); x.fill();
    x.fillStyle = '#c85b5b'; x.beginPath(); x.ellipse(0, 56 + open * 6, 9 + open * 4, 3 + open * 4, 0, 0, Math.PI); x.fill();
    x.fillStyle = '#fff'; x.fillRect(-10 - open * 4, 50 - (4 + open * 15) + 1, 20 + open * 8, 4);
  }
  x.restore();
}

/* ---------- caption ---------- */
function caption(sc, lt) {
  var s = (sc.text.replace(/U\.S\./g, 'U\u2024S\u2024').match(/[^.!?]+[.!?]+/g) || [sc.text]).map(function (q) { return q.replace(/\u2024/g, '.'); }), L = s.reduce(function (a, b) { return a + b.length; }, 0);
  var u = (lt - sc.lead) / sc.speech, acc = 0, cur = s[s.length - 1];
  for (var i = 0; i < s.length; i++) { acc += s[i].length / L; if (u < acc) { cur = s[i]; break; } }
  if (lt < sc.lead * 0.6) return;
  cur = cur.trim(); x.font = '600 24px ' + F; var lines = [cur];
  if (x.measureText(cur).width > 1100) {   // two lines, split near the middle at a word
    var wds = cur.split(' '), best = 0, bd = 1e9;
    for (var j = 1; j < wds.length; j++) { var d = Math.abs(x.measureText(wds.slice(0, j).join(' ')).width - x.measureText(wds.slice(j).join(' ')).width); if (d < bd) { bd = d; best = j; } }
    lines = [wds.slice(0, best).join(' '), wds.slice(best).join(' ')];
  }
  var wdt = Math.max.apply(null, lines.map(function (l) { return x.measureText(l).width; })) + 48, hh = lines.length * 32 + 14, top = 700 - hh;
  box(W / 2 - wdt / 2, top, wdt, hh, 12, 'rgba(15,23,42,.82)');
  lines.forEach(function (l, j) { txt(l, W / 2, top + 23 + j * 32, 24, '#fff', 600, 'center'); });
}

