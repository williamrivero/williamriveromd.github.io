# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 16: Renal pharmacology and medication stewardship.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2024 chapter 4
practice points and KDIGO 2012 AKI aminoglycoside grades (2A, 2B) checked against KDIGO summaries; Cockcroft-Gault, Lapi 2013,
Matzke 2011, Rybak 2020, Davenport 2020 and Vanherweghem 1993 against PubMed records; FDA metformin labeling against the 2016
communication. Calculations in the case are arithmetic illustrations. No doses. Fictional case."""

MODULE = {'image_alt': 'A Filipino medical intern lays out an elderly farmer&rsquo;s plastic bag of tablets, sachets and an unlabeled herbal bottle on a ward table while a resident checks a drug reference on a phone.',
 'objectives': ['<strong>Intern:</strong> Reconcile every medicine, supplement and herbal product a patient takes, and flag the nephrotoxins and the drugs that accumulate when kidney function falls.',
                '<strong>Resident:</strong> Adjust drugs for kidney function using the right estimate (creatinine clearance (CrCl), indexed or nonindexed estimated glomerular filtration rate, or a combined creatinine and cystatin C estimate), and recognize when no estimate is valid because creatinine is not at steady state.',
                '<strong>Fellow:</strong> Lead medication stewardship for patients on hemodialysis, continuous kidney replacement therapy (CKRT) and after transplant, including drug removal by dialysis, therapeutic drug monitoring and sick-day plans.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the medicine list as a kidney intervention</span>As an <strong>intern</strong>, '
        'you are the person most likely to find the plastic bag of tablets, the neighbor&rsquo;s &ldquo;rayuma&rdquo; capsules and the '
        'decoction in a softdrink bottle. That discovery often explains the admission. As a <strong>resident</strong>, you choose the kidney '
        'estimate that fits the drug and the patient, and you stop or adjust what harms. As a <strong>fellow</strong>, you advise on drugs in '
        'dialysis, CKRT and transplant patients, where the kidney has been replaced by a machine or a graft and the old rules no longer '
        'apply.</div>\n'
        '{{plain:Think of a drug in the body as water poured into a basin with a drain. The size of the basin is the volume of distribution; the '
        'width of the drain is the clearance. The water level is the drug concentration. Narrow the drain and the level rises with every '
        'pour.}}\n'
        '<p>The picture has a limit. The body has more than one drain: the kidney, the liver and the gut wall all clear drugs, and kidney '
        'disease narrows the liver and gut drains too, by inhibiting drug-metabolizing enzymes and transporters. The basin also changes shape: '
        'edema and ascites enlarge it for water-soluble drugs, while uremic toxins and low albumin free more drug from its binding proteins. '
        'Some drugs leave behind active metabolites that only the kidney can clear. And the drain can be widened again by dialysis, which removes '
        'some drugs efficiently and others hardly at all. Dosing in kidney disease is the art of estimating all of these at once.</p>\n'
        '{{cards:Key numbers|Drug dosing estimate (KDIGO 2024)::Validated creatinine-based eGFR equations are appropriate for most people and settings '
        '(practice point)|Narrow therapeutic index (KDIGO 2024)::Combined creatinine and cystatin C equations, or measured GFR, may be indicated (practice '
        'point)|Extremes of body size (KDIGO 2024)::eGFR not indexed to body surface area may be indicated (practice point)|NSAID triple therapy (nested '
        'case-control, 487,372 users)::AKI rate ratio 1.31; 1.82 in the first 30 days|Aminoglycosides (KDIGO 2012 AKI)::Avoid unless no suitable, less '
        'nephrotoxic alternative (2A)|Metformin (FDA labeling)::Contraindicated below an eGFR of 30 mL/min/1.73 m&sup2;}}\n'
        '<p>Most medication harm in kidney disease is predictable: a drug that accumulates, a nephrotoxin added to a dry patient, or a prescription '
        'copied forward for years while the eGFR fell. A few harms are hidden in products nobody wrote down. Your work is to find every substance, '
        'choose the right kidney estimate for each drug, stop what injures, and leave a plan for when to restart.</p>\n',
 'case': {'title': 'The farmer with the bag of rayuma pills',
          'html': '<p>Saturday, 11 p.m., the emergency room of a provincial hospital in Cabanatuan City, Nueva Ecija. Mr. Ernesto Villanueva, 74, a '
                  'retired rice farmer, has vomited for three days and barely eaten. He weighs 52 kg and is about 160 cm tall. He has type 2 '
                  'diabetes and hypertension. His prescribed medicines are metformin, losartan and hydrochlorothiazide. For knee pain he has taken '
                  '&ldquo;rayuma&rdquo; capsules from a neighbor twice a day for a month, plus mefenamic acid bought at the corner drugstore.</p>\n'
                  '<p>His blood pressure is 96/60 mm Hg lying down, pulse 108. His creatinine is 3.1 mg/dL; it was 1.3 mg/dL at a health center '
                  'check three months ago. Potassium is 5.9 mmol/L, bicarbonate 14 mmol/L, lactate 4.2 mmol/L, glucose 212 mg/dL. Urine output since '
                  'arrival is 80 mL in 3 hours.</p>\n'
                  '<p>You are the admitting resident. The intern hands you a plastic bag: blister packs, loose white tablets, the unlabeled capsules '
                  'and a bottle of brown liquid. The emergency physician has ordered intravenous vancomycin and amikacin &ldquo;for possible '
                  'sepsis&rdquo; and asks you for the doses.</p>\n',
          'questions': ['Which of his medicines and products are contributing to this admission, and what will you stop?',
                        'Which kidney estimate will you use to dose his antibiotics tonight, and why are both equations misleading right now?',
                        'What plan will he and his family take home about restarting medicines and sick days?']},
 'sections': [('pk',
               'Pharmacokinetics',
               'Pharmacokinetics in kidney disease: the basin, the drains and the binding',
               '<p>Four quantities decide a drug&rsquo;s concentration over time: absorption, volume of distribution, protein binding and clearance. '
               'Kidney disease changes all four. The Kidney Disease: Improving Global Outcomes (KDIGO) conference on drug dosing noted that although '
               'glomerular filtration rate (GFR) is the metric used to adjust doses, kidney disease also affects nonrenal clearance, a point most pharmacokinetic studies have not '
               'captured, and that patients on kidney replacement therapy and children are poorly studied.[[ntr16_2]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Quantity</th><th>What kidney disease does</th><th>What you see or do</th></tr></thead><tbody>'
               '<tr><td>Clearance (renal)</td><td>Falls with GFR for drugs excreted unchanged in urine</td><td>Accumulation: reduce the dose, lengthen the '
               'interval, or choose another drug</td></tr>'
               '<tr><td>Clearance (nonrenal)</td><td>Uremia inhibits some liver and gut enzymes and transporters</td><td>Some &ldquo;liver&rdquo; drugs '
               'still accumulate</td></tr>'
               '<tr><td>Active metabolites</td><td>Renally cleared metabolites build up</td><td>Toxicity from a parent drug at a &ldquo;normal&rdquo; dose '
               '(for example, sedation from opioid metabolites)</td></tr>'
               '<tr><td>Volume of distribution</td><td>Edema, ascites and overload enlarge it for water-soluble drugs</td><td>The loading dose is not reduced '
               'for kidney function, and may need to be larger</td></tr>'
               '<tr><td>Protein binding</td><td>Low albumin and uremic toxins raise the free fraction</td><td>A &ldquo;normal&rdquo; total level can '
               'hide a high free level (phenytoin is the classic example)</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Loading versus maintenance.</strong> The loading dose fills the basin, so it depends on the volume of distribution, not on '
               'the drain. In a septic patient with acute kidney injury (AKI), cutting the first dose of an antibiotic because the creatinine is high leaves the infection '
               'untreated during the hours that matter most. The maintenance dose replaces what the drains remove, so that is where kidney function '
               'enters. Ask the pharmacist and the attending for both numbers separately.</p>\n'
               '<p><strong>Half-life and time to steady state.</strong> When clearance falls, half-life lengthens, and so does the time to reach a '
               'steady concentration. A drug whose level would have stabilized in a day may take several days in kidney failure, and a toxic level may '
               'appear on day 4 of a regimen that looked fine on day 1.</p>\n'
               '{{key:Separate the loading dose from the maintenance dose. Kidney function changes the second, rarely the first.}}\n'
               '\n{{fig:ntr16_a}}\n'),
              ('adjust',
               'Which estimate',
               'Adjusting for kidney function: which number, and when none is valid',
               '<p>Drug labels written before 2010 usually based their kidney bands on creatinine clearance estimated by the Cockcroft&ndash;Gault '
               'equation, derived in 1976 from 249 patients and compared against measured clearance in 236, with a correlation of 0.83. It uses age, '
               'weight and serum creatinine, with 15% less for women.[[ntr16_3]] Modern laboratories report eGFR from the Chronic Kidney Disease '
               'Epidemiology Collaboration (CKD-EPI) 2021 equation, indexed to a body surface area of 1.73 m&sup2;.[[ntr16_4]] The two numbers often '
               'disagree, most of all in small, older patients.</p>\n'
               '<p>KDIGO 2024 gives three practice points (ungraded): validated creatinine-based eGFR equations are appropriate for drug dosing in most '
               'people and settings; for drugs with a narrow therapeutic range, or when the creatinine estimate is unreliable, equations that combine '
               'creatinine and cystatin C, or a measured GFR, may be indicated; and at extremes of body weight, eGFR not indexed for body surface area '
               'may be indicated.[[ntr16_1]] Nonindexed eGFR in mL/min is the indexed value multiplied by the patient&rsquo;s body surface area and '
               'divided by 1.73.</p>\n'
               '{{formula:<strong>Arithmetic illustration, not a dose.</strong> Mr. Villanueva&rsquo;s baseline creatinine of 1.3 mg/dL at age 74 gives a '
               'CKD-EPI 2021 eGFR of about 58 mL/min/1.73 m&sup2;. His body surface area is about 1.5 m&sup2;, so his nonindexed eGFR is about 50 mL/min. '
               'Cockcroft&ndash;Gault gives about 37 mL/min for the same creatinine. Tonight&rsquo;s creatinine of 3.1 mg/dL would give a '
               'Cockcroft&ndash;Gault value near 15 mL/min, but that number is not valid, because creatinine has not reached steady state.}}\n'
               '<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Better estimate</th><th>Why</th></tr></thead><tbody>'
               '<tr><td>Stable chronic kidney disease (CKD), most drugs</td><td>Creatinine-based eGFR</td><td>KDIGO 2024 practice point</td></tr>'
               '<tr><td>Label states creatinine clearance bands</td><td>Cockcroft&ndash;Gault, or nonindexed eGFR as the label and pharmacist advise</td><td>The '
               'label was tested in those units</td></tr>'
               '<tr><td>Very small or very large body size</td><td>Nonindexed eGFR (mL/min)</td><td>Drug clearance depends on the patient&rsquo;s actual '
               'GFR, not one scaled to 1.73 m&sup2;</td></tr>'
               '<tr><td>Narrow therapeutic index, low muscle mass, amputation</td><td>eGFRcr-cys or measured GFR, if available</td><td>Creatinine '
               'misleads; errors are costly</td></tr>'
               '<tr><td>AKI with creatinine rising or falling</td><td>No equation is valid; use the clinical picture, urine output, kinetic estimates and '
               'drug levels</td><td>Equations assume steady state</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>When creatinine is moving.</strong> All the equations assume that creatinine production equals excretion. When filtration '
               'falls suddenly, creatinine takes days to rise to its new level, so any equation applied to a rising creatinine overestimates GFR. In '
               'the first day of severe AKI the true GFR may be close to zero while the equation still says 25. Kinetic eGFR (Module 2) helps; '
               'urine output and drug levels help more. As the kidney recovers, the opposite happens and doses that were right on day 3 become too low '
               'by day 7.</p>\n'
               '<p><strong>Philippine practice.</strong> The site&rsquo;s Drug Index (<a href="../drugs/">Dosis</a>) shows the kidney dosing bands from '
               'United States labels in the measure the label uses, so a band written in creatinine clearance stays in creatinine clearance. Cystatin C '
               'is unavailable or costly in many provinces; when you cannot measure it, write which estimate you used and why.</p>\n'
               '{{key:Name the estimate next to every kidney-adjusted dose: eGFR, nonindexed eGFR or creatinine clearance. In AKI, write that no '
               'estimate is at steady state.}}\n'),
              ('nephrotox',
               'Nephrotoxins',
               'Nephrotoxins: nonsteroidal anti-inflammatory drugs (NSAIDs), aminoglycosides, vancomycin, contrast and herbal products',
               '<p><strong>NSAIDs and the triple whammy.</strong> When blood volume or pressure falls, the kidney holds GFR up by two levers: '
               'prostaglandins dilate the afferent arteriole, and angiotensin II constricts the efferent arteriole. A nonsteroidal anti-inflammatory '
               'drug (NSAID) removes the first lever; an angiotensin-converting enzyme (ACE) inhibitor or angiotensin receptor blocker (ARB), together called renin-angiotensin system inhibitors (RASi), removes '
               'the second; a diuretic lowers the volume that both were defending. In a cohort of 487,372 users of antihypertensive drugs in the United '
               'Kingdom, double combinations with an NSAID were not associated with more AKI, but the triple combination was (rate ratio 1.31), most '
               'of all in the first 30 days (1.82).[[ntr16_5]] The study was observational and cannot prove cause, but the physiology and the timing '
               'point the same way. In the Philippines, mefenamic acid, ibuprofen and combination pain relievers are commonly bought without a '
               'prescription; ask by brand name.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Agent</th><th>Mechanism of injury</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>NSAIDs</td><td>Afferent vasoconstriction; interstitial nephritis</td><td>Stop in AKI and advanced CKD; avoid with RASi plus '
               'diuretic</td></tr>'
               '<tr><td>Aminoglycosides</td><td>Proximal tubular uptake and necrosis</td><td>Use only without a suitable alternative; once-daily dosing; '
               'levels</td></tr>'
               '<tr><td>Vancomycin</td><td>Tubular injury, worse with high exposure and with other nephrotoxins</td><td>AUC-guided monitoring</td></tr>'
               '<tr><td>Iodinated contrast</td><td>Vasoconstriction and tubular toxicity; risk lower than once believed</td><td>Do not withhold needed '
               'imaging; prophylaxis per risk</td></tr>'
               '<tr><td>Herbal and slimming products</td><td>Interstitial fibrosis, tubular injury, hidden drugs or heavy metals</td><td>Identify, stop, '
               'report</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Aminoglycosides.</strong> KDIGO 2012 suggests not using aminoglycosides for infections unless no suitable, less nephrotoxic '
               'alternative is available (2A), and, in patients with normal kidney function in steady state, giving them as a single daily dose rather '
               'than multiple daily doses (2B).[[ntr16_7]] When they are needed in AKI, for a resistant gram-negative infection for example, the plan '
               'needs the attending, the pharmacist and drug levels.</p>\n'
               '<p><strong>Vancomycin.</strong> The 2020 revised consensus guideline from four United States pharmacy and infectious diseases societies '
               'recommends area-under-the-curve (AUC)-guided dosing and monitoring for serious methicillin-resistant <em>Staphylococcus aureus</em> '
               '(MRSA) infections, with a target AUC of 400 to 600 mg&middot;h/L (assuming a minimum inhibitory concentration of 1 mg/L), in place of '
               'trough-only monitoring, to keep efficacy while lowering kidney injury.[[ntr16_6]] Where AUC software or rapid levels are unavailable, '
               'the unit protocol and the pharmacist decide how levels are used.</p>\n'
               '<p><strong>Iodinated contrast.</strong> The American College of Radiology and National Kidney Foundation consensus concluded that the '
               'risk of AKI after intravenous contrast has been overstated, because older studies lacked control groups to separate AKI caused by '
               'contrast from AKI that merely followed it. Prophylaxis with intravenous normal saline is indicated for patients with AKI or an eGFR '
               'below 30 who are not on maintenance dialysis, and may be considered at 30 to 44 in individual high-risk cases.[[ntr16_8]] A needed computed tomography (CT) scan '
               'should not be withheld from a patient with sepsis or a stroke because of the creatinine.</p>\n'
               '<p><strong>Herbal products.</strong> In 1993, nephrologists in Brussels described nine young women with rapidly progressive interstitial '
               'fibrosis after the same slimming regimen containing Chinese herbs; all had severe kidney failure, and several started dialysis.[[ntr16_9]] That case series is now '
               'regarded as the start of what became known as aristolochic acid nephropathy. Many Philippine &ldquo;kidney cleanse,&rdquo; '
               '&ldquo;rayuma&rdquo; and slimming products have no label you can trust, and some contain undeclared steroids or NSAIDs. Ask, keep the '
               'product, report it, and treat it as a suspect until proven otherwise.</p>\n'
               '{{key:In every patient with AKI, list the NSAID, the RASi, the diuretic, the antibiotic, the contrast and the herbal product, and '
               'decide about each one by name.}}\n'),
              ('dialysis-dosing',
               'Dialysis and transplant',
               'Dosing on dialysis, CKRT and after transplant',
               '<p>Once the native kidney fails, the drain is a dialyzer, a peritoneal membrane or a graft. Whether a drug is removed depends on the drug '
               '(molecular size, protein binding, volume of distribution) and on the treatment (membrane flux, blood and dialysate flow, session length, '
               'and whether it is intermittent or continuous).[[ntr16_2]] Small, water-soluble, weakly bound drugs with a small volume of distribution '
               'are removed well; large, highly bound or widely distributed drugs are not.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Treatment</th><th>Drug removal pattern</th><th>Practical point</th></tr></thead><tbody>'
               '<tr><td>Intermittent hemodialysis</td><td>Large removal during the session, little between</td><td>Give dialyzable drugs after the session '
               'on dialysis days, as the label and pharmacist advise</td></tr>'
               '<tr><td>CKRT</td><td>Continuous removal; total clearance often higher than the old &ldquo;anuric&rdquo; doses assume</td><td>Underdosing '
               'antibiotics is a real risk; dose to the effluent rate the attending sets</td></tr>'
               '<tr><td>Prolonged intermittent therapy: sustained low-efficiency dialysis (SLED) or prolonged intermittent renal replacement therapy (PIRRT)</td><td>Between the two; evidence thin</td><td>Plan doses around the session with '
               'the pharmacist</td></tr>'
               '<tr><td>Peritoneal dialysis</td><td>Slow, continuous, usually small removal</td><td>Intraperitoneal antibiotics follow International Society for Peritoneal Dialysis (ISPD) guidance</td></tr>'
               '<tr><td>Kidney transplant</td><td>Graft function varies; calcineurin inhibitors interact widely</td><td>Check every new drug for cytochrome P450 3A4 (CYP3A4) '
               'interactions and nephrotoxicity</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Residual function counts.</strong> A patient on hemodialysis who still passes a liter of urine a day clears some drugs '
               'between sessions. Protect that function by avoiding nephrotoxins; it is worth more than any drug you could add.</p>\n'
               '<p><strong>Transplant stewardship.</strong> Tacrolimus and cyclosporine are metabolized by the cytochrome P450 3A4 system. Azole '
               'antifungals, some macrolides and some calcium channel blockers raise their levels; rifampicin and several antiepileptic drugs lower '
               'them. Each change can cause toxicity or rejection. A fellow checks every new prescription for a transplant recipient against the '
               'immunosuppressant, and asks for a level when an interacting drug starts or stops.</p>\n'
               '<div class="tc-keyp"><span class="tc-lab">In children</span>Doses are written per kilogram or per square meter of body surface area, '
               'and kidney function and drug-metabolizing enzymes mature through infancy and childhood, so the same drug behaves differently at '
               'different ages.[[ntr16_11]] Pediatric labeling, a pediatric pharmacist and the pediatric nephrologist set the dose. See '
               '<a href="attending-pediatric-nephrologist-28-medicines-safeguarding-service.html">Attending Pediatric Nephrologist, Module 28</a>.</div>\n'
               '{{key:On dialysis or CKRT, ask two questions for every drug: is it removed by this treatment, and when is the next session or the '
               'current effluent rate? Then dose with the pharmacist.}}\n'),
              ('sick-day',
               'Sick days',
               'Sick-day plans and restarting medicines',
               '<p>During vomiting, diarrhea, fever or poor intake, some medicines that protect the kidney in health can harm it when the patient is '
               'dry: RASi and diuretics deepen the fall in GFR, sodium-glucose cotransporter 2 (SGLT2) inhibitors add volume loss and the risk of ketoacidosis, metformin can '
               'accumulate and contribute to lactic acidosis if the kidney fails, and NSAIDs remove the last defense. Sulfonylureas and insulin can '
               'cause hypoglycemia when the patient is not eating and clearance falls.</p>\n'
               '<p>KDIGO 2024 suggests considering planned discontinuation of medicines such as metformin, ACE inhibitors, ARBs and SGLT2 inhibitors '
               'in certain circumstances, such as before elective surgery or while managing adverse effects, and advises communicating a clear plan for '
               'when to restart them (practice points).[[ntr16_1]] The United States Food and Drug Administration (FDA) labeling for metformin also asks for it to be stopped before iodinated '
               'contrast in patients with an eGFR of 30 to 60 and restarted when kidney function is stable, and it is contraindicated below '
               '30.[[ntr16_10]] Sick-day rules rest on physiology and consensus rather than trials, and they carry their own risk: a protective drug '
               'stopped during an illness and never restarted. The restart plan matters as much as the stop.</p>\n'
               '{{flow:Sick-day plan the patient carries|When to use it::Vomiting, diarrhea, fever with sweating, or not eating or drinking normally for a '
               'day.|Hold these::Metformin, SGLT2 inhibitor, ACE inhibitor or ARB, diuretic, and any NSAID, unless your doctor wrote otherwise.|Keep '
               'these::Insulin with more frequent glucose checks, and other medicines as written; ask before stopping heart or transplant medicines.|Drink '
               'and check::Small, frequent drinks; glucose checks if diabetic; note urine output.|Seek help::Vomiting that does not stop, very little urine, '
               'drowsiness, fast breathing, or glucose very high or low.|Restart::Within 24 to 48 hours of eating and drinking normally, unless told otherwise.}}\n'
               '<p>A common memory aid in the United Kingdom lists the classes as sulfonylureas, ACE inhibitors, diuretics, metformin, ARBs, NSAIDs '
               'and SGLT2 inhibitors. Use whatever list your unit uses, translate it into the patient&rsquo;s language, and write it on a card with '
               'the patient&rsquo;s own brand names.</p>\n'
               '{{call:Stop and call the attending nephrologist (per unit protocol, but always ask the attending nephrologist for guidance) when you '
               'find:<ul><li>AKI with potassium of 6.0 mmol/L or higher, severe acidosis or very low urine output</li><li>Suspected metformin-associated '
               'lactic acidosis: high lactate with acidosis in a patient taking metformin and failing kidneys</li><li>A request to give an aminoglycoside '
               'or a second nephrotoxin to a patient with AKI</li><li>A toxic drug level, or a narrow-therapeutic-index drug in a patient whose kidney '
               'function is changing fast</li><li>A possible poisoning or overdose that dialysis might remove</li></ul>}}\n'
               '{{key:Every stop needs a restart date. Write when each held medicine comes back, and who will check.}}\n'
               '\n{{fig:ntr16_b}}\n')],
 'debrief': ['<p><strong>What contributed, and what to stop.</strong> Three days of vomiting made him volume depleted. Losartan and '
             'hydrochlorothiazide with mefenamic acid form the triple combination associated with AKI, worst in the first weeks; the unlabeled '
             '&ldquo;rayuma&rdquo; capsules may contain an NSAID or a steroid. Metformin, with a creatinine of 3.1 mg/dL and a lactate of 4.2 '
             'mmol/L, must be stopped and lactic acidosis considered. Hold losartan, hydrochlorothiazide, metformin, mefenamic acid and the '
             'capsules; keep the products for identification. Treat the volume depletion and the potassium per the attending.</p>\n',
             '<p><strong>Which estimate tonight.</strong> None is valid: creatinine is rising, so every equation overestimates his GFR, and the '
             'Cockcroft&ndash;Gault value near 15 mL/min is no better. If sepsis is likely, give full loading doses, because the loading dose '
             'depends on volume of distribution, not on the kidney; then set maintenance doses and intervals with the pharmacist, guided by urine '
             'output and drug levels. Ask whether amikacin is truly needed: KDIGO suggests avoiding aminoglycosides when a less nephrotoxic option '
             'exists (2A). For vancomycin, use AUC-guided monitoring as the unit protocol allows. Reassess daily as the kidney recovers.</p>\n',
             '<p><strong>The plan home.</strong> Before discharge, his baseline creatinine estimates (eGFR about 58, nonindexed about 50, '
             'Cockcroft&ndash;Gault about 37) decide which doses his labels allow. Give him and his daughter a sick-day card in Tagalog with his '
             'brand names: hold metformin, losartan, the diuretic and any pain reliever when vomiting or not eating, and restart within 24 to 48 hours '
             'of eating normally, or as the doctor writes. Write the restart date for losartan and metformin, list paracetamol as the safer pain '
             'reliever at the dose the attending sets, tell him not to take the neighbor&rsquo;s capsules, and arrange a creatinine and potassium '
             'check within a week.</p>\n'],
 'skills': {'title': 'Renal pharmacology and medication stewardship',
            'intro': 'Complete with a preceptor, on the ward or in clinic. Sign-off is local.',
            'items': [('Completes a medicine reconciliation that includes over-the-counter, herbal and supplement products by brand name', False),
                      ('Chooses between eGFR, nonindexed eGFR and creatinine clearance for a named drug and states why', False),
                      ('Explains why no equation is valid when creatinine is not at steady state and plans dosing by other means', False),
                      ('Identifies the NSAID, RASi and diuretic combination and stops or replaces the NSAID', False),
                      ('Plans antibiotic dosing for a patient on hemodialysis or CKRT with the pharmacist, including timing around sessions', False),
                      ('Writes a sick-day card with hold and restart instructions in the patient&rsquo;s language', False)],
            'placement': 'Ward, emergency room, dialysis unit or clinic'},
 'quiz': [('An intern reconciles medicines for a 70-year-old admitted with AKI. Which finding most needs to be flagged?',
           ['Daily paracetamol at the dose the attending set',
            'An ARB, a thiazide diuretic and an over-the-counter NSAID taken together',
            'A statin taken at night',
            'A multivitamin without minerals'],
           1,
           'The NSAID, RASi and diuretic triple combination was associated with AKI (rate ratio 1.31, 1.82 in the first 30 days). The other items '
           'carry far less kidney risk.'),
          ('A frail 82-year-old woman weighing 40 kg has a stable creatinine of 1.0 mg/dL. Her drug&rsquo;s label gives kidney bands in creatinine '
           'clearance. What is the best approach?',
           ['Use the indexed eGFR alone because the laboratory reports it',
            'Assume normal kidney function because creatinine is normal',
            'Use creatinine clearance (Cockcroft&ndash;Gault) or a nonindexed eGFR as the label and pharmacist advise, recognizing low muscle mass',
            'Wait for a measured GFR before giving any dose'],
           2,
           'The label was tested in creatinine clearance, and indexed eGFR overstates the actual GFR of a small patient. A normal creatinine in low '
           'muscle mass can hide reduced function.'),
          ('A fellow is asked to dose a dialyzable antibiotic for a patient on CKRT. Which statement is most accurate?',
           ['CKRT patients should receive the same dose as anuric patients off dialysis',
            'Continuous removal can be substantial, so underdosing is a real risk; dose to the effluent rate with the pharmacist',
            'CKRT never removes antibiotics',
            'Give the dose only after the CKRT circuit is stopped'],
           1,
           'Clearance on CKRT depends on the effluent rate and the drug; using old anuric doses risks treatment failure.'),
          ('A patient with sepsis and AKI has a creatinine rising from 1.1 to 2.6 mg/dL over 24 hours. The emergency team wants to halve the first '
           'antibiotic dose because of the creatinine. What is the best response?',
           ['Agree, because the eGFR is low',
            'Give the full loading dose, which depends on volume of distribution, then set maintenance doses by kidney function and levels',
            'Delay the antibiotic until creatinine stabilizes',
            'Give the dose orally instead'],
           1,
           'The loading dose fills the volume of distribution; kidney function affects maintenance. The rising creatinine also means the eGFR is '
           'not at steady state.'),
          ('A man with CKD G3b on metformin, an ARB and an SGLT2 inhibitor asks what to do if he gets gastroenteritis. Which advice best matches '
           'KDIGO 2024 practice points?',
           ['Double his ARB to protect the kidney',
            'Stop all medicines permanently',
            'Hold metformin, the ARB and the SGLT2 inhibitor during the illness, with a clear plan for when to restart',
            'Add an NSAID for cramps'],
           2,
           'KDIGO suggests planned temporary discontinuation of such drugs in certain circumstances and a clear restart plan. Stopping permanently '
           'removes protection; NSAIDs add injury.')],
 'terms': [('ACE', 'Angiotensin-converting enzyme'),
           ('AKI', 'Acute kidney injury'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('AUC', 'Area under the concentration-time curve'),
           ('CKD', 'Chronic kidney disease'),
           ('CKD-EPI', 'Chronic Kidney Disease Epidemiology Collaboration'),
           ('CKRT', 'Continuous kidney replacement therapy'),
           ('CT', 'Computed tomography'),
           ('CYP3A4', 'Cytochrome P450 3A4'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('eGFRcr-cys', 'eGFR from creatinine and cystatin C combined'),
           ('FDA', 'United States Food and Drug Administration'),
           ('GFR', 'Glomerular filtration rate'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('MRSA', 'Methicillin-resistant Staphylococcus aureus'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('PIRRT', 'Prolonged intermittent renal replacement therapy'),
           ('RASi', 'Renin-angiotensin system inhibitor'),
           ('SGLT2', 'Sodium-glucose cotransporter 2'),
           ('SLED', 'Sustained low-efficiency dialysis')],
 'readings': [('physician-on-duty-20-prescribing-without-kidneys.html', 'Physician on Duty, Module 20: Prescribing without kidneys'),
              ('nsaid-kidney-injury.html', 'NSAIDs and Kidney Injury'),
              ('herbal-nephropathy.html', 'Herbal Nephropathy'),
              ('medicines-and-your-kidneys.html', 'Medicines and Your Kidneys')],
 'calcs': ['calc-renal-med-safety.html', 'calc-renal-abx-dosing.html', 'calc-vancomycin-auc.html', 'calc-aminoglycoside-dosing.html',
           'calc-doac-renal-dosing.html', 'calc-drug-interaction-checker.html', 'calc-cockcroft-gault.html']}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
