# -*- coding: utf-8 -*-
"""Physician on Duty, Module 03: Life Without Kidney Function II: Uremia, Residual Function, and Starting Dialysis.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at the dialysis chair of an older Filipino woman, holding a urine measuring jug and a laboratory sheet, while the patient&rsquo;s daughter stands beside her.",
    "objectives": [
        "Recognize the uremic syndrome and name the findings that need the attending nephrologist the same day.",
        "Explain uremic toxins by size and protein binding, and predict which ones hemodialysis removes poorly.",
        "State the urgent and planned reasons to start dialysis, and explain why current guidance ties the decision to symptoms and signs rather than to an estimated glomerular filtration rate (eGFR) alone.",
        "Define residual kidney function, describe how it is measured, and list what protects it and what harms it.",
        "Describe incremental hemodialysis, what its trials have and have not shown, and the safety checks it requires.",
    ],
    "big": """
{{plain:Picture a house where the garbage collection has stopped. The big bags by the door are easy to see and easy to count. But the smell that makes the house hard to live in comes from many small things that nobody sees. Dialysis is a truck that comes three times a week and takes the big bags well. Some of the small things it barely touches.}}
<p>The picture has a limit. Garbage sits still, and uremic solutes do not. They act on many organs. The bag we count, urea, is only mildly toxic itself. It is a marker that rises along with hundreds of other retained solutes.[[meyer2007]] And many new dialysis patients still have kidneys that collect some of the garbage every hour of the week.</p>
{{cards:Key terms for this module|Uremia::The illness caused by retained solutes when the kidneys fail.|Uremic toxin::A retained solute that harms the body.|Middle molecule::A retained solute larger than about 500 daltons, often a small protein.|Protein-bound solute::A retained solute that travels attached to albumin.|Residual kidney function (RKF)::The kidney function a patient still has after dialysis starts.|Residual urea clearance (Kru)::The urea clearance of the patient&rsquo;s own kidneys, from a timed urine collection.|Incremental hemodialysis::Starting with fewer or shorter sessions while the kidneys still help, then stepping up as their help fades.}}
<p>Most patients in your chairs are stable on their prescription. A few have uremia that is coming back, or kidney function that is quietly fading. Your work is to ask the uremia questions at every session, protect the kidney function that remains, and bring clear measurements to the attending nephrologist.</p>
""",
    "case": {"title": "She still passes a liter a day", "html": """
<p>Aling Rosario Dimaculangan, 58, is a retired public-school teacher from Malolos. She has diabetic kidney disease and started hemodialysis 7 weeks ago on a twice-weekly schedule written by her attending nephrologist.</p>
<p>It is 1:40 p.m., the start of the Thursday afternoon shift, after a 3-day gap. Nurse Jomar Villanueva reports. Her pre-dialysis weight is 2.9 kilograms above her target. Her blood pressure is 168/94 mm Hg and her pulse is 92 per minute. She is not breathless at rest. Both ankles are faintly swollen.</p>
<p>Aling Rosario says she &ldquo;still passes about a liter a day.&rdquo; Her daughter disagrees. She says it has been less since a computed tomography (CT) scan with contrast at another hospital 10 days ago. Her mother has also been nauseated in the mornings and itchy at night. The last timed urine collection was 6 weeks ago.</p>
<p>Nurse Villanueva has checked the access and sent pre-dialysis blood for the monthly panel. She asks you, &ldquo;Doc, should we add an extra session this week?&rdquo;</p>
<p><em>Illustrative values only, not targets.</em></p>
""", "questions": ["Which of her findings point to uremia, and which point to volume, and why does the difference matter?",
                  "What may have happened to her residual kidney function, and what information would show it?",
                  "Who decides whether her schedule changes, and what exactly will you report?"]},
    "sections": [
        ("uremia", "What uremia looks like", "What uremia looks like at the bedside", """
<p>Module 2 covered water, salt, potassium, and acid. This section covers the rest of the load. Healthy kidneys clear it in two ways. Small, water-soluble solutes pass through the glomerulus in the filtrate. Many solutes that travel attached to albumin cannot be filtered. Instead, cells of the proximal tubule take them from the blood and pass them into the urine. This is tubular secretion.[[meyer2007]]</p>
<p>When both routes fail, solutes accumulate and act on many organs at once. So uremia looks like many unrelated complaints.[[meyer2007]]</p>
{{fig:pod03_uremia}}
<div class="table-wrap"><table>
<thead><tr><th>Organ</th><th>What goes wrong</th><th>What you see or hear at the chair</th></tr></thead>
<tbody>
<tr><td>Brain and nerves</td><td>Solutes slow brain function and injure nerves</td><td>Fatigue, poor concentration, broken sleep, restless legs. Later, confusion and asterixis, a flapping tremor of the hands</td></tr>
<tr><td>Gut</td><td>Solutes act on the gut and the brain centers for appetite</td><td>Poor appetite, morning nausea or vomiting, a metallic taste</td></tr>
<tr><td>Skin</td><td>Uremic itch, from several causes acting together</td><td>Scratch marks, poor sleep from night itch</td></tr>
<tr><td>Blood</td><td>Platelets stick and clump poorly</td><td>Easy bruising, bleeding gums, needle sites that keep oozing</td></tr>
<tr><td>Serosa</td><td>The linings of the heart and lungs become inflamed</td><td>Chest pain that changes with posture or breathing, a pericardial rub</td></tr>
<tr><td>Muscle and nutrition</td><td>Poor intake and increased protein breakdown</td><td>Weight loss, thin arms and temples, weakness</td></tr>
</tbody></table></div>
<p>The features in this table follow a standard review and dialysis text.[[meyer2007]][[daugirdas2015]] They overlap with depression, anemia, and the effects of medicines, so the diagnosis is clinical.</p>
<h3>What the evidence says</h3>
<p>The uremic syndrome is a clinical description, not a laboratory threshold. No single solute explains it, and urea causes few of the symptoms itself.[[meyer2007]] A blood result supports your judgment but cannot replace your questions.</p>
<h3>What you do</h3>
{{cards:Five uremia questions for every pre-dialysis check|Appetite::Are you eating as much as usual?|Nausea::Have you vomited or felt sick, especially in the morning?|Itch::Does itching keep you awake?|Sleep::Are you sleeping through the night?|Thinking::Ask the family. Has the patient been slower, forgetful, or confused?}}
<p>Ask the same questions each time and write the answers. A change from the patient&rsquo;s own pattern matters most. This adds a uremia lens to the safe-to-start check in Module 11.</p>
<p>A new pericardial rub matters for a second reason. It may change the anticoagulation plan for the session, and that plan belongs to the attending nephrologist.[[daugirdas2015]]</p>
{{call:Stop and call the attending nephrologist the same day for a new pericardial rub, new confusion or asterixis, bleeding with no other cause, or uremic symptoms that return despite a fully delivered prescription. A rub with a low or falling blood pressure is an emergency: start your unit&rsquo;s protocol and call at once. Module 13 covers the falling pressure.}}
{{key:Ask the same five uremia questions at every session. A new answer is a finding, and it goes in the record.}}
"""),
        ("toxins", "Three kinds of toxin", "Three kinds of cargo: small, middle, and protein-bound toxins", """
<p>Picture three sizes of cargo at a gate. Small boxes pass easily. Large crates pass only through a wide gate, with a push. Boxes chained to a heavy trolley barely move at all. The gate is the dialyzer membrane, and the trolley is albumin.</p>
{{fig:pod03_toxins}}
<p>The European Uremic Toxin Work Group screened 857 publications and cataloged 90 retained solutes. Of these, 68 weighed less than 500 daltons. The other 22 were middle molecules, and 12 of those were larger than 12,000 daltons. Twenty-five solutes were bound to protein, and most of them were small.[[vanholder2003]] A 2012 update reviewed 621 later articles and added 56 newly reported solutes.[[duranton2012]]</p>
<p>A 2021 consensus conference added two dimensions to size: how dialysis removes each solute, and its links to symptoms and outcomes. This is a consensus statement, not a graded recommendation.[[rosner2021]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Group</th><th>Examples</th><th>How healthy kidneys clear it</th><th>How conventional hemodialysis does</th></tr></thead>
<tbody>
<tr><td>Small, water-soluble</td><td>Urea, creatinine, potassium</td><td>Filtration</td><td>Well, by diffusion</td></tr>
<tr><td>Middle molecules</td><td>Beta-2 microglobulin</td><td>Filtration, then uptake and breakdown in the tubule</td><td>Poorly with a low-flux membrane. Better with a high-flux membrane and convection</td></tr>
<tr><td>Protein-bound</td><td>Indoxyl sulfate, p-cresyl sulfate</td><td>Tubular secretion</td><td>Poorly with any membrane, because only the free fraction crosses</td></tr>
</tbody></table></div>
<p>Using the terms from Module 5: small solutes diffuse fast. Middle molecules diffuse slowly, so high-flux membranes and convection help. Module 7 covers the hemodiafiltration trials.</p>
<p>Protein-bound solutes are different. Most of each molecule sits on albumin, which stays behind the membrane. The healthy tubule works around this: transporters pull the solute off albumin and secrete it into the urine.[[meyer2007]] Several of these solutes, such as indoxyl sulfate, come from the breakdown of dietary protein by gut bacteria.[[meyer2007]]</p>
<h3>What the evidence does and does not show</h3>
<p>Poor removal of protein-bound solutes by dialysis is established physiology. Their tubular secretion is one reason residual kidney function may be valuable. Whether removing more of them improves how patients feel or how long they live is not proven. Treat that link as a mechanistic hypothesis.[[rosner2021]]</p>
<h3>What you do</h3>
<p>Kt/V, the urea-based dose measure in Module 7, is a surrogate. It tracks urea, not the whole retained load. A patient with a good Kt/V and new uremic symptoms is still reported.</p>
{{key:Urea is the messenger, not the whole message. A good urea number does not rule out uremia.}}
"""),
        ("when", "When dialysis begins", "When dialysis begins: symptoms, not a single number", """
<p>Starting dialysis is like fixing a leaking roof. You do not wait for the ceiling to fall, and you do not replace the roof because a gauge crossed an arbitrary line.</p>
<h3>Why one number cannot mark the day</h3>
<p>As nephrons are lost, the survivors compensate. Each filters more and excretes more potassium, phosphate, and acid. For a time the blood stays close to normal. Then the adaptations fail, at different levels of kidney function in different people. So the decision rests on the patient, not on a glomerular filtration rate (GFR).</p>
<h3>The evidence: the IDEAL trial</h3>
<p>The IDEAL (Initiating Dialysis Early And Late) trial randomized 828 adults with progressive chronic kidney disease (CKD) at 32 centers in Australia and New Zealand. One group was planned to start dialysis at an estimated GFR of 10 to 14 mL per minute (early start), the other at 5 to 7 (late start). GFR was estimated by the Cockcroft-Gault equation.[[cooper2010]]</p>
<p>Over a median of 3.59 years, 37.6% of the early group and 36.6% of the late group died. The hazard ratio for early start was 1.04 (95% confidence interval 0.83 to 1.30).[[cooper2010]]</p>
<p>One detail changes how you read the result. In the late group, 75.9% started above the target GFR because symptoms developed.[[cooper2010]] So the trial shows that waiting under close follow-up, and starting when symptoms appear, is safe. It does not show that waiting for a GFR of 5 to 7 in a patient with symptoms is safe.</p>
<h3>What the guidelines say</h3>
<p>Kidney Disease: Improving Global Outcomes (KDIGO) 2024 Practice Point 5.4.1 says to initiate dialysis based on a composite assessment of a person&rsquo;s symptoms, signs, quality of life, preferences, level of GFR, and laboratory abnormalities. Practice Point 5.4.2 says to start when one or more of these is present: symptoms or signs of kidney failure, such as uremic neurologic signs, pericarditis, anorexia, acid-base or electrolyte problems that resist medicines, or intractable itch; volume or blood pressure that cannot be controlled; and nutritional decline that resists dietary care, or cognitive impairment. It notes that this often, but not invariably, occurs at a GFR between 5 and 10 mL per minute per 1.73 m&sup2;. Both are practice points, which KDIGO does not grade.[[kdigo_ckd2024]]</p>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) 2015 Guideline 1.2, which is not graded, bases the decision primarily on signs and symptoms of uremia, protein-energy wasting, and whether metabolic problems and volume overload can still be managed medically.[[kdoqi_hd2015]] A KDIGO Controversies Conference called for starts that reflect each patient&rsquo;s goals.[[chan2019]] None sets a GFR at which dialysis must begin.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Urgent: start the same day</th><th>Planned: start in the coming days or weeks</th></tr></thead>
<tbody>
<tr><td>Chemistry</td><td>High potassium that does not respond to treatment. Severe metabolic acidosis</td><td>Acid or electrolyte problems that medicines no longer control</td></tr>
<tr><td>Volume</td><td>Fluid in the lungs that does not respond to medicines</td><td>Volume or blood pressure that can no longer be controlled</td></tr>
<tr><td>Uremia</td><td>Pericarditis. Encephalopathy, with confusion, asterixis, or seizures. Uremic bleeding</td><td>Poor appetite, nausea, intractable itch, fatigue, or slowed thinking that are getting worse</td></tr>
<tr><td>Nutrition</td><td></td><td>Weight and muscle loss that dietary care does not reverse</td></tr>
</tbody></table></div>
<p>Both columns draw on the KDIGO list.[[kdigo_ckd2024]] Sorting them into urgent and planned is established practice.[[daugirdas2015]]</p>
{{flow:From advanced CKD to the first session|Education::The patient and family learn about treatment options, including transplantation, by CKD stage 4 (KDOQI).|Plan the access::A KDIGO practice point advises considering access planning when the GFR is below 15 to 20 mL per minute per 1.73 m&sup2;, or when the two-year risk of needing kidney replacement therapy is above 40%.|Watch for the first failures::Visits look for symptoms, nutritional decline, and loss of control of volume, pressure, potassium, and acid.|Decide together::The nephrologist, the patient, and the family weigh symptoms, signs, and preferences.|First session::A planned start through a mature access. Module 12 covers the first sessions.}}
<p>The education and access steps come from the same guidelines.[[kdoqi_hd2015]][[kdigo_ckd2024]] Once dialysis starts, creatinine-based GFR equations are no longer valid, because dialysis removes creatinine.</p>
<h3>What you do</h3>
<p>A referred patient may arrive with a creatinine value and a note that says &ldquo;start dialysis today.&rdquo; Find out which indication is present and how urgent it is. Record the symptoms and signs, and call the attending nephrologist with them. The decision and the prescription belong to the nephrologist. The <a href="calc-starting-dialysis-planner.html">starting dialysis planner</a> gives a structured list of indications and preparations to bring to that call.</p>
{{formula:<strong>Decision walk-through, illustrative patients.</strong><br>Patient A: a 64-year-old man, estimated GFR 7 mL per minute per 1.73 m&sup2;. No symptoms, normal potassium, stable weight.<br>Patient B: estimated GFR 11. Pericardial rub, vomiting, and asterixis.<br>Patient B has two urgent indications, pericarditis and encephalopathy, plus vomiting, despite the higher GFR. Call now.<br>Patient A has no indication from the table. In IDEAL, waiting with close follow-up gave the same survival as an early start: 36.6% versus 37.6% died.[[cooper2010]][[kdigo_ckd2024]]<br><strong>What this does and does not tell you.</strong> Both patients go to the nephrologist. The difference is the urgency of the call and what you write.}}
{{key:Dialysis is started for the patient&rsquo;s symptoms and signs. The creatinine value is context, not the indication.}}
"""),
        ("residual", "Residual function", "Residual kidney function: the small helper that works all week", """
<p>Think of a small helper who works all 168 hours of the week while the big machine works about twelve. The helper is slow, but never stops.</p>
{{fig:pod03_helper}}
<h3>What the remaining nephrons do</h3>
<p>Residual kidney function (RKF) is the work the patient&rsquo;s own kidneys still do. The surviving nephrons filter small solutes and water. They secrete protein-bound solutes, which dialysis removes poorly. They excrete salt, water, potassium, and phosphate between sessions. They also keep some of their hormone work, including erythropoietin and activated vitamin D.[[meyer2007]][[daugirdas2015]]</p>
<p>This function declines after dialysis starts, and fastest at first. In 42 patients from a pilot trial in the United States, kidney urea clearance fell by a median of 32% by week 6 and by about 61% by week 48. Urine volume fell more steadily, by a median of 47% by week 48. Urine volume correlated only moderately with urea clearance.[[sirich2024]]</p>
<h3>What the evidence shows</h3>
<p>These studies are observational. Each is open to the same confounder: patients who keep their kidney function are often healthier in other ways.</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Design and size</th><th>Finding</th></tr></thead>
<tbody>
<tr><td>Obi and colleagues, 2016</td><td>Cohort of 6,538 patients starting hemodialysis in the United States</td><td>Faster first-year loss of residual urea clearance was associated with higher mortality. A decline of 6.0 versus 1.5 mL per minute per 1.73 m&sup2; per year carried an adjusted hazard ratio of 2.00 (1.55 to 2.59)[[obi2016]]</td></tr>
<tr><td>Choices for Healthy Outcomes in Caring for End-Stage Renal Disease (CHOICE) Study, 2010</td><td>Prospective cohort of 734 patients starting hemodialysis in 81 clinics</td><td>Urine output at year 1 was associated with lower all-cause mortality (hazard ratio 0.70, 0.52 to 0.93) and with lower erythropoietin doses.[[shafi2010]]</td></tr>
<tr><td>CANUSA (Canada-USA) reanalysis, 2001</td><td>601 patients on peritoneal dialysis</td><td>Each additional 250 mL of daily urine was associated with a 36% lower relative risk of death. Peritoneal clearance was not associated with survival[[bargman2001]]</td></tr>
</tbody></table></div>
<p>None of these studies shows that preserving residual function prolongs life. The authors of the largest cohort said the benefit of preservation strategies on mortality still has to be determined.[[obi2016]]</p>
<h3>How residual function is measured</h3>
<p>Urine volume is easy to record but tracks clearance loosely. The better measure is residual urea clearance (Kru), calculated from a timed collection of every void between two sessions. It uses the urine urea nitrogen, the urine volume, the collection time, and the mean of the post-dialysis and next pre-dialysis blood urea nitrogen (BUN).[[daugirdas2015]]</p>
<p>KDOQI 2015 Guideline 3.2, which is not graded, says the dose of hemodialysis may be reduced in a patient with significant residual function, provided that function is measured periodically.[[kdoqi_hd2015]]</p>
{{formula:<strong>Worked example, illustrative numbers. Residual urea clearance from a timed interdialytic urine collection.</strong>[[daugirdas2015]]<br>Kru (mL per minute) = [urine urea nitrogen (mg/dL) &times; urine volume (mL)] &divide; [mean BUN (mg/dL) &times; collection time (minutes)]<br>Mean BUN = (post-dialysis BUN + next pre-dialysis BUN) &divide; 2<br>Collection over a 44-hour interval: 44 &times; 60 = 2,640 minutes. Urine volume 1,320 mL. Urine urea nitrogen 380 mg/dL.<br>Post-dialysis BUN 22 mg/dL, next pre-dialysis BUN 62 mg/dL. Mean BUN = (22 + 62) &divide; 2 = 42 mg/dL.<br>Kru = (380 &times; 1,320) &divide; (42 &times; 2,640) = 501,600 &divide; 110,880 = <strong>about 4.5 mL per minute</strong>.<br><strong>What it does and does not tell you.</strong> A missed void lowers the result falsely. A mistimed blood sample changes it as much as the urine does. It informs the nephrologist&rsquo;s prescription and does not set it.}}
<p>The <a href="calc-measured-crcl.html">measured creatinine clearance calculator</a> uses the same timed-urine arithmetic for creatinine.</p>
<h3>What you do</h3>
<p>Treat urine volume as a vital sign of the kidney. Ask for it at every session, write the patient&rsquo;s estimate as a trend, and report a fall. The <a href="calc-urine-output-fluid-balance.html">urine output and fluid balance tool</a> helps you track it.</p>
{{formula:<strong>Arithmetic illustration, not a target. Urine as a vital sign.</strong><br>A patient who passes 1,000 mL a day removes about 1,000 &times; 3 = 3,000 mL over a 3-day gap.<br>If urine falls to 300 mL a day, the same gap removes about 300 &times; 3 = 900 mL.<br>The difference, about 3,000 &minus; 900 = 2,100 mL, now stays in the body and adds to the next session&rsquo;s fluid goal.<br><strong>What it does and does not tell you.</strong> It explains why weight gains rise as urine falls, not what fluid goal is safe. That belongs to the prescription (Module 8).}}
{{key:Record urine volume at every session as a trend. A falling trend is a finding to report, not a detail.}}
"""),
        ("protect", "Protecting it", "What protects and what harms residual function", """
<p>The helper is fragile. Low pressure, poisons, and dehydration all slow him down, and some injuries are permanent.</p>
<p>The surviving nephrons depend on blood flow, and there are few spares. Low pressure during dialysis, aggressive fluid removal, and vomiting or diarrhea all reduce that flow. Drugs that injure the tubule or narrow the arterioles add damage, and so does obstruction or infection of the urinary tract.</p>
{{fig:pod03_nephron}}
<div class="table-wrap"><table>
<thead><tr><th>Factor</th><th>Why it matters</th><th>Strength of evidence</th></tr></thead>
<tbody>
<tr><td>Low blood pressure during dialysis, aggressive fluid removal</td><td>Less blood flow to the remaining nephrons</td><td>Inference from physiology. Module 13 covers prevention</td></tr>
<tr><td>Volume depletion from vomiting, diarrhea, or a target weight set too low</td><td>Less blood flow to the remaining nephrons</td><td>Inference from physiology</td></tr>
<tr><td>Iodinated contrast</td><td>Narrowing of kidney vessels and direct injury to tubular cells</td><td>Inference. The size of the risk in this group is not well measured</td></tr>
<tr><td>Nonsteroidal anti-inflammatory drugs (NSAIDs)</td><td>They block the prostaglandins that keep the arterioles of a struggling kidney open</td><td>Established physiology, inference for this group</td></tr>
<tr><td>Aminoglycoside antibiotics</td><td>Direct injury to tubular cells</td><td>Established physiology, inference for this group</td></tr>
<tr><td>Hemodialysis rather than peritoneal dialysis</td><td>Mechanism not established</td><td>Association[[moist2000]]</td></tr>
<tr><td>Angiotensin-converting enzyme (ACE) inhibitor or calcium channel blocker use</td><td>Mechanism not established</td><td>Association with less loss. A hypothesis, not proof of protection[[moist2000]]</td></tr>
</tbody></table></div>
<h3>What the evidence shows</h3>
<p>Moist and colleagues studied a national random sample of new dialysis patients in the United States. Loss was defined as a urine volume below 200 mL in 24 hours at about one year. Loss was more likely with diabetes (adjusted odds ratio 1.82), heart failure (1.32), and female sex (1.45). Patients on peritoneal dialysis were less likely to lose function than those on hemodialysis (0.35). Use of an ACE inhibitor (0.68) or a calcium channel blocker (0.77) was associated with less loss.[[moist2000]]</p>
<p>The authors called these findings hypotheses. Patients who received these drugs may have differed in other ways, so the study does not show that either drug protects the kidney. The harms in the table are inference from physiology, not trial results.</p>
<h3>What you do</h3>
<p>Before you agree to iodinated contrast, a nonsteroidal drug, or an aminoglycoside for a patient who still passes urine, ask whether the attending nephrologist wants an alternative. Report recurrent low pressure (Module 13) in such a patient, because each episode may cost kidney function as well as comfort.</p>
{{call:Stop and call the attending nephrologist when a patient reports or shows a fall in urine output, or when a contrast study, a nephrotoxic drug, or surgery is planned for a patient who still passes urine. Do not change the prescription. Bring the dates, the urine volumes, and the planned procedure.}}
{{key:A patient who still passes urine has something to lose. Protect it before every scan, every new medicine, and every session.}}
"""),
        ("incremental", "Incremental dialysis", "Incremental dialysis: starting with less, then stepping up", """
<p>Think of a dimmer switch rather than an on-off switch. Dialysis starts low while the kidneys still help, and it is turned up as their help fades.</p>
<p>The physiology is addition. The total clearance a patient receives is kidney clearance plus dialysis clearance. When residual urea clearance is substantial, fewer sessions can reach a similar total. The plan is safe only if residual function is measured and the prescription steps up when it falls.</p>
<h3>The trials, in order of strength</h3>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Design and size</th><th>Main findings</th></tr></thead>
<tbody>
<tr><td>Fern&aacute;ndez Lucas and colleagues, Spain, 2025</td><td>Open-label randomized trial, 150 patients, hemodiafiltration (HDF) twice versus three times weekly</td><td>No difference in GFR decline, anuria (5 versus 4 patients), admissions, or mortality. 69.1 versus 122.6 sessions a year. Fifteen patients stepped up to three times weekly after an average of 193 days[[fernandezlucas2025]]</td></tr>
<tr><td>Vilar and colleagues, United Kingdom, 2022</td><td>Feasibility randomized trial, 55 patients, four centers, 12 months</td><td>Feasible. Fewer serious adverse events with incremental start (incidence rate ratio 0.47, 0.27 to 0.81). Three deaths in each group. Lower serum bicarbonate. Lower cost. No signal that residual function was protected[[vilar2022]]</td></tr>
<tr><td>Murea and colleagues, United States, 2022</td><td>Pilot randomized trial, 48 patients, 14 dialysis centers</td><td>Twice weekly for 6 weeks, with protocol diuretics, bicarbonate, and a potassium binder. Feasible. Smaller declines in urine volume and clearance, with confidence intervals that crossed zero. One death versus six. Funded by industry[[murea2022]]</td></tr>
<tr><td>Kittiskulnam and colleagues, Thailand, 2025</td><td>Randomized trial, 30 patients, 12 months</td><td>Once weekly with a low-protein diet and keto-analogues, versus twice weekly with a regular diet. Urine at 3 months 1,921 versus 1,305 mL a day. Higher urea clearance at 6 months. Two things changed at once, so their effects cannot be separated[[kittiskulnam2025]]</td></tr>
<tr><td>TwoPlus, United States, in progress</td><td>Randomized non-inferiority trial, 350 patients planned</td><td>Composite of death, hospital admission, or emergency visits at 2 years. Results not yet published[[murea2024]]</td></tr>
</tbody></table></div>
<p>The trials are small. None of the completed trials had a clinical primary outcome such as death or hospital admission. TwoPlus does. The completed trials show feasibility and suggest reasonable safety in selected patients watched closely. They disagree on whether residual function is protected. The British and Spanish trials found no difference. The two smaller trials suggest benefit, with wide uncertainty.</p>
<h3>The observational data</h3>
<p>Obi and colleagues compared 351 patients who started twice weekly with 8,068 matched patients who started three times weekly. The incremental group kept 16% more residual urea clearance. Incremental starts were associated with higher mortality only in patients whose baseline clearance was 3.0 mL per minute per 1.73 m&sup2; or less (hazard ratio 1.61, 1.07 to 2.44). Above that level there was no difference (0.99, 0.76 to 1.28).[[obi2016incr]] Doctors chose who started twice weekly, and all had survived the first year, so bias is likely.</p>
<p>A meta-analysis of 22 cohort studies of incremental hemodialysis and peritoneal dialysis (75,292 participants) found no clear mortality difference (risk ratio 1.14, 0.85 to 1.52), with wide disagreement between studies (heterogeneity 86%). Full-dose dialysis began after about 12 months on average.[[garofalo2019]]</p>
<h3>What the guidelines say</h3>
<p>KDOQI Guideline 3.2 permits a reduced dose with measured residual function, as above.[[kdoqi_hd2015]] The KDIGO Controversies Conference called for better evidence on individualized approaches.[[chan2019]] Neither sets a threshold.</p>
{{formula:<strong>Decision walk-through. The opening case against four entry rules.</strong><br>Vilar 2022: urea clearance 3 mL per minute per 1.73 m&sup2; or more.[[vilar2022]]<br>Murea 2022: urine 500 mL a day or more and estimated GFR 5 or more.[[murea2022]]<br>Fern&aacute;ndez Lucas 2025: kidney urea clearance 2.5 mL per minute or more.[[fernandezlucas2025]]<br>TwoPlus: kidney urea clearance 3.5 mL per minute per 1.73 m&sup2; or more and urine 500 mL in 24 hours or more.[[murea2024]]<br>Aling Rosario&rsquo;s last clearance is 6 weeks old, and her urine may have fallen since the scan. You cannot say which rule she would meet today.<br><strong>What this does and does not tell you.</strong> These are study eligibility rules, not unit thresholds, and none is a validated cut-off. The nephrologist and your unit&rsquo;s protocol set the criteria. You bring current measurements.}}
{{flow:Stepping up from fewer sessions to full dialysis|Start::The attending nephrologist orders fewer sessions because measured residual function is substantial.|Measure::Urine volume every session. Timed collections as ordered.|Watch after the long gap::Potassium, fluid gain, blood pressure, bicarbonate, and uremic symptoms.|Recognize a trigger::A fall in urine or clearance, rising weight gains, high potassium, low bicarbonate, or new symptoms.|Report::Call the attending nephrologist with the measurements and the trend.|Step up::The nephrologist decides whether to add time or sessions.}}
<h3>What you do</h3>
<p>A patient on a twice-weekly schedule is not missing a session. Watch closely after the long gap. The trial in the United Kingdom found lower bicarbonate with incremental starts.[[vilar2022]] Report any fall in urine, rising weight gains, or new uremic symptoms. Each may prompt a step up.</p>
{{key:Incremental dialysis is a plan that depends on measured kidney function. When the urine falls, the plan must change, and the nephrologist changes it.}}
"""),
        ("bedside", "At the chair", "Putting it together at the chair", """
<p>Three questions cover every patient. They take less than a minute once they become habit.</p>
{{cards:Three questions at every chair|Is this uremia?::Ask the five uremia questions. Compare the answers with the patient&rsquo;s own pattern.|Is there kidney function to protect?::Ask about urine volume. Check for planned contrast, new drugs, or recent low pressure.|Is the schedule still right?::Check the order, the weight gain after the long gap, and the date of the last timed collection.}}
<h3>The timed collection</h3>
<p>A timed collection is only as good as its handling. At the start time the patient empties the bladder and discards that urine, then keeps every void until the stop time. The two blood samples must bracket the collection: one at the end of the previous session, one at the start of the next. Follow your unit&rsquo;s protocol and the skills checklist below.</p>
{{fig:pod03_urinekit}}
<p>When you call, use the situation, background, assessment, and recommendation (SBAR) format from Module 1. Include the schedule, the last clearance and its date, and recent events.</p>
{{key:Bring measurements, not impressions: a urine volume, a weight trend, and the date of the last collection.}}
"""),
    ],
    "debrief": ["""
<p><strong>Uremia or volume?</strong> Two findings point to uremia: morning nausea and night itch. Both are new. Three findings point to volume: a weight 2.9 kilograms above target after the long gap, a blood pressure of 168/94 mm Hg, and ankle edema. She is not breathless at rest. The two problems have different fixes. Extra fluid removal treats volume but does not replace the protein-bound and middle-sized solutes her kidneys may have been clearing. You ask the five questions in full, examine for a rub and asterixis, and find neither.</p>
<p><strong>What happened to her residual function?</strong> Her story fits a fall in residual function after the contrast scan. The timing fits, and less urine, new symptoms, and a larger weight gain are what lost kidney work would produce. Diet, medicines, or another cause of nausea remain possible. Three pieces of information would settle it: a measured urine volume, a repeat timed collection to compare with 6 weeks ago, and today&rsquo;s potassium and bicarbonate. Ask too whether anyone gave her an NSAID or other new medicine at the other hospital.</p>
<p><strong>Who decides, and what do you report?</strong> The attending nephrologist decides whether her schedule changes. An extra session and today&rsquo;s fluid goal are both part of the prescription. You call before connection. In SBAR form: Aling Rosario, 7 weeks on twice-weekly hemodialysis, is 2.9 kilograms above target with ankle edema and new nausea and itch. Her family reports less urine since a contrast CT scan 10 days ago, and her last timed collection was 6 weeks ago. You request a review of her schedule and an order for a repeat timed collection, and you ask how the nephrologist wants today&rsquo;s fluid goal handled. You record the advice and the time, and tell Nurse Villanueva and the family the plan.</p>
"""],
    "skills": {"title": "Measuring urine output and a timed interdialytic urine collection",
               "intro": "Perform these steps with a patient who still passes urine, or in a role play with a colleague, while your preceptor observes.",
               "items": [
                   ("Confirms the order for the collection and the steps in the unit&rsquo;s protocol.", True),
                   ("Explains the collection to the patient and family in plain language, including the start rule: empty the bladder and discard that urine at the start time.", False),
                   ("Labels the container with the patient&rsquo;s name, a second identifier, and the start time.", True),
                   ("Instructs that every void until the stop time goes into the container, and explains how to store it.", False),
                   ("Records the stop time and includes the final void.", False),
                   ("Confirms that the post-dialysis blood sample was drawn at the end of the previous session and that the pre-dialysis sample is drawn at the start of the next.", True),
                   ("Records the total volume and any missed void honestly in the record.", True),
                   ("Records the patient&rsquo;s own estimate of daily urine at each session as a trend.", False),
                   ("Asks the five uremia questions and records the answers.", False),
                   ("Reports a reported or measured fall in urine volume to the attending nephrologist.", True),
                   ("Checks whether any planned contrast study or new nephrotoxic drug has been discussed with the nephrologist.", False),
               ],
               "placement": "For two weeks, list every patient on your shifts who still passes urine. For each, record the urine estimate at each session, the date of the last timed collection, and any recent contrast study or new medicine. Review the list with your preceptor and identify one patient whose trend you will report to the attending nephrologist."},
    "quiz": [
        ("Why is urea described as a marker of uremia rather than its main cause?",
         ["Dialysis does not remove urea",
          "Urea is only mildly toxic itself and rises along with many other retained solutes",
          "Urea is bound to albumin",
          "Urea levels are always normal in uremia"], 1,
         "Urea is easy to measure and moves with the retained load, but it causes few of the symptoms itself."),
        ("A man has a Kt/V above target but reports new night itch, poor appetite, and morning nausea. What is the best interpretation?",
         ["His dialysis is adequate, so the symptoms are not uremic",
          "He needs an antihistamine and no report",
          "A good urea-based measure does not rule out uremia, so report the symptoms",
          "He should skip his next session"], 2,
         "Kt/V is a surrogate that tracks urea, not middle or protein-bound solutes."),
        ("Why does conventional hemodialysis remove indoxyl sulfate poorly?",
         ["Most of it is bound to albumin, and only the small free fraction crosses the membrane",
          "It is too large to pass any membrane",
          "It is produced only during dialysis",
          "It is removed only by convection"], 0,
         "The healthy tubule secretes protein-bound solutes. Dialysis cannot."),
        ("What did the European Uremic Toxin Work Group find about the 90 retained solutes it cataloged?",
         ["They were all larger than 12,000 daltons",
          "They were all bound to protein",
          "They were all removed well by low-flux dialysis",
          "Most were small, but many were middle molecules or protein-bound"], 3,
         "Of 90 solutes, 68 were under 500 daltons, 22 were middle molecules, and 25 were protein-bound."),
        ("What did the IDEAL trial show?",
         ["Early start reduced deaths by about one third",
          "A planned early start did not improve survival compared with waiting under close follow-up",
          "Late start increased cardiovascular events",
          "Dialysis should begin at an estimated GFR of 15"], 1,
         "Deaths were 37.6% with early start and 36.6% with late start."),
        ("Why must the IDEAL result be read with care?",
         ["Most patients in the late-start group began dialysis above the target GFR because symptoms developed",
          "The trial was too small to detect any difference",
          "It included only patients on peritoneal dialysis",
          "It used measured rather than estimated GFR"], 0,
         "It tested waiting with close follow-up, not waiting in a symptomatic patient."),
        ("A referred woman with an estimated GFR of 9 has a pericardial rub, vomiting, and asterixis. What is the best next step?",
         ["Send her home",
          "Book a planned start in two weeks",
          "Order a repeat creatinine and wait for it",
          "Call the attending nephrologist now about an urgent start"], 3,
         "A pericardial rub and asterixis are urgent uremic indications whatever the GFR, and the vomiting adds to them."),
        ("How does KDIGO 2024 grade its practice points on when to start dialysis?",
         ["They are practice points, which KDIGO does not grade",
          "Grade 1A",
          "Grade 2C",
          "Class I, Level of Evidence A"], 0,
         "Practice points are ungraded. Do not borrow another system&rsquo;s grades."),
        ("A resident calculates an estimated GFR from the creatinine of a patient on dialysis for a year. What is wrong?",
         ["Nothing, if the patient is weighed first",
          "The equation must be multiplied by two",
          "Equations that estimate GFR from creatinine are not valid once dialysis has started",
          "Creatinine cannot be measured in dialysis patients"], 2,
         "Dialysis removes creatinine, so the blood level no longer reflects kidney function."),
        ("What did the CHOICE cohort find about urine output at one year on hemodialysis?",
         ["It prevented death in a randomized comparison",
          "It was associated with lower all-cause mortality, in an observational study",
          "It had no relationship with any outcome",
          "It increased erythropoietin needs"], 1,
         "The hazard ratio was 0.70 in an observational cohort, so confounding is possible."),
        ("A timed collection gives a much lower clearance than before. The patient forgot to collect two voids. What is the best interpretation?",
         ["Her kidney function has certainly been lost",
          "The result is accurate because the blood samples were timed",
          "Missed voids raise the calculated clearance",
          "The result underestimates her clearance. Record the missed voids and tell the nephrologist"], 3,
         "An incomplete collection lowers the calculated clearance. Record it honestly."),
        ("A man who passes a liter of urine a day is scheduled for a non-urgent contrast CT scan. What should you do?",
         ["Approve the scan, because he is on dialysis anyway",
          "Ask whether the attending nephrologist wants an alternative or a plan before the scan",
          "Cancel the scan on your own authority",
          "Add an extra dialysis session after the scan"], 1,
         "Residual function is worth protecting, and the decision belongs to the nephrologist."),
        ("What did Moist and colleagues find about ACE inhibitor use and loss of residual function?",
         ["ACE inhibitors were shown to protect residual function in a trial",
          "ACE inhibitors caused loss of residual function",
          "Use was associated with less loss, which the authors treated as a hypothesis",
          "There was no association"], 2,
         "The adjusted odds ratio was 0.68 in an observational cohort, which does not prove protection."),
        ("A woman on twice-weekly dialysis has rising weight gains and says her urine has fallen. What do you do?",
         ["Report the trend to the attending nephrologist, who decides whether to step up the schedule",
          "Record a missed session",
          "Change her to three sessions a week",
          "Raise her fluid goal to remove the extra weight in one session"], 0,
         "Rising gains and falling urine are triggers to step up. The schedule and the fluid goal belong to the nephrologist."),
        ("What have the completed randomized trials of incremental dialysis shown so far?",
         ["Incremental starts clearly preserve residual function",
          "Incremental starts double mortality",
          "Twice-weekly dialysis is safe for every patient",
          "Incremental starts are feasible in selected patients, and results on protecting residual function disagree"], 3,
         "The British and Spanish trials found no protection. Two smaller trials suggested benefit. TwoPlus is in progress."),
    ],
    "terms": [("Uremic syndrome", "The illness caused by retained solutes in kidney failure, affecting the brain, gut, skin, blood, serosa, and muscle."),
              ("Uremic retention solute", "A substance that builds up in the blood when the kidneys fail. It is called a uremic toxin when it harms the body."),
              ("Middle molecule", "A retained solute larger than about 500 daltons. High-flux membranes and convection remove it better than low-flux membranes."),
              ("Protein-bound solute", "A retained solute that travels attached to albumin. The kidney secretes it, and dialysis removes it poorly."),
              ("Tubular secretion", "Active transfer of a substance from the blood into the urine by the cells of the kidney tubule."),
              ("Asterixis", "A flapping tremor of the outstretched hands, seen in uremic and other metabolic encephalopathies."),
              ("Residual kidney function", "The kidney function a patient still has after dialysis starts."),
              ("Residual urea clearance (Kru)", "The volume of blood the kidneys clear of urea each minute, calculated from a timed interdialytic urine collection."),
              ("Incremental hemodialysis", "Starting with fewer or shorter sessions while residual function is substantial, then increasing as it falls."),
              ("Practice point", "A KDIGO statement of expert guidance that is not graded for strength or evidence.")],
    "readings": [("when-should-dialysis-start.html", "The indications for starting dialysis and the evidence on timing, for patients and clinicians."),
                 ("incremental-dialysis.html", "How incremental dialysis works and which patients may be suited to it."),
                 ("uremic-toxin-precursors.html", "Where uremic toxins come from, including those made by gut bacteria from dietary protein.")],
    "calcs": ["calc-starting-dialysis-planner.html", "calc-measured-crcl.html", "calc-urine-output-fluid-balance.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
