# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 12: Pediatric hemodialysis, prescription logic and vascular access. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain why and when children receive hemodialysis, and how the prescription scales blood flow and dose to body size.",
        "Describe the pediatric vascular access options and the principle of venous preservation.",
        "Apply the tunneled catheter care bundle and relate it to the SCOPE results.",
        "Summarize what the HDF, Heart and Height study shows, and what it cannot.",
    ],
    "big": """
<p>Hemodialysis in children uses the same machine principles as in adults, but every setting is scaled to a smaller body and a longer future. A child&rsquo;s blood flow, dialyzer and lines are sized to their body; their vascular access must last, or be replaceable, for decades.</p>
<p>Your work in this module is to understand the logic of the prescription well enough to verify it, and to protect the child&rsquo;s veins and catheter as a lifetime asset.</p>
{{plain:Think of a child&rsquo;s veins as a savings account that must last a lifetime. Every line placed, every blood draw from a protected vein, is a withdrawal. Some withdrawals are necessary; none should be careless.}}
<p>The picture has a limit. Money can be earned back. A damaged central vein usually cannot. Narrowing from repeated catheters can close off the veins a child would need for a fistula or even a transplant later. That is why the account must be protected even when today&rsquo;s need is urgent.</p>
{{cards:Key terms for this module|Central venous line (CVL)::A tunneled catheter in a large central vein used for hemodialysis.|Arteriovenous fistula (AVF)::A surgical connection of an artery to a vein in the arm.|Blood flow rate (QB)::How fast the pump moves blood through the circuit, in mL/min.|Venous preservation::Protecting veins from needles and lines that are not needed.|Hemodiafiltration (HDF)::Hemodialysis with added convection using large replacement-fluid volumes.}}
""",
    "case": {"title": "The phlebotomist and the left arm", "html": """
<p><strong>Carlo Mendoza, 13</strong>, 38 kilograms, has a tunneled central line for hemodialysis and is scheduled for an arm vein assessment for a future fistula. In the ward, a phlebotomist prepares to draw blood from his left forearm, the arm the vascular surgeon has marked for the fistula. His mother says, &ldquo;They always use that arm, his veins are good there.&rdquo; <strong>Nurse Jessa</strong> walks in.</p>
""", "questions": ["Why does the choice of arm matter?",
                  "What should Jessa do right now?",
                  "What would make a fistula a better or worse plan for Carlo?"]},
    "sections": [
        ("why-hd-in-children", "Prescription", "Why hemodialysis, and how the prescription scales", """
<p>Hemodialysis is often preferred for children over about five years of age when PD is not suitable or not chosen; PD is more often used in younger children and those under about 10 kilograms.[[pdn_fischbach2005]] Hemodialysis in children should be delivered in a pediatric unit with a multidisciplinary team, because nutrition, growth and schooling are part of the treatment.</p>
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>Pediatric practice described by the ESPN guidelines (2005)</th><th>Your check</th></tr></thead>
<tbody>
<tr><td>Blood flow</td><td>150&ndash;200 mL/min/m&sup2;, or 5&ndash;7 mL/min/kg, often sufficient; in small children (weight + 10) &times; 2.5 mL/min as a rule of thumb</td><td>Ordered QB in mL/min/kg and mL/min/m&sup2;</td></tr>
<tr><td>Sessions</td><td>Usually three per week, 3 to 4 hours; more often for infants or some adolescents</td><td>Session time matches the order</td></tr>
<tr><td>Dose</td><td>A minimum Kt/V of 1.2 to 1.4, with recognition that urea is only one measure</td><td>Monthly adequacy results in the record</td></tr>
<tr><td>Dialyzer and lines</td><td>Sized to the child, with blood volume in mind (Module 13)</td><td>Correct sizes per the order</td></tr>
</tbody></table></div>
<p>These figures come from practical guidelines written in 2005 and are expert guidance, not trial evidence.[[pdn_fischbach2005]] Your unit&rsquo;s pediatric protocol and the written order decide. Kt/V is a surrogate measure of small-solute removal; it is not growth, well-being or survival.</p>
<p><strong>Worked check.</strong> A 20-kilogram child with BSA 0.8 m&sup2; and an ordered QB of 120 mL/min: 120 &divide; 20 = 6 mL/min/kg; 120 &divide; 0.8 = 150 mL/min/m&sup2;. Both sit in the described ranges. A QB of 250 mL/min would be 12.5 mL/min/kg, a reason to confirm the order.</p>
{{key:Convert the ordered blood flow to mL/min/kg and mL/min/m&sup2;. A value far outside the range is a question, not a setting.}}
"""),
        ("access-for-a-lifetime", "Access", "Access for a lifetime", """
<p>The European Society for Paediatric Nephrology (ESPN) Dialysis Working Group consensus, graded with the GRADE system, reviewed three access types: tunneled central lines, AVFs and arteriovenous grafts. Observational studies and the International Paediatric Haemodialysis Network registry associate central lines with significantly more infection, dysfunction and need for replacement. Despite this, AVFs are used in only about 25% of children on hemodialysis. The consensus emphasizes the right access for the right child at the right time, with venous preservation at all times; fistulas may not suit very young children or those expecting a short dialysis course before transplant.[[pdn_shroff2019]]</p>
{{fig:pdn12_a}}
<ul>
<li>Protect the arm planned for a fistula: no needles, no cuffs, no intravenous cannulas. Mark it and tell everyone.</li>
<li>Draw blood from the dialysis access at the session when ordered, rather than from protected veins.</li>
<li>Report any arm or facial swelling in a child with a central line; it may signal central vein narrowing.</li>
</ul>
{{key:Every vein is a future access. Protect the fistula arm as if it were already a fistula.}}
"""),
        ("catheter-care", "Catheter care", "Catheter care and the bundle", """
<p>A tunneled central line is a direct path to the bloodstream. The SCOPE collaborative&rsquo;s catheter care bundle (hand hygiene, mask, scrub-the-hub, exit-site care, dressing, and aseptic connection and disconnection) was followed by a fall in catheter-associated bloodstream infection from 3.3 to 0.8 per 100 patient-months over 48 months in 325 children.[[pdn_marsenic2020]] The design was pre&ndash;post, so it supports the bundle without proving each step.</p>
{{fig:pdn12_b}}
<p>Lock solutions, dressing types and exit-site agents follow the unit protocol. The SCOPE cohort&rsquo;s observational association between mupirocin at the hemodialysis catheter exit and more infection is a reason not to improvise.[[pdn_ruebner2022]]</p>
<h3>Hemodiafiltration in children</h3>
<p>The HDF, Heart and Height study compared conventional hemodialysis with online postdilution HDF in 190 children from 28 centers; 78 and 55 completed one year. HDF was associated with no progression in carotid intima-media thickness, a gain in height standard deviation score, lower beta-2-microglobulin, and fewer headaches, dizziness and cramps.[[pdn_shroff2019hdf]] The study was nonrandomized, and its main outcomes are surrogates; the authors call for randomized confirmation.</p>
{{key:The catheter bundle works when every step is done every time. HDF looks promising in children, but the evidence is observational.}}
"""),
    ],
    "debrief": ["""
<p><strong>Why the arm matters.</strong> The left forearm is planned for a fistula. Repeated needling can damage those veins and reduce the chance of a working fistula, which the ESPN consensus associates with fewer infections than central lines.</p>
<p><strong>Right now.</strong> Jessa politely stops the draw, explains the plan to the phlebotomist and the mother, and arranges for blood to be drawn from the dialysis line at the next session or from another site as the team directs. She marks the arm and adds an alert to the chart.</p>
<p><strong>Fistula fit.</strong> Carlo is 13, 38 kilograms, with suitable veins and an uncertain wait for transplant, all favoring a fistula. A living donor ready within months might change the plan; the team decides.</p>
"""],
    "skills": {"title": "Prescription check and access protection", "intro": "Use fictional orders and access models.",
               "items": [("Converts ordered blood flow to mL/min/kg and mL/min/m&sup2; and compares with the described ranges", True),
                         ("Marks and protects a planned fistula arm and communicates it to the team", True),
                         ("Performs tunneled catheter care using every bundle element", True),
                         ("Recognizes and reports arm or facial swelling in a child with a central line", False),
                         ("Explains in plain words why veins are protected", False)]},
    "quiz": [
        ('Hemodialysis is often preferred for children over about:',
         ['5 years', '1 year', '15 years', 'Never'], 0,
         'PD is more common in younger and smaller children.'),
        ('A described blood flow for children is:',
         ['50 mL/min/m&sup2;', '150&ndash;200 mL/min/m&sup2; or 5&ndash;7 mL/min/kg', '500 mL/min always', 'Same as adults'], 1,
         'ESPN practical guidelines, 2005.'),
        ('Ordered QB 120 mL/min in a 20-kg child equals:',
         ['2 mL/min/kg', '12 mL/min/kg', '6 mL/min/kg', '60 mL/min/kg'], 2,
         '120 &divide; 20.'),
        ('Ordered QB 250 mL/min in a 20-kg child equals 12.5 mL/min/kg. You:',
         ['Run it', 'Halve it yourself', 'Ignore it', 'Confirm the order with the prescriber'], 3,
         'Far above the described range.'),
        ('Kt/V is:',
         ['A surrogate for small-solute removal', 'A patient-felt outcome', 'A growth measure', 'A blood pressure'], 0,
         'Urea is only one measure.'),
        ('The ESPN access consensus found central lines associated with:',
         ['Fewer infections', 'More infection, dysfunction and replacement', 'No difference', 'Better growth'], 1,
         'Observational and registry data.'),
        ('About what share of children on hemodialysis use an AVF?',
         ['5%', '75%', '25%', '100%'], 2,
         'Despite their advantages.'),
        ('Venous preservation means:',
         ['Using any vein', 'Avoiding all blood tests', 'Using only central lines', 'Protecting veins from unneeded needles and lines'], 3,
         'Today&rsquo;s vein is tomorrow&rsquo;s access.'),
        ('A phlebotomist prepares to use the marked fistula arm. You:',
         ['Stop it and arrange another site', 'Allow it', 'Leave', 'Ask the child to decide'], 0,
         'Protect the fistula arm.'),
        ('Arm or facial swelling in a child with a central line may signal:',
         ['Normal growth', 'Central vein narrowing or thrombosis', 'Allergy only', 'Dehydration'], 1,
         'Report it.'),
        ('SCOPE catheter bundles: CA-BSI fell to:',
         ['2.0', '3.3', '0.8 per 100 patient-months', '0'], 2,
         'From 3.3 over 48 months; pre&ndash;post.'),
        ('Which is a catheter bundle element?',
         ['Skipping masks', 'Leaving caps off', 'Weekly hand hygiene', 'Scrub-the-hub'], 3,
         'Every step, every time.'),
        ('The HDF, Heart and Height study was:',
         ['Nonrandomized and observational', 'A large randomized trial', 'A survey', 'Adult only'], 0,
         'Randomized confirmation is needed.'),
        ('In that study, HDF was associated with:',
         ['Faster cIMT progression', 'Height gain and no cIMT progression', 'More cramps', 'Higher beta-2-microglobulin'], 1,
         'Surrogate outcomes; association only.'),
        ('Where should hemodialysis for children ideally be delivered?',
         ['Any adult unit', 'At home without training', 'A pediatric unit with a multidisciplinary team', 'In school'], 2,
         'Growth and schooling are part of care.'),
    ],
    "terms": [("Central venous line", "A tunneled catheter in a large central vein for hemodialysis."),
              ("Arteriovenous fistula", "A surgical artery-to-vein connection for hemodialysis needles."),
              ("Arteriovenous graft", "A tube connecting an artery and a vein, used when a fistula is not possible."),
              ("Venous preservation", "Protecting veins from unneeded needles and lines."),
              ("Kt/V", "A urea-based measure of hemodialysis dose; a surrogate."),
              ("Hemodiafiltration", "Hemodialysis with added convection using replacement fluid.")],
    "readings": [("hemodialysis-access-lifeline.html", "Making hemodialysis access last."),
                 ("dialysis-access-care.html", "Caring for a dialysis access."),
                 ("dialysis-prescription.html", "How a hemodialysis prescription is built.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-bsa.html"],
}
