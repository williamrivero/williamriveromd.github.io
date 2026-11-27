# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 02: The growing kidney and the pediatric renal assessment.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. CKiD U25 and
bedside Schwartz constants checked against the PubMed abstracts; AAP 2017 categories, measurement and prevalence against the
guideline text; IPNA 2022 definitions against the published table; KDIGO 2024 pediatric points against KDIGO's pediatric
takeaways. Fictional case."""

MODULE = {'image_alt': 'A pediatric nephrologist measures a teenage boy&rsquo;s height against a wall stadiometer in a clinic while his mother watches.',
 'objectives': ['Interpret a child&rsquo;s creatinine against height, age, sex and muscle mass, and choose a validated pediatric estimating equation.',
                'Measure and classify blood pressure in a child correctly, and quantify proteinuria with the definitions children&rsquo;s guidelines use.',
                'Combine growth, blood pressure, urine and estimated glomerular filtration rate into a single problem statement.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; reading the child, not the number</span>Most children reach you '
        'because someone saw one abnormal value: a creatinine flagged on a school physical, a dipstick after a fever, a blood pressure taken '
        'with the wrong cuff. Your duty is to decide whether the kidney is actually abnormal, and to say so in a way the family, the school '
        'and the referring doctor can act on.</div>\n'
        '{{plain:A creatinine value without the child is like a shoe size without the wearer. Size 6 is enormous for a toddler, ordinary for '
        'a 12-year-old and small for an adult.}}\n'
        '<p>The picture has a limit. Shoe size depends on one thing; creatinine depends on several. Its production follows muscle mass, which '
        'tracks height but also sex, puberty, training, diet and supplements. Its clearance follows the glomerular filtration rate (GFR), '
        'which in a child is still maturing in the first year and later rises with body size. And it lags: after an injury, creatinine '
        'catches up with the GFR only over a day or more. So a number on a report is a clue, not a verdict.</p>\n'
        '{{cards:Key numbers|Bedside Schwartz (2009)::eGFR = 0.413 &times; height (cm) / serum creatinine (mg/dL)|CKiD U25, '
        'creatinine::K 41.8 for males and 37.6 for females (sex-dependent form)|Low eGFR flag (KDIGO 2024)::eGFRcr below 90 mL/min per 1.73 '
        'm&sup2; in children and adolescents over age 2|Nephrotic-range proteinuria (IPNA 2022)::UPCR &ge;200 mg/mmol (2 mg/mg) in a spot '
        'urine|Clinical hypertension in children (AAP 2017)::About 3.5%}}\n'
        '<p>Most children with an &ldquo;abnormal&rdquo; kidney test have normal kidneys measured badly or interpreted against adult rules. '
        'A few have real, silent disease that the first number hinted at. Your work is to repeat the right test the right way, read it '
        'against the child&rsquo;s age and size, and write a problem statement that separates the two.</p>\n',
 'case': {'title': 'The varsity player with a &ldquo;high&rdquo; creatinine',
          'html': '<p>Monday, 9 a.m., your clinic in Lipa City, Batangas. Miguel Santos is 12 years old, 158 cm and 52 kg, and plays guard '
                  'for his school&rsquo;s varsity basketball team. The school physician has barred him from the provincial meet because his '
                  'pre-participation creatinine was 1.1 mg/dL, flagged high against the laboratory&rsquo;s pediatric range. The same screen '
                  'showed a urine dipstick of 1+ protein and a blood pressure of 134/86 mm Hg, taken with an adult cuff at the end of '
                  'practice.</p>\n'
                  '<p>His mother, Mrs. Teresa Santos, has brought a bag of his supplements, including a creatine powder the coach recommended, '
                  'and asks whether he needs an ultrasound and &ldquo;kidney vitamins.&rdquo; The coach has texted her twice: the team list '
                  'closes Friday. Miguel says he feels fine and wants to play.</p>\n',
          'questions': ['Does Miguel have reduced kidney function?',
                        'What will you repeat, and how will you measure it this time?',
                        'What will you tell Miguel, his mother and the school physician?']},
 'sections': [('development',
               'The growing kidney',
               'The growing kidney',
               '<p>A child&rsquo;s kidney is a moving target. Nephrons form through late gestation, and in most preterm infants nephrogenesis is '
               'still under way at birth. An autopsy study of preterm neonates found that renal maturation accelerated after preterm birth, '
               'with a larger share of abnormal glomeruli and enlarged renal corpuscles than in gestational controls, which suggests fewer '
               'functional nephrons and a kidney already working hard.[[apn02_7]] The study was small and descriptive; it shows structure, not '
               'outcome. The clinical message is the one the site&rsquo;s Born Small guide carries: prematurity is a lifelong kidney risk worth '
               'recording.</p>\n'
               '<p>Filtration matures quickly after birth. GFR rises through fetal life, matures rapidly after birth according to gestational '
               'and postmenstrual age, and reaches adult values, normalized to body surface area, by about 1 year of postnatal age, as one '
               'review summarizes.[[apn02_6]] In the first days of life the infant&rsquo;s creatinine also reflects the mother&rsquo;s, so a '
               'single early value says little about the baby&rsquo;s own kidneys. Module 14 covers the newborn in detail.</p>\n'
               '<p>After infancy, GFR normalized to surface area is roughly stable, but absolute GFR and muscle mass both grow. That is why a '
               'normal creatinine for a 3-year-old is a worrying creatinine for a 1-year-old, and why a fit adolescent boy can have a creatinine '
               'that would alarm you in his younger sister.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Stage</th><th>What the kidney is doing</th><th>What you see</th></tr></thead><tbody>'
               '<tr><td>Preterm newborn</td><td>Nephrogenesis may still be under way; maturation accelerates after birth</td><td>Creatinine '
               'shaped by the mother&rsquo;s in the first days; fragile handling of salt and water</td></tr>'
               '<tr><td>First year</td><td>GFR rising toward adult values per body surface area</td><td>Creatinine falling from birth values; '
               'small changes matter</td></tr>'
               '<tr><td>Childhood</td><td>Normalized GFR stable; body and muscle growing</td><td>Creatinine rising slowly with height</td></tr>'
               '<tr><td>Puberty</td><td>Rapid growth in body and muscle; a reduced kidney mass may not keep up</td><td>Creatinine rising, '
               'sometimes sharply in boys; a high-risk period for children with CKD</td></tr>'
               '</tbody></table></div>\n'
               '<p>Puberty deserves its own line. The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 chronic kidney disease (CKD) '
               'guideline advises monitoring children more often than their CKD stage alone would suggest during puberty, because a kidney with '
               'reduced capacity may not grow enough to match the body.[[apn02_3]]</p>\n'
               '{{key:Ask three questions of every pediatric creatinine: how old, how tall, and how much muscle. The answer may change the number&rsquo;s '
               'meaning more than the number itself.}}\n'),
              ('egfr',
               'Creatinine and eGFR',
               'From creatinine to estimated GFR',
               '<p>Because creatinine production scales with muscle, and muscle scales roughly with height, pediatric equations divide height by '
               'creatinine and multiply by a constant, K.</p>\n'
               '<p><strong>Bedside Schwartz.</strong> In 2009 the Chronic Kidney Disease in Children (CKiD) investigators refit the old Schwartz '
               'formula to creatinine measured by modern enzymatic methods. Their data came from 349 children aged 1 to 16 with CKD, median '
               'measured GFR 41.3 mL/min per 1.73 m&sup2;. With height in centimeters, 0.413 &times; height / creatinine gave a good '
               'approximation of their full equation.[[apn02_2]] The authors noted that children with higher GFR were needed to validate it for '
               'screening. In a healthy, muscular adolescent, the bedside formula was never designed to be precise.</p>\n'
               '<p><strong>CKiD U25.</strong> In 2021 the same group developed equations for ages 1 to 25 from 2,655 observations in 928 '
               'participants, with GFR measured by iohexol disappearance. The creatinine equations use K &times; height / creatinine with a '
               'sex-specific K of 41.8 for males and 37.6 for females, or an age- and sex-dependent K that rises through childhood (from 35.7 '
               'at age 1 to 50.8 at 18 and older in males; from 33.1 to 41.4 in females). Cystatin C equations use K &times; 1 / cystatin C, '
               'with constant K of 81.9 for males and 74.9 for females. The age-dependent creatinine form reduced bias, notably in young '
               'children and young adults.[[apn02_1]] These are estimates in children with CKD; they are less tested at normal GFR.</p>\n'
               '<p><strong>What KDIGO 2024 adds.</strong> Estimate GFR in children with equations developed or validated in comparable '
               'populations. Measure GFR when a more accurate value would change a treatment decision. Use a cystatin C-based equation in '
               'children with low muscle mass, such as neuromuscular conditions, because creatinine-based equations may give falsely high '
               'values. An eGFRcr below 90 mL/min per 1.73 m&sup2; can be flagged as low in children and adolescents over age 2.[[apn02_3]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Situation</th><th>How creatinine misleads</th><th>What to do</th></tr></thead><tbody>'
               '<tr><td>Muscular adolescent athlete, creatine supplements, high protein intake</td><td>More creatinine produced: eGFR falsely '
               'low</td><td>Repeat after rest and stopping supplements; add cystatin C</td></tr>'
               '<tr><td>Cerebral palsy, muscular dystrophy, spina bifida, malnutrition</td><td>Little muscle: eGFR falsely high</td><td>Use '
               'cystatin C; measure GFR if a decision depends on it</td></tr>'
               '<tr><td>First days of life</td><td>Mother&rsquo;s creatinine still present</td><td>Follow the trend, not one value (Module 14)</td></tr>'
               '<tr><td>Acute illness</td><td>Creatinine lags the GFR change</td><td>Do not use steady-state equations to stage acute injury</td></tr>'
               '<tr><td>Different laboratory methods</td><td>Older non-enzymatic assays read higher</td><td>Ask how the laboratory measures '
               'creatinine; compare like with like</td></tr>'
               '</tbody></table></div>\n'
               '{{key:An eGFR is an estimate built on assumptions about muscle. When the child breaks the assumptions, change the marker or measure '
               'the GFR.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the pediatric ward &middot; fictional</span><p>Bea, 10, has spastic cerebral '
               'palsy and weighs 19 kg. Her creatinine is 0.3 mg/dL, and the resident writes &ldquo;excellent kidney function&rdquo; before '
               'starting a nephrotoxic antibiotic.</p><p>You ask for a cystatin C. Her cystatin C-based estimate is about half of what the '
               'creatinine suggested, and the pharmacist adjusts the drug interval.</p><p class="tc-scene-take"><b>What this shows.</b> A low '
               'creatinine in a child with little muscle is not reassurance.</p></div>\n'
               '\n{{fig:apn02_a}}\n'),
              ('bp-urine',
               'Pressure and urine',
               'Blood pressure and urine, measured properly',
               '<p><strong>Blood pressure.</strong> The American Academy of Pediatrics (AAP) 2017 guideline classifies children aged 1 to under 13 '
               'by percentiles for age, sex and height, and adolescents 13 and older by fixed cut points that match adult categories: normal '
               'below 120/80, elevated 120&ndash;129/&lt;80, stage 1 hypertension 130/80 to 139/89, and stage 2 at 140/90 mm Hg or above. For '
               'younger children, elevated starts at the 90th percentile (or 120/80, whichever is lower), stage 1 at the 95th percentile (or '
               '130/80), and stage 2 at the 95th percentile plus 12 mm Hg (or 140/90).[[apn02_4]] The guideline puts the prevalence of clinical '
               'hypertension in children at about 3.5%.[[apn02_4]] Module 5 covers diagnosis and treatment.</p>\n'
               '<p>Measurement errors are common and usually raise the reading. The guideline asks for the right arm, standard technique, and a '
               'cuff whose bladder length is 80% to 100% of the arm circumference and whose width is at least 40%. Oscillometric screening '
               'readings that are high should be confirmed by auscultation.[[apn02_4]] An adult cuff on a thin arm, a reading straight after '
               'exercise, or a child talking during measurement can each turn normal into &ldquo;hypertension.&rdquo;</p>\n'
               '<p><strong>Protein.</strong> Children make proteinuria for benign reasons (fever, exercise, standing) and for serious ones. '
               'Quantify it with a spot urine protein-to-creatinine ratio (UPCR), ideally on a first-morning sample, which excludes '
               'orthostatic protein. The International Pediatric Nephrology Association (IPNA) defines nephrotic-range proteinuria as a UPCR of '
               '200 mg/mmol (2 mg/mg) or more in a spot urine, or 1,000 mg/m&sup2; per day or more in a 24-hour collection, corresponding to '
               '3+ or 4+ on the dipstick.[[apn02_5]] KDIGO 2024 suggests referring children for specialist care with a sustained albumin-to-'
               'creatinine ratio (ACR) of 30 mg/g (3 mg/mmol) or more, or a protein-to-creatinine ratio of 200 mg/g (20 mg/mmol) or more, '
               'using an early-morning sample taken when the child is well.[[apn02_3]]</p>\n'
               '<p><strong>Blood and sediment.</strong> The dipstick detects heme, not red cells. Look at the sediment yourself when you can. '
               'Dysmorphic red cells and red cell casts point to the glomerulus; uniform red cells with clots point to the urinary tract; heme '
               'without red cells suggests hemoglobin or myoglobin. Module 11 builds on this.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Benign explanation to exclude</th><th>Test that settles it</th></tr></thead><tbody>'
               '<tr><td>High blood pressure on one reading</td><td>Wrong cuff, exercise, anxiety, talking</td><td>Repeat with correct cuff, '
               'seated and rested, by auscultation; then ambulatory monitoring if needed</td></tr>'
               '<tr><td>Dipstick 1+ protein</td><td>Exercise, fever, standing, concentrated urine</td><td>First-morning UPCR, repeated when '
               'well</td></tr>'
               '<tr><td>Dipstick blood</td><td>Menstruation, exercise, trauma</td><td>Microscopy of a fresh sample; repeat when well</td></tr>'
               '<tr><td>Creatinine above the pediatric range</td><td>Muscle, supplements, laboratory method</td><td>Repeat after rest; '
               'cystatin C; compare with height-based estimate</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Measure once properly before you measure many times badly. The right cuff and a first-morning urine settle most referrals.}}\n'),
              ('practice',
               'The problem statement',
               'Putting it together: the problem statement',
               '<p>A child&rsquo;s growth chart is a vital sign. Plot height, weight and, where relevant, head circumference at every visit, and '
               'look at the velocity, not only the percentile. A child whose height crosses percentile lines downward may have CKD, acidosis or '
               'a tubular disorder long before creatinine says so. A child whose weight rises while height stalls may be retaining fluid or '
               'eating badly.</p>\n'
               '<p>Then write a problem statement in one or two sentences that a resident or a school physician can act on. It should name the '
               'child&rsquo;s age and size, the estimated GFR and the equation used, the blood pressure category, the urine findings with their '
               'quantity, the growth trend, and whether the picture is acute, chronic or not yet known.</p>\n'
               '{{flow:Five steps from referral to problem statement|Who is the child::Age, sex, height, weight, puberty stage, prematurity, '
               'muscle mass, medicines and supplements.|Is the number real::Repeat under the right conditions: rested, well, correct cuff, '
               'first-morning urine, same laboratory.|Estimate properly::A validated pediatric equation; cystatin C when muscle is atypical; '
               'measured GFR when a decision depends on it.|Look for company::Blood pressure, urine sediment and protein, growth velocity, '
               'ultrasound if structure is in question.|Write it::One sentence naming eGFR and equation, blood pressure category, urine findings '
               'and growth trend, and the plan.}}\n'
               '<div class="table-wrap"><table><thead><tr><th>Problem statement element</th><th>Example</th></tr></thead><tbody>'
               '<tr><td>Child</td><td>12-year-old boy, 158 cm, early puberty, athlete, on creatine powder</td></tr>'
               '<tr><td>Kidney function</td><td>Creatinine-based estimate low on one sample; cystatin C estimate normal</td></tr>'
               '<tr><td>Blood pressure</td><td>Normal for age, sex and height on correct cuff after rest</td></tr>'
               '<tr><td>Urine</td><td>First-morning UPCR normal; no blood on microscopy</td></tr>'
               '<tr><td>Growth</td><td>Tracking the 60th percentile for height</td></tr>'
               '<tr><td>Conclusion</td><td>No evidence of kidney disease; repeat in 6&ndash;12 months</td></tr>'
               '</tbody></table></div>\n'
               '{{call:<ul><li>eGFR below the low flag on repeat with a valid equation, or falling over time</li><li>Nephrotic-range proteinuria, '
               'edema or low albumin</li><li>Stage 2 hypertension confirmed by auscultation, or any blood pressure with headache, vomiting or '
               'visual change</li><li>Red cell casts or visible hematuria with edema or hypertension</li><li>Height velocity falling across '
               'percentile lines with any abnormal kidney test</li></ul>}}\n'
               '{{key:A good problem statement is short, quantified and honest about what is not yet known.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By Viber, a referring pediatrician &middot; fictional</span><p>A pediatrician in '
               'Naga sends a photo of a report: creatinine 0.6 mg/dL in a 2-year-old, &ldquo;normal range,&rdquo; with a growth chart showing '
               'height falling from the 50th to below the 3rd percentile over a year.</p><p>You calculate a height-based estimate and ask for a '
               'blood gas, electrolytes, urinalysis and a kidney ultrasound before the child is seen.</p><p class="tc-scene-take"><b>What this '
               'shows.</b> &ldquo;Normal range&rdquo; on an adult-style report may be abnormal for a toddler. Read the child, then the '
               'number.</p></div>\n'
               '\n{{fig:apn02_b}}\n')],
 'debrief': ['<p><strong>Does he have reduced function?</strong> Probably not, but one sample cannot tell you. A bedside Schwartz estimate '
             '(0.413 &times; 158 / 1.1) is about 59 mL/min per 1.73 m&sup2;, but Miguel is a muscular adolescent taking creatine, and the '
             'sample followed training. Each of these raises creatinine without any change in GFR, and the bedside formula was built in '
             'children with CKD, not in athletes. Treat the result as unconfirmed.</p>\n',
             '<p><strong>What to repeat.</strong> Ask him to stop the creatine and avoid heavy training for a few days, then repeat creatinine '
             'with a cystatin C at the same laboratory and calculate CKiD U25 estimates from both. Collect a first-morning urine for UPCR and '
             'microscopy. Measure blood pressure on his right arm with a correctly sized cuff after five minutes of rest, by auscultation. If '
             'all are normal, no ultrasound is needed now. If the cystatin C estimate is also low or protein persists, proceed to a full '
             'evaluation.</p>\n',
             '<p><strong>What to say.</strong> Tell Miguel and his mother what each test showed and why the first creatinine probably '
             'overstated the problem. Explain that &ldquo;kidney vitamins&rdquo; are not needed and that supplements can confuse tests. Write '
             'to the school physician with the repeat results and a clear statement: no evidence of kidney disease on repeat testing, cleared to '
             'play, with a repeat check in 6 to 12 months. If the results are not back by Friday, say so honestly rather than clearing him on '
             'hope.</p>\n'],
 'skills': {'title': 'The growing kidney and the pediatric renal assessment',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Calculates bedside Schwartz and CKiD U25 estimates and explains when each misleads', False),
                      ('Measures blood pressure in a child with a correctly sized cuff and classifies it by AAP 2017 categories', False),
                      ('Orders and interprets a first-morning UPCR and examines a urine sediment', False),
                      ('Writes a quantified problem statement that includes growth velocity', False)],
            'placement': 'Outpatient clinic or simulation'},
 'quiz': [('A 12-year-old athlete taking creatine has a creatinine above the pediatric range. What is the best next step?',
           ['Kidney biopsy',
            'Repeat after rest and stopping supplements, with a cystatin C',
            'Start a kidney-protective diet',
            'Restrict protein to the minimum'],
           1,
           'Muscle mass, supplements and recent exercise raise creatinine without changing GFR. A cystatin C estimate is less dependent on '
           'muscle.'),
          ('In which child is a creatinine-based eGFR most likely to be falsely high?',
           ['A muscular adolescent football player',
            'A child after a high-protein meal',
            'A 10-year-old with spastic cerebral palsy and low muscle mass',
            'A child taking creatine supplements'],
           2,
           'Low muscle mass means little creatinine is produced, so the estimate overstates GFR. KDIGO 2024 suggests a cystatin C-based '
           'equation in such children.'),
          ('By AAP 2017, how is a blood pressure of 132/84 mm Hg classified in a 14-year-old?',
           ['Normal',
            'Elevated',
            'Stage 2 hypertension',
            'Stage 1 hypertension'],
           3,
           'From age 13, AAP 2017 uses adult-style cut points: 130/80 to 139/89 mm Hg is stage 1 hypertension.'),
          ('Which sample best quantifies proteinuria in a school-age child while excluding orthostatic protein?',
           ['A first-morning spot urine protein-to-creatinine ratio',
            'A dipstick after school',
            'A random afternoon albumin dipstick',
            'A urine culture'],
           0,
           'A first-morning UPCR avoids the protein that appears when a child is upright and active. IPNA defines nephrotic range as UPCR '
           '&ge;200 mg/mmol (2 mg/mg).'),
          ('What did the CKiD U25 equations change compared with the bedside Schwartz formula?',
           ['They removed height from the equation',
            'They apply only to adults',
            'They use sex-specific and age-dependent constants across ages 1 to 25',
            'They use urine creatinine instead of serum creatinine'],
           2,
           'CKiD U25 uses K &times; height / creatinine with sex-specific or age- and sex-dependent K, and parallel cystatin C equations, '
           'developed in 928 participants aged 1 to 25.')],
 'terms': [('AAP', 'American Academy of Pediatrics'),
           ('ACR', 'Albumin-to-creatinine ratio'),
           ('CKD', 'Chronic kidney disease'),
           ('CKiD', 'Chronic Kidney Disease in Children (study)'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('eGFRcr', 'Creatinine-based estimated glomerular filtration rate'),
           ('GFR', 'Glomerular filtration rate'),
           ('IPNA', 'International Pediatric Nephrology Association'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('U25', 'Under 25 (CKiD equations for ages 1 to 25)'),
           ('UPCR', 'Urine protein-to-creatinine ratio')],
 'readings': [('how-to-properly-assess-kidney-function.html', 'How to Properly Assess Your Kidney Function: Creatinine, eGFR, Cystatin C & Urine ACR'),
              ('born-small-kidneys-for-life.html', 'Born Small, Kidneys for Life: Birth History and Kidney Health'),
              ('proteins-proteinuria.html', 'Proteins & Proteinuria')],
 'calcs': ['calc-ckid-u25-egfr.html', 'calc-schwartz-egfr.html', 'calc-pediatric-egfr.html', 'calc-pediatric-bp.html', 'calc-pediatric-growth-percentiles.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
