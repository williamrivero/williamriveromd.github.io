# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 05: APD: cycler setup, the treatment record and alarms.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain how an automated peritoneal dialysis (APD) prescription (total volume, fill volume, number of cycles, tidal mode, last fill, day dwell) shapes clearance and fluid removal.",
        "Cross-check a programmed cycler against the written order and stop on any mismatch.",
        "Read a cycler treatment record (or remote-monitoring summary) for completion, drain patterns, ultrafiltration and alarms.",
        "Respond safely to drain alarms, interruptions and power failure, using only device-permitted checks.",
        "Recognize when an alarm is a symptom of a clinical problem that needs urgent assessment.",
    ],
    "big": """
<p>APD moves dialysis into the night. That brings freedom in the day and a new set of risks at 2 AM: a machine programmed differently from the order, a drain alarm that wakes the patient five times, a brownout in the middle of a cycle, a long day dwell that quietly absorbs fluid back.</p>
<p>Your work in this module is to make sure that what the cycler does is exactly what the nephrologist ordered, to read its record the way you would read a nursing note, and to treat repeated alarms as clinical information. Most cycler problems are not machine problems. They are the patient&rsquo;s bowel, catheter, abdomen or household, reported through a machine.</p>
{{plain:Think of the cycler as a very obedient assistant that follows a written recipe exactly, all night, without judgment. If the recipe card is wrong, it makes the wrong dish perfectly.}}
<p>The picture has a limit. A recipe does not change the cook. The cycler&rsquo;s record, though, tells you about the patient: how well the catheter drains, whether the abdomen tolerates the fill volume, whether the person stayed connected. The machine is both a delivery device and a monitoring device.</p>
{{cards:Key terms for this module|Cycle::One fill, dwell and drain performed by the cycler.|Tidal mode::A setting that leaves a reserve volume in the abdomen at each drain.|Last fill::The final fill that stays in during the day, also called the day dwell.|Initial drain::The drain of the day dwell at the start of the night&rsquo;s therapy.|Treatment record::The cycler&rsquo;s log of volumes, times, alarms and interventions.}}
""",
    "case": {"title": "Six alarms by morning", "html": """
<p><strong>Kristine, 29</strong>, a public-school teacher in Pampanga, has been on APD for three months with a night program and an icodextrin day dwell. She chose APD so she could keep teaching. Nurse <strong>Arnel</strong> reviews her cycler summary on Monday morning.</p>
<p><strong>Nights 1&ndash;5.</strong> Therapy completes. The initial drain of the day dwell is about 2,100 mL from a 2,000 mL last fill. Total UF is about 800 mL a night.</p>
<p><strong>Night 6.</strong> Four low-drain alarms between 1 and 4 AM. Therapy runs 70 minutes longer than prescribed. Initial drain is 1,600 mL.</p>
<p><strong>Night 7.</strong> Six alarms. Total UF about 300 mL. Kristine has texted: &ldquo;Sir, the machine kept waking me. Sorry I pressed bypass twice.&rdquo;</p>
""", "questions": ["What does the pattern in the cycler record tell you?",
                  "What is the most likely cause, and what makes peritonitis less likely?",
                  "What do you report, and to whom?"]},
    "sections": [
        ("the-physiology-of", "The prescription", "The physiology of an APD prescription", """
<p>APD usually delivers several short exchanges overnight. Short dwells keep the diffusion gradient steep (Module 1), which helps small-solute clearance. They also keep the glucose gradient strong, which helps fluid removal during the night. The trade-offs come in the day.</p>
{{fig:pd05_night}}
<div class="table-wrap"><table>
<thead><tr><th>Prescription element</th><th>What it does</th><th>What can go wrong</th></tr></thead>
<tbody>
<tr><td>Total night volume and cycle count</td><td>Sets night clearance</td><td>Too many short cycles waste time draining and filling</td></tr>
<tr><td>Fill volume</td><td>Larger fills increase membrane contact</td><td>Discomfort, breathlessness, leak, hernia</td></tr>
<tr><td>Tidal mode (partial drain each cycle)</td><td>Keeps some fluid in; reduces drain pain and alarms</td><td>Fluid accumulation if UF is not accounted for</td></tr>
<tr><td>Last fill or day dwell</td><td>Adds clearance and middle-molecule removal over the day</td><td>A long glucose day dwell may become net negative; icodextrin is often used</td></tr>
<tr><td>Midday exchange</td><td>Splits a long day dwell</td><td>Adds a manual connection</td></tr>
<tr><td>No day dwell (&ldquo;dry day&rdquo;)</td><td>Comfort, less glucose</td><td>Less clearance; may be insufficient once urine falls</td></tr>
</tbody></table></div>
<h3>Example: why tidal mode exists</h3>
<p>Mr. Ramon complains of a sharp pain low in his pelvis at the end of every drain. It wakes him three or four times a night. The catheter tip sits against the bowel or bladder as the abdomen empties. The nephrologist changes his program to tidal mode, so each drain leaves a reserve in the abdomen and the tip never sits on bare tissue. The pain stops. His record now shows partial drains, and you need to know that when you read it, or the volumes will look wrong.</p>
<p>The prescription is the nephrologist&rsquo;s. Your role is to know what each element does so you can spot when the record and the patient do not match.</p>
{{key:Know what each line of the program is for. That is how you notice when the record stops making sense.}}
"""),
        ("what-the-evidence", "The evidence", "What the evidence shows", """
<p>In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS), an observational cohort of 7,051 adults across seven countries, facilities with higher APD use had lower peritonitis risk (rate ratio 0.95 per 10-percentage-point higher APD use, 95% confidence interval 0.91 to 1.00).[[pd_perl2020]] This is an association at the facility level, at the margin of statistical significance. It does not show that switching any individual to APD prevents peritonitis. Facilities that use more APD may differ in many other ways.</p>
<p>The 2021 International Society for Peritoneal Dialysis (ISPD) membrane recommendations note that APD and icodextrin may lessen the mortality risk associated with fast peritoneal solute transfer. That statement is a practice point, not a graded recommendation.[[pd_morelle2021]]</p>
<p>When a patient asks, &ldquo;Is the machine safer?&rdquo;, the honest answer is that APD suits some lives and some membranes better, that it does not remove the need for perfect technique, and that the choice is made with the nephrologist.</p>
"""),
        ("prepare-and-verify", "Prepare and verify", "Prepare and verify", """
<p>Before the first setup, and after any order change:</p>
<ol>
<li>Confirm the patient and the current written order.</li>
<li>Cross-check on the cycler: therapy type, total volume, fill volume, number of cycles, therapy time, tidal settings if used, last fill volume and solution, patient weight if entered, and any UF limits set by the team.</li>
<li>Check solutions: type, strength, volume, expiry and integrity, and that the bags placed on the cycler match the program.</li>
<li>Escalate any mismatch before starting. <strong>Do not &ldquo;correct&rdquo; a program to match your guess of what was meant.</strong></li>
<li>Prepare the space: a clean, stable surface; the cycler at the height the manufacturer specifies relative to the patient; the drain line to a toilet, drain or collection container as the unit approves.</li>
<li>Set up, prime and connect using the model-specific instructions, protecting the sterile connections.</li>
</ol>
<h3>Example: a mismatch on the first night home</h3>
<p>Nurse Arnel does a home setup for Mrs. Leonora, newly trained on APD. The written order says the last fill is icodextrin. The cycler, programmed at the supplier&rsquo;s training center, shows a last fill drawn from the glucose bags. Nothing on the machine looks wrong. Only the comparison reveals it.</p>
<p>Arnel does not reprogram the machine to what he believes the nephrologist meant. He pauses the setup, calls the nephrologist, reads both versions aloud and asks which is correct. The order is confirmed, the program is corrected by the person authorized under the unit&rsquo;s procedure, and he documents the discrepancy and who resolved it. It took twelve minutes. A glucose day dwell in a fast transporter could have cost her a liter of fluid a day.</p>
{{key:A mismatch stops the setup. Ask; never assume which side is right.}}
"""),
        ("read-the-treatment", "Read the record", "Read the treatment record", """
<p>A cycler record or remote-monitoring summary is a nursing assessment tool. Read it the same way every time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>What to look for</th></tr></thead>
<tbody>
<tr><td>Completion</td><td>Full therapy delivered? Early stops? Bypassed drains?</td></tr>
<tr><td>Therapy time</td><td>Much longer than prescribed suggests slow drains</td></tr>
<tr><td>Initial drain</td><td>The day dwell drained at the start of the night; low values suggest day-dwell absorption or catheter problems</td></tr>
<tr><td>Cycle-by-cycle drain</td><td>A progressive fall suggests catheter malposition, constipation or fibrin</td></tr>
<tr><td>Total UF</td><td>Trend over days against weight and urine</td></tr>
<tr><td>Alarms</td><td>Type, phase, frequency, time of night</td></tr>
<tr><td>Manual interventions</td><td>Bypasses, skipped cycles</td></tr>
</tbody></table></div>
<p>Compare what you see with symptoms, morning weights, blood pressure and urine trend. Obtain device logs only with consent and through the approved data system.</p>
<h3>Worked example: three weeks, one record</h3>
<div class="table-wrap"><table>
<thead><tr><th>Week</th><th>Nights completed</th><th>Average therapy time</th><th>Average initial drain</th><th>Average night UF</th><th>Morning weight</th></tr></thead>
<tbody>
<tr><td>1</td><td>7 of 7</td><td>9 h 05 min</td><td>2,150 mL</td><td>750 mL</td><td>61.0 kg</td></tr>
<tr><td>2</td><td>6 of 7</td><td>9 h 10 min</td><td>2,100 mL</td><td>700 mL</td><td>61.3 kg</td></tr>
<tr><td>3</td><td>4 of 7</td><td>7 h 20 min</td><td>2,100 mL</td><td>650 mL</td><td>62.4 kg</td></tr>
</tbody></table></div>
<p>Drains and UF per night barely changed. What changed is that three nights in week three were stopped early, and therapy time fell by almost two hours. The weight followed. The question is not about the catheter. It is about the patient&rsquo;s night: a new baby in the house, a night-shift job, a power problem, fear of the alarms? Ask, with interest, and report the lost therapy with the reason.</p>
{{key:Read completion before you read volumes. Treatment that was not delivered cannot work.}}
"""),
        ("respond-to-alarms", "Respond to alarms", "Respond to alarms and interruptions", """
<p><strong>Assess the person first.</strong> A drain alarm in a patient with severe abdominal pain is not a machine problem.</p>
{{fig:pd05_alarm}}
<p>Then:</p>
<ol>
<li>Record the alarm, the phase, recurrence, time and symptoms.</li>
<li>Use only checks permitted by the device and the local plan: closed clamps, kinked lines, the patient lying on the line, cycler height, and a position change if the patient&rsquo;s condition allows.</li>
<li>Never override, repeatedly bypass or silence alarms outside the trained plan.</li>
<li>Follow the trained safe-disconnection and power-failure plan.</li>
<li>Use backup CAPD only when there is a prescribed backup regimen, suitable supplies at home and validated competence.</li>
<li>Call the PD team for repeated unresolved alarms or lost therapy.</li>
</ol>
<div class="table-wrap"><table>
<thead><tr><th>Alarm pattern</th><th>Likely mechanisms</th><th>Red flags that change urgency</th></tr></thead>
<tbody>
<tr><td>Low drain, every cycle, from the start</td><td>Catheter malposition, kink, constipation, fibrin, omental wrap</td><td>Severe pain, fever, cloudy effluent</td></tr>
<tr><td>Low drain, worsening over nights</td><td>Constipation, migration, rising fluid absorption</td><td>Breathlessness, weight gain</td></tr>
<tr><td>Drain pain at the end of drain</td><td>Catheter tip against bowel or bladder</td><td>Persistent pain, cloudy effluent</td></tr>
<tr><td>Fill alarm</td><td>Clamp closed, kink, solution bag issue</td><td>Leak at the exit site, or swelling of the genitals or abdominal wall</td></tr>
<tr><td>Repeated power interruptions</td><td>Unstable supply</td><td>Lost therapy plus rising weight</td></tr>
</tbody></table></div>
<h3>Example: the 2 AM phone call</h3>
<p>Mang Rudy calls the PD hotline at 2:10 AM. &ldquo;Low drain&rdquo; has sounded twice. Nurse Joan asks first how he feels: no pain, no fever. She asks him to look at the bag: clear. Then she walks him through the permitted checks. Are the clamps open? Yes. Is the line kinked? He follows it with his hand. He has been sleeping on his left side, on top of it. He rolls over and the drain resumes. Joan documents the call and asks him to mention it at his next visit. Nothing more was needed, because the person was checked first.</p>
<h3>Example: a brownout during a typhoon</h3>
<p>Mrs. Imelda&rsquo;s barangay loses power at 11 PM during a typhoon. Her cycler stops mid-fill. Her written power-failure plan, reviewed before the rainy season, tells her what to do: follow the device instructions for safe disconnection, and do one manual exchange using her prescribed backup regimen if the power is not back within the stated time. She has backup bags and was checked on manual technique last month. In the morning she calls the PD unit to report the lost therapy and her weight. Because the plan existed before the storm, nobody improvised at midnight.</p>
{{call:Call the PD team for repeated unresolved alarms, lost therapy, or any alarm with severe pain, fever or cloudy effluent. Never teach patients to bypass alarms as a routine.}}
"""),
        ("red-flags-in", "Red flags", "Red flags in this module", """
{{stop:<ul><li>Severe abdominal pain with any alarm: urgent assessment through the PD pathway; emergency services if unstable.</li><li>Cloudy effluent in the drain bag or line in the morning.</li><li>Swelling of the abdominal wall, groin or genitals during therapy (possible leak).</li><li>Breathlessness after the last fill (possible hydrothorax or overfill; urgent).</li></ul>}}
<p>A morning drain bag is the easiest thing for a tired patient to empty without looking at. Teach every APD patient to look at the bag, against light or print, before it goes down the toilet.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What the record says.</strong> The problem is new and progressive: four alarms on night 6, six on night 7, longer therapy time, a lower initial drain and a fall in UF from about 800 to about 300 mL. Kristine bypassed drains twice, so less treatment was delivered than the record&rsquo;s volumes suggest.</p>
<p><strong>The most likely cause.</strong> Arnel calls Kristine. She has had no bowel movement for four days, since starting iron tablets. No fever, no abdominal pain, effluent clear, weight up 0.8 kg. A loaded bowel can displace the catheter tip, so constipation is a common cause of drain failure. Clear effluent and no pain make peritonitis unlikely now.</p>
<p><strong>What he reports.</strong> He calls the nephrologist the same day with the full pattern: alarm count, phase and timing; therapy delivered and the two bypasses; initial drain trend; UF trend; bowel history; and weight. Bowel management is ordered by the nephrologist, with review and an abdominal X-ray if the drain does not recover, as the team decides.</p>
<p><strong>What he teaches.</strong> Report constipation early. Do not bypass drain alarms as a fix. And thank her for telling him about the bypasses, so she tells him next time.</p>
<p><strong>Take-home.</strong> Repeated drain alarms are symptoms. Read them with the bowel, the weight and the effluent.</p>
"""],
    "skills": {"title": "APD setup with a scripted alarm (OSCE station 2)",
               "intro": "Compare a mock written order against a programmed training cycler. Identify a deliberately mismatched last-fill volume and solution. Simulate an unresolved drain alarm and deliver an escalation call with exact alarm, phase, frequency, checks tried, symptoms, effluent and therapy delivered.",
               "items": [("Verifies the cycler program against the written order.", True),
                         ("Prevents a contaminated connection.", True),
                         ("Identifies the external checks the device allows.", False),
                         ("Escalates an unresolved alarm without overriding it.", True),
                         ("Records completed and missed treatment.", False)]},
    "quiz": [
        ("The programmed last-fill solution differs from the written order. What should happen?",
         ["Pause the setup and obtain clarification before treatment", "Use the program; the machine knows best", "Change the order to match the machine", "Skip the last fill"], 0,
         "Never start on a mismatch, and never guess which side is right. Ask the prescriber and document who resolved it."),
        ("Why do short overnight dwells help small-solute clearance?",
         ["They increase protein loss", "They warm the abdomen", "They keep the diffusion gradient steep", "They stop glucose absorption completely"], 2,
         "Frequent fresh fills restore the gradient before it flattens."),
        ("A long glucose day dwell may:",
         ["Always remove the most fluid", "Prevent constipation", "Have no effect", "Become net negative as the osmotic gradient fades"], 3,
         "The glucose is absorbed and reabsorption continues, which is why icodextrin is often used for the day dwell."),
        ("Mr. Ramon has sharp pelvic pain at the end of every drain. What does tidal mode do for him?",
         ["Fully drains every cycle", "Leaves a reserve volume so the catheter tip does not sit on bare tissue", "Adds a day dwell", "Doubles the fill volume"], 1,
         "Partial drains keep some fluid in, which reduces end-of-drain pain and alarms. The prescriber decides on tidal mode."),
        ("In PDOPPS, higher facility APD use was:",
         ["Proven to prevent peritonitis in individuals", "Associated with modestly lower peritonitis risk, at the margin of significance", "Associated with higher peritonitis", "Not studied"], 1,
         "The rate ratio was 0.95 per 10 percentage points, confidence interval 0.91 to 1.00, in an observational design."),
        ("A drain alarm occurs and the patient reports severe abdominal pain. First priority?",
         ["Repeat the drain cycle", "Override the alarm", "Tell the patient to sleep", "Assess the person and arrange urgent assessment through the PD pathway"], 3,
         "Person first. Severe pain with an alarm is a clinical problem until proven otherwise."),
        ("Which check is usually permitted for a drain alarm?",
         ["Checking for closed clamps or kinked lines", "Forceful flushing of the catheter", "Disabling the alarm", "Cutting the line"], 0,
         "External checks per the device instructions are permitted. The others are unsafe."),
        ("Drain volumes fall over several nights and the patient has had no bowel movement for four days. This most suggests:",
         ["Peritonitis", "Normal variation", "Constipation affecting catheter position", "Exit-site infection"], 2,
         "A loaded bowel can displace the catheter tip. Constipation is a common cause of catheter dysfunction."),
        ("What must accompany an escalation for recurring low drain?",
         ["Only &ldquo;the machine keeps alarming&rdquo;", "The patient&rsquo;s address", "Alarm type and phase, frequency, checks tried, symptoms, effluent and therapy delivered", "Nothing; wait for the morning"], 2,
         "Complete data let the team decide without calling back."),
        ("When may backup CAPD be used during a power failure?",
         ["When a prescribed backup regimen, suitable supplies and validated competence exist", "Whenever the patient wishes", "Never", "Only in the hospital"], 0,
         "Backup must be planned and validated before the storm, not improvised during it."),
        ("Swelling of the genitals during APD fill suggests:",
         ["Normal fill", "A possible dialysate leak; report promptly", "Peritonitis", "Constipation"], 1,
         "Leaks can track into the abdominal wall and genitals."),
        ("A patient&rsquo;s drains and UF per night are unchanged, but three nights last week stopped early and weight rose 1.4 kg. What should you explore first?",
         ["The catheter position", "Why therapy was stopped early, and report the lost therapy with the reason", "The solution brand", "Nothing; the volumes are fine"], 1,
         "Read completion before volumes. Undelivered therapy explains the weight gain; the reason may be social, technical or fear of alarms."),
        ("Breathlessness soon after the last fill should prompt:",
         ["Ignoring it", "More fluid", "A larger fill next time", "Urgent assessment for overfill or hydrothorax"], 3,
         "A pleural leak or overfill can make breathing difficult and needs urgent assessment."),
        ("Who sets the APD prescription?",
         ["The PD nurse", "The nephrologist", "The supplier", "The patient"], 1,
         "The nurse verifies the program against the order and monitors the result."),
        ("Why is the cycler record described as a monitoring tool?",
         ["It replaces clinic visits", "It stores the patient&rsquo;s diet", "It shows drain patterns, completion, UF and alarms that reflect the patient&rsquo;s condition", "It sets the prescription automatically"], 2,
         "The record carries clinical signals about the catheter, the bowel, the abdomen and the household."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Icodextrin", "A large glucose polymer solution absorbed slowly, used for long dwells."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Tidal mode", "An APD setting that leaves a reserve volume in the abdomen at each drain."),
              ("Last fill", "The final APD fill that stays in during the day, also called the day dwell."),
              ("Initial drain", "The drain of the day dwell at the start of the night&rsquo;s therapy."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("Hydrothorax", "Dialysate leaking into the chest through a gap in the diaphragm."),
              ("Hernia", "Bulging of abdominal contents through a weak point in the wall.")],
    "readings": [("fluid-management-dialysis.html", "Fluid balance on dialysis."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Preparing dialysis patients for typhoons and outages.")],
    "calcs": ["calc-pd-adequacy.html", "calc-dialysis-continuity-planner.html"],
}
