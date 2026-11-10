/* kidney-workforce-planners.js — renalcarematters.com
 *
 * Deterministic arithmetic for three operational scenario planners that
 * accompany guides/nephrology-workforce-crisis-or-opportunity.html:
 *
 *   C01  capacityPlan()    Kidney care capacity and FTE gap planner
 *   C02  shiftCoverage()   Dialysis shift coverage planner
 *   C03  backlogPlan()     Referral backlog and e-consult scenario planner
 *
 * Formula version: 1.0 (2026-11-11), from calculator-specifications.md v1.0.
 * Status: operational arithmetic only. These are NOT validated clinical
 * prediction models. They do not estimate mortality, burnout, quality, safety,
 * regulatory compliance, or an individual patient's waiting time.
 *
 * Contract (do not change without review):
 *   - Pure functions, no DOM, no network, no storage. Node-testable via
 *     tests/kidney-workforce-planners.cjs.
 *   - Missing values are never coerced to zero: a required blank is an error.
 *   - Negative counts/hours and non-finite values are rejected.
 *   - Percent fields are 0–1 here; the UI converts from 0–100.
 *   - Full precision is kept; rounding happens only in the UI.
 *   - Undefined outputs are returned as null with a reason, never NaN/Infinity.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.KidneyWorkforcePlanners = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var VERSION = '1.0';
  var MAX_WEEKS_PER_YEAR = 52.18;

  /* ── Input helpers ─────────────────────────────────────────────────── */

  // Parse a raw value (string or number). Blank → null (missing). Never 0.
  function parseNum(v) {
    if (v === null || v === undefined) return null;
    if (typeof v === 'number') return v;
    var s = String(v).trim().replace(/,/g, '');
    if (s === '') return null;
    var n = Number(s);
    return n;
  }

  function isFiniteNum(n) { return typeof n === 'number' && isFinite(n); }

  // Validate one field. Returns the number, or pushes an error and returns undefined.
  // opts: {required, min, max, minExclusive, maxExclusive, integer, label}
  function field(raw, opts, errors, key) {
    var n = parseNum(raw);
    var label = opts.label || key;
    if (n === null) {
      if (opts.required) errors.push({ field: key, message: label + ' is required.' });
      return null;
    }
    if (!isFiniteNum(n)) { errors.push({ field: key, message: label + ' must be a number.' }); return undefined; }
    if (opts.integer && Math.floor(n) !== n) { errors.push({ field: key, message: label + ' must be a whole number.' }); return undefined; }
    if (opts.min !== undefined) {
      if (opts.minExclusive ? n <= opts.min : n < opts.min) {
        errors.push({ field: key, message: label + (opts.minExclusive ? ' must be greater than ' : ' cannot be less than ') + opts.min + '.' });
        return undefined;
      }
    }
    if (opts.max !== undefined) {
      if (opts.maxExclusive ? n >= opts.max : n > opts.max) {
        errors.push({ field: key, message: label + ' cannot be more than ' + opts.max + '.' });
        return undefined;
      }
    }
    return n;
  }

  // UI percent (0–100) → fraction (0–1). Blank stays null.
  function pctToFraction(v) {
    var n = parseNum(v);
    if (n === null) return null;
    if (!isFiniteNum(n)) return n;
    return n / 100;
  }

  /* ── C01  Kidney care capacity and FTE gap planner (one role) ─────────
   * input = {
   *   role: 'Nephrologist',
   *   activities: [{label, volume, minutes}],        // annual volume V, mean minutes M
   *   fixedRows:  [{label, hours}],                  // annual fixed hours F (nonoverlapping)
   *   paidFTE, hoursPerWeek, weeksPerYear, availableFraction,  // P, W, Y, A (A as 0–1)
   *   locumHours                                     // optional separate supply row, hours/year
   * }
   */
  function capacityPlan(input) {
    var errors = [], warnings = [];
    input = input || {};
    var acts = Array.isArray(input.activities) ? input.activities : [];
    var fixed = Array.isArray(input.fixedRows) ? input.fixedRows : [];

    var rows = [];
    var activityHours = 0;
    acts.forEach(function (a, i) {
      var blank = parseNum(a.volume) === null && parseNum(a.minutes) === null;
      if (blank && !(a.label && String(a.label).trim())) return; // fully empty row: ignore
      var V = field(a.volume, { required: true, min: 0, label: 'Activity ' + (i + 1) + ' annual volume' }, errors, 'activities.' + i + '.volume');
      var M = field(a.minutes, { required: true, min: 0, label: 'Activity ' + (i + 1) + ' minutes per activity' }, errors, 'activities.' + i + '.minutes');
      if (isFiniteNum(V) && isFiniteNum(M)) {
        var h = V * M / 60;
        activityHours += h;
        rows.push({ kind: 'activity', label: a.label || ('Activity ' + (i + 1)), hours: h });
      }
    });
    var fixedHours = 0;
    fixed.forEach(function (f, i) {
      if (parseNum(f.hours) === null && !(f.label && String(f.label).trim())) return;
      var F = field(f.hours, { required: true, min: 0, label: 'Fixed row ' + (i + 1) + ' hours' }, errors, 'fixedRows.' + i + '.hours');
      if (isFiniteNum(F)) { fixedHours += F; rows.push({ kind: 'fixed', label: f.label || ('Fixed ' + (i + 1)), hours: F }); }
    });
    if (rows.length === 0 && errors.length === 0) warnings.push('No activity or fixed-hour rows entered: modeled demand is zero.');

    var P = field(input.paidFTE, { required: true, min: 0, label: 'Filled paid FTE' }, errors, 'paidFTE');
    var W = field(input.hoursPerWeek, { required: true, min: 0, minExclusive: true, label: 'Paid hours per week' }, errors, 'hoursPerWeek');
    var Y = field(input.weeksPerYear, { required: true, min: 0, minExclusive: true, max: MAX_WEEKS_PER_YEAR, label: 'Working weeks per year' }, errors, 'weeksPerYear');
    var A = field(input.availableFraction, { required: true, min: 0, max: 1, label: 'Share of hours available for this work' }, errors, 'availableFraction');
    var L = field(input.locumHours, { required: false, min: 0, label: 'Locum hours per year' }, errors, 'locumHours');

    if (errors.length) return { ok: false, version: VERSION, errors: errors, warnings: warnings };

    var D = activityHours + fixedHours;
    var H = W * Y * A;                    // available hours per paid FTE
    var locum = isFiniteNum(L) ? L : 0;
    var S = P * H + locum;               // available capacity (hours)
    var fteDefined = H > 0;
    if (!fteDefined) warnings.push('Available share is 0%: hours are shown, but FTE conversion is not defined.');

    var signedGap = D - S;
    var shortfall = Math.max(0, signedGap);
    var out = {
      ok: true, version: VERSION, errors: [], warnings: warnings,
      role: input.role || '',
      demandHours: D, activityHours: activityHours, fixedHours: fixedHours,
      contributions: rows.map(function (r) { return { kind: r.kind, label: r.label, hours: r.hours, share: D > 0 ? r.hours / D : null }; }),
      hoursPerFTE: H,
      paidFTE: P, locumHours: locum,
      capacityHours: S,
      signedGapHours: signedGap,
      shortfallHours: shortfall,
      requirementFTE: fteDefined ? D / H : null,
      additionalFTE: fteDefined ? shortfall / H : null,
      additionalPeopleRoundedUp: fteDefined ? Math.ceil(shortfall / H - 1e-12) : null,
      utilizationPct: S > 0 ? D / S * 100 : null,
      status: null
    };
    if (D === 0 && S === 0) out.status = 'No modeled activity and no available capacity.';
    else if (S === 0) out.status = 'Utilization undefined: no available capacity.';
    else if (shortfall > 0) out.status = 'Modeled demand exceeds available capacity.';
    else out.status = 'Modeled demand is within available capacity.';
    if (locum > 0) warnings.push('Locum hours are counted as a separate supply row, not as filled posts.');
    return out;
  }

  /* ── C02  Dialysis shift coverage planner ──────────────────────────────
   * input = { nonOverlapping: true|false, blocks: [{
   *   label, hours, status:'open'|'closed', patients N, ratio R,
   *   charge C, scheduled K, unavailable U, minimum Qmin (optional),
   *   qualifiedAvailable (optional) }] }
   */
  function shiftCoverage(input) {
    input = input || {};
    var blocks = Array.isArray(input.blocks) ? input.blocks : [];
    var errors = [], warnings = [], results = [];
    blocks.forEach(function (b, i) {
      var tag = 'Block ' + (i + 1);
      var pre = 'blocks.' + i + '.';
      var status = b.status === 'closed' ? 'closed' : (b.status === 'open' ? 'open' : null);
      if (!status) { errors.push({ field: pre + 'status', message: tag + ': choose whether the unit is open or closed.' }); return; }
      var hours = field(b.hours, { required: true, min: 0, minExclusive: true, max: 24, label: tag + ' duration (hours)' }, errors, pre + 'hours');
      if (status === 'closed') {
        if (errors.length) return;
        results.push({ label: b.label || tag, status: 'closed', hours: hours, required: 0, available: null, gap: 0, covered: null, missingWorkerHours: 0, flags: ['Unit recorded as closed: no coverage requirement modeled.'] });
        return;
      }
      var N = field(b.patients, { required: true, min: 0, integer: true, label: tag + ' concurrent patients' }, errors, pre + 'patients');
      var R = field(b.ratio, { required: N !== 0, min: 0, minExclusive: true, label: tag + ' patients per direct-care worker' }, errors, pre + 'ratio');
      var C = field(b.charge, { required: true, min: 0, integer: true, label: tag + ' additional charge/supervisory workers' }, errors, pre + 'charge');
      var K = field(b.scheduled, { required: true, min: 0, integer: true, label: tag + ' scheduled workers' }, errors, pre + 'scheduled');
      var U = field(b.unavailable, { required: true, min: 0, integer: true, label: tag + ' workers unavailable' }, errors, pre + 'unavailable');
      var Qmin = field(b.minimum, { required: false, min: 0, integer: true, label: tag + ' minimum staffing' }, errors, pre + 'minimum');
      var Qa = field(b.qualifiedAvailable, { required: false, min: 0, integer: true, label: tag + ' qualified workers available' }, errors, pre + 'qualifiedAvailable');
      if (isFiniteNum(U) && isFiniteNum(K) && U > K) { errors.push({ field: pre + 'unavailable', message: tag + ': unavailable workers cannot exceed scheduled workers.' }); return; }
      if (!isFiniteNum(N) || !isFiniteNum(C) || !isFiniteNum(K) || !isFiniteNum(U) || !isFiniteNum(hours)) return;
      if (N > 0 && !isFiniteNum(R)) return;
      var direct = N === 0 ? 0 : Math.ceil(N / R - 1e-12);
      var Q = direct + C;
      var flags = [];
      if (isFiniteNum(Qmin) && Qmin > Q) { flags.push('Entered minimum staffing (' + Qmin + ') sets the requirement.'); Q = Qmin; }
      if (N === 0) flags.push('Open with no patients: only charge/minimum staffing applies.');
      var B = K - U;
      var gap = Math.max(0, Q - B);
      if (isFiniteNum(Qa)) {
        if (Qa > B) errors.push({ field: pre + 'qualifiedAvailable', message: tag + ': qualified workers cannot exceed available workers.' });
        else if (Qa < Q) flags.push('Skill mix: ' + Qa + ' qualified worker(s) available for ' + Q + ' required.');
      }
      results.push({ label: b.label || tag, status: 'open', hours: hours, patients: N, ratio: N === 0 ? R : R, directRequired: direct, charge: C,
        required: Q, available: B, gap: gap, covered: B >= Q, missingWorkerHours: gap * hours, flags: flags });
    });
    if (blocks.length === 0) errors.push({ field: 'blocks', message: 'Add at least one time block.' });
    if (errors.length) return { ok: false, version: VERSION, errors: errors, warnings: warnings };
    var peak = results.reduce(function (m, r) { return Math.max(m, r.gap); }, 0);
    var nonOverlap = input.nonOverlapping === true;
    var missing = nonOverlap ? results.reduce(function (s, r) { return s + r.missingWorkerHours; }, 0) : null;
    if (!nonOverlap) warnings.push('Blocks overlap or overlap is unconfirmed: total missing worker-hours is not summed.');
    return { ok: true, version: VERSION, errors: [], warnings: warnings, blocks: results, peakGap: peak,
      totalMissingWorkerHours: missing, uncoveredBlocks: results.filter(function (r) { return r.covered === false; }).length };
  }

  /* ── C03  Referral backlog and e-consult scenario planner ──────────────
   * input = { backlog B0, arrivalsPerWeek L, slotsPerWeek S, noncompletion P (0–1),
   *           alternativeFraction E (0–1 or null = not modeled),
   *           minutesPerAlternative T (optional), horizonWeeks (default 52) }
   */
  function backlogPlan(input) {
    input = input || {};
    var errors = [], warnings = [];
    var B0 = field(input.backlog, { required: true, min: 0, label: 'Current backlog' }, errors, 'backlog');
    var L = field(input.arrivalsPerWeek, { required: true, min: 0, label: 'New accepted referrals per week' }, errors, 'arrivalsPerWeek');
    var S = field(input.slotsPerWeek, { required: true, min: 0, label: 'New-patient slots per week' }, errors, 'slotsPerWeek');
    var P = field(input.noncompletion, { required: true, min: 0, max: 1, label: 'Share of slots not completed' }, errors, 'noncompletion');
    var E = field(input.alternativeFraction, { required: false, min: 0, max: 1, label: 'Share resolved by alternative pathway' }, errors, 'alternativeFraction');
    var T = field(input.minutesPerAlternative, { required: false, min: 0, label: 'Specialist minutes per alternative-pathway episode' }, errors, 'minutesPerAlternative');
    var horizon = field(input.horizonWeeks === undefined ? 52 : input.horizonWeeks, { required: true, min: 1, max: 104, integer: true, label: 'Horizon (weeks)' }, errors, 'horizonWeeks');
    if (errors.length) return { ok: false, version: VERSION, errors: errors, warnings: warnings };

    var eModeled = isFiniteNum(E);
    if (!eModeled) warnings.push('Alternative pathway not modeled (blank is not treated as a benefit).');
    var Eu = eModeled ? E : 0;
    var C = S * (1 - P);
    var A = L * (1 - Eu);
    var net = C - A;
    var series = [B0];
    var b = B0;
    for (var w = 1; w <= horizon; w++) { b = Math.max(0, b + A - C); series.push(b); }

    var clearance, clearanceNote;
    if (B0 === 0) { clearance = 0; clearanceNote = A > C ? 'No current backlog, but arrivals exceed completed capacity, so a queue will form.' : 'No current backlog.'; }
    else if (C > A) { clearance = Math.ceil(B0 / (C - A) - 1e-12); clearanceNote = 'Idealized clearance under constant weekly flows.'; }
    else { clearance = null; clearanceNote = 'Backlog will not clear under these assumptions.'; }

    var altHours = null;
    if (eModeled && isFiniteNum(T)) altHours = L * E * T / 60;
    else if (eModeled && E > 0) warnings.push('Enter specialist minutes per alternative-pathway episode to count its workload.');
    if (eModeled && E > 0) warnings.push('Alternative-pathway work must be funded; confirm slots are already net of this time.');

    return { ok: true, version: VERSION, errors: [], warnings: warnings,
      completedPerWeek: C, clinicArrivalsPerWeek: A, netChangePerWeek: A - C,
      clearanceWeeks: clearance, clearanceNote: clearanceNote,
      alternativeModeled: eModeled, alternativeSpecialistHoursPerWeek: altHours,
      series: series, horizonWeeks: horizon, finalBacklog: series[series.length - 1] };
  }

  /* ── Export helpers ────────────────────────────────────────────────── */

  // Escape a cell for CSV; neutralize formula-like user text (=, +, -, @, tab, CR).
  function csvCell(v) {
    if (v === null || v === undefined) return '';
    var s = String(v);
    if (/^[=+\-@\t\r]/.test(s) && !/^-?\d+(\.\d+)?$/.test(s)) s = "'" + s;
    if (/[",\n\r]/.test(s)) s = '"' + s.replace(/"/g, '""') + '"';
    return s;
  }
  function toCSV(rows) {
    return rows.map(function (r) { return r.map(csvCell).join(','); }).join('\r\n');
  }

  return {
    VERSION: VERSION,
    MAX_WEEKS_PER_YEAR: MAX_WEEKS_PER_YEAR,
    parseNum: parseNum,
    pctToFraction: pctToFraction,
    capacityPlan: capacityPlan,
    shiftCoverage: shiftCoverage,
    backlogPlan: backlogPlan,
    csvCell: csvCell,
    toCSV: toCSV
  };
});
