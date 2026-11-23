# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 15: Counseling and Filipino Food Skills. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian and a mother measuring fish sauce with a spoon over a pot of tinola in a home kitchen.",
    "objectives": [
        "Use an elicit, offer, check sequence to agree on one change the patient chooses.",
        "Use teach-back to confirm that advice was understood.",
        "Adapt teaching for low health literacy, language, and numeracy.",
        "Calculate nutrients in a household recipe per serving, and say where the estimate may be wrong.",
        "Use the Philippine Food Exchange Lists and the Pinggang Pinoy plate to build meals.",
        "Plan for a tight budget and for fiestas without abandoning the plan.",
    ],
    "big": """
{{plain:Counseling is not pouring information into a bucket. It is helping someone carry one bucket at a time up a hill they already know. Ask what they already carry, offer one change that fits, and check that they can lift it. Five changes at once spill on the first step.}}
{{cards:Key terms for this module|Elicit, offer, check::Ask what the person knows and wants, offer information or options with permission, then check what they make of it.|Teach-back::Asking the patient to explain or show, in their own words, what they will do.|Health literacy::The ability to find, understand, and use health information.|Food exchange::A portion of food with a set amount of energy, protein, carbohydrate, and fat, from the Philippine Food Exchange Lists.|Pinggang Pinoy::The Filipino healthy plate: half vegetables and fruits, a quarter rice or other energy food, a quarter fish, meat, or other protein food.|Recipe yield::How many servings a pot makes.}}
{{flow:One counseling visit|Elicit::&ldquo;What have you been told about your diet? What is hardest?&rdquo;|Offer::&ldquo;May I share two options?&rdquo;|Choose::The patient picks one change.|Teach-back::&ldquo;Show me how you will measure it.&rdquo;|Plan::When, a fallback, and a check-in date.}}
""",
    "case": {"title": "Tinola for four", "html": """
<p>Aling Rosa, 60, cooks for her family of four. Her husband, Mang Pedro, is on hemodialysis. She makes tinola twice a week: chicken, green papaya, malunggay, ginger, one bouillon cube, and patis.</p>
<p>The bouillon cube (fictional label) contains 1,200 mg of sodium, and the patis she adds contains about 600 mg. The pot makes four equal servings. Mang Pedro usually takes an extra half bowl of broth. She says she cannot cook separately for him and that the family will complain if the tinola tastes &ldquo;bland.&rdquo; Money is tight.</p>
""", "questions": ["How much sodium from the cube and patis is in one serving, and in Mang Pedro&rsquo;s serving?",
                  "Why is your estimate uncertain?",
                  "What change might she accept, and how will you check that she understood?"]},
    "sections": [
        ("counsel", "Counseling", "Elicit, offer, check", """
<p>Advice that ignores what the patient already knows, believes, and can afford rarely survives the trip home. Start by asking. &ldquo;What have you been told about food since dialysis started?&rdquo; &ldquo;What is the hardest part?&rdquo; &ldquo;Who cooks? Who shops? How much is the food budget?&rdquo; Listen for mistaken rules, as these are common, and for what the person cares about.</p>
<p>Then ask permission before offering: &ldquo;May I share two ideas?&rdquo; Offer options, not orders. Let the patient choose one. A change chosen by the patient is more likely to happen than a change chosen for them. Agree on when it starts, what happens if it fails (a fallback), and when you will check.</p>
<p>The Academy of Nutrition and Dietetics and National Kidney Foundation standards place this kind of patient-centered counseling, with documented goals and follow-up, at the center of competent renal practice.[[pace2021]]</p>
{{key:One change the patient chose, done well, is worth more than ten changes you listed.}}
"""),
        ("literacy", "Being understood", "Teach-back, language, and numbers", """
<p>Many patients nod when they do not understand, out of respect or embarrassment. Teach-back checks your teaching, not the patient. Say: &ldquo;I want to be sure I explained this clearly. Can you show me how you will measure the patis tomorrow?&rdquo; If the answer is wrong, explain again, differently, and ask again.</p>
{{cards:Making advice usable|Use the patient&rsquo;s language::Tagalog, Cebuano, Kapampangan, or other; use an interpreter or a family member the patient chooses.|Use objects, not numbers::A teaspoon, a matchbox-size piece of fish, a marked cup of rice.|Show, do not only tell::Measure the patis together; read a label together.|Keep it short::Two or three points per visit, written in large print or as pictures.|Involve the cook::The person who cooks often needs the teaching more than the patient.}}
<p>Numbers are hard for many people. &ldquo;Less than 2,000 mg of sodium&rdquo; means little to most patients. &ldquo;One level teaspoon of salt for the whole day, from everything&rdquo; is clearer. &ldquo;Two matchbox pieces of fish at lunch&rdquo; is clearer than &ldquo;20 g of protein.&rdquo;</p>
"""),
        ("recipe", "Recipe arithmetic", "Calculate a household recipe", """
<p>Patients eat dishes, not nutrients. To estimate the sodium, potassium, or protein in a dish:</p>
{{flow:Recipe calculation|List::Every ingredient that adds the nutrient, with amounts.|Find values::From the label, or the Philippine Food Composition Tables for the raw or cooked form used.|Add::The total for the pot.|Divide::By the number of equal servings.|Adjust::For the actual portion, extra broth, and table condiments.|State the uncertainty::What you assumed and could not measure.}}
{{formula:Sodium per serving = (cube 1,200 mg + patis 600 mg) &divide; 4 servings = 450 mg. Mang Pedro&rsquo;s serving with an extra half bowl of broth = about 450 &times; 1.5 = 675 mg, if the sodium is spread evenly in the broth.}}
<p>The estimate is uncertain for several reasons. Sodium dissolves into the broth, so a serving heavy in broth carries more than one heavy in chicken. Servings are rarely equal. The chicken and vegetables add some sodium of their own. Patis at the table is not counted. Write down what you assumed. Use the Philippine Food Composition Tables (PhilFCT) for ingredient values and record the source and date.[[philfct]] The site&rsquo;s recipe analyzer and label scanner can help with the arithmetic. The Philippine Society of Nephrology also publishes patient nutrition materials you can use alongside your own.[[psn_nutrition]]</p>
{{fig:rd15_recipe}}
"""),
        ("meals", "Building meals", "Exchanges, the plate, budgets, and fiestas", """
<p><strong>Food exchanges.</strong> The Philippine Food Exchange Lists group foods by portions with similar energy and nutrients. One meat exchange, for example, is a portion of fish, chicken, or meat with about 8 g of protein.[[fel2019]] Exchanges let you turn a protein target into portions: 60 g of protein a day is roughly five to six meat exchanges plus the protein in rice and vegetables. They are approximate. Check sodium, potassium, and phosphorus separately, because the exchange lists were not designed for kidney disease.</p>
<p><strong>The plate.</strong> Pinggang Pinoy shows a healthy Filipino plate: half vegetables and fruits, a quarter rice or other energy food, a quarter protein food.[[pinggang]] For energy and nutrient needs of healthy Filipinos, the reference is the Philippine Dietary Reference Intakes.[[pdri2015]] The plate is a good starting picture for CKD stages 1 to 3, with portions adjusted for the patient&rsquo;s protein target and potassium.</p>
<p><strong>A tight budget.</strong> Eggs, tofu, monggo, and small fish are affordable protein. Rice and root crops supply cheap energy. Frozen and canned foods vary; read the sodium. Buy in season. Ask what the family already buys before suggesting anything new.</p>
<p><strong>Fiestas and holidays.</strong> Banning party food fails. Plan it: a smaller plate, fresh-served food rather than leftovers, the patient&rsquo;s favorite dish in a measured portion, broth and sawsawan left out, binders taken with the meal, and less salt in the meals before and after. Patients on dialysis should not skip a session for a party.</p>
{{fig:rd15_plate}}
"""),
    ],
    "debrief": ["""
<p><strong>How much sodium?</strong> (1,200 + 600) &divide; 4 = 450 mg per equal serving from the cube and patis. With an extra half bowl of broth, Mang Pedro gets about 675 mg from those two seasonings alone. On a 2,000 mg day, that is a third of his allowance in one bowl.</p>
<p><strong>Why is it uncertain?</strong> Servings are not exactly equal, sodium sits mostly in the broth, the chicken adds some sodium of its own, and any patis at the table is not counted. Say this when you write it down.</p>
<p><strong>What might she accept?</strong> Ask her first what she thinks would work. Options to offer: use half a bouillon cube and add more ginger, onion, and garlic; add the patis at the table for the rest of the family and not to the pot; give Mang Pedro his serving before adding extra broth. Let her choose one. She keeps cooking one pot for everyone, and the family adds seasoning at the table.</p>
<p><strong>How will you check?</strong> Teach-back: &ldquo;Show me how much cube you will use next time.&rdquo; Then a call or visit in a week: did the family accept it, did it cost more, did Mang Pedro&rsquo;s weight gain change? The cook is often the real patient in a counseling visit. Teaching her well may do more than any diet sheet.</p>
"""],
    "skills": {"title": "Counseling with recipe calculation and teach-back",
               "intro": "The preceptor plays a family cook. Materials: a household recipe, two labels, measuring spoons.",
               "items": [
                   ("Opens by asking what the person knows, what is hardest, and who cooks and shops.", False),
                   ("Asks permission before offering options and offers at least two.", False),
                   ("Lets the person choose one change and agrees on timing, a fallback, and follow-up.", False),
                   ("Calculates a nutrient per serving from a recipe and adjusts for the actual portion.", False),
                   ("States the assumptions and uncertainty in the estimate.", False),
                   ("Uses household measures and objects instead of numbers.", False),
                   ("Uses teach-back and re-explains if needed.", True),
                   ("Documents the goal, the change chosen, and the follow-up date.", False),
               ],
               "placement": "Calculate sodium per serving for three dishes your patients commonly cook, using real labels and PhilFCT values."},
    "quiz": [
        ("A bouillon cube has 1,200 mg sodium and patis adds 600 mg; the pot makes four servings. Sodium per serving from these is:",
         ["300 mg", "450 mg", "600 mg", "1,800 mg"], 1,
         "1,800 ÷ 4 = 450 mg."),
        ("With an extra half bowl of broth, the serving rises to about:",
         ["450 mg", "675 mg", "900 mg", "1,800 mg"], 1,
         "450 × 1.5 = 675 mg, assuming even distribution."),
        ("Which makes a recipe estimate less certain?",
         ["Measured spoons", "Uneven servings and extra broth", "Writing the date", "Using the label"], 1,
         "Sodium follows the broth."),
        ("Which question is teach-back?",
         ["&ldquo;You understand, right?&rdquo;", "&ldquo;Any questions?&rdquo;", "&ldquo;Show me how you will measure the patis tomorrow.&rdquo;", "&ldquo;Was this helpful?&rdquo;"], 2,
         "The patient demonstrates the plan."),
        ("Teach-back checks:",
         ["The patient&rsquo;s intelligence", "Whether the explanation was clear", "Laboratory results", "The recipe"], 1,
         "It tests the teaching."),
        ("In elicit, offer, check, the step before offering is:",
         ["Lecturing", "Asking what the person knows and wants", "Giving a handout", "Weighing"], 1,
         "Start with the person&rsquo;s view."),
        ("Why let the patient choose the change?",
         ["It saves time", "A self-chosen change is more likely to happen", "It is required", "It does not matter"], 1,
         "Ownership supports action."),
        ("&ldquo;Less than 2,000 mg of sodium&rdquo; is clearer to most patients as:",
         ["90 mmol", "One level teaspoon of salt for the whole day, from everything", "5 g of sodium", "No salt"], 1,
         "Household measures beat numbers."),
        ("One meat exchange provides about:",
         ["2 g of protein", "8 g of protein", "20 g of protein", "No protein"], 1,
         "From the Philippine Food Exchange Lists."),
        ("Pinggang Pinoy fills half the plate with:",
         ["Rice", "Vegetables and fruits", "Meat", "Noodles"], 1,
         "Half vegetables and fruits, a quarter energy food, a quarter protein."),
        ("Why check potassium and phosphorus separately when using exchanges?",
         ["Exchanges list them precisely", "Exchange lists were not designed for kidney disease", "They do not matter", "Exchanges only cover fat"], 1,
         "Use PhilFCT and labels for these."),
        ("Which is affordable protein?",
         ["Imported steak", "Eggs, tofu, monggo, small fish", "Protein bars", "Cheese"], 1,
         "Local staples serve the budget."),
        ("For a fiesta, the best approach is:",
         ["Ban all party food", "Plan portions, leave out broth and sawsawan, take binders, and keep dialysis", "Skip dialysis", "Eat only rice"], 1,
         "Planning works better than banning."),
        ("Who often needs the teaching most?",
         ["The neighbor", "The person who cooks", "The driver", "No one"], 1,
         "The cook decides what is served."),
        ("When a patient&rsquo;s first language is Kapampangan, you should:",
         ["Teach in English only", "Use Kapampangan, an interpreter, or a family member the patient chooses", "Skip teaching", "Give a handout only"], 1,
         "Use the patient&rsquo;s language."),
    ],
    "terms": [("Fallback", "What the patient will do if the main plan cannot be followed that day."),
              ("Numeracy", "The ability to use numbers in daily life."),
              ("Tinola", "Chicken soup with ginger, green papaya or chayote, and leaves."),
              ("Aling and Mang", "Respectful titles for an older woman and man."),
              ("PhilFCT", "Philippine Food Composition Tables.")],
    "readings": [("ckd-friendly-recipes.html", "Kidney-friendly Filipino recipes."),
                 ("ckd-recipe-analyzer.html", "Recipe nutrient analysis tool."),
                 ("nutrition-labels-ckd.html", "Reading labels in kidney disease."),
                 ("meal-prep-fastfood-ckd.html", "Meal prep and fast food choices.")],
    "calcs": ["calc-sodium-intake.html", "calc-potassium-load.html", "calc-phosphorus-load.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
