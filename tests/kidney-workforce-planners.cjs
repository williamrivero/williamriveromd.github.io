// Tests for assets/kidney-workforce-planners.js (C01–C03, formula v1.0).
// Run: node tests/kidney-workforce-planners.cjs
// Worked examples come from calculator-specifications.md v1.0 (2026-11-11) and are
// recomputed here by a second, independent method where practical.
const assert = require('node:assert/strict');
const K = require('../assets/kidney-workforce-planners.js');
let checks = 0;
const ok = (c, m) => { assert.ok(c, m); checks++; };
const eq = (a, b, m) => { assert.deepEqual(a, b, m); checks++; };
const near = (a, b, m, tol = 1e-9) => { assert.ok(Math.abs(a - b) <= tol, `${m}: ${a} vs ${b}`); checks++; };
const noBad = (obj, m) => { const s = JSON.stringify(obj); ok(!/NaN|Infinity/.test(s), m + ' has no NaN/Infinity'); };

/* ── C01 ─────────────────────────────────────────────────────────────── */
const c01 = (o = {}) => K.capacityPlan(Object.assign({
  role: 'Nephrologist',
  activities: [{ label: 'Clinic visits', volume: 5000, minutes: 30 }],
  fixedRows: [{ label: 'Minimum coverage', hours: 500 }],
  paidFTE: 2, hoursPerWeek: 40, weeksPerYear: 46, availableFraction: 0.75
}, o));

{ // spec worked example
  const r = c01();
  ok(r.ok, 'C01 example builds');
  near(r.demandHours, 3000, 'D');
  near(r.hoursPerFTE, 1380, 'H');
  near(r.capacityHours, 2760, 'S');
  near(r.shortfallHours, 240, 'shortfall');
  near(r.additionalFTE, 0.173913, 'additional FTE', 1e-6);
  near(r.requirementFTE, 2.173913, 'requirement FTE', 1e-6);
  eq(r.additionalFTE.toFixed(2), '0.17', 'display 0.17');
  eq(r.additionalPeopleRoundedUp, 1, 'whole people rounded up');
  // second method: hours → FTE via total requirement minus filled
  near(r.requirementFTE - 2, r.additionalFTE, 'two-method agreement');
  near(r.utilizationPct, 3000 / 2760 * 100, 'utilization');
  noBad(r, 'C01 example');
}
{ // missing values are not zero
  const r = c01({ paidFTE: '' });
  ok(!r.ok && r.errors.some(e => e.field === 'paidFTE'), 'blank paid FTE is an error, not 0');
  const r2 = c01({ activities: [{ label: 'x', volume: '', minutes: 30 }] });
  ok(!r2.ok, 'blank activity volume is an error');
}
{ // invalid inputs
  ok(!c01({ paidFTE: -1 }).ok, 'negative FTE rejected');
  ok(!c01({ hoursPerWeek: 0 }).ok, 'W must be > 0');
  ok(!c01({ weeksPerYear: 53 }).ok, 'Y ≤ 52.18');
  ok(!c01({ availableFraction: 1.2 }).ok, 'A ≤ 1');
  ok(!c01({ activities: [{ volume: 'abc', minutes: 3 }] }).ok, 'non-numeric rejected');
  ok(!c01({ activities: [{ volume: Infinity, minutes: 3 }] }).ok, 'infinite rejected');
}
{ // A = 0 → hours only, FTE suppressed
  const r = c01({ availableFraction: 0 });
  ok(r.ok, 'A=0 allowed');
  eq(r.requirementFTE, null, 'FTE suppressed');
  eq(r.utilizationPct, null, 'utilization undefined');
  ok(/no available capacity/.test(r.status), 'status says undefined');
  noBad(r, 'A=0');
}
{ // no staff
  const r = c01({ paidFTE: 0 });
  eq(r.capacityHours, 0, 'capacity 0');
  eq(r.utilizationPct, null, 'utilization null with zero capacity');
  near(r.additionalFTE, 3000 / 1380, 'all demand is shortfall');
}
{ // no activity, no capacity
  const r = c01({ activities: [], fixedRows: [], paidFTE: 0 });
  ok(r.ok, 'empty builds');
  ok(/No modeled activity/.test(r.status), 'D=0,S=0 message');
  noBad(r, 'empty');
}
{ // locum is separate supply
  const r = c01({ locumHours: 240 });
  near(r.shortfallHours, 0, 'locum closes gap');
  ok(r.warnings.some(w => /Locum/.test(w)), 'locum warning');
}
{ // monotonic: more demand cannot reduce shortfall
  let prev = -1;
  for (const v of [0, 1000, 3000, 5000, 9000]) {
    const r = c01({ activities: [{ volume: v, minutes: 30 }] });
    ok(r.shortfallHours >= prev, 'C01 monotonic in volume'); prev = r.shortfallHours;
  }
}
{ // contributions sum to demand
  const r = c01({ activities: [{ label: 'a', volume: 100, minutes: 60 }, { label: 'b', volume: 300, minutes: 20 }], fixedRows: [{ label: 'f', hours: 50 }] });
  near(r.contributions.reduce((s, c) => s + c.hours, 0), r.demandHours, 'contributions sum');
  near(r.demandHours, 100 + 100 + 50, 'D multi-row');
}

/* ── C02 ─────────────────────────────────────────────────────────────── */
const blk = (o = {}) => Object.assign({ label: 'AM', hours: 8, status: 'open', patients: 24, ratio: 4, charge: 1, scheduled: 7, unavailable: 1 }, o);
{
  const r = K.shiftCoverage({ nonOverlapping: true, blocks: [blk()] });
  ok(r.ok, 'C02 example builds');
  eq(r.blocks[0].required, 7, 'Q = ceil(24/4)+1 = 7');
  eq(r.blocks[0].available, 6, 'B = 7-1');
  eq(r.blocks[0].gap, 1, 'gap 1');
  eq(r.blocks[0].covered, false, 'not covered');
  eq(r.totalMissingWorkerHours, 8, '8 missing worker-hours');
  eq(r.peakGap, 1, 'peak gap');
  const r2 = K.shiftCoverage({ nonOverlapping: true, blocks: [blk({ patients: 25 })] });
  eq(r2.blocks[0].required, 8, 'ceil(25/4)+1 = 8');
  noBad(r, 'C02');
}
{ // validation
  ok(!K.shiftCoverage({ blocks: [blk({ unavailable: 8 })] }).ok, 'U > K rejected');
  ok(!K.shiftCoverage({ blocks: [blk({ patients: 2.5 })] }).ok, 'non-integer N rejected');
  ok(!K.shiftCoverage({ blocks: [blk({ ratio: 0 })] }).ok, 'R must be positive');
  ok(!K.shiftCoverage({ blocks: [blk({ status: '' })] }).ok, 'status required (no silent closure)');
  ok(!K.shiftCoverage({ blocks: [blk({ ratio: '' })] }).ok, 'blank R rejected when patients > 0');
  ok(!K.shiftCoverage({ blocks: [] }).ok, 'needs a block');
}
{ // empty open unit keeps charge + minimum
  const r = K.shiftCoverage({ nonOverlapping: true, blocks: [blk({ patients: 0, ratio: '', minimum: 2, scheduled: 1, unavailable: 0 })] });
  ok(r.ok, 'open empty builds');
  eq(r.blocks[0].required, 2, 'minimum applies');
  eq(r.blocks[0].gap, 1, 'gap vs minimum');
}
{ // closed block
  const r = K.shiftCoverage({ nonOverlapping: true, blocks: [blk({ status: 'closed' })] });
  eq(r.blocks[0].required, 0, 'closed → no requirement');
}
{ // overlapping blocks are not summed
  const r = K.shiftCoverage({ nonOverlapping: false, blocks: [blk(), blk({ label: 'PM' })] });
  eq(r.totalMissingWorkerHours, null, 'no sum for overlapping blocks');
}
{ // qualification flag
  const r = K.shiftCoverage({ nonOverlapping: true, blocks: [blk({ scheduled: 8, unavailable: 0, qualifiedAvailable: 5 })] });
  ok(r.blocks[0].covered && r.blocks[0].flags.some(f => /Skill mix/.test(f)), 'skill mismatch flagged separately from coverage');
}
{ // monotonic: extra patient cannot reduce required staff
  let prev = -1;
  for (let n = 0; n <= 30; n++) {
    const r = K.shiftCoverage({ nonOverlapping: true, blocks: [blk({ patients: n })] });
    ok(r.blocks[0].required >= prev, 'C02 monotonic'); prev = r.blocks[0].required;
  }
}

/* ── C03 ─────────────────────────────────────────────────────────────── */
const c03 = (o = {}) => K.backlogPlan(Object.assign({ backlog: 120, arrivalsPerWeek: 30, slotsPerWeek: 40, noncompletion: 0.10 }, o));
{
  const r = c03();
  ok(r.ok, 'C03 example builds');
  near(r.completedPerWeek, 36, 'C=36');
  near(r.clinicArrivalsPerWeek, 30, 'A=30');
  eq(r.clearanceWeeks, 20, 'clearance 20 weeks');
  ok(!r.alternativeModeled, 'blank E not modeled');
  // second method: simulate until zero
  let b = 120, w = 0; while (b > 0) { b = Math.max(0, b + 30 - 36); w++; }
  eq(w, r.clearanceWeeks, 'simulation agrees');
  eq(r.series[20], 0, 'series hits 0 at week 20');
  const r2 = c03({ alternativeFraction: 0.2, minutesPerAlternative: 15 });
  near(r2.clinicArrivalsPerWeek, 24, 'A=24 with E=0.2');
  eq(r2.clearanceWeeks, 10, 'clearance 10 weeks');
  near(r2.alternativeSpecialistHoursPerWeek, 1.5, '1.5 specialist h/week');
  noBad(r2, 'C03');
}
{
  const r = c03({ slotsPerWeek: 30 }); // C=27 < A=30
  eq(r.clearanceWeeks, null, 'will not clear');
  ok(/will not clear/.test(r.clearanceNote), 'message');
  ok(r.finalBacklog > 120, 'backlog grows');
  const z = c03({ backlog: 0 });
  eq(z.clearanceWeeks, 0, 'B0=0 → 0');
  ok(!c03({ noncompletion: 1.5 }).ok, 'P ≤ 1');
  ok(!c03({ backlog: -5 }).ok, 'negative backlog rejected');
  ok(!c03({ arrivalsPerWeek: '' }).ok, 'blank L is an error');
  const s0 = c03({ slotsPerWeek: 0 });
  ok(s0.ok && s0.clearanceWeeks === null, 'zero slots handled');
  noBad(s0, 'zero slots');
}
{ // monotonic: more completed capacity cannot worsen the backlog
  let prev = Infinity;
  for (const s of [20, 30, 36, 40, 60]) {
    const r = c03({ slotsPerWeek: s });
    ok(r.finalBacklog <= prev, 'C03 monotonic'); prev = r.finalBacklog;
  }
}

/* ── helpers ─────────────────────────────────────────────────────────── */
eq(K.pctToFraction('75'), 0.75, 'percent conversion');
eq(K.pctToFraction(''), null, 'blank percent stays null');
eq(K.parseNum(''), null, 'blank → null');
eq(K.csvCell('=SUM(A1)'), "'=SUM(A1)", 'formula neutralized');
eq(K.csvCell('-5'), '-5', 'negative number kept');
eq(K.csvCell('a,b'), '"a,b"', 'comma quoted');
eq(K.toCSV([['x', 1], ['@cmd', 'y']]), "x,1\r\n'@cmd,y", 'CSV rows');

console.log(`kidney-workforce-planners: ${checks} checks passed`);
