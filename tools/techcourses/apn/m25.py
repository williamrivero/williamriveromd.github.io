# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 25: HD emergencies, water safety, and children in adult HD units.
Written November 27, 2026 for the Renal Care Academy in the voice of the Physician on Duty modules, to the medical teaching
standard. Study figures from the PubMed abstracts (Hothi 2008, Fadel 2014, Geer 2017, Pouria 1998, de Oliveira 2009); the PCRRT
recommendations are expert opinion by the authors' own statement. Water requirements from DOH AO 2013-0003 as listed on the HFSRB
dialysis-clinic page and the Supreme Court e-library text; no contaminant limits are restated here. No doses. Every case is fictional."""

MODULE = {
    "image_alt": "In an adult dialysis unit, a nurse lowers the chair of a teenage boy who is pale and holding his head, while a physician on duty checks his pupils and the boy's mother stands close by.",
    "objectives": [
        "Explain why intradialytic hypotension and dialysis disequilibrium strike children faster, and set first sessions that prevent them.",
        "Lead the response to the hemodialysis emergencies an adult unit will face with a child, including when to stop the pump and when not to return blood.",
        "Make an adult hemodialysis unit safe for a child: water quality under DOH AO 2013-0003, pediatric equipment, stop-and-call rules, consent and school.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; a child in a unit built for adults</span>Many Filipino children on hemodialysis (HD) dialyze in adult units, often far from you. The nurses and the physician on duty (POD) are skilled with adults and see a child only occasionally. You own the child&rsquo;s prescription and the rules that make the unit safe for that child: what the first sessions look like, what equipment must be in the room, which signs stop the session, who is called, and whether the water the child is dialyzed against meets the Department of Health (DOH) standard. The medical director owns the unit; you make sure the child fits safely inside it.</div>
{{plain:Picture taking a glass of water out of a bucket and the same glass out of a cup. The bucket hardly changes. The cup is half empty. An adult on HD is the bucket; a 20-kilogram child is the cup. The same dialysis machine, the same lines and the same habits remove the same glass.}}
<p>The picture has a limit. A cup cannot fight back; a child can, for a while. Children hold their blood pressure by speeding the heart and tightening the vessels, so the pressure may look normal until the reserve is gone, then fall quickly. And dialysis does not only remove water. It removes urea from the blood faster than from the brain, and in a child starting dialysis that difference can pull water into the brain. The cup picture explains hypotension; the brain needs its own picture.</p>
{{cards:Key numbers|Caruaru, Brazil, 1996 (water)::All 126 patients in one HD unit became ill after water from a lake with heavy cyanobacterial growth was used; 60 died|Relative blood volume in children (Hothi 2008)::Falls to 88% by hour 1, 84% by hour 2 and 82% by hour 3 separated sessions with and without complications (retrospective)|Intradialytic events with blood-volume-guided removal (Fadel 2014)::33 to 4 per 180 sessions (uncontrolled, 15 children)|DOH AO 2013-0003, microbiological testing::Raw water, product water and point of use, at least every month|DOH AO 2013-0003, chemical testing::Point of use, every six months}}
<p>Most HD sessions in children are uneventful. A few go wrong fast: a falling pressure, a confused child in the first hour, air in a line, cherry-red blood, a needle out of a fistula. Your work is to set up the first sessions and the unit so these rarely happen, to make sure the nurse and the POD know exactly when to stop and call, and to check that the water a child&rsquo;s blood meets every session is as clean as the law requires.</p>
""",
    "case": {"title": "Vomiting in the first hour",
             "html": """
<p>Rafael &ldquo;Paeng&rdquo; Bautista is 13 and weighs 40 kilograms. He was referred late: his kidney failure from untreated posterior urethral valves was found only when he collapsed at school in Tarlac City three weeks ago. His blood urea nitrogen was 186 mg/dL at that admission. He now dialyzes at an adult freestanding unit near home, because the nearest pediatric HD unit is in Manila, about 125 kilometers away. His first two sessions, on your written order, were short and gentle.</p>
<p>It is 9:40 a.m., 50 minutes into his third session. The order sheet for today was rewritten by a covering nurse from the unit&rsquo;s adult template: four hours, the unit&rsquo;s standard blood flow, the adult dialyzer. Paeng has vomited twice and says his head hurts. He is restless and answers questions slowly. His blood pressure is 168/100 mm Hg, pulse 66 per minute. The POD calls you: &ldquo;I gave an antiemetic. His pressure is high, not low, so he is not dry. Can we continue?&rdquo; His mother asks whether this is normal. The unit&rsquo;s resuscitation cart has adult masks and an adult dosing chart only.</p>
""",
             "questions": ["What is happening to Paeng, and what do you tell the POD right now?",
                           "Which other HD emergencies must the POD exclude at the chair?",
                           "What has to change in this unit before Paeng&rsquo;s next session?"]},
    "sections": [
        ("physiology", "Why children crash", "Why a child on HD crashes faster", """
<p><strong>Volume.</strong> The machine removes water only from the blood. The tissues refill the vessels, but refilling has a speed limit. A child&rsquo;s blood volume is small, the extracorporeal circuit holds a larger share of it than in an adult (Module 23 covers the circuit and priming), and a weight gain that looks modest in kilograms may be a large percentage of the child. Children defend their pressure with a fast heart rate and tight vessels, so a normal pressure can hide a heart that is already struggling. In 22 adolescents and young adults on chronic HD, the cardiac index fell midway through the session in 12 (54%) without any hypotension, and the size of the blood volume fall was the only factor associated with that decline.[[apn25_5]] That small study does not show long-term harm, but it shows that the blood pressure cuff can be the last instrument to notice.</p>
<p><strong>Osmoles.</strong> Urea crosses cell membranes slowly enough that dialysis lowers blood urea faster than brain urea. For a while the brain is relatively hyperosmolar, and water moves into it. Brain cells in chronic uremia also hold extra organic osmolytes that they cannot shed quickly. The result is cerebral edema and raised intracranial pressure: dialysis disequilibrium syndrome (DDS). Its signs range from restlessness and headache to vomiting, confusion, seizures and coma. It is rare but serious, its mechanism is not fully understood, and treatment once it develops is rarely successful, so prevention matters most.[[apn25_1]] The children at risk are the ones starting dialysis with a very high urea, the very young, and those with an existing brain problem.</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Mechanism</th><th>Who is at risk</th><th>What you see at the chair</th></tr></thead>
<tbody>
<tr><td>Intradialytic hypotension (IDH)</td><td>Fluid removal outruns refilling; vessel tone and the heart cannot compensate</td><td>Small children, large weight gain, adult-sized circuit, inaccurate target weight</td><td>Rising heart rate first, then yawning, pallor, cramps, abdominal pain, vomiting, then a low pressure</td></tr>
<tr><td>DDS</td><td>Urea falls in blood faster than in brain; water moves into the brain</td><td>First sessions, very high urea, aggressive clearance</td><td>Headache, vomiting, restlessness, confusion, rising blood pressure with a slow pulse, seizures</td></tr>
<tr><td>Hypoglycemia</td><td>Glucose lost into dialysate in a small child with poor intake</td><td>Infants and small children, poor feeding</td><td>Sweating, irritability, drowsiness</td></tr>
<tr><td>Hypothermia</td><td>Blood cooled in a long circuit; small body mass</td><td>Infants and small children</td><td>Cold peripheries, shivering, falling temperature</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">On the phone, the adult habit &middot; fictional</span><p>A POD in Batangas calls about Nicole, 8, 22 kilograms, three hours into her session. Her pressure is 96/60, which he calls normal. Her heart rate has climbed from 92 to 140 and she is quiet.</p><p>You ask him to stop fluid removal and lay her flat. Her heart rate falls to 110 within ten minutes. You agree to end the session early and revise her target weight on Friday.</p><p class="tc-scene-take"><b>What this shows.</b> In a child, the pulse warns before the pressure does. Ask for the heart rate trend, not only the last blood pressure.</p></div>
{{key:In a child, a rising heart rate is the first sign of volume trouble, and vomiting with a headache in the first sessions is the brain until proven otherwise.}}
{{fig:apn25_a}}
"""),
        ("evidence", "Evidence", "What the evidence shows", """
<p><strong>The evidence is thin, and the authors say so.</strong> The Pediatric Continuous Renal Replacement Therapy (PCRRT) Workgroup reviewed strategies to prevent IDH in children: frequent blood pressure monitoring, dialysate sodium profiling, ultrafiltration guided by blood volume monitoring, dialysate cooling, hemodiafiltration, and some medicines. It concluded that none has been studied extensively in children and that its recommendations reflect expert opinion.[[apn25_2]] Treat them as a reasoned starting point, not as tested practice.</p>
<p><strong>Blood volume monitoring.</strong> Hothi and colleagues reviewed 74 blood volume records from children on HD. Sessions with complications had a steeper fall in relative blood volume in the first hour and a change in heart rate. Thresholds of 88% at the end of hour 1, 84% at hour 2 and 82% at hour 3 separated sessions with and without complications; no value at hour 4 did, and polyuric children developed complications at lower thresholds than oliguric children.[[apn25_3]] The design was retrospective and single-center, so the numbers describe that cohort, not a target for your patient. In an uncontrolled before-and-after study of 15 children, ultrafiltration guided by noninvasive hematocrit monitoring was followed by a fall in intradialytic morbid events from 33 to 4 per 180 sessions, without a change in blood pressure.[[apn25_4]] A review of blood pressure management in children on dialysis places blood volume monitoring and bioimpedance alongside clinical judgment in setting target weight, and stresses that reducing interdialytic weight gain is critical.[[apn25_10]] Taken together, the studies suggest that watching the slope of blood volume can prevent episodes; they do not show fewer hospital admissions or better growth.</p>
<p><strong>Disequilibrium.</strong> No trial defines a safe first session for children. The pediatric review by Zepeda-Orozco and Quigley explains the physiology and argues for avoiding DDS rather than treating it, because treatment once it develops is rarely successful.[[apn25_1]] In practice, that means a deliberately limited first session or two, with the actual blood flow, duration and dialyzer set by the attending and the unit&rsquo;s pediatric protocol, and reassessment before each step up.</p>
<div class="tc-scene"><span class="tc-lab">Writing the first sessions &middot; fictional</span><p>Angel, 9, 24 kilograms, arrives at a pediatric ward in Iloilo with a very high urea, fluid overload and a new tunneled catheter. The resident asks you for &ldquo;the usual four hours.&rdquo;</p><p>You write a deliberately short first session with a modest clearance goal and limited fluid removal, using the unit&rsquo;s pediatric protocol for blood flow and dialyzer, and a second session the next day on the same terms. You add three lines for the nurse: check the neurologic state every 30 minutes, stop and call for headache or vomiting, and do not step up until you have reviewed the post-session urea.</p><p class="tc-scene-take"><b>What this shows.</b> The first sessions are a deliberate under-treatment of urea to protect the brain. Fluid can be addressed separately; the urea gradient cannot be undone.</p></div>
<p><strong>Water.</strong> The evidence here is not a trial but a set of disasters. After a drought in February 1996, a unit in Caruaru, Brazil, used water from a lake with a heavy growth of cyanobacteria. All 126 patients developed acute neurotoxicity and liver injury; 60 died. Microcystins, toxins made by the cyanobacteria, were found in patients&rsquo; serum, dialysis filters and water-treatment columns.[[apn25_6]] In a Brazilian unit in 2004, dialysate chloramine rose and patients developed an outbreak of anemia from hemolysis; it resolved within a month after the activated charcoal column was exchanged, without a change in erythropoietin doses.[[apn25_7]] A child&rsquo;s blood meets many liters of dialysate across a thin membrane at every session, and a small body has little reserve against a toxin. Water safety is a pediatric safety issue.</p>
{{key:Most pediatric HD safety rules rest on physiology and expert opinion, not trials. Say so to the unit, and follow them anyway: the cost of being wrong falls on a small body.}}
"""),
        ("emergencies", "Emergencies", "The emergencies an adult unit will meet with a child", """
<p>The nurse is at the chair first; the POD is a few steps away; you are on the phone. This table is written for all three. The rule that governs it is old and simple: stop the blood pump at once only when continuing would add harm (air, hemolysis, a severe dialyzer reaction, blood loss from a dislodged needle or an open line). For everything else, stop fluid removal, protect the child, and think.</p>
<div class="table-wrap"><table>
<thead><tr><th>Emergency</th><th>Early sign in a child</th><th>Why it happens</th><th>First action at the chair</th><th>Return the blood?</th></tr></thead>
<tbody>
<tr><td>IDH</td><td>Rising pulse, yawning, pallor, abdominal pain, vomiting</td><td>Removal faster than refilling</td><td>Lay flat, legs raised as breathing allows; stop fluid removal; fluid per unit protocol if no recovery</td><td>Yes, if the session ends and the circuit is sound</td></tr>
<tr><td>DDS</td><td>Headache, vomiting, restlessness, confusion, seizure</td><td>Cerebral edema from the urea gradient</td><td>Slow or stop dialysis on the physician&rsquo;s order; protect the airway; check glucose; call</td><td>Yes, if the circuit is sound</td></tr>
<tr><td>Air embolism</td><td>Sudden breathlessness, cough, chest pain, cyanosis, collapse; foam in the venous line</td><td>Air entering the circuit through a loose connection or empty line</td><td>Clamp the venous line, stop the pump, lay the child on the left side with head down, give oxygen</td><td>No</td></tr>
<tr><td>Hemolysis</td><td>Chest or back pain, breathlessness, cherry-red or translucent venous blood</td><td>Contaminated or overheated dialysate, kinked lines, chloramine</td><td>Stop the pump, clamp the lines, keep the circuit and dialysate for testing, check potassium urgently</td><td>No</td></tr>
<tr><td>Dialyzer reaction</td><td>Itching, wheeze, flushing, hypotension in the first minutes</td><td>Reaction to the dialyzer or its sterilant</td><td>Stop the pump; treat anaphylaxis by the unit&rsquo;s pediatric protocol; keep the dialyzer</td><td>No, if severe</td></tr>
<tr><td>Venous needle dislodgement or open line</td><td>Blood on the sheet or floor; the venous pressure alarm may not sound</td><td>Needle pulled out under a blanket; line disconnected</td><td>Stop the pump, clamp, apply pressure, estimate blood lost</td><td>No; call at once for a small child</td></tr>
<tr><td>Hyperkalemia before or after a session</td><td>Weakness, palpitations, a broad or peaked complex on the monitor</td><td>Missed session, diet, tissue breakdown</td><td>Electrocardiogram; follow the stabilize-shift-remove sequence of Module 4 under the unit&rsquo;s protocol</td><td>Not applicable</td></tr>
<tr><td>Seizure</td><td>Generalized or focal seizure</td><td>DDS, hypoglycemia, hypertension, hypocalcemia</td><td>Protect, side position, oxygen, glucose check; stop dialysis and call</td><td>Yes, if the circuit is sound and the seizure has stopped</td></tr>
</tbody></table></div>
<p>Two points need emphasis for a child. First, blood loss that an adult would tolerate is large for a 20-kilogram child, so a clotted circuit with blood not returned, or a needle out under the blanket for a few minutes, is an emergency in its own right. Second, every drug given at the chair, from fluid boluses to antiemetics to resuscitation drugs, is weight-based. The unit needs a pediatric emergency drug reference prepared by a pharmacist from the hospital&rsquo;s formulary, posted on the cart, with the child&rsquo;s current weight written on the treatment sheet.</p>
{{flow:A child in trouble during HD: the first two minutes|Go to the chair::Look at the child: responsive, breathing, pulse, color. Call for help early.|Lay the child down::Flat, legs raised as breathing allows; on the side if vomiting or seizing.|Stop fluid removal::The pump keeps running unless air, hemolysis, a severe reaction or blood loss is suspected.|Look at the lines::Venous line for foam or cherry-red blood; every connection; the needle sites under the blanket.|Measure::Heart rate and rhythm, blood pressure, oxygen saturation, temperature, glucose.|Call::The POD at once; the POD calls the attending pediatric nephrologist with the trend, what was done, and what is being asked.}}
{{call:<ul><li>Any seizure, or confusion, restlessness or vomiting with headache in the first sessions</li><li>Heart rate rising steadily, or blood pressure falling despite stopping fluid removal</li><li>Foam in the venous line, or sudden breathlessness or chest pain</li><li>Cherry-red or translucent blood in the venous line, or several patients unwell at the same time</li><li>Blood loss from a needle, line or clotted circuit in a child under 30 kilograms</li><li>Wheeze, flushing or collapse in the first minutes of a session</li></ul>}}
{{key:Stop the pump for air, hemolysis, a severe reaction or blood loss. For everything else, stop the fluid removal, lie the child down, and look before you act.}}
{{fig:apn25_b}}
"""),
        ("water", "Water safety", "Water as a pediatric hazard, and what DOH AO 2013-0003 requires", """
<p><strong>Why water matters more than anything else in the room.</strong> Tap water is safe to drink because the gut is a selective barrier and the volume is small. In HD, water becomes dialysate and meets the blood across a thin membrane, session after session. Disinfectants that make drinking water safe, such as chlorine and chloramine, become toxins: chloramine oxidizes hemoglobin and lyses red cells.[[apn25_7]] Bacteria and their fragments in poorly maintained systems drive fever and inflammation. A water system that fails can harm every patient on the shift at once.</p>
<p><strong>The Philippine standard.</strong> DOH Administrative Order (AO) 2012-0001 sets the licensure rules for dialysis facilities and defines water treatment against the standards of the Association for the Advancement of Medical Instrumentation (AAMI).[[apn25_9]] DOH AO 2013-0003, listed by the Health Facilities and Services Regulatory Bureau (HFSRB) among the issuances for dialysis clinics, sets the implementing guidelines for analyzing, monitoring and maintaining that water.[[apn25_8]] Its main provisions, as published:</p>
<div class="table-wrap"><table>
<thead><tr><th>What AO 2013-0003 sets</th><th>As stated in the order</th><th>What the attending checks</th></tr></thead>
<tbody>
<tr><td>Who is responsible</td><td>The medical director is responsible for the quality of water in the HD clinic, and that involvement must be documented, for example by initialing test results</td><td>Who signs the results in the unit where your patient dialyzes</td></tr>
<tr><td>Where water is sampled</td><td>Raw water, product water after the reverse osmosis (RO) system, and the point of use</td><td>That all three points appear on the latest report</td></tr>
<tr><td>Microbiological testing</td><td>All three points before the unit opens, then at least every month</td><td>The date of the most recent report</td></tr>
<tr><td>Chemical testing</td><td>Point of use before the unit opens, then every six months, as amended in the order</td><td>The date of the most recent chemical report</td></tr>
<tr><td>Product-water total dissolved solids (TDS)</td><td>Measured, monitored and recorded weekly in the clinic logbook</td><td>That the logbook is current</td></tr>
<tr><td>Who collects samples</td><td>Staff of DOH-accredited laboratories, with set alternatives</td><td>That the laboratory is accredited</td></tr>
<tr><td>When a result fails</td><td>The clinic temporarily stops operating until a repeat test of the failing parameter complies, notifies patients, and takes corrective action such as cleaning or replacing RO membranes and disinfecting the distribution loop</td><td>Whether your patient&rsquo;s family was told, and when dialysis resumed</td></tr>
</tbody></table></div>
<p>The order&rsquo;s numeric limits for bacteria and chemical contaminants are set out in its text and annexes; the copy available online is partly illegible, and the order&rsquo;s own frequency table differs from its amended chemical-testing section. This module does not restate the limits. The unit&rsquo;s technical staff and medical director hold the current table, and they are the ones to ask.[[apn25_8]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What fails</th><th>What the child may show</th><th>Who catches it first</th></tr></thead>
<tbody>
<tr><td>Carbon filter exhausted; chloramine breaks through</td><td>Falling hemoglobin, hemolysis, needing more erythropoietin</td><td>The technician&rsquo;s chlorine check before the shift</td></tr>
<tr><td>RO membrane failing</td><td>Usually nothing at first</td><td>The weekly TDS record; the monthly and six-monthly reports</td></tr>
<tr><td>Bacterial growth in the loop</td><td>Fever and chills during sessions, often in several patients</td><td>The monthly microbiological report; a cluster of fevers on one shift</td></tr>
<tr><td>Water supply disrupted after a typhoon or by rationing</td><td>Sessions cancelled or shortened</td><td>The medical director&rsquo;s contingency plan</td></tr>
</tbody></table></div>
<p><strong>Typhoons, brownouts and rationed water.</strong> In much of the country the threat to a child&rsquo;s sessions is less often a contaminant than a water system that stops: a typhoon cuts the supply, a brownout stops the RO plant, or rationing leaves the storage tank low. Ask each unit where your patients dialyze what its contingency plan is, which unit will take your child if it closes for several days, and how the family will be told. A child who misses two sessions after a storm comes back with a dangerous potassium and fluid overload, which is the emergency you can plan for in advance.</p>
{{key:The medical director owns the water, and the law says so. Before a child dialyzes in any unit, ask to see the latest microbiological and chemical reports and who signed them.}}
{{fig:apn25_c}}
"""),
        ("practice", "A child in an adult unit", "Making an adult unit safe for a child", """
<p><strong>Before the first session.</strong> A child should not arrive at an adult unit as a surprise. Visit or call the medical director and head nurse, and agree a short checklist:</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Why it matters for a child</th></tr></thead>
<tbody>
<tr><td>Bloodlines and dialyzer sized for the child, ordered and in stock</td><td>Circuit volume against the child&rsquo;s blood volume (Module 23)</td></tr>
<tr><td>Blood pressure cuffs in pediatric sizes; a scale accurate to the child&rsquo;s weight</td><td>A wrong cuff gives a wrong pressure; a weight error of half a kilogram is a large share of a small child&rsquo;s fluid goal</td></tr>
<tr><td>Pediatric resuscitation equipment (masks, airways, bag) and a weight-based emergency drug reference prepared by a pharmacist</td><td>Adult equipment and doses do not fit</td></tr>
<tr><td>A written pediatric order sheet that the adult template cannot overwrite</td><td>The commonest error is a covering nurse using the adult default</td></tr>
<tr><td>Consent from a parent or guardian and assent from the child, recorded</td><td>The child is a minor; assent respects the child and improves cooperation</td></tr>
<tr><td>A chaperone and a parent at the chair, and a chair placed where staff can see the child</td><td>A child in a row of adults is easy to overlook and may be frightened</td></tr>
<tr><td>Schedule that fits school, and something to do during sessions</td><td>Three sessions a week can end a school career if no one plans around it</td></tr>
<tr><td>The latest water reports, seen</td><td>DOH AO 2013-0003 obligations are the medical director&rsquo;s; your check is that they are current</td></tr>
</tbody></table></div>
<p><strong>The endorsement.</strong> Give the unit one page: the child&rsquo;s weight and target weight with the date set, the prescription with every number on it, what the first sessions look like and when they may step up, the stop-and-call rules below, and your number and your backup&rsquo;s. A unit that has to guess will guess the adult answer.</p>
<p><strong>Coverage is not a prescription.</strong> PhilHealth covers HD sessions under PhilHealth Circular (PC) 2024-0023.[[apn25_11]] The number of sessions a benefit pays for tells the family what is covered; it does not set how often or how long a child dialyzes. Confirm the rules on the date of service with the unit&rsquo;s PhilHealth staff, and write the clinical frequency from the child&rsquo;s needs.</p>
<p><strong>The adolescent among adults.</strong> A 15-year-old in a row of elderly adults sees, three times a week, what kidney failure can do to a body. Some adolescents are frightened by it; others decide it will never be them and stop coming. Ask the unit to seat the young person where staff can talk to them, to let them bring schoolwork or headphones, and to tell you after the first missed session, not the third. Ask the family about school directly: an afternoon shift that ends a school career is a clinical harm worth rearranging the unit&rsquo;s schedule for.</p>
<p><strong>Missed sessions.</strong> A child who misses a session is at risk of hyperkalemia and fluid overload before the next one. Agree with the unit that a missed session triggers a same-day call to the family, a potassium check if the child is unwell, and a call to you. The emergency response itself follows Module 4.</p>
<div class="tc-scene"><span class="tc-lab">At the adult unit, the template &middot; fictional</span><p>A month after Paeng&rsquo;s episode, the head nurse shows you the unit&rsquo;s new order sheet. Children&rsquo;s sheets are printed on yellow paper with &ldquo;Pediatric: do not change without the attending pediatric nephrologist&rdquo; across the top, and the adult template no longer opens for a patient under 18 in the unit&rsquo;s system.</p><p>You add the child&rsquo;s weight-based emergency drug sheet, signed by the hospital pharmacist, to the cart.</p><p class="tc-scene-take"><b>What this shows.</b> Safety in a mixed unit comes from changing the system so that the adult default cannot reach the child.</p></div>
{{call:<ul><li>Any order that differs from the written pediatric prescription: the nurse does not run it until the attending is reached</li><li>A child weighing more than the target weight by more than the agreed amount, before the session starts</li><li>A first or second session in a newly started child with any headache, vomiting or confusion</li><li>Any emergency in the table above</li><li>A failed water test or a unit closure that will interrupt the child&rsquo;s sessions</li><li>A missed session, or a family that says they cannot come</li></ul>}}
{{key:Write the child&rsquo;s prescription so it cannot be mistaken for an adult&rsquo;s, and agree in advance exactly what makes the nurse stop and call.}}
"""),
    ],
    "debrief": [
        "<p><strong>What is happening.</strong> Paeng is developing dialysis disequilibrium syndrome. He is in his third session, he started dialysis with a very high urea, and today&rsquo;s session was run on the adult template, so urea is falling faster than his brain can follow. Headache, vomiting, restlessness, slowed answers and a high pressure with a slow pulse fit rising intracranial pressure; a high pressure does not mean he can tolerate more. Tell the POD to stop the session now, or to reduce it to the minimum on your order, protect his airway, lay him on his side, check his glucose and oxygen saturation, and observe his conscious level closely. An antiemetic treats a symptom, not the cause. If he seizes or his level of consciousness falls, he needs a hospital with a pediatric intensive care unit, and you call the receiving physician yourself.</p>",
        "<p><strong>What else to exclude.</strong> The POD should look at the venous line for foam (air) or cherry-red blood (hemolysis), check every connection and the needle sites, check glucose for hypoglycemia, and record temperature. Hypertensive encephalopathy can look similar and may coexist; the treatment of the blood pressure follows your direction and the hospital&rsquo;s pediatric protocol. A seizure, focal signs or a falling consciousness level are reasons for urgent transfer, whatever the cause. Ask whether other patients on the shift are unwell: several sick patients at once points to the water or the dialysate, not to Paeng.</p>",
        "<p><strong>What has to change.</strong> The failure was a system that let the adult template overwrite a child&rsquo;s order. Before his next session, agree with the medical director that pediatric orders are printed separately and cannot be changed without you; write the next sessions with every number, and the rule for stepping up. Stock pediatric resuscitation equipment and a pharmacist-prepared, weight-based emergency drug reference on the cart. Ask to see the unit&rsquo;s latest microbiological and chemical water reports under DOH AO 2013-0003 and who signed them. Explain to his mother what happened, in plain words, and that it was preventable. Then plan the longer question: whether a 13-year-old is best served in this unit, and how soon he can be referred for transplant evaluation.</p>",
    ],
    "skills": {"title": 'HD emergencies, water safety, and children in adult HD units',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Writes first-session orders for a newly started, very uremic child with explicit step-up rules", False),
                         ("Leads a simulated chair emergency (air, hemolysis or disequilibrium), including the return-blood decision", False),
                         ("Reviews an adult unit&rsquo;s water reports against DOH AO 2013-0003 with the medical director", False),
                         ("Completes a pediatric readiness checklist and endorsement for an adult HD unit", False)],
               "placement": "Simulation or supervised practice"},
    "quiz": [
        ("A newly started 12-year-old develops headache, vomiting and restlessness in the first hour of his third session; blood pressure is high and pulse slow. What is the most likely diagnosis?",
         ["Intradialytic hypotension",
          "Dialysis disequilibrium syndrome",
          "Dialyzer reaction",
          "Air embolism"],
         1,
         "Early sessions, a very high starting urea and neurologic symptoms with a high pressure and slow pulse point to cerebral edema from the urea gradient. Prevention with limited first sessions matters most."),
        ("Foam appears in the venous line and the child suddenly becomes breathless. What should the nurse do with the blood in the circuit?",
         ["Return it quickly to restore volume",
          "Return it after rinsing the dialyzer",
          "Continue dialysis at a lower blood flow",
          "Clamp the venous line, stop the pump, and do not return the blood"],
         3,
         "Suspected air embolism means stopping the pump and clamping; blood is not returned. Lay the child on the left side, head down, and give oxygen."),
        ("Under DOH AO 2013-0003, who is responsible for the quality of water in a hemodialysis clinic?",
         ["The medical director",
          "The attending nephrologist of each patient",
          "The local government unit",
          "The water utility"],
         0,
         "The order makes the medical director responsible and requires documentation of that involvement, for example by initialing test results."),
        ("What did Hothi and colleagues find in children on HD?",
         ["The final relative blood volume at hour 4 predicted complications",
          "Blood pressure alone predicted complications",
          "A steeper fall in relative blood volume in the first hour and a change in heart rate were associated with complications",
          "Blood volume monitoring had no relationship to complications"],
         2,
         "In 74 retrospective records, early slope and heart rate change mattered; thresholds at hours 1 to 3 discriminated, but no hour-4 value did."),
        ("PhilHealth covers a set number of HD sessions under PC 2024-0023. How should that number be used?",
         ["As the child&rsquo;s prescribed frequency",
          "As information about coverage, with frequency set by the child&rsquo;s clinical needs",
          "As the maximum the attending may prescribe",
          "As the minimum the unit must deliver"],
         1,
         "Coverage is not a prescription. Confirm benefit rules on the date of service and write clinical frequency from the child&rsquo;s needs."),
    ],
    "terms": [("AAMI", "Association for the Advancement of Medical Instrumentation"), ("AO", "Administrative Order"),
              ("DDS", "Dialysis disequilibrium syndrome"), ("DOH", "Department of Health"), ("HD", "Hemodialysis"),
              ("HFSRB", "Health Facilities and Services Regulatory Bureau"), ("IDH", "Intradialytic hypotension"),
              ("PC", "PhilHealth Circular"), ("PCRRT", "Pediatric Continuous Renal Replacement Therapy (Workgroup)"),
              ("POD", "Physician on duty"), ("RO", "Reverse osmosis"), ("TDS", "Total dissolved solids")],
    "readings": [('dialysis-water-treatment-systems.html', 'Hemodialysis Water Treatment Systems: A Clinical & Engineering Reference for Dialysis Staff'),
                 ('hemodialysis-complications.html', 'Managing Complications of Hemodialysis'),
                 ('code-blue-acls-dialysis-unit.html', 'Efficient Handling of Code Blues & ACLS in a Dialysis Unit')],
    "calcs": ["calc-ufr-ceiling.html", "calc-plasma-volume.html", "calc-potassium-load.html",
              "calc-wts-self-assessment.html", "calc-bsa.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
