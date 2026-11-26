# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 08: Watching Every Access on the Floor. Written for this series from published sources."""

MODULE = {
    "image_alt": "A fistula arm with taped needles and a looped line resting on top of a blanket so the access stays visible.",
    "objectives": [
        "Keep every access on the floor visible and secured, every session.",
        "Explain why the venous pressure alarm can miss a dislodged needle.",
        "Lead the first minute of access bleeding and of needle dislodgement.",
        "Recognize findings that mean a fistula or graft should not be needled today.",
        "Keep catheter connections safe on a floor with several catheters.",
    ],
    "big": """
{{plain:Picture a garden hose with its nozzle resting in a bucket. If the nozzle slips out, the pump keeps running and the water pours onto the floor. The pressure gauge at the tap barely moves.}}
<p>That is venous needle dislodgement. Blood keeps returning from the blood pump, often 300 mL a minute, but now onto the bed or floor. The machine reads venous pressure mostly from the resistance of the line and the needle, not the vein. When the needle slips out, the reading may fall only a little and stay inside the alarm window. The alarm is a backup; the eyes are the main safeguard.</p>
<p>The picture has a limit. Water on a floor is easy to see; blood can soak quietly into a blanket or a mattress, and a patient who is asleep or confused will not call out. The loss also comes out of a blood volume of only a few liters, so every minute counts. Your work in this module is to keep every access visible, check it on a schedule, and run the first minute of a bleed the same way every time.</p>
{{cards:Key terms for this module|Arteriovenous fistula (AVF)::A vein joined to an artery in the arm, which enlarges so it can be needled.|Graft::A tube joining an artery and a vein, used like a fistula.|Tunneled catheter::A tube in a large neck or chest vein, tunneled under the skin.|Venous needle dislodgement::The return needle coming out while the pump runs.|Thrill::The buzzing felt over a working fistula or graft.|Bruit::The whooshing sound heard over a working fistula or graft.}}
""",
    "case": {"title": "Under the blanket", "html": """
<p>At 9:15 the unit is cold. Mr. Arturo Gomez, 55, who has a left forearm fistula, pulls his blanket up to his chin and falls asleep. Blood flow is 300 mL a minute.</p>
<p>At 9:40, the patient in the next chair calls out that the floor under Bed 5 is wet. The venous pressure alarm never sounded. The charge nurse, Benjie Ocampo, is at Bed 12.</p>
""", "questions": ["Why did the alarm not sound?",
                  "What are the first sixty seconds?",
                  "What floor-wide rule prevents this from happening again?"]},
    "sections": [
        ("alarm", "Why the alarm misses it", "Why the alarm can miss a dislodged needle", """
<p>In a bench simulation of 19 needle dislodgements, the machine&rsquo;s venous pressure alarm sounded in only 8, or 42%.[[hn_frinak2023]] A review of needle dislodgement and line separation recommends that the access be visible at all times, that lines be taped securely with a loop, and that wetness detectors be used where available.[[hn_speranzareid2021]]</p>
{{fig:cn08_hose}}
<p>The rule that follows is simple: the access is never covered. If the patient is cold, give a second blanket under the access arm, or keep the arm on top of the blanket. The charge nurse checks this on every round.</p>
{{key:Never covered. The alarm is a backup; your eyes are the safeguard.}}
"""),
        ("bleed", "First minute", "The first minute of access bleeding", """
{{fig:cn08_bleed}}
{{flow:The first minute|Stop the blood pump::Every second the pump runs, blood leaves the patient.|Press firmly on the site::For a dislodged needle, press the hole in the skin and the vessel with gauze. Do not lift to look.|Call for help::One nurse keeps pressing; another brings what is needed.|Clamp the lines::Stop any flow from the circuit.|Check the patient, then call::Pressure, pulse, and consciousness; estimate the loss; call the physician before any decision about reconnection.}}
<p>In a review of 88 deaths from access bleeding in Australia and New Zealand, 78% of the deaths with a known location happened at home or in a nursing home, not in the dialysis unit.[[jose2017]] Teach every patient and family member to press firmly and call for help. The charge nurse makes sure that teaching happens, even on busy days.</p>
"""),
        ("noneedle", "Don&rsquo;t needle today", "Findings that mean do not needle today", """
<p>Look, listen, and feel before needling. Some findings mean hold and call, not &ldquo;needle somewhere else&rdquo;:</p>
{{fig:cn08_dontneedle}}
<ul>
<li>Thin, shiny skin over a bulge (aneurysm), or a scab on it</li>
<li>Spontaneous bleeding from the access</li>
<li>Redness, warmth, pus, or a fever</li>
<li>No thrill or bruit, or a change in the sound</li>
<li>A cold, pale, or painful hand on the access side</li>
</ul>
<p>Guidance from the Kidney Disease Outcomes Quality Initiative (KDOQI) advises urgent surgical assessment for skin erosion over an access, because it can rupture.[[lok2020]] These are hold-and-call findings for the attending nephrologist and, through them, the access surgeon.</p>
"""),
        ("cath", "Catheters", "Catheters on a busy floor", """
<p>Catheters carry the highest infection risk of any access, and in a meta-analysis of observational studies, patients dialyzed through a catheter had higher risks of death, infection, and cardiovascular events than those with a fistula.[[ravani2013]] On a floor with several catheter patients, the charge nurse plans connections so each one is a protected, uninterrupted task (Module 4): mask, hand hygiene, hub scrub, a fresh cap, and the hub never left open to the air.</p>
<p>Air embolism is a catheter emergency. If air enters the line: clamp, place the patient on the left side with the head down if your protocol says so, give oxygen, and call.[[mccarthy2016]]</p>
{{scene:Three catheters at 6:00|<p>A Monday morning has three catheter patients in one pod. Instead of three nurses rushing three connections at once, the charge nurse staggers them: Arnel connects Bed 2 at 6:00, Bed 4 at 6:10, Bed 6 at 6:20, each with the do-not-interrupt apron on. The fistula patients in the next pod are connected meanwhile by Kris and Mika. The schedule runs ten minutes longer and nobody&rsquo;s hub is open while an alarm calls the nurse away.</p>}}
"""),
        ("arm", "Arm rules", "Arm rules for everyone", """
<p>No blood pressure cuff, tight sleeve, wristwatch, intravenous line, or blood draw on the access arm, and no sleeping on it. Patients know this; ward nurses, phlebotomists, and relatives often do not. The charge nurse makes sure the rule travels with the patient: on the board, on the transfer summary (Module 16), and in a sentence to anyone who reaches for that arm.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Why no alarm.</strong> The alarm did not fail. It was never designed to catch dislodgement reliably: most of the venous reading comes from the line and the needle. The blanket hid the site.</p>
<p><strong>The first sixty seconds.</strong> Benjie stops the blood pump, presses firmly on the site, calls for help, has the lines clamped, and checks the patient: pressure 98/60, pulse 112, awake. He estimates the loss from the soaked linen at roughly 400 to 600 mL and calls the physician, who orders a hemoglobin and holds reconnection. How much could have been lost? At 300 mL a minute, every unwatched minute risks up to 300 mL (Head Nurse toolkit #c7). Partial dislodgement, clotting, and pump pauses usually reduce the real loss, but the arithmetic is the reason for the rule.</p>
<p><strong>The floor-wide rule.</strong> From today, blankets go under the access arm or the arm stays outside; venous lines are taped with a loop; every round checks every access by sight. Benjie writes it up as an incident with the system fix, not a blame note about the sleeping patient.</p>
"""],
    "skills": {"title": "Access oversight",
               "intro": "Round a real floor checking every access, then lead a simulated dislodgement on a training arm.",
               "items": [
                   ("Checks that every access is visible and every venous line is taped with a loop.", True),
                   ("Explains why the venous pressure alarm can miss dislodgement.", False),
                   ("Leads the first minute of bleeding: stop, press, call, clamp, check.", True),
                   ("Does not return blood or reconnect without the physician&rsquo;s decision after a bleed.", True),
                   ("Lists five findings that mean do not needle today.", True),
                   ("Plans catheter connections as protected, staggered tasks.", False),
                   ("States the first steps for air embolism.", True),
                   ("Teaches a patient and a relative to press and call at home, using teach-back.", False),
               ],
               "placement": "For one week, count on each round how many accesses were covered or poorly taped, and what you did."},
    "quiz": [
        ("In the bench study, how often did the alarm sound for a dislodged needle?",
         ["100%", "42%", "10%", "0%"], 1,
         "8 of 19 dislodgements."),
        ("What is the first action in access bleeding?",
         ["Look under the gauze", "Stop the pump and press firmly", "Return the blood", "Call the family"], 1,
         "Stop the loss first."),
        ("Where did most fatal access bleeds with a known location happen?",
         ["In dialysis units", "At home or in nursing homes", "In surgery", "In ambulances"], 1,
         "78% of those with a known location."),
        ("A scab on thin, shiny skin over an aneurysm. What do you do?",
         ["Needle elsewhere", "Hold and call for urgent assessment", "Remove the scab", "Ignore it"], 1,
         "Skin erosion over an access can rupture."),
        ("Which access carries the highest infection risk?",
         ["Fistula", "Graft", "Catheter", "All equal"], 2,
         "Catheters are the riskiest access."),
        ("The access should be:",
         ["Covered for warmth", "Visible at all times", "Covered only at night", "Bandaged during dialysis"], 1,
         "Never covered."),
        ("At 300 mL a minute, an unwatched minute risks up to:",
         ["30 mL", "300 mL", "3,000 mL", "3 mL"], 1,
         "The arithmetic behind the rule."),
        ("On the access arm:",
         ["Blood pressure cuffs are fine", "No cuffs, tight sleeves, watches, IV lines, or blood draws", "Only IV lines are allowed", "Only blood draws are allowed"], 1,
         "The rule travels with the patient."),
        ("Why does the venous pressure reading barely change when the needle comes out?",
         ["The vein is strong", "Most of the reading comes from the line and needle resistance", "The machine is old", "Blood is thick"], 1,
         "That is why eyes beat alarms."),
        ("No thrill or bruit before needling means:",
         ["Needle anyway", "Hold and call", "Use a bigger needle", "Wait an hour"], 1,
         "The access may have clotted."),
        ("Air enters a catheter line. First steps?",
         ["Speed up the pump", "Clamp, position per protocol, oxygen, call", "Remove the catheter", "Flush with saline"], 1,
         "Stop more air entering, then get help."),
        ("After a bleed is controlled, who decides about reconnection?",
         ["The charge nurse", "The physician", "The patient", "The technician"], 1,
         "Reconnection follows the physician&rsquo;s assessment."),
        ("A cold patient insists on covering his arm. Best response?",
         ["Let him", "Offer a blanket under the arm or a second blanket, and explain why", "Turn off the air conditioner for everyone", "Stop the session"], 1,
         "Warmth and visibility can both be met."),
        ("Why stagger three catheter connections in one pod?",
         ["To save gauze", "So each is a protected, uninterrupted task", "Because of PhilHealth rules", "To finish later"], 1,
         "An open hub plus an alarm is how infections start."),
        ("Who should be taught to press and call at home?",
         ["Nobody", "Every patient and family member", "Only patients with grafts", "Only nurses"], 1,
         "Most fatal bleeds happen outside the unit."),
    ],
    "terms": [("Arteriovenous fistula (AVF)", "A vein joined to an artery so it can be needled."),
              ("Graft", "A tube joining an artery and a vein, used like a fistula."),
              ("Tunneled catheter", "A tube in a large vein, tunneled under the skin."),
              ("Venous needle dislodgement", "The return needle coming out while the pump runs."),
              ("Thrill", "The buzzing felt over a working fistula or graft."),
              ("Bruit", "The whooshing sound heard over a working fistula or graft."),
              ("Air embolism", "Air entering the bloodstream through the circuit or catheter.")],
    "readings": [("hemodialysis-access-lifeline.html", "Keeping a dialysis access working for years."),
                 ("dialysis-access-care.html", "Caring for a fistula, graft, or catheter."),
                 ("dialysis-access-infection.html", "Recognizing and preventing access infections.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c7", "calc-catheter-exposure.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
