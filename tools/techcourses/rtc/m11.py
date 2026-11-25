# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 11: Claims Evidence, Denials, and Financial Protection. Written for this series from published sources."""

MODULE = {
    "image_alt": "A claims officer and a coordinator comparing a checklist with a claim folder on a desk in a small office.",
    "objectives": [
        "Keep claim evidence aligned with the care actually delivered, starting from admission.",
        "Calculate the 60-day filing deadline and track it with the claims team.",
        "Distinguish a returned claim from a denied claim and route each correctly.",
        "Protect the donor and the recipient from avoidable charges, using the DOH donor expense rule.",
        "Explain what the evidence shows about donor costs and why it matters.",
    ],
    "big": """
{{plain:A claim is like a receipt you must show to be reimbursed for a business trip. The receipt has to match the trip: right dates, right person, right items, filed before the deadline. A missing boarding pass or a receipt filed late can cost the whole reimbursement, even though the trip really happened.}}
{{fig:rtc11_window}}
<p>The picture has a limit. A traveler pays first and gets reimbursed later. In the Z Benefits package the hospital files the claim, and if it is denied, the risk is that the cost lands on a family who was told it was covered &mdash; or, worse, on a donor who should never pay for donating. So claims work is not just paperwork. It is financial protection for two people.</p>
<p>PhilHealth&rsquo;s kidney transplant circular sets the rules: the facility files within 60 days after discharge; PhilHealth processes complete claims within 30 working days; and claims are denied for late filing, missing kidney transplant (KT) registry registration or form, mandatory services not provided, or inconsistent data.[[rtc_ph2026]] Your part is to make sure the evidence exists, matches the care, and reaches the claims team in time.</p>
{{cards:Key terms for this module|Claim::The hospital&rsquo;s request to PhilHealth for payment under the package.|Filing window::The period in which a claim must be filed: 60 days after discharge for this package.|Return::A claim sent back for correction or completion; it can be fixed and resubmitted.|Denial::A decision not to pay, with a stated reason and an appeal route.|Mandatory services::Services the package requires to be provided and documented.|Financial neutrality::The donor neither gains nor loses money because of donation.}}
""",
    "case": {"title": "Day 52", "html": """
<p>Mrs. Erlinda Bautista, 50, received a kidney from her husband, Mr. Felix Bautista, 53. Both were discharged on July 1. It is now August 22, day 52 after discharge.</p>
<p>The claims clerk tells you the claim cannot be filed: the KT registry entry for Mrs. Bautista was never completed, and the essential-services checklist is missing the donor&rsquo;s postoperative visit.</p>
<p>Meanwhile, Mr. Bautista shows you a bill from the hospital&rsquo;s outpatient laboratory for 6,800 pesos for his two-week post-donation blood tests. &ldquo;They said donor tests are not covered.&rdquo;</p>
""", "questions": ["What is the filing deadline, and what has to happen before it?",
                  "Is the donor&rsquo;s bill correct? Whom do you involve?",
                  "What would have prevented both problems?"]},
    "sections": [
        ("follow", "Evidence should follow care", "Build the claim from admission, not at discharge", """
<p>The safest claim is assembled as care happens. When evidence is gathered after discharge, people are hard to reach, results are scattered, and the 60-day window is already running.</p>
<div class="table-wrap"><table>
<thead><tr><th>Evidence</th><th>When to check it</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Pre-authorization and its validity</td><td>Before admission</td><td>Z Benefits coordinator</td></tr>
<tr><td>KT registry registration and form</td><td>Before admission; confirm the entry exists</td><td>Designated registry user</td></tr>
<tr><td>Essential-services checklist entries</td><td>Daily during admission; before discharge</td><td>Clinical teams, collected by the coordinator</td></tr>
<tr><td>Consistent identifiers and dates across forms</td><td>Before filing</td><td>Claims team</td></tr>
<tr><td>Discharge summary and statement of account</td><td>At discharge</td><td>Attending team; billing</td></tr>
</tbody></table></div>
<p>Never create evidence for a service that did not happen, and never alter a clinical record to fit a claim. If a mandatory service was not provided, the claims lead decides how to report it; the clinical record stays true.</p>
{{key:Build the claim as care happens. A claim assembled after discharge starts its race already behind.}}
"""),
        ("window", "Keep the window", "Sixty days after discharge", """
<p>The filing deadline is counted from discharge. Put it in the register the day the patient goes home, with weekly checks.</p>
{{formula:Filing deadline = discharge date + 60 days}}
<p>For a discharge on July 1, the deadline is August 30. The <a href="calc-transplant-coordinator-toolkit.html#tool-4">claim filing window tool</a> calculates the date and the days left. Existing late-filing rules apply, with special consideration for natural calamities or fortuitous events; ask the claims lead before relying on any exception.[[rtc_ph2026]]</p>
{{scene:Two weeks of quiet|<p>At a Cavite hospital, coordinator Ms. Mylene Torres sets a weekly claim check every Monday after each transplant discharge. On day 14 she finds that the donor&rsquo;s anesthesia record is missing from the packet.</p>
<p>She asks anesthesia the same day; the record arrives on day 16. The claim is filed on day 30 with 30 days to spare.</p>
<p class="tc-scene-take">The fix took two days because it was found on day 14, not day 58.</p>}}
{{key:Enter the 60-day deadline on the day of discharge and check the packet weekly.}}
"""),
        ("return", "Return versus denial", "Different problems, different routes", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Return</th><th>Denial</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>The claim is incomplete or needs correction</td><td>A decision not to pay, with a reason</td></tr>
<tr><td>Common causes</td><td>Missing attachment, unclear entry</td><td>Late filing, missing KT registry, mandatory services not provided, inconsistent data</td></tr>
<tr><td>What to do</td><td>Correct and resubmit within the allowed time</td><td>The claims lead reviews; appeal or reconsideration through PhilHealth&rsquo;s process if grounds exist</td></tr>
<tr><td>Coordinator&rsquo;s role</td><td>Find the missing evidence fast</td><td>Supply the facts and timeline; never alter records</td></tr>
</tbody></table></div>
<p>Keep a simple log of returns and denials by reason. If the same reason keeps appearing &mdash; registry entries, a particular form &mdash; fix the upstream step, not each claim.</p>
{{key:A return is a task; a denial is a decision. Fix returns fast, and route denials to the claims lead with the facts.}}
"""),
        ("protect", "Protect both people from avoidable harm", "The donor never pays for donating", """
<p>The DOH living-donor order states that donation-related medical expenses, donor care, and follow-up must not be charged to the donor by the transplant facility.[[rtc_doh2021]] PhilHealth&rsquo;s package covers donor evaluation, management, and nephrectomy, and the post-transplant packages list donor monitoring.[[rtc_ph2026]][[rtc_ph2025a]] When a donor receives a bill for donation-related care, the coordinator&rsquo;s job is to stop it reaching the donor and to route it to billing and the program manager to resolve.</p>
<p>Charges are only part of the burden. The evidence on donor costs is consistent, though none of it comes from the Philippines:</p>
<ul>
<li>A Canadian prospective cohort of 821 donors found median out-of-pocket costs of 1,254 Canadian dollars, with total costs (including lost productivity) above 5,500 Canadian dollars for 25% of donors.[[rtc_przech2018]]</li>
<li>A US survey of 796 donors found that 26% rated their financial burden at 5 or more out of 10, including some with no out-of-pocket costs, because of lost wages and continuing expenses.[[rtc_wiseman2017]]</li>
<li>In the Canadian cohort, donors with higher expenses had worse mental health-related quality of life at three months, after adjustment for their pre-donation mental health.[[rtc_barnieh2021]]</li>
</ul>
<p>These studies are observational and from high-income countries. They do not tell us the size of the burden here, but they do show that &ldquo;covered&rdquo; and &ldquo;cost-free&rdquo; are different things, and that cost is associated with harm beyond money.</p>
{{key:The donor never pays for donation-related care. Stop the bill, route it, and ask about the costs no bill shows.}}
"""),
    ],
    "debrief": ["""
<p><strong>The deadline.</strong> July 1 plus 60 days is August 30; eight days remain. Today, ask the designated registry user to complete Mrs. Bautista&rsquo;s KT registry entry, and ask the donor&rsquo;s surgical clinic to document the postoperative visit that was actually done, if it was done. If it was not done, the claims lead decides how to report it; nothing is backfilled. Recheck daily until filing.</p>
<p><strong>The donor&rsquo;s bill.</strong> Not correct. Post-donation tests are donation-related care that the facility must not charge to the donor. Apologize, take the bill, and route it to billing and the program manager to cancel or redirect. Tell Mr. Bautista he does not need to pay it, and confirm in writing once it is resolved.</p>
<p><strong>Prevention.</strong> Registry entry confirmed before admission, the essential-services checklist kept daily, a weekly claim check from discharge, and a billing flag on every donor account so donation-related charges never reach the donor.</p>
"""],
    "skills": {"title": "Claim readiness and donor charge protection",
               "intro": "Prepare a mock claim packet from admission to filing and resolve a mock donor charge while your preceptor observes.",
               "items": [
                   ("Confirms pre-authorization validity and KT registry entry before admission.", True),
                   ("Calculates the filing deadline and sets weekly checks.", False),
                   ("Distinguishes a return from a denial and routes each correctly.", False),
                   ("Refuses to create or alter evidence to fit a claim.", True),
                   ("Stops a donation-related charge from reaching a simulated donor and routes it.", True),
                   ("Asks a donor privately about indirect costs: lost income, travel, childcare.", False),
               ],
               "placement": "With the claims team, review returns and denials for transplant claims in the last year and group them by reason."},
    "terms": [("Claim", "The hospital&rsquo;s request for payment."), ("Filing window", "Sixty days after discharge for this package."),
              ("Return", "A claim sent back for correction."), ("Denial", "A decision not to pay, with a reason."),
              ("Mandatory services", "Services the package requires and checks."), ("Financial neutrality", "No gain or loss from donation.")],
    "readings": [("philhealth-z-packages.html", "The patient guide to PhilHealth&rsquo;s transplant package.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-4", "calc-transplant-coordinator-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["11"])
