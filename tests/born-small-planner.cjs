// Tests for assets/born-small-planner.js and the Born Small study table.
// Run: node tests/born-small-planner.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const P = require('../assets/born-small-planner.js');
let checks = 0;
const ok = (c, m) => { assert.ok(c, m); checks++; };
const eq = (a, b, m) => { assert.deepEqual(a, b, m); checks++; };

const base = (over = {}) => Object.assign({
  audienceAge: 'adult',
  birthWeight: { value: '', unit: 'g', ounces: '' },
  gestation: { weeks: '', days: '' },
  documentedSGA: 'unknown', documentedFGR: 'unknown', nicuCare: 'unknown', neonatalAKI: 'unknown',
  neonatalDialysis: 'unknown', congenitalKidneyUrinaryCondition: 'unknown', majorCongenitalHeartCondition: 'unknown',
  clinicianIdentifiedCurrentConcern: 'unknown', sourceConfidence: 'mixed-uncertain', confirmedUnusual: false
}, over);
const rules = (o) => P.buildPrompts(base(o));
const FORBIDDEN = /(low|medium|high)[ -]risk|your risk is|\bnormal\b|risk score|\d+(\.\d+)?\s*%/i;

// 1. All unknown: useful questions, unknowns preserved, no reassurance or risk language
{
  const s = P.buildSummary(base(), 'en');
  ok(s.ok, 'all-unknown summary builds');
  eq(s.ruleIds, ['base', 'record']);
  eq(s.questions.length, 5);
  ok(s.entered.filter(e => e.value === 'Unknown').length >= 10, 'unknowns preserved');
  const text = P.toPlainText(s);
  ok(!FORBIDDEN.test(text.replace(s.scope, '')), 'no risk or reassurance language');
  ok(text.includes(s.scope), 'scope line present');
}

// 2. Audience is the only required field
{
  const v = P.validate(base({ audienceAge: '' }));
  ok(!v.ok && v.errors[0].code === 'audience-required', 'audience required');
}

// 3. LBW boundary: 2.5 kg is not below; 2.499 kg is (unrounded comparison)
{
  const a = P.normalizeWeight({ value: '2.5', unit: 'kg' });
  eq([a.grams, a.belowLBW], [2500, false]);
  const b = P.normalizeWeight({ value: '2.499', unit: 'kg' });
  ok(b.belowLBW && Math.abs(b.grams - 2499) < 1e-9, '2.499 kg below LBW');
  ok(!rules({ birthWeight: { value: '2.5', unit: 'kg' } }).includes('weight'), 'Q-weight absent at 2500');
  ok(rules({ birthWeight: { value: '2499.9', unit: 'g' } }).includes('weight'), 'Q-weight at 2499.9 g');
}

// 4. VLBW boundary
{
  ok(!rules({ birthWeight: { value: '1500', unit: 'g' } }).includes('vlbw'), 'no Q-vlbw at 1500');
  ok(rules({ birthWeight: { value: '1499', unit: 'g' } }).includes('vlbw'), 'Q-vlbw at 1499');
  ok(rules({ birthWeight: { value: '1.4999', unit: 'kg' } }).includes('vlbw'), 'Q-vlbw unrounded kg');
}

// 5. Preterm boundary
{
  ok(rules({ gestation: { weeks: '36', days: '6' } }).includes('gestation'), '36w6d preterm');
  ok(!rules({ gestation: { weeks: '37', days: '0' } }).includes('gestation'), '37w0d not preterm');
}

// 6. Preterm + documented growth problem; blank days preserved
{
  const r = rules({ gestation: { weeks: '33', days: '' }, documentedSGA: 'yes' });
  ok(r.includes('pretermGrowth') && r.includes('growth'), 'Q-preterm-growth at 33 w');
  const g = P.normalizeGestation({ weeks: '33', days: '' });
  eq([g.days, g.totalDays], [null, null]);
  const r2 = rules({ gestation: { weeks: '34', days: '0' }, documentedFGR: 'yes' });
  ok(!r2.includes('pretermGrowth') && r2.includes('growth'), 'no Q-preterm-growth at 34 w');
  const s = P.buildSummary(base({ gestation: { weeks: '33', days: '' } }), 'en');
  ok(s.entered[2].value.includes('extra days not given'), 'day uncertainty shown');
}

// 7. Invalid entries produce errors and no summary
{
  for (const [over, code] of [
    [{ gestation: { weeks: '33', days: '7' } }, 'days-range'],
    [{ gestation: { weeks: '33.5', days: '' } }, 'weeks-integer'],
    [{ gestation: { weeks: '', days: '3' } }, 'weeks-needed'],
    [{ birthWeight: { value: '0', unit: 'g' } }, 'nonpositive'],
    [{ birthWeight: { value: '-1', unit: 'g' } }, 'format'],
    [{ birthWeight: { value: '2abc', unit: 'kg' } }, 'format'],
    [{ birthWeight: { value: '2,5', unit: 'kg' } }, 'format'],
    [{ birthWeight: { value: 'Infinity', unit: 'g' } }, 'format']
  ]) {
    const v = P.validate(base(over));
    ok(!v.ok && v.errors.some(e => e.code === code), 'error ' + code);
    ok(!P.buildSummary(base(over), 'en').ok, 'no summary for ' + code);
  }
}

// 8. Pounds/ounces
{
  const w = P.normalizeWeight({ value: '5', unit: 'lb-oz', ounces: '8' });
  ok(Math.abs(w.grams - (5 * 453.59237 + 8 * 28.349523125)) < 1e-9, 'lb-oz conversion');
  eq(P.normalizeWeight({ value: '5', unit: 'lb-oz', ounces: '16' }).code, 'ounces-range');
  eq(P.normalizeWeight({ value: '5.5', unit: 'lb-oz', ounces: '' }).code, 'pounds-integer');
}

// 9. Typo confirmation, not silent change
{
  const v = P.validate(base({ birthWeight: { value: '250', unit: 'g' } }));
  ok(!v.ok && v.needsConfirm, 'unusual weight needs confirmation');
  ok(P.validate(base({ birthWeight: { value: '250', unit: 'g' }, confirmedUnusual: true })).ok, 'confirmed passes');
  ok(P.validate(base({ gestation: { weeks: '43', days: '' } })).needsConfirm, 'unusual weeks');
  eq(P.normalizeWeight({ value: '250', unit: 'g' }).grams, 250);
}

// 10. Dialysis yes, AKI no: both kept, clarification prompt
{
  const s = P.buildSummary(base({ neonatalDialysis: 'yes', neonatalAKI: 'no' }), 'en');
  ok(s.ruleIds.includes('inconsistent') && s.ruleIds.includes('neonatal'), 'inconsistent + neonatal');
  ok(s.entered.find(e => e.label.startsWith('Newborn dialysis')).value.startsWith('Yes'), 'dialysis kept');
  ok(s.entered.find(e => e.label.startsWith('Newborn kidney injury')).value.startsWith('No'), 'AKI kept');
}

// 11. Cardiac and current concern
{
  const r = rules({ majorCongenitalHeartCondition: 'yes', clinicianIdentifiedCurrentConcern: 'yes' });
  ok(r.includes('cardiac') && r.includes('congenital') && r.includes('current'), 'cardiac/congenital/current');
}

// 12. Adolescent growth period
{
  ok(rules({ audienceAge: 'adolescent', gestation: { weeks: '35', days: '' } }).includes('growthYears'), 'adolescent preterm');
  ok(!rules({ audienceAge: 'adult', gestation: { weeks: '35', days: '' } }).includes('growthYears'), 'adult no');
  ok(!rules({ audienceAge: 'adolescent' }).includes('growthYears'), 'adolescent without history no');
}

// 13. Recollection-only history labeled as reported in summary and plain text
{
  const s = P.buildSummary(base({ sourceConfidence: 'family-recollection', birthWeight: { value: '2', unit: 'kg' } }), 'en');
  ok(s.entered[1].value.includes('(reported)'), 'reported label on weight');
  ok(P.toPlainText(s).includes('(reported)'), 'reported in plain text');
  const m = P.buildSummary(base({ sourceConfidence: 'medical-record', birthWeight: { value: '2', unit: 'kg' } }), 'en');
  ok(!m.entered[1].value.includes('reported'), 'no reported label for records');
}

// 14. Rule order is fixed and deduplicated
{
  const r = rules({ birthWeight: { value: '1200', unit: 'g' }, gestation: { weeks: '30', days: '2' }, documentedSGA: 'yes',
    neonatalAKI: 'yes', neonatalDialysis: 'yes', majorCongenitalHeartCondition: 'yes', audienceAge: 'adolescent',
    clinicianIdentifiedCurrentConcern: 'yes' });
  eq(r, P.RULE_ORDER.filter(id => r.includes(id)), 'table order');
  const s = P.buildSummary(base({ birthWeight: { value: '1200', unit: 'g' } }), 'en');
  eq(new Set(s.questions.map(q => q.text)).size, s.questions.length, 'no duplicate questions');
}

// 15. Every language has every string; no output text is missing
{
  const keys = Object.keys(P.strings.en.Q);
  for (const lang of ['tl', 'ceb', 'kap']) {
    const t = P.strings[lang];
    for (const k of keys) ok(t.Q[k] && (Array.isArray(t.Q[k]) ? t.Q[k].length === 4 : t.Q[k].length > 10), lang + ' Q.' + k);
    for (const k of Object.keys(P.strings.en.E)) ok(t.E[k], lang + ' E.' + k);
    const s = P.buildSummary(base({ birthWeight: { value: '1200', unit: 'g' }, gestation: { weeks: '30', days: '' },
      documentedSGA: 'yes', majorCongenitalHeartCondition: 'yes', audienceAge: 'adolescent' }), lang);
    ok(s.ok && s.questions.every(q => typeof q.text === 'string' && q.text.length > 5), lang + ' summary complete');
    ok(!/undefined/.test(P.toPlainText(s)), lang + ' no undefined');
  }
}

// 16. Static study table in the guide matches the authoritative JSON
{
  const data = JSON.parse(fs.readFileSync(path.join(root, 'assets/born-small-evidence-data.json'), 'utf8'));
  const html = fs.readFileSync(path.join(root, 'guides/born-small-kidneys-for-life.html'), 'utf8');
  const tables = [...html.matchAll(/<table[^>]*class="[^"]*bs-study-table[^"]*"[^>]*>([\s\S]*?)<\/table>/g)];
  ok(tables.length >= 1, 'study table present');
  for (const [, body] of tables) {
    const rows = [...body.matchAll(/<tr[^>]*data-cohort="([^"]+)"[^>]*data-group="([^"]+)"[^>]*data-risk="([\d.]+)"[^>]*>/g)];
    ok(rows.length >= 4, 'table rows');
    for (const [, cohort, group, risk] of rows) {
      const c = data.cohorts.find(x => x.id === cohort);
      const g = c && c.groups.find(x => x.id === group);
      ok(g && g.risk_pct === Number(risk), `table ${cohort}/${group} = JSON`);
    }
  }
  for (const c of data.cohorts) {
    const aga = c.groups.find(g => g.id === 'AGA').risk_pct, sga = c.groups.find(g => g.id === 'SGA').risk_pct;
    const pp = Math.round((sga - aga) * 10) / 10;
    eq(pp, c.expected.diff_pp, c.id + ' pp');
    eq(Math.round(pp * 10), c.expected.diff_per1k, c.id + ' per1k');
  }
  // Privacy: the planner must not touch storage or network with entered data
  const js = fs.readFileSync(path.join(root, 'assets/born-small-planner.js'), 'utf8');
  ok(!/localStorage\.setItem|sessionStorage|fetch\(|XMLHttpRequest|sendBeacon|history\.(push|replace)State|location\.hash\s*=/.test(js), 'no storage/network writes');
}

console.log(`born-small-planner: ${checks} checks passed`);
