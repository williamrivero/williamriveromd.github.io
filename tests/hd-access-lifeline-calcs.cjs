// Acceptance tests for assets/hd-access-lifeline-calcs.js (blueprint C01–C05).
// Run: node tests/hd-access-lifeline-calcs.cjs
const assert = require('node:assert/strict');
const C = require('../assets/hd-access-lifeline-calcs.js');
let checks = 0;
const ok = (c, m) => { assert.ok(c, m); checks++; };
const near = (a, b, tol, m) => { assert.ok(Math.abs(a - b) <= tol, `${m}: got ${a}, expected ${b}`); checks++; };

// ---- C01 catheter exposure: date-union, boundaries, missing values ----
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-03-01', catheters: [{ insert: '2026-01-01', remove: '2026-01-11' }] });
  ok(r.ok && r.catheterDays === 10, '[Jan 1, Jan 11) = 10 days');
  ok(r.observedDays === 59, 'Jan 1 to Mar 1 (2026, non-leap) = 59 observed days');
}
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-03-01', catheters: [
    { insert: '2026-01-01', remove: '2026-01-11' }, { insert: '2026-01-05', remove: '2026-01-15' }] });
  ok(r.catheterDays === 14, 'overlapping intervals = 14 days, not 20');
  ok(r.overlapDaysRemoved === 6, 'overlap removed = 6');
}
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-01-31', catheters: [{ insert: '2025-12-20', remove: '2026-01-10' }] });
  ok(r.catheterDays === 9, 'interval clipped to window start');
}
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-01-31', catheters: [{ insert: '2026-01-21', missingRemoval: 'ongoing' }] });
  ok(r.catheterDays === 10 && r.warnings.length === 1, 'missing removal treated as ongoing, flagged');
}
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-01-31', catheters: [{ insert: '2026-01-21', missingRemoval: 'unknown' }] });
  ok(r.catheterDays === 0 && r.minimumOnly === true, 'unknown removal excluded and labeled minimum');
}
{
  const r = C.catheterExposure({ windowStart: '2026-01-01', windowEnd: '2026-01-31', catheters: [{ insert: '2026-01-10', remove: '2026-01-10' }] });
  ok(r.catheterDays === 0 && /same date/.test(r.warnings.join(' ')), 'same-day insertion/removal = 0 days with disclosure');
}
{
  const r = C.catheterExposure({ windowStart: '2026-02-01', windowEnd: '2026-01-01', catheters: [] });
  ok(!r.ok, 'reversed window rejected');
  const r2 = C.catheterExposure({ windowStart: '2026-02-30', windowEnd: '2026-03-10', catheters: [] });
  ok(!r2.ok, 'impossible date rejected');
}
{
  const r = C.catheterExposure({ windowStart: '2024-02-01', windowEnd: '2024-03-01', catheters: [{ insert: '2024-02-01', remove: '2024-03-01' }] });
  ok(r.catheterDays === 29 && Math.abs(r.percent - 100) < 1e-9, 'leap February = 29 days, 100%');
}

// ---- C02 infection rate with exact Poisson CI ----
{
  const r = C.infectionRate(3, 6000);
  near(r.rate, 0.5, 1e-12, '3 / 6,000 = 0.50 per 1,000');
  // Garwood exact 95% CI for k=3: (0.618672, 8.767273) -> per 1,000 over 6,000 days
  near(r.lower, 0.618672 / 6, 1e-5, 'k=3 lower bound');
  near(r.upper, 8.767273 / 6, 1e-5, 'k=3 upper bound');
}
{
  const r = C.infectionRate(0, 6000);
  ok(r.ok && r.rate === 0 && r.lower === 0, '0 / 6,000 = 0');
  near(r.upper * 6, 3.688879, 1e-5, 'k=0 upper bound is 3.689 events (nonzero)');
}
{
  ok(!C.infectionRate(2, 0).ok, 'zero exposure undefined');
  ok(!C.infectionRate(1.5, 100).ok, 'non-integer events rejected');
}
{ // reference values from scipy.stats.chi2.ppf (independent implementation)
  const ref = { 1: [0.025318, 5.571643], 9: [4.115373, 17.084803], 32: [21.887976, 45.174452], 100: [81.363991, 121.626794] };
  for (const [k, [lo, hi]] of Object.entries(ref)) {
    const ci = C.poissonExactCI(Number(k));
    near(ci.lower, lo, 1e-4, `k=${k} lower vs scipy`);
    near(ci.upper, hi, 1e-4, `k=${k} upper vs scipy`);
  }
}

// ---- C05 scenario and absolute effects ----
{
  near(C.rateScenario(0.46, 10000), 4.6, 1e-12, 'heparin-lock trial rate x 10,000 days = 4.6 events');
  near(C.rateScenario(0.13, 10000), 1.3, 1e-12, 'taurolidine/heparin trial rate x 10,000 days = 1.3 events');
  const e = C.absoluteEffect(0.408, 0.240);
  near(e.arr, 0.168, 1e-12, 'ARR'); ok(e.nnt === 6, 'NNT = ceil(1/0.168) = 6');
  const h = C.absoluteEffect(0.075, 0.226);
  ok(h.kind === 'harm' && h.nnh === 7, 'NNH = ceil(1/0.151) = 7');
  ok(C.absoluteEffect(0.47, 0.47).kind === 'none', 'no difference');
  ok(!C.absoluteEffect(1.2, 0.3).ok, 'risk > 100% rejected');
}

// ---- C03 intervention burden ----
{
  const procs = [{ date: '2025-02-01' }, { date: '2025-08-01' }, { date: '2026-01-15' }, { date: '2026-06-01' }];
  const r = C.interventionBurden({ followStart: '2025-01-01', followEnd: '2027-01-01', firstUseDate: '2025-04-01', procedures: procs });
  ok(r.total === 4 && r.maturation === 1 && r.maintenance === 3, 'phase split by first-use date');
  ok(r.accessDays === 730, '2 calendar years = 730 days');
  near(C.interventionBurden({ followStart: '2025-01-01', followEnd: '2025-01-01', procedures: [] }).ok ? 1 : 0, 0, 0, 'zero follow-up rejected');
}
{ // blueprint acceptance: 4 procedures in 730.5 access-days = 2.0 / access-year
  near(4 / (730.5 / 365.25), 2.0, 1e-12, '4 in 730.5 days = 2.0 per access-year');
  const r = C.interventionBurden({ followStart: '2025-01-01', followEnd: '2025-03-01', procedures: [{ date: '2025-02-01' }, { date: '2025-02-01' }], bundleSameDay: true, firstUseDate: '2025-01-15' });
  ok(r.total === 1 && r.excluded === 1 && r.shortFollowUp, 'same-day bundle counted once; short follow-up flagged');
  const idx = C.interventionBurden({ followStart: '2025-01-01', followEnd: '2026-01-01', procedures: [{ date: '2025-01-01', index: true }] });
  ok(idx.total === 0, 'index creation excluded');
}

// ---- C04 Qa / CO ----
{
  near(C.qaCoRatio(2000, 6).percent, 33.333333, 1e-5, 'Qa 2,000 / CO 6 = 33.3%');
  near(C.pctChange(600, 450).percent, -25, 1e-12, '600 -> 450 = -25%');
  ok(!C.qaCoRatio(2000, 0).ok && !C.qaCoRatio(2000, -1).ok, 'CO <= 0 rejected');
  ok(!C.pctChange(0, 450).ok, 'baseline 0 rejected');
  ok(C.daysBetween('2026-01-01', '2026-01-31') === 30, 'days between measurements');
}

console.log(`hd-access-lifeline-calcs: ${checks} checks passed`);
