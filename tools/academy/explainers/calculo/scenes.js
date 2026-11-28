/* ---------- Calculo scenes ---------- */
var R = 400, IND = '#312e81', IND2 = '#3730a3', AMBER = '#b45309';
function chip(X, Y, label, bg, fg, sz, h) { sz = sz || 15; h = h || 30; x.font = '700 ' + sz + 'px ' + F; var w = x.measureText(label).width + 24; box(X, Y, w, h, h / 2, bg); txt(label, X + w / 2, Y + h / 2, sz, fg, 700, 'center'); return w; }
function calcIcon(X, Y, s, col) { x.save(); x.translate(X, Y); x.scale(s, s); box(-16, -20, 32, 40, 6, col); box(-11, -15, 22, 9, 2, 'rgba(255,255,255,.85)');
  for (var r = 0; r < 3; r++) for (var c = 0; c < 3; c++) box(-11 + c * 8, -2 + r * 7, 6, 5, 1, 'rgba(255,255,255,.7)'); x.restore(); }
function field(X, Y, w, label, val, hl) { txt(label, X, Y, 14, '#475569', 700); box(X, Y + 12, w, 38, 8, hl ? '#fef3c7' : '#f8fafc', hl ? '#f59e0b' : '#cbd5e1', hl ? 2 : 1.5); txt(val, X + 12, Y + 31, 17, INK, 700); }
function card(X, Y, w, h, title) { box(X, Y, w, h, 14, '#fff', '#dfe6f0', 2); x.save(); rr(X, Y, w, h, 14); x.clip(); x.fillStyle = TEAL; x.fillRect(X, Y, w, 5); x.restore(); txt(title, X + 22, Y + 34, 19, NAVY, 800); }
var CATS = [['Kidney Function & GFR', '#1a6b72'], ['Pharmacology & Dosing', '#0d9488'], ['Dialysis Adequacy & Fluid', '#1f3864'], ['Fluids, Electrolytes & Acid–Base', '#6b21a8'],
  ['Minerals, Anemia & Iron', '#b91c1c'], ['Nutrition, Body & Lifestyle', '#166534'], ['Acute Kidney Injury', '#0f766e'], ['Critical Care & Emergency', '#dc2626']];
var scenes = [
  function title(lt, T) {
    var a = pop(fadeIn(lt, .2, .7)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 30);
    box(R + 10, 66, 520, 58, 29, 'rgba(49,46,129,.10)'); txt('RENAL CARE MATTERS  ·  CALCULO', R + 40, 95, 18, IND, 800);
    txt('Calculo', R + 30, 196, 84, NAVY, 800); txt('clinical calculators for kidney care', R + 32, 262, 34, GOLD, 800); x.restore();
    var cols = CATS.map(function (c) { return c[1]; }); var n = 0;
    for (var r = 0; r < 4; r++) for (var c = 0; c < 9; c++) { var i = r * 9 + c, u = pop(fadeIn(lt, 1.6 + i * .06, .35)); if (u <= 0) continue; n++;
      x.save(); x.translate(R + 60 + c * 64, 340 + r * 62); x.scale(u * .9, u * .9); calcIcon(0, 0, 1, cols[i % cols.length]); x.restore(); }
    var b = pop(fadeIn(lt, 4.4, .5)); if (b > 0) { x.save(); x.globalAlpha = Math.min(1, b); box(R + 640, 360, 210, 150, 20, IND);
      txt('250+', R + 745, 418, 54, '#fff', 800, 'center'); txt('calculators · free', R + 745, 470, 17, '#e0e7ff', 700, 'center'); x.restore(); }
  },
  function browse(lt, T) {
    box(R + 10, 84, 850, 480, 18, '#fff', '#dfe6f0', 2);
    var typed = 'egfr'.slice(0, Math.max(0, Math.min(4, Math.floor((lt - .5) / .2))));
    box(R + 40, 110, 790, 50, 25, '#f8fafc', IND2, 2.5); txt('⌕', R + 66, 135, 22, IND2, 800, 'center'); txt(typed || 'Search calculators', R + 88, 135, 18, typed ? INK : '#94a3b8', 600);
    if (lt > 1.4 && lt < 4.0) { var res = ['CKD-EPI 2021 eGFR', 'eGFR (cystatin C)', 'Cockcroft–Gault CrCl']; res.forEach(function (r2, i) { var u = ease(fadeIn(lt, 1.4 + i * .15, .3));
      x.save(); x.globalAlpha = u; box(R + 40, 172 + i * 46, 790, 40, 10, i === 0 ? '#eef2ff' : '#fff', '#e2e8f0', 1.5); calcIcon(R + 64, 192 + i * 46, .55, '#1a6b72'); txt(r2, R + 88, 192 + i * 46, 16, INK, 700); x.restore(); }); }
    var g = ease(fadeIn(lt, 3.8, .4)); if (g > 0) { x.save(); x.globalAlpha = g; txt('23 categories', R + 40, 196, 18, NAVY, 800);
      CATS.forEach(function (c, i) { var u = pop(fadeIn(lt, 4.0 + i * .18, .35)); if (u <= 0) return; var col = i % 2, row = Math.floor(i / 2);
        x.save(); x.translate(R + 40 + col * 400, 226 + row * 74); x.scale(1, u); box(0, 0, 384, 60, 12, '#fff', c[1], 2.5); box(0, 0, 10, 60, 5, c[1]); calcIcon(36, 30, .6, c[1]); txt(c[0], 62, 30, 15.5, INK, 800); x.restore(); });
      x.restore(); }
  },
  function cardScene(lt, T) {
    card(R + 10, 84, 520, 470, 'CKD-EPI 2021 eGFR');
    txt('Units', R + 32, 140, 14, '#475569', 700); var si = lt > 3.2 && lt < 4.6; box(R + 90, 126, 90, 28, 14, si ? '#f1f5f9' : TEAL); txt('mg/dL', R + 135, 140, 13, si ? '#475569' : '#fff', 800, 'center');
    box(R + 186, 126, 90, 28, 14, si ? TEAL : '#f1f5f9'); txt('µmol/L', R + 231, 140, 13, si ? '#fff' : '#475569', 800, 'center');
    var v = [fadeIn(lt, .6, .2) > .5, fadeIn(lt, 1.2, .2) > .5, fadeIn(lt, 1.8, .2) > .5];
    field(R + 32, 176, 220, 'Age (years)', v[0] ? '62' : '', false); field(R + 272, 176, 236, 'Sex', v[1] ? 'Female' : '', false);
    field(R + 32, 252, 476, 'Serum creatinine', v[2] ? (si ? '124 µmol/L' : '1.4 mg/dL') : '', false);
    var r = ease(fadeIn(lt, 2.2, .5)); if (r > 0) { x.save(); x.globalAlpha = r; box(R + 32, 336, 476, 150, 14, '#ecfeff', TEAL, 2);
      txt('eGFR', R + 54, 366, 15, DTEAL, 800); txt('43', R + 54, 420, 60, DTEAL, 800); txt('mL/min/1.73 m²', R + 140, 432, 17, '#334155', 700);
      chip(R + 360, 404, 'Stage G3b', '#0e4a50', '#fff', 15, 34); x.restore(); }
    var t = ease(fadeIn(lt, 4.4, .5)); if (t > 0) { x.save(); x.globalAlpha = t; box(R + 560, 180, 300, 200, 16, '#fff', '#dfe6f0', 2);
      txt('Result at once', R + 584, 214, 18, NAVY, 800); txt('No "Calculate" button:', R + 584, 250, 15, '#475569', 600); txt('it updates as you type.', R + 584, 274, 15, '#475569', 600);
      txt('Tabular numbers, one', R + 584, 316, 15, '#475569', 600); txt('Units row per calculator.', R + 584, 340, 15, '#475569', 600); x.restore(); }
  },
  function sample(lt, T) {
    card(R + 10, 84, 600, 470, 'Kidney Failure Risk Equation (KFRE)');
    var on = lt > 1.6 && lt < 5.6, pr = lt > 1.4 && lt < 1.7, cl = lt > 5.4 && lt < 5.7;
    box(R + 32, 112 + 0, 0, 0, 0);
    var b1 = on ? '#b45309' : IND2; box(R + 380, 114 + (pr ? 2 : 0), 210, 40, 20, on ? '#fff7ed' : IND2, on ? '#b45309' : IND2, 2);
    txt(on ? 'Clear sample' : 'Sample data', R + 485, 134 + (pr ? 2 : 0), 15, on ? '#9a3412' : '#fff', 800, 'center');
    field(R + 32, 176, 260, 'Age (years)', on ? '58' : '', on); field(R + 312, 176, 276, 'Sex', on ? 'Male' : '', on);
    field(R + 32, 252, 260, 'eGFR', on ? '28' : '', on); field(R + 312, 252, 276, 'Urine ACR (mg/g)', on ? '450' : '', on);
    if (on) { box(R + 32, 340, 556, 44, 10, '#fff7e6', '#f0c674', 1.5); txt('Sample values are amber, and never saved as patient values.', R + 48, 362, 14.5, '#6b4200', 700); }
    var c = lt > 5.6 ? ease(fadeIn(lt, 5.6, .4)) : 0; if (c > 0) { x.save(); x.globalAlpha = c; box(R + 32, 340, 556, 44, 10, '#ecfeff', TEAL, 1.5); txt('Your own values are back.', R + 48, 362, 15, DTEAL, 800); x.restore(); }
    if (pr || cl) { x.strokeStyle = 'rgba(55,48,163,.6)'; x.lineWidth = 4; x.beginPath(); x.arc(R + 485, 134, 30, 0, Math.PI * 2); x.stroke(); }
  },
  function handoff(lt, T) {
    var a = pop(fadeIn(lt, .3, .5)); x.save(); x.globalAlpha = Math.min(1, a); box(R + 260, 86, 380, 90, 45, IND);
    txt('Age 62  ·  58 kg  ·  Cr 1.4 mg/dL', R + 450, 131, 19, '#fff', 800, 'center'); x.restore();
    var cards = [['Cockcroft–Gault', [['Age', '62'], ['Weight', '58 kg'], ['Creatinine', '1.4']]], ['CKD-EPI 2021', [['Age', '62'], ['Creatinine', '1.4'], ['Sex', '—']]], ['Body surface area', [['Weight', '58 kg'], ['Height', '—']]]];
    cards.forEach(function (c, i) { var X = R + 10 + i * 290, u = ease(fadeIn(lt, 1.4 + i * .5, .5)); if (u <= 0) return;
      var y0 = 176, y1 = 250; x.strokeStyle = 'rgba(55,48,163,' + (.5 * u) + ')'; x.lineWidth = 3; x.setLineDash([7, 7]); x.lineDashOffset = -T * 30;
      x.beginPath(); x.moveTo(R + 450, y0); x.lineTo(X + 140, y1); x.stroke(); x.setLineDash([]);
      x.save(); x.globalAlpha = u; card(X, 250, 280, 250, c[0]);
      c[1].forEach(function (f, j) { var filled = f[1] !== '—' && lt > 2.0 + i * .5 + j * .25; txt(f[0], X + 22, 312 + j * 60, 13.5, '#475569', 700);
        box(X + 22, 322 + j * 60, 236, 30, 7, filled ? '#eef2ff' : '#f8fafc', filled ? '#818cf8' : '#cbd5e1', 1.5); if (filled) txt(f[1], X + 34, 337 + j * 60, 15, INK, 800); });
      x.restore(); });
    var s = ease(fadeIn(lt, 5.6, .5)); if (s > 0) { x.save(); x.globalAlpha = s; box(R + 250, 520, 400, 40, 20, '#f8fafc', '#cbd5e1', 1.5); txt('🔒  Saved only on this device', R + 450, 540, 16, '#334155', 800, 'center'); x.restore(); }
  },
  function formula(lt, T) {
    card(R + 10, 84, 850, 470, 'CKD-EPI 2021 eGFR');
    box(R + 32, 132, 806, 50, 10, '#f8fafc', '#cbd5e1', 1.5); var o = lt > 1.0; txt((o ? '▾' : '▸') + '  Formula, sources & limitations', R + 50, 157, 17, IND2, 800);
    var a = ease(fadeIn(lt, 1.1, .5)); if (a > 0) { x.save(); x.globalAlpha = a;
      txt('Formula', R + 50, 214, 15, NAVY, 800); box(R + 50, 228, 770, 48, 8, '#0f172a');
      txt('eGFR = 142 × min(Scr/κ, 1)^α × max(Scr/κ, 1)^−1.200 × 0.9938^age × 1.012 [female]', R + 64, 252, 14.5, '#e2e8f0', 700);
      var b = ease(fadeIn(lt, 2.6, .5)); x.globalAlpha = a * b; txt('Source', R + 50, 314, 15, NAVY, 800);
      txt('Inker LA, et al. New creatinine- and cystatin C–based equations to estimate GFR', R + 50, 342, 14.5, '#334155', 600); txt('without race. N Engl J Med. 2021;385:1737–1749.', R + 50, 364, 14.5, '#334155', 600);
      var c = ease(fadeIn(lt, 4.4, .5)); x.globalAlpha = a * c; txt('Limitations', R + 50, 410, 15, '#9a3412', 800);
      txt('Needs a stable creatinine: not for acute kidney injury. Less accurate at extremes', R + 50, 438, 14.5, '#334155', 600); txt('of muscle mass, in pregnancy and in children.', R + 50, 460, 14.5, '#334155', 600);
      x.restore(); }
  },
  function install(lt, T) {
    var d = ease(fadeIn(lt, .3, .6)); var X = R + 10 - (1 - d) * 420;
    box(R + 440, 84, 420, 470, 18, '#f8fafc', '#e2e8f0', 1.5); for (var i = 0; i < 6; i++) { x.fillStyle = '#e2e8f0'; x.fillRect(R + 470, 130 + i * 56, 320 - (i % 3) * 50, 12); }
    box(R + 440, 290, 46, 120, 12, IND); txt('C', R + 463, 350, 20, '#fff', 800, 'center');
    x.save(); x.globalAlpha = d; box(X, 84, 410, 470, 18, '#eef2ff', '#c7d2fe', 2); box(X + 22, 106, 40, 40, 10, IND); calcIcon(X + 42, 126, .7, '#6366f1');
    txt('Calculo: the calculators', X + 74, 118, 18, IND, 800); txt('as an app', X + 74, 140, 18, IND, 800);
    box(X + 22, 170, 366, 110, 12, '#fff', '#e2e8f0', 1.5); txt('Install on your phone or computer', X + 38, 196, 15, INK, 800);
    var pi = lt > 2.0 && lt < 2.4; box(X + 38, 222 + (pi ? 2 : 0), 160, 40, 20, IND2); txt('Install Calculo', X + 118, 242 + (pi ? 2 : 0), 15, '#fff', 800, 'center');
    box(X + 22, 296, 366, 150, 12, '#fff', '#e2e8f0', 1.5); txt('Offline use', X + 38, 322, 15, INK, 800);
    box(X + 38, 340, 250, 40, 20, IND2); txt('Download every calculator', X + 163, 360, 14, '#fff', 800, 'center');
    var p = Math.max(0, Math.min(1, (lt - 3.4) / 3.6)); box(X + 38, 396, 334, 10, 5, '#e2e8f0'); if (p > 0) box(X + 38, 396, 334 * p, 10, 5, IND2);
    txt(p >= 1 ? 'Every calculator is saved on this device.' : 'Saving ' + Math.floor(p * 100) + '%…', X + 38, 426, 14, p >= 1 ? '#166534' : '#475569', 700); x.restore();
    var ph = pop(fadeIn(lt, 7.6, .5)); if (ph > 0) { x.save(); x.globalAlpha = Math.min(1, ph); box(R + 560, 150, 220, 380, 30, '#111827'); box(R + 572, 170, 196, 340, 18, '#fff');
      txt('No signal', R + 670, 200, 14, '#b91c1c', 800, 'center'); x.strokeStyle = '#b91c1c'; x.lineWidth = 3; x.beginPath(); x.moveTo(R + 612, 196); x.lineTo(R + 628, 206); x.stroke();
      card(R + 582, 222, 176, 150, 'eGFR'); txt('43', R + 604, 320, 40, DTEAL, 800); txt('✓ Works offline', R + 670, 410, 15, '#166534', 800, 'center'); x.restore(); }
  },
  function end(lt, T) {
    var a = pop(fadeIn(lt, .2, .6)); x.save(); x.globalAlpha = Math.min(1, a);
    box(R + 30, 110, 820, 150, 20, '#fff7e6', '#f0c674', 2.5); txt('Supports your judgment,', R + 60, 162, 38, '#6b4200', 800); txt('never replaces it.', R + 60, 212, 30, '#6b4200', 700); x.restore();
    var b = ease(fadeIn(lt, 3.4, .6)); x.save(); x.globalAlpha = b; box(R + 30, 300, 820, 210, 20, '#fff', IND2, 2.5);
    box(R + 60, 334, 64, 64, 16, IND); calcIcon(R + 92, 366, .95, '#6366f1'); txt('Calculo', R + 144, 352, 34, NAVY, 800); txt('Clinical Calculators & Tools', R + 144, 388, 22, IND2, 700);
    txt('renalcarematters.com/guides/calculators', R + 60, 460, 22, INK, 700); x.restore();
  }
];
