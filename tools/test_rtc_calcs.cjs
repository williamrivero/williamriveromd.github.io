/* ===== RTC-CALC-CORE (pure functions; tested by tools/test_rtc_calcs.cjs) ===== */
var RTC = (function () {
  function n(x) { var v = parseFloat(x); return isFinite(v) ? v : NaN; }
  function addDays(d, k) { var r = new Date(d.getTime()); r.setDate(r.getDate() + k); return r; }
  function addMonths(d, m) { var r = new Date(d.getTime()); var day = r.getDate(); r.setDate(1); r.setMonth(r.getMonth() + m); var last = new Date(r.getFullYear(), r.getMonth() + 1, 0).getDate(); r.setDate(Math.min(day, last)); return r; }
  function days(a, b) { return Math.round((Date.UTC(b.getFullYear(), b.getMonth(), b.getDate()) - Date.UTC(a.getFullYear(), a.getMonth(), a.getDate())) / 86400000); }
  function addWorkingDays(d, k) { var r = new Date(d.getTime()), c = 0; while (c < k) { r.setDate(r.getDate() - 1); var w = r.getDay(); if (w !== 0 && w !== 6) c++; } return r; }
  function gates(map) {
    var open = [], pending = [], closed = 0, total = 0;
    Object.keys(map).forEach(function (k) { var v = map[k]; if (v === "na") return; total++; if (v === "closed") closed++; else if (v === "pending") pending.push(k); else open.push(k); });
    return { ready: open.length === 0 && pending.length === 0 && total > 0, open: open, pending: pending, closed: closed, total: total };
  }
  function aging(opened, due, today, warn) {
    var o = days(opened, today), toDue = days(today, due), tier;
    if (toDue < 0) tier = -toDue > 7 ? "escalate" : "overdue"; else if (toDue <= warn) tier = "due soon"; else tier = "on time";
    return { daysOpen: o, daysToDue: toDue, tier: tier };
  }
  function validity(approved, surgery, validDays, today) {
    var expiry = addDays(approved, validDays);
    return { expiry: expiry, daysLeft: today ? days(today, expiry) : NaN, surgeryOk: surgery ? surgery <= expiry : null, surgeryMargin: surgery ? days(surgery, expiry) : NaN };
  }
  function filing(discharge, windowDays, today) { var dl = addDays(discharge, windowDays); return { deadline: dl, daysLeft: days(today, dl) }; }
  function gap(estimate, rate, confirmed, promised) { var g = estimate - rate - confirmed; return { gap: Math.max(0, g), surplus: g < 0 ? -g : 0, ifPromised: Math.max(0, g - promised) }; }
  function runway(onHand, perDay, leadWorking, closures, today) {
    if (!(perDay > 0)) return null;
    var d = Math.floor(onHand / perDay), runOut = addDays(today, d), latest = addDays(addWorkingDays(runOut, leadWorking), -closures);
    return { days: d, runOut: runOut, latestRefill: latest, actNow: latest <= today };
  }
  function donorPlan(donation, years) { var out = [{ label: "6 months", date: addMonths(donation, 6) }]; for (var y = 1; y <= years; y++) out.push({ label: y === 1 ? "1 year" : y + " years", date: addMonths(donation, 12 * y) }); return out; }
  return { n: n, addDays: addDays, addMonths: addMonths, days: days, addWorkingDays: addWorkingDays, gates: gates, aging: aging, validity: validity, filing: filing, gap: gap, runway: runway, donorPlan: donorPlan };
})();
if (typeof module !== "undefined") module.exports = RTC;
/* ===== END RTC-CALC-CORE ===== */
const assert=require('assert');const R=RTC;
const D=(y,m,d)=>new Date(y,m-1,d);const iso=d=>d.toISOString().slice(0,10);
const ymd=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
assert.equal(ymd(R.validity(D(2026,3,1),D(2026,9,15),180,D(2026,3,1)).expiry),'2026-08-28');
assert.equal(R.validity(D(2026,3,1),D(2026,9,15),180,null).surgeryOk,false);
assert.equal(ymd(R.filing(D(2026,7,1),60,D(2026,8,22)).deadline),'2026-08-30');
assert.equal(R.filing(D(2026,7,1),60,D(2026,8,22)).daysLeft,8);
assert.equal(R.gap(1200000,993000,0,0).gap,207000);
assert.equal(R.gap(1200000,993000,100000,50000).ifPromised,57000);
const rw=R.runway(40,4,5,0,D(2026,11,27));assert.equal(rw.days,10);assert.equal(ymd(rw.runOut),'2026-12-07');
assert.equal(ymd(rw.latestRefill),'2026-11-30');
const a=R.aging(D(2026,3,3),D(2026,3,10),D(2026,3,20),3);assert.equal(a.daysOpen,17);assert.equal(a.tier,'escalate');
assert.equal(R.gates({a:'closed',b:'na',c:'pending'}).ready,false);assert.equal(R.gates({a:'closed',b:'na'}).ready,true);
const p=R.donorPlan(D(2026,1,31),2);assert.equal(ymd(p[0].date),'2026-07-31');assert.equal(ymd(p[1].date),'2027-01-31');assert.equal(p.length,3);
console.log('RTC calc tests: all passed');
