# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician writing readings on a water room log sheet.",
    "objectives": [
        "List the daily checks in a dialysis water room, and state what each one proves.",
        "Perform a total chlorine test correctly: the right sample point, the right timing, and a correct reading of the result.",
        "Record results in a way that another person could rely on without asking you.",
        "Recognize a trend, and report it before any limit is reached.",
    ],
    "big": """
{{plain:Think of the guard at a subdivision gate. If he writes &ldquo;cars, OK&rdquo; at the end of the day, his logbook is useless when something goes missing. If he writes each plate number, the time, and his name, anyone can check it later. A water room log works the same way.}}
<p>The picture has a limit. The guard sees each car. You cannot see chlorine, hardness, or bacteria; you see only what a test shows you. A test done at the wrong tap, read too late, or written down as a tick proves nothing. Your work is to do a small number of checks properly and to write down exactly what you saw.</p>
{{flow:The daily round, start of day|System on and stable::Let the system run for the time your procedure states before you test anything.|Chlorine::Test total chlorine after the carbon tanks before the first patient.|Pretreatment::Read the filter pressures, check the softener clock, and check the salt.|Reverse osmosis::Record conductivity, flows, pressures, and rejection.|Loop::Record the pressure, flow, and return readings.|Sign and release::Record every number, sign the log, and tell the nurse the water is released.}}
{{cards:Key terms for this module|Total chlorine::Free chlorine plus chloramine. This is the test that protects patients.|Reagent::The chemical in a test kit that changes color when it meets the substance being tested.|Blank or control::A check that the test itself is working before you trust its answer.|Trend::The direction in which results are moving over days or weeks.|Release::The recorded statement that today&rsquo;s checks passed and treatment may begin.}}
""",
    "case": {
        "title": "A row of ticks",
        "html": """
<p>It is Monday, 05:30. Mr. Dennis Aquino, 27, a newly hired water technician, takes over the water room today. The chlorine log for the past month shows a tick in every box, the same initials, and no numbers. The test strips in the drawer expired four months ago. He tests with a fresh kit. The result is 0.06 mg/L after the first carbon tank and less than 0.02 mg/L after the second. The first patients are due at 06:15, and the charge nurse, Ms. Rowena Santiago, asks whether she can start.</p>
""",
        "questions": ["Can the past month&rsquo;s log be relied on, and what do you do about it?",
                      "What does today&rsquo;s result tell you, and may treatments start?",
                      "What do you report, and what should change so this does not happen again?"],
    },
    "sections": [
        ("checks", "Daily checks", "What is checked, and what each check proves", """
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>What it proves</th><th>What it cannot tell you</th></tr></thead>
<tbody>
<tr><td>Total chlorine after the carbon tanks</td><td>The carbon is still removing chlorine and chloramine</td><td>Anything about bacteria or minerals</td></tr>
<tr><td>Hardness after the softener</td><td>The softener still has capacity left</td><td>Whether its timer is set correctly</td></tr>
<tr><td>Pressure drop across each filter</td><td>The filter is not clogged</td><td>Whether the filter is torn and letting dirt through</td></tr>
<tr><td>Product conductivity and percent rejection</td><td>The membrane is still separating out dissolved salts</td><td>Anything about chlorine, bacteria, or endotoxin</td></tr>
<tr><td>Flows and pressures</td><td>The system can meet the unit&rsquo;s demand for water</td><td>The quality of that water</td></tr>
<tr><td>Monthly culture and endotoxin test</td><td>The loop was microbiologically clean on the day of sampling</td><td>What will happen next week</td></tr>
</tbody></table></div>
<p>Read the right-hand column as carefully as the middle one. A perfect conductivity reading feels reassuring, but it says nothing about chlorine or bacteria.</p>
{{key:No single reading covers for another. Each check answers one question only, so every check on the round is done every time.}}
"""),
        ("chlorine", "Chlorine test", "The total chlorine test, step by step", """
<p>The total chlorine test is the most important test a water technician performs, because it is the one that tells you the carbon is still protecting patients. Units test before the first patient of the day and then at set intervals, commonly before each patient shift or every four hours. Follow your own procedure.[[iso23500_1]][[coulliette2013]]</p>
{{flow:Performing the test|Run the system::The system must already be running, so that the sample is water that passed through the carbon at working flow.|Choose the port::Sample after the first (worker) tank. If chlorine is found there, sample after the second.|Flush the port::Let water run for the stated time, so you are not testing water that sat still in the tap.|Use a total chlorine test::A free chlorine test will miss chloramine. Check the kit&rsquo;s name and expiry date.|Time it::Read the color at exactly the time the kit states. Too early or too late gives a wrong answer.|Record the number::Write the value and unit, the port, the time, and your name.}}
{{cards:Acting on the result|At or below the limit after the worker tank::Record the result and release the water.|Above the limit after the worker tank::Test after the polisher at once. Tell the responsible person, because the worker tank needs replacement. Test more often, as your procedure states.|Above the limit after the polisher::Stop. No treatments on this water. Tell the charge nurse and the medical director immediately.}}
<p>The limit in the international standard is 0.1 mg/L of total chlorine.[[iso23500_3]] Your test must be sensitive enough to read at that level. A swimming pool test kit is not.</p>
{{stop:Never write a result you did not see. A test that was skipped is recorded as not done, with the reason, and reported.}}
"""),
        ("records", "Good records", "Writing a log that can be trusted", """
<p>A log has two readers: you today, and someone else later. That later reader may be the technician on the next shift, a physician looking for the cause of a patient&rsquo;s anemia, or an inspector. None of them can ask you what you meant. The entry has to speak for itself.</p>
{{cards:Six rules for the water log|Numbers, not ticks::Write the actual reading with its unit.|At the time::Record each reading when you take it, not from memory at the end of the shift.|In ink, or in the approved system::Correct an error with a single line through it, the right value, your initials, and the date.|No blanks::If a check was not done, write why.|Out of range is flagged::Mark it, state what you did, and name whom you told.|Signed::Every entry carries a name.}}
<p>Use one test on every entry before you sign: could an inspector, a physician, or the technician on the next shift understand exactly what was found and what was done, without asking you?</p>
"""),
        ("trends", "Trends", "Reading trends", """
{{fig:dashboard|A trend line shows what a single result cannot. Plot the main water readings over time and look for the direction they are moving.}}
<p>Most failures in a water system arrive slowly, because the parts wear out slowly. Carbon is used up grain by grain. A filter collects dirt a little at a time. So the pressure drop climbs a little each week, rejection slips by a fraction of a percent, and chlorine after the worker tank moves from undetectable to just detectable. None of these crosses a limit on the day you notice it. Reporting it on that day is the difference between a planned filter change and a cancelled shift.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you see over time</th><th>What it may mean</th></tr></thead>
<tbody>
<tr><td>Pressure drop across a filter rising</td><td>The filter is loading with dirt; a backwash or change is due</td></tr>
<tr><td>Chlorine after the worker tank becoming detectable</td><td>The carbon is nearing exhaustion, or the feed water carries more chlorine than before</td></tr>
<tr><td>Hardness after the softener rising</td><td>The resin is exhausted, the salt is low, or regeneration is failing</td></tr>
<tr><td>Rejection falling</td><td>Membrane damage, scaling, or a leaking seal</td></tr>
<tr><td>Bacterial counts rising month to month but still under the limit</td><td>Biofilm is forming; disinfection may be due sooner</td></tr>
</tbody></table></div>
<p>The practical point is that you report direction, not only position. &ldquo;Within limits, but higher every week for a month&rdquo; is a complete and useful report.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Can the past month&rsquo;s log be relied on?</strong> No. A month of ticks, made with strips that had already expired, is not evidence that the water was safe. It is also not proof that it was unsafe. It is a gap in the record. Report it to the chief technician and the medical director as a gap, without blame, and do not rewrite or fill in the old entries.</p>
<p><strong>What today&rsquo;s result tells you.</strong> Today&rsquo;s result is 0.06 mg/L after the worker tank and less than 0.02 after the polisher. If the unit&rsquo;s limit is 0.1 mg/L, both are within it, and Mr. Aquino can record the numbers and release the water to Ms. Santiago. But chlorine that can be detected after the worker tank is a trend worth reporting the same morning, because the carbon may be nearing exhaustion. Test after both tanks at the next interval and write every number.</p>
<p><strong>What to report and what should change.</strong> Report the gap in the old log and the detectable chlorine after the worker tank. Then fix the system that allowed the ticks: in-date kits with a reorder point, a log sheet that asks for numbers and ports instead of boxes to tick, and a second person who reviews the log each week.</p>
"""],
    "skills": {
        "title": "Total chlorine test and daily log",
        "intro": "Materials: the unit&rsquo;s total chlorine test kit, a timer, the sample ports, and the log.",
        "items": [("Confirms the system has been running for the stated time before sampling.", False),
                  ("Checks that the kit is a total chlorine test and is in date.", True),
                  ("Selects the correct sample port and flushes it for the stated time.", True),
                  ("Follows the kit instructions exactly, including the reading time.", True),
                  ("Records the value, unit, port, time, and name.", False),
                  ("States the correct action for a result above the limit after the worker tank and after the polisher.", True),
                  ("Completes the remaining daily readings with numbers and units and signs the release.", False),
                  ("Points out one trend in the past month&rsquo;s log and says whom to tell.", False)],
        "placement": "Perform the start-of-day round with your preceptor on three different days. On the third, the preceptor only observes.",
    },
    "quiz": [
        ("Which test detects chloramine?",
         ["Free chlorine test", "Total chlorine test", "Hardness test", "Conductivity"], 1, "Total chlorine includes free chlorine and chloramine. A free chlorine test misses chloramine."),
        ("Where is the first chlorine sample of the day taken?",
         ["From the feed water", "After the first (worker) carbon tank", "From the drain", "From a dialysis machine"], 1,
         "Testing after the worker shows whether it is still doing its job."),
        ("Chlorine is above the limit after the second carbon tank. What happens next?",
         ["Record it and continue", "Retest tomorrow", "Stop treatments on this water and inform the nurse and medical director at once", "Lower the reverse osmosis pressure"], 2,
         "Breakthrough after the polisher means chlorine can reach patients."),
        ("Why must the color be read at exactly the stated time?",
         ["To save time", "The color keeps changing, so an early or late reading gives a wrong value", "The kit expires in minutes", "It does not matter"], 1,
         "Test chemistry is timed; follow the kit instructions."),
        ("Which log entry is acceptable?",
         ["A tick", "&ldquo;OK&rdquo;", "&ldquo;0.04 mg/L total chlorine, port after tank 1, 05:40, J. Cruz&rdquo;", "A blank"], 2,
         "A usable record gives the number, unit, place, time, and person."),
        ("You forgot the midday chlorine test. What do you write?",
         ["The morning value again", "Nothing", "That the test was not done, why, and whom you told; then test now", "A tick"], 2,
         "Records must be true. Report the gap and test immediately."),
        ("Pressure drop across the sediment filter has risen a little every week for a month. No limit has been reached. What should you do?",
         ["Ignore it", "Report the trend so that a backwash or change can be planned", "Remove the gauge", "Increase pump pressure"], 1,
         "Trends allow planned maintenance instead of emergency repair."),
        ("Product conductivity is excellent today. What does this tell you about chlorine?",
         ["Chlorine is absent", "Nothing; conductivity does not measure chlorine", "Chlorine is high", "The carbon is new"], 1,
         "Each check answers one question only."),
    ],
    "terms": [("Free chlorine", "Chlorine that is not combined with ammonia."),
              ("Sample port", "A small tap fitted at a set point in the system for taking test samples."),
              ("Out of range", "A result outside the limits your unit has set.")],
    "readings": [("dialysis-water-treatment-systems.html", "Monitoring schedules and the troubleshooting flow."),
                 ("dialysis-qapi-vs-cqi.html", "How run charts and trends are used in quality review.")],
}
