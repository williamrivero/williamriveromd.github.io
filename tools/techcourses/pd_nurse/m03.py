# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 03: The catheter, the tunnel and the exit site.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Describe the PD catheter&rsquo;s anatomy (intraperitoneal segment, deep cuff, tunnel, superficial cuff, exit site) and how each part protects or exposes the patient.",
        "Explain how bacteria travel from skin to peritoneum, and why the exit site and tunnel are the front line.",
        "Assess and document an exit site and tunnel using the 2023 International Society for Peritoneal Dialysis (ISPD) definitions of exit-site infection and tunnel infection.",
        "Distinguish a healing site, an equivocal site and an infected site, and escalate with the right urgency.",
        "Coordinate insertion-phase care, first use and long-term catheter protection with the access team.",
    ],
    "big": """
<p>A peritoneal dialysis (PD) catheter is a permanent hole through the body&rsquo;s main defense, the skin. Most days the body seals around it and nothing happens. When the seal fails, bacteria can travel along the outside of the catheter, down the tunnel, past the cuffs and into the peritoneum.</p>
<p>Catheter-related infections are an important risk factor for peritonitis and for losing the catheter, and with it, PD itself.[[pd_chow2023]] Most of them start small: a little crust, a little redness, a yellow stain on the gauze. Your work is to look at the exit site the same way every time, describe what you see in words the team can act on, and catch an infection while it is still at the skin.</p>
{{plain:Think of the catheter as a pipe passing through the wall of a house. The exit site is the outer seal. The tunnel is the passage through the wall. The cuffs are two layers of insulation that the tissue grows into, anchoring the pipe and blocking drafts.}}
<p>The picture has a limit. A wall does not heal or fight back. The tissue around a catheter forms a living tract lined by new skin that grows inward toward the superficial cuff over weeks. Pulling, moisture and bacteria all disrupt that lining. And unlike insulation, a cuff that becomes infected can harbor bacteria that antibiotics struggle to reach. That is why a deep infection so often ends with the catheter coming out.</p>
{{cards:Key terms for this module|Exit site::Where the catheter leaves the skin.|Tunnel::The catheter&rsquo;s path under the skin between the cuffs.|Cuff::A fabric ring that tissue grows into, anchoring the catheter.|Exit-site infection::Purulent discharge at the exit site, with or without redness.|Tunnel infection::Inflammation along the tunnel, with or without fluid around the catheter on ultrasound.|Immobilization::Securing the catheter so it cannot pull or twist at the exit site.}}
""",
    "case": {"title": "Saturday morning discharge", "html": """
<p><strong>Jun-Jun, 34</strong>, a call-center agent in Pasig on APD for 14 months, calls on a Saturday morning. Nurse <strong>Mae</strong> answers the PD line.</p>
<p><strong>Hour 0.</strong> He reports yellow discharge on his dressing for two days. His exit site &ldquo;is sore when the belt presses.&rdquo; He feels well and wants to know if he can wait until Monday. Effluent from the night cycler was clear. He has a team-building outing on Sunday.</p>
""", "questions": ["Does this meet the definition of exit-site infection? Of tunnel infection?",
                  "How urgent is this, even though he feels well?",
                  "What should happen before any antibiotic is given?"]},
    "sections": [
        ("the-physiology-and", "Anatomy and physiology", "The physiology and the anatomy", """
<h3>Catheter segments</h3>
<p>Follow the catheter from inside out. The intraperitoneal segment, coiled or straight, sits deep in the pelvis where drainage is best. The deep cuff anchors in the muscle of the abdominal wall. The subcutaneous tunnel runs to the superficial cuff, which sits about 2 to 4 cm inside the exit site. The exit site usually points downward or to the side, so fluid and debris drain away instead of pooling.[[pd_crabtree2019]]</p>
<p>Insertion technique, exit-site location and catheter design are decided by the access team, guided by the 2019 International Society for Peritoneal Dialysis (ISPD) guideline on creating and maintaining PD access.[[pd_crabtree2019]] Ideally the exit site is marked before insertion with the patient sitting and standing, away from the belt line and skin folds. That is a team decision, but you can help by asking the patient where their belt, waistband or work harness sits.</p>
{{fig:pd03_anatomy}}
<h3>How bacteria get in</h3>
<p>There are two routes to the peritoneum along a catheter.</p>
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>How</th><th>What protects against it</th></tr></thead>
<tbody>
<tr><td>Intraluminal</td><td>Through the inside of the catheter, from touch contamination during exchanges</td><td>Exchange technique and the contamination response (Module 4)</td></tr>
<tr><td>Periluminal</td><td>Along the outside of the catheter, from the exit site down the tunnel</td><td>Exit-site care, immobilization, early detection</td></tr>
</tbody></table></div>
<p><em>Staphylococcus aureus</em> and <em>Pseudomonas aeruginosa</em> are the classic periluminal organisms and the ones most likely to cause catheter loss. Carrying <em>S. aureus</em> in the nose raises the risk of exit-site infection. The 2023 ISPD recommendations address screening and treating carriers.[[pd_chow2023]] Whether a patient is screened or treated follows the prescriber and your unit&rsquo;s protocol.</p>
<h3>How the site heals</h3>
<p>After insertion, the tract lines itself with new skin over roughly six weeks. During that time the site is fragile. Pulling, twisting or catching the catheter on clothing tears the new lining and opens a path for bacteria.</p>
<p>Consider Mr. Dante, a construction foreman, three weeks after insertion. He tucks the catheter loosely into his waistband and climbs scaffolding all day. By Friday the site is red and weeping. Nothing about his technique at exchanges was wrong. The injury was mechanical, and it happened eight hours a day.</p>
{{key:Immobilization is a preventive intervention, not a comfort measure. Ask every patient where the catheter sits during work, sleep and travel.}}
"""),
        ("definitions-you-will", "Definitions", "Definitions you will use (ISPD 2023)", """
<p>The 2023 ISPD catheter-related infection recommendations revised and clarified these definitions.[[pd_chow2023]] Use the words exactly, because the team&rsquo;s decisions, and the program&rsquo;s infection rate, depend on everyone meaning the same thing.</p>
<ul>
<li><strong>Exit-site infection:</strong> purulent discharge, with or without redness of the skin where the catheter meets it.</li>
<li><strong>Tunnel infection:</strong> clinical inflammation (redness, swelling, hardness or tenderness) along the catheter tunnel, with or without fluid around the catheter on ultrasound.</li>
<li><strong>Catheter-related peritonitis:</strong> peritonitis together with, or within three months of, an exit-site or tunnel infection with the same organism, or with one site sterile after recent antibiotics. This term is defined in the 2022 peritonitis recommendations.</li>
</ul>
<h3>Redness alone is not the same as infection</h3>
<p>Redness around the catheter without pus can follow trauma, a new dressing product or early healing. It needs a careful look, a measurement and closer follow-up. It does not need automatic antibiotics. Pus is the key finding.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you see</th><th>Meets exit-site infection?</th><th>Why</th></tr></thead>
<tbody>
<tr><td>4 mm of pink skin, no drainage, two days after the patient caught the catheter on a drawer</td><td>No</td><td>Redness without pus, with a clear mechanical cause. Measure, review immobilization, recheck.</td></tr>
<tr><td>Thick yellow discharge on the gauze, no redness</td><td>Yes</td><td>Purulence alone meets the definition.</td></tr>
<tr><td>Clear, slightly blood-stained fluid in the first week after insertion</td><td>Not by itself</td><td>Early drainage is common while the tract heals. Report per protocol, especially if it increases.</td></tr>
<tr><td>Pus at the site, and the skin over the tunnel is red and tender</td><td>Yes, and possible tunnel infection</td><td>Inflammation along the tunnel raises the stakes. Same-day escalation.</td></tr>
</tbody></table></div>
{{key:Pus defines exit-site infection. Redness alone earns a measurement and a recheck, not an antibiotic.}}
"""),
        ("prevention-what-the", "Prevention", "Prevention: what the evidence supports", """
<p>Many exit-site rituals are passed down from unit to unit. Some rest on trials, some on observational data and some on common sense. Know which is which, so you can explain them honestly to patients.</p>
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>What the evidence shows</th><th>How to describe it</th></tr></thead>
<tbody>
<tr><td>Systemic antibiotic prophylaxis at catheter insertion</td><td>Reduces early peritonitis. It is the only 1A recommendation in the 2022 ISPD peritonitis guideline. In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS), facilities that used insertion antibiotics had lower peritonitis risk (rate ratio 0.83).</td><td>Strong evidence; prescriber decision</td></tr>
<tr><td>Regular topical antibiotic cream or ointment at the exit site</td><td>Downgraded in the 2023 update. In PDOPPS, facility use was associated with lower peritonitis risk that did not reach statistical significance (rate ratio 0.79, 95% confidence interval 0.62 to 1.01).</td><td>Mixed; follow unit protocol</td></tr>
<tr><td>Exit-site dressing cover</td><td>A clarified suggestion in 2023, especially during the healing phase</td><td>Follow unit protocol</td></tr>
<tr><td>Catheter immobilization</td><td>Mechanistically sound; reduces traction injury</td><td>Practice standard</td></tr>
<tr><td>Treating nasal <em>S. aureus</em> carriage</td><td>Addressed in the 2023 recommendations</td><td>Prescriber decision per protocol</td></tr>
<tr><td>Hand hygiene before every site care</td><td>Foundational infection prevention</td><td>Practice standard</td></tr>
</tbody></table></div>
<p>PDOPPS is an observational cohort of 7,051 adults in 209 facilities across seven countries.[[pd_perl2020]] Its associations do not prove that any single practice caused the lower rates. Facilities that use one good practice tend to use many.</p>
<h3>Program targets</h3>
<p>The 2023 recommendations set a target: the overall exit-site infection rate should be no more than 0.40 episodes per year at risk.[[pd_chow2023]] Your unit&rsquo;s rate measures the program, not individual patients. Module 12 covers how to count it.</p>
<h3>Example: working out your unit&rsquo;s rate</h3>
<p>A provincial PD program follows 40 patients. Over the past year, because some patients started or stopped during the year, the total time at risk adds up to 34.5 patient-years. The team recorded 11 exit-site infections.</p>
<p>Rate = 11 episodes &divide; 34.5 years at risk = about 0.32 episodes per year at risk. That is within the 2023 target. The head nurse then looks at the 11 episodes one by one. Six followed catheter trauma, four of them in patients who do manual labor. The next improvement project writes itself: immobilization teaching for working patients.</p>
{{key:A rate tells you whether the program is on track. The episodes behind the rate tell you what to fix.}}
{{fig:pd03_fig_03_exit_site_prevention_evidence}}
"""),
        ("assessment-at-every", "Assessment and triage", "Assessment at every indicated visit", """
<p>Ask first, then look and feel, in the same order every time. Ask about pain, recent pulling or trauma, a wet or soiled dressing, fever, a change in drainage, cloudy effluent and abdominal pain.</p>
{{fig:pd03_grading}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>What to record</th></tr></thead>
<tbody>
<tr><td>Drainage</td><td>None, serous, bloody or purulent; amount; whether it expresses on gentle pressure, per unit technique</td></tr>
<tr><td>Skin</td><td>Redness with its diameter in millimeters, swelling, crust, granulation tissue (&ldquo;proud flesh&rdquo;)</td></tr>
<tr><td>Tunnel</td><td>Tenderness, swelling or hardness along the course under the skin to the superficial cuff</td></tr>
<tr><td>Catheter</td><td>Cuff visible at the exit, cracks, security of immobilization</td></tr>
<tr><td>Systemic</td><td>Temperature, effluent clarity, abdominal pain</td></tr>
</tbody></table></div>
<p>Photograph only with the facility&rsquo;s approved image system and the patient&rsquo;s consent. A dated photo series is often the clearest way to show change over time. A photo on your personal phone is not part of the record and is a privacy risk.</p>
<h3>Write what you saw, not what you concluded</h3>
<div class="table-wrap"><table>
<thead><tr><th>Weak note</th><th>Useful note</th></tr></thead>
<tbody>
<tr><td>&ldquo;Exit site slightly infected.&rdquo;</td><td>&ldquo;Exit site: 6 mm redness, small amount of thick yellow drainage on gauze, expresses on gentle pressure. Tender over the tunnel about 2 cm from the exit. No cuff visible. Temperature 37.1 &deg;C. Effluent clear. No abdominal pain. Caught catheter on seatbelt six days ago.&rdquo;</td></tr>
</tbody></table></div>
<h3>Triage</h3>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Urgency</th><th>Your action</th></tr></thead>
<tbody>
<tr><td>Healing site, no drainage, minimal redness</td><td>Routine</td><td>Reinforce care, document</td></tr>
<tr><td>Redness without pus, no tunnel signs</td><td>Same-week review</td><td>Document size, recheck within the unit&rsquo;s timeframe, review technique and trauma</td></tr>
<tr><td>Purulent discharge</td><td>Same-day PD team contact</td><td>Culture per protocol before any ordered treatment; document; teach</td></tr>
<tr><td>Tunnel tenderness or swelling</td><td>Same day, prompt</td><td>Escalate for possible tunnel infection; screen for peritoneal symptoms</td></tr>
<tr><td>Any of the above plus cloudy effluent or abdominal pain</td><td>Urgent</td><td>Activate the peritonitis pathway (Module 7) as well</td></tr>
<tr><td>Cuff visible through the exit site</td><td>Same day</td><td>Escalate; often a sign of chronic infection</td></tr>
</tbody></table></div>
<h3>Example: two sites on the same morning</h3>
<p>Nurse Mae sees two patients before ten. <strong>Ms. Cora</strong> has 5 mm of redness and no drainage. She moved house last weekend and carried boxes against her abdomen. Mae measures the redness, reviews how she secures the catheter, and books a recheck within the unit&rsquo;s timeframe. <strong>Mr. Bert</strong> has a dry crust that, when gently lifted per unit technique, shows a bead of pus. He feels fine. Mae swabs per protocol before any ordered antibiotic and calls the nephrologist the same morning. Same-looking sites, different findings, different urgency.</p>
{{call:Call the PD team the same day for any purulent exit site or tunnel tenderness. Activate the peritonitis pathway if the effluent is cloudy or there is abdominal pain.}}
<p><strong>Treatment is a prescriber decision.</strong> The 2023 update emphasized close clinical monitoring to decide how long to treat. It also described options short of replacing the catheter, including shaving or removing the outer cuff and relocating the exit site.[[pd_chow2023]] Your observations at follow-up visits are what make that monitoring possible.</p>
"""),
        ("insertion-and-first", "Insertion and first use", "Insertion and first use", """
<p><strong>Before insertion.</strong> Explain the procedure, where the exit site will be, how long healing takes and what to report. Confirm the patient knows the dressing is not changed at home during the early period unless the team says so. Ask about work, bathing, sports and travel, because each affects the plan.</p>
<p><strong>After insertion.</strong> Coordinate with the access team on the first dressing change, when flushing happens and when PD can begin. When time allows, many programs wait about two weeks before full PD to let the tunnel heal. Urgent-start PD uses small volumes with the patient lying down, under a specific protocol, to limit leaks. Follow your unit&rsquo;s protocol exactly.</p>
<h3>Example: questions that prevent trouble</h3>
<div class="table-wrap"><table>
<thead><tr><th>Patient says</th><th>What you teach</th></tr></thead>
<tbody>
<tr><td>&ldquo;I bathe in the river behind our house.&rdquo;</td><td>River and pool water can carry organisms such as <em>Pseudomonas</em>. Ask the team about bathing rules; protect the site per protocol.</td></tr>
<tr><td>&ldquo;My work uniform has a tight belt.&rdquo;</td><td>Plan where the catheter will sit and how it is secured; consider a different belt position.</td></tr>
<tr><td>&ldquo;I want to go home to the province for a fiesta next week.&rdquo;</td><td>The site is still healing. Discuss timing and what to bring with the team.</td></tr>
<tr><td>&ldquo;The gauze looks wet with clear fluid.&rdquo;</td><td>Report it. Early leak and drainage need the team to look, especially after an urgent start.</td></tr>
</tbody></table></div>
{{key:Most early exit-site problems are mechanical. Ask about the patient&rsquo;s day before you blame their technique.}}
{{fig:pd03_fig_03_catheter_break_in_first_weeks}}
"""),
    ],
    "debrief": ["""
<p><strong>Mae&rsquo;s questions.</strong> Any pain along the line toward the belly? &ldquo;Yes, a little, about two finger-widths in.&rdquo; Fever? No. Abdominal pain? No. Any pulling? He caught the catheter on his seatbelt last week.</p>
<p><strong>Does it meet the definitions?</strong> Purulent discharge meets the definition of exit-site infection. Tenderness along the tunnel raises concern for tunnel infection. Clear effluent and no abdominal pain argue against peritonitis now, but the risk is real, because the infection is moving toward the cuff.</p>
<p><strong>How urgent?</strong> Same day. Feeling well does not change the anatomy. Waiting until Monday gives a tunnel infection two more days to reach the cuff, where antibiotics work poorly and catheters are lost.</p>
<p><strong>Before any antibiotic.</strong> Mae contacts the on-call PD nurse and nephrologist the same morning. She arranges an exit-site swab before any ordered antibiotic and asks Jun-Jun to come in for a tunnel assessment. She tells him to call at once if the effluent turns cloudy or abdominal pain starts, and to discuss the Sunday outing with the team. She documents the trauma history and his belt position. At follow-up she reviews immobilization and clothing.</p>
<p><strong>Take-home.</strong> Purulence plus tunnel tenderness is a same-day problem, even in a patient who feels well.</p>
"""],
    "skills": {"title": "Exit site and low drain (OSCE station 4)",
               "intro": "Using faculty-provided photographs, classify a healing site, isolated redness, a purulent exit-site infection and a site with tunnel swelling. Document findings and disposition without assigning treatment.",
               "items": [("Obtains symptoms and effluent data.", False),
                         ("Assesses exit-site and tunnel findings using the ISPD 2023 definitions.", False),
                         ("Avoids forceful or unapproved manipulation of the catheter.", True),
                         ("Triages severe symptoms and closes the loop.", True),
                         ("Records action and response.", False)]},
    "quiz": [
        ("Which finding defines exit-site infection in the 2023 ISPD recommendations?",
         ["Purulent discharge, with or without redness", "Redness alone", "Crust at the site", "Any discomfort"], 0,
         "Pus is the defining feature. Redness alone may be mechanical or part of healing. Crust and discomfort are nonspecific."),
        ("What defines tunnel infection?",
         ["Any exit-site redness", "Cloudy effluent", "Clinical inflammation along the tunnel, with or without fluid around the catheter on ultrasound", "Fever alone"], 2,
         "Tunnel infection is inflammation along the course under the skin. Cloudy effluent points to peritonitis; fever alone is nonspecific."),
        ("Mr. Dante, three weeks after insertion, climbs scaffolding with his catheter tucked loosely in his waistband. Why does this matter?",
         ["It improves drainage", "It increases glucose absorption", "It causes constipation", "Traction tears the healing tract and opens a path for bacteria"], 3,
         "The new lining of the tract is fragile for weeks. Repeated pulling injures it and invites infection."),
        ("Which organism is classically linked to periluminal infection and catheter loss?",
         ["<em>Escherichia coli</em>", "<em>Staphylococcus aureus</em>", "<em>Candida albicans</em> only", "Coagulase-negative staphylococci only"], 1,
         "<em>S. aureus</em>, together with <em>P. aeruginosa</em>, are the classic periluminal organisms."),
        ("What is the 2023 ISPD target for the overall exit-site infection rate?",
         ["No more than 0.10 episodes per year at risk", "No more than 0.40 episodes per year at risk", "No more than 1.0 episode per year at risk", "No target was set"], 1,
         "The 2023 update set a target of no more than 0.40 episodes per year at risk."),
        ("Which prevention measure carries the only 1A recommendation in the 2022 peritonitis guideline?",
         ["Daily mupirocin at the exit site", "Weekly exit-site photography", "Daily chlorhexidine bathing", "Systemic antibiotic prophylaxis at catheter insertion"], 3,
         "Insertion prophylaxis is the 1A recommendation. Routine topical antibiotics were downgraded in 2023."),
        ("How should the PDOPPS association between topical exit-site antibiotics and peritonitis be described?",
         ["A lower risk that did not reach statistical significance in observational data", "Proven to halve peritonitis", "Harmful", "Unstudied"], 0,
         "The rate ratio was 0.79 with a confidence interval that crossed 1, in an observational design. That is a hint, not proof."),
        ("Ms. Cora has 5 mm of redness, no drainage and no tunnel signs. She carried heavy boxes last weekend. Best action?",
         ["Start antibiotics", "Ignore it", "Document the size, review trauma and immobilization, and recheck within the unit&rsquo;s timeframe", "Activate the peritonitis pathway"], 2,
         "Redness alone after trauma needs measurement and follow-up, not automatic treatment."),
        ("Purulent exit-site discharge plus new cloudy effluent should prompt:",
         ["Exit-site care only", "A routine appointment next week", "Peritonitis pathway activation as well as exit-site evaluation", "A dressing change only"], 2,
         "Cloudy effluent means possible peritonitis, which may be catheter-related. Both problems need attention today."),
        ("When should an exit-site swab be taken relative to ordered antibiotics?",
         ["Before the first dose when feasible, per protocol", "After several days of antibiotics", "Never", "Only if fever is present"], 0,
         "Cultures taken before antibiotics are more likely to identify the organism, which guides the prescriber&rsquo;s choice."),
        ("A program had 11 exit-site infections over 34.5 patient-years at risk. What is the rate?",
         ["About 0.32 episodes per year at risk", "About 3.1 episodes per year at risk", "About 0.11 episodes per year at risk", "It cannot be calculated"], 0,
         "11 divided by 34.5 is about 0.32, within the 2023 target of no more than 0.40."),
        ("A cuff visible at the exit site suggests:",
         ["A normal finding", "A good seal", "A need for more fluid", "Cuff extrusion, often linked to chronic infection; escalate"], 3,
         "An extruding cuff is a same-day escalation."),
        ("Which catheter interventions short of full replacement did the 2023 update describe for persistent infection?",
         ["Cutting the catheter shorter at home", "Taping the catheter tighter", "Switching solution brand", "Shaving or removing the outer cuff and relocating the exit site"], 3,
         "These are procedures done by the access team."),
        ("Why should exit-site findings be documented the same way at every visit?",
         ["To satisfy auditors only", "To detect change over time and support decisions on treatment duration", "Because it is faster", "It is not necessary"], 1,
         "Consistent descriptions, with measurements, show whether the site is improving or worsening."),
        ("Which route of infection is mainly addressed by exchange technique rather than exit-site care?",
         ["Periluminal", "Hematogenous", "Intraluminal (touch contamination)", "Transmural from the bowel only"], 2,
         "Technique protects the inside of the system. Exit-site care protects the outside."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Tunnel", "The path of the catheter under the skin between the cuffs."),
              ("Cuff", "A fabric ring on the catheter that tissue grows into, anchoring it."),
              ("Exit-site infection", "Purulent discharge at the exit site, with or without redness (ISPD 2023)."),
              ("Tunnel infection", "Inflammation along the catheter tunnel, with or without a fluid collection on ultrasound."),
              ("Immobilization", "Securing the catheter so it cannot pull or twist at the exit site."),
              ("Granulation tissue", "Moist, red new tissue at a wound; at the exit site sometimes called proud flesh."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell.")],
    "readings": [("dialysis-access-infection.html", "Access infection prevention across dialysis modalities.")],
    "calcs": [],
}
