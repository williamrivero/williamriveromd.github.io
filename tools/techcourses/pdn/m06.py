# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 6: Medication safety. POD voice. Fictional cases. No pediatric doses are stated."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain why weight-based and body-surface-area dosing creates ten-fold errors, and the habits that prevent them.",
        "Predict which drugs dialysis is likely to remove from the drug&rsquo;s size, protein binding and distribution.",
        "Verify a pediatric dose against weight, units and concentration with an independent double check.",
        "Time and document medicines around dialysis sessions as ordered, and report missed or vomited doses.",
    ],
    "big": """
<p>Almost every medicine a child receives is calculated, not chosen from a fixed tablet. The dose depends on weight or body surface area, the liquid comes in a concentration, and the volume is measured in a syringe. Each step is a chance to move a decimal point. A ten-fold error in an adult dose may be noticed; in a child it may be the entire difference between a dose and an overdose.</p>
<p>Your work in this module is not to choose doses. The pediatric nephrologist and pharmacist do that. Your work is to make sure the dose the child receives is the dose that was ordered, at the right time relative to dialysis.</p>
{{plain:Think of a dose as a sentence with three words: an amount, a unit and a concentration. Change any word, and the sentence means something else. &ldquo;Five&rdquo; means nothing until you know &ldquo;five milligrams&rdquo; and &ldquo;in one milliliter&rdquo;.}}
<p>The picture has a limit. Even a perfectly checked sentence can be wrong for the child if the kidney and the dialysis change how long the drug stays in the body. That is the prescriber&rsquo;s and pharmacist&rsquo;s reasoning, but you are the one who sees the child sleepy after a dose or vomiting it back. Report what you see.</p>
{{cards:Key terms for this module|Ten-fold error::A dose ten times too large or too small, usually from a misplaced decimal or a zero.|Concentration::Amount of drug per volume, for example mg per mL.|Protein binding::The share of a drug attached to blood proteins; bound drug is poorly dialyzed.|Volume of distribution::How widely a drug spreads through body tissues; wide spread means little is in the blood for dialysis to remove.|Independent double check::Two people calculating separately and comparing.}}
""",
    "case": {"title": "Point five or five", "html": """
<p><strong>Ella Navarro, 4</strong>, weighs 15 kilograms and is on hemodialysis three times a week. Her new order for an oral medicine reads &ldquo;.5 mL&rdquo;. The bottle&rsquo;s concentration differs from the one the family used last month. Her mother says Ella usually gets her morning medicines &ldquo;before the machine&rdquo;. <strong>Nurse Dani</strong> prepares the dose.</p>
""", "questions": ["What is unsafe about the order as written?",
                  "How should Dani verify the dose?",
                  "Should the medicine be given before or after dialysis?"]},
    "sections": [
        ("ten-fold-errors", "Ten-fold errors", "Where ten-fold errors come from", """
<p>Pediatric doses travel through many hands: prescriber, pharmacist, nurse, caregiver. Errors cluster at the steps where a number is converted or copied.</p>
{{fig:pdn06_a}}
<div class="table-wrap"><table>
<thead><tr><th>Error source</th><th>Example</th><th>Prevention</th></tr></thead>
<tbody>
<tr><td>Naked decimal</td><td>&ldquo;.5 mL&rdquo; read as &ldquo;5 mL&rdquo;</td><td>Always a leading zero: 0.5 mL</td></tr>
<tr><td>Trailing zero</td><td>&ldquo;5.0 mg&rdquo; read as &ldquo;50 mg&rdquo;</td><td>Never a trailing zero: 5 mg</td></tr>
<tr><td>Unit confusion</td><td>mg versus mcg; mL versus mg</td><td>Write units in full where confusion is possible; order in mg, give in mL with the concentration stated</td></tr>
<tr><td>Changed concentration</td><td>A new brand or a compounded liquid</td><td>Recalculate the volume each time the bottle changes</td></tr>
<tr><td>Outdated weight</td><td>Dose based on last year&rsquo;s weight</td><td>Confirm the weight used and when it was measured</td></tr>
</tbody></table></div>
{{key:Leading zero always, trailing zero never, and recalculate every time the bottle changes.}}
"""),
        ("what-dialysis-removes", "Removal", "What dialysis removes", """
<p>Dialysis removes drugs by the same physics that removes urea. A drug is likely to be removed when it is small, water-soluble, little bound to protein and mostly in the blood rather than the tissues. A drug that is large, highly protein-bound or widely distributed in tissues is removed little.</p>
<div class="table-wrap"><table>
<thead><tr><th>Drug property</th><th>Effect on removal by dialysis</th><th>Practical consequence</th></tr></thead>
<tbody>
<tr><td>Small molecule, water-soluble</td><td>More removed</td><td>Often given after the session; a supplemental dose may be ordered</td></tr>
<tr><td>Highly protein-bound</td><td>Less removed</td><td>Timing around dialysis matters less</td></tr>
<tr><td>Large volume of distribution</td><td>Little in the blood to remove</td><td>Dialysis does not clear an overdose well</td></tr>
<tr><td>High-flux dialyzer or longer session</td><td>More removed than older low-flux dialysis</td><td>Older dosing references may underestimate loss</td></tr>
</tbody></table></div>
<p>In PD, removal is slower and continuous, and some drugs are added to the dialysate on purpose, such as intraperitoneal antibiotics for peritonitis (Module 11). For timing, follow the order. When an order says &ldquo;after dialysis&rdquo; and the family gives it before, the child may lose part of the dose to the dialyzer. Ask the family what they actually do at home.</p>
{{key:Small, water-soluble, unbound drugs are dialyzed. When the order says after dialysis, it means after.}}
"""),
        ("the-checked-dose", "Checked dose", "The checked dose", """
<p>For high-alert medicines and for every calculated pediatric dose your unit lists, use an independent double check.</p>
{{fig:pdn06_b}}
{{formula:Volume to give (mL) = ordered dose (mg) &divide; concentration (mg/mL)<br>Check the dose per kg: ordered dose (mg) &divide; weight (kg) = mg/kg, compare with the order or pharmacy reference<br>Example arithmetic only: 30 mg ordered, liquid 10 mg/mL &rarr; 3 mL; 30 mg &divide; 15 kg = 2 mg/kg}}
<p>That example verifies arithmetic. It does not say 2 mg/kg is a right dose for any drug. If the per-kilogram dose differs from the order or the pharmacy label, stop and ask the prescriber or pharmacist. Body-surface-area doses use square meters; check which basis the order uses before you compare.</p>
<p>Give oral liquids with an oral syringe, never an injection syringe that could be connected to a line. Record vomiting within the time your unit specifies and ask whether to repeat; do not repeat a dose on your own.</p>
{{scene:Dani and the &ldquo;.5&rdquo;|<p>Dani will not give a dose written as &ldquo;.5 mL&rdquo; with a new concentration. She asks for the order in milligrams, checks Ella&rsquo;s weight from today, calculates the volume from the new bottle, and asks a colleague to calculate separately. The two answers match the pharmacist&rsquo;s label. The order says &ldquo;after dialysis&rdquo;, so she gives it after the session and teaches Ella&rsquo;s mother the change.</p><p class="tc-scene-take">Ask for the dose in milligrams, calculate from the bottle in your hand, and match the timing to the order.</p>}}
{{key:Dose in milligrams, volume from the bottle in your hand, a second person calculating blind, and timing from the order.}}
"""),
    ],
    "debrief": ["""
<p><strong>Unsafe order.</strong> A naked decimal (&ldquo;.5&rdquo;), a volume without a milligram dose, and a changed concentration together make a ten-fold error likely.</p>
<p><strong>Verification.</strong> Order in milligrams with a leading zero; today&rsquo;s weight; volume calculated from the new bottle; independent double check; comparison with the pharmacist&rsquo;s label.</p>
<p><strong>Timing.</strong> As ordered. If the order says after dialysis, give it after and teach the family why; if the order is silent, ask.</p>
"""],
    "skills": {"title": "Medication verification", "intro": "Use fictional orders and training liquids.",
               "items": [("Rejects an order with a naked decimal or trailing zero and requests correction", True),
                         ("Calculates volume from the dose and the concentration in hand", True),
                         ("Performs an independent double check for a calculated pediatric dose", True),
                         ("States whether a drug is likely to be dialyzed from its properties", False),
                         ("Gives an oral liquid with an oral syringe and documents vomiting and the follow-up decision", False)]},
    "quiz": [
        ('How should half a milliliter be written?',
         ['.5 mL', '0.50 mL', '0.5 mL', '1/2'], 2,
         'A leading zero prevents a ten-fold error.'),
        ('Why avoid &ldquo;5.0 mg&rdquo;?',
         ['It is too precise', 'It is illegal', 'It wastes ink', 'The decimal can be missed and read as 50 mg'], 3,
         'Never a trailing zero.'),
        ('The liquid&rsquo;s concentration changed. You should:',
         ['Recalculate the volume from the new concentration', 'Give the same mL as before', 'Halve the dose', 'Ask the parent'], 0,
         'Same mg can mean a different mL.'),
        ('Which drug is most likely removed by dialysis?',
         ['Large, protein-bound, widely distributed', 'Small, water-soluble, little protein binding', 'Any drug', 'Only antibiotics'], 1,
         'It behaves like urea.'),
        ('A drug with a very large volume of distribution:',
         ['Is removed easily', 'Is never used in children', 'Has little in the blood for dialysis to remove', 'Dissolves in dialysate'], 2,
         'Dialysis treats such overdoses poorly.'),
        ('Order says &ldquo;after dialysis&rdquo;; family gives it before. Risk?',
         ['None', 'Overdose', 'Allergy', 'Part of the dose may be removed by the dialyzer'], 3,
         'Ask what actually happens at home.'),
        ('30 mg ordered; liquid 10 mg/mL. Volume?',
         ['3 mL', '0.3 mL', '30 mL', '300 mL'], 0,
         '30 &divide; 10 = 3 mL.'),
        ('30 mg for a 15-kg child is:',
         ['0.5 mg/kg', '2 mg/kg', '45 mg/kg', '15 mg/kg'], 1,
         '30 &divide; 15 = 2 mg/kg. Arithmetic only; not a dose recommendation.'),
        ('Your mg/kg check does not match the order. Next step?',
         ['Give it', 'Round it', 'Stop and ask the prescriber or pharmacist', 'Ask the parent'], 2,
         'The nurse verifies; the prescriber decides.'),
        ('Why use an oral syringe for liquids?',
         ['Cheaper', 'More accurate always', 'Children prefer it', 'It cannot be connected to an intravenous line'], 3,
         'It prevents wrong-route errors.'),
        ('A child vomits soon after a dose. You:',
         ['Record it and ask whether to repeat', 'Repeat immediately', 'Ignore it', 'Double the next dose'], 0,
         'Never repeat on your own.'),
        ('Who chooses the dose of a pediatric medicine?',
         ['The nurse', 'The prescriber, checked by the pharmacist', 'The parent', 'The dialysis technician'], 1,
         'The nurse makes sure the ordered dose is given.'),
        ('High-flux dialyzers compared with older low-flux dialysis:',
         ['Remove less drug', 'Remove none', 'May remove more drug', 'Only remove potassium'], 2,
         'Older references may underestimate removal.'),
        ('Which is an independent double check?',
         ['Reading your colleague&rsquo;s answer', 'Asking the parent', 'Checking twice yourself', 'Two people calculating separately, then comparing'], 3,
         'Separate calculation avoids anchoring.'),
        ('What weight should a dose use?',
         ['A recent, documented weight confirmed with the order', 'Last year&rsquo;s', 'An estimate', 'The target weight always'], 0,
         'Children grow; confirm the weight and its date.'),
    ],
    "terms": [("Ten-fold error", "A dose ten times too large or small."),
              ("Concentration", "Amount of drug per volume, such as mg per mL."),
              ("Protein binding", "The share of drug bound to blood proteins; bound drug is poorly dialyzed."),
              ("Volume of distribution", "How widely a drug spreads into tissues."),
              ("Oral syringe", "A syringe designed only for mouth doses that cannot connect to an intravenous line."),
              ("High-alert medicine", "A drug with a high risk of serious harm when given in error.")],
    "readings": [("medicines-and-your-kidneys.html", "How kidneys handle medicines."),
                 ("antibiotic-stewardship-dialysis.html", "Antibiotic stewardship in dialysis.")],
    "calcs": ["calc-bsa.html", "calc-pediatric-dialysis-nurse-toolkit.html"],
}
