# -*- coding: utf-8 -*-
MODULE = {
    "sub": "What the urea numbers really measure and how a bad sample fools them, why a good Kt/V can hide a patient who keeps ending early, how fast fluid removal stuns the heart, what the trials say about dose and time, and how to run a monthly review that treats volume and tolerance as clinical questions.",
    "desc": "Special Dialysis Nurse Roles Module 13: the dialysis adequacy, volume and outcomes nurse. Urea kinetics, valid sampling, URR and Kt/V, prescribed versus delivered treatment, ultrafiltration rate and myocardial stunning, HEMO, DOPPS, Owen and Flythe evidence, KDOQI 2015 targets, and an integrated monthly review.",
    "keywords": "dialysis adequacy nurse, urea reduction ratio Kt/V sampling, post dialysis BUN sample method, delivered versus prescribed dialysis time, ultrafiltration rate mortality, HEMO study dialysis dose, KDOQI 2015 hemodialysis adequacy",
    "image_alt": "A Filipino dialysis nurse drawing a post-dialysis blood sample from the arterial line at the slow-flow setting, with a timer visible on the machine.",
    "objectives": [
        "Validate adequacy sampling and distinguish the prescribed treatment from the treatment delivered.",
        "Calculate the urea reduction ratio from valid data and interpret it alongside Kt/V, time and the patient's condition.",
        "Coordinate review of recurrent fluid and treatment-tolerance problems without changing the prescription.",
        "Integrate nutrition, symptoms and patient goals into a monthly outcome review.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "What was ordered, and what the patient received",
         "html": """
<p>Think of a prescription for a four-hour drive at a set speed. The planned distance is the prescription. The distance actually covered depends on traffic, stops, a flat tire, and whether the driver turned back early. Dialysis adequacy is about the distance actually covered: how much cleaning and fluid removal the patient really received, compared with what was planned.</p>
<p>The picture has a limit. A car's odometer is direct. Dialysis adequacy is measured indirectly, through urea in two blood samples, and a wrongly timed sample can make a short or recirculating treatment look excellent. And adequacy is not only urea: a patient can have a good number and still feel terrible, be breathless before every session, cramp every time, and end early. The adequacy nurse checks that the numbers are valid, compares the plan with what happened, and brings tolerance and symptoms to the same table as Kt/V.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>First ask whether the number is valid. Then ask whether the patient actually received the prescription. Then ask how the patient is doing. The physician decides any change.</div>
"""},
        {"id": "kinetics", "nav": "Urea and sampling", "tag": "Physiology", "h2": "Start with whether the data are valid",
         "html": """
<p><strong>Why urea.</strong> Urea is a small, easily measured waste product made from protein breakdown. It is not especially toxic itself; it stands in for the many small solutes dialysis removes. The urea reduction ratio (URR) is the percentage fall in blood urea during one session: URR = (pre − post) ÷ pre × 100. Kt/V adds the dialyzer's clearance (K), time (t) and the patient's urea distribution volume (V); single-pool Kt/V is commonly calculated with the second-generation Daugirdas formula, which also accounts for urea removed with ultrafiltration and urea generated during the session.[[daugirdas1993]]</p>
<div class="tc-formula">Worked example: pre-dialysis urea 150 mg/dL, post-dialysis 50 mg/dL. URR = (150 − 50) ÷ 150 × 100 = 66.7 percent. A URR of about 65 percent corresponds roughly to a single-pool Kt/V of 1.2; the Kt/V calculator gives the exact value from time, fluid removed and weight.</div>
<p><strong>Why the post sample is so sensitive.</strong> At the end of treatment, blood in the arterial line may be mixed with cleaned blood returning from the venous needle (access recirculation), and blood throughout the body is still re-equilibrating. A post sample drawn at full blood flow, or several minutes late, gives a falsely low or falsely high urea. Units use a standard method, either slowing the blood pump or stopping it for a defined interval, then drawing from the arterial line at a fixed time.[[bcr_urea]] Whichever method your unit uses, the same method must be used every time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Sampling error</th><th>Effect on the result</th></tr></thead>
<tbody>
<tr><td>Pre sample drawn after saline or heparin entered the line</td><td>Pre urea diluted: URR falsely low</td></tr>
<tr><td>Post sample drawn at full flow with recirculation</td><td>Post urea falsely low: URR falsely high</td></tr>
<tr><td>Post sample drawn late after rebound</td><td>Post urea higher: URR falsely low</td></tr>
<tr><td>Tubes mislabeled pre and post, or wrong patient</td><td>Meaningless result</td></tr>
</tbody></table></div>
<div class="tc-keyp"><span class="tc-lab">Remember</span>A result from a sample pair you cannot vouch for should be repeated by the unit method before anyone acts on it.</div>
"""},
        {"id": "evidence", "nav": "What the trials show", "tag": "Evidence", "h2": "Adequacy is a floor, not a dial",
         "html": """
<p><strong>Too little is associated with harm.</strong> In 13,473 United States hemodialysis patients, a URR below 60 percent was associated with a higher risk of death than 65 to 69 percent (odds ratios 1.28 for 55 to 59 percent, 1.39 below 55 percent). In the same analysis, low serum albumin was a far stronger predictor of death than URR.[[owen1993]] This was observational: patients with low URR differed in other ways.</p>
<p><strong>More than enough did not help.</strong> The HEMO trial randomly assigned 1,846 patients on thrice-weekly dialysis to a standard dose (single-pool Kt/V about 1.32) or a high dose (about 1.71). Mortality was not significantly different (relative risk 0.96, 95 percent confidence interval 0.84 to 1.10).[[hemo2002]] So once the dose reaches the floor, pushing urea clearance higher does not reliably buy survival.</p>
<p><strong>The guideline.</strong> The KDOQI 2015 adequacy update sets a target single-pool Kt/V of 1.4 per thrice-weekly session, with a minimum delivered dose of 1.2.[[hd2015]] Kt/V and URR are surrogate measures: they describe small-solute removal, not how the patient feels or lives.</p>
<p><strong>Time and fluid removal matter beyond urea.</strong> In the international DOPPS cohort of 22,000 patients, treatment time longer than 240 minutes was associated with lower mortality (relative risk 0.81), and an ultrafiltration rate above 10 mL/kg/h with more intradialytic hypotension and higher mortality.[[saran2006]] In an analysis of HEMO participants, ultrafiltration rates above 13 mL/kg/h were associated with higher all-cause mortality (adjusted hazard ratio 1.59) and cardiovascular mortality (1.71).[[flythe2011]] These are associations, but they fit the physiology: removing fluid faster than it can refill the blood vessels from the tissues causes low blood pressure, and repeated drops in heart blood flow can stun heart muscle.</p>
<div class="tc-plain"><span class="tc-lab">How certain are we?</span>Strong (randomized): raising dose above the standard did not lower mortality. Associations (observational): low URR, short time and high ultrafiltration rate with worse survival. Guideline: KDOQI target spKt/V 1.4, minimum 1.2. All urea measures are surrogates.</div>
"""},
        {"id": "delivered", "nav": "Prescribed versus delivered", "tag": "Practice", "h2": "Compare the prescription with what was delivered",
         "html": """
<p>When adequacy falls, the cause is usually in delivery, not in the prescription. Check the common contributors before anyone changes the order.</p>
<div class="tc-cards">
<div class="tc-card"><b>Time</b>Minutes actually delivered, from blood flow on to blood returned; early terminations and their reasons.</div>
<div class="tc-card"><b>Blood flow</b>Achieved, not prescribed; access problems, arterial pressure alarms.</div>
<div class="tc-card"><b>Access</b>Recirculation from stenosis or needle placement (Module 2); catheter dysfunction.</div>
<div class="tc-card"><b>Dialyzer and dialysate</b>Correct dialyzer; clotting in the circuit; dialysate flow as ordered.</div>
<div class="tc-card"><b>Sampling</b>Was the sample pair valid?</div>
<div class="tc-card"><b>Missed sessions</b>Sessions skipped or shortened across the month.</div>
</div>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 3</span>Mr. Ben Soriano's prescription is 240 minutes. Delivered: 210 minutes (30 short), 3.2 liters removed, post-dialysis weight 58 kg. Ultrafiltration rate = 3,200 mL ÷ 58 kg ÷ 3.5 h = 15.8 mL/kg/h, above the rate associated with harm in observational data. His URR from a valid sample pair is 69 percent. The number looks adequate, but the session was short and the fluid came off fast. This goes to the physician as a tolerance and volume question, not as "adequacy met."</div>
<div class="tc-stop"><span class="tc-lab">Never</span>Raise the ultrafiltration rate to finish on time, shorten a session to fit the schedule, or change the target weight or time on your own. Report and let the physician decide.</div>
"""},
        {"id": "volume", "nav": "Volume and tolerance", "tag": "Physiology", "h2": "Treat volume and tolerance as clinical questions",
         "html": """
<p>During ultrafiltration, fluid is removed from the blood. The blood volume is kept up by fluid moving in from the tissues (plasma refill). If removal outpaces refill, blood volume falls, blood pressure drops, and the patient cramps, feels faint or vomits. The usual drivers are a large weight gain between sessions (so more must come off), a short session (so it must come off faster), a target weight set too low, heart disease, and blood pressure medicines taken before dialysis.</p>
<p>Recurrent cramps, hypotension and early terminations are signals for a team review, not for pushing harder. Things the physician may consider include reviewing the target weight, the timing of blood pressure medicines, longer or extra sessions, dialysate settings and salt intake. Your part is to bring the data: weights, gains, ultrafiltration rates, blood pressures, symptoms, early endings and their reasons, and the patient's own account.</p>
<div class="tc-scene"><span class="tc-lab">Good number, bad sessions &middot; fictional</span><p>Aling Myrna's spKt/V is 1.45. But in the past month she ended early six times because of cramps, and twice she arrived breathless with ankle swelling. Staff suggest raising the ultrafiltration rate so she "finishes the fluid in time."</p><p>Nurse Rico pulls her month together: average weight gain 3.6 kilograms, ultrafiltration rates of 14 to 17 mL/kg/h, six early endings, and an amlodipine dose she takes in the morning before dialysis. He presents it to Dr. Reyes and the dietitian. The physician reviews her target weight and medicine timing, adds a longer session once a week, and the dietitian works with her on salt.</p><p class="tc-scene-take"><b>What this shows.</b> The Kt/V was fine. The problem was volume and tolerance, and it was solved by a team review, not by faster fluid removal.</p></div>
"""},
        {"id": "review", "nav": "Monthly review", "tag": "Coordination", "h2": "Build an integrated monthly review",
         "html": """
<p>Bring the measures together once a month for each patient, so that urea numbers sit beside the things patients feel.</p>
<ol class="tc-flow">
<li><b>Validity</b>Was the sample pair valid? Repeat if not.</li>
<li><b>Delivery</b>Minutes delivered versus prescribed; blood flow; missed sessions.</li>
<li><b>Adequacy</b>URR and Kt/V by the unit's method.</li>
<li><b>Volume</b>Weight gains, ultrafiltration rates, blood pressure, edema, breathlessness.</li>
<li><b>Tolerance</b>Cramps, hypotension, early endings, post-dialysis fatigue.</li>
<li><b>Nutrition and bone</b>Albumin trend, appetite, referral to the dietitian; CKD–mineral and bone disorder results flagged for the physician.</li>
<li><b>Goals</b>What the patient wants from treatment; residual urine output.</li>
<li><b>Actions</b>Owner and date for each, reviewed next month.</li>
</ol>
<p>Albumin is a marker, not a diagnosis: a low albumin can reflect inflammation, fluid overload or protein loss as well as poor intake, so it prompts a dietitian and physician review rather than a nutrition diagnosis by the nurse.</p>
"""},
    ],
    "case": {
        "title": "The adequate patient who keeps leaving early",
        "html": """
<p><strong>Monthly review.</strong> Mr. Ben Soriano, 52, has a spKt/V of 1.42 this month. In the same month he ended treatment early seven times (average 25 minutes short) because of cramps, and arrived breathless before two Monday sessions. His average weight gain is 3.8 kilograms on a target of 58 kilograms.</p>
<p>Today's post-dialysis sample was drawn by a new nurse at full blood flow, not by the unit's slow-flow method. A colleague proposes raising his ultrafiltration rate "so he finishes the fluid before he cramps." Mr. Soriano says he hates the cramps and is thinking of skipping Saturdays.</p>
""",
        "acte": {
            "Assess": "The adequacy number may be falsely high (invalid post sample). Delivery is short, ultrafiltration rates are high, Monday breathlessness suggests volume overload after the long gap, and the patient is considering missing sessions.",
            "Communicate": "Ask for the sample pair to be repeated by the unit method. Present the month's data to the physician: delivered minutes, ultrafiltration rates, weight gains, cramps, breathlessness, his thoughts of skipping. Do not raise the ultrafiltration rate.",
            "Teach": "Teach the new nurse the post-sample method. With Mr. Soriano, explore what makes the cramps worse and teach salt and fluid basics with teach-back (Module 5); explain why skipping Saturdays would make Mondays worse.",
            "Escalate": "Ask for a physician and dietitian review of target weight, session time, medicine timing and salt. Record owners and a review date.",
        },
        "outcome": """
<p>The repeated sample gave a spKt/V of 1.31, still above the minimum but lower than reported. The physician extended his Monday session, reviewed his target weight and blood pressure medicines, and the dietitian worked on salt. Over six weeks his early endings fell to one a month and he kept his Saturday sessions.</p>
""",
        "task": "Write the monthly review note for Mr. Soriano using the eight steps in this module, with an owner and date for each action.",
    },
    "second_round": ("Mr. Soriano's URR is now 72 percent, but his residual urine output has fallen to almost nothing and his pre-dialysis potassium is rising.",
                     "A short summary for the physician that explains why a good URR does not answer these new findings, and what data you would bring."),
    "evidence_out": "Five valid sample pairs drawn by the unit method under observation, and three integrated monthly reviews presented to the physician.",
    "critical": "Raising the ultrafiltration rate or changing time or target weight without an order, or reporting adequacy from an invalid sample pair.",
    "reflect": "Which patient in your unit has a good Kt/V but a hard time on dialysis? Who has looked at both at the same time?",
    "practice": {
        "intro": "Sampling is learned on patients under direct supervision; calculations can be practiced with fictional data.",
        "items": [
            "Draw five pre and post sample pairs by your unit's method under observation.",
            "Calculate URR and ultrafiltration rate for ten fictional sessions and check with the calculators.",
            "Compare prescribed and delivered minutes for all patients for one week and list reasons for shortfalls.",
            "Prepare and present three integrated monthly reviews to the physician.",
            "Review one patient's month with the dietitian, linking weight gain, salt and symptoms.",
        ],
    },
    "job_aid": ("Integrated monthly review", [
        "Patient code, month, prescription (time, blood flow, dialyzer, target weight)",
        "Sample pair valid (method, time, labels): yes/no",
        "URR and Kt/V by unit method",
        "Delivered versus prescribed minutes; early endings and reasons",
        "Missed or shortened sessions",
        "Weight gains; ultrafiltration rates; blood pressure; edema or breathlessness",
        "Cramps, hypotension, post-dialysis fatigue",
        "Albumin trend; dietitian referral",
        "Patient goals; residual urine",
        "Actions: owner, date",
    ]),
    "metric": "Eligible sessions delivering the prescribed duration, divided by eligible sessions reviewed, with documented clinical exceptions; balanced by hypotension, cramps, symptom burden and patient goals.",
    "readings": [
        ("dialysis-adequacy.html", "Dialysis adequacy explained."),
        ("dry-weight-determination.html", "How target weight is determined."),
        ("dialysis-cramps-stasis-pigmentation.html", "Cramps during dialysis."),
    ],
    "academy": [("Hemodialysis Nurse Module 6: Principles, prescription and adequacy", "nephrology-nursing-06-hd-principles-prescription-adequacy.html")],
    "calcs": ["calc-dialysis-nurse-portfolio-toolkit.html", "calc-dialysis-adequacy-ktv.html", "calc-ultrafiltration-rate.html", "calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
    "terms": [
        ("Urea reduction ratio", "The percentage fall in blood urea during one session."),
        ("Kt/V", "Dialyzer urea clearance times treatment time, divided by the patient's urea distribution volume."),
        ("Recirculation", "Cleaned blood returning from the venous needle being drawn back into the arterial needle, distorting the post sample."),
        ("Ultrafiltration rate", "Fluid removed per kilogram of body weight per hour."),
        ("Plasma refill", "The movement of fluid from tissues into the bloodstream during fluid removal."),
        ("Myocardial stunning", "Temporary weakening of heart muscle after reduced blood flow, as can happen with rapid fluid removal."),
    ],
    "quiz": [
        {"stem": "Pre-dialysis urea is 150 mg/dL and post-dialysis urea is 50 mg/dL. What is the URR?",
         "options": [["About 67 percent.", True, "(150 − 50) ÷ 150 × 100."],
                     ["33 percent.", False, "That is post divided by pre."],
                     ["100 percent.", False, "Not possible here."],
                     ["50 percent.", False, "Miscalculated."]], "sources": []},
        {"stem": "A post-dialysis sample is drawn at full blood flow from a recirculating access. What happens to the URR?",
         "options": [["It is falsely high, because post urea is falsely low.", True, "Cleaned blood contaminates the sample."],
                     ["It is falsely low.", False, "Opposite."],
                     ["It is unaffected.", False, "It is affected."],
                     ["It becomes zero.", False, "Not the effect."]], "sources": ["bcr_urea"]},
        {"stem": "What did the HEMO trial show?",
         "options": [["A higher dose (spKt/V about 1.71 vs 1.32) did not significantly lower mortality.", True, "RR 0.96."],
                     ["A higher dose halved mortality.", False, "Not found."],
                     ["Low-flux membranes increased mortality.", False, "Not significantly different."],
                     ["It was observational.", False, "It was randomized."]], "sources": ["hemo2002"]},
        {"stem": "What spKt/V does KDOQI 2015 target for thrice-weekly hemodialysis?",
         "options": [["1.4, with a minimum delivered dose of 1.2.", True, "Guideline target and floor."],
                     ["2.0 for everyone.", False, "Not the guideline."],
                     ["0.8.", False, "Too low."],
                     ["No target exists.", False, "There is one."]], "sources": ["hd2015"]},
        {"stem": "In the HEMO analysis, what ultrafiltration rate was associated with higher all-cause mortality?",
         "options": [["Above 13 mL/kg/h (adjusted hazard ratio 1.59).", True, "Observational association."],
                     ["Below 5 mL/kg/h.", False, "Not the finding."],
                     ["Any rate.", False, "Not the finding."],
                     ["Above 30 mL/kg/h only.", False, "Not the threshold."]], "sources": ["flythe2011"]},
        {"stem": "A patient has a good Kt/V but ends early most sessions because of cramps. Staff suggest raising the ultrafiltration rate. What do you do?",
         "options": [["Do not raise it; bring delivered time, rates, weights and symptoms to the physician.", True, "A tolerance and volume problem needs a clinical review."],
                     ["Raise it so he finishes on time.", False, "Faster removal worsens cramps and hypotension."],
                     ["Shorten all his sessions.", False, "Not a nursing decision."],
                     ["Ignore it; Kt/V is adequate.", False, "Surrogate is not the whole picture."]], "sources": ["flythe2011", "saran2006"], "critical": True},
        {"stem": "Fluid removed 3.2 L, post weight 58 kg, delivered time 3.5 h. What is the ultrafiltration rate?",
         "options": [["About 15.8 mL/kg/h.", True, "3,200 ÷ 58 ÷ 3.5."],
                     ["About 5.5 mL/kg/h.", False, "Miscalculated."],
                     ["About 55 mL/kg/h.", False, "Miscalculated."],
                     ["About 0.9 mL/kg/h.", False, "Miscalculated."]], "sources": []},
        {"stem": "What did DOPPS find about treatment time?",
         "options": [["Time longer than 240 minutes was associated with lower mortality (RR 0.81).", True, "Observational association."],
                     ["Shorter sessions were safer.", False, "Opposite."],
                     ["Time had no association.", False, "Association found."],
                     ["It was a randomized trial.", False, "It was a cohort study."]], "sources": ["saran2006"]},
        {"stem": "Why are URR and Kt/V called surrogate measures?",
         "options": [["They describe small-solute removal, not how the patient feels or survives.", True, "Label surrogates as surrogates."],
                     ["They are estimated by machines.", False, "Not the reason."],
                     ["They are inaccurate.", False, "They can be accurate."],
                     ["They replace clinical review.", False, "They do not."]], "sources": ["hd2015"]},
        {"stem": "In the 13,473-patient cohort, which was a stronger predictor of death than URR?",
         "options": [["Low serum albumin.", True, "About 21 times more powerful."],
                     ["Treatment time.", False, "Not the comparison reported."],
                     ["Age alone.", False, "Not the comparison reported."],
                     ["Blood flow rate.", False, "Not reported."]], "sources": ["owen1993"]},
        {"stem": "The pre sample was drawn after saline entered the line. What is the effect?",
         "options": [["Pre urea is diluted, so URR is falsely low.", True, "Dilution lowers the pre value."],
                     ["URR is falsely high.", False, "Opposite."],
                     ["No effect.", False, "There is an effect."],
                     ["Post urea rises.", False, "The pre sample is affected."]], "sources": ["bcr_urea"]},
        {"stem": "When adequacy falls, what is usually checked first?",
         "options": [["Delivery: time, blood flow, access recirculation, clotting and sampling.", True, "Most falls come from delivery, not the prescription."],
                     ["A new dialyzer brand.", False, "Not first."],
                     ["The patient's diet.", False, "Not the first cause of low clearance."],
                     ["The weather.", False, "Irrelevant."]], "sources": []},
        {"stem": "A patient's albumin is low. What is the nurse's role?",
         "options": [["Flag it for dietitian and physician review; albumin also reflects inflammation and fluid.", True, "A marker, not a nutrition diagnosis."],
                     ["Diagnose malnutrition and start supplements.", False, "Outside nursing scope."],
                     ["Ignore it.", False, "It is a strong prognostic marker."],
                     ["Reduce dialysis time.", False, "Not a nursing decision."]], "sources": ["owen1993"]},
        {"stem": "What causes cramps and hypotension during fluid removal?",
         "options": [["Removal outpacing plasma refill from the tissues.", True, "Blood volume falls faster than it is replaced."],
                     ["Too much dialysate potassium.", False, "Not the general mechanism."],
                     ["Heparin.", False, "Not the mechanism."],
                     ["Cold dialysate.", False, "Cooler dialysate tends to support blood pressure."]], "sources": ["flythe2011"]},
        {"stem": "A new nurse drew the post sample by a different method. What should happen to the result?",
         "options": [["Repeat the pair by the unit method before anyone acts on it.", True, "Methods must be consistent."],
                     ["Report it as usual.", False, "Validity is uncertain."],
                     ["Adjust the result by 10 percent.", False, "Not valid."],
                     ["Discard and never repeat.", False, "Repeat by the method."]], "sources": ["bcr_urea"], "critical": True},
    ],
    "exam": [
        {"stem": "Which action is outside the adequacy nurse's scope?",
         "options": [["Raising the ultrafiltration rate to finish fluid removal on time.", True, "A prescription decision."],
                     ["Repeating an invalid sample pair by the unit method.", False, "Within scope."],
                     ["Reporting delivered versus prescribed minutes.", False, "Within scope."],
                     ["Presenting a monthly review.", False, "Within scope."]], "sources": ["flythe2011"], "critical": True},
        {"stem": "What did the HEMO trial teach about dialysis dose?",
         "options": [["Above the standard dose, higher urea clearance did not lower mortality.", True, "Adequacy is a floor, not a dial."],
                     ["Higher dose always helps.", False, "Not found."],
                     ["Dose does not matter at all.", False, "Too little is associated with harm."],
                     ["Only membranes matter.", False, "Not found."]], "sources": ["hemo2002"]},
    ],
}

# ── v2 completion (24 Nov 2026): second and third worked scenarios ──
def _sec(sid):
    return next(s for s in MODULE["sections"] if s["id"] == sid)

_sec("kinetics")["html"] += """
<div class="tc-scene"><span class="tc-lab">A URR too good to be true &middot; fictional</span><p>Mrs. Erlinda Pascual's urea reduction ratio is usually 66 to 68 percent. This month it reads 81 percent: pre-dialysis urea 140 mg/dL, post-dialysis 27 mg/dL. Nothing in her prescription changed.</p><p>Nurse Mae, the adequacy nurse, checks how the post sample was drawn. A float nurse took it from the venous line after rinse-back had started, so saline had diluted the sample. A falsely low post value makes the URR look higher than the treatment delivered. Mae marks the result as an invalid sample, tells the physician, and asks that the next sample be drawn by the unit's slow-flow method (blood pump slowed per protocol, sample from the arterial line before rinse-back). The repeat URR is 67 percent.</p><p>She also adds the sampling steps to the float nurse orientation sheet.</p><p class="tc-scene-take"><b>What this shows.</b> A sudden improvement with no change in treatment usually points to the sample, not the patient. Check how the number was made before celebrating it.</p></div>
"""

_sec("delivered")["html"] += """
<div class="tc-scene"><span class="tc-lab">The missing 26 minutes &middot; fictional</span><p>Mr. Rodel Santos is prescribed 4 hours (240 minutes) three times a week. Over 12 sessions this month, the machine logs show an average of 214 minutes: four late starts after transport delays (average 20 minutes lost), three early terminations for cramps (average 30 minutes), and one stop for a machine alarm (35 minutes).</p><div class="tc-formula">Delivered ÷ prescribed = 214 ÷ 240 = 89 percent. Over the month that is 12 × 26 = 312 minutes, more than one full session, never delivered.</div><p>Nurse Mae brings the sum and its causes to the monthly review rather than only the Kt/V. The physician reviews his prescription and target weight; the social worker looks into transport; Mae flags the cramps pattern for review alongside his fluid gains. She does not add minutes, raise the blood flow or change the ultrafiltration herself.</p><p class="tc-scene-take"><b>What this shows.</b> Lost minutes are invisible session by session and obvious when added up. Each cause has a different owner.</p></div>
"""
