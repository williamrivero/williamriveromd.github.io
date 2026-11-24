# -*- coding: utf-8 -*-
"""Physician on Duty, Module 31: Rules, Records, and Quality.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at the nurses&rsquo; station at the end of a shift, reading a form carefully before signing it, with a nurse beside her and a quiet treatment floor behind them.",
    "objectives": [
        "Outline who regulates a Philippine hemodialysis facility and state what the Department of Health licensing order expects of a physician on duty.",
        "Obtain, witness, and document consent and informed refusal, using the four elements the Supreme Court set out for informed consent.",
        "Protect patient data under the Data Privacy Act and the unit&rsquo;s privacy procedures.",
        "Write session notes, event notes, certificates, and abstracts that state facts, times, actions, and calls, and sign only what you have verified.",
        "Name the main quality indicators of a dialysis unit, read a run chart, and explain what a rate per 100 patient-months means.",
        "Report an incident or near miss, take part in a root cause review, and describe one Plan-Do-Study-Act cycle with a dialysis example.",
    ],
    "big": """
{{plain:Think of a jeepney route. One agency grants the franchise for the route. Another licenses the driver and registers the vehicle. The barangay decides where the stops are. Each body checks a different thing, and the driver answers to all of them at once. A dialysis unit works the same way: several bodies each check one part of what happens on your shift.}}
<p>The picture has a limit. In health care the bodies overlap, their rules leave gaps, and your professional duty to the patient applies even where no rule is written. The rules set the floor.</p>
<p>Every session ends with signatures: on the treatment sheet, the progress note, and sometimes a certificate, an abstract, or a refusal form. Each is read later by someone who was not there: an insurer, a court, a receiving hospital, or a quality review. Errors and adverse events in dialysis units are common enough to count. One report from four units found 88 of them in 64,541 treatments, about one every 733 treatments.[[holley2006]]</p>
{{cards:Key terms for this module|Licensing order::The Department of Health (DOH) administrative order that sets the minimum standards a dialysis facility must meet to operate.|Informed refusal::A patient&rsquo;s decision to decline or stop a treatment after the risks of declining have been explained in words the patient understands.|Sensitive personal information::Under the Data Privacy Act, a class of personal data that includes health information. It carries stricter rules on sharing.|Event note::A timed entry in the chart that records what happened, what was done, the response, and who was called.|Quality indicator::A measure tracked over time to show how well a unit cares for its patients, such as the infection rate.|Run chart::A graph of a measure in time order with its median drawn as a line, used to tell a real change from noise.|Near miss::An error or hazard that was caught before it reached the patient.|Plan-Do-Study-Act (PDSA) cycle::A small, planned test of one change, measured and then kept, adapted, or abandoned.}}
<p>Most of what you sign is routine and true. A few signatures certify things you did not see, and a few events never reach the logbook. Your work is to sign only what you verified, to record events so a stranger can follow them, and to bring what you see to the unit&rsquo;s quality review.</p>
""",
    "case": {"title": "&ldquo;Please sign the form, Doc&rdquo;", "html": """
<p>It is Friday, 6:40 p.m., at the end of the second shift in a 15-station unit in Angeles City. Mr. Danilo Mendoza, 49, asked to come off at hour two of his four-hour session because his ride home was leaving. His pre-dialysis potassium this week was 6.1 mmol/L, and he arrived today 3.2 kilograms above his dry weight. These values are illustrative.</p>
<p>The nurse, Ms. Arlene Pangilinan, hands you three papers. The first is a &ldquo;Refusal of Treatment&rdquo; form, already filled in with &ldquo;patient refused&rdquo; and a blank line for your signature. The second is a medical certificate his employer requested, stating that he &ldquo;completed dialysis today.&rdquo; The third is the incident log, where she has written that his venous needle infiltrated at hour one and was replaced. The attending nephrologist has not been called. Mr. Mendoza is already standing.</p>
""", "questions": ["What must you do and document before you sign the refusal, and who should witness it?",
                  "Can you sign the certificate as written, and what would you write instead?",
                  "What goes into the incident log about the infiltration, and is this also a near miss worth reviewing?"]},
    "sections": [
        ("rules", "Who regulates what", "Who regulates what", """
<p>Module 1 set out your role. This section names the rules behind it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Body</th><th>What it governs</th><th>What it checks in your unit</th></tr></thead>
<tbody>
<tr><td>Department of Health (DOH)</td><td>Licensing of the facility. Administrative Order (AO) 2012-0001 for dialysis facilities[[doh2012]] and AO 2013-0003 for dialysis water[[doh_ao2013_0003]]</td><td>Staff, equipment, water, records, and quality systems</td></tr>
<tr><td>Philippine Health Insurance Corporation (PhilHealth)</td><td>The hemodialysis benefit, accreditation, and claims, set by circular[[philhealth_pc2024_0023]]</td><td>Whether the sessions claimed match the records</td></tr>
<tr><td>National Privacy Commission (NPC)</td><td>Personal data under the Data Privacy Act[[ra10173]] and breach management[[npc_circular16_03]]</td><td>How patient information is handled</td></tr>
<tr><td>Professional Regulation Commission (PRC)</td><td>Your license to practice</td><td>That you are licensed</td></tr>
<tr><td>Philippine Society of Nephrology (PSN)</td><td>A public professional standard for hemodialysis clinics, 3rd edition, 2024[[psn2024]]</td><td>Good practice. A standard, not a law</td></tr>
</tbody></table></div>
<h3>What the licensing order expects of you</h3>
<p>AO 2012-0001 is the licensing order for dialysis facilities.[[doh2012]] It lists what the physician on duty must be. You attend to patients under the supervision of the Medical Director. You are licensed by the PRC and hold one of the qualifying credentials the order lists. You have experience in the care of patients with end-stage kidney disease. You have updated training in advanced cardiovascular life support (ACLS). You are present during the unit&rsquo;s hours of operation.[[doh2012]] The order states that the ratio of physician on duty to hemodialysis stations &ldquo;shall not be more than 1:15.&rdquo;[[doh2012]] The order also limits a Medical Director to three facilities and requires an adverse events logbook and a continuous quality improvement (CQI) system.[[doh2012]]</p>
<p>The PSN standard states that the ratio of physician on duty to stations is ideally 1:15, and that where physicians on duty are few in the area, a maximum of 1:20 is allowed &ldquo;as long as he/she is able to adequately attend to the needs of the patients.&rdquo;[[psn2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Requirement</th><th>DOH licensing order (the legal floor)</th><th>PSN standard (good practice)</th></tr></thead>
<tbody>
<tr><td>Presence</td><td>Present during hours of operation</td><td>Able to attend adequately to the patients&rsquo; needs</td></tr>
<tr><td>Resuscitation</td><td>Updated ACLS training</td><td>Updated ACLS certificate from a DOH-accredited provider</td></tr>
<tr><td>Stations per physician on duty</td><td>Not more than 1:15</td><td>Ideally 1:15. Up to 1:20 where physicians on duty are few, if the patients&rsquo; needs are met</td></tr>
</tbody></table></div>
<p>Where the two differ, the DOH order is the law and the PSN standard is advice. On staffing, the PSN allowance of up to 1:20 does not lift the order&rsquo;s limit of 1:15. Your Medical Director sets the unit&rsquo;s rule within the order and can show you the current licensing documents.</p>
<p>PhilHealth sets its hemodialysis benefit by circular. Circular 2024-0023 adjusted the package for members and their qualified dependents with chronic kidney disease stage 5, effective October 9, 2024.[[philhealth_pc2024_0023]] Benefit rules change often, so this module does not quote them. Your unit&rsquo;s claims officer is the source for the rules in force.</p>
{{key:The DOH order is the floor, not the goal. Know what it requires of you by name: present, licensed, experienced, ACLS current, and supervised by the Medical Director.}}
"""),
        ("signatures", "What you sign", "What you sign, and what each signature certifies", """
<p>A signature is a promise in ink. It says &ldquo;I saw this,&rdquo; &ldquo;I did this,&rdquo; or &ldquo;I checked this.&rdquo; A later reader takes it as a statement of fact.</p>
<div class="table-wrap"><table>
<thead><tr><th>Document</th><th>What your signature certifies</th><th>Who usually signs</th></tr></thead>
<tbody>
<tr><td>Session record or progress note</td><td>You assessed the patient at the time written</td><td>The physician on duty</td></tr>
<tr><td>An order during the session</td><td>You take responsibility for the instruction, within the attending nephrologist&rsquo;s prescription</td><td>The physician on duty, often after a call</td></tr>
<tr><td>Medical certificate</td><td>You examined the patient and every statement on it is true</td><td>The physician who examined the patient</td></tr>
<tr><td>Clinical abstract</td><td>It summarizes the chart accurately</td><td>Usually the attending nephrologist</td></tr>
<tr><td>Transfer or referral letter</td><td>The receiving physician can act on what it says</td><td>The physician on duty, with the attending nephrologist&rsquo;s plan</td></tr>
<tr><td>Refusal or against-advice form</td><td>The risks were explained and the patient declined</td><td>The patient, the physician who explained, and witnesses</td></tr>
</tbody></table></div>
<h3>How a documentation error becomes a false statement</h3>
<p>A form arrives pre-filled, the shift is ending, and the family is waiting. You sign without reading, sign for a session you did not witness, or back-date an entry. A missing entry is a gap in the record. A signed entry that is untrue is a false statement, and it carries your license number.</p>
<p>Read every document before you sign it. Sign only what you personally verified. When you summarize another clinician&rsquo;s findings, write &ldquo;per chart&rdquo; or name the source. Refer requests outside your role, such as a disability certification, to the attending nephrologist.</p>
{{call:Stop and call the attending nephrologist or the Medical Director when you are asked to sign a document about care you did not provide or a finding you did not verify, or when the document&rsquo;s purpose is a claim, a legal matter, or a death. Follow your unit&rsquo;s protocol on who signs what.}}
"""),
        ("consent", "Consent and refusal", "Consent and refusal", """
<p>Consent is like a map handed over before a trip. The patient sees where each road leads, including the road of doing nothing, and then chooses. The map is yours to draw. The choice is the patient&rsquo;s.</p>
<h3>What the law asks</h3>
<p>In <em>Li v. Spouses Soliman</em> (G.R. No. 165279, en banc, June 7, 2011), the Supreme Court set out four elements of a malpractice claim based on informed consent: the physician had a duty to disclose material risks; the physician failed to disclose them or disclosed them inadequately; as a direct result, the patient consented to treatment he or she would otherwise have refused; and the patient was injured by it.[[li_soliman2011]]</p>
<p>The ruling turns on disclosure of material risks. For dialysis, these include the risks of declining treatment. The PSN standard asks that dialysis consent be updated at least annually and as needed, and that the consent form preferably be witnessed by two people who also sign it.[[psn2024]]</p>
<h3>Who consents, and to what</h3>
<p>A patient with decision-making capacity consents for himself or herself. Capacity means the patient can understand the information, weigh it, and communicate a choice. When a patient lacks capacity, a representative decides, as your unit&rsquo;s policy directs. Blood transfusion and catheter insertion usually need their own consent.</p>
<h3>Refusal is a decision, and it is documented like a procedure</h3>
<p>A competent adult may refuse a session, shorten one, or leave against advice. Your job is to make sure the refusal is informed and that the record shows it. For a patient with a high potassium, plain words mean saying that the heart can stop.</p>
{{flow:Consent and refusal at the chair|Check capacity::Can the patient understand, weigh, and communicate a choice? If not, involve the representative per the unit&rsquo;s policy.|Explain in plain words::The treatment, the main risks, the alternatives, and the risks of declining. Use the patient&rsquo;s language.|Ask the reason::A ride, a cost, a symptom, or a fear can often be solved.|Hear the decision::Let the patient say it in his or her own words.|Witness::Have the form witnessed as your unit&rsquo;s policy requires. The PSN standard prefers two witnesses who also sign.|Call::Tell the attending nephrologist before the patient leaves if you can, and agree on the follow-up plan.|Document::What was explained, the risks named, the patient&rsquo;s words, the witnesses, the call, and the plan.}}
<p>A pre-filled form that says only &ldquo;patient refused&rdquo; documents none of this. Withdrawal from dialysis altogether is a different conversation, covered in Module 26.</p>
{{key:An informed refusal is documented like a procedure: what was explained, what the patient said, who witnessed it, and who was called.}}
"""),
        ("privacy", "Patient data", "Patient data and privacy", """
<p>A patient&rsquo;s chart is like a house key. You give a copy only to people who live in the house. A copy sent to the wrong person cannot be called back.</p>
<p>Republic Act 10173, the Data Privacy Act of 2012, governs personal information. Health information falls in its stricter class of sensitive personal information.[[ra10173]] NPC Circular 16-03 governs personal data breaches. It requires the organization responsible for the data to notify the Commission and the affected patients within 72 hours of knowing of a breach that requires notification, and it gives the response to a breach response team that keeps the data protection officer informed.[[npc_circular16_03]] You do not decide whether a breach meets that test. You report it at once so that the people who do decide have their full 72 hours.</p>
<h3>Where dialysis units leak data</h3>
<p>Patients sit together for hours, for years. Staff coordinate by phone. Serology status decides where a patient sits. Each habit is useful, and each can expose a patient.</p>
{{fig:pod31_privacy_at_the_station}}
<div class="table-wrap"><table>
<thead><tr><th>Risk</th><th>How it exposes a patient</th><th>Safer practice</th></tr></thead>
<tbody>
<tr><td>Patient board on the wall</td><td>Full names, diagnoses, or schedules visible to every visitor</td><td>Initials or station numbers, per the unit&rsquo;s policy</td></tr>
<tr><td>Photos of the treatment sheet</td><td>Images stay on personal phones and in cloud backups</td><td>The unit&rsquo;s approved channel for images and results</td></tr>
<tr><td>Group chats</td><td>Names and laboratory results reach people with no need to know</td><td>Minimum information, the approved channel, no names where a record number will do</td></tr>
<tr><td>Station labels</td><td>Hepatitis B, hepatitis C, or human immunodeficiency virus (HIV) status visible to other patients</td><td>Isolation signs that follow infection control rules without naming the infection, per the unit&rsquo;s policy</td></tr>
<tr><td>Open charts</td><td>A chart left on a chair can be read by the next patient&rsquo;s family</td><td>Charts closed and returned to the station</td></tr>
</tbody></table></div>
<p>When you suspect a breach, such as a lost phone or a message sent to the wrong group, report it to the data protection officer and the Medical Director at once.</p>
{{key:Share the least, with the fewest, through the approved channel. Report a suspected breach the moment you know of it.}}
"""),
        ("notes", "Notes that hold up", "Notes that hold up", """
<p>Write every note for a stranger who will read it at 3 a.m. or in a courtroom two years later. That reader cannot ask you what you meant.</p>
<p>AO 2012-0001 requires confidential records that identify the patient, and an adverse events logbook.[[doh2012]] The PSN standard requires complete records for every patient.[[psn2024]] Neither says how to write a good note. The elements below come from what a later reader needs.</p>
{{fig:pod31_model_event_note}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>What to write</th><th>Why a later reader needs it</th></tr></thead>
<tbody>
<tr><td>Date and clock time</td><td>The time of the event and the time of the entry</td><td>Sets the order of events</td></tr>
<tr><td>Findings</td><td>Vital signs with units, symptoms, the access, the machine readings that matter</td><td>Shows what you knew when you acted</td></tr>
<tr><td>Actions</td><td>What was done, by whom, and when</td><td>Shows the response was timely</td></tr>
<tr><td>Response</td><td>What changed after each action</td><td>Shows whether the plan worked</td></tr>
<tr><td>Call made</td><td>Whom you called and when</td><td>Shows escalation</td></tr>
<tr><td>Advice received</td><td>What the attending nephrologist advised</td><td>Shows who decided what</td></tr>
<tr><td>Plan and owner</td><td>What happens next and who is responsible</td><td>Lets the next shift continue</td></tr>
<tr><td>Signature</td><td>Your name, signature, and license number per the unit&rsquo;s format</td><td>Shows who wrote it</td></tr>
</tbody></table></div>
<p>Label late entries as late, with the time written. Never insert them to look contemporaneous. Correct errors with a single line, dated and initialed.</p>
<h3>What the evidence on structured communication shows</h3>
<p>In a prospective study of a pediatric resident handoff program in nine hospitals, covering 10,740 admissions, medical errors fell from 24.5 to 18.8 per 100 admissions and preventable adverse events from 4.7 to 3.3 per 100 admissions after standardized written and oral handoffs were introduced.[[starmer2014]] The design was before and after, without a control group, and the setting was not dialysis. Module 1 reviews the Situation-Background-Assessment-Recommendation (SBAR) format. A systematic review of eleven studies, eight of them before-and-after designs, found moderate evidence that SBAR improves patient safety, most clearly for telephone calls, and noted a lack of high-quality research.[[muller2018]]</p>
<p>In dialysis, a mailed survey of 422 nurses in outpatient units found that negative ratings of handoff safety were associated with frequent access thrombosis and patient complaints.[[thomashawkins2015]] The survey was cross-sectional and relied on nurses&rsquo; reports, so it shows an association and not that better handoffs prevent clotting.</p>
{{formula:<strong>Illustrative documentation check, not a target.</strong> Score one of your own event notes for eight elements: date, time, findings, actions, response, call made, advice received, and plan with owner.<br>Note with 6 of 8 elements: 6 &divide; 8 = 0.75, or 75%.<br>Five notes scoring 8, 6, 7, 5, and 7: mean = 33 &divide; 5 = 6.6 of 8; 6.6 &divide; 8 = 82.5%.<br>The element most often missing in this example: advice received.<br>This is a teaching checklist; no validated score exists for dialysis notes. The number shows which element you drop, not whether a note would satisfy a court.}}
{{key:A good event note answers six questions for a stranger: when, what you saw, what you did, what changed, whom you called, and what happens next.}}
"""),
        ("quality", "Measuring quality", "How a unit measures itself", """
<p>A pilot reads an instrument panel. No single gauge says the flight is going well; together, watched over time, they do. A unit reads its quality the same way.</p>
{{fig:dashboard}}
<h3>The main indicators, and what each measures</h3>
<p>A surrogate is a laboratory value or process measure expected to track an outcome. An outcome is what patients feel: death, admission, infection. A unit can improve a surrogate without improving the outcome.</p>
<div class="table-wrap"><table>
<thead><tr><th>Indicator</th><th>What it measures</th><th>Surrogate or patient outcome</th></tr></thead>
<tbody>
<tr><td>Delivered dose: single-pool Kt/V or urea reduction ratio (URR)</td><td>How much urea each session removes, as set out in the Kidney Disease Outcomes Quality Initiative (KDOQI) adequacy guideline[[kdoqi_hd2015]]. Module 7 owns the target</td><td>Surrogate</td></tr>
<tr><td>Catheter use</td><td>The share of patients dialyzing through a catheter</td><td>Process measure linked to infection risk</td></tr>
<tr><td>Bloodstream infection rate</td><td>Infections per 100 patient-months</td><td>Patient outcome</td></tr>
<tr><td>Hemoglobin, phosphate, and parathyroid hormone</td><td>Anemia and mineral control</td><td>Surrogates</td></tr>
<tr><td>Hospitalization and mortality</td><td>Admissions and deaths, best read as standardized ratios</td><td>Patient outcomes</td></tr>
<tr><td>Missed and shortened sessions</td><td>Treatment not delivered</td><td>Process measure. Skipping is associated with higher mortality in the Dialysis Outcomes and Practice Patterns Study (DOPPS)[[saran2003]]</td></tr>
<tr><td>Water test results</td><td>Whether the water meets the order&rsquo;s limits</td><td>Process measure</td></tr>
<tr><td>Patient-reported outcomes</td><td>Symptoms and quality of life in the patient&rsquo;s words</td><td>Patient outcome</td></tr>
</tbody></table></div>
<p>In DOPPS, an international prospective cohort, skipping one or more sessions a month was associated with higher mortality (relative risk 1.30).[[saran2003]] Patients who skip differ in many ways from those who do not, so this is an association, not the effect of one skipped session.</p>
<h3>Rates need the right denominator</h3>
<p>A count of infections means little without the time at risk. Patel and colleagues reported bloodstream infections per 100 patient-months.[[patel2013]] One patient dialyzing for a whole month contributes one patient-month.</p>
{{formula:<strong>Rate per 100 patient-months, illustrative.</strong> Formula: events &divide; patient-months &times; 100, the denominator used by Patel and colleagues.<br>One month: 3 bloodstream infections in a unit of 60 patients. 3 &divide; 60 &times; 100 = 5.0 per 100 patient-months.<br>Six months: 4 infections over 360 patient-months. 4 &divide; 360 &times; 100 = 1.1 per 100 patient-months.<br>In a small unit, one infection more or less moves the monthly rate a great deal, so read the longer period and the run chart. Rates per 1,000 catheter-days cannot be compared directly with rates per 100 patient-months.}}
<p>The site&rsquo;s access infection calculator gives a rate per 1,000 catheter-days with an exact confidence interval. Label the denominator whenever you report a rate.</p>
<h3>Reading a run chart</h3>
<p>Perla and colleagues describe four rules that separate a real change from random variation.[[perla2011]] A shift is six or more consecutive points all above or all below the median. A trend is five or more consecutive points all going up or all going down. Too few or too many runs (crossings of the median) and an obviously different astronomical point are the other two. Points on the median are skipped: they neither add to nor break a shift. The shift and run rules need more than ten points before they apply.[[perla2011]]</p>
{{fig:pod31_run_chart_shift}}
{{formula:<strong>Run chart, illustrative data.</strong> Percentage of patients dialyzing through a catheter, months 1 to 12: 30, 28, 31, 29, 30, 27, 24, 23, 22, 22, 21, 20.<br>Sorted: 20, 21, 22, 22, 23, 24, 27, 28, 29, 30, 30, 31. The middle two values are 24 and 27, so the median is (24 + 27) &divide; 2 = 25.5.<br>Months 7 to 12 (24, 23, 22, 22, 21, 20) are six consecutive points below the median. By the shift rule of Perla and colleagues, this is a signal.<br>The run chart tells you that something changed around month 7. It does not tell you what. Ask what the unit did differently that month.}}
<p>The site&rsquo;s run chart calculator draws the median and applies these rules for you.</p>
<h3>Standardized ratios compare like with like</h3>
<p>A unit with older, sicker patients will have more admissions and deaths. A standardized ratio divides the observed number by the number expected for that unit&rsquo;s case mix.</p>
{{formula:<strong>Standardized ratio, illustrative.</strong> Observed admissions in a year: 18. Expected for this case mix: 15.<br>Ratio = observed &divide; expected = 18 &divide; 15 = 1.2.<br>Above 1 means more events than expected. With small numbers the confidence interval, from the site&rsquo;s standardized ratio calculator, decides whether 1.2 is a signal. The ratio is only as good as the model behind the expected number.}}
<h3>Payment programs are not proof of quality</h3>
<p>In the United States, a regression discontinuity study of 5,830 outpatient centers found that 19.0% were penalized under the End-Stage Renal Disease Quality Incentive Program. Penalization was not associated with improvement in total performance scores (0.4 point, 95% confidence interval &minus;2.5 to 3.2).[[sheetz2021]] The study was observational and could not see how centers responded. It suggests that a penalty alone does not make a unit better.</p>
{{key:Read trends, not single months. A run chart tells you whether a change is real; a single red number does not.}}
"""),
        ("incidents", "Incidents", "Incidents, near misses, and root cause review", """
<p>An incident is the crash. A near miss is the swerve that avoided it. Both show the dangerous bend in the road.</p>
<h3>What goes wrong in dialysis units</h3>
<p>Holley reviewed 18 months of quality assurance forms from four hemodialysis units: 88 errors and adverse events in 64,541 treatments. Infiltration of the access (31) and clotting of the circuit (19) were the most common. There were 35 medication errors, and omission of an ordered medicine was the most frequent kind (24 of 35, 69%). No patient was hospitalized as a result.[[holley2006]] The report was descriptive and relied on what staff wrote down. A unit that reports little is not necessarily safe.</p>
{{flow:The incident and near-miss loop|Make the patient safe::Treat the patient first, as your unit&rsquo;s protocol directs.|Report the same shift::Write it in the unit&rsquo;s logbook or reporting system, with times and facts, without blame.|Notify::Tell the attending nephrologist of any event that reached the patient. Tell the charge nurse and the Medical Director per protocol.|Review::The unit looks for causes in the system, not only in the person.|Fix the system::Choose the strongest change the unit can make.|Feed back::Staff hear what was found and what changed.}}
<h3>Root cause review, and why it often disappoints</h3>
<p>A root cause review asks why an event happened, and why again, until it reaches causes the unit can change.</p>
{{fig:fishbone|A fishbone diagram for a cluster of catheter bloodstream infections sorts possible causes into groups, so the team looks beyond the first explanation that comes to mind.}}
<p>Peerally and colleagues argue that root cause analysis in health care often falls short. Investigators settle for weaker administrative fixes, such as reminders, instead of fixing latent causes such as poorly designed technology. They recommend skilled investigators, involving patients and families, and checking whether each fix worked.[[peerally2017]] Their paper is an expert analysis, not a trial.</p>
{{fig:pod31_weak_vs_strong_actions}}
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Weaker fix</th><th>Stronger fix</th></tr></thead>
<tbody>
<tr><td>A patient&rsquo;s ordered medicine was not given during the session</td><td>Remind the nurses to check the orders</td><td>A medication line on the treatment sheet that must be signed before the session can be closed</td></tr>
<tr><td>A dialyzer was set up for the wrong patient</td><td>Retrain on labeling</td><td>Labels printed from the patient list and a two-person check at the chair</td></tr>
</tbody></table></div>
<p>DOH patient safety issuances also shape how a unit reports events. This module does not summarize them. Ask your Medical Director which ones your unit&rsquo;s reporting follows.</p>
<p>Report every incident and near miss the same shift, without blame words. In a review, describe what happened, not who is at fault.</p>
{{call:Stop and call the attending nephrologist and the Medical Director the same day for any event that caused harm, any medication or blood transfusion error that reached the patient, any wrong-patient or wrong-dialyzer event, and any cluster of similar illness among patients (Module 30). Make the patient safe first, as your unit&rsquo;s protocol directs.}}
{{key:Report the near miss as carefully as the incident. It shows the same bend in the road without the injury.}}
"""),
        ("cqi", "One improvement cycle", "One improvement cycle, and what is uncertain", """
<p>Cooking adobo for a new family is a fair picture of improvement. You change one thing at a time, taste, and keep what works.</p>
<p>The picture has a limit. A cook tastes in minutes. A unit &ldquo;tastes&rdquo; through noisy monthly data, so it needs a clear measure and a run chart.</p>
<h3>The method</h3>
<p>In a Plan-Do-Study-Act (PDSA) cycle you plan one change and predict its effect, do it on a small scale, study the data against the prediction, and act: keep, adapt, or abandon it.</p>
{{fig:pdsa|Improvement runs in small cycles. In the catheter care example below, each cycle tests one part of the bundle and the team checks the run chart.}}
<p>PDSA is often done badly. A systematic review of 73 published projects found that fewer than 20% (14 of 73) documented a sequence of iterative cycles. Only 15% of the projects analyzed in detail (7 of 47) used data collected monthly or more often to guide each cycle.[[taylor2014]]</p>
<p>AO 2012-0001 requires every dialysis facility to keep a system for continuous quality improvement.[[doh2012]] The PSN standard expects CQI meetings at least once a month, documented, and led by the unit&rsquo;s clinical head.[[psn2024]]</p>
<h3>A dialysis example with evidence</h3>
<p>A Centers for Disease Control and Prevention (CDC) collaborative of 17 outpatient units used a bundle: chlorhexidine exit-site care, staff training, care audits, and feedback of rates. Pooled bloodstream infection rates went from 1.09 to 0.89 per 100 patient-months, and access-related infection rates from 0.73 to 0.42. Modeled rates fell 32% and 54% at the start of the intervention.[[patel2013]] The project had no control arm.</p>
<p>A cluster-randomized initiative in 211 matched facility pairs was stronger. Units that adopted chlorhexidine-alcohol exit-site care and &ldquo;scrub the hubs&rdquo; had 0.81 bloodstream infections per 1,000 catheter-days during follow-up, against 1.04 in usual-care units. Adjusted analysis confirmed reductions of 21% to 22%.[[rosenblum2014]] The CDC lists its core interventions on one page.[[cdc_dialysis_bsi2024]]</p>
{{cards:A PDSA cycle on catheter care, illustrative|Plan::Predict that a hub-scrub step will lower infections. Measure: infections per 100 patient-months, monthly.|Do::Two nurses on one shift test it for two weeks and record adherence.|Study::Adherence was high. The infection rate needs months of data.|Act::Extend to all shifts and review the run chart at each CQI meeting.}}
<p>Your part is practical. Bring data and observations to the CQI meeting. Carry out the agreed change on your shift. Say so when a change does not fit the floor.</p>
<h3>What is uncertain</h3>
<ul>
<li>Whether AO 2012-0001 is still the operative order. No superseding order was found in public sources on November 25, 2026. Your Medical Director confirms this with the DOH.</li>
<li>The staffing ratio. The DOH order sets a maximum of 1:15. The PSN standard allows up to 1:20 with conditions. The order is the legal limit; your Medical Director confirms how the unit applies it.</li>
<li>Most quality improvement evidence in dialysis comes from before-and-after or observational studies. Only one study cited here is cluster-randomized.[[rosenblum2014]] Penalizing low scores did not improve U.S. center scores.[[sheetz2021]]</li>
<li>No validated score exists for the quality of dialysis notes. The eight-element checklist in this module is a teaching tool.</li>
</ul>
{{key:A good improvement project changes one thing, measures it monthly, and keeps the change only if the run chart moves.}}
"""),
    ],
    "debrief": ["""
<p><strong>What must you do before you sign the refusal?</strong> Do not sign the pre-filled form yet. First go to Mr. Mendoza. Check that he can understand, weigh, and communicate a choice. If he can, the decision is his. His reason is his ride, which the family may be able to solve. Explain the risks in plain words: with a high potassium this week and a large weight gain, a session cut in half leaves him at risk of a dangerous heart rhythm and of fluid in the lungs. Call the attending nephrologist while he is still in the unit, because the nephrologist may want to change the plan or arrange an earlier session. If he still leaves, record what you explained, his reason in his own words, the time, the call and the advice, and the follow-up plan. Have the form witnessed as your unit&rsquo;s policy requires. The PSN standard prefers two witnesses who also sign, such as Ms. Pangilinan and a second staff member.</p>
<p><strong>Can you sign the certificate as written?</strong> No. It says he completed dialysis today, and he did not. Signing it would be a false statement. A true certificate states that he attended the unit today for scheduled hemodialysis, with the actual start and end times. The employer does not need his diagnosis or his potassium. If your unit reserves certificates for the attending nephrologist, refer the request.</p>
<p><strong>What goes into the incident log, and is there a near miss?</strong> The infiltration reached the patient, so it is an incident. The entry states the time, what was seen and done, the patient&rsquo;s condition, and who was told, without blame words. The early end of the session is a refusal, documented in the chart. There is also a near miss worth reviewing: a high-risk patient nearly left with only a pre-filled form and no call to the nephrologist. That points to the system, not to Ms. Pangilinan, and a CQI meeting can fix pre-filled forms.</p>
"""],
    "skills": {"title": "Auditing your own notes and writing an incident report",
               "intro": "Work through these steps with your own recent notes and one real or simulated event, while your preceptor or the Medical Director reviews your work.",
               "items": [
                   ("Selects five of your own event notes from the last month, using the unit&rsquo;s approved system.", False),
                   ("Scores each note for the eight elements and records the element most often missing.", False),
                   ("Identifies any signature on a document that certified something you did not personally verify.", True),
                   ("Writes a refusal note that includes what was explained, the patient&rsquo;s words, the witnesses, and the call to the attending nephrologist.", True),
                   ("Writes an incident report that is factual, timed, and free of blame language.", True),
                   ("Classifies the event as an incident or a near miss, and as reaching or not reaching the patient.", False),
                   ("Names who must be notified for this event and notifies them.", True),
                   ("States one contributing factor in the system, not in a person.", False),
                   ("Computes one unit indicator as a rate with the correct denominator.", False),
                   ("Places one month&rsquo;s value on the unit&rsquo;s run chart and states whether the chart shows a signal.", False),
                   ("Proposes one PDSA test of change with a measure and a review date.", False),
                   ("Handles the audit data without exposing patient identifiers outside the unit&rsquo;s system.", True),
               ],
               "placement": "Over the next month, score five of your event notes each week with the eight-element checklist. Bring your most-missed element and one near miss you saw to the unit&rsquo;s monthly CQI meeting, and agree with the Medical Director on one small change to test."},
    "quiz": [
        ("Which list matches what DOH AO 2012-0001 expects of a physician on duty?",
         ["Board certification in nephrology and presence during the first hour only",
          "Present during hours of operation, PRC-licensed with a listed credential, experienced with end-stage kidney disease, ACLS updated, and supervised by the Medical Director",
          "Presence on call by telephone, with ACLS optional",
          "Authority to change the dialysis prescription when the nephrologist is unavailable"], 1,
         "These are the order&rsquo;s requirements."),
        ("The PSN standard and the DOH order differ on a staffing point. How should the unit handle the difference?",
         ["Follow whichever is less strict",
          "Ignore the PSN standard because it is not law",
          "Treat the DOH order as the legal floor and let the Medical Director set the unit&rsquo;s rule within it",
          "Follow the PSN standard because it is more recent"], 2,
         "The order is law. The standard is good practice. The Medical Director sets the unit&rsquo;s rule, and it cannot fall below the order."),
        ("At 6:30 p.m., a nurse hands you a medical certificate stating that a patient &ldquo;completed dialysis today.&rdquo; The patient left at hour two. What do you do?",
         ["Sign it, because the patient attended",
          "Sign it and add &ldquo;per nurse&rdquo;",
          "Refuse any certificate for this patient",
          "Write a certificate that states the true times of attendance, or refer it per unit policy"], 3,
         "Every statement on a certificate must be true."),
        ("In <em>Li v. Spouses Soliman</em>, which element must a patient prove in an informed-consent claim?",
         ["That the patient would not have consented had the material risks been disclosed",
          "That the physician was not board certified",
          "That the consent form had no witness",
          "That the treatment was experimental"], 0,
         "Duty to disclose, failure to disclose, consent otherwise not given, and injury."),
        ("Mr. Reyes, alert and oriented, wants to stop his session at hour one to attend a wake. His potassium this week was high. What comes first after you explain the risks?",
         ["Have security keep him in the chair",
          "Ask his reason and look for a way to meet it, then call the attending nephrologist",
          "Sign the refusal form and discharge him",
          "Tell him he cannot return if he leaves"], 1,
         "A competent adult may refuse. The reason is often solvable."),
        ("Which refusal note best holds up?",
         ["&ldquo;Patient refused. Discharged.&rdquo;",
          "&ldquo;Patient noncompliant again.&rdquo;",
          "&ldquo;Risks explained. Patient insisted.&rdquo;",
          "&ldquo;5:10 p.m. Explained risk of dangerous heart rhythm from high potassium. Patient: &lsquo;My ride is leaving.&rsquo; Witnessed by two staff. Attending nephrologist called 5:15 p.m.; advised session tomorrow.&rdquo;"], 3,
         "It has the time, explanation, the patient&rsquo;s words, witnesses, call, and plan."),
        ("A nurse posts a photo of a treatment sheet with the patient&rsquo;s name in a staff group chat that includes a supplier. What do you do?",
         ["Report it to the data protection officer and the Medical Director at once",
          "Delete the photo and say nothing",
          "Wait to see whether the supplier mentions it",
          "Tell the nurse to be careful next time and close the matter"], 0,
         "Report at once so the breach team has its full time to decide on notification."),
        ("Under the Data Privacy Act, how is a dialysis patient&rsquo;s hepatitis B status classed?",
         ["Public information within the unit",
          "Sensitive personal information",
          "Information that can be shared with any patient who asks",
          "Information outside the Act because it is clinical"], 1,
         "Health information is sensitive personal information."),
        ("You forgot to write a note about a 2:15 p.m. episode and remember at 5:00 p.m. What is correct?",
         ["Write it in the 2:15 p.m. space as if written then",
          "Leave it out because the shift is over",
          "Write it now, labeled as a late entry with the current time",
          "Ask the nurse to write it under her name"], 2,
         "Inserting it to look contemporaneous makes the record untrue."),
        ("A unit of 50 patients had 2 bloodstream infections in one month. What is the rate per 100 patient-months?",
         ["2.0", "4.0", "25", "0.4"], 1,
         "2 &divide; 50 &times; 100 = 4.0."),
        ("Monthly catheter percentages for 12 months show the last six points all below the median. What does this mean?",
         ["Nothing, because six points are too few",
          "The last point alone proves improvement",
          "The median must be recalculated without them",
          "A shift: a signal that something changed, which the team should explain"], 3,
         "Six or more consecutive points on one side of the median is a shift."),
        ("A unit&rsquo;s standardized hospitalization ratio is 1.2. Which statement is correct?",
         ["Admissions were 20% above the number expected for this case mix, and the confidence interval decides if this is a signal",
          "The unit is 20% worse than every other unit",
          "Admissions rose 1.2 per patient",
          "The ratio proves poor care"], 0,
         "Observed divided by expected. The interval decides."),
        ("What did the study of the U.S. End-Stage Renal Disease Quality Incentive Program show?",
         ["Penalized centers improved sharply",
          "Penalties lowered mortality",
          "Penalization was not associated with improvement in total performance scores",
          "Penalties were randomized"], 2,
         "No association was found across 5,830 centers."),
        ("After a medication omission, a review recommends &ldquo;remind staff to check orders.&rdquo; Why do critics call this a weak fix?",
         ["Reminders are illegal",
          "It relies on people remembering and leaves the system that allowed the error unchanged",
          "Medication omissions never harm patients",
          "Only the Medical Director can give reminders"], 1,
         "Reviews often settle for administrative fixes instead of changing system causes."),
        ("A team wants to cut catheter infections. Which plan best fits a well-run PDSA cycle?",
         ["Change five practices at once and check the rate in a year",
          "Retrain everyone and stop measuring",
          "Copy another unit&rsquo;s policy without testing it",
          "Test one change on one shift, measure adherence and the monthly rate, and decide at the next CQI meeting"], 3,
         "Small tests and data over time are what published PDSA projects most often lack."),
    ],
    "terms": [("Licensing order", "The DOH administrative order that sets the minimum standards a dialysis facility must meet to operate. For dialysis facilities this is AO 2012-0001."),
              ("Informed refusal", "A decision to decline or stop treatment after the risks of declining have been explained in words the patient understands."),
              ("Decision-making capacity", "The ability to understand information about a treatment, weigh it, and communicate a choice."),
              ("Sensitive personal information", "A class of personal data under the Data Privacy Act that includes health information."),
              ("Late entry", "A chart entry written after the event, labeled with the time it was actually written."),
              ("Patient-month", "One patient dialyzing in the unit for one month. The usual denominator for infection rates per 100 patient-months."),
              ("Run chart", "A time-ordered graph of a measure with its median line, read with simple rules for shifts, trends, and runs."),
              ("Standardized ratio", "Observed events divided by the number expected for the unit&rsquo;s case mix."),
              ("Near miss", "An error or hazard caught before it reached the patient."),
              ("Plan-Do-Study-Act (PDSA) cycle", "A small, planned test of one change, measured and then kept, adapted, or abandoned.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How quality assessment and continuous quality improvement work in a dialysis unit, with the monthly meeting."),
                 ("philhealth-z-packages.html", "Background on PhilHealth benefit packages. Check current rules with your unit&rsquo;s claims officer."),
                 ("advance-care-planning-dialysis.html", "The line between refusing one session, covered here, and choosing to stop dialysis, covered in Module 26.")],
    "calcs": ["calc-qapi-run-chart-spc.html", "calc-access-infection-rate.html", "calc-smr-hospitalization-rate.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
