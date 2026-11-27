# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 14: The hemodialysis session: initiation, monitoring and completion. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain dialysis disequilibrium and why first sessions in children are short and gentle.",
        "Verify a fluid-removal plan in mL/kg/h and % body weight, and explain why fast removal is harmful in small children.",
        "Monitor a child during hemodialysis with attention to trends, behavior and early signs of intolerance.",
        "Complete a session safely, including blood return, post-weight and handoff.",
    ],
    "big": """
<p>During hemodialysis, two things leave the child: solutes such as urea, and water. Both can leave too fast. Urea leaving the blood faster than the brain can follow causes disequilibrium. Water leaving the blood faster than it refills from the tissues causes low blood pressure. Children are vulnerable to both because their volumes are small and their signs come late.</p>
<p>Your work in this module is to run a session that removes what was ordered at a pace the child tolerates, and to notice intolerance before it becomes collapse.</p>
{{plain:Think of the blood as a small reservoir fed by a large lake, the tissues. The machine drains the reservoir. If you drain slowly, the lake refills it. Drain too fast, and the reservoir empties even though the lake is still full.}}
<p>The picture has a limit. The refill rate is not fixed: it depends on how much extra fluid the tissues hold, the child&rsquo;s albumin, heart function and blood vessel tone. A child near target weight refills slowly. That is why intolerance often appears at the end of a session, when the child is close to dry weight.[[pdn_fischbach2005]]</p>
{{cards:Key terms for this module|Dialysis disequilibrium::Brain swelling from a rapid fall in blood urea, causing headache, vomiting, confusion or seizures.|Plasma refilling::Fluid moving from tissues back into the blood during ultrafiltration.|Ultrafiltration rate::Fluid removed per hour, best expressed per kilogram.|Intradialytic hypotension::A fall in blood pressure during dialysis with symptoms or the need to intervene.|Blood volume monitoring::A machine sensor that tracks the relative change in blood volume during the session.}}
""",
    "case": {"title": "Quiet in the third hour", "html": """
<p><strong>Jasmine Ortiz, 11</strong>, 30 kilograms, has a 1.2 kilogram fluid-removal goal over 3 hours. In the third hour she stops chatting, yawns repeatedly, and asks to lie flat. Her heart rate has risen from 92 to 118 beats per minute; her blood pressure is still in her usual range. Her mother says, &ldquo;She&rsquo;s just tired.&rdquo; <strong>Nurse Leo</strong> is at the next chair.</p>
""", "questions": ["What is Jasmine&rsquo;s ultrafiltration rate in mL/kg/h?",
                  "What do the yawning and rising heart rate suggest?",
                  "What does Leo do first?"]},
    "sections": [
        ("first-sessions-and-disequilibrium", "First sessions", "First sessions and disequilibrium", """
<p>When dialysis starts in a child with a high urea, a rapid fall in blood urea can leave the brain relatively concentrated; water moves into brain cells and they swell. This dialysis disequilibrium syndrome causes headache, nausea, vomiting, restlessness, confusion and, rarely, seizures, usually in the first hours or sessions.[[zepedaorozco2012]][[raina2022]]</p>
{{fig:pdn14_a}}
<p>Prevention is a gentle start. The ESPN guidelines describe a first-session blood flow of about 3 mL/kg/min (or 90 mL/m&sup2;), keeping urea clearance below about 3 mL/min/kg, and a first session of no more than 3 hours, adapted to the fluid need.[[pdn_fischbach2005]] A pediatric systematic review and clinical recommendations on disequilibrium support a gradual approach in children starting dialysis.[[raina2022]] Your role is to verify that the first-session order follows the unit&rsquo;s pediatric start protocol, and to watch for early symptoms.</p>
{{key:First sessions are short and slow on purpose. Headache, vomiting or restlessness early in a first session is disequilibrium until proven otherwise.}}
"""),
        ("fluid-removal-in-children", "Fluid removal", "Fluid removal in a small body", """
<p>The total fluid to remove comes from the difference between the pre-dialysis weight and the target weight, plus anything given during the session. Express the rate per kilogram so that children of different sizes can be compared.</p>
{{formula:Ultrafiltration rate (mL/kg/h) = volume to remove (mL) &divide; hours &divide; weight (kg)<br>Example: 1,200 mL over 3 h in 30 kg &rarr; 400 mL/h &divide; 30 = about 13.3 mL/kg/h, or 1.3% of body weight per hour}}
<p>Older pediatric practice guidelines described a weight loss of 1.5% to 2% of body weight per hour as standard, while warning that the amount and rate must be tolerable.[[pdn_fischbach2005]] More recent pediatric evidence links faster removal with harm to blood vessels: in the HDF, Heart and Height study, a higher ultrafiltration rate was associated with higher carotid intima-media thickness and mean arterial pressure scores.[[pdn_shroff2019hdf]] The Pediatric Continuous Renal Replacement Therapy (PCRRT) Workgroup notes that intradialytic hypotension in children has not been studied extensively, so most preventive measures rest on adult data and expert opinion.[[pdn_raina2019]] The safe rate for a given child is a prescriber decision; your job is to calculate it, see whether the child tolerates it, and report when they do not.</p>
{{fig:pdn14_b}}
{{key:Express fluid removal in mL/kg/h. A rate the child does not tolerate is too fast, whatever the number says.}}
"""),
        ("monitoring-and-completion", "Monitoring", "Monitoring and completion", """
<p>Children compensate for falling blood volume by raising their heart rate and tightening their vessels. Blood pressure can stay normal until compensation fails. Watch the trend and the child, not one number.</p>
<div class="table-wrap"><table>
<thead><tr><th>Watch</th><th>Early sign of trouble</th></tr></thead>
<tbody>
<tr><td>Behavior</td><td>Quiet, yawning, restless, irritable, asking to lie down</td></tr>
<tr><td>Heart rate</td><td>Steady rise from the child&rsquo;s baseline</td></tr>
<tr><td>Skin and color</td><td>Pallor, sweating, cool hands</td></tr>
<tr><td>Symptoms</td><td>Abdominal pain, nausea, cramps, dizziness, headache</td></tr>
<tr><td>Machine</td><td>Blood volume curve falling steeply, access and venous pressure changes</td></tr>
</tbody></table></div>
<p>When intolerance appears: lay the child flat with legs raised if appropriate, reduce or stop ultrafiltration per protocol, and call the nephrologist. Fluid boluses and other treatments are given only as ordered.</p>
<p><strong>Completion.</strong> Return blood per protocol and the priming plan, take a post-dialysis weight under the same conditions as the pre-weight, record vital signs and how the child feels, check the access, and hand over with I-PASS or your unit&rsquo;s structured format, which was associated with fewer medical errors in pediatric hospitals.[[starmer2014]]</p>
{{key:Behavior and heart rate change before blood pressure in children. Act on the trend.}}
"""),
    ],
    "debrief": ["""
<p><strong>The rate.</strong> 1,200 mL &divide; 3 h &divide; 30 kg &asymp; 13.3 mL/kg/h, about 1.3% of body weight per hour, in the third hour near her target weight.</p>
<p><strong>The signs.</strong> Yawning, quietness, wanting to lie flat and a heart rate rising from 92 to 118 suggest falling blood volume with compensation still holding her blood pressure.</p>
<p><strong>First action.</strong> Leo lays Jasmine flat, reduces or pauses ultrafiltration per protocol, rechecks her vital signs and calls the nephrologist. He tells her mother what he sees and why. Later he reports the episode so the team can review her target weight and removal plan.</p>
"""],
    "skills": {"title": "Running a pediatric session", "intro": "Simulation first, then supervised sessions.",
               "items": [("Verifies a first-session order against the unit&rsquo;s pediatric start protocol", True),
                         ("Calculates ultrafiltration rate in mL/kg/h and % body weight per hour with a second check", True),
                         ("Monitors behavior, heart rate trend, color and symptoms, not blood pressure alone", False),
                         ("Responds to intolerance by positioning, reducing ultrafiltration per protocol and calling", True),
                         ("Completes blood return, post-weight under matched conditions, and a structured handoff", False)]},
    "quiz": [
        ('Dialysis disequilibrium is caused by:',
         ['Low potassium', 'Air embolism', 'A rapid fall in blood urea causing brain swelling', 'Infection'], 2,
         'Water moves into relatively concentrated brain cells.'),
        ('A sign of disequilibrium:',
         ['Better mood', 'Rash', 'Cough', 'Headache, vomiting, restlessness or confusion'], 3,
         'Usually early in first sessions.'),
        ('Described first-session blood flow for children:',
         ['About 3 mL/kg/min', 'About 15 mL/kg/min', 'Maximum the pump allows', 'Same as usual'], 0,
         'With a session of no more than 3 hours.'),
        ('1,200 mL over 3 h in 30 kg equals about:',
         ['4 mL/kg/h', '13.3 mL/kg/h', '40 mL/kg/h', '400 mL/kg/h'], 1,
         '400 mL/h &divide; 30.'),
        ('In the 3H study, a higher ultrafiltration rate was associated with:',
         ['Better growth', 'Fewer cramps', 'Higher cIMT and mean arterial pressure scores', 'Nothing'], 2,
         'Observational association.'),
        ('The PCRRT Workgroup notes that pediatric intradialytic hypotension:',
         ['Is well studied in large trials', 'Never occurs', 'Is only adult', 'Has not been studied extensively in children'], 3,
         'Much guidance rests on adult data.'),
        ('Why does intolerance often appear late in a session?',
         ['Plasma refilling slows as the child nears target weight', 'Machines slow down', 'Children get bored', 'Dialysate runs out'], 0,
         'The lake refills the reservoir more slowly.'),
        ('Which often changes first in a child losing blood volume?',
         ['Blood pressure', 'Heart rate and behavior', 'Temperature', 'Weight'], 1,
         'Compensation keeps blood pressure up until it fails.'),
        ('A child yawns repeatedly and asks to lie flat in hour three. You:',
         ['Ignore it', 'Increase ultrafiltration', 'Lay flat, reduce ultrafiltration per protocol, recheck and call', 'End without telling anyone'], 2,
         'Act on early signs.'),
        ('Fluid boluses during a session are given:',
         ['Whenever the nurse thinks', 'By the parent', 'Never', 'Only as ordered'], 3,
         'Follow the order and protocol.'),
        ('The post-dialysis weight should be taken:',
         ['Under the same conditions as the pre-weight', 'Any way', 'Only monthly', 'Before blood return'], 0,
         'Comparable weights.'),
        ('I-PASS handoffs in pediatric hospitals were associated with:',
         ['More errors', 'Fewer medical errors', 'No change', 'Longer stays'], 1,
         'Starmer 2014, a multicenter intervention study.'),
        ('A blood volume monitor shows:',
         ['Absolute blood volume', 'Potassium', 'The relative change in blood volume during the session', 'Kt/V'], 2,
         'A trend tool.'),
        ('The older ESPN guideline described standard hourly weight loss as:',
         ['0.1% of body weight', '5%', '10%', '1.5%&ndash;2% of body weight, if tolerated'], 3,
         'Older practice description; tolerance decides.'),
        ('Who decides the safe fluid-removal rate for a child?',
         ['The prescriber', 'The nurse', 'The parent', 'The machine'], 0,
         'The nurse calculates and reports tolerance.'),
    ],
    "terms": [("Dialysis disequilibrium syndrome", "Brain swelling from a rapid fall in blood urea."),
              ("Plasma refilling", "Fluid moving from tissues back into the blood during ultrafiltration."),
              ("Ultrafiltration rate", "Fluid removed per hour, best expressed per kilogram."),
              ("Intradialytic hypotension", "A symptomatic fall in blood pressure during dialysis."),
              ("Blood volume monitoring", "Tracking the relative change in blood volume during dialysis."),
              ("I-PASS", "A structured handoff: illness severity, patient summary, action list, situation awareness, synthesis by receiver.")],
    "readings": [("hemodialysis-complications.html", "Complications during hemodialysis."),
                 ("dry-weight-determination.html", "How dry weight is set.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-pediatric-bp.html"],
}
