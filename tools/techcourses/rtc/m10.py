# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 10: PhilHealth and Other Payers. Written for this series from published sources."""

MODULE = {
    "image_alt": "A Z Benefits coordinator explaining a printed cost plan to a recipient and his sister at a hospital billing counter.",
    "objectives": [
        "Explain the difference between clinical clearance, ethics approval, and payer pre-authorization.",
        "Identify the PhilHealth kidney transplant package code and rate that matches a case, under the correct circular version.",
        "Track the 180-day pre-authorization validity and the deceased-donor two-working-day rule.",
        "Estimate the out-of-pocket gap and plan other confirmed assistance, without promising coverage.",
        "Plan affordability across time, including the post-transplant packages and donor monitoring.",
    ],
    "big": """
{{plain:A pre-authorization is like a confirmed hotel booking. It tells you the room is reserved and roughly what you will pay. It does not tell you that your flight will leave on time, that your passport is valid, or that you are well enough to travel. And the booking expires if you arrive too late.}}
{{fig:rtc10_approvals}}
<p>The picture has a limit. A hotel charges one guest. A living-donor transplant involves two people, and the PhilHealth kidney transplant package covers the donor&rsquo;s evaluation, management, and nephrectomy within the recipient&rsquo;s package.[[rtc_ph2026]] At the same time, the DOH living-donor order says the transplant facility must not charge the donor for donation-related medical care and follow-up.[[rtc_doh2021]] So the coordinator plans two people&rsquo;s costs: what the package pays, what the recipient may still owe, and what must never reach the donor.</p>
<p>Your job in this module is to read the package by version, keep its clocks, and help families plan honestly. You do not decide what PhilHealth pays. You make sure the request is complete, on time, and under the right circular, and that nobody mistakes a payment approval for anything else.</p>
{{cards:Key terms for this module|Z Benefits::PhilHealth packages for medically and economically catastrophic conditions, including kidney transplantation.|Contracted facility::A hospital PhilHealth has contracted to provide a Z Benefits package.|Pre-authorization::PhilHealth&rsquo;s approval, before the service, that a case qualifies for the package.|Package code::The code for a specific variant of the package, such as Z025A1.|Co-payment::Any amount the patient may be charged beyond the package, under the contract&rsquo;s terms.|Post-KT package::PhilHealth&rsquo;s separate packages for care after transplant, including immunosuppressants and donor monitoring.}}
""",
    "case": {"title": "The estimate and the calendar", "html": """
<p>Mr. Rommel Aquino, 45, a jeepney operator from Batangas, will receive a kidney from his sister, Ms. Liza Aquino, 40. The team plans laparoscopic donor surgery and basiliximab induction. The hospital&rsquo;s written estimate for the whole admission is 1,200,000 pesos.</p>
<p>The pre-authorization was approved on March 1. Because the donor&rsquo;s psychiatric review was delayed, surgery is now planned for September 15.</p>
<p>Ms. Aquino asks you privately whether she will have to pay for her own tests and operation. Mr. Aquino has a promise of 100,000 pesos from his local government and has applied to the Philippine Charity Sweepstakes Office (PCSO).</p>
""", "questions": ["Which package code applies, and what is the estimated gap before assistance?",
                  "What is wrong with the calendar, and what do you do now?",
                  "What do you tell Ms. Aquino about her costs?"]},
    "sections": [
        ("approvals", "Explain the different approvals", "Payment is not permission", """
<p>Families hear &ldquo;approved&rdquo; once and assume everything is approved. Name each approval and its owner every time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Approval</th><th>Owner</th><th>What it means</th><th>What it does not mean</th></tr></thead>
<tbody>
<tr><td>Clinical clearance</td><td>Transplant team; donor clinicians</td><td>Transplant is medically appropriate for this person</td><td>Payment, consent, or ethics approval</td></tr>
<tr><td>Ethics approval</td><td>HTEC</td><td>The donation is voluntary and unrewarded, with conditions met</td><td>Medical fitness or payment</td></tr>
<tr><td>Pre-authorization</td><td>PhilHealth</td><td>The case qualifies for the package, within its validity</td><td>Medical or ethical clearance; a fixed surgery date</td></tr>
<tr><td>Consent</td><td>The person, with the surgeon</td><td>The person agrees, after understanding</td><td>Any of the above</td></tr>
</tbody></table></div>
{{key:Name the approval and its owner every time you say &ldquo;approved.&rdquo; A payment approval is never a clinical or ethical clearance.}}
"""),
        ("package", "Use the right package, under the right version", "Codes, rates, and clocks", """
<p>PhilHealth&rsquo;s kidney transplant package has eight variants, defined by donor type, induction medicine, and surgical approach. The rates below are in PC 2024-0035 and are unchanged in Revision 1, PC 2026-0019 (published November 21, 2026; effective 15 days after publication).[[rtc_ph2024]][[rtc_ph2026]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Donor</th><th>Induction</th><th>Surgical approach</th><th>Code</th><th>Package rate (PHP)</th></tr></thead>
<tbody>
<tr><td>Living</td><td>Basiliximab or eATG</td><td>Laparoscopic donor, open recipient</td><td>Z025A1</td><td>993,000</td></tr>
<tr><td>Living</td><td>Basiliximab or eATG</td><td>Open donor and recipient</td><td>Z025A2</td><td>865,000</td></tr>
<tr><td>Living</td><td>rATG</td><td>Laparoscopic donor, open recipient</td><td>Z025B1</td><td>1,045,000</td></tr>
<tr><td>Living</td><td>rATG</td><td>Open donor and recipient</td><td>Z025B2</td><td>918,000</td></tr>
<tr><td>Deceased</td><td>Basiliximab or eATG</td><td>Machine perfusion</td><td>Z026A1</td><td>2,093,000</td></tr>
<tr><td>Deceased</td><td>Basiliximab or eATG</td><td>Cold storage</td><td>Z026A2</td><td>1,583,000</td></tr>
<tr><td>Deceased</td><td>rATG</td><td>Machine perfusion</td><td>Z026B1</td><td>2,146,000</td></tr>
<tr><td>Deceased</td><td>rATG</td><td>Cold storage</td><td>Z026B2</td><td>1,636,000</td></tr>
</tbody></table></div>
<p>(eATG and rATG are equine and rabbit antithymocyte globulin, two induction medicines; the team chooses the medicine, and the code follows the choice.)</p>
<p>Two clocks start with the package. An approved pre-authorization is valid for <strong>180 calendar days</strong>. For a living donor, the request is submitted before the package is availed; for a deceased donor, within <strong>two working days after</strong> the procedure.[[rtc_ph2026]] When a surgery date moves, check it against the expiry at once. The <a href="calc-transplant-coordinator-toolkit.html#tool-3">pre-authorization timer</a> in the toolkit does the date arithmetic.</p>
<p>Two rules about people sit around the package. Each contracted facility must have at least one Z Benefits Coordinator, and each may handle at most three Z packages; and cases pre-authorized and performed under PC 2024-0035 are claimed under PC 2024-0035.[[rtc_ph2026]]</p>
{{key:Match the code to the team&rsquo;s plan, record the circular version, and put the 180-day expiry in the register the day approval arrives.}}
"""),
        ("gap", "Estimate the gap honestly", "What the package does not cover", """
<p>A package rate is not the bill. Facility estimates vary with room choice, specialist fees, complications, and length of stay, and the contract may allow co-payment for amenities or upgrades.[[rtc_ph2026]] Give families a written estimate, show the package code and rate beside it, subtract only assistance that is confirmed in writing, and say clearly that the remaining figure is an estimate.</p>
{{formula:Estimated gap = facility estimate &minus; package rate &minus; confirmed assistance}}
<div class="table-wrap"><table>
<thead><tr><th>Possible assistance</th><th>What to confirm</th></tr></thead>
<tbody>
<tr><td>Local government unit (LGU) assistance</td><td>Amount, purpose, and when it is released, in writing</td></tr>
<tr><td>PCSO medical assistance</td><td>Approval letter, amount, and to whom it is paid</td></tr>
<tr><td>DOH Medical Assistance for Indigent and Financially Incapacitated Patients (MAIFIP)</td><td>Eligibility and the hospital&rsquo;s process</td></tr>
<tr><td>Health maintenance organization (HMO) or employer coverage</td><td>What is covered alongside PhilHealth, and the approval</td></tr>
</tbody></table></div>
<p>Promised money is not confirmed money. Count it only when the letter arrives. The <a href="calc-transplant-coordinator-toolkit.html#tool-5">out-of-pocket gap estimator</a> lays this out and reminds you that the donor&rsquo;s donation-related care is not a cost to the donor.</p>
{{key:Subtract only assistance confirmed in writing, and label the result as an estimate.}}
"""),
        ("time", "Plan affordability across time", "The operation is the first bill, not the last", """
<p>The transplant package covers the operation and its admission. Life afterward has its own costs: immunosuppressants every day, prophylaxis, drug-level monitoring, laboratory tests, and sometimes a graft biopsy. PhilHealth&rsquo;s post-kidney transplantation packages for adults (PC 2025-0012) and children (PC 2025-0011) cover these services and list living donor monitoring among them.[[rtc_ph2025a]][[rtc_ph2025c]] Help families see the year ahead: what the post-transplant package covers, where medicines will be dispensed, and what may still be paid out of pocket.</p>
<p>The donor needs the same foresight. Costs for living donors are common: a systematic review of 16 studies found that about 80% of donors had some financial loss, mostly lost income and travel.[[rtc_fu2021]] Ask the donor privately about time off work, travel, and childcare, and link them to support the program can offer. Module 11 covers protection from donation-related charges.</p>
{{key:Plan the first year after transplant and the donor&rsquo;s costs before surgery, not after discharge.}}
"""),
    ],
    "debrief": ["""
<p><strong>The code and the gap.</strong> Living donor, basiliximab, laparoscopic donor surgery: Z025A1, 993,000 pesos. Before assistance, the estimated gap is 1,200,000 minus 993,000, or 207,000 pesos. The local government&rsquo;s 100,000 pesos counts only when confirmed in writing; the PCSO application counts only when approved. Give Mr. Aquino the estimate in writing, labeled as an estimate.</p>
<p><strong>The calendar.</strong> March 1 plus 180 calendar days is August 28. September 15 falls after the pre-authorization expires. Flag it today to the Z Benefits lead and the surgeon by SBAR, and find out from the lead what the circular allows (a new request or an extension). Do not move the surgery date yourself, and do not tell the family the benefit is lost.</p>
<p><strong>Ms. Aquino.</strong> Tell her, privately, that her evaluation and operation are covered within her brother&rsquo;s package and that the facility does not charge donors for donation-related medical care and follow-up. Ask what other costs worry her &mdash; travel, time off work &mdash; and link her to support.</p>
"""],
    "skills": {"title": "Package selection and cost plan",
               "intro": "Prepare a package selection, a pre-authorization timeline, and a written cost plan for a fictional pair while your preceptor observes.",
               "items": [
                   ("Explains clinical clearance, ethics approval, pre-authorization, and consent as four separate approvals.", True),
                   ("Selects the package code from the team&rsquo;s plan and records the circular version.", False),
                   ("Calculates the 180-day expiry and flags a surgery date that falls after it.", True),
                   ("Calculates an estimated gap using only confirmed assistance and labels it as an estimate.", False),
                   ("Explains to a simulated donor, privately, that donation-related care is not charged to the donor.", True),
                   ("Outlines the first year&rsquo;s post-transplant costs and the post-KT package.", False),
               ],
               "placement": "With the Z Benefits lead, review two recent pre-authorizations. Record the approval date, expiry, and surgery date for each."},
    "terms": [("Z Benefits", "PhilHealth packages for catastrophic conditions."), ("Pre-authorization", "Payer approval before the service."),
              ("Package code", "The code for one package variant."), ("Co-payment", "An amount beyond the package allowed by contract."),
              ("LGU", "Local government unit."), ("MAIFIP", "Medical Assistance for Indigent and Financially Incapacitated Patients.")],
    "readings": [("philhealth-z-packages.html", "The patient guide to PhilHealth&rsquo;s dialysis and transplant packages.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-3", "calc-transplant-coordinator-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
