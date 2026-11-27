# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 21: Pregnancy, children and older adults.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
Renal physiology of pregnancy, the CKD-pregnancy meta-analysis, TOCOS, the intensive hemodialysis cohort comparison,
the frailty phenotype and the nursing-home dialysis cohort checked against PubMed abstracts; ACOG Practice Bulletin 222
definitions; AAP 2017 blood pressure categories and AAP 2018 maintenance fluid statement as in the verified APN banks;
KDIGO 2024 Chapter 5 practice points against the KDIGO summary. No doses. Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow, an obstetrician and a pregnant Filipino woman with kidney disease review a blood pressure log together in a Pampanga hospital clinic.",
    "objectives": [
        "<strong>Intern:</strong> Recognize three patients who look well until they do not: the pregnant woman with new hypertension after 20 weeks, the child whose blood pressure, urine output or weight has not been measured correctly, and the frail older adult whose creatinine looks &ldquo;normal.&rdquo; Report each one early.",
        "<strong>Resident:</strong> Adapt acute kidney injury (AKI) and chronic kidney disease (CKD) care to pregnancy, childhood and old age: read creatinine against the physiology of each, use pediatric estimating equations and blood pressure percentiles, and review medicines for fetal, pediatric and geriatric risk.",
        "<strong>Fellow:</strong> Counsel a woman with CKD or on dialysis about pregnancy using absolute and relative risks, plan an adolescent&rsquo;s transition to adult care, and offer conservative kidney management to an older adult as a real option alongside dialysis.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; three patients the adult renal service often gets wrong</span>The <strong>intern</strong> measures and reports: the blood pressure and urine dipstick of a pregnant woman, the weight and cuff size of a child, the falls and confusion of an older adult. The <strong>resident</strong> reinterprets the numbers for the body in front of them and reviews every medicine for the baby, the child or the frail elder. The <strong>fellow</strong> holds the long conversations: whether and when to become pregnant, when a teenager is ready for the adult clinic, and whether dialysis will give an 85-year-old more good days or fewer.</div>
{{plain:Picture a jeepney built for twenty passengers. Most days it runs fine with sixteen. Load it with twenty-four, as in pregnancy, and the same engine must work harder; small faults show quickly. Put a child behind the wheel and every control is the wrong size. Drive an old jeepney with a worn engine and a quiet dashboard, and the gauges stay in the normal range until the engine stops.}}
<p>The picture has a limit. A jeepney does not change its own engine. The body does. In pregnancy the glomerular filtration rate (GFR) rises by about 50%, plasma volume grows by 30% to 50%, and blood pressure falls by about 10 mm Hg by the second trimester, so a creatinine that is &ldquo;normal&rdquo; for a nonpregnant woman may already mean lost function.[[ntr21_1]] In children, GFR matures through infancy and creatinine rises with muscle as the child grows, so adult reference ranges and adult equations do not apply.[[ntr21_8]] In older adults, muscle mass falls, so a low creatinine can hide a low GFR, and frailty, not age, predicts who is harmed by treatment.[[ntr21_11]]</p>
{{cards:Key numbers|GFR in pregnancy::Rises about 50%; creatinine, urea and uric acid fall (review)|Preeclampsia (ACOG 2020)::Blood pressure &ge;140/90 mm Hg after 20 weeks with proteinuria or severe features; severe range &ge;160/110|CKD and pregnancy (meta-analysis, 506,340 pregnancies)::Preeclampsia odds ratio 10.36; premature delivery odds ratio 5.72|Intensive hemodialysis in pregnancy (cohort comparison)::Live births 85% with more than 36 hours a week versus 48% with 20 hours or less|Adolescents 13 and older (AAP 2017)::Stage 1 hypertension 130/80 to 139/89 mm Hg|Nursing home residents starting dialysis (US cohort)::At 12 months, 58% had died and 13% kept their earlier function}}
<p>Most pregnant women with mild CKD, most children seen on an adult ward and most older adults with CKD do well when the team adjusts its habits. A few are harmed because no one did: the preeclampsia called a &ldquo;flare,&rdquo; the child given adult fluids, the elder started on dialysis without being asked what she wanted. Your work is to change your reference points for each of these three bodies, to call the specialist who knows them best, and to keep the person&rsquo;s own goals at the center.</p>
""",
    "case": {"title": "Ten weeks", "html": """
<p>Monday, 2 p.m., the renal clinic of a government hospital in San Fernando, Pampanga. Mrs. Kristine Aquino, 30, a public school teacher, has immunoglobulin A nephropathy (IgAN), diagnosed by biopsy two years ago. Her estimated glomerular filtration rate (eGFR) is 52 mL/min/1.73 m&sup2;, urine protein-to-creatinine ratio 1.1 g/g, and clinic blood pressure 132/84 mm Hg. She takes losartan and a statin.</p>
<p>She is ten weeks pregnant. The pregnancy was not planned, and she and her husband are happy. Her mother, who came with her, says she should stop &ldquo;all those chemicals&rdquo; for the baby&rsquo;s sake. Her obstetrician at the district hospital has asked the renal service for &ldquo;clearance.&rdquo; The resident, Dr. Mark Dizon, has written &ldquo;continue home meds&rdquo; on the referral form.</p>
""", "questions": ["What must change in her medicines and monitoring now, and who needs to know?",
                  "What are her risks in this pregnancy, and how would you explain them in numbers she can follow?",
                  "At 28 weeks her blood pressure is 152/98 mm Hg and her proteinuria has doubled. How would you separate preeclampsia from an IgAN flare, and who leads?"]},
    "sections": [
        ("pregnancy", "Pregnancy", "Pregnancy: a different normal, a narrower margin", """
<p>Pregnancy reshapes the kidney within weeks. Systemic vascular resistance falls, partly because vessels become less sensitive to vasoconstrictor hormones. The renin-angiotensin-aldosterone system switches on in response, and the body retains sodium and water, so plasma volume expands by 30% to 50%. Kidney blood flow and GFR rise by about 50%, and serum creatinine, urea and uric acid fall. The thirst threshold resets lower, so serum sodium runs slightly low. The kidneys lengthen, and physiologic dilation of the collecting systems is seen in up to 80% of women.[[ntr21_1]]</p>
<p>Three practical consequences follow. A creatinine that would be normal outside pregnancy may represent reduced function. Mild hydronephrosis on ultrasound is often physiologic, especially on the right. And estimating equations were not built for pregnancy, so follow the trend in creatinine and protein rather than an eGFR.</p>
{{fig:ntr21_a}}
<h3>Preeclampsia: recognize it early</h3>
<p>The American College of Obstetricians and Gynecologists (ACOG) defines preeclampsia as new blood pressure of 140/90 mm Hg or higher on two occasions at least four hours apart after 20 weeks of gestation, with proteinuria (300 mg or more in 24 hours, or a protein-to-creatinine ratio of 0.3 mg/mg or more) or, in the absence of proteinuria, with severe features: thrombocytopenia, rising creatinine, raised liver enzymes, pulmonary edema, or new headache or visual disturbance. Blood pressure of 160/110 mm Hg or higher is in the severe range.[[ntr21_2]] HELLP syndrome (hemolysis, elevated liver enzymes and low platelets) is a severe form.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding after 20 weeks</th><th>Points toward preeclampsia</th><th>Points toward the kidney disease itself</th></tr></thead>
<tbody>
<tr><td>Blood pressure</td><td>New or sharply rising, with headache or visual change</td><td>Hypertension present before 20 weeks</td></tr>
<tr><td>Urine</td><td>Rising protein with a bland sediment</td><td>Active sediment: dysmorphic red cells, red cell casts</td></tr>
<tr><td>Blood</td><td>Falling platelets, rising liver enzymes, hemolysis</td><td>Low complement or positive serology in lupus</td></tr>
<tr><td>Timing</td><td>Third trimester, resolving after delivery</td><td>Any time, including the first trimester</td></tr>
</tbody></table></div>
<p>The overlap is real, and the two can coexist. Separating them is a joint task for the obstetrician and the nephrologist, because the treatment of severe preeclampsia is delivery, which the obstetric team leads.</p>
<h3>Pregnancy with CKD: risks in numbers</h3>
<p>A meta-analysis of 23 studies with 506,340 pregnancies found that women with CKD had higher odds of preeclampsia (odds ratio 10.36), premature delivery (5.72), small-for-gestational-age or low birth weight (4.85), cesarean section (2.67) and pregnancy failure (1.80) than women without CKD. In the nine studies with long-term kidney follow-up, pregnancy was not associated with faster CKD progression (odds ratio 0.96, 95% confidence interval 0.69 to 1.35).[[ntr21_3]] These are pooled observational data and relative odds; the absolute risk depends on the baseline.</p>
<p>The Torino-Cagliari Observational Study (TOCOS) gives the absolute picture. Comparing 504 pregnancies in women with CKD with 836 low-risk pregnancies, a combined outcome of preterm delivery, neonatal intensive care or small-for-gestational-age occurred in 34.1% of women with CKD stage 1 and 90.0% of those with stages 4 to 5. Even women with stage 1 CKD and no hypertension, proteinuria or systemic disease had higher odds of the combined outcome than controls (odds ratio 1.88).[[ntr21_4]] Risk rises with stage, hypertension and proteinuria, and it is never zero.</p>
<h3>Pregnancy on dialysis</h3>
<p>Fertility falls in advanced CKD, and pregnancy on dialysis is uncommon and high risk. In a comparison of 22 pregnancies in a Toronto program that used intensive hemodialysis with 70 pregnancies in a United States registry, live births were 86.4% versus 61.4%, and median gestation was 36 versus 27 weeks. Live births were 48% in women dialyzed 20 hours a week or less and 85% in those dialyzed more than 36 hours a week.[[ntr21_5]] This was an observational comparison of small cohorts from different eras; it supports intensifying dialysis in pregnancy but does not set a number of hours. In the Philippines, intensive hemodialysis means extra sessions beyond the usual schedule. Plan early with the unit and the family how they will be arranged and paid for, and confirm PhilHealth session counts on the date of service.</p>
<h3>Medicines</h3>
<p>Angiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) carry fetal risk, which the Kidney Disease: Improving Global Outcomes (KDIGO) blood pressure guideline lists among the cautions for these first-line agents.[[ntr21_6]] Mycophenolate is teratogenic and must be replaced before conception in women with lupus or a transplant. Statins are usually stopped in pregnancy. ACOG recommends low-dose aspirin, started in the late first or early second trimester, for women at high risk of preeclampsia, a group that includes women with kidney disease.[[ntr21_2]] The choice and timing of each change are made with the obstetrician and the attending nephrologist; the doses come from them and the formulary.</p>
{{call:Stop and call the attending nephrologist and the obstetric team now when a pregnant woman with kidney disease has <ul><li>blood pressure of 160/110 mm Hg or higher;</li><li>headache, visual change, epigastric pain or breathlessness;</li><li>a rising creatinine, falling platelets or rising liver enzymes;</li><li>a fall in urine output or new edema of the face.</li></ul>Do this per unit protocol, but always ask the attending nephrologist for guidance.}}
{{key:In pregnancy, judge creatinine against a lower normal, follow trends rather than eGFR, and treat every new rise in blood pressure after 20 weeks as preeclampsia until the obstetrician and nephrologist agree it is not.}}
"""),
        ("child-adult-team", "The child on an adult team", "The child seen by an adult team: what must change", """
<p>Many Philippine provincial hospitals have no pediatric nephrologist. The child with acute kidney injury, nephrotic syndrome or hypertension may be seen first by an adult internal medicine resident or an adult nephrology fellow on a shared call schedule. A child is not a small adult, and the errors come from adult habits.</p>
<div class="table-wrap"><table>
<thead><tr><th>Adult habit</th><th>Why it fails in a child</th><th>What to do instead</th></tr></thead>
<tbody>
<tr><td>Reading creatinine against adult ranges</td><td>Normal creatinine is much lower in children and rises with age and muscle</td><td>Use a pediatric estimating equation such as the Chronic Kidney Disease in Children under-25 (CKiD U25) equation</td></tr>
<tr><td>Fixed blood pressure cut points</td><td>Normal pressure rises with age, sex and height</td><td>Use percentiles for children under 13; adult-style cut points from 13</td></tr>
<tr><td>Fluids by the liter</td><td>Volume, electrolytes and glucose needs scale with weight; hypotonic fluids cause hyponatremia</td><td>Weight-based fluids with isotonic maintenance solutions, per the pediatric protocol</td></tr>
<tr><td>Doses from memory</td><td>Doses are by weight or body surface area, with maximums</td><td>Use the pediatric formulary; have a second person check</td></tr>
<tr><td>Consent from the patient alone</td><td>Parents give permission; the child gives assent as able</td><td>Explain to both, in words the child understands</td></tr>
</tbody></table></div>
<p>The estimating equations matter because creatinine-based GFR in children depends on height. The CKiD U25 equations, developed in children and young adults with CKD, use age- and sex-specific constants from 1 to 25 years and allow one equation to follow a patient across the move to adult care.[[ntr21_8]] The site&rsquo;s pediatric eGFR calculators carry them.</p>
<p>The American Academy of Pediatrics (AAP) 2017 guideline defines hypertension in children aged 1 to under 13 by percentiles for age, sex and height, with stage 1 starting at the 95th percentile, and uses adult-style cut points from age 13: stage 1 at 130/80 to 139/89 mm Hg and stage 2 at 140/90 mm Hg or higher.[[ntr21_7]] Use a cuff whose bladder width is at least 40% of the arm circumference; a cuff too small gives falsely high readings.[[ntr21_7]]</p>
<p>For maintenance intravenous fluids, the AAP 2018 guideline recommends isotonic solutions with appropriate potassium chloride and dextrose for patients from 28 days to 18 years of age (evidence quality A, strong recommendation), with stated exclusions such as neurosurgical, cardiac and kidney disorders that need individual plans.[[ntr21_10]] A child with AKI or nephrotic syndrome often falls into that excluded group, which is exactly why the pediatric nephrologist should be called.</p>
<h3>When to call the pediatric nephrologist</h3>
<p>Call the pediatric nephrologist, by phone or teleconsultation if none is on site, for every child with AKI, nephrotic syndrome at first presentation or with complications, stage 2 hypertension or hypertension with symptoms, hematuria with proteinuria or a rising creatinine, a suspected congenital anomaly of the kidney and urinary tract, or any child being considered for dialysis. In the Philippines, transfer to a regional pediatric center often depends on the family&rsquo;s money and transport; start that conversation early.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>The Attending Pediatric Nephrologist track is the pediatric spine of this course. Its Module 2 covers GFR maturation, the estimating equations and blood pressure measurement in children, and its Module 28 covers pediatric medicines and safeguarding. Pediatric residents should read both alongside this module. See <a href="attending-pediatric-nephrologist-02-growing-kidney-assessment.html">Attending Pediatric Nephrologist, Module 2</a> and <a href="attending-pediatric-nephrologist-28-medicines-safeguarding-service.html">Attending Pediatric Nephrologist, Module 28</a>.</div>
{{key:When a child arrives on an adult service, change four things at once: the creatinine reference, the blood pressure reference, the fluid plan and the dose source. Then call the pediatric nephrologist.}}
"""),
        ("older", "Older adults", "Older adults: frailty, misleading creatinine and the question of dialysis", """
<p>The older adult with CKD brings three traps. Creatinine underestimates the problem. Medicines pile up. And dialysis, offered by default, may not deliver what the patient hopes for.</p>
<h3>Creatinine and the shrinking muscle</h3>
<p>Creatinine comes from muscle. A frail 80-year-old woman who weighs 40 kg makes little creatinine, so her serum value may sit in the laboratory&rsquo;s normal range while her GFR is low. Estimating equations partly adjust for age, but not for unusually low muscle mass. KDIGO 2024 advises adding cystatin C when creatinine-based estimates are likely to be inaccurate and the decision matters.[[ntr21_12]] Cystatin C is expensive and not available in many Philippine laboratories. When you cannot get it, say in the note that the eGFR probably overestimates function, and dose medicines cautiously.</p>
<h3>Frailty, not age</h3>
<p>Fried and colleagues defined frailty in 5,317 adults aged 65 and older as three or more of five features: unintentional weight loss, self-reported exhaustion, weak grip, slow walking and low physical activity. Frailty affected 6.9% of these community-dwelling adults and predicted falls, worsening disability, hospital admission and death independently of other illness.[[ntr21_11]] Frailty is far more common in people with advanced CKD and on dialysis than in the community, and it is what separates the 80-year-old who will do well on dialysis from the one who will not.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain of a geriatric assessment</th><th>What to check on a renal ward</th><th>Why it changes the kidney plan</th></tr></thead>
<tbody>
<tr><td>Function</td><td>Walking, bathing, toileting; falls in the past year</td><td>Predicts tolerance of dialysis and travel</td></tr>
<tr><td>Cognition and mood</td><td>Memory, delirium, depression</td><td>Shapes consent and self-care</td></tr>
<tr><td>Nutrition</td><td>Weight loss, appetite, teeth</td><td>Protein-energy wasting changes prognosis and diet advice</td></tr>
<tr><td>Medicines</td><td>Every tablet, including herbal and over-the-counter</td><td>Doses by kidney function; falls and bleeding risk</td></tr>
<tr><td>Social support</td><td>Who lives with the patient, who brings them to clinic, who pays</td><td>Three trips a week to a dialysis unit need a person and a fare</td></tr>
<tr><td>Goals</td><td>What matters most: time, comfort, home, family</td><td>The basis of the modality choice</td></tr>
</tbody></table></div>
{{fig:ntr21_b}}
<h3>What dialysis does and does not give the frail elder</h3>
<p>In 3,702 United States nursing home residents who started dialysis, the median score for dependence in daily activities worsened in the three months after starting. By 12 months, 58% had died and only 13% had kept their pre-dialysis level of function.[[ntr21_13]] In a single Dutch center, 311 patients aged 70 or older chose either dialysis or conservative management. Overall, median survival was longer with dialysis (3.1 versus 1.5 years from the time of choice), but among patients aged 80 or older the difference was no longer statistically significant (2.1 versus 1.4 years), and it shrank in those with heavy comorbidity.[[ntr21_14]] Both studies are observational and the groups differed; they do not prove that dialysis causes decline. They show that for some older adults, dialysis adds treatment burden without adding much time.</p>
<p>KDIGO 2024 asks you to inform people with CKD about kidney replacement options and about comprehensive conservative management, and to offer conservative management as a valid choice for people who choose not to pursue kidney replacement therapy (practice points).[[ntr21_12]] Conservative management is not &ldquo;doing nothing.&rdquo; It treats symptoms, anemia, acidosis, fluid and potassium, and plans for the end of life. Module 32 covers the conversation in depth.</p>
<p>In the Philippines the decision is usually a family decision. The eldest child, a sibling working abroad, and the lola herself may hold different views. Ask the patient first, alone if she wishes, what matters most to her. Then hold a family meeting with the attending, and write down what was decided and why.</p>
{{key:In an older adult, measure frailty and ask about goals before you discuss dialysis. Age alone tells you little; frailty and the patient&rsquo;s own priorities tell you most.}}
"""),
        ("transition", "Transition", "From pediatric to adult care: transition, not transfer", """
<p>An adolescent with CKD, a kidney transplant or a glomerular disease must move from a pediatric service, where parents managed appointments and medicines, to an adult service, where the young adult is expected to manage alone. The move happens at the age when risk-taking, school and work changes, and the wish to be like everyone else are strongest. Missed doses and missed visits around this time are a well-known cause of lost kidney function and transplant rejection.</p>
<p>The International Society of Nephrology (ISN) and the International Pediatric Nephrology Association (IPNA) published a consensus statement that frames transition as a planned, gradual process rather than a single transfer of records, with shared responsibility between pediatric and adult services.[[ntr21_9]] It is a consensus, not a graded guideline. In practice it means starting early, teaching skills step by step, and handing over when the young person is ready and clinically stable, not in the middle of a crisis.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What the young person learns</th><th>What the adult team does</th></tr></thead>
<tbody>
<tr><td>Early adolescence</td><td>Names the diagnosis and each medicine; answers some questions in clinic</td><td>Nothing yet, but the pediatric team mentions that a move will come</td></tr>
<tr><td>Middle adolescence</td><td>Refills medicines, books appointments, sees the doctor alone for part of the visit</td><td>Shares information about the adult clinic; a joint visit if possible</td></tr>
<tr><td>Late adolescence</td><td>Explains the history to a new doctor, knows what to do when sick, understands contraception and pregnancy risks with their medicines</td><td>Receives a written summary; a named person meets the young adult at the first visits</td></tr>
<tr><td>Young adulthood</td><td>Manages independently, with family support if wanted</td><td>Keeps visits frequent in the first year; follows up quickly on any missed visit</td></tr>
</tbody></table></div>
<p>The CKiD U25 equation runs to age 25, so the same estimate can follow the young adult across the move and avoid a false jump in eGFR when the adult team switches equations.[[ntr21_8]]</p>
<p>In the Philippines, transition often coincides with leaving home for college in Manila or Cebu, or with a first job. Ask where the patient will live and study, find an adult clinic near there, and check that their medicines and laboratory tests will remain affordable. A young woman on an ACE inhibitor or mycophenolate needs a private conversation about contraception and pregnancy before she leaves pediatric care.</p>
{{flow:Transition checklist for the adult team|Before the first visit::Get a written summary: diagnosis, biopsy, transplant details, medicines, allergies, recent results.|First visit::See the young adult alone for part of the visit; ask about school, work, relationships and who pays for medicines.|Medicines::Confirm doses and a refill plan the patient can afford; check that the eGFR equation is consistent.|Reproductive health::Discuss contraception and pregnancy risks with teratogenic or fetotoxic medicines.|Follow-up::Book the next visit before they leave; call if they miss it.}}
{{key:Transition is a process that starts years before the transfer. On the adult side, see the young adult alone, keep the same eGFR equation, and act quickly on the first missed visit.}}
"""),
    ],
    "debrief": ["""
<p><strong>Medicines and monitoring now.</strong> &ldquo;Continue home meds&rdquo; is wrong. Losartan carries fetal risk and should be stopped now, with blood pressure controlled by an agent the obstetrician and attending nephrologist consider safe in pregnancy; the statin is usually stopped too. She should not stop everything, as her mother suggests, because uncontrolled pressure harms both her and the baby. Discuss low-dose aspirin with the obstetrician, since kidney disease places her at high risk of preeclampsia. Agree on a joint plan with the district hospital obstetrician: blood pressure at every visit and at home, urine protein-to-creatinine ratio and creatinine at set intervals, and a clear route back to the renal clinic.</p>
""", """
<p><strong>Her risks in numbers.</strong> Explain that women with CKD have about ten times the odds of preeclampsia and about six times the odds of premature delivery compared with women without CKD, but that pregnancy has not been shown to speed up CKD on average. Use absolute terms too: in TOCOS, about one in three women with stage 1 CKD and most women with stages 4 to 5 had preterm delivery, neonatal intensive care or a small baby. Her CKD stage, proteinuria above 1 g/g and borderline pressure place her in a middle-risk group. Many women like her have a healthy baby, often delivered early, but the risks are real and need close joint care. Say this to her and her husband first, then with her mother if she wishes.</p>
""", """
<p><strong>Preeclampsia or flare at 28 weeks.</strong> New blood pressure above 140/90 mm Hg after 20 weeks with doubled proteinuria fits preeclampsia until shown otherwise; it can also coexist with an IgAN flare. Check platelets, liver enzymes, creatinine, and urine sediment. A bland sediment with falling platelets and rising liver enzymes points to preeclampsia; new dysmorphic red cells or red cell casts point to active IgAN. Ask about headache and vision. The obstetric team leads, because the treatment of severe preeclampsia is delivery; the nephrologist advises on blood pressure, kidney function and whether a flare needs treatment after delivery. If her pressure reaches 160/110 mm Hg or she has symptoms, this is an emergency.</p>
"""],
    "skills": {"title": "Pregnancy, child and older-adult adjustments",
               "intro": "Complete with a preceptor across at least two of the three patient groups, on the ward, in clinic or in simulation. Sign-off is local.",
               "items": [
                   ("States the ACOG definition of preeclampsia and its severe features, and lists the findings that separate it from active glomerular disease.", False),
                   ("Reviews a pregnant woman&rsquo;s medicine list and identifies fetotoxic or teratogenic drugs for discussion with the obstetrician.", False),
                   ("Measures a child&rsquo;s blood pressure with a correctly sized cuff and classifies it by AAP 2017 percentiles or adolescent cut points.", False),
                   ("Calculates a pediatric eGFR with the CKiD U25 equation and explains why adult equations do not apply.", False),
                   ("Completes a frailty screen and a goals conversation with an older adult with advanced CKD before dialysis is discussed.", False),
                   ("Writes a transition summary for an adolescent moving to adult care.", False),
               ],
               "placement": "Renal clinic, obstetric co-management clinic, pediatric ward or geriatric ward"},
    "quiz": [
        ("An intern sees a woman at 30 weeks of gestation with known CKD. Her blood pressure is 162/112 mm Hg and she has a headache. What should the intern do?",
         ["Recheck the blood pressure tomorrow",
          "Call the resident, the attending nephrologist and the obstetric team now; this is a severe-range pressure with a symptom",
          "Give her usual losartan",
          "Reassure her that headaches are common in pregnancy"], 1,
         "Blood pressure of 160/110 mm Hg or higher is severe range, and headache is a severe feature of preeclampsia. Restarting losartan is wrong because ACE inhibitors and ARBs carry fetal risk."),
        ("A resident is asked to interpret a creatinine of 0.9 mg/dL in a woman at 24 weeks of gestation whose prepregnancy creatinine was 0.6 mg/dL. What is the best interpretation?",
         ["Normal, because 0.9 mg/dL is within the adult reference range",
          "A rise that may reflect reduced kidney function, because GFR normally rises about 50% in pregnancy and creatinine falls",
          "A laboratory error",
          "A sign of dehydration only, requiring no follow-up"], 1,
         "Pregnancy raises GFR and lowers creatinine, so a creatinine above the prepregnancy value is abnormal even if it sits within the nonpregnant range. Calling it normal applies the wrong reference point."),
        ("An 84-year-old woman with CKD G5, frailty and dementia is referred for dialysis. Her children disagree about it. What should the fellow do?",
         ["Start dialysis because her eGFR is below 10",
          "Refuse dialysis because of her age",
          "Assess frailty, ask about her own goals as far as she can express them, and present both dialysis and comprehensive conservative management in a family meeting with the attending",
          "Let the eldest child decide alone"], 2,
         "KDIGO 2024 asks clinicians to inform people about both kidney replacement and conservative management and to offer conservative management as a valid choice. Age alone is not a reason to refuse, and the decision belongs to the patient and family with the team."),
        ("A 9-year-old boy with AKI is admitted to an adult medical ward in a provincial hospital. Which plan is safest?",
         ["Start an adult maintenance fluid at a fixed rate",
          "Use adult creatinine ranges and the adult eGFR equation",
          "Weigh him, use a pediatric eGFR equation and blood pressure percentiles, write weight-based fluids from the pediatric protocol, and call the pediatric nephrologist",
          "Wait for the creatinine to rise further before calling anyone"], 2,
         "Children need weight-based fluids, pediatric reference ranges and pediatric equations, and AKI in a child is an indication to call the pediatric nephrologist. Adult fluids at a fixed rate risk overload and hyponatremia."),
        ("A 19-year-old transplant recipient from a pediatric program misses his first two adult clinic visits after moving to Manila for college. What should the adult team do?",
         ["Discharge him from the clinic for nonattendance",
          "Wait until he returns on his own",
          "Contact him promptly, find out what stopped him, check his medicine supply and tacrolimus levels, and arrange a visit he can reach",
          "Ask the pediatric team to take him back permanently"], 2,
         "The period around transfer carries high risk of missed doses and rejection. The ISN&ndash;IPNA consensus frames transition as a shared, planned process; acting quickly on missed visits is part of it."),
    ],
    "terms": [
        ("AAP", "American Academy of Pediatrics"),
        ("ACE", "Angiotensin-converting enzyme"),
        ("ACOG", "American College of Obstetricians and Gynecologists"),
        ("AKI", "Acute kidney injury"),
        ("ARB", "Angiotensin receptor blocker"),
        ("CKD", "Chronic kidney disease"),
        ("CKiD U25", "Chronic Kidney Disease in Children under-25 (equation)"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("GFR", "Glomerular filtration rate"),
        ("HELLP", "Hemolysis, elevated liver enzymes and low platelets"),
        ("IgAN", "Immunoglobulin A nephropathy"),
        ("IPNA", "International Pediatric Nephrology Association"),
        ("ISN", "International Society of Nephrology"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("TOCOS", "Torino-Cagliari Observational Study"),
    ],
    "readings": [
        ("ckd-and-pregnancy.html", "CKD and Pregnancy"),
        ("ckd-children-young-adults.html", "CKD in Children &amp; Young Adults"),
        ("hemodialysis-elderly.html", "Hemodialysis in Older Adults"),
        ("attending-pediatric-nephrologist-02-growing-kidney-assessment.html", "Attending Pediatric Nephrologist, Module 2: Assessing the growing kidney"),
    ],
    "calcs": ["calc-frailty-assessment.html", "calc-pediatric-egfr.html", "calc-ckid-u25-egfr.html", "calc-pediatric-bp.html",
              "calc-charlson-comorbidity.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
