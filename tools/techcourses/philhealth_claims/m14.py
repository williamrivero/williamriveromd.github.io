# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 14: HMO Payments, Disallowances, and Collections.
Part 6 (HMO claims and collections), added November 26, 2026. Regulatory statements were checked against the
Insurance Commission's own documents on November 26, 2026. Every HMO, patient, staff name, and amount is fictional."""

MODULE = {
    "image_alt": "A claims officer and a finance officer review an aging report on a large screen, with columns of colored bars for several payers, one bar much longer than the rest.",
    "objectives": [
        "Post an HMO payment against its remittance and claims, including tax withheld, and classify every difference.",
        "Sort disallowances by cause, fix what is fixable at the source, and appeal within the contract window.",
        "Age HMO receivables by payer from proof of receipt, and run a dated, written collection ladder.",
        "Escalate an unresolved HMO dispute through provider relations, management, and the Insurance Commission&rsquo;s complaint process.",
        "Recognize payer risk early and keep any decision to stop accepting an HMO separate from a patient&rsquo;s treatment.",
    ],
    "big": """
{{plain:Collecting from several HMOs is like collecting rent from several tenants, each on a different lease. One pays on the first of the month, one pays late but in full, one pays part and argues about the rest. A good landlord keeps one page per tenant: what is owed, since when, and what was done about it. Nobody remembers; the page does.}}
<p>The picture has a limit. A landlord can evict a tenant who stops paying. A dialysis unit cannot evict a patient because the patient&rsquo;s HMO is slow. The money matters, because HMO payments help pay for the nurses, the machines, and the water system. But the person in the chair is not the debtor. The HMO is, under its contract with your unit.</p>
<p>The HMO sector has been under financial strain. In 2023 and again in 2024 the Insurance Commission eased its liquidity requirement for HMOs, citing rising health care costs and industry losses; under the 2024 relief, an HMO below the full requirement must send the Commission a monthly schedule of claims still payable and keep proof of payment of valid claims ready for inspection.[[pc_ic_cl2024_18]] For your desk, that is a reminder that payment speed is a signal worth watching, payer by payer.</p>
{{fig:pc_hmo_aging}}
{{cards:Key terms for this module|Remittance::The HMO&rsquo;s payment advice, claim by claim: billed, approved, deducted, paid.|Disallowance::An amount the HMO refuses to pay on a claim, with a stated reason.|Appeal::Your written request that the HMO reconsider a disallowance, within the contract window.|Aging::How long each unpaid claim has been open, counted from proof of receipt.|Collection ladder::Your written, dated sequence of follow-ups, from statement to formal complaint.|Exposure::The total your unit is owed by one HMO at a given time.}}
""",
    "case": {"title": "Three payers, three speeds", "html": """
<p>At month-end, Arnel Bautista, the claims officer, prints the aging report. &ldquo;Bayanihan Health&rdquo; (fictional) pays within its 30-day term. &ldquo;Kalinga Care&rdquo; (fictional) pays in about 45 days against a 45-day term. &ldquo;Tanglaw Medical Plan&rdquo; (fictional) has 1,180,000 pesos open, 640,000 of it more than 90 days past proof of receipt, against a 60-day term.</p>
<p>Tanglaw&rsquo;s latest remittance pays 212,000 pesos on a 260,000-peso batch. The 48,000-peso difference is listed as &ldquo;LOA expired&rdquo; for six sessions and &ldquo;not covered&rdquo; for two. Twelve patients at the unit carry Tanglaw cards. The unit manager asks Arnel: &ldquo;Should we stop accepting Tanglaw?&rdquo;</p>
""", "questions": ["How does Arnel handle the 48,000-peso difference?",
                  "What collection steps come next for Tanglaw&rsquo;s overdue balance?",
                  "How should he answer the manager, and what must happen for the twelve patients?"]},
    "sections": [
        ("posting", "Posting payments", "Matching HMO payments to claims", """
<p>Post HMO payments the way you post PhilHealth remittances (Module 8): match the claim register, the HMO&rsquo;s remittance, and the finance ledger at claim level. A bank deposit alone never closes a claim. One deposit can cover many claims, some paid in part.</p>
<p>HMO payments add one step. The HMO usually withholds tax on what it pays the unit and issues a certificate of tax withheld (BIR Form 2307). The amount deposited is then smaller than the amount approved, and the difference is tax already paid on the unit&rsquo;s behalf, not a short payment. Finance confirms the rate and collects the certificates; the claims desk records approved, withheld, and paid separately so a tax line is never mistaken for a disallowance.</p>
{{formula:<strong>Worked example (fictional).</strong> Batch billed: 260,000 pesos. HMO approved: 212,000 pesos. Tax withheld per the certificate: 4,240 pesos. Deposited: 207,760 pesos. Classify: 212,000 approved = 207,760 paid + 4,240 withheld (matched). The 48,000-peso gap between billed and approved is a disallowance, line by line, and opens the next workflow.}}
{{key:Keep approved, withheld, and paid in three columns. Only the gap between billed and approved is a disallowance.}}
"""),
        ("disallow", "Disallowances", "Sorting and appealing disallowances", """
<p>Read every disallowance line and sort it by cause. The cause decides the fix and the owner. Some are the unit&rsquo;s own errors, fixed at the source and refiled if the contract allows; some are the HMO&rsquo;s errors, contested in writing; some are true non-coverage, which you can learn from but not appeal.</p>
<div class="table-wrap"><table>
<thead><tr><th>Reason given</th><th>Usual cause</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>LOA expired or missing</td><td>Renewal not requested in time (Module 13)</td><td>If a valid LOA covered the date, appeal with it; if not, fix the reminder system, and follow unit policy for the balance</td></tr>
<tr><td>Amount above the approved limit</td><td>HMO line not capped by the LOA</td><td>Correct the split; the excess was never the HMO&rsquo;s</td></tr>
<tr><td>PhilHealth not deducted</td><td>PhilHealth share left on the HMO line</td><td>Correct the statement and refile per the contract</td></tr>
<tr><td>Not covered</td><td>Plan excludes the service</td><td>Check the plan; appeal only if the plan covers it; review how coverage was verified</td></tr>
<tr><td>Duplicate</td><td>Batch or claim sent twice, or HMO error</td><td>Show the single original with proof of receipt</td></tr>
<tr><td>Filed late</td><td>Missed contract filing period</td><td>Appeal only with proof of timely receipt</td></tr>
<tr><td>Missing document</td><td>Incomplete packet, or a document the contract does not require</td><td>Send it if required; if it is superfluous, say so in writing</td></tr>
</tbody></table></div>
<p>Write each appeal as a short letter: the claim, the amount, the HMO&rsquo;s stated reason, why it is wrong, the evidence attached, and the contract clause relied on. File it within the contract&rsquo;s appeal window, and diary the date you expect an answer. The Insurance Commission treats denying a claim without reasonable investigation of the available documents, and delaying payment by asking for superfluous documents, as unsound business acts by an HMO.[[pc_ic_cl2024_01]] Quote that standard politely when it applies; do not threaten with it.</p>
{{call:A disallowance caused by the unit&rsquo;s own error is never moved onto the patient&rsquo;s bill. Charge a patient only what your unit&rsquo;s policy allows and the patient agreed to in advance.}}
"""),
        ("aging", "Aging and the ladder", "Aging receivables and the collection ladder", """
<p>Age every unpaid claim from its proof of receipt, by HMO, in fixed buckets: 0 to 30, 31 to 60, 61 to 90, and over 90 days. Compare each HMO against its own contract term, not against the other HMOs. Thirty-five days is late for a 30-day term and early for a 60-day term. Calculator 8 in the claims toolkit builds this report from a list of claims and ranks the HMOs that need attention first.</p>
{{flow:A dated collection ladder (adapt the days to each contract)|At the payment term::Send a statement of account listing every open claim, with transmittal numbers and proof of receipt.|Term plus 15 days::Written reminder to the HMO&rsquo;s claims or accounts officer; ask for a payment date in writing.|Term plus 30 days::Escalate to the HMO&rsquo;s provider-relations head; request a reconciliation meeting with your list against theirs.|Term plus 60 days::Formal demand letter signed by management, citing the contract&rsquo;s payment and dispute clauses.|Unresolved::Management decides on a complaint to the Insurance Commission and on any change in accreditation.}}
<p>Under the Insurance Commission&rsquo;s Circular Letter 2018-14, complaints against an HMO that belongs to one of the two HMO industry associations are endorsed to that association&rsquo;s grievance machinery for mediation, which must conclude within 30 days of the endorsement; complaints against other HMOs, and cases that fail mediation, are handled by the Commission&rsquo;s Public Assistance and Mediation Division.[[pc_ic_cl2018_14]] Whether and when to file is a management decision. Your job is to make sure the file is ready: the contract, the claims list, the proofs of receipt, the remittances, every letter, and the dates of every call.</p>
{{key:Every step on the ladder is written and dated. A follow-up nobody wrote down did not happen.}}
"""),
        ("risk", "Payer risk", "Payer risk and the patients who carry the card", """
<p>Watch each HMO&rsquo;s pattern, not only its balance. Warning signs are a lengthening average time to pay, more partial payments, new reasons for disallowance, requests for documents the contract never required, and slow answers to reconciliation requests. Report them to the claims lead and finance monthly, with the numbers. Rates and patterns, labeled and dated, persuade management far better than a sense that &ldquo;Tanglaw is always late.&rdquo;</p>
<p>When management considers suspending or ending an accreditation, the decision belongs to management and must follow the agreement&rsquo;s notice clause. The desk&rsquo;s part is to protect the patients who carry that card:</p>
<ul>
<li>List every affected patient, with each one&rsquo;s PhilHealth status and remaining sessions.</li>
<li>Make sure each patient hears about the change from the unit, in plain words, before it takes effect, with what it means for their bill.</li>
<li>Route patients who will face new costs to social service for funding options, early.</li>
<li>Keep claims for services already rendered under the old agreement alive: they are still owed.</li>
</ul>
<p>No patient&rsquo;s session is stopped or delayed because of an HMO dispute. The PhilHealth benefit is unaffected by any HMO decision, and the treating team, not the claims desk, decides any change in a patient&rsquo;s care.</p>
{{key:An HMO&rsquo;s debt is a business problem between the unit and the HMO. It is never settled at the dialysis chair.}}
"""),
    ],
    "debrief": ["""
<p><strong>The 48,000 pesos.</strong> Sort it line by line. For the six &ldquo;LOA expired&rdquo; sessions, check the LOA file: if a valid LOA covered any of those dates, appeal with it within the contract window; if not, the error is the unit&rsquo;s, so fix the renewal reminders and follow unit policy for the balance, without moving it silently onto the patients. For the two &ldquo;not covered&rdquo; lines, check the plan; appeal only if it covers the service, and review how coverage was verified at intake.</p>
<p><strong>Tanglaw&rsquo;s overdue balance.</strong> It is well past the 60-day term, so the ladder is overdue too. Send a full statement of account with proofs of receipt, request a reconciliation meeting with provider relations, and prepare the file for a management demand letter. Record every step with a date.</p>
<p><strong>The manager&rsquo;s question.</strong> Give the facts, not a verdict: Tanglaw&rsquo;s days to pay, partial payments, and disallowance trend against its contract, and the exposure. The decision is management&rsquo;s, under the agreement&rsquo;s notice clause. Whatever it decides, the twelve patients keep their sessions, hear about any change from the unit before it happens, and are referred early to social service if their costs will change. Their PhilHealth benefit is not affected.</p>
"""],
    "skills": {"title": "HMO remittance, aging, and collection file",
               "intro": "Post a fictional HMO remittance with tax withheld and disallowances, write one appeal, and build an aging report for three HMOs.",
               "items": [
                   ("Separates approved, withheld, and paid, and matches each claim to its remittance line.", True),
                   ("Sorts every disallowance by cause and assigns an owner and a date.", True),
                   ("Writes an appeal with the claim, reason, evidence, and contract clause, within the window.", False),
                   ("Ages claims from proof of receipt and compares each HMO with its own term.", False),
                   ("Keeps a dated collection ladder and a complete escalation file.", False),
                   ("Never moves a unit-caused disallowance onto a patient&rsquo;s bill.", True),
               ],
               "placement": "Prepare one month&rsquo;s HMO aging report at your unit with finance and present the three oldest items with their next steps."},
    "quiz": [
        ("A deposit is smaller than the approved amount by exactly the tax on the certificate. What is the difference?",
         ["A disallowance", "Tax withheld on the unit&rsquo;s behalf, not a short payment", "A duplicate", "An error by the bank"], 1,
         "Keep approved, withheld, and paid in separate columns."),
        ("Which document shows tax an HMO withheld from its payment to the unit?",
         ["The LOA", "BIR Form 2307, the certificate of tax withheld", "The transmittal", "The PhilHealth remittance"], 1,
         "Finance collects the certificates."),
        ("Billed 260,000 pesos, approved 212,000. What is the disallowance?",
         ["212,000 pesos", "48,000 pesos", "4,240 pesos", "260,000 pesos"], 1,
         "Only the gap between billed and approved."),
        ("A disallowance says &ldquo;LOA expired,&rdquo; and your file shows a valid LOA for that date. What do you do?",
         ["Accept it", "Appeal in writing with the valid LOA, within the contract window", "Bill the patient", "Refile the claim twice"], 1,
         "Evidence plus the clause, on time."),
        ("A disallowance came from the unit&rsquo;s own split error. Who pays the excess?",
         ["The patient, automatically", "Not the patient by default; correct the source and follow unit policy", "PhilHealth", "The HMO anyway"], 1,
         "Unit errors are not moved onto patients."),
        ("From what point do you age an unpaid HMO claim?",
         ["The service date only", "The proof of receipt of the batch", "The day it is paid", "The year end"], 1,
         "Proof of receipt starts the clock."),
        ("A claim is 35 days old. When is it late?",
         ["Always", "When it is past that HMO&rsquo;s own contract term", "Never", "After 90 days only"], 1,
         "Compare each HMO with its own term."),
        ("What does a written collection ladder add?",
         ["Nothing", "Dated, recorded steps that management and the Insurance Commission can follow", "Faster dialysis", "Lower taxes"], 1,
         "A follow-up nobody wrote down did not happen."),
        ("Under Circular Letter 2018-14, where is a complaint against an HMO that belongs to an industry association first sent?",
         ["Directly to court", "To that association&rsquo;s grievance machinery for mediation", "To PhilHealth", "To the Department of Health"], 1,
         "Mediation must conclude within 30 days of endorsement."),
        ("How long does the association have to conclude mediation of an endorsed complaint?",
         ["7 days", "30 days from receipt of the endorsement", "90 days", "One year"], 1,
         "Failed cases go to the Commission&rsquo;s mediation division."),
        ("Who decides whether to file a complaint or suspend an HMO accreditation?",
         ["The clerk", "Management, following the agreement&rsquo;s notice clause", "The patient", "The HMO&rsquo;s agent"], 1,
         "The desk prepares the file and the facts."),
        ("Which is a warning sign of payer risk?",
         ["Payment within term", "Lengthening time to pay and more partial payments", "Clear remittances", "Fast LOA approvals"], 1,
         "Watch the pattern, not only the balance."),
        ("The unit suspends an HMO. What happens to sessions for patients carrying that card?",
         ["They stop", "They continue; patients are told in advance and routed to social service if costs change", "They move to another unit", "They wait for the HMO"], 1,
         "A debt is never settled at the chair."),
        ("What happens to claims for services already rendered when an accreditation ends?",
         ["They are forgiven", "They are still owed and pursued", "They go to PhilHealth", "They expire immediately"], 1,
         "Rendered services remain receivable."),
        ("What did the Insurance Commission&rsquo;s 2024 liquidity relief require of HMOs below the full requirement?",
         ["Nothing", "A monthly schedule of claims payable and proof of payment of valid claims on request", "Closing within 30 days", "Paying all claims in cash"], 1,
         "A sign of sector strain worth watching payer by payer."),
    ],
    "terms": [("Remittance", "The HMO&rsquo;s claim-by-claim payment advice."),
              ("Disallowance", "An amount the HMO refuses to pay, with a reason."),
              ("Appeal", "A written request to reconsider a disallowance, within the contract window."),
              ("Aging", "How long a claim has been unpaid, counted from proof of receipt."),
              ("Collection ladder", "A dated, written sequence of follow-ups."),
              ("Exposure", "The total owed by one HMO at a given time.")],
    "readings": [("hmo-ckd-coverage.html", "Why HMOs often limit kidney care, explained for patients and families.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
