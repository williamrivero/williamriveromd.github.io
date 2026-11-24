#!/usr/bin/env python3
"""Builds guides/calc-reprocessing-technician-toolkit.html from the Charge Nurse toolkit page (same chrome, CSS and scripts),
replacing the head, hero, calculator sections and calculator script. Training calculators only: no output is a release decision.
Run from the repo root:  python3 tools/techcourses/reprocessing_tech/build_toolkit.py
Then run the calculator patchers (build_calc_app.py, add_calc_nav_pill.py, patch_calc_handoff.py, patch_guide_rail.py,
patch_share_buttons.py, generate_latest_calculators.py)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "guides" / "calc-dialysis-charge-nurse-toolkit.html"
OUT = ROOT / "guides" / "calc-reprocessing-technician-toolkit.html"

TITLE = "Reprocessing Technician Toolkit: 6 Training Calculators"
DESC = ("Six training calculators for dialyzer reprocessing: total cell volume retained, a use counter with every acceptance gate, "
        "germicide dilution, contact time and storage window, a dialysis water log check, and a monthly reuse audit. No output is a release decision.")
KEYW = ("dialyzer reprocessing calculator, total cell volume TCV calculator, dialyzer reuse count, PhilHealth five uses dialyzer, "
        "germicide dilution C1V1, peracetic acid contact time, dialysis water TDS log, dialyzer reuse audit")
OG_IMG = "https://renalcarematters.com/images/og/dialyzer-reprocessing-technician-vignette-hero.jpg"
OG_ALT = "A reprocessing technician checking the label of a hollow-fiber dialyzer at a clean reprocessing station"

SECTIONS = r"""
<nav class="toc" aria-label="Calculators">
<a href="#c1">1 TCV retained</a><a href="#c2">2 Use counter and gates</a><a href="#c3">3 Germicide dilution</a><a href="#c4">4 Contact and storage clock</a><a href="#c5">5 Water log check</a><a href="#c6">6 Monthly audit</a>
</nav>
<div class="notice" role="note"><b>Training only.</b> These tools do arithmetic for learning and for checking your own work. None of them releases a dialyzer, approves a water result or sets a chemical value. Limits, concentrations and times come from your unit&rsquo;s approved reuse program and the instructions for use (IFU). Use synthetic or de-identified data only; nothing you enter leaves this page.</div>

<section class="calc" id="c1" aria-labelledby="h1">
<h2 id="h1">1 · Total cell volume (TCV) retained</h2>
<p class="mod">Modules 02, 09</p>
<div class="grid">
<div><label for="c1b">Baseline TCV of this dialyzer (mL)</label><input id="c1b" type="number" step="0.1" value="100" placeholder="e.g. 100"></div>
<div><label for="c1m">Measured TCV after processing (mL)</label><input id="c1m" type="number" step="0.1" value="82" placeholder="e.g. 82"></div>
<div><label for="c1f">Unit floor (%) &middot; PhilHealth PC 2024-0029 cites 80</label><input id="c1f" type="number" step="0.1" value="80" placeholder="80"></div>
</div>
<button type="button" onclick="cnc1()">Calculate</button>
<div class="out" id="c1out" aria-live="polite"></div>
<p class="why"><b>Formula.</b> Retained TCV (%) = measured &divide; baseline &times; 100. The baseline is this dialyzer&rsquo;s own first measurement, never a catalog value. A missing, zero or negative baseline returns HOLD. A measured value above baseline is flagged for review, never capped or accepted automatically. <b>Meeting the floor passes one gate only:</b> identity, eligibility, uses left, inspection, integrity, the processing record, germicide, storage time and the residual test must all pass too.</p>
</section>

<section class="calc" id="c2" aria-labelledby="h2">
<h2 id="h2">2 · Use counter and acceptance gates</h2>
<p class="mod">Modules 03, 09</p>
<div class="grid">
<div><label for="c2u">Completed treatment uses so far (including the first)</label><input id="c2u" type="number" min="0" step="1" value="4" placeholder="e.g. 4"></div>
<div><label for="c2c">Payer ceiling (total uses) &middot; PhilHealth PC 2024-0023 cites 5</label><input id="c2c" type="number" min="1" step="1" value="5"></div>
<div><label for="c2l">IFU or facility limit (total uses, leave blank if none)</label><input id="c2l" type="number" min="1" step="1" value="" placeholder="e.g. 3"></div>
<div><label for="c2e">Patient eligibility (current program list)</label><select id="c2e"><option value="">Not recorded</option><option value="p">Eligible</option><option value="f">Not eligible / status changed</option></select></div>
<div><label for="c2t">TCV gate</label><select id="c2t"><option value="">Not recorded</option><option value="p">Passed</option><option value="f">Failed</option></select></div>
<div><label for="c2i">Integrity (pressure-hold) gate</label><select id="c2i"><option value="">Not recorded</option><option value="p">Passed</option><option value="f">Failed</option></select></div>
<div><label for="c2v">Inspection and processing record</label><select id="c2v"><option value="">Not recorded</option><option value="p">Complete, no rejecting finding</option><option value="f">Rejecting finding or gap</option></select></div>
</div>
<button type="button" onclick="cnc2()">Check</button>
<div class="out" id="c2out" aria-live="polite"></div>
<p class="why"><b>Logic.</b> Next use = completed uses + 1. The limit is the stricter of the payer ceiling and any IFU or facility limit. A next use above the limit is NOT ELIGIBLE, whatever the tests say. Any failed gate makes the dialyzer NOT ELIGIBLE; any gate not recorded returns HOLD. <b>Uses are not reuses:</b> five uses means the first treatment plus four reuses. A processing cycle that had to be repeated is not a use.</p>
</section>

<section class="calc" id="c3" aria-labelledby="h3">
<h2 id="h3">3 · Germicide dilution check (C1V1 = C2V2)</h2>
<p class="mod">Module 06</p>
<div class="grid">
<div><label for="c3s">Stock concentration (%) from the product label</label><input id="c3s" type="number" step="0.01" value="" placeholder="from the IFU"></div>
<div><label for="c3t">Target concentration (%) from the IFU and SOP</label><input id="c3t" type="number" step="0.01" value="" placeholder="from the IFU"></div>
<div><label for="c3v">Final volume to prepare (L)</label><input id="c3v" type="number" step="0.01" value="" placeholder="e.g. 10"></div>
</div>
<button type="button" onclick="cnc3()">Calculate</button>
<div class="out" id="c3out" aria-live="polite"></div>
<p class="why"><b>Formula.</b> Volume of concentrate V1 = (target C2 &times; final volume V2) &divide; stock C1; water = V2 &minus; V1. No default values are given because concentrations are product-specific. <b>The arithmetic predicts the strength; only the potency test proves it.</b> In a CDC-investigated outbreak, poorly mixed germicide measured 1.4% at the top and 3.5% at the bottom of the same container (Beck-Sague et al., 1990). Mix in the order and manner the IFU sets, then test.</p>
</section>

<section class="calc" id="c4" aria-labelledby="h4">
<h2 id="h4">4 · Contact time and storage clock</h2>
<p class="mod">Module 10</p>
<div class="grid">
<div><label for="c4f">Germicide fill date and time</label><input id="c4f" type="datetime-local"></div>
<div><label for="c4c">Minimum contact time (hours) from the IFU</label><input id="c4c" type="number" min="0" step="0.1" value="" placeholder="from the IFU"></div>
<div><label for="c4s">Maximum storage (days) from the IFU and program</label><input id="c4s" type="number" min="0" step="0.1" value="" placeholder="from the IFU"></div>
<div><label for="c4u">Planned treatment date and time</label><input id="c4u" type="datetime-local"></div>
</div>
<button type="button" onclick="cnc4()">Check window</button>
<div class="out" id="c4out" aria-live="polite"></div>
<p class="why"><b>Formula.</b> Earliest use = fill time + minimum contact time. Expiry = fill time + maximum storage. Before the earliest use the dialyzer is not yet disinfected; after expiry it is outside the proven window. Either way it is reprocessed or discarded as your procedure directs. A missing fill time returns HOLD.</p>
</section>

<section class="calc" id="c5" aria-labelledby="h5">
<h2 id="h5">5 · Dialysis water log check</h2>
<p class="mod">Module 05</p>
<div class="grid">
<div><label for="c5t">Latest weekly product-water TDS (mg/L)</label><input id="c5t" type="number" min="0" step="0.1" value="" placeholder="e.g. 6"></div>
<div><label for="c5ta">TDS corrective-action value (mg/L) &middot; DOH AO 2013-0003 cites 10</label><input id="c5ta" type="number" min="0" step="0.1" value="10"></div>
<div><label for="c5td">Date of that TDS reading</label><input id="c5td" type="date"></div>
<div><label for="c5m">Latest point-of-use microbiology (CFU/mL)</label><input id="c5m" type="number" min="0" step="1" value="" placeholder="lab result"></div>
<div><label for="c5ml">Microbiology maximum (CFU/mL), your edition</label><input id="c5ml" type="number" min="0" step="1" value="100"></div>
<div><label for="c5ma">Microbiology action level (CFU/mL)</label><input id="c5ma" type="number" min="0" step="1" value="50"></div>
<div><label for="c5e">Latest endotoxin (EU/mL)</label><input id="c5e" type="number" min="0" step="0.001" value="" placeholder="lab result"></div>
<div><label for="c5el">Endotoxin maximum (EU/mL), your edition</label><input id="c5el" type="number" min="0" step="0.001" value="0.25"></div>
<div><label for="c5ea">Endotoxin action level (EU/mL)</label><input id="c5ea" type="number" min="0" step="0.001" value="0.125"></div>
<div><label for="c5md">Date of the microbiology sample</label><input id="c5md" type="date"></div>
</div>
<button type="button" onclick="cnc5()">Check log</button>
<div class="out" id="c5out" aria-live="polite"></div>
<p class="why"><b>Rules shown.</b> DOH AO 2013-0003: weekly product-water TDS with corrective action above 10 mg/L; microbiology at least monthly. The default microbiology and endotoxin values follow ISO 23500-3 dialysis water (maximum 100 CFU/mL and 0.25 EU/mL, action levels at half); check them against the edition your facility follows. Green = below action level; amber = at or above the action level (investigate and correct); red = above the maximum, or a test overdue (TDS older than 7 days, microbiology older than 31 days). <b>The medical director owns water quality;</b> this tool never clears water for use.</p>
</section>

<section class="calc" id="c6" aria-labelledby="h6">
<h2 id="h6">6 · Monthly reuse audit</h2>
<p class="mod">Module 12</p>
<div class="grid">
<div><label for="c6n">Dialyzers used this month (new dialyzers started)</label><input id="c6n" type="number" min="0" step="1" value="100"></div>
<div><label for="c6t">Treatments delivered with them</label><input id="c6t" type="number" min="0" step="1" value="440"></div>
<div><label for="c6p">Processing cycles performed</label><input id="c6p" type="number" min="0" step="1" value="352"></div>
<div><label for="c6r">Pyrogenic reactions (fever or chills during treatment)</label><input id="c6r" type="number" min="0" step="1" value="1"></div>
<div><label for="c6d1">Discards: failed TCV</label><input id="c6d1" type="number" min="0" step="1" value="6"></div>
<div><label for="c6d2">Discards: failed integrity</label><input id="c6d2" type="number" min="0" step="1" value="2"></div>
<div><label for="c6d3">Discards: clot or visual</label><input id="c6d3" type="number" min="0" step="1" value="5"></div>
<div><label for="c6d4">Discards: use limit reached</label><input id="c6d4" type="number" min="0" step="1" value="70"></div>
<div><label for="c6d5">Discards: expiry, time limit or record gap</label><input id="c6d5" type="number" min="0" step="1" value="3"></div>
<div><label for="c6d6">Discards: other</label><input id="c6d6" type="number" min="0" step="1" value="1"></div>
</div>
<button type="button" onclick="cnc6()">Summarize</button>
<div class="out" id="c6out" aria-live="polite"></div>
<p class="why"><b>Formulas.</b> Average uses per dialyzer = treatments &divide; dialyzers used. Discard rate by reason = discards for that reason &divide; processing cycles. Reactions per 1,000 treatments = reactions &divide; treatments &times; 1,000. <b>Average uses is a result of good care, not a target:</b> rewarding a higher number can lead staff to pass dialyzers that should fail. Read the numbers together; a rise in reactions is always investigated.</p>
</section>
<div class="disclaimer"><strong>Important:</strong> These are training calculators. They do not release dialyzers, clear water, or set chemical concentrations, contact times or limits; your unit&rsquo;s approved reuse program, the instructions for use and the medical director do. Draft, reviewed November 25, 2026.</div>
"""

SCRIPT = r"""<script>
(function(){
function v(id){var e=document.getElementById(id);if(!e)return NaN;var x=String(e.value).trim();return x===""?NaN:Number(x);}
function s(id){var e=document.getElementById(id);return e?String(e.value).trim():"";}
function f(x,d){return isFinite(x)?x.toFixed(d===undefined?1:d):"&ndash;";}
function put(id,h){document.getElementById(id).innerHTML=h;}
function bad(id,m){put(id,'<span class="flag-red">'+m+'</span>');}
var TR=" <em>Training result only; not a release decision.</em>";
function dt(id){var x=s(id);if(!x)return null;var d=new Date(x);return isNaN(d.getTime())?null:d;}
function fmt(d){return d.toLocaleString("en-US",{weekday:"short",month:"short",day:"numeric",year:"numeric",hour:"numeric",minute:"2-digit"});}

window.cnc1=function(){var b=v("c1b"),m=v("c1m"),fl=v("c1f");
 if(!isFinite(b)||b<=0){put("c1out","<span class='flag-amber'>HOLD.</span> The baseline is missing, zero or negative. Never substitute a catalog value; resolve the record first."+TR);return;}
 if(!isFinite(m)||m<0){bad("c1out","Enter a measured volume of zero or more.");return;}
 if(!isFinite(fl)||fl<=0||fl>100){bad("c1out","Enter the unit floor as a percentage between 1 and 100.");return;}
 var r=m/b*100,h="Retained TCV <strong>"+f(r,1)+"%</strong> ("+f(m,1)+" &divide; "+f(b,1)+" &times; 100).<br>";
 if(m>b)h+="<span class='flag-amber'>FLAG FOR REVIEW.</span> Measured volume is above baseline. Suspect a measurement or record error; do not accept or cap it.";
 else if(r<fl)h+="<span class='flag-red'>Below the "+f(fl,0)+"% floor.</span> The volume gate fails. Follow your procedure for disposition.";
 else h+="<span class='flag-green'>Meets the "+f(fl,0)+"% floor.</span> This is one gate only; every other gate must also pass.";
 if(m<=b&&r>=fl&&r<fl+3)h+="<br>Close to the floor: the dialyzer has lost about "+f(100-r,0)+"% of its blood compartment and may clean less than when new. Report a falling trend.";
 put("c1out",h+TR);};

window.cnc2=function(){var u=v("c2u"),c=v("c2c"),l=v("c2l");
 if(!isFinite(u)||u<0||Math.floor(u)!==u){bad("c2out","Enter completed uses as a whole number, 0 or more.");return;}
 if(!isFinite(c)||c<1){bad("c2out","Enter the payer ceiling as total uses.");return;}
 var lim=isFinite(l)&&l>=1?Math.min(c,l):c,nx=u+1,h=[];
 h.push("Next treatment would be <strong>use "+nx+"</strong> (the first treatment plus "+(nx-1)+" reuse"+(nx-1===1?"":"s")+"). Limit applied: <strong>"+lim+" total uses</strong>"+(isFinite(l)&&l>=1&&l<c?" (the IFU or facility limit is stricter than the payer ceiling)":"")+".");
 var fail=[],miss=[];
 if(nx>lim)fail.push("use limit reached");
 [["c2e","eligibility"],["c2t","TCV"],["c2i","integrity"],["c2v","inspection and processing record"]].forEach(function(g){var x=s(g[0]);if(x==="f")fail.push(g[1]+" failed");else if(x!=="p")miss.push(g[1]+" not recorded");});
 if(fail.length)h.push("<span class='flag-red'>NOT ELIGIBLE:</span> "+fail.join("; ")+". One failed gate stops the dialyzer, whatever the others show.");
 else if(miss.length)h.push("<span class='flag-amber'>HOLD:</span> "+miss.join("; ")+". Missing evidence is never treated as a pass.");
 else h.push("<span class='flag-green'>The gates entered here are recorded as passed.</span> Germicide, contact time, storage window, rinse, residual test and two-person verification still apply (Module 10).");
 put("c2out",h.join("<br>")+TR);};

window.cnc3=function(){var c1=v("c3s"),c2=v("c3t"),v2=v("c3v");
 if(!(c1>0)||!(c2>0)||!(v2>0)){bad("c3out","Enter the stock and target concentrations from the product IFU, and the final volume. All must be above zero.");return;}
 if(c2>=c1){bad("c3out","The target concentration must be lower than the stock concentration.");return;}
 var v1=c2*v2/c1,w=v2-v1;
 put("c3out","Measure <strong>"+f(v1,3)+" L</strong> of concentrate and make up to <strong>"+f(v2,2)+" L</strong> (about "+f(w,3)+" L of product water), in the order and manner the IFU sets.<br><span class='flag-amber'>Now mix and test potency.</span> The calculation cannot show whether the batch is evenly mixed or the stock has lost strength."+TR);};

window.cnc4=function(){var fi=dt("c4f"),c=v("c4c"),st=v("c4s"),u=dt("c4u");
 if(!fi){put("c4out","<span class='flag-amber'>HOLD.</span> No fill time: the dialyzer has no proven window."+TR);return;}
 if(!(c>=0)||!(st>0)){bad("c4out","Enter the minimum contact time (hours) and maximum storage (days) from the IFU and program.");return;}
 var e=new Date(fi.getTime()+c*3600000),x=new Date(fi.getTime()+st*86400000),h=[];
 if(x<=e){bad("c4out","Maximum storage must be longer than the minimum contact time. Check the values.");return;}
 h.push("Earliest use: <strong>"+fmt(e)+"</strong><br>Expiry: <strong>"+fmt(x)+"</strong>");
 if(u){if(u<e)h.push("<span class='flag-red'>Planned use is before the minimum contact time.</span> Not yet disinfected.");
  else if(u>x)h.push("<span class='flag-red'>Planned use is after expiry.</span> Outside the proven window; reprocess or discard per procedure.");
  else h.push("<span class='flag-green'>Planned use is inside the window.</span> Rinse, residual test and two-person verification still apply.");}
 put("c4out",h.join("<br>")+TR);};

window.cnc5=function(){var now=new Date(),h=[],worst=0;
 function band(val,act,max,label,unit){if(!isFinite(val)){h.push(label+": <span class='flag-amber'>no result entered</span>.");worst=Math.max(worst,1);return;}
  if(isFinite(max)&&val>max){h.push(label+" <strong>"+val+" "+unit+"</strong>: <span class='flag-red'>above the maximum</span>. Stop per program, report to the medical director&rsquo;s designate, follow the corrective-action plan.");worst=2;}
  else if(isFinite(act)&&val>=act){h.push(label+" <strong>"+val+" "+unit+"</strong>: <span class='flag-amber'>at or above the action level</span>. Report today; investigate and correct.");worst=Math.max(worst,1);}
  else h.push(label+" <strong>"+val+" "+unit+"</strong>: <span class='flag-green'>below the action level</span>.");}
 var t=v("c5t"),ta=v("c5ta");
 if(isFinite(t)&&isFinite(ta)&&t>ta){h.push("Product-water TDS <strong>"+t+" mg/L</strong>: <span class='flag-red'>above the corrective-action value of "+ta+" mg/L</span>. Corrective action must be documented before processing.");worst=2;}
 else if(isFinite(t))h.push("Product-water TDS <strong>"+t+" mg/L</strong>: <span class='flag-green'>within the corrective-action value</span>.");
 else{h.push("Product-water TDS: <span class='flag-amber'>no result entered</span>.");worst=Math.max(worst,1);}
 band(v("c5m"),v("c5ma"),v("c5ml"),"Microbiology","CFU/mL");
 band(v("c5e"),v("c5ea"),v("c5el"),"Endotoxin","EU/mL");
 var td=dt("c5td"),md=dt("c5md");
 if(td){var a=(now-td)/86400000;if(a>7){h.push("<span class='flag-red'>TDS reading is "+Math.floor(a)+" days old</span>; weekly testing is overdue.");worst=2;}}
 if(md){var b=(now-md)/86400000;if(b>31){h.push("<span class='flag-red'>Microbiology sample is "+Math.floor(b)+" days old</span>; monthly testing is overdue.");worst=2;}}
 h.push(worst===2?"<strong>Overall: red.</strong> Do not start processing until the person responsible for water clears it in writing.":(worst===1?"<strong>Overall: amber.</strong> Report and follow up today.":"<strong>Overall: green</strong> for the values entered."));
 put("c5out",h.join("<br>")+" <em>Training check only; this tool never clears water for use.</em>");};

window.cnc6=function(){var n=v("c6n"),t=v("c6t"),p=v("c6p"),r=v("c6r");
 if(!(n>0)||!(t>0)){bad("c6out","Enter dialyzers used and treatments delivered (both above zero).");return;}
 if(t<n){bad("c6out","Treatments cannot be fewer than dialyzers used; each dialyzer has at least one use.");return;}
 var labels=["failed TCV","failed integrity","clot or visual","use limit reached","expiry, time limit or record gap","other"],h=[],tot=0;
 h.push("Average uses per dialyzer: <strong>"+f(t/n,2)+"</strong>.");
 if(p>0){labels.forEach(function(L,i){var d=v("c6d"+(i+1));if(isFinite(d)&&d>0){tot+=d;h.push("Discards, "+L+": "+d+" ("+f(d/p*100,1)+"% of processing cycles)");}});
  h.push("All discards: <strong>"+tot+"</strong> ("+f(tot/p*100,1)+"% of processing cycles).");}
 else h.push("<span class='flag-amber'>Enter processing cycles to calculate discard rates.</span>");
 if(isFinite(r)&&r>=0){var rr=r/t*1000;h.push("Pyrogenic reactions: <strong>"+f(rr,2)+" per 1,000 treatments</strong>"+(r>0?" <span class='flag-amber'>&mdash; review every reaction and look for a cluster.</span>":"."));}
 h.push("<em>Average uses is a result, not a target. Read it beside discards and reactions.</em>");
 put("c6out",h.join("<br>"));};
})();
</script>"""

src = SRC.read_text(encoding="utf-8")
h = src
h = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", h, count=1, flags=re.S)
h = h.replace("calc-dialysis-charge-nurse-toolkit", "calc-reprocessing-technician-toolkit")
h = re.sub(r'<meta property="article:published_time"[^>]*>\n?', "", h)
h = re.sub(r'<meta property="article:modified_time" content="[^"]*">', '<meta property="article:modified_time" content="2026-11-25T00:00:00+08:00">', h)
for k in ("og:title", "twitter:title"):
    h = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', lambda m: f'<meta {m.group(1)}="{k}" content="{TITLE}">', h)
for k in ("og:description", "twitter:description", "description"):
    h = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', lambda m: f'<meta {m.group(1)}="{k}" content="{DESC}">', h)
h = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{KEYW}">', h)
h = h.replace("https://renalcarematters.com/images/og/dialysis-charge-nurse-vignette-hero.jpg", OG_IMG)
h = re.sub(r'<meta property="og:image:alt" content="[^"]*">', f'<meta property="og:image:alt" content="{OG_ALT}">', h)
h = h.replace('"name": "Dialysis Charge Nurse Toolkit: 8 Shift Calculators"', f'"name": "{TITLE}"')
hero = """<section class="hero">
<div class="container">
<div class="hero-tag">Renal Care Academy · Dialyzer Reprocessing Technician · Training Tools</div>
<h1>Reprocessing Technician <em>Toolkit</em></h1>
<p class="hero-sub">Six training calculators for the Renal Care Academy Dialyzer Reprocessing Technician track: total cell volume retained, a use counter with every acceptance gate, germicide dilution, the contact and storage window, a water log check, and a monthly reuse audit. Each one shows its formula and what the number does, and does not, tell you. None of them releases a dialyzer. Nothing you enter leaves this page.</p>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; <a href="../academy/dialyzer-reprocessing-technician.html" class="hero-xlink">Dialyzer Reprocessing Technician track</a></p>
</div>
</section>
<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#c1">TCV</a><a class="nav-pill" href="#c2">Use counter</a><a class="nav-pill" href="#c3">Dilution</a><a class="nav-pill" href="#c4">Storage clock</a><a class="nav-pill" href="#c5">Water log</a><a class="nav-pill" href="#c6">Audit</a>
</div>
</nav>"""
h = re.sub(r'<section class="hero">.*?</nav>', lambda m: hero, h, count=1, flags=re.S)
h = re.sub(r'(<main class="container cnc">).*?(</main>)', lambda m: m.group(1) + "\n" + SECTIONS + "\n" + m.group(2), h, count=1, flags=re.S)
h, n = re.subn(r"<script>\s*\(function\(\)\{\s*function v\(id\).*?window\.cnc8=.*?\}\)\(\);\s*</script>", lambda m: SCRIPT, h, count=1, flags=re.S)
assert n == 1, "calculator script not found"
assert "window.cnc8" not in h and "window.cnc7" not in h, "old calculator script still present"
rel = """<!-- RELATED-GUIDES-START -->
<div class="related-guides" id="related-guides">
  <h2>Related</h2>
  <div class="related-cards">
    <a class="related-card" href="../academy/dialyzer-reprocessing-technician.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Dialyzer Reprocessing Technician: the study track</div></a>
    <a class="related-card" href="dialyzer-reprocessing-reuse.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Dialyzer reprocessing and reuse</div></a>
    <a class="related-card" href="dialysis-water-treatment-systems.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Dialysis water treatment systems</div></a>
    <a class="related-card" href="calc-dialysis-water-reuse.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Dialysis water reuse calculator</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""
h = re.sub(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", lambda m: rel, h, count=1, flags=re.S)
h = h.replace('<a href="hemodialysis-complications.html" aria-label="Go to related guide">', '<a href="dialyzer-reprocessing-reuse.html" aria-label="Go to related guide">')
h = h.replace("cnc", "rtk")      # scoped class, style id and function names
assert "Charge Nurse Toolkit" not in h, "leftover Charge Nurse title"
OUT.write_text(h, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), len(h))
