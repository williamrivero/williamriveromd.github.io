# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 10: Medical Nutrition Therapy in Peritoneal Dialysis. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient at home performing a peritoneal dialysis exchange beside a small dining table with a light meal.",
    "objectives": [
        "Explain how glucose is absorbed from peritoneal dialysis (PD) fluid and count it as energy.",
        "Explain why protein needs stay high on PD and rise during peritonitis.",
        "Manage early fullness and poor appetite around the exchange schedule.",
        "Recognize low potassium as common on PD and say what the evidence shows about treating it.",
        "Know which glucose meters give false readings with icodextrin.",
        "Recognize cloudy fluid and abdominal pain as reasons to call the PD team at once.",
    ],
    "big": """
{{plain:Peritoneal dialysis uses the lining of the belly as the filter. Sugar water is placed inside, and over hours, waste and water move from the blood into it. But the traffic goes both ways. Some of the sugar moves into the blood and becomes energy, and some of the patient&rsquo;s protein moves out into the bag. A PD patient is being fed sugar and drained of protein around the clock.}}
{{cards:Key terms for this module|Peritoneal dialysis (PD)::Dialysis using the lining of the abdomen (peritoneum), done at home.|Exchange::Draining used fluid and filling fresh fluid. Four a day in continuous ambulatory PD.|Automated PD (APD)::A machine performs exchanges at night.|Dextrose concentration::How much glucose is in the fluid, such as 1.5%, 2.5%, or 4.25%. Stronger fluid removes more water and gives more glucose.|Icodextrin::A starch-based PD fluid used for the long dwell; it releases maltose into the blood.|Peritonitis::Infection of the peritoneum; the first sign is often cloudy drained fluid.|Effluent::The fluid drained out after a dwell.}}
{{flow:Order of work on PD|Schedule::Which fluids, how many exchanges, which strengths.|Hidden energy::Glucose absorbed from the fluid.|Protein::Losses into the fluid, and appetite.|Potassium::Often low, not high.|Glucose meters::Safe with icodextrin?|Red flags::Cloudy fluid or belly pain goes to the PD team now.}}
""",
    "case": {"title": "Full by dinner", "html": """
<p>Mrs. Villanueva, 58, has been on continuous ambulatory PD for eight months. She weighs 60 kg. The PD nurse estimates she absorbs about 80 g of glucose a day from her dialysis fluid. The team puts her total energy need at 1,800 kcal a day.</p>
<p>She says she feels full and bloated by dinner and eats little. Her potassium has fallen from 4.2 to 3.4 mmol/L over three months. She asks if she should still avoid bananas, as her old diet sheet says. While you are talking, she mentions that this morning&rsquo;s drained fluid looked &ldquo;a bit cloudy.&rdquo;</p>
""", "questions": ["What should you do about the cloudy fluid, and when?",
                  "How much energy is she getting from her dialysis fluid, and what is left for food?",
                  "What would you say about bananas?"]},
    "sections": [
        ("glucose", "Hidden energy", "Count the glucose in the bag", """
<p>PD fluid contains glucose so that water will move from the blood into the belly. Over a dwell, part of that glucose crosses into the blood. In a classic study of patients on continuous ambulatory PD, net absorption averaged about 180 g of glucose a day, about 8 kcal per kg of body weight a day, or 12% to 34% of total energy intake.[[grodstein1981]] The amount depends on the strength of the fluid, the number of exchanges, and how fast the patient&rsquo;s membrane transports solutes.</p>
{{formula:Energy from dialysate (kcal/day) = absorbed glucose (g/day) &times; kcal per gram. Example: 80 g &times; 3.4 kcal/g = 272 kcal. Food energy target = 1,800 &minus; 272 = about 1,528 kcal/day. Use the kcal-per-gram value your PD team uses (3.4 for glucose monohydrate is common) and write it in the note.}}
<p>The absorbed glucose is ordinary energy. In a thin patient it helps. In a patient with diabetes or obesity it raises glucose, weight, and blood fats. KDOQI advises counting dialysate energy as part of total intake (expert opinion).[[kdoqi2020]] Ask the PD team for their estimate rather than guessing, and recheck it when the fluid strengths change. The figure is an estimate; the patient&rsquo;s weight trend tells you whether the plan is right.</p>
{{fig:rd10_glucose}}
<p><strong>Example from practice.</strong> Mr. Corpuz, 72 kg, has diabetes and does four CAPD exchanges a day. The PD team estimates he absorbs about 120 g of glucose a day: 120 &times; 3.4 = about 410 kcal. His team-set energy target is 1,900 kcal, so food should supply about 1,490 kcal. Last month one exchange was changed to a stronger fluid because he was retaining water. His absorbed glucose rose, and so did his afternoon glucose readings. You ask the PD team for a new estimate and tell the diabetes team why his glucose changed.</p>
"""),
        ("protein", "Protein and appetite", "Protein out, fullness in", """
<p>Protein crosses the membrane too. A stable PD patient loses about 5 to 15 g of protein a day into the fluid, mostly albumin, and much more during peritonitis. That is why KDOQI applies the same 1.0 to 1.2 g/kg/day protein advice to PD as to HD (expert opinion).[[kdoqi2020]] The International Society for Peritoneal Dialysis (ISPD) advises that PD care be goal-directed, with nutrition and appetite reviewed as part of how well the patient lives, not only by laboratory numbers.[[ispd2020]]</p>
<p>Two things work against eating. The fluid in the belly, often 2 liters, presses on the stomach and causes early fullness. And the steady glucose supply blunts appetite.</p>
{{cards:Practical ideas for early fullness|Small, frequent meals::Five or six small meals instead of three large ones.|Protein first::Eat the fish, egg, or chicken before the rice.|Timing with drains::Eat soon after a drain, when the belly is emptier, if the routine allows.|Fewer drinks with meals::Drink between meals, not during them.|Report persistent bloating::Constipation and a full belly make each other worse, and both can disturb drainage. Tell the PD nurse.}}
<p>You do not change the exchange schedule or fluid strengths. Those belong to the nephrologist and the PD team. You can tell them which part of the day is hardest for eating and ask whether anything can be adjusted.</p>
<p><strong>Example from practice.</strong> Mrs. Pangilinan, 55 kg, on PD, needs 55 to 66 g of protein a day. Her fluid alone removes perhaps 5 to 15 g. She eats about 40 g and says she is &ldquo;full of water&rdquo; by noon. You build five small meals. Breakfast after her morning drain: an egg and a pandesal. Ten o&rsquo;clock: a small piece of fish. Lunch: fish first, then a half cup of rice. Mid-afternoon: tokwa. Dinner: chicken before the rice. The same food in five portions fits around her belly, and after three weeks she is eating about 55 g. If she develops peritonitis, the losses rise and the plan must be reviewed.</p>
"""),
        ("potassium", "Potassium", "On PD, potassium is more often low than high", """
<p>PD runs all day, and the fluid contains no potassium, so potassium is removed continuously. Many PD patients have low or low-normal potassium, especially if they eat poorly. Low potassium slows the bowel and may make it easier for gut bacteria to cross into the peritoneum.</p>
<p>A randomized trial in Thailand tested this. 167 PD patients with low potassium were assigned either to a protocol of oral potassium to keep the level at 4 to 5 mmol/L or to the usual approach of treating only when it fell below 3.5. Over about a year, the protocol group had fewer episodes of peritonitis (hazard ratio 0.47), and 4% had a high potassium without symptoms.[[pichitporn2022]] This was one open-label trial of moderate size. It suggests correcting low potassium matters, and it needs confirmation.</p>
{{key:A PD patient with a falling potassium usually needs more potassium-rich food, not less. Old hemodialysis diet sheets that ban bananas can do harm here. Report the result; supplements are ordered by the physician.}}
<p><strong>Example from practice.</strong> Mr. Soliman, 66, has been on PD for a year. His potassium is 3.1 mmol/L. He has leg cramps, feels weak, and opens his bowels every three days. His diet sheet, copied from a hemodialysis clinic, bans bananas, potatoes, and tomatoes. You lift those limits, add a banana and a serving of boiled potato or kamote each day, and report the result. The physician orders a potassium supplement as well.[[pichitporn2022]] Three weeks later his potassium is 4.0 mmol/L and the cramps have stopped.</p>
"""),
        ("safety", "Safety", "Icodextrin, glucose meters, and the cloudy bag", """
<p><strong>Icodextrin.</strong> This starch-based fluid is used for the long dwell. It releases maltose and related sugars into the blood. Some glucose meters and test strips, those using the enzyme glucose dehydrogenase with the cofactor pyrroloquinoline quinone, read maltose as glucose and show a falsely high result. A patient may then be given insulin for a high glucose that does not exist and become dangerously low. The product label warns about this.[[extraneal]] Confirm with the PD team that the patient&rsquo;s meter is safe with icodextrin. When in doubt, the hospital laboratory glucose is the reference.</p>
<p><strong>Peritonitis.</strong> Cloudy drained fluid is the most common first sign of peritonitis. Abdominal pain and fever may follow, or may not. ISPD advises that patients with cloudy fluid be presumed to have peritonitis and treated promptly; the drained fluid is sent for cell count and culture, and antibiotics are often started before the results return.[[ispd_perit2022]] Every hour of delay matters for the membrane and the patient.</p>
{{stop:Cloudy fluid, abdominal pain, or fever in a PD patient: stop the nutrition visit and contact the PD team at once, following the unit&rsquo;s protocol. Tell the patient to keep the cloudy bag for the team. Nutrition can wait until treatment has started.}}
<p>After an episode, protein losses rise for several days. Check intake, protein, and glucose exposure again with the team once the patient is on treatment.</p>
{{fig:rd10_cloudy}}
<p><strong>Example from practice.</strong> Mr. Rosales, 63, on PD with an icodextrin overnight dwell, is admitted for a hernia repair. The ward meter reads his glucose at 280 mg/dL, and an insulin dose is about to be given. You ask what his overnight fluid is, and the nurse sends a laboratory glucose. It returns at 110 mg/dL. The ward meter uses a strip that reads the maltose from icodextrin as glucose.[[extraneal]] Without that question, he would have been given insulin he did not need and could have gone dangerously low. Write the warning on his chart.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What about the cloudy fluid?</strong> Act on it first, now. Cloudy fluid on PD is peritonitis until proven otherwise, even without fever or pain. Stop the nutrition visit. Contact the PD team immediately under the unit&rsquo;s protocol, and tell her to keep the bag. Everything else in this case comes after that.</p>
<p><strong>How much energy comes from the fluid?</strong> 80 g &times; 3.4 kcal/g = about 272 kcal a day. That leaves about 1,528 kcal to come from food. Write down the 3.4 kcal/g figure and that the 80 g estimate came from the PD team. Her protein target is 1.0 to 1.2 &times; 60 = 60 to 72 g a day, and it will rise while she has peritonitis.</p>
<p><strong>What about bananas?</strong> Her potassium is low, not high, and falling. The old ban is wrong for her now. Report the 3.4 mmol/L result to the team, who may order a supplement, and tell her she can eat bananas and other potassium-rich fruits and vegetables. Cancel the old diet sheet in writing.</p>
<p><strong>And the fullness?</strong> Small, frequent meals with protein first, drinks between meals, and food soon after a drain. Ask about constipation. Tell the PD nurse which part of the day is hardest. PD patients see their team less often than HD patients. When you see one, look for the problem nobody has asked about yet.</p>
"""],
    "skills": {"title": "Peritoneal dialysis nutrition review and urgent escalation",
               "intro": "Use a fictional PD patient card with a fluid schedule and three months of results. The preceptor will reveal one red flag during the visit.",
               "items": [
                   ("Asks for the PD schedule, fluid strengths, and the team&rsquo;s estimate of absorbed glucose, and records the kcal-per-gram value used.", False),
                   ("Calculates dialysate energy and the energy left for food.", False),
                   ("Sets a protein target of 1.0 to 1.2 g/kg/day and explains protein losses.", False),
                   ("Recognizes low or falling potassium and cancels outdated restrictions.", False),
                   ("Confirms that the glucose meter is safe with icodextrin.", True),
                   ("When cloudy fluid is mentioned, stops the visit and contacts the PD team at once.", True),
                   ("Gives practical advice for early fullness without changing the exchange schedule.", False),
               ],
               "placement": "Spend one session in a PD clinic or on a home visit with the PD nurse, and watch one exchange from start to finish."},
    "quiz": [
        ("A PD patient absorbs 80 g of glucose a day. At 3.4 kcal/g, the energy from dialysate is:",
         ["80 kcal", "272 kcal", "800 kcal", "1,800 kcal"], 1,
         "80 × 3.4 = 272 kcal."),
        ("Total energy need is 1,800 kcal and dialysate supplies 272 kcal. Food should supply about:",
         ["272 kcal", "1,528 kcal", "1,800 kcal", "2,072 kcal"], 1,
         "1,800 − 272 = about 1,528 kcal."),
        ("Why do protein needs stay high on PD?",
         ["PD causes protein to be absorbed", "Protein is lost into the dialysis fluid every day", "PD patients are always obese", "They do not"], 1,
         "About 5 to 15 g a day, more with peritonitis."),
        ("What should happen first when a PD patient reports cloudy fluid?",
         ["A routine diet review", "Immediate contact with the PD team", "A lower-protein meal", "Wait for fever"], 1,
         "Cloudy fluid is presumed peritonitis and needs urgent assessment."),
        ("Potassium on PD is often:",
         ["High, because PD removes none", "Low, because fluid without potassium removes it all day", "Unrelated to diet", "Always normal"], 1,
         "Continuous removal makes low potassium common."),
        ("In the Thai trial, keeping potassium at 4 to 5 mmol/L in hypokalemic PD patients was associated with:",
         ["More peritonitis", "Fewer peritonitis episodes", "No change", "Higher mortality"], 1,
         "Hazard ratio 0.47 for peritonitis in one open-label trial."),
        ("A PD patient with potassium 3.4 mmol/L asks whether to keep avoiding bananas. You should:",
         ["Keep the ban", "Report the result and lift the ban", "Ban all fruit", "Start a supplement yourself"], 1,
         "Low potassium calls for more, not less, with the physician informed."),
        ("Which meters may falsely read high with icodextrin?",
         ["All meters", "Those using glucose dehydrogenase with pyrroloquinoline quinone", "Laboratory analyzers", "None"], 1,
         "Maltose is read as glucose by these meters."),
        ("Why is a falsely high glucose reading dangerous?",
         ["It causes thirst", "Insulin may be given for a high that does not exist, causing a severe low", "It raises potassium", "It is not dangerous"], 1,
         "Treating a false high can cause real hypoglycemia."),
        ("Early fullness on PD is mainly caused by:",
         ["Low potassium", "Fluid in the abdomen pressing on the stomach, and steady glucose absorption", "Too much protein", "Phosphate binders"], 1,
         "Both reduce how much the patient can eat."),
        ("Which advice helps early fullness?",
         ["Three large meals", "Small frequent meals with protein first", "More drinks with meals", "Skip breakfast"], 1,
         "Smaller meals and protein first make room for what matters."),
        ("Who changes the PD fluid strengths or schedule?",
         ["The dietitian", "The nephrologist and PD team", "The patient alone", "The pharmacist"], 1,
         "The dietitian reports eating problems; the team decides."),
        ("Stronger PD fluid (for example 4.25%) gives:",
         ["Less glucose", "More glucose absorbed", "No glucose", "Protein"], 1,
         "Higher dextrose removes more water and adds more glucose energy."),
        ("After peritonitis, protein losses:",
         ["Fall", "Rise for several days", "Stop", "Do not change"], 1,
         "Inflammation of the membrane increases protein loss."),
        ("In a patient with diabetes on PD, absorbed glucose may:",
         ["Lower blood glucose", "Raise glucose, weight, and blood fats", "Lower potassium", "Have no effect"], 1,
         "Dialysate glucose is real energy and real glucose."),
    ],
    "terms": [("Dwell", "The time the fluid stays in the abdomen."),
              ("Peritoneum", "The thin lining of the abdominal cavity, used as the dialysis membrane."),
              ("Maltose", "A sugar made of two glucose units, released by icodextrin."),
              ("Continuous ambulatory PD", "Manual exchanges through the day, usually four."),
              ("Membrane transport", "How fast waste and glucose cross the peritoneum; differs between patients.")],
    "readings": [("eating-on-dialysis.html", "Eating on dialysis, including PD."),
                 ("potassium-hyperkalemia-ckd.html", "Potassium in kidney disease.")],
    "calcs": ["calc-pd-glucose-absorption.html", "calc-pd-adequacy.html", "calc-energy-expenditure.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
