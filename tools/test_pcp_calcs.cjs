// Tests for the Patient and Care Partner Toolkit core (tools/patients_care_partners/toolkit/script.html).
// Run: node tools/test_pcp_calcs.cjs
const fs = require("fs"), path = require("path"), assert = require("assert");
const src = fs.readFileSync(path.join(__dirname, "patients_care_partners", "toolkit", "script.html"), "utf8");
const core = src.split("/* ===== PCP-CALC-CORE")[1].split("/* ===== END PCP-CALC-CORE")[0];
const m = { exports: {} };
new Function("module", core.slice(core.indexOf("\n")) + "\nmodule.exports = PCP;")(m);
const P = m.exports;
let n = 0; const t = (name, fn) => { fn(); n++; };
const d = (y, mo, da) => new Date(y, mo - 1, da);

t("trend sorts and computes change", () => {
  const r = P.trend([{ d: d(2026, 6, 1), v: 40 }, { d: d(2026, 1, 1), v: 50 }, { d: d(2026, 11, 1), v: 38 }]);
  assert.strictEqual(r.points[0].v, 50); assert.strictEqual(r.change, -12); assert.strictEqual(Math.round(r.pct), -24);
});
t("trend needs two points", () => { assert.strictEqual(P.trend([{ d: d(2026, 1, 1), v: 50 }]).change, null); });
t("sodium multiplies servings", () => {
  const r = P.sodium([{ mg: 820, servings: 2 }, { mg: 300, servings: 1 }]);
  assert.strictEqual(r.total, 1940); assert.strictEqual(Math.round(r.whoShare), 97); assert.strictEqual(r.target, undefined);
});
t("sodium against own target", () => { const r = P.sodium([{ mg: 500, servings: 3 }], 1500); assert.strictEqual(r.left, 0); });
t("fluid requires own allowance", () => { assert.throws(() => P.fluid(NaN, [250])); });
t("fluid counts and reports remaining", () => { const r = P.fluid(1000, [250, 150, 200, NaN]); assert.strictEqual(r.used, 600); assert.strictEqual(r.left, 400); });
t("fluid over plan is negative left", () => { assert.strictEqual(P.fluid(500, [600]).left, -100); });
t("weight gain and percent of target", () => { const r = P.gain(58, 60.3, 58); assert.strictEqual(Math.round(r.gain * 10), 23); assert.strictEqual(Math.round(r.pct * 10), 40); });
t("weight gain without target", () => { assert.strictEqual(P.gain(58, 59, NaN).pct, null); });
t("sessions left and run-out date", () => {
  const r = P.sessions(156, 120, 3, d(2026, 11, 28)); assert.strictEqual(r.left, 36);
  assert.deepStrictEqual([r.runOut.getFullYear(), r.runOut.getMonth() + 1, r.runOut.getDate()], [2027, 2, 20]);
});
t("sessions never negative", () => { assert.strictEqual(P.sessions(156, 160, 3, d(2026, 1, 1)).left, 0); });
t("refill plan two weeks ahead", () => {
  const r = P.refill(["20:00", "08:00", ""], 1, 40, 14, d(2026, 11, 28));
  assert.deepStrictEqual(r.times, ["08:00", "20:00"]); assert.strictEqual(r.days, 20); assert.strictEqual(r.askNow, false);
  assert.strictEqual(r.ask.getDate(), d(2026, 12, 4).getDate());
});
t("refill ask now when short", () => { assert.strictEqual(P.refill(["08:00"], 1, 10, 14, d(2026, 11, 28)).askNow, true); });
t("negative inputs rejected", () => { assert.throws(() => P.gain(-1, 60)); assert.throws(() => P.sessions(156, -1, 3, new Date())); });
console.log(`PCP toolkit: ${n} tests passed`);
