# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 8: Dialysis catheters and central veins. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A procedure room with ultrasound and fluoroscopy, a surgeon checking a guidewire position on the screen while a nurse monitors the patient.",
    "objectives": [
        "Explain how a dialysis catheter injures central veins and why biofilm makes catheter infections hard to clear.",
        "Choose a catheter site that protects future access, using the UK Kidney Association (UKKA) 2025 graded statements.",
        "Recognize insertion complications that turn troubleshooting into an emergency.",
        "Give every catheter an indication, a review date and an exit plan.",
    ],
    "big": """
{{plain:A dialysis catheter is a temporary bridge across a river. It gets traffic across today, but every day it stands, it erodes the riverbanks it rests on, and one day those banks may be needed for a permanent crossing.}}
<p>The picture has a limit. A bridge erodes slowly and visibly. A catheter injures the vein wall where it touches and where flow is turbulent; the healing response narrows the vein, often silently, until a fistula in that arm years later swells the limb. Meanwhile a film of bacteria and fibrin, a biofilm, coats the catheter within days, and antibiotics struggle to reach the bacteria inside it.</p>
{{cards:Key terms for this module|Tunneled catheter::A cuffed catheter tunneled under the skin to the vein, used for weeks to months.|Non-tunneled catheter::An uncuffed catheter for short-term use, usually days.|Fibrin sheath::A sleeve of fibrin and cells around a catheter tip that blocks flow.|Biofilm::A layer of bacteria in a matrix on the catheter surface, protected from antibiotics.|Exit plan::The date and condition under which the catheter will be removed or replaced by an arteriovenous access.}}
<p>Some patients need a catheter: an urgent start, a failed access, or a short expected course. Your work is to place it where it protects the future, recognize when insertion has gone wrong, and make sure it does not quietly become permanent.</p>
""",
    "case": {"title": "Breathless after the exchange", "html": """
<p>Mr. Ramon Lacson, 70, had his left subclavian tunneled catheter exchanged over a guidewire this morning by a junior colleague because of poor flow. Two hours later the dialysis nurse calls: the new catheter will not run above 180 mL/min, and Mr. Lacson has become breathless. His oxygen saturation is 89% on room air, down from 97%, and his blood pressure is 96/60 mm Hg. The nurse asks whether to reverse the lines and try again.</p>
<p>There is no chest radiograph after the exchange. His right internal jugular vein was occluded by an old catheter two years ago, which is why the left subclavian was used.</p>
""", "questions": [
        "What do you tell the nurse in the next minute?",
        "What complications are you worried about, and what do you need now?",
        "Looking back, what should his access plan have said about this catheter?"]},
    "sections": [
        ("injury", "How catheters harm", "How catheters injure veins and harbor infection", """
<p>A catheter moves with every heartbeat and breath. Where its tip or body rubs the vein wall, the endothelium is injured; platelets and fibrin deposit; smooth muscle cells proliferate. The result is fibrin sheath around the catheter and stenosis in the vein wall, worst in the subclavian and brachiocephalic veins, which bend and are compressed between the clavicle and first rib. A catheter on the same side as a future fistula, or alongside a pacemaker lead, adds to this injury.[[vs_saad2017]]</p>
{{fig:vs08_a}}
<p>Within days, bacteria from the skin or the hub colonize the catheter and form biofilm. Inside it they grow slowly and are shielded from antibiotics and white cells. This is why the same organism often returns after treatment, and why some organisms usually mean removal (Module 15).</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Mechanism</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Early dysfunction</td><td>Malposition, kink, tip against the wall</td><td>Poor flow from day one, positional flow</td></tr>
<tr><td>Late dysfunction</td><td>Intraluminal thrombus, fibrin sheath</td><td>Falling flow over weeks, high pressures</td></tr>
<tr><td>Central venous stenosis</td><td>Wall injury and healing</td><td>Arm, face or chest swelling, collaterals</td></tr>
<tr><td>Infection</td><td>Biofilm on the catheter surface</td><td>Fever or rigors at connection, exit-site pus</td></tr>
</tbody></table></div>
"""),
        ("site", "Choosing the site", "Where to place it, and what the guidelines say", """
<p>The UK Kidney Association (UKKA) 2025 guideline gives graded statements on catheter insertion and care. It recommends routinely favoring the right internal jugular vein for tunneled catheters, though imaging, access location and preference may modify the choice (statement 5.1, grade 1C); routinely avoiding the subclavian route where alternative veins are available (5.2, grade 1C); real-time ultrasound for insertion, with fluoroscopy for left-sided or subclavian approaches (5.3, grade 1C); access by trained staff with a strict aseptic approach (5.4, grade 1C); assessment of the exit site and function at each session (5.5, grade 1C); and exit-site disinfection with 2% chlorhexidine (5.6, grade 2C).[[vs_ukka]]</p>
<p>For dysfunction, UKKA recommends locking each lumen with a thrombolytic as initial treatment (6.2, grade 1C), and replacing the catheter, usually by guidewire exchange, when that fails, in a setting where fibrin sheath disruption is available (6.3, grade 1C).[[vs_ukka]] Repeated manipulation without a diagnosis wastes time and can injure the vein.</p>
{{flow:Every catheter needs four answers|Why now?::The indication: urgent start, failed access, short course, or patient choice.|Where?::The site that protects the planned arteriovenous access.|How was it checked?::Imaging used at insertion and position confirmed.|Until when?::Review date, removal condition, and who owns it.}}
{{key:A catheter without a removal date tends to become permanent. Write the date when you write the indication.}}
"""),
        ("complications", "When it goes wrong", "Insertion complications: when to stop troubleshooting", """
<p>Most poor flow after insertion is mechanical and fixable. But some complications threaten life: pneumothorax, hemothorax, perforation of a central vein or the right atrium with bleeding into the mediastinum or pericardium, arterial puncture, and air embolism. Their early signs overlap with ordinary problems: poor flow, chest discomfort, breathlessness, low blood pressure. The difference is that the patient is getting worse.</p>
{{fig:vs08_b}}
<p>The rule is simple: when a patient deteriorates after a catheter procedure, the problem is the patient, not the flow rate. Stop routine troubleshooting. Do not reverse lines or keep dialyzing through a catheter of uncertain position. Assess airway, breathing and circulation, image the chest, and call the senior and emergency team. Device-specific steps belong to the manufacturer&rsquo;s instructions and your local protocol; this module rehearses recognition and the decision to stop.</p>
{{scene:Procedure room, fictional|<p>During a right jugular insertion, the guidewire meets resistance at 15 cm. Your trainee wants to push harder. You stop, check the wire under fluoroscopy, see it heading into a small branch, withdraw and redirect under imaging.</p><p class="tc-scene-take"><b>What this shows.</b> Resistance is information. Pushing through it turns a nuisance into a perforation.</p>}}
{{call:Stop using the catheter and call for emergency assessment if a patient becomes breathless, hypotensive, hypoxic, or develops chest pain after insertion or exchange. Confirm catheter position with imaging before any further use.}}
"""),
    ],
    "debrief": [
        "<p><strong>The next minute.</strong> Tell the nurse to stop dialysis through the new catheter, not to reverse the lines, to give oxygen, to lay him in a position he tolerates, and to call the physician on duty to assess him now. You are on your way, or the emergency team is called.</p>",
        "<p><strong>Your worries.</strong> After a left subclavian exchange with poor flow, new hypoxia and low pressure, consider pneumothorax or hemothorax, venous or atrial perforation with mediastinal or pericardial bleeding, malposition, and air embolism. He needs a chest radiograph now, bedside ultrasound for pericardial fluid, monitoring, and senior help. Until position is confirmed, the catheter is not used.</p>",
        "<p><strong>The access plan.</strong> His right jugular is already occluded; a left subclavian catheter threatens his left central veins and every future left-arm access. His plan should have named the indication, the expected duration, the planned arteriovenous access and side, and a removal date, and asked whether a fistula or graft could be created to remove the need for a subclavian line.</p>",
    ],
    "skills": {"title": "Catheter indication, safety and exit plan",
               "intro": "Simulation or supervised procedure list.",
               "items": [("States the indication and expected duration before insertion", False),
                         ("Chooses a site that protects the planned arteriovenous access", False),
                         ("Uses real-time ultrasound, and fluoroscopy where indicated", True),
                         ("Stops and escalates when the patient deteriorates after insertion", True),
                         ("Writes a review date and removal or replacement plan with an owner", True)],
               "placement": "Simulation or procedure room"},
    "quiz": [
        ("New breathlessness and hypotension follow poor function of a recently exchanged catheter. What is the best response?",
         ["Urgent patient assessment, stop using the catheter, image and escalate", "Reverse the lines and continue",
          "Delay until the next routine visit", "Increase the blood pump speed"],
         0, "Clinical deterioration changes the task from troubleshooting to possible insertion-complication management."),
        ("What should accompany every catheter indication?",
         ["A promise of indefinite use", "A review date and a removal or longer-term access plan",
          "A statement that future veins no longer matter", "Monthly exchange"],
         1, "Catheters belong inside the patient&rsquo;s ongoing access strategy."),
        ("UKKA 2025 recommends which vein as the routine first choice for a tunneled catheter?",
         ["Left subclavian", "Right internal jugular", "Femoral", "Left external jugular"],
         1, "Statement 5.1 (grade 1C); the subclavian route is avoided where alternatives exist (5.2)."),
        ("What does UKKA recommend as initial treatment for catheter dysfunction?",
         ["Immediate removal", "Locking each lumen with a thrombolytic agent", "Reversing lines permanently", "Systemic heparin infusion"],
         1, "Statement 6.2 (grade 1C); exchange follows if thrombolytics fail (6.3)."),
        ("Why do subclavian catheters particularly threaten future arm access?",
         ["They are shorter", "They injure the subclavian and brachiocephalic veins, causing central stenosis",
          "They cause hand ischemia", "They cannot be tunneled"],
         1, "Wall injury where the vein bends and is compressed leads to stenosis that later obstructs arm access outflow."),
    ],
    "terms": [("Guidewire exchange", "Replacing a catheter over a wire through the same tract."),
              ("Pneumothorax", "Air in the chest outside the lung, which can collapse it.")],
    "readings": [("dialysis-access-infection.html", "Catheter infections and why biofilm matters."),
                 ("dialysis-access-care.html", "How catheters are cared for in the unit.")],
    "calcs": ["calc-catheter-exposure.html", "calc-access-infection-rate.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
