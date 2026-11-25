# -*- coding: utf-8 -*-
"""OT/PT track, Module 03: Screen Before Movement and Respond to Deterioration. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physical therapist kneeling beside a seated patient and asking how he feels before a walk, a nurse nearby.",
    "objectives": [
        "Explain why blood pressure can fall on standing after dialysis and why heart rate can mislead.",
        "Perform a structured pre-session screen using the unit&rsquo;s agreed parameter sheet.",
        "Decide to proceed, adapt, defer or stop, and state the reason.",
        "Stop immediately and summon help for red-flag symptoms, staying with the patient.",
        "Hand over a deterioration with SBAR and record who authorized any restart.",
    ],
    "big": """
{{plain:A pilot runs a checklist before every takeoff, even on a clear day with a plane that flew perfectly yesterday. Not because something is usually wrong, but because the one day something is wrong, the checklist is what catches it.}}
<p>The picture has a limit. A plane&rsquo;s checklist has fixed numbers. Your patients do not. A systolic pressure that is normal for one person on dialysis is dangerously low for another, and the same person can be stable at 9 a.m. and unstable at 2 p.m. after losing three liters in the chair. So your checklist asks questions and compares numbers with the person&rsquo;s own baseline and the limits the physician has set, rather than with one universal threshold.</p>
<p>This track gives no universal exercise-clearance numbers. The handoff that built it warns against inventing them, and the right numbers differ by patient. Instead, your unit agrees a <strong>parameter sheet</strong> with the nephrologist: which observations to take, at what values to adapt or defer, and whom to call. This module teaches the reasoning that makes the sheet work.</p>
{{fig:otpt03_decision}}
{{cards:Key terms for this module|Orthostatic hypotension::A fall in blood pressure on standing, often with dizziness or blurred vision.|Parameter sheet::The unit&rsquo;s physician-approved list of observations and limits for therapy sessions.|Proceed / adapt / defer / stop::The four decisions at every session.|SBAR::Situation, Background, Assessment, Recommendation: a structured handover.|Red flag::A symptom that means stop now and get help.}}
""",
    "case": {"title": "The final minute", "html": """
<p><strong>Monday, 1:35 p.m.</strong> Mrs. Corazon Reyes, 71, finished her morning hemodialysis at 11:30 with 2.8 kilograms removed. She is seated in the rehabilitation gym doing arm exercises with an elastic band when she becomes pale and clammy. She says her chest feels &ldquo;heavy, like a sack of rice.&rdquo; Her pulse on the finger oximeter reads 74.</p>
<p>&ldquo;One more minute,&rdquo; she says. &ldquo;I want to finish. I always finish.&rdquo;</p>
<p>PT Carlo Dizon is alone with her. The dialysis unit is two corridors away.</p>
""", "questions": ["What do you do in the next 60 seconds, in order?",
                  "Why does a pulse of 74 not reassure you?",
                  "What will you say when help arrives, and what must happen before she exercises again?"]},
    "sections": [
        ("why-pressure-falls", "Why pressure falls", "Standing up after dialysis: the physiology", """
<p>When anyone stands, about half a liter of blood shifts into the legs and belly. Pressure sensors in the neck and chest detect the drop and, within seconds, tighten the blood vessels and speed the heart. Pressure recovers before the brain notices.</p>
{{fig:otpt03_orthostasis}}
<p>After hemodialysis that reflex is working against three handicaps. First, ultrafiltration has removed fluid from the blood faster than it refills from the tissues, so there is less volume to shift. Second, many patients have autonomic neuropathy from diabetes or uremia, so the vessels tighten slowly. Third, beta-blockers and other antihypertensives blunt the heart-rate response. The result is a pressure that falls on standing, sometimes minutes later, sometimes only in a warm bathroom.</p>
<p>The same handicaps make heart rate a poor alarm. A patient on metoprolol can be in shock with a pulse of 70. A pulse that looks normal never cancels a worrying symptom.</p>
{{key:After dialysis, check symptoms and pressure on standing, and never let a normal pulse overrule a bad symptom.}}
"""),
        ("screen", "The screen", "A screen at every session", """
<p>Screen every time, briefly, and write it down. The questions are the same for OT and PT.</p>
{{flow:Pre-session screen|Ask::Chest discomfort, breathlessness, dizziness or fainting, fever, new pain, bleeding, falls, missed dialysis, new medicines, and how they feel today compared with usual.|Check the handoff::With the nurse: today&rsquo;s session, fluid removed, symptoms in the chair, access, any new restrictions or parameters.|Observe::The observations on your unit&rsquo;s sheet, taken with approved technique, never on the access arm: often blood pressure sitting and standing, pulse, oxygen saturation, temperature when indicated.|Compare::With the person&rsquo;s baseline and with the physician&rsquo;s parameters, not with a textbook number.|Decide::Proceed, adapt or defer, and record why.}}
<p>Timing matters. Many units prefer therapy on non-dialysis days, or before a session, or during the first half of a session under the nurse&rsquo;s eye (Module 10). Straight after a session with a large fluid removal is the riskiest time for standing tasks.</p>
{{key:The screen is quick when all is well and life-saving when it is not. Never skip it because the patient &ldquo;was fine yesterday.&rdquo;}}
"""),
        ("decide", "Proceed, adapt, defer, stop", "Four decisions, and when each applies", """
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>When</th><th>What you do</th></tr></thead>
<tbody>
<tr><td><strong>Proceed</strong></td><td>No new symptoms; observations within the agreed parameters and close to baseline</td><td>Deliver the planned session; keep watching</td></tr>
<tr><td><strong>Adapt</strong></td><td>Stable but tired, mildly dizzy on standing that settles, or observations near a limit</td><td>Shorten, sit instead of stand, add help, lower intensity; recheck</td></tr>
<tr><td><strong>Defer</strong></td><td>An unresolved acute change, or observations outside the agreed parameters</td><td>No therapy today; tell the nurse; ask for review; book the next try</td></tr>
<tr><td><strong>Stop</strong></td><td>A red flag during activity</td><td>Stop at once, make the patient safe, call for help, stay</td></tr>
</tbody></table></div>
{{call:Stop at once and summon immediate help for chest pain or pressure, fainting or near-fainting, severe or new breathlessness, new weakness, numbness, facial droop or confusion, significant bleeding (including from the access), a disrupted or dislodged access, palpitations with dizziness, or any rapid deterioration. Activate your facility&rsquo;s emergency response when indicated. Do not leave the patient.}}
<p>What you do not do matters as much. Do not diagnose hyperkalemia from symptoms, do not &ldquo;walk off&rdquo; an arrhythmia, and do not give water, salt, sugar, medicines or oxygen outside your authority and the emergency protocol.</p>
<p>Is exercise in this population dangerous? In a randomized trial of early physical and occupational therapy in mechanically ventilated patients, there was one serious adverse event in 498 therapy sessions (a desaturation), and sessions were stopped for instability in 4 percent.[[otpt_schweickert2009]] In the largest trial of exercise during dialysis, adverse events during sessions were similar in the exercise and usual-care groups.[[otpt_andingrost2023]] Supervised activity with screening is safe for most patients. The screen is what keeps it safe.</p>
{{key:Completion targets never override a concerning change. The session that stops early is the session that went right.}}
"""),
        ("sbar", "Handing over", "SBAR, and a restart that is authorized", """
<p>When you call for help, the first 30 seconds of what you say decide how fast help comes. Use SBAR (Situation, Background, Assessment, Recommendation):</p>
{{formula:<strong>Illustrative SBAR.</strong> <em>Situation:</em> &ldquo;This is Carlo, PT, rehab gym. Mrs. Reyes, 71, has chest heaviness and is pale and clammy during seated arm exercise. I stopped at 1:35.&rdquo; <em>Background:</em> &ldquo;Hemodialysis this morning, 2.8 kilograms removed, finished 11:30. On metoprolol.&rdquo; <em>Assessment:</em> &ldquo;Pulse 74 on the oximeter, saturation 95 percent. I don&rsquo;t have a pressure yet. She is alert.&rdquo; <em>Recommendation:</em> &ldquo;I need a nurse and a doctor here now. I&rsquo;ve activated the emergency response.&rdquo;}}
<p>Do not guess the diagnosis; give the facts. Afterward, document what you saw, what you did and when, who came, and what they decided. Exercise resumes only after a clinician has reviewed the event and authorized a restart, with any revised parameters written down. If your unit requires an incident report, complete it separately; the clinical note and the incident report do different jobs.</p>
{{key:A restart is a decision, not a default. Record who authorized it and the parameters they set.}}
"""),
    ],
    "debrief": ["""
<p><strong>The next 60 seconds.</strong> Carlo stops the exercise at once, despite her wish to finish. He keeps her seated and supported, loosens the band, and stays with her. He calls for immediate help: the emergency button or code in the gym, or by phone to the dialysis unit and the responding physician, per the facility pathway. He checks responsiveness and breathing and prepares to start basic life support if she collapses.</p>
<p><strong>Why the pulse does not reassure.</strong> She takes metoprolol, which blunts the heart-rate response; she had fluid removed hours earlier; and she has a red-flag symptom. Chest heaviness with pallor and sweating may be a cardiac event or a pressure drop. Either needs a clinician now.</p>
<p><strong>The handover and the restart.</strong> Carlo gives SBAR as above, then documents the times, observations and actions. Mrs. Reyes does not exercise again until the physician has reviewed the event, any tests are done, and a restart with written parameters is authorized. Carlo also reviews whether 2 hours after a 2.8-kilogram session was the right time for her therapy, and proposes a non-dialysis-day slot.</p>
"""],
    "skills": {"title": "Screen, decide and escalate",
               "intro": "Screen a simulated patient, make a proceed, adapt or defer decision, then respond to a scripted deterioration.",
               "items": [
                   ("Asks all screening questions, including missed dialysis, falls and new medicines.", False),
                   ("Obtains the nurse&rsquo;s handoff and locates the unit&rsquo;s parameter sheet.", True),
                   ("Takes observations with approved technique, never on the access arm, including sitting and standing pressure when indicated.", True),
                   ("States a proceed, adapt or defer decision with a reason tied to the screen.", False),
                   ("Stops immediately at a red flag and keeps the patient safe.", True),
                   ("Summons help through the facility pathway and stays with the patient.", True),
                   ("Gives a complete SBAR without guessing a diagnosis.", False),
                   ("Documents the event and the name of the clinician who authorized any restart.", True),
               ],
               "placement": "For two weeks, record your screen and decision for every session. Review the deferrals with your preceptor: were the reasons sound, and was a review obtained each time?"},
    "terms": [("Orthostatic hypotension", "A fall in blood pressure on standing."),
              ("Parameter sheet", "The physician-approved list of observations and limits for therapy."),
              ("Red flag", "A symptom that means stop and get help now."),
              ("Restart authorization", "A clinician&rsquo;s documented decision that therapy may resume, with any new limits.")],
    "readings": [("post-dialysis-fatigue.html", "Why patients feel drained after dialysis."),
                 ("potassium-hyperkalemia-ckd.html", "Potassium and the heart in kidney disease: why symptoms are unreliable.")],
    "calcs": ["calc-renal-rehabilitation-toolkit.html#tool-6"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["03"])
