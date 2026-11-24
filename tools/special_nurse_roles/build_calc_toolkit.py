#!/usr/bin/env python3
"""Build guides/calc-dialysis-nurse-portfolio-toolkit.html (Dialysis Nurse Portfolio Toolkit).

Four tools for hemodialysis nurses who carry a special portfolio (Renal Care Academy, Special Dialysis Nurse Roles):
(1) honest rate: a proportion with exclusions shown, a 95% Wilson interval and a small-sample warning;
(2) infection rate per 100 patient-months, stratified by fistula, graft and catheter, with denominator checks;
(3) treatment-delivery check: urea reduction ratio with a sample-validity checklist, delivered vs prescribed minutes,
    and ultrafiltration rate in mL/kg/h;
(4) hemoglobin trend: change per week between two dated results, with the product-label rapid-rise flag; never a dose.
Chrome is copied from an existing calculator, as tools/dialysis_support_staff/build_calc_toolkit.py does.
Re-running carries over the page's article:published_time. Run via generate_special_dialysis_nurse_roles.py --calc.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "guides"
SRC = GUIDES / "calc-allograft-egfr-trend.html"
OUT = GUIDES / "calc-dialysis-nurse-portfolio-toolkit.html"
SLUG = "calc-dialysis-nurse-portfolio-toolkit"
URL = f"https://renalcarematters.com/guides/{SLUG}"
TITLE = "Dialysis Nurse Portfolio Toolkit: Honest Rates, Infection Rates, Treatment Delivery and Hemoglobin Trend"
DESC = ("Four tools for hemodialysis nurses who carry a unit portfolio: an honest audit rate with exclusions and a 95% range, "
        "bloodstream infection rates per 100 patient-months by access type, a treatment-delivery check (URR with sample validity, "
        "delivered minutes, ultrafiltration rate), and the pace of hemoglobin change. Educational; never suggests a dose.")
KEYWORDS = ("dialysis audit rate calculator, hand hygiene compliance confidence interval, dialysis bloodstream infection rate per 100 patient-months, "
            "urea reduction ratio calculator, delivered dialysis time, ultrafiltration rate mL/kg/h, hemoglobin change per week")

HERO = """<section class="hero">
<div class="container">
<div class="hero-tag">Dialysis Nursing &middot; Portfolio &middot; Toolkit</div>
<h1>Dialysis Nurse Portfolio <em>Toolkit</em></h1>
<p class="hero-sub">Four tools for the nurse who looks across patients and across weeks: turn audit counts into honest percentages, calculate infection rates with the right denominator, check whether a treatment was delivered as prescribed, and see how fast hemoglobin is changing. Built for the Renal Care Academy Special Dialysis Nurse Roles subtrack. It never suggests a dose or a prescription change.</p>
<div class="hero-meta">
</div>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;&middot;&nbsp; <a href="../academy/special-dialysis-nurse-roles.html" class="hero-xlink">Special Dialysis Nurse Roles →</a></p>
</div>
</section>"""

NAV = """<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#instructions">Instructions</a>
<a class="nav-pill" href="#when">When to Use</a>
<a class="nav-pill" href="#rate">Honest Rate</a>
<a class="nav-pill" href="#infection">Infection Rate</a>
<a class="nav-pill" href="#delivery">Treatment Delivery</a>
<a class="nav-pill" href="#hb">Hemoglobin Trend</a>
<a class="nav-pill" href="#evidence">Evidence</a>
</div>
</nav>"""

def field(id_, label, ph, hint="", extra='min="0" step="any"', typ="number", full=False):
    st = ' style="grid-column:1/-1;"' if full else ""
    h = f'\n      <div class="field-hint">{hint}</div>' if hint else ""
    return f"""    <div class="calc-field"{st}>
      <label for="{id_}">{label}</label>
      <input type="{typ}" id="{id_}" placeholder="{ph}" {extra}>{h}
    </div>"""

def result(prefix, cards):
    cs = "\n".join(f'      <div class="calc-metric-card"><div class="cmv" id="{prefix}-{k}">—</div><div class="cml">{l}</div><div class="cmt" id="{prefix}-{k}t">{t}</div></div>' for k, l, t in cards)
    return f"""  <div class="calc-result-box" id="{prefix}-result" role="status" aria-live="polite">
    <div class="calc-metrics-row">
{cs}
    </div>
    <div class="calc-verdict-text" id="{prefix}-verdict"></div>
    <div class="calc-action-text" id="{prefix}-action"></div>
  </div>"""

MAIN = f"""<main class="container">

<div class="mdc-instructions" id="instructions"><span class="mdc-instr-label">Instructions</span>
<ol style="margin:0 0 0 1.2em;line-height:2;">
  <li><strong>Honest rate:</strong> enter how many cases were eligible, how many you excluded and why, and how many met the standard. Use it for hand hygiene, referral closure, teach-back, records accuracy or corrective actions.</li>
  <li><strong>Infection rate:</strong> enter bloodstream infections and patient-months for each access type separately. One patient treated for a whole month is one patient-month.</li>
  <li><strong>Treatment delivery:</strong> enter pre- and post-dialysis urea from a valid sample pair, the prescribed and delivered minutes, and the fluid removed with the post-dialysis weight.</li>
  <li><strong>Hemoglobin trend:</strong> enter two results with their dates.</li>
  <li>Nothing you enter is stored or sent. Use fictional or de-identified numbers for practice.</li>
</ol>
</div>

<details class="mdc-acc" id="when">
<summary>When to Use</summary>
<div class="mdc-acc-body">
<p>Use these tools for portfolio work: monthly audits, the quality meeting, an infection review, an adequacy review, or an anemia trend that needs to reach the prescriber. They make the arithmetic and the denominators visible so that the unit can act on honest numbers.</p>
<div class="alert alert-amber">
<div class="alert-icon">⚠️</div>
<div class="alert-body">
<h4>When NOT to rely on it</h4>
<p>This toolkit never recommends a dose, a prescription change, a target weight or a treatment time. A hemoglobin fall with bleeding symptoms, an access with no thrill, or a patient who is unwell needs the physician now, not a calculation. Urea reduction ratio is a surrogate measure; Kt/V by your unit&rsquo;s method and the patient&rsquo;s symptoms, fluid status and goals matter as much.</p>
</div>
</div>
</div>
</details>

<section class="section" id="rate">
<div class="section-tag">Tool 1</div>
<h2>Honest rate</h2>
<p>A percentage is only as honest as its denominator. Record exclusions openly; never drop the hard cases to make the number look better.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("rt-elig", "Eligible cases (the full denominator before exclusions)", "e.g. 20", extra='min="1" step="1"')}
{field("rt-excl", "Excluded, with a written reason (optional)", "e.g. 0", extra='min="0" step="1"')}
{field("rt-num", "Met the standard (numerator)", "e.g. 8", extra='min="0" step="1"')}
{field("rt-goal", "Unit goal (percent, optional)", "e.g. 90")}
  </div>
  <button class="calc-btn" type="button" id="rt-btn">Calculate</button>
{result("rt", [("pct", "Result", "percent of the denominator used"), ("ci", "95% range", "plausible true value"), ("gap", "To reach goal", "more cases needed")])}
  <p class="calc-disclaimer">⚕ The 95% range (Wilson score interval) shows how much a small count can bounce by chance. Show results month by month on a run chart before calling a change real.</p>
</div>
</section>

<section class="section" id="infection">
<div class="section-tag">Tool 2</div>
<h2>Bloodstream infection rate by access type</h2>
<p>Rates are per 100 patient-months, calculated separately for each access type, because catheters carry a much higher risk than fistulas. Mixing them hides where the problem is.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("in-fe", "Fistula: bloodstream infections", "e.g. 0", extra='min="0" step="1"')}
{field("in-fm", "Fistula: patient-months", "e.g. 180", extra='min="0" step="any"')}
{field("in-ge", "Graft: bloodstream infections", "e.g. 0", extra='min="0" step="1"')}
{field("in-gm", "Graft: patient-months", "e.g. 12", extra='min="0" step="any"')}
{field("in-ce", "Catheter: bloodstream infections", "e.g. 3", extra='min="0" step="1"')}
{field("in-cm", "Catheter: patient-months", "e.g. 54", extra='min="0" step="any"')}
  </div>
  <button class="calc-btn" type="button" id="in-btn">Calculate</button>
{result("in", [("f", "Fistula", "per 100 patient-months"), ("g", "Graft", "per 100 patient-months"), ("c", "Catheter", "per 100 patient-months"), ("all", "All access", "per 100 patient-months")])}
  <p class="calc-disclaimer">⚕ Use one written definition of a bloodstream infection and count every positive blood culture event the same way each month. With small numbers, one infection moves the rate a lot; look at the events themselves, not only the rate.</p>
</div>
</section>

<section class="section" id="delivery">
<div class="section-tag">Tool 3</div>
<h2>Treatment-delivery check</h2>
<p>Was the treatment delivered as prescribed? Validity first, then the numbers.</p>
<div class="calc-wrap">
  <fieldset class="calc-field" style="grid-column:1/-1;border:1px solid var(--border);border-radius:10px;padding:10px 14px;">
    <legend style="font-weight:700;padding:0 6px;">Sample validity (tick each that is true)</legend>
    <label style="display:block;"><input type="checkbox" id="dv-c1"> Pre-dialysis sample drawn before any saline or heparin entered the line</label>
    <label style="display:block;"><input type="checkbox" id="dv-c2"> Post-dialysis sample drawn by the unit's method (slow-flow or stop-pump) at the time the protocol states</label>
    <label style="display:block;"><input type="checkbox" id="dv-c3"> Both tubes labeled with the right patient, date and pre or post</label>
    <label style="display:block;"><input type="checkbox" id="dv-c4"> Treatment ran without a long interruption, or the interruption is recorded</label>
  </fieldset>
  <div class="calc-grid">
{field("dv-pre", "Pre-dialysis urea or BUN (any unit, same for both)", "e.g. 150", extra='min="0" step="any"')}
{field("dv-post", "Post-dialysis urea or BUN (same unit)", "e.g. 50", extra='min="0" step="any"')}
{field("dv-rx", "Prescribed treatment minutes", "e.g. 240", extra='min="0" step="1"')}
{field("dv-del", "Delivered treatment minutes", "e.g. 210", extra='min="0" step="1"')}
{field("dv-uf", "Fluid removed (liters)", "e.g. 3.2", extra='min="0" step="any"')}
{field("dv-wt", "Post-dialysis weight (kg)", "e.g. 58", extra='min="1" step="any"')}
  </div>
  <button class="calc-btn" type="button" id="dv-btn">Check</button>
{result("dv", [("urr", "Urea reduction ratio", "percent"), ("time", "Time delivered", "percent of prescribed"), ("ufr", "Ultrafiltration rate", "mL/kg/h over delivered time")])}
  <p class="calc-disclaimer">⚕ For thrice-weekly treatment, the 2015 KDOQI guideline targets a single-pool Kt/V of 1.4 with a delivered minimum of 1.2; a urea reduction ratio of 65% corresponds roughly to a Kt/V of 1.2. A higher dose did not lower mortality in the HEMO trial, so adequacy is a floor, not a dial. Ultrafiltration rates above 13 mL/kg/h were associated with higher mortality in an observational analysis. The physician decides any change.</p>
</div>
</section>

<section class="section" id="hb">
<div class="section-tag">Tool 4</div>
<h2>Hemoglobin trend</h2>
<p>How fast is hemoglobin moving? Speed matters as much as the level.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("hb-1", "Earlier hemoglobin (g/dL)", "e.g. 10.2", extra='min="0" step="any"')}
{field("hb-d1", "Date of earlier result", "", typ="date", extra='')}
{field("hb-2", "Latest hemoglobin (g/dL)", "e.g. 8.1", extra='min="0" step="any"')}
{field("hb-d2", "Date of latest result", "", typ="date", extra='')}
  </div>
  <fieldset class="calc-field" style="grid-column:1/-1;border:1px solid var(--border);border-radius:10px;padding:10px 14px;">
    <legend style="font-weight:700;padding:0 6px;">Any of these now? (tick all that apply)</legend>
    <label style="display:block;"><input type="checkbox" id="hb-s1"> Black or bloody stools, vomiting blood, or other bleeding</label>
    <label style="display:block;"><input type="checkbox" id="hb-s2"> Dizziness, chest pain, breathlessness or fainting</label>
    <label style="display:block;"><input type="checkbox" id="hb-s3"> Fever or active infection</label>
  </fieldset>
  <button class="calc-btn" type="button" id="hb-btn">Calculate</button>
{result("hb", [("chg", "Change", "g/dL"), ("wk", "Per week", "g/dL per week"), ("days", "Interval", "days")])}
  <p class="calc-disclaimer">⚕ This tool only describes the trend. Epoetin product labels advise prescriber review when hemoglobin rises by more than 1 g/dL in any 2-week period. A falling hemoglobin with bleeding symptoms is a clinical problem for the physician today, not a step on a dosing protocol.</p>
</div>
</section>

<details class="mdc-acc" id="evidence">
<summary>Evidence &amp; References</summary>
<div class="mdc-acc-body">
<h3 class="mdc-sub">Formula &amp; Equations</h3>
<table class="lab-table">
<thead><tr><th>Quantity</th><th>Equation or rule</th></tr></thead>
<tbody>
<tr><td>Honest rate</td><td>Numerator ÷ (eligible − excluded) × 100, with a 95% Wilson score interval; exclusions shown beside the result</td></tr>
<tr><td>Infection rate</td><td>Bloodstream infections ÷ patient-months × 100, per access type and overall</td></tr>
<tr><td>Urea reduction ratio</td><td>(Pre − post) ÷ pre × 100</td></tr>
<tr><td>Time delivered</td><td>Delivered minutes ÷ prescribed minutes × 100</td></tr>
<tr><td>Ultrafiltration rate</td><td>Fluid removed (mL) ÷ post-dialysis weight (kg) ÷ delivered hours</td></tr>
<tr><td>Hemoglobin pace</td><td>(Latest − earlier) ÷ days between × 7</td></tr>
</tbody>
</table>
<h3 class="mdc-sub">Evidence</h3>
<p>Run charts display a measure in time order and use simple run rules to separate signal from noise. In a CDC collaborative of 17 outpatient hemodialysis facilities, audits with feedback, catheter-care training and chlorhexidine exit-site care were followed by modeled falls of 32% in bloodstream infections and 54% in access-related bloodstream infections; the project had no control group. The KDOQI 2015 adequacy guideline sets a target single-pool Kt/V of 1.4 for thrice-weekly hemodialysis with a minimum delivered dose of 1.2. In the HEMO trial, a higher dose did not reduce mortality. In an analysis of HEMO participants, ultrafiltration rates above 13 mL/kg/h were associated with higher all-cause and cardiovascular mortality. The KDIGO 2026 anemia guideline frames treatment as an individual decision weighing symptoms and risks.</p>
</div>
</details>

<div class="disclaimer"><strong>Important:</strong> This toolkit is an educational and audit aid. Physician orders, your unit&rsquo;s protocols and the patient&rsquo;s clinical condition govern all care.</div>

</main>"""

RELATED = """<!-- RELATED-GUIDES-START -->
<div class="related-guides">
  <h2>
    <span data-lang="en">Related Guides</span>
  </h2>
  <div class="related-cards">
  <a class="related-card" href="../academy/special-dialysis-nurse-roles.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Special Dialysis Nurse Roles</div>
    <div class="related-card-desc">Fourteen modules for hemodialysis nurses who carry a unit portfolio.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card" href="calc-qapi-run-chart-spc.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Run Chart</div>
    <div class="related-card-desc">Plot a measure over time and see whether a change is real.</div>
    <div class="related-card-arrow">Open →</div></a>
  <a class="related-card" href="calc-dialysis-adequacy-ktv.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Dialysis Adequacy (Kt/V)</div>
    <div class="related-card-desc">Single-pool Kt/V by the Daugirdas formula.</div>
    <div class="related-card-arrow">Open →</div></a>
  <a class="related-card has-thumb" href="dialysis-qapi-vs-cqi.html">
    <div class="related-card-tag">Quality</div>
    <div class="related-card-title">QAPI and CQI in Dialysis</div>
    <div class="related-card-desc">How dialysis units measure and improve quality.</div>
    <div class="related-card-arrow">Read →</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""

SCRIPT = r"""<script id="sdnr-tk-js">
(function(){
  var $=function(id){return document.getElementById(id);};
  function num(id){var v=parseFloat($(id).value);return isNaN(v)?null:v;}
  function show(p){$(p+'-result').style.display='block';}
  function r1(x){return Math.round(x*10)/10;}
  function wilson(x,n){var p=x/n,z=1.96,den=1+z*z/n,cen=(p+z*z/(2*n))/den,half=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;return [Math.max(0,cen-half)*100,Math.min(1,cen+half)*100];}
  // Tool 1: honest rate
  $('rt-btn').addEventListener('click',function(){
    show('rt');var e=num('rt-elig'),ex=num('rt-excl')||0,x=num('rt-num'),g=num('rt-goal');
    if(e===null||x===null||e<1||ex<0||ex>=e||x<0||x>e-ex){$('rt-verdict').innerHTML='<strong>Enter eligible cases (at least 1), exclusions smaller than that, and a numerator no larger than the denominator.</strong>';$('rt-action').innerHTML='';return;}
    var n=e-ex,ci=wilson(x,n),p=x/n*100;
    $('rt-pct').textContent=p.toFixed(0)+'%';$('rt-ci').textContent=ci[0].toFixed(0)+'–'+ci[1].toFixed(0)+'%';
    if(g!==null&&g>0&&g<=100){var need=Math.max(0,Math.ceil(g/100*n)-x);$('rt-gap').textContent=String(need);$('rt-gapt').textContent=need===0?'goal met':'more of '+n;}else{$('rt-gap').textContent='—';$('rt-gapt').textContent='set a goal';}
    var exs=ex>0?' after excluding '+ex+' of '+e+' (state the reason for each)':'';
    $('rt-verdict').innerHTML='<strong>'+p.toFixed(0)+'% ('+x+' of '+n+')</strong>'+exs+'. The true value could plausibly be anywhere from '+ci[0].toFixed(0)+'% to '+ci[1].toFixed(0)+'%.';
    var msg=n<30?'<strong>Small sample:</strong> report the count with the percentage and list the cases that did not meet the standard by name in the action log.':'Plot this month beside earlier months on a run chart and look at the pattern of misses before testing a change.';
    if(ex>0&&ex/e>0.2)msg='<strong>Check the exclusions:</strong> more than one in five eligible cases were excluded. Exclusions that remove the hardest cases make a rate look better than care really is. '+msg;
    $('rt-action').innerHTML=msg;
  });
  // Tool 2: infection rate
  $('in-btn').addEventListener('click',function(){
    show('in');var t=[['f','in-fe','in-fm'],['g','in-ge','in-gm'],['c','in-ce','in-cm']],E=0,M=0,bad=false,parts=[];
    t.forEach(function(a){var e=num(a[1]),m=num(a[2]);if(e===null&&m===null){$('in-'+a[0]).textContent='—';return;}
      if(e===null)e=0;if(m===null||m<=0){if(e>0)bad=true;$('in-'+a[0]).textContent='—';return;}
      var r=e/m*100;$('in-'+a[0]).textContent=r.toFixed(2);E+=e;M+=m;parts.push([a[0],r,m]);});
    if(bad){$('in-verdict').innerHTML='<strong>An access type has infections but no patient-months.</strong> Every event needs a denominator.';$('in-action').innerHTML='';return;}
    if(M<=0){$('in-verdict').innerHTML='<strong>Enter patient-months for at least one access type.</strong>';$('in-action').innerHTML='';return;}
    $('in-all').textContent=(E/M*100).toFixed(2);
    var names={f:'fistula',g:'graft',c:'catheter'},hi=parts.reduce(function(a,b){return b[1]>a[1]?b:a;},parts[0]);
    $('in-verdict').innerHTML='<strong>Overall '+(E/M*100).toFixed(2)+' per 100 patient-months</strong> ('+E+' infections over '+r1(M)+' patient-months). Highest by access type: '+names[hi[0]]+' at '+hi[1].toFixed(2)+'.';
    $('in-action').innerHTML=(M<100?'<strong>Small denominator:</strong> one event moves the rate a lot; review each infection as a case. ':'')+'Pair the rate with the catheter share of your patients and with hand hygiene and catheter-care observations, so you can see where to act.';
  });
  // Tool 3: delivery
  $('dv-btn').addEventListener('click',function(){
    show('dv');var pre=num('dv-pre'),post=num('dv-post'),rx=num('dv-rx'),del=num('dv-del'),uf=num('dv-uf'),wt=num('dv-wt');
    var ok=['dv-c1','dv-c2','dv-c3','dv-c4'].every(function(i){return $(i).checked;});
    var v=[],a=[];
    if(pre!==null&&post!==null&&pre>0&&post>=0&&post<pre){var urr=(pre-post)/pre*100;$('dv-urr').textContent=urr.toFixed(1)+'%';
      if(!ok){v.push('<strong style="color:var(--amber)">URR '+urr.toFixed(1)+'%, but the sample pair is not confirmed valid.</strong>');a.push('Do not report or act on this value until the sampling problem is checked; repeat the pair by the unit method if the physician asks.');}
      else{v.push('<strong>URR '+urr.toFixed(1)+'%.</strong>'+(urr<65?' Below 65%, which corresponds roughly to a Kt/V under 1.2.':''));if(urr<65)a.push('Report to the physician with the delivered minutes, blood flow achieved, access problems and any interruptions; these explain most low values.');}}
    else{$('dv-urr').textContent='—';}
    if(rx!==null&&del!==null&&rx>0&&del>=0){var tp=del/rx*100;$('dv-time').textContent=tp.toFixed(0)+'%';if(tp<100){v.push('Delivered '+del+' of '+rx+' prescribed minutes ('+(rx-del)+' minutes short).');a.push('Record why the session ended early (cramps, hypotension, access, schedule, patient request). A repeated pattern is a clinical question for the team, not a reason to remove fluid faster.');}}
    else{$('dv-time').textContent='—';}
    if(uf!==null&&wt!==null&&wt>0&&del!==null&&del>0){var ufr=uf*1000/wt/(del/60);$('dv-ufr').textContent=ufr.toFixed(1);if(ufr>13){v.push('<strong style="color:var(--red)">Ultrafiltration rate '+ufr.toFixed(1)+' mL/kg/h.</strong> Rates above 13 were associated with higher mortality.');a.push('Report to the physician with the weight gain between sessions and symptoms. Raising the rate to finish on time is not a nursing decision.');}else{v.push('Ultrafiltration rate '+ufr.toFixed(1)+' mL/kg/h.');}}
    else{$('dv-ufr').textContent='—';}
    $('dv-verdict').innerHTML=v.length?v.join(' '):'<strong>Enter at least one set of values.</strong>';
    $('dv-action').innerHTML=a.join(' ');
  });
  // Tool 4: hemoglobin
  $('hb-btn').addEventListener('click',function(){
    show('hb');var a=num('hb-1'),b=num('hb-2'),d1=$('hb-d1').value,d2=$('hb-d2').value;
    var red=$('hb-s1').checked||$('hb-s2').checked,inf=$('hb-s3').checked;
    if(a===null||b===null||!d1||!d2){$('hb-verdict').innerHTML='<strong>Enter both results and both dates.</strong>';$('hb-action').innerHTML='';return;}
    var days=(new Date(d2)-new Date(d1))/86400000;if(days<=0){$('hb-verdict').innerHTML='<strong>The latest date must be after the earlier date.</strong>';$('hb-action').innerHTML='';return;}
    var ch=b-a,wk=ch/days*7;$('hb-chg').textContent=(ch>0?'+':'')+ch.toFixed(1);$('hb-wk').textContent=(wk>0?'+':'')+wk.toFixed(2);$('hb-days').textContent=Math.round(days);
    var two=ch/days*14;
    if(red){$('hb-verdict').innerHTML='<strong style="color:var(--red)">Symptoms of bleeding or poor oxygen delivery with this trend.</strong>';$('hb-action').innerHTML='Check vital signs and tell the physician now. This is not a dosing-protocol step.';return;}
    if(ch<0){$('hb-verdict').innerHTML='<strong>Falling '+Math.abs(wk).toFixed(2)+' g/dL per week</strong> over '+Math.round(days)+' days.';$('hb-action').innerHTML='Report the trend to the prescriber with iron studies, recent blood loss (access bleeding, sampling, procedures), infection and missed doses.'+(inf?' Active infection was ticked: check the order on holding intravenous iron.':'');}
    else if(two>1){$('hb-verdict').innerHTML='<strong style="color:var(--amber)">Rising faster than 1 g/dL per 2 weeks</strong> (about '+two.toFixed(1)+' g/dL per 2 weeks).';$('hb-action').innerHTML='Product labels advise prescriber review at this pace. Tell the prescriber before the next scheduled dose; do not change the dose yourself.';}
    else{$('hb-verdict').innerHTML='<strong>Change of '+(ch>0?'+':'')+ch.toFixed(1)+' g/dL</strong> over '+Math.round(days)+' days.';$('hb-action').innerHTML='Record the trend for the scheduled anemia review.'+(inf?' Active infection was ticked: check the order on holding intravenous iron.':'');}
  });
})();
</script>"""


def main():
    s = SRC.read_text(encoding="utf-8")
    pub = None
    if OUT.exists():
        m = re.search(r'<meta property="article:published_time" content="([^"]+)">', OUT.read_text(encoding="utf-8"))
        pub = m.group(1) if m else None
    head, body = s.split("</head>", 1)
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', head)
    head = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{KEYWORDS}">', head)
    head = head.replace("https://renalcarematters.com/guides/calc-allograft-egfr-trend", URL)
    head = re.sub(r'<meta property="article:published_time" content="[^"]*">\n?', (f'<meta property="article:published_time" content="{pub}">\n' if pub else ""), head)
    head = re.sub(r'<meta property="article:modified_time" content="[^"]*">\n?', "", head)
    head = re.sub(r'<meta property="og:site_name" content="[^"]*">', '<meta property="og:site_name" content="Renal Care Matters">', head)
    for k in ("og:title", "twitter:title"):
        head = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', rf'<meta \1="{k}" content="{TITLE}">', head)
    for k in ("og:description", "twitter:description"):
        head = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', rf'<meta \1="{k}" content="{DESC}">', head)
    head = re.sub(r'"name": "Kidney Allograft eGFR Trend[^"]*"', f'"name": "{TITLE}"', head)
    head = re.sub(r'\s*"dateModified": "[^"]*",\n\s*"datePublished": "[^"]*",', "", head)
    body = re.sub(r'<section class="hero">.*?</section>', lambda _m: HERO, body, count=1, flags=re.S)
    body = re.sub(r'<nav class="nav-strip">.*?</nav>', lambda _m: NAV, body, count=1, flags=re.S)
    body = re.sub(r'<main class="container">.*?</main>', lambda _m: MAIN, body, count=1, flags=re.S)
    body = re.sub(r"<!-- REFERENCES-ACC-START -->.*?<!-- REFERENCES-ACC-END -->\n?", "", body, flags=re.S)
    body = re.sub(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", lambda _m: RELATED, body, count=1, flags=re.S)
    body = re.sub(r"<script>\s*document\.getElementById\('target_egfr'\).*?</script>", lambda _m: SCRIPT, body, count=1, flags=re.S)
    if "sdnr-tk-js" not in body:
        sys.exit("calculator script anchor not found in template")
    OUT.write_text(head + "</head>" + body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
