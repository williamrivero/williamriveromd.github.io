# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 10: APD, cycler setup, alarms and home monitoring. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain why automated PD (APD) suits many school-age children, and what small fill volumes do to cycler behavior.",
        "Cross-check a cycler program against the written order before the first night.",
        "Interpret common cycler alarms as information about the child and respond without unsafe overrides.",
        "Read the home treatment record for missed therapy, drain trends and early warnings.",
    ],
    "big": """
<p>Automated PD lets a cycler run exchanges overnight while the child sleeps, freeing the day for school and play. That is why it is common in children. The cost is that a machine now measures, times and alarms, and small fill volumes push some cyclers close to their limits. A cycler that alarms all night wakes the whole family, and tired families start bypassing alarms.</p>
<p>Your work in this module is to make sure the cycler does what the order says, to help families understand alarms, and to read the treatment record for trouble before it becomes an emergency.</p>
{{plain:Think of the cycler as a careful babysitter who follows written instructions exactly and calls you whenever something is unclear. If the instructions are wrong, the babysitter follows them anyway. If the babysitter calls every hour, you start ignoring the phone.}}
<p>The picture has a limit. A babysitter can tell you why she called. A cycler gives a code. The meaning of the code lives in the device&rsquo;s instructions and in the child: a &ldquo;low drain&rdquo; may be a kinked line, constipation, a catheter problem or fluid absorbed by a child who is dehydrated.</p>
{{cards:Key terms for this module|APD::Automated peritoneal dialysis: a cycler performs exchanges, usually overnight.|Tidal PD::Draining only part of the fill each cycle, leaving a reserve volume, to reduce drain pain and alarms.|Last fill::A fill left in the abdomen during the day after the cycler finishes.|Treatment record::The cycler&rsquo;s log of fills, drains, dwell times and alarms.|Override::Bypassing an alarm and continuing; allowed only as the device instructions and training permit.}}
""",
    "case": {"title": "Every night at two", "html": """
<p><strong>Andrea Lim, 10</strong>, 28 kilograms, has been on APD for two months. Her mother, <strong>Grace</strong>, says the cycler alarms &ldquo;low drain&rdquo; almost every night around 2 a.m., and she has learned to press &ldquo;bypass&rdquo; so everyone can sleep. Andrea is tired at school. The clinic nurse, <strong>Mark</strong>, downloads the treatment record before the monthly visit.</p>
""", "questions": ["What could the 2 a.m. low-drain alarms mean?",
                  "What risks come with routine bypassing?",
                  "What should Mark look for in the record?"]},
    "sections": [
        ("small-volume-cycling", "Small volumes", "Cycling small volumes", """
<p>The cycler program translates the order into machine settings: fill volume, number of cycles, dwell time, total therapy time, last fill, and sometimes tidal settings. Before the first night, two people check the program against the written order, field by field, using the child&rsquo;s current weight and BSA as in Module 7.</p>
{{fig:pdn10_a}}
<p>Small fills interact with the machine in predictable ways. Each cycler has a minimum fill volume, and the 2020 ISPD pediatric guideline notes that automated PD is not suitable for newborns because their fill volumes are too small for current machines (1D).[[pd_nourse2021]] In small children, short dwells mean many drain phases per night, and each drain is a chance for an alarm. Tidal settings, ordered by the nephrologist, can reduce drain pain and alarms by leaving a reserve volume.</p>
<p>Line length and bed height matter. The cycler measures by weight or pressure, and the child&rsquo;s position relative to the machine affects flow, as the device instructions describe.</p>
{{key:Two people check the cycler program against the order, field by field, before the first night and after every order change.}}
"""),
        ("alarms-as-signals", "Alarms", "Alarms as clinical signals", """
<p>Treat every repeated alarm as information about the child, not only about the machine.</p>
{{fig:pdn10_b}}
<div class="table-wrap"><table>
<thead><tr><th>Alarm type</th><th>Possible meaning in the child</th><th>First response</th></tr></thead>
<tbody>
<tr><td>Low drain or slow drain</td><td>Kinked line, position, constipation, catheter tip position, fibrin; occasionally fluid absorbed in a dehydrated child</td><td>Check lines and position; follow the device steps; report a pattern</td></tr>
<tr><td>Line occlusion or patient line</td><td>Clamp closed, line kinked under the child, catheter problem</td><td>Check clamps and the line path</td></tr>
<tr><td>Fill or supply problem</td><td>Bag clamp closed, empty bag, wrong bag</td><td>Check bags and clamps against the setup</td></tr>
</tbody></table></div>
<p>Repeated bypassing of drain alarms can leave fluid in the abdomen that adds to the next fill. In a small child, that overfill raises intraperitoneal pressure, causing pain, breathing difficulty or leaks. Overrides are allowed only as the device instructions and the family&rsquo;s training permit, and a pattern of alarms is always reported.</p>
{{call:Stop the cycler and call the PD team, per unit protocol, if alarms come with abdominal pain, cloudy fluid, fever, vomiting, breathing difficulty, a swollen abdomen or leakage at the exit site.}}
{{key:One alarm is a problem to fix. The same alarm every night is a pattern to report.}}
"""),
        ("the-home-record", "The record", "The home treatment record", """
<p>The cycler&rsquo;s log and the family&rsquo;s chart together show what actually happened at home. Read them monthly and whenever something changes.</p>
<ul>
<li><strong>Delivered therapy:</strong> total time, number of cycles completed, nights missed or shortened.</li>
<li><strong>Drain pattern:</strong> volumes per cycle, the hour alarms cluster, initial drain of the day dwell.</li>
<li><strong>Ultrafiltration:</strong> net removal per night against the trend and the child&rsquo;s weight and blood pressure.</li>
<li><strong>Bypasses:</strong> how many, at which phase.</li>
<li><strong>Family notes:</strong> fluid appearance, pain, fever, school days missed.</li>
</ul>
<p>Missed or shortened therapy is not a moral failing to scold. It is usually a sign that the plan does not fit the family: work shifts, power cuts, alarm fatigue, a child who resists. Bring it to the team as a problem to solve (Module 18).</p>
{{scene:Mark and the download|<p>Mark sees drain alarms at about 2 a.m. on 24 of 30 nights, each followed by a bypass, and lower ultrafiltration on those nights. Andrea&rsquo;s chart notes hard stools. He asks Grace whether Andrea sleeps on one side, reviews constipation with the nephrologist, asks about a tidal setting, and retrains Grace on what a bypass leaves behind.</p><p class="tc-scene-take">The pattern in the log turned a nuisance into a fixable problem.</p>}}
{{key:Read the log for what was delivered, not what was prescribed. The gap between them is your work.}}
"""),
    ],
    "debrief": ["""
<p><strong>Meaning.</strong> Clustering at the same hour suggests a position or catheter-tip problem, often worsened by constipation; the log and history support that.</p>
<p><strong>Risks of bypassing.</strong> Retained fluid adds to the next fill and raises intraperitoneal pressure; therapy is reduced; real problems are missed. Andrea&rsquo;s tiredness may reflect disturbed sleep and less dialysis.</p>
<p><strong>The record.</strong> Alarm timing and frequency, bypasses, ultrafiltration per night, missed therapy, and notes on stools and pain. Mark brings a specific pattern and a proposed fix to the nephrologist.</p>
"""],
    "skills": {"title": "Cycler verification and alarms", "intro": "Use a training cycler or the device simulator.",
               "items": [("Cross-checks every cycler field against the written order with a second person", True),
                         ("Explains three alarm types to a caregiver in plain words with the first response for each", False),
                         ("Identifies a pattern of alarms and bypasses in a treatment record", False),
                         ("States when to stop the cycler and call the PD team", True),
                         ("Documents delivered therapy against prescribed therapy", False)]},
    "quiz": [
        ('Why is APD common in school-age children?',
         ['It is cheaper', 'It needs no catheter', 'It runs overnight and frees the day for school', 'It removes more protein'], 2,
         'Days stay free.'),
        ('Before the first night, the cycler program is:',
         ['Trusted from the factory', 'Set by the family', 'Copied from another child', 'Checked against the order, field by field, by two people'], 3,
         'Machines follow wrong instructions exactly.'),
        ('Why is APD not suitable for newborns per ISPD 2020 (1D)?',
         ['Fill volumes are too small for current machines', 'Noise', 'Cost', 'Infection'], 0,
         'Manual PD may be used.'),
        ('Tidal PD:',
         ['Drains everything each cycle', 'Leaves a reserve volume to reduce drain pain and alarms', 'Uses no fluid', 'Is for adults only'], 1,
         'Ordered by the nephrologist.'),
        ('A low-drain alarm every night at the same hour suggests:',
         ['Random noise', 'Peritonitis always', 'A position or catheter-tip problem, often worsened by constipation', 'A broken cycler always'], 2,
         'Patterns point to causes.'),
        ('Risk of routinely bypassing drain alarms in a small child:',
         ['None', 'Better sleep only', 'More clearance', 'Retained fluid adds to the next fill and raises intraperitoneal pressure'], 3,
         'Overfill causes pain, breathing trouble or leaks.'),
        ('Which finding means stop the cycler and call?',
         ['Abdominal pain with cloudy fluid', 'Clear fluid', 'A bag clamp closed', 'Child asleep'], 0,
         'Possible peritonitis.'),
        ('The treatment record shows:',
         ['Only the prescription', 'What was actually delivered', 'Nothing useful', 'Only alarms'], 1,
         'Compare delivered with prescribed.'),
        ('Missed therapy at home is best approached as:',
         ['A reason to scold', 'Irrelevant', 'A sign the plan may not fit the family', 'A legal matter'], 2,
         'Solve the fit problem.'),
        ('A line occlusion alarm: first check:',
         ['The order', 'The dialyzer', 'The blood pressure', 'Clamps and the line path under the child'], 3,
         'Simple causes first.'),
        ('Why do short dwells increase alarms in small children?',
         ['More drain phases per night, each a chance for an alarm', 'They do not', 'Less fluid used', 'Machines tire'], 0,
         'More drains, more alarms.'),
        ('A fill or supply alarm often means:',
         ['A catheter break', 'A bag clamp closed, an empty or wrong bag', 'Peritonitis', 'Low blood pressure'], 1,
         'Check the setup.'),
        ('Overrides are allowed:',
         ['Whenever the family wants', 'Never under any condition', 'Only as device instructions and training permit', 'Only by the child'], 2,
         'And patterns are reported.'),
        ('Lower ultrafiltration on nights with bypasses suggests:',
         ['Better dialysis', 'Nothing', 'Higher clearance', 'Less effective therapy those nights'], 3,
         'Retained or skipped volumes reduce removal.'),
        ('After every order change, the cycler program is:',
         ['Rechecked against the new order', 'Left as is', 'Reset to default', 'Changed by the family alone'], 0,
         'Every change needs a new check.'),
    ],
    "terms": [("APD", "Automated peritoneal dialysis using a cycler."),
              ("Cycler", "A machine that performs PD exchanges automatically."),
              ("Tidal PD", "Partial drains with a reserve volume left in."),
              ("Last fill", "A fill left in during the day after cycling."),
              ("Treatment record", "The cycler&rsquo;s log of fills, drains, dwells and alarms."),
              ("Bypass", "Overriding an alarm to continue therapy.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis for families."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Power outages and typhoons for families on dialysis.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html"],
}
