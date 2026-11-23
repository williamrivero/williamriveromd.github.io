# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 08: Diabetes, Obesity, and Cardiometabolic Risk. Written for this series from published sources."""

MODULE = {
    "image_alt": "A woman checking her glucose with a meter at a workplace canteen table, a packed lunch in front of her.",
    "objectives": [
        "Explain why the risk of low blood glucose rises as kidney function falls.",
        "Say when glycated hemoglobin (HbA1c) can mislead in advanced CKD and dialysis, and what other glucose data to use.",
        "Plan carbohydrate amount and timing around the patient&rsquo;s meals, work, and medicines.",
        "Recognize recurrent low glucose as a safety problem and route it to the diabetes team.",
        "Describe how newer medicines change appetite, intake, and fluid, and what the dietitian watches for.",
        "Plan weight loss in CKD that protects muscle.",
    ],
    "big": """
{{plain:Insulin is like a key that lets glucose into cells. A healthy kidney does two quiet jobs with that key: it clears used insulin from the blood, and it makes some glucose of its own between meals. When the kidney fails, insulin keys stay in the lock longer, and the kidney&rsquo;s own glucose supply shrinks. So the same insulin dose that was safe last year can now push glucose too low, especially when a meal is skipped.}}
{{cards:Key terms for this module|Glycated hemoglobin (HbA1c)::The share of hemoglobin carrying glucose. It reflects average glucose over the life of red cells, about three months.|Hypoglycemia::Low blood glucose, commonly below 70 mg/dL. Below 54 mg/dL is clinically important.|Continuous glucose monitor (CGM)::A small sensor under the skin that reads glucose every few minutes.|Sodium-glucose cotransporter 2 (SGLT2) inhibitor::A medicine such as dapagliflozin or empagliflozin that makes the kidney pass glucose in urine and protects kidneys and heart.|Glucagon-like peptide-1 receptor agonist (GLP-1 RA)::A medicine such as semaglutide that lowers glucose, reduces appetite, and slows stomach emptying.|Sarcopenic obesity::Excess body fat together with low muscle mass and strength.}}
{{flow:Order of work in diabetes with CKD|Safety::Any low glucose readings? Who treats them?|Data::Time-stamped readings, meals, and medicine times.|Pattern::Which meals are skipped, late, or very large?|Plan::Carbohydrate spread across the day, built from food the patient eats.|Weight::If weight loss is a goal, protect protein and muscle.|Handoff::Medicine changes go to the diabetes team.}}
""",
    "case": {"title": "The skipped lunch", "html": """
<p>Ms. Ramos, 52, works shifts at a call center. She has type 2 diabetes and CKD G4. She takes insulin glargine at night and a short-acting insulin with breakfast and dinner. She received iron and an erythropoiesis-stimulating agent for anemia two months ago. Her HbA1c dropped from 8.1% to 6.4% in that time, and her doctor was pleased.</p>
<p>Her meter shows two readings of 58 and 62 mg/dL before dinner this week, both on days she skipped lunch because her break was cut short. She felt shaky and sweaty and drank a soft drink. Today she feels well, and her glucose is 140 mg/dL.</p>
""", "questions": ["What is your first action, and who must know?",
                  "Why might her HbA1c look better than her glucose really is?",
                  "What food plan would fit her shift?"]},
    "sections": [
        ("glucose", "Glucose and the kidney", "Why low glucose becomes more likely", """
<p>To understand why, start with what a healthy kidney does for glucose. Between meals, the liver and the kidney both release glucose into the blood. The kidney supplies a real share of it after an overnight fast. The kidney also clears insulin from the blood, so a dose wears off on time.</p>
<p>As eGFR falls, both jobs fade. Insulin and some tablets, such as the sulfonylureas, stay active longer. The kidney adds less glucose between meals. Appetite is often poor, and meals are skipped on dialysis days. Put together, a patient whose glucose was hard to bring down five years ago may now go low on the same treatment. KDIGO advises individual HbA1c targets from below 6.5% to below 8.0%, aiming higher in people at greater risk of hypoglycemia (a firm recommendation, grade 1C).[[kdigo_dm2022]]</p>
{{key:A patient with advanced CKD whose glucose readings are &ldquo;getting better on their own&rdquo; may be losing kidney function or eating less. Ask, and tell the diabetes team.}}
"""),
        ("data", "Reading the numbers", "When HbA1c misleads, and what to use instead", """
<p>HbA1c measures glucose stuck to hemoglobin, so it depends on how long red cells live. In advanced CKD and on dialysis, red cells live a shorter time, and treatment with erythropoiesis-stimulating agents, iron, or a transfusion brings a wave of young cells that have not yet picked up much glucose. HbA1c then reads lower than the true average glucose.[[kdigo_dm2022]][[kdigo_anemia2026]] KDIGO advises that when HbA1c and measured glucose do not agree, a continuous glucose monitor or self-monitoring can guide treatment (advice without a formal grade).</p>
<div class="table-wrap"><table>
<thead><tr><th>Data</th><th>What it tells you</th><th>Watch for</th></tr></thead>
<tbody>
<tr><td>HbA1c</td><td>Average over about three months</td><td>Falsely low after anemia treatment or transfusion, and on dialysis</td></tr>
<tr><td>Meter readings with time and meal notes</td><td>When glucose goes high or low, and why</td><td>Readings taken only in the morning miss afternoon lows</td></tr>
<tr><td>Continuous glucose monitor</td><td>Time in range and time below range</td><td>Cost; ask what the patient can afford</td></tr>
<tr><td>Food and medicine diary</td><td>Links each low to a skipped meal or a dose</td><td>The most useful thing you can ask for</td></tr>
</tbody></table></div>
<p>Your job with these data is not to change a dose. It is to find the pattern, such as lows only on workdays, only after dialysis, or only when lunch is missed, and bring it to the diabetes team with the times.</p>
{{fig:rd08_glucose_pattern}}
"""),
        ("plan", "The plan", "Plan carbohydrate around the person", """
<p>There is no special &ldquo;renal diabetic diet.&rdquo; The American Diabetes Association and KDIGO both advise an eating pattern rich in vegetables, fruits, whole grains, fiber, legumes, and plant protein, and low in refined carbohydrate and sweetened drinks, with protein at 0.8 g/kg/day for CKD not on dialysis.[[ada2026]][[kdigo_dm2022]] The work is to make that fit the person: her shift, her budget, her rice.</p>
{{cards:Carbohydrate planning in practice|Rice in a measured cup::One cup of cooked rice is about 40 to 45 g of carbohydrate. Keep it steady from meal to meal, especially with fixed insulin doses.|No skipped meals on insulin::If a meal cannot be eaten, the patient needs a plan agreed with the diabetes team, not a guess.|Portable food::A packed lunch, a sandwich, or crackers with egg for short breaks.|Sweet drinks::Soft drinks, juice, and 3-in-1 coffee are the first sugars to replace, except when treating a low.|Treating a low::Fast sugar first, as the team taught her, then a snack with protein once she recovers. Glucose tablets avoid the phosphorus in colas.}}
<p>Then check that the plan still gives enough energy. Diabetes advice and kidney advice together can shrink a diet until little is left. A patient who cuts rice for her glucose, meat for her kidneys, and fruit for her potassium is on a starvation diet. Count the day&rsquo;s energy before you send her home.</p>
{{call:Recurrent glucose below 70 mg/dL, any reading below 54 mg/dL, a low that needed another person&rsquo;s help, or a patient on insulin who cannot eat because of illness: tell the diabetes team the same day. Severe symptoms or a patient who cannot swallow safely go through the emergency pathway.}}
"""),
        ("weight", "Medicines and weight", "New medicines, and weight loss that keeps muscle", """
<p><strong>SGLT2 inhibitors</strong> make the kidney pass glucose in the urine, about 200 to 300 kcal a day in people with good kidney function and less as eGFR falls. They protect the kidneys and heart. Patients may lose a little weight and feel thirsty. Ask about sick days: the team usually tells patients to pause these medicines when they cannot eat or drink, to avoid a rare, serious acid problem called ketoacidosis. That instruction comes from the prescriber; you make sure the patient knows it exists.</p>
<p><strong>GLP-1 receptor agonists</strong> reduce appetite and slow the stomach. In the FLOW trial, 3,533 people with type 2 diabetes and CKD were randomly assigned to weekly semaglutide or placebo. Over a median of 3.4 years, the main outcome, a combination of kidney failure, a large fall in eGFR, and death from kidney or heart causes, happened 24% less often with semaglutide (hazard ratio 0.76).[[flow2024]] This was a large randomized trial, so the benefit is well supported for people like those enrolled. For you, the practical point is that appetite can fall a lot. Watch for intake dropping below protein needs, nausea, and dehydration, and report them.</p>
<p><strong>Weight loss.</strong> Many patients with diabetes and CKD carry excess weight, and losing some of it helps blood pressure, glucose, and sometimes eligibility for a transplant. But in CKD, a fast loss often takes muscle with it. Aim for a modest deficit, keep protein at the prescribed level, spread it over meals, and pair the diet with activity the patient can do. Track grip strength or a chair-stand test, not only the scale. When weight falls and strength falls with it, the plan needs changing.</p>
{{fig:rd08_weight_muscle}}
"""),
    ],
    "debrief": ["""
<p><strong>What is the first action?</strong> Tell the diabetes team today. Two symptomatic readings in the 50s and low 60s in one week, on insulin, are recurrent hypoglycemia. Give them the readings, the times, the skipped lunches, and her insulin doses. Check that she has a written plan for treating a low and knows whom to call. If a low happens during your visit, follow the unit&rsquo;s protocol.</p>
<p><strong>Why might her HbA1c mislead?</strong> She had anemia treatment two months ago. The young red cells it produced have carried glucose for only a short time, so her HbA1c fell faster than her average glucose did. It may also be falling because she is having lows. A falling HbA1c here is not proof that her diabetes is better controlled. Her meter readings with times tell you more.</p>
<p><strong>What food plan fits her shift?</strong> A lunch she can eat in a short break: rice in a measured cup with egg or fish and a vegetable, packed from home, or a sandwich with egg if her break is very short. A small snack with protein in her bag for days the break is cut. Ask whether she can take a fixed meal break and whether her employer would allow it. Replace the soft drinks she drinks as treats with water, and keep a fast sugar source for actual lows.</p>
<p><strong>What do you leave to the team?</strong> Insulin doses and timing. Her shift changed and her kidneys changed, and the prescription may need to follow. Your part is to show the team exactly when the lows happen. When you bring them a pattern, they can make a decision.</p>
"""],
    "skills": {"title": "Glucose pattern review and hypoglycemia handoff",
               "intro": "Use a fictional week of meter readings with meal and medicine times.",
               "items": [
                   ("Asks first about any low readings and how they were treated.", True),
                   ("Explains why HbA1c can read falsely low after anemia treatment or on dialysis.", False),
                   ("Links each low or high reading to a meal, a missed meal, or a medicine time.", False),
                   ("Reports recurrent lows to the diabetes team the same day with readings and times, without changing a dose.", True),
                   ("Plans carbohydrate portions and timing around the patient&rsquo;s work and meals.", False),
                   ("Checks that combined diabetes and kidney restrictions still meet the energy target.", False),
                   ("Asks about sick-day instructions for SGLT2 inhibitors and appetite changes on GLP-1 receptor agonists.", False),
                   ("For weight loss, sets a protein target and a measure of muscle function as well as weight.", False),
               ],
               "placement": "Sit with a diabetes educator or physician for one clinic and note how each insulin change was decided."},
    "quiz": [
        ("Why does the risk of hypoglycemia rise as CKD advances?",
         ["Patients eat more", "Insulin is cleared more slowly and the kidney releases less glucose", "Glucose is absorbed faster", "HbA1c rises"], 1,
         "Slower insulin clearance and less kidney glucose release both lower glucose."),
        ("A patient received an erythropoiesis-stimulating agent two months ago. Her HbA1c may be:",
         ["Falsely high", "Falsely low", "Unchanged", "Impossible to measure"], 1,
         "Young red cells carry less glucose, so HbA1c reads low."),
        ("KDIGO&rsquo;s HbA1c target in diabetes with CKD is:",
         ["Below 5.5% for all", "Individualized from below 6.5% to below 8.0%", "Above 9%", "Not needed"], 1,
         "A firm recommendation (grade 1C) to individualize the target."),
        ("Which data best explain recurrent lows before dinner?",
         ["HbA1c alone", "Time-stamped meter readings with meal and medicine times", "Body mass index", "Serum albumin"], 1,
         "Times link each low to a missed meal or a dose."),
        ("Two symptomatic lows on insulin this week. The dietitian should:",
         ["Reduce the insulin dose", "Tell the diabetes team the same day", "Wait for the next HbA1c", "Tell her to stop insulin on workdays"], 1,
         "Recurrent hypoglycemia is a safety issue for the prescribing team."),
        ("One cup of cooked rice contains about how much carbohydrate?", ["5 to 10 g", "40 to 45 g", "100 g", "150 g"], 1,
         "About 40 to 45 g; keeping the portion steady helps with fixed insulin doses."),
        ("Why is a cola a poor routine drink but sometimes used to treat a low?",
         ["It has no sugar", "It is fast sugar, but it also carries phosphate additives and empty calories", "It raises potassium", "It contains protein"], 1,
         "Fast sugar treats a low; glucose tablets do so without the phosphorus."),
        ("An SGLT2 inhibitor causes glucose to be:",
         ["Stored in the liver", "Passed in the urine", "Absorbed faster", "Turned into protein"], 1,
         "It blocks glucose reabsorption in the kidney."),
        ("Who gives sick-day instructions for pausing an SGLT2 inhibitor?",
         ["The dietitian", "The prescriber", "The pharmacist alone", "The patient decides"], 1,
         "The dietitian checks that the patient knows the instruction exists."),
        ("In the FLOW trial, semaglutide reduced the main kidney and heart outcome by about:",
         ["4%", "24%", "50%", "It did not"], 1,
         "Hazard ratio 0.76 over a median 3.4 years in 3,533 patients."),
        ("What should the dietitian watch for in a patient starting a GLP-1 receptor agonist?",
         ["Higher appetite", "A fall in intake below protein needs, nausea, and dehydration", "Rising potassium only", "Nothing"], 1,
         "Appetite can drop sharply; protein intake must be protected."),
        ("A patient cuts rice for glucose, meat for her kidneys, and fruit for potassium. The main risk is:",
         ["High phosphorus", "Too little energy and protein overall", "Weight gain", "High sodium"], 1,
         "Stacked restrictions can shrink intake below need."),
        ("Sarcopenic obesity means:",
         ["Low fat and high muscle", "Excess fat with low muscle mass and strength", "Normal weight", "Only high body mass index"], 1,
         "The scale can hide low muscle."),
        ("During weight loss in CKD, what should be tracked besides weight?",
         ["Hair growth", "Grip strength or a chair-stand test", "Eye color", "Shoe size"], 1,
         "Function shows whether muscle is being kept."),
        ("Which change belongs to the diabetes team, not the dietitian?",
         ["Packing a lunch", "Changing the insulin dose", "Measuring rice", "Keeping a snack in the bag"], 1,
         "Medicine doses belong to the prescriber."),
    ],
    "terms": [("Sulfonylurea", "A tablet that makes the pancreas release insulin; can cause lows in CKD."),
              ("Time in range", "The share of the day glucose stays in the target range on a sensor."),
              ("Ketoacidosis", "A serious buildup of acid from fat breakdown; rare with SGLT2 inhibitors."),
              ("Erythropoiesis-stimulating agent", "A medicine that tells the bone marrow to make red cells."),
              ("Chair-stand test", "How many times a person can stand from a chair in a set time.")],
    "readings": [("filipino-diabetic-diet.html", "A Filipino diabetic meal plan for patients."),
                 ("sugar-control-kidney-disease.html", "Glucose control when kidneys fail."),
                 ("obesity-ckd.html", "Weight and kidney disease.")],
    "calcs": ["calc-eag-hba1c.html", "calc-insulin-dose.html", "calc-sglt2i-eligibility.html", "calc-lowcarb-ckd-planner.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
