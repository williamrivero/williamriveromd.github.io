# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 3: Examine and preserve the vessels. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon compares both of a patient&rsquo;s arms under good light while the patient holds a tourniquet-free fist.",
    "objectives": [
        "Take a vessel history that finds prior central lines, cardiac devices, previous access and limb problems.",
        "Examine both arms for arterial inflow, superficial veins, outflow warning signs and baseline hand function.",
        "Explain why a good superficial vein does not settle central outflow or hand perfusion.",
        "Teach vein preservation to the patient and to the teams who place lines.",
    ],
    "big": """
{{plain:A fistula is a new river channel. Water comes in from the artery, flows along the vein, and must drain into the sea through the central veins. A wide, beautiful stretch of river is useless if the mouth downstream is silted shut.}}
<p>The picture has a limit. A river can flood its banks harmlessly. When central outflow is blocked, the new arterial flow backs up into the arm: it swells, the access runs at high pressure, needle sites bleed, and the fistula fails. The obstruction is often invisible on the surface and hidden in the patient&rsquo;s history of catheters and devices.</p>
{{cards:Key terms for this module|Inflow::The artery that supplies the access, judged by pulses, pressures and imaging.|Outflow::The path from the access vein through the axillary, subclavian and brachiocephalic veins to the heart.|Central venous stenosis::Narrowing of the central veins, often after catheters or pacemaker leads.|Vein preservation::Avoiding needles and catheters in veins that may be needed for access.|Baseline hand examination::Color, temperature, capillary refill, sensation and power, recorded before surgery.}}
<p>Most arms that look good are good. A few hide a central stenosis, a weak inflow, or a hand that is already marginal. Your work is to look for those few before you draw an incision.</p>
""",
    "case": {"title": "The swollen arm with the beautiful vein", "html": """
<p>Mr. Danilo Reyes, 57, is referred for a left upper-arm fistula. His left cephalic vein is visible and generous with a light tourniquet. He mentions that his left arm has been &ldquo;a little puffy&rdquo; for months, especially by evening. He had a dual-chamber pacemaker placed through the left subclavian vein three years ago, and a right internal jugular dialysis catheter for two months last year during a hospitalization in Pampanga.</p>
<p>On examination the left arm is 2 cm larger in circumference than the right at mid-forearm. There are small dilated veins over the left upper chest. Both radial pulses are strong.</p>
""", "questions": [
        "What does his history tell you before you look at the vein?",
        "What would you want to know before committing to the left arm?",
        "How would you explain vein preservation to him and to the medical team?"]},
    "sections": [
        ("history", "Vessel history", "The history that changes the plan", """
<p>The best predictor of hidden outflow trouble is the history of what has been inside the central veins. A catheter in a central vein injures the endothelium where it touches the wall and where blood flow is turbulent; the healing response narrows the vessel. Pacemaker and defibrillator leads do the same along their length. Peripherally inserted central catheters (PICCs) injure the very arm veins an access needs. In a case-control study of 282 hemodialysis patients, a previous PICC was strongly associated with lacking a functioning fistula (adjusted odds ratio 2.8 after accounting for vessel size, sex and prior central catheters).[[vs_elters2012]] It was a retrospective single-center study, so it shows association, not proof that PICCs caused each failure.</p>
{{fig:vs03_a}}
<p>The combination of a venous dialysis catheter and a cardiac implantable electronic device (CIED) is particularly risky: it adds central stenosis risk to the risk of an infected lead.[[vs_saad2017]] Ask about every line, device and previous access, and about arm swelling, chest-wall veins and old imaging.</p>
<div class="table-wrap"><table>
<thead><tr><th>History item</th><th>Why it matters</th><th>What you may find</th></tr></thead>
<tbody>
<tr><td>Previous central catheters, especially subclavian</td><td>Endothelial injury and stenosis</td><td>Arm or face swelling, chest-wall collaterals</td></tr>
<tr><td>Pacemaker or defibrillator leads</td><td>Stenosis along the lead; infection risk</td><td>Swelling on the device side</td></tr>
<tr><td>PICCs and repeated venipuncture</td><td>Thrombosed or scarred arm veins</td><td>Cord-like veins, scars</td></tr>
<tr><td>Previous access operations</td><td>Used segments, ligations, altered anatomy</td><td>Scars, absent thrill, old operative notes</td></tr>
<tr><td>Diabetes, peripheral arterial disease, smoking</td><td>Weak inflow, calcified arteries, marginal hand</td><td>Weak pulses, cool fingers</td></tr>
</tbody></table></div>
{{key:Ask about every catheter and device before you look at the arm. The history finds what the eye cannot.}}
"""),
        ("exam", "Examination", "Examining both arms", """
<p>Examine both arms with the patient seated and the arms supported. Feel the brachial, radial and ulnar pulses, and compare blood pressure in both arms; a difference of more than a few millimeters of mercury suggests a proximal arterial stenosis on the lower side. Test the palmar arch with an Allen test or, better, with Doppler. Map the superficial veins with a light tourniquet, noting continuity, depth and how far a straight segment runs. Look for edema, collaterals and scars.</p>
{{fig:vs03_b}}
<p>Record the hand before you touch it: color, temperature, capillary refill, sensation in each digit, grip and pinch. A neuropathic or already ischemic hand is at higher risk after access creation, and without a baseline you cannot tell later whether a deficit is new.</p>
<p>The UK Kidney Association (UKKA) 2025 guideline suggests imaging the central veins, by conventional or cross-sectional venography, before access creation in patients with clinical features or a high risk of central venous stenosis (statement 2.5, grade 2C).[[vs_ukka]] Duplex ultrasound sees the arm veins well but not the central veins behind the clavicle.</p>
{{flow:Examination sequence|Inflow::Pulses, bilateral pressures, palmar arch.|Superficial veins::Tourniquet mapping, continuity, depth, straight segment.|Outflow::Edema, collaterals, circumference difference, device side.|Hand baseline::Color, refill, sensation, power, recorded.}}
{{call:A swollen arm, chest-wall collaterals, or a device on the planned side are outflow warning signs. Image the central veins, or choose the other arm, before you commit.}}
"""),
        ("preserve", "Vein preservation", "Protecting the veins the patient will need", """
<p>Veins are a finite resource. UKKA suggests education on vascular access and vein preservation for everyone likely to need long-term hemodialysis (statement 2.2, grade 2C), and avoiding cannulas, and where possible all punctures, above the wrist in the non-dominant or fistula-planned arm for adults with a high lifetime risk of kidney failure (2.3, grade 2D).[[vs_ukka]] The evidence is mostly observational, but the harm of an unnecessary PICC in a future access arm is easy to avoid.</p>
<p>Preservation needs other teams. Write it on the problem list and the medication chart. Ask the ward to use hand veins, and the vascular access team to choose a tunneled internal jugular line over a PICC when central access is needed. Teach the patient a sentence to say: &ldquo;Please do not use this arm; I may need it for dialysis.&rdquo;</p>
{{scene:Medical ward, fictional|<p>You are asked to see a patient with CKD stage 4 on the medical ward. A PICC request for two weeks of antibiotics is on the chart. You call the attending physician, explain that this arm is the patient&rsquo;s best future access, and agree on a small-bore tunneled jugular catheter instead.</p><p class="tc-scene-take"><b>What this shows.</b> The cheapest access operation is the vein you saved from someone else&rsquo;s needle.</p>}}
{{key:When the history and the examination disagree, do not trust your first impression. Get the information that settles the question.}}
"""),
    ],
    "debrief": [
        "<p><strong>What the history says.</strong> A left-sided pacemaker, a prior catheter, months of left arm swelling, a 2 cm circumference difference and chest-wall veins all point to central venous stenosis on the left. A left upper-arm fistula would pour arterial flow into a blocked outflow and could make his arm much worse.</p>",
        "<p><strong>Before committing.</strong> Image the central veins (venography or cross-sectional imaging) and discuss the findings with the nephrologist and, because of the pacemaker, with his cardiologist. Examine the right arm fully: the right internal jugular catheter is also a risk to right central outflow, so it may need imaging too. Record his baseline hand examination on both sides.</p>",
        "<p><strong>Preservation.</strong> Tell Mr. Reyes which arm to protect and why, in plain words, and give him the sentence to say to nurses. Write the restriction in his chart and the dialysis unit&rsquo;s record, and ask that future central lines avoid the subclavian route.</p>",
    ],
    "skills": {"title": "Structured access assessment",
               "intro": "Perform on a volunteer or a consenting patient under supervision.",
               "items": [("Obtains a history of central catheters, PICCs, cardiac devices and previous access", True),
                         ("Compares pulses and blood pressure in both arms and assesses the palmar arch", False),
                         ("Maps superficial veins and notes depth, continuity and straight segments", False),
                         ("Identifies outflow warning signs and arranges central imaging when present", True),
                         ("Records a baseline hand examination on both sides", True),
                         ("Explains vein preservation to the patient and documents it in the chart", False)],
               "placement": "Access clinic"},
    "quiz": [
        ("Which history is especially relevant before choosing an arm for access?",
         ["The patient&rsquo;s preferred dialyzer", "Previous central lines and implanted cardiac devices",
          "Favorite sleeping position alone", "The time of the last meal"],
         1, "Prior central instrumentation and device leads can obstruct outflow and change the plan."),
        ("A patient has unilateral arm swelling and a large superficial vein on the same side. What should happen?",
         ["Assess the possible outflow obstruction before committing to that arm", "Select the arm because the vein is visible",
          "Reassure because swelling proves good flow", "Use a graft on that arm instead"],
         0, "Superficial appearance does not resolve an outflow warning sign; image the central veins or choose the other side."),
        ("In the El Ters case-control study, a previous peripherally inserted central catheter (PICC) was associated with what?",
         ["A higher chance of a functioning fistula", "No relationship to access outcomes",
          "Lacking a functioning fistula, independent of vessel size and prior central catheters", "Lower infection rates"],
         2, "The adjusted odds ratio was 2.8; the design shows association, not proof of causation in each case."),
        ("Why record a baseline hand examination before access creation?",
         ["It is required for billing", "So that a new postoperative deficit can be recognized as new",
          "It predicts fistula maturation exactly", "It replaces duplex ultrasound"],
         1, "Without a baseline, a later sensory or motor deficit cannot be judged as new or old."),
        ("UKKA 2025 suggests central vein imaging before access creation in which patients?",
         ["Every patient", "No patient", "Patients with clinical features or a high risk of central venous stenosis",
          "Only patients over 70"],
         2, "Statement 2.5 (grade 2C) targets imaging to those with signs or risk factors."),
    ],
    "terms": [("Central venous stenosis", "Narrowing of the large veins in the chest, often after catheters or device leads."),
              ("Allen test", "A bedside check that the hand can be supplied by the ulnar artery when the radial is compressed.")],
    "readings": [("hemodialysis-access-lifeline.html", "Vein preservation from the patient&rsquo;s side."),
                 ("dialysis-access-care.html", "What patients are taught about protecting their access arm.")],
    "calcs": ["calc-abi.html", "calc-catheter-exposure.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
