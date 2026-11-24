# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How the marrow, erythropoietin and iron work together, why the hemoglobin target sits below normal, what the big trials showed, when a falling hemoglobin is bleeding rather than a dose step, what a protocol does and does not authorize, and how to make every injection reliable.",
    "desc": "Special Dialysis Nurse Roles Module 9: the anemia management and medication safety nurse in hemodialysis. Renal anemia physiology, KDIGO 2026, TREAT and PIVOTAL trial evidence, red flags, protocol authority, ESA and IV iron administration safety, response and adverse-event tracking.",
    "keywords": "anemia nurse dialysis, renal anemia erythropoietin iron, KDIGO 2026 anemia guideline, TREAT trial darbepoetin stroke, PIVOTAL trial IV iron hemodialysis, ESA administration safety, hemoglobin falling dialysis bleeding",
    "image_alt": "A Filipino dialysis nurse reviewing a printed hemoglobin trend chart at a patient's chair while the patient describes his symptoms.",
    "objectives": [
        "Explain renal anemia as a causal chain of erythropoietin deficiency, iron availability, inflammation and blood loss, and organize trends to show it.",
        "Recognize findings that need prescriber review now rather than a protocol step, including signs of bleeding.",
        "State what a physician-authorized plan permits and apply it without independent prescribing.",
        "Prevent erythropoiesis-stimulating agent and intravenous iron administration errors and track response, adverse effects and missed doses.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A factory, an order slip and a delivery truck",
         "html": """
<p>Think of the bone marrow as a factory that makes red cells. It needs an <em>order slip</em> to start production: the hormone erythropoietin, made mainly by the kidneys. It needs <em>raw material</em>: iron, delivered by a truck called transferrin. And it needs the factory floor to be calm: inflammation slows everything down. In kidney failure the order slips stop coming, the trucks are often half-empty or held at the gate, and dialysis itself loses a little blood every session. Anemia is the result.</p>
<p>The picture has a limit. Factories can simply be pushed to produce more. The marrow can too, with an erythropoiesis-stimulating agent (ESA), but pushing hemoglobin all the way back to normal turned out to cause harm, especially strokes. So renal anemia care is not "raise the number as high as possible"; it is a balance between symptoms, transfusion avoidance and risk, decided by the physician. The anemia nurse keeps the factory's records honest and makes sure every delivery is exactly what was ordered.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Organize the trend, check the order, give exactly what is ordered, report early. A sudden fall is a clinical problem, not the next step on a spreadsheet.</div>
"""},
        {"id": "physiology", "nav": "Physiology", "tag": "Physiology", "h2": "Interpret the pattern before the number",
         "html": """
<p><strong>Erythropoietin deficiency.</strong> Kidney cells that sense oxygen release erythropoietin when oxygen delivery falls. Damaged kidneys make too little for the degree of anemia, so the marrow is under-stimulated.</p>
<p><strong>Iron.</strong> Two measures are used together. <em>Ferritin</em> reflects stored iron but also rises with inflammation, so a high ferritin does not always mean plenty of usable iron. <em>Transferrin saturation (TSAT)</em> reflects iron in transit to the marrow. Hepcidin, a liver hormone that rises with inflammation and in kidney failure, locks iron in storage and blocks absorption from the gut, which is why intravenous iron is the usual route in hemodialysis.</p>
<p><strong>Blood loss.</strong> Blood left in the circuit, frequent sampling, access bleeding, and gastrointestinal bleeding (more common in kidney failure, and with antiplatelet and anticoagulant medicines) all drain red cells and iron.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>What may be happening</th><th>What the nurse does</th></tr></thead>
<tbody>
<tr><td>Slow fall over months, low TSAT</td><td>Iron deficiency or ongoing small losses</td><td>Organize iron studies and losses for the scheduled review</td></tr>
<tr><td>Fall with fever, high ferritin, low TSAT</td><td>Inflammation blocking iron use (infection, catheter, surgery)</td><td>Report; check the order on holding iron during active infection</td></tr>
<tr><td><strong>Rapid fall</strong> with black stools, vomiting blood, dizziness, chest pain</td><td><strong>Bleeding</strong></td><td><strong>Vital signs and the physician today</strong>, not a dose step</td></tr>
<tr><td>Rapid rise</td><td>Response faster than intended; risk with ESA</td><td>Report before the next scheduled dose</td></tr>
<tr><td>No response despite doses given</td><td>Iron deficiency, inflammation, missed doses, other causes</td><td>Check actual doses given (not just ordered) and report</td></tr>
</tbody></table></div>
"""},
        {"id": "evidence", "nav": "What the trials showed", "tag": "Evidence", "h2": "Why the target sits below normal",
         "html": """
<p><strong>Too high is harmful.</strong> In the TREAT trial, 4,038 patients with diabetes, chronic kidney disease (not on dialysis) and anemia were randomly assigned to darbepoetin aiming for a hemoglobin of about 13 g/dL, or to placebo with rescue treatment below 9 g/dL. The higher target did not reduce death or cardiovascular events (hazard ratio 1.05) or death or kidney failure (1.06). Stroke occurred in 101 patients on darbepoetin versus 53 on placebo (hazard ratio 1.92), an absolute difference of about 2.4 percentage points, roughly one extra stroke for every 42 patients treated to the higher target. Transfusions were fewer and fatigue improved only modestly.[[treat2009]] Earlier trials in other populations pointed the same way. This is why ESA dosing aims to reduce transfusions and symptoms, not to normalize hemoglobin.</p>
<p><strong>Iron given proactively.</strong> In the PIVOTAL trial, 2,141 adults on maintenance hemodialysis were randomly assigned to proactive high-dose intravenous iron sucrose (withheld if ferritin was above 700 µg/L or TSAT 40 percent or higher) or reactive low-dose iron. Over a median of 2.1 years, the combined outcome of heart attack, stroke, heart failure hospitalization or death occurred in 29.3 versus 32.3 percent (hazard ratio 0.85), an absolute difference of 3.0 percentage points, about one event prevented per 33 patients over two years. Patients on proactive iron needed less ESA, and infection rates were the same.[[pivotal2019]] The trial was open-label with blinded outcome assessment, and its findings apply to the iron product and thresholds tested.</p>
<p><strong>The current guideline.</strong> The KDIGO 2026 anemia guideline, the first update since 2012, frames treatment as an individual decision that weighs symptoms against risks, calls for a complete blood count, reticulocyte count, ferritin and TSAT when anemia is evaluated, and advises withholding iron when ferritin exceeds 700 ng/mL or TSAT reaches 40 percent, and suspending iron during active infection.[[anemia2026]] Newer oral agents (hypoxia-inducible factor prolyl hydroxylase inhibitors, HIF-PHIs) raise erythropoietin by mimicking low oxygen; whether and which to use is the physician's decision, based on the guideline and local availability.</p>
<div class="tc-plain"><span class="tc-lab">How certain are we?</span>Strong (randomized): aiming for near-normal hemoglobin with an ESA increases stroke without reducing deaths. Strong (randomized, one trial): proactive iron within ferritin and TSAT limits reduced a cardiovascular composite and ESA use. Hemoglobin itself is a surrogate; the outcomes patients feel are symptoms, transfusions, strokes and survival.</div>
"""},
        {"id": "authority", "nav": "What a protocol permits", "tag": "Scope", "h2": "Know what a protocol authorizes",
         "html": """
<p>Many units use an anemia protocol: a physician-signed document that sets laboratory schedules, hemoglobin bands, and the dose steps the prescriber has pre-approved. A protocol is a prescription written in advance. It authorizes only what it says, for the patients it covers, and only while its exclusions do not apply.</p>
<div class="tc-cards">
<div class="tc-card"><b>Within the protocol</b>Drawing the scheduled labs; recording results; giving the dose the prescriber's signed protocol specifies for this patient and band; reporting.</div>
<div class="tc-card"><b>Outside it, always</b>Any patient with bleeding, a rapid change, infection, a new medicine, recent surgery, chest pain or stroke symptoms; any dose outside the band; any judgment about cause.</div>
<div class="tc-card"><b>Never</b>Following a spreadsheet, a foreign protocol, a benefit table or a colleague's habit in place of a current physician order.</div>
</div>
<div class="tc-scene"><span class="tc-lab">The spreadsheet says increase &middot; fictional</span><p>Mr. Romy Aquino's hemoglobin fell from 10.2 to 8.1 g/dL in two weeks. The unit's anemia spreadsheet automatically suggests the next ESA step up. Before the session he mentions black stools for three days and feeling dizzy when standing.</p><p>Nurse Marie, the anemia nurse, does not follow the spreadsheet. She checks his blood pressure and pulse lying and standing, asks about aspirin and pain relievers, and calls Dr. Reyes: "Hemoglobin down 2.1 g/dL in two weeks, black stools for three days, dizzy on standing, pulse 108 standing. I'm concerned about bleeding." Dr. Reyes reviews him at once and arranges urgent evaluation.</p><p class="tc-scene-take"><b>What this shows.</b> A fall of 2.1 g/dL in 14 days, about 1 g/dL a week, with bleeding symptoms, is outside any dosing protocol. The toolkit's hemoglobin trend shows the pace; the symptoms decide the urgency.</p></div>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 4</span>10.2 g/dL on November 3 and 8.1 g/dL on November 17: change −2.1 g/dL over 14 days, −1.05 g/dL per week. With bleeding symptoms ticked, the toolkit's only advice is to check vital signs and tell the physician now. For a rise, epoetin product labels advise prescriber review when hemoglobin rises more than 1 g/dL in any 2-week period;[[epo_label]] the toolkit flags that pace and never suggests a dose.</div>
"""},
        {"id": "administer", "nav": "Reliable administration", "tag": "Medication safety", "h2": "Make administration reliable",
         "html": """
<ol class="tc-flow">
<li><b>Order</b>Current, signed, for this patient: product, dose, route, frequency, hold rules.</li>
<li><b>Product</b>Right product and strength; ESAs differ in units and dosing intervals; check the label, not the box color.</li>
<li><b>Storage</b>ESAs are kept refrigerated and protected from light per label; record the fridge temperature; do not shake.</li>
<li><b>Identity</b>Two identifiers at the chair.</li>
<li><b>Route and timing</b>As ordered: into the venous line or subcutaneously; intravenous iron infused per order and label, watched for reactions.</li>
<li><b>Record</b>What was actually given, or held and why, the same session.</li>
</ol>
<p><strong>Adverse reactions.</strong> Intravenous iron can rarely cause hypersensitivity reactions; know the unit's reaction protocol, keep emergency medicines ready, and stop and call if the patient develops breathlessness, chest tightness, rash, low blood pressure or swelling. ESAs raise blood pressure in some patients and, as the trials showed, carry thrombotic risk; new high blood pressure, access clotting or neurological symptoms are reported.</p>
<p><strong>Actual exposure.</strong> A patient may be "on" an ESA in the chart and have missed four doses because of stock-outs, cost or missed sessions. Track doses given, not ordered. Many cases of "ESA resistance" are missed doses or unrecognized iron deficiency.</p>
<div class="tc-stop"><span class="tc-lab">Stop and call</span>Black or bloody stools, vomiting blood, chest pain, sudden weakness or speech change, a hemoglobin change much faster than expected, or a reaction during iron infusion.</div>
"""},
        {"id": "ph", "nav": "Philippine practice", "tag": "Local practice", "h2": "In a Philippine unit",
         "html": """
<p>ESAs and intravenous iron are costly, and supply depends on PhilHealth benefits, hospital stock and what patients can buy. Benefit packages list services; they are not dosing orders and do not set targets for an individual patient.[[phic2024_23]] When a patient brings an ESA from an outside pharmacy, check the product, strength, storage during transport, and the order before giving it. Blood transfusion needs a separate order, consent per policy and bedside double-checking; for patients being considered for a kidney transplant, tell the transplant liaison about every transfusion, because transfusions can create antibodies that make matching harder (Module 10).</p>
"""},
    ],
    "case": {
        "title": "Black stools and a dose suggestion",
        "html": """
<p><strong>Friday, 6:20 a.m.</strong> Mr. Romy Aquino, 59, on hemodialysis for two years, has a hemoglobin of 8.1 g/dL; two weeks ago it was 10.2. The unit spreadsheet suggests the next ESA step. He takes aspirin and recently bought an over-the-counter pain reliever for knee pain. He reports black stools for three days and dizziness when standing. Lying: blood pressure 118/70, pulse 92. Standing: 96/60, pulse 112.</p>
<p>A colleague says, "Just follow the protocol and give the higher dose; the doctor comes on Tuesday."</p>
""",
        "acte": {
            "Assess": "Rapid fall (about 1 g/dL per week), melena, postural drop in blood pressure with rising pulse, aspirin and a likely NSAID: probable gastrointestinal bleeding. Outside any dosing protocol.",
            "Communicate": "Physician now, not Tuesday, with SBAR including the trend, symptoms, postural vital signs and medicines. Inform the charge nurse; the dialysis plan for today (fluid removal, heparin) needs the physician's decision.",
            "Teach": "Explain to Mr. Aquino why the dose is not being increased today and what symptoms to report urgently. Ask about the over-the-counter product and bring it.",
            "Escalate": "If the physician cannot be reached, follow the unit's escalation route to the clinical head or emergency care. Record that the spreadsheet suggestion was not followed and why.",
        },
        "outcome": """
<p>Dr. Reyes reviewed him within the hour, held heparin for the session, reduced fluid removal and arranged same-day gastroenterology referral. Endoscopy found a bleeding ulcer. The over-the-counter product was an NSAID. The ESA plan was reviewed after the bleeding was treated.</p>
""",
        "task": "Write the SBAR you would use, in four lines, and the note recording why the protocol step was not applied.",
    },
    "second_round": ("Three weeks later his hemoglobin has risen from 8.1 to 10.0 g/dL in 14 days after transfusion and resumed ESA, and his pre-dialysis blood pressure is higher than usual.",
                     "A trend note using the Portfolio Toolkit, the label statement on rapid rise, and the message you would send to the prescriber before the next scheduled dose."),
    "evidence_out": "A three-month anemia trend review for five fictional patients with correct escalation decisions, and an observed ESA and IV iron administration check.",
    "critical": "Applying a protocol dose step to a patient with signs of bleeding or another exclusion, or giving an ESA or iron without a current valid order.",
    "reflect": "In your unit, who notices when a patient's hemoglobin falls fast, and how quickly does it reach the physician?",
    "practice": {
        "intro": "Use de-identified trends or the fictional cases; administration is observed by your preceptor.",
        "items": [
            "Plot hemoglobin, ferritin and TSAT for five patients over six months and identify each pattern.",
            "Read your unit's anemia protocol and list its exclusions and who signed it.",
            "Complete an observed ESA administration from order check to documentation.",
            "Observe an intravenous iron infusion and review the reaction protocol and emergency medicines.",
            "Audit one month of ESA doses ordered versus given and report missed doses with reasons.",
        ],
    },
    "job_aid": ("Anemia review sheet", [
        "Patient code; ESA product and current order (date, prescriber)",
        "Hemoglobin values with dates (last 3 months)",
        "Ferritin and TSAT with dates",
        "Change per week (Portfolio Toolkit)",
        "Red flags: bleeding, infection, surgery, chest pain, neurological symptoms",
        "Medicines that raise bleeding risk (aspirin, anticoagulant, NSAID)",
        "Doses ordered versus given; reasons for missed doses",
        "Adverse effects (blood pressure, reactions, access clotting)",
        "Transfusions (and transplant liaison informed)",
        "Reported to prescriber (date, decision)",
    ]),
    "metric": "Anemia reviews due with a documented prescriber plan and completed follow-up, divided by reviews due; balanced by adverse events, transfusions, missed doses and treatment burden.",
    "readings": [
        ("anemia-management.html", "The site's guide to anemia in kidney disease."),
        ("epo-resistant-renal-anemia.html", "When erythropoietin does not seem to work."),
        ("understanding-iron.html", "Iron explained for patients."),
    ],
    "academy": [("Hemodialysis Nurse Module 3: CKD complications, nutrition and medicines", "nephrology-nursing-03-ckd-complications-nutrition-medicines.html")],
    "calcs": ["calc-dialysis-nurse-portfolio-toolkit.html", "calc-iron-status-tsat.html"],
    "terms": [
        ("Erythropoietin", "The kidney hormone that signals the bone marrow to make red blood cells."),
        ("ESA", "An injected medicine that acts like erythropoietin."),
        ("Ferritin", "A blood marker of stored iron that also rises with inflammation."),
        ("Transferrin saturation", "The share of the iron-carrying protein loaded with iron, reflecting iron available to the marrow."),
        ("Hepcidin", "A liver hormone that locks iron in storage and blocks absorption, raised by inflammation."),
        ("Protocol", "A physician-signed plan written in advance that authorizes only what it states, for the patients it covers."),
    ],
    "quiz": [
        {"stem": "Hemoglobin fell from 10.2 to 8.1 g/dL in two weeks and the patient has black stools. The spreadsheet suggests an ESA increase. What do you do?",
         "options": [["Check vital signs and report to the physician now as possible bleeding; do not apply the dose step.", True, "Bleeding is an exclusion from any dosing protocol."],
                     ["Give the higher dose as suggested.", False, "Treats a bleed as a dose problem."],
                     ["Wait for the next scheduled review.", False, "Bleeding needs same-day attention."],
                     ["Give extra iron.", False, "A prescribing decision, and not the priority."]], "sources": ["anemia2026"], "critical": True},
        {"stem": "What did the TREAT trial show about aiming for a hemoglobin of about 13 g/dL with darbepoetin?",
         "options": [["No reduction in death or cardiovascular events, and about twice as many strokes (HR 1.92).", True, "101 versus 53 strokes."],
                     ["Fewer deaths and strokes.", False, "Not found."],
                     ["No difference in anything.", False, "Stroke was increased and transfusions decreased."],
                     ["It was an observational study.", False, "It was randomized."]], "sources": ["treat2009"]},
        {"stem": "In PIVOTAL, what did proactive intravenous iron achieve compared with reactive iron?",
         "options": [["A lower cardiovascular composite (29.3 vs 32.3 percent), less ESA use and no more infections.", True, "Hazard ratio 0.85."],
                     ["More infections.", False, "Infection rates were the same."],
                     ["Higher ESA doses.", False, "ESA doses were lower."],
                     ["No difference in any outcome.", False, "The composite was reduced."]], "sources": ["pivotal2019"]},
        {"stem": "Per KDIGO 2026, when is iron withheld?",
         "options": [["When ferritin exceeds 700 ng/mL or TSAT reaches 40 percent, and during active infection.", True, "As stated in the guideline's algorithm."],
                     ["Whenever hemoglobin is above 9 g/dL.", False, "Not the rule."],
                     ["Never.", False, "There are withholding rules."],
                     ["Only on weekends.", False, "Not a rule."]], "sources": ["anemia2026"]},
        {"stem": "Why can a high ferritin be misleading?",
         "options": [["Ferritin also rises with inflammation, so it may not reflect usable iron.", True, "Read it with TSAT and the clinical picture."],
                     ["Ferritin measures hemoglobin.", False, "It does not."],
                     ["Ferritin is always low in dialysis.", False, "Not true."],
                     ["Ferritin rises after meals only.", False, "Not the reason."]], "sources": ["anemia2026"]},
        {"stem": "What does an anemia protocol authorize?",
         "options": [["Only what the signed protocol states, for covered patients, while no exclusion applies.", True, "A protocol is a prescription written in advance."],
                     ["Any dose the nurse judges best.", False, "Not independent prescribing."],
                     ["Doses from any overseas protocol.", False, "No authority here."],
                     ["Doses in the PhilHealth benefit table.", False, "Benefits are not orders."]], "sources": []},
        {"stem": "Epoetin labels advise prescriber review at what pace of hemoglobin rise?",
         "options": [["More than 1 g/dL in any 2-week period.", True, "Report before the next scheduled dose."],
                     ["Any rise at all.", False, "Not the label threshold."],
                     ["More than 5 g/dL per month.", False, "Not the label threshold."],
                     ["Rises do not matter.", False, "Rapid rises do."]], "sources": ["epo_label"]},
        {"stem": "During an intravenous iron infusion the patient becomes breathless with a rash. What do you do first?",
         "options": [["Stop the infusion, call for help and follow the reaction protocol.", True, "Possible hypersensitivity reaction."],
                     ["Slow the infusion and continue.", False, "Unsafe."],
                     ["Give the rest after the session.", False, "Unsafe."],
                     ["Document and wait.", False, "Delays treatment."]], "sources": [], "critical": True},
        {"stem": "A patient seems 'resistant' to ESA. What should the anemia nurse check first?",
         "options": [["Doses actually given versus ordered, iron status, infection and blood loss.", True, "Missed doses and iron deficiency are common causes."],
                     ["Ask for a higher dose immediately.", False, "Not a nursing decision, and may miss the cause."],
                     ["Switch products.", False, "Prescribing decision."],
                     ["Nothing; resistance is permanent.", False, "Often reversible causes."]], "sources": []},
        {"stem": "Why is the hemoglobin target in kidney disease set below the normal range?",
         "options": [["Trials aiming for near-normal hemoglobin with ESAs increased stroke without reducing deaths.", True, "The balance of benefit and harm favors lower targets."],
                     ["Normal hemoglobin is impossible on dialysis.", False, "It can be reached, with harm."],
                     ["ESAs are expensive.", False, "Cost is not the evidence reason."],
                     ["Patients feel worse at normal levels.", False, "Not the main finding."]], "sources": ["treat2009"]},
        {"stem": "How should ESAs be stored?",
         "options": [["Refrigerated and protected from light, per label, without shaking.", True, "Storage affects potency."],
                     ["At room temperature in the drawer.", False, "May lose potency."],
                     ["Frozen.", False, "Not per label."],
                     ["Shaken before use.", False, "Avoid shaking."]], "sources": []},
        {"stem": "A patient being considered for transplant receives a blood transfusion. Whom should the anemia nurse tell?",
         "options": [["The transplant liaison, because transfusions can create antibodies that affect matching.", True, "Sensitization matters for transplant."],
                     ["No one.", False, "This affects transplant."],
                     ["Only the family.", False, "The liaison must know."],
                     ["The blood bank only.", False, "The transplant team needs to know."]], "sources": []},
        {"stem": "Is hemoglobin a patient-important outcome?",
         "options": [["No; it is a surrogate. Patients feel symptoms, transfusions, strokes and survival.", True, "Label surrogates as surrogates."],
                     ["Yes, it is the main outcome.", False, "It is a surrogate."],
                     ["Only in trials.", False, "It is a surrogate everywhere."],
                     ["Only above 13 g/dL.", False, "Not relevant."]], "sources": ["treat2009"]},
        {"stem": "A patient brings an ESA bought from an outside pharmacy. What do you check before giving it?",
         "options": [["Product, strength, storage during transport, expiry and a current order.", True, "Medication safety checks apply to every source."],
                     ["Only the expiry date.", False, "Not enough."],
                     ["Nothing; the patient paid for it.", False, "Safety checks still apply."],
                     ["Only the price.", False, "Irrelevant to safety."]], "sources": []},
        {"stem": "About how many patients needed proactive iron in PIVOTAL to prevent one composite event over about two years?",
         "options": [["About 33.", True, "Absolute difference of 3.0 percentage points."],
                     ["About 3.", False, "Far too few."],
                     ["About 300.", False, "Too many."],
                     ["It cannot be calculated.", False, "Event rates were reported."]], "sources": ["pivotal2019"]},
    ],
    "exam": [
        {"stem": "Which finding takes a patient outside an anemia dosing protocol?",
         "options": [["Black stools with a rapid hemoglobin fall.", True, "Possible bleeding needs the physician now."],
                     ["A stable hemoglobin within the band.", False, "Within protocol."],
                     ["A routine monthly laboratory draw.", False, "Within protocol."],
                     ["A missed lunch.", False, "Not relevant."]], "sources": ["anemia2026"], "critical": True},
        {"stem": "What did TREAT teach about high hemoglobin targets?",
         "options": [["They increased stroke without reducing deaths or cardiovascular events.", True, "Randomized evidence."],
                     ["They reduced deaths.", False, "Not found."],
                     ["They had no effect on stroke.", False, "Stroke roughly doubled."],
                     ["They reduced transfusions to zero.", False, "Reduced, not eliminated."]], "sources": ["treat2009"]},
    ],
}

# ── v2 completion (24 Nov 2026): second and third worked scenarios ──
def _sec(sid):
    return next(s for s in MODULE["sections"] if s["id"] == sid)

_sec("physiology")["html"] += """
<div class="tc-scene"><span class="tc-lab">The rise that was too fast &middot; fictional</span><p>Mrs. Celia Navarro, 64, is on an ESA under the unit's anemia protocol. Her hemoglobin was 9.4 g/dL on the 3rd and 10.8 g/dL on the 17th: a rise of 1.4 g/dL in 14 days. The protocol's next step reads "continue current dose." Her blood pressure before dialysis has crept up over the same two weeks.</p><p>Nurse Lorna, the anemia nurse, works out the change per week (0.7 g/dL), sees that it is above the label's trigger of more than 1 g/dL in any 2-week period, and notes that the protocol step does not address it. She does not change the dose herself. She sends an SBAR to Dr. Reyes with the two dated values, the rate of rise, the blood pressure trend, and the question "Please review the ESA dose." Dr. Reyes reduces the dose and asks for a repeat hemoglobin in two weeks; Lorna writes the order, the owner and the check date on the anemia tracker.</p><p class="tc-scene-take"><b>What this shows.</b> A fast rise is a safety signal even when the number is still below target, because the speed of change, not just the level, is linked with harm. The nurse recognizes and reports; the prescriber decides.</p></div>
"""

_sec("administer")["html"] += """
<div class="tc-scene"><span class="tc-lab">Iron day, and a red catheter exit site &middot; fictional</span><p>Mr. Danilo Ramos, 58, dialyzes through a tunneled catheter. Today's schedule lists his weekly IV iron under the proactive iron protocol. At connection he has a temperature of 38.2 °C, and the skin around the catheter exit site is red, warm and tender, with a small amount of pus.</p><p>Nurse Lorna does not give the iron. The unit protocol, signed by the nephrologist, says to hold IV iron in suspected active infection and to notify the prescriber. She tells the charge nurse and Dr. Reyes, who examines him, orders blood cultures from the catheter and a peripheral vein before the first antibiotic dose, and starts treatment. Lorna records "IV iron held, suspected catheter infection, Dr. Reyes informed 7:10 a.m." and puts a review flag on the anemia tracker for the next week.</p><p class="tc-scene-take"><b>What this shows.</b> Holding a dose because the protocol says so is not a dose change; it is following the order. Any decision about when to restart belongs to the prescriber. The same red site also belongs to the infection prevention nurse's surveillance (Module 3).</p></div>
"""
