# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 15: AKI in children: sepsis, nephrotoxins and tropical infections.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
Numbers checked against the PubMed abstracts of pRIFLE (Akcan-Arikan 2007), AWARE (Kaddourah 2017), NINJA (Goldstein 2016), Alobaidi
2018, Laoprasopwattana 2010 and the ppCRRT registry (Sutherland 2010); the WHO 2009 dengue guideline and PhilHealth Circular 2026-0008 on
the issuers' sites. KDIGO 2026 AKI/AKD is cited as a public-review draft only. No doses."""

MODULE = {'image_alt': 'A pediatric nephrologist listens to the chest of a girl sitting up in a hospital bed during a dengue outbreak, while her father watches.',
 'objectives': ['Stage pediatric acute kidney injury (AKI) with KDIGO and pRIFLE criteria, estimate a missing baseline honestly, and calculate '
                'percentage fluid overload.',
                'Manage AKI in dengue, leptospirosis and sepsis with attention to the phase of illness, fluid balance and nephrotoxin exposure.',
                'Plan follow-up after pediatric AKI, using KDIGO 2012 as the current guideline and the KDIGO 2026 acute kidney disease concept as a draft.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the consultant who reads the fluid chart</span>In the Philippine wet '
        'season your phone fills with children in dengue shock, leptospirosis after floods and sepsis from every cause. The pediatric resident '
        'and the intensivist own the bedside; your duty is to stage the kidney injury from trends, to say plainly when fluid has become the '
        'problem, to remove the drugs that are adding injury, to decide when dialysis is needed and where it can be done, and to make sure the '
        'child is seen again after discharge.</div>\n'
        '{{plain:Think of the kidney in a sick child as a rice field during a typhoon. First the field is dry because the irrigation has failed; '
        'then the water comes all at once and the field floods. The same field needs opposite help a day apart.}}\n'
        '<p>The picture has a limit. A rice field does not die from flooding in an hour, and it has no lungs. A child does. In dengue, fluid that '
        'leaked out during the critical phase returns to the vessels during recovery, and a child who needed boluses yesterday can drown in '
        'pleural fluid today. The kidney also has its own injury that does not simply reverse when perfusion returns. So you read the phase of '
        'illness and the fluid balance together, every few hours.</p>\n'
        '{{cards:Key numbers|AWARE (4,683 PICU patients)::AKI 26.9%; severe AKI 11.6%; 28-day death 11.0% vs 2.5% without severe AKI|Creatinine '
        'alone (AWARE)::Missed AKI in 67.2% of patients with low urine output|Fluid overload meta-analysis (44 studies, 7,507 children)::Adjusted '
        'odds of death up 6% per 1% fluid overload|NINJA (pediatric wards)::AKI rate down 64%, 2.96 to 1.06 per 1,000 patient-days|Follow-up '
        '(KDIGO 2012, ungraded)::Evaluate about 3 months after AKI}}\n'
        '<p>Most pediatric AKI is prerenal or early tubular injury that improves when perfusion is restored and harmful drugs are stopped. A '
        'few children have severe AKI with fluid overload that needs dialysis. Your work is to tell the two apart early, keep the second group '
        'from being harmed by more fluid, and follow both after they go home.</p>\n',
 'case': {'title': 'Day 5 of dengue, and the urine has stopped',
          'html': '<p>It is August, during a dengue outbreak. At 1 a.m. the pediatric resident at a provincial hospital in Iloilo City calls you. '
                  'Kyla Mendoza is 10 years old and weighed 32 kg on admission. She is on day 5 of illness; she went into shock on day 4 and '
                  'received crystalloid boluses and then a colloid, following the dengue protocol. Her hematocrit was 48% at the worst and is now '
                  '36%. Her platelets are 18,000/&micro;L.</p>\n'
                  '<p>Over the last 10 hours she has passed 0.3 mL/kg of urine per hour. Her creatinine is 1.2 mg/dL; no earlier value exists. '
                  'She now weighs 35.2 kg. Her respiratory rate is 40, oxygen saturation 92% on nasal cannula, and the chest film shows bilateral '
                  'pleural effusions; the abdomen is tense with ascites. Blood pressure is 118/70 and her pulse is 104 and full. The resident has '
                  'written another fluid bolus &ldquo;for oliguria&rdquo; and asks you to approve it. The intensive care unit is full. Her father, '
                  'a tricycle driver, asks whether she needs dialysis and whether PhilHealth will pay for it.</p>\n',
          'questions': ['Does Kyla have AKI, what stage, and how much fluid overload does she have?',
                        'Should she receive another bolus? What is driving the oliguria, and what should happen tonight?',
                        'What follow-up does she need after discharge, and how would you answer her father about coverage?']},
 'sections': [('physiology',
               'Physiology',
               'How a child&rsquo;s kidney fails in critical illness',
               '<p>A child&rsquo;s kidneys receive a large share of cardiac output, and the medulla works close to hypoxia. Three mechanisms '
               'dominate in sick children, often together.</p>\n'
               '<p><strong>Low perfusion.</strong> In hypovolemia or shock, afferent constriction and low pressure lower filtration. Early on, '
               'tubules are intact: they conserve sodium avidly, urine sodium is low and urine is concentrated. If perfusion is restored quickly, '
               'function returns.</p>\n'
               '<p><strong>Sepsis.</strong> Septic AKI is not only low flow. Inflammatory mediators, microvascular dysfunction and mitochondrial '
               'stress injure tubules even when cardiac output is normal or high. Fluid restores flow but not this injury, so giving more fluid to '
               'a septic child with normal perfusion and low urine output adds overload without adding filtration.</p>\n'
               '<p><strong>Venous congestion.</strong> When central venous and intra-abdominal pressures rise, the pressure gradient across the '
               'kidney falls and the encapsulated organ is compressed. Ascites, a tense abdomen and high ventilator pressures all raise this '
               'outflow pressure. The kidney then makes less urine because of the fluid already given.</p>\n'
               '<p><strong>Fluid overload as an outcome.</strong> Percentage fluid overload is calculated as (fluid in minus fluid out, in liters) '
               'divided by the admission weight in kilograms, times 100; many units use daily weights instead.[[apn15_11]] It matters because '
               'overloaded tissue oxygenates poorly, lungs stiffen, bowel swells, and creatinine is diluted so the AKI looks smaller than it is.</p>\n'
               '<p><strong>Why creatinine lags.</strong> Creatinine rises only after filtration has been low for hours, and how far it rises depends '
               'on how much creatinine the body makes. A small or malnourished child, or a child with wasted muscle after a long illness, makes little '
               'creatinine, so even a severe fall in filtration produces a modest number. A doubling from 0.3 to 0.6 mg/dL can look normal on a '
               'laboratory sheet built for adults. Fluid overload adds dilution. Each of these makes creatinine a late and quiet signal in children, '
               'which is why urine output, weight and the trend carry so much weight.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Mechanism</th><th>What breaks</th><th>What you see</th><th>What helps</th></tr></thead>'
               '<tbody>'
               '<tr><td>Low perfusion</td><td>Filtration pressure falls; tubules intact</td><td>Cool peripheries, tachycardia, concentrated urine, '
               'low urine sodium</td><td>Restore volume and pressure</td></tr>'
               '<tr><td>Septic tubular injury</td><td>Inflammation and microvascular dysfunction</td><td>Low urine output despite adequate '
               'perfusion</td><td>Treat the source; avoid overload; avoid nephrotoxins</td></tr>'
               '<tr><td>Venous congestion</td><td>Transrenal gradient falls; kidney compressed</td><td>Edema, effusions, ascites, rising weight</td>'
               '<td>Stop fluid; diuretic if responsive; remove fluid by dialysis if not</td></tr>'
               '<tr><td>Nephrotoxins</td><td>Direct tubular or hemodynamic injury</td><td>Creatinine rise days after exposure</td><td>Stop, '
               'substitute, adjust; count exposures daily</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Before you approve a bolus for oliguria, ask whether this child is underfilled or congested. Oliguria is a symptom of both, and '
               'the treatments are opposite.}}\n'),
              ('staging',
               'Staging',
               'Staging and measuring pediatric AKI',
               '<p>The pediatric modification of the RIFLE criteria (pRIFLE) was developed in 150 critically ill children and staged AKI by '
               'estimated creatinine clearance and urine output; AKI was associated with death independent of illness severity (odds ratio '
               '3.0).[[apn15_3]] The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 definition, still the current final version, unified '
               'the adult and pediatric criteria and is what most pediatric studies now use.[[apn15_1]] The KDIGO 2026 AKI and acute kidney disease '
               '(AKD) guideline is a public-review draft; until it is final, quote the 2012 criteria and grades.[[apn15_2]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>KDIGO 2012 stage</th><th>Creatinine</th><th>Urine output</th></tr></thead><tbody>'
               '<tr><td>1</td><td>1.5&ndash;1.9 times baseline, or a rise of &ge;0.3 mg/dL</td><td>&lt;0.5 mL/kg/h for 6&ndash;12 h</td></tr>'
               '<tr><td>2</td><td>2.0&ndash;2.9 times baseline</td><td>&lt;0.5 mL/kg/h for &ge;12 h</td></tr>'
               '<tr><td>3</td><td>&ge;3 times baseline, or &ge;4.0 mg/dL, or KRT started, or in patients under 18 an eGFR &lt;35 mL/min/1.73 '
               'm&sup2;</td><td>&lt;0.3 mL/kg/h for &ge;24 h, or anuria for &ge;12 h</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Urine output is not optional.</strong> The Assessment of Worldwide Acute Kidney Injury, Renal Angina and Epidemiology '
               '(AWARE) study prospectively followed 4,683 patients aged 3 months to 25 years in 32 pediatric intensive care units (PICUs). Creatinine '
               'alone failed to identify AKI in 67.2% of patients who met the urine output criterion.[[apn15_4]] In a ward without catheters, '
               'weighed diapers or measured voids, charted at fixed times, are the test.</p>\n'
               '<p><strong>The missing baseline.</strong> Many Filipino children have never had a creatinine measured. When no baseline exists, '
               'units commonly back-calculate an expected value from the child&rsquo;s height with a bedside pediatric equation and an assumed normal '
               'GFR. Write in the note that the baseline is estimated and how; a staging built on an assumed baseline is a hypothesis that the '
               'next creatinines will test.</p>\n'
               '<p><strong>Fluid overload is a second staging.</strong> Calculate it every day in every child with AKI. In the case, Kyla has gained '
               '3.2 kg on an admission weight of 32 kg: 10% fluid overload by weight, before counting the pleural and peritoneal fluid already '
               'on the film.</p>\n'
               '{{key:Stage AKI from both creatinine and urine output, write down how you chose the baseline, and calculate percentage fluid '
               'overload every day.}}\n'
               '\n{{fig:apn15_a}}\n'),
              ('tropical',
               'Tropical AKI',
               'Dengue, leptospirosis and sepsis',
               '<p><strong>Dengue.</strong> The World Health Organization (WHO) 2009 guideline describes three phases: febrile, critical and '
               'recovery. In the critical phase, around defervescence, capillaries leak plasma, hematocrit rises and shock can develop; in the '
               'recovery phase, leaked fluid is reabsorbed into the circulation, hematocrit falls, and the child who received generous fluid during '
               'the leak can develop pulmonary edema, effusions and heart strain. The guideline warns about fluid overload as a major cause of '
               'complications and advises reducing or stopping intravenous fluid once leak stops.[[apn15_8]]</p>\n'
               '<p>AKI is uncommon in pediatric dengue but grave when it occurs. In a Thai review of children under 15 admitted with dengue '
               'hemorrhagic fever from 1989 to 2007, AKI occurred in 25 of 2,893 admissions (0.9%), and 64.0% of those children died; dengue '
               'grade IV shock and obesity were the main risk factors, and survivors recovered normal creatinine.[[apn15_7]] The numbers are from a '
               'single referral center over two decades with older intensive care, so mortality today may be lower, but the message holds: dengue '
               'AKI is a marker of profound shock, bleeding and multiorgan failure.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Dengue phase</th><th>Fluid physiology</th><th>Kidney picture</th><th>What the '
               'attending says</th></tr></thead><tbody>'
               '<tr><td>Febrile</td><td>Intake may be poor; leak has not begun</td><td>Usually normal</td><td>Oral fluids; watch for warning signs</td></tr>'
               '<tr><td>Critical (leak)</td><td>Plasma leaks; hematocrit rises; shock possible</td><td>Prerenal; low urine output with high '
               'hematocrit</td><td>Fluid by the dengue protocol, titrated to perfusion and hematocrit</td></tr>'
               '<tr><td>Recovery (reabsorption)</td><td>Leaked fluid returns; hematocrit falls</td><td>Urine output usually rises; if it does not, '
               'AKI plus overload</td><td>Stop or reduce fluid; diuretic if stable and responsive; dialysis if overloaded and anuric</td></tr>'
               '<tr><td>Falling hematocrit with instability</td><td>Bleeding, not reabsorption</td><td>Prerenal from blood loss</td><td>Look for '
               'bleeding; blood, not crystalloid</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Leptospirosis.</strong> Children wade in floodwater too. Leptospiral injury to the proximal tubule and thick ascending '
               'limb typically causes nonoliguric AKI with potassium and sodium wasting, and severe disease adds jaundice, low platelets and '
               'pulmonary hemorrhage. The Pediatric Infectious Disease Society of the Philippines (PIDSP) published a pediatric leptospirosis '
               'guideline (2019 edition, published 2023), developed with the GRADE method, for diagnosis, antibiotic management and '
               'prevention.[[apn15_9]] Follow it and your hospital formulary for antibiotics; your part is the kidney, the potassium and the lungs. '
               'PhilHealth has a benefits package for moderate to severe leptospirosis with separate packages for cases needing hemodialysis and '
               'for cases needing peritoneal dialysis.[[apn15_10]] Confirm the current rules on the date of service, and choose the modality for '
               'clinical reasons, not because of the package.</p>\n'
               '<p><strong>Sepsis.</strong> Septic AKI is the most common form in the PICU. In AWARE, severe AKI (stage 2 or 3) occurred in 11.6% '
               'and was associated with 28-day death after adjustment for 16 covariates (adjusted odds ratio 1.77, 95% confidence interval 1.17 to '
               '2.68); 11.0% of children with severe AKI died, against 2.5% without.[[apn15_4]] This is an association. It identifies the children '
               'who need closer monitoring; it does not show that treating the creatinine changes survival.</p>\n'
               '<p><strong>Fluid overload in the evidence.</strong> A meta-analysis of 44 studies including 7,507 critically ill children found '
               'that fluid overload, however defined, was associated with in-hospital death (odds ratio 4.34), and after adjustment for illness '
               'severity each 1% increase in fluid overload raised the odds of death by 6% (adjusted odds ratio 1.06, 1.03 to 1.10).[[apn15_6]] '
               'Most included studies were retrospective cohorts, so sicker children may simply receive more fluid; no randomized trial has shown '
               'that restricting fluid after resuscitation saves lives in children. The association is consistent enough to make daily fluid '
               'balance a vital sign.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">By Viber, from a district hospital in Leyte &middot; fictional</span><p>A '
               '13-year-old boy who helped clear a flooded canal has fever, calf pain, jaundice and a creatinine of 3.4 mg/dL. He is passing urine, '
               'and his potassium is 3.0 mmol/L. The resident asks whether he can wait for leptospirosis serology before treating.</p><p>You ask '
               'them to start antibiotics now per the PIDSP guideline, replace potassium cautiously, count respiratory rate and oxygen saturation every '
               'hour, and call you at once for hemoptysis. You also find him a dialysis-capable bed in Tacloban in case his lungs or urine fail.</p>'
               '<p class="tc-scene-take"><b>What this shows.</b> In leptospirosis, the serology can wait; the antibiotics, the potassium and the '
               'lungs cannot.</p></div>\n'
               '{{key:In dengue, know the phase. A falling hematocrit with stable vital signs and effusions means reabsorption: stop the fluid. A '
               'falling hematocrit with shock means bleeding: give blood.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>At the first call.</strong> Ask for the trend, not the last value: creatinine series, hourly urine output, weights, '
               'fluid in and out, hematocrit and platelets in dengue, potassium and bicarbonate, and the drug chart. Examine, or ask the resident '
               'to describe, perfusion, the jugular venous pressure if visible, lung sounds, effusions, liver size and the abdomen.</p>\n'
               '<p><strong>Steward nephrotoxins.</strong> The Nephrotoxic Injury Negated by Just-in-Time Action (NINJA) program screened '
               'noncritically ill hospitalized children receiving an intravenous aminoglycoside for more than 3 days or more than 3 nephrotoxins at '
               'once, and pharmacists recommended daily creatinine. Over 43 months, nephrotoxin exposures fell by 38% (11.63 to 7.24 per 1,000 '
               'patient-days) and AKI by 64% (2.96 to 1.06 per 1,000 patient-days); the authors estimated 398 AKI episodes avoided.[[apn15_5]] It was '
               'a single-center quality improvement project in a well-resourced hospital, without a control group, but the method is cheap: a daily '
               'list, a daily creatinine and a daily question about each drug.</p>\n'
               '<p><strong>Decide about fluid and dialysis.</strong> If the child is perfused and congested, stop maintenance fluid beyond what '
               'drugs and nutrition need, try a loop diuretic if blood pressure allows and urine is still being made, and plan kidney replacement '
               'if overload is progressing, the lungs are failing, or potassium and acidosis are not controlled. Peritoneal dialysis (PD) and '
               'continuous kidney replacement therapy (CKRT) are covered in Module 16. If the intensive care unit is full, the decision about where '
               'the child goes is yours to make with the intensivist and the referring physician, and it is made tonight.</p>\n'
               '<p><strong>Dose drugs to the kidney you have today.</strong> Antibiotics, anticonvulsants, antivirals and sedatives cleared by the '
               'kidney accumulate as filtration falls, and creatinine overestimates function while it is still rising. Ask the pharmacist to adjust '
               'every renally cleared drug to the current, not the admission, kidney function, and to readjust when the kidney recovers or dialysis '
               'starts; under-dosing an antibiotic in sepsis is also harm. The unit&rsquo;s pediatric formulary sets the numbers.</p>\n'
               '<p><strong>Feed the child.</strong> A catabolic child breaks down muscle, which raises potassium, phosphate and urea and weakens '
               'recovery. Fluid restriction for overload should not become starvation; concentrated feeds and early dialysis to create room for '
               'nutrition are often the better trade.</p>\n'
               '{{flow:The oliguric child at 1 a.m.|Stage it::Creatinine trend, urine output, and an estimated baseline written as estimated.|Weigh the '
               'fluid::Percentage fluid overload from weights or balance; effusions and ascites on examination.|Name the phase::In dengue, critical '
               'leak or reabsorption; in sepsis, resuscitated or not.|Choose the direction::Underfilled: fluid. Congested: stop fluid, diuretic if '
               'responsive.|Remove what harms::Nephrotoxins, contrast, unnecessary drugs; adjust the rest.|Set the trigger::Potassium, acidosis, '
               'oxygen need or overload that will start dialysis, written in the chart.|Place the child::The bed where that dialysis can happen.}}\n'
               '<p><strong>Plan the follow-up.</strong> KDIGO 2012 advises evaluating patients about 3 months after AKI for resolution, new onset or '
               'worsening of chronic kidney disease (CKD) (ungraded).[[apn15_1]] The KDIGO 2026 draft describes acute kidney disease, the period of '
               'ongoing kidney dysfunction after an AKI episode, as a phase that needs its own monitoring; until the guideline is final, use the '
               'concept to justify follow-up, not as a graded rule.[[apn15_2]] For a child, write the AKI stage, the peak and discharge creatinine, '
               'the drugs to avoid, and who checks blood pressure, urinalysis for protein and creatinine at about 3 months. The family needs the same '
               'plan in plain words.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>At discharge after pediatric AKI</th><th>Why</th></tr></thead><tbody>'
               '<tr><td>Stage, peak and discharge creatinine</td><td>The next clinician needs the size of the injury</td></tr>'
               '<tr><td>Blood pressure</td><td>Hypertension can be the first sign of residual damage</td></tr>'
               '<tr><td>Urinalysis or urine protein-to-creatinine ratio</td><td>Proteinuria marks persisting injury</td></tr>'
               '<tr><td>Creatinine at about 3 months</td><td>KDIGO 2012 practice, ungraded</td></tr>'
               '<tr><td>Nephrotoxin warning</td><td>The family and the next doctor should avoid unnecessary nonsteroidal anti-inflammatory drugs (NSAIDs) and aminoglycosides</td></tr>'
               '<tr><td>Named owner</td><td>Without a name, follow-up does not happen</td></tr>'
               '</tbody></table></div>\n'
               '<div class="tc-scene"><span class="tc-lab">In clinic, three months later &middot; fictional</span><p>Jerome, 7, had stage 3 AKI from '
               'septic shock after a perforated appendix and needed four days of PD in Bacolod. He comes to your clinic because the discharge '
               'summary named you. His creatinine is back to an estimated normal, but his urine protein-to-creatinine ratio is raised and his blood '
               'pressure is at the 95th percentile.</p><p>You repeat both, confirm them, and enroll him in CKD follow-up.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> A normal creatinine after AKI is not the end of the story; protein and blood pressure '
               'tell the rest.</p></div>\n'
               '{{call:<ul><li>Oliguria with rising oxygen need or effusions</li><li>Potassium rising despite treatment, or electrocardiogram (ECG) '
               'changes</li><li>Fluid overload of 10% or more and still climbing</li><li>Leptospirosis with hemoptysis or falling saturation</li>'
               '<li>Dengue with falling hematocrit and shock (suspect bleeding)</li></ul>}}\n'
               '{{key:Every child who had AKI leaves with a stage, a 3-month check, a blood pressure and urine plan, and a name.}}\n'
               '\n{{fig:apn15_b}}\n')],
 'debrief': ['<p><strong>AKI and fluid overload.</strong> She has had urine output of 0.3 mL/kg per hour for 10 hours, which meets KDIGO stage 1 '
             'by urine output whatever her baseline creatinine, and becomes stage 2 if it continues for two more hours. '
             'Her creatinine of 1.2 mg/dL is likely well above an estimated baseline for a 10-year-old, and dilution means it understates the '
             'injury. Her weight has risen 3.2 kg on 32 kg: 10% fluid overload, with effusions and ascites besides.</p>\n',
             '<p><strong>Another bolus?</strong> No. Her hematocrit has fallen from 48% to 36% with a full pulse, stable blood pressure, '
             'effusions and ascites: this is reabsorption on day 5 to 6, not ongoing leak, and the oliguria reflects AKI plus congestion. Ask the '
             'resident to cancel the bolus and stop maintenance fluid beyond what is needed. Check for bleeding (stool, gastric aspirate, vital '
             'signs) because a falling hematocrit with shock would change everything. If she is passing any urine and blood pressure allows, a '
             'diuretic trial is reasonable. Set triggers for dialysis (worsening oxygenation, potassium, acidosis, rising overload) and agree '
             'tonight with the intensivist where she goes if they are met; a full intensive care unit is a reason to arrange transfer early, not '
             'to wait.</p>\n',
             '<p><strong>Follow-up and coverage.</strong> At discharge she needs a summary with stage, peak and discharge creatinine, and a check '
             'of blood pressure, urine protein and creatinine at about 3 months, with your name on it. Tell her father that if dialysis is needed '
             'it will be chosen for her safety, that hospitals bill PhilHealth for an admission like this under the rules in force on the date of '
             'service, and that the hospital&rsquo;s PhilHealth desk and social worker can confirm what applies. Do not quote an amount you have '
             'not confirmed.</p>\n'],
 'skills': {'title': 'AKI in children: sepsis, nephrotoxins and tropical infections',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Stages pediatric AKI by creatinine and urine output and documents how the baseline was chosen', False),
                      ('Calculates percentage fluid overload from weights and from fluid balance', False),
                      ('Identifies the dengue phase from hematocrit, vital signs and fluid signs, and advises on fluid accordingly', False),
                      ('Writes a pediatric post-AKI discharge plan with a named owner and a 3-month review', False)],
            'placement': 'Supervised ward or PICU consultation, or simulation'},
 'quiz': [('A 10-year-old on day 6 of dengue has a falling hematocrit, stable blood pressure, a full pulse, pleural effusions and low urine output. '
           'What is the best next step?',
           ['Another crystalloid bolus',
            'Stop or reduce intravenous fluid, look for bleeding, and consider a diuretic if she is still passing urine',
            'Start a colloid infusion',
            'Ignore the effusions and repeat the hematocrit in 24 hours'],
           1,
           'Falling hematocrit with stable hemodynamics and effusions signals reabsorption. More fluid worsens congestion; bleeding must be excluded.'),
          ('In AWARE, what proportion of patients with low urine output would have been missed by creatinine alone?',
           ['67.2%', '11.6%', '26.9%', '2.5%'],
           0,
           'Creatinine alone failed to identify AKI in 67.2% of patients who met the urine output criterion. Measure urine output.'),
          ('How is percentage fluid overload calculated in the pediatric CKRT registry?',
           ['Weight today divided by height',
            'Urine output divided by fluid intake',
            '(Fluid in minus fluid out in liters) divided by admission weight in kilograms, times 100',
            'Hematocrit change times weight'],
           2,
           'This is the formula used by Sutherland and colleagues; daily weights are an alternative.'),
          ('What does the fluid overload meta-analysis by Alobaidi and colleagues show?',
           ['That fluid restriction after resuscitation saves lives in a randomized trial',
            'That fluid overload is unrelated to outcome',
            'That only overload above 30% matters',
            'An association between each 1% increase in fluid overload and 6% higher adjusted odds of death, mostly from observational studies'],
           3,
           'The pooled data are observational; sicker children may receive more fluid, so causation is not proven.'),
          ('Which statement about KDIGO AKI guidance is correct as of November 2026?',
           ['KDIGO 2026 AKI/AKD is final and replaces 2012',
            'KDIGO 2012 remains the current final guideline; the 2026 AKI/AKD guideline is a public-review draft',
            'KDIGO has no follow-up advice after AKI',
            'KDIGO 2012 does not apply to children'],
           1,
           'Quote the 2012 criteria and grades; use the 2026 acute kidney disease concept as draft guidance only.')],
 'terms': [('AKI', 'Acute kidney injury'),
           ('AKD', 'Acute kidney disease'),
           ('pRIFLE', 'Pediatric modified Risk, Injury, Failure, Loss, End-stage criteria'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('AWARE', 'Assessment of Worldwide Acute Kidney Injury, Renal Angina and Epidemiology study'),
           ('PICU', 'Pediatric intensive care unit'),
           ('KRT', 'Kidney replacement therapy'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('GFR', 'Glomerular filtration rate'),
           ('WHO', 'World Health Organization'),
           ('PIDSP', 'Pediatric Infectious Disease Society of the Philippines'),
           ('GRADE', 'Grading of Recommendations Assessment, Development and Evaluation'),
           ('NINJA', 'Nephrotoxic Injury Negated by Just-in-Time Action'),
           ('PD', 'Peritoneal dialysis'),
           ('CKRT', 'Continuous kidney replacement therapy'),
           ('CKD', 'Chronic kidney disease'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('ECG', 'Electrocardiogram')],
 'readings': [('dengue-aki-kidney.html', 'Dengue & Your Kidneys — When Fever Becomes a Kidney Emergency'),
              ('leptospirosis-nephropathy.html', 'Leptospirosis After Flood Exposure: Symptoms, Kidney Warning Signs & What To Do'),
              ('aki-does-not-end-at-discharge.html', 'AKI Does Not End at Discharge: 90-Day Recovery Guide')],
 'calcs': ['calc-pediatric-aki.html', 'calc-pediatric-uo.html', 'calc-fluid-overload.html', 'calc-fena-feurea.html', 'calc-post-aki-followup.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
