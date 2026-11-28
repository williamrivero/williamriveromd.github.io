# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 04: BLS at the Dialysis Chair. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse giving chest compressions to a man in a fully flattened dialysis recliner while a second nurse seals a bag-valve-mask.",
    "objectives": [
        "Flatten a dialysis recliner and start compressions within seconds, using a firm surface only when it causes no delay.",
        "Deliver compressions at 100 to 120 a minute and a depth of 5 to 6 cm, with full recoil and pauses under 10 seconds.",
        "Apply the defibrillator pads at the chair and resume compressions immediately after a shock.",
        "Ventilate with a bag-valve-mask using a two-person technique, giving just enough volume for visible chest rise.",
        "Relieve severe choking in an adult with the 2025 sequence of back blows and abdominal thrusts.",
    ],
    "big": """
{{plain:During cardiac arrest, compressions are the heart. Each push squeezes the heart between the breastbone and the spine and sends a small amount of blood to the brain and the heart muscle. Each time you stop, that flow falls to zero almost at once, and it takes several compressions to build it back up.}}
<p>The picture has a limit. Compressions do not simply squeeze the heart like a hand on a sponge; they also change the pressure in the whole chest, which moves blood forward. The practical lesson is the same. Blood flow during CPR depends on depth, rate, full recoil (the chest must refill), and above all on not stopping. Most of the quality of CPR is lost in pauses: for the pulse check, for the machine, for the ventilation, for the next person to take over.</p>
<p>This module is for everyone on the floor: nurses, physicians, technicians, assistants and support staff. BLS is the part of resuscitation that anyone can start, and in dialysis clinics it is the part most strongly associated with survival.[[pun2019]]</p>
{{cards:Key terms for this module|Chest compression fraction (CCF)::The share of the arrest time spent compressing.|Recoil::Letting the chest rise fully between compressions so the heart can refill.|Bag-valve-mask (BVM)::A self-inflating bag and mask used to give breaths.|Automated external defibrillator (AED)::A defibrillator that analyzes the rhythm and prompts a shock.|Two-person ventilation::One person seals the mask with both hands; another squeezes the bag.|Severe choking::The person cannot speak, cough or breathe because of an obstruction.}}
""",
    "case": {"title": "The chair that would not recline", "html": """
<p>At 7:05 a.m., Mrs. Lorna Castillo, 64, collapses forward in her chair at a dialysis unit in Quezon City, ten minutes after connection. Nurse assistant Mr. Jomar Villanueva is passing the station. She does not answer, she is gasping, and he feels no pulse.</p>
<p>He shouts for help and pulls the recliner lever. The backrest goes only halfway down; the mechanism sticks. Mrs. Castillo weighs about 85 kg. Two nurses arrive with the crash cart 40 seconds later. One says, &ldquo;Let us move her to the floor.&rdquo;</p>
""", "questions": ["What should Mr. Villanueva do in the first 20 seconds?",
                  "Should the team move Mrs. Castillo to the floor? What would decide it?",
                  "When the defibrillator arrives, what happens to compressions?"]},
    "sections": [
        ("start", "Flatten and start", "Flatten the recliner, and start", """
<p>Dialysis recliners are designed for a sitting patient, not for CPR. Most can be tilted back flat or into a head-down position with a lever or a button; some have a CPR release. Know your unit&rsquo;s chairs before you need them, because the AHA preference for a firm surface is conditional: a firm surface, supine when feasible, is preferred <em>if it does not delay compressions</em> (COR 2a, LOE C-LD). For adults with obesity, consider how moving the patient to a firm surface may delay compressions (COR 2a, LOE C-LD).[[aha2025_bls]]</p>
{{fig:rl04_flatten}}
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What to do</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Recliner flattens normally</td><td>Flatten fully; start compressions; slide a backboard under when a second person is free</td><td>A firm, flat surface with no delay</td></tr>
<tr><td>Recliner sticks halfway</td><td>Start compressions in the chair as flat as it goes; a second person works the mechanism or prepares to move</td><td>Compressions now; a better surface later</td></tr>
<tr><td>Chair cannot be flattened at all, patient light</td><td>Move to the floor with enough hands, after clamping per the circuit nurse</td><td>Floor is firm; brief interruption</td></tr>
<tr><td>Heavy patient, chair partly flat</td><td>Compress where the patient is; reposition only with enough people and a plan</td><td>Moving a heavy patient can cost a minute of no flow</td></tr>
</tbody></table></div>
<p>Moving a patient who is still connected to the circuit can pull out the needles or the catheter. Before any move, the circuit nurse stops the blood pump and clamps, or disconnects per protocol (Module 7). Kneeling on the chair edge or using a step stool gives a short compressor the height to lock the elbows.</p>
{{key:Compressions start where the patient is. Improve the surface only when it costs no time, and never move a connected patient until the circuit nurse says the lines are safe.}}
"""),
        ("quality", "High-quality compressions", "Compressions that move blood", """
<p>The 2025 AHA adult BLS guideline sets the targets.[[aha2025_bls]]</p>
{{fig:rl04_compression}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>AHA 2025 recommendation</th><th>Grade</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Rate</td><td>100 to 120 a minute</td><td>COR 2a, LOE B-NR</td><td>Too slow moves too little blood; too fast leaves no time to refill</td></tr>
<tr><td>Depth</td><td>At least 5 cm; avoid more than 6 cm</td><td>COR 1, LOE B-NR</td><td>Shallow compressions move little blood; very deep ones cause injury</td></tr>
<tr><td>Recoil</td><td>Allow full chest recoil; do not lean</td><td>COR 2a, LOE C-LD</td><td>The heart refills during recoil</td></tr>
<tr><td>Compression fraction</td><td>At least 60% may be reasonable</td><td>COR 2b, LOE C-LD</td><td>Every pause drops flow to near zero</td></tr>
<tr><td>Pulse check</td><td>No more than 10 seconds</td><td>COR 1, LOE C-LD</td><td>Long checks are long pauses</td></tr>
<tr><td>Ratio (no advanced airway)</td><td>30 compressions to 2 breaths</td><td>COR 2a, LOE B-NR</td><td>Balances oxygen and flow</td></tr>
</tbody></table></div>
<p>Compressors tire within about two minutes, and their depth falls before they notice. Swap at every two-minute rhythm check, or sooner if the compressor is tiring, with the next person ready beside the chair so the swap takes a second or two. The recorder or a feedback device calls out the rate. The 60% fraction in the guideline is a floor, not a goal; in this course&rsquo;s drills the team aims higher, which is an Academy teaching choice, not a guideline number. The <a href="../guides/calc-resuscitation-lab-toolkit.html#tool-1">CPR interruption analyzer</a> computes the fraction from timed pauses.</p>
{{key:Push 5 to 6 cm deep, 100 to 120 a minute, let the chest rise fully, swap every two minutes, and protect every second of compression time.}}
"""),
        ("defib", "Defibrillator at the chair", "The defibrillator at the chair", """
<p>Compressions continue until the defibrillator or AED is applied (COR 1, LOE C-LD). Pads go anterolateral (right upper chest and left side under the armpit) or anteroposterior (front and back) (COR 2a, LOE C-LD), placed clear of a chest-wall catheter exit site and any wet dressing. When a monitored patient goes into VF with pads already on, defibrillate immediately (COR 2a, LOE C-LD). After a shock, resume compressions immediately rather than pausing to check the rhythm (COR 2a, LOE B-R), and keep the pauses before and after a shock as short as possible (COR 1, LOE C-LD).[[aha2025_bls]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Who</th><th>What is said</th></tr></thead>
<tbody>
<tr><td>Pads on while compressions continue</td><td>Defibrillator person</td><td>&ldquo;Pads on.&rdquo;</td></tr>
<tr><td>Analyze (AED) or rhythm check (manual), under 10 seconds</td><td>Leader</td><td>&ldquo;Stop compressions. Rhythm check.&rdquo;</td></tr>
<tr><td>If shockable: compress again while charging (manual)</td><td>Compressor</td><td>&ldquo;Charging, continue compressions.&rdquo;</td></tr>
<tr><td>Clear and shock</td><td>Defibrillator person</td><td>&ldquo;Everyone clear: patient, chair, lines, machine. Shocking.&rdquo;</td></tr>
<tr><td>Resume at once</td><td>Compressor</td><td>&ldquo;Compressions.&rdquo;</td></tr>
</tbody></table></div>
<p>An AED is designed for any trained staff member, including a technician or assistant. In a dialysis unit, the specific hazards are fluid on the chair or floor and hands on the blood lines or the machine during a shock (Module 7).</p>
{{key:Compress until the pads are on, pause only to analyze and shock, and compress again immediately after the shock.}}
"""),
        ("airway", "Breaths and choking", "Bag-mask breaths, oxygen, and choking", """
<p>In a dialysis unit without an anesthetist, the bag-valve-mask is the airway. It works well with two people: one holds the mask with both hands, lifting the jaw into the mask; the other squeezes the bag slowly over about one second, just enough to see the chest rise. Ventilate with visible chest rise (COR 2a, LOE C-LD).[[aha2025_bls]] Large, fast breaths push air into the stomach and raise chest pressure, which reduces blood returning to the heart.</p>
{{fig:rl04_bvm}}
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Likely cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Chest does not rise</td><td>Poor seal or tongue blocking the throat</td><td>Two-hand seal; head tilt and jaw lift; oral airway in an unresponsive patient</td></tr>
<tr><td>Stomach swells</td><td>Breaths too large or too fast</td><td>Smaller, slower breaths</td></tr>
<tr><td>Vomit in the airway</td><td>Common in arrest</td><td>Turn the head if safe, suction, continue</td></tr>
<tr><td>Dentures loose</td><td>Poor fit</td><td>Leave well-fitting dentures in for a seal; remove loose ones</td></tr>
</tbody></table></div>
<h3>Choking</h3>
<p>Choking happens in dialysis units too: at meal times, with hard candy for a dry mouth, or with a tablet. The 2025 AHA sequence for an adult with severe foreign-body airway obstruction is repeated cycles of five back blows followed by five abdominal thrusts until the object comes out or the person becomes unresponsive (COR 1, LOE B-NR). If you cannot encircle the abdomen, or in late pregnancy, use five back blows followed by five chest thrusts. If the person becomes unresponsive, start CPR with compressions. Do not perform blind finger sweeps (COR 3: Harm, LOE C-LD).[[aha2025_bls]] A patient connected to a circuit is choking in a chair: stop the blood pump and clamp before standing them up for thrusts.</p>
{{fig:rl04_choking}}
{{key:Two people, two hands on the mask, just enough breath to see the chest rise. For choking: five back blows, five abdominal thrusts, repeat.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first 20 seconds.</strong> Mr. Villanueva has recognized arrest correctly: unresponsive, gasping, no pulse. He shouts for help and starts compressions in the chair as flat as it goes. He does not wait for the chair to work.</p>
<p><strong>The floor?</strong> Mrs. Castillo weighs 85 kg and is still connected. Moving her now would interrupt compressions and risk pulling out the needles. The better plan: keep compressing in the half-flat chair, have one nurse work the lever or the CPR release, and slide a backboard behind her if the chair stays upright. If the team decides to move her, the circuit nurse first stops the pump and clamps, four people lift on a count, and compressions restart within seconds on the floor. The AHA&rsquo;s firm-surface preference applies only if it does not delay compressions.</p>
<p><strong>When the defibrillator arrives.</strong> Compressions continue while the pads go on. The team pauses only to analyze, shocks if advised with everyone clear of the patient, chair, lines and machine, and resumes compressions immediately after the shock.</p>
<p>The stuck lever is a system finding. After the event, the chair is tagged out, and every recliner&rsquo;s CPR position is checked in the next morning&rsquo;s round.</p>
"""],
    "skills": {"title": "BLS at the dialysis chair",
               "intro": "On a manikin in a dialysis recliner, with a feedback device if available, perform two minutes of CPR and an AED sequence while a supervisor observes.",
               "items": [
                   ("Recognizes arrest (unresponsive, not breathing normally, no definite pulse in 10 seconds) and shouts for help.", True),
                   ("Flattens the recliner or starts compressions where the patient is, without delay.", True),
                   ("Compresses at 100 to 120 a minute, 5 to 6 cm deep, with full recoil.", True),
                   ("Keeps every pause under 10 seconds and swaps compressors at two minutes.", False),
                   ("Applies pads in the correct positions, clear of the catheter exit site and wet dressings.", False),
                   ("Calls &ldquo;clear&rdquo; for patient, chair, lines and machine before the shock, and resumes compressions immediately.", True),
                   ("Ventilates with a two-person bag-mask technique with visible chest rise.", False),
                   ("Demonstrates the adult choking sequence on a trainer.", False),
               ],
               "placement": "Test the CPR position of every recliner in your unit with the biomedical technician and tag any that fail."},
    "terms": [("Recoil", "Letting the chest rise fully between compressions."),
              ("Compression fraction", "The share of arrest time spent compressing."),
              ("Anterolateral pads", "One pad below the right collarbone, one on the left side below the armpit."),
              ("Anteroposterior pads", "One pad on the front of the chest, one on the back."),
              ("Oral airway", "A curved plastic airway placed in the mouth of an unresponsive patient."),
              ("Back blows", "Firm blows between the shoulder blades to dislodge an obstruction.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-1"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["04"])
