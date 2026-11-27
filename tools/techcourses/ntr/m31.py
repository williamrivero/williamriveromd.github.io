# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 31: Procedural safety and renal point-of-care ultrasound.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
KDIGO 2012 AKI 5.4.1 (2D), 5.4.2 (Not Graded), 5.4.3 (1A), 5.4.4 (1B) checked against the guideline summary.
Brass 2015 (Cochrane), 3SITES 2015, Cathedia 2008, Poggio 2020, VExUS 2020 and LUST 2021 checked against PubMed
abstracts. No doses or order sets. Fictional case."""

MODULE = {
    "image_alt": "A Filipino nephrology fellow holds an ultrasound probe over the flank of a young woman lying prone after a kidney biopsy, while a resident watches the screen and a nurse records her blood pressure.",
    "objectives": [
        "<strong>Intern:</strong> Prepare a patient for a renal procedure with the pre-procedure checklist, take part in the time-out, and monitor and report vital signs, urine and pain after the procedure.",
        "<strong>Resident:</strong> Obtain informed consent within your privileges, assist at temporary dialysis catheter insertion and kidney biopsy, and recognize and escalate complications at once.",
        "<strong>Fellow:</strong> Where privileged, place temporary dialysis catheters with ultrasound guidance at the site the Kidney Disease: Improving Global Outcomes (KDIGO) guideline prefers, perform native kidney biopsies, and use point-of-care ultrasound (POCUS) of the kidney, bladder, inferior vena cava and lungs with an honest view of its evidence.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; hands, eyes and limits</span>Procedures are where training status matters most, because the harm is immediate. An <strong>intern</strong> owns preparation, the checklist, the time-out and post-procedure observation. A <strong>resident</strong> obtains consent and assists, within what the hospital has authorized. A <strong>fellow</strong> performs catheter insertion and biopsy only where the hospital&rsquo;s credentialing grants the privilege and a supervisor is available, and uses POCUS to answer focused bedside questions. Everyone owns the right to stop.</div>
{{plain:Think of ultrasound as the reverse camera on a car. Parking by feel works most of the time; with the camera you see the post before you hit it.}}
<p>The picture has a limit. A reverse camera shows the whole rear at once. An ultrasound shows a thin slice, and a needle is visible only when it lies in that slice. Operators who see the vein and then look away while the needle advances get most of the risk back. Ultrasound also does not see coagulation, platelet function or blood pressure, the things that decide whether a biopsy bleeds. And a POCUS image answers the question you asked, such as &ldquo;is the bladder full?&rdquo; or &ldquo;are there B-lines?&rdquo;, not every question a radiologist would ask of the same organ.</p>
<p>The underlying physiology explains where the risks sit. The internal jugular vein lies beside the carotid artery and above the lung apex. The femoral vein lies beside the femoral artery in a site that is harder to keep clean. The kidney receives about a fifth of the cardiac output through a cortex full of arcuate and interlobular arteries; in kidney failure, platelets work poorly. Each procedure in this module is a needle pushed past one of these structures.</p>
{{cards:Key numbers|Ultrasound for jugular access (Cochrane 2015, 35 trials)::Total complications cut by 71% (RR 0.29) and arterial puncture by 72% (RR 0.28) versus landmarks|Ultrasound for dialysis catheters (KDIGO 2012, 5.4.3)::Recommended (1A)|Native biopsy complications (Poggio 2020, 118,064 biopsies)::Transfusion 1.6%, intervention to stop bleeding 0.3%, death 0.06%|Femoral versus jugular dialysis catheters (Cathedia, 750 patients)::Colonization similar overall (40.8 vs 35.7 per 1,000 catheter-days); jugular hematoma 3.6% vs femoral 1.1%|Lung ultrasound-guided strategy (LUST, 367 patients on hemodialysis)::Congestion relieved more often (78% vs 56%) but no difference in death, myocardial infarction or heart failure (HR 0.88)}}
<p>Most renal procedures go well when the patient is prepared, the operator is privileged and the image guides the needle. A few go wrong, usually by bleeding, and the first hour decides the outcome. Your work is to prepare carefully, consent honestly, use ultrasound properly, watch closely afterward, and call early.</p>
""",
    "case": {"title": "Four o&rsquo;clock, after the biopsy", "html": """
<p>Wednesday, a tertiary hospital in Quezon City. Ms. Kristine Lopez, 29, has suspected lupus nephritis: proteinuria of 3.4 g/day, red cell casts and a creatinine of 1.8 mg/dL that was 0.9 three months ago. Her platelets are 140 &times; 10&sup9;/L and her coagulation tests are normal. Her blood pressure the night before was 150/95 mm Hg. At 10 a.m. the nephrology fellow, Dr. Paolo Reyes, took two cores from the lower pole of the left kidney under real-time ultrasound, with the attending present. Her hemoglobin before the biopsy was 11.2 g/dL.</p>
<p>At 4 p.m. the nurse calls the resident on duty, Dr. Mae Santos. Ms. Lopez has new left flank pain, her urine is red with small clots, her blood pressure is 100/60 mm Hg and her heart rate is 118 per minute. A repeat hemoglobin, sent an hour ago per the post-biopsy protocol, is 8.9 g/dL. Her mother is asking whether &ldquo;the doctor in training&rdquo; did something wrong.</p>
""", "questions": ["What is happening, and what does the resident do in the first 30 minutes?",
                  "What risk factors for bleeding were present, and which could have been addressed before?",
                  "How should the team speak with Ms. Lopez and her mother, and what must be documented?"]},
    "sections": [
        ("consent-safety", "Consent and safety", "Consent, privileges and the time-out", """
<p>A procedure is safe when four things line up: the right indication, the right patient preparation, the right operator with the right supervision, and a team that will stop when something is wrong. Most harm comes from a gap in one of them, not from a lack of skill.</p>
<div class="table-wrap"><table><thead><tr><th>Step</th><th>Why it exists</th><th>Who owns it</th></tr></thead><tbody>
<tr><td>Indication confirmed</td><td>A procedure without a clear question to answer carries all the risk and none of the benefit</td><td>Attending and fellow</td></tr>
<tr><td>Privileges checked</td><td>The hospital, not a course or a title, decides who may perform which procedure and under what supervision</td><td>Fellow, with the department</td></tr>
<tr><td>Informed consent</td><td>The patient must understand the reason, the alternatives, the risks with real numbers, who will do the procedure and that a trainee will take part</td><td>The person performing or a privileged delegate</td></tr>
<tr><td>Pre-procedure checklist</td><td>Blood pressure, platelets, coagulation, antithrombotic drugs, allergies, fasting, consent signed, site marked</td><td>Intern and nurse, checked by the fellow</td></tr>
<tr><td>Time-out</td><td>Right patient, right side, right procedure, equipment and ultrasound ready, everyone agrees</td><td>Whole team; anyone may stop it</td></tr>
<tr><td>Post-procedure plan written</td><td>Who watches what, how often, and when to call</td><td>Fellow; carried out by nurse and intern</td></tr>
</tbody></table></div>
<p><strong>Consent the Philippine way, correctly.</strong> Decisions in Filipino families are often shared, and the family may expect to sign. If the patient has capacity, the patient consents; the family may be present and help. Say the trainee&rsquo;s role plainly: &ldquo;Dr. Reyes, a nephrology fellow, will do the biopsy with Dr. Cruz, the attending, beside him.&rdquo; Give numbers from evidence, such as the biopsy figures in this module, rather than &ldquo;maliit lang ang risk.&rdquo; Use the language the patient speaks best, and check understanding by asking them to explain it back.</p>
<p><strong>The right to stop.</strong> Every team member, including the intern and the nurse, may stop a procedure for a safety concern: wrong side, missing consent, a patient who is confused, a supervisor who has left the room, an image that does not show the needle. Your unit sets a limit on needle passes before the operator steps back; know it before you start.</p>
{{key:Before any needle, confirm indication, privilege, consent and checklist, and say out loud that anyone may stop the procedure.}}
"""),
        ("catheter-insertion", "Dialysis catheters", "Temporary dialysis catheters: site, ultrasound and the chest film", """
<p><strong>The guideline.</strong> KDIGO 2012 suggests starting kidney replacement therapy in acute kidney injury (AKI) through an uncuffed, nontunneled dialysis catheter rather than a tunneled one (2D). For the vein it gives an order of preference: right internal jugular first, femoral second, left internal jugular third, and subclavian last, with preference for the dominant side (Not Graded). It recommends ultrasound guidance for insertion (1A) and a chest radiograph promptly after placing a jugular or subclavian catheter and before its first use (1B).[[ntr31_1]]</p>
<p><strong>The mechanism behind the order.</strong> The right internal jugular vein runs almost straight into the superior vena cava and right atrium, so a catheter sits well and flows well. The left internal jugular path bends twice, so catheters kink, flow poorly and injure the vein wall. The subclavian vein is last because a catheter there can narrow it, and a narrowed subclavian vein ruins the arm for a future fistula; in a patient who may need long-term dialysis, that is a lifelong cost. The femoral vein is easy and away from the lung, but it is harder to keep clean and it keeps the patient in bed.</p>
<div class="table-wrap"><table><thead><tr><th>Site</th><th>Strength</th><th>Weakness</th><th>Bedside note</th></tr></thead><tbody>
<tr><td>Right internal jugular</td><td>Straight path, good flow</td><td>Carotid artery beside it; lung apex below</td><td>First choice in KDIGO 2012</td></tr>
<tr><td>Femoral</td><td>No pneumothorax; compressible; fast in an emergency</td><td>Infection risk rises with body mass; limits mobility</td><td>Reasonable second choice, especially in thin patients</td></tr>
<tr><td>Left internal jugular</td><td>Available when the right is not</td><td>Tortuous path, poorer flow</td><td>Third choice</td></tr>
<tr><td>Subclavian</td><td>Comfortable, lower infection in non-dialysis catheters</td><td>Pneumothorax; stenosis that can rule out future arm access</td><td>Last choice for dialysis</td></tr>
</tbody></table></div>
<p><strong>The evidence for ultrasound.</strong> A Cochrane review of 35 randomized and quasi-randomized trials with 5,108 participants compared two-dimensional ultrasound with landmarks for internal jugular catheterization in adults and children. Ultrasound reduced total complications by 71% (14 trials, 2,406 participants, risk ratio [RR] 0.29), arterial puncture by 72% (22 trials, 4,388 participants, RR 0.28) and hematoma by 73%, and increased first-attempt success by 57%. The quality of evidence was very low to moderate, and heterogeneity was significant.[[ntr31_2]] The review also found data supporting ultrasound used during the puncture, not only to mark the vein beforehand.</p>
<p><strong>Femoral or jugular?</strong> The Cathedia trial randomized 750 critically ill adults needing a first dialysis catheter to jugular or femoral placement. Catheter colonization did not differ overall (40.8 versus 35.7 per 1,000 catheter-days for femoral and jugular; hazard ratio 0.85), and catheter-related bloodstream infection was similar (2.3 versus 1.5 per 1,000 catheter-days). Body mass index changed the answer: in the heaviest third (above 28.4 kg/m&sup2;) jugular catheters were colonized less, and in the lightest third (below 24.2) femoral catheters were. Hematomas were more frequent with jugular placement (3.6% versus 1.1%).[[ntr31_4]] Colonization is a surrogate for infection. Many Filipino patients fall in the lighter group, so a femoral catheter placed well is a defensible choice when the right jugular is not suitable.</p>
<p><strong>A note on 3SITES.</strong> This trial randomized 3,471 nontunneled central venous catheters in adult intensive care to subclavian, jugular or femoral sites. Bloodstream infection or symptomatic thrombosis occurred at 1.5, 3.6 and 4.6 per 1,000 catheter-days respectively, while pneumothorax needing a chest tube occurred in 1.5% of subclavian and 0.5% of jugular insertions.[[ntr31_3]] These were general central lines, not dialysis catheters, and the trial did not measure later venous stenosis. That is why KDIGO still puts the subclavian site last for dialysis.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Vessels are small and close together, so real-time ultrasound matters even more, catheter size and length are chosen by weight, and most children need sedation or general anesthesia for insertion and biopsy. Vein preservation is a lifelong concern because a child may need dialysis access for decades. See <a href="attending-pediatric-nephrologist-24-vascular-access.html">Attending Pediatric Nephrologist, Module 24</a>.</div>
<p><strong>Philippine practice.</strong> Not every emergency room or provincial ward has an ultrasound machine at night. That is a system problem to raise, not a reason to abandon the 1A recommendation casually. If no machine is available and dialysis cannot wait, the most experienced privileged operator inserts, usually at the femoral site, and the team documents why.</p>
{{fig:ntr31_b}}
{{key:Right jugular first, femoral second, subclavian last; watch the needle tip on ultrasound the whole way; get a chest film before using a jugular or subclavian catheter.}}
"""),
        ("biopsy", "Kidney biopsy", "Native kidney biopsy: who bleeds, and what to do when they do", """
<p><strong>Why the kidney bleeds.</strong> A biopsy needle passes through the cortex, where arcuate and interlobular arteries branch densely. A small tear seals when the capsule tamponades the leak and platelets plug the vessel. Bleeding grows when pressure in the vessel is high (uncontrolled hypertension), when platelets work poorly (uremia, antiplatelet drugs), when clotting fails (anticoagulants, liver disease), when the kidney is small and scarred so a core must pass more tissue, and when the patient is acutely ill. Blood can track outside the capsule into a hematoma, into the collecting system as visible hematuria with clots, or both.</p>
<p><strong>How often.</strong> A systematic review and meta-analysis for the Kidney Precision Medicine Project pooled 87 studies with 118,064 native biopsies done with automated devices under imaging. Estimated rates were pain at the site 4.3%, hematoma 11%, macroscopic hematuria 3.5%, bleeding needing transfusion 1.6%, intervention to stop bleeding 0.3% and death 0.06% (0.03% for outpatient biopsies). Complications were more frequent in hospitalized patients and those with acute kidney disease.[[ntr31_5]] These are pooled estimates from studies of mixed quality; use them for consent, and expect your own unit&rsquo;s rate to differ.</p>
<div class="table-wrap"><table><thead><tr><th>Before the biopsy</th><th>Why</th><th>What you check</th></tr></thead><tbody>
<tr><td>Blood pressure</td><td>High arterial pressure drives bleeding through a needle tract</td><td>Controlled to the unit&rsquo;s threshold before the procedure</td></tr>
<tr><td>Platelets and coagulation</td><td>Plug formation and clotting</td><td>Count and clotting tests per protocol; uremic platelet dysfunction is not shown by the count</td></tr>
<tr><td>Antithrombotic drugs</td><td>Aspirin, clopidogrel, anticoagulants</td><td>Stopped or bridged per protocol, with the prescriber&rsquo;s agreement</td></tr>
<tr><td>Kidney size and number</td><td>Small, echogenic kidneys give low yield and more risk; a solitary kidney raises the stakes</td><td>Ultrasound before the day</td></tr>
<tr><td>Baseline hemoglobin</td><td>The comparison that tells you later whether bleeding is significant</td><td>Recorded, with the post-biopsy schedule written</td></tr>
<tr><td>Rescue plan</td><td>A rare major bleed needs blood and interventional radiology quickly</td><td>Blood type and screen; know who can embolize and how long it takes</td></tr>
</tbody></table></div>
<p><strong>After the biopsy.</strong> Most bleeding shows itself within the first hours, though it can be delayed. The post-biopsy protocol sets bed rest, vital-sign checks, urine inspection and a repeat hemoglobin. The intern and nurse watch for flank pain, dizziness, a rising pulse, a falling pressure and red urine, and call at once.</p>
<p><strong>When it bleeds.</strong> Resuscitate first: two large-bore lines, crossmatched blood, fluid, and frequent vital signs. Stop any antithrombotic drug. Use POCUS to look for a perinephric hematoma and a bladder distended with clot. Call the attending nephrologist and, per protocol, interventional radiology for angiography and embolization if instability persists, and urology if clot retention blocks the bladder. Agents that improve platelet function in uremia are a decision for the attending.</p>
{{flow:Bleeding after a kidney biopsy|Recognize::Flank pain, dizziness, rising pulse, falling pressure, red urine or clots, a falling hemoglobin.|Resuscitate::Lay flat, oxygen per protocol, two large-bore lines, fluid, send crossmatch and repeat hemoglobin.|Call::The attending nephrologist now. Do not wait for the next hemoglobin.|Look::POCUS for perinephric hematoma and a clot-filled bladder.|Stop drugs::Hold antithrombotics; avoid anything that worsens bleeding.|Escalate::Transfusion per protocol; interventional radiology for embolization if instability persists; urology for clot retention.|Talk and write::Tell the patient and family what is happening and what is being done; document times, values and actions.}}
<p><strong>Philippine practice.</strong> Kidney pathology often needs immunofluorescence and electron microscopy that many provincial hospitals send to Metro Manila, and results can take days to weeks. Interventional radiology is not available everywhere. A biopsy should be done where a major bleed can be managed, which may mean transferring the patient before the procedure rather than after a complication.</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>Hypotension, a rising pulse, or a hemoglobin fall after biopsy</li><li>Gross hematuria with clots, or inability to void after biopsy</li><li>Pulsatile blood, bright red backflow or a dilator in an artery during catheter insertion: leave it in place and call; do not pull it out</li><li>New breathlessness or falling oxygen saturation after a jugular or subclavian attempt</li><li>Any procedure where the supervisor is not available or the image does not show the needle</li></ul>}}
{{key:Every biopsy patient is a possible bleeder for the first hours. Watch pulse and pressure, not only the hemoglobin, and call at the first sign.}}
"""),
        ("pocus", "POCUS", "Point-of-care ultrasound: focused questions, honest answers", """
<p>Point-of-care ultrasound (POCUS) is ultrasound done and interpreted by the treating clinician at the bedside to answer a focused question. In nephrology, five views do most of the work.</p>
<div class="table-wrap"><table><thead><tr><th>Question</th><th>View</th><th>What you see</th><th>Limits</th></tr></thead><tbody>
<tr><td>Is there obstruction?</td><td>Kidney, long and short axis</td><td>Dilated pelvis and calyces (hydronephrosis), graded mild to severe</td><td>Early obstruction may not dilate yet; a full bladder can dilate both sides</td></tr>
<tr><td>Is the disease chronic?</td><td>Kidney size and cortex</td><td>Small kidneys with bright cortex and thin parenchyma suggest chronic disease</td><td>Diabetes and amyloidosis can keep kidneys large</td></tr>
<tr><td>Is the bladder full or clotted?</td><td>Bladder, transverse and sagittal</td><td>Volume estimate, catheter balloon position, clot</td><td>Ascites can mimic a full bladder</td></tr>
<tr><td>Is the patient congested?</td><td>Lung (B-lines, effusion) and inferior vena cava (IVC)</td><td>Many B-lines suggest interstitial fluid; a plethoric IVC suggests high right atrial pressure</td><td>B-lines also occur in pneumonia and fibrosis; IVC size changes with breathing pattern and ventilation</td></tr>
<tr><td>Is venous congestion harming the kidney?</td><td>Venous excess ultrasound (VExUS): IVC plus hepatic, portal and intrarenal venous Doppler</td><td>A graded pattern of flow abnormality</td><td>Needs Doppler skill; validated mostly after cardiac surgery</td></tr>
</tbody></table></div>
<p><strong>VExUS, and what it shows.</strong> The VExUS grading system was developed in a single-center post hoc analysis of 145 patients after cardiac surgery, with 706 ultrasound assessments. Severe congestion, defined as severe flow abnormalities in several Doppler patterns with an IVC of at least 2 cm, had the strongest association with subsequent AKI (hazard ratio 3.69; 2.82 after adjustment) and a positive likelihood ratio of 6.37 when seen at intensive care admission.[[ntr31_6]] It is a promising tool for seeing congestion; it has not been shown in a randomized trial to improve outcomes when used to guide treatment.</p>
<p><strong>LUST, and what it teaches about surrogates.</strong> The Lung Water by Ultra-Sound Guided Treatment (LUST) trial randomized 367 patients on hemodialysis with high cardiovascular risk to a strategy that used pre-dialysis lung ultrasound to adjust ultrafiltration and drugs, or to usual care. Over a mean of 1.49 years, lung congestion was relieved more often with ultrasound guidance (78% versus 56%), and the strategy was safe. The primary outcome of death, nonfatal myocardial infarction or decompensated heart failure did not differ (hazard ratio 0.88, 95% confidence interval 0.63 to 1.24). A post hoc analysis suggested fewer recurrent heart failure episodes.[[ntr31_7]] The lesson is general: POCUS reliably changes what you <em>see</em>, a surrogate, and that does not guarantee a change in what patients <em>experience</em>.</p>
<p><strong>Using it well.</strong> Ask one question before you place the probe. Record the images you base a decision on. Combine the finding with the examination, the trend and the history; a single B-line count does not prescribe a fluid goal. Learn under supervision, keep a logbook, and have your early studies reviewed. The site&rsquo;s VExUS and right atrial pressure calculators help you grade consistently.</p>
<p><strong>Philippine practice.</strong> Handheld ultrasound devices have made POCUS possible in provincial hospitals and dialysis units that have no radiologist at night. Doppler-capable machines for VExUS are less common. A bladder scan and a look for hydronephrosis are within reach of most trained residents and answer two of the most common AKI questions in minutes.</p>
{{fig:ntr31_a}}
{{key:Ask one focused question, answer it with the right view, and treat the image as a surrogate to combine with the patient, not as an order.}}
"""),
    ],
    "debrief": [
        "<p><strong>What is happening, first 30 minutes.</strong> She is bleeding from the biopsy site, into the collecting system (clots) and probably around the kidney (flank pain), with hemodynamic signs of significant blood loss: a heart rate of 118, a pressure of 100/60 and a hemoglobin fall of 2.3 g/dL. Dr. Santos lays her flat, gives oxygen per protocol, secures two large-bore lines, starts fluid, sends crossmatch and repeat blood counts, and calls the attending nephrologist at once rather than waiting for another hemoglobin. A bedside ultrasound can show a perinephric hematoma and whether the bladder is filling with clot. Antithrombotic drugs are held. If she does not stabilize, the attending arranges transfusion and interventional radiology for embolization, and urology if clots block the bladder.</p>",
        "<p><strong>Risk factors.</strong> She was a hospitalized patient with acute kidney disease, which Poggio and colleagues found carries higher complication rates than outpatient biopsy. Her blood pressure was 150/95 mm Hg the night before; uncontrolled pressure drives bleeding and should have been brought to the unit&rsquo;s threshold before the procedure. Uremia may impair platelet function despite a normal count. Two cores is a usual number; the operator&rsquo;s experience, real-time guidance and a lower-pole approach were appropriate. A written rescue plan (blood type and screen, knowing who can embolize) belongs in the preparation.</p>",
        "<p><strong>Talking and documenting.</strong> The attending and fellow speak with Ms. Lopez and her mother together and honestly: bleeding is a known risk that was discussed in consent (transfusion in about 1.6% of biopsies), this is what is being done, and this is who is responsible. Avoid defensiveness and blame; a fellow performing under supervision is normal training, and the attending is accountable. Document the time of each finding, each value, each action, who was called and when, and the conversation with the family. Report through the hospital&rsquo;s incident system per policy, so the team can learn from it.</p>",
    ],
    "skills": {"title": "Procedural safety and renal POCUS",
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local and never grants a privilege.",
               "items": [("Completes a pre-biopsy checklist including blood pressure, platelets, coagulation, antithrombotics, kidney size and rescue plan", False),
                         ("Obtains informed consent that states the trainee&rsquo;s role and quotes complication rates from evidence", False),
                         ("States the KDIGO 2012 site order and grades for temporary dialysis catheters, and the reason for each", False),
                         ("Performs supervised POCUS of kidney, bladder, IVC and lungs and reports a focused answer", False),
                         ("Leads the first response to simulated post-biopsy bleeding, including escalation and documentation", False)],
               "placement": "Procedure room, ward, ICU or simulation; privileges remain with the hospital"},
    "quiz": [
        ("Two hours after a kidney biopsy, the patient&rsquo;s pulse rises from 84 to 112 per minute and she feels dizzy. What should the intern do first?",
         ["Wait for the scheduled hemoglobin result before calling",
          "Recheck the vital signs, keep her flat, and call the resident at once",
          "Encourage her to walk to the bathroom to check her urine",
          "Give oral fluids and reassess in 2 hours"],
         1,
         "A rising pulse and dizziness after biopsy suggest bleeding; the intern should keep her flat, recheck and call immediately. Waiting for the hemoglobin delays care, and walking may worsen bleeding or cause a fall."),
        ("A resident is asked to obtain consent for a native kidney biopsy that a fellow will perform. Which statement belongs in the consent conversation?",
         ["&ldquo;The risk is very small, so there is nothing to worry about&rdquo;",
          "&ldquo;Bleeding needing transfusion occurs in about 1.6 of every 100 biopsies, and a fellow will perform it with the attending present&rdquo;",
          "&ldquo;Your family can sign for you because they will decide anyway&rdquo;",
          "&ldquo;The attending will do it&rdquo; even though the fellow will"],
         1,
         "Consent should give real numbers (pooled transfusion rate 1.6%) and state the trainee&rsquo;s role. A capable patient consents for herself, and misstating who performs the procedure invalidates consent."),
        ("According to KDIGO 2012, which is the preferred vein for a temporary dialysis catheter in AKI, and how should it be inserted?",
         ["Left subclavian, by landmarks",
          "Right internal jugular, with ultrasound guidance (1A)",
          "Left internal jugular, by landmarks",
          "Right subclavian, with ultrasound guidance"],
         1,
         "KDIGO 2012 prefers the right internal jugular first, femoral second, left jugular third, subclavian last (Not Graded), and recommends ultrasound guidance (1A). The subclavian vein risks stenosis that ruins future arm access."),
        ("A thin patient (body mass index 21 kg/m&sup2;) needs urgent dialysis; the right internal jugular vein is thrombosed. Which choice is best supported?",
         ["Subclavian catheter, because infection is lowest",
          "Femoral catheter under ultrasound, because Cathedia found lower colonization with femoral catheters in the lightest patients",
          "Delay dialysis until the jugular vein recanalizes",
          "Left jugular by landmarks to avoid the groin"],
         1,
         "KDIGO 2012 ranks femoral second, and Cathedia found femoral colonization lower than jugular in patients with BMI below 24.2. 3SITES studied general central lines and the subclavian site threatens future access."),
        ("In the LUST trial, a lung ultrasound-guided strategy in patients on hemodialysis relieved congestion more often (78% vs 56%). What happened to the primary outcome?",
         ["Death, myocardial infarction and heart failure fell by half",
          "There was no significant difference (HR 0.88, 95% CI 0.63 to 1.24)",
          "The strategy increased intradialytic hypotension deaths",
          "The trial was stopped early for benefit"],
         1,
         "Congestion on ultrasound is a surrogate; improving it did not change the composite of death, myocardial infarction or decompensated heart failure. A post hoc analysis suggested fewer recurrent heart failure episodes."),
    ],
    "terms": [("AKI", "Acute kidney injury"), ("BMI", "Body mass index"), ("CI", "Confidence interval"),
              ("HR", "Hazard ratio"), ("ICU", "Intensive care unit"), ("IVC", "Inferior vena cava"),
              ("KDIGO", "Kidney Disease: Improving Global Outcomes"), ("LUST", "Lung Water by Ultra-Sound Guided Treatment (trial)"),
              ("POCUS", "Point-of-care ultrasound"), ("RR", "Risk ratio"), ("VExUS", "Venous excess ultrasound")],
    "readings": [("pocus-nephrology.html", "POCUS in Nephrology"),
                 ("physician-on-duty-10-catheters.html", "Physician on Duty, Module 10: Catheters"),
                 ("attending-nephrologist-11-glomerular-disease-biopsy.html", "Attending Nephrologist, Module 11: Glomerular disease and biopsy"),
                 ("vascular-surgeon-08-dialysis-catheters-and-central-veins.html", "Vascular Surgeon, Module 8: Dialysis catheters and central veins")],
    "calcs": ["calc-vexus-grading.html", "calc-rap-ivc.html", "calc-egfr-ckd-epi.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
