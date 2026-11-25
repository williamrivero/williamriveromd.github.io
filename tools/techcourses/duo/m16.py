# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 16: Unit economics and transparent pricing. Written for this course from published sources."""

MODULE = {
    "image_alt": "A 3D chart of rising teal bars crossing a falling navy curve, one bar stepping abruptly higher.",
    "objectives": [
        "Separate fixed, variable, and step costs and compute cost per treatment at different volumes.",
        "Calculate contribution and break-even, and recognize when no break-even exists.",
        "Test the plan with sensitivity analysis while holding safety costs fixed.",
        "Set and publish prices that patients can understand before they start.",
    ],
    "big": """
{{plain:Cost per treatment behaves like the cost per passenger on a jeepney. The driver&rsquo;s daily costs are mostly fixed, so each extra passenger lowers the cost per seat, until the jeepney is full and a second one is needed.}}
<p>The picture has a limit. A jeepney can squeeze in one more passenger. A dialysis unit cannot squeeze in a patient beyond what its staff can safely cover. Some costs are not choices: safe staffing, water testing, and infection supplies are constraints the economics must work around.</p>
{{cards:Key terms for this module|Fixed cost::A cost that does not change with sessions in a range: rent, core salaries, depreciation.|Variable cost::A cost that rises with each session: dialyzer, lines, concentrate, drugs.|Step cost::A cost that jumps at a threshold: a new shift or team.|Contribution::Net revenue per session minus variable cost per session.|Break-even::Fixed cost divided by contribution.}}
<p>Your work is to know your unit&rsquo;s numbers, keep safety outside the bargaining, and charge patients honestly.</p>
""",
    "case": {"title": "The price cut", "html": """
<p>A competitor opens near a unit in Cebu City and advertises that HMO patients pay nothing extra. The owner, Mr. Alberto Chua, considers cutting his net revenue per session for HMO patients by 1,000 pesos to keep their referrals. His fixed costs are 920,000 pesos a month, net revenue averages 6,350 pesos a session across all payers, and variable cost is 2,100 pesos. (All figures are fictional. Because the PhilHealth package includes the professional fee, the facility&rsquo;s own share of a PhilHealth session is less than 6,350 pesos; use your actual split.)</p>
""", "questions": ["What is the current break-even?", "What happens to break-even after the cut?", "What must not be cut to make the numbers work?"]},
    "sections": [
        ("costs", "Three kinds of cost", "Fixed, variable, and step", """
{{fig:duo16a}}
<p>Cost per treatment = (fixed + variable costs) &divide; sessions delivered. As sessions rise, fixed costs spread thinner, and cost per treatment falls, until a step adds a block of fixed cost at once. <strong>Worked example (fictional).</strong> With fixed costs of 920,000 pesos and variable cost of 2,100 pesos a session, cost per treatment is 4,729 pesos at 350 sessions and 4,400 pesos at 400. If a new nurse team adds 210,000 pesos a month above 400 sessions, cost per treatment at 450 is about 4,611 pesos, higher than at 400.</p>
{{key:Run the step before you promise the volume.}}
"""),
        ("contribution", "Contribution", "Contribution and break-even", """
{{fig:duo16b}}
<p>Contribution is what each session leaves after its own variable cost, to pay fixed costs and then profit. In the example, 6,350 &minus; 2,100 = 4,250 pesos. Break-even = 920,000 &divide; 4,250 = 216.5, so 217 sessions a month.</p>
<p>If contribution is zero or negative, no volume breaks even: every extra session loses money before overhead. The calculator says so instead of giving a number. That is a signal to fix price, payer mix, or variable cost, not to add volume.</p>
{{key:Negative contribution has no break-even. More volume makes it worse.}}
"""),
        ("sensitivity", "Sensitivity", "Test the numbers, not the safety", """
<p>Change one assumption at a time: volume, revenue, supply prices, collection days. Hold safety costs fixed while you do it. Staffing is the largest controllable cost and the one most tied to outcomes; facilities with heavier staffing loads were associated with higher death and hospitalization rates.[[uom_plantinga2024]] A budget that balances by cutting below safe staffing moves the cost to patients and, later, to admissions and the unit&rsquo;s reputation.</p>
{{key:Safety costs are constraints, not variables. Balance the budget with everything else.}}
"""),
        ("pricing", "Pricing", "Prices patients can understand", """
<p>Publish your charges for each payer category in plain language, and give each patient a written estimate before the first session (Module 14). Avoid prices that look free but recover the cost elsewhere, such as through compulsory purchases or extra fees. The patient-share calculator shows a family their yearly total.</p>
<p>Competing on price is legitimate. Competing on inducements, or by cutting the parts of care patients cannot see, is not.</p>
{{key:A price a family can understand before they start is part of good care.}}
"""),
    ],
    "debrief": ["""
<p><strong>Current break-even.</strong> 920,000 &divide; 4,250 = 217 sessions a month.</p>
<p><strong>After the cut.</strong> For HMO sessions, contribution falls to 3,250 pesos. If all sessions were at that level, break-even would rise to 920,000 &divide; 3,250 = 284 sessions. Mixed payers fall between. Run both on the calculator.</p>
<p><strong>What must not be cut.</strong> Safe staffing, water testing, infection supplies, and make-up slots. If the cut only works by touching those, decline it.</p>
"""],
    "skills": {"title": "Unit economics worksheet with safety constraints",
               "intro": "Complete a unit economics worksheet for a fictional unit and present the price decision to a mock board.",
               "items": [("Separates fixed, variable, and step costs.", False),
                         ("Calculates contribution and break-even on the calculator.", False),
                         ("Recognizes that a negative contribution has no break-even.", False),
                         ("Holds safe staffing, water testing, and infection supplies fixed in every scenario.", True),
                         ("Shows the step cost before committing to growth.", False),
                         ("Publishes charges and gives written estimates before the first session.", True)],
               "placement": "Ask your finance officer to classify last month&rsquo;s costs as fixed, variable, or step."},
    "quiz": [
        ("Fixed costs 920,000 pesos; contribution 4,250 pesos. Break-even is:",
         ["184", "217", "250", "4,250"],
         1, "920,000 &divide; 4,250 = 216.5, so 217 sessions."),
        ("Net revenue 3,000 pesos; variable cost 3,000 pesos. What is break-even?",
         ["1,000 sessions", "None: contribution is zero", "3,000 sessions", "Every session"],
         1, "With zero contribution, no volume covers fixed costs."),
        ("Why does cost per treatment fall as volume rises?",
         ["Variable costs disappear", "Fixed costs spread over more sessions", "Prices rise", "Staff work for free"],
         1, "Until a step adds fixed cost."),
        ("Which cost should be held fixed in every scenario?",
         ["Office decorations", "Safe staffing", "Advertising", "Owner distributions"],
         1, "Safety costs are constraints."),
        ("A competitor advertises free care but adds compulsory purchases. This is:",
         ["Transparent pricing", "A price that looks free but recovers the cost elsewhere", "Required by PhilHealth", "Good practice"],
         1, "Patients need the true total."),
        ("What is a step cost?",
         ["A cost per staircase", "A cost that jumps at a threshold, such as a new shift", "A variable cost", "A tax"],
         1, "Steps change cost per treatment suddenly."),
    ],
    "terms": [("Payer mix", "The share of sessions paid by PhilHealth, HMOs, patients, and others.")],
    "readings": [("zero-balance-billing-philhealth.html", "What zero balance billing means for patients.")],
    "calcs": ["calc-dialysis-owner-toolkit.html#c1", "calc-dialysis-owner-toolkit.html#c2", "calc-dialysis-owner-toolkit.html#c8"],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
