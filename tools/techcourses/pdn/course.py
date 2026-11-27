# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse: a Nephrology Nursing specialty subtrack, in the POD/DCH package schema.
Built from the v2 blueprint (~/Downloads/Pedia Dialysis Nurse/PEDIATRIC-DIALYSIS-NURSE-BLUEPRINT-v2.md), which improves the
v1.0 handoff package. Module ids 01 to 20 keep the handoff's PDN-01 to PDN-20 numbering. Every case and record is fictional."""
from pathlib import Path as _P
import importlib.util as _u

HUB = "pediatric-dialysis-nurse"
TOOLKIT = "calc-pediatric-dialysis-nurse-toolkit.html"

COURSE = {
    "title": "Pediatric Dialysis Nurse",
    "short": "Pediatric Dialysis Nurse",
    "hub_slug": HUB,
    "label": "Nephrology Nursing specialty subtrack for pediatric dialysis",
    "tag": "Nephrology Nursing &middot; Specialization",
    "icon": "🧸",
    "no_branch": True,
    "audience": ("Philippine-licensed registered nurses entering pediatric peritoneal dialysis or hemodialysis &middot; pediatric "
                 "dialysis nurse educators and preceptors"),
    "audience_type": "Registered nurses in pediatric dialysis",
    "level": "Registered nurses with adult dialysis training or pediatric nursing experience",
    "review_date": "2026-11-27",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 40,
    "keywords": ("pediatric dialysis nurse Philippines, pediatric hemodialysis nursing, pediatric peritoneal dialysis nursing, "
                 "ISPD 2024 pediatric peritonitis guideline, SCOPE collaborative, extracorporeal volume children, PD fill volume "
                 "per square meter, pediatric CKRT fluid overload, caregiver teaching PD, transition adolescent kidney, Renal Care Academy"),
    "page_title": "Pediatric Dialysis Nurse: A Nephrology Nursing Specialty Track",
    "desc": ("A free eight-week specialty track for registered nurses caring for infants, children and adolescents on dialysis: "
             "development and consent, weight-based arithmetic, infection prevention, PD and hemodialysis in small bodies, emergencies, "
             "acute kidney injury, growth, caregiver teaching, transition and Philippine practice. Cases, skills checklists and a "
             "self-assessment in every module."),
    "h1": "Pediatric Dialysis <em>Nurse</em>",
    "sub": ("A specialty track for registered nurses who dialyze children. Small bodies leave small margins: learn why each check "
            "protects the child, how to teach the family, and exactly when to call."),
    "disclaimer": ("Educational material for registered nurses. Completing it is an Academy learning record only. It does not confer "
                   "CPD units, PSN or National Kidney and Transplant Institute (NKTI) training recognition, PhilHealth staffing credit, "
                   "or clinical privileges, and it does not replace your facility&rsquo;s protocols, device instructions, or written orders."),
    "scope_note": ("This module is study material for registered nurses in pediatric dialysis. It explains the reasoning behind common "
                   "nursing decisions; it is not a procedure. Exact steps follow your unit&rsquo;s pediatric protocol and the device "
                   "instructions; treatment parameters follow the written order of the pediatric nephrologist. Nurses assess, verify, "
                   "teach, document and escalate; they do not prescribe, choose antibiotics, change doses or adjust anticoagulation. "
                   "Every case is fictional and every value in a case is illustrative. Pending review by a pediatric nephrologist and a "
                   "senior pediatric dialysis nurse."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Specialty subtrack &middot; registered nurses",
    "branch_blurb": ("For registered nurses who dialyze infants, children and adolescents: development and consent, weight-based "
                     "arithmetic, PD and hemodialysis in small bodies, emergencies, growth, caregiver teaching and transition."),
    "parent": ("nephrology-nursing.html", "Nephrology Nursing",
               "The parent course. Its dialysis modules are the adult foundation this track builds on."),
    "academy_meta": "20 modules &middot; eight weeks &middot; eight skills stations",
    "hero_alt": ("A pediatric dialysis nurse kneeling at eye level beside a seven-year-old girl in a small dialysis chair while the "
                 "girl's mother holds a picture book, in a bright pediatric dialysis room."),
    "start_h2": "Children are not small adults",
    "start_html": f"""
<p>A child on dialysis is still growing, still learning to read, still deciding who to trust. Kidney failure in childhood is rare, and that rarity is part of the danger: most dialysis nurses meet children only now and then, and the routines built for adults are the ones their hands know. In a 70-kilogram adult, a few hundred milliliters of blood outside the body, a misplaced decimal, or a fill volume that is slightly large are absorbed by the size of the body. In a 10-kilogram child they are not.</p>
<p>This track takes a registered nurse from the reasons children&rsquo;s kidneys fail to the quality numbers of a pediatric program, in twenty modules over eight weeks. It assumes you know adult dialysis or pediatric nursing, and it fills the gap between them. Most pediatric guidance rests on registries, consensus and quality-improvement collaboratives rather than large trials, because children on dialysis are few. The modules say so whenever it matters.[[pdn_warady2024]][[pdn_shroff2019]]</p>
{{{{cards:Exit competencies|A &middot; The child and the family::Communicate by developmental stage, obtain assent alongside consent, and recognize safeguarding concerns.|B &middot; Measurement::Measure reliably and verify every weight-based order with units and an independent check.|C &middot; Infection and access::Protect PD catheters, central lines and fistulas with bundles that measurably lower infection.|D &middot; PD in small bodies::Verify fill volumes scaled to body surface area and deliver CAPD and APD safely.|E &middot; Hemodialysis in small bodies::Check extracorporeal volume, priming, blood flow and fluid removal against the child&rsquo;s size.|F &middot; Deterioration::Recognize emergencies, acute kidney injury and fluid overload early and escalate.|G &middot; Teaching and transitions::Teach caregivers to safe independence and prepare adolescents for school, transplant and adult care.|H &middot; Quality::Document honestly, know who governs what in the Philippines, and calculate infection rates.}}}}
<p>Prerequisites: a current Philippine nursing license; adult dialysis training (for example Nephrology Nursing Modules 1 to 10) if you are new to dialysis, or a pediatric assessment and resuscitation refresher if you are new to children. Rare emergencies are practiced in simulation and recorded as simulation.</p>
""",
    "is_not": ("It is a training track written independently from published guidelines, research and Philippine issuances. It is not "
               "a license, PSN or National Kidney and Transplant Institute (NKTI) training, a PhilHealth staffing credential, CPD credit, "
               "or clinical privileges. No Philippine issuance reviewed for this track sets a separate pediatric dialysis nurse license "
               "or a pediatric nurse-to-patient ratio. It does not replace your unit&rsquo;s pediatric protocols, the device "
               "instructions for use, or the pediatric nephrologist&rsquo;s written orders."),
    "pathways_tag": "Eight weeks",
    "pathways_h2": "Eight weeks, 164 planned hours",
    "pathways_nav": "Weeks",
    "pathways_html": """
<p>The plan pairs about 84 hours of self-study and simulation with 80 hours of supervised exposure in an authorized pediatric setting: 42 study, 42 simulation and 80 supervised hours in all. These are design estimates. They are not equivalent to PSN structured renal training or PhilHealth-recognized PD training, and no child is exposed to risk to fill a log: rare events are simulated.</p>
<div class="table-wrap"><table>
<thead><tr><th>Week</th><th>Modules</th><th>Coached session</th><th>Supervised evidence</th><th>Competency</th></tr></thead>
<tbody>
<tr><td>1</td><td>1 &middot; Role and scope<br>2 &middot; Causes and modality<br>3 &middot; Development, assent and safeguarding</td><td>Explain dialysis to a six-year-old with a drawing; role-play assent with a teenager</td><td>A learning agreement; a communication plan for one child</td><td>A</td></tr>
<tr><td>2</td><td>4 &middot; Assessment and arithmetic<br>5 &middot; Infection prevention<br>6 &middot; Medication safety</td><td>Reconcile a 24-hour chart with a seeded decimal error; scrub-the-hub on a model</td><td>Reconciled chart; observed aseptic hub care</td><td>B, C</td></tr>
<tr><td>3</td><td>7 &middot; PD prescription<br>8 &middot; Catheter and exit site<br>9 &middot; CAPD</td><td>Convert fill volumes to mL/m&sup2;; score exit-site photographs; mock exchange with a dry and a wet breach</td><td>Order review; exit-site assessment; observed exchange</td><td>C, D</td></tr>
<tr><td>4</td><td>10 &middot; APD<br>11 &middot; Peritonitis</td><td>Cycler program cross-check; timed cloudy-bag call with SBAR</td><td>Cycler setup or record review; urgent call log</td><td>D, F</td></tr>
<tr><td>5</td><td>12 &middot; HD prescription and access<br>13 &middot; The small circuit<br>14 &middot; The session</td><td>Extracorporeal volume worksheet; first-session time-out</td><td>Pre-treatment check; observed session monitoring</td><td>E</td></tr>
<tr><td>6</td><td>15 &middot; Emergencies<br>16 &middot; AKI and CKRT</td><td>Hyperkalemia and air-embolism drills; fluid overload percentage from a PICU chart</td><td>Assessed simulation; ICU balance interpretation</td><td>F</td></tr>
<tr><td>7</td><td>17 &middot; Growth and nutrition<br>18 &middot; Caregiver teaching</td><td>Plot a growth chart; teach-back with a grandmother who reads poorly</td><td>Growth referral; return demonstration record</td><td>G</td></tr>
<tr><td>8</td><td>19 &middot; Adolescence and transition<br>20 &middot; Philippine practice and quality</td><td>Transition interview; infection-rate run chart</td><td>Capstone and portfolio</td><td>G, H</td></tr>
</tbody></table></div>
<p><strong>Before week 1.</strong> Confirm your license and resuscitation credentials, meet your preceptor, obtain the unit&rsquo;s pediatric protocols and device instructions, and get oriented to emergency procedures and incident reporting. <strong>After week 8.</strong> Continue supervised practice until every sign-off item is observed on the unit&rsquo;s own equipment and in the age and size band you will be assigned.</p>
""",
    "modules_h2": "Twenty modules in four parts",
    "modules_intro": ("Study the modules in order; Module 15 may be read early if you will be assigned to clinical work. Each starts "
                      "from a plain picture of what is happening, moves to the physiology and the evidence, and ends with what you do "
                      "at the bedside, with the family and in the record."),
    "syllabus_note": ("Each module takes about two to three hours to read and work through, plus coached practice. Skills checklists "
                      "are completed with a preceptor, in simulation first and then in supervised practice."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 15; the mastery mark is 4 of 5 on two different sets. The self-assessments are for learning. They tell you what to reread; they do not show that you can do the work.</p>
<div class="table-wrap"><table>
<thead><tr><th>Milestone</th><th>What it involves</th><th>Pass mark</th><th>Who records it</th></tr></thead>
<tbody>
<tr><td><strong>1 &middot; Academy study</strong></td><td>All twenty modules, cases and self-assessments; the end-of-track examination (40 questions, two from every module)</td><td>4 of 5 on two sets per module; 32 of 40 on the examination</td><td>You, in your own learning record</td></tr>
<tr><td><strong>2 &middot; Simulation</strong></td><td>Eight skills stations (see the trainer page)</td><td>Every critical behavior, each station</td><td>Preceptor</td></tr>
<tr><td><strong>3 &middot; Capstone</strong></td><td>Portfolio and one improvement proposal for a fictional pediatric program</td><td>Rubric, full credit for urgent responses</td><td>Nurse educator</td></tr>
<tr><td><strong>4 &middot; Facility authorization</strong></td><td>Observed practice on the unit&rsquo;s own devices, by modality, age and size band, with supervision level and review date</td><td>Independent and safe, critical items met</td><td>Authorized assessors, approved by the facility</td></tr>
</tbody></table></div>
<p>A critical failure in simulation or practice means stop, protect the child, debrief and reassess; a high quiz score cannot average it away. Completing milestone 1 never substitutes for milestone 4. Academy completion is an educational learning record only.</p>
""",
    "sources_html": """
<p>Clinical content follows the International Society for Peritoneal Dialysis (ISPD) 2024 pediatric infection guideline, the European Society for Paediatric Nephrology (ESPN) Dialysis Working Group&rsquo;s hemodialysis and vascular-access recommendations, the ISPD 2020 pediatric acute PD guideline, the Pediatric Renal Nutrition Taskforce, the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 CKD guideline, and the registries and quality collaboratives that supply most pediatric evidence: SCOPE, IPPN, AWARE and the prospective pediatric CRRT registry.[[pdn_warady2024]][[pdn_fischbach2005]][[pdn_shroff2019]][[pd_nourse2021]][[pdn_shaw2020]][[kdigo_ckd2024]][[pdn_neu2016]][[pdn_ploos2021]][[pdn_kaddourah2017]][[pdn_sutherland2010]]</p>
<p>Philippine requirements follow the Philippine Nursing Act, Department of Health licensing rules for dialysis facilities, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, and PhilHealth PD benefit issuances.[[pd_ra9173]][[doh2012]][[psn2024]][[pd_ph_sat]][[pc_pa2025_0074]][[pd_ph_pa2026]] Philippine pediatric dialysis registry figures were not available for this track; where the text gives numbers, it names their source and country.</p>
<h3>Requirements reference (reviewed November 27, 2026)</h3>
<div class="table-wrap"><table>
<thead><tr><th>Authority</th><th>Question it answers</th><th>What the review found</th></tr></thead>
<tbody>
<tr><td>Professional Regulation Commission (PRC) and Board of Nursing</td><td>Is the nurse lawfully authorized?</td><td>Current license; scope includes care of children and families</td></tr>
<tr><td>Department of Health (DOH) licensing of dialysis facilities</td><td>Is the facility licensed for the service?</td><td>Regional assessment tool lists licensed nurses with renal dialysis training, BLS, ACLS-trained nurse each shift, and 1:4 nurse-to-station staffing; not a pediatric-acuity standard</td></tr>
<tr><td>PSN hemodialysis guidelines (2024)</td><td>Professional expectations</td><td>Structured renal dialysis training; current BLS and ACLS</td></tr>
<tr><td>PhilHealth PD First self-assessment tool</td><td>PD program staffing and training</td><td>At least one full-time PD nurse; recognized PD training; nurse-to-patient wording &ldquo;1:20&rdquo; is a caseload statement needing interpretation</td></tr>
<tr><td>PhilHealth Advisories 2025-0074 and 2026-0013</td><td>Pediatric automated PD pilot</td><td>Pilot sites NKTI, UP-PGH and PCMC; extended to July 31, 2026; later status not verified</td></tr>
</tbody></table></div>
<p>Verify every row with the responsible office before a hiring, staffing or compliance decision, and confirm pediatric benefit status with the PhilHealth Regional Office before discussing coverage with a family.</p>
""",
    "trainers_intro": "A pediatric dialysis nurse educator or unit head can use these modules as the guided-study part of a new nurse&rsquo;s orientation. ",
    "trainer_h2": "Running the track with a new pediatric dialysis nurse",
    "trainer_html": """
<p><strong>Preparation.</strong> Obtain the facility&rsquo;s pediatric protocols and device instructions; prepare training-only PD bags and cycler sets, a training PD catheter, pediatric HD blood lines and a dialyzer for demonstration, central-line and fistula models, pediatric cuffs and scales, mock orders, simulated effluent, growth charts and blank records. Use fictional examples only, and orient learners to emergency procedures, safeguarding reporting and incident reporting before clinical exposure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Skills station and setup</th><th>Observable behaviors (critical in bold)</th></tr></thead>
<tbody>
<tr><td>1 &middot; Assent and consent with a 9-year-old and her father</td><td>Introduces self to the child first &middot; <strong>explains in words that fit her age and checks understanding</strong> &middot; seeks assent and parental consent separately &middot; <strong>responds to a safeguarding cue by following the reporting pathway</strong></td></tr>
<tr><td>2 &middot; Reconciled chart with a seeded unit error</td><td>Obtains a reliable weight &middot; reconciles every route &middot; <strong>calculates with units and an independent check</strong> &middot; <strong>stops when the order and the machine entry disagree</strong></td></tr>
<tr><td>3 &middot; CAPD exchange with a wet contamination</td><td><strong>Verifies identity, order and fill volume in mL and mL/m&sup2;</strong> &middot; protects key parts &middot; <strong>stops at the breach, clamps, and calls for the prophylaxis decision</strong> &middot; records volumes</td></tr>
<tr><td>4 &middot; APD with a low-drain alarm and a mismatched program</td><td><strong>Cross-checks the cycler program against the order</strong> &middot; reads the alarm as a clinical signal &middot; <strong>escalates without override</strong> &middot; documents missed therapy</td></tr>
<tr><td>5 &middot; Cloudy effluent with fever at home (telephone)</td><td><strong>Screens for sepsis and routes emergency care</strong> &middot; keeps the bag and arranges sampling after an adequate dwell &middot; SBAR with read-back &middot; time-stamps the call</td></tr>
<tr><td>6 &middot; Pediatric HD time-out</td><td><strong>Confirms weight, extracorporeal volume as a share of blood volume, and priming plan</strong> &middot; checks blood flow against size &middot; scrub-the-hub &middot; <strong>does not start with an unresolved discrepancy</strong></td></tr>
<tr><td>7 &middot; Emergency on dialysis (hyperkalemia arrhythmia or air in the venous line)</td><td><strong>Stops the pump and clamps appropriately</strong> &middot; calls the team and starts pediatric resuscitation as trained &middot; assigns roles &middot; structured handover</td></tr>
<tr><td>8 &middot; Caregiver return demonstration and transition handoff</td><td>Uses teach-back &middot; <strong>withholds readiness sign-off after an unsafe step</strong> &middot; plans retraining &middot; completes an I-PASS handoff</td></tr>
</tbody></table></div>
<p>Allow 10 minutes for each station plus 5 minutes of feedback. Pass with every critical behavior. Pause any unsafe simulated action, debrief, and retest with a different setup.</p>
<p>Record each observation with learner, date, setting, modality, the child&rsquo;s age and size band, equipment and procedure version, simulation or clinical, prompted or independent, critical items, next step and assessor signature. Keep signed records in the facility&rsquo;s approved system, never on this site. Reassess after a relevant incident, an extended absence, a change of device or protocol, and at the facility&rsquo;s scheduled interval.</p>
""",
    "completion_html": """
<ul>
<li><strong>Academy study:</strong> self-assessments at 4 of 5 on two different sets for each module, and the examination at 32 of 40.</li>
<li><strong>Simulation:</strong> all eight stations passed with every critical behavior.</li>
<li><strong>Facility authorization:</strong> observed practice signed by authorized assessors, specifying modality, age and size band, device, supervision level and review date.</li>
</ul>
<p>Completing the Academy track is an educational learning record. It is not CPD credit, PhilHealth staffing credit, recognized PD or HD training, or clinical privileges.</p>
""",
    "related": [("peritoneal-dialysis-ckd.html", "The site&rsquo;s patient guide to peritoneal dialysis."),
                ("born-small-kidneys-for-life.html", "Birth weight, prematurity and lifelong kidney risk.")],
}

W = ["Part A &middot; Foundations (weeks 1&ndash;2)", "Part B &middot; Peritoneal dialysis (weeks 3&ndash;4)",
     "Part C &middot; Hemodialysis and acute care (weeks 5&ndash;6)", "Part D &middot; Growing up on dialysis (weeks 7&ndash;8)"]

_ROWS = [
    ("01", "role-scope-and-the-childs-journey", "The Pediatric Dialysis Nurse: Role, Scope and the Child&rsquo;s Journey", 0, (2, 2, 4)),
    ("02", "pediatric-kidney-failure-and-modality", "Why Children&rsquo;s Kidneys Fail, and How a Modality Is Chosen", 0, (2, 2, 4)),
    ("03", "development-assent-consent-and-safeguarding", "Development, Assent, Consent and Safeguarding", 0, (2, 2, 4)),
    ("04", "assessment-fluid-and-calculations", "Assessment, Fluid Balance and Weight-Based Arithmetic", 0, (2, 2, 4)),
    ("05", "infection-prevention-and-access-protection", "Infection Prevention and Access Protection", 0, (2, 2, 4)),
    ("06", "medication-safety", "Medication Safety in Children on Dialysis", 0, (2, 2, 4)),
    ("07", "pd-physiology-and-prescription", "PD in Children: Physiology, Readiness and the Prescription", 1, (2, 2, 4)),
    ("08", "pd-catheter-and-exit-site", "The PD Catheter, Exit Site and Mechanical Problems", 1, (2, 2, 4)),
    ("09", "capd-supervised-exchange", "CAPD: A Supervised Exchange in a Small Body", 1, (2, 2, 4)),
    ("10", "apd-cycler-and-home-monitoring", "APD: Cycler Setup, Alarms and Home Monitoring", 1, (2, 2, 4)),
    ("11", "pd-peritonitis-and-exit-site-infection", "PD Peritonitis and Exit-Site Infection: The First Hour", 1, (2, 2, 4)),
    ("12", "hd-prescription-and-vascular-access", "Pediatric Hemodialysis: Prescription Logic and Vascular Access", 2, (2, 2, 4)),
    ("13", "hd-circuit-water-and-preparation", "The Small Circuit: Blood Volume, Priming, Water and Preparation", 2, (2, 2, 4)),
    ("14", "hd-session-monitoring", "The Hemodialysis Session: Initiation, Monitoring and Completion", 2, (2, 2, 4)),
    ("15", "emergencies-and-resuscitation", "Emergencies and Pediatric Resuscitation Readiness", 2, (3, 4, 4)),
    ("16", "aki-acute-pd-and-ckrt", "AKI, Acute PD and Continuous Kidney Replacement Therapy", 2, (2, 2, 4)),
    ("17", "growth-nutrition-anemia-and-bone", "Growth, Nutrition, Anemia and Bone", 3, (2, 2, 4)),
    ("18", "caregiver-teaching-and-home", "Teaching Caregivers, Home Support and Disaster Planning", 3, (2, 2, 4)),
    ("19", "adolescence-school-transplant-transition", "Adolescence, School, Transplant and Transition", 3, (2, 2, 4)),
    ("20", "philippine-practice-quality-capstone", "Philippine Requirements, Records, Quality and Capstone", 3, (3, 2, 4)),
]


def _load(name):
    s = _u.spec_from_file_location("_pdn_" + name, _P(__file__).with_name(name + ".py"))
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return m


SUBS = _load("subs").SUBS
MODULES = []
for _id, _slug, _title, _w, _h in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": SUBS[int(_id)], "part": W[_w],
                    "hours": _h, "card_img": f"{HUB}-{_id}-card.webp"})

COURSE["hub_sections"] = _load("hub").HUB_SECTIONS
