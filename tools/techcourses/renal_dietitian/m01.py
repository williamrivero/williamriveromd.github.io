# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 01: The Renal Dietitian's Role and the First Consult. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian at a clinic desk on the telephone with a laboratory report in hand, a patient seated beside her.",
    "objectives": [
        "Confirm chronic kidney disease (CKD) from two results at least three months apart, and classify it by cause, glomerular filtration rate category, and albuminuria category.",
        "Sort a nutrition referral into routine, expedited, or urgent, and say what makes it so.",
        "State what a registered nutritionist-dietitian (RND) decides, and what belongs to the physician, nurse, and pharmacist.",
        "Collect the six things every first renal consult needs before any advice is given.",
        "Escalate a critical result with a structured, closed-loop handoff and document who accepted it.",
        "Explain why renal diets are now individualized instead of fixed lists of forbidden foods.",
    ],
    "big": """
{{plain:Think of the kidneys as the household&rsquo;s waste collector and water meter in one. When collection slows, the family does not stop eating; it sorts what it brings home so less waste piles up between pickups. Your job is to help each family sort, using what the kidney can still do today. The picture is useful but incomplete: the kidney also makes hormones and balances acid, which is why diet touches bone, blood, and muscle too.}}
{{cards:Key terms for this module|Chronic kidney disease (CKD)::Abnormal kidney structure or function for at least three months, with implications for health.|Estimated glomerular filtration rate (eGFR)::An estimate, from a blood test, of how much blood the kidneys filter each minute.|Urine albumin-to-creatinine ratio (UACR)::The amount of albumin in a spot urine sample, corrected for how concentrated the urine is.|Medical nutrition therapy (MNT)::Assessment, a nutrition prescription, counseling, and follow-up given by a dietitian for a medical condition.|Nutrition Care Process (NCP)::The four-step method of assessment, diagnosis, intervention, and monitoring that Philippine hospitals are required to document.|Critical result::A laboratory value that the laboratory or unit policy says must be reported to a clinician at once.|Closed-loop handoff::A report in which the receiver repeats the message back and accepts responsibility, and you record that they did.}}
{{flow:Three habits this module teaches|Stage before you advise::Know the cause, the eGFR category, and the albuminuria category, with dates.|Triage before you teach::Decide whether this referral is routine, expedited, or urgent.|Hand off, then document::A warning that nobody accepted has not been delivered.}}
""",
    "case": {"title": "The label-reading referral", "html": """
<p>Mrs. Dela Cruz, 59, is referred for &ldquo;label reading and a low-salt diet.&rdquo; Her record shows an eGFR of 36 mL/min/1.73 m&sup2; in July and 34 in November, with a UACR of 420 mg/g. She takes losartan and, since last month, spironolactone.</p>
<p>You telephone to confirm tomorrow&rsquo;s appointment. She says she has felt weak since yesterday and that her heart is &ldquo;skipping.&rdquo; While you are speaking, the laboratory posts today&rsquo;s potassium and flags it as critical.</p>
""", "questions": ["How would you classify her kidney disease, and what makes it chronic?",
                  "Is this still a routine referral?",
                  "Exactly what will you say, to whom, and what will you write down?"]},
    "sections": [
        ("stage", "Staging", "Read the kidney history before the diet history", """
<p>A nutrition prescription depends on how much kidney function is left and how fast it is changing, so the first task is to stage the disease. Chronic kidney disease (CKD) is defined as abnormal kidney structure or function, present for at least three months, with implications for health.[[kdigo_ckd2024]] One low result is not CKD. Dehydration, an infection, or a new medicine can lower the estimated glomerular filtration rate (eGFR) for a few days.</p>
<p>KDIGO classifies CKD by <strong>C</strong>ause, <strong>G</strong>FR category, and <strong>A</strong>lbuminuria category, the &ldquo;CGA&rdquo; system.[[kdigo_ckd2024]] The two numbers answer different questions. The eGFR says how much filtering is left. The urine albumin-to-creatinine ratio (UACR) says how leaky the filter is, and it predicts progression and heart disease at every level of eGFR.</p>
<div class="table-wrap"><table>
<thead><tr><th>GFR category</th><th>eGFR (mL/min/1.73 m&sup2;)</th><th>Albuminuria category</th><th>UACR (mg/g)</th></tr></thead>
<tbody>
<tr><td>G1</td><td>90 or higher</td><td>A1</td><td>Below 30</td></tr>
<tr><td>G2</td><td>60 to 89</td><td>A2</td><td>30 to 300</td></tr>
<tr><td>G3a</td><td>45 to 59</td><td>A3</td><td>Above 300</td></tr>
<tr><td>G3b</td><td>30 to 44</td><td></td><td></td></tr>
<tr><td>G4</td><td>15 to 29</td><td></td><td></td></tr>
<tr><td>G5</td><td>Below 15</td><td></td><td></td></tr>
</tbody></table></div>
<p>G1 and G2 count as CKD only when there is another marker of kidney damage, such as albuminuria or an abnormal ultrasound.[[kdigo_ckd2024]] Two cautions matter to a dietitian. First, eGFR from creatinine depends on muscle: a frail patient with little muscle can have a reassuring eGFR and poor kidney function, and a high cooked-meat meal or a creatine supplement can lower it for a day. Second, when kidney function is changing quickly, as in acute illness, eGFR formulas are unreliable and should not be used to stage.</p>
{{fig:rd01_cga}}
{{key:Write the stage the way the nephrologist does: cause, G category, A category, and the dates of the two results that prove it is chronic. &ldquo;Diabetic kidney disease, G3b A3, eGFR 36 in July and 34 in November.&rdquo;}}
"""),
        ("triage", "Triage", "Sort the referral: routine, expedited, or urgent", """
<p>A referral slip tells you what the sender was thinking on the day it was written. The patient may have changed since. Before you plan a teaching session, collect six things: the referral question, the kidney stage or dialysis modality, recent hospital stays, the trend in weight and intake, the latest potassium, bicarbonate, phosphorus, and glucose with their dates, and the current medicine list including supplements and herbal products.</p>
{{cards:Three levels of referral|Routine::Stable patient, steady intake and weight, no safety signal. Example: a first visit for G3a CKD with normal potassium. See at the next scheduled clinic.|Expedited (days)::Intake has fallen clearly, weight is dropping without intention, a new dialysis start, a new tube feeding, or discharge after a long admission. See within the week and tell the referring clinician.|Urgent (now)::A critical laboratory result, new weakness, palpitations, confusion, breathlessness at rest, a low glucose that is not responding, cloudy peritoneal dialysis fluid, or a missed dialysis session with symptoms. Stop teaching and activate the unit&rsquo;s urgent pathway.}}
<p>The Academy of Nutrition and Dietetics and National Kidney Foundation standards describe this sorting as part of competent nephrology practice: the dietitian screens, sets priorities, and communicates concerns to the team.[[pace2021]] The reason is physiological. A patient with G4 CKD who starts a potassium-sparing medicine can go from a normal to a dangerous potassium within weeks, and the first person to hear about the weakness is often the one who telephones about the diet.</p>
{{stop:A critical result with symptoms is a medical emergency, not a nutrition problem. Do not start diet teaching, do not ask the patient to &ldquo;avoid bananas and come tomorrow,&rdquo; and do not wait for the clinic day. Call the responsible physician or follow the emergency pathway now.}}
"""),
        ("scope", "Your role", "What is yours to decide", """
<p>In the Philippines, the practice of nutrition and dietetics is regulated by Republic Act No. 10862, and hospitals are required by the Department of Health to document nutrition care using the Nutrition Care Process (NCP): assessment, diagnosis, intervention, and monitoring and evaluation.[[ra10862]][[doh_ncp2019]] Within that process the dietitian owns the nutrition assessment, the nutrition diagnosis, the nutrition prescription within the diet order, counseling, and follow-up.</p>
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Who decides</th><th>The dietitian&rsquo;s part</th></tr></thead>
<tbody>
<tr><td>Energy and protein targets, meal plan, food choices</td><td>Dietitian, within the physician&rsquo;s diet order</td><td>Calculate, document the guideline and weight used, counsel, review</td></tr>
<tr><td>Phosphate binder, potassium binder, insulin, diuretic, vitamin D doses</td><td>Physician</td><td>Report intake, timing problems, and adherence barriers; reinforce the written instructions</td></tr>
<tr><td>Dry weight, dialysis time, dialysis fluid</td><td>Nephrologist</td><td>Report weight history, intake, and fluid sources</td></tr>
<tr><td>Oral nutrition supplement</td><td>Facility policy; often dietitian recommends, physician orders</td><td>Select the product and amount, monitor response</td></tr>
<tr><td>Tube feeding or parenteral nutrition</td><td>Physician with the nutrition support team</td><td>Assess, recommend formula and rate, monitor delivery and tolerance</td></tr>
<tr><td>Emergency treatment</td><td>Physician and nurse</td><td>Recognize, call, hand off, document</td></tr>
</tbody></table></div>
<p>The line between &ldquo;reinforcing&rdquo; and &ldquo;changing&rdquo; a medicine is where new dietitians slip. Telling a patient to take the binder with the first bite of a meal, when that is what the label says, is reinforcement. Telling her to take two instead of one because the meal is large is a dose change, and it belongs to the prescriber.</p>
<p>Old renal diets were built as lists of forbidden foods. Two findings changed that. Restriction often lowered total intake and muscle mass, and many high laboratory values turned out to have causes other than food. The KDOQI 2020 guideline therefore recommends adjusting potassium and phosphorus intake to keep serum levels in the normal range for that patient, not restricting everyone.[[kdoqi2020]] Individualizing is harder than handing out a list. It is the reason a trained dietitian is on the team.</p>
"""),
        ("handoff", "Handoff", "Escalate with a closed loop", """
<p>A handoff is closed when three things have happened: you gave the facts, the receiver repeated them back, and the receiver accepted responsibility. Use a fixed structure so nothing is left out under pressure. Many units use Situation, Background, Assessment, Recommendation (SBAR).</p>
{{flow:A 20-second critical-result handoff|Situation::&ldquo;I am the dietitian. Mrs. Dela Cruz, 59, has a potassium flagged critical today and new palpitations and weakness.&rdquo;|Background::&ldquo;CKD G3b A3. On losartan; spironolactone was added last month.&rdquo;|Assessment::&ldquo;I am concerned this is symptomatic hyperkalemia. I have not given diet advice.&rdquo;|Recommendation::&ldquo;Please take over urgent evaluation now. Where should she go, and who will call her?&rdquo;|Read-back::The receiver repeats the name, the result, and the plan. You record the time and the name.}}
{{fig:rd01_handoff}}
<p>Then document: the value and its units, the time it was posted, the symptoms in the patient&rsquo;s words, whom you called and when, what they directed, and that they accepted. If you cannot reach the first person within the time your policy allows, go to the next name on the escalation list. Resume nutrition education only after the team says the patient is stable.</p>
{{key:Your handoff does not need a diagnosis. It needs the result, the symptoms, the medicines that changed, and a clear request.}}
"""),
    ],
    "debrief": ["""
<p><strong>How would you classify her kidney disease?</strong> As CKD G3b A3. An eGFR of 34 falls in G3b, and a UACR of 420 mg/g is above 300, so A3. Two results below 60, four months apart, make it chronic. Write the cause as &ldquo;to be confirmed with the nephrologist&rdquo; until someone has confirmed it.</p>
<p><strong>Is this still a routine referral?</strong> No. It was routine when it was written. A critical potassium with palpitations and weakness makes it urgent today. Notice the medicine list: spironolactone added to losartan in G3b CKD is a well-known cause of a rising potassium. Food is unlikely to be the main cause, and a diet sheet is not the treatment.</p>
<p><strong>What will you say, and what will you write?</strong> Tell Mrs. Dela Cruz not to wait for tomorrow, and follow your unit&rsquo;s pathway to get her seen now. Then call the responsible physician with the handoff in this module: the result, her symptoms, the medicine that changed, and a clear request. Ask for a read-back. Write down the value, the time it was posted, her symptoms in her own words, whom you called and when, what they told you, and that they accepted.</p>
<p><strong>And the label reading?</strong> It can wait until she is safe. When you do see her, the potassium history will shape what you teach. A dietitian is often the first person to hear a patient say &ldquo;I feel weak.&rdquo; Part of your job is to make sure that sentence reaches a physician the same hour.</p>
"""],
    "skills": {"title": "First-consult triage and critical-result handoff",
               "intro": "Use a fictional record. The preceptor plays the patient and then the physician on the telephone.",
               "items": [
                   ("Finds two kidney results at least three months apart and states the cause, G category, and A category with dates and units.", False),
                   ("Collects the six first-consult items: referral question, stage or modality, recent admissions, weight and intake trend, key laboratory results with dates, and medicines including supplements.", False),
                   ("Classifies the referral as routine, expedited, or urgent and gives the reason.", False),
                   ("On a simulated critical result with symptoms, stops teaching and activates the urgent pathway without giving diet advice first.", True),
                   ("Delivers a structured handoff in under 30 seconds and obtains a read-back.", True),
                   ("Documents value, units, time, symptoms, recipient, directions, and acceptance.", True),
                   ("States one decision that belongs to the physician and how the dietitian contributes to it.", False),
                   ("Uses the escalation list when the first contact does not answer.", False),
               ],
               "placement": "During your first week, find your unit&rsquo;s critical-result policy and escalation list, and write the names and numbers on a card you carry."},
    "quiz": [
        ("An eGFR of 34 mL/min/1.73 m² with a UACR of 420 mg/g, both confirmed over four months, is classified as:",
         ["G3a A2", "G3b A3", "G4 A3", "G3b A2"], 1,
         "An eGFR of 30 to 44 is G3b, and a UACR above 300 mg/g is A3."),
        ("What establishes that kidney disease is chronic?",
         ["A referral slip that says CKD", "One eGFR below 60", "Abnormal results present for at least three months", "A UACR above 30 mg/g on one occasion"], 2,
         "Chronicity requires abnormality of structure or function for at least three months. One result may reflect a temporary problem."),
        ("A patient has an eGFR of 75 and a normal urine test and ultrasound. Does she have CKD?",
         ["Yes, G2", "No; G1 and G2 need another marker of kidney damage", "Yes, because any eGFR below 90 is CKD", "It cannot be known without a biopsy"], 1,
         "G1 and G2 are CKD only when a marker of kidney damage, such as albuminuria, is also present."),
        ("Why can a frail, thin patient have a misleadingly good creatinine-based eGFR?",
         ["Creatinine comes from muscle, and low muscle mass lowers serum creatinine", "Frail patients drink more water", "eGFR formulas ignore age", "Albumin interferes with the test"], 0,
         "Creatinine is produced by muscle. With little muscle, serum creatinine is low and the formula overestimates kidney function."),
        ("During a call, a patient reports new palpitations, and the laboratory flags her potassium as critical. What is the first action?",
         ["Teach a low-potassium diet by telephone", "Ask for a three-day food record", "Schedule her for tomorrow&rsquo;s clinic", "Activate the urgent pathway and call the responsible physician"], 3,
         "A critical result with symptoms needs immediate medical assessment. Diet teaching comes after stabilization."),
        ("Which referral should be seen within days, not at the next routine clinic?",
         ["Stable G3a CKD, first visit", "A patient who started hemodialysis last week and is eating half his usual intake", "A request for a recipe booklet", "A stable transplant recipient five years after surgery"], 1,
         "A new dialysis start with falling intake is a high-risk transition and should be expedited."),
        ("A patient asks whether she can take two phosphate binder tablets with a large meal. The prescription says one. The dietitian should:",
         ["Agree, because the meal is large", "Tell her to skip the binder", "Reinforce the prescribed dose and ask the prescriber about adjusting it", "Tell her binders are optional"], 2,
         "Changing a dose belongs to the prescriber. The dietitian reports the question and reinforces the written instruction."),
        ("In SBAR, where does &ldquo;spironolactone was added last month&rdquo; belong?",
         ["Situation", "Background", "Assessment", "Recommendation"], 1,
         "Background holds the relevant history, including recent medicine changes."),
        ("A handoff is &ldquo;closed&rdquo; when:",
         ["You have left a voicemail", "You have written a chart note", "The receiver has repeated the message and accepted responsibility", "The patient has been told to come in"], 2,
         "Closing the loop means read-back and acceptance. A message nobody acknowledged has not been delivered."),
        ("Which document requires Philippine hospitals to record nutrition care as assessment, diagnosis, intervention, and monitoring?",
         ["The KDIGO 2024 guideline", "Department of Health Administrative Order No. 2019-0033", "The Food Exchange Lists", "The PhilHealth benefit circular"], 1,
         "The Department of Health order sets out the Nutrition Care Process in hospitals."),
        ("Why did guidelines move away from fixed lists of forbidden foods?",
         ["Lists were too short", "Blanket restriction lowered intake, and many abnormal results had causes other than food", "Patients preferred longer lists", "Laboratories stopped measuring potassium"], 1,
         "Restriction for everyone risks wasting, and non-diet causes are common. KDOQI 2020 recommends adjusting intake to the individual&rsquo;s serum levels."),
        ("Which item is NOT one of the six things to collect before a first consult?",
         ["Current medicines and supplements", "Trend in weight and intake", "The patient&rsquo;s favorite restaurant", "Recent laboratory results with dates"], 2,
         "The six are the referral question, stage or modality, recent admissions, weight and intake trend, key results with dates, and medicines."),
        ("The UACR mainly tells you:",
         ["How much filtering capacity is left", "How leaky the kidney filter is", "How much protein the patient eats", "Whether the patient is dehydrated"], 1,
         "Albuminuria reflects damage to the filtering barrier and predicts progression and cardiovascular risk."),
        ("You cannot reach the attending physician about a critical result. What next?",
         ["Wait an hour and try again", "Send an email", "Call the next person on the unit&rsquo;s escalation list", "Advise the patient yourself"], 2,
         "The escalation list exists for this. Move to the next contact within the time your policy sets."),
        ("After an urgent handoff, what should the note contain?",
         ["Only the diet plan", "Value and units, time, symptoms, recipient, directions, and acceptance", "The dietitian&rsquo;s opinion of the medicine", "Nothing until the patient returns"], 1,
         "The record must let another clinician see what was found, who was told, and who took responsibility."),
    ],
    "terms": [("CGA classification", "Cause, GFR category, and albuminuria category: the KDIGO way of describing CKD."),
              ("Albuminuria", "Albumin in the urine; a sign that the kidney&rsquo;s filter is damaged."),
              ("Nutrition Care Process", "Assessment, nutrition diagnosis, intervention, and monitoring and evaluation."),
              ("SBAR", "Situation, Background, Assessment, Recommendation: a structure for clinical reports."),
              ("Read-back", "The receiver repeats the message so both sides know it was understood."),
              ("Escalation list", "The order of people to call when the first person cannot be reached."),
              ("Scope of practice", "What a profession is licensed and trained to do.")],
    "readings": [("nutrition-kidney-patients.html", "The patient-facing overview you will often hand out after a first visit."),
                 ("potassium-hyperkalemia-ckd.html", "Why potassium rises in kidney disease, including medicine causes."),
                 ("proteins-proteinuria.html", "What albuminuria means, in plain language.")],
    "calcs": ["calc-egfr-ckd-epi.html", "calc-proteinuria-uacr.html", "calc-kfre.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
