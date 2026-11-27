# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 8: The PD catheter, exit site and mechanical problems. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Describe pediatric PD catheter design and exit-site placement, and why diapers, gastrostomies and ostomies change the plan.",
        "Perform and teach exit-site care consistent with the 2024 ISPD pediatric guideline and the unit protocol.",
        "Score an exit site and recognize infection signs that need same-day escalation.",
        "Work through poor drainage from simple external causes inward, and know when to stop and call.",
    ],
    "big": """
<p>A PD catheter is a child&rsquo;s lifeline for months or years. It leaves the body through a small exit site and runs through a tunnel under the skin, anchored by cuffs that tissue grows into. Most catheter trouble falls into two families: infection along the tunnel and exit site, and mechanical failure when fluid will not flow.</p>
<p>Your work in this module is to keep the exit site healthy, to notice the first signs of trouble, and to solve simple drainage problems without causing new ones.</p>
{{plain:Think of the exit site as a gate in a fence. The cuffs are the posts that hold the fence tight. If the gate stays clean and dry and the posts stay firm, nothing gets through. If the gate is wet, rubbed or pulled, dirt gets in along the fence line.}}
<p>The picture has a limit. A gate is fixed; a child is not. Children grow, crawl, pull at tubes and wear diapers. The exit site must be placed and protected for the child&rsquo;s life stage, and the catheter must be secured so play does not tug on it.</p>
{{cards:Key terms for this module|Cuff::A felt ring on the catheter that tissue grows into, anchoring it and sealing the tunnel.|Tunnel::The path of the catheter under the skin between the cuffs.|Exit site::Where the catheter leaves the skin.|Exit-site score::A points system for redness, swelling, crusting, pain and drainage.|Outflow failure::Fluid runs in but does not drain out well.}}
""",
    "case": {"title": "He drains half", "html": """
<p><strong>Jun-jun Bautista, 5</strong>, 18 kilograms, has been on PD for three weeks. His father, <strong>Arnel</strong>, calls at 9 p.m.: the cycler keeps alarming, and Jun-jun drained only about half of the 700 mL fill. He has not had a bowel movement for three days. He has no fever, the fluid looks clear, and he says his tummy is &ldquo;a little full&rdquo;. <strong>Nurse Ivy</strong> takes the call.</p>
""", "questions": ["What simple causes should Ivy check first?",
                  "What would make this an urgent call instead of a troubleshooting call?",
                  "What should Arnel not do?"]},
    "sections": [
        ("catheter-design", "Catheter design", "Catheter design and exit-site placement", """
<p>The 2024 ISPD pediatric guideline suggests a double-cuff PD catheter with a downward or lateral exit-site orientation (2D), and perioperative intravenous antibiotics before insertion (2C).[[pdn_warady2024]] A downward exit lets sweat and debris drain away from the tunnel. The exit site is placed away from the diaper line in infants and away from a gastrostomy or ostomy; in children with a colostomy, the guideline&rsquo;s rationale discusses alternatives such as a chest-wall exit.</p>
{{fig:pdn08_a}}
<p>Catheters fail more often in children than many expect. In the IPPN registry, 13% of 2,453 children needed at least one access revision, an overall rate of 0.14 per treatment year; among new patients, catheter survival was 84% at 12 months and 73% at 48 months. Mechanical malfunction caused 60% of revisions, peritonitis 16%, exit-site infection 12% and leakage 6%. Younger age, CAKUT and ostomies were associated with revision, and a revision was associated with a higher risk of technique failure or death.[[pdn_borzych2017]] These are registry associations, but they make the point: protecting the catheter protects the modality.</p>
{{key:Downward or lateral exit, away from diapers and stomas, catheter secured against tugs. Protect the catheter and you protect PD.}}
"""),
        ("exit-site-care", "Exit-site care", "Exit-site care", """
<p>A new exit site is left undisturbed to heal, with dressing changes only as the surgical team orders, usually by trained staff. After healing, routine care begins.</p>
<div class="table-wrap"><table>
<thead><tr><th>ISPD 2024 pediatric statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Routine exit-site care with a sterile cleansing solution 2 to 3 times per week</td><td>2D</td></tr>
<tr><td>A topical antibiotic applied to the exit site whenever exit-site care is performed</td><td>2D</td></tr>
<tr><td>Topical gentamicin may be considered as an alternative to mupirocin</td><td>Rationale text, not a graded statement</td></tr>
</tbody></table></div>
<p>Grade 2D means a weak suggestion on very low-certainty evidence; your unit&rsquo;s protocol decides the agent and frequency.[[pdn_warady2024]] Whatever the protocol, the technique is the same: hand hygiene, a clean surface, look before you clean, clean from the exit outward, dry, apply the ordered agent, secure the catheter so it does not pull, and record what you saw.</p>
<h3>Scoring what you see</h3>
<p>Exit-site scores give points for swelling, crust, redness, tenderness and discharge. The guideline&rsquo;s rationale says an exit-site infection should be assumed with a cumulative score of 4 or more, and purulent discharge alone is diagnostic (19.4, 2C).[[pdn_warady2024]] Score the same way every time so the trend means something, and photograph only if your unit&rsquo;s consent and privacy rules allow it.</p>
{{key:Look, score, then clean. Purulent discharge alone means infection; call the PD team the same day.}}
"""),
        ("when-it-will-not-drain", "Poor drainage", "When it will not drain", """
<p>Outflow failure means fluid runs in but drains slowly or incompletely. Most causes are outside the catheter or easily reversible. Work from the outside in.</p>
{{fig:pdn08_b}}
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Why</th><th>What the caregiver can do</th></tr></thead>
<tbody>
<tr><td>Clamps open, lines not kinked, bag below the abdomen</td><td>Simple obstruction</td><td>Check every clamp and the line path</td></tr>
<tr><td>Position</td><td>The catheter tip may lie against bowel</td><td>Change position, sit up, turn</td></tr>
<tr><td>Constipation and full bladder</td><td>A loaded bowel pushes on the catheter tip or kinks it</td><td>Report; laxatives only as ordered</td></tr>
<tr><td>Fibrin (white strands in the fluid)</td><td>Fibrin can block the catheter</td><td>Report; heparin in the bag only as ordered</td></tr>
<tr><td>Catheter migration or omental wrap</td><td>Needs imaging or a procedure</td><td>None; the team decides</td></tr>
</tbody></table></div>
{{call:Stop troubleshooting and call the PD team at once, per unit protocol, if drainage problems come with abdominal pain, fever, cloudy fluid, vomiting, a swollen or tender exit site, leakage at the exit site, or breathing difficulty. Never flush a PD catheter forcefully or use a syringe on it unless your unit protocol and training allow it.}}
{{key:Clamps, kinks, position, bowels, fibrin, then call. Pain, fever or cloudy fluid turns a drainage problem into an urgent one.}}
"""),
    ],
    "debrief": ["""
<p><strong>Simple causes first.</strong> Ivy asks Arnel to check every clamp and the line path, to sit Jun-jun up and turn him, and to look for white strands in the bag. Three days without a bowel movement makes constipation the likely cause.</p>
<p><strong>What would make it urgent.</strong> Pain, fever, cloudy fluid, vomiting, leakage or breathing difficulty. None is present now, so Ivy reports to the PD nephrologist the same evening for a constipation plan and a review of how to continue the night.</p>
<p><strong>What not to do.</strong> No forceful flushing, no syringe on the catheter, no stronger dextrose bag to &ldquo;pull more&rdquo;, and no skipping the rest of the night without the team&rsquo;s advice. Ivy documents the call and the plan.</p>
"""],
    "skills": {"title": "Exit site and drainage", "intro": "Use a training catheter and photographs.",
               "items": [("Performs exit-site care with hand hygiene, assessment before cleaning, and catheter securing", True),
                         ("Scores exit sites from photographs consistently with a colleague", False),
                         ("Recognizes purulent discharge as infection and escalates the same day", True),
                         ("Talks a caregiver through external drainage checks by telephone", False),
                         ("Stops troubleshooting and escalates when pain, fever or cloudy fluid appear", True)]},
    "quiz": [
        ('ISPD 2024 pediatric guideline suggests which catheter and exit orientation?',
         ['Double cuff, downward or lateral exit (2D)', 'Single cuff, upward exit', 'Any catheter', 'Double cuff, upward exit'], 0,
         'Downward exits let debris drain away.'),
        ('Why place the exit site away from the diaper area in infants?',
         ['Appearance', 'To reduce contamination by urine and stool', 'It is easier to insert', 'No reason'], 1,
         'Diapers are a route for infection.'),
        ('In the IPPN registry, what share of children needed at least one PD access revision?',
         ['1%', '50%', '13%', '90%'], 2,
         '321 of 2,453 children.'),
        ('Most pediatric PD catheter revisions were caused by:',
         ['Peritonitis', 'Leakage', 'Cost', 'Mechanical malfunction (60%)'], 3,
         'Mechanical problems dominated.'),
        ('Routine exit-site care frequency suggested by ISPD 2024 pediatric:',
         ['2 to 3 times per week (2D)', 'Daily always', 'Monthly', 'Never'], 0,
         'A weak suggestion; follow the unit protocol.'),
        ('Grade 2D means:',
         ['Strong recommendation, high certainty', 'Weak suggestion, very low certainty', 'Law', 'Not graded'], 1,
         'Level 2 = suggest; D = very low certainty.'),
        ('Which finding alone defines an exit-site infection?',
         ['Mild redness', 'A crust', 'Purulent discharge', 'Itching'], 2,
         'Statement 19.4 (2C).'),
        ('An exit-site infection should be assumed at a cumulative score of:',
         ['1', '2', '10', '4 or more'], 3,
         'From the guideline&rsquo;s rationale.'),
        ('First check for poor drainage:',
         ['Clamps, kinks and bag position', 'Order imaging', 'Give antibiotics', 'Remove the catheter'], 0,
         'External causes are common and simple.'),
        ('Three days without a bowel movement and poor drainage suggests:',
         ['Peritonitis', 'Constipation pushing on the catheter', 'Leak', 'Hernia'], 1,
         'Report for a laxative plan as ordered.'),
        ('White strands in the effluent are likely:',
         ['Pus', 'Food', 'Fibrin', 'Glucose'], 2,
         'Heparin only as ordered.'),
        ('Which turns a drainage call into an urgent one?',
         ['Clear fluid', 'A bowel movement', 'Good appetite', 'Abdominal pain, fever or cloudy fluid'], 3,
         'Infection must be excluded.'),
        ('Should a caregiver forcefully flush the PD catheter?',
         ['No, unless protocol and training allow', 'Yes', 'Only at night', 'Only with saline'], 0,
         'Force can damage the catheter.'),
        ('A catheter revision in the IPPN registry was associated with:',
         ['Better survival', 'Higher risk of technique failure or death', 'No change', 'Shorter dialysis'], 1,
         'An association that underlines catheter protection.'),
        ('Why secure the catheter against pulling?',
         ['Looks tidy', 'To stop drainage', 'Tugging damages the tunnel and exit site', 'Required for school'], 2,
         'Children move and play.'),
    ],
    "terms": [("Cuff", "A felt ring on the catheter that anchors it and seals the tunnel."),
              ("Tunnel", "The catheter&rsquo;s path under the skin."),
              ("Exit site", "Where the catheter leaves the skin."),
              ("Outflow failure", "Fluid drains slowly or incompletely."),
              ("Fibrin", "Protein strands that can block a catheter."),
              ("Omental wrap", "The omentum, a fatty apron in the abdomen, wrapping around the catheter tip.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis basics for families."),
                 ("dialysis-access-infection.html", "Access infections and their prevention.")],
    "calcs": [],
}
