// Fixture tests for assets/interorgan-crosstalk-calcs.js (post-AKI follow-up planner, VExUS worksheet)
// and a regression check of the KDIGO 2026 iron criteria the guide links to (assets/ckd-anemia-2026.js).
// Run: node tests/interorgan-crosstalk-calcs.cjs
const assert = require('node:assert/strict');
const C = require('../assets/interorgan-crosstalk-calcs.js');
const A = require('../assets/ckd-anemia-2026.js');
let checks = 0;
const eq = (a, b, m) => { assert.deepEqual(a, b, m); checks++; };
const ok = (v, m) => { assert.ok(v, m); checks++; };
const near = (a, b, m) => { assert.ok(Math.abs(a - b) < 1e-9, (m || '') + ' got ' + a + ' expected ' + b); checks++; };

/* ── Month arithmetic: clamp to the last valid day; leap years ── */
eq(C.addMonths('2026-08-31', 3), '2026-11-30');
eq(C.addMonths('2026-09-10', 3), '2026-12-10');
eq(C.addMonths('2026-11-30', 3), '2027-02-28');
eq(C.addMonths('2027-11-30', 3), '2028-02-29');   // leap year
eq(C.addMonths('2028-02-29', 3), '2028-05-29');
eq(C.addMonths('2026-10-31', 3), '2027-01-31');   // year rollover
eq(C.addMonths('2026-12-31', 3), '2027-03-31');
eq(C.addMonths('2100-11-30', 3), '2101-02-28');   // 2100 is not a leap year
eq(C.parseDate('2026-02-30'), null);
eq(C.parseDate('2026-13-01'), null);
eq(C.parseDate('31/08/2026'), null);
eq(C.diffDays('2026-08-31', '2026-11-30'), 91);
eq(C.diffDays('2028-02-28', '2028-03-01'), 2);

/* ── Blueprint fixtures ── */
let r = C.postAki({ onset: '2026-08-31', discharge: '2026-09-10', assess: '2026-11-21', stage: '2' });
eq(r.errors, []); eq(r.milestone, '2026-11-30'); eq(r.basis, 'onset'); eq(r.status, 'upcoming'); eq(r.daysToMilestone, 9); eq(r.pathway, 'routine');
eq(r.checklist.length, 4);
r = C.postAki({ onset: null, discharge: '2026-09-10', assess: '2026-11-21', stage: 'unknown' });
eq(r.milestone, '2026-12-10'); eq(r.basis, 'discharge-fallback'); ok(r.notes.some(n => /operational fallback/.test(n)));
ok(r.notes.some(n => /does not derive a stage/.test(n)));
// Baseline 88.4 µmol/L and latest 1.5 mg/dL → +0.5 mg/dL and +50%
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-30', baseCr: 88.4, baseUnit: 'umol/L', baseDate: '2026-06-01', lastCr: 1.5, lastUnit: 'mg/dL', lastDate: '2026-11-28' });
near(r.trend.baseMgdl, 1); near(r.trend.absMgdl, 0.5); near(r.trend.pct, 50); near(r.trend.absUmol, 44.2); eq(r.status, 'due-today');
// Same values in mixed units the other way round
r = C.postAki({ onset: '2026-08-31', assess: '2026-12-05', baseCr: 1.0, baseUnit: 'mg/dL', baseDate: '2026-06-01', lastCr: 132.6, lastUnit: 'umol/L', lastDate: '2026-11-28' });
near(r.trend.absMgdl, 0.5); near(r.trend.pct, 50); eq(r.status, 'reached'); eq(r.daysToMilestone, -5);
// A latest test dated before the baseline must prevent a trend
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-30', baseCr: 1.0, baseUnit: 'mg/dL', baseDate: '2026-11-01', lastCr: 1.5, lastUnit: 'mg/dL', lastDate: '2026-10-01' });
eq(r.trend, null); ok(r.warnings.some(w => /dated before the baseline/.test(w)));
// Dialysis dependence must override any routine-only checklist
r = C.postAki({ onset: '2026-08-31', assess: '2026-10-01', dialysis: true });
eq(r.pathway, 'dialysis-transition'); ok(r.flags.some(f => /dialysis-transition pathway/.test(f))); ok(!r.checklist.some(c => /^Spot urine/.test(c)));
r = C.postAki({ onset: '2026-08-31', assess: '2026-10-01', dialysis: true, concerns: { recovery: true, hf: true, lytes: true } });
eq(r.flags.length, 4); eq(r.pathway, 'dialysis-transition');

/* ── Invalid and missing input ── */
ok(C.postAki({ assess: '2026-11-21' }).errors.length);                                     // no event date
ok(C.postAki({ onset: '2026-08-31' }).errors.some(e => /Assessment date is required/.test(e)));
ok(C.postAki({ onset: '2026-12-01', assess: '2026-11-21' }).errors.some(e => /after the assessment/.test(e))); // future event
ok(C.postAki({ onset: '2026-09-10', discharge: '2026-09-01', assess: '2026-11-21' }).errors.some(e => /before the AKI onset/.test(e)));
ok(C.postAki({ onset: '2026-02-30', assess: '2026-11-21' }).errors.length);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: 0, baseUnit: 'mg/dL', lastCr: 1.5, lastUnit: 'mg/dL' });   // zero creatinine
eq(r.trend, null); ok(r.warnings.length === 1);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: -1, baseUnit: 'mg/dL', lastCr: 1.5, lastUnit: 'mg/dL' });
eq(r.trend, null);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: NaN, baseUnit: 'mg/dL', lastCr: 1.5, lastUnit: 'mg/dL' });
eq(r.trend, null);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: 1, baseUnit: 'mmol', lastCr: 1.5, lastUnit: 'mg/dL' });      // unsupported unit
eq(r.trend, null);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', lastCr: 1.5, lastUnit: 'mg/dL' });                                  // unknown baseline shown explicitly
eq(r.trend, null); eq(r.baselineKnown, false); ok(r.notes.some(n => /Baseline creatinine unknown/.test(n)));
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: 1, baseUnit: 'mg/dL', lastCr: 1.5, lastUnit: 'mg/dL', lastDate: '2026-11-25' }); // latest after assessment
eq(r.trend, null);
r = C.postAki({ onset: '2026-08-31', assess: '2026-11-21', baseCr: 1, baseUnit: 'mg/dL', lastCr: 1.5, lastUnit: 'mg/dL' });      // dates missing → trend with caution note
near(r.trend.pct, 50); eq(r.trend.datesKnown, false);
// The planner never returns a recovery label, a derived stage, a risk figure or a drug instruction.
const dump = JSON.stringify(C.postAki({ onset: '2026-08-31', discharge: '2026-09-10', assess: '2026-11-21', stage: '3', ckd: true, baseCr: 1, baseUnit: 'mg/dL', lastCr: 1.2, lastUnit: 'mg/dL', concerns: { recovery: true } }));
ok(!/recovered|stage [123]\b|risk of|%|\bmg\b(?!\/dL)|start |stop /i.test(dump.replace(/does not show recovery|incomplete recovery|recovery surveillance/g, '')));

/* ── VExUS (original VExUS C table) ── */
eq(C.vexus({ ivc: 1.9, hepatic: 'severe', portal: 'severe', renal: 'severe' }).grade, 0);
eq(C.vexus({ ivc: 1.99 }).grade, 0);
let v = C.vexus({ ivc: 2.0, hepatic: 'normal', portal: 'normal', renal: 'normal' }); eq(v.grade, 1); eq(v.complete, true);   // IVC exactly 2.0 cm
eq(C.vexus({ ivc: 2.4, hepatic: 'mild', portal: 'mild', renal: 'mild' }).grade, 1);
eq(C.vexus({ ivc: 2.4, hepatic: 'severe', portal: 'mild', renal: 'normal' }).grade, 2);
eq(C.vexus({ ivc: 2.4, hepatic: 'normal', portal: 'severe', renal: 'mild' }).grade, 2);
eq(C.vexus({ ivc: 2.4, hepatic: 'normal', portal: 'normal', renal: 'severe' }).grade, 2);
eq(C.vexus({ ivc: 2.4, hepatic: 'severe', portal: 'severe', renal: 'normal' }).grade, 3);
eq(C.vexus({ ivc: 2.4, hepatic: 'severe', portal: 'severe', renal: 'severe' }).grade, 3);
// Incomplete data: a definitive grade only where the source rule already settles it
v = C.vexus({ ivc: 2.4, hepatic: 'severe', portal: 'severe', renal: null }); eq(v.grade, 3); eq(v.complete, true);
v = C.vexus({ ivc: 2.4, hepatic: 'severe', portal: null, renal: 'normal' }); eq(v.grade, null); eq(v.atLeast, 2); eq(v.complete, false);
v = C.vexus({ ivc: 2.4, hepatic: 'mild', portal: null, renal: null }); eq(v.grade, null); eq(v.atLeast, 1);
v = C.vexus({ ivc: 2.4 }); eq(v.grade, null); eq(v.atLeast, 1);
ok(C.vexus({ ivc: null }).errors.length); ok(C.vexus({ ivc: 0 }).errors.length); ok(C.vexus({ ivc: -2 }).errors.length); ok(C.vexus({ ivc: 23 }).errors.length); ok(C.vexus({ ivc: NaN }).errors.length);
ok(C.vexus({ ivc: 2.4, hepatic: 'weird' }).errors.length);
// Portal pulsatility cutoffs: at and immediately around 30% and 50%
eq(C.portalClass(29.9), 'normal'); eq(C.portalClass(30), 'mild'); eq(C.portalClass(49.9), 'mild'); eq(C.portalClass(50), 'severe'); eq(C.portalClass(0), 'normal'); eq(C.portalClass(100), 'severe');
eq(C.portalClass(-1), null); eq(C.portalClass(101), null);
eq(C.vexus({ ivc: 2.4, hepatic: 'normal', portalPct: 50, renal: 'normal' }).grade, 2);
eq(C.vexus({ ivc: 2.4, hepatic: 'normal', portalPct: 49.9, renal: 'normal' }).grade, 1);
ok(C.vexus({ ivc: 2.4, hepatic: 'normal', portalPct: 140, renal: 'normal' }).errors.length);

/* ── KDIGO 2026 iron criteria (existing shared module): blueprint fixtures ── */
const iron = (setting, ferritin, tsat, extra) => A.iron(Object.assign({ setting, ferritin, tsat }, extra || {}));
eq(iron('hd', 500, 30).eligible, true);          // HD 500/30 → meets
eq(iron('hd', 500, 30.1).eligible, false);       // HD 500/30.1 → does not meet
eq(iron('pd', 99, 39).eligible, true);           // PD 99/39 → meets
eq(iron('pd', 100, 25).eligible, false);         // PD 100/25 → does not meet
eq(iron('pd', 100, 24.9).eligible, true);        // PD 100/24.9 → meets
eq(iron('nd', 300, 24).eligible, false);         // Non-dialysis 300/24 → does not meet
eq(iron('nd', 150, 22).eligible, true);          // guide case 3: ferritin 150, TSAT 22%
eq(iron('hd', 700, 39.9, { ongoing: true }).action, 'REVIEW MAINTENANCE');   // on iron 700/39.9 → withholding threshold not met
eq(iron('hd', 700.1, 39.9, { ongoing: true }).action, 'WITHHOLD');
eq(iron('hd', 700, 40, { ongoing: true }).action, 'WITHHOLD');
for (const s of ['hd', 'pd', 'nd']) eq(iron(s, 150, 22, { infection: true }).action, 'PAUSE');   // infection → clinician review regardless of numbers
eq(iron('nd', 150, 101).action, 'INVALID'); eq(iron('nd', 150, -1).action, 'INVALID'); eq(iron('unknown', 150, 22).action, 'INVALID');

console.log(checks + ' checks passed: month clamping and leap dates, post-AKI fixtures, unit handling, invalid input, VExUS grading and cutoffs, KDIGO 2026 iron fixtures.');
