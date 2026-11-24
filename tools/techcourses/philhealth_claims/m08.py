# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 08: Payments, Reconciliation, and Professional Fees."""

MODULE = {
    "image_alt": "A finance staff member at a desk, seen in soft silhouette, looking through a glass window onto a bright dialysis treatment floor.",
    "objectives": [
        "Match claim, remittance, and ledger evidence at claim level, and classify every variance.",
        "Calculate the expected allowed amount and its facility and professional-fee split.",
        "State when professional fees must be released and track disbursement evidence.",
        "Compute first-pass acceptance, return, and denial rates with fixed, labeled definitions.",
        "Explain why accurate reconciliation is part of keeping patients on dialysis.",
    ],
    "big": """
{{plain:Reconciliation is checking your shopping receipt against the bag and your bank statement. Three records should tell the same story: what you claimed, what PhilHealth says it allowed and paid, and what finance actually posted. Any difference needs a reason and an owner.}}
<p>The picture has a limit: a missing grocery item is a small loss; a missing remittance is not. Hemodialysis was PhilHealth&rsquo;s top paid procedure in 2024, and its payments fund the unit that keeps patients alive: the machines, the nurses, the water system.[[pc_news2025_nkti]] A deposit that is never matched to its claims hides denials and underpayments until it is too late to act on them.</p>
{{fig:pc_match}}
{{cards:Key terms for this module|Claimed::What the facility filed.|Allowed::What PhilHealth accepted for payment.|Paid::What actually arrived.|Outstanding::What is still expected.|Remittance::PhilHealth&rsquo;s detailed payment advice, claim by claim.|Professional fee::The 350-peso share of each session&rsquo;s package for the professional.}}
""",
    "case": {"title": "One posting short", "html": """
<p>PhilHealth&rsquo;s remittance for SIM-08 shows two allowed hemodialysis sessions and a 12,700-peso payment. Finance can find only one 6,350-peso posting tied to the claim. Reimbursement was received on March 3. The nephrologist asks when to expect the professional fees.</p>
""", "questions": ["What is the expected allowed amount and its split?",
                  "How do you classify the missing 6,350 pesos, and who owns it?",
                  "By when must the professional fees be released?"]},
    "sections": [
        ("match", "The three-way match", "Matching claim, remittance, and ledger", """
<p>Match the claim reference, patient token, dates, and sessions across the claim register, the remittance detail, and the finance ledger. Separate claimed, allowed, paid, and outstanding amounts. Investigate unmatched or partial amounts, rejected sessions, accounting allocations, and batch posting delays, and record who owns each investigation and its next checkpoint.</p>
{{formula:<strong>Worked example.</strong> Four expected sessions: 4 &times; 6,350 = 25,400 pesos claimed. The remittance allows three: 3 &times; 6,350 = 19,050 pesos (18,000 facility and 1,050 professional) and lists the fourth as denied, with a denial workflow open (Module 7). Calculator 3 in the claims toolkit does this split and flags unexplained differences.}}
<p>A deposit alone never closes individual claims. One batch deposit can cover dozens of claims and some partial amounts; only the remittance lines and ledger postings show which.</p>
"""),
        ("fees", "Professional fees", "Releasing professional fees on time", """
<p>Under Circular 2024-0023, the facility releases the professional fees to the affiliated professionals within one month from receipt of PhilHealth reimbursement.[[pc_pc2024_0023]] Finance records the disbursement evidence. Patient adjustments go through the approved refund or correction workflow, not through the professional-fee account.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Example (fictional)</th></tr></thead>
<tbody>
<tr><td>Reimbursement received</td><td>March 3</td></tr>
<tr><td>Professional-fee release due</td><td>By April 3 (confirm your local counting convention)</td></tr>
<tr><td>Amount due</td><td>350 pesos &times; allowed sessions</td></tr>
<tr><td>Released, by whom, evidence</td><td>Finance; disbursement reference</td></tr>
</tbody></table></div>
"""),
        ("rates", "Performance rates", "Measuring the claims desk honestly", """
<p>Rates help a claims desk see whether its process is improving, but only if every month uses the same definitions. Label the cohort and the start point, and keep unsubmitted cases out of the rates (track them separately).</p>
<div class="table-wrap"><table>
<thead><tr><th>Rate</th><th>Numerator</th><th>Denominator</th></tr></thead>
<tbody>
<tr><td>First-pass acceptance</td><td>Claims paid without an initial return</td><td>Claims in the adjudicated cohort</td></tr>
<tr><td>Return rate</td><td>Claims initially returned</td><td>Claims with a first outcome in the cohort</td></tr>
<tr><td>Denial rate</td><td>Claims denied</td><td>Claims in the adjudicated cohort</td></tr>
<tr><td>Aging</td><td>Open receivables in 0&ndash;30, 31&ndash;60, 61&ndash;90, and over 90 days</td><td>All open receivables, from a labeled start point</td></tr>
</tbody></table></div>
<p>Example: 120 claims in the cohort, 9 initially returned, 3 denied, and 106 paid on first pass give a return rate of 7.5%, a denial rate of 2.5%, and first-pass acceptance of 88.3%. Calculator 4 computes these and refuses a cohort whose parts add up to more than the whole.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Expected amount.</strong> Two allowed sessions: 12,700 pesos, split 12,000 for the facility and 700 for professional fees.</p>
<p><strong>The missing posting.</strong> Classify the second 6,350 pesos as unexplained until confirmed. Match the remittance lines, the batch deposit, and the ledger postings, and assign a finance and claims follow-up with a date.</p>
<p><strong>Professional fees.</strong> Within one month of receiving reimbursement: by April 3, using your facility&rsquo;s counting convention. Finance records the disbursement evidence.</p>
"""],
    "skills": {"title": "Remittance reconciliation",
               "intro": "Reconcile a fictional remittance of five claims with one short payment and one denial, then compute the month&rsquo;s rates.",
               "items": [
                   ("Matches claim register, remittance lines, and ledger postings at claim level.", True),
                   ("Calculates the allowed amount and the facility and professional-fee split.", False),
                   ("Classifies every variance and assigns an owner and checkpoint.", True),
                   ("Computes the professional-fee release due date from the receipt date.", False),
                   ("Computes rates with labeled definitions and excludes unsubmitted cases.", False),
               ],
               "placement": "Reconcile one month of remittances at your unit with finance and present the unexplained items."},
    "quiz": [
        ("Can a deposit alone establish that all claims in a batch were paid?",
         ["Yes", "No; match it to detailed remittance and ledger allocations", "Only small batches", "Only in December"], 1,
         "Deposits hide partial payments."),
        ("When does the professional-fee release clock start under Circular 2024-0023?",
         ["At the session", "At receipt of PhilHealth reimbursement", "At filing", "At year end"], 1,
         "Release within one month of receipt."),
        ("Five allowed sessions. What are the gross, facility, and professional amounts?",
         ["31,750, 30,000, and 1,750 pesos", "31,750, 31,400, and 350 pesos", "30,000, 28,250, and 1,750 pesos", "25,400, 24,000, and 1,400 pesos"], 0,
         "6,350, 6,000, and 350 times five."),
        ("Reimbursement was received March 3. When must professional fees be released?",
         ["Within one week", "Within one month, by April 3 (confirm local counting convention)", "By year end", "When the doctor asks"], 1,
         "One month from receipt."),
        ("120 claims in the cohort, 9 initially returned. What is the return rate?",
         ["9%", "7.5%", "12%", "0.75%"], 1,
         "9 &divide; 120."),
        ("Which cases are excluded from performance rates?",
         ["Denied claims", "Unsubmitted cases, tracked separately", "Paid claims", "Returned claims"], 1,
         "Rates describe adjudicated claims."),
        ("Two allowed sessions and one 6,350-peso posting found. How is the rest classified?",
         ["Paid", "Unexplained until confirmed, with an owner", "Denied", "Refunded"], 1,
         "Never assume."),
        ("Why must aging start from a labeled point?",
         ["Decoration", "So months can be compared honestly", "PhilHealth requires day 30", "To shorten the report"], 1,
         "Receipt, transmission, or service date, chosen and stated."),
        ("Who records professional-fee disbursement evidence?",
         ["The clerk", "Finance", "The patient", "PhilHealth"], 1,
         "Claims staff track; finance disburses."),
        ("Four sessions claimed, three allowed. What is the difference from claimed?",
         ["6,350 pesos, with a denial workflow open", "350 pesos", "Zero", "25,400 pesos"], 0,
         "25,400 minus 19,050."),
        ("What is first-pass acceptance?",
         ["Claims filed on time", "Claims paid without an initial return, over the adjudicated cohort", "Claims with no errors at intake", "Claims under 30 days old"], 1,
         "Fixed definitions make months comparable."),
        ("Returned 9, denied 3, and first-pass paid 115 in a cohort of 120. What is wrong?",
         ["Nothing", "The parts add up to more than the cohort; check the data", "The denial rate is too low", "Rates cannot be computed"], 1,
         "Calculator 4 refuses this."),
        ("Where do patient refunds go?",
         ["Out of the professional-fee account", "Through the approved refund or correction workflow", "To PhilHealth", "To the nurse"], 1,
         "Keep the accounts separate."),
        ("Which three records does a three-way match compare?",
         ["Intake, PDD, eligibility", "Claim register, remittance detail, finance ledger", "CF1, CF2, CF4", "Schedule, transport, treatment"], 1,
         "Claim, payment advice, and posting."),
        ("Why does reconciliation matter to patients?",
         ["It does not", "Payments fund the unit that keeps them on dialysis, and unmatched deposits hide problems", "It sets their diet", "It changes their PIN"], 1,
         "Finance sustains care."),
    ],
    "terms": [("Claimed", "What the facility filed."),
              ("Allowed", "What PhilHealth accepted for payment."),
              ("Remittance", "PhilHealth&rsquo;s detailed payment advice."),
              ("Professional fee", "The professional&rsquo;s share of each package."),
              ("First-pass acceptance", "Claims paid without an initial return, over the adjudicated cohort."),
              ("Aging", "How long receivables have been open, from a labeled start point.")],
    "readings": [("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
