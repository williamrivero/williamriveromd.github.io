# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 10: Longitudinal care, nutrition and safe transitions.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Run a structured routine follow-up that covers therapy, access, nutrition, metabolic issues, mental health, supplies and the person&rsquo;s goals.",
        "Explain the nutritional and metabolic consequences of peritoneal dialysis (PD) (protein loss, glucose absorption, low potassium) and the 2026 International Society of Renal Nutrition and Metabolism (ISRNM) and International Society for Peritoneal Dialysis (ISPD) nutrition recommendations at a nursing level.",
        "Prevent the icodextrin and glucose meter error that can hide hypoglycemia.",
        "Hand over a PD patient safely between home, ward, emergency department and other facilities.",
        "Coordinate transplant referral, modality change and supportive care as planned transitions rather than crises.",
    ],
    "big": """
<p>The first three months of PD are about training and starting. The years after are about keeping the person well, nourished and on therapy, and keeping them safe whenever they cross a boundary: admitted to a ward where nobody knows PD, moved to another city, switched to hemodialysis, listed for a transplant.</p>
<p>Nearly half of people who start PD are no longer on it at two years, according to the 2026 ISPD position statement on loss from PD therapy.[[pd_quinn2026]] Some of those exits are the right outcome, such as transplantation. Some are avoidable. Your work is to make every exit a planned one, and to make every handover complete.</p>
{{plain:Think of PD care as a relay race run over years. Each handover of the baton, clinic to home, home to ward, ward back home, is where races are lost.}}
<p>The picture has a limit. In a relay, every runner knows the baton. In a general ward, the receiving team may never have seen a PD catheter, may not know the order, and may stop or change therapy without telling the PD unit. You may need to hand over the baton and teach how to hold it.</p>
{{cards:Key terms for this module|Protein-energy wasting::Loss of body protein and energy stores, common in kidney failure.|Icodextrin interference::A false glucose reading on some meters in patients using icodextrin.|Handoff::The structured transfer of information and responsibility between teams.|Planned exit::Leaving PD by a prepared route, such as transplant or a planned move to hemodialysis.|Medication reconciliation::Comparing every medicine list to find and resolve differences.}}
""",
    "case": {"title": "A normal sugar that was not", "html": """
<p><strong>Mrs. Teresita Uy, 66</strong>, a retired bookkeeper with diabetes, has been on CAPD for three years with an icodextrin night dwell. She is admitted to the medical ward of a general hospital in Quezon City for peritonitis. Nurse <strong>Grace</strong> from the PD unit visits on day 1.</p>
<p>The ward&rsquo;s glucose meter reads 180 mg/dL, and insulin by sliding scale is due. Mrs. Uy says she feels shaky and sweaty. On day 6, her discharge orders list four exchanges of 1.5% dextrose. Her home record shows three 1.5% exchanges plus icodextrin overnight.</p>
""", "questions": ["What is wrong with the glucose reading on the ward?",
                  "What do you do about the conflicting discharge orders?",
                  "What follow-up must be arranged before she leaves?"]},
    "sections": [
        ("routine-follow-up", "Routine follow-up", "Routine follow-up", """
<p>At each scheduled review, cover every domain, in the same order, every time. The domain you skip is the one where the problem was hiding.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>Questions and checks</th></tr></thead>
<tbody>
<tr><td>Goals</td><td>What matters now? Any change in work, family or plans?</td></tr>
<tr><td>Therapy</td><td>Records versus order; missed exchanges or cycler sessions; supply problems</td></tr>
<tr><td>Fluid</td><td>Weight, blood pressure, edema, breathlessness, ultrafiltration (UF), urine trend</td></tr>
<tr><td>Access</td><td>Exit site, tunnel, catheter integrity, drain performance</td></tr>
<tr><td>Nutrition</td><td>Appetite, unintended weight change, intake, protein sources, diet barriers</td></tr>
<tr><td>Bowel</td><td>Constipation, which affects catheter function and enteric peritonitis risk</td></tr>
<tr><td>Metabolic</td><td>Potassium, glucose control in diabetes, results due</td></tr>
<tr><td>Medicines</td><td>Reconciliation; new prescriptions from other doctors</td></tr>
<tr><td>Mental health and sleep</td><td>Mood, anxiety, burnout, sleep, caregiver strain</td></tr>
<tr><td>Supplies and finances</td><td>Delivery reliability, storage, benefit status</td></tr>
<tr><td>Plans</td><td>Transplant work-up, advance care planning, next tests</td></tr>
</tbody></table></div>
<p>Document responsibilities and dates across disciplines.</p>
<h3>Example: the domain that mattered</h3>
<p>Mr. Jaime&rsquo;s numbers are fine: weight steady, UF good, exit site clean. When Nurse Grace reaches mental health, he goes quiet. His wife, who helps with his exchanges, has started night shifts to pay for his medicines. He has been skipping his midday exchange so she can sleep, and he feels like a burden. He did not mention it because &ldquo;the numbers were good.&rdquo;</p>
<p>Grace records the skipped exchanges, refers him to the social worker about benefits and medicine costs, and tells the nephrologist about the missed therapy and his mood. The numbers would have changed in a month. The conversation changed them today.</p>
{{key:Cover every domain at every review. Good numbers can sit on top of a household under strain.}}
"""),
        ("nutrition-and-metabolism", "Nutrition", "Nutrition and metabolism", """
<h3>Protein and albumin loss</h3>
<p>PD loses protein into the effluent every day through the large pores (Module 1), and more during peritonitis. Inflammation, poor appetite from glucose absorption, and abdominal fullness add to the risk of protein-energy wasting.</p>
<h3>Glucose exposure</h3>
<p>Glucose in the solution is absorbed. It supplies calories, which can help an underweight person and harm someone with obesity, diabetes or high blood lipids. Stronger exchanges carry more glucose. The site&rsquo;s glucose absorption calculator shows the order of magnitude for a given prescription.</p>
<div class="table-wrap"><table>
<thead><tr><th>Patient</th><th>What absorbed glucose means for them</th><th>What you watch and report</th></tr></thead>
<tbody>
<tr><td>Lola Ising, 79, 41 kg, poor appetite</td><td>Extra calories may help, but fullness may blunt her appetite further</td><td>Weight, meals actually eaten, early satiety; refer to the dietitian</td></tr>
<tr><td>Mr. Ben, 54, diabetes, weight rising</td><td>Extra calories and glucose worsen weight and glucose control</td><td>Glucose trend, weight, how often stronger bags are used; report to the team</td></tr>
</tbody></table></div>
<h3>Potassium</h3>
<p>Because PD removes potassium continuously and many patients eat little, low potassium is common, unlike in hemodialysis. The 2022 ISPD peritonitis recommendations name low potassium as a modifiable peritonitis risk factor.[[pd_li2022]] Patients often carry hemodialysis-era advice to avoid fruit. Check what they are actually eating, and route potassium decisions to the team and the renal dietitian.</p>
<p>Consider Mrs. Nenita, who transferred from hemodialysis to PD a year ago. She still refuses bananas, mangoes and vegetables, as she was taught in the hemodialysis unit. Her potassium is low and she is constipated. You report the result and her intake to the team and dietitian. You do not tell her to &ldquo;eat bananas freely,&rdquo; and you do not leave the old rule standing.</p>
<h3>The 2026 joint ISRNM and ISPD practice recommendation</h3>
<p>This is the first international nutrition guidance specific to PD. It used the GRADE framework for graded recommendations and expert-consensus practice points. It covers five themes: nutrition screening, assessment and monitoring; dietary recommendations; nutrition interventions for complications; supplementation; and education to build health, nutrition and food literacy.[[pd_wang2026]] Nurses contribute screening, monitoring and reinforcement of the dietitian&rsquo;s plan.</p>
{{key:Advice that was right on hemodialysis can be wrong on PD. Ask what the patient is actually eating, and why.}}
{{fig:pd10_fig_10_glucose_absorption_low_potassium}}
"""),
        ("the-icodextrin-glucose", "Icodextrin and glucose meters", "The icodextrin and glucose meter hazard", """
<p>Icodextrin is broken down to maltose and other short sugars that circulate in the blood. Some point-of-care glucose meters and test strips cannot tell maltose from glucose, and report falsely high glucose.</p>
<p>The real danger is a falsely normal reading when the patient is actually hypoglycemic, or insulin given for a falsely high reading. A patient who is shaky and sweaty with a &ldquo;normal&rdquo; meter reading is the classic warning.</p>
{{fig:pd10_ico}}
<p><strong>Every patient on icodextrin, and every ward they are admitted to, must use a glucose method that is compatible according to product labeling and facility policy.</strong> Put &ldquo;on icodextrin&rdquo; on the handoff, the medication list and the bedside.</p>
<h3>Example: where the error enters</h3>
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>How the error happens</th><th>Prevention</th></tr></thead>
<tbody>
<tr><td>Emergency department</td><td>Triage meter used before anyone knows the patient is on icodextrin</td><td>Patient carries a card: &ldquo;I use icodextrin. Check meter compatibility.&rdquo;</td></tr>
<tr><td>General ward</td><td>Ward meter not labeled compatible; sliding-scale insulin ordered</td><td>PD unit alerts the ward; laboratory glucose or compatible method ordered</td></tr>
<tr><td>Home</td><td>Patient buys a new meter at a pharmacy</td><td>Teach the patient to check compatibility before switching meters</td></tr>
</tbody></table></div>
{{call:If a patient on icodextrin has symptoms of low blood sugar with a normal or high meter reading, treat it as possible hypoglycemia under the ward protocol and alert the physician at once. Obtain a laboratory or compatible glucose.}}
"""),
        ("hospital-and-home", "Transitions", "Hospital and home transitions", """
<p><strong>Admission to a non-PD ward.</strong> Call or send to the receiving team:</p>
{{fig:pd10_relay}}
<ul>
<li>The current PD order (modality, solutions, volumes, dwell or cycler program), actual delivery over the last days, and the next planned treatment</li>
<li>Who will perform the next exchange, and how; whether the PD unit will send staff or supplies</li>
<li>Catheter, exit-site and tunnel status; last dressing</li>
<li>Infection history, recent cultures and sensitivities, allergies</li>
<li>Icodextrin use and glucose-meter compatibility</li>
<li>Fluid targets, weight, urine output, potassium</li>
<li>Outstanding issues and the PD unit&rsquo;s contact number</li>
</ul>
<h3>Example: a ward handoff call</h3>
<p>&ldquo;This is Nurse Grace from the PD unit about Mrs. Uy in bed 12. She is on CAPD: three 1.5% exchanges by day and icodextrin overnight. Her last exchange was at 2 PM. Our PD nurse will come at 6 PM for the next one and bring supplies; please do not connect anything to the catheter before then. She is on icodextrin, so please use laboratory glucose or a compatible meter. Effluent culture sent this morning; I will follow it. Our number is on the front of her chart.&rdquo;</p>
<h3>Discharge home</h3>
<p>Compare the discharge orders with the pre-admission home record. Identify pending cultures and who will review them. Check supplies, technique (retrain after peritonitis or a long admission), transport and the follow-up date. Resolve conflicting instructions through the treating team before the patient relies on them.</p>
<h3>Transfer to another unit or city</h3>
<p>Send the order, records, recent labs and a named contact. Confirm the receiving unit uses the same system, or arrange device-specific training.</p>
<p>For example, Mr. Rey is moving home to Iloilo to be near his children. Two weeks before he leaves, Nurse Grace calls the receiving PD unit, sends his order and recent labs, learns that they use a different cycler model, and arranges a training session there in his first week. She gives Mr. Rey a printed summary and the name of the nurse expecting him.</p>
{{key:Every transition is a medicine-safety and glucose-safety moment. Name who does the next exchange.}}
"""),
        ("planned-exits-from", "Planned exits", "Planned exits from PD", """
<div class="table-wrap"><table>
<thead><tr><th>Exit</th><th>Nursing role</th></tr></thead>
<tbody>
<tr><td>Transplant</td><td>Keep the work-up moving; plan catheter management with the transplant team</td></tr>
<tr><td>Transfer to hemodialysis</td><td>Prepare early when trends suggest PD is failing (falling UF, recurrent peritonitis, burnout); vascular access planning with the team</td></tr>
<tr><td>Recovery of kidney function</td><td>Rare; document and support</td></tr>
<tr><td>Transfer to another program</td><td>Complete handover</td></tr>
<tr><td>Supportive or conservative care</td><td>Advance care planning, symptom focus, family support</td></tr>
<tr><td>Death</td><td>Bereavement support; review for learning</td></tr>
</tbody></table></div>
<p>The 2026 ISPD position statement recommends replacing the vague term &ldquo;technique failure&rdquo; with standardized definitions of each cause of loss, and proposes key performance indicators for benchmarking (Module 12).[[pd_quinn2026]]</p>
<h3>Example: planned versus crash</h3>
<p><strong>Mr. Lando</strong> has had three peritonitis episodes in a year, and his UF is falling. Nurse Grace raises the pattern at the team review. The nephrologist discusses a future move to hemodialysis with him, and a fistula is created while he is still on PD. Four months later, when PD no longer keeps his fluid down, he starts hemodialysis through a mature fistula, as an outpatient.</p>
<p><strong>Mr. Toto</strong> had the same trend but no one raised it. He arrives in the emergency department breathless, and starts hemodialysis through a neck catheter after an admission.</p>
<p>Both left PD. Only one exit was planned.</p>
{{key:Watch the trend that predicts an exit, and raise it early. A planned exit is safer and kinder than a crash.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is wrong with the reading.</strong> Grace checks the ward meter: it is not labeled compatible with icodextrin. Mrs. Uy&rsquo;s shakiness and sweating fit hypoglycemia, and the meter may be reading her maltose as glucose. Grace alerts the ward nurse and the attending physician, who hold the sliding-scale insulin and order a laboratory glucose and a compatible method. Laboratory glucose is 68 mg/dL. The insulin would have pushed it lower.</p>
<p><strong>The conflicting orders.</strong> On day 6, the discharge orders and her home record disagree on the night dwell. Grace does not let Mrs. Uy go home with conflicting instructions. She contacts the treating nephrologist, confirms the intended order, and updates the written order card. She also adds &ldquo;on icodextrin: check meter compatibility&rdquo; to the discharge summary.</p>
<p><strong>Follow-up before she leaves.</strong> Grace lists the pending culture with the reviewer and date, checks supplies at home, and arranges retraining in one week (peritonitis is a retraining trigger) and an exit-site check. She gives Mrs. Uy an icodextrin card for her wallet.</p>
<p><strong>Take-home.</strong> Every transition is a medicine-safety and glucose-safety moment.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete both tasks for a fictional patient discharged after peritonitis.",
               "items": [("Write a hospital handoff and a follow-up call note for a fictional patient discharged after peritonitis.", False),
                         ("Include the owner of the next treatment, icodextrin status, pending results with the reviewer and date, and a backup contact.", False)]},
    "quiz": [
        ("Why can some glucose meters give falsely high readings in patients on icodextrin?",
         ["Icodextrin is broken down to maltose, which some meters read as glucose", "Icodextrin raises true glucose very high", "The meter is always broken", "Icodextrin contains insulin"], 0,
         "Meters that cannot tell maltose from glucose over-read."),
        ("What is the main danger of that interference?",
         ["Overestimated potassium", "Peritonitis", "Missed hypoglycemia, or insulin given for a falsely high reading", "None"], 2,
         "A falsely normal reading can hide true hypoglycemia, and insulin can make it worse."),
        ("Why is low potassium more common in PD than in hemodialysis?",
         ["Icodextrin adds potassium", "PD stops potassium excretion", "It is not more common", "Continuous potassium removal and often poor intake"], 3,
         "PD removes potassium every hour, and many patients eat little or still follow hemodialysis-era restrictions."),
        ("Old and new prescriptions conflict at discharge. What should the nurse do?",
         ["Use the newer one automatically", "Pause the disputed instruction, get clarification from the treating team, then document and communicate the verified order", "Let the patient choose", "Use both"], 1,
         "Never send a patient home with two versions of the order."),
        ("What makes culture follow-up closed-loop?",
         ["Sending the sample", "A named reviewer and timeframe, confirmation of review, and communication of the plan", "Writing &ldquo;pending&rdquo;", "Asking the patient to call the lab"], 1,
         "A result nobody owns is a result nobody acts on."),
        ("The 2026 ISRNM and ISPD nutrition recommendations are notable because they:",
         ["Ban all protein", "Apply only to children", "Are regulations", "Are the first international PD-specific nutrition practice recommendations, using GRADE and practice points"], 3,
         "They mix graded recommendations with expert-consensus practice points."),
        ("Which item must be in a ward handoff for a PD patient?",
         ["The current PD order, delivery, next treatment and who will do it", "The patient&rsquo;s favorite color", "Only the room number", "Nothing; the ward will figure it out"], 0,
         "The receiving team may never have handled PD. Tell them who does the next exchange."),
        ("Why is protein-energy wasting a concern in PD?",
         ["PD adds protein", "It is not a concern", "Daily effluent protein loss, inflammation and appetite suppression from glucose and abdominal fullness", "Only in hemodialysis"], 2,
         "Several mechanisms push in the same direction."),
        ("Mrs. Nenita avoids all fruit because of hemodialysis-era advice and has low potassium. Best action?",
         ["Tell her to eat bananas freely", "Ignore it", "Report the result and her intake to the team and dietitian for individual advice", "Stop PD"], 2,
         "Potassium decisions belong to the team and dietitian. Do not leave the old rule standing, and do not replace it with your own."),
        ("What does the 2026 ISPD position statement recommend about &ldquo;technique failure&rdquo;?",
         ["Replace it with standardized definitions of each cause of loss from PD, and key performance indicators", "Use it more often", "Report only deaths", "Nothing"], 0,
         "Specific causes point to specific fixes. A vague label hides them."),
        ("After a long admission for peritonitis, what should discharge planning include?",
         ["Only a prescription", "Retraining and technique review, pending results with a reviewer, supplies and a follow-up date", "Nothing", "Hemodialysis transfer, always"], 1,
         "Peritonitis and long admissions are both retraining triggers."),
        ("Mr. Lando and Mr. Toto both leave PD for hemodialysis. Which made Mr. Lando&rsquo;s exit planned?",
         ["Luck", "The falling trend was raised early, so a fistula was created while he was still on PD", "He had no peritonitis", "He refused PD"], 1,
         "Raising the predictive trend early allowed access planning and an outpatient start."),
        ("Why ask about constipation at routine visits?",
         ["It is unrelated", "To prescribe laxatives yourself", "For billing", "It affects catheter drainage and is linked to enteric peritonitis risk"], 3,
         "Report it; bowel management is a team decision."),
        ("Glucose absorbed from PD solution:",
         ["Has no metabolic effect", "Adds calories that may help underweight patients and harm those with obesity, diabetes or high blood lipids", "Lowers blood glucose", "Is always fully drained out"], 1,
         "The same calories mean different things for Lola Ising and for Mr. Ben."),
        ("Mr. Rey is moving to another province. What should you send?",
         ["Only a goodbye message", "Nothing", "His order, records, recent labs and a named contact, and confirm device compatibility or training", "Only the catheter brand"], 2,
         "A different cycler model needs training before he relies on it."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Icodextrin", "A large glucose polymer solution absorbed slowly, used for long dwells."),
              ("Maltose", "A sugar produced when icodextrin is broken down; some glucose meters misread it as glucose."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Tunnel", "The path of the catheter under the skin between the cuffs."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Protein-energy wasting", "Loss of body protein and energy stores, common in kidney failure."),
              ("Medication reconciliation", "Comparing every medicine list to find and resolve differences."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell.")],
    "readings": [("eating-on-dialysis.html", "Diet on dialysis."),
                 ("advance-care-planning-dialysis.html", "Advance care planning in dialysis.")],
    "calcs": ["calc-pd-glucose-absorption.html", "calc-nutrition-screening.html", "calc-potassium-load.html"],
}
