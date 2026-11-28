/* ---------- Med Scheduler scenes (lt = seconds into the scene) ---------- */
var R = 400, PURPLE = '#6b46c1', AMBER = '#b45309';
function pill(X, Y, col, s) { s = s || 1; x.save(); x.translate(X, Y); x.scale(s, s); rr(-22, -10, 44, 20, 10); x.fillStyle = '#fff'; x.fill(); x.strokeStyle = col; x.lineWidth = 2.5; x.stroke();
  x.beginPath(); x.moveTo(0, -10); x.lineTo(0, 10); x.stroke(); rr(-22, -10, 22, 20, 10); x.fillStyle = col; x.fill(); x.restore(); }
function chip(X, Y, label, bg, fg, sz) { x.font = '700 ' + (sz || 15) + 'px ' + F; var w = x.measureText(label).width + 24; box(X, Y, w, 30, 15, bg); txt(label, X + w / 2, Y + 15, sz || 15, fg, 700, 'center'); return w; }
function hourX(h, X0, w) { return X0 + (h - 5) / 18 * w; }   // 5:00 .. 23:00
function dayBar(X0, Y, w, lt, opts) {
  box(X0, Y, w, 10, 5, '#e2e8f0');
  [[6, 'sun', 'Wakes'], [7, 'meal', 'Breakfast'], [12, 'meal', 'Lunch'], [18, 'meal', 'Dinner'], [22, 'moon', 'Bedtime']].forEach(function (e, i) {
    var a = pop(fadeIn(lt, (opts.t0 || 0) + i * 0.35, .4)); if (a <= 0) return;
    var px = hourX(e[0], X0, w); x.save(); x.translate(px, Y + 5); x.scale(a, a);
    x.fillStyle = '#fff'; x.strokeStyle = TEAL; x.lineWidth = 3; x.beginPath(); x.arc(0, 0, 20, 0, Math.PI * 2); x.fill(); x.stroke();
    x.strokeStyle = e[1] === 'sun' ? '#d97706' : e[1] === 'moon' ? NAVY : TEAL; x.fillStyle = x.strokeStyle; x.lineWidth = 2.5;
    if (e[1] === 'sun') { x.beginPath(); x.arc(0, 0, 6, 0, Math.PI * 2); x.fill(); for (var r = 0; r < 8; r++) { var an = r * Math.PI / 4; x.beginPath(); x.moveTo(Math.cos(an) * 9, Math.sin(an) * 9); x.lineTo(Math.cos(an) * 13, Math.sin(an) * 13); x.stroke(); } }
    else if (e[1] === 'moon') { x.beginPath(); x.arc(0, 0, 10, 0, Math.PI * 2); x.fill(); x.fillStyle = '#fff'; x.beginPath(); x.arc(5, -4, 9, 0, Math.PI * 2); x.fill(); }
    else { x.beginPath(); x.arc(0, 0, 11, 0, Math.PI * 2); x.stroke(); x.beginPath(); x.arc(0, 0, 5, 0, Math.PI * 2); x.stroke(); }
    x.restore(); if (a > .9) { var al = e[0] === 6 ? 'right' : e[0] === 7 ? 'left' : 'center', ox = e[0] === 6 ? 12 : e[0] === 7 ? -12 : 0;
      txt(e[2], px + ox, Y + 44, 14, '#475569', 700, al); txt((e[0] > 12 ? e[0] - 12 : e[0]) + ':00 ' + (e[0] >= 12 ? 'PM' : 'AM'), px + ox, Y + 62, 13, '#94a3b8', 600, al); }
  });
}
var scenes = [
  function title(lt, T) {
    var a = pop(fadeIn(lt, .2, .7)); x.save(); x.globalAlpha = Math.min(1, a); x.translate(0, (1 - a) * 30);
    box(R + 10, 66, 560, 58, 29, 'rgba(26,107,114,.12)'); txt('DOSIS  ·  THE DRUG INDEX APP', R + 40, 95, 18, TEAL, 800);
    txt('Med Scheduler', R + 30, 196, 76, NAVY, 800); txt('one clear daily timetable', R + 32, 262, 40, GOLD, 800); x.restore();
    // a messy prescription becomes a timetable
    var m = ease(fadeIn(lt, 2.0, .6)); x.save(); x.globalAlpha = m;
    box(R + 40, 330, 300, 260, 14, '#fff', '#cbd5e1', 2); txt('℞', R + 64, 362, 30, NAVY, 800);
    for (var i = 0; i < 6; i++) { x.strokeStyle = '#94a3b8'; x.lineWidth = 3; x.beginPath(); x.moveTo(R + 64, 400 + i * 30); for (var k = 0; k < 9; k++) x.lineTo(R + 64 + k * 26, 400 + i * 30 + Math.sin(k * 1.7 + i) * 5); x.stroke(); }
    x.restore();
    var arr = ease(fadeIn(lt, 3.4, .5)); if (arr > 0) { x.save(); x.globalAlpha = arr; x.fillStyle = GOLD; x.beginPath(); x.moveTo(R + 360, 450); x.lineTo(R + 410, 450); x.lineTo(R + 410, 432); x.lineTo(R + 440, 460); x.lineTo(R + 410, 488); x.lineTo(R + 410, 470); x.lineTo(R + 360, 470); x.fill(); x.restore(); }
    var tb = ease(fadeIn(lt, 4.0, .6)); x.save(); x.globalAlpha = tb;
    box(R + 460, 330, 400, 260, 14, '#fff', TEAL, 2); txt('Daily schedule', R + 484, 360, 20, NAVY, 800);
    [['7:00 AM', [TEAL, '#b91c1c']], ['12:30 PM', [TEAL]], ['6:30 PM', [TEAL, PURPLE]], ['10:00 PM', [GOLD]]].forEach(function (r, i) {
      var y = 404 + i * 46; txt(r[0], R + 484, y, 17, INK, 700); r[1].forEach(function (c, j) { pill(R + 640 + j * 56, y, c, .9); });
      x.strokeStyle = '#e2e8f0'; x.lineWidth = 1; x.beginPath(); x.moveTo(R + 480, y + 23); x.lineTo(R + 840, y + 23); x.stroke(); });
    x.restore();
  },
  function day(lt, T) {
    var a = ease(fadeIn(lt, .2, .5)); x.save(); x.globalAlpha = a;
    box(R + 10, 90, 850, 470, 18, '#fff', '#dfe6f0', 2); txt("1. The patient's day", R + 40, 130, 24, NAVY, 800); x.restore();
    dayBar(R + 70, 210, 730, lt, { t0: .6 });
    var h = ease(fadeIn(lt, 4.4, .5)); x.save(); x.globalAlpha = h;
    txt('Dialysis', R + 40, 330, 18, NAVY, 800);
    var w1 = chip(R + 130, 316, 'Hemodialysis', TEAL, '#fff'); var on = lt > 5.6;
    chip(R + 150 + w1, 316, 'Mon · Wed · Fri', on ? NAVY : '#e2e8f0', on ? '#fff' : '#475569'); chip(R + 310 + w1, 316, 'Tue · Thu · Sat', '#e2e8f0', '#475569');
    x.restore();
    var s = ease(fadeIn(lt, 6.4, .6)); if (s > 0) { x.save(); x.globalAlpha = s;
      var x1 = hourX(7, R + 70, 730), x2 = hourX(11, R + 70, 730);
      box(x1, 390, Math.max(250, x2 - x1) * s, 44, 10, 'rgba(31,56,100,.12)', NAVY, 2); txt('Session  7:00 – 11:00 AM', x1 + 14, 412, 16, NAVY, 800);
      txt('🩸', x1 - 22, 412, 22, NAVY, 400, 'center'); x.restore(); }
    var t = ease(fadeIn(lt, 7.4, .5)); if (t > 0) { x.save(); x.globalAlpha = t; box(R + 40, 470, 18, 18, 4, TEAL); txt('✓', R + 49, 479, 14, '#fff', 800, 'center');
      txt('Hold blood-pressure medicines until after dialysis', R + 68, 480, 16, INK, 600); x.restore(); }
  },
  function meds(lt, T) {
    // pasted prescription -> rows
    var a = ease(fadeIn(lt, .2, .5)); x.save(); x.globalAlpha = a;
    box(R + 10, 90, 380, 450, 16, '#fffdf5', '#e7d9a8', 2); txt('Paste a prescription', R + 34, 124, 20, NAVY, 800);
    var rx = ['Sevelamer  1 tab TID with meals', 'Levothyroxine  1 tab OD', 'Amlodipine  1 tab OD', 'Carvedilol  1 tab BID', 'Atorvastatin  1 tab HS', 'Calcium carbonate  1 tab TID'];
    rx.forEach(function (r, i) { var v = fadeIn(lt, .5 + i * .25, .3); if (v > 0) { x.save(); x.globalAlpha = v * a; txt(r, R + 34, 168 + i * 40, 16, '#334155', 600); x.restore(); } });
    var press = lt > 3.6 && lt < 3.9; box(R + 34, 470 + (press ? 2 : 0), 230, 44, 22, press ? DTEAL : TEAL); txt('Read the prescription', R + 149, 492 + (press ? 2 : 0), 17, '#fff', 700, 'center');
    x.restore();
    var names = [['Sevelamer', 'Three times daily', 'with food'], ['Levothyroxine', 'Once daily', 'empty stomach'], ['Amlodipine', 'Once daily', ''], ['Carvedilol', 'Twice daily', 'with food'], ['Atorvastatin', 'At bedtime', 'bedtime'], ['Calcium carbonate', 'Three times daily', '']];
    box(R + 420, 90, 440, 450, 16, '#fff', '#dfe6f0', 2); txt('2. Medicines', R + 444, 124, 20, NAVY, 800);
    txt('Medicine', R + 444, 160, 13, '#64748b', 700); txt('How often', R + 650, 160, 13, '#64748b', 700);
    names.forEach(function (n, i) {
      var u = ease(fadeIn(lt, 4.0 + i * .3, .45)); if (u <= 0) return;
      var y = 194 + i * 52, sx = R + 160 + (R + 444 - R - 160) * u, sy = 168 + i * 40 + (y - 168 - i * 40) * u;
      x.save(); x.globalAlpha = u; box(sx - 8, sy - 20, 420, 42, 8, '#f8fafc', '#e2e8f0', 1.5); txt(n[0], sx + 4, sy - 3, 16, INK, 700);
      if (n[2]) txt('· label: ' + n[2], sx + 4, sy + 13, 11.5, TEAL, 600); txt(n[1], sx + 206, sy, 15, '#334155', 600); x.restore();
    });
  },
  function rules(lt, T) {
    var cards = [['Label', 'Meal and time-of-day rules, from the drug label', TEAL, '🏷'], ['Spacing', 'Medicines that block each other are kept apart', AMBER, '↔'], ['Fewest times', 'Every rule met with the fewest dose times', NAVY, '⏱']];
    cards.forEach(function (c, i) { var a = pop(fadeIn(lt, .4 + i * 2.1, .5)); if (a <= 0) return;
      x.save(); x.globalAlpha = Math.min(1, a); var y = 84 + i * 96; x.translate(R + 10 + 20 * (1 - a), 0);
      box(0, y, 400, 82, 14, '#fff', c[2], 2.5); box(14, y + 17, 48, 48, 24, c[2]); txt(c[3], 38, y + 42, 22, '#fff', 800, 'center');
      txt(c[0], 76, y + 28, 19, c[2], 800); txt(c[1], 76, y + 56, 13.5, '#475569', 600); x.restore(); });
    // the timetable fills in
    box(R + 440, 84, 420, 466, 16, '#fff', '#dfe6f0', 2); txt('Daily schedule · CKD, not on dialysis', R + 464, 116, 18, NAVY, 800);
    var slots = [['6:00 AM', 'On waking'], ['7:00 AM', 'Breakfast'], ['12:30 PM', 'Lunch'], ['6:30 PM', 'Dinner'], ['10:00 PM', 'Bedtime']];
    slots.forEach(function (s, i) { var y = 160 + i * 76; txt(s[0], R + 464, y, 16, INK, 800); txt(s[1], R + 464, y + 20, 13, '#64748b', 600);
      x.strokeStyle = '#e2e8f0'; x.lineWidth = 1; x.beginPath(); x.moveTo(R + 460, y + 44); x.lineTo(R + 840, y + 44); x.stroke(); });
    var drops = [[0, 'Levothyroxine', '#b91c1c', 1.2], [1, 'Sevelamer', TEAL, 2.4], [1, 'Carvedilol', NAVY, 3.0], [2, 'Sevelamer', TEAL, 3.6], [3, 'Sevelamer', TEAL, 4.2], [3, 'Carvedilol', NAVY, 4.8], [4, 'Atorvastatin', GOLD, 5.4]];
    var cnt = {}; drops.forEach(function (d) { var k = cnt[d[0]] = (cnt[d[0]] || 0) + 1; var u = ease(fadeIn(lt, d[3], .5)); if (u <= 0) return;
      var tx = R + 590 + (k - 1) * 130, ty = 160 + d[0] * 76 + 6; x.save(); x.globalAlpha = u; var y = ty - (1 - u) * 60;
      pill(tx, y, d[2], .8); txt(d[1], tx + 22, y, 12.5, INK, 700); x.restore(); });
  },
  function hdDays(lt, T) {
    function table(X, title, hd) {
      box(X, 84, 410, 470, 16, '#fff', hd ? NAVY : '#dfe6f0', hd ? 3 : 2); txt(title, X + 22, 116, 19, NAVY, 800);
      var rows = hd ? [['7:00 AM', 'Breakfast'], ['9:00 AM', 'Mid-morning'], ['11:30 AM', 'After dialysis'], ['12:30 PM', 'Lunch']] : [['7:00 AM', 'Breakfast'], ['9:00 AM', 'Mid-morning'], ['', ''], ['12:30 PM', 'Lunch']];
      rows.forEach(function (r, i) { if (!r[0]) return; var y = 196 + i * 88; txt(r[0], X + 22, y, 16, INK, 800); txt(r[1], X + 22, y + 20, 13, '#64748b', 600);
        x.strokeStyle = '#e2e8f0'; x.lineWidth = 1; x.beginPath(); x.moveTo(X + 18, y + 46); x.lineTo(X + 392, y + 46); x.stroke(); });
      if (hd) { box(X + 150, 136, 240, 40, 10, 'rgba(31,56,100,.12)', NAVY, 2); txt('Dialysis 7:00 – 11:00 AM', X + 166, 156, 15, NAVY, 800); }
    }
    function med(X, row, name, col) { var y = 196 + row * 88; pill(X + 190, y, col, .8); txt(name, X + 212, y, 13.5, INK, 700); }
    var a = ease(fadeIn(lt, .2, .5)); x.save(); x.globalAlpha = a;
    table(R + 10, 'Non-dialysis day', false); med(R + 10, 1, 'Folic acid', GOLD); med(R + 10, 3, 'Amlodipine', '#b91c1c');
    var X = R + 450; table(X, 'Dialysis day', true);
    var u = ease(fadeIn(lt, 3.0, 1.4)); var row = 1 + u;
    var y = 196 + row * 88; pill(X + 190, y, GOLD, .8); txt('Folic acid', X + 212, y, 13.5, INK, 700);
    if (u > .95) { var c = pop(fadeIn(lt, 4.5, .4)); x.save(); x.globalAlpha = Math.min(1, c); chip(X + 190, y + 18, 'moved: due during the session', '#dcfce7', '#14532d', 12); x.restore(); }
    med(X, 3, 'Amlodipine', '#b91c1c');
    var b = pop(fadeIn(lt, 6.4, .4)); if (b > 0) { x.save(); x.globalAlpha = Math.min(1, b); chip(X + 190, 196 + 3 * 88 + 18, 'blood pressure: same time daily', '#eef2ff', NAVY, 12); chip(R + 200, 196 + 3 * 88 + 18, 'same time daily', '#eef2ff', NAVY, 12); x.restore(); }
    x.restore();
  },
  function why(lt, T) {
    var w = pop(fadeIn(lt, 6.4, .5)); if (w > 0) { x.save(); x.globalAlpha = Math.min(1, w);
      box(R + 10, 70, 850, 70, 14, '#fff7e6', '#f0c674', 2); txt('⚠  Spacing not met', R + 34, 92, 18, '#6b4200', 800);
      txt('Levothyroxine and sevelamer: give levothyroxine at least 4 hours apart.', R + 34, 120, 15.5, '#6b4200', 600); x.restore(); }
    box(R + 10, 160, 850, 400, 16, '#fff', '#dfe6f0', 2); txt('Why each medicine is where it is', R + 34, 194, 20, NAVY, 800);
    var items = [['Sevelamer', 'Take with food', 'Label', TEAL, 0.6], ['Calcium carbonate', 'Used as a calcium supplement; between meals', 'Evidence', PURPLE, 2.0], ['Amlodipine', 'Same time every day, after the dialysis session', 'Practice default', GOLD, 3.4], ['Atorvastatin', 'At bedtime, to limit stomach upset', 'Practice default', GOLD, 4.4]];
    items.forEach(function (it, i) { var a = ease(fadeIn(lt, it[4], .45)); if (a <= 0) return; var y = 240 + i * 78;
      x.save(); x.globalAlpha = a; x.translate((1 - a) * 30, 0); box(R + 34, y - 26, 802, 64, 10, '#f8fafc', '#e2e8f0', 1.5);
      txt(it[0], R + 52, y - 6, 17, INK, 800); txt(it[1], R + 52, y + 18, 14, '#475569', 600);
      x.font = '800 13px ' + F; var cw = x.measureText(it[2]).width + 22; box(R + 816 - cw, y - 12, cw, 26, 13, it[3]); txt(it[2], R + 816 - cw / 2, y + 1, 13, '#fff', 800, 'center'); x.restore(); });
  },
  function outputs(lt, T) {
    var cards = [
      function (X) { txt('Copy text', X + 20, 120, 20, NAVY, 800); box(X + 20, 140, 240, 250, 8, '#0f172a');
        ['OPTIMIZED MEDICATION', 'INTAKE SCHEDULE', '', '6:00 AM  Levothyroxine', '7:00 AM  Sevelamer,', '          Carvedilol', '12:30 PM Sevelamer', '6:30 PM  Sevelamer,', '          Carvedilol', '10:00 PM Atorvastatin'].forEach(function (l, i) { txt(l, X + 32, 162 + i * 22, 12, i < 2 ? '#fbbf24' : '#e2e8f0', i < 2 ? 800 : 600); });
        var c = lt > 2.4 && lt < 3.4; box(X + 20, 410, 240, 44, 22, c ? '#16a34a' : TEAL); txt(c ? '✓ Copied' : 'Copy text', X + 140, 432, 17, '#fff', 800, 'center'); },
      function (X) { txt('Patient sheet', X + 20, 120, 20, NAVY, 800); box(X + 20, 140, 240, 300, 6, '#fff', '#cbd5e1', 1.5);
        txt('My medicines', X + 36, 164, 15, INK, 800); for (var i = 0; i < 6; i++) { var y = 196 + i * 38; box(X + 36, y - 9, 18, 18, 3, '#fff', '#334155', 1.5);
          if (lt > 4.2 + i * .25) txt('✓', X + 45, y, 15, '#16a34a', 800, 'center'); x.fillStyle = '#cbd5e1'; x.fillRect(X + 64, y - 3, 150 - (i % 3) * 25, 6); }
        box(X + 20, 456, 240, 0, 0); },
      function (X) { txt('Pill count', X + 20, 120, 20, NAVY, 800); box(X + 20, 140, 240, 300, 12, '#f8fafc', '#e2e8f0', 1.5);
        var n = Math.round(Math.min(1, Math.max(0, (lt - 5.2) / 1.6)) * 210); txt(String(n), X + 140, 250, 64, TEAL, 800, 'center'); txt('pills for 30 days', X + 140, 300, 16, '#475569', 700, 'center');
        for (var k = 0; k < 7; k++) pill(X + 62 + (k % 4) * 52, 360 + Math.floor(k / 4) * 34, [TEAL, NAVY, GOLD, PURPLE][k % 4], .7); }
    ];
    cards.forEach(function (f, i) { var a = pop(fadeIn(lt, .3 + i * 1.6, .5)); if (a <= 0) return; x.save(); x.globalAlpha = Math.min(1, a);
      var X = R + 10 + i * 290; x.translate(0, (1 - a) * 30); box(X, 84, 280, 470, 16, '#fff', '#dfe6f0', 2); f(X); x.restore(); });
    txt('Illustration: a fictional sample', R + 440, 590, 14, '#94a3b8', 600, 'center');
  },
  function end(lt, T) {
    var a = pop(fadeIn(lt, .2, .6)); x.save(); x.globalAlpha = Math.min(1, a);
    box(R + 30, 110, 820, 150, 20, '#fff7e6', '#f0c674', 2.5); txt('Review the schedule', R + 60, 160, 40, '#6b4200', 800); txt('before you give it to a patient.', R + 60, 212, 30, '#6b4200', 700);
    x.restore();
    var b = ease(fadeIn(lt, 3.8, .6)); x.save(); x.globalAlpha = b;
    box(R + 30, 300, 820, 210, 20, '#fff', TEAL, 2.5);
    box(R + 60, 334, 64, 64, 16, '#0e4a50'); pill(R + 92, 366, '#fbbf24', 1.0);
    txt('Med Scheduler', R + 144, 352, 32, NAVY, 800); txt('in Dosis, the Drug Index', R + 144, 388, 22, TEAL, 700);
    txt('renalcarematters.com/drugs/med-scheduler', R + 60, 460, 22, INK, 700); x.restore();
  }
];
