#!/usr/bin/env python3
"""Build guides/calc-dialysis-nurse-assistant-toolkit.html (Patient Care Assistant Toolkit).

Three tools for Dialysis Nurse Assistants / Patient Care Assistants and their preceptors: (1) weight and tare check with
the weight gain since the last session, (2) standing blood pressure check against the consensus definition of orthostatic
hypotension, (3) timed count and temperature converter. Every tool checks or converts a measurement the assistant was
asked to take and ends in a report to the RN; none proposes a treatment decision.
Chrome is copied from an existing calculator, as tools/dialysis_support_staff/build_calc_toolkit.py does.
Re-running carries over the page's article:published_time. Run via generate_dialysis_nurse_assistant.py --calc.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "guides"
SRC = GUIDES / "calc-allograft-egfr-trend.html"
OUT = GUIDES / "calc-dialysis-nurse-assistant-toolkit.html"
SLUG = "calc-dialysis-nurse-assistant-toolkit"
URL = f"https://renalcarematters.com/guides/{SLUG}"
TITLE = "Patient Care Assistant Toolkit: Dialysis Weight and Tare, Standing Blood Pressure and Timed Counts"
DESC = ("Three checks for dialysis nurse assistants and patient care assistants: net weight with wheelchair tare and weight gain "
        "since the last session, a standing blood pressure check against the consensus definition, and pulse, respiration and "
        "temperature conversions. Educational; every result is reported to the nurse.")
KEYWORDS = ("dialysis weight tare calculator, interdialytic weight gain percent calculator, wheelchair weight subtract, orthostatic "
            "hypotension calculator 20 10, standing blood pressure drop, pulse count 15 seconds times 4, Fahrenheit to Celsius nursing aide")

HERO = """<section class="hero">
<div class="container">
<div class="hero-tag">Dialysis Unit &middot; Nurse Assistant &middot; Toolkit</div>
<h1>Patient Care Assistant <em>Toolkit</em></h1>
<p class="hero-sub">Three quick checks for the numbers a Dialysis Nurse Assistant is asked to measure: a true net weight with the wheelchair tare and the gain since last session, a standing blood pressure check, and timed counts and temperature conversions. Each tool shows its arithmetic and ends the same way: report to the nurse. Built for the Renal Care Academy Dialysis Nurse Assistant / PCA subtrack.</p>
<div class="hero-meta">
</div>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;&middot;&nbsp; <a href="../academy/dialysis-nurse-assistant.html" class="hero-xlink">Nurse Assistant / PCA subtrack →</a></p>
</div>
</section>"""

NAV = """<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#instructions">Instructions</a>
<a class="nav-pill" href="#when">When to Use</a>
<a class="nav-pill" href="#weight">Weight &amp; Tare</a>
<a class="nav-pill" href="#standing">Standing BP</a>
<a class="nav-pill" href="#counts">Counts &amp; Temperature</a>
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
  <li><strong>Weight and tare:</strong> enter the scale reading, its unit, the weighed tare of the wheelchair or device, any clothing allowance your unit uses, and the last post-dialysis weight. Add your unit&rsquo;s written report threshold if it has one.</li>
  <li><strong>Standing blood pressure:</strong> enter the lying or sitting reading and the standing readings the nurse asked for. Help a dizzy patient sit first; complete numbers only when the patient is safe.</li>
  <li><strong>Counts and temperature:</strong> enter how many beats or breaths you counted and for how long; or a temperature to convert.</li>
  <li>Nothing you enter is stored or sent. Never enter a patient&rsquo;s name.</li>
</ol>
</div>

<details class="mdc-acc" id="when">
<summary>When to Use</summary>
<div class="mdc-acc-body">
<p>Use these tools while training (Modules 5 and 9 of the subtrack) and at work when your unit allows a check of your arithmetic. They catch the common errors: a guessed tare, pounds read as kilograms, a timed count multiplied wrongly, a standing drop calculated from the wrong pair of readings.</p>
<div class="alert alert-amber">
<div class="alert-icon">⚠️</div>
<div class="alert-body">
<h4>When NOT to rely on it</h4>
<p>These tools never decide anything about treatment. They do not set a dry weight, a fluid goal, a treatment time or a medicine. A symptom (breathlessness, chest pain, dizziness, confusion) is reported to the nurse at once, before any calculation. The thresholds shown are descriptions from published sources or your own unit&rsquo;s written threshold, not targets.</p>
</div>
</div>
</div>
</details>

<section class="section" id="weight">
<div class="section-tag">Tool 1</div>
<h2>Weight and tare check</h2>
<p>Results stay in your browser. Nothing is stored or sent.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("wt-scale", "Scale reading", "e.g. 78.6")}
    <div class="calc-field">
      <label for="wt-unit">Unit shown on the scale</label>
      <select id="wt-unit">
        <option value="kg" selected>Kilograms (kg)</option>
        <option value="lb">Pounds (lb)</option>
      </select>
      <div class="field-hint">Check the display; pounds read as kilograms is a common error</div>
    </div>
{field("wt-tare", "Tare of wheelchair or device (same unit)", "e.g. 15.2", "Weighed empty on the same scale, or the chair&rsquo;s labeled tare. 0 if standing")}
{field("wt-cloth", "Clothing or item allowance (same unit)", "e.g. 0", "Only if your unit uses one")}
{field("wt-post", "Last post-dialysis weight (kg)", "e.g. 58.0")}
{field("wt-thr", "Unit report threshold for gain (kg, optional)", "from your unit&rsquo;s policy", "Leave blank if your unit has none")}
  </div>
  <button class="calc-btn" type="button" id="wt-btn">Calculate</button>
{result("wt", [("net", "Net weight", "kg"), ("gain", "Gain since last", "kg"), ("pct", "Gain", "% of last post-weight")])}
  <p class="calc-disclaimer">⚕ Net weight = (scale &minus; tare &minus; allowance), converted to kilograms. Gain = net weight &minus; last post-dialysis weight. Report both, with the tare and how it was obtained, to the nurse.</p>
</div>
</section>

<section class="section" id="standing">
<div class="section-tag">Tool 2</div>
<h2>Standing blood pressure check</h2>
<p>For a lying-or-sitting to standing check the nurse asked for. Uses the consensus definition: a fall of at least 20 mm Hg systolic or at least 10 mm Hg diastolic within 3 minutes of standing.</p>
<div class="calc-wrap">
  <div class="calc-grid">
{field("st-s0", "Lying or sitting systolic (mm Hg)", "e.g. 132")}
{field("st-d0", "Lying or sitting diastolic (mm Hg)", "e.g. 74")}
{field("st-p0", "Lying or sitting pulse (per minute)", "e.g. 78", "Optional")}
{field("st-s1", "Standing systolic at about 1 minute", "e.g. 104")}
{field("st-d1", "Standing diastolic at about 1 minute", "e.g. 62")}
{field("st-p1", "Standing pulse at about 1 minute", "e.g. 96", "Optional")}
{field("st-s3", "Standing systolic at about 3 minutes", "optional", "Leave blank if the patient had to sit")}
{field("st-d3", "Standing diastolic at about 3 minutes", "optional")}
    <div class="calc-field">
      <label for="st-sym">Symptoms on standing</label>
      <select id="st-sym">
        <option value="none" selected>None reported</option>
        <option value="dizzy">Dizzy, lightheaded, vision dimming, or unsteady</option>
      </select>
    </div>
  </div>
  <button class="calc-btn" type="button" id="st-btn">Check</button>
{result("st", [("sys", "Largest systolic fall", "mm Hg"), ("dia", "Largest diastolic fall", "mm Hg"), ("pul", "Pulse change", "per minute")])}
  <p class="calc-disclaimer">⚕ A description used by clinicians, not a decision for you. If the patient is dizzy, help them sit and call the nurse first; record whichever readings you safely obtained.</p>
</div>
</section>

<section class="section" id="counts">
<div class="section-tag">Tool 3</div>
<h2>Timed count and temperature converter</h2>
<div class="calc-wrap">
  <div class="calc-grid">
    <div class="calc-field">
      <label for="ct-what">What you counted</label>
      <select id="ct-what">
        <option value="pulse" selected>Pulse (beats)</option>
        <option value="resp">Respirations (breaths)</option>
      </select>
    </div>
{field("ct-n", "Number counted", "e.g. 19", extra='min="0" step="1"')}
    <div class="calc-field">
      <label for="ct-sec">Counted for</label>
      <select id="ct-sec">
        <option value="15">15 seconds</option>
        <option value="30" selected>30 seconds</option>
        <option value="60">60 seconds</option>
      </select>
    </div>
    <div class="calc-field">
      <label for="ct-reg">Rhythm or pattern</label>
      <select id="ct-reg">
        <option value="reg" selected>Regular</option>
        <option value="irr">Irregular</option>
      </select>
    </div>
{field("tp-val", "Temperature to convert (optional)", "e.g. 100.4 or 38.0", extra='step="any"')}
    <div class="calc-field">
      <label for="tp-unit">Temperature entered in</label>
      <select id="tp-unit">
        <option value="F" selected>Fahrenheit (&deg;F)</option>
        <option value="C">Celsius (&deg;C)</option>
      </select>
    </div>
  </div>
  <button class="calc-btn" type="button" id="ct-btn">Convert</button>
{result("ct", [("rate", "Rate", "per minute"), ("temp", "Temperature", "converted"), ("note", "Recount?", "")])}
  <p class="calc-disclaimer">⚕ Count a full 60 seconds when the pulse or breathing is irregular. Report a new fever, shivering, or a rate far from the patient&rsquo;s usual at once.</p>
</div>
</section>

<details class="mdc-acc" id="evidence">
<summary>Evidence &amp; References</summary>
<div class="mdc-acc-body">
<h3 class="mdc-sub">Formula &amp; Equations</h3>
<table class="lab-table">
<thead><tr><th>Quantity</th><th>Equation or rule</th></tr></thead>
<tbody>
<tr><td>Pounds to kilograms</td><td>lb &times; 0.4536</td></tr>
<tr><td>Net weight</td><td>Scale reading &minus; tare &minus; clothing allowance (then converted to kg)</td></tr>
<tr><td>Weight gain</td><td>Net weight &minus; last post-dialysis weight</td></tr>
<tr><td>Gain as a percent</td><td>Gain &divide; last post-dialysis weight &times; 100</td></tr>
<tr><td>Standing fall</td><td>Lying or sitting value &minus; lowest standing value (systolic and diastolic separately)</td></tr>
<tr><td>Consensus definition of orthostatic hypotension</td><td>Systolic fall &ge; 20 mm Hg or diastolic fall &ge; 10 mm Hg within 3 minutes of standing</td></tr>
<tr><td>Rate per minute</td><td>Count &times; (60 &divide; seconds counted)</td></tr>
<tr><td>Temperature</td><td>&deg;C = (&deg;F &minus; 32) &times; 5/9; &deg;F = &deg;C &times; 9/5 + 32</td></tr>
</tbody>
</table>
<h3 class="mdc-sub">Evidence</h3>
<p>Weight gained between sessions is almost entirely water, and the pre-dialysis weight is a main input to the fluid the prescription removes, so an error in tare or units becomes an error in treatment. In 34,107 United States hemodialysis patients, an average interdialytic gain of 4.0 kg or more was associated with higher cardiovascular death than a gain of 1.5 to 2.0 kg after adjustment (hazard ratio 1.25), an association rather than a target. Excessive gain was also associated with higher mortality in the international DOPPS cohort. The consensus statement of the American Autonomic Society and European Federation of Autonomic Societies defines orthostatic hypotension as a sustained fall of at least 20 mm Hg systolic or 10 mm Hg diastolic within 3 minutes of standing. A systematic review of 328 studies found that single sources of error can move a blood pressure reading by tens of mm Hg, so an unexpected value should be repeated. Pulse oximetry can miss low oxygen, more often in patients with darker skin, so a symptom outranks a reassuring number.</p>
</div>
</details>

<div class="disclaimer"><strong>Important:</strong> This toolkit is an educational aid for supervised support workers. It does not make clinical decisions. The registered nurse assesses every finding, and your unit&rsquo;s written thresholds and procedures govern practice.</div>

</main>"""

RELATED = """<!-- RELATED-GUIDES-START -->
<div class="related-guides">
  <h2>
    <span data-lang="en">Related Guides</span>
  </h2>
  <div class="related-cards">
  <a class="related-card" href="../academy/dialysis-nurse-assistant.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Dialysis Nurse Assistant / PCA</div>
    <div class="related-card-desc">Twelve modules for the supervised support role in hemodialysis.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card" href="../academy/dialysis-nurse-assistant-05-arrival-observations-weights.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Module 5: Arrival, Observations and Weights</div>
    <div class="related-card-desc">Two identifiers, true weights, tare, and readings that lie.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card" href="calc-dialysis-support-staff-toolkit.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Dialysis Support Staff Toolkit</div>
    <div class="related-card-desc">Label dilution and wet contact time, turnover budget and safe lift check.</div>
    <div class="related-card-arrow">Open →</div></a>
  <a class="related-card has-thumb" href="dry-weight-determination.html">
    <div class="related-card-tag">Dialysis</div>
    <div class="related-card-title">Dry Weight Determination</div>
    <div class="related-card-desc">How the team decides a patient&rsquo;s target weight.</div>
    <div class="related-card-arrow">Read →</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""

SCRIPT = r"""<script id="dna-tk-js">
(function(){
  var $=function(id){return document.getElementById(id);};
  function num(id){var v=parseFloat($(id).value);return isNaN(v)?null:v;}
  function show(p){$(p+'-result').style.display='block';}
  function r1(x){return Math.round(x*10)/10;}
  // Tool 1: weight and tare
  $('wt-btn').addEventListener('click',function(){
    show('wt');var s=num('wt-scale'),t=num('wt-tare'),c=num('wt-cloth'),post=num('wt-post'),thr=num('wt-thr'),u=$('wt-unit').value;
    if(t===null)t=0;if(c===null)c=0;
    if(s===null||s<=0){$('wt-verdict').innerHTML='<strong>Enter the scale reading.</strong>';$('wt-action').innerHTML='';return;}
    var f=u==='lb'?0.4536:1,net=(s-t-c)*f;
    if(net<=0){$('wt-verdict').innerHTML='<strong style="color:var(--red)">The tare and allowance are larger than the reading.</strong> Check the numbers and the unit.';$('wt-action').innerHTML='';return;}
    $('wt-net').textContent=r1(net);
    if(post===null||post<=0){$('wt-gain').textContent='—';$('wt-pct').textContent='—';
      $('wt-verdict').innerHTML='<strong>Net weight '+r1(net)+' kg</strong>'+(u==='lb'?' (converted from pounds)':'')+'.';
      $('wt-action').innerHTML='Record the reading, the tare and how it was obtained, and report to the nurse.';return;}
    var g=net-post,p=g/post*100;$('wt-gain').textContent=(g>0?'+':'')+r1(g);$('wt-pct').textContent=(g>0?'+':'')+r1(p)+'%';
    var flag=g<0||(thr!==null&&thr>0&&g>thr);
    $('wt-gain').style.color=flag?'var(--red)':'';
    var v='<strong>Net weight '+r1(net)+' kg; '+(g>=0?'up ':'down ')+r1(Math.abs(g))+' kg ('+r1(Math.abs(p))+'%) since the last post-dialysis weight.</strong>';
    if(g<0)v+=' A loss between sessions is unusual: re-check the tare, the unit and the record, then tell the nurse.';
    else if(thr!==null&&thr>0&&g>thr)v+=' <span style="color:var(--red)">Above your unit&rsquo;s report threshold of '+thr+' kg: tell the nurse now.</span>';
    $('wt-verdict').innerHTML=v;
    $('wt-action').innerHTML='<strong>Report:</strong> &ldquo;'+r1(net)+' kilograms net'+(t>0?', tare '+r1(t*f)+' kg':'')+', '+(g>=0?'up ':'down ')+r1(Math.abs(g))+' from the last post-weight.&rdquo; Add any symptom first. You do not suggest a fluid goal.';
  });
  // Tool 2: standing blood pressure
  $('st-btn').addEventListener('click',function(){
    show('st');var s0=num('st-s0'),d0=num('st-d0'),p0=num('st-p0'),s1=num('st-s1'),d1=num('st-d1'),p1=num('st-p1'),s3=num('st-s3'),d3=num('st-d3'),sym=$('st-sym').value;
    if(s0===null||d0===null||s1===null||d1===null){$('st-verdict').innerHTML='<strong>Enter the lying or sitting reading and at least the 1-minute standing reading.</strong>';$('st-action').innerHTML='';return;}
    var sl=s3!==null?Math.min(s1,s3):s1,dl=d3!==null?Math.min(d1,d3):d1,sf=s0-sl,df=d0-dl;
    $('st-sys').textContent=sf;$('st-dia').textContent=df;$('st-pul').textContent=(p0!==null&&p1!==null)?((p1-p0>0?'+':'')+(p1-p0)):'—';
    var meets=sf>=20||df>=10;$('st-sys').style.color=sf>=20?'var(--red)':'';$('st-dia').style.color=df>=10?'var(--red)':'';
    var v=meets?'<strong style="color:var(--red)">Meets the consensus definition</strong> (systolic fall '+sf+', diastolic fall '+df+' mm Hg).':'<strong>Does not meet the consensus definition</strong> (systolic fall '+sf+', diastolic fall '+df+' mm Hg).';
    if(sym==='dizzy')v+=' <strong>The patient was dizzy:</strong> keep them seated and tell the nurse now, whatever the numbers.';
    $('st-verdict').innerHTML=v;
    $('st-action').innerHTML='<strong>Report:</strong> &ldquo;Sitting '+s0+' over '+d0+', standing '+s1+' over '+d1+(s3!==null&&d3!==null?' at one minute and '+s3+' over '+d3+' at three':' at one minute')+(p0!==null&&p1!==null?', pulse '+p0+' to '+p1:'')+(sym==='dizzy'?', dizzy':'')+'.&rdquo; The nurse decides what it means.';
  });
  // Tool 3: counts and temperature
  $('ct-btn').addEventListener('click',function(){
    show('ct');var n=num('ct-n'),sec=parseInt($('ct-sec').value,10),irr=$('ct-reg').value==='irr',what=$('ct-what').value,tv=num('tp-val'),tu=$('tp-unit').value;
    var parts=[];
    if(n!==null&&n>=0){var rate=Math.round(n*60/sec);$('ct-rate').textContent=rate;
      var need=irr&&sec<60;$('ct-note').textContent=need?'Yes':'No';$('ct-notet').textContent=need?'count a full 60 seconds':'';
      parts.push('<strong>'+(what==='pulse'?'Pulse':'Respirations')+' '+rate+' per minute</strong> ('+n+' in '+sec+' seconds).'+(need?' The rhythm was irregular: count again for a full 60 seconds and record that number.':''));}
    else{$('ct-rate').textContent='—';$('ct-note').textContent='—';}
    if(tv!==null){var out=tu==='F'?((tv-32)*5/9):(tv*9/5+32);$('ct-temp').textContent=(Math.round(out*10)/10)+(tu==='F'?' °C':' °F');
      var c=tu==='F'?out:tv;parts.push('Temperature '+(Math.round(out*10)/10)+(tu==='F'?' °C':' °F')+'.'+(c>=38?' <span style="color:var(--red)">A temperature of 38 °C or higher is a fever: tell the nurse now.</span>':''));}
    else{$('ct-temp').textContent='—';}
    if(!parts.length){$('ct-verdict').innerHTML='<strong>Enter a count or a temperature.</strong>';$('ct-action').innerHTML='';return;}
    $('ct-verdict').innerHTML=parts.join(' ');
    $('ct-action').innerHTML='Record the value, the method and the time. Report any change from the patient&rsquo;s usual, shivering or a new fever at once.';
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
    og = GUIDES.parent / "images" / "calc-dialysis-nurse-assistant-toolkit-og.png"
    if og.exists():
        img = "https://renalcarematters.com/images/" + og.name
        head = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*"', lambda m: m.group(1) + img + '"', head)
        head = re.sub(r'<meta property="og:image:width" content="\d+">', '<meta property="og:image:width" content="1200">', head)
        head = re.sub(r'<meta property="og:image:height" content="\d+">', '<meta property="og:image:height" content="630">', head)
    body = re.sub(r'<section class="hero">.*?</section>', lambda _m: HERO, body, count=1, flags=re.S)
    body = re.sub(r'<nav class="nav-strip">.*?</nav>', lambda _m: NAV, body, count=1, flags=re.S)
    body = re.sub(r'<main class="container">.*?</main>', lambda _m: MAIN, body, count=1, flags=re.S)
    body = re.sub(r"<!-- REFERENCES-ACC-START -->.*?<!-- REFERENCES-ACC-END -->\n?", "", body, flags=re.S)
    body = re.sub(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", lambda _m: RELATED, body, count=1, flags=re.S)
    body = re.sub(r"<script>\s*document\.getElementById\('target_egfr'\).*?</script>", lambda _m: SCRIPT, body, count=1, flags=re.S)
    if "dna-tk-js" not in body:
        sys.exit("calculator script anchor not found in template")
    OUT.write_text(head + "</head>" + body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
