# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse: a Nephrology Nursing specialty subtrack, in the POD/DCH package schema.
Built from the PD Nurse v2 blueprint (~/Documents/PD Nurse/v2). Every case and record is fictional.
Lesson IDs PD01 to PD12 map to module ids 01 to 12; slugs follow the blueprint filenames."""

HUB = "peritoneal-dialysis-nurse"
NN10 = "nephrology-nursing-10-pd-home-dialysis-nursing.html"

COURSE = {
    "title": "Peritoneal Dialysis Nurse",
    "short": "PD Nurse",
    "hub_slug": HUB,
    "label": "Nephrology Nursing specialty subtrack for peritoneal dialysis",
    "tag": "Nephrology Nursing &middot; Specialization",
    "icon": "💧",
    "no_branch": True,
    "audience": ("Philippine-licensed registered nurses entering adult peritoneal dialysis practice &middot; PD nurse educators and preceptors"),
    "audience_type": "Registered nurses in peritoneal dialysis",
    "level": "Registered nurses who have completed Nephrology Nursing Module 10",
    "review_date": "2026-11-24",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("peritoneal dialysis nurse Philippines, PD nurse training, CAPD APD nursing, PD peritonitis nursing ISPD 2022, "
                 "PD exit site infection ISPD 2023, peritoneal equilibration test nursing, PhilHealth PD First Z benefit, "
                 "assisted peritoneal dialysis, PD patient teaching, Renal Care Academy"),
    "page_title": "Peritoneal Dialysis Nurse: A Nephrology Nursing Specialty Track",
    "desc": ("A free six-week specialty track for registered nurses in peritoneal dialysis: physiology, home readiness, the catheter and exit site, "
             "CAPD and APD, goal-directed monitoring, peritonitis, urgent problems, teaching, transitions, special populations, and Philippine "
             "practice and quality. Cases, skills checklists, and a self-assessment in every module."),
    "h1": "Peritoneal Dialysis <em>Nurse</em>",
    "sub": ("A specialty track for registered nurses in peritoneal dialysis. Learn why each step protects the patient, read the small numbers "
            "that warn early, and know exactly when to call."),
    "disclaimer": ("Educational material for registered nurses. Completing it is an Academy learning record only. It does not confer CPD units, "
                   "PSN or National Kidney and Transplant Institute (NKTI) training recognition, PhilHealth staffing credit, or clinical privileges, and it does not replace your facility&rsquo;s "
                   "protocols, device instructions, or written orders."),
    "scope_note": ("This module is study material for registered nurses in adult peritoneal dialysis (PD). It explains the reasoning behind common nursing "
                   "decisions; it is not a procedure. Exact steps follow your unit&rsquo;s protocol and the device instructions; treatment parameters follow "
                   "the written order. Nurses assess, verify, teach, document and escalate; prescription and medication decisions belong to the "
                   "nephrologist. Every case is fictional. Pending clinical review by a PD nephrologist and a PD nurse educator."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Specialty subtrack &middot; registered nurses",
    "branch_blurb": ("For registered nurses in peritoneal dialysis: physiology, readiness, the catheter, CAPD and APD, monitoring, peritonitis, "
                     "urgent problems, teaching, transitions, and quality. Part of Nephrology Nursing; continues Module 10."),
    "parent": ("nephrology-nursing.html", "Nephrology Nursing",
               "The parent course. Module 10 introduces peritoneal dialysis and home dialysis nursing."),
    "academy_meta": "12 modules &middot; six weeks &middot; five skills stations",
    "hero_alt": "A peritoneal dialysis nurse kneeling beside a seated patient at a clean home exchange corner while the patient's grandson watches from the doorway.",
    "start_h2": "The nurse in the home program",
    "start_html": f"""
<p>Most Filipinos with kidney failure start dialysis in a hemodialysis center, often after an urgent admission. Peritoneal dialysis (PD) lets many of them dialyze at home instead, with fewer trips, no needles, and more control of the day. It also asks a great deal: a catheter that must stay clean for years, a technique repeated more than a thousand times a year, and a person at home who must recognize trouble early. Internationally, nearly half of people who start PD are no longer on it at two years.[[pd_quinn2026]] Peritonitis, technique drift and unplanned transfers explain much of that, and the PD nurse is the program&rsquo;s main defense against all three.</p>
<p>This track continues <a href="{NN10}">Nephrology Nursing Module 10: Peritoneal Dialysis and Home Dialysis Nursing</a>. It takes a registered nurse from the physiology of a single dwell to the quality numbers of a whole program, in twelve modules over six weeks.</p>
{{{{cards:Exit competencies|A &middot; Readiness::Explain PD physiology, support an informed modality choice, and assess patient and home readiness.|B &middot; Technique and access::Verify treatment, demonstrate aseptic continuous ambulatory PD (CAPD) and automated PD (APD), and assess the catheter and exit site using International Society for Peritoneal Dialysis (ISPD) 2023 definitions.|C &middot; Triage::Triage infection, contamination, mechanical and volume problems, and close the loop.|D &middot; Teaching::Teach patients and caregivers, judge readiness by return demonstration and teach-back, and plan retraining.|E &middot; Monitoring and transitions::Monitor goal-directed treatment, collect valid samples, and hand over safely between home and hospital.|F &middot; Quality::Calculate PD infection and loss-from-PD indicators against ISPD targets and improve one thing at a time.}}}}
<p>Prerequisites: a current Philippine nursing license, Nephrology Nursing Module 10 or equivalent, and basic infection prevention and medication safety. Rare emergencies are practiced in simulation, and every simulated event is recorded as simulation.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published guidelines, research and Philippine issuances. It is not a license, PSN or "
               "National Kidney and Transplant Institute (NKTI) training, a PhilHealth staffing credential, CPD credit, or clinical privileges. It does not replace your unit&rsquo;s protocols, the device "
               "instructions for use, or the nephrologist&rsquo;s written orders."),
    "pathways_tag": "Six weeks",
    "pathways_h2": "Six weeks, sixty planned hours",
    "pathways_nav": "Weeks",
    "pathways_html": """
<p>Each week pairs two modules with about four hours of self-study and case work, two hours of simulation or coached review, and four hours of supervised practice or structured observation: 24, 12 and 24 hours in all. These are design estimates. Extend supervised practice until the required opportunities and your facility&rsquo;s criteria are met, and record rare events practiced in simulation as simulation.</p>
<div class="table-wrap"><table>
<thead><tr><th>Week</th><th>Modules</th><th>Coached session</th><th>Supervised evidence</th><th>Competency</th></tr></thead>
<tbody>
<tr><td>1</td><td>1 &middot; How PD works<br>2 &middot; Modality counseling and readiness</td><td>Explain the three-pore model with a drawing; conduct a readiness interview with a role-player</td><td>A shared decision or readiness plan with owners and a reassessment date</td><td>A</td></tr>
<tr><td>2</td><td>3 &middot; Catheter and exit site<br>4 &middot; The manual exchange</td><td>Grade exit sites from photographs; mock exchange with a seeded packaging defect and a dry and a wet breach</td><td>Exit-site and tunnel assessment; an observed exchange</td><td>B</td></tr>
<tr><td>3</td><td>5 &middot; The cycler<br>6 &middot; Monitoring and membrane testing</td><td>Cross-check a cycler program against a mock order; time peritoneal equilibration test samples</td><td>Cycler setup or record review; a longitudinal nursing note</td><td>B, E</td></tr>
<tr><td>4</td><td>7 &middot; Peritonitis<br>8 &middot; Mechanical and urgent problems</td><td>Timed cloudy-bag call with SBAR; after-hours power-failure drill</td><td>Supervised triage call or scenario log</td><td>C</td></tr>
<tr><td>5</td><td>9 &middot; Teach, validate, retrain<br>10 &middot; Longitudinal care and transitions</td><td>Teach-back lab with a learner who reads poorly; ward handoff with an icodextrin alert</td><td>Readiness and retraining records; a supervised handoff</td><td>D, E</td></tr>
<tr><td>6</td><td>11 &middot; Pediatric, acute and assisted PD<br>12 &middot; Philippine practice and quality</td><td>Assistance plan for a stroke survivor; infection-rate calculation and run chart</td><td>Capstone and quality exercise</td><td>E, F</td></tr>
</tbody></table></div>
<p><strong>Before week 1.</strong> Confirm your current PRC license, complete Nephrology Nursing Module 10, meet your preceptor, obtain the unit&rsquo;s PD protocols and device instructions, and get oriented to emergency procedures and incident reporting. <strong>After week 6.</strong> Continue supervised practice until every sign-off item is observed on the unit&rsquo;s own equipment.</p>
""",
    "modules_h2": "Twelve modules in six weeks",
    "modules_intro": ("Study the modules in order. Each starts from a plain picture of what is happening, moves to the physiology and the evidence, "
                      "and ends with what you do at the bedside, on the phone, and in the record."),
    "syllabus_note": ("Each module takes about 2.5 to 3.5 hours to read and work through, plus coached practice. Skills checklists are completed with a "
                      "preceptor, in simulation first and then in supervised practice."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 15; the mastery mark is 4 of 5 on two different sets. The self-assessments are for learning. They tell you what to reread; they do not show that you can do the work.</p>
<div class="table-wrap"><table>
<thead><tr><th>Milestone</th><th>What it involves</th><th>Pass mark</th><th>Who records it</th></tr></thead>
<tbody>
<tr><td><strong>1 &middot; Academy training</strong></td><td>All twelve modules, cases and self-assessments; the end-of-track examination (40 questions from all banks)</td><td>4 of 5 on two sets per module</td><td>You, in your own learning record</td></tr>
<tr><td><strong>2 &middot; Knowledge check</strong></td><td>A 24-point faculty check built from questions kept off the learner pages</td><td>20 of 24</td><td>Nurse educator</td></tr>
<tr><td><strong>3 &middot; Simulation</strong></td><td>Five skills stations: manual exchange, cycler setup, cloudy-bag call, exit site and low drain, teaching a learner with limited vision</td><td>4 of 5 per station, every critical behavior</td><td>Preceptor</td></tr>
<tr><td><strong>4 &middot; Capstone</strong></td><td>Readiness and risk plan, urgent SBAR, follow-up note and one improvement aim for a fictional CAPD patient</td><td>8 of 10, full credit for the urgent response</td><td>Nurse educator</td></tr>
<tr><td><strong>5 &middot; Clinical sign-off</strong></td><td>Observed practice on the unit&rsquo;s own devices: two manual exchanges, two cycler setups or reviews, two exit-site assessments, one readiness or training encounter, one handoff</td><td>Independent and safe, critical items met</td><td>Preceptor, approved by the facility</td></tr>
</tbody></table></div>
<p><strong>Remediation.</strong> When a domain is weak, the preceptor arranges coached practice and reassesses on an equivalent case. When consent or opportunities limit observation, the gap is recorded and the affected task is deferred or supervised longer. Reassessment is triggered by a relevant incident, an extended absence, a change of device or protocol, and the facility&rsquo;s scheduled interval.</p>
<p>Completing milestone 1 or 3 never substitutes for milestone 5. Academy completion is an educational learning record only.</p>
""",
    "sources_html": """
<p>Clinical content follows the International Society for Peritoneal Dialysis (ISPD) recommendations on peritonitis (2022), catheter-related infection (2023), goal-directed prescribing (2020), membrane evaluation (2021), access (2019), acute PD (2020), assisted PD (2024), teaching PD (2025), nutrition with the International Society of Renal Nutrition and Metabolism (2026), and tracking loss from PD therapy (2026), together with the trials and cohorts they rest on.[[pd_li2022]][[pd_chow2023]][[pd_brown2020]][[pd_morelle2021]][[pd_crabtree2019]][[pd_cullis2021]][[pd_oliver2024]][[pd_chow2025]][[pd_wang2026]][[pd_quinn2026]][[pd_perl2020]]</p>
<p>Philippine requirements follow the Philippine Nursing Act, PhilHealth PD Z-benefit contracting, and the PD First self-assessment tool.[[pd_ra9173]][[pd_ph_pc2024]][[pd_ph_sat]][[pd_ph_pa2026]] Where Philippine figures are not available from a registry, the text names the source and labels press reports as such.</p>
<h3>Requirements reference (reviewed November 24, 2026)</h3>
<div class="table-wrap"><table>
<thead><tr><th>Authority</th><th>Question it answers</th><th>Evidence to keep</th></tr></thead>
<tbody>
<tr><td>Professional Regulation Commission (PRC) and Board of Nursing</td><td>Is the nurse lawfully authorized to practice?</td><td>Current PRC license; facility privilege record</td></tr>
<tr><td>Department of Health and its Health Facilities and Services Regulatory Bureau (HFSRB)</td><td>Is the facility licensed for the service it provides?</td><td>License to operate or written applicability determination for a PD service</td></tr>
<tr><td>PhilHealth PD Z-benefit contracting</td><td>Is the facility contracted, the patient eligible, the episode documented?</td><td>Current contract, annexes, rosters, training certificates, patient records</td></tr>
<tr><td>PhilHealth PD First self-assessment tool</td><td>Staffing and training standard</td><td>At least one full-time PD nurse; nurse-to-patient ratio stated as 1:20; PRC license; recognized PD training; unit head validation</td></tr>
<tr><td>Philippine Society of Nephrology and National Kidney and Transplant Institute (NKTI)</td><td>Recognized training pathways</td><td>Course title, dates, duration, CPD listing, and acceptance for your setting</td></tr>
</tbody></table></div>
<p>Verify every row against the current issuance with the responsible office before a hiring or compliance decision. Benefit amounts, pediatric benefit status after July 31, 2026, and region-specific text must be confirmed with the PhilHealth Regional Office.</p>
""",
    "trainers_intro": "A PD nurse educator or unit head can use these modules as the guided-study part of a new PD nurse&rsquo;s orientation. ",
    "trainer_h2": "Running the track with a new PD nurse",
    "trainer_html": """
<p><strong>Preparation.</strong> Obtain the facility protocols and device instructions; prepare training-only bags and cycler consumables, a training catheter, personal protective equipment, mock orders, simulated effluent, labels, a mock escalation roster and blank charts. Use fictional or approved de-identified examples, and orient learners to scope of practice, emergency procedures and reporting before clinical exposure.</p>
<p><strong>Knowledge check.</strong> Use the twelve module self-check pairs as a 24-point bank kept off learner pages. One point per item when every essential element of the model answer is present; threshold 20 of 24. If an item has been exposed, change the scenario while keeping the required decisions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Skills station and setup</th><th>Five observable behaviors (critical in bold)</th></tr></thead>
<tbody>
<tr><td>1 &middot; CAPD with a mock order and a compromised bag</td><td><strong>Verifies identity and prescription</strong> &middot; <strong>rejects the compromised supply</strong> &middot; <strong>protects critical parts and stops at a breach</strong> &middot; demonstrates the device flow with the approved checklist &middot; records volumes and appearance</td></tr>
<tr><td>2 &middot; APD with a scripted alarm and a mismatched prescription</td><td><strong>Verifies the cycler program against the order</strong> &middot; <strong>prevents a contaminated connection</strong> &middot; identifies allowed external checks &middot; <strong>escalates an unresolved alarm without override</strong> &middot; records completed and missed treatment</td></tr>
<tr><td>3 &middot; Infection call, cloudy bag with pain</td><td><strong>Recognizes urgency and activates the PD pathway</strong> &middot; <strong>checks for instability and routes emergency care as indicated</strong> &middot; preserves the specimen and coordinates sampling &middot; relays SBAR with read-back &middot; time-stamps contact and disposition</td></tr>
<tr><td>4 &middot; Exit site and low drain, photographs and log</td><td>Obtains symptoms and effluent data &middot; assesses exit-site and tunnel findings &middot; <strong>avoids forceful unapproved manipulation</strong> &middot; <strong>triages severe symptoms and closes the loop</strong> &middot; records action and response</td></tr>
<tr><td>5 &middot; Home readiness, learner with limited vision</td><td>Assesses barriers and preferences &middot; demonstrates and adapts instruction &middot; observes independent return demonstration &middot; <strong>withholds readiness sign-off after unsafe performance</strong> &middot; specifies coaching, support and reassessment</td></tr>
</tbody></table></div>
<p>Allow 10 minutes for each station plus 5 minutes of feedback. Pass at 4 of 5 with every critical behavior. Pause any unsafe simulated action, debrief, and retest with a different setup.</p>
<p><strong>Supervised evidence (educational targets).</strong> Two satisfactory observed CAPD exchanges, two APD setup or treatment reviews including an observed setup, two exit-site assessments, one home readiness or training encounter, and one supervised handoff, plus documented simulations for urgent events. Credentialing follows current facility and contracting criteria.</p>
<p><strong>Capstone.</strong> A fictional new adult CAPD patient with limited storage and a caregiver available only in the evenings; after initial teaching, a log of falling drain volumes and a message about cloudy effluent. The learner writes a one-page readiness and risk plan, an immediate SBAR, a follow-up nursing note and one measurable improvement aim. Score 0 to 2 for each of readiness feasibility, urgent response, closed-loop documentation, interprofessional coordination and metric definition; pass at 8 of 10 with full credit for the urgent response.</p>
<p>Record each observation with learner ID, date and site, competency and device, simulation or clinical, prompted or independent or deferred, critical items met, next step and preceptor signature. Keep signed records and credential evidence in the facility&rsquo;s approved system, never on this site. Reassess after relevant incidents, extended absence, a change of device or protocol, and at the facility&rsquo;s scheduled interval.</p>
""",
    "completion_html": """
<ul>
<li><strong>Academy training:</strong> self-assessments at 4 of 5 on two different sets for each module, with missed questions reviewed.</li>
<li><strong>Simulation:</strong> all five skills stations passed at 4 of 5 with every critical behavior, and urgent events rehearsed.</li>
<li><strong>Clinical sign-off:</strong> observed practice signed by the preceptor and approved by the facility, with any deferred task and its supervision plan recorded.</li>
</ul>
<p>Completing the Academy track is an educational learning record. It is not CPD credit, PhilHealth staffing credit, recognized PD training, or clinical privileges.</p>
""",
    "related": [("peritoneal-dialysis-ckd.html", "The site&rsquo;s patient guide to peritoneal dialysis."),
                ("adding-peritoneal-dialysis-program.html", "Starting and running a PD program.")],
}

W = ["Week 1 &middot; Foundations", "Week 2 &middot; Access and CAPD", "Week 3 &middot; APD and monitoring",
     "Week 4 &middot; Infection and urgent problems", "Week 5 &middot; Teaching and transitions", "Week 6 &middot; Special populations and quality"]

_ROWS = [
    ("01", "fundamentals-and-role", "How PD Works, and What the PD Nurse Does", 0),
    ("02", "selection-and-home-readiness", "Modality Counseling, Shared Decisions and Home Readiness", 0),
    ("03", "access-and-exit-site-care", "The Catheter, the Tunnel and the Exit Site", 1),
    ("04", "capd", "The Manual Exchange: Measurement and Contamination", 1),
    ("05", "apd", "The Cycler: Setup, Treatment Record and Alarms", 2),
    ("06", "goal-directed-monitoring", "Monitoring, Membrane Testing and Goal-Directed PD", 2),
    ("07", "infection-and-peritonitis", "Peritonitis: Recognition, Sampling and Prevention", 3),
    ("08", "mechanical-and-urgent-problems", "Mechanical, Volume and Urgent Problems", 3),
    ("09", "patient-and-caregiver-teaching", "Teach, Validate and Retrain", 4),
    ("10", "longitudinal-and-transitional-care", "Longitudinal Care, Nutrition and Safe Transitions", 4),
    ("11", "special-populations", "Pediatric, Acute and Assisted PD", 5),
    ("12", "philippine-practice-and-quality", "Philippine Practice, Records and Quality", 5),
]
SUBS = {}
try:
    from pathlib import Path as _P
    import importlib.util as _u
    _s = _u.spec_from_file_location("_pd_subs", _P(__file__).with_name("subs.py"))
    _m = _u.module_from_spec(_s); _s.loader.exec_module(_m); SUBS = _m.SUBS
except Exception:
    pass

MODULES = []
for _id, _slug, _title, _w in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": SUBS.get(int(_id), _title), "part": W[_w],
                    "hours": (2, 1, 2), "card_img": f"{HUB}-{_id}-card.webp"})

try:
    _h = _u.spec_from_file_location("_pd_hub", _P(__file__).with_name("hub.py"))
    _hm = _u.module_from_spec(_h); _h.loader.exec_module(_hm)
    COURSE["hub_sections"] = _hm.HUB_SECTIONS
except Exception as _e:  # surface the problem at build time rather than silently dropping content
    raise
