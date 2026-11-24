# -*- coding: utf-8 -*-
"""Physician on Duty, Module 12: First Sessions and Unusual Sessions.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty reviewing referral papers with a nurse beside a new dialysis patient with a fresh neck catheter dressing.",
    "objectives": [
        "Explain why the first sessions are short and gentle, using the physics of urea removal and the high death rate of new dialysis patients.",
        "Explain how dialysis disequilibrium develops, name who is at risk, and recognize its early signs at the chair.",
        "Apply different goals and cautions to a patient with acute kidney injury on outpatient dialysis, whose aim is recovery.",
        "Receive a visiting or newly transferred patient safely by verifying identity, order, access, serology, and records before the first connection.",
        "Explain what isolated ultrafiltration removes and what it leaves behind, and when the attending nephrologist may choose it.",
    ],
    "big": """
{{plain:Think of the first long drive in a new car. You do not know how it brakes, how it corners, or how the engine behaves on a hill. So you drive slowly at first and learn its handling before you go faster. A first dialysis session is driven the same way.}}
<p>The picture has a limit. A new car is the same car on day one and day thirty. A new dialysis patient is not. The body has adapted to weeks of high urea and acid, and dialysis changes that chemistry within hours. The risk lies in the speed of change, so the first sessions are deliberately less efficient.</p>
{{cards:Key terms for this module|First-ever session::The first hemodialysis treatment of a patient&rsquo;s life, usually through a new catheter.|Dialysis disequilibrium syndrome (DDS)::Brain swelling and neurologic symptoms during or soon after dialysis, caused by a fast fall in plasma urea and other solutes.|Osmolality::The concentration of dissolved particles in a fluid. Water moves toward the side with more particles.|Urea reduction ratio (URR)::The percentage fall in blood urea during one session.|Acute kidney injury (AKI)::A sudden loss of kidney function over hours to days, which may recover.|Transient patient::A patient who dialyzes in your unit for a short time while away from the home unit.|Isolated ultrafiltration (isolated UF)::Removal of plasma water by pressure alone, with no dialysis fluid flowing.}}
<p>Most sessions are routine because the patient, the access, and the order have been tested many times. A few sessions remove that safety margin: a first dialysis, a patient still recovering from acute kidney injury, a visitor from another unit, and a session that removes only water. Your work is to recognize these sessions before connection, to check the order as if you had to defend each line, and to call the attending nephrologist early.</p>
""",
    "case": {"title": "New patient, urea of 250", "html": """
<p>Wednesday, 1:00 p.m. Mrs. Erlinda &ldquo;Linda&rdquo; Bautista, 64, arrives from a provincial hospital after three weeks of vomiting and poor appetite. She has never seen a nephrologist. A non-tunneled catheter was placed in her right internal jugular vein this morning. The nurse, Mr. Paolo Cruz, shows you a handwritten order relayed by phone: &ldquo;HD 4 hours, blood flow as tolerated, UF 2 L.&rdquo;</p>
<p>Her results from this morning: blood urea nitrogen (BUN) 250 mg/dL, creatinine 15.8 mg/dL, sodium 132 mmol/L, potassium 5.9 mmol/L, bicarbonate 12 mmol/L, and glucose 110 mg/dL. Her blood pressure is 172/96 mm Hg, pulse 96 per minute, and oxygen saturation 96%. She weighs 52 kilograms. She is drowsy but answers questions, and she has asterixis, a flapping tremor of the outstretched hands. Her hepatitis B and C results are &ldquo;pending.&rdquo; All values are illustrative.</p>
""", "questions": ["How high is her risk of disequilibrium, and why?",
                  "What in the order and the unit protocol must you check before connection, and what do you tell the attending nephrologist?",
                  "Where does she dialyze today while her serology is pending?"]},
    "sections": [
        ("firstweek", "First sessions", "Why the first sessions are different", """
<p>A maintenance patient brings a known body to the chair. The access has been used many times. The dry weight has been tested. A new patient brings none of this.</p>
<h3>What the new patient brings</h3>
<p>The new patient usually arrives with the highest urea of their dialysis life, because the kidneys have failed slowly and no one has cleared the waste. Acid has built up for the same reason, so the bicarbonate is often low. The access is often a catheter placed hours earlier. The response of the blood pressure to fluid removal is unknown. Many new patients still make urine, and that leftover function protects them. Module 3 explained why. In a large cohort of patients starting hemodialysis, a faster loss of this residual kidney function was associated with higher mortality.[[obi2016]] The study was observational, so sicker patients may have lost function faster for other reasons.</p>
<h3>The first months carry the highest risk</h3>
<p>Robinson and colleagues followed 86,886 patients in 11 countries in the Dialysis Outcomes and Practice Patterns Study (DOPPS). In the first 120 days of hemodialysis, there were 26.7 deaths per 100 patient-years. From day 121 to day 365 there were 16.9, and after the first year there were 13.7. In every country, mortality was higher in the early period than in the intermediate period.[[robinson2014]]</p>
<p>This is an observational finding. Part of the early excess reflects the patients themselves: many start dialysis unplanned, sick, and through a catheter. The study does not show that gentler first sessions lower this death rate. It does show that the transition period deserves your closest attention.</p>
<h3>What you do</h3>
<p>Treat every first-ever session as a session in which you call the attending nephrologist before connection. Confirm that the order was written for a first session, as Module 7 describes. Confirm that the access is usable (Modules 9 and 10). Confirm the serology plan (section 5). Module 11 gave you the safe-to-start assessment; for a new patient, add a baseline neurologic check.</p>
{{flow:The first three sessions, stepwise|Check the order::Confirm the attending nephrologist wrote or approved it for a first session. Every setting is per the attending&rsquo;s order.|Gentle first session::Shorter and less efficient than a maintenance session, as the attending prescribes. Watch for headache, nausea, and restlessness.|Reassess::Before the next session, review symptoms, pressure, weight, urine output, and the post-dialysis results.|Step up::The attending nephrologist raises time, blood flow, or dialyzer size over the following sessions, toward the maintenance prescription.}}
{{key:A first session is never routine. Read the order as if you had to defend each line.}}
"""),
        ("dds", "Disequilibrium", "Dialysis disequilibrium: what happens in the brain", """
<p>Picture two rooms joined by a narrow door. The blood is one room, and the dialyzer drains its dissolved particles quickly. The brain is the other room, and its particles can leave only through the narrow door. For a while, the brain room holds more particles than the blood room. Water moves toward the side with more particles, so water moves into the brain.</p>
{{fig:pod12_tworooms}}
<p>The picture has a limit. Urea is not the only actor, and the door is not the only reason the brain lags. Researchers have proposed three mechanisms, and they may act together.</p>
<h3>Normal physiology first</h3>
<p>Osmolality is the concentration of dissolved particles in a fluid. Water crosses cell membranes freely and moves toward the side with higher osmolality. Sodium and glucose stay mostly outside cells, so they pull water strongly. Urea crosses most cell membranes, so in a steady state it is an &ldquo;ineffective&rdquo; osmole: it is equal on both sides and pulls no water.[[hall2021]] Urea becomes effective when its plasma level falls faster than it can leave the cells. Brain cells, behind the blood-brain barrier, are the slowest to equalize.</p>
<h3>What breaks: three proposed mechanisms</h3>
{{cards:Three proposed mechanisms|Reverse urea effect::Dialysis removes urea from the blood faster than from the brain. The brain is left relatively hyperosmolar, and water enters it.|Idiogenic osmoles::Brain cells adapt to a long hyperosmolar state by making their own particles. These do not leave quickly when plasma osmolality falls, so they hold water in the brain.|Brain acidosis::Fast correction of systemic acidosis may lower the pH of the cerebrospinal fluid, which may add to brain swelling.}}
<p>Sahani and colleagues described all three.[[sahani2001]] Silver, Sterns, and Halperin critically reviewed the experimental work. They concluded that the reverse urea hypothesis remains a viable explanation, and that rapid reduction of a high urea level by itself predisposes to the condition.[[silver1996]] A high starting urea, removed quickly, leaves the brain relatively hyperosmolar. Water enters, the brain swells, and the pressure inside the skull rises. Symptoms follow, from headache to seizures.[[patel2008]][[zepedaorozco2012]]</p>
{{formula:<strong>Worked example A: urea&rsquo;s share of osmolality (illustrative numbers).</strong><br>Calculated osmolality (mOsm/kg) = 2 &times; sodium + glucose &divide; 18 + BUN &divide; 2.8, with glucose and BUN in mg/dL.[[hall2021]]<br>Linda, before dialysis: 2 &times; 132 + 110 &divide; 18 + 250 &divide; 2.8 = 264 + 6.1 + 89.3 = 359.4 mOsm/kg. Urea contributes 89.3.<br>If one session achieved a URR of 65%: post-BUN = 250 &times; 0.35 = 87.5 mg/dL. Urea now contributes 87.5 &divide; 2.8 = 31.3. The urea share falls by 58.0 mOsm/kg.<br>If the session achieved a URR of 30%: post-BUN = 250 &times; 0.70 = 175 mg/dL. Urea contributes 62.5. The urea share falls by 26.8 mOsm/kg.<br>What it tells you: the osmotic shift grows with the starting urea and with the fraction removed in one session. What it does not tell you: no validated &ldquo;safe&rdquo; fall exists, and sodium and glucose also change during dialysis. The target URR for a first session is the attending nephrologist&rsquo;s decision.}}
<p>The site&rsquo;s osmolal gap calculator uses the same three terms.</p>
<div class="table-wrap"><table>
<thead><tr><th>Illustrative scenario for Linda</th><th>BUN (mg/dL)</th><th>Urea share (mOsm/kg)</th><th>Calculated osmolality, sodium and glucose held constant</th></tr></thead>
<tbody>
<tr><td>Before dialysis</td><td>250</td><td>89.3</td><td>359.4</td></tr>
<tr><td>After a session with a URR of 30%</td><td>175</td><td>62.5</td><td>332.6</td></tr>
<tr><td>After a session with a URR of 65%</td><td>87.5</td><td>31.3</td><td>301.4</td></tr>
</tbody></table></div>
<h3>Who is at risk</h3>
<p>Risk is highest in a first-ever session, with a very high pre-dialysis urea, with severe acidosis, in a patient returning after several missed sessions, and in a patient with existing brain disease such as a recent stroke, head injury, or seizure disorder. It is also described in AKI and with continuous therapies.[[mistry2019]][[raina2022]][[patel2008]] These risk factors come from reviews and case reports, not from studies that measured risk.</p>
<h3>What the evidence can and cannot tell you</h3>
<p>Mistry described the condition as a diagnosis of exclusion that is uncommon and becoming rarer. Because it is rare, randomized trials of prevention are almost impossible.[[mistry2019]] Raina and colleagues reviewed 49 reports with 321 patients, with a pediatric focus. Among 226 patients with the syndrome, nausea occurred in 25.2%, headache in 24.8%, vomiting in 23.9%, muscle cramps in 18.1%, reduced consciousness in 8.8%, confusion in 4.4%, and seizure in 4.9%. Reports clustered in the early dialysis era.[[raina2022]] These are case series. They describe what the syndrome looks like, not how often it occurs or which prevention works best.</p>
{{key:Disequilibrium is caused by cleaning too much too fast in a body that has adapted to high urea. The prevention is in the prescription.}}
"""),
        ("prevent", "Prevent and recognize", "Preventing and recognizing disequilibrium at the chair", """
<p>Think of lowering a heavy load with a rope. If you let go, it falls hard. If you lower it in stages, it lands safely. The first sessions lower the urea in stages.</p>
<h3>Prevention belongs to the order</h3>
<p>The attending nephrologist prevents disequilibrium through the prescription. The usual approach lowers the efficiency of the first sessions and adds sessions instead. Sahani and colleagues described shortening the first run to 25% to 30% of a normal session, lowering the blood flow or the dialysis fluid flow, or using a less efficient dialyzer, with dialysis frequency increased instead. A second strategy raises plasma osmolality by adding solutes to the blood.[[sahani2001]] These are strategies described in a review, not tested targets. Any number for your patient is the attending nephrologist&rsquo;s to set.</p>
<p>Your part is to check that the order fits the patient. An order that would suit a stable maintenance patient, such as four hours with blood flow &ldquo;as tolerated,&rdquo; does not fit a first session with a BUN of 250. When the order and the patient do not match, you do not change the order. You call.</p>
{{formula:<strong>Worked example B: reading the first-session URR (illustrative numbers).</strong><br>URR (%) = (pre-BUN &minus; post-BUN) &divide; pre-BUN &times; 100.[[kdoqi_hd2015]]<br>Pre-BUN 250 mg/dL, post-BUN 180 mg/dL: (250 &minus; 180) &divide; 250 &times; 100 = 70 &divide; 250 &times; 100 = 28%.<br>What it tells you: the first session lowered urea by about a quarter, which is often what the attending intended. What it does not tell you: that the dose is inadequate. A low URR is expected in a deliberately gentle first session, and the maintenance targets in Module 7 do not apply to it. The site&rsquo;s Kt/V calculator computes the same ratio.}}
<h3>Recognition</h3>
<p>Early signs are headache, nausea, vomiting, restlessness, blurred vision, and muscle cramps. Late signs are confusion, seizures, and reduced consciousness.[[patel2008]][[zepedaorozco2012]] Symptoms can begin during the session or shortly after it. Zepeda-Orozco and Quigley noted that treatment once the syndrome is established is rarely successful, so early recognition matters most.[[zepedaorozco2012]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you see</th><th>What else looks like this (module)</th></tr></thead>
<tbody>
<tr><td>Early</td><td>Headache, nausea, vomiting, restlessness, blurred vision, cramps</td><td>Low blood pressure (Module 13). Dialyzer reaction (Module 16). Cramps from fluid removal (Module 24)</td></tr>
<tr><td>Late</td><td>Confusion, drowsiness, seizure, reduced consciousness</td><td>Low blood sugar (Module 18). Stroke or subdural bleeding (Module 18). Hypertensive emergency (Module 14)</td></tr>
<tr><td>Timing clue</td><td>Onset in a first session or after missed sessions, often in the later part of the run or soon after</td><td>A dialyzer reaction usually starts in the first minutes. A low pressure follows fluid removal</td></tr>
</tbody></table></div>
<p>Disequilibrium is a diagnosis of exclusion.[[mistry2019]] A headache in a new patient may also come from high pressure, low sugar, or bleeding inside the skull, which matters more in a patient who received heparin. Your first job is to rule out the causes you can check in minutes.</p>
{{fig:pod12_newsymptoms}}
<h3>What you do</h3>
{{flow:New symptoms in a new patient|Go to the chair::Look at the patient. Check that the patient responds, breathes comfortably, and has a pulse.|Slow or stop::Ask the nurse to slow or stop the treatment as your unit&rsquo;s protocol allows.|Check the quick causes::Blood glucose, blood pressure, pulse, and a brief neurologic examination: orientation, pupils, limb movement, speech.|Protect the patient::Turn a vomiting patient to the side. Keep the chair low and the side rails up. Seizure care follows Module 18.|Call::Call the attending nephrologist at once. Report the time into the session, the blood flow, the symptoms, and your findings.|Record::Write the time of onset, the findings, each step, and the advice received.}}
<p>Hemodialysis emergency reviews describe the same sequence: recognize early, slow or stop, exclude other causes, and treat seizures if they occur.[[saha2017]][[greenberg2021]] The evidence for each step rests on mechanism and case experience, not on trials.</p>
{{call:Stop and call the attending nephrologist when headache, vomiting, restlessness, blurred vision, or confusion appears in a new patient or in one returning after missed sessions. Slow or stop the treatment per your unit&rsquo;s protocol while you call.}}
{{key:In a new patient, a headache is disequilibrium until you have checked the pressure, the sugar, and the nervous system and called the attending.}}
"""),
        ("aki", "The AKI patient", "The patient with acute kidney injury: a different goal", """
<p>A cast on a broken leg is not meant to stay. You put it on so the bone can heal, and you check each week whether it can come off. Dialysis for acute kidney injury (AKI) works the same way.</p>
{{fig:pod12_akicast}}
<p>The picture has a limit. A bone heals on a predictable schedule, and a kidney does not. Some kidneys recover in two weeks, some in three months, and some never. The only way to know is to measure.</p>
<h3>Physiology: what can deepen the injury</h3>
<p>An injured kidney may recover over weeks as its tubular cells regenerate. During that time it is sensitive to low blood flow. A fall in blood pressure during dialysis reduces kidney perfusion and may set recovery back. Nephrotoxic medicines, such as nonsteroidal anti-inflammatory drugs and aminoglycosides, and iodinated contrast add further injury. Removing too much fluid has the same effect.</p>
<h3>Evidence: how many recover, and when</h3>
<p>Jordan and colleagues followed 111 patients discharged on outpatient hemodialysis after AKI. Forty-five (41%) recovered. Of those who recovered, 55.5% did so within 30 days of discharge, 35.5% between 30 and 60 days, and 9% between 60 and 90 days. Forty-nine (44%) progressed to kidney failure, and 17 (15%) died or went to hospice.[[jordan2021]] Gautam and colleagues studied 119 patients: 42.0% became dialysis independent, 48.7% were declared to have kidney failure, and 9.2% died. Heart failure, worse baseline kidney function, and a recent earlier episode of AKI predicted outcome.[[gautam2015]]</p>
<p>Both studies were single-center and observational, and both selected patients well enough to leave the hospital. Their recovery rates cannot be applied directly to your unit. A 2024 review concluded that about one third of such patients survive and recover enough to stop dialysis, and that data to guide dialysis management for recovery are lacking.[[babroudi2024]]</p>
<p>One small quality-improvement study tested a structured protocol in 9 patients, with weekly recovery assessment and individualized dose and ultrafiltration rate. Adherence to the protocol was 53.8%, and adherence was associated with fewer episodes of intradialytic hypotension. Three of the nine patients were free of dialysis within 90 days.[[ortizsoriano2023]] The study shows feasibility. It does not show that the protocol improves recovery.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Patient with AKI</th><th>Maintenance patient</th></tr></thead>
<tbody>
<tr><td>Goal</td><td>Support the patient until the kidney recovers, then stop</td><td>Long-term replacement of kidney function</td></tr>
<tr><td>Fluid removal</td><td>Gentle. Avoid low pressure, which may deepen the injury</td><td>Reach the dry weight within a safe rate (Module 8)</td></tr>
<tr><td>Urine output</td><td>Recorded every session. A rise is news to report</td><td>Recorded where residual function is followed</td></tr>
<tr><td>Laboratory tests between sessions</td><td>Pre-dialysis creatinine and urea trends, and any timed urine the attending orders</td><td>Monthly routine tests per protocol</td></tr>
<tr><td>Medicines</td><td>No nephrotoxin or contrast without the attending&rsquo;s approval</td><td>Dosed for kidney failure (Module 20)</td></tr>
<tr><td>Review</td><td>The attending nephrologist reviews recovery at a set interval, often weekly</td><td>Routine monthly review</td></tr>
</tbody></table></div>
<h3>What you do</h3>
<p>Confirm that the order labels the patient as AKI. Record urine output and weight at every session. Follow the attending&rsquo;s plan for avoiding low pressure. Do not give or approve any nephrotoxic medicine without the attending&rsquo;s agreement. Watch for the signs of recovery: rising urine output, and a pre-dialysis creatinine or urea that no longer rises as expected between sessions. Report them the same day. The attending nephrologist decides whether to hold a session, repeat laboratory tests, or order a timed urine collection. The site&rsquo;s urine output and fluid balance calculator helps you keep the trend in one place.</p>
{{formula:<strong>Worked example C: the recovery watch (illustrative numbers).</strong><br>Mr. Danilo Reyes had AKI after severe leptospirosis and is in week 3 of outpatient dialysis. His urine output rises from 200 to 900 mL per day over two weeks. His pre-dialysis creatinine stops rising between sessions.<br>Sequence: you record the trend, report it to the attending nephrologist, and the attending decides whether to hold a session and repeat tests or to collect a timed urine.<br>Timed creatinine clearance (mL/min) = urine creatinine &times; urine volume (mL) &divide; (plasma creatinine &times; collection time in minutes).[[hall2021]]<br>Illustration: urine creatinine 40 mg/dL, volume 900 mL over 24 hours (1,440 minutes), plasma creatinine 5.0 mg/dL. Clearance = 40 &times; 900 &divide; (5.0 &times; 1,440) = 36,000 &divide; 7,200 = 5.0 mL/min.<br>What it tells you: the kidney is clearing some creatinine, and the trend matters more than one value. What it does not tell you: an incomplete collection underestimates clearance, creatinine clearance overestimates true filtration, and plasma creatinine is not stable between sessions. The decision to stop dialysis is the attending nephrologist&rsquo;s.}}
{{key:For a patient with AKI, every session asks one question: is the kidney coming back? Protect it, and measure it.}}
"""),
        ("visitor", "The visiting patient", "The transient or newly transferred patient", """
<p>A relief pilot who takes over a plane in mid-flight reads the log before touching the controls. Another unit set the prescription, knows the access, and has the records. You take over with only what the patient carries.</p>
<h3>What can go wrong</h3>
<p>Five errors recur. The prescription is transcribed wrongly. The access is unfamiliar, so needles go in the wrong place or the catheter&rsquo;s lumens are reversed. A patient with unknown hepatitis status is placed at a general station. The visiting unit used a different dialyzer or dialysis fluid concentrate. An allergy or a code status decision is missing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Document</th><th>Why you need it</th></tr></thead>
<tbody>
<tr><td>Current dialysis order with dry weight</td><td>The starting point for the local order the attending nephrologist writes</td></tr>
<tr><td>The last several session records</td><td>Usual pressures, weight gains, problems during sessions, and the blood flow actually achieved</td></tr>
<tr><td>Access type, cannulation map, and recent problems</td><td>Where to needle, which direction, and what to avoid (Modules 9 and 10)</td></tr>
<tr><td>Recent laboratory results</td><td>Potassium, hemoglobin, and urea for safety and comparison</td></tr>
<tr><td>Hepatitis B surface antigen, hepatitis B surface antibody, and hepatitis C antibody, with dates</td><td>Station and machine assignment by your unit&rsquo;s protocol</td></tr>
<tr><td>Medication list and allergies</td><td>Heparin allergy or intolerance, and medicines given during dialysis</td></tr>
<tr><td>Vaccination record</td><td>Hepatitis B immunity status</td></tr>
<tr><td>Advance directives and code status</td><td>What to do if the patient arrests in your unit</td></tr>
<tr><td>Referring nephrologist&rsquo;s contact details</td><td>For questions before and after the session</td></tr>
</tbody></table></div>
{{fig:pod12_intakeform}}
<h3>Serology and isolation</h3>
<p>Hepatitis B spreads easily in dialysis units through blood on surfaces and equipment. The Centers for Disease Control and Prevention (CDC) recommends that patients who carry hepatitis B surface antigen dialyze in a separate room with dedicated machines, equipment, and supplies, that staff caring for them not care for susceptible patients at the same time, and that every patient&rsquo;s status be known on admission.[[cdc2001]] Hepatitis C testing and the Kidney Disease: Improving Global Outcomes (KDIGO) position on isolation are covered in Module 29.[[gordon2019]] Here the rule is plain. If a result is missing, unknown, or older than your unit accepts, follow your unit&rsquo;s protocol for unknown status until results are verified.</p>
<h3>What you do</h3>
{{flow:Accepting a visitor or transfer, in order|Identity::Confirm two identifiers and match them to every document.|Documents::Go through the intake list. Mark each item verified, missing, or out of date.|Serology::Place the patient by verified status, or by the unit&rsquo;s rule for unknown status.|Local order::Ask the attending nephrologist to write or approve an order for your unit. The visiting order is information, not an instruction to your staff.|Access::Examine the fistula, graft, or catheter yourself before the first needle or connection.|Baseline::Record weight, pressure, and the safe-to-start assessment from Module 11.|Connect::Start only when the order, the station, and the access are all confirmed.}}
{{formula:<strong>Worked example D: the visitor intake sort (decision walk-through, illustrative).</strong><br>Mrs. Tess Villanueva, a balikbayan visiting from abroad, brings an order printed by her home unit, a left arm fistula, and hepatitis B and C results dated seven months ago.<br>Verified: identity on two identifiers. The fistula, after your examination finds a good thrill and a mature vessel.<br>Needs the attending nephrologist: the printed order, which must become a local order. Her dry weight, which you compare with today&rsquo;s weight and examination. Any setting your unit cannot match.<br>Unit protocol for unknown status: her serology, if seven months is older than your unit accepts. She dialyzes where your protocol places patients with unverified status, and fresh samples are drawn as the protocol directs.<br>Before needling: a local order exists, the station is assigned, and the fistula is examined.<br>What the sort tells you: what blocks the first connection. What it does not tell you: whether her home prescription is right for her today. That judgment is the attending&rsquo;s.}}
<p>Module 28 covers the documents a patient carries out when traveling, and Module 29 covers serology schedules.</p>
{{call:Stop and call the attending nephrologist before connection when a visiting or transferred patient has no written order, no dry weight, or no verified serology. Do not connect on a referring unit&rsquo;s order alone unless your unit&rsquo;s protocol explicitly allows it.}}
{{key:A visitor&rsquo;s first session in your unit is a first session for your staff. Read the log before you fly.}}
"""),
        ("isouf", "Isolated UF", "Isolated ultrafiltration: removing water without dialysis", """
<p>Wringing a towel removes water without washing it. The water comes out, but the dirt stays. Isolated ultrafiltration does the same to the blood.</p>
{{fig:pod12_isouf}}
<p>The picture has a limit. The water that leaves the blood is not pure. It carries the small solutes dissolved in plasma at about their plasma concentration. So some sodium, urea, and potassium do leave, but only in proportion to the small volume of fluid removed.</p>
<h3>Physiology</h3>
<p>Module 5 explained diffusion and ultrafiltration. In ordinary hemodialysis both happen together. Dialysis fluid flows past the membrane and pulls solutes out by diffusion, while pressure pushes water out. In isolated ultrafiltration, the dialysis fluid flow is turned off. Pressure alone pushes plasma water across the membrane, a form of convection without diffusion.[[daugirdas2015]]</p>
<p>The fluid removed has roughly the composition of plasma water. Sodium leaves with the water, so salt and water are removed together. Urea, potassium, and acid are cleared only in proportion to the volume removed, which is small compared with what diffusion clears in a full session.</p>
<p>Blood pressure often holds better. During diffusive dialysis, urea leaves the plasma quickly and plasma osmolality falls. Water then tends to move from the blood into the cells, and refilling of the blood from the tissues slows. In isolated ultrafiltration, plasma osmolality changes little, so refilling and vessel tone are better preserved.[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What happens to</th><th>Isolated ultrafiltration</th><th>Standard hemodialysis</th></tr></thead>
<tbody>
<tr><td>Water</td><td>Removed by pressure</td><td>Removed by pressure</td></tr>
<tr><td>Sodium</td><td>Removed with the water</td><td>Removed with the water, and adjusted toward the dialysis fluid level by diffusion</td></tr>
<tr><td>Urea</td><td>Very little removed</td><td>Removed by diffusion</td></tr>
<tr><td>Potassium</td><td>Very little removed</td><td>Removed by diffusion</td></tr>
<tr><td>Acid</td><td>Not corrected</td><td>Corrected by bicarbonate from the dialysis fluid</td></tr>
<tr><td>Plasma osmolality</td><td>Little change</td><td>Falls as urea is removed</td></tr>
</tbody></table></div>
<h3>When the attending nephrologist may choose it</h3>
<p>The attending may choose isolated ultrafiltration for severe fluid overload when a large removal is needed. It may also be chosen for overload in a patient at risk of disequilibrium, because it removes water without a fast fall in urea. A patient whose pressure falls during sessions may tolerate a sequence of isolated ultrafiltration followed by diffusive dialysis.[[daugirdas2015]]</p>
<p>Three cautions apply. It does not treat high potassium or correct acidosis. The ultrafiltration rate still matters, and fast removal can still drop the pressure (Module 8). Its advantages rest on physiology and textbook practice; this search found no randomized trials of patient outcomes.</p>
{{key:Isolated ultrafiltration removes water and salt, not potassium or acid. When potassium is high, confirm with the attending that diffusive dialysis will follow.}}
"""),
    ],
    "debrief": ["""
<p><strong>How high is her risk of disequilibrium, and why?</strong> High. This is her first-ever session. Her BUN of 250 mg/dL means that urea alone contributes about 89 mOsm/kg to her plasma osmolality, as worked example A shows. Her bicarbonate of 12 mmol/L adds the risk of fast acid correction. She is already drowsy with asterixis, so her brain is affected before dialysis begins, and a new change will be harder to notice. A four-hour session at full blood flow could remove more than half of her urea in one afternoon. That is the pattern that produces disequilibrium.</p>
<p><strong>What must you check, and what do you tell the attending nephrologist?</strong> The order was relayed by phone and is handwritten. Confirm that the attending nephrologist wrote or approved it and that it is meant as a first-session order. Four hours with blood flow &ldquo;as tolerated&rdquo; reads like a maintenance order. The fluid goal also needs a second look. She has vomited for three weeks and may be short of volume, although her pressure is high; Module 8 covers how you judge this at the bedside. Confirm that the catheter position was checked per protocol. Note her potassium of 5.9 and her glucose. Record her baseline orientation and asterixis. Then call. In SBAR form (situation, background, assessment, recommendation), tell the attending: a new patient with a BUN of 250, bicarbonate of 12, drowsiness, and asterixis; an order that reads as a full maintenance session; a fluid goal that may not fit a patient who has been vomiting; and pending serology. Ask for a written first-session order, and repeat back what you receive.</p>
<p><strong>Where does she dialyze today?</strong> Her hepatitis B and C results are pending, so her status is unknown. She dialyzes where your unit&rsquo;s protocol places patients with unknown status, on the machine and station that protocol assigns, until verified results arrive.[[cdc2001]] Make sure samples have been drawn per protocol. Module 29 covers serology schedules.</p>
"""],
    "skills": {"title": "New-patient and visiting-patient intake review",
               "intro": "Perform this intake review on a real new or visiting patient, or on a prepared mock chart, while your preceptor observes.",
               "items": [
                   ("Confirms identity with two identifiers and matches them to every document.", False),
                   ("Confirms that the order is written or approved by the attending nephrologist for this unit, and states whether it is a first-session order.", True),
                   ("Reviews the latest urea, potassium, bicarbonate, sodium, and glucose, and names the disequilibrium risk factors present.", True),
                   ("Confirms serology results and their dates, and applies the unit protocol for unknown status if any result is missing or out of date.", True),
                   ("Examines the access and confirms it is cleared for use: catheter position confirmed per protocol, or fistula maturity documented.", False),
                   ("Records the baseline neurologic status, including orientation, headache, and asterixis, before connection.", False),
                   ("Calculates the fluid goal and the ultrafiltration rate as Module 8 teaches.", False),
                   ("Confirms allergies, the medication list, and code status.", False),
                   ("Briefs the nurse on the early signs of disequilibrium to report at once.", False),
                   ("Calls the attending nephrologist before connection for every first-ever session and documents the call.", True),
               ],
               "placement": "Over your next month of shifts, complete this review for at least two new or visiting patients. For each, write down the disequilibrium risk factors you found and what the attending nephrologist changed in the order. Review both with your preceptor."},
    "quiz": [
        ("Why is a first-ever hemodialysis session usually shorter and less efficient than a maintenance session?",
         ["The new catheter cannot carry a normal blood flow",
          "A fast fall in a very high urea can swell the brain",
          "New patients do not need much clearance",
          "Dialyzers are less efficient the first time they are used"], 1,
         "The brain has adapted to a high urea. Lowering it fast creates an osmotic gradient into the brain."),
        ("In the DOPPS analysis of 86,886 patients, what was the pattern of mortality after starting hemodialysis?",
         ["Mortality was highest in the first 120 days",
          "Mortality was lowest in the first 120 days",
          "Mortality was constant over time",
          "Mortality was high early only in the United States"], 0,
         "Early mortality exceeded intermediate mortality in every country studied. The study was observational."),
        ("Why does urea pull little water across cell membranes in a steady state, but more during fast dialysis?",
         ["Urea is too large to cross membranes",
          "Dialysis converts urea into sodium",
          "Urea crosses membranes, so it is equal on both sides until its plasma level falls faster than it can leave the cells",
          "Urea binds water inside the brain"], 2,
         "Urea is an ineffective osmole at equilibrium. It becomes effective when plasma urea falls faster than brain urea."),
        ("Using calculated osmolality = 2 &times; sodium + glucose &divide; 18 + BUN &divide; 2.8, what does a BUN of 140 mg/dL contribute?",
         ["14 mOsm/kg",
          "28 mOsm/kg",
          "70 mOsm/kg",
          "50 mOsm/kg"], 3,
         "140 &divide; 2.8 = 50. The urea share is large when the BUN is high."),
        ("Which statement about the mechanism of dialysis disequilibrium is best supported?",
         ["It is caused only by idiogenic osmoles",
          "The reverse urea hypothesis remains viable, and other mechanisms may contribute",
          "It is caused by low blood pressure during dialysis",
          "Its mechanism was settled by randomized trials"], 1,
         "A critical review found the reverse urea hypothesis viable. Idiogenic osmoles and brain acidosis are also proposed."),
        ("A 70-year-old man is 90 minutes into his first session. He has a new headache, has vomited once, and is restless. His pressure is unchanged. What do you do first?",
         ["Give an antiemetic and continue the session at the same settings",
          "Increase the blood flow to finish sooner",
          "Have the treatment slowed or stopped per protocol, check glucose and a neurologic examination, and call the attending nephrologist",
          "Wait for the session to end and reassess"], 2,
         "These are early signs of disequilibrium. Treatment after it is established is rarely successful, so you act early."),
        ("A maintenance patient returns after missing four sessions. Her urea is very high and she is drowsy. The nurse plans to run her usual order. What is the best response?",
         ["Call the attending nephrologist before connection, because missed sessions raise her disequilibrium risk",
          "Run a longer session to catch up",
          "Run her usual order, because she is not a new patient",
          "Send her home and reschedule"], 0,
         "A patient whose urea has risen for weeks resembles a new patient. Her usual order may be too efficient today."),
        ("How strong is the evidence that a particular first-session prescription prevents disequilibrium?",
         ["Several large randomized trials",
          "A meta-analysis of randomized trials",
          "A KDIGO recommendation graded 1A",
          "Mechanism, reviews, and case series only"], 3,
         "The syndrome is rare, so randomized trials are almost impossible. Prevention rests on physiology and expert practice."),
        ("A man with acute kidney injury after leptospirosis is in week 3 of outpatient dialysis. His urine output has risen from 200 to 900 mL per day. What should you do?",
         ["Stop dialysis today",
          "Record the trend and report it to the attending nephrologist the same day",
          "Ignore it, because urine output does not reflect kidney function",
          "Increase his fluid removal goal"], 1,
         "Rising urine output may signal recovery. The decision to test or stop belongs to the attending nephrologist."),
        ("In the cohort by Jordan and colleagues, what share of patients discharged on outpatient dialysis after AKI recovered kidney function?",
         ["About 10%",
          "About 90%",
          "About 41%",
          "None"], 2,
         "45 of 111 recovered, most within 30 days of discharge. The study was single-center and selected."),
        ("Why is low blood pressure during dialysis a particular concern in a patient with AKI?",
         ["It may reduce kidney perfusion and set back recovery",
          "It raises the potassium",
          "It causes disequilibrium",
          "It damages the dialyzer"], 0,
         "An injured kidney depends on blood flow to heal. Hypotension is a second injury."),
        ("A visiting patient arrives with an order from her home unit and hepatitis results dated seven months ago. Your unit accepts results only within a shorter interval. What is the correct plan?",
         ["Use the home order and place her at a general station",
          "Refuse to dialyze her",
          "Place her at a general station and draw new samples",
          "Ask the attending nephrologist for a local order, and place her by the unit protocol for unknown status"], 3,
         "The visiting order is information. Out-of-date serology is managed as unknown status."),
        ("Which document from a transferred patient tells you where and in which direction to needle?",
         ["The vaccination record",
          "The access type and cannulation map",
          "The medication list",
          "The advance directive"], 1,
         "The cannulation map and recent access problems guide the first needling (Modules 9 and 10)."),
        ("A patient with heart failure and a high potassium is ordered isolated ultrafiltration first. What is true?",
         ["Isolated ultrafiltration will lower the potassium",
          "Isolated ultrafiltration corrects acidosis",
          "Isolated ultrafiltration removes water and salt but clears little potassium, so diffusive dialysis is still needed",
          "Isolated ultrafiltration cannot remove sodium"], 2,
         "Without dialysis fluid flow there is no diffusion. Potassium leaves only in the small volume removed."),
        ("Why is blood pressure often better tolerated during isolated ultrafiltration than during diffusive dialysis?",
         ["Plasma osmolality changes little, so refilling and vessel tone are better preserved",
          "Less fluid can be removed",
          "The blood pump is turned off",
          "The dialysis fluid is cooler"], 0,
         "Diffusive dialysis lowers plasma osmolality as urea leaves, which slows refilling. Isolated ultrafiltration does not."),
    ],
    "terms": [("Dialysis disequilibrium syndrome", "Brain swelling and neurologic symptoms during or soon after dialysis, caused by a fast fall in plasma urea and other solutes."),
              ("Osmolality", "The concentration of dissolved particles in a fluid, in mOsm per kilogram of water."),
              ("Ineffective osmole", "A solute, such as urea at steady state, that crosses cell membranes and so pulls no water."),
              ("Idiogenic osmoles", "Particles made by brain cells to protect their volume during a long hyperosmolar state."),
              ("Asterixis", "A flapping tremor of the outstretched hands, seen in uremia and other metabolic brain disorders."),
              ("Urea reduction ratio", "The percentage fall in blood urea during one session."),
              ("Acute kidney injury requiring dialysis", "Sudden loss of kidney function severe enough to need dialysis, with a chance of recovery."),
              ("Transient patient", "A patient who dialyzes in a unit for a short time while away from the home unit."),
              ("Isolated ultrafiltration", "Removal of plasma water by pressure alone, with no dialysis fluid flowing.")],
    "readings": [("starting-dialysis-new-beginning.html", "What a new patient experiences in the first weeks of dialysis, for you and for the family."),
                 ("hemodialysis-transfer-guide.html", "How patients and units prepare for a transfer or a visit to another unit."),
                 ("aki-does-not-end-at-discharge.html", "Follow-up and recovery after acute kidney injury.")],
    "calcs": ["calc-osmolal-gap.html", "calc-dialysis-adequacy-ktv.html", "calc-urine-output-fluid-balance.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
