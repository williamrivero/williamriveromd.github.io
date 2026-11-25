# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Why a rising creatinine in a recipient who feels perfectly well can be the first and only sign of rejection, how to sort the other causes before anyone says the word, what a biopsy and the newer blood tests can and cannot tell you, and how to keep a biopsy patient safe.",
    "desc": "Transplant Nurse Module 7: kidney graft dysfunction, differential diagnosis of rising creatinine, T-cell-mediated and antibody-mediated rejection (Banff 2022), donor-specific antibodies, donor-derived cell-free DNA, kidney allograft biopsy complications and nursing care, and rejection treatment monitoring for Philippine registered nurses.",
    "keywords": "kidney transplant rejection signs nurse, rising creatinine after transplant, antibody-mediated rejection, transplant kidney biopsy complications, donor-derived cell-free DNA, Banff classification",
    "image_alt": "A nurse checking the biopsy site and urine color of a kidney transplant recipient lying flat after a graft biopsy, with a vital-sign chart at the bedside.",
    "objectives": [
        "Compare a creatinine result with the individual's own baseline and trajectory to judge whether it is actionable.",
        "List the competing causes of graft dysfunction and the nursing data that point toward each.",
        "Explain the difference between T-cell-mediated and antibody-mediated rejection in plain terms.",
        "Describe what biopsy, donor-specific antibody and donor-derived cell-free DNA results can and cannot show.",
        "Prepare a patient for graft biopsy and recognize post-biopsy bleeding.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A smoke alarm with no sound",
         "html": """
<p>Rejection is a fire that usually starts without smoke you can see or smell. The transplanted kidney has no pain fibers that fire early, and it keeps making urine until injury is advanced. The only alarm most patients have is a laboratory value: creatinine creeping up from their own baseline, sometimes with new protein in the urine. By the time a patient feels unwell, much of the damage may be done.</p>
<p>The alarm is also nonspecific. Creatinine rises with dehydration, too much tacrolimus, a blocked stent, an infection, a virus, or rejection. A good nurse does not shout "rejection" at the first beep, and does not silence the alarm because the patient "feels fine." The nurse gathers the clues that let the team find the fire quickly.</p>
"""},
        {"id": "trend", "nav": "Start with the trend", "tag": "Physiology", "h2": "Is this creatinine actionable?",
         "html": """
<p>Creatinine is filtered freely and secreted slightly. Its blood level therefore rises roughly in inverse proportion to glomerular filtration. With a single kidney, a small absolute rise can mean a large proportional loss of function.</p>
<p>Take a recipient whose stable baseline is 1.1 mg/dL. Today the result is 1.4 mg/dL. That is a 27 percent rise. It is meaningful, even though 1.4 might look "near normal" on the laboratory report.</p>
<p>Compare every value with the patient's own baseline and recent trajectory, not the laboratory reference range. Most programs specify a percentage or absolute rise that triggers review; know yours. The <a href="calc-allograft-egfr-trend.html">Allograft eGFR Trend</a> calculator helps you see the slope.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mr. Domingo's creatinine is 1.5 mg/dL. His usual is 1.1. He feels perfectly well and is annoyed that you want to talk before he goes home.</p><p>You ask your list of questions. He has had loose stools for four days. He started taking a mefenamic acid tablet each night for a toothache. His tacrolimus was drawn after breakfast, and he took the dose at 6 a.m. You record all three, and you call the transplant nephrologist with the creatinine, the clues, and the fact that the level is not a trough.</p><p class="tc-scene-take"><b>What this shows.</b> When you call with the clues already gathered, the team can sort dehydration, a drug effect and rejection in one conversation instead of three.</p></div>

<p><strong>Gather the clues before you call.</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Possible cause</th><th>Clues the nurse can collect</th></tr></thead>
<tbody>
<tr><td>Low volume or perfusion</td><td>Vomiting, diarrhea, poor intake, new diuretic or blood pressure drug, orthostatic dizziness, weight loss</td></tr>
<tr><td>Calcineurin inhibitor toxicity</td><td>High or mistimed tacrolimus level, new interacting drug, tremor, diarrhea raising absorption</td></tr>
<tr><td>Rejection</td><td>Missed doses, low or highly variable levels, recent dose reduction, new donor-specific antibodies; often no symptoms</td></tr>
<tr><td>Infection</td><td>Fever, dysuria, graft tenderness (pyelonephritis), cytomegalovirus or BK polyomavirus results (Module 8)</td></tr>
<tr><td>Obstruction</td><td>Retained stent past its removal date, swelling near the graft (lymphocele), falling urine, hydronephrosis on ultrasound</td></tr>
<tr><td>Vascular</td><td>New severe hypertension and a graft bruit (transplant renal artery stenosis), especially months after surgery</td></tr>
<tr><td>Recurrent disease</td><td>New proteinuria or hematuria in a patient whose original disease can recur (for example IgA nephropathy, focal segmental glomerulosclerosis)</td></tr>
</tbody></table></div>
"""},
        {"id": "rejection", "nav": "Types of rejection", "tag": "Physiology", "h2": "T cells and antibodies: two ways to reject",
         "html": """
<p><strong>T-cell-mediated rejection (TCMR).</strong> Recipient T lymphocytes recognize donor HLA, enter the graft and attack tubules and, in severe cases, arteries. It is the classic early rejection, often linked to inadequate immunosuppression or missed doses, and it usually responds to pulse corticosteroids or, if severe, anti-thymocyte globulin.</p>
<p><strong>Antibody-mediated rejection (ABMR).</strong> Antibodies against donor HLA, either present before transplant or formed later (de novo donor-specific antibodies), bind the endothelium of the graft's small vessels and recruit complement and inflammatory cells. The biopsy shows inflammation in glomerular and peritubular capillaries (microvascular inflammation). Chronic ABMR is the leading immunologic cause of late graft loss, and nonadherence is a frequent trigger.[[schinstock2019]] It is harder to treat; options include plasmapheresis, intravenous immunoglobulin (IVIG) and optimizing maintenance therapy.</p>
<p>The Banff classification, updated at the 2022 meeting, standardizes how pathologists label these patterns. It added categories that recognize microvascular inflammation even when donor-specific antibodies cannot be detected, reflecting growing evidence that the injury pattern matters more than a single antibody test.[[naesens2024]] For the nurse, the practical point is simple: the biopsy diagnosis, interpreted with the antibody results and clinical picture, guides treatment, and the team will explain which type is present.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Kevin, 24, had a transplant two years ago. His tacrolimus levels have swung between 3 and 11 ng/mL on the same dose for the past six months. Today his creatinine has risen and new donor-specific antibodies are reported. He says he never misses a dose.</p><p>You do not argue. You ask the normalizing question from Module 6: "Many people miss a dose now and then. In the last month, how many times has that happened?" He admits he often skips the evening dose when he works night shifts at a call center. You document what he said, without judgment, and share it with the team before the biopsy.</p><p class="tc-scene-take"><b>What this shows.</b> Antibody-mediated rejection often has a behavioral story behind it. The nurse who hears that story changes the treatment plan.</p></div>

<div class="tc-keyp"><span class="tc-lab">Remember</span>A rise in creatinine triggers an evaluation for rejection <em>and</em> for other causes. It does not establish rejection. Neither does a normal creatinine exclude it, which is why some centers do protocol biopsies and antibody surveillance.</div>
"""},
        {"id": "proteinuria", "nav": "Protein in the urine", "tag": "Physiology", "h2": "Protein in the urine: the second signal",
         "html": """
<p>Creatinine tells you how much the kidney filters. Protein in the urine tells you how well the filter holds together. The two can move separately, so a graft can have a stable creatinine and still be in trouble.</p>
<p><strong>Why protein leaks.</strong> The glomerular filter is a three-layer barrier: the cells lining the capillary, a basement membrane, and the podocytes, cells whose interlocking foot processes form the final slit. Healthy filters hold back albumin and larger proteins. Injury to any layer lets protein through. In a transplant, three kinds of injury are common causes. Antibody-mediated rejection inflames the capillaries. A recurrent or new glomerular disease attacks the podocytes or the basement membrane. Some drugs, such as mTOR inhibitors, can increase protein leak. Protein in the urine is also, independently, a marker of higher cardiovascular risk.</p>
<p><strong>Measuring it well.</strong> A dipstick gives a rough signal. Most programs follow the urine protein-to-creatinine ratio, or the albumin-to-creatinine ratio, on a spot sample, which corrects for how concentrated the urine is. A first-morning sample is often preferred because protein loss varies through the day. Collect a clean midstream sample, label it with the date and time, and avoid sampling during a urinary infection, menstruation or after heavy exercise when you can, because each can raise the result. Compare each value with the patient's own previous results.</p>
<p><strong>When protein rises fast.</strong> Some diseases come back in the new kidney. Focal segmental glomerulosclerosis can recur very early, sometimes within days of transplant, with heavy protein loss, swelling and foamy urine. A sudden, large rise in protein in a patient whose original kidney disease is known to recur needs the team that day. Know your patient's original diagnosis; it is in the referral and it matters for the rest of the graft's life.</p>
<div class="tc-scene"><span class="tc-lab">On the transplant ward, day 5 &middot; fictional</span><p>Aaron, 19, lost his own kidneys to focal segmental glomerulosclerosis. His new kidney is working well and his creatinine is falling. On day five you notice his urine is frothy and his ankles are puffy. His weight is up 2 kilograms since yesterday, although his fluid balance is even.</p><p>You send a spot urine for protein-to-creatinine ratio as your standing orders allow, and tell the resident about the froth, the edema, the weight and his original diagnosis. The result is very high. The team starts its protocol for recurrence that evening.</p><p class="tc-scene-take"><b>What this shows.</b> A falling creatinine does not mean all is well. Knowing the patient's original disease told you what frothy urine might mean.</p></div>
<div class="tc-keyp"><span class="tc-lab">Remember</span>Creatinine and protein are two different signals. Follow both against the patient's own baseline, and know which original diseases can come back.</div>
"""},
        {"id": "tests", "nav": "Tests", "tag": "Evidence", "h2": "What the tests can and cannot tell you",
         "html": """
<p><strong>Biopsy</strong> remains the reference standard for diagnosing rejection and distinguishing it from toxicity, infection and recurrent disease.</p>
<p><strong>Donor-specific antibodies (DSA)</strong> in the blood show humoral sensitization against the donor. Their presence raises suspicion of ABMR and their appearance after transplant is a warning sign, but not every DSA causes injury.</p>
<p><strong>Donor-derived cell-free DNA (dd-cfDNA)</strong> measures DNA fragments released by injured graft cells. In a prospective study of 102 recipients, a level below 1 percent had a negative predictive value of 84 percent for active rejection and 96 percent for ABMR, while positive predictive values were lower (61 and 44 percent).[[bloom2017]] In other words, a low result is reassuring, especially against ABMR; a high result signals injury that still needs a biopsy to explain. Availability and cost in the Philippines are limited.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>A recipient's relative, a nurse working abroad, sends a message: "Can't you just do the cell-free DNA test instead of a biopsy? It's safer."</p><p>You explain what the test can and cannot do: a low result is reassuring, especially against antibody-mediated rejection; a high result shows injury but not its cause, so it would still lead to a biopsy. The decision about which test fits this situation belongs to the transplant nephrologist, and you pass the question on.</p><p class="tc-scene-take"><b>What this shows.</b> A new test is a tool with known strengths and limits, not a replacement for the reference standard.</p></div>

"""},
        {"id": "biopsy", "nav": "Biopsy care", "tag": "Practice", "h2": "Keeping a biopsy patient safe",
         "html": """
<p>A transplant kidney lies close to the skin, which makes it easier to biopsy than a native kidney. Complications are uncommon but real. A meta-analysis of 72 studies and more than 40,000 allograft biopsies found pooled rates of 3.2 percent for visible blood in the urine, 0.3 percent for bleeding needing transfusion, and 0.9 percent for major complications; visible hematuria was more common in middle-income than high-income countries (6.4 versus 2.6 percent).[[ho2022]] Graft loss and death were extremely rare.</p>
<p><strong>Before the biopsy</strong></p>
<ul>
<li>Verify the order, consent, identity and indication.</li>
<li>Ask specifically about antiplatelet drugs, anticoagulants and herbal products, with the name and the time of the last dose, and report them to the procedural team; the team decides whether to proceed.</li>
<li>Check the ordered blood count, coagulation tests, and blood pressure; uncontrolled hypertension increases bleeding risk.</li>
<li>Follow fasting and medication instructions as ordered; desmopressin is sometimes used, although prospective evidence for routine use is limited and absent for transplant biopsies.[[lim2021]]</li>
</ul>
<p><strong>After the biopsy</strong></p>
<ul>
<li>Bed rest and vital signs at the ordered intervals (often frequent for the first hours).</li>
<li>Inspect the site, ask about pain, and check the color of every void.</li>
<li>Check the ordered post-procedure hemoglobin.</li>
<li>Teach the patient to report dizziness, worsening pain, or red urine or clots after discharge.</li>
</ul>
<div class="tc-stop"><span class="tc-lab">Stop and call</span>New or severe pain at the graft, hypotension or rising heart rate, visible hematuria with clots, urinary retention from clots, or a falling hemoglobin after biopsy need immediate escalation.</div>
<div class="tc-scene"><span class="tc-lab">On the day-procedure unit &middot; fictional</span><p>During the pre-biopsy check you ask Mrs. Lopez what she took this week, "including anything from the drugstore or herbal." Her list has no aspirin. Then she mentions the "heart tablet" her cardiologist gave her after a stent last year, 75 mg every morning. It is clopidogrel, and she took it today.</p><p>You tell the procedural team before she is moved. The biopsy is rescheduled, and the team decides, with her cardiologist, how to manage the antiplatelet drug.</p><p class="tc-scene-take"><b>What this shows.</b> Asking about every tablet by name, with the time of the last dose, is how bleeding risk is found before the needle, not after.</p></div>

<p><strong>During rejection treatment</strong>, monitor for the effects of the ordered therapy: high glucose, mood change and infection with pulse steroids; fever, rigors, low blood pressure and low blood counts with anti-thymocyte globulin; line care, fluid balance and calcium with plasmapheresis; and infusion reactions with IVIG.</p>
"""},
        {"id": "talking", "nav": "Talking about rejection", "tag": "Communication", "h2": "After the diagnosis: talking about rejection and slow decline",
         "html": """
<p>For many recipients, the word "rejection" means the kidney is lost. The diagnosis often comes with fear, guilt and blame. How you talk with the patient in the days after a biopsy shapes whether he keeps trusting the team and keeps taking his medicines.</p>
<p><strong>Explain what rejection is and is not.</strong> Rejection means the immune system is attacking the kidney. Many episodes, especially T-cell-mediated rejection found early, respond to treatment. Chronic antibody-mediated rejection is harder to treat and is the leading immunologic cause of late graft loss.[[schinstock2019]] Do not predict the outcome. Say what the team has found, what the treatment is for, and when the next results will tell more. Leave the prognosis to the nephrologist, and be present when it is discussed if you can.</p>
<p><strong>Talk about adherence without accusation.</strong> If missed doses may have contributed, the patient often knows it already. Shame makes people hide more. Ask in a neutral way: "Many people find it hard to take every dose. In the last month, how many doses do you think you missed?" Then look for the reason, such as cost, side effects, a confusing schedule, depression or a school timetable, and route it to the person who can help. In a multicenter cohort of recipients who developed new donor-specific antibodies, nonadherence was the strongest predictor of later graft failure.[[schinstock2019]] That is a reason to solve the barrier, not to blame the patient.</p>
<p><strong>After treatment, the risk calendar resets.</strong> Pulse steroids or anti-thymocyte globulin raise infection risk for months, as Module 8 explains. The team often restarts infection prophylaxis and orders more frequent blood tests and level checks. Teach the patient why the visits have suddenly increased, so the extra burden feels purposeful.</p>
<h3>When the kidney is slowly failing</h3>
<p>Some grafts decline over years, from repeated rejection, scarring, drug toxicity or recurrent disease. The creatinine creeps up visit by visit. Patients often sense it before they are told. A graft that is failing raises the same questions as native kidney failure did: preparing a dialysis access, considering a second transplant, and planning conservative care if that fits the patient's wishes. Starting these conversations early, as in Module 1, prevents an emergency start of dialysis through a catheter. Module 9 covers the practical steps.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Six years after her transplant, Mrs. Agustin's eGFR has fallen from 52 to 21. At today's visit she asks you quietly, "Is my kidney dying?"</p><p>You do not deflect. You say that the kidney is working less well each year, that Dr. Santos will talk with her today about what that means, and that there are things to plan now, such as a fistula and the question of a second transplant, so that nothing has to happen in a rush. You ask if she would like her daughter to join the conversation. You tell Dr. Santos what she asked before he comes in.</p><p class="tc-scene-take"><b>What this shows.</b> A failing graft needs the same early planning as failing native kidneys. Answer honestly, prepare the doctor, and bring the family in.</p></div>
"""},
    ],
    "case": {
        "title": "Two missed doses and a new antibiotic",
        "html": """
<p><strong>Wednesday, 8:45 a.m., transplant clinic.</strong> Mr. Navarro, 49, is two months after a deceased-donor transplant. He works as a sales agent and is cheerful and in a hurry. His creatinine today is 1.9 mg/dL. Over the past month it has been 1.3 to 1.4.</p>
<p>"I feel great, Nurse. Can I go? I have a client at ten." You ask your questions. Last week he traveled to Davao for work and "forgot the evening tablets twice, but I took double the next morning." Four days ago a doctor there started him on ciprofloxacin for burning on urination. He is still taking it.</p>
<p>His blood pressure is 148/90 mmHg, higher than usual. The chart shows his ureteric stent was due for removal two weeks ago; there is no record that it was removed.</p>
""",
        "acte": {
            "Assess": "Exact dates of missed doses, current symptoms (dysuria, fever, graft tenderness), fluid intake, urine output, weight change, medicines including the antibiotic and any NSAIDs, timing of his last tacrolimus level, and whether the stent has been removed.",
            "Communicate": "Alert the transplant team the same day with an SBAR: a 40 percent rise from baseline, missed doses, recent antibiotic for a urinary infection, blood pressure, and the stent status. Request the ordered urine culture, tacrolimus trough, ultrasound and antibody tests, each with a named result owner.",
            "Teach": "Explain that feeling well does not mean the kidney is safe, that this rise needs prompt evaluation, and why missed doses matter. Plan doses around travel using teach-back.",
            "Escalate": "Arrange ordered reassessment promptly rather than at the next routine visit. If biopsy is planned, begin the pre-biopsy checklist, including antithrombotics.",
        },
        "task": "Write a trend-based SBAR and a results-tracking entry listing each ordered test, its owner and the date it will be reviewed.",
        "outcome": """
<p>The nurse in the story did not let him leave for his client. She explained, briefly, that a 40 percent rise needs a same-day look even when he feels well, and that doubling a dose the next morning does not undo a missed one.</p>
<p>Her call to Dr. Santos listed everything at once: the creatinine trend, the two missed doses and the doubled one, the urinary infection and the antibiotic, the blood pressure, and the stent that was never removed. Dr. Santos ordered a urine culture, a correctly timed tacrolimus level, an ultrasound and donor-specific antibodies. The nurse wrote each test in the tracker with its owner and review date.</p>
<p>The ultrasound showed mild swelling of the kidney around the retained stent. The stent was removed, the infection treated, and his creatinine settled to 1.5. Because of the missed doses, the team also planned a biopsy; that is where the second round begins.</p>
""",
    },
    "second_round": ("Before the planned biopsy he mentions taking a daily aspirin his cardiologist prescribed, last taken this morning.", "A pre-biopsy checklist with the medication, last dose time, procedural contact and the documented decision owner."),
    "evidence_out": "Trend-based SBAR and biopsy safety checklist.",
    "critical": "Telling an asymptomatic patient to delay evaluation because he feels well.",
    "reflect": "How does your unit define an actionable creatinine rise for a recipient, and who owns the result when it comes back on a weekend?",
    "practice": {
        "intro": "On the ward and in clinic.",
        "items": [
            "Calculate the percentage change from baseline for three synthetic creatinine results and decide which are actionable.",
            "Collect a full differential history (volume, drugs, levels, infection, obstruction) and present it as an SBAR.",
            "Prepare a patient for graft biopsy using the checklist, including antithrombotics.",
            "Perform post-biopsy monitoring at the ordered intervals and document urine color and site checks.",
            "Observe the administration of a rejection therapy and the monitoring it requires.",
        ],
    },
    "readings": [
        ("transplant-allograft-failure.html", "How grafts fail and what follows."),
        ("highly-sensitized-kidney-transplant-candidates-clinician.html", "Antibodies, sensitization and ABMR risk."),
        ("kidney-transplant.html", "Patient overview of rejection."),
    ],
    "calcs": ["calc-allograft-egfr-trend.html"],
    "terms": [
        ("Microvascular inflammation", "Inflammatory cells in the graft's glomerular and peritubular capillaries, a hallmark of antibody-mediated rejection."),
        ("Banff classification", "The international standard for classifying kidney transplant biopsy findings."),
        ("Negative predictive value", "The probability that a person with a negative test truly does not have the condition."),
        ("Plasmapheresis", "A procedure that removes plasma, including antibodies, and replaces it with other fluid."),
        ("Recurrent disease", "Return of the original kidney disease in the transplanted kidney."),
    ],
    "quiz": [
        {"stem": "A recipient's baseline creatinine is 1.1 mg/dL; today it is 1.4 mg/dL and she feels well. What is the best interpretation?",
         "options": [("A 27 percent rise from her baseline that warrants evaluation.", True, "Compare with the individual's own baseline."),
                     ("Normal, because it is within the laboratory range.", False, "Reference ranges miss proportional loss with one kidney."),
                     ("Proof of rejection.", False, "It triggers evaluation; it does not prove rejection."),
                     ("Irrelevant if urine output is good.", False, "Urine output does not exclude graft dysfunction.")],
         "sources": []},
        {"stem": "Does a rise in creatinine establish rejection?",
         "options": [("No. It triggers evaluation for rejection and other causes of graft dysfunction.", True, "Many causes raise creatinine."),
                     ("Yes, always.", False, "Volume, drugs, infection and obstruction also raise it."),
                     ("Yes, if above 2 mg/dL.", False, "No cutoff proves rejection."),
                     ("Only in living-donor kidneys.", False, "Applies to all.")],
         "sources": ["naesens2024"]},
        {"stem": "Why can rejection be clinically silent?",
         "options": [("The graft has few early pain signals and keeps making urine until injury is advanced; creatinine may be the only sign.", True, "Rejection often presents only in laboratory values."),
                     ("Rejection never causes injury.", False, "It causes serious injury."),
                     ("Immunosuppressants mask all laboratory changes.", False, "Laboratory changes still occur."),
                     ("Rejection only happens in the first week.", False, "It can occur at any time.")],
         "sources": []},
        {"stem": "Which feature characterizes antibody-mediated rejection?",
         "options": [("Antibodies against donor HLA injure the graft's small vessels, causing microvascular inflammation.", True, "ABMR targets the endothelium."),
                     ("T cells attack tubules only.", False, "That describes TCMR."),
                     ("It is caused by a blocked catheter.", False, "Not immunologic."),
                     ("It always responds to a single dose of steroids.", False, "ABMR is harder to treat.")],
         "sources": ["naesens2024", "schinstock2019"]},
        {"stem": "In recipients with de novo DSA, which factor most strongly predicted graft failure?",
         "options": [("Medication nonadherence (hazard ratio about 6.5).", True, "Nonadherence is a major driver of antibody-mediated graft loss."),
                     ("Blood type O.", False, "Not reported."),
                     ("Female sex.", False, "Not the strongest predictor."),
                     ("A living donor.", False, "Not reported as a predictor.")],
         "sources": ["schinstock2019"]},
        {"stem": "A dd-cfDNA result is below 1 percent. How should it be interpreted?",
         "options": [("Reassuring, especially against antibody-mediated rejection, but not a substitute for clinical judgment.", True, "High negative predictive value; lower positive predictive value."),
                     ("Proof of rejection.", False, "Low levels argue against active rejection."),
                     ("Meaningless.", False, "It has useful negative predictive value."),
                     ("An indication for immediate rejection treatment.", False, "Treatment requires diagnosis.")],
         "sources": ["bloom2017"]},
        {"stem": "In the allograft biopsy meta-analysis, roughly how often did bleeding require transfusion?",
         "options": [("About 0.3 percent.", True, "Major complications about 0.9 percent; gross hematuria about 3.2 percent."),
                     ("About 30 percent.", False, "Far too high."),
                     ("Never.", False, "It occurs, rarely."),
                     ("About 10 percent.", False, "Too high.")],
         "sources": ["ho2022"]},
        {"stem": "A patient reports taking aspirin this morning before a planned graft biopsy. What should the nurse do?",
         "options": [("Record the drug and last dose time and inform the procedural team, who decide whether to proceed.", True, "Antithrombotic status is a key pre-biopsy safety check."),
                     ("Proceed; aspirin does not matter.", False, "Aspirin increases bleeding risk."),
                     ("Cancel the biopsy yourself.", False, "The team decides."),
                     ("Give a reversal drug on your own.", False, "Outside scope.")],
         "sources": ["ho2022"]},
        {"stem": "Which finding after a graft biopsy needs immediate escalation?",
         "options": [("Hypotension, rising heart rate and visible clots in the urine.", True, "Suggests significant bleeding."),
                     ("Mild soreness at the site.", False, "Expected."),
                     ("Asking for a meal after the fasting period.", False, "Not concerning."),
                     ("Light pink first void that clears.", False, "May occur; continue monitoring.")],
         "sources": ["ho2022"]},
        {"stem": "What is the current evidence for routine desmopressin before kidney biopsy?",
         "options": [("Limited for native biopsies and absent for transplant biopsies; use follows the team's protocol.", True, "Systematic review found insufficient evidence for routine use."),
                     ("Strong evidence that it prevents all bleeding.", False, "Not supported."),
                     ("Proven harmful.", False, "Not shown."),
                     ("Mandatory by guideline.", False, "Not a guideline mandate.")],
         "sources": ["lim2021"]},
        {"stem": "A recipient has a retained ureteric stent four months after surgery and rising creatinine. What should be considered?",
         "options": [("Obstruction or infection from the retained stent.", True, "Forgotten stents encrust and obstruct."),
                     ("Normal healing.", False, "Stents are usually removed within weeks."),
                     ("Rejection only.", False, "Other causes must be considered."),
                     ("Dehydration only.", False, "The stent is an important clue.")],
         "sources": ["wilson2013"]},
        {"stem": "What did the 2022 Banff meeting add?",
         "options": [("Recognition of microvascular inflammation patterns even when DSA is not detected.", True, "Refined phenotypes of antibody-mediated injury."),
                     ("Elimination of biopsy as a diagnostic tool.", False, "Biopsy remains the standard."),
                     ("A rule that creatinine alone diagnoses rejection.", False, "Not the case."),
                     ("New organ allocation rules.", False, "Banff concerns pathology.")],
         "sources": ["naesens2024"]},
        {"stem": "Which monitoring is most relevant during pulse methylprednisolone for rejection?",
         "options": [("Blood glucose, mood and signs of infection.", True, "Steroid effects."),
                     ("Hearing tests.", False, "Not typical."),
                     ("Vision charts only.", False, "Not the priority."),
                     ("None is needed.", False, "Monitoring is required.")],
         "sources": []},
        {"stem": "New severe hypertension with a graft bruit months after transplant suggests what?",
         "options": [("Transplant renal artery stenosis.", True, "A vascular cause of graft dysfunction."),
                     ("Acute TCMR.", False, "Not typically associated with a bruit."),
                     ("Urine leak.", False, "Not consistent."),
                     ("Normal finding.", False, "Needs evaluation.")],
         "sources": []},
        {"stem": "Which history best supports CNI toxicity as a cause of rising creatinine?",
         "options": [("A recent new azole antifungal and tremor.", True, "Raised tacrolimus levels cause toxicity."),
                     ("Two missed tacrolimus doses.", False, "Suggests under-immunosuppression."),
                     ("Diarrhea with weight loss only.", False, "Suggests volume depletion, though diarrhea can raise levels."),
                     ("New proteinuria years later.", False, "May suggest recurrent disease or chronic ABMR.")],
         "sources": []},
    ],
    "exam": [
        {"stem": "A recipient two months after transplant has a creatinine 40 percent above baseline, feels well, missed two doses, and recently started an antibiotic. What should the nurse do?",
         "options": [("Obtain dates and medicine details, alert the team promptly, and arrange ordered reassessment with a named result owner.", True, "Prompt, owned evaluation."),
                     ("Reassure him and recheck in three months.", False, "Delays evaluation of possible rejection."),
                     ("Tell him he has rejection.", False, "Premature."),
                     ("Increase his tacrolimus dose.", False, "Unauthorized.")],
         "sources": ["naesens2024"]},
        {"stem": "What warrants prompt assessment after a graft biopsy?",
         "options": [("New severe pain, hypotension, visible bleeding or other signs of instability.", True, "Signs of significant bleeding."),
                     ("Mild discomfort.", False, "Expected."),
                     ("Hunger.", False, "Expected."),
                     ("Boredom during bed rest.", False, "Not clinical.")],
         "sources": ["ho2022"]},
        {"stem": "Which statement about dd-cfDNA is accurate?",
         "options": [("A low result has high negative predictive value, especially for ABMR; a high result signals injury needing further evaluation.", True, "Interpreted with clinical context."),
                     ("It replaces biopsy entirely.", False, "Biopsy remains the reference standard."),
                     ("A high result proves TCMR.", False, "Positive predictive value is modest."),
                     ("It measures tacrolimus levels.", False, "Unrelated.")],
         "sources": ["bloom2017"]},
    ],
}
