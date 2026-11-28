# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 05: Adult Cardiac Arrest: Shockable and Nonshockable. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician holding defibrillator controls while the team steps back from a flattened dialysis chair, hands raised.",
    "objectives": [
        "Follow the shockable (VF and pulseless VT) and nonshockable (asystole and PEA) paths of adult cardiac arrest within the two-minute cycle.",
        "Time epinephrine correctly for each path and state its dose and interval, with the AHA grade.",
        "Explain when amiodarone or lidocaine may be considered, and why routine calcium, bicarbonate and pacing are not recommended in arrest.",
        "Use end-tidal carbon dioxide to judge CPR quality and to detect a possible return of circulation.",
        "Search for the reversible causes most common in dialysis patients, starting with potassium, volume and the circuit.",
    ],
    "big": """
{{plain:Think of the arrested heart in two ways. In ventricular fibrillation, the heart is like a stadium where every person is clapping at a different time: lots of noise, no rhythm, no pumping. A shock silences the whole stadium at once so one leader can start a steady beat again. In asystole and PEA, there is either silence or a steady beat with no one actually moving. A shock has nothing to fix; you need to find out why the pump is empty or stopped.}}
<p>The picture has a limit. Even a successful shock leaves a stunned heart that pumps weakly for a while, which is why compressions restart immediately after the shock instead of waiting to see. And in PEA the &ldquo;why&rdquo; matters more than the rhythm: in a dialysis patient the answer is often potassium, an empty circulation after fluid removal, bleeding from the access, air, or blood around the heart.</p>
<p>This module teaches the adult arrest algorithm as two paths that share one engine: high-quality CPR in two-minute cycles, a brief rhythm check, and a constant search for the cause.</p>
{{cards:Key terms for this module|Ventricular fibrillation (VF)::Chaotic ventricular electrical activity with no pumping.|Pulseless ventricular tachycardia (pVT)::A fast ventricular rhythm with no pulse; treated like VF.|Asystole::No electrical activity.|Pulseless electrical activity (PEA)::An organized rhythm with no pulse.|Epinephrine::A drug that constricts blood vessels and raises the pressure that perfuses the heart and brain during CPR.|End-tidal carbon dioxide (ETCO2)::Carbon dioxide at the end of each breath; it rises with blood flow.}}
""",
    "case": {"title": "Collapse at Station 7", "html": """
<p>At 9:40 a.m. on a Tuesday, Mr. Arnel Gutierrez, 61, two hours into his session at a freestanding unit in Pasig, suddenly slumps. Nurse Ms. Camille Ortiz finds him unresponsive, not breathing, with no pulse. The physician-on-duty stepped out ten minutes ago to the pharmacy next door and is coming back. The ACLS-certified nurse, Mr. Gab Fernandez, takes the lead.</p>
<p>Compressions start within 15 seconds. The circuit nurse stops fluid removal. Pads go on at 40 seconds. The screen shows a chaotic, irregular trace with no organized complexes.</p>
""", "questions": ["What happens at the first rhythm check, and what is said?",
                  "When is epinephrine first given on this path, and how much?",
                  "If the rhythm becomes organized at the third check, what decides the next step?"]},
    "sections": [
        ("paths", "Two paths", "One rhythm check, two paths", """
<p>Every adult arrest runs on the same engine: high-quality CPR, a rhythm check every two minutes that lasts under 10 seconds, and a decision at each check. The rhythm at the check chooses the path.</p>
{{fig:rl05_two_paths}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Shockable: VF and pulseless VT</th><th>Nonshockable: asystole and PEA</th></tr></thead>
<tbody>
<tr><td>At the rhythm check</td><td>Shock, then 2 minutes of CPR at once</td><td>No shock; 2 minutes of CPR</td></tr>
<tr><td>Epinephrine</td><td>After initial defibrillation attempts fail (COR 2a, LOE B-NR)</td><td>As soon as feasible (COR 2a, LOE B-NR)</td></tr>
<tr><td>Antiarrhythmic</td><td>Amiodarone or lidocaine may be considered if VF/pVT persists after shocks (COR 2b, LOE B-R)</td><td>Not indicated</td></tr>
<tr><td>Main thinking</td><td>Shock early and often enough; minimize pauses</td><td>Find and treat the cause</td></tr>
</tbody></table></div>
<p>The 2025 guideline recommends biphasic defibrillators over monophasic (COR 2a, LOE B-R), single shocks rather than stacked shocks (COR 2a, LOE B-NR), and the manufacturer&rsquo;s recommended energy; if it is unknown, the maximum dose may be considered (COR 2b, LOE C-LD). For VF that persists after three or more shocks, the usefulness of changing pad position (vector change) or double sequential defibrillation has not been established (COR 2b, LOE B-R).[[aha2025_als]] Know your unit&rsquo;s device and its first energy before the day you need it.</p>
{{key:VF and pulseless VT get a shock first. Asystole and PEA get epinephrine as soon as feasible. Both get two minutes of uninterrupted CPR between checks.}}
"""),
        ("drugs", "Drugs and access", "Epinephrine, antiarrhythmics, and the drugs not to give routinely", """
<p>Epinephrine constricts peripheral blood vessels, which raises the pressure in the aorta during compressions and pushes more blood into the coronary and cerebral arteries. The 2025 guideline recommends epinephrine for adults in cardiac arrest (COR 1, LOE B-R); 1 mg every 3 to 5 minutes is reasonable (COR 2a, LOE B-R); high-dose epinephrine is not recommended for routine use (COR 3: No Benefit, LOE B-R).[[aha2025_als]] In practice, every other two-minute cycle keeps the interval within 3 to 5 minutes; the recorder calls the time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Drug</th><th>Algorithm dose (adult)</th><th>When</th><th>2025 grade</th></tr></thead>
<tbody>
<tr><td>Epinephrine intravenous (IV) or intraosseous (IO)</td><td>1 mg every 3 to 5 minutes</td><td>Nonshockable: as soon as feasible. Shockable: after initial shocks fail</td><td>COR 1 (give); COR 2a (dose and timing)</td></tr>
<tr><td>Amiodarone IV or IO</td><td>300 mg, then 150 mg</td><td>VF/pVT persisting after shocks</td><td>COR 2b, LOE B-R (amiodarone or lidocaine)</td></tr>
<tr><td>Lidocaine IV or IO (alternative)</td><td>1 to 1.5 mg/kg, then 0.5 to 0.75 mg/kg</td><td>Same</td><td>COR 2b, LOE B-R</td></tr>
<tr><td>Calcium, routine</td><td>Not given routinely</td><td>Only for a specific cause (for example, suspected hyperkalemia, per protocol)</td><td>Routine use: COR 3, No Benefit</td></tr>
<tr><td>Sodium bicarbonate, routine</td><td>Not given routinely</td><td>Only for a specific cause, per protocol</td><td>Routine use: COR 3, No Benefit</td></tr>
</tbody></table></div>
<p>For access, the guideline recommends attempting intravenous access first (COR 1, LOE A) and intraosseous access if IV attempts fail or are not feasible (COR 2a, LOE A).[[aha2025_als]] A dialysis patient often has access already: a working catheter or a needle in the fistula. Module 7 explains how to use it safely, including aspirating the catheter lock before giving drugs. Routine electrical pacing during established cardiac arrest is not recommended (COR 3: No Benefit, LOE B-R).[[aha2025_als]]</p>
<p>The doses here are those printed on the 2025 adult cardiac arrest algorithm, quoted so you can recognize them. Give drugs only within your license and your unit&rsquo;s approved protocol and stock.</p>
{{key:Epinephrine 1 mg every 3 to 5 minutes: as soon as feasible in nonshockable arrest, after the first failed shocks in shockable arrest. No routine calcium or bicarbonate unless a specific cause calls for it.}}
"""),
        ("cycle", "The cycle and ETCO2", "Running the two-minute cycle, and reading carbon dioxide", """
<p>A well-run arrest has a rhythm of its own. The leader keeps time with the recorder and announces each step a few seconds before it is due, so the next compressor, the defibrillator, and the drug are ready.</p>
{{fig:rl05_cycle}}
{{flow:One two-minute cycle, shockable path|0:00::Compressions running. Leader: &ldquo;Next check in two minutes. Draw up epinephrine for after the second shock.&rdquo;|1:45::Next compressor ready beside the chair. Defibrillator person ready to charge.|2:00::&ldquo;Stop. Rhythm check.&rdquo; Under 10 seconds. If VF: &ldquo;Charging, continue compressions.&rdquo;|2:05::&ldquo;Everyone clear: patient, chair, lines, machine.&rdquo; Shock. &ldquo;Compressions.&rdquo; New compressor starts.|2:10::Drug given if due; recorder writes the time; leader reviews reversible causes aloud.}}
<p>End-tidal carbon dioxide reflects how much blood the compressions are moving through the lungs. Monitoring physiological parameters such as ETCO2 may be reasonable to monitor and optimize CPR quality (COR 2b, LOE C-LD), and an abrupt increase in ETCO2 may be used to detect a return of spontaneous circulation (COR 2b, LOE B-NR).[[aha2025_als]] Many freestanding dialysis units do not have capnography; where you do, a falling value tells the leader to check compressor fatigue, and a sudden rise tells the team to check for a pulse at the next pause.</p>
{{fig:rl05_etco2}}
{{key:The leader runs the clock: announce every check and every drug a few seconds early, swap compressors at each check, and use ETCO2 when you have it.}}
"""),
        ("causes", "Reversible causes", "The reversible causes that dominate in dialysis", """
<p>Every arrest has a cause, and in nonshockable arrest finding it is often the only way back. General lists of reversible causes apply to dialysis patients, but the order of likelihood is different. Ask the questions below aloud during each cycle.</p>
{{fig:rl05_reversible}}
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Why in dialysis</th><th>Clue</th><th>Action during CPR</th></tr></thead>
<tbody>
<tr><td>Hyperkalemia</td><td>Missed session, long gap, diet, hemolysis</td><td>Monday, early in the session, slow wide rhythm before arrest</td><td>Per unit protocol (Module 8); plan dialysis after return of spontaneous circulation (ROSC)</td></tr>
<tr><td>Hypovolemia</td><td>Fluid removal, blood loss</td><td>Late in the session, falling pressure before arrest</td><td>Stop fluid removal; saline through the circuit or IV</td></tr>
<tr><td>Hemorrhage</td><td>Needle dislodgement, line separation</td><td>Wet blanket, blood on the floor</td><td>Lift the blanket; clamp; press</td></tr>
<tr><td>Air embolism</td><td>Air in the venous line or an open catheter</td><td>Foam in the line, air alarm, sudden collapse</td><td>Clamp; do not return the blood (Module 7)</td></tr>
<tr><td>Hypokalemia</td><td>Low-potassium bath, late in the session</td><td>Arrest late in the session or after</td><td>Check potassium; physician decides</td></tr>
<tr><td>Hypocalcemia</td><td>Low-calcium bath, citrate</td><td>Long QT before arrest</td><td>Check calcium; physician decides</td></tr>
<tr><td>Tamponade</td><td>Uremic or dialysis-associated pericardial effusion</td><td>Missed sessions, chest pain, low pressure before arrest</td><td>Ultrasound if available; emergency transfer</td></tr>
<tr><td>Hypoglycemia</td><td>Insulin, poor intake, glucose-free bath</td><td>Diabetes, confusion before collapse</td><td>Check glucose; treat per protocol</td></tr>
<tr><td>Hypoxia, acidosis, toxins, thrombosis, tension pneumothorax</td><td>As in any patient</td><td>History, examination</td><td>Ventilate well; treat the specific cause</td></tr>
</tbody></table></div>
<p>Hypokalemia appears in the list because arrest late in a session is associated with low-potassium baths in observational studies, not because it has been proven to cause each event.[[karnik2001]][[pun2011]] The timing of the arrest in the session is the clue: early suggests high potassium, late suggests volume, low potassium or low calcium.</p>
{{key:In dialysis, ask about potassium, volume, bleeding, air and the session clock first. Early arrests point to high potassium; late ones to volume and low electrolytes.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first rhythm check.</strong> A chaotic trace with no organized complexes in an unresponsive, pulseless patient is VF. Mr. Fernandez says: &ldquo;VF. Charging, continue compressions. Everyone clear: patient, chair, lines, machine. Shock.&rdquo; Compressions resume at once after the shock. The runner has already called the ambulance and the physician-on-duty.</p>
<p><strong>Epinephrine.</strong> On the shockable path, epinephrine 1 mg IV is given after initial defibrillation attempts fail; in the AHA algorithm that is after the second shock, then every 3 to 5 minutes. If VF persists after further shocks, amiodarone 300 mg or lidocaine may be considered, per protocol. Drugs go through the dialysis access once the circuit nurse has made it safe (Module 7).</p>
<p><strong>An organized rhythm.</strong> At the third check the screen shows organized complexes. The leader feels for a definite pulse within 10 seconds. A pulse with a measurable pressure is ROSC: move to post-ROSC care (Module 12). No pulse is PEA: continue compressions on the nonshockable path, give epinephrine every 3 to 5 minutes, and search for causes, starting with potassium (he was two hours in), volume, and bleeding at the access.</p>
"""],
    "skills": {"title": "Leading adult cardiac arrest",
               "intro": "Lead a shockable and a nonshockable megacode on a manikin and simulator while a supervisor observes.",
               "items": [
                   ("Runs two-minute cycles with rhythm checks under 10 seconds.", True),
                   ("Shocks VF or pulseless VT promptly with a clear safety call, and resumes compressions immediately.", True),
                   ("Times epinephrine correctly for the shockable and nonshockable paths, with 3 to 5 minute intervals.", True),
                   ("Considers amiodarone or lidocaine for VF/pVT persisting after shocks, per protocol.", False),
                   ("Does not order routine calcium, bicarbonate or pacing without a specific indication.", False),
                   ("States at least four dialysis-weighted reversible causes and acts on the clues.", False),
                   ("Uses ETCO2, when available, to judge CPR quality and possible ROSC.", False),
                   ("Confirms ROSC by a definite pulse and pressure, not by the rhythm alone.", True),
               ],
               "placement": "Observe or take part in one quarterly megacode; afterward, list the times of first shock and first epinephrine from the recorder&rsquo;s sheet."},
    "terms": [("Biphasic defibrillator", "A defibrillator whose current flows one way then reverses; preferred over monophasic."),
              ("Stacked shocks", "Several shocks in a row without compressions between them; not preferred."),
              ("Vector change", "Moving the pads to a different position for refractory VF; usefulness not established."),
              ("Double sequential defibrillation", "Two defibrillators shocking almost together; usefulness not established."),
              ("Intraosseous access", "A needle into the bone marrow used when no vein is available."),
              ("Tamponade", "Fluid around the heart that stops it filling.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": ["calc-resuscitation-lab-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
