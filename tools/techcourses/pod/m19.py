# -*- coding: utf-8 -*-
"""Physician on Duty, Module 19: Bleeding and Heparin.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at a dialysis chair shines a penlight into the mouth of a patient whose tooth was pulled the day before, while a nurse waits with a heparin syringe held back.",
    "objectives": [
        "Explain why the dialysis circuit clots, how heparin prevents it, and why uremia, anemia, and other drugs add to the risk of bleeding.",
        "Run a bleeding-risk check before each session and escalate a patient who may need reduced or no heparin.",
        "Describe how a session with little or no heparin is run, and what it costs in clotting and lost treatment.",
        "Manage prolonged needle-site bleeding and recognize hidden bleeding in the gut, head, retroperitoneum, or access, following your unit&rsquo;s protocol.",
        "Recognize the timing and clues of heparin-induced thrombocytopenia and use the 4Ts score to decide when to call.",
        "Handle the patient who takes an anticoagulant or antiplatelet drug, or who has had a recent procedure, by asking the right questions and calling the attending nephrologist.",
    ],
    "big": """
{{plain:Blood in a glass test tube clots within minutes. Blood that flows through plastic tubing and a dialyzer behaves the same way. Heparin is the brake that keeps it liquid inside the tubing for the length of the session.}}
<p>The picture has a limit. The tubing is not a closed tube. Heparin flows back into the patient, so the brake also works in every fresh wound: a tooth socket, a biopsy site, a needle hole, an ulcer. The dose that protects the circuit can reopen a wound.</p>
{{cards:Key terms for this module|Unfractionated heparin::The usual blood thinner for the dialysis circuit. It acts within minutes and its effect fades over a few hours.|Antithrombin::A natural protein that switches off clotting enzymes. Heparin makes it work far faster.|Heparin-free dialysis::A session run with no systemic blood thinner, using other measures to keep the circuit open.|Uremic platelet dysfunction::Poor sticking and clumping of platelets in kidney failure, which prolongs bleeding.|Heparin-induced thrombocytopenia (HIT)::An immune reaction to heparin that lowers the platelet count and causes clots.|4Ts score::A bedside score that estimates how likely HIT is before any laboratory test.|Direct oral anticoagulant (DOAC)::A tablet blood thinner that blocks one clotting enzyme directly, such as apixaban or rivaroxaban.}}
<p>Most sessions run safely on the usual heparin order. A few patients arrive with a fresh wound, a hidden bleed, a new blood thinner, or a falling platelet count. Your work is to find those patients before the heparin is given, to control bleeding when it happens, and to call the attending nephrologist early. You report the risk; the nephrologist decides the dose.</p>
""",
    "case": {"title": "Dental extraction yesterday", "html": """
<p>Mrs. Corazon &ldquo;Cora&rdquo; Manalastas, 59, has dialyzed on Tuesdays, Thursdays, and Saturdays for four years through a left forearm fistula. She takes aspirin. Since a hospital stay last month for new atrial fibrillation, she also takes an anticoagulant prescribed by her cardiologist.</p>
<p>It is Thursday, 1:15 p.m., before needling. She mentions that two lower molars were pulled yesterday afternoon at a dental clinic in Malabon, and she spat a little blood overnight. The nurse, Mr. Jun Ramirez, has the standard heparin bolus drawn up. He has checked her vital signs and her mouth. One socket holds a small clot; the other is oozing slightly.</p>
<p>Her blood pressure is 142/80 mm Hg. Her heart rate is 92 per minute and irregular. Last week&rsquo;s monthly labs showed a hemoglobin of 9.6 g/dL and platelets of 188 &times; 10<sup>9</sup>/L. These are illustrative values, not targets.</p>
""", "questions": ["Should the heparin bolus be given as ordered, and who decides?",
                  "What three facts must you collect before you call the attending nephrologist?",
                  "If the session runs with little or no heparin, what will you watch for during it?"]},
    "sections": [
        ("heparin", "Why heparin", "Why the circuit clots and what heparin does", """
<p>Blood clots wherever it meets a surface that is not healthy vessel lining, and a dialysis circuit is meters of such surface.[[shen2012]][[daugirdas2015]]</p>
{{fig:pod19_clotting}}
<p>Three features push the blood toward clotting. Plastic and membrane surfaces start the contact pathway, and platelets stick to them. Blood slows and swirls in the venous chamber, where it also meets air. And the dialyzer removes water, so blood thickens inside the fibers. Each leads to thrombin, the enzyme that turns fibrinogen into fibrin strands, which with platelets block the fibers one by one.</p>
<p>Heparin binds antithrombin, a natural brake on clotting, and makes it act far faster against thrombin and factor Xa. The effect is greatest during dialysis and fades over the hours after it. That is why needle sites bleed at the end of a session, and why a wound can bleed again that evening.</p>
<h3>Why the dialysis patient bleeds more easily</h3>
<p>Module 4 explained that uremic platelets stick and clump poorly, and that dialysis only partly corrects this. Anemia adds to it. Red cells crowd the center of flowing blood and push platelets toward the wall, so with fewer red cells, fewer platelets reach an injury. Raising the hematocrit improves the bleeding time, a laboratory surrogate for bleeding risk.[[kaw2006]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Factor</th><th>What it does</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>Circuit surface and slow flow</td><td>Starts clotting inside the circuit</td><td>Dark streaks in the dialyzer, clot in the venous chamber, rising circuit pressures</td></tr>
<tr><td>Heparin</td><td>Blocks thrombin in the circuit and in the patient</td><td>Longer bleeding from needle sites and fresh wounds</td></tr>
<tr><td>Uremic platelets</td><td>Weak sticking and clumping</td><td>Oozing from small wounds, easy bruising</td></tr>
<tr><td>Anemia</td><td>Fewer platelets pushed toward the vessel wall</td><td>More oozing when hemoglobin is low</td></tr>
<tr><td>Other drugs</td><td>Aspirin, clopidogrel, warfarin, and the DOACs add their own brake</td><td>Bleeding that is out of proportion to the wound</td></tr>
</tbody></table></div>
<h3>How much heparin, and who decides</h3>
<p>No heparin regimen for maintenance hemodialysis is supported by trials. Units use weight-based, fixed, or low-dose schedules and change them on clinical signs.[[shen2012]] One United States program moved 66 patients to a low-dose protocol and compared before with after. Heparin per session fell by more than half. The urea reduction ratio (URR), a surrogate for dialysis dose, was 73.0% on the low dose and 71.2% on the standard dose.[[murea2018]] Moderate dialyzer clotting rose slightly. The study was not randomized and did not test bleeding or survival. It shows that a lower dose can keep the circuit working, not that it is safer.</p>
<p>Learn your unit&rsquo;s standard order and who may change it. You do not change the dose. You notice when the balance has shifted and say so before the bolus is given.</p>
{{key:Heparin protects the circuit and threatens every fresh wound in the patient. Ask about wounds before every session.}}
"""),
        ("riskcheck", "Bleeding-risk check", "The bleeding-risk check before each session", """
<p>Think of the check as a gate: five questions between the patient and the heparin bolus. Five &ldquo;no&rdquo; answers let the usual order go ahead. Any &ldquo;yes&rdquo; holds the bolus until the attending nephrologist has heard.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gate question</th><th>Why it matters</th><th>What to look for or ask</th></tr></thead>
<tbody>
<tr><td>1. Any surgery, biopsy, tooth extraction, or catheter insertion in the past few days?</td><td>A fresh wound holds only a young clot, and heparin stops it from growing firm</td><td>Date and time of the procedure, sutures or packing, oozing now</td></tr>
<tr><td>2. Any active or recent bleeding?</td><td>Heparin adds to bleeding that has already started</td><td>Black stool, vomiting blood, nosebleed, blood in urine, needle sites that bled long last session</td></tr>
<tr><td>3. Any fall or head injury?</td><td>Bleeding inside the skull can build slowly over hours to days</td><td>Headache, drowsiness, confusion, new weakness, bruises on the head</td></tr>
<tr><td>4. Any new anticoagulant or antiplatelet drug?</td><td>The session heparin adds to the brake the patient already takes</td><td>Drug name, dose, time of the last dose, who prescribed it</td></tr>
<tr><td>5. Low platelets or a large hemoglobin drop on the latest labs?</td><td>Few platelets, or a fall in hemoglobin, may signal a bleed or HIT</td><td>Compare with the previous result, not only with the normal range</td></tr>
</tbody></table></div>
<p>The gate is a teaching tool built from the risks that sources on heparin describe, not a validated score.[[shen2012]][[kaw2006]] If your unit&rsquo;s protocol has its own version, use it.</p>
<h3>Why the gut deserves its own question</h3>
<p>Upper gastrointestinal (GI) bleeding is the hidden bleed you are most likely to meet. In a United States Renal Data System (USRDS) cohort, 698 first admissions for upper GI bleeding occurred over 30,648 patient-years. After adjustment, cardiovascular disease (relative risk 1.32), current smoking (1.11), and inability to walk independently (1.32) were associated with bleeding. Aspirin, antiplatelet, and anticoagulant use were not significantly associated, but this 1990s cohort was not designed to test drug effects, so it does not show that blood thinners are safe.[[wasse2003]] Among 50,497 episodes of nonvariceal upper GI bleeding in dialysis patients, 30-day mortality was 10.7%.[[yang2013]] Both studies were observational. They support asking about black stool at every session.</p>
{{flow:Heparin decision at the chair|Ask the five questions::With the nurse, before the heparin syringe is opened. Record each answer.|All answers no::The usual heparin order goes ahead.|Any answer yes::Hold the bolus. Do not needle yet if bleeding is active or the patient looks unwell.|Look and measure::Vital signs, the wound, the needle sites, the latest hemoglobin and platelets.|Call the attending nephrologist::Report the yes answers, what you saw, and the drugs with their last doses.|Follow the plan given::Record the plan and who decided.}}
{{formula:<strong>Worked example A. Bleeding-risk sort before the bolus (illustrative walk-through).</strong><br>Mrs. Manalastas, from the opening case.<br>1. Procedure in the past few days: yes (two molars pulled about 21 hours ago).<br>2. Active bleeding: yes (oozing from one socket).<br>3. Fall or head injury: no.<br>4. Anticoagulant or antiplatelet drug: yes (an anticoagulant started last month, plus aspirin).<br>5. Low platelets or hemoglobin drop: no (platelets 188 &times; 10<sup>9</sup>/L).<br>Result: three yes answers, one of them active oozing. She sits in the &ldquo;call before heparin&rdquo; lane of the flow above.<br>What this tells you: the bolus waits and the nephrologist is called now. What it does not tell you: whether she needs a reduced dose, no heparin, or a different method. That choice is the nephrologist&rsquo;s.}}
{{call:Stop and call the attending nephrologist before any heparin is given when any gate answer is yes. If you cannot reach the nephrologist, follow the unit&rsquo;s escalation list. Do not give the standard bolus to fill the gap.}}
"""),
        ("heparinfree", "Little or no heparin", "Running a session with little or no heparin", """
<p>Picture a river in winter. Moving water does not freeze; water pooled at the edges does. A session without heparin keeps the blood moving, rinses where it pools, and uses surfaces that clot less.</p>
{{fig:pod19_heparinfree}}
<p>Methods vary by unit, and your unit&rsquo;s protocol sets every number.[[shen2012]][[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Method</th><th>How it keeps the circuit open</th><th>Limits</th></tr></thead>
<tbody>
<tr><td>Higher blood flow, as the prescription allows</td><td>Less time for blood to stand still in the circuit</td><td>Limited by the access and the patient</td></tr>
<tr><td>Saline flushes at set times</td><td>Rinses the dialyzer and lets staff see early clotting</td><td>The flush volume must be removed again as fluid</td></tr>
<tr><td>Low-clotting or heparin-grafted dialyzer</td><td>Membrane surface starts less clotting</td><td>Cost and supply</td></tr>
<tr><td>Citrate-containing dialysis fluid</td><td>Citrate binds calcium, which clotting needs, at the membrane</td><td>Availability in the Philippines varies; ask your unit</td></tr>
<tr><td>Regional citrate in the circuit</td><td>Citrate infused before the dialyzer, calcium replaced after it</td><td>Needs close monitoring; mainly a hospital method</td></tr>
</tbody></table></div>
<h3>What the evidence shows</h3>
<p>In 12,468 older United States patients starting hemodialysis, 836 (6.7%) were dialyzed heparin-free. A history of bleeding and lower hemoglobin and platelets made it more likely. Heparin-free dialysis was not associated with less bleeding (hazard ratio [HR] 1.15, 95% confidence interval [CI] 0.83 to 1.60), nor with more thrombosis or death.[[shen2013]] The cohort was observational, and patients went heparin-free because they were already at risk, so the comparison is confounded. Omitting heparin is no guarantee of safety.</p>
<p>Two small randomized crossover trials tested methods. EvoCit dialyzed 26 patients with a heparin-grafted dialyzer, with citrate-enriched dialysis fluid and no systemic heparin or with heparin. Kt/V, a surrogate for dialysis dose, was 1.47 versus 1.50, which met the noninferiority margin, but 4.2% of heparin-free sessions ended early for clotting, against none with heparin.[[francois2022]] The SAFE pilot used an asymmetric triacetate dialyzer without anticoagulant in 20 patients. With citrate-containing dialysis fluid, 90.8% of sessions finished without early clotting; with predilution hemodiafiltration, 83.3% did.[[vandenbosch2021]] Neither trial measured bleeding or death. A heparin-free method keeps most sessions running, and the minority that clot cost blood and treatment time.</p>
<p>Watch for steadily rising venous or transmembrane pressure, dark streaks during a flush, and a growing clot in the venous chamber. Module 16 covers the clotted circuit. Your part is to see the trend and call before the circuit is lost.</p>
{{formula:<strong>Worked example B. Blood lost with a clotted circuit (illustrative arithmetic, not a device value).</strong><br>Method: red-cell volume lost = blood volume in the circuit &times; hematocrit.<br>Suppose the dialyzer and lines hold about 150 mL of blood (illustrative; the real volume is printed on the dialyzer and line set labels).<br>Hematocrit 30% (illustrative).<br>Red-cell volume lost = 150 mL &times; 0.30 = 45 mL, plus about 105 mL of plasma.<br>Two clotted circuits in a month = about 90 mL of red cells.<br>What this tells you: why repeated clotting matters in anemia (Module 21). What it does not tell you: whether this patient needs any change in treatment.}}
{{call:Stop and call the attending nephrologist when pressures rise steadily or clot appears in a session with little or no heparin, and before any decision to end the session early. Report the time into the session and the treatment delivered so far.}}
"""),
        ("needles", "Needle-site bleeding", "Bleeding after the needles come out", """
<p>Every needle leaves two holes, one in the skin and one in the vessel wall, a short distance apart because the needle enters at an angle. Pressure on the skin hole alone can leave the vessel hole bleeding.</p>
{{fig:pod19_twoholes}}
<p>Module 9 teaches the technique: two fingertips and a small gauze over both holes, firm enough to stop the bleeding while a thrill remains, with no tourniquet.[[kcuk_bleed]] This module asks why one patient bleeds longer than usual.</p>
{{fig:pod09_pressure}}
<h3>Why a needle site keeps bleeding</h3>
<p>Platelets plug the hole, and fibrin knits the plug into a firm clot. Anything that weakens either step, or pushes harder against the plug, prolongs bleeding.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Likely cause</th><th>What you report</th></tr></thead>
<tbody>
<tr><td>Both sites bleed long, in one session only</td><td>More heparin effect than usual: a mid-session dose, a short session, or a new blood thinner</td><td>The heparin given and its timing; any new drug</td></tr>
<tr><td>Both sites bleed long, session after session</td><td>Uremic platelets, anemia, or a heparin order that no longer fits</td><td>The pattern, the latest hemoglobin and platelets</td></tr>
<tr><td>The venous site bleeds long, again and again</td><td>A narrowing downstream raises pressure in the access (Module 9)</td><td>The pattern, the thrill and bruit, any change in venous pressure during dialysis</td></tr>
<tr><td>Bleeding through thin, shiny skin or a scab</td><td>A weakened wall over an aneurysm or an infected site</td><td>Urgently, as a possible impending rupture</td></tr>
</tbody></table></div>
<p>Reviews of dialysis emergencies put pressure first and the search for a cause second. Their advice rests on experience, not trials.[[greenberg2021]][[saha2017]]</p>
{{flow:Bleeding after needle removal|Press on the right spot::Two fingertips and a small gauze over the skin hole and the vessel hole.|Hold for the set time::Press for the time your unit&rsquo;s protocol sets, without lifting to look.|Check::Lift gently. Look for oozing, and feel for the thrill.|Still bleeding::Press again for the set time. Check vital signs. Ask about blood thinners and recent wounds.|Bleeding not controlled::Keep pressing. Call for help and call the attending nephrologist at once.}}
<p>A single long bleed needs a note: time pressed, the thrill afterward, and the heparin given. A pattern needs a report.</p>
{{call:Stop and call when correct pressure does not control the bleeding, when blood spurts from an access, or when bleeding comes with a fall in blood pressure or a rising pulse. Keep pressing while someone else calls. Module 9 covers the response to a ruptured access.}}
"""),
        ("hidden", "Hidden bleeding", "Bleeding you cannot see", """
<p>Some bleeding happens out of sight: into the gut, the skull, the space behind the abdomen, or the tissues around the access. You find it by its effects.</p>
{{fig:pod19_hidden}}
<h3>How a hidden bleed shows itself</h3>
<p>Blood loss lowers the volume returning to the heart, so the pulse rises and the vessels tighten. Fluid removal pulls the same way. The pressure falls earlier and further than the fluid removed explains. Module 13 covers the falling pressure; a hidden bleed is one of its dangerous causes.</p>
<div class="table-wrap"><table>
<thead><tr><th>Site</th><th>Clues at the chair</th><th>First move, while you call</th></tr></thead>
<tbody>
<tr><td>Upper or lower gut</td><td>Black, tarry stool. Vomiting blood or coffee-ground material. Pallor, fast pulse, dizziness on sitting up</td><td>Stop heparin per protocol. Vital signs. Urgent hemoglobin per protocol. Prepare for transfer</td></tr>
<tr><td>Head</td><td>Headache, drowsiness, confusion, vomiting, or new weakness, especially after a fall</td><td>Stop heparin per protocol. Level of consciousness and pupils. Urgent transfer for imaging</td></tr>
<tr><td>Retroperitoneum, the space behind the abdomen</td><td>Back, flank, or groin pain, often after a femoral catheter or a procedure. A falling pressure</td><td>Stop heparin per protocol. Vital signs. Urgent transfer</td></tr>
<tr><td>Access arm</td><td>A tense, growing swelling or bruise around the access, often after a missed needle</td><td>Pressure, as Module 9 describes. Check the thrill. Call</td></tr>
<tr><td>The circuit</td><td>A dislodged needle or an open connection, often under a blanket</td><td>Module 16. Stop the blood pump and press on the site</td></tr>
</tbody></table></div>
{{fig:pod16_hidden|The circuit can hide a bleed too. Module 16 covers the dislodged needle.}}
<p>The Glasgow-Blatchford score helps sort suspected upper GI bleeding. One of its items is blood urea, which is high in every dialysis patient, so the score overstates risk. Treat it as context for your call.</p>
<h3>Treating the platelet defect is the nephrologist&rsquo;s call</h3>
<p>The nephrologist may treat the platelet defect itself. Desmopressin raises factor VIII and large von Willebrand factor proteins, which help platelets stick. In a randomized, double-blind crossover trial of 12 patients with uremia, it shortened the bleeding time in all of them, for at least four hours in most.[[mannucci1983]] Bleeding time is a surrogate, not blood loss. Reviews also describe conjugated estrogens, cryoprecipitate, more effective dialysis, and correction of anemia, which differ in onset and duration.[[hedges2007]][[kaw2006]] The evidence is small, and the choice is the nephrologist&rsquo;s.</p>
<p>For any hidden bleed: stop the heparin per protocol, assess, stop fluid removal if the pressure is falling, and call. Instability or a suspected head or internal bleed usually means ending the session and transfer.</p>
{{call:Stop and call the attending nephrologist at once, and arrange transfer to the emergency room, for any suspected internal bleed, any head injury in a patient on an anticoagulant or antiplatelet drug, or any bleed with a falling pressure and rising pulse. Do not wait for the hemoglobin result before you call.}}
{{key:A pressure that falls faster than the fluid removed explains, with a rising pulse, is a bleed until proved otherwise.}}
"""),
        ("hit", "HIT", "Heparin-induced thrombocytopenia: timing and clues", """
<p>In a few patients, the immune system tags heparin bound to a platelet protein, platelet factor 4. The antibodies coat platelets and switch them on. Activated platelets release clotting signals and are cleared from the blood, so the count falls while clots form. Fewer platelets with more clotting is the core of heparin-induced thrombocytopenia (HIT).[[cuker2018]]</p>
<p>The dialysis unit meets HIT mainly in the new patient who received heparin in hospital, or in a patient restarting heparin after a recent exposure. A patient who has dialyzed on heparin for years is past the usual window, so a new fall in platelets more often has another cause.</p>
<div class="table-wrap"><table>
<thead><tr><th>The T</th><th>What it asks</th><th>In the dialysis unit</th></tr></thead>
<tbody>
<tr><td>Thrombocytopenia</td><td>How far the platelet count fell, and how low it went</td><td>Compare with the count before heparin, not with the normal range</td></tr>
<tr><td>Timing</td><td>When the fall began, counted from the start of heparin</td><td>Typically 5 to 10 days after heparin starts, sooner after a recent exposure. Ask about heparin in hospital</td></tr>
<tr><td>Thrombosis</td><td>New clots or other complications</td><td>A newly clotted access or catheter, repeated circuit clotting, a swollen leg, skin lesions at injection sites</td></tr>
<tr><td>Other causes</td><td>Whether another explanation is more likely</td><td>Infection, other drugs, bleeding, liver disease, a laboratory clump</td></tr>
</tbody></table></div>
<p>Each T scores 0, 1, or 2 points. A total of 0 to 3 is low probability, 4 to 5 intermediate, and 6 to 8 high.[[lo2006]] Use the site&rsquo;s 4Ts calculator, which carries the point definitions, rather than scoring from memory.</p>
<h3>What the score can and cannot do</h3>
<p>Lo and colleagues tested the 4Ts prospectively in 100 patients in a Canadian hospital and 236 referred to a German laboratory. Only 1 of 64 and 0 of 55 low-score patients had clinically significant antibodies. Intermediate scores carried antibodies in 28.6% and 7.9%, and high scores in 100% and 21.4%.[[lo2006]] A low score rules HIT out well. A higher score raises suspicion, but its meaning varied between settings.</p>
<p>The American Society of Hematology (ASH) 2018 guideline, built with the Grading of Recommendations Assessment, Development and Evaluation (GRADE) method, makes strong recommendations to use the 4Ts score rather than clinical impression alone, and to avoid HIT testing and empiric treatment when the score is low. The choice among non-heparin anticoagulants carries conditional recommendations, and the guideline addresses renal replacement therapy in acute HIT.[[cuker2018]]</p>
{{formula:<strong>Worked example C. Reading the 4Ts (illustrative values).</strong><br>A new patient&rsquo;s platelet count is 210 &times; 10<sup>9</sup>/L before heparin. On day 7 of heparin exposure it is 85 &times; 10<sup>9</sup>/L. Her graft clotted yesterday. No infection, new drug, or other cause has been found.<br>Thrombocytopenia: the fall is 125 &divide; 210 = about 60%, and the lowest count is well above 20 &times; 10<sup>9</sup>/L.<br>Timing: day 7, inside the typical window.<br>Thrombosis: a new clot in the access.<br>Other causes: none found.<br>Enter each item in the 4Ts calculator. With any reasonable reading of the thrombosis item, the total falls in the high band (6 to 8).<br>What this tells you: every heparin source stops now, and the nephrologist is called today. What it does not tell you: that she has HIT. Only laboratory testing, an antibody test and, where available, a functional test, can support that.}}
{{call:Stop and call the attending nephrologist the same day for an intermediate or high 4Ts score, or for a falling platelet count with a new clot. Have every source of heparin held per protocol while you call.}}
{{key:When HIT is possible, every source of heparin stops, including the catheter lock and flushes.}}
<p>Heparin also hides in catheter locks, line flushes, and some coated devices. Ask the nurse to name each one. The replacement anticoagulant and catheter lock are chosen by the attending nephrologist, often with a hematologist.</p>
"""),
        ("thinners", "Blood thinners and procedures", "Blood thinners, antiplatelets, and recent procedures", """
<p>The session heparin adds to whatever brake the patient already takes. Your questions tell the nephrologist how hard that brake is pressed.</p>
<div class="table-wrap"><table>
<thead><tr><th>Drug class</th><th>Examples</th><th>What to ask</th><th>What the dialysis evidence shows</th></tr></thead>
<tbody>
<tr><td>Antiplatelet drugs</td><td>Aspirin, clopidogrel</td><td>Why it was started. Any coronary stent, and when</td><td>Stopping after a recent stent carries its own danger; never stop it yourself</td></tr>
<tr><td>Vitamin K antagonist</td><td>Warfarin</td><td>Last dose. Latest international normalized ratio (INR) and its date</td><td>In RENAL-AF, warfarin was in the target range only 44% of the time[[pokorney2022]]</td></tr>
<tr><td>Direct oral anticoagulants (DOACs)</td><td>Apixaban, rivaroxaban, dabigatran</td><td>Which drug, what dose, time of the last dose</td><td>Apixaban is barely removed by dialysis.[[mavrakanas2017]] Dabigatran is cleared mainly by the kidneys and builds up</td></tr>
<tr><td>Injected heparins</td><td>Enoxaparin</td><td>Why it was given, last dose</td><td>Cleared by the kidneys, so its effect lasts longer in kidney failure</td></tr>
</tbody></table></div>
<h3>What the trials in dialysis show</h3>
<p>Apixaban is the DOAC best studied in hemodialysis. In a pharmacokinetic study of 7 patients, the reduced dose gave exposure similar to the standard dose in people with normal kidney function. The standard dose, taken by 5 of them, gave levels above that range. Only 4% of the drug was removed by a dialysis session.[[mavrakanas2017]] The study measured drug levels, not bleeding or strokes.</p>
<p>Two randomized trials followed. RENAL-AF compared apixaban at the standard dose, or the reduced dose for older or lighter patients, with warfarin in 154 hemodialysis patients with atrial fibrillation. It stopped early because enrollment was slow. At one year, major or clinically relevant nonmajor bleeding occurred in 32% with apixaban and 26% with warfarin (HR 1.20, 95% CI 0.63 to 2.30). Stroke or systemic embolism occurred in 3.0% and 3.3%. The trial was underpowered.[[pokorney2022]] AXADIA-AFNET 8 randomized 97 patients to reduced-dose apixaban or phenprocoumon, a warfarin-like drug. Major bleeding, clinically relevant nonmajor bleeding, or death occurred in 45.8% and 51.0% (HR 0.93, 95% CI 0.53 to 1.65). No outcome differed.[[reinecke2023]]</p>
<p>A 2026 target trial emulation, an observational analysis designed to mimic a trial, matched 3,978 new apixaban users with 3,978 new warfarin users on hemodialysis. Apixaban was associated with lower rates of ischemic stroke (HR 0.66, 95% CI 0.47 to 0.94) and clinically important bleeding (HR 0.72, 95% CI 0.63 to 0.83). Death did not differ. Patients stayed on apixaban for a median of only 58 days, and residual confounding remains possible.[[winkelmayer2026]]</p>
<p>The sources do not agree. The randomized trials were too small to detect modest differences, and the large favorable data are observational. Whether any oral anticoagulant helps a dialysis patient with atrial fibrillation remains unsettled. A Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference framed this uncertainty in a conference statement, not a graded recommendation.[[turakhia2018]] Modules 15 and 20 cover atrial fibrillation and prescribing. The HAS-BLED calculator gives context, but it was not developed in dialysis patients.</p>
<h3>Recent procedures</h3>
<p>No trial tells us how long to reduce or hold heparin after a dental extraction, biopsy, catheter insertion, or minor surgery. Units set this by protocol. Ask the date and time of the procedure, whether sutures or packing were used, and whether the wound is oozing now.</p>
{{call:Stop and call the attending nephrologist before heparin is given for any new anticoagulant or antiplatelet drug, and for any procedure in the past few days. Never stop or hold a patient&rsquo;s anticoagulant or antiplatelet drug on your own.}}
<h3>The call card</h3>
<p>Be exact about the circuit blood. Returning it helps a bleeding patient. It is wrong only when the blood or the circuit is unsafe.</p>
{{flow:Call card: bleeding and heparin|Recognize::Oozing that will not stop. Blood in the mouth, stool, or vomit. A falling pressure with a rising pulse. Headache or drowsiness after a fall. A swelling access arm. Falling platelets with new clots.|First 2 minutes::Correct pressure on any external site. Vital signs. Check the thrill. Ask about procedures, falls, and blood thinners with their last doses. Check the latest hemoglobin and platelets.|Stop dialysis?::Stop heparin per protocol for any active bleeding. End the session, with the nephrologist, for instability, a suspected internal or head bleed, or access bleeding that pressure does not control.|Return the blood?::Yes, when the circuit is intact and the patient can take the volume. Returning blood helps a bleeding patient. Do NOT return the blood if the circuit has clotted, if air or hemolysis is suspected, or if the circuit has been opened or contaminated (Module 16). A ruptured access cannot take the blood back; keep pressing.|Call::The attending nephrologist, at once. The emergency room for a suspected internal bleed, a head injury on a blood thinner, or instability. The surgeon or access team for a ruptured access.|Write::What bled, where, and for how long. Heparin given and when. Each blood thinner and its last dose. Vital signs. Pressure time. Who was called, when, and what was advised. Where the patient went.}}
"""),
    ],
    "debrief": ["""
<p><strong>Should the bolus be given as ordered, and who decides?</strong> No, not yet. Mrs. Manalastas answers yes to three gate questions: a procedure less than a day ago, a socket that is still oozing, and two drugs that already slow clotting. The standard bolus would reach her sockets within minutes, while their young clots are weakest. You ask Mr. Ramirez to hold the bolus and the needling until the plan is clear. The heparin decision belongs to the attending nephrologist. Your job is to make sure it is made with the facts in hand, before the syringe is emptied.</p>
<p><strong>What three facts must you collect before you call?</strong> First, the anticoagulant: its name, the dose, and the exact time of the last tablet. Second, the wound: when the teeth were pulled, whether sutures or packing were used, and how much she is oozing now, which you check yourself with a penlight and gauze. Third, her current state: blood pressure, pulse, signs of blood loss elsewhere, and the latest hemoglobin and platelets. You report this in the SBAR format from Module 1: Situation, Background, Assessment, Recommendation.</p>
<p><strong>If she dialyzes with little or no heparin, what will you watch?</strong> The circuit and the mouth. Steadily rising venous or transmembrane pressure, dark streaks during a flush, or a growing clot in the venous chamber are early signs of clotting, and you call before the circuit is lost. Her own anticoagulant still acts, so you check the socket during the session and the needle sites after removal. Before she leaves, the sites and socket are dry, and she knows what to do if bleeding starts at home.</p>
"""],
    "skills": {"title": "Pre-session bleeding-risk check and access hemostasis",
               "intro": "Perform this check on a simulated patient or a colleague in a dialysis chair while your preceptor observes and plays the nurse. Then demonstrate hemostasis on a training arm or describe it step by step.",
               "items": [
                   ("Asks the five gate questions before heparin is given and records each answer.", True),
                   ("Looks for active bleeding in the mouth, nose, needle sites, and catheter exit, and reviews the latest hemoglobin and platelets.", False),
                   ("Records every anticoagulant or antiplatelet drug by name, with the time of the last dose.", True),
                   ("Calls the attending nephrologist before heparin when any gate answer is yes.", True),
                   ("After needle removal, applies firm two-finger pressure with a small gauze over the vessel hole as well as the skin hole, with no tourniquet.", False),
                   ("Keeps pressure for the unit&rsquo;s set time without lifting to check.", False),
                   ("Checks for a thrill after bleeding stops.", True),
                   ("Recognizes bleeding that correct pressure does not control, and escalates at once.", True),
                   ("Names the signs of internal bleeding: a falling pressure, a rising pulse, black stool, abdominal or back pain, and headache or drowsiness after a fall.", False),
                   ("Uses the 4Ts calculator for a falling platelet count and states that every source of heparin stops when HIT is possible, including catheter locks and flushes.", True),
                   ("States when the blood in the circuit must not be returned.", True),
                   ("Documents the bleeding event, the pressure time, the heparin given, and the calls made.", False),
               ],
               "placement": "For two weeks, join the nurse at the start of each session on your shifts and run the five gate questions with each patient before heparin is given. Keep a log of every yes answer, what was found, and the plan the attending nephrologist gave. Review the log with your preceptor and identify one gate question that patients often answer wrongly at first."},
    "quiz": [
        ("How does heparin prevent clotting in the dialysis circuit?",
         ["It dissolves fibrin that has already formed",
          "It makes antithrombin switch off thrombin and factor Xa much faster",
          "It blocks platelets from sticking to plastic",
          "It removes calcium from the blood"], 1,
         "Heparin works through antithrombin. It prevents new fibrin but does not dissolve existing clot."),
        ("Why does anemia add to bleeding in a dialysis patient?",
         ["Red cells release heparin",
          "Low hemoglobin lowers the platelet count",
          "With fewer red cells in the center of the stream, fewer platelets are pushed toward the vessel wall",
          "Anemia makes the dialyzer remove clotting factors"], 2,
         "Red cells push platelets toward the vessel wall."),
        ("What did the low-dose heparin study by Murea and colleagues show?",
         ["Low-dose heparin reduced bleeding deaths",
          "Low-dose heparin caused frequent circuit loss",
          "Heparin per session fell by more than half while the urea reduction ratio was maintained, in a before-and-after comparison",
          "Weight-based dosing is the proven standard"], 2,
         "A nonrandomized study that did not test bleeding or survival."),
        ("A man arrives for dialysis and mentions that a skin lesion was removed from his back this morning. The wound is dry under a dressing. What do you do before the heparin bolus?",
         ["Give the usual bolus because the wound is dry",
          "Give half the usual bolus",
          "Treat the procedure as a yes on the gate and call the attending nephrologist before heparin",
          "Cancel the session"], 2,
         "A recent procedure is a yes even when the wound looks dry."),
        ("In the USRDS cohort studied by Wasse and colleagues, which factor was associated with upper GI bleeding after adjustment?",
         ["Cardiovascular disease",
          "Aspirin use",
          "Peritoneal dialysis",
          "Female sex"], 0,
         "Cardiovascular disease, smoking, and inability to walk independently were associated with bleeding."),
        ("In the cohort of 12,468 patients described by Shen and colleagues, how was heparin-free dialysis related to bleeding?",
         ["It cut bleeding by half",
          "It was not associated with less bleeding, but patients went heparin-free because they were already at risk",
          "It doubled bleeding",
          "It was associated with fewer strokes"], 1,
         "The bleeding hazard ratio was 1.15, and confounding limits any conclusion."),
        ("A woman is on a heparin-free session after a biopsy. In hour two the venous pressure has risen steadily, and dark streaks appear in the dialyzer during a flush. What is the best next step?",
         ["Give a heparin bolus to save the circuit",
          "Ignore the change until an alarm sounds",
          "Raise the fluid removal goal",
          "Call the attending nephrologist now, before the circuit clots, and follow the unit&rsquo;s protocol"], 3,
         "These are early signs of clotting. An early call saves blood and treatment time."),
        ("What did the EvoCit trial show about a heparin-grafted dialyzer with citrate-enriched dialysis fluid and no systemic heparin?",
         ["It was noninferior for Kt/V, but 4.2% of sessions ended early for clotting",
          "It reduced deaths",
          "It never clotted",
          "It was inferior for Kt/V"], 0,
         "Kt/V is a surrogate, and clinical outcomes were not measured."),
        ("At the end of Mrs. Lim&rsquo;s session, her arterial needle site keeps oozing after removal. How should it be pressed?",
         ["A tourniquet above the access",
          "A thick towel pressed over the whole forearm",
          "Two fingertips and a small gauze over the vessel hole and the skin hole, lifted every minute to check",
          "Two fingertips and a small gauze over the vessel hole and the skin hole, held for the set time without lifting"], 3,
         "Lifting early breaks the forming clot."),
        ("For three sessions in a row, a man&rsquo;s venous needle site in his graft has bled long after correct pressure. What does this pattern most suggest?",
         ["A narrowing downstream that raises pressure in the graft",
          "Too little heparin",
          "A normal finding in grafts",
          "Low blood pressure"], 0,
         "This points to outflow stenosis. Report it for access assessment."),
        ("A 70-year-old woman on dialysis has a pressure that falls faster than her fluid removal explains, and her pulse has risen from 80 to 110 per minute. She mentions black stools this week. What do you do?",
         ["Give fluid and continue the session unchanged",
          "Stop heparin per protocol, assess, call the attending nephrologist, and prepare for transfer",
          "Increase the blood pump speed",
          "Wait for the hemoglobin result before calling"], 1,
         "This suggests upper GI bleeding. Do not wait for laboratory results to call."),
        ("Why should the Glasgow-Blatchford score be read with care in a dialysis patient?",
         ["It was designed for children",
          "It ignores the pulse",
          "Its blood urea item is high in every dialysis patient, so the score overstates risk",
          "It requires an endoscopy first"], 2,
         "The score is context, not a decision."),
        ("A man started dialysis 9 days ago after a hospital stay with heparin injections. His platelets have fallen from 230 to 95 &times; 10<sup>9</sup>/L, and his catheter clotted. The 4Ts score is high. What happens to heparin?",
         ["Only the bolus is stopped",
          "Heparin continues at a lower dose",
          "Heparin continues until the antibody test returns",
          "Every source stops, including catheter locks and flushes, and the nephrologist is called the same day"], 3,
         "When HIT is possible, all heparin stops."),
        ("In the study by Lo and colleagues, what did a low 4Ts score show?",
         ["It confirmed HIT",
          "It ruled HIT out well in both settings",
          "It had no predictive value",
          "It meant the same in every hospital as a high score"], 1,
         "Low-score patients almost never had significant antibodies."),
        ("What is the best summary of the evidence on oral anticoagulants for hemodialysis patients with atrial fibrillation?",
         ["Large trials prove apixaban prevents strokes",
          "Warfarin is proven superior",
          "Small, inconclusive trials and favorable observational data",
          "Anticoagulants are proven harmful"], 2,
         "The trials were underpowered; the 2026 analysis was observational."),
    ],
    "terms": [("Unfractionated heparin", "The usual blood thinner for the dialysis circuit. It works through antithrombin and fades over a few hours."),
              ("Antithrombin", "A natural protein that switches off thrombin and factor Xa. Heparin speeds its action."),
              ("Heparin-free dialysis", "A session run with no systemic blood thinner, using flushes, blood flow, and special dialyzers or dialysis fluid instead."),
              ("Uremic platelet dysfunction", "Weak sticking and clumping of platelets in kidney failure, which prolongs bleeding."),
              ("Bleeding time", "A test of how long a small standard cut bleeds. It is a surrogate, not a measure of blood loss."),
              ("Heparin-induced thrombocytopenia (HIT)", "An immune reaction to heparin bound to platelet factor 4 that lowers the platelet count and causes clots."),
              ("4Ts score", "A bedside score of thrombocytopenia, timing, thrombosis, and other causes that estimates the likelihood of HIT."),
              ("Direct oral anticoagulant (DOAC)", "A tablet blood thinner that directly blocks thrombin or factor Xa, such as dabigatran, apixaban, or rivaroxaban."),
              ("Retroperitoneum", "The space behind the abdominal cavity, where bleeding can collect without visible signs."),
              ("Target trial emulation", "An observational analysis designed to mimic a randomized trial using registry or claims data.")],
    "readings": [("hemodialysis-complications.html", "An overview of problems during dialysis, including bleeding and clotting."),
                 ("dialysis-access-care.html", "Care of the access, including needle-site bleeding and when to seek help."),
                 ("hemodialysis-access-lifeline.html", "How fistulas and grafts work and the warning signs of trouble.")],
    "calcs": ["calc-4ts-hit.html", "calc-glasgow-blatchford.html", "calc-has-bled.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
