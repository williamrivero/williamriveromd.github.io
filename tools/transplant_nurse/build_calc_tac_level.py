#!/usr/bin/env python3
"""Build guides/calc-tacrolimus-level-check.html (Tacrolimus Level Check: trough timing, C/D ratio, IPV).

The page chrome (head, master + shared calculator CSS, header, toggles, footer scripts) is copied from an
existing calculator so the new page matches the library; only the content blocks are replaced. Run once,
then run the calculator pipeline (see generate_transplant_nurse.py --calc). Re-running rebuilds the page
and carries over its article:published_time.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUIDES = ROOT / "guides"
SRC = GUIDES / "calc-allograft-egfr-trend.html"
OUT = GUIDES / "calc-tacrolimus-level-check.html"
SLUG = "calc-tacrolimus-level-check"
URL = f"https://renalcarematters.com/guides/{SLUG}"
TITLE = "Tacrolimus Level Check: Trough Timing, C/D Ratio and Variability"
DESC = ("Check whether a tacrolimus level was a true trough from the dose and draw times, calculate the "
        "concentration-to-dose (C/D) ratio, and compute intrapatient variability (IPV) from serial troughs. "
        "Educational tool for kidney transplant nurses and clinicians; center protocols govern.")
KEYWORDS = ("tacrolimus trough timing, tacrolimus level calculator, concentration to dose ratio tacrolimus, "
            "tacrolimus intrapatient variability, coefficient of variation tacrolimus, kidney transplant nurse calculator")

HERO = f"""<section class="hero">
<div class="container">
<div class="hero-tag">Nephrology &middot; Transplant &middot; Clinical Calculator</div>
<h1>Tacrolimus Level Check <em>&amp; Variability</em></h1>
<p class="hero-sub">Was this level really a trough? Enter the dose and blood-draw times to check, then see the concentration-to-dose ratio and, from a series of levels on an unchanged dose, the intrapatient variability. Built for the Renal Care Academy Transplant Nurse subtrack.</p>
<div class="hero-meta">
</div>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;&middot;&nbsp; <a href="../academy/transplant-nurse-06-immunosuppression.html" class="hero-xlink">Transplant Nurse Module 6 →</a></p>
</div>
</section>"""

NAV = """<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#instructions">Instructions</a>
<a class="nav-pill" href="#when">When to Use</a>
<a class="nav-pill" href="#pearls">Pearls &amp; Pitfalls</a>
<a class="nav-pill" href="#calculator">Calculator</a>
<a class="nav-pill" href="#nextsteps">Next Steps</a>
<a class="nav-pill" href="#evidence">Evidence</a>
</div>
</nav>"""

MAIN = """<main class="container">

<div class="mdc-instructions" id="instructions"><span class="mdc-instr-label">Instructions</span>
<ol style="margin:0 0 0 1.2em;line-height:2;">
  <li>Choose the formulation: twice-daily immediate-release (dose every 12 hours) or once-daily extended-release (every 24 hours).</li>
  <li>Enter the date and time of the <strong>last dose taken before the sample</strong>, and the date and time the blood was <strong>actually drawn</strong>. If the next dose was already taken before the draw, tick the box.</li>
  <li>Enter the total daily dose in milligrams and the measured whole-blood level in ng/mL. Add the team's target range if you know it.</li>
  <li>Optionally paste earlier troughs taken on the same unchanged dose (three or more) to calculate intrapatient variability (IPV).</li>
  <li>Select <strong>Check level</strong>. Document the times and route the result to the transplant team. This tool never recommends a dose.</li>
</ol>
</div>

<details class="mdc-acc" id="when">
<summary>When to Use</summary>
<div class="mdc-acc-body">
<p>Use it whenever a tacrolimus result is about to be filed, charted or acted on, and especially when it is unexpectedly high or low. Tacrolimus has a narrow therapeutic window, and dose adjustments are based on the trough (C<sub>0</sub>), the lowest concentration just before the next dose. A sample drawn after the morning dose sits near the peak and can read two or three times higher than the true trough; read as a trough, it can lead to a dose cut that exposes the kidney to rejection.</p>
<div class="alert alert-teal">
<div class="alert-icon">✅</div>
<div class="alert-body">
<h4>Appropriate population</h4>
<p>Kidney transplant recipients on immediate-release (twice daily) or extended-release (once daily) tacrolimus whose levels are measured as troughs. Also useful for teaching the trough routine to patients and new staff.</p>
</div>
</div>
<div class="alert alert-amber">
<div class="alert-icon">⚠️</div>
<div class="alert-body">
<h4>When NOT to rely on it</h4>
<p>Do not use it for centers that monitor by area under the curve or by timed post-dose levels, for intravenous tacrolimus, for cyclosporine, or during acute illness with vomiting or diarrhea, when absorption is unpredictable. It does not interpret whether a level is right for a given patient; the transplant team sets the target.</p>
</div>
</div>
</div>
</details>

<details class="mdc-acc" id="pearls">
<summary>Pearls &amp; Pitfalls</summary>
<div class="mdc-acc-body">
<div class="alert alert-green">
<div class="alert-icon">💡</div>
<div class="alert-body">
<h4>Pearls</h4>
<p>Teach the routine: on blood-test mornings, bring the tacrolimus dose and take it <em>after</em> the draw, and note the time of last night's dose. Write three times on every request: last dose, collection, and next dose. A low C/D ratio (a &ldquo;fast metabolizer&rdquo;) and high IPV are both observational risk markers: they flag patients for review of adherence, interactions and formulation, not automatic dose changes.</p>
</div>
</div>
<div class="alert alert-red">
<div class="alert-icon">⛔</div>
<div class="alert-body">
<h4>Pitfalls</h4>
<p>Do not calculate a C/D ratio from a mistimed level; it is meaningless. Do not compare levels across a formulation or brand switch as if nothing changed. Rifampicin, carbamazepine and phenytoin lower levels; azoles, clarithromycin, diltiazem, verapamil, grapefruit and pomelo raise them. Diarrhea can raise levels.</p>
</div>
</div>
</div>
</details>

<section class="section" id="calculator">
<div class="section-tag">Interactive Tool</div>
<h2>Tacrolimus Level Check</h2>
<p>Results stay in your browser. Nothing is stored or sent.</p>
<div class="calc-wrap">
  <div class="calc-grid">
    <div class="calc-field">
      <label for="tlc-form">Formulation</label>
      <select id="tlc-form">
        <option value="12" selected>Immediate-release, twice daily (every 12 h)</option>
        <option value="24">Extended-release, once daily (every 24 h)</option>
      </select>
    </div>
    <div class="calc-field">
      <label for="tlc-dose">Total daily dose (mg/day)</label>
      <input type="number" id="tlc-dose" placeholder="e.g. 6" min="0.1" max="60" step="0.1">
      <div class="field-hint">For 3 mg twice daily, enter 6</div>
    </div>
    <div class="calc-field">
      <label for="tlc-last">Last dose taken (date and time)</label>
      <input type="datetime-local" id="tlc-last">
    </div>
    <div class="calc-field">
      <label for="tlc-draw">Blood drawn (date and time)</label>
      <input type="datetime-local" id="tlc-draw">
    </div>
    <div class="calc-field">
      <label for="tlc-level">Measured level (ng/mL)</label>
      <input type="number" id="tlc-level" placeholder="e.g. 7.5" min="0" max="80" step="0.1">
    </div>
    <div class="calc-field">
      <label for="tlc-tlow">Team target range (optional)</label>
      <div style="display:flex;gap:8px;"><input type="number" id="tlc-tlow" placeholder="e.g. 5" min="0" max="40" step="0.1" aria-label="Target low (ng/mL)"><input type="number" id="tlc-thigh" placeholder="e.g. 8" min="0" max="40" step="0.1" aria-label="Target high (ng/mL)"></div>
      <div class="field-hint">Low and high, ng/mL, as set by the team</div>
    </div>
    <div class="calc-field" style="grid-column:1/-1;">
      <label><input type="checkbox" id="tlc-nexttaken"> The next dose was already taken before the blood was drawn</label>
    </div>
    <div class="calc-field" style="grid-column:1/-1;">
      <label for="tlc-series">Earlier troughs on the same unchanged dose (optional)</label>
      <input type="text" id="tlc-series" placeholder="e.g. 6.8, 9.4, 5.1, 8.2" inputmode="decimal">
      <div class="field-hint">Three or more values, separated by commas; the current level is added automatically if its timing is valid</div>
    </div>
  </div>
  <button class="calc-btn" type="button" id="tlc-btn">Check level</button>
  <div class="calc-result-box" id="tlc-result" role="status" aria-live="polite">
    <div class="calc-metrics-row">
      <div class="calc-metric-card"><div class="cmv" id="tlc-hours">—</div><div class="cml">Hours after dose</div><div class="cmt" id="tlc-window">trough window</div></div>
      <div class="calc-metric-card"><div class="cmv" id="tlc-valid">—</div><div class="cml">True trough?</div><div class="cmt">timing check</div></div>
      <div class="calc-metric-card"><div class="cmv" id="tlc-cd">—</div><div class="cml">C/D ratio</div><div class="cmt" id="tlc-cdcat">ng/mL per mg/day</div></div>
      <div class="calc-metric-card"><div class="cmv" id="tlc-ipv">—</div><div class="cml">IPV (CV%)</div><div class="cmt" id="tlc-ipvn">needs 3+ levels</div></div>
    </div>
    <div class="calc-verdict-text" id="tlc-verdict"></div>
    <div class="calc-action-text" id="tlc-action"></div>
  </div>
  <p class="calc-disclaimer">⚕ Educational tool. It checks sample timing and computes two observational risk markers; it does not recommend doses. Center protocols and the transplant team govern every dose decision.</p>
</div>
</section>

<details class="mdc-acc" id="nextsteps">
<summary>Next Steps</summary>
<div class="mdc-acc-body">
<ul style="margin:8px 0 0 1.1em;padding:0;line-height:1.8;">
<li><strong>Not a true trough:</strong> label the result as mistimed on the request and in the chart, with the actual times, and route it to the team, who will interpret it and decide on a repeat. Reteach the trough routine.</li>
<li><strong>True trough outside the target:</strong> report to the team with the times, current medicines (new antibiotics, antifungals, anticonvulsants, rifampicin), supplements, diarrhea or vomiting, missed doses and any formulation or brand change.</li>
<li><strong>Low C/D ratio or high IPV:</strong> flag for review of adherence, interactions and formulation at the next team discussion; use a structured adherence question.</li>
<li>Never change, hold or substitute a dose without an authorized order.</li>
</ul>
</div>
</details>

<details class="mdc-acc" id="evidence">
<summary>Evidence &amp; References</summary>
<div class="mdc-acc-body">
<h3 class="mdc-sub">Formula &amp; Equations</h3>
<table class="lab-table">
<thead><tr><th>Quantity</th><th>Equation or rule</th></tr></thead>
<tbody>
<tr><td>Hours after dose</td><td>Collection time − last dose time</td></tr>
<tr><td>Trough window (this tool)</td><td>Twice daily: 11 to 13 h after the last dose; once daily: 22 to 26 h; and the next dose not yet taken</td></tr>
<tr><td>Concentration-to-dose ratio</td><td>Trough (ng/mL) ÷ total daily dose (mg/day)</td></tr>
<tr><td>C/D categories</td><td>Below 1.05: fast; 1.05 to 1.54: intermediate; 1.55 or above: slow metabolizer (cutoffs from the original kidney transplant cohort; not validated as treatment thresholds)</td></tr>
<tr><td>Intrapatient variability</td><td>Coefficient of variation = sample standard deviation ÷ mean × 100, from three or more troughs on an unchanged dose</td></tr>
</tbody>
</table>
<p style="font-size:.88rem;color:var(--text-muted);margin-top:10px;">The timing windows are a practical convention for teaching and documentation; centers may use narrower or wider windows. IPV thresholds differ between studies (values above roughly 30 percent are often described as high), and IPV is meaningful only when the dose, formulation and interacting drugs did not change across the levels.</p>
<h3 class="mdc-sub">Evidence</h3>
<p>Tacrolimus-based triple therapy was established by the ELITE-Symphony trial, in which low-dose tacrolimus produced the lowest one-year rejection rate and best graft survival among four regimens. In a cohort of 248 kidney recipients, a low C/D ratio was associated with lower eGFR over two years and more biopsy-proven calcineurin inhibitor toxicity and BK polyomavirus nephropathy. High intrapatient variability has been repeatedly associated with rejection, donor-specific antibodies and graft loss, and nonadherence is a leading cause. All three markers derive from observational data; they identify patients for closer review rather than dictating dose.</p>
</div>
</details>

<div class="disclaimer"><strong>Important:</strong> This calculator is an educational aid for transplant nurses, clinicians and informed patients. It does not replace the transplant team's interpretation of drug levels or its dosing decisions.</div>

</main>"""

RELATED = """<!-- RELATED-GUIDES-START -->
<div class="related-guides">
  <h2>
    <span data-lang="en">Related Guides</span>
  </h2>
  <div class="related-cards">
  <a class="related-card" href="calc-tacrolimus-dosing.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Tacrolimus Dosing &amp; Target Trough</div>
    <div class="related-card-desc">Weight-based starting dose and typical target trough by time after transplant.</div>
    <div class="related-card-arrow">Calculate →</div></a>
  <a class="related-card" href="calc-drug-interaction-checker.html">
    <div class="related-card-tag">Calculator</div>
    <div class="related-card-title">Drug Interaction Checker</div>
    <div class="related-card-desc">Screen a medicine list for interactions before routing to the pharmacist.</div>
    <div class="related-card-arrow">Open →</div></a>
  <a class="related-card" href="../academy/transplant-nurse-06-immunosuppression.html">
    <div class="related-card-tag">Renal Care Academy</div>
    <div class="related-card-title">Transplant Nurse Module 6: Immunosuppression and Medication Safety</div>
    <div class="related-card-desc">Mechanisms, trough timing, interactions, formulations and nonadherence.</div>
    <div class="related-card-arrow">Read →</div></a>
  <a class="related-card has-thumb" href="kidney-transplant.html">
    <div class="related-card-tag">Transplant</div>
    <div class="related-card-title">Kidney Transplant</div>
    <div class="related-card-desc">Patient overview of transplant and its medicines.</div>
    <div class="related-card-arrow">Read →</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""

SCRIPT = r"""<script id="tlc-js">
(function(){
  var $=function(id){return document.getElementById(id);};
  function num(id){var v=parseFloat($(id).value);return isNaN(v)?null:v;}
  function series(){return ($('tlc-series').value||'').split(/[,;\s]+/).map(parseFloat).filter(function(x){return !isNaN(x)&&x>0;});}
  function cv(a){var n=a.length,m=a.reduce(function(s,x){return s+x;},0)/n;var sd=Math.sqrt(a.reduce(function(s,x){return s+(x-m)*(x-m);},0)/(n-1));return {cv:sd/m*100,mean:m,sd:sd};}
  function run(){
    var interval=parseFloat($('tlc-form').value),dose=num('tlc-dose'),lvl=num('tlc-level');
    var last=$('tlc-last').value,draw=$('tlc-draw').value,taken=$('tlc-nexttaken').checked;
    var lo=num('tlc-tlow'),hi=num('tlc-thigh');
    var verdict=$('tlc-verdict'),action=$('tlc-action'),box=$('tlc-result');
    box.style.display='block';
    if(!last||!draw||lvl===null){verdict.innerHTML='<strong>Enter the last dose time, the draw time and the level.</strong>';action.innerHTML='';return;}
    var h=(new Date(draw)-new Date(last))/3600000;
    var win=interval===12?[11,13]:[22,26];
    $('tlc-window').textContent='trough window '+win[0]+'–'+win[1]+' h';
    $('tlc-hours').textContent=h.toFixed(1);
    var valid=h>=win[0]&&h<=win[1]&&!taken;
    var why='';
    if(h<0){why='The draw time is before the dose time. Check the entries.';valid=false;}
    else if(taken){why='The next dose was taken before the draw, so this level reflects a fresh dose.';}
    else if(h<win[0]){why='Drawn '+h.toFixed(1)+' h after the dose, before the trough window'+(h<=4?', close to the peak; it may read two to three times higher than the true trough':'')+'.';}
    else if(h>win[1]){why='Drawn '+h.toFixed(1)+' h after the dose, after the trough window; a dose may have been missed or delayed, and the level may underestimate exposure.';}
    $('tlc-valid').textContent=valid?'Yes':'No';
    $('tlc-valid').style.color=valid?'var(--green)':'var(--red)';
    var cdTxt='—',cat='ng/mL per mg/day';
    if(valid&&dose){var cd=lvl/dose;cdTxt=cd.toFixed(2);cat=cd<1.05?'fast metabolizer range':(cd<1.55?'intermediate range':'slow metabolizer range');}
    else if(!valid){cat='not calculated (mistimed)';}
    $('tlc-cd').textContent=cdTxt;$('tlc-cdcat').textContent=cat;
    var s=series();if(valid)s=s.concat([lvl]);
    if(s.length>=3){var r=cv(s);$('tlc-ipv').textContent=r.cv.toFixed(0)+'%';$('tlc-ipvn').textContent=s.length+' levels, mean '+r.mean.toFixed(1)+' ng/mL'+(r.cv>=30?' · high':'');}
    else{$('tlc-ipv').textContent='—';$('tlc-ipvn').textContent='needs 3+ levels';}
    var tgt='';
    if(valid&&lo!==null&&hi!==null){tgt=lvl<lo?' The trough is <strong>below</strong> the team target ('+lo+'–'+hi+' ng/mL).':(lvl>hi?' The trough is <strong>above</strong> the team target ('+lo+'–'+hi+' ng/mL).':' The trough is within the team target ('+lo+'–'+hi+' ng/mL).');}
    if(valid){
      verdict.innerHTML='<strong style="color:var(--green)">Timing is consistent with a true trough</strong> ('+h.toFixed(1)+' h after the last dose).'+tgt;
      action.innerHTML='<strong>Action:</strong> document last dose, collection and next dose times and route the result to the transplant team'+(tgt.indexOf('within')<0&&tgt?' with current medicines, missed doses, diarrhea or vomiting, and any formulation change':'')+'. A low C/D ratio or IPV of 30% or more is a flag for review of adherence, interactions and formulation, not a dosing instruction.';
    } else {
      verdict.innerHTML='<strong style="color:var(--red)">Not a true trough.</strong> '+why;
      action.innerHTML='<strong>Action:</strong> label the result as mistimed with the actual times, route it to the team for interpretation and a repeat if they request one, and reteach the trough routine. Do not use it to calculate a C/D ratio or to adjust a dose.';
    }
  }
  $('tlc-btn').addEventListener('click',run);
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
    head = head.replace('"audienceType": "patient"', '"audienceType": "Clinician"')
    body = re.sub(r'<section class="hero">.*?</section>', lambda _m: HERO, body, count=1, flags=re.S)
    body = re.sub(r'<nav class="nav-strip">.*?</nav>', lambda _m: NAV, body, count=1, flags=re.S)
    body = re.sub(r'<main class="container">.*?</main>', lambda _m: MAIN, body, count=1, flags=re.S)
    body = re.sub(r"<!-- REFERENCES-ACC-START -->.*?<!-- REFERENCES-ACC-END -->\n?", "", body, flags=re.S)
    body = re.sub(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", lambda _m: RELATED, body, count=1, flags=re.S)
    # drop the source page's calculator script, keep the shared ones
    body = re.sub(r"<script>\s*document\.getElementById\('target_egfr'\).*?</script>", lambda _m: SCRIPT, body, count=1, flags=re.S)
    if "tlc-js" not in body:
        sys.exit("calculator script anchor not found in template")
    OUT.write_text(head + "</head>" + body, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
