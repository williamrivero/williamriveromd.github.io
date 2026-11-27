# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 22: Modality education and kidney replacement planning.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
IDEAL numbers from the PubMed abstract; KDIGO 2024 practice points 2.2.1-2.2.3, 5.3.1-5.3.2, 5.4.1-5.4.5 and
5.5.1-5.5.3 against the KDIGO summary; KDIGO 2019 controversies conference, ISPD 2020, KDOQI 2019 access and
Verberne 2016 as in the verified banks or PubMed. PhilHealth benefits named without amounts except the HD package
stated in the brief (PHP 6,350, effective October 9, 2024). No doses. Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow sits with a farmer and his wife at a kitchen table in Isabela, showing a printed chart of dialysis, transplant and conservative care, while their daughter joins by video call on a phone.",
    "objectives": [
        "<strong>Intern:</strong> Explain in plain words what hemodialysis, peritoneal dialysis, transplantation and conservative care involve, check understanding with teach-back, and record what the patient and family understood and asked.",
        "<strong>Resident:</strong> Time preparation for kidney replacement therapy (KRT) by risk and symptoms, using the Kidney Failure Risk Equation (KFRE) and the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 practice points, and start the practical steps: access referral, vein preservation, transplant referral and benefit registration.",
        "<strong>Fellow:</strong> Lead a shared modality decision that includes transplantation and comprehensive conservative management, with the family present, the evidence on timing stated honestly, and the patient&rsquo;s goals at the center.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the patient who is approaching kidney failure</span>The <strong>intern</strong> explains the options in plain Tagalog, Ilocano or English, uses teach-back, and writes down what the patient understood and what she fears. The <strong>resident</strong> notices that the risk of kidney failure is high months before the symptoms come, and starts the slow steps early: access, vaccinations, transplant referral, PhilHealth registration. The <strong>fellow</strong> runs the family meeting, lays out every option including transplant and conservative care, and helps the patient choose by what matters to her, not by what the unit is used to.</div>
{{plain:Picture a family planning to move house before the rainy season. If they start packing in March, they choose the new place, hire a truck and move on a dry day. If they wait until the roof leaks in August, they move at night in the rain, into whatever room is free. Kidney failure is the rainy season. The emergency catheter at 2 a.m. is the night move.}}
<p>The picture has a limit. A family knows when the rains come. Kidney decline is less predictable: some patients lose function steadily, some plateau for years, and some die of heart disease before they ever need dialysis. That is why planning is driven by an estimate of risk, not by a calendar, and why preparation that turns out not to be needed is not wasted. The other limit is that the move itself is a choice. Dialysis, transplantation and conservative care each suit different people, and the right one depends on the person&rsquo;s body, home, work, family and goals as much as on her creatinine.</p>
{{cards:Key numbers|Refer to nephrology (KDIGO 2024)::5-year kidney failure risk of 3% to 5% by KFRE (practice point)|Multidisciplinary care (KDIGO 2024)::2-year risk above 10% (practice point)|Modality education and preparation (KDIGO 2024)::2-year risk above 40%, or GFR below about 15 to 20 mL/min/1.73 m&sup2; (practice points)|When dialysis usually starts (KDIGO 2024)::For symptoms or signs, often but not always at GFR 5 to 10 mL/min/1.73 m&sup2; (practice point)|IDEAL trial, 828 adults::Death 37.6% with early start versus 36.6% with late start (HR 1.04)|PhilHealth hemodialysis::Up to 156 sessions a year at PHP 6,350 per session for PDD-registered patients (confirm on date of service)}}
<p>Most patients who reach kidney failure have been known to a doctor for years. A few arrive for the first time in the emergency room. Your work is to make the first group&rsquo;s start planned, chosen and safe; to start dialysis for symptoms and signs rather than for a number; and to make sure every patient hears about all the options, including the ones your hospital does not offer.</p>
""",
    "case": {"title": "The kitchen table in Isabela", "html": """
<p>Wednesday, 3 p.m., the renal clinic of a provincial hospital in Ilagan, Isabela. Mrs. Rosario Dela Cruz, 56, lives with her husband, a rice farmer, in a barangay 40 minutes away by tricycle. She has had type 2 diabetes for eighteen years and chronic kidney disease (CKD) from diabetic kidney disease. Her estimated glomerular filtration rate (eGFR) has fallen from 19 to 11 mL/min/1.73 m&sup2; over a year, and her urine albumin-to-creatinine ratio is 1,800 mg/g. The KFRE gives a 2-year risk of kidney failure of about 60%. She feels more tired than last year but eats well, sleeps well, and has no itch, nausea or swelling. Potassium is 5.4 mmol/L, bicarbonate 19 mmol/L, blood pressure 138/82 mm Hg. Diabetic retinopathy has reduced her vision; she reads large print with glasses.</p>
<p>Their concrete house has a spare room and a deep well. Her son and his family live next door. Her daughter, a domestic worker in Hong Kong, joins by video call and says her mother should &ldquo;have the best, the dialysis in Manila.&rdquo; The resident, Dr. Jerome Pascual, has written: &ldquo;eGFR 11. For temporary catheter insertion and hemodialysis next week.&rdquo;</p>
""", "questions": ["Does Mrs. Dela Cruz need dialysis next week, and what should decide when she starts?",
                  "How would you present her options, and which of them fit her life?",
                  "What should be done this month so that, whenever she starts, the start is planned?"]},
    "sections": [
        ("when-start", "When to start", "When to start: symptoms and signs, not a single number", """
<p>For decades, many units started dialysis at a set level of kidney function, and the trend worldwide was to start earlier. The reasoning seemed sound: uremic toxins accumulate, so why wait? The answer came from a randomized trial.</p>
<p>IDEAL randomized 828 adults with progressive CKD at 32 centers in Australia and New Zealand to planned dialysis start at an estimated GFR of 10.0 to 14.0 mL/min (early) or 5.0 to 7.0 mL/min (late), estimated by the Cockcroft&ndash;Gault equation. The early group started a median of 1.8 months after randomization, the late group 7.4 months. Over a median of 3.6 years, 37.6% of the early group and 36.6% of the late group died (hazard ratio [HR] 1.04, 95% confidence interval 0.83 to 1.30), and cardiovascular events, infections and dialysis complications did not differ. Of the late group, 75.9% started above the 7.0 mL/min target because symptoms appeared.[[ntr22_2]]</p>
<p>Read IDEAL in two ways. It shows that starting early, by a number, does not help survival. It also shows that most patients assigned to wait developed symptoms and started a little earlier than planned. The lesson is to watch closely and start for the right reasons, not to delay at all costs.</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2024 practice point</th><th>What it means for your plan</th></tr></thead>
<tbody>
<tr><td>Decide on starting by weighing symptoms, signs, quality of life, preferences, GFR and laboratory abnormalities together</td><td>A single eGFR value never decides alone</td></tr>
<tr><td>Start dialysis for one or more indications: symptoms of kidney failure, inability to control volume or blood pressure, nutritional decline or cognitive impairment not responding to diet; this often but not invariably occurs at GFR 5 to 10 mL/min/1.73 m&sup2;</td><td>Ask about appetite, nausea, itch, sleep, concentration, weight and breathlessness at every visit</td></tr>
<tr><td>Plan preemptive transplantation or dialysis access when GFR falls below about 15 to 20 mL/min/1.73 m&sup2;, or when the 2-year KRT risk is above 40%</td><td>Preparation starts months before the start</td></tr>
</tbody></table></div>
<p>The practice points are from the KDIGO 2024 CKD guideline.[[ntr22_1]] They are practice points, which KDIGO uses for advice not backed by a systematic evidence review, so they carry no grade.</p>
<h3>Predicting the rainy season: the KFRE</h3>
<p>The KFRE uses age, sex, eGFR and urine albumin-to-creatinine ratio to estimate the 2-year and 5-year risk of needing dialysis or a transplant. A multinational meta-analysis of cohorts across many countries confirmed that it predicts accurately, with recalibration needed in some regions.[[ntr22_3]] KDIGO 2024 uses it at three thresholds: a 5-year risk of 3% to 5% to refer to nephrology, a 2-year risk above 10% to begin multidisciplinary care, and a 2-year risk above 40% to begin modality education and preparation, each in addition to eGFR-based criteria (practice points).[[ntr22_1]] The KFRE predicts kidney failure, not death. In an older or very sick patient, death from heart disease may come first, which is one reason the conversation must include conservative care.</p>
{{fig:ntr22_b}}
<p>In many Philippine hospitals, patients still start dialysis in the emergency room, through a temporary catheter, often after years of clinic visits where no one began the preparation. Each of those starts is a planning failure that the resident can prevent.</p>
{{call:Stop and call the attending nephrologist for an urgent start when a patient with advanced CKD has <ul><li>potassium that is high with electrocardiogram changes or does not respond to treatment;</li><li>pulmonary edema or fluid overload not responding to diuretics;</li><li>severe metabolic acidosis;</li><li>pericardial rub or effusion, encephalopathy, seizures or uremic bleeding.</li></ul>Do this per unit protocol, but always ask the attending nephrologist for guidance.}}
{{key:Start dialysis for symptoms and signs, not for a number. Start preparing when the 2-year KFRE risk passes 40% or the eGFR falls below about 15 to 20, whichever comes first.}}
"""),
        ("options", "The options", "The options: what each one asks of the patient and family", """
<p>Every patient approaching kidney failure should hear about four paths. KDIGO 2024 asks that people with CKD be informed about all kidney replacement options and about comprehensive conservative management (practice point).[[ntr22_1]] The KDIGO controversies conference on dialysis initiation called for moving away from a one-size-fits-all approach toward care built on each patient&rsquo;s goals and preferences, within quality and safety standards.[[ntr22_4]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>What it involves</th><th>What it asks of the patient and family</th><th>Philippine coverage and access</th></tr></thead>
<tbody>
<tr><td>In-center hemodialysis (HD)</td><td>Usually three sessions a week of about four hours, through a fistula, graft or catheter</td><td>Travel three times a week, time away from work or farm, a companion for some patients</td><td>PhilHealth covers up to 156 sessions a year for patients in the PhilHealth Dialysis Database (PDD); transport and take-home medicines are not covered</td></tr>
<tr><td>Peritoneal dialysis (PD)</td><td>Exchanges at home through a catheter in the abdomen, by hand several times a day or by machine overnight</td><td>A clean space for supplies, hand hygiene, training, vision and dexterity or a trained helper</td><td>PhilHealth Z benefit package for PD; supply delivery depends on the provider and location</td></tr>
<tr><td>Kidney transplantation</td><td>A kidney from a living or deceased donor, with lifelong immunosuppression</td><td>Evaluation tests, a suitable donor, travel to a transplant center, adherence for life</td><td>Concentrated in a few centers; PhilHealth transplant benefits exist, and the 2026 revision should be confirmed before quoting amounts</td></tr>
<tr><td>Comprehensive conservative management</td><td>No dialysis; active treatment of symptoms, anemia, acidosis, fluid and potassium; planning for the end of life</td><td>Regular visits, honest conversations about prognosis, home or hospice support</td><td>Clinic visits and medicines are mostly out of pocket; palliative services are limited outside cities</td></tr>
</tbody></table></div>
<p>The hemodialysis package of PHP 6,350 per session took effect on October 9, 2024, under the circular that institutionalized 156 sessions a year.[[ntr22_5]] The PD benefit is a separate Z benefit package.[[ntr22_6]] Confirm current rules and amounts on the date of service, and never let the size of a benefit choose the modality for the patient.</p>
<h3>What the evidence can and cannot tell you</h3>
<p>No large trial has randomized patients between hemodialysis and peritoneal dialysis; observational comparisons are confounded by who chooses which. In practice, the two give broadly similar outcomes for patients who can do either, and PD often preserves residual kidney function and daily freedom. The International Society for Peritoneal Dialysis (ISPD) recommends that PD be prescribed in a goal-directed way, agreed with the patient, to support the life the patient wants to live.[[ntr22_7]]</p>
<p>For older adults, conservative management is a real choice. In a Dutch single-center cohort of 311 patients aged 70 or older, dialysis was associated with longer survival overall, but among those 80 or older the difference was no longer statistically significant, and it shrank with heavy comorbidity.[[ntr22_8]] This was observational and the groups differed in age. KDIGO 2024 asks that conservative management be offered as a valid option to people who choose not to have kidney replacement therapy (practice point).[[ntr22_1]]</p>
<p>Transplantation, for those who can receive it, usually offers the most life and the most freedom. Ask early whether the patient has a willing, healthy relative. In the Philippines that relative may be working overseas, which affects timing and testing, and the law and the transplant center&rsquo;s ethics committee govern who may donate.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>For a child with progressive kidney failure, KDIGO 2024 calls preemptive transplantation from a living or deceased donor the preferred treatment, usually timed at an eGFR of about 5 to 15 mL/min/1.73 m&sup2; depending on age, size and rate of progression, and it adds poor growth despite optimized care as an indication to start KRT (practice points).[[ntr22_1]] PD at home is often the first dialysis option for small children because it suits their size and lets them stay in school. See <a href="attending-pediatric-nephrologist-19-choosing-krt.html">Attending Pediatric Nephrologist, Module 19</a>.</div>
{{key:Present all four paths to every patient: hemodialysis, peritoneal dialysis, transplantation and conservative care, whether or not your hospital offers them. Leaving one out is a decision made for the patient.}}
"""),
        ("shared-decision", "Shared decision", "The shared decision: from teach-back to the family meeting", """
<p>A modality choice is a decision with no single right answer. The person who will live with it should make it, with the information, time and support to choose well. KDIGO 2024 asks the multidisciplinary team to provide education and counseling about KRT options, transplantation, access surgery, and the ethical, psychological and social issues, and to include care partners where appropriate (practice points).[[ntr22_1]]</p>
<h3>The intern&rsquo;s part: plain words and teach-back</h3>
<p>Teach-back means asking the patient to explain, in her own words, what she has understood, then correcting and asking again. It tests your explanation, not the patient. Say: &ldquo;I want to be sure I explained it well. Can you tell me how peritoneal dialysis is done at home?&rdquo; Write down the answer, the questions, and the fears. A patient who says &ldquo;once you start dialysis you die soon&rdquo; is telling you what she has seen in her barangay; address it gently with facts.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What to do</th><th>Words that help</th></tr></thead>
<tbody>
<tr><td>Make the choice visible</td><td>Say there is a decision to make and more than one good answer</td><td>&ldquo;There are several ways to care for your kidneys from here. We will choose together.&rdquo;</td></tr>
<tr><td>Explain each option</td><td>Use a printed chart or decision aid in her language; include benefits, burdens and costs</td><td>&ldquo;This one is done at home every day. This one means traveling to the unit three times a week.&rdquo;</td></tr>
<tr><td>Ask what matters</td><td>Work, farm, grandchildren, travel, independence, faith, money, comfort</td><td>&ldquo;What would a good day look like for you a year from now?&rdquo;</td></tr>
<tr><td>Check understanding</td><td>Teach-back</td><td>&ldquo;Can you tell me in your own words what we discussed?&rdquo;</td></tr>
<tr><td>Decide, or decide when</td><td>Allow time; a decision can be revisited</td><td>&ldquo;You do not have to decide today. Let us meet again in two weeks with your family.&rdquo;</td></tr>
</tbody></table></div>
<h3>The fellow&rsquo;s part: the family meeting</h3>
<p>In the Philippines a modality decision is almost always a family decision. The spouse, the eldest child, a sibling abroad, and sometimes a parish priest or pastor may all have a voice. Plan the meeting: book a quiet room, invite those the patient wants, connect the relative abroad by video at a time that suits both time zones, and bring a nurse or social worker.</p>
<p>Start by asking the patient, alone first if she wishes, what she wants the family to know. In the meeting, describe her kidney function and her risk simply, present every option, and invite questions from each person. When a relative abroad pushes for &ldquo;the best,&rdquo; help the family see that the best is the option that fits the patient&rsquo;s body and life, not the most expensive or the most distant. Name the burden on the family member who will do the daily work, whether that is driving to the unit or helping with exchanges.</p>
{{fig:ntr22_a}}
<p>Home factors decide much of PD&rsquo;s feasibility: a clean room or corner for supplies, clean water for hand washing, a place to store boxes, and either good vision and hand function or a trained helper. Visual impairment from retinopathy does not rule out PD; many patients succeed with large-print guides, assisted exchanges or a family helper. A nurse home visit, where available, answers these questions better than a clinic interview.</p>
{{key:Let the patient choose what fits her life. Ask what a good day looks like for her, test your explanation with teach-back, and bring the family in on her terms.}}
"""),
        ("preparation", "Preparation", "Preparation: access, transplant referral, vaccines and paperwork", """
<p>Preparation takes months, and every step has a lead time. An arteriovenous fistula needs weeks to months to mature. A PD catheter needs time to heal before full use. Transplant evaluation needs tests, specialist visits and donor work-up. Benefit registration needs documents. That is why KDIGO 2024 ties preparation to a 2-year risk above 40% or a GFR below about 15 to 20, not to the day dialysis starts.[[ntr22_1]]</p>
<h3>Access and the life-plan</h3>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 vascular access guideline asks the team to build an end-stage kidney disease (ESKD) Life-Plan: a long-term plan for the sequence of modalities and accesses a patient may need over a lifetime, chosen with the patient, rather than a reflex fistula for everyone.[[ntr22_9]] For a patient choosing hemodialysis, that usually means referral to a vascular surgeon in time for a fistula to mature. For a patient choosing PD, it means a catheter placed by a trained operator with time to heal. For a patient waiting for a preemptive transplant, it may mean preserving veins and planning a backup.</p>
<p>Vein preservation is everyone&rsquo;s job, and the intern can do it today. In any patient with advanced CKD, protect the veins of the arm most likely to carry a future fistula: draw blood and place intravenous lines on the back of the hand or the other arm when possible, avoid peripherally inserted central catheters unless the attending agrees, and write &ldquo;protect veins&rdquo; on the chart and the bed.</p>
<h3>The preparation checklist</h3>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Who leads</th><th>Why it cannot wait</th></tr></thead>
<tbody>
<tr><td>Modality education and family meeting</td><td>Fellow and nurse educator</td><td>The choice decides every later step</td></tr>
<tr><td>Access referral (fistula or PD catheter)</td><td>Resident with the attending</td><td>Maturation and healing take weeks to months</td></tr>
<tr><td>Transplant referral and donor discussion</td><td>Fellow with the transplant center</td><td>Evaluation is long; preemptive transplant is best for suitable patients</td></tr>
<tr><td>Hepatitis B serology and vaccination</td><td>Resident</td><td>Dialysis units require serology, and vaccination takes months to complete</td></tr>
<tr><td>Hepatitis C and human immunodeficiency virus (HIV) screening as the unit requires</td><td>Resident</td><td>Determines machine and room assignment in the unit</td></tr>
<tr><td>PhilHealth membership and PDD registration</td><td>Social worker with the unit</td><td>The hemodialysis benefit applies to patients registered in the PDD</td></tr>
<tr><td>Transport, work and family plan</td><td>Social worker, patient, family</td><td>Three trips a week or daily exchanges change a household&rsquo;s routine and income</td></tr>
<tr><td>Medicines, anemia, acidosis, potassium, diet</td><td>Resident and dietitian</td><td>A well-prepared body tolerates the start better</td></tr>
</tbody></table></div>
<p>The PDD requirement and the 156-session coverage come from the PhilHealth circular.[[ntr22_5]] Ask the social worker to start PhilHealth paperwork when preparation starts, not when the first session is booked. Explore Malasakit Center assistance for costs outside the packages.</p>
{{flow:From high risk to a planned start|KFRE 2-year risk above 10%::Multidisciplinary CKD care: diet, medicines, anemia, bone, blood pressure.|KFRE 2-year risk above 40% or eGFR below about 15 to 20::Modality education, family meeting, vein preservation, hepatitis B vaccination, transplant referral.|Choice made::Access referral for the chosen modality; PhilHealth and PDD paperwork; transport plan.|Watch closely::Symptoms, nutrition, volume, potassium, acidosis at every visit; KFRE and eGFR trend.|Planned start::Begin dialysis for symptoms or signs, on a working access, on a day chosen in advance. Or continue conservative care if that is the choice.}}
<p>If the patient chooses conservative management, the preparation is different but just as real: a symptom plan, advance care planning, and a clear route to help at home. KDIGO 2024 asks that people with a recognized need for end-of-life care, including those on conservative management, have access to advance care planning resources (practice point).[[ntr22_1]] The KDIGO conference on supportive care describes this as part of kidney care, not a separate service.[[ntr22_10]]</p>
{{key:Start every preparation step when the 2-year risk passes 40%: the conversation, the access, the transplant referral, the vaccine and the paperwork. A planned start is built months before the first session.}}
"""),
    ],
    "debrief": ["""
<p><strong>Not next week.</strong> An eGFR of 11 alone is not a reason to start. Mrs. Dela Cruz eats and sleeps well, has no uremic symptoms, no fluid overload, controlled blood pressure, and a manageable potassium and bicarbonate. IDEAL showed no survival benefit from starting early by a number, and KDIGO 2024 asks that the start be decided by symptoms, signs and preferences, often at a GFR of 5 to 10. Her 2-year KFRE risk of about 60% and eGFR below 15 do mean preparation should begin now. A temporary catheter next week would expose her to infection and to a crash-like start she does not need. Treat her acidosis and potassium, review her diet, and see her often.</p>
""", """
<p><strong>The options.</strong> Present all four. In-center hemodialysis in Ilagan means three tricycle trips of 40 minutes each way every week; PhilHealth covers the sessions once she is registered in the PDD, but not the fares. PD at home suits her spare room and her son&rsquo;s family next door; her reduced vision is a challenge, not a bar, if a family member trains as her helper. Ask whether a healthy relative might donate a kidney and whether she wants a transplant evaluation. Conservative management should be mentioned as a valid choice, even if she is unlikely to choose it at 56. Ask her what a good day looks like a year from now. Hold a family meeting with her daughter on video at a time that suits Hong Kong, and gently explain that the best treatment is the one that fits her mother&rsquo;s life.</p>
""", """
<p><strong>This month.</strong> Write &ldquo;protect veins&rdquo; on her chart and use the back of the hand for blood draws. Check hepatitis B serology and start vaccination if she is not immune; screen as the unit requires. Ask the social worker to begin PhilHealth and PDD paperwork and to look at transport support. Once she chooses, refer for a fistula or a PD catheter in time to mature or heal. If a relative may donate, refer both to the transplant center. Record the education given and her teach-back. Agree on how often she will be seen and which symptoms should bring her in sooner.</p>
"""],
    "skills": {"title": "Modality education and preparation",
               "intro": "Complete with a preceptor on two patients with advanced CKD approaching kidney failure. Sign-off is local.",
               "items": [
                   ("Explains hemodialysis, peritoneal dialysis, transplantation and conservative management in plain language and confirms understanding with teach-back.", False),
                   ("Calculates the 2-year and 5-year KFRE and states the KDIGO 2024 practice point each result triggers.", False),
                   ("Distinguishes indications to start dialysis from a low eGFR alone, citing IDEAL.", False),
                   ("Completes a preparation checklist: vein preservation, hepatitis B status, access referral, transplant discussion and PDD registration.", False),
                   ("Plans or takes part in a family meeting, including a relative abroad by video, and documents the decision and the reasons.", False),
               ],
               "placement": "CKD clinic, renal ward or dialysis unit"},
    "quiz": [
        ("An intern has explained peritoneal dialysis to a patient. What is the best way to check that the explanation worked?",
         ["Ask &ldquo;Do you understand?&rdquo;",
          "Ask the patient to explain in her own words how the exchanges are done at home, then correct and repeat",
          "Give her a leaflet and end the visit",
          "Ask her daughter whether her mother understood"], 1,
         "Teach-back tests the explanation by asking the patient to restate it. &ldquo;Do you understand?&rdquo; usually gets a polite yes that hides confusion."),
        ("A man with CKD G4 has a 2-year KFRE risk of 45% and an eGFR of 18 mL/min/1.73 m&sup2;. He has no symptoms. What does KDIGO 2024 advise?",
         ["Start dialysis now",
          "Wait until eGFR is below 10 before discussing anything",
          "Begin modality education and preparation, including access planning and transplant referral (practice point)",
          "Refer to nephrology only if the 5-year risk exceeds 50%"], 2,
         "A 2-year risk above 40% is the KDIGO 2024 practice-point threshold for modality education and preparation. Starting dialysis now ignores the absence of symptoms; waiting until eGFR is below 10 leaves no time to prepare."),
        ("A fellow is asked what the IDEAL trial showed. Which answer is most accurate?",
         ["Early start at eGFR 10 to 14 improved survival",
          "Planned early start did not improve survival compared with planned late start (37.6% versus 36.6% deaths), and most of the late group started earlier than planned because of symptoms",
          "Late start increased cardiovascular events",
          "IDEAL compared hemodialysis with peritoneal dialysis"], 1,
         "IDEAL found no survival or adverse-event difference (HR 1.04), and 75.9% of the late-start group began above the target because of symptoms. It supports starting for symptoms and close monitoring, not delay at all costs."),
        ("A 72-year-old retired teacher in Leyte with CKD G5 and severe heart failure says she does not want dialysis. Her son insists. What should the fellow do?",
         ["Start dialysis because her son wants it",
          "Discharge her from the renal clinic",
          "Explore her reasons and goals, explain comprehensive conservative management as a valid option alongside dialysis, and hold a family meeting with the attending",
          "Tell her conservative management means no further treatment"], 2,
         "KDIGO 2024 asks clinicians to offer conservative management as a valid choice for those who decline KRT, and conservative management actively treats symptoms. Discharging her or overriding her choice are both wrong."),
        ("A woman with CKD G5 choosing hemodialysis needs blood tests on the ward. Her non-dominant left arm has good forearm veins. What should the intern do?",
         ["Draw blood from the left forearm because the veins are best",
          "Place a peripherally inserted central catheter in the left arm for convenience",
          "Protect the left arm veins: use the back of the hand or the other arm, and mark the chart &ldquo;protect veins&rdquo;",
          "Avoid all blood tests until the fistula is made"], 2,
         "The arm most likely to carry a future fistula must be protected; repeated punctures and central lines damage the veins needed for access. Avoiding all tests is unsafe."),
    ],
    "terms": [
        ("CKD", "Chronic kidney disease"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("ESKD", "End-stage kidney disease"),
        ("GFR", "Glomerular filtration rate"),
        ("HD", "Hemodialysis"),
        ("HIV", "Human immunodeficiency virus"),
        ("HR", "Hazard ratio"),
        ("IDEAL", "Initiating Dialysis Early and Late (trial)"),
        ("ISPD", "International Society for Peritoneal Dialysis"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("KDOQI", "Kidney Disease Outcomes Quality Initiative"),
        ("KFRE", "Kidney Failure Risk Equation"),
        ("KRT", "Kidney replacement therapy"),
        ("PD", "Peritoneal dialysis"),
        ("PDD", "PhilHealth Dialysis Database"),
    ],
    "readings": [
        ("when-should-dialysis-start.html", "When Should Dialysis Start?"),
        ("peritoneal-dialysis-ckd.html", "Peritoneal Dialysis"),
        ("attending-nephrologist-13-kidney-failure-planning.html", "Attending Nephrologist, Module 13: Kidney failure planning"),
        ("attending-nephrologist-20-conservative-care.html", "Attending Nephrologist, Module 20: Conservative care"),
    ],
    "calcs": ["calc-kfre.html", "calc-starting-dialysis-planner.html", "calc-pediatric-ckd-krt-risk.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
