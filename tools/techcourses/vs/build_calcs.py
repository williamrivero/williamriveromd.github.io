#!/usr/bin/env python3
"""Build the three Vascular Surgeon track calculators from the calc-abi.html shell (house calculator layout).

    python3 tools/techcourses/vs/build_calcs.py

Writes guides/calc-av-fistula-maturation.html, guides/calc-hand-ischemia-dbi.html and guides/calc-av-access-outcome-audit.html.
Idempotent: each page is rebuilt from the shell every run. Then run the calculator pipeline (see the track README).
Sources are PubMed-verified (November 25, 2026); see tools/techcourses/vs/refs.py.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
G = ROOT / "guides"
SHELL = G / "calc-abi.html"


def apa(key):
    import importlib.util
    spec = importlib.util.spec_from_file_location("vsrefs", Path(__file__).resolve().parent / "refs.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.REFS[key]


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def field(fid, label, hint, ph, mn="0", mx="100000", step="any", fn="run()"):
    return (f'    <div class="calc-field">\n      <label for="{fid}">{label}</label>\n'
            f'      <input type="number" id="{fid}" min="{mn}" max="{mx}" step="{step}" placeholder="e.g. {ph}" oninput="{fn}">\n'
            f'      <div class="field-hint">{hint}</div>\n    </div>')


def select(fid, label, hint, opts, fn="run()"):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return (f'    <div class="calc-field">\n      <label for="{fid}">{label}</label>\n'
            f'      <select id="{fid}" onchange="{fn}">{o}</select>\n      <div class="field-hint">{hint}</div>\n    </div>')


def check(fid, label, fn="run()"):
    return (f'    <div class="calc-field">\n      <label style="display:flex;gap:8px;align-items:flex-start;font-weight:500;">'
            f'<input type="checkbox" id="{fid}" onchange="{fn}" style="width:auto;margin-top:4px;"> {label}</label>\n    </div>')


def metric(mid, label):
    return (f'      <div class="calc-metric-card">\n        <div class="cmv" id="{mid}" style="font-size:22px;line-height:1.2;">&mdash;</div>\n'
            f'        <div class="cml">{label}</div>\n        <div class="cmt" id="{mid}-cmt">&mdash;</div>\n      </div>')


def acc(aid, title, body):
    return f'<details class="mdc-acc" id="{aid}">\n<summary>{title}</summary>\n<div class="mdc-acc-body">\n{body}\n</div>\n</details>\n'


def alert(kind, icon, h, p):
    return (f'<div class="alert alert-{kind}">\n<div class="alert-icon">{icon}</div>\n<div class="alert-body">\n<h4>{h}</h4>\n<p>{p}</p>\n</div>\n</div>')


MATH_JS = r"""
function vsLnGamma(z){var c=[76.18009172947146,-86.50532032941677,24.01409824083091,-1.231739572450155,0.1208650973866179e-2,-0.5395239384953e-5];var x=z,y=z,t=x+5.5;t-=(x+0.5)*Math.log(t);var s=1.000000000190015;for(var j=0;j<6;j++){y+=1;s+=c[j]/y;}return -t+Math.log(2.5066282746310005*s/x);}
function vsBetacf(a,b,x){var M=200,E=3e-12,qab=a+b,qap=a+1,qam=a-1,c=1,d=1-qab*x/qap;if(Math.abs(d)<1e-30)d=1e-30;d=1/d;var h=d;for(var m=1;m<=M;m++){var m2=2*m,aa=m*(b-m)*x/((qam+m2)*(a+m2));d=1+aa*d;if(Math.abs(d)<1e-30)d=1e-30;c=1+aa/c;if(Math.abs(c)<1e-30)c=1e-30;d=1/d;h*=d*c;aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));d=1+aa*d;if(Math.abs(d)<1e-30)d=1e-30;c=1+aa/c;if(Math.abs(c)<1e-30)c=1e-30;d=1/d;var del=d*c;h*=del;if(Math.abs(del-1)<E)break;}return h;}
function vsIbeta(a,b,x){if(x<=0)return 0;if(x>=1)return 1;var bt=Math.exp(vsLnGamma(a+b)-vsLnGamma(a)-vsLnGamma(b)+a*Math.log(x)+b*Math.log(1-x));return x<(a+1)/(a+b+2)?bt*vsBetacf(a,b,x)/a:1-bt*vsBetacf(b,a,1-x)/b;}
function vsBetaInv(p,a,b){var lo=0,hi=1;for(var i=0;i<100;i++){var mid=(lo+hi)/2;if(vsIbeta(a,b,mid)<p)lo=mid;else hi=mid;}return (lo+hi)/2;}
function vsCP(k,n){var lo=k===0?0:vsBetaInv(0.025,k,n-k+1);var hi=k===n?1:vsBetaInv(0.975,k+1,n-k);return [lo,hi];}
function vsGammaP(a,x){if(x<=0)return 0;var gln=vsLnGamma(a);if(x<a+1){var ap=a,sum=1/a,del=sum;for(var n=0;n<500;n++){ap+=1;del*=x/ap;sum+=del;if(Math.abs(del)<Math.abs(sum)*3e-12)break;}return sum*Math.exp(-x+a*Math.log(x)-gln);}var b=x+1-a,c=1e30,d=1/b,h=d;for(var i=1;i<500;i++){var an=-i*(i-a);b+=2;d=an*d+b;if(Math.abs(d)<1e-30)d=1e-30;c=b+an/c;if(Math.abs(c)<1e-30)c=1e-30;d=1/d;var dl=d*c;h*=dl;if(Math.abs(dl-1)<3e-12)break;}return 1-Math.exp(-x+a*Math.log(x)-gln)*h;}
function vsGammaInv(p,a){var lo=0,hi=Math.max(10,a*10+50);for(var i=0;i<200;i++){var mid=(lo+hi)/2;if(vsGammaP(a,mid)<p)lo=mid;else hi=mid;}return (lo+hi)/2;}
function vsPoisCI(k){var lo=k===0?0:vsGammaInv(0.025,k);var hi=vsGammaInv(0.975,k+1);return [lo,hi];}
function vsNum(id){var e=document.getElementById(id);if(!e||e.value==='')return NaN;return parseFloat(e.value);}
function vsSet(id,v,c){var e=document.getElementById(id);if(e)e.innerHTML=v;var f=document.getElementById(id+'-cmt');if(f&&c!==undefined)f.innerHTML=c;}
function vsPct(x){return (100*x).toFixed(1)+'%';}
function vsBox(id,level){var r=document.getElementById(id);var dark=document.documentElement.getAttribute('data-theme')==='dark';var col={ok:dark?'var(--green)':'#166534',warn:dark?'var(--amber)':'#92400e',bad:dark?'var(--red)':'#b91c1c',info:dark?'var(--teal)':'#1a6b72'}[level];var bg={ok:dark?'rgba(22,101,52,.10)':'#f0fdf4',warn:dark?'rgba(146,64,14,.10)':'#fffbeb',bad:dark?'rgba(185,28,28,.10)':'#fff0f0',info:dark?'rgba(26,107,114,.10)':'#eef8f8'}[level];r.style.display='block';r.style.borderColor=col;r.style.background=bg;}
"""

CALCS = [
    # ───────────────────────── 1. AV fistula maturation ─────────────────────────
    {
        "file": "calc-av-fistula-maturation.html",
        "title": "AV Fistula Maturation Readiness Check",
        "seo_title": "AV Fistula Maturation Readiness Check: Ultrasound Criteria and Timing",
        "desc": ("Check whether a new arteriovenous fistula is likely ready for cannulation from vein diameter, access flow, depth and weeks "
                 "since creation: Robbin ultrasound criteria with observed adequacy rates, NEAT physiologic suitability, the opinion-based "
                 "rule of 6s, and UKKA 2025 timing prompts."),
        "tag": "Nephrology · Clinical Calculator · Vascular Access",
        "h1": "AV Fistula Maturation <em>Readiness Check</em>",
        "sub": ("Enter the duplex findings of a new fistula. The check compares them with the ultrasound criteria that predicted adequacy for "
                "dialysis in published studies, flags depth and timing, and reminds you that a thrill and a calendar date do not establish "
                "readiness."),
        "xlink": ("calc-hand-ischemia-dbi.html", "Hand ischemia check →"),
        "instructions": [
            "Enter the <strong>minimum vein diameter</strong> (mm) at the planned cannulation zone, the <strong>access flow</strong> (mL/min, brachial artery or access flow by duplex), and the <strong>depth</strong> of the vein (mm from skin) where needles will go.",
            "Enter the <strong>weeks since creation</strong>.",
            "Tick whether a straight, superficial segment long enough for two needles has been identified and marked.",
            "Results show the Robbin criteria (diameter of at least 4 mm and flow of at least 500 mL/min), NEAT physiologic suitability, the opinion-based rule of 6s, and timing prompts. Measurements are surrogates for usability: the decision rests on a joint assessment with the dialysis team.",
        ],
        "fields": [field("fm-diam", "Minimum vein diameter (mm)", "At the planned needle zone.", "4.2", "0", "30", "0.1"),
                   field("fm-flow", "Access flow (mL/min)", "Duplex volume flow.", "620", "0", "5000", "1"),
                   field("fm-depth", "Vein depth from skin (mm)", "At the planned needle zone.", "5", "0", "40", "0.1"),
                   field("fm-weeks", "Weeks since creation", "Whole or decimal weeks.", "6", "0", "104", "0.5"),
                   check("fm-seg", "A straight superficial segment long enough for two needles is identified and marked")],
        "metrics": [metric("fm-robbin", "Robbin criteria"), metric("fm-six", "Rule of 6s (opinion)"), metric("fm-time", "Timing")],
        "when": ("<p>Use at the maturation review of a new autogenous fistula, typically 2 to 6 weeks after creation and later if it is not yet "
                 "usable, to structure the joint decision with the dialysis team about first cannulation or further investigation.</p>"
                 + alert("amber", "⚠️", "Not a cannulation order", "A favorable result does not authorize cannulation. First use needs an examination by an experienced cannulator and a written first-use plan. Grafts follow device-specific rules and are not assessed with these criteria.")),
        "pearls": (alert("green", "💡", "Both criteria matter", "In Robbin&rsquo;s study, 95% of fistulas meeting both diameter and flow criteria were adequate for dialysis, against 33% meeting neither. One criterion alone was less reassuring.")
                   + alert("red", "🚫", "Pitfalls", "Diameter depends on method (tourniquet, temperature). A thrill shows flow, not usability. A deep vein may need superficialization even with excellent flow. Cannulation within 14 days of creation was associated with a higher failure risk in DOPPS (observational).")),
        "why": ("<p>Most fistulas take months to mature and about one in four never become usable. Objective duplex criteria help separate "
                "fistulas likely to support dialysis from those needing investigation, which shortens catheter exposure and avoids "
                "damaging an immature vein with early needling.</p>"),
        "next": ("<ul style=\"margin:8px 0 0 1.1em;padding:0;line-height:1.8;\">"
                 "<li><strong>Both criteria met, superficial, segment marked:</strong> agree a written first-use plan with an experienced cannulator (Academy Vascular Surgeon Module 9).</li>"
                 "<li><strong>Good flow but deep:</strong> discuss superficialization or transposition.</li>"
                 "<li><strong>Low flow:</strong> look for juxta-anastomotic or inflow stenosis and diverting side branches.</li>"
                 "<li><strong>Not mature beyond 6 weeks:</strong> investigate (UKKA 2025 statement 3.9, grade 1C).</li></ul>"),
        "formula": [("Robbin criteria", "Minimum vein diameter &ge; 4 mm and access flow &ge; 500 mL/min (both / one / neither)"),
                    ("NEAT physiologic suitability", "Brachial artery flow &ge; 500 mL/min and vein diameter &ge; 4 mm"),
                    ("Rule of 6s (expert opinion)", "Diameter &ge; 6 mm, depth &lt; 6 mm, flow &ge; 600 mL/min, at about 6 weeks"),
                    ("Timing prompts", "&lt; 2 weeks: early-cannulation caution (DOPPS); &ge; 6 weeks and not mature: investigate (UKKA 3.9)")],
        "refs": ["vs_robbin2002", "vs_lok2017", "vs_ukka", "vs_rayner2003", "vs_huber2021"],
        "related": [("calc-hand-ischemia-dbi.html", "Calculator", "Hand Ischemia &amp; DBI Check"),
                    ("calc-av-access-outcome-audit.html", "Calculator", "AV Access Outcome Audit"),
                    ("hemodialysis-access-lifeline.html", "Guide", "The Access as a Lifeline")],
        "js": r"""
function run(){
  var d=vsNum('fm-diam'),q=vsNum('fm-flow'),z=vsNum('fm-depth'),w=vsNum('fm-weeks'),seg=document.getElementById('fm-seg').checked;
  var box=document.getElementById('fm-result');
  if(isNaN(d)||isNaN(q)){box.style.display='none';return;}
  var dOK=d>=4,qOK=q>=500,n=(dOK?1:0)+(qOK?1:0),lvl,rb,rc;
  if(n===2){rb='Both met';rc='95% adequate in Robbin (19 of 20)';lvl='ok';}
  else if(n===1){rb='One met';rc=dOK?'Diameter &ge; 4 mm alone: 89% adequate (24 of 27)':'Flow &ge; 500 alone: 84% adequate (26 of 31)';lvl='warn';}
  else{rb='Neither met';rc='33% adequate in Robbin (5 of 15)';lvl='bad';}
  vsSet('fm-robbin',rb,rc);
  var six=0,sixN=3; if(d>=6)six++; if(q>=600)six++; if(!isNaN(z)){sixN=4; if(z<6)six++;}
  vsSet('fm-six',six+' of '+sixN,'Expert benchmark, not validated');
  var tt='&mdash;',tc='Enter weeks since creation';
  if(!isNaN(w)){ if(w<2){tt='Early';tc='Cannulation &le; 14 days: 2.1-fold failure risk (DOPPS, observational)';if(lvl==='ok')lvl='warn';}
    else if(w<6){tt='Within window';tc='UKKA: first maturity assessment at 2 to 6 weeks';}
    else{tt=(n===2)?'Past 6 weeks':'Investigate';tc=(n===2)?'Assess for first use':'Not mature beyond 6 weeks: investigate (UKKA 3.9)';} }
  vsSet('fm-time',tt,tc);
  var v='Diameter '+d+' mm, flow '+q+' mL/min'+(isNaN(z)?'':', depth '+z+' mm')+'. '+(n===2?'Meets both Robbin criteria and NEAT physiologic suitability.':(n===1?'Meets one Robbin criterion; NEAT suitability not met.':'Meets neither Robbin criterion.'));
  var a=[];
  if(!isNaN(z)&&z>6)a.push('The vein is deep: it may be hard to needle and superficialization may be needed.');
  if(n<2)a.push('Look for inflow or juxta-anastomotic stenosis and side branches diverting flow.');
  if(!seg)a.push('No usable segment has been marked yet: first use needs a marked, straight, superficial segment.');
  if(n===2&&seg&&(isNaN(z)||z<=6))a.push('Findings support readiness. Agree a written first-use plan with an experienced cannulator; do not authorize by phone.');
  document.getElementById('fm-verdict').innerHTML=v;document.getElementById('fm-action').innerHTML=a.join(' ');
  vsBox('fm-result',lvl);
}
""",
    },
    # ───────────────────────── 2. Hand ischemia and DBI ─────────────────────────
    {
        "file": "calc-hand-ischemia-dbi.html",
        "title": "Hand Ischemia and Digital–Brachial Index Check",
        "seo_title": "Access Hand Ischemia Check: Digital–Brachial Index and Steal Grade",
        "desc": ("Grade access-related hand ischemia (steal syndrome) with the UKKA 2025 clinical scale, compute the digital–brachial index "
                 "from finger and arm pressures, and flag new neurologic deficit that needs immediate surgical assessment."),
        "tag": "Nephrology · Clinical Calculator · Vascular Access",
        "h1": "Hand Ischemia <em>&amp; Digital&ndash;Brachial Index</em>",
        "sub": ("For a patient with an arteriovenous access and hand symptoms: grade the clinical severity, compute the digital&ndash;brachial "
                "index (DBI), and see the urgency. Symptoms and examination decide; the DBI supports."),
        "xlink": ("calc-av-fistula-maturation.html", "Maturation check →"),
        "instructions": [
            "Choose the <strong>symptom grade</strong> and tick <strong>new motor or sensory deficit</strong> if present. These drive urgency.",
            "Choose the <strong>onset</strong> relative to access creation.",
            "Optionally enter the <strong>digit systolic pressure</strong> on the access hand and the <strong>brachial systolic pressure</strong> (usually the non-access arm). The DBI is digit pressure divided by brachial pressure.",
            "A thrill or bruit is not entered: access flow says nothing about hand perfusion.",
        ],
        "fields": [select("hi-grade", "Symptom grade (UKKA 2025)", "Choose the highest that applies.",
                          [("", "Choose&hellip;"), ("0", "No symptoms"), ("1", "Pale or cool hand, no pain"),
                           ("2", "Pain on exercise or during dialysis"), ("3", "Pain at rest"), ("4", "Ulcer or necrosis")]),
                   check("hi-neuro", "New motor weakness or sensory loss in the access hand"),
                   select("hi-onset", "Onset after access creation", "Timing points to cause.",
                          [("", "Choose&hellip;"), ("a", "Within 24 hours"), ("s", "Within 1 month"), ("c", "After 1 month")]),
                   field("hi-dig", "Digit systolic, access hand (mm Hg)", "Photoplethysmography or Doppler.", "60", "0", "300", "1"),
                   field("hi-bra", "Brachial systolic (mm Hg)", "Usually the non-access arm.", "130", "1", "300", "1")],
        "metrics": [metric("hi-sev", "Clinical grade"), metric("hi-dbi", "Digital&ndash;brachial index"), metric("hi-urg", "Urgency")],
        "when": ("<p>Use when a patient with a fistula or graft reports a cold, pale, painful, weak or numb hand, or a finger ulcer, and at "
                 "follow-up after brachial-based access in patients with diabetes, peripheral arterial disease or coronary disease.</p>"
                 + alert("red", "⛔", "Do not wait on this tool", "New weakness, numbness, rest pain or tissue loss needs immediate surgical assessment, whatever the result here.")),
        "pearls": (alert("green", "💡", "Pressure, not reversed flow", "Reversed flow beyond the access (steal) is common and often harmless. Ischemia comes from low perfusion pressure in the hand when arteries cannot adapt.")
                   + alert("red", "🚫", "Pitfalls", "Low DBI values are common after access creation and do not by themselves mean ischemia. Consider carpal tunnel syndrome, arthritis and neuropathy. Ischemic monomelic neuropathy can present with a warm hand.")),
        "why": ("<p>Hand ischemia threatens function and is easily missed when the access thrill is strong. A shared severity scale makes "
                "urgency explicit for nurses, physicians on duty and surgeons, and timing helps point to cause.</p>"),
        "next": ("<ul style=\"margin:8px 0 0 1.1em;padding:0;line-height:1.8;\">"
                 "<li><strong>Grade 1:</strong> no treatment needed; document and review (UKKA 4.9, grade 2C: manage mild steal conservatively).</li>"
                 "<li><strong>Grade 2:</strong> treatment often needed and may be planned; duplex for inflow stenosis or high flow.</li>"
                 "<li><strong>Grade 3 or tissue loss:</strong> prompt surgical treatment.</li>"
                 "<li><strong>New neurologic deficit:</strong> immediate surgical assessment.</li></ul>"),
        "formula": [("Digital&ndash;brachial index", "Digit systolic pressure (access hand) &divide; brachial systolic pressure"),
                    ("Clinical grade (UKKA 2025, Table 1)", "1 pale or cool, no pain; 2 pain on exercise or dialysis; 3 rest pain, ulcer or necrosis"),
                    ("Onset", "Within 24 hours: mostly grafts; after 1 month: mostly brachial-based fistulas (Scheltinga 2009)"),
                    ("Context", "Small banding series: DBI 0.52 before and 0.65 after flow reduction in symptomatic patients (van Hoek 2009)")],
        "refs": ["vs_ukka", "vs_scheltinga2009", "vs_scheltinga2012", "vs_vanhoek2009"],
        "related": [("calc-av-fistula-maturation.html", "Calculator", "AV Fistula Maturation Check"),
                    ("calc-access-flow-cardiac.html", "Calculator", "Access Flow &amp; Cardiac Burden"),
                    ("dialysis-access-care.html", "Guide", "Caring for Your Dialysis Access")],
        "js": r"""
function run(){
  var g=document.getElementById('hi-grade').value,neu=document.getElementById('hi-neuro').checked,on=document.getElementById('hi-onset').value;
  var dg=vsNum('hi-dig'),br=vsNum('hi-bra'),box=document.getElementById('hi-result');
  if(g===''&&!neu&&(isNaN(dg)||isNaN(br))){box.style.display='none';return;}
  var gi=g===''?-1:parseInt(g,10),lab=['None','1, mild','2, moderate','3, severe','3, severe with tissue loss'],lvl='info',urg,uc;
  vsSet('hi-sev',gi<0?'&mdash;':lab[gi],gi<0?'Choose a grade':['No action needed','No treatment; review','Treatment often needed','Prompt treatment','Prompt treatment'][gi]);
  if(!isNaN(dg)&&!isNaN(br)&&br>0){vsSet('hi-dbi',(dg/br).toFixed(2),'Supportive only; interpret with symptoms');}else vsSet('hi-dbi','&mdash;','Enter both pressures');
  if(neu||gi>=3){urg='Immediate';uc='Same-day surgical assessment';lvl='bad';}
  else if(gi===2){urg='Soon';uc='Surgical review; duplex for causes';lvl='warn';}
  else if(gi===1){urg='Routine';uc='Document and review';lvl='ok';}
  else{urg='&mdash;';uc='Grade the symptoms';}
  vsSet('hi-urg',urg,uc);
  var v=[],a=[];
  if(neu)v.push('New motor or sensory deficit: possible acute nerve ischemia (for example ischemic monomelic neuropathy), a surgical emergency.');
  if(on==='a')v.push('Onset within 24 hours of surgery is most often associated with grafts.');
  if(on==='c')v.push('Chronic onset is most often associated with brachial-based fistulas.');
  if(gi>=2)a.push('Look for an inflow arterial stenosis or a high-flow access; options (angioplasty, banding, DRIL, PAI, RUDI, ligation) are chosen by a qualified surgeon.');
  a.push('A strong thrill does not reassure about the hand.');
  document.getElementById('hi-verdict').innerHTML=v.join(' ')||'Clinical grade drives urgency; the DBI supports.';
  document.getElementById('hi-action').innerHTML=a.join(' ');
  vsBox('hi-result',lvl);
}
""",
    },
    # ───────────────────────── 3. Outcome audit ─────────────────────────
    {
        "file": "calc-av-access-outcome-audit.html",
        "title": "AV Access Outcome Audit",
        "seo_title": "AV Access Outcome Audit: Primary Failure, Functional Use and Catheter Infection Rates",
        "desc": ("Audit an access service honestly: primary failure and functional use with Clopper–Pearson 95% confidence intervals, "
                 "best and worst case for patients lost to follow-up, intervention rate per access-year and catheter infection rate per "
                 "1,000 catheter-days with exact Poisson intervals."),
        "tag": "Nephrology · Clinical Calculator · Vascular Access · Quality",
        "h1": "AV Access <em>Outcome Audit</em>",
        "sub": ("Turn a year of access work into transparent numbers: counts beside rates, confidence intervals, and what the result would be if "
                "every patient lost to follow-up had done well or badly."),
        "xlink": ("calc-access-infection-rate.html", "Infection rate tool →"),
        "instructions": [
            "Enter the number of <strong>accesses created</strong> in the audit cohort and how many were <strong>lost to follow-up</strong> before the outcome window closed.",
            "Enter <strong>primary failures</strong> (never usable or failed before use) and the number <strong>used successfully for dialysis</strong> within your stated window, both counted among those followed up.",
            "Optionally enter interventions and access-years at risk, and catheter-days with catheter-related bloodstream infections (CRBSI).",
            "Define the cohort, window and censoring rules before collecting data, and report them with the results.",
        ],
        "fields": [field("oa-n", "Accesses created", "Cohort size.", "118", "1", "100000", "1", "run()"),
                   field("oa-l", "Lost to follow-up", "Before the window closed.", "21", "0", "100000", "1"),
                   field("oa-f", "Primary failures (among followed)", "Never usable or failed before use.", "24", "0", "100000", "1"),
                   field("oa-u", "Used successfully (among followed)", "Within your stated window.", "63", "0", "100000", "1"),
                   field("oa-i", "Interventions (optional)", "Procedures to maintain or salvage.", "40", "0", "100000", "1"),
                   field("oa-y", "Access-years at risk (optional)", "Sum of follow-up time.", "80", "0", "1000000", "0.1"),
                   field("oa-cd", "Catheter-days (optional)", "Total in the period.", "9500", "0", "10000000", "1"),
                   field("oa-b", "CRBSI events (optional)", "Using a prespecified definition.", "4", "0", "100000", "1")],
        "metrics": [metric("oa-pf", "Primary failure"), metric("oa-fu", "Functional use"), metric("oa-miss", "Lost to follow-up"),
                    metric("oa-ir", "Interventions per access-year"), metric("oa-crb", "CRBSI per 1,000 catheter-days")],
        "when": ("<p>Use for a service audit, a quality meeting or a capstone service proposal, when you need numbers that can be compared over "
                 "time without hiding missing data or small-number uncertainty.</p>"
                 + alert("amber", "⚠️", "Definitions first", "Rates per 1,000 catheter-days and NHSN rates per 100 patient-months are different measures. Do not compare across definitions or across services with different case mix.")),
        "pearls": (alert("green", "💡", "Technical is not functional", "Report patency and functional use separately. A patent fistula that is never used is a failure for the patient.")
                   + alert("red", "🚫", "Pitfalls", "Dropping patients lost to follow-up flatters results. Small services see wide intervals: one event can move a rate dramatically, so show counts.")),
        "why": ("<p>The SVS reporting standards define patency so results can be compared. Honest audits state their denominator, show "
                "uncertainty and missing data, and point to a change the team can test.</p>"),
        "next": ("<ul style=\"margin:8px 0 0 1.1em;padding:0;line-height:1.8;\">"
                 "<li>Pick one gap the numbers expose, such as unused mature fistulas or long catheter exposure.</li>"
                 "<li>Define one process change and one measure, and set a review date.</li>"
                 "<li>Plot the measure monthly on a <a href=\"calc-qapi-run-chart-spc.html\" style=\"color:var(--teal);font-weight:600;\">run chart</a>.</li></ul>"),
        "formula": [("Primary failure", "failures &divide; (created &minus; lost); exact Clopper&ndash;Pearson 95% CI"),
                    ("Functional use", "used &divide; (created &minus; lost); best case adds all lost as used, worst case counts them as not used"),
                    ("Intervention rate", "interventions &divide; access-years; exact Poisson 95% CI"),
                    ("CRBSI rate", "events &divide; catheter-days &times; 1,000; exact Poisson 95% CI")],
        "refs": ["vs_sidawy2002", "vs_ukka", "vs_aljaishi2014", "vs_huber2021"],
        "related": [("calc-access-infection-rate.html", "Calculator", "Access Infection Rate with Exact CI"),
                    ("calc-access-intervention-burden.html", "Calculator", "Access Intervention Burden"),
                    ("dialysis-qapi-vs-cqi.html", "Guide", "QAPI versus CQI in Dialysis")],
        "js": r"""
function run(){
  var N=vsNum('oa-n'),L=vsNum('oa-l'),F=vsNum('oa-f'),U=vsNum('oa-u'),I=vsNum('oa-i'),Y=vsNum('oa-y'),C=vsNum('oa-cd'),B=vsNum('oa-b');
  var box=document.getElementById('oa-result');
  if(isNaN(N)||N<1){box.style.display='none';return;}
  if(isNaN(L))L=0; var n=N-L, lvl='info', msg=[];
  if(n<1||L<0){vsSet('oa-pf','&mdash;','Check counts');box.style.display='block';return;}
  vsSet('oa-miss',L+' of '+N,vsPct(L/N)+' of the cohort');
  if(!isNaN(F)&&F<=n){var c=vsCP(F,n);vsSet('oa-pf',vsPct(F/n),F+' of '+n+'; 95% CI '+vsPct(c[0])+' to '+vsPct(c[1]));}else vsSet('oa-pf','&mdash;','Enter failures (&le; followed)');
  if(!isNaN(U)&&U<=n){var c2=vsCP(U,n);vsSet('oa-fu',vsPct(U/n),U+' of '+n+'; 95% CI '+vsPct(c2[0])+' to '+vsPct(c2[1]));
    msg.push('If every patient lost to follow-up had used the access, functional use would be '+vsPct((U+L)/N)+'; if none had, '+vsPct(U/N)+'.');}
  else vsSet('oa-fu','&mdash;','Enter used (&le; followed)');
  if(!isNaN(I)&&!isNaN(Y)&&Y>0){var p=vsPoisCI(I);vsSet('oa-ir',(I/Y).toFixed(2),I+' in '+Y+' access-years; 95% CI '+(p[0]/Y).toFixed(2)+' to '+(p[1]/Y).toFixed(2));}else vsSet('oa-ir','&mdash;','Optional');
  if(!isNaN(B)&&!isNaN(C)&&C>0){var q=vsPoisCI(B);vsSet('oa-crb',(1000*B/C).toFixed(2),B+' in '+C+' catheter-days; 95% CI '+(1000*q[0]/C).toFixed(2)+' to '+(1000*q[1]/C).toFixed(2));}else vsSet('oa-crb','&mdash;','Optional');
  if(L/N>0.1){msg.push('More than 10% were lost to follow-up: report the best and worst case above alongside the main result.');lvl='warn';}
  document.getElementById('oa-verdict').innerHTML='Denominator for outcomes: '+n+' followed of '+N+' created.';
  document.getElementById('oa-action').innerHTML=msg.join(' ');
  vsBox('oa-result',lvl);
}
""",
    },
]


def build(spec, shell):
    s = shell
    t, d, url = spec["seo_title"], spec["desc"], f"https://renalcarematters.com/guides/{spec['file'][:-5]}"
    s = re.sub(r"<title>.*?</title>", f"<title>{t}</title>", s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc_attr(d)}">', s, count=1)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*(">)', rf"\g<1>{url}\g<2>", s, count=1)
    for prop in ("og:title", "twitter:title"):
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*(">)', rf"\g<1>{esc_attr(spec['title'])}\g<2>", s)
    for prop in ("og:description", "twitter:description"):
        s = re.sub(rf'(<meta (?:property|name)="{prop}" content=")[^"]*(">)', rf"\g<1>{esc_attr(d)}\g<2>", s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(">)', rf"\g<1>{url}\g<2>", s)
    s = re.sub(r'(<meta property="article:published_time" content=")[^"]*(">\n?)', "", s)
    s = s.replace('"name": "Ankle-Brachial Index (ABI)"', f'"name": "{spec["title"]}"').replace(
        '"url": "https://renalcarematters.com/guides/calc-abi"', f'"url": "{url}"')
    s = s.replace("https://renalcarematters.com/guides/calc-abi\"", url + '"')
    s = re.sub(r'<div class="hero-tag">.*?</div>', f'<div class="hero-tag">{spec["tag"]}</div>', s, count=1)
    s = re.sub(r"<h1>.*?</h1>", f"<h1>{spec['h1']}</h1>", s, count=1, flags=re.S)
    s = re.sub(r'<p class="hero-sub">.*?</p>', f'<p class="hero-sub">{spec["sub"]}</p>', s, count=1, flags=re.S)
    s = re.sub(r'<div class="hero-meta">.*?</div>', '<div class="hero-meta">\n</div>', s, count=1, flags=re.S)
    s = s.replace('<a href="calc-prevent-cvd.html" class="hero-xlink">CV risk calculator →</a>',
                  f'<a href="{spec["xlink"][0]}" class="hero-xlink">{spec["xlink"][1]}</a>')
    # main
    instr = "\n".join(f"<li>{x}</li>" for x in spec["instructions"])
    rows = "\n".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in spec["formula"])
    refs = "\n".join(f"<li>{apa(k)}</li>" for k in spec["refs"])
    stem = spec["file"][5:-5].split("-")[0][:2]
    pid = {"calc-av-fistula-maturation.html": "fm", "calc-hand-ischemia-dbi.html": "hi", "calc-av-access-outcome-audit.html": "oa"}[spec["file"]]
    main = f"""<main class="container">

<div class="mdc-instructions" id="instructions"><span class="mdc-instr-label">Instructions</span>
<ol style="margin:0 0 8px 1.1em;padding:0;line-height:1.8;">
{instr}
</ol>
<p style="font-size:.92rem;color:var(--text-muted);">All computation runs in your browser; no values are stored or transmitted. Educational tool written for the Renal Care Academy Vascular Surgeon track; clinical review pending.</p>
</div>

{acc("when", "When to Use", spec["when"])}
{acc("pearls", "Pearls &amp; Pitfalls", spec["pearls"])}
{acc("why", "Why Use It", spec["why"])}
<section class="section" id="calculator">
<div class="section-tag">Interactive Tool</div>
<h2>{spec["title"]}</h2>
<div class="calc-wrap">

  <div class="calc-grid">
{chr(10).join(spec["fields"])}
  </div>

  <div class="calc-result-box" id="{pid}-result" style="display:none;">
    <div class="calc-metrics-row">
{chr(10).join(spec["metrics"])}
    </div>
    <div class="calc-verdict-text" id="{pid}-verdict"></div>
    <div class="calc-action-text" id="{pid}-action"></div>
    <p class="calc-disclaimer">⚕ Educational aid for licensed clinicians. Thresholds come from the cited studies and guidelines and are surrogates or prompts, not decisions.</p>
  </div>
</div>
</section>

{acc("nextsteps", "Next Steps", spec["next"])}
<details class="mdc-acc" id="evidence">
<summary>Evidence &amp; References</summary>
<div class="mdc-acc-body">
<h3 class="mdc-sub">Formula and rules</h3>
<table class="lab-table">
<thead><tr><th>Quantity</th><th>Rule</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
<h3 class="mdc-sub">References</h3>
<ol style="margin:8px 0 0 1.1em;padding:0;line-height:1.85;font-size:.94rem;">
{refs}
</ol>
</div>
</details>

<div class="disclaimer"><strong>Important:</strong> This calculator is an educational aid for licensed clinicians and does not replace examination, imaging, or your institution&rsquo;s protocols. It does not authorize cannulation, surgery or any change in treatment.</div>

</main>"""
    fn = f"vsRun_{pid}"
    main = main.replace('"run()"', f'"{fn}()"')
    js = spec["js"].replace("function run(", f"function {fn}(")
    s = re.sub(r"<main\b.*?</main>", lambda m: main, s, count=1, flags=re.S)
    # replace the ABI script with this calculator's script
    s = re.sub(r"<script>\s*/\* Ankle-Brachial Index.*?</script>",
               lambda m: "<script>\n/* " + spec["title"] + " (Renal Care Academy, Vascular Surgeon track) */" + MATH_JS + js + "</script>",
               s, count=1, flags=re.S)
    # references accordion
    ref_items = "\n".join(f"<li>{apa(k)}</li>" for k in spec["refs"])
    s = re.sub(r'(<details class="ref-acc".*?<span style="margin-left:auto;[^>]*>)\d+ sources(</span>.*?<ol[^>]*>).*?(</ol>)',
               lambda m: m.group(1) + f"{len(spec['refs'])} sources" + m.group(2) + "\n" + ref_items + "\n" + m.group(3), s, count=1, flags=re.S)
    # related guides
    cards = "\n".join(f'    <a class="related-card" href="{h}">\n      <div class="related-card-tag">{tg}</div>\n      <div class="related-card-title">{tt}</div>\n    </a>'
                      for h, tg, tt in spec["related"])
    s = re.sub(r'(<div class="related-cards">).*?(</div>\n</div>\n<!-- RELATED-GUIDES-END -->)', lambda m: m.group(1) + "\n" + cards + "\n  " + m.group(2), s, count=1, flags=re.S)
    assert "calcABI" not in s, spec["file"]
    (G / spec["file"]).write_text(s, encoding="utf-8")
    print("wrote", spec["file"])


if __name__ == "__main__":
    shell = SHELL.read_text(encoding="utf-8")
    for c in CALCS:
        build(c, shell)
