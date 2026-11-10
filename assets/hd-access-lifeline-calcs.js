/* hd-access-lifeline-calcs.js — pure calculation functions for the
   "Lifeline That Lasts a Lifetime" hemodialysis vascular access tools.
   Used by guides/calc-catheter-exposure.html, calc-access-infection-rate.html,
   calc-access-intervention-burden.html and calc-access-flow-cardiac.html.
   Tested by tests/hd-access-lifeline-calcs.cjs (node tests/hd-access-lifeline-calcs.cjs).

   Conventions
   - Dates are ISO strings "YYYY-MM-DD", converted to whole UTC day numbers.
   - Intervals are start-inclusive / end-exclusive: [Jan 1, Jan 11) = 10 days.
   - Nothing here predicts an individual patient's risk. Rates are facility or
     cohort metrics; ratios are descriptive. No value is stored or transmitted.
*/
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.HDAccessCalc = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var DAY_MS = 86400000;

  function dayNum(iso) {
    if (typeof iso !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(iso)) return null;
    var p = iso.split('-').map(Number);
    var t = Date.UTC(p[0], p[1] - 1, p[2]);
    var d = new Date(t);
    if (d.getUTCFullYear() !== p[0] || d.getUTCMonth() !== p[1] - 1 || d.getUTCDate() !== p[2]) return null;
    return Math.round(t / DAY_MS);
  }
  function isoFromDay(n) { return new Date(n * DAY_MS).toISOString().slice(0, 10); }

  /* Union of half-open day intervals [s,e). Returns merged list and total days. */
  function unionDays(intervals) {
    var iv = intervals.filter(function (x) { return x && x[1] > x[0]; })
      .map(function (x) { return [x[0], x[1]]; })
      .sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
    var out = [];
    iv.forEach(function (x) {
      var last = out[out.length - 1];
      if (last && x[0] <= last[1]) last[1] = Math.max(last[1], x[1]);
      else out.push(x);
    });
    var total = out.reduce(function (s, x) { return s + (x[1] - x[0]); }, 0);
    return { merged: out, days: total };
  }

  /* C01 — catheter exposure.
     opts: { windowStart, windowEnd, catheters:[{insert, remove, missingRemoval:'ongoing'|'unknown'}],
             sustainedAvUseDate, accessCreatedDate }
     Returns catheter-present days (union clipped to window), observed days, percent,
     and warnings. Missing removal: 'ongoing' -> counted to windowEnd; 'unknown' -> excluded + warning. */
  function catheterExposure(opts) {
    var errors = [], warnings = [];
    var ws = dayNum(opts.windowStart), we = dayNum(opts.windowEnd);
    if (ws === null || we === null) { errors.push('Enter a valid observation window (start and end dates).'); }
    else if (we <= ws) { errors.push('The window end must be after the window start (end date is exclusive).'); }
    if (errors.length) return { ok: false, errors: errors };
    var clipped = [], unknownCount = 0;
    (opts.catheters || []).forEach(function (c, i) {
      var s = dayNum(c.insert);
      if (s === null) { if (c.insert) warnings.push('Catheter ' + (i + 1) + ': insertion date is not a valid date and was skipped.'); return; }
      var e;
      if (c.remove) {
        e = dayNum(c.remove);
        if (e === null) { warnings.push('Catheter ' + (i + 1) + ': removal date is not valid and was skipped.'); return; }
        if (e < s) { warnings.push('Catheter ' + (i + 1) + ': removal is before insertion and was skipped.'); return; }
        if (e === s) warnings.push('Catheter ' + (i + 1) + ': inserted and removed on the same date counts as 0 days under the end-exclusive rule.');
      } else if (c.missingRemoval === 'unknown') {
        unknownCount++; warnings.push('Catheter ' + (i + 1) + ': removal date unknown, so it was excluded. The exposure shown is a minimum.'); return;
      } else {
        e = we; warnings.push('Catheter ' + (i + 1) + ': no removal date, counted as still in place to the end of the window.');
      }
      var cs = Math.max(s, ws), ce = Math.min(e, we);
      if (ce > cs) clipped.push([cs, ce]);
    });
    var u = unionDays(clipped);
    var observed = we - ws;
    var out = {
      ok: true, errors: [], warnings: warnings,
      observedDays: observed,
      catheterDays: u.days,
      catheterFreeDays: observed - u.days,
      percent: observed > 0 ? (u.days / observed) * 100 : null,
      segments: u.merged.map(function (x) { return { start: isoFromDay(x[0]), end: isoFromDay(x[1]), days: x[1] - x[0] }; }),
      overlapDaysRemoved: clipped.reduce(function (s, x) { return s + (x[1] - x[0]); }, 0) - u.days,
      minimumOnly: unknownCount > 0,
      daysCreationToSustainedUse: null
    };
    var cr = dayNum(opts.accessCreatedDate || ''), su = dayNum(opts.sustainedAvUseDate || '');
    if (cr !== null && su !== null) {
      if (su >= cr) out.daysCreationToSustainedUse = su - cr;
      else warnings.push('Sustained AV-access use date is before the creation date; check the dates.');
    }
    return out;
  }

  /* Poisson helpers — exact (Garwood) two-sided interval via bisection on the Poisson CDF. */
  function logFact(n) { var s = 0; for (var i = 2; i <= n; i++) s += Math.log(i); return s; }
  function poissonCdf(k, mu) { // P(X <= k)
    if (k < 0) return 0;
    if (mu === 0) return 1;
    var lf = 0, sum = 0, logMu = Math.log(mu), maxLog = -Infinity, terms = [];
    for (var i = 0; i <= k; i++) {
      if (i > 0) lf += Math.log(i);
      var lt = i * logMu - mu - lf; terms.push(lt); if (lt > maxLog) maxLog = lt;
    }
    for (var j = 0; j < terms.length; j++) sum += Math.exp(terms[j] - maxLog);
    return Math.min(1, Math.exp(maxLog) * sum);
  }
  function bisect(f, lo, hi) { // f increasing in mu crossing 0
    for (var i = 0; i < 200; i++) { var m = (lo + hi) / 2; if (f(m) > 0) hi = m; else lo = m; if (hi - lo < 1e-12 * Math.max(1, hi)) break; }
    return (lo + hi) / 2;
  }
  function poissonExactCI(k, conf) {
    conf = conf || 0.95; var a = (1 - conf) / 2;
    if (!(k >= 0) || Math.floor(k) !== k) return null;
    var hiBound = Math.max(10, k * 4 + 50);
    var lower = k === 0 ? 0 : bisect(function (mu) { return (1 - poissonCdf(k - 1, mu)) - a; }, 0, hiBound);
    var upper = bisect(function (mu) { return a - poissonCdf(k, mu); }, 0, hiBound);
    return { lower: lower, upper: upper };
  }

  /* C02 — event rate per 1,000 exposure-days with exact 95% CI. */
  function infectionRate(events, exposureDays, per) {
    per = per || 1000;
    if (!(exposureDays > 0)) return { ok: false, error: 'Exposure days must be greater than zero; a rate with zero exposure is undefined.' };
    if (!(events >= 0) || Math.floor(events) !== Number(events)) return { ok: false, error: 'Events must be a whole number of zero or more.' };
    var ci = poissonExactCI(Number(events));
    return { ok: true, rate: events / exposureDays * per, lower: ci.lower / exposureDays * per, upper: ci.upper / exposureDays * per, per: per };
  }

  /* C05 — constant-rate planning scenario: expected events = rate x exposure / 1,000. */
  function rateScenario(ratePer1000, exposureDays) {
    if (!(ratePer1000 >= 0) || !(exposureDays > 0)) return null;
    return ratePer1000 * exposureDays / 1000;
  }

  /* C05 — binary risks over a shared horizon. ARR = control - treatment; NNT only if ARR > 0. */
  function absoluteEffect(controlRisk, treatRisk) {
    if (!(controlRisk >= 0 && controlRisk <= 1 && treatRisk >= 0 && treatRisk <= 1)) return { ok: false, error: 'Risks must be between 0 and 1 (0% to 100%).' };
    var arr = controlRisk - treatRisk;
    var res = { ok: true, arr: arr, rr: controlRisk > 0 ? treatRisk / controlRisk : null, rrr: controlRisk > 0 ? arr / controlRisk : null };
    if (Math.abs(arr) < 1e-12) { res.kind = 'none'; res.nnt = null; }
    else if (arr > 0) { res.kind = 'benefit'; res.nnt = Math.ceil(1 / arr - 1e-9); }
    else { res.kind = 'harm'; res.nnh = Math.ceil(1 / -arr - 1e-9); }
    return res;
  }

  /* C03 — intervention burden per access-year. */
  function interventionBurden(opts) {
    var errors = [], warnings = [];
    var start = dayNum(opts.followStart), end = dayNum(opts.followEnd);
    if (start === null || end === null) errors.push('Enter valid follow-up start and end dates.');
    else if (end <= start) errors.push('Follow-up end must be after the start.');
    if (errors.length) return { ok: false, errors: errors };
    var accessDays = end - start;
    var firstUse = dayNum(opts.firstUseDate || '');
    var mat = 0, maint = 0, excluded = 0, seen = {};
    (opts.procedures || []).forEach(function (p, i) {
      var d = dayNum(p.date);
      if (d === null) { if (p.date) warnings.push('Procedure ' + (i + 1) + ': invalid date skipped.'); return; }
      if (d < start || d >= end) { excluded++; return; }
      if (p.index) { excluded++; return; } // the creation surgery itself is not a burden event
      var key = d + '|' + (p.episode || i);
      if (opts.bundleSameDay && seen[d + '|day']) { excluded++; return; }
      seen[d + '|day'] = true; seen[key] = true;
      var phase = p.phase || (firstUse !== null && d >= firstUse ? 'maintenance' : 'maturation');
      if (phase === 'maturation') mat++; else maint++;
    });
    if (firstUse === null) warnings.push('No first-use date: procedures without a phase are counted as maturation procedures.');
    var years = accessDays / 365.25;
    return {
      ok: true, errors: [], warnings: warnings, accessDays: accessDays, accessYears: years,
      maturation: mat, maintenance: maint, total: mat + maint, excluded: excluded,
      ratePerYear: (mat + maint) / years,
      maintenanceRatePerYear: maint / years,
      shortFollowUp: accessDays < 180
    };
  }

  /* C04 — access flow / cardiac output worksheet. */
  function qaCoRatio(qaMlMin, coLMin) {
    if (!(qaMlMin > 0)) return { ok: false, error: 'Access flow (Qa) must be greater than zero mL/min.' };
    if (!(coLMin > 0)) return { ok: false, error: 'Cardiac output must be greater than zero L/min.' };
    return { ok: true, percent: (qaMlMin / 1000) / coLMin * 100 };
  }
  function pctChange(baseline, current) {
    if (!(baseline > 0)) return { ok: false, error: 'Baseline must be greater than zero.' };
    if (!(current >= 0)) return { ok: false, error: 'Current value must be zero or more.' };
    return { ok: true, percent: (current - baseline) / baseline * 100 };
  }
  function daysBetween(a, b) { var x = dayNum(a), y = dayNum(b); return (x === null || y === null) ? null : Math.abs(y - x); }

  return {
    dayNum: dayNum, isoFromDay: isoFromDay, unionDays: unionDays,
    catheterExposure: catheterExposure,
    poissonCdf: poissonCdf, poissonExactCI: poissonExactCI, infectionRate: infectionRate,
    rateScenario: rateScenario, absoluteEffect: absoluteEffect,
    interventionBurden: interventionBurden,
    qaCoRatio: qaCoRatio, pctChange: pctChange, daysBetween: daysBetween,
    logFact: logFact
  };
});
