# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 04: The CAPD exchange, measurement and contamination response.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain why the &ldquo;flush before fill&rdquo; step in a twin-bag (double-bag) system protects the peritoneum, and the trial evidence behind it.",
        "Verify an exchange against the written order and reject a compromised supply.",
        "Demonstrate a continuous ambulatory peritoneal dialysis (CAPD) exchange in simulation using the unit&rsquo;s approved checklist for the actual device.",
        "Calculate and interpret net ultrafiltration for an exchange and for a day, including the measurement errors that distort it.",
        "Classify a contamination event as dry or wet, and run the contamination call with the details the team needs.",
    ],
    "big": """
<p>A patient on CAPD performs more than a thousand exchanges a year. Each one is a moment when the sterile inside of the system is briefly open to the room. Nearly all peritonitis from touch contamination starts with one lapse in one of those moments.</p>
<p>Your work in this module has three parts. Teach a technique that is the same every time. Make measurement honest, so the numbers in the diary mean what they say. And make sure that when a lapse happens, as it will, the patient stops and calls instead of hoping it will be fine.</p>
{{plain:Think of an exchange as a sealed water system with one valve you must open by hand. As long as nothing touches the valve&rsquo;s inner surfaces, the system stays clean. The moment a finger, a sleeve or a drop of tap water touches the inside of a connector, the system is no longer closed.}}
<p>The picture has a limit. PD solution is not just water. It is a warm, glucose-rich fluid, an excellent place for bacteria to grow. A few bacteria introduced at connection can multiply during a four-hour dwell inside the abdomen. That is why a single touch matters, and why the response is measured in hours.</p>
{{cards:Key terms for this module|Transfer set::The short tube permanently attached to the catheter, which the patient connects to each new bag.|Flush before fill::Sending a little fresh solution straight to the drain bag before filling, to wash out bacteria introduced at connection.|Net ultrafiltration (UF)::Drained volume minus filled volume for an exchange.|Dry contamination::A break in technique with the system closed and no fluid infused after it.|Wet contamination::A break with the system open, fluid infused after it, or a leak.}}
""",
    "case": {"title": "A sleeve and a connector", "html": """
<p><strong>Tita Carmen, 63</strong>, a retired seamstress from Caloocan, is in her second week of CAPD training. Nurse <strong>Bea</strong> observes from beside the training table.</p>
<p>Carmen checks her bag, washes her hands and connects. During the drain phase she reaches up to scratch her nose. Her sleeve brushes the open connector of the new bag line before she connects it. She freezes, glances at Bea, then reaches for an alcohol swab.</p>
<p>&ldquo;Sorry, ma&rsquo;am,&rdquo; she says. &ldquo;I will just clean it.&rdquo;</p>
""", "questions": ["What kind of contamination is this, dry or wet?",
                  "What do you do with the bag and the exchange?",
                  "What do you say to Carmen so she keeps reporting?"]},
    "sections": [
        ("the-physiology-and", "Why the technique works", "The physiology and the engineering", """
<h3>Why &ldquo;flush before fill&rdquo; works</h3>
<p>Modern CAPD uses a Y-shaped twin-bag system: one tube to a fresh bag, one to a drainage bag, joined to the patient&rsquo;s transfer set. After connecting, the patient drains the abdomen first. Then a small amount of fresh solution flushes straight into the drainage bag. Any bacteria introduced at the moment of connection are washed into the drain bag instead of being pushed into the peritoneum. Only then does fresh solution fill the abdomen.</p>
{{fig:pd04_flush}}
<h3>The evidence</h3>
<p>A Cochrane systematic review of 12 randomized or quasi-randomized trials (991 patients) found that Y-set or double-bag systems reduced the proportion of patients who developed peritonitis compared with older standard spike systems (odds ratio 0.33, 95% confidence interval 0.24 to 0.46). Double-bag systems also did better than Y-sets (odds ratio 0.44, 95% confidence interval 0.27 to 0.71).[[pd_daly2001]]</p>
<p>This is strong, replicated randomized evidence on an outcome patients feel. It is why twin-bag systems are the standard. The trials are old and were done mostly in high-income settings, but the mechanism is direct and the effect is large. When a patient asks why they must flush every time, this is the answer: the step was tested, and it works.</p>
<h3>What the patient controls</h3>
<p>The system does its part. The patient controls the rest: hand hygiene, a clean surface, no fan or open window blowing toward the connection, no pets in the room, a mask if the program requires one, never touching the connector tips, and checking every bag before using it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common home habit</th><th>Why it matters</th><th>What to teach</th></tr></thead>
<tbody>
<tr><td>Electric fan running toward the table to keep cool</td><td>Moves dust and droplets toward an open connector</td><td>Turn the fan off or away during connection</td></tr>
<tr><td>Doing the exchange while watching a teleserye in the sala</td><td>Interruptions and visitors</td><td>One closed room, no visitors, phone silent</td></tr>
<tr><td>Wiping hands on a shared towel</td><td>Recontaminates clean hands</td><td>Single-use paper towel or the program&rsquo;s method</td></tr>
<tr><td>The cat sleeps on the exchange table</td><td>Animal contact near the connection</td><td>Pets out of the room; wipe the surface</td></tr>
</tbody></table></div>
{{key:Flush before fill was tested in trials and works. Teach it as a non-negotiable step, not a habit.}}
"""),
        ("before-the-exchange", "Before the exchange", "Before the exchange", """
<p>Use the approved checklist for the system the patient actually has. The steps below are principles, not a procedure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Patient identity and current written order</td><td>Orders change. An outdated card at home is a common error.</td></tr>
<tr><td>Solution type and strength, for example 1.5%, 2.5% or 4.25% dextrose, or icodextrin</td><td>The wrong strength changes fluid removal; the wrong product can cause harm.</td></tr>
<tr><td>Fill volume and dwell timing</td><td>Prescribed by the nephrologist.</td></tr>
<tr><td>Expiry, clarity, seals, pull rings, package integrity</td><td>A leaking or cloudy bag may be contaminated.</td></tr>
<tr><td>Warming method</td><td>Only approved dry warming methods. Never a microwave or a hot water bath unless the device instructions allow it.</td></tr>
<tr><td>Environment and hand hygiene</td><td>Clean, closed room; hands washed and dried per program.</td></tr>
</tbody></table></div>
<h3>Example: the order on the refrigerator door</h3>
<p>Nurse Rhea visits Mr. Efren at home. Taped to the refrigerator is his prescription card from eight months ago: four exchanges of 1.5%. Two months ago the nephrologist changed his night bag to a stronger solution. His wife has been buying supplies from the old card. Nobody did anything careless; the card simply never changed.</p>
<p>Rhea replaces the card with the current order, dates it and asks the supplier to confirm the delivery list. She documents the mismatch and tells the nephrologist, because two months on the wrong night bag may explain his recent weight gain.</p>
<h3>Example: two bags in poor light</h3>
<p>Mrs. Nora keeps her supplies in a dim storeroom. The labels for two strengths look alike at arm&rsquo;s length. She reads the strength aloud every time now, at the exchange table, under a lamp. The habit costs five seconds.</p>
{{key:Replace any questionable supply before you begin. A doubtful bag is never &ldquo;probably fine.&rdquo;}}
"""),
        ("during-and-after", "During and after", "During and after", """
<p>Follow the device instructions for connection, drain, flush, fill and disconnection. Protect the critical parts from touch. Watch comfort and flow.</p>
<p>Look at the drained effluent against a printed page or a white background. You should be able to read through it. Cloudy effluent is a same-day call (Module 7). Teach patients to do this at every exchange, including the ones done half-asleep at 6 AM.</p>
<p>Record the actual fill and drain volumes, dwell timing, effluent appearance, symptoms and any deviation. A deviation recorded honestly is useful. A diary filled in from memory at the end of the week is not.</p>
<div class="table-wrap"><table>
<thead><tr><th>What the patient notices</th><th>What it may mean</th><th>What to teach</th></tr></thead>
<tbody>
<tr><td>Drain slower than usual</td><td>Position, constipation, kinked line, catheter problem (Module 8)</td><td>Change position, check clamps and lines, record the time; call if it persists</td></tr>
<tr><td>Pain on inflow</td><td>Cold solution, fast flow, catheter position</td><td>Check warming; report pain that persists or is severe</td></tr>
<tr><td>Fibrin strands in the bag</td><td>Protein strands that can block the catheter</td><td>Record and report per protocol</td></tr>
<tr><td>Cannot read print through the bag</td><td>Cloudy effluent, possible peritonitis</td><td>Save the bag and call the PD unit today</td></tr>
</tbody></table></div>
"""),
        ("measuring-ultrafiltration-honestly", "Measuring UF", "Measuring ultrafiltration honestly", """
<p><strong>Net UF for one exchange = drained volume &minus; filled volume.</strong> A positive number means fluid was removed. A negative number means fluid was absorbed.</p>
{{key:Daily net UF is the sum of all exchanges in 24 hours.}}
<h3>Worked example: one day&rsquo;s diary</h3>
<div class="table-wrap"><table>
<thead><tr><th>Exchange</th><th>Filled</th><th>Drained</th><th>Net UF</th></tr></thead>
<tbody>
<tr><td>6 AM</td><td>2,000 mL</td><td>1,900 mL</td><td>&minus;100 mL</td></tr>
<tr><td>11 AM</td><td>2,000 mL</td><td>2,350 mL</td><td>+350 mL</td></tr>
<tr><td>4 PM</td><td>2,000 mL</td><td>2,250 mL</td><td>+250 mL</td></tr>
<tr><td>9 PM</td><td>2,000 mL</td><td>2,200 mL</td><td>+200 mL</td></tr>
<tr><td><strong>Total</strong></td><td></td><td></td><td><strong>+700 mL</strong></td></tr>
</tbody></table></div>
<p>The 6 AM drain follows the long night dwell, so a small negative number may be expected physiology with glucose (Module 1). It may also signal a problem. Trend it and report it with weight and urine.</p>
<h3>Most errors come from measurement, not physiology</h3>
<div class="table-wrap"><table>
<thead><tr><th>Source of error</th><th>Effect</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>Bag overfill (manufacturers may add volume beyond the labeled fill)</td><td>Overestimates or distorts UF, depending on the method</td><td>Use the unit&rsquo;s standard method, weighing bags or labeled volume, consistently</td></tr>
<tr><td>Flush volume going to the drain bag</td><td>Inflates &ldquo;drain&rdquo; if not accounted for</td><td>Teach the unit&rsquo;s convention</td></tr>
<tr><td>Incomplete drain</td><td>Underestimates UF; leaves fluid in the abdomen</td><td>Check position and drain time; report a persistent incomplete drain</td></tr>
<tr><td>Spills or leaks</td><td>Unknown loss</td><td>Record as a deviation</td></tr>
<tr><td>Different scales or methods day to day</td><td>False trends</td><td>Same scale, same method, same time</td></tr>
</tbody></table></div>
<h3>Example: the UF that fell overnight</h3>
<p>Mr. Gary&rsquo;s daily UF dropped from about +800 mL to about +450 mL in one week. Before anyone suspected the membrane, Nurse Rhea asked one question: &ldquo;Did anything change in how you measure?&rdquo; His son had started weighing the bags on the kitchen scale instead of the bathroom scale, and had stopped subtracting the empty-bag weight the same way. With the old method restored, the numbers returned. Nothing was wrong with Mr. Gary. Something was wrong with the arithmetic.</p>
{{key:Before you read a falling UF as physiology, rule out a change in measurement.}}
{{fig:pd04_fig_04_net_uf_diary_error_sources}}
"""),
        ("contamination-dry-or", "Contamination", "Contamination: dry or wet", """
<p>The 2022 International Society for Peritoneal Dialysis (ISPD) peritonitis recommendations revised the guidance on managing contamination of the PD system.[[pd_li2022]] Programs commonly classify events this way.</p>
{{fig:pd04_contam}}
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>What happened</th><th>Typical program response (per protocol and prescriber)</th></tr></thead>
<tbody>
<tr><td><strong>Dry contamination</strong></td><td>A break in sterile technique, but the system was closed (clamp shut) and no fluid was infused after the break</td><td>Stop. Do not proceed with that connection. Replace the affected part, for example a cap or the transfer set, as the program directs. Report.</td></tr>
<tr><td><strong>Wet contamination</strong></td><td>The system was open, fluid was infused after the break, or there is a leak</td><td>Stop. Clamp. Do not fill, or stop filling. Call the PD team at once. The team may send effluent for testing and may prescribe preventive antibiotics.</td></tr>
</tbody></table></div>
<h3>Example: sort these events</h3>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Classification</th><th>Why</th></tr></thead>
<tbody>
<tr><td>The cap of the transfer set falls on the floor before connection. The clamp is closed.</td><td>Dry</td><td>The system stayed closed and nothing was infused. Replace per program.</td></tr>
<tr><td>A brownout during the fill; the patient gropes for a flashlight and touches the connection with the clamp open.</td><td>Wet</td><td>The system was open at the touch, and filling continued.</td></tr>
<tr><td>A crack appears in the transfer set and solution drips from it.</td><td>Wet</td><td>A leak means the system is open.</td></tr>
<tr><td>The grandchild touches the new bag&rsquo;s connector tip before it is attached; clamp closed.</td><td>Dry</td><td>Closed system, no fluid infused. Use a new bag.</td></tr>
</tbody></table></div>
<h3>The contamination call</h3>
<p>State exactly what touched what, when, whether the clamp was closed, whether any fluid entered after the touch, whether the transfer set or catheter is damaged, and whether there are symptoms. Record the time of the call, who accepted it and the instructions given, read back.</p>
<p>A good call sounds like this: &ldquo;This is Nurse Rhea about Mr. Efren, CAPD. At 7:10 this evening, during the fill, the power went out and he touched the connection with the clamp open. About 500 mL had filled after the touch. Transfer set intact. No pain, effluent from the last drain clear. Requesting instructions.&rdquo;</p>
<h3>The teaching message</h3>
<p>&ldquo;If anything touches the tip, stop and call. Do not wipe it and continue.&rdquo; Alcohol on a touched connector does not make it sterile again. Patients who fear blame hide contamination, and hidden contamination becomes peritonitis three days later. Make calling feel safe.</p>
{{call:Call the PD team at once for any wet contamination. Do not continue the fill while you wait.}}
"""),
        ("red-flags-in", "Red flags", "Red flags in this module", """
{{stop:<ul><li>Cloudy effluent at any exchange.</li><li>Fluid leaking around the exit site during fill.</li><li>Severe pain on inflow or outflow.</li><li>A cracked transfer set or catheter.</li></ul>}}
<p>Each of these goes to the PD team the same day. A cracked transfer set with leaking fluid is also a wet contamination, so clamp above the crack if the program teaches it, and call at once.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Dry or wet?</strong> The clamp on the new line is closed and no fresh fluid has been infused. This is dry contamination of the new bag&rsquo;s connector.</p>
<p><strong>What Bea does.</strong> Bea stops the exchange. She discards that bag, has Carmen wash her hands again, uses a fresh bag and completes the exchange. She records the event and tells the PD nurse coordinator.</p>
<p><strong>What she says.</strong> Then she uses the moment. &ldquo;You did the right thing by stopping. The swab does not make it clean again, so next time, stop and call me before you wipe anything. At home, you call the PD line. Nobody will scold you for calling.&rdquo;</p>
<p><strong>Later that week.</strong> Carmen&rsquo;s exchange reads 2,350 mL drained from a 2,000 mL fill: net UF +350 mL, clear effluent. Bea asks her to say aloud what she would do if the drained fluid were cloudy. Carmen answers: &ldquo;Save the bag and call the PD unit today.&rdquo;</p>
"""],
    "skills": {"title": "CAPD exchange with a compromised bag (OSCE station 1)",
               "intro": "Using a mock order and a training kit, identify a seeded packaging defect, perform the exchange with the approved checklist, and rehearse both a dry and a wet contamination call with your preceptor acting as the on-call nurse.",
               "items": [("Verifies patient identity and the written prescription.", True),
                         ("Rejects a compromised supply.", True),
                         ("Protects critical parts and stops at a breach.", True),
                         ("Demonstrates the device-specific flow using the approved checklist.", False),
                         ("Records volumes and effluent appearance.", False)]},
    "quiz": [
        ("Why does flushing fresh solution to the drain bag before filling reduce peritonitis risk?",
         ["It washes bacteria introduced at connection into the drain bag instead of the peritoneum", "It warms the solution", "It removes glucose", "It measures the fill volume"], 0,
         "That is the mechanism of flush before fill. It does not warm, remove glucose or measure anything."),
        ("In the Cochrane review of 12 trials, Y-set or double-bag systems compared with standard systems:",
         ["Increased peritonitis", "Had no effect", "Reduced the proportion of patients with peritonitis (odds ratio 0.33)", "Were never tested in trials"], 2,
         "Randomized evidence showed a large reduction, which is why twin-bag systems are the standard."),
        ("Fill 2,000 mL, drain 1,850 mL. What is net UF?",
         ["+150 mL", "3,850 mL", "0 mL", "&minus;150 mL"], 3,
         "1,850 minus 2,000 is &minus;150 mL: fluid was absorbed."),
        ("Fill 2,000 mL, drain 2,350 mL. What is net UF?",
         ["&minus;350 mL", "+350 mL", "+2,350 mL", "+4,350 mL"], 1,
         "2,350 minus 2,000 is +350 mL: fluid was removed."),
        ("A bag has a small leak at the seal. Best action?",
         ["Use it quickly", "Replace it before beginning and report the defect", "Tape the leak", "Use it for the drain bag only"], 1,
         "A compromised bag may be contaminated. Never use it, and report the defect so the supplier can check the batch."),
        ("The patient touches the tip of the new bag connector; the clamp is closed and no fluid has entered. This is:",
         ["Wet contamination", "Not contamination", "Peritonitis", "Dry contamination"], 3,
         "The system stayed closed and nothing was infused after the break."),
        ("During a brownout, the patient touches the connection with the clamp open and the fill continues. This is best classified as:",
         ["Wet contamination; clamp and call the PD team at once", "Dry contamination", "A normal event", "A drain alarm"], 0,
         "The system was open at the touch and fluid entered afterward."),
        ("What information matters most in a contamination call?",
         ["The patient&rsquo;s favorite food", "Only the time", "What touched what, when, clamp status, whether fluid entered, damage and symptoms", "The brand of solution only"], 2,
         "These details tell the team which response fits."),
        ("Which warming method is acceptable?",
         ["Microwave", "Hot water bath", "Only the approved dry warming method per device instructions", "Direct sunlight"], 2,
         "Other methods risk overheating or contaminating the bag."),
        ("Mr. Gary&rsquo;s UF fell sharply in one week, just after his son began weighing bags on a different scale. What should you consider first?",
         ["Membrane failure", "A change in measurement", "Peritonitis", "That he is drinking less"], 1,
         "Rule out a measurement change before reading a falling UF as physiology."),
        ("A patient wipes the touched connector with alcohol and continues. The best teaching response is:",
         ["Praise her for cleaning it", "Explain that a touched sterile part means stopping and calling, and make calling feel safe", "Ignore it", "Report her for noncompliance"], 1,
         "Wiping does not restore sterility, and blame discourages reporting."),
        ("How can a patient check effluent clarity simply?",
         ["Smell it", "Taste it", "Shake it", "Look through it at printed text or a white background"], 3,
         "If print cannot be read through it, the effluent may be cloudy."),
        ("Mr. Efren&rsquo;s wife has been buying supplies from an eight-month-old prescription card. What is the best response?",
         ["Tell her to keep using it until the next visit", "Replace the card with the current dated order, confirm deliveries, and tell the nephrologist", "Change the solution yourself", "Ignore it if he feels well"], 1,
         "Verification against the current order is nursing work. The mismatch may explain clinical changes, so the nephrologist needs to know."),
        ("Who decides whether preventive antibiotics are given after wet contamination?",
         ["The patient", "The prescriber, per the unit&rsquo;s protocol", "The nurse alone", "The supplier"], 1,
         "Antibiotic decisions belong to the prescriber or a written standing protocol."),
        ("Why is a single touch contamination significant in PD?",
         ["It changes solution strength", "It damages the catheter", "PD solution is a warm, glucose-rich fluid where bacteria can multiply during a dwell", "It is not significant"], 2,
         "A few bacteria can grow during the dwell, which is why the response is time-sensitive."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Icodextrin", "A large glucose polymer solution absorbed slowly, used for long dwells."),
              ("Transfer set", "The short tube attached to the catheter that connects to each new bag."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Flush before fill", "Sending a little fresh solution straight to the drain bag before filling, to wash out bacteria introduced at connection."),
              ("Dry contamination", "A break in sterile technique with the system closed and no fluid infused after the break."),
              ("Wet contamination", "A break with the system open, fluid infused after the break, or a leak."),
              ("Fibrin", "Protein strands that can appear in effluent and may block the catheter."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell.")],
    "readings": [("peritoneal-dialysis-ckd.html", "What patients learn about exchanges at home.")],
    "calcs": ["calc-pd-glucose-absorption.html"],
}
