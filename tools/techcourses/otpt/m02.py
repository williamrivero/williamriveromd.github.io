# -*- coding: utf-8 -*-
"""OT/PT track, Module 02: Kidney Disease Through a Functional Lens. Written for this series from published sources."""

MODULE = {
    "image_alt": "A therapist and an older man on a landing halfway up a hospital staircase, the man resting a hand on the rail.",
    "objectives": [
        "Explain the capacity&ndash;demand gap and use it to describe a renal patient&rsquo;s functional problem.",
        "Trace how muscle protein breakdown, anemia, acidosis, fluid shifts, neuropathy and bone disease each reduce function.",
        "Link common renal findings in the chart to functional signs you can observe and measure.",
        "Recognize frailty and its prevalence in people on dialysis, and what it predicts.",
        "Explain why the dialysis schedule itself shapes when and how a person can be active.",
    ],
    "big": """
{{plain:Every task has a price, and every person has a budget. Climbing one flight of stairs costs a healthy 60-year-old a small part of what their legs and heart can give. For a 60-year-old on dialysis, the same flight may cost most of it. Nothing about the stairs changed. The budget shrank.}}
{{fig:otpt00_capacity_gap}}
<p>The picture has a limit. The budget is not one number. Aerobic capacity, muscle strength, balance and blood pressure control each run their own account, and kidney failure drains them at different rates. A man may walk 300 meters on the flat yet fail to rise from a low <em>bangko</em> without his arms. Your assessment finds which account is short, because each one is fixed differently.</p>
<p>This module gives you the physiology behind the shrinking budget. You do not need to manage these problems medically; the nephrologist does. You need to recognize them, because each one changes what is safe and what will work.</p>
{{cards:Key terms for this module|Capacity::The maximum a person can do: aerobic capacity, strength, balance.|Demand::What a task requires of that capacity.|Sarcopenia::Loss of muscle mass and strength beyond normal aging.|Frailty::Reduced physiological reserve, so a small stress causes a large decline.|Uremia::The toxic state of advanced kidney failure, from retained waste products.}}
""",
    "case": {"title": "Four findings, four problems", "html": """
<p><strong>Thursday, 2:10 p.m.</strong> OT Bea Santiago and PT Carlo Dizon review the chart of Mr. Ernesto Villanueva, 64, on hemodialysis for two years, before seeing him together.</p>
<p>His most recent results and notes list: hemoglobin 92 g/L; serum bicarbonate 18 mmol/L; serum albumin 33 g/L; average interdialytic weight gain 3.2 kilograms; &ldquo;postural dizziness after HD&rdquo;; &ldquo;burning feet, decreased vibration sense&rdquo;; and a wrist fracture last year after a minor slip. He takes metoprolol.</p>
<p>His wife says he now sits most of the day, &ldquo;because everything tires him.&rdquo;</p>
""", "questions": ["Which functional problem does each finding most likely contribute to?",
                  "Which of these findings changes how you will screen and test him?",
                  "Which problems belong to the renal team to treat, and which can rehabilitation address directly?"]},
    "sections": [
        ("muscle", "Why muscle shrinks", "Muscle in kidney failure: breakdown outpaces building", """
<p>Muscle is never fixed. It is rebuilt every day, with protein synthesis on one side and protein breakdown on the other. In kidney failure the balance tips toward breakdown. Metabolic acidosis activates the cell&rsquo;s protein-recycling machinery (the ubiquitin&ndash;proteasome pathway). Chronic inflammation and insulin resistance blunt the signals that build muscle. Poor appetite and dietary restrictions reduce the protein supply, and dialysis itself removes amino acids. Add inactivity, the strongest driver of all, and muscle shrinks.</p>
{{fig:otpt02_muscle}}
<p>What you see is weakness in the large leg muscles first: a slow, arm-assisted rise from a chair, difficulty with stairs, a shorter step. In a cohort of adults with CKD stages 2 to 4, lower-extremity performance was at least 30 percent below predicted while handgrip was relatively preserved.[[otpt_roshanravan2013]] That is why handgrip alone can miss the problem; test the legs.</p>
{{key:In kidney failure, test the legs, not just the grip. Leg strength fails first.}}
"""),
        ("oxygen", "Oxygen and blood pressure", "Less oxygen delivered, less stable pressure", """
<p><strong>Anemia.</strong> The failing kidney makes too little erythropoietin, so red cells fall. Less hemoglobin means less oxygen carried to working muscle, so the same walk demands a higher heart rate and feels harder. Breathlessness and early fatigue on exertion are expected; a sudden change is not, and goes to the nurse.</p>
<p><strong>The heart.</strong> Many people on dialysis have a thickened left ventricle and vascular stiffness from years of high blood pressure and fluid load. The heart fills less easily and tolerates fast swings in volume poorly.</p>
<p><strong>Fluid and pressure swings.</strong> Between sessions, fluid accumulates; during dialysis, ultrafiltration removes it, often two to three liters in four hours. Plasma volume falls faster than it can refill from the tissues. Add autonomic neuropathy (common with diabetes) and medicines such as beta-blockers, and the reflex that keeps blood pressure up when a person stands is weak. That is why dizziness after dialysis is common, and why Module 3 makes screening on standing a habit.</p>
{{key:A breathless walk can be anemia; a dizzy stand can be fluid removal. Neither is a reason to stop rehabilitation, but both change when and how you test.}}
"""),
        ("nerves-bones", "Nerves, bones and brain", "Balance, bones and thinking", """
<p><strong>Peripheral neuropathy.</strong> Uremia and diabetes damage long nerves first: burning or numb feet, lost vibration and position sense. Without accurate signals from the feet, balance depends on vision and slow conscious correction. People with neuropathy walk with a wider base, look down, and fall when lighting is poor or the ground is uneven.</p>
<p><strong>Bone disease.</strong> CKD&ndash;mineral and bone disorder (CKD-MBD) disturbs calcium, phosphate, parathyroid hormone and vitamin D, weakening bone. In a United States Renal Data System analysis, the relative risk of hip fracture in people on dialysis was about 4.4 times that of the general population of the same sex.[[otpt_alem2000]] A fall that bruises a healthy person can break a dialysis patient&rsquo;s hip.</p>
<p><strong>Cognition.</strong> Many people on hemodialysis have unrecognized cognitive impairment (Module 7). It affects how they learn an exercise, follow a plan, and judge risk.</p>
{{key:Neuropathy and fragile bones turn a stumble into a fracture. Balance training and fall prevention are not optional extras in this population.}}
"""),
        ("frailty", "Frailty", "Frailty: when reserve runs out", """
{{fig:otpt02_cascade}}
<p>Frailty is what happens when all these accounts run low together. A frail person may manage a quiet day, but a small stress&mdash;a missed session, an infection, a hospital stay&mdash;tips them into a large and lasting loss of function.</p>
<p>Frailty is common in dialysis. A meta-analysis pooled its prevalence in hemodialysis at 34.3 percent, ranging from 6 to 82 percent depending on the tool and the population.[[zhao2020]] In a large United States cohort of people starting dialysis, 67.7 percent were frail by that study&rsquo;s definition, and frailty was associated with death (adjusted hazard ratio 2.24) and with death or hospitalization.[[johansen2007]] Both are observational: frailty marks risk; it does not prove that treating frailty changes survival. The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline asks clinicians to fit physical activity advice to each person&rsquo;s cardiovascular health, tolerance and frailty, and to consider referral to rehabilitation professionals.[[otpt_kdigo2024]]</p>
<p>Two quick screens are useful on the floor: the Clinical Frailty Scale (CFS), a 1 to 9 judgment based on function,[[rockwood2005]] and the SARC-F questionnaire for sarcopenia. Neither replaces your performance tests (Module 5).</p>
{{key:Frailty is a reserve problem. The question is not only what the person can do today, but how much a bad week will cost them.}}
"""),
        ("schedule", "The dialysis week", "How the schedule shapes the week", """
<p>A person on hemodialysis three times a week spends about 12 hours a week sitting in the chair, plus travel and waiting, often 20 hours or more. After a session, many feel washed out for hours; the time to recover varies widely between people (Module 6). The long weekend gap leaves the most fluid on board before the first session of the week.</p>
<p>For you, this means three practical rules. Test at a consistent point in the week so results can be compared. Plan more demanding work on non-dialysis days or early in a session (Module 10). And never judge a person&rsquo;s capacity by how they look straight after dialysis.</p>
{{key:Always record which day of the dialysis week, and how long after a session, you measured.}}
"""),
    ],
    "debrief": ["""
<p><strong>Mapping findings to function.</strong> Hemoglobin of 92 g/L (anemia) contributes to breathlessness and early fatigue. Bicarbonate of 18 mmol/L (acidosis) and albumin of 33 g/L point toward muscle breakdown and poor nutritional reserve, feeding leg weakness. Large interdialytic weight gains and postural dizziness after dialysis, with metoprolol blunting the heart-rate response, raise the risk of blood pressure falling on standing. Burning feet and lost vibration sense mean neuropathy and poor balance. A wrist fracture after a minor slip suggests fragile bone.</p>
<p><strong>What changes the screen and tests.</strong> The dizziness and beta-blocker mean Carlo checks symptoms and blood pressure on standing, never relies on heart rate alone for intensity, and avoids testing straight after dialysis. Neuropathy and the fracture history mean close guarding for balance tests.</p>
<p><strong>Who treats what.</strong> Anemia, acidosis, fluid gains and bone disease are the renal team&rsquo;s to treat; Carlo and Bea report what they see (for example, worsening dizziness). Rehabilitation directly addresses leg weakness, endurance, balance, transfers, the bathing routine and the &ldquo;everything tires him&rdquo; spiral of inactivity.</p>
"""],
    "skills": {"title": "Chart-to-function mapping",
               "intro": "Review a deidentified renal chart and present a functional problem list to your preceptor.",
               "items": [
                   ("Identifies treatment modality, schedule and access from the chart.", False),
                   ("Links at least four renal findings to plausible functional consequences, explaining the mechanism of each.", False),
                   ("Identifies findings that change screening or testing safety (for example, postural symptoms, beta-blocker, neuropathy, fracture).", True),
                   ("Distinguishes problems the renal team treats from those rehabilitation addresses directly.", True),
                   ("Scores a Clinical Frailty Scale and explains the score in function terms.", False),
                   ("Presents a three-line functional problem list in the patient&rsquo;s own goal language.", False),
               ],
               "placement": "Map the charts of three patients on your caseload to functional problem lists and compare them with what the patients say limits them."},
    "terms": [("Capacity", "What a person can do at most: endurance, strength, balance."),
              ("Demand", "What a task requires."), ("Sarcopenia", "Low muscle strength and mass."),
              ("Frailty", "Low reserve; small stresses cause large declines."),
              ("Interdialytic weight gain", "Fluid weight gained between dialysis sessions."),
              ("Autonomic neuropathy", "Nerve damage that weakens the reflexes that keep blood pressure up on standing.")],
    "readings": [("hemodialysis-elderly.html", "Older adults on dialysis: frailty, falls and goals."),
                 ("ckd-associated-osteoporosis.html", "Why bones break more easily in kidney disease."),
                 ("anemia-management.html", "Anemia in kidney disease, and why it makes people tired.")],
    "calcs": ["calc-frailty-assessment.html", "calc-sarcopenia-sarcf.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["02"])
