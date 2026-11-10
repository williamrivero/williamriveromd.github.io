/* dysnatremia-kernels.js — pure, deterministic arithmetic for the RenalCareMatters
   dysnatremia guide and its calculators (calc-sodium-trajectory-tracker.html,
   calc-dysnatremia-toolkit.html).

   Rules this file enforces (from the dysnatremia blueprint, Nov 2026):
   - No DOM, no storage, no network. Inputs in, plain objects out.
   - Missing input = null, never zero. Invalid denominators throw a ValidationError.
   - Full internal precision; rounding happens only at display time in the UI.
   - Limit comparisons use unrounded values: equal = "at-limit", greater = "exceeded".
   - Present tonicity uses MEASURED sodium, never glucose-corrected sodium.
   - Observed changes are reported over their actual elapsed time; nothing is
     extrapolated into an "actual 24-hour correction".
   - Relowering never erases an earlier excursion: maxima are computed over every
     measured pair in the episode.
   Formula version: DYSNA-K 1.0 (2026-11-11). */
(function (root) {
  'use strict';
  var VERSION = 'DYSNA-K 1.0 (2026-11-11)';

  function ValidationError(msg) { this.name = 'ValidationError'; this.message = msg; }
  ValidationError.prototype = Object.create(Error.prototype);

  function isNum(x) { return typeof x === 'number' && isFinite(x); }
  function present(x) { return x !== null && x !== undefined && x !== '' && !(typeof x === 'number' && isNaN(x)); }
  function req(x, name, opts) {
    opts = opts || {};
    if (!present(x)) throw new ValidationError(name + ' is required.');
    var v = typeof x === 'string' ? Number(String(x).trim()) : x;
    if (!isNum(v)) throw new ValidationError(name + ' must be a finite number.');
    if (opts.positive && !(v > 0)) throw new ValidationError(name + ' must be greater than zero.');
    if (opts.nonneg && v < 0) throw new ValidationError(name + ' cannot be negative.');
    return v;
  }
  function opt(x, name, opts) { return present(x) ? req(x, name, opts) : null; }
  function result(values, assumptions, warnings, sourceIds) {
    return { values: values, assumptions: assumptions || [], warnings: warnings || [], sourceIds: sourceIds || [], formulaVersion: VERSION };
  }

  /* ── Unit conversions ─────────────────────────────────────────── */
  var GLUCOSE_MGDL_PER_MMOL = 18;      // approximate, as used in the plasma osmolality formula
  var BUN_MGDL_PER_UREA_MMOL = 2.8;    // BUN (mg/dL) / 2.8 = urea (mmol/L)
  var UREA_MW = 60.06;                 // g/mol
  function glucoseToMgdl(v, unit) { return unit === 'mmol' ? v * GLUCOSE_MGDL_PER_MMOL : v; }
  function glucoseToMmol(v, unit) { return unit === 'mmol' ? v : v / GLUCOSE_MGDL_PER_MMOL; }
  function ureaToMmol(v, unit) {
    if (unit === 'bun_mgdl') return v / BUN_MGDL_PER_UREA_MMOL;
    if (unit === 'urea_mmol') return v;
    throw new ValidationError('Urea unit must be BUN mg/dL or urea mmol/L.');
  }

  /* ── C02 Tonicity and glucose-corrected sodium ─────────────────── */
  function tonicity(inp) {
    var na = req(inp.na, 'Measured sodium', { positive: true });
    var gUnit = inp.glucoseUnit === 'mmol' ? 'mmol' : 'mgdl';
    var g = req(inp.glucose, 'Glucose', { nonneg: true });
    var gMmol = glucoseToMmol(g, gUnit), gMgdl = glucoseToMgdl(g, gUnit);
    var urea = opt(inp.urea, 'BUN/urea', { nonneg: true });
    var ureaMmol = urea === null ? null : ureaToMmol(urea, inp.ureaUnit || 'bun_mgdl');
    var mOsm = opt(inp.measuredOsm, 'Measured osmolality', { positive: true });
    var w = [], a = [];
    var effective = 2 * na + gMmol;
    var calculated = ureaMmol === null ? null : effective + ureaMmol;
    var gap = (calculated !== null && mOsm !== null) ? mOsm - calculated : null;
    if (ureaMmol === null) w.push('BUN/urea missing: total calculated osmolarity and osmolal gap are unavailable (missing is not zero). Effective tonicity is still shown.');
    var corr16 = null, corr24 = null;
    if (gMgdl > 100) {
      corr16 = na + 1.6 * (gMgdl - 100) / 100;
      corr24 = na + 2.4 * (gMgdl - 100) / 100;
    } else {
      a.push('Glucose is not above 100 mg/dL (about 5.6 mmol/L); the hyperglycemia sodium correction does not apply.');
    }
    a.push('Present tonicity uses measured sodium, not corrected sodium.');
    a.push('Calculated osmolarity (mOsm/L) is compared with measured osmolality (mOsm/kg) as a practical approximation; your laboratory equation may differ.');
    a.push('The 1.6 and 2.4 coefficients are two published correction factors; the spread is model uncertainty, not a confidence interval.');
    if (mOsm !== null && mOsm >= 275 && effective < 275) w.push('Measured osmolality is not low but effective tonicity is: ineffective osmoles (urea, ethanol) can hide true hypotonicity.');
    if (mOsm !== null && mOsm < 275 && gMgdl <= 100) a.push('Measured osmolality below 275 mOsm/kg commonly establishes hypotonicity (European guideline threshold), interpreted with glucose and ineffective osmoles.');
    return result({ effectiveOsmolarity: effective, calculatedOsmolarity: calculated, osmolalGap: gap,
      correctedNa16: corr16, correctedNa24: corr24, glucoseMmol: gMmol, glucoseMgdl: gMgdl, ureaMmol: ureaMmol }, a, w, ['hillier1999', 'adrogue2022', 'spasovski2014']);
  }

  /* ── C03 Hypernatremia water deficit and ongoing-loss planner ───── */
  function waterDeficit(inp) {
    var wt = req(inp.weightKg, 'Weight', { positive: true });
    var c = req(inp.coefficient, 'TBW coefficient', { positive: true });
    if (c > 1) throw new ValidationError('TBW coefficient must be a fraction of body weight (for example 0.5).');
    var na = req(inp.na, 'Current sodium', { positive: true });
    var tgt = req(inp.targetNa, 'Target sodium', { positive: true });
    if (!(tgt < na)) throw new ValidationError('Target sodium must be below current sodium for a water-deficit estimate.');
    var tbw = wt * c;
    var deficit = tbw * (na / tgt - 1);
    var sens = null;
    if (Array.isArray(inp.sensitivityCoefficients)) {
      sens = inp.sensitivityCoefficients.map(function (k) {
        var kk = req(k, 'Sensitivity coefficient', { positive: true });
        return { coefficient: kk, tbwL: wt * kk, deficitL: wt * kk * (na / tgt - 1) };
      });
    }
    return result({ tbwL: tbw, deficitL: deficit, sensitivity: sens },
      ['Deficit excludes ongoing and insensible losses; add them separately.',
       'The coefficient range is a sensitivity analysis of an assumption, not a statistical confidence interval.',
       'Deficit to an interim target differs from deficit to 140 mmol/L.'], [], ['yun2023']);
  }

  /* Planner: allocate part of the deficit to a horizon and add free-water losses.
     All entries are FREE WATER in liters over the same horizon. */
  function waterPlan(inp) {
    var d = req(inp.deficitL, 'Deficit', { nonneg: true });
    var frac = req(inp.fractionOfDeficit, 'Fraction of deficit for this horizon', { nonneg: true });
    if (frac > 1) throw new ValidationError('Fraction of deficit cannot exceed 1.');
    var renal = opt(inp.renalFreeWaterLossL, 'Renal electrolyte-free water loss', {});
    var extra = opt(inp.extrarenalFreeWaterLossL, 'Extrarenal free-water loss', { nonneg: true });
    var insens = opt(inp.insensibleLossL, 'Insensible loss', { nonneg: true });
    var planned = opt(inp.plannedFreeWaterL, 'Planned free water already given', { nonneg: true });
    var w = [];
    [['renal', renal], ['extrarenal', extra], ['insensible', insens]].forEach(function (p) {
      if (p[1] === null) w.push('No ' + p[0] + ' loss entered; it is excluded, not assumed to be zero.');
    });
    var total = d * frac + (renal || 0) + (extra || 0) + (insens || 0) - (planned || 0);
    return result({ allocatedDeficitL: d * frac, totalFreeWaterL: total }, [
      'Each entry must be free water, not total fluid volume.',
      'Renal loss should be the electrolyte-free water clearance, so urine is not counted twice.',
      'A liter of hypotonic saline is not a liter of free water (0.45% saline is about half free water).',
      'An arithmetic hourly equivalent is not an infusion-rate order; recalculate after each new sodium.'], w, ['yun2023', 'tomkins2026']);
  }

  /* ── C04 Electrolyte-free water clearance ───────────────────────── */
  function efwc(inp) {
    var p = req(inp.pna, 'Plasma sodium', { positive: true });
    var una = req(inp.una, 'Urine sodium', { nonneg: true });
    var uk = req(inp.uk, 'Urine potassium', { nonneg: true });
    var v = req(inp.urineVolume, 'Urine volume', { nonneg: true });
    var ratio = (una + uk) / p;
    var clr = v * (1 - ratio);
    var clues = [];
    if (ratio > 1) clues.push('Urine electrolyte ratio above 1');
    var uosm = opt(inp.uosm, 'Urine osmolality', { positive: true });
    if (uosm !== null && uosm > 500) clues.push('Urine osmolality above 500 mOsm/kg');
    if (inp.volumePerDay !== false && v < 1.5) clues.push('Urine volume below 1.5 L/day');
    return result({ ratio: ratio, clearance: clr, restrictionDifficultyClues: clues }, [
      'Positive clearance = kidneys excreting water in excess of sodium plus potassium; negative = the reverse. Negative values are kept.',
      'This is electrolyte-free water clearance, not osmolar free-water clearance.',
      'Describes the sampled renal component only; extrarenal losses and intake are not included.',
      'Clues are enrichment criteria used in EFFLUX-FLUID, not a validated response score.'], [], ['jaiyen2026', 'garrett2026']);
  }

  /* ── C05 Fluid scenario explorer ────────────────────────────────── */
  function fluidOneLiter(inp) {
    var tbw = req(inp.tbwL, 'Total body water', { positive: true });
    var na = req(inp.na, 'Current sodium', { positive: true });
    var fna = req(inp.infNa, 'Infusate sodium', { nonneg: true });
    var fk = opt(inp.infK, 'Infusate potassium', { nonneg: true });
    return result({ deltaPer1L: (fna + (fk || 0) - na) / (tbw + 1) },
      ['Adrogué–Madias estimate for 1 L in a closed system; do not multiply by large volumes.', 'Serial measured sodium supersedes every projection.'],
      fk === null ? ['Infusate potassium not entered; treated as none added.'] : [], ['adrogue2022']);
  }
  function fluidFinite(inp) {
    var tbw = req(inp.tbwL, 'Total body water', { positive: true });
    var na = req(inp.na, 'Current sodium', { positive: true });
    var V = req(inp.volumeL, 'Volume', { positive: true });
    var fna = req(inp.infNa, 'Infusate sodium', { nonneg: true });
    var fk = opt(inp.infK, 'Infusate potassium', { nonneg: true });
    var pred = (tbw * na + V * (fna + (fk || 0))) / (tbw + V);
    return result({ predictedNa: pred, delta: pred - na },
      ['Simplified closed-system mass balance; urine output, potassium shifts and compartments change the real course.',
       'Educational estimate only: it does not select or repeat a bolus.'], [], ['garrett2026']);
  }

  /* ── C06 Solute and urea explainer ──────────────────────────────── */
  function soluteUrineVolume(inp) {
    var osm = req(inp.osmolesPerDay, 'Daily osmole excretion', { nonneg: true });
    var u = req(inp.uosm, 'Urine osmolality', { positive: true });
    return result({ urineLPerDay: osm / u }, ['Uses the practical approximation 1 kg water ≈ 1 L.', 'Arithmetic does not promise a sodium response or set a dose.'], [], ['wendt2023']);
  }
  function ureaOsmoles(grams) {
    var g = req(grams, 'Urea', { nonneg: true });
    return result({ mOsm: g / UREA_MW * 1000 }, ['Potential osmoles if fully available for urinary excretion; absorption and metabolism vary.'], [], ['wendt2023']);
  }

  /* ── C01 Sodium trajectory and correction-limit tracker ─────────── */
  function parseTime(iso) {
    if (typeof iso !== 'string' || !/([zZ]|[+-]\d\d:?\d\d)$/.test(iso.trim())) {
      throw new ValidationError('Each collection time needs a timezone offset (for example 2026-11-11T08:00:00+08:00).');
    }
    var ms = Date.parse(iso.trim());
    if (!isFinite(ms)) throw new ValidationError('Unreadable collection time: ' + iso);
    return ms;
  }
  function chronicityPathway(onset) {
    if (onset === 'acute-documented') return 'acute-documented';
    return 'chronic-or-unknown-cautious-pathway';
  }
  function classify(change, ceiling, margin) {
    if (ceiling === null || ceiling === undefined) return 'no-ceiling';
    if (change > ceiling) return 'exceeded';
    if (change === ceiling) return 'at-limit';
    if (margin !== null && margin !== undefined && change >= ceiling - margin) return 'approaching';
    return 'below';
  }
  /* opts: { direction:'rise'|'fall' (hyponatremia rise / hypernatremia fall),
             ceilings:{h24:number|null,h48:number|null}, approachMargin:number,
             sparseGapH:number, nowISO:string, staleH:number, onset:'acute-documented'|'chronic'|'unknown' } */
  function trajectory(obs, opts) {
    opts = opts || {};
    var dir = opts.direction === 'fall' ? 'fall' : 'rise';
    var ceil = opts.ceilings || { h24: 8, h48: null };
    var margin = present(opts.approachMargin) ? opts.approachMargin : 2;
    var sparseGap = present(opts.sparseGapH) ? opts.sparseGapH : 6;
    if (!Array.isArray(obs) || obs.length === 0) throw new ValidationError('Enter at least one sodium value with its collection time.');
    var pts = obs.map(function (o, i) {
      return { idx: i, t: parseTime(o.t), iso: o.t, na: req(o.na, 'Sodium #' + (i + 1), { positive: true }), method: o.method || 'unknown' };
    });
    // conflicting duplicate timestamps
    var byT = {}, dupes = [];
    pts.forEach(function (p) {
      if (byT[p.t] !== undefined) {
        if (byT[p.t].na !== p.na) throw new ValidationError('conflict-requires-resolution: two different sodium values share the collection time ' + p.iso + '. Resolve which is correct; values are never averaged silently.');
        dupes.push(p.iso);
      } else byT[p.t] = p;
    });
    var s = Object.keys(byT).map(function (k) { return byT[k]; }).sort(function (a, b) { return a.t - b.t; });
    var H = 3600000, warnings = [], flags = [];
    if (dupes.length) warnings.push('Identical duplicate entries removed: ' + dupes.join(', '));
    var methods = {}; s.forEach(function (p) { methods[p.method] = 1; });
    if (Object.keys(methods).filter(function (m) { return m !== 'unknown'; }).length > 1) flags.push({ code: 'mixed-assay', text: 'Mixed measurement methods (for example blood gas and laboratory): differences can reflect assay, not physiology.' });
    var first = s[0], last = s[s.length - 1];
    var sign = dir === 'rise' ? 1 : -1;
    function windowMax(W) {
      var best = null;
      for (var i = 0; i < s.length; i++) for (var j = i + 1; j < s.length; j++) {
        var dt = (s[j].t - s[i].t) / H;
        if (dt > 0 && dt <= W + 1e-9) {
          var ch = sign * (s[j].na - s[i].na);
          if (best === null || ch > best.change) best = { change: ch, from: s[i].iso, to: s[j].iso, hours: dt };
        }
      }
      return best;
    }
    var m24 = windowMax(24), m48 = windowMax(48);
    var intervals = [];
    for (var k = 1; k < s.length; k++) {
      var dh = (s[k].t - s[k - 1].t) / H;
      intervals.push({ from: s[k - 1].iso, to: s[k].iso, hours: dh, change: s[k].na - s[k - 1].na, ratePerH: (s[k].na - s[k - 1].na) / dh });
      if (dh > sparseGap) flags.push({ code: 'sparse-window', text: 'Gap of ' + dh.toFixed(1) + ' h without a sodium between ' + s[k - 1].iso + ' and ' + s[k].iso + '; a peak may have been missed.' });
    }
    var spanH = (last.t - first.t) / H;
    var cov24 = spanH >= 24 ? 'complete' : 'incomplete';
    if (cov24 === 'incomplete' && s.length > 1) flags.push({ code: 'incomplete-window', text: 'Only ' + spanH.toFixed(1) + ' h observed; the 24-hour window is incomplete. Changes are reported over their actual elapsed time and are not extrapolated.' });
    var st24 = m24 ? classify(m24.change, ceil.h24, margin) : 'insufficient-data';
    var st48 = m48 ? classify(m48.change, ceil.h48, margin) : 'insufficient-data';
    if (st24 === 'exceeded' || st48 === 'exceeded') flags.push({ code: 'exceeded', text: 'An observed ' + dir + ' exceeded a selected ceiling. Stop or revise active therapy and obtain expert input now.' });
    else if (st24 === 'at-limit' || st48 === 'at-limit') flags.push({ code: 'at-limit', text: 'An observed ' + dir + ' reached the selected ceiling exactly. No further ' + dir + ' is allowed in that window.' });
    else if (st24 === 'approaching' || st48 === 'approaching') flags.push({ code: 'approaching', text: 'Within ' + margin + ' mmol/L of a selected ceiling (product rule, configurable).' });
    var lastInt = intervals.length ? intervals[intervals.length - 1] : null;
    if (lastInt && sign * lastInt.ratePerH >= 1) flags.push({ code: 'fast-interval', text: 'Latest interval changed ' + Math.abs(lastInt.ratePerH).toFixed(2) + ' mmol/L/h. This is not proof of a future 24-hour breach, but it needs an earlier recheck and a urine-output review.' });
    if (opts.nowISO && present(opts.staleH)) {
      var age = (parseTime(opts.nowISO) - last.t) / H;
      if (age > opts.staleH) flags.push({ code: 'stale', text: 'Latest sodium is ' + age.toFixed(1) + ' h old.' });
    }
    var pathway = chronicityPathway(opts.onset);
    if (pathway !== 'acute-documented') flags.push({ code: 'chronicity', text: 'Onset not documented within 48 h: the cautious chronic pathway applies.' });
    return result({
      n: s.length, first: { t: first.iso, na: first.na }, latest: { t: last.iso, na: last.na },
      baselineToCurrent: last.na - first.na, spanHours: spanH, coverage24: cov24,
      maxObserved24: m24, maxObserved48: m48, status24: st24, status48: st48,
      intervals: intervals, pathway: pathway, flags: flags, sorted: s.map(function (p) { return { t: p.iso, na: p.na, method: p.method }; })
    }, [
      'Maxima use every measured pair within the window, so a relowered sodium never erases an earlier excursion.',
      'A missing sample can hide a peak; no result here is labeled safe.',
      'Equality with a ceiling is "at limit"; only a larger change is "exceeded". Comparisons use unrounded values.',
      'Ceilings are the ones you selected from a named protocol; this tool does not choose them.'], warnings, ['sterns2024', 'spasovski2014']);
  }

  var api = { VERSION: VERSION, ValidationError: ValidationError, tonicity: tonicity, waterDeficit: waterDeficit, waterPlan: waterPlan,
    efwc: efwc, fluidOneLiter: fluidOneLiter, fluidFinite: fluidFinite, soluteUrineVolume: soluteUrineVolume,
    ureaOsmoles: ureaOsmoles, trajectory: trajectory, classify: classify, chronicityPathway: chronicityPathway,
    glucoseToMgdl: glucoseToMgdl, glucoseToMmol: glucoseToMmol, ureaToMmol: ureaToMmol };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.DysNa = api;
})(typeof window !== 'undefined' ? window : this);
