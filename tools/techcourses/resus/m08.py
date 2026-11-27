# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 08: Hyperkalemia: With a Pulse and in Arrest. Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A physician comparing an ECG with peaked T waves to a laboratory slip while a nurse keeps the patient dialyzing.",
    "objectives": [
        "Explain how high extracellular potassium brings the heart&rsquo;s resting membrane potential toward threshold, and how calcium protects it.",
        "Treat hyperkalemia with a pulse in three steps (protect, shift, remove), keeping a stable connected patient on dialysis.",
        "State the 2025 AHA position on calcium, bicarbonate, insulin-glucose and inhaled beta-agonists in hyperkalemic cardiac arrest, with grades.",
        "Compare the ERC 2025 hyperkalemic-arrest treatment with the AHA position, and explain why the unit protocol must choose.",
        "Plan glucose monitoring after insulin and the decision about dialysis after the pulse returns.",
    ],
    "big": """
{{plain:Think of each heart muscle cell as a spring-loaded trap. Normally the spring is pulled back a long way, so it takes a strong, deliberate signal to spring it, and it resets cleanly after each beat. High potassium outside the cell lets the spring partly relax. At first the trap fires too easily; then, as it relaxes further, it can no longer reset at all, and the heart slows, widens and stops.}}
<p>The picture has a limit. The &ldquo;spring&rdquo; is the resting membrane potential, set mainly by the ratio of potassium inside to potassium outside the cell. As outside potassium rises, the cell sits closer to its firing threshold. Sodium channels, which drive the fast upstroke of each beat, are partly inactivated when the cell sits closer to zero, so conduction slows: that is the widening QRS. Calcium does not change potassium at all. It raises the threshold, restoring the gap between where the cell sits and where it fires. That is why calcium protects the heart for a time but treats nothing.</p>
<p>In a dialysis unit, hyperkalemia is the reversible cause most likely to be on the list, and the one with the most disagreement between guidelines once the heart has stopped. This module separates the two situations clearly, because the treatments and the evidence are different.</p>
{{cards:Key terms for this module|Hyperkalemia::A serum potassium above the normal range; your unit sets its action thresholds.|Resting membrane potential::The voltage across a resting cell membrane, set mainly by the potassium gradient.|Membrane stabilization::Raising the firing threshold with intravenous calcium; it does not lower potassium.|Shifting::Moving potassium into cells with insulin (given with glucose) or a beta-agonist such as salbutamol.|Removal::Taking potassium out of the body; in kidney failure, mainly by dialysis.|Hyperkalemic cardiac arrest::Cardiac arrest in which high potassium is the suspected cause.}}
""",
    "case": {"title": "The missed session", "html": """
<p>Mr. Eduardo Panganiban, 55, missed his Saturday session to attend a family wake in Batangas. He arrives at 6:10 a.m. on Monday, weak, with heavy legs. His pre-dialysis potassium is sent; the laboratory says 45 minutes. His ECG shows tall, narrow T waves and a QRS that looks slightly wide. Heart rate 58, blood pressure 130/80. He is connected and dialysis starts at 6:30.</p>
<p>At 6:50, before the result is back, his rhythm slows to 40 and becomes wide. At 6:55 he is unresponsive and pulseless; the monitor shows a slow, wide, organized rhythm.</p>
""", "questions": ["What should have happened between 6:10 and 6:30?",
                  "At 6:55, which algorithm is he in, and what is treated first?",
                  "What do the AHA and the ERC say about potassium drugs now, and who decides for your unit?"]},
    "sections": [
        ("pulse", "With a pulse", "Hyperkalemia with a pulse: protect, shift, remove", """
<p>A patient with high potassium and a pulse is in a race, but one you can usually win. The plan has three steps, each with a different purpose, and each step buys time for the next. The doses below are those of the European Resuscitation Council (ERC) 2025 guideline, quoted so you can recognize them;[[erc2025_special]] the UK Kidney Association guideline gives similar regimens;[[an06_1]] your unit order set decides.</p>
{{fig:rl08_protect_shift_remove}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What</th><th>ERC 2025 regimen (patients with circulation)</th><th>What it does and does not do</th></tr></thead>
<tbody>
<tr><td>Protect</td><td>Intravenous calcium when the ECG shows potassium changes</td><td>10 mL of 10% calcium chloride IV for severe hyperkalemia with ECG changes</td><td>Restores the threshold gap within minutes; lasts a short time; does not lower potassium</td></tr>
<tr><td>Shift</td><td>Insulin with glucose; nebulized salbutamol as an adjunct</td><td>10 units soluble insulin with 25 g glucose IV; if pre-treatment glucose is below 7 mmol/L, follow with 10% glucose at 50 mL an hour for 5 hours. Salbutamol 10 to 20 mg nebulized as an adjunct</td><td>Moves potassium into cells; total body potassium unchanged; effect wears off</td></tr>
<tr><td>Remove</td><td>Dialysis</td><td>Dialysis for severe hyperkalemia resisting medical treatment</td><td>The only real removal in a patient on dialysis</td></tr>
</tbody></table></div>
<p>Insulin-based treatment causes hypoglycemia often in patients with kidney failure, because insulin is cleared by the kidneys and its effect lasts longer.[[apel2014]] Check capillary glucose regularly for several hours after insulin, as your order set specifies, and give the follow-on glucose it calls for.</p>
<p>For a connected, stable patient, the most important rule is negative: do not stop dialysis. Card 10, signed off for this Academy, puts it plainly: dialysis is the treatment; calcium and insulin only buy time.</p>
{{key:Protect with calcium, shift with insulin and glucose (plus salbutamol), remove with dialysis. Check glucose for hours after insulin, and keep a stable patient dialyzing.}}
"""),
        ("ecg", "The ECG and timing", "The ECG, the laboratory, and the minutes in between", """
<p>Treatment of hyperkalemia with ECG changes does not wait for the laboratory. Treatment of a high laboratory value does not wait for ECG changes. Both errors happen because each test is treated as the confirmation of the other.</p>
{{fig:rl08_blindspot}}
<div class="table-wrap"><table>
<thead><tr><th>You have</th><th>What it means</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Typical ECG changes, no result yet</td><td>Potassium is likely high and affecting the heart now</td><td>Protect and shift per order set; call the physician; dialyze</td></tr>
<tr><td>High result, normal ECG</td><td>ECG changes are often absent at high values</td><td>Treat the value per order set; dialyze</td></tr>
<tr><td>High result, sample hemolyzed</td><td>Possibly falsely high</td><td>Repeat the sample, but treat at once if the ECG is abnormal</td></tr>
<tr><td>Slow wide rhythm, story of a missed session</td><td>Potassium until proven otherwise</td><td>Treat now; pads on; pacing and arrest may follow</td></tr>
</tbody></table></div>
<p>In a retrospective review of hospital patients with high potassium, the typical ECG changes were often missing, even at high values.[[montague2008]] The progression from peaked T waves to a sine wave is a teaching pattern, not a warning system; the jump from &ldquo;slightly wide&rdquo; to arrest can take minutes, as it did in the case.</p>
{{key:ECG changes do not wait for the laboratory, and a high value does not wait for ECG changes. A story of missed dialysis plus a slow wide rhythm is treated now.}}
"""),
        ("arrest", "In arrest", "Hyperkalemic cardiac arrest: where the guidelines differ", """
<p>Once the patient is pulseless, cardiac arrest comes first: compressions, the rhythm check, epinephrine on the right path. Potassium becomes the reversible cause to treat during CPR. Here the major guidelines diverge, and the course shows both positions side by side rather than blending them.</p>
{{fig:rl08_aha_erc}}
<div class="table-wrap"><table>
<thead><tr><th>Treatment during hyperkalemic arrest</th><th>AHA 2025 (adults and children)[[aha2025_special]]</th><th>ERC 2025[[erc2025_special]]</th></tr></thead>
<tbody>
<tr><td>Intravenous calcium</td><td>Effectiveness not well established (COR 2b, LOE C-LD)</td><td>10 mL of 10% calcium chloride IV as a rapid bolus; consider repeating if arrest is refractory or prolonged</td></tr>
<tr><td>Sodium bicarbonate</td><td>Effectiveness not well established (COR 2b, LOE C-EO)</td><td>50 mmol IV, in the arrest setting only, given through a separate line or with a flush between it and calcium</td></tr>
<tr><td>Insulin and glucose</td><td>Effectiveness not well established (COR 2b, LOE C-EO)</td><td>No arrest-specific dose given; general regimen applies</td></tr>
<tr><td>Inhaled beta-agonists</td><td>Not recommended (COR 3: No Benefit, LOE C-EO)</td><td>No arrest-specific dose given</td></tr>
<tr><td>Dialysis</td><td>Not addressed in the arrest recommendations</td><td>Definitive; rarely used in arrest; feasible during CPR in case reports; consider for refractory severe hyperkalemia per local protocol</td></tr>
</tbody></table></div>
<p>Why the difference? The underlying evidence is thin. An International Liaison Committee on Resuscitation (ILCOR) systematic review found insufficient evidence to recommend for or against calcium or bicarbonate in hyperkalemic arrest; almost no studies included patients in arrest.[[jessen2025]] The AHA reads that gap as &ldquo;effectiveness not well established,&rdquo; and cautions that drug therapy must not interrupt CPR. The ERC reads the same physiology and case experience as reason enough to give calcium and bicarbonate. Neither position is proven by a trial in arrested patients.</p>
<p>Two practical rules hold under both: calcium and bicarbonate are never given through the same line without a flush, because they precipitate; and none of these drugs is worth a pause in compressions. Card 1 already states the position this Academy uses: guidelines differ, and your unit protocol decides.</p>
{{key:In hyperkalemic arrest, CPR comes first. The AHA calls calcium, bicarbonate and insulin of uncertain effectiveness and advises against inhaled beta-agonists; the ERC gives calcium chloride with bicarbonate. Your unit protocol chooses, written down in advance.}}
"""),
        ("after", "After the pulse returns", "After return of spontaneous circulation (ROSC): potassium rebounds, and dialysis is the plan", """
<p>A pulse after hyperkalemic arrest is not the end of the potassium problem. Calcium wears off; insulin and salbutamol move potassium into cells only for hours; the potassium is still in the body. The ERC notes that dialysis may be needed early in the post-resuscitation period.[[erc2025_special]] In a freestanding unit, that usually means transfer to a hospital that can dialyze an unstable patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>After return of spontaneous circulation (ROSC)</th><th>Why</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td>Repeat potassium and glucose</td><td>Potassium rebounds; insulin causes late hypoglycemia</td><td>Physician-on-duty</td></tr>
<tr><td>Continuous ECG</td><td>Recurrent arrhythmia</td><td>Physician-on-duty</td></tr>
<tr><td>Restarting dialysis in your unit</td><td>Only if the patient is stable enough and the attending agrees</td><td>Attending nephrologist</td></tr>
<tr><td>Transfer for dialysis in hospital</td><td>Unstable patients need monitored dialysis</td><td>Attending nephrologist and receiving team</td></tr>
<tr><td>Review the prescription and the reason for the missed session</td><td>Prevent the next one</td><td>Attending nephrologist, social worker, head nurse</td></tr>
</tbody></table></div>
<p>Do not restart dialysis after ROSC without the attending nephrologist, even when the potassium is the obvious cause (Card 1). The decision weighs the benefit of removal against the risk of starting a circuit in a patient whose pressure may not tolerate it.</p>
{{key:After ROSC, potassium comes back. Recheck potassium and glucose, keep the monitor on, and let the attending nephrologist decide where and when dialysis restarts.}}
{{call:Potassium above your unit&rsquo;s action threshold, any potassium ECG change, or a slow wide rhythm: start the order set while you call the physician-on-duty and the attending nephrologist. Follow your unit protocol, and always ask the attending nephrologist for guidance before stopping or restarting dialysis.}}
"""),
    ],
    "debrief": ["""
<p><strong>6:10 to 6:30.</strong> Missed session plus weakness plus peaked T waves and a slightly wide QRS is hyperkalemia affecting the heart. The order set should have started before connection: intravenous calcium for the ECG changes, insulin with glucose (and salbutamol if prescribed), the monitor and pads on, and urgent connection to dialysis with the potassium bath the physician orders. The laboratory result was not needed to start.</p>
<p><strong>6:55.</strong> He is in cardiac arrest with a slow, wide, organized rhythm and no pulse: PEA. Compressions start at once; the circuit nurse stops fluid removal and makes the blood decision (no circuit cause, so return or clamp and disconnect, per Module 7); epinephrine is given as soon as feasible on the nonshockable path. Potassium is the leading reversible cause.</p>
<p><strong>The drugs.</strong> The AHA 2025 guideline calls the effectiveness of calcium, bicarbonate and insulin-glucose in hyperkalemic arrest not well established and advises against inhaled beta-agonists; the ERC 2025 guideline gives 10 mL of 10% calcium chloride with 50 mmol of sodium bicarbonate through separate lines, and considers dialysis for refractory arrest. The team follows whichever the unit protocol has adopted, decided before today, and never pauses compressions to give them. After ROSC, the attending nephrologist decides where dialysis continues.</p>
"""],
    "skills": {"title": "Hyperkalemia with a pulse and in arrest",
               "intro": "In two simulator scenarios, manage hyperkalemia with a pulse and hyperkalemic cardiac arrest while a supervisor observes.",
               "items": [
                   ("Starts treatment for ECG changes without waiting for the laboratory result.", True),
                   ("States protect, shift, remove, and what each step does and does not do.", False),
                   ("Keeps a stable connected patient on dialysis and calls the attending nephrologist.", True),
                   ("Orders glucose checks for several hours after insulin.", False),
                   ("In arrest, prioritizes compressions and the arrest algorithm before potassium drugs.", True),
                   ("States the AHA and ERC positions accurately and follows the unit protocol.", False),
                   ("Never gives calcium and bicarbonate in the same line without a flush.", True),
                   ("After ROSC, rechecks potassium and glucose and does not restart dialysis without the attending.", False),
               ],
               "placement": "Read your unit&rsquo;s hyperkalemia order set with the physician-on-duty and note which framework (AHA, ERC, or local) it follows for arrest."},
    "terms": [("Resting membrane potential", "The voltage across a resting cell membrane, set mainly by the potassium gradient."),
              ("Membrane stabilization", "Raising the firing threshold with calcium."),
              ("Potassium shift", "Moving potassium into cells without removing it from the body."),
              ("Calcium chloride", "A calcium salt with more calcium per milliliter than calcium gluconate."),
              ("Precipitation", "Calcium and bicarbonate forming a solid in the same line."),
              ("Rebound hyperkalemia", "Potassium rising again as shifting treatments wear off.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "The site guide to potassium and hyperkalemia in kidney disease.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["08"])
