# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 23: Pediatric HD prescription: the circuit, the child and adequacy.
Written November 27, 2026 for the Renal Care Academy, in the voice of the Physician on Duty modules and to the medical teaching standard.
Numbers checked against the European Pediatric Dialysis Working Group HD guideline (Fischbach 2005, PMC full text), the 3H study design and
results papers, the daily OL-HDF cohort and IPHN registry abstracts, the infant CKD5 recommendations (PMC full text) and PhilHealth PC 2024-0023.
The blueprint's figure for blood volume per kilogram was not found in a verified source and is not stated. No anticoagulant dose, blood flow
order or ultrafiltration limit in this file is an order; the unit's pediatric protocol sets the prescription."""

MODULE = {
 'image_alt': 'A 6-year-old Filipino boy reads a picture book in a reclining chair in an adult hemodialysis unit while a nurse checks small blood lines and his mother sits beside him.',
 'objectives': [
    'Match the hemodialysis (HD) circuit to the child, keeping extracorporeal volume within about a tenth of the child&rsquo;s blood volume and deciding when to prime with blood or albumin.',
    'Write the elements of a pediatric HD prescription (blood flow, time, dialyzer, target weight, ultrafiltration) and review delivered dialysis, with Kt/V treated as a surrogate.',
    'Interpret the evidence on longer, more frequent and convective dialysis in children, including hemodiafiltration, and plan the child&rsquo;s week around school and growth.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the child&rsquo;s prescriber in an adult unit</span>Many Philippine children '
        'on hemodialysis (HD) are dialyzed in adult units, where the nurses and the physician on duty are skilled with adults and see a child only '
        'occasionally. You write a prescription that the unit can deliver safely with the equipment it has, you tell the team what is different about '
        'this child, and you review the child every month: delivered dialysis, target weight, blood pressure, growth and school.</div>\n'
        '{{plain:A dialysis circuit is a loan of blood. The machine borrows blood, cleans it and returns it. For an adult, the loan is a small fraction '
        'of what the body holds. For a small child, the same circuit can borrow so much that the body runs short while the loan is out.}}\n'
        '<p>The picture has a limit. The blood is not simply missing; it is replaced by the priming fluid the circuit was filled with, and the body '
        'responds by tightening vessels and pulling fluid from the tissues. A small child has less reserve for both, so the volume outside the body, '
        'the speed of fluid removal and the speed of solute removal all matter more than in an adult. And at the end of the session the circuit returns '
        'its contents, which is a fluid load of its own.[[apn23_1]]</p>\n'
        '{{cards:Key numbers|Extracorporeal volume::Total of needles or catheter, tubing and dialyzer should be less than about 10% of the child&rsquo;s '
        'total blood volume [European Pediatric Dialysis Working Group 2005]|Blood flow described::150&ndash;200 mL/min/m&sup2; or 5&ndash;7 mL/min/kg '
        'often sufficient [same source]|Kt/V::A minimum single-session Kt/V of 1.2&ndash;1.4 thought desirable; adequacy tested monthly [same '
        'source]|Target weight::Reassess almost monthly in infants and adolescents [same source]|HDF, Heart and Height (3H) study, non-randomized::190 children, 28 centers; '
        'height standard deviation score (SDS) rose on hemodiafiltration, static on HD}}\n'
        '<p>These are ranges described by an expert group, not orders. Your unit&rsquo;s pediatric protocol and the equipment it actually has set the '
        'prescription for each child.</p>\n'
        '<p>Most school-age children dialyze safely three times a week once the circuit fits them and the fluid plan is realistic. A few, especially '
        'small children and new starters, are harmed by an adult prescription applied to a child&rsquo;s body. Your work is to fit the circuit, the '
        'blood flow and the fluid removal to the child, to judge the prescription by delivered dialysis, blood pressure and growth, and to protect the '
        'school week.</p>\n',
 'case': {'title': 'Adult lines for an 18 kg boy',
          'html': '<p>Miguel Alcantara is 6 years old, weighs 18 kg and is 112 cm tall. He was on peritoneal dialysis (PD) for two years. After a '
                  'third <em>Pseudomonas</em> peritonitis his catheter was removed and his membrane is no longer usable. Yesterday a tunneled '
                  'internal jugular catheter was placed at a tertiary government hospital in Iloilo City, and he is to start maintenance HD at an '
                  'adult freestanding unit near his home in Pavia, Iloilo.</p>\n'
                  '<p>At 7 a.m. the head nurse calls you. The unit has no pediatric blood lines; the smallest dialyzer it stocks is an adult size. '
                  'His blood urea nitrogen is 98 mg/dL, potassium 5.8 mmol/L, and he is 1.2 kg above his last clinic weight with mild periorbital '
                  'edema. The physician on duty suggests a standard 4-hour session at the blood flow used for small adults &ldquo;to catch up.&rdquo; '
                  'His mother, Grace, asks how he can stay in Grade 1 if he must come three mornings a week.</p>\n',
          'questions': ['Is the adult circuit safe for Miguel, and what do you need to know before the first session?',
                        'What will the first sessions look like in principle, and why not a standard adult session?',
                        'What will you review every month once Miguel is established, and how will you protect his school week?']},
 'sections': [
  ('circuit', 'Circuit', 'The circuit against the child&rsquo;s blood volume',
   '<p>The extracorporeal circuit is everything outside the child: the catheter or needles, the arterial and venous blood lines and the '
   'dialyzer&rsquo;s blood compartment. When the session starts, the child&rsquo;s blood fills it and the priming fluid enters the child. The '
   'European Pediatric Dialysis Working Group guideline states that the total extracorporeal blood volume should preferably be less than 10% of the '
   'child&rsquo;s total blood volume, which is essential for small children; a near-normal hemoglobin allows this to be exceeded slightly without '
   'hypotension. It adds that the larger the extracorporeal volume, the larger the volume returned to the child at the end, and that priming with '
   'saline, albumin and sometimes blood should be used in the first sessions in babies and small infants.[[apn23_1]]</p>\n'
   '<p><strong>How to apply it.</strong> Ask the unit for the priming volume of the blood lines and of the dialyzer it proposes, add them, and compare '
   'the total with 10% of the child&rsquo;s estimated blood volume, using the pediatric reference your unit&rsquo;s protocol names. If the circuit is '
   'larger than that limit, you have three choices: find smaller lines and a smaller dialyzer, prime the circuit with albumin or blood as your '
   'protocol directs, or delay HD and transfer the child to a center equipped for children. A school-age child of 18 kg may be within the limit with '
   'pediatric lines and outside it with adult lines; an infant almost always needs pediatric equipment and often a blood prime.</p>\n'
   '<p><strong>Choosing lines and dialyzer.</strong> Lines from neonatal to adolescent sizes exist, and they differ in volume, biocompatibility and '
   'sterilization method.[[apn23_1]] The guideline suggests a synthetic membrane and notes that a high-flux membrane requires ultrapure '
   'dialysate.[[apn23_1]] Choose the dialyzer by blood compartment volume and surface area relative to the child, not by what is on the shelf for '
   'adults.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Component</th><th>Why it matters in a child</th><th>What you ask the unit</th></tr></thead><tbody>'
   '<tr><td>Blood lines</td><td>Adult lines hold far more blood than pediatric lines</td><td>Priming volume of the arterial and venous lines '
   'stocked</td></tr>'
   '<tr><td>Dialyzer</td><td>Blood compartment volume adds to the total; surface area sets clearance</td><td>Priming volume and surface area of the '
   'smallest dialyzer available</td></tr>'
   '<tr><td>Catheter or needles</td><td>Small lumens limit blood flow</td><td>Catheter size and the flow it achieved at insertion</td></tr>'
   '<tr><td>Priming fluid</td><td>Saline dilutes, albumin supports pressure, blood prevents anemia and hypotension</td><td>What the protocol allows and '
   'who orders blood</td></tr>'
   '<tr><td>Rinse-back at the end</td><td>Returning the circuit adds fluid</td><td>How rinse-back volume is counted in the fluid balance</td></tr>'
   '</tbody></table></div>\n'
   '<p><strong>Infants.</strong> The infant recommendations name PD as the preferred therapy and reserve HD as first choice for primary oxalosis and '
   'for infants who cannot have PD (omphalocele, gastroschisis, diaphragmatic hernia, an obliterated peritoneal cavity, bladder exstrophy), or as '
   'short-term rescue after PD catheter problems or abdominal surgery.[[apn23_9]] If an infant needs HD, it belongs in a center with pediatric '
   'equipment and staff.</p>\n'
   '{{key:Add up the circuit before the first session. If it is more than about a tenth of the child&rsquo;s blood volume, change the equipment, '
   'prime it, or move the child.}}\n'
   '<div class="tc-scene"><span class="tc-lab">At an adult unit, first session &middot; fictional</span><p>A 14 kg girl is connected with adult '
   'lines and the smallest adult dialyzer. Twenty minutes in, she is pale and yawning, and her blood pressure has fallen by a third. No fluid has yet '
   'been removed.</p><p>The circuit had taken a large share of her blood volume and replaced it with saline. You stop the session safely, return the '
   'blood, and arrange pediatric lines and a blood prime before her next session.</p><p class="tc-scene-take"><b>What this shows.</b> Early '
   'hypotension in a small child is often the circuit, not the ultrafiltration.</p></div>\n'
   '{{fig:apn23_a}}\n'),
  ('dose', 'Dose', 'Blood flow, time and the urea dose',
   '<p><strong>Blood flow.</strong> Urea clearance rises with blood flow. The pediatric guideline describes an extracorporeal blood flow of '
   '150&ndash;200 mL/min/m&sup2; or 5&ndash;7 mL/min/kg as often sufficient.[[apn23_1]] It is a range for the prescriber, not a target to push '
   'toward; the catheter, the child&rsquo;s blood pressure and the session goal set the actual flow.</p>\n'
   '<p><strong>The first sessions.</strong> A very uremic child is at risk of dialysis disequilibrium: urea falls quickly in the blood but slowly in '
   'the brain, water moves into brain cells, and the child develops headache, vomiting, confusion or seizures. The guideline therefore keeps blood '
   'flow low and the first session short, so that urea clearance in that session is gentle, and builds up over several sessions.[[apn23_1]] Module 25 '
   'covers disequilibrium in detail. &ldquo;Catching up&rdquo; is exactly what the first sessions must not do.</p>\n'
   '<p><strong>Kt/V.</strong> Kt/V is dialyzer urea clearance (K) multiplied by session time (t), divided by the urea distribution volume (V). In '
   'children, V can be estimated from sex-, height- and weight-specific formulas. The guideline describes a minimum Kt/V of 1.2&ndash;1.4 as '
   'desirable, recommends monthly adequacy testing, and warns that dialysis and residual kidney clearance are not equivalent and that the '
   'prescription should be adequate before it is optimized, not only a urea dose.[[apn23_1]] It also asks that Kt/V be read with the normalized '
   'protein catabolic rate, because a well-fed growing child generates more urea.[[apn23_1]] Kt/V is a surrogate: it says nothing about fluid, '
   'phosphate, middle molecules or how the child feels.</p>\n'
   '<p><strong>Access and delivered dose.</strong> In the International Pediatric Hemodialysis Network (IPHN) registry of 552 children from 27 '
   'countries, central venous catheters were the predominant access; arteriovenous fistulas achieved higher blood flow and Kt/V, and catheters had '
   'more dysfunction (2.5 versus 1.2 per 1,000 access-days) and all the access infections (1.3 per 1,000 catheter-days).[[apn23_5]] This is '
   'observational and confounded by age and the expected time to transplant, but it reminds you that the access often limits the dose (Module 24).</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Why delivered dialysis falls</th><th>What you see</th><th>What you check</th></tr></thead><tbody>'
   '<tr><td>Catheter cannot deliver the set flow</td><td>Arterial pressure alarms, flow turned down</td><td>Achieved versus prescribed blood flow, '
   'catheter position, lock practice</td></tr>'
   '<tr><td>Sessions shortened</td><td>Cramps, hypotension, late starts, school or transport</td><td>Minutes delivered per session over the '
   'month</td></tr>'
   '<tr><td>Recirculation</td><td>Kt/V falls with no change in time or flow</td><td>Line reversal, catheter tip</td></tr>'
   '<tr><td>Sampling error</td><td>An unexpected jump or drop</td><td>Timing and technique of the post-dialysis sample</td></tr>'
   '<tr><td>Dialyzer clotting</td><td>Rising venous pressure, dark fibers</td><td>Anticoagulation per protocol, hematocrit</td></tr>'
   '</tbody></table></div>\n'
   '<p><strong>Dialysate and water.</strong> The 2005 guideline describes bicarbonate-buffered dialysate, a glucose concentration at physiological '
   'level, a low dialysate calcium becoming standard, and quality control of the dialysate for bacteria and endotoxin; high-flux membranes and online '
   'HDF need ultrapure dialysate because back-filtration can carry contaminants into the blood.[[apn23_1]] In an adult unit, ask the technical staff '
   'what water and dialysate quality the unit achieves before you ask for high-flux dialysis or HDF for a child (Module 25 covers water safety).</p>\n'
   '{{cards:A complete pediatric HD order|Circuit::Lines, dialyzer, total extracorporeal volume, priming fluid.|Blood side::Access, blood flow for '
   'this phase (first sessions or maintenance), session time, frequency.|Dialysate::Composition per protocol: sodium, potassium, calcium, '
   'bicarbonate; dialysate flow.|Fluid::Target weight and date set, maximum hourly ultrafiltration, what to do if it cannot be reached.|Anticoagulation '
   'and lock::From the pediatric protocol, with the catheter&rsquo;s lumen volumes.|Monitoring::Observations and how often, blood tests, when to call '
   'you and the alert values.}}\n'
   '<p>Write the whole order every time it changes. In an adult unit the physician on duty may meet the child for the first time at 2 a.m.; the '
   'order sheet is your voice in the room.</p>\n'
   '{{key:Start gently, then build. A child&rsquo;s first sessions are short and slow on purpose; adequacy comes over weeks, not in one '
   'morning.}}\n'),
  ('fluid', 'Fluid', 'Ultrafiltration and target weight in a growing child',
   '<p><strong>Target weight.</strong> The guideline defines dry weight as the weight at the end of a regular session below which the child becomes '
   'symptomatically hypotensive. In children it is particularly hard to define: hypotension depends on plasma refilling as well as on the '
   'ultrafiltration rate, body composition changes with age, and in infants and adolescents dry weight must be reassessed almost monthly to follow '
   'rapid growth, and also during growth hormone treatment or illness.[[apn23_1]] A target weight that is not raised as the child grows makes every '
   'session pull off tissue the child has just built, and the child cramps, becomes hypotensive and stops growing.</p>\n'
   '<p><strong>Fluid removal.</strong> The speed of ultrafiltration, relative to the child&rsquo;s size, decides whether refilling keeps up. In the 3H '
   'study, a higher ultrafiltration rate was among the factors associated with higher carotid intima-media thickness and mean arterial pressure '
   'scores.[[apn23_2]] Use your unit&rsquo;s pediatric protocol for the maximum hourly ultrafiltration, and when the weight gain between sessions '
   'cannot be removed within it, lengthen or add sessions rather than pulling harder.</p>\n'
   '<p><strong>Blood pressure and the heart.</strong> In 910 children on HD or hemodiafiltration (HDF) in IPHN, uncontrolled hypertension was '
   'present in 55% of observations and masked hypertension in 24%; 51% of 1,135 echocardiograms showed left ventricular hypertrophy (LVH). Blood pressure '
   'standard deviation scores were associated with interdialytic weight gain, and weight gain was associated with lower urine output and higher '
   'dialysate sodium. Conventional HD rather than HDF was associated with higher mean arterial pressure scores and with LVH '
   'progression.[[apn23_6]] These are associations in a large prospective registry; they point to salt and water balance as the modifiable target.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Sign</th><th>Too wet</th><th>Too dry</th></tr></thead><tbody>'
   '<tr><td>Blood pressure before dialysis</td><td>Above the 95th percentile, rising</td><td>Low, falls further on standing</td></tr>'
   '<tr><td>During the session</td><td>Comfortable; pressure stays high</td><td>Cramps, yawning, vomiting, hypotension near the end</td></tr>'
   '<tr><td>Examination</td><td>Periorbital or leg edema, raised venous pressure, crackles</td><td>Dry mucosa, tired after every session</td></tr>'
   '<tr><td>Weight trend</td><td>Gains between sessions consistently large</td><td>Post-dialysis weight below target, no weight gain over months</td></tr>'
   '<tr><td>Growth</td><td>Weight up, height flat (fluid, not tissue)</td><td>Weight flat, height flat (tissue being removed)</td></tr>'
   '</tbody></table></div>\n'
   '<div class="tc-scene"><span class="tc-lab">At the monthly review &middot; fictional</span><p>A 12-year-old girl on HD for eight months cramps '
   'in the last hour of most sessions. Her target weight has not changed since she started; she has grown 4 cm and her mother says she is eating '
   'better.</p><p>You examine her, review the session blood pressures and raise the target weight. The cramps stop over two weeks.</p><p '
   'class="tc-scene-take"><b>What this shows.</b> In a growing child a fixed target weight is a falling target weight. Review it every month.</p></div>\n'
   '<p><strong>Residual urine.</strong> Many children start HD with some urine output, and it is worth protecting: it widens the fluid allowance, '
   'clears middle molecules and phosphate, and makes each session gentler. In the IPHN cohort, lower urine output was associated with larger weight '
   'gains.[[apn23_6]] Measure it at each monthly review, avoid nephrotoxic drugs and contrast where alternatives exist, and avoid repeated '
   'hypotension during sessions, which can injure what remains.</p>\n'
   '{{key:Reassess the target weight every month, and remove fluid at a speed the child can refill. When the gain is too large, add time, not '
   'speed.}}\n'
   '{{fig:apn23_b}}\n'),
  ('evidence', 'Evidence', 'Longer, more frequent and convective dialysis',
   '<p>Children on dialysis carry cardiovascular disease and growth failure from early childhood. The question is whether more dialysis time or more '
   'convective clearance changes those outcomes.</p>\n'
   '<p><strong>The 3H study.</strong> The HDF, Heart and Height (3H) study was a non-randomized comparison within the IPHN registry. It enrolled 190 '
   'children from 28 centers; 78 on conventional HD and 55 on postdilution online HDF completed one year. The groups were similar for age, dialysis '
   'vintage, access, frequency, blood flow and residual function. Carotid intima-media thickness score rose on HD and stayed static on HDF (HD '
   'associated with a 0.47 higher annualized score on propensity analysis); height score rose on HDF and stayed static on HD; mean arterial pressure '
   'score rose on HD only. Children on HDF had lower &beta;2-microglobulin, parathyroid hormone (PTH) and C-reactive protein, fewer headaches, dizziness or '
   'cramps, and shorter recovery after sessions.[[apn23_2]] At baseline, HDF children achieved a median convection volume of 13.3 L/m&sup2;, and '
   'ultrapure water was available to only 52% of the HD group.[[apn23_3]] The authors state that randomized trials are needed. The study shows an '
   'association with surrogate vascular measures and growth, not fewer deaths or events.</p>\n'
   '<p><strong>Daily online HDF.</strong> In a single-center observational cohort of 15 children already on growth hormone, daily online HDF six days '
   'a week (18 hours weekly) raised mean growth velocity from 3.8 to 14.3 cm per year in the first year, and height score moved from &minus;1.5 to '
   '+0.2 over a mean 20.5 months.[[apn23_4]] It is a small uncontrolled study with an intensive regimen few programs can offer, but it shows what '
   'happens to growth when dialysis is no longer the limit.</p>\n'
   '<p><strong>The bigger picture.</strong> The 2005 guideline already noted that longer or daily dialysis controls phosphate better than conventional '
   'HD and should be considered at least for high-risk children with cardiovascular impairment, and that dialysis in children is a temporary measure '
   'compared with transplantation, which gives the best chance of rehabilitation in education and psychosocial functioning.[[apn23_1]] A review in '
   'The Lancet Child &amp; Adolescent Health notes that morbidity and mortality remain higher on chronic dialysis than after transplantation.[[apn23_7]] '
   'Every HD prescription for a child is also a bridge: keep the transplant work-up moving (Module 26).</p>\n'
   '<p><strong>Coverage.</strong> PhilHealth covers up to 156 HD sessions a year under Circular 2024-0023.[[apn23_8]] That is enough for three '
   'sessions a week, not a ceiling on what a child needs. If a child needs longer or more frequent sessions, write the clinical reason in the chart, '
   'discuss the cost with the family and the social worker, and confirm the benefit on the date of service.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Study</th><th>Design and size</th><th>Main finding</th><th>What it does not show</th></tr></thead>'
   '<tbody><tr><td>3H[[apn23_2]]</td><td>Non-randomized, 190 children, 28 centers</td><td>Vascular scores static and height rising on HDF</td><td>Fewer '
   'deaths or cardiovascular events; causation</td></tr>'
   '<tr><td>Daily online HDF[[apn23_4]]</td><td>Single center, 15 children, uncontrolled</td><td>Catch-up growth on 18 hours a week</td><td>Effect '
   'of HDF versus time; generalizability</td></tr>'
   '<tr><td>IPHN hypertension cohort[[apn23_6]]</td><td>Prospective registry, 910 children</td><td>Weight gain, dialysate sodium and HD (vs HDF) '
   'associated with blood pressure and LVH</td><td>That changing them reduces LVH</td></tr></tbody></table></div>\n'
   '{{key:More time and more convection are associated with better growth and vascular measures in children, in non-randomized studies. Use them to '
   'argue for time, but call them associations.}}\n'),
  ('practice', 'Practice', 'The monthly review and the child&rsquo;s week',
   '<p>On your monthly visit, review the child and the dialysis together. In an adult unit, also review whether the unit can still meet the '
   'child&rsquo;s needs.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>What you review</th><th>Why</th><th>What makes you act</th></tr></thead><tbody>'
   '<tr><td>Delivered minutes and achieved blood flow for every session</td><td>Delivered, not prescribed, dialysis</td><td>Shortened sessions, flow '
   'repeatedly turned down</td></tr>'
   '<tr><td>Kt/V, sampled correctly, with protein catabolic rate</td><td>Surrogate for small-solute dose and intake</td><td>A fall without a change '
   'in prescription</td></tr>'
   '<tr><td>Target weight, weight gains, session blood pressures, symptoms</td><td>Fluid status</td><td>Cramps, hypotension, edema, rising '
   'pressure</td></tr>'
   '<tr><td>Height, weight and growth velocity on the chart</td><td>The outcome that matters</td><td>Flat height, weight that is fluid</td></tr>'
   '<tr><td>Blood pressure percentile; ambulatory monitoring where available</td><td>Masked and uncontrolled hypertension are common</td><td>Pressures '
   'above the 95th percentile</td></tr>'
   '<tr><td>Potassium, phosphate, calcium, PTH, bicarbonate, albumin, hemoglobin, iron studies</td><td>Bone, growth, anemia</td><td>See Module 18 '
   'for anemia and bone</td></tr>'
   '<tr><td>Access function and the lock used</td><td>Access limits the dose</td><td>Alarms, poor flow, fever (Module 24)</td></tr>'
   '<tr><td>School attendance, mood, the family&rsquo;s transport and cost</td><td>Three sessions a week are a heavy load</td><td>Missed school, '
   'skipped sessions</td></tr></tbody></table></div>\n'
   '<p><strong>Anticoagulation and locks.</strong> The circuit needs anticoagulation, usually heparin, and some units use citrate or a heparin-free '
   'technique when bleeding risk is high. The catheter is locked between sessions with heparin or citrate. Doses and lock volumes come from your '
   'unit&rsquo;s pediatric protocol and the catheter&rsquo;s labeled lumen volume, never from the adult default.</p>\n'
   '<p><strong>Anemia and nutrition.</strong> Blood lost in the circuit and in sampling matters more in a small child; keep sampling to what changes '
   'management. A growing child on HD needs protein and energy for growth on top of dialysis losses; the dietitian should see the child at least as '
   'often as your unit protocol requires, and the Kt/V should be read alongside the protein catabolic rate.[[apn23_1]]</p>\n'
   '<p><strong>The child&rsquo;s week.</strong> Three sessions of several hours, plus travel, can take half a school week. Ask the unit for an '
   'afternoon shift after classes, or a Monday-Wednesday-Friday afternoon pattern, and write a letter to the school explaining the absences, the '
   'catheter, and activities to avoid. The pediatric guideline names the school teacher and play therapist as members of the team.[[apn23_1]] In an '
   'adult unit, ask for a chair in a quieter corner, a chaperone, permission for the parent to stay, and something to do: books, a tablet with '
   'headphones, homework.</p>\n'
   '<div class="tc-scene"><span class="tc-lab">In an adult unit, a Saturday session &middot; fictional</span><p>A 10-year-old girl dialyzes between two '
   'elderly men. The nurse on duty has not dialyzed a child before and asks whether the adult resuscitation cart will do; the girl&rsquo;s mother has '
   'been asked to wait outside.</p><p>You speak to the head nurse: a weight-based pediatric resuscitation sheet taped to the cart, the mother allowed '
   'at the chair as the unit&rsquo;s chaperone policy permits, a quieter chair for the next session, and your number on the order sheet.</p><p '
   'class="tc-scene-take"><b>What this shows.</b> An adult unit can dialyze a child safely when someone makes the differences explicit. That someone is '
   'you.</p></div>\n'
   '<p><strong>When the adult unit is not the right place.</strong> Some children should dialyze only where pediatric equipment and staff are '
   'available: infants and small children whose circuit needs a blood prime, children with unstable blood pressure or heart disease, new starters '
   'with very high urea, and any child the unit staff say they cannot safely care for. Say so in writing, and arrange the transfer rather than '
   'asking an adult unit to improvise.</p>\n'
   '{{flow:Monthly pediatric HD review|Delivered dialysis::Minutes, achieved blood flow, alarms; Kt/V sampled correctly.|Fluid::Target weight '
   'reassessed, weight gains, session pressures, cramps.|Growth::Height and weight on the chart; dietitian review.|Blood pressure::Percentile, '
   'medicines, ambulatory monitoring where possible.|Labs::Potassium, phosphate, PTH, hemoglobin, iron, albumin.|Access::Flow, alarms, infection '
   'signs.|Life::School days missed, mood, transport, cost.|Plan::One change at a time, written so the physician on duty can follow it.}}\n'
   '{{key:Review delivered dialysis, target weight, blood pressure and growth every month, and protect the school week. A child on HD is a student '
   'first.}}\n'
   '{{call:<ul><li>Hypotension, pallor or yawning in the first 30 minutes of a session in a small child (circuit volume)</li><li>Headache, vomiting, '
   'confusion or seizure during or after an early session (disequilibrium; Module 25)</li><li>Fever or rigors during dialysis with a catheter '
   '(Module 24)</li><li>Pre-dialysis potassium above the unit&rsquo;s alert value, or electrocardiogram (ECG) changes</li><li>Blood pressure persistently above the 95th '
   'percentile with edema</li></ul>}}\n'
   '{{fig:apn23_c}}\n'),
 ],
 'debrief': [
    '<p><strong>The circuit.</strong> Not until you have added it up. Ask the head nurse for the priming volumes of the adult lines and the smallest '
    'dialyzer, total them, and compare the total with 10% of Miguel&rsquo;s estimated blood volume using your unit&rsquo;s pediatric reference. If '
    'the circuit exceeds that, the options are pediatric lines and a smaller dialyzer from the referring hospital, a prime with albumin or blood as your '
    'protocol directs, or starting HD at the hospital that placed his catheter until the adult unit is equipped. Check his hemoglobin and blood '
    'pressure, confirm the catheter tip position and the flow it achieved, and make sure the unit has a pediatric resuscitation plan.</p>\n',
    '<p><strong>The first sessions.</strong> His urea is high and he has been uremic for days, so a standard adult session at a high blood flow risks '
    'disequilibrium: headache, vomiting, confusion or a seizure. The guideline keeps blood flow low and the first session short, with clearance built '
    'up over several sessions. Treat his potassium and fluid within that frame, removing fluid at a rate his small blood volume can refill. Write '
    'the prescription in full so the physician on duty can follow it, with the blood flow, time, dialyzer, target weight for now, maximum '
    'ultrafiltration, anticoagulation from the pediatric protocol, and when to call you.</p>\n',
    '<p><strong>Every month and every week.</strong> Review delivered minutes and blood flow, Kt/V with protein catabolic rate, his target weight (he '
    'is growing), blood pressure percentile, height and weight on the chart, potassium, phosphate, PTH and hemoglobin, and the catheter. Tell Grace you '
    'will ask the unit for an afternoon shift after classes, write to his school, and keep his transplant work-up moving, because dialysis is the '
    'bridge, not the destination. PhilHealth covers up to 156 sessions a year; if he ever needs more time, you will document why and confirm '
    'coverage.</p>\n'],
 'skills': {'title': 'Pediatric HD prescription: the circuit, the child and adequacy',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Totals the extracorporeal volume of a proposed circuit and compares it with 10% of the child&rsquo;s estimated blood volume', False),
                      ('Writes a complete pediatric HD prescription that a physician on duty in an adult unit can follow', False),
                      ('Reassesses target weight against growth, blood pressure and session symptoms', False),
                      ('Reviews delivered minutes, achieved blood flow and Kt/V together and identifies the cause of a fall', False)],
            'placement': 'Pediatric or adult HD unit with a pediatric patient, or simulation'},
 'quiz': [
    ('What does the European Pediatric Dialysis Working Group guideline advise about extracorporeal volume?',
     ['It should equal the child&rsquo;s plasma volume',
      'It should preferably be less than about 10% of the child&rsquo;s total blood volume',
      'It matters only in adolescents',
      'It is irrelevant if saline is used to prime'],
     1,
     'A larger circuit takes more of a small child&rsquo;s blood volume and returns more fluid at the end. Blood or albumin priming is used in babies and small infants.'),
    ('A very uremic 6-year-old starts HD. Why is a standard adult session at high blood flow unsafe?',
     ['It wastes dialysate',
      'It causes hyperkalemia',
      'Rapid urea removal risks dialysis disequilibrium with cerebral edema',
      'It lowers Kt/V'],
     2,
     'Urea falls faster in blood than in brain; water shifts into brain cells. First sessions are short with low blood flow.'),
    ('A 12-year-old on HD has cramps late in most sessions; she has grown 4 cm since her target weight was set. What is the most likely problem?',
     ['Her target weight is too low for her current size',
      'Her Kt/V is too high',
      'She needs a larger dialyzer',
      'She has a catheter infection'],
     0,
     'In infants and adolescents dry weight should be reassessed almost monthly; a fixed target in a growing child removes tissue, not fluid.'),
    ('What did the 3H study show?',
     ['Hemodiafiltration reduced mortality in a randomized trial',
      'No differences between HD and HDF',
      'HD improved growth more than HDF',
      'In a non-randomized comparison, vascular scores stayed static and height rose on HDF, while they worsened or stayed static on HD'],
     3,
     'The findings are associations with surrogates and growth; the authors call for randomized trials.'),
    ('PhilHealth covers up to 156 HD sessions a year. How should this shape a child&rsquo;s prescription?',
     ['It sets the maximum dialysis a child may receive',
      'It is coverage, not a prescription; prescribe the dialysis the child needs, document the reason, and confirm coverage on the date of service',
      'It means children must dialyze exactly three times a week',
      'It applies only to adults'],
     1,
     'Coverage never becomes clinical frequency. Longer or extra sessions need a documented clinical reason and a cost discussion.'),
 ],
 'terms': [('ECG', 'Electrocardiogram'),
           ('HD', 'Hemodialysis'),
           ('HDF', 'Hemodiafiltration'),
           ('IPHN', 'International Pediatric Hemodialysis Network'),
           ('LVH', 'Left ventricular hypertrophy'),
           ('PD', 'Peritoneal dialysis'),
           ('PTH', 'Parathyroid hormone'),
           ('SDS', 'Standard deviation score'),
           ('3H', 'HDF, Heart and Height (study)')],
 'readings': [('dialysis-prescription.html', 'Understanding Your Dialysis Prescription'),
              ('hemodiafiltration-deep-dive.html', 'Hemodiafiltration Deep Dive: What the Evidence Has Taught Us'),
              ('fluid-management-dialysis.html', 'Fluid Management &amp; Interdialytic Weight Gain: What Happens Between Your Sessions')],
 'calcs': ['calc-dialysis-adequacy-ktv.html', 'calc-bsa.html', 'calc-dialysis-kinetics.html', 'calc-dry-weight-estimator.html', 'calc-pediatric-bp.html'],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
