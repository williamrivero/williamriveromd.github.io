# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 5: Infection prevention and access protection. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Trace how organisms reach a child&rsquo;s bloodstream or peritoneum, including routes unique to children.",
        "Protect key parts and catheter hubs with aseptic non-touch technique and scrub-the-hub.",
        "Summarize the SCOPE evidence on care bundles and state honestly what a quality collaborative can and cannot prove.",
        "Respond to an early infection signal by recording, escalating and protecting the specimen.",
    ],
    "big": """
<p>Infection is the leading cause of illness and technique failure in children on dialysis. A child on PD carries a tube from the skin into the abdomen; a child on hemodialysis often carries a tube into a large vein near the heart. Every connection is a door.</p>
<p>Your work in this module is to keep those doors closed: clean hands, protected key parts, scrubbed hubs, clean exit sites, and attention to the extra routes that come with being small.</p>
{{plain:Think of a catheter hub as the front door of a house in a dusty street. Wiping your feet once is not enough if you leave the door open while you talk. Protect the door, open it only as long as needed, and clean it every time.}}
<p>The picture has a limit. A house door keeps out what you can see. Bacteria that cause line infections are invisible and can live in a thin film inside the hub and on the catheter wall, where a quick wipe does not reach. That is why scrubbing time and friction matter, and why the catheter itself, not only the skin, is the target.</p>
{{cards:Key terms for this module|Key part::A part that must stay sterile, such as a hub, connector tip or needle.|Aseptic non-touch technique::Doing a procedure without touching key parts.|Biofilm::A protective layer bacteria form on catheter surfaces.|Care bundle::A small set of evidence-based steps done together, every time.|Catheter-associated bloodstream infection (CA-BSI)::Infection of the blood that starts from a catheter.}}
""",
    "case": {"title": "The diaper and the dressing", "html": """
<p><strong>Baby Elijah Gomez, 14 months</strong>, has a PD catheter and a gastrostomy tube. At a home visit, <strong>Nurse Carmela</strong> finds the exit-site dressing damp at the lower edge, where the diaper rubs. His grandmother says she changes the dressing &ldquo;when it looks dirty&rdquo;. In the same week, a 13-year-old on hemodialysis in the unit has a temperature of 38.4 &deg;C an hour into treatment.</p>
""", "questions": ["Which routes put Elijah at risk, and what can be changed?",
                  "What is the first response to the teenager&rsquo;s fever?",
                  "Which care-bundle steps would you audit in this unit?"]},
    "sections": [
        ("chain-of-transmission", "Transmission", "How organisms reach the child", """
<p>Most catheter infections start from the child&rsquo;s own skin or from hands that touch a key part. Organisms travel along the outside of the catheter from the exit site, or along the inside from a contaminated hub or connection.</p>
{{fig:pdn05_a}}
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>Why children are different</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Hands</td><td>Children touch lines; parents and siblings help</td><td>Hand hygiene for everyone near the line; teach the family the moments</td></tr>
<tr><td>Hubs and connections</td><td>Small lines, frequent access, play</td><td>Scrub the hub; keep caps on; never leave a line open</td></tr>
<tr><td>Exit site</td><td>Diapers, sweat, a busy child</td><td>Exit site away from the diaper; dressing for incontinent children</td></tr>
<tr><td>Gastrostomy and ostomies</td><td>Common in children on PD</td><td>Placed before or with the PD catheter when possible; extra care and prophylaxis decisions by the team</td></tr>
</tbody></table></div>
<p>The 2024 International Society for Peritoneal Dialysis (ISPD) pediatric guideline says a dressing is crucial for children with incontinence and that the exit site should avoid the diaper area in infants. It suggests placing a gastrostomy before or at the same time as the PD catheter (2D), and prophylactic antibiotic and antifungal cover when a gastrostomy is placed in a child already on PD (2D).[[pdn_warady2024]]</p>
{{key:In small children, diapers, gastrostomies and helping hands are infection routes. Plan for them; do not hope.}}
"""),
        ("key-parts-and-hubs", "Hubs", "Key parts and hubs", """
<p>Aseptic non-touch technique means you never touch a key part, even with gloves. Gloves protect you; technique protects the child.</p>
<p>For hemodialysis catheters, the Centers for Disease Control and Prevention (CDC) core interventions include hand hygiene, catheter care with an antiseptic, scrubbing the hub before each access, and staff competency and audit.[[cdc_core2013]] The scrub-the-hub protocol uses friction on the hub threads and end for the time stated by the antiseptic&rsquo;s instructions, then lets it dry before connection.[[cdc_scrubhub]]</p>
<h3>Antibiotic ointment at hemodialysis catheter exit sites</h3>
<p>Do not assume an ointment helps. In the Standardizing Care to Improve Outcomes in Pediatric End-Stage Kidney Disease (SCOPE) cohort of 1,277 children, mupirocin at the hemodialysis catheter exit site was associated with a higher rate of catheter-associated bloodstream infection (rate ratio 4.45).[[pdn_ruebner2022]] This is an observational association that may reflect which children received it. It is a reason to follow the unit&rsquo;s written protocol, not to improvise.</p>
{{key:Gloves protect you; technique protects the child. Scrub, wait, connect. Never touch a key part.}}
"""),
        ("bundles-that-work", "Bundles", "Bundles that lowered infection", """
<p>Most pediatric infection evidence comes from quality collaboratives rather than randomized trials, because children on dialysis are few. The SCOPE collaborative asked centers to adopt standardized care bundles and to audit them.</p>
{{fig:pdn05_b}}
<div class="table-wrap"><table>
<thead><tr><th>Bundle</th><th>Population</th><th>Before</th><th>After</th><th>Design</th></tr></thead>
<tbody>
<tr><td>Hemodialysis catheter care</td><td>325 children, 15 centers</td><td>3.3 CA-BSI per 100 patient-months</td><td>0.8 at 48 months</td><td>Pre&ndash;post, adjusted[[pdn_marsenic2020]]</td></tr>
<tr><td>PD follow-up care</td><td>644 children, 24 centers</td><td>0.63 peritonitis episodes per patient-year</td><td>0.42 at 36 months</td><td>Pre&ndash;post[[pdn_neu2016]]</td></tr>
</tbody></table></div>
<p>In the PD analysis, peritonitis rates fell further as compliance with follow-up care rose, reaching statistical significance at 80% compliance.[[pdn_neu2016]] Pre&ndash;post designs cannot exclude other changes that happened at the same time, so these results support bundles strongly but do not prove each step. What they show reliably is that consistent, audited practice is followed by fewer infections.</p>
{{scene:The 13-year-old with a fever|<p>Nurse Raffy sees 38.4 &deg;C an hour into treatment. He rechecks, looks at the exit site and the child, takes blood pressure and heart rate, and calls the nephrologist at once, per unit protocol. Blood cultures are drawn as ordered before any antibiotic. He records the time of each step and the hub care done at connection.</p><p class="tc-scene-take">A fever on a line is a bloodstream infection until the team says otherwise.</p>}}
{{key:Bundles work when everyone does every step, every time, and someone checks. Audit is part of the bundle.}}
"""),
    ],
    "debrief": ["""
<p><strong>Elijah&rsquo;s routes.</strong> The diaper wets the dressing, and the dressing is changed by appearance rather than on schedule. Carmela re-teaches dressing care and diaper positioning, checks the gastrostomy, records the exit-site appearance with a score, and asks the PD team about the dressing plan. Retraining follows the unit&rsquo;s protocol.</p>
<p><strong>The fever.</strong> Recheck, assess, call the nephrologist, obtain cultures as ordered before antibiotics, and record times.</p>
<p><strong>Audit.</strong> Hand hygiene, scrub-the-hub timing and drying, exit-site care, dressing integrity, and connection and disconnection technique, observed and recorded monthly.</p>
"""],
    "skills": {"title": "Asepsis and access protection", "intro": "Practice on models first.",
               "items": [("Performs hand hygiene at the right moments and teaches them to a caregiver", False),
                         ("Scrubs the hub with friction for the antiseptic&rsquo;s stated time and lets it dry", True),
                         ("Connects and disconnects without touching a key part", True),
                         ("Assesses and dresses an exit site in a child in diapers", False),
                         ("Responds to fever on a line by assessing, escalating and preserving cultures before antibiotics", True)]},
    "quiz": [
        ('Most catheter infections start from:',
         ['Air', 'The child&rsquo;s skin or hands touching a key part', 'Food', 'Dialysate only'], 1,
         'Outside along the catheter or inside from the hub.'),
        ('What does aseptic non-touch technique require?',
         ['Sterile gloves always', 'No hand hygiene', 'Never touching a key part', 'Touching only with the left hand'], 2,
         'Gloves protect you; technique protects the child.'),
        ('Why is drying time important in scrub-the-hub?',
         ['It looks neat', 'It is optional', 'To warm the hub', 'The antiseptic needs contact and drying time to work'], 3,
         'Follow the antiseptic&rsquo;s stated time.'),
        ('Which is a route more common in young children?',
         ['Diapers soiling the exit site', 'Shaving', 'Smoking', 'Contact lenses'], 0,
         'Exit sites should avoid the diaper area in infants.'),
        ('ISPD 2024 suggests a gastrostomy be placed:',
         ['Never', 'Before or at the same time as the PD catheter (2D)', 'Only after transplant', 'Only in adolescents'], 1,
         'Placement after PD starts carries more risk.'),
        ('After 48 months of SCOPE catheter bundles, CA-BSI fell from 3.3 to:',
         ['2.9', '0', '0.8 per 100 patient-months', '5.0'], 2,
         '325 children, 15 centers; pre&ndash;post.'),
        ('SCOPE PD follow-up bundles: peritonitis fell from 0.63 to:',
         ['0.1', '1.0', '0.6', '0.42 episodes per patient-year'], 3,
         '644 children, 24 centers, at 36 months.'),
        ('What can a pre&ndash;post collaborative not prove?',
         ['That each bundle step caused the fall', 'That infections fell', 'That centers took part', 'That rates were measured'], 0,
         'Other changes may have happened at the same time.'),
        ('In the SCOPE cohort, mupirocin at the HD catheter exit site was:',
         ['Associated with fewer infections', 'Associated with more CA-BSI (RR 4.45), observational', 'Proven harmful in a trial', 'Not studied'], 1,
         'An association; follow the written protocol.'),
        ('PD peritonitis rates fell significantly once bundle compliance reached about:',
         ['20%', '50%', '80%', '100%'], 2,
         'Consistency matters.'),
        ('A child on HD develops 38.4 &deg;C during treatment. First priority?',
         ['Give paracetamol and continue', 'End the shift', 'Change the dialyzer', 'Assess, call the nephrologist and obtain cultures as ordered before antibiotics'], 3,
         'Treat as a bloodstream infection until proven otherwise.'),
        ('Who should perform hand hygiene near a child&rsquo;s line?',
         ['Everyone who touches or helps, including family', 'Only the nurse', 'Only the doctor', 'No one at home'], 0,
         'Families and siblings help with care.'),
        ('A dressing on an incontinent child is described by ISPD 2024 as:',
         ['Unnecessary', 'Crucial', 'Harmful', 'Optional'], 1,
         'Rationale text, not a graded statement.'),
        ('What is biofilm?',
         ['A dressing type', 'A cleaning solution', 'A protective layer bacteria form on catheter surfaces', 'A diaper'], 2,
         'Biofilm explains why friction and time matter.'),
        ('Audit is:',
         ['Separate from the bundle', 'Only for managers', 'Optional', 'Part of the bundle'], 3,
         'Bundles work when someone checks.'),
    ],
    "terms": [("Key part", "A part that must stay sterile, such as a hub or connector tip."),
              ("Aseptic non-touch technique", "Performing a procedure without touching key parts."),
              ("Biofilm", "A protective layer that bacteria form on surfaces such as catheters."),
              ("Care bundle", "A small set of evidence-based steps done together every time."),
              ("CA-BSI", "Catheter-associated bloodstream infection."),
              ("Gastrostomy", "A feeding tube placed through the abdominal wall into the stomach.")],
    "readings": [("dialysis-access-infection.html", "Dialysis access infections: prevention and response."),
                 ("dialysis-access-care.html", "Caring for a dialysis access.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-access-infection-rate.html"],
}
