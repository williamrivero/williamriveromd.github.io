# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 06: Risk Management and Proving Improvement. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a quality lead in front of a run chart and a risk register taped to the wall of a small dialysis office.",
    "objectives": [
        "Write a risk as cause, failure, and consequence, score it, and name its owner and escalation threshold.",
        "Use failure mode and effects analysis to test a process before you change it.",
        "Investigate an event from work as it was actually done, looking for latent conditions rather than a person to blame.",
        "Choose a fix from the stronger end of the hierarchy, and measure whether it worked.",
        "Calculate a rate with its denominator and confidence interval, and pair every measure with a balancing measure.",
        "Tell audit, improvement, and research apart, and send research questions to the ethics pathway.",
    ],
    "big": """
{{plain:Safety layers are like slices of Swiss cheese. Each slice has holes, and most of the time the holes do not line up. Harm happens on the day they do.}}
{{fig:dch06_cheese}}
<p>The picture has a limit. Real holes move. A layer that held yesterday can open today because a nurse is new, the unit is running late, or an override has become habit. Risk management is the work of finding where the holes keep lining up, and making that slice thicker.</p>
{{cards:Key terms for this module|Risk::A possible event described as cause, failure, and consequence.|Residual risk::The risk that remains after existing controls.|FMEA::Failure mode and effects analysis, a structured way to ask how each step of a process could fail and what would follow.|Latent condition::A weakness built into the system, such as a sort order or a staffing pattern, that waits for an active error.|QAPI::Quality assessment and performance improvement, the unit&rsquo;s ongoing program to measure and improve care.|Balancing measure::A measure that checks whether an improvement caused harm somewhere else.|Run chart::Data plotted over time with a median line, used to tell a real change from noise.}}
""",
    "case": {"title": "The order caught in time", "html": """
<p>At a twelve-station unit in Valenzuela, nurse Ms. Aileen Santos is about to program a dialysate potassium of 1.0 mmol/L for Mr. Ricardo Cruz. She stops. The order was written for Mr. Ricardo de la Cruz, who sits two stations away. The patient list sorts by station, not by name, and both men are on the afternoon shift. The electronic record has a patient-confirmation pop-up, but staff say they click through it because it appears on every screen. Nobody was harmed.</p>
<p>Your quality lead, Mr. Joel Ramos, asks what to put in the report. &ldquo;Should I just remind everyone to be careful?&rdquo;</p>
""", "questions": ["What allowed the order to reach the wrong chart?",
                  "What change would you test next week, and how would you know it helped?",
                  "What would make you escalate this beyond the unit?"]},
    "sections": [
        ("risk", "Writing a risk", "Write it so it can be fixed", """
<p>&ldquo;Patient identification&rdquo; is a topic, not a risk. A useful risk statement has three parts: the cause, the failure, and the consequence. &ldquo;Because two patients with similar names share a shift and the list sorts by station (cause), an order may be entered in the wrong chart (failure), and a patient may receive the wrong dialysate potassium (consequence).&rdquo;</p>
<p>Score likelihood and severity on a scale your facility has approved, name the existing controls and how you know they work, and estimate the residual risk. Assign an owner for the residual risk and a threshold above which it goes to leadership. A rare risk with a catastrophic consequence still deserves leadership review, even if its score looks modest.</p>
{{formula:<strong>Teaching scale.</strong> Likelihood 1 to 5 &times; severity 1 to 5. In this course&rsquo;s exercises, a score of 15 or more, or any catastrophic consequence, triggers leadership review. Your facility&rsquo;s approved thresholds apply in practice. Calculator 4 scores and flags a risk.}}
<p>Before you change a process, test it on paper. In failure mode and effects analysis, a team walks each step and asks how it could fail, what would follow, and how likely and detectable that failure is. One Taiwanese unit used it to redesign deterioration alerts during hemodialysis and reported that its hazard scores fell by 71%.[[dch_lin2022]] That is a single-center before-and-after report, but the method is cheap and often finds the hole before a patient does.</p>
"""),
        ("investigate", "Investigating", "After an event: work as done, not work as imagined", """
<p>After a serious event, stabilize care first, preserve records and equipment, notify leadership and the required parties, and support the patient and the staff involved (Module 13). Then build the timeline from how the work was actually done that day. The goal is to find the latent conditions, not to find the person who touched it last.</p>
<p>Ask what made the error easy and what made catching it hard. In the case, the latent conditions are the station sort order, two similar names on one shift, and an alert that fires so often that staff no longer read it. Each of those will be there tomorrow, whoever is on duty.</p>
{{fig:dch06_hierarchy}}
{{flow:The hierarchy of fixes, strongest first|Remove or force::Make the error impossible: separate similar names across shifts, require a barcode or second identifier before programming.|Standardize and simplify::One way to do the step, on every shift.|Check and alert::A second person or a targeted alert, used sparingly so it stays meaningful.|Train and remind::Necessary, but on its own it fades within weeks.}}
{{key:A reminder to be careful is the weakest fix there is. Choose one from higher up the list, then measure it.}}
"""),
        ("measure", "Measuring", "A rate needs a denominator", """
{{fig:dch06_rate}}
<p>A count tells you how many. A rate tells you how often, and only a rate can be compared across months or units. Every rate needs a definition of the event, a denominator, a time window, and a statement of what data are missing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>Numerator</th><th>Denominator</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Bloodstream infection rate</td><td>Events meeting the definition</td><td>Patient-months</td><td>3 in 150 = 2.0 per 100 patient-months</td></tr>
<tr><td>Catheter-related infection rate</td><td>Events in catheter patients</td><td>Catheter-days</td><td>2 in 900 = 2.2 per 1,000 catheter-days</td></tr>
<tr><td>Missed treatments</td><td>Sessions missed</td><td>Sessions scheduled</td><td>12 in 600 = 2.0 per 100</td></tr>
<tr><td>Identification check done</td><td>Correct checks observed</td><td>Opportunities observed</td><td>45 of 50 = 90%</td></tr>
</tbody></table></div>
<p>The first and third rates are both 2 per 100, but they measure different risks with different denominators. Small numbers swing widely by chance; a month with two infections instead of one is not a trend. Calculator 3 gives the rate with a 95% confidence interval and compares two periods. Plot rates on a run chart and react to a signal, such as six points in a row on one side of the median, rather than to a single point.</p>
{{fig:dch06_runchart}}
<p>Pair every improvement measure with a balancing measure. If a second identifier check cuts wrong-chart entries but adds fifteen minutes to afternoon starts, the delay is a harm too, and you need to see it.</p>
"""),
        ("research", "Research", "Improvement or research?", """
<p>An audit asks whether you do what you said you would. Improvement asks whether a change made your own care better. Research asks a question meant to produce knowledge for others, usually by comparing groups, changing care for the purpose of the study, or sharing data beyond the unit. The line matters because research needs ethical review and, usually, consent.[[dch_phreb2022]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Activity</th><th>Example</th><th>Who decides how it proceeds</th></tr></thead>
<tbody>
<tr><td>Audit</td><td>Percentage of sessions with a correct two-identifier check</td><td>Quality program</td></tr>
<tr><td>Improvement</td><td>Testing a new check for four weeks with run charts</td><td>Quality program, with governance</td></tr>
<tr><td>Research</td><td>Comparing outcomes before and after a vendor&rsquo;s device and publishing them, or sharing treatment-level data with a sponsor</td><td>Research ethics committee, privacy lead, and governance, before any data leave or care changes</td></tr>
</tbody></table></div>
{{call:Stop any data release or study-related change in care until the research ethics pathway and the privacy lead have made a written determination.}}
<p>Readiness for good research looks like good quality work: clear data definitions, complete records, trained staff, and a named data custodian. A retrospective analysis must reckon with selection bias, confounding, and missing data before anyone draws conclusions.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What allowed it?</strong> Latent conditions: two similar names on the same shift, a patient list sorted by station, and an alert that fires on every screen so staff click through it. Ms. Santos&rsquo;s attention was the only layer that held. Thank her, and record what caught it.</p>
<p><strong>What change, and how would you know?</strong> Move one of the two patients to a different shift if clinically acceptable, and test a two-identifier check before any dialysate prescription is programmed. Measure the percentage of sessions with a correct check (process), wrong-chart entries caught or reaching the patient (outcome), and minutes added to treatment start (balancing). Review override data for the pop-up and ask IT whether it can fire only when names are similar. Run it for four weeks, including a deliberately busy shift.</p>
<p><strong>When to escalate?</strong> If the fix you need, such as changing the record system or adding staff, is beyond the unit&rsquo;s authority, or if the residual risk stays above your threshold, take it to the owner with the risk statement, the options, and the cost. A memo reminding staff to be careful is not an option.</p>
"""],
    "skills": {"title": "Risk score, causal timeline, and effectiveness check",
               "intro": "Score one risk, reconstruct one near miss, and design a measured change while a preceptor observes.",
               "items": [
                   ("Writes the risk as cause, failure, and consequence.", False),
                   ("Scores it with rationale and names existing controls and their evidence.", False),
                   ("Builds the timeline from work as done and identifies at least two latent conditions.", True),
                   ("Chooses a fix above &ldquo;train and remind&rdquo; on the hierarchy.", False),
                   ("Defines a process, outcome, and balancing measure with denominators.", False),
                   ("Contains the immediate hazard before the investigation is complete.", True),
                   ("Escalates residual risk above the threshold to governance with options.", True),
                   ("Routes a research request to the ethics pathway and privacy lead before any data release.", True),
               ],
               "placement": "Choose one recurring near miss on your unit. Run a four-week test of a stronger fix with a run chart and a balancing measure, and present the result to your quality meeting."},
    "quiz": [
        ("Which is a usable risk statement?",
         ["Patient identification", "Because two similar names share a shift, an order may enter the wrong chart and a patient may receive the wrong dialysate", "Errors happen", "Staff are careless"], 1,
         "Cause, failure, consequence."),
        ("A rare risk has a catastrophic consequence but a modest score. What should happen?",
         ["Ignore it", "It still goes to leadership review", "Lower its severity", "Wait for it to happen"], 1,
         "Catastrophic consequences merit review regardless of score."),
        ("What is a latent condition?",
         ["A nurse&rsquo;s mistake", "A weakness built into the system that waits for an active error", "A patient&rsquo;s illness", "A machine alarm"], 1,
         "Sort orders, staffing patterns, and noisy alerts are latent conditions."),
        ("Which fix is strongest?",
         ["A reminder memo", "Retraining", "Making the error impossible or forcing a check before the step", "A poster"], 2,
         "Remove or force sits at the top of the hierarchy."),
        ("What did a single-center FMEA redesign of deterioration alerts report?",
         ["No change", "A 71% fall in hazard scores", "Higher mortality", "A randomized benefit"], 1,
         "A before-and-after report: useful, not definitive."),
        ("A unit had 3 bloodstream infections in 150 patient-months. What is the rate?",
         ["0.5 per 100", "2.0 per 100 patient-months", "3.0 per 100", "50 per 100"], 1,
         "3 divided by 150, times 100."),
        ("Infections went from one to two this month. What is the right response?",
         ["Declare an outbreak", "Plot the rate with its denominator and look for a real signal, unless patients are at risk now", "Ignore it", "Retrain everyone"], 1,
         "Small numbers move by chance."),
        ("What is a balancing measure?",
         ["The budget", "A measure that checks whether an improvement caused harm elsewhere", "The average of two measures", "A staff survey"], 1,
         "Treatment-start delay balances a new check."),
        ("What distinguishes completing an action from proving it worked?",
         ["Nothing", "Implementation shows it was done; later observation and outcomes show whether risk fell", "The owner&rsquo;s signature", "The cost"], 1,
         "Close actions on evidence of effect."),
        ("A vendor wants treatment-level data to compare outcomes before and after its device. What is this?",
         ["Routine audit", "Research needing ethics review and privacy determination first", "Improvement", "Marketing only"], 1,
         "Data leaving the unit for a comparison is research."),
        ("What should an investigation look for first?",
         ["The person to discipline", "What made the error easy and catching it hard", "The cheapest fix", "Who reported it"], 1,
         "Systems, not scapegoats."),
        ("Which run chart pattern is a signal rather than noise?",
         ["One high point", "Six or more consecutive points on one side of the median", "Two points close together", "Any month above average"], 1,
         "Use rules, not impressions."),
        ("Why are the infection rate and missed-treatment rate in the example different measures even though both are 2 per 100?",
         ["They are the same", "They use different events and denominators and reflect different risks", "One is wrong", "Rates cannot be compared"], 1,
         "Label every denominator."),
        ("When does residual risk go to the governing body?",
         ["Never", "When it stays above the threshold or needs resources beyond the unit", "Only after harm", "When staff complain"], 1,
         "Escalate with options and costs."),
        ("A pop-up alert fires on every screen and staff click through it. What is the problem?",
         ["Staff laziness", "Alert fatigue makes the alert a weak, noisy layer", "The pop-up is too small", "Nothing"], 1,
         "Alerts used sparingly stay meaningful."),
    ],
    "terms": [("Risk", "A possible event written as cause, failure, and consequence."),
              ("Residual risk", "Risk remaining after current controls."),
              ("FMEA", "Failure mode and effects analysis."),
              ("Latent condition", "A system weakness that waits for an active error."),
              ("QAPI", "Quality assessment and performance improvement."),
              ("Run chart", "Data over time with a median line."),
              ("Balancing measure", "A check for harm caused elsewhere by an improvement."),
              ("Denominator", "The population or opportunities a rate is measured against.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "QAPI and continuous quality improvement in dialysis.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
