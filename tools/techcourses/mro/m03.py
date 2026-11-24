# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 03: Identity, Intake, and the Master Patient Index. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records clerk at a dialysis intake desk checking an older patient's ID card while his daughter waits beside him.",
    "objectives": [
        "Match a patient on two approved person-level identifiers.",
        "Search the master patient index with name variants before creating any chart.",
        "Explain, from evidence, how duplicate records are actually created.",
        "Quarantine and resolve a suspected duplicate or misfile without exposing either record, while alerting the clinical team if treatment is imminent.",
    ],
    "big": """
{{plain:Every later step &mdash; the claim, the registry row, the transfer packet, the reprocessed dialyzer &mdash; inherits whatever identity a document was filed under. Attach the wrong person at intake and every later step is wrong in a way that looks right.}}
<p>Dialysis units carry particular risk. The same patients return three times a week, namesakes and relatives often dialyze on the same shift, and reprocessed dialyzers must return to exactly one person.</p>
{{cards:Key terms for this module|Master patient index (MPI)::Master patient index; the list linking each person to one chart number.|Person-level identifier::A fact about who the patient is, such as full name and date of birth, not where they sit.|Duplicate::Two records for one person.|Misfile::A correct document placed in the wrong patient&rsquo;s chart.|Merge::Combining two records that belong to one person, through a controlled workflow.|PhilHealth Identification Number (PIN)::PhilHealth Identification Number.}}
""",
    "case": {"title": "Two Marias", "html": """
<p>A referral arrives for &ldquo;Training Patient,&rdquo; born 1972, with no full birth date. Your index has two candidates: SIM-041, born February 4, 1972, and SIM-042, born May 8, 1972. The phone number printed on the referral does not match the sending hospital&rsquo;s number in your directory. SIM-042 dialyzes this afternoon.</p>
""", "questions": ["Where does the referral go right now?",
                  "How will you verify, and through which channel?",
                  "Who else needs to know before the afternoon shift?"]},
    "sections": [
        ("two", "Two identifiers", "Two identifiers, both about the person", """
<p>Use two approved person-level identifiers &mdash; typically full name and date of birth, plus the institutional patient number or the PhilHealth Identification Number (PIN) where policy allows. A station number, chair, shift, or room describes <em>where</em> the patient is today, not <em>who</em> they are, so it never counts.</p>
<p>Before assigning a new permanent chart number, search the master patient index (MPI) with name variants: maiden and married surnames, middle name present or absent, swapped first and last names, and nicknames such as &ldquo;Jun&rdquo; or &ldquo;Baby.&rdquo; Record aliases and previous identifiers with their source.</p>
{{fig:mro03_duplicates}}
"""),
        ("evidence", "The evidence", "How duplicates and wrong-patient errors really happen", """
<p>In a multisite study of 398,939 confirmed duplicate record pairs, the most frequently mismatched field was the middle name (58.3% of pairs), and most name mismatches were plain misspellings or swapped name order.[[mro_just2016]] Duplicates are mostly made at the front desk by ordinary typing. The controls that follow are equally ordinary: a written naming convention (full middle name, never an initial when the full name is known), a required search routine, and a monthly duplicate report reviewed by a second person.</p>
<p>Some intuitive controls fail when tested. In a randomized trial of 3,356 clinicians and 12.1 million orders, limiting users to one open record at a time did not reduce wrong-patient orders compared with allowing four (90.7 vs. 88.0 per 100,000 order sessions; odds ratio 1.03, 95% confidence interval 0.90 to 1.20).[[mro_adelman2019]] Other controls look promising: in a large emergency-department cohort, showing the patient&rsquo;s photograph in the record banner was <em>associated with</em> fewer wrong-patient orders (adjusted odds ratio 0.57).[[mro_salmasian2020]] That study was observational, so it suggests rather than proves benefit, and photographs need a documented lawful basis and consent process under the Data Privacy Act. In hemodialysis clinics, nursing teams name patient-identification errors as their main gap against international patient-safety goals.[[mro_lima2023]]</p>
{{key:Verify identity at the point of action. Search before you create.}}
"""),
        ("resolve", "Resolving", "Suspected duplicate or misfile", """
{{flow:Safe resolution|Stop::Halt further routing of the contested document.|Quarantine::Place it in a protected exception queue.|Notify::Tell HIM and the clinical owner.|Verify independently::Use a trusted directory number, not the number on the suspicious document.|Resolve through the controlled workflow::Merge or reassign only with authorization, preserving both original identifiers.|Check downstream::Claims, registry rows, the dialyzer log, and any released copies.}}
{{call:Never merge on a likely match. &ldquo;Probably the same person&rdquo; is the exact belief that produces a wrong-patient merge, which is far harder to undo than a duplicate. If either candidate is scheduled today, alert the charge nurse now so identity is verified at the bedside while you resolve the record.}}
"""),
    ],
    "debrief": ["""
<p><strong>Right now.</strong> The referral goes to the protected exception queue, marked pending match, filed to neither chart.</p>
<p><strong>Verification.</strong> Call the sending hospital&rsquo;s records office using the number in your verified directory and confirm the full birth date and a second identifier. Do not read either candidate&rsquo;s details to the caller.</p>
<p><strong>Who else.</strong> Alert the charge nurse at once because SIM-042 dialyzes this afternoon. Record who verified, when, and how, and leave a dated resolution note on the chart that receives the document.</p>
"""],
    "skills": {"title": "Identity verification and exception handling",
               "intro": "Process a fictional intake and a suspected misfile with a preceptor.",
               "items": [
                   ("Uses two person-level identifiers and rejects location-based identifiers.", True),
                   ("Searches the MPI with name variants before creating a chart.", True),
                   ("Quarantines a contested document and verifies through an independently trusted channel.", True),
                   ("Alerts the clinical team in parallel when treatment is imminent.", True),
                   ("Lists every downstream place a corrected record must be checked.", False),
               ],
               "placement": "Run your unit&rsquo;s duplicate report for last month, or ask IT for one, and review three pairs with your supervisor."},
    "terms": [("MPI", "Master patient index."), ("PIN", "PhilHealth Identification Number."),
              ("Duplicate", "Two records for one person."), ("Misfile", "A correct document in the wrong chart."),
              ("Merge", "Combining two records of one person through a controlled workflow."),
              ("HIM", "Health information management.")],
    "readings": [("personal-medical-journal-health-history.html", "Why a patient&rsquo;s own health history helps keep records straight.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["03"])
