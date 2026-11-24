# -*- coding: utf-8 -*-
"""Extra course-home sections for the Peritoneal Dialysis Nurse track (COURSE["hub_sections"]).
Each entry is placed before an existing course-home section id (start, pathways, modules, how, syllabus,
assessment, sources, trainers). Content comes from the PD Nurse v2 blueprint (SYLLABUS, REQUIREMENTS,
FACULTY, WORKSHEETS, CALCULATORS) and the verified sources in refs.py. Every case and record is fictional."""


def _calc(f, title, desc):
    return (f'  <a href="{f}" class="calc-card">\n    <div class="calc-card-icon">⌬</div>\n    <div class="calc-card-body">\n'
            f'      <div class="calc-card-title">{title}</div>\n      <div class="calc-card-desc">{desc}</div>\n    </div>\n'
            f'    <span class="calc-card-arrow">Open →</span>\n  </a>')


_CALCS = [
    ("calc-pd-adequacy.html", "Peritoneal Dialysis Adequacy", "Weekly Kt/V and creatinine clearance, with the residual kidney contribution. Modules 1, 5 and 6."),
    ("calc-pd-glucose-absorption.html", "Glucose Absorption in Peritoneal Dialysis", "Glucose and calories absorbed from the solution. Modules 4, 6 and 10."),
    ("calc-fluid-overload.html", "Cumulative Fluid Balance", "Fluid gained over several days as a share of body weight. Module 8."),
    ("calc-dialysis-continuity-planner.html", "Dialysis Continuity Planner", "Contacts, supplies and backup plans for outages and typhoons. Modules 2, 5 and 8."),
    ("calc-starting-dialysis-planner.html", "Starting Dialysis Planner", "Timing and preparation questions before the first exchange. Module 2."),
    ("calc-frailty-assessment.html", "Frailty Assessment", "Standard questions and simple physical measures for the readiness assessment. Modules 2 and 11."),
    ("calc-nutrition-screening.html", "Malnutrition Screening", "Short validated screening tools for nutritional risk. Modules 6 and 10."),
    ("calc-potassium-load.html", "Dietary Potassium Estimator", "Potassium in common Filipino foods, for dietitian-guided review of low potassium. Module 10."),
    ("calc-aki-staging.html", "Acute Kidney Injury Staging", "Severity staging for the acute PD orientation. Module 11."),
    ("calc-pediatric-egfr.html", "Pediatric Kidney Function Estimate", "Context for the pediatric orientation; prescriptions belong to the pediatric team. Module 11."),
    ("calc-qapi-run-chart-spc.html", "Run Chart and Control Chart Generator", "Plot a monthly infection rate and mark each change. Modules 7 and 12."),
    ("calc-qapi-cqi-toolkit.html", "Improvement Method Worksheets", "Small tests of change and cause analysis. Module 12."),
    ("calc-dialysis-qapi-scorecard.html", "Dialysis Unit Quality Scorecard", "A monthly scorecard for unit quality indicators. Module 12."),
]

HUB_SECTIONS = [
    # ── The role ────────────────────────────────────────────────────────────
    {"id": "role", "nav": "The role", "tag": "The role", "before": "pathways",
     "h2": "What a peritoneal dialysis nurse does",
     "html": """
<p>A PD nurse is part clinician, part teacher, part coordinator. Most of the work happens away from the patient: on the telephone at 6 AM, in a training room with a nervous caregiver, at a kitchen table during a home visit, or in a ward explaining to a colleague how a cycler works. The patient does the treatment; you make sure they can, and you notice early when something is going wrong.</p>
<p>The proposed Philippine job description below was written for this track from the blueprint&rsquo;s review of Philippine requirements and international employer postings. A facility should adapt it to its own policies and the current PhilHealth contract.</p>
{{cards:Proposed job description|Purpose::Provide safe nursing care and coordinate patient and caregiver readiness for prescribed PD across clinic, home and hospital.|Reports to::The PD unit or center head, or a designated nursing supervisor. Works with the nephrologist, access team, pharmacy, dietitian, infection prevention, social work and benefits staff.|Assess and plan::Symptoms, volume status, home readiness, caregiver capacity and barriers to adherence; develop and review the nursing plan.|Verify and deliver::Check prescriptions and supplies; perform delegated procedures and monitor CAPD and APD under written orders, competencies and protocols.|Teach and validate::Demonstration, teach-back and return demonstration; document readiness; schedule retraining.|Triage and escalate::Cloudy effluent, abdominal pain, contamination, exit-site change, poor flow, volume deterioration and equipment failure; close the loop.|Coordinate::Access care, referrals, specimens, supplies, emergency plans, hospital transitions and follow-up.|Record and improve::Nursing and training records, benefit documentation, infection and safety reports, and outcome review with the team.}}
<h3>Where your role stops</h3>
<p>Under the Philippine Nursing Act (Republic Act 9173), nursing practice includes assessment, health teaching, collaboration and carrying out written orders.[[pd_ra9173]] In PD that becomes a clear division of labor:</p>
<div class="table-wrap"><table>
<thead><tr><th>You do</th><th>You route to the nephrologist or authorized prescriber</th></tr></thead>
<tbody>
<tr><td>Verify the patient, modality, solution, strength and volumes against the written order</td><td>Any change in solution, dwell, cycler program or icodextrin use</td></tr>
<tr><td>Compare the treatment actually delivered with the treatment ordered</td><td>Any medicine started, stopped or changed, including antibiotics</td></tr>
<tr><td>Assess fluid status, symptoms, exit site, tunnel and effluent</td><td>Interpreting adequacy and membrane tests for a prescription change</td></tr>
<tr><td>Teach, observe return demonstration and judge readiness against program criteria</td><td>Modality change, catheter procedures and admission decisions</td></tr>
<tr><td>Triage calls, activate the PD pathway and document a closed-loop handoff</td><td>Diagnosing peritonitis and choosing its treatment</td></tr>
<tr><td>Help assemble PhilHealth documentation as instructed</td><td>Eligibility and payment decisions, which stay with authorized benefits staff</td></tr>
</tbody></table></div>
{{key:The line is not about importance. Your observations are often the team&rsquo;s first warning. Report the pattern with numbers and times; leave the prescription to the prescriber.}}
<h3>Staffing, experience and how other countries set the bar</h3>
<p>The PhilHealth PD First self-assessment tool lists at least one full-time PD nurse, a nurse-to-patient ratio stated as 1:20, a current license from the Professional Regulation Commission (PRC), and recognized PD training through the listed pathways with validation by the unit head.[[pd_ph_sat]] Do not import the hemodialysis 1:4 ratio into PD; the workload is different. Confirm with the PhilHealth Regional Office how caseload and coverage are counted for your contract.[[pd_ph_pc2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>What the example shows</th><th>What this track takes from it</th></tr></thead>
<tbody>
<tr><td>Philippines (hospital posting)</td><td>An employer posting for a PD nurse calls for a licensed nurse and prefers one year of PD experience, with emphasis on assessment, problem solving and patient teaching.</td><td>Track experience as a hiring criterion, separate from course completion.</td></tr>
<tr><td>United States (federal rule)</td><td>The registered nurse responsible for home training must have at least 12 months of nursing experience plus 3 months in the specific modality; certified facilities must train patients, plan for emergencies and keep training records.[[pd_cfr494140]][[pd_cfr494100]]</td><td>Document modality experience, caregiver training, retraining after change, and emergency planning.</td></tr>
<tr><td>United Kingdom and Canada (employer postings)</td><td>Senior PD nurse roles include caseload coordination, education, home visits, leadership, audit and quality improvement.</td><td>Include home visits, teaching, audit and improvement in the role from the start.</td></tr>
</tbody></table></div>
"""},

    # ── Competency map ─────────────────────────────────────────────────────
    {"id": "competencies", "nav": "Competencies", "tag": "Outcomes", "before": "pathways",
     "h2": "Six exit competencies, mapped to the modules",
     "html": """
<p>Every module builds toward six observable competencies. The table shows where each is taught and how a preceptor gathers the evidence.</p>
<div class="table-wrap"><table>
<thead><tr><th>Competency</th><th>Taught in</th><th>Evidence a preceptor collects</th></tr></thead>
<tbody>
<tr><td><strong>A &middot; Readiness.</strong> Explain PD, support an informed modality choice, and assess patient and home readiness.</td><td>Modules 1, 2, 11</td><td>Structured readiness interview and a documented plan with owners and a reassessment date</td></tr>
<tr><td><strong>B &middot; Technique and access.</strong> Verify treatment, demonstrate aseptic CAPD and APD, and assess the catheter and exit site.</td><td>Modules 3, 4, 5</td><td>Direct observation; skills stations 1 and 2</td></tr>
<tr><td><strong>C &middot; Triage.</strong> Recognize infection, contamination, mechanical and volume problems, escalate, and close the loop.</td><td>Modules 3, 7, 8</td><td>Supervised calls, charting; skills stations 3 and 4</td></tr>
<tr><td><strong>D &middot; Teaching.</strong> Teach patients and caregivers, judge readiness by return demonstration and teach-back, and plan retraining.</td><td>Modules 2, 9</td><td>Teaching observation; skills station 5</td></tr>
<tr><td><strong>E &middot; Monitoring and transitions.</strong> Review goal-directed treatment, collect valid samples, hand over safely, and support benefit documentation.</td><td>Modules 5, 6, 10, 11, 12</td><td>Chart audit, longitudinal nursing note, handoff; capstone</td></tr>
<tr><td><strong>F &middot; Quality.</strong> Calculate infection and loss-from-PD indicators against international targets and test one improvement.</td><td>Modules 7, 12</td><td>Rate calculation, run chart and improvement aim</td></tr>
</tbody></table></div>
"""},

    # ── Evidence at a glance ───────────────────────────────────────────────
    {"id": "evidence", "nav": "Key evidence", "tag": "Evidence", "before": "modules",
     "h2": "The numbers a PD nurse should know",
     "html": """
<p>These are the findings the track returns to most often. Each is explained in its module with the design and limits of the study; the verbs here are chosen to match the strength of the evidence.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>What it shows</th><th>Strength</th><th>Module</th></tr></thead>
<tbody>
<tr><td>Loss from PD</td><td>Nearly half of people who start PD are no longer on it at two years, most often because of transfer to hemodialysis, death or transplantation.[[pd_quinn2026]]</td><td>Position statement summarizing registry data</td><td>2, 10, 12</td></tr>
<tr><td>Double-bag and Y-set systems</td><td>Reduced the proportion of patients with peritonitis compared with older spike systems (odds ratio 0.33; 12 trials, 991 patients).[[pd_daly2001]]</td><td>Randomized trials (systematic review)</td><td>4</td></tr>
<tr><td>More small-solute clearance</td><td>Raising peritoneal clearance did not improve survival (ADEMEX, 965 patients, relative risk 1.00). In a Hong Kong trial of 320 patients, Kt/V targets of 1.5&ndash;1.7, 1.7&ndash;2.0 and above 2.0 gave similar two-year survival, though the lowest group had more clinical problems.[[pd_paniagua2002]][[pd_lo2003]]</td><td>Randomized trials</td><td>6</td></tr>
<tr><td>Peritonitis rates in practice</td><td>Crude rate 0.28 episodes per patient-year across seven countries; 0.26 in the United States to 0.40 in Thailand; one facility in ten above 0.50.[[pd_perl2020]]</td><td>Observational cohort (PDOPPS, 7,051 patients)</td><td>7, 12</td></tr>
<tr><td>Training of 6 days or more</td><td>Associated with lower facility peritonitis risk (rate ratio 0.81). Longer training may mark better-resourced programs rather than cause the difference.[[pd_perl2020]]</td><td>Observational</td><td>9</td></tr>
<tr><td>Antibiotics at catheter insertion</td><td>The only 1A recommendation in the 2022 peritonitis guideline.[[pd_li2022]]</td><td>Strong recommendation, high-quality evidence</td><td>3</td></tr>
<tr><td>Diagnosing peritonitis</td><td>At least two of: compatible symptoms or cloudy effluent; effluent white cells above 100/&micro;L after a dwell of at least 2 hours with more than 50% polymorphonuclear cells; positive culture.[[pd_li2022]]</td><td>Guideline, GRADE 1C</td><td>7</td></tr>
<tr><td>Program infection targets</td><td>Peritonitis no more than 0.40 episodes per year at risk; more than 80% of patients peritonitis-free per year; culture-negative episodes under 15%; exit-site infection no more than 0.40 per year at risk.[[pd_li2022]][[pd_chow2023]]</td><td>Guideline targets</td><td>7, 12</td></tr>
<tr><td>Exit-site infection</td><td>Defined by purulent discharge, with or without redness; tunnel infection by inflammation along the tunnel, with or without fluid on ultrasound.[[pd_chow2023]]</td><td>Guideline definitions</td><td>3</td></tr>
<tr><td>The peritoneal equilibration test</td><td>First test at 6 to 12 weeks (GRADE 1A). Faster solute transfer is associated with lower survival (1A). Low ultrafiltration capacity: 4-hour net ultrafiltration under 400 mL with 3.86% glucose or under 100 mL with 2.27% (1B).[[pd_morelle2021]]</td><td>Guideline grades as published</td><td>6</td></tr>
<tr><td>Acute PD</td><td>A suitable modality for acute kidney injury in all settings (adults 1B; children 1C).[[pd_cullis2021]][[pd_nourse2021]]</td><td>Guideline grades as published</td><td>11</td></tr>
</tbody></table></div>
<p>Goal-directed prescribing, teaching PD, assisted PD and the 2026 nutrition recommendation are written as practice points or consensus statements, and the modules describe them that way rather than as graded evidence.[[pd_brown2020]][[pd_chow2025]][[pd_oliver2024]][[pd_wang2026]]</p>
"""},

    # ── Red flags ──────────────────────────────────────────────────────────
    {"id": "redflags", "nav": "Red flags", "tag": "Quick reference", "before": "modules",
     "h2": "Red flags the whole track comes back to",
     "html": """
<p>Most PD problems are slow and quiet. A few are not. These situations override routine troubleshooting in every module; learn them before anything else. Exact steps follow your unit&rsquo;s protocol and the nephrologist&rsquo;s orders.</p>
<div class="table-wrap"><table>
<thead><tr><th>What the patient or record shows</th><th>What it may mean</th><th>Your first action</th></tr></thead>
<tbody>
<tr><td>Cloudy effluent, with or without pain</td><td>Peritonitis until proven otherwise</td><td>Same-day PD team contact; screen for instability; keep and label the bag; sample before antibiotics when feasible, without delaying care (Module 7)</td></tr>
<tr><td>A sterile part touched, or the system opened</td><td>Contamination, dry or wet</td><td>Stop; clamp; do not fill if fluid may have entered; call (Module 4)</td></tr>
<tr><td>Purulent exit-site discharge, or tenderness along the tunnel</td><td>Exit-site or tunnel infection</td><td>Same-day team review; swab before ordered treatment; check effluent (Module 3)</td></tr>
<tr><td>Breathlessness at rest, chest pain, confusion, fainting</td><td>Fluid overload, pleural leak or another emergency</td><td>Emergency pathway; defer troubleshooting (Modules 1 and 8)</td></tr>
<tr><td>New breathlessness after fills, especially on the right</td><td>Dialysate leaking into the chest</td><td>Stop fills and call urgently (Module 8)</td></tr>
<tr><td>Drain alarm with severe abdominal pain</td><td>A clinical problem, not a machine problem</td><td>Assess the person first; urgent PD pathway (Module 5)</td></tr>
<tr><td>Painful, firm hernia with vomiting</td><td>Possible strangulation</td><td>Emergency evaluation (Module 8)</td></tr>
<tr><td>Normal or high glucose reading in a drowsy patient on icodextrin</td><td>Meter reading maltose as glucose, hiding low sugar</td><td>Check with a compatible method; alert the team (Module 10)</td></tr>
<tr><td>Weight rising, urine falling, while exchange ultrafiltration looks positive</td><td>Loss of residual kidney function</td><td>Report the whole trend the same day (Modules 1 and 6)</td></tr>
</tbody></table></div>
"""},

    # ── Calculators ────────────────────────────────────────────────────────
    {"id": "calculators", "nav": "Calculators", "tag": "Tools", "before": "how",
     "h2": "Calculators used in this track",
     "html": "<p>These site calculators are linked from the modules where they are used. They support learning and review; prescription decisions belong to the nephrologist.</p>\n<div class=\"calc-cards-wrap\">\n"
             + "\n".join(_calc(*c) for c in _CALCS) + "\n</div>"},

    # ── Worksheets ─────────────────────────────────────────────────────────
    {"id": "worksheets", "nav": "Worksheets", "tag": "Printable worksheets", "before": "assessment",
     "h2": "Worksheets for practice and coaching",
     "html": """
<p>Use these with fictional cases during the course. For real patients, use your facility&rsquo;s approved forms and records; never enter patient information on this site.</p>
<h3>1 &middot; Readiness and teaching plan (Modules 2 and 9)</h3>
<div class="table-wrap"><table>
<thead><tr><th>Task or barrier</th><th>Patient or caregiver preference</th><th>Support and owner</th><th>Observable criterion</th><th>Reassessment date</th></tr></thead>
<tbody>
<tr><td>Clean exchange area</td><td></td><td></td><td>Identifies and prepares a safe workspace</td><td></td></tr>
<tr><td>Exchange or cycler technique</td><td></td><td></td><td>Completes the approved checklist independently</td><td></td></tr>
<tr><td>Escalation and contingency</td><td></td><td></td><td>Teach-back gives the contact, the action and the backup</td><td></td></tr>
<tr><td>Storage and supply delivery</td><td></td><td></td><td>Shows the space and the backup arrangement</td><td></td></tr>
</tbody></table></div>
<h3>2 &middot; Exchange and treatment review (Modules 4 and 5)</h3>
<div class="table-wrap"><table>
<thead><tr><th>Date and time</th><th>Modality and order</th><th>Fill (mL)</th><th>Drain (mL)</th><th>Net UF (mL)</th><th>Dwell or cycler summary</th><th>Effluent, symptoms, alarms</th><th>Deviation and action</th></tr></thead>
<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table></div>
<p>Net ultrafiltration (UF) for an exchange is the drained volume minus the instilled volume. Use the same scale and the same convention for bag overfill and flush every time.</p>
<h3>3 &middot; Trend exercise (Module 6)</h3>
<p>Assume consistent measurement. Day 5 includes an omitted dwell. Decide what you can infer, what you must verify, and what you would escalate.</p>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>Morning weight (kg)</th><th>Measured daily net UF (mL)</th><th>Urine (mL)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>1</td><td>65.0</td><td>800</td><td>650</td><td>Baseline</td></tr>
<tr><td>2</td><td>65.2</td><td>740</td><td>600</td><td></td></tr>
<tr><td>3</td><td>65.4</td><td>690</td><td>540</td><td></td></tr>
<tr><td>4</td><td>65.7</td><td>530</td><td>470</td><td>Mild ankle edema</td></tr>
<tr><td>5</td><td>66.0</td><td>370</td><td>450</td><td>Dwell omitted</td></tr>
<tr><td>6</td><td>66.4</td><td>450</td><td>360</td><td>All therapy recorded</td></tr>
<tr><td>7</td><td>67.0</td><td>370</td><td>300</td><td>Breathless on exertion</td></tr>
</tbody></table></div>
<p><strong>Facilitator key.</strong> Weight is up 2.0 kg while measured removal by PD and urine fell from about 1,450 mL to 670 mL a day. The missed dwell explains part of day 5, but the trend continues afterward. Verify delivery and measurement, assess breathing, vital signs and other volume findings, and escalate the whole pattern the same day. Use the emergency pathway if the patient is unstable.</p>
<h3>4 &middot; Triage and handoff (Modules 7, 8 and 10)</h3>
{{flow:SBAR with a closed loop|Situation::Time, caller, where the patient is, the problem, and immediate stability.|Background::Modality, last treatment, recent access events, relevant orders and allergies.|Assessment::Symptoms, timing, effluent, equipment, and what has already been done.|Recommendation::The review you request, urgency, disposition, specimen plan and next contact.|Close the loop::Accepting clinician, read-back, time stamp, expected review, and the action if unreachable.}}
<h3>5 &middot; Quality measures (Module 12)</h3>
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>Case definition</th><th>Numerator</th><th>Denominator</th><th>Frequency</th><th>Data owner</th><th>Improvement action</th></tr></thead>
<tbody>
<tr><td>Peritonitis rate</td><td>ISPD 2022 definition; relapsing episodes counted once</td><td>Episodes</td><td>Patient-years at risk</td><td></td><td></td><td></td></tr>
<tr><td>Culture-negative share</td><td>No growth on effluent culture</td><td>Culture-negative episodes</td><td>All episodes</td><td></td><td></td><td></td></tr>
<tr><td>Timely handoff</td><td>Cloudy-bag call to accepted handoff within the unit&rsquo;s target</td><td>Calls meeting target</td><td>Eligible calls</td><td></td><td></td><td></td></tr>
</tbody></table></div>
"""},

    # ── Philippine program workflow ────────────────────────────────────────
    {"id": "philhealth", "nav": "PhilHealth", "tag": "Philippine practice", "before": "sources",
     "h2": "Where the PD nurse fits in a PhilHealth PD program",
     "html": """
<p>PhilHealth pays for peritoneal dialysis through Z-benefit contracting with accredited PD providers, under PhilHealth Circular 2024-0036 and its current annexes.[[pd_ph_pc2024]] The nurse does not decide eligibility or payment, but the records the nurse keeps are what make a claim possible. Confirm every step below with your benefits lead and the current annexes.</p>
{{flow:A typical documentation path|Eligibility::Check that the patient has chronic kidney disease stage 5 and is registered in the PhilHealth Dialysis Database, as instructed by benefits staff.|Preauthorization::Route the request through the contracting team using the current forms.|Initiation::Record training dates, readiness sign-off and the first home treatment.|Follow-up::Keep treatment records, visits, laboratory results and supply deliveries current.|Infection episodes::Record each peritonitis and exit-site infection with dates, organism and outcome.|Exit or transfer::Record the date and cause using standardized definitions of loss from PD.}}
<p>The pediatric automated PD pilot was extended through July 31, 2026; its status after that date had not been confirmed when this track was written.[[pd_ph_pa2026]] Benefit amounts and inclusions change, so confirm them with the PhilHealth Regional Office before you counsel a patient.</p>
"""},

    # ── FAQ ────────────────────────────────────────────────────────────────
    {"id": "faq", "nav": "FAQ", "tag": "Questions", "before": "trainers",
     "h2": "Frequently asked questions",
     "html": """
<h3>Do I need hemodialysis experience first?</h3>
<p>No, but you need the foundations: kidney assessment, chronic kidney disease, infection prevention, medication safety, and Nephrology Nursing Module 10 or its equivalent. Many employers prefer a year of PD experience for independent roles; this track does not replace that.</p>
<h3>Does completing the track make me a recognized PD nurse for PhilHealth?</h3>
<p>No. PhilHealth lists specific training pathways and unit-head validation.[[pd_ph_sat]] The Academy records your learning; recognized training, privileges and credentialing are separate.</p>
<h3>How long does it take?</h3>
<p>The suggested pilot is six weeks and 60 planned hours: 24 of self-study and cases, 12 of simulation or coached review, and 24 of supervised practice. Extend supervised practice until you have the required opportunities.</p>
<h3>Can I study only the modules I need?</h3>
<p>Yes, for review. For sign-off, work through all twelve in order, because later modules assume the physiology and triage habits of earlier ones.</p>
<h3>Does the track cover pediatric and acute PD?</h3>
<p>At orientation level only, in Module 11. Children&rsquo;s prescriptions and acute PD in unstable patients belong to specialized teams, and independent practice needs further training.</p>
<h3>Is any patient information stored?</h3>
<p>No. Quiz answers are scored in your browser, and the optional saved result stays on your device. Keep patient records and staff credentials in your facility&rsquo;s approved systems.</p>
"""},
]
