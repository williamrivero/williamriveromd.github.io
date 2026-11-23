# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How acute kidney injury is recognized hours before it becomes obvious, how to sort its causes at the bedside, when to escalate without waiting, and how intermittent, prolonged, and continuous kidney support differ.",
    "desc": "Module 4 of the Nephrology Nursing & Hemodialysis self-study series: acute kidney injury criteria, hemodynamic, intrinsic and obstructive causes, monitoring, urgent escalation for hyperkalemia, and intermittent, prolonged intermittent and continuous kidney support.",
    "keywords": "acute kidney injury nursing, AKI criteria KDIGO, oliguria bladder obstruction, hyperkalemia ECG escalation, SBAR handoff, CRRT versus intermittent hemodialysis, PIRRT",
    "objectives": [
        "Apply the creatinine and urine-output criteria that define acute kidney injury.",
        "Sort likely causes into reduced kidney perfusion, intrinsic kidney damage, and obstruction, using bedside findings.",
        "Monitor a patient at risk and recognize the findings that require urgent escalation.",
        "Deliver a concise clinical handoff for a time-critical problem such as hyperkalemia with electrocardiogram changes.",
        "Compare intermittent, prolonged intermittent, and continuous kidney support.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "Before, inside, or after the filter",
         "html": """
<p>If a household tap slows to a trickle, there are only three places to look: the supply into the house, the filter itself, or a blockage in the outflow pipe. Acute kidney injury (AKI) is sorted the same way. Either too little blood is reaching the kidneys, or the kidney tissue is damaged, or urine cannot drain. The question is worth asking in that order at every bedside, because the first and third are often reversible within hours if someone notices, and the nurse is usually the person positioned to notice.</p>
"""},
        {"id": "physiology", "nav": "Definition and causes", "tag": "Physiology", "h2": "Criteria and the three categories of cause",
         "html": """
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline defines AKI by any one of the following: a rise in serum creatinine of 0.3 mg/dL (26.5 &micro;mol/L) or more within 48 hours; a rise to 1.5 times baseline or more, known or presumed to have occurred within the prior 7 days; or a urine volume below 0.5 mL/kg per hour for 6 hours.[[aki2012]] Severity is staged 1 to 3 by the size of the creatinine rise or the duration of low urine output. The absolute numbers are small on purpose: creatinine lags behind the true fall in filtration, so a change from 0.9 to 1.3 mg/dL can represent a substantial loss of function. A KDIGO update that broadens the framework to acute kidney disease (AKD) and adds biomarkers was released as a public-review draft in 2026; until the final version is published, the 2012 criteria remain the reference.[[aki2012]][[ostermann2020]]</p>
<p><strong>Reduced perfusion</strong> is the most common category in hospitalized patients. Volume loss from vomiting, diarrhea, or bleeding, low cardiac output, and sepsis all reduce the pressure that drives filtration. Medicines can remove the kidney&rsquo;s defenses: a nonsteroidal anti-inflammatory drug (NSAID) narrows the vessel entering the glomerulus, and a renin–angiotensin blocker relaxes the vessel leaving it. <strong>Intrinsic damage</strong> includes acute tubular injury from prolonged poor perfusion, sepsis, or toxins such as aminoglycosides and contrast media, as well as inflammation of the glomeruli or the interstitium. In the Philippines, leptospirosis and severe dengue are important infectious causes. <strong>Obstruction</strong> has to affect both kidneys, a single functioning kidney, or the bladder outlet to cause AKI; an enlarged prostate, a blocked urinary catheter, stones, and pelvic tumors are typical.</p>
"""},
        {"id": "evidence", "nav": "Escalation", "tag": "Evidence", "h2": "What cannot wait",
         "html": """
<p>No medicine has been shown to reverse established AKI. Management is supportive: restore perfusion, stop or adjust harmful medicines, relieve obstruction, and prevent the complications that kill, chiefly hyperkalemia, pulmonary edema, and severe acidosis.[[aki2012]] Kidney support is started for these complications when they do not respond to medical treatment; trials of starting dialysis earlier, before such complications, have not shown a survival benefit.[[ostermann2020]]</p>
<p>Hyperkalemia is the complication with the shortest fuse. Potassium sets the resting electrical state of heart muscle, and a high level can progress from peaked T waves to a widened QRS complex and cardiac arrest with little warning. A KDIGO conference on potassium graded acute hyperkalemia by both the level and the electrocardiogram (ECG): a potassium of 6.5 mmol/L or higher is severe whether or not the ECG has changed, and a level of 6.0 mmol/L or higher with ECG changes is also severe.[[clase2020]] Emergency treatment follows a fixed logic: intravenous calcium to stabilize the heart, insulin with glucose and inhaled beta-agonist to shift potassium into cells, and then removal from the body, by dialysis if the kidneys cannot do it.[[clase2020]] In cardiac arrest from suspected hyperkalemia, standard resuscitation takes priority and the resuscitation guideline assigns these drugs a more limited role.[[aha2025special]] These are prescribed treatments; the nurse&rsquo;s time-critical tasks are recognition, continuous cardiac monitoring, an immediate call, and having the treatments ready.</p>
<p>Structured handoff formats such as Situation, Background, Assessment, Recommendation (SBAR) are associated with improved communication and patient safety in a systematic review, although the evidence is of moderate quality.[[muller2018]] In an emergency their value is practical: the listener hears the problem and the request in the first sentence.</p>
"""},
        {"id": "bedside", "nav": "Monitoring and support", "tag": "Clinical application", "h2": "Monitoring, and the forms of kidney support",
         "html": """
<p>For a patient at risk, record hourly urine output when a catheter is in place, daily weight, strict intake and output, and vital signs with attention to the trend. When urine output falls, check the simple things first: is the catheter kinked or blocked, and is the bladder palpable or distended on a bladder scan? Review the medication chart for agents that harm the kidney or accumulate when it fails, and ask whether doses need adjustment. Report a creatinine rise that meets the criteria even if the patient looks well.</p>
<p>When kidney support is needed, three forms are used. The choice depends mainly on how stable the circulation is and on what the hospital can provide.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Intermittent hemodialysis</th><th>Prolonged intermittent therapy</th><th>Continuous therapy</th></tr></thead>
<tbody>
<tr><td>Typical duration</td><td>3 to 5 hours</td><td>6 to 12 hours</td><td>24 hours a day</td></tr>
<tr><td>Solute and fluid removal</td><td>Fast</td><td>Moderate</td><td>Slow and steady</td></tr>
<tr><td>Best suited to</td><td>Stable circulation; rapid potassium removal</td><td>Borderline circulation; limited continuous-therapy resources</td><td>Unstable circulation, vasopressor support, brain swelling risk</td></tr>
<tr><td>Nursing demands</td><td>Dialysis nurse at bedside for the session</td><td>Dialysis nurse for a longer session</td><td>Hourly fluid balance, circuit and anticoagulation monitoring around the clock</td></tr>
</tbody></table></div>
<p>The slow form is called continuous renal replacement therapy (CRRT), and the middle form is prolonged intermittent renal replacement therapy (PIRRT). Randomized comparisons have not shown that any one form improves survival over the others; the slower forms are chosen because they are better tolerated when blood pressure is fragile.[[aki2012]][[ostermann2020]]</p>
"""},
    ],
    "case": {
        "title": "A catheter, a creatinine, and a potassium",
        "html": """
<p>Mr. Benjamin, 74, is two days post hip surgery in the intensive care unit (ICU). His creatinine was 0.9 mg/dL before surgery and is 1.3 mg/dL this morning, 36 hours later. Urine output through his catheter has been 15 mL per hour for the last four hours, and his lower abdomen is firm and tender. He has received an NSAID for pain since surgery. A repeat blood test returns a potassium of 6.7 mmol/L, and the monitor now shows tall, peaked T waves.</p>
""",
        "acte": {
            "Assess": "Airway, breathing, circulation; 12-lead ECG and continuous monitoring; catheter patency and bladder (palpation or scan); fluid balance; current medicines.",
            "Communicate": "Immediate call using SBAR: potassium 6.7 with peaked T waves, AKI by creatinine criteria, oliguria with a distended bladder, on an NSAID. Request urgent review and hyperkalemia orders.",
            "Teach": "Tell the patient, briefly and calmly, what is happening and why he is being monitored closely.",
            "Escalate": "Do not wait for a repeat sample to call. Widening QRS, slow heart rate, or loss of consciousness: activate the cardiac arrest team.",
        },
        "task": "Write the SBAR you would deliver by phone, in no more than five sentences.",
    },
    "quiz": [
        {"stem": "A patient&rsquo;s serum creatinine rises from 0.9 mg/dL to 1.3 mg/dL over 36 hours. Urine output is not yet available. Does this meet the KDIGO definition of acute kidney injury?",
         "options": [
             ("No; creatinine must at least double", False, "Doubling corresponds to stage 2. The definition is met by smaller changes."),
             ("No; 1.3 mg/dL is within the normal range of many laboratories", False, "AKI is defined by change from baseline, not by the reference range."),
             ("Yes; the creatinine rose by 0.3 mg/dL or more within 48 hours", True, "An increase of 0.4 mg/dL in 36 hours meets the first criterion. Any one criterion is sufficient."),
             ("It cannot be determined without a urine sodium", False, "Urine sodium may help explore the cause but is not part of the definition."),
         ],
         "objective": "Apply the creatinine and urine-output criteria that define acute kidney injury.", "sources": ["aki2012"], "flag": "Based on the KDIGO 2012 criteria; recheck when the 2026 AKI/AKD guideline is finalized."},
        {"stem": "A catheterized postoperative patient has passed 15 mL of urine per hour for four hours. His lower abdomen is firm, tender, and dull to percussion. What should the nurse suspect and do first?",
         "options": [
             ("Dehydration; increase the intravenous fluid rate", False, "Giving more fluid to a patient who cannot drain urine does not help and may cause overload."),
             ("Urinary obstruction; check the catheter for kinks or blockage and assess the bladder", True, "Low output with a distended bladder suggests that urine is being made but cannot drain. A blocked catheter is a reversible cause that the nurse can identify immediately."),
             ("Normal postoperative response; continue routine observation", False, "This output is below 0.5 mL/kg per hour for an adult and the abdominal findings are abnormal."),
             ("Intrinsic kidney damage; prepare for dialysis", False, "Dialysis is not the first step, and obstruction should be excluded before assuming tissue damage."),
         ],
         "objective": "Sort likely causes into reduced kidney perfusion, intrinsic kidney damage, and obstruction, using bedside findings.", "sources": ["aki2012"], "flag": "Catheter flushing or replacement follows local procedure and orders."},
        {"stem": "The same patient&rsquo;s potassium is 6.7 mmol/L and the monitor shows new peaked T waves. Which action is most appropriate?",
         "options": [
             ("Repeat the sample and wait for the result before informing the physician", False, "ECG changes with this level make a false result unlikely, and delay risks cardiac arrest."),
             ("Give the next scheduled dose of his oral potassium-binding medicine and reassess in two hours", False, "Oral binders act slowly and do not protect the heart."),
             ("Document the result for the morning round", False, "This is a medical emergency."),
             ("Escalate urgently with a concise structured handoff, keep the patient on continuous cardiac monitoring, and prepare for prescribed emergency treatment", True, "Hyperkalemia with ECG changes is severe. The nurse&rsquo;s priorities are immediate escalation, monitoring, and readiness to give the treatments ordered."),
         ],
         "objective": "Monitor a patient at risk and recognize the findings that require urgent escalation.", "sources": ["clase2020", "aha2025special", "muller2018"], "flag": "Emergency drug treatment is by physician order or approved hospital protocol."},
    ],
    "reflect": "Recall a time you escalated a deteriorating patient. Did the first sentence of your call state the problem and what you needed? Rewrite it now.",
    "practice": {
        "intro": "With your preceptor in a ward or critical care area, follow one patient with or at risk of AKI through a shift.",
        "items": [
            "Calculates urine output in mL/kg per hour and compares with the AKI criteria.",
            "Checks catheter patency and bladder status when output falls.",
            "Reviews the medication chart for kidney-relevant agents and raises queries appropriately.",
            "Delivers an SBAR handoff for a simulated hyperkalemia scenario within one minute.",
        ],
    },
    "readings": [
        ("acute-kidney-injury-on-ckd.html", "AKI in a patient who already has CKD."),
        ("aki-icu-dialysis-decisions.html", "How decisions about starting kidney support in the ICU are made."),
        ("crrt-continuous-renal-replacement-therapy.html", "Clinician reference for continuous therapy."),
        ("potassium-hyperkalemia-ckd.html", "Hyperkalemia: causes, ECG changes, and treatment."),
        ("tropical-infection-aki.html", "Leptospirosis, dengue, and other tropical causes of AKI."),
    ],
    "calcs": ["calc-aki-staging.html", "calc-urine-output-fluid-balance.html", "calc-crrt-dose.html"],
    "external": [
        ("KDIGO AKI/AKD guideline page (2012 guideline and 2026 draft status)", "https://kdigo.org/guidelines/acute-kidney-injury/"),
    ],
    "terms": [
        ("Oliguria", "Low urine output; in adults, below 0.5 mL/kg per hour."),
        ("Baseline creatinine", "The patient&rsquo;s usual creatinine before the acute illness."),
        ("Peaked T waves", "Tall, narrow T waves on the ECG; an early sign of hyperkalemia."),
    ],
    "image": {
        "file": "renal-nursing-04-aki-escalation",
        "alt": "Hospital nurses assess a patient and make an urgent clinical handoff.",
        "purpose": "Show escalation as a calm, practiced two-person action.",
        "scene": "In an ICU bay, one Filipina nurse in the foreground speaks on a wall-mounted telephone while reading from a clipboard. Behind her, slightly out of focus, a male nurse leans over an older male patient in bed, hand on the patient&rsquo;s wrist.",
        "focal": "The nurse on the phone, face composed and attentive.",
        "setting": "Philippine tertiary hospital ICU, bedside monitor and infusion stands in soft focus.",
        "details": "Monitor screen blurred to indistinct colored traces; urinary drainage bag hanging below bed level.",
        "exclusions": "No legible monitor values or waveforms, no drug labels, no visible distress or resuscitation maneuvers.",
        "archetype": "J (Environmental storytelling)", "reviewer": "Critical care nurse and nephrologist",
    },
    "flags": [
        "AKI definition is KDIGO 2012; the KDIGO 2026 AKI/AKD guideline was in public-review draft and must be rechecked on publication.",
        "Hyperkalemia emergency sequence is by physician order or hospital protocol; review by a nephrologist before release.",
    ],
    "crosswalk": {
        "ph": "PSN 2024 nurse training topics: indications for hemodialysis, complications",
        "anna": "Acute kidney injury; acute care kidney replacement therapies",
        "edtna": "Acute kidney injury and acute renal replacement therapy",
        "nncc": "Transplant and acute therapies; concepts of kidney disease",
    },
}
