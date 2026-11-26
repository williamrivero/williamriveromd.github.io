# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 14: Vitamins, Minerals, Supplements, and Foods That Harm. Written for this series from published sources."""

MODULE = {
    "image_alt": "A table covered with supplement bottles, herbal tea packets, and star fruit, a dietitian reading one label with a magnifier.",
    "objectives": [
        "Explain which vitamins are lost in dialysis and which build up in kidney failure.",
        "Advise on water-soluble vitamin supplements for patients with poor intake or on dialysis.",
        "Explain why vitamin A and high-dose vitamin C can harm people with kidney failure.",
        "Review a patient&rsquo;s supplement bag in a structured way.",
        "Recognize star fruit (balimbing) and kamias as dangerous for people with kidney disease.",
        "Route herbal and supplement questions to the physician and pharmacist.",
    ],
    "big": """
{{plain:Water-soluble vitamins are like coins in an open hand: whatever is not used soon slips away in the urine or, on dialysis, into the dialysis fluid. Fat-soluble vitamins and some minerals are like coins in a closed fist: the healthy kidney opens the fist to release the excess, and a failed kidney cannot. So dialysis patients may run short of the first kind and build up too much of the second.}}
<p>The picture has a limit. Not every vitamin follows the hand. Vitamin D is fat-soluble, yet it is often low in kidney disease and may need replacing under the team&rsquo;s direction, while vitamin C is water-soluble, yet large doses turn into oxalate that a failed kidney cannot clear. The open hand and the closed fist are a sorting rule, not a law; the label and the laboratory result decide. Your work in this module is to sort every product the patient brings, keep what helps, and stop what can harm.</p>
{{cards:Key terms for this module|Water-soluble vitamins::B vitamins (including thiamine, folate, and B12) and vitamin C. Lost in dialysis.|Fat-soluble vitamins::A, D, E, and K. Stored in the body.|Renal multivitamin::A product with B vitamins and modest vitamin C, without vitamin A or minerals that build up.|Oxalate::A compound in some foods and made from vitamin C; forms crystals with calcium in the kidney.|Caramboxin::A nerve toxin in star fruit that a failing kidney cannot clear.|Kamias::Averrhoa bilimbi, a sour fruit related to star fruit, rich in oxalate.}}
{{flow:The supplement bag review|Bring everything::Pills, powders, teas, drinks, creams.|Read each label::Ingredients and amounts.|Sort::Needed, harmless, duplicate, or risky.|Report::Risky items to the physician and pharmacist.|Teach::Why, and what to do instead.}}
""",
    "case": {"title": "The bag of bottles", "html": """
<p>Mrs. Castro, 66, on hemodialysis for a year, brings a bag her son filled after reading online. It holds a general multivitamin with vitamin A 5,000 IU, vitamin C 1,000 mg tablets, a calcium-plus-vitamin-D tablet, a magnesium supplement, noni juice, and a &ldquo;kidney detox&rdquo; herbal tea. She also says a neighbor gave her balimbing &ldquo;to cleanse the kidneys,&rdquo; and she has eaten two.</p>
<p>She feels well today. Her potassium is 5.6 mmol/L, and her calcium is at the top of the range.</p>
""", "questions": ["Which item worries you most, and what will you do now?",
                  "Which items could harm her, and why?",
                  "What would a sensible vitamin plan look like?"]},
    "sections": [
        ("vitamins", "Vitamins", "What is lost and what builds up", """
<p>Dialysis removes small molecules that dissolve in water, and that includes B vitamins and vitamin C. Poor appetite, restrictions on fruits and vegetables, and inflammation add to the shortfall. Fat-soluble vitamins behave differently. Vitamin A is normally cleared by the kidney, and its levels rise in kidney failure, sometimes to toxic levels with bone pain, high calcium, and dry skin.[[kdoqi2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Vitamin</th><th>In kidney failure</th><th>Practical point</th></tr></thead>
<tbody>
<tr><td>B vitamins (thiamine, B6, folate)</td><td>Lost in dialysis; intake often low</td><td>KDOQI considers supplementing reasonable when intake is poor</td></tr>
<tr><td>Vitamin B12</td><td>Usually adequate; check if deficient</td><td>Supplement if deficient</td></tr>
<tr><td>Vitamin C</td><td>Lost in dialysis; excess turns into oxalate</td><td>Modest supplement only if intake is low; avoid high doses</td></tr>
<tr><td>Vitamin A</td><td>Builds up</td><td>Avoid supplements</td></tr>
<tr><td>Vitamin D (nutritional)</td><td>Often deficient</td><td>Physician checks the level and prescribes</td></tr>
<tr><td>Vitamin E, vitamin K</td><td>Varies</td><td>Not routinely supplemented</td></tr>
</tbody></table></div>
<p>For dialysis patients whose intake stays inadequate, KDOQI considers a multivitamin with all the water-soluble vitamins reasonable, and it suggests folate, vitamin B12, or a B complex to correct a documented deficiency. It considers it reasonable not to give vitamin A or E routinely on dialysis because of toxicity. The multivitamin and vitamin A statements are expert opinion.[[kdoqi2020]] For vitamin C, it is reasonable to aim for the usual daily intake, about 75 to 90 mg, not the 1,000 mg tablets sold for colds; high doses raise oxalate, which can deposit in tissues and blood vessels.[[kdoqi2020]] The ESPEN micronutrient guideline adds that patients on CKRT lose water-soluble vitamins and trace elements continuously and need monitoring.[[berger2022]]</p>
<p>Zinc and selenium are not routinely supplemented. Iron is given by the physician based on iron tests, often intravenously on dialysis. Calcium and magnesium supplements add to loads the kidney cannot clear (Module 7).</p>
<p><strong>Example from practice.</strong> Mr. Lagman, 60, on hemodialysis, has taken vitamin C 1,000 mg every day for two years &ldquo;for immunity,&rdquo; along with a general multivitamin containing 5,000 IU of vitamin A. KDOQI considers about 75 to 90 mg of vitamin C a day reasonable, because high doses turn into oxalate. It advises against routine vitamin A supplements on dialysis, because vitamin A builds up.[[kdoqi2020]] You list both products for the physician and suggest asking about a renal vitamin. He still gets his B vitamins, without the oxalate and the extra vitamin A.</p>
"""),
        ("bag", "The supplement bag", "Review the bag, item by item", """
<p>Many patients take products their physicians do not know about. Ask every patient, at every review, to bring every pill, powder, tea, and drink. Read each label yourself.</p>
{{cards:Sort each item into one of four groups|Needed::Prescribed and appropriate, such as a renal multivitamin or a prescribed vitamin D.|Harmless::Low dose and nothing that builds up; still list it.|Duplicate::The same ingredient twice, such as calcium in two products.|Risky::Vitamin A, high-dose vitamin C, potassium, magnesium, phosphorus, aluminum, unknown herbs, &ldquo;detox&rdquo; products, juices such as noni (very high in potassium).}}
<p>You may advise that a non-prescribed product be stopped when its risk is clear and it is a food or over-the-counter product, following your facility&rsquo;s policy, and you must tell the physician. You do not stop a prescribed medicine. Herbal products are the hardest, because ingredients and amounts are often unknown, and some are contaminated. When in doubt, ask the patient to pause the product and bring it to the physician and pharmacist.</p>
{{fig:rd14_bag}}
<p><strong>Example from practice.</strong> Mrs. Cuenca, 68, on hemodialysis, has a calcium at the top of the range. Her bag holds a prescribed calcium carbonate binder, an over-the-counter calcium-and-vitamin D tablet, and a milk powder for &ldquo;strong bones&rdquo; fortified with calcium. Sort them. The binder is needed. The milk powder is food, and its calcium counts. The over-the-counter tablet duplicates the binder. You advise pausing that tablet under your facility&rsquo;s policy and tell the physician the same day. The physician decides about the binder.</p>
"""),
        ("starfruit", "Star fruit and kamias", "Star fruit and kamias: foods that harm", """
<p>Star fruit (balimbing, <em>Averrhoa carambola</em>) is common in Philippine markets and in folk remedies. It contains two harmful substances. Oxalate can deposit in the kidney and cause sudden kidney injury. Caramboxin, a nerve toxin, is normally cleared by the kidneys; when they fail, it builds up and causes hiccups, confusion, seizures, and coma.</p>
<p>A review of published cases found 136 people with star fruit poisoning; 69% already had kidney disease, but some had normal kidneys and ate large amounts or drank the juice on an empty stomach. Symptoms ranged from hiccups to prolonged seizures. Dialysis improved the nerve symptoms, and the authors advised early dialysis once poisoning is recognized.[[yasawardene2021]][[yasawardene2020]] This evidence comes from case reports. They cannot tell us how common poisoning is, but they show the harm is real and can be severe.</p>
<p>Kamias (<em>Averrhoa bilimbi</em>), the sour fruit used in sinigang and in juices, is a close relative rich in oxalate. Case reports describe sudden kidney injury from oxalate deposits after drinking kamias juice.[[bartholameuz2023]]</p>
{{stop:A patient with kidney disease who has eaten star fruit or drunk its juice, especially with hiccups, confusion, weakness, or vomiting, needs urgent medical assessment. Call the physician now. Tell every patient with CKD or on dialysis to avoid star fruit completely, and to avoid kamias juice and large amounts of kamias.}}
<p><strong>Example from practice.</strong> Mr. Mendoza, 69, on hemodialysis, ate three balimbing and drank a glass of the juice &ldquo;to clean the kidneys.&rdquo; Six hours later he had hiccups that would not stop, and by evening he was confused. His family thought it was a stroke. On the phone you ask what he ate, then direct the family to the emergency room and call the nephrologist. Early dialysis is the treatment for star fruit poisoning.[[yasawardene2021]] Days later, on the ward, you teach the family that star fruit is never safe for him.</p>
"""),
        ("herbs", "Herbs and remedies", "Herbs, teas, and &ldquo;kidney cleansers&rdquo;", """
<p>&ldquo;Kidney detox&rdquo; products claim to cleanse the kidneys. No product does that, and some cause harm. Herbal products can contain potassium, oxalate, heavy metals, or compounds that affect medicines. Some plants, such as those containing aristolochic acid, cause kidney failure outright.</p>
<p>Ask without judgment. Many patients use remedies because a relative cares about them, or because they fear dialysis. Respect that, explain the risk, and offer something the family can do instead: cook a meal the patient enjoys, help with the binder, come to the next clinic.</p>
{{key:When a patient asks about a remedy, the useful answer is not &ldquo;no&rdquo; alone. It is &ldquo;not this one, and here is why, and here is what would help instead.&rdquo;}}
{{call:Any herbal product in a transplant recipient, any product with unknown ingredients in a patient with CKD or on dialysis, or any new symptom after starting a remedy: report it to the physician and ask the pharmacist to review it.}}
<p><strong>Example from practice.</strong> Mrs. Panganiban, 59, has G3b CKD. For six weeks she has been drinking a &ldquo;kidney detox&rdquo; tea in a plain bag with no ingredient list. Her creatinine has risen from 1.6 to 2.2 mg/dL. Ask without blame: &ldquo;Who gave it to you? What did they hope it would do?&rdquo; Her son bought it because he is afraid she will need dialysis. Ask her to stop the tea and bring the bag to the physician and pharmacist. Then give the son something useful to do: cook her lunches with less salt and come to the next clinic visit.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What worries you most?</strong> The balimbing. She has eaten two star fruits and has kidney failure. Even though she feels well now, caramboxin can cause hiccups, confusion, and seizures, sometimes hours later. Call the physician now, tell them what she ate and when, and follow their instructions. She may need monitoring or extra dialysis. Tell her and her son that star fruit must not be eaten again.</p>
<p><strong>Which other items could harm her?</strong> The multivitamin with 5,000 IU of vitamin A, because vitamin A builds up in kidney failure. The 1,000 mg vitamin C tablets, because the excess becomes oxalate. Noni juice, which is very high in potassium, and her potassium is already 5.6 mmol/L. The calcium-plus-vitamin-D tablet, with her calcium at the top of the range. The magnesium supplement, which her kidneys cannot clear. The &ldquo;detox&rdquo; tea, with unknown contents.</p>
<p><strong>What would a sensible plan look like?</strong> Ask her to pause all of these and bring them to the physician and pharmacist, following your facility&rsquo;s policy. If the team agrees, a renal multivitamin with B vitamins and modest vitamin C, and vitamin D only if prescribed after a blood test. Thank her son for caring, and suggest helping in ways that fit her plan.</p>
<p><strong>And next time?</strong> Ask about supplements and remedies at every visit. Many patients do not think of them as medicines. A dietitian who asks routinely will find the bag before it causes harm.</p>
"""],
    "skills": {"title": "Supplement bag review",
               "intro": "The preceptor provides a bag of real or mock product labels and a fictional patient card.",
               "items": [
                   ("Asks the patient to bring every pill, powder, tea, and drink, and reads each label.", False),
                   ("Sorts each item as needed, harmless, duplicate, or risky, with reasons.", False),
                   ("Identifies vitamin A, high-dose vitamin C, potassium, magnesium, phosphorus, and calcium as risks in kidney failure.", False),
                   ("Recognizes star fruit ingestion as urgent and calls the physician at once.", True),
                   ("Advises avoiding star fruit and kamias juice and explains why.", False),
                   ("Reports risky items to the physician and pharmacist and does not stop a prescribed medicine.", True),
                   ("Responds to remedies with respect and offers alternatives the family can do.", False),
               ],
               "placement": "Review the supplement use of five patients with your preceptor and list every product the physician did not know about."},
    "quiz": [
        ("Which vitamins are lost in dialysis?",
         ["Vitamin A and D", "Water-soluble vitamins such as B vitamins and C", "Vitamin K only", "None"], 1,
         "Small water-soluble molecules pass into the dialysis fluid."),
        ("Why avoid vitamin A supplements in kidney failure?",
         ["It is lost in dialysis", "It builds up and can become toxic", "It raises potassium", "It lowers glucose"], 1,
         "The failing kidney cannot clear it."),
        ("Why avoid 1,000 mg vitamin C tablets?",
         ["They contain potassium", "Excess vitamin C turns into oxalate", "They raise protein", "They lower calcium"], 1,
         "Oxalate can deposit in tissues and vessels."),
        ("A sensible vitamin C intake for a dialysis patient is about:",
         ["10 mg", "75 to 90 mg", "1,000 mg", "5,000 mg"], 1,
         "The usual daily intake, not high doses."),
        ("Star fruit is dangerous in kidney disease because it contains:",
         ["Potassium only", "Oxalate and caramboxin", "Sodium", "Gluten"], 1,
         "Oxalate injures the kidney; caramboxin is a nerve toxin."),
        ("A dialysis patient ate two star fruits this morning and feels well. You should:",
         ["Reassure her", "Call the physician now", "Wait for symptoms", "Give water"], 1,
         "Symptoms can be delayed; early assessment matters."),
        ("Symptoms of star fruit poisoning include:",
         ["Hiccups, confusion, and seizures", "Hair loss", "Itchy eyes only", "Weight gain"], 0,
         "Caramboxin affects the nervous system."),
        ("Kamias is a risk because it is rich in:",
         ["Potassium", "Oxalate", "Protein", "Sugar"], 1,
         "Case reports describe acute oxalate kidney injury after kamias juice."),
        ("Noni juice is a problem in CKD mainly because of its high:",
         ["Protein", "Potassium", "Calcium", "Iron"], 1,
         "It can raise serum potassium."),
        ("Which item belongs in the &ldquo;duplicate&rdquo; group?",
         ["A prescribed renal vitamin", "Calcium in both a binder and an over-the-counter supplement", "A single herbal tea", "Water"], 1,
         "The same ingredient in two products."),
        ("Who stops a prescribed medicine?",
         ["The dietitian", "The prescriber", "The patient&rsquo;s son", "The pharmacist alone"], 1,
         "The dietitian reports; the prescriber decides."),
        ("KDOQI considers supplementing water-soluble vitamins reasonable in:",
         ["All healthy adults", "Patients with poor intake or on dialysis", "No one", "Only children"], 1,
         "Expert opinion in KDOQI 2020."),
        ("The evidence on star fruit poisoning comes mainly from:",
         ["Large randomized trials", "Case reports and case series", "Animal studies only", "No evidence"], 1,
         "Case reports show the harm, not how common it is."),
        ("A &ldquo;kidney detox&rdquo; tea:",
         ["Cleans the kidneys", "Has no proven benefit and may contain harmful substances", "Replaces dialysis", "Is always safe"], 1,
         "No product cleanses the kidneys."),
        ("The best response to a patient&rsquo;s remedy is:",
         ["Mock it", "Explain the risk, and offer something helpful instead", "Ignore it", "Approve it"], 1,
         "Respect, explain, redirect."),
    ],
    "terms": [("Aristolochic acid", "A plant toxin that causes kidney failure and cancer."),
              ("Balimbing", "Star fruit, <em>Averrhoa carambola</em>."),
              ("Noni", "<em>Morinda citrifolia</em>, a fruit sold as juice; very high in potassium."),
              ("Trace elements", "Minerals needed in tiny amounts, such as zinc and selenium."),
              ("Renal vitamin", "A multivitamin designed for kidney failure.")],
    "readings": [("calcium-iron-vitamin-e-safety.html", "Supplement safety in kidney disease."),
                 ("food-kidney-toxins.html", "Foods that can harm the kidneys."),
                 ("vitamin-b1-niacin-kidney-care.html", "Thiamine and niacin in kidney care.")],
    "calcs": ["calc-renal-med-safety.html", "calc-drug-interaction-checker.html", "calc-vitamin-d-dose.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
