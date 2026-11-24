# -*- coding: utf-8 -*-
"""Physician on Duty, Module 23: Food, Fluid, and Muscle (nutrition and protein-energy wasting on hemodialysis).
Written for this series from published sources."""

MODULE = {
    "image_alt": "A thin older Filipino man in a dialysis chair, his shirt hanging loose, while his wife holds a lunch box. The physician on duty and a nurse study a chart of his weight over the past months.",
    "objectives": [
        "Explain why protein and energy needs rise on hemodialysis, using amino acid losses into the dialysis fluid, inflammation, acidosis, and muscle breakdown.",
        "Recognize protein-energy wasting by its four categories and screen for it at the chair with the 7-point Subjective Global Assessment, the weight trend, and muscle measures.",
        "Distinguish loss of fat and muscle from loss of fluid when the dry weight falls, and escalate to the attending nephrologist correctly.",
        "Give practical advice on salt, fluid, potassium, and phosphate, built on Filipino food, that agrees with the current guideline and with your unit&rsquo;s dietitian.",
        "Describe the evidence for eating and oral supplements during dialysis and for intradialytic parenteral nutrition, with the strength of each.",
        "State when to refer a patient to the renal dietitian and when to call the attending nephrologist.",
    ],
    "big": """
{{plain:Picture a sack of rice with a small tear at the bottom. Each time it is lifted, a few grains fall out. If no one refills it, the sack grows lighter so slowly that no one notices until it sags. A patient on hemodialysis loses a little of what the body has built at every session.}}
<p>The picture has a limit. A sack only leaks. The body also breaks down its own muscle when it is inflamed, acidic, or resistant to insulin, and uremia dulls appetite. The tear is real but small. The larger problems are a shrunken supply and faster breakdown.</p>
{{cards:Key terms for this module|Protein-energy wasting (PEW)::Loss of the body&rsquo;s protein stores and energy reserves in kidney disease.|Subjective Global Assessment (SGA)::A bedside score from the history of weight and intake and a look at fat and muscle.|Malnutrition-Inflammation Score (MIS)::A 10-part score that adds body mass index and blood tests to the SGA.|Normalized protein catabolic rate (nPCR)::Daily protein breakdown per kilogram, estimated from the rise in urea between sessions.|Oral nutritional supplement (ONS)::A ready-made drink or powder that adds protein and energy to meals.|Intradialytic parenteral nutrition (IDPN)::Nutrients given into the dialysis circuit during the session.|Sarcopenia::Loss of muscle mass and strength.}}
<p>Most patients keep their muscle with enough food, dialysis, and activity. A few slide into wasting quietly, while their weight looks like good news. Your work is to notice the slide, correct the advice that causes it, and bring the renal dietitian and the attending nephrologist in early.</p>
""",
    "case": {"title": "He lost five kilos, and everyone was pleased", "html": """
<p>Mr. Bienvenido Ocampo, 68, has been on hemodialysis for two years for kidney failure from hypertension. He dialyzes on Tuesdays, Thursdays, and Saturdays. Over four months his post-dialysis weight fell from 64 to 59 kilograms (illustrative). The team lowered his dry weight twice because &ldquo;he reaches it so easily.&rdquo;</p>
<p>His wife says he eats &ldquo;a little rice and soup.&rdquo; A relative told him that meat is bad for the kidneys, so he avoids it. He has stopped going to church on Sundays because he is tired. His serum albumin has gone from 3.8 to 3.2 g/dL over the same months (illustrative).</p>
<p>Today, a Thursday, he cramps at hour three and his pressure falls. Ms. Arlene Villaruz, the nurse, lays the chair back and stops fluid removal under the unit&rsquo;s protocol. He recovers within minutes. She then asks you whether the dry weight should be lowered again.</p>
""", "questions": ["Is this weight loss fluid, fat, or muscle, and how can you tell at the chair?",
                  "What would a two-minute nutrition screen show, and whom do you call?",
                  "What is wrong with the advice he received about meat, and what does current guidance say instead?"]},
    "sections": [
        ("needs", "Why more protein", "Why a dialysis patient needs more protein, not less", """
<p>Muscle protein is broken down and rebuilt every day, and amino acids from food pay for the rebuilding. Kidney failure and dialysis tip that balance toward breakdown.</p>
{{fig:pod23_removes}}
<p>The first loss is in the dialyzer. Free amino acids are small, so they cross the membrane with urea. Ikizler and colleagues measured the dialysis fluid in nine patients on three membranes. About 6 to 8 grams of amino acids left per session, depending on the membrane. On the sixth reuse of a high-flux dialyzer, losses rose by about half, and albumin appeared in the fluid.[[ikizler1994]] The study was small and used dialyzers of the 1990s. Across three sessions, about 7 grams each comes to roughly 3 grams a day: real, but modest. The larger losses happen inside the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Driver</th><th>What it does to muscle</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>Inflammation, from a catheter, infection, or uremia</td><td>Speeds protein breakdown, suppresses appetite, lowers albumin production</td><td>Fever, a catheter, a raised C-reactive protein, a falling albumin</td></tr>
<tr><td>Metabolic acidosis (Module 2)</td><td>Activates the pathways that break down muscle protein</td><td>A low pre-dialysis bicarbonate</td></tr>
<tr><td>Insulin resistance</td><td>Muscle responds less to the signals that build it</td><td>Weakness out of proportion to intake</td></tr>
<tr><td>Poor appetite</td><td>Uremia, nausea, altered taste, depression, and post-dialysis fatigue cut intake</td><td>Skipped meals, &ldquo;a little rice and soup&rdquo;</td></tr>
<tr><td>Inactivity</td><td>Muscle that is not used is not rebuilt</td><td>Sitting all day between sessions</td></tr>
</tbody></table></div>
<p>A standard dialysis text describes the same drivers.[[daugirdas2015]] Their weight differs between patients, so the screen in this module asks about each.</p>
<h3>What the guideline says about protein and energy</h3>
<p>Before dialysis, some patients are advised to eat less protein. On dialysis the advice changes. The Kidney Disease Outcomes Quality Initiative (KDOQI) 2020 nutrition guideline recommends a dietary protein intake of 1.0 to 1.2 g/kg body weight per day for metabolically stable adults on maintenance hemodialysis (Grade 1C; OPINION for peritoneal dialysis). It also recommends an energy intake of 25 to 35 kcal/kg body weight per day, set by age, sex, activity, and other factors (Grade 1C).[[kdoqi_nut2020]] The Kidney Disease: Improving Global Outcomes (KDIGO) 2022 diabetes guideline gives the same protein range for patients with diabetes on dialysis as an ungraded practice point.[[kdigo_dm2022]] Module 22 covers the diabetic diet.</p>
<p>The 1 means &ldquo;we recommend,&rdquo; and the C means low certainty of evidence. The direction is firm. The prescription for your patient belongs to the dietitian and the nephrologist.</p>
{{formula:<strong>Worked example 1, illustrative arithmetic, not an order.</strong> KDOQI 2020 range: 1.0 to 1.2 g/kg/day (Grade 1C).[[kdoqi_nut2020]] Patient weight: 59 kg.<br>1.0 &times; 59 = 59 grams of protein per day. 1.2 &times; 59 = about 71 grams per day.<br><em>What it tells you:</em> the size of the gap in a patient who eats a little rice and soup. <em>What it does not tell you:</em> which body weight to use (actual, adjusted, or ideal). The guideline leaves that to clinical judgment.}}
<h3>Estimating intake from the urea numbers</h3>
<p>Module 7 used the urea values to judge the dose. They also estimate intake. Urea rises between sessions because the body breaks down protein, and in a stable patient breakdown equals intake. The normalized protein catabolic rate (nPCR) turns the rise into grams per kilogram per day.[[depner1996]]</p>
{{formula:<strong>Worked example 2, illustrative.</strong> Bedside interdialytic-rise equation, as used in the site&rsquo;s nPCR calculator:<br>nPCR (g/kg/day) = 0.22 + (0.036 &times; urea nitrogen rise in mg/dL &times; 24) &divide; interval in hours.<br>Post-dialysis blood urea nitrogen (BUN) on Tuesday: 18 mg/dL. Pre-dialysis BUN on Thursday: 42 mg/dL. Rise: 24 mg/dL. Interval: 44 hours.<br>0.036 &times; 24 &times; 24 = 20.7. Then 20.7 &divide; 44 = 0.47. Then 0.22 + 0.47 = about 0.7 g/kg/day.<br><em>What it tells you:</em> in a stable patient, intake is probably below the guideline range. <em>What it does not tell you:</em> it is a surrogate. It misleads during infection, with residual urine output, and while the patient&rsquo;s own muscle is breaking down. Trend it monthly beside the weight and albumin.}}
{{key:Before dialysis, the advice was often &ldquo;less protein.&rdquo; On dialysis it changes to &ldquo;enough protein.&rdquo; Check which advice the patient is still following.}}
"""),
        ("pew", "What wasting is", "Protein-energy wasting: what it is and how common", """
<p>Picture a house that burns its own walls to keep the lights on. When intake falls short and breakdown runs fast, the body spends muscle and fat the same way. The picture has a limit: the body does not choose this. Inflammation and acidosis drive breakdown even when food is available.</p>
<p>In 2008, an expert panel of the International Society of Renal Nutrition and Metabolism (ISRNM) proposed the term protein-energy wasting (PEW) for loss of body protein and fuel reserves in kidney disease. The panel set criteria in four categories. The diagnosis needs findings in at least three of the four, with at least one finding in each category used.[[fouque2008]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Category</th><th>Examples of criteria proposed by the ISRNM panel</th><th>What it looks like at the chair</th></tr></thead>
<tbody>
<tr><td>Serum chemistry</td><td>Low albumin (below 3.8 g/dL by the bromcresol green method), low transthyretin (prealbumin, below 30 mg/dL in dialysis patients), or low cholesterol (below 100 mg/dL)</td><td>A monthly albumin that keeps drifting down</td></tr>
<tr><td>Body mass</td><td>Body mass index below 23 (the panel noted that a lower cutoff may suit some Asian populations), unintended weight loss of 5% over 3 months or 10% over 6 months, or total body fat below 10%</td><td>A post-dialysis weight that falls month after month. Loose clothes</td></tr>
<tr><td>Muscle mass</td><td>Loss of muscle mass of 5% over 3 months or 10% over 6 months, a mid-arm muscle circumference more than 10% below the reference median, or low creatinine appearance</td><td>Thin upper arms, hollow temples, prominent collarbones</td></tr>
<tr><td>Dietary intake</td><td>Unintended protein intake below 0.8 g/kg per day, or energy intake below 25 kcal/kg per day, for at least 2 months</td><td>&ldquo;A little rice and soup.&rdquo; A low nPCR</td></tr>
</tbody></table></div>
<p>The panel added that markers of inflammation, such as C-reactive protein, are useful clues but do not define wasting. It advised documenting each criterion on at least three occasions, preferably 2 to 4 weeks apart, so one low value does not make the diagnosis.[[fouque2008]] The criteria are expert consensus, not a validated diagnostic test.</p>
<h3>How common it is</h3>
<p>Carrero and colleagues pooled 90 studies of 16,434 patients on maintenance dialysis in 34 countries. Using the SGA or the MIS, the middle half of studies found wasting in 28% to 54% of patients. Region explained part of the variation.[[carrero2018]] The studies were observational and used different tools. Still, on a typical shift several of your patients are wasting.</p>
{{cards:Signs of wasting at the chair|Temples::Hollowing at the sides of the forehead.|Collarbones and shoulders::Bones that stand out more than they did.|Upper arm::A thin non-access arm with a loose fold over the triceps.|Hands::Hollows between the thumb and the index finger.|Clothes::A belt on a new hole, a ring that slides.|Appetite::A lunch box that goes home full.|Grip::A weak handshake, or trouble opening a bottle.}}
<h3>Why albumin alone misleads</h3>
<p>Albumin is on every monthly sheet, but it is not a nutrition test. The liver makes less during inflammation, and extra fluid dilutes it. A well-fed patient can have a low albumin during an infection. Low albumin is a surrogate: it tells you something is wrong, not what. Read it beside the temperature, the edema, and the weight trend.</p>
{{key:A falling albumin is a question, not an answer. Ask whether the patient is inflamed, overloaded, or underfed, and remember it may be all three.}}
"""),
        ("screen", "Screen at the chair", "A two-minute screen at the chair", """
<p>Think of the screen as three questions and two looks: weight, food, and the gut; then the body and the numbers.</p>
<h3>The tools and their evidence</h3>
<p>The KDOQI 2020 guideline states that the 7-point Subjective Global Assessment (SGA) is a valid and reliable tool for nutritional status in adults on dialysis (Grade 1B). It suggests that the Malnutrition-Inflammation Score (MIS) may be used in adults on maintenance hemodialysis (Grade 2C).[[kdoqi_nut2020]] The SGA rests on the history of weight and intake, symptoms, function, and a look at fat and muscle.</p>
<p>The MIS adds body mass index, albumin, and total iron-binding capacity to the SGA, for 10 components scored 0 to 3. In 83 hemodialysis outpatients followed for a year, a higher score correlated with more hospital days and was associated with death. Only nine patients died, so the risk estimate was wide.[[kalantar2001]] The score tracks outcomes. That acting on it changes them is not shown.</p>
<p>Muscle strength adds what the scale misses. Hwang and colleagues pooled 9 prospective cohorts of patients on dialysis. Patients with low handgrip strength had a higher risk of death than those with high strength (risk ratio 1.88, 95% confidence interval 1.51 to 2.33). Each additional kilogram of grip was associated with a 5% lower risk.[[hwang2019]] These are associations. Weak grip marks frailty and illness as well as poor nutrition.</p>
<p>The site&rsquo;s nutrition screening calculator scores the SGA and the MIS. Use the tool your unit has chosen, scored the same way each time.</p>
{{flow:The two-minute nutrition screen|Weight trend::Open the record and read the post-dialysis weights for the last three months. Note the percent change.|Intake::Ask what the patient ate yesterday, how many meals, and which protein foods. Ask whether the patient follows any food rule from a relative or an old handout.|Gut and mouth::Ask about nausea, vomiting, diarrhea, loose or painful teeth, ill-fitting dentures, and trouble swallowing.|Look::Check the temples, collarbones, upper arm on the non-access side, and hands. Check the ankles and the lower back for edema.|Grip::If the unit has a dynamometer, measure grip on the non-access hand.|Numbers::Read the latest albumin, potassium, phosphate, bicarbonate, and nPCR together, never one alone.|Score and act::Score the SGA or the unit&rsquo;s tool. Refer a positive screen to the renal dietitian and inform the attending nephrologist.}}
<p>Your unit&rsquo;s protocol sets the routine interval and who scores it. Your part is to run the screen when something changes: a falling weight, a full lunch box going home, or a wife who says &ldquo;he does not eat anymore.&rdquo;</p>
{{call:Stop and call the attending nephrologist, and refer to the renal dietitian the same week per your unit&rsquo;s protocol, when you find unplanned weight loss over several months with poor intake or a positive screen; a patient who cannot eat or keep food down because of nausea, vomiting, or mouth or teeth problems; or a falling albumin with fever, new edema, or breathlessness.}}
{{key:Ask what the patient ate yesterday, look at the arms and temples, and read the weight trend. Those three take two minutes and catch most wasting.}}
"""),
        ("fleshfluid", "Flesh or fluid", "Falling weight: flesh or fluid?", """
<p>Picture a shrinking balloon. It could be leaking air, or the rubber could be thinning. A falling post-dialysis weight is the same puzzle: water, or body.</p>
<p>The picture has a limit, and the limit is the point. The post-dialysis weight is tissue plus fluid. Module 8 set out how the dry weight is chosen. When a patient loses muscle and fat but the target stays the same, the scale hides the loss. The same weight now holds less tissue and more water, which can appear as rising pressure, edema, or breathlessness.</p>
<p>Lowering the target by the tissue lost can be right. The danger is chasing the weight. A patient who eats less also takes in less salt and water, so the target is reached easily. The team reads this as extra fluid and lowers it again. Once the target falls below the new true dry weight, each session pulls fluid the body cannot spare. The patient cramps and drops late in the session, and no one treats the wasting.</p>
<p>The KDIGO Controversies Conference on blood pressure and volume lists reassessment of the target weight among the first measures when sessions are complicated by low pressure. Its statements are conference conclusions, not graded recommendations.[[kdigo_bpvol2020]] That a target set for one body becomes wrong when the body changes is established physiology. No trial tells you how often to reassess.</p>
{{formula:<strong>Worked example 3, illustrative.</strong> Percent weight change = (old weight &minus; new weight) &divide; old weight &times; 100 (arithmetic).<br>(64 &minus; 59) &divide; 64 &times; 100 = 7.8% over 4 months.<br>The ISRNM panel lists unintended weight loss of 5% over 3 months, or 10% over 6 months, among the body-mass criteria for wasting.[[fouque2008]]<br><em>What it tells you:</em> this loss deserves attention. <em>What it does not tell you:</em> whether it is water or tissue. The bedside look and the intake history decide that.}}
{{flow:Falling weight: flesh or fluid|Confirm the trend::Read the post-dialysis weights over three months. Calculate the percent change.|Ask about food::What did the patient eat yesterday? Any new food rules? Any nausea, mouth, or teeth problems?|Look for tissue loss::Temples, collarbones, arms, hands, clothes, grip.|Look for fluid::Edema, breathlessness, blood pressure trend, and the weight gain between sessions.|Check the session::Cramps or drops late in the session at the current target suggest the target may now be too low.|Report::Tell the attending nephrologist what you found, and refer to the dietitian. The dry weight is reviewed by the nephrologist, not changed by you.}}
{{call:Stop and call the attending nephrologist before any further change to the target weight when you are asked to lower the dry weight in a patient whose weight has been falling and who may be losing tissue. Manage today&rsquo;s session by protocol while you call.}}
{{key:A falling dry weight is not always good news. Ask whether the patient lost water, or lost himself.}}
"""),
        ("plate", "Salt, fluid, K, P", "Salt, fluid, potassium, and phosphate with Filipino food", """
<p>Picture the dialysis plate: rice, a fresh protein, vegetables, and the sauces on the side. The picture has a limit: portions differ with urine output, laboratory results, and body size, and the dietitian sets them. Your part is to answer everyday questions in a way that agrees with the dietitian and does not push the patient toward wasting.</p>
{{fig:pod23_plate}}
<h3>Salt and fluid</h3>
<p>Module 2 explained that salt drives thirst. Fluid advice without salt advice fails. The KDOQI 2020 guideline recommends limiting sodium intake to less than 100 mmol per day, which is less than 2.3 grams of sodium, in adults on dialysis (Grade 1C).[[kdoqi_nut2020]] Filipino cooking carries sodium in fish sauce (patis), soy sauce, shrimp paste (bagoong), seasoning cubes, dried and salted fish, and instant noodles.</p>
{{fig:pod02_salt|Salt in the Filipino kitchen. The salt that drives thirst often comes from sauces and seasonings, not the salt shaker.}}
<p>The fluid allowance belongs to the nephrologist. It depends on urine output and the gains between sessions, not on one number for everyone. Patients often count only drinks, but fluid also hides in soup, porridge, ice, and fruit.</p>
{{fig:pod23_fluid}}
<h3>Potassium</h3>
<p>Module 2 covered why potassium rises. The question here is food. The KDOQI 2020 guideline states that it is reasonable to change dietary potassium to keep serum potassium in the normal range (OPINION). For patients with a high or low potassium, it suggests that intake be based on the patient&rsquo;s needs and the clinician&rsquo;s judgment (Grade 2D).[[kdoqi_nut2020]] A KDIGO Controversies Conference described a shift away from blanket restriction toward eating patterns that are associated with better outcomes, such as diets rich in plants. It also noted how few data show that changing the diet brings an abnormal serum potassium back to normal.[[clase2020]]</p>
<p>The two sources differ in tone more than substance. Both ask for an individual plan. Units still differ in how strictly they restrict, and the evidence either way is weak.</p>
{{fig:pod23_potassium}}
<p>A high pre-dialysis potassium has more causes than the last banana. Before you blame the food, look for these.</p>
<div class="table-wrap"><table>
<thead><tr><th>Non-food cause</th><th>How it raises potassium</th><th>What to ask or check</th></tr></thead>
<tbody>
<tr><td>Missed or shortened sessions</td><td>Less potassium is removed, and more days of intake build up</td><td>Attendance and minutes delivered</td></tr>
<tr><td>Constipation</td><td>The colon secretes more potassium when the kidneys cannot. Hard stools slow this route</td><td>Bowel habits over the past week</td></tr>
<tr><td>Metabolic acidosis</td><td>Potassium shifts out of cells</td><td>Pre-dialysis bicarbonate</td></tr>
<tr><td>Medicines</td><td>Some blood pressure and heart medicines reduce potassium removal by the gut or the remaining kidney, or slow its entry into cells</td><td>The medication list, for the nephrologist to review</td></tr>
<tr><td>Tissue breakdown or a hemolyzed sample</td><td>Potassium leaks from damaged cells, in the body or in the tube</td><td>Recent injury, bleeding, or a difficult blood draw</td></tr>
</tbody></table></div>
<p>The site&rsquo;s potassium load calculator, drawn from the Philippine Food Composition Tables, shows where large loads hide: coconut water, taro, potato, mung beans, and saba banana.</p>
<h3>Phosphate</h3>
<p>The KDOQI 2020 guideline recommends changing dietary phosphorus to keep serum phosphate in the normal range (Grade 1B).[[kdoqi_nut2020]] The source of phosphate matters. Phosphate in plant foods is partly bound and poorly absorbed. Phosphate in meat and fish is absorbed better. Phosphate added to processed food as a preservative or flavor is absorbed most completely.[[kdoqi_nut2020]] Module 21 covers phosphate binders and the mineral axis.</p>
<p>Sullivan and colleagues tested this in a cluster randomized trial of 279 hemodialysis patients with high phosphate in 14 facilities. Patients taught to avoid foods with phosphorus additives had a fall in serum phosphorus 0.6 mg/dL larger than those in usual care after 3 months (95% confidence interval 0.1 to 1.0).[[sullivan2009]] Phosphate is a surrogate, and the trial did not measure fractures, heart disease, or death. It does show that the additive load is real and that teaching changes it.</p>
{{fig:pod23_phosphate}}
<p>This matters for protein. A patient told to cut phosphate often cuts meat, fish, and eggs. The better trade is to keep the fresh protein and drop the hotdog, the luncheon meat, the instant noodles, and the cola.</p>
{{cards:What the physician on duty does about food|Answer plainly::Use the unit&rsquo;s handouts. Agree with the dietitian.|Protect protein::Never answer a high phosphate or potassium by stopping meat, fish, or eggs.|Look past the plate::Check attendance, bowels, bicarbonate, and medicines before blaming fruit.|Refer::Meal planning goes to the dietitian; patterns go to the nephrologist.}}
{{key:Salt drives thirst, processed food drives phosphate, and a high potassium has more causes than the last banana.}}
"""),
        ("intradialytic", "Eating and supplements", "Eating and supplements during dialysis", """
<p>Twelve hours a week in a chair can feed the patient or starve him. The picture has a limit: food in the chair has a cost. Module 13 explained that a meal can lower the pressure during fluid removal, and a drowsy patient can choke.</p>
<h3>Meals during dialysis</h3>
<p>An ISRNM consensus statement concluded that meals or supplements during hemodialysis may improve nutritional status and should be considered for patients without contraindications. It listed the risks: a fall in pressure after eating, aspiration, gut symptoms, hygiene, and possibly less efficient waste removal, and it called for larger trials.[[kistler2018]] This is consensus built on small studies, not a graded recommendation. Follow your unit&rsquo;s policy on food in the chair.</p>
<h3>Oral nutritional supplements</h3>
<p>The KDOQI 2020 guideline suggests a trial of oral nutritional supplements for at least three months in adults on dialysis who are at risk of wasting or have it, when counseling alone does not meet their needs (Grade 2D).[[kdoqi_nut2020]] A 2D grade is a suggestion on very low certainty evidence.</p>
<p>A Cochrane review of 22 randomized trials with 1,278 participants found that oral protein-based supplements probably raise serum albumin (mean difference 0.19 g/dL, moderate certainty), more so in hemodialysis and malnourished patients. They may make little or no difference to weight or body mass index.[[mah2020]] A 2023 meta-analysis of 22 trials with 1,185 patients found small rises in albumin (1.26 g/L), body mass index (0.30 kg/m&sup2;), and handgrip strength (0.96 kg), with no change in serum potassium or phosphorus.[[liu2023]]</p>
<p>The two reviews disagree on body mass index. They included different trials, and all effects are small surrogates. The authors of the 2023 review state that it remains uncertain whether the gains translate into outcomes that matter to patients.[[liu2023]] Supplements raise albumin a little, probably most in those who need it, and do not appear to worsen potassium or phosphate.</p>
<h3>Intradialytic parenteral nutrition</h3>
<p>Intradialytic parenteral nutrition (IDPN) delivers amino acids, glucose, and fat into the venous line during the session. Cano and colleagues randomized 186 malnourished hemodialysis patients, all given oral supplements, to one year of IDPN or none. IDPN did not improve death at two years, the primary outcome, or admissions, body mass index, or laboratory markers. Both groups improved on supplements.[[cano2007]]</p>
<p>The KDOQI 2020 guideline suggests a trial of IDPN for patients with wasting whose needs cannot be met by mouth or tube (Grade 2C).[[kdoqi_nut2020]] The two fit together: IDPN adds nothing for a patient who can take oral supplements. It is a prescription, and the physician on duty never starts it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Intervention</th><th>Outcome measured</th><th>What the evidence shows</th><th>Certainty</th></tr></thead>
<tbody>
<tr><td>Counseling by a dietitian</td><td>Intake, nutritional status</td><td>Recommended as the first step in the guideline[[kdoqi_nut2020]]</td><td>Guideline statement</td></tr>
<tr><td>Oral supplements</td><td>Albumin, body mass index, grip (surrogates)</td><td>Small rises in albumin and grip. No data showing fewer deaths[[mah2020]][[liu2023]]</td><td>Moderate for albumin. Grade 2D in KDOQI</td></tr>
<tr><td>Meals during dialysis</td><td>Intake, nutritional markers</td><td>May help. Risks of low pressure and aspiration[[kistler2018]]</td><td>Consensus, small studies</td></tr>
<tr><td>IDPN</td><td>Death, admissions, nutrition markers</td><td>No benefit over oral supplements in one large trial[[cano2007]]</td><td>One randomized trial. Grade 2C in KDOQI for those who cannot eat</td></tr>
<tr><td>Exercise during dialysis</td><td>Walk distance, fitness, strength</td><td>Improves function measures. No mortality data[[young2018]][[zhao2026]]</td><td>Not formally graded. All cycling trials were at high risk of bias</td></tr>
</tbody></table></div>
{{cards:When to refer to the renal dietitian|Positive screen::The SGA or the unit&rsquo;s tool flags risk.|Falling weight::Unplanned loss over months, or a dry weight lowered more than once.|Poor intake::Fewer meals, avoided protein foods, or a low nPCR.|Abnormal chemistry::A persistently high potassium or phosphate, or a falling albumin.|Outdated rules::A food rule that does not fit dialysis.}}
{{key:Supplements raise albumin a little, which is a surrogate. Eating in the chair helps many and endangers a few. IDPN is the nephrologist&rsquo;s decision for the patient who cannot eat.}}
"""),
        ("muscle", "Keeping muscle", "Keeping muscle: activity and exercise", """
<p>Muscle is a bank account that pays out only if you keep depositing. Protein is one deposit, and use is the other. The picture has a limit: in kidney failure, inflammation and acidosis are thought to blunt the response of muscle to both, so expectations should be modest.</p>
<p>Physical activity on hemodialysis is low and tends to fall over time.[[zhao2026]] Exercise during the session uses supervised time that is otherwise lost.</p>
{{fig:pod23_exercise}}
<h3>What the trials show</h3>
<p>Young and colleagues reviewed 13 randomized trials of cycling during dialysis. Pooled data showed no significant change in peak oxygen uptake, a measure of fitness, or in quality of life on the Short Form 36 questionnaire. The distance walked in six minutes improved by about 88 meters. All included trials were judged at high risk of bias.[[young2018]]</p>
<p>A 2026 meta-analysis by Zhao and colleagues pooled 23 trials with 1,114 patients. Combined aerobic and resistance exercise during dialysis improved physical activity and peak oxygen uptake. Resistance exercise improved muscle strength. Moderate intensity improved all three.[[zhao2026]] Effects were reported as standardized mean differences, which are hard to translate into bedside units.</p>
<p>The earlier review tested cycling alone and found little change in fitness. The later one included resistance work and found gains. Both report function, which matters to patients, but neither reported an effect on deaths or admissions.</p>
<h3>What the physician on duty does</h3>
<p>Support the unit&rsquo;s exercise program, clear patients for it as the protocol directs, and encourage walking on non-dialysis days. Muscle cannot be rebuilt without amino acids, so exercise without enough protein is plausibly less useful. That is physiology, not a trial result. Stop in-chair exercise for a falling pressure (Module 13), chest pain or breathlessness (Module 15), or any problem at the needle sites.</p>
{{key:Muscle needs both food and use. Support the unit&rsquo;s program, stop when the pressure falls, and remember that the benefit shown so far is in function, not survival.}}
"""),
    ],
    "debrief": ["""
<p><strong>Fluid, fat, or muscle?</strong> Mostly tissue. He lost 7.8% of his weight in four months while eating little and avoiding meat. He is tired, his albumin is falling, and he has no edema. Today he cramped and dropped late in the session at a target lowered twice. That pattern fits a target chasing a shrinking body. He reaches it easily because he eats, salts, and drinks less, not because he carries extra water. You confirm it at the chair by looking at his temples, collarbones, and non-access arm, and by checking his ankles and lower back for edema.</p>
<p><strong>The screen and the call.</strong> The weight trend shows loss. Yesterday he ate rice and soup twice, with no fish, egg, or meat. His upper denture is loose. His temples are hollow and his arms are thin. Ms. Villaruz scores him at risk on the unit&rsquo;s SGA form. You do not lower the dry weight. You call the attending nephrologist and report the trend, the screen, the cramps, and the albumin, and say the loss may be flesh. The nephrologist asks for a dry weight review, a dietitian referral this week, a check for infection, a dental review, and this month&rsquo;s nPCR. You record the call and the plan.</p>
<p><strong>The advice about meat.</strong> The relative&rsquo;s rule may come from advice given before dialysis. On hemodialysis, the KDOQI 2020 guideline recommends 1.0 to 1.2 g/kg of protein per day for stable patients (Grade 1C), roughly 59 to 71 grams a day for him, far more than rice and soup provide. You tell him and his wife that his body now needs protein to rebuild what dialysis and illness take, and that fish, egg, and chicken are good choices. The dietitian sets the portions around his phosphate and potassium, and may suggest a supplement trial.</p>
"""],
    "skills": {"title": "Two-minute nutrition screen at the chair",
               "intro": "Perform this screen on a patient in your unit, with consent, or on a colleague playing a patient, while your preceptor observes. Score the patient with the tool your unit uses.",
               "items": [
                   ("Reviews the post-dialysis weight trend for the last three months and states the percent change.", True),
                   ("Asks about appetite, the number of meals, and the protein foods eaten yesterday.", False),
                   ("Asks whether the patient follows any food rule from relatives or old handouts.", False),
                   ("Asks about nausea, vomiting, diarrhea, teeth, dentures, and swallowing.", False),
                   ("Inspects the temples, collarbones, upper arm on the non-access side, and hands for loss of muscle and fat.", False),
                   ("Checks for edema to separate fluid change from tissue change.", True),
                   ("Measures handgrip on the non-access hand if the unit has a dynamometer.", False),
                   ("Scores the 7-point SGA or the unit&rsquo;s tool correctly.", False),
                   ("Reads the latest albumin, potassium, phosphate, bicarbonate, and nPCR together and explains what each can and cannot show.", False),
                   ("Corrects outdated advice, such as &ldquo;avoid all meat,&rdquo; in plain language that agrees with the dietitian.", True),
                   ("Declines to lower the dry weight on the spot and explains why the nephrologist must review it.", True),
                   ("Refers a positive screen to the renal dietitian and informs the attending nephrologist.", True),
               ],
               "placement": "Over two weeks, run the two-minute screen on five patients whose weight has fallen or whose albumin is low. For each, write the percent weight change, the screen result, and whether you judged the change to be fluid or tissue. Review the cases with your preceptor and the unit&rsquo;s dietitian."},
    "quiz": [
        ("Why do protein needs rise once a patient starts hemodialysis?",
         ["The dialysis fluid adds urea to the blood",
          "Amino acids are lost into the dialysis fluid, and inflammation and acidosis speed muscle breakdown",
          "Dialysis stops the liver from making protein",
          "Protein is needed to replace the water removed"], 1,
         "Each session removes amino acids, and inflammation and acidosis speed breakdown."),
        ("In the study by Ikizler and colleagues, about how much amino acid was lost per session?",
         ["Less than 1 gram",
          "About 50 grams",
          "About 6 to 8 grams",
          "About 100 grams"], 2,
         "About 6 to 8 grams, depending on the membrane: real but modest."),
        ("What does the KDOQI 2020 guideline recommend for protein intake in metabolically stable adults on maintenance hemodialysis?",
         ["The same low intake advised before dialysis",
          "No recommendation is made",
          "As little protein as possible to reduce urea",
          "1.0 to 1.2 g/kg per day, Grade 1C"], 3,
         "A strong recommendation (1) on low-certainty evidence (C)."),
        ("A 66-year-old woman on dialysis has an albumin of 3.1 g/dL. She has had a fever for two days and a catheter in her neck. Her weight is stable and she eats well. What is the best reading of her albumin?",
         ["Inflammation is a likely cause, so look for infection before labeling her malnourished",
          "She has protein-energy wasting and needs supplements now",
          "Her dialysis dose is too high",
          "The value is normal for a dialysis patient"], 0,
         "Inflammation lowers albumin. Alone, it does not diagnose wasting."),
        ("Under the ISRNM criteria, what is needed to diagnose protein-energy wasting?",
         ["A raised C-reactive protein",
          "A low albumin alone",
          "Findings in at least three of four categories: chemistry, body mass, muscle mass, and intake",
          "A body mass index below the normal range"], 2,
         "The panel required findings across categories. Inflammation markers are clues, not criteria."),
        ("A pooled analysis of 90 dialysis studies found that the middle half of studies reported protein-energy wasting in what share of patients?",
         ["28% to 54%",
          "1% to 5%",
          "Over 90%",
          "10% to 15%"], 0,
         "The 25th to 75th percentile range was 28% to 54%."),
        ("Which tool does the KDOQI 2020 guideline describe as valid and reliable for nutritional assessment in adults on dialysis, with Grade 1B?",
         ["Body mass index alone",
          "The 7-point Subjective Global Assessment",
          "Serum albumin",
          "Mid-arm circumference alone"], 1,
         "The MIS carries a weaker 2C statement."),
        ("A man&rsquo;s post-dialysis weight fell from 70 to 65 kilograms in three months. He eats less, his temples are hollow, and he has no edema. The nurse asks whether to lower his dry weight. What do you do?",
         ["Lower it by five kilograms to match the scale",
          "Lower it by one kilogram as a trial",
          "Raise the fluid goal to keep the pressure up",
          "Leave the target as it is, run the nutrition screen, and call the attending nephrologist to review it"], 3,
         "About 7% lost, with signs of tissue loss. The dry weight belongs to the nephrologist."),
        ("Why can a patient who loses muscle but keeps the same dry weight become overloaded?",
         ["Muscle releases water when it breaks down",
          "The same target weight now holds less tissue and more fluid",
          "Dialysis removes less fluid from thin patients",
          "Lost muscle raises sodium in the blood"], 1,
         "If tissue falls and the target does not, water fills the gap."),
        ("A woman&rsquo;s pre-dialysis potassium is high for the second month. She has stopped eating fruit, has not moved her bowels in four days, and missed a session last week. What is the best next step?",
         ["Tell her to stop eating vegetables as well",
          "Increase her blood flow on your own",
          "Report the constipation and missed session as likely causes to the attending nephrologist and ask the dietitian to review her intake",
          "Reassure her that the result is a laboratory error"], 2,
         "Missed dialysis and constipation explain it better than her diet."),
        ("What did the cluster randomized trial by Sullivan and colleagues show?",
         ["Teaching patients to avoid phosphorus additives lowered serum phosphorus more than usual care",
          "Phosphorus additives have no effect on serum phosphate",
          "Avoiding additives reduced deaths",
          "Cutting all meat lowered phosphate without harm"], 0,
         "The fall was 0.6 mg/dL larger at three months, a surrogate outcome."),
        ("A tricycle driver brings instant noodles and a cola to every session, and his phosphate stays high. What advice fits current guidance?",
         ["Stop all fish, egg, and meat",
          "Drink more cola to dilute the phosphate",
          "Double the binder on your own",
          "Keep the fresh protein, cut the processed foods, and see the dietitian"], 3,
         "Additive phosphate is absorbed more completely than phosphate in fresh food."),
        ("What did the Cochrane review of oral protein-based supplements in dialysis find?",
         ["Supplements reduced deaths by half",
          "Supplements probably raise serum albumin a little, a surrogate outcome",
          "Supplements raise potassium dangerously",
          "Supplements had no effect on any measure"], 1,
         "The mean difference in albumin was 0.19 g/dL, with moderate certainty. Albumin is a surrogate."),
        ("In the randomized trial by Cano and colleagues, what did adding intradialytic parenteral nutrition to oral supplements do?",
         ["Halved two-year mortality",
          "Improved albumin but increased infections",
          "Did not improve two-year mortality, admissions, or nutritional markers",
          "Replaced the need for oral supplements"], 2,
         "IDPN added nothing over oral supplements in 186 malnourished patients."),
        ("An 80-year-old man falls asleep with rice in his mouth during hour two and his pressure falls soon after. What is the best response after you clear his mouth and manage the drop?",
         ["Report the episode and suggest the team review whether and when he eats in the chair",
          "Ban all food for every patient in the unit",
          "Start intradialytic parenteral nutrition",
          "Tell the family to bring more food"], 0,
         "Eating in the chair helps many and endangers a few. The team decides who eats, and when."),
    ],
    "terms": [("Protein-energy wasting", "Loss of the body&rsquo;s protein stores and energy reserves in kidney disease, defined by chemistry, body mass, muscle mass, and intake."),
              ("Subjective Global Assessment", "A bedside nutrition score built from the history of weight and intake and a physical look at fat and muscle."),
              ("Malnutrition-Inflammation Score", "A 10-part score, 0 to 30, that adds body mass index and blood tests to the SGA."),
              ("Normalized protein catabolic rate", "An estimate of daily protein breakdown per kilogram, from the rise in urea between sessions. In a stable patient it reflects intake."),
              ("Oral nutritional supplement", "A ready-made drink or powder that adds protein and energy to meals."),
              ("Intradialytic parenteral nutrition", "Amino acids, glucose, and fat given into the dialysis circuit during a session."),
              ("Phosphate additive", "Phosphate added to processed food as a preservative or flavor. It is absorbed more completely than phosphate in fresh food."),
              ("Sarcopenia", "Loss of muscle mass and strength."),
              ("Surrogate outcome", "A laboratory value or measurement used in place of an outcome the patient feels, such as albumin in place of survival.")],
    "readings": [("nutrition-kidney-patients.html", "An overview of eating well with kidney disease and on dialysis."),
                 ("phosphorus-ckd.html", "Phosphate in food, additives, and the mineral balance in kidney disease."),
                 ("potassium-hyperkalemia-ckd.html", "Potassium in food and the many causes of a high potassium.")],
    "calcs": ["calc-nutrition-screening.html", "calc-npcr.html", "calc-potassium-load.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
