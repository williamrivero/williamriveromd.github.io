# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 11: Learning From Incidents and Proving Improvement. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse leading a short huddle in front of a run chart taped to a wall in a dialysis unit.",
    "objectives": [
        "Separate the immediate response to an incident from the analysis that follows.",
        "Reconstruct what happened by asking what people saw, expected, and found hard, not why they failed.",
        "Rank corrective actions by how strongly they prevent the same slip reaching the next patient.",
        "Define an indicator in six parts and add a balancing measure.",
        "Read a run chart and react to signals, not single points.",
        "Run a small Plan-Do-Study-Act test and decide, from data, whether to adopt, adapt, or abandon.",
    ],
    "big": """
{{plain:Think of each safety layer in the unit as a slice of Swiss cheese: the order check, the second nurse, the alarm, the visible access, the water test. Each slice has holes. Harm happens when the holes line up.}}
<p>The picture has a known weakness. It can make every slice look equally strong. They are not. A barrier that physically prevents an error is stronger than a sign asking people to remember. The hierarchy in this module fixes that.</p>
{{fig:hn11_cheese}}
{{cards:Key terms for this module|Incident::An event that harmed, or could have harmed, a patient.|Near miss::An error caught before it reached the patient.|Forcing function::A design that makes the wrong action impossible.|Indicator::A defined measure tracked over time.|Balancing measure::A measure that watches for harm caused by the change itself.|Run chart::A plot of a measure over time with a median line.|PDSA::Plan-Do-Study-Act, a small test of a change.}}
""",
    "case": {"title": "The second mislabeled specimen", "html": """
<p>Twice in a month, a blood specimen drawn in the first busy hour of the morning shift was labeled with another patient&rsquo;s name. Both were caught by the laboratory before results were released. Staff point to one label printer shared by stations 1 to 4, at the end of the row.</p>
<p>You audit 60 label checks over two weeks and find 6 missing or wrong. The team tries a small change: labels printed and checked at the chair before the specimen leaves the patient&rsquo;s side. Over the next two weeks, 2 of 55 checks are missing or wrong.</p>
""", "questions": ["Did the change work?",
                  "What else should you be measuring?",
                  "Is there a stronger fix than a new checking step?"]},
    "sections": [
        ("respond", "Respond, then analyze", "Respond first, then reconstruct", """
<p>People make slips at a predictable rate, more under fatigue, interruption, and time pressure. Those are exactly the conditions of the first busy hour. Blaming the nurse who slipped removes one person and leaves the conditions. Designing the work so the slip cannot reach the patient protects every nurse who comes next.</p>
{{flow:From incident to fix|Respond::Care for the patient. Contain the hazard. Preserve equipment, lines, vials, logs, and the screen record. Report through the approved pathway.|Reconstruct::Build a timeline from records and short individual accounts.|Ask::What did you see? What did you expect? What made the safe action hard at that moment? Not &ldquo;why didn&rsquo;t you?&rdquo;|Find the conditions::Workload, interruptions, layout, equipment design, unclear orders, outdated documents, missing supervision. Most incidents have more than one.|Choose fixes::From the top of the hierarchy, each with an owner, a date, and a measure.}}
<p>Structured communication can reduce harm. A handoff program across nine hospitals was associated with medical errors falling from 24.5 to 18.8 per 100 admissions, and preventable adverse events from 4.7 to 3.3.[[hn_starmer2014]] A later rollout across 32 programs was associated with a 47% fall in reported handoff-related adverse events.[[hn_starmer2023]] These were before-and-after studies of resident physicians, not dialysis units. Applying them to dialysis handoffs is an inference.</p>
{{scene:Four interruptions|<p>A nurse gives a patient a heparin bolus twice: once at connection, and again ten minutes later. The patient is unharmed. The administrator&rsquo;s first question is whether the nurse should be suspended.</p>
<p>You reconstruct first. In the ten minutes after connection, the nurse was interrupted four times: a machine alarm at the next station, a relative asking about parking, a phone call from the laboratory, and a request to help lift a patient. The bolus was recorded on a sheet at the nurses&rsquo; station, not at the chair, so when she came back she could not see that it had been given. Suspending her would remove one nurse and leave the interruptions and the sheet in place. The fixes come from the conditions: record the bolus at the chair at the moment it is given, and protect the first ten minutes of each connection from non-urgent interruptions.</p>}}
"""),
        ("hierarchy", "Hierarchy of fixes", "Some fixes are stronger than others", """
{{fig:hn11_hierarchy}}
<div class="table-wrap"><table>
<thead><tr><th>Strength</th><th>Type</th><th>Dialysis example</th></tr></thead>
<tbody>
<tr><td>Strongest</td><td>Remove or force</td><td>The machine cannot start until the scanned order matches the settings. Different connector shapes for different concentrates</td></tr>
<tr><td>Strong</td><td>Standardize and simplify</td><td>One taping method for every needle. A label printer at each station</td></tr>
<tr><td>Intermediate</td><td>Check and double-check</td><td>Spoken read-back of the order against the screen. The opening-gate checklist</td></tr>
<tr><td>Weakest</td><td>Train, remind, warn</td><td>A memo. A poster. A retraining session</td></tr>
</tbody></table></div>
<p>Training is still needed to introduce a stronger fix. On its own, it fades within weeks. If every action from a review sits in the bottom row, the review is not finished.</p>
{{scene:Two boxes on one shelf|<p>A nurse sets up a dialyzer with a smaller surface area than the one ordered. The two sizes come in boxes of the same color and are stored side by side on the same shelf. The error is caught at the three-way check.</p>
<p>The first suggestion at the review is &ldquo;Remind staff to check the dialyzer size.&rdquo; That is training, the weakest fix, and it will fade. A stronger fix changes the setup: store the two sizes on different shelves, add a large colored label to each shelf, and list the dialyzer size on the station&rsquo;s printed order so it is read aloud at the check. Stronger still would be a supply process that delivers each patient&rsquo;s dialyzer to the station already matched to the order. The review is finished only when at least one fix sits above the bottom row.</p>}}
{{key:Ask of every corrective action: would this stop the same slip from reaching the next patient on a tired, busy morning?}}
"""),
        ("measure", "Measuring", "Defining an indicator", """
<p>Every indicator needs six things written down: the numerator, the denominator, what is included and excluded, the period, the data source, and the owner. Add one balancing measure for the harm the change might cause. A new check at the start of each session may delay starts, so measure start delays.</p>
<p>A hemodialysis program in China tracked intradialytic hypotension, circuit clotting, interdialytic weight control, catheter infection, and patient satisfaction over four years and used them to target improvement.[[hn_tang2026]] Pick a small set like this and keep the definitions fixed.</p>
{{formula:<strong>Rate with its uncertainty.</strong> 6 of 60 = 10.0% (95% confidence interval about 4.7% to 20.1%).<br>2 of 55 = 3.6% (about 1.0% to 12.3%).<br>The intervals overlap. The change is promising, not yet proven.}}
{{scene:The check that delayed every start|<p>To stop wrong prescriptions, the unit adds a second-nurse check at every connection. Prescription mismatches found at the check fall from three a month to none.</p>
<p>The balancing measure tells the rest of the story. The median delay between a patient sitting down and connection rises from 8 to 20 minutes, and patients on the first shift begin to finish late, which pushes the second shift later. The check was working, but at a cost the team had not planned for. The next test changes the timing: the second nurse checks the machine settings during priming, before the patient sits down. Mismatches stay at zero, and the delay falls to 10 minutes. Without the balancing measure, the unit would have declared success and created a new problem.</p>}}
"""),
        ("runchart", "Run charts", "Reading a run chart", """
{{fig:hn11_runchart}}
<p>Plot the measure over time with a median line. Do not react to one high or low point. React to a signal. Four probability-based rules tell a real signal from noise.[[hn_perla2011]]</p>
{{cards:Run chart signals|Shift::Six or more points in a row all above, or all below, the median. Points on the median are skipped.|Trend::Five or more points in a row all going up, or all going down.|Too few runs::The line crosses the median far less often than chance would predict.|Astronomical point::One value that everyone agrees is clearly different.}}
<p>Small samples move a lot by chance. Always show the denominator beside the rate.</p>
{{scene:One bad month|<p>The run chart of sessions with low pressure has a median of 11%. In March, the value is 18%. The administrator wants a new protocol by Friday.</p>
<p>One high point is not a signal. March had a holiday week, fewer sessions, and therefore a small denominator, so the rate swings more by chance. You show the denominator beside the rate and wait. April is 10%, May is 12%. Then, from June to November, six points in a row sit above the median. That is a shift, and it began the month the unit changed to a new brand of concentrate. Now there is something worth investigating, and the run chart tells you when to look.</p>}}
"""),
        ("pdsa", "Testing a change", "Testing small with Plan-Do-Study-Act", """
{{flow:One PDSA cycle|Plan::State the change, where, for how long, and your prediction. &ldquo;Printing and checking at the chair on stations 1 to 4 for two weeks will cut label errors by half.&rdquo;|Do::Run it on one station group or one shift.|Study::Compare the result with the prediction. Check the balancing measure.|Act::Adopt, adapt, or abandon. Then test on a larger scale.}}
<p>Bring the results to the quality meeting with the clinical head. Record each action with an owner and a due date, and return to test whether it worked. An action is closed only when the owner and the reviewer have recorded evidence that it worked, not when it was carried out.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Did it work?</strong> Possibly. The rate fell from 10.0% to 3.6%, but with 60 and 55 observations the confidence intervals overlap. Keep measuring weekly. Check that the definition of a failed check did not change between the two periods, and compare shifts.</p>
<p><strong>What else to measure.</strong> The balancing measure: start delays. If checking at the chair adds two minutes to every start, the afternoon shift may lose time it cannot afford (Module 3). Plot both measures on run charts.</p>
<p><strong>A stronger fix.</strong> The check is an intermediate fix. The underlying condition is a printer at the end of a row of four stations, which makes a nurse walk away from the patient between drawing and labeling. A printer at each station removes the walk and the mix-up it allows. That is a standardize-and-simplify fix, a step higher on the hierarchy. Assign an owner, a date, and a review.</p>
"""],
    "skills": {"title": "Run chart and action log",
               "intro": "Build a run chart from synthetic weekly data, then present a PDSA plan to your facilitator acting as the clinical head.",
               "items": [
                   ("Writes an indicator definition with numerator, denominator, inclusions, period, source, and owner.", True),
                   ("Adds a balancing measure.", True),
                   ("Plots the data with a median line and the denominators shown.", False),
                   ("Identifies any shift or trend correctly.", True),
                   ("States whether a before-and-after difference could be chance, with a reason.", True),
                   ("Ranks proposed fixes by the hierarchy.", True),
                   ("Writes a PDSA plan with a prediction.", False),
                   ("Assigns an owner and a review date for each action.", False),
                   ("States what evidence will close the action.", True),
               ],
               "placement": "Choose one measure from your unit. Plot it weekly for eight weeks, run one PDSA cycle, and present the result at the quality meeting."},
    "quiz": [
        ("Why is blaming the nurse who slipped not enough?",
         ["Nurses dislike it", "It removes one person and leaves the conditions that caused the slip", "It is illegal", "It takes too long"], 1,
         "Design the work so the slip cannot reach the patient."),
        ("Which question is best when reconstructing an incident?",
         ["Why didn&rsquo;t you check?", "What made the safe action hard at that moment?", "Who is to blame?", "Have you read the policy?"], 1,
         "The answer reveals the conditions."),
        ("Rank from strongest to weakest: retraining, a forcing function, a checklist.",
         ["Retraining, checklist, forcing function", "Forcing function, checklist, retraining", "Checklist, retraining, forcing function", "All are equal"], 1,
         "Remove or force, standardize, check, then train."),
        ("A review produces only a memo and a retraining session. What do you ask?",
         ["Nothing more", "What stronger fix would stop the same slip on a busy morning?", "Who will sign the memo?", "When is the next training?"], 1,
         "Weak fixes fade within weeks."),
        ("Baseline errors were 6 of 60 and after a test 2 of 55. What is the best conclusion?",
         ["Proven success", "Promising, but the confidence intervals overlap. Keep measuring", "No change", "The test failed"], 1,
         "Small samples move a lot by chance."),
        ("Why keep the denominator beside the rate?",
         ["It looks complete", "It shows how much the rate could move by chance and whether volume changed", "It is required by PhilHealth", "It replaces the numerator"], 1,
         "Rates from small denominators are unstable."),
        ("What is a balancing measure?",
         ["The main outcome", "A measure that watches for harm caused by the change itself", "The budget", "A staff satisfaction survey"], 1,
         "A new check might delay starts."),
        ("Six consecutive weekly points fall below the median. What does that indicate?",
         ["Random noise", "A shift, a likely real change", "A data error", "A trend"], 1,
         "Six or more on one side is the shift rule."),
        ("Five consecutive points each rise above the one before. What is this?",
         ["A shift", "A trend", "An astronomical point", "Noise"], 1,
         "Five or more rising or falling is a trend."),
        ("What should happen before testing a change across the whole unit?",
         ["Nothing", "A small test on one station group or shift, with a prediction", "A memo to all staff", "A purchase order"], 1,
         "Test small, learn, then scale."),
        ("When is a corrective action closed?",
         ["When it is assigned", "When the owner and reviewer have recorded evidence that it worked", "When the meeting ends", "After 30 days"], 1,
         "Doing it is not the same as showing it worked."),
        ("What did the structured handoff program show?",
         ["No effect", "23% fewer medical errors in hospital residents", "More errors", "Shorter shifts"], 1,
         "Before-and-after data in residents. Applying it to dialysis is an inference."),
        ("Which is a forcing function?",
         ["A poster near the machine", "A machine that will not start until the scanned order matches the settings", "A reminder at huddle", "A refresher course"], 1,
         "It makes the wrong action impossible."),
        ("Which six elements define an indicator?",
         ["Name, color, size, font, chart, date", "Numerator, denominator, inclusions, period, data source, owner", "Patient, nurse, doctor, machine, water, drug", "Budget, staff, time, place, cost, result"], 1,
         "Without them, a trend cannot be trusted."),
        ("What is the median line on a run chart for?",
         ["Decoration", "A reference for the shift and run rules", "Showing the target", "Showing the average cost"], 1,
         "The rules are counted against the median."),
    ],
    "terms": [("Incident", "An event that harmed, or could have harmed, a patient."),
              ("Near miss", "An error caught before it reached the patient."),
              ("Forcing function", "A design that makes the wrong action impossible."),
              ("Indicator", "A defined measure tracked over time."),
              ("Balancing measure", "A measure that watches for harm caused by the change."),
              ("Run chart", "A plot of a measure over time with a median line."),
              ("PDSA", "Plan-Do-Study-Act, a small test of a change."),
              ("Confidence interval", "The range within which the true value probably lies.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality assessment and improvement in dialysis units."),
                 ("hemodialysis-complications.html", "Common events worth measuring."),
                 ("dialysis-access-infection.html", "Infection as a quality indicator.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c5", "calc-dialysis-head-nurse-toolkit.html#c10"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
