# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 17: Growth, nutrition, anemia and bone. POD voice. Fictional cases. No doses."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Measure and plot growth accurately and recognize growth failure that needs referral.",
        "Explain why children on dialysis struggle to grow and gain weight, including dialysate protein losses.",
        "Support the renal dietitian&rsquo;s feeding plan at the chair and at home, including tube feeding.",
        "Recognize the signs of anemia and bone-mineral disorder in a child and report them.",
    ],
    "big": """
<p>For an adult on dialysis, success is staying well. For a child, success also means growing. Growth failure is one of the hardest problems in pediatric CKD, and it does not repair itself: height lost in childhood is often not regained. Growth is therefore an outcome in its own right, measured at every visit and plotted on a chart.</p>
<p>Your work in this module is to measure accurately, plot honestly, reinforce the feeding plan, and notice when anemia or bone disease is holding a child back.</p>
{{plain:Think of growth as building a house on a tight budget. Energy and protein are the bricks, the hormones are the builders, and healthy bone is the frame. CKD cuts the budget, slows the builders and weakens the frame at the same time.}}
<p>The picture has a limit. More bricks do not always build a better house. Feeding a child more calories without enough protein, or without controlling phosphate and acid, adds fat rather than height, and some children on tube feeds become overweight. Growth needs the whole plan, which is why a renal dietitian leads it.</p>
{{cards:Key terms for this module|Height velocity::How fast a child grows in height, in cm per year.|Percentile and standard deviation score::Where a child&rsquo;s height sits compared with healthy children.|Gastrostomy feeding::Feeding through a tube into the stomach.|Recombinant growth hormone::A manufactured hormone given by injection to some children with growth failure.|CKD-mineral and bone disorder::Disturbed calcium, phosphate, parathyroid hormone and vitamin D affecting bone and vessels.}}
""",
    "case": {"title": "The same trousers for two years", "html": """
<p><strong>Rafael Cruz, 7</strong>, has been on PD for two years. His mother jokes that he still fits the trousers he wore when he started. On the clinic stadiometer he measures 112 cm; the chart shows his height below the 3rd percentile and his height velocity below the 25th percentile for the past year. His appetite is poor, and he often refuses the evening feed. <strong>Nurse Cathy</strong> plots the numbers.</p>
""", "questions": ["Is this growth failure, and what should Cathy check before calling it?",
                  "Who decides on growth hormone, and on what criteria?",
                  "What can Cathy do about the feeding?"]},
    "sections": [
        ("growth-is-an-outcome", "Growth", "Growth is an outcome", """
<p>Measure the same way every time (Module 4), plot on the reference chart your unit uses, and look at the line, not one point. Two numbers matter most: height for age and height velocity.</p>
{{fig:pdn17_a}}
<p>The European Society for Paediatric Nephrology clinical practice recommendations state that children with CKD stages 3 to 5 or on dialysis should be candidates for growth hormone if they have persistent growth failure, defined as height below the 3rd percentile for age and sex and height velocity below the 25th percentile, once other treatable causes have been addressed and the child still has growth potential.[[pdn_drube2019]] The treatable causes include poor intake, acidosis, bone-mineral disorder and anemia. The decision belongs to the pediatric nephrologist; your accurate measurements are its evidence.</p>
<p>Nutrition problems in children on PD are common and vary by region. In the IPPN registry of 1,001 children from 35 countries, 8.9% were underweight and 19.7% overweight or obese at the start of PD; underweight was most prevalent in South and Southeast Asia (20%).[[pdn_schaefer2019]]</p>
{{key:Measure carefully, plot every time, and report when the line falls away. Height lost in childhood is hard to regain.}}
"""),
        ("feeding-the-child", "Feeding", "Feeding the child", """
<p>Children on dialysis often eat poorly: uremia dulls appetite, PD fluid fills the abdomen and absorbs glucose, medicines taste bad, and infants may vomit. PD also removes protein into the dialysate. The Pediatric Renal Nutrition Taskforce (PRNT) recommendations address energy needs in poor growth and obesity, the extra protein needed to replace dialysate losses, and how to deliver the plan with breast milk, formula, food and supplements.[[pdn_shaw2020]] Many of their statements carry low grades or rest on opinion and must be adapted by the treating physician and dietitian.</p>
{{fig:pdn17_b}}
<div class="table-wrap"><table>
<thead><tr><th>Nurse&rsquo;s task</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Weigh and measure accurately</td><td>The dietitian&rsquo;s plan depends on it</td></tr>
<tr><td>Ask what the child actually ate and kept down</td><td>Prescribed feeds and delivered feeds often differ</td></tr>
<tr><td>Check gastrostomy sites and tube function</td><td>Feeds stop when tubes block or sites become sore</td></tr>
<tr><td>Reinforce the plan in the family&rsquo;s food culture</td><td>Rice, soups and snacks are part of Filipino meals; advice must fit them</td></tr>
<tr><td>Report vomiting, refusal and weight change</td><td>The plan may need changing</td></tr>
</tbody></table></div>
{{key:The renal dietitian writes the plan; the nurse measures what was actually eaten and reports the gap.}}
"""),
        ("anemia-and-bone", "Anemia and bone", "Anemia and bone", """
<p>Anemia in CKD comes mainly from too little erythropoietin and from iron deficiency, worsened by blood losses from sampling and circuits. In a child it shows as pallor, tiredness, poor school stamina and breathlessness on play. Treatment with erythropoiesis-stimulating agents and iron follows the pediatric nephrologist&rsquo;s orders.</p>
<p>CKD-mineral and bone disorder begins early in childhood CKD: phosphate rises, active vitamin D falls, parathyroid hormone rises, and growing bones deform or fracture. Signs include bone pain, limping, bowed legs or knock knees, and slow growth. Phosphate binders must be taken with meals to work, which is hard for children who graze or refuse food; ask how they are taken.</p>
<p>Minimize blood sampling to what is ordered and record volumes (Module 13). A growing child&rsquo;s blood volume is small, and avoidable losses worsen anemia.</p>
{{key:Pale and tired, limping or bowing: report it. Binders work only with food; ask how the child takes them.}}
"""),
    ],
    "debrief": ["""
<p><strong>Growth failure?</strong> Height below the 3rd percentile and height velocity below the 25th percentile over a year fit the ESPN definition. Cathy first confirms the measurement technique and plotting, then reports.</p>
<p><strong>Growth hormone.</strong> The pediatric nephrologist decides, after addressing treatable causes such as intake, acidosis, bone disease and anemia, and if Rafael still has growth potential.</p>
<p><strong>Feeding.</strong> Cathy records what he actually eats and refuses, asks whether the evening feed coincides with a full abdomen after a PD fill, and refers to the renal dietitian for a revised plan that fits the family&rsquo;s meals.</p>
"""],
    "skills": {"title": "Growth and nutrition at the chair", "intro": "Use growth charts and fictional records.",
               "items": [("Measures height with a stadiometer or length board to standard technique", True),
                         ("Plots height and calculates height velocity on the unit&rsquo;s chart", True),
                         ("Records actual intake versus prescribed feeds for three days", False),
                         ("Checks a gastrostomy site and tube function", False),
                         ("Reports growth failure, anemia signs or bone signs with measurements", False)]},
    "quiz": [
        ('Why is growth an outcome in pediatric dialysis?',
         ['It is not', 'Height lost in childhood is often not regained', 'For school photos', 'It affects dialysis dose only'], 1,
         'Growth failure persists.'),
        ('Growth hormone candidacy per ESPN recommendations includes height below which percentile?',
         ['25th', '50th', '3rd', '75th'], 2,
         'With height velocity below the 25th percentile.'),
        ('Before growth hormone, the team first addresses:',
         ['Nothing', 'School grades', 'Sleep only', 'Intake, acidosis, bone-mineral disorder and anemia'], 3,
         'Treatable causes come first.'),
        ('Who decides on growth hormone?',
         ['The pediatric nephrologist', 'The nurse', 'The parent', 'The school'], 0,
         'The nurse supplies accurate measurements.'),
        ('In IPPN, underweight at PD start was most prevalent in:',
         ['The US', 'South and Southeast Asia (20%)', 'Northern Europe', 'Nowhere'], 1,
         'Relevant to Filipino children.'),
        ('Why do children on PD need extra protein?',
         ['They do not', 'For muscles only', 'PD removes protein into the dialysate', 'Glucose replaces protein'], 2,
         'PRNT addresses dialysate losses.'),
        ('PRNT recommendations with low grades should be:',
         ['Ignored', 'Applied strictly', 'Used by parents alone', 'Adapted to the child by the physician and dietitian'], 3,
         'Clinical judgment applies.'),
        ('Who writes the feeding plan?',
         ['The renal dietitian', 'The nurse', 'The pharmacist', 'The child'], 0,
         'The nurse measures and reports.'),
        ('A child refuses the evening feed after a PD fill. Possible reason?',
         ['Bad behavior', 'A full abdomen and glucose absorption reduce appetite', 'Laziness', 'No reason'], 1,
         'Report for plan adjustment.'),
        ('Main cause of anemia in CKD:',
         ['Too much iron', 'Vitamin C', 'Too little erythropoietin and iron deficiency', 'Dialysis water'], 2,
         'Plus blood losses.'),
        ('Signs of bone-mineral disorder in children:',
         ['Tall stature', 'Better appetite', 'None', 'Bone pain, limping, bowed legs, slow growth'], 3,
         'Growing bones deform.'),
        ('Phosphate binders work only when:',
         ['Taken with meals', 'Taken at bedtime', 'Taken on an empty stomach', 'Crushed in water'], 0,
         'They bind phosphate in food.'),
        ('Why minimize blood sampling?',
         ['Lab cost only', 'Small blood volume; losses worsen anemia', 'Children dislike needles only', 'No reason'], 1,
         'Record volumes.'),
        ('Height velocity is measured in:',
         ['kg per month', 'mm per day', 'cm per year', 'percentiles only'], 2,
         'Speed of growth.'),
        ('Tube-fed children on dialysis can become:',
         ['Only underweight', 'Taller automatically', 'Immune to CKD', 'Overweight if energy exceeds need'], 3,
         'Growth needs the whole plan.'),
    ],
    "terms": [("Height velocity", "Growth speed in cm per year."),
              ("Stadiometer", "A device for measuring standing height."),
              ("Growth hormone", "A manufactured hormone for some children with growth failure."),
              ("Gastrostomy", "A feeding tube through the abdominal wall into the stomach."),
              ("Phosphate binder", "A medicine taken with food to reduce phosphate absorption."),
              ("CKD-mineral and bone disorder", "Disturbed calcium, phosphate, hormone and bone metabolism in CKD.")],
    "readings": [("eating-on-dialysis.html", "Eating on dialysis."),
                 ("anemia-management.html", "Anemia in kidney disease."),
                 ("nutrition-kidney-patients.html", "Nutrition for kidney patients.")],
    "calcs": ["calc-pediatric-growth-percentiles.html", "calc-pediatric-bmi-zscore.html", "calc-pediatric-calcium.html"],
}
