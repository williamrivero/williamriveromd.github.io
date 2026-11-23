# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 02: How the Kidney Handles Nutrients. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian sketching a kidney and a plate of food on a whiteboard for two colleagues.",
    "objectives": [
        "Trace dietary protein to urea and explain why protein intake changes blood urea but also muscle mass.",
        "Explain how sodium intake controls thirst, body water, and blood pressure when the kidney cannot excrete it.",
        "Describe the two ways the body handles a potassium load: shifting it into cells within minutes and excreting it over hours.",
        "Explain how phosphorus retention leads to high parathyroid hormone and bone disease before serum phosphorus rises.",
        "Explain how diet produces acid, how the kidney removes it, and what acidosis does to muscle and bone.",
        "Connect each mechanism to one nutrition decision you will make in later modules.",
    ],
    "big": """
{{plain:A healthy kidney is a very forgiving accountant. Eat more salt, potassium, or protein today, and it simply writes a larger check to the urine tonight, so the blood stays the same. A failing kidney can still write checks, but smaller ones and more slowly. Blood levels then begin to follow the diet. The analogy stops at one point: the kidney is also a gland, and losing its hormones (active vitamin D, erythropoietin) causes problems that no diet can fully correct.}}
{{cards:Key terms for this module|Nephron::One of about a million filtering units in each kidney: a filter (glomerulus) joined to a long processing tube (tubule).|Urea::The main nitrogen waste made by the liver from protein; measured as blood urea nitrogen (BUN).|Uremia::The illness caused by retained wastes: poor appetite, nausea, altered taste, itching, fatigue.|Aldosterone::An adrenal hormone that makes the kidney and colon keep sodium and excrete potassium.|Parathyroid hormone (PTH)::A hormone that raises blood calcium and makes the kidney excrete phosphorus.|Fibroblast growth factor 23 (FGF23)::A bone hormone that makes the kidney excrete phosphorus and lowers active vitamin D.|Net endogenous acid production::The acid the body makes each day from food, mainly from animal protein, minus the alkali from fruits and vegetables.}}
{{flow:From plate to blood: the same path for every nutrient|Intake::How much is eaten, and in what form.|Absorption::How much crosses the gut; this varies widely for phosphorus.|Distribution::Where it goes: blood, cells, or bone.|Excretion::What the kidney, the bowel, or dialysis removes.|Blood level::The result of all four, not of intake alone.}}
""",
    "case": {"title": "The same lunch, three patients", "html": """
<p>Three people eat the same lunch: a cup and a half of rice, a large piece of fried bangus, a bowl of sinigang with kangkong and radish, patis on the side, and a banana.</p>
<p>Ana, 30, has healthy kidneys. Ben, 62, has CKD G4 and takes an angiotensin receptor blocker. Carlos, 55, has no urine output and is on hemodialysis three times a week; his next session is in two days.</p>
""", "questions": ["What happens to the sodium, potassium, phosphorus, and protein nitrogen in each person over the next 24 hours?",
                  "Whose blood results will change the most, and why?",
                  "Which single meal would you worry about least?"]},
    "sections": [
        ("nitrogen", "Protein", "Protein, urea, and the price of restriction", """
<p>Protein is the only macronutrient that carries nitrogen. When amino acids are used for energy, the liver removes the nitrogen and packs it into urea, and the kidneys excrete it. In a person in balance, urea production tracks protein intake closely. This is the basis of estimating protein intake from urea: from a 24-hour urine urea nitrogen in CKD, or from urea kinetics on dialysis as the normalized protein catabolic rate.[[maroni1985]][[kdoqi2020]]</p>
{{formula:Estimated protein intake (g/day) = 6.25 &times; [urine urea nitrogen (g/day) + 0.031 &times; body weight (kg)]. Valid only in a stable patient; add urinary protein losses when they are heavy.}}
<p>When filtration falls, urea and other nitrogen wastes build up. Some of them blunt appetite and change taste, which is why patients with advanced CKD often say that meat &ldquo;tastes like metal.&rdquo; Lowering protein intake lowers the production of these wastes and of acid and phosphorus, which mostly travel with protein. A high protein load also raises pressure inside the remaining filters (hyperfiltration), a mechanism thought to speed their loss.</p>
<p>There is a price. The body has no protein store apart from its working tissue. If protein or energy intake falls below need, muscle is broken down to supply amino acids. Acidosis, inflammation, and insulin resistance in CKD make muscle breakdown easier and rebuilding harder. A low-protein diet without enough energy therefore does harm, and Module 4 treats energy and protein as one prescription.</p>
{{fig:rd02_nitrogen}}
{{key:Urea reflects the balance of protein eaten, muscle broken down, and what the kidney or dialysis removes. A rising urea in a patient who is eating less means catabolism or bleeding, not too much meat.}}
"""),
        ("sodium", "Sodium and water", "Sodium decides thirst, water, and pressure", """
<p>Sodium is the main particle outside cells, and water follows it. The brain defends the concentration of sodium in blood, not the amount. After a salty meal, the concentration rises slightly, thirst and antidiuretic hormone respond, and water is retained until the concentration is normal again. The body now holds more sodium and more water at the same concentration. A healthy kidney excretes the surplus within a day or two.</p>
<p>A diseased kidney excretes it slowly, and a patient without urine cannot excrete it until the next dialysis. The retained salt water expands the blood volume and raises blood pressure. This is why blood pressure in CKD is &ldquo;salt-sensitive&rdquo; and why sodium reduction lowers it: across 21 randomized trials in people with CKD, lowering intake by about 1,700 mg of sodium a day reduced blood pressure by about 7/4 mm Hg, with high certainty, although the trials were too short to show effects on kidney failure or death.[[mcmahon2021]]</p>
{{cards:What follows from the physiology|Thirst is a sodium problem::A patient on dialysis who is told to drink less but still eats salty food will be thirsty and will drink. Teach sodium first, fluid second.|Serum sodium is not a salt gauge::A normal serum sodium says the water matches the salt. It does not say the total is right. Weight and blood pressure do.|A low serum sodium is usually too much water::It is rarely a reason to eat more salt. Report it; do not treat it with patis.}}
"""),
        ("potassium", "Potassium", "Potassium: a fast shift and a slow exit", """
<p>About 98% of the body&rsquo;s potassium is inside cells. The amount in the blood is small, and the heart is sensitive to it, so the body has two defenses against a potassium-rich meal. Within minutes, insulin and adrenaline push potassium into muscle and liver cells. Over hours, the kidney excretes it, driven by aldosterone and by the delivery of sodium and water to the far end of the tubule. The colon excretes a small share, which grows as kidney function falls.[[clase2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Defense</th><th>What weakens it</th><th>What you ask about</th></tr></thead>
<tbody>
<tr><td>Shift into cells (insulin)</td><td>Insulin deficiency, high glucose, prolonged fasting, acidosis</td><td>Glucose control, skipped meals, bicarbonate level</td></tr>
<tr><td>Kidney excretion (aldosterone)</td><td>Low eGFR; ACE inhibitors, angiotensin receptor blockers, spironolactone, finerenone; nonsteroidal anti-inflammatory drugs; trimethoprim; volume depletion</td><td>New or changed medicines, pain relievers, recent diarrhea or poor intake</td></tr>
<tr><td>Colon excretion</td><td>Constipation</td><td>Bowel habit, fiber and fluid, constipating medicines</td></tr>
<tr><td>Dialysis removal</td><td>Missed or shortened sessions, access problems</td><td>Attendance, the long gap between sessions</td></tr>
</tbody></table></div>
<p>The form of the potassium matters as well. Potassium chloride in salt substitutes and potassium additives in processed foods are absorbed almost completely. Potassium in whole plant foods comes with fiber, which speeds bowel transit, and with alkali, which helps move potassium into cells. In a cohort of 8,043 adults on hemodialysis, higher reported dietary potassium was not associated with higher serum potassium or with death; the study was observational and relied on food questionnaires, so it does not prove that intake is irrelevant, but it argues against blaming food first.[[bernier2021]]</p>
{{fig:rd02_potassium}}
"""),
        ("phosphorus", "Phosphorus and acid", "Phosphorus, bone hormones, and acid", """
<p>Phosphorus is absorbed in the small intestine, stored mostly in bone, and excreted by the kidney. As nephrons are lost, each remaining nephron must excrete more. Two hormones make that happen: fibroblast growth factor 23 (FGF23) from bone, and parathyroid hormone (PTH). Both rise early, and for years they keep serum phosphorus normal. The cost is high PTH, low active vitamin D (FGF23 switches off its production), and progressive bone and blood vessel disease, together called chronic kidney disease&ndash;mineral and bone disorder (CKD-MBD).[[kdigo_mbd2017]]</p>
<p>Two points follow for a dietitian. A normal serum phosphorus in G3 to G4 CKD does not mean phosphorus handling is normal. And how much phosphorus is absorbed depends on its source: roughly 40% to 60% from animal foods, less from plant foods where much is bound as phytate, and nearly all from inorganic phosphate additives.[[kalantar2010]] In a one-week crossover study of nine patients with CKD, a vegetarian diet with the same phosphorus content as a meat diet led to lower serum phosphorus and lower FGF23.[[moe2011]] The study was small and short, but it supports reading ingredient lists before removing whole foods.</p>
<p><strong>Acid.</strong> Metabolizing animal protein and grains produces acid; fruits and vegetables supply alkali. A healthy kidney excretes the net acid each day, mostly as ammonium. A failing kidney cannot, and serum bicarbonate falls. The body then buffers acid with bone and breaks down muscle protein, so chronic acidosis contributes to bone loss and wasting and is associated with faster loss of kidney function.[[kdoqi2020]] This is the mechanism behind using fruits and vegetables, or sodium bicarbonate, to correct acidosis (Module 6).</p>
{{flow:Why phosphorus stays &ldquo;normal&rdquo; while damage accumulates|Fewer nephrons::Less phosphorus is filtered.|FGF23 rises::Each nephron excretes more; active vitamin D falls.|Calcium absorption falls::Blood calcium tends to drop.|PTH rises::Bone releases calcium and phosphorus; the kidney excretes more phosphorus.|Late stage::Serum phosphorus finally rises, usually in G4 to G5.}}
{{key:Blood levels are late signals. By the time potassium or phosphorus is high, the body&rsquo;s compensations have been working for years. Ask what changed recently, in medicines, bowel habit, dialysis, or intake, before changing the diet.}}
"""),
    ],
    "debrief": ["""
<p><strong>What happens in Ana, with healthy kidneys?</strong> Her kidneys pass the extra sodium, potassium, phosphorus, and urea within a day. By tomorrow her blood results look the same as yesterday&rsquo;s.</p>
<p><strong>What happens in Ben, with G4 CKD on an angiotensin receptor blocker?</strong> He clears all four, but slowly. The salt raises his blood pressure and may swell his ankles for a day or two. His potassium exit is narrowed twice, by low eGFR and by his medicine, so the banana, the leafy sinigang, and the fish matter more for him than for Ana, and more again if he is constipated. His phosphorus will probably stay normal, because FGF23 and PTH rise to push it out. Normal here does not mean healthy.</p>
<p><strong>What happens in Carlos, who makes no urine?</strong> Almost nothing leaves until dialysis, except a little potassium through the bowel. The salt makes him thirsty, and whatever he drinks stays as weight. Insulin holds potassium in his cells for a while, then the blood level climbs over two days. Dialysis removes only part of the phosphorus, so the binder he takes with this meal matters. His results change the most.</p>
<p><strong>Which meal would you worry about least?</strong> Ana&rsquo;s. For Ben and Carlos, one lunch matters less than the pattern of every lunch, and less than the medicines, bowel habit, and dialysis schedule in the table above. When you can explain a result from physiology, you will stop blaming the banana for problems a banana did not cause.</p>
"""],
    "skills": {"title": "Explaining a laboratory result from physiology",
               "intro": "The preceptor gives three fictional results. For each, explain the mechanism aloud in plain language before proposing any food change.",
               "items": [
                   ("Explains why a rising urea in a patient who is eating less suggests muscle breakdown or another source, not excess protein.", False),
                   ("Explains to a simulated patient why salty food causes thirst and weight gain between dialysis sessions.", False),
                   ("Names at least three non-diet causes of a high potassium before discussing food.", True),
                   ("Explains why serum phosphorus can be normal while PTH is high.", False),
                   ("Explains how acidosis leads to muscle and bone loss, and names two ways to correct it.", False),
                   ("States that a low serum sodium is reported to the physician and is not treated by adding salt.", True),
                   ("Uses the intake, absorption, distribution, excretion sequence to organize the explanation.", False),
               ],
               "placement": "Choose one patient&rsquo;s monthly results with your preceptor and write a three-line physiological explanation for each abnormal value."},
    "quiz": [
        ("Which nutrient is the source of urea?", ["Carbohydrate", "Fat", "Protein", "Fiber"], 2,
         "Urea is made by the liver from the nitrogen in amino acids."),
        ("A patient with CKD eats less for two weeks, and his urea rises. The most likely explanation is:",
         ["He is secretly eating more meat", "His own muscle is being broken down, or there is another source such as bleeding", "Urea does not depend on protein", "The laboratory made an error"], 1,
         "With low intake, a rising urea points to catabolism or another nitrogen source."),
        ("After a salty meal, what does the body defend first?",
         ["The total amount of sodium", "The concentration of sodium in the blood", "Urine volume", "Blood potassium"], 1,
         "Thirst and antidiuretic hormone restore concentration by retaining water, which expands volume."),
        ("Why does telling a hemodialysis patient to &ldquo;drink less&rdquo; often fail on its own?",
         ["Patients forget", "Thirst is driven by sodium intake, so salt must be reduced first", "Water is not absorbed", "Dialysis causes thirst"], 1,
         "Sodium raises the blood concentration and triggers thirst. Lowering sodium lowers the drive to drink."),
        ("In the Cochrane review of salt reduction in CKD, the blood pressure fell by about:",
         ["1/1 mm Hg", "7/4 mm Hg", "20/10 mm Hg", "It did not fall"], 1,
         "Lowering sodium by about 1,700 mg a day reduced blood pressure by about 7/4 mm Hg; trials were short."),
        ("About how much of the body&rsquo;s potassium is inside cells?", ["2%", "50%", "75%", "98%"], 3,
         "Nearly all potassium is intracellular, so small shifts change the blood level."),
        ("Which hormone moves potassium into cells within minutes of a meal?", ["Aldosterone", "Insulin", "Parathyroid hormone", "Erythropoietin"], 1,
         "Insulin, with adrenaline, drives potassium into cells. Fasting and insulin deficiency weaken this."),
        ("Which of these lowers kidney potassium excretion?",
         ["A loop diuretic", "Spironolactone", "A high-fiber diet", "Sodium bicarbonate"], 1,
         "Spironolactone blocks aldosterone, which the kidney needs to excrete potassium."),
        ("Why does constipation matter for potassium in advanced CKD?",
         ["The colon excretes a growing share of potassium as kidney function falls", "Constipation raises insulin", "Stool contains no potassium", "It does not matter"], 0,
         "Colonic excretion becomes more important as eGFR falls, and constipation reduces it."),
        ("Which source of phosphorus is absorbed most completely?",
         ["Phytate in beans", "Phosphorus in fresh fish", "Inorganic phosphate additives", "Phosphorus in brown rice"], 2,
         "Additives are nearly fully absorbed; plant phytate is the least available."),
        ("In early CKD, serum phosphorus is usually normal because:",
         ["Patients eat less phosphorus", "FGF23 and PTH rise and force the remaining nephrons to excrete more", "The gut stops absorbing it", "Bone stores all of it"], 1,
         "Hormonal compensation keeps the level normal for years, at the cost of high PTH and low active vitamin D."),
        ("Which foods add the most acid load?",
         ["Fruits", "Vegetables", "Animal protein and grains", "Water"], 2,
         "Animal protein and grains produce acid; fruits and vegetables supply alkali."),
        ("Chronic metabolic acidosis in CKD contributes to:",
         ["Muscle and bone loss", "Weight gain", "Low potassium", "High hemoglobin"], 0,
         "Acid is buffered by bone and promotes muscle protein breakdown."),
        ("The Maroni formula estimates protein intake from:",
         ["Serum albumin", "24-hour urine urea nitrogen and body weight", "Body mass index", "Serum creatinine"], 1,
         "It uses urine urea nitrogen plus a weight-based estimate of non-urea nitrogen, in a stable patient."),
        ("In a large cohort on hemodialysis, higher reported dietary potassium was:",
         ["Strongly linked to hyperkalemia", "Not associated with serum potassium or death", "Proven to be protective", "Not measured"], 1,
         "The association was null; the study was observational, so it informs but does not settle practice."),
    ],
    "terms": [("Hyperfiltration", "Raised pressure and flow in the remaining filters, thought to speed their loss."),
              ("Catabolism", "Breakdown of body tissue, especially muscle, to supply energy or amino acids."),
              ("Phytate", "The storage form of phosphorus in seeds and grains, poorly absorbed by humans."),
              ("Salt-sensitive blood pressure", "Blood pressure that rises and falls with sodium intake."),
              ("Normalized protein catabolic rate (nPCR)", "An estimate of protein intake from urea kinetics in a stable dialysis patient."),
              ("Bicarbonate", "The main buffer in blood; a low value indicates metabolic acidosis."),
              ("CKD-MBD", "Chronic kidney disease&ndash;mineral and bone disorder.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "Potassium physiology for patients, with the medicine causes."),
                 ("phosphorus-ckd.html", "Sources of phosphorus and how binders work."),
                 ("sodium-salt-reduction-ckd.html", "Sodium, thirst, and blood pressure in plain language.")],
    "calcs": ["calc-urine-protein-excretion.html", "calc-npcr.html", "calc-na-balance.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
