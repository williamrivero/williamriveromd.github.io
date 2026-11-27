# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 12: Philippine practice, records and quality improvement.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient, nurse and unit is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Distinguish the roles of the Professional Regulation Commission (PRC) and Board of Nursing, the Department of Health (DOH) and its Health Facilities and Services Regulatory Bureau (HFSRB), PhilHealth, and professional societies in a Philippine peritoneal dialysis (PD) program.",
        "Support PhilHealth PD Z-benefit documentation within your scope, routing eligibility and payment decisions to authorized staff.",
        "Calculate peritonitis and exit-site infection rates, months between episodes, percentage of patients peritonitis-free and culture-negative percentage, and compare them with International Society for Peritoneal Dialysis (ISPD) targets.",
        "Apply the 2026 ISPD framework for tracking loss from PD therapy.",
        "Design a small, measurable improvement with a run chart and a balancing measure.",
    ],
    "big": """
<p>A PD program is more than a group of patients doing exchanges. It is licensed, contracted, staffed, audited and, ideally, improving. Your daily documentation is what lets the program prove eligibility, receive payment, meet standards and see its own performance.</p>
<p>Your work in this module is to keep records that are complete and honest, to know which authority governs which question, and to turn the numbers into one improvement at a time. Most programs do not need a grand quality plan. They need one nurse who counts carefully, looks behind each number and changes one thing.</p>
{{plain:Think of the program as a jeepney route with a franchise, a vehicle inspection and a fare matrix. The driver, the nurse, does the daily work, but the route survives only if the paperwork, the vehicle and the service all pass.}}
<p>The picture has a limit. Patients are not passengers who can switch routes easily, and quality numbers are not just compliance. A peritonitis rate is a count of people who suffered. Treat it with that weight.</p>
{{cards:Key terms for this module|Patient-years at risk::The total time all patients spent on PD in the period, in years.|Rate::Episodes divided by patient-years at risk.|Run chart::Monthly values plotted over time with a median line.|Balancing measure::A measure that checks a change has not caused harm elsewhere.|Z-benefit::PhilHealth&rsquo;s benefit package for selected catastrophic conditions, including PD.}}
""",
    "case": {"title": "A year of numbers", "html": """
<p>The PD unit at a provincial hospital in Nueva Ecija has 32 patients. Nurse coordinator <strong>Mylene</strong> reviews last year&rsquo;s records before the annual program meeting.</p>
<p>She counts 9 peritonitis episodes over 28.5 patient-years. Three were culture-negative. Twenty-four of the 32 patients had no peritonitis during the year. Exits from PD: 2 transplants, 4 transfers to hemodialysis and 3 deaths. The hospital director has asked for &ldquo;one slide that says how we are doing.&rdquo;</p>
""", "questions": ["Is the unit within the ISPD targets?",
                  "Which indicator needs work first?",
                  "What would you change, and how would you know it did not cause harm?"]},
    "sections": [
        ("who-governs-what", "Who governs what", "Who governs what (verify current issuances)", """
<p>Use the dated requirements reference on the course home page with your unit&rsquo;s credentialing and benefits leads. Issuances change; the summary below is a map, not the final word.</p>
{{fig:pd12_gov}}
<div class="table-wrap"><table>
<thead><tr><th>Authority</th><th>Question it answers</th><th>Your evidence</th></tr></thead>
<tbody>
<tr><td>PRC and Board of Nursing (Republic Act 9173)</td><td>Are you lawfully authorized to practice nursing?</td><td>Current PRC license and facility privilege record[[pd_ra9173]]</td></tr>
<tr><td>DOH and HFSRB</td><td>Is the facility licensed for the service it provides?</td><td>Facility license to operate or written applicability determination; PD-specific licensing route confirmed with HFSRB or the regional Center for Health Development</td></tr>
<tr><td>PhilHealth PD Z-benefit contracting (Circular 2024-0036 and current annexes)</td><td>Is the facility contracted, the patient eligible, the episode documented?</td><td>Contract, self-assessment tool, rosters, training certificates, patient records per current annexes[[pd_ph_pc2024]]</td></tr>
<tr><td>PhilHealth PD First self-assessment tool</td><td>Staffing and training standard</td><td>At least one full-time PD nurse; nurse-to-patient ratio stated as 1:20; PRC licensure; recognized PD training per listed pathways; head validation[[pd_ph_sat]]</td></tr>
<tr><td>Philippine Society of Nephrology; National Kidney and Transplant Institute (NKTI)</td><td>Recognized training pathways</td><td>Course title, dates, duration, continuing professional development listing, acceptance for the specific setting</td></tr>
</tbody></table></div>
<h3>Benefit amounts and coverage change</h3>
<p>Press reports in 2024 described a PD First Z-benefit package of &#8369;270,000 per year covering solutions, accessories and 90 to 120 exchanges a month depending on the prescription. These are press reports, not the circular. Confirm the current amount, inclusions and annexes with the PhilHealth Regional Office before counseling a patient.</p>
<h3>Scope</h3>
<p>You help patients and the team assemble documentation, check chronic kidney disease (CKD) stage 5 and PhilHealth Dialysis Database status as instructed, and record initiation, follow-up, infection episodes, and exit or transfer. Eligibility decisions and payment decisions remain with authorized personnel.</p>
<h3>Example: the question at the counter</h3>
<p>A patient&rsquo;s daughter asks Nurse Mylene whether PhilHealth will &ldquo;cover everything&rdquo; for her father&rsquo;s PD. Mylene does not quote a figure she read online. She explains, plainly, that the program is contracted for the PD benefit, that the benefits officer checks each patient&rsquo;s eligibility and what is included, and that she will help assemble the documents. She walks the daughter to the benefits officer and records the referral. The daughter leaves with an appointment, not a guess.</p>
<h3>Example: the hemodialysis ratio that does not apply</h3>
<p>During an internal audit, a new administrator asks why the PD unit has one nurse for 18 patients when hemodialysis units staff far more tightly. The coordinator shows the self-assessment tool&rsquo;s stated ratio for PD and explains that PD nursing is training, follow-up and triage, not chairside care. Importing a hemodialysis ratio into PD, in either direction, misreads the work.</p>
{{key:Know which authority answers which question. Route eligibility and payment to the people authorized to decide.}}
"""),
        ("measuring-infection", "Measuring infection", "Measuring infection", """
<p><strong>Peritonitis rate (episodes per year at risk)</strong> = number of episodes &divide; total patient-years at risk.</p>
<p><strong>Patient-years at risk</strong> = the sum of each patient&rsquo;s days on PD in the period &divide; 365.25. Count time from the start of PD training or treatment. Report pre-PD peritonitis (after insertion but before PD starts) separately, per the 2022 definitions. Count relapsing peritonitis as one episode, per ISPD counting conventions.[[pd_li2022]]</p>
<p><strong>Months between episodes</strong> = 12 &divide; rate.</p>
<p><strong>Percentage of patients peritonitis-free</strong> = patients with no episode in the period &divide; patients at risk in the period &times; 100.</p>
<p><strong>Culture-negative percentage</strong> = culture-negative episodes &divide; all episodes &times; 100.</p>
<p><strong>Exit-site infection rate</strong> = episodes &divide; patient-years at risk.</p>
<div class="table-wrap"><table>
<thead><tr><th>Indicator</th><th>ISPD target</th></tr></thead>
<tbody>
<tr><td>Peritonitis rate</td><td>&le; 0.40 episodes per year at risk (2022)</td></tr>
<tr><td>Patients peritonitis-free per year</td><td>&gt; 80% (2022)</td></tr>
<tr><td>Culture-negative peritonitis</td><td>&lt; 15% of episodes (2022, GRADE 1C)</td></tr>
<tr><td>Exit-site infection rate</td><td>&le; 0.40 episodes per year at risk (2023)</td></tr>
</tbody></table></div>
<h3>Worked example: patient-years when patients come and go</h3>
<div class="table-wrap"><table>
<thead><tr><th>Patient</th><th>Days on PD this year</th></tr></thead>
<tbody>
<tr><td>A, whole year</td><td>365</td></tr>
<tr><td>B, started July 1</td><td>184</td></tr>
<tr><td>C, transplanted March 31</td><td>90</td></tr>
<tr><td>D, whole year</td><td>365</td></tr>
<tr><td><strong>Total</strong></td><td><strong>1,004 days</strong></td></tr>
</tbody></table></div>
<p>1,004 &divide; 365.25 = about 2.75 patient-years at risk. Four patients, but not four years. Counting heads instead of time is the most common error in small units, and it makes the rate look better than it is.</p>
<h3>Worked calculations</h3>
<ul>
<li>6 episodes over 20 patient-years: 6 &divide; 20 = <strong>0.30 episodes per patient-year</strong>; 12 &divide; 0.30 = <strong>40 months between episodes</strong>. Below the 0.40 target.</li>
<li>4 episodes over 8 patient-years: 4 &divide; 8 = <strong>0.50 per patient-year</strong>; 12 &divide; 0.50 = <strong>24 months between episodes</strong>. Above target.</li>
<li>3 of 14 episodes culture-negative: 3 &divide; 14 &times; 100 = <strong>21%</strong>. Above the 15% target; review sampling and laboratory methods.</li>
</ul>
<h3>Small numbers mislead</h3>
<p>A unit with 25 patients may see its rate jump from 0.20 to 0.60 because of two extra episodes. Report confidence intervals where possible, look at trends over 12 months, and read each episode&rsquo;s root cause. Do not change a whole program because of one bad quarter, and do not celebrate one good one.</p>
<h3>International comparison</h3>
<p>In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS), crude peritonitis rates were 0.28 episodes per patient-year overall, ranging from 0.26 in the United States to 0.40 in Thailand, and 10% of facilities exceeded 0.50. These are observational data from seven countries, not including the Philippines.[[pd_perl2020]]</p>
{{key:Count time, not heads. Then read the episodes behind the rate.}}
{{fig:pd12_fig_12_patient_years_at_risk_rates}}
"""),
        ("tracking-loss-from", "Tracking loss from PD", "Tracking loss from PD", """
<p>The 2026 ISPD position statement notes that nearly half of people who start PD are no longer on it at two years. The most common causes are transfer to hemodialysis, death and kidney transplantation. Others include recovery of kidney function, transfer to another dialysis program and loss to follow-up. The statement replaces the inconsistently defined term &ldquo;technique failure&rdquo; with standardized definitions of causes of loss, recommendations on measurement, analysis and reporting, and key performance indicators for benchmarking and improvement.[[pd_quinn2026]]</p>
<p>For your program: record the date and cause of every exit using the agreed definitions. Distinguish clinically different outcomes; transplant is a success, while death and hemodialysis transfer need review. Review hemodialysis transfers for preventable causes such as peritonitis, catheter dysfunction, inadequate fluid removal, burnout or caregiver loss.</p>
<h3>Example: one word hid four stories</h3>
<p>A unit&rsquo;s registry listed every hemodialysis transfer last year as &ldquo;technique failure.&rdquo; When the coordinator reopened the four charts, she found four different causes: refractory peritonitis after a wet contamination that was not reported; catheter migration that was never repositioned; fluid overload in a patient whose urine had stopped; and a patient whose only caregiver went abroad. Each points to a different fix: reporting culture, access support, earlier membrane review, and assisted PD planning. None was visible under the old label.</p>
<div class="table-wrap"><table>
<thead><tr><th>Exit</th><th>Review question</th></tr></thead>
<tbody>
<tr><td>Transplant</td><td>Celebrate; was the catheter plan smooth?</td></tr>
<tr><td>Transfer to hemodialysis</td><td>Which cause? Was it predictable and planned?</td></tr>
<tr><td>Death</td><td>Expected or unexpected? Any PD-related contribution?</td></tr>
<tr><td>Transfer to another program</td><td>Was the handover complete?</td></tr>
<tr><td>Loss to follow-up</td><td>What failed: contact, cost, transport?</td></tr>
</tbody></table></div>
{{key:Record the specific cause of every exit. A vague label hides the fix.}}
"""),
        ("improving-one-thing", "Improving one thing", "Improving one thing at a time", """
{{fig:pd12_run}}
<ol>
<li><strong>Pick a problem with data.</strong> For example, a culture-negative rate of 21%, or a median time from cloudy-fluid call to first antibiotic dose of 9 hours.</li>
<li><strong>Write an aim.</strong> &ldquo;Reduce median call-to-antibiotic time from 9 hours to under 4 hours within 6 months.&rdquo;</li>
<li><strong>Choose measures.</strong> Outcome (peritonitis cure without catheter loss), process (time stamps from call to sample to dose), balancing (after-hours staff workload, unnecessary emergency visits).</li>
<li><strong>Test a change.</strong> A one-page cloudy-bag pathway, a pre-labeled sample kit at home, an after-hours phone tree.</li>
<li><strong>Plot a run chart.</strong> Monthly values, a median line, and the date of each change.</li>
<li><strong>Review and adapt.</strong></li>
</ol>
<h3>Example: a run chart in six months</h3>
<div class="table-wrap"><table>
<thead><tr><th>Month</th><th>Cloudy-bag calls</th><th>Median hours, call to first dose</th><th>Note</th></tr></thead>
<tbody>
<tr><td>January</td><td>2</td><td>9.5</td><td>Baseline</td></tr>
<tr><td>February</td><td>1</td><td>8.0</td><td>Baseline</td></tr>
<tr><td>March</td><td>2</td><td>8.5</td><td>One-page pathway introduced March 15</td></tr>
<tr><td>April</td><td>1</td><td>5.0</td><td></td></tr>
<tr><td>May</td><td>2</td><td>4.5</td><td>Home sample kits issued</td></tr>
<tr><td>June</td><td>1</td><td>3.5</td><td></td></tr>
</tbody></table></div>
<p>The direction is encouraging, but the numbers are small: nine calls in six months. The team keeps plotting for another six months before declaring success, and checks the balancing measure: after-hours calls to the on-call nurse rose slightly, and no unnecessary emergency visits were recorded. A single month at 3.5 hours is a hope, not a result.</p>
{{key:Change one thing, measure it monthly, and watch a balancing measure so the fix does not create a new problem.}}
"""),
    ],
    "debrief": ["""
<p><strong>Mylene&rsquo;s calculations.</strong> Peritonitis rate: 9 &divide; 28.5 = 0.32 episodes per patient-year, about 38 months between episodes, under the 0.40 target. Peritonitis-free: 24 &divide; 32 = 75%, under the &gt;80% target. Culture-negative: 3 &divide; 9 = 33%, well above the 15% target.</p>
<p><strong>Which indicator first.</strong> The culture-negative rate. It is furthest from target, and it is the indicator nurses control most directly.</p>
<p><strong>Mylene&rsquo;s plan.</strong> She reviews the three culture-negative episodes: two had antibiotics before sampling after emergency department visits, and one sample sat for 14 hours before reaching the laboratory. Her aim: culture-negative below 15% within 12 months. The change: an emergency-department alert card carried by every patient (&ldquo;Send PD effluent for cell count, Gram stain and culture before antibiotics when feasible; call the PD unit&rdquo;) and a courier arrangement with the laboratory.</p>
<p><strong>How she will know it did no harm.</strong> Her balancing measure is time to first antibiotic dose, so that sampling never delays treatment. She plots both monthly.</p>
<p><strong>The exits.</strong> She also reviews the four hemodialysis transfers using the 2026 definitions: two after refractory peritonitis, one for inadequate fluid removal, one after caregiver loss. Her slide for the director shows the three infection indicators against target, the exits by specific cause, and the one change she is testing.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete both tasks with the data set your preceptor supplies.",
               "items": [("Build a mock contracted-provider document packet (facility record, nurse qualifications, eligibility workflow per current annexes).", False),
                         ("Calculate peritonitis rate, months between episodes, percentage peritonitis-free and culture-negative percentage for a supplied data set, and propose one improvement aim with a numerator, denominator, reporting interval, owner and balancing measure.", False)]},
    "quiz": [
        ("What is the peritonitis rate for 4 episodes over 8 patient-years?",
         ["0.50 episodes per patient-year", "0.25", "2.0", "32"], 0,
         "4 divided by 8 is 0.50, above the 0.40 target."),
        ("At a rate of 0.50 episodes per patient-year, how many months between episodes?",
         ["6", "12", "24", "50"], 2,
         "12 divided by 0.50 is 24 months."),
        ("6 episodes over 20 patient-years gives:",
         ["3.3", "0.12", "1.2", "0.30 episodes per patient-year"], 3,
         "6 divided by 20 is 0.30, below the target."),
        ("3 of 14 episodes are culture-negative. Is the unit within the ISPD 2022 target?",
         ["Yes, 21% is below 30%", "No, 21% exceeds the &lt;15% target", "Yes, any value is acceptable", "Cannot be determined"], 1,
         "21% is above target. Review sampling, transport and laboratory methods."),
        ("What evidence should the head verify when hiring under a PD Z contract?",
         ["Only a r&eacute;sum&eacute;", "Current PRC authority, training evidence accepted for that facility, validation, staffing and contract evidence under current requirements", "A recommendation letter", "A social media profile"], 1,
         "The contract and self-assessment tool define the evidence; check the current versions."),
        ("Who decides PhilHealth eligibility and payment?",
         ["The PD nurse alone", "The patient", "The supplier", "Authorized benefits personnel under the contract and current annexes"], 3,
         "You help assemble documents; you do not decide eligibility or payment."),
        ("Which body licenses health facilities?",
         ["DOH through HFSRB", "PRC", "PhilHealth", "A professional society"], 0,
         "PRC licenses people; DOH through HFSRB licenses facilities; PhilHealth contracts and pays."),
        ("What nurse-to-patient ratio does the PhilHealth PD First self-assessment tool state?",
         ["1:4", "1:100", "1:20", "None"], 2,
         "Do not import the hemodialysis ratio into PD."),
        ("How should relapsing peritonitis be counted in the rate?",
         ["As two episodes", "Not at all", "As one episode, per ISPD counting conventions", "As three episodes"], 2,
         "Counting a relapse twice would inflate the rate."),
        ("What does the 2026 ISPD position statement recommend instead of &ldquo;technique failure&rdquo;?",
         ["Standardized definitions for each cause of loss from PD, with key performance indicators", "Counting only deaths", "No tracking", "Using &ldquo;dropout&rdquo;"], 0,
         "Specific causes reveal specific fixes."),
        ("Why can a small unit&rsquo;s peritonitis rate swing widely from year to year?",
         ["The formula changes", "Small numbers; one or two episodes change the rate greatly", "ISPD targets change yearly", "It cannot"], 1,
         "Look at 12-month trends and each episode&rsquo;s cause."),
        ("Which is a balancing measure for an initiative to sample before antibiotics?",
         ["Number of patients", "Solution brand", "Clinic paint color", "Time to first antibiotic dose"], 3,
         "It checks that better sampling does not delay treatment."),
        ("24 of 32 patients were peritonitis-free last year. Against the ISPD 2022 target:",
         ["75%, above target", "92%", "No target exists", "75%, below the &gt;80% target"], 3,
         "24 divided by 32 is 75%."),
        ("Four patients were on PD for 365, 184, 90 and 365 days this year. About how many patient-years at risk is that?",
         ["4.0", "About 2.75", "1,004", "About 1.5"], 1,
         "1,004 days divided by 365.25 is about 2.75. Counting heads instead of time overstates the denominator."),
        ("Before counseling a patient on the PD Z-benefit amount, you should:",
         ["Quote a press report", "Guess", "Confirm the current amount and inclusions with the PhilHealth Regional Office", "Avoid the topic entirely"], 2,
         "Amounts and inclusions change. Refer to the benefits officer and the current issuance."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CKD", "Chronic kidney disease."),
              ("Exit-site infection", "Purulent discharge at the exit site, with or without redness (ISPD 2023)."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Culture-negative peritonitis", "Peritonitis in which no organism grows from the effluent culture."),
              ("Relapsing peritonitis", "A new episode within 4 weeks of finishing therapy, same organism or one sterile episode."),
              ("Patient-years at risk", "The total time all patients spent on PD in the period, in years."),
              ("Run chart", "A graph of a measure over time with a median line, used to see whether a change made a difference."),
              ("Balancing measure", "A measure that checks whether a change has caused harm elsewhere.")],
    "readings": [("adding-peritoneal-dialysis-program.html", "Starting and running a PD program."),
                 ("dialysis-qapi-vs-cqi.html", "Quality assessment and improvement in dialysis.")],
    "calcs": ["calc-qapi-run-chart-spc.html", "calc-qapi-cqi-toolkit.html", "calc-dialysis-qapi-scorecard.html"],
}
