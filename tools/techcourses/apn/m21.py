# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 21: Home PD: training the family, school, and non-infectious complications.
Written November 27, 2026 for the Renal Care Academy, in the voice of the Physician on Duty modules and to the medical teaching standard.
Numbers checked against the ISPD 2024 pediatric infection guideline (publisher full text), IPPN and SCOPE abstracts, the EPDWG EPS survey,
Fischbach & Warady 2009 and Zurowska 2013 (PMC full text), and PhilHealth PC 2024-0036 documents, PA 2025-0074 and PA 2026-0013.
Coverage facts are stated as coverage only; the unit's pediatric protocol sets every prescription."""

MODULE = {
 'image_alt': 'A Filipino mother and her school-age son sit beside a home peritoneal dialysis cycler in a clean corner of their house at night while a nurse on a video call checks the setup.',
 'objectives': [
    'Run caregiver training for home peritoneal dialysis (PD) as a curriculum with return demonstration, a home visit and retraining, and explain what the training evidence does and does not show.',
    'Diagnose and manage the non-infectious complications of pediatric PD: outflow failure, leaks, hernias, hydrothorax, ultrafiltration failure, encapsulating peritoneal sclerosis (EPS) and hypokalemia.',
    'Explain the PhilHealth pediatric PD Z package and the automated PD (APD) pilot to a family accurately, keeping coverage separate from the prescription.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the attending of a home therapy</span>Once a child goes home on peritoneal '
        'dialysis (PD), the dialysis unit is a bedroom and the dialysis nurse is a mother. You certify that the caregiver is trained, you review the home '
        'record every month, you sign the PhilHealth pediatric checklist as attending pediatric nephrologist, and you decide when a complication means '
        'a change of prescription, a surgeon, or a change of modality.[[apn21_16]]</div>\n'
        '{{plain:Home PD is like teaching a family to fly a small plane every night. The plane is simple and reliable, but only if the pre-flight checks '
        'are done every time, the instruments are read, and the pilot is rested.}}\n'
        '<p>The picture has a limit. A plane fails suddenly; PD usually fails slowly. Drains shrink over weeks, a hernia grows, the membrane changes over '
        'years, and a caregiver&rsquo;s strength runs down without anyone noticing. Most of these failures are visible in the home record before they '
        'reach the emergency room, if someone looks.</p>\n'
        '{{cards:Key numbers|International Pediatric Peritoneal Dialysis Network (IPPN) training survey::Median total training 24 hours; under 20 hours associated with higher peritonitis rates|Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (SCOPE) '
        'training cohort::1,450 trainings; only 23% met all four training components; no association with early peritonitis|PD catheter revisions, '
        'IPPN::60% mechanical malfunction, 6% leakage|EPS in European children::Prevalence 1.5%; 8.7 per 1,000 patient-years|PhilHealth pediatric PD '
        'eligibility::Age 0 to 18 years and 364 days|Pediatric APD pilot::Extended to July 31, 2026; status after that date unresolved}}\n'
        '<p>Most children on home PD do well when the family is trained, supported and rested. A few develop mechanical problems that look like dialysis '
        'failure, and a very few develop membrane failure or sclerosis after years. Your work is to build a training program that keeps families safe, to '
        'separate mechanical from membrane causes when drains fall, and to notice the exhausted caregiver before the exhaustion becomes an infection or '
        'a missed night.</p>\n',
 'case': {'title': 'Three weeks without sleep',
          'html': '<p>Joshua Manalo is 9 years old and weighs 24 kg. He has been on nightly automated PD (APD) for 14 months for kidney failure after '
                  'posterior urethral valves. He lives with his mother, Liezl, and two younger sisters in San Fernando, Pampanga; his father works in '
                  'Saudi Arabia. You see him at your clinic in a provincial hospital; his cycler and solutions come through a program in Metro Manila.</p>\n'
                  '<p>For three weeks the cycler has alarmed for low drain three or four times a night. Liezl gets up for each alarm and has not slept '
                  'more than three hours a night. Joshua&rsquo;s home weight is up 1.4 kg in ten days, his blood pressure today is 128/86 mm Hg, above '
                  'the 95th percentile for his age and height, his abdomen is distended, and there is a soft bulge at the umbilicus when he coughs. He '
                  'has not passed stool for four days. He has missed six school days this month.</p>\n'
                  '<p>Liezl asks whether he can switch to hemodialysis at the adult unit 15 minutes from their house so that she can sleep. She has also '
                  'heard that PhilHealth coverage for children on the machine may end.</p>\n',
          'questions': ['What is the most likely cause of the poor drains, and what will you do first?',
                        'What is the bulge at the umbilicus, and how does it change the prescription?',
                        'How will you answer Liezl about switching to hemodialysis and about coverage?']},
 'sections': [
  ('training', 'Training', 'Training the family and preparing the home',
   '<p>Every home PD program depends on one or two people at home who do the exchanges, set up the cycler, care for the exit site and recognize '
   'trouble. Training turns a frightened parent into that person. It is a curriculum, not a demonstration: written objectives, practice on a '
   'training model, return demonstration until the skill is safe, a written or oral test, a home visit, and retraining at set times and after every '
   'complication.</p>\n'
   '<p><strong>What the guideline suggests.</strong> The 2024 international pediatric guideline on PD-associated infections suggests that session '
   'length and total training duration be tailored to the child and caregivers, favoring longer total training where possible, and that a home '
   'visit be part of training (both 2D, weak suggestions on very low-quality evidence).[[apn21_1]]</p>\n'
   '<p><strong>What the studies show.</strong> In an International Pediatric Peritoneal Dialysis Network (IPPN) survey, 62 of 137 centers responded. '
   'A PD nurse trained families in 93.5% of centers; median total training was 24 hours; 58% of centers made home visits. Training shorter than 20 '
   'hours and fewer training tools were associated with higher peritonitis rates after adjustment for the proportion of infants and country '
   'income.[[apn21_2]] In the Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (SCOPE) collaborative, 1,450 trainings '
   'were analyzed for four components: a home visit, one-to-one training, starting training at least 10 days after catheter insertion, and sessions '
   'of 3 hours or less. Only 23% met all four, and neither single components nor all-or-none compliance was associated with peritonitis within 90 '
   'days of training.[[apn21_3]] The authors note that SCOPE&rsquo;s required monthly review of catheter care may have blunted any training effect. A '
   '2026 scoping review of 12 studies found pediatric training programs poorly aligned with International Society for Peritoneal Dialysis (ISPD) guidance, rarely defined by objectives and criteria, '
   'and silent on family outcomes.[[apn21_4]]</p>\n'
   '<p>The honest summary: longer, structured training is associated with fewer infections in one survey but not in a cohort with strong monthly '
   'follow-up, and no trial has tested it. Training still matters because it is the only way a family learns to do the procedure; the evidence gap is '
   'about which details matter most.</p>\n'
   '<p><strong>The Philippine home.</strong> The home visit is where training meets reality. Check what a training room cannot show.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Home check</th><th>Why it matters</th><th>What you arrange</th></tr></thead><tbody>'
   '<tr><td>Electricity, brownout pattern, outlet with grounding</td><td>APD stops when power fails mid-cycle</td><td>A written plan for brownouts: '
   'manual drain, switch to continuous ambulatory PD (CAPD) exchanges per protocol, who to call</td></tr>'
   '<tr><td>A clean, closable space with a table and good light</td><td>Touch contamination happens on cluttered surfaces near pets and '
   'visitors</td><td>A dedicated corner; pets out of the room during connection</td></tr>'
   '<tr><td>Clean water and soap for hand washing</td><td>Hand hygiene before every connection</td><td>Alcohol hand rub where water is '
   'unreliable</td></tr>'
   '<tr><td>Dry storage for a month of solution boxes</td><td>Flooding and heat damage supplies</td><td>Raised shelving; typhoon plan with a two-week '
   'reserve where possible</td></tr>'
   '<tr><td>Who else can do the exchanges</td><td>One caregiver cannot cover every night for years</td><td>Train a second adult: a grandmother, aunt or '
   'older sibling who is an adult</td></tr>'
   '<tr><td>Distance and transport to the PD center</td><td>Peritonitis needs treatment within hours</td><td>A named nearer hospital and a written '
   'plan for cloudy effluent (Module 22)</td></tr></tbody></table></div>\n'
   '<p><strong>School.</strong> Nightly APD is chosen partly so that a child can attend school by day. Write a letter for the school with what the '
   'teacher should know: the catheter is not contagious, the child can join most activities but should avoid contact that pulls on the catheter, '
   'swimming follows the unit&rsquo;s policy, and who to call for abdominal pain or fever. Ask about school days missed at every review; absence is '
   'an outcome.</p>\n'
   '{{cards:When to retrain|After every peritonitis or exit-site infection::Watch a full exchange and exit-site care; find the step that failed.|After '
   'a touch contamination::Review the connection technique the same week.|When the caregiver changes::A new grandmother, aunt or adult sibling is '
   'trained to the same standard, not by the tired parent alone.|When the equipment changes::A new cycler, a switch from CAPD to APD, or new '
   'solution bags.|After a long hospital stay::Skills fade; observe before discharge.|Each year::Even a perfect caregiver drifts.}}\n'
   '<div class="tc-scene"><span class="tc-lab">The first night at home &middot; fictional</span><p>A mother in Cavite, discharged that afternoon after '
   'two weeks of training, calls at 11 p.m.: the cycler shows an error code she does not recognize and her son is crying.</p><p>The PD nurse on call '
   'talks her through the screen, the code turns out to be a clamp left closed, and the cycle restarts. The next morning the program adds a page of '
   'common error codes, in Filipino and English, to every discharge packet.</p><p class="tc-scene-take"><b>What this shows.</b> The first nights at '
   'home are part of training. A phone line that answers is the last training tool.</p></div>\n'
   '{{key:Train to a standard, not to a schedule. Certify the caregiver only after a safe return demonstration, then visit the home and retrain after '
   'every complication.}}\n'
   '{{fig:apn21_a}}\n'),
  ('coverage', 'Coverage', 'PhilHealth: what the package covers and what it does not decide',
   '<p>PhilHealth Circular 2024-0036 created the Z benefits package for PD with separate adult and pediatric packages. For children it covers '
   'continuous ambulatory PD (CAPD) and, as a pilot at selected facilities, automated PD (APD).[[apn21_11]] The pediatric eligibility checklist '
   'requires an age of 0 to 18 years and 364 days, written informed consent from parents or guardian, stage 5 chronic kidney disease (CKD) '
   'requiring kidney replacement therapy (not temporary dialysis for acute kidney injury), a permanent PD catheter, PD initiation completed at an '
   'accredited facility, a patient or caregiver adequately trained to do PD at home, and no known allergy to PD solutions.[[apn21_12]] The guide to the '
   'circular adds registration in the PhilHealth Dialysis Database.[[apn21_11]]</p>\n'
   '<p><strong>What it covers.</strong> The package is organized in coverage tiers of solution bags per day (for children, tiers of 2-liter bags for CAPD '
   'and of 5-liter bags for APD), supplies such as transfer sets and APD cassettes, PD catheter insertion and initiation, exit-site and peritonitis '
   'prevention care, outpatient treatment of PD-related peritonitis, laboratory tests and medicines, and administration that includes monthly '
   'monitoring, follow-up visits and training.[[apn21_11]] The pediatric CAPD checklist names the attending pediatric nephrologist and is certified '
   'by the attending physician or pediatric nephrologist.[[apn21_16]]</p>\n'
   '<p><strong>The APD pilot.</strong> PhilHealth Advisory 2025-0074 set the pilot implementation of APD in children at three government tertiary '
   'centers in Metro Manila.[[apn21_13]] Advisory 2026-0013 extended the pilot to July 31, 2026, with pilot sites continuing under the existing '
   'guidelines.[[apn21_14]] No later issuance had been found when this module was written. The status after July 31, 2026 is unresolved: confirm it '
   'with your PhilHealth liaison and the program coordinator before you tell a family that APD is covered, not covered, or ending.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>The package decides</th><th>The package does not decide</th></tr></thead><tbody>'
   '<tr><td>Who is eligible and what documents are needed</td><td>Whether PD is the right modality for this child</td></tr>'
   '<tr><td>Which coverage tier is paid</td><td>The fill volume, number of exchanges or glucose strength</td></tr>'
   '<tr><td>Which facilities may provide APD during the pilot</td><td>Whether this child needs APD for school, sleep or fluid control</td></tr>'
   '<tr><td>What is reimbursed on the date of service</td><td>What you write in the chart: that must be the true prescription</td></tr>'
   '</tbody></table></div>\n'
   '<div class="tc-scene"><span class="tc-lab">At the program office &middot; fictional</span><p>The PD coordinator asks you to sign the monthly '
   'pediatric checklist for a 7-year-old. The form lists the highest CAPD tier, but your prescription for the past two months uses fewer exchanges '
   'because his residual urine has held up.</p><p>You correct the checklist to match the prescription in the chart and ask the coordinator to file '
   'it that way.</p><p class="tc-scene-take"><b>What this shows.</b> The signature certifies the true prescription. A form filled to the highest '
   'tier is a false claim, however well meant.</p></div>\n'
   '{{key:Coverage is not a prescription. Prescribe what the child needs, document it truthfully, and confirm the benefit on the date of service.}}\n'),
  ('mechanical', 'Mechanical', 'Outflow failure, leaks, hernias and hydrothorax',
   '<p>When drains fall, the question is whether the fluid cannot get out (mechanical), has gone somewhere else (leak), or was never pulled in by the '
   'membrane (ultrafiltration failure). Mechanical causes are far more common. In the IPPN registry, mechanical malfunction accounted for 60% of PD '
   'access revisions in children and leakage for 6%, and mechanical failure doubled the risk of technique failure compared with infectious causes '
   '(hazard ratio 1.95).[[apn21_6]]</p>\n'
   '<p><strong>Outflow failure.</strong> The catheter drains by gravity from the lowest part of the pelvis. A loaded rectum pushes the tip up and out '
   'of the pelvis and compresses the catheter. The omentum can wrap the side holes, and fibrin can block them, especially after peritonitis or '
   'bloody effluent. The classic sign is inflow that runs well with outflow that is slow or incomplete. Work from the simple to the surgical: '
   'constipation, then position, then fibrin, then the omentum.</p>\n'
   '<p><strong>Leaks and hernias.</strong> Raised intraperitoneal pressure (IPP) drives fluid into the abdominal wall, along the catheter tunnel, '
   'through a patent processus vaginalis into the scrotum or labia, or through the umbilicus. Large fills, coughing, constipation and sitting upright '
   'with a full abdomen all raise IPP; Fischbach and Warady list hernia and hydrothorax among the harms of an excessive fill.[[apn21_7]] A hernia in a '
   'child on PD needs surgical repair; until then, lower the IPP.</p>\n'
   '<p><strong>Hydrothorax.</strong> Dialysate can pass through a defect in the diaphragm into the pleural space, usually on the right. The child '
   'becomes breathless, drains fall, and a pleural effusion appears. Fluid from the chest has a high glucose compared with blood. Stop PD, support '
   'breathing, and decide with the surgeon and the family whether to repair the defect or change modality.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Most likely cause</th><th>First steps</th></tr></thead><tbody>'
   '<tr><td>Inflow good, outflow slow, no stool</td><td>Constipation</td><td>Laxative plan per protocol; recheck drains after stools</td></tr>'
   '<tr><td>Outflow poor after stool; tip high on abdominal X-ray</td><td>Catheter migration</td><td>Mobility, repeat X-ray; surgical or radiological '
   'repositioning</td></tr>'
   '<tr><td>Strands in effluent, slow both ways</td><td>Fibrin</td><td>Heparin in the dialysate or catheter as protocol directs</td></tr>'
   '<tr><td>Recurrent outflow failure despite the above</td><td>Omental wrap</td><td>Laparoscopic review, omentectomy</td></tr>'
   '<tr><td>Swelling of abdominal wall, scrotum, labia or umbilicus</td><td>Leak or hernia</td><td>Lower fills or rest PD; surgical repair</td></tr>'
   '<tr><td>Breathlessness, pleural effusion, falling drains</td><td>Hydrothorax</td><td>Stop PD; chest imaging; pleural fluid glucose; surgeon</td></tr>'
   '</tbody></table></div>\n'
   '<div class="tc-scene"><span class="tc-lab">In the clinic &middot; fictional</span><p>A 6-year-old girl from Nueva Ecija is referred for '
   '&ldquo;PD failure, for HD&rdquo; after two weeks of poor drains. Her abdominal X-ray shows a rectum full of stool and the catheter tip in the '
   'left upper quadrant.</p><p>After a bowel regimen the tip returns to the pelvis and her drains recover in three days. The HD referral is '
   'withdrawn.</p><p class="tc-scene-take"><b>What this shows.</b> Most outflow failure is mechanical, and constipation is the commonest reversible '
   'cause. Rule it out before anyone talks about changing modality.</p></div>\n'
   '{{key:When drains fall, ask three questions in order: is the fluid stuck, is it leaking, or was it never pulled in? Treat the bowel first.}}\n'
   '{{fig:apn21_b}}\n'),
  ('membrane', 'Membrane', 'Ultrafiltration failure, sclerosis and the slow complications',
   '<p><strong>The membrane changes from the start.</strong> In a multicenter biopsy study of children on PD with neutral-pH, low glucose degradation '
   'product solutions, peritoneal blood microvessel density was 110% and 93% higher after up to 6 and 12 months of PD than before dialysis, and the '
   'submesothelial layer was 23% and 58% thicker. Microvessel density correlated with faster small-solute transport.[[apn21_9]] More capillaries mean '
   'glucose is absorbed faster and the osmotic pull is lost sooner. This is an observational tissue study; it shows that even the more biocompatible '
   'solutions alter the membrane, not that any one solution changes clinical outcome.</p>\n'
   '<p><strong>Ultrafiltration failure.</strong> Before blaming the membrane, exclude a catheter problem, a leak to the abdominal wall or pleura, and '
   'excess salt and water intake. Fischbach and Warady list the membrane causes: a fill too small for the membrane, a large vascular surface from '
   'inflammation or glucose injury, impaired water transport through aquaporins, high lymphatic absorption at high IPP, and a reduced surface after '
   'adhesions or sclerosis.[[apn21_7]] A peritoneal equilibration test (PET) with a stronger glucose solution shows the early dip in dialysate sodium '
   'that reflects water moving through aquaporins; little or no dip points to impaired free-water transport.[[apn21_7]] The 2020 International Society '
   'for Peritoneal Dialysis (ISPD) volume recommendations, written as practice points because no randomized trial informs blood pressure targets in '
   'PD, ask that euvolemia be pursued while protecting residual urine output and that blood pressure be a key measure of prescription quality.[[apn21_15]]</p>\n'
   '<p><strong>Encapsulating peritoneal sclerosis (EPS).</strong> EPS is the rare, late threat: the peritoneum thickens into a cocoon around the bowel. '
   'A 10-year survey of 14 European pediatric units found 22 cases, a prevalence of 1.5% (8.7 per 1,000 patient-years on PD). Children with EPS had a '
   'median PD vintage of 5.9 years versus 1.7 years in the rest. Fifteen of 17 children diagnosed on PD (88%) developed ultrafiltration failure first, a '
   'median of 2.8 months before bowel obstruction; 20 of 22 had signs of bowel obstruction; 3 died during follow-up.[[apn21_8]] EPS can also appear '
   'after transfer to hemodialysis (HD) or after transplantation. The survey is descriptive and cannot tell you how to prevent EPS, but it tells you who '
   'to watch: the child with long PD vintage, many peritonitis episodes and new ultrafiltration failure.</p>\n'
   '<p><strong>Potassium and protein.</strong> Children on PD lose potassium in effluent and often eat little. In SCOPE, 437 of 1,186 children (37%) '
   'had sustained hypokalemia (3.5 mmol/L or lower in at least two of three consecutive months), and it was not associated with the peritonitis rate '
   '(rate ratio 1.07, 95% confidence interval 0.80 to 1.44).[[apn21_17]] That differs from adult data, where the ISPD 2022 guideline treats '
   'hypokalemia as a modifiable peritonitis risk factor.[[apn21_18]] Correct hypokalemia for the heart, muscle and bowel, through diet and the '
   'unit&rsquo;s protocol, whatever its link to infection. Protein is lost in effluent every day and more during peritonitis; the dietitian&rsquo;s '
   'protein target must account for it, and many infants need tube feeds to grow.[[apn21_10]]</p>\n'
   '<p><strong>Residual urine.</strong> Residual kidney function eases fluid and solute control and makes PD last longer. Protect it: avoid '
   'nephrotoxic drugs and contrast where there is an alternative, avoid volume depletion from overly aggressive ultrafiltration, and measure urine '
   'output at every review. The ISPD volume practice points ask that fluid removal by ultrafiltration and urine output be considered together and '
   'that residual function not be compromised.[[apn21_15]]</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Slow complication</th><th>Mechanism</th><th>What you see first</th></tr></thead><tbody>'
   '<tr><td>Fast transport over time</td><td>Neoangiogenesis from glucose and inflammation</td><td>Day dwell drains less than it took in; rising '
   'glucose strength needed</td></tr>'
   '<tr><td>Impaired free-water transport</td><td>Aquaporin dysfunction</td><td>No sodium dip on PET; poor response to stronger glucose</td></tr>'
   '<tr><td>EPS</td><td>Fibrosis encasing the bowel</td><td>Ultrafiltration failure, then vomiting, distension, bloody effluent, obstruction</td></tr>'
   '<tr><td>Hypokalemia</td><td>Effluent loss, low intake</td><td>Weakness, constipation, ileus</td></tr>'
   '<tr><td>Protein loss</td><td>Large pores, peritonitis</td><td>Falling albumin, poor growth</td></tr></tbody></table></div>\n'
   '{{key:New ultrafiltration failure in a child with years on PD and repeated peritonitis is EPS until proven otherwise. Plan the exit from PD before '
   'the bowel obstructs.}}\n'
   '{{fig:apn21_c}}\n'),
  ('practice', 'Practice', 'The monthly home review and the tired caregiver',
   '<p>The monthly review of a child on home PD covers four things: the child, the dialysis, the home and the caregiver. Do it face to face at the '
   'interval your unit sets, with the home log, the growth chart and the exit-site photograph in front of you.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Domain</th><th>What you review</th><th>Red flag</th></tr></thead><tbody>'
   '<tr><td>The child</td><td>Height, weight, blood pressure percentile, edema, appetite, stool pattern, school attendance, mood</td><td>Falling '
   'height standard deviation score (SDS), rising pressure, school days missed</td></tr>'
   '<tr><td>The dialysis</td><td>Fill and drain by exchange, net ultrafiltration, alarms, residual urine, glucose strengths used</td><td>Drains below '
   'fills, stronger glucose needed month after month</td></tr>'
   '<tr><td>The blood</td><td>Potassium, sodium, bicarbonate, calcium, phosphate, albumin, hemoglobin; adequacy and PET as indicated</td><td>Low '
   'potassium, falling albumin</td></tr>'
   '<tr><td>The exit site</td><td>Photograph and score; dressing technique</td><td>Any score above zero</td></tr>'
   '<tr><td>The home</td><td>Supplies, brownouts, flooding, pets, cleanliness of the corner</td><td>Running out of solution; storage wet</td></tr>'
   '<tr><td>The caregiver</td><td>Sleep, work, money, mood, who helps, connection technique on a short observed exchange</td><td>Exhaustion, skipped '
   'exchanges, touch contamination</td></tr></tbody></table></div>\n'
   '<p><strong>The caregiver is a clinical problem.</strong> In a study of 41 children on APD in Poland, 51.2% of primary caregivers scored in the '
   'range that suggests possible abnormal mental functioning on the General Health Questionnaire, and most reported a medium burden.[[apn21_5]] It '
   'was a cross-sectional survey in a different health system, but the pattern is familiar in Philippine homes, where one mother often carries the '
   'nights alone while the father works abroad. Ask directly: &ldquo;How many hours did you sleep last night?&rdquo; Then act: train a second adult, '
   'reduce alarms by fixing the mechanics, involve the social worker, and consider respite admissions or a planned period of in-center care if the '
   'family is breaking.</p>\n'
   '<p><strong>When to change modality.</strong> PD should change when it cannot keep the child well or safe: refractory ultrafiltration failure, '
   'EPS, a membrane lost to peritonitis, a hernia or leak that cannot be repaired, or a home that cannot sustain it despite support. Exhaustion alone '
   'is a reason to fix the burden first, then decide with the family. HD in an adult unit near home has its own costs for a child: vascular access, '
   'three sessions a week during school hours, and a unit not built for children (Modules 23 to 25).</p>\n'
   '<p><strong>Typhoon season.</strong> From June to November, review the disaster plan before the first storm: a two-week reserve of solution where '
   'the program allows, a dry raised shelf, the manual exchange the family will use if the cycler cannot run, a charged phone, and the name of the '
   'nearest hospital that can drain a peritoneum and take an effluent culture if roads to the PD center close. Families on islands or in '
   'flood-prone barangays need this plan in writing.</p>\n'
   '<p><strong>The growing child.</strong> As a child on PD reaches adolescence, teach self-care step by step: exit-site care first, then connection '
   'under supervision, then the whole procedure. A teenager who can do a safe exchange can sleep over at a relative&rsquo;s house, join a school '
   'trip with a plan, and carry that skill into transplant preparation and the adult unit.</p>\n'
   '{{flow:Home PD review: the order of questions|Is the child growing and normotensive?::Growth chart, blood pressure percentile, edema.|Is the '
   'dialysis delivering?::Drains, ultrafiltration, residual urine, alarms.|Is anything mechanical?::Stool, catheter position, leaks, hernias.|Is the '
   'membrane changing?::Rising glucose needs, PET when indicated, EPS risk with long vintage.|Is the home safe?::Power, water, storage, pets, '
   'supplies.|Is the caregiver coping?::Sleep, money, help at home, observed technique.}}\n'
   '<div class="tc-scene"><span class="tc-lab">At the monthly review &middot; fictional</span><p>Aling Merly has done her granddaughter&rsquo;s '
   'exchanges for two years. On a short observed exchange she touches the tip of the transfer set while opening the cap. She says she has been doing it '
   'this way &ldquo;for months, to save time.&rdquo;</p><p>You arrange retraining with the PD nurse that week and record a touch contamination in the '
   'program log.</p><p class="tc-scene-take"><b>What this shows.</b> Technique drifts over time. Observing one exchange at review finds errors that '
   'no questionnaire will.</p></div>\n'
   '{{key:Review the child, the dialysis, the home and the caregiver every month. A tired caregiver is a risk factor you can treat.}}\n'
   '{{call:<ul><li>Breathlessness or a new pleural effusion in a child on PD</li><li>Vomiting, abdominal distension and bloody or cloudy effluent in a '
   'child with long PD vintage (possible EPS or peritonitis)</li><li>A hernia that is tender, hard or cannot be reduced</li><li>No outflow after the '
   'bowel is emptied</li><li>A caregiver who says she cannot continue</li></ul>}}\n'),
 ],
 'debrief': [
    '<p><strong>The poor drains.</strong> Four days without stool, a distended abdomen and alarms for low drain point first to constipation, which '
    'pushes the catheter tip out of the pelvis and compresses it. Start the unit&rsquo;s bowel regimen today, ask Liezl to log drains for the next two '
    'nights, and order an abdominal X-ray if drains do not recover after stools. His rising weight and blood pressure follow from fluid that is not '
    'coming out; reassess his fluid allowance and blood pressure medicines once the bowel is cleared, and look for a leak.</p>\n',
    '<p><strong>The bulge.</strong> A soft umbilical bulge on coughing in a child on PD is a hernia, driven by intraperitoneal pressure and made worse by '
    'constipation and a full abdomen. Ask for a pediatric surgical review for repair. Until then, lower the pressure as your protocol allows: avoid '
    'large day dwells, keep exchanges lying down where possible, and treat the constipation. Teach Liezl the signs of incarceration: a hard, tender '
    'bulge, vomiting, or a bulge that will not go back.</p>\n',
    '<p><strong>Liezl.</strong> Thank her and take the exhaustion seriously; it is part of the clinical problem. Fixing the constipation should reduce '
    'the alarms. Offer to train a second adult and involve the social worker. Explain honestly that hemodialysis would mean a catheter or fistula, '
    'three daytime sessions a week in an adult unit, and more missed school, so you would rather make PD workable first; if it still is not, you will '
    'plan the change together. On coverage, tell her what is true: the APD benefit for children was a pilot extended to July 31, 2026, and you will '
    'confirm its current status with the PhilHealth liaison and the program coordinator before anything changes. His prescription will follow his needs, '
    'not the coverage.</p>\n'],
 'skills': {'title': 'Home PD: training the family, school, and non-infectious complications',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Certifies a caregiver after observed return demonstration using a written training checklist', False),
                      ('Completes a home visit checklist covering power, water, storage, pets and a second trained adult', False),
                      ('Works up outflow failure in order: bowel, position, fibrin, omentum, leak', False),
                      ('Explains the pediatric PD Z package and APD pilot status to a family without turning coverage into a prescription', False)],
            'placement': 'Home PD program, clinic or simulated family meeting'},
 'quiz': [
    ('What does the evidence on caregiver training for pediatric PD show?',
     ['A randomized trial proved 24 hours of training halves peritonitis',
      'Shorter training was associated with more peritonitis in an IPPN survey, but SCOPE found no association with four training components',
      'Home visits have been shown to increase infection',
      'Training duration does not need to be tailored'],
     1,
     'The evidence is observational and conflicting; the 2024 pediatric guideline makes weak (2D) suggestions to tailor training and to include a home visit.'),
    ('A child on APD has slow outflow, good inflow and no stool for four days. What is the first step?',
     ['Refer for catheter replacement',
      'Start a higher glucose solution',
      'Treat constipation and recheck drains',
      'Switch to hemodialysis'],
     2,
     'Constipation is the commonest reversible cause of outflow failure; it displaces and compresses the catheter.'),
    ('Which pattern should raise concern for encapsulating peritoneal sclerosis?',
     ['New ultrafiltration failure in a child with years on PD and repeated peritonitis',
      'A single exit-site infection in the first month',
      'Clear fluid at the exit site on day two',
      'A hernia found at catheter insertion'],
     0,
     'In the European pediatric survey, EPS children had longer PD vintage and most developed ultrafiltration failure a median 2.8 months before obstruction.'),
    ('A child on PD becomes breathless with a right pleural effusion and falling drains. What is the most likely diagnosis?',
     ['Peritonitis',
      'Ultrafiltration failure from aquaporin dysfunction',
      'Pneumonia unrelated to PD',
      'Hydrothorax from dialysate passing through the diaphragm'],
     3,
     'Stop PD, image the chest, compare pleural fluid glucose with blood and involve the surgeon.'),
    ('A family asks whether PhilHealth pediatric APD coverage continues after July 31, 2026. What is the correct answer?',
     ['It has ended',
      'It continues unchanged',
      'Its status after that date is unresolved; confirm with the PhilHealth liaison',
      'APD was never covered for children'],
     2,
     'Advisory 2026-0013 extended the pilot to July 31, 2026. Never say it ended or continues without a later issuance.'),
 ],
 'terms': [('APD', 'Automated peritoneal dialysis'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('CKD', 'Chronic kidney disease'),
           ('EPS', 'Encapsulating peritoneal sclerosis'),
           ('HD', 'Hemodialysis'),
           ('IPP', 'Intraperitoneal pressure'),
           ('IPPN', 'International Pediatric Peritoneal Dialysis Network'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('PD', 'Peritoneal dialysis'),
           ('PET', 'Peritoneal equilibration test'),
           ('SCOPE', 'Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (collaborative)'),
           ('SDS', 'Standard deviation score')],
 'readings': [('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide'),
              ('living-with-dialysis.html', 'Staying Well on Dialysis — What Every HD Patient Must Know'),
              ('typhoon-disaster-preparedness-dialysis.html', 'Typhoon & Disaster Preparedness for Dialysis Patients')],
 'calcs': ['calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-pediatric-growth-percentiles.html', 'calc-pediatric-bp.html'],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
