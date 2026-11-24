# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 07: Mid-Session Surveillance. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse crouching beside a drowsy older woman during dialysis while another nurse brings a glucose meter.",
    "objectives": [
        "Explain why blood pressure falls during dialysis in terms of removal rate and refill.",
        "Recognize intradialytic hypotension by symptoms and by the definitions used in research.",
        "Give the first nursing response to falling pressure and cramps inside the unit protocol, and know when to call.",
        "Detect low blood sugar during a session in patients on insulin or sulfonylureas.",
        "Notice the patient who goes quiet, and treat drowsiness as a finding until proven otherwise.",
        "Prevent falls at disconnection and on the way out of the unit.",
    ],
    "big": """
{{plain:Picture a water tank drained from the bottom while a slow pipe refills it from the ground around it. If you drain faster than the pipe fills, the level drops, however much water is still in the ground.}}
<p>The blood is the tank and the tissues are the ground. During hemodialysis (HD), the machine removes fluid only from the blood, and the tissues refill it at a limited rate; the speed of removal is the ultrafiltration rate (UFR). When removal outruns refill, blood volume falls, the heart has less to pump, and the vessels tighten to hold the pressure up. In many dialysis patients that defense is weak: a stiff heart, nerve damage from diabetes, or a blood pressure tablet taken that morning.[[daugirdas2001]][[reeves2018]]</p>
<p>The tank picture stops short of one thing. A falling pressure also lowers blood flow to the heart, the brain, and the gut, and repeated drops are associated with injury to the heart muscle.[[burton2009]] This is why the charge nurse watches the middle of the session as closely as its start.</p>
{{cards:Key terms for this module|Intradialytic hypotension::A fall in blood pressure during dialysis that causes symptoms or needs nursing action.|Nadir::The lowest systolic pressure in a session.|Refill::Movement of water from the tissues back into the blood vessels.|Hypoglycemia::Low blood sugar.|Sulfonylurea::A diabetes tablet that makes the pancreas release insulin, and can cause low blood sugar.|Post-dialysis fatigue::Tiredness after a session that can last hours.}}
""",
    "case": {"title": "&ldquo;Lola is just sleeping&rdquo;", "html": """
<p>Mrs. Felicidad Cruz, 79, has diabetes treated with insulin. She started dialysis at 6:30 with a pressure of 138/70 and a fluid goal of 2.8 liters on a dry weight of 48 kilograms. She took her usual morning insulin and skipped breakfast because the jeepney came early.</p>
<p>At 8:45, the assigned nurse charts &ldquo;sleeping comfortably.&rdquo; On his 8:50 round, the charge nurse, Ramon Aquino, finds her hard to rouse and sweaty. Her pressure is 92/50. The machine shows 1.6 liters removed.</p>
""", "questions": ["What are the two most likely causes, and how do you tell them apart in two minutes?",
                  "What does Ramon do first, and what does he say to the physician?",
                  "What should have been caught at 6:15?"]},
    "sections": [
        ("define", "Defining a fall", "Defining a fall in pressure", """
<p>The European Best Practice Guideline (EBPG) defined intradialytic hypotension as a fall in systolic pressure of 20 mm Hg or more, or in mean arterial pressure of 10 mm Hg or more, with symptoms or a need for nursing action.[[ebpg2007]] In a large United States cohort, a nadir systolic below 90 mm Hg was the definition most strongly associated with death; for patients who started at 160 or more, a nadir below 100 was.[[hn_flythe2015]]</p>
{{fig:cn07_tank}}
<p>Use symptoms and numbers together. Yawning, cramping, nausea, dizziness, restlessness, or going quiet often come before the number falls. A patient who drops from 180 to 120 may be in more trouble than one who sits at 105 every session.</p>
"""),
        ("first", "First response", "The first response, inside the protocol", """
<p>Most units&rsquo; protocols share a common first sequence. Follow yours; this is the logic behind it.</p>
{{fig:cn07_algo}}
{{flow:First response to falling pressure|Stop or reduce fluid removal::The cause is usually removal outrunning refill; stopping removal lets the tissues catch up.|Lay the patient flat::Legs raised if breathing allows; this returns blood to the heart.|Check access, lines, and glucose::A disconnected line, bleeding, or low blood sugar can look the same.|Recheck pressure; saline per protocol::Give the volume your protocol allows.|Call::Per your unit&rsquo;s protocol, and always ask the attending nephrologist for guidance.}}
{{call:Call the physician now if pressure does not recover within minutes after stopping fluid removal and lying flat, or if there is chest pain, a new irregular pulse, confusion, breathlessness, or this is the second drop of the session. A drop that does not respond is something else until proven otherwise: a heart attack, an arrhythmia, bleeding, infection, or fluid around the heart.}}
"""),
        ("cool", "What does not work as hoped", "What does not work as hoped", """
<p>Cooling the dialysate was expected to protect pressure and the heart. In the MyTEMP trial (Major Outcomes With Personalized Dialysate Temperature), 84 Canadian centers were randomized to a cooler-dialysate policy or standard temperature, and cardiovascular death or admission did not differ.[[hn_mytemp2022]] Cooling may still help a particular symptomatic patient, as the attending decides; it is not a unit-wide fix.</p>
<p>The approach with the strongest logic is prevention: realistic fluid goals, longer or extra sessions when needed, and blood pressure tablets timed after dialysis rather than before (Module 5).</p>
"""),
        ("cramps", "Cramps", "Cramps", """
<p>Cramps cluster in the last hour and on days with large fluid removal. They are associated with fast removal and low blood volume. The first response is to slow or stop fluid removal and stretch the muscle; further treatment follows the unit protocol. A patient who cramps every session needs the fluid plan reviewed, not just more saline every time.</p>
"""),
        ("glucose", "Low blood sugar", "Low blood sugar during dialysis", """
<p>Glucose falls during dialysis, and the fall can be steep. In a 2026 study that used continuous glucose monitoring in 40 adults with insulin-treated diabetes, mean glucose fell 32% during dialysis, reached its lowest point at about 125 minutes, and 20% of participants had low blood sugar during a session.[[cn_liarakos2026]] It was a small observational study, but the pattern is clear and fits what nurses see.</p>
{{fig:cn07_glucose}}
<p>Low blood sugar looks like low pressure: sweating, confusion, drowsiness. Check a fingerstick glucose whenever a patient on insulin or a sulfonylurea becomes drowsy, sweaty, or confused, whatever the pressure shows. Treat per protocol and tell the physician.</p>
{{key:Drowsy plus diabetes medicine equals a fingerstick, before you decide it is only the pressure.}}
"""),
        ("quiet", "Going quiet", "The patient who goes quiet", """
<p>&ldquo;Sleeping comfortably&rdquo; is one of the most dangerous entries on a dialysis chart. Drowsiness during a session can be ordinary tiredness, or it can be low pressure, low blood sugar, high potassium, a stroke, or low oxygen. Rouse every patient at every round. If you cannot rouse someone easily, treat it as an emergency (Module 12).</p>
<p>Tiredness after dialysis is common, which is exactly why a sleepy patient is easy to dismiss. A meta-analysis of twelve studies found a pooled prevalence of post-dialysis fatigue of 61%.[[cn_dou2023]] Most sleepy patients are only tired. The rule exists for the few who are not.</p>
{{scene:The man who would not wake|<p>On a 10:00 round, Nurse Ana Villareal finds Mr. Lito Bautista, 66, asleep with his mouth slightly open. She touches his shoulder; he does not open his eyes. She says his name louder; he mumbles. His pressure is 118/70, the same as at the start. His glucose is 104. She notices the left side of his face droops. She stops the session per protocol, calls the physician on duty, and the patient is transferred for stroke assessment. If she had charted &ldquo;sleeping,&rdquo; the window for treatment might have closed.</p>}}
"""),
        ("falls", "Falls at disconnection", "Falls at disconnection", """
<p>After the session, sit the patient up slowly, check standing pressure if your protocol asks, and walk beside anyone with a history of falls, a low post-dialysis pressure, or a new blood pressure medicine. The riskiest moment is the first few steps toward the door, when pressure is at its lowest of the day.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Two likely causes.</strong> Low pressure from fast fluid removal, and low blood sugar from insulin without breakfast. Both make an older woman sweaty and hard to rouse. A two-minute check of pressure plus a fingerstick glucose separates them, or shows both.</p>
<p><strong>The two minutes (Toolkit #c8).</strong> Her systolic fell from 138 to 92: 46 mm Hg, or 33%. Removed so far: 1.6 liters in 2 hours 20 minutes, 1,600 &divide; 2.33 &divide; 48 = 14.3 mL/kg/h, above 13. Ramon stops fluid removal and lays her flat in twenty seconds, and asks the second nurse for a fingerstick while he rechecks the pressure: glucose 52 mg/dL. He treats the low sugar and gives saline per protocol, then calls: &ldquo;Mrs. Cruz, 79, took insulin and skipped breakfast, hard to rouse at 8:50, glucose 52, pressure 92/50 from 138, fluid removal stopped at 1.6 liters, rate was 14.3 mL/kg/h. Glucose treated, saline given. I need orders for the rest of the session and for her insulin.&rdquo; At 9:00 she is awake, pressure 112/60, glucose 118.</p>
<p><strong>What should have been caught at 6:15.</strong> Nobody asked about insulin and breakfast, and a fluid goal of 2.8 liters on a 48-kilogram patient over four hours implied a rate of 14.6 mL/kg/h. Both are pre-dialysis questions (Module 5). The fix is a standard question at the scale and a rule that any drowsy patient on diabetes medicine gets a glucose check.</p>
"""],
    "skills": {"title": "Mid-session surveillance",
               "intro": "A facilitator runs three simulated deteriorations: falling pressure, low blood sugar, and a patient who cannot be roused. A fourth station covers disconnection of a fall-risk patient.",
               "items": [
                   ("States the EBPG definition and the nadir flags.", False),
                   ("Stops or reduces fluid removal and lays the patient flat within the first minute.", True),
                   ("Checks access, lines, and glucose as part of the first response.", True),
                   ("Calls the physician when pressure does not recover or red-flag features appear.", True),
                   ("Checks glucose in a drowsy patient on insulin or a sulfonylurea.", True),
                   ("Rouses every patient on rounds and treats an unrousable patient as an emergency.", True),
                   ("Walks a fall-risk patient to the door and sits them up slowly.", False),
               ],
               "placement": "For two weeks, record every episode of falling pressure on your shifts: the rate at the time, the first response, and whether glucose was checked."},
    "quiz": [
        ("Which nadir was most strongly associated with death in the cohort (start below 160)?",
         ["Below 120", "Below 100", "Below 90", "Below 70 mm Hg"], 2,
         "Below 100 for patients who started at 160 or more."),
        ("What is the first step when pressure falls?",
         ["Call a code", "Stop or reduce fluid removal and lay the patient flat if breathing allows", "Increase blood flow", "Give potassium"], 1,
         "Let refill catch up."),
        ("What did MyTEMP show for cooler dialysate as a unit-wide policy?",
         ["Fewer cardiovascular events", "No difference in cardiovascular death or admission", "More deaths", "It was not randomized"], 1,
         "Cooling may still help a particular patient."),
        ("In the glucose monitoring study, how many participants had low blood sugar during a session?",
         ["1%", "20%", "60%", "None"], 1,
         "One in five, with the lowest point about two hours in."),
        ("A drowsy patient on insulin needs:",
         ["A blanket", "A fingerstick glucose and a pressure check", "More fluid removal", "To be left asleep"], 1,
         "Low sugar and low pressure look alike."),
        ("Pressure does not recover after stopping fluid removal and lying flat. Think of:",
         ["Ordinary fatigue", "Heart attack, arrhythmia, bleeding, infection, or fluid around the heart", "Thirst", "Anxiety"], 1,
         "Call the physician now."),
        ("Cramps are associated with:",
         ["Slow fluid removal", "Fast fluid removal and low blood volume", "High glucose", "Cold rooms only"], 1,
         "Slow or stop removal and stretch the muscle."),
        ("When is the riskiest moment for a fall?",
         ["Arrival", "The first steps after disconnection", "Mid-session", "Weighing in"], 1,
         "Pressure is lowest just after the session."),
        ("What defines intradialytic hypotension in the EBPG?",
         ["Any systolic below 120", "A fall of 20 mm Hg systolic or 10 mm Hg mean pressure, with symptoms or a need for action", "A heart rate above 100", "Only fainting"], 1,
         "Numbers plus symptoms or a need for nursing action."),
        ("What is the pooled prevalence of post-dialysis fatigue in the meta-analysis?",
         ["About 10%", "About 61%", "About 90%", "Unknown"], 1,
         "Common, which is why a sleepy patient is easy to dismiss."),
        ("Mrs. Cruz has 1.6 liters removed in 2.33 hours at 48 kilograms. What is the rate?",
         ["About 9 mL/kg/h", "About 14 mL/kg/h", "About 20 mL/kg/h", "About 30 mL/kg/h"], 1,
         "1,600 &divide; 2.33 &divide; 48 = 14.3."),
        ("A patient asks for the fluid goal to be &ldquo;finished&rdquo; in the last hour. What do you do?",
         ["Raise the rate to catch up", "Explain the risk and ask the physician; do not raise the rate on your own", "Agree", "End the session"], 1,
         "Catching up means a dangerous rate."),
        ("What is the second drop of pressure in one session a signal of?",
         ["Nothing", "The plan needs changing today; call the physician", "Normal tiredness", "A machine fault"], 1,
         "Repeated drops need a decision."),
        ("Why is &ldquo;sleeping comfortably&rdquo; a dangerous chart entry?",
         ["It is rude", "It can hide low pressure, low sugar, high potassium, stroke, or low oxygen", "Patients should stay awake", "It is too long"], 1,
         "Rouse every patient at every round."),
        ("When should blood pressure tablets usually be timed, if the physician agrees?",
         ["Just before dialysis", "After dialysis", "During dialysis", "Never"], 1,
         "Taking them before dialysis weakens the body&rsquo;s defense against falling pressure."),
    ],
    "terms": [("Intradialytic hypotension", "A fall in pressure during dialysis that causes symptoms or needs action."),
              ("Nadir", "The lowest systolic pressure in a session."),
              ("Refill", "Movement of water from the tissues back into the blood."),
              ("Hypoglycemia", "Low blood sugar."),
              ("Sulfonylurea", "A diabetes tablet that can cause low blood sugar."),
              ("European Best Practice Guideline (EBPG)", "European guidelines on hemodialysis, including hemodynamic stability."),
              ("Post-dialysis fatigue", "Tiredness after a session that can last hours.")],
    "readings": [("hemodialysis-complications.html", "The main complications of a session."),
                 ("post-dialysis-fatigue.html", "Why patients feel tired after dialysis."),
                 ("dialysis-cramps-stasis-pigmentation.html", "Why cramps happen during dialysis.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c8", "calc-hd-session-review.html", "calc-ufr-ceiling.html", "calc-dialysis-charge-nurse-toolkit.html#c6"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
