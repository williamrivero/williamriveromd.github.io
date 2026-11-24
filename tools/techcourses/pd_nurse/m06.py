# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 06: Monitoring, membrane testing and goal-directed PD.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain what &ldquo;goal-directed PD&rdquo; means and why the 2020 International Society for Peritoneal Dialysis (ISPD) recommendations moved away from a single clearance target.",
        "Describe what the Adequacy of Peritoneal Dialysis in Mexico (ADEMEX) trial and the Hong Kong randomized trial showed about increasing peritoneal small-solute clearance.",
        "Explain what a peritoneal equilibration test (PET) measures, when it is done, and how fast solute transfer and low ultrafiltration capacity change management.",
        "Collect timed effluent, urine and blood samples so that the results can be trusted.",
        "Prepare a structured nursing review that puts trends, delivered therapy and the person&rsquo;s goals in one picture for the team.",
    ],
    "big": """
<p>For years, peritoneal dialysis (PD) quality was judged by one number: weekly Kt/V urea. Randomized trials then showed that pushing that number higher did not help people live longer. The field moved to a broader question. Is this person feeling well, in fluid balance, eating, functioning and living the life they want, with the safest prescription that achieves it?</p>
<p>Your work is to bring the evidence for that question to every review: trends, delivered therapy, symptoms, nutrition, residual urine, and test results that were collected properly. A nephrologist can only interpret what you put in front of them. A result from a spoiled test, or a trend with no context, leads to the wrong decision as surely as a wrong order.</p>
{{plain:Think of a car&rsquo;s dashboard. Speed matters, but you also watch fuel, temperature and the warning lights. And the point of the journey is where the passengers want to go.}}
<p>The picture has a limit. A dashboard reports a machine. A person on PD has a membrane that changes with time and infection, kidneys that lose function, an appetite that waxes and wanes, and goals that shift. The readings must be interpreted against that person, not against a fixed specification.</p>
{{cards:Key terms for this module|Goal-directed PD::Care aimed at goals agreed with the person, not at a single number.|Kt/V::A laboratory measure of urea clearance, used as a surrogate for dialysis dose.|PET::A standardized 4-hour dwell that measures how fast solutes cross the membrane and how much water is removed.|D/P creatinine::The dialysate-to-plasma creatinine ratio; higher values mean faster transfer.|Surrogate::A laboratory or test value used in place of an outcome the patient feels.}}
""",
    "case": {"title": "The first PET", "html": """
<p><strong>Mr. Benjamin Cruz, 52</strong>, a hardware store owner in Marikina, has been on CAPD for 10 weeks. Nurse <strong>Hazel</strong> is preparing his first PET and a nursing review.</p>
<p><strong>PET day.</strong> Hazel confirms the protocol and solution strength against the order. The night dwell was done as instructed. The pre-test drain is complete. Samples are drawn at the ordered times. The final 4-hour drain measures 2,350 mL from 2,000 mL of 2.27% glucose solution: net UF +350 mL. D/P creatinine at 4 hours is reported as high relative to the unit&rsquo;s reference ranges.</p>
<p><strong>Trend data.</strong> Over five days, his weight rises from 68.0 to 70.0 kg. Daily UF falls from about 750 to 450 mL, and urine from about 600 to 350 mL. He reports mild breathlessness climbing the stairs to his stockroom. All exchanges were done. His night dwell drains less than it was filled on most days.</p>
""", "questions": ["Is the PET result valid? What could have spoiled it?",
                  "What does the five-day trend show?",
                  "What do you bring to the nephrologist, and what do you leave to them?"]},
    "sections": [
        ("what-the-evidence", "The clearance trials", "What the evidence showed about clearance", """
<p>Two randomized trials changed how PD adequacy is judged. Know them well enough to explain them to a patient who asks why the team no longer chases a higher number.</p>
<h3>ADEMEX</h3>
<p>ADEMEX (Mexico, 2002) randomized 965 CAPD patients either to continue four 2-liter exchanges daily or to a modified prescription aimed at a higher peritoneal creatinine clearance. Peritoneal clearance rose and stayed higher in the intervention group, but survival was the same (relative risk of death 1.00, 95% confidence interval 0.80 to 1.24). Two-year survival was about 68% in the control group and 69% in the intervention group.[[pd_paniagua2002]]</p>
<h3>The Hong Kong trial</h3>
<p>The Hong Kong trial (2003) randomized 320 new CAPD patients with little residual function to total weekly Kt/V targets of 1.5 to 1.7, 1.7 to 2.0, or above 2.0. Two-year survival did not differ significantly: 87%, 86% and 82%. More patients in the lowest-target group were withdrawn by their physicians for clinical problems, and more needed erythropoietin. The authors recommended a minimum total Kt/V above 1.7.[[pd_lo2003]]</p>
<h3>What this means</h3>
<p>Above a modest floor, more small-solute clearance does not buy survival. Kt/V is a surrogate: a laboratory measure of dose, not an outcome patients feel. The 2020 ISPD practice recommendations on prescribing high-quality goal-directed PD therefore treat Kt/V and creatinine clearance as one input among several, not as the definition of adequate dialysis. These recommendations are practice points, not graded recommendations, because the evidence base is limited.[[pd_brown2020]]</p>
<p>Both trials studied CAPD patients in specific populations two decades ago, and most of the Hong Kong patients had little residual function. They do not say that clearance is irrelevant. They say that beyond a floor, chasing the number is not the same as helping the person.</p>
{{key:Kt/V is a surrogate. Above a modest floor, raising it did not improve survival in trials. Read it alongside how the person is living.}}
"""),
        ("goal-directed-pd", "Goal-directed PD", "Goal-directed PD", """
<p>The 2020 ISPD recommendations describe care goals agreed through shared decision-making between the person and the team. The aim is both to let the person achieve their own life goals and to deliver high-quality care.[[pd_brown2020]] In practice, a review covers these domains.</p>
{{fig:pd06_dash}}
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>What you bring to the review</th></tr></thead>
<tbody>
<tr><td>Person&rsquo;s goals and symptoms</td><td>Energy, sleep, appetite, nausea, itch, restless legs, mood, ability to work or care for family</td></tr>
<tr><td>Fluid status</td><td>Weight trend, blood pressure, edema, breathlessness, daily UF, urine volume</td></tr>
<tr><td>Residual kidney function</td><td>Urine volume trend; timed urine collection when ordered</td></tr>
<tr><td>Delivered therapy</td><td>Exchanges done versus ordered, cycler completion, missed treatments</td></tr>
<tr><td>Nutrition</td><td>Appetite, weight change, diet history. The 2026 joint International Society of Renal Nutrition and Metabolism (ISRNM) and ISPD nutrition recommendations emphasize screening and monitoring nutrition, managing protein-energy wasting, and education that builds food literacy.[[pd_wang2026]]</td></tr>
<tr><td>Metabolic</td><td>Potassium (low potassium is common in PD and is a modifiable peritonitis risk factor in the 2022 ISPD recommendations), and glucose in people with diabetes[[pd_li2022]]</td></tr>
<tr><td>Solute clearance</td><td>Kt/V and creatinine clearance results, interpreted with the rest</td></tr>
<tr><td>Membrane function</td><td>PET results and UF capacity</td></tr>
</tbody></table></div>
<h3>Example: two patients, one Kt/V</h3>
<p><strong>Lola Pacita, 81</strong>, has a total Kt/V just above the unit&rsquo;s usual floor. She eats well, sleeps, walks to Sunday Mass and helps her granddaughter with homework. Her weight and blood pressure are steady. Her goal is to stay home and stay herself.</p>
<p><strong>Mr. Noel, 48</strong>, has the same Kt/V. He has lost 3 kg in two months, feels nauseated in the mornings and has stopped going to his tricycle route.</p>
<p>The number is identical. The reviews are not. For Lola Pacita you report a person meeting her goals. For Mr. Noel you report weight loss, nausea, lost function and his appetite history, and you flag the pattern for the nephrologist and the dietitian. The decision about either prescription is the nephrologist&rsquo;s. Your report decides whether they see the difference.</p>
{{key:Bring the person to the review, not just the results. Two identical numbers can describe two very different lives.}}
"""),
        ("the-peritoneal-equilibration", "The PET", "The peritoneal equilibration test", """
<h3>What it measures</h3>
<p>The PET characterizes how quickly small solutes cross the membrane, the peritoneal solute transfer rate (PSTR), and how much water a standard dwell removes.</p>
{{fig:pd06_pet}}
<h3>How it is done (ISPD 2021)</h3>
<p>A 4-hour dwell with either 2.27% glucose (2.5% dextrose) or 3.86% glucose (4.25% dextrose), using creatinine as the index solute. The key result is the dialysate-to-plasma creatinine ratio at 4 hours (D/P creatinine). Higher values mean faster transfer.[[pd_morelle2021]]</p>
<h3>When</h3>
<p>Early, between 6 and 12 weeks after starting PD (GRADE 1A for timing), and later when clinically indicated, for example after a fall in UF or after severe peritonitis.[[pd_morelle2021]]</p>
<h3>Why it matters</h3>
<ul>
<li>A faster PSTR is associated with lower survival on PD (GRADE 1A in the 2021 recommendations). Part of the reason is lower UF and more fluid reabsorption in long dwells.[[pd_morelle2021]]</li>
<li>That fluid problem can be mitigated by shortening glucose dwells, using icodextrin, or using higher glucose concentrations (GRADE 1A). Icodextrin, compared with glucose, can improve fluid status and reduce episodes of fluid overload (GRADE 1A).[[pd_morelle2021]]</li>
<li><strong>Low UF capacity</strong> should be suspected when net UF from a 4-hour PET is less than 400 mL with 3.86% glucose (4.25% dextrose) or less than 100 mL with 2.27% glucose (2.5% dextrose) (GRADE 1B), or when daily UF is not enough to keep the person euvolemic (practice point). Low UF can also come from mechanical problems or leaks.[[pd_morelle2021]]</li>
<li>When low UF is suspected, a 3.86% PET with measurement of the <strong>sodium dip at 1 hour</strong> helps identify intrinsic membrane dysfunction: reduced water transport through the aquaporins.[[pd_morelle2021]]</li>
</ul>
<h3>The nurse&rsquo;s part is accuracy</h3>
<p>The result is only as good as the timing of the samples, the completeness of the drain, the dwell length and the solution strength actually used.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What can spoil it</th></tr></thead>
<tbody>
<tr><td>Overnight dwell before the test</td><td>Wrong solution or length per protocol</td></tr>
<tr><td>Drain before the test dwell</td><td>An incomplete drain leaves residual fluid that dilutes the results</td></tr>
<tr><td>Infusion</td><td>Wrong strength; slow infusion shifts the timing</td></tr>
<tr><td>Samples at specified times</td><td>Missed or late samples</td></tr>
<tr><td>Blood sample</td><td>Not drawn at the specified time</td></tr>
<tr><td>Final drain</td><td>Incomplete; volume not measured accurately</td></tr>
<tr><td>Glucose correction for the creatinine assay</td><td>Some laboratory methods need correction for high dialysate glucose; confirm with the laboratory</td></tr>
</tbody></table></div>
<h3>Example: a PET that could not be trusted</h3>
<p>Mrs. Gemma&rsquo;s PET reports a 4-hour net UF of only +50 mL with 2.27% glucose, below the threshold that suggests low UF capacity. Before anyone labels her membrane, Nurse Hazel reviews the worksheet. The fill was started 25 minutes late because the warmer was occupied, but the samples were drawn by the clock, not by the dwell time. The final drain was stopped early when the patient needed the bathroom, and about 300 mL was estimated rather than measured.</p>
<p>Hazel reports exactly that: the result may reflect the test, not the membrane. The nephrologist orders a repeat. On the repeat, done carefully, her UF is well above the threshold. One spoiled test could have changed her prescription for months.</p>
{{key:A PET result is a measurement of the test as well as the membrane. Report any deviation with the result.}}
"""),
        ("adequacy-collections", "Adequacy collections", "Adequacy collections", """
<p>Weekly Kt/V and creatinine clearance in PD combine a 24-hour effluent collection, a 24-hour urine collection and a blood sample. Teach the patient exactly how to collect: the start and end times, all bags or a measured sample per protocol, the urine container, storage and transport.</p>
<p>Document missed samples. Ask the team whether an incomplete collection should be repeated.</p>
<h3>Example: the missing night bag</h3>
<p>Mr. Raul brings his 24-hour collection. While labeling, Nurse Hazel asks him to walk her through the day. He emptied the 6 AM bag into the toilet out of habit, then remembered. The collection is short by one exchange.</p>
<p>Hazel does not estimate the missing bag, and she does not send the sample as complete. She records the omission, tells the team and asks whether to repeat. A result calculated from three quarters of a day would understate his clearance and could prompt a prescription change he does not need.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common collection error</th><th>Effect on the result</th></tr></thead>
<tbody>
<tr><td>One effluent bag discarded</td><td>Clearance understated</td></tr>
<tr><td>Urine collection started with a full bladder</td><td>Urine clearance overstated</td></tr>
<tr><td>Urine passed at work not collected</td><td>Residual function understated</td></tr>
<tr><td>Blood drawn days away from the collection</td><td>Ratio may not reflect the collection period</td></tr>
</tbody></table></div>
{{key:An invalid collection is worse than none, because it looks like evidence.}}
"""),
        ("reading-trends", "Reading trends", "Reading trends", """
<p>State the baseline, the interval and the current value. Then give context: missed exchanges, changes in intake, falling urine, measurement changes, intercurrent illness, symptoms. A trend over a week is more informative than a single day.</p>
<div class="table-wrap"><table>
<thead><tr><th>Weak</th><th>Useful</th></tr></thead>
<tbody>
<tr><td>&ldquo;Weight is up.&rdquo;</td><td>&ldquo;Weight rose from 68.0 to 70.0 kg over five days while daily UF fell from about 750 to 450 mL and urine from about 600 to 350 mL. All exchanges done. Night dwell net negative most days. Mild breathlessness on stairs; none at rest.&rdquo;</td></tr>
<tr><td>&ldquo;Not eating well.&rdquo;</td><td>&ldquo;Weight down 3 kg in two months. Skipping breakfast because of nausea. Stopped working his tricycle route three weeks ago.&rdquo;</td></tr>
</tbody></table></div>
<p>Then separate three things in your handoff: what can be inferred, what still needs checking, and what needs escalation. &ldquo;Fluid is accumulating&rdquo; can be inferred. &ldquo;Is the scale the same?&rdquo; needs checking. &ldquo;Breathless at rest&rdquo; would need escalation today.</p>
{{key:Baseline, interval, current value, context. Then say what you infer, what you still need to check and what needs action.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is the PET valid?</strong> On the record, yes: protocol and solution strength confirmed against the order, the night dwell as instructed, a complete pre-test drain, samples at the ordered times and a measured final drain. If any of those had slipped, Hazel would report the deviation with the result. His net UF of +350 mL with 2.27% glucose is above the low-UF threshold of 100 mL for that strength.</p>
<p><strong>What the trend shows.</strong> Fluid is accumulating: 2 kg in five days, with both routes falling, UF and urine. His long night dwell is net negative most days. That pattern fits faster solute transfer with fluid reabsorption in the long dwell, which the high D/P creatinine supports.</p>
<p><strong>What Hazel brings.</strong> She screens for emergency signs and finds none at rest. She records the trends with dates, notes the net-negative long dwell, and presents the PET result with the observation that the pattern fits faster transfer and long-dwell reabsorption. She adds his breathlessness on the stairs and his falling urine.</p>
<p><strong>What she leaves to the nephrologist.</strong> She does not suggest a specific prescription. The nephrologist reviews and considers changes to the long dwell. Hazel teaches salt restriction and arranges a weight and symptom check in three days.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete all three tasks using the trend table your preceptor provides.",
               "items": [("Plot seven days of weight, UF and urine from the trend table.", False),
                         ("Mark the missed dwell.", False),
                         ("Write a five-line handoff that states what can be inferred, what needs verification and what needs escalation.", False)]},
    "quiz": [
        ("In ADEMEX, increasing peritoneal creatinine clearance:",
         ["Did not change survival (relative risk 1.00)", "Reduced mortality by half", "Increased mortality", "Was never achieved"], 0,
         "Clearance rose and stayed higher, but survival was the same."),
        ("Kt/V urea is best described as:",
         ["A patient-important outcome", "A measure of fluid removal", "A surrogate measure of dose", "A measure of membrane transport"], 2,
         "It is a laboratory surrogate, not an outcome patients feel."),
        ("The 2020 ISPD goal-directed prescribing recommendations are:",
         ["GRADE 1A recommendations", "Regulations", "Withdrawn", "Practice points"], 3,
         "They are labeled practice points because the evidence base is limited. Do not assign a grade."),
        ("When should the first PET be done according to the 2021 ISPD recommendations?",
         ["On day 1 of PD", "Between 6 and 12 weeks after starting PD", "After 5 years", "Only after peritonitis"], 1,
         "The timing carries GRADE 1A. Later PETs follow clinical indications."),
        ("A faster peritoneal solute transfer rate is associated with:",
         ["Better survival", "Lower survival on PD, partly through lower UF in long dwells", "No effect", "Fewer infections"], 1,
         "This is a GRADE 1A association in the 2021 recommendations."),
        ("Which 4-hour PET result suggests low UF capacity with 3.86% glucose?",
         ["Net UF more than 800 mL", "Net UF of exactly 1,000 mL", "Any positive UF", "Net UF less than 400 mL"], 3,
         "The ISPD 2021 threshold for 3.86% glucose is less than 400 mL (GRADE 1B)."),
        ("And with 2.27% glucose?",
         ["Net UF less than 100 mL", "Net UF less than 1,000 mL", "Net UF greater than 400 mL", "Not defined"], 0,
         "The threshold for 2.27% glucose is less than 100 mL."),
        ("What does the sodium dip at 1 hour of a 3.86% dwell help assess?",
         ["Infection", "Potassium balance", "Water transport through aquaporins (intrinsic membrane function)", "Catheter position"], 2,
         "A reduced dip suggests impaired free-water transport."),
        ("Mrs. Gemma&rsquo;s PET was filled 25 minutes late but sampled by the clock, and the final drain was estimated. What should you report?",
         ["The result as valid", "The result together with the deviations, so the team can decide whether to repeat", "Only the UF value", "Nothing, and repeat it yourself"], 1,
         "Report deviations with the result. A spoiled test can mislabel a membrane and change a prescription unnecessarily."),
        ("A 24-hour effluent collection missed one bag. Best action?",
         ["Record the omission, inform the team, and ask whether to repeat", "Report the result as complete", "Estimate the missing bag", "Discard the whole result silently"], 0,
         "Transparency preserves the result&rsquo;s meaning. An estimate looks like evidence but is not."),
        ("Which modifiable peritonitis risk factor named in the 2022 ISPD recommendations also appears in metabolic monitoring?",
         ["High sodium", "Low potassium", "High calcium", "Anemia"], 1,
         "Low potassium is common in PD and is a named modifiable risk factor."),
        ("In the Hong Kong trial, patients assigned to the lowest Kt/V target (1.5 to 1.7):",
         ["Had markedly lower survival", "Had better nutrition", "Were all transferred to hemodialysis", "Had similar survival but more clinical problems and more erythropoietin use"], 3,
         "Survival did not differ significantly, but more were withdrawn for clinical problems."),
        ("Lola Pacita and Mr. Noel have the same Kt/V. He has lost 3 kg and stopped working; she is meeting her goals. What should your reviews show?",
         ["Identical reports, since the numbers match", "Each person&rsquo;s symptoms, function, nutrition and goals alongside the number", "Only the Kt/V", "A recommendation to raise both prescriptions"], 1,
         "Clearance is one input among many. Your report decides whether the nephrologist sees the difference."),
        ("Icodextrin compared with glucose for the long dwell:",
         ["Worsens fluid status", "Can improve fluid status and reduce fluid-overload episodes (GRADE 1A)", "Prevents peritonitis", "Has no role"], 1,
         "This is from the ISPD 2021 recommendations. Whether to use it is the prescriber&rsquo;s decision."),
        ("When reporting a trend, which statement is most useful?",
         ["&ldquo;Weight is up.&rdquo;", "&ldquo;He is doing okay.&rdquo;", "&ldquo;Weight rose from 68.0 to 70.0 kg over five days while daily UF fell from about 750 to 450 mL and urine from about 600 to 350 mL; all exchanges done; mild breathlessness on exertion.&rdquo;", "&ldquo;See chart.&rdquo;"], 2,
         "Baseline, interval, current values and context."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Icodextrin", "A large glucose polymer solution absorbed slowly, used for long dwells."),
              ("Residual kidney function", "The filtering and urine output the patient's own kidneys still provide."),
              ("Aquaporin", "A water-only channel in capillary walls that lets water cross without sodium."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Peritoneal equilibration test (PET)", "A standardized 4-hour dwell that measures how fast solutes cross the membrane and how much water is removed."),
              ("PSTR", "Peritoneal solute transfer rate: how quickly small solutes cross the membrane."),
              ("D/P creatinine", "Dialysate-to-plasma creatinine ratio; higher values mean faster solute transfer."),
              ("Kt/V", "A laboratory measure of urea clearance used as a surrogate for dialysis dose."),
              ("Surrogate", "A test or laboratory value used in place of an outcome patients feel."),
              ("Protein-energy wasting", "Loss of body protein and energy stores common in kidney failure."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell.")],
    "readings": [("dialysis-adequacy.html", "Dialysis adequacy measures and their limits."),
                 ("eating-on-dialysis.html", "Nutrition on dialysis.")],
    "calcs": ["calc-pd-adequacy.html", "calc-pd-glucose-absorption.html", "calc-nutrition-screening.html"],
}
