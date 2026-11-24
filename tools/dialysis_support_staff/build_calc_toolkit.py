#!/usr/bin/env python3
"""Build guides/calc-dialysis-support-staff-toolkit.html (Dialysis Support Staff Toolkit).

Four tools for orderlies, EVS aides and their supervisors: (1) label dilution and wet contact time planner,
(2) station turnover time budget, (3) safe lift check (revised NIOSH lifting equation, occasional lifts),
(4) audit tally (fluorescent-marker thoroughness or hand hygiene compliance, with a 95% Wilson interval).
Chrome is copied from an existing calculator, as tools/transplant_nurse/build_calc_tac_level.py does.
Re-running carries over the page's article:published_time. Run via generate_dialysis_support_staff.py --calc.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "guides"
SRC = GUIDES / "calc-allograft-egfr-trend.html"
OUT = GUIDES / "calc-dialysis-support-staff-toolkit.html"
SLUG = "calc-dialysis-support-staff-toolkit"
URL = f"https://renalcarematters.com/guides/{SLUG}"
TITLE = "Dialysis Support Staff Toolkit: Dilution, Contact Time, Turnover, Safe Lifting and Audits"
DESC = ("Four tools for dialysis unit orderlies, environmental service aides and supervisors: a label dilution and wet "
        "contact time planner using only your product label, a station turnover time budget, a safe lift check with the "
        "revised NIOSH lifting equation, and an audit tally for cleaning and hand hygiene. Educational; local task cards govern.")
KEYWORDS = ("disinfectant dilution calculator from label, contact time planner cleaning, dialysis station turnover time, "
            "NIOSH lifting equation calculator metric, lifting index calculator, hand hygiene compliance calculator, fluorescent marker audit percentage")

HERO = """<section class="hero">
<div class="container">
<div class="hero-tag">Dialysis Unit &middot; Support Staff &middot; Toolkit</div>
<h1>Dialysis Support Staff <em>Toolkit</em></h1>
<p class="hero-sub">Four practical tools for orderlies, environmental service aides and their supervisors: dilute by measurement from your own label, keep surfaces wet for the full contact time, check whether the shift gap allows a full station turnover, judge a lift before it hurts someone, and turn audit counts into honest percentages. Built for the Renal Care Academy Dialysis Unit Support Staff subtrack.</p>
<div class="hero-meta">
</div>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;&middot;&nbsp; <a href="../academy/dialysis-unit-support-staff.html" class="hero-xlink">Support Staff subtrack →</a></p>
</div>
</section>"""

NAV = """<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#instructions">Instructions</a>
<a class="nav-pill" href="#when">When to Use</a>
<a class="nav-pill" href="#dilution">Dilution</a>
<a class="nav-pill" href="#turnover">Turnover</a>
<a class="nav-pill" href="#lift">Safe Lift</a>
<a class="nav-pill" href="#audit">Audit</a>
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
  <li><strong>Dilution and contact time:</strong> copy the dilution and wet contact time exactly from your product label or unit task card. This tool never supplies a dilution or a contact time of its own.</li>
  <li><strong>Turnover budget:</strong> enter your unit&rsquo;s real shift gap and the minutes each phase actually takes (time them for a week).</li>
  <li><strong>Safe lift check:</strong> measure the lift (centimeters and kilograms) for boxes, jugs, bins and bags. Not for lifting people.</li>
  <li><strong>Audit tally:</strong> enter the number of targets or opportunities and how many passed.</li>
  <li>Nothing you enter is stored or sent. Results are for learning, planning and discussion with your supervisor.</li>
</ol>
</div>

<details class="mdc-acc" id="when">
<summary>When to Use</summary>
<div class="mdc-acc-body">
<p>Use these tools while training (Modules 6, 7, 12 and 15 of the subtrack), when setting up task cards and storage, and when a supervisor reviews whether the schedule, products and storeroom let staff work safely. They make the arithmetic visible so problems can be fixed at the system level.</p>
<div class="alert alert-amber">
<div class="alert-icon">⚠️</div>
<div class="alert-body">
<h4>When NOT to rely on it</h4>
<p>Never use a dilution or contact time that is not printed on your product&rsquo;s label or your unit&rsquo;s task card. Do not use the lift check for patient handling: no adult can be lifted by hand within safe limits, and patient moves follow the nurse&rsquo;s plan with equipment. The lift check here covers occasional lifts only (one hour or less of lifting); frequent lifting needs the full NIOSH frequency table.</p>
</div>
</div>
</div>
</details>

<section class="section" id="dilution">
<div class="section-tag">Tool 1</div>
<h2>Label dilution and wet contact time</h2>
<p>Results stay in your browser. Nothing is stored or sent.</p>
<div class="calc-wrap">
  <div class="calc-grid">
    <div class="calc-field">
      <label for="dl-mode">How does your label state the dilution?</label>
      <select id="dl-mode">
        <option value="perL" selected>Milliliters of concentrate per liter of water</option>
        <option value="ratioW">Ratio 1 : N (1 part concentrate to N parts water)</option>
        <option value="ratioT">Ratio 1 : N (1 part concentrate in N parts total solution)</option>
      </select>
      <div class="field-hint">If the label does not say which ratio it means, ask your supervisor before mixing</div>
    </div>
{field("dl-val", "Number from the label (mL per liter, or N)", "copy from the label")}
{field("dl-vol", "Volume you want to make (liters)", "e.g. 4", "Bucket or bottle size")}
{field("dl-ct", "Wet contact time on the label (minutes)", "copy from the label", "Optional")}
{field("dl-dry", "How long the surface stays wet (minutes)", "time it", "Optional: time one wipe on the real surface")}
  </div>
  <button class="calc-btn" type="button" id="dl-btn">Calculate</button>
{result("dl", [("conc", "Concentrate", "mL"), ("water", "Water", "mL"), ("rewet", "Re-wets needed", "to reach contact time")])}
  <p class="calc-disclaimer">⚕ Uses only the numbers you enter from your label. Mix with the protection on the safety data sheet, water first then concentrate, and label the container with product, dilution, date, time and initials.</p>
</div>
</section>

<section class="section" id="turnover">
<div class="section-tag">Tool 2</div>
<h2>Station turnover time budget</h2>
<p>Shows whether the gap between treatments leaves time for the full environmental phase including wet contact time. A negative slack means the schedule, not the worker, needs to change.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("tb-gap", "Scheduled gap between end and next start (minutes)", "e.g. 30")}
{field("tb-clin", "Clinical phase until the patient has left (minutes)", "e.g. 12", "Rinse-back, needle removal, circuit removal, patient leaves")}
{field("tb-rem", "Removing items and visible soil (minutes)", "e.g. 4")}
{field("tb-dis", "Wetting all surfaces with disinfectant (minutes)", "e.g. 6")}
{field("tb-ct", "Label wet contact time after the last surface (minutes)", "from the label")}
{field("tb-insp", "Inspection, record and handoff (minutes)", "e.g. 2")}
{field("tb-setup", "Clinical setup of the next treatment after release (minutes)", "e.g. 3")}
  </div>
  <button class="calc-btn" type="button" id="tb-btn">Check the budget</button>
{result("tb", [("need", "Time needed", "minutes"), ("slack", "Slack", "minutes"), ("env", "Environmental phase", "minutes")])}
  <p class="calc-disclaimer">⚕ A simple model: contact time is counted from the last surface wetted, and phases are assumed not to overlap. Never shorten contact time to fit a schedule.</p>
</div>
</section>

<section class="section" id="lift">
<div class="section-tag">Tool 3</div>
<h2>Safe lift check (revised NIOSH lifting equation)</h2>
<p>For boxes, jugs, bins and bags lifted with two hands. Not for lifting people.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("lf-load", "Weight of the load (kg)", "e.g. 12")}
{field("lf-h", "Hands in front of the ankles, horizontal (cm)", "e.g. 40", "25 to 63 cm; closer is better")}
{field("lf-v", "Hand height at the start of the lift (cm)", "e.g. 0 (floor) or 75 (waist)", "0 to 175 cm")}
{field("lf-d", "Vertical travel of the lift (cm)", "e.g. 100", "Start to end height difference")}
{field("lf-a", "Twist at the start (degrees)", "e.g. 0", "0 to 135; 0 means no twist")}
    <div class="calc-field">
      <label for="lf-f">How often (one hour or less of lifting)</label>
      <select id="lf-f">
        <option value="1.00" selected>Occasional: about 1 lift every 5 minutes or less</option>
        <option value="0.97">About 1 lift every 2 minutes</option>
        <option value="0.94">About 1 lift every minute</option>
      </select>
      <div class="field-hint">For more frequent or longer lifting, use the full NIOSH table</div>
    </div>
    <div class="calc-field">
      <label for="lf-c">Grip on the load</label>
      <select id="lf-c">
        <option value="good" selected>Good: handles or cut-outs</option>
        <option value="fair">Fair: can curl fingers under it</option>
        <option value="poor">Poor: no handholds, bulky or floppy</option>
      </select>
    </div>
  </div>
  <button class="calc-btn" type="button" id="lf-btn">Check the lift</button>
{result("lf", [("rwl", "Recommended limit", "kg"), ("li", "Lifting index", "load ÷ limit"), ("main", "Biggest penalty", "factor")])}
  <p class="calc-disclaimer">⚕ An ergonomic estimate for healthy workers, not a guarantee. A lifting index above 1 means the task should be redesigned: store heavy items between knee and shoulder height, use carts, split loads, or lift with a second person.</p>
</div>
</section>

<section class="section" id="audit">
<div class="section-tag">Tool 4</div>
<h2>Audit tally</h2>
<p>For fluorescent-marker cleaning audits (targets marked and targets removed) or hand hygiene observation (opportunities and actions performed).</p>
<div class="calc-wrap">
  <div class="calc-grid">
    <div class="calc-field">
      <label for="au-type">Type of audit</label>
      <select id="au-type">
        <option value="marker" selected>Fluorescent-marker cleaning audit</option>
        <option value="hh">Hand hygiene observation</option>
      </select>
    </div>
{field("au-den", "Targets marked, or opportunities observed", "e.g. 30", extra='min="1" step="1"')}
{field("au-num", "Targets removed, or actions performed", "e.g. 21", extra='min="0" step="1"')}
{field("au-goal", "Unit goal (percent, optional)", "e.g. 90")}
  </div>
  <button class="calc-btn" type="button" id="au-btn">Calculate</button>
{result("au", [("pct", "Result", "percent"), ("ci", "95% range", "plausible true value"), ("gap", "To reach goal", "more passes needed")])}
  <p class="calc-disclaimer">⚕ Small samples bounce by chance; the 95% range shows how wide the uncertainty is. Plot results over weeks on a run chart before calling a change real. Use results to fix systems, not to blame individuals.</p>
</div>
</section>

<details class="mdc-acc" id="evidence">
<summary>Evidence &amp; References</summary>
<div class="mdc-acc-body">
<h3 class="mdc-sub">Formula &amp; Equations</h3>
<table class="lab-table">
<thead><tr><th>Quantity</th><th>Equation or rule</th></tr></thead>
<tbody>
<tr><td>Concentrate (mL per liter)</td><td>mL per liter × liters</td></tr>
<tr><td>Concentrate (1 : N parts water)</td><td>Volume × 1 ÷ (N + 1)</td></tr>
<tr><td>Concentrate (1 : N total)</td><td>Volume × 1 ÷ N</td></tr>
<tr><td>Re-wets needed</td><td>Round up (contact time ÷ wet time) − 1</td></tr>
<tr><td>Turnover slack</td><td>Gap − (clinical + removal + wetting + contact + inspection + next setup)</td></tr>
<tr><td>Recommended weight limit</td><td>23 kg × HM × VM × DM × AM × FM × CM; HM = 25/H; VM = 1 − 0.003 |V − 75|; DM = 0.82 + 4.5/D; AM = 1 − 0.0032 A; CM good 1.00, fair 0.95 (start below 75 cm) or 1.00, poor 0.90</td></tr>
<tr><td>Lifting index</td><td>Load ÷ recommended weight limit</td></tr>
<tr><td>Audit percentage</td><td>Passes ÷ total × 100, with a 95% Wilson score interval</td></tr>
</tbody>
</table>
<p style="font-size:.88rem;color:var(--text-muted);margin-top:10px;">Horizontal distances below 25 cm count as 25; above 63 cm, or a start height above 175 cm, the limit is zero (the lift should not be done). Vertical travel below 25 cm counts as 25. The frequency multipliers shown are for one hour or less of lifting from the NIOSH applications manual; longer or more frequent lifting needs the full table.</p>
<h3 class="mdc-sub">Evidence</h3>
<p>Disinfectant products must be used at the dilution and for the contact time on their labels; in a laboratory study of ready-to-use wipes, no further killing occurred once a product had dried, so a surface that dries early needs re-wetting. A bundle approach to surface disinfection combines the right product, correct technique, training, and monitoring with feedback. The revised NIOSH lifting equation and its lifting index identify lifting tasks that raise back-injury risk; its authors noted it was not fully validated but gives limits consistent with or lower than the wider literature, and NIOSH excluded patient handling from its use. Fluorescent marking showed that fewer than half of high-touch targets were cleaned at baseline in hospital rooms; audit with feedback improved thoroughness, and in the REACH trial a cleaning bundle including audit and feedback was followed by fewer vancomycin-resistant enterococcal infections. Hand hygiene compliance is measured as actions performed divided by opportunities observed, following the WHO method.</p>
</div>
</details>

<div class="disclaimer"><strong>Important:</strong> This toolkit is an educational and planning aid. Product labels, your unit&rsquo;s task cards, infection prevention and safety procedures, and the nurse&rsquo;s patient-handling plan govern all practice.</div>

</main>"""

RELATED = """<!-- RELATED-GUIDES-START -->
<div class="related-guides">
  <h2>
    <span data-lang="en">Related Guides</span>
  </h2>
  <div class="related-cards">
  <a class="related-card" href="../academy/dialysis-unit-support-staff.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Dialysis Unit Support Staff</div>
    <div class="related-card-desc">Fifteen modules for orderlies and environmental service aides.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card" href="../academy/dialysis-unit-support-staff-07-station-turnover.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Module 7: Safe Turnover of a Dialysis Station</div>
    <div class="related-card-desc">Clinical clearance, four statuses, wet contact time and the cleaning trials.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card" href="calc-qapi-run-chart-spc.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Run Chart</div>
    <div class="related-card-desc">Plot audit results over time and see whether a change is real.</div>
    <div class="related-card-arrow">Open →</div></a>
  <a class="related-card has-thumb" href="dialysis-qapi-vs-cqi.html">
    <div class="related-card-tag">Quality</div>
    <div class="related-card-title">QAPI and CQI in Dialysis</div>
    <div class="related-card-desc">How dialysis units measure and improve quality.</div>
    <div class="related-card-arrow">Read →</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""

SCRIPT = r"""<script id="duss-tk-js">
(function(){
  var $=function(id){return document.getElementById(id);};
  function num(id){var v=parseFloat($(id).value);return isNaN(v)?null:v;}
  function show(p){$(p+'-result').style.display='block';}
  function r1(x){return Math.round(x*10)/10;}
  // Tool 1: dilution
  $('dl-btn').addEventListener('click',function(){
    show('dl');var mode=$('dl-mode').value,v=num('dl-val'),L=num('dl-vol'),ct=num('dl-ct'),dry=num('dl-dry');
    var verdict=$('dl-verdict'),action=$('dl-action');
    if(v===null||L===null||v<=0||L<=0){verdict.innerHTML='<strong>Enter the label number and the volume.</strong>';action.innerHTML='';return;}
    var total=L*1000,conc;
    if(mode==='perL'){conc=v*L;}else if(mode==='ratioW'){conc=total/(v+1);}else{if(v<=1){verdict.innerHTML='<strong>For a 1 : N total ratio, N must be greater than 1.</strong>';return;}conc=total/v;}
    var water=mode==='perL'?total:total-conc;
    $('dl-conc').textContent=r1(conc);$('dl-water').textContent=Math.round(water);
    var rew='—',rt='to reach contact time';
    if(ct!==null&&dry!==null&&ct>0&&dry>0){var n=Math.max(0,Math.ceil(ct/dry)-1);rew=String(n);rt=n===0?'stays wet long enough':'apply '+n+' more time'+(n>1?'s':'')+' before it dries';}
    $('dl-rewet').textContent=rew;$('dl-rewett').textContent=rt;
    verdict.innerHTML='<strong>Measure '+r1(conc)+' mL of concentrate</strong> and add it to '+Math.round(water)+' mL of water'+(mode==='perL'?' (about '+L+' L)':'')+'.';
    action.innerHTML='<strong>Label:</strong> product name, dilution as on the label, date and time mixed, your initials. Discard as the label says. Never top up an old solution, and never mix two products.';
  });
  // Tool 2: turnover
  $('tb-btn').addEventListener('click',function(){
    show('tb');var ids=['tb-clin','tb-rem','tb-dis','tb-ct','tb-insp','tb-setup'],gap=num('tb-gap'),parts=ids.map(num);
    if(gap===null||parts.some(function(x){return x===null;})){$('tb-verdict').innerHTML='<strong>Enter the gap and every phase (use 0 if a phase does not apply).</strong>';$('tb-action').innerHTML='';return;}
    var need=parts.reduce(function(a,b){return a+b;},0),env=parts[1]+parts[2]+parts[3]+parts[4],slack=gap-need;
    $('tb-need').textContent=r1(need);$('tb-slack').textContent=r1(slack);$('tb-env').textContent=r1(env);
    $('tb-slack').style.color=slack<0?'var(--red)':(slack<5?'var(--amber)':'var(--green)');
    if(slack<0){$('tb-verdict').innerHTML='<strong style="color:var(--red)">The gap is '+r1(-slack)+' minutes too short.</strong> Contact time or inspection will be squeezed.';$('tb-action').innerHTML='<strong>Report to the supervisor:</strong> stagger start times, add staff at changeover, or ask the IPC lead about a product with a contact time that fits. Never shorten contact time.';}
    else if(slack<5){$('tb-verdict').innerHTML='<strong style="color:var(--amber)">Only '+r1(slack)+' minutes of slack.</strong> One late pickup or a small spill will push the turnover over.';$('tb-action').innerHTML='Record exceptions in the log so the supervisor can see how often this happens.';}
    else{$('tb-verdict').innerHTML='<strong style="color:var(--green)">The budget works with '+r1(slack)+' minutes to spare.</strong>';$('tb-action').innerHTML='Recheck with real timings over a week; averages hide the busy days.';}
  });
  // Tool 3: lift
  $('lf-btn').addEventListener('click',function(){
    show('lf');var L=num('lf-load'),H=num('lf-h'),V=num('lf-v'),D=num('lf-d'),A=num('lf-a');if(A===null)A=0;
    if(L===null||H===null||V===null||D===null){$('lf-verdict').innerHTML='<strong>Enter the weight, horizontal distance, start height and travel.</strong>';$('lf-action').innerHTML='';return;}
    var HM=H<=25?1:(H>63?0:25/H),VM=V>175?0:Math.max(0,1-0.003*Math.abs(V-75)),DM=D<=25?1:(D>175?0:0.82+4.5/D),AM=A>135?0:1-0.0032*A;
    var FM=parseFloat($('lf-f').value),c=$('lf-c').value,CM=c==='good'?1:(c==='fair'?(V<75?0.95:1):0.90);
    var f={'Hands far from the body':HM,'Start height':VM,'Travel distance':DM,'Twisting':AM,'Frequency':FM,'Grip':CM};
    var rwl=23*HM*VM*DM*AM*FM*CM;$('lf-rwl').textContent=rwl>0?r1(rwl):'0';
    var worst=Object.keys(f).reduce(function(a,b){return f[a]<=f[b]?a:b;});$('lf-main').textContent=worst;$('lf-maint').textContent='multiplier '+f[worst].toFixed(2);
    if(rwl<=0){$('lf-li').textContent='—';$('lf-verdict').innerHTML='<strong style="color:var(--red)">This lift is outside the equation&rsquo;s safe range.</strong>';$('lf-action').innerHTML='Redesign: bring the load closer, store it between knee and shoulder height, or use a cart.';return;}
    var li=L/rwl;$('lf-li').textContent=li.toFixed(2);$('lf-li').style.color=li>1?'var(--red)':'var(--green)';
    $('lf-verdict').innerHTML=li>1?'<strong style="color:var(--red)">Above the recommended limit</strong> (lifting index '+li.toFixed(2)+').':'<strong style="color:var(--green)">Within the recommended limit</strong> (lifting index '+li.toFixed(2)+').';
    $('lf-action').innerHTML=li>1?'<strong>Change the task, not the worker:</strong> improve the biggest penalty ('+worst.toLowerCase()+'), store the item at waist height, use a cart, split the load, or lift with help. Report the task to your supervisor.':'Keep the load close, avoid twisting by moving your feet, and recheck if the weight, height or frequency changes.';
  });
  // Tool 4: audit
  $('au-btn').addEventListener('click',function(){
    show('au');var n=num('au-den'),x=num('au-num'),g=num('au-goal');
    if(n===null||x===null||n<1||x<0||x>n){$('au-verdict').innerHTML='<strong>Enter a total of at least 1 and a number of passes no larger than the total.</strong>';$('au-action').innerHTML='';return;}
    var p=x/n,z=1.96,den=1+z*z/n,cen=(p+z*z/(2*n))/den,half=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;
    var lo=Math.max(0,cen-half)*100,hi=Math.min(1,cen+half)*100;
    $('au-pct').textContent=(p*100).toFixed(0)+'%';$('au-ci').textContent=lo.toFixed(0)+'–'+hi.toFixed(0)+'%';
    var type=$('au-type').value==='hh'?'hand hygiene compliance':'cleaning thoroughness';
    if(g!==null&&g>0&&g<=100){var need=Math.max(0,Math.ceil(g/100*n)-x);$('au-gap').textContent=String(need);$('au-gapt').textContent=need===0?'goal met':'more passes out of '+n;}else{$('au-gap').textContent='—';$('au-gapt').textContent='set a goal';}
    $('au-verdict').innerHTML='<strong>'+type.charAt(0).toUpperCase()+type.slice(1)+': '+(p*100).toFixed(0)+'%</strong> ('+x+' of '+n+'). The true value could plausibly be anywhere from '+lo.toFixed(0)+'% to '+hi.toFixed(0)+'%.';
    $('au-action').innerHTML=n<30?'<strong>Small sample:</strong> collect more observations before drawing conclusions, and look at which targets or moments were missed.':'Look at the pattern of misses (which surfaces, which moments), test one change with a Plan-Do-Study-Act cycle, and plot the result over weeks.';
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
    if "duss-tk-js" not in body:
        sys.exit("calculator script anchor not found in template")
    OUT.write_text(head + "</head>" + body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
