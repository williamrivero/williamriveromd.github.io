/* ---------- Paratus scenes ---------- */
var R = 400, RED = '#991b1b', DRED = '#7f1d1d', AMBER = '#b45309';
function chip(X, Y, label, bg, fg, sz, h) { sz = sz || 15; h = h || 30; x.font = '700 ' + sz + 'px ' + F; var w = x.measureText(label).width + 24; box(X, Y, w, h, h / 2, bg); txt(label, X + w / 2, Y + h / 2, sz, fg, 700, 'center'); return w; }
function appIcon(X, Y, s) { x.save(); x.translate(X, Y); x.scale(s, s); box(-50, -50, 100, 100, 24, DRED);
  x.strokeStyle = '#fff'; x.lineWidth = 7; x.lineJoin = 'round'; x.lineCap = 'round'; x.beginPath(); x.moveTo(-36, 4); x.lineTo(-14, 4); x.lineTo(-6, -10); x.lineTo(4, 26); x.lineTo(14, -30); x.lineTo(22, 4); x.lineTo(36, 4); x.stroke(); x.restore(); }
function bars(X, Y, w, n, col) { for (var i = 0; i < n; i++) box(X, Y + i * 14, w * (i === n - 1 ? .6 : 1), 7, 3.5, col || '#e2e8f0'); }
function wrapTxt(s, X, Y, maxW, size, color, weight, lh) { x.font = (weight || 600) + ' ' + size + 'px ' + F; var wds = s.split(' '), line = '', yy = Y;
  wds.forEach(function (w) { var t = line ? line + ' ' + w : w; if (x.measureText(t).width > maxW && line) { txt(line, X, yy, size, color, weight); line = w; yy += lh; } else line = t; }); if (line) txt(line, X, yy, size, color, weight); return yy; }
/* icons */
function icon(kind, X, Y, s, col) { x.save(); x.translate(X, Y); x.scale(s, s); x.strokeStyle = col; x.fillStyle = col; x.lineWidth = 5; x.lineCap = 'round'; x.lineJoin = 'round';
  if (kind === 'storm') { x.beginPath(); x.arc(-8, -6, 14, Math.PI, 0); x.arc(10, -2, 11, Math.PI * 1.3, Math.PI * .5); x.lineTo(-22, 9); x.arc(-22, -2, 11, Math.PI * .5, Math.PI * 1.5); x.fill();
    for (var i = 0; i < 3; i++) { x.beginPath(); x.moveTo(-12 + i * 11, 16); x.lineTo(-16 + i * 11, 26); x.stroke(); } }
  else if (kind === 'quake') { x.beginPath(); x.moveTo(-18, 18); x.lineTo(-18, -8); x.lineTo(0, -24); x.lineTo(18, -8); x.lineTo(18, 18); x.closePath(); x.stroke();
    x.lineWidth = 3.5; x.beginPath(); x.moveTo(2, -14); x.lineTo(-4, -2); x.lineTo(4, 6); x.lineTo(-2, 18); x.stroke(); x.lineWidth = 4;
    x.beginPath(); x.moveTo(-30, 26); x.lineTo(-20, 22); x.lineTo(-10, 28); x.lineTo(0, 22); x.lineTo(10, 28); x.lineTo(20, 22); x.lineTo(30, 26); x.stroke(); }
  else if (kind === 'fire') { x.beginPath(); x.moveTo(0, 26); x.bezierCurveTo(-24, 24, -24, 0, -12, -10); x.bezierCurveTo(-10, 0, -4, 2, -4, -4); x.bezierCurveTo(-6, -16, 2, -24, 6, -28); x.bezierCurveTo(8, -14, 24, -6, 20, 10); x.bezierCurveTo(18, 22, 8, 26, 0, 26); x.fill(); }
  else if (kind === 'bolt') { x.beginPath(); x.moveTo(6, -28); x.lineTo(-16, 4); x.lineTo(-2, 4); x.lineTo(-8, 28); x.lineTo(16, -6); x.lineTo(2, -6); x.closePath(); x.fill(); }
  else if (kind === 'sun') { x.beginPath(); x.arc(0, 0, 10, 0, Math.PI * 2); x.fill(); for (var k = 0; k < 8; k++) { var a = k * Math.PI / 4; x.beginPath(); x.moveTo(Math.cos(a) * 16, Math.sin(a) * 16); x.lineTo(Math.cos(a) * 25, Math.sin(a) * 25); x.stroke(); } }
  else if (kind === 'list') { box(-18, -24, 36, 48, 6, null, col, 5); for (var j = 0; j < 3; j++) { x.beginPath(); x.moveTo(-9, -10 + j * 11); x.lineTo(9, -10 + j * 11); x.stroke(); } }
  else if (kind === 'heart') { x.beginPath(); x.moveTo(0, 22); x.bezierCurveTo(-30, 2, -22, -24, 0, -10); x.bezierCurveTo(22, -24, 30, 2, 0, 22); x.fill(); }
  x.restore(); }

var CARDS = [['Code on dialysis', '#b91c1c'], ['Blood leak alarm', '#b91c1c'], ['Low blood pressure', '#b45309'], ['Needle dislodgement', '#1f3864'], ['Air embolism', '#1f3864'],
  ['Hemolysis', '#1f3864'], ['Dialyzer reaction', '#1f3864'], ['Chest pain', '#be123c'], ['Arrhythmia', '#be123c'], ['Hyperkalemia', '#be123c'], ['Low blood sugar', '#b45309'],
  ['Seizure', '#b45309'], ['Suspected stroke', '#b45309'], ['Fever and rigors', '#0e7490'], ['Power failure', '#5b21b6'], ['Earthquake', '#5b21b6'], ['Fire or smoke', '#5b21b6'],
  ['Typhoon warning', '#5b21b6'], ['Water failure', '#5b21b6']];
var RES = ['Ready before the collapse', 'How algorithms think', 'Recognizing the algorithm', 'BLS at the dialysis chair', 'Adult cardiac arrest', 'Bradycardia, tachycardia',
  'Arrest in the dialysis chair', 'Hyperkalemia', 'Circuit emergencies', 'Pediatric BLS', 'Pediatric arrest', 'ROSC, transfer, handover', 'Team, code status, debrief'];

var scenes = [
  function title(lt, T) {
    var a = pop(fadeIn(lt, .2, .7)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 30);
    box(R + 10, 66, 520, 58, 29, 'rgba(153,27,27,.10)'); txt('RENAL CARE MATTERS  ·  PARATUS', R + 40, 95, 18, DRED, 800);
    txt('Paratus', R + 30, 196, 84, DRED, 800); txt('Latin for "ready" · emergency readiness', R + 32, 262, 30, GOLD, 800); x.restore();
    var b = pop(fadeIn(lt, 1.4, .6)); if (b > 0) { x.save(); x.translate(R + 735, 175); x.scale(b * 1.3, b * 1.3); appIcon(0, 0, 1); x.restore(); }
    [['Act', '19 quick cards', '#b91c1c'], ['Learn', '25 modules', '#1f3864'], ['Practice', 'megacodes · drills', '#0e7490']].forEach(function (p, i) {
      var u = pop(fadeIn(lt, 2.6 + i * .45, .45)); if (u <= 0) return; x.save(); x.translate(R + 30 + i * 280, 360); x.scale(1, u);
      box(0, 0, 262, 150, 18, '#fff', p[2], 2.5); box(0, 0, 262, 8, 4, p[2]); txt(p[0], 24, 58, 34, p[2], 800); txt(p[1], 24, 106, 18, '#334155', 700); x.restore(); });
  },
  function cards(lt, T) {
    var h = ease(fadeIn(lt, .3, .4)); x.save(); x.globalAlpha = h; txt('Emergency Quick Cards', R + 20, 96, 34, DRED, 800);
    chip(R + 430, 80, '19 one-screen cards', '#fee2e2', DRED, 16, 32); x.restore();
    CARDS.forEach(function (c, i) { var col = i % 4, row = Math.floor(i / 4), u = pop(fadeIn(lt, .8 + i * .22, .35)); if (u <= 0) return;
      var X = R + 20 + col * 212, Y = 140 + row * 88; x.save(); x.translate(X + 100, Y + 36); x.scale(u, u); x.translate(-100, -36);
      var hl = (i === 0 || i === 1) && lt > 4.5 && lt < 7.5 || (i >= 14) && lt > 7.5;
      box(0, 0, 200, 72, 12, hl ? '#fff7ed' : '#fff', c[1], hl ? 3.5 : 2); box(0, 0, 10, 72, 5, c[1]);
      txt(String(i + 1), 28, 20, 13, c[1], 800); wrapTxt(c[0], 28, 40, 162, 15.5, INK, 800, 18); x.restore(); });
  },
  function oneCard(lt, T) {
    var a = ease(fadeIn(lt, .2, .5)); x.save(); x.globalAlpha = a; box(R + 10, 70, 840, 540, 18, '#fff', '#e5e7eb', 2);
    x.save(); rr(R + 10, 70, 840, 540, 18); x.clip(); x.fillStyle = '#5b21b6'; x.fillRect(R + 10, 70, 840, 66); x.restore();
    txt('Card 15', R + 36, 92, 14, '#ede9fe', 800); txt('Power fails during dialysis', R + 36, 118, 26, '#fff', 800);
    var steps = [['Every nurse', 'Stay with your patients: airway, alertness, the access.'], ['Technician', 'Report the power status: generator, stability, fuel.'],
      ['Charge nurse + POD', 'Decide: stay on a stable generator, or begin the take-off.'], ['Chair nurse', 'Return the blood by hand crank, one staff member per patient.']];
    steps.forEach(function (s, i) { var u = ease(fadeIn(lt, .9 + i * .55, .35)); if (u <= 0) return; x.save(); x.globalAlpha = a * u; var Y = 160 + i * 66;
      x.fillStyle = '#5b21b6'; x.beginPath(); x.arc(R + 56, Y + 22, 17, 0, Math.PI * 2); x.fill(); txt(String(i + 1), R + 56, Y + 22, 17, '#fff', 800, 'center');
      var w = chip(R + 88, Y + 8, s[0], '#ede9fe', '#4c1d95', 14, 28); txt(s[1], R + 100 + w, Y + 22, 16.5, INK, 650); x.restore(); });
    var c = pop(fadeIn(lt, 3.6, .45)); if (c > 0) { x.save(); x.globalAlpha = a * Math.min(1, c); var Y = 424; box(R + 36, Y, 790, 90, 12, '#fef2f2', '#b91c1c', 2.5);
      txt('⚠  Critical', R + 56, Y + 24, 17, '#991b1b', 800); txt('Without power the air detector and venous clamp may not work:', R + 56, Y + 50, 15.5, '#7f1d1d', 650);
      txt('one staff member watches each venous line until the clamp is closed.', R + 56, Y + 68, 15.5, '#7f1d1d', 650); x.restore(); }
    var d = ease(fadeIn(lt, 5.4, .4)); if (d > 0) { x.save(); x.globalAlpha = a * d; box(R + 36, 530, 790, 44, 10, '#f8fafc', '#cbd5e1', 1.5);
      txt('▸  Details: other causes, monitoring, circuit, blood return, escalation, restart, records', R + 54, 552, 15, '#475569', 700); x.restore(); }
    x.restore();
  },
  function resus(lt, T) {
    var h = ease(fadeIn(lt, .2, .4)); x.save(); x.globalAlpha = h; txt('Dialysis Team Resuscitation Lab', R + 20, 92, 30, NAVY, 800);
    chip(R + 520, 76, '13 modules', '#e0e7ff', NAVY, 16, 32); x.restore();
    RES.forEach(function (m, i) { var col = i < 7 ? 0 : 1, row = i < 7 ? i : i - 7, u = ease(fadeIn(lt, .6 + i * .32, .3)); if (u <= 0) return;
      x.save(); x.globalAlpha = u; x.translate((1 - u) * 20, 0); var X = R + 20 + col * 300, Y = 128 + row * 64; box(X, Y, 284, 54, 10, '#fff', '#dbe3ee', 1.5);
      box(X, Y, 44, 54, 10, NAVY); txt(String(i + 1), X + 22, Y + 27, 18, '#fff', 800, 'center'); wrapTxt(m, X + 56, Y + 27, 220, 15, INK, 750, 18); x.restore(); });
    var m = ease(fadeIn(lt, 1.2, .6)); if (m > 0) { x.save(); x.globalAlpha = m; monitor(R + 630, 150, 230, 200, T, { rhythm: 'sinus', hr: 78, hrShown: '78', spo2: '97' }); x.restore(); }
  },
  function disaster(lt, T) {
    var h = ease(fadeIn(lt, .2, .4)); x.save(); x.globalAlpha = h; txt('Disaster Preparedness and Response', R + 20, 92, 30, '#5b21b6', 800);
    chip(R + 570, 76, '12 modules', '#ede9fe', '#4c1d95', 16, 32); x.restore();
    var T6 = [['storm', 'Typhoons and floods', '#0369a1'], ['quake', 'Earthquake on the machine', '#92400e'], ['fire', 'Fire and evacuation', '#c2410c'],
      ['bolt', 'Power, water, supplies', '#a16207'], ['sun', 'Heat, ashfall, outbreaks', '#b45309'], ['list', 'Keeping everyone dialyzed', '#1f3864']];
    T6.forEach(function (t, i) { var col = i % 3, row = Math.floor(i / 3), u = pop(fadeIn(lt, .9 + i * .55, .4)); if (u <= 0) return;
      var X = R + 20 + col * 280, Y = 140 + row * 220; x.save(); x.translate(X + 130, Y + 95); x.scale(u, u); x.translate(-130, -95);
      box(0, 0, 260, 190, 18, '#fff', t[2], 2.5); x.fillStyle = 'rgba(0,0,0,.04)'; x.beginPath(); x.arc(130, 72, 48, 0, Math.PI * 2); x.fill();
      icon(t[0], 130, 72, 1.35, t[2]); wrapTxt(t[1], 24, 150, 220, 17, INK, 800, 21); x.restore(); });
  },
  function practice(lt, T) {
    var h = ease(fadeIn(lt, .2, .4)); x.save(); x.globalAlpha = h; txt('Practice', R + 20, 92, 34, '#0e7490', 800); x.restore();
    // facilitator tablet
    var a = ease(fadeIn(lt, .6, .5)); if (a > 0) { x.save(); x.globalAlpha = a; box(R + 20, 128, 270, 250, 18, '#1e293b'); box(R + 32, 140, 246, 226, 10, '#fff');
      txt('Facilitator', R + 48, 164, 16, NAVY, 800); txt('Rhythm', R + 48, 196, 13, '#475569', 700);
      var vf = lt > 3.0; box(R + 48, 208, 214, 34, 8, '#f8fafc', '#cbd5e1', 1.5); txt(vf ? 'Ventricular fibrillation' : 'Sinus rhythm', R + 60, 225, 14, INK, 700);
      txt('HR · SpO₂', R + 48, 262, 13, '#475569', 700); box(R + 48, 274, 100, 30, 8, '#f8fafc', '#cbd5e1', 1.5); box(R + 160, 274, 102, 30, 8, '#f8fafc', '#cbd5e1', 1.5);
      txt(vf ? '—' : '84', R + 60, 289, 14, INK, 700); txt(vf ? '—' : '96', R + 172, 289, 14, INK, 700);
      var pr = lt > 2.8 && lt < 3.1; box(R + 48, 318 + (pr ? 2 : 0), 214, 36, 18, '#0e7490'); txt('Update display', R + 155, 336 + (pr ? 2 : 0), 15, '#fff', 800, 'center'); x.restore();
      x.save(); x.globalAlpha = a; x.setLineDash([8, 8]); x.lineDashOffset = -T * 30; x.strokeStyle = '#0e7490'; x.lineWidth = 3; x.beginPath(); x.moveTo(R + 300, 250); x.lineTo(R + 350, 250); x.stroke(); x.restore(); }
    var m = ease(fadeIn(lt, 1.0, .5)); if (m > 0) { x.save(); x.globalAlpha = m; var vf2 = lt > 3.1;
      monitor(R + 360, 118, 490, 270, T, vf2 ? { rhythm: 'vf', hr: 0, hrShown: '---', spo2: '--', alarm: 'VENTRICULAR FIBRILLATION', capno: true, co2: 10, co2Shown: '10', rr: 10 } : { rhythm: 'sinus', hr: 84, hrShown: '84', spo2: '96', capno: true, co2: 38, co2Shown: '38', rr: 14 });
      txt('Shared monitor display, on a second screen', R + 605, 404, 15, '#334155', 700, 'center'); x.restore(); }
    var d = ease(fadeIn(lt, 4.4, .5)); if (d > 0) { x.save(); x.globalAlpha = d; box(R + 20, 430, 830, 160, 18, '#fff', '#5b21b6', 2.5);
      icon('storm', R + 70, 492, 1.1, '#5b21b6'); txt('Disaster tabletop drill', R + 120, 474, 21, '#4c1d95', 800); txt('Timed injects, a call-down timer and an evacuation sheet', R + 120, 506, 16, '#334155', 650);
      var left = Math.max(0, 300 - Math.floor((lt - 4.4) * 7)), mm = Math.floor(left / 60), ss = left % 60; box(R + 640, 458, 180, 64, 12, '#4c1d95');
      txt('Next inject', R + 730, 476, 13, '#ddd6fe', 700, 'center'); txt(mm + ':' + (ss < 10 ? '0' : '') + ss, R + 730, 504, 28, '#fff', 800, 'center');
      txt('Inject 2 of 6', R + 120, 552, 15, '#6b21a8', 800); box(R + 240, 545, 380, 14, 7, '#ede9fe'); box(R + 240, 545, 380 * Math.min(1, (lt - 4.4) / 3) * .33 + 2, 14, 7, '#7c3aed'); x.restore(); }
  },
  function install(lt, T) {
    var a = ease(fadeIn(lt, .2, .5)); x.save(); x.globalAlpha = a;
    // phone
    var PX = R + 40, PY = 76; box(PX, PY, 300, 540, 36, '#0f172a'); box(PX + 12, PY + 14, 276, 512, 26, '#f8fafc');
    x.save(); rr(PX + 12, PY + 14, 276, 512, 26); x.clip();
    box(PX + 12, PY + 14, 276, 50, 0, '#1f3864'); txt('Emergency Readiness', PX + 150, PY + 40, 15, '#fff', 800, 'center');
    for (var i = 0; i < 5; i++) bars(PX + 36, PY + 90 + i * 70, 226, 3);
    var open = ease(fadeIn(lt, 1.0, .5)), tapT = lt > .8 && lt < 1.05;
    box(PX + 12 - (1 - open) * 0, PY + 200, 30 + (tapT ? 4 : 0), 110, 8, DRED); x.save(); x.translate(PX + 27, PY + 255); x.rotate(-Math.PI / 2); txt('Paratus', 0, 0, 13, '#fff', 800, 'center'); x.restore();
    if (open > 0) { var dw = 240 * open; x.fillStyle = 'rgba(15,23,42,' + (.35 * open) + ')'; x.fillRect(PX + 12, PY + 14, 276, 512);
      box(PX + 12, PY + 14, dw, 512, 0, '#fff'); if (open > .8) { var X = PX + 30;
        appIcon(X + 22, PY + 64, .42); txt('Paratus', X + 52, PY + 58, 20, DRED, 800); txt('Emergency readiness', X + 52, PY + 78, 12.5, '#475569', 700);
        var pi = lt > 2.2 && lt < 2.5; box(X, PY + 116 + (pi ? 2 : 0), 190, 40, 20, RED); txt('Install Paratus', X + 95, PY + 136 + (pi ? 2 : 0), 15, '#fff', 800, 'center');
        box(X, PY + 176, 190, 40, 20, RED); txt('Download everything', X + 95, PY + 196, 14.5, '#fff', 800, 'center');
        var p = Math.max(0, Math.min(1, (lt - 3.2) / 2.6)); box(X, PY + 232, 190, 12, 6, '#fee2e2'); box(X, PY + 232, 190 * p, 12, 6, RED);
        txt(p >= 1 ? '✓ Saved on this device' : 'Saving ' + Math.floor(p * 100) + '%', X, PY + 264, 13.5, p >= 1 ? '#166534' : '#475569', 800);
        txt('One download, about 37 MB', X, PY + 290, 12.5, '#64748b', 650); } }
    // app bar
    box(PX + 12, PY + 476, 276, 50, 0, '#1e293b'); ['Back', 'Home', 'Cards', 'Practice', 'Print'].forEach(function (b, j) { txt(b, PX + 40 + j * 55, PY + 501, 12, '#e2e8f0', 700, 'center'); });
    x.restore(); x.restore();
    var o = pop(fadeIn(lt, 6.2, .5)); if (o > 0) { x.save(); x.globalAlpha = Math.min(1, o); var X = R + 420;
      box(X, 120, 420, 150, 20, '#fff', '#e2e8f0', 2); txt('No signal', X + 30, 160, 20, '#b91c1c', 800);
      for (var k = 0; k < 4; k++) box(X + 30 + k * 18, 230 - k * 14, 12, 14 + k * 14, 3, '#cbd5e1'); x.strokeStyle = '#b91c1c'; x.lineWidth = 4; x.beginPath(); x.moveTo(X + 26, 240); x.lineTo(X + 110, 180); x.stroke();
      txt('No power', X + 200, 160, 20, '#b91c1c', 800); icon('bolt', X + 240, 214, 1.1, '#cbd5e1'); x.beginPath(); x.moveTo(X + 205, 240); x.lineTo(X + 280, 186); x.stroke();
      box(X, 300, 420, 260, 20, '#f0fdf4', '#16a34a', 2.5); txt('✓  Still works offline', X + 30, 340, 22, '#166534', 800);
      ['Quick cards', 'Both courses', 'Megacode and disaster drills'].forEach(function (s, j) { var u = ease(fadeIn(lt, 6.8 + j * .4, .3)); x.globalAlpha = Math.min(1, o) * u;
        txt('•  ' + s, X + 40, 392 + j * 44, 19, INK, 700); }); x.restore(); }
  },
  function outro(lt, T) {
    var a = pop(fadeIn(lt, .2, .6)); x.save(); x.globalAlpha = Math.min(1, a); box(R + 30, 100, 820, 170, 20, '#fff7e6', '#f0c674', 2.5);
    txt('Follow your unit protocol,', R + 60, 150, 34, '#6b4200', 800); txt('and always ask the Attending Nephrologist', R + 60, 198, 26, '#6b4200', 700); txt('for guidance.', R + 60, 234, 26, '#6b4200', 700); x.restore();
    var b = pop(fadeIn(lt, 3.8, .6)); if (b > 0) { x.save(); x.globalAlpha = Math.min(1, b); x.translate(0, (1 - b) * 20);
      appIcon(R + 100, 376, .7); txt('Paratus', R + 156, 360, 38, DRED, 800); txt('Emergency readiness for dialysis teams', R + 156, 400, 21, '#334155', 700);
      txt('renalcarematters.com/paratus', R + 60, 480, 24, INK, 800); x.restore(); }
  }
];
