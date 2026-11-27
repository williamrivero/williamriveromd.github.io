# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 24: Vascular access in children.
Written November 27, 2026 for the Renal Care Academy in the voice of the Physician on Duty modules, to the medical teaching
standard. Grades checked against the ESPN Dialysis Working Group 2019 consensus (GRADE, 1A to 2D, or ungraded) and the IDSA 2009
catheter-infection guideline (IDSA strength A to C, quality I to III). Registry and cohort figures from the PubMed abstracts
(IPHN 2019, SCOPE 2020 and 2022). No doses. Every case is fictional."""

MODULE = {
    "image_alt": "A pediatric nephrologist and a dialysis nurse examine the dressing over a tunneled catheter on the chest of a twelve-year-old boy sitting in a dialysis chair, his mother beside him.",
    "objectives": [
        "Choose between a tunneled central venous catheter and an arteriovenous fistula for a child, using size, the expected time to transplant and a lifelong vein plan.",
        "Troubleshoot catheter dysfunction and lead the response to suspected catheter-related bloodstream infection, including when the catheter must come out.",
        "Write an access plan that protects veins from birth and that an adult hemodialysis unit can follow without you in the room.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the access plan for a whole childhood</span>A child who starts hemodialysis (HD) at 8 may need kidney replacement therapy for sixty years. The attending pediatric nephrologist owns the vascular access plan: which veins are protected, which access is placed and when, who is called when it fails, and how the plan follows the child to an adult HD unit 60 kilometers away. The surgeon creates the access, the interventionist rescues it, and the nurse uses it three times a week. You decide what the next access will be before the present one fails.</div>
{{plain:Think of a child&rsquo;s veins as the few roads into a small town. Every needle, every intravenous line and every catheter is roadwork. Most roadwork is repaired. Some leaves a road closed for good, and the town cannot build new ones.}}
<p>The picture has a limit. A closed road is visible; a closed vein often is not. A peripherally inserted central catheter (PICC) or a temporary jugular line can narrow a central vein without any sign for years, until a fistula in that arm swells, or a new catheter will not pass. Veins also grow with the child, so a vein too small for a fistula at 15 kilograms may be ideal at 35. The plan has to look forward in time, not only at today&rsquo;s anatomy.</p>
{{cards:Key numbers|Arteriovenous fistula (AVF) use in children on HD::About 25% (ESPN 2019, citing the IPHN registry)|Catheter infection, IPHN registry::1.3 per 1,000 catheter-days; none reported with fistulas|Access dysfunction, IPHN registry::2.5 per 1,000 catheter-days vs 1.2 per 1,000 fistula-days|Bloodstream infection after a care bundle, SCOPE::3.3 to 0.8 per 100 patient-months over 48 months|Time to transplant, IPHN registry::Median 14 months with catheters vs 20 months with fistulas}}
<p>Most children on HD start with a tunneled central venous catheter (CVC), because they are small, because they started urgently, or because a transplant is expected soon. A few will dialyze long enough, and grow enough, that a fistula would serve them better. Your work is to protect every vein that a future fistula or catheter will need, to keep the catheter working and uninfected while it is the lifeline, and to recognize the night when a fever on dialysis is sepsis from the line.</p>
""",
    "case": {"title": "Rigors at minute twenty",
             "html": """
<p>Carlo Dizon is 12 and weighs 34 kilograms. Reflux nephropathy brought him to kidney failure seven months ago, and he dialyzes on Monday, Wednesday and Friday through a right internal jugular tunneled catheter at an adult freestanding unit in San Fernando, Pampanga. Your pediatric center is in Quezon City, about 60 kilometers away. His mother, Aling Marites, is being evaluated as his kidney donor; her work-up has stalled on cost.</p>
<p>It is 7:20 a.m. on a Wednesday. Twenty minutes after the lines were connected, Carlo began to shake. His temperature is 39.2 &deg;C, heart rate 138 per minute, blood pressure 92/54 mm Hg; before the session it was 118/72. The exit site looks clean. His left arm carries the scar of a PICC placed during a pneumonia admission last year. The physician on duty (POD), an internist, calls you: &ldquo;I gave paracetamol. Can we finish the session and get cultures on Friday? The unit has no pediatric culture bottles.&rdquo; Aling Marites, beside the chair, asks the nurse to pull the catheter out now.</p>
""",
             "questions": ["What should happen at the chair in the next 30 minutes?",
                           "Does the catheter have to come out, and who decides?",
                           "What would have made this less likely, and what is Carlo&rsquo;s access plan from today?"]},
    "sections": [
        ("physiology", "Veins as a resource", "Why a child&rsquo;s veins are the scarce resource", """
<p>An HD access must deliver blood to the circuit fast enough for the dialyzer to work, then take it back. Flow through a tube rises steeply with its radius: in laminar flow, halving the radius cuts flow to about a sixteenth at the same pressure. That physics is the whole problem of pediatric access. A small child&rsquo;s veins and arteries are narrow, so the catheter that fits is narrow, and the fistula that is made may never carry enough flow to mature.</p>
<p>A catheter does damage while it works. Its tip and body rub the vein wall with every heartbeat and breath, and the endothelium responds with inflammation, smooth-muscle growth and a fibrin sheath. Over months this narrows the central vein (central venous stenosis), silently, until a fistula in that arm swells or a future catheter will not pass.</p>
<p>A fistula works differently. Joining an artery to a vein exposes the vein to arterial flow and pressure. Over weeks the vein dilates and its wall thickens, a process called maturation. It needs a vein of adequate diameter, an artery that can deliver flow, and an undamaged path back to the heart. Every venipuncture in the forearm and every PICC in the arm can remove one of those conditions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Access</th><th>What it needs from the child</th><th>How it usually fails</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Tunneled CVC</td><td>A patent central vein, usually the right internal jugular, and a tip position that allows free flow</td><td>Thrombus, fibrin sheath, kinking or tip migration; infection of the lumen or tunnel; central stenosis over time</td><td>Arterial or venous pressure alarms, flow that improves when the child turns the head, fever or rigors soon after connection</td></tr>
<tr><td>AVF</td><td>A vein and artery of adequate size, a clear central path, time to mature, and a team that can cannulate a small arm</td><td>Failure to mature, stenosis, thrombosis, infiltration during cannulation</td><td>Weak or absent thrill, pulsatile hard segment, prolonged bleeding after needles, swelling of the arm</td></tr>
<tr><td>Arteriovenous graft (AVG)</td><td>A synthetic or biological conduit between artery and vein</td><td>Stenosis at the venous anastomosis, thrombosis, infection</td><td>Rising venous pressures, loss of thrill</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">On the ward, the PICC request &middot; fictional</span><p>A pediatric resident messages you at 9 p.m. Elijah, 5, has chronic kidney disease (CKD) stage 4 from renal dysplasia and needs two weeks of intravenous antibiotics for osteomyelitis. The resident has booked a PICC in the left arm for the morning.</p><p>You ask for a small-bore tunneled central line in the internal jugular vein instead, placed by the team that would one day place his dialysis catheter, and you write &ldquo;No PICC, no blood draws above the wrist in either arm: future fistula&rdquo; on the order sheet and the front of the chart.</p><p class="tc-scene-take"><b>What this shows.</b> Vein preservation is decided by whoever writes the next order. Put the rule where that person will read it.</p></div>
{{key:Every vein in a child with CKD belongs to the future fistula or the future catheter. Spend it only when nothing else will do.}}
{{fig:apn24_a}}
"""),
        ("evidence", "Choosing the access", "What the evidence shows about choosing an access", """
<p><strong>What adults taught us, and where it stops.</strong> For adults, &ldquo;fistula first&rdquo; changed practice. The Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 update moved the frame to an end-stage kidney disease &ldquo;Life-Plan&rdquo;: the right access for the patient, chosen with a view of every access that patient will need.[[apn24_6]] Children fit that frame better than adults do, because their life-plan is longer and more often ends in a transplant.</p>
<p><strong>The pediatric consensus.</strong> The European Society for Pediatric Nephrology (ESPN) Dialysis Working Group published its recommendations in 2019, graded with the Grading of Recommendations Assessment, Development and Evaluation (GRADE) system. Where evidence was thin, the group marked its expert opinion as such.[[apn24_1]] Its statements most relevant to an attending are these:</p>
<div class="table-wrap"><table>
<thead><tr><th>ESPN 2019 statement</th><th>Grade as published</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>Educate children with CKD and their carers about venous preservation</td><td>Ungraded</td><td>Start at diagnosis, not at the HD referral</td></tr>
<tr><td>Refer children with CKD stage 4 who are being prepared for HD to a dedicated vascular access team</td><td>2D</td><td>Name the surgeon and the imaging service early</td></tr>
<tr><td>Children who need chronic HD should start with a functioning AVF where appropriate</td><td>2C</td><td>A suggestion, weighed against size and expected time to transplant</td></tr>
<tr><td>Reserve cuffed CVLs for very small children, urgent or unplanned HD, patient preference, or a short expected time on HD before transplant</td><td>Ungraded</td><td>Most of your catheters will fall into one of these groups; write which one</td></tr>
<tr><td>Image the central veins when stenosis is suspected, for example after previous catheters</td><td>2D</td><td>Before any fistula in a child who has had lines</td></tr>
<tr><td>Avoid creating an AVF in the arm on the side of a central venous stenosis</td><td>Ungraded</td><td>A fistula cannot drain through a narrowed vein</td></tr>
<tr><td>Create the AVF at least 3 months before its expected use; assess maturation 4 to 6 weeks after creation by examination and duplex ultrasound</td><td>2D; 2D</td><td>Plan backward from the date dialysis is likely to start</td></tr>
</tbody></table></div>
<p>The consensus calls central venous lines &ldquo;CVLs&rdquo;; this module uses CVC for the same device. It does not set a weight cutoff as a recommendation. It notes that earlier guidance suggested considering a fistula in children over 20 kilograms expected to wait more than a year for a transplant, and that fistulas have been created in children under 10 kilograms with microvascular technique.[[apn24_1]] Read that as a signal about surgical skill, not a rule about weight.</p>
<p><strong>The registry.</strong> The International Pediatric Hemodialysis Network (IPHN) followed 552 children from 27 countries prospectively between 2012 and 2017. Over 314 patient-years, 628 catheters, 225 fistulas and 17 grafts were placed. Infections were reported only with catheters, at 1.3 per 1,000 catheter-days, and 47% of those infections required the access to be replaced. Dysfunction ran at 2.5 per 1,000 catheter-days against 1.2 per 1,000 fistula-days. Catheters needed 82% more revisions and almost three times as many replacements at a new site. Fistulas delivered higher blood flow and higher urea clearance (Kt/V, a surrogate for dialysis dose). One-third of children with a fistula still needed a temporary catheter while it matured.[[apn24_2]]</p>
<p>The registry also shows why the comparison is not fair. Catheter use was associated with younger age and with the expectation of an early living related transplant, with a median time to transplant of 14 months against 20 months with fistulas, and a threefold higher rate of living related transplantation.[[apn24_2]] The design was observational. It shows that catheters carry more infection and dysfunction; it does not show that placing a fistula in a given child would have improved survival or growth, because the children who got fistulas were different from the start.</p>
<p><strong>The Philippine reality.</strong> Few surgeons in the country create fistulas in small children, and a transplant date is rarely certain, because donor work-up, cross-matching and costs move at the family&rsquo;s pace. PhilHealth covers HD sessions under PhilHealth Circular (PC) 2024-0023; that circular pays for sessions, not for a particular access, and it does not tell you which access a child should have.[[apn24_7]] If the transplant is likely within months, a well-cared-for catheter is reasonable. If the work-up has stalled, the plan should change.</p>
{{key:Choose the access for the time the child will really spend on HD, not the time the family hopes for. Re-ask the question every three months.}}
"""),
        ("catheter", "The catheter", "Keeping the catheter working", """
<p><strong>Where it goes.</strong> Most pediatric access teams prefer the right internal jugular vein for a tunneled catheter, because the path to the right atrium is short and straight. The subclavian route is avoided: stenosis there threatens every future access in that arm. Femoral catheters are a fallback when the neck veins are unusable, and they carry the problem of a diaper and a moving hip. The tip should sit where blood flows freely, usually near the junction of the superior vena cava and the right atrium; a tip that is too short draws against the vein wall, especially as the child grows taller.</p>
<p><strong>Why it stops working.</strong> Early dysfunction, in the first days, usually means the catheter is kinked, malpositioned or too short. Late dysfunction usually means thrombus inside the lumen or a fibrin sheath around the tip. Growth matters in children: a tip that sat well at 9 may have pulled back into the superior vena cava by 11. The ESPN group suggests tissue plasminogen activator (t-PA) both as a locking solution to prevent catheter thrombosis (2B) and as the thrombolytic for catheter thrombosis (2D); it notes that fibrin-sheath disruption and catheter exchange are rarely used in children and lack pediatric studies.[[apn24_1]] Which lock your unit uses, and how much, comes from the unit&rsquo;s protocol and pharmacy, not from this module.</p>
<div class="table-wrap"><table>
<thead><tr><th>What the nurse reports</th><th>Most likely cause</th><th>What the nurse can do under protocol</th><th>When the nurse calls the POD, and the POD calls you</th></tr></thead>
<tbody>
<tr><td>Arterial pressure alarm (very negative) at the start; flow better when the child turns or lifts the head</td><td>Tip against the vein wall; tip pulled back with growth</td><td>Reposition the child; check clamps and lines for kinks; reverse lines only if the unit protocol allows</td><td>Recurring at two sessions, or blood flow too low to deliver the session: call for a chest radiograph and an access review</td></tr>
<tr><td>Cannot aspirate from one or both lumens</td><td>Thrombus in the lumen or at the tip</td><td>Gentle flush per protocol; never force a flush against resistance</td><td>Same session: the thrombolytic decision belongs to the physician and the unit protocol</td></tr>
<tr><td>Rising venous pressure through the session</td><td>Clotting in the venous lumen or the circuit; kink</td><td>Inspect the circuit and the external catheter; follow the anticoagulation protocol</td><td>Circuit clotted with blood not returned: tell the POD at once (blood loss in a small child)</td></tr>
<tr><td>Swelling of the face, neck or arm on the catheter side</td><td>Central vein thrombosis or stenosis</td><td>Stop and examine; do not keep running against rising pressure</td><td>Immediately; this needs imaging and a decision about the catheter</td></tr>
<tr><td>Cuff visible at the exit site, or the catheter longer outside than recorded</td><td>Catheter migration; risk of dislodgement</td><td>Do not use until reviewed; secure; measure the external length</td><td>Immediately; a migrated catheter may sit in the wrong vein</td></tr>
<tr><td>Bleeding at the exit site after insertion or during anticoagulation</td><td>Local bleeding; anticoagulation effect</td><td>Pressure; check the dressing and the circuit anticoagulation</td><td>Bleeding that does not stop with pressure, or any fall in blood pressure</td></tr>
</tbody></table></div>
<p><strong>Care that prevents trouble.</strong> The Standardizing Care to Improve Outcomes in Pediatric End Stage Renal Disease (SCOPE) collaborative introduced standardized catheter care bundles across North American pediatric dialysis centers. In 325 children with tunneled catheters at 15 centers, bundle compliance reached 87.6%, and the adjusted catheter-associated bloodstream infection (CA-BSI) rate fell from 3.3 per 100 patient-months before the bundles to 0.8 per 100 patient-months 48 months later.[[apn24_3]] That is a before-and-after quality improvement design without a control group. Secular trends and attention may explain part of the fall, but the direction is consistent with what a careful connection and dressing technique should do.</p>
<div class="tc-scene"><span class="tc-lab">On your monthly visit, the dressing &middot; fictional</span><p>At the adult unit in Angeles City you watch a new nurse connect Kyla, 10. She wears a mask but the child does not; the caps come off and the hubs sit open on the drape while she reaches for the syringes.</p><p>You do not correct her in front of the family. Afterward you sit with the head nurse, walk through the unit&rsquo;s catheter connection checklist step by step, and agree that the nurse will be observed for her next three connections.</p><p class="tc-scene-take"><b>What this shows.</b> Most catheter infections start at the hub. Watching one connection tells you more than any culture report.</p></div>
{{key:A catheter that fails early is in the wrong place. A catheter that fails late is clotting or sheathed. Find which before anyone changes the prescription.}}
{{fig:apn24_b}}
"""),
        ("infection", "Catheter infection", "Fever on dialysis: catheter-related bloodstream infection", """
<p><strong>How organisms get in.</strong> In the first weeks, organisms from the skin track along the outside of the catheter through the tunnel. Later, most enter through the hub, travel down the lumen and settle in a biofilm on the catheter&rsquo;s inner wall. When the circuit is connected and the pump starts, that biofilm sheds bacteria and endotoxin into the blood. That is why rigors that begin minutes after connection point to the catheter until proven otherwise.</p>
<p><strong>The guideline.</strong> The Infectious Diseases Society of America (IDSA) 2009 guideline grades its statements by strength (A to C) and quality of evidence (I to III). For patients on HD through a catheter, it recommends drawing peripheral blood cultures from vessels that will not be needed for a future fistula, such as hand veins (A-III); cultures drawn from the bloodlines connected to the catheter during dialysis are acceptable when no peripheral sample can be obtained (B-II). Empirical therapy should include vancomycin and gram-negative coverage chosen from the local antibiogram (A-II).[[apn24_5]] Doses and drug choices come from your unit&rsquo;s pediatric formulary and a pharmacist, weighed for the child&rsquo;s size and for dialysis clearance.</p>
<p><strong>When the catheter must come out.</strong> IDSA recommends always removing the infected catheter when HD catheter-related bloodstream infection (CRBSI) is caused by <em>Staphylococcus aureus</em>, <em>Pseudomonas</em> species or <em>Candida</em> species, and inserting a temporary catheter at another site (A-II); if no other site exists, exchange over a guidewire (B-II). For other organisms, therapy can start without immediate removal. If fever, chills, unstable blood pressure or altered mental status resolve within 2 to 3 days and there is no metastatic infection, the catheter can be exchanged over a guidewire or retained with an antibiotic lock after each session for 10 to 14 days (B-II). Persistent symptoms or metastatic infection mean removal (B-II).[[apn24_5]]</p>
<p>The guideline is frank about children. Small blood volumes reduce the yield of cultures, peripheral samples are hard to obtain, and losing access is a real harm, so treatment without removal is often attempted; such children should be watched closely and the device removed if they deteriorate or the infection recurs. Fungal infection treated without removal has a low success rate.[[apn24_5]] The IDSA grades rest largely on adult data and on expert opinion, which is what the &ldquo;II&rdquo; and &ldquo;III&rdquo; mean.</p>
<p><strong>What the SCOPE cohort adds.</strong> In 1,277 children from 35 pediatric dialysis centers, 79.7% dialyzed through a catheter. Among them, mupirocin at the exit site was associated with a higher CA-BSI rate (rate ratio 4.45), and centers that improved their compliance with care practices saw CA-BSI fall from 2.71 to 0.71 per 100 patient-months.[[apn24_4]] The mupirocin signal is an observational association and may reflect which children received it; it is a reason to look at your own unit&rsquo;s practice, not proof of harm.</p>
{{flow:Fever or rigors during HD through a catheter: the first 30 minutes|At the chair::The nurse stops fluid removal, checks blood pressure, pulse, temperature, oxygen saturation and mental state, and calls the POD. Inspect the exit site and tunnel for redness, tenderness or pus.|Cultures before antibiotics::Blood cultures from the catheter or the bloodlines and, if feasible, a peripheral sample from a hand vein. Adult bottles are acceptable when pediatric bottles are not stocked; label the source of each sample.|Decide whether to continue::If the child is unstable, stop the session; return blood only if the circuit is intact and the POD agrees. A stable child may complete a short session on the attending&rsquo;s advice.|First dose::Empirical antibiotics chosen from the unit&rsquo;s pediatric protocol and antibiogram, covering gram-positive and gram-negative organisms. The dose comes from the formulary and pharmacist, not from memory.|Call the attending::The POD calls you with the vital-sign trend, the exit site, what was drawn and given. Agree who reviews cultures at 24 to 48 hours.|Decide where the child is safest::Hypotension that does not recover, altered mental state, or a tender tunnel means transfer to a hospital with a pediatric ward or intensive care unit today.}}
{{call:<ul><li>Systolic blood pressure that does not recover after fluid removal stops, or a heart rate that keeps rising</li><li>Altered mental state, poor perfusion, or oxygen saturation falling</li><li>Pus, redness or tenderness along the tunnel</li><li>Culture growing <em>Staphylococcus aureus</em>, <em>Pseudomonas</em> or yeast</li><li>Fever that persists or returns after 2 to 3 days of treatment</li><li>Swelling of the face, neck or arm on the catheter side</li></ul>}}
{{key:Rigors minutes after connection are the catheter speaking. Culture first, treat the same hour, and decide about removal by the organism and the child&rsquo;s course, not by the family&rsquo;s fear or the unit&rsquo;s convenience.}}
{{fig:apn24_c}}
"""),
        ("practice", "Fistulas and the plan", "Fistulas in small arms, needles, and the written access plan", """
<p><strong>Making the fistula work.</strong> A fistula in a child is a team project. Before surgery, the ESPN group suggests a structured history, examination and duplex ultrasound (2C), and imaging of the central veins when stenosis is suspected (2D). It suggests placing the fistula in the non-dominant arm where possible (ungraded) and distally in the arm (2D). Once the fistula has matured adequately, cannulation should use the rope-ladder or buttonhole technique (2C), with aseptic technique (ungraded).[[apn24_1]]</p>
<p><strong>Watching it.</strong> The ESPN group suggests routine structured physical examination of every fistula by nurses and physicians (2D), and urgent referral to the access surgeon when dysfunction is found (ungraded).[[apn24_1]] A healthy fistula has a soft, continuous thrill and a vein that collapses when the arm is raised. Steal, where the fistula diverts so much blood that the hand becomes cold, pale or painful, is possible but rarely seen in children.[[apn24_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding on examination</th><th>Likely meaning</th><th>Who acts, and how fast</th></tr></thead>
<tbody>
<tr><td>No thrill, no bruit</td><td>Thrombosed fistula</td><td>Do not cannulate. Call the attending the same day; rescue is time-sensitive</td></tr>
<tr><td>Pulsatile, hard segment; weak or systolic-only thrill</td><td>Outflow stenosis</td><td>Access review and duplex ultrasound within days</td></tr>
<tr><td>Prolonged bleeding after needles at several sessions</td><td>High pressure in the vein from an outflow stenosis</td><td>Access review; check anticoagulation</td></tr>
<tr><td>Swollen arm, prominent chest wall veins</td><td>Central venous stenosis, often from an old catheter</td><td>Central venous imaging; the fistula may be at risk</td></tr>
<tr><td>Cold, pale or painful hand during dialysis</td><td>Steal</td><td>Same-day surgical review</td></tr>
</tbody></table></div>
<p><strong>Needles and fear.</strong> For a 10-year-old, two large needles three times a week can become the worst part of kidney failure. The ESPN text recommends local anesthetic creams to ease fistula cannulation, whatever technique is used.[[apn24_1]] Add the simple things: the same experienced cannulator where possible, a child life or play approach that lets the child rehearse, and honesty about what will hurt. A child who dreads the needles will skip sessions as an adolescent.</p>
<p><strong>The written access plan.</strong> Few Philippine units have a dedicated pediatric vascular access team, so the plan in the chart has to do the team&rsquo;s work. One page is enough:</p>
<div class="table-wrap"><table>
<thead><tr><th>Line in the plan</th><th>Example for Carlo</th></tr></thead>
<tbody>
<tr><td>Present access, date placed, who placed it, tip position on the last film</td><td>Right internal jugular tunneled CVC, placed seven months ago at the pediatric center</td></tr>
<tr><td>Why this access, and the expected time on HD</td><td>Expected living related transplant; donor work-up stalled; reassess at the next monthly review</td></tr>
<tr><td>Veins to protect</td><td>No PICC, no blood draws or cannulas above the wrist in either arm; left arm has had a PICC</td></tr>
<tr><td>Next access and the trigger to make it</td><td>If no transplant date by a set month: vein mapping and central venous imaging, then fistula referral</td></tr>
<tr><td>What the unit does when the access fails, and whom it calls</td><td>Dysfunction and fever pathways from this module; attending&rsquo;s and backup&rsquo;s numbers</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">At the transplant review, the plan that changed &middot; fictional</span><p>Jessa, 14, has dialyzed through a catheter for 16 months &ldquo;while waiting for transplant.&rdquo; Her father&rsquo;s evaluation stopped when he left for work in Qatar; no other donor has come forward.</p><p>You tell the family that the catheter was the right bridge for a short wait and is no longer the right access for a long one. You order vein mapping and central venous imaging and refer her to the one surgeon in the region who creates fistulas in teenagers, while the transplant team keeps looking for a donor.</p><p class="tc-scene-take"><b>What this shows.</b> A bridge that has lasted longer than planned is no longer a bridge. The access plan has a date on it for that reason.</p></div>
{{key:Write the next access before you need it, give the plan a review date, and put the vein rules where the next prescriber will read them.}}
{{call:<ul><li>Loss of thrill or bruit in a fistula</li><li>A cold, pale or painful hand during dialysis</li><li>Arm, face or neck swelling on the side of a catheter or fistula</li><li>Bleeding from an access that does not stop with firm pressure</li><li>A catheter that has moved, a visible cuff, or a cracked hub</li></ul>}}
"""),
    ],
    "debrief": [
        "<p><strong>The next 30 minutes.</strong> Rigors and fever 20 minutes into a session through a catheter are catheter-related bloodstream infection until proven otherwise, and Carlo&rsquo;s falling blood pressure and rising pulse say he is already septic. Paracetamol and Friday cultures is the wrong plan. Ask the nurse to stop fluid removal and the POD to draw blood cultures now, from the catheter or bloodlines and, if possible, from a hand vein, using adult bottles if pediatric ones are not stocked. The first dose of empirical antibiotics covering gram-positive and gram-negative organisms should be given within the hour, chosen from the unit&rsquo;s pediatric protocol with a pharmacist. Stop the session; return the blood only if the circuit is intact. With a heart rate of 138 and a pressure below his baseline, he needs a pediatric bed today: call the pediatric center, speak to the accepting physician, and send a written endorsement with the vital-sign trend, the cultures drawn and the time of the first dose.</p>",
        "<p><strong>The catheter.</strong> Not necessarily, and not at the chair. IDSA recommends removal when the culture grows <em>Staphylococcus aureus</em>, <em>Pseudomonas</em> or <em>Candida</em>, when symptoms persist beyond 2 to 3 days, when there is metastatic infection, or when the tunnel is infected. Otherwise the catheter can be treated in place with systemic antibiotics and an antibiotic lock, or exchanged over a guidewire, which matters for a child whose left arm has already lost a vein. The decision belongs to the attending with the access team, at the receiving hospital, once cultures are back and the child&rsquo;s course is clear. Explain this to Aling Marites in plain words: pulling the line in the unit would leave Carlo with no way to dialyze and would not treat the infection faster.</p>",
        "<p><strong>Prevention and the plan.</strong> Carlo&rsquo;s infection most likely started at the hub, so review how the adult unit connects and dresses his catheter, against a written bundle like the ones the SCOPE centers used. His left-arm PICC should have been avoided; write the vein rules on the front of his chart. Then face the real issue: a transplant that was expected within months has stalled on cost. Ask the transplant coordinator and the social worker to move the donor work-up, and set a date. If there is still no transplant date by then, order vein mapping and central venous imaging and refer him for a fistula in the right arm, because a catheter that has become a long-term access is now the riskier choice.</p>",
    ],
    "skills": {"title": 'Vascular access in children',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Writes a one-page access plan with protected veins, next access and review date", False),
                         ("Talks a nurse through catheter dysfunction using the troubleshooting table", False),
                         ("Leads a simulated fever-on-HD call: cultures, first dose, removal decision and transfer", False),
                         ("Examines a fistula and explains the findings to the unit nurse", False)],
               "placement": "Simulation or supervised practice"},
    "quiz": [
        ("A 13-year-old dialyzing through a tunneled catheter develops rigors 15 minutes after connection. What is the most appropriate first step?",
         ["Give paracetamol and finish the session, culturing at the next session",
          "Draw blood cultures before antibiotics, then give empirical therapy the same hour",
          "Remove the catheter at the chair",
          "Start oral antibiotics and send the child home"],
         1,
         "Rigors soon after connection suggest catheter-related bloodstream infection. Cultures first, then empirical therapy covering gram-positive and gram-negative organisms (IDSA A-II), chosen from the unit&rsquo;s pediatric protocol."),
        ("Which culture result makes IDSA 2009 recommend removing an infected hemodialysis catheter?",
         ["Staphylococcus aureus",
          "Coagulase-negative staphylococci in a child who defervesces within 48 hours",
          "Escherichia coli with prompt clinical response",
          "No growth after 48 hours"],
         0,
         "IDSA recommends removal for S. aureus, Pseudomonas and Candida (A-II). Other organisms can be treated with the catheter in place if the child responds within 2 to 3 days."),
        ("What did the IPHN registry show about catheters and fistulas in children?",
         ["Fistulas had more infections than catheters",
          "Placing a fistula improved survival in a randomized comparison",
          "There was no difference in dysfunction",
          "Infections were reported only with catheters, and catheters had more dysfunction and replacements"],
         3,
         "Catheter infections ran at 1.3 per 1,000 catheter-days; dysfunction 2.5 vs 1.2 per 1,000 days. The study was observational; catheter use was associated with age and with an expected early transplant."),
        ("A catheter&rsquo;s arterial pressure alarm sounds at the start of each session and improves when the child turns the head. What is the most likely cause?",
         ["Catheter infection",
          "Dialyzer clotting",
          "The tip lying against the vein wall or pulled back as the child grew",
          "Hyperkalemia"],
         2,
         "Positional, early-session inflow problems point to tip position. Growth can pull a tip back into the superior vena cava; a chest radiograph and access review follow if it recurs."),
        ("Which ESPN 2019 statement applies to a child with a central venous stenosis on the left?",
         ["Avoid creating a fistula in the left arm",
          "Place the fistula in the left arm because it is non-dominant",
          "Central venous stenosis has no bearing on fistula placement",
          "Always place a graft instead"],
         0,
         "A fistula drains through the central veins on its side. The ESPN group advises avoiding an AVF on the side of a central venous stenosis (ungraded) and imaging central veins when stenosis is suspected (2D)."),
    ],
    "terms": [("AVF", "Arteriovenous fistula"), ("AVG", "Arteriovenous graft"), ("CA-BSI", "Catheter-associated bloodstream infection"),
              ("CKD", "Chronic kidney disease"), ("CRBSI", "Catheter-related bloodstream infection"), ("CVC", "Central venous catheter"),
              ("CVL", "Central venous line"), ("ESPN", "European Society for Pediatric Nephrology"),
              ("GRADE", "Grading of Recommendations Assessment, Development and Evaluation"), ("HD", "Hemodialysis"),
              ("IDSA", "Infectious Diseases Society of America"), ("IPHN", "International Pediatric Hemodialysis Network"),
              ("KDOQI", "Kidney Disease Outcomes Quality Initiative"), ("Kt/V", "Urea clearance multiplied by time, divided by urea distribution volume"),
              ("PC", "PhilHealth Circular"), ("PICC", "Peripherally inserted central catheter"), ("POD", "Physician on duty"),
              ("SCOPE", "Standardizing Care to Improve Outcomes in Pediatric End Stage Renal Disease"), ("t-PA", "Tissue plasminogen activator")],
    "readings": [('hemodialysis-access-lifeline.html', 'Transforming the Achilles Heel of Hemodialysis Access into a &quot;Lifeline That Lasts for a Lifetime&quot;'),
                 ('dialysis-access-infection.html', 'When the Access Gets Infected'),
                 ('dialysis-access-care.html', 'Dialysis Access Care: Your Lifeline — Protect It Every Day')],
    "calcs": ["calc-catheter-exposure.html", "calc-access-infection-rate.html", "calc-av-fistula-maturation.html",
              "calc-hand-ischemia-dbi.html", "calc-bsa.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
