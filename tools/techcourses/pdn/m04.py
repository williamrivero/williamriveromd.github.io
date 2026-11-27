# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 4: Assessment, fluid balance and weight-based arithmetic. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Obtain weights, heights and blood pressures that can be trusted, using the right scale, conditions and cuff.",
        "Account for every fluid route in a child, including flushes, medicines and dialysis balance.",
        "Calculate weight-based rates with units at every step, and verify them with an independent check.",
        "Classify a child&rsquo;s blood pressure by percentile and recognize when a reading does not fit the child.",
    ],
    "big": """
<p>In adult dialysis, a 200-gram error on the scale is noise. In a 10-kilogram child it is 2% of body weight. A decimal slip in a fluid order can be the whole difference between safe and dangerous. Pediatric dialysis rests on small numbers, so it rests on measurement and arithmetic.</p>
<p>Your work in this module is to make every number trustworthy before it reaches a decision: measured the same way each time, written with units, and checked by a second person who did not see your answer.</p>
{{plain:Think of a recipe scaled down from a restaurant to a single serving. A pinch of salt that disappears in a big pot ruins a small bowl. Every ingredient must be measured more carefully, not less, when the batch is small.}}
<p>The picture has a limit. A recipe scales in proportion; a child does not. A child&rsquo;s body surface area, blood volume and metabolic rate do not shrink at the same pace as weight. That is why some orders use kilograms and others use square meters, and why you must know which one an order uses.</p>
{{cards:Key terms for this module|Target weight::The weight the nephrologist aims for after fluid removal, reviewed as the child grows.|Fluid balance::All fluid in minus all fluid out over a stated period.|mL/kg/h::Volume per kilogram of body weight per hour.|Body surface area (BSA)::An estimate of skin area in square meters, from height and weight.|Percentile::Where a value sits among healthy children of the same age, sex and height.}}
""",
    "case": {"title": "300 per hour", "html": """
<p><strong>Kyla Ramos, 6</strong>, weighs 20 kilograms and is on acute PD in a provincial hospital. The written order is net removal of 300 mL over 3 hours. The bedside worksheet, copied by a busy night nurse, reads &ldquo;300 mL/hour&rdquo;. <strong>Nurse Paolo</strong> takes over at 6 a.m. Kyla&rsquo;s weight this morning is 20.6 kilograms on a different scale than yesterday&rsquo;s.</p>
""", "questions": ["What is the intended hourly removal, in mL/h and mL/kg/h?",
                  "Can Paolo continue with the worksheet as written?",
                  "Is today&rsquo;s weight gain real?"]},
    "sections": [
        ("trustworthy-measurements", "Measurements", "Making measurements trustworthy", """
<p>A weight is only comparable to another weight taken the same way. Use the same calibrated scale, at the same point in the routine, with the same clothing or a dry diaper, and note whether the abdomen contains dialysate. A child with 600 mL of PD fluid in the abdomen weighs 0.6 kilograms more than the same child drained.</p>
<div class="table-wrap"><table>
<thead><tr><th>Measurement</th><th>Do</th><th>Common error</th></tr></thead>
<tbody>
<tr><td>Weight</td><td>Same scale, same time, minimal clothing; infants nude or dry diaper; record PD fluid in or out</td><td>Different scale; wet diaper; full abdomen not recorded</td></tr>
<tr><td>Height or length</td><td>Length board under 2 years; stadiometer, shoes off, heels to the wall after</td><td>Tape measure on a moving child</td></tr>
<tr><td>Blood pressure</td><td>Right cuff, child seated and calm, same arm (not the fistula arm), repeat if high</td><td>Cuff too small reads falsely high</td></tr>
<tr><td>Temperature, heart rate, breathing</td><td>Compare with the child&rsquo;s own baseline and age norms</td><td>Reading one value without the trend</td></tr>
</tbody></table></div>
<p>The target weight is not permanent. A growing child gains lean tissue, so a target weight that does not rise can slowly dehydrate the child. Report steady weight below target together with symptoms, and report a target that has not been reviewed in months.</p>
{{key:A weight means nothing without its conditions. Same scale, same time, same clothing, abdomen full or empty recorded.}}
"""),
        ("every-route-counts", "Fluid routes", "Every route counts", """
<p>In a small child, the &ldquo;hidden&rdquo; fluids can be a large share of the day. Intravenous line flushes, medicine diluents and feed water add up. A 10-kilogram child who receives ten 5 mL flushes a day has received 50 mL, about 5 mL per kilogram, before any drink.</p>
{{fig:pdn04_a}}
<p>Distinguish two balances. <strong>Body fluid balance</strong> counts everything in and out of the child. <strong>Dialysis balance</strong> counts only what the dialysis removed or added. For PD, net removal for a completed exchange is drained volume minus instilled volume, recorded separately from the initial drain. Confirm whether a cycler&rsquo;s displayed total includes the initial drain or the last fill before you write it down.</p>
<p>Insensible losses are larger in proportion in small children, and fever or fast breathing increases them. Maintenance fluid estimates such as the Holliday&ndash;Segar method are planning tools for the prescriber, not targets for the nurse.</p>
{{key:Count the flushes and the medicines. In a small child they can be a meal&rsquo;s worth of water.}}
"""),
        ("arithmetic-with-units", "Arithmetic", "Arithmetic with units", """
<p>Write the units at every step. Units that do not cancel tell you a step is wrong before the child pays for it.</p>
{{fig:pdn04_b}}
{{formula:Hourly removal = total volume &divide; hours<br>Weight-based rate = hourly removal &divide; weight (kg)<br>Example: 300 mL &divide; 3 h = 100 mL/h; 100 mL/h &divide; 20 kg = 5 mL/kg/h}}
<p>That arithmetic verifies an order. It does not tell you the order is clinically right. A safe removal rate depends on the child&rsquo;s blood pressure, blood volume, symptoms and the nephrologist&rsquo;s goal. Never infer a safe rate from arithmetic alone.</p>
<h3>The independent check</h3>
<p>The second person calculates from the order and the weight without seeing your answer. Then you compare. A second person who only reads your number and nods tends to agree with it, including its errors.</p>
{{scene:6:05 a.m., the handover|<p>Paolo reads the order, then the worksheet. 300 mL over 3 hours is 100 mL per hour, 5 mL/kg per hour. The worksheet says 300 mL per hour, three times the order. He stops the cycler program change, asks a colleague to calculate separately, gets 100 mL/h, and calls the nephrologist to confirm the order and the machine entry.</p><p class="tc-scene-take">A mismatch between order, worksheet and machine is a stop sign, not a rounding issue.</p>}}
{{key:Units at every step, a second person calculating blind, and a stop whenever order, worksheet and machine disagree.}}
"""),
        ("blood-pressure-in-children", "Blood pressure", "Blood pressure in children", """
<p>A child&rsquo;s normal blood pressure depends on age, sex and height. The 2017 American Academy of Pediatrics (AAP) guideline classifies children under 13 years by percentile (elevated from the 90th, stage 1 hypertension from the 95th) and uses fixed values from age 13, aligned with adult categories (stage 1 from 130/80 mmHg).[[pdn_flynn2017]] For children with CKD, it suggests a treatment goal of a 24-hour mean arterial pressure below the 50th percentile on ambulatory monitoring.</p>
<p>Use a cuff whose bladder width is at least 40% of the arm&rsquo;s circumference and whose length covers 80% to 100% of it. A cuff that is too small reads falsely high, which can lead to unnecessary fluid removal. Low blood pressure in a child is often a late sign of shock, because children compensate with heart rate first; see Module 15.</p>
{{key:Interpret a child&rsquo;s blood pressure against age, sex and height, with the right cuff, and always beside the heart rate.}}
"""),
    ],
    "debrief": ["""
<p><strong>The arithmetic.</strong> 300 mL &divide; 3 h = 100 mL/h; &divide; 20 kg = 5 mL/kg/h. The worksheet&rsquo;s 300 mL/h is three times the order.</p>
<p><strong>Continue?</strong> No. Paolo stops at the mismatch, obtains an independent calculation, and has the nephrologist confirm the order and the machine entry before any change. He documents the discrepancy and files an incident report so the copying step can be fixed.</p>
<p><strong>The weight.</strong> A 0.6 kg rise on a different scale is uninterpretable until he reweighs on yesterday&rsquo;s scale, with the abdomen&rsquo;s fill state recorded. If the gain is real, he reports it with the balance and blood pressure.</p>
"""],
    "skills": {"title": "Measurement and arithmetic", "intro": "Use models and fictional charts first.",
               "items": [("Weighs a child under standard conditions and records clothing and PD fill state", True),
                         ("Selects a cuff by arm circumference and repeats a high reading", False),
                         ("Reconciles a 24-hour intake and output sheet including flushes and medicine volumes", False),
                         ("Calculates mL/h and mL/kg/h with units and an independent blind check", True),
                         ("Stops and escalates when order, worksheet and machine entry disagree", True)],
               "placement": "Audit three real pediatric charts (de-identified) for scale, clothing and fill-state documentation; report gaps to your preceptor."},
    "quiz": [
        ('A 10-kg child: 200 g scale error is what share of body weight?',
         ['2%', '0.2%', '20%', '0.02%'], 0,
         '0.2 &divide; 10 = 2%.'),
        ('Why record whether the abdomen contains PD fluid when weighing?',
         ['It changes the color', 'Intraperitoneal fluid adds weight that is not body water gain', 'It does not matter', 'Hospital policy only'], 1,
         '600 mL in the abdomen adds about 0.6 kg.'),
        ('Which measures length in a child under 2 years?',
         ['Tape measure while walking', 'A wall chart standing', 'A length board', 'Parent&rsquo;s estimate'], 2,
         'Infants are measured lying on a length board.'),
        ('A cuff that is too small:',
         ['Reads falsely low', 'Has no effect', 'Measures heart rate', 'Reads falsely high'], 3,
         'Overestimation can trigger unneeded fluid removal.'),
        ('Recommended cuff bladder width is at least what share of arm circumference?',
         ['40%', '20%', '60%', '100%'], 0,
         'Length 80%&ndash;100% of the circumference.'),
        ('300 mL over 3 hours in a 20-kg child equals:',
         ['300 mL/h', '100 mL/h, 5 mL/kg/h', '15 mL/kg/h', '60 mL/h'], 1,
         '300 &divide; 3 = 100; 100 &divide; 20 = 5.'),
        ('The calculation is correct. What follows?',
         ['It is safe', 'Increase it', 'Check it against the order and the child&rsquo;s clinical state', 'Nothing'], 2,
         'Arithmetic and clinical appropriateness are separate checks.'),
        ('What makes a double check independent?',
         ['The second nurse reads your answer', 'The parent checks', 'It is done twice by you', 'The second nurse calculates without seeing your answer'], 3,
         'Seeing an answer biases agreement.'),
        ('Ten 5 mL flushes in a 10-kg child equal:',
         ['5 mL/kg', '0.5 mL/kg', '50 mL/kg', 'Nothing important'], 0,
         '50 mL &divide; 10 kg = 5 mL/kg.'),
        ('Net removal for a completed PD exchange is:',
         ['Fill minus drain', 'Drained volume minus instilled volume', 'Initial drain only', 'The cycler&rsquo;s first number'], 1,
         'Record the initial drain separately.'),
        ('Why must the target weight be reviewed in a growing child?',
         ['It never changes', 'For billing', 'Lean growth means an unchanged target can slowly dehydrate the child', 'Parents ask'], 2,
         'Growth adds tissue.'),
        ('In the AAP 2017 guideline, a 14-year-old&rsquo;s stage 1 hypertension starts at:',
         ['90th percentile', '120/70', '160/100', '130/80 mmHg'], 3,
         'From age 13, fixed values aligned with adult categories.'),
        ('For children with CKD, the AAP 2017 suggested treatment goal is:',
         ['24-hour MAP below the 50th percentile on ambulatory monitoring', 'Any BP below 140/90', 'Systolic below 100', 'No goal'], 0,
         'A stricter goal for CKD.'),
        ('Low blood pressure in a child is often:',
         ['An early sign of shock', 'A late sign of shock', 'Normal on dialysis', 'Caused by the cuff'], 1,
         'Children compensate with heart rate first.'),
        ('Worksheet, order and machine disagree. You should:',
         ['Average them', 'Use the machine value', 'Stop, obtain an independent calculation and confirm with the prescriber', 'Use the worksheet'], 2,
         'A mismatch is a stop sign.'),
    ],
    "terms": [("Target weight", "The weight aimed for after fluid removal; reviewed as the child grows."),
              ("Fluid balance", "All fluid in minus all fluid out over a stated period."),
              ("Insensible losses", "Water lost through skin and breath, not measured directly."),
              ("Stadiometer", "A wall-mounted device for measuring standing height."),
              ("Percentile", "Where a value sits among healthy children of the same age, sex and height."),
              ("Ambulatory blood pressure monitoring", "Automatic blood pressure readings over 24 hours during normal life.")],
    "readings": [("dry-weight-determination.html", "How dry weight is set and why it changes."),
                 ("fluid-management-dialysis.html", "Fluid management on dialysis.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-pediatric-bp.html", "calc-holliday-segar.html", "calc-fluid-overload.html"],
}
