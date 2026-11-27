/* Renal Care Academy: inline tools inside modules (Dr. William Gregory Rivero, Nov 27 2026).
 *
 * Small working versions of Calculo calculators and Dosis lookups, placed in the module section that teaches them:
 *   ktv     spKt/V (Daugirdas second generation, UF / post-dialysis weight), URR and ultrafiltration rate:
 *           the same formula and targets as /guides/calc-dialysis-adequacy-ktv.
 *   sodium  Hyponatremia correction: total body water, sodium deficit for a planned rise, Adrogué–Madias change per
 *           infusate (150 mL 3% bolus; volume of 3% saline for the planned rise) checked against the correction
 *           limits the module teaches (data-opts "limits").
 *   dose    Kidney function (Cockcroft–Gault CrCl, CKD-EPI 2021 eGFR, as on the Calculo pages) and the APPROVED
 *           Dosis kidney-dosing tiles for that function or dialysis modality, quoted as published in the Drug Index
 *           (window.RCM_KDOSE, built by tools/academy/apply_tools.py from drugs/interactions.json).
 * Markup: <form class="rcm-tool" data-tool="ktv|sodium|dose" data-opts='{...}'> written by apply_tools.py from
 * data/academy-tools.json. A <form>, so Listen (read aloud) skips it. Nothing is stored or sent anywhere.
 * Edit this file; apply_tools.py fingerprints and tags it.
 */
(function () {
  "use strict";
  var forms = document.querySelectorAll("form.rcm-tool[data-tool]");
  if (!forms.length) return;

  /* ---------- shared ---------- */
  var css = document.createElement("style");
  css.textContent =
    ".rcm-tool{border:1px solid var(--border,#e2e6eb);border-top:4px solid var(--teal,#1a6b72);border-radius:14px;background:var(--white,#fff);" +
    "padding:16px 18px 14px;margin:22px 0 8px;color:var(--text,#1e2a38);font-size:15px;line-height:1.5}" +
    ".rcm-tool *{box-sizing:border-box}" +
    ".rt-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 4px}" +
    ".rt-title{font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:17px;margin:0}" +
    ".rt-chip{font-size:11px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;border-radius:999px;padding:2px 9px;" +
    "background:var(--teal-light,#e1f5f0);color:var(--teal,#1a6b72)}" +
    ".rt-chip.rt-dosis{background:var(--purple-soft,#faf5ff);color:var(--purple,#6b21a8)}" +
    ".rt-sub{margin:0 0 12px;color:var(--text-muted,#4a5568);font-size:14px}" +
    ".rt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px 12px;margin:0 0 10px}" +
    ".rt-f label{display:block;font-size:13px;font-weight:600;color:var(--text-mid,#2c3a4a);margin:0 0 3px}" +
    ".rt-f input,.rt-f select{width:100%;font:inherit;font-size:16px;padding:7px 9px;border:1px solid var(--border,#e2e6eb);border-radius:8px;" +
    "background:var(--bg,#f9fafb);color:var(--text,#1e2a38)}" +
    ".rt-f input:focus,.rt-f select:focus{outline:2px solid var(--teal,#1a6b72);outline-offset:1px}" +
    ".rt-f .rt-hint{font-size:12px;color:var(--text-muted,#4a5568);margin-top:2px}" +
    ".rt-unit{display:inline-flex;margin-left:6px;vertical-align:1px}.rt-unit button{font:inherit;font-size:11px;padding:1px 7px;border:1px solid var(--border,#e2e6eb);" +
    "background:transparent;color:var(--text-muted,#4a5568);cursor:pointer}.rt-unit button:first-child{border-radius:6px 0 0 6px}.rt-unit button:last-child{border-radius:0 6px 6px 0;border-left:0}" +
    ".rt-unit button[aria-pressed=true]{background:var(--teal,#1a6b72);border-color:var(--teal,#1a6b72);color:var(--white,#fff)}" +
    ".rt-out{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:6px 0 8px}" +
    ".rt-m{border:1px solid var(--border,#e2e6eb);border-radius:10px;padding:9px 11px;background:var(--bg,#f9fafb)}" +
    ".rt-v{font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:22px;font-variant-numeric:tabular-nums;line-height:1.2}" +
    ".rt-v small{font-size:13px;font-weight:600;margin-left:3px;color:var(--text-muted,#4a5568)}" +
    ".rt-l{font-size:13px;color:var(--text-mid,#2c3a4a);font-weight:600}.rt-s{font-size:12.5px;color:var(--text-muted,#4a5568)}" +
    ".rt-ok .rt-v,.rt-ok .rt-s{color:var(--green,#166534)}.rt-warn .rt-v,.rt-warn .rt-s{color:var(--amber,#92400e)}.rt-bad .rt-v,.rt-bad .rt-s{color:var(--red,#b91c1c)}" +
    ".rt-msg{font-size:14px;margin:4px 0 8px;padding:8px 11px;border-radius:8px;background:var(--bg,#f9fafb);border:1px solid var(--border,#e2e6eb)}" +
    ".rt-msg.rt-bad{background:var(--red-soft,#fff0f0);color:var(--red,#b91c1c);border-color:transparent}" +
    ".rt-msg.rt-warn{background:var(--amber-soft,#fffbeb);color:var(--amber,#92400e);border-color:transparent}" +
    ".rt-msg.rt-ok{background:var(--green-soft,#f0fdf4);color:var(--green,#166534);border-color:transparent}" +
    ".rt-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:2px 0 8px}" +
    ".rt-btn{font:inherit;font-size:13.5px;font-weight:600;border:1px solid var(--teal,#1a6b72);color:var(--teal,#1a6b72);background:transparent;border-radius:999px;padding:4px 13px;cursor:pointer}" +
    ".rt-btn:hover{background:var(--teal,#1a6b72);color:var(--white,#fff)}" +
    ".rt-foot{font-size:12.5px;color:var(--text-muted,#4a5568);margin:8px 0 0}.rt-foot a{color:var(--teal,#1a6b72);font-weight:600}" +
    ".rt-foot details{margin:0 0 6px}.rt-foot summary{cursor:pointer;font-weight:600;color:var(--text-mid,#2c3a4a)}" +
    ".rt-foot code{font-size:12px}" +
    ".rt-drug{position:relative}.rt-list{position:absolute;z-index:30;left:0;right:0;top:100%;margin:2px 0 0;padding:4px 0;list-style:none;max-height:260px;overflow:auto;" +
    "background:var(--white,#fff);border:1px solid var(--border,#e2e6eb);border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.14)}" +
    ".rt-list li{padding:6px 11px;cursor:pointer;font-size:14.5px}.rt-list li small{color:var(--text-muted,#4a5568);margin-left:6px}" +
    ".rt-list li[aria-selected=true],.rt-list li:hover{background:var(--teal-light,#e1f5f0)}" +
    ".rcm-tool .rt-bands{list-style:none;margin:6px 0 4px !important;padding:0 !important;display:grid;gap:6px}.rcm-tool .rt-bands li{margin:0 !important}" +
    ".rt-bands li{display:grid;grid-template-columns:minmax(120px,210px) 1fr auto;gap:4px 12px;align-items:baseline;padding:7px 10px;border-radius:9px;" +
    "border:1px solid var(--border,#e2e6eb);font-size:14px;opacity:.72}" +
    ".rt-bands li.rt-cur{opacity:1;border:2px solid var(--teal,#1a6b72);background:var(--teal-light,#e1f5f0)}" +
    ".rt-bands .rt-bl{font-weight:600;color:var(--text-mid,#2c3a4a)}" +
    ".rt-tag{justify-self:start;align-self:center;font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;border-radius:999px;padding:1px 8px;white-space:nowrap}" +
    ".rt-t-none{background:var(--green-soft,#f0fdf4);color:var(--green,#166534)}.rt-t-adjust{background:var(--amber-soft,#fffbeb);color:var(--amber,#92400e)}" +
    ".rt-t-avoid{background:var(--red-soft,#fff0f0);color:var(--red,#b91c1c)}.rt-t-nodata{background:var(--bg,#f9fafb);color:var(--text-muted,#4a5568);border:1px solid var(--border,#e2e6eb)}" +
    ".rt-dn{font-family:Inter,system-ui,sans-serif;font-weight:700;font-size:16px;margin:8px 0 0}" +
    "@media (max-width:560px){.rt-bands li{grid-template-columns:1fr}.rcm-tool{padding:14px 13px 12px}}" +
    "@media print{.rcm-tool{break-inside:avoid}.rt-btn,.rt-unit{display:none}}";
  document.head.appendChild(css);

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function num(input) {
    if (!input) return NaN;
    var v = String(input.value).trim().replace(",", ".");
    return v === "" ? NaN : parseFloat(v);
  }
  function fmt(x, d) { return (Math.round(x * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d); }
  var uid = 0;
  function field(id, label, attrs, hint) {
    var a = "";
    for (var k in attrs) a += " " + k + '="' + esc(attrs[k]) + '"';
    return '<div class="rt-f"><label for="' + id + '">' + label + "</label><input id=\"" + id + '" inputmode="decimal" autocomplete="off"' + a + ">" +
      (hint ? '<div class="rt-hint">' + hint + "</div>" : "") + "</div>";
  }
  function metric(cls, value, unit, label, sub) {
    return '<div class="rt-m ' + (cls || "") + '"><div class="rt-v">' + value + (unit ? "<small>" + unit + "</small>" : "") + "</div>" +
      '<div class="rt-l">' + label + "</div>" + (sub ? '<div class="rt-s">' + sub + "</div>" : "") + "</div>";
  }
  function head(form, title, chip, sub, intro) {
    return '<div class="rt-head"><h3 class="rt-title">' + title + '</h3><span class="rt-chip' + (chip === "Dosis" ? " rt-dosis" : "") + '">' +
      (chip === "Dosis" ? "Dosis lookup" : "Calculo") + "</span></div>" +
      '<p class="rt-sub">' + (intro ? esc(intro) + " " : "") + sub + "</p>";
  }
  var SAFETY = "A learning aid. Check the order and the full label, and follow your unit protocol; always ask the attending nephrologist.";

  /* ---------- Kt/V, URR, UFR ---------- */
  function ktv(form, o) {
    var p = "rt" + (++uid) + "-";
    form.innerHTML = head(form, o.title || "Try it: spKt/V and URR", "Calculo",
      "Enter one session's paired urea results. Use the same unit for both (BUN mg/dL or urea mmol/L).", o.intro) +
      '<div class="rt-grid">' +
      field(p + "pre", "Pre-dialysis BUN", { placeholder: "e.g. 70" }) +
      field(p + "post", "Post-dialysis BUN", { placeholder: "e.g. 22" }) +
      field(p + "t", "Session length (minutes)", { placeholder: "e.g. 240" }) +
      field(p + "uf", "Fluid removed (L)", { placeholder: "e.g. 2.5" }) +
      field(p + "w", "Post-dialysis weight (kg)", { placeholder: "e.g. 58" }) +
      "</div>" +
      '<div class="rt-row"><button type="button" class="rt-btn" data-x>Try an example</button><button type="button" class="rt-btn" data-c>Clear</button></div>' +
      '<div class="rt-res" aria-live="polite"></div>' +
      '<div class="rt-foot"><details><summary>How it is calculated</summary>' +
      "<p>spKt/V (Daugirdas, second generation) = −ln(R − 0.008 × t) + (4 − 3.5 × R) × UF ÷ W, where R = post ÷ pre urea, t = session hours, " +
      "UF = liters removed and W = post-dialysis weight. URR = (pre − post) ÷ pre × 100. Ultrafiltration rate = UF × 1000 ÷ hours ÷ weight. " +
      "Targets as in the Calculo calculator: spKt/V 1.4 per thrice-weekly session, with a delivered minimum of 1.2 (KDOQI 2015); URR 65% or more. " +
      "A single result is read with the sampling technique, the session's minutes and the trend.</p></details>" +
      'Full calculator: <a href="/guides/calc-dialysis-adequacy-ktv">Dialysis adequacy (Kt/V and URR) in Calculo</a>. ' + SAFETY + "</div>";
    var $ = function (s) { return form.querySelector("#" + p + s); }, res = form.querySelector(".rt-res");
    function run() {
      var pre = num($("pre")), post = num($("post")), min = num($("t")), uf = num($("uf")), w = num($("w"));
      if ([pre, post, min, w].some(isNaN)) { res.innerHTML = ""; return; }
      if (isNaN(uf)) uf = 0;
      if (pre <= 0 || post <= 0 || min <= 0 || w <= 0 || uf < 0) { res.innerHTML = '<p class="rt-msg rt-warn">Check the numbers: every value must be above zero.</p>'; return; }
      if (post >= pre) { res.innerHTML = '<p class="rt-msg rt-bad">The post-dialysis value must be lower than the pre-dialysis value. Check that the two samples were not swapped or mislabeled.</p>'; return; }
      var R = post / pre, t = min / 60, inner = R - 0.008 * t;
      if (inner <= 0) { res.innerHTML = '<p class="rt-msg rt-warn">These values fall outside the range the formula was built for. Recheck the session length and results.</p>'; return; }
      var k = -Math.log(inner) + (4 - 3.5 * R) * (uf / w), urr = (pre - post) / pre * 100, ufr = uf * 1000 / t / w;
      var kr = Math.round(k * 100) / 100, ur = Math.round(urr * 10) / 10, fr = Math.round(ufr * 10) / 10;
      var kc = kr >= 1.4 ? "rt-ok" : kr >= 1.2 ? "rt-warn" : "rt-bad";
      var ks = kr >= 1.4 ? "At or above the 1.4 target" : kr >= 1.2 ? "Above the 1.2 minimum, below the 1.4 target" : "Below the 1.2 delivered minimum";
      res.innerHTML = '<div class="rt-out">' +
        metric(kc, fmt(kr, 2), "", "spKt/V", ks) +
        metric(ur >= 65 ? "rt-ok" : "rt-warn", fmt(ur, 1), "%", "URR", ur >= 65 ? "At or above 65%" : "Below 65%") +
        metric(fr < 10 ? "rt-ok" : fr < 13 ? "rt-warn" : "rt-bad", fmt(fr, 1), "mL/kg/h", "Ultrafiltration rate", fr < 10 ? "Under 10" : fr < 13 ? "10 to 13: watch closely" : "13 or more: high") +
        "</div>" + (kr < 1.2 ? '<p class="rt-msg rt-bad">Before calling the dose low, check the sampling: post-dialysis blood drawn the right way and time, the session given in full, and the access working without recirculation.</p>' : "");
    }
    form.addEventListener("input", run);
    form.querySelector("[data-x]").addEventListener("click", function () {
      var ex = o.example || [70, 22, 240, 2.5, 58];
      ["pre", "post", "t", "uf", "w"].forEach(function (s, i) { $(s).value = ex[i]; });
      run();
    });
    form.querySelector("[data-c]").addEventListener("click", function () { ["pre", "post", "t", "uf", "w"].forEach(function (s) { $(s).value = ""; }); run(); });
  }

  /* ---------- hyponatremia correction ---------- */
  function sodium(form, o) {
    var p = "rt" + (++uid) + "-", L = o.limits || { first24: 10, after: 8, source: "" };
    form.innerHTML = head(form, o.title || "Try it: planning a safe sodium rise", "Calculo",
      "Estimates only. They assume no urine and no other losses, so measure sodium again and re-plan.", o.intro) +
      '<div class="rt-grid">' +
      field(p + "na", "Serum sodium (mmol/L)", { placeholder: "e.g. 109" }) +
      field(p + "w", "Weight (kg)", { placeholder: "e.g. 60" }) +
      '<div class="rt-f"><label for="' + p + 'f">Body water fraction</label><select id="' + p + 'f">' +
      '<option value="0.6">Adult male (0.6)</option><option value="0.5">Adult female (0.5)</option>' +
      '<option value="0.5">Older male (0.5)</option><option value="0.45">Older female (0.45)</option></select></div>' +
      field(p + "r", "Planned rise in the first 24 h (mmol/L)", { placeholder: "e.g. 6" }) +
      "</div>" +
      '<div class="rt-row"><button type="button" class="rt-btn" data-x>Try an example</button><button type="button" class="rt-btn" data-c>Clear</button></div>' +
      '<div class="rt-res" aria-live="polite"></div>' +
      '<div class="rt-foot"><details><summary>How it is calculated</summary>' +
      "<p>Total body water = weight × fraction. Sodium deficit for the planned rise = total body water × planned rise. Change in serum sodium from " +
      "1 L of a fluid (Adrogué–Madias) = (fluid sodium − serum sodium) ÷ (total body water + 1); for a smaller volume V in liters, " +
      "(fluid sodium − serum sodium) × V ÷ (total body water + V). 3% saline carries 513 mmol/L of sodium. The formulas ignore urine and other " +
      "losses; a water diuresis can raise sodium faster than predicted.</p></details>" +
      "Limits used here: +" + L.first24 + " mmol/L in the first 24 h, +" + L.after + " mmol/L in each 24 h after" + (L.source ? " (" + esc(L.source) + ")" : "") + ". " +
      'Full calculator: <a href="/guides/calc-sodium-correction-rate">Sodium correction rate in Calculo</a>. ' + SAFETY + "</div>";
    var $ = function (s) { return form.querySelector("#" + p + s); }, res = form.querySelector(".rt-res");
    function run() {
      var na = num($("na")), w = num($("w")), f = parseFloat($("f").value), rise = num($("r"));
      if (isNaN(na) || isNaN(w)) { res.innerHTML = ""; return; }
      if (na < 90 || na > 160 || w <= 0 || w > 250) { res.innerHTML = '<p class="rt-msg rt-warn">Check the numbers (sodium 90 to 160 mmol/L, weight in kg).</p>'; return; }
      var tbw = w * f, bolus = (513 - na) * 0.15 / (tbw + 0.15), perL = (513 - na) / (tbw + 1);
      var out = metric("", fmt(tbw, 1), "L", "Total body water", "weight × " + f) +
        metric("", "+" + fmt(bolus, 1), "mmol/L", "One 150 mL 3% bolus", "predicted rise");
      var msg = "";
      if (!isNaN(rise) && rise > 0) {
        var vol = rise / perL * 1000, over = rise > L.first24;
        out += metric("", fmt(tbw * rise, 0), "mmol", "Sodium deficit", "for +" + fmt(rise, 1) + " mmol/L") +
          metric(over ? "rt-bad" : "", fmt(vol, 0), "mL", "3% saline for the planned rise", "if no other gains or losses");
        msg = over ? '<p class="rt-msg rt-bad">The planned rise of ' + fmt(rise, 1) + " mmol/L is above the +" + L.first24 + " mmol/L limit for the first 24 h. Plan a smaller rise.</p>"
          : '<p class="rt-msg rt-ok">Planned rise within the +' + L.first24 + " mmol/L first-day limit. Ceiling at 24 h: " + fmt(na + L.first24, 0) + " mmol/L; at 48 h: " + fmt(na + L.first24 + L.after, 0) + " mmol/L.</p>";
      }
      res.innerHTML = '<div class="rt-out">' + out + "</div>" + msg;
    }
    form.addEventListener("input", run);
    form.addEventListener("change", run);
    form.querySelector("[data-x]").addEventListener("click", function () {
      var ex = o.example || [109, 60, "0.5", 6];
      $("na").value = ex[0]; $("w").value = ex[1]; $("f").value = ex[2]; $("r").value = ex[3]; run();
    });
    form.querySelector("[data-c]").addEventListener("click", function () { ["na", "w", "r"].forEach(function (s) { $(s).value = ""; }); run(); });
  }

  /* ---------- kidney function + Dosis kidney dosing ---------- */
  var BANDS = { ge60: "≥ 60", "30_59": "30 to 59", "15_29": "15 to 29", lt15: "< 15" };
  var TAG = { none: "No change", adjust: "Adjust", avoid: "Avoid", nodata: "Not studied" };
  function bandFor(v) { return v >= 60 ? "ge60" : v >= 30 ? "30_59" : v >= 15 ? "15_29" : "lt15"; }
  function dose(form, o) {
    var D = window.RCM_KDOSE;
    if (!D) { return; }   // fallback link stays
    var p = "rt" + (++uid) + "-", names = [];
    Object.keys(D.d).forEach(function (s) {
      var r = D.d[s];
      names.push({ s: s, t: r.n, n: r.n.toLowerCase(), kind: "" });
      (r.b || []).forEach(function (b) { names.push({ s: s, t: b, n: b.toLowerCase(), kind: r.n }); });
    });
    form.innerHTML = head(form, o.title || "Try it: kidney function and drug dosing", "Dosis",
      "Estimate kidney function, then look up a medicine's reviewed kidney dosing from the Dosis Drug Index.", o.intro) +
      '<div class="rt-grid">' +
      '<div class="rt-f"><label for="' + p + 'm">Kidney replacement</label><select id="' + p + 'm">' +
      '<option value="">None (not on dialysis)</option><option value="hd">Hemodialysis</option><option value="pd">Peritoneal dialysis</option>' +
      '<option value="crrt">CRRT</option></select></div>' +
      field(p + "age", "Age (years)", { placeholder: "e.g. 72" }) +
      '<div class="rt-f"><label for="' + p + 'sex">Sex</label><select id="' + p + 'sex"><option value="">Choose</option><option value="f">Female</option><option value="m">Male</option></select></div>' +
      field(p + "w", "Weight (kg)", { placeholder: "e.g. 52" }) +
      '<div class="rt-f"><label for="' + p + 'cr">Creatinine <span class="rt-unit" role="group" aria-label="Creatinine unit"><button type="button" aria-pressed="true" data-u="mg">mg/dL</button>' +
      '<button type="button" aria-pressed="false" data-u="umol">µmol/L</button></span></label><input id="' + p + 'cr" inputmode="decimal" autocomplete="off" placeholder="e.g. 1.9"></div>' +
      "</div>" +
      '<div class="rt-grid">' +
      field(p + "crcl", "CrCl (mL/min)", { placeholder: "from the fields above, or type it" }, "Cockcroft–Gault, actual weight") +
      field(p + "egfr", "eGFR (mL/min/1.73 m²)", { placeholder: "from the fields above, or type it" }, "CKD-EPI 2021") +
      '<div class="rt-f rt-drug"><label for="' + p + 'q">Medicine (generic or Philippine brand)</label><input id="' + p + 'q" autocomplete="off" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="' + p + 'list" placeholder="e.g. acyclovir">' +
      '<ul class="rt-list" id="' + p + 'list" role="listbox" hidden></ul></div>' +
      "</div>" +
      '<div class="rt-row"><button type="button" class="rt-btn" data-x>Try an example</button><button type="button" class="rt-btn" data-c>Clear</button></div>' +
      '<div class="rt-res" aria-live="polite"></div>' +
      '<div class="rt-foot"><details><summary>Where these numbers come from</summary>' +
      "<p>CrCl = (140 − age) × weight × (0.85 if female) ÷ (72 × creatinine in mg/dL), with actual body weight; µmol/L is divided by 88.4. " +
      "eGFR = CKD-EPI 2021 (race-free). Each band, and the label's own measure (CrCl or eGFR), is quoted from the medicine's Dosis page, where " +
      "kidney dosing appears only after review (" + Object.keys(D.d).length + " medicines so far). A medicine missing here is not necessarily safe in kidney disease.</p></details>" +
      'Full tools: <a href="/guides/calc-cockcroft-gault">Cockcroft–Gault in Calculo</a> (ideal or adjusted weight) · <a href="/drugs/">Dosis Drug Index</a>. ' + SAFETY + "</div>";
    var $ = function (s) { return form.querySelector("#" + p + s); }, res = form.querySelector(".rt-res"), list = $("list");
    var unit = "mg", chosen = null, typedCrcl = false, typedEgfr = false, act = -1, shown = [];

    function estimate() {
      var age = num($("age")), w = num($("w")), cr = num($("cr")), sex = $("sex").value;
      if (isNaN(age) || isNaN(cr) || !sex || age < 18 || cr <= 0) return;
      var scr = unit === "umol" ? cr / 88.4 : cr;
      if (!typedCrcl && !isNaN(w) && w > 0) $("crcl").value = Math.round((140 - age) * w * (sex === "f" ? 0.85 : 1) / (72 * scr));
      if (!typedEgfr) {
        var k = sex === "f" ? 0.7 : 0.9, a = sex === "f" ? -0.241 : -0.302, r = scr / k;
        $("egfr").value = Math.round(142 * Math.pow(Math.min(r, 1), a) * Math.pow(Math.max(r, 1), -1.2) * Math.pow(0.9938, age) * (sex === "f" ? 1.012 : 1));
      }
    }
    function render() {
      if (!chosen) { res.innerHTML = ""; return; }
      var r = D.d[chosen], k = r.k, mod = $("m").value, crcl = num($("crcl")), egfr = num($("egfr"));
      var usesCrcl = k.b.some(function (b) { return /CrCl/.test(b[1]); }), meas = usesCrcl ? "CrCl" : "eGFR", val = usesCrcl ? crcl : egfr;
      var cur = !mod && !isNaN(val) ? bandFor(val) : "";
      var rows = k.b.filter(function (b) { return b[3] !== "hide"; }).map(function (b) {
        return '<li class="' + (b[0] === cur ? "rt-cur" : "") + '"><span class="rt-bl">' + esc(b[1]) + '</span><span class="rt-bt">' + esc(b[2]) + "</span>" +
          '<span class="rt-tag rt-t-' + b[3] + '">' + (TAG[b[3]] || "") + "</span></li>";
      });
      [["hd", "Hemodialysis"], ["pd", "Peritoneal dialysis"], ["crrt", "CRRT"]].forEach(function (m) {
        var x = k[m[0]];
        if (x && x[1] !== "hide") rows.push('<li class="' + (mod === m[0] ? "rt-cur" : "") + '"><span class="rt-bl">' + m[1] + '</span><span class="rt-bt">' + esc(x[0]) + "</span>" +
          '<span class="rt-tag rt-t-' + x[1] + '">' + (TAG[x[1]] || "") + "</span></li>");
      });
      var note;
      if (mod) note = "Highlighted: the " + { hd: "hemodialysis", pd: "peritoneal dialysis", crrt: "CRRT" }[mod] + " row.";
      else if (isNaN(val)) note = "This label's bands use <strong>" + meas + "</strong>. Enter " + (usesCrcl ? "a CrCl (or age, sex, weight and creatinine)" : "an eGFR (or age, sex and creatinine)") + " to highlight the band.";
      else note = "This label's bands use <strong>" + meas + "</strong>; highlighted for " + meas + " " + Math.round(val) + "." +
        (usesCrcl && !isNaN(egfr) && Math.abs(egfr - crcl) >= 10 && bandFor(egfr) !== bandFor(crcl) ? " The eGFR would fall in a different band: dose by the measure the label uses." : "");
      res.innerHTML = '<p class="rt-dn">' + esc(r.n) + "</p>" + '<p class="rt-sub" style="margin:2px 0 4px">' + note + "</p>" +
        '<ul class="rt-bands">' + rows.join("") + "</ul>" +
        '<p class="rt-foot" style="margin-top:4px">Short form of the reviewed kidney dosing. <a href="/drugs/' + chosen + '">Open ' + esc(r.n) + " in Dosis</a> for the full label text, dosage forms and Philippine brands.</p>";
    }
    function closeList() { list.hidden = true; $("q").setAttribute("aria-expanded", "false"); act = -1; }
    function pick(i) {
      var h = shown[i]; if (!h) return;
      chosen = h.s; $("q").value = D.d[h.s].n; closeList(); render();
    }
    function search() {
      var q = $("q").value.trim().toLowerCase();
      chosen = null;
      if (q.length < 2) { closeList(); render(); return; }
      var seen = {}, starts = [], has = [];
      names.forEach(function (h) {
        var i = h.n.indexOf(q);
        if (i < 0) return;
        var key = h.s + "|" + (h.kind ? h.t : "");
        if (seen[key]) return; seen[key] = 1;
        (i === 0 ? starts : has).push(h);
      });
      var gen = function (a, b) { return (a.kind ? 1 : 0) - (b.kind ? 1 : 0) || a.t.length - b.t.length; };
      shown = starts.sort(gen).concat(has.sort(gen)).slice(0, 12);
      if (!shown.length) {
        list.innerHTML = '<li aria-disabled="true">No reviewed kidney dosing for “' + esc($("q").value.trim()) + '” yet. <a href="/drugs/">Search the Dosis Drug Index</a></li>';
      } else {
        list.innerHTML = shown.map(function (h, i) {
          return '<li role="option" id="' + p + "o" + i + '" data-i="' + i + '">' + esc(h.t) + (h.kind ? "<small>" + esc(h.kind) + "</small>" : "") + "</li>";
        }).join("");
      }
      list.hidden = false; $("q").setAttribute("aria-expanded", "true"); act = -1;
      var exact = shown.filter(function (h) { return h.n === q; });
      if (exact.length) { chosen = exact[0].s; render(); }
    }
    $("q").addEventListener("input", search);
    $("q").addEventListener("keydown", function (e) {
      if (list.hidden || !shown.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        act = (act + (e.key === "ArrowDown" ? 1 : -1) + shown.length) % shown.length;
        Array.prototype.forEach.call(list.children, function (li, i) { li.setAttribute("aria-selected", i === act ? "true" : "false"); });
        $("q").setAttribute("aria-activedescendant", p + "o" + act);
      } else if (e.key === "Enter") { e.preventDefault(); pick(act < 0 ? 0 : act); }
      else if (e.key === "Escape") closeList();
    });
    list.addEventListener("mousedown", function (e) { var li = e.target.closest("li[data-i]"); if (li) { e.preventDefault(); pick(+li.getAttribute("data-i")); } });
    document.addEventListener("click", function (e) { if (!form.contains(e.target)) closeList(); });
    $("crcl").addEventListener("input", function () { typedCrcl = $("crcl").value !== ""; render(); });
    $("egfr").addEventListener("input", function () { typedEgfr = $("egfr").value !== ""; render(); });
    ["age", "w", "cr"].forEach(function (s) { $(s).addEventListener("input", function () { estimate(); render(); }); });
    ["sex", "m"].forEach(function (s) { $(s).addEventListener("change", function () { estimate(); render(); }); });
    Array.prototype.forEach.call(form.querySelectorAll(".rt-unit button"), function (b) {
      b.addEventListener("click", function () {
        unit = b.getAttribute("data-u");
        Array.prototype.forEach.call(form.querySelectorAll(".rt-unit button"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        $("cr").placeholder = unit === "mg" ? "e.g. 1.9" : "e.g. 168";
        estimate(); render();
      });
    });
    form.querySelector("[data-x]").addEventListener("click", function () {
      var ex = o.example || { age: 72, sex: "f", w: 52, cr: 1.9, drug: "acyclovir" };
      typedCrcl = typedEgfr = false; $("crcl").value = ""; $("egfr").value = "";
      $("m").value = ex.m || ""; $("age").value = ex.age; $("sex").value = ex.sex; $("w").value = ex.w; $("cr").value = ex.cr;
      estimate();
      if (D.d[ex.drug]) { chosen = ex.drug; $("q").value = D.d[ex.drug].n; }
      render();
    });
    form.querySelector("[data-c]").addEventListener("click", function () {
      ["age", "w", "cr", "crcl", "egfr", "q"].forEach(function (s) { $(s).value = ""; });
      $("sex").value = ""; $("m").value = ""; typedCrcl = typedEgfr = false; chosen = null; closeList(); render();
    });
  }

  var TOOLS = { ktv: ktv, sodium: sodium, dose: dose };
  Array.prototype.forEach.call(forms, function (f) {
    var o = {};
    try { o = JSON.parse(f.getAttribute("data-opts") || "{}"); } catch (e) {}
    f.addEventListener("submit", function (e) { e.preventDefault(); });
    if (TOOLS[f.getAttribute("data-tool")]) TOOLS[f.getAttribute("data-tool")](f, o);
  });
})();
