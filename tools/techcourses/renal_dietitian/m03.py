# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 03: Nutrition Assessment, Diagnosis, and Monitoring. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian measuring a seated patient's mid-arm with a tape, a handgrip dynamometer on the table.",
    "objectives": [
        "Build a weight timeline from comparable weights and calculate percent weight change correctly.",
        "Collect intake with a method suited to the question, and check it against an objective marker when one is available.",
        "Perform and record a basic nutrition-focused physical examination and handgrip strength test.",
        "Explain why serum albumin alone cannot diagnose malnutrition.",
        "Apply the criteria for protein-energy wasting (PEW) and the Global Leadership Initiative on Malnutrition (GLIM) criteria, and say how they differ.",
        "Write a problem, etiology, signs and symptoms (PES) statement with a measurable monitoring plan.",
    ],
    "big": """
{{plain:Assessing nutrition in kidney disease is like weighing a sponge. The sponge (muscle and fat) and the water it holds are on the scale together. A patient can lose three kilograms of muscle and gain three liters of fluid, and the scale will not move. Your work is to separate the sponge from the water, using the timing of the weight, the examination, and how the person functions.}}
{{cards:Key terms for this module|Dry weight (target weight)::The weight after dialysis at which the patient has no excess fluid and no symptoms of too little. Set by the nephrologist.|Protein-energy wasting (PEW)::Loss of body protein and energy stores in kidney disease, from low intake plus inflammation, acidosis, and catabolism.|Subjective Global Assessment (SGA)::A structured bedside rating of nutrition from history and examination; the 7-point version is used in dialysis.|Malnutrition-Inflammation Score (MIS)::A 10-item score for dialysis patients that adds laboratory values and body mass index to the SGA items.|Handgrip strength::Peak grip force measured with a dynamometer; a quick measure of muscle function.|PES statement::Problem, etiology, signs and symptoms: the format of a nutrition diagnosis.|Normalized protein catabolic rate (nPCR)::An estimate of protein intake from urea, valid only when the patient is stable.}}
{{flow:The assessment sequence|History::Weight timeline, intake, appetite, gut symptoms, function, food access.|Examination::Muscle, fat, edema, mouth and teeth, grip strength.|Data::Laboratory trends, dialysis adequacy, medicines.|Diagnosis::A PES statement with a cause you can act on.|Plan::One intervention, one measure, one date, one owner.}}
""",
    "case": {"title": "The denture", "html": """
<p>Mr. Reyes, 67, has been on hemodialysis for three years. His post-dialysis weight was 62.0 kg six weeks ago and 58.0 kg this week. Today, before dialysis, he weighs 61.0 kg, and the nurse remarks that &ldquo;his weight is about the same.&rdquo;</p>
<p>He tells you he has eaten about half his usual portions since a new lower denture began rubbing. His serum albumin fell from 3.9 to 3.3 g/dL during a chest infection last month. His temples look hollow, and his grip feels weak.</p>
""", "questions": ["Which two weights should be compared, and what is the percent loss?",
                  "What can and cannot be concluded from the albumin?",
                  "Write a PES statement with a cause you can act on this week."]},
    "sections": [
        ("weights", "Weights", "Build a timeline from comparable weights", """
<p>Weight in kidney disease is tissue plus fluid, and the fluid part can change by several kilograms in two days. Compare only like with like: post-dialysis with post-dialysis, a peritoneal dialysis weight taken the same way each time (drained or filled, stated in the note), or in CKD, morning weights with a note on edema. Record the date, the timing, and the source of every weight.[[kdoqi2020]]</p>
{{formula:Percent weight change = (earlier weight &minus; current weight) &divide; earlier weight &times; 100. Example: (62.0 &minus; 58.0) &divide; 62.0 &times; 100 = 6.5% loss in six weeks.}}
<p>Unintentional loss of 5% in three months or 10% in six months is one of the criteria for protein-energy wasting, and loss of more than 5% within six months is a GLIM phenotypic criterion.[[fouque2008]][[glim2019]] A falling post-dialysis weight with normal blood pressure and no cramps is likely tissue loss. A stable weight with rising blood pressure, new edema, or breathlessness can hide tissue loss replaced by fluid, and that should be raised with the nephrologist as a possible need to lower the dry weight.</p>
<p>Which weight goes into the calculations in later modules? KDOQI does not name one formula; it asks for clinical judgment that accounts for edema and body composition.[[kdoqi2020]] In practice, use the edema-free weight (post-dialysis or target weight) for most patients, and say in the note when you have used an adjusted or ideal weight for someone with obesity or severe wasting, and why.</p>
{{fig:rd03_weights}}
<p><strong>Example from practice.</strong> Mrs. Lacson, 59, is on peritoneal dialysis. In January the clinic weighed her at 58.5 kg with her daytime dwell of 2 liters in. In March they weighed her drained, at 57.0 kg, and the nurse recorded a 1.5 kg loss. Two liters of dialysis fluid weigh about 2 kg, so her January weight without fluid was about 56.5 kg. She has gained 0.5 kg, not lost 1.5. Write &ldquo;drained&rdquo; or &ldquo;full&rdquo; beside every PD weight, and compare only like with like.</p>
"""),
        ("intake", "Intake", "Measure intake, then check it", """
<p>Choose the method for the question. A 24-hour recall is quick and shows pattern and timing. A three-day food record that includes a dialysis day and a weekend day is the method KDOQI prefers for estimating energy and protein intake, because single days vary widely.[[kdoqi2020]] A food frequency list finds habits such as daily instant noodles or sweetened drinks. Ask about condiments at the table, broth, and food eaten outside the home; these carry most of the sodium.</p>
<p>All self-report under-counts. Where you can, check it. In a stable patient on dialysis, the nPCR estimates protein intake from urea; in CKD, a 24-hour urine urea nitrogen does the same.[[maroni1985]] Both are wrong when the patient is catabolic or building tissue, because urea then reflects more or less than intake. An nPCR of 0.8 g/kg/day in a patient who reports eating well is a prompt to ask again, not a verdict.</p>
{{cards:Questions that find the cause|Appetite::Is food unappealing all day or only after dialysis? Has taste changed? Any nausea or early fullness?|Mouth and gut::Dentures, sores, swallowing, constipation, diarrhea.|Access to food::Who shops and cooks? What is the food budget? Is there refrigeration?|Restrictions::Which foods has the patient stopped, and who advised it? Old or mistaken rules are a common cause of low intake.|Mood and burden::Low mood, fatigue after dialysis, pill burden, time lost to treatment.}}
<p><strong>Example from practice.</strong> Mr. Ferrer, 64 kg, has been on hemodialysis for two years. He says he eats well. His nPCR is 0.75 g/kg/day. His three-day food record shows 32 g of protein on the dialysis day, 68 g on a non-dialysis weekday, and 70 g on Sunday. The average is about 57 g, or 0.9 g/kg/day, which agrees broadly with the nPCR. A single 24-hour recall on a Sunday would have looked adequate. The record found the problem: on dialysis days he leaves at 5 a.m. and eats nothing until dinner.</p>
"""),
        ("exam", "Examination", "Examine, measure function, and read laboratory results in context", """
<p>A nutrition-focused physical examination takes five minutes. Look and feel for muscle loss at the temples, the collarbones, the shoulders, the shoulder blades, the back of the hand between thumb and forefinger, the thigh, and the calf. Check fat at the triceps and under the eyes. Press for edema at the ankles and, in a patient who lies in bed, over the sacrum. Look in the mouth. Examine after dialysis when possible, when fluid hides less.</p>
<p><strong>Handgrip strength</strong> measures function, which often falls before body measurements do. KDOQI suggests it as an indicator of protein-energy status and functional status when baseline data are available for comparison (a weak suggestion, grade 2B).[[kdoqi2020]] Measure on the arm without a fistula, seated, elbow at 90 degrees, best of three attempts, and compare the patient with himself over time.</p>
<p><strong>Structured tools.</strong> KDOQI recommends the 7-point Subjective Global Assessment as a valid and reliable tool for assessing nutritional status in adults with CKD stage 5 on dialysis (a firm recommendation, grade 1B), and says the Malnutrition-Inflammation Score may be used in maintenance hemodialysis and after transplantation (a weak suggestion, grade 2C).[[kdoqi2020]][[mis2001]] Routine screening at least twice a year for patients with CKD stages 3 to 5 and on dialysis is an expert-opinion statement.[[kdoqi2020]]</p>
<p><strong>Albumin.</strong> Serum albumin falls with inflammation, infection, fluid overload, protein lost in urine or dialysate, and liver disease. Inflammation both lowers its production and moves it out of the bloodstream. A low albumin predicts death and hospitalization on dialysis, so it must never be ignored, but it does not tell you how much the patient eats, and feeding alone often does not correct it while inflammation continues.[[kdoqi2020]] Read it as a marker of risk that asks &ldquo;why?&rdquo;</p>
{{fig:rd03_nfpe}}
<p><strong>Example from practice.</strong> Mrs. Pineda, 70, has a body mass index of 26 and an albumin of 3.6 g/dL, and on paper she looks well nourished. On examination her temples are hollow and her collarbones stand out. Her grip strength, measured on the arm without the fistula, has fallen from 18 to 13 kg in four months. Her 7-point SGA rating is 4, moderate malnutrition. The weight hides muscle loss under fat and fluid. The grip trend, compared with her own earlier results, is the earliest signal you have.[[kdoqi2020]]</p>
"""),
        ("diagnose", "Diagnosis", "Name the problem, then make the note actionable", """
<p>Two sets of criteria are in use. They overlap, and you should know which one your unit records.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Protein-energy wasting (ISRNM, 2008)</th><th>GLIM malnutrition (2019)</th></tr></thead>
<tbody>
<tr><td>Built for</td><td>Acute and chronic kidney disease</td><td>All adult patients, any setting</td></tr>
<tr><td>Rule</td><td>At least one item in three of four categories</td><td>At least one phenotypic and one etiologic criterion</td></tr>
<tr><td>Body mass</td><td>Body mass index below 23 kg/m&sup2;; unintentional weight loss of 5% in 3 months or 10% in 6 months; body fat below 10%</td><td>Weight loss above 5% in 6 months or above 10% beyond 6 months; low body mass index (Asia: below 18.5, or below 20 from age 70)</td></tr>
<tr><td>Muscle</td><td>Reduced muscle mass (5% in 3 months or 10% in 6 months); reduced mid-arm muscle circumference</td><td>Reduced muscle mass by a validated method</td></tr>
<tr><td>Intake</td><td>Unintended protein intake below 0.8 g/kg/day on dialysis (below 0.6 in CKD stages 2 to 5) or energy below 25 kcal/kg/day, for at least 2 months</td><td>Reduced intake or assimilation (etiologic)</td></tr>
<tr><td>Biochemistry or inflammation</td><td>Albumin below 3.8 g/dL; prealbumin below 30 mg/dL (dialysis); cholesterol below 100 mg/dL</td><td>Inflammation or disease burden (etiologic)</td></tr>
</tbody></table></div>
<p>Sources: International Society of Renal Nutrition and Metabolism (ISRNM) expert panel; GLIM consensus.[[fouque2008]][[glim2019]] The body mass index cut-off of 23 in the PEW criteria came from mortality data in dialysis populations; many healthy Filipino adults are below it, so do not label a stable, well, small-framed patient on that item alone.</p>
<p><strong>The PES statement.</strong> A nutrition diagnosis links a nutrition problem to a cause the dietitian can influence, with evidence. &ldquo;Hemodialysis&rdquo; and &ldquo;low albumin&rdquo; are not etiologies you can treat; &ldquo;pain on chewing&rdquo; and &ldquo;misses lunch on dialysis days&rdquo; are. Then write a plan that another person could carry out: one intervention the patient chose, one measure, one date, and who is responsible.[[doh_ncp2019]]</p>
{{stop:Intake falling together with unintentional weight loss, or weight loss with new weakness or infection, is not a routine finding. Report it to the nephrologist and nurse the same day, with the numbers, even while you start the nutrition plan.}}
<p><strong>Example from practice.</strong> Ms. Ignacio, 52, on peritoneal dialysis, has lost 4% of her body weight in three months. A weak note says: &ldquo;Malnutrition related to PD.&rdquo; A useful one says: &ldquo;Inadequate protein intake related to early fullness from the 2-liter daytime dwell, as evidenced by a 3-day intake of 0.7 g/kg/day against a prescription of 1.0 to 1.2 and a 4% weight loss in 3 months.&rdquo; The cause can be changed, by meal timing around drains and a question to the PD team about the dwell. The evidence can be measured again. The plan follows: five small meals with protein first, a reweigh and a repeat record in four weeks, and a message to the PD nurse.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Which weights should be compared?</strong> The two post-dialysis weights: (62.0 &minus; 58.0) &divide; 62.0 &times; 100 = 6.5% in six weeks. Today&rsquo;s pre-dialysis weight of 61.0 kg includes about 3 kg of fluid, and that is what made the nurse think nothing had changed. Tell the nephrologist: his dry weight may now be too high for the tissue he has left.</p>
<p><strong>What does the albumin tell you?</strong> Less than it seems. It fell during a chest infection. It marks him as a patient at high risk and fits the picture, but it is not proof that he eats too little, and it will not be your measure of whether the plan works over the next two weeks.</p>
<p><strong>What is the PES statement?</strong> &ldquo;Inadequate oral intake related to pain on chewing from an ill-fitting denture, as evidenced by reported half portions for six weeks, 6.5% loss on comparable post-dialysis weights, and visible muscle loss at the temples.&rdquo; He meets the protein-energy wasting criteria for body mass, intake, and biochemistry. The cause is one you can act on this week.</p>
<p><strong>What is the plan?</strong> Ask for a dental review. Agree on soft protein foods he likes: lugaw with egg and flaked fish, tofu, soft-cooked fish, taho without the syrup if his glucose allows. If his intake has not recovered in one to two weeks, discuss an oral supplement with the team. Check portions eaten and chewing pain by telephone at one week, and his post-dialysis weight and grip strength at two and four weeks. Report the weight loss to the nephrologist today. A scale reading the same number is the easiest place for wasting to hide, and the dietitian is often the one who finds it.</p>
"""],
    "skills": {"title": "Renal nutrition assessment and documentation",
               "intro": "Materials: a fictional chart with six weeks of weights, a tape measure, and a handgrip dynamometer if the unit has one.",
               "items": [
                   ("Selects comparable weights, states their timing, and calculates percent change correctly.", False),
                   ("Recognizes when a stable scale weight may hide tissue loss and says what to report to the nephrologist.", True),
                   ("Takes a recall that includes a dialysis day, condiments, broth, and food eaten outside the home.", False),
                   ("Asks about appetite, mouth and gut symptoms, food access, self-imposed restrictions, and mood.", False),
                   ("Examines at least five muscle sites and checks for edema, and records findings in plain terms.", False),
                   ("Measures handgrip strength on the non-access arm, best of three, and records the position used.", False),
                   ("Explains to the preceptor why albumin alone does not diagnose malnutrition.", False),
                   ("Writes a PES statement whose etiology the plan can address, with one measure, one date, and one owner.", False),
                   ("Reports combined intake decline and weight loss to the team the same day.", True),
               ],
               "placement": "Complete one full assessment under supervision, using your unit&rsquo;s screening tool, and compare your SGA rating with your preceptor&rsquo;s."},
    "quiz": [
        ("A patient&rsquo;s post-dialysis weight was 62 kg six weeks ago and is 58 kg now. Today&rsquo;s pre-dialysis weight is 61 kg. The percent loss is:",
         ["1.6%", "4.9%", "6.5%", "It cannot be calculated"], 2,
         "Compare post-dialysis with post-dialysis: (62 − 58) ÷ 62 × 100 = 6.5%."),
        ("Why is the pre-dialysis weight a poor measure of tissue change?",
         ["Scales are less accurate before dialysis", "It includes fluid gained since the last session", "Patients wear more clothing", "It is always lower"], 1,
         "Interdialytic fluid can add several kilograms and hide tissue loss."),
        ("A stable weight with rising blood pressure and new ankle edema may mean:",
         ["Good nutrition", "Tissue loss replaced by fluid; the dry weight may need review", "Too little sodium", "Nothing"], 1,
         "Fluid can replace lost tissue at the same scale weight. Report it to the nephrologist."),
        ("Which intake method does KDOQI prefer for estimating energy and protein intake?",
         ["A single 24-hour recall", "A three-day food record", "Serum albumin", "Body mass index"], 1,
         "A three-day record, including a dialysis day and a non-dialysis day, reduces day-to-day error."),
        ("The nPCR is unreliable as a measure of protein intake when the patient is:",
         ["Stable", "Catabolic or anabolic", "On hemodialysis", "Vegetarian"], 1,
         "Urea then reflects tissue breakdown or building, not intake alone."),
        ("Which is NOT a cause of low serum albumin?",
         ["Inflammation", "Fluid overload", "Protein loss in urine or dialysate", "High handgrip strength"], 3,
         "Albumin falls with inflammation, dilution, losses, and liver disease."),
        ("Which tool does KDOQI firmly recommend (grade 1B) for assessing nutritional status in adults on dialysis?",
         ["Body mass index alone", "7-point Subjective Global Assessment", "Serum cholesterol", "Waist circumference"], 1,
         "The 7-point SGA is recommended as valid and reliable in CKD stage 5 on dialysis."),
        ("On which arm should handgrip be measured in a hemodialysis patient with a fistula?",
         ["The fistula arm", "The arm without the fistula", "Either arm", "Neither; use leg strength"], 1,
         "Protect the access arm; measure the other side the same way each time."),
        ("How many of the four ISRNM categories must be met to diagnose PEW?",
         ["One", "Two", "Three", "All four"], 2,
         "At least one item in three of the four categories."),
        ("The GLIM diagnosis requires:",
         ["A low albumin", "One phenotypic and one etiologic criterion", "Three laboratory abnormalities", "A body mass index below 23"], 1,
         "GLIM combines a phenotype (weight loss, low body mass index, or low muscle) with a cause (reduced intake or inflammation)."),
        ("Which etiology makes a PES statement actionable?",
         ["Related to hemodialysis", "Related to low albumin", "Related to pain on chewing", "Related to age"], 2,
         "The etiology should be something the nutrition plan can change."),
        ("Unintentional weight loss that meets the ISRNM body-mass criterion is:",
         ["2% in 1 month", "5% in 3 months or 10% in 6 months", "Any loss", "15% in a year"], 1,
         "These thresholds are part of the PEW body-mass category."),
        ("A small-framed, well, active patient has a stable body mass index of 21. On the PEW body mass index item alone you should:",
         ["Diagnose PEW", "Not diagnose PEW; one item in one category is not enough, and the cut-off came from other populations", "Start tube feeding", "Ignore weight from now on"], 1,
         "PEW needs three categories. The 23 kg/m² cut-off is applied with judgment in small-framed adults."),
        ("Intake has halved and weight has fallen 6% in six weeks. Besides starting a plan, you should:",
         ["Wait for next month&rsquo;s laboratory results", "Report it to the nephrologist and nurse the same day", "Tell the patient to eat more", "Recheck albumin weekly"], 1,
         "Combined intake decline and weight loss needs prompt team review."),
        ("A good monitoring plan states:",
         ["&ldquo;Continue to monitor&rdquo;", "One measure, one date, and who is responsible", "The dietitian&rsquo;s name only", "A list of all laboratory tests"], 1,
         "A plan another person could carry out names the measure, the time, and the owner."),
    ],
    "terms": [("Comparable weights", "Weights taken at the same point in the treatment cycle, so fluid differences cancel out."),
              ("Nutrition-focused physical examination", "A structured look and feel for muscle loss, fat loss, and fluid."),
              ("Inflammation", "The body&rsquo;s response to injury or infection; it lowers albumin and appetite and speeds muscle loss."),
              ("Sarcopenia", "Low muscle mass with low strength or performance."),
              ("Etiology", "The cause, in a PES statement."),
              ("ISRNM", "International Society of Renal Nutrition and Metabolism."),
              ("GLIM", "Global Leadership Initiative on Malnutrition.")],
    "readings": [("kain-pa-rin.html", "Poor appetite in kidney disease, written for patients and families."),
                 ("dry-weight-determination.html", "How the nephrologist sets and revises the dry weight."),
                 ("eating-on-dialysis.html", "What patients are told about protein on dialysis.")],
    "calcs": ["calc-nutrition-screening.html", "calc-hd-adequacy-npcr.html", "calc-sarcopenia-sarcf.html", "calc-bmi-bsa-ibw.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
