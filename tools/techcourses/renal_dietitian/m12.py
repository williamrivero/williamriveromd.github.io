# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 12: Nutrition Before and After Kidney Transplantation. Written for this series from published sources."""

MODULE = {
    "image_alt": "A family kitchen where a transplant recipient and spouse cook fish thoroughly, a pomelo set aside on the counter.",
    "objectives": [
        "Prepare a transplant candidate&rsquo;s nutrition so they arrive at surgery strong, not merely lighter.",
        "Explain why needs change from the first weeks to the first year after transplant.",
        "Decide which dialysis-era restrictions to lift, based on current kidney function and results.",
        "Recognize post-transplant diabetes and steroid-related high glucose, and coordinate with the team.",
        "Teach food safety with familiar Filipino dishes.",
        "Route questions about foods and herbs that change tacrolimus levels to the transplant pharmacist.",
    ],
    "big": """
{{plain:A new kidney is a working engine placed in a car that has been parked for years. The car runs again, but it needs new habits: the old dialysis rules may no longer fit, the medicines that protect the kidney change appetite, glucose, and blood fats, and the body&rsquo;s defenses are lowered on purpose. Nutrition after transplant is mostly about helping the new engine last.}}
<p>The picture has a limit. A transplanted kidney is not a new engine in an unchanged car. It works inside an immune system that is lowered on purpose, and the same medicines that protect it raise glucose, blood fats, and blood pressure and change how the body handles potassium and magnesium. Food can even change the drug level itself: grapefruit, and probably pomelo, slow the breakdown of tacrolimus. Your work in this module is to prepare candidates, keep the first weeks safe, and protect the graft for the long term.</p>
{{cards:Key terms for this module|Transplant candidate::A person being evaluated for, or waiting for, a kidney transplant.|Graft::The transplanted kidney.|Immunosuppressant::A medicine that lowers the immune response so the graft is not rejected, such as tacrolimus, mycophenolate, and prednisone.|Tacrolimus::The main anti-rejection medicine; its blood level must stay in a narrow range.|Cytochrome P450 3A4 (CYP3A4)::An enzyme in the gut and liver that breaks down tacrolimus. Some foods block it.|Post-transplantation diabetes mellitus (PTDM)::Diabetes that first appears after transplant.|Food safety::Handling food to prevent infection: clean, separate, cook, chill.}}
{{flow:The transplant journey|Waiting::Prehabilitation: protein, strength, function.|First weeks::Healing, high protein, high glucose from steroids, food safety.|First months::Lift old dialysis rules carefully; watch potassium, phosphate, magnesium.|Long term::Weight, blood pressure, lipids, diabetes, bone.}}
""",
    "case": {"title": "The fiesta two weeks out", "html": """
<p>Mr. Domingo, 45, received a kidney from his sister two weeks ago. His creatinine is improving. He takes tacrolimus, mycophenolate, and prednisone. His appetite is poor, and his glucose readings have been 220 to 260 mg/dL in the afternoon.</p>
<p>His family is planning a homecoming party with kinilaw, lechon, and fruit. He asks whether he can eat the kinilaw, whether he can have pomelo, and whether an herbal tonic a relative sent from abroad is safe. He also asks if he must still avoid bananas and keep drinking only a liter a day, as he did on dialysis.</p>
""", "questions": ["What would you say about the kinilaw and the pomelo?",
                  "Who should check the herbal tonic, and why?",
                  "Should he keep his dialysis restrictions?"]},
    "sections": [
        ("before", "Before transplant", "Arrive at surgery strong", """
<p>Candidates are often weak after years of dialysis. Frailty and low muscle mass before transplant are linked to longer hospital stays and more complications. The KDIGO candidate guideline advises assessing nutrition and frailty during evaluation and addressing them before surgery.[[kdigo_txcand2020]]</p>
<p>Some programs ask candidates with obesity to lose weight. KDIGO advises against excluding candidates on body mass index alone, and when weight loss is advised, the goal is less fat with muscle kept.[[kdigo_txcand2020]] Fast weight loss on dialysis often takes muscle. The candidate should keep dialysis-level protein (1.0 to 1.2 g/kg/day), reduce energy modestly, and stay active. Measure grip strength or a chair-stand test along with weight. Tell the transplant team what is happening to strength, not only to the scale.</p>
{{key:The goal before transplant is a stronger patient, not just a lighter one.}}
<p><strong>Example from practice.</strong> Mr. Esguerra, 47, on hemodialysis, weighs 95 kg at 1.70 m, a body mass index of 33. His transplant program advised weight loss. On a crash diet he lost 7 kg in two months, and his grip strength fell from 34 to 27 kg. He is lighter and weaker. With the team you change the plan: protein back to 1.0 to 1.2 g/kg of an adjusted weight, a modest energy deficit, and a daily walk. You track grip strength with every weigh-in. KDIGO advises against excluding him on body mass index alone.[[kdigo_txcand2020]]</p>
"""),
        ("after", "After transplant", "The first weeks and the first year", """
<p>In the first weeks, the body is healing from surgery, and high-dose steroids break down muscle and raise glucose. Protein needs are high, often around 1.3 to 1.5 g/kg/day in the early period, a common practice figure rather than a graded recommendation. Appetite can be poor. Small, frequent meals and an oral supplement may help.</p>
<p><strong>Lifting the old rules.</strong> With a working graft, most patients no longer need the dialysis diet. But do not lift every restriction on day one. Tacrolimus can raise potassium and lower magnesium. A delayed or poorly working graft may still need potassium and fluid limits. Phosphate often falls after transplant, sometimes very low, as the new kidney and high parathyroid hormone pass it out. Read the current results, ask the transplant team what they want, and lift restrictions one at a time.</p>
<p><strong>Glucose.</strong> Steroids raise glucose in the afternoon and evening. Tacrolimus reduces insulin release. Post-transplant diabetes is common, and an international consensus advises screening and treating it with lifestyle measures and medicines chosen with the team.[[sharif2024]] Your part: carbohydrate spread over the day, fewer sweet drinks, a meal pattern that matches the steroid dose, and readings with times passed to the team.</p>
<p><strong>Long term.</strong> After the first months, the risks shift to weight gain, high blood pressure, high blood fats, diabetes, and bone loss. The KDIGO recipient guideline advises managing these as cardiovascular risk factors.[[kdigo_tx2009]] Many patients gain weight in the first year. Plan for it early.</p>
{{fig:rd12_timeline}}
<p><strong>Example from practice.</strong> Ms. Cortez, 38, is three weeks after her transplant. Her phosphate is 1.8 mg/dL, low, yet she still avoids milk and eggs from her dialysis days. Her potassium is 5.3 mmol/L on tacrolimus, and her magnesium is low. Lift one restriction at a time. With the team&rsquo;s agreement, add milk and eggs back to help her phosphate. Keep a moderate potassium plan for now. Raise her protein to about 1.3 to 1.5 g/kg, or 72 to 83 g at 55 kg. Recheck in a week. Not every rule from dialysis is wrong, and not every rule is still needed.</p>
"""),
        ("safety", "Food safety", "Food safety with familiar meals", """
<p>Immunosuppressants make infections from food more likely and more serious. The United States Food and Drug Administration lists transplant recipients among people at higher risk and teaches four steps: clean, separate, cook, and chill.[[fda_foodsafety]] The transplant program sets the specific rules and how long they last.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual dish</th><th>The risk</th><th>A safer choice</th></tr></thead>
<tbody>
<tr><td>Kinilaw, sushi, raw oysters</td><td>Raw fish and shellfish; vinegar does not kill all bacteria or parasites</td><td>Fish cooked through, such as paksiw or sinigang</td></tr>
<tr><td>Soft-boiled or raw egg in drinks or desserts</td><td>Salmonella</td><td>Eggs cooked until the yolk is firm</td></tr>
<tr><td>Rare or undercooked meat</td><td>Bacteria in the center</td><td>Meat cooked through; no pink</td></tr>
<tr><td>Fiesta food left out for hours</td><td>Bacteria grow at room temperature</td><td>Eat it freshly served; chill leftovers within two hours</td></tr>
<tr><td>Unpasteurized milk, street ice, unsafe water</td><td>Bacteria and parasites</td><td>Pasteurized milk, boiled or bottled water, ice from safe water</td></tr>
</tbody></table></div>
<p>Teach the family too, because they shop and cook. Use teach-back: ask the patient to tell you which dishes he will choose at the party.</p>
<p><strong>Example from practice.</strong> Mr. Domingo&rsquo;s homecoming party starts at noon. By 3 p.m. the lechon, the pancit, and the leche flan have been on the table for three hours. Using teach-back, ask him what he will eat. A good answer: &ldquo;Freshly served pancit and lechon at noon, cooked fish instead of kinilaw, leche flan only if the eggs were cooked firm. Nothing left out after two o&rsquo;clock. Bottled water, no street ice.&rdquo; His sister repeats the same plan for the leftovers: into the refrigerator within two hours.[[fda_foodsafety]]</p>
{{fig:rd12_fig_transplant_food_safety_swaps}}
"""),
        ("drugs", "Food and medicines", "Foods, herbs, and tacrolimus", """
<p>Tacrolimus is broken down by an enzyme, CYP3A4, in the gut and liver. Grapefruit juice blocks this enzyme, so tacrolimus levels can rise and cause toxicity. Pomelo, a close relative of grapefruit and common in the Philippines, contains similar compounds. Evidence for pomelo comes mainly from laboratory and animal studies, including one in rats in which pomelo juice raised tacrolimus levels, and from reviews of food interactions.[[egashira2012]][[tolou2025]] That is weaker evidence than for grapefruit, but the mechanism is the same, so most programs advise avoiding both.</p>
<p>Herbal products are a larger unknown. Many contain several plants in unknown amounts, and some, such as St. John&rsquo;s wort, lower tacrolimus levels and can lead to rejection. Others raise them. You cannot judge a product from its label.</p>
{{call:Any herbal product, tonic, or supplement in a transplant recipient: ask the patient to bring it in and not to start it, and send the question to the transplant pharmacist or physician before use. Do not judge it safe yourself.}}
{{fig:rd12_interaction}}
<p><strong>Example from practice.</strong> Mr. Bernardo, 52, two years after his transplant, has a tacrolimus trough that has risen from 7 to 13 ng/mL. His dose has not changed. When the transplant nurse asks about food, he says that since Christmas he has eaten half a pomelo every day. Pomelo is a plausible cause, because it may block the same enzyme as grapefruit, and the evidence is weaker than for grapefruit.[[egashira2012]][[tolou2025]] You report it to the transplant team the same day. They decide on the dose and the repeat level, and you advise him to stop the pomelo.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The kinilaw and the pomelo?</strong> Not the kinilaw, not now. It is raw fish in vinegar, and vinegar does not make it safe for someone on three immunosuppressants. Offer a cooked fish dish the family enjoys, such as paksiw or sinigang. No pomelo either: it acts like grapefruit on the enzyme that breaks down tacrolimus. Lechon is fine to eat freshly served, in a sensible portion; the skin and fat are heavy, and his glucose is already high. Fruit other than pomelo and grapefruit, washed and peeled, is fine.</p>
<p><strong>The herbal tonic?</strong> Ask him to bring it, not to start it, and send it to the transplant pharmacist or physician. Herbs can raise or lower tacrolimus levels, and the label will not tell you which. Explain why, so he does not feel his relative&rsquo;s gift is being dismissed.</p>
<p><strong>The dialysis restrictions?</strong> Probably not all of them, but check first. His creatinine is improving. Look at his current potassium, phosphate, and magnesium, and ask the transplant team about fluid; many recipients are asked to drink more, not less, in the early weeks. Lift restrictions one at a time with the team&rsquo;s agreement.</p>
<p><strong>And the glucose?</strong> Afternoon readings of 220 to 260 mg/dL fit steroid-related high glucose. Pass the readings and times to the team. Spread his carbohydrate through the day, swap sweet drinks for water, and plan party portions with him. After transplant, the dietitian helps the patient follow new rules that keep the graft working.</p>
"""],
    "skills": {"title": "Post-transplant nutrition visit",
               "intro": "Use a fictional recipient two to six weeks after surgery, with a medicine list and current results.",
               "items": [
                   ("Reviews current kidney function, potassium, phosphate, magnesium, and glucose before changing any restriction.", False),
                   ("Confirms with the transplant team which dialysis-era restrictions to lift.", False),
                   ("Teaches the four food safety steps and suggests cooked versions of familiar raw dishes.", False),
                   ("Uses teach-back with the patient or family member who cooks.", False),
                   ("Advises against grapefruit and pomelo and explains why.", False),
                   ("Routes every herbal or supplement question to the transplant pharmacist or physician before use.", True),
                   ("Reports glucose readings with times and plans carbohydrate around the steroid dose.", False),
                   ("For a candidate, plans weight change that keeps protein and measures strength.", False),
               ],
               "placement": "Attend one transplant clinic or pre-transplant evaluation and review the program&rsquo;s food safety handout."},
    "quiz": [
        ("Which party dish is the immediate food-safety risk for a recent transplant recipient?",
         ["Paksiw", "Kinilaw", "Boiled rice", "Cooked vegetables"], 1,
         "Raw fish in vinegar is not reliably safe."),
        ("Why should transplant recipients avoid pomelo?",
         ["It is high in sodium", "It may block the enzyme that breaks down tacrolimus, like grapefruit", "It contains protein", "It lowers glucose"], 1,
         "The mechanism is shared with grapefruit; evidence is mainly laboratory and animal."),
        ("A recipient brings a herbal tonic. You should:",
         ["Approve it if the label looks natural", "Ask him not to start it and refer it to the transplant pharmacist or physician", "Tell him to take half", "Ignore it"], 1,
         "Herbs can raise or lower tacrolimus levels."),
        ("Before transplant, the goal of weight management is:",
         ["Fastest possible loss", "Less fat with muscle kept", "Gaining weight", "No change in diet"], 1,
         "Rapid loss on dialysis often takes muscle."),
        ("Which result should be checked before lifting a potassium restriction after transplant?",
         ["Albumin", "Current serum potassium", "Hemoglobin", "Cholesterol"], 1,
         "Tacrolimus and slow graft function can keep potassium high."),
        ("Tacrolimus commonly causes:",
         ["Low potassium and high magnesium", "High potassium and low magnesium", "Low glucose", "Low blood pressure only"], 1,
         "Monitor both after transplant."),
        ("Phosphate after transplant often:",
         ["Rises sharply", "Falls, sometimes very low", "Stays the same", "Cannot be measured"], 1,
         "The new kidney and high PTH pass phosphate into urine."),
        ("Afternoon high glucose after transplant is most often linked to:",
         ["Mycophenolate", "Prednisone", "Iron", "Vitamin D"], 1,
         "Steroids raise glucose later in the day."),
        ("The four food safety steps are:",
         ["Wash, dry, fold, store", "Clean, separate, cook, chill", "Buy, cook, eat, rest", "Salt, dry, smoke, store"], 1,
         "Taught by the U.S. Food and Drug Administration."),
        ("Fiesta leftovers should be chilled within:",
         ["Two hours", "Six hours", "Twelve hours", "The next day"], 0,
         "Bacteria grow quickly at room temperature."),
        ("Who sets the transplant patient&rsquo;s specific food rules and their duration?",
         ["The dietitian alone", "The transplant program", "The patient&rsquo;s family", "The food vendor"], 1,
         "Programs differ; follow theirs."),
        ("KDIGO advises that transplant candidates with obesity be:",
         ["Excluded on body mass index alone", "Not excluded on body mass index alone", "Told to fast", "Given high-fat diets"], 1,
         "Assessment should be broader than one number."),
        ("Long-term risks after transplant include:",
         ["Weight gain, high blood pressure, high blood fats, diabetes, and bone loss", "Only rejection", "Only infection", "None"], 0,
         "Manage them as cardiovascular risk factors."),
        ("A recipient asks if he must still drink only a liter a day. You should:",
         ["Say yes", "Check with the transplant team; many are asked to drink more early on", "Say he can drink nothing", "Tell him to drink three liters without asking"], 1,
         "Fluid advice changes with the graft; the team decides."),
        ("Why use teach-back for food safety?",
         ["It saves time", "It confirms that the patient can apply the advice to real dishes", "It is required by law", "It replaces the handout"], 1,
         "Understanding is shown, not assumed."),
    ],
    "terms": [("Prehabilitation", "Building strength and nutrition before surgery."),
              ("Delayed graft function", "A new kidney that is slow to start working; dialysis may still be needed for a time."),
              ("Paksiw", "Fish or meat cooked in vinegar and spices."),
              ("Kinilaw", "Raw fish cured in vinegar or citrus."),
              ("Rejection", "The immune system attacking the graft.")],
    "readings": [("kidney-transplant.html", "Kidney transplant for patients and families."),
                 ("transplant-prehabilitation.html", "Getting fit for a kidney transplant.")],
    "calcs": ["calc-tacrolimus-dosing.html", "calc-allograft-egfr-trend.html", "calc-transplant-prom.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
