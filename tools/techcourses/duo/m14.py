# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 14: PhilHealth participation and benefit stewardship. Written for this course from published sources."""

MODULE = {
    "image_alt": "A billing officer at a clinic counter explaining a printed benefit form to an older couple; the wife holds a small notebook.",
    "objectives": [
        "State the current PhilHealth hemodialysis package and what it includes.",
        "Describe the conditions that must all hold before a session is paid.",
        "Explain why covered sessions carry no co-payment, when an additional service may, and present it in writing before the first session.",
        "Plan with patients for the yearly session limit.",
    ],
    "big": """
{{plain:The PhilHealth package is like a scholarship that pays tuition per class attended, up to a yearly limit. The school is paid only if the student is enrolled, the class happened, the attendance sheet is signed, and the claim is filed on time.}}
<p>The picture has a limit. A student who misses class loses a lesson. A dialysis patient who misses a session risks a hospital admission. That is why the unit must treat every scheduled session as care first and revenue second, and why charges to patients must be clear before the first session, not after.</p>
{{cards:Key terms for this module|Package rate::The amount PhilHealth pays per hemodialysis session.|PhilHealth Dialysis Database (PDD)::The registry a patient must be in before hemodialysis claims are paid.|Agreement form::The form the patient signs for each session, which states the package.|Co-payment::An amount the patient pays in addition to the package, only where the rules allow.|Session limit::The maximum number of sessions the package covers in a calendar year.}}
<p>Your work is to steward a public benefit honestly: claim what was delivered, charge only what is allowed and disclosed, and help patients plan for the limit.</p>
""",
    "case": {"title": "Why are we still paying?", "html": """
<p>Mr. and Mrs. Felipe Navarro, both in their sixties, come to the front desk of a unit in Marikina. Mr. Navarro has dialyzed three times a week since January. They read in the news that PhilHealth now pays &ldquo;almost a million pesos a year,&rdquo; yet the unit charges them 650 pesos per session. Their daughter asks whether the unit is allowed to do that.</p>
""", "questions": ["What does the package include?", "What should the family have been told before the first session?", "What happens late in the year?"]},
    "sections": [
        ("package", "The package", "The hemodialysis package", """
{{fig:duo14a}}
<p>Under PhilHealth Circular No. 2024-0023, the hemodialysis (HD) package is 6,350 pesos per session for members and qualified dependents with chronic kidney disease stage 5, for up to 156 sessions a calendar year.[[dch_philhealth2024]][[duo_ph_news2025]] The package <strong>includes both the facility fee and the professional fee</strong>; the agreement form the patient signs says so.[[duo_ph_agreement]] At 156 sessions, PhilHealth pays up to 990,600 pesos a year per patient. That ceiling is arithmetic, not guaranteed revenue and not profit.</p>
<p>PhilHealth covers peritoneal dialysis (PD) and transplant through separate packages. Some public pages still carry older wording, including an earlier limit of 90 sessions. Where pages disagree, the circular prevails. Check for amendments before you set prices each year.</p>
{{key:6,350 pesos per session, facility and professional fees included, up to 156 sessions a year. Confirm it against the current circular every year.}}
"""),
        ("eligibility", "Eligibility", "When a session is paid", """
<p>A session is paid only when every link holds: the patient is an eligible member or dependent registered in the PhilHealth Dialysis Database (PDD); the facility is accredited; the session was delivered and documented; the agreement form was signed; and the claim was filed on time.[[pc_pa2016_0030]][[dch_philhealth2023acc]] Break any link and the claim fails. Module 15 follows the chain to the bank.</p>
<p>Register new patients in the PDD early, ideally before the first session, and check eligibility monthly. A patient who loses eligibility should hear it from the unit, early, with help from a social worker, not discover it at the counter.</p>
{{key:Check every link before you count a session as revenue.}}
"""),
        ("charges", "Charges", "What a patient may be charged", """
{{fig:duo14b}}
<p>The package is meant to cover the minimum standard of hemodialysis care with <strong>no co-payment</strong>. When PhilHealth announced the 6,350-peso rate, it said the increase was approved so that patients would pay nothing extra for that minimum set of services, which the circular lists: the session itself, the dialyzer, solutions and supplies, anticoagulation, anemia medicines, and specified laboratory tests.[[dch_philhealth_news2024]][[dch_philhealth2024]] A covered session therefore carries no charge to the patient above the package.</p>
<p>Co-payment is allowed only for additional or premium services beyond that minimum standard, and the facility must fully explain any such co-payment to the patient. Where a patient needs an additional professional service, such as a teleconsultation or an immediate intervention for a complication during the session, the professional fee co-payment is capped at 450 pesos and recorded on the agreement form.[[dch_philhealth_news2024]][[dch_philhealth2024]] Neither is an automatic per-session surcharge.</p>
<p>The fair practice is simple: give every patient a written estimate before the first session, showing that covered sessions cost them nothing extra, which additional or premium services could carry a co-payment and why, and what happens beyond the yearly limit. Use the patient-share calculator to show the yearly total. If a family cannot read the estimate, explain it in their language and give them a copy.</p>
{{stop:Never charge a patient for services the package covers, and never apply an automatic surcharge to every session.}}
{{key:No co-payment for covered services. Anything extra is optional, explained, written, and before the first session.}}
"""),
        ("limits", "The yearly limit", "Planning for the limit", """
<p>A patient on three sessions a week needs about 156 sessions in a 52-week year, so the limit fits a normal schedule closely. Extra sessions for fluid overload or a 53rd week can push a patient past it. Track each patient&rsquo;s sessions used and tell the patient and family early if the count will run out before December 31, with a social worker&rsquo;s help to find other support.</p>
<p>Dialysis continues regardless. A patient who reaches the limit still needs every session, and the clinical decision about how often to dialyze is never changed to fit the package.</p>
{{key:Track sessions used for every patient. Warn early; never shorten care to fit the limit.}}
"""),
    ],
    "debrief": ["""
<p><strong>What the package includes.</strong> 6,350 pesos per session, with both the facility and professional fees, up to 156 sessions a year.</p>
<p><strong>The 650 pesos.</strong> A flat charge on every covered session is not allowed: the package covers the minimum standard of care with no co-payment. Stop it today. Review each session with the billing officer and the clinical head; refund every amount that was charged for covered services. A co-payment is possible only for an additional or premium service the patient actually received and was told about in advance, and an additional professional fee may not exceed 450 pesos.</p>
<p><strong>Before the first session.</strong> A written estimate showing all of this, explained in the family&rsquo;s language.</p>
"""],
    "skills": {"title": "Payer participation checklist and patient charge matrix",
               "intro": "Build a charge matrix for your unit and test it with a mock family conversation.",
               "items": [("States the package rate, inclusions, and session limit from the current circular.", False),
                         ("Lists each link that must hold before a session is paid.", False),
                         ("Removes any automatic surcharge and any charge for covered services.", True),
                         ("Gives a written estimate before the first session.", True),
                         ("Tracks sessions used per patient and warns early about the limit.", False),
                         ("Confirms that dialysis frequency is never changed to fit the package.", True)],
               "placement": "Read three patients&rsquo; agreement forms and check each charge against the circular."},
    "quiz": [
        ("What is the PhilHealth hemodialysis package per session under Circular 2024-0023?",
         ["2,600 pesos", "4,000 pesos", "6,350 pesos, including facility and professional fees", "6,350 pesos, facility fee only"],
         2, "The package includes both the facility and professional fees."),
        ("How many sessions a year does the package cover?",
         ["90", "104", "156", "Unlimited"],
         2, "Up to 156 sessions per calendar year."),
        ("A unit adds a flat 650-peso charge to every covered hemodialysis session. Under the current package, this is:",
         ["Allowed for private units", "Not allowed: covered minimum services carry no co-payment", "Allowed if PhilHealth pays late", "Required for professional fees"],
         1, "The package covers the minimum standard of care with no co-payment. A co-payment applies only to additional or premium services, explained in advance, with additional professional fees capped at 450 pesos."),
        ("When should a patient receive a written estimate of charges?",
         ["After the first month", "Before the first session", "Only if they ask", "At the end of the year"],
         1, "Charges are disclosed before care begins."),
        ("A patient will reach the 156-session limit in November. What should the unit do?",
         ["Reduce sessions to two a week", "Warn early, involve a social worker, and continue dialysis as prescribed", "Discharge the patient", "Charge double"],
         1, "Care is not changed to fit the package."),
        ("Which link is required before a hemodialysis claim is paid?",
         ["Registration in the PhilHealth Dialysis Database", "A hospital admission", "A transplant referral", "A doctor&rsquo;s letter to the media"],
         0, "Registration in the PDD is one of the required links."),
    ],
    "terms": [("Qualified dependent", "A family member covered under a member&rsquo;s PhilHealth benefits.")],
    "readings": [("zero-balance-billing-philhealth.html", "What zero balance billing means for patients."),
                 ("philhealth-z-packages.html", "PhilHealth packages for kidney transplant and peritoneal dialysis.")],
    "calcs": ["calc-dialysis-owner-toolkit.html#c8", "calc-dialysis-clinical-head-toolkit.html#c5"],
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
