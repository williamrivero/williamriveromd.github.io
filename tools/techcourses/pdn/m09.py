# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 9: CAPD, a supervised exchange in a small body. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Prepare the room, the supplies and the child for a manual exchange, including distraction and positioning.",
        "Perform a supervised manual exchange with key-part protection and accurate small-volume measurement.",
        "Distinguish dry from wet contamination and take the right next step for each.",
        "Record volumes, appearance and timing so that trends can be read.",
    ],
    "big": """
<p>The steps of a manual exchange are the same for a child as for an adult: drain, flush, fill. What makes pediatric continuous ambulatory PD (CAPD) different is the small volume, the child who may not hold still, and the measurement errors that matter more when every bag is small. A 50 mL measuring error is trivial in a 2,000 mL adult exchange; in a 300 mL infant exchange it is one-sixth of the bag.</p>
<p>Your work in this module is to perform and teach an exchange that is clean, accurate and calm, and to recognize and report a contamination honestly.</p>
{{plain:Think of the exchange as a short flight: pre-flight checks, takeoff, cruise and landing. Most accidents happen at takeoff and landing, the moments of connection and disconnection. That is where your full attention belongs.}}
<p>The picture has a limit. A plane&rsquo;s passengers sit belted. A toddler does not. Plan the child&rsquo;s position, comfort and distraction before you open anything, and have a second pair of hands if the child may move.</p>
{{cards:Key terms for this module|Flush before fill::Running a little fresh fluid from the bag to the drain before filling, to wash away any contamination at the connection.|Dry contamination::A break in technique with the system clamped and no fluid flow.|Wet contamination::A break in technique while fluid was flowing, or a disconnection with an open system.|Effluent::The drained fluid.|Net ultrafiltration::Drained volume minus filled volume.}}
""",
    "case": {"title": "The cap on the floor", "html": """
<p><strong>Nurse Tess</strong> is supervising <strong>Lola Pilar</strong>, 62, who is learning to do exchanges for her grandson <strong>Kiko, 4</strong>, 16 kilograms. Kiko wriggles as Lola Pilar opens the new bag. The transfer-set cap slips from her fingers to the floor while the line is open to the patient side. Lola Pilar quickly picks up a new cap and says, &ldquo;No harm done.&rdquo;</p>
""", "questions": ["Is this a dry or a wet contamination, and what difference does it make?",
                  "What should Tess do in the next five minutes?",
                  "How could the setup have prevented this?"]},
    "sections": [
        ("before-the-exchange", "Preparation", "Before the exchange", """
<p>Most errors are prevented before the bag is opened.</p>
<ul>
<li><strong>The space:</strong> clean, closed windows and fans off, pets out, a clean surface, good light.</li>
<li><strong>The supplies:</strong> correct bag and dextrose strength, expiry date, clear fluid, no leaks, warmed by the approved dry method only, never in water or a microwave.</li>
<li><strong>The order:</strong> fill volume in mL, checked against the child&rsquo;s BSA as in Module 7.</li>
<li><strong>The child:</strong> toileted if possible, positioned comfortably, with a distraction ready: a song, a video, a toy, a parent&rsquo;s hand. For a child likely to move, a second adult holds and comforts, not restrains.</li>
<li><strong>The performer:</strong> mask as the protocol requires, hand hygiene, no jewelry, no phone in the hands.</li>
</ul>
{{key:Prepare the child as carefully as the bag. A calm child is a clean exchange.}}
"""),
        ("the-exchange", "The exchange", "The exchange, step by step", """
<p>Follow the device&rsquo;s instructions and the unit procedure. The physiology behind the steps does not change.</p>
{{fig:pdn09_a}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Connect without touching key parts</td><td>Connection is the main contamination point</td></tr>
<tr><td>Drain fully, with the child lying or reclining</td><td>Incomplete drains leave fluid that adds to the next fill and raises pressure</td></tr>
<tr><td>Flush before fill</td><td>Washes contamination at the connection into the drain bag, not the abdomen</td></tr>
<tr><td>Fill only the ordered volume</td><td>In small bags, measure by weight or graduated markings as the protocol says</td></tr>
<tr><td>Disconnect and cap without touching key parts</td><td>The second high-risk moment</td></tr>
<tr><td>Inspect and measure the effluent</td><td>Cloudiness, fibrin, blood; net ultrafiltration</td></tr>
</tbody></table></div>
<p>Measure small volumes the way your unit validated: weighing bags (1 gram of fluid is about 1 mL) is usually more accurate than reading markings on a soft bag. Record drained volume, filled volume, net ultrafiltration, appearance and time.</p>
{{key:Connection and disconnection are takeoff and landing. Full attention, no touching, no talking over the open line.}}
"""),
        ("contamination", "Contamination", "Dry versus wet contamination", """
<p>A contamination is a break in technique that may have let organisms into the system. What happens next depends on whether fluid flowed.</p>
{{fig:pdn09_b}}
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>What happened</th><th>Usual next step (per protocol)</th></tr></thead>
<tbody>
<tr><td>Dry</td><td>Break with the system clamped and no fluid flow, for example touching a connector before connection</td><td>Clamp, cover, replace the contaminated part as the protocol says, report</td></tr>
<tr><td>Wet</td><td>Break while fluid was flowing or the system was open to the patient, for example a disconnection with an open transfer set</td><td>Clamp at once, cover, call the PD team for transfer-set change and the prophylaxis decision</td></tr>
</tbody></table></div>
<p>The 2024 ISPD pediatric guideline suggests prophylactic antibiotics after wet contamination of the PD system (7.4, 2D), and its rationale describes a single intraperitoneal dose of cefazolin as reasonable for most patients.[[pdn_warady2024]] The choice and dose are the team&rsquo;s. Your job is to recognize the event, stop, protect the line and report it honestly, without blame, so the caregiver keeps reporting.</p>
{{scene:The cap on the floor|<p>Tess says calmly, &ldquo;Let&rsquo;s stop and clamp.&rdquo; She clamps the transfer set, covers the end with a sterile cap from her kit, and explains that because the line was open to Kiko, this counts as a wet contamination. She calls the PD nephrologist for the transfer-set change and prophylaxis decision, then praises Lola Pilar for saying what happened.</p><p class="tc-scene-take">A contamination reported is a contamination managed. Thank the person who reports it.</p>}}
{{key:Stop, clamp, cover, call. Wet contamination needs the team&rsquo;s prophylaxis decision; dry contamination still gets reported.}}
"""),
    ],
    "debrief": ["""
<p><strong>Type.</strong> The transfer set was open to the patient side when the cap fell, so it is a wet contamination, which carries more risk than a dry one.</p>
<p><strong>The next five minutes.</strong> Clamp, cover with a sterile cap, call the PD team for the transfer-set change and the prophylaxis decision, document the time and event, and watch Kiko for fever, pain or cloudy fluid in the coming days.</p>
<p><strong>Prevention.</strong> A second adult to comfort and steady Kiko, a distraction ready before opening, and supplies laid out within reach so no hand leaves the line. Lola Pilar&rsquo;s training continues until she shows a clean exchange with a moving child.</p>
"""],
    "skills": {"title": "Supervised manual exchange", "intro": "Simulation on a training model first, then supervised practice.",
               "items": [("Prepares the space, checks bag, strength, expiry, clarity and fill volume against the order", True),
                         ("Positions and prepares the child with comfort and distraction", False),
                         ("Connects, drains, flushes, fills and disconnects without touching key parts", True),
                         ("Measures small volumes by the unit&rsquo;s validated method and records net ultrafiltration", False),
                         ("Recognizes a wet contamination, clamps, covers and calls the PD team", True)]},
    "quiz": [
        ('A 50 mL measuring error in a 300 mL exchange is about:',
         ['1%', 'One-sixth of the bag', 'Half', 'Nothing'], 1,
         '50 &divide; 300 &asymp; 17%.'),
        ('Why flush before fill?',
         ['To warm the fluid', 'To save fluid', 'To wash connection contamination into the drain bag', 'To remove air only'], 2,
         'Contamination goes to the drain, not the abdomen.'),
        ('How should PD bags be warmed?',
         ['Microwave', 'Hot water bath', 'Not at all', 'The approved dry method'], 3,
         'Wet and microwave warming risk contamination and burns.'),
        ('Which are the highest-risk moments of an exchange?',
         ['Connection and disconnection', 'Reading the order', 'Drain measurement', 'Disposal'], 0,
         'Takeoff and landing.'),
        ('How is a small drained volume measured most accurately?',
         ['Guessing', 'Weighing the bag (1 g &asymp; 1 mL) as validated', 'Reading a soft bag&rsquo;s markings always', 'Counting drops'], 1,
         'Follow the unit&rsquo;s validated method.'),
        ('Net ultrafiltration equals:',
         ['Fill minus drain', 'Drain only', 'Drain minus fill', 'Fill only'], 2,
         'Positive means fluid removed.'),
        ('A connector is touched before connection, system clamped. This is:',
         ['Wet contamination', 'Peritonitis', 'Normal', 'Dry contamination'], 3,
         'No fluid flowed.'),
        ('A cap falls with the transfer set open to the patient. This is:',
         ['Wet contamination', 'Dry contamination', 'No contamination', 'A leak'], 0,
         'The system was open.'),
        ('ISPD 2024 pediatric on wet contamination:',
         ['No action', 'Suggests prophylactic antibiotics (7.4, 2D)', 'Remove the catheter', 'Stop PD'], 1,
         'The team chooses the agent.'),
        ('Who decides the antibiotic after wet contamination?',
         ['The caregiver', 'The nurse', 'The PD nephrologist or team', 'The pharmacist alone'], 2,
         'The nurse recognizes and reports.'),
        ('Why thank a caregiver who reports a contamination?',
         ['Politeness only', 'Required by law', 'To end the call', 'So they keep reporting instead of hiding events'], 3,
         'Blame drives events underground.'),
        ('What should a second adult do for a wriggling toddler?',
         ['Comfort and steady the child', 'Restrain forcefully', 'Leave the room', 'Do the exchange'], 0,
         'Comfort, not force.'),
        ('Before opening the bag you check:',
         ['Only the color', 'Strength, volume, expiry, clarity and leaks', 'Only the expiry', 'Nothing'], 1,
         'Pre-flight checks.'),
        ('Incomplete drains matter because:',
         ['They waste fluid', 'They look bad', 'Leftover fluid adds to the next fill and raises pressure', 'They change the color'], 2,
         'Overfill raises intraperitoneal pressure.'),
        ('After a contamination, watch the child for:',
         ['Hunger', 'Sleepiness only', 'Nothing', 'Fever, abdominal pain or cloudy fluid'], 3,
         'Early peritonitis signs.'),
    ],
    "terms": [("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Transfer set", "The short tube attached to the PD catheter where connections are made."),
              ("Flush before fill", "Running fresh fluid to the drain before filling."),
              ("Dry contamination", "A break in technique with no fluid flow."),
              ("Wet contamination", "A break in technique while fluid flowed or the system was open."),
              ("Net ultrafiltration", "Drained volume minus filled volume.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis for families."),
                 ("adding-peritoneal-dialysis-program.html", "How a PD program supports home exchanges.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html"],
}
