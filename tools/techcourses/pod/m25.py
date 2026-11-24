# -*- coding: utf-8 -*-
"""Physician on Duty, Module 25: Special Patients: Frailty, Complex Illness, and Pregnancy.
Written for this series from published sources."""

MODULE = {
    "image_alt": "An elderly Filipino woman with a cane being helped to stand from the dialysis chair by a nurse, while the physician on duty checks her standing blood pressure and her daughter stands beside them.",
    "objectives": [
        "Recognize frailty, fall risk, cognitive impairment, and polypharmacy at the chair, using the Clinical Frailty Scale and a fall-risk screen.",
        "Change your approach to a session for heart failure, liver disease, cancer, and lupus or other immune disease, and know which changes belong to the nephrologist.",
        "Adapt goals for the older or frail patient and open, without leading, a conversation about what matters most to the patient.",
        "Support the adolescent or young adult who is moving into an adult unit.",
        "Explain how kidney failure affects periods, fertility, and sexual function, and outline advice on contraception.",
        "Recognize possible pregnancy in a dialysis patient, act the same day, explain why dialysis is intensified, and name the drug classes to stop or switch, per the attending nephrologist and obstetrician.",
    ],
    "big": """
{{plain:Picture a jeepney on its usual route. Most passengers ride without trouble. A few need the driver to slow at every bump: an old man with a cane, a pregnant woman, a passenger who is already sick. The jeepney is the same; the ride has to change.}}
<p>The picture has a limit. A passenger&rsquo;s needs are visible, and a dialysis patient&rsquo;s often are not. Frailty is rarely charted. Heart failure narrows the margin for fluid removal without outward sign. A pregnancy can go unrecognized for months. You find these patients only if you look.</p>
{{cards:Key terms for this module|Frailty::A state of low physiologic reserve, in which a small stress causes a large loss of function.|Clinical Frailty Scale (CFS)::A one-number rating of fitness and frailty, scored from what the patient can do. The original had 7 levels; the later version has 9.|Orthostatic hypotension::A fall in blood pressure on standing, which can cause dizziness and falls.|Polypharmacy::The use of many medicines at once, with rising risk of interactions, errors, and side effects.|Pill burden::The number of tablets and capsules a patient swallows each day.|Human chorionic gonadotropin (hCG)::A hormone made by the placenta. Blood and urine tests for pregnancy detect it.|Intensified hemodialysis::Longer or more frequent sessions than the standard schedule, prescribed by the nephrologist.}}
<p>Most of your patients fit the standard session. A few need it run differently, and the stakes are high: a fall after dialysis, a heart that cannot tolerate fast fluid removal, a pregnancy that needs more dialysis now. Your work is to notice these patients early, do what your unit&rsquo;s protocol allows, and bring each one to the attending nephrologist with the right facts.</p>
""",
    "case": {"title": "Eighty-two, three falls this month", "html": """
<p>Mrs. Remedios Santiago, 82, a retired schoolteacher, has dialyzed for four years through a left arm fistula. She has heart failure with a weak pumping heart and type 2 diabetes. Her daughter, Ms. Liza Santiago, says she fell three times this month, twice in the evening after dialysis. She now needs help to bathe and has stopped cooking.</p>
<p>She takes 14 different medicines (illustrative), including a sleeping pill prescribed by another doctor. Today she arrived 1.2 kilograms (illustrative) above her target weight. At the end of the session, the nurse, Ms. Josephine Aquino, reports her blood pressure: 96/58 mm Hg sitting and 82/50 mm Hg standing. Ms. Aquino adds that Mrs. Santiago &ldquo;seems more forgetful lately.&rdquo; The daughter asks you quietly whether dialysis is &ldquo;still helping her.&rdquo;</p>
""", "questions": ["Is it safe to send her home now, and what do you do before she stands to leave?",
                  "How frail is she, and which of her fall risks can be changed?",
                  "What will you tell the attending nephrologist, and how do you answer the daughter&rsquo;s question without making a decision that is not yours?"]},
    "sections": [
        ("complex", "Complex illness", "Complex illness: what changes in the session", """
<p>The machine is the same; the passenger is different. The second disease changes how much fluid the heart can lose, how easily the patient bleeds, and what a change in behavior means. Module 4 covers the underlying physiology. This section asks what you will see differently in the chair.</p>
<h3>Heart failure: the narrow margin</h3>
<p>A healthy heart pumps more when it is filled more, across a wide range. This is the Frank-Starling relation. A failing heart sits on a lower, flatter curve. It needs enough filling to keep its output, yet a little extra fluid backs up into the lungs. The band between too full and too empty is narrow.</p>
{{fig:pod25_hf_margin}}
<p>Fluid removal moves the patient across that band, sometimes within minutes. A stiff, thick heart behaves the same way. Medicines that slow the heart or relax the vessels blunt the defenses Module 13 described.</p>
<p>The evidence is thin. The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference on heart failure in chronic kidney disease (CKD) discussed reduced and preserved ejection fraction in dialysis patients and identified gaps in trial evidence, so many choices rest on extrapolation.[[house2019]] It is a conference report, not a graded recommendation.</p>
{{fig:idh|Low blood pressure during dialysis. Frail patients and patients with heart failure are the group at highest risk.}}
<h3>Liver disease, cancer, and lupus</h3>
<p>No dialysis-specific trials guide the session for these patients. What follows is physiology and standard-text practice, a list of what to watch, not a protocol.[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Second disease</th><th>What changes in the body</th><th>What you may see in the chair</th><th>Who decides the change</th></tr></thead>
<tbody>
<tr><td>Heart failure</td><td>Narrow band between congestion and low output. Medicines that blunt the heart rate response</td><td>Breathlessness before the session, low pressure during it, arrhythmia</td><td>Nephrologist, with the cardiologist: dry weight, fluid goal, session length</td></tr>
<tr><td>Cirrhosis of the liver</td><td>Low albumin slows refilling. Fluid in the abdomen (ascites). Low clotting factors and platelets</td><td>Early low pressure, bleeding at needle sites, confusion from liver failure (hepatic encephalopathy) that looks like uremia</td><td>Nephrologist: heparin and fluid goal</td></tr>
<tr><td>Cancer</td><td>Chemotherapy, rapid tumor cell breakdown (tumor lysis), high calcium, low white cells</td><td>Fever with a catheter, high potassium, confusion from high calcium, bleeding when platelets are low</td><td>Nephrologist with the oncologist: timing of chemotherapy around sessions</td></tr>
<tr><td>Lupus or other immune disease</td><td>Immune-suppressing medicines. Inflammation of the lining of the heart or lungs (serositis). In some patients, partial return of kidney function</td><td>Fever and infection with few signs, chest pain that changes with breathing, rising urine output</td><td>Nephrologist with the rheumatologist: immune medicines, testing for recovery</td></tr>
<tr><td>Frailty or pregnancy</td><td>Little reserve, or a second circulation</td><td>Falls after the session; missed periods and nausea</td><td>Sections 2 to 8</td></tr>
</tbody></table></div>
<h3>What you do</h3>
<p>Read the problem list before the first patient arrives. Ask the attending nephrologist for a written plan for each of these patients before you need it. Escalate early; these patients have less time between warning and harm.</p>
{{key:For the complex patient, know the second disease before you start the machine.}}
"""),
        ("frailty", "Frailty", "Frailty: the patient who has no reserve", """
<p>Picture a household with no savings. One hospital bill and the family is in debt. A frail patient tolerates an ordinary session, but one extra stress, such as a large fluid goal or a new medicine, tips her into a fall, confusion, or a hospital stay.</p>
<p>The picture has a limit. Reserve is lost in several systems at once. Muscle wastes, as Module 23 describes. Inflammation, anemia, inactivity, and the repeated stress of each session add to it. The result is a patient who looks stable in the chair and fails at the door.</p>
<h3>How common, and what it is associated with</h3>
<p>In 2,275 adults in a national United States dialysis cohort, 67.7% were frail by the study&rsquo;s definition. Frailty was associated with death (adjusted hazard ratio 2.24) and with death or hospitalization.[[johansen2007]] A meta-analysis pooled the prevalence in hemodialysis at 34.3%, ranging from 6% to 82% across studies.[[zhao2020]] The answer depends on the tool and the population.</p>
<p>A 2024 meta-analysis of 36 studies with 56,867 patients on maintenance hemodialysis found frailty associated with death (hazard ratio 1.97), hospitalization (odds ratio 2.47), and problems with the vascular access (hazard ratio 1.72). It was also associated with depression, falls, and fractures.[[cheng2024]] The studies were observational and gave no pooled absolute risks. Frail patients are also older and sicker, which may explain part of the association. No trial has shown that treating frailty in dialysis patients prolongs life.</p>
{{fig:pod25_frailty_signs}}
<h3>The Clinical Frailty Scale</h3>
<p>Rockwood and colleagues built the Clinical Frailty Scale (CFS) in 2,305 older Canadians. The original had 7 levels. Each one-level rise was associated with a 21.2% higher risk of death over about 70 months, adjusted for age, sex, and education; the area under the curve for death at 18 months was 0.77.[[rockwood2005]]</p>
<p>Alfaadhel and colleagues asked nephrologists to score the CFS in 390 patients starting dialysis. The median score was 4. Each one-point rise was associated with higher mortality, with an adjusted hazard ratio of 1.22.[[alfaadhel2015]] The cohort was mostly white and Canadian, and the scale was scored by the treating nephrologist. It has not been validated in Filipino dialysis units.</p>
<p>The site calculator uses the later 9-level version, which adds very severely frail and terminally ill. Record which version you used.</p>
{{cards:Frailty and fall-risk screen at the chair|Clinical Frailty Scale::Score it from walking, bathing, dressing, cooking, and shopping. Record the version.|Falls::Falls, near-falls, and dizziness since the last session.|Standing pressure::Sitting and standing pressure and heart rate after the session, per protocol.|Thinking::New forgetfulness or changed behavior prompts a screen.|Medicines::Sedatives, sleeping pills, and medicines from other doctors.|Muscle::The site&rsquo;s SARC-F screen asks about strength, walking, rising, stairs, and falls.}}
{{formula:<strong>Worked example 1: scoring the Clinical Frailty Scale (illustrative).</strong><br>Facts: walks with a cane; needs help to bathe; has stopped cooking; eats and uses the toilet alone.<br>Step 1. Dependent for outside activities and housework: beyond &ldquo;mildly frail.&rdquo;<br>Step 2. Independent in eating and toileting: not &ldquo;severely frail,&rdquo; which means dependent for personal care.<br>Step 3. Best fit: &ldquo;moderately frail&rdquo; (level 6 in both versions).[[rockwood2005]]<br>In one dialysis cohort, each one-point rise carried an adjusted mortality hazard ratio of 1.22.[[alfaadhel2015]]<br><em>What it tells you:</em> she needs closer watching at the door and after any change. <em>What it does not tell you:</em> how long she will live, or whether she should continue dialysis.}}
<h3>What you do</h3>
<p>Score the CFS from how the patient walks in, how she rises, and what the family says she can do at home. Use the site&rsquo;s frailty calculator unless your unit uses another tool. Record the score and version, rescore after any hospital stay, and report a rising score to the attending nephrologist.</p>
{{key:Frailty is a description that guides your attention. It is not a prognosis for one person.}}
"""),
        ("falls", "Falls and memory", "Falls and memory", """
<p>Picture the walk from the chair to the jeepney as the most dangerous part of the session. The machine is off, the nurse has turned to the next patient, and the patient climbs a step with less blood volume than at any other time of the week.</p>
<p>The picture has a limit: the danger is not the walk but what the body brings to it. Fluid removal lowers blood volume, and an older patient&rsquo;s vessels and heart correct slowly on standing. That is post-dialysis orthostatic hypotension. Nerve damage blunts balance, poor vision hides the step, and a sedative slows reaction time. In diabetes, blood sugar can fall after the session (Module 22). One cause may not cause a fall; three together often do.</p>
<p>Falls and fractures were among the outcomes associated with frailty in the 2024 meta-analysis.[[cheng2024]]</p>
{{fig:pod11_standing|Sitting and standing pressure before the patient leaves. Module 11 describes the full check.}}
{{formula:<strong>Worked example 3: the orthostatic drop after dialysis (illustrative).</strong><br>Sitting 96/58 mm Hg; standing 82/50 mm Hg.<br>Systolic fall = 96 &minus; 82 = 14 mm Hg.<br>Diastolic fall = 58 &minus; 50 = 8 mm Hg.<br><em>What it tells you:</em> the size of the drop, read with symptoms and heart rate. <em>What it does not tell you:</em> whether she may go home. That follows your unit&rsquo;s standing-pressure definition and the Module 11 check.}}
<h3>Memory and thinking</h3>
<p>Cerebrovascular disease, diabetes, and uremia all damage thinking. Murray and colleagues tested 338 hemodialysis patients aged 55 or older in the United States. Only 12.7% had normal cognition; 36.1% had moderate and 37.3% severe impairment. Only 2.9% had a documented diagnosis.[[murray2006]] The study was cross-sectional and regional, so it cannot show whether dialysis worsens thinking. It shows that impairment is common and usually missed.</p>
<p>Impaired thinking affects medicine use and consent. A sudden change is different: it suggests delirium, an emergency with a cause to find.</p>
{{flow:Fall after dialysis|Assess for injury::Do not lift at once. Check breathing, consciousness, head, neck, hips, and access arm.|Vital signs::Pressure lying and, if safe, sitting. Heart rate and rhythm.|Glucose::Per protocol, in diabetes or new confusion.|Red flags::Head strike, anticoagulant, new confusion, cannot bear weight, painful limb.|Call::The attending nephrologist for any fall in the unit, at once for a red flag.|Document::Time, findings, actions, advice, and who escorted the patient home.}}
{{flow:First session after a hospital stay|Discharge summary::Diagnosis, procedures, and the intended plan.|Weight::Compare with the old target. Weight lost in hospital can make the old target wrong.|New medicines::Especially sedatives, antibiotics, and blood pressure medicines.|Access::Check the fistula or catheter.|Rescore frailty::Repeat the Clinical Frailty Scale.|Call::Report to the attending nephrologist before the fluid goal is set.}}
<h3>What you do</h3>
<p>Ask a frail patient about falls at every visit. Run the Module 11 standing check before discharge. Screen thinking with the site&rsquo;s cognitive screen when behavior changes, and screen for delirium when the change is new. Confirm that someone escorts a frail patient home.</p>
{{call:Stop and call the attending nephrologist for a fall, in the unit or since the last session, with head strike, anticoagulant use, new confusion, or inability to bear weight; for new or rapidly worsening confusion; and for a frail or heart-failure patient who cannot stand safely after the session. Keep the patient seated and observed while you call.}}
"""),
        ("pills", "Medicines and goals", "Too many medicines, and goals that fit the person", """
<p>Picture a weekly pill box with every compartment overflowing. Each tablet was added for a good reason by someone. No one has looked at the whole box in a year.</p>
<p>The picture has a limit. The harm is not the number alone. Many drugs are cleared by the kidney, so they build up. A sedative from one doctor, an antihistamine for itch from another, and a morning blood pressure tablet can together produce the fall that Section 3 described. Module 20 covers each drug; this section is about the whole box.</p>
{{fig:pod25_pillbox}}
<h3>What the evidence shows</h3>
<p>Chiu and colleagues counted pills in 233 patients in three United States units. The median was 19 a day, above 25 in one quarter, and about half were phosphate binders. Higher pill burden was associated with lower physical quality of life.[[chiu2009]] The study was cross-sectional; whether removing pills helps has not been tested.</p>
{{formula:<strong>Worked example 4: counting pills, not drug names (illustrative).</strong><br>14 medicines on the list.<br>Phosphate binders: 3 meals &times; 2 tablets = 6 tablets.<br>Blood pressure medicines: 4 tablets. Diabetes medicines: 2 tablets. All others: 7 tablets.<br>Total = 6 + 4 + 2 + 7 = 19 tablets per day, the median reported by Chiu and colleagues.[[chiu2009]]<br><em>What it tells you:</em> the daily load and where it comes from. <em>What it does not tell you:</em> which tablet to stop.}}
<h3>Goals that belong to the patient</h3>
<p>The KDIGO Controversies Conference on supportive care in CKD described a high burden of physical and psychosocial symptoms in people with advanced CKD, including those on dialysis, and set out a roadmap for conservative and palliative care.[[davison2015]] It is a conference roadmap, not a graded guideline.</p>
<p>The goals-of-care discussion belongs to the attending nephrologist and to Module 26. You can open the door with one question: &ldquo;What matters most to you now?&rdquo; Write the answer in the patient&rsquo;s own words.</p>
<h3>What you do</h3>
<ol>
<li>Reconcile the list using the boxes the family brings. The site&rsquo;s medicine safety checker helps.</li>
<li>Flag sedatives, anticholinergic drugs (dry mouth, confusion, constipation), new drugs, and duplicates for the nephrologist. Do not stop any yourself.</li>
<li>Record what matters most to the patient and pass it on.</li>
</ol>
{{key:For a frail patient, each pill must earn its place, and each goal must be the patient&rsquo;s own.}}
"""),
        ("young", "The young adult", "The adolescent and young adult moving to an adult unit", """
<p>Picture a student who changes schools in the middle of the year. The subjects are the same; the teachers, rules, and friends are not.</p>
<p>The picture has a limit. A school change is one event; moving from pediatric to adult kidney care is a process. In a children&rsquo;s unit, parents managed the schedule and the medicines. In an adult unit, the patient is expected to. That gap opens when school, work, and body image matter most.</p>
<h3>What the consensus says</h3>
<p>The International Society of Nephrology (ISN) and the International Pediatric Nephrology Association (IPNA) describe transfer to adult care as the end of a transition process involving both teams. They ask that it be individualized, build the young person&rsquo;s self-management skills, and assess the support around them.[[watson2011]] This is expert consensus, offered as a basis for local practice, not a graded guideline.</p>
<h3>What you may notice</h3>
<p>Missed sessions, high weight gains, and high potassium are the visible signs. Behind them are school timetables, jobs, embarrassment about the access, relationships, and conflict with parents. Missed sessions also put transplant readiness at risk (Module 27).</p>
<h3>What you do</h3>
<p>Speak to the young patient first and the parent second, and offer a private moment. Keep sessions predictable where your unit can. Report missed sessions to the attending nephrologist as facts, without blame.</p>
{{key:Talk to the young patient first, and report missed sessions without blame.}}
{{cards:How to open the conversation|Periods and contraception::&ldquo;Some women on dialysis can still become pregnant. Can I ask about your periods and whether you use contraception?&rdquo; Ask in private.|The frail patient&rsquo;s goals::&ldquo;What matters most to you now?&rdquo; Then listen. Do not offer choices you cannot promise.|The family&rsquo;s worry::&ldquo;That is a good question for the nephrologist. I will tell her you asked.&rdquo;|The young adult::&ldquo;I would like to hear from you first. May your mother join us after?&rdquo;|Missed sessions::&ldquo;You were not here on Saturday. What made it hard?&rdquo;}}
"""),
        ("hormones", "Hormones and fertility", "Hormones, fertility, and sexual function", """
<p>Picture a radio station broadcasting through heavy static. The signal arrives garbled, and sometimes it comes through clearly.</p>
<p>The picture has a limit, and the limit is the point: static does not silence the station. The hypothalamus sends pulses to the pituitary gland, which drives the ovaries or testes, which signal back up the chain. Kidney failure disturbs this chain at several steps, and the timed pulses that drive ovulation become irregular.[[daugirdas2015]]</p>
{{fig:pod25_hormone_axis}}
<p>In women, periods become irregular or stop and fertility falls, yet ovulation can still occur, especially with more intensive dialysis or after transplant. In men, testosterone falls and erectile dysfunction is common. Anemia, depression, diabetes, and medicines add to the problem.</p>
<h3>What the evidence shows</h3>
<p>Navaneethan and colleagues pooled 50 observational studies with 8,343 patients with CKD. The summary estimate of erectile dysfunction in men was 70%. Women with CKD scored lower than the general population on the Female Sexual Function Index, a validated questionnaire. Sexual dysfunction was most common in patients on dialysis.[[navaneethan2010]] The studies used different tools, few included women, and self-report carries its own bias.</p>
<p>The UK Kidney Association, then called the Renal Association, published a guideline on pregnancy and kidney disease in 2019. It recommends that advice on safe and effective contraception be offered to all women of reproductive age with CKD (Recommendation 3.1.1, grade 1D).[[wiles2019]]</p>
<h3>What you do</h3>
<p>Do not assume that a woman on dialysis cannot conceive. Ask about her periods and her contraception in private, with a female nurse present if she prefers. Ask men about sexual function in the same calm way. Refer the questions to the attending nephrologist and, where needed, to an obstetrician-gynecologist or urologist.</p>
{{key:Reduced fertility is not no fertility. A woman on dialysis can become pregnant.}}
"""),
        ("pregnancy", "Possible pregnancy", "Possible pregnancy: recognize and act the same day", """
<p>Picture a smoke detector that sometimes sounds with no fire, in a house where no one thinks to check it. The pregnancy test in kidney failure can sound without a pregnancy. More often, the diagnosis comes late because no one thought to test.</p>
<p>The picture has a limit. A false alarm costs time spent on confirmation. A missed pregnancy costs weeks of the wrong treatment.</p>
<h3>Why recognition is late</h3>
<p>Irregular periods, nausea, and weight change are common on dialysis and are also early signs of pregnancy, so everyone attributes them to the kidneys. The test can also mislead. Human chorionic gonadotropin (hCG) and its fragments are partly cleared by the kidney, so serum levels can be raised in a woman with kidney failure who is not pregnant. The evidence in dialysis is case-level: one report described a non-pregnant patient whose raised level delayed her transplant by nearly a month.[[rahbar2026]] How often this happens is unknown.</p>
<div class="table-wrap"><table>
<thead><tr><th>Why the test or the story misleads</th><th>What it means at the chair</th><th>How it is settled</th></tr></thead>
<tbody>
<tr><td>The kidney normally clears part of the hormone and its fragments</td><td>A raised serum result may not mean pregnancy. Evidence is case-level[[rahbar2026]]</td><td>Specialist interpretation, a repeat test, and pelvic ultrasound, arranged by the nephrologist and obstetrician</td></tr>
<tr><td>Missed periods are common in kidney failure</td><td>Absent periods do not exclude pregnancy</td><td>Ask, and test per your unit&rsquo;s protocol</td></tr>
<tr><td>Nausea and weight change are common on dialysis</td><td>Morning nausea or a steadily rising weight is easily blamed on the kidneys</td><td>Ask, and report the pattern</td></tr>
<tr><td>Many patients pass little or no urine</td><td>A urine test may not be possible</td><td>Serum testing with confirmation</td></tr>
</tbody></table></div>
<h3>Why dialysis is intensified</h3>
<p>A growing baby needs a steady environment. Wastes, fluid, and salt build up between sessions and fall sharply during each one. Longer, more frequent sessions keep levels lower and steadier and remove fluid more gently.</p>
<p>Hladunewich and colleagues compared 22 pregnancies in a Toronto intensive hemodialysis program with 70 in an American registry. Live births were 86.4% versus 61.4%. In women already on dialysis, median pregnancy length was 36 versus 27 weeks. Overall, live births were 48% in women dialyzed 20 hours a week or fewer and 85% in women dialyzed more than 36 hours a week.[[hladunewich2014]]</p>
<p>A systematic review by Piccoli and colleagues gathered 681 pregnancies in dialysis patients reported since 2000. In the case series, 83% of births were preterm. More weekly hours of hemodialysis were associated with fewer preterm births and fewer small-for-gestational-age infants.[[piccoli2016]]</p>
<p>Both are observational. The comparison crossed two countries, two care systems, and different eras, and the women may have differed in other ways. The dose-response pattern is consistent, but no trial has tested it.</p>
{{fig:pod25_pregnancy_dialysis}}
{{formula:<strong>Worked example 2: weekly dialysis hours (illustrative arithmetic).</strong><br>Weekly hours = sessions per week &times; hours per session.<br>Standard schedule: 3 &times; 4 = 12 hours per week.<br>An intensified schedule, for illustration only: 6 &times; 6 = 36 hours per week.<br>In the cohort comparison, live births were 48% at 20 hours a week or fewer and 85% at more than 36 hours a week, an absolute difference of 37 percentage points.[[hladunewich2014]]<br><em>What it tells you:</em> the direction and size of an association. <em>What it does not tell you:</em> the right schedule for one woman, which is the nephrologist&rsquo;s prescription.}}
<h3>What the guideline says</h3>
<p>The UK pregnancy guideline words its strong statements as &ldquo;we recommend&rdquo; (grade 1) and its conditional statements as &ldquo;we suggest&rdquo; (grade 2), with a letter from A to D that rates the evidence.[[wiles2019]]</p>
<ul>
<li>Women established on hemodialysis before pregnancy should receive long, frequent hemodialysis (Recommendation 5.2.2, grade 1C).</li>
<li>The guideline suggests prescribing the dialysis dose aiming for a pre-dialysis urea below 12.5 mmol/L, about 35 mg/dL as blood urea nitrogen (5.2.3, grade 2C).</li>
<li>Women with CKD who are pregnant or planning pregnancy should be advised by a multidisciplinary team that includes an obstetrician and a nephrologist (1.1, grade 1D).</li>
<li>Parenteral iron and erythropoiesis-stimulating agents should be given if indicated in pregnancy (4.6.1 and 4.6.2, grade 1C). Module 21 covers anemia; the change in plan is the nephrologist&rsquo;s.</li>
</ul>
<p>These are guideline statements, not orders for your unit. Whether your unit can provide more sessions, or must transfer the patient, is for the attending nephrologist and the Medical Director to decide.</p>
{{flow:Possible pregnancy: first steps|Suspect::Missed periods, nausea, unexplained weight change, or she says she may be pregnant.|Speak in private::Last period, contraception, symptoms.|Tell the nephrologist the same day::Not at the next clinic visit.|Testing::Per your unit&rsquo;s protocol. A positive serum result needs confirmation.|Medicine list::Flag the classes in Section 8.|Obstetric referral::Arranged by the nephrologist.|Document::What she reported, what you did, whom you told.}}
{{call:Stop and call the attending nephrologist the same day for any suspected or confirmed pregnancy. In a pregnant patient, vaginal bleeding, abdominal pain, very high blood pressure, or headache with changes in vision is an obstetric emergency: follow your unit&rsquo;s protocol, call the nephrologist at once, and arrange urgent obstetric care.}}
"""),
        ("pregdrugs", "Medicines in pregnancy", "Medicines to stop or switch in pregnancy", """
<p>Picture the pill box from Section 4, reviewed through the eyes of the baby. Some tablets that protect the mother can harm a developing baby.</p>
<p>The picture has a limit: stopping a tablet is also a harm. A blood pressure medicine stopped without a replacement leaves the mother&rsquo;s pressure uncontrolled, which harms both. A medicine that crosses the placenta reaches developing organs, and some classes block systems the baby needs, such as the hormone system that angiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) act on. Timing matters, which is why the guideline asks for a plan before pregnancy.</p>
<h3>What the guideline says</h3>
<div class="table-wrap"><table>
<thead><tr><th>Drug class</th><th>Guideline statement</th><th>Grade</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td>Angiotensin-converting enzyme (ACE) inhibitors</td><td>Women with CKD who take them should have a plan for stopping or converting them, made in advance[[wiles2019]]</td><td>Recommendation 3.3.5, 1B</td><td>Nephrologist with the obstetrician</td></tr>
<tr><td>Angiotensin receptor blockers (ARBs)</td><td>Should be stopped in advance of pregnancy[[wiles2019]]</td><td>Recommendation 3.3.6, 1D</td><td>Nephrologist with the obstetrician</td></tr>
<tr><td>Mycophenolate mofetil (an immune-suppressing drug used in lupus and after transplant)</td><td>Should be stopped before pregnancy, with an interval before conception to allow conversion to a pregnancy-safe alternative[[wiles2019]]</td><td>Recommendation 2.5, 1C</td><td>Nephrologist with the rheumatologist or transplant team</td></tr>
<tr><td>Anticoagulants, lipid-lowering drugs, newer oral anemia drugs, vitamin D analogs, and phosphate binders</td><td>Not addressed in the guideline statements reviewed for this module. Each needs review against a current drug-in-pregnancy reference</td><td>None quoted</td><td>Nephrologist with the obstetrician and pharmacist</td></tr>
<tr><td>Over-the-counter and herbal products</td><td>Safety in pregnancy is often unknown</td><td>None quoted</td><td>Nephrologist with the obstetrician</td></tr>
</tbody></table></div>
<p>The table works at the level of drug class. It gives no doses and names no replacements; both belong to the nephrologist and the obstetrician.</p>
<h3>What you do</h3>
<ol>
<li>List every medicine, including over-the-counter, herbal, and other doctors&rsquo; prescriptions.</li>
<li>Flag the classes in the table to the nephrologist and obstetrician the same day.</li>
<li>Never stop an antihypertensive without a replacement plan from the nephrologist.</li>
<li>Record what you flagged and to whom.</li>
</ol>
{{key:Find every medicine and flag it the same day. The decision to stop or switch belongs to the nephrologist and the obstetrician.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it safe to send her home now?</strong> Not yet. She has fallen three times this month, twice after dialysis. Her systolic pressure falls by 14 mm Hg on standing, from an already low 96. She has heart failure, diabetes, and a sleeping pill. Sit her back down, check a blood sugar per protocol, and ask how she feels on standing. Dizziness means she is not ready, whatever the number. Apply your unit&rsquo;s Module 11 criteria. If she cannot stand safely, keep her observed and call the attending nephrologist. Confirm that her daughter will walk her to the vehicle.</p>
<p><strong>How frail is she, and which risks can change?</strong> A cane, help to bathe, and no cooking, with independent eating and toileting, fit moderately frail. The sleeping pill is the clearest changeable risk. Her standing drop may respond to a review of her fluid goal, dry weight, and medicine timing. Her new forgetfulness needs a screen, because the sedative may be the cause. Each change is the nephrologist&rsquo;s; your work is to see and report them.</p>
<p><strong>What do you tell the nephrologist and the daughter?</strong> Use SBAR from Module 1 (situation, background, assessment, recommendation): the falls, today&rsquo;s standing drop, the sleeping pill, the pill count, the frailty score, the forgetfulness, and the daughter&rsquo;s question. Suggest a medicine review, a fluid review, and a cognitive screen. Tell the daughter her question deserves a full conversation and that you will pass it on. Ask Mrs. Santiago what matters most to her and record it. Do not say whether dialysis is helping; that conversation belongs to the nephrologist and Module 26.</p>
"""],
    "skills": {"title": "Frailty and fall-risk screen, and the private question",
               "intro": "Perform this screen on a frail patient at the end of a real session, or on a colleague playing the patient, while your preceptor observes.",
               "items": [
                   ("Observes the patient walk in and rise from the chair, and describes what was seen.", False),
                   ("Scores the Clinical Frailty Scale from function and history, and records the version used.", False),
                   ("Asks about falls, near-falls, and dizziness since the last session.", True),
                   ("Measures sitting and standing blood pressure and heart rate after dialysis, per the unit&rsquo;s protocol.", True),
                   ("Checks blood sugar in a patient with diabetes who is dizzy or confused.", False),
                   ("Reviews the medicine list for sedatives, anticholinergic drugs, new drugs, and duplicates.", False),
                   ("Screens thinking when behavior or adherence has changed, and screens for delirium when the change is new.", False),
                   ("Confirms safe transport and a companion for the trip home.", False),
                   ("Documents the findings and informs the attending nephrologist of any fall with injury, head strike, or anticoagulant use.", True),
                   ("Records, in the patient&rsquo;s own words, what matters most to the patient.", False),
                   ("Asks a woman of reproductive age, in private, about her periods and contraception.", False),
                   ("Recognizes possible pregnancy and informs the attending nephrologist the same day.", True),
               ],
               "placement": "Over two weeks, score the Clinical Frailty Scale for every patient aged 70 or older on your shifts and ask each one about falls. Review the list with your preceptor, and bring the three highest-risk patients to the attending nephrologist with one suggested change for each."},
    "quiz": [
        ("Why does a patient with heart failure tolerate fast fluid removal poorly?",
         ["The dialyzer removes fluid faster in heart failure",
          "Heart failure raises plasma refilling too much",
          "The failing heart has a narrow band between congestion and low output",
          "Heart failure patients have no fluid to remove"], 2,
         "A failing heart sits on a low, flat Frank-Starling curve, so a small change in filling matters."),
        ("A man with cirrhosis becomes drowsy and confused in hour two. What is the best first interpretation?",
         ["Confusion with several possible causes, including liver failure, low sugar, bleeding, and infection",
          "Uremia that will clear by the end of the session",
          "An expected effect that needs no action",
          "Disequilibrium, which affects every long-term patient"], 0,
         "Hepatic encephalopathy can look like uremia. Check sugar and vital signs, look for bleeding and infection, and call."),
        ("Frailty prevalence in hemodialysis ranged from 6% to 82% across studies. What best explains the range?",
         ["Frailty does not occur in younger patients",
          "Only one tool was used",
          "Most studies were randomized",
          "Studies used different tools in different populations"], 3,
         "The pooled estimate was 34.3%, but the answer depends on the tool and the population."),
        ("What does a Clinical Frailty Scale score of moderately frail tell you about one dialysis patient?",
         ["Exactly how long the patient will live",
          "That the patient needs closer watching and has a higher average risk of death",
          "That dialysis should stop",
          "Nothing, because the scale was never tested in dialysis"], 1,
         "Each one-point rise was associated with a hazard ratio of 1.22 in a dialysis cohort. It describes group risk, not one person&rsquo;s prognosis."),
        ("An 84-year-old woman stands after dialysis and says the room is spinning. Her standing pressure is much lower than sitting. What do you do first?",
         ["Let her walk slowly to the exit with her son",
          "Give saline before she stands again",
          "Sit or lay her down, recheck pressures, and apply the unit&rsquo;s discharge criteria",
          "Lower her dry weight for the next session"], 2,
         "A patient who is dizzy on standing is not ready to go. The fluid plan belongs to the nephrologist."),
        ("A frail man fell at home yesterday and struck his head. He takes an anticoagulant and seems well. What is the right step?",
         ["Start the session and mention the fall next month",
          "Call the attending nephrologist now, before the session proceeds",
          "Stop his anticoagulant yourself",
          "Reassure him because he seems well"], 1,
         "A head strike on an anticoagulant is a stop-and-call trigger, even when the patient looks well. Session heparin adds bleeding risk; the nephrologist decides how to proceed."),
        ("In the study by Murray and colleagues, what share of older hemodialysis patients had a documented diagnosis of cognitive impairment?",
         ["About one half",
          "About one third",
          "About one in eight",
          "Fewer than 3 in 100"], 3,
         "Only 2.9% had a documented diagnosis, although most had moderate or severe impairment on testing."),
        ("What did Chiu and colleagues find about pill burden?",
         ["A median of 19 pills a day, with higher burden associated with lower physical quality of life",
          "Removing pills improved survival",
          "Phosphate binders made up a small share",
          "Most patients took every pill as prescribed"], 0,
         "The study was cross-sectional. It shows an association, not that removing pills helps."),
        ("A daughter asks whether dialysis is still helping her frail mother. What is the best response?",
         ["Tell her dialysis should be stopped",
          "Tell her dialysis is clearly helping",
          "Acknowledge the question, ask the patient what matters most, record it, and tell the nephrologist",
          "Change the subject"], 2,
         "You open the door without leading. The goals-of-care conversation belongs to the attending nephrologist."),
        ("A 19-year-old from a children&rsquo;s unit keeps missing Saturday sessions. His mother answers for him. What is the best approach?",
         ["Speak only to his mother",
          "Warn him that he will lose his slot",
          "Ignore it because he is young",
          "Speak to him first, ask what makes Saturday hard, and report the pattern without blame"], 3,
         "The ISN and IPNA consensus asks for an individualized transition that builds self-management skills."),
        ("Why should you ask a woman on dialysis about contraception?",
         ["Women on dialysis are always infertile",
          "Fertility is reduced but not absent, and pregnancy changes the treatment at once",
          "Contraception improves dialysis adequacy",
          "It matters only before transplant"], 1,
         "The UK guideline recommends contraception advice for all women of reproductive age with CKD (3.1.1, grade 1D)."),
        ("Ms. Bautista, 29, on dialysis for two years, reports three missed periods and morning nausea. What is the first priority?",
         ["Tell the attending nephrologist the same day and arrange testing per protocol",
          "Reassure her that dialysis patients cannot conceive",
          "Stop her blood pressure medicines",
          "Wait for her next clinic visit"], 0,
         "These symptoms are common in kidney failure, which is why pregnancy is recognized late. Act the same day."),
        ("A non-pregnant woman on dialysis has a raised serum pregnancy hormone. What explains this possibility?",
         ["The dialyzer produces the hormone",
          "Heparin interferes with every pregnancy test",
          "The liver makes the hormone in kidney failure",
          "The kidney normally clears part of the hormone, so levels can rise without pregnancy"], 3,
         "The evidence is case-level. A positive serum result needs specialist confirmation."),
        ("In the comparison by Hladunewich and colleagues, what was associated with more live births?",
         ["Fewer sessions",
          "Stopping dialysis in the third trimester",
          "More weekly hours of hemodialysis",
          "Higher hemoglobin targets"], 2,
         "Live births were 48% at 20 hours a week or fewer and 85% above 36 hours. The comparison was observational."),
        ("A pregnant dialysis patient takes an ACE inhibitor. What do you do?",
         ["Stop it now and send her home",
          "Flag it to the nephrologist and obstetrician the same day, without stopping it yourself",
          "Double her other blood pressure medicine",
          "Continue it because no guideline addresses it"], 1,
         "The guideline asks for a plan to stop or convert ACE inhibitors (3.3.5, grade 1B). Stopping without a replacement leaves her pressure uncontrolled."),
    ],
    "terms": [("Frailty", "A state of low physiologic reserve, in which a small stress causes a large loss of function."),
              ("Clinical Frailty Scale", "A rating of fitness and frailty scored from what the patient can do. The original had 7 levels; the later version has 9."),
              ("Orthostatic hypotension", "A fall in blood pressure on standing, which can cause dizziness and falls."),
              ("Polypharmacy", "The use of many medicines at once, with rising risk of interactions and side effects."),
              ("Pill burden", "The number of tablets and capsules a patient swallows each day."),
              ("Delirium", "An acute, fluctuating disturbance of attention and thinking, with a medical cause."),
              ("Hepatic encephalopathy", "Confusion or drowsiness caused by liver failure."),
              ("Human chorionic gonadotropin", "A hormone made by the placenta, detected by pregnancy tests."),
              ("Intensified hemodialysis", "Longer or more frequent sessions than the standard schedule, prescribed by the nephrologist."),
              ("Transition", "The planned process of moving a young person from pediatric to adult care.")],
    "readings": [("hemodialysis-elderly.html", "Dialysis in older adults: frailty, falls, and goals of care."),
                 ("ckd-and-pregnancy.html", "Pregnancy in kidney disease, from planning to delivery."),
                 ("heart-failure-ckd.html", "How heart failure and kidney failure interact.")],
    "calcs": ["calc-frailty-assessment.html", "calc-cognitive-screen-ckd.html", "calc-renal-med-safety.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
