// Tests for the Renal Social Worker toolkit core (guides/calc-social-worker-toolkit.html). Run: node tools/test_sw_calcs.cjs
const fs = require("fs"), path = require("path"), assert = require("assert");
const page = fs.readFileSync(path.join(__dirname, "..", "guides", "calc-social-worker-toolkit.html"), "utf8");
const core = page.split("/* ===== SW-CALC-CORE")[1].split("/* ===== END SW-CALC-CORE")[0];
const mod = { exports: {} }; new Function("module", "/*" + core.slice(core.indexOf("*/")))(mod);
const SW = mod.exports;
const close = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, a + " != " + b);
// 1 access cost: handoff example
let r = SW.accessCost({ visits: 6, outward: 120, back: 120, escort: 0, other: 30, oneTime: 300, confirmed: 1000 });
close(r.gross, 1920); close(r.gap, 920); close(r.excess, 0);
assert.throws(() => SW.accessCost({ visits: 2.5, outward: 1, back: 1, escort: 0, other: 0, oneTime: 0, confirmed: 0 }));
assert.throws(() => SW.accessCost({ visits: 2, outward: -1, back: 1, escort: 0, other: 0, oneTime: 0, confirmed: 0 }));
assert.throws(() => SW.accessCost({ visits: SW.n(""), outward: 1, back: 1, escort: 0, other: 0, oneTime: 0, confirmed: 0 }));
assert.throws(() => SW.accessCost({ visits: Infinity, outward: 1, back: 1, escort: 0, other: 0, oneTime: 0, confirmed: 0 }));
// 2 spending share
r = SW.spendShare(4000, 25000); close(r.share, 16); assert.ok(r.over10 && !r.over25);
assert.strictEqual(SW.spendShare(0, 0), null);
assert.throws(() => SW.spendShare(5, 4));
// 3 sessions
r = SW.sessions(156, 120, 3, new Date(2026, 8, 30)); assert.strictEqual(r.left, 36); close(r.weeks, 12);
assert.strictEqual(r.runOut.getFullYear() + "-" + (r.runOut.getMonth() + 1) + "-" + r.runOut.getDate(), "2026-12-23");
assert.strictEqual(SW.sessions(156, 160, 3, new Date(2026, 0, 1)).left, 0);
assert.strictEqual(SW.sessions(156, 10, 0, new Date(2026, 0, 1)).weeks, null);
// 4 aging
r = SW.aging(new Date(2026, 2, 3), new Date(2026, 2, 13), new Date(2026, 2, 20), 3);
assert.strictEqual(r.daysOpen, 17); assert.strictEqual(r.daysToDue, -7); assert.strictEqual(r.tier, "overdue");
assert.strictEqual(SW.aging(new Date(2026, 2, 1), new Date(2026, 2, 10), new Date(2026, 2, 18), 3).tier, "escalate");
assert.strictEqual(SW.aging(new Date(2026, 2, 1), new Date(2026, 2, 10), new Date(2026, 2, 8), 3).tier, "due soon");
assert.strictEqual(SW.aging(new Date(2026, 2, 1), new Date(2026, 2, 20), new Date(2026, 2, 8), 3).tier, "on track");
// 5 workload: handoff example
r = SW.workload([{ episodes: 8, minutes: 45 }, { episodes: 2, minutes: 120 }], 5, 12, 30);
close(r.demand, 15); close(r.balance, -3); close(r.fte, 0.5);
assert.throws(() => SW.workload([{ episodes: 1.5, minutes: 45 }], 0, 1, 30));
assert.throws(() => SW.workload([], 0, 1, 0));
// 6 rate
close(SW.rate(10, 12), 83.33333333333333); assert.strictEqual(SW.rate(0, 0), null);
assert.throws(() => SW.rate(5, 4)); assert.throws(() => SW.rate(1.5, 4)); assert.throws(() => SW.rate(-1, 4));
// privacy: no network or storage calls in the page script
const script = page.split("/* ===== SW-CALC-CORE")[1].split("</script>")[0];
["fetch(", "XMLHttpRequest", "localStorage", "sessionStorage", "navigator.sendBeacon"].forEach(k => assert.ok(!script.includes(k), "found " + k));
console.log("social worker toolkit: all tests passed");
