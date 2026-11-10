// Tests the MM-CORE arithmetic shipped inside guides/calc-mineral-metabolism-workbench.html.
// Run: node tests/mineral-metabolism-workbench.cjs   (golden fixtures from the handoff manifest + invalid-input paths)
const fs = require('fs'), path = require('path'), vm = require('vm');
const html = fs.readFileSync(path.join(__dirname, '..', 'guides', 'calc-mineral-metabolism-workbench.html'), 'utf8');
const start = html.indexOf('/* MM-CORE v'), end = html.indexOf("if (typeof module !== 'undefined') module.exports = MM;", start);
if (start < 0 || end < 0) { console.error('MM-CORE block not found'); process.exit(1); }
const ctx = {}; vm.createContext(ctx); vm.runInContext(html.slice(start, end) + '\nthis.MM = MM;', ctx);
const MM = ctx.MM;
let pass = 0, fail = 0;
function t(name, cond, info) { if (cond) { pass++; } else { fail++; console.log('FAIL', name, info !== undefined ? JSON.stringify(info) : ''); } }
const close = (a, b, tol = 1e-6) => Math.abs(a - b) <= tol;
const mg = { spUnit: 'mg/dL', upUnit: 'mg/dL', scrUnit: 'mg/dL', ucrUnit: 'mg/dL' };

// Golden fixtures (manifest)
let r = MM.phosphateHandling({ ...mg, sp: 2, up: 20, scr: 1, ucr: 100 });
t('F1 ok', r.ok, r);
t('F1 FE 10%', close(r.fePercent, 10), r.fePercent);
t('F1 TRP 0.90', close(r.trp, 0.9), r.trp);
t('F1 TmP/GFR 1.928571', close(r.tmpGfr, 1.928571428571429), r.tmpGfr);
t('F1 nonlinear branch', r.branch === 'nonlinear');
r = MM.phosphateHandling({ ...mg, sp: 2, up: 40, scr: 1, ucr: 100 });
t('F2 FE 20%', close(r.fePercent, 20)); t('F2 TRP 0.80', close(r.trp, 0.8)); t('F2 TmP 1.6', close(r.tmpGfr, 1.6), r.tmpGfr);
t('F2 linear branch', r.branch === 'linear');

// Branch boundary: TRP exactly 0.86 must use the ≤ (linear) branch. FE 14% → UP = 0.14 × SP × UCr / SCr
r = MM.phosphateHandling({ ...mg, sp: 2, up: 28, scr: 1, ucr: 100 });
t('Boundary TRP 0.86', close(r.trp, 0.86, 1e-12), r.trp);
t('Boundary uses linear branch', r.branch === 'linear', r.branch);
t('Boundary TmP = 0.86 × 2', close(r.tmpGfr, 1.72), r.tmpGfr);
// Just above the boundary uses the nonlinear branch (published discontinuity preserved)
r = MM.phosphateHandling({ ...mg, sp: 2, up: 27.99, scr: 1, ucr: 100 });
t('Above boundary nonlinear', r.branch === 'nonlinear' && r.trp > 0.86, r);
t('Discontinuity preserved (~1.654)', close(r.tmpGfr, 2 * 0.3 * r.trp / (1 - 0.8 * r.trp)), r.tmpGfr);

// Unit equivalence: SI inputs give the same FE/TRP/TmP
r = MM.phosphateHandling({ spUnit: 'mmol/L', upUnit: 'mmol/L', scrUnit: 'µmol/L', ucrUnit: 'µmol/L',
  sp: 2 * 0.3229, up: 20 * 0.3229, scr: 88.4, ucr: 8840 });
t('SI equivalence FE', close(r.fePercent, 10)); t('SI equivalence TmP mg/dL', close(r.tmpGfrMgdl, 1.928571428571429), r.tmpGfrMgdl);
t('SI TmP unit follows serum unit', r.tmpGfrUnit === 'mmol/L' && close(r.tmpGfr, 1.928571428571429 * 0.3229));
// Mixed creatinine units: serum mg/dL, urine mmol/L (100 mg/dL = 8.84 mmol/L)
r = MM.phosphateHandling({ spUnit: 'mg/dL', upUnit: 'mg/dL', scrUnit: 'mg/dL', ucrUnit: 'mmol/L', sp: 2, up: 20, scr: 1, ucr: 8.84 });
t('Mixed creatinine units', r.ok && close(r.fePercent, 10), r);
// Mixed phosphate units: serum mmol/L, urine mg/dL
r = MM.phosphateHandling({ spUnit: 'mmol/L', upUnit: 'mg/dL', scrUnit: 'mg/dL', ucrUnit: 'mg/dL', sp: 0.6458, up: 20, scr: 1, ucr: 100 });
t('Mixed phosphate units', r.ok && close(r.fePercent, 10), r);

// Invalid paths — each returns specific errors, never a number
const bad = (o, field) => { const x = MM.phosphateHandling({ ...mg, sp: 2, up: 20, scr: 1, ucr: 100, ...o }); return !x.ok && x.errors.some(e => e.field === field); };
t('blank SP', bad({ sp: '' }, 'sp')); t('NaN UP', bad({ up: NaN }, 'up')); t('Infinity SCr', bad({ scr: Infinity }, 'scr'));
t('zero SP', bad({ sp: 0 }, 'sp')); t('zero SCr', bad({ scr: 0 }, 'scr')); t('zero UCr', bad({ ucr: 0 }, 'ucr'));
t('negative UP', bad({ up: -1 }, 'up')); t('negative SP', bad({ sp: -2 }, 'sp'));
t('missing unit', bad({ spUnit: undefined }, 'spUnit')); t('unknown unit', bad({ ucrUnit: 'g/L' }, 'ucrUnit'));
t('TRP < 0 rejected', bad({ up: 250 }, 'up'));
r = MM.phosphateHandling({ ...mg, sp: 2, up: 0, scr: 1, ucr: 100 });
t('UP zero permitted with warning', r.ok && r.warnings.length === 1 && close(r.trp, 1));

// PTH ratio fixtures
let p = MM.pthRatio(540, 65); t('PTH 540/65', close(p.ratio, 8.307692307692308), p);
p = MM.pthRatio(540, 88); t('PTH 540/88', close(p.ratio, 6.136363636363637), p);
t('No ratio when ULN missing', !MM.pthRatio(540, NaN).ok); t('No ratio when ULN 0', !MM.pthRatio(540, 0).ok); t('No ratio ULN negative', !MM.pthRatio(540, -5).ok);
t('Band only for G5D', MM.pthBand(5, 'G3a-G5') === null && MM.pthBand(5, 'G5D') === 'within');
t('Band edges', MM.pthBand(2, 'G5D') === 'within' && MM.pthBand(9, 'G5D') === 'within' && MM.pthBand(9.0001, 'G5D') === 'above' && MM.pthBand(1.9999, 'G5D') === 'below');
t('Transplant gets no band', MM.pthBand(5, 'Tx') === null);

// Series: assay change creates a break; delta only within comparable assay
const s = MM.buildSeries([
  { t: 1, analyte: 'iPTH', value: 540, unit: 'pg/mL', method: 'Assay A', uln: 65 },
  { t: 2, analyte: 'iPTH', value: 600, unit: 'pg/mL', method: 'Assay A', uln: 65 },
  { t: 3, analyte: 'iPTH', value: 540, unit: 'pg/mL', method: 'Assay B', uln: 88 }]).iPTH;
t('Segment break on assay change', s[2].segment === 1 && s[1].segment === 0);
t('Delta within assay', s[1].delta === 60); t('No delta across assay', s[2].delta === null && !s[2].comparablePrior);
t('Same raw value, different standardized', close(s[0].ratio, 8.30769, 1e-5) && close(s[2].ratio, 6.13636, 1e-5));

// Ledger
let L = MM.calciumLedger([{ name: 'Calcium carbonate 500', mgPerUnit: 200, unitsPerDose: 2, dosesPerDay: 3 }]);
t('Ledger 200×2×3 = 1200', L.ok && L.totalMgPerDay === 1200 && L.unitsPerDay === 6, L);
L = MM.calciumLedger([{ name: 'X', mgPerUnit: 200, unitsPerDose: 1, dosesPerDay: 3 }, { name: ' x ', mgPerUnit: 200, unitsPerDose: 1, dosesPerDay: 1 }]);
t('Duplicate flagged', L.duplicates.length === 1);
t('Ledger rejects negative', !MM.calciumLedger([{ name: 'A', mgPerUnit: -1, unitsPerDose: 1, dosesPerDay: 1 }]).ok);
t('Ledger rejects NaN', !MM.calciumLedger([{ name: 'A', mgPerUnit: NaN, unitsPerDose: 1, dosesPerDay: 1 }]).ok);
t('Carbonate 1250 mg salt → ~500.7 mg elemental', close(MM.saltToElemental(1250, 'carbonate'), 500.549, 0.01), MM.saltToElemental(1250, 'carbonate'));
t('Acetate 667 mg salt → ~169 mg elemental', close(MM.saltToElemental(667, 'acetate'), 169.0, 0.1), MM.saltToElemental(667, 'acetate'));

// Converter
t('Phos 3.1 mg/dL → 1.001 mmol/L', close(MM.convert('phosphate', 3.1, 'mg/dL').value, 1.00099));
t('Total Ca 10 mg/dL → 2.495', close(MM.convert('totalCalcium', 10, 'mg/dL').value, 2.495));
t('Ionized Ca 1.2 mmol/L → 4.81 mg/dL', close(MM.convert('ionizedCalcium', 1.2, 'mmol/L').value, 4.8096));
t('No total↔ionized conversion', !MM.convert('totalCalcium', 10, 'mmol/L').ok === false && !MM.convert('calcium', 10, 'mg/dL').ok);
t('Unit mismatch rejected', !MM.convert('pth', 10, 'mg/dL').ok);

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
