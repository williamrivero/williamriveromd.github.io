# -*- coding: utf-8 -*-
"""Physician on Duty, Module 10: The Lifeline II: Catheters.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a dialysis nurse, both masked, examining the dressing over a tunneled dialysis catheter on a seated patient's upper chest.",
    "objectives": [
        "Tell a tunneled catheter from a non-tunneled catheter, and explain why the difference matters.",
        "Inspect the exit site, the tunnel, and the external limbs before a catheter is used.",
        "Apply the steps of safe connection and disconnection, and explain what each prevents.",
        "Work through poor catheter flow step by step.",
        "Recognize catheter infection, air entry, bleeding, dislodgement, and an exposed cuff, and carry out the first actions.",
        "Explain why every catheter needs a written plan for its removal.",
    ],
    "big": """
{{plain:Think of a dialysis catheter as a door cut through the outside wall of a house, opening straight into the main hallway. Deliveries can start the same day, but whatever comes through it reaches every room within seconds. Safety depends on how the door is opened, how it is closed, and how soon the wall can be repaired.}}
<p>The picture has limits. A catheter is also a plastic tube lying inside a large vein, with its tip close to the heart. Blood clots on it, bacteria grow on it, and the vein around it scars. Those three processes explain most catheter problems.</p>
{{fig:access_types3|The three kinds of access. Module 9 covered the fistula and the graft. This module covers the catheter.}}
{{cards:Key terms for this module|Central venous catheter (CVC)::A tube placed in a large vein, with its tip in or near the heart. A dialysis CVC has two channels.|Lumen::One channel inside the catheter. The red (arterial) lumen draws blood out. The blue (venous) lumen returns it.|Tunneled catheter::A catheter that runs under the skin before it enters the vein. It has a cuff.|Cuff::A fabric band around a tunneled catheter. Tissue grows into it.|Exit site::The place where the catheter comes out through the skin.|Hub::The threaded end of each catheter limb, where the cap or the blood line attaches.|Lock::Fluid left inside each lumen between sessions to keep it from clotting.|Catheter-related bloodstream infection (CRBSI)::Bacteria or fungi in the blood that came from the catheter.}}
""",
    "case": {"title": "The catheter that would only push", "html": """
<p>Mrs. Lourdes Villanueva, 54, dialyzes on Tuesdays and Fridays through a tunneled catheter in her right internal jugular vein. It was placed five months ago &ldquo;until the fistula is ready.&rdquo; No fistula surgery has been scheduled.</p>
<p>On Friday morning the nurse, Jun, calls you to her chair. Saline flushes easily into the red lumen, but he cannot draw blood back from it. The blue lumen works both ways. The chart shows that the lines were reversed for the last two sessions, with a lower pump speed and repeated pressure alarms.</p>
<p>Jun offers two ideas: push harder with a small syringe, or reverse the lines again. Mrs. Villanueva mentions that she felt cold and shaky near the end of Tuesday&rsquo;s session and feverish that night. Her temperature now is 37.9&deg;C. There is a small crust at the exit site.</p>
""", "questions": ["What explains a lumen that accepts a flush but will not give blood back?",
                  "Which bedside steps are safe to try now, and which are not?",
                  "Which two other findings in this history must reach the attending nephrologist today?"]},
    "sections": [
        ("types", "Two kinds of catheter", "Two kinds of catheter, and where the tip sits", """
<p>A dialysis machine needs a large, steady blood flow. A catheter supplies it from a central vein close to the heart. A dialysis catheter has two lumens. By convention the red limb draws blood out to the machine and the blue limb returns it.[[daugirdas2015]]</p>
{{fig:pod10_types}}
<p>The two kinds differ in what lies between the skin and the vein. A non-tunneled catheter passes straight through the skin into the vein. Skin bacteria have a short path along its outer surface, and only a stitch holds it. A tunneled catheter travels under the skin first, and a fabric cuff sits inside that tunnel. Over the weeks after insertion, tissue grows into the cuff. The cuff then anchors the catheter and acts as a barrier between the skin and the vein.[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Non-tunneled catheter</th><th>Tunneled, cuffed catheter</th></tr></thead>
<tbody>
<tr><td>What you see</td><td>Enters at the neck or groin, held by a stitch</td><td>Exits on the upper chest; a small scar on the neck marks where it enters the vein</td></tr>
<tr><td>Cuff</td><td>None</td><td>Present, hidden inside the tunnel</td></tr>
<tr><td>Intended use</td><td>Days, for urgent starts</td><td>Weeks to months, as a bridge or when no other access is possible</td></tr>
</tbody></table></div>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) guideline prefers tunneled catheters because the infection risk is lower. It considers it reasonable to limit a non-tunneled catheter to under two weeks, or to the period set by facility policy. Both statements are expert opinion, not trial results.[[kdoqi_va2019]]</p>
<p>The tip matters as much as the entry point. The tip of a tunneled catheter is meant to lie in or near the right atrium, where blood flow is high.[[daugirdas2015]] Bacteria or air that enter the catheter therefore arrive at the heart at once. A catheter that has slipped outward may have its tip in a narrower vein, where it flows poorly.</p>
{{key:Learn three things about each catheter: which kind it is, when it was placed, and what the plan is for replacing it.}}
"""),
        ("inspect", "Exit site and tunnel", "Inspecting the exit site, the tunnel, and the limbs", """
<p>A catheter is examined before every connection, not only when there is a complaint. KDOQI considers a physical check of the access before each use reasonable practice.[[kdoqi_va2019]] An infection found before connection is a local problem. The same infection found after the pump has started may already have been flushed into the bloodstream.</p>
{{fig:pod10_exit}}
<p>The nurse removes the old dressing with clean technique. Then ask, look, and feel, in the same order each time.</p>
{{flow:Catheter check before connection|Ask::Fever, chills, pain at the catheter, or a wet or loose dressing since the last session.|Look at the exit site::Redness, swelling, crust, pus, or bleeding. On a non-tunneled catheter, check that the stitch is intact.|Look for the cuff::It should not be visible. Compare the length of catheter outside the skin with the last recorded length.|Feel the tunnel::Press gently from the exit site toward the neck. Tenderness, warmth, or a firm cord is abnormal.|Check the limbs::Both clamps closed, both caps on, no cracks, no kinks.|Look at the patient::Swelling of the face, neck, or arm on the catheter side suggests a narrowed central vein.}}
{{fig:pod10_exitcompare}}
<p>The Infectious Diseases Society of America (IDSA) separates two local infections by distance. An exit-site infection is redness, hardening, or tenderness within 2 centimeters of the exit site, with or without pus. A tunnel infection extends more than 2 centimeters from the exit site along the tunnel.[[idsa_crbsi2009]] A tunnel infection lies deeper than a topical treatment can reach, and closer to the vein.</p>
<p>A healed exit site is dry and painless. Pus is never normal.</p>
{{call:Stop and call the attending nephrologist before the catheter is used when the cuff is visible, when the catheter looks longer than it was, or when the stitch of a non-tunneled catheter has come loose. Secure the catheter with tape and a sterile dressing, with both clamps closed and both caps on. Do not push it back in, and do not use it until the nephrologist has decided.}}
<p>An exposed cuff means that the catheter has moved outward. The anchor and the barrier are lost, and the tip may have moved. The part that has been outside is no longer sterile, which is why it is never pushed back. Whether the catheter can be used is the nephrologist&rsquo;s decision.</p>
"""),
        ("hub", "Connecting and disconnecting", "Safe connection and disconnection, and what each step is for", """
<p>During connection and disconnection the hub is open for a few seconds. An open hub is a direct path to the right atrium for bacteria and for air.</p>
{{fig:pod10_hub}}
<p><strong>Bacteria.</strong> Organisms reach the blood by two routes. They can track along the outside of the catheter from the skin, which the tunnel and cuff are designed to slow. They can also enter the inside of the catheter through the hub, carried by hands, breath, or a contaminated cap. Once on the plastic, they can form a layer called a biofilm. A biofilm helps organisms withstand the body&rsquo;s defenses and makes them less susceptible to antibiotics.[[cdc_bsi2011]]</p>
<p><strong>Air.</strong> Pressure in the central veins is low. During a deep breath in it can fall below the pressure of room air, especially in a patient who is sitting up or who is volume depleted.[[mccarthy2016]] If a hub and its clamp are both open, air can be drawn into the vein. A review of hemodialysis emergencies lists uncapped catheters and failure to clamp among the causes of air embolism.[[greenberg2021]]</p>
<p>The United States Centers for Disease Control and Prevention (CDC) publishes a hub protocol for dialysis catheters. The steps below follow its order.[[cdc_scrubhub]] Your unit&rsquo;s procedure sets the antiseptic and the details.</p>
{{flow:Opening a catheter hub safely|Prepare::Masks, hand hygiene, and new clean gloves.|Clamp first::Confirm that the clamp is closed before the cap comes off. This step keeps air out.|Scrub::Scrub the threads and the end of the hub with antiseptic, using a new pad for each hub. This removes bacteria before they are pushed inside.|Let it dry::Antiseptic needs contact time. A scrubbed hub must not touch clothes, the chair, or the bed.|Attach at once::Connect the sterile syringe or blood line. An uncapped catheter is never left unattended.|Finish clean::Remove gloves and perform hand hygiene.}}
<p>Disconnection follows the same logic: clamp, disconnect, scrub the hub, attach a new sterile cap, and confirm that the clamp is still closed.[[cdc_scrubhub]] The lock placed in each lumen is part of the prescription.</p>
{{fig:catheter_safety}}
<h3>What the evidence shows</h3>
<p>In a cluster-randomized quality improvement study of 211 matched pairs of facilities, one group adopted chlorhexidine with alcohol for exit-site care and alcohol pads to scrub the hubs. That group had 0.81 positive blood cultures per 1,000 catheter-days, compared with 1.04 under usual care.[[rosenblum2014]]</p>
<p>In a CDC collaborative of 17 volunteer facilities, a package of catheter care, staff training, audits, and feedback was followed by a 54% fall in modeled access-related bloodstream infection rates.[[patel2013]] The project had no control group, so the fall cannot be credited to the package with certainty. Some elements rest on weaker ground. The CDC protocol notes that data supporting masks are lacking, though KDOQI considers them reasonable.[[cdc_scrubhub]][[kdoqi_va2019]]</p>
{{key:A dialysis catheter is not a line for routine blood draws, intravenous fluids, or medicines outside dialysis. Each extra opening is one more chance for bacteria and air to enter.}}
"""),
        ("flow", "Poor flow", "Poor flow, step by step", """
<p>KDOQI defines catheter dysfunction as failure to maintain the prescribed blood flow without lengthening the treatment.[[kdoqi_va2019]] At the chair you see arterial pressure alarms, a reduced pump speed, or a lumen that will not give blood back.</p>
<h3>Why a catheter pushes but will not pull</h3>
<p>The two directions of flow are not equal. The venous lumen pushes blood out, and pushing tends to clear its opening. The arterial lumen draws blood in by suction, and suction pulls nearby material over the opening. That material may be the vein wall, a small clot, or a fibrin sheath. A fibrin sheath is a sleeve of protein and cells that grows along the outside of a catheter over weeks.[[daugirdas2015]]</p>
{{fig:pod10_ballvalve}}
<p>Timing suggests the cause. Poor flow in the first days after insertion is usually mechanical: a kink, a tight stitch, or a tip in the wrong place. Poor flow after weeks of good function more often comes from clot or a fibrin sheath.[[daugirdas2015]]</p>
{{flow:Poor catheter flow, in order|Look at the patient::Check blood pressure, breathing, and temperature. Ask about chills. A failing catheter may also be infected.|Look at the outside::Clamps fully open, no kink under the dressing, no tight stitch, blood lines not twisted.|Check the length::If the cuff shows or the catheter looks longer, stop and call.|Change position::Ask the patient to cough, turn the head, or lie flatter. Flow that returns points to a tip resting against the vein wall.|Flush per protocol::A trained dialysis nurse may flush the lumen with saline, following the unit&rsquo;s nursing procedure. Nobody forces a flush against resistance. Tell the attending nephrologist that it was needed.|Lower the pump speed per protocol::A slower speed needs less suction, but it also delivers less dialysis. Blood flow is part of the prescription, so the attending nephrologist is informed.|Reverse the lines only if protocol allows::Reversal is a nursing procedure and a temporary measure to finish today&rsquo;s session. It increases recirculation, so the attending nephrologist is informed each time.|Call and record::Report to the attending nephrologist the flow achieved, each step tried, and whether the lines were reversed. Write the same in the treatment record.}}
<p>Forcing a flush is unsafe. For the same push of the thumb, a narrow syringe produces a higher pressure than a wide one. A review of catheter flushing, written about venous catheters other than dialysis catheters, states that a small syringe or a hard push against resistance increases the risk of damage to the catheter.[[goossens2015]] Whatever is forced out of a blocked lumen also enters the bloodstream. Syringe size and flushing technique are set by your unit&rsquo;s nursing procedure.</p>
<p>Reversing the lines often restores flow, because the blocked lumen now pushes. It has a cost. The intake now lies downstream of the return, so some cleaned blood is drawn straight back into the machine. This is called recirculation. In a prospective study of 102 patients with tunneled catheters, recirculation above 10% was found in 3% with the lines in the usual position and in 86% with the lines reversed. Among patients usually run reversed, about half could be run in the usual position. In them, measured clearance was no better with the lines reversed, despite a higher pump speed.[[pannu2006]] This was one center, and clearance was measured in a subgroup. KDOQI describes reversal as a temporary respite that allows a session to be completed.[[kdoqi_va2019]] Reversal does not treat the cause, and repeated reversal is a reason to call.</p>
<p>KDOQI considers a conservative bedside approach reasonable as the first step. For clot, it conditionally recommends a clot-dissolving (thrombolytic) medicine placed inside each lumen.[[kdoqi_va2019]] In a randomized trial of 225 patients with new catheters, a weekly thrombolytic lock reduced catheter malfunction and bacteremia compared with heparin locks alone.[[hemmelgarn2011]] Thrombolytic locks, imaging, and catheter exchange are ordered by the nephrologist per protocol. KDOQI regards replacement at a new site as the last resort.[[kdoqi_va2019]]</p>
{{call:Call the attending nephrologist when a catheter cannot deliver the prescribed blood flow, when the lines had to be reversed, or when it has flowed poorly at more than one session. A slowed or shortened session delivers less dialysis, and the response belongs to the prescription.}}
"""),
        ("infection", "Catheter infection", "Recognizing catheter infection and taking the first steps", """
<p>A catheter gives bacteria a surface to live on and a route to the blood. In a systematic review of 62 cohort studies with 586,337 participants, patients using catheters had a higher risk of fatal infection than patients using fistulas (risk ratio 2.12).[[ravani2013]] The studies were observational, and the authors judged the risk of selection bias to be high, since sicker patients are more likely to have catheters.</p>
{{fig:dai_clinic|How dialysis access infection presents.}}
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>What you find</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Exit-site infection</td><td>Redness, tenderness, crust, or pus close to the exit site. The patient may feel well</td><td>Local, but it can spread along the catheter</td></tr>
<tr><td>Tunnel infection</td><td>Tenderness, redness, or hardening along the tunnel</td><td>Deep to the skin and next to the vein</td></tr>
<tr><td>Bloodstream infection</td><td>Fever or chills, often during dialysis. Low blood pressure or confusion. The exit site may look normal</td><td>Can seed the heart valves, spine, and joints</td></tr>
</tbody></table></div>
<p>A normal exit site does not rule out a bloodstream infection, because the bacteria may live inside the lumen. Chills that begin after dialysis starts are typical, because the pump washes organisms from the catheter into the circulation. Elderly and diabetic patients may have no fever, only low blood pressure or confusion.</p>
{{call:Fever or chills in a patient with a catheter is a catheter-related bloodstream infection until proven otherwise. Examine the patient, start your unit&rsquo;s protocol, and call the attending nephrologist at once. Do not send the patient home to &ldquo;observe.&rdquo;}}
{{flow:First steps for suspected catheter infection|Assess::Temperature, blood pressure, heart rate, mental state, exit site, and tunnel. Look for another source of infection.|Call early::Use the structured report from Module 1. Say plainly that the patient has a catheter.|Culture first::Draw blood cultures per protocol before the first antibiotic. Swab any pus.|Protect the veins::For a peripheral sample, use a hand vein, not a forearm vein that a future fistula will need.|Give antibiotics as ordered::The choice comes from the nephrologist and the unit protocol.|Decide where the patient goes::An unstable patient needs the hospital.}}
<p>The order comes from guidelines. IDSA gives its strongest grade to obtaining blood cultures before antibiotics. It advises taking peripheral samples from vessels that a fistula will not need, such as hand veins.[[idsa_crbsi2009]] KDOQI also considers cultures before antibiotics reasonable.[[kdoqi_va2019]]</p>
<p>What happens to the catheter is the nephrologist&rsquo;s decision. Options include removal, exchange over a wire, and an antibiotic lock. For certain organisms the catheter is always removed, as the nephrologist and infectious disease guidance direct.[[idsa_crbsi2009]]</p>
{{fig:dai_prevention|Preventing dialysis access infection.}}
"""),
        ("exitplan", "The exit plan", "Why every catheter needs an exit plan", """
<p>In the systematic review above, patients using catheters also had a higher risk of death from any cause than patients using fistulas (risk ratio 1.53).[[ravani2013]] These are associations, and part of the difference reflects who receives a catheter.</p>
<p>Three harms accumulate with time. Each week adds exposure to infection. Clot and fibrin reduce flow, which reduces the dialysis delivered. And the catheter lies against the wall of the central vein, which can scar and narrow over time. Catheters in the neck and chest veins are a leading cause of this narrowing, called central vein stenosis, particularly after long use or several catheters. It can cause swelling of the arm, face, or neck, and it threatens a fistula or graft on that side.[[agarwal2013]][[kdoqi_va2019]]</p>
<p>KDOQI therefore suggests a fistula or graft over a catheter for most patients, and suggests that most patients who start with a catheter convert when possible. It grades the supporting evidence as very low to moderate.[[kdoqi_va2019]] It accepts a tunneled catheter while a fistula matures, and as long-term access for selected patients with no better option. It asks that each patient have a documented, regularly reviewed access plan.[[kdoqi_va2019]] The CDC lists catheter reduction among its core practices for preventing bloodstream infection.[[cdc_dialysis_bsi2024]]</p>
{{flow:From catheter to fistula or graft|Urgent start::A catheter is placed because dialysis cannot wait.|Refer::The nephrologist arranges vein mapping and a surgical opinion.|Create::The surgeon creates a fistula or places a graft.|Mature::The fistula develops over weeks. The catheter stays in use and is cared for at every session.|Cannulate::The team begins using the new access.|Remove::The catheter comes out once the new access works reliably.}}
<p>You do not write this plan, but you can notice when it has stalled. Write the insertion date and the plan in your note, and tell the attending nephrologist about any catheter with no plan.</p>
{{key:Keep needles and blood pressure cuffs away from the arm chosen for a fistula. Module 9 explained why those veins must be saved.}}
"""),
        ("emergencies", "Catheter emergencies", "Catheter emergencies and the first actions", """
<p>Catheter emergencies are uncommon. Each has a first action that does not wait for an order. Start it per your unit&rsquo;s protocol while a colleague calls the attending nephrologist.</p>
<div class="table-wrap"><table>
<thead><tr><th>Emergency</th><th>What you see</th><th>First actions</th></tr></thead>
<tbody>
<tr><td>Air entry</td><td>An open, unclamped hub or a disconnected line. Sudden cough, breathlessness, chest pain, low blood pressure, confusion, or collapse</td><td>Clamp the catheter. Stop the blood pump. Do not return the blood. Give oxygen. Position the patient per protocol</td></tr>
<tr><td>Bleeding from a limb or hub</td><td>Blood running from a missing cap, a loose connection, or a cracked limb</td><td>Clamp between the leak and the patient. Replace the cap with sterile technique</td></tr>
<tr><td>Bleeding around the catheter</td><td>Blood soaking the dressing at the exit site</td><td>Apply firm, direct pressure with sterile gauze. Check blood pressure</td></tr>
<tr><td>Catheter pulled partly out</td><td>Cuff visible, or a longer length outside the skin</td><td>Do not push it back. Do not use it. Secure it with tape and a sterile dressing</td></tr>
<tr><td>Catheter pulled completely out</td><td>Catheter in the patient&rsquo;s hand or on the floor</td><td>Lay the patient flat. Press firmly over the exit site and over the point where the catheter entered the vein. Cover with an airtight dressing. Call for help</td></tr>
</tbody></table></div>
<h3>Air</h3>
<p>Air that enters a central vein travels to the right side of the heart and the lung arteries. There it can block blood flow and cause cardiac arrest. In a patient who is sitting up, air can also rise through the jugular vein toward the brain. A published review cites 100 to 300 milliliters as a volume that may be fatal in an adult.[[greenberg2021]]</p>
<p>The same review advises stopping dialysis, not returning the blood in the circuit, giving oxygen, and supporting the circulation. For suspected venous air embolism it recommends lying the patient on the left side. It warns that a head-down position may worsen brain swelling when air has reached the brain.[[greenberg2021]] Positioning advice is not uniform across sources. It rests on physiological reasoning and case experience, not on trials. Follow your unit&rsquo;s protocol.</p>
<h3>Bleeding and dislodgement</h3>
<p>The review lists uncapped ports, disconnection from the circuit, and accidental removal as catheter-related causes of serious bleeding, and it advises continuous direct pressure.[[greenberg2021]] After a tunneled catheter comes out, the hole in the vein lies at the base of the neck, several centimeters from the exit site. Press on both places. The patient lies flat and the dressing is airtight because air can enter through the empty track.[[mccarthy2016]]</p>
<p>Bleeding around the exit site is most common soon after insertion and after heparin. Heparin is part of the prescription, so report the bleeding before the next dose.</p>
{{call:Stop and call for bleeding around a catheter that continues despite firm pressure, for any bleeding with a fall in blood pressure, and for any suspected air entry. Start the first actions while a colleague makes the call.}}
{{flow:Call card: catheter emergency|Recognize::An open or disconnected hub, blood on the dressing or the floor, a visible cuff, a catheter out of place, or fever and chills.|First 2 minutes::Clamp the catheter and stop the blood pump. Press on any bleeding point. Give oxygen if the patient is breathless or collapsed. Check airway, breathing, pulse, and blood pressure.|Stop dialysis?::Yes for air entry, dislodgement, uncontrolled bleeding, or an unstable patient. For poor flow or suspected infection in a stable patient, follow protocol and the nephrologist&rsquo;s advice.|Return the blood?::Do NOT return blood if air may be in the circuit or may have entered the patient, if the circuit is clotted, or if the catheter is damaged, pulled out, or showing its cuff. Otherwise return it per protocol and as the attending nephrologist advises.|Call::The attending nephrologist. Activate the emergency response for collapse or suspected air embolism.|Write::Time, findings, catheter length outside the skin, estimated blood loss, actions, the patient&rsquo;s response, and who was informed.}}
"""),
    ],
    "debrief": ["""
<p><strong>What explains a lumen that accepts a flush but will not give blood back?</strong> Something covers the opening of the red lumen only when suction is applied. Pushing saline lifts it away, and pulling draws it back. After five months of use, a fibrin sheath or a small clot at the tip is most likely. A tip resting against the vein wall is the other possibility.</p>
<p><strong>Which bedside steps are safe, and which are not?</strong> The safe steps are the ordered ones. Examine Mrs. Villanueva first. Check the clamps, the limbs, and the length of catheter outside the skin. Ask her to cough and change position. A saline flush by the nurse is allowed if your unit&rsquo;s nursing procedure describes it. Pushing hard with a small syringe is not safe, because the pressure can damage the catheter and force material into her circulation. Reversing the lines a third time without telling the attending nephrologist is also wrong. Reversal increases recirculation, and her pump speed was lowered, so she has probably received less dialysis than prescribed for a week, on a twice-weekly schedule with little margin.</p>
<p><strong>Which two other findings must reach the nephrologist today?</strong> The first is the chills on Tuesday, the fever that night, and today&rsquo;s temperature. Chills on dialysis in a patient with a catheter suggest a bloodstream infection until proven otherwise. Blood cultures come before any antibiotic, per protocol, and the crusted exit site needs a careful look. The second is that this catheter has no exit plan. It was placed as a bridge, and five months later no surgery is booked.</p>
<p>One call covers all three. Whether she dialyzes today, and how, is the nephrologist&rsquo;s decision.</p>
"""],
    "skills": {"title": "Exit-site inspection and hub handling",
               "intro": "Your preceptor observes you examine three catheters before connection, and observes you supervise one connection and one disconnection performed by a dialysis nurse.",
               "items": [
                   ("States the type of catheter, its site, the insertion date, and the documented access plan.", False),
                   ("Asks about fever, chills, pain at the catheter, and whether the dressing became wet or loose.", True),
                   ("Confirms that the patient and staff wear masks, and performs hand hygiene before touching the dressing.", True),
                   ("Inspects the exit site for redness, swelling, crust, pus, and bleeding.", True),
                   ("Checks for a visible cuff and compares the external catheter length with the last record.", True),
                   ("Palpates the tunnel from the exit site toward the neck for tenderness, warmth, and hardening.", False),
                   ("Inspects both limbs for cracks and kinks, and confirms that both clamps are closed and both caps are in place.", True),
                   ("Looks for swelling of the face, neck, or arm on the catheter side.", False),
                   ("Confirms that the clamp is closed before each cap or blood line is removed.", True),
                   ("Confirms that each hub is scrubbed with a new antiseptic pad and allowed to dry.", True),
                   ("Confirms that an open hub is never left unattended and does not touch a non-sterile surface.", True),
                   ("At disconnection, confirms new sterile caps, closed clamps, and the lock ordered for that patient.", False),
                   ("States which findings would stop the connection and prompt a call to the attending nephrologist.", True),
                   ("Records the findings, including the external catheter length, in the treatment record.", False),
               ],
               "placement": "For two weeks, list every catheter in the unit during your shifts with its type, insertion date, and access plan. Discuss with your preceptor any catheter that has no plan."},
    "quiz": [
        ("What does the cuff on a tunneled catheter do?",
         ["Measures pressure in the vein", "Releases antibiotic into the tunnel",
          "Anchors the catheter and helps block bacteria once tissue grows into it", "Prevents clot at the tip"], 2,
         "The cuff sits inside the tunnel. Ingrown tissue holds the catheter and forms a barrier between skin and vein."),
        ("The chart shows that a non-tunneled neck catheter was inserted five weeks ago. It flows well. What should you do?",
         ["Report it to the attending nephrologist", "Nothing, because it works",
          "Remove it after the session", "Ask the nurse to add a stitch"], 0,
         "Non-tunneled catheters are intended for short use because infection risk rises with time. The plan belongs to the nephrologist."),
        ("Why is a catheter examined before every connection?",
         ["The dressing must be changed by a physician", "An infection found before connection is still local",
          "Catheters move at every session", "To choose the pump speed"], 1,
         "Once the pump starts, organisms at the exit site or in the lumen can be flushed into the blood."),
        ("Before connection, a ring of white fabric is visible at the exit site of a tunneled catheter. What comes next?",
         ["Push the catheter in until the fabric is hidden", "Start at a low pump speed",
          "Trim the fabric and redress", "Secure the catheter, do not use it, and call the attending nephrologist"], 3,
         "A visible cuff means the catheter has moved outward. The exposed part is not sterile and the tip may be out of position."),
        ("Which step, done before a cap is removed, protects most directly against air entry?",
         ["Scrubbing the hub", "Wearing a mask", "Confirming that the clamp is closed", "Changing gloves"], 2,
         "Central venous pressure can fall below room pressure during a breath in. Scrubbing and masks protect against bacteria."),
        ("A ward nurse asks to run an overnight antibiotic through a patient&rsquo;s dialysis catheter because the veins are difficult. What is the best answer?",
         ["Agree, because the catheter is already in place", "Agree, if the blue lumen is used",
          "Decline routine use and refer the request to the attending nephrologist", "Agree, if gloves are worn"], 2,
         "Each extra opening of the hub adds risk of infection and air entry."),
        ("What did the cluster-randomized study of catheter care compare?",
         ["Chlorhexidine exit-site care plus hub scrubbing, against usual care", "Tunneled against non-tunneled catheters",
          "Antibiotic locks against heparin locks", "Masks against no masks"], 0,
         "Intervention facilities had fewer positive blood cultures per 1,000 catheter-days."),
        ("Why can a lumen accept a saline flush and still fail to give blood back?",
         ["The saline is too cold", "Suction pulls the vein wall, a clot, or a fibrin sheath over the opening",
          "The pump is running backward", "The blood pressure is too high"], 1,
         "Pushing lifts the obstruction away and pulling draws it back, like a flap."),
        ("A tunneled catheter placed three days ago flows poorly from the first session. Which cause is most likely?",
         ["A fibrin sheath", "Central vein scarring", "Biofilm in the lumen", "A kink, a tight stitch, or a poorly placed tip"], 3,
         "Early poor flow is usually mechanical. Clot and fibrin sheath are typical after weeks of good function."),
        ("A lumen resists a saline flush. Why should nobody push harder with a small syringe?",
         ["Small syringes are not sterile", "High pressure can damage the catheter and force material into the bloodstream",
          "It dilutes the lock", "It triggers an alarm"], 1,
         "For the same push, a small syringe generates a higher pressure. Stop and call the attending nephrologist."),
        ("In the study of 102 patients with tunneled catheters, what happened when the blood lines were reversed?",
         ["Recirculation was rare in both positions", "Clearance improved",
          "Significant recirculation became common, with no gain in clearance", "Infection was prevented"], 2,
         "Recirculation above 10% was found in 86% with lines reversed and 3% in the usual position."),
        ("Forty minutes into dialysis, a 67-year-old man with a tunneled catheter has shaking chills. His exit site is clean. How do you interpret this?",
         ["A cold room", "A clean exit site rules out catheter infection",
          "Anxiety", "A catheter-related bloodstream infection until proven otherwise"], 3,
         "Bacteria inside the lumen are washed into the blood when the pump runs. The exit site may look normal."),
        ("For the same patient, what should happen before the first antibiotic?",
         ["Blood cultures per protocol, and a call to the attending nephrologist", "Removal of the catheter at the chair",
          "Discharge home with advice to return", "A forearm cannula for fluids"], 0,
         "Guidelines give priority to cultures before antibiotics. Forearm veins are saved for a future fistula."),
        ("At disconnection a hub is found open and unclamped. The seated patient coughs, becomes breathless, and her blood pressure falls. What do you do first?",
         ["Return the blood quickly", "Sit her more upright and observe",
          "Clamp the catheter, stop the pump, do not return the blood, give oxygen, and call for help", "Flush the catheter"], 2,
         "This is suspected air entry. Returning blood or flushing could push more air into the patient."),
        ("A patient eight months into catheter dialysis says a fistula operation is unnecessary because the catheter works. What is the most useful response?",
         ["Agree", "Explain that the risks grow with time, and tell the attending nephrologist that the plan has stalled",
          "Promise removal next week", "Schedule the surgery yourself"], 1,
         "Catheter use is associated with more infection and death than fistula use. The access plan belongs to the nephrologist."),
    ],
    "terms": [("Central venous catheter", "A tube placed in a large vein with its tip in or near the heart."),
              ("Tunneled catheter", "A catheter that runs under the skin before entering the vein and carries a cuff."),
              ("Cuff", "A fabric band on a tunneled catheter that tissue grows into, anchoring the catheter."),
              ("Exit site", "The place where the catheter comes out through the skin."),
              ("Hub", "The threaded end of a catheter limb where the cap or blood line attaches."),
              ("Lock", "Fluid left in each catheter lumen between sessions to prevent clotting."),
              ("Fibrin sheath", "A sleeve of protein and cells that grows along the outside of a catheter and can block its openings."),
              ("Recirculation", "Cleaned blood drawn straight back into the machine instead of mixing with the patient&rsquo;s circulation."),
              ("Catheter-related bloodstream infection", "Bacteria or fungi in the blood that came from the catheter."),
              ("Air embolism", "Air in the bloodstream that blocks blood flow in the heart, lungs, or brain.")],
    "readings": [("dialysis-access-infection.html", "How access infections are prevented, recognized, and treated."),
                 ("dialysis-access-care.html", "Daily care of a catheter, fistula, or graft, written for patients."),
                 ("hemodialysis-access-lifeline.html", "Why a fistula or graft is the long-term goal.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
