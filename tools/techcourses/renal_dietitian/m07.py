# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 07: Phosphorus, Calcium, Vitamin D, and Bone. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian pointing to the ingredient list on a processed meat package while a patient holds a pill organizer.",
    "objectives": [
        "Explain why phosphorus control on dialysis depends on diet, binders, and dialysis together.",
        "Rank phosphorus sources by absorption and find phosphate additives on an ingredient list.",
        "Use the phosphorus-to-protein ratio to lower phosphorus without lowering protein.",
        "Teach binder timing and find the practical reasons binders are missed, without changing a dose.",
        "Describe what the guidelines recommend, with grades, and what the HiLo trial did and did not show.",
        "Account for calcium from food, binders, and supplements, and for vitamin D status.",
    ],
    "big": """
{{plain:Phosphorus is like dust in a house with a weak vacuum. Dialysis is the vacuum and it runs only a few hours a week. Binders are doormats that trap dust at the door, but only if they are in place when someone walks in, which means with food. Diet is how much dust is carried in. No single one of the three keeps the house clean.}}
<p>The picture has a limit. The body is not a closed house: phosphorus moves in and out of bone under the control of parathyroid hormone (PTH) and fibroblast growth factor 23 (FGF23), so the blood level can rise from bone even when intake is modest. And the serum phosphorus you are steering is a surrogate; no trial has yet shown that lowering it to a target prevents death or hospital admission.</p>
<p>Your work is to cut the phosphorus that brings no protein, time the binders with food, and hand the bone signals to the physician.</p>
{{cards:Key terms for this module|Phosphorus and phosphate::Phosphorus is the element in food tables; phosphate is its form in blood and in additives. In practice the words are used together.|Phosphate binder::A medicine taken with food that traps phosphate in the gut so it leaves in the stool.|Phosphate additive::An inorganic phosphate salt added to processed food for texture, moisture, or shelf life. Nearly all of it is absorbed.|Phosphorus-to-protein ratio::Milligrams of phosphorus per gram of protein in a food. Lower is better when protein must be kept high.|Secondary hyperparathyroidism::Overactive parathyroid glands driven by kidney disease.|Calcium load::Total elemental calcium from food, calcium-based binders, and supplements.|25-hydroxyvitamin D::The blood test for vitamin D stores.}}
{{flow:Where phosphorus control fails|Intake::Additives and large portions of processed food.|Binders::Not taken, taken late, or not matched to meals and snacks.|Dialysis::Missed or shortened sessions.|Bone and hormones::High PTH releasing phosphorus from bone; vitamin D medicines raising absorption.}}
""",
    "case": {"title": "The workday binder", "html": """
<p>Ms. Aquino, 46, has been on hemodialysis for two years. Her phosphorus was 6.4 mg/dL last month and is 6.7 mg/dL now. Calcium is 9.6 mg/dL and intact PTH is 580 pg/mL, rising over six months. She takes sevelamer, &ldquo;one with each meal.&rdquo;</p>
<p>She works in a call center. On workdays she skips the binder because she is unsure whether to take it before or after eating and does not like colleagues to see her pills. Lunch is usually a hotdog or tocino meal with a cola, and she drinks three sachets of 3-in-1 coffee a shift. Her appetite is poor; she eats about 0.9 g/kg/day of protein.</p>
""", "questions": ["Which of the three controls (diet, binders, dialysis) is failing, and where exactly?",
                  "Which food changes lower phosphorus without lowering her protein?",
                  "What do you ask the pharmacist or nephrologist, and what do you not change yourself?"]},
    "sections": [
        ("why", "Why it matters", "Three controls, none sufficient alone", """
<p>A typical mixed diet supplies about 1,000 to 1,400 mg of phosphorus a day, of which well over half is absorbed. A standard hemodialysis session removes on the order of 800 mg, three times a week. The arithmetic does not close: over a week, absorption exceeds removal for most patients who eat adequately, which is why most people on dialysis are prescribed binders and why adequate protein intake and a normal phosphorus are in tension.[[kalantar2010]]</p>
<p>High phosphorus is associated with vascular calcification, fractures, and death in observational studies of people on dialysis, and it drives PTH upward. On that basis KDIGO suggests lowering elevated phosphate toward the normal range in CKD G3a to G5D (a weak suggestion, grade 2C), basing treatment on serial measurements of phosphate, calcium, and PTH considered together, and on progressively or persistently elevated phosphate (both advice without a formal grade).[[kdigo_mbd2017]] A KDIGO conference in 2023 judged these recommendations still consistent with the evidence and called for more personalized care.[[ketteler2025]]</p>
<p><strong>What has not been shown.</strong> No randomized trial has yet shown that lowering phosphorus to a particular target reduces death or hospital admission. The HiLo trial set out to compare a higher target (6.5 mg/dL or above) with a lower one (below 5.5 mg/dL) in people on in-center hemodialysis. It was stopped early after enrolling 793 of a planned 4,400 patients, with too little difference in phosphate between the groups; the primary outcome did not differ (win ratio 0.97; 95% confidence interval, 0.55 to 1.71), and the investigators concluded that no inference about phosphate targets could be drawn.[[hilo2025]] The trial neither supports strict control nor shows that loosening it is safe. Until better evidence arrives, follow your unit&rsquo;s target, and never pursue it at the cost of the patient&rsquo;s protein and energy intake.</p>
{{key:A normal phosphorus is a laboratory goal. How the body works and observational studies suggest it helps, but no trial has proven it. Losing muscle is a harm we know is real. When the two pull against each other, protect intake and go after the phosphorus that brings no protein.}}
<p><strong>Example from practice.</strong> Run the arithmetic for Mr. Velasco, 65 kg, eating 1.1 g/kg of protein, about 72 g a day. At about 12 mg of phosphorus per gram of protein, his protein foods bring about 860 mg. Colas and processed meat add perhaps 300 mg more, for about 1,160 mg a day. If about 60% is absorbed, that is about 700 mg a day, or 4,900 mg a week. Three sessions remove about 2,400 mg. About 2,500 mg a week must be handled by binders and by removing additives, and on a twice-weekly schedule the gap is wider.[[kalantar2010]] Asking him to cut his protein in half would close the gap at the cost of his muscle.</p>
{{fig:rd07_fig_weekly_phosphorus_balance}}
"""),
        ("sources", "Sources", "Find phosphorus that carries no protein", """
<p>KDOQI recommends adjusting dietary phosphorus to keep serum phosphate in the normal range (a firm recommendation, grade 1B) and says it is reasonable to consider how much of each source the body absorbs (expert opinion). KDIGO suggests limiting dietary phosphate, alone or with other treatments (a weak suggestion, grade 2D), and considering the source (advice without a formal grade).[[kdoqi2020]][[kdigo_mbd2017]] The source matters because absorption differs so much.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Approximate absorption</th><th>Examples</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Inorganic additives</td><td>About 90% or more</td><td>Processed meats, &ldquo;enhanced&rdquo; frozen chicken and seafood, colas, 3-in-1 coffee and non-dairy creamers, processed cheese, instant noodles, baking powder</td><td>Reduce first. They add phosphorus with little or no useful protein.</td></tr>
<tr><td>Animal foods</td><td>About 40% to 60%</td><td>Fish, meat, egg, milk</td><td>Keep for protein; choose by phosphorus-to-protein ratio.</td></tr>
<tr><td>Plant foods</td><td>About 20% to 40%</td><td>Beans, nuts, whole grains (phytate)</td><td>Usually no need to restrict.</td></tr>
</tbody></table></div>
<p>Absorption figures are approximate.[[kalantar2010]] Labels in the Philippines list ingredients but seldom the amount of phosphorus, so teach patients to search the ingredient list for the letters &ldquo;phos&rdquo;: phosphoric acid, sodium tripolyphosphate, dipotassium phosphate, calcium phosphate, pyrophosphate.</p>
<p><strong>The phosphorus-to-protein ratio.</strong> When a patient needs 1.0 to 1.2 g/kg/day of protein, choose protein foods with less phosphorus per gram. Egg white is the lowest (about 1 to 2 mg per gram of protein). Most fresh fish, chicken, pork, and beef fall around 8 to 12 mg/g. Milk, cheese, egg yolk, organ meats, and small fish eaten with bones (dilis, sardines) are higher, and processed meats with additives are highest. A target below about 12 mg/g for the day&rsquo;s diet has been proposed; it is a planning aid, not a validated threshold.[[kalantar2010]]</p>
<p>Boiling meat or fish in water and discarding the liquid lowers its phosphorus somewhat while keeping most of the protein. That makes nilaga a useful method, provided the patient does not then drink all the broth.</p>
{{fig:rd07_phos_sources}}
<p><strong>Example from practice.</strong> Ms. Aquino&rsquo;s workday lunch of a hotdog and a cola carries phosphorus that is absorbed almost completely, and little protein of value. Change two things: fried galunggong with rice in place of the hotdog, and water or calamansi juice in place of the cola. The phosphate additives are gone, and the protein is about the same or better. On weekends, three egg whites scrambled with tomato give about 10 g of protein with very little phosphorus. She keeps one whole egg for flavor. This is a protein trade, not a protein cut.</p>
"""),
        ("binders", "Binders", "Binders: timing is the dietitian&rsquo;s business, the dose is not", """
<p>A binder works only on the food that is in the gut with it. Taken an hour after the meal, it binds little. Taken with a cup of coffee and no food, it binds nothing useful. Teach the timing written on the prescription, usually with the first bites or during the meal, and ask the questions that find out why doses are missed.</p>
{{cards:Why binders are missed|Timing unclear::&ldquo;Before or after?&rdquo; Nobody showed her.|Meals away from home::The pills stay in the bathroom cabinet. A small container in the bag solves it.|Embarrassment::Taking several tablets in front of colleagues.|Snacks and merienda::A burger at 3 p.m. has more phosphorus than a light breakfast, but the binder is tied to &ldquo;three meals.&rdquo;|Side effects and size::Large tablets, bloating, constipation.|Cost::Fewer tablets taken to make the box last.}}
<p>Report what you find to the prescriber or pharmacist. Whether the dose should be spread differently across meals and snacks, changed to another binder, or increased is their decision. KDIGO suggests restricting the dose of calcium-based binders in adults receiving phosphate-lowering treatment (a weak suggestion, grade 2B) and avoiding high blood calcium (a weak suggestion, grade 2C), which is why the type of binder and the calcium level belong in your handoff.[[kdigo_mbd2017]]</p>
{{stop:Do not tell a patient to take extra binder for a large meal, to skip a binder, or to switch products. Reinforce the written instructions and ask the prescriber. A calcium above the laboratory range, or a patient taking calcium supplements in addition to a calcium-based binder, should be reported.}}
<p><strong>Example from practice.</strong> Mr. Sison, 49, on hemodialysis, takes calcium carbonate with breakfast, lunch, and dinner, as prescribed. He works nights. His largest phosphorus loads are a 3 p.m. merienda of pancit canton with 3-in-1 coffee and a 1 a.m. meal from the canteen, and he takes no binder with either. You record the times and the foods and send them to the prescriber: &ldquo;Meals at 7 a.m., 3 p.m., 7 p.m., and 1 a.m. Binder taken only with the first three; the 3 p.m. and 1 a.m. meals are the heaviest in phosphorus.&rdquo; Whether to move or add doses is the prescriber&rsquo;s decision.</p>
"""),
        ("calcium", "Calcium and vitamin D", "Count calcium, and ask about vitamin D", """
<p>Calcium balance in CKD is narrow. Too little worsens PTH; too much, especially with low PTH and little bone turnover, may deposit in blood vessels. KDOQI suggests a total elemental calcium intake of 800 to 1,000 mg a day, counting food, supplements, and calcium-based binders, for adults with CKD stages 3 to 4 not taking active vitamin D analogs (a weak suggestion, grade 2B), and individualized adjustment on dialysis in light of vitamin D analogs and calcimimetics (expert opinion).[[kdoqi2020]]</p>
{{formula:Calcium load (mg/day) = dietary calcium + elemental calcium in binders + elemental calcium in supplements. Calcium carbonate is 40% elemental calcium: a 500 mg tablet of calcium carbonate supplies 200 mg.}}
<p>Patients often take over-the-counter calcium &ldquo;for the bones&rdquo; without telling anyone, on top of a calcium-based binder. Add it up and report it.</p>
<p><strong>Vitamin D.</strong> Two different things share the name. Nutritional vitamin D (cholecalciferol or ergocalciferol) fills the body&rsquo;s stores, measured as 25-hydroxyvitamin D. Active vitamin D and its analogs (calcitriol, paricalcitol) are medicines for secondary hyperparathyroidism that raise calcium and phosphorus absorption. KDOQI suggests supplementing nutritional vitamin D to correct deficiency or insufficiency (a weak suggestion, grade 2C).[[kdoqi2020]] Both are prescribed by the physician. Your part is to ask what the patient takes, including high-dose products bought online, and to know that a rising phosphorus after an active vitamin D dose increase may not be dietary at all.</p>
{{fig:rd07_binder_timing}}
<p><strong>Example from practice.</strong> Mrs. Tolentino, 64, has G4 CKD and takes no active vitamin D. She takes calcium carbonate 500 mg with each of three meals as a binder: 3 &times; 200 = 600 mg of elemental calcium. She also takes an over-the-counter tablet labeled 600 mg of elemental calcium &ldquo;for the bones.&rdquo; Her food adds about 400 mg. The total is about 1,600 mg a day, against a KDOQI suggestion of 800 to 1,000 mg.[[kdoqi2020]] You report the total and both products. The prescriber decides which to change.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Which control is failing?</strong> Two of the three, and maybe a third. The binder is skipped on workdays, which is most days. The diet carries a lot of phosphorus that brings no protein: the hotdog or tocino, the cola with phosphoric acid, and three sachets of 3-in-1 coffee with phosphate salts in the creamer. Confirm with the nurse that she attends and completes her dialysis. Her rising PTH is also releasing phosphorus from bone, and that is a medical matter.</p>
<p><strong>Can you lower her phosphorus without lowering her protein?</strong> Yes, and you must. She eats only about 0.9 g/kg/day of protein, below what dialysis needs, so do not remove protein foods. Swap the processed-meat lunch for fresh fish, chicken, or egg with rice from the same canteen, or a packed meal. That lowers phosphorus and raises usable protein at the same time. Replace the cola with water. Move from 3-in-1 sachets to brewed or plain instant coffee, no creamer, with a little sugar if her glucose allows. Add egg whites, which carry almost no phosphorus.</p>
<p><strong>Is the binder yours to fix?</strong> The timing is yours to teach. The dose is not yours to change. Ask the pharmacist to confirm exactly when the prescription says to take it, and to help make it work on her shift: a pill case in her bag, and whether a dose should cover her afternoon snack.</p>
<p><strong>What do you tell the nephrologist?</strong> Phosphorus 6.4 then 6.7 mg/dL, calcium 9.6 mg/dL, PTH 580 pg/mL and rising, binders missed on workdays, the additive sources you found and are changing, and protein intake below target. Review her intake and next month&rsquo;s results together. A patient told only to &ldquo;avoid phosphorus&rdquo; usually ends up eating less protein. Finding the phosphorus that brings no protein is the dietitian&rsquo;s particular skill.</p>
"""],
    "skills": {"title": "Phosphorus review that protects protein",
               "intro": "Materials: three ingredient lists, a fictional monthly laboratory sheet, and a binder prescription.",
               "items": [
                   ("Reviews phosphorus with calcium and PTH trends, not as a single value.", False),
                   ("Finds phosphate additives on ingredient lists by searching for &ldquo;phos.&rdquo;", False),
                   ("Proposes swaps that lower phosphorus while keeping or raising protein.", True),
                   ("Asks when, where, and with what the binder is taken, and why doses are missed.", False),
                   ("Teaches binder timing exactly as prescribed and does not alter the dose.", True),
                   ("Adds up calcium from food, binders, and supplements and reports the total.", False),
                   ("Asks about vitamin D products, including those bought without prescription.", False),
                   ("Confirms dialysis attendance and delivered time with the nurse.", False),
                   ("Hands off to the pharmacist or nephrologist with numbers and a specific question.", False),
               ],
               "placement": "At a supermarket or sari-sari store, photograph the ingredient lists of ten commonly eaten processed foods and mark every phosphate additive."},
    "quiz": [
        ("Why do most patients on hemodialysis need binders despite dialysis?",
         ["Dialysis removes no phosphorus", "Weekly absorption usually exceeds what three sessions remove", "Binders replace dialysis", "Phosphorus is not absorbed"], 1,
         "A session removes on the order of 800 mg, less than typical absorption over the days between."),
        ("Which source of phosphorus is absorbed most completely?",
         ["Beans", "Fresh fish", "Phosphate additives in processed food", "Brown rice"], 2,
         "Inorganic additives are about 90% absorbed or more."),
        ("Which ingredient indicates a phosphate additive?",
         ["Sodium tripolyphosphate", "Citric acid", "Monosodium glutamate", "Ascorbic acid"], 0,
         "Look for &ldquo;phos&rdquo; in the ingredient list."),
        ("Which protein food has the lowest phosphorus-to-protein ratio?",
         ["Processed cheese", "Egg white", "Hotdog", "Dilis eaten with bones"], 1,
         "Egg white has about 1 to 2 mg of phosphorus per gram of protein."),
        ("A patient with low protein intake and high phosphorus should first:",
         ["Stop all fish and meat", "Reduce additive-containing foods and drinks", "Stop eating rice", "Double the binder"], 1,
         "Remove phosphorus that carries no protein; protect protein intake."),
        ("When should a phosphate binder be taken?",
         ["At bedtime", "With food, as the prescription states", "One hour after meals", "Only on dialysis days"], 1,
         "A binder acts on the food that is in the gut with it."),
        ("A patient asks to take an extra binder with a fiesta meal. You should:",
         ["Agree", "Tell her to skip the meal", "Reinforce the prescription and refer the question to the prescriber", "Stop the binder"], 2,
         "Dose changes belong to the prescriber."),
        ("KDIGO suggests that decisions about phosphate-lowering treatment be based on:",
         ["One high value", "Progressively or persistently elevated phosphate, with calcium and PTH considered together", "The patient&rsquo;s weight", "Albumin"], 1,
         "Serial measurements and the three values together guide treatment."),
        ("The HiLo trial showed that:",
         ["A higher phosphate target reduces death", "A lower phosphate target reduces death", "No inference about targets could be drawn; it stopped early with poor separation", "Binders are harmful"], 2,
         "Enrollment and phosphate separation were insufficient."),
        ("How much elemental calcium is in a 500 mg calcium carbonate tablet?",
         ["50 mg", "200 mg", "400 mg", "500 mg"], 1,
         "Calcium carbonate is 40% elemental calcium."),
        ("KDOQI suggests a total elemental calcium intake in CKD stages 3 to 4 (not on active vitamin D) of about:",
         ["200 to 400 mg/day", "800 to 1,000 mg/day", "2,000 to 2,500 mg/day", "No limit"], 1,
         "800 to 1,000 mg a day from all sources (a weak suggestion, grade 2B)."),
        ("Which is a medicine for secondary hyperparathyroidism and not a nutritional supplement?",
         ["Cholecalciferol", "Calcitriol", "Ergocalciferol", "Cod liver oil"], 1,
         "Calcitriol is active vitamin D; it raises calcium and phosphorus absorption."),
        ("Phosphorus rises after a dose increase of an active vitamin D analog. The likely explanation is:",
         ["More dietary phosphorus", "Increased intestinal phosphorus absorption from the medicine", "Laboratory error", "Too much dialysis"], 1,
         "Active vitamin D raises absorption of calcium and phosphorus."),
        ("Three sachets of 3-in-1 coffee a day matter for phosphorus because:",
         ["Coffee beans are high in phosphorus", "The creamer commonly contains phosphate salts", "Sugar binds phosphorus", "They do not matter"], 1,
         "Non-dairy creamers often contain phosphate additives."),
        ("Boiling meat and discarding the liquid:",
         ["Raises phosphorus", "Lowers phosphorus somewhat while keeping most protein", "Removes all protein", "Adds calcium"], 1,
         "Some phosphorus moves into the cooking liquid."),
    ],
    "terms": [("Vascular calcification", "Calcium phosphate deposits in artery walls."),
              ("Intact PTH", "The usual laboratory measure of parathyroid hormone."),
              ("Calcimimetic", "A medicine that lowers PTH by making the parathyroid gland more sensitive to calcium."),
              ("Elemental calcium", "The actual calcium content of a calcium salt."),
              ("Win ratio", "A way of analyzing a ranked composite outcome; 1.0 means no difference."),
              ("Surrogate target", "A laboratory value treated in the hope of improving outcomes patients feel.")],
    "readings": [("phosphorus-ckd.html", "Phosphorus for patients, with additive lists."),
                 ("calcium-iron-vitamin-e-safety.html", "Calcium and other supplements: what is safe."),
                 ("vitamin-d-philippines-kidney-disease.html", "Vitamin D in Filipino patients with kidney disease.")],
    "calcs": ["calc-phosphorus-load.html", "calc-ckd-mbd.html", "calc-corrected-calcium.html", "calc-mineral-metabolism-workbench.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
