# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 12: Pulse Restored: ROSC, Transfer and Handover. Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A nurse handing a written summary to ambulance staff beside a stretcher while the monitor shows a regular rhythm.",
    "objectives": [
        "Confirm return of spontaneous circulation with a definite pulse and blood pressure, not with the rhythm alone.",
        "Deliver the first ten minutes of care after return of spontaneous circulation (ROSC): airway, oxygen titrated to 90 to 98%, mean arterial pressure of at least 65 mm Hg, a 12-lead ECG, glucose and potassium.",
        "Recognize re-arrest early and return to the arrest algorithm without delay.",
        "Explain what a freestanding dialysis unit can and should not do after ROSC, including why dialysis is not restarted without the attending nephrologist.",
        "Give a structured handover that combines the arrest facts and the dialysis facts.",
    ],
    "big": """
{{plain:A returned pulse is like a fire that has stopped burning but is still smoking. The danger has changed shape, not ended. The heart that just restarted is stunned and irritable; the brain that went without blood is swelling; the cause of the arrest, whether potassium or blood loss or a blocked artery, is usually still there.}}
<p>The picture has a limit. Smoke does not usually reignite on its own, but a heart after arrest often does: re-arrest is common in the first minutes and hours. And unlike a fire scene, the patient now needs things a dialysis unit may not have: mechanical ventilation, continuous blood pressure monitoring, emergency coronary angiography, temperature control. In one large series, 60% of patients who arrested in dialysis units died within 48 hours.[[karnik2001]] The minutes after ROSC decide whether the patient reaches the place that can give that care.</p>
<p>This module covers the immediate post-ROSC priorities that apply in any dialysis unit, and the handover that lets the receiving team continue without starting over.</p>
{{cards:Key terms for this module|Return of spontaneous circulation (ROSC)::A definite pulse and measurable blood pressure after cardiac arrest.|Re-arrest::Loss of circulation again after ROSC.|Mean arterial pressure (MAP)::The average arterial pressure driving organ perfusion.|Temperature control::Deliberate management of body temperature after arrest in patients who do not follow commands.|Handover::Structured transfer of information and responsibility to the next team.|Post-cardiac arrest syndrome::The combined brain injury, heart dysfunction and whole-body inflammation that follow arrest.}}
""",
    "case": {"title": "Pulse restored, now what?", "html": """
<p>At 2:35 p.m., after 11 minutes of CPR, two shocks and two doses of epinephrine, Mr. Leonardo Ramos, 70, has a palpable carotid pulse at a freestanding unit in Taytay, Rizal. The monitor shows sinus tachycardia at 112. His blood pressure is 84/50 mm Hg. He is not following commands. He is breathing on his own, irregularly, with saturation 89% on a mask. He arrested 3 hours into a session; 2.6 L had been removed, and the blood was returned at the start of the arrest. His pre-dialysis potassium this morning was 5.1 mmol/L.</p>
<p>The ambulance, called at the start of the arrest, is stuck in traffic; expected arrival is 20 minutes. A nurse asks the physician-on-duty, &ldquo;Should we put him back on dialysis while we wait?&rdquo;</p>
""", "questions": ["How do you confirm this is ROSC, and what do you check in the next ten minutes?",
                  "What should the answer be about restarting dialysis?",
                  "What goes into the handover when the ambulance arrives?"]},
    "sections": [
        ("confirm", "Confirming ROSC", "Is it really ROSC?", """
<p>ROSC is a clinical finding: a definite pulse and a measurable blood pressure. An organized rhythm on the monitor is not enough; it may be PEA (Module 3). Signs that support ROSC include a palpable central pulse, a measurable blood pressure, an abrupt rise in end-tidal carbon dioxide if capnography is in use (COR 2b, LOE B-NR),[[aha2025_als]] spontaneous breathing, and movement.</p>
{{fig:rl12_rosc_check}}
<div class="table-wrap"><table>
<thead><tr><th>Finding at the rhythm check</th><th>Interpretation</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Organized rhythm, definite pulse, measurable pressure</td><td>ROSC</td><td>Post-ROSC care; keep pads on</td></tr>
<tr><td>Organized rhythm, no definite pulse</td><td>PEA</td><td>Resume compressions at once</td></tr>
<tr><td>Organized rhythm, weak uncertain pulse, no measurable pressure</td><td>Treat as no pulse</td><td>Resume compressions; recheck at the next pause</td></tr>
<tr><td>Pulse present, then lost</td><td>Re-arrest</td><td>Compressions; arrest algorithm</td></tr>
</tbody></table></div>
<p>Keep the pads on and the defibrillator connected after ROSC. Re-arrest is common, and when it happens the team should be compressing again within seconds, with the last rhythm, drugs and times already on the recorder&rsquo;s sheet.</p>
{{key:ROSC means a definite pulse and a pressure, not just a rhythm. Keep the pads on, because re-arrest is common.}}
"""),
        ("first10", "The first ten minutes", "The first ten minutes after the pulse returns", """
<p>The 2025 AHA post-cardiac arrest guideline sets the targets for adults.[[aha2025_post]] A freestanding dialysis unit can meet most of them for the first minutes with what it already has: oxygen, a bag-mask, monitoring, IV access, saline, a 12-lead ECG, a glucose meter and a potassium sample.</p>
{{fig:rl12_first10}}
<div class="table-wrap"><table>
<thead><tr><th>Priority</th><th>2025 AHA recommendation</th><th>Grade</th><th>In a dialysis unit</th></tr></thead>
<tbody>
<tr><td>Oxygen</td><td>100% inspired oxygen until saturation can be measured reliably; avoid hypoxemia; then titrate to SpO2 90% to 98%</td><td>COR 1, B-R; COR 1, B-NR; COR 2a, B-R</td><td>Mask or bag-mask; assist breathing if slow or irregular</td></tr>
<tr><td>Ventilation</td><td>In comatose patients, keep PaCO2 in the normal range (about 35 to 45 mm Hg)</td><td>COR 1, LOE B-R</td><td>Avoid over-bagging; usually no blood gas available</td></tr>
<tr><td>Blood pressure</td><td>Prevent hypotension with a MAP of at least 65 mm Hg</td><td>COR 1, LOE B-R</td><td>Saline per physician; vasopressor only if stocked and ordered</td></tr>
<tr><td>12-lead ECG</td><td>As soon as feasible after ROSC</td><td>COR 1, LOE B-NR</td><td>Record and send with the patient; ST elevation changes the destination</td></tr>
<tr><td>Glucose</td><td>Avoiding below 70 and above 180 mg/dL may be reasonable</td><td>COR 2b, LOE B-NR</td><td>Capillary glucose; treat low glucose</td></tr>
<tr><td>Temperature</td><td>Deliberate temperature control (32 to 37.5 &deg;C) for at least 36 hours in patients who do not follow commands</td><td>COR 1, B-R; COR 2a, B-R</td><td>Do not warm actively; avoid fever; continues in hospital</td></tr>
</tbody></table></div>
<p>The guideline also notes that pulse oximetry may miss hypoxemia in patients with darker skin pigmentation (COR 2b, LOE C-LD).[[aha2025_post]] Treat a borderline saturation with care and look at the patient&rsquo;s color, breathing and mental status as well.</p>
<p>For a dialysis patient, add two checks: potassium (the cause or a rebound) and the access (bleeding, a dislodged needle, a clamped and capped catheter). The circuit nurse confirms the circuit is safe and the blood decision was recorded.</p>
{{key:After ROSC: oxygen to 90 to 98%, gentle ventilation, MAP at least 65, a 12-lead ECG, glucose, potassium, the access, and pads still on.}}
"""),
        ("unit", "What a unit can do", "What a freestanding unit can and should not do", """
<p>A hospital-based unit hands over to an intensive care team in minutes. A freestanding unit holds a critically ill patient until the ambulance arrives, sometimes for longer than the arrest itself. Plan for that interval in advance.</p>
{{fig:rl12_unit_limits}}
<div class="table-wrap"><table>
<thead><tr><th>Can do</th><th>Should not do</th></tr></thead>
<tbody>
<tr><td>Oxygen, bag-mask support, airway positioning, suction</td><td>Prolonged manual ventilation without a plan or a second person</td></tr>
<tr><td>Continuous monitoring; repeat blood pressure every few minutes</td><td>Leave the patient unmonitored while waiting for transport</td></tr>
<tr><td>Saline bolus per physician; glucose correction</td><td>Start drugs not stocked, not ordered, or outside protocol</td></tr>
<tr><td>12-lead ECG; potassium and glucose samples</td><td>Delay transfer to wait for laboratory results</td></tr>
<tr><td>Call the receiving hospital early with a summary</td><td>Send the patient without the ECG, the record sheet, or the dialysis facts</td></tr>
<tr><td>Keep the access safe for drugs and for the next dialysis</td><td>Restart dialysis without the attending nephrologist</td></tr>
</tbody></table></div>
<p>Restarting dialysis after ROSC is tempting when potassium or fluid overload caused the arrest. Card 1 is clear: do not restart dialysis unless the attending nephrologist says so. The ERC notes that dialysis may be needed early after ROSC,[[erc2025_special]] but a patient with a pressure of 84/50 who does not follow commands needs monitored care first, and the decision of where and when dialysis resumes belongs to the attending nephrologist and the receiving team. Restarting a circuit in an unstable patient can drop the pressure and cause re-arrest.</p>
{{key:Stabilize, monitor, document and transfer. Dialysis restarts only on the attending nephrologist&rsquo;s decision, usually in the receiving hospital.}}
"""),
        ("handover", "Handover", "A handover the ambulance can use", """
<p>The receiving team needs two kinds of facts: what happened in the arrest, and what was happening on the dialysis machine. The second kind is the one most often lost.</p>
{{fig:rl12_handover}}
{{flow:Handover in order (about 60 seconds)|Identity and status::Name, age, dialysis vintage, access type, code status, allergies.|The event::Time of collapse, witnessed or not, first rhythm, time to first compression and first shock.|Treatment::Shocks (number, energy), drugs (name, dose, times), airway, duration of CPR, time of ROSC.|The dialysis facts::Hours on the machine, fluid removed, whether the blood was returned, last potassium and its time, dialysis fluid potassium and calcium, heparin given.|Now::Current pressure, rhythm, saturation, glucose, mental status, the 12-lead ECG, and what has been asked of the attending nephrologist.}}
<p>Send the recorder&rsquo;s sheet, the ECG, the dialysis treatment sheet, and the medication list. Tell the family as soon as a staff member is free, with the leader or charge nurse, in plain words. Then document, restock the cart, check the defibrillator, and hold the debrief (Module 13).</p>
{{key:Hand over the arrest and the dialysis together: time on the machine, fluid removed, blood returned or not, and the last potassium travel with the patient.}}
{{call:After any ROSC: keep the pads on, call the receiving hospital and the attending nephrologist, and follow your unit protocol for transfer. Never restart dialysis without the attending nephrologist&rsquo;s explicit decision.}}
"""),
    ],
    "debrief": ["""
<p><strong>Confirm and stabilize.</strong> A palpable carotid pulse with a measurable pressure (84/50) is ROSC; the pads stay on. In the next ten minutes: oxygen titrated to a saturation of 90 to 98% (89% is too low; support his breathing with the bag-mask if it stays irregular), gentle ventilation, a saline bolus per the physician to bring the MAP (about 61 now) to at least 65, a 12-lead ECG, capillary glucose, and a repeat potassium sample. The access is checked; the catheter or needles are safe and clamped.</p>
<p><strong>Restart dialysis?</strong> No, not without the attending nephrologist. He is hypotensive and not following commands; he needs monitored care, and the decision where and when dialysis resumes belongs to the attending and the receiving team. His morning potassium was 5.1 and 2.6 L had been removed, so volume depletion is as likely a contributor as potassium.</p>
<p><strong>Handover.</strong> Seventy, on dialysis, access type; collapse at 2:24 p.m., witnessed, first rhythm, compressions within seconds; two shocks with energies, two doses of epinephrine with times; ROSC at 2:35; three hours on the machine, 2.6 L removed, blood returned at the start; potassium 5.1 this morning; current pressure, rhythm, saturation, glucose; ECG attached; attending nephrologist informed. The recorder&rsquo;s sheet and dialysis sheet go with him.</p>
"""],
    "skills": {"title": "Post-ROSC care and handover",
               "intro": "Continue a megacode past ROSC: stabilize for ten simulated minutes and give a handover to a facilitator playing the ambulance crew.",
               "items": [
                   ("Confirms ROSC by a definite pulse and blood pressure, and keeps the pads on.", True),
                   ("Titrates oxygen to a saturation of 90 to 98% and avoids over-ventilation.", False),
                   ("Targets a MAP of at least 65 mm Hg with fluids or drugs per physician order.", False),
                   ("Records a 12-lead ECG and checks glucose and potassium.", False),
                   ("Recognizes re-arrest and resumes compressions within seconds.", True),
                   ("Does not restart dialysis without the attending nephrologist.", True),
                   ("Gives a structured handover including time on machine, fluid removed, blood decision and last potassium.", True),
               ],
               "placement": "Draft your unit&rsquo;s one-page post-ROSC handover sheet and agree it with the nearest receiving emergency room."},
    "terms": [("ROSC", "A definite pulse and measurable blood pressure after arrest."),
              ("Re-arrest", "Loss of circulation again after ROSC."),
              ("MAP", "Mean arterial pressure, the average pressure driving organ perfusion."),
              ("Temperature control", "Deliberate management of body temperature after arrest."),
              ("Post-cardiac arrest syndrome", "Brain injury, heart dysfunction and inflammation after arrest."),
              ("Dialysis vintage", "How long a patient has been on dialysis.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-4"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["12"])
