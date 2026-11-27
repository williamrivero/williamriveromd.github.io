# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 13: Diabetes, obesity and kidney protection.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Trial numbers
(CREDENCE, DAPA-CKD, EMPA-KIDNEY, FIDELIO-DKD, FIGARO-DKD, FLOW, CONFIDENCE) from PubMed abstracts; numbers needed to treat and
events per 1000 from the published full texts where the papers report them; where a paper reports no NNT, only the event
percentages and their difference are given and labeled as such. KDIGO 2022 and 2024 grades checked against KDIGO summaries;
FDA metformin labeling against the 2016 communication; PhilHealth GAMOT list against PC 2025-0013. No doses. Fictional case."""

MODULE = {'image_alt': 'A Filipino nephrology fellow and a public school teacher look together at four medicine boxes arranged on a clinic desk while the teacher counts pesos in her wallet.',
 'objectives': ['<strong>Intern:</strong> Name the four pillars of kidney protection in type 2 diabetes with chronic kidney disease (CKD): a renin-angiotensin system inhibitor (RASi), a sodium-glucose cotransporter 2 (SGLT2) inhibitor, a nonsteroidal mineralocorticoid receptor antagonist (nsMRA) and a glucagon-like peptide-1 receptor agonist (GLP-1 RA), and the mechanism behind each.',
                '<strong>Resident:</strong> Start and monitor the pillars safely: eligibility by estimated glomerular filtration rate (eGFR) and potassium, the expected early eGFR dip, sick-day rules, ketoacidosis and hyperkalemia warnings, and metformin limits by eGFR.',
                '<strong>Fellow:</strong> Sequence therapies using the absolute benefits and numbers needed to treat that the trials report, together with what the patient can afford in the Philippines, and say plainly what is surrogate and what is a hard outcome.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the patient with diabetes and albuminuria</span>As an <strong>intern</strong>, '
        'you check that every patient with diabetes has an eGFR and a urine albumin-to-creatinine ratio (ACR) on record, and you list which pillars '
        'the patient is on and which are missing. As a <strong>resident</strong>, you start and monitor them with your attending: you know the '
        'eligibility thresholds, the potassium and creatinine checks, and the symptoms that mean stop. As a <strong>fellow</strong>, you decide '
        'the order when the family can afford only one more medicine, and you can explain the choice in absolute numbers, not slogans.</div>\n'
        '{{plain:Think of each glomerulus in a person with diabetes as a rice cooker left on high. The extra heat cooks the rice faster at first '
        '(the GFR rises), but the pot scorches (the filter scars). Each pillar turns the heat down by a different knob.}}\n'
        '<p>The picture has a limit. A rice cooker has one heating element; the diabetic kidney has several injury pathways running at once. '
        'Glomerular hypertension is one. Mineralocorticoid receptor overactivation, which drives inflammation and fibrosis directly, is another. '
        'Obesity, insulin resistance and systemic inflammation are a third. A RASi and an SGLT2 inhibitor (SGLT2i) mainly lower glomerular pressure from '
        'opposite ends of the glomerulus; an nsMRA mainly targets inflammation and fibrosis; a GLP-1 RA lowers glucose, weight and blood pressure '
        'and has anti-inflammatory effects whose share of its kidney benefit is still uncertain. Because the pathways differ, the benefits add.</p>\n'
        '{{cards:Key numbers|CREDENCE (canagliflozin)::43.2 vs 61.2 events per 1000 patient-years; number needed to treat (NNT) 22 over 2.5 years|DAPA-CKD '
        '(dapagliflozin)::9.2% vs 14.5% over a median 2.4 years; NNT 19|EMPA-KIDNEY (empagliflozin)::13.1% vs 16.9% over a median 2.0 years; 42 fewer '
        'events per 1000 over 2 years|FIDELIO-DKD (finerenone)::17.8% vs 21.1%; NNT 29 at 3 years for the kidney outcome|FLOW (semaglutide)::18.7% vs '
        '23.2%; NNT 20 over 3 years|SGLT2 inhibitor in type 2 diabetes and CKD (KDIGO 2024)::Recommended at eGFR 20 mL/min/1.73 m&sup2; or more (1A)}}\n'
        '<p>Most patients with diabetes and CKD in a Philippine clinic are on one pillar, often a RASi at a low dose, and sometimes none. A few are '
        'on all four. Your work is to know which pillar each patient is missing and why, to start the next one safely, and, when money decides, '
        'to choose the one that buys the most protection for that patient.</p>\n',
 'case': {'title': 'The teacher who can afford one more medicine',
          'html': '<p>Monday, 9 a.m., the nephrology clinic of a tertiary hospital in Batangas City. Mrs. Teresita Valdez, 58, teaches Grade 5 '
                  'in a public elementary school. She has had type 2 diabetes for 14 years and hypertension for 9. She takes metformin and '
                  'losartan, both bought as generics. Her body mass index (BMI) is 29 kg/m&sup2;; she gained weight during the pandemic years '
                  'and has not lost it.</p>\n'
                  '<p>Today her eGFR is 48 mL/min/1.73 m&sup2;, her ACR 620 mg/g on two samples, potassium 4.6 mmol/L, glycated hemoglobin '
                  '(HbA1c) 7.6%, and standardized blood pressure 134/82 mm Hg. Her losartan is at the highest dose she tolerates. Her retina '
                  'shows background diabetic retinopathy; her urine sediment is bland.</p>\n'
                  '<p>She has read online about &ldquo;the new diabetes injection&rdquo; and about &ldquo;the kidney pill.&rdquo; She says: '
                  '&ldquo;Doc, my salary and my husband&rsquo;s pension cover one more medicine, not three. Which one?&rdquo; You are the '
                  'first-year fellow; your attending asks you to present a recommendation with numbers.</p>\n',
          'questions': ['Which pillars is she on, which are missing, and why does each matter for her kidneys?',
                        'Which one medicine would you recommend first, and how would you start and monitor it?',
                        'How will you explain the benefit in absolute numbers and the cost in the Philippine setting?']},
 'sections': [('mechanism',
               'Mechanism',
               'Why diabetic kidneys hyperfilter, and where each pillar acts',
               '<p>Start with the proximal tubule. Glucose filtered at the glomerulus is reabsorbed with sodium by SGLT2. In chronic hyperglycemia the '
               'tubule reabsorbs more glucose and therefore more sodium. Less sodium and chloride reach the macula densa further downstream. The '
               'macula densa reads this as &ldquo;the filtration rate is low,&rdquo; and tubuloglomerular feedback dilates the afferent arteriole to '
               'raise it. At the same time, angiotensin II constricts the efferent arteriole. Inflow opens, outflow tightens, and glomerular pressure '
               'rises. This is hyperfiltration: a high single-nephron GFR bought with a high glomerular pressure that injures podocytes, leaks albumin '
               'and scars the glomerulus.</p>\n'
               '{{flow:From hyperglycemia to scarring|More glucose filtered::SGLT2 reabsorbs more glucose and sodium in the proximal tubule.|Less sodium '
               'downstream::The macula densa senses low delivery.|Feedback misfires::The afferent arteriole dilates; angiotensin II keeps the efferent '
               'arteriole tight.|Pressure rises::Glomerular hypertension and hyperfiltration.|Damage::Podocyte injury, albuminuria, tubular inflammation, '
               'fibrosis and falling GFR.}}\n'
               '<p>Each pillar acts on a different link. An SGLT2 inhibitor blocks proximal sodium-glucose reabsorption, restores sodium delivery to the '
               'macula densa, and lets the afferent arteriole constrict again. A RASi, meaning an angiotensin-converting enzyme (ACE) inhibitor or an angiotensin receptor blocker (ARB), relaxes the efferent arteriole. Both lower glomerular pressure, '
               'which is why both cause a small early eGFR dip that is a sign of the drug working, not of injury. An nsMRA blocks mineralocorticoid '
               'receptors on kidney, vascular and immune cells, reducing inflammation and fibrosis, with a modest effect on blood pressure. A GLP-1 RA '
               'lowers glucose, weight and blood pressure and may reduce inflammation; how much each contributes to its kidney benefit is not yet '
               'established.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Pillar</th><th>Main target</th><th>What you see after starting</th><th>Main safety '
               'watch</th></tr></thead><tbody>'
               '<tr><td>RASi (ACE inhibitor or ARB)</td><td>Efferent arteriole; albuminuria</td><td>Small eGFR dip, lower ACR</td><td>Potassium, '
               'creatinine rise over 30%</td></tr>'
               '<tr><td>SGLT2 inhibitor</td><td>Proximal tubule; tubuloglomerular feedback</td><td>Small eGFR dip, mild glycosuria, slight weight '
               'loss</td><td>Volume depletion, genital infection, ketoacidosis</td></tr>'
               '<tr><td>Nonsteroidal MRA (finerenone)</td><td>Mineralocorticoid receptor; inflammation, fibrosis</td><td>Lower ACR, small potassium '
               'rise</td><td>Hyperkalemia</td></tr>'
               '<tr><td>GLP-1 RA</td><td>Glucose, weight, blood pressure, inflammation</td><td>Lower HbA1c and weight</td><td>Nausea, vomiting, '
               'volume depletion</td></tr>'
               '</tbody></table></div>\n'
               '{{key:The early eGFR dip after an SGLT2 inhibitor or a RASi is the pressure coming down. Recheck it; do not stop the drug for it '
               'unless the rise in creatinine is large or the patient is volume depleted.}}\n'
               '\n{{fig:ntr13_a}}\n'),
              ('pillars',
               'The four pillars',
               'The trials in absolute numbers',
               '<p>Relative risk reductions sound alike: 30%, 39%, 28%, 18%, 24%. Absolute numbers tell you what a patient gains. Each trial below '
               'enrolled patients already on a RASi where it was indicated; the benefits are added to RASi, not instead of it. Where a paper reports '
               'a number needed to treat (NNT), it is given; where it does not, the event percentages and their difference are given, and labeled '
               'as a subtraction rather than an NNT the authors reported.</p>\n'
               '<p><strong>CREDENCE (canagliflozin).</strong> 4,401 adults with type 2 diabetes, an eGFR of 30 to below 90 and an ACR above 300 to '
               '5,000 mg/g. The trial stopped early at a median 2.62 years. The primary outcome (kidney failure, doubling of creatinine, or renal or '
               'cardiovascular death) occurred at 43.2 versus 61.2 events per 1000 patient-years (hazard ratio [HR] 0.70). Kidney failure itself was '
               'lower (HR 0.68), as were heart failure hospitalizations (HR 0.61).[[ntr13_3]] The authors reported an NNT of 22 over 2.5 years, and '
               'estimated 47 fewer primary outcome events per 1000 patients treated for 2.5 years.[[ntr13_3]]</p>\n'
               '<p><strong>DAPA-CKD (dapagliflozin).</strong> 4,304 adults, with or without diabetes, eGFR 25 to 75, ACR 200 to 5,000 mg/g. Over a '
               'median 2.4 years the primary outcome (50% eGFR decline, kidney failure, or renal or cardiovascular death) occurred in 9.2% versus '
               '14.5% (HR 0.61), NNT 19. Death from any cause was 4.7% versus 6.8%. Effects were similar with and without diabetes.[[ntr13_4]]</p>\n'
               '<p><strong>EMPA-KIDNEY (empagliflozin).</strong> 6,609 adults with an eGFR of 20 to below 45, or 45 to below 90 with an ACR of 200 '
               'mg/g or more. Over a median 2.0 years, kidney disease progression or cardiovascular death occurred in 13.1% versus 16.9% (HR 0.72), '
               'consistent with and without diabetes and across eGFR ranges.[[ntr13_5]] The authors expressed this as 42 fewer primary outcomes per '
               '1000 patients treated for 2 years.[[ntr13_5]] Ketoacidosis occurred in 6 versus 1 patients.[[ntr13_5]]</p>\n'
               '<p><strong>FIDELIO-DKD (finerenone).</strong> 5,734 adults with type 2 diabetes and CKD on a maximally tolerated RASi. Over a median '
               '2.6 years, the kidney outcome (kidney failure, sustained 40% eGFR decline or renal death) occurred in 17.8% versus 21.1% (HR 0.82), and '
               'the cardiovascular outcome in 13.0% versus 14.8% (HR 0.86).[[ntr13_6]] The authors reported NNTs of 29 for the kidney outcome and 42 '
               'for the cardiovascular outcome at 3 years. Hyperkalemia led to stopping the drug in 2.3% versus 0.9%.[[ntr13_6]]</p>\n'
               '<p><strong>FIGARO-DKD (finerenone).</strong> 7,437 adults with type 2 diabetes and earlier CKD (eGFR 25 to 90 with ACR 30 to 300 mg/g, '
               'or eGFR 60 or more with ACR 300 to 5,000 mg/g). Over a median 3.4 years the cardiovascular outcome occurred in 12.4% versus 14.2% (HR '
               '0.87), driven mainly by fewer heart failure hospitalizations (HR 0.71). The kidney composite, 9.5% versus 10.8% (HR 0.87, 95% '
               'confidence interval 0.76 to 1.01), was not statistically significant. Hyperkalemia stopped the drug in 1.2% versus 0.4%.[[ntr13_7]] The '
               'difference in the reported cardiovascular percentages is 1.8 points; the abstract reports no NNT.</p>\n'
               '<p><strong>FLOW (semaglutide).</strong> 3,533 adults with type 2 diabetes and CKD (eGFR 50 to 75 with ACR above 300, or eGFR 25 to below '
               '50 with ACR above 100 mg/g). The trial stopped early at a median 3.4 years. Major kidney disease events occurred in 331 versus 410 '
               'patients, 18.7% versus 23.2%, or 5.8 versus 7.5 per 100 patient-years (HR 0.76); cardiovascular death (HR 0.71), major cardiovascular '
               'events (HR 0.82) and death from any cause (HR 0.80) were also lower.[[ntr13_8]] Over 3 years, the authors estimated that 20 people '
               'would need treatment to prevent one primary outcome event, 45 to prevent one major cardiovascular event and 39 to prevent one '
               'death.[[ntr13_8]] The eGFR slope was 1.16 mL/min/1.73 m&sup2; per year less steep, a surrogate that agrees with the hard outcomes.[[ntr13_8]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Trial</th><th>Population</th><th>Primary outcome, drug vs placebo</th><th>Absolute '
               'benefit as reported</th></tr></thead><tbody>'
               '<tr><td>CREDENCE</td><td>Type 2 diabetes (T2D), eGFR 30&ndash;&lt;90, ACR &gt;300</td><td>43.2 vs 61.2 per 1000 patient-years</td><td>NNT 22 over 2.5 years</td></tr>'
               '<tr><td>DAPA-CKD</td><td>With or without diabetes, eGFR 25&ndash;75, ACR 200&ndash;5,000</td><td>9.2% vs 14.5%</td><td>NNT 19 over a median 2.4 years</td></tr>'
               '<tr><td>EMPA-KIDNEY</td><td>With or without diabetes, eGFR 20&ndash;&lt;90 (ACR &ge;200 if eGFR &ge;45)</td><td>13.1% vs 16.9%</td>'
               '<td>42 fewer per 1000 over 2 years</td></tr>'
               '<tr><td>FIDELIO-DKD</td><td>T2D, moderate to severe albuminuria, on RASi</td><td>17.8% vs 21.1% (kidney)</td><td>NNT 29 at 3 years</td></tr>'
               '<tr><td>FIGARO-DKD</td><td>T2D, earlier CKD, on RASi</td><td>12.4% vs 14.2% (cardiovascular)</td><td>Difference 1.8 points; no NNT in abstract</td></tr>'
               '<tr><td>FLOW</td><td>T2D, eGFR 25&ndash;75 with albuminuria</td><td>18.7% vs 23.2%</td><td>NNT 20 over 3 years</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>What the trials do not tell you.</strong> NNTs from different trials are not directly comparable: the populations, outcomes '
               'and follow-up differ, and higher-risk populations produce smaller NNTs. Few participants in FIDELIO-DKD or FIGARO-DKD were on '
               'an SGLT2 inhibitor at baseline, so the size of benefit when the pillars are stacked is estimated rather than measured. The CONFIDENCE '
               'trial started finerenone and empagliflozin together and found that the combination lowered ACR 29% more than finerenone alone and 32% '
               'more than empagliflozin alone at 180 days, without unexpected adverse events.[[ntr13_9]] Albuminuria is a surrogate; CONFIDENCE did '
               'not test kidney failure.</p>\n'
               '<p><strong>The guideline position.</strong> KDIGO 2024 recommends an SGLT2 inhibitor for adults with type 2 diabetes, CKD and an eGFR '
               'of 20 mL/min/1.73 m&sup2; or more (1A); for adults with CKD and an eGFR of 20 or more with an ACR of 200 mg/g or more, or with heart '
               'failure (1A); and suggests one for adults with an eGFR of 20 to 45 and an ACR below 200 mg/g (2B). It suggests an nsMRA with proven '
               'kidney or cardiovascular benefit for adults with type 2 diabetes, an eGFR above 25, normal potassium and albuminuria of 30 mg/g or more '
               'despite a maximum tolerated RASi (2A). It recommends a long-acting GLP-1 RA for adults with type 2 diabetes and CKD who have not '
               'reached their glycemic target on metformin and an SGLT2 inhibitor, or cannot use them (1B).[[ntr13_2]] KDIGO has taken a medications '
               'management focused update of the CKD guideline through public review; check its status before teaching these statements as final.[[ntr13_14]]</p>\n'
               '{{key:Quote the absolute benefit and the follow-up time with every relative risk: &ldquo;19 patients treated for about 2.4 years to '
               'prevent one major kidney or cardiovascular event&rdquo; is something a patient can weigh.}}\n'
               '\n{{fig:ntr13_b}}\n'),
              ('glycemia',
               'Glucose',
               'Glucose control in CKD: what HbA1c can and cannot tell you',
               '<p>Glucose control protects the small vessels, but in CKD both the measurement and the drugs change. HbA1c reflects the average '
               'glucose over the life of the red cell. In advanced CKD, anemia, a shortened red cell life span, iron or erythropoiesis-stimulating '
               'agent treatment and transfusion all distort it, usually downward. KDIGO 2022 recommends HbA1c to monitor glycemic control, with an '
               'individualized target ranging from below 6.5% to below 8.0% in patients with diabetes and CKD not on dialysis (1C).[[ntr13_1]] The '
               'lower end suits a younger patient with few complications and a low hypoglycemia risk; the upper end suits an older patient with '
               'advanced CKD, cardiovascular disease, limited life expectancy or a history of hypoglycemia. Where HbA1c seems discordant with '
               'finger-stick readings, trust a pattern of glucose readings over a single number.</p>\n'
               '<p><strong>Metformin by eGFR.</strong> KDIGO 2022 recommends metformin for patients with type 2 diabetes, CKD and an eGFR of 30 or '
               'more (1B).[[ntr13_1]] The United States Food and Drug Administration (FDA) labeling, revised in 2016, states that metformin is '
               'contraindicated below an eGFR of 30, that starting it at 30 to 45 is not recommended, that the benefit and risk should be reassessed '
               'if eGFR falls below 45 in a patient already taking it, and that it should be stopped before iodinated contrast in patients with an '
               'eGFR of 30 to 60 and restarted once kidney function is confirmed stable.[[ntr13_12]] Dose reductions by eGFR come from the label and '
               'the attending.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>eGFR (mL/min/1.73 m&sup2;)</th><th>Metformin (FDA labeling)</th><th>SGLT2 inhibitor '
               '(KDIGO 2024)</th></tr></thead><tbody>'
               '<tr><td>45 or more</td><td>Can be used; check eGFR at least yearly</td><td>Recommended in T2D with CKD (1A)</td></tr>'
               '<tr><td>30 to 44</td><td>Do not start; reassess if already taking</td><td>Recommended in T2D with CKD (1A)</td></tr>'
               '<tr><td>20 to 29</td><td>Contraindicated</td><td>Recommended in T2D with CKD (1A); can be continued below 20 if tolerated, per '
               'KDIGO practice point</td></tr>'
               '<tr><td>Below 20</td><td>Contraindicated</td><td>Not started; continued if already taking and tolerated, until kidney replacement therapy (KRT)</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Hypoglycemia.</strong> As GFR falls, insulin and sulfonylureas are cleared more slowly and the kidney contributes less '
               'gluconeogenesis, so hypoglycemia becomes more likely. A teacher who skips lunch because of classroom duty, or a farmer who works '
               'through noon, is at real risk on a long-acting sulfonylurea. The glucose-lowering effect of an SGLT2 inhibitor wanes at low eGFR, but '
               'its kidney and heart benefits do not, which is why KDIGO lets it continue.</p>\n'
               '<div class="tc-keyp"><span class="tc-lab">In children</span>Type 2 diabetes now occurs in adolescents with obesity, and albuminuria '
               'can appear within a few years of diagnosis. The kidney outcome trials in this module enrolled adults only; kidney '
               'protection in children rests on blood pressure control, RASi where albuminuria is present, weight and glucose care, and pediatric '
               'labeling for each drug. See <a href="attending-pediatric-nephrologist-17-pediatric-ckd.html">Attending Pediatric Nephrologist, Module '
               '17</a>.</div>\n'
               '{{key:Set the HbA1c target for the person, between below 6.5% and below 8.0%, and check the metformin dose against the eGFR every '
               'time the eGFR changes.}}\n'),
              ('obesity',
               'Obesity',
               'Obesity and the kidney: lower thresholds for Filipinos',
               '<p>Obesity injures the kidney through more than diabetes and hypertension. Excess body mass raises GFR demand, so each nephron '
               'hyperfilters; visceral fat drives insulin resistance, sympathetic activity and sodium retention; and adipose tissue releases '
               'inflammatory signals. The biopsy picture of obesity-related glomerulopathy, enlarged glomeruli with secondary focal segmental '
               'sclerosis, follows this chain. In a patient with diabetes, obesity adds to every pathway the pillars target.</p>\n'
               '<p><strong>Which BMI.</strong> A World Health Organization (WHO) expert consultation found that the proportion of Asian people at high '
               'risk of type 2 diabetes and cardiovascular disease is substantial at BMIs below the international overweight cut point of 25 '
               'kg/m&sup2;. It kept the international classification but proposed additional public health action points at 23, 27.5, 32.5 and 37.5 '
               'kg/m&sup2;.[[ntr13_10]] In practice, many Filipino clinicians treat a BMI of 23 as the start of increased risk and 27.5 as high risk; '
               'waist circumference adds information when BMI understates visceral fat.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Approach</th><th>What it changes</th><th>Evidence level and caution</th></tr></thead><tbody>'
               '<tr><td>Diet and activity</td><td>Weight, blood pressure, glucose</td><td>Foundation for everyone; adapt to CKD potassium and phosphate '
               'needs with the dietitian</td></tr>'
               '<tr><td>GLP-1 RA</td><td>Weight, glucose, blood pressure; kidney and heart outcomes in FLOW</td><td>FLOW enrolled people with type 2 '
               'diabetes; out-of-pocket cost is high</td></tr>'
               '<tr><td>SGLT2 inhibitor</td><td>Modest weight loss; kidney and heart protection</td><td>Benefit does not depend on weight loss</td></tr>'
               '<tr><td>Bariatric surgery</td><td>Large weight loss</td><td>Specialist referral; evidence for kidney outcomes is mainly observational</td></tr>'
               '</tbody></table></div>\n'
               '<p>Weight talk needs care. Many patients have heard &ldquo;magpapayat ka&rdquo; (you need to slim down) at every visit and have stopped '
               'listening. Ask what the family cooks, when the patient eats, and what one change is possible this month: rice portion, sweetened '
               'drinks, merienda. Avoid crash diets and imported slimming products, some of which have caused kidney injury (Module 16).</p>\n'
               '{{key:In Filipino patients, start counting cardiometabolic risk at a BMI of 23 kg/m&sup2;, and treat obesity as a kidney risk factor '
               'in its own right.}}\n'),
              ('access-cost',
               'Access and cost',
               'Access and cost: sequencing when the family pays',
               '<p>In the Philippines, kidney protection is often paid out of pocket, month by month. A regimen that is perfect on paper and bought '
               'twice a year protects nothing. Your sequencing must combine the evidence, the patient&rsquo;s risk and what the family can sustain.</p>\n'
               '<p><strong>What PhilHealth covers.</strong> The PhilHealth Guaranteed and Accessible Medications for Outpatient Treatment (GAMOT) benefit, '
               'part of the YAKAP primary care program, lists dapagliflozin, metformin, losartan, atorvastatin and rosuvastatin among its molecules, '
               'with an annual medicine limit of PHP 20,000 per member; finerenone and semaglutide are not on the list.[[ntr13_11]] Medicines are free '
               'only when prescribed at the member&rsquo;s registered YAKAP clinic and dispensed at an accredited pharmacy at PhilHealth&rsquo;s set '
               'price; a branded product priced above it is not covered unless the pharmacy offers it at that price.[[ntr13_13]] The list can change, '
               'so confirm it on the date you prescribe. Help the patient register.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Step</th><th>Why in this order</th><th>Philippine access</th></tr></thead><tbody>'
               '<tr><td>1. RASi at the highest tolerated dose</td><td>Foundation; benefit in albuminuric CKD; inexpensive</td><td>Generic losartan on '
               'the GAMOT list</td></tr>'
               '<tr><td>2. SGLT2 inhibitor</td><td>Kidney, heart failure and survival benefit across diabetes status; NNT 19 to 22 over about 2.5 '
               'years in the trials; 1A</td><td>Dapagliflozin on the GAMOT list</td></tr>'
               '<tr><td>3. nsMRA if ACR stays 30 mg/g or more and potassium is normal</td><td>Adds kidney and heart failure benefit; 2A</td><td>Out of '
               'pocket</td></tr>'
               '<tr><td>4. GLP-1 RA if glucose or weight targets are not met, or for added cardiovascular benefit</td><td>FLOW: NNT 20 over 3 years; 1B '
               'for glycemic indication</td><td>Out of pocket; injection and cold storage</td></tr>'
               '<tr><td>Throughout</td><td>Statin, blood pressure, glucose targets</td><td>Statins and metformin on the GAMOT list</td></tr>'
               '</tbody></table></div>\n'
               '<p>This order is a common reading of the evidence, not a rule. A patient with heart failure gains more from an SGLT2 inhibitor; a patient '
               'with severe obesity and poor glucose control may gain more from a GLP-1 RA if it is affordable; a patient whose ACR stays high on a RASi '
               'and an SGLT2 inhibitor is the FIDELIO-DKD patient. When cost limits the list, say so in the chart, so the next doctor does not assume '
               'the missing pillar was forgotten.</p>\n'
               '<p><strong>Safety at the start.</strong> Before an SGLT2 inhibitor: check volume status and the diuretic dose, teach genital hygiene, '
               'and teach the sick-day rule: hold it during vomiting, diarrhea, poor intake or acute illness, and before major surgery, and restart '
               'when eating and drinking normally (KDIGO practice point).[[ntr13_2]] Ketoacidosis on an SGLT2 inhibitor can occur with near-normal '
               'glucose. Before finerenone: check potassium and plan the recheck. Before a GLP-1 RA: warn about nausea and vomiting, which can cause '
               'volume depletion and acute kidney injury (AKI) in a patient with CKD. A 2026 KDIGO diabetes guideline is in public-review draft; until it is final, the 2022 '
               'guideline stands.</p>\n'
               '{{call:Stop and call the attending nephrologist (per unit protocol, but always ask the attending nephrologist for guidance) when you '
               'find:<ul><li>Nausea, vomiting, abdominal pain, fast breathing or drowsiness in a patient on an SGLT2 inhibitor, even with normal '
               'glucose</li><li>Potassium of 6.0 mmol/L or higher on a RASi or finerenone</li><li>Creatinine rising more than 30% after starting a pillar, '
               'or with vomiting and poor intake</li><li>Severe perineal pain, swelling or fever on an SGLT2 inhibitor</li><li>Recurrent hypoglycemia '
               'as eGFR falls</li></ul>}}\n'
               '{{key:When the family can buy only one more medicine, pick the pillar with the best evidence for this patient&rsquo;s risk that the '
               'family can sustain every month, and write down why the others are missing.}}\n')],
 'debrief': ['<p><strong>Pillars on and missing.</strong> She is on one pillar, losartan at the highest tolerated dose, plus metformin for glucose. '
             'She is missing an SGLT2 inhibitor, an nsMRA and a GLP-1 RA. With an eGFR of 48 and an ACR of 620 mg/g she has glomerular '
             'hypertension that losartan has only partly lowered; her residual albuminuria is the target. An SGLT2 inhibitor would lower glomerular '
             'pressure from the afferent side; finerenone would act on inflammation and fibrosis; a GLP-1 RA would help her weight and glucose. '
             'Metformin can continue at her eGFR with a dose checked against the label.</p>\n',
             '<p><strong>The one medicine.</strong> An SGLT2 inhibitor. She fits CREDENCE, DAPA-CKD and EMPA-KIDNEY, KDIGO 2024 recommends it at '
             'her eGFR (1A), and dapagliflozin is on the PhilHealth GAMOT list. Start it with the attending: review volume and any diuretic, teach '
             'genital hygiene and the sick-day rule, and recheck creatinine and potassium in a few weeks, expecting a small eGFR dip. If her ACR stays '
             'above 30 mg/g with normal potassium and she can later afford it, finerenone is the next step; a GLP-1 RA if glucose or weight targets '
             'are not met.</p>\n',
             '<p><strong>Explaining it.</strong> &ldquo;In the DAPA-CKD trial, about 15 in 100 people like you on placebo had a serious kidney or '
             'heart event over about two and a half years; on the medicine it was about 9 in 100. About one person in 19 who takes it avoids such an '
             'event over that time.&rdquo; Explain that the eGFR may dip a little at first and that this is expected. On cost: help her register '
             'with a YAKAP clinic and a GAMOT pharmacy, confirm that the list still includes dapagliflozin, and record that finerenone and a GLP-1 RA '
             'were deferred for cost, not forgotten.</p>\n'],
 'skills': {'title': 'Diabetes, obesity and kidney protection',
            'intro': 'Complete with a preceptor, in clinic or on the ward. Sign-off is local.',
            'items': [('Lists the four pillars with the mechanism and main safety watch for each', False),
                      ('Checks SGLT2 inhibitor and nsMRA eligibility by eGFR, ACR and potassium against KDIGO 2024', False),
                      ('Teaches sick-day rules and ketoacidosis warning signs to a patient starting an SGLT2 inhibitor', False),
                      ('Checks metformin against the eGFR thresholds in the FDA labeling', False),
                      ('Explains a trial result to a patient in absolute numbers with the follow-up time', False),
                      ('Writes a sequencing plan that records which pillars were deferred for cost', False)],
            'placement': 'Diabetes clinic, CKD clinic or ward'},
 'quiz': [('Which set correctly lists the four pillars of kidney protection in type 2 diabetes with albuminuric CKD?',
           ['RASi, SGLT2 inhibitor, nonsteroidal MRA, GLP-1 RA',
            'RASi, sulfonylurea, statin, loop diuretic',
            'ACE inhibitor plus ARB, SGLT2 inhibitor, insulin, aspirin',
            'Metformin, insulin, dipeptidyl peptidase-4 (DPP-4) inhibitor, thiazide'],
           0,
           'Each of the four has kidney outcome evidence or KDIGO-graded support. Dual ACE inhibitor plus ARB is to be avoided, and the other drugs '
           'lack kidney outcome trials of this kind.'),
          ('Three weeks after starting an SGLT2 inhibitor, a patient&rsquo;s eGFR falls from 48 to 44 mL/min/1.73 m&sup2;. She is well, eating '
           'normally and euvolemic. What is the best action?',
           ['Stop the SGLT2 inhibitor permanently',
            'Continue it and recheck; a small early dip reflects lower glomerular pressure',
            'Add finerenone immediately to counter the dip',
            'Start metformin dose escalation'],
           1,
           'The early dip is expected hemodynamics after restoring tubuloglomerular feedback. Stopping it would throw away a 1A-recommended '
           'benefit; a large fall, or a fall with volume depletion, needs review.'),
          ('A fellow must explain DAPA-CKD in absolute terms. Which statement matches the trial report?',
           ['The drug cut events by 39%, so 39 in 100 patients benefit',
            'Primary outcome 9.2% vs 14.5% over a median 2.4 years; NNT 19',
            'Primary outcome 13.1% vs 16.9%; NNT 26',
            'Benefit was seen only in patients with diabetes'],
           1,
           'DAPA-CKD reported 9.2% vs 14.5% (HR 0.61) with an NNT of 19, similar with and without diabetes. A relative reduction is not the share of '
           'patients who benefit; 13.1% vs 16.9% are EMPA-KIDNEY figures.'),
          ('A 66-year-old man with type 2 diabetes has an eGFR of 34 mL/min/1.73 m&sup2;. He is not yet on metformin. According to the FDA '
           'labeling, what applies?',
           ['Start metformin at the usual dose',
            'Starting metformin at an eGFR of 30 to 45 is not recommended',
            'Metformin is contraindicated at any eGFR below 60',
            'Metformin is preferred over an SGLT2 inhibitor at this eGFR'],
           1,
           'The 2016 labeling: contraindicated below 30, do not start at 30 to 45, reassess if already taking and eGFR falls below 45. An SGLT2 '
           'inhibitor is recommended at this eGFR (KDIGO 2024, 1A).'),
          ('A patient on a maximally tolerated ARB and an SGLT2 inhibitor still has an ACR of 410 mg/g, eGFR 52 and potassium 4.4 mmol/L. He can '
           'now afford one more medicine. Which addition has the most direct guideline support?',
           ['A second ARB',
            'A nonsteroidal MRA with proven kidney or cardiovascular benefit (KDIGO 2024, 2A)',
            'A loop diuretic for albuminuria',
            'Stopping the SGLT2 inhibitor to make room for insulin'],
           1,
           'Persistent albuminuria of 30 mg/g or more with normal potassium on a maximal RASi is the KDIGO 2A indication for an nsMRA, the diabetic kidney disease (DKD) population of the FIDELIO-DKD '
           'trial. Dual RASi is to be avoided.')],
 'terms': [('ACE', 'Angiotensin-converting enzyme'),
           ('ACR', 'Albumin-to-creatinine ratio'),
           ('AKI', 'Acute kidney injury'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('BMI', 'Body mass index'),
           ('CKD', 'Chronic kidney disease'),
           ('CONFIDENCE', 'Trial of finerenone and empagliflozin started together in CKD with type 2 diabetes'),
           ('CREDENCE', 'Canagliflozin and Renal Events in Diabetes with Established Nephropathy Clinical Evaluation (trial)'),
           ('DAPA-CKD', 'Dapagliflozin and Prevention of Adverse Outcomes in Chronic Kidney Disease (trial)'),
           ('DPP-4', 'Dipeptidyl peptidase-4'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('EMPA-KIDNEY', 'Study of Heart and Kidney Protection with Empagliflozin (trial)'),
           ('FDA', 'United States Food and Drug Administration'),
           ('FIDELIO-DKD', 'Finerenone in Reducing Kidney Failure and Disease Progression in Diabetic Kidney Disease (trial)'),
           ('FIGARO-DKD', 'Finerenone in Reducing Cardiovascular Mortality and Morbidity in Diabetic Kidney Disease (trial)'),
           ('FLOW', 'Evaluate Renal Function with Semaglutide Once Weekly (trial)'),
           ('GAMOT', 'Guaranteed and Accessible Medications for Outpatient Treatment (PhilHealth)'),
           ('GFR', 'Glomerular filtration rate'),
           ('GLP-1 RA', 'Glucagon-like peptide-1 receptor agonist'),
           ('HbA1c', 'Glycated hemoglobin'),
           ('HR', 'Hazard ratio'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KRT', 'Kidney replacement therapy'),
           ('MRA', 'Mineralocorticoid receptor antagonist'),
           ('NNT', 'Number needed to treat'),
           ('nsMRA', 'Nonsteroidal mineralocorticoid receptor antagonist'),
           ('RASi', 'Renin-angiotensin system inhibitor'),
           ('SGLT2', 'Sodium-glucose cotransporter 2'),
           ('T2D', 'Type 2 diabetes'),
           ('WHO', 'World Health Organization'),
           ('YAKAP', 'Yaman ng Kalusugan Program (PhilHealth primary care program)')],
 'readings': [('diabetes-kidneys.html', 'Diabetes and Your Kidneys'),
              ('glp1-ozempic-ckd.html', 'GLP-1 Medicines (Ozempic) and CKD'),
              ('obesity-ckd.html', 'Obesity and CKD'),
              ('ckd-financial-stress.html', 'CKD and Financial Stress')],
 'calcs': ['calc-sglt2i-eligibility.html', 'calc-metformin-ckd-safety.html', 'calc-eag-hba1c.html', 'calc-dkd-risk.html', 'calc-bmi-bsa-ibw.html',
           'calc-insulin-dose.html']}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
