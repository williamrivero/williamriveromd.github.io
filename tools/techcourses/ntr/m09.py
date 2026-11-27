# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 09: AKI, AKD and recovery (including tropical AKI).
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2012
statements and grades checked against the guideline's summary of recommendations; KDIGO 2026 AKI/AKD treated as a public-review
draft; trial and cohort numbers checked against PubMed abstracts or full text. No doses. Fictional case."""

MODULE = {
 'image_alt': 'A resident and a medical intern at the bedside of a jaundiced farmer in a provincial hospital ward, checking the urine bag while the patient&rsquo;s wife watches.',
 'objectives': [
  '<strong>Intern:</strong> Recognize a rising creatinine or a falling urine output early, stage it by the Kidney Disease: Improving Global Outcomes (KDIGO) criteria, and report the exposures that matter: floodwater, fever, medicines, contrast, herbal products and heat.',
  '<strong>Resident:</strong> Build the acute kidney injury (AKI) differential by mechanism, including leptospirosis, dengue, severe malaria, snakebite and heat illness, and write a monitored plan that protects the kidney while the cause is treated.',
  '<strong>Fellow:</strong> Integrate the indications for kidney replacement therapy (KRT), the place of biomarkers in the KDIGO 2026 public-review draft, and a structured follow-up for acute kidney disease (AKD) and the risk of chronic kidney disease (CKD).',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the rising creatinine on your service</span>The <strong>intern</strong> is often the first to see the number: a creatinine higher than yesterday, a urine bag that has not been emptied since noon, a patient who waded through a flood last week. Your job is to notice, chart the urine, list the exposures, and report early. The <strong>resident</strong> owns the differential, the stage, the monitoring plan and the conversation with the attending. The <strong>fellow</strong> decides with the attending when the kidney needs support, which patients need transfer, and who will see the patient after discharge. Nobody on this ladder waits for the creatinine to &ldquo;declare itself.&rdquo;</div>
{{plain:Think of the kidneys as a water treatment plant for a town. The plant runs quietly with a large reserve. When a typhoon cuts the power, floods the intake or poisons the filters, the town does not notice at once. The tanks stay full for a while. By the time the taps run brown, the plant has been failing for a day or more.}}
<p>The picture has a limit. A treatment plant either runs or stops, but the kidney fails along a continuum, and the number we watch lags behind the injury. Creatinine is made by muscle at a fairly steady rate and cleared mainly by filtration. When filtration falls suddenly, creatinine does not jump. It climbs over hours to days toward a new steady state, so a creatinine that is still &ldquo;only slightly up&rdquo; on day one can hide a filtration rate that has already collapsed. Urine output responds faster, but it is lost when nobody measures it, and it can be preserved in some injuries, leptospirosis among them, while the filtration rate falls. In a patient with little muscle, the elderly woman or the wasted farmer, creatinine underestimates the injury twice: it starts low and it rises slowly.</p>
<p>Underneath the number, three things happen. Blood flow to the kidney can fall, from bleeding, dehydration, capillary leak or shock, and the kidney protects itself until it cannot. The tubules can be injured directly, by toxins, pigments, ischemia or infection, and the injured cells slough and block their own tubules. Or the outflow can be obstructed. In the tropics, one infection can do all three at once, which is why leptospirosis and severe malaria fill nephrology wards after the rains.</p>
{{cards:Key numbers|AKI by KDIGO 2012 (not graded)::Creatinine rise of 0.3 mg/dL or more within 48 hours, or to 1.5 times baseline or more within 7 days, or urine output below 0.5 mL/kg/h for 6 hours|Evaluate 3 months after AKI (KDIGO 2012, not graded)::Check for resolution, new CKD or worsening of existing CKD|Leptospirosis after the 2009 Metro Manila flood::51 of 471 hospitalized patients died (10.8%); anuria at admission carried a risk ratio of 4.17 for death (observational)|AKI in dengue (meta-analysis of 37 studies)::Pooled prevalence 8% (observational, high heterogeneity)|CKD after AKI (meta-analysis of 13 cohorts)::Pooled adjusted hazard ratio 8.8 for CKD and 3.1 for kidney failure (observational)}}
<p>Most patients with AKI on a medical ward recover once the cause is fixed: fluid for the dehydrated, the culprit drug stopped, the catheter unblocked, the infection treated. A few have AKI that kills within days unless someone recognizes the tropical pattern, measures the urine, and starts or transfers for kidney replacement in time. Your work is to stage early, find the mechanism, protect the kidney from the next insult, and make sure recovery is checked, not assumed.</p>
""",
 'case': {'title': 'After the flood in Nueva Ecija',
          'html': """
<p>Tuesday, 3 p.m., the medicine ward of a provincial hospital in Cabanatuan City, ten days after a typhoon flooded the rice fields of Nueva Ecija. Mr. Romeo Dizon, 48, a farmer, waded in floodwater for three days to save his seedlings. Five days ago he developed fever, severe calf pain and red eyes. Today he is yellow. He weighs about 62 kg.</p>
<p>His blood pressure is 100/60 mm Hg, pulse 108 per minute, temperature 38.4 &deg;C, oxygen saturation 95% on room air. His creatinine is 4.6 mg/dL. The only earlier value, from a health center check two years ago, was 0.9 mg/dL. Potassium is 3.3 mmol/L, total bilirubin 9.8 mg/dL, platelets 42,000 per microliter. The urine bag holds 280 mL since admission 24 hours ago. The medical intern, Dr. Kristine Villanueva, notices that he has received two doses of an aminoglycoside started in the emergency room and an injectable painkiller from the nonsteroidal anti-inflammatory drug (NSAID) group for his myalgia.</p>
<p>The hospital has one hemodialysis machine, already booked for maintenance patients, and no intensive care bed tonight. His wife asks whether he will need &ldquo;dialysis forever.&rdquo; The resident, Dr. Paolo Reyes, calls the nephrology fellow at the referral center in Manila.</p>
""",
          'questions': ['What stage of AKI is this, and what should the intern report in the first hour?',
                        'What is the likely cause, what else must be excluded, and what is the monitored plan?',
                        'When does he need kidney replacement or transfer, and what happens after he goes home?']},
 'sections': [
  ('definitions', 'Definitions', 'Defining AKI and AKD, and the baseline problem', """
<p>The KDIGO 2012 guideline unified earlier systems into one definition and one staging table. AKI is any of: a rise in serum creatinine of 0.3 mg/dL or more within 48 hours; a rise to 1.5 times baseline or more, known or presumed to have occurred within the prior 7 days; or urine output below 0.5 mL/kg/h for 6 hours. The definition and the staging are ungraded statements, and KDIGO adds that the cause should be determined whenever possible (also not graded).[[ntr09_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Creatinine</th><th>Urine output</th></tr></thead>
<tbody>
<tr><td>1</td><td>1.5 to 1.9 times baseline, or a rise of 0.3 mg/dL or more</td><td>Below 0.5 mL/kg/h for 6 to 12 hours</td></tr>
<tr><td>2</td><td>2.0 to 2.9 times baseline</td><td>Below 0.5 mL/kg/h for 12 hours or more</td></tr>
<tr><td>3</td><td>3.0 times baseline or more, or creatinine 4.0 mg/dL or more, or start of KRT</td><td>Below 0.3 mL/kg/h for 24 hours or more, or no urine for 12 hours or more</td></tr>
</tbody></table></div>
<p>Use the worse of the two criteria. A patient staged 1 by creatinine and 3 by urine output is stage 3. Urine output is the criterion most often lost, because it needs a measured bag, a recorded weight and a person who divides one by the other. That person is usually the intern.</p>
<h3>The baseline problem</h3>
<p>Every ratio needs a baseline, and many Philippine patients have none, or have one on a phone photo from a clinic two years ago. Write down which value you used and why: a recent outpatient creatinine, the lowest value during this admission, or an estimate. A low admission value that later rises is AKI; a high admission value that later falls was also AKI, recognized late. In a patient with little muscle, a &ldquo;normal&rdquo; creatinine can hide a large loss of filtration, and a doubling from 0.5 to 1.0 mg/dL is stage 2 even though both numbers look harmless.</p>
<h3>From AKI to AKD</h3>
<p>AKI describes the first 7 days. CKD needs more than 90 days. Between them sits acute kidney disease (AKD). The Acute Disease Quality Initiative (ADQI) 16 workgroup proposed AKD as the course after AKI when kidney dysfunction persists, with its own staging and management, so that patients in that window are not forgotten.[[ntr09_3]] KDIGO 2012 already asked clinicians to evaluate patients 3 months after AKI for resolution, new CKD or worsening of existing CKD (not graded).[[ntr09_1]]</p>
{{fig:ntr09_a}}
<p><strong>The 2026 draft.</strong> KDIGO released a public-review draft of a 2026 AKI and AKD guideline, its first major update since 2012. It frames AKI and AKD as a continuum of injury, recovery and risk for CKD, covers risk prediction, biomarkers and electronic alerts, nephrotoxin stewardship, KRT and follow-up, and states that updated definitions incorporate both functional criteria and structural biomarkers.[[ntr09_2]] It is a draft. Until KDIGO publishes a final version, the 2012 guideline remains the final guideline, and you should not quote draft wording as a recommendation on a chart.</p>
{{key:Stage by creatinine and by urine output, take the worse, and write the baseline you used next to the stage.}}
"""),
  ('causes', 'Causes', 'Finding the mechanism, not just the label', """
<p>The old split into prerenal, intrinsic and postrenal is useful only if you treat it as a question about mechanism. Ask three things in order: is the kidney underperfused, is the tubule or interstitium injured, and is the outflow blocked? In a hospitalized patient, more than one is often true.</p>
<div class="table-wrap"><table>
<thead><tr><th>Mechanism</th><th>What breaks</th><th>What you see at the bedside</th><th>First move</th></tr></thead>
<tbody>
<tr><td>Low perfusion</td><td>Volume loss, capillary leak, low cardiac output or vasodilation lowers glomerular pressure</td><td>Thirst, low jugular venous pressure, orthostasis, tachycardia, concentrated urine</td><td>Assess volume honestly; treat shock; review blood pressure medicines</td></tr>
<tr><td>Altered glomerular hemodynamics</td><td>NSAIDs block afferent dilation; angiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) block efferent tone</td><td>Creatinine rises after a new drug or during dehydration</td><td>Medicine reconciliation; hold the culprits during the illness</td></tr>
<tr><td>Tubular injury</td><td>Ischemia, aminoglycosides, contrast, pigment (myoglobin, hemoglobin), sepsis</td><td>Muddy brown casts, urine sodium not low, creatinine still rising after perfusion is restored</td><td>Stop toxins; check creatine kinase; sediment</td></tr>
<tr><td>Interstitial or glomerular injury</td><td>Drug allergy, infection, vasculitis, glomerulonephritis</td><td>Rash, eosinophils, white cell casts; or blood and protein with red cell casts</td><td>Urinalysis and microscopy; escalate red cell casts the same day</td></tr>
<tr><td>Obstruction</td><td>Prostate, stones, clot, a blocked catheter, pelvic tumor</td><td>Palpable bladder, anuria, flank pain, a urinary catheter that has stopped draining</td><td>Flush or replace the catheter; bladder scan; kidney ultrasound</td></tr>
</tbody></table></div>
<h3>Indices and their traps</h3>
<p>The fractional excretion of sodium (FENa) and of urea (FEUrea) can support the impression of low perfusion, but they were derived in selected patients and fail in common situations: diuretics raise FENa, CKD blunts concentrating ability, and pigment and contrast injury can produce a low FENa with real tubular damage. Use them as one clue among several, never as a verdict. The site&rsquo;s FENa/FEUrea calculator shows the arithmetic; the interpretation belongs to the whole picture.</p>
<h3>Philippine exposures to ask about</h3>
<p>Ask every AKI patient about floodwater or farm work in the past month, fever with myalgia, travel to a malaria area, snake or insect bites, heavy exertion in heat, over-the-counter painkillers for &ldquo;rayuma,&rdquo; herbal teas and &ldquo;kidney cleanse&rdquo; products, and recent contrast scans. Tropical AKI is shaped by infections, animal and plant toxins, herbal medicines and environmental heat, all of which are preventable or treatable when recognized early.[[ntr09_5]] Write the answers in the note even when they are negative; a negative exposure history is information the next doctor will need.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children are staged with the same KDIGO table, but creatinine is lower and rises with growth, so pediatric teams also use the pediatric modification of the Risk, Injury, Failure, Loss, End-stage criteria (pRIFLE), based on estimated creatinine clearance. Neonatal AKI has its own definitions because a newborn&rsquo;s creatinine first reflects the mother&rsquo;s. In a Philippine series of 86 children with leptospirosis, 62% were oliguric and peritoneal dialysis was started in 36% of the oliguric group.[[ntr09_14]] See <a href="attending-pediatric-nephrologist-15-pediatric-aki.html">Attending Pediatric Nephrologist, Module 15</a> and <a href="attending-pediatric-nephrologist-14-neonatal-kidney-aki.html">Module 14</a>.</div>
{{key:Ask three questions for every AKI: is the kidney underperfused, is it injured, is it blocked? Then ask what in this patient&rsquo;s week explains it.}}
"""),
  ('tropical', 'Tropical AKI', 'Tropical AKI: leptospirosis, dengue, malaria, snakebite and heat', """
<p>The Philippines carries the full burden of tropical AKI. Leptospirosis rises after every typhoon season. Dengue fills pediatric and adult wards each rainy season. Severe malaria persists in a few provinces, mostly in Palawan. Snakebite reaches rural emergency rooms, and heat illness is rising with longer hot seasons. Each injures the kidney by its own mechanism, and the mechanism decides what you watch for.[[ntr09_5]]</p>
<h3>Leptospirosis</h3>
<p>Leptospires enter through broken skin or mucosa from water contaminated by rat urine. In the kidney they reach the proximal tubule and the interstitium. The result is tubulointerstitial nephritis with tubular dysfunction, often with a urine output that is preserved early, potassium wasting rather than retention, and a creatinine that climbs while the patient still passes urine. Hypotension, bleeding, jaundice and muscle injury add ischemic and pigment injury on top. The severe form, with jaundice, kidney failure and bleeding, is Weil disease, and pulmonary hemorrhage is its most lethal complication.[[ntr09_5]]</p>
{{fig:ntr09_b}}
<p>The Philippine data are sobering. After the September 2009 typhoon flooded Metro Manila, a hospital-based investigation at San Lazaro Hospital reviewed 471 hospitalized patients with leptospirosis. Fifty-one died, a case-fatality ratio of 10.8%. The main causes of death were pulmonary hemorrhage (35% of deaths), acute respiratory distress or respiratory failure (24%) and acute renal failure (20%). Older age, jaundice, anuria and hemoptysis at admission were associated with death; anuria carried a risk ratio of 4.17, and a creatinine above 3.0 mg/dL a risk ratio of 3.27. Delayed antimicrobial treatment was also associated with death. Only one patient received peritoneal dialysis and seven were transferred elsewhere for hemodialysis, and the authors suggested that wider access to peritoneal dialysis might reduce deaths.[[ntr09_6]] The study was observational, from one referral hospital, and only a third of patients had laboratory testing, so it describes associations, not proof that earlier dialysis would have saved those lives.</p>
<p>The Philippine clinical practice guideline on leptospirosis lists oliguria or anuria among its criteria for hospital admission, allows outpatient care only for patients with good urine output, and names oliguric hyperkalemic acute renal failure among the features associated with death.[[ntr09_7]] Follow your hospital&rsquo;s current leptospirosis protocol for antimicrobials and for any adjunctive therapy; this module gives no doses.</p>
<h3>Dengue</h3>
<p>Dengue injures the kidney mainly through the critical phase of plasma leakage: intravascular volume falls, shock lowers perfusion, and late or excessive fluid replacement swings the patient into overload. Rhabdomyolysis, hemolysis and direct viral or immune injury add to it. A meta-analysis of 37 observational studies with 21,764 patients found a pooled AKI prevalence of 8% among people with dengue, with high heterogeneity across studies.[[ntr09_8]] Module 5 teaches the fluid phases; here, remember that the kidney in dengue is usually a perfusion problem first, and that the day the leak stops is the day fluid becomes a hazard.</p>
<h3>Severe malaria</h3>
<p>In falciparum malaria, parasitized red cells stick to small vessels and impair the microcirculation, systemic inflammation and endothelial activation follow, and hemolysis releases cell-free hemoglobin that drives oxidative injury to the tubules. AKI is an independent predictor of death in adults and children with severe malaria. Prompt diagnosis and artesunate are the core of treatment, and a review of the field notes that kidney replacement therapy (RRT) reduces mortality in malaria AKI but that delayed diagnosis remains a problem.[[ntr09_9]] Ask about travel to southern Palawan or other endemic areas in any febrile patient with jaundice and a rising creatinine.</p>
<h3>Snakebite</h3>
<p>Snakebite AKI comes mainly from vipers, whose venom causes coagulopathy, hemolysis, muscle injury and direct tubular toxicity.[[ntr09_10]] The best known Philippine species, the Philippine cobra, causes mainly neurotoxic envenoming: ptosis, weakness and respiratory paralysis.[[ntr09_11]] So in a Philippine snakebite, the airway and the antivenom usually come before the kidney, but a bitten patient with bleeding, dark urine or a rising creatinine needs the same AKI workup as any other.</p>
<h3>Heat</h3>
<p>Heat illness injures the kidney through volume depletion, rhabdomyolysis and direct heat stress, and laborers, athletes and the elderly in non-air-conditioned homes carry most of the risk.[[ntr09_5]] Check creatine kinase in any heat casualty with a rising creatinine, and use the McMahon score to estimate the risk of kidney replacement in rhabdomyolysis.</p>
<div class="table-wrap"><table>
<thead><tr><th>Condition</th><th>Main kidney mechanism</th><th>Clue on your ward</th><th>What it changes</th></tr></thead>
<tbody>
<tr><td>Leptospirosis</td><td>Tubulointerstitial nephritis, potassium wasting, plus ischemia and pigment</td><td>Floodwater exposure, calf pain, red eyes, jaundice, low potassium with high creatinine</td><td>Early antimicrobials; watch for anuria and lung bleeding; plan dialysis access early</td></tr>
<tr><td>Dengue</td><td>Capillary leak and shock, then overload</td><td>Day 3 to 6 of fever, rising hematocrit, falling platelets</td><td>Phase-guided fluids; daily weights; stop fluids when the leak stops</td></tr>
<tr><td>Severe malaria</td><td>Microvascular sequestration, hemolysis, oxidative injury</td><td>Travel to an endemic area, jaundice, dark urine, anemia</td><td>Blood film or rapid test now; artesunate; early KRT if needed</td></tr>
<tr><td>Snakebite (viper)</td><td>Coagulopathy, hemolysis, myolysis, direct toxicity</td><td>Bleeding gums, prolonged clotting, dark urine</td><td>Antivenom per protocol; coagulation and creatinine every day</td></tr>
<tr><td>Heat illness</td><td>Volume loss, rhabdomyolysis</td><td>Laborer or athlete, confusion, very high temperature, cola urine</td><td>Cooling; creatine kinase; volume repletion with monitoring</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist when, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>Urine output stays below 0.3 mL/kg/h for 12 hours or the patient becomes anuric</li><li>Potassium is high with electrocardiogram (ECG) changes, or acidosis or pulmonary edema does not respond to first measures</li><li>A leptospirosis patient coughs blood, desaturates or needs oxygen</li><li>Confusion, seizures or a pericardial rub suggest uremia</li><li>Your hospital cannot dialyze tonight and the patient is heading toward any of the above</li></ul>}}
{{key:In a febrile patient with AKI after a flood, think leptospirosis first, count the urine every shift, check the potassium both ways, and arrange the dialysis route before the patient needs it.}}
"""),
  ('kidney-protect', 'Kidney protection', 'Protecting the injured kidney: fluids, drugs and contrast', """
<p>An injured kidney has lost its reserve. A dose of a drug, a scan or an hour of hypotension that a healthy kidney ignores can push it from stage 1 to stage 3. Protection means removing every avoidable second hit.</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2012 statement</th><th>Grade</th><th>What it means on your ward</th></tr></thead>
<tbody>
<tr><td>Stratify patients for AKI risk by their susceptibilities and exposures</td><td>1B</td><td>Know who on your list is at risk before the creatinine moves</td></tr>
<tr><td>Isotonic crystalloids rather than colloids (albumin or starches) for volume expansion, in the absence of hemorrhagic shock</td><td>2B</td><td>Crystalloid first; reassess after every portion</td></tr>
<tr><td>Vasopressors together with fluids in vasomotor shock</td><td>1C</td><td>Do not drown a vasodilated patient to raise the pressure</td></tr>
<tr><td>Do not use diuretics to prevent AKI</td><td>1B</td><td>A diuretic makes urine, not kidney function</td></tr>
<tr><td>Do not use diuretics to treat AKI, except to manage volume overload</td><td>2C</td><td>Use them for the lungs, not for the creatinine</td></tr>
<tr><td>Do not use low-dose dopamine to prevent or treat AKI</td><td>1A</td><td>&ldquo;Renal-dose dopamine&rdquo; has no place</td></tr>
<tr><td>Avoid aminoglycosides unless no suitable, less nephrotoxic alternative exists</td><td>2A</td><td>Ask whether the aminoglycoside is still needed today</td></tr>
<tr><td>Iso-osmolar or low-osmolar iodinated contrast rather than high-osmolar</td><td>1B</td><td>Check what your radiology department stocks</td></tr>
<tr><td>Intravenous volume expansion with isotonic sodium chloride or sodium bicarbonate in patients at increased risk of contrast injury</td><td>1A</td><td>Plan prophylaxis with the radiologist, per protocol</td></tr>
<tr><td>Not oral fluids alone in patients at increased risk of contrast injury</td><td>1C</td><td>&ldquo;Drink more water&rdquo; is not prophylaxis</td></tr>
</tbody></table></div>
<p>All rows are from the KDIGO 2012 guideline, with its own grades.[[ntr09_1]]</p>
<h3>Contrast: the risk has been overstated</h3>
<p>Older studies counted every creatinine rise after a scan as contrast injury. The American College of Radiology (ACR) and National Kidney Foundation (NKF) consensus separates contrast-induced AKI (caused by the contrast) from contrast-associated AKI (coincident with it) and concludes that the risk from intravenous iodinated contrast has been overstated. It advises prophylaxis with intravenous normal saline for patients with AKI or an estimated glomerular filtration rate (eGFR) below 30 mL/min/1.73 m&sup2; who are not on maintenance dialysis, and leaves patients with an eGFR of 30 to 44 at the ordering clinician&rsquo;s discretion in high-risk circumstances.[[ntr09_12]] The practical lesson: do not deny a patient a scan that will change management, such as a computed tomography (CT) scan for suspected obstruction or abscess, because of fear of contrast. Protect the patient with timing, volume and the lowest effective dose instead.</p>
<h3>Stewardship works</h3>
<p>A pediatric hospital in the United States screened its electronic records every day for children receiving an intravenous aminoglycoside for more than 3 days or 3 or more nephrotoxins at once, and pharmacists then recommended daily creatinine monitoring. Over 43 months the exposure rate fell by 38% (from 11.63 to 7.24 exposures per 1,000 patient-days) and the AKI rate by 64% (from 2.96 to 1.06 episodes per 1,000 patient-days). The authors estimated 398 AKI episodes avoided.[[ntr09_13]] It was a quality improvement project without a control group, but it shows that a list and a daily habit change outcomes.</p>
<div class="table-wrap"><table>
<thead><tr><th>Medicine group</th><th>How it harms the injured kidney</th><th>What you propose</th></tr></thead>
<tbody>
<tr><td>NSAIDs, including over-the-counter and injectable painkillers</td><td>Remove prostaglandin dilation of the afferent arteriole</td><td>Stop; use other analgesia per formulary</td></tr>
<tr><td>ACE inhibitors, ARBs, diuretics</td><td>Lower glomerular pressure or volume during illness</td><td>Hold during the acute illness; plan who restarts them</td></tr>
<tr><td>Metformin, sodium-glucose cotransporter 2 (SGLT2) inhibitors</td><td>Accumulation or ketoacidosis risk while sick</td><td>Hold per sick-day rules; restart when eating and stable</td></tr>
<tr><td>Aminoglycosides, vancomycin, amphotericin</td><td>Direct tubular toxicity</td><td>Review the indication daily; use levels and kidney-adjusted dosing per pharmacy</td></tr>
<tr><td>Herbal and &ldquo;kidney cleanse&rdquo; products</td><td>Unknown ingredients, some directly nephrotoxic</td><td>Ask, record the product name, ask the family to bring it</td></tr>
</tbody></table></div>
{{key:Every day an AKI patient is on your list, read the medicine chart for nephrotoxins and write what you stopped, what you held and why.}}
"""),
  ('recovery', 'Recovery and follow-up', 'Support, recovery and life after AKI', """
<h3>When the kidney needs support</h3>
<p>KDIGO 2012 advises starting kidney replacement therapy emergently when life-threatening changes in fluid, electrolyte and acid-base balance exist, and considering the broader clinical context, the conditions that can be modified with KRT and the trends of laboratory tests rather than a single creatinine or urea threshold (both not graded).[[ntr09_1]] In practice, the indications are refractory hyperkalemia, refractory acidosis, pulmonary edema that diuretics cannot fix, uremic complications such as pericarditis or encephalopathy, and certain poisonings. Module 10 covers timing trials, modality and dose. Here the point is the province: a patient who will need dialysis in 24 hours needs the decision about transfer, access and modality today, because the road to Manila or to the next dialysis center is long and the typhoon may close it.</p>
<p><strong>Biomarkers.</strong> Urine and blood markers of tubular stress and injury can detect damage before creatinine rises. The KDIGO 2026 draft folds structural biomarkers into its definitions,[[ntr09_2]] but most Philippine hospitals cannot measure them, and the draft is not final. For now, a measured urine output, a repeated creatinine and a urine sediment remain your biomarkers.</p>
<h3>Recovery is a process</h3>
<p>Recovery is not a single day. The creatinine falls, but the nadir may settle above the old baseline, proteinuria may persist, and blood pressure may rise. ADQI 16 described AKD to cover exactly this window between 7 and 90 days, with staging and management of its own.[[ntr09_3]] A patient discharged with &ldquo;improving creatinine&rdquo; and no plan is lost to follow-up in this window.</p>
<p>The long-term risk is real. A meta-analysis of 13 cohort studies found pooled incidence rates of 25.8 CKD events and 8.6 kidney failure events per 100 person-years after AKI. Compared with patients without AKI, those with AKI had a pooled adjusted hazard ratio of 8.8 for CKD, 3.1 for kidney failure and 2.0 for death. The risk was graded by AKI severity: for CKD, about 2.0 after mild AKI, 3.3 after moderate AKI and 28.2 after severe AKI.[[ntr09_4]] All studies were retrospective and observational, heterogeneity was high, and residual confounding is likely, so these numbers show that AKI marks a patient at risk; they do not prove that preventing AKI prevents CKD.</p>
{{flow:Post-AKI follow-up plan|Before discharge::Record the peak creatinine, the stage, the cause, the discharge creatinine and whether dialysis was needed. List every medicine held and who will restart it.|Within 1 to 2 weeks::Creatinine, potassium, blood pressure and weight at the nearest clinic or health center. Restart held medicines one at a time, per the attending.|At 3 months::Creatinine with eGFR, urine albumin-to-creatinine ratio, blood pressure. Decide: recovered, AKD resolving, or new or worse CKD (KDIGO 2012, not graded).|After 3 months::If eGFR or albuminuria is abnormal, manage and stage as CKD (Module 11). If recovered, tell the patient that AKI raises lifetime risk and to avoid NSAIDs and unneeded herbal products.}}
<p><strong>Philippine reality.</strong> Many patients go home to a town with no nephrologist and pay out of pocket for each laboratory test. Give the patient and family a written card with the diagnosis, the peak and discharge creatinine, the date of the next test and the name of the doctor who will read it. Use the post-AKI follow-up calculator to set the schedule, and send the summary with the patient, not only in the chart.</p>
{{key:No AKI patient leaves without a written plan: the peak and discharge creatinine, the medicines held, the date of the next test, and who will look at the 3-month result.}}
"""),
 ],
 'debrief': [
  """<p><strong>Stage and first hour.</strong> His creatinine is about five times his old baseline and above 4.0 mg/dL, so he is stage 3 by creatinine. His 280 mL over 24 hours in a 62-kg man is about 0.19 mL/kg/h, below 0.3 for 24 hours, so he is also stage 3 by urine output. Dr. Villanueva should report the stage with the baseline used (the health center value, with its date), the measured urine output, the floodwater exposure and timeline, the jaundice and low platelets, the low potassium, and the two nephrotoxins already given. She asks for an hourly urine record and daily weights and flags the aminoglycoside and the NSAID for the resident.</p>""",
  """<p><strong>Cause and plan.</strong> Floodwater, fever, calf pain, conjunctival suffusion, jaundice and AKI with a low potassium form the classic picture of severe leptospirosis, Weil disease. The differential still includes dengue, severe malaria if he traveled, sepsis from another source, and rhabdomyolysis, and obstruction must be excluded with a bladder scan or ultrasound. Dr. Reyes asks for creatine kinase, a urinalysis with sediment, a blood film or malaria test if travel fits, dengue tests, blood gas and chest film, and starts the leptospirosis antimicrobial per protocol. He stops the NSAID, asks whether the aminoglycoside is needed now that the likely cause is known, assesses volume carefully because the patient is tachycardic and hypotensive but may leak into his lungs, and writes the triggers for calling the attending.</p>""",
  """<p><strong>Support, transfer and after.</strong> He has stage 3 AKI with oliguria, jaundice and low platelets: features linked with death in the 2009 Manila outbreak. He does not yet have refractory hyperkalemia, acidosis or pulmonary edema, but he is heading toward needing dialysis in a hospital whose only machine is booked. The fellow and the attending decide on early transfer to a center that can dialyze and ventilate, or acute peritoneal dialysis if transfer is impossible. To his wife, the fellow says that most patients who survive leptospirosis recover kidney function, that recovery is checked, not assumed, and that he will need a creatinine within two weeks and again at three months.</p>""",
 ],
 'skills': {'title': 'Staging and planning an AKI on the ward',
            'intro': 'Complete with your resident, fellow or attending on a real or simulated patient. Sign-off is local.',
            'items': [
             ('Stages AKI by both KDIGO creatinine and urine output criteria, states the baseline used, and calculates mL/kg/h correctly', False),
             ('Takes a tropical exposure history (floodwater, fever, travel, bites, heat, herbal products, NSAIDs) and documents negatives', False),
             ('Presents a mechanism-based differential (perfusion, tubular or interstitial injury, obstruction) with the tests that separate them', False),
             ('Reconciles the medicine chart and lists every nephrotoxin stopped or held with the reason', False),
             ('States the emergency indications for kidney replacement and the local transfer or acute peritoneal dialysis route', False),
             ('Writes a discharge follow-up plan with peak and discharge creatinine, held medicines and a 3-month review date', False)],
            'placement': 'Medicine ward, emergency department or intensive care unit, during a renal or medicine rotation'},
 'quiz': [
  ('A 70-kg man has passed 450 mL of urine over the last 24 hours. His creatinine rose from 1.0 to 1.4 mg/dL over the same day. By KDIGO 2012, what is his stage?',
   ['Stage 1, because the creatinine rose by less than 1.5 times',
    'Stage 3, because urine output has been below 0.3 mL/kg/h for 24 hours, and the worse criterion counts',
    'No AKI, because the creatinine rise is under 0.5 mg/dL',
    'Stage 2, because the urine output is low but not absent'],
   1,
   '450 mL &divide; 70 kg &divide; 24 h is about 0.27 mL/kg/h, below 0.3 for 24 hours: stage 3 by urine output. The creatinine rise of 0.4 mg/dL alone is stage 1, which is why the first option is tempting, but KDIGO stages by the worse criterion. Do the arithmetic before you stage.'),
  ('A farmer with fever, calf pain and jaundice after floodwater exposure has a creatinine of 3.8 mg/dL, good urine output and a potassium of 3.1 mmol/L. Which mechanism best explains this pattern?',
   ['Prerenal azotemia from dehydration alone',
    'Postrenal obstruction from a stone',
    'Leptospiral tubulointerstitial injury with tubular potassium wasting',
    'Glomerulonephritis with red cell casts'],
   2,
   'Leptospirosis targets the proximal tubule and interstitium; urine output can be preserved early and potassium is often low. Dehydration alone would not explain jaundice, calf pain and hypokalemia with a rising creatinine.'),
  ('What is the status of the KDIGO 2026 AKI and AKD guideline as of November 2026, and how should a fellow use it?',
   ['It is final and replaces the 2012 guideline',
    'It is a public-review draft; the 2012 guideline remains final, and draft wording should not be charted as a recommendation',
    'It has been withdrawn',
    'It applies only to children'],
   1,
   'KDIGO released the 2026 guideline as a public-review draft. Its framework, including structural biomarkers in the definitions, is useful for thinking, but the 2012 guideline remains the final guideline until KDIGO publishes otherwise.'),
  ('A 66-year-old woman with an eGFR of 52 mL/min/1.73 m&sup2; and suspected abdominal abscess needs a contrast CT. The team wants to cancel the scan because of kidney risk. What is the best response?',
   ['Cancel the scan; any contrast exposure is too dangerous at this eGFR',
    'Give oral water only and proceed',
    'Proceed if the scan will change management; by the ACR and NKF consensus, routine prophylaxis is advised for AKI or eGFR below 30, not at 52',
    'Use high-osmolar contrast to shorten the scan'],
   2,
   'The ACR-NKF consensus judges the risk of intravenous contrast to have been overstated and advises intravenous saline prophylaxis for AKI or eGFR below 30. Missing an abscess is the larger danger. KDIGO advises against oral fluids alone and against high-osmolar contrast.'),
  ('A man is discharged after dialysis-requiring AKI from sepsis; his creatinine is 1.6 mg/dL, down from a peak of 6.2 and a baseline of 1.0. What does the evidence on long-term outcomes support?',
   ['No follow-up is needed once the creatinine is falling',
    'Follow-up only if he has symptoms',
    'A creatinine and urine albumin check at 3 months, because AKI is associated with later CKD and kidney failure in a graded way',
    'Restart all held medicines at discharge'],
   2,
   'KDIGO 2012 advises evaluation 3 months after AKI (not graded). A meta-analysis of 13 cohorts found an adjusted hazard ratio of 8.8 for CKD after AKI, highest after severe AKI. The data are observational, but they justify a planned check rather than an assumption of recovery.'),
 ],
 'terms': [
  ('ACE', 'Angiotensin-converting enzyme'),
  ('ACR', 'American College of Radiology'),
  ('ADQI', 'Acute Disease Quality Initiative'),
  ('AKD', 'Acute kidney disease'),
  ('AKI', 'Acute kidney injury'),
  ('ARB', 'Angiotensin receptor blocker'),
  ('CKD', 'Chronic kidney disease'),
  ('CT', 'Computed tomography'),
  ('ECG', 'Electrocardiogram'),
  ('eGFR', 'Estimated glomerular filtration rate'),
  ('FENa', 'Fractional excretion of sodium'),
  ('FEUrea', 'Fractional excretion of urea'),
  ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
  ('KRT', 'Kidney replacement therapy'),
  ('NKF', 'National Kidney Foundation'),
  ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
  ('pRIFLE', 'Pediatric modification of the Risk, Injury, Failure, Loss, End-stage criteria'),
  ('SGLT2', 'Sodium-glucose cotransporter 2'),
  ('Weil disease', 'The severe form of leptospirosis, with jaundice, kidney failure and bleeding'),
 ],
 'readings': [('attending-nephrologist-05-aki-and-post-aki-care.html', 'Attending Nephrologist, Module 5: AKI and post-AKI care'),
              ('leptospirosis-nephropathy.html', 'Leptospirosis and the Kidney'),
              ('tropical-infection-aki.html', 'Tropical Infections and Acute Kidney Injury'),
              ('aki-does-not-end-at-discharge.html', 'AKI Does Not End at Discharge')],
 'calcs': ['calc-aki-staging.html', 'calc-leptospirosis-aki-risk.html', 'calc-dengue-aki-risk.html', 'calc-severe-malaria-cam.html',
           'calc-fena-feurea.html', 'calc-mcmahon-rhabdo.html', 'calc-renal-angina-index.html', 'calc-post-aki-followup.html', 'calc-spark-aki.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
