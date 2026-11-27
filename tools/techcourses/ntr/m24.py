# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 24: Vascular access and the patient life-plan.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
KDOQI 2019 statements and grades checked against the guideline statement list; Ravani 2013, Al-Jaishi 2014, Asif 2007 and the IPHN
registry against PubMed abstracts. No doses, no lock or antibiotic regimens. Every case is fictional."""

MODULE = {
 'image_alt': 'A nephrology fellow examines the forearm fistula of a seated patient, listening with a stethoscope while a resident feels the thrill, '
              'in a Philippine dialysis unit.',
 'objectives': [
  '<strong>Intern:</strong> Protect the arm veins of every patient with advanced chronic kidney disease, recognize an access that has no thrill, '
  'is bleeding or shows signs of infection, and report it at once.',
  '<strong>Resident:</strong> Examine an arteriovenous fistula by looking, feeling and listening, recognize inflow and outflow dysfunction and '
  'catheter dysfunction or infection, and write a clear referral.',
  '<strong>Fellow:</strong> Plan dialysis access with each patient through the end-stage kidney disease (ESKD) Life-Plan of the Kidney Disease '
  'Outcomes Quality Initiative (KDOQI) 2019 guideline, choose between fistula, graft, catheter and peritoneal dialysis, and lead monitoring and '
  'timely referral.',
 ],
 'big': """<div class="tc-keyp"><span class="tc-lab">Your role &middot; guardian of the veins</span>The intern protects veins: no blood draws or
intravenous lines in the arm chosen for a fistula, and no peripherally inserted central catheter (PICC) without asking the nephrology team. The
resident examines the access at every dialysis round and admission, and knows a failing fistula before it clots. The fellow plans the access
years ahead, with the patient, the surgeon and the family, and keeps the plan written where everyone can see it.</div>
{{plain:Think of vascular access as the road to a town. A fistula is a paved road that took months to build and lasts for years if it is
maintained. A catheter is a temporary bridge put up overnight: useful in an emergency, but it washes out, it lets in trouble, and each one
built damages the riverbank so the next one is harder to place.}}
<p>The picture has a limit. A fistula is not built once and finished. After a surgeon joins an artery to a vein, the vein must dilate and
thicken under arterial pressure until it carries enough blood for dialysis. Many never do. And the road can narrow anywhere along its length:
at the arterial inflow, at the anastomosis, in the needling segment, or far away in the central veins of the chest, often because of
catheters placed months or years before. So the access is a lifelong project that depends on veins that were protected long before
anyone thought of dialysis.</p>
{{cards:Key numbers|Catheter versus fistula (62 cohort studies, 586,337 people)::All-cause mortality risk ratio 1.53; fatal infection 2.12; cardiovascular events 1.38 (observational)|Fistula primary failure (meta-analysis, 7,393 fistulas)::23%|Fistula primary patency including failures::60% at 1 year, 51% at 2 years|Physical examination versus angiography (142 fistulas)::Outflow stenosis sensitivity 92%, specificity 86%; inflow 85% and 71%|KDOQI 2019 referral for access::When eGFR is 15&ndash;20 mL/min/1.73 m&sup2; (expert opinion)|KDOQI 2019 maturation check::By 4&ndash;6 weeks after creation (expert opinion)}}
<p>Most Philippine patients start hemodialysis through a catheter, often in an emergency, because they reached a nephrologist late or could not
afford surgery in time. A few keep that catheter for years and lose central vein after central vein to infection and stenosis. Your work is to
plan the access before it is needed, examine it every time you see the patient, and refer early when it begins to fail.</p>
""",
 'case': {'title': 'The second catheter this year',
  'html': """<p>It is Wednesday afternoon on the medical ward of a provincial hospital in Batangas City. Mrs. Lourdes Dimaculangan, 54, a sari-sari
store owner with diabetes, started hemodialysis 11 months ago through a temporary femoral catheter after she came to the emergency room
breathless and uremic. A tunneled right internal jugular catheter followed. No fistula was created: the family could not pay for surgery then,
and she was afraid of &ldquo;having her arm cut.&rdquo;</p>
<p>Three months ago she was admitted with fever and chills that began during dialysis, with blood cultures growing <em>Staphylococcus aureus</em>.
The right catheter was removed and a tunneled left internal jugular catheter placed. Today she is admitted again because the unit could not keep
the blood flow up and two sessions ended early. She has a healed PICC scar on her left arm from a pneumonia admission two years ago, before she
knew she had kidney disease. Her left arm and left face are a little puffy, and there are dilated veins over her left upper chest.</p>
<p>The fellow asks you, the resident, to examine her access and her arms and to draft a plan for the attending nephrologist.</p>""",
  'questions': ['What does Mrs. Dimaculangan&rsquo;s course say about her ESKD Life-Plan, and where did it fail?',
                'What do you look for in her arms, neck and chest, and what do the swelling and chest veins suggest?',
                'What should the fellow propose for her access now and over the next months?']},
 'sections': [
  ('life-plan', 'Life-Plan', 'The ESKD Life-Plan: access as part of a life, not a procedure', """
<p>The KDOQI 2006 guideline promoted &ldquo;fistula first.&rdquo; Fistula rates rose, but so did fistulas that never matured, interventions
to rescue them and months spent on catheters waiting. The 2019 update replaced a single rule with a plan for each person. KDOQI considers it
reasonable for every patient with chronic kidney disease (CKD) heading toward kidney failure to have an individualized ESKD Life-Plan that is
regularly reviewed, updated and documented in the medical record, with an annual review (expert opinion).[[ntr24_1]] The Life-Plan maps the
modalities a person is likely to use over a lifetime (peritoneal dialysis, hemodialysis, transplant, conservative care) and the access each
needs, in the order that preserves the most future options.</p>
<p>The reasoning is about sequence. A forearm fistula placed first leaves the upper arm for later. A catheter in the left internal jugular can
narrow the left brachiocephalic vein and ruin every future access in the left arm. A patient who starts on peritoneal dialysis keeps both arms
untouched for years. A patient with a living donor ready in six months may reasonably skip fistula surgery. KDOQI considers an arteriovenous (AV)
access, fistula or graft, reasonable when it is consistent with the Life-Plan and the person&rsquo;s goals (expert opinion), and lists
situations where a tunneled catheter is reasonable: short term, for example while a newly created AV access is not yet ready, and long
term, for example when life expectancy is limited (expert opinion).[[ntr24_1]]</p>
<p><strong>Why the access type matters.</strong> In a systematic review of 62 cohort studies including 586,337 people, catheter users, compared with
fistula users, had higher all-cause mortality (risk ratio 1.53, 95% confidence interval 1.41 to 1.67), fatal infections (2.12) and cardiovascular
events (1.38); graft users also had higher mortality than fistula users (1.18).[[ntr24_2]] The authors rated the risk of selection bias as high: sicker
patients are more likely to have catheters, so these numbers describe association, not the effect of switching a given patient.</p>
<p><strong>Why the fistula is not automatic.</strong> A meta-analysis of 46 studies found a primary failure rate of 23% for new fistulas; primary
patency, counting those failures, was 60% at 1 year and 51% at 2 years, and secondary patency 71% and 64%.[[ntr24_3]] A fistula is the best access
when it works, and a fistula plan must include what happens when it does not.</p>
<div class="table-wrap"><table><thead><tr><th>Person</th><th>Reasonable first access in the Life-Plan</th><th>Why</th></tr></thead><tbody>
<tr><td>Working adult, good veins, months before dialysis</td><td>Forearm fistula, or peritoneal dialysis catheter</td><td>Time to mature; preserves the upper arm</td></tr>
<tr><td>Older adult, poor veins, short expected time on dialysis</td><td>Graft or tunneled catheter, by goals</td><td>A fistula may not mature in the time that matters</td></tr>
<tr><td>Living donor transplant expected within months</td><td>Catheter or peritoneal dialysis</td><td>Surgery may not be needed</td></tr>
<tr><td>Emergency start without access</td><td>Catheter now, permanent access planned at once</td><td>The catheter is a bridge, not a destination</td></tr>
<tr><td>Prefers home therapy</td><td>Peritoneal dialysis catheter</td><td>Both arms kept for later</td></tr>
</tbody></table></div>
<p>KDOQI suggests referral for access assessment and creation when the estimated glomerular filtration rate (eGFR) is 15 to 20 mL/min/1.73 m&sup2;
in patients with progressive CKD, and selective preoperative ultrasound vessel mapping in patients at high risk of access failure (conditional,
low-quality evidence); the referral threshold itself is expert opinion.[[ntr24_1]] In the Philippines, where cost delays surgery and many patients
first meet a nephrologist in the emergency room, the referral often comes too late. The Life-Plan conversation belongs in the CKD clinic, at the
first visit with an eGFR under 30.</p>
<p><strong>What you do at your stage.</strong> The intern writes &ldquo;protect left arm: no needles&rdquo; on the chart of a CKD patient
when asked. The resident asks every new dialysis patient what the access plan is. The fellow writes the Life-Plan in the chart: current
modality and access, the next access and its timing, transplant status, and the date of the next review.</p>
{{key:Every patient heading to dialysis needs a written plan for this access, the next access and the one after. A catheter without a plan is
how central veins are lost.}}
{{fig:ntr24_b}}
"""),
  ('exam', 'Examine the fistula', 'Look, feel, listen: examining a fistula', """
<p>A fistula is a high-flow, low-resistance circuit. Blood leaves the artery at the anastomosis, rushes into the vein and returns to the heart. A
healthy fistula is soft, with a continuous thrill that you feel and a continuous low-pitched bruit that you hear through systole and diastole.
A narrowing changes the physics. Upstream of a narrowing the vein is under higher pressure, so it becomes pulsatile and does not collapse;
downstream it is flat. A narrowing in the inflow, on the arterial side, gives a weak, flat fistula that fills poorly.</p>
<p>Physical examination is accurate enough to matter. In 142 patients referred for fistula dysfunction, examination before angiography identified
outflow stenosis with a sensitivity of 92% and a specificity of 86%, and inflow stenosis with 85% and 71%, against an independent, blinded
reading of the angiogram.[[ntr24_4]] This was a referred population with suspected problems, examined by experienced interventionists, so the
accuracy in routine rounds by trainees is likely lower. But the skill is learnable, cheap and available in every province.</p>
{{flow:Fistula examination at the chair|Look::Arm swelling, collateral veins on the chest or shoulder, aneurysms, shiny or thin skin over needling sites, redness, discharge, scabs that do not heal. Compare both arms.|Feel::A continuous thrill at the anastomosis. Strong pulsation instead of a thrill suggests a downstream (outflow) narrowing. A weak, flat vessel suggests an inflow problem.|Arm elevation test::Raise the arm above the heart. A healthy fistula collapses. One that stays distended suggests outflow stenosis.|Augmentation test::Occlude the fistula a few centimeters above the anastomosis. The pulse below should strengthen. A weak augmentation suggests inflow stenosis.|Listen::A continuous low-pitched bruit is normal. A high-pitched or systolic-only bruit suggests a narrowing.|Check the hand::Color, warmth, capillary refill, sensation and pain, especially during dialysis.}}
<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Physiology</th><th>Likely problem</th><th>What the dialysis nurse may report</th></tr></thead><tbody>
<tr><td>Pulsatile, does not collapse on arm elevation</td><td>High pressure above a downstream narrowing</td><td>Outflow stenosis</td><td>High venous pressure alarms, prolonged bleeding after needle removal</td></tr>
<tr><td>Weak, flat, poor augmentation</td><td>Low inflow</td><td>Inflow (arterial or juxta-anastomotic) stenosis</td><td>Low arterial pressure alarms, cannot reach blood flow, collapse of the vein</td></tr>
<tr><td>Whole arm swollen, chest collaterals</td><td>Central vein narrowing; blood reroutes through collaterals</td><td>Central vein stenosis, often after catheters or PICCs</td><td>Arm swelling that worsens during dialysis</td></tr>
<tr><td>No thrill, no bruit</td><td>No flow</td><td>Thrombosis</td><td>Cannot needle, no blood return</td></tr>
<tr><td>Cold, pale, painful hand during dialysis</td><td>Blood diverted from the hand into the fistula</td><td>Access-related hand ischemia (steal)</td><td>Pain and numbness during sessions</td></tr>
<tr><td>Thin shiny skin, scab over an aneurysm</td><td>Wall weakened by repeated needling</td><td>Risk of rupture</td><td>Bleeding between sessions</td></tr>
</tbody></table></div>
<p>KDOQI 2019 recommends regular physical examination or check of the fistula by a knowledgeable and experienced practitioner to detect
dysfunction, and treats clinical monitoring as primary and surveillance findings as supplementary.[[ntr24_1]] For grafts, KDOQI does not suggest routine
surveillance by flow measurement, pressure monitoring or imaging in addition to clinical monitoring (conditional, low-quality evidence); for fistulas it
found insufficient evidence to make a suggestion.[[ntr24_1]] A new fistula should be evaluated for maturation by an appropriate member of the access team
by 4 to 6 weeks after creation (expert opinion).[[ntr24_1]]</p>
<p><strong>What you do at your stage.</strong> The intern checks for a thrill and reports its absence at once. The resident examines the fistula
in this order at every round and documents findings in words, not &ldquo;AVF functioning.&rdquo; The fellow correlates the examination with
the dialysis flow sheet and refers for imaging or intervention when findings and alarms agree.</p>
{{key:Examine the fistula the same way every time: look, feel, raise the arm, augment, listen, check the hand. A narrowing is usually felt
before it clots.}}
{{fig:ntr24_a}}
"""),
  ('catheters', 'Catheters', 'Catheters: the bridge, its course and its dangers', """
<p>A tunneled cuffed hemodialysis catheter enters a central vein, usually the right internal jugular, runs down through the brachiocephalic vein
and superior vena cava, and ends with its tip in the right atrium or at the junction of the superior vena cava and right atrium. The other end
travels under the skin of the chest to an exit site several centimeters away, where a cuff in the tunnel becomes fixed by scar tissue and blocks
bacteria from tracking along the outside. Two lumens carry blood out and back. KDOQI lists the internal jugular as the preferred site, followed by
external jugular, femoral, subclavian and lumbar, and considers the right side preferable to the left because the course to the atrium is
straighter (expert opinion).[[ntr24_1]]</p>
<p>The dangers follow from the anatomy. The catheter is a foreign body in the bloodstream with a direct path from the skin. Infection can start at
the exit site, track along the tunnel, or colonize the lumen and seed the blood every time it is opened. The catheter rubs the vein wall and
provokes thrombosis and stenosis of the central veins, which may not show until a fistula on that side swells the arm. Fibrin sheath and
thrombus at the tip reduce flow, so K falls and the dose with it.</p>
<div class="table-wrap"><table><thead><tr><th>Problem</th><th>Mechanism</th><th>What you see</th><th>What you do at your stage</th></tr></thead><tbody>
<tr><td>Exit-site infection</td><td>Skin bacteria at the exit</td><td>Redness, crust or pus within about 2 cm of the exit</td><td>Report; swab per protocol; the fellow decides treatment</td></tr>
<tr><td>Tunnel infection</td><td>Infection along the subcutaneous track</td><td>Tenderness, redness or induration along the tunnel</td><td>Report now; usually needs catheter removal</td></tr>
<tr><td>Catheter-related bloodstream infection</td><td>Bacteria in the lumen enter the blood at connection</td><td>Fever or rigors starting soon after dialysis begins; hypotension</td><td>Blood cultures before antibiotics; call the fellow and attending</td></tr>
<tr><td>Dysfunction</td><td>Fibrin sheath, thrombus, malposition or kinking</td><td>Cannot reach the prescribed blood flow; pressure alarms; lines reversed</td><td>Review the flow sheet; follow the catheter protocol; refer</td></tr>
<tr><td>Central vein stenosis</td><td>Endothelial injury from the catheter</td><td>Arm, face or breast swelling; chest wall collaterals</td><td>Examine both arms and chest; document; refer for imaging</td></tr>
</tbody></table></div>
<p>KDOQI defines catheter dysfunction as failure to maintain the prescribed extracorporeal blood flow required for adequate hemodialysis (expert
opinion), and suggests locking solutions chosen to help prevent infection and dysfunction where feasible (conditional, low-quality evidence); the
lock and its concentration come from the unit&rsquo;s protocol.[[ntr24_1]] The Infectious Diseases Society of America (IDSA) 2009 guideline
describes how to diagnose catheter-related bloodstream infection with paired blood cultures and how to decide on catheter removal by the infecting microbe and
course; <em>Staphylococcus aureus</em> bacteremia is among the infections in which a hemodialysis catheter is usually removed and complications
such as endocarditis must be sought.[[ntr24_5]] Antibiotic choice and duration come from that guideline, the unit&rsquo;s protocol and the
attending.</p>
<p><strong>What you do at your stage.</strong> The intern never uses a dialysis catheter for blood draws or infusions unless the unit protocol and
the nephrology team allow it. The resident examines the exit site and tunnel at every round, and takes blood cultures before the first antibiotic
when a catheter patient has fever. The fellow counts catheter days, decides with the attending when to remove a catheter, and treats every catheter
as a bridge with an end date.</p>
{{key:A catheter is a bridge with an end date. Write the date and the destination in the chart the day it goes in.}}
"""),
  ('dysfunction', 'Dysfunction', 'Recognizing dysfunction and referring in time', """
<p>An access fails gradually and then suddenly. A narrowing grows over weeks; blood flow falls, recirculation rises, the Kt/V drifts down,
bleeding after needle removal lengthens, and then one morning there is no thrill. The goal is to act in the weeks before that morning, because a
thrombosed fistula may not be salvageable and the patient returns to a catheter.</p>
<div class="table-wrap"><table><thead><tr><th>Clue</th><th>Where it appears</th><th>What it suggests</th></tr></thead><tbody>
<tr><td>Falling Kt/V without a change in the order</td><td>Monthly laboratory results</td><td>Recirculation or low access flow (Module 23)</td></tr>
<tr><td>Rising venous pressure; prolonged bleeding</td><td>Flow sheet; nurse report</td><td>Outflow stenosis</td></tr>
<tr><td>Arterial pressure alarms; cannot reach blood flow</td><td>Flow sheet</td><td>Inflow stenosis or catheter dysfunction</td></tr>
<tr><td>Difficult cannulation; new pain</td><td>Nurse report</td><td>Stenosis, infiltration, aneurysm or a fistula that never matured</td></tr>
<tr><td>Change on examination</td><td>Your round</td><td>Any of the above, localized by look, feel and listen</td></tr>
<tr><td>Arm swelling</td><td>Examination</td><td>Central vein stenosis</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>A
fistula or graft has lost its thrill and bruit: thrombosis is time-sensitive.</li><li>An access bleeds and does not stop with firm pressure, or an
aneurysm has thin, shiny or ulcerated skin.</li><li>A catheter patient has fever, rigors or hypotension at the start of dialysis.</li><li>The hand
on the access side is cold, pale, numb or painful.</li><li>Redness, pus or tenderness tracks along a catheter tunnel or over a graft.</li></ul>}}
<p>In the Philippines, intervention depends on what is near. Some provinces have a vascular surgeon but no interventional radiology, or the reverse;
many patients pay for angiography themselves. The fellow&rsquo;s task is to know the local pathway before it is needed: who can see a failing
fistula within days, who can declot one, and what it costs. The Philippine Society of Nephrology (PSN) 2024 hemodialysis guidelines set the local
standards that units follow for access care.[[ntr24_7]]</p>
<p><strong>What you do at your stage.</strong> The resident brings the flow sheet and the examination together in one sentence: &ldquo;Venous
pressures rising for three weeks, bleeding 25 minutes after needle removal, pulsatile fistula that does not collapse on arm elevation.&rdquo;
The fellow refers with that sentence, agrees on urgency with the attending, and tells the patient what will happen if nothing is done.</p>
{{key:Act on the trend, not on the clot. Three weeks of rising pressures and longer bleeding are a referral, not a watching brief.}}
"""),
  ('vein-preservation', 'Vein preservation', 'Preserving veins, starting in the ward', """
<p>Every future fistula depends on veins that someone else may have used up. Venipuncture, intravenous cannulas and especially PICCs injure the
endothelium of arm veins; PICCs and subclavian lines narrow the central veins that every arm access drains through. A patient with CKD stage 4
whose cephalic vein was used for a week of antibiotics may have lost the best fistula site before ever seeing a nephrologist.</p>
<p>KDOQI considers it reasonable to protect all central and peripheral arteries and veins from damage whenever possible, and to avoid peripherally
inserted catheters and unnecessary venipunctures in patients with CKD (expert opinion).[[ntr24_1]] These are expert-opinion statements, but the
physiology is not in dispute, and in the Philippines the cost of losing a site is a catheter that the family may pay for again and again.</p>
<div class="table-wrap"><table><thead><tr><th>Ward practice</th><th>Why it matters</th><th>Better practice</th></tr></thead><tbody>
<tr><td>Blood draws from the cephalic vein at the wrist or forearm</td><td>Scarring of the commonest fistula vein</td><td>Use dorsal hand veins; sign &ldquo;save this arm&rdquo; at the bed</td></tr>
<tr><td>PICC for a week of antibiotics</td><td>Arm and central vein thrombosis and stenosis</td><td>Ask nephrology first; consider a small-bore internal jugular line if central access is needed</td></tr>
<tr><td>Subclavian temporary dialysis catheter</td><td>Central stenosis that ruins the arm on that side</td><td>Internal jugular or femoral per KDOQI site order</td></tr>
<tr><td>Blood pressure cuff or needles on a fistula arm</td><td>Compression, thrombosis, infection</td><td>Use the other arm; label the fistula arm</td></tr>
</tbody></table></div>
<div class="tc-keyp"><span class="tc-lab">In children</span>Small vessels make fistulas harder to create and slower to mature in children, and many expect
an early living-related transplant, so catheters are used more often. In the International Pediatric Hemodialysis Network registry of 552 children,
628 catheters and 225 fistulas were placed; catheters gave lower blood flows and Kt/V, and infections were reported only with catheters.[[ntr24_6]] See <a
href="attending-pediatric-nephrologist-24-vascular-access.html">Attending Pediatric Nephrologist, Module 24</a>.</div>
<p><strong>What you do at your stage.</strong> The intern asks before placing a line in a CKD patient&rsquo;s arm and uses the hand veins for
blood draws. The resident questions every PICC order for a patient with an eGFR under 30. The fellow teaches the ward, writes vein preservation into
admission orders for CKD patients, and makes sure the dialysis unit knows which arm is reserved.</p>
{{key:The fistula a patient has in three years is decided by the needle a ward team uses today. Ask before you puncture an arm vein in CKD.}}
"""),
 ],
 'debrief': [
  """<p><strong>Where the Life-Plan failed.</strong> Mrs. Dimaculangan never had a Life-Plan. She reached a nephrologist in the emergency room, a
catheter became the plan, a fistula was deferred for cost and fear, and peritoneal dialysis was apparently not discussed. Each catheter carried
infection risk, and her <em>Staphylococcus aureus</em> bacteremia is the outcome that the observational data warn about. The PICC placed two years
ago, before her kidney disease was known, likely injured the left arm veins. The plan must now be written: modality options including
peritoneal dialysis, the next access, transplant eligibility and a review date.</p>""",
  """<p><strong>The examination.</strong> Look at both arms, the neck and the chest; feel for veins suitable for a fistula; check the catheter exit
site and tunnel for redness, tenderness or pus; and ask about fever at the start of dialysis. Left arm and face swelling with dilated chest veins on
the side of a current catheter and an old PICC suggest left brachiocephalic or central vein stenosis or thrombosis, which also explains the poor
flow. Document it in words and arrange imaging with the attending.</p>""",
  """<p><strong>What the fellow proposes.</strong> Restore adequate dialysis now through catheter assessment or exchange per the unit protocol and the
interventional team. Then plan permanent access: vessel mapping with ultrasound, favoring the right arm if the central veins on that side are open,
or a graft if the veins are poor, with a referral date set before discharge. Offer peritoneal dialysis honestly as an option that spares her veins.
Explain to her and her family what a fistula operation involves, what it costs and what PhilHealth and the hospital can cover, and that each
catheter makes the next access harder.</p>""",
 ],
 'skills': {'title': 'Vascular access and the patient life-plan',
            'intro': 'Complete with a preceptor in a dialysis unit or ward. Sign-off is local.',
            'items': [('Examines a fistula by look, feel, arm elevation, augmentation and auscultation, and documents findings in words', False),
                      ('Examines a tunneled catheter exit site and tunnel and recognizes exit-site and tunnel infection', False),
                      ('Recognizes signs of central vein stenosis and access-related hand ischemia', False),
                      ('Writes or updates an ESKD Life-Plan with the current access, the next access and a review date', False),
                      ('Writes a referral that combines flow sheet trends and examination findings', False),
                      ('Teaches a ward team or family about vein preservation', False)],
            'placement': 'Supervised dialysis unit or ward rotation'},
 'quiz': [
  ('An intern is asked to draw blood from a patient with CKD stage 4 whose chart says &ldquo;save left arm.&rdquo; What is the best action?',
   ['Draw from the left cephalic vein because it is the easiest',
    'Use a hand vein on the right, or ask the nephrology team, and avoid the left arm veins',
    'Place a peripherally inserted central catheter (PICC) to avoid repeated punctures',
    'Draw from the left antecubital vein and apply pressure longer'],
   1,
   'KDOQI considers it reasonable to protect arm veins and avoid peripherally inserted central catheters (PICCs) and unnecessary venipunctures in CKD (expert opinion). A PICC injures arm and '
   'central veins and can ruin future access.'),
  ('A resident examines a fistula that is strongly pulsatile and stays distended when the arm is raised above the heart. Venous pressure alarms have increased. What is most likely?',
   ['Inflow stenosis at the arterial side', 'Outflow stenosis downstream of the needling segment',
    'A normal maturing fistula', 'Access-related hand ischemia'],
   1,
   'A narrowing downstream raises pressure upstream, so the vein becomes pulsatile and does not collapse on elevation. Inflow stenosis gives a flat, weak '
   'fistula with poor augmentation.'),
  ('A fellow plans access for a 45-year-old man with progressive CKD, eGFR 18 mL/min/1.73 m&sup2;, good forearm veins and no living donor. Which plan best follows KDOQI 2019?',
   ['Wait until he needs dialysis, then place a tunneled catheter',
    'Discuss his ESKD Life-Plan now, including peritoneal dialysis, and refer for access assessment with a documented plan for the next access',
    'Create an upper arm fistula first to ensure high flows',
    'Place a peripherally inserted central catheter (PICC) so that blood draws are easier until surgery'],
   1,
   'KDOQI suggests referral for access when eGFR is 15&ndash;20 (expert opinion) and an individualized, documented Life-Plan. A forearm fistula first preserves '
   'the upper arm; waiting for a catheter start is what the plan is meant to avoid.'),
  ('A patient with a tunneled catheter develops rigors and a temperature of 39&deg;C 20 minutes into dialysis. The exit site looks clean. What should the resident do first?',
   ['Continue dialysis and give paracetamol',
    'Take blood cultures before any antibiotic, stop or modify dialysis per protocol, and call the fellow and attending',
    'Remove the catheter at the bedside',
    'Assume it is a dialyzer reaction and change the dialyzer'],
   1,
   'Fever or rigors soon after connection suggests catheter-related bloodstream infection even with a clean exit site. Cultures come before antibiotics; '
   'removal and antibiotics are decided with the attending per IDSA guidance and the unit protocol.'),
  ('A resident presents the Ravani systematic review (62 cohort studies). Which statement is accurate?',
   ['It proved that switching a catheter to a fistula halves mortality',
    'Catheter use was associated with higher mortality than fistula use (risk ratio 1.53), with a high risk of selection bias',
    'Grafts and fistulas had identical mortality',
    'It was a randomized trial of 586,337 patients'],
   1,
   'The review pooled observational cohorts; sicker patients more often have catheters, so the association does not show the effect of switching a given '
   'patient. Grafts were also associated with higher mortality than fistulas (1.18).'),
 ],
 'terms': [('AV', 'Arteriovenous'), ('AVF', 'Arteriovenous fistula'), ('AVG', 'Arteriovenous graft'), ('CKD', 'Chronic kidney disease'),
           ('ESKD', 'End-stage kidney disease'), ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('eGFR', 'Estimated glomerular filtration rate'), ('PICC', 'Peripherally inserted central catheter'),
           ('IDSA', 'Infectious Diseases Society of America'), ('PSN', 'Philippine Society of Nephrology'),
           ('IPHN', 'International Pediatric Hemodialysis Network')],
 'readings': [('vascular-surgeon-02-the-lifetime-access-plan.html', 'Vascular Surgeon, Module 2: The lifetime access plan'),
              ('vascular-surgeon-03-examine-and-preserve-the-vessels.html', 'Vascular Surgeon, Module 3: Examine and preserve the vessels'),
              ('physician-on-duty-09-fistulas-and-grafts.html', 'Physician on Duty, Module 9: Fistulas and grafts'),
              ('physician-on-duty-10-catheters.html', 'Physician on Duty, Module 10: Catheters')],
 'calcs': ['calc-av-fistula-maturation.html', 'calc-access-flow-cardiac.html', 'calc-catheter-exposure.html', 'calc-hand-ischemia-dbi.html',
           'calc-access-infection-rate.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
