# -*- coding: utf-8 -*-
# Module 9 expansion, part 3: diabetes on hemodialysis. Sections follow the monthly laboratory panel (m09_x2.py).
OBJECTIVES = [
    "Explain why blood glucose behaves differently on hemodialysis (HD), including slower insulin clearance, glucose in the dialysate, and the limits of glycated hemoglobin (HbA1c), and check and respond to glucose at the chair per protocol.",
    "Check the feet of a patient with diabetes on HD at the chair, refer a wound promptly, and coordinate diet, meal timing, and eye care with the dietitian and physician.",
]
EXTRA = [
    {"after": "monthly-labs", "id": "diabetes-hd", "nav": "Diabetes on HD", "tag": "Clinical application",
     "h2": "Diabetes on hemodialysis: why glucose behaves differently",
     "html": """
<p>Diabetes is the most common cause of kidney failure in many dialysis units, and a large share of the patients on any shift live with it. Earlier sections touched on low blood sugar as a symptom to check at the chair and a risk to teach before the patient goes home. This section explains why glucose behaves differently once a person is on hemodialysis (HD). Then you can anticipate problems instead of only reacting to them.</p>
<p><strong>The plain model.</strong> Think of blood glucose as the level of water in a tank with a tap in and a drain out. Food and the liver fill the tank. Insulin opens the drain into the cells.</p>
<p>The picture has a limit. A tank has one tap and one drain. The body has more hands on the controls. Healthy kidneys do two quiet jobs: they break down a large part of the insulin that circulates, and they make some new glucose of their own when a person is fasting. Kidney failure changes both jobs. The dialysis session then adds a third influence of its own.</p>
<p><strong>The mechanisms</strong></p>
<ul>
<li><strong>Insulin lasts longer.</strong> As kidney function falls, less insulin is cleared, so each injected dose acts for longer, and some tablets and their active products accumulate. A dose that suited the patient in earlier chronic kidney disease (CKD) may now be too strong.</li>
<li><strong>Less glucose is made between meals.</strong> The failing kidney contributes less new glucose during fasting, so a missed or delayed meal has a larger effect than before.</li>
<li><strong>Appetite and intake vary.</strong> Nausea, taste change, and a session that falls across a mealtime reduce what the patient eats on dialysis days.</li>
<li><strong>Insulin resistance pulls the other way.</strong> Uremia makes the tissues less responsive to insulin, and dialysis partly reverses this. The net result is unpredictable. Some patients need less treatment after starting dialysis. In some, the glucose falls so much that the physician stops diabetes medicines altogether. You report the pattern. The physician decides what it means.</li>
<li><strong>The dialysate acts as a glucose buffer.</strong> Glucose moves freely across the dialyzer membrane. Most current concentrates contain glucose at a level close to normal blood glucose. During the session, the blood glucose is pulled toward the dialysate level. A high glucose falls, and a low glucose is partly supported. Where a glucose-free dialysate is used, glucose leaves the blood throughout the session, and low blood sugar during treatment is more likely. When the session ends, the buffer is gone. In some patients glucose may fall in the hours that follow. That is one reason low readings appear on the way home or in the evening.</li>
</ul>
<p><strong>High glucose matters differently too.</strong> In a person who passes little urine, high glucose cannot be lost through the kidneys. It may increase thirst and therefore the weight gained between sessions, and it may draw potassium out of the cells into the blood. A very high reading with drowsiness or confusion is reported at once, not saved for the round.</p>
<p><strong>Why glycated hemoglobin (HbA1c) is less reliable.</strong> HbA1c reflects how much glucose has attached to hemoglobin over the life of the red cell. In kidney failure that life is shorter, and treatments common in the unit, such as an erythropoiesis-stimulating agent (ESA), intravenous iron, and blood transfusion, add young red cells that have had less time to collect glucose. The result tends to read lower than the true average glucose, so a reassuring HbA1c can hide high readings. The international diabetes guideline for CKD notes that HbA1c becomes less reliable at the most advanced stages, especially on dialysis, and that home glucose checks or a continuous glucose monitor can help when HbA1c and daily readings disagree.[[kdigo2022dm]] Other blood tests of average glucose, such as glycated albumin or fructosamine, have their own limits and are ordered by the physician where available. HbA1c is itself a surrogate: a laboratory marker of average glucose, not an outcome the patient feels. Your contribution is simple and valuable. Report when HbA1c and the patient&rsquo;s own readings do not tell the same story, and note any recent transfusion or new ESA or iron course beside the result.</p>
<p><strong>Checking glucose at the chair.</strong> The unit protocol states who is checked, when, and how. Common points are:</p>
<div class="table-wrap"><table>
<thead><tr><th>When</th><th>Why</th><th>What to note</th></tr></thead>
<tbody>
<tr><td>On arrival, if the protocol includes it</td><td>A low reading before connection changes the plan for the session</td><td>Time of the last meal and of the last insulin or tablet dose</td></tr>
<tr><td>With any suggestive symptom during treatment</td><td>Sweating, tremor, confusion, or drowsiness can look like low blood pressure (BP) or disequilibrium</td><td>Glucose and BP together, before attributing symptoms to either</td></tr>
<tr><td>Before the patient leaves, if the protocol includes it</td><td>Low readings often appear after the session</td><td>Reading, symptoms, and whether food is available on the way home</td></tr>
</tbody></table></div>
<ul>
<li><strong>Sample site.</strong> Use a fingerstick or a sample from the arterial side, as the protocol directs. Blood from the venous (return) line has just passed the dialyzer and reflects the dialysate glucose more than the patient&rsquo;s, so it can mislead.</li>
<li><strong>The meter.</strong> Use the unit&rsquo;s approved meter with quality-control checks done. Some meter types read falsely high in patients who use the icodextrin solution for peritoneal dialysis; a patient moving between therapies is flagged to the physician and the meter checked against the unit&rsquo;s list.</li>
<li><strong>Low reading.</strong> Treat per protocol: by mouth if the patient is alert and can swallow, intravenous glucose per order or protocol if not. Recheck at the interval the protocol sets, and inform the physician. Document each episode with the likely cause, because a pattern points to a dose or timing problem.</li>
<li><strong>Warning signs may be absent.</strong> Long-standing diabetes can blunt the body&rsquo;s alarm signals, and some heart and BP medicines mask the fast heartbeat and tremor. Check a patient who is simply quieter or slower than usual.</li>
</ul>
<p><strong>Diet coordination.</strong> The diabetic diet and the kidney diet can seem to contradict each other: fruit and some vegetables recommended for diabetes may be high in potassium, and protein needs rise once dialysis starts. A patient who has spent years cutting rice and eating more fruit may now be told the opposite in part. The dietitian builds one plan that fits both (Module 3). You make sure the messages heard in the unit match it. Raise the practical points with the team: whether the patient eats before coming, what snack is allowed or provided during the session under unit policy, and how insulin timing fits the dialysis-day schedule, which the prescriber sets.</p>
<p><strong>On dialysis, insulin lasts longer and the session moves glucose on its own. Check glucose with blood pressure before you name the cause of any symptom.</strong></p>
"""},
    {"after": "diabetes-hd", "id": "diabetes-feet", "nav": "Feet and eyes", "tag": "Clinical application",
     "h2": "Feet, wounds, and eyes: protecting what diabetes and dialysis put at risk",
     "html": """
<p>People with diabetes on HD are at high risk of foot ulcers and amputation. Follow how the harms combine. Nerve damage removes the warning of pain, so a pebble in a slipper or a burn from a hot floor goes unnoticed. Narrowed and calcified arteries in the legs bring less blood to heal the small wound that follows. Dry skin cracks easily and lets bacteria in. Infection then spreads quickly in tissue with poor blood flow. The dialysis chair offers an advantage no clinic visit can match. You see the patient for hours, several times a week, often with the feet uncovered.</p>
<p><strong>The chair-side foot check.</strong> The unit protocol sets how often a full check is done and how it is recorded; a quick look at every session costs little. A structured check covers:</p>
<ul>
<li><strong>Skin:</strong> cracks, calluses, blisters, redness, and the areas between the toes, where moisture and fungal infection hide.</li>
<li><strong>Color and temperature:</strong> a cold, pale, or dusky foot, or one foot warmer and redder than the other.</li>
<li><strong>Pulses</strong> at the ankle and top of the foot, where the protocol includes them, and how quickly color returns after pressure.</li>
<li><strong>Nails:</strong> ingrown or thickened nails, and signs of cutting too close.</li>
<li><strong>Sensation:</strong> by the simple test the unit has adopted, if any, or by asking whether the patient can feel the floor and the slipper.</li>
<li><strong>Footwear:</strong> slippers that rub, shoes that are too tight from swelling, and walking barefoot at home or outdoors, which is common and risky.</li>
</ul>
<p><strong>A wound is referred the same day.</strong> Any break in the skin, blister, black or blue area, swelling, discharge, or new pain in a foot is reported to the physician at that session, not at the monthly round, and documented with its size, appearance, and location. Infection in a diabetic foot can progress over days, and a patient with poor circulation may need assessment by a wound or vascular specialist. Do not start home remedies or soaking. Teach the patient not to apply herbal preparations, hot compresses, or strong antiseptics to a foot wound, because a numb foot burns easily and some products damage tissue. Dressings follow the physician&rsquo;s order.</p>
<p><strong>Teaching that protects the feet.</strong> Teach the patient and family, by teach-back, to:</p>
<ul>
<li>look at both feet every day, using a mirror or a family member for the soles;</li>
<li>wear footwear indoors and out, and check inside shoes before putting them on;</li>
<li>wash and dry the feet daily, especially between the toes, and moisturize the skin but not between the toes;</li>
<li>have nails cut straight across, by a trained person if vision or reach is poor;</li>
<li>never use a blade on calluses, and never test bath water with the feet;</li>
<li>report any wound, color change, or swelling at the next session, or sooner if it worsens.</li>
</ul>
<p><strong>Eyes.</strong> Diabetic eye disease usually progresses without symptoms until vision is threatened, and patients on dialysis often miss eye appointments because their week is already full. Check that a regular eye examination is in the care plan as the physician advises, help the patient fit it around dialysis days, and record the date of the last examination. Sudden loss or blurring of vision, a curtain or shadow across the visual field, or a burst of new floaters is an urgent problem: it is reported to the physician the same day, and the physician decides on eye referral and on any change to the heparin order. Poor vision also matters at the chair: it affects how a patient reads a glucose meter, draws up insulin, checks the feet, and recognizes medicines, so teaching is adapted, and a family member is involved where needed.</p>
<p><strong>Putting it together at the round.</strong> For each patient with diabetes, bring a short summary to the monthly round: glucose episodes since the last round, the most recent HbA1c with its caveats, any foot findings and referrals, the date of the last eye examination, and diet or meal-timing problems raised by the patient. This gives the physician and dietitian a single picture instead of scattered notes.</p>
<p><strong>A painless blister on a numb, cool foot is urgent. Report it the same session, and never wait for the patient to complain.</strong></p>
"""},
]
QUIZ = [
    {"stem": "A patient with diabetes on HD has an HbA1c in the target range set by her physician. She received a blood transfusion six weeks ago and her ESA dose was increased last month. Her home glucose diary shows many readings well above her usual range. What do you do?",
     "options": [
         ("Reassure her that her diabetes is well controlled because the HbA1c is in range", False, "HbA1c tends to read low on dialysis, especially after a transfusion or more ESA, so it may not reflect the high home readings."),
         ("Advise her to increase her insulin dose until the home readings come down", False, "Nurses do not change doses; the prescriber decides any change to treatment."),
         ("Report that the HbA1c and home readings disagree, noting the recent transfusion and ESA change, for the physician's review", True, "A shorter red-cell life, transfusion, and ESA therapy can make HbA1c read falsely low. When it disagrees with home readings, the physician needs both, with the reasons that may explain the gap."),
         ("Ask the laboratory to repeat the HbA1c, because a result that disagrees with the diary must be a laboratory error", False, "The difference is expected on dialysis; repeating the same test does not solve the problem, and other tests are ordered by the physician."),
     ],
     "objective": "Explain why blood glucose behaves differently on hemodialysis (HD), including slower insulin clearance, glucose in the dialysate, and the limits of glycated hemoglobin (HbA1c), and check and respond to glucose at the chair per protocol.", "sources": ["kdigo2022dm"], "flag": ""},
    {"stem": "During treatment, a patient with diabetes and poor eyesight mentions that his slipper has been rubbing. You find a small blister on the side of his foot, which he had not felt, and the foot is cooler than the other one. What is the best action?",
     "options": [
         ("Teach him to soak the foot in warm water with salt at home, and look again next session", False, "Soaking softens the skin and a numb foot burns easily; a wound in a cool, numb foot needs prompt medical assessment."),
         ("Document the blister's size and location, report it to the physician today, and teach daily foot checks with family help and footwear that does not rub", True, "Loss of sensation and reduced blood flow make a small blister dangerous. Same-day reporting allows assessment and referral, and teaching involves the family because his vision is poor."),
         ("Wait for the monthly round, since the blister is small and he has no pain", False, "Absence of pain reflects nerve damage, not safety; waiting allows infection to progress."),
         ("Burst the blister to relieve pressure and apply an antiseptic from the unit stock", False, "Wound care follows the physician's order; opening a blister breaks the skin barrier."),
     ],
     "objective": "Check the feet of a patient with diabetes on HD at the chair, refer a wound promptly, and coordinate diet, meal timing, and eye care with the dietitian and physician.", "sources": ["anna7"], "flag": "Foot-check frequency and wound referral pathway follow unit protocol."},
]
TERMS = [
    ("Dialysate glucose", "Glucose added to the dialysis concentrate at about the level of normal blood glucose, which steadies blood glucose during the session."),
    ("Glycated hemoglobin (HbA1c)", "Glucose attached to hemoglobin, reflecting average glucose over the red-cell life span; tends to read low on dialysis."),
    ("Continuous glucose monitor", "A small sensor under the skin that reads tissue glucose throughout the day and night."),
    ("Diabetic foot check", "A structured look at the skin, color, temperature, pulses, nails, sensation, and footwear of a person with diabetes."),
]
FLAGS = [
    "No glucose thresholds, dialysate glucose concentrations, treatment amounts, or HbA1c targets are stated; all follow the physician's order and unit protocol.",
    "The KDIGO 2022 diabetes guideline is cited for the reduced reliability of HbA1c in advanced CKD and dialysis and for the role of home glucose checks or continuous monitoring when results disagree; please confirm the practice-point wording against the guideline text.",
    "The statements that insulin resistance partly improves with dialysis, that glucose may fall in the hours after a session, and that hyperglycemia may raise thirst and serum potassium are physiology taught with 'may'; no outcome data are cited.",
    "The icodextrin meter interference statement is general; the unit should keep its own list of meters approved for patients on icodextrin.",
    "Foot-check frequency, sensation test (for example a monofilament), and the wound referral pathway are left to unit protocol; no amputation or ulcer rates are stated.",
    "The heparin-and-eye-bleeding remark is phrased as a physician decision only; no evidence on retinal bleeding with dialysis heparin is cited.",
    "fetch_refs.py globs m??_x*.py, so NEW_REFS in this file should be picked up; confirm kdigo2022dm is added to refs_pubmed_raw.json.",
]
NEW_REFS = {
    "kdigo2022dm": "36272764",
}
