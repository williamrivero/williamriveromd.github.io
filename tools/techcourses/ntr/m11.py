# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 11: CKD evaluation, risk and referral.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2024
definitions, recommendations (1A, 1B, 1C) and practice points checked against KDIGO summaries; KFRE derivation and
validation figures against the PubMed abstracts (Tangri 2011, 2016); CKM staging against the AHA presidential advisory;
PhilHealth Konsulta/YAKAP laboratory list against PhilHealth documents. No doses. Fictional case."""

MODULE = {'image_alt': 'A Filipino internal medicine resident explains a color-coded kidney risk chart to a middle-aged jeepney driver and his wife in a hospital outpatient clinic.',
 'objectives': ['<strong>Intern:</strong> Stage chronic kidney disease (CKD) by glomerular filtration rate (GFR) category and albuminuria category, and present the cause, the stage and the trend in one sentence.',
                '<strong>Resident:</strong> Confirm chronicity and look for the cause, then use the kidney failure risk equation (KFRE) with the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 thresholds to time referral and preparation.',
                '<strong>Fellow:</strong> Run a CKD clinic with risk-based follow-up: monitoring intervals, cardiovascular-kidney-metabolic risk, referral criteria and a written plan the primary care team can follow.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the CKD patient in the outpatient clinic and on the ward</span>'
        'As an <strong>intern</strong>, you collect the creatinine values, urine tests and medicine list over time, stage the CKD correctly and '
        'present it without confusing a single bad day with a chronic disease. As a <strong>resident</strong>, you prove chronicity, look for the '
        'cause, estimate the risk of kidney failure and decide, with your attending, whether this patient needs a nephrologist now, later or at '
        'all. As a <strong>fellow</strong>, you run the clinic: you set the follow-up interval by risk, you start the conversation about kidney '
        'replacement early enough, and you write plans that a busy primary care physician in the province can carry out.</div>\n'
        '{{plain:Think of the kidneys as a large company with about two million workers, the nephrons. Lose a few hundred thousand and the company '
        'still meets its quota, because the remaining workers do overtime. The quarterly report (the creatinine) looks normal until the workforce is '
        'small. A leaking factory floor (albumin in the urine) is often the first sign that something is wrong inside.}}\n'
        '<p>The picture has a limit. Overtime in the kidney is not free. Each surviving nephron filters more (single-nephron hyperfiltration), its '
        'glomerular pressure rises, and the higher pressure injures the podocytes and the filtration barrier. Albumin that crosses the barrier is '
        'reabsorbed by the proximal tubule, and that work itself drives inflammation and scarring. So albuminuria is both a marker of damage and a '
        'contributor to it. Creatinine, meanwhile, depends on muscle mass and tubular secretion as well as filtration: a small, older Filipino woman '
        'can have lost half her filtration with a creatinine still inside the laboratory&rsquo;s normal range. CKD is therefore defined by two '
        'measurements, not one, and staged by both.</p>\n'
        '{{cards:Key numbers|Definition (KDIGO 2024)::Abnormalities of kidney structure or function present for more than 3 months, with implications '
        'for health|CKD thresholds (KDIGO 2024)::GFR below 60 mL/min/1.73 m&sup2; and/or albumin-to-creatinine ratio (ACR) 30 mg/g (3 mg/mmol) or '
        'more|Risk equation (KDIGO 2024)::Use an externally validated equation for absolute kidney failure risk in CKD G3 to G5 (1A)|Referral '
        '(KDIGO 2024)::A 5-year kidney failure risk of 3% to 5% can prompt nephrology referral (practice point)|Preparation (KDIGO 2024)::A 2-year risk '
        'above 40% can guide modality education, access planning and transplant referral (practice point)|KFRE accuracy (meta-analysis, 721,357 '
        'people)::C statistic 0.90 at 2 years and 0.88 at 5 years}}\n'
        '<p>Most people with CKD will never need dialysis; far more will have a heart attack, a stroke or heart failure first. A few will lose '
        'kidney function quickly and arrive at the emergency room uremic, with no access and no plan. Your work is to tell these groups apart '
        'early, to treat the many for cardiovascular and kidney protection, and to bring the few to a nephrologist while there is still time to '
        'prepare.</p>\n',
 'case': {'title': 'The jeepney driver with a &ldquo;slightly high&rdquo; creatinine',
          'html': '<p>Tuesday, 10 a.m., the medicine outpatient department of a public hospital in Malolos, Bulacan. Mr. Romeo Dizon, 52, drives a '
                  'jeepney on the Malolos&ndash;Meycauayan route from 5 a.m. to 7 p.m., six days a week. He has had type 2 diabetes for 11 years '
                  'and high blood pressure for 6. He takes metformin and losartan when he can buy them, and a &ldquo;kidney cleanse&rdquo; capsule '
                  'his neighbor sells. A barangay health center referred him with a note: &ldquo;Crea slightly high, pls eval.&rdquo;</p>\n'
                  '<p>You are the second-year resident. His creatinine today is 2.05 mg/dL, which the calculator turns into an estimated GFR (eGFR) '
                  'of 38 mL/min/1.73 m&sup2;. His urine ACR is 480 mg/g. He shows you a phone photo of a creatinine of 1.6 mg/dL from a private '
                  'laboratory 14 months ago. His blood pressure is 156/94 mm Hg, his glycated hemoglobin (HbA1c) is 8.4%, and his urinalysis shows '
                  '3+ protein, no red cells and no casts. He has no eye examination on record. His wife, Mrs. Lorna Dizon, asks the question every '
                  'family asks: &ldquo;Doc, magda-dialysis na po ba siya?&rdquo; (Will he need dialysis now?)</p>\n'
                  '<p>The intern on your team has written &ldquo;CKD stage 3&rdquo; and is about to move on to the next patient.</p>\n',
          'questions': ['What is his full CKD classification, and is it really chronic?',
                        'What is his risk of kidney failure, and does he need a nephrologist now?',
                        'What will the clinic plan say, and how often will you see him?']},
 'sections': [('define',
               'Define and stage',
               'Defining and staging CKD: two numbers and a cause',
               '<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline defines chronic kidney disease (CKD) as abnormalities of kidney '
               'structure or function, present for more than 3 months, with implications for health.[[ntr11_1]] In practice the two commonest markers '
               'are a GFR below 60 mL/min/1.73 m&sup2; and an albumin-to-creatinine ratio (ACR) of 30 mg/g (3 mg/mmol) or more. Other markers of damage '
               'count too: abnormal urine sediment, tubular disorders, structural abnormalities on imaging, abnormalities on biopsy, or a kidney '
               'transplant.[[ntr11_1]]</p>\n'
               '<p>KDIGO classifies CKD by Cause, GFR category and Albuminuria category (the CGA system).[[ntr11_1]] The cause comes first in the label '
               'because it decides treatment. The two numbers come next because each predicts outcomes independently: at any eGFR, more albumin means '
               'more risk of kidney failure, cardiovascular death and death from any cause.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>GFR category</th><th>eGFR (mL/min/1.73 m&sup2;)</th><th>Albuminuria category</th>'
               '<th>ACR</th></tr></thead><tbody>'
               '<tr><td>G1</td><td>&ge;90</td><td>A1 (normal to mildly increased)</td><td>&lt;30 mg/g (&lt;3 mg/mmol)</td></tr>'
               '<tr><td>G2</td><td>60&ndash;89</td><td>A2 (moderately increased)</td><td>30&ndash;300 mg/g (3&ndash;30 mg/mmol)</td></tr>'
               '<tr><td>G3a</td><td>45&ndash;59</td><td>A3 (severely increased)</td><td>&gt;300 mg/g (&gt;30 mg/mmol)</td></tr>'
               '<tr><td>G3b</td><td>30&ndash;44</td><td colspan="2" rowspan="3">G1 and G2 count as CKD only with another marker of damage, such as albuminuria</td></tr>'
               '<tr><td>G4</td><td>15&ndash;29</td></tr>'
               '<tr><td>G5</td><td>&lt;15</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Which eGFR.</strong> Use a validated creatinine equation, now the race-free Chronic Kidney Disease Epidemiology Collaboration '
               '(CKD-EPI) 2021 equation in most laboratories.[[ntr11_4]] Creatinine-based eGFR misleads in people with very low or very high muscle '
               'mass, amputations, cirrhosis or wasting. KDIGO recommends using an equation that combines creatinine and cystatin C (eGFRcr-cys) in '
               'clinical situations when the creatinine estimate is less accurate (1C), and, where cystatin C is available, using the combined '
               'estimate to assign the GFR category (1B).[[ntr11_1]] In many Philippine provinces cystatin C is not on the laboratory menu, or the '
               'family pays for it out of pocket. Then state the limitation in your note, look for other evidence, and do not stage a cachectic '
               'patient on creatinine alone without saying so.</p>\n'
               '<p><strong>Proving chronicity.</strong> One abnormal value is not CKD. KDIGO lists the ways to prove a duration of at least 3 months: '
               'past eGFR values, past urine tests, imaging (small kidneys, thin cortex), biopsy findings, or a history that explains a long-standing '
               'process.[[ntr11_1]] After acute kidney injury (AKI), wait 3 months after discharge before diagnosing CKD.[[ntr11_1]] The phone photo, '
               'the barangay health center logbook, the old discharge summary in a plastic envelope: in the Philippines, chronicity is often proven by '
               'detective work, not by the hospital information system.</p>\n'
               '<p><strong>Albuminuria needs confirming.</strong> Urine albumin varies from day to day with fever, exercise, a high-protein meal, '
               'menstruation, urinary infection and uncontrolled glucose or blood pressure. KDIGO notes that rises beyond 100% or falls beyond 50% are '
               'probably beyond random fluctuation.[[ntr11_1]] Repeat a high ACR on an early-morning sample before you label a patient A2 or A3, and '
               'record the method. A dipstick reading of protein is a screen, not a category.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Trap</th><th>Why it misleads</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>A single high creatinine during an illness</td><td>AKI or acute kidney disease, not CKD</td><td>Repeat after recovery; label AKI '
               'until 3 months have passed</td></tr>'
               '<tr><td>&ldquo;Normal&rdquo; creatinine in a small, older woman</td><td>Low muscle mass hides lost filtration</td><td>Read the eGFR, '
               'not the creatinine; consider cystatin C</td></tr>'
               '<tr><td>Creatinine rise after a gym diet with protein shakes or creatine</td><td>Generation, not filtration, has changed</td><td>Ask '
               'about supplements; repeat after stopping</td></tr>'
               '<tr><td>One ACR during a urinary infection</td><td>Inflammation raises albumin</td><td>Treat, then repeat</td></tr>'
               '<tr><td>&ldquo;CKD stage 3&rdquo; with no albuminuria category</td><td>Hides half the risk</td><td>Always write G and A, and the cause</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Write CKD as cause, G category and A category, with the date range that proves chronicity. &ldquo;CKD stage 3&rdquo; alone is an '
               'incomplete sentence.}}\n'
               '\n{{fig:ntr11_a}}\n'),
              ('risk',
               'Estimate risk',
               'Estimating risk: the heat map, the KFRE and the heart',
               '<p>The KDIGO heat map turns the two numbers into colors: green (low risk), yellow (moderately increased), orange (high) and red (very high). '
               'The colors summarize pooled data from large cohorts on kidney failure, cardiovascular death, AKI and death from any cause.[[ntr11_1]] They '
               'are a population picture. They do not tell Mr. Dizon his own chance of reaching dialysis, and they do not use his age.</p>\n'
               '<p><strong>The kidney failure risk equation (KFRE).</strong> Tangri and colleagues derived the KFRE in 3,449 Canadian patients with '
               'CKD G3 to G5 referred to nephrologists, and validated it in a second cohort of 4,942. The most accurate model used eight laboratory and '
               'demographic variables (C statistic 0.917 in development, 0.841 in validation); a simpler four-variable model uses age, sex, eGFR and '
               'ACR.[[ntr11_2]] An individual participant meta-analysis of 31 cohorts, 721,357 people with CKD G3 to G5 in more than 30 countries, '
               'found excellent discrimination (C statistic 0.90 at 2 years, 0.88 at 5 years). Calibration was adequate in North America, but the '
               'original equation overestimated risk in some non-North American cohorts, and a calibration factor improved it.[[ntr11_3]] No Philippine '
               'cohort was among them. Read the result as an estimate with a margin, and expect it may run high for Filipino patients.</p>\n'
               '<p>KDIGO 2024 recommends using an externally validated risk equation to estimate the absolute risk of kidney failure in people with '
               'CKD G3 to G5 (1A). Its practice points (ungraded) attach actions to thresholds: a 5-year risk of 3% to 5% can be used to decide on '
               'nephrology referral; a 2-year risk above 10% can time multidisciplinary care; and a 2-year risk above 40% can guide modality education, '
               'preparation for kidney replacement therapy (KRT) including vascular access, and transplant referral.[[ntr11_1]] These sit alongside, '
               'not in place of, the eGFR and ACR criteria and clinical judgment.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>KFRE result</th><th>What it can trigger (KDIGO practice point)</th><th>What you do in the '
               'clinic</th></tr></thead><tbody>'
               '<tr><td>5-year risk below 3%</td><td>Care can usually stay in primary care if no other criterion applies</td><td>Treat risk factors; '
               'repeat eGFR and ACR at least yearly</td></tr>'
               '<tr><td>5-year risk 3% to 5% or more</td><td>Nephrology referral</td><td>Refer with the trend, the cause workup and the medicine list</td></tr>'
               '<tr><td>2-year risk above 10%</td><td>Multidisciplinary CKD care</td><td>Dietitian, diabetes educator, social worker, pharmacist</td></tr>'
               '<tr><td>2-year risk above 40%</td><td>Modality education, access planning, transplant referral</td><td>Hemodialysis, peritoneal dialysis, '
               'transplant and conservative care discussed with the family; vein preservation</td></tr>'
               '</tbody></table></div>\n'
               '{{formula:<strong>Arithmetic illustration, not a target.</strong> For Mr. Dizon (52, male, eGFR 38, ACR 480 mg/g), the four-variable KFRE '
               'with the North American calibration gives a 5-year risk of about 15% and a 2-year risk of about 5%. With the non-North American '
               'calibration factor, both are a little lower. Run the site calculator yourself; do not copy these figures into a chart.}}\n'
               '<p><strong>The heart comes first in most patients.</strong> The same heat map predicts cardiovascular death, and in the yellow and orange '
               'cells cardiovascular events are more common than kidney failure. The American Heart Association (AHA) cardiovascular-kidney-metabolic '
               '(CKM) advisory places CKD inside one syndrome with obesity, diabetes and heart disease, and stages it from 0 (no risk factors) to 4 '
               '(clinical cardiovascular disease). Moderate- to high-risk CKD by the KDIGO heat map sits in stage 2, and very high-risk CKD counts as a '
               'risk equivalent in stage 3.[[ntr11_5]] CKM staging is a framework for prevention, not trial evidence that staging itself improves '
               'outcomes. The AHA Predicting Risk of cardiovascular disease EVENTs (PREVENT) equations, derived and validated in more than 6 million US '
               'adults aged 30 to 79, include eGFR and can add ACR; adding ACR improved calibration in people with ACR above 300 mg/g.[[ntr11_6]] '
               'PREVENT has not been validated in a Philippine population; use it as a structured estimate, not a verdict.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">On the ward &middot; fictional</span><p>Aling Mercedes, 81, from San Fernando, Pampanga, '
               'has an eGFR of 31 and an ACR of 12 mg/g, stable for six years. The KFRE gives her a 5-year risk well under 3%. Her daughter wants a '
               'dialysis access &ldquo;just in case.&rdquo;</p><p>You explain that she is far more likely to die of her heart disease than to need '
               'dialysis, and that the plan is blood pressure, her statin and avoiding nephrotoxins.</p><p class="tc-scene-take"><b>What this shows.</b> '
               'A low eGFR in an old, stable patient without albuminuria is a different disease from the same eGFR in a 52-year-old with heavy '
               'albuminuria.</p></div>\n'
               '{{key:Put a number on kidney failure risk in every patient with CKD G3 to G5, and say out loud which is more likely: the heart or '
               'dialysis.}}\n'
               '\n{{fig:ntr11_b}}\n'),
              ('cause',
               'Find the cause',
               'Finding the cause: is this really diabetic kidney disease?',
               '<p>In the Philippines, diabetes and hypertension are the leading causes of kidney failure. That is exactly why the label is applied too '
               'quickly. A patient with diabetes can also have immunoglobulin A (IgA) nephropathy, membranous nephropathy, lupus, obstruction from an enlarged prostate, '
               'stones, reflux nephropathy, an analgesic or herbal injury, or a hereditary disease. Each has its own treatment, and some are '
               'reversible.</p>\n'
               '<p>The causal chain of diabetic kidney disease (DKD) explains which features fit. Years of hyperglycemia raise sodium-glucose reabsorption '
               'in the proximal tubule, less sodium reaches the macula densa, tubuloglomerular feedback dilates the afferent arteriole, and glomerular '
               'pressure rises (Module 13 traces this). Albuminuria usually rises slowly before the eGFR falls, and the same microvascular injury '
               'appears in the retina. A picture that breaks this chain suggests another cause.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Fits diabetic kidney disease</th><th>Suggests another cause</th></tr>'
               '</thead><tbody>'
               '<tr><td>Duration of diabetes</td><td>Long, often 10 years or more in type 2 (onset is often uncertain)</td><td>Heavy proteinuria within '
               'months of diagnosis</td></tr>'
               '<tr><td>Retina</td><td>Diabetic retinopathy present</td><td>No retinopathy despite heavy albuminuria (especially in type 1)</td></tr>'
               '<tr><td>Urine sediment</td><td>Bland</td><td>Dysmorphic red cells, red cell casts</td></tr>'
               '<tr><td>Course</td><td>Gradual albuminuria, then gradual eGFR decline</td><td>Rapid eGFR fall, sudden nephrotic syndrome</td></tr>'
               '<tr><td>Systemic clues</td><td>Other microvascular disease</td><td>Rash, arthritis, hemoptysis, weight loss, new anemia out of '
               'proportion</td></tr>'
               '<tr><td>Imaging</td><td>Normal-sized or large kidneys</td><td>Asymmetric kidneys, hydronephrosis, cysts</td></tr>'
               '</tbody></table></div>\n'
               '<p>The cause workup at your stage is usually modest and inexpensive: a repeat ACR, a microscopic urinalysis read by someone who knows '
               'what a dysmorphic red cell looks like (Module 4), a kidney ultrasound, a fundus examination, a careful medicine and supplement history, '
               'and, when the picture suggests it, serologies. Biopsy belongs to the nephrologist and to a patient whose management would change.</p>\n'
               '<p><strong>The medicine and supplement history.</strong> Ask about nonsteroidal anti-inflammatory drugs (NSAIDs) and other pain relievers bought without prescription for back pain from '
               'driving or farm work, herbal &ldquo;kidney cleanse&rdquo; capsules, lagundi or other decoctions, imported slimming products and '
               'anabolic steroids. Write the brand names; bring the bottles if possible. Module 16 covers the nephrotoxic ones.</p>\n'
               '<div class="tc-keyp"><span class="tc-lab">In children</span>The causes are different: congenital anomalies of the kidney and urinary '
               'tract (CAKUT), reflux and hereditary diseases dominate, and diabetes is rare. GFR is estimated with pediatric equations, and albuminuria '
               'or proteinuria thresholds and referral criteria are written for children: KDIGO advises referring a child with confirmed albuminuria or '
               'proteinuria, persistent hematuria, any sustained fall in eGFR, hypertension, or a urinary tract anomaly.[[ntr11_9]] Growth, '
               'neurodevelopment and the transition to adult care are part of CKD care. See <a href="attending-pediatric-nephrologist-17-pediatric-ckd.html">'
               'Attending Pediatric Nephrologist, Module 17</a>.</div>\n'
               '{{key:Before you write &ldquo;diabetic kidney disease,&rdquo; check the retina, the sediment, the ultrasound and the speed of decline. '
               'If one does not fit, say so and look further.}}\n'),
              ('referral-plan',
               'Refer and plan',
               'Referral, follow-up and the clinic plan',
               '<p><strong>Who goes to the nephrologist.</strong> KDIGO 2024 lists referral criteria for adults, including a consistent eGFR below 30 '
               'mL/min/1.73 m&sup2;, a consistent ACR of 300 mg/g or more, a 5-year kidney failure risk of 3% to 5% or more, accelerated progression, '
               'AKI or an abrupt sustained fall in eGFR, persistent unexplained hematuria with red cell casts, hypertension refractory to four or more '
               'agents, persistent potassium abnormalities, recurrent or extensive stones, and hereditary kidney disease.[[ntr11_1]] A referral is not '
               'a transfer of ownership. Most patients will be co-managed: the primary care team carries the daily care, and the nephrologist sets the '
               'kidney-specific plan.</p>\n'
               '<p><strong>How often to check.</strong> KDIGO advises assessing albuminuria and GFR at least once a year in people with CKD, and more '
               'often as the heat-map risk rises (practice point).[[ntr11_1]] Draw the trend, not just the latest point. A small early fall in eGFR after '
               'starting a renin-angiotensin system inhibitor (RASi) or a sodium-glucose cotransporter 2 (SGLT2) inhibitor is expected hemodynamics; KDIGO '
               'advises continuing the RASi unless creatinine rises by more than 30% within 4 weeks (practice point).[[ntr11_1]] A fall of the same size '
               'during dengue season is a different story (Module 9).</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Stage of training</th><th>What you own in the CKD clinic</th></tr></thead><tbody>'
               '<tr><td>Intern</td><td>Collect old values (phone photos, logbooks), stage G and A, list every medicine and supplement, present the trend</td></tr>'
               '<tr><td>Resident</td><td>Prove chronicity, order the cause workup, run the KFRE, start or adjust kidney protection with the attending, '
               'write the referral</td></tr>'
               '<tr><td>Fellow</td><td>Set follow-up intervals by risk, lead modality and conservative care conversations, write the shared plan for '
               'primary care, audit who is lost to follow-up</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Philippine practice.</strong> Many patients reach you through a barangay health center or a PhilHealth Konsulta provider, '
               'now part of the PhilHealth YAKAP primary care program. The published Konsulta laboratory list includes serum creatinine, urinalysis, '
               'fasting blood sugar, HbA1c and a lipid profile, but not a urine albumin-to-creatinine ratio.[[ntr11_7]][[ntr11_8]] That gap matters: '
               'a dipstick misses moderately increased albuminuria, and without an ACR you cannot place the patient on the heat map or run the KFRE. '
               'Where the family cannot pay for an ACR, write the dipstick result honestly, mark the A category as unknown, and plan the test for when '
               'it can be done. Diabetic clinics in local government units are a natural place to screen; the fellow can help them set up an annual '
               'creatinine-and-ACR day.</p>\n'
               '<p><strong>The plan the patient carries.</strong> Write it in short lines the patient and the next doctor can read: the diagnosis in CGA '
               'form, the kidney failure risk in words (&ldquo;about 15 in 100 over 5 years&rdquo;), the targets set by the attending, the medicines that '
               'protect the kidney and the ones to avoid, the date of the next creatinine and ACR, and what should bring the patient back early. Use '
               'Tagalog, Kapampangan, Cebuano or the family&rsquo;s own language for the spoken explanation. KDIGO has begun a focused update on '
               'medications management in CKD; check the guideline page for its status before you teach the current statements as final.[[ntr11_10]]</p>\n'
               '{{call:Stop and call the attending nephrologist (per unit protocol, but always ask the attending nephrologist for guidance) when you '
               'find:<ul><li>eGFR falling fast, or a new creatinine rise with oliguria</li><li>Potassium of 6.0 mmol/L or higher, or severe acidosis</li>'
               '<li>Red cell casts or dysmorphic hematuria with a falling eGFR</li><li>New nephrotic syndrome or edema that is not responding</li>'
               '<li>Uremic symptoms: vomiting, confusion, pericardial rub, bleeding</li><li>eGFR below 15 mL/min/1.73 m&sup2; with no plan for kidney '
               'replacement or conservative care</li></ul>}}\n'
               '{{key:Every CKD patient leaves your clinic with three things written down: the CGA label, the risk in words, and the date of the next '
               'eGFR and ACR.}}\n')],
 'debrief': ['<p><strong>Classification and chronicity.</strong> He has CKD G3b A3, probably due to diabetic kidney disease with hypertension, '
             'not yet proven. Chronicity is supported by the creatinine of 1.6 mg/dL 14 months ago (eGFR about 51) and by heavy albuminuria in a '
             'man with 11 years of diabetes, but the ACR should be repeated on an early-morning sample, and an ultrasound and a fundus examination '
             'should be done. The sediment is bland, which fits. The &ldquo;kidney cleanse&rdquo; capsule must be identified and stopped. The '
             'intern&rsquo;s &ldquo;CKD stage 3&rdquo; misses the A3, the cause and the speed of decline, about 13 mL/min/1.73 m&sup2; in a little '
             'over a year.</p>\n',
             '<p><strong>Risk and referral.</strong> The four-variable KFRE gives roughly a 15% 5-year risk and a 5% 2-year risk with the North '
             'American calibration, lower with the non-North American factor. Either way, the 5-year risk exceeds the 3% to 5% referral threshold, '
             'and his ACR of 480 mg/g is itself a referral criterion. He needs a nephrologist now, not dialysis now. Tell Mrs. Dizon plainly: he does '
             'not need dialysis today, his risk over the next few years is real, and treatment can lower it. Cardiovascular risk is high too, and it '
             'deserves the same attention.</p>\n',
             '<p><strong>The clinic plan.</strong> Repeat creatinine and ACR to confirm, ultrasound, fundus examination, potassium and bicarbonate. '
             'With the attending: blood pressure control (Module 12), losartan at the highest tolerated dose taken every day, an SGLT2 inhibitor, '
             'glycemic control with attention to the metformin dose at his eGFR, and a statin (Module 13). Stop the supplement and NSAIDs. Refer to '
             'nephrology with the trend and medicine list, and see him at least every 3 to 4 months while his risk is high, adjusting the interval '
             'to his course. Ask whether PhilHealth YAKAP medicines can cut his costs.</p>\n'],
 'skills': {'title': 'CKD evaluation, risk and referral',
            'intro': 'Complete with a preceptor, in clinic or on the ward. Sign-off is local.',
            'items': [('Stages CKD by cause, GFR category and albuminuria category, with evidence of chronicity', False),
                      ('Identifies when creatinine-based eGFR is unreliable and states the limitation in the note', False),
                      ('Runs the four-variable KFRE and explains the result to a patient in plain words', False),
                      ('Lists the findings that argue against diabetic kidney disease and orders the matching workup', False),
                      ('Writes a referral and a follow-up plan that a primary care physician can carry out', False)],
            'placement': 'Medicine outpatient clinic, CKD clinic or ward'},
 'quiz': [('A 60-year-old woman has an eGFR of 52 mL/min/1.73 m&sup2; and an ACR of 45 mg/g, both confirmed twice over 6 months. How is her CKD '
           'classified?',
           ['G3a A2', 'G2 A2', 'G3b A1', 'G3a A3'],
           0,
           'eGFR 45&ndash;59 is G3a and ACR 30&ndash;300 mg/g is A2. G3b would need an eGFR of 30&ndash;44; A3 would need an ACR above 300 mg/g.'),
          ('KDIGO 2024 recommends which approach to kidney failure risk in CKD G3 to G5?',
           ['Use eGFR category alone to decide referral',
            'Use an externally validated risk equation to estimate absolute risk of kidney failure (1A)',
            'Refer every patient with eGFR below 60',
            'Use the heat map color as the individual risk'],
           1,
           'Recommendation 2.2.1 is graded 1A. The heat map is a population summary and does not include age; eGFR alone ignores albuminuria.'),
          ('In a CKD clinic, a patient&rsquo;s 2-year KFRE risk is 45%. According to KDIGO 2024 practice points, what should this prompt?',
           ['Nothing new; risk equations are only for primary care',
            'Repeat the KFRE in 5 years',
            'Modality education, kidney replacement preparation including access planning, and transplant referral',
            'Immediate dialysis initiation'],
           2,
           'A 2-year risk above 40% can guide modality education, preparation for KRT and transplant referral. It is not an indication to start '
           'dialysis, which depends on symptoms and complications.'),
          ('A 45-year-old man with type 2 diabetes diagnosed 2 years ago has nephrotic-range proteinuria, no retinopathy and dysmorphic red cells '
           'in the urine. What is the best next step?',
           ['Label diabetic kidney disease and intensify glucose control',
            'Discuss with nephrology for evaluation of a non-diabetic cause, including possible biopsy',
            'Repeat the ACR in 1 year',
            'Start dialysis planning'],
           1,
           'Short duration, no retinopathy and an active sediment break the diabetic chain. Intensifying glucose control alone would miss a '
           'treatable glomerular disease.'),
          ('An 80-year-old woman has a stable eGFR of 33 for 5 years, ACR 15 mg/g and a 5-year KFRE risk of 1.5%. Her family asks for a fistula. '
           'What fits the evidence best?',
           ['Create a fistula now to be safe',
            'Refer for transplant evaluation',
            'Explain that her kidney failure risk is low, focus on cardiovascular protection and nephrotoxin avoidance, and review yearly',
            'Start an urgent dialysis education program'],
           2,
           'Her risk is far below the 3% to 5% referral threshold and below the 40% 2-year preparation threshold; cardiovascular events are '
           'more likely than kidney failure. An access now would expose her to a procedure she probably will never need.')],
 'terms': [('ACR', 'Albumin-to-creatinine ratio'),
           ('AHA', 'American Heart Association'),
           ('AKI', 'Acute kidney injury'),
           ('CAKUT', 'Congenital anomalies of the kidney and urinary tract'),
           ('CGA', 'Cause, GFR category and albuminuria category (KDIGO classification)'),
           ('CKD', 'Chronic kidney disease'),
           ('CKD-EPI', 'Chronic Kidney Disease Epidemiology Collaboration'),
           ('CKM', 'Cardiovascular-kidney-metabolic'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('eGFRcr-cys', 'eGFR from creatinine and cystatin C combined'),
           ('GFR', 'Glomerular filtration rate'),
           ('HbA1c', 'Glycated hemoglobin'),
           ('IgA', 'Immunoglobulin A'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KFRE', 'Kidney failure risk equation'),
           ('KRT', 'Kidney replacement therapy'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('RASi', 'Renin-angiotensin system inhibitor'),
           ('PREVENT', 'Predicting Risk of cardiovascular disease EVENTs (AHA equations)'),
           ('SGLT2', 'Sodium-glucose cotransporter 2'),
           ('YAKAP', 'Yaman ng Kalusugan Program (PhilHealth primary care program)')],
 'readings': [('attending-nephrologist-09-ckd-progression.html', 'Attending Nephrologist, Module 9: CKD progression'),
              ('understanding-ckd.html', 'Understanding CKD'),
              ('diabetes-kidney-disease-not-always-diabetic.html', 'Diabetes and Kidney Disease: Not Always Diabetic'),
              ('how-to-properly-assess-kidney-function.html', 'How to Properly Assess Kidney Function')],
 'calcs': ['calc-kfre.html', 'calc-ckm-staging.html', 'calc-ckd-progression-slope.html', 'calc-uacr-trend.html', 'calc-prevent-cvd.html',
           'calc-egfr-ckd-epi.html']}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
