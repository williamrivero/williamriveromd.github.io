# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 09: Transport, Work, Housing, Food, and Disability Access. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient arriving by tricycle at a dialysis unit entrance early in the morning, a social worker greeting him.",
    "objectives": [
        "Calculate the full cost of getting to dialysis each month, including the companion and lost wages, and compare it with confirmed support.",
        "Estimate a household&rsquo;s health spending as a share of its total spending, and explain what the 10% and 25% marks mean.",
        "Explore work options with a patient: schedule changes, employer letters, leave and disability benefits, and new work that fits treatment.",
        "Screen for housing, water, and food problems that make treatment unsafe or impossible, and route them.",
        "Help a person apply for a PWD ID and its discounts where they qualify.",
    ],
    "big": """
{{plain:Getting to dialysis is a simple equation that families solve every week: fare out plus fare back, times two if someone has to come along, plus the meal on the way, plus the day of work the companion loses. Multiply by thirteen visits a month. When that number grows bigger than the household can pay, sessions start to disappear.}}
{{fig:sw09_access}}
<p>The picture has a limit. Families do not solve the equation once. A typhoon week, a sick companion, a fare increase, a lost job, or a move to a relative&rsquo;s house in another town changes it overnight. And the costs are not only money: a four-hour session plus two hours of travel, three times a week, takes about eighteen hours, the equivalent of two working days.</p>
<p>Your job in this module is to make these costs visible, early, and to work on them before they become missed sessions. The evidence shows why. In the international DOPPS cohort of 20,994 patients, longer self-reported travel time was associated with higher mortality and lower health-related quality of life (HR-QOL); the travel time was a single unvalidated question and many patients did not respond, so the finding is an association.[[sw_moist2008]] In 182,536 United States patients, transport problems and bad weather were among the reasons linked to missed treatments.[[chan2014]]</p>
{{cards:Key terms for this module|Access cost::Everything it costs to attend treatment beyond the treatment itself: fares, companion, food, lost income.|Confirmed support::Assistance that has been decided and will be paid; pending support does not count.|Health spending share::Out-of-pocket health spending divided by total household spending (or income).|SDG 3.8.2::The United Nations indicator that counts households spending more than 10% or 25% of their budget on health.|PWD ID::An identification card for persons with disability, which carries legal discounts.|Food insecurity::Not having reliable access to enough affordable, suitable food.}}
""",
    "case": {"title": "The tricycle fare and the 5 a.m. shift", "html": """
<p>Thursday, 6:15 a.m. Mr. Rodel Manalo, 51, arrives late for the 6:00 a.m. shift for the third time this month. He lives in a barangay 14 kilometers from the unit in Batangas. The jeepney does not run before 5:30 a.m., so he takes a special tricycle trip that costs PHP 250 each way. His wife comes with him because he is weak after dialysis; she loses her day at a carinderia, about PHP 400.</p>
<p>He used to drive a delivery truck; he lost the job two months after starting dialysis. The family of five now lives on his wife&rsquo;s earnings and a monthly remittance from his brother. He has not applied for a PWD ID. He says they eat rice and instant noodles most nights &ldquo;to save for the fare.&rdquo;</p>
<p>The charge nurse asks you to &ldquo;do something about his lateness&rdquo;; late starts are delaying the next shift.</p>
""", "questions": ["What does his attendance actually cost the household each month?",
                  "What options could reduce that cost or the lateness?",
                  "What else in his story needs a referral today?"]},
    "sections": [
        ("equation", "The access equation", "Count everything", """
<p>Count the full cost of one visit, then multiply by the visits in a month. Include what families usually forget: the return trip, the companion&rsquo;s fares, food, and the income the companion loses.</p>
{{formula:<strong>Worked example, illustrative.</strong> Gross = visits &times; (fare out + fare back + companion&rsquo;s fares + other per visit) + one-time costs. Gap = gross &minus; confirmed support.<br>Six visits &times; (PHP 120 + PHP 120 + PHP 0 + PHP 30) + PHP 300 one-time = 6 &times; 270 + 300 = PHP 1,920.<br>Confirmed support: PHP 1,000. Pending support: not subtracted.<br>Gap = 1,920 &minus; 1,000 = PHP 920.<br>What the number tells you: what the household must still find. What it does not tell you: whether they can. Compare it with their budget.}}
<p>The <a href="calc-social-worker-toolkit.html#tool-1">access cost tool</a> does this arithmetic for any schedule. Do it with the family, not for them; seeing the number together often changes the conversation from &ldquo;he is always late&rdquo; to &ldquo;this is what it costs.&rdquo;</p>
<p>Then put the number in context. The <a href="calc-social-worker-toolkit.html#tool-2">household spending share tool</a> divides out-of-pocket health spending by total household spending. The United Nations Sustainable Development Goal (SDG) indicator 3.8.2 tracks households whose health spending is more than 10% or more than 25% of their total spending or income. These marks describe financial hardship across populations; they are not eligibility rules for any Philippine program.</p>
{{formula:<strong>Worked example, illustrative.</strong> Share = out-of-pocket health spending &divide; total household spending &times; 100.<br>Health spending this month (fares, companion, medicines, food on dialysis days): PHP 4,000. Total household spending: PHP 25,000.<br>Share = 4,000 &divide; 25,000 &times; 100 = 16%. Above the 10% mark, below 25%.<br>What the number tells you: kidney care is taking a large bite of this budget. What it does not tell you: what the family is giving up to pay it. Ask.}}
{{key:Count the companion, the food, and the lost wages. Show the family the number, and compare it with what they actually have.}}
"""),
        ("work", "Work and income", "Keeping a livelihood alongside treatment", """
<p>Losing work is one of the biggest shocks of kidney failure, and it compounds every other cost. Many people stop working when dialysis starts, sometimes because of illness, often because the schedule and the job cannot fit together. Some of those jobs could have been kept.</p>
{{fig:sw09b_options}}
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>What you do</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td>Change the dialysis shift to fit work</td><td>Ask the unit about afternoon or evening slots</td><td>Head nurse and attending nephrologist</td></tr>
<tr><td>Ask the employer for adjusted hours</td><td>With consent, a letter stating the treatment schedule, without unnecessary detail</td><td>The employer</td></tr>
<tr><td>Sick leave, sickness or disability benefits</td><td>Check membership and contributions with the Social Security System (SSS) or the Government Service Insurance System (GSIS)</td><td>SSS or GSIS</td></tr>
<tr><td>Work that fits treatment</td><td>Referral to livelihood programs of the Department of Labor and Employment (DOLE) or local government; home-based work</td><td>The person</td></tr>
<tr><td>Peritoneal dialysis to free daytime hours</td><td>Raise it with the nephrologist if the person is interested (Module 14)</td><td>The person and the nephrologist</td></tr>
</tbody></table></div>
<p>An employer letter needs the person&rsquo;s consent and only the facts the employer needs: that they receive a treatment on set days and times. It should not name the diagnosis unless the person wants it named.</p>
{{key:Ask about work in the first month. A job kept is worth more than any assistance found later.}}
"""),
        ("home", "Housing, water, and food", "When home makes treatment unsafe", """
<p>A home affects treatment in concrete ways. Peritoneal dialysis needs a clean space and storage. Hemodialysis needs a fistula arm kept clean and safe. Everyone on dialysis needs food that fits the diet and a way to keep medicines dry and cool. Ask about these directly, without making the person feel judged.</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Why it matters clinically</th><th>Who must hear</th></tr></thead>
<tbody>
<tr><td>Skipping meals to pay fares</td><td>Weight loss, weakness, poor healing; low albumin is a warning sign on dialysis</td><td>Dietitian and nephrologist this week</td></tr>
<tr><td>Living on instant noodles and canned food</td><td>High salt; more thirst and fluid gain; often high phosphate</td><td>Dietitian</td></tr>
<tr><td>No clean water or a flooded home</td><td>Infection risk for peritoneal dialysis and wounds</td><td>Peritoneal dialysis nurse and nephrologist</td></tr>
<tr><td>Eviction, homelessness, unsafe home</td><td>Missed sessions; lost medicines; safety</td><td>Your supervisor and local social welfare office</td></tr>
</tbody></table></div>
<p>Food is the hidden cost of the access equation. When money runs short, families cut food first, because the fare cannot be cut. A patient who says &ldquo;we eat rice and noodles to save for the fare&rdquo; is telling you the access cost has already reached their plate.</p>
{{key:Ask what the household eats. When food is being cut to pay for transport, the dietitian and nephrologist need to know this week.}}
"""),
        ("disability", "Disability and the PWD ID", "A legal discount many miss", """
<p>People with kidney failure on dialysis may qualify as persons with disability under Philippine law, and a PWD ID carries a 20% discount on many purchases, including some medical services and medicines, as the site&rsquo;s patient guide explains. Many patients have never applied. Check the current requirements with the local office that issues PWD IDs, and ask the attending physician for the medical certificate it requires.</p>
<p>A discount is a percentage of what the patient pays, so it helps most when costs are high. It does not replace PhilHealth or assistance; it adds to them.</p>
{{flow:Helping a person get a PWD ID|Check eligibility::Ask the local issuing office about current rules for kidney failure and dialysis.|Medical certificate::Ask the attending physician for the certificate in the format the office requires.|Documents::Identification, photo, barangay documents as required.|Apply::A family member may be able to file on the patient&rsquo;s behalf; ask.|Use it::Show the ID before each payment; ask how the discount was computed.}}
{{key:Ask every patient on dialysis whether they have a PWD ID. It is a legal discount, not a favor.}}
{{scene:The shared ride|<p>Social worker Ms. Joanna Dizon notices that four patients on the same shift live in the same municipality and each pays for a special trip.</p>
<p>With their consent, she introduces them to each other. They share one vehicle and split the cost, and the local government agrees to cover part of the fare for dialysis days.</p>
<p class="tc-scene-take">The cost per person fell by more than half because someone looked at the schedule as a map.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The monthly cost.</strong> With 13 sessions a month: tricycle PHP 500 a day (250 each way) plus his wife&rsquo;s lost earnings of about PHP 400 a day = PHP 900 per visit, about PHP 11,700 a month before food. Put it in the access cost tool with him and his wife. Then compare it with their total monthly spending in the spending share tool; it is likely far above the 25% mark.</p>
<p><strong>Options.</strong> Ask the head nurse whether a later shift is possible (it would let him take the first jeepney and arrive on time, and solve the charge nurse&rsquo;s problem). Look for other patients from his barangay to share a ride. Check his SSS contributions from his driving years for disability or sickness benefits. Help him apply for a PWD ID. Check local government transport aid. Raise with the nephrologist whether his post-dialysis weakness needs review, and whether he might be interested in hearing about peritoneal dialysis.</p>
<p><strong>Referrals today.</strong> Eating mostly rice and instant noodles to save for the fare is a food and salt problem: tell the dietitian and nephrologist this week. His job loss and the family&rsquo;s strain deserve a check on mood (Module 10) and on his wife&rsquo;s load (Module 13). Tell the charge nurse what you found: the lateness has a cause, and a plan.</p>
"""],
    "skills": {"title": "An access cost estimate with a family",
               "intro": "With a simulated patient and companion, calculate the monthly access cost and spending share and agree a plan while your supervisor observes.",
               "items": [
                   ("Calculates monthly access cost including the companion, food, and lost wages.", False),
                   ("Subtracts only confirmed support when stating the gap.", True),
                   ("Calculates the household health spending share and explains the 10% and 25% marks as population indicators, not eligibility rules.", False),
                   ("Explores at least three work or schedule options and names who decides each.", False),
                   ("Asks about food, water, and housing, and routes food insecurity to the dietitian and nephrologist.", True),
                   ("Checks for a PWD ID and explains how to apply.", False),
               ],
               "placement": "For one patient (with consent), complete an access cost estimate and review it with the patient a month later to see what changed."},
    "terms": [("Access cost", "Everything it costs to attend treatment beyond the treatment itself."),
              ("Health spending share", "Out-of-pocket health spending divided by total household spending."),
              ("SDG 3.8.2", "The indicator counting households spending over 10% or 25% of their budget on health."),
              ("PWD ID", "An identification card for persons with disability, carrying legal discounts."),
              ("Food insecurity", "Not having reliable access to enough affordable, suitable food."),
              ("Employer letter", "A consented letter stating treatment days and times without unnecessary detail.")],
    "readings": [("pwd-card-ckd.html", "The patient guide to the PWD card for people with kidney disease."),
                 ("ckd-financial-stress.html", "The patient guide to money stress in kidney disease.")],
    "calcs": ["calc-social-worker-toolkit.html#tool-1", "calc-social-worker-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["09"])
