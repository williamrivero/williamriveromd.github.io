# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 03: Recognizing the Right Algorithm. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse feeling the neck pulse of a pale man in a dialysis chair while looking at the bedside monitor.",
    "objectives": [
        "Distinguish cardiac arrest, respiratory arrest, and deterioration with a pulse, using breathing and a definite pulse.",
        "Explain why a rhythm strip alone cannot establish a pulse, perfusion, or stability, and confirm each at the patient.",
        "Separate shockable from nonshockable arrest, and bradycardia or tachycardia with a pulse from pulseless rhythms.",
        "Tell pre-arrest hyperkalemia from hyperkalemic cardiac arrest, and describe the typical potassium ECG changes and their limits.",
        "Choose the adult or pediatric pathway, and recognize when an evolving patient needs a different algorithm.",
    ],
    "big": """
{{plain:Think of the monitor as a weather radar and the patient as the sky above you. The radar shows patterns quickly, but it cannot tell you whether it is actually raining on your head. You look up. In resuscitation, looking up means touching the patient: is there breathing, is there a pulse, is the skin warm, is the person answering you?}}
<p>The picture has a limit. A radar at least measures something real in the sky. A monitor measures only electricity. Electricity and pumping usually travel together, but in pulseless electrical activity (PEA) the wiring fires normally while the pump moves no blood, and in some low-output states the rhythm looks fine while the brain is starving. Recognition therefore always combines the strip with the patient.</p>
<p>Recognition is a separate competency from knowing the algorithms. A nurse can recite every step of the arrest algorithm and still lose a minute because the patient &ldquo;looked like another low blood pressure.&rdquo; This module trains the first seconds: which algorithm are we in?</p>
{{cards:Key terms for this module|Respiratory arrest::No breathing or only gasping, with a definite pulse. The heart still pumps; oxygen is running out.|Pulseless electrical activity (PEA)::An organized rhythm on the monitor with no palpable pulse.|Asystole::No electrical activity; a flat line confirmed in more than one lead and with the gain turned up.|Return of spontaneous circulation (ROSC)::A definite pulse and blood pressure after arrest.|Shockable rhythm::Ventricular fibrillation (VF) or pulseless ventricular tachycardia (pVT).|Peaked T wave::A tall, narrow, symmetrical T wave, one possible sign of high potassium.}}
""",
    "case": {"title": "&ldquo;It looks like another low BP&rdquo;", "html": """
<p>Mr. Danilo Reyes, 59, dialyzes three times a week in a freestanding unit in Davao City. He often has low blood pressure in the last hour. At 3:20 p.m., near the end of his session, nurse Ms. Jen Torres hears the blood pressure alarm: 72/40 mm Hg. Mr. Reyes is slumped in the chair. His eyes are half open. He breathes slowly, with a snoring sound every few seconds.</p>
<p>A colleague calls out, &ldquo;Another low BP. Legs up, saline bolus?&rdquo; The bedside monitor shows a regular, narrow rhythm at 64 per minute.</p>
""", "questions": ["Which algorithm is Mr. Reyes in? What would you check first, and how quickly?",
                  "What does the regular rhythm on the monitor tell you, and what does it not tell you?",
                  "What should Ms. Torres say in the next ten seconds?"]},
    "sections": [
        ("states", "Three states", "Arrest, respiratory arrest, or getting worse with a pulse", """
<p>From the doorway, three very different emergencies look alike: a slumped, gray patient who does not answer. Two questions at the patient separate them in ten seconds: is the breathing normal, and is there a definite pulse? The AHA recommends checking breathing and pulse together, and limiting the pulse check to no more than 10 seconds (COR 1, LOE C-LD).[[aha2025_bls]]</p>
{{fig:rl03_three_states}}
<div class="table-wrap"><table>
<thead><tr><th>State</th><th>Breathing</th><th>Pulse</th><th>Algorithm</th><th>First move</th></tr></thead>
<tbody>
<tr><td>Deterioration with circulation</td><td>Present (may be fast or labored)</td><td>Definite</td><td>The cause: hypotension, bradycardia or tachycardia, hypoglycemia, reaction</td><td>Lay flat, monitor, call; use the matching card</td></tr>
<tr><td>Respiratory arrest</td><td>Absent or gasping</td><td>Definite</td><td>Ventilation with a pulse</td><td>Open the airway; one breath every 6 seconds; recheck the pulse every 2 minutes</td></tr>
<tr><td>Cardiac arrest</td><td>Absent or gasping</td><td>None definite</td><td>Cardiac arrest</td><td>Compressions now</td></tr>
</tbody></table></div>
<p>For an adult in respiratory arrest with a pulse, the AHA suggests one breath every 6 seconds (10 per minute) (COR 2a, LOE C-LD).[[aha2025_bls]] The pulse is rechecked often, because respiratory arrest becomes cardiac arrest within minutes if oxygen does not arrive.</p>
<p>Gasping is the trap. Agonal breathing is a brainstem reflex in a brain without blood flow. It is irregular, slow, and sometimes noisy, and staff who see the chest move often decide the patient is breathing. Treat gasping as not breathing.</p>
{{key:Breathing normally and a definite pulse: two checks, ten seconds, at the patient. Gasping counts as not breathing.}}
"""),
        ("strip", "Strip and patient", "A rhythm strip cannot feel a pulse", """
<p>The monitor shows electrical activity. It does not show whether the heart pumps, whether the brain is perfused, or whether the pressure is adequate. The same organized narrow rhythm at 64 per minute can belong to a patient talking comfortably, a patient in shock, or a patient in PEA.</p>
{{fig:rl03_rhythm_vs_pulse}}
<div class="table-wrap"><table>
<thead><tr><th>On the monitor</th><th>Possible patient states</th><th>What decides</th></tr></thead>
<tbody>
<tr><td>Organized rhythm, normal rate</td><td>Healthy circulation; shock; PEA; ROSC</td><td>A definite pulse, blood pressure, responsiveness</td></tr>
<tr><td>Wide, fast, regular rhythm</td><td>VT with a pulse (stable or unstable); pulseless VT</td><td>A pulse, then the five signs of instability</td></tr>
<tr><td>Chaotic, no organized complexes</td><td>VF; artifact from a loose lead or patient movement</td><td>The patient: VF is always pulseless and unresponsive</td></tr>
<tr><td>Flat line</td><td>Asystole; a disconnected lead; gain set too low</td><td>Check leads, gain, and a second lead</td></tr>
<tr><td>Very slow rhythm</td><td>Bradycardia with a pulse (stable or unstable); arrest</td><td>A pulse and perfusion</td></tr>
</tbody></table></div>
<p>Two errors follow from treating the strip. The first is the case above: a regular rhythm reassures the team while the patient is in arrest. The second is the reverse: shocking &ldquo;VF&rdquo; that is really artifact from a patient shivering or a nurse adjusting the lines. The rule protects against both: the rhythm decides <em>which</em> arrest treatment, only after the patient has told you it <em>is</em> an arrest.</p>
{{key:The strip chooses the treatment; the patient decides whether there is a pulse. Never let a regular rhythm stop compressions without a definite pulse.}}
"""),
        ("rhythms", "Shockable or not, stable or not", "The four rhythm decisions", """
<p>Once the patient is placed, recognition narrows to four decisions. Each has a physiological reason.</p>
<h3>Shockable or nonshockable</h3>
<p>VF and pulseless VT are electrical chaos or a ventricular rhythm too fast to fill the heart. A shock depolarizes the whole heart at once so a normal pacemaker can take over. Asystole has no electricity to reset, and PEA already has organized electricity without pumping; neither responds to a shock, and both point the team toward causes such as potassium, volume, hypoxia or tamponade. In clinic registries the first rhythm varies: one population study found VF or VT in 72 of 102 dialysis-unit arrests,[[davis2008]] while a later registry of 398 clinic arrests found two thirds nonshockable.[[pun2019]] Do not assume; attach the defibrillator and let the rhythm decide.</p>
<h3>With a pulse or pulseless</h3>
<p>A slow or fast rhythm with a definite pulse belongs to the bradycardia or tachycardia algorithms. The same rhythm without a pulse belongs to arrest.</p>
<h3>Stable or unstable</h3>
<p>For a rhythm with a pulse, instability is defined by its effect on organs: low blood pressure, acutely altered mental status, signs of shock, ischemic chest discomfort or acute heart failure.[[aha2025_als]] The 2025 adult guideline gives one example threshold for wide-complex tachycardia: a systolic pressure under 80 mm Hg or altered mentation indicates instability requiring immediate cardioversion.[[aha2025_als]]</p>
{{fig:rl03_stability}}
<h3>Adult or pediatric</h3>
<p>Pediatric guidance applies to infants and children up to about puberty; after puberty, adult guidance applies.[[aha2025_pbls]] The pediatric pathway is chosen early because ventilation, compression technique, ratios, drug doses and energies all change (Modules 10 and 11).</p>
{{key:Shockable or not, pulse or not, stable or not, child or adult. Four decisions, each tied to what the heart is actually doing.}}
"""),
        ("potassium", "Potassium and the ECG", "Pre-arrest hyperkalemia, hyperkalemic arrest, and the ECG", """
<p>In a dialysis unit, high potassium is the overlay that changes everything. Recognition separates two very different situations. <strong>Hyperkalemia with a pulse</strong> is a race to protect the heart, shift potassium, and dialyze; the patient may look well. <strong>Hyperkalemic cardiac arrest</strong> is cardiac arrest first, with potassium as the reversible cause to treat during CPR. The same laboratory value can belong to either, so the five questions come before the potassium.</p>
{{fig:rl03_k_ecg}}
<div class="table-wrap"><table>
<thead><tr><th>Typical ECG change as potassium rises</th><th>What is happening in the membrane</th></tr></thead>
<tbody>
<tr><td>Peaked, narrow T waves</td><td>Faster repolarization</td></tr>
<tr><td>Flattened or absent P waves, longer PR</td><td>Slowed atrial conduction</td></tr>
<tr><td>Widening QRS, slow junctional or ventricular rhythm</td><td>Slowed conduction through the ventricles</td></tr>
<tr><td>Sine-wave pattern, then VF, asystole or PEA</td><td>Conduction failing; arrest</td></tr>
</tbody></table></div>
<p>That order is a teaching pattern, not a reliable ladder. In a retrospective review of hospital patients with high potassium, typical ECG changes were often absent, even at high values.[[montague2008]] A dialysis patient may jump from a nearly normal tracing to a slow wide rhythm or arrest. A normal ECG never makes a high potassium safe; an abnormal ECG never waits for the laboratory.</p>
<p>In a dialysis unit, suspect potassium first when a slow, wide, or bizarre rhythm appears before or early in a session, after a missed session or the long weekend gap, or in a patient on an atrioventricular nodal blocking drug (Module 6, BRASH).</p>
{{key:Pulse first, potassium second. Hyperkalemia with a pulse and hyperkalemic arrest are different algorithms, and a normal ECG proves nothing.}}
{{call:A slow, wide or bizarre rhythm in a dialysis patient, with or without a laboratory result: attach the defibrillator, check for a pulse, and call the physician-on-duty now. Follow your unit protocol, and always ask the attending nephrologist for guidance.}}
"""),
    ],
    "debrief": ["""
<p><strong>The algorithm.</strong> Slow snoring breaths every few seconds are agonal breathing, not normal breathing. The first check is a pulse, for no more than 10 seconds, while looking at the chest. If no definite pulse is felt, Mr. Reyes is in cardiac arrest, whatever the monitor shows.</p>
<p><strong>The monitor.</strong> A regular narrow rhythm at 64 per minute means organized electricity. In a patient with gasping and no pulse, that is pulseless electrical activity: a nonshockable arrest. The rhythm does not prove circulation; the low pressure alarm and the gasping argue strongly against it.</p>
<p><strong>The ten seconds.</strong> Ms. Torres says: &ldquo;Not breathing normally. No pulse. Code! Chair flat, start compressions.&rdquo; She does not give a saline bolus first. Then the team stops fluid removal, applies pads, follows the nonshockable path with epinephrine as soon as feasible, and looks for causes: volume from fluid removal, potassium, hypoxia, bleeding at the access (lift the blanket), and tamponade.</p>
<p>The habit that would have saved the minute: in any slumped dialysis patient, check breathing and pulse together before treating the blood pressure.</p>
"""],
    "skills": {"title": "Recognition at the chair",
               "intro": "In five rapid scenarios run by a facilitator with a manikin and a monitor simulator, name the algorithm and first action within 15 seconds each.",
               "items": [
                   ("Checks breathing and a definite pulse together within 10 seconds before treating blood pressure.", True),
                   ("Treats gasping or agonal breathing as not breathing.", True),
                   ("States that an organized rhythm without a pulse is PEA and starts compressions.", True),
                   ("Confirms a flat line by checking leads, gain and a second lead while compressions continue.", False),
                   ("Judges stability of a rhythm with a pulse by the five signs of instability.", False),
                   ("Separates hyperkalemia with a pulse from hyperkalemic arrest and names the first action for each.", False),
                   ("Chooses the pediatric pathway for a child before puberty and says why.", False),
               ],
               "placement": "Complete three recognition rounds in the Practice Lab and review every missed item with the charge nurse."},
    "terms": [("Agonal breathing", "Gasping breaths from a brain without blood flow; not normal breathing."),
              ("PEA", "Pulseless electrical activity: an organized rhythm with no pulse."),
              ("Asystole", "No electrical activity, confirmed in more than one lead."),
              ("Artifact", "Interference on the monitor from movement or loose leads, not the heart."),
              ("Hyperkalemic cardiac arrest", "Cardiac arrest in which high potassium is the suspected cause."),
              ("Sine-wave pattern", "A late ECG pattern of severe hyperkalemia in which QRS and T merge into smooth waves.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "The site guide to potassium and hyperkalemia in kidney disease.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["03"])
