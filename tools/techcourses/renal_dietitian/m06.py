# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 06: Potassium, Acid-Base Balance, and Fiber. Written for this series from published sources."""

MODULE = {
    "image_alt": "A market stall with bananas, leafy greens, and root crops; a dietitian talking with a vendor and a patient.",
    "objectives": [
        "Work through the non-diet causes of a high potassium before changing food.",
        "Distinguish highly absorbed potassium (additives, salt substitutes, juices) from potassium in whole plant foods.",
        "Decide when potassium restriction is justified, how tight, and when to lift it.",
        "Explain how fruits and vegetables correct metabolic acidosis, and which patients need caution.",
        "Use fiber and bowel regularity as part of potassium management.",
        "Recognize low potassium as a problem in its own right and report it.",
    ],
    "big": """
{{plain:Serum potassium is the water level in a small basin with one tap and three drains. Food is the tap. The drains are the cells (opened by insulin), the kidney (opened by aldosterone), and the bowel. When the level rises, most people reach for the tap. Often a drain is blocked: a new medicine, constipation, a missed dialysis, or acidosis. Turning down the tap while a drain is blocked helps little and costs the patient vegetables. The basin is close to the truth, with one caution: the level that matters to the heart can change in hours, so a high result is first a safety question.}}
{{cards:Key terms for this module|Hyperkalemia::Serum potassium above the laboratory&rsquo;s upper limit, commonly 5.0 or 5.5 mmol/L.|Hypokalemia::Serum potassium below the lower limit, commonly 3.5 mmol/L.|Pseudohyperkalemia::A falsely high result from red cells breaking in the sample (hemolysis), a tight tourniquet, or a delayed sample.|RAAS inhibitors::Renin&ndash;angiotensin&ndash;aldosterone system blockers: ACE inhibitors, angiotensin receptor blockers, and mineralocorticoid receptor antagonists. They protect the kidney and heart and raise potassium.|Potassium binder::A medicine that traps potassium in the gut. Prescribed by the physician.|Metabolic acidosis::Too much acid in the body, seen as a low serum bicarbonate.|Leaching::Soaking or boiling cut vegetables in plenty of water and discarding the water to remove some potassium.}}
{{flow:When potassium is high|Safety::Critical or with symptoms? Urgent pathway.|Is it real?::Hemolysis, sampling, timing after dialysis.|Drains::Medicines, bowel, acidosis, glucose, dialysis.|Concentrated sources::Salt substitutes, additives, juices, coconut water, supplements.|Only then::Adjust portions of whole foods, as little as needed.}}
""",
    "case": {"title": "No more vegetables", "html": """
<p>Mrs. Garcia, 64, has diabetic kidney disease, CKD G4. Her potassium was 5.7 mmol/L last month and 5.6 mmol/L this week; neither was flagged critical, and she has no symptoms. Her bicarbonate is 18 mmol/L. She takes telmisartan. A relative told her to stop all fruits and vegetables, and she has. She now opens her bowels every four or five days.</p>
<p>She drinks a glass of buko juice most afternoons &ldquo;for the kidneys,&rdquo; uses a &ldquo;low-sodium salt&rdquo; her daughter bought, and takes ibuprofen for knee pain. Her fasting glucose readings have been above 200 mg/dL.</p>
""", "questions": ["List every likely contributor to her potassium. Which are diet, and which are not?",
                  "Which two food-related changes would lower potassium most, at the least nutritional cost?",
                  "What do you report to the physician, and what do you leave to the physician?"]},
    "sections": [
        ("causes", "Causes", "Look for the blocked drain first", """
<p>KDIGO&rsquo;s conference on potassium concluded that hyperkalemia in CKD is usually the result of several factors together, and that diet is seldom the only one.[[clase2020]] KDOQI likewise asks clinicians to adjust dietary potassium to maintain a normal serum level, and on purpose it sets no single number for everyone.[[kdoqi2020]] Start with a checklist that puts diet last.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Why it raises potassium</th><th>Who acts</th></tr></thead>
<tbody>
<tr><td>Is the result real? Hemolyzed sample, long tourniquet time, sample taken soon after dialysis</td><td>Potassium leaks from blood cells in the tube</td><td>Physician decides on a repeat</td></tr>
<tr><td>New or increased RAAS inhibitor, potassium-sparing diuretic, trimethoprim, nonsteroidal anti-inflammatory drug, potassium supplement</td><td>Less kidney excretion, or added load</td><td>Physician; you report what the patient takes, including over-the-counter pain relievers</td></tr>
<tr><td>Constipation</td><td>Less colonic excretion</td><td>You: fiber, fluid within allowance, activity; physician: laxatives</td></tr>
<tr><td>Metabolic acidosis (low bicarbonate)</td><td>Potassium moves out of cells</td><td>Physician treats; diet contributes</td></tr>
<tr><td>High glucose or missed insulin; prolonged fasting</td><td>Less insulin-driven shift into cells</td><td>Diabetes team; you address meal timing</td></tr>
<tr><td>Missed, shortened, or inefficient dialysis</td><td>Less removal</td><td>Nephrologist and nurse</td></tr>
<tr><td>Concentrated potassium sources</td><td>Large, rapidly absorbed load</td><td>You</td></tr>
</tbody></table></div>
<p>RAAS inhibitors deserve a special note. They slow CKD progression and protect the heart, and stopping them for a mildly high potassium may cost the patient more than it gains. Your contribution is to remove other causes so the physician can keep the medicine going. Never advise a patient to stop one.</p>
{{stop:A potassium flagged critical, or any high potassium with weakness, palpitations, or a slow or irregular pulse, goes to the physician at once. Do not send the patient home with a diet sheet.}}
<p><strong>Example from practice.</strong> Mr. Mercado, 58, on hemodialysis, has a Monday potassium of 6.2 mmol/L, and the note on the report says &ldquo;slightly hemolyzed.&rdquo; The nurse recalls a difficult draw with a long tourniquet time. The physician orders a repeat, and it comes back at 4.9. Nothing about his diet needed to change. The month before, a similar rise was real, and the cause was co-trimoxazole for a urinary infection. In both months, the answer was found in the checklist before anyone looked at his plate.[[clase2020]]</p>
"""),
        ("sources", "Sources", "Not all dietary potassium is equal", """
<p>Potassium from different foods does not reach the blood equally. Potassium salts added to food and potassium chloride in salt substitutes are absorbed almost completely and quickly. Juices and coconut water deliver a large amount in a few swallows, without fiber. Whole fruits, vegetables, and legumes release potassium more slowly, bring fiber that speeds its exit through the bowel, and bring alkali that helps move potassium into cells.[[clase2020]] That is why KDIGO advises limiting foods whose potassium the body absorbs easily, such as processed foods, for people with CKD G3 to G5 who have a history of hyperkalemia (advice without a formal grade).[[kdigo_ckd2024]]</p>
{{cards:Review these before touching vegetables|Salt substitutes::&ldquo;Low-sodium&rdquo; or &ldquo;lite&rdquo; salts with potassium chloride.|Additives::Potassium chloride, potassium lactate, potassium phosphate, and potassium sorbate on ingredient lists of processed meats, sauces, and &ldquo;reduced-sodium&rdquo; products.|Drinks::Buko juice, fruit juices, vegetable juices, malunggay or other leaf &ldquo;shots,&rdquo; some sports and herbal drinks.|Dried and concentrated foods::Dried fruit, tomato paste, chocolate and cocoa drinks, large portions of nuts.|Supplements::Multivitamin-minerals with potassium, herbal products such as noni juice.}}
<p>If potassium stays high after the drains and the concentrated sources are dealt with, adjust whole foods with the lightest touch that works: smaller portions of the highest-potassium items the patient eats often (banana, avocado, ripe mango, kamote and other root crops, tomato sauce, legumes), with replacements, not gaps. Boiling cut root crops and vegetables in plenty of water and discarding the water lowers their potassium, at the cost of water-soluble vitamins. Where a number is needed, units commonly work to about 2,000 to 3,000 mg (50 to 75 mmol) a day; this range is convention, not a graded recommendation, and it should be lifted when the potassium is controlled or a binder is started.</p>
<p>The evidence that restricting whole-food potassium improves outcomes is thin. In the largest cohort on hemodialysis, reported potassium intake was not associated with serum potassium, hyperkalemia, or death.[[bernier2021]] This is observational and questionnaire-based; it does not license unlimited intake for an individual with repeated high values, but it does mean that a blanket ban on fruits and vegetables has no outcome evidence behind it and has known costs in fiber, alkali, and enjoyment.</p>
{{fig:rd06_potassium_sources}}
<p><strong>Example from practice.</strong> Mrs. Herrera, 63, has G4 CKD, and her potassium is 5.5 mmol/L. She has already stopped bananas. She drinks a large glass of buko juice every afternoon. A glass of coconut water can carry roughly 600 mg of potassium, more than a medium banana, delivered in a few swallows without fiber. She also uses tomato paste in most dishes. You swap the juice for water with calamansi, use fresh tomato in place of paste, and keep her vegetables. Her potassium is rechecked in four weeks, as her physician planned.</p>
"""),
        ("acid", "Acid and fiber", "Acidosis, fruits and vegetables, and the bowel", """
<p>As Module 2 described, animal protein and grains produce acid, and fruits and vegetables supply alkali. KDOQI states that it is reasonable to keep serum bicarbonate at 24 to 26 mmol/L (expert opinion), and suggests reducing net acid production with more fruits and vegetables (a weak suggestion, grade 2C) or bicarbonate supplementation (a firm recommendation, grade 1C) in adults with CKD stages 1 to 4.[[kdoqi2020]] KDIGO advises considering treatment, with or without dietary change, to prevent acidosis with clinical consequences, for example a bicarbonate below 18 mmol/L (advice without a formal grade).[[kdigo_ckd2024]]</p>
<p>In a one-year randomized trial in 71 people with stage 4 hypertensive kidney disease, fruits and vegetables dosed to halve dietary acid raised blood bicarbonate and lowered urinary markers of kidney injury, as sodium bicarbonate did, and plasma potassium did not rise in either group.[[goraya2013]] Now look at who was in it. Patients were chosen for a low risk of hyperkalemia, and the outcomes were laboratory markers, not kidney failure. The trial shows that the approach can be safe in selected patients with close monitoring. It does not show that it is safe for someone like Mrs. Garcia while her potassium is 5.6.</p>
<p><strong>Fiber and the bowel.</strong> The colon becomes an important exit for potassium as kidney function falls, so constipation matters. It is common in CKD because of fluid limits, binders, iron tablets, low activity, and the very restriction of fruits and vegetables meant to help. Restoring fiber, from vegetables, lower-potassium fruits, oats, and whole grains as phosphorus allows, is potassium management. Increase gradually and tell the physician if bowel habit does not improve; laxative choice is a medical decision.</p>
{{key:A patient who stops all fruits and vegetables loses fiber and alkali, becomes constipated and more acidotic, and may end with a higher potassium than before. Liberalize safely instead of restricting widely.}}
<p><strong>Example from practice.</strong> Mr. Galang, 66, has G4 CKD. His bicarbonate is 17 mmol/L, his potassium 4.6 mmol/L, and he opens his bowels twice a week. Unlike Mrs. Garcia, he has room on potassium. The physician starts sodium bicarbonate. You add vegetables and lower-potassium fruit gradually, with oats at breakfast, and ask the team to recheck his potassium within a few weeks.[[kdoqi2020]][[goraya2013]] Eight weeks later his bicarbonate is 21 mmol/L, his potassium 4.8, and his bowels move every day. The same food plan would have been wrong for a patient whose potassium was already 5.6.</p>
"""),
        ("low", "Low potassium", "The other direction: low potassium", """
<p>Low potassium is less discussed and also dangerous: it causes weakness, cramps, constipation, and rhythm disturbances. In kidney care it appears with poor intake, vomiting or diarrhea, loop or thiazide diuretics, and in peritoneal dialysis, where potassium is removed continuously by fluid that contains none (Module 10). On hemodialysis, a patient who eats poorly and dialyzes against a low-potassium dialysis fluid can leave the session with a low level.</p>
<p>A low or falling potassium is a prompt to ask about intake and losses and to tell the physician, who decides on supplements or a change in dialysis fluid. It is also the moment to cancel an old potassium restriction that nobody lifted. Old restrictions are among the most common findings in a first renal consult.</p>
{{cards:When to lift a potassium restriction|Potassium normal on repeated checks::Especially after a cause was corrected.|A potassium binder was started::The physician may want diet liberalized.|Intake or weight is falling::Protecting intake comes first.|Peritoneal dialysis, or low potassium::Restriction is usually wrong.|After transplant with good function::Reassess from current results (Module 12).}}
{{fig:rd06_decision}}
<p><strong>Example from practice.</strong> Mrs. Espiritu, 70, on hemodialysis, went home three weeks ago after a hip fracture. Her appetite is poor, and her pre-dialysis potassium is 3.3 mmol/L. On her refrigerator is a diet sheet from 2019: &ldquo;No banana, no potato, no tomato.&rdquo; Nobody has looked at it since. You lift the restriction and add a banana or boiled kamote on non-dialysis days. You also tell the nephrologist, because the potassium level in her dialysis fluid is part of the prescription and may need review.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What is raising her potassium?</strong> Several things, and most are not food. Telmisartan is one; it protects her kidneys and heart, and stopping it is not your call. Ibuprofen is another: it lowers potassium excretion and can harm kidney function. Her bicarbonate of 18 mmol/L means acidosis, which pushes potassium out of cells. Her glucose is high, so less potassium is driven into cells. Constipation has closed part of the bowel route. On the food side, there are two concentrated sources: the salt substitute and the daily buko juice.</p>
<p><strong>Was stopping all vegetables a good idea?</strong> No. She has already stopped them, and her potassium has not come down. She has lost fiber and alkali, and she is more constipated and more acidotic than before. The restriction may be making the problem worse.</p>
<p><strong>Which two changes help most for the least cost?</strong> Stop the salt substitute, and replace the buko juice with water. Both deliver potassium that is absorbed almost completely and brings nothing she needs. Then bring vegetables and lower-potassium fruits back in measured portions, to restore fiber and alkali and to ease the constipation.</p>
<p><strong>What do you report, and what do you leave?</strong> Report to the physician: potassium 5.7 then 5.6 mmol/L, bicarbonate 18, daily ibuprofen, fasting glucose above 200 mg/dL, constipation, and the two food sources you have stopped. Leave to the physician: whether to repeat the potassium, the pain reliever, treatment of acidosis, the telmisartan, a potassium binder, laxatives, and her glucose medicines. Agree on a recheck date, and plan to lift any restriction once her potassium is controlled. Finding the blocked drains is often the most useful thing a dietitian does for a high potassium.</p>
"""],
    "skills": {"title": "Working up a high potassium from the nutrition side",
               "intro": "Use a fictional card with two potassium results, a medicine list, a bowel history, and a food recall.",
               "items": [
                   ("Checks first whether the result is critical or accompanied by symptoms, and escalates if so.", True),
                   ("Asks about sample quality and timing, and leaves the decision to repeat to the physician.", False),
                   ("Reviews medicines, including over-the-counter pain relievers and supplements, and reports them without advising the patient to stop a prescribed medicine.", True),
                   ("Asks about bowel habit, glucose control, and dialysis attendance.", False),
                   ("Identifies salt substitutes, additives, juices, and coconut water before whole foods.", False),
                   ("If whole foods are adjusted, names specific items and portions and gives replacements.", False),
                   ("Protects fiber, energy, and protein intake in the plan.", False),
                   ("States the conditions under which the restriction will be lifted and sets a recheck date with the team.", False),
               ],
               "placement": "Review the potassium results of ten patients with your preceptor. For each value above range, list the non-diet causes you can find in the record."},
    "quiz": [
        ("A stable patient has a mildly high potassium on two checks. What comes before changing whole-food intake?",
         ["Nothing; restrict vegetables at once", "Review of sample quality, medicines, bowel habit, acidosis, glucose, dialysis, and concentrated sources", "Stopping the angiotensin receptor blocker yourself", "A protein restriction"], 1,
         "Hyperkalemia is usually multifactorial, and diet is seldom the only cause."),
        ("Which ingredient most deserves attention on a &ldquo;low-sodium salt&rdquo; label?",
         ["Citric acid", "Potassium chloride", "Iodine", "Anti-caking agent"], 1,
         "Potassium chloride is absorbed almost completely."),
        ("Why is a glass of buko juice a different load from a serving of vegetables with similar potassium?",
         ["It contains sodium", "It is absorbed quickly and without fiber", "It contains protein", "It is not different"], 1,
         "Liquids deliver potassium rapidly; whole foods bring fiber and alkali."),
        ("A hemolyzed blood sample can cause:",
         ["Falsely low potassium", "Falsely high potassium", "Falsely low glucose", "No change"], 1,
         "Potassium leaks from broken red cells: pseudohyperkalemia."),
        ("Which over-the-counter medicine can raise potassium and harm kidney function?",
         ["Paracetamol", "Ibuprofen", "Loperamide", "Antacid"], 1,
         "Nonsteroidal anti-inflammatory drugs reduce kidney potassium excretion."),
        ("A patient asks whether to stop her angiotensin receptor blocker because of potassium. You should:",
         ["Tell her to stop it", "Tell her to halve it", "Explain that the physician decides, and report the other causes you found", "Ignore the question"], 2,
         "RAAS inhibitors are protective; the dietitian helps remove other causes."),
        ("How does constipation raise potassium in advanced CKD?",
         ["It raises aldosterone", "It reduces colonic potassium excretion", "It increases absorption of sodium", "It does not"], 1,
         "The colon is an important exit route when eGFR is low."),
        ("KDOQI&rsquo;s statement on dietary potassium is:",
         ["Restrict everyone to 2,000 mg/day (1A)", "Adjust intake to maintain serum potassium in the normal range (expert opinion)", "Never restrict", "Restrict only fruit"], 1,
         "It is an opinion-based statement that calls for individualization."),
        ("In the trial of fruits and vegetables for acidosis in stage 4 CKD, potassium did not rise. An important limit is that:",
         ["Patients were selected for low hyperkalemia risk", "No one ate vegetables", "It lasted one day", "It was done in dialysis patients"], 0,
         "The result applies to selected, monitored patients."),
        ("KDIGO suggests considering treatment to prevent acidosis with clinical consequences at a bicarbonate below about:",
         ["30 mmol/L", "26 mmol/L", "18 mmol/L", "10 mmol/L"], 2,
         "A practice point gives below 18 mmol/L in adults as an example."),
        ("Which change is most likely to lower potassium at the least nutritional cost?",
         ["Stopping all vegetables", "Stopping the salt substitute and juices", "Halving rice", "Stopping fish"], 1,
         "Removing concentrated, fully absorbed sources costs little nutritionally."),
        ("Boiling cut root crops in plenty of water and discarding the water:",
         ["Raises potassium", "Lowers potassium and also removes some vitamins", "Has no effect", "Removes protein"], 1,
         "Leaching lowers potassium content, with loss of water-soluble vitamins."),
        ("In which patient is potassium restriction usually wrong?",
         ["Peritoneal dialysis with a potassium of 3.3 mmol/L", "CKD G5 with repeated potassium of 6.0 mmol/L", "A patient using a salt substitute", "None"], 0,
         "Low potassium is common in peritoneal dialysis and should be reported, not restricted."),
        ("An old potassium restriction should be lifted when:",
         ["Never", "Potassium is normal on repeated checks or a binder has been started", "The patient asks for sweets", "Albumin rises"], 1,
         "Restrictions should end when the reason ends."),
        ("The observational finding that dietary potassium was not associated with serum potassium on hemodialysis means:",
         ["Diet never matters", "Blanket bans lack outcome support, but individuals with repeated high values still need assessment", "All patients should take potassium supplements", "The study proves cause and effect"], 1,
         "It weakens the case for universal restriction without proving intake is irrelevant."),
    ],
    "terms": [("Bioavailable", "Able to be absorbed and reach the blood."),
              ("Mineralocorticoid receptor antagonist", "A medicine that blocks aldosterone, such as spironolactone or finerenone."),
              ("Alkali", "A base that neutralizes acid; supplied by fruits and vegetables as citrate and similar salts."),
              ("Hemolysis", "Breaking of red blood cells."),
              ("Buko juice", "Young coconut water."),
              ("Kamote", "Sweet potato.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "The patient guide on potassium."),
                 ("fiber-patient-education.html", "Fiber and bowel health in kidney disease."),
                 ("plant-forward-renal-diet.html", "Bringing vegetables back safely.")],
    "calcs": ["calc-potassium-load.html", "calc-fiber-intake-tracker.html", "calc-bicarb-deficit.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
