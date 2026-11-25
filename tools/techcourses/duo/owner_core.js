/* ===== DUO-CALC-CORE (pure functions; tested by tools/techcourses/duo/test_owner_calc.cjs) ===== */
var DUO = (function () {
  function n(x) { var v = parseFloat(x); return isFinite(v) ? v : NaN; }
  function pos(x) { return isFinite(x) && x > 0; }
  /* 1. Contribution margin and break-even. Ordinary break-even is undefined when contribution is zero or negative. */
  function breakeven(fixed, revenue, variable, volume) {
    if (!(fixed >= 0) || !(revenue >= 0) || !(variable >= 0)) return { error: "Enter fixed cost, net revenue and variable cost as zero or more." };
    var cm = revenue - variable;
    if (cm <= 0) return { error: "Contribution per session is " + cm.toFixed(0) + ". No volume covers fixed costs when each session loses money before overhead. Fix price, payer mix or variable cost first." };
    var be = Math.ceil(fixed / cm - 1e-9);
    var out = { cm: cm, cmRatio: revenue > 0 ? cm / revenue : NaN, be: be };
    if (isFinite(volume) && volume >= 0) { out.profit = volume * cm - fixed; out.safety = volume > 0 ? (volume - be) / volume : NaN; }
    return out;
  }
  /* 2. Cost per treatment across volumes, with a step cost that starts above a threshold. */
  function costCurve(fixed, variable, vols, stepAt, stepCost) {
    return vols.map(function (v) {
      var f = fixed + (pos(stepAt) && v > stepAt ? (stepCost || 0) : 0);
      return { v: v, fixed: f, total: f + variable * v, per: v > 0 ? (f + variable * v) / v : NaN };
    });
  }
  /* 3. Physical versus staffed capacity in station-sessions per week, and patients supported at a given frequency. */
  function capacity(stations, oos, shifts, days, staffedStations, perWeek, census) {
    var usable = Math.max(0, stations - (oos || 0));
    var phys = usable * shifts * days;
    var staffed = (isFinite(staffedStations) && staffedStations >= 0) ? Math.min(usable, staffedStations) * shifts * days : phys;
    var safe = Math.min(phys, staffed);
    var pts = perWeek > 0 ? Math.floor(safe / perWeek) : NaN;
    return { usable: usable, phys: phys, staffed: staffed, safe: safe, patients: pts, util: (isFinite(census) && pts > 0) ? census / pts : NaN,
             limit: staffed < phys ? "staffing" : "stations" };
  }
  /* 4. Full-time equivalents with a relief factor, and staff cost per session. */
  function fte(postsPerShift, shiftsPerWeek, hoursPerShift, contractHours, relief, monthlyCostPerFte, sessionsPerMonth) {
    if (!pos(contractHours)) return { error: "Enter contracted hours per week." };
    var base = postsPerShift * shiftsPerWeek * hoursPerShift / contractHours;
    var need = base * (1 + (relief || 0) / 100);
    var cost = need * (monthlyCostPerFte || 0);
    return { base: base, need: need, hire: Math.ceil(need - 1e-9), cost: cost, perSession: pos(sessionsPerMonth) ? cost / sessionsPerMonth : NaN };
  }
  /* 5. Cash tied up in receivables, days sales outstanding, and weeks of runway. */
  function cash(netRevenueMonth, receivables, daysToCollect, cashOnHand, monthlyCashCosts) {
    var daily = netRevenueMonth / 30;
    var tied = daily * daysToCollect;
    var dso = daily > 0 ? receivables / daily : NaN;
    var weeklyCost = monthlyCashCosts * 12 / 52;
    return { daily: daily, tied: tied, dso: dso, runwayWeeks: weeklyCost > 0 ? cashOnHand / weeklyCost : Infinity };
  }
  /* 6. Level loan payment and debt service coverage ratio. */
  function loan(principal, annualRatePct, years, annualCashAvailable) {
    if (!pos(principal) || !pos(years)) return { error: "Enter a principal and a term above zero." };
    var nPer = Math.round(years * 12), r = annualRatePct / 100 / 12;
    var pmt = r === 0 ? principal / nPer : principal * r / (1 - Math.pow(1 + r, -nPer));
    var annual = pmt * 12;
    return { pmt: pmt, annual: annual, interest: pmt * nPer - principal, dscr: annual > 0 ? annualCashAvailable / annual : NaN };
  }
  /* 7. Simple payback and net present value of a capital project. */
  function project(capex, annualNet, years, discountPct, salvage) {
    if (!pos(capex)) return { error: "Enter the capital cost." };
    var d = discountPct / 100, npv = -capex;
    for (var t = 1; t <= years; t++) npv += annualNet / Math.pow(1 + d, t);
    if (salvage) npv += salvage / Math.pow(1 + d, years);
    return { payback: annualNet > 0 ? capex / annualNet : Infinity, npv: npv };
  }
  /* 8. What the patient pays in a year. Covered sessions carry no co-payment (PhilHealth Circular 2024-0023): the patient pays only for
     optional additional or premium services, with an additional professional fee capped at 450 pesos, and for sessions beyond the yearly limit. */
  function patientShare(o) {
    var planned = Math.round(o.perWeek * o.weeks);
    var covered = Math.min(planned, o.limit);
    var beyond = Math.max(0, planned - covered);
    var addonSessions = Math.min(Math.max(0, o.addonSessions || 0), covered);
    var prof = Math.max(0, o.profFee || 0);
    var addon = addonSessions * (Math.max(0, o.addonCharge || 0) + Math.min(prof, 450));
    var perBeyond = Math.max(0, (o.selfPay || 0) - (o.support || 0));
    return { planned: planned, covered: covered, beyond: beyond, addonSessions: addonSessions, addon: addon, perBeyond: perBeyond,
             beyondTotal: beyond * perBeyond, year: addon + beyond * perBeyond, pkgYear: covered * o.pkg, profOverCap: prof > 450 };
  }
  return { n: n, breakeven: breakeven, costCurve: costCurve, capacity: capacity, fte: fte, cash: cash, loan: loan, project: project, patientShare: patientShare };
})();
if (typeof module !== "undefined") module.exports = DUO;
/* ===== END DUO-CALC-CORE ===== */
