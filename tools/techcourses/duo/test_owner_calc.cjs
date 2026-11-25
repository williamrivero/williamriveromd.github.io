// Tests for the Dialysis Unit Owner toolkit core. Run: node test_owner_calc.cjs <path to owner_core.js>
const assert = require("assert");
const DUO = require(require("path").resolve(process.argv[2] || require("path").join(__dirname, "owner_core.js")));
const near = (a, b, tol = 0.5) => assert.ok(Math.abs(a - b) <= tol, `${a} != ${b}`);

// Blueprint toolkit example: 6000 − 3900 = 2100; 630000 / 2100 = 300 sessions.
let b = DUO.breakeven(630000, 6000, 3900, 400);
assert.strictEqual(b.cm, 2100); assert.strictEqual(b.be, 300); near(b.profit, 210000);
// Unit Manager example: 920000 / (6350 − 2100) = 216.5 → 217.
assert.strictEqual(DUO.breakeven(920000, 6350, 2100).be, 217);
// Nonpositive contribution is rejected.
assert.ok(DUO.breakeven(500000, 3000, 3000).error);
assert.ok(DUO.breakeven(500000, 2500, 3000).error);

let c = DUO.costCurve(920000, 2100, [400, 350], 380, 150000);
near(c[0].per, (1070000 + 2100 * 400) / 400); near(c[1].per, (920000 + 2100 * 350) / 350);

let k = DUO.capacity(12, 1, 3, 6, 9, 3, 140);
assert.strictEqual(k.phys, 198); assert.strictEqual(k.staffed, 162); assert.strictEqual(k.safe, 162);
assert.strictEqual(k.patients, 54); assert.strictEqual(k.limit, "staffing");

let f = DUO.fte(3, 18, 6, 48, 15, 38000, 600);
near(f.base, 6.75, 0.001); near(f.need, 7.7625, 0.001); assert.strictEqual(f.hire, 8);

let cs = DUO.cash(2540000, 6350000, 75, 3000000, 2200000);
near(cs.tied, 6350000, 1); near(cs.dso, 75, 0.01);

let l = DUO.loan(12000000, 9, 7, 3200000);
near(l.pmt, 193070, 5); near(l.dscr, 3200000 / (l.pmt * 12), 0.0001);
assert.ok(DUO.loan(0, 9, 7, 1).error);
near(DUO.loan(1200, 0, 1, 1200).pmt, 100, 0.001);

let p = DUO.project(4500000, 1200000, 7, 10, 0);
near(p.payback, 3.75, 0.001); near(p.npv, 1342105, 10);

let s = DUO.patientShare({ pkg: 6350, perWeek: 3, weeks: 52, limit: 156, addonSessions: 4, addonCharge: 0, profFee: 450, selfPay: 6350, support: 0 });
assert.strictEqual(s.planned, 156); assert.strictEqual(s.beyond, 0); assert.strictEqual(s.addon, 1800); assert.strictEqual(s.year, 1800); assert.ok(!s.profOverCap);
let s2 = DUO.patientShare({ pkg: 6350, perWeek: 3, weeks: 53, limit: 156, addonSessions: 0, profFee: 600, selfPay: 6350, support: 0 });
assert.strictEqual(s2.beyond, 3); assert.strictEqual(s2.year, 3 * 6350); assert.ok(s2.profOverCap);
let s3 = DUO.patientShare({ pkg: 6350, perWeek: 3, weeks: 52, limit: 156, addonSessions: 2, addonCharge: 0, profFee: 900, selfPay: 0 });
assert.strictEqual(s3.addon, 900);
console.log("owner toolkit core: all tests passed");
