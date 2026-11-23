# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician and a nurse reviewing a water system log together.",
    "objectives": [
        "Apply one response pattern to any out-of-range water result: stop, hold, report, investigate, release.",
        "Describe the immediate response to chlorine breakthrough, reverse osmosis failure, loss of supply, and suspected contamination.",
        "Handle water treatment chemicals safely.",
        "Write an incident record and take part in a review that prevents a repeat.",
    ],
    "big": """
{{plain:Think of a jeepney driver who hears a grinding sound from the brakes. He does not need to know which part has failed before he acts. He pulls over, tells the passengers to step down, and calls the mechanic. Finding the broken part comes after everyone is safe.}}
<p>The picture has a limit. A driver hears his problem. A water problem is silent: it shows only as a number on a test or a line on an alarm panel, and it can reach every patient on the floor at once. Every water system fails sooner or later. A tank is exhausted, a pump stops, the city cuts the supply, a typhoon floods the pump room. What protects patients on that day is not the equipment. It is a technician who knows the first three moves by heart: stop, hold, report.</p>
{{flow:One response for every water problem|Stop::Do not start new treatments on water you cannot vouch for.|Hold::Mark the system or the stations as on hold, so that no one starts by mistake.|Report::Tell the charge nurse immediately; the medical director is informed.|Investigate::Find the cause with the responsible person. Do not guess.|Correct and verify::Fix the cause, then retest at the right points.|Release::Only the designated person lifts the hold, and does so in writing.}}
{{cards:Key terms for this module|Hold::A formal stop on using the water or equipment.|Release::Formal permission to resume, given by the designated person.|Root cause::The underlying reason a problem happened, not only what was seen.|Corrective and preventive action::A written plan that fixes the problem and stops it from returning.|Contingency plan::The unit&rsquo;s prepared plan for losing water, power, or the building.}}
""",
    "case": {
        "title": "Breakthrough before the second shift",
        "html": """
<p>It is Thursday. At 10:45 the water technician, Mr. Paolo Navarro, 34, runs the pre-shift chlorine test. It reads 0.18 mg/L after the first carbon tank. He tests after the second tank at once: 0.14 mg/L. The unit&rsquo;s limit is 0.1 mg/L.</p>
<p>Six patients from the first shift are still on dialysis. In the waiting area, the second-shift patients are already weighed and seated, and the charge nurse, Ms. Carmela Dizon, is assigning stations.</p>
""",
        "questions": ["May the second shift start?",
                      "Who must know in the next two minutes, and what exactly will you say?",
                      "What is the technician&rsquo;s job here, and what belongs to the nurse and the physician?"],
    },
    "sections": [
        ("pattern", "Decision flow", "The decision flow", """
{{fig:wts_golden}}
<p>A fixed pattern removes hesitation. Under pressure, people wait for certainty, and certainty takes time that patients connected to the water do not have. You do not have to know the cause before you stop. You stop because a limit was crossed, and you find the cause afterward.</p>
{{stop:A repeat test that looks better does not cancel the first result. Two different results mean you do not yet know the truth. The hold stays until the responsible person is satisfied.}}
"""),
        ("failures", "Common failures", "Four failures and the first response", """
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>How it shows</th><th>First response by the technician</th><th>Decided by others</th></tr></thead>
<tbody>
<tr><td>Chlorine above the limit after the second carbon tank</td><td>Chlorine test</td><td>Hold all new starts. Tell the charge nurse at once, and state whether patients are connected. Do not adjust the result, and do not wait for a retest.</td><td>What happens to connected patients; when the system is released</td></tr>
<tr><td>Reverse osmosis failure or low rejection alarm</td><td>Alarm, high product conductivity, low flow</td><td>Hold new starts. Report the alarm text and the readings. Check the simple causes your procedure lists, such as a closed valve or a tripped pump.</td><td>Use of any backup; calling the service provider</td></tr>
<tr><td>Loss of feed water or low pressure</td><td>Low-pressure alarm, tank level falling</td><td>Report immediately, with the remaining tank volume if there is a tank. Contact the supplier as your plan states.</td><td>Shortening, rescheduling, or moving treatments</td></tr>
<tr><td>Suspected contamination: several patients with fever or chills, or water of unusual color or smell</td><td>Patient symptoms, observation</td><td>Report. Collect samples before anyone disinfects. Preserve the log.</td><td>Stopping treatments; medical care; notification of authorities</td></tr>
</tbody></table></div>
<p>Read the last column as carefully as the third. Your first response is fast and fixed. Everything in the last column belongs to the clinical team and the medical director, and your report is what lets them decide quickly.</p>
<p>After any repair or replacement, such as new carbon, a new membrane, or pipe work, the system is flushed, tested, and often disinfected before it is released. New carbon sheds fine dust and needs thorough rinsing. New pipe work needs disinfection and a clean culture.</p>
"""),
        ("disaster", "Supply loss and disasters", "Power, water supply, and typhoons", """
{{fig:typhoon}}
<p>In the Philippines, brownouts and water interruptions are ordinary events, and typhoons and floods come every year. The time to prepare is before the storm signal is raised. A prepared water room has four things. It knows its reserve volume and how many treatments that volume supports. It has a tested arrangement with the generator, including which pumps the generator powers. It has a named water tanker supplier, with the understanding that delivered water is a new source and must be tested. And its equipment is raised above the expected flood level where possible.</p>
{{cards:After the water or power comes back|Do not assume::The system coming back to life is not a release.|Check the clocks::Softener and disinfection timers may now be wrong.|Flush::Water that sat still in the loop may have grown bacteria.|Test::Chlorine, hardness, and reverse osmosis readings, before any patient.|After a flood::Treat the system as contaminated until it has been inspected, disinfected, and tested.}}
"""),
        ("chemicals", "Chemical safety", "Working safely with chemicals", """
{{cards:Rules for the chemical store|Read the safety data sheet::Do it before you first handle any product.|Wear what it says::Usually gloves, eye protection, and an apron; sometimes a respirator.|Never mix::Bleach with acid, or any two products, unless the procedure says so.|Label everything::Including spray bottles and transfer containers.|Ventilate::Keep the room aired during disinfection.|Know the eyewash::Find it before you need it.}}
<p>Salt, citric acid, peracetic acid, and bleach are common in a water room. Each is safe when handled as directed and harmful when it is not. If you spill one, report it and clean it up by the written method. Do not hose it into the drain.</p>
"""),
        ("quality", "Records and review", "From incident to improvement", """
{{fig:pdsa}}
<p>Write the incident record the same day, in plain facts: what was found, when, and where; what was done; who was told; and when the hold was released, and by whom. The record does not need to explain the cause. The cause comes from the review, where the people involved keep asking &ldquo;why&rdquo; until they reach something that can be changed: a missing reorder point for carbon, a timer without a battery backup, a log that accepted ticks.</p>
{{fig:fishbone}}
<p>Notice that none of those causes is a person. A review that ends with &ldquo;the technician was careless&rdquo; changes nothing, and the same event returns with a different technician. Water results belong on the agenda of the unit&rsquo;s regular quality meeting: chlorine results, cultures and endotoxin, incidents, and disinfection records. A technician who brings a clear chart to that meeting does as much for patient safety as any piece of equipment in the room.</p>
"""),
    ],
    "debrief": ["""
<p><strong>May the second shift start?</strong> No. Chlorine is above the limit after both tanks, so chlorine and chloramine may be reaching the stations. Mr. Navarro places the hold before he does anything else.</p>
<p><strong>Who must know, and what to say.</strong> Within two minutes, Ms. Dizon must hear something like this: &ldquo;Total chlorine is 0.18 after tank one and 0.14 after tank two at 10:45. Our limit is 0.1. Six patients are still on dialysis. I am holding all new starts.&rdquo; Notice what the report contains: the numbers, the ports, the time, the limit, the patients at risk, and the action already taken.</p>
<p><strong>Whose job is what.</strong> The nurse and the nephrologist decide what happens to the six connected patients, and whether anyone needs assessment for hemolysis. The technician&rsquo;s job is to hold, report, and record; to help find the cause, which may be exhausted carbon, a higher dose from the utility, or flow beyond the tanks&rsquo; capacity; and to retest at both ports after correction. The system returns to service only when the designated person releases it in writing.</p>
"""],
    "skills": {
        "title": "Out-of-range drill",
        "intro": "Materials: a simulated log with a chlorine result above the limit, hold tags, the unit&rsquo;s contingency plan, and an incident form.",
        "items": [("Recognizes the out-of-range result without prompting.", True),
                  ("Places a hold and prevents new treatment starts.", True),
                  ("Reports to the charge nurse within two minutes with the result, ports, time, and whether patients are connected.", True),
                  ("Does not replace the first result with a better repeat result.", True),
                  ("Lists possible causes without claiming one as fact.", False),
                  ("States the tests required before release and who may release.", False),
                  ("Completes the incident record with facts, times, and names.", False),
                  ("Locates the contingency plan, the reserve volume figure, and the tanker supplier&rsquo;s contact.", False)],
        "placement": "Read your unit&rsquo;s contingency plan for loss of water and loss of power, and walk the route with your preceptor.",
    },
    "quiz": [
        ("What are the first three moves for any out-of-range water result?",
         ["Retest, wait, record", "Stop, hold, report", "Disinfect, rinse, release", "Call the supplier, wait, restart"], 1,
         "Stop new starts, place a hold, and report. Investigation follows."),
        ("The first chlorine test is above the limit; a repeat is below it. What is correct?",
         ["Use the lower result", "Average them", "Keep the hold until the responsible person is satisfied", "Discard both"], 2,
         "Conflicting results mean the true value is unknown."),
        ("Who decides what happens to patients already on dialysis when the water is in doubt?",
         ["The technician", "The nurse and physician", "The water utility", "The patient&rsquo;s family"], 1,
         "The technician reports quickly; clinical decisions belong to the clinical team."),
        ("Several patients have fever and chills and contamination is suspected. Why sample before disinfecting?",
         ["Sampling is faster", "Disinfection would destroy the evidence of what patients were exposed to", "Disinfectant spoils sample bottles", "It is not necessary"], 1,
         "Samples taken afterward cannot show what was in the water during the event."),
        ("Power returns after a long outage. What should be checked before treatment resumes?",
         ["Nothing; power is back", "Timers, a flush of the loop, and the start-of-day tests", "Only the lights", "Only the generator fuel"], 1,
         "A restart is not a release. Timers drift and stagnant water may have grown bacteria."),
        ("Delivered tanker water arrives during a supply cut. How should it be regarded?",
         ["The same as city water", "As a new source that must be tested", "As already dialysis grade", "As unusable"], 1,
         "A different source can bring different contaminants."),
        ("Which is a root cause rather than a description?",
         ["Chlorine was 0.14 mg/L", "The second shift was delayed", "There was no reorder point for replacement carbon", "The test was done at 10:45"], 2,
         "A root cause is something that can be changed to prevent a repeat."),
        ("Before handling a disinfectant for the first time, what do you read?",
         ["The price list", "The safety data sheet", "The delivery note", "Nothing"], 1,
         "The safety data sheet gives hazards, protective equipment, and first aid."),
    ],
    "terms": [("Incident record", "A factual account of a problem and the response, written the same day."),
              ("Reserve volume", "The stored treated water available if the supply stops."),
              ("Eyewash station", "A fixture for flushing chemicals from the eyes.")],
    "readings": [("dialysis-water-treatment-systems.html", "Troubleshooting and the stop triggers in full."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Disaster planning for dialysis units and patients."),
                 ("dialysis-qapi-vs-cqi.html", "How incidents become improvement projects.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
}
