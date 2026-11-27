// Tests for the Resuscitation Lab toolkit core (guides/calc-resuscitation-lab-toolkit.html). Run: node tools/test_resus_toolkit.cjs
const fs = require("fs"), path = require("path"), assert = require("assert");
const page = fs.readFileSync(path.join(__dirname, "..", "guides", "calc-resuscitation-lab-toolkit.html"), "utf8");
const core = page.split("/* ===== RL-CALC-CORE")[1].split("/* ===== END RL-CALC-CORE")[0];
const mod = { exports: {} }; new Function("module", "/*" + core.slice(core.indexOf("*/")))(mod);
const RL = mod.exports;
const close = (a, b, e) => assert.ok(Math.abs(a - b) < (e || 1e-9), a + " != " + b);
// 1 CCF: 600 s with pauses 8+6+14+9+22+7 = 66 s -> 89.0%
let r = RL.ccf(600, RL.list("8, 6, 14, 9, 22, 7"));
close(r.fraction, 89); assert.strictEqual(r.totalPause, 66); assert.strictEqual(r.longest, 22); assert.strictEqual(r.over10, 2);
close(RL.ccf(100, []).fraction, 100);
assert.throws(() => RL.ccf(10, [11]));        // boundary: pauses exceed observation
assert.throws(() => RL.ccf(0, [1]));          // error: zero observation
assert.throws(() => RL.list("5, x"));         // error: bad pause
assert.strictEqual(RL.ccf(100, [10]).over10, 0); // boundary: exactly 10 s is not over 10
// 2 timeline: default log
const log = "00:00 recognition\n00:12 compressions start\n00:35 pads on\n00:40 compressions stop\n00:46 shock\n00:47 compressions start\n00:58 circuit stopped\n01:30 blood returned\n02:47 compressions stop\n02:53 compressions start\n03:10 epinephrine\n04:50 compressions stop\n04:58 shock\n04:59 compressions start\n07:05 epinephrine\n08:00 ROSC";
r = RL.timeline(RL.parse(log));
assert.strictEqual(r.toCompression, 12); assert.strictEqual(r.toPads, 35); assert.strictEqual(r.toShock, 46); assert.strictEqual(r.toEpi, 190);
assert.strictEqual(r.toCircuit, 58); assert.strictEqual(r.toRosc, 480); assert.strictEqual(r.shocks, 2); assert.deepStrictEqual(r.epiGaps, [235]);
// on-time: 12-40 (28) + 47-167 (120) + 173-290 (117) + 299-480 (181) = 446 of window 468 -> 95.3%
close(r.fraction, 100 * 446 / 468); assert.strictEqual(r.longestPause, 9); assert.strictEqual(r.pausesOver10, 0);
assert.throws(() => RL.parse("1:5 shock"));   // error: bad time
assert.throws(() => RL.timeline([]));         // error: empty
assert.strictEqual(RL.timeline(RL.parse("00:05 recognition\n00:30 compressions start\n01:00 end")).toCompression, 25);
// 3 pediatric trainer (AHA 2025 algorithm doses)
r = RL.peds(20, "epi", 0.1); close(r.dose, 0.2); close(r.volume, 2); assert.ok(!r.capped); assert.ok(!r.concMismatch);
r = RL.peds(120, "epi", 0.1); close(r.dose, 1); assert.ok(r.capped);       // boundary: maximum 1 mg
r = RL.peds(20, "epi", 1); close(r.volume, 0.2); assert.ok(r.concMismatch); // concentration trap flagged
r = RL.peds(25, "amio", 50); close(r.dose, 125); close(r.volume, 2.5);
close(RL.peds(70, "amio", 50).dose, 300);                                  // boundary: maximum 300 mg
close(RL.peds(20, "lido", 20).dose, 20);
close(RL.peds(20, "ade1", 3).dose, 2); close(RL.peds(80, "ade1", 3).dose, 6); close(RL.peds(80, "ade2", 3).dose, 12);
close(RL.peds(20, "def1").raw, 40); close(RL.peds(20, "def2").raw, 80); close(RL.peds(20, "defmax").raw, 200);
r = RL.peds(20, "cv1"); close(r.raw, 10); close(r.high, 20); close(RL.peds(20, "cv2").raw, 40);
close(RL.peds(20, "fl20").raw, 400); close(RL.peds(20, "fl10").raw, 200);
assert.ok(RL.peds(45, "epi", 0.1).adultSize);
assert.throws(() => RL.peds(0.2, "epi", 0.1));  // error: weight too low
assert.throws(() => RL.peds(200, "epi", 0.1));  // error: weight too high
assert.throws(() => RL.peds(20, "epi", 0));     // error: zero concentration
assert.ok(RL.checkTry(2, 2).ok); assert.ok(RL.checkTry(20, 2).tenfold); assert.ok(!RL.checkTry(2.5, 2).ok);
assert.strictEqual(RL.checkTry(NaN, 2), null);
// 4 oxygen: 680 L at 2000, now 1000, reserve 200, 15 L/min -> 272 L, 18.1 min
r = RL.oxygen(680, 2000, 1000, 200, 15); close(r.usable, 272); close(r.minutes, 272 / 15);
assert.strictEqual(RL.oxygen(680, 2000, 100, 200, 15).usable, 0);    // boundary: below reserve
assert.throws(() => RL.oxygen(680, 2000, 2500, 200, 15));             // error: above full
// 5 rotation
let rows = RL.rotation(["A", "B", "C"], ["Leader", "Compressor", "Recorder", "Airway", "Watcher"], 3);
assert.strictEqual(rows.length, 3);
rows.forEach((row) => assert.ok(!/combine/.test(row.Watcher), "watcher never combined"));
assert.strictEqual(rows[0].Leader, "A"); assert.strictEqual(rows[1].Leader, "B");
assert.throws(() => RL.rotation([], ["Leader"], 1));
console.log("resus toolkit: all tests passed");
