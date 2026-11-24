# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 04: Energy, Protein, and Eating Patterns in Stable CKD. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian and an older man comparing two plates: one with a large fried pork portion, one with fish, tofu, vegetables, and rice.",
    "objectives": [
        "State the KDIGO 2024, KDOQI 2020, and American Diabetes Association 2026 protein recommendations for adults with CKD not on dialysis, with their grades, and explain why they differ.",
        "Decide whether a patient is metabolically stable before any protein restriction is discussed.",
        "Calculate an energy and protein prescription and record the weight and guideline used.",
        "Describe what randomized trials show, and do not show, about low-protein and ketoanalogue-supplemented diets.",
        "Identify the patients in whom protein should not be restricted, including frail older adults.",
        "Build a plant-dominant, less processed eating pattern from familiar Filipino foods.",
    ],
    "big": """
{{plain:Protein in kidney disease is like fuel for a truck with a worn engine. Too rich a mixture strains the engine; too lean, and the truck starts burning its own frame. The dietitian sets the mixture for this engine, on this road, and checks the frame at every visit. Where the picture falls short: the &ldquo;frame&rdquo; is muscle, and it is also lost to acidosis and inflammation even when the fuel is right.}}
{{cards:Key terms for this module|Metabolically stable::No active inflammatory or infectious illness, no hospital stay in the past two weeks, no poorly controlled diabetes or wasting cancer, no recent significant weight loss, and not on high-dose steroids.|Low-protein diet (LPD)::About 0.55 to 0.60 g of protein per kg per day.|Very low-protein diet (VLPD)::About 0.28 to 0.43 g/kg/day, always with ketoanalogue or essential amino acid supplements.|Ketoanalogues::Nitrogen-free versions of essential amino acids; the body adds nitrogen from its own waste to complete them.|High biological value protein::Protein with all essential amino acids in good proportion, such as egg, fish, meat, milk, and soy.|Plant-dominant diet::A pattern in which more than half the protein comes from plants.|Ultra-processed food::Industrial formulations with additives, such as instant noodles, processed meats, and sweetened drinks.}}
{{flow:Order of work|Stability::Is the patient metabolically stable and eating enough?|Weight::Which weight, and why?|Energy first::Without enough energy, protein is burned as fuel.|Protein second::Which guideline, which target, which sources?|Pattern::More plants, fewer ultra-processed foods.|Review::Weight, intake, function, and laboratory results at a set date.}}
""",
    "case": {"title": "Two guidelines, one patient", "html": """
<p>Mr. Santos, 58, has CKD G4 A2 from hypertension. He does not have diabetes. He weighs 60 kg with no edema, his weight has been steady for a year, and he walks to the market daily. A food record shows about 75 g of protein a day, mostly pork and processed meats, and about 1,650 kcal.</p>
<p>His nephrologist writes: &ldquo;Protein restriction per dietitian.&rdquo; The clinic normally follows KDIGO. A supervised low-protein pathway with ketoanalogues is available, at his own expense.</p>
""", "questions": ["What is his protein target under KDIGO 2024, and under KDOQI 2020?",
                  "What must be true before a lower target is offered?",
                  "What would you change first on his plate?"]},
    "sections": [
        ("guidelines", "Guidelines", "Three guidelines, three numbers", """
<p>To understand protein in kidney disease, start with a healthy adult. The recommended intake for healthy adults is about 0.8 g of protein per kilogram of body weight a day. Most Filipino adults with chronic kidney disease (CKD) eat more than that, often 1.2 g/kg/day or above, much of it as pork and processed meat.</p>
<p>All the major guidelines agree on one thing: in CKD that is getting worse, very high protein intake should be avoided. They disagree on how low to go. They read the same trials, but they weigh the benefit of slowing the kidney disease differently against the risk of losing muscle.</p>
<div class="table-wrap"><table>
<thead><tr><th>Guideline</th><th>What it says for adults with CKD G3 to G5, not on dialysis</th><th>How firm</th></tr></thead>
<tbody>
<tr><td>Kidney Disease: Improving Global Outcomes (KDIGO) 2024</td><td>Keep protein at 0.8 g/kg/day. In adults at risk of progression, avoid more than 1.3 g/kg/day. A very low-protein diet with ketoanalogues may be offered to willing, able adults, with close supervision.</td><td>0.8 g/kg/day is a weak suggestion (grade 2C). The rest is advice without a formal grade.</td></tr>
<tr><td>Kidney Disease Outcomes Quality Initiative (KDOQI) 2020, without diabetes</td><td>In stable adults, under close supervision, 0.55 to 0.60 g/kg/day, or 0.28 to 0.43 g/kg/day with ketoanalogues.</td><td>A firm recommendation (grade 1A).</td></tr>
<tr><td>KDOQI 2020, with diabetes</td><td>0.6 to 0.8 g/kg/day is reasonable.</td><td>Expert opinion.</td></tr>
<tr><td>American Diabetes Association 2026 and KDIGO Diabetes 2022</td><td>Aim for 0.8 g/kg/day in diabetes with CKD not on dialysis.</td><td>KDIGO Diabetes: a weak suggestion (grade 2C).</td></tr>
</tbody></table></div>
<p>Sources: [[kdigo_ckd2024]][[kdoqi2020]][[ada2026]][[kdigo_dm2022]].</p>
<p>So which number do you use? Not the average. Choose one guideline with the nephrologist, write down which one, and write down why. For most patients in a general clinic, KDIGO&rsquo;s 0.8 g/kg/day is a sound starting point. It is the same as the healthy-adult intake, so it feels normal to patients, and because most of them arrive eating far more, reaching it is already a real change. The lower KDOQI range is for a smaller group: stable, well-nourished, motivated patients who can see a dietitian every one to three months.</p>
{{fig:rd04_protein_ladder}}
{{key:Quote each guideline&rsquo;s grade as it is written. KDOQI&rsquo;s 1A and KDIGO&rsquo;s 2C come from two panels using their own systems. One cannot be turned into the other.}}
<p><strong>Example from practice.</strong> Mrs. Dizon, 66, has type 2 diabetes and G3b A2 CKD. She weighs 55 kg without edema and eats about 77 g of protein a day, or 1.4 g/kg, mostly pork and longganisa. She has diabetes, so the KDOQI 0.55 to 0.60 g/kg range for people without diabetes does not apply. With her nephrologist you choose KDIGO Diabetes 2022: 0.8 g/kg/day, or about 44 g.[[kdigo_dm2022]][[ada2026]] Her note reads: &ldquo;Protein target 44 g/day (0.8 g/kg, edema-free weight 55 kg), KDIGO Diabetes 2022, grade 2C. Reduce in steps over 3 months; review weight and grip at each visit.&rdquo;</p>
"""),
        ("evidence", "Evidence", "What the trials show, and what they cannot", """
<p><strong>Low-protein diets.</strong> A Cochrane review pooled 17 trials in 2,996 adults without diabetes. Very low-protein diets probably reduced the number of people with CKD stage 4 or 5 who reached kidney failure. Ordinary low-protein diets may have made little difference to that outcome. Neither probably changed the risk of death. The trials told us little about muscle loss or quality of life.[[hahn2020]] In plain words: the evidence is strongest for the hardest diet to follow, and weakest for the moderate one.</p>
<p><strong>Ketoanalogues.</strong> In a single-center trial in Romania, 207 adults without diabetes, with eGFR below 30, were assigned for 15 months either to a vegetarian very low-protein diet (0.3 g/kg/day) with ketoanalogues or to a standard low-protein diet (0.6 g/kg/day). Fewer patients on the ketoanalogue diet needed dialysis or lost half their kidney function. About one patient was spared that outcome for every four to five treated.[[garneata2016]] Now look at who was in it. Only 14% of the patients screened were enrolled, and only after a three-month trial period that kept those who followed the diet and were well nourished. The result shows what is possible in ideal candidates. It does not tell you what to expect in an ordinary clinic.</p>
<p><strong>Older adults.</strong> Three cohorts, two in Spain and one in Sweden, followed 8,543 adults aged 60 and older. Among those with CKD, mostly stages 1 to 3, people who ate 1.0 g/kg/day of protein died less often than those who ate 0.8 g/kg/day (hazard ratio 0.88).[[carballo2024]] This was an observational study. Healthier people eat more, so it shows an association and does not prove that more protein prolongs life. It is still a good reason not to restrict protein in older adults who are frail or losing muscle, which is what KDIGO advises.</p>
<p><strong>Energy.</strong> KDOQI recommends 25 to 35 kcal/kg/day for stable adults with CKD, on dialysis, or after transplant, adjusted for age, sex, activity, body build, weight goals, and illness (a firm recommendation, grade 1C).[[kdoqi2020]] The reason is simple. Protein is kept for building and repair only when the body has enough energy from other foods. If energy is short, the body burns protein, from the plate first and then from muscle. A low-protein diet at 20 kcal/kg/day is a wasting diet.</p>
<p><strong>Example from practice.</strong> Two patients ask about the ketoanalogue diet in the same week. Mr. Fernandez, 50, has G4 CKD without diabetes. He is well nourished, has a stable weight, keeps detailed food records, and can pay for the tablets. Mrs. Lopez, 79, has G4 CKD. She lives alone and has lost 3 kg since the rainy season began. The trial population looks like Mr. Fernandez, who was screened, adherent, and well nourished.[[garneata2016]] It does not look like Mrs. Lopez. For her, the same diet risks wasting, and the benefit seen in the trial may never arrive.</p>
"""),
        ("who", "Who not to restrict", "Check stability before you restrict", """
<p>Protein restriction is a treatment for stable people with years ahead in which slowing progression matters. It is the wrong treatment for someone who is losing tissue now.</p>
{{cards:Do not lower protein when|Metabolically unstable::Acute infection, hospital stay in the past two weeks, uncontrolled diabetes, active cancer, high-dose steroids.|Already wasting::Unintentional weight loss, intake below need, low grip strength, or PEW criteria met.|Frail or sarcopenic and older::Function now outweighs progression years from now.|Starting dialysis soon or on dialysis::Needs rise to 1.0 to 1.2 g/kg/day (Module 9).|Pregnant, or a child::Refer; adult targets do not apply.|Heavy proteinuria with low albumin and edema::Discuss with the nephrologist; do not add a restriction on your own.}}
<p>For those who are suitable, a low-protein prescription needs four things in place: energy intake at target, at least half the protein from high biological value or well-combined plant sources, a review every one to three months with weight, intake, and grip strength, and a clear rule for stopping. Ketoanalogues are a prescription product; dosing and monitoring of calcium belong to the nephrologist.</p>
{{stop:If a patient on a low-protein diet loses weight without intending to, eats less than the energy target for two weeks, or becomes ill, stop the restriction, return to at least 0.8 g/kg/day, and tell the nephrologist the same day.}}
<p><strong>Example from practice.</strong> Mr. Castillo, 60, started a 0.6 g/kg diet with ketoanalogues three months ago at 62 kg. Today he weighs 59.5 kg, a 4% loss. Last week he had a urinary infection, and his food record shows about 1,300 kcal a day, near 21 kcal/kg, well below his target. Three stop signals are present: unintended weight loss, intake below the energy target, and illness. You return him to at least 0.8 g/kg/day, about 50 g, and you call the nephrologist that afternoon. The restriction can be offered again when he is stable.</p>
"""),
        ("pattern", "The plate", "From grams to a Filipino plate", """
<p>Beyond grams, the pattern of eating matters. KDIGO advises a healthy, diverse diet with more plant-based than animal-based foods and fewer ultra-processed foods (advice without a formal grade).[[kdigo_ckd2024]] KDOQI suggests a Mediterranean-style pattern, and more fruits and vegetables, in CKD stages 1 to 4 (a weak suggestion, grade 2C).[[kdoqi2020]] In the Chronic Renal Insufficiency Cohort, higher intake of ultra-processed foods was associated with faster CKD progression and higher mortality; the study is observational, and people who eat more processed food differ in income and health in ways that are hard to adjust for.[[sullivan2023]] The plant-dominant low-protein diet, 0.6 to 0.8 g/kg/day with more than half from plants, is an idea built on this physiology. No trial has yet tested whether it changes outcomes.[[plado2020]]</p>
<p>Why would plants help? Compared with processed meats, they bring less phosphorus that the body can absorb, less acid, more fiber, and less sodium. The usual worry is potassium, which Module 6 addresses; in most patients with normal potassium, vegetables do not need to be restricted.</p>
<div class="table-wrap"><table>
<thead><tr><th>Food (cooked, household measure)</th><th>Approximate protein</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Fish, meat, or chicken, one matchbox-size piece (about 30 g)</td><td>7 to 8 g</td><td>One meat exchange in the Philippine Food Exchange Lists</td></tr>
<tr><td>Egg, one medium</td><td>6 to 7 g</td><td>The yolk carries most of the phosphorus</td></tr>
<tr><td>Tofu (tokwa), about half a cup of cubes</td><td>7 to 8 g</td><td>Plant protein of high quality</td></tr>
<tr><td>Cooked mung beans (monggo), half a cup</td><td>about 7 g</td><td>Also carries potassium and fiber</td></tr>
<tr><td>Cooked rice, one cup</td><td>about 4 g</td><td>Three cups a day adds 12 g that patients forget to count</td></tr>
</tbody></table></div>
<p>These values are rounded teaching figures. Check the Philippine Food Composition Tables and the Food Exchange Lists for the food and preparation in front of you.[[philfct]][[fel2019]] In practice, most of the change comes from three moves: shrink the meat portion to one or two matchbox pieces per meal, replace processed meats with fresh fish, egg, or tofu, and keep the rice, vegetables, and cooking oil that supply energy.</p>
{{fig:rd04_plate}}
<p><strong>Example from practice.</strong> Turn Mrs. Dizon&rsquo;s 44 g into food. Three cups of rice give about 12 g, and her vegetables about 4 g. That leaves about 28 g for protein foods: one egg at breakfast (6 to 7 g), two matchbox-size pieces of fish at lunch (14 to 16 g), and half a cup of tokwa at dinner (7 to 8 g). The day comes to about 43 to 47 g, close to target. She keeps her rice, eats fish she likes, and drops the processed meat. The plate is smaller in pork and larger in vegetables, not a list of what she cannot eat.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What is his target under each guideline?</strong> Under KDIGO, 0.8 &times; 60 = 48 g a day. Under KDOQI&rsquo;s low-protein range, 0.55 to 0.60 &times; 60 = 33 to 36 g a day, with close supervision. For energy, KDOQI&rsquo;s 25 to 35 kcal/kg gives 1,500 to 2,100 kcal a day. His 1,650 kcal sits inside that range, and his steady weight says it is enough for now.</p>
<p><strong>Could he have the lower target?</strong> He could be offered it. He is stable, well nourished, active, and has not lost weight. But it needs four things: enough energy every day, a visit every one to three months, his own informed choice, and money for ketoanalogues if they are used. If he says no, 48 g a day is a sound, guideline-backed target, and it is already about a third less than the 75 g he eats now.</p>
<p><strong>What would you change first on his plate?</strong> The processed meats. They carry sodium and phosphate additives as well as protein, so one swap lowers three things. Replace them with fresh fish, egg, or tofu, about two matchbox-size pieces at lunch and dinner and one at breakfast, which comes to roughly 35 to 40 g of protein from those foods. Let rice and vegetables supply the rest. Keep the rice and the cooking oil so his energy does not fall.</p>
<p><strong>What goes in the note?</strong> The guideline you used, the 60 kg weight and why you used it, and a review in six to eight weeks with his weight and a repeat food record. The nephrologist wrote &ldquo;per dietitian.&rdquo; That is trust, and the note is how you show what you did with it.</p>
"""],
    "skills": {"title": "Writing a stable-CKD nutrition prescription",
               "intro": "Use a fictional patient card with stage, weight, a three-day food record, and laboratory results.",
               "items": [
                   ("Screens for metabolic instability, poor intake, and frailty before discussing restriction.", True),
                   ("States the weight used for calculation and the reason.", False),
                   ("Calculates energy and protein in kcal/day and g/day, with units.", False),
                   ("Names the guideline chosen and quotes its grade as written.", False),
                   ("Explains to the preceptor why the KDIGO and KDOQI targets differ and why they are not averaged.", False),
                   ("Converts the protein target into household portions using the patient&rsquo;s usual foods.", False),
                   ("Checks that the plan still meets the energy target.", True),
                   ("Sets a review date with weight, intake, and function, and states the rule for stopping a restriction.", False),
               ],
               "placement": "For one supervised patient, write the prescription twice, once under KDIGO and once under KDOQI, and discuss with your preceptor which fits and why."},
    "quiz": [
        ("Under KDIGO 2024, the suggested protein intake for an adult with CKD G4 who weighs 60 kg is:",
         ["33 to 36 g/day", "48 g/day", "60 to 72 g/day", "78 g/day"], 1,
         "0.8 g/kg/day × 60 kg = 48 g/day (a weak suggestion, grade 2C)."),
        ("Under KDOQI 2020, the low-protein range for a metabolically stable 60 kg adult with CKD stage 4 without diabetes is:",
         ["33 to 36 g/day", "48 g/day", "60 to 72 g/day", "17 to 26 g/day without supplements"], 0,
         "0.55 to 0.60 g/kg/day × 60 kg = 33 to 36 g/day, under close clinical supervision (a firm recommendation, grade 1A)."),
        ("The KDOQI energy recommendation for metabolically stable adults with CKD is:",
         ["15 to 20 kcal/kg/day", "25 to 35 kcal/kg/day", "40 to 45 kcal/kg/day", "A fixed 2,000 kcal/day"], 1,
         "25 to 35 kcal/kg/day, individualized (a firm recommendation, grade 1C)."),
        ("Why must energy be adequate before protein is lowered?",
         ["Energy raises eGFR", "Without enough energy, dietary and body protein are used as fuel", "Energy lowers potassium", "It is not important"], 1,
         "Protein is spared for tissue maintenance only when energy needs are met."),
        ("Which patient should NOT be offered a low-protein diet?",
         ["A stable, well-nourished 55-year-old with G4 CKD", "A 79-year-old with G3b CKD, weight loss, and slow gait", "A motivated 60-year-old with steady weight", "A patient who asks about ketoanalogues"], 1,
         "Frailty with weight loss calls for protecting intake; KDIGO suggests considering higher targets in such patients."),
        ("In the ketoanalogue trial by Garneata and colleagues, what limits applying the result widely?",
         ["It was not randomized", "Only 14% of screened patients were randomized after a run-in selecting adherent, well-nourished people", "It lasted one week", "It included only patients on dialysis"], 1,
         "The trial shows what is achievable in highly selected patients."),
        ("The Cochrane review of low-protein diets in adults without diabetes concluded that:",
         ["Low-protein diets clearly reduce death", "Very low-protein diets probably reduce progression to kidney failure; effects on death are probably nil", "All protein restriction is harmful", "No trials exist"], 1,
         "The benefit was seen for very low-protein diets in stages 4 to 5; mortality was probably not affected."),
        ("An observational study finds that older adults with CKD who eat more protein die less often. The best reading is:",
         ["More protein is proven to prolong life", "The association may be partly explained by healthier people eating more; it supports not restricting frail older adults", "The study should be ignored", "Protein should be unlimited"], 1,
         "Association is not causation; confounding by health status is likely."),
        ("&ldquo;Metabolically stable&rdquo; excludes a patient who:",
         ["Has had steady weight for a year", "Was discharged from hospital five days ago after pneumonia", "Walks daily", "Has controlled blood pressure"], 1,
         "A recent hospital stay for acute illness means the patient is not stable."),
        ("KDIGO&rsquo;s advice to avoid more than 1.3 g/kg/day in adults at risk of progression is a:",
         ["Grade 1A recommendation", "Practice point without a formal grade", "Legal requirement", "KDOQI statement"], 1,
         "It is an ungraded practice point."),
        ("One cup of cooked rice provides about how much protein?", ["0 g", "4 g", "10 g", "15 g"], 1,
         "About 4 g per cup; three cups add about 12 g a day."),
        ("Which first change addresses protein, sodium, and phosphate additives together?",
         ["Removing rice", "Replacing processed meats with fresh fish, egg, or tofu", "Stopping all vegetables", "Drinking more water"], 1,
         "Processed meats carry all three; fresh sources lower them without lowering energy."),
        ("A patient on a supervised low-protein diet develops pneumonia and eats poorly. You should:",
         ["Continue the diet strictly", "Stop the restriction, return to at least 0.8 g/kg/day, and inform the nephrologist", "Lower protein further", "Stop all food records"], 1,
         "Restriction is for stable patients; illness raises needs and the risk of wasting."),
        ("The plant-dominant low-protein diet is best described as:",
         ["Proven in large outcome trials", "An idea built on physiology, not yet tested in an outcome trial", "A KDIGO grade 1A recommendation", "A very low-protein diet"], 1,
         "It rests on physiology; outcome trials have not yet been done."),
        ("For an adult with diabetes and CKD not on dialysis, the American Diabetes Association and KDIGO Diabetes guideline advise aiming for:",
         ["0.3 g/kg/day", "0.8 g/kg/day", "1.5 g/kg/day", "No target"], 1,
         "Both advise 0.8 g/kg/day; lower intakes are not recommended in diabetes."),
    ],
    "terms": [("Nitrogen balance", "Protein nitrogen eaten minus nitrogen lost; negative balance means tissue is being lost."),
              ("Number needed to treat", "How many patients must be treated for one to benefit."),
              ("Confounding", "A third factor that explains an association between two others."),
              ("Food exchange", "A portion of food with a defined energy and protein content, used for meal planning."),
              ("Practice point", "Guidance from a guideline panel that has no formal evidence grade."),
              ("Frailty", "Reduced strength, endurance, and reserve that raises the risk of harm from stress.")],
    "readings": [("ketoanalogue-supplementation.html", "How ketoanalogues work, for patients and clinicians."),
                 ("plant-forward-renal-diet.html", "A plant-forward kidney diet in Filipino foods."),
                 ("hold-ketoanalogue-until-nephrology-review.html", "Why ketoanalogues need a nephrologist&rsquo;s review first.")],
    "calcs": ["calc-ckd-nutrition-rx.html", "calc-energy-expenditure.html", "calc-ketoanalogue-dose.html", "calc-ketoanalogue-plan-check.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
