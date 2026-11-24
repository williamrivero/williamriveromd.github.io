# -*- coding: utf-8 -*-
"""Physician on Duty, Module 28: Outside the Unit: Surgery, Contrast, Hospital Stays, and Travel.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty beside a dialysis chair talks on the phone while an orthopedic resident holds a consent form. An older man with a splinted hip lies on a stretcher next to the dialysis machine.",
    "objectives": [
        "Explain why the timing of hemodialysis around surgery matters, and summarize the evidence on the dialysis-to-surgery interval and postoperative risk.",
        "Advise a referring doctor on iodinated and gadolinium-based contrast in a dialysis patient, including the patient who still makes urine, using the American College of Radiology and National Kidney Foundation consensus statements.",
        "Protect the vascular access and the arm veins during a hospital stay, and write a clear access-protection instruction.",
        "Write a peri-procedure dialysis note that states the facts and the questions for the attending nephrologist, without certifying fitness for surgery on the nephrologist&rsquo;s behalf.",
        "Prepare a patient for travel with the right documents, test results, and prescription summary, and explain the infection risk of dialysis in another unit.",
        "Plan the first session after a hospital discharge, and recognize the patient at high risk of readmission.",
    ],
    "big": """
{{plain:Picture a house whose only drain is blocked. Water, ash, and kitchen waste pile up until the garbage truck comes on its fixed days. Now a contractor arrives, a crowd comes to dinner, and the truck is told to skip a visit. Nobody in the crowd knows the drain is blocked.}}
<p>The picture has a limit. A patient on dialysis is not a passive house. Potassium shifts in and out of cells, and some patients still make a little urine. But the core point holds. A dialysis patient has no steady exit for potassium, water, and acid, and the doctors who plan surgery, scans, and admissions often do not see dialysis patients every day.</p>
{{cards:Key terms for this module|Peri-procedure period::The time immediately before, during, and after an operation or invasive test.|Dialysis-to-surgery interval::The time between the end of the last dialysis session and the start of a procedure.|Residual kidney function::The filtration that the patient&rsquo;s own kidneys still perform. It is usually seen as some daily urine output.|Iodinated contrast::The contrast medium used for computed tomography (CT) and angiography.|Gadolinium-based contrast::The contrast medium used for magnetic resonance imaging (MRI).|Peripherally inserted central catheter (PICC)::A long catheter placed through an arm vein with its tip in a large central vein.|Vein preservation::Protecting the arm veins from needles, cuffs, and catheters so they remain usable for a fistula or graft.|Readmission::A return to hospital within a short time after discharge, often counted at 30 days.}}
<p>Most dialysis patients pass through surgery, scans, and hospital stays without harm when the unit and the other teams share facts early. A few are harmed by gaps: a skipped session before an operation, an emergency session ordered for no reason, a catheter in the arm that was saved for a fistula, a trip with no chair booked at the other end. Your work is to supply the facts, protect the access, and bring the attending nephrologist into every decision that changes the prescription.</p>
""",
    "case": {"title": "Surgery tomorrow, dialysis today", "html": """
<p>It is Friday, two in the afternoon. Mr. Ernesto Villanueva, 66, dialyzes on Mondays, Wednesdays, and Fridays through a left forearm fistula. He is in the chair, and the session is running under the standing order. The nurse, Ms. Grace Santos, hands you a note from the orthopedic resident.</p>
<p>Mr. Villanueva fell at home on Wednesday night and has a right hip fracture. Surgery is booked for Monday at 7 AM. The note reads: &ldquo;Please clear for surgery. He also needs a CT angiogram of the leg tonight. Can he have contrast? Should we put a PICC in the left arm for antibiotics?&rdquo;</p>
<p>Today he arrived 2.8 kilograms above his dry weight. His blood pressure is 150/88 mm Hg. His potassium this morning was 5.8 mmol/L and his hemoglobin 9.4 g/dL. He takes clopidogrel. He still passes about 300 mL of urine a day. These are illustrative values for this case, not targets.</p>
""", "questions": ["What is the problem with a Monday 7 AM operation after a Friday session, and what will you ask the attending nephrologist to decide?",
                  "What do you tell the resident about contrast tonight, given his urine output?",
                  "What do you write about the PICC and the &ldquo;clearance,&rdquo; and what goes in your note?"]},
    "sections": [
        ("why", "Why surgery is different", "Why the dialysis patient is different on the operating table", """
<p>Working kidneys are the safety valve of the peri-procedure period. They excrete the potassium released by injured tissue, the acid made by poorly perfused muscle, and the water given in intravenous (IV) fluids. In a dialysis patient the valve is closed. Whatever enters the blood stays until the next session.</p>
{{fig:pod28_surgeryload}}
<p>Module 2 explained how potassium, water, and acid accumulate between sessions. Surgery adds to each through a chain of causes.</p>
<div class="table-wrap"><table>
<thead><tr><th>What happens in surgery</th><th>What it does to the blood</th><th>What the other team may see</th></tr></thead>
<tbody>
<tr><td>Tissue injury and crushed muscle</td><td>Cells break and release potassium and acid</td><td>A potassium rise after the operation that is larger than expected</td></tr>
<tr><td>Transfusion of stored blood</td><td>Stored red cells leak potassium into the bag as they age</td><td>A potassium rise after several units</td></tr>
<tr><td>A long fast</td><td>Insulin falls. Insulin normally drives potassium into cells, so more stays in the blood</td><td>A higher potassium on the morning of surgery</td></tr>
<tr><td>Acidosis from poor perfusion</td><td>Hydrogen ions enter cells and potassium leaves them</td><td>Potassium and acid rising together</td></tr>
<tr><td>Intravenous fluids</td><td>No urine to excrete them, so they stay in the circulation and tissues</td><td>Breathlessness and edema after the operation</td></tr>
</tbody></table></div>
<p>Uremic bleeding (Module 4), heparin (Module 19), and drug dosing (Module 20) add to the risk and are not repeated here.</p>
<h3>What the evidence shows about risk</h3>
<p>Palamuthusingam and colleagues pooled 49 studies of elective surgery, with 41,822 patients on chronic dialysis and more than 10 million without kidney failure. Dialysis was associated with higher odds of death after surgery in every surgical field, with an odds ratio (OR) from 4.0 to 10.8.[[palamuthusingam2020]]</p>
{{cards:Postoperative death: dialysis compared with normal kidney function|Orthopedic surgery::OR 10.8 (95% confidence interval 7.3 to 15.9), the highest excess in the review.|Vascular surgery::OR 4.0 (3.2 to 4.9), the lowest excess in the review.|After adjustment::The excess was smaller after accounting for age and other illness, but remained.|What it does not show::Which steps would lower the risk. These are observational data.}}
<p>Part of the excess reflects the heart disease, diabetes, and frailty that travel with kidney failure. Either way, these patients are fragile in surgery, and the plan should start early.</p>
<p>The Revised Cardiac Risk Index (RCRI) was derived in 4,315 patients aged 50 or older having elective major noncardiac surgery at one teaching hospital. It counts six predictors, and a serum creatinine above 2.0 mg/dL is one of them. Every dialysis patient therefore starts with at least one point.[[lee1999]]</p>
<p>The 2024 American Heart Association and American College of Cardiology (AHA/ACC) multisociety guideline on perioperative cardiovascular management replaced the 2014 guideline.[[acc_aha_periop2024]] For patients with known cardiovascular disease being considered for noncardiac surgery, it states that a validated risk-prediction tool can be useful to estimate the risk of major cardiac events (Class of Recommendation 2a, Level of Evidence B-NR). The cardiac work-up belongs to the anesthesiologist and the cardiologist. Your part is to make sure they know what dialysis brings.</p>
{{key:A dialysis patient carries several times the postoperative risk of other patients. The safest operation is one planned around the dialysis schedule.}}
"""),
        ("timing", "Timing", "Timing dialysis around surgery and procedures", """
<p>Think of a calendar. The surgeon picks the day. The unit&rsquo;s job is to have the patient arrive with the smallest possible load of potassium and fluid. On a thrice-weekly schedule, potassium and fluid peak at the end of the long weekend gap (Module 2). A Monday morning operation lands at that peak.</p>
{{fig:pod28_calendar}}
<h3>The Medicare study</h3>
<p>No trial has tested the best interval between dialysis and surgery. The largest study is a retrospective cohort by Fielding-Singh and colleagues. It covered 1,147,846 procedures in 346,828 United States Medicare patients on hemodialysis from 2011 to 2018. The outcome was death within 90 days.[[fieldingsingh2022]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Last session before surgery</th><th>90-day mortality</th><th>Absolute difference compared with 1 day</th><th>Adjusted hazard ratio</th></tr></thead>
<tbody>
<tr><td>1 day before</td><td>4.2%</td><td>Reference</td><td>Reference</td></tr>
<tr><td>2 days before</td><td>4.7%</td><td>0.6 percentage points</td><td>1.14</td></tr>
<tr><td>3 days before</td><td>5.2%</td><td>1.0 percentage point</td><td>1.25</td></tr>
</tbody></table></div>
<p>Dialysis on the day of surgery was associated with lower 90-day mortality, 4.0% compared with 4.5% without same-day dialysis (adjusted hazard ratio 0.88). Same-day dialysis also weakened the association between a long interval and death.[[fieldingsingh2022]]</p>
<p>The authors called the absolute differences small and warned of residual confounding. A patient operated on three days after dialysis may have been sicker or operated on urgently. The study shows an association, not that moving a session saves lives.</p>
{{formula:<strong>Illustrative arithmetic from the published rates, not a target.</strong><br>Absolute risk difference = 5.2% &minus; 4.2% = 1.0 percentage point = 0.010.<br>Number needed to harm = 1 &divide; 0.010 = 100.<br>In this association, about 100 procedures done 3 days after dialysis rather than 1 day go with one additional death within 90 days.[[fieldingsingh2022]]<br>What it tells you: the excess risk is real but modest. What it does not tell you: that an extra session would prevent that death.}}
<h3>Worked example: Mr. Villanueva&rsquo;s weekend</h3>
{{formula:<strong>Illustrative interval.</strong> Friday session ends at 6 PM. Surgery starts Monday at 7 AM.<br>Friday 6 PM to Monday 6 PM = 72 hours. Monday 6 PM back to 7 AM = 11 hours earlier.<br>Interval = 72 &minus; 11 = 61 hours, about 3 calendar days.<br>Published 90-day mortality: 5.2% at 3 days compared with 4.2% at 1 day, an association.[[fieldingsingh2022]]<br>Options to present to the attending nephrologist: a session on Sunday, an early session on Monday before surgery, or the usual schedule with a potassium check before surgery.<br>What it tells you: he will reach surgery at the end of his longest gap. What it does not tell you: which option is right. That depends on his potassium, his fluid, the timing of the operation, and the unit&rsquo;s capacity.}}
<p>The site&rsquo;s continuity planner and interdialytic weight gain calculator help you prepare the call. Neither decides the plan.</p>
{{flow:Dialysis timing around a planned procedure|Know the date::Confirm the procedure, the date, the start time, and the requesting team.|Map the gap::Find the last session before the procedure. Note whether the procedure falls after the long gap.|Gather the facts::Today&rsquo;s weight gain, the last potassium and its date, urine output, the access, and the anticoagulant and antiplatelet medicines.|Ask about heparin::Note the heparin used in sessions. Module 19 covers heparin-free sessions and bleeding.|Call the attending nephrologist::Present the gap, the facts, and the options. The nephrologist decides on any extra, moved, or heparin-free session.|Write the plan::Record the decision, who made it, and what the surgical team was told.}}
{{call:Stop and call the attending nephrologist when a surgeon or anesthesiologist asks for an extra or rescheduled session, a heparin-free session, or a potassium result before surgery, and when any procedure is planned on the access arm.}}
"""),
        ("contrast", "Contrast", "Contrast for CT and MRI: what is safe and what to arrange", """
<p>Contrast cannot injure filtration that no longer exists. A kidney that still makes urine, however little, has something left to protect. Module 3 explained why that leftover function matters.</p>
{{fig:pod28_contrastrkf}}
<h3>Iodinated contrast for CT and angiography</h3>
<p>The old fear with iodinated contrast was contrast-induced acute kidney injury. The American College of Radiology (ACR) and the National Kidney Foundation (NKF) reviewed this in 2020. Their consensus statement says the risk has been overstated, because older studies lacked control groups.[[acr_nkf_iodinated2020]]</p>
<p>The same statement advises IV normal saline prophylaxis for patients with acute kidney injury or an estimated glomerular filtration rate (eGFR) below 30 mL/min/1.73 m&sup2; who are not on maintenance dialysis. This is a consensus statement, not a graded recommendation. It does not apply to your patients on maintenance dialysis.[[acr_nkf_iodinated2020]]</p>
<p>What about the urine a dialysis patient still makes? Oloko and colleagues reviewed 9 studies with 434 dialysis patients and pooled the 7 with complete data. Residual function changed by a mean of &minus;0.16 mL/min after contrast (95% confidence interval &minus;0.66 to 0.34), which was not significant. The studies were small and varied widely, and few reported clinical outcomes.[[oloko2020]] The evidence suggests no large loss but cannot exclude a small one.</p>
<p>Should the patient be dialyzed right after the scan? A narrative review in the &ldquo;Things We Do for No Reason&rdquo; series argues against emergency dialysis after contrast in patients on chronic hemodialysis. Its reasons: modern low-osmolar agents cause small fluid shifts, an extra session does not protect residual function, and delaying a needed scan can harm the patient.[[ninan2022]] This is expert argument, not a trial.</p>
{{formula:<strong>Worked walk-through, illustrative.</strong> Mr. Villanueva, CT angiogram of the leg tonight.<br>Step 1. Agent: iodinated contrast.<br>Step 2. He is on maintenance dialysis, so the saline prophylaxis advice for patients not on dialysis does not apply.[[acr_nkf_iodinated2020]]<br>Step 3. He passes about 300 mL of urine a day. Tell the attending nephrologist, who weighs the need for the scan against a possible small effect on residual function. Pooled data show no significant loss.[[oloko2020]]<br>Step 4. No emergency session is needed solely for the contrast.[[ninan2022]]<br>Step 5. Mention heart failure or a large contrast volume in the call.<br>What it tells you: the scan should not wait for dialysis. What it does not tell you: whether this patient&rsquo;s urine output will change.}}
<p>A warning: the site&rsquo;s contrast kidney injury risk score was built for patients not on dialysis. Do not use it for a patient on maintenance dialysis.</p>
<h3>Gadolinium-based contrast for MRI</h3>
<p>The fear with gadolinium was nephrogenic systemic fibrosis (NSF), a thickening of the skin and organs seen with older agents in patients with advanced kidney failure. The 2021 ACR and NKF consensus statement reports zero NSF cases after 4,931 doses of group II agents in patients with eGFR below 30. The upper bound of the 95% confidence interval was 0.2% for patients on dialysis. The statement says that starting or changing dialysis is likely unnecessary after a group II or group III agent.[[acr_nkf_gbcm2021]] This is a consensus statement, not a graded recommendation.</p>
{{cards:Contrast decision card|Which agent::Iodinated for CT and angiography. Gadolinium-based for MRI. Ask the radiology team which group of gadolinium agent they use. The reassurance covers group II and group III agents only. For any other agent, tell the attending nephrologist.|Anuric patient::No residual function to lose. Keep the usual schedule unless the nephrologist decides otherwise.|Patient who still makes urine::Tell the attending nephrologist before the scan if you can. The nephrologist weighs the benefit of the scan against the residual function.|What to ask::Daily urine volume, the agent and its group, the expected volume, heart failure, and when the next session is due.|Who decides::The requesting doctor decides the scan. The attending nephrologist decides any change to dialysis.}}
{{key:Do not order an emergency session solely because contrast was given. Do tell the nephrologist when a patient who still makes urine is scheduled for contrast.}}
"""),
        ("ward", "On the ward", "The dialysis patient on the ward: protect the veins and the schedule", """
<p>Picture a wristband that says: dialysis access arm, no blood pressure cuff, no needles, no IV lines. In a hospital, many people who have never met the patient will reach for an arm. Without a visible instruction, any of them can damage a working fistula or the veins saved for the next one.</p>
{{fig:pod28_wristband}}
<p>Modules 9 and 10 explained why the arm veins are a limited supply. Needles and catheters scar and narrow veins, and a central vein catheter can block outflow from the whole arm.</p>
<h3>What the evidence shows</h3>
<p>El Ters and colleagues studied 282 hemodialysis patients in seven units. Patients without a working fistula were more likely to have had a PICC in the past: 44.2% compared with 19.7% of patients with a working fistula. After adjustment for vein size, sex, and earlier central catheters, a prior PICC was associated with lack of a working fistula (adjusted OR 2.8, 95% confidence interval 1.5 to 5.5).[[elters2012]] This was a retrospective case-control study of mostly white patients. It cannot prove that the PICC caused the loss, but the direction fits what is known about vein injury.</p>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 vascular access guideline addresses this in its section on vessel preservation. Statement 6.10 reads: &ldquo;KDOQI considers it reasonable to protect all central and peripheral arteries and veins from damage whenever possible.&rdquo; It names avoidance of peripherally inserted catheters and unnecessary venipuncture in patients on dialysis or with chronic kidney disease who are expected to need an access. The grade is Expert Opinion.[[kdoqi_va2019]]</p>
{{fig:save_veins|Save the veins: one arm kept free of cuffs, needles, and lines, for the access the patient has or will need.}}
<h3>What you do</h3>
<p>Write an access-protection note per your unit&rsquo;s protocol, naming the access, its side, and any arm saved for a future access. Ask the ward to call the unit before any central line. Teach the patient to say, &ldquo;This is my dialysis arm.&rdquo; If a central line is needed, the route belongs to the attending nephrologist and the ward team together.</p>
{{call:Stop and call the attending nephrologist when a ward plans a PICC, a subclavian line, or venipuncture on the access arm or the future access arm, and when a patient returns from hospital with a new dry weight, a new catheter, or new antibiotics and no nephrology plan.}}
<h3>The first session after discharge</h3>
<p>The weeks after a hospital stay are fragile. The old dry weight may be wrong, new medicines may need review, and plans made on the ward may not have reached the unit.</p>
<p>Erickson and colleagues studied 26,613 United States hemodialysis patients after hospital discharge. Using an instrumental-variable method, they estimated that one additional provider visit in the month after discharge was associated with a 3.5 percentage point lower absolute probability of readmission within 30 days (95% confidence interval 1.6 to 5.3).[[erickson2014]] The method reduces confounding but does not remove it. It supports a careful first contact after discharge.</p>
{{flow:First session after hospital discharge|Get the papers::Read the discharge summary before the fluid goal is set. If it is missing, ask the family or call the hospital.|Check the medicines::List every new medicine. Check doses for kidney failure using your unit&rsquo;s references. Module 20 covers dosing.|Question the dry weight::Compare today&rsquo;s weight with the old dry weight. Module 8 covers reassessment.|Check the access::Note any new catheter, its site, and its dressing. Check the fistula for a thrill.|Screen for infection::Fever, a new wound, or a catheter site that looks red.|Check the test results::Hepatitis tests may be needed per your unit&rsquo;s protocol after a hospital stay. Module 29 covers the schedule.|Call the attending nephrologist::Report what changed. The nephrologist sets the new dry weight and medicines.}}
"""),
        ("letter", "The peri-procedure note", "Writing a peri-procedure note or clearance letter", """
<p>Teams outside the unit often ask for &ldquo;clearance for surgery.&rdquo; Fitness for an operation is a shared decision of the surgeon, the anesthesiologist, and, for a dialysis patient, the attending nephrologist. What the unit can give at once is facts. A good peri-procedure note answers the questions the other team does not know to ask, then names the questions that belong to the nephrologist.</p>
{{fig:pod28_letter}}
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>What to write</th><th>Why the other team needs it</th></tr></thead>
<tbody>
<tr><td>Identifiers</td><td>Name, age, hospital number, procedure, date, time, requesting team</td><td>Links the note to the right patient and event</td></tr>
<tr><td>Dialysis schedule</td><td>Days, last session date and end time, next planned session</td><td>Shows where the procedure falls in the gap</td></tr>
<tr><td>Fluid</td><td>Dry weight, today&rsquo;s weight, daily urine output</td><td>Guides IV fluid limits and shows whether residual function exists</td></tr>
<tr><td>Potassium</td><td>Last result with date and time</td><td>Shows the starting point before tissue injury and fasting add more</td></tr>
<tr><td>Bleeding</td><td>Heparin used in sessions, anticoagulant and antiplatelet medicines</td><td>Guides the surgical and anesthetic plan. Module 19 covers this</td></tr>
<tr><td>Access</td><td>Type and side, plus any arm saved for a future access</td><td>Keeps cuffs, needles, and lines off the access arm</td></tr>
<tr><td>Infection status</td><td>Hepatitis B, hepatitis C, and human immunodeficiency virus (HIV) results with dates</td><td>Guides isolation and equipment. Module 29 covers this</td></tr>
<tr><td>Allergies</td><td>Including contrast and heparin</td><td>Prevents a known reaction</td></tr>
<tr><td>Questions and contact</td><td>The questions for the attending nephrologist, and &ldquo;Please contact Dr. ___ (attending nephrologist) at ___ before scheduling&rdquo;</td><td>Puts the decisions in the right hands</td></tr>
</tbody></table></div>
<h3>Words to avoid</h3>
<p>Do not write &ldquo;cleared for surgery&rdquo; on your own. The words certify that the kidney-related risks are settled, and only the attending nephrologist can settle them. Write the facts, then the questions. Write instead: &ldquo;Peri-procedure dialysis plan pending review by the attending nephrologist.&rdquo;</p>
<h3>Worked example: scoring the RCRI</h3>
{{formula:<strong>Illustrative scoring, not a decision rule.</strong> Revised Cardiac Risk Index: one point each for high-risk surgery, ischemic heart disease, heart failure, cerebrovascular disease, preoperative insulin treatment, and creatinine above 2.0 mg/dL.[[lee1999]]<br>High-risk surgery: the paper defines it as intraperitoneal, intrathoracic, or suprainguinal vascular surgery. Hip repair is outside these, so 0.<br>Ischemic heart disease 0. Heart failure 0. Cerebrovascular disease 0. Insulin 0. Creatinine above 2.0 mg/dL: 1.<br>Score = 1. Major cardiac complication rate for 1 point in the validation cohort: 0.9%.[[lee1999]]<br>What it tells you: one sign of risk that the anesthesiologist will already count. What it does not tell you: his real risk. The index was derived in 1999 in elective surgery at one hospital and not in dialysis patients, whose postoperative mortality is several times higher.[[palamuthusingam2020]] It may underestimate their risk, an untested inference. A hip fracture repair is also urgent, not elective. The cardiac assessment follows the 2024 guideline and belongs to the anesthesiologist and cardiologist.[[acc_aha_periop2024]]}}
<p>Certificates, abstracts, and signatures are covered in Module 31.</p>
{{key:Write facts and questions, not clearance. The attending nephrologist and the surgical team decide fitness for the operation.}}
"""),
        ("travel", "Travel", "Travel: holidays, overseas work, and pilgrimage", """
<p>A traveling dialysis patient carries the unit along: a folder of papers, a booked chair at the other end, and a plan for the trip back. Module 12 covers receiving a visitor. This section prepares your own patient to leave.</p>
<h3>Why travel carries an infection risk</h3>
<p>Hepatitis B and C spread in dialysis units through shared surfaces, equipment, and lapses in technique. A visitor shares the host unit&rsquo;s risk.</p>
<p>Ghafur and colleagues followed patients in seven United Kingdom units who traveled to resource-limited countries. New hepatitis C infection occurred after 4 of 153 travel episodes (2.6%, 95% confidence interval 0.7% to 6.6%). Early infections were detected by hepatitis C virus ribonucleic acid (RNA) before antibody appeared, and liver enzymes could be normal.[[ghafur2007]] Bhattacharya and colleagues described 16 hepatitis C infections acquired during holiday dialysis abroad in two Birmingham units. These made up 44% of all patients with hepatitis C in those units.[[bhattacharya2009]]</p>
<p>Both studies are observational and from high-income units. No Philippine data were found, and the risk at provincial units is unknown. The direction still applies to any patient who dialyzes in an unfamiliar unit.</p>
<h3>On return</h3>
<p>Test the patient on return, per your unit&rsquo;s protocol, before the patient rejoins the general dialysis area. The Centers for Disease Control and Prevention (CDC) recommendations set routine hepatitis B and hepatitis C testing for hemodialysis patients.[[cdc2001]] Module 29 owns the testing schedule and the rules for isolation.</p>
{{fig:pod28_travelfolder}}
{{cards:Travel checklist|Booking::Written confirmation of sessions at the receiving unit, with dates and times.|Test results::Hepatitis B, hepatitis C, and HIV results with dates, within the window the receiving unit asks for.|Prescription summary::Dry weight, dialyzer, session time, dialysis fluid, heparin, and access, reviewed and signed by the attending nephrologist.|Medicine list::Generic names, doses as prescribed, and timing.|Latest results::Recent blood counts, chemistry, and adequacy results.|Contacts::The home unit&rsquo;s number and the attending nephrologist&rsquo;s contact.|Diet and fluid::Advice on heat, sweating, salty festival food, and long trips, from the dietitian or nephrologist.|Missed session plan::What to do and whom to call if a session falls through.}}
{{formula:<strong>Decision walk-through, illustrative.</strong> Mr. Ramil Garcia, 48, will spend two weeks in Samar for a fiesta.<br>1. Booking confirmed? If not, tell the nephrologist before he leaves.<br>2. Test dates within the receiving unit&rsquo;s window? Ask that unit.<br>3. Prescription summary and medicine list: drafted by you, signed by the attending nephrologist.<br>4. Contacts: home unit and nephrologist.<br>5. On return: testing per your unit&rsquo;s protocol before he rejoins the general area.[[ghafur2007]][[cdc2001]]<br>What it tells you: what he needs to dialyze safely away. What it does not tell you: the infection risk of the receiving unit.}}
<p>For overseas work or a pilgrimage such as the Hajj, no dialysis-specific evidence was found. Use the same checklist, start earlier, and refer the specifics to the attending nephrologist. The continuity planner maps sessions around travel dates, and the potassium load calculator helps you explain festival food.</p>
{{key:Before any trip, the patient needs a booked chair, dated test results, and a signed prescription summary. After the trip, the patient needs testing before rejoining the general area.}}
"""),
        ("handoff", "Talking to other doctors", "Talking to other doctors: what they need from the unit", """
<p>Surgeons, radiologists, and ward physicians rarely manage dialysis. Three facts are the ones they most often do not know, and each one changes what they do.</p>
{{cards:Three facts other teams often miss|Little or no urine::IV fluid stays in the body. A drug that needs urine to leave stays too. Ask them to count every bag.|Potassium rises fast::Between sessions, and faster still with tissue injury, transfusion, and fasting. A normal morning value can be high by the afternoon.|The access arm is off-limits::No blood pressure cuff, no needles, no IV line, no PICC on the access arm, or on the arm saved for the next access.}}
<p>Use the SBAR format from Module 1 (situation, background, assessment, recommendation). Keep it short and end with who decides.</p>
{{flow:SBAR to the orthopedic resident, illustrative|Situation::&ldquo;This is the physician on duty at the dialysis unit, calling about Mr. Ernesto Villanueva, booked for hip surgery on Monday at 7 AM.&rdquo;|Background::&ldquo;He dialyzes Monday, Wednesday, and Friday through a left forearm fistula. Today&rsquo;s session ends at 6 PM. This morning&rsquo;s potassium was 5.8. He takes clopidogrel and still passes about 300 mL of urine a day.&rdquo;|Assessment::&ldquo;Monday morning is the end of his longest gap. The CT angiogram tonight does not need an emergency session. The left arm cannot take a PICC.&rdquo;|Recommendation::&ldquo;I am calling Dr. Reyes, his attending nephrologist, now about a session before surgery and the contrast. Please plan any central line with her. I will send a written note within the hour with her number.&rdquo;}}
<p>The call promises no session and approves no operation. It gives the facts, protects the arm, and names the decision-maker.</p>
{{key:The physician on duty supplies facts and protects the access. The attending nephrologist sets the dialysis plan around the procedure.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is the problem with Monday, and what will you ask?</strong> Friday&rsquo;s session ends at about 6 PM, so Monday 7 AM falls about 61 hours later, at the end of his longest gap. His potassium is already 5.8 mmol/L on a session day, and he arrived 2.8 kg above his dry weight. In the Medicare study, a three-day interval was associated with 90-day mortality of 5.2% compared with 4.2% at one day. The differences were small and confounding is likely. You call the attending nephrologist with these facts. You ask whether to add a Sunday session, run an early Monday session, or keep the schedule with a potassium check before surgery. You mention the heparin and the clopidogrel. The nephrologist decides.</p>
<p><strong>What about contrast tonight?</strong> You tell the resident that the CT angiogram should not be delayed for dialysis. He is on maintenance dialysis, so the saline prophylaxis advice for patients not on dialysis does not apply, and no emergency session is needed for the contrast alone. He still passes about 300 mL a day, so you tell the attending nephrologist. Because he arrived above his dry weight, you also mention his fluid status.</p>
<p><strong>What do you write about the PICC and the clearance?</strong> You write that the left fistula arm must have no blood pressure cuff, needle, IV line, or PICC, and that any central line is discussed with the attending nephrologist first. You do not write &ldquo;cleared for surgery.&rdquo; Your note lists his schedule and last session, dry weight and today&rsquo;s weight, his potassium with time, his heparin and clopidogrel, his access and side, his urine output, his hepatitis and HIV status with dates, and his allergies. It closes with the questions for the nephrologist and her contact number. You sign, date, and time it.</p>
"""],
    "skills": {"title": "Writing a peri-procedure dialysis note",
               "intro": "Write a peri-procedure note for a real or simulated patient with a planned procedure, while your preceptor observes and plays the requesting surgeon.",
               "items": [
                   ("Confirms the patient&rsquo;s identity and the procedure, date, time, and requesting team.", False),
                   ("Records the dialysis schedule, the last session date and end time, and the sessions planned before the procedure.", False),
                   ("Records the dry weight, today&rsquo;s weight, the last potassium with its date, and the daily urine output.", False),
                   ("Lists the anticoagulant and antiplatelet medicines and the heparin used in sessions.", False),
                   ("Records the access type and side and writes &ldquo;no blood pressure cuff, venipuncture, IV line, or PICC on the access arm,&rdquo; naming any arm saved for a future access.", True),
                   ("Records hepatitis B, hepatitis C, and HIV status with dates.", False),
                   ("For a contrast request, records the agent type and whether the patient still makes urine.", False),
                   ("Does not write &ldquo;cleared for surgery&rdquo; without the attending nephrologist&rsquo;s review, and writes the questions for the nephrologist instead.", True),
                   ("Calls the attending nephrologist for any request to add, move, or change a session or the heparin.", True),
                   ("Gives the requesting team the nephrologist&rsquo;s contact and the unit&rsquo;s number.", False),
                   ("Gives a short SBAR report to the requesting team and names who decides.", False),
                   ("Signs, dates, and times the note.", False),
               ],
               "placement": "For one month, collect every request your unit receives from other teams about surgery, contrast, admission, or travel. For each, note what was asked, what facts were missing, and who decided. Review the list with your preceptor and draft a one-page template for your unit."},
    "quiz": [
        ("Why does a long fast before surgery raise the potassium of a dialysis patient?",
         ["Fasting increases potassium absorption from the gut",
          "Insulin falls, so less potassium is driven into cells",
          "Fasting stimulates the kidney to retain potassium",
          "Fasting lowers the potassium in dialysis fluid"], 1,
         "With little insulin during a fast, less potassium moves into cells, and no kidney removes it."),
        ("In the meta-analysis by Palamuthusingam and colleagues, what happened to the excess postoperative mortality of dialysis patients after adjustment for age and other illness?",
         ["It disappeared",
          "It reversed, favoring dialysis patients",
          "It was reduced but persisted",
          "It was not assessed"], 2,
         "Adjustment attenuated the excess, but it remained in every surgical field."),
        ("A patient on Monday-Wednesday-Friday dialysis is booked for elective surgery on Monday at 8 AM. What is the main concern about the timing?",
         ["The operation falls at the end of the longest gap, when potassium and fluid peak",
          "Monday surgery means the unit is busiest",
          "Dialysis must always be done the day after surgery",
          "The fistula cannot be used on Mondays"], 0,
         "Potassium and fluid peak after the weekend gap. The nephrologist decides on any session change."),
        ("In the Medicare study of dialysis timing before surgery, what was the 90-day mortality when the last session was 3 days before surgery, compared with 1 day?",
         ["10.8% compared with 4.0%",
          "4.0% compared with 4.5%",
          "4.7% compared with 4.2%",
          "5.2% compared with 4.2%"], 3,
         "The absolute difference was 1.0 percentage point. The study was observational, and the authors warned of residual confounding."),
        ("Using the published absolute risk difference of 1.0 percentage point, about how many procedures done 3 days rather than 1 day after dialysis go with one additional death in that association?",
         ["10", "100", "1,000", "25"], 1,
         "1 divided by 0.010 is 100. This is a number needed to harm for an association, not a proven effect of moving a session."),
        ("A surgeon asks you to add a heparin-free session tonight before a morning operation. A chair is free. What do you do?",
         ["Run the session as requested, since the chair is free",
          "Refuse, because extra sessions are never needed",
          "Run the session with the usual heparin",
          "Gather the facts and call the attending nephrologist, who decides on the session and the heparin"], 3,
         "Both are changes to the prescription. Your facts make the decision quick."),
        ("An emergency physician asks whether an anuric patient on maintenance hemodialysis needs dialysis right after a CT scan with iodinated contrast. What is the best answer?",
         ["No emergency session is needed for the contrast alone, and the scan should not be delayed",
          "Yes, within two hours of the scan",
          "Yes, but only if the patient received saline before the scan",
          "The scan should be cancelled"], 0,
         "Keep the usual schedule. Delaying a needed scan can cause more harm."),
        ("The ACR and NKF consensus statement advises IV saline prophylaxis before iodinated contrast in which group?",
         ["All patients on maintenance hemodialysis",
          "Anuric patients only",
          "Patients with acute kidney injury or eGFR below 30 who are not on maintenance dialysis",
          "No patients at all"], 2,
         "The advice is for patients not on dialysis. It is a consensus statement, not a graded recommendation."),
        ("A woman on dialysis still passes about 500 mL of urine a day and is scheduled for a contrast CT. What should the physician on duty do?",
         ["Cancel the CT",
          "Tell the attending nephrologist, who weighs the scan against her residual function",
          "Order an extra session after the scan",
          "Give IV saline before the scan"], 1,
         "Pooled data show no significant loss, from small studies. The nephrologist weighs it."),
        ("What does the 2021 ACR and NKF statement say about dialysis after a group II gadolinium-based agent?",
         ["Dialysis must start within 24 hours",
          "Two extra sessions are needed",
          "Group II agents are contraindicated in dialysis patients",
          "Starting or changing dialysis is likely unnecessary"], 3,
         "Zero NSF cases were found after 4,931 doses in patients with eGFR below 30. It is a consensus statement."),
        ("A ward team plans a PICC in the right arm of a patient whose left arm fistula works and whose right arm was mapped for a future access. What do you do?",
         ["Agree, since the fistula is in the other arm",
          "Ask them to place it in the left arm instead",
          "Ask them to hold and discuss the route with the attending nephrologist, and write an access-protection note",
          "Remove any PICC that is placed"], 2,
         "A prior PICC is associated with lack of a working fistula. KDOQI considers vein preservation reasonable (Expert Opinion)."),
        ("In the case-control study by El Ters and colleagues, what was the adjusted association between a prior PICC and lack of a working fistula?",
         ["OR 2.8, an association that cannot prove cause",
          "OR 0.5, showing protection",
          "No association",
          "A randomized effect showing that PICCs cause fistula failure"], 0,
         "The adjusted odds ratio was 2.8 (1.5 to 5.5). The study was retrospective and observational."),
        ("An orthopedic resident asks you to write &ldquo;cleared for surgery&rdquo; for a dialysis patient. What is the best response?",
         ["Write it, since the patient dialyzed today",
          "Write a facts-only peri-procedure note with the questions for the attending nephrologist and the nephrologist&rsquo;s contact",
          "Refuse to write anything",
          "Write it and add the RCRI score"], 1,
         "The surgical team and the nephrologist decide fitness. You supply the facts."),
        ("A patient returns from two weeks of dialysis in a unit abroad with weak infection control. What does the evidence from United Kingdom units suggest?",
         ["Testing is unnecessary if liver enzymes are normal",
          "Only antibody testing is useful",
          "Travel carries no measurable risk",
          "New hepatitis C infection can occur, and early infection may show RNA before antibody"], 3,
         "In one study, 4 of 153 travel episodes led to new hepatitis C. Test per your unit&rsquo;s protocol."),
        ("A woman comes for her first session after a week in hospital. She weighs 3 kg less than her old dry weight and has new medicines but no discharge summary. What comes first?",
         ["Use the old dry weight as today&rsquo;s fluid goal",
          "Set a new dry weight yourself at today&rsquo;s weight",
          "Obtain the discharge information and call the attending nephrologist before the fluid goal is set",
          "Send her home without dialysis"], 2,
         "The nephrologist sets the dry weight and medicines. You bring the facts."),
    ],
    "terms": [("Peri-procedure period", "The time immediately before, during, and after an operation or invasive test."),
              ("Dialysis-to-surgery interval", "The time between the end of the last dialysis session and the start of a procedure."),
              ("Residual kidney function", "The filtration the patient&rsquo;s own kidneys still perform, usually seen as daily urine output."),
              ("Revised Cardiac Risk Index", "A six-item score that estimates the risk of major cardiac complications after noncardiac surgery."),
              ("Nephrogenic systemic fibrosis", "A thickening of the skin and organs linked to older gadolinium agents in advanced kidney failure."),
              ("Peripherally inserted central catheter", "A long catheter placed through an arm vein with its tip in a large central vein."),
              ("Vein preservation", "Protecting arm veins from needles, cuffs, and catheters so they remain usable for an access."),
              ("Residual confounding", "Bias that remains after adjustment, because some differences between groups were not measured."),
              ("Number needed to harm", "The number of patients exposed to a factor for one additional bad outcome, calculated as 1 divided by the absolute risk difference.")],
    "readings": [("contrast-nephropathy.html", "Contrast and the kidney, for patients and families who ask about scans."),
                 ("travel-dialysis-ckd.html", "Planning travel with kidney disease and dialysis."),
                 ("hemodialysis-transfer-guide.html", "What moving between units involves, from the patient&rsquo;s side.")],
    "calcs": ["calc-dialysis-continuity-planner.html", "calc-idwg-fluid.html", "calc-potassium-load.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
