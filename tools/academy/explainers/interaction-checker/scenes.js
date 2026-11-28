/* ---------- Interaction Checker scenes ---------- */
var R = 400, PURPLE = '#6b46c1', AMBER = '#b45309';
var G = { ci: ['Contraindicated', '#7f1d1d'], av: ['Avoid', '#b91c1c'], am: ['Adjust or monitor', '#b45309'], mi: ['Minor', '#64748b'] };
function pill(X, Y, col, s) { s = s || 1; x.save(); x.translate(X, Y); x.scale(s, s); rr(-22, -10, 44, 20, 10); x.fillStyle = '#fff'; x.fill(); x.strokeStyle = col; x.lineWidth = 2.5; x.stroke();
  x.beginPath(); x.moveTo(0, -10); x.lineTo(0, 10); x.stroke(); rr(-22, -10, 22, 20, 10); x.fillStyle = col; x.fill(); x.restore(); }
function chip(X, Y, label, bg, fg, sz, h) { sz = sz || 15; h = h || 30; x.font = '700 ' + sz + 'px ' + F; var w = x.measureText(label).width + 24; box(X, Y, w, h, h / 2, bg); txt(label, X + w / 2, Y + h / 2, sz, fg, 700, 'center'); return w; }
function kidney(X, Y, s, col) { x.save(); x.translate(X, Y); x.scale(s, s); x.fillStyle = col; x.beginPath();
  x.moveTo(0, -60); x.bezierCurveTo(50, -64, 62, -10, 48, 30); x.bezierCurveTo(36, 64, -6, 70, -20, 44); x.bezierCurveTo(-30, 26, -6, 18, -8, 0);
  x.bezierCurveTo(-10, -16, -34, -20, -30, -38); x.bezierCurveTo(-26, -54, -14, -60, 0, -60); x.fill(); x.restore(); }
var MEDS = [['Ibuprofen', '#b91c1c'], ['Losartan', NAVY], ['Furosemide', TEAL], ['Clarithromycin', PURPLE], ['Atorvastatin', GOLD]];
var scenes = [
  function title(lt, T) {
    var a = pop(fadeIn(lt, .2, .7)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 30);
    box(R + 10, 66, 560, 58, 29, 'rgba(26,107,114,.12)'); txt('DOSIS  ·  THE DRUG INDEX APP', R + 40, 95, 18, TEAL, 800);
    txt('Interaction Checker', R + 30, 196, 70, NAVY, 800); txt('medicines, pairs and the kidneys', R + 32, 260, 36, GOLD, 800); x.restore();
    // a network of medicines; the lines light up one by one
    var cx = R + 440, cy = 450, rad = 135, pts = MEDS.map(function (m, i) { var an = -Math.PI / 2 + i * 2 * Math.PI / 5; return [cx + Math.cos(an) * rad * 1.5, cy + Math.sin(an) * rad * .78]; });
    var links = [[0, 1, G.am[1]], [0, 2, G.am[1]], [1, 2, G.am[1]], [3, 4, G.am[1]], [1, 2, G.mi[1]]];
    links.forEach(function (l, i) { var u = ease(fadeIn(lt, 2.2 + i * .5, .5)); if (u <= 0) return; var p = pts[l[0]], q = pts[l[1]];
      x.strokeStyle = l[2]; x.lineWidth = 4; x.setLineDash([8, 7]); x.lineDashOffset = -T * 30; x.beginPath(); x.moveTo(p[0], p[1]); x.lineTo(p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u); x.stroke(); x.setLineDash([]); });
    pts.forEach(function (p, i) { var u = pop(fadeIn(lt, 1.2 + i * .18, .4)); if (u <= 0) return; x.save(); x.translate(p[0], p[1]); x.scale(u, u);
      box(-70, -22, 140, 44, 22, '#fff', MEDS[i][1], 3); pill(-44, 0, MEDS[i][1], .55); txt(MEDS[i][0], 6, 1, 14, INK, 800, 'center'); x.restore(); });
  },
  function add(lt, T) {
    box(R + 10, 90, 850, 470, 18, '#fff', '#dfe6f0', 2); txt('Add a medicine', R + 40, 130, 22, NAVY, 800);
    var typed = 'losar'.slice(0, Math.max(0, Math.min(5, Math.floor((lt - .6) / .18))));
    box(R + 40, 154, 520, 48, 10, '#f8fafc', TEAL, 2.5); txt(typed + (Math.floor(T * 2) % 2 ? '|' : ''), R + 58, 178, 19, INK, 600);
    if (lt > 1.6 && lt < 2.9) { box(R + 40, 206, 520, 92, 10, '#fff', '#cbd5e1', 1.5); box(R + 44, 210, 512, 40, 8, '#ecfeff'); txt('Losartan', R + 58, 230, 17, INK, 800); txt('generic', R + 160, 230, 14, '#64748b', 600);
      txt('Losartan + hydrochlorothiazide', R + 58, 272, 16, '#475569', 600); }
    var n = lt < 2.9 ? 0 : Math.min(5, 1 + Math.floor((lt - 2.9) / .4)), xx = R + 40, yy = 236;
    for (var i = 0; i < n; i++) { var m = [MEDS[1], MEDS[0], MEDS[2], MEDS[3], MEDS[4]][i]; x.font = '800 16px ' + F; var w = x.measureText(m[0]).width + 84;
      if (xx + w > R + 840) { xx = R + 40; yy += 54; } var u = pop(fadeIn(lt, 2.9 + i * .4, .35)); x.save(); x.translate(xx + w / 2, yy + 22); x.scale(u, u);
      box(-w / 2, -22, w, 44, 22, '#fff', m[1], 2.5); pill(-w / 2 + 24, 0, m[1], .5); txt(m[0], -w / 2 + 46, 1, 16, INK, 800); txt('☆', w / 2 - 18, 1, 16, GOLD, 800, 'center'); x.restore(); xx += w + 12; }
    var f = ease(fadeIn(lt, 3.6, .5)); x.save(); x.globalAlpha = f; txt('★ Favorites', R + 40, 420, 16, GOLD, 800); txt('Recent', R + 160, 420, 16, '#64748b', 700);
    var pr = lt > 5.0 && lt < 5.4; box(R + 40, 460 + (pr ? 2 : 0), 270, 46, 23, pr ? DTEAL : TEAL); txt('Paste a medication list', R + 175, 483 + (pr ? 2 : 0), 17, '#fff', 800, 'center'); x.restore();
  },
  function kidneyFn(lt, T) {
    box(R + 10, 90, 470, 470, 18, '#fff', '#dfe6f0', 2); txt('Kidney function', R + 40, 130, 22, NAVY, 800);
    var opts = ['Not specified', 'eGFR or CrCl 60 or more', 'eGFR or CrCl 30 to 59', 'eGFR or CrCl 15 to 29', 'Below 15, not on dialysis', 'Hemodialysis', 'Peritoneal dialysis', 'CRRT'];
    var sel = lt < .8 ? 0 : Math.min(5, Math.floor((lt - .8) / .45));
    opts.forEach(function (o, i) { var y = 168 + i * 47; var on = i === sel; box(R + 40, y, 410, 40, 8, on ? '#ecfeff' : '#f8fafc', on ? TEAL : '#e2e8f0', on ? 3 : 1.5);
      txt(o, R + 58, y + 20, 16, on ? DTEAL : '#334155', on ? 800 : 600); if (on && i === 5 && lt > 3.4) txt('✓', R + 426, y + 20, 18, TEAL, 800, 'center'); });
    var u = pop(fadeIn(lt, 4.6, .5)); if (u > 0) { x.save(); x.globalAlpha = Math.min(1, u); x.translate(0, (1 - u) * 20);
      box(R + 510, 170, 350, 210, 18, '#eef2ff', '#6366f1', 2.5); box(R + 534, 194, 44, 44, 11, '#312e81'); txt('⌗', R + 556, 216, 24, '#fff', 800, 'center');
      txt('From Calculo', R + 592, 216, 20, '#312e81', 800); txt('eGFR', R + 534, 278, 16, '#475569', 700); txt('24', R + 534, 322, 46, '#312e81', 800); txt('mL/min/1.73 m²', R + 600, 330, 14, '#475569', 600);
      x.restore(); }
    var v = ease(fadeIn(lt, 6.4, .5)); if (v > 0) { x.save(); x.globalAlpha = v; box(R + 510, 400, 350, 56, 14, '#fff', TEAL, 2); txt('→ filled in: eGFR or CrCl 15 to 29', R + 530, 428, 16, DTEAL, 800); x.restore(); }
  },
  function grades(lt, T) {
    var gs = [G.ci, G.av, G.am, G.mi], txts = ['The source says the combination must not be used.', 'Avoid; use only with specialist reason and close monitoring.', 'Usually usable with a dose change, spacing, or monitoring.', 'Small or uncommon effect; awareness is enough.'];
    gs.forEach(function (g, i) { var u = pop(fadeIn(lt, .5 + i * .9, .45)); if (u <= 0) return; var y = 96 + i * 92; x.save(); x.globalAlpha = Math.min(1, u); x.translate((1 - u) * 40, 0);
      box(R + 10, y, 850, 76, 14, '#fff', g[1], 2.5); box(R + 10, y, 14, 76, 7, g[1]); chip(R + 40, y + 20, g[0], g[1], '#fff', 16, 36); txt(txts[i], R + 280, y + 38, 16, '#334155', 600); x.restore(); });
    var w = ease(fadeIn(lt, 5.2, .5)); if (w > 0) { x.save(); x.globalAlpha = w; box(R + 10, 476, 850, 92, 14, '#f8fafc', '#cbd5e1', 1.5);
      txt('What happens', R + 36, 506, 17, NAVY, 800); txt('What to do', R + 36, 544, 17, TEAL, 800); x.fillStyle = '#cbd5e1'; x.fillRect(R + 190, 503, 380, 7); x.fillRect(R + 190, 541, 460, 7); x.restore(); }
  },
  function example(lt, T) {
    box(R + 10, 84, 850, 330, 16, '#fff', G.am[1], 2.5);
    pill(R + 50, 124, GOLD, .8); txt('Atorvastatin  +  Clarithromycin', R + 80, 124, 22, INK, 800); chip(R + 640, 108, G.am[0], G.am[1], '#fff', 15, 32);
    txt('From the Atorvastatin monograph', R + 40, 168, 14, '#64748b', 700);
    var a = ease(fadeIn(lt, 1.2, .5)); x.save(); x.globalAlpha = a; txt('What happens', R + 40, 214, 17, NAVY, 800);
    txt('Higher atorvastatin levels (CYP3A4/transporter inhibition).', R + 40, 244, 17, '#334155', 600); x.restore();
    var b = ease(fadeIn(lt, 4.4, .5)); x.save(); x.globalAlpha = b; txt('What to do', R + 40, 300, 17, TEAL, 800);
    txt('Do not exceed atorvastatin 20 mg; monitor for myopathy.', R + 40, 330, 17, '#334155', 700); x.restore();
    // level gauge rising
    var g = ease(fadeIn(lt, 1.8, 2.2)); box(R + 40, 440, 820, 120, 14, '#f8fafc', '#e2e8f0', 1.5); txt('Atorvastatin level', R + 64, 470, 15, '#475569', 700);
    box(R + 64, 496, 760, 26, 13, '#e2e8f0'); var grd = x.createLinearGradient(R + 64, 0, R + 824, 0); grd.addColorStop(0, '#16a34a'); grd.addColorStop(.6, '#f59e0b'); grd.addColorStop(1, '#b91c1c');
    box(R + 64, 496, 300 + 380 * g, 26, 13, grd); if (g > .2) txt('↑ with clarithromycin', R + 364 + 380 * g - 12, 540, 14, AMBER, 800, 'right');
  },
  function kidneys(lt, T) {
    var u = ease(fadeIn(lt, .4, 1.4)); var tri = [[MEDS[0], -1], [MEDS[1], 0], [MEDS[2], 1]];
    kidney(R + 210, 260, 1.5, 'rgba(185,28,28,' + (0.2 + 0.25 * u) + ')');
    tri.forEach(function (t, i) { var sx = R + 60 + i * 150, sy = 470, ex2 = R + 210 + t[1] * 140, ey = 150 + (i === 1 ? -40 : 0); var px = sx + (ex2 - sx) * u, py = sy + (ey - sy) * u;
      box(px - 66, py - 20, 132, 40, 20, '#fff', t[0][1], 2.5); txt(t[0][0], px, py + 1, 14, INK, 800, 'center'); });
    var w = pop(fadeIn(lt, 2.4, .5)); if (w > 0) { x.save(); x.globalAlpha = Math.min(1, w); box(R + 40, 520, 350, 50, 12, '#fff7e6', '#f0c674', 2); txt('⚠  "Triple whammy"', R + 64, 545, 19, '#6b4200', 800); x.restore(); }
    var t2 = ease(fadeIn(lt, 4.6, .5)); x.save(); x.globalAlpha = t2;
    box(R + 420, 84, 440, 486, 16, '#fff', '#dfe6f0', 2); txt('Kidney dosing (hemodialysis)', R + 444, 118, 18, NAVY, 800);
    [['Ibuprofen', 'Not recommended', '#fee2e2', '#991b1b'], ['Losartan', 'No adjustment; not dialyzed', '#dcfce7', '#14532d'], ['Clarithromycin', 'As CrCl <30: halve dose', '#fef3c7', '#78350f'], ['Atorvastatin', 'No dose change', '#dcfce7', '#14532d']].forEach(function (r, i) {
      var v = ease(fadeIn(lt, 5.0 + i * .45, .35)); if (v <= 0) return; var y = 150 + i * 98; x.save(); x.globalAlpha = v * t2;
      txt(r[0], R + 444, y + 18, 16, INK, 800); box(R + 444, y + 38, 392, 44, 10, r[2]); txt(r[1], R + 460, y + 60, 16, r[3], 800); x.restore(); });
    x.restore();
  },
  function limits(lt, T) {
    var a = pop(fadeIn(lt, .3, .5)); x.save(); x.globalAlpha = Math.min(1, a);
    box(R + 10, 90, 850, 130, 18, '#fff7e6', '#f0c674', 2.5); txt('No result does not mean no interaction.', R + 40, 140, 28, '#6b4200', 800); txt('Check the full prescribing information.', R + 40, 184, 20, '#6b4200', 700); x.restore();
    var btns = [['🔗  Copy link', TEAL, 4.2], ['🖨  Print', NAVY, 5.2], ['Med Scheduler  →', '#0e4a50', 6.2]];
    btns.forEach(function (b, i) { var u = pop(fadeIn(lt, b[2], .45)); if (u <= 0) return; x.save(); x.globalAlpha = Math.min(1, u); var X = R + 10 + i * 290; x.translate(X + 135, 330); x.scale(u, u);
      box(-135, -36, 270, 72, 36, b[1]); txt(b[0], 0, 1, 20, '#fff', 800, 'center'); x.restore(); });
    var c = lt > 4.6 && lt < 5.6; if (c) { box(R + 40, 390, 210, 36, 18, '#dcfce7'); txt('✓ Link copied', R + 145, 408, 15, '#14532d', 800, 'center'); }
    var s = ease(fadeIn(lt, 6.8, .6)); if (s > 0) { x.save(); x.globalAlpha = s; box(R + 470, 400, 390, 140, 14, '#fff', '#dfe6f0', 2); txt('Daily schedule', R + 494, 430, 17, NAVY, 800);
      [['7:00 AM', [GOLD]], ['6:30 PM', [NAVY, TEAL]], ['10:00 PM', [GOLD]]].forEach(function (r, i) { txt(r[0], R + 494, 466 + i * 26, 14, INK, 700); r[1].forEach(function (c2, j) { pill(R + 620 + j * 50, 466 + i * 26, c2, .6); }); }); x.restore(); }
  },
  function end(lt, T) {
    var a = pop(fadeIn(lt, .2, .6)); x.save(); x.globalAlpha = Math.min(1, a);
    box(R + 30, 130, 820, 210, 20, '#fff', TEAL, 2.5); box(R + 60, 164, 64, 64, 16, '#0e4a50'); pill(R + 92, 196, '#fbbf24', 1.0);
    txt('Interaction Checker', R + 144, 182, 32, NAVY, 800); txt('in Dosis, the Drug Index', R + 144, 218, 22, TEAL, 700);
    txt('renalcarematters.com/drugs/interactions', R + 60, 290, 22, INK, 700); x.restore();
    var b = ease(fadeIn(lt, 3.6, .6)); x.save(); x.globalAlpha = b; box(R + 30, 380, 820, 70, 16, '#f8fafc', '#e2e8f0', 1.5);
    txt('★  Favorites and recent medicines stay on this device', R + 60, 415, 19, '#475569', 700); x.restore();
  }
];
