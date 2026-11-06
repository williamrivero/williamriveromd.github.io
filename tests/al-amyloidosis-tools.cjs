/* tests/al-amyloidosis-tools.cjs — run: node tests/al-amyloidosis-tools.cjs
 * Behavior tests for assets/al-amyloidosis-tools.js (comparator + passport) and a
 * data-integrity check that the guide's clinician table matches the evidence JSON. */
'use strict';
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const T = require('../assets/al-amyloidosis-tools.js');

const TODAY = '2026-11-06';
let n = 0;
function test(name, fn) { fn(); n++; console.log('  ok  ' + name); }
const near = (a, b, eps = 1e-9) => Math.abs(a - b) < eps;

function prot(a, b, extra = {}) {
  const base = { measure: 'total-protein-24h', unit: 'g/24h', shownAs: 'exact', collectionComplete: 'yes' };
  return { earlier: Object.assign({}, base, a), later: Object.assign({}, base, b), ...extra };
}
function egfr(a, b) {
  const base = { equation: 'ckd-epi-2021-cr', shownAs: 'exact' };
  return { earlier: Object.assign({}, base, a), later: Object.assign({}, base, b) };
}
const CTX_OK = { adult: 'yes', onDialysis: 'no', acuteOrUnstable: 'no', sameProteinMethod: 'yes' };

console.log('Kidney Trend Comparator');

test('6 g/24h -> 3 g/24h: -3 g/24h and -50%, no response label', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '6' }, { date: '2026-07-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(r.ok);
  assert.ok(r.protein.computed);
  assert.ok(near(r.protein.change.abs, -3));
  assert.ok(near(r.protein.change.pct, -50));
  const txt = T.summaryText(r, 'en');
  assert.ok(/decreased by 3\.0 g\/24h \(50\.0%\)/.test(txt), txt);
  assert.ok(!/remission|respon(se|der) (met|achieved)|relapse|progression|recovery achieved|safe|failed/i.test(txt.replace(T.S.en.always, '').replace(T.S.en.discord, '')));
});

test('6,000 mg/24h -> 3 g/24h gives the same result after normalization', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '6,000', unit: 'mg/24h' }, { date: '2026-07-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(r.protein.computed);
  assert.ok(near(r.protein.change.abs, -3) && near(r.protein.change.pct, -50));
  assert.strictEqual(r.protein.unit, 'g/24h');
});

test('UACR -> UPCR: no comparison, explains different analytes', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '900', measure: 'uacr', unit: 'mg/g' }, { date: '2026-07-10', value: '1200', measure: 'upcr', unit: 'mg/g' }), context: CTX_OK }, TODAY);
  assert.ok(!r.protein.computed);
  assert.deepStrictEqual(r.protein.reasons, ['p-measure-diff']);
});

test('ratio mg/g -> mg/mmol: no comparison in version one', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '3000', measure: 'upcr', unit: 'mg/g' }, { date: '2026-07-10', value: '150', measure: 'upcr', unit: 'mg/mmol' }), context: CTX_OK }, TODAY);
  assert.ok(!r.protein.computed);
  assert.deepStrictEqual(r.protein.reasons, ['p-unit-diff']);
});

test('ratio units are never converted to g/day', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '3000', measure: 'upcr', unit: 'mg/g' }, { date: '2026-07-10', value: '1500', measure: 'upcr', unit: 'mg/g' }), context: CTX_OK }, TODAY);
  assert.ok(r.protein.computed);
  assert.strictEqual(r.protein.unit, 'mg/g');
  assert.ok(!/g\/24h|g\/day/.test(T.summaryText(r, 'en')));
});

test('incomplete or unknown 24-hour collection: no percentage comparison', () => {
  ['no', 'unknown'].forEach(c => {
    const r = T.compare({ protein: prot({ date: '2026-01-10', value: '6', collectionComplete: c }, { date: '2026-07-10', value: '3' }), context: CTX_OK }, TODAY);
    assert.ok(!r.protein.computed && r.protein.reasons.includes('p-collection'));
    assert.ok(!/%/.test(T.seriesLines(r.protein, 'en').filter(l => l.k === 'result').map(l => l.text).join('')));
  });
});

test('baseline zero: absolute difference shown, percentage undefined (no infinity)', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '0' }, { date: '2026-07-10', value: '0.4' }), context: CTX_OK }, TODAY);
  assert.ok(r.protein.computed);
  assert.ok(near(r.protein.change.abs, 0.4));
  assert.strictEqual(r.protein.change.pct, null);
  const txt = T.summaryText(r, 'en');
  assert.ok(/not defined/.test(txt) && !/Infinity|NaN/.test(txt));
});

test('later exact zero is allowed', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '2' }, { date: '2026-07-10', value: '0' }), context: CTX_OK }, TODAY);
  assert.ok(r.protein.computed && near(r.protein.change.pct, -100));
});

test('blank, <0.2, >90, negative, 2abc, 1e3, Infinity are never parsed as exact numbers', () => {
  assert.strictEqual(T.parseValue('').status, 'blank');
  assert.strictEqual(T.parseValue('<0.2').status, 'limit');
  assert.strictEqual(T.parseValue('>90').status, 'limit');
  assert.strictEqual(T.parseValue('-1').status, 'invalid');
  assert.strictEqual(T.parseValue('-1').reason, 'negative');
  ['2abc', '1e3', 'Infinity', 'NaN', '.5', '1.2.3', '6,00', '0x10', '3 g'].forEach(s => assert.strictEqual(T.parseValue(s).status, 'invalid', s));
  assert.strictEqual(T.parseValue(' 6,000.5 ').value, 6000.5);
});

test('a limit value suppresses arithmetic instead of stripping the sign', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '6' }, { date: '2026-07-10', value: '<0.2' }), context: CTX_OK }, TODAY);
  assert.ok(r.ok && !r.protein.computed && r.protein.reasons.includes('p-limit'));
  const r2 = T.compare({ protein: prot({ date: '2026-01-10', value: '6' }, { date: '2026-07-10', value: '0.2', shownAs: 'below' }), context: CTX_OK }, TODAY);
  assert.ok(!r2.protein.computed && r2.protein.reasons.includes('p-limit'));
});

test('invalid input blocks the run with field errors', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '2abc' }, { date: '2026-07-10', value: '-3' }), context: CTX_OK }, TODAY);
  assert.ok(!r.ok);
  assert.deepStrictEqual(r.errors.map(e => e.code).sort(), ['format', 'negative']);
});

test('eGFR 60 -> 48, stable adult, same equation: -12 and -20%, no diagnosis', () => {
  const r = T.compare({ egfr: egfr({ date: '2026-01-10', value: '60' }, { date: '2026-07-10', value: '48' }), context: CTX_OK }, TODAY);
  assert.ok(r.egfr.computed && near(r.egfr.change.abs, -12) && near(r.egfr.change.pct, -20));
  const txt = T.summaryText(r, 'en');
  assert.ok(/decreased by 12\.0 \(20\.0%\)/.test(txt), txt);
  assert.ok(!/CKD stage|AKI|progression|relapse/i.test(txt));
});

test('eGFR withheld for dialysis, child, unstable, unknown setting, or equation mismatch', () => {
  const pts = egfr({ date: '2026-01-10', value: '60' }, { date: '2026-07-10', value: '48' });
  const cases = [
    [{ ...CTX_OK, onDialysis: 'yes' }, 'e-dialysis'],
    [{ ...CTX_OK, onDialysis: 'unknown' }, 'e-dialysis-unknown'],
    [{ ...CTX_OK, adult: 'no' }, 'e-child'],
    [{ ...CTX_OK, adult: 'unknown' }, 'e-adult-unknown'],
    [{ ...CTX_OK, acuteOrUnstable: 'yes' }, 'e-unstable'],
    [{ ...CTX_OK, acuteOrUnstable: 'unknown' }, 'e-unstable-unknown']
  ];
  cases.forEach(([ctx, code]) => {
    const r = T.compare({ egfr: pts, context: ctx }, TODAY);
    assert.ok(!r.egfr.computed && r.egfr.reasons.includes(code), code);
  });
  const mis = T.compare({ egfr: egfr({ date: '2026-01-10', value: '60' }, { date: '2026-07-10', value: '48', equation: 'mdrd' }), context: CTX_OK }, TODAY);
  assert.ok(mis.egfr.reasons.includes('e-equation-diff'));
  const unk = T.compare({ egfr: egfr({ date: '2026-01-10', value: '60', equation: 'unknown' }, { date: '2026-07-10', value: '48' }), context: CTX_OK }, TODAY);
  assert.ok(unk.egfr.reasons.includes('e-equation-unknown'));
});

test('protein falls while eGFR falls: neutral discordance prompt, no recovery wording', () => {
  const r = T.compare({ protein: prot({ date: '2026-01-10', value: '6' }, { date: '2026-07-10', value: '3' }),
    egfr: egfr({ date: '2026-01-12', value: '60' }, { date: '2026-07-12', value: '48' }), context: CTX_OK }, TODAY);
  assert.ok(r.discordant);
  const txt = T.summaryText(r, 'en');
  assert.ok(txt.includes(T.S.en.discord) && txt.includes(T.S.en.always));
  assert.ok(!/kidney remission|treatment failed|\bsafe\b/i.test(txt));
});

test('reverse, impossible, and future dates are errors', () => {
  const rev = T.compare({ protein: prot({ date: '2026-07-10', value: '6' }, { date: '2026-01-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(!rev.ok && rev.errors.some(e => e.code === 'date-order'));
  const imp = T.compare({ protein: prot({ date: '2026-02-30', value: '6' }, { date: '2026-07-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(!imp.ok && imp.errors.some(e => e.code === 'date-invalid'));
  const fut = T.compare({ protein: prot({ date: '2026-01-10', value: '6' }, { date: '2027-01-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(!fut.ok && fut.errors.some(e => e.code === 'date-future'));
});

test('same-date inputs: values shown, labeled same-date, no trend arithmetic', () => {
  const r = T.compare({ protein: prot({ date: '2026-07-10', value: '6' }, { date: '2026-07-10', value: '3' }), context: CTX_OK }, TODAY);
  assert.ok(r.ok && r.protein.sameDate && !r.protein.computed);
  assert.ok(T.summaryText(r, 'en').includes(T.S.en.sameDate));
});

test('negative zero is normalized in display', () => {
  assert.strictEqual(T.fmt(-0), '0.00');
  assert.strictEqual(T.fmt(-0.001), '0.00');
  assert.strictEqual(T.fmtPct(-0.01), '0.0');
});

test('every language has every string key used by the comparator and passport', () => {
  const keys = o => Object.keys(o).sort();
  ['tl', 'ceb', 'kap'].forEach(l => {
    assert.deepStrictEqual(keys(T.S[l]), keys(T.S.en), l);
    ['R', 'E', 'measure', 'eq', 'rec', 'status', 'autoQ', 'Q'].forEach(g => assert.deepStrictEqual(keys(T.S[l][g]), keys(T.S.en[g]), l + '.' + g));
    assert.strictEqual(T.S[l].planLines.length, T.S.en.planLines.length);
  });
});

console.log('Shared Care Passport');

test('all records unknown: useful questions, no test orders', () => {
  const pp = T.buildPassport({ records: {}, questions: [] });
  assert.strictEqual(pp.gather.length, 6);
  assert.strictEqual(pp.autoQuestions.length, 6);
  const txt = T.passportText(pp, 'en');
  assert.ok(!/order|schedule a|you need a (biopsy|scan|test)/i.test(txt.replace(T.S.en.ppScope, '')));
  assert.ok(txt.includes(T.S.en.ppScope));
});

test('records available are listed as available; cardiac not requested adds a question, not a gather item', () => {
  const pp = T.buildPassport({ records: { typing: 'yes', hematology: 'yes', kidney: 'yes', cardiac: 'not-requested', meds: 'yes', plan: 'yes' }, questions: ['q2', 'q7'] });
  assert.strictEqual(pp.gather.length, 0);
  assert.deepStrictEqual(pp.autoQuestions, ['cardiac']);
  assert.deepStrictEqual(pp.questions, ['q2', 'q7']);
});

console.log('Evidence data integrity');

test('clinician table and chart source match the evidence JSON; no invented intervals', () => {
  const data = JSON.parse(fs.readFileSync(path.join(__dirname, '../assets/al-amyloidosis-evidence-data.json'), 'utf8'));
  const html = fs.readFileSync(path.join(__dirname, '../guides/al-amyloidosis-kidneys.html'), 'utf8');
  const rows = [...html.matchAll(/<tr data-score="(\d)" data-rrt="([\d.]+)">/g)].map(m => [+m[1], +m[2]]);
  assert.deepStrictEqual(rows, data.macrophage_scores.map(s => [s.score, s.rrt_cuminc_5y_pct]));
  assert.ok(html.includes('1.31') && html.includes('1.09') && html.includes('1.56'));
  assert.ok(html.includes('9.44') && html.includes('3.25') && html.includes('27.39'));
  assert.ok(html.includes(String(data.cohort_n)) && html.includes(String(data.sap_landmark.n)));
  assert.strictEqual(data.percent_ci, null);
});

console.log('\n' + n + ' tests passed');
