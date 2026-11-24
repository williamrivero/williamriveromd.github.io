#!/usr/bin/env python3
"""Builds guides/calc-dialysis-charge-nurse-toolkit.html from the Head Nurse toolkit page (same chrome, CSS and scripts),
replacing the head, hero, table of contents, the calculator sections and the calculator script.
Run from the repo root:  python3 tools/techcourses/charge_nurse/build_toolkit.py
Then run the calculator patchers (build_calc_app.py, add_calc_nav_pill.py, patch_calc_handoff.py, patch_guide_rail.py,
patch_share_buttons.py, generate_latest_calculators.py)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "guides" / "calc-dialysis-head-nurse-toolkit.html"
OUT = ROOT / "guides" / "calc-dialysis-charge-nurse-toolkit.html"

TITLE = "Dialysis Charge Nurse Toolkit: 8 Shift Calculators"
DESC = ("Eight shift tools for dialysis charge nurses: station cover against the DOH limit, an acuity-weighted assignment, "
        "staggered breaks, lost patient-minutes, a heparin pump arithmetic check, a post-dialysis fall-risk screen, a "
        "pre-dialysis risk sorter with ultrafiltration rate, and an intradialytic pressure-drop tracker.")
KEYW = ("dialysis charge nurse calculator, hemodialysis assignment acuity, nurse break planner, dialysis station ratio DOH, "
        "heparin pump rate check, Morse fall scale dialysis, ultrafiltration rate, intradialytic hypotension calculator")
OG_IMG = "https://renalcarematters.com/images/og/dialysis-charge-nurse-vignette-hero.jpg"
OG_ALT = "A charge nurse at the center of a dialysis unit at dawn directing staff to their stations"

SECTIONS = r"""
<nav class="toc" aria-label="Calculators">
<a href="#c1">1 Station cover</a><a href="#c2">2 Assignment balance</a><a href="#c3">3 Breaks</a><a href="#c4">4 Lost minutes</a><a href="#c5">5 Heparin pump check</a><a href="#c6">6 Fall risk</a><a href="#c7">7 Risk sorter</a><a href="#c8">8 Pressure drop</a>
</nav>
<div class="notice" role="note"><b>A teaching and checking aid.</b> These tools do not authorize staffing, prescribe treatment, or replace your unit&rsquo;s protocol. Values that set limits are entered by your unit. Use synthetic or de-identified data only; nothing you enter leaves this page. Where the protocol is silent, ask the attending nephrologist.</div>

<section class="calc" id="c1" aria-labelledby="h1">
<h2 id="h1">1 · Station cover check</h2>
<p class="mod">Modules 01, 03</p>
<div class="grid">
<div><label for="c1st">Stations running this shift</label><input id="c1st" type="number" min="0" value="16" placeholder="e.g. 16"></div>
<div><label for="c1n">Nurses who can work alone (including the charge nurse)</label><input id="c1n" type="number" min="0" value="4" placeholder="e.g. 4"></div>
<div><label for="c1cn">Chairs the charge nurse carries herself</label><input id="c1cn" type="number" min="0" value="2" placeholder="e.g. 2"></div>
<div><label for="c1or">Orientees on the floor (not counted)</label><input id="c1or" type="number" min="0" value="0" placeholder="e.g. 1"></div>
<div><label for="c1lim">Stations per nurse limit (unit setting; DOH AO 2012-0001 is 4)</label><input id="c1lim" type="number" min="1" value="4" placeholder="e.g. 4"></div>
<div><label for="c1br">Nurses on break at the same time (worst window)</label><input id="c1br" type="number" min="0" value="1" placeholder="e.g. 1"></div>
</div>
<button type="button" onclick="cnc1()">Check</button>
<div class="out" id="c1out" aria-live="polite"></div>
<p class="why"><b>Formula.</b> Stations left for staff nurses = stations &minus; charge nurse&rsquo;s own chairs. Per staff nurse now = that number &divide; (nurses &minus; 1). Worst break window = same stations &divide; (nurses &minus; 1 &minus; nurses on break). <b>Rules shown side by side.</b> DOH AO 2012-0001: no more than 1 nurse to 4 stations per shift, a licensing condition. PSN 2024: 1 nurse to 4 patients, or 1 to 6 with a nursing assistant, professional guidance. This tool checks against the limit you enter and never reports a staffing level as authorized.</p>
</section>

<section class="calc" id="c2" aria-labelledby="h2">
<h2 id="h2">2 · Acuity-weighted assignment balance</h2>
<p class="mod">Module 03</p>
<label for="c2d">One patient per line: nurse, then any tags (stable, catheter, newaccess, hypo, isolation, help, transfusion). Example: <em>Arnel, catheter</em></label>
<textarea id="c2d">Arnel, catheter
Arnel, catheter
Arnel, stable
Kris, stable, hypo
Kris, stable, help
Kris, stable
Kris, stable
Mika, stable
Mika, stable
Mika, stable
Mika, stable
Joy, stable, isolation</textarea>
<div class="grid">
<div><label for="c2nc">Nurses NOT signed off for catheters (comma-separated)</label><input id="c2nc" type="text" value="Mika" placeholder="e.g. Mika"></div>
<div><label for="c2cap">Orientee point cap (optional)</label><input id="c2cap" type="number" min="0" value="5" placeholder="e.g. 5"></div>
<div><label for="c2ori">Orientees (comma-separated)</label><input id="c2ori" type="text" value="Mika" placeholder="e.g. Mika"></div>
</div>
<button type="button" onclick="cnc2()">Balance</button>
<div class="out" id="c2out" aria-live="polite"></div>
<p class="why"><b>Example scale</b> (edit to your unit): stable 1; catheter 3 instead of 1; new or problem access +1; frequent low pressure or arrhythmia +2; isolation +2; needs help walking, confused, or new to dialysis +1; transfusion or IV medicine +1. <b>Honest limit.</b> No acuity tool for outpatient hemodialysis has been shown in trials to improve outcomes. Points make load visible; judgment decides.</p>
</section>

<section class="calc" id="c3" aria-labelledby="h3">
<h2 id="h3">3 · Staggered break planner</h2>
<p class="mod">Module 03</p>
<div class="grid">
<div><label for="c3first">Last connection finishes</label><input id="c3first" type="time" value="06:45"></div>
<div><label for="c3last">First disconnection starts</label><input id="c3last" type="time" value="10:00"></div>
<div><label for="c3len">Break length (minutes)</label><input id="c3len" type="number" min="5" value="30" placeholder="e.g. 30"></div>
<div><label for="c3names">Nurses in break order (comma-separated)</label><input id="c3names" type="text" value="Mika, Arnel, Kris, Joy" placeholder="e.g. Mika, Arnel"></div>
<div><label for="c3buf">Protected window after connection and before disconnection (minutes)</label><input id="c3buf" type="number" min="0" value="30" placeholder="e.g. 30"></div>
</div>
<button type="button" onclick="cnc3()">Plan</button>
<div class="out" id="c3out" aria-live="polite"></div>
<p class="why"><b>Rule.</b> One break at a time, never inside the protected windows after the last connection or before the first disconnection, when most low-pressure, needle, and bleeding problems happen. Check the worst window with tool 1.</p>
</section>

<section class="calc" id="c4" aria-labelledby="h4">
<h2 id="h4">4 · Late starts and lost patient-minutes</h2>
<p class="mod">Modules 02, 06, 17</p>
<label for="c4d">One patient per line: minutes started late, minutes stopped early, minutes paused by alarms (for example: 15, 0, 5)</label>
<textarea id="c4d">15, 0, 0
15, 0, 0
20, 0, 5
10, 15, 0
15, 0, 0</textarea>
<div class="grid">
<div><label for="c4sess">Prescribed session (minutes)</label><input id="c4sess" type="number" min="1" value="240" placeholder="e.g. 240"></div>
<div><label for="c4per">Same pattern repeats how many shifts a week</label><input id="c4per" type="number" min="0" value="6" placeholder="e.g. 6"></div>
</div>
<button type="button" onclick="cnc4()">Count</button>
<div class="out" id="c4out" aria-live="polite"></div>
<p class="why"><b>Why.</b> Delivered time drives dialysis dose; shortened and missed sessions were associated with higher mortality in DOPPS (Dialysis Outcomes and Practice Patterns Study) data. Minutes added back at the end are not lost; this tool counts what was not added back.</p>
</section>

<section class="calc" id="c5" aria-labelledby="h5">
<h2 id="h5">5 · Heparin pump arithmetic check</h2>
<p class="mod">Module 09</p>
<div class="grid">
<div><label for="c5r">Ordered rate (units per hour, from the current order)</label><input id="c5r" type="number" step="any" min="0" value="1000" placeholder="e.g. 1000"></div>
<div><label for="c5c">Syringe concentration (units per mL)</label><input id="c5c" type="number" step="any" min="0" value="1000" placeholder="e.g. 1000"></div>
<div><label for="c5h">Infusion hours</label><input id="c5h" type="number" step="any" min="0" value="4" placeholder="e.g. 4"></div>
<div><label for="c5lo">Unit plausible pump range, low (mL/h)</label><input id="c5lo" type="number" step="any" min="0" placeholder="unit setting"></div>
<div><label for="c5hi">Unit plausible pump range, high (mL/h)</label><input id="c5hi" type="number" step="any" min="0" placeholder="unit setting"></div>
</div>
<button type="button" onclick="cnc5()">Check</button>
<div class="out" id="c5out" aria-live="polite"></div>
<p class="why"><b>Formula.</b> Pump rate (mL/h) = ordered units per hour &divide; syringe units per mL. Total units = units per hour &times; hours. <b>This is a plausibility check, not a dose.</b> The dose is the prescriber&rsquo;s. Any mismatch with a second nurse&rsquo;s independent calculation, or a result ten times larger or smaller than usual, means stop and check the order.</p>
</section>

<section class="calc" id="c6" aria-labelledby="h6">
<h2 id="h6">6 · Post-dialysis fall-risk screen</h2>
<p class="mod">Modules 05, 07</p>
<div class="grid">
<div><label for="c6a">History of falling (last 3 months)</label><select id="c6a"><option value="0">No (0)</option><option value="25">Yes (25)</option></select></div>
<div><label for="c6b">More than one medical diagnosis</label><select id="c6b"><option value="0">No (0)</option><option value="15" selected>Yes (15)</option></select></div>
<div><label for="c6c">Walking aid</label><select id="c6c"><option value="0">None, bed rest, or nurse assists (0)</option><option value="15">Crutches, cane, or walker (15)</option><option value="30">Holds on to furniture (30)</option></select></div>
<div><label for="c6d">Intravenous line or heparin lock</label><select id="c6d"><option value="0">No (0)</option><option value="20">Yes (20)</option></select></div>
<div><label for="c6e">Gait</label><select id="c6e"><option value="0">Normal, bed rest, or wheelchair (0)</option><option value="10">Weak (10)</option><option value="20">Impaired (20)</option></select></div>
<div><label for="c6f">Mental status</label><select id="c6f"><option value="0">Knows own limits (0)</option><option value="15">Overestimates or forgets limits (15)</option></select></div>
</div>
<div class="grid">
<div><label for="c6g">Systolic pressure fell to below the patient&rsquo;s usual after dialysis</label><select id="c6g"><option value="0">No</option><option value="1">Yes</option></select></div>
<div><label for="c6h">New or increased blood pressure medicine</label><select id="c6h"><option value="0">No</option><option value="1">Yes</option></select></div>
<div><label for="c6i">Fell after a previous session</label><select id="c6i"><option value="0">No</option><option value="1">Yes</option></select></div>
</div>
<button type="button" onclick="cnc6()">Score</button>
<div class="out" id="c6out" aria-live="polite"></div>
<p class="why"><b>Morse Fall Scale</b> (Morse 1989): six items, 0 to 125. Commonly used bands: 0&ndash;24 low, 25&ndash;44 moderate, 45 or more high; units set their own. <b>Limit.</b> Morse was developed in hospital inpatients and is not validated specifically for hemodialysis; use it as a prompt. Older patients on hemodialysis fell about 1.6 times per person-year in a prospective cohort (Cook 2006). The three dialysis prompts are not scored; any &ldquo;yes&rdquo; means walk beside the patient and check standing pressure if your protocol asks.</p>
</section>

<section class="calc" id="c7" aria-labelledby="h7">
<h2 id="h7">7 · Pre-dialysis risk sorter and ultrafiltration rate</h2>
<p class="mod">Module 05</p>
<fieldset style="border:0;padding:0;margin:0 0 8px"><legend style="font-size:.9rem;color:var(--text-mid);margin-bottom:6px">Tick every finding present</legend>
<div class="grid">
<label><input type="checkbox" id="c7n1"> Breathless lying flat or new breathlessness</label>
<label><input type="checkbox" id="c7n2"> Chest pain or palpitations</label>
<label><input type="checkbox" id="c7n3"> New confusion or drowsiness</label>
<label><input type="checkbox" id="c7n4"> Potassium above the unit&rsquo;s critical value with no documented plan</label>
<label><input type="checkbox" id="c7n5"> Fever or chills with a catheter</label>
<label><input type="checkbox" id="c7n6"> Cold, pale, or painful access hand</label>
<label><input type="checkbox" id="c7t1"> Weight gain above the unit&rsquo;s threshold</label>
<label><input type="checkbox" id="c7t2"> Pressure well above or below the patient&rsquo;s usual</label>
<label><input type="checkbox" id="c7t3"> Missed medicines</label>
<label><input type="checkbox" id="c7t4"> Fall since the last session</label>
<label><input type="checkbox" id="c7t5"> Took insulin or a sulfonylurea without eating</label>
<label><input type="checkbox" id="c7m1"> Weight trend slowly rising over weeks</label>
<label><input type="checkbox" id="c7m2"> Poor appetite or low mood</label>
<label><input type="checkbox" id="c7m3"> Transport or cost problems</label>
</div></fieldset>
<div class="grid">
<div><label for="c7w">Dry weight (kg)</label><input id="c7w" type="number" step="any" value="62" placeholder="e.g. 62"></div>
<div><label for="c7v">Planned removal (L)</label><input id="c7v" type="number" step="any" value="4.1" placeholder="e.g. 4.1"></div>
<div><label for="c7h">Planned time (hours)</label><input id="c7h" type="number" step="any" value="4" placeholder="e.g. 4"></div>
</div>
<button type="button" onclick="cnc7()">Sort</button>
<div class="out" id="c7out" aria-live="polite"></div>
<p class="why"><b>Lanes.</b> Now: call the physician before connection. Today: tell the physician during this session. This month: route to the attending or team. <b>Rate.</b> UFR (ultrafiltration rate) = mL &divide; hours &divide; kg. Above 13 mL/kg/h was associated with higher all-cause and cardiovascular mortality in an observational cohort (Flythe 2011); no trial has shown that capping the rate saves lives. Thresholds for potassium and weight gain are your unit&rsquo;s. The fluid goal is the prescriber&rsquo;s.</p>
</section>

<section class="calc" id="c8" aria-labelledby="h8">
<h2 id="h8">8 · Intradialytic pressure-drop tracker</h2>
<p class="mod">Module 07</p>
<div class="grid">
<div><label for="c8ps">Pre-dialysis systolic (mm Hg)</label><input id="c8ps" type="number" value="138" placeholder="e.g. 138"></div>
<div><label for="c8pd">Pre-dialysis diastolic (mm Hg)</label><input id="c8pd" type="number" value="70" placeholder="e.g. 70"></div>
<div><label for="c8cs">Current systolic (mm Hg)</label><input id="c8cs" type="number" value="92" placeholder="e.g. 92"></div>
<div><label for="c8cd">Current diastolic (mm Hg)</label><input id="c8cd" type="number" value="50" placeholder="e.g. 50"></div>
<div><label for="c8sy">Symptoms (dizzy, cramping, yawning, nausea, drowsy)</label><select id="c8sy"><option value="1">Yes</option><option value="0">No</option></select></div>
<div><label for="c8uf">Fluid removed so far (L)</label><input id="c8uf" type="number" step="any" value="1.6" placeholder="e.g. 1.6"></div>
<div><label for="c8t">Time on dialysis so far (hours)</label><input id="c8t" type="number" step="any" value="2.33" placeholder="e.g. 2.33"></div>
<div><label for="c8w">Dry weight (kg)</label><input id="c8w" type="number" step="any" value="48" placeholder="e.g. 48"></div>
</div>
<button type="button" onclick="cnc8()">Check</button>
<div class="out" id="c8out" aria-live="polite"></div>
<p class="why"><b>Definitions.</b> European Best Practice Guideline: a fall in systolic pressure of 20 mm Hg or more, or in mean arterial pressure of 10 mm Hg or more, with symptoms or a need for nursing intervention. In a large cohort, a nadir below 90 mm Hg (below 100 if the session started at 160 or more) was most strongly associated with death (Flythe 2015). Mean arterial pressure = diastolic + (systolic &minus; diastolic) &divide; 3. <b>First response</b> follows your unit&rsquo;s protocol; always ask the attending nephrologist for guidance. Check glucose in any drowsy patient on insulin or a sulfonylurea.</p>
</section>
<div class="disclaimer"><strong>Important:</strong> These tools do arithmetic, not decisions. They do not authorize staffing or replace your unit&rsquo;s protocols, current regulations, or the attending nephrologist, who is always asked for guidance. Draft, reviewed November 24, 2026.</div>
"""

SCRIPT = r"""<script>
(function(){
function v(id){var e=document.getElementById(id);if(!e)return NaN;var x=String(e.value).trim();return x===""?NaN:Number(x);}
function s(id){var e=document.getElementById(id);return e?String(e.value).trim():"";}
function ck(id){var e=document.getElementById(id);return !!(e&&e.checked);}
function f(x,d){return isFinite(x)?x.toFixed(d===undefined?1:d):"&ndash;";}
function put(id,h){document.getElementById(id).innerHTML=h;}
function bad(id,m){put(id,'<span class="flag-red">'+m+'</span>');}
function esc(t){return t.replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
function list(t){return t.split(",").map(function(x){return x.trim().toLowerCase();}).filter(Boolean);}
function mins(t){var m=/^(\d{1,2}):(\d{2})$/.exec(t);return m?(+m[1])*60+(+m[2]):NaN;}
function hhmm(x){x=((x%1440)+1440)%1440;var h=Math.floor(x/60),m=x%60;return (h<10?"0":"")+h+":"+(m<10?"0":"")+m;}

window.cnc1=function(){var st=v("c1st"),n=v("c1n"),cn=v("c1cn"),or=v("c1or"),lim=v("c1lim"),br=v("c1br");
 if(!(st>=0&&n>=1&&cn>=0&&lim>=1&&br>=0))return bad("c1out","Check inputs: at least one nurse and a limit of 1 or more.");
 if(cn>st)return bad("c1out","The charge nurse cannot carry more chairs than are running.");
 var flat=st/n,rest=st-cn,staff=n-1,h=[];
 h.push("Simple count: <strong>"+f(flat,2)+"</strong> stations per nurse ("+st+" &divide; "+n+") against a limit of "+lim+".");
 if(staff<1){h.push(rest>0?"<span class='flag-red'>Only the charge nurse is counted, but "+rest+" stations are left for other nurses.</span>":"Only the charge nurse is on the floor.");}
 else{var now=rest/staff,cls=now>lim?"flag-red":"flag-green";
  h.push("With the charge nurse carrying "+cn+": <strong class='"+cls+"'>"+f(now,2)+"</strong> stations per staff nurse ("+rest+" &divide; "+staff+").");
  var onfloor=staff-br;
  if(br>0){if(onfloor<1)h.push("<span class='flag-red'>In the break window no staff nurse is left for "+rest+" stations.</span>");
   else{var bw=rest/onfloor;h.push("Worst break window ("+br+" on break): <strong class='"+(bw>lim?"flag-red":"flag-green")+"'>"+f(bw,2)+"</strong> stations per staff nurse.");}}
  if(now>lim)h.push("<span class='flag-red'>Above the limit you entered. Hold the extra stations and escalate: hazard, protection now, help needed, recheck time.</span>");}
 if(or>0)h.push("Orientees ("+or+") are not counted toward the limit.");
 h.push("<span style='font-size:.86rem'>Shown for information: PSN 2024 counts patients (1:4, or 1:6 with a nursing assistant). It does not amend the DOH licensing condition. This tool never reports a staffing level as authorized.</span>");
 put("c1out",h.join("<br>"));};

var PTS={stable:1,catheter:3,newaccess:1,hypo:2,isolation:2,help:1,transfusion:1};
window.cnc2=function(){var lines=s("c2d").split(/\n/).map(function(l){return l.trim();}).filter(Boolean);
 if(!lines.length)return bad("c2out","Enter one patient per line.");
 var noc=list(s("c2nc")),ori=list(s("c2ori")),cap=v("c2cap"),N={},order=[],warn=[];
 lines.forEach(function(l,i){var p=l.split(",").map(function(x){return x.trim();}),nm=p[0];if(!nm)return;var key=nm.toLowerCase();
  var tags=p.slice(1).map(function(x){return x.toLowerCase();}),pts=tags.indexOf("catheter")>=0?3:1;
  tags.forEach(function(t){if(t!=="stable"&&t!=="catheter"&&PTS[t])pts+=PTS[t];});
  if(!N[key]){N[key]={name:nm,pts:0,pats:0};order.push(key);}N[key].pts+=pts;N[key].pats++;
  if(tags.indexOf("catheter")>=0&&noc.indexOf(key)>=0)warn.push("Line "+(i+1)+": "+esc(nm)+" has a catheter patient but is not signed off for catheters.");});
 var tot=0,max=-1,min=1e9,rows="";
 order.forEach(function(k){var x=N[k];tot+=x.pts;max=Math.max(max,x.pts);min=Math.min(min,x.pts);
  var flag=(ori.indexOf(k)>=0&&cap>0&&x.pts>cap)?" <span class='flag-amber'>above orientee cap</span>":"";
  rows+="<tr><td>"+esc(x.name)+"</td><td>"+x.pats+"</td><td>"+x.pts+flag+"</td></tr>";});
 var h="<table class='res'><tr><th>Nurse</th><th>Patients</th><th>Points</th></tr>"+rows+"</table>";
 h+="Total <strong>"+tot+"</strong> points · spread (highest minus lowest) <strong>"+(max-min)+"</strong>.";
 if(warn.length)h+="<br><span class='flag-red'>"+warn.join("<br>")+"</span>";
 put("c2out",h);};

window.cnc3=function(){var a=mins(s("c3first")),b=mins(s("c3last")),len=v("c3len"),buf=v("c3buf"),names=s("c3names").split(",").map(function(x){return x.trim();}).filter(Boolean);
 if(!(isFinite(a)&&isFinite(b)&&len>0&&buf>=0&&names.length))return bad("c3out","Enter both times, a break length, and at least one nurse.");
 if(b<=a)b+=1440;
 var start=a+buf,end=b-buf,need=names.length*len;
 if(end-start<need)return bad("c3out","Not enough protected time: "+(end-start)+" minutes available for "+need+" minutes of breaks. Shorten breaks, use a relief nurse, or plan some breaks after disconnection.");
 var gap=Math.floor(((end-start)-need)/(names.length+1)),t=start+gap,rows="";
 names.forEach(function(nm,i){rows+="<tr><td>"+esc(nm)+"</td><td>"+hhmm(t)+"&ndash;"+hhmm(t+len)+"</td><td>"+esc(names[(i+1)%names.length])+"</td></tr>";t+=len+gap;});
 put("c3out","Protected window: breaks only between <strong>"+hhmm(start)+"</strong> and <strong>"+hhmm(end)+"</strong>.<table class='res'><tr><th>Nurse</th><th>Break</th><th>Suggested cover</th></tr>"+rows+"</table>Write it on the board at assignment time. Check the worst window in tool 1.");};

window.cnc4=function(){var lines=s("c4d").split(/\n/).map(function(l){return l.trim();}).filter(Boolean),sess=v("c4sess"),per=v("c4per");
 if(!lines.length||!(sess>0))return bad("c4out","Enter one patient per line and the session length.");
 var tot=0,n=0;
 for(var i=0;i<lines.length;i++){var p=lines[i].split(",").map(Number);if(p.some(function(x){return !(x>=0);}))return bad("c4out","Line "+(i+1)+": use three numbers zero or more.");tot+=p[0]+(p[1]||0)+(p[2]||0);n++;}
 var h="Lost this shift: <strong>"+tot+" patient-minutes</strong> across "+n+" patients ("+f(tot/sess,2)+" full sessions).";
 if(per>0){var wk=tot*per,yr=wk*52;h+="<br>If the pattern repeats "+per+" shifts a week: <strong>"+f(wk/60,1)+" hours a week</strong>, about <strong>"+f(yr/sess,0)+" full sessions a year</strong> for the unit.";}
 h+="<br>Minutes you add back at the end are not lost. Count only those not given back.";
 put("c4out",h);};

window.cnc5=function(){var r=v("c5r"),c=v("c5c"),h=v("c5h"),lo=v("c5lo"),hi=v("c5hi");
 if(!(r>=0&&c>0&&h>0))return bad("c5out","Enter the ordered rate, a concentration above zero, and the hours.");
 var ml=r/c,units=r*h,vol=ml*h,out="Pump rate <strong>"+f(ml,2)+" mL/h</strong> · total <strong>"+Math.round(units).toLocaleString("en-US")+" units</strong> in <strong>"+f(vol,1)+" mL</strong> over "+f(h,2).replace(/\.?0+$/,"")+" h.";
 if(isFinite(lo)&&isFinite(hi)&&hi>0){out+=(ml<lo||ml>hi)?"<br><span class='flag-amber'>Outside your unit&rsquo;s plausible range ("+lo+"&ndash;"+hi+" mL/h). Stop and check the order and the syringe.</span>":"<br><span class='flag-green'>Inside your unit&rsquo;s plausible range.</span>";}
 out+="<br>Have a second nurse calculate independently from the current order before comparing. A tenfold difference means stop and check.";
 put("c5out",out);};

window.cnc6=function(){var t=["c6a","c6b","c6c","c6d","c6e","c6f"].reduce(function(a,id){return a+v(id);},0);
 var band=t>=45?"<span class='flag-red'>high</span>":(t>=25?"<span class='flag-amber'>moderate</span>":"<span class='flag-green'>low</span>");
 var d=[];if(v("c6g")===1)d.push("pressure below usual after dialysis");if(v("c6h")===1)d.push("new or increased blood pressure medicine");if(v("c6i")===1)d.push("fell after a previous session");
 put("c6out","Morse total <strong>"+t+"</strong> of 125 · commonly used band: <strong>"+band+"</strong>."+(d.length?"<br><span class='flag-amber'>Dialysis prompts: "+d.join("; ")+". Walk beside the patient to the door; sit up slowly; check standing pressure if your protocol asks.</span>":"")+"<br>A prompt, not a validated hemodialysis score.");};

window.cnc7=function(){var now=[],today=[],month=[],L={c7n1:"breathless lying flat or new breathlessness",c7n2:"chest pain or palpitations",c7n3:"new confusion or drowsiness",c7n4:"critical potassium with no documented plan",c7n5:"fever or chills with a catheter",c7n6:"cold, pale, or painful access hand",c7t1:"weight gain above threshold",c7t2:"pressure well off the usual",c7t3:"missed medicines",c7t4:"fall since last session",c7t5:"insulin or sulfonylurea without food",c7m1:"slowly rising weight trend",c7m2:"poor appetite or low mood",c7m3:"transport or cost problems"};
 Object.keys(L).forEach(function(k){if(ck(k)){(k.charAt(2)==="n"?now:(k.charAt(2)==="t"?today:month)).push(L[k]);}});
 var w=v("c7w"),vol=v("c7v"),h=v("c7h"),out="";
 out+=now.length?"<span class='flag-red'>Now (call before connection):</span> "+now.join("; ")+"<br>":"";
 out+=today.length?"<span class='flag-amber'>Today (tell the physician this session):</span> "+today.join("; ")+"<br>":"";
 out+=month.length?"This month (route to the team): "+month.join("; ")+"<br>":"";
 if(!(now.length||today.length||month.length))out+="No findings ticked.<br>";
 if(w>0&&vol>=0&&h>0){var r=vol*1000/h/w,mx=13*w*h,cls=r>13?"flag-red":(r>10?"flag-amber":"flag-green");
  out+="Planned UFR <strong class='"+cls+"'>"+f(r,1)+" mL/kg/h</strong>. At "+f(h,2).replace(/\.?0+$/,"")+" h, removal at or below 13 mL/kg/h is up to <strong>"+Math.round(mx).toLocaleString("en-US")+" mL</strong>; the same "+f(vol,1)+" L at or below 13 needs at least <strong>"+f(vol*1000/13/w,1)+" h</strong>.";
  if(r>13)out+=" Raise with the prescriber before connection.";}
 if(now.length)out+="<br><b>SBAR (Situation, Background, Assessment, Recommendation) starter:</b> &ldquo;I am calling about a patient before connection with "+now.join(", ")+(w>0&&vol>=0&&h>0?"; the planned UFR is "+f(vol*1000/h/w,1)+" mL/kg/h":"")+". I need a decision before we start.&rdquo;";
 put("c7out",out);};

window.cnc8=function(){var ps=v("c8ps"),pd=v("c8pd"),cs=v("c8cs"),cd=v("c8cd"),sy=v("c8sy"),uf=v("c8uf"),t=v("c8t"),w=v("c8w");
 if(!(ps>0&&pd>0&&cs>0&&cd>0))return bad("c8out","Enter both pressure pairs.");
 var drop=ps-cs,pct=drop/ps*100,m1=pd+(ps-pd)/3,m2=cd+(cs-cd)/3,md=m1-m2,ebpg=(drop>=20||md>=10)&&sy===1,nad=ps>=160?100:90,low=cs<nad,h=[];
 h.push("Systolic fall <strong>"+drop+" mm Hg</strong> ("+f(pct,1)+"%) · mean arterial pressure "+f(m1,1)+" &rarr; "+f(m2,1)+" (fall <strong>"+f(md,1)+"</strong>).");
 h.push(ebpg?"<span class='flag-red'>Meets the EBPG definition (with symptoms).</span>":((drop>=20||md>=10)?"<span class='flag-amber'>Meets the pressure part of the EBPG definition; watch for symptoms.</span>":"Does not meet the EBPG pressure criterion."));
 h.push(low?"<span class='flag-red'>Below the nadir flag of "+nad+" mm Hg.</span>":"Above the nadir flag of "+nad+" mm Hg.");
 if(uf>=0&&t>0&&w>0){var r=uf*1000/t/w;h.push("Ultrafiltration so far <strong class='"+(r>13?"flag-red":(r>10?"flag-amber":"flag-green"))+"'>"+f(r,1)+" mL/kg/h</strong>.");}
 if(ebpg||low)h.push("First response per your unit&rsquo;s protocol: stop or reduce fluid removal, lay flat if breathing allows, check access, lines, and glucose, recheck; call the physician if not better in minutes or if there is chest pain, a new rhythm, or confusion. Always ask the attending nephrologist for guidance.");
 put("c8out",h.join("<br>"));};
})();
</script>"""

src = SRC.read_text(encoding="utf-8")
h = src
# head
h = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", h, count=1, flags=re.S)
h = h.replace("calc-dialysis-head-nurse-toolkit", "calc-dialysis-charge-nurse-toolkit")
h = re.sub(r'<meta property="article:published_time"[^>]*>\n?', "", h)
h = re.sub(r'<meta property="article:modified_time" content="[^"]*">', '<meta property="article:modified_time" content="2026-11-24T00:00:00+08:00">', h)
for k in ("og:title", "twitter:title"):
    h = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', lambda m: f'<meta {m.group(1)}="{k}" content="{TITLE}">', h)
for k in ("og:description", "twitter:description", "description"):
    h = re.sub(rf'<meta (property|name)="{k}" content="[^"]*">', lambda m: f'<meta {m.group(1)}="{k}" content="{DESC}">', h)
h = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{KEYW}">', h)
h = h.replace("https://renalcarematters.com/images/og/dialysis-head-nurse-vignette-hero.jpg", OG_IMG)
h = re.sub(r'<meta property="og:image:alt" content="[^"]*">', f'<meta property="og:image:alt" content="{OG_ALT}">', h)
h = h.replace('"name": "Dialysis Head Nurse Toolkit: 13 Calculators"', f'"name": "{TITLE}"')
# hero
hero = f"""<section class="hero">
<div class="container">
<div class="hero-tag">Renal Care Academy · Dialysis Charge Nurse · Shift Tools</div>
<h1>Dialysis Charge Nurse <em>Toolkit</em></h1>
<p class="hero-sub">Eight working tools for the Renal Care Academy Dialysis Charge Nurse track: station cover, assignment balance, breaks, lost minutes, a heparin pump check, fall risk, a pre-dialysis risk sorter, and a pressure-drop tracker. Each one shows its formula and what the number does, and does not, tell you. Clinical decisions stay with the prescriber and your unit&rsquo;s protocol; always ask the attending nephrologist for guidance. Nothing you enter leaves this page.</p>
<p style="margin:14px 0 0;font-size:.9rem;"><a href="calculators.html" class="hero-xlink">← All calculators &amp; tools</a> &nbsp;·&nbsp; <a href="../academy/dialysis-charge-nurse.html" class="hero-xlink">Dialysis Charge Nurse track</a></p>
</div>
</section>
<nav class="nav-strip">
<div class="nav-pills">
<a class="nav-pill" href="#c1">Station cover</a><a class="nav-pill" href="#c2">Assignment</a><a class="nav-pill" href="#c3">Breaks</a><a class="nav-pill" href="#c7">Risk sorter</a><a class="nav-pill" href="#c8">Pressure drop</a>
</div>
</nav>"""
h = re.sub(r'<section class="hero">.*?</nav>', hero, h, count=1, flags=re.S)
# sections
h = re.sub(r'(<main class="container hnc">).*?(</main>)', lambda m: m.group(1) + "\n" + SECTIONS + "\n" + m.group(2), h, count=1, flags=re.S)
# script: replace the calculator IIFE (the one defining window.hnc1)
h = re.sub(r"<script>\s*\(function\(\)\{\s*function v\(id\).*?window\.hnc13=.*?\}\)\(\);\s*</script>", lambda m: SCRIPT, h, count=1, flags=re.S)
assert "window.hnc" not in h, "old calculator script still present"
# related
rel = """<!-- RELATED-GUIDES-START -->
<div class="related-guides" id="related-guides">
  <h2>Related</h2>
  <div class="related-cards">
    <a class="related-card" href="../academy/dialysis-charge-nurse.html"><div class="related-card-tag">Academy</div><div class="related-card-title">Dialysis Charge Nurse: the study track</div></a>
    <a class="related-card" href="calc-dialysis-head-nurse-toolkit.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">Dialysis Head Nurse Toolkit</div></a>
    <a class="related-card" href="calc-hd-session-review.html"><div class="related-card-tag">Calculator</div><div class="related-card-title">HD Session Hemodynamic Review</div></a>
    <a class="related-card" href="hemodialysis-complications.html"><div class="related-card-tag">Guide</div><div class="related-card-title">Hemodialysis complications</div></a>
  </div>
</div>
<!-- RELATED-GUIDES-END -->"""
h = re.sub(r"<!-- RELATED-GUIDES-START -->.*?<!-- RELATED-GUIDES-END -->", lambda m: rel, h, count=1, flags=re.S)
h = h.replace("hnc", "cnc")      # scoped class and style id
assert "Head Nurse Toolkit" in h  # only in the related card
OUT.write_text(h, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), len(h))
