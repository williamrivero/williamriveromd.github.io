# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 19: Philippine documentation and quality. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "An access team at a quality meeting reviewing a run chart of catheter use and functional fistula outcomes on a laptop.",
    "objectives": [
        "Write an operative and follow-up record that makes the clinical decision understandable, separate from claim paperwork.",
        "Distinguish a procedure code, payer classification, eligibility and payable amount.",
        "Define access outcomes with explicit numerators, denominators and follow-up, using the Society for Vascular Surgery (SVS) reporting standards.",
        "Separate technical patency from functional use, and turn an audit into a testable change.",
    ],
    "big": """
{{plain:Measuring an access service by counting open fistulas is like judging a bus company by how many buses have engines that start. It matters, but passengers care whether the bus arrives, on time, with them on it.}}
<p>The picture has a limit. A bus company can count passengers easily. Access outcomes are harder: patients move between units, die, receive transplants or switch modality, and each of these removes them from follow-up in a different way. A measure is only honest if its definition, denominator, time window and missing data are stated.</p>
{{cards:Key terms for this module|Primary patency::Time from creation until any intervention or thrombosis.|Assisted primary patency::Time until thrombosis or abandonment, allowing interventions that keep a still-open access working.|Secondary patency::Time until abandonment, allowing any intervention including thrombectomy.|Functional use::The access is actually used for dialysis as prescribed.|Denominator::The group and time over which an outcome is counted.}}
<p>Your work is to keep the clinical record, the claim and the audit separate and accurate, and to report outcomes in a way that helps the team improve rather than look good.</p>
""",
    "case": {"title": "The dashboard that counts everything", "html": """
<p>Your hospital&rsquo;s new quality dashboard reports &ldquo;fistula success: 92%.&rdquo; It counts every fistula that had a thrill at the six-week clinic visit. Of last year&rsquo;s 118 fistulas, 21 patients never returned to clinic. Of those who did, the dialysis units report that 34 fistulas were still not being used at six months, and those patients remained on catheters.</p>
<p>At the same meeting, the billing officer asks you to write the PhilHealth package amount for fistula creation into the access lesson for residents, &ldquo;so they know what to expect.&rdquo;</p>
""", "questions": [
        "What is wrong with the 92% figure, and how would you report outcomes instead?",
        "What should the residents&rsquo; lesson say about codes and payment?",
        "What would you propose as the team&rsquo;s first improvement?"]},
    "sections": [
        ("record", "The clinical record", "A record that explains the decision", """
<p>The clinical record exists so the next clinician understands what happened and why: the indication and the Life-Plan behind it, the consent discussion, findings, the procedure, the immediate result, complications, restrictions, follow-up owner and warning signs. The dialysis unit needs a timely handoff even when claim paperwork is still in progress; a delayed claim must never delay the clinical message.</p>
{{fig:vs19_b}}
<p>Philippine regulation and payer policy shape the paperwork around the record. The Department of Health (DOH) licenses dialysis facilities and sets their records and referral requirements.[[an01_2]] PhilHealth publishes quality standards for maintenance hemodialysis (Circular 2024-0029) and its hemodialysis coverage rules (Circular 2024-0023).[[vs_ph_pc2024_0029]][[an01_6]] These rules change. Check the circulars in force on the date of service with your claims lead before quoting any requirement or amount.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What answers it</th><th>What it does not establish</th></tr></thead>
<tbody>
<tr><td>What procedure was done?</td><td>The operative note and procedure code</td><td>Eligibility or payment</td></tr>
<tr><td>How does the payer classify it?</td><td>The payer&rsquo;s current classification annex</td><td>That a specific amount is payable</td></tr>
<tr><td>Is this patient and provider eligible?</td><td>Current circulars, membership and accreditation</td><td>The clinical indication</td></tr>
<tr><td>What will be paid?</td><td>The package rules in force on the date of service</td><td>Anything in a teaching module</td></tr>
</tbody></table></div>
{{key:A code describes what was done. It does not prove that a patient is eligible or that any amount is payable.}}
"""),
        ("measures", "Honest measures", "Defining outcomes honestly", """
<p>The Society for Vascular Surgery (SVS) reporting standards define primary, assisted primary and secondary patency so that results can be compared between services.[[vs_sidawy2002]] Each needs a clear start (the day of creation, not the day of first use, unless stated), clear events, and clear censoring: death, transplant, modality change and loss to follow-up handled the same way every time. Patency is still a surrogate. The UK Kidney Association (UKKA) 2025 guideline emphasizes outcomes such as functional use and catheter-free dialysis, and HFM reported functional patency alongside maturation.[[vs_ukka]][[vs_huber2021]]</p>
{{fig:vs19_a}}
<p>Report counts beside rates, show the follow-up interval, and state how many patients are missing. For infection, a rate per 1,000 catheter-days and the National Healthcare Safety Network (NHSN) rate per 100 patient-months are different measures; do not compare them without reconciling definitions. Small services should show confidence intervals, because a single event can swing a rate dramatically.</p>
{{flow:A defensible access audit|Define the cohort::Who, created when, by whom.|Define the outcome::Primary failure, functional use, catheter-free days, interventions per year.|Define follow-up::Window, censoring for death, transplant and modality change.|Count missing data::Report it; do not drop it.|Show uncertainty::Counts, rates and confidence intervals.|Choose a change::A specific process to test, with a review date.}}
"""),
        ("improve", "Improvement", "From audit to improvement", """
<p>An audit is useful only if it leads to a change the team can test. Track a small set of measures: referral-to-assessment time, the proportion with a documented first-use handoff, functional use within a set window, catheter days, unplanned procedures, major bleeding, and patient-reported burden. Compare like with like, and avoid punishing services that take the hardest patients.</p>
{{scene:Quality meeting, fictional|<p>A service finds that 40% of patients with mature fistulas still dialyze through catheters three months after maturation. The cause is a missing first-use handoff. The team introduces a one-page handoff and a phone call to the unit at maturation; three months later the proportion falls to 22%.</p><p class="tc-scene-take"><b>What this shows.</b> The biggest gains often come from closing a handoff, not from changing the operation.</p>}}
{{call:Never present an unverified benefit amount or classification entry as a guarantee of payment, in a lesson, a consent discussion or a patient handout.}}
"""),
    ],
    "debrief": [
        "<p><strong>The 92%.</strong> It counts technical patency at six weeks, excludes the 21 patients lost to follow-up, and ignores the 34 fistulas not used by six months. Report separately: primary failure, functional use at a stated interval (for example, the proportion used successfully for dialysis by six months), catheter-free dialysis, with the denominator of 118, the number missing, and confidence intervals.</p>",
        "<p><strong>Codes and payment.</strong> The lesson should explain that a procedure code, a payer classification, eligibility and a payable amount are separate, and that amounts must be checked on the date of service with the claims lead. Do not copy a historical amount into a permanent lesson.</p>",
        "<p><strong>First improvement.</strong> Find out why 34 fistulas were not used. If, as often, first-use handoffs were missing or maturation was not assessed, introduce a structured handoff and a maturation visit at four to six weeks, and re-measure functional use in three months.</p>",
    ],
    "skills": {"title": "Documentation bundle and audit design",
               "intro": "Use a fictional documentation set and audit dataset.",
               "items": [("Reconciles a fictional operative record and dialysis handoff", False),
                         ("Distinguishes code, classification, eligibility and payment", True),
                         ("Defines an outcome with numerator, denominator, window and censoring", True),
                         ("Reports missing follow-up and confidence intervals", False),
                         ("Proposes a measurable improvement with a review date", False)],
               "placement": "Quality meeting or simulation"},
    "quiz": [
        ("An official classification table includes an access procedure. What does that establish?",
         ["A fixed reimbursement amount for every patient", "Its presence in that classification; eligibility and payment still need separate verification",
          "Automatic provider accreditation", "That the procedure is indicated"],
         1, "Classification, payment and accreditation are separate questions."),
        ("Which outcome report is more transparent?",
         ["Calling every patent access a success", "Omitting patients lost to follow-up",
          "Reporting technical and functional outcomes separately with denominators and missing data", "Reporting only the best surgeon&rsquo;s results"],
         2, "Clear definitions make results interpretable."),
        ("Under the Society for Vascular Surgery (SVS) reporting standards, what distinguishes secondary from primary patency?",
         ["Secondary patency allows interventions, including thrombectomy, until abandonment", "Secondary patency counts only grafts",
          "Primary patency allows thrombectomy", "There is no difference"],
         0, "Primary patency ends at any intervention or thrombosis; secondary ends at abandonment."),
        ("Why should a small service show confidence intervals with its infection rate?",
         ["They are required by PhilHealth", "A single event can change a small-number rate dramatically", "They make rates higher", "They replace counts"],
         1, "Uncertainty is large with few events; show counts too."),
        ("A rate per 1,000 catheter-days and a National Healthcare Safety Network (NHSN) rate per 100 patient-months are what?",
         ["Identical measures", "Different measures that should not be compared without reconciling definitions", "Both payment rules", "Both patency measures"],
         1, "Different denominators and definitions."),
    ],
    "terms": [("Censoring", "Removing a patient from follow-up at a stated point (death, transplant, transfer) without counting it as an event."),
              ("Functional patency", "An access that remains usable for dialysis.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality assurance and improvement in dialysis units."),
                 ("hemodialysis-access-lifeline.html", "Why functional access matters to patients.")],
    "calcs": ["calc-av-access-outcome-audit.html", "calc-access-infection-rate.html", "calc-qapi-run-chart-spc.html", "calc-dialysis-qapi-scorecard.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
