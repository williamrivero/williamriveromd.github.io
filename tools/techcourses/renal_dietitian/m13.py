# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 13: Supportive Care, Frailty, and Special Populations. Written for this series from published sources."""

MODULE = {
    "image_alt": "An older man eating a small meal at a family table with grandchildren, a dietitian visiting the home.",
    "objectives": [
        "Set nutrition goals with a patient choosing conservative kidney management, starting from what matters to the patient.",
        "Ease symptoms that stop people eating: poor appetite, altered taste, dry mouth, nausea, constipation, and itch.",
        "Recognize frailty and sarcopenia and change the priority from restriction to function.",
        "Give stone-prevention advice that depends on the stone type.",
        "Coordinate fluid advice in polycystic kidney disease with the kidney team.",
        "Recognize children and pregnant patients as needing specialist care, and refer them.",
    ],
    "big": """
{{plain:For most patients, the renal diet is like a long-distance plan: small sacrifices now to protect the kidneys for years. For a patient choosing comfort over dialysis, the distance is shorter and the plan changes. The question is no longer &ldquo;What will slow the kidney?&rdquo; but &ldquo;What will help this person eat with the family, sleep, and feel well?&rdquo; Restrictions stay only if they still earn their place.}}
{{cards:Key terms for this module|Conservative kidney management (CKM)::Planned, active care for kidney failure without dialysis, focused on symptoms and quality of life.|Kidney supportive care::Care for symptoms, distress, and advance planning, for any patient with kidney disease, alongside other treatment.|Frailty::Low strength, endurance, and reserve; small stresses cause large setbacks.|Sarcopenia::Loss of muscle mass and strength.|Hypercalciuria::Too much calcium in the urine, a common cause of calcium stones.|Autosomal dominant polycystic kidney disease (ADPKD)::An inherited disease in which fluid-filled cysts grow in the kidneys.}}
{{flow:Order of work in supportive care|Ask::What matters most to you now?|Symptoms::What stops you eating?|Rules::Which restrictions still help, and which only cost?|Small trial::One change, a review date.|Team::Share the plan with the supportive care team and family.}}
""",
    "case": {"title": "Strong enough to eat with the family", "html": """
<p>Lolo Ernesto, 83, has CKD G5 and has chosen conservative management after long talks with his nephrologist and family. In two months his weight fell from 52 to 48 kg. He tires walking to the bathroom. His mouth is dry, food tastes &ldquo;like metal,&rdquo; and he has itchy skin.</p>
<p>His daughter stopped giving him fish and monggo because a neighbor said &ldquo;all protein is poison for the kidneys.&rdquo; He eats mostly lugaw and crackers. When you ask what he wants, he says: &ldquo;To be strong enough to sit at the table with my grandchildren on Sundays.&rdquo;</p>
""", "questions": ["What is the nutrition goal here?",
                  "Which restrictions would you review first?",
                  "What would make you call the team the same day?"]},
    "sections": [
        ("ckm", "Conservative care", "Start from what matters to the person", """
<p>The International Society of Nephrology describes conservative kidney management as planned, holistic care for people with kidney failure who choose not to have dialysis. It focuses on symptoms, function, and the person&rsquo;s goals, and kidney supportive care brings the same focus to people on any treatment.[[davison2024]]</p>
<p>For a dietitian, that changes the first question. Instead of &ldquo;What is the eGFR?&rdquo; ask &ldquo;What matters most to you now?&rdquo; Answers are often simple and concrete: eating with family, less thirst, fewer trips to clinic, not being a burden, getting to church. A diet plan that serves that goal is the right plan.</p>
<p>Some restrictions still help. A moderate protein intake may reduce uremic symptoms such as nausea and poor appetite in advanced CKD; keeping potassium safe prevents sudden deterioration; limiting salt can ease swelling and breathlessness. Others only cost: strict rules that shrink intake, hard-to-follow fluid limits, or foods banned years ago that are not needed now. Weigh each one with the patient and the supportive care team. Agree on a short trial, two to four weeks, and a date to review.</p>
{{key:In supportive care, a restriction must earn its place by making the person feel better, not by improving a laboratory number.}}
<p><strong>Example from practice.</strong> Lola Felisa, 88, has chosen conservative kidney management. Her potassium has been steady at 4.8 mmol/L for six months. She keeps a one-liter fluid limit and a strict low-potassium diet from years ago, and she says thirst is the worst part of her day. Her goal: &ldquo;to stop feeling thirsty all the time.&rdquo; With her nephrologist you agree on a two-week trial. Her salt comes down, and her fluid is guided by thirst. Her weight and ankles are checked weekly. At review she is less thirsty, her weight is steady, and her ankles are unchanged. The restriction that cost her the most had stopped earning its place.</p>
"""),
        ("symptoms", "Symptoms", "Ease what stops people eating", """
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>What you can try</th><th>Tell the team</th></tr></thead>
<tbody>
<tr><td>Poor appetite</td><td>Small portions often; favorite foods; most food at the best time of day</td><td>Weight loss; a review of medicines that blunt appetite</td></tr>
<tr><td>Metallic or altered taste</td><td>Sour and aromatic flavors: calamansi, ginger, garlic, onion, herbs; plastic utensils</td><td>Possible zinc deficiency or uremia; the physician decides on tests or dialysis questions</td></tr>
<tr><td>Dry mouth</td><td>Sips, ice chips counted as fluid, sour candy if glucose allows, mouth care</td><td>Medicines that dry the mouth</td></tr>
<tr><td>Nausea</td><td>Dry crackers, cold foods with little smell, smaller meals</td><td>Persistent nausea; anti-nausea medicine</td></tr>
<tr><td>Constipation</td><td>Fiber from tolerated fruits and vegetables, oats, movement</td><td>Laxatives; iron or binder side effects</td></tr>
<tr><td>Itch</td><td>Check phosphorus sources if phosphorus is high</td><td>Itch has several causes; treatment is medical</td></tr>
</tbody></table></div>
<p>Ask about the caregiver too. A daughter who cooks three different meals a day for three family members will burn out. Simple plans that fit the family&rsquo;s food work better than perfect plans that do not.</p>
{{fig:rd13_symptoms}}
<p><strong>Example from practice.</strong> Mr. Tiongson, 75, on hemodialysis, says everything tastes &ldquo;like coins&rdquo; and that he is nauseated most mornings. You suggest fish with calamansi and ginger, cold dishes with little smell, and plastic utensils. You also tell the team about the morning nausea, because it can come from uremia or from too little dialysis, and that is a medical question. Two weeks later he eats better at lunch. The nephrologist has adjusted his prescription as well.</p>
"""),
        ("frailty", "Frailty", "Frailty and sarcopenia: protect function first", """
<p>Screen every older patient for frailty: unintended weight loss, weakness, slow walking, low activity, and exhaustion. A short tool such as the SARC-F questionnaire, grip strength, or a chair-stand test takes minutes. When frailty or sarcopenia is present, the KDIGO 2024 guideline advises considering higher protein and energy targets rather than lower ones (advice without a formal grade).[[kdigo_ckd2024]] Observational data in older adults with mild to moderate CKD point the same way.[[carballo2024]]</p>
<p>Protein helps muscle most when spread across meals and paired with movement. Even simple activity, such as standing from a chair ten times or a short daily walk, works with the diet. Ask a physical therapist to help if one is available.</p>
{{stop:New confusion, severe breathlessness, chest pain, vomiting with inability to keep food down, or a sudden fall in alertness is an acute change, not progression of frailty. Call the physician or follow the urgent pathway.}}
<p><strong>Example from practice.</strong> Mrs. Samonte, 76, 50 kg, has G4 CKD. Her SARC-F score is 6 of 10, and a score of 4 or more suggests sarcopenia. She needs her arms to rise from a chair. She eats about 0.6 g/kg of protein because a doctor years ago told her to. With her nephrologist you raise it toward 0.8 to 1.0 g/kg, about 40 to 50 g, following KDIGO&rsquo;s advice for frail patients.[[kdigo_ckd2024]] The protein is spread across three meals at about 15 g each, and she stands from a chair ten times twice a day. Her function is measured again in six weeks.</p>
"""),
        ("special", "Special groups", "Stones, polycystic kidneys, children, and pregnancy", """
<p><strong>Kidney stones.</strong> Advice depends on the type of stone and the urine tests, so ask for the stone analysis and any 24-hour urine results first. The American Urological Association (AUA) guideline advises fluid enough to make at least 2.5 liters of urine a day for stone formers, limiting sodium, and, for calcium stones, normal dietary calcium of about 1,000 to 1,200 mg a day rather than restriction, because dietary calcium binds oxalate in the gut. Oxalate-rich foods are limited only when urine oxalate is high, and animal protein is limited for some stone types.[[aua2014]] A high fluid goal must fit the rest of the patient&rsquo;s health; it may be unsafe in heart failure, low serum sodium, or advanced CKD.</p>
<p><strong>Polycystic kidney disease.</strong> The KDIGO 2025 ADPKD guideline covers diet and fluid, including water intake and sodium.[[kdigo_adpkd2025]] Fluid advice in ADPKD depends on kidney function, medicines (tolvaptan causes heavy urine output and thirst), and other conditions. Follow the kidney team&rsquo;s plan rather than giving a fixed number yourself.</p>
<p><strong>Children and pregnancy.</strong> Adult targets in this course do not apply. Children need growth-based assessment by a pediatric renal team. Pregnancy in a woman with CKD or on dialysis needs joint care by nephrology, obstetrics, and a dietitian experienced in both. Recognize them and refer.</p>
{{key:When a case falls outside adult kidney care, the safest action is a clear, prompt referral, not an adapted adult plan.}}
<p><strong>Example from practice.</strong> Mr. Gonzaga, 44, has calcium oxalate stones and an eGFR of 75. He stopped milk and cheese because &ldquo;calcium makes stones.&rdquo; His 24-hour urine volume is 1.4 liters. The AUA guideline points the other way: drink enough to make at least 2.5 liters of urine a day, eat a normal 1,000 to 1,200 mg of dietary calcium so that it binds oxalate in the gut, and limit sodium.[[aua2014]] You bring back a glass of milk with meals, set a fluid target he can track by the color of his urine, and cut back on instant noodles. His second urine collection will show whether it worked.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What is the goal?</strong> His own: to be strong enough to sit with his grandchildren on Sundays. Write it in the plan. Every change should help him reach it. A protein cap that leaves him too weak to sit up fails that goal.</p>
<p><strong>Which restrictions first?</strong> The neighbor&rsquo;s protein ban. Fish and monggo are among the foods he can still enjoy and that help him keep strength. Bring them back in small, soft portions: flaked fish in lugaw, egg, tofu, monggo soup. Explain to his daughter, kindly, that the advice she heard was wrong for him. For the metallic taste, try calamansi, ginger, and garlic. For the dry mouth, sips and mouth care. Agree on a two-week trial.</p>
<p><strong>What else?</strong> A 4 kg loss in two months and new weakness need the nephrologist and supportive care team this week, with the numbers. Ask about the itch and the taste: they may be signs of advancing uremia that the team should weigh. Ask how his daughter is managing.</p>
<p><strong>What would make you call today?</strong> New confusion, severe breathlessness, vomiting with no food staying down, or a sudden drop in alertness. In supportive care, the dietitian often helps a family learn that feeding someone well can look different from following the old rules.</p>
"""],
    "skills": {"title": "Supportive care nutrition visit",
               "intro": "The preceptor plays an older patient choosing conservative management, with a family member present.",
               "items": [
                   ("Asks the patient what matters most and records the answer as the goal.", False),
                   ("Reviews each restriction and keeps only those that help the patient feel better.", False),
                   ("Asks about appetite, taste, dry mouth, nausea, constipation, itch, and caregiver burden.", False),
                   ("Screens for frailty with a short tool or strength test.", False),
                   ("Agrees on a short trial with a review date shared with the supportive care team.", False),
                   ("Recognizes an acute change and routes it to the physician or urgent pathway.", True),
                   ("Refers children and pregnant patients to specialist care instead of adapting adult targets.", True),
               ],
               "placement": "Join one supportive care or home visit and write down the patient&rsquo;s stated goal in his or her own words."},
    "quiz": [
        ("In conservative kidney management, the first nutrition question is:",
         ["What is the eGFR?", "What matters most to you now?", "How much protein do you eat?", "What is your weight?"], 1,
         "Goals shape every later decision."),
        ("A patient&rsquo;s goal is to sit with family on Sundays. Which outcome fits it best?",
         ["A fixed protein cap", "Enough strength and tolerable symptoms to join the family meal", "Identical laboratory results", "Weight loss"], 1,
         "The plan serves the person&rsquo;s goal."),
        ("A neighbor told the family that all protein is harmful. The patient is losing weight. You should:",
         ["Agree", "Explain that some protein is needed and bring back small portions of favored foods", "Ban rice instead", "Say nothing"], 1,
         "Mistaken restrictions are a common cause of wasting."),
        ("For metallic taste, which suggestion is useful?",
         ["More salt", "Sour and aromatic flavors such as calamansi and ginger", "Metal spoons", "Skipping meals"], 1,
         "Acid and aromatics can mask metallic taste."),
        ("KDIGO 2024 advises considering, in older adults with frailty or sarcopenia:",
         ["Lower protein targets", "Higher protein and energy targets", "Fasting", "No change"], 1,
         "Function outweighs slowing progression in this group."),
        ("Which is a short frailty or sarcopenia screen?",
         ["SARC-F questionnaire", "Serum albumin", "Body mass index alone", "Urine color"], 0,
         "SARC-F takes minutes; grip strength and chair-stand also help."),
        ("For calcium stone formers, the AUA advises dietary calcium:",
         ["Restricted to 300 mg/day", "At normal levels, about 1,000 to 1,200 mg/day", "Unlimited supplements", "Avoided entirely"], 1,
         "Dietary calcium binds oxalate in the gut."),
        ("The AUA fluid goal for stone formers is enough to make urine of at least:",
         ["1 liter a day", "2.5 liters a day", "5 liters a day", "No goal"], 1,
         "Dilute urine lowers the chance of crystals forming."),
        ("Before advising a high fluid intake for stones, check:",
         ["Favorite drink", "Stone type and whether heart, sodium, or kidney problems make it unsafe", "Shoe size", "Nothing"], 1,
         "High fluid can harm some patients."),
        ("Who should set the fluid plan in ADPKD?",
         ["The dietitian alone", "The kidney team, considering function and medicines", "The patient&rsquo;s friends", "No one"], 1,
         "Tolvaptan and kidney function change the advice."),
        ("An 11-year-old with CKD and slowing growth needs:",
         ["Adult targets scaled down", "Referral to a pediatric renal team", "A low-protein diet", "No change"], 1,
         "Children need growth-based specialist care."),
        ("A woman on dialysis becomes pregnant. The best action is:",
         ["Continue her usual plan", "Prompt referral for joint nephrology, obstetric, and dietetic care", "Restrict protein", "Wait"], 1,
         "Pregnancy changes every target."),
        ("Which is an acute change requiring urgent medical review?",
         ["Gradual tiredness over months", "New confusion", "Preferring lugaw", "A request for recipes"], 1,
         "Acute changes are not frailty progression."),
        ("Why ask about the caregiver?",
         ["To assign blame", "Because the plan depends on who shops and cooks, and caregivers can burn out", "It is not needed", "For billing"], 1,
         "A plan the family cannot sustain will fail."),
        ("In supportive care, a restriction should stay only if:",
         ["It improves a laboratory number", "It makes the person feel better or prevents a crisis", "It was in the old diet sheet", "The family likes it"], 1,
         "Restrictions must earn their place."),
    ],
    "terms": [("Advance care planning", "Talking about future care wishes before a crisis."),
              ("Uremic symptoms", "Nausea, poor appetite, itch, altered taste, and tiredness from retained wastes."),
              ("Tolvaptan", "A medicine that slows cyst growth in ADPKD; causes heavy urine output."),
              ("Lolo", "Grandfather; a respectful term for an older man."),
              ("24-hour urine", "A collection used to measure stone-forming substances.")],
    "readings": [("managing-kidney-stones.html", "Kidney stones for patients."),
                 ("calcium-disorders-and-kidney-stones.html", "Calcium, urine, and stones."),
                 ("hemodialysis-elderly.html", "Older adults and dialysis decisions."),
                 ("kain-pa-rin.html", "Poor appetite in kidney disease.")],
    "calcs": ["calc-sarcopenia-sarcf.html", "calc-frailty-assessment.html", "calc-stone-prevention-fluid.html", "calc-urine-supersaturation.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
