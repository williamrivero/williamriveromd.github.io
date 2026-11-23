# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 03: PhilHealth: Accreditation, the Package, and the Claim. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a claims officer comparing a treatment record with a claim printout at a desk in a dialysis clinic.",
    "objectives": [
        "Keep a calendar of license, accreditation, and signatory validity so the unit never treats patients it cannot claim for.",
        "Explain the current PhilHealth hemodialysis benefit in plain words: who qualifies, how many sessions, how much, and what the package must include.",
        "Trace one session from the physician order to the claim, and find the record a discrepancy starts from.",
        "Hold a claim that the records do not support, and correct an error with an audit trail.",
        "Explain a disputed charge to a patient in the language the patient uses at home.",
        "Use returned and denied claims as a quality signal.",
    ],
    "big": """
{{plain:A claim is the last car of a train. It can only be as long and as straight as the cars in front of it: the order, the machine log, the nursing record, the medicine record. If one car is missing, the claim is pulling air.}}
<p>The picture has a limit. A train runs in one direction. Errors in billing often start at the end, in a template or a batch upload, and travel backward into the record when someone &ldquo;fixes&rdquo; the chart to match the claim. The rule runs one way: the claim follows the record, never the reverse.</p>
{{cards:Key terms for this module|PDD::PhilHealth Dialysis Database. Patients with chronic kidney disease stage 5 must be registered to use the hemodialysis benefit.|Package rate::The fixed amount PhilHealth pays per covered session.|Minimum standards::The services, medicines, supplies, and tests a covered session must include.|No copay::The rule that patients are not billed for items within the minimum standards.|Return to hospital (RTH)::A claim sent back for correction or missing documents.|Denial::A claim PhilHealth will not pay.|PRO::PhilHealth Regional Office.}}
""",
    "case": {"title": "The session on two dates", "html": """
<p>Mr. Leonardo Bautista, 61, dialyzes at your unit in Marilao. His treatment record shows a session on 10 November. The claim for that session is dated 11 November. His statement also shows a separate charge for a monthly laboratory panel that the package already includes. Last week a receiving unit in Valenzuela called: Mr. Bautista had two sessions there in October while his daughter was in hospital, which your records do not show.</p>
<p>His son, Mr. Jun Bautista, is at the front desk. &ldquo;We were told there is no copay. Why are we being charged? And will Papa run out of sessions?&rdquo;</p>
""", "questions": ["Which record do you check first, and why?",
                  "What do you tell Mr. Jun Bautista today, before the records are reconciled?",
                  "What must happen to the claim, and to the separate charge?"]},
    "sections": [
        ("benefit", "The benefit", "What the current benefit covers", """
<p>PhilHealth Circular 2024-0023, Revision 2, took effect in October 2024. It covers up to 156 hemodialysis sessions a year, three a week, for members and qualified dependents with chronic kidney disease stage 5 registered in the PDD, at a package rate of 6,350 pesos per session, or up to 990,600 pesos a year.[[dch_philhealth2024]][[dch_philhealth_news2024]] Earlier revisions set lower rates during 2024; always apply the rules in force on the date of treatment.</p>
<p>The package is designed for no copay for its minimum standards. PhilHealth&rsquo;s advisory on the first revision clarified that coverage applies to the services listed in the circular&rsquo;s minimum-standards table, that their provision depends on the patient&rsquo;s clinical assessment, and that the no-copay provision applies to them.[[dch_philhealth_pa2024]] A separate circular, 2024-0029, sets out quality standards for maintenance hemodialysis that PhilHealth uses as its reference.[[dch_philhealth2024q]]</p>
{{fig:dch03_package}}
<p>Read the minimum-standards table yourself, with your billing lead. Then check that the unit&rsquo;s charge master cannot bill separately for anything inside it. A charge for an included item is a billing error, however it is labeled.</p>
{{fig:dch03_calendar}}
{{formula:<strong>Session arithmetic.</strong> 3 sessions a week &times; 52 weeks = 156. At 6,350 pesos each, 156 sessions = 990,600 pesos. A patient who needs a fourth weekly session for six weeks after a hospitalization uses 6 extra sessions and will run short near the end of the year. Calculator 5 projects the date.}}
{{key:Coverage rules decide who pays. They never decide whether a patient is dialyzed today.}}
"""),
        ("status", "Provider status", "Keep the unit claimable", """
<p>A session delivered on a day the license, the accreditation, or a signatory&rsquo;s authority had lapsed may not be payable, however good the care. Build one calendar for all of them.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Owner</th><th>What to watch</th></tr></thead>
<tbody>
<tr><td>Department of Health (DOH) License to Operate</td><td>Compliance lead</td><td>Expiry, scope, and any change that needs approval (Module 2)</td></tr>
<tr><td>PhilHealth accreditation</td><td>Compliance lead</td><td>The renewal filing window, the provider data record, the notarized performance commitment, and the fee[[dch_philhealth2023acc]][[dch_philhealth_pa2025]]</td></tr>
<tr><td>Authorized signatories</td><td>Owner</td><td>Who may sign claims and certifications, and their validity</td></tr>
<tr><td>Patient registration</td><td>Claims lead</td><td>PDD registration for every new patient before the first claim</td></tr>
<tr><td>Session counts</td><td>Claims lead</td><td>Sessions used per patient across every unit the patient visited</td></tr>
</tbody></table></div>
<p>Confirm the current accreditation cycle and filing dates with your PRO. Filing windows change from year to year.</p>
"""),
        ("trace", "The trace", "The chart-to-claim trace", """
{{fig:dch03_trace}}
<p>Every month, pick five sessions at random and follow each one from the order to the claim. Start from the entry made at the time of treatment, because that is the record least likely to have been edited.</p>
{{flow:The trace, one session|1. Eligibility::PDD registration and sessions remaining on the date of service.|2. Order::A current, signed prescription for that session.|3. Delivery::Machine log and nursing record agree on date, start and end times, and fluid removed.|4. Medicines and tests::Recorded as given or done, and inside the package where required.|5. Itemization::The statement shows no separate charge for an included item.|6. Claim::Date, patient, and session match the treatment record.}}
<p>When a claim is returned or denied, classify the reason. Compare it with the contemporaneous records. Correct a supported administrative error with an audit trail that shows the original entry, the correction, who made it, and when. Never change a clinical record to fit a claim. Send anything uncertain to the claims supervisor and hold it.</p>
{{call:Stop and hold any claim that the treatment record does not support. Escalate a suspected pattern of billing errors to the owner and compliance lead in writing. Do not submit to meet a deadline.}}
"""),
        ("patient", "Talking with the patient", "Explaining a disputed charge", """
<p>Patients and families often hear about billing before they hear about anything else. A clear, early explanation in the language they use at home prevents a dispute from becoming a reason to stop coming.</p>
<div class="table-wrap"><table>
<thead><tr><th>Say</th><th>Avoid</th></tr></thead>
<tbody>
<tr><td>&ldquo;That charge looks wrong to us too. We are checking it, and we will tell you by Friday.&rdquo;</td><td>&ldquo;That is how the system works.&rdquo;</td></tr>
<tr><td>&ldquo;If it was charged by mistake, we will reverse it or refund it.&rdquo;</td><td>Promising a refund before the record is checked</td></tr>
<tr><td>&ldquo;Your father&rsquo;s dialysis continues while we sort this out.&rdquo;</td><td>Linking treatment to payment</td></tr>
<tr><td>&ldquo;Here is how to file a complaint if you are not satisfied.&rdquo;</td><td>Leaving the family without a route</td></tr>
</tbody></table></div>
<p>Count sessions across units. Patients who dialyze elsewhere while traveling, or after a transfer, use the same annual allocation. Ask about other units at every transfer and every return.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Which record first?</strong> The treatment record made at the time of the session: the machine log and nursing note for 10 November. If they confirm treatment on 10 November, the claim date is an administrative error to correct with an audit trail. If the records disagree with each other, hold the claim and investigate before anything is submitted.</p>
<p><strong>What to tell Mr. Jun Bautista today.</strong> That the separate laboratory charge appears to be for an item the package already includes, that you are checking it, and that it will be reversed or refunded if confirmed, with a date. That his father&rsquo;s dialysis continues regardless. That the two October sessions in Valenzuela count toward the 156, and you will work out with him how many remain.</p>
<p><strong>The claim and the charge.</strong> Verify utilization through the approved PhilHealth channel, including the Valenzuela sessions. Hold the discrepant claim until the dates are reconciled. Reverse the laboratory charge if confirmed, and find out how the billing template allowed it. Then check five more statements for the same error.</p>
"""],
    "skills": {"title": "Chart-to-claim trace and patient explanation",
               "intro": "Trace three fictional sessions from order to claim, then explain one discrepancy to a preceptor playing a family member.",
               "items": [
                   ("Checks PDD registration and sessions remaining on the date of service.", False),
                   ("Starts from the contemporaneous treatment record.", True),
                   ("Matches order, machine log, nursing record, medicines, itemization, and claim.", False),
                   ("Identifies a separate charge for a package-included item as an error.", True),
                   ("Holds an unsupported claim and escalates the possible billing error.", True),
                   ("Corrects an administrative error with an audit trail, without altering the clinical record.", True),
                   ("Explains the charge in plain language, gives a date, and states that treatment continues.", False),
                   ("Provides the complaint route.", False),
                   ("Counts sessions delivered at other units.", False),
               ],
               "placement": "Trace five sessions at your unit this month. Present the results and any template or process defect you found to your claims lead."},
    "quiz": [
        ("How many hemodialysis sessions a year does the current PhilHealth benefit cover for eligible patients?",
         ["90", "144", "156", "Unlimited"], 2,
         "156 sessions, three a week for a year."),
        ("What is the package rate per covered session under Circular 2024-0023?",
         ["2,600 pesos", "4,000 pesos", "6,350 pesos", "9,000 pesos"], 2,
         "The rate rose in steps during 2024 to 6,350 pesos."),
        ("Which circular sets quality standards PhilHealth uses as its reference for maintenance hemodialysis?",
         ["2024-0023", "2024-0029", "2023-0012", "2025-0055"], 1,
         "2024-0023 sets the benefit; 2024-0029 the quality reference."),
        ("Where does a chart-to-claim trace start?",
         ["The claim", "The billing template", "The record made at the time of treatment", "The patient&rsquo;s memory"], 2,
         "The contemporaneous record is least likely to have been edited."),
        ("The statement shows a separate charge for a test inside the package. What is it?",
         ["An allowed extra", "A billing error to reverse or refund if confirmed", "A copay", "A donation"], 1,
         "No-copay rules make included items non-billable."),
        ("A session appears on the schedule but the treatment record is missing. What do you do with the claim?",
         ["Submit it", "Hold it until the source evidence is reconciled", "Submit and fix later", "Delete the schedule"], 1,
         "Claims follow records."),
        ("How should an administrative error in a claim be corrected?",
         ["Overwrite it", "With an audit trail showing original, correction, author, and time", "Verbally", "By editing the clinical record to match"], 1,
         "Never change a clinical record to fit a claim."),
        ("A patient had two sessions at another unit in October. Why does it matter?",
         ["It does not", "They count toward the same annual allocation", "They are paid twice", "They cancel the PDD registration"], 1,
         "Count sessions across units."),
        ("A family asks whether dialysis will stop while a charge is disputed. What do you say?",
         ["It depends on payment", "Treatment continues while the charge is checked", "Ask PhilHealth", "Only if they pay a deposit"], 1,
         "Coverage never decides whether a patient is dialyzed today."),
        ("Which is the PRO?",
         ["The Philippine Renal Organization", "The PhilHealth Regional Office", "The patient relations officer", "The private renal office"], 1,
         "Confirm accreditation cycles with your PRO."),
        ("Twelve claims are returned for the same missing signature. What is this?",
         ["Bad luck", "A process defect to fix at the step that let them leave", "A reason to stop claiming", "An inspection finding"], 1,
         "Returned claims are a quality signal."),
        ("A patient on four sessions a week for six weeks after a hospitalization will likely:",
         ["Lose PDD registration", "Run short of covered sessions near year end", "Be charged a copay immediately", "Need a new accreditation"], 1,
         "Six extra sessions come out of the same 156."),
        ("What must be in place before the first claim for a new patient?",
         ["A transplant referral", "PDD registration", "A second nephrologist", "A water culture"], 1,
         "Registration is a condition of the benefit."),
        ("Who should approve submission when the claim date and the treatment date disagree?",
         ["Nobody until the records are reconciled and the claims supervisor reviews it", "The receptionist", "The patient", "The vendor"], 0,
         "Route uncertainty to the claims supervisor and hold."),
        ("Why keep the license, accreditation, and signatory dates on one calendar?",
         ["Neatness", "A lapse in any one can make delivered sessions unpayable", "PhilHealth requires one calendar", "For the owner&rsquo;s convenience"], 1,
         "Status is a prerequisite for every claim."),
    ],
    "terms": [("PDD", "PhilHealth Dialysis Database."),
              ("Package rate", "The fixed amount paid per covered session."),
              ("Minimum standards", "The services, medicines, supplies, and tests a covered session must include."),
              ("No copay", "Patients are not billed for items within the minimum standards."),
              ("Return to hospital (RTH)", "A claim sent back for correction."),
              ("Denial", "A claim that will not be paid."),
              ("Audit trail", "A record of the original entry, the correction, who made it, and when."),
              ("PRO", "PhilHealth Regional Office.")],
    "readings": [("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
