# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 11: Water and Machines: Hold, Escalate, Release. Written for this series from published sources.
Deliberately numberless: water limits belong to the unit's approved protocol (blueprint v1.0 safety decision)."""

MODULE = {
    "image_alt": "A charge nurse and a water technician checking a test strip beside carbon tanks in a dialysis water room.",
    "objectives": [
        "Follow water through the treatment chain and say what each stage removes.",
        "Read the water log before opening and recognize an incomplete or abnormal entry.",
        "Hold treatment when water or a machine is not released, and escalate.",
        "Lead the first steps when several patients react in a pattern that suggests water or dialysate.",
        "Reopen only on a signed release from the authorized people.",
    ],
    "big": """
{{plain:A water refilling station sells water you can drink. A dialysis water room makes water that touches your blood across a thin membrane, more than a hundred liters each session. The standard is not &ldquo;drinkable&rdquo;; it is &ldquo;safe in the bloodstream.&rdquo;}}
<p>The treatment chain removes particles, hardness, chlorine and chloramine, dissolved ions, and microbes in turn. Each stage protects the next. If one fails, the next may be overwhelmed, and a contaminant can reach the patient within one shift.[[hn_iso2024]] The charge nurse does not run the water room. She makes sure nobody connects a patient to water that has not been released.</p>
{{cards:Key terms for this module|Carbon tank::Removes chlorine and chloramine.|Reverse osmosis (RO)::A membrane that removes most dissolved ions and many microbes.|Distribution loop::The pipes that carry treated water to the machines.|Endotoxin::Fragments of bacteria that can cause fever and inflammation.|Conductivity alarm::A machine alarm that the dialysate mix may be wrong.|Release::The authorized technical lead&rsquo;s signed statement that water or a machine is fit to use.}}
""",
    "case": {"title": "Headache and nausea in three chairs", "html": """
<p>At 7:20, three patients in neighboring stations complain of nausea and headache; one also has chest tightness and back pain. All three started between 6:30 and 6:45. The morning chlorine entry was signed at 5:40 as &ldquo;within limit.&rdquo;</p>
<p>The water technician mentions that the carbon tank was backwashed late the night before. The charge nurse is Ramon Aquino. Nine other patients are connected.</p>
""", "questions": ["What could connect the three patients?",
                  "What are the first steps, in order?",
                  "Who can restart the unit, and on what basis?"]},
    "sections": [
        ("chain", "The chain", "The treatment chain and what fails", """
<p>Carbon removes chlorine and chloramine. When carbon is exhausted or bypassed, chloramine reaches the patient and damages red cells, causing hemolysis.[[ward1996]] Aluminum and fluoride in dialysis water have caused fatal outbreaks in the past.[[tipple1991]] Bacteria and endotoxins grow in stagnant pipes and can cause fever and chills during dialysis.</p>
{{fig:cn11_chain}}
"""),
        ("log", "Reading the log", "Reading the water log", """
<p>Before opening, check that the day&rsquo;s tests are entered, signed, and timed, and that any out-of-range entry has an action written beside it. The numerical limits and the testing schedule are in the unit&rsquo;s approved water protocol under DOH AO 2013-0003 and the applicable standards; the charge nurse does not set or change them.[[hn_doh2013]] This module deliberately gives no numbers. A charge nurse who carries numbers in her head, instead of reading the protocol, will one day use an old one.</p>
{{key:No numbers in your head. Numbers live in the protocol; your job is to see that they were checked and signed.}}
"""),
        ("pattern", "A pattern in neighboring chairs", "A symptom pattern in neighboring chairs", """
<p>Several patients with similar symptoms soon after starting point to something they share: the water, a batch of dialysate concentrate, a batch of dialyzers or lines, or the room. Act on the pattern without waiting for proof.[[hn_greenberg2021]][[saha2017]]</p>
{{fig:cn11_hold}}
{{flow:First steps, per your unit&rsquo;s protocol|Stop dialysis in affected patients::Do not return the blood if hemolysis is suspected: dark or port-wine-colored blood in the venous line, back pain, chest tightness.|Call::The physician on duty and the attending nephrologist; the water technician and the biomedical lead.|Hold new connections::Nobody else starts on that water or batch.|Save evidence::Patient blood samples, the dialysate, a water sample, lines and dialyzers, labeled with times.|Watch everyone else::One nurse assigned to the other patients&rsquo; symptoms and pressures.}}
{{call:Suspected hemolysis (dark venous-line blood, back pain, chest tightness): stop, do not return the blood, and call the physician now.}}
"""),
        ("machines", "Machines", "Machines", """
<p>A machine is used only after release by the biomedical staff. A tagged machine stays out of the bay. If a machine alarms for conductivity or temperature, do not override the alarm to keep going. Take the patient off per protocol if needed, take the machine out of use, tag it, and tell the technician.</p>
{{scene:The alarm that kept coming back|<p>At 8:10 a conductivity alarm sounds at Bed 6. The staff nurse silences it twice. The charge nurse stops at the chair: the alarm means the dialysate mix may be wrong. She has the patient taken off per protocol, moves him to a released machine, tags Machine 6, and calls the biomedical technician. The technician finds a cracked concentrate line. Twice silenced, one more time would have been dialysis with the wrong fluid.</p>}}
"""),
        ("restart", "Restart", "Restart needs signatures", """
<p>Reopening after a water or machine event requires the authorized technical lead&rsquo;s release and the medical director&rsquo;s agreement, in writing, per the unit protocol. A charge nurse never restarts on &ldquo;it should be fine now.&rdquo; There is no automatic restart rule.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What connects them.</strong> Three similar reactions in neighboring stations soon after starting point to a shared cause: water, dialysate concentrate, a batch of disposables, or the room. Back pain and chest tightness in one patient raise the possibility of hemolysis.</p>
<p><strong>The timeline.</strong> 7:20 symptoms in three chairs. 7:21 Ramon stops the three sessions, without returning the blood of the patient whose venous line looks dark, and calls the physician on duty. 7:23 he holds new connections and assigns one nurse to watch the other nine patients. 7:25 he calls the water technician and the biomedical lead. 7:30 the attending is informed; blood samples, dialysate, and a water sample are saved and labeled. 7:45 the technician retests total chlorine at the point of use: above the unit&rsquo;s limit; the carbon bed is exhausted.</p>
<p><strong>Restart.</strong> The carbon is replaced by 9:30. The technical lead signs the release and the medical director agrees in writing at 10:10. The affected patients are assessed by the physician; one is admitted. The remaining morning patients are rescheduled for the afternoon with full time. Ramon reopens only on signatures.</p>
"""],
    "skills": {"title": "Hold, escalate, release",
               "intro": "Read three sample water logs (one complete, one incomplete, one with an out-of-range entry) and run a tabletop water event with the technician.",
               "items": [
                   ("Names each stage of the treatment chain and what it removes.", False),
                   ("Identifies an incomplete or unsigned log entry as a hold.", True),
                   ("Recognizes a symptom pattern in neighboring chairs as a possible shared cause.", True),
                   ("Stops dialysis without returning blood when hemolysis is suspected.", True),
                   ("Calls the physician, technician, and biomedical lead, and holds new connections.", True),
                   ("Assigns a nurse to watch the other patients.", False),
                   ("Saves and labels evidence.", False),
                   ("Requires a signed release before restart.", True),
               ],
               "placement": "Spend one morning with the water technician during the daily tests, and review the log together."},
    "quiz": [
        ("What does carbon remove?",
         ["Bacteria", "Chlorine and chloramine", "Calcium", "Aluminum only"], 1,
         "When carbon fails, chloramine reaches the blood."),
        ("How does chloramine harm dialysis patients?",
         ["It raises pressure", "It damages red cells and causes hemolysis", "It lowers glucose", "It clots lines"], 1,
         "Oxidation of hemoglobin."),
        ("Several neighboring patients with similar symptoms soon after starting suggests:",
         ["Coincidence", "A shared cause", "Anxiety", "Late breakfast"], 1,
         "Act on the pattern."),
        ("Dark venous-line blood with back pain. What do you do?",
         ["Return blood quickly", "Stop and do not return the blood", "Increase blood flow", "Ignore it"], 1,
         "Suspected hemolysis."),
        ("Who can restart after a water event?",
         ["The charge nurse", "The technical lead&rsquo;s signed release with the medical director&rsquo;s agreement", "Any nurse", "The patient"], 1,
         "Restart needs signatures."),
        ("Where are the water limits?",
         ["In the charge nurse&rsquo;s memory", "In the approved water protocol", "With PhilHealth", "Nowhere"], 1,
         "Read the protocol; do not recall it."),
        ("A conductivity alarm sounds. What do you do?",
         ["Override it", "Take the machine out of use and tell biomedical", "Continue", "Lower blood flow"], 1,
         "The dialysate mix may be wrong."),
        ("During a water hold, the other patients are:",
         ["Ignored", "Watched by an assigned nurse", "Disconnected", "Sent home"], 1,
         "The event is not only in three chairs."),
        ("What does reverse osmosis remove?",
         ["Only particles", "Most dissolved ions and many microbes", "Nothing", "Only chlorine"], 1,
         "A membrane step after carbon."),
        ("What can bacteria and endotoxins in the loop cause?",
         ["Low glucose", "Fever and chills during dialysis", "Cramps only", "Nothing"], 1,
         "Stagnant pipes grow bacteria."),
        ("What evidence should be saved?",
         ["Nothing", "Blood samples, dialysate, a water sample, lines and dialyzers, labeled with times", "Only the chart", "Only the machine"], 1,
         "The investigation needs them."),
        ("The technician says, &ldquo;Go ahead, I&rsquo;ll sign later.&rdquo; What do you do?",
         ["Go ahead", "Wait for the signature", "Ask the patients", "Restart half the stations"], 1,
         "No signature, no restart."),
        ("Why does this module give no numerical water limits?",
         ["They do not exist", "They belong to the unit&rsquo;s approved protocol, and numbers in memory go out of date", "They are secret", "Nurses cannot read numbers"], 1,
         "The charge nurse checks that they were applied."),
        ("A log entry is out of range but has no action written beside it. What is it?",
         ["Fine", "A hold until the action is documented", "A typo", "Optional"], 1,
         "An abnormal result needs a recorded response."),
        ("Is there an automatic restart rule after a water event?",
         ["Yes, after one hour", "No; restart is a signed decision", "Yes, after the next test", "Yes, if patients feel well"], 1,
         "Written release and agreement only."),
    ],
    "terms": [("Carbon tank", "Removes chlorine and chloramine."),
              ("Reverse osmosis (RO)", "A membrane that removes most dissolved ions and many microbes."),
              ("Distribution loop", "Pipes carrying treated water to the machines."),
              ("Endotoxin", "Bacterial fragments that can cause fever and inflammation."),
              ("Conductivity alarm", "A warning that the dialysate mix may be wrong."),
              ("Hemolysis", "The bursting of red blood cells.")],
    "readings": [("dialysis-water-treatment-systems.html", "How dialysis water is treated and tested.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c8", "calc-carbon-tank-ebct.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
