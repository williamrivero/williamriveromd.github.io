# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 18: CKD complications: anemia, mineral and bone disease, acidosis.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
KDIGO 2026 anemia pediatric algorithm checked against KDIGO's central illustration for children (no grades are printed on it); KDIGO 2017
CKD-MBD pediatric statements against the guideline summary; Goodman 2000, Brown 2022, Shroff 2017 and McAlister 2020 against PubMed
abstracts. Iron thresholds are quoted as the guideline states them. No doses."""

MODULE = {'image_alt': 'A pediatric nephrologist examines the knees of a girl standing with mild knock-knees in a clinic, while her mother holds a folder of laboratory results.',
 'objectives': ['Work up and treat anemia in a child with chronic kidney disease (CKD) using the KDIGO 2026 pediatric algorithm: iron status '
                'first, correctable causes next, erythropoiesis-stimulating agents last, separating graded recommendations from practice points.',
                'Explain chronic kidney disease&ndash;mineral and bone disorder (CKD-MBD) in a growing skeleton and apply KDIGO 2017 and pediatric '
                'recommendations on calcium, phosphate, parathyroid hormone, vitamin D and growth.',
                'Recognize metabolic acidosis as a growth problem as well as a chemistry problem, and state what the pediatric evidence does and does '
                'not show.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the keeper of the slow complications</span>The complications in this '
        'module do not call you at night. They show up as a child who is pale and tired at school, who limps, who stops growing, or whose '
        'arteries are calcifying silently. In a Philippine peritoneal dialysis (PD) or hemodialysis (HD) program you also manage what families can afford: an '
        'erythropoiesis-stimulating agent (ESA) bought a few vials at a time, binders taken when there is money, and a diet built on cheap '
        'processed food. Your duty is to look at these numbers every month, treat in the right order, and explain why each one matters for '
        'the child&rsquo;s future.</div>\n'
        '{{plain:Think of the kidney as a small factory that makes three products besides urine: a hormone that tells the marrow to make red '
        'cells, the active form of vitamin D that lets the gut take up calcium, and a steady export of acid. When the factory shrinks, all three '
        'supply lines fail together.}}\n'
        '<p>The picture has a limit. A factory that closes simply stops shipping. The body answers each shortage with a compensation that does '
        'its own harm: the parathyroid glands enlarge and pull calcium from bone, the marrow is starved of iron by an inflamed liver, and bone '
        'buffers acid by giving up its mineral. In a child these compensations land on a growing skeleton, so the cost is paid in height, '
        'deformity and arteries that age early.</p>\n'
        '{{cards:Key numbers|KDIGO 2026 pediatric algorithm, severe iron deficiency::Ferritin &lt;45 ng/mL: start iron|Iron indicated (pediatric '
        'algorithm)::Ferritin &lt;100 ng/mL with TSAT &lt;40%, or ferritin 100&ndash;300 ng/mL with TSAT &lt;25%|Infant length (KDIGO 2017, '
        '1B)::Measured at least quarterly in CKD G2&ndash;G5D|Coronary calcification (young adults on dialysis)::14 of 16 aged 20&ndash;30 vs none of 23 '
        'under 20|Bicarbonate and growth (CKiD, 1,082 children)::Bicarbonate &le;18 associated with height z score lower by 0.39 in '
        'nonglomerular CKD}}\n'
        '<p>Most children with CKD stage 4 and beyond have at least one of these complications, and many have all three. The order of treatment '
        'matters: iron before ESA, phosphate and vitamin D before calcimimetics or surgery, acidosis corrected before you blame growth hormone '
        'resistance. Your work is to find each problem early, treat in that order, and keep the growing skeleton in view.</p>\n',
 'case': {'title': 'The girl who limps to the PD clinic',
          'html': '<p>Angelica Navarro is 12 years old and has been on continuous ambulatory PD for two years at a pediatric center; she lives '
                  'in Tarlac City with her mother, Merly, who does her exchanges. At today&rsquo;s monthly clinic her hemoglobin is 8.0 g/dL, '
                  'ferritin 60 ng/mL and transferrin saturation (TSAT) 14%. Her serum phosphate is 7.2 mg/dL, calcium 8.6 mg/dL, parathyroid '
                  'hormone (PTH) has risen on each of the last three checks and is now well above the range the unit targets, and alkaline '
                  'phosphatase is high. Her bicarbonate is 20 mmol/L.</p>\n'
                  '<p>She walks with a limp, complains of knee pain, and has developed knock-knees over the past year; her height velocity has '
                  'slowed. Merly buys the ESA two vials at a time when she has money, so doses are skipped. The phosphate binder is taken '
                  '&ldquo;when we remember,&rdquo; and Angelica&rsquo;s favorite foods are instant noodles, processed meat and soft drinks. The '
                  'adult nephrologist who covers the PD unit on weekends has suggested a blood transfusion and a higher ESA dose.</p>\n',
          'questions': ['Why is Angelica anemic, and what should be done first?',
                        'Why is she limping and knock-kneed, and what is the order of treatment?',
                        'Does her bicarbonate matter, and what does the evidence say about acidosis and growth?']},
 'sections': [('anemia',
               'Anemia',
               'Anemia: iron first, ESA last',
               '<p><strong>Mechanism.</strong> Peritubular interstitial cells in the kidney sense oxygen delivery and release erythropoietin. In '
               'CKD that production falls relative to the degree of anemia. At the same time, inflammation and reduced kidney clearance raise '
               'hepcidin, which blocks iron absorption from the gut and traps iron in macrophages, so the marrow is short of iron even when stores '
               'seem adequate. Blood loss from sampling, from the dialysis circuit in HD, and from the gut adds to iron deficiency. '
               'Hyperparathyroidism, inadequate dialysis, infection and B12 or folate deficiency blunt the response to treatment.</p>\n'
               '<p><strong>The guideline.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2026 anemia guideline covers adults and '
               'children, uses the Grading of Recommendations Assessment, Development and Evaluation (GRADE) approach for its recommendations, and separately issues practice points that give clinical advice not '
               'supported by a systematic review.[[apn18_1]] Its algorithm for children, published as a figure and central illustration, sets out '
               'this order:[[apn18_2]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Step in the KDIGO 2026 pediatric algorithm</th><th>What it says</th><th>Physiologic '
               'reason</th></tr></thead><tbody>'
               '<tr><td>Screen</td><td>Complete blood count, reticulocytes, ferritin and TSAT; diagnose anemia by age-defined cutoffs</td><td>Normal '
               'hemoglobin changes with age</td></tr>'
               '<tr><td>Severe iron deficiency</td><td>Ferritin &lt;45 ng/mL: start iron, oral or intravenous according to the family&rsquo;s values '
               'and preferences</td><td>No marrow can respond without iron</td></tr>'
               '<tr><td>Iron indicated</td><td>Ferritin &lt;100 ng/mL with TSAT &lt;40%, or ferritin 100&ndash;300 ng/mL with TSAT &lt;25%</td><td>'
               'Functional deficiency: stores present but unavailable</td></tr>'
               '<tr><td>Monitor iron</td><td>Every 3 months; withhold if ferritin &gt;700 ng/mL or TSAT &ge;40%; suspend during active infection; '
               'switch oral to intravenous if no response or not tolerated</td><td>Excess iron and iron during infection may do harm</td></tr>'
               '<tr><td>Look for other causes</td><td>Bleeding, hemolysis, inflammation, B12, folate, thyroid, PTH and others</td><td>ESA will not '
               'overcome an untreated cause</td></tr>'
               '<tr><td>Consider ESA</td><td>After correctable causes, weighing symptoms, the benefits of a higher hemoglobin and the harms of '
               'transfusion or ESA; give subcutaneously at the lowest effective dose; check hemoglobin every 2&ndash;4 weeks after starting or '
               'changing; base maintenance thresholds on benefits and harms; suspend ESA in stroke or thrombosis</td><td>Erythropoietin '
               'replacement works only with iron and a responsive marrow</td></tr>'
               '</tbody></table></div>\n'
               '<p>The illustration does not print grades beside each step. When you need to say how strong a statement is, quote the grade or '
               '&ldquo;practice point&rdquo; label from the full guideline text, not from the figure. The ESA dose and the hemoglobin '
               'threshold for a given child come from your unit&rsquo;s pediatric protocol.</p>\n'
               '<p><strong>Transfusion.</strong> In a child who may need a kidney transplant, every transfusion risks sensitization to human '
               'leukocyte antigens (HLA) and can lengthen the wait for a compatible kidney. Transfusion is for symptomatic or dangerous anemia, not '
               'a way to raise a number that iron and a regular ESA supply could fix.</p>\n'
               '<p><strong>Cost and supply.</strong> An ESA bought two vials at a time is an ESA given irregularly, and irregular dosing looks like '
               'resistance. Before you raise the dose, find out how many doses were actually given. Ask the hospital&rsquo;s social service about '
               'assistance programs, and confirm with your PhilHealth liaison what the child&rsquo;s dialysis package currently includes on the date '
               'of service; do not assume medicines are covered.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">At the HD unit in Lucena, the hemoglobin that would not rise &middot; fictional</span>'
               '<p>An 11-year-old boy on hemodialysis in an adult unit has a hemoglobin of 7.6 g/dL. The adult nephrologist covering the unit has raised the '
               'ESA order twice. You ask for the dose log and the iron studies: ferritin is 38 ng/mL, and the log shows that a third of doses were '
               'skipped because the family could not buy them that week.</p><p>You start iron, ask the unit&rsquo;s social worker to apply for '
               'ESA assistance, and agree with the adult nephrologist to hold the dose steady until the iron and the supply are sorted.</p>'
               '<p class="tc-scene-take"><b>What this shows.</b> In a resource-limited unit, anemia is often an iron problem and a supply problem '
               'before it is a dose problem.</p></div>\n'
               '{{key:Check iron and count the doses actually given before you call a child ESA-resistant or order a transfusion.}}\n'
               '\n{{fig:apn18_a}}\n'),
              ('mbd',
               'Bone and mineral',
               'Mineral and bone disease in a growing skeleton',
               '<p><strong>Mechanism.</strong> As nephrons are lost, phosphate excretion falls. Bone cells respond by releasing fibroblast growth '
               'factor 23 (FGF23), which increases phosphate excretion per nephron and suppresses activation of vitamin D. Calcitriol falls, gut '
               'calcium absorption falls, and serum calcium tends down. The parathyroid glands, sensing low calcium, low calcitriol and high '
               'phosphate, secrete more PTH and enlarge. PTH holds calcium up by increasing bone resorption. In an adult this produces renal '
               'osteodystrophy; in a child it lands on the growth plate.</p>\n'
               '<p><strong>The growing skeleton.</strong> High PTH disorganizes the growth plate and weakens metaphyseal bone. Children develop '
               'rickets-like changes, genu valgum (knock-knees) or bowing, bone pain, fractures, and slipped capital femoral epiphysis, which presents '
               'as hip or knee pain and a limp in an older child or adolescent. Native vitamin D deficiency is common in children with CKD and is '
               'causally linked with rickets and fractures in healthy children and those with CKD.[[apn18_4]] Over-suppression causes the opposite '
               'problem, low-turnover (adynamic) bone, which also impairs growth and lets calcium go to soft tissues.</p>\n'
               '<p><strong>Arteries.</strong> Calcium and phosphate that bone cannot take up deposit in vessels. Goodman and colleagues scanned 39 '
               'young people on dialysis aged 7 to 30: none of the 23 under 20 had coronary calcification on electron-beam computed tomography (CT), but 14 of the 16 aged '
               '20 to 30 did, against 3 of 60 healthy controls. Those with calcification had been on dialysis longer and had higher phosphate, '
               'calcium&ndash;phosphate product and calcium intake, and in 10 patients rescanned after about 20 months the calcification score nearly '
               'doubled.[[apn18_7]] This is a small cross-sectional study with limited follow-up; it shows that the exposure accumulated in childhood '
               'appears as coronary calcification in early adulthood, not that any single treatment prevents it.</p>\n'
               '<p><strong>The guidelines.</strong> The KDIGO 2017 CKD-MBD update recommends monitoring calcium, phosphate, PTH and alkaline '
               'phosphatase from CKD G3a in adults (1C) and suggests starting in G2 in children; recommends that infants with CKD G2 to G5D have length '
               'measured at least quarterly and children assessed for linear growth at least annually (1B); suggests maintaining serum calcium in '
               'the age-appropriate normal range in children with CKD G3a to G5D (2C); and states that in children it is reasonable to base the '
               'choice of phosphate-lowering treatment on serum calcium (not graded).[[apn18_3]] European pediatric working groups published '
               'GRADE-based recommendations for native vitamin D and for active vitamin D analogues in children with CKD stages 2 to 5 and on dialysis, '
               'noting how few pediatric studies exist and labeling expert-opinion statements as such.[[apn18_4]][[apn18_5]] The Pediatric Renal '
               'Nutrition Taskforce (PRNT) gives graded recommendations on dietary calcium and phosphate, including the common phosphate-containing '
               'foods and the management of hyperphosphatemia.[[apn18_6]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Likely mechanism</th><th>What it means for the skeleton</th><th>First '
               'move</th></tr></thead><tbody>'
               '<tr><td>High phosphate</td><td>Reduced excretion; high intake from processed food additives</td><td>Drives PTH and vascular '
               'calcification</td><td>Diet with the dietitian; binder taken with meals; adequate dialysis</td></tr>'
               '<tr><td>Low or low-normal calcium</td><td>Low calcitriol; low intake</td><td>Drives PTH; rickets</td><td>Keep in the age-appropriate '
               'range (KDIGO 2017, 2C)</td></tr>'
               '<tr><td>Rising PTH, high alkaline phosphatase</td><td>Secondary hyperparathyroidism; high-turnover bone</td><td>Deformity, pain, '
               'slipped epiphysis, poor growth</td><td>Correct phosphate, calcium and vitamin D; active vitamin D per protocol</td></tr>'
               '<tr><td>Low 25-hydroxyvitamin D</td><td>Poor intake, little sun, losses</td><td>Rickets, fractures</td><td>Native vitamin D per the '
               'pediatric recommendations</td></tr>'
               '<tr><td>Very low PTH with high calcium</td><td>Over-suppression; adynamic bone</td><td>Poor growth; soft-tissue calcium</td><td>Reduce '
               'calcium load and active vitamin D</td></tr>'
               '</tbody></table></div>\n'
               '<p>In the Philippines, phosphate comes cheaply. Instant noodles, processed meats, cheese spreads and dark soft drinks carry phosphate '
               'additives that are absorbed far more completely than the phosphate in natural food. A dietitian who knows local food and local '
               'prices is worth more than a second binder.</p>\n'
               '{{key:Treat phosphate, calcium and vitamin D first, measure growth, and watch the bones and joints. A limp in a child with high PTH '
               'is a hip until proven otherwise.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the PD clinic, the binder in the cupboard &middot; fictional</span><p>A 10-year-old '
               'boy on PD in Pampanga has a phosphate that will not come down. His mother shows you a full bottle of binder; he takes it at bedtime '
               'because &ldquo;that is when we remember.&rdquo;</p><p>You explain that the binder works only in the gut, with the food, and the '
               'dietitian moves it to the main meals and swaps his afternoon instant noodles for rice and egg.</p><p class="tc-scene-take"><b>What '
               'this shows.</b> A binder taken without food binds nothing. Ask when and how, not only whether.</p></div>\n'
               '\n{{fig:apn18_b}}\n'),
              ('acidosis',
               'Acidosis',
               'Metabolic acidosis and growth',
               '<p><strong>Mechanism.</strong> The kidney excretes the daily acid load by making ammonium and regenerating bicarbonate. As nephron '
               'mass falls, each nephron makes more ammonium, which may itself injure the interstitium through complement activation and fibrosis. '
               'When total ammonium production can no longer keep up, bicarbonate falls. Bone buffers the retained acid by releasing calcium carbonate '
               'and phosphate, muscle protein is broken down, and acidosis blunts the growth hormone and insulin-like growth factor 1 (IGF-1) axis. In a '
               'child, each of these lowers growth.</p>\n'
               '<p><strong>The evidence.</strong> In the Chronic Kidney Disease in Children (CKiD) cohort of 1,082 children (808 nonglomerular, 274 '
               'glomerular), a baseline bicarbonate of 22 mEq/L or less was associated with worse height z scores in all children. Over time, '
               'bicarbonate of 18 or less and 19 to 22 mEq/L were associated with height z scores lower by 0.39 and 0.17 in children with '
               'nonglomerular CKD, after adjustment for glomerular filtration rate (GFR), proteinuria, calcium, phosphate, PTH and CKD duration; no significant association was '
               'found in glomerular disease. Children with persistent alkali therapy had a positive association between bicarbonate and height '
               'z score.[[apn18_8]] This is observational. It suggests that acidosis contributes to poor growth and that sustained correction may '
               'help, but it is not a trial, and the authors call for one. Height z score is a measured outcome that matters to families; it is not '
               'the same as adult height.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Effect of acidosis</th><th>Mechanism</th><th>What you see</th></tr></thead><tbody>'
               '<tr><td>Poor growth</td><td>Growth hormone and IGF-1 axis blunted; bone buffering</td><td>Falling height velocity; low height z '
               'score</td></tr>'
               '<tr><td>Bone disease</td><td>Calcium carbonate released from bone to buffer acid</td><td>Worsening CKD-MBD despite phosphate '
               'control</td></tr>'
               '<tr><td>Muscle wasting</td><td>Protein breakdown increased</td><td>Low weight-for-height; low creatinine generation</td></tr>'
               '<tr><td>Possible progression</td><td>Adaptive ammonium production injures the interstitium (hypothesis)</td><td>Faster decline in estimated GFR (eGFR) '
               'in some cohorts</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>In practice.</strong> Check bicarbonate at every CKD visit and every monthly dialysis review. Alkali therapy is cheap, and '
               'the dose and preparation come from your unit&rsquo;s formulary. Watch sodium load in a child who is hypertensive or overloaded, and '
               'remember that in a child on PD the dialysate buffer contributes too.</p>\n'
               '{{key:A low bicarbonate in a growing child is a growth problem. Correct it before you conclude that the child needs growth '
               'hormone.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Monthly review in the dialysis child.</strong> Look at hemoglobin, ferritin and TSAT on the schedule your unit sets; '
               'calcium, phosphate and PTH; bicarbonate; height, weight and height velocity; and the joints and gait. Ask the family how many ESA '
               'doses were given, when the binder is taken, and what the child ate yesterday.</p>\n'
               '<p><strong>Treat in order.</strong> For anemia: iron status, correctable causes, then ESA as the KDIGO 2026 pediatric algorithm '
               'describes. For bone: phosphate (diet, binder with meals, adequate dialysis), calcium in the age-appropriate range, native vitamin D '
               'repletion, then active vitamin D for rising PTH as the pediatric recommendations describe. For acidosis: alkali per protocol. For '
               'growth: all of the above before growth hormone (Module 17).</p>\n'
               '<p><strong>Look at the child, not only the labs.</strong> Examine the knees, ankles and wrists; watch the child walk; ask about bone '
               'pain. Any new limp or hip or knee pain in a child with high PTH needs a hip radiograph to look for a slipped capital femoral '
               'epiphysis, and an orthopedic opinion if present.</p>\n'
               '<p><strong>Coordinate with the dialysis prescription.</strong> Each of these complications depends on dialysis delivered. Phosphate and '
               'acid are removed by dialysis, and PD loses protein and some vitamins into the effluent. When phosphate or bicarbonate drifts, check '
               'that the prescribed dialysis is being done (missed PD exchanges and shortened HD sessions are common reasons), and review adequacy '
               'with the dialysis team (Modules 20 to 25).</p>\n'
               '<p><strong>Share the plan with whoever covers the unit.</strong> Many children on dialysis are seen on weekends by an adult nephrologist '
               'or a physician on duty. Write the anemia, bone and acid plan where they will read it: the iron decision, the ESA dose policy, the binder '
               'timing and the transfusion threshold your unit uses for children awaiting transplant. A covering doctor who does not know the plan will '
               'treat the number in front of them.</p>\n'
               '<p><strong>Explain the long view to the family.</strong> These complications feel abstract to a tired mother doing exchanges every '
               'night. Connect each to something the family can see: pale skin and tiredness, the limp, the height chart, and, for older children, the '
               'arteries they will need as adults and the transplant they are waiting for.</p>\n'
               '{{flow:Monthly complication review|Blood::Hemoglobin, ferritin, TSAT; doses actually given; signs of bleeding or infection.|Bone::'
               'Calcium, phosphate, PTH, alkaline phosphatase; vitamin D status at intervals; binder timing.|Acid::Bicarbonate; alkali taken.|Growth::'
               'Height, weight, velocity, plotted.|Body::Gait, knees, hips, wrists; bone pain.|Plate::What the child ate; phosphate additives; '
               'dietitian follow-up.|Plan::One change at a time, with a date to recheck.}}\n'
               '<div class="table-wrap"><table><thead><tr><th>Common mistake</th><th>Why it harms</th><th>Better move</th></tr></thead><tbody>'
               '<tr><td>Raising the ESA dose without checking iron or adherence</td><td>Higher exposure, little gain, more cost</td><td>Iron status '
               'and dose count first</td></tr>'
               '<tr><td>Transfusing for a number</td><td>HLA sensitization before transplant</td><td>Transfuse for symptoms or danger only</td></tr>'
               '<tr><td>Binder at bedtime</td><td>No food to bind</td><td>Binder with meals and snacks containing phosphate</td></tr>'
               '<tr><td>Ignoring a limp</td><td>Slipped epiphysis can progress</td><td>Examine; image the hip</td></tr>'
               '<tr><td>Accepting bicarbonate in the high teens</td><td>Growth and bone suffer</td><td>Correct per protocol and recheck</td></tr>'
               '</tbody></table></div>\n'
               '{{call:<ul><li>Hemoglobin falling quickly, or symptoms of severe anemia</li><li>New limp, hip or knee pain with high PTH</li><li>Calcium '
               'high with very low PTH (over-suppression)</li><li>Phosphate persistently high despite diet and binder</li><li>Bicarbonate falling '
               'despite alkali</li></ul>}}\n'
               '{{key:Every month, ask three questions for each complication: what is the number, what was actually taken, and what is the child&rsquo;s '
               'body telling you.}}\n')],
 'debrief': ['<p><strong>Why anemic, and what first?</strong> She has absolute or functional iron deficiency (ferritin 60 ng/mL, TSAT 14%, '
             'which meets the KDIGO 2026 pediatric algorithm&rsquo;s indication for iron), irregular ESA dosing because of cost, and probably a '
             'contribution from her hyperparathyroidism. Start iron, choosing the route with Merly, and count how many ESA doses were actually given '
             'before anyone raises the dose. Look for other causes. Avoid transfusion unless she is symptomatic or in danger, because sensitization '
             'could lengthen her wait for a transplant. Ask social service about ESA assistance and confirm coverage with the PhilHealth liaison.</p>\n',
             '<p><strong>Why the limp?</strong> High phosphate from processed food and missed binders, low-normal calcium and rising PTH with a high '
             'alkaline phosphatase mean active secondary hyperparathyroidism with high-turnover bone disease, which is deforming her knees and '
             'slowing her growth. Get a hip radiograph to exclude a slipped capital femoral epiphysis, and an orthopedic opinion if present. Then '
             'treat in order: the dietitian on phosphate additives, the binder with meals, a review of PD adequacy, calcium in the age-appropriate '
             'range, native vitamin D status, and active vitamin D for PTH as the pediatric recommendations and unit protocol describe.</p>\n',
             '<p><strong>Does the bicarbonate matter?</strong> Yes. A bicarbonate of 20 mmol/L falls in the 19&ndash;22 range that the CKiD analysis '
             'associated with lower height z scores in nonglomerular CKD, and acidosis also worsens bone disease and muscle wasting. The evidence is '
             'observational and children with persistent alkali use did better, so correct it as the unit&rsquo;s protocol directs, review the PD '
             'prescription, and recheck. Explain to Merly that pale skin, knee pain and slow growth are linked, and that fixing the basics in order '
             'is how they get better.</p>\n'],
 'skills': {'title': 'CKD complications: anemia, mineral and bone disease, acidosis',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Interprets ferritin and TSAT against the KDIGO 2026 pediatric algorithm and explains the iron decision to a family', False),
                      ('Reviews a child&rsquo;s calcium, phosphate, PTH and alkaline phosphatase trend and states the order of treatment', False),
                      ('Examines gait, knees and hips in a child with CKD-MBD and orders hip imaging when indicated', False),
                      ('Takes a dietary history that identifies phosphate additives and binder timing', False)],
            'placement': 'Pediatric CKD or dialysis clinic under supervision'},
 'quiz': [('A child on PD has hemoglobin 8.0 g/dL, ferritin 60 ng/mL and TSAT 14%. What does the KDIGO 2026 pediatric algorithm indicate first?',
           ['Double the ESA dose',
            'Iron therapy, after which other causes are sought and ESA is reconsidered',
            'Immediate transfusion',
            'No treatment until ferritin is below 45 ng/mL'],
           1,
           'Ferritin below 100 ng/mL with TSAT below 40% meets the algorithm&rsquo;s indication for iron.'),
          ('Why should transfusion be avoided where possible in a child who may need a kidney transplant?',
           ['Transfusion causes hypophosphatemia',
            'Transfusion lowers PTH',
            'Transfusion can sensitize the child to HLA antigens and lengthen the wait for a compatible kidney',
            'Transfusion is contraindicated on PD'],
           2,
           'Sensitization narrows the pool of compatible donors.'),
          ('What did KDIGO 2017 recommend about growth monitoring in children with CKD G2&ndash;G5D?',
           ['Length measured at least quarterly in infants and linear growth assessed at least annually in children (1B)',
            'Height every five years',
            'No growth monitoring is needed on dialysis',
            'Bone age every month'],
           0,
           'This is recommendation 3.2.5 of the 2017 update, graded 1B.'),
          ('What did the Goodman 2000 study of young people on dialysis find?',
           ['Coronary calcification in all children under 10',
            'No calcification in any patient',
            'Calcification unrelated to phosphate',
            'No calcification in those under 20, but in 14 of 16 aged 20 to 30, associated with dialysis duration and higher phosphate'],
           3,
           'Exposure accumulated in childhood shows in early adulthood; the study was small and cross-sectional.'),
          ('What does the CKiD analysis of bicarbonate and growth show?',
           ['A randomized benefit of alkali on final height',
            'An observational association between low bicarbonate and lower height z scores in nonglomerular CKD',
            'No relation in any group',
            'That acidosis improves growth'],
           1,
           'The authors call for trials; persistent alkali use was associated with better height z scores.')],
 'terms': [('CKD', 'Chronic kidney disease'),
           ('CKD-MBD', 'Chronic kidney disease&ndash;mineral and bone disorder'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('ESA', 'Erythropoiesis-stimulating agent'),
           ('TSAT', 'Transferrin saturation'),
           ('PTH', 'Parathyroid hormone'),
           ('FGF23', 'Fibroblast growth factor 23'),
           ('GRADE', 'Grading of Recommendations Assessment, Development and Evaluation'),
           ('HLA', 'Human leukocyte antigen'),
           ('PD', 'Peritoneal dialysis'),
           ('HD', 'Hemodialysis'),
           ('PRNT', 'Pediatric Renal Nutrition Taskforce'),
           ('CKiD', 'Chronic Kidney Disease in Children cohort study'),
           ('GFR', 'Glomerular filtration rate'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('IGF-1', 'Insulin-like growth factor 1'),
           ('CT', 'Computed tomography')],
 'readings': [('anemia-management.html', 'Anemia Management'),
              ('ckd-mbd.html', 'CKD-MBD: Kidney, Bone & Heart'),
              ('metabolic-acidosis-ckd.html', 'Metabolic Acidosis in CKD — The Silent Bicarbonate Drop Linked to Faster Kidney Loss')],
 'calcs': ['calc-iron-status-tsat.html', 'calc-ckd-mbd.html', 'calc-pediatric-calcium.html', 'calc-phosphorus-load.html',
           'calc-pediatric-growth-percentiles.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
