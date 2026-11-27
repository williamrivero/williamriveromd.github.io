# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 02: How Resuscitation Algorithms Think. Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A small team at a whiteboard beside a dialysis chair while a physician sketches a branching decision path.",
    "objectives": [
        "Describe any resuscitation algorithm with the same ten parts: trigger, assessment, branches, first actions, parallel tasks, reassessment, transitions, common errors, dialysis considerations, and drill.",
        "Use five decision questions (responsive, breathing normally, definite pulse, shockable rhythm, stable) to enter the right algorithm.",
        "Explain why each branch point changes treatment, using the physiology behind it.",
        "Plan the parallel tasks of a seven-person team across one two-minute cycle.",
        "Recognize the moments when a patient moves from one algorithm to another, and announce the transition aloud.",
    ],
    "big": """
{{plain:An algorithm is like a road map with junctions. You do not memorize every street; you learn to read the signs at each junction. Is the person awake? Breathing? Is there a pulse? Will a shock help? Is the circulation holding? Each answer sends you down one road, and each road has a short list of first moves.}}
<p>The picture has a limit. Maps assume the road stays still. Patients do not. A man with a slow pulse can lose it while you prepare the pacer; a woman in arrest can regain a pulse during the next two minutes of compressions. So the real skill is not following one road to its end. It is reading the signs again at every pause, and changing roads the moment the answer changes.</p>
<p>This module teaches the shape every algorithm in the course shares. Once you see that shape, the adult arrest, bradycardia, tachycardia and pediatric algorithms stop being separate charts to memorize. They become variations on five questions.</p>
{{cards:Key terms for this module|Algorithm::A structured sequence of assessments, decisions and actions for one clinical problem.|Trigger::The finding that tells you to enter an algorithm.|Branch point::A question whose answer changes what you do next.|Parallel tasks::Actions done at the same time by different team members.|Reassessment::A short, planned check of the patient after an action or a set interval.|Transition::Moving from one algorithm to another because the patient&rsquo;s condition changed.}}
""",
    "case": {"title": "Box by box", "html": """
<p>At 10:15 a.m., Mrs. Remedios Aquino, 72, is two hours into her session at a hospital-based dialysis unit in Iloilo City. She has been on hemodialysis for six years and takes a beta-blocker. Nurse Mr. Carlo Medina notices she is drowsy. Her heart rate on the monitor is 38 per minute and her blood pressure is 78/40 mm Hg. She opens her eyes to her name and says she feels faint.</p>
<p>Dr. Ana Villaruel, the physician-on-duty, arrives with the defibrillator. While the team attaches pads and prepares atropine, Mrs. Aquino stops answering. Her breathing becomes slow gasps. Mr. Medina cannot feel a carotid pulse.</p>
""", "questions": ["Which algorithm was the team in at 10:15, and which one are they in now?",
                  "What should be said aloud at the moment of transition?",
                  "Which tasks happen at the same time in the next 60 seconds, and who does each?"]},
    "sections": [
        ("frame", "The ten-part frame", "One frame for every algorithm", """
<p>Algorithm charts are compressed. They show boxes and arrows, but not why each box exists or who does it. This course unpacks every algorithm into the same ten parts so you can learn one and recognize the rest.</p>
{{fig:rl02_frame}}
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>The question it answers</th><th>Example (adult arrest)</th></tr></thead>
<tbody>
<tr><td>1 Trigger</td><td>When do I enter this algorithm?</td><td>Unresponsive, not breathing normally, no definite pulse in 10 seconds</td></tr>
<tr><td>2 Assessment</td><td>What do I check, and what is still unknown?</td><td>Rhythm on the monitor; cause not yet known</td></tr>
<tr><td>3 Branches</td><td>Which answer changes treatment, and why?</td><td>Shockable or not: a shock fixes VF, not asystole</td></tr>
<tr><td>4 First actions</td><td>What happens in the first minute?</td><td>Compressions, pads, shock if shockable</td></tr>
<tr><td>5 Parallel tasks</td><td>Who does what at the same time?</td><td>Airway, IV access, drugs, circuit, recorder</td></tr>
<tr><td>6 Reassessment</td><td>When do I look again?</td><td>Every 2 minutes, a pause of under 10 seconds</td></tr>
<tr><td>7 Transitions</td><td>When do I change algorithms?</td><td>Organized rhythm with a pulse: care after return of spontaneous circulation (ROSC)</td></tr>
<tr><td>8 Common errors</td><td>Where do teams go wrong?</td><td>Treating the monitor instead of feeling for a pulse</td></tr>
<tr><td>9 Dialysis considerations</td><td>What changes because of the circuit?</td><td>Fluid removal stopped, blood decision announced</td></tr>
<tr><td>10 Drill</td><td>How do we practice it?</td><td>Interactive case and a facilitated megacode</td></tr>
</tbody></table></div>
<p>The diagrams in this course are original teaching layouts. They follow the 2025 AHA recommendations but are not copies of AHA algorithm charts, which belong to the AHA courses.</p>
{{key:Learn the frame once. Every algorithm then becomes a trigger, a few branch points, and a short list of first moves.}}
"""),
        ("questions", "Five questions", "Five questions that sort the floor", """
<p>Almost every emergency on the dialysis floor can be placed in the right algorithm by five questions asked in order. Each question exists because its answer changes the physiology you are treating.</p>
{{fig:rl02_five_questions}}
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Why it changes treatment</th><th>If the answer is no</th></tr></thead>
<tbody>
<tr><td>1 Responsive?</td><td>A responsive patient has a brain that is still perfused</td><td>Shout for help; check breathing and pulse together</td></tr>
<tr><td>2 Breathing normally?</td><td>Gasping is a sign of a brain without blood flow, not breathing</td><td>Treat gasping as not breathing</td></tr>
<tr><td>3 Definite pulse within 10 seconds?</td><td>No pulse means no circulation: only compressions move blood</td><td>Start compressions: cardiac arrest</td></tr>
<tr><td>4 Shockable rhythm?</td><td>VF and pulseless VT are chaotic electricity that a shock can reset; asystole and PEA are not</td><td>Nonshockable path: epinephrine as soon as feasible, find the cause</td></tr>
<tr><td>5 Stable? (when there is a pulse)</td><td>Low pressure, confusion, shock, chest pain or heart failure mean the rhythm is starving organs now</td><td>Unstable: treat the rhythm immediately (atropine or pacing; synchronized cardioversion)</td></tr>
</tbody></table></div>
<p>The AHA recommends that pulse checks take no more than 10 seconds, and that compressions restart immediately if no pulse is definitely felt (COR 1, LOE C-LD).[[aha2025_bls]] The word &ldquo;definitely&rdquo; matters: a weak, uncertain pulse in a gasping patient is treated as no pulse. Compressions on a patient who turns out to have a pulse rarely cause serious harm; withholding them from a patient in arrest is fatal.</p>
<p>The fifth question uses signs, not numbers. The 2025 adult ALS guideline describes instability as hypotension, acutely altered mental status, signs of shock, ischemic chest discomfort, or acute heart failure caused by the rhythm.[[aha2025_als]] A heart rate of 38 is not itself unstable; a heart rate of 38 with a pressure of 78/40 and drowsiness is.</p>
{{key:Responsive, breathing normally, definite pulse, shockable, stable. Ask them in order, out loud, every time.}}
"""),
        ("parallel", "Parallel tasks", "One chart, seven people, at the same time", """
<p>Algorithm charts read from top to bottom, which suggests one action after another. A real team works in parallel. While one person compresses, another applies pads, a third manages the airway, a fourth draws up epinephrine, a fifth manages the circuit, a sixth records, and a seventh watches the other patients. The leader&rsquo;s job is to keep these lanes moving together and to make the decisions at each branch.</p>
{{fig:rl02_parallel}}
<div class="table-wrap"><table>
<thead><tr><th>Seconds after recognition</th><th>Compressor</th><th>Defibrillator and drugs</th><th>Circuit nurse</th><th>Leader</th></tr></thead>
<tbody>
<tr><td>0 to 15</td><td>Chair flat, compressions start</td><td>Brings defibrillator</td><td>Stops fluid removal</td><td>Calls the code, names roles</td></tr>
<tr><td>15 to 60</td><td>Continues</td><td>Pads on, rhythm analysis</td><td>Stops blood pump if needed; blood decision</td><td>Reads rhythm; orders shock or not</td></tr>
<tr><td>60 to 120</td><td>Continues; second compressor ready</td><td>Draws up epinephrine as ordered</td><td>Secures access for drugs; announces blood status</td><td>Asks for reversible causes; checks ambulance call</td></tr>
<tr><td>At 2 minutes</td><td>Swaps compressor</td><td>Charges before the pause if shockable</td><td>Reports circuit safe</td><td>Leads a pause under 10 seconds</td></tr>
</tbody></table></div>
<p>The leader stays hands-off when staffing allows. A leader who is also compressing cannot see the monitor, the clock and the team at once. In a three-person team this is not possible, and Module 13 shows which roles combine safely.</p>
{{key:The chart is sequential; the team is parallel. The leader keeps the lanes moving and owns every branch decision.}}
"""),
        ("transitions", "Transitions", "When the patient changes roads", """
<p>The most common recognition error is staying in the wrong algorithm after the patient has changed. A team preparing a pacer for bradycardia keeps working on the pacer after the pulse is gone. A team in arrest keeps compressing after a strong pulse has returned because nobody checked. Every reassessment is a chance to ask the five questions again.</p>
{{fig:rl02_transitions}}
<div class="table-wrap"><table>
<thead><tr><th>From</th><th>Change</th><th>To</th><th>First move</th></tr></thead>
<tbody>
<tr><td>Bradycardia or tachycardia with a pulse</td><td>Pulse lost, not breathing normally</td><td>Cardiac arrest</td><td>Compressions now</td></tr>
<tr><td>Cardiac arrest</td><td>Organized rhythm and a definite pulse</td><td>Post-ROSC care</td><td>Check pressure, oxygen, ECG</td></tr>
<tr><td>Cardiac arrest, nonshockable</td><td>VF appears at a rhythm check</td><td>Shockable path</td><td>Shock</td></tr>
<tr><td>Post-ROSC</td><td>Pulse lost again</td><td>Cardiac arrest</td><td>Compressions now</td></tr>
<tr><td>Deterioration with a pulse (child)</td><td>Heart rate under 60 with poor perfusion despite good ventilation</td><td>Pediatric cardiopulmonary resuscitation (CPR)</td><td>Compressions</td></tr>
</tbody></table></div>
<p>Say the transition aloud: &ldquo;No pulse. We are now in cardiac arrest. Start compressions.&rdquo; This closes the old plan for everyone at once. The recorder writes the time, and the leader re-names the roles if needed.</p>
{{key:At every reassessment, ask the five questions again. When the answer changes, announce the new algorithm aloud.}}
{{scene:The pacer that kept the team busy|<p>During a drill, the team spent 90 seconds adjusting a transcutaneous pacer on a manikin whose pulse the facilitator had removed. The recorder noticed first: &ldquo;Nobody has checked a pulse since the pads went on.&rdquo;</p>
<p class="tc-scene-take">Equipment pulls attention. A planned reassessment pulls it back to the patient.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The two algorithms.</strong> At 10:15 Mrs. Aquino was in the bradycardia-with-a-pulse algorithm, and she was unstable: heart rate 38, pressure 78/40, drowsy. The right moves were monitor, oxygen, IV access, atropine as ordered, and preparing to pace, while looking for causes: potassium, the beta-blocker, ischemia. When she stopped responding, began gasping, and had no definite pulse, she moved to cardiac arrest.</p>
<p><strong>The words.</strong> Dr. Villaruel says: &ldquo;No pulse. Cardiac arrest. Carlo, compressions now. Chair flat.&rdquo; The atropine and pacer plan stops. The recorder notes the time.</p>
<p><strong>The next 60 seconds, in parallel.</strong> Mr. Medina compresses; a second nurse takes over the bag-mask; the pads already on the chest go to analysis; the circuit nurse stops fluid removal and the blood pump and announces the blood decision; the runner calls the hospital code team; the watcher stays with the other patients; and the leader asks, &ldquo;Potassium? When was her last result?&rdquo; Slow rhythm plus a beta-blocker in a dialysis patient raises BRASH and hyperkalemia (Modules 6 and 8).</p>
"""],
    "skills": {"title": "Five questions and an announced transition",
               "intro": "During a facilitated scenario, lead the first two minutes of an evolving case while a supervisor observes.",
               "items": [
                   ("Asks the five decision questions aloud in order: responsive, breathing normally, definite pulse, shockable, stable.", True),
                   ("Limits the pulse check to 10 seconds and treats an uncertain pulse with gasping as no pulse.", True),
                   ("Judges stability by signs (pressure, mental status, shock, chest pain, heart failure), not by heart rate alone.", False),
                   ("Assigns parallel tasks by name within the first 30 seconds.", False),
                   ("Recognizes a change at reassessment and announces the new algorithm aloud.", True),
                   ("Stops the previous plan (for example, pacing) when the patient enters cardiac arrest.", True),
               ],
               "placement": "Shadow the physician-on-duty for one shift and, for each patient event, name the algorithm aloud afterward and the question that placed it there."},
    "terms": [("Algorithm", "A structured sequence of assessments, decisions and actions for one problem."),
              ("Branch point", "A question whose answer changes the next action."),
              ("Reassessment", "A planned check of the patient after an action or interval."),
              ("Transition", "Moving to another algorithm because the patient changed."),
              ("Agonal breathing", "Gasping breaths of a brain without blood flow; treated as not breathing."),
              ("Instability", "Signs that the rhythm is starving organs: low pressure, confusion, shock, chest pain, heart failure.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["02"])
