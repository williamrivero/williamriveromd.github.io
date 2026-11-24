// Tests for the Medical Records Officer toolkit core (guides/calc-medical-records-officer-toolkit.html).
// Run: node tools/test_mro_calcs.cjs
const fs = require('fs'), path = require('path'), vm = require('vm');
const html = fs.readFileSync(path.join(__dirname, '..', 'guides', 'calc-medical-records-officer-toolkit.html'), 'utf8');
const core = html.slice(html.indexOf('var MRO = (function'), html.indexOf('/* ===== END MRO-CALC-CORE'));
const ctx = {}; vm.createContext(ctx); vm.runInContext(core + '\nthis.MRO = MRO;', ctx); const MRO = ctx.MRO;
const assert = require('assert');
const D=(s)=>new Date(s+'T00:00');
let L=MRO.ledger(156,141,2,3,6350,D('2026-11-07')); assert.equal(L.left,13); assert.equal(L.valueLeft,13*6350); assert.ok(L.beforeYearEnd);
console.log('cap', L.cap.toDateString());
let R=MRO.reuse(32,5,26,128,20); assert.equal(R.dzLeft,6); assert.equal(R.usesLeft,32);
let T=MRO.retention(D('2019-06-30'),7,0,false,D('2026-11-24')); assert.equal(T.eligible.toDateString(),D('2026-06-30').toDateString()); assert.equal(T.status,'eligible');
assert.equal(MRO.retention(D('2019-06-30'),7,0,true,D('2026-11-24')).status,'hold');
assert.equal(MRO.retention(D('2019-06-30'),7,15,false,D('2026-11-24')).status,'retain');
let C=MRO.clock(MRO.parseDT('2026-11-24 14:15'),MRO.parseDT('2026-11-24 15:15')); assert.equal(C.deadline.toISOString(),MRO.parseDT('2026-11-27 14:15').toISOString()); assert.equal(C.left,71);
let W=MRO.wilson(16,20); assert.equal(Math.round(W.lo*1000),584); assert.equal(Math.round(W.hi*1000),919);
assert.equal(MRO.sampleSize(0.8,0.1),62); assert.equal(MRO.sampleSize(0.5,0.1),97);
let B=MRO.batch(18,16,1,0); assert.equal(B.variance,1);
let V=MRO.vintage(D('2021-03-03'),D('2026-11-24')); assert.deepEqual([V.y,V.m,V.d],[5,8,21]);
assert.equal(MRO.days(D('2026-07-30'),D('2026-12-10')),133);
console.log('all MRO calculator tests passed');
