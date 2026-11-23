# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician recording readings on a water room log sheet.",
    "objectives": [
        "List the daily checks in a dialysis water room and say what each one proves.",
        "Perform a total chlorine test correctly, including the sample point, timing, and reading of the result.",
        "Record results so that another person could rely on them.",
        "Recognize a trend and report it before a limit is reached.",
    ],
    "big": """
{{plain:Monitoring is how a water room proves, every day, that it is safe. A test that is done at the wrong tap, read too late, or written down as a tick instead of a number proves nothing. This module is about doing a small number of checks properly and writing down what you actually saw.}}
{{flow:The daily round, start of day|System on and stable::Let the system run for the time your procedure states before testing.|Chlorine::Test total chlorine after the carbon tanks before the first patient.|Pretreatment::Filter pressures, softener clock, and salt.|Reverse osmosis::Conductivity, flows, pressures, rejection.|Loop::Pressure, flow, and return readings.|Sign and release::Record every number, sign, and tell the nurse the water is released.}}
{{cards:Key terms for this module|Total chlorine::Free chlorine plus chloramine. This is the test that protects patients.|Reagent::The chemical in a test kit that changes color.|Blank or control::A check that the test itself is working.|Trend::The direction results are moving over days or weeks.|Release::The recorded statement that today&rsquo;s checks passed and treatment may begin.}}
""",
    "case": {
        "title": "A row of ticks",
        "html": """
<p>A new technician takes over the water room. The chlorine log for the past month shows a tick in every box and the same initials. There are no numbers. The test strips in the drawer expired four months ago. This morning&rsquo;s test with a fresh kit reads 0.06 mg/L after the first carbon tank and less than 0.02 mg/L after the second.</p>
""",
        "questions": ["Can the past month&rsquo;s log be relied on?",
                      "What does today&rsquo;s result mean, and may treatments start?",
                      "What needs to be reported, and what should change?"],
    },
    "sections": [
        ("checks", "Daily checks", "What is checked, and what each check proves", """
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>What it proves</th><th>What it cannot tell you</th></tr></thead>
<tbody>
<tr><td>Total chlorine after the carbon tanks</td><td>The carbon is still removing chlorine and chloramine</td><td>Anything about bacteria or minerals</td></tr>
<tr><td>Hardness after the softener</td><td>The softener still has capacity</td><td>Whether the timer is set correctly</td></tr>
<tr><td>Pressure drop across each filter</td><td>The filter is not clogged</td><td>Whether the filter is torn and passing dirt</td></tr>
<tr><td>Product conductivity and percent rejection</td><td>The membrane is separating dissolved salts</td><td>Anything about chlorine, bacteria, or endotoxin</td></tr>
<tr><td>Flows and pressures</td><td>The system can meet demand</td><td>Water quality</td></tr>
<tr><td>Monthly culture and endotoxin test</td><td>The loop is microbiologically clean on that day</td><td>What will happen next week</td></tr>
</tbody></table></div>
{{key:No single reading covers for another. Each check answers one question only.}}
"""),
        ("chlorine", "Chlorine test", "The total chlorine test, step by step", """
<p>The total chlorine test is the most important test a water technician performs. Units test before the first patient of the day and then at set intervals, commonly before each patient shift or every four hours; follow your procedure.[[iso23500_1]][[coulliette2013]]</p>
{{flow:Performing the test|Run the system::The system must have been running, so the sample reflects water that passed through the carbon at working flow.|Choose the port::Sample after the first (worker) tank. If chlorine is found there, sample after the second.|Flush the port::Let water run for the stated time so you are not testing water that sat in the tap.|Use a total chlorine test::A free chlorine test will miss chloramine. Check the kit&rsquo;s name and expiry date.|Time it::Read the color at exactly the time the kit states. Too early or too late gives a wrong answer.|Record the number::Write the value and unit, the port, the time, and your name.}}
{{cards:Acting on the result|At or below the limit after the worker tank::Record and release.|Above the limit after the worker tank::Test after the polisher at once. Tell the responsible person; the worker tank needs replacement. Test more often, as your procedure states.|Above the limit after the polisher::Stop. No treatments on this water. Tell the charge nurse and medical director immediately.}}
<p>The limit in the international standard is 0.1 mg/L of total chlorine.[[iso23500_3]] The test must be sensitive enough to read at that level; a pool test kit is not.</p>
{{stop:Never write a result you did not see. A test that was skipped is recorded as not done, with the reason, and reported.}}
"""),
        ("records", "Good records", "Writing a log that can be trusted", """
{{cards:Six rules for the water log|Numbers, not ticks::Write the actual reading with its unit.|At the time::Record when you take the reading, not from memory at the end of the shift.|In ink, or in the approved system::Corrections are a single line through the error, the right value, your initials, and the date.|No blanks::If a check was not done, write why.|Out of range is flagged::Mark it, state what you did, and name whom you told.|Signed::Every entry has a name.}}
<p>A good test of any entry: could an inspector, a physician, or a technician on the next shift understand exactly what was found and what was done, without asking you?</p>
"""),
        ("trends", "Trends", "Reading trends", """
{{fig:dashboard|A trend line shows what a single result cannot. Plot the main water readings over time and look for direction.}}
<p>Most failures in a water system arrive slowly. Pressure drop climbs a little each week. Rejection slips by a fraction of a percent. Chlorine after the worker tank moves from undetectable to just detectable. None of these crosses a limit on the day you notice it. Reporting it then is the difference between a planned filter change and a cancelled shift.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you see over time</th><th>What it may mean</th></tr></thead>
<tbody>
<tr><td>Pressure drop across a filter rising</td><td>Filter loading; backwash or change due</td></tr>
<tr><td>Chlorine after the worker tank becoming detectable</td><td>Carbon nearing exhaustion, or higher chlorine in the feed water</td></tr>
<tr><td>Hardness after the softener rising</td><td>Resin exhausted, salt low, or regeneration failing</td></tr>
<tr><td>Rejection falling</td><td>Membrane damage, scaling, or a leaking seal</td></tr>
<tr><td>Bacterial counts rising month to month but under the limit</td><td>Biofilm forming; disinfection may be due sooner</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> A month of ticks with expired strips is not evidence that the water was safe, and it should be reported to the chief technician and medical director as a gap in the record, without blame and without rewriting it. Today&rsquo;s result is 0.06 mg/L after the worker tank and less than 0.02 after the polisher. If the unit&rsquo;s limit is 0.1 mg/L, both are within it and the water can be released, but detectable chlorine after the worker tank is a trend worth reporting: the carbon may be nearing exhaustion. What should change: in-date kits with a reorder point, a log that asks for numbers and ports, and a second person reviewing the log each week.</p>
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
    "terms": [("Free chlorine", "Chlorine not combined with ammonia."),
              ("Sample port", "A small tap fitted for taking test samples at a set point in the system."),
              ("Out of range", "A result outside the limits the unit has set.")],
    "readings": [("dialysis-water-treatment-systems.html", "Monitoring schedules and the troubleshooting flow."),
                 ("dialysis-qapi-vs-cqi.html", "How run charts and trends are used in quality review.")],
}
