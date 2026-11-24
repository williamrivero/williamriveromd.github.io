# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 05: Sodium, Fluid, and Volume. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient and dietitian reading the label on an instant noodle packet beside bottles of fish sauce and soy sauce.",
    "objectives": [
        "Convert between sodium and salt, and between milligrams and millimoles.",
        "State the KDIGO and KDOQI sodium recommendations with their grades and the main exception.",
        "Estimate sodium from a label, a recipe, and table condiments, including broth and second servings.",
        "Calculate interdialytic weight gain as kilograms and as a percentage, and interpret it with the interval and symptoms.",
        "Explain why salt substitutes containing potassium chloride need individual review in kidney disease.",
        "Recognize the volume findings that need urgent medical assessment.",
    ],
    "big": """
{{plain:Salt is a sponge for water. Every teaspoon of salt a person without kidney function eats will hold about a liter of water in the body until dialysis removes it, and the thirst it causes is the body asking for that water. Asking a patient to drink less while the salt stays the same is asking him to ignore thirst for two days. The sponge picture is close to the truth: sodium holds water outside the cells, where it raises blood pressure and fills the lungs.}}
{{cards:Key terms for this module|Sodium (Na)::The mineral in salt that holds water outside cells. Labels list it in milligrams.|Salt (sodium chloride)::About 40% sodium by weight. 1 g of sodium equals about 2.5 g of salt.|Interdialytic weight gain (IDWG)::Weight gained between two dialysis sessions; almost all of it is fluid.|Dry weight::The post-dialysis weight at which the patient has no excess fluid. Set by the nephrologist.|Residual kidney function::Urine the patient still makes. It allows more fluid and should be protected.|Ultrafiltration rate::How fast fluid is removed during dialysis, in mL per kg per hour.|Salt substitute::A product that replaces some sodium chloride with potassium chloride.}}
{{flow:Teach in this order|Find the sodium::Condiments, broth, instant and processed foods.|Change one source::The one the family agrees to change.|Then discuss fluid::Only if weight gains or symptoms call for it.|Check::Weight gain, blood pressure, thirst, and whether meals are still enjoyed.}}
""",
    "case": {"title": "The whole packet", "html": """
<p>Mr. Lim, 54, dialyzes twice a week, on Monday and Thursday, and makes about one glass of urine a day. On Monday his pre-dialysis weight is 66.5 kg. His post-dialysis weight last Thursday was 64.0 kg. He feels well.</p>
<p>He eats instant noodles most evenings. The label (fictional) lists 720 mg of sodium per serving and two servings per packet; he eats the whole packet with the broth. He also keeps patis on the table. The nurse asks you to &ldquo;put him on a one-liter fluid restriction.&rdquo;</p>
""", "questions": ["How much sodium is in his noodle dinner, and what share of a 2,000 mg day is that?",
                  "What is his weight gain in kilograms and as a percentage, and over how many days?",
                  "What would you teach first, and what symptom would change today&rsquo;s visit into an urgent one?"]},
    "sections": [
        ("numbers", "The numbers", "Sodium arithmetic and the guideline targets", """
<p>Labels list sodium; cooks think in salt; some laboratory and urine reports use millimoles. Learn three conversions and you can move between them.</p>
{{formula:Salt (g) = sodium (g) &times; 2.5 &nbsp;&middot;&nbsp; Sodium (mmol) = sodium (mg) &divide; 23 &nbsp;&middot;&nbsp; One level teaspoon of salt is about 5 g of salt, or about 2,000 mg of sodium.}}
<p>Two guidelines set the target, and they are close. KDIGO suggests less than 2 g of sodium a day for people with CKD, which is less than 90 mmol, or about 5 g of salt (a weak suggestion, grade 2C).[[kdigo_ckd2024]] KDOQI recommends less than 2.3 g a day, or 100 mmol, to lower blood pressure and help control fluid (a firm recommendation, grade 1B, in CKD stages 3 to 5; grade 1C on dialysis).[[kdoqi2020]] KDIGO adds one exception: people whose kidneys waste sodium usually should not be restricted. They are uncommon, and the nephrologist will tell you who they are.</p>
<p>How good is the evidence? A Cochrane review pooled 21 randomized trials in people with CKD. Cutting sodium by about 1,700 mg a day lowered blood pressure by about 7/4 mm Hg, and the reviewers were highly confident of that result. Albuminuria fell too, in earlier stages. But the trials lasted only 1 to 36 weeks, too short to show whether fewer people reached dialysis, had a stroke, or died.[[mcmahon2021]] The same review found that some patients on lower salt had symptomatic low blood pressure. When a patient on several blood pressure medicines makes a big change, tell the team.</p>
{{key:A target of 2,000 mg of sodium is about one level teaspoon of salt for the whole day, from all sources: cooking, the table, and what is already inside processed food.}}
<p><strong>Example from practice.</strong> Mrs. Ramirez buys canned corned beef. The label (fictional) gives 780 mg of sodium per serving and three servings per can, and the family of three shares one can. Her serving: 780 mg sodium &times; 2.5 = about 2.0 g of salt, or 780 &divide; 23 = 34 mmol. That is 39% of a 2,000 mg target in one portion. Her 24-hour urine sodium is 180 mmol, which is about 4,100 mg of sodium or 10 g of salt a day, double the target. The urine shows the whole day; the label shows where the first big piece comes from.</p>
"""),
        ("sources", "Finding sodium", "Where the sodium is in a Filipino diet", """
<p>In home cooking, most sodium comes from a short list: table salt, patis (fish sauce), toyo (soy sauce), bagoong, bouillon cubes and seasoning granules, and sinigang or other soup mixes. A tablespoon of patis or toyo often carries 1,000 mg of sodium or more, half a day&rsquo;s allowance; brands differ, so read the label. Outside the home, the main sources are instant noodles, canned goods, processed meats such as tocino, longganisa, hotdog, and ham, dried and salted fish, chips, and fast food.</p>
{{cards:Four habits that hide sodium|Sawsawan::A dipping saucer refilled through the meal. Ask how many times, and measure one refill.|Broth::Soup dissolves the seasoning. A second bowl of sabaw can double the sodium of the dish.|The whole packet::Many labels give values per serving, with two or more servings in the pack.|Seasoning stacked on seasoning::Bouillon plus patis plus soup mix in one pot.}}
<p>To estimate a recipe, add the sodium of every seasoning that went into the pot, divide by the number of servings, and then adjust for the person who takes extra broth. State the uncertainty; you are estimating, not measuring. The site&rsquo;s label scanner and recipe analyzer can do the arithmetic, and Module 15 practices it by hand.[[philfct]]</p>
<p>Flavor does not have to fall with sodium. Calamansi, vinegar, garlic, onion, ginger, tomato, lemongrass, pepper, and chili carry a dish when salt is reduced, and taste adapts to lower salt within a few weeks if the change is gradual.</p>
{{fig:rd05_sodium_sources}}
<p><strong>Example from practice.</strong> Mrs. Salazar, 61, has G3b CKD. She says she &ldquo;never adds salt.&rdquo; Using the labels in her kitchen (fictional values), you add up her Tuesday. Sinigang mix, 2,400 mg in a pot for six: 400 mg. Patis in the pot, 1,200 mg for six: 200 mg. The sawsawan of patis, refilled twice at about a teaspoon each, about 400 mg per refill: 800 mg. Instant pancit canton for merienda: 1,100 mg. The total is about 2,500 mg before counting any salt in the food itself. The largest item was the sawsawan, the one thing she did not think of as salt.</p>
"""),
        ("substitutes", "Salt substitutes", "Salt substitutes: good evidence, wrong population", """
<p>Salt substitutes replace part of the sodium chloride with potassium chloride. In a large randomized trial in rural China, among about 21,000 people with prior stroke or aged 60 and older with high blood pressure, a substitute of 75% sodium chloride and 25% potassium chloride lowered the rate of stroke (rate ratio 0.86), major cardiovascular events, and death over about five years, without a detectable increase in serious hyperkalemia.[[neal2021]]</p>
<p>That is strong evidence for the general hypertensive population. It does not transfer to your patients, because people with serious kidney disease and those taking potassium-sparing medicines were excluded from the trial. Potassium chloride is absorbed almost completely, and a kidney that cannot excrete potassium, or a patient on an angiotensin receptor blocker or spironolactone, may not handle it.[[clase2020]]</p>
{{stop:Ask every patient with CKD, on dialysis, or after transplant whether a &ldquo;low-sodium salt,&rdquo; &ldquo;lite salt,&rdquo; or &ldquo;heart salt&rdquo; is used at home, and read the ingredient list for potassium chloride. Do not recommend one yourself. If a patient wants to use one, the nephrologist decides, with a potassium check.}}
<p><strong>Example from practice.</strong> Mr. Pascual, 67, makes no urine and dialyzes three times a week. His potassium has risen from 5.4 to 6.3 mmol/L over two months. His dialysis and his diet have not changed. His daughter bought a &ldquo;lite salt&rdquo; for his blood pressure. The label says it is half potassium chloride. Potassium chloride is about 52% potassium, so half a teaspoon of that salt, about 2.5 g, carries about 650 mg of potassium, more than a medium banana, and nearly all of it is absorbed. You tell the nephrologist and ask the family to set the salt aside until he decides.[[clase2020]]</p>
"""),
        ("fluid", "Fluid and volume", "Fluid: individualize, then measure", """
<p>Not every patient with kidney disease needs a fluid limit. Most patients with CKD who still pass urine normally should drink to thirst. A fluid limit is for patients who retain water: those on dialysis with little or no urine, and those with heart failure or low serum sodium as directed by the physician. For a patient on hemodialysis, a common starting rule is the previous day&rsquo;s urine volume plus about 500 to 750 mL, adjusted by the nephrologist to weight gain, blood pressure, and climate; it is a rule of thumb and not a graded recommendation.</p>
<p><strong>Interdialytic weight gain.</strong> Compare today&rsquo;s pre-dialysis weight with the last post-dialysis weight, and note the number of days between.</p>
{{formula:IDWG (kg) = pre-dialysis weight &minus; previous post-dialysis weight. IDWG (%) = IDWG &divide; dry weight (or previous post-dialysis weight) &times; 100.}}
<p>Many units aim to keep gains below about 4% to 4.5% of dry weight, because larger gains mean higher blood pressure before dialysis and faster fluid removal during it. Faster ultrafiltration is associated with low blood pressure during dialysis, cramps, and higher mortality in observational studies, and KDIGO&rsquo;s conference on volume management advises counseling on sodium as the first step in limiting gains, with targets individualized.[[flythe2020]] The percentage thresholds are convention, not trial-proven cut-offs. In the Philippines many patients dialyze twice a week, so the interval is three or four days and the same daily intake produces a larger gain; interpret the number against the interval, the urine output, and the symptoms.</p>
<p>A very low gain is not always good news. A patient who gains almost nothing and is losing weight may simply not be eating. Read IDWG together with the food record.</p>
{{cards:Practical fluid tools|Count what counts::Water, coffee, juice, soup, lugaw, ice, gelatin, and watery fruit.|One measured bottle::Fill a marked bottle each morning; when it is empty, the day&rsquo;s drinking is done.|For thirst::Lower the sodium first. Then small sips, ice chips counted as fluid, rinsing without swallowing, sugar-free gum, and good glucose control.|In hot weather::Ask the nephrologist whether the limit changes; sweat losses rise.}}
{{fig:rd05_idwg}}
{{stop:New breathlessness at rest or when lying flat, a sudden large weight gain, chest pain, or oxygen saturation below the unit&rsquo;s threshold is not a counseling problem. Call the nurse and the physician on duty now.}}
<p><strong>Example from practice.</strong> Mrs. Gatchalian, 55 kg dry weight, dialyzes on Tuesdays and Fridays and still passes about 600 mL of urine a day. Her gain is 2.4 kg over the three-day gap (4.4%) and 3.0 kg over the four-day gap (5.5%). Both are about 0.75 to 0.8 kg a day, the same habit spread over different intervals. A starting allowance of her urine plus 500 to 750 mL would be 1,100 to 1,350 mL a day. The first thing you change, though, is the tuyo at breakfast and the patis at lunch, because they drive her thirst. Contrast Mr. Uy in the next chair, who gains only 0.5 kg and whose post-dialysis weight has fallen 2 kg in a month. His small gain is a sign that he is not eating.</p>
"""),
    ],
    "debrief": ["""
<p><strong>How much sodium is in the noodle dinner?</strong> Two servings &times; 720 mg = 1,440 mg. That is 72% of a 2,000 mg day in one bowl, before any patis from the table.</p>
<p><strong>How much did he gain, and over how long?</strong> 66.5 &minus; 64.0 = 2.5 kg, which is 2.5 &divide; 64.0 &times; 100 = 3.9%. It built up over four days, Thursday to Monday, and he still passes about a glass of urine a day. For that interval, it is a moderate gain. He has no symptoms.</p>
<p><strong>Should you start a one-liter fluid limit?</strong> Not yourself, and not first. A fluid prescription belongs to the nephrologist. And a fluid limit without a salt change will fail, because the noodles will keep him thirsty. Pass the nurse&rsquo;s request on, with your findings.</p>
<p><strong>What would you teach first?</strong> The sodium. Offer him choices: use half the seasoning sachet, leave the broth, or swap three noodle dinners a week for rice, fresh fish, and a vegetable with calamansi and garlic. Ask him to measure his patis with a teaspoon for one week. Check his weight gain and thirst in two weeks.</p>
<p><strong>What would make this visit urgent?</strong> New breathlessness at rest or when lying flat. Then you stop the counseling and call the nurse and the physician on duty. The nurse saw a fluid problem. You found the salt behind it. The nephrologist decides what to prescribe. That is how the three roles fit together.</p>
"""],
    "skills": {"title": "Sodium estimate and volume-aware counseling",
               "intro": "Materials: two food labels, a household recipe card, a teaspoon and tablespoon, and a fictional dialysis record.",
               "items": [
                   ("Reads serving size and servings per pack and calculates sodium for the amount actually eaten.", False),
                   ("Converts sodium to salt and to teaspoons for the patient.", False),
                   ("Estimates sodium per serving of a recipe and states the uncertainty from broth and second servings.", False),
                   ("Asks about table condiments, refills, and food eaten outside the home.", False),
                   ("Checks the ingredient list of any salt substitute for potassium chloride and refers the question to the nephrologist.", True),
                   ("Calculates interdialytic weight gain in kg and percent with the correct weights and states the interval.", False),
                   ("Teaches sodium before fluid and does not set a fluid limit independently.", True),
                   ("Recognizes resting breathlessness as urgent and calls the nurse and physician.", True),
                   ("Agrees on one change chosen by the patient and sets a review date.", False),
               ],
               "placement": "With permission, review three patients&rsquo; weight gains over one month with the charge nurse and note which gains followed a long interval."},
    "quiz": [
        ("A label lists 720 mg of sodium per serving and two servings per packet. A patient eats the whole packet. Sodium eaten is:",
         ["360 mg", "720 mg", "1,440 mg", "2,880 mg"], 2,
         "Two servings × 720 mg = 1,440 mg."),
        ("2 g of sodium is about how much salt?", ["2 g", "5 g", "10 g", "23 g"], 1,
         "Sodium × 2.5 = salt; 2 g of sodium is about 5 g of salt, one level teaspoon."),
        ("KDIGO 2024 suggests a sodium intake for people with CKD of:",
         ["Less than 1 g/day", "Less than 2 g/day", "Less than 4 g/day", "No limit"], 1,
         "Less than 2 g of sodium a day (a weak suggestion, grade 2C)."),
        ("The KDOQI 2020 sodium statement is:",
         ["Less than 2.3 g/day", "Less than 0.5 g/day", "At least 5 g/day", "Not stated"], 0,
         "Less than 2.3 g (100 mmol) a day; grade 1B in CKD stages 3 to 5 and 1C on dialysis."),
        ("What did the Cochrane review of salt reduction in CKD establish with high certainty?",
         ["Fewer deaths", "Lower blood pressure", "Less dialysis", "Fewer strokes"], 1,
         "Blood pressure fell by about 7/4 mm Hg. Trials were too short for hard outcomes."),
        ("Pre-dialysis weight 66.5 kg; previous post-dialysis weight 64.0 kg. The gain is:",
         ["1.5 kg (2.3%)", "2.5 kg (3.9%)", "2.5 kg (3.8% of 66.5)", "3.5 kg (5.5%)"], 1,
         "66.5 − 64.0 = 2.5 kg; 2.5 ÷ 64.0 × 100 = 3.9%."),
        ("Why should sodium be taught before fluid?",
         ["Sodium is easier to measure", "Sodium drives thirst; lowering it makes a fluid limit achievable", "Fluid does not matter", "Guidelines forbid fluid advice"], 1,
         "Thirst follows sodium intake."),
        ("A patient on twice-weekly dialysis has the same daily intake as one on thrice-weekly dialysis. His weight gain per interval will be:",
         ["Smaller", "The same", "Larger, because the interval is longer", "Zero"], 2,
         "Gain accumulates over more days."),
        ("A salt substitute lists potassium chloride. For a patient with CKD G4 on losartan, you should:",
         ["Recommend it freely", "Not recommend it; refer the question to the nephrologist", "Double the amount", "Ignore it"], 1,
         "Potassium chloride is fully absorbed, and the trial evidence excluded people with serious kidney disease."),
        ("The large salt-substitute trial showed fewer strokes in:",
         ["Patients on dialysis", "Older adults with hypertension or prior stroke, excluding serious kidney disease", "Children", "Transplant recipients"], 1,
         "The benefit applies to the population studied, which excluded those at risk of hyperkalemia."),
        ("Which patient most likely does NOT need a fluid limit?",
         ["Anuric patient on hemodialysis", "CKD G3a with normal urine output and no edema", "Heart failure with low sodium", "Peritoneal dialysis with poor ultrafiltration"], 1,
         "Patients who pass urine normally and have no fluid retention should drink to thirst."),
        ("Very low weight gains with falling post-dialysis weight suggest:",
         ["Excellent adherence", "Poor food intake", "Too much salt", "A scale error only"], 1,
         "Little food means little sodium and fluid; check the food record."),
        ("Which counts toward a fluid allowance?",
         ["Lugaw and soup", "Dry bread", "Grilled fish", "Boiled egg"], 0,
         "Liquids and foods that are liquid at room temperature count."),
        ("Which finding makes a visit urgent?",
         ["A preference for soup", "New breathlessness at rest", "An unlabeled recipe", "Mild thirst"], 1,
         "Resting breathlessness may be pulmonary edema and needs immediate assessment."),
        ("Who sets the dry weight and the fluid prescription?",
         ["The dietitian", "The patient&rsquo;s family", "The nephrologist", "The technician"], 2,
         "The dietitian contributes intake and weight data; the nephrologist decides."),
    ],
    "terms": [("Sawsawan", "A dipping sauce at the table, usually patis, toyo, or bagoong with calamansi or vinegar."),
              ("Sabaw", "Broth."),
              ("Pulmonary edema", "Fluid in the lungs, felt as breathlessness, worse lying flat."),
              ("Anuric", "Passing no urine, or almost none."),
              ("Sodium-wasting", "A kidney condition in which too much sodium is lost in urine."),
              ("Rate ratio", "The event rate in one group divided by the rate in another.")],
    "readings": [("sodium-salt-reduction-ckd.html", "A patient guide to lowering sodium."),
                 ("fluid-management-dialysis.html", "Fluid, thirst, and weight gain on dialysis."),
                 ("el-nino-heat-dialysis.html", "Fluid and heat for dialysis patients."),
                 ("ckd-label-scanner.html", "A label-reading tool for patients.")],
    "calcs": ["calc-sodium-intake.html", "calc-idwg-fluid.html", "calc-ufr-ceiling.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
