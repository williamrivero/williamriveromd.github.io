# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 06: The Order, the Machine, and the Minutes. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two nurses reading a dialysis order aloud against the machine screen before connecting a waiting patient.",
    "objectives": [
        "Explain what each main line of a hemodialysis order does in the body.",
        "Run a two-person, read-aloud check of the order, the machine, and the patient before connection.",
        "Explain why delivered time and blood flow, not prescribed time, decide the dose of dialysis.",
        "Count minutes lost to late starts, early stops, and alarm pauses, and act on them.",
        "Respond to a patient who asks to come off early by finding the reason.",
    ],
    "big": """
{{plain:A dialysis order is like a recipe. If the oven runs cooler than the dial says, or the cake comes out ten minutes early, it is not the cake on the recipe card, however carefully the ingredients were measured.}}
<p>The picture has a limit. A recipe card does not change, but the dose of dialysis is set at the chair, by the blood actually cleaned: the real blood flow through the dialyzer, the real dialysis fluid flow, and the real minutes on the machine. The machine can display the right numbers while the access sends cleaned blood straight back into the needle (recirculation), or the session is cut short. Prescribed is not the same as delivered. Your work in this module is to make the order, the machine, and the minutes match, and to count the minutes that were lost.</p>
{{cards:Key terms for this module|Dialysate::The dialysis fluid on the other side of the membrane; its potassium, sodium, bicarbonate, and calcium are prescribed.|Three-way check::Order, machine, and patient compared aloud by two people before connection.|Kt/V::A measure of the dose of dialysis: how much of the body&rsquo;s water is cleared of urea in a session.|Delivered time::The minutes the patient actually spent on the machine with blood flowing.|Recirculation::Cleaned blood returning straight into the arterial needle, which lowers the real dose.}}
""",
    "case": {"title": "&ldquo;She always asks to come off early&rdquo;", "html": """
<p>Mrs. Teresita Lim, 58, is prescribed four hours three times a week. Over the last month she has averaged three hours twenty-five minutes: some late arrivals, two early stops for cramps, and frequent alarm pauses. Her last single-pool Kt/V (spKt/V) was 1.12. Her dry weight is 55 kilograms and she often arrives 3.5 kilograms above it.</p>
<p>The staff nurse says, &ldquo;She signs the refusal form, so it&rsquo;s fine.&rdquo;</p>
""", "questions": ["How much dialysis has she lost in a month?",
                  "What is behind the early stops?",
                  "What does the charge nurse do, and who else is involved?"]},
    "sections": [
        ("lines", "The order", "What each line of the order does", """
<p>Every line of a dialysis order changes something specific in the body. The dialyzer and blood flow set how much blood is cleaned. Time sets for how long. The dialysate potassium sets how fast potassium falls, and how low. Sodium affects thirst and pressure. Bicarbonate corrects acid. Temperature affects pressure stability. The fluid goal sets the ultrafiltration rate (Module 5). Anticoagulation keeps the circuit from clotting.</p>
{{fig:cn06_order}}
<p>The potassium line shows why exact matching matters. In a case-control study of patients who had sudden cardiac arrest in United States dialysis clinics, a dialysate potassium below 2 mmol/L was associated with arrest.[[pun2011]] A bath of 1.0 instead of 2.0, picked by mistake, is not a small difference.</p>
"""),
        ("check", "Three-way check", "The three-way check", """
<p>Before connection, two people read the order aloud against the machine screen and the patient&rsquo;s identity and access. The four lines that most often differ are the dialysate potassium, the fluid goal, the time, and the anticoagulation. A check done by one person reading silently catches less, because the eye sees what it expects.</p>
{{scene:The bath that did not match|<p>Nurse Rhea Gonzales and the charge nurse read Bed 4&rsquo;s order aloud at 6:20. &ldquo;Potassium two.&rdquo; Rhea looks at the screen: the machine is set to 1.0, left over from the previous patient on that machine. They change it before connection and report it as a near miss. At the next huddle, the charge nurse asks everyone to reset the dialysate settings when a machine is turned over between patients.</p>}}
{{key:Read it aloud, two people, before the needle. Silent checks see what they expect.}}
"""),
        ("dose", "Dose", "The dose depends on delivered time", """
<p>The National Kidney Foundation Kidney Disease Outcomes Quality Initiative (KDOQI) recommends a target spKt/V of 1.4 per thrice-weekly session, with a minimum delivered of 1.2.[[hn_kdoqi2015]] The Hemodialysis (HEMO) Study randomized patients to a higher or a standard dose and found that the higher dose did not improve survival.[[hn_eknoyan2002]] The lesson is not &ldquo;more is always better.&rdquo; It is that falling below the standard dose is harm.</p>
<p>In the international Dialysis Outcomes and Practice Patterns Study (DOPPS), shortening sessions was associated with higher mortality, and missing sessions with more.[[hn_saran2003]] These findings are observational: patients who shorten may differ in other ways. The direction is consistent, and the mechanism is simple: less time, less cleaning, faster fluid removal.</p>
"""),
        ("minutes", "Lost minutes", "Where the minutes go", """
<p>Late starts, early stops, and alarm pauses all subtract. Ten minutes a session is thirty minutes a week, about twenty-six hours a year: more than six full four-hour sessions. The unit sees these losses only if someone counts them.</p>
{{fig:cn06_minutes}}
<p>Put the end time on the board and count minutes lost per chair at each shift. Minutes added back at the end are not lost. Minutes not given back are dialysis that never happened, whatever the record says (Module 17).</p>
"""),
        ("stop", "Early stops", "The patient who wants to stop early", """
<p>A request to stop early is a symptom, not a personality. Cramps, low pressure, a wet catheter dressing, a job, a ride that leaves at 10:00, depression, and boredom each have different answers. Ask why, tell the patient what the lost minutes mean in plain words, tell the physician, and record the reason and the minutes.</p>
<p>A signed refusal form records a decision. It does not end the problem, and it does not protect the patient. If the reason is fixable, fix it.</p>
{{scene:The 10:00 tricycle|<p>Mr. Romeo Salazar, 49, comes off twenty minutes early every Wednesday. The charge nurse asks why. His neighbor drives the tricycle to the market at 10:15 and is his only ride home. She asks the head nurse whether he can move to the 5:30 slot on Wednesdays. He can. His Wednesday sessions are now full length, and no form was needed.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The lost minutes.</strong> Prescribed: 240 minutes &times; 12 sessions = 2,880 minutes a month. Delivered: 205 minutes on average &times; 12 = 2,460 minutes. Lost: 420 minutes, about 1.75 sessions a month, or about 21 sessions a year (Toolkit #c4).</p>
<p><strong>Behind the early stops.</strong> Her cramps happen in the last hour on days when she arrives 3.5 kilograms over. Removing 3.5 liters in four hours from a 55-kilogram woman is about 15.9 mL/kg/h, above 13. Fast removal causes cramps; cramps cause early stops; early stops leave more fluid for next time. The low Kt/V follows from the lost minutes and alarm pauses.</p>
<p><strong>What the charge nurse does.</strong> She asks the attending nephrologist to review the dry weight and fluid targets and whether a longer or extra session is needed. She refers Mrs. Lim to the dietitian for salt and fluid advice. She asks about her travel and work, and checks the access for the cause of the alarm pauses. She starts counting minutes on the board. The refusal form stays in the chart, but it is not where the story ends.</p>
"""],
    "skills": {"title": "Order, machine, minutes",
               "intro": "Run the three-way check on five connections and audit one week of delivered time for one pod.",
               "items": [
                   ("Explains four order lines in physiologic terms.", False),
                   ("Runs a two-person, read-aloud check before every connection observed.", True),
                   ("Stops and corrects a mismatch before connection and reports it as a near miss.", True),
                   ("Calculates minutes lost per patient per month.", False),
                   ("Asks for the reason before accepting an early stop.", True),
                   ("Records the reason, minutes, and the physician notified.", True),
                   ("Proposes one fix for a recurring reason (transport, cramps, alarms).", False),
               ],
               "placement": "For one week, record prescribed and delivered minutes for every patient in one pod and present the losses at the huddle."},
    "quiz": [
        ("What is the KDOQI target spKt/V per thrice-weekly session?",
         ["1.0", "1.2", "1.4", "2.0"], 2,
         "With a minimum delivered of 1.2."),
        ("What did the HEMO Study show about a higher-than-standard dose?",
         ["It improved survival", "It did not improve survival", "It increased deaths", "It was not tested"], 1,
         "Below standard is harm; above standard did not add benefit."),
        ("Ten minutes lost per session over a year is about:",
         ["2 hours", "26 hours", "100 hours", "6 hours"], 1,
         "More than six full four-hour sessions."),
        ("A dialysate potassium below 2 mmol/L was associated with:",
         ["Better survival", "Sudden cardiac arrest", "Cramps only", "Nothing"], 1,
         "Exact matching of the bath matters."),
        ("The three-way check compares:",
         ["Order, machine, and patient", "Order, chart, and bill", "Machine, water, and cart", "Nurse, physician, and technician"], 0,
         "Read aloud, two people, before connection."),
        ("A signed refusal form:",
         ["Ends the matter", "Records a decision; the cause still needs action", "Is not needed", "Replaces telling the physician"], 1,
         "Find the reason and fix what can be fixed."),
        ("In DOPPS, shortened sessions were:",
         ["Protective", "Associated with higher mortality", "Unrelated to outcomes", "Proven harmless"], 1,
         "Observational, but consistent."),
        ("Which lines most often differ between order and machine?",
         ["Patient name only", "Potassium, fluid goal, time, anticoagulation", "Dialyzer color", "Chair number"], 1,
         "Check these four aloud every time."),
        ("Mrs. Lim loses 35 minutes per session, 12 sessions a month. How much is that?",
         ["120 minutes", "420 minutes", "35 minutes", "4,200 minutes"], 1,
         "35 &times; 12 = 420 minutes, about 1.75 sessions."),
        ("Why does a silent single check miss errors?",
         ["It is too slow", "The eye sees what it expects", "Machines hide numbers", "It is not allowed"], 1,
         "Reading aloud forces each value to be seen."),
        ("What lowers the real dose even when the screen shows the right blood flow?",
         ["Recirculation in the access", "A clean dialyzer", "A full session", "A correct bath"], 0,
         "Cleaned blood returning to the arterial needle is cleaned again."),
        ("A patient stops early every Wednesday because of her ride. Best action?",
         ["Shorten every session", "Change the slot or arrange transport", "Ignore it", "Discharge her"], 1,
         "Fix the reason, not the minutes."),
        ("Cramps in the last hour on high-gain days suggest:",
         ["Low potassium only", "Fast fluid removal", "A bad dialyzer", "Anxiety"], 1,
         "Ask the physician to review the fluid plan."),
        ("Minutes added back at the end of the session are:",
         ["Lost", "Not lost", "Not allowed", "Counted twice"], 1,
         "Count only minutes not given back."),
        ("A machine turned over between patients still shows the last bath. What prevents this?",
         ["Hoping", "Resetting dialysate settings at turnover and the read-aloud check", "Using one bath for all", "Faster turnover"], 1,
         "Two layers: reset, then check."),
    ],
    "terms": [("Dialysate", "The dialysis fluid on the other side of the membrane."),
              ("Three-way check", "Order, machine, and patient compared aloud before connection."),
              ("Kt/V", "A measure of the dose of dialysis."),
              ("Delivered time", "Minutes actually spent on the machine with blood flowing."),
              ("Recirculation", "Cleaned blood returning straight to the arterial needle.")],
    "readings": [("dialysis-adequacy.html", "How the dose of dialysis is measured and why it matters."),
                 ("dialysis-prescription.html", "The parts of a hemodialysis prescription."),
                 ("dialysis-cramps-stasis-pigmentation.html", "Why cramps happen during dialysis.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c4", "calc-dialysis-adequacy-ktv.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
