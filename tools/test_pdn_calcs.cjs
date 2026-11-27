// Tests for the Pediatric Dialysis Nurse Toolkit core (guides/calc-pediatric-dialysis-nurse-toolkit.html).
const fs = require("fs"), path = require("path"), assert = require("assert");
const html = fs.readFileSync(path.join(__dirname, "..", "guides", "calc-pediatric-dialysis-nurse-toolkit.html"), "utf8");
const core = html.match(/\/\* ===== PDN-CALC-CORE[\s\S]*?\/\* ===== END PDN-CALC-CORE ===== \*\//)[0];
const m = { exports: {} }; new Function("module", core)(m); const P = m.exports;
const near = (a, b, t = 0.01) => assert.ok(Math.abs(a - b) <= t, a + " vs " + b);
near(P.bsa(110, 18), 0.7416, 0.001);
let f = P.fill(110, 18, 5, 1000); near(f.perM2, 1348.4, 0.5); near(f.perKg, 55.56, 0.01); assert.strictEqual(f.band, "within");
f = P.fill(75, 9, 1, 900); near(f.perM2, 2078.5, 0.5); assert.strictEqual(f.band, "above");
f = P.fill(75, 9, 1, 300); near(f.perM2, 692.8, 0.5); assert.strictEqual(f.band, "within");
let e = P.ecv(10, 2, 40, 28); near(e.ebv, 800); near(e.pct, 8.5); e = P.ecv(3.5, 0, 40, 28); near(e.ebv, 297.5); near(e.pct, 22.86, 0.01);
let q = P.qb(20, 115, 120); near(q.perKg, 6); near(q.rule, 75); near(q.first, 60);
let u = P.ufr(30, 1200, 3); near(u.perH, 400); near(u.perKgH, 13.33, 0.01); near(u.pctBwH, 1.333, 0.001);
assert.strictEqual(P.pdNet(600, 680), 80);
near(P.fo(3.8, 1.3, 25), 10);
near(P.perPtYear(3, 96), 0.375); near(P.perPtYear(4, 90), 0.5333, 0.001); assert.strictEqual(P.perPtYear(1, 0), null);
near(P.per100(1, 60), 1.6667, 0.001);
assert.throws(() => P.bsa(0, 10)); assert.throws(() => P.perPtYear(1.5, 12));
console.log("pdn toolkit: all tests passed");
