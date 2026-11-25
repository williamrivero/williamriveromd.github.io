(function () {
  if (typeof document === "undefined") return;
  var $ = function (id) { return document.getElementById(id); }, v = function (id) { return DUO.n($(id).value); };
  var f1 = function (x, d) { return isFinite(x) ? x.toLocaleString("en-US", { maximumFractionDigits: d === undefined ? 1 : d }) : "&ndash;"; };
  var peso = function (x) { return isFinite(x) ? (x < 0 ? "&minus;" : "") + "&#8369;" + Math.round(Math.abs(x)).toLocaleString("en-US") : "&ndash;"; };
  var flag = function (cls, t) { return '<span class="flag f-' + cls + '">' + t + "</span>"; };
  var run = {
    c1: function () { var r = DUO.breakeven(v("c1_fx"), v("c1_rev"), v("c1_var"), v("c1_vol"));
      if (r.error) return flag("stop", "No break-even") + " " + r.error;
      var out = "Contribution: <b>" + peso(r.cm) + " per session</b> (" + f1(r.cmRatio * 100, 0) + "% of revenue).<br>Break-even: <b>" + r.be.toLocaleString("en-US") + " sessions a month</b>.";
      if (isFinite(r.profit)) out += "<br>At " + f1(v("c1_vol"), 0) + " sessions: operating result <b>" + peso(r.profit) + "</b> a month; margin of safety " + f1(r.safety * 100, 0) + "%. " + (r.profit >= 0 ? flag("ok", "Above break-even") : flag("warn", "Below break-even"));
      return out + '<p class="note">Operating result before tax, debt principal and owner distributions. Profit is not cash: see calculator 5.</p>'; },
    c2: function () { var vols = $("c2_vols").value.split(/[,\s]+/).map(Number).filter(function (x) { return isFinite(x) && x > 0; });
      if (!vols.length) return "Enter at least one volume.";
      var rows = DUO.costCurve(v("c2_fx"), v("c2_var"), vols, v("c2_step"), v("c2_sc"));
      return "<table><thead><tr><th>Sessions a month</th><th>Fixed cost</th><th>Total cost</th><th>Cost per treatment</th></tr></thead><tbody>" +
        rows.map(function (x) { return "<tr><td>" + x.v + "</td><td>" + peso(x.fixed) + "</td><td>" + peso(x.total) + "</td><td><b>" + peso(x.per) + "</b></td></tr>"; }).join("") +
        '</tbody></table><p class="note">Above the step, fixed cost jumps. Compare the extra sessions&rsquo; contribution (calculator 1) with the step cost before you commit.</p>'; },
    c3: function () { var r = DUO.capacity(v("c3_st"), v("c3_oos"), v("c3_sh"), v("c3_d"), v("c3_ss"), v("c3_pw"), v("c3_cen"));
      return "Physical capacity: <b>" + r.phys + " station-sessions a week</b>. Safely staffed: <b>" + r.staffed + "</b>. Limiting resource: <b>" + r.limit + "</b>.<br>Patients supported at " + f1(v("c3_pw"), 0) + " sessions a week: <b>" + r.patients + "</b>. " +
        (isFinite(r.util) ? "Census uses " + f1(r.util * 100, 0) + "% of safe capacity. " + (r.util > 1 ? flag("stop", "Over safe capacity") : r.util > 0.9 ? flag("warn", "Little room for make-up sessions") : flag("ok", "Room for make-up sessions")) : "") +
        '<p class="note">Keep slots free for make-up sessions and admissions. A full schedule leaves no room to reschedule a missed treatment.</p>'; },
    c4: function () { var r = DUO.fte(v("c4_p"), v("c4_s"), v("c4_h"), v("c4_c"), v("c4_r"), v("c4_cost"), v("c4_sess"));
      if (r.error) return r.error;
      return "Base requirement: <b>" + f1(r.base, 2) + " FTE</b>. With relief: <b>" + f1(r.need, 2) + " FTE</b>, so hire <b>" + r.hire + "</b>.<br>Monthly cost: <b>" + peso(r.cost) + "</b>" + (isFinite(r.perSession) ? ", or <b>" + peso(r.perSession) + " per session</b>" : "") + "." +
        '<p class="note">Check the result against the minimum ratios in your license conditions and the PSN guideline. Never round staffing down to meet a budget.</p>'; },
    c5: function () { var r = DUO.cash(v("c5_rev"), v("c5_ar"), v("c5_days"), v("c5_cash"), v("c5_cost"));
      return "Daily net revenue: <b>" + peso(r.daily) + "</b>. Cash tied up at " + f1(v("c5_days"), 0) + " days to collect: <b>" + peso(r.tied) + "</b>.<br>Days sales outstanding from your receivables: <b>" + f1(r.dso, 0) + " days</b>. Runway on cash in hand: <b>" + f1(r.runwayWeeks, 1) + " weeks</b>. " +
        (r.runwayWeeks < 8 ? flag("stop", "Under 8 weeks: act now") : r.runwayWeeks < 13 ? flag("warn", "Under 13 weeks") : flag("ok", "13 weeks or more")) +
        '<p class="note">The 8- and 13-week marks are teaching triggers, not a standard. Build your own 13-week cash forecast with base, delayed-collection and disruption cases.</p>'; },
    c6: function () { var r = DUO.loan(v("c6_p"), v("c6_r"), v("c6_y"), v("c6_cf"));
      if (r.error) return r.error;
      return "Monthly payment: <b>" + peso(r.pmt) + "</b>; yearly debt service <b>" + peso(r.annual) + "</b>; total interest over the term <b>" + peso(r.interest) + "</b>.<br>DSCR: <b>" + f1(r.dscr, 2) + "</b>. " +
        (r.dscr < 1 ? flag("stop", "Cash does not cover debt") : r.dscr < 1.25 ? flag("warn", "Thin cushion") : flag("ok", "Cushion above 1.25")) +
        '<p class="note">1.25 is a common lending reference, not a Philippine rule; your loan agreement sets the covenant. Test the ratio again with a 60-day collection delay.</p>'; },
    c7: function () { var r = DUO.project(v("c7_c"), v("c7_a"), v("c7_y"), v("c7_d"), v("c7_s"));
      if (r.error) return r.error;
      return "Simple payback: <b>" + (isFinite(r.payback) ? f1(r.payback, 1) + " years" : "never") + "</b>. Net present value at " + f1(v("c7_d"), 1) + "%: <b>" + peso(r.npv) + "</b>. " +
        (r.npv >= 0 ? flag("ok", "Returns at least the discount rate") : flag("warn", "Below the discount rate")) +
        '<p class="note">Some safety projects (a backup generator, a water-system repair) are required whatever their NPV. Use this to choose how to fund them, not whether.</p>'; },
    c8: function () { var r = DUO.patientShare({ pkg: v("c8_pk"), perWeek: v("c8_pw"), weeks: v("c8_wk"), limit: v("c8_lim"), addonSessions: v("c8_an"), addonCharge: v("c8_ac"), profFee: v("c8_pf"), selfPay: v("c8_sp"), support: v("c8_os") });
      return "Planned sessions: <b>" + r.planned + "</b> (" + r.covered + " within the limit, " + r.beyond + " beyond). PhilHealth pays up to <b>" + peso(r.pkgYear) + "</b>.<br>" +
        "Covered sessions: <b>no co-payment</b>. Optional additional services on " + r.addonSessions + " sessions: <b>" + peso(r.addon) + "</b>." + (r.beyond ? " Sessions beyond the limit: <b>" + peso(r.beyondTotal) + "</b>." : "") +
        "<br>Patient&rsquo;s yearly total: <b>" + peso(r.year) + "</b>. " + (r.profOverCap ? flag("stop", "Professional fee above 450 pesos") + " The calculator capped it at 450; the circular does not allow more." : flag("ok", "Within the 450-peso cap")) +
        '<p class="note">A co-payment applies only to an additional or premium service the patient received and was told about in advance, written on the agreement form. Never add a charge to every session.</p>'; }
  };
  document.querySelectorAll("button[data-run]").forEach(function (b) { b.addEventListener("click", function () { var id = b.getAttribute("data-run"); try { $(id + "_out").innerHTML = run[id](); } catch (e) { $(id + "_out").textContent = "Check the inputs."; } }); });
  Object.keys(run).forEach(function (k) { try { $(k + "_out").innerHTML = run[k](); } catch (e) {} });
})();
