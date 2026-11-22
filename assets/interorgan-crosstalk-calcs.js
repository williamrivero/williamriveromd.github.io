/* Interorgan crosstalk tools: shared pure logic (no DOM), used by
 * guides/calc-post-aki-followup.html, guides/calc-vexus-grading.html and
 * tests/interorgan-crosstalk-calcs.cjs.
 *
 * Post-AKI follow-up planner: KDIGO 2012 AKI guideline, recommendation 2.3.4
 *   (evaluate 3 months after AKI for resolution, new onset, or worsening of CKD; Not Graded).
 *   Planning aid only: no recovery label, no derived AKI stage, no risk estimate, no drug advice.
 * VExUS worksheet: original grading table (VExUS C), Beaubien-Souligny et al., Ultrasound J 2020.
 *   Documents a grade from operator-classified findings; no AKI probability, no diuretic advice.
 * Nothing here stores or transmits a value.
 */
(function (root) {
  'use strict';
  var UMOL_PER_MGDL = 88.4;
  function isNum(x) { return typeof x === 'number' && isFinite(x); }

  /* ── Calendar dates (date-only, no time zone): 'YYYY-MM-DD' ── */
  function daysInMonth(y, m) { return [31, (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0 ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]; }
  function parseDate(s) {
    if (typeof s !== 'string') return null;
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s.trim());
    if (!m) return null;
    var y = +m[1], mo = +m[2], d = +m[3];
    if (y < 1900 || y > 2200 || mo < 1 || mo > 12 || d < 1 || d > daysInMonth(y, mo)) return null;
    return { y: y, m: mo, d: d };
  }
  function fmt(o) { return o.y + '-' + (o.m < 10 ? '0' : '') + o.m + '-' + (o.d < 10 ? '0' : '') + o.d; }
  /* Days since a fixed civil epoch (proleptic Gregorian); pure integer arithmetic. */
  function ordinal(o) {
    var y = o.y, m = o.m;
    if (m <= 2) { y -= 1; m += 12; }
    return 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) + Math.floor((153 * (m - 3) + 2) / 5) + o.d;
  }
  function diffDays(a, b) { return ordinal(b) - ordinal(a); }   /* b − a */
  /* Add whole calendar months; a day that does not exist clamps to the last valid day. */
  function addMonths(s, n) {
    var o = parseDate(s); if (!o) return null;
    var idx = (o.y * 12 + (o.m - 1)) + n;
    var y = Math.floor(idx / 12), m = (idx % 12) + 1;
    return fmt({ y: y, m: m, d: Math.min(o.d, daysInMonth(y, m)) });
  }

  function toMgdl(value, unit) {
    if (!isNum(value)) return null;
    if (unit === 'mg/dL') return value;
    if (unit === 'umol/L') return value / UMOL_PER_MGDL;
    return null;
  }

  /* inp: { onset, discharge, assess : 'YYYY-MM-DD' | null,
           stage : '1'|'2'|'3'|'unknown',
           baseCr, baseUnit, baseDate, lastCr, lastUnit, lastDate,
           dialysis : bool, ckd : bool,
           concerns : { recovery, hf, lytes } }                                  */
  function postAki(inp) {
    var out = { errors: [], warnings: [], notes: [], checklist: [], flags: [] };
    var onset = inp.onset ? parseDate(inp.onset) : null;
    var disch = inp.discharge ? parseDate(inp.discharge) : null;
    var assess = inp.assess ? parseDate(inp.assess) : null;
    if (inp.onset && !onset) out.errors.push('AKI onset date is not a valid calendar date.');
    if (inp.discharge && !disch) out.errors.push('Discharge date is not a valid calendar date.');
    if (!inp.assess) out.errors.push('Assessment date is required.');
    else if (!assess) out.errors.push('Assessment date is not a valid calendar date.');
    if (!inp.onset && !inp.discharge) out.errors.push('Enter the AKI onset date, or the discharge date if onset is unknown.');
    if (onset && assess && diffDays(assess, onset) > 0) out.errors.push('AKI onset date is after the assessment date.');
    if (disch && assess && diffDays(assess, disch) > 0) out.errors.push('Discharge date is after the assessment date.');
    if (onset && disch && diffDays(onset, disch) < 0) out.errors.push('Discharge date is before the AKI onset date.');
    if (out.errors.length) return out;

    /* Milestone: guideline anchor = 3 calendar months after AKI onset.
       Onset unknown → separate discharge-based checkpoint, labeled as an operational fallback. */
    if (onset) { out.basis = 'onset'; out.milestone = addMonths(inp.onset, 3); }
    else { out.basis = 'discharge-fallback'; out.milestone = addMonths(inp.discharge, 3);
      out.notes.push('AKI onset is unknown. This date is an operational fallback counted from discharge, not the guideline anchor.'); }
    out.daysToMilestone = diffDays(assess, parseDate(out.milestone));
    out.status = out.daysToMilestone > 0 ? 'upcoming' : (out.daysToMilestone === 0 ? 'due-today' : 'reached');
    out.daysSinceEvent = diffDays(onset || disch, assess);

    /* Creatinine trend (optional): needs a credible positive baseline dated on or before the latest test. */
    out.trend = null;
    var hasBase = inp.baseCr !== null && inp.baseCr !== undefined && inp.baseCr !== '';
    var hasLast = inp.lastCr !== null && inp.lastCr !== undefined && inp.lastCr !== '';
    if (!hasBase) out.baselineKnown = false; else out.baselineKnown = true;
    if (hasBase || hasLast) {
      var b = hasBase ? toMgdl(inp.baseCr, inp.baseUnit) : null;
      var l = hasLast ? toMgdl(inp.lastCr, inp.lastUnit) : null;
      var bd = inp.baseDate ? parseDate(inp.baseDate) : null, ld = inp.lastDate ? parseDate(inp.lastDate) : null;
      if (hasBase && (b === null || b <= 0)) out.warnings.push('Baseline creatinine must be a positive number with a unit; no trend calculated.');
      else if (hasLast && (l === null || l <= 0)) out.warnings.push('Latest creatinine must be a positive number with a unit; no trend calculated.');
      else if (inp.baseDate && !bd) out.warnings.push('Baseline creatinine date is not a valid calendar date; no trend calculated.');
      else if (inp.lastDate && !ld) out.warnings.push('Latest creatinine date is not a valid calendar date; no trend calculated.');
      else if (!hasBase) out.notes.push('Baseline creatinine unknown: no change from baseline is calculated.');
      else if (!hasLast) out.notes.push('No latest creatinine entered: no change from baseline is calculated.');
      else if (bd && ld && diffDays(bd, ld) < 0) out.warnings.push('The latest creatinine is dated before the baseline; no trend calculated. Check the dates.');
      else if (ld && assess && diffDays(assess, ld) > 0) out.warnings.push('The latest creatinine is dated after the assessment date; no trend calculated.');
      else {
        out.trend = { baseMgdl: b, lastMgdl: l, absMgdl: l - b, absUmol: (l - b) * UMOL_PER_MGDL, pct: (l - b) / b * 100, datesKnown: !!(bd && ld) };
        if (!bd || !ld) out.notes.push('One or both creatinine dates are missing; confirm the baseline came before the latest test.');
        out.notes.push('A change from baseline describes two values. It does not show recovery, define a stage, or stand in for a steady-state kidney function assessment.');
      }
    } else out.notes.push('Baseline creatinine unknown: no change from baseline is calculated.');

    /* Dialysis at discharge overrides any routine-only checklist. */
    if (inp.dialysis) {
      out.pathway = 'dialysis-transition';
      out.flags.push('Dialysis at discharge: follow-up is clinician-directed and should not wait for the 3-month checkpoint. Use a dedicated dialysis-transition pathway where one exists.');
      out.checklist = [
        'Nephrology-directed schedule for dialysis sessions, access care and recovery surveillance (pre-dialysis creatinine trend, urine output).',
        'Medication reconciliation, including doses that depend on kidney function or dialysis timing.',
        'Blood pressure, volume status and target-weight review.',
        'Potassium, bicarbonate and other electrolytes as directed.',
        'When dialysis stops: creatinine and kidney function assessment and a spot urine albumin-to-creatinine ratio (uACR), then the 3-month reassessment below.'
      ];
    } else {
      out.pathway = 'routine';
      out.checklist = [
        'Serum creatinine and kidney function assessment (estimated GFR at steady state; consider cystatin C when creatinine is less reliable).',
        'Spot urine albumin-to-creatinine ratio (uACR).',
        'Blood pressure and volume status review.',
        'Medication reconciliation: what was stopped, what was restarted, and what still needs a decision.'
      ];
    }
    var c = inp.concerns || {};
    if (c.recovery) out.flags.push('Concern about incomplete recovery: schedule clinician-directed review earlier than the 3-month checkpoint.');
    if (c.hf) out.flags.push('Heart failure: coordinate earlier volume, blood pressure and medication review with the treating team.');
    if (c.lytes) out.flags.push('Unresolved electrolyte issue: repeat testing on the clinician\'s schedule, earlier than the 3-month checkpoint.');
    if (inp.ckd) out.notes.push('Known CKD: at reassessment the question is whether CKD has worsened, using established chronicity criteria (abnormality present for more than 3 months).');
    else out.notes.push('At reassessment, evaluate for resolution or new CKD using established chronicity criteria (abnormality present for more than 3 months).');
    if (inp.stage === 'unknown' || !inp.stage) out.notes.push('Maximum AKI stage not documented: this tool does not derive a stage.');
    out.notes.push('Follow-up earlier than 3 months is always allowed; the checkpoint is the latest routine reassessment, not the first permitted one.');
    return out;
  }

  /* ── VExUS worksheet ──
     inp: { ivc : number (cm) | null,
            hepatic : 'normal'|'mild'|'severe'|null,
            portal  : 'normal'|'mild'|'severe'|null,  (or portalPct : number → classified)
            renal   : 'normal'|'mild'|'severe'|null }                              */
  function portalClass(pct) {
    if (!isNum(pct) || pct < 0 || pct > 100) return null;
    return pct >= 50 ? 'severe' : (pct >= 30 ? 'mild' : 'normal');
  }
  function vexus(inp) {
    var out = { errors: [], trace: [], grade: null, complete: false, atLeast: null };
    var ivc = inp.ivc;
    if (ivc === null || ivc === undefined || ivc === '') { out.errors.push('Inferior vena cava (IVC) diameter is required; the grade cannot be assigned without it.'); return out; }
    if (!isNum(ivc) || ivc <= 0 || ivc > 6) { out.errors.push('IVC diameter must be a number in centimeters (for example 2.3).'); return out; }
    var portal = inp.portal || null;
    if (inp.portalPct !== null && inp.portalPct !== undefined && inp.portalPct !== '') {
      var pc = portalClass(inp.portalPct);
      if (pc === null) { out.errors.push('Portal pulsatility must be between 0 and 100%.'); return out; }
      portal = pc; out.trace.push('Portal pulsatility ' + inp.portalPct + '% → ' + pc + ' (under 30% normal, 30% to under 50% mild, 50% or more severe).');
    }
    var ok = { normal: 1, mild: 1, severe: 1 };
    var beds = { 'Hepatic vein': inp.hepatic || null, 'Portal vein': portal, 'Intrarenal vein': inp.renal || null };
    for (var k in beds) if (beds[k] !== null && !ok[beds[k]]) { out.errors.push(k + ' pattern is not recognized.'); return out; }
    if (ivc < 2) {
      out.grade = 0; out.complete = true;
      out.trace.unshift('IVC ' + ivc + ' cm is under 2 cm → grade 0; Doppler patterns do not change the grade.');
      return out;
    }
    out.trace.unshift('IVC ' + ivc + ' cm is 2 cm or more → grade depends on the three Doppler patterns.');
    var severe = 0, unknown = 0;
    for (var b in beds) {
      if (beds[b] === null) { unknown++; out.trace.push(b + ': not obtained.'); }
      else { if (beds[b] === 'severe') severe++; out.trace.push(b + ': ' + beds[b] + '.'); }
    }
    out.severe = severe; out.unknown = unknown;
    if (severe >= 2) { out.grade = 3; out.complete = true; out.trace.push('Two or more severely abnormal patterns → grade 3' + (unknown ? ' (a missing pattern cannot lower it).' : '.')); }
    else if (unknown === 0) { out.grade = severe === 1 ? 2 : 1; out.complete = true; out.trace.push(severe === 1 ? 'Exactly one severely abnormal pattern → grade 2.' : 'Normal or mildly abnormal patterns only → grade 1.'); }
    else { out.atLeast = severe === 1 ? 2 : 1; out.trace.push('Incomplete: ' + unknown + ' pattern(s) not obtained, so only a lower bound can be stated (at least grade ' + out.atLeast + ').'); }
    return out;
  }

  var api = { UMOL_PER_MGDL: UMOL_PER_MGDL, parseDate: parseDate, addMonths: addMonths, diffDays: function (a, b) { return diffDays(parseDate(a), parseDate(b)); }, toMgdl: toMgdl, postAki: postAki, portalClass: portalClass, vexus: vexus };
  root.CrosstalkCalcs = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
