# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 10: Critical care nephrology and kidney replacement in the ICU.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Trial numbers checked
against PubMed abstracts (AKIKI, IDEAL-ICU, STARRT-AKI, AKIKI 2, ATN, RENAL, RICH, Schwenger 2012, Gabriel 2008, Zhang 2015,
Uchino 2009); KDIGO 2012 statements and grades checked against its summary of recommendations; ISPD 2020 adult AKI statements and
grades checked against the PubMed abstract. KDIGO 2026 AKI/AKD treated as a public-review draft. No drug doses. Fictional case."""

MODULE = {
 'image_alt': 'A nephrology fellow and an ICU nurse set up a standard hemodialysis machine beside a ventilated patient in a Philippine intensive care unit, while a resident reviews the monitor.',
 'objectives': [
  '<strong>Intern:</strong> Recognize the urgent indications for kidney replacement therapy (KRT) in a ward or intensive care unit (ICU) patient, from potassium, acid-base, fluid and uremia, and escalate at once with a structured report.',
  '<strong>Resident:</strong> Recognize the urgent and the relative indications for KRT and prepare the patient: venous access, consent, volume and laboratory review, medicine review, and the right bed and machine.',
  '<strong>Fellow:</strong> Choose the timing, modality (continuous kidney replacement therapy [CKRT], sustained low-efficiency dialysis or prolonged intermittent KRT [SLED/PIRRT], intermittent hemodialysis or acute peritoneal dialysis) and anticoagulation, prescribe the dose the guidelines state, and plan liberation from KRT.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the ICU patient whose kidneys have stopped</span>The <strong>intern</strong> reads the potassium, the blood gas and the urine bag first, and must recognize the five numbers that cannot wait. The <strong>resident</strong> prepares: a catheter site, a consent, a machine, a bed, a list of what the dialysis will and will not fix. The <strong>fellow</strong>, with the attending nephrologist, decides whether to start now or wait, which therapy the hospital can actually deliver tonight, how much, with what anticoagulation, and when to stop.</div>
{{plain:Think of kidney replacement as a rented generator during a power outage. When the main line fails, the generator keeps the lights and the refrigerator running. But it is noisy, it costs money every hour, it needs fuel and a technician, and it can start a fire. You switch it on when the outage threatens something that matters, not at the first flicker, and you switch it off as soon as the main line returns.}}
<p>The picture has a limit. A generator does not change whether the main line comes back; KRT does not heal the kidney. It replaces part of what the kidney did: it removes potassium, acid, urea and water, and it can remove some toxins. It does not replace the kidney&rsquo;s endocrine work, it adds its own risks (catheter infection, bleeding, hypotension that can injure a recovering kidney again), and in trials, starting earlier in patients without an urgent need did not save more lives. The decision is therefore a balance: support a failing physiology, without harming the organ you hope will recover.</p>
<p>Physiology sets the urgency. Potassium above the heart&rsquo;s tolerance stops it. Severe acidemia depresses contractility and blunts the response to vasopressors. Fluid that cannot be excreted floods the lungs. Uremic toxins inflame the pericardium and cloud the brain. Each of these has a medical treatment that buys time; KRT is what you use when that time has run out, or will run out before the kidney returns.</p>
{{cards:Key numbers|STARRT-AKI (2,927 analyzed)::Death at 90 days 43.9% accelerated vs 43.7% standard; dialysis dependence among survivors 10.4% vs 6.0%|AKIKI (620 patients)::49% of the delayed group never received KRT|CKRT dose (KDIGO 2012, 1A)::Deliver an effluent volume of 20&ndash;25 mL/kg/h|Intermittent or extended KRT (KDIGO 2012, 1A)::Deliver a Kt/V of 3.9 per week|Acute peritoneal dialysis (ISPD 2020, 1B)::A suitable modality for AKI in all settings}}
<p>Most critically ill patients with acute kidney injury (AKI) never need dialysis, and many who meet a &ldquo;failure&rdquo; stage recover if you wait safely. A few need KRT tonight, and a delay kills them. Your work is to recognize the urgent few, to wait deliberately and watchfully in the rest, to choose the therapy your hospital can deliver well, and to stop it when the kidney comes back.</p>
""",
 'case': {'title': 'One machine in Davao',
          'html': """
<p>Thursday, 9 p.m., the ICU of a tertiary hospital in Davao City. Mr. Arnel Cabahug, 57, a fish vendor with type 2 diabetes, was admitted two days ago with pneumonia and septic shock. He is intubated and on norepinephrine at a moderate and rising rate. He weighs 70 kg.</p>
<p>His creatinine has risen from 1.1 to 3.9 mg/dL. Urine output has been 10 to 15 mL per hour for the last 14 hours despite fluid. Potassium is 6.3 mmol/L and the electrocardiogram (ECG) shows peaked T waves. Arterial pH is 7.16 with a bicarbonate of 11 mmol/L. His cumulative fluid balance is plus 6.2 liters, oxygen needs are rising, and the chest film shows new bilateral haziness.</p>
<p>The medical intern, Dr. Bea Sarmiento, has already asked the nurse for a repeat potassium and called the resident, Dr. Jerome Lim. The hospital has no CKRT machine and no citrate solution. It has one standard hemodialysis machine on wheels, a portable water system, and a dialysis nurse who can stay until 7 a.m. The nephrology fellow, Dr. Maricel Tan, is on her way.</p>
""",
          'questions': ['Does he need KRT now, and what must be done before the first session?',
                        'With one hemodialysis machine and no CKRT, which modality will you choose, and why?',
                        'How will you set the dose and anticoagulation, and how will you know when to stop?']},
 'sections': [
  ('when', 'When to start', 'When to start: the urgent few and the waiting many', """
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline advises starting KRT emergently when life-threatening changes in fluid, electrolyte and acid-base balance exist, and considering the broader clinical context, the conditions that can be modified with KRT and the trends of laboratory tests rather than single urea and creatinine thresholds. Both statements are not graded.[[ntr10_1]] The old mnemonic AEIOU gives the trainee a checklist of the urgent indications.</p>
<div class="table-wrap"><table>
<thead><tr><th>Letter</th><th>What fails</th><th>What you see</th><th>Medical bridge while you call</th></tr></thead>
<tbody>
<tr><td>A &middot; Acidosis</td><td>The kidney cannot regenerate bicarbonate</td><td>Falling pH and bicarbonate, rising vasopressor needs</td><td>Treat the cause; ventilator settings with the ICU team</td></tr>
<tr><td>E &middot; Electrolytes</td><td>Potassium cannot be excreted</td><td>High potassium, ECG changes, arrhythmia</td><td>Membrane stabilization and shift per protocol (Module 7)</td></tr>
<tr><td>I &middot; Intoxication</td><td>A dialyzable toxin accumulates</td><td>Toxic alcohols, lithium, salicylate, some others</td><td>Antidote per poison center; KRT per toxicology guidance</td></tr>
<tr><td>O &middot; Overload</td><td>Water cannot be excreted</td><td>Rising oxygen needs, new infiltrates, positive balance, no response to diuretics</td><td>Stop non-essential fluid; diuretic trial if urine is still made</td></tr>
<tr><td>U &middot; Uremia</td><td>Uremic toxins accumulate</td><td>Pericardial rub, encephalopathy, uremic bleeding</td><td>Do not wait for a number</td></tr>
</tbody></table></div>
<h3>The timing trials</h3>
<p>Four large randomized trials asked whether starting KRT early, in patients with severe AKI but no urgent indication, saves lives.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Patients</th><th>Comparison</th><th>Main result</th></tr></thead>
<tbody>
<tr><td>AKIKI, 2016</td><td>620 ventilated or vasopressor-dependent patients, KDIGO stage 3</td><td>Immediate vs delayed until an urgent criterion or oliguria for more than 72 hours</td><td>Day-60 mortality 48.5% vs 49.7%; 49% of the delayed group never received KRT; catheter bloodstream infection 10% vs 5%[[ntr10_3]]</td></tr>
<tr><td>IDEAL-ICU, 2018</td><td>488 patients with septic shock and failure-stage AKI</td><td>Within 12 hours vs after 48 hours if no recovery</td><td>Stopped for futility; day-90 mortality 58% vs 54%; 38% of the delayed group never needed KRT; 17% met emergency criteria while waiting[[ntr10_4]]</td></tr>
<tr><td>STARRT-AKI, 2020</td><td>3,019 randomized, 2,927 analyzed</td><td>Within 12 hours vs standard (start only for conventional indications or AKI lasting more than 72 hours)</td><td>Day-90 mortality 43.9% vs 43.7%; dialysis dependence among survivors 10.4% vs 6.0%; adverse events 23.0% vs 16.5%[[ntr10_5]]</td></tr>
<tr><td>AKIKI 2, 2021</td><td>278 patients already oliguric for more than 72 hours or with blood urea nitrogen above 112 mg/dL</td><td>Start then vs wait longer, until an urgent indication or blood urea nitrogen 140 mg/dL</td><td>KRT-free days 12 vs 10 (no difference); in a multivariable analysis, the more-delayed strategy had a hazard ratio for death at day 60 of 1.65[[ntr10_6]]</td></tr>
</tbody></table></div>
{{fig:ntr10_b}}
<p>Read them together. An accelerated start did not lower mortality in any trial. In STARRT-AKI it was associated with more dependence on dialysis among survivors: 4.4 more per 100 survivors, roughly one extra dialysis-dependent survivor for every 23 survivors treated early, and 6.5 more patients per 100 with adverse events.[[ntr10_5]] Waiting avoided KRT altogether in about two of every five to one of every two patients in the delayed arms.[[ntr10_3]][[ntr10_4]] AKIKI 2 then showed the limit of waiting: once a patient was oliguric for more than 72 hours or had a markedly high blood urea nitrogen, waiting longer gained nothing and, in its secondary analysis, was associated with more deaths.[[ntr10_6]] That analysis was not the primary outcome and the trial was small, so it is a warning, not a rule.</p>
<p>The practical position: start for an urgent indication; in the rest, wait with a written plan of what you are watching and what will make you start; and do not let &ldquo;watchful waiting&rdquo; drift into neglect. The KDIGO 2026 public-review draft also addresses timing, modality, dose and discontinuation, but it is a draft, and its wording should not be charted as a recommendation.[[ntr10_2]]</p>
<p><strong>Philippine reality.</strong> In a provincial hospital, the question is often not &ldquo;when&rdquo; but &ldquo;where.&rdquo; If your hospital cannot dialyze, the decision to transfer must come before the urgent indication, because the transfer itself takes hours and a typhoon can close the road. Waiting safely needs a machine within reach.</p>
{{call:Stop and call the attending nephrologist now, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>Potassium with ECG changes, or not falling after the protocol&rsquo;s first measures</li><li>pH falling or vasopressor needs climbing with a severe metabolic acidosis</li><li>Rising oxygen needs or new infiltrates with a positive balance and little urine</li><li>Pericardial rub, new confusion or seizures in a uremic patient</li><li>A suspected dialyzable poisoning</li><li>Your hospital cannot start KRT and the patient is moving toward any of the above</li></ul>}}
{{key:Start KRT for the urgent indication, not the creatinine. Everyone else gets a written list of the triggers you are watching, rechecked every shift.}}
"""),
  ('which', 'Which modality', 'Which modality: what the patient needs and what the hospital has', """
<p>Every modality moves blood or peritoneal fluid past a membrane and removes solutes by diffusion, convection or both, and water by ultrafiltration. What differs is the speed. Slow therapies remove the same water over more hours, so the plasma refills from the tissues at a pace the circulation tolerates; fast therapies remove it in hours and can drop the blood pressure of a patient on vasopressors, injuring a kidney that was starting to recover.</p>
{{fig:ntr10_a}}
<div class="table-wrap"><table>
<thead><tr><th>Modality</th><th>How it runs</th><th>Strength</th><th>Cost and limits in the Philippines</th></tr></thead>
<tbody>
<tr><td>CKRT (continuous hemofiltration, hemodialysis or hemodiafiltration)</td><td>24 hours a day on a dedicated machine with bagged fluids</td><td>Gentle fluid and solute removal in unstable patients</td><td>Machine, filters and fluids often unavailable outside large centers; high cost; needs continuous trained nursing</td></tr>
<tr><td>SLED or PIRRT</td><td>Standard hemodialysis machine, run for longer sessions at lower flows</td><td>Much of CKRT&rsquo;s gentleness with equipment most hospitals already own</td><td>Needs treated water, a dialysis nurse for the whole session, and a machine not booked for maintenance patients</td></tr>
<tr><td>Intermittent hemodialysis</td><td>Standard session of a few hours</td><td>Fastest potassium and toxin removal</td><td>Hypotension in shock; large fluid shifts</td></tr>
<tr><td>Acute peritoneal dialysis</td><td>Catheter in the peritoneum; manual or automated exchanges</td><td>No blood circuit, no anticoagulation, no machine needed; gentle</td><td>Slower; needs a catheter, sterile technique and solutions; less suited after abdominal surgery</td></tr>
</tbody></table></div>
<h3>What the guidelines say</h3>
<p>KDIGO 2012 advises using continuous and intermittent KRT as complementary therapies (not graded) and suggests CKRT rather than standard intermittent KRT for hemodynamically unstable patients (2B).[[ntr10_1]] Note the word &ldquo;standard&rdquo;: prolonged intermittent therapy was not what that suggestion compared against.</p>
<p>The International Society for Peritoneal Dialysis (ISPD) 2020 adult guideline states that peritoneal dialysis should be considered a suitable modality for AKI in all settings (1B). It recommends flexible catheters where resources and expertise exist (1B), accepts rigid or improvised catheters in resource-poor settings where they may still be life-saving (1C), finds nephrologist-inserted catheters safe and functional in patients without contraindications (1B), and says nephrologists should be trained and permitted to insert them (practice point). In critically ill patients, especially with liver dysfunction and high lactate, it prefers bicarbonate-containing solutions (1B), with lactate solutions as the alternative where bicarbonate is unavailable (practice point).[[ntr10_10]]</p>
<h3>The evidence for the &ldquo;in-between&rdquo; options</h3>
<p><strong>SLED.</strong> A German randomized trial assigned 232 surgical ICU patients to 12-hour SLED with a batch system or 24-hour continuous venovenous hemofiltration. Mortality at 90 days was 49.6% with SLED and 55.6% with hemofiltration, a difference that was not significant. Hemodynamic stability did not differ; the SLED group had fewer ventilator days, fewer ICU days, fewer transfusions, less nursing time and lower costs.[[ntr10_12]] A meta-analysis of 17 studies found no mortality difference between extended daily dialysis and CKRT in its 7 randomized trials (533 patients; relative risk 0.90, 95% confidence interval 0.74 to 1.11), similar kidney recovery and fluid removal, and a lower mortality with extended dialysis only in observational studies, which the authors warned may reflect selection bias.[[ntr10_13]]</p>
<p><strong>Acute peritoneal dialysis.</strong> A Brazilian trial randomized 120 patients with acute tubular necrosis to high-volume peritoneal dialysis or daily hemodialysis. Mortality (58% vs 53%) and kidney recovery (28% vs 26%) were similar, and peritoneal dialysis was associated with a shorter time to recovery of kidney function.[[ntr10_11]] It was one center, and peritoneal dialysis delivered a lower weekly Kt/V, a dose measure that is itself a surrogate. Still, together with the ISPD statement, it supports acute peritoneal dialysis as a real option, not a last resort, where blood-based therapy is unavailable or unsafe.</p>
<p><strong>Philippine practice.</strong> In many provinces, SLED on the hospital&rsquo;s standard hemodialysis machine and acute peritoneal dialysis are the realistic choices for an unstable patient, because CKRT machines, filters, fluids and citrate are unavailable or unaffordable. That is not second-rate care when it is done well. The fellow&rsquo;s job is to know what the hospital has before the night it is needed: which machine, which water, which nurse, which catheters, which peritoneal solutions.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children need smaller circuits, blood-primed circuits in infants, and weight-based prescriptions, and peritoneal dialysis is often the first choice in infants and in low-resource settings. Fluid overload at the start of CKRT is associated with mortality in pediatric registries. See <a href="attending-pediatric-nephrologist-16-ckrt-picu.html">Attending Pediatric Nephrologist, Module 16</a>.</div>
{{key:Choose the modality the patient&rsquo;s circulation can tolerate and the hospital can deliver all night. A well-run SLED or acute peritoneal dialysis beats a CKRT that stops every few hours.}}
"""),
  ('dose', 'Dose', 'How much: dose, and why more was not better', """
<p>The dose of KRT is a measure of small-solute clearance: effluent volume per kilogram per hour for continuous therapy, weekly Kt/V for intermittent or extended therapy. Both are surrogates. They track urea removal, not survival, and two large trials tested whether more of them helps.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Patients</th><th>More intensive</th><th>Less intensive</th><th>Result</th></tr></thead>
<tbody>
<tr><td>ATN (US Veterans Affairs and National Institutes of Health [VA/NIH]), 2008</td><td>1,124 critically ill with AKI and organ failure or sepsis</td><td>Intermittent or SLED six times a week; continuous at 35 mL/kg/h</td><td>Three times a week; continuous at 20 mL/kg/h</td><td>Day-60 mortality 53.6% vs 51.5%; no difference in recovery; more hypotension during intensive intermittent sessions[[ntr10_7]]</td></tr>
<tr><td>RENAL, 2009</td><td>1,508 critically ill adults with AKI</td><td>Continuous hemodiafiltration at 40 mL/kg/h</td><td>25 mL/kg/h</td><td>Day-90 mortality 44.7% in both groups; hypophosphatemia 65% vs 54%[[ntr10_8]]</td></tr>
</tbody></table></div>
<p>More clearance did not reduce deaths in either trial, and it brought more electrolyte losses and, with intermittent therapy, more hypotension. KDIGO 2012 therefore recommends delivering an effluent volume of 20&ndash;25 mL/kg/h for CKRT (1A) and a Kt/V of 3.9 per week for intermittent or extended KRT (1A), noting that achieving the delivered effluent target usually requires prescribing a higher one (not graded).[[ntr10_1]]</p>
<h3>Prescribed is not delivered</h3>
<p>Filters clot, the circuit stops for scans and procedures, alarms pause the pumps. A prescription that looks correct on paper can deliver much less over 24 hours. Measure what was actually delivered each day: effluent volume collected divided by weight and hours run.</p>
{{formula:<strong>Arithmetic illustration, not a prescription.</strong> CKRT dose (mL/kg/h) = total effluent per hour (mL/h) &divide; weight (kg).<br>A 70-kg patient with an effluent of 1,750 mL/h receives 25 mL/kg/h while the circuit runs. If the circuit runs only 18 of 24 hours, the delivered average is about 19 mL/kg/h.}}
<p><strong>Fluid is a separate decision.</strong> Net ultrafiltration, the water removed, is set apart from the solute dose. In a patient on vasopressors, remove it slowly and adjust it to the blood pressure and the tissue perfusion hour by hour, with the ICU team. The site&rsquo;s CKRT dose, ultrafiltration-rate and flowsheet calculators help you track delivered dose and balance across shifts.</p>
{{key:Prescribe the dose the guideline states, measure what was delivered, and set the fluid goal separately, hour by hour.}}
"""),
  ('anticoag', 'Anticoagulation', 'Keeping the circuit open: citrate, heparin or nothing', """
<p>Blood that touches plastic and membrane starts to clot. A clotted filter stops treatment and loses the blood inside it. Anticoagulation keeps the circuit open, but systemic anticoagulation in a critically ill patient adds bleeding risk, so the choice is a trade.</p>
<p>Citrate works locally. Infused into the blood as it leaves the patient, it binds ionized calcium, and without calcium the clotting cascade stalls inside the circuit. Much of the citrate-calcium complex is removed by the filter, and calcium is replaced before or after the blood returns, so the patient&rsquo;s own clotting is largely untouched. The liver normally metabolizes the citrate that reaches the patient; in severe liver failure or deep shock it can accumulate. Heparin works systemically: it protects the filter by anticoagulating the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2012 statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>For intermittent KRT, use unfractionated or low-molecular-weight heparin rather than other anticoagulants (in patients without increased bleeding risk or contraindication)</td><td>1C</td></tr>
<tr><td>For CKRT, use regional citrate anticoagulation rather than heparin in patients without contraindications for citrate</td><td>2B</td></tr>
<tr><td>In patients with increased bleeding risk, use regional citrate rather than no anticoagulation during CKRT</td><td>2C</td></tr>
<tr><td>In patients with increased bleeding risk, avoid regional heparinization during CKRT</td><td>2C</td></tr>
</tbody></table></div>
<p>All rows are from KDIGO 2012, with its grades.[[ntr10_1]]</p>
<p>The RICH trial in 26 German centers randomized 638 patients receiving CKRT to regional citrate or systemic heparin; 596 completed it before it was stopped early. Median filter life was 47 hours with citrate and 26 hours with heparin. Mortality at 90 days was 51.2% vs 53.6%, a difference that was not statistically significant. Bleeding complications occurred in 5.1% with citrate and 16.9% with heparin, about 12 fewer bleeds per 100 patients.[[ntr10_9]] Filter life is a process outcome; the bleeding difference is one patients feel.</p>
<h3>No anticoagulation</h3>
<p>Where citrate is unavailable and bleeding risk is high, as in leptospirosis with low platelets or dengue, many Philippine units run SLED or intermittent hemodialysis without anticoagulation. Physiology helps the circuit: adequate blood flow, attention to catheter position, and avoiding excessive hemoconcentration in the filter. Expect more clotting, plan for shorter runs, and do not add heparin by reflex when a filter clots in a bleeding patient. Acute peritoneal dialysis needs no anticoagulation at all, which is one more reason to consider it in the bleeding patient.</p>
{{key:Match the anticoagulant to the patient&rsquo;s bleeding risk and to what your hospital stocks; write the choice and the reason in the order.}}
"""),
  ('liberation', 'Liberation', 'Stopping KRT: recognizing the kidney&rsquo;s return', """
<p>KRT should stop when it is no longer required (KDIGO 2012, not graded), and KDIGO suggests not using diuretics to enhance recovery of kidney function or to reduce the duration or frequency of KRT (2B).[[ntr10_1]] Every day on KRT is a day of catheter risk, hypotension risk and cost, so the question &ldquo;can we stop?&rdquo; belongs on every round.</p>
<p>The best bedside signal is urine. In a post hoc analysis of an observational study of 1,006 patients treated with CKRT in 54 ICUs in 23 countries, 529 survived initial therapy. Of these, 313 came off CKRT and did not need KRT again for at least 7 days; their hospital mortality was 28.5% compared with 42.7% in those who needed it again. Urine output in the 24 hours before stopping was the strongest predictor of success (area under the curve 0.808), and its predictive value fell when diuretics were being given (0.671 with diuretics vs 0.845 without).[[ntr10_14]] Spontaneous urine predicts recovery; urine squeezed out by diuretics predicts less.</p>
{{flow:Daily liberation check|Is the original indication gone::Potassium, acid-base and fluid are controlled; uremic signs have settled; shock is resolving.|Is the patient making urine without help::Rising spontaneous urine output over the past 24 hours, before diuretics, is the strongest single signal.|Is the creatinine falling between sessions::For intermittent therapy, a falling pre-session creatinine or urea suggests the kidney is working.|Step down, then pause::CKRT to SLED to intermittent sessions as the circulation allows; then hold the next session and watch.|Watch for the rebound::Potassium, acid-base, volume and urine every shift after the last session. Restart if an urgent indication returns.|Remove the catheter promptly::Every catheter day is infection risk; plan removal once KRT is no longer expected.}}
<p>After liberation, the patient has AKD, not a healed kidney. Hand them to the follow-up plan in Module 9: discharge creatinine, medicines held, a test within two weeks and a review at three months.</p>
{{key:Ask &ldquo;can we stop KRT today?&rdquo; on every round, and let spontaneous urine, not diuretic-driven urine, answer it.}}
"""),
 ],
 'debrief': [
  """<p><strong>Start now, and prepare.</strong> Yes. He has two urgent indications at once: hyperkalemia with ECG changes and pulmonary edema with oliguria in a positive balance, plus a severe metabolic acidemia on rising vasopressors. Dr. Sarmiento was right to repeat the potassium and call at once; the protocol&rsquo;s membrane stabilization and shift measures bridge the hour it takes to start. Dr. Lim prepares a temporary dialysis catheter, ideally in the right internal jugular vein under ultrasound guidance per KDIGO, obtains consent from the family, reviews the platelets and clotting, lists the antibiotics and other medicines that will need dose review, and confirms that the ICU bed can host the machine and its water supply.</p>""",
  """<p><strong>Modality.</strong> He is in shock on rising norepinephrine, so a standard four-hour hemodialysis risks hypotension. With no CKRT available, Dr. Tan chooses SLED on the hospital&rsquo;s standard machine, run longer at lower flows, which gives similar outcomes to CKRT in trials and uses the equipment and nurse the hospital has. If the machine were unavailable or the catheter could not be placed, acute peritoneal dialysis would be the alternative; ISPD 2020 calls it suitable for AKI in all settings (1B). The first session is shaped to the emergency: potassium and acid first, fluid removal slow and titrated to the pressure.</p>""",
  """<p><strong>Dose, anticoagulation and stopping.</strong> Dr. Tan aims for the KDIGO extended-therapy target of a weekly Kt/V of 3.9 (1A), knowing that more did not help in ATN or RENAL, and records what was delivered. With no citrate and a septic patient whose platelets are falling, she runs the session without anticoagulation, accepting a higher risk of circuit clotting, and writes why. Each day the team asks whether the indications have resolved and whether his urine is returning without diuretics. When spontaneous urine rises and potassium and pH stay controlled between sessions, they hold a session, watch for rebound, then remove the catheter and hand him to post-AKI follow-up.</p>""",
 ],
 'skills': {'title': 'Starting and running KRT in the ICU',
            'intro': 'Complete with your fellow or attending nephrologist, in the ICU or in simulation. Sign-off is local.',
            'items': [
             ('Lists the urgent indications for KRT and the medical bridge for each, and escalates with an SBAR report', False),
             ('Summarizes AKIKI, IDEAL-ICU, STARRT-AKI and AKIKI 2 in one sentence each, with the absolute differences', False),
             ('Chooses a modality for a given patient and hospital, naming what SLED/PIRRT and acute peritoneal dialysis need to run safely', False),
             ('States the KDIGO dose targets with grades, calculates delivered dose from a flowsheet, and sets the fluid goal separately', False),
             ('Chooses an anticoagulation strategy for a patient with high bleeding risk and documents the reason', False),
             ('Performs a daily liberation check and writes the plan for stepping down, pausing and catheter removal', False)],
            'placement': 'Intensive care unit, dialysis unit, or simulation laboratory'},
 'quiz': [
  ('On a night shift, a ward patient with AKI has a potassium of 6.9 mmol/L with peaked T waves and a urine output of 5 mL per hour. What should the intern do first?',
   ['Repeat the potassium in the morning',
    'Call the resident or attending now and start the hyperkalemia protocol while the call is made',
    'Order a renal ultrasound and wait for the result',
    'Give a diuretic and recheck in six hours'],
   1,
   'Hyperkalemia with ECG changes is an urgent indication for treatment and possibly KRT. The protocol&rsquo;s first measures bridge the time to dialysis. A diuretic in near-anuria will not fix this quickly, and waiting until morning is dangerous.'),
  ('Before a first KRT session in the ICU, which preparation step does KDIGO 2012 recommend with grade 1A?',
   ['A tunneled cuffed catheter for every patient',
    'Ultrasound guidance for dialysis catheter insertion',
    'Routine diuretic loading to test kidney recovery',
    'Placing the catheter in the subclavian vein first'],
   1,
   'KDIGO recommends ultrasound guidance (1A). It suggests an uncuffed nontunneled catheter to start (2D) and lists the right internal jugular first and the subclavian last among sites (not graded). It suggests not using diuretics to speed recovery (2B).'),
  ('A fellow is asked to explain the STARRT-AKI result to the ICU team. Which summary is most accurate?',
   ['Accelerated KRT lowered 90-day mortality by about 10%',
    'Accelerated KRT did not lower 90-day mortality and was associated with more dialysis dependence among survivors (10.4% vs 6.0%) and more adverse events',
    'The trial was stopped early because accelerated KRT was harmful',
    'Accelerated KRT improved kidney recovery'],
   1,
   'Mortality was 43.9% vs 43.7%. Among 90-day survivors, 10.4% vs 6.0% remained on dialysis, and adverse events were 23.0% vs 16.5%. IDEAL-ICU, not STARRT-AKI, was stopped for futility.'),
  ('A septic patient on norepinephrine needs KRT in a provincial hospital with one standard hemodialysis machine and no CKRT. Which choice is best supported?',
   ['A standard four-hour hemodialysis with full fluid removal',
    'Transfer only, with no therapy until a CKRT machine is found, even if it takes a day',
    'SLED on the standard machine, or acute peritoneal dialysis if blood-based therapy is not feasible',
    'Wait until the creatinine reaches 10 mg/dL'],
   2,
   'SLED gives outcomes similar to CKRT in randomized trials and uses equipment the hospital has; ISPD 2020 calls acute peritoneal dialysis suitable for AKI in all settings (1B). A fast standard session risks hypotension, and waiting a day for a machine or a creatinine number is not justified when indications exist.'),
  ('After five days of SLED, a patient&rsquo;s urine output has risen to 1,100 mL per day without diuretics, potassium and pH are stable, and he is off vasopressors. What is the best next step?',
   ['Continue daily SLED until the creatinine is normal',
    'Start a high-dose diuretic to speed recovery and continue SLED',
    'Hold the next session, monitor for rebound every shift, and plan catheter removal if stable',
    'Switch to CKRT for a gentler finish'],
   2,
   'Spontaneous urine output is the strongest predictor of successful discontinuation; diuretics weaken that signal and KDIGO suggests not using them to enhance recovery (2B). Waiting for a normal creatinine prolongs catheter and hypotension risk.'),
 ],
 'terms': [
  ('AEIOU', 'Acidosis, Electrolytes, Intoxication, Overload, Uremia: the urgent indications for KRT'),
  ('AKD', 'Acute kidney disease'),
  ('AKI', 'Acute kidney injury'),
  ('AKIKI', 'Artificial Kidney Initiation in Kidney Injury (trial)'),
  ('ATN', 'Acute Renal Failure Trial Network (VA/NIH trial of KRT intensity)'),
  ('CKRT', 'Continuous kidney replacement therapy'),
  ('ECG', 'Electrocardiogram'),
  ('ICU', 'Intensive care unit'),
  ('IDEAL-ICU', 'Initiation of Dialysis Early Versus Delayed in the Intensive Care Unit (trial)'),
  ('ISPD', 'International Society for Peritoneal Dialysis'),
  ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
  ('KRT', 'Kidney replacement therapy'),
  ('Kt/V', 'Urea clearance (K) times treatment time (t) divided by urea distribution volume (V); a dose measure'),
  ('PIRRT', 'Prolonged intermittent renal replacement therapy'),
  ('RENAL', 'Randomized Evaluation of Normal versus Augmented Level of renal replacement therapy (trial)'),
  ('RICH', 'Regional citrate versus systemic heparin anticoagulation for CKRT (trial)'),
  ('SBAR', 'Situation, Background, Assessment, Recommendation'),
  ('SLED', 'Sustained low-efficiency dialysis'),
  ('STARRT-AKI', 'Standard versus Accelerated Initiation of Renal Replacement Therapy in Acute Kidney Injury (trial)'),
  ('VA/NIH', 'US Department of Veterans Affairs and National Institutes of Health'),
 ],
 'readings': [('attending-nephrologist-07-acute-krt-icu.html', 'Attending Nephrologist, Module 7: Acute KRT in the ICU'),
              ('attending-nephrologist-08-crrt-delivery.html', 'Attending Nephrologist, Module 8: Delivering CKRT'),
              ('crrt-continuous-renal-replacement-therapy.html', 'Continuous Renal Replacement Therapy'),
              ('aki-icu-dialysis-decisions.html', 'AKI in the ICU: Dialysis Decisions')],
 'calcs': ['calc-crrt-dose.html', 'calc-crrt-uf-rate.html', 'calc-crrt-flowsheet.html', 'calc-vasopressor-inotrope.html',
           'calc-qsofa-sofa.html', 'calc-fluid-overload.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
