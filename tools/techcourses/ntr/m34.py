# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 34: PhilHealth documentation, benefits and transitions.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. PhilHealth HD
benefit (PC 2023-0009, PC 2024-0023, the 2025 release, PA 2024-0036, the agreement form), PD Z (PC 2024-0036 and the
January 2025 release) checked on the web; kidney transplant Z Revision 1 (PC 2026-0019) taught from the coordinator-supplied
facts file read from the signed circular (PC2026-0019_FACTS.md), nothing added beyond it. Kripalani 2007 and Starmer 2014 against PubMed. Rates must be confirmed on the
date of service. No doses. Fictional case."""

MODULE = {
 'image_alt': 'A nephrology fellow and an internal medicine resident sit with a Filipino patient on hemodialysis and his son at a ward table, sorting a folder of laboratory results, a treatment record and a PhilHealth form before discharge.',
 'objectives': [
  '<strong>Intern:</strong> Document a dialysis patient&rsquo;s diagnosis, sessions, medicines and handoffs accurately, so that the record can support both the next clinician and a Philippine Health Insurance Corporation (PhilHealth) claim.',
  '<strong>Resident:</strong> Complete PhilHealth Dialysis Database (PDD) registration and hemodialysis (HD) benefit records correctly, and explain the 156-session benefit to a patient and family.',
  '<strong>Fellow:</strong> Own benefit-aware transitions between hospital, units, peritoneal dialysis (PD) and transplant without letting benefit rules drive the prescription.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the paper that keeps the patient dialyzing</span>The intern writes the notes and the medicine list that everyone downstream will copy. The resident fills in the registration and benefit papers and sits with the family to explain them. The fellow decides how the patient moves between settings, and checks that the prescription was written for the kidneys, not for the payer. When the paper is wrong, a patient arrives at a new unit with no record, no registration and no sessions recognized, and misses dialysis while the papers are fixed.</div>
{{plain:Think of the hemodialysis benefit as a book of prepaid bus tickets. Each calendar year the registered passenger gets 156 tickets, one per trip, enough for three trips a week all year. The tickets work only on accredited buses, and only if the passenger was registered before the first trip.}}
<p>The picture has a limit. A bus ticket does not care where you go. A dialysis prescription does: the number of sessions, their length and what is given in them come from the patient&rsquo;s kidneys, heart, volume and laboratory results, not from the size of the ticket book. PhilHealth says so itself: the services in the package depend on the provider&rsquo;s clinical assessment and are not intended to be provided on the patient&rsquo;s demand.[[ntr34_5]] The benefit removes a barrier; it does not write the order.</p>
{{cards:Key numbers (confirm on the date of service)|HD sessions covered per calendar year::Up to 156, for patients with chronic kidney disease stage 5 registered in the PDD (PhilHealth circulars 2023-0009 and 2024-0023)|HD package rate::PHP 6,350 per session, which PhilHealth&rsquo;s 2025 release dates from October 9, 2024; includes facility and professional fees|Maximum HD coverage per year::PHP 990,600 (PhilHealth 2025 release)|Unused HD sessions::Do not carry over to the next year (PhilHealth guide to circular 2023-0009)|Discharge summary available at the first post-discharge visit::12% to 34% of visits in a systematic review (Kripalani 2007)}}
<p>Most transitions go smoothly when three things travel with the patient: a true diagnosis of chronic kidney disease stage 5 with its evidence, an active PDD registration, and a complete transfer packet. A few go wrong because one of these is missing, or because someone chose a prescription to fit the benefit. Your work is to make the paper accurate, to make the handoff complete, and to keep the clinical decision clinical.</p>
""",
 'case': {'title': 'Going home to Sorsogon',
  'html': """
<p>Thursday, 3 p.m., the medicine ward of a tertiary hospital in Quezon City. Mr. Romeo Dizon, 58, a tricycle driver with type 2 diabetes for 15 years, was admitted three weeks ago breathless and vomiting, with a creatinine of 11.8 mg/dL and a potassium of 6.6 mmol/L. A creatinine of 4.1 mg/dL from a clinic visit 14 months ago is on his phone. His kidneys are 8.6 and 8.9 cm and echogenic. He started HD through a right internal jugular tunneled catheter and has had nine sessions. The attending nephrologist has documented chronic kidney disease stage 5 from diabetic kidney disease. He still passes about 500 mL of urine a day.</p>
<p>He will be discharged on Saturday to his family in Sorsogon City, where there is an accredited HD unit about 20 minutes from his home. Dr. Andrea Lim, the second-year resident, is asked to &ldquo;fix the PhilHealth papers.&rdquo; His son, Jun, who works in Dubai and is on the phone, asks: &ldquo;Can Papa do dialysis only twice a week so the 156 sessions last, and so we spend less on the fare?&rdquo; The unit in Sorsogon has asked for &ldquo;the usual referral.&rdquo;</p>
""",
  'questions': ['What must be documented and registered before Saturday so that Mr. Dizon&rsquo;s benefit works in Sorsogon?',
                'How should the team answer Jun&rsquo;s request for twice-weekly dialysis?',
                'What goes in the transfer packet, and how should the handoff to the Sorsogon unit be done?']},
 'sections': [
  ('hd-benefit', 'The HD benefit', 'The hemodialysis benefit: 156 sessions and what they require', """
<p>PhilHealth Circular 2023-0009 institutionalized the expansion of the HD benefit from 90 to 156 sessions a year, explaining the number as three sessions a week for 52 weeks, the frequency it describes as the current standard for adequate HD. It defines the PDD as the system that collects data on members and dependents with chronic kidney disease stage 5.[[ntr34_1]] PhilHealth&rsquo;s own guide to the circular states that sessions not used in a year cannot be added to the next.[[ntr34_2]] Revision 2, Circular 2024-0023, carries the benefit forward with coverage expansion.[[ntr34_3]]</p>
<p>The rate changed twice in 2024. PhilHealth&rsquo;s 2025 news release states that the package rate became PHP 6,350 per session effective October 9, 2024, that patients with chronic kidney disease stage 5 registered in the PDD can avail of up to 156 sessions a year, and that PhilHealth will therefore shoulder up to PHP 990,600 a year per patient.[[ntr34_4]] Press reports of the circular gave October 7 as the effective date; if a claim around those days matters, check the circular itself. The patient agreement form states that the PHP 6,350 rate includes the fees of the facility and the professional.[[ntr34_6]]</p>
<p>A 2024 advisory lists the minimum standards of the package: an erythropoiesis-stimulating agent in the vial sizes of the Philippine National Formulary, intravenous iron sucrose as indicated, heparin or enoxaparin as needed, laboratory tests as needed (complete blood count, creatinine, hepatitis profile, alkaline phosphatase, potassium, phosphorus, calcium, iron studies and albumin), low-flux or high-flux dialyzers, and the use of machines, utilities and staff time. It says coverage is subject to the policy&rsquo;s no-copay provision, that services depend on the patient&rsquo;s status by the provider&rsquo;s clinical assessment, and that they are not provided on demand.[[ntr34_5]] The Philippine Society of Nephrology (PSN) guideline asks the attending nephrologist to comply with the documentary requirements for the patient&rsquo;s PhilHealth HD benefit.[[ntr34_16]]</p>
{{fig:ntr34_a}}
<p>The causal chain from paper to dialysis chair is short. No PDD registration, no recognized sessions. No clear diagnosis of chronic kidney disease stage 5, no registration. No signed treatment record for each session, no claim. An error anywhere upstream becomes a family paying out of pocket, or a patient skipping sessions to save money.</p>
<div class="table-wrap"><table><thead><tr><th>What the record must show</th><th>Why it matters</th><th>Common error</th></tr></thead><tbody>
<tr><td>Diagnosis of chronic kidney disease stage 5, with evidence of chronicity (old creatinine values, kidney size, the attending&rsquo;s assessment)</td><td>PDD registration is for stage 5 chronic disease</td><td>Registering acute kidney injury that may recover as chronic disease</td></tr>
<tr><td>PDD registration status, before the first claimed session</td><td>Registration comes before availment</td><td>Assuming the next unit will register him</td></tr>
<tr><td>Each session: date, duration, prescription with the ultrafiltration rate (UFR), the physician present, signatures</td><td>The claim rests on the session record</td><td>Unsigned sheets; signatures by someone not present (Module 33)</td></tr>
<tr><td>Medicines and laboratory tests given in the session</td><td>They are part of the package minimum</td><td>Charging the family separately for package items</td></tr>
<tr><td>Signed patient agreement</td><td>Documents that the patient was informed of the benefit</td><td>Signed without explanation</td></tr>
<tr><td>Sessions used this calendar year</td><td>The receiving unit must know what remains</td><td>Not counted when the patient moves</td></tr>
</tbody></table></div>
<p>Two integrity points deserve to be said plainly. A patient on dialysis for acute kidney injury that may recover is not a patient with chronic kidney disease stage 5, and labeling him so to unlock a benefit is a false record that also closes the door on recovery-focused follow-up (Module 9). And the benefit has no place in deciding how many sessions a patient needs: the prescription comes from residual function, volume, potassium, symptoms and adequacy, as Modules 22 and 23 explain. When a family asks for fewer sessions to save the tickets, the honest answer is that 156 sessions are enough for three a week all year, and that any change in frequency is a clinical decision the attending makes and monitors.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> write the evidence of chronicity in your notes, with dates. <strong>Resident:</strong> start the PDD registration with the hospital&rsquo;s PhilHealth or dialysis staff as soon as the attending documents stage 5, not on the day of discharge. <strong>Fellow:</strong> check that every prescription change in the chart has a clinical reason written beside it.</div>
{{key:Register the true diagnosis early, document every session, and never let the ticket book write the prescription.}}
"""),
  ('pd-z', 'PD Z benefit', 'Peritoneal dialysis and its Z benefit', """
<p>Peritoneal dialysis is underused in the Philippines, and part of the reason is that the patient, the family and often the physician never hear it offered. A benefit exists. PhilHealth Circular 2024-0036 governs the Z benefits package for PD.[[ntr34_7]] PhilHealth&rsquo;s January 2025 release describes an expanded package effective January 1, 2025: for adults it covers continuous ambulatory peritoneal dialysis (CAPD) only, at PHP 389,640 or PHP 510,140 a year depending on the daily PD solutions needed; for children it covers CAPD and automated peritoneal dialysis (APD) at higher ranges. Patients must have chronic kidney disease stage 5 and be registered in the PDD first, must meet membership eligibility, must follow their treatment plan including follow-up visits, and must not share, sell or distribute the PD solutions provided to them. The release listed 51 contracted PD providers nationwide.[[ntr34_8]] PhilHealth has also run a pilot of APD coverage for children under separate advisories; check the current status.</p>
<p>The mechanism behind PD&rsquo;s value in the provinces is practical. PD runs at home, every day, without a machine for CAPD, without a three-times-weekly trip and without a dialysis chair. For a patient who lives two hours by bus from the nearest HD unit, or who wants to keep working, that changes life more than any laboratory number. It also needs a contracted provider for training, supplies and follow-up, a clean space at home, and someone able to do the exchanges.</p>
<div class="table-wrap"><table><thead><tr><th>Question in the family meeting</th><th>What to check</th><th>Where the answer comes from</th></tr></thead><tbody>
<tr><td>Is PD medically possible?</td><td>Abdominal surgery history, hernias, ability to do exchanges, home conditions</td><td>Attending nephrologist; Module 27</td></tr>
<tr><td>Is there a contracted PD provider near home?</td><td>The current PhilHealth list of contracted providers</td><td>PhilHealth list; hospital dialysis coordinator</td></tr>
<tr><td>Is the patient registered in the PDD?</td><td>Registration status</td><td>Same registration as for HD</td></tr>
<tr><td>Adult or child?</td><td>Adult package covers CAPD; pediatric arrangements include APD</td><td>Circular 2024-0036 and current advisories</td></tr>
<tr><td>What will the family still pay?</td><td>Transport, home preparation, items outside the package</td><td>Provider; hospital social service</td></tr>
</tbody></table></div>
<p>There is no trial in this module&rsquo;s sources showing that the PD benefit changes outcomes; what it changes is access. The decision between HD and PD rests on the clinical and personal factors in Module 27, and both should be offered where both are possible.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> ask every new dialysis patient whether anyone has explained PD. <strong>Resident:</strong> know the nearest contracted PD provider to your hospital&rsquo;s catchment. <strong>Fellow:</strong> offer PD with HD in every modality conversation where it is medically possible, and document that you did.</div>
{{key:A benefit no one mentions is a benefit no one uses. Offer PD where it is possible, and know who near the patient&rsquo;s home can provide it.}}
"""),
  ('transplant-z', 'Transplant Z benefit', 'The kidney transplant Z benefit, Revision 1', """
<p>The best treatment for many patients with kidney failure is a transplant, and cost is one of the reasons Filipino families never begin the evaluation. PhilHealth Circular 2024-0035 set the first Z benefits package for kidney transplantation.[[ntr34_10]] Circular 2026-0019, the Z Benefits Package for Kidney Transplantation (Revision 1), signed on October 26, 2026, amends it and covers both adults and children.[[ntr34_17]] The circular takes effect 15 days after publication in the Official Gazette or a newspaper of general circulation; the document itself does not state the publication date, so confirm the effective date with PhilHealth. Care after the transplant falls under separate PhilHealth benefits; check the current circulars.</p>
<p><strong>Who and where.</strong> All patients with chronic kidney disease stage 5 who meet the clinical criteria are eligible, with a living donor, related or non-related, or a deceased donor, subject to PhilHealth&rsquo;s membership eligibility rules. Selection follows the circular&rsquo;s pre-authorization checklist and request form, and the benefit is available only in contracted health facilities. A multidisciplinary team (MDT) that includes the attending nephrologist, a transplant surgeon and, for living-donor procedures, a urologist evaluates donor and recipient and submits the treatment plan. Facilities must follow the ethical guidelines on living donation (Department of Health [DOH] Administrative Order 2021-0059) and the laws on voluntary donation; deceased donation must be non-commercial, and a deceased-donor claim needs an organ retrieval report from an authorized organ procurement organization.[[ntr34_17]]</p>
<p><strong>Timing.</strong> For a living-donor transplant, the facility&rsquo;s liaison submits the pre-authorization checklist and request form, the Member Empowerment form and the MDT plan before the benefit is used. For a deceased-donor transplant, pre-authorization is submitted within 2 working days after the transplant. An approved pre-authorization is valid for 180 calendar days. Contracted facilities assign a kidney transplantation (KT) registration number and submit a KT Registry form for every patient, and the facility files the claim within 60 days after discharge.[[ntr34_17]]</p>
<p><strong>What it covers.</strong> Pre-transplant evaluation; immunosuppressant therapy in the induction phase until one week after discharge from the transplant; the transplant surgery; donor management, donor nephrectomy, and organ retrieval and preservation. The 45-day annual benefit limit does not apply. There is no separate facility and professional fee: PhilHealth pays the facility, which distributes the professional fee. Drugs are reimbursed if they are in the latest Philippine National Drug Formulary (PNDF); otherwise they need a positive health technology assessment recommendation.[[ntr34_17]]</p>
<div class="table-wrap"><table><thead><tr><th>Code</th><th>Donor</th><th>Induction</th><th>Surgery or retrieval</th><th>Package rate (PHP)</th></tr></thead><tbody>
<tr><td>Z025A1</td><td>Living</td><td>Basiliximab or equine antithymocyte globulin (ATG)</td><td>Laparoscopic donor, open recipient</td><td>993,000</td></tr>
<tr><td>Z025A2</td><td>Living</td><td>Basiliximab or equine ATG</td><td>Open surgery for both</td><td>865,000</td></tr>
<tr><td>Z025B1</td><td>Living</td><td>Rabbit ATG</td><td>Laparoscopic donor, open recipient</td><td>1,045,000</td></tr>
<tr><td>Z025B2</td><td>Living</td><td>Rabbit ATG</td><td>Open surgery for both</td><td>918,000</td></tr>
<tr><td>Z026A1</td><td>Deceased</td><td>Basiliximab or equine ATG</td><td>Retrieval with machine perfusion</td><td>2,093,000</td></tr>
<tr><td>Z026A2</td><td>Deceased</td><td>Basiliximab or equine ATG</td><td>Retrieval with cold storage</td><td>1,583,000</td></tr>
<tr><td>Z026B1</td><td>Deceased</td><td>Rabbit ATG</td><td>Retrieval with machine perfusion</td><td>2,146,000</td></tr>
<tr><td>Z026B2</td><td>Deceased</td><td>Rabbit ATG</td><td>Retrieval with cold storage</td><td>1,636,000</td></tr>
</tbody></table></div>
<p>Rates as printed in the circular signed October 26, 2026; confirm the effective date and current rates with your PhilHealth liaison on the date of service.</p>
<p><strong>What the family pays.</strong> There is no copayment in basic or ward accommodation, none for recipients who need special beds such as reverse isolation, and none for managing postoperative complications of donors and recipients. Copayment is allowed only for amenities, the choice of a physician within the MDT, specialist fees in non-basic accommodation, or services the package does not cover, and it must be agreed during the Member Empowerment form discussion. No balance billing beyond the package rate is allowed for covered services.[[ntr34_17]]</p>
<p><strong>If the graft fails.</strong> After the Z benefit, patients remain eligible for the HD or PD benefits if they return to dialysis, whether because of graft failure from rejection or infection, acute kidney injury or other complications.[[ntr34_17]] Tell families this early: fear of losing the dialysis benefit should not be the reason they decline a transplant evaluation.</p>
<div class="table-wrap"><table><thead><tr><th>You can say</th><th>You should not say</th></tr></thead><tbody>
<tr><td>&ldquo;PhilHealth has a Z benefit for kidney transplantation, from a living or a deceased donor, for adults and children, at contracted centers.&rdquo;</td><td>&ldquo;It is covered,&rdquo; before the transplant center has checked eligibility and pre-authorization</td></tr>
<tr><td>&ldquo;The package rate depends on the donor type, the induction medicine and the surgical method; the transplant center&rsquo;s liaison will confirm the current rate.&rdquo;</td><td>A rate as if it were final, without confirming the effective date</td></tr>
<tr><td>&ldquo;In ward accommodation there is no copayment, and the hospital may not bill beyond the package for covered services.&rdquo;</td><td>Promises about medicines after the induction phase; those fall under other benefits and the formulary</td></tr>
<tr><td>&ldquo;If the kidney fails, you can return to the dialysis benefit.&rdquo;</td><td>&ldquo;You will lose PhilHealth dialysis if you get a transplant&rdquo;</td></tr>
</tbody></table></div>
<p>The physician&rsquo;s job is the same whatever the rate. Refer early to a transplant center when the estimated glomerular filtration rate (eGFR) is falling toward kidney failure (Module 29), identify potential living donors and explain that donation must be voluntary and within the ethical rules, and keep the patient&rsquo;s records, serologies and dialysis history complete so that the MDT evaluation and pre-authorization are not delayed.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> record whether transplant has been discussed and whether a living donor has been named. <strong>Resident:</strong> refer to the transplant center and its PhilHealth liaison, and tell the family about the no-copayment and return-to-dialysis rules. <strong>Fellow:</strong> know your nearest contracted transplant center, the pre-authorization timing for living and deceased donors, and read the current circular before every benefit conversation.</div>
{{key:Quote a benefit only from the circular you have read, with its date, and send the family to the transplant center&rsquo;s liaison to confirm the effective date and rate on the day.}}
"""),
  ('transfer-packet', 'The transfer packet', 'The transfer packet and the handoff', """
<p>A dialysis patient who moves from a hospital to an outpatient unit, from one unit to another, or from one province to another carries risk in the move itself. Information gets lost at each transfer. A systematic review of communication at hospital discharge found that direct communication between hospital physicians and primary care physicians happened in only 3% to 20% of discharges, that a discharge summary was available at the first post-discharge visit in only 12% to 34%, and that summaries often lacked test results (missing from 33% to 63%), discharge medicines (2% to 40%), tests pending at discharge (65%) and follow-up plans (2% to 43%).[[ntr34_13]] Those studies were observational, mostly from North American settings, but every Filipino trainee who has received a patient with &ldquo;no papers&rdquo; will recognize them.</p>
<p>Structured handoffs help. In the multicenter study of a structured resident handoff program, medical errors fell from 24.5 to 18.8 per 100 admissions and preventable adverse events from 4.7 to 3.3 per 100 admissions after implementation, without longer handoffs.[[ntr34_14]] The design was before and after, so it shows association rather than proof; the lesson that a standard structure reduces omissions carries over to a transfer letter.</p>
{{fig:ntr34_b}}
<div class="table-wrap"><table><thead><tr><th>Transfer packet item</th><th>What the receiving unit does with it</th></tr></thead><tbody>
<tr><td>Diagnosis, cause of kidney failure, evidence of chronicity, date of first dialysis</td><td>Confirms eligibility and plans long-term care</td></tr>
<tr><td>PDD registration status and sessions used this calendar year</td><td>Continues the benefit and counts what remains</td></tr>
<tr><td>Current prescription: frequency, duration, dialyzer, target weight and fluid removal limits, anticoagulation approach, as written by the attending</td><td>Starts the first session safely</td></tr>
<tr><td>Vascular access: type, site, date placed, problems; plan for permanent access</td><td>Protects the access; continues the referral</td></tr>
<tr><td>Hepatitis B surface antigen, hepatitis C antibody and human immunodeficiency virus (HIV) results with dates; hepatitis B vaccination status</td><td>Assigns the correct station or machine</td></tr>
<tr><td>Recent laboratory results, with dates; results still pending and who will follow them</td><td>Avoids repeating tests; closes loops</td></tr>
<tr><td>Medicine list with what changed and why; allergies</td><td>Prevents duplication and omission</td></tr>
<tr><td>Residual urine output; heart, volume and blood pressure issues; intradialytic events so far</td><td>Anticipates problems in the chair</td></tr>
<tr><td>Goals of care and who decides with the patient</td><td>Respects the family&rsquo;s decisions</td></tr>
<tr><td>Sending attending&rsquo;s name and contact number</td><td>Lets the receiving physician call</td></tr>
</tbody></table></div>
<p>Send the packet through a channel the patient has agreed to, and only to the people who need it; the Data Privacy Act treats health information as sensitive personal information.[[ntr34_15]] Give the patient and family a copy to carry, because the courier is often the only reliable delivery system across provinces. Then make a telephone call, physician to physician or unit to unit, before the first session. The call is where the receiving physician asks the question your letter did not answer.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Sessions remaining = 156 &minus; sessions already claimed this calendar year.<br>A patient who has had 9 sessions in the hospital this year has 147 left for the rest of the calendar year, wherever he dialyzes. A patient who moves in December with 140 sessions used has 16 left, and the count resets on January 1.}}
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>a family asks for fewer sessions or a shorter prescription to save money or sessions;</li><li>a patient is about to be discharged with no confirmed receiving unit or first session date;</li><li>a diagnosis of chronic kidney disease stage 5 is being written mainly to register a patient whose kidneys may recover;</li><li>the receiving unit cannot take the patient because of serology status or capacity.</li></ul>}}
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> draft the packet from the chart and list what you could not find. <strong>Resident:</strong> complete it, give the family a copy, and confirm the first session date at the receiving unit. <strong>Fellow:</strong> make the physician-to-physician call and check that the plan is safe for the first week.</div>
{{key:A transfer is complete when the receiving physician has the packet, the patient has a copy, someone has called, and the first session has a date.}}
"""),
 ],
 'debrief': [
  '<p><strong>Papers before Saturday.</strong> The attending has documented chronic kidney disease stage 5 with evidence of chronicity: an old creatinine of 4.1 mg/dL, small echogenic kidneys and long-standing diabetes. Andrea makes sure that evidence is written in the chart with dates, starts the PDD registration now with the hospital&rsquo;s PhilHealth or dialysis staff, and makes sure each of the nine sessions has a signed treatment record. The family signs the HD benefits agreement after it is explained in Tagalog. She counts the sessions claimed this year so the Sorsogon unit knows what remains.</p>',
  '<p><strong>Twice a week.</strong> The team thanks Jun for asking openly. The 156 sessions cover three sessions a week all year, so saving tickets is not a reason to cut sessions, and the PHP 6,350 package includes the facility and professional fees. Whether Mr. Dizon could do fewer sessions is a clinical question: he still passes about 500 mL of urine, but he arrived with hyperkalemia and fluid overload, and any change in frequency would be the attending&rsquo;s decision with close monitoring of potassium, weight and symptoms. Transport cost is a real burden; the team refers the family to the hospital social service and records the concern. PD is also explained as an option for later, once his access and training can be arranged near home.</p>',
  '<p><strong>The packet and the call.</strong> The packet carries the diagnosis and evidence of chronicity, PDD status, sessions used, the attending&rsquo;s current prescription, the catheter details and the plan for a fistula, dated hepatitis B, hepatitis C and HIV results, recent laboratory results and pending tests, the medicine list with changes, residual urine output, goals of care and the attending&rsquo;s number. Mr. Dizon carries a copy. The fellow calls the Sorsogon unit&rsquo;s nephrologist on Friday and confirms the first session for Monday, so no more than one interdialytic interval passes without dialysis.</p>',
 ],
 'skills': {'title': 'PhilHealth documentation, benefits and transitions',
  'intro': 'Complete with a preceptor, on a real discharge with consent or on a simulated chart. Sign-off is local.',
  'items': [('Documents the evidence of chronicity for chronic kidney disease stage 5 with dates and sources', False),
            ('Explains the 156-session HD benefit, its rate and the PDD requirement to a patient and family in plain language', False),
            ('Identifies the nearest contracted PD provider and explains the PD Z benefit conditions', False),
            ('Completes a transfer packet with every item on the checklist and lists anything missing', False),
            ('Makes a physician-to-physician handoff call and confirms the first session date at the receiving unit', False)],
  'placement': 'Medicine ward, dialysis unit or discharge planning meeting'},
 'quiz': [
  ('An intern is writing the progress note of a patient newly started on maintenance hemodialysis. Which entry best supports both the next clinician and the PhilHealth registration?',
   ['&ldquo;ESRD, on HD&rdquo;',
    'Chronic kidney disease stage 5 from diabetic kidney disease, with dated evidence of chronicity (creatinine 14 months ago, kidney size on ultrasound) and the attending&rsquo;s assessment',
    '&ldquo;Renal failure, for dialysis, PhilHealth to follow&rdquo;',
    'The latest creatinine value only'],
   1,
   'PDD registration is for chronic kidney disease stage 5, and the next clinician needs the evidence that the disease is chronic. A bare label (the tempting distractor) tells neither of them why.'),
  ('A resident explains the HD benefit to a newly registered patient. Which statement is accurate as of PhilHealth&rsquo;s 2025 release?',
   ['Up to 90 sessions a year at PHP 4,000 per session',
    'Up to 156 sessions a calendar year at PHP 6,350 per session, for patients registered in the PDD, with unused sessions not carried over',
    'Unlimited sessions for any patient on dialysis',
    'Up to 156 sessions, and unused sessions carry over to the next year'],
   1,
   'PhilHealth states up to 156 sessions a year at PHP 6,350 per session for PDD-registered patients with chronic kidney disease stage 5, and its guide says unused sessions are not added to the next year. The carry-over option is the most tempting error.'),
  ('A fellow reviews a request to reduce a patient&rsquo;s HD from three to two sessions a week &ldquo;so the benefit lasts.&rdquo; What principle should guide the decision?',
   ['Benefit limits should set the prescription to avoid running out',
    'The benefit covers three sessions a week all year, so frequency is a clinical decision based on residual function, volume, potassium and symptoms, made and monitored by the attending',
    'Twice weekly is always adequate',
    'The patient&rsquo;s request should be followed without assessment'],
   1,
   'PhilHealth itself states that services follow clinical assessment, not demand, and 156 sessions equal three a week for 52 weeks. Following the request without assessment (a tempting distractor) ignores the patient&rsquo;s safety.'),
  ('A family whose father is on hemodialysis declines a transplant evaluation because they fear losing the dialysis benefit and being billed beyond PhilHealth. Under PhilHealth Circular 2026-0019, what can you accurately tell them?',
   ['Transplant patients permanently lose the HD benefit',
    'Patients who return to dialysis after the Z benefit remain eligible for HD or PD benefits, and there is no copayment in ward accommodation and no balance billing beyond the package rate for covered services',
    'The family must pay all fees above PHP 500,000',
    'PhilHealth covers transplant only from deceased donors'],
   1,
   'The circular keeps HD and PD eligibility after graft failure and bars copayment in basic or ward accommodation and balance billing for covered services. Losing the dialysis benefit (the tempting distractor) is a common fear the circular contradicts; confirm the effective date with the liaison.'),
  ('A patient on HD moves from Iloilo City to a unit in Roxas City. Which handoff is most likely to prevent a missed session and an unsafe first treatment?',
   ['A one-line referral letter given to the patient',
    'An email of the full chart to the receiving unit&rsquo;s general address',
    'A complete transfer packet, a copy for the patient, a physician-to-physician call, and a confirmed first session date',
    'Telling the patient to ask the new unit to call the old one'],
   2,
   'Discharge information is often missing at the first visit, and structured handoffs are associated with fewer errors. Sending the whole chart to a general address (a tempting distractor) is neither structured nor a safe privacy practice.'),
 ],
 'terms': [('APD', 'Automated peritoneal dialysis'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('ESRD', 'End-stage renal disease'),
           ('HD', 'Hemodialysis'),
           ('HIV', 'Human immunodeficiency virus'),
           ('PD', 'Peritoneal dialysis'),
           ('PDD', 'PhilHealth Dialysis Database'),
           ('PhilHealth', 'Philippine Health Insurance Corporation'),
           ('PHP', 'Philippine peso'),
           ('PSN', 'Philippine Society of Nephrology')],
 'readings': [('attending-nephrologist-21-philhealth-claims.html', 'Attending Nephrologist, Module 21: PhilHealth Claims'),
              ('philhealth-claims-02-eligibility-and-pdd.html', 'PhilHealth Claims, Module 2: Eligibility and the PDD'),
              ('hemodialysis-transfer-guide.html', 'Hemodialysis Transfer Guide'),
              ('philhealth-z-packages.html', 'PhilHealth Z Benefit Packages')],
 'calcs': ['calc-philhealth-claims-toolkit.html', 'calc-dialysis-continuity-planner.html', 'calc-hd-session-review.html', 'calc-starting-dialysis-planner.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
