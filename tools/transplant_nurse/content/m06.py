# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How each immunosuppressant quiets a different step of T-cell activation, why tacrolimus has a narrow window and a trough that must be timed to the minute, which everyday drugs and fruits push levels up or down, and how to respond safely to a missed dose, a stock-out or a brand switch.",
    "desc": "Transplant Nurse Module 6: immunosuppression mechanisms (calcineurin inhibitors, mycophenolate, corticosteroids, belatacept), ELITE-Symphony and BENEFIT evidence, tacrolimus trough timing, concentration-to-dose ratio and intrapatient variability, CYP3A interactions including rifampicin, formulation safety, nonadherence and teratogenicity for Philippine registered nurses.",
    "keywords": "tacrolimus trough timing nurse, tacrolimus drug interactions rifampicin, mycophenolate pregnancy, immunosuppressant nonadherence kidney transplant, tacrolimus formulation switch, intrapatient variability tacrolimus",
    "image_alt": "A nurse and a young transplant recipient at a kitchen table sorting tablets into a weekly pill organizer beside a printed medicine schedule.",
    "objectives": [
        "Explain how calcineurin inhibitors, antimetabolites, corticosteroids and costimulation blockers interrupt T-cell activation.",
        "Relate each drug class to the adverse effects and monitoring a nurse must watch for.",
        "Time and document a tacrolimus trough correctly, and explain why a mistimed level misleads.",
        "Identify common interactions that raise or lower tacrolimus levels, including those common in the Philippines.",
        "Respond within scope to missed or vomited doses, stock-outs and formulation switches, and teach a safe response.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "Three switches on the same alarm",
         "html": """
<p>Think of rejection as an alarm that needs three switches turned before it sounds. A T lymphocyte that meets donor HLA must receive three signals before it multiplies and attacks. Signal 1 is recognition: its receptor sees the foreign antigen. Signal 2 is a confirming handshake, a costimulatory contact with the antigen-presenting cell. Signal 3 is growth: interleukin-2 (IL-2) and other cytokines tell the activated cell to divide.</p>
<p>Maintenance immunosuppression blocks different switches with different drugs. Each drug can then be given at a lower, safer dose. That is the logic of triple therapy.</p>
<p>The picture has a limit. An alarm is either on or off; T-cell activation is graded, and a partly blocked switch still lets some signal through, which is why levels and doses matter so much. The immune system is also not just T cells. B cells and antibodies cause antibody-mediated rejection (Module 7), and the same drugs that quiet rejection also weaken defense against viruses and cancer (Modules 8 and 9). Immunosuppression is a balance point, not a dial turned to maximum.</p>
"""},
        {"id": "classes", "nav": "Drug classes", "tag": "Pharmacology", "h2": "What each drug class does, and what to watch",
         "html": """
<div class="table-wrap"><table>
<thead><tr><th>Class and examples</th><th>Mechanism</th><th>What the nurse watches</th></tr></thead>
<tbody>
<tr><td>Calcineurin inhibitors (CNI): tacrolimus, cyclosporine</td><td>Block calcineurin, so the transcription factor NFAT cannot switch on IL-2; blocks signal 1 downstream</td><td>Trough levels; rising creatinine (afferent vasoconstriction, chronic toxicity); tremor, headache; high potassium, low magnesium; new diabetes; hypertension; rarely confusion or seizures</td></tr>
<tr><td>Antimetabolites: mycophenolate (MMF, enteric-coated mycophenolic acid), azathioprine</td><td>Mycophenolic acid (MPA) inhibits inosine monophosphate dehydrogenase; lymphocytes depend on this route to make purines, so they cannot multiply</td><td>Diarrhea, nausea, abdominal pain; low white cells and platelets; serious birth defects and miscarriage risk</td></tr>
<tr><td>Corticosteroids: prednisone, methylprednisolone</td><td>Broad suppression of cytokine genes and inflammatory cell traffic</td><td>Glucose, blood pressure, mood and sleep, bone health, weight, wound healing, infection</td></tr>
<tr><td>Costimulation blocker: belatacept</td><td>Blocks the CD80/86-CD28 handshake (signal 2); monthly infusion</td><td>Infusion schedule adherence; infection; post-transplant lymphoproliferative disorder (PTLD) risk in Epstein-Barr virus-negative recipients</td></tr>
<tr><td>mTOR inhibitors: sirolimus, everolimus</td><td>Block signal 3 growth signaling</td><td>Mouth ulcers, edema, high lipids, proteinuria, slow wound healing</td></tr>
<tr><td>Induction: basiliximab, anti-thymocyte globulin (ATG)</td><td>Intense, short-term T-cell suppression around surgery, per protocol</td><td>Infusion reactions, fever, low white cells and platelets with ATG</td></tr>
</tbody></table></div>
<p><strong>Why tacrolimus is the backbone.</strong> In the ELITE-Symphony trial of 1,645 recipients, low-dose tacrolimus with mycophenolate and steroids produced the lowest biopsy-proven acute rejection rate at one year (12.3 percent versus 24.0 to 37.2 percent with cyclosporine or sirolimus regimens) and the best kidney function. Rejection and estimated glomerular filtration rate (eGFR) are surrogates; the outcome patients feel is keeping the kidney, and one-year graft survival was also highest with low-dose tacrolimus (94.2 percent versus 89.3 to 93.1 percent).[[ekberg2007]] The KDIGO recipient guideline recommends maintenance with a calcineurin inhibitor plus an antiproliferative agent, with or without steroids (1B), and suggests tacrolimus as the first-line calcineurin inhibitor (2A) and mycophenolate as the first-line antiproliferative agent (2B).[[txrecip2009]] Most centers have used tacrolimus-based triple therapy since.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Three weeks after transplant, Mr. Tan says his hands shake when he holds a cup, and he has been thirsty and passing urine at night. His fasting glucose today is 176 mg/dL (9.8 mmol/L). He has never had diabetes.</p><p>You recognize two classic calcineurin inhibitor effects. You check today's tacrolimus level and its timing, record the tremor and the glucose, and route both to the transplant nephrologist. You also tell Mr. Tan that these effects are known and that the team can act on them, so that he does not quietly stop his tablets.</p><p class="tc-scene-take"><b>What this shows.</b> Knowing each drug's signature side effects lets you connect a new symptom to the right medicine, and report it before the patient stops taking it.</p></div>

<p><strong>Belatacept as an alternative.</strong> In the seven-year follow-up of the BENEFIT trial, belatacept-based regimens reduced the combined risk of death or graft loss by 43 percent compared with cyclosporine (hazard ratio 0.57 for both belatacept regimens), with equal contributions from fewer deaths and fewer graft losses, and with eGFR rising rather than falling; early acute rejection was more frequent with belatacept.[[vincenti2016]] Death and graft loss are the outcomes that matter most, which is what makes this result notable. Its use depends on availability, cost and the recipient's Epstein-Barr virus status.</p>
"""},
        {"id": "toxicity", "nav": "Narrow window", "tag": "Physiology", "h2": "A narrow window: why the protecting drugs can also harm",
         "html": """
<p>Tacrolimus has a narrow therapeutic window. Too little, and T cells escape control and attack the graft. Too much, and the drug injures the very kidney it protects, raises infection and cancer risk, and causes a long list of side effects. The window is narrow, and it moves: it is set higher in the first months and lower later, by the team, for each patient. That is the reason for all the attention to levels in this module.</p>
<p><strong>How a calcineurin inhibitor hurts the kidney.</strong> Calcineurin is not found only in T cells. Blocking it in the kidney's small arteries tightens the afferent arteriole, the vessel that brings blood into each glomerulus. Less blood enters, so filtration falls and creatinine rises. This early effect follows the drug level and reverses when the level comes down. Over years, repeated exposure can thicken and scar the arteriole walls and the tissue around the tubules. This chronic injury does not reverse. The team balances the two dangers: rejection from too little drug and slow scarring from too much.</p>
<div class="table-wrap"><table>
<thead><tr><th>Effect</th><th>The mechanism in one line</th><th>What you notice or report</th></tr></thead>
<tbody>
<tr><td>Rising creatinine</td><td>Afferent arteriole constriction, worse at high levels</td><td>A creatinine rise with a high trough, especially after a new interacting drug</td></tr>
<tr><td>High potassium and mild acidosis</td><td>The drug makes the distal tubule hold on to sodium and chloride, which reduces potassium and acid excretion</td><td>Potassium creeping up with a normal creatinine; the patient eating potassium-rich fruit</td></tr>
<tr><td>Low magnesium</td><td>The tubule wastes magnesium</td><td>Cramps, tremor; low magnesium on routine tests</td></tr>
<tr><td>High blood pressure</td><td>Vessel constriction and salt retention</td><td>Home readings above the target the team has set</td></tr>
<tr><td>High glucose</td><td>Direct effect on the insulin-making cells of the pancreas, added to steroids</td><td>Thirst, frequent urination, high fasting glucose</td></tr>
<tr><td>Tremor, headache, rarely confusion or seizures</td><td>Effects on nerve cells, worse at high levels</td><td>Shaking hands, new headaches, any change in thinking</td></tr>
</tbody></table></div>
<p><strong>The other drugs have their own signatures.</strong> Mycophenolate stops lymphocytes from multiplying, but it also slows other fast-dividing cells, such as the lining of the gut and the bone marrow. That explains its diarrhea and its low white cell counts. Steroids act on almost every tissue, which is why their effects include glucose, mood, bone, skin, weight and wound healing. When a patient reports a new symptom, ask which drug's mechanism could produce it. The answer guides what you report and to whom.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>A high tacrolimus level is not a safe level. Too much drug harms the kidney, the nerves and the pancreas, and raises infection risk. Report a high level as promptly as a low one.</div>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mrs. Ventura, 14 months after transplant, has a creatinine of 1.6 mg/dL, up from 1.2. Her tacrolimus trough is well above her usual range, and her potassium is 5.7 mmol/L. She mentions a "slight tremor" and that she started taking a medicine for a fungal infection of her nails, prescribed at a mall clinic two weeks ago.</p><p>You confirm the trough was drawn at the right time, write down the name of the antifungal, and report the full picture to Dr. Santos that morning: high level, rising creatinine, rising potassium, tremor and a new drug known to raise tacrolimus. He stops the antifungal and adjusts her dose.</p><p class="tc-scene-take"><b>What this shows.</b> A creatinine rise is not always rejection. A high level, a new drug and the drug's signature side effects together point to toxicity.</p></div>
"""},
        {"id": "trough", "nav": "Timing a trough", "tag": "Practice", "h2": "Tacrolimus levels: timing is the test",
         "html": """
<p>Tacrolimus has a narrow therapeutic window. Too low and rejection follows; too high and the kidney, nerves and pancreas suffer. Absorption varies widely between people and within one person, so doses are adjusted to whole-blood levels. The standard is the <em>trough</em> (C<sub>0</sub>): the lowest level, just before the next dose. The KDIGO recipient guideline recommends measuring calcineurin inhibitor levels (1B), suggests doing so every other day after surgery until the target is reached and again whenever a drug, the patient's condition or kidney function changes (2C), and suggests the 12-hour trough for tacrolimus (2C).[[txrecip2009]] A trough is a surrogate: it estimates exposure, which is what drives both rejection and toxicity.</p>
<ul>
<li><strong>Twice-daily immediate-release:</strong> trough about 12 hours after the evening dose, drawn just before the morning dose.</li>
<li><strong>Once-daily extended-release:</strong> trough about 24 hours after the last dose, drawn just before the next one.</li>
</ul>
<p>A sample drawn two hours <em>after</em> the morning dose is near the peak and can read two or three times higher than the true trough. If the team reads it as a trough, they may cut a dose that was correct and expose the kidney to rejection. Your documentation is part of the test: record the actual time of the last dose, the actual collection time, and when the next dose is due. If the timing was wrong, say so on the request and in the chart, so the result is interpreted correctly.</p>
<div class="tc-scene"><span class="tc-lab">At the laboratory window, 7:40 a.m. &middot; fictional</span><p>Your clinic draws tacrolimus levels from 7 to 9 a.m. Mrs. Natividad is in line. You ask the question you ask every recipient in that line: "Have you taken this morning's tacrolimus?" She has not. Her evening dose was at 7:30 p.m. You write both times on the request.</p><p>Behind her, Mr. Uy took his dose at 6:30 a.m. "so I wouldn't forget." You write that on his request too, and flag it: this sample will not be a trough.</p><p class="tc-scene-take"><b>What this shows.</b> One question at the laboratory window turns a number into an interpretable result.</p></div>

<div class="tc-plain"><span class="tc-lab">Teach-back line</span>"On blood-test mornings, bring your tacrolimus with you and take it <em>after</em> the blood is drawn. Then write down when you took last night's dose."</div>
<p><strong>Two more ways to read levels.</strong> The <em>concentration-to-dose (C/D) ratio</em> divides the trough by the total daily dose. In a German cohort of 248 recipients, patients with a low C/D ratio ("fast metabolizers," who need high doses to reach target) had lower eGFR over two years and more biopsies showing CNI toxicity and BK polyomavirus nephropathy.[[tholking2014]] <em>Intrapatient variability (IPV)</em> measures how much one person's troughs swing on an unchanged dose, usually as a coefficient of variation. High IPV is consistently associated with rejection, donor-specific antibodies and graft loss, and nonadherence is a major cause.[[shuker2015]] Both are observational markers: they flag patients for closer attention (adherence, interactions, formulation) rather than dictating a dose. The <a href="calc-tacrolimus-level-check.html">Tacrolimus Level Check</a> calculator computes timing validity, C/D ratio and IPV from your entries.</p>
"""},
        {"id": "interactions", "nav": "Interactions", "tag": "Pharmacology", "h2": "Drugs, foods and herbs that move tacrolimus",
         "html": """
<p>Tacrolimus is broken down by cytochrome P450 3A (CYP3A) enzymes in the gut wall and liver and pumped back into the gut by P-glycoprotein. Anything that blocks these raises levels; anything that induces them lowers levels, sometimes dramatically.</p>
<div class="tc-cards">
<div class="tc-card"><b>Raise levels (toxicity risk)</b>Azole antifungals (fluconazole, voriconazole, itraconazole); clarithromycin and erythromycin; diltiazem and verapamil; some HIV and hepatitis C antivirals; grapefruit and its relative pomelo (<em>suha</em>).</div>
<div class="tc-card"><b>Lower levels (rejection risk)</b>Rifampicin, the cornerstone of tuberculosis treatment; carbamazepine, phenytoin, phenobarbital; St John's wort.</div>
<div class="tc-card"><b>Add kidney or potassium stress</b>Nonsteroidal anti-inflammatory drugs (mefenamic acid, ibuprofen) and potassium-sparing drugs add to CNI effects on kidney blood flow and potassium.</div>
<div class="tc-card"><b>Unknown effect</b>Herbal teas, "detox" products and supplements are rarely tested. Ask about them by name: <em>lagundi</em>, <em>sambong</em>, <em>malunggay</em> capsules, turmeric.</div>
</div>
<p><strong>Rifampicin deserves a special warning in the Philippines.</strong> It induces CYP3A so strongly that tacrolimus levels can fall to near zero within days, and the effect persists for a week or more after rifampicin stops. A recipient started on standard tuberculosis treatment by a provincial clinic, without the transplant team knowing, is at high risk of rejection. Teach recipients to tell every prescriber that they have a transplant and to call the program before starting any new medicine.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Nanay Fe, 18 months after her transplant, calls about a routine refill. Almost as an afterthought, she says the health center started her on "the six-month cough medicine" last week, four tablets a day.</p><p>You ask her to read the label. It is a fixed-dose tuberculosis combination containing rifampicin. You call the transplant nephrologist that afternoon, and an urgent tacrolimus level is drawn. It has fallen from 7.1 to 2.3 ng/mL.</p><p class="tc-scene-take"><b>What this shows.</b> Patients rarely think of tuberculosis tablets as "new medicines." Ask by name, ask about health-center treatment, and route it the same day.</p></div>

<p>The <a href="calc-drug-interaction-checker.html">Drug Interaction Checker</a> helps you screen, but verification with the transplant pharmacist or team is the standard before any new drug is started.</p>
"""},
        {"id": "reading", "nav": "Reading levels", "tag": "Practice", "h2": "Reading a run of levels: a worked example",
         "html": """
<p>One level is a snapshot. A run of levels is a story. Your job is not to decide the dose. Your job is to make sure the story is accurate, so the prescriber reads it correctly. That means collecting the facts behind each number: when the last dose was taken, when the sample was drawn, whether any dose was missed, which formulation was taken, and what else changed.</p>
<p><strong>Things that move a level without any change in dose.</strong> Some you have met already: interacting drugs, foods and herbs, and timing. Others are easy to miss. Diarrhea can <em>raise</em> tacrolimus levels, because an inflamed gut breaks down and pumps out less of the drug before it is absorbed. This surprises many nurses, who expect diarrhea to lower absorption. Vomiting a dose, or skipping doses before a clinic visit and taking them on the morning of the test, distort the result in the other direction. A change from one brand or generic to another can change exposure even at the same milligram dose.</p>
<div class="table-wrap"><table>
<thead><tr><th>Week</th><th>Trough</th><th>What the nurse found</th><th>What it suggests</th></tr></thead>
<tbody>
<tr><td>1</td><td>In the usual range</td><td>Drawn 12 hours after the evening dose; no changes</td><td>A reliable baseline</td></tr>
<tr><td>2</td><td>Well above range</td><td>Morning dose taken at 6 a.m., blood drawn at 8 a.m.</td><td>Not a trough. A peak was drawn. Repeat with correct timing</td></tr>
<tr><td>3</td><td>Above range</td><td>Correct timing. Three days of watery diarrhea</td><td>Diarrhea may be raising the level. Report both</td></tr>
<tr><td>5</td><td>Below range</td><td>Pharmacy supplied a different generic two weeks ago</td><td>A formulation change. Report it, with the product name</td></tr>
<tr><td>6</td><td>Very variable over months</td><td>Patient admits often taking the evening dose "when I remember"</td><td>High intrapatient variability linked to missed doses; an adherence conversation, not only a dose change</td></tr>
</tbody></table></div>
<p>Notice that four of the five abnormal results had an explanation the nurse could find in a few questions. A prescriber who sees only the numbers might raise or lower the dose for each one. A prescriber who sees the numbers with the facts makes fewer, better changes. Write those facts beside each result in the patient's level record.</p>
<p><strong>When the brand changes.</strong> Different tacrolimus products are not always interchangeable milligram for milligram, and the immediate-release and extended-release forms must never be mixed up. If a patient's supply changes to a different product, the team usually wants to know before the switch, and often wants a level soon after it. Teach patients to check the name and appearance of their tablets at every refill and to call before taking a different product.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Mang Romy calls on Tuesday. His tacrolimus capsules "look different" this month. The pharmacy told him they are "the same medicine, cheaper."</p><p>You ask him to read the name and strength on the box. It is a different generic product. You ask whether he has started them yet; he has not. You tell Dr. Santos, who agrees to the switch and orders a trough in one week. You write the new product name, the start date and the level date in his record, and tell Mang Romy exactly when to have his blood drawn.</p><p class="tc-scene-take"><b>What this shows.</b> A product change is a clinical event. Record it, report it, and time the next level so the team can see its effect.</p></div>
"""},
        {"id": "errors", "nav": "Preventing errors", "tag": "Practice", "h2": "Reconciliation, formulations, missed doses and supply",
         "html": """
<p><strong>Reconcile against two sources.</strong> Compare what the patient actually takes (bring the bottles) with the current verified order. Check drug, exact formulation and brand, strength, dose, route, timing, and recent changes. Immediate-release twice-daily tacrolimus and once-daily extended-release products are <em>not</em> interchangeable milligram for milligram. A switch between them, or between brands or generics, can change exposure and needs a team-directed plan and a follow-up level.</p>
<p><strong>Missed or vomited doses.</strong> Document what was missed or vomited and when, contact the designated team, and teach the individualized instruction they give. Do not invent a rule; programs differ. A recipient with repeated vomiting or diarrhea may not be absorbing tacrolimus (or may be absorbing more, since diarrhea can raise levels), and needs prompt review.</p>
<p><strong>Supply gaps are emergencies in slow motion.</strong> Running out of tacrolimus for even a few days can trigger rejection. When a patient says supply will run out, confirm the remaining count and the schedule, contact the team and pharmacy the same day, arrange an authorized continuity plan, and confirm the plan with the patient. Benefits staff can check post-transplant package coverage (Module 10).</p>
<div class="tc-scene"><span class="tc-lab">By text message &middot; fictional</span><p>On a Saturday, Allan texts the clinic number: "Nurse, the pharmacy has no Prograf until next Friday. I have 5 capsules left. Can I take one a day so it lasts?"</p><p>You do not answer the dosing question. You reply that he must not stretch his doses, and that someone from the team will call him within the hour. Then you call the on-call transplant physician and the pharmacy. By evening there is an authorized plan: a supply from the center's pharmacy and a level next week. You call Allan back, have him repeat the plan, and document it.</p><p class="tc-scene-take"><b>What this shows.</b> Supply gaps are handled the same day, by the team, and confirmed with the patient. Stretching doses is never the nurse's call.</p></div>

<p><strong>Nonadherence is common and predictable.</strong> A meta-analysis across organs found immunosuppressant nonadherence was highest among kidney recipients, about 36 cases per 100 patients per year.[[dew2007]] In a multicenter observational study of 113 recipients who developed de novo donor-specific antibodies, nonadherence was the strongest patient-level predictor of later graft failure (hazard ratio 6.5).[[schinstock2019]] Observational data cannot prove that nonadherence alone caused the losses, but the association is large and consistent with other studies. Ask without judgment: "Many people miss a dose now and then. In the last month, how many times has that happened to you?" A structured tool such as the Basel scale in the <a href="calc-transplant-prom.html">transplant PROM suite</a> makes the question routine.</p>
<p><strong>Pregnancy and mycophenolate.</strong> Mycophenolate causes serious birth defects and miscarriage. Ask about pregnancy intentions and contraception early and at every review, and route a possible pregnancy on mycophenolate to the team urgently, the same day. Planned pregnancy is possible after transplant with a regimen change made in advance (Module 11).</p>
<div class="tc-stop"><span class="tc-lab">Stop and report</span>Any dose change, substitution or omission must come from an authorized prescriber. A nurse who "just adjusts" a tacrolimus dose from a level, or tells a patient to skip mycophenolate, is practicing outside scope.</div>
"""},
    ],
    "case": {
        "title": "The level drawn after breakfast",
        "html": """
<p><strong>Friday, 11:30 a.m., transplant clinic.</strong> Ms. Reyes, 34, is three months after a living-related transplant. She takes twice-daily tacrolimus, mycophenolate and prednisone. Her tacrolimus result today is 14.8 ng/mL. Her usual troughs are 7 to 8.</p>
<p>You ask about timing. She took her morning tacrolimus at 7:00 a.m. with breakfast, "because the line is long and I get hungry," and had blood drawn at 9:30 a.m. She feels fine apart from a cough.</p>
<p>Before she leaves, she shows you a prescription from a provincial clinic: clarithromycin 500 mg twice daily for seven days, for the cough. She plans to buy it on the way home and start tonight. She also mentions, unprompted, that she and her husband "might try for a baby next year."</p>
""",
        "acte": {
            "Assess": "Exact dose times and collection time, any symptoms of toxicity (tremor, headache), the cough (fever, sputum, breathlessness), other new medicines or supplements, and whether she is using contraception.",
            "Communicate": "Flag the result as not a trough, with documented dose and draw times, to the transplant team. Report the clarithromycin prescription before she starts it, so the team and pharmacist can advise on an alternative or level monitoring, and report the cough for assessment.",
            "Teach": "Teach-back the trough routine: bring the morning dose and take it after the blood test. Teach her to tell every prescriber about her transplant and to check with the program before starting any medicine.",
            "Escalate": "If the cough is accompanied by fever or breathlessness, arrange prompt assessment (Module 8). Ensure a repeat, correctly timed level is ordered and has an owner.",
        },
        "task": "Write the reconciliation note (two sources, discrepancy, interaction flag) and the teach-back record.",
        "outcome": """
<p>The nurse in the story wrote three times on the result: last dose 7:00 a.m., blood drawn 9:30 a.m., next dose 7:00 p.m. She flagged it to the team as "not a trough", so the dose would not be cut on a misleading number.</p>
<p>She asked Ms. Reyes not to start the clarithromycin until the team had seen it, and called the transplant pharmacist, who explained that clarithromycin can raise tacrolimus levels sharply. Dr. Santos reviewed the cough that afternoon, chose a different antibiotic, and ordered a correctly timed level for Monday.</p>
<p>The nurse also passed on the pregnancy plan, because mycophenolate must be changed well before conception. Ms. Reyes left with a written trough routine she had explained back in her own words: "Bring the capsules, take them after the blood is drawn."</p>
""",
    },
    "second_round": ("The pharmacy has only a different tacrolimus formulation in stock, and her next level is due tomorrow morning.", "A two-source reconciliation, a safe routing plan to the team and pharmacist, and a timed sampling teach-back."),
    "evidence_out": "Medication reconciliation and teach-back.",
    "critical": "Advising a dose change or substitution without authorization.",
    "reflect": "Think of the last tacrolimus level you saw. Could you tell from the record whether it was a true trough?",
    "practice": {
        "intro": "With the transplant pharmacist and your preceptor.",
        "items": [
            "Complete a two-source reconciliation for a recipient, including formulation and brand.",
            "Document a tacrolimus trough with last-dose, collection and next-dose times.",
            "Screen a synthetic medicine list for CYP3A interactions and route findings to the pharmacist.",
            "Teach the trough routine and missed-dose instructions using teach-back.",
            "Locate your program's procedure for stock-outs and formulation switches.",
        ],
    },
    "readings": [
        ("kidney-transplant.html", "Patient overview of transplant medicines."),
        ("herbal-nephropathy.html", "Herbal products and kidney harm."),
        ("transplant-allograft-failure.html", "How rejection and nonadherence lead to graft loss."),
    ],
    "calcs": ["calc-tacrolimus-level-check.html", "calc-tacrolimus-dosing.html", "calc-drug-interaction-checker.html", "calc-transplant-prom.html"],
    "terms": [
        ("Trough level", "The drug concentration just before the next dose, the lowest point of the dosing cycle."),
        ("Calcineurin", "An enzyme that activates the transcription factor NFAT, switching on interleukin-2 in T cells."),
        ("Narrow therapeutic index", "A small gap between effective and toxic concentrations."),
        ("Enzyme inducer", "A drug that increases the amount of a metabolizing enzyme, lowering levels of drugs it breaks down."),
        ("Coefficient of variation", "Standard deviation divided by the mean, expressed as a percentage."),
    ],
    "quiz": [
        {"stem": "How does tacrolimus suppress rejection?",
         "options": [("It inhibits calcineurin, preventing NFAT from switching on interleukin-2 in T cells.", True, "Blocks T-cell activation."),
                     ("It kills all white blood cells.", False, "That is not its mechanism."),
                     ("It blocks purine synthesis.", False, "That is mycophenolate."),
                     ("It removes antibodies from the blood.", False, "That is plasmapheresis.")],
         "sources": ["ekberg2007"]},
        {"stem": "A twice-daily tacrolimus level was drawn 2.5 hours after the morning dose. What should the nurse do?",
         "options": [("Flag it as not a trough, document dose and draw times, and route to the team for interpretation and a repeat.", True, "A post-dose level overestimates the trough."),
                     ("Report it as the trough.", False, "Misleads dosing."),
                     ("Reduce the evening dose.", False, "Outside scope."),
                     ("Discard the result.", False, "Document and route; do not discard.")],
         "sources": []},
        {"stem": "Which times should accompany every tacrolimus trough?",
         "options": [("Actual previous dose time, specimen collection time and scheduled next dose time.", True, "Needed to judge whether it is a true trough."),
                     ("Only the collection date.", False, "Insufficient."),
                     ("Time of breakfast only.", False, "Insufficient."),
                     ("The time the result was released.", False, "Not relevant to timing validity.")],
         "sources": []},
        {"stem": "A recipient is started on rifampicin for tuberculosis by another clinic. What is the main risk?",
         "options": [("Rifampicin strongly induces CYP3A, lowering tacrolimus levels and risking rejection.", True, "A major interaction, highly relevant in the Philippines."),
                     ("Rifampicin raises tacrolimus to toxic levels.", False, "It lowers them."),
                     ("There is no interaction.", False, "It is one of the strongest interactions."),
                     ("Rifampicin only interacts with mycophenolate.", False, "Its key interaction here is with tacrolimus.")],
         "sources": ["subramanian2019"]},
        {"stem": "Which drug is most likely to raise tacrolimus levels?",
         "options": [("Clarithromycin.", True, "A CYP3A inhibitor."),
                     ("Rifampicin.", False, "Lowers levels."),
                     ("Carbamazepine.", False, "Lowers levels."),
                     ("Phenytoin.", False, "Lowers levels.")],
         "sources": []},
        {"stem": "In ELITE-Symphony, which regimen had the lowest biopsy-proven acute rejection rate?",
         "options": [("Low-dose tacrolimus with mycophenolate and steroids (12.3 percent).", True, "It also had the best kidney function and graft survival."),
                     ("Low-dose sirolimus.", False, "Highest rejection rate (37.2 percent)."),
                     ("Standard-dose cyclosporine.", False, "25.8 percent."),
                     ("Steroids alone.", False, "Not a study arm.")],
         "sources": ["ekberg2007"]},
        {"stem": "What is the most important safety concern with mycophenolate in women of reproductive age?",
         "options": [("It causes serious birth defects and miscarriage, so pregnancy intentions and contraception must be addressed early.", True, "A possible pregnancy on mycophenolate is urgent."),
                     ("It causes weight gain.", False, "Not the main concern."),
                     ("It raises tacrolimus levels.", False, "Not a major interaction."),
                     ("It is safe in pregnancy.", False, "It is teratogenic.")],
         "sources": []},
        {"stem": "Can a patient switch from twice-daily immediate-release tacrolimus to a once-daily product using the same milligram dose without a plan?",
         "options": [("No. Formulations are not interchangeable milligram for milligram; switches need a team plan and follow-up level.", True, "Exposure can change."),
                     ("Yes, the dose is identical.", False, "Not interchangeable."),
                     ("Yes, if the brand is the same company.", False, "Still requires a plan."),
                     ("Only pharmacists can decide, without telling the team.", False, "Team-directed.")],
         "sources": []},
        {"stem": "What does a low tacrolimus concentration-to-dose ratio suggest?",
         "options": [("A fast metabolizer, associated in one cohort with lower eGFR and more CNI toxicity and BK nephropathy.", True, "Observational marker for closer attention."),
                     ("Excellent adherence.", False, "C/D does not measure adherence directly."),
                     ("The dose is too high.", False, "It reflects metabolism relative to dose."),
                     ("Rejection is impossible.", False, "False.")],
         "sources": ["tholking2014"]},
        {"stem": "What does high tacrolimus intrapatient variability (IPV) indicate?",
         "options": [("Large swings in troughs on an unchanged dose, associated with rejection and graft loss and often with nonadherence.", True, "A risk marker prompting review."),
                     ("A stable, ideal regimen.", False, "High IPV is unfavorable."),
                     ("Laboratory error only.", False, "Usually reflects patient factors."),
                     ("That the dose must be doubled.", False, "Prompts review, not automatic dose change.")],
         "sources": ["shuker2015"]},
        {"stem": "A patient will run out of tacrolimus in three days. What is the immediate nursing task?",
         "options": [("Confirm remaining supply and schedule, contact the team and pharmacy urgently, arrange an authorized continuity plan and confirm it with the patient.", True, "Supply gaps risk rejection."),
                     ("Tell him to take half doses to stretch supply.", False, "Unauthorized dose change."),
                     ("Advise him to borrow from another patient.", False, "Unsafe."),
                     ("Note it for the next clinic visit.", False, "Too late.")],
         "sources": []},
        {"stem": "Among solid-organ recipients, which group had the highest immunosuppressant nonadherence rate in the meta-analysis?",
         "options": [("Kidney recipients, about 36 cases per 100 patients per year.", True, "Compared with 7 to 15 in other organs."),
                     ("Heart recipients.", False, "Lower for immunosuppressants."),
                     ("Liver recipients.", False, "Lower."),
                     ("No differences were found.", False, "Rates differed by organ.")],
         "sources": ["dew2007"]},
        {"stem": "Which question best screens for nonadherence?",
         "options": [("'Many people miss a dose now and then. In the last month, how many times has that happened to you?'", True, "Normalizing, specific and time-bound."),
                     ("'You always take your medicines, right?'", False, "Leading."),
                     ("'Why are you not taking your medicines?'", False, "Accusatory."),
                     ("'Your levels prove you are noncompliant.'", False, "Judgmental and possibly wrong.")],
         "sources": ["dew2007"]},
        {"stem": "Which adverse effect is characteristic of calcineurin inhibitors?",
         "options": [("Tremor, high potassium, low magnesium and new-onset diabetes.", True, "Classic CNI effects."),
                     ("Mouth ulcers and high lipids.", False, "More typical of mTOR inhibitors."),
                     ("Diarrhea and low white cells.", False, "More typical of mycophenolate."),
                     ("Hair loss only.", False, "Not characteristic.")],
         "sources": []},
        {"stem": "What did the seven-year BENEFIT follow-up show for belatacept versus cyclosporine?",
         "options": [("A 43 percent lower risk of death or graft loss, with eGFR rising over time.", True, "Hazard ratio 0.57 with both belatacept regimens."),
                     ("Higher mortality with belatacept.", False, "Lower."),
                     ("No difference in any outcome.", False, "A significant difference was found."),
                     ("Fewer early rejections with belatacept.", False, "Early rejection was more frequent with belatacept.")],
         "sources": ["vincenti2016"]},
    ],
    "exam": [
        {"stem": "A tacrolimus level was drawn after the morning dose, and the patient plans to start an outside prescription. What is the correct nursing response?",
         "options": [("Flag the timing, document dose and draw times, reconcile the proposed drug, and confirm pharmacy and team follow-up.", True, "Prevents misinterpretation and an interaction."),
                     ("Report the level as a trough and approve the prescription.", False, "Misleading and outside scope."),
                     ("Adjust the dose yourself.", False, "Unauthorized."),
                     ("Tell her to stop tacrolimus until the level is repeated.", False, "Dangerous.")],
         "sources": ["tholking2014"]},
        {"stem": "A patient is about to run out of tacrolimus. What is the immediate task?",
         "options": [("Confirm supply and schedule, contact team and pharmacy urgently, arrange an authorized continuity plan, and confirm with the patient.", True, "Prevents a gap."),
                     ("Advise skipping alternate doses.", False, "Unauthorized."),
                     ("Wait for the next visit.", False, "Too late."),
                     ("Substitute another immunosuppressant.", False, "Unauthorized.")],
         "sources": ["dew2007"]},
        {"stem": "Which statement about tacrolimus and rifampicin is correct?",
         "options": [("Rifampicin lowers tacrolimus levels and the team must be told before it starts.", True, "Strong CYP3A induction."),
                     ("They can be combined without monitoring.", False, "Unsafe."),
                     ("Rifampicin raises tacrolimus.", False, "It lowers it."),
                     ("Only the TB clinic needs to know.", False, "The transplant team must be informed.")],
         "sources": ["subramanian2019"]},
    ],
}
