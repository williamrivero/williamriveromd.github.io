/* ---------- Drug Index + Dosis intro scenes ---------- */
var R = 400, PURPLE = '#6b46c1', AMBER = '#b45309', GREEN = '#2e6b3e', RED = '#b91c1c', GRAY = '#64748b';
function chip(X, Y, label, bg, fg, sz, h) { sz = sz || 15; h = h || 30; x.font = '700 ' + sz + 'px ' + F; var w = x.measureText(label).width + 24; box(X, Y, w, h, h / 2, bg); txt(label, X + w / 2, Y + h / 2, sz, fg, 700, 'center'); return w; }
function pill(X, Y, col, s) { s = s || 1; x.save(); x.translate(X, Y); x.scale(s, s); rr(-22, -10, 44, 20, 10); x.fillStyle = '#fff'; x.fill(); x.strokeStyle = col; x.lineWidth = 2.5; x.stroke();
  x.beginPath(); x.moveTo(0, -10); x.lineTo(0, 10); x.stroke(); rr(-22, -10, 22, 20, 10); x.fillStyle = col; x.fill(); x.restore(); }
function kidney(X, Y, s, col) { x.save(); x.translate(X, Y); x.scale(s, s); x.fillStyle = col; x.beginPath();
  x.moveTo(0, -60); x.bezierCurveTo(50, -64, 62, -10, 48, 30); x.bezierCurveTo(36, 64, -6, 70, -20, 44); x.bezierCurveTo(-30, 26, -6, 18, -8, 0);
  x.bezierCurveTo(-10, -16, -34, -20, -30, -38); x.bezierCurveTo(-26, -54, -14, -60, 0, -60); x.fill(); x.restore(); }
function wrapTxt(s, X, Y, maxW, size, color, weight, lh) { x.font = (weight || 600) + ' ' + size + 'px ' + F; var wds = s.split(' '), line = '', yy = Y;
  wds.forEach(function (w) { var t = line ? line + ' ' + w : w; if (x.measureText(t).width > maxW && line) { txt(line, X, yy, size, color, weight); line = w; yy += lh; } else line = t; }); if (line) txt(line, X, yy, size, color, weight); return yy; }
function bars(X, Y, w, n, col, gap) { gap = gap || 14; for (var i = 0; i < n; i++) box(X, Y + i * gap, w * (i === n - 1 ? .62 : (i % 3 === 1 ? .92 : 1)), 7, 3.5, col || '#e2e8f0'); }
/* the Dosis app icon: teal tile, white capsule */
function dosisIcon(X, Y, s) { x.save(); x.translate(X, Y); x.scale(s, s); box(-50, -50, 100, 100, 24, TEAL);
  x.rotate(-Math.PI / 4.5); rr(-36, -15, 72, 30, 15); x.fillStyle = '#fff'; x.fill(); rr(0, -15, 36, 30, 15); x.fillStyle = '#9fd3d6'; x.fill(); x.fillRect(0, -15, 15, 30);
  x.strokeStyle = '#fff'; x.lineWidth = 3; rr(-36, -15, 72, 30, 15); x.stroke(); x.restore(); }
function icon(kind, X, Y, s, col) { x.save(); x.translate(X, Y); x.scale(s, s); x.strokeStyle = col; x.fillStyle = col; x.lineWidth = 5; x.lineCap = 'round'; x.lineJoin = 'round';
  if (kind === 'search') { x.beginPath(); x.arc(-5, -5, 14, 0, Math.PI * 2); x.stroke(); x.beginPath(); x.moveTo(6, 6); x.lineTo(20, 20); x.stroke(); }
  else if (kind === 'book') { box(-22, -18, 44, 36, 4, null, col, 5); x.beginPath(); x.moveTo(0, -18); x.lineTo(0, 18); x.stroke(); }
  else if (kind === 'kidney') { x.restore(); kidney(X, Y, s * .38, col); return; }
  else if (kind === 'offline') { [[-16, 10], [-6, 2], [4, -6], [14, -14]].forEach(function (b, i) { box(b[0] - 3, b[1], 7, 18 - b[1] + 2, 2, col); }); }
  else if (kind === 'sun') { x.beginPath(); x.arc(0, 0, 8, 0, Math.PI * 2); x.fill(); for (var k = 0; k < 8; k++) { var a = k * Math.PI / 4; x.beginPath(); x.moveTo(Math.cos(a) * 13, Math.sin(a) * 13); x.lineTo(Math.cos(a) * 19, Math.sin(a) * 19); x.stroke(); } }
  else if (kind === 'meal') { x.lineWidth = 4; x.beginPath(); x.arc(0, 2, 13, 0, Math.PI * 2); x.stroke(); x.beginPath(); x.moveTo(-20, -12); x.lineTo(-20, 16); x.moveTo(20, -12); x.lineTo(20, 16); x.stroke(); }
  else if (kind === 'moon') { x.beginPath(); x.arc(0, 0, 14, 0.6, Math.PI * 2 - 0.6); x.arc(8, 0, 11, Math.PI * 2 - 0.9, 0.9, true); x.fill(); }
  else if (kind === 'shield') { x.beginPath(); x.moveTo(0, -24); x.lineTo(20, -16); x.quadraticCurveTo(20, 12, 0, 24); x.quadraticCurveTo(-20, 12, -20, -16); x.closePath(); x.fill();
    x.strokeStyle = '#fff'; x.lineWidth = 4.5; x.beginPath(); x.moveTo(-9, 0); x.lineTo(-2, 8); x.lineTo(10, -8); x.stroke(); }
  x.restore(); }
function count(target, u) { var v = Math.round(target * ease(u) / 100) * 100; return v.toLocaleString('en-US'); }

var scenes = [
  function title(lt, T) {
    var a = pop(fadeIn(lt, .2, .7)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 30);
    box(R + 10, 66, 500, 58, 29, 'rgba(26,107,114,.12)'); txt('RENAL CARE MATTERS  ·  DOSIS', R + 40, 95, 18, TEAL, 800);
    txt('Drug Index', R + 30, 196, 84, NAVY, 800); txt('and Dosis, its app', R + 32, 262, 34, GOLD, 800); x.restore();
    var b = pop(fadeIn(lt, 1.3, .6)); if (b > 0) { x.save(); x.translate(R + 735, 180); x.scale(b * 1.3, b * 1.3); dosisIcon(0, 0, 1); x.restore(); }
    [['search', 'Find', 'every registered product', NAVY], ['book', 'Read', 'official label text', TEAL], ['kidney', 'Dose', 'by kidney function', GREEN], ['offline', 'Carry', 'offline, as an app', GOLD]].forEach(function (p, i) {
      var u = pop(fadeIn(lt, 3.2 + i * .45, .5)); if (u <= 0) return; var X = R + 20 + i * 212, Y = 340;
      x.save(); x.translate(X + 98, Y + 85); x.scale(u, u); x.translate(-X - 98, -Y - 85);
      box(X, Y, 196, 170, 18, '#fff', '#dfe6f0', 2); box(X, Y, 196, 8, 4, p[3]);
      icon(p[0], X + 42, Y + 58, p[0] === 'kidney' ? 1 : 1.1, p[3]); txt(p[1], X + 76, Y + 58, 30, INK, 800);
      wrapTxt(p[2], X + 22, Y + 110, 160, 17, '#475569', 600, 22); x.restore(); });
    var c = fadeIn(lt, 5.4, .5); if (c > 0) { x.save(); x.globalAlpha = c; chip(R + 20, 548, 'Free', 'rgba(46,107,62,.12)', GREEN, 16, 32); chip(R + 98, 548, 'For clinicians in the Philippines', 'rgba(31,56,100,.10)', NAVY, 16, 32); x.restore(); }
  },
  function stats(lt, T) {
    var a = fadeIn(lt, .2, .5); x.save(); x.globalAlpha = a;
    chip(R + 20, 70, 'FDA PHILIPPINES REGISTRY', 'rgba(31,56,100,.10)', NAVY, 15, 32); txt('Every registered product, one index', R + 20, 140, 40, NAVY, 800); x.restore();
    var cards = [[37000, 'drug products', 'registered in the Philippines', TEAL, 4.6], [2300, 'generic names', 'one page per generic', NAVY, 7.2],
      [1100, 'drug classes', 'from the registry', PURPLE, 8.2], [6000, 'supplement & nutrition brands', 'food supplements, FSMP, FSDU', GOLD, 9.8]];
    cards.forEach(function (c, i) { var u = pop(fadeIn(lt, c[4], .5)); if (u <= 0) return; var X = R + 20 + (i % 2) * 422, Y = 190 + Math.floor(i / 2) * 200;
      x.save(); x.translate(X + 200, Y + 90); x.scale(u, u); x.translate(-X - 200, -Y - 90);
      box(X, Y, 400, 180, 20, '#fff', '#dfe6f0', 2); box(X, Y + 20, 8, 140, 4, c[3]);
      pill(X + 340, Y + 44, c[3], 1.1); txt(count(c[0], fadeIn(lt, c[4], 1.6)) + '+', X + 36, Y + 62, 52, c[3], 800);
      txt(c[1], X + 36, Y + 116, 22, INK, 800); txt(c[2], X + 36, Y + 148, 16, '#64748b', 600); x.restore(); });
  },
  function search(lt, T) {
    box(R + 10, 70, 850, 300, 18, '#fff', '#dfe6f0', 2);
    var word = 'losartan', typed = word.slice(0, Math.max(0, Math.min(word.length, Math.floor((lt - .5) / .14))));
    box(R + 40, 96, 600, 52, 26, '#f8fafc', TEAL, 2.5); icon('search', R + 72, 122, .8, TEAL);
    txt(typed + (Math.floor(T * 2) % 2 ? '|' : ''), R + 100, 123, 20, INK, 600);
    if (typed.length) txt('Search the drug index', R + 660, 122, 15, '#94a3b8', 600);
    var rows = [['Losartan potassium', 'generic', TEAL], ['Losartan + hydrochlorothiazide', 'generic', TEAL], ['Angiotensin II receptor blocker (ARB)', 'drug class', PURPLE]];
    rows.forEach(function (r, i) { var v = fadeIn(lt, 1.7 + i * .25, .3); if (v <= 0) return; var Y = 166 + i * 50; x.save(); x.globalAlpha = v;
      box(R + 40, Y, 600, 42, 10, i === 0 ? '#ecfeff' : '#fff', '#e2e8f0', 1.5); pill(R + 70, Y + 21, r[2], .6); txt(r[0], R + 96, Y + 21, 17, INK, 700);
      chip(R + 640 - 22 - (x.measureText(r[1]).width + 24) - 8, Y + 8, r[1], 'rgba(100,116,139,.12)', GRAY, 13, 26); x.restore(); });
    var fields = ['Brand', 'Generic', 'Drug class', 'Indication', 'Manufacturer', 'Registration no.'];
    txt('Search by', R + 40, 336, 15, '#64748b', 800); var xx = R + 130;
    fields.forEach(function (f, i) { var on = lt > .9 + i * .55; var w = chip(xx, 321, f, on ? 'rgba(26,107,114,.14)' : '#f1f5f9', on ? TEAL : '#94a3b8', 14, 30); xx += w + 8; });
    var b = fadeIn(lt, 6, .5); if (b <= 0) return; x.save(); x.globalAlpha = b; x.translate(0, (1 - b) * 20);
    box(R + 10, 396, 850, 200, 18, '#fff', '#dfe6f0', 2); txt('Browse by', R + 40, 432, 22, NAVY, 800);
    var tabs = [['Generic A–Z', 0], ['Brand', 0], ['Drug class', 7.0], ['Therapeutic area', 7.8], ['Kidney dosing', 8.7]]; xx = R + 40;
    tabs.forEach(function (t, i) { var on = t[1] && lt > t[1]; x.font = '700 16px ' + F; var w = x.measureText(t[0]).width + 32;
      box(xx, 456, w, 40, 10, on ? TEAL : '#f8fafc', on ? TEAL : '#e2e8f0', 1.5); txt(t[0], xx + w / 2, 476, 16, on ? '#fff' : '#475569', 700, 'center'); xx += w + 10; });
    var cur = lt > 8.7 ? 2 : lt > 7.8 ? 1 : 0, lists = [['ACE inhibitors', 'Angiotensin II receptor blockers', 'Calcium channel blockers'], ['Cardiovascular', 'Kidney and urinary', 'Infections'], ['No change', 'Adjust the dose', 'Avoid']];
    var cols = [[PURPLE, PURPLE, PURPLE], [NAVY, TEAL, GOLD], [GREEN, AMBER, RED]];
    if (lt > 7) lists[cur].forEach(function (s, i) { var X = R + 40 + i * 272; box(X, 516, 258, 54, 10, '#fff', '#e2e8f0', 1.5); box(X, 516, 7, 54, 3.5, cols[cur][i]); txt(s, X + 22, 543, 16, INK, 700); });
    x.restore();
  },
  function monograph(lt, T) {
    var a = ease(fadeIn(lt, .1, .5)); x.save(); x.globalAlpha = a; x.translate(0, (1 - a) * 24);
    box(R + 10, 70, 850, 530, 18, '#fff', '#dfe6f0', 2); rr(R + 10, 70, 850, 92, 18); x.save(); x.clip(); x.fillStyle = NAVY; x.fillRect(R + 10, 70, 850, 92); x.restore();
    txt('Losartan potassium', R + 40, 104, 30, '#fff', 800); txt('Angiotensin II receptor blocker', R + 40, 138, 16, '#c7d2fe', 600);
    var cw = chip(R + 560, 96, 'U.S. FDA label', 'rgba(255,255,255,.16)', '#fff', 14, 28); chip(R + 568 + cw, 96, 'verbatim', GOLD, '#fff', 14, 28);
    var toc = ['Use', 'Dosing', 'Kidney dosing', 'Warnings', 'Interactions', 'Adverse reactions', 'Pharmacokinetics', 'References'];
    toc.forEach(function (s, i) { var on = Math.floor((lt - 1.2) / .5) === i; txt(s, R + 40, 196 + i * 40, 16, on ? TEAL : '#475569', on ? 800 : 600); if (on) box(R + 28, 186 + i * 40, 4, 20, 2, TEAL); });
    x.fillStyle = '#e2e8f0'; x.fillRect(R + 210, 180, 2, 400);
    txt('Dosage and administration', R + 236, 196, 18, NAVY, 800);
    box(R + 236, 216, 340, 150, 10, '#f8fafc'); txt('“', R + 246, 236, 40, 'rgba(184,134,11,.5)', 800); bars(R + 270, 236, 290, 8, '#cbd5e1');
    txt('Text from the official label,', R + 236, 394, 15, '#64748b', 700); txt('laid out, never reworded.', R + 236, 416, 15, '#64748b', 700);
    var p = fadeIn(lt, 4.6, .5); if (p > 0) { x.save(); x.globalAlpha = p; x.translate((1 - p) * 30, 0);
      box(R + 600, 180, 240, 400, 14, '#f8fafc', '#e2e8f0', 1.5); txt('Philippine products', R + 618, 208, 17, NAVY, 800);
      for (var i = 0; i < 5; i++) { var v = fadeIn(lt, 5 + i * .3, .3); if (v <= 0) continue; var Y = 236 + i * 66; x.save(); x.globalAlpha = v * p;
        box(R + 614, Y, 212, 56, 10, '#fff', '#e2e8f0', 1.5); txt('Brand', R + 628, Y + 18, 12, '#94a3b8', 700); box(R + 676, Y + 13, 90 + (i * 23) % 50, 9, 4.5, '#cbd5e1');
        txt('Reg. no.', R + 628, Y + 38, 12, '#94a3b8', 700); box(R + 690, Y + 33, 80, 9, 4.5, 'rgba(26,107,114,.35)'); x.restore(); }
      x.restore(); }
    x.restore();
  },
  function kidneyDose(lt, T) {
    var a = fadeIn(lt, .1, .5); x.save(); x.globalAlpha = a;
    txt('Kidney dosing, by kidney function', R + 20, 100, 36, NAVY, 800); chip(R + 20, 128, 'Example layout', 'rgba(100,116,139,.12)', GRAY, 14, 28); x.restore();
    var bands = [['≥ 60', 'mL/min', GREEN], ['30–59', 'mL/min', AMBER], ['15–29', 'mL/min', AMBER], ['< 15', 'mL/min', RED], ['HD', 'hemodialysis', RED], ['PD', 'peritoneal', '#94a3b8'], ['CRRT', 'continuous', '#94a3b8']];
    bands.forEach(function (b, i) { var u = pop(fadeIn(lt, .8 + i * .28, .4)); if (u <= 0) return; var X = R + 20 + i * 120, Y = 180;
      x.save(); x.translate(X + 55, Y + 70); x.scale(u, u); x.translate(-X - 55, -Y - 70);
      box(X, Y, 110, 140, 14, b[2]); txt(b[0], X + 55, Y + 58, 28, '#fff', 800, 'center'); txt(b[1], X + 55, Y + 96, 14, 'rgba(255,255,255,.9)', 700, 'center'); x.restore(); });
    var lg = [['No change', GREEN, 4.6], ['Adjust', AMBER, 5.3], ['Avoid', RED, 5.9], ['Not studied', '#94a3b8', 6.6]], xx = R + 20;
    lg.forEach(function (l) { var v = pop(fadeIn(lt, l[2], .35)); x.font = '700 17px ' + F; var w = x.measureText(l[0]).width + 52; if (v > 0) { x.save(); x.globalAlpha = Math.min(1, v);
      box(xx, 350, w, 40, 20, '#fff', '#e2e8f0', 1.5); x.fillStyle = l[1]; x.beginPath(); x.arc(xx + 22, 370, 8, 0, Math.PI * 2); x.fill(); txt(l[0], xx + 38, 371, 17, INK, 700); x.restore(); } xx += w + 12; });
    var k = ease(fadeIn(lt, 7.6, .5)); if (k <= 0) return; x.save(); x.globalAlpha = k; x.translate(0, (1 - k) * 24);
    box(R + 20, 420, 830, 160, 18, '#fff7ed', '#fdba74', 2); kidney(R + 88, 500, .78, '#c2410c');
    txt('Kidney injury risk', R + 150, 462, 26, '#9a3412', 800); txt('Flagged from the label, grouped by mechanism', R + 150, 496, 17, '#7c2d12', 600);
    xx = R + 150; ['tubular', 'hemodynamic', 'interstitial nephritis', 'crystal'].forEach(function (s) { xx += chip(xx, 524, s, 'rgba(194,65,12,.12)', '#9a3412', 14, 30) + 8; });
    x.restore();
  },
  function tools(lt, T) {
    var a = fadeIn(lt, .1, .5); x.save(); x.globalAlpha = a; txt('Two tools, one data set', R + 20, 100, 36, NAVY, 800); x.restore();
    var l = pop(fadeIn(lt, 1.4, .5)); if (l > 0) { var X = R + 20; x.save(); x.translate(X + 200, 350); x.scale(l, l); x.translate(-X - 200, -350);
      box(X, 140, 405, 440, 20, '#fff', '#dfe6f0', 2); box(X, 140, 405, 8, 4, PURPLE); txt('Interaction Checker', X + 28, 186, 24, PURPLE, 800);
      var P = [[X + 110, 270, NAVY, 'Losartan'], [X + 300, 270, TEAL, 'Furosemide'], [X + 205, 380, RED, 'Ibuprofen']];
      [[0, 1], [0, 2], [1, 2]].forEach(function (e, i) { var u = ease(fadeIn(lt, 2.4 + i * .35, .4)); if (u <= 0) return; var p = P[e[0]], q = P[e[1]];
        x.strokeStyle = AMBER; x.lineWidth = 4; x.setLineDash([8, 7]); x.lineDashOffset = -T * 30; x.beginPath(); x.moveTo(p[0], p[1]); x.lineTo(p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u); x.stroke(); x.setLineDash([]); });
      P.forEach(function (p) { box(p[0] - 80, p[1] - 22, 160, 44, 22, '#fff', p[2], 3); pill(p[0] - 54, p[1], p[2], .55); txt(p[3], p[0] + 12, p[1] + 1, 14, INK, 800, 'center'); });
      var g = [['Contraindicated', '#7f1d1d'], ['Avoid', RED], ['Adjust or monitor', AMBER], ['Minor', GRAY]], yy = 440;
      g.forEach(function (c, i) { var v = fadeIn(lt, 3.6 + i * .3, .3); if (v <= 0) return; x.save(); x.globalAlpha = v; var w = chip(X + 28 + (i % 2) * 190, yy + Math.floor(i / 2) * 44, c[0], c[1], '#fff', 14, 32); x.restore(); });
      x.restore(); }
    var r = pop(fadeIn(lt, 5.2, .5)); if (r > 0) { var X2 = R + 445; x.save(); x.translate(X2 + 200, 350); x.scale(r, r); x.translate(-X2 - 200, -350);
      box(X2, 140, 405, 440, 20, '#fff', '#dfe6f0', 2); box(X2, 140, 405, 8, 4, TEAL); txt('Med Scheduler', X2 + 28, 186, 24, TEAL, 800);
      var X0 = X2 + 40, w = 325, hx = function (h) { return X0 + (h - 5) / 18 * w; };
      box(X0, 250, w, 10, 5, '#e2e8f0'); box(hx(13), 244, hx(17) - hx(13), 22, 6, 'rgba(26,107,114,.25)'); txt('Dialysis', (hx(13) + hx(17)) / 2, 230, 13, TEAL, 800, 'center');
      [[6, 'sun'], [7, 'meal'], [12, 'meal'], [18, 'meal'], [22, 'moon']].forEach(function (m) { icon(m[1], hx(m[0]), 290, .6, '#64748b'); });
      var rows = [['7:00 AM', [TEAL, RED]], ['5:30 PM', [NAVY]], ['7:00 PM', [TEAL, PURPLE]], ['10:00 PM', [GOLD]]];
      rows.forEach(function (rw, i) { var v = pop(fadeIn(lt, 6.4 + i * .35, .35)); if (v <= 0) return; var y = 352 + i * 54; x.save(); x.globalAlpha = Math.min(1, v);
        box(X2 + 28, y - 22, 350, 44, 10, '#f8fafc', '#e2e8f0', 1.5); txt(rw[0], X2 + 48, y, 16, INK, 800); rw[1].forEach(function (c, j) { pill(X2 + 200 + j * 58, y, c, .9); }); x.restore(); });
      x.restore(); }
  },
  function offline(lt, T) {
    // a drug page with the teal Dosis tab on its left edge; the drawer slides out
    box(R + 10, 70, 520, 530, 18, '#fff', '#dfe6f0', 2); txt('Drug Index', R + 70, 108, 20, NAVY, 800); bars(R + 70, 140, 420, 3); bars(R + 70, 200, 420, 4); bars(R + 70, 280, 420, 3);
    var pulse = 1 + (lt > .8 && lt < 2.2 ? .08 * Math.sin((lt - .8) * 12) : 0);
    x.save(); x.translate(R + 26, 360); x.scale(pulse, pulse); box(-16, -70, 34, 140, 10, TEAL); x.rotate(-Math.PI / 2); txt('Dosis', 0, 1, 16, '#fff', 800, 'center'); x.restore();
    var d = ease(fadeIn(lt, 2.0, .6)); if (d > 0) { var DX = R + 10 - 340 * (1 - d); x.save(); rr(R + 10, 70, 520, 530, 18); x.clip();
      box(DX, 70, 340, 530, 0, '#f0fdfa'); x.fillStyle = 'rgba(26,107,114,.25)'; x.fillRect(DX + 338, 70, 2, 530); dosisIcon(DX + 60, 130, .55);
      txt('Dosis', DX + 100, 118, 22, TEAL, 800); txt('the Drug Index app', DX + 100, 144, 14, '#475569', 700);
      box(DX + 28, 186, 284, 48, 24, TEAL); txt('Install Dosis', DX + 170, 210, 17, '#fff', 800, 'center');
      txt('Offline use', DX + 28, 274, 16, NAVY, 800); txt('The complete index, one download', DX + 28, 298, 14, '#475569', 600);
      var pr = ease(fadeIn(lt, 3.4, 2.4)); box(DX + 28, 322, 284, 16, 8, '#ccfbf1'); if (pr > 0) box(DX + 28, 322, 284 * pr, 16, 8, TEAL);
      txt(pr < 1 ? 'Saving ' + Math.round(pr * 100) + '%' : 'Saved · ready offline ✓', DX + 28, 362, 15, pr < 1 ? '#475569' : GREEN, 800);
      x.restore(); }
    // a phone with no signal
    var p = pop(fadeIn(lt, 6.2, .5)); if (p > 0) { x.save(); x.translate(R + 700, 330); x.scale(p, p);
      box(-120, -250, 240, 470, 34, '#0f172a'); box(-108, -234, 216, 438, 26, '#e6f2f2'); box(-30, -228, 60, 12, 6, '#0f172a');
      icon('offline', -60, -190, .7, '#94a3b8'); x.strokeStyle = RED; x.lineWidth = 4; x.lineCap = 'round'; x.beginPath(); x.moveTo(-80, -204); x.lineTo(-42, -176); x.stroke();
      txt('No signal', 6, -190, 15, RED, 800, 'center');
      dosisIcon(0, -70, .9); txt('Dosis', 0, 2, 20, INK, 800, 'center');
      var ok = fadeIn(lt, 7.4, .4); if (ok > 0) { x.save(); x.globalAlpha = ok; box(-90, 50, 180, 44, 22, GREEN); txt('Works offline', 0, 72, 17, '#fff', 800, 'center'); x.restore(); }
      var m = pop(fadeIn(lt, 9.6, .5)); if (m > 0) { x.save(); x.globalAlpha = Math.min(1, m); box(-96, 116, 192, 64, 12, '#fff', '#cbd5e1', 1.5); box(-96, 116, 192, 20, 12, NAVY); x.fillStyle = NAVY; x.fillRect(-96, 126, 192, 10);
        txt('Every Monday', 0, 160, 16, NAVY, 800, 'center'); txt('labels refreshed', 0, 127, 11, '#fff', 800, 'center'); x.restore(); }
      x.restore(); }
  },
  function end(lt, T) {
    var a = pop(fadeIn(lt, .2, .6)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 24);
    box(R + 20, 80, 830, 150, 18, '#fff', '#dfe6f0', 2); icon('shield', R + 82, 155, 1.5, TEAL);
    txt('Supports your clinical judgment,', R + 140, 130, 26, NAVY, 800); txt('it does not replace it.', R + 140, 164, 26, NAVY, 800);
    txt('Always check the full prescribing information.', R + 140, 200, 18, '#475569', 700); x.restore();
    var b = pop(fadeIn(lt, 4.6, .6)); if (b <= 0) return; x.save(); x.globalAlpha = Math.min(1, b); x.translate(0, (1 - b) * 24);
    box(R + 20, 270, 830, 270, 22, 'rgba(26,107,114,.08)', 'rgba(26,107,114,.25)', 2); dosisIcon(R + 130, 405, 1.25);
    txt('Dosis', R + 230, 360, 64, TEAL, 800); txt('The Drug Index app', R + 232, 412, 24, GOLD, 800);
    txt('renalcarematters.com/drugs', R + 232, 470, 28, INK, 800); x.restore();
  }
];
