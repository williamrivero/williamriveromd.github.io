# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 7: Capital planning and financing. Written for this course from published sources."""

MODULE = {
    "image_alt": "A calculator, a loan schedule, and building keys resting on a clinic floor plan, with a hard hat at the edge.",
    "objectives": [
        "Build a sources-and-uses table that includes working capital and contingency.",
        "Calculate a loan payment and the debt service coverage ratio (DSCR), and test it under delay.",
        "Size reserves for repairs, replacement, and slow collections.",
        "Set a distribution policy that pays owners only after safety and solvency tests pass.",
    ],
    "big": """
{{plain:Financing a dialysis unit is like packing for a long trip with no shops on the way. You pack the obvious things, then the spare tire, the water, and the money for the day the bus breaks down. The spare tire never looks necessary until it is.}}
<p>The picture has a limit. A traveler can cut the trip short. A unit with patients cannot. Reserves are not caution for its own sake; they are what lets the unit keep treating people through a broken pump, a late payment, or a typhoon.</p>
{{cards:Key terms for this module|Sources and uses::A table showing where the money comes from and where it goes; the totals must match.|Working capital::Cash needed to run while payments are still on their way.|Debt service::Loan principal and interest due in a period.|Debt service coverage ratio (DSCR)::Cash available for debt payments divided by the payments due.|Distribution::Money paid out to owners.}}
<p>Your work here is to raise enough money for the whole unit, including the parts that only matter on a bad day, and to pay owners last.</p>
""",
    "case": {"title": "The seven-year loan", "html": """
<p>Three partners in Lipa, Batangas, plan a 12-station unit. A bank offers 12 million pesos over seven years at 9% a year. Their projection shows 3.2 million pesos a year of cash available for loan payments. Two partners want monthly distributions from the first profitable month, &ldquo;to recover our money.&rdquo; The third, Dr. Hazel Mercado, is the unit&rsquo;s future clinical head and worries about the water system&rsquo;s replacement in year eight.</p>
""", "questions": ["Can the unit carry this loan?", "What happens to the coverage if collections slow?", "What should the distribution policy say?"]},
    "sections": [
        ("sources", "Sources and uses", "Every peso accounted for", """
{{fig:duo07a}}
<p>A sources-and-uses table puts the money raised on one side and the money spent on the other. Sources are owner equity, loans, and sometimes supplier or lease financing. Uses are the fit-out, the water system, machines and chairs, opening stock, licensing, the working capital reserve, and a contingency. The two columns must add to the same total.</p>
<p>The lines owners forget are the last two. A unit that spends everything on the building opens with no cash to pay staff while the first claims are processed. Size working capital from your expected days to collect (Module 17), and set a contingency for the inevitable surprises in construction and commissioning.</p>
{{key:If working capital and contingency are not in the uses column, the plan is not funded.}}
"""),
        ("debt", "Debt", "Can the unit carry the loan?", """
<p>A loan&rsquo;s monthly payment depends on the principal, the rate, and the term. <strong>Worked example (fictional).</strong> 12 million pesos at 9% for seven years costs about 193,000 pesos a month, roughly 2.32 million pesos a year. With 3.2 million pesos a year available, the DSCR is about 3.2 &divide; 2.32 = 1.38.</p>
<p>A ratio above 1 means cash covers the payments; the cushion above 1 is what protects you when something goes wrong. Many lenders look for 1.25 or more, but your loan agreement sets the actual covenant. Now test it: if collections slow by sixty days in the first year, available cash may fall well below the projection, and the ratio may drop below 1. That is the year to have a reserve.</p>
{{key:Test the coverage ratio with slow collections, not only with the projection.}}
"""),
        ("reserves", "Reserves", "Reserves for the bad day", """
<p>Three reserves protect patients. A <strong>working capital reserve</strong> covers payroll and suppliers while claims are pending. A <strong>repair reserve</strong> lets a held machine or a failed pump be fixed today, without a board debate. A <strong>replacement reserve</strong> sets aside money every year for machines and the water system, which wear out on a schedule you can predict.</p>
<p>Use the project calculator to compare a planned replacement with an emergency one. A water system replaced on schedule is a project; a water system that fails is a crisis that stops every session.</p>
{{key:Fund repairs and replacement every year, before anyone is paid a distribution.}}
"""),
        ("distributions", "Distributions", "Owners are paid last", """
{{fig:duo07b}}
<p>A distribution policy decides when owners may take money out. Make it conditional. Before any distribution, the board confirms four things: payroll and statutory remittances are current, every funded safety action is on time, the cash reserve is at target, and loan covenants are met. If any answer is no, the distribution waits.</p>
<p>This protects owners too. Distributions taken from a unit that later cannot pay its staff or fix its water are distributions that will have to be put back, usually at a worse moment.</p>
{{stop:Do not approve a distribution while payroll, remittances, or a funded safety action is overdue.}}
{{key:Safety and solvency first, distributions last.}}
"""),
    ],
    "debrief": ["""
<p><strong>Can the unit carry the loan?</strong> On the projection, yes: DSCR about 1.38. But test it at 60 days of slower collections and lower first-year volume. If the ratio falls below 1, raise more equity or negotiate a grace period.</p>
<p><strong>The policy.</strong> No monthly distributions from the first profitable month. Distributions only after the four conditions pass, reviewed quarterly. Dr. Mercado is right: put the water system&rsquo;s replacement into an annual reserve now.</p>
"""],
    "skills": {"title": "Capital plan, sources and uses, and distribution policy",
               "intro": "Prepare a capital plan for a fictional 12-station unit and present it to a mock lender and board.",
               "items": [("Balances sources and uses, including working capital and contingency.", False),
                         ("Calculates the loan payment and DSCR on the calculator.", False),
                         ("Re-tests coverage with a 60-day collection delay.", False),
                         ("Funds repair and replacement reserves every year.", False),
                         ("Holds distributions while payroll, remittances, or a safety action is overdue.", True),
                         ("Presents the plan with assumptions labeled as fictional or sourced.", False)],
               "placement": "Ask your finance officer for last year&rsquo;s repair spending and compare it with the reserve."},
    "quiz": [
        ("Which line is most often missing from a new unit&rsquo;s uses column?",
         ["Machines", "Working capital reserve", "Chairs", "Signage"],
         1, "Without working capital, the unit cannot pay staff while claims are pending."),
        ("Annual cash available is 3.2 million pesos; annual debt service is 2.32 million. What is the DSCR?",
         ["0.73", "1.38", "2.32", "5.52"],
         1, "3.2 &divide; 2.32 is about 1.38."),
        ("What does a DSCR below 1 mean?",
         ["The loan is paid off", "Cash does not cover the debt payments", "The bank owes the unit", "The unit is profitable"],
         1, "Below 1, the unit must find cash elsewhere to pay the loan."),
        ("Why test coverage with slow collections?",
         ["Banks require color charts", "Slow collections reduce the cash available for payments, often in the first year", "It raises the interest rate", "It is a DOH rule"],
         1, "Collection delay is one of the commonest reasons a sound plan runs short of cash."),
        ("Which condition should block an owner distribution?",
         ["A new staff uniform", "Overdue payroll or remittances", "A rainy month", "A new competitor"],
         1, "Payroll, remittances, and funded safety actions come before distributions."),
        ("Why set aside a replacement reserve every year?",
         ["To lower taxes", "Machines and water systems wear out on a predictable schedule", "PhilHealth requires it", "To raise prices"],
         1, "Planned replacement avoids a crisis that stops every session."),
    ],
    "terms": [("Covenant", "A condition in a loan agreement, such as a minimum coverage ratio."),
              ("Contingency", "Money set aside for costs that are likely but not yet known.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html#c6", "calc-dialysis-owner-toolkit.html#c7"],
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
