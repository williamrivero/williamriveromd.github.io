# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 13: HMO Verification, Letters of Authorization, and the HMO Claim.
Part 6 (HMO claims and collections), added November 26, 2026. Every HMO, patient, staff name, rate, and code here
is fictional; contracted rates and validity periods come from each unit's own agreements."""

MODULE = {
    "image_alt": "A clerk at an intake desk reads an approval code from a laptop screen while a patient waits with her health card and ID, a nurse preparing a dialysis chair behind them.",
    "objectives": [
        "Verify HMO membership, plan coverage, and the unit&rsquo;s accreditation as separate checks, with a reference for each.",
        "Request, read, and file a letter of authorization, and act correctly when it is pending, denied, capped, or expired.",
        "Split a session&rsquo;s charges among PhilHealth, the HMO, and the patient, with each line billed once.",
        "Assemble an HMO claim batch with a transmittal, control totals, and proof of receipt, filed once within the contract period.",
        "Keep a patient&rsquo;s treatment separate from an HMO approval problem.",
    ],
    "big": """
{{plain:A letter of authorization (LOA) works like a hotel reservation confirmation. It has a number, a date range, and a spending limit. Show it at check-in and the bill goes to the company that booked the room, up to the limit. Arrive a day after the dates on it, or run up a bill past the limit, and the company will not pay the difference.}}
<p>The picture has a limit. A hotel can turn a guest away; a dialysis unit does not turn away a patient whose LOA has lapsed. The LOA decides who pays, never whether the session happens. It also does not decide what the patient needs: the treating team does. The LOA only records what the HMO agreed to pay for, for whom, for how long, and up to how much.</p>
<p>Most HMO disallowances at a dialysis unit trace back to the first two minutes at the desk: a card not checked against the plan, an LOA that expired over the weekend, an approved amount lower than the bill, or a PhilHealth share left on the HMO&rsquo;s line. Your work in this module is to make those minutes count, then build a claim the HMO can pay without asking for anything more.</p>
{{fig:pc_hmo_loa}}
{{cards:Key terms for this module|Verification::Confirming, with a reference number, that the member is active, the plan covers the service, and your unit is accredited.|Letter of authorization::The HMO&rsquo;s approval: a code, the member, the service, validity dates, and an approved amount.|Approved amount::The most the HMO will pay under that LOA.|Period LOA::One approval covering several sessions over a set period, when the contract allows it.|Transmittal::The list that goes with a claim batch: every claim, its amount, and the batch total.|Proof of receipt::The HMO&rsquo;s stamped copy, portal receipt, or email acknowledging the batch.}}
""",
    "case": {"title": "Monday, and the approval ended Friday", "html": """
<p>Mrs. Teresita Ramos (fictional, SIM-13), 58, has maintenance HD every Monday, Wednesday, and Friday. Her employer&rsquo;s plan with &ldquo;Kalinga Care&rdquo; (a fictional HMO) pays the hemodiafiltration difference she chose with her nephrologist, under a period LOA. It is Monday, November 3. The clerk, Grace Villanueva, sees that the LOA&rsquo;s validity ended on Friday, October 31. Kalinga Care&rsquo;s portal is down. Mrs. Ramos is already being weighed at the scale, and the nurse is preparing her chair.</p>
<p>Her bill per session has three parts: the PhilHealth package of 6,350 pesos, a 1,500-peso hemodiafiltration difference she agreed to in writing, and a 250-peso blanket rental she asked for that her plan does not cover.</p>
""", "questions": ["What happens to Mrs. Ramos&rsquo;s session this morning?",
                  "What do you do about the expired LOA, and what do you tell her?",
                  "How is today&rsquo;s bill split, and which line is at risk?"]},
    "sections": [
        ("verify", "Verification", "Three checks before the first session", """
<p>In Module 2 you kept PhilHealth eligibility and dialysis-database registration as separate checks. HMO verification works the same way: three questions, three answers, three references. A yes to one never answers the others.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>How you check</th><th>What you record</th></tr></thead>
<tbody>
<tr><td>Is the member active today?</td><td>Card and a valid ID, then the HMO portal or hotline</td><td>Coverage dates, reference number, time, and the agent&rsquo;s name if by phone</td></tr>
<tr><td>Does the plan cover this service here?</td><td>Plan benefits for outpatient dialysis or the premium item, the maximum benefit limit and what is left of it, and any exclusion</td><td>Benefit, remaining limit, and the source of the answer</td></tr>
<tr><td>Is your unit accredited with this HMO today?</td><td>Your payer profile (Module 12)</td><td>Agreement in force, and the date you checked</td></tr>
</tbody></table></div>
<p>Repeat the checks whenever the year turns, the employer changes plans, the member changes jobs, or the PhilHealth allocation is about to run out. A plan that paid in March can end in April when an employer switches HMOs.</p>
{{key:A card is a question, not an answer. Verify membership, coverage, and accreditation separately, and write down where each answer came from.}}
"""),
        ("loa", "The LOA", "Reading and keeping the letter of authorization", """
<p>Request the LOA through the channel your payer profile names, before the service when the contract requires it. When it arrives, read it against the patient in front of you, field by field:</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Check</th></tr></thead>
<tbody>
<tr><td>Member name and number</td><td>Matches the card and the ID exactly</td></tr>
<tr><td>Service</td><td>Matches what will be billed, for example the hemodiafiltration difference, not &ldquo;consultation&rdquo;</td></tr>
<tr><td>Validity dates</td><td>Cover every session you will bill under it; note the last valid date in the schedule</td></tr>
<tr><td>Number of sessions or approved amount</td><td>Not lower than what you will bill; if it is, the excess is not the HMO&rsquo;s</td></tr>
<tr><td>Approval code</td><td>Copied exactly onto the claim</td></tr>
</tbody></table></div>
<p><strong>When the LOA is pending, denied, capped, or expired.</strong> The session goes ahead. Tell the patient in plain words what is not yet approved and what your unit&rsquo;s payment policy says will happen if approval does not come. Record that conversation. Request the LOA, or its renewal, at once, and write down the time of each request and each answer. If the HMO is slow to act on a complete request, escalate through provider relations: the Insurance Commission treats failing to issue or deny an LOA within a reasonable time after the required documents are submitted as an unsound business act.[[pc_ic_cl2024_01]]</p>
<p>Set reminders before every LOA&rsquo;s last valid date, the same way you set reminders before accreditation expires (Module 9). A period LOA that ends on a Friday is a Monday problem unless someone renewed it on Wednesday.</p>
{{call:Never ask a patient to sign a blank claim or availment form, and never change the dates on an LOA. If the dates do not cover the session, request a new one.}}
"""),
        ("split", "Splitting the bill", "Splitting one session among three payers", """
<p>Build the statement line by line, and give each line one payer (Module 12). PhilHealth&rsquo;s package comes first. The HMO&rsquo;s line is limited by three things at once: what the contract allows, what the member&rsquo;s plan covers, and what the LOA approved. The patient&rsquo;s line holds only what neither covers and the patient agreed to.</p>
{{formula:<strong>Worked example (fictional rates).</strong> One session: PhilHealth package 6,350 pesos. Hemodiafiltration difference 1,500 pesos, agreed in writing; the plan covers it and the LOA approves up to 1,500 pesos per session: the HMO line is 1,500 pesos. Blanket rental 250 pesos, requested by the patient and not covered: the patient line is 250 pesos. Total 8,100 pesos: 6,350 PhilHealth, 1,500 HMO, 250 patient. If the LOA had approved only 1,200 pesos, the HMO line would be 1,200, and the other 300 would need a decision under the patient&rsquo;s signed agreement and your unit&rsquo;s policy, not a quiet move onto the HMO claim.}}
<p>Calculator 7 in the claims toolkit does this split. It also subtracts the HMO line from the member&rsquo;s remaining maximum benefit limit, so you can see weeks ahead when the plan will run out and start the conversation with the patient and social service early.</p>
<p>Two lines need special care. A covered, indicated item inside the PhilHealth package never goes on the HMO line or the patient line (Module 3). And the nephrologist&rsquo;s professional fee goes wherever the payer profile says: through the unit or billed directly by the doctor, never both.</p>
{{key:The HMO line is the smallest of three numbers: what the contract allows, what the plan covers, and what the LOA approved.}}
"""),
        ("packet", "The claim batch", "Building and filing the HMO claim batch", """
<p>HMOs are usually billed in batches: one batch per HMO, per period, with a transmittal on top. The HMO checks the batch against its approvals line by line. Anything it cannot trace is deducted, so build the batch so every line traces to its source, as you did for PhilHealth in Module 5.</p>
{{fig:pc_hmo_batch}}
<div class="table-wrap"><table>
<thead><tr><th>In every claim</th><th>Source</th></tr></thead>
<tbody>
<tr><td>LOA copy or approval code, valid on each service date</td><td>The LOA file</td></tr>
<tr><td>Itemized statement showing the PhilHealth deduction, the HMO share, and the patient share</td><td>Billing system</td></tr>
<tr><td>Signed availment or claim form for each session, when the HMO requires it</td><td>Signed at the session, never later</td></tr>
<tr><td>Treatment record or physician&rsquo;s certification, when the contract requires it</td><td>Nursing and the nephrologist</td></tr>
</tbody></table></div>
<p><strong>The transmittal</strong> lists every claim with the member, service dates, approval code, and amount, and ends with a control total: the number of claims and the batch amount. Keep a copy. <strong>Proof of receipt</strong> is the HMO&rsquo;s stamped transmittal, portal receipt, or acknowledgment email, with the date. Without it, you cannot prove you filed on time, and your aging clock has no start point (Module 14).</p>
<p>File within the contract&rsquo;s filing period, and set an internal target well before it, as you do for PhilHealth (Module 6). If you are not sure a batch arrived, ask the HMO for its status before you send it again. A batch sent twice creates duplicate claims, and duplicates are slow and awkward to unwind.</p>
{{key:One batch, one transmittal, one proof of receipt, filed once, within the contract period.}}
"""),
    ],
    "debrief": ["""
<p><strong>The session.</strong> Mrs. Ramos is dialyzed this morning as planned. The expired LOA is a payment question for the desk, not a reason to delay her treatment.</p>
<p><strong>The expired LOA.</strong> Request the renewal through Kalinga Care&rsquo;s backup channel in the payer profile (hotline or email) now, and record the time and reference. Tell Mrs. Ramos, in plain words, that her approval needs renewing, that her dialysis continues, and what your unit&rsquo;s policy says about today&rsquo;s hemodiafiltration difference if the renewal does not cover today. Record the conversation. Add a reminder before the next LOA&rsquo;s last valid date, and ask why the renewal was not requested last Wednesday.</p>
<p><strong>The split.</strong> 6,350 pesos to PhilHealth, 1,500 pesos to Kalinga Care only if the renewed LOA covers November 3, and 250 pesos to Mrs. Ramos for the blanket she asked for. The 1,500-peso line is at risk: do not file it under the expired LOA.</p>
"""],
    "skills": {"title": "HMO intake and claim batch",
               "intro": "Verify a fictional HMO member, read an LOA, split three sessions, and build a five-claim batch with a transmittal.",
               "items": [
                   ("Records membership, plan coverage, and accreditation as three checks with references.", True),
                   ("Reads every LOA field against the patient and flags a validity gap before the session date.", True),
                   ("Proceeds with treatment and records a plain-language payment conversation when the LOA is not in force.", True),
                   ("Splits each session into PhilHealth, HMO, and patient lines, with the HMO line capped by the LOA.", False),
                   ("Builds a transmittal with control totals that match the claims.", False),
                   ("Files once within the contract period and keeps proof of receipt.", True),
               ],
               "placement": "Shadow one HMO intake and one batch submission at your unit, and compare them with the payer profile."},
    "quiz": [
        ("Which three checks make up HMO verification?",
         ["Name, age, address", "Active membership, plan coverage for the service, and your unit&rsquo;s accreditation", "PIN, PDD, CF1", "Card, photo, signature"], 1,
         "Each answer needs its own reference."),
        ("An LOA&rsquo;s validity ended Friday; the patient is due Monday. What happens to the session?",
         ["Cancelled", "It goes ahead; the desk works on the renewal and explains the payment policy", "Delayed until approval", "Moved to next week"], 1,
         "The LOA decides who pays, not whether the session happens."),
        ("The LOA approves 1,200 pesos; the HMO share on the bill is 1,500 pesos. What is the HMO line?",
         ["1,500 pesos", "1,200 pesos; the 300 needs a decision under the patient&rsquo;s agreement and unit policy", "Zero", "1,350 pesos"], 1,
         "The HMO line is capped by the LOA."),
        ("PhilHealth package 6,350, hemodiafiltration difference 1,500 (covered and approved), uncovered blanket 250. What is the split?",
         ["8,100 to the HMO", "6,350 PhilHealth, 1,500 HMO, 250 patient", "6,350 PhilHealth, 1,750 HMO", "7,850 PhilHealth, 250 patient"], 1,
         "Each line has one payer."),
        ("The dates on the LOA do not cover a session. What do you do?",
         ["Change the dates", "Request a new LOA; never alter one", "Bill it anyway", "Ask the patient to sign a blank form"], 1,
         "Altered approvals are disallowed and dishonest."),
        ("What should a transmittal end with?",
         ["A thank-you note", "A control total: the number of claims and the batch amount", "The patient&rsquo;s diagnosis", "Nothing"], 1,
         "Control totals let both sides check the batch."),
        ("Why keep proof of receipt for each batch?",
         ["Decoration", "It proves timely filing and starts the aging clock", "The patient wants it", "To send the batch twice"], 1,
         "No receipt, no start point."),
        ("You are not sure a batch reached the HMO. What do you do first?",
         ["Send it again", "Ask the HMO for its status before any resend", "Wait a year", "Bill the patient"], 1,
         "Duplicates are slow to unwind."),
        ("A covered, indicated item inside the PhilHealth package. Which line does it go on?",
         ["The HMO line", "The patient line", "Neither; the package already paid it", "Both"], 2,
         "Covered package items are never billed again."),
        ("Under the Insurance Commission&rsquo;s Circular Letter 2024-01, an HMO that sits on a complete LOA request is",
         ["Following normal practice", "Committing an unsound business act by failing to act within a reasonable time", "Allowed up to 90 days", "Not regulated"], 1,
         "Escalate through provider relations with your record of requests."),
        ("When should you repeat HMO verification for a long-term dialysis patient?",
         ["Never", "When the year turns, the plan or employer changes, or the PhilHealth allocation is about to run out", "Only if the HMO calls", "Every session by phone"], 1,
         "Plans change with employers and years."),
        ("Where does the nephrologist&rsquo;s professional fee go on an HMO claim?",
         ["Always through the unit", "Wherever the payer profile says, never billed twice", "Always billed by the doctor", "Onto the patient line"], 1,
         "Contracts differ; the profile records which."),
        ("Why does Calculator 7 track the remaining maximum benefit limit?",
         ["To bill faster", "To see weeks ahead when the plan will run out and start the conversation early", "To report to PhilHealth", "To set the session schedule"], 1,
         "A plan running out is a patient conversation, not a surprise."),
        ("A patient is asked to sign an availment form after three sessions, all at once. What is wrong?",
         ["Nothing", "Forms are signed at each session, never later", "It should be four", "Only the nurse signs"], 1,
         "Signatures must reflect the date of service."),
        ("The HMO line equals the smallest of which three numbers?",
         ["Rate, tax, discount", "What the contract allows, what the plan covers, and what the LOA approved", "Sessions, hours, nurses", "PhilHealth, patient, doctor"], 1,
         "All three limits apply at once."),
    ],
    "terms": [("Letter of authorization", "The HMO&rsquo;s approval for a service, with a code, dates, and an approved amount."),
              ("Period LOA", "One approval for several sessions over a set period."),
              ("Approved amount", "The most the HMO pays under one LOA."),
              ("Transmittal", "The list of claims in a batch, with a control total."),
              ("Control total", "The number of claims and the batch amount, used to check a batch."),
              ("Proof of receipt", "The HMO&rsquo;s dated acknowledgment that a batch arrived.")],
    "readings": [("hmo-ckd-coverage.html", "Why HMOs often limit kidney care, explained for patients and families.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
