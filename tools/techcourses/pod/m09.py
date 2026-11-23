# -*- coding: utf-8 -*-
"""Physician on Duty, Module 09: The Lifeline I: Fistulas and Grafts.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician resting two fingers on a patient's forearm fistula while listening with a stethoscope before a dialysis session.",
    "objectives": [
        "Tell an arteriovenous fistula from an arteriovenous graft at the bedside, and explain why the difference matters.",
        "Perform a look, listen, and feel examination, with the arm elevation and pulse augmentation tests.",
        "Recognize the findings of narrowing, clotting, infection, an aneurysm at risk, and poor blood supply to the hand.",
        "Decide whether an access is safe to needle today, and state what to report.",
        "Control bleeding from a needle site and give the first response to a ruptured access.",
        "State what must never be done to an access arm, and explain the reason for each rule.",
    ],
    "big": """
{{plain:Picture a plumber who joins a high-pressure water main straight to a soft garden hose. Water now rushes through the hose all day, and a hand resting on it feels a steady hum. If the hose is pinched farther along, the part before the pinch turns hard and thumps with every surge. If the flow stops, the hose goes quiet. A fistula or graft is that hose. Your fingers and your stethoscope can tell you in about a minute whether it is flowing, pinched, or silent.}}
<p>The picture has limits. An access is living tissue, or a tube surrounded by living tissue. It does not kink. It narrows slowly as its wall thickens from the inside. It can clot, become infected, or thin until it bleeds. Each problem has a bedside sign that you can find before a needle goes in.</p>
<p>Patients call the access their lifeline, because the veins for making a new one are limited.</p>
{{cards:Key terms for this module|Vascular access::The route by which blood leaves the body for dialysis and returns to it.|Arteriovenous fistula (AVF)::A surgical join between an artery and the patient&rsquo;s own vein. The vein enlarges and is used for needling.|Arteriovenous graft (AVG)::A tube of synthetic material placed under the skin to connect an artery to a vein. The tube is used for needling.|Anastomosis::The surgical join between two vessels, or between a vessel and a graft.|Thrill::A fine vibration felt with the fingers over a flowing access.|Bruit::The rushing sound of the same flow, heard with a stethoscope.|Stenosis::A narrowing inside a vessel or graft.|Thrombosis::A clot that blocks the access.}}
""",
    "case": {"title": "The thrill is gone", "html": """
<p>Mrs. Lourdes Bautista, 64, has dialyzed twice a week for three years through a fistula in her left upper arm. Her last session was on Friday. It is now Tuesday morning. She tells the nurse, Jun Villanueva, that the &ldquo;buzz&rdquo; in her arm stopped on Sunday evening. She did not think it was urgent, because nothing hurt.</p>
<p>Jun feels the arm and finds no thrill. He asks you to confirm before anyone picks up a needle. In the treatment record you read two notes from last week: &ldquo;venous pressure higher than usual&rdquo; and &ldquo;needle sites bled longer than usual after the session.&rdquo; Mrs. Bautista is 3.4 kilograms above her dry weight. A senior technician offers to &ldquo;try one needle near the scar and see if blood comes.&rdquo;</p>
""", "questions": ["What do you examine, and what do you expect to find?",
                  "Should anyone needle this fistula today?",
                  "Whom do you call, what do you say, and what else does Mrs. Bautista need today?"]},
    "sections": [
        ("anatomy", "Fistula or graft", "Fistula or graft: two ways to join an artery to a vein", """
<p>Module 1 noted that a dialysis machine moves about 300 milliliters of blood a minute. An ordinary arm vein cannot supply that. A surgeon therefore joins an artery to a vein, so that arterial blood takes a shortcut into the vein.</p>
<p>In an arteriovenous fistula (AVF), the artery is joined to the patient&rsquo;s own vein. Over the following weeks to months the vein widens and its wall thickens under the new flow. This process is called maturation. In an arteriovenous graft (AVG), a synthetic tube bridges the artery and the vein, and the needles go into the tube.[[lok2020]]</p>
{{fig:access_types3|The three kinds of access. This module covers the fistula and the graft. Module 10 covers the catheter.}}
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Fistula</th><th>Graft</th></tr></thead>
<tbody>
<tr><td>What you needle</td><td>The patient&rsquo;s own enlarged vein</td><td>A synthetic tube under the skin</td></tr>
<tr><td>How it looks and feels</td><td>A soft, compressible vein, often uneven in width</td><td>A uniform tube, straight or looped, firmer than a vein</td></tr>
<tr><td>Time before first use</td><td>Weeks to months, and some never mature</td><td>Usually sooner, as the surgeon advises</td></tr>
<tr><td>Usual site of narrowing</td><td>Near the join, or along the vein that drains it</td><td>Where the graft meets the vein</td></tr>
<tr><td>Infection</td><td>Less common</td><td>More common, and seldom cured by antibiotics alone</td></tr>
<tr><td>Arm elevation test</td><td>Useful</td><td>Not useful, because a graft is a firm tube that does not flatten</td></tr>
</tbody></table></div>
<p>Two terms describe the direction of flow. Inflow is the artery and the join. Outflow is the vein that carries blood back toward the heart. In a looped graft the direction is not obvious from the skin, so read the access diagram in the chart.</p>
<h3>What the evidence says about the choice</h3>
<p>A systematic review pooled 62 cohort studies with 586,337 participants. Compared with patients who used a fistula, patients who used a graft had a higher risk of death (risk ratio 1.18) and of fatal infection (risk ratio 1.36). Patients who used a catheter had the highest risks.[[ravani2013]] The authors rated the risk of selection bias as high. Healthier patients are more likely to receive a fistula, so these figures show an association only.</p>
<p>A fistula is also not a guaranteed success. In a meta-analysis of 7,393 fistulas, 23% failed before they could be used, although the studies defined failure in different ways.[[aljaishi2014]] The attending nephrologist and the surgeon decide when a new access is ready for its first needle.</p>
{{key:Before you examine any access, find three facts in the chart: fistula or graft, when it was created, and which way the blood flows.}}
"""),
        ("exam", "Look, listen, feel", "Look, listen, feel: the one-minute examination", """
<p>Blood in a working access flows fast, in systole and in diastole, because the vein offers little resistance. Fast flow through the join makes the wall vibrate. Your fingers feel that vibration as a thrill, and your stethoscope hears it as a bruit.</p>
{{fig:look_listen_feel}}
<p>Looking finds problems of the skin, the wall, and the hand. Listening and feeling test the flow.[[lok2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Healthy access</th><th>Findings that need a closer look</th></tr></thead>
<tbody>
<tr><td>Look</td><td>Even skin, healed needle marks spread along the access, both arms the same size</td><td>Redness, swelling, pus, a scab that does not heal, a bulge with thin or shiny skin, a swollen arm, veins visible on the chest or shoulder, a pale or dusky hand</td></tr>
<tr><td>Listen</td><td>A low-pitched, continuous rushing sound</td><td>A high-pitched or whistling sound, heard only in systole, or no sound</td></tr>
<tr><td>Feel</td><td>A continuous thrill, strongest near the arterial join, in a soft and easily compressed access</td><td>A hard, bounding pulse in place of a thrill, a thrill felt only in systole, a weak or flat access, warmth or tenderness, or no thrill</td></tr>
</tbody></table></div>
<p>Work in the same order every time. Ask about pain, swelling, bleeding at home, a change in the buzz, and a cold or numb hand. Uncover and compare both arms. Then look, feel, and listen from the scar to the shoulder. In a fistula, add the two tests in the next section. Record your decision.</p>
<h3>How accurate the examination is</h3>
<p>In a prospective study of 142 patients referred for a poorly working fistula, one experienced examiner recorded a diagnosis before angiography. For narrowing of the outflow, the examination had a sensitivity of 92% and a specificity of 86%. For narrowing of the inflow, the figures were 85% and 71%.[[asif2007]]</p>
<p>Skill matters. In a second study of 177 patients, the findings of a resident trained in the examination agreed closely with angiography. Those of the referring general nephrologists agreed only moderately.[[coentrao2012]] Both studies enrolled patients who were already suspected of a problem, so the examination may perform less well in patients without symptoms.</p>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) guideline recommends regular examination of every fistula and graft by a trained practitioner. As expert opinion, it adds that everyone who cares for hemodialysis (HD) patients should learn the skill.[[lok2020]]</p>
{{key:You cannot recognize an abnormal thrill until you have felt many normal ones. Examine every access you can in your first weeks.}}
"""),
        ("flow", "Narrowing and clotting", "Narrowing and clotting: when the flow changes", """
<p>The most common threat to an access is stenosis. Scar-like tissue grows from the inner wall and narrows the channel over weeks to months. Blood still enters at arterial pressure, but it cannot leave as easily. Three things follow, and each one can be felt.</p>
{{fig:pod09_stenosis}}
<p>First, pressure rises in the segment before the narrowing. The soft thrill gives way to a hard, bounding pulse, sometimes called a water-hammer pulse. Second, flow through the narrowing stops during diastole, so the thrill and the bruit shorten to systole only. Third, blood speeds up through the tight point, and the bruit there becomes high-pitched.[[salman2013]]</p>
<p>Narrowing of the inflow gives the opposite picture. Too little blood enters, so the access feels weak and flat along its length.[[salman2013]]</p>
<h3>Two bedside tests for a fistula</h3>
{{fig:pod09_tests}}
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>What you do</th><th>Normal</th><th>Abnormal</th></tr></thead>
<tbody>
<tr><td>Arm elevation, for the outflow</td><td>Look with the arm down, then raise it above the heart so that gravity drains the vein.</td><td>The whole fistula flattens.</td><td>Outflow narrowing: the part between the join and the narrowing stays full. Only the part beyond it flattens.</td></tr>
<tr><td>Pulse augmentation, for the inflow</td><td>Feel the pulse near the join while the other hand presses the fistula closed a few centimeters farther along.</td><td>The pulse becomes clearly stronger.</td><td>Inflow narrowing: the pulse strengthens little or not at all.</td></tr>
</tbody></table></div>
<p>Both tests work best in fistulas. The arm elevation test does not apply to a graft.[[salman2013]]</p>
<h3>Clues from the session itself</h3>
<p>The dialysis record adds to the examination. KDOQI lists the following as clinical indicators of a significant narrowing.[[lok2020]]</p>
<p>On examination, they are a swollen access arm and the changes in pulse, thrill, and bruit described above. During dialysis, they are new difficulty placing needles, clots drawn back through a needle, a blood flow below the prescribed rate, bleeding after needle removal that is longer than usual at three sessions in a row, and an unexplained fall in dialysis adequacy.</p>
<p>Finding these signs is called monitoring. Surveillance uses instruments, such as flow measurement or ultrasound, to look for narrowing before any sign appears. KDOQI does not recommend opening a narrowing that causes no clinical indicators, and it found the evidence too weak to advise routine surveillance of fistulas.[[lok2020]] A recent guideline from the United Kingdom takes a similar view.[[ukka2025]] Your hands and the treatment record are the main tools.</p>
<h3>Thrombosis</h3>
<p>A narrowed access clots when flow becomes slow enough. Low blood pressure, loss of body fluid, and pressure on the arm during sleep are commonly described triggers.[[daugirdas2015]] A clotted access has no thrill and no bruit. A fistula may feel like a firm cord. A pulse may remain near the join, where arterial blood still beats against the clot.[[salman2013]]</p>
<p>Time matters. Observational studies discussed in the KDOQI guideline associate earlier treatment with better results.[[lok2020]] Report a clotted access at once. The nephrologist arranges the procedure.</p>
{{call:Call the attending nephrologist at once when an access has no thrill and no bruit. Do not allow a trial needle. Record when the patient last felt the thrill. The nephrologist decides how the patient will be dialyzed and where the access will be repaired.}}
"""),
        ("wall", "Skin, wall, and hand", "Infection, aneurysm, and steal", """
<p>The flow can be normal while the skin, the wall, or the hand is in trouble. These three problems are found mainly by looking.</p>
<h3>Infection</h3>
<p>Every needle crosses the skin, and skin carries bacteria. A graft is foreign material, so bacteria that reach it are hard for the body to clear. KDOQI notes that graft infections seldom resolve with antibiotics alone, and that fistula infections are less common.[[lok2020]]</p>
<p>Do not allow needling through an infected area. Report the findings to the attending nephrologist, who orders cultures and treatment under your unit&rsquo;s protocol.</p>
<p>The signs are redness, warmth, swelling, or tenderness over the access, pus or fluid from a needle site, broken skin, or a visible graft. Fever is sometimes the only sign.</p>
<h3>Aneurysm</h3>
<p>An aneurysm is a bulge of the fistula wall. A pseudoaneurysm is a contained leak through a hole in the wall, held in by the surrounding tissue. It is the usual form in a graft.[[ukka2025]] Needling the same small area again and again weakens the wall and the skin over it. This is called area puncture. In a study of 7,058 patients in nine countries, area puncture was associated with a higher risk of access failure than moving the needle sites in an orderly way along the access, called rope-ladder needling.[[parisotto2014]] The study was observational.</p>
{{fig:pod09_aneurysm}}
<p>Many aneurysms are stable for years. The danger is the skin. When it thins, little remains to hold back arterial pressure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Lower concern</th><th>At risk of rupture</th></tr></thead>
<tbody>
<tr><td>Size over time</td><td>Unchanged</td><td>Growing</td></tr>
<tr><td>Skin over the bulge</td><td>Soft, movable, can be pinched up</td><td>Thin, shiny, pale, cannot be pinched up</td></tr>
<tr><td>Surface</td><td>Intact</td><td>Ulcer or scab</td></tr>
<tr><td>Arm raised</td><td>The bulge softens and flattens</td><td>The bulge stays tense</td></tr>
<tr><td>Bleeding after needle removal</td><td>Usual for the patient</td><td>Often prolonged</td></tr>
</tbody></table></div>
<p>This table follows the KDOQI guideline, whose advice on recognizing and needling aneurysms is expert opinion.[[lok2020]] An expert review agreed that treatment of aneurysms rests on experience and not on trials.[[inston2017]] KDOQI advises against needling an aneurysm when another site is available. When none is, the needle goes into the side or base of the bulge and not into its top.[[lok2020]]</p>
{{call:Hold needling and call the attending nephrologist the same day for a scab, an ulcer, or thin shiny skin over an aneurysm, or for a bulge that is growing. Tell the patient not to pick the scab and to keep the arm protected. KDOQI advises emergency surgical assessment for erosion or bleeding.}}
<h3>Steal: a hand short of blood</h3>
<p>The access is a low-resistance shortcut. Blood that would have supplied the hand can take the shortcut instead. Healthy arteries compensate by widening. Diseased arteries cannot, and the pressure reaching the hand falls.[[scheltinga2012]] KDOQI lists older age, female sex, diabetes, and peripheral artery disease as predictors.[[lok2020]]</p>
<p>The patient reports a cold, numb, or painful hand. You may find pale or dusky fingers, a weak grip, or sores at the fingertips. Always compare with the other hand. Severity ranges from mild numbness to gangrene.[[lok2020]]</p>
{{call:Call the attending nephrologist the same day for a hand that is cold, painful at rest, weak, or ulcerated. KDOQI advises urgent referral to a surgeon who is experienced in access problems. Severe pain or weakness soon after access surgery is an emergency.}}
"""),
        ("decide", "Safe to needle today", "Safe to needle today: the decision and the arm rules", """
<p>You do not place the needles. You decide, with the nurse, whether needling is safe, and you make the call when it is not.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you find</th><th>What it suggests</th><th>Needle today?</th><th>Whom to call</th></tr></thead>
<tbody>
<tr><td>No thrill and no bruit, even if a pulse remains near the join</td><td>Thrombosis</td><td>No</td><td>Attending nephrologist, at once</td></tr>
<tr><td>Bleeding that pressure does not stop</td><td>Rupture or a large hole in the wall</td><td>No</td><td>Emergency response and the nephrologist, at once</td></tr>
<tr><td>Scab, ulcer, or thin shiny skin over a bulge</td><td>Aneurysm at risk of rupture</td><td>Hold</td><td>Attending nephrologist, same day, before the patient leaves</td></tr>
<tr><td>Redness, pus, exposed graft, or fever with a tender access</td><td>Infection</td><td>Not through the area. Hold and ask</td><td>Attending nephrologist, same day</td></tr>
<tr><td>Cold, painful, weak, or ulcerated hand</td><td>Steal</td><td>Hold and ask</td><td>Attending nephrologist, same day</td></tr>
<tr><td>Hard pulse, systolic-only thrill, high-pitched bruit, swollen arm</td><td>Stenosis</td><td>Ask first if the finding is new. If it is known and a thrill is present, needle as the access plan states, away from the narrowing</td><td>Attending nephrologist, before needling if new, otherwise during the shift</td></tr>
<tr><td>New access not yet cleared for use</td><td>Still maturing</td><td>No</td><td>Follow the written access plan. Attending nephrologist if the plan is missing or unclear</td></tr>
</tbody></table></div>
<h3>Rules for the access arm</h3>
<p>Each rule protects the flow, the wall, or the skin. Most rest on custom and expert opinion. They cost nothing, and the harm they prevent is the loss of an access.</p>
{{cards:Never on an access arm|No blood pressure cuff::Cuff pressure stops the flow, and stopped flow can clot.|No blood draws or intravenous lines::Each puncture outside the planned needle sites injures the wall and can bring infection.|No tight bandage, watch, sleeve, or bag strap::Steady pressure around the arm slows the flow.|No needle through infected, scabbed, or thin skin::The skin may not seal when the needle comes out.|No wrap that encircles the arm after a session::Pressure belongs on the needle site only.}}
<p>The other arm also needs care, because it may hold the next access. KDOQI considers it reasonable to protect the arm veins and arteries of every patient who is on dialysis or may need it, and to avoid unnecessary punctures and long catheters placed through arm veins.[[lok2020]]</p>
"""),
        ("bleeding", "Bleeding", "Bleeding from a needle site or a ruptured access", """
<p>A working access carries several hundred milliliters to more than a liter of blood each minute.[[daugirdas2015]] A needle hole normally seals under fingertip pressure. A larger hole can empty the circulation within minutes.</p>
<p>Fatal bleeding is rare. A review from Australia and New Zealand estimated fewer than one death for every 1,000 patient-years on dialysis, and the authors judged these deaths potentially preventable.[[jose2017]] In a review of 88 fatal access bleeds in the United States, 78% of the deaths with a known location happened at home or in a nursing home.[[ellingson2012]] A patient safety alert in England described 11 life-threatening bleeds over three years, seven of them fatal, and noted that in some patients warning signs had not been recognized.[[nhs2018]] All three reports are retrospective.</p>
<p>Two lessons follow. Many ruptures give warning, so examine the skin. Most happen away from the unit, so the patient and family must know what to do.</p>
<h3>Bleeding from a needle site</h3>
{{fig:pod09_pressure}}
{{flow:A needle site that keeps bleeding|Press on the right spot::Use two gloved fingertips and a small folded gauze. The hole in the vessel lies slightly beyond the hole in the skin, along the needle track. Cover both.|Press firmly, not completely::Stop the bleeding without stopping the thrill. Feel for the thrill beyond your fingers.|Hold without lifting::Keep steady pressure for the time in your unit&rsquo;s protocol. Lifting the gauze pulls the clot away.|Avoid bulky pads::A thick towel spreads the force and hides the bleeding.|Check and record::Confirm that the bleeding has stopped and that the thrill is present before any dressing goes on.}}
<p>Then ask why it happened. Common causes are the blood thinner given during the session, high pressure from an outflow narrowing, and fragile skin over an aneurysm. Longer bleeding at several sessions in a row is a clinical indicator of stenosis.[[lok2020]] Report it to the attending nephrologist. The blood thinner is part of the prescription.</p>
<h3>A ruptured access</h3>
<p>Rupture is a tear in the wall, usually through eroded skin over an aneurysm or an infected graft. Your only aim is to stop the bleeding. Saving the access is not a goal at this moment.[[kcuk_bleed]]</p>
{{flow:First response to a ruptured access|Press directly on the bleeding point::Use gloved fingers and a small gauze, and press hard, even if the thrill stops. Do not pile on towels.|Shout for help while you press::Call the unit&rsquo;s emergency response. Send someone to telephone the attending nephrologist.|If the patient is on the machine::Have the nurse stop the blood pump and clamp the lines at once. Do not return the blood now.|Lay the patient flat and raise the arm::Give oxygen and ask for an intravenous line in the other arm, as your unit&rsquo;s protocol allows.|Do not let go::Keep the pressure on through the transfer. If direct pressure fails, use the further steps in your unit&rsquo;s protocol.|Transfer::The patient needs a surgeon, even if the bleeding stops.}}
<p>Guidance written for patients in the United Kingdom adds an improvised tool for a bleed that direct pressure does not stop. A plastic bottle cap is placed over the bleeding point with its hollow side against the skin and is held down firmly, and bandaged in place if possible, to seal the area.[[kcuk_bleed]] This is expert opinion written for patients at home, based on 2018 recommendations from two British professional societies. It has not been tested in a trial, and it does not replace direct pressure or the call for help. Ask whether your unit teaches it.</p>
{{call:Bleeding that is not controlled by direct pressure is an emergency. Activate the emergency response, keep pressing, and have the attending nephrologist called at once. Do not release the pressure to look, to dress the wound, or to move the patient.}}
{{flow:Call card: bleeding from a fistula or graft|Recognize::Bleeding that spurts, soaks the gauze, or returns when pressure is eased.|First 2 minutes::Gloves. Firm fingertip pressure on the bleeding point. Call for help. Patient flat, arm raised.|Stop dialysis?::Yes, at once, for a rupture, for a needle that has come out, or for any bleeding that pressure does not control. Have the nurse stop the blood pump and clamp the lines.|Return the blood?::Not during the emergency. Never delay pressure to save the blood in the circuit. Do NOT return blood while the access still bleeds, through a needle that has come out or moved, into a swollen needle site, or from a circuit that holds air or clots or has stood still longer than your unit&rsquo;s protocol allows. Never put back a needle that has come out. The nurse returns blood only when the bleeding is controlled, the return needle is secure and away from the bleeding point, and the attending nephrologist agrees. If in doubt, do not return it.|Call::Emergency response and the attending nephrologist at once. Transfer for surgical assessment after any rupture.|Write::Time, site, estimated blood loss including blood left in the circuit, the thrill afterward, vital signs, and who was called.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you examine, and what do you expect to find?</strong> Look, listen, and feel along the whole fistula, and compare the two arms and hands. In Mrs. Bautista you would expect no thrill and no bruit. The vein may feel firm, like a cord, and a pulse may remain near the join. These findings mean thrombosis. Last week&rsquo;s notes explain it. A higher venous pressure and longer bleeding after needle removal are warning signs of an outflow narrowing. The fistula gave warning twice before it clotted.</p>
<p><strong>Should anyone needle it today?</strong> No. A needle placed in a clotted fistula yields no flow. It injures the wall, and it may make the repair harder. A &ldquo;trial needle&rdquo; adds harm and no information, because the examination has already answered the question.</p>
<p><strong>Whom do you call, and what else does she need?</strong> Call the attending nephrologist now, because a clotted access is best cleared promptly. Report the access type and age, the time she last felt the thrill, your findings, and last week&rsquo;s two notes. She also still needs dialysis. She is four days from her last session and 3.4 kilograms above her dry weight, so assess her as Module 2 described. The nephrologist decides how she will be dialyzed today and where the fistula will be repaired.</p>
<p>Last week&rsquo;s notes should have led to a call that day. Mrs. Bautista should also have known to telephone the unit as soon as the thrill was gone.</p>
"""],
    "skills": {"title": "Full access examination",
               "intro": "Examine the fistula or graft of five patients before needling while your preceptor observes. Include at least one graft.",
               "items": [
                   ("Reads the chart for the access type, date of creation, direction of flow, and notes from the last three sessions.", True),
                   ("Asks about pain, swelling, bleeding at home, a change in the thrill, and coldness or numbness of the hand.", False),
                   ("Cleans hands, exposes both arms to the shoulder, and compares arm size and the two hands.", True),
                   ("Inspects the whole access for redness, discharge, scabs, bulges, and thin or shiny skin.", True),
                   ("Palpates from the arterial join along the whole access and states whether a thrill is present and continuous.", True),
                   ("Distinguishes a thrill from a pulse and states where each is felt.", True),
                   ("Listens along the access and describes the pitch and timing of the bruit.", False),
                   ("Performs the arm elevation test on a fistula and states the result.", False),
                   ("Performs the pulse augmentation test on a fistula and states the result.", False),
                   ("Checks the hand for color, warmth, sensation, and grip, compared with the other side.", False),
                   ("States a decision: safe to needle, or hold and call, with the findings that support it.", True),
                   ("Shows where and how to press on a bleeding needle site, and checks the thrill afterward.", True),
                   ("Records the findings and states what would be reported to the attending nephrologist.", False),
               ],
               "placement": "During your first two weeks, examine one access before every shift with a senior nurse, and ask the nurse to show you one access with a known narrowing so that you can feel the difference."},
    "quiz": [
        ("What is the main difference between a fistula and a graft?",
         ["A fistula uses the patient&rsquo;s own vein, and a graft uses a synthetic tube", "A fistula is in the arm, and a graft is in the neck",
          "A fistula has no join to an artery", "A graft needs no needles"], 0,
         "In a fistula the patient&rsquo;s own vein is needled. In a graft a synthetic tube connects artery and vein and is needled."),
        ("Why is the thrill of a healthy access continuous?",
         ["The heart rate is fast", "The vein offers little resistance, so blood flows in systole and in diastole",
          "The needles keep the flow going", "The vein valves vibrate"], 1,
         "The access is a low-resistance path, so flow and vibration continue through diastole."),
        ("You feel a hard, bounding pulse where a soft thrill used to be. What is the most likely cause?",
         ["Inflow narrowing", "Infection", "Outflow narrowing beyond that point", "Steal"], 2,
         "Blood enters at arterial pressure and cannot leave easily, so pressure rises before the narrowing."),
        ("You raise the arm of a patient with a forearm fistula. The lower half stays full and the upper half flattens. What does this suggest?",
         ["A normal fistula", "Inflow narrowing", "Thrombosis", "An outflow narrowing between the two halves"], 3,
         "A normal fistula flattens along its length. With an outflow narrowing, only the part beyond it drains."),
        ("In the pulse augmentation test, the pulse near the join barely strengthens. What does this suggest?",
         ["Inflow narrowing", "Outflow narrowing", "An aneurysm", "A normal fistula"], 0,
         "With normal inflow the pulse strengthens clearly against the occluding finger."),
        ("Mr. Ramos has a looped forearm graft. Before his session the nurse finds no thrill and no bruit. He feels well. What do you do first?",
         ["Allow one trial needle", "Confirm the findings, hold needling, and call the attending nephrologist at once",
          "Apply a warm compress and re-examine later", "Book an ultrasound for next week"], 1,
         "No thrill and no bruit mean thrombosis. A trial needle adds harm, and earlier treatment is associated with better results."),
        ("Which statement about graft infection does the KDOQI guideline support?",
         ["It is rarer than fistula infection", "The area can be needled if there is no fever",
          "It seldom resolves with antibiotics alone", "It never causes fever"], 2,
         "A graft is foreign material, and bacteria that reach it are hard to clear."),
        ("Mrs. Aquino has a bulge on her fistula. Today the skin over it is shiny, cannot be pinched up, and has a small scab. The thrill is normal. What is the best action?",
         ["Needle elsewhere and review next month", "Remove the scab to inspect beneath",
          "Dress the scab and proceed", "Hold needling and call the attending nephrologist today"], 3,
         "Thin shiny skin and a scab mean a wall at risk of rupture. KDOQI advises emergency surgical assessment for erosion."),
        ("Why does repeated needling in one small area raise concern?",
         ["It weakens the wall and skin, and was associated with more access failure in a large cohort", "A randomized trial showed that it causes infection",
          "It lowers blood flow during the session", "It causes steal"], 0,
         "In an observational study of 7,058 patients, area puncture was associated with a higher risk of access failure than rope-ladder needling."),
        ("Mr. Santiago has diabetes and a new upper-arm fistula. The hand on that side is cold, numb, and pale. The thrill is strong. What is the most likely problem?",
         ["Thrombosis", "Steal", "Infection", "Outflow narrowing"], 1,
         "Blood is taking the shortcut through the access, and diseased arteries cannot compensate."),
        ("A needle site is still bleeding after the session. Which technique is correct?",
         ["A tight bandage around the arm", "Lifting the gauze often to check",
          "Two fingertips over the skin hole and the vessel hole, firm enough to stop bleeding while a thrill remains", "A thick towel over the whole access"], 2,
         "Pressure belongs on the needle site. It should stop the bleeding without stopping the flow, and it should not be lifted early."),
        ("A scab over an aneurysm gives way during dialysis, and blood pours from the arm. Which response is correct?",
         ["Return the blood in the circuit first", "Apply a loose dressing and wait for the surgeon",
          "Release the pressure each minute to look", "Press hard on the bleeding point, call for help, and have the blood pump stopped"], 3,
         "Direct pressure comes first and is not released. Blood in the circuit is never a reason to delay."),
        ("In the review of 88 fatal access bleeds, where did most deaths with a known location occur?",
         ["At home or in a nursing home", "In the dialysis unit", "In the operating room", "In the emergency room"], 0,
         "The figure was 78%. Patients and families need to know the warning signs and how to press."),
        ("A ward nurse is about to take a blood pressure on a fistula arm. What is the best explanation to give?",
         ["The reading will be falsely high", "The cuff can stop the flow, and stopped flow can clot",
          "The cuff will cause steal", "The cuff will infect the fistula"], 1,
         "The rule rests on physiology and expert opinion, and it costs nothing to follow."),
        ("What does KDOQI say about a narrowing that causes no clinical indicators?",
         ["Always open it", "Treat it with a blood thinner",
          "It does not recommend opening it", "Create a new access"], 2,
         "KDOQI relies on regular examination and the treatment record to identify the narrowings that need action."),
    ],
    "terms": [("Arteriovenous fistula", "A surgical join between an artery and the patient&rsquo;s own vein, which enlarges and is needled for dialysis."),
              ("Arteriovenous graft", "A synthetic tube under the skin that connects an artery to a vein and is needled for dialysis."),
              ("Anastomosis", "The surgical join between two vessels, or between a vessel and a graft."),
              ("Maturation", "The widening and thickening of a fistula vein in the weeks to months after surgery."),
              ("Thrill and bruit", "The vibration felt and the sound heard over a flowing access."),
              ("Stenosis", "A narrowing inside a vessel or graft."),
              ("Thrombosis", "A clot that blocks the access."),
              ("Aneurysm and pseudoaneurysm", "A bulge of the vessel wall, and a contained leak through a hole in the wall."),
              ("Steal", "Too little blood reaching the hand because blood is diverted through the access."),
              ("Rope-ladder needling", "Moving the needle sites in an orderly way along the access so that each site can heal.")],
    "readings": [("hemodialysis-access-lifeline.html", "The types of access and how each is made, in more detail."),
                 ("dialysis-access-care.html", "How patients care for a fistula or graft at home."),
                 ("dialysis-access-infection.html", "Recognition and prevention of access infection.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
