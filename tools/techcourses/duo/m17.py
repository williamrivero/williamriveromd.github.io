# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 17: Cash flow, working capital, and financial controls. Written for this course from published sources."""

MODULE = {
    "image_alt": "A finance officer studying a thirteen-week wall calendar beside a bundle of payroll envelopes.",
    "objectives": [
        "Explain why a profitable unit can run out of cash.",
        "Calculate cash tied up in receivables, days sales outstanding (DSO), and runway.",
        "Build a 13-week cash forecast with base, delayed-collection, and disruption cases.",
        "Install the basic controls that stop money going missing, and pay people first.",
    ],
    "big": """
{{plain:Cash is the blood pressure of a business. A patient can have a healthy heart and still faint if pressure drops for a moment. A unit can be profitable on paper and still miss payroll if cash arrives two months after the sessions it pays for.}}
<p>The picture has a limit. Blood pressure recovers in seconds. A missed payroll damages trust for months, and a missed supplier payment can stop deliveries of dialyzers. That is why owners watch cash weekly, not only profit monthly.</p>
{{cards:Key terms for this module|Receivables::Money owed to the unit for sessions already delivered.|Days sales outstanding (DSO)::Receivables divided by daily revenue: how many days of revenue are waiting.|Working capital::Cash needed to run while receivables are collected.|Runway::Weeks the unit can pay its bills from cash on hand.|Segregation of duties::Splitting tasks so no one person can order, approve, and pay alone.}}
<p>Your work is to see cash problems weeks before they happen and to make sure that money cannot quietly disappear.</p>
""",
    "case": {"title": "Profitable and short", "html": """
<p>A 15-station unit in Batangas City shows an operating profit of 780,000 pesos a month. In the second week of November, the finance officer, Mr. Rolando Dimaculangan, warns that payroll at the end of the month may be short. Net revenue is about 2.54 million pesos a month, receivables are 6.35 million pesos, cash on hand is 3 million, and monthly cash costs including the loan are 2.2 million.</p>
""", "questions": ["How can a profitable unit be short of cash?", "How many weeks of runway does it have?", "What should the board do first?"]},
    "sections": [
        ("profit-cash", "Profit is not cash", "Why profit is not cash", """
{{fig:duo17a}}
<p>Revenue is recognized when a session is delivered. Cash arrives when the claim is paid, often weeks or months later. In between, the unit pays staff, suppliers, rent, and the loan. The gap must be financed, and that is working capital.</p>
<p><strong>Worked example (fictional).</strong> Net revenue of 2.54 million pesos a month is about 84,700 pesos a day. If claims take 75 days to pay, about 84,700 &times; 75 = 6.35 million pesos is tied up in receivables at any moment. The income statement can look healthy while the bank balance falls.</p>
{{key:Watch cash weekly. Profit tells you whether the model works; cash tells you whether you will make payroll.}}
"""),
        ("forecast", "The forecast", "The 13-week cash forecast", """
<p>A 13-week forecast lists, week by week, opening cash, expected receipts, payroll and statutory remittances, supplier payments, loan payments, and closing cash. Next week&rsquo;s opening cash is this week&rsquo;s closing cash. Build three cases: a base case, a delayed-collection case, and a disruption case such as a typhoon week. Count each claim once; do not include it in both ordinary receipts and a catch-up line.</p>
<p>Set triggers. In this course&rsquo;s teaching example, runway under 13 weeks prompts a board review and under 8 weeks prompts immediate action. Those are teaching marks, not standards; set your own with your accountant and lender.</p>
{{key:Forecast thirteen weeks in three cases and act on triggers, not surprises.}}
"""),
        ("controls", "Controls", "Controls that stop money going missing", """
{{fig:duo17b}}
<p>Four simple controls prevent most losses: two signatures for payments above a limit; the person who orders goods is not the person who pays for them; someone other than the bookkeeper reconciles the bank statement every month; and payroll and statutory remittances are paid before discretionary spending. Add a rule that owner and related-party transactions are approved by someone without the conflict.</p>
{{key:No one person should be able to order, approve, and pay.}}
"""),
        ("triggers", "When cash runs short", "When cash runs short", """
<p>When the forecast shows a shortfall, act in this order: chase the oldest claims and fix the causes from Module 15; agree payment timing with suppliers early and honestly; draw on the working capital reserve; then seek short-term financing. Hold owner distributions. Pay staff and remittances first.</p>
{{stop:Never delay payroll or statutory remittances to protect distributions, and never cut safety supplies to cover a cash gap.}}
{{key:Pay people first, distributions last, and keep the safety supplies flowing.}}
"""),
    ],
    "debrief": ["""
<p><strong>Profitable and short.</strong> About 6.35 million pesos is tied up in receivables at 75 days. Profit is real; cash is late.</p>
<p><strong>Runway.</strong> 3 million &divide; about 508,000 pesos of cash costs a week = about 5.9 weeks. That is below the 8-week teaching trigger: act now.</p>
<p><strong>First steps.</strong> Chase the oldest claims, fix the causes of delay, talk to suppliers early, draw the reserve, hold distributions, and pay staff and remittances on time.</p>
"""],
    "skills": {"title": "Rolling cash forecast, liquidity triggers, and bank controls",
               "intro": "Build a 13-week cash forecast in three cases and a bank-control checklist.",
               "items": [("Explains the gap between recognized revenue and cash.", False),
                         ("Calculates cash tied in receivables, DSO, and runway on the calculator.", False),
                         ("Builds base, delayed-collection, and disruption cases without double counting.", False),
                         ("Sets triggers with the accountant and lender.", False),
                         ("Installs two-signature, split-duty, and independent reconciliation controls.", False),
                         ("Pays payroll and remittances before distributions and never cuts safety supplies for cash.", True)],
               "placement": "Ask your finance officer for receivables by age and calculate DSO."},
    "quiz": [
        ("Why can a profitable unit run short of cash?",
         ["Profit is always fake", "Cash for sessions arrives weeks after the costs are paid", "PhilHealth pays in advance", "Taxes are paid daily"],
         1, "The collection gap must be financed."),
        ("Net revenue 2.54 million pesos a month; claims take 75 days. About how much is tied in receivables?",
         ["2.54 million", "6.35 million", "75,000", "190 million"],
         1, "About 84,700 &times; 75."),
        ("Cash on hand 3 million; weekly cash costs about 508,000. Runway is about:",
         ["2 weeks", "6 weeks", "13 weeks", "26 weeks"],
         1, "3,000,000 &divide; 508,000 is about 5.9 weeks."),
        ("Which control separates duties?",
         ["One person orders, approves, and pays", "The person who orders goods does not pay for them", "No bank reconciliation", "Cash kept in a drawer"],
         1, "Segregation of duties prevents loss and fraud."),
        ("Cash is short. What comes first?",
         ["Owner distributions", "Payroll and statutory remittances", "New equipment", "Marketing"],
         1, "People and legal obligations come first."),
        ("Why build a disruption case in the forecast?",
         ["For decoration", "Typhoons and outages delay collections and raise costs", "PhilHealth requires it", "To lower taxes"],
         1, "Disruptions are predictable in kind, if not in date."),
    ],
    "terms": [("Bank reconciliation", "Matching the unit&rsquo;s records to the bank statement.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html#c5"],
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
