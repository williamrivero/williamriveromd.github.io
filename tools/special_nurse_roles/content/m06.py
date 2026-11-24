# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How to choose a problem worth solving, define a measure before counting, tell a real change from noise with a run chart, run a small Plan-Do-Study-Act test, and make the quality meeting end in owned actions reported fairly.",
    "desc": "Special Dialysis Nurse Roles Module 6: the quality improvement and clinical audit nurse in hemodialysis. QA, QAPI and CQI, aim statements, operational definitions and denominators, run-chart rules, PDSA fidelity, balancing measures, action logs and fair reporting.",
    "keywords": "dialysis quality improvement nurse, QAPI dialysis Philippines, run chart rules shift trend, PDSA cycle healthcare, operational definition denominator audit, balancing measure, clinical audit nurse hemodialysis",
    "image_alt": "A Filipino dialysis nurse pointing to a hand-drawn run chart on a whiteboard while two colleagues and the head nurse look on.",
    "objectives": [
        "Choose a problem worth solving and write an aim with an outcome, a process and a balancing measure.",
        "Write operational definitions, validate the denominator and handle missing data honestly.",
        "Display data over time on a run chart and apply run rules to separate signal from noise.",
        "Plan and evaluate a small PDSA test, keep an action log, and report results fairly.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A measure is a promise about what you counted",
         "html": """
<p>Think of a bathroom scale. If you weigh yourself once, after lunch, in your shoes, you learn very little. If you weigh yourself every morning, the same way, on the same scale, and plot the numbers, you can see whether your weight is really changing or just bouncing. And if you quietly start weighing yourself after a long run, the line drops, but nothing real has changed.</p>
<p>The picture has a limit. A bathroom scale measures one person. A unit measure counts many patients, many staff and many events, and every count depends on a definition: what qualifies, what is excluded, who is in the denominator. A measure is a promise that you counted the same thing the same way every time. The quality nurse keeps that promise, and then uses the honest number to test small changes until care improves.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Define before you count. Plot over time before you claim a change. Change one thing at a time and measure what it might break.</div>
"""},
        {"id": "terms", "nav": "QA, QAPI and CQI", "tag": "Concepts", "h2": "Choose a problem worth solving",
         "html": """
<p>Units use several overlapping words. <strong>Quality assurance</strong> checks whether care meets a standard (an audit). <strong>Quality assessment and performance improvement (QAPI)</strong> is the program that collects indicators, reviews them in a regular multidisciplinary meeting and acts on them; the PSN guidelines expect hemodialysis units to run such a program under the clinical head.[[psn2024]] <strong>Continuous quality improvement (CQI)</strong> is the method: small, repeated tests of change. The site's guide on QAPI and CQI explains the difference in more depth.</p>
<p>A problem is worth solving when it matters to patients, happens often enough to measure, and is within the unit's power to change. Write it as an aim statement: <em>what</em> will improve, <em>for whom</em>, <em>by how much</em>, <em>by when</em>.</p>
<div class="tc-cards">
<div class="tc-card"><b>Outcome measure</b>What patients experience: access-related bloodstream infections per 100 patient-months.</div>
<div class="tc-card"><b>Process measure</b>What staff do: catheter connections observed with every critical step.</div>
<div class="tc-card"><b>Balancing measure</b>What the change might break: minutes added to each connection; delayed starts.</div>
</div>
<p>The nurse supports the program. Accountability for the unit's quality stays with the clinical head and the governing body, and a project that will be published as research needs ethics review, which is separate from routine improvement.</p>
"""},
        {"id": "define", "nav": "Define before counting", "tag": "Measurement", "h2": "Define the measure before counting",
         "html": """
<p>An <strong>operational definition</strong> says exactly what counts. For "referral completed": is it completed when the form is sent, when the receiving service confirms it, when the procedure is done, or when the plan comes back and is acted on? Each answer gives a different number. Formal measure manuals spend pages on these definitions and exclusions for exactly this reason.[[cms_meas26]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Example: access referral closure</th></tr></thead>
<tbody>
<tr><td>Population</td><td>All in-center hemodialysis patients with an access referral due in the month</td></tr>
<tr><td>Numerator</td><td>Referrals with a returned specialist plan filed in the chart and acted on</td></tr>
<tr><td>Denominator</td><td>All referrals due in the month</td></tr>
<tr><td>Exclusions</td><td>Patient died or transferred out before the due date (each listed with reason)</td></tr>
<tr><td>Data source</td><td>Access referral tracker, checked against the chart</td></tr>
<tr><td>Frequency</td><td>Monthly</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">The 100 percent slide &middot; fictional</span><p>The quality slide says "Referral completion: 100%." Nurse Liza checks the tracker. Twenty referrals were due. Twelve forms were sent, and all twelve are counted as complete because "the form was sent." Only eight have a returned specialist plan. Management wants to publish 100 percent.</p><p>Liza shows the three possible definitions side by side: 12 of 12 forms sent (100 percent of a denominator that drops the eight never sent), 12 of 20 sent (60 percent), and 8 of 20 closed (40 percent). She recommends reporting 40 percent as the closure rate, because closure is what helps the patient, and proposes one change to test.</p><p class="tc-scene-take"><b>What this shows.</b> The 100 percent was produced by the denominator, not by care. A wrong denominator hides patients.</p></div>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 1</span>8 of 20 is 40 percent, with a 95 percent range of about 22 to 61 percent. If the unit excluded 6 "difficult" referrals without a written reason, the rate would become 8 of 14 (57 percent); the toolkit flags exclusions above one in five as a warning sign.</div>
<p><strong>Missing data.</strong> When records are incomplete, say so: "data available for 46 of 52 patients." Do not quietly drop the missing six, and do not assume they were fine.</p>
"""},
        {"id": "runchart", "nav": "Run charts", "tag": "Evidence", "h2": "Test a small change and look over time",
         "html": """
<p>A single before-and-after comparison is easily fooled by chance. A <strong>run chart</strong> plots the measure in time order with a median line, and simple rules tell you when a pattern is unlikely to be chance.[[perla2011]]</p>
<div class="tc-cards">
<div class="tc-card"><b>Shift</b>Six or more consecutive points all above or all below the median (points on the median are skipped).</div>
<div class="tc-card"><b>Trend</b>Five or more consecutive points all going up or all going down.</div>
<div class="tc-card"><b>Too few or too many runs</b>The line crosses the median far less or far more often than chance predicts.</div>
<div class="tc-card"><b>Astronomical point</b>A value obviously different from all others, worth investigating as an event.</div>
</div>
<p><strong>Plan-Do-Study-Act (PDSA).</strong> Each cycle tests one change on a small scale with a prediction: <em>Plan</em> the change and predict the result; <em>Do</em> it; <em>Study</em> the data against the prediction; <em>Act</em> by adopting, adapting or abandoning. A systematic review of 73 published PDSA reports found that fewer than 20 percent documented a sequence of iterative cycles, and only 15 percent of those analyzed in full used data at monthly or more frequent intervals.[[taylor2014]] In other words, many "PDSA projects" were one-off changes without the method's core features. Do the method properly: small, predicted, repeated, plotted.</p>
<div class="tc-plain"><span class="tc-lab">How certain are we?</span>Run-chart rules are established statistical conventions. The PDSA method is widely used but often applied poorly, so the strength of any one project's claim depends on how faithfully it was done. Process measures are surrogates; check the outcome too.</div>
<div class="tc-scene"><span class="tc-lab">One change, three cycles &middot; fictional</span><p>Liza tests a change: a named nurse calls the receiving service on day 3 after every access referral. Cycle 1 (two weeks, Aileen's referrals only): prediction, at least half confirmed by day 5; result, 4 of 5. Cycle 2 (all referrals for a month): 13 of 17 confirmed by day 5; but the calls added about 20 minutes a day to Aileen's work (balancing measure). Cycle 3: calls batched on Tuesdays and Fridays. Over the next seven months the monthly closure rate sits above the old median every month: a shift.</p><p class="tc-scene-take"><b>What this shows.</b> Small cycles, honest predictions, a balancing measure that changed the design, and a run-chart rule rather than a single good month.</p></div>
"""},
        {"id": "meeting", "nav": "Meetings that act", "tag": "Coordination", "h2": "Make the meeting lead to action",
         "html": """
<p>Many quality meetings review numbers and end without decisions. The quality nurse prepares the meeting so that it ends in owned actions.</p>
<ol class="tc-flow">
<li><b>Before</b>Validate the data; prepare run charts, not single numbers; list open actions.</li>
<li><b>During</b>Review each measure against its definition; discuss causes; agree one change or no change.</li>
<li><b>Record</b>Action, owner, due date, and how success will be measured.</li>
<li><b>After</b>Circulate the action log within two working days.</li>
<li><b>Next meeting</b>Start with the action log: done, not done, why.</li>
</ol>
<p><strong>Fair reporting.</strong> Report counts with percentages; show the denominator and exclusions; present unit data, not individual blame. Where a measure falls because of a few patients with complex needs, say so and stratify rather than excluding them. Pay attention to equity: if catheter rates are highest among patients who live farthest away or cannot afford surgery, that is a finding to act on, not to average out.</p>
<div class="tc-stop"><span class="tc-lab">Never</span>Change a definition, drop cases or pick a time window to make a number look better. If a definition must change, mark the break on the chart.</div>
"""},
        {"id": "sustain", "nav": "Sustaining change", "tag": "Practice", "h2": "Keep the gains",
         "html": """
<p>Improvements fade when they depend on one enthusiastic person. Build the change into the system: a checklist line, a roster slot, a field in the tracker, a step in orientation (Module 4). Keep plotting the measure monthly after the project ends; a sustained shift on the run chart is the evidence that the change has become normal practice. When a measure has been stable for a long time, reduce how often it is audited and move attention to the next problem, but keep a periodic check.</p>
"""},
    ],
    "case": {
        "title": "Publish the 100 percent",
        "html": """
<p><strong>Monday, 4 p.m., manager's office.</strong> The unit is preparing its quarterly report for the hospital board. The draft slide reads: "Access referral completion: 100%." The manager wants it published, saying, "The board likes good news, and the forms were all sent."</p>
<p>Your tracker shows: 20 referrals were due this quarter; 12 forms were sent; 8 specialist plans came back; 6 of the 8 procedures have been done. Two patients waiting longest are both on catheters and live in Bulacan, two hours away from the receiving hospital.</p>
""",
        "acte": {
            "Assess": "The 100 percent uses a denominator that excludes unsent referrals and a numerator that counts sending, not closure. The honest closure rate is 8 of 20 (40 percent). The longest waits cluster among patients far from the receiving hospital: an equity signal.",
            "Communicate": "Show the manager the three definitions side by side, recommend reporting 40 percent (8 of 20) with the definition, and present the improvement plan. Keep the discussion about the system, not the staff.",
            "Teach": "Explain why the board is better served by an honest baseline plus a plan than by a number that cannot be repeated next quarter.",
            "Escalate": "If pressure to publish the misleading figure continues, raise it with the clinical head, who is accountable for the quality program. Put the two longest-waiting catheter patients on the next access meeting agenda.",
        },
        "outcome": """
<p>The board report showed "Referral closure: 40% (8 of 20), new definition, baseline," with a run chart and a PDSA plan. Two quarters later the run chart showed a shift above the baseline median, which the board found more convincing than the old 100 percent.</p>
""",
        "task": "Write the operational definition for 'access referral closure' using the six parts in this module, and a three-line slide note that reports the baseline fairly.",
    },
    "second_round": ("After your change, the closure rate rises, but delayed session starts on Tuesdays and Fridays have doubled.",
                     "An updated PDSA cycle that names the balancing measure, your prediction for a redesigned change, and how you will plot both measures together."),
    "evidence_out": "One measure specification with numerator, denominator and exclusions; a run chart with run rules applied; one documented PDSA cycle with a balancing measure.",
    "critical": "Changing definitions, dropping cases or selecting time windows to improve a reported result.",
    "reflect": "Pick one number your unit reports regularly. Can you state its numerator, denominator and exclusions from memory? If not, who can?",
    "practice": {
        "intro": "Use your unit's de-identified data with the head nurse's permission, or the fictional data in this module.",
        "items": [
            "Write operational definitions for two measures your unit already reports.",
            "Build a run chart of one measure over at least 12 months and apply the four run rules.",
            "Plan one PDSA cycle with a prediction and a balancing measure; run it and record the study step.",
            "Prepare and circulate the action log after one quality meeting.",
            "Stratify one measure by a patient group (access type, distance, age) and report what you find.",
        ],
    },
    "job_aid": ("Measure specification and PDSA log", [
        "Aim statement (what, for whom, how much, by when)",
        "Outcome, process and balancing measures",
        "Numerator, denominator, exclusions (with reason)",
        "Data source and who collects it; frequency",
        "Baseline median and dates",
        "PDSA cycle number, change tested, scale (who, how long)",
        "Prediction (written before the test)",
        "Result versus prediction; balancing measure result",
        "Decision: adopt, adapt or abandon",
        "Owner, next cycle date",
    ]),
    "metric": "Primary example: access referrals closed (plan returned and acted on) divided by all referrals due; process: follow-up call made by day 3; balancing: minutes of coordination work per day and patient-reported burden.",
    "readings": [
        ("dialysis-qapi-vs-cqi.html", "QAPI and CQI explained for dialysis units."),
        ("dialysis-access-infection.html", "An example of an outcome worth measuring."),
    ],
    "academy": [("Head Nurse track", "dialysis-head-nurse.html")],
    "calcs": ["calc-qapi-run-chart-spc.html", "calc-qapi-cqi-toolkit.html", "calc-qapi-meeting-wizard.html", "calc-dialysis-nurse-portfolio-toolkit.html"],
    "terms": [
        ("Operational definition", "A precise statement of what counts in a measure's numerator, denominator and exclusions."),
        ("Run chart", "A time-ordered plot of a measure with a median line, read with simple run rules."),
        ("Shift", "Six or more consecutive points on one side of the median, a sign of non-random change."),
        ("Balancing measure", "A measure of what a change might make worse."),
        ("PDSA cycle", "A small test of change: Plan with a prediction, Do, Study the result, Act on it."),
    ],
    "quiz": [
        {"stem": "Twenty referrals were due, 12 forms were sent and 8 plans returned. Which is the honest closure rate?",
         "options": [["8 of 20 (40 percent).", True, "Closure means a returned plan; all due referrals belong in the denominator."],
                     ["12 of 12 (100 percent).", False, "Drops unsent referrals and counts sending, not closure."],
                     ["8 of 12 (67 percent).", False, "Drops the 8 never sent."],
                     ["12 of 20 (60 percent).", False, "Counts sending, not closure."]], "sources": [], "critical": True},
        {"stem": "What is a 'shift' on a run chart?",
         "options": [["Six or more consecutive points all above or all below the median.", True, "A standard run rule."],
                     ["Any single point above the goal.", False, "One point is not a shift."],
                     ["Three points going up.", False, "A trend needs five."],
                     ["A change in the median.", False, "Not the definition."]], "sources": ["perla2011"]},
        {"stem": "What is a 'trend' on a run chart?",
         "options": [["Five or more consecutive points all going up or all going down.", True, "A standard run rule."],
                     ["Two months of improvement.", False, "Too short."],
                     ["The average of all points.", False, "Not a trend."],
                     ["Any point outside the goal.", False, "Not a trend."]], "sources": ["perla2011"]},
        {"stem": "What did the systematic review of 73 PDSA reports find?",
         "options": [["Fewer than 20 percent documented iterative cycles, and few used frequent data.", True, "Many projects lacked the method's core features."],
                     ["PDSA always improves outcomes.", False, "Not what was studied."],
                     ["PDSA is harmful.", False, "Not found."],
                     ["All projects used monthly data.", False, "Only 15 percent of those fully analyzed did."]], "sources": ["taylor2014"]},
        {"stem": "Which is a balancing measure for a change that adds a phone follow-up to every referral?",
         "options": [["Minutes of nurse time added per day.", True, "It measures what the change might make worse."],
                     ["Referral closure rate.", False, "That is the outcome."],
                     ["Calls made by day 3.", False, "That is the process."],
                     ["Number of referrals due.", False, "That is the denominator."]], "sources": []},
        {"stem": "Six 'difficult' referrals are excluded without written reasons, raising the rate from 40 to 57 percent. What is the problem?",
         "options": [["Unexplained exclusions remove the hardest cases and inflate the result.", True, "Exclusions need written reasons and should be few."],
                     ["None; exclusions are always allowed.", False, "Not without reasons."],
                     ["The rate should be rounded to 60 percent.", False, "Rounding does not fix the problem."],
                     ["The denominator should be the patients who agreed.", False, "That also inflates."]], "sources": []},
        {"stem": "Records are missing for 6 of 52 patients. How should this be reported?",
         "options": [["State 'data available for 46 of 52 patients' and do not assume the missing were fine.", True, "Missingness must be visible."],
                     ["Drop the 6 silently.", False, "Hides a data problem."],
                     ["Count the 6 as meeting the standard.", False, "Unjustified assumption."],
                     ["Count the 6 as failing.", False, "Also an assumption; report the gap."]], "sources": []},
        {"stem": "Which aim statement is best?",
         "options": [["'Raise access referral closure from 40 to 70 percent for all in-center patients by June.'", True, "States what, for whom, how much and by when."],
                     ["'Improve referrals.'", False, "Too vague."],
                     ["'Work harder on access.'", False, "Not measurable."],
                     ["'Achieve 100 percent everything.'", False, "Unrealistic and vague."]], "sources": []},
        {"stem": "Who holds accountability for the unit's QAPI program?",
         "options": [["The clinical head and governing body, supported by the quality nurse.", True, "The nurse supports; accountability stays with leadership."],
                     ["The quality nurse alone.", False, "She supports the program."],
                     ["PhilHealth.", False, "A payer, not the program owner."],
                     ["Each patient.", False, "Not accountable for the program."]], "sources": ["psn2024"]},
        {"stem": "In a PDSA cycle, when is the prediction written?",
         "options": [["Before the test is run.", True, "A prediction made afterward is not a prediction."],
                     ["After the results are known.", False, "Defeats the purpose."],
                     ["Only if the test succeeds.", False, "Always before."],
                     ["It is optional.", False, "It is a core feature."]], "sources": ["taylor2014"]},
        {"stem": "A measure has been stable at goal for two years. What is reasonable?",
         "options": [["Audit less often but keep a periodic check, and move attention to the next problem.", True, "Sustain with lighter monitoring."],
                     ["Stop measuring forever.", False, "Drift can return unnoticed."],
                     ["Audit daily.", False, "Wasteful."],
                     ["Change the definition to make it harder.", False, "Breaks the series."]], "sources": []},
        {"stem": "A manager wants to publish a misleading 100 percent. The quality nurse cannot persuade her. What next?",
         "options": [["Raise it with the clinical head, who is accountable for the quality program.", True, "Escalate within the governance structure."],
                     ["Publish it to avoid conflict.", False, "Misleading reporting harms trust and patients."],
                     ["Post the real figure on social media.", False, "Not an appropriate channel."],
                     ["Delete the tracker.", False, "Destroys evidence."]], "sources": []},
        {"stem": "Why plot data over time rather than compare one month before with one month after?",
         "options": [["Single comparisons are easily fooled by chance variation.", True, "Run charts separate signal from noise."],
                     ["Plots look nicer.", False, "Not the reason."],
                     ["The board requires charts.", False, "Not the reason."],
                     ["One month is always enough.", False, "Usually not."]], "sources": ["perla2011"]},
        {"stem": "Catheter rates are highest among patients living farthest from the surgical center. How should this be handled?",
         "options": [["Report it as an equity finding and act on it, rather than averaging it away.", True, "Stratification reveals who is left behind."],
                     ["Exclude distant patients from the measure.", False, "Hides the problem."],
                     ["Ignore it; distance is not the unit's problem.", False, "The unit can act on access to referral."],
                     ["Blame the patients for living far away.", False, "Not fair or useful."]], "sources": []},
        {"stem": "What should the next quality meeting start with?",
         "options": [["The action log: what was done, not done, and why.", True, "Closes the loop on decisions."],
                     ["A new set of measures.", False, "First review existing actions."],
                     ["Individual blame for misses.", False, "Not useful."],
                     ["Social updates.", False, "Not the priority."]], "sources": []},
    ],
    "exam": [
        {"stem": "Which change to a measure is never acceptable?",
         "options": [["Dropping cases or changing the definition to make a result look better.", True, "This breaks the promise a measure makes."],
                     ["Marking a documented definition change on the chart.", False, "That is correct practice."],
                     ["Stratifying by access type.", False, "Useful."],
                     ["Reporting missing data.", False, "Correct practice."]], "sources": [], "critical": True},
        {"stem": "Six consecutive monthly points sit above the baseline median after a change. What does this suggest?",
         "options": [["A shift, unlikely to be chance alone.", True, "A standard run-chart rule."],
                     ["Random noise.", False, "Six consecutive points is the shift rule."],
                     ["A trend.", False, "A trend is five rising or falling points."],
                     ["Nothing can be concluded.", False, "The rule supports a real change."]], "sources": ["perla2011"]},
    ],
}
