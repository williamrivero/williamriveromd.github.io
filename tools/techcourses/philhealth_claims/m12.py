# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 12: HMOs, Accreditation, and the Payer Profile.
Part 6 (HMO claims and collections), added November 26, 2026. Regulatory statements were checked against the
Insurance Commission's own documents on November 26, 2026. Every HMO, patient, and staff name here is fictional."""

MODULE = {
    "image_alt": "A claims officer at a desk pins four color-coded payer cards to a corkboard beside a printed contract, with the dialysis floor visible through a window.",
    "objectives": [
        "Explain who regulates health maintenance organizations in the Philippines and how to confirm that an HMO is licensed.",
        "Identify the clauses of an HMO accreditation agreement that govern claims, and record them in a payer profile.",
        "Explain in plain words why many HMO plans limit or exclude maintenance dialysis.",
        "Apply the payment order for a dialysis session: PhilHealth first, then the HMO, then the patient, with each peso billed once.",
        "Keep treatment separate from coverage when an HMO card, contract, or plan is in doubt.",
    ],
    "big": """
{{plain:Each HMO your unit works with is like a different club with its own house rules. Your unit holds a membership with each club: the accreditation agreement. One club wants approval by phone, another by portal. One pays in 30 days, another in 60. One covers dialysis, another does not. Nobody can memorize all the rules, so the claims desk writes them down, club by club, and checks them before every claim.}}
<p>The picture has a limit. A club can bend its own rules; an HMO cannot. HMOs are regulated by the Insurance Commission, and its circulars set standards for how they handle members, approvals, and claims.[[pc_eo192_2015]][[pc_ic_cl2024_01]] Your unit&rsquo;s contract with each HMO sits inside those rules. And one thing no contract changes: a patient on maintenance hemodialysis (HD) still needs the next session on time, whatever the card in their wallet says.</p>
<p>This module is about knowing your payers. Most HMO claim problems are not mysteries. They come from a lapsed accreditation, a plan that never covered dialysis, or a rule that changed in the contract but not in the desk&rsquo;s memory. Your work is to know, for each HMO, what was agreed, and to keep that knowledge written, dated, and current.</p>
{{fig:pc_hmo_payers}}
{{cards:Key terms for this module|HMO::A health maintenance organization: a company that collects fixed fees from members or employers and pays accredited providers for covered care.|Accreditation agreement::The signed contract between your unit and one HMO: services, rates, approvals, documents, and payment terms.|Letter of authorization::The HMO&rsquo;s approval for a service, with a code, validity dates, and an approved amount (Module 13).|Maximum benefit limit::The most the plan will pay for a member in a period, per illness or per year.|Pre-existing condition::An illness that began before the member&rsquo;s coverage started; many plans limit it.|Payer profile::Your one-page summary of one HMO&rsquo;s rules, taken from the signed contract and kept current.}}
""",
    "case": {"title": "A card from a club we used to belong to", "html": """
<p>Mr. Rodolfo Aquino (fictional, SIM-12), 61, transfers to your unit for maintenance HD three times a week. He is registered in the PhilHealth Dialysis Database and has used 141 of his 156 sessions this year. At intake his daughter hands you a health card from &ldquo;Sagip Health&rdquo; (a fictional HMO). &ldquo;His company plan covers everything,&rdquo; she says. &ldquo;Please bill them for the rest.&rdquo;</p>
<p>Your payer list shows that your unit&rsquo;s accreditation with Sagip Health ended on September 30 and has not been renewed. Nobody at the desk has read Mr. Aquino&rsquo;s plan. His first session with you is in two hours.</p>
""", "questions": ["Does anything about the card change whether Mr. Aquino is dialyzed today?",
                  "What do you need to know before you tell the family that Sagip Health will pay anything?",
                  "Why do his 141 used sessions matter for the HMO conversation?"]},
    "sections": [
        ("regulation", "Who regulates HMOs", "Who regulates HMOs, and how to check a license", """
<p>Until 2015 the Department of Health supervised HMOs. Executive Order No. 192, signed on November 12, 2015, transferred their regulation and supervision to the Insurance Commission, which now licenses HMOs, sets their capital and reserve rules, and acts against fraud and deceptive practices.[[pc_eo192_2015]] An HMO operating legally holds a certificate of authority from the Commission, and the Commission publishes the list of HMOs that hold one.[[pc_ic_hmo_list]]</p>
<p>The Commission&rsquo;s Circular Letter 2024-01 lists unsound business acts for HMOs. Several touch the claims desk directly: denying claims without reasonable investigation of the available documents, failing to affirm or deny a claim within a reasonable time after the required documents are in, failing to issue or deny a letter of authorization within a reasonable time, and delaying payment by asking for superfluous or irrelevant documents.[[pc_ic_cl2024_01]] The circular sets fines per violation and allows suspension or revocation of a license. It speaks of a &ldquo;reasonable time&rdquo;; it does not set a number of days. The number of days you can hold an HMO to comes from your contract.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you check</th><th>Where</th><th>How often</th></tr></thead>
<tbody>
<tr><td>The HMO holds a current certificate of authority</td><td>The Insurance Commission&rsquo;s published list</td><td>At accreditation, then every quarter</td></tr>
<tr><td>Your unit&rsquo;s accreditation with the HMO is in force on the service date</td><td>The signed agreement and its renewal letter</td><td>Before every claim batch</td></tr>
<tr><td>The HMO has not notified a suspension or a change in terms</td><td>Written notices filed in the payer profile</td><td>Whenever a notice arrives</td></tr>
</tbody></table></div>
{{key:An HMO card proves membership in a plan. It does not prove that the plan covers dialysis, or that your unit is accredited with that HMO today.}}
"""),
        ("contract", "The agreement", "What the accreditation agreement decides", """
<p>The accreditation agreement is the rulebook for every claim you send that HMO. Two HMOs can differ on almost every clause, which is why the desk never works from memory or from what a call-center agent said last month. Read the signed agreement, then copy the clauses below into a payer profile for that HMO. Date it, name who checked it, and update it whenever an amendment or notice arrives.</p>
{{fig:pc_hmo_profile}}
<div class="table-wrap"><table>
<thead><tr><th>Clause</th><th>The question it answers</th><th>Why the desk needs it</th></tr></thead>
<tbody>
<tr><td>Covered services and rates</td><td>Which services the HMO pays for at your unit, and at what contracted rate</td><td>You cannot bill a rate the contract does not list.</td></tr>
<tr><td>Approval rules</td><td>Whether a letter of authorization is needed per session or per period, how to request it, and how long it stays valid</td><td>An expired or missing approval is a common reason for disallowance (Module 14).</td></tr>
<tr><td>Coordination with PhilHealth</td><td>How the PhilHealth benefit is applied before the HMO pays</td><td>Prevents billing the same peso twice.</td></tr>
<tr><td>Filing period and documents</td><td>How many days you have to submit, from what start point, with which attachments</td><td>Late or incomplete claims may be refused.</td></tr>
<tr><td>Payment term</td><td>How many days the HMO has to pay after receiving a complete claim</td><td>Your aging and follow-up clock (Module 14).</td></tr>
<tr><td>Professional fees</td><td>Whether the nephrologist bills the HMO directly or through the unit</td><td>Avoids a fee billed twice or not at all.</td></tr>
<tr><td>Disallowances and appeals</td><td>How a deduction is explained and how many days you have to contest it</td><td>An appeal filed late is usually lost.</td></tr>
<tr><td>Suspension and termination</td><td>How much notice either side must give, and what happens to patients mid-treatment</td><td>Protects patients and claims already rendered.</td></tr>
</tbody></table></div>
<p>When the agreement is silent or unclear on a point, do not fill the gap with a guess. Ask the HMO&rsquo;s provider-relations officer in writing, file the written answer in the payer profile, and tell the claims lead.</p>
{{key:The signed agreement governs. Memory, habit, and a phone call do not.}}
"""),
        ("coverage", "Why dialysis is limited", "Why many HMO plans limit maintenance dialysis", """
<p>HMOs are priced for illness that comes and goes: a pneumonia, a fracture, an operation. They spread that cost across many members, most of whom stay healthy in a given year. Kidney failure on maintenance dialysis is the opposite. It is lifelong, it is predictable, and it costs the same large amount every week. A plan that paid for it without limit would have to charge every member much more. That is why plans often exclude or cap pre-existing chronic conditions, and why some cover dialysis only up to the maximum benefit limit or only as part of a hospital stay.</p>
<p>The result for your desk is simple: <strong>never assume a plan covers dialysis.</strong> Plans differ even within one HMO, because an employer buys a specific package. Confirm coverage for this member, for this service, for this period, and get it in writing. The site&rsquo;s patient guide on HMO coverage for kidney disease explains the same facts to families in plain words.</p>
<p>Why the urgency matters. In a large United States cohort of patients on HD, missed and shortened sessions were associated with more hospitalization and higher death rates; in a European cohort, missing a session was associated with higher risks of hospitalization and death, most of all when the missed session followed the long weekend gap.[[pc_obialo2012]][[pc_fotheringham2020]] Both studies were observational. They show a strong association, not proof that each missed session causes harm, but they are why this course treats a coverage question as never a reason to delay treatment.</p>
{{call:Never tell a patient or family that a session will not happen until the HMO approves it. Treatment goes ahead under your unit&rsquo;s payment policy while the coverage question is worked out.}}
"""),
        ("order", "Who pays first", "PhilHealth first, then the HMO, then the patient", """
<p>When a patient has both PhilHealth and an HMO, the benefits are layered. On October 1, 2026, PhilHealth and thirteen HMOs and private health insurers signed a memorandum of understanding that makes PhilHealth the first payer for primary care under its YAKAP program, with the HMO or insurer paying eligible costs beyond PhilHealth&rsquo;s limits.[[pc_news2026_yakap_hmo]][[pc_news2026_yakap_hmo2]] That agreement covers primary care, not dialysis. But it states the order dialysis units already follow, and most accreditation agreements write it in: apply the PhilHealth benefit first, bill the HMO only for what remains within its contract and the member&rsquo;s plan, and bill the patient only for what neither covers and the patient agreed to.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>PhilHealth</th><th>HMO</th><th>Patient</th></tr></thead>
<tbody>
<tr><td>Covered session within the 156, package items only</td><td>The package pays</td><td>Nothing for items the package already paid</td><td>Nothing (Module 3)</td></tr>
<tr><td>Premium choice the patient agreed to in writing, such as hemodiafiltration</td><td>The package pays its share</td><td>The difference, if the contract and plan cover it and an approval is issued</td><td>Only what remains and was agreed</td></tr>
<tr><td>Sessions after the yearly allocation is used</td><td>None for that year</td><td>May become the first payer, if the plan covers dialysis</td><td>What remains, after a funding conversation</td></tr>
<tr><td>Patient not yet registered in the dialysis database</td><td>Held until registration is verified (Module 2)</td><td>Only if the plan covers it; do not shift PhilHealth&rsquo;s share to the HMO to save time</td><td>Per unit policy, explained in advance</td></tr>
</tbody></table></div>
<p>The last row is a trap. When PhilHealth registration is pending, it is tempting to bill the whole session to the HMO. Unless the contract allows it, that is billing the HMO for a share that belongs to PhilHealth, and the HMO will deduct it later. Ask the claims lead before you do it.</p>
{{formula:<strong>Each peso once.</strong> For every line on the statement, one payer, written down: PhilHealth, the HMO (with its approval code), or the patient (with a signed agreement where required). If a line has two payers, or none, the statement is not ready.}}
{{key:Bill each peso once, to the payer whose turn it is.}}
"""),
    ],
    "debrief": ["""
<p><strong>Treatment today.</strong> Nothing about the card changes it. Mr. Aquino is dialyzed as scheduled. His PhilHealth benefit covers today&rsquo;s session, since he has 15 sessions left this year, and the coverage question is worked out alongside his care.</p>
<p><strong>Before promising anything.</strong> Your unit is not accredited with Sagip Health on today&rsquo;s date, so you cannot bill it as an accredited provider. You also do not know whether his plan covers dialysis. Tell the family plainly and kindly: PhilHealth covers his sessions for now; the HMO question is open; you will tell them by a set date what you find. Ask the claims lead whether the unit is renewing with Sagip Health, and whether the plan allows reimbursement to the member for care at a non-accredited unit.</p>
<p><strong>Why 141 matters.</strong> At three sessions a week, his remaining 15 sessions run out in about five weeks, before the end of the year. After that, an HMO that covers dialysis would become the first payer. That is exactly when coverage needs to be settled, so start now (Calculator 2 projects the date).</p>
"""],
    "skills": {"title": "Payer profile",
               "intro": "Build a payer profile for one fictional HMO from a sample accreditation agreement, then check a card against it.",
               "items": [
                   ("Confirms the HMO&rsquo;s certificate of authority on the Insurance Commission&rsquo;s current list and records the date checked.", True),
                   ("Confirms the unit&rsquo;s accreditation is in force on the service date.", True),
                   ("Copies the eight claims clauses from the signed agreement, with dates and the name of the checker.", False),
                   ("Records an unclear clause as a written question to provider relations, not as a guess.", False),
                   ("Explains the payment order for one session with each line assigned to one payer.", False),
                   ("States that treatment proceeds while coverage is unresolved.", True),
               ],
               "placement": "Review your unit&rsquo;s payer profiles with the claims lead and mark any clause that no longer matches the signed agreement."},
    "quiz": [
        ("Which government agency now regulates and supervises HMOs in the Philippines?",
         ["The Department of Health", "The Insurance Commission", "PhilHealth", "The Department of Labor and Employment"], 1,
         "Executive Order No. 192 (2015) moved HMO regulation to the Insurance Commission."),
        ("How do you confirm that an HMO is licensed to operate?",
         ["Ask the member", "Check the Insurance Commission&rsquo;s list of HMOs with certificates of authority", "Look at the card design", "Call any hospital"], 1,
         "The Commission publishes and updates the list."),
        ("Under Circular Letter 2024-01, which is an unsound business act?",
         ["Asking for a valid ID", "Denying a claim without reasonable investigation of the available documents", "Paying a claim early", "Issuing a letter of authorization"], 1,
         "Denials must rest on a reasonable investigation."),
        ("Circular Letter 2024-01 requires an HMO to act on a letter of authorization within what period?",
         ["24 hours", "A reasonable time after all required documents are submitted", "30 days", "It sets no standard"], 1,
         "The circular says reasonable time; your contract gives the number of days."),
        ("Where does the number of days an HMO has to pay your unit usually come from?",
         ["The member&rsquo;s card", "The payment term in the accreditation agreement", "PhilHealth&rsquo;s filing rule", "The call-center agent"], 1,
         "The signed agreement governs."),
        ("A patient shows a valid HMO card. What does it prove?",
         ["That dialysis is covered", "Membership in a plan, not dialysis coverage or your unit&rsquo;s accreditation", "That the HMO will pay today", "That PhilHealth is not needed"], 1,
         "Coverage and accreditation are separate checks."),
        ("Why do many HMO plans limit maintenance dialysis?",
         ["Dialysis is rarely needed", "It is lifelong, predictable, and costly, unlike the episodic illness plans are priced for", "The law forbids HMOs from covering it", "PhilHealth asks them to"], 1,
         "Plans are priced for illness that comes and goes."),
        ("The agreement does not say whether professional fees go through the unit. What do you do?",
         ["Assume they do", "Ask provider relations in writing and file the answer in the payer profile", "Bill both ways", "Skip the fees"], 1,
         "Never fill a contract gap with a guess."),
        ("A covered session within the 156, package items only. What does the HMO pay?",
         ["The full session", "Nothing for items the PhilHealth package already paid", "Half", "The professional fee"], 1,
         "Each peso is billed once."),
        ("A patient has used all 156 sessions in October. Who may become the first payer for later sessions that year?",
         ["Nobody", "The HMO, if the plan covers dialysis", "PhilHealth again", "The nephrologist"], 1,
         "After the allocation, PhilHealth pays no more sessions that year."),
        ("PhilHealth registration is pending. Can you bill PhilHealth&rsquo;s share to the HMO to save time?",
         ["Yes, always", "Not unless the contract allows it; ask the claims lead", "Yes, if the family agrees", "Yes, in December"], 1,
         "The HMO will deduct a share that belongs to PhilHealth."),
        ("What did the October 1, 2026 PhilHealth memorandum with HMOs and insurers establish?",
         ["HMOs replace PhilHealth for dialysis", "PhilHealth as the first payer for primary care under YAKAP, with HMOs paying beyond its limits", "Free dialysis in all HMOs", "A new filing deadline"], 1,
         "It covers primary care; dialysis units already follow the same order."),
        ("The HMO has not approved coverage yet and the patient is due on the chair. What happens?",
         ["Wait for approval", "Treatment goes ahead under unit policy while coverage is worked out", "Send the patient home", "Reschedule next week"], 1,
         "Coverage never delays treatment."),
        ("What did the cohort studies on missed hemodialysis sessions show?",
         ["Proof that each missed session causes death", "An association between missed sessions and more hospitalization and death", "No relationship", "Benefit from skipping sessions"], 1,
         "Observational studies show association, not proof of cause."),
        ("A statement line has two payers listed. What does that mean?",
         ["It is fine", "The statement is not ready; each line needs one payer", "Split it evenly", "Send it to both"], 1,
         "One line, one payer."),
    ],
    "terms": [("Certificate of authority", "The Insurance Commission&rsquo;s license that allows an HMO to operate."),
              ("Accreditation agreement", "The signed contract between your unit and one HMO."),
              ("Payer profile", "A one-page, dated summary of one HMO&rsquo;s claims rules taken from the signed agreement."),
              ("Maximum benefit limit", "The most a plan pays for a member in a set period."),
              ("Pre-existing condition", "An illness that began before the member&rsquo;s coverage started."),
              ("First payer", "The payer whose benefit is applied before any other.")],
    "readings": [("hmo-ckd-coverage.html", "Why HMOs often limit kidney care, explained for patients and families."),
                 ("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
