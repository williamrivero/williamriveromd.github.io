# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 16: CKRT and acute dialysis in the pediatric intensive care unit.
Dialysis module, expanded at Dr. Rivero's request (five sections). Written November 27, 2026 in the voice of the Physician on Duty modules,
to the medical teaching standard, for Philippine practice. Numbers checked against the PubMed abstracts of the ppCRRT registry papers
(Sutherland 2010, Askenazi 2013, Brophy 2005), Goldstein 2001, Garzotto 2014, Brophy 2001, CARPEDIEM (Ronco 2014), Nidus (Coulthard 2014),
Menon 2019, Kwiatkowski 2017 and the ISPD 2020 pediatric acute PD guideline (Nourse 2021); KDIGO 2012 recommendation 5.3.2.2 against the
guideline text. Guideline ranges are quoted as the guideline states them; orders come from the unit's protocol. No doses."""

MODULE = {'image_alt': 'A pediatric nephrologist and a pediatric intensivist stand at the bedside of a ventilated infant connected to a continuous '
                       'kidney replacement therapy machine, reviewing the fluid balance sheet together.',
 'objectives': ['Decide with the intensivist when a critically ill child needs kidney replacement, using fluid overload, the trajectory of the '
                'illness and the ppCRRT evidence with its limits.',
                'Prescribe and supervise continuous kidney replacement therapy (CKRT) in a child: circuit volume against blood volume, blood '
                'priming and its hazards, vascular access, anticoagulation with citrate or heparin, and delivered versus prescribed dose.',
                'Run acute peritoneal dialysis in the PICU and in low-resource settings, and choose between acute PD, conventional CKRT and '
                'small-infant machines for the child in front of you.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; co-owner of the machine</span>In the pediatric intensive care unit '
        '(PICU), the intensivist owns the child and you co-own the kidney replacement. In a Philippine tertiary hospital that usually means '
        'one pediatric nephrologist for several units, a CKRT machine bought for adults, nurses who may run it a few times a year, and acute '
        'peritoneal dialysis (PD) as the dependable fallback. Your duty is to agree on when to start, to write a prescription the nurses can '
        'deliver at 3 a.m., to review it every day with the intensivist, and to say early when the child should go to a center that can do '
        'what yours cannot.</div>\n'
        '{{plain:Think of CKRT as a second, slow river running beside the child&rsquo;s blood. A small stream of blood is diverted, cleaned and '
        'drained of excess water, then returned, hour after hour, so gently that the main river barely notices.}}\n'
        '<p>The picture has a limit. In a small child the second river is not small. An adult circuit can hold a fifth or more of an '
        'infant&rsquo;s blood, so the first minutes of connection can drop the pressure, dilute the blood or, if the circuit is primed with '
        'banked blood, deliver a load of potassium, acid and citrate. And the river is only as good as its flow: a clotted filter, a kinked '
        'catheter or a machine that alarms all night delivers far less than the order says. So CKRT in children is gentle only when it is '
        'sized, primed and watched with care.</p>\n'
        '{{cards:Key numbers|Fluid overload at CKRT start (ppCRRT, 297 children)::Mortality 65.6% with &ge;20%, 43.1% with 10&ndash;20%, 29.4% with '
        '&lt;10%|Children &le;10 kg on CKRT (ppCRRT)::Survival 43% vs 64% in children &gt;10 kg|Extracorporeal volume in infants (Garzotto '
        '2014)::No more than 10&ndash;15% of blood volume|Heparin vs citrate circuit life (ppCRRT)::42.1 vs 44.7 hours; no anticoagulation 27.2 '
        'hours|CARPEDIEM priming volume::Under 30 mL}}\n'
        '<p>Most children who need acute dialysis in a Philippine PICU can be treated with acute PD or with CKRT on the machine you have, if the '
        'prescription is sized to the child. A few, especially infants under 10 kg on high-dose inotropes, need a level of precision your unit '
        'may not have. Your work is to start before overload becomes the disease, to make the circuit safe for the child&rsquo;s size, to '
        'deliver the dose you prescribe, and to know which child should be moved.</p>\n',
 'case': {'title': 'Postoperative day 3, and 2 kg heavier',
          'html': '<p>It is 6 p.m. in the cardiac PICU of a tertiary government heart hospital in Quezon City. Elijah Santiago is 7 months old. '
                  'He weighed 8.0 kg before complete repair of a large ventricular septal defect with a long bypass time. On postoperative day 3 he '
                  'weighs 10.0 kg. He is ventilated, on milrinone and epinephrine, with a mean airway pressure that has crept up all day. His urine '
                  'output on a furosemide infusion has been 0.4 mL/kg per hour for 12 hours. Creatinine has risen from 0.3 to 0.9 mg/dL and '
                  'potassium is 5.8 mmol/L. His mean arterial pressure is adequate on the current infusions, and lactate is normal.</p>\n'
                  '<p>A soft PD catheter was placed in the operating room and has drained serous ascites by gravity. The intensivist wants to start '
                  'CKRT tonight on the unit&rsquo;s machine, whose smallest available set, the nurses tell you, has an extracorporeal volume of about '
                  '150 mL. The cardiac surgeon prefers PD &ldquo;because the catheter is already in.&rdquo; Two of the three night nurses have '
                  'never run acute PD on an infant. Elijah&rsquo;s parents, who traveled from Batangas, ask whether a machine will make him better or '
                  'is a sign that he is dying.</p>\n',
          'questions': ['Does Elijah need kidney replacement now, and why does 25% fluid overload matter?',
                        'CKRT on this machine or acute PD through the surgical catheter: what does each mean for an 8 kg infant, and what has to be '
                        'in place before either starts tonight?',
                        'Who writes and reviews the prescription, and what will you tell his parents?']},
 'sections': [('physiology',
               'Physiology',
               'When and why: fluid overload and the decision to start',
               '<p>A critically ill child accumulates fluid for understandable reasons: resuscitation, drugs and blood products delivered in '
               'volume, nutrition, capillary leak after sepsis or bypass, and kidneys that cannot excrete what is given. Once the circulation is '
               'restored, that fluid stops helping. It sits in the lungs, where it stiffens them and raises ventilator pressures; in the bowel wall, '
               'where it impairs feeding and barrier function; in the myocardium, where it worsens diastolic function; and around the kidney, '
               'where it raises venous and capsular pressure and lowers filtration further. The child is caught in a loop: overload worsens the '
               'kidney, and the failing kidney worsens overload.</p>\n'
               '<p>Percentage fluid overload is the way pediatric teams measure this. The prospective pediatric CRRT (ppCRRT) registry defined it '
               'as fluid in minus fluid out from PICU admission to CKRT initiation, in liters, divided by the admission weight in kilograms, times '
               '100.[[apn16_1]] Daily weights give a similar answer when the scale is reliable; in a ventilated infant with drains, both methods '
               'need care.</p>\n'
               '<p><strong>The evidence.</strong> Goldstein and colleagues first reported that among 21 children on continuous venovenous '
               'hemofiltration, survivors had less fluid overload at initiation than nonsurvivors (16.4% vs 34.0%), even after accounting for '
               'illness severity.[[apn16_2]] The ppCRRT registry then followed 297 children at 13 US centers. Mortality was 65.6% in children who '
               'started CKRT with 20% or more fluid overload, 43.1% with 10% to 20%, and 29.4% with less than 10%. After adjustment for illness '
               'severity, each 1% increase in fluid overload was associated with 3% higher odds of death (adjusted odds ratio 1.03), and 20% or more '
               'carried an adjusted odds ratio of 8.5 (95% confidence interval 2.8 to 25.7).[[apn16_1]] The authors state the limit plainly: this is '
               'an observational association, interventions were not standardized, and it does not prove that starting earlier saves lives. Sicker '
               'children accumulate more fluid and may die for that reason alone.</p>\n'
               '<p>Size adds risk. In the same registry, children weighing 10 kg or less had lower survival than larger children (36 of 84, 43%, vs '
               '166 of 260, 64%). Among the small children, survivors had higher urine output, lower fluid overload and lower illness scores at '
               'initiation; children under 5 kg more often needed blood priming.[[apn16_3]] Again observational, but it describes the infant in this '
               'module&rsquo;s case: small, overloaded, on inotropes, and at the edge of what a standard circuit can do safely.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Indication</th><th>Physiologic reason</th><th>What you see at the bedside</th></tr>'
               '</thead><tbody>'
               '<tr><td>Fluid overload that is rising despite diuretics</td><td>Excretion cannot match obligatory intake; tissue edema impairs '
               'organs</td><td>Rising weight, effusions, higher ventilator pressures, failed feeds</td></tr>'
               '<tr><td>Need for volume to give nutrition, blood products or drugs</td><td>Restriction would starve the child or withhold therapy</td>'
               '<td>Nutrition held &ldquo;because of fluid&rdquo;</td></tr>'
               '<tr><td>Hyperkalemia not controlled medically</td><td>Membrane excitability; arrhythmia risk</td><td>Rising potassium, electrocardiogram (ECG) changes</td></tr>'
               '<tr><td>Severe metabolic acidosis</td><td>Bicarbonate cannot be given without sodium and volume</td><td>Falling pH despite '
               'treatment</td></tr>'
               '<tr><td>Uremic complications</td><td>Encephalopathy, bleeding, pericarditis</td><td>Altered sensorium, oozing</td></tr>'
               '<tr><td>Toxin or metabolic crisis</td><td>Dialyzable toxin or ammonia in inborn errors</td><td>Specific diagnosis; a different '
               'urgency and prescription</td></tr>'
               '</tbody></table></div>\n'
               '<p>The decision is rarely a single number. It is a trajectory: is overload rising, are the lungs and bowel paying for it, and is a '
               'diuretic response realistic in the next few hours? A child at 12% and climbing on a failed diuretic infusion may need dialysis '
               'sooner than a child at 18% who is now passing urine freely.</p>\n'
               '{{key:Do not wait for an absolute indication when overload is rising and the organs are paying for it. Agree on a fluid overload '
               'trigger with the intensivist before the child reaches it.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the PICU huddle, the number on the whiteboard &middot; fictional</span><p>In a PICU in '
               'Cebu, the team writes each child&rsquo;s percentage fluid overload on the whiteboard every morning. A 4-year-old with sepsis is at '
               '9% on day 2 and 14% on day 3, oliguric on a furosemide infusion, with a rising oxygen need.</p><p>You and the intensivist agree that '
               'if she is above 15% tomorrow or her oxygen need rises again tonight, CKRT starts. At 2 a.m. the resident calls: oxygen need is up. '
               'The decision has already been made; the circuit is primed within the hour.</p><p class="tc-scene-take"><b>What this shows.</b> A '
               'trigger agreed in daylight is easier to act on at night than a debate started at 2 a.m.</p></div>\n'
               '\n{{fig:apn16_a}}\n'),
              ('circuit',
               'The circuit',
               'The circuit and the child: volume, priming and access',
               '<p><strong>Blood volume.</strong> A child&rsquo;s circulating blood volume is roughly 80 mL per kilogram in infancy and early '
               'childhood. An 8 kg infant has about 640 mL. Every milliliter of blood that leaves the body to fill the circuit must come from that '
               'volume at connection, and it carries red cells, platelets and heat away with it.</p>\n'
               '<p>Pediatric CKRT literature advises that the extracorporeal circuit should hold no more than about 10% to 15% of the blood volume '
               'in infants and neonates, to prevent hypotension and anemia at connection.[[apn16_4]] Above that, the circuit is usually primed '
               'with blood or a blood&ndash;albumin mixture so that the child receives blood back at connection instead of losing it. Your unit&rsquo;s '
               'protocol sets the threshold and the priming recipe.</p>\n'
               '<p><strong>The hazards of a blood prime.</strong> Banked red cells are stored cold, in an acidic citrate solution, and leak '
               'potassium over time. Brophy and colleagues found blood bank units with a pH of 6.1 to 6.4, high potassium, low sodium and low '
               'calcium. In two infants, priming with such blood through an AN69 membrane caused severe hypotension at connection, which they '
               'attributed to pH-dependent bradykinin release by the membrane; they described techniques to prevent it.[[apn16_5]] Whatever membrane '
               'your unit uses, the principle is the same: a blood prime must be buffered and its potassium and calcium corrected before it reaches '
               'a small child, and the first minutes after connection need a nurse watching the pressure with fluids and calcium ready as the '
               'protocol directs.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Circuit-to-blood-volume problem</th><th>Mechanism</th><th>What you may see</th><th>What '
               'the protocol does about it</th></tr></thead><tbody>'
               '<tr><td>Large circuit, saline prime</td><td>Blood is diluted and removed into the circuit</td><td>Hypotension, falling hemoglobin '
               'at connection</td><td>Blood or albumin prime above the threshold</td></tr>'
               '<tr><td>Blood prime from banked blood</td><td>Acidic, high-potassium, low-calcium blood enters the child</td><td>Arrhythmia, '
               'hypotension, low ionized calcium</td><td>Buffer and correct the prime; monitor at connection</td></tr>'
               '<tr><td>Blood prime through an AN69 membrane</td><td>pH-dependent bradykinin generation</td><td>Sudden hypotension at the start'
               '</td><td>Avoid the combination or use the published mitigation steps</td></tr>'
               '<tr><td>Cold returned blood</td><td>Heat loss through the circuit</td><td>Hypothermia that can mask fever</td><td>Blood warmer; '
               'temperature charted</td></tr>'
               '<tr><td>Circuit loss when the filter clots</td><td>Blood in a clotted circuit cannot be returned</td><td>Anemia with each '
               'circuit change</td><td>Anticoagulation that works; avoid needless changes</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Access.</strong> Flow, and therefore dose, depends on the catheter. The KDIGO 2012 guideline lists the right internal '
               'jugular vein as the first choice for a dialysis catheter in AKI, then the femoral veins, with the subclavian route last because '
               'of the risk of central stenosis that would ruin future fistulas.[[apn16_7]] In a small child the femoral route is often used, '
               'but a femoral catheter in an infant can kink with hip flexion and give poor flows. Catheter size by weight and the pump speed are '
               'in your unit&rsquo;s protocol; the attending&rsquo;s task is to insist that the line is placed by someone experienced, under '
               'ultrasound, and that its position is checked, because a catheter that cannot deliver the blood flow will clot every circuit.</p>\n'
               '<p><strong>Machines built for small children.</strong> Standard CKRT machines are adult machines used off label in children under '
               'about 15 kg. Three alternatives have been described. The Cardio-Renal Pediatric Dialysis Emergency Machine (CARPEDIEM) was designed '
               'for neonates and small infants, with a priming volume under 30 mL, miniaturized roller pumps and scales accurate to 1 g; its first '
               'patient, a 2.9 kg neonate with 65% fluid overload, was treated for more than 400 hours and survived.[[apn16_8]] The Newcastle infant '
               'dialysis and ultrafiltration system (Nidus) dialyzed 10 babies of 1.8 to 5.9 kg without blood priming, through single-lumen access, '
               'with clearances higher than PD and ultrafiltration controlled to microliter precision; the planned randomized comparison with PD '
               'enrolled only two babies.[[apn16_9]] An adult ultrafiltration device with an extracorporeal volume of 33 mL was used across 119 '
               'pediatric admissions at several US centers; children under 10 kg had lower survival to the end of kidney support than those over 20 '
               'kg (60% vs 97%), and cardiovascular complications at initiation occurred in 3% of treatments.[[apn16_10]] All three reports are '
               'small, from expert centers, and without randomized comparison. None of these machines is generally available in Philippine '
               'hospitals as of this writing, so for most of your patients the choice is between acute PD and a standard machine with careful '
               'priming.</p>\n'
               '{{key:Before the first connection, calculate the child&rsquo;s blood volume and the circuit&rsquo;s share of it. That fraction decides '
               'the prime, the catheter and the vigilance at the bedside.}}\n'
               '\n{{fig:apn16_b}}\n'),
              ('delivery',
               'Anticoagulation and dose',
               'Anticoagulation, dose and what is actually delivered',
               '<p>A circuit clots when blood slows and meets a foreign surface. Every clot costs the child: the blood in the circuit is lost, '
               'treatment stops while a new set is primed (and, in a small child, possibly primed with blood again), and the dose delivered for '
               'that day falls. Anticoagulation is therefore part of the dose.</p>\n'
               '<p><strong>Heparin.</strong> Systemic unfractionated heparin is familiar and cheap, and its effect can be measured and reversed. Its '
               'cost is bleeding, especially after surgery, in coagulopathy or with low platelets, and the rare heparin-induced '
               'thrombocytopenia.</p>\n'
               '<p><strong>Regional citrate.</strong> Citrate infused into the circuit near the access chelates ionized calcium, which the '
               'coagulation cascade needs, so blood in the filter does not clot. Much of the citrate&ndash;calcium complex is removed by the filter; '
               'the rest returns to the child, where the liver and muscle metabolize citrate to bicarbonate, and calcium is replaced by a separate '
               'infusion. Anticoagulation stays in the circuit, not in the child. The risks follow from the chemistry: low ionized calcium in the '
               'child if replacement lags; metabolic alkalosis from bicarbonate generation; and citrate accumulation when the liver cannot '
               'metabolize it, as in liver failure or profound shock. Accumulation shows as a rising total calcium with a falling ionized calcium '
               '(a widening ratio between them) and a worsening acidosis.</p>\n'
               '<p><strong>The evidence.</strong> In the ppCRRT registry, 138 children received 442 circuits over 18,208 hours. Mean circuit survival '
               'was similar with heparin (42.1 hours) and citrate (44.7 hours) and shorter without anticoagulation (27.2 hours); clotting rates were '
               '25% with heparin, 27% with citrate and 50% with none. Life-threatening bleeding attributable to anticoagulation occurred only in the '
               'heparin group.[[apn16_6]] This was an observational registry, not a randomized trial, so centers chose methods for reasons that may '
               'have affected outcomes. The KDIGO 2012 guideline suggests regional citrate rather than heparin for CKRT in patients without '
               'contraindications to citrate (2B), a recommendation drawn largely from adult trials.[[apn16_7]] In children the same physiology '
               'applies, with two cautions: small infants have little liver reserve and a high citrate load relative to size, and many have just had '
               'cardiac surgery or have liver dysfunction.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Choice</th><th>Strength</th><th>Weakness</th><th>Watch</th></tr></thead><tbody>'
               '<tr><td>Regional citrate</td><td>Anticoagulation confined to the circuit; no systemic bleeding risk from the anticoagulant</td>'
               '<td>Needs a calcium infusion and a protocol nurses trust; risk of accumulation in liver failure and shock</td><td>Circuit and '
               'patient ionized calcium; total-to-ionized calcium ratio; pH and bicarbonate</td></tr>'
               '<tr><td>Systemic heparin</td><td>Simple, familiar, measurable</td><td>Bleeding; heparin-induced thrombocytopenia</td><td>Clotting '
               'time per protocol; platelets; surgical drains and wounds</td></tr>'
               '<tr><td>No anticoagulation</td><td>No anticoagulant risk</td><td>Short circuit life; more blood loss and downtime</td><td>Circuit '
               'pressures; time lost per day</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Dose.</strong> CKRT dose is usually expressed as effluent flow scaled to body size, by weight or by body surface area. '
               'The figure you order is the prescribed dose. The delivered dose is lower whenever the machine stops: alarms, bag changes, circuit '
               'clotting, catheter problems, trips to imaging and procedures. Adult data, summarized in the KDIGO guideline, show that delivered '
               'dose often falls well short of prescription, which is why the guideline advises prescribing with that gap in mind and monitoring '
               'what is actually delivered.[[apn16_7]] The prescribed number for children comes from your unit&rsquo;s protocol; the attending&rsquo;s '
               'job is to compare it every day with the hours the machine actually ran.</p>\n'
               '<p><strong>Fluid removal.</strong> Net ultrafiltration is the clinical point of CKRT in most children. It is set as a net hourly '
               'removal after all intake is counted, revised as the child&rsquo;s blood pressure and perfusion allow. Removing fluid faster than '
               'the tissues refill the vessels drops the pressure and, in a child on inotropes, may force the intensivist to raise them. Agree '
               'with the intensivist on a daily net balance goal and on what the nurse does if the pressure falls.</p>\n'
               '<p><strong>Drugs.</strong> CKRT removes many drugs, especially small, water-soluble, poorly protein-bound antibiotics, and the '
               'clearance depends on the effluent flow. Under-dosing an antibiotic in a septic child on CKRT is as dangerous as overdosing a '
               'nephrotoxin. The pharmacist adjusts each drug to the CKRT prescription, and the adjustment is revisited when the prescription or '
               'the circuit changes.</p>\n'
               '{{flow:Daily CKRT review with the intensivist|Hours delivered::How long did the machine actually run in 24 hours, and why did it '
               'stop?|Circuits used::How many circuits clotted, and how much blood was lost with them?|Fluid::Net balance against goal; weight; '
               'percentage fluid overload trend.|Chemistry::Potassium, phosphate, magnesium, bicarbonate, ionized calcium; total-to-ionized calcium '
               'ratio on citrate.|Access::Flows and pressures; catheter position; signs of infection.|Drugs and nutrition::Pharmacist review of every '
               'drug against the current prescription; protein and energy delivered.|Next step::Continue, adjust, or plan to wean.}}\n'
               '{{key:A dose that is not delivered is not a dose. Each morning, compare what you prescribed with the hours the machine ran and the '
               'number of circuits it took.}}\n'),
              ('acute_pd',
               'Acute PD',
               'Acute peritoneal dialysis in the PICU and in low-resource settings',
               '<p>Acute PD uses the peritoneum, which is large relative to body size in a small child, as the membrane. Dialysate with dextrose '
               'is run into the abdomen, dwells while solutes diffuse and water follows the osmotic gradient, and is drained. It needs no blood '
               'circuit, no anticoagulation and no vascular access, and it removes fluid gradually. Its weaknesses are lower and less predictable '
               'clearance than an extracorporeal circuit, less precise fluid removal, leaks around a fresh catheter, and pressure on the diaphragm '
               'in a child with stiff lungs.</p>\n'
               '<p><strong>The guideline.</strong> The International Society for Peritoneal Dialysis (ISPD) 2020 guideline for PD in AKI in children '
               'states that PD is a suitable kidney replacement modality for children with AKI (1C).[[apn16_11]] On access, it recommends a Tenckhoff '
               'catheter inserted by a surgeon in the operating theater as optimal (1B); a Seldinger kit (1C) or interventional radiology placement '
               '(1D) as acceptable alternatives; rigid stylet catheters only when soft Seldinger catheters are unavailable, for less than 3 days '
               '(1C); and improvised catheters only when no standard access exists (practice point). It recommends prophylactic antibiotics before '
               'insertion (1B) and a closed delivery system with a Y connection (1A), with burettes to measure fill and drain volumes for manual PD '
               'in small children (practice point). In resource-limited settings, an open system with spiked bags may be used if it limits '
               'contamination sites and measures volumes precisely (practice point).[[apn16_11]]</p>\n'
               '<p>On solutions, it advises commercially prepared fluids (1C), with locally prepared fluid acceptable where resources do not permit, '
               'under careful sterile preparation and monitoring of outcomes such as peritonitis (1C, minimum standard); bicarbonate-based solutions '
               'are preferred in hepatic dysfunction, hemodynamic instability or worsening acidosis (1D), with lactate as the alternative (2D). '
               'Potassium is added to dialysate once serum potassium falls below 4 mmol/L (practice point). Automated PD is suitable for pediatric AKI '
               'except in neonates, whose fill volumes are too small for current machines (1D).[[apn16_11]]</p>\n'
               '<p>On the prescription, the guideline describes, as practice points, starting with small fill volumes to limit leakage, '
               '10&ndash;20 mL/kg, and increasing gradually as tolerated toward about 30&ndash;40 mL/kg (800&ndash;1,100 mL/m&sup2;); initial cycles of '
               'about 60 to 90 minutes including inflow, dwell and drain, shortened in neonates and small infants to achieve ultrafiltration; and '
               'continuous PD through the full 24 hours for the first 1 to 3 days (1C), with close monitoring of intake and output toward '
               'normotension and euvolemia (1B).[[apn16_11]] These are the guideline&rsquo;s ranges, not orders. The fill, dwell, dextrose strength '
               'and potassium for a given child are written from your unit&rsquo;s protocol, adjusted to intra-abdominal pressure, breathing and '
               'response.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Acute PD element (ISPD 2020 pediatric)</th><th>Grade as the guideline states it</th>'
               '<th>Why it matters physiologically</th></tr></thead><tbody>'
               '<tr><td>PD is suitable for pediatric AKI</td><td>1C</td><td>Large peritoneal surface per kilogram; no blood circuit</td></tr>'
               '<tr><td>Surgically placed Tenckhoff catheter</td><td>1B</td><td>Secure seal, fewer leaks, longer use</td></tr>'
               '<tr><td>Closed system with Y connection</td><td>1A</td><td>Fewer contamination points; less peritonitis</td></tr>'
               '<tr><td>Burettes for manual PD in small children</td><td>Practice point</td><td>Small volumes must be measured exactly</td></tr>'
               '<tr><td>Continuous PD for the first 1&ndash;3 days</td><td>1C</td><td>Clearance in PD depends on time on dialysis</td></tr>'
               '<tr><td>Bicarbonate solutions in liver dysfunction or shock</td><td>1D</td><td>Lactate needs a working liver to become bicarbonate</td></tr>'
               '<tr><td>Improvised catheters only when nothing else exists</td><td>Practice point</td><td>Higher leak, blockage and infection risk</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>After cardiac surgery.</strong> Infants after bypass often accumulate fluid quickly, and many cardiac programs place a PD '
               'catheter in the operating room. Kwiatkowski and colleagues randomized 73 infants under 6 months with a PD catheter placed at surgery to '
               'a standardized PD regimen or intravenous furosemide for postoperative oliguria. There was no difference in the primary outcome, '
               'negative fluid balance on postoperative day 1. The furosemide group was three times more likely to reach 10% fluid overload (odds '
               'ratio 3.0), more likely to have prolonged ventilation (odds ratio 3.1), and had longer inotrope use and more electrolyte '
               'abnormalities; mortality (9.4% vs 3.1%) and length of stay did not differ significantly. PD was stopped early in 9 of 41 patients '
               'because of pleural&ndash;peritoneal communication.[[apn16_12]] It is a single-center, unblinded trial with a neutral primary outcome, '
               'so the secondary benefits suggest rather than prove an advantage. It supports using a catheter that is already in place early, '
               'before overload builds, and it warns that the pleura and peritoneum may communicate after cardiac surgery.</p>\n'
               '<p><strong>Low-resource settings.</strong> Acute PD is the most widely deliverable dialysis for children in low-resource settings, '
               'because it needs no machine, no water treatment and no blood circuit. The Saving Young Lives initiative, a partnership of international kidney '
               'and peritoneal dialysis societies described in 2016, was built on that premise: supporting acute PD for children and adults with AKI '
               'where no other dialysis exists.[[apn16_13]] In the Philippines, the same logic applies to the district and provincial hospital that cannot '
               'transfer a child in time: a trained team, a sterile closed system and burettes can keep a child alive until transfer is possible or '
               'the kidney recovers.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">In a provincial hospital in Samar, after a storm &middot; fictional</span><p>Roads to '
               'Tacloban are closed. A 5-year-old with severe AKI after leptospirosis is anuric with a potassium of 6.8 mmol/L and climbing. There '
               'is no CKRT machine and no pediatric hemodialysis. A surgeon places a soft catheter by Seldinger technique; commercial PD fluid is '
               'available from the adult PD supply.</p><p>By Viber you walk the nurses through a closed system with burettes and a written exchange '
               'sheet, and agree with the pediatrician on 12-hourly electrolytes, as the guideline describes for the first day. Two days later the '
               'roads open and she is transferred, stable.</p><p class="tc-scene-take"><b>What this shows.</b> Acute PD is not second-rate dialysis '
               'when it is the dialysis that can be delivered tonight.</p></div>\n'
               '{{key:Acute PD is a first-line option for many children with AKI, not a last resort. Use a proper catheter, a closed system and '
               'measured volumes, and treat the guideline&rsquo;s ranges as limits for the protocol, not as orders.}}\n'
               '\n{{fig:apn16_c}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Agree on ownership in writing.</strong> In the PICU the intensivist manages hemodynamics, ventilation, sedation and the '
               'overall plan; you manage the kidney replacement prescription and its chemistry, together. The order sheet should name both of you, '
               'state who the nurse calls for circuit problems and for hemodynamic problems, and show the daily review time. Ambiguity about '
               'who adjusts the fluid removal at 3 a.m. is a common cause of harm.</p>\n'
               '<p><strong>Choose the modality for the child and the unit.</strong> Ask four questions. How small is the child relative to the '
               'circuit you have? Is the abdomen usable (no recent abdominal surgery, no severe ascites leaking around wounds, no '
               'pleural&ndash;peritoneal communication)? How precise must fluid removal be, given the lungs and the inotropes? And who will run '
               'it overnight, with what experience? A child of 30 kg in septic shock on a standard machine with trained nurses is a different '
               'proposition from an 8 kg infant on a 150 mL circuit with nurses who rarely use it.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Question</th><th>Favors acute PD</th><th>Favors CKRT</th></tr></thead><tbody>'
               '<tr><td>Size relative to circuit</td><td>Small infant; circuit a large fraction of blood volume</td><td>Larger child; circuit a small '
               'fraction</td></tr>'
               '<tr><td>Abdomen</td><td>Intact, catheter in place</td><td>Recent abdominal surgery, peritonitis, pleural&ndash;peritoneal leak</td></tr>'
               '<tr><td>Need for precise, rapid clearance</td><td>Moderate need</td><td>Severe hyperkalemia, toxin, hyperammonemia, very high '
               'catabolism</td></tr>'
               '<tr><td>Hemodynamics</td><td>Unstable; avoids the connection drop</td><td>Stable enough for connection, or a blood prime can be '
               'made safe</td></tr>'
               '<tr><td>Staff and equipment</td><td>No CKRT machine or trained CKRT nurses</td><td>Machine and trained nurses available around the '
               'clock</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Write the order the night nurse can follow.</strong> Modality; access; for CKRT the circuit set, prime, blood flow, '
               'replacement and dialysate solutions and flows, anticoagulation with its monitoring and calcium plan, and net fluid removal goal; for '
               'PD the catheter, system, solution, fill, dwell, drain and cycle as the protocol sets them, with potassium and dextrose rules; in '
               'both, laboratory times, temperature, and what the nurse does for low pressure, a clotted circuit, a leak or poor drainage. Use the '
               'unit&rsquo;s pediatric template; do not improvise numbers by phone.</p>\n'
               '<p><strong>Review every day, and wean deliberately.</strong> Rising urine output, falling fluid overload and stable chemistry are the '
               'signs to try a pause. Many units stop CKRT for a trial off with diuretic support and repeat chemistry, or move from continuous to '
               'intermittent PD exchanges. If the kidney does not recover, the conversation moves to longer-term dialysis and to Module 19.</p>\n'
               '<p><strong>Transfer early when your unit cannot do it safely.</strong> A tiny infant on high-dose inotropes who needs CKRT with a '
               'circuit larger than your protocol allows, or a child with a metabolic crisis needing high clearance, may need a center with more '
               'experience. The time to arrange that is before the child is too unstable to move.</p>\n'
               '<p><strong>Talk to the family.</strong> Parents often hear &ldquo;machine&rdquo; as &ldquo;last resort.&rdquo; Explain that the '
               'kidneys are injured and cannot remove the fluid and salts the child needs to lose, that dialysis does that job while the kidneys '
               'heal, that most children who survive their illness recover kidney function, and that the dialysis does not make the illness itself '
               'better or worse. Name the risks plainly: bleeding, infection, low blood pressure at the start, and, for PD, leaks.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">At 3 a.m., the alarm that kept stopping the machine &middot; fictional</span><p>A '
               '12 kg child on CKRT in Davao has had the access pressure alarm sound every few minutes since midnight. The nurse has paused the '
               'pump repeatedly and the second circuit has clotted. The fluid removal for the night is 20% of the goal.</p><p>You ask the nurse '
               'to check the child&rsquo;s position and the femoral catheter for kinking, and ask the intensivist to review the line in the '
               'morning. The leg was flexed; straightened and splinted, the alarms stop.</p><p class="tc-scene-take"><b>What this shows.</b> Most '
               'lost CKRT dose is lost at the catheter and at the bedside, not in the prescription.</p></div>\n'
               '{{call:<ul><li>Hypotension within minutes of connection</li><li>Ionized calcium falling or the total-to-ionized calcium ratio '
               'widening on citrate</li><li>Bleeding on heparin, or a falling platelet count</li><li>Two circuits clotted in 24 hours</li><li>PD fluid '
               'leaking from the wound or appearing in a chest drain</li><li>Fluid overload still rising after 24 hours of therapy</li></ul>}}\n'
               '{{key:Name two owners, write one order the night nurse can follow, review it every morning, and move the child early if your unit '
               'cannot do it safely.}}\n')],
 'debrief': ['<p><strong>Does he need it now?</strong> Yes. He is 25% overloaded (2.0 kg on 8.0 kg), his ventilator pressures are rising, his '
             'urine output on a furosemide infusion is low, his potassium is climbing, and the trajectory is the wrong way. In the ppCRRT registry, '
             'children starting CKRT with 20% or more fluid overload had 65.6% mortality against 29.4% below 10%. That is an association, not '
             'proof that starting earlier saves lives, but every hour of overload in a ventilated infant costs lung and bowel function. He also '
             'weighs under 10 kg, a group with lower survival on CKRT. Start kidney replacement tonight.</p>\n',
             '<p><strong>CKRT or PD?</strong> His blood volume is about 640 mL; a 150 mL circuit is about 23% of it, above the 10&ndash;15% that '
             'pediatric literature advises, so CKRT on this set would need a blood prime, buffered and corrected for potassium and calcium, with '
             'a connection drop to manage in an infant on two inotropes. The surgical PD catheter is in and draining, and in a randomized trial in '
             'infants after cardiac surgery, PD reduced the chance of reaching 10% fluid overload compared with furosemide. Acute PD is a '
             'reasonable first choice, provided the abdomen is intact, there is no pleural&ndash;peritoneal leak, and the night nurses are '
             'supported: a closed system with burettes, a written exchange sheet from the unit protocol, small starting fills, and someone '
             'experienced at the bedside for the first exchanges. If PD does not achieve the fluid goal, or the lungs worsen with abdominal '
             'filling, move to CKRT with a safe blood prime.</p>\n',
             '<p><strong>Ownership and the parents.</strong> Write the order together with the intensivist: you own the dialysis prescription '
             'and chemistry, the intensivist owns hemodynamics and ventilation, and the order names who the nurse calls for what, with a fixed '
             'daily review. Tell his parents that his kidneys are temporarily unable to remove the extra water from surgery, that dialysis takes '
             'over that job while they recover, that it does not mean he is dying, that most babies whose hearts recover also recover their '
             'kidneys, and what the risks are. Offer to show them the setup at the bedside.</p>\n'],
 'skills': {'title': 'CKRT and acute dialysis in the pediatric intensive care unit',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Calculates percentage fluid overload and the circuit-to-blood-volume fraction, and states the priming decision', False),
                      ('Reviews a CKRT order with the intensivist, including anticoagulation monitoring and the net fluid goal', False),
                      ('Supervises the set-up of acute PD with a closed system and burettes, and writes the exchange sheet from the unit protocol', False),
                      ('Leads a daily review of delivered hours, circuit losses, chemistry and drug adjustments', False)],
            'placement': 'Supervised PICU practice or simulation'},
 'quiz': [('In the ppCRRT registry, what was mortality in children who started CKRT with 20% or more fluid overload, compared with less than 10%?',
           ['10% vs 5%',
            '65.6% vs 29.4%',
            '43.1% vs 43.1%',
            '29.4% vs 65.6%'],
           1,
           'Mortality was 65.6% with &ge;20% and 29.4% with &lt;10%. The association is observational and does not prove that earlier initiation '
           'saves lives.'),
          ('An 8 kg infant has a blood volume of about 640 mL. The available CKRT set holds about 150 mL. What follows?',
           ['The circuit is about 23% of blood volume, above the 10&ndash;15% pediatric limit, so a blood prime or a smaller circuit is needed',
            'No adjustment is needed because CKRT is gentle',
            'Prime with saline and connect quickly',
            'CKRT is contraindicated in all infants'],
           0,
           'Pediatric literature advises keeping the extracorporeal volume to about 10&ndash;15% of blood volume in infants; above that, units '
           'prime with blood or blood&ndash;albumin, buffered and corrected.'),
          ('What did the ppCRRT anticoagulation analysis show?',
           ['Citrate circuits lasted half as long as heparin circuits',
            'Anticoagulation made no difference to circuit life',
            'Heparin and citrate circuits lasted similarly; circuits without anticoagulation clotted more; life-threatening bleeding occurred '
            'only with heparin',
            'Citrate caused more bleeding than heparin'],
           2,
           'Mean circuit life was 42.1 hours with heparin and 44.7 with citrate, against 27.2 with none. The data are observational.'),
          ('Which sign suggests citrate accumulation during CKRT?',
           ['Falling total calcium with rising ionized calcium',
            'Metabolic alkalosis with a normal calcium ratio',
            'A rising platelet count',
            'Rising total calcium with falling ionized calcium and worsening acidosis'],
           3,
           'When the liver cannot metabolize citrate, citrate-bound calcium accumulates, ionized calcium falls and acidosis worsens.'),
          ('What did the Kwiatkowski 2017 trial of PD versus furosemide in infants after cardiac surgery show?',
           ['PD lowered mortality significantly',
            'No difference in the primary outcome; furosemide was associated with more 10% fluid overload, longer ventilation and inotrope use',
            'Furosemide was superior on every outcome',
            'PD caused more peritonitis than furosemide caused ototoxicity'],
           1,
           'The primary outcome (negative balance on day 1) was neutral; secondary outcomes favored PD. PD stopped early in 9 of 41 for '
           'pleural&ndash;peritoneal communication.')],
 'terms': [('CKRT', 'Continuous kidney replacement therapy'),
           ('CRRT', 'Continuous renal replacement therapy (older term for CKRT, used in cited titles)'),
           ('ppCRRT', 'Prospective Pediatric Continuous Renal Replacement Therapy Registry'),
           ('PICU', 'Pediatric intensive care unit'),
           ('PD', 'Peritoneal dialysis'),
           ('AKI', 'Acute kidney injury'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('CARPEDIEM', 'Cardio-Renal Pediatric Dialysis Emergency Machine'),
           ('Nidus', 'Newcastle infant dialysis and ultrafiltration system'),
           ('AN69', 'Acrylonitrile and sodium methallyl sulfonate copolymer membrane'),
           ('ECG', 'Electrocardiogram')],
 'readings': [('crrt-continuous-renal-replacement-therapy.html', 'Continuous Renal Replacement Therapy (CRRT): A Clinical Reference — Basics to Advanced'),
              ('aki-icu-dialysis-decisions.html', 'Dialysis Decisions in the ICU: AKI, Prognosis & Time-Limited Trials'),
              ('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide')],
 'calcs': ['calc-crrt-dose.html', 'calc-crrt-uf-rate.html', 'calc-fluid-overload.html', 'calc-pediatric-uo.html', 'calc-bsa.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
