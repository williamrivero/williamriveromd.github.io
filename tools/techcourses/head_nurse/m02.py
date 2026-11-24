# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 02: Reading Trends Across Sessions. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse reviewing a weight and blood pressure trend on a tablet beside a patient being weighed before dialysis.",
    "objectives": [
        "Explain what builds up between sessions, and why the first session after the weekend carries the most risk.",
        "Explain why removing fluid faster than the tissues can refill the blood lowers blood pressure.",
        "Calculate interdialytic weight gain and the fluid removal rate, and say what each number means.",
        "Sort a pre-dialysis finding into Now, Today, or This month, and act at the right speed.",
        "Summarize what the evidence shows about missed sessions, fast fluid removal, and low pressure during dialysis.",
        "Close a critical result loop so that a named person owns the next step.",
    ],
    "big": """
{{plain:A healthy kidney adjusts all day, like a thermostat. Thrice-weekly dialysis adjusts in three short bursts, like switching on the air conditioner for four hours and off for forty-four. Between bursts, everything the kidney would have cleared builds up.}}
<p>The picture has a limit. A room tolerates fast cooling. A patient does not tolerate fast fluid removal, because water leaves the blood faster than the tissues can refill it.</p>
{{cards:Key terms for this module|Interdialytic weight gain (IDWG)::Weight gained between the end of one session and the start of the next. Almost all of it is water.|Dry weight::The target weight at the end of a session, set by the attending nephrologist.|Ultrafiltration (UF)::Removal of water from the blood by pressure across the dialyzer membrane.|UF rate::Fluid removed per hour per kilogram of body weight, in mL/h/kg.|Plasma refilling::Movement of water from the tissues back into the blood vessels as the machine removes it.|Nadir pressure::The lowest systolic pressure recorded during a session.|Critical result::A laboratory value that needs a clinician&rsquo;s decision within a set time under the unit&rsquo;s policy.}}
""",
    "case": {"title": "Monday, station 9", "html": """
<p>Mrs. Teresita Villanueva, 58, dialyzes on Mondays, Wednesdays, and Fridays through a left forearm fistula. She missed Friday because her son&rsquo;s tricycle broke down. Today she says she could not lie flat last night and her heart &ldquo;keeps jumping.&rdquo; Her weight is 3.4 kilograms above her dry weight of 60 kilograms, about what she usually gains over a weekend.</p>
<p>In the chart, a potassium result from Thursday&rsquo;s routine blood test is flagged critical. There is no note that anyone called a physician about it. Her daughter asks, &ldquo;She missed Friday. Can she just stay an hour longer today?&rdquo;</p>
""", "questions": ["Which lane does this belong in, and what do you do first?",
                  "Why is her near-usual weight gain not reassuring?",
                  "What does the daughter&rsquo;s request need before anyone answers it?"]},
    "sections": [
        ("drift", "What builds up", "What builds up between sessions", """
<p><strong>Water and salt.</strong> Without urine, every glass of water and every salty meal stays in the body. It goes first into the blood, then into the tissues. Blood pressure rises, then the pressure in the lung capillaries. Breathlessness when lying flat is fluid until proven otherwise, even when the scale looks familiar. A patient who has lost muscle during an illness is overloaded at an unchanged dry weight, because the dry weight no longer fits the body.</p>
<p><strong>Potassium.</strong> Almost all potassium removal now depends on dialysis. The level rises across the gap and peaks before the first session of the week. A missed session, potassium-rich food, constipation, and acidosis push it higher. A high potassium makes the heart&rsquo;s electrical system unstable. It may cause weakness or palpitations, or nothing at all, before an arrhythmia.</p>
{{fig:hn02_sawtooth}}
<p>The long gap shows up in deaths. In a large United States cohort of patients on thrice-weekly dialysis, all-cause mortality on the day after the two-day gap was 22.1 per 100 person-years, against 18.0 on other days. Deaths from cardiac causes and admissions for heart attack were also higher.[[hn_foley2011]] This is an observational finding, but it is large, consistent, and fits the physiology.</p>
<p>Missing a session makes it worse. In the international Dialysis Outcomes and Practice Patterns Study (DOPPS), missed sessions were associated with 68% higher mortality. The risk of missing ranged from under 1% in Italy and Japan to 24% in the United States, and longer travel time and depressive symptoms predicted it.[[hn_alsalmi2018]] A fiftyfold difference between countries means that much of the problem lies in systems, not in patients. Module 9 returns to this.</p>
{{key:Monday is the most dangerous day of the week for a Monday-Wednesday-Friday patient, and the patient who missed Friday is the most dangerous patient on Monday.}}
"""),
        ("refill", "Removal and refill", "Why fast fluid removal drops the pressure", """
<p>The machine removes water only from the blood. The tissues must refill the blood as it goes. Refilling has a speed limit, and the limit differs between patients. When removal outruns refilling, blood volume falls, the heart fills less, and the pressure drops. The patient yawns, cramps, feels sick, or goes quiet.</p>
{{fig:hn02_refill}}
<p>The body defends itself by tightening the vessels and speeding the heart. Many dialysis patients have weaker defenses: diabetic nerve damage, a thick or stiff heart, or blood pressure tablets taken that morning. Module 7 covers what happens when the defenses fail.</p>
<p>Repeated drops in pressure may injure the heart and gut over time. Imaging studies show parts of the heart muscle working less well during sessions. This link between repeated episodes and lasting damage is a reasonable hypothesis, not a proven chain.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Data</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Fast fluid removal</td><td>Above 13 mL/h/kg, compared with 10 or less, was associated with 59% higher all-cause and 71% higher cardiovascular mortality. Risk began to rise above 10[[hn_flythe2011]]</td><td>Observational data from a trial cohort. Large weight gains may explain part of it</td></tr>
<tr><td>Low pressure during dialysis</td><td>A nadir systolic below 90 mm Hg was the definition most strongly associated with death. If the session started at 160 or more, below 100 was[[hn_flythe2015]]</td><td>Observational</td></tr>
<tr><td>Recovery time</td><td>One patient in ten needed more than 12 hours to recover after a session. Longer recovery was associated with greater weight loss during dialysis, hospital admission, and death[[hn_rayner2014]]</td><td>Observational</td></tr>
<tr><td>Lung ultrasound to guide dry weight</td><td>In a trial of 367 high-risk patients, it cleared more lung congestion but did not reduce death, heart attack, or heart failure (hazard ratio 0.88; 95% confidence interval 0.63 to 1.24)[[hn_zoccali2021]]. A smaller trial showed smaller heart chambers[[hn_loutradis2022]]</td><td>Randomized. Benefit shown on images, not on outcomes patients feel</td></tr>
</tbody></table></div>
<p>No trial has shown that capping the fluid removal rate at any number saves lives. The numbers 10 and 13 are flags for a conversation with the nephrologist, not limits for the nurse to enforce.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> UF rate = fluid to remove (mL) &divide; hours &divide; weight (kg).<br>3,400 mL over 4 hours in a 60-kg patient = about 14 mL/kg/h. The same 3,400 mL over 3 hours = about 19 mL/kg/h.}}
"""),
        ("lanes", "Three lanes", "Sort every finding into a lane", """
<p>A pre-dialysis assessment produces many findings. The skill is to decide how fast each one needs action.</p>
{{fig:hn02_lanes}}
<div class="table-wrap"><table>
<thead><tr><th>Lane</th><th>Examples</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Now</td><td>New breathlessness at rest, chest pain, confusion, palpitations or weakness after a missed session, a critical result with no documented call</td><td>Assess at once. Call the physician. Do not connect on the old order until the physician has seen the patient or given an order</td></tr>
<tr><td>Today</td><td>Weight gain well above the patient&rsquo;s usual, a planned UF rate above 13 mL/h/kg, a nadir below 90 mm Hg last session, a change in the access</td><td>Raise it before connection. Longer time, an extra session, or a new dry weight are the prescriber&rsquo;s options</td></tr>
<tr><td>This month</td><td>Hemoglobin drifting, phosphate rising, albumin falling, recovery time lengthening, two shortened sessions</td><td>Add it to the monthly review list with an owner</td></tr>
</tbody></table></div>
<p>The thresholds for &ldquo;Now&rdquo; follow your unit&rsquo;s protocol. Where the protocol is silent, ask the attending nephrologist.</p>
<p>For anemia, the KDIGO 2026 guideline replaced the 2012 edition. For patients on hemodialysis, it suggests weighing the benefits and risks of starting an erythropoiesis-stimulating agent when hemoglobin is 9 to 10 g/dL or below, once iron deficiency and other causes are addressed, and pausing intravenous iron during active infection.[[hn_kdigo_anemia2026]] Use your unit&rsquo;s adopted targets for maintenance ranges.</p>
{{call:Stop and call the physician on duty or the attending nephrologist at once for any Now finding. Do not connect on the existing order until a physician has decided. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("loop", "Closing the loop", "Closing a result loop", """
<p>A critical result that nobody acted on is one of the most common ways patients are harmed between sessions. The result exists. The decision does not.</p>
{{fig:hn02_loop}}
{{flow:A closed loop|Received::The result reaches a named nurse, with the time.|Told::A named physician hears the value, the time it was taken, and the clinical context. Ask for a read-back.|Decided::The physician gives an order or a plan.|Recorded::The order, the time, and who gave it are written down.|Owned::A named person is responsible for the next step: a repeat test, a change in the prescription, a call to the patient.}}
<p>Check the context before calling. A potassium from a hemolyzed sample, or one drawn after a long tourniquet, may be falsely high. Report it anyway, with that context. The physician decides whether to repeat it.</p>
<p>Two questions belong in every monthly review. &ldquo;How long does it take you to recover after a session?&rdquo; and &ldquo;What symptom bothers you most?&rdquo; The first has outcome data behind it.[[hn_rayner2014]]</p>
{{key:A loop is closed when a named person owns the next step. Until then, it is open, however many people have seen the result.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which lane, and what first?</strong> Now. She missed Friday, so her last session was Wednesday. She has breathlessness lying flat, palpitations, and an open critical potassium. Each of these alone would be urgent. Together, with the long gap, they are the picture Module 2 warns about. Seat her upright, put her on the monitor if your unit has one, take her pulse yourself, and call the physician on duty now. Give the facts in order: missed Friday, symptoms and when they started, the vital signs, the critical potassium and the date it was drawn, and her current prescription.</p>
<p><strong>Why is the weight not reassuring?</strong> Her gain is close to her usual weekend gain, but her weekend was five days, not three. If she gained the same amount over a longer gap, she may have been eating little, which can also mean she is losing muscle and her dry weight is now too high. Breathlessness lying flat tells you more than the scale does.</p>
<p><strong>The daughter&rsquo;s request.</strong> Her instinct is sensible: more time does remove more. But how long, how fast, and with which dialysis fluid potassium are the prescriber&rsquo;s decisions. Removing a large potassium load quickly carries its own risk of arrhythmia, which Module 7 explains. Thank her, tell her the doctor is deciding now, and come back to the broken tricycle once the acute risk is handled. That is a Module 9 conversation.</p>
"""],
    "skills": {"title": "Pre-dialysis trend review and SBAR call",
               "intro": "Review three synthetic patients before a shift, sort the findings, and make one call to a facilitator playing the physician.",
               "items": [
                   ("Calculates weight gain and the planned UF rate for each patient.", True),
                   ("Compares today&rsquo;s gain with the patient&rsquo;s own usual gain and the length of the gap.", False),
                   ("Asks about breathing, orthopnea, palpitations, and chest pain, and looks for edema.", True),
                   ("Sorts each finding into Now, Today, or This month and states why.", True),
                   ("Identifies any open critical result and its date.", True),
                   ("Delivers a one-minute SBAR call that states urgency first and asks for a specific decision.", True),
                   ("Obtains and records a read-back of the order.", False),
                   ("Names the owner of each pending result.", True),
                   ("Asks the recovery-time question and records the answer.", False),
                   ("Does not change the prescription or connect on the old order for a Now finding.", True),
               ],
               "placement": "For two weeks, list every patient arriving after a missed session and every planned UF rate above 13 mL/h/kg. Note what was done and who decided. Review the list with your facilitator."},
    "quiz": [
        ("For a Monday-Wednesday-Friday patient, on which day is mortality highest?",
         ["Wednesday", "Friday", "Monday, after the two-day gap", "No difference"], 2,
         "In the Foley cohort, deaths were higher on the day after the long interval."),
        ("Why is breathlessness when lying flat important even when the weight gain looks usual?",
         ["It is usually anxiety", "It suggests fluid in the lungs, and dry weight may no longer fit the body", "It only matters in heart failure", "It means the scale is wrong"], 1,
         "A patient who has lost muscle can be overloaded at an unchanged dry weight."),
        ("A 60-kg patient needs 3,400 mL removed in 4 hours. What is the UF rate?",
         ["About 8 mL/kg/h", "About 14 mL/kg/h", "About 19 mL/kg/h", "About 57 mL/kg/h"], 1,
         "3,400 &divide; 4 &divide; 60 = 14.2."),
        ("The same patient wants to leave after 3 hours with the same goal. What happens to the rate?",
         ["It falls", "It stays the same", "It rises to about 19 mL/kg/h", "It doubles to 28"], 2,
         "Less time for the same fluid means faster removal."),
        ("What did Flythe and colleagues find for UF rates above 13 mL/kg/h?",
         ["No association with outcomes", "An association with higher all-cause and cardiovascular mortality", "Proof that capping the rate saves lives", "Lower blood pressure only"], 1,
         "The study was observational. No trial has shown that a cap saves lives."),
        ("In DOPPS, the four-month risk of missing a session ranged from under 1% to 24% between countries. What does this suggest?",
         ["Patient character explains it", "Systems such as transport and scheduling drive much of it", "Missing has no consequences", "The data are unreliable"], 1,
         "A fiftyfold difference between countries points to systems."),
        ("Which nadir pressure definition was most strongly associated with death?",
         ["Any fall with cramps", "A nadir systolic below 90 mm Hg", "Any episode needing saline", "A fall of 10 mm Hg"], 1,
         "Definitions built on symptoms or interventions were not associated with death."),
        ("Why does water removal faster than refilling lower the pressure?",
         ["The heart pumps harder", "Blood volume falls because the tissues cannot refill the blood fast enough", "The dialysis fluid is too cold", "Potassium rises"], 1,
         "The machine removes water only from the blood."),
        ("What did the lung ultrasound outcome trial show?",
         ["Fewer deaths", "More lung congestion cleared, but no reduction in death or major cardiac events", "Harm from ultrasound", "Shorter sessions"], 1,
         "The benefit was seen on images, not on outcomes patients feel."),
        ("A patient missed Friday, has palpitations, and has a critical potassium with no documented call. Which lane?",
         ["This month", "Today", "Now", "No lane, routine care"], 2,
         "Each finding alone is urgent. Together they are a Now finding."),
        ("What closes a critical result loop?",
         ["The result is printed", "A named recipient acknowledges it, a decision is recorded, and follow-up has an owner", "The patient is told", "It is filed in the chart"], 1,
         "Until someone owns the next step, the loop is open."),
        ("Hemoglobin has drifted from 10.8 to 9.9 g/dL over three months. Which lane?",
         ["Now", "Today", "This month", "None"], 2,
         "It is a trend for the monthly review with the nephrologist."),
        ("Which question has outcome data behind it as a routine check?",
         ["Do you like the unit?", "How long does it take you to recover after a session?", "Did you sleep well?", "Do you have questions?"], 1,
         "Longer recovery was associated with hospitalization and death in DOPPS."),
        ("A family member asks for an extra hour after a missed session. Who decides?",
         ["The head nurse", "The family", "The prescriber", "The nurse at the chair"], 2,
         "Time, rate, and dialysis fluid are part of the prescription."),
        ("Why should a potassium from a hemolyzed sample still be reported?",
         ["It is always accurate", "The physician decides whether to repeat it, with the context given", "Reporting is optional", "It replaces the next test"], 1,
         "Report the value with its context. Do not decide alone that it is false."),
    ],
    "terms": [("Interdialytic weight gain", "Weight gained between the end of one session and the start of the next."),
              ("Dry weight", "The target weight at the end of a session, set by the attending nephrologist."),
              ("Ultrafiltration rate", "Fluid removed per hour per kilogram of body weight."),
              ("Plasma refilling", "Movement of water from the tissues back into the blood vessels during dialysis."),
              ("Nadir pressure", "The lowest systolic pressure recorded during a session."),
              ("Orthopnea", "Breathlessness when lying flat."),
              ("Critical result", "A laboratory value that needs a clinician&rsquo;s decision within a set time."),
              ("SBAR", "A four-part way to report: Situation, Background, Assessment, Recommendation.")],
    "readings": [("dry-weight-determination.html", "How dry weight is judged and when it should be reassessed."),
                 ("fluid-management-dialysis.html", "Salt and fluid advice that reduces weight gain between sessions."),
                 ("hemodialysis-complications.html", "The main complications of a session.")],
    "calcs": ["calc-idwg-fluid.html", "calc-ufr-ceiling.html", "calc-dialysis-head-nurse-toolkit.html#c2"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
