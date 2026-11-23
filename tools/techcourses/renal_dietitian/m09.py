# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 09: Medical Nutrition Therapy in Maintenance Hemodialysis. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient in a hemodialysis chair eating a small packed meal while a dietitian reviews a chart with the nurse.",
    "objectives": [
        "Explain why protein needs rise when hemodialysis (HD) starts, and rewrite a pre-dialysis plan.",
        "Assess intake on a dialysis day and a non-dialysis day, including the long gap.",
        "Weigh the benefits and risks of eating during treatment.",
        "Use oral nutrition supplements in a stepwise plan, and say what the trials show about intradialytic parenteral nutrition (IDPN).",
        "Adapt advice for twice-weekly and incremental schedules.",
        "Recognize when a fall in intake or weight needs the nephrologist today.",
    ],
    "big": """
{{plain:Starting dialysis is like a family moving from a small house with a slow leak to a bigger house with a cleaning crew that comes three times a week. The crew clears waste well, but every visit also carries away some of the family&rsquo;s food: amino acids, vitamins, and glucose leave with the waste. The diet that suited the small, leaky house now leaves the family short. The comparison has one gap: the &ldquo;crew&rdquo; also stirs up inflammation, which raises protein needs further.}}
{{cards:Key terms for this module|Hemodialysis (HD)::Blood is pumped through a filter outside the body to remove waste and fluid, usually 4 hours, two or three times a week.|Amino acid losses::About 6 to 12 g of amino acids pass into the dialysis fluid in each session.|Oral nutrition supplement (ONS)::A ready-made drink or powder that adds energy and protein.|Intradialytic parenteral nutrition (IDPN)::Amino acids, glucose, and fat given into the dialysis circuit during treatment.|Incremental hemodialysis::Starting with fewer or shorter sessions while the patient still has useful urine output.|Interdialytic interval::The time between sessions; the long gap is the weekend in a thrice-weekly schedule.}}
{{flow:Stepwise nutrition support on HD|Counsel::Find the cause and fix the plan.|Fortify food::Add protein and energy to meals the patient already eats.|Oral supplement::A product chosen with the patient, with a trial period.|Tube feeding::If oral intake still falls short and the gut works.|IDPN or full parenteral nutrition::Selected patients, with the team.}}
""",
    "case": {"title": "Still on the old diet", "html": """
<p>Mr. Tan, 63, started HD five weeks ago. Before dialysis he followed a 48 g/day protein plan, 0.8 g/kg at his 60 kg weight, and he is proud of how well he has kept to it. He dialyzes Monday, Wednesday, and Friday at 6 a.m.</p>
<p>He leaves home at 4:30 a.m. without breakfast, because &ldquo;eating before dialysis makes me dizzy.&rdquo; After the session he is tired and eats little until dinner. His post-dialysis weight has fallen from 60.0 to 58.5 kg. He is otherwise well.</p>
""", "questions": ["What is his protein target now, and how far is he below it?",
                  "Why is his dialysis day his worst day for nutrition?",
                  "What two changes would you try first, and how would you know they worked?"]},
    "sections": [
        ("needs", "Why needs rise", "The day dialysis starts, the diet must change", """
<p>Before dialysis, protein was kept moderate to slow kidney damage and limit waste. Once dialysis starts, that reason is gone, and three new losses appear. Each session removes about 6 to 12 g of amino acids. Contact between blood and the dialysis circuit stirs low-grade inflammation, which speeds muscle breakdown. And on dialysis days many patients simply eat less.[[ikizler2013]]</p>
<p>KDOQI advises 1.0 to 1.2 g/kg/day of protein for metabolically stable adults on HD or peritoneal dialysis, with or without diabetes (expert opinion), and the same energy range as in CKD, 25 to 35 kcal/kg/day (a firm recommendation, grade 1C).[[kdoqi2020]] For a 60 kg patient, that is 60 to 72 g of protein a day, compared with 48 g before.</p>
{{key:Every patient starting dialysis needs a new nutrition prescription in the first weeks. A pre-dialysis protein restriction that nobody lifts is one of the most common causes of wasting in the first year.}}
<p>Phosphorus rises with protein, which is why many patients and some staff resist raising it. Module 7 showed how to add protein while keeping phosphorus down: fresh sources, egg whites, no additives, and binders taken with meals. Potassium and fluid advice now depend on urine output, the dialysis schedule, and the monthly results, not on the old list.</p>
"""),
        ("week", "The dialysis week", "Look at the whole week, not one day", """
<p>Ask for two recalls: one dialysis day and one non-dialysis day. They often look like two different patients. On dialysis days, early transport, the session itself, and tiredness afterward can wipe out one or two meals. In the Philippines, many patients dialyze twice a week, so the gap is three or four days, and potassium, phosphorus, and fluid build up for longer.</p>
{{cards:Common barriers on dialysis days|Early shifts::No breakfast before a 5 or 6 a.m. start.|Dizziness::Eating just before a session can drop blood pressure in some patients.|Tiredness after::&ldquo;Washed out&rdquo; for hours; meals are skipped until evening.|Cost and travel::Fare, food, and lost work pay on the same day.|Unit rules::Some units do not allow food during treatment.}}
<p>Then look at the data the unit already has. The normalized protein catabolic rate (nPCR), calculated from urea before and after dialysis, estimates protein intake in stable patients. An nPCR below about 1.0 g/kg/day supports your concern; a normal nPCR in a patient who is losing weight does not cancel it. Compare serial post-dialysis weights at the same point in the week, and ask the nurse whether sessions are being shortened or missed.[[kdoqi2020]]</p>
{{fig:rd09_week}}
"""),
        ("eating", "Eating during treatment", "Food in the chair: benefits and cautions", """
<p>Eating during HD is common in Asia and less common in some Western units. An international expert consensus from the International Society of Renal Nutrition and Metabolism (ISRNM) concluded that meals, snacks, or oral supplements during treatment can improve nutrition and that the possible problems can usually be managed.[[kistler2018]] The problems are real: blood pressure can fall after eating, especially in patients prone to low pressure; there is a risk of choking in drowsy patients; and hygiene and staff time need planning.</p>
<p>The strongest data come from a large quality-improvement program in the United States. Patients with albumin at or below 3.5 g/dL who received a supervised oral supplement during dialysis were compared with matched patients who did not. In the analysis that kept everyone in their starting group, deaths were slightly lower with supplements (adjusted hazard ratio 0.91); among those who stayed on the program, the difference was larger (hazard ratio 0.66).[[lacson2012]] This was not a randomized trial. Patients who keep taking a supplement are often healthier in other ways, so it shows an association and does not prove that the supplement prevented deaths. It does support offering one.</p>
{{cards:Making it safe|Timing::Early in the session, not in the last hour when pressure is lowest.|Who::Not patients with frequent low pressure, poor swallowing, or drowsiness, unless the nurse agrees.|What::Small, low-potassium, low-phosphorus items, or a renal supplement.|Unit policy::Follow it, and help change it with the nephrologist if evidence supports a change.}}
"""),
        ("support", "Stepping up", "Supplements, IDPN, and other schedules", """
<p><strong>Oral supplements.</strong> When counseling and fortified food do not close the gap, KDOQI suggests a trial of oral supplements for at least three months in patients with or at risk of protein-energy wasting (a weak suggestion).[[kdoqi2020]] Choose a product the patient will drink: check energy and protein per serving, potassium, phosphorus, and sugar, the price per day, and taste. One serving a day, taken during or right after dialysis, is a reasonable start. Set a review in two to four weeks with intake and weight.</p>
<p><strong>IDPN.</strong> IDPN delivers amino acids, glucose, and fat into the blood during the session. It cannot cover a full day&rsquo;s needs; it adds to oral intake. Two randomized trials frame what it can do. In France, 186 malnourished HD patients all received oral supplements, and half also had IDPN for a year. Two-year survival and hospital admissions did not differ.[[cano2007]] In Germany, IDPN for 16 weeks raised prealbumin more than counseling alone in 83 patients.[[marsen2017]] Prealbumin is a laboratory marker, not survival. So IDPN can improve nutrition markers, and it has not been shown to help patients live longer. KDOQI suggests a trial only when oral and tube feeding cannot meet needs (a weak suggestion).[[kdoqi2020]] Eligibility, the solution, and glucose monitoring belong to the nephrologist and nutrition support team.</p>
<p><strong>Twice-weekly and incremental dialysis.</strong> Some patients start with fewer sessions while they still pass useful urine. Their potassium and fluid allowances depend on that urine. Ask about urine output at every visit, because when it falls, the diet must tighten and the nephrologist may add sessions.</p>
{{stop:Report to the nephrologist the same day: post-dialysis weight falling with poor intake, new difficulty eating or swallowing, vomiting or diarrhea lasting more than a day, or a patient who has stopped eating after a hospital stay.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is his target now?</strong> At 60 kg, 1.0 to 1.2 g/kg/day is 60 to 72 g of protein a day. He is eating about 48 g, so he is 12 to 24 g short, every day, and his weight shows it: 1.5 kg lost in five weeks. Nobody told him the rules had changed. He is being punished for following them well.</p>
<p><strong>Why is his dialysis day the worst?</strong> He leaves at 4:30 a.m. without food, dialyzes on an empty stomach, and is too tired afterward to eat until dinner. On three days a week he eats one real meal. His non-dialysis days may look much better.</p>
<p><strong>What would you try first?</strong> Tell him, clearly and kindly, that his protein should now go up, and why. Then work on the dialysis day. If eating before dialysis makes him dizzy, try a small, easy breakfast he can carry and eat early in the session if the unit allows, such as pandesal with egg, or a small portion of the unit&rsquo;s approved snack. Add a protein-rich snack after the session, before he naps. If those do not close the gap in two weeks, discuss an oral supplement with the team.</p>
<p><strong>How will you know it worked?</strong> Repeat both recalls at two weeks. Track his post-dialysis weight at the same session each week. Check the next nPCR. Tell the nephrologist about the weight loss and the new plan today. The dietitian is often the only person on the team who asks a new patient what he ate on the way to dialysis.</p>
"""],
    "skills": {"title": "Hemodialysis nutrition review",
               "intro": "Use a fictional patient in the first three months of dialysis.",
               "items": [
                   ("Recalculates protein for dialysis (1.0 to 1.2 g/kg/day) and identifies any leftover pre-dialysis restriction.", True),
                   ("Takes a dialysis-day recall and a non-dialysis-day recall.", False),
                   ("Asks about transport, session time, tiredness, and food at the unit.", False),
                   ("Reads nPCR and serial post-dialysis weights and explains their limits.", False),
                   ("Applies the unit&rsquo;s policy on eating during treatment and names patients for whom it is unsafe.", False),
                   ("Chooses an oral supplement by protein, energy, potassium, phosphorus, cost, and taste, and sets a trial period.", False),
                   ("Explains what the IDPN trials showed and did not show.", False),
                   ("Reports weight loss with poor intake to the nephrologist the same day.", True),
               ],
               "placement": "Spend one full HD shift on the floor and record what each patient ate before, during, and after the session."},
    "quiz": [
        ("The KDOQI protein advice for stable adults on HD is:",
         ["0.6 g/kg/day", "0.8 g/kg/day", "1.0 to 1.2 g/kg/day", "2.0 g/kg/day"], 2,
         "1.0 to 1.2 g/kg/day, expert opinion."),
        ("For a stable 60 kg patient on HD, the protein range is:",
         ["33 to 36 g/day", "48 g/day", "60 to 72 g/day", "90 to 100 g/day"], 2,
         "1.0 to 1.2 × 60 = 60 to 72 g/day."),
        ("About how many grams of amino acids are lost in one HD session?",
         ["Less than 1 g", "6 to 12 g", "50 g", "100 g"], 1,
         "About 6 to 12 g pass into the dialysis fluid each session."),
        ("Why is a dialysis day often the worst nutrition day?",
         ["Food is forbidden", "Early travel, the session, and tiredness can remove one or two meals", "Dialysis lowers appetite permanently", "It is not"], 1,
         "Ask for a dialysis-day recall as well as a non-dialysis-day recall."),
        ("A patient started HD six weeks ago and still follows his 0.8 g/kg/day plan. The dietitian should:",
         ["Praise him and continue", "Raise the target to 1.0 to 1.2 g/kg/day and explain why", "Lower it further", "Wait for albumin to fall"], 1,
         "A leftover pre-dialysis restriction is a common cause of early wasting."),
        ("An nPCR is a reliable estimate of protein intake when the patient is:",
         ["Catabolic", "Metabolically stable", "Hospitalized", "Starving"], 1,
         "In unstable patients urea reflects tissue breakdown, not intake."),
        ("A main risk of eating during HD is:",
         ["High phosphorus", "A fall in blood pressure after eating in some patients", "Weight gain", "Low potassium"], 1,
         "Post-meal hypotension is a reason for timing and selection, not a blanket ban."),
        ("When is eating during dialysis safest?",
         ["In the last hour", "Early in the session, in patients without frequent low pressure", "Never", "Only lying flat"], 1,
         "Blood pressure is usually lowest late in the session."),
        ("In the large U.S. supplement program, why does the result not prove the supplement saved lives?",
         ["It was randomized", "It was observational; patients who kept taking it may have been healthier", "It had no deaths", "It used IDPN"], 1,
         "Healthy-adherer effects can explain part of the association."),
        ("In the French IDPN trial, adding IDPN to oral supplements:",
         ["Reduced death", "Did not change two-year survival", "Doubled hospital admissions", "Was not randomized"], 1,
         "Survival and admissions did not differ."),
        ("The German IDPN trial showed improvement in:",
         ["Survival", "Prealbumin, a laboratory marker", "Hospital admissions", "Kidney function"], 1,
         "A marker improved; patient outcomes were not shown."),
        ("KDOQI suggests a trial of oral supplements, when counseling alone fails, for at least:",
         ["One week", "Three months", "One year", "One day"], 1,
         "A minimum three-month trial, a weak suggestion."),
        ("Who decides whether a patient receives IDPN?",
         ["The dietitian alone", "The nephrologist with the nutrition support team", "The patient&rsquo;s family", "The technician"], 1,
         "The dietitian assesses and recommends; the team decides."),
        ("A patient on incremental twice-weekly HD reports much less urine. The diet may need to:",
         ["Loosen", "Tighten for potassium and fluid, with the nephrologist informed", "Stay the same", "Stop protein"], 1,
         "Allowances depended on urine output."),
        ("Which finding should go to the nephrologist the same day?",
         ["A request for recipes", "Falling post-dialysis weight with poor intake", "A question about rice brands", "A stable weight"], 1,
         "Weight loss with poor intake needs prompt team review."),
    ],
    "terms": [("Fortified food", "A usual dish with extra protein or energy added, such as egg in lugaw."),
              ("Prealbumin", "A blood protein that changes faster than albumin; also falls with inflammation."),
              ("Healthy-adherer effect", "People who stick with a treatment tend to be healthier in other ways."),
              ("Urea kinetics", "Calculations from urea before and after dialysis."),
              ("Post-meal hypotension", "A fall in blood pressure after eating.")],
    "readings": [("eating-on-dialysis.html", "Eating on dialysis, for patients."),
                 ("kain-pa-rin.html", "Poor appetite and what helps."),
                 ("starting-dialysis-new-beginning.html", "What changes when dialysis starts.")],
    "calcs": ["calc-hd-adequacy-npcr.html", "calc-npcr.html", "calc-idwg-fluid.html", "calc-dialysis-adequacy-ktv.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
