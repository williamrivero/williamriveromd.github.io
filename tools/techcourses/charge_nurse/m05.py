# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 05: Sorting Risk Before Connection. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse weighing an older man before dialysis while the charge nurse reviews a trend on a tablet beside them.",
    "objectives": [
        "Explain why the first session after the two-day gap carries the most risk.",
        "Sort each pre-dialysis finding into Now, Today, or This month, and act at the right speed.",
        "Calculate the ultrafiltration rate in mL/kg/h and explain why a high rate matters.",
        "Read weight, pressure, and laboratory trends rather than single values.",
        "Identify patients at risk of falls and of low blood sugar before connection.",
        "Close the loop on a critical result so that a named person owns the next step.",
    ],
    "big": """
{{plain:A working kidney is a water treatment plant that runs day and night. Dialysis is a truck that comes three times a week and hauls everything away at once. Between visits, water, salt, potassium, and acid pile up.}}
<p>The truck picture explains the sawtooth pattern: levels climb between sessions and fall during them. It hides one thing. The truck can only take away what has reached the blood. In chronic kidney disease (CKD) stage 5, there is little or no other exit. Fluid sitting in the tissues has to move back into the blood vessels before the machine can remove it. Take too much, too fast, and the blood empties faster than the tissues can refill it. That is why the assessment before connection decides how hard the session can push.</p>
{{cards:Key terms for this module|Interdialytic weight gain (IDWG)::Weight gained between the end of one session and the start of the next; almost all of it is water.|Dry weight::The target weight at the end of a session, set by the attending nephrologist.|Ultrafiltration (UF)::Removal of water from the blood across the dialyzer membrane.|Ultrafiltration rate (UFR)::Fluid removed per hour per kilogram of body weight, in mL/kg/h.|Orthopnea::Breathlessness when lying flat.|Critical result::A laboratory value that needs a clinician&rsquo;s decision within a set time under unit policy.}}
""",
    "case": {"title": "Monday, 4.1 kilograms", "html": """
<p>Mr. Danilo Reyes, 67, has diabetes and heart failure. He dialyzes Monday, Wednesday, and Friday. On Monday at 6:00 his weight is 4.1 kilograms above his dry weight of 62 kilograms. His pressure is 168/94. He tells the nurse he slept on two pillows instead of one.</p>
<p>His Friday potassium, reported on Saturday, was 6.4 mmol/L. There is no note that anyone called a physician. The staff nurse plans to remove the full 4.1 liters in four hours. The charge nurse, Grace Valdez, is reviewing the floor before the first connections.</p>
""", "questions": ["Which findings belong in the Now lane?",
                  "What is the planned ultrafiltration rate, and why does it matter?",
                  "Who owns the potassium result, and what does Grace say on the phone?"]},
    "sections": [
        ("gap", "The long gap", "Why Monday is the riskiest day", """
<p>In a large United States cohort of patients on thrice-weekly dialysis, all-cause mortality on the day after the two-day gap was 22.1 per 100 person-years, against 18.0 on other days. Cardiac deaths and admissions for heart attack were also higher.[[hn_foley2011]] The study is observational, but the mechanism fits: the most water and potassium of the week, and the longest time for both to build.</p>
{{fig:cn05_sawtooth}}
<p>So Monday and Tuesday mornings deserve the slowest, most careful look before connection. The patient who also missed Friday is the riskiest patient of the week.</p>
"""),
        ("lanes", "Three lanes", "Now, Today, This month", """
<p>Sort every finding by how fast someone must decide.</p>
{{fig:cn05_lanes}}
<div class="table-wrap"><table>
<thead><tr><th>Lane</th><th>Examples</th><th>What you do</th></tr></thead>
<tbody>
<tr><td><strong>Now</strong></td><td>New breathlessness or orthopnea; chest pain or palpitations; new confusion; a potassium above the unit&rsquo;s critical value with no documented plan; fever or chills with a catheter; a cold, pale, or painful access hand</td><td>Call the physician before connection</td></tr>
<tr><td><strong>Today</strong></td><td>Weight gain above the unit&rsquo;s threshold; pressure well above or below the patient&rsquo;s usual; missed medicines; a fall since the last session; insulin taken without breakfast</td><td>Tell the physician during this session</td></tr>
<tr><td><strong>This month</strong></td><td>A weight slowly rising over weeks; poor appetite; low mood; transport or money problems</td><td>Route to the attending nephrologist or the team</td></tr>
</tbody></table></div>
<p>The thresholds for potassium, weight gain, and pressure are your unit&rsquo;s. The lanes are about speed, not about who is to blame.</p>
"""),
        ("speed", "Speed of removal", "Fluid and the speed of removal", """
<p>An ultrafiltration rate above 13 mL/kg/h, compared with 10 or less, was associated with 59% higher all-cause and 71% higher cardiovascular mortality in a cohort drawn from a large trial.[[hn_flythe2011]] Imaging studies show parts of the heart muscle working less well during sessions with large or fast fluid removal, a finding called myocardial stunning.[[burton2009]]</p>
{{fig:cn05_ufr}}
<p>Both findings are observational. No trial has shown that capping the rate at any number saves lives, which is why the attending nephrologist, not the nurse, sets the plan. The charge nurse&rsquo;s job is to notice when the planned rate is high and to ask before connection, not after the pressure falls.</p>
{{formula:<strong>Ultrafiltration rate</strong> = fluid to remove (mL) &divide; hours &divide; dry weight (kg).<br>Example: 3,000 mL over 4 hours in a 60-kg patient = 3,000 &divide; 4 &divide; 60 = 12.5 mL/kg/h.}}
{{scene:Same fluid, different patients|<p>Two patients on the same shift each need 3,000 mL removed over four hours. Mrs. Lourdes Navarro weighs 45 kilograms; Mr. Eduardo Salcedo weighs 80. For Mrs. Navarro, 3,000 &divide; 4 &divide; 45 = about 17 mL/kg/h. For Mr. Salcedo, 3,000 &divide; 4 &divide; 80 = about 9 mL/kg/h. The same number on the screen is a very different demand on two hearts. The charge nurse flags Mrs. Navarro to the physician before connection.</p>}}
"""),
        ("trends", "Trends", "Trends, not snapshots", """
<p>A weight gain of 3 kilograms is routine for one patient and alarming for another. A potassium of 5.8 that has been 5.7 for months differs from 5.8 after 4.6 last month. Look at the last three sessions and the last two laboratory sets before you decide what a number means.</p>
<p>Watch for two patterns. A pre-dialysis weight creeping up with a post-dialysis pressure creeping down can mean the dry weight is now set too low, or that the patient is gaining flesh. A patient who has lost muscle after an illness may be overloaded at an unchanged dry weight, because the same weight now carries more water. Both are Today findings for the physician.</p>
"""),
        ("falls", "Falls and glucose", "Falls and low blood sugar", """
<p>Older patients on hemodialysis fall often. In a prospective cohort of patients aged 65 and older, there were 1.60 falls per person-year, nearly half fell at least once, and 19% of falls caused injury.[[cn_cook2006]] Risk is highest just after the session, when pressure is lowest (Module 7).</p>
{{fig:cn05_falls}}
<p>Glucose falls during dialysis too. In a 2026 study that used continuous glucose monitoring in 40 adults with insulin-treated diabetes, mean glucose fell 32% during dialysis to its lowest point at about two hours, and 20% of participants had low blood sugar during a session.[[cn_liarakos2026]] Before connection, ask every patient on insulin or a sulfonylurea two questions: &ldquo;Did you take your diabetes medicine today?&rdquo; and &ldquo;What did you eat?&rdquo;</p>
"""),
        ("loop", "Closing the loop", "Closing the loop on a result", """
<p>A critical result is closed only when five links hold: received, told to a physician, decided, recorded, and owned (who does what next, by when). Mr. Reyes&rsquo;s potassium broke at the second link. Nobody did anything wrong on purpose; the result arrived on a Saturday and no named person owned it.</p>
{{key:If a result does not have a named owner, it belongs to the charge nurse until it does.}}
"""),
    ],
    "debrief": ["""
<p><strong>The Now lane.</strong> Orthopnea and an unaddressed potassium of 6.4 after the long gap. Either one alone is a Now finding.</p>
<p><strong>The planned rate (Toolkit #c7).</strong> 4.1 liters over four hours is 1,025 mL per hour. Divided by the dry weight of 62 kilograms, that is 16.5 mL/kg/h, above the 13 associated with harm. At four hours, the most that stays at or below 13 is 13 &times; 62 &times; 4 = 3,224 mL. Options for the attending: remove about 3.2 liters today and see him again tomorrow, extend the session (4.1 liters over five hours is about 13.2 mL/kg/h), or something else the physician decides. Grace presents the numbers; the physician chooses.</p>
<p><strong>The call.</strong> Before connection, Grace calls the physician on duty: &ldquo;Mr. Reyes, 67, Monday after the long gap, up 4.1 kilograms, slept on two pillows, pressure 168/94. Friday potassium was 6.4 with no documented plan. The planned rate is 16.5 mL/kg/h. I need a decision on the fluid goal, and whether you want a repeat potassium and an electrocardiogram (ECG) before we start.&rdquo; The physician orders both, sets the fluid goal, and extends the session. Grace records the decision and who owns the repeat potassium. She also asks the head nurse to fix how weekend results reach a named person.</p>
"""],
    "skills": {"title": "Pre-dialysis risk sort and Situation-Background-Assessment-Recommendation (SBAR) call",
               "intro": "Review three synthetic patients before a shift, sort the findings, calculate the rates, and make one call to a facilitator playing the physician.",
               "items": [
                   ("Sorts ten findings into Now, Today, and This month, and explains why.", True),
                   ("Calculates the ultrafiltration rate in mL/kg/h for each patient.", True),
                   ("Identifies the long-gap session and the patient who missed a session.", False),
                   ("Compares today&rsquo;s values with the patient&rsquo;s own trend.", False),
                   ("Asks about diabetes medicine and food before connection.", True),
                   ("Screens for fall risk and plans help at disconnection.", False),
                   ("Makes an SBAR (Situation, Background, Assessment, Recommendation) call that asks for a specific decision.", True),
                   ("Does not connect on the old plan while a Now finding is unresolved.", True),
                   ("Records who owns each pending result.", True),
               ],
               "placement": "For two weeks, list every Monday patient with a planned rate above 13 mL/kg/h or an open critical result, and what was decided."},
    "quiz": [
        ("For a Monday-Wednesday-Friday patient, mortality was highest on:",
         ["Wednesday", "The day after the two-day gap", "Saturday", "No difference"], 1,
         "Monday, after the long gap, in the Foley cohort."),
        ("What is the ultrafiltration rate for 3 liters over 4 hours in a 60-kg patient?",
         ["10.0", "12.5", "15.0", "7.5 mL/kg/h"], 1,
         "3,000 &divide; 4 &divide; 60 = 12.5."),
        ("A rate above 13 mL/kg/h was:",
         ["Proven harmful in a trial", "Associated with higher mortality in a cohort", "Protective", "Irrelevant"], 1,
         "Observational; no trial has proven a cap."),
        ("Orthopnea before dialysis belongs in which lane?",
         ["This month", "Today", "Now", "None"], 2,
         "Call before connection."),
        ("When is a result loop closed?",
         ["When the slip is filed", "When a named person owns the next step", "When the patient is told", "When it is repeated"], 1,
         "Received, told, decided, recorded, owned."),
        ("Older patients on hemodialysis fell about how often in the cohort?",
         ["0.2 times per person-year", "1.6 times per person-year", "5 times per person-year", "Never"], 1,
         "Nearly half fell at least once."),
        ("In the glucose monitoring study, glucose during dialysis:",
         ["Rose", "Fell about a third, lowest about two hours in", "Did not change", "Fell only at the end"], 1,
         "And 20% of participants had low blood sugar during a session."),
        ("Who sets the fluid goal?",
         ["The charge nurse", "The attending nephrologist or physician on duty", "The technician", "The family"], 1,
         "The nurse presents the numbers; the prescriber decides."),
        ("The same 3 liters over 4 hours in a 45-kg patient is about:",
         ["9 mL/kg/h", "13 mL/kg/h", "17 mL/kg/h", "25 mL/kg/h"], 2,
         "3,000 &divide; 4 &divide; 45 = 16.7."),
        ("A potassium of 5.8 after 4.6 last month is:",
         ["Reassuring", "A change worth reporting today", "Ignored", "Normal for all patients"], 1,
         "Trends matter more than single values."),
        ("Which is a Today finding?",
         ["Chest pain", "Missed medicines", "Fever with a catheter", "Cold painful access hand"], 1,
         "The others are Now."),
        ("What two questions should a patient on insulin hear before connection?",
         ["Name and address", "Did you take your diabetes medicine today, and what did you eat?", "Where do you live and work?", "Who is your doctor?"], 1,
         "Low blood sugar during dialysis is common in this group."),
        ("A patient lost muscle during a hospital stay but returns at his old dry weight. What may be true?",
         ["He is perfectly dry", "He may be overloaded, because the same weight now carries more water", "His scale is broken", "Nothing has changed"], 1,
         "Dry weight must fit the body he has now."),
        ("Why is a long-gap patient who also missed Friday especially risky?",
         ["He is tired", "Five days of water and potassium have built up", "He is new", "He has no access"], 1,
         "The longest gap of all."),
        ("A result arrives with no named owner. Who owns it?",
         ["Nobody", "The charge nurse, until someone else does", "The patient", "The laboratory"], 1,
         "Unowned results are how loops break."),
    ],
    "terms": [("Interdialytic weight gain (IDWG)", "Weight gained between sessions."),
              ("Dry weight", "The target weight at the end of a session."),
              ("Ultrafiltration rate (UFR)", "Fluid removed per hour per kilogram, in mL/kg/h."),
              ("Orthopnea", "Breathlessness when lying flat."),
              ("Myocardial stunning", "Temporary weakness of parts of the heart muscle during dialysis."),
              ("Critical result", "A laboratory value that needs a clinician&rsquo;s decision within a set time.")],
    "readings": [("fluid-management-dialysis.html", "Salt and fluid advice that reduces weight gain between sessions."),
                 ("dry-weight-determination.html", "How dry weight is judged and reassessed."),
                 ("potassium-hyperkalemia-ckd.html", "High potassium: causes, risks, and treatment.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c7", "calc-ufr-ceiling.html", "calc-idwg-fluid.html", "calc-dialysis-charge-nurse-toolkit.html#c6"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
