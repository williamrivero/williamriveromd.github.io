# -*- coding: utf-8 -*-
"""Extra course-home sections for the Pediatric Dialysis Nurse track (COURSE["hub_sections"]).
Each entry is placed before an existing course-home section id. Content comes from the v2 blueprint and verified sources."""

TOOLKIT = "calc-pediatric-dialysis-nurse-toolkit.html"


def _calc(f, title, desc):
    return (f'  <a href="{f}" class="calc-card">\n    <div class="calc-card-icon">⌬</div>\n    <div class="calc-card-body">\n'
            f'      <div class="calc-card-title">{title}</div>\n      <div class="calc-card-desc">{desc}</div>\n    </div>\n'
            f'    <span class="calc-card-arrow">Open →</span>\n  </a>')


_CALCS = [
    (TOOLKIT, "Pediatric Dialysis Nurse Toolkit", "Six order-verification tools: body surface area (BSA) and fill volume, extracorporeal volume, blood flow, fluid removal, percent fluid overload, infection rates."),
    ("calc-pediatric-egfr.html", "Pediatric eGFR (bedside CKiD)", "Estimated glomerular filtration rate (GFR) from height and creatinine. Module 2."),
    ("calc-pediatric-bp.html", "Pediatric Blood Pressure Percentile", "Classify a child&rsquo;s blood pressure by age, sex and height. Module 4."),
    ("calc-pediatric-growth-percentiles.html", "Pediatric Growth Percentiles", "Plot height and weight against reference curves. Module 17."),
    ("calc-pediatric-aki.html", "Pediatric AKI Staging", "Stage acute kidney injury in a child. Module 16."),
    ("calc-fluid-overload.html", "Cumulative Fluid Balance", "Fluid gained as a share of body weight. Modules 4 and 16."),
    ("calc-access-infection-rate.html", "Access Infection Rate", "Infection rate with an exact 95% confidence interval. Modules 5 and 20."),
]

HUB_SECTIONS = [
    {"id": "role", "nav": "The role", "tag": "The role", "before": "pathways",
     "h2": "What a pediatric dialysis nurse does",
     "html": """
<p>The pediatric dialysis nurse gives prescribed peritoneal dialysis (PD) or hemodialysis to infants, children and adolescents, teaches and supports their caregivers, and protects the things a child on dialysis still has to do: grow, learn, play and, usually, get ready for a transplant. The role below is a synthesized specification for local adaptation, not an official Department of Health, PSN or PhilHealth job description.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>What the nurse does</th><th>What the nurse does not do without separate authorization</th></tr></thead>
<tbody>
<tr><td>Assessment</td><td>Weighs, measures, takes age-appropriate vital signs, reconciles orders, fluid, access and medicines</td><td>Set the target weight or fluid-removal goal</td></tr>
<tr><td>Treatment</td><td>Delivers validated PD and hemodialysis tasks using approved procedures and device instructions</td><td>Prescribe, prime with blood or albumin without an order, insert catheters, repair equipment</td></tr>
<tr><td>Safety</td><td>Recognizes deterioration, protects the child, escalates early</td><td>Choose antibiotics, change doses, adjust anticoagulation</td></tr>
<tr><td>Family</td><td>Teaches to safe independence, judged by return demonstration; supports siblings and schooling</td><td>Transfer prescribing responsibility to a caregiver</td></tr>
<tr><td>Continuity</td><td>Coordinates nutrition, growth, psychosocial care, school, transplant preparation and transition</td><td>Manage transplant immunosuppression (transplant pathway)</td></tr>
<tr><td>Quality</td><td>Keeps accurate records, gives structured handoffs, joins incident learning and improvement</td><td>Rank individual nurses by small-number infection rates</td></tr>
</tbody></table></div>
"""},
    {"id": "evidence", "nav": "Key evidence", "tag": "Evidence", "before": "modules",
     "h2": "The numbers a pediatric dialysis nurse should know",
     "html": """
<div class="table-wrap"><table>
<thead><tr><th>Number</th><th>What it means</th><th>Source and strength</th></tr></thead>
<tbody>
<tr><td>Under about 10% of blood volume</td><td>Total extracorporeal volume (lines, needles, dialyzer) for a child on hemodialysis</td><td>ESPN practical guidelines, 2005; expert guidance[[pdn_fischbach2005]]</td></tr>
<tr><td>150&ndash;200 mL/min/m&sup2; (5&ndash;7 mL/min/kg)</td><td>Blood flow often sufficient for a child&rsquo;s hemodialysis</td><td>ESPN practical guidelines, 2005[[pdn_fischbach2005]]</td></tr>
<tr><td>Up to about 1,400 mL/m&sup2;</td><td>Fill volume at which the peritoneum keeps recruiting in children 2 years and older; under 2, about 800 mL/m&sup2; is often the upper limit, by tolerance</td><td>Physiology review, 2009[[pdn_fischbach2009]]</td></tr>
<tr><td>0.4 or fewer</td><td>Peritonitis episodes per patient-year at risk for a pediatric PD program</td><td>ISPD 2024 pediatric guideline, not graded[[pdn_warady2024]]</td></tr>
<tr><td>3.3 &rarr; 0.8</td><td>Hemodialysis catheter bloodstream infections per 100 patient-months after care bundles in SCOPE</td><td>Quality collaborative, pre&ndash;post[[pdn_marsenic2020]]</td></tr>
<tr><td>20% or more</td><td>Fluid overload at the start of continuous kidney replacement therapy associated with 65.6% mortality, versus 29.4% below 10%</td><td>Prospective registry, observational[[pdn_sutherland2010]]</td></tr>
<tr><td>67.2%</td><td>Share of critically ill children with low urine output whose AKI creatinine alone missed</td><td>AWARE, prospective multinational[[pdn_kaddourah2017]]</td></tr>
<tr><td>5% at 3 years</td><td>Overall probability of death on maintenance PD in the IPPN registry, from 2% in North America to 9% in Eastern Europe</td><td>Prospective registry[[pdn_ploos2021]]</td></tr>
</tbody></table></div>
"""},
    {"id": "redflags", "nav": "Red flags", "tag": "Quick reference", "before": "modules",
     "h2": "Red flags the whole track comes back to",
     "html": """
{{call:Stop and call the pediatric nephrologist or emergency team, per your unit&rsquo;s protocol, for: cloudy PD fluid, abdominal pain or fever in a child on PD; fever, rigors or hypotension during or after hemodialysis; a child who is unusually quiet, floppy, irritable or hard to wake; fast breathing, poor color or a heart rate trending up during fluid removal; an air, blood-leak or venous-pressure alarm you cannot explain; a weight, order or machine entry that do not agree; any concern that a child is being harmed. Per unit protocol, but always ask the attending nephrologist&rsquo;s guidance.}}
"""},
    {"id": "calculators", "nav": "Calculators", "tag": "Tools", "before": "how",
     "h2": "Calculators used in this track",
     "html": "<p>Every calculator here verifies arithmetic against an order. None of them is a prescribing tool.</p>\n<div class=\"calc-cards-wrap\">\n" + "\n".join(_calc(*c) for c in _CALCS) + "\n</div>"},
    {"id": "faq", "nav": "FAQ", "tag": "Questions", "before": "trainers",
     "h2": "Frequently asked questions",
     "html": """
<div class="qa-item"><div class="qa-q">Is there a separate Philippine license for pediatric dialysis nurses?</div><div class="qa-a">None was found in the issuances reviewed for this track (November 2026). Facility licensing, PSN training expectations, PhilHealth contracting and the hospital&rsquo;s own privileges still apply, and an institution may add its own requirements.</div></div>
<div class="qa-item"><div class="qa-q">I am an adult hemodialysis nurse. Which modules matter most?</div><div class="qa-a">All of them, but Modules 3, 4, 6, 13 and 15 change your habits most: development and assent, weight-based arithmetic, ten-fold errors, extracorporeal volume, and pediatric emergencies.</div></div>
<div class="qa-item"><div class="qa-q">Does finishing the track let me work alone with children?</div><div class="qa-a">No. It is study. Your facility authorizes you by modality, age and size band, device and supervision level after observed practice.</div></div>
<div class="qa-item"><div class="qa-q">Is pediatric automated PD covered by PhilHealth?</div><div class="qa-a">A pilot at NKTI, UP-PGH and PCMC was extended to July 31, 2026. Its status after that date was not verified for this track. Confirm with PhilHealth before discussing coverage with a family.</div></div>
"""},
]
