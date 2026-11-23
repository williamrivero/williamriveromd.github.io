# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 02: Licensing and Inspection Readiness. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a head nurse walking a dialysis unit with a floor plan, tracing the route from the entrance to a treatment chair.",
    "objectives": [
        "Identify which Department of Health (DOH) issuances govern your facility, and which questions each one answers.",
        "Recognize changes that need a regulatory decision before they happen: new stations, a new bay, relocation, or a change of ownership.",
        "Run a three-source tracer that compares the document, the observed practice, and the staff interview.",
        "Write a finding with its requirement, condition, exposure, containment, owner, due date, and closure evidence.",
        "Distinguish completing a corrective action from proving that it worked.",
        "Keep an evidence index that an inspector can follow without you in the room.",
    ],
    "big": """
{{plain:A license is a photograph of your unit on the day it was approved. Every change you make afterward, a new chair, a moved wall, a new owner, makes the photograph a little less true.}}
<p>The picture has a limit. A photograph does not change, but the rules do. The DOH can revise what a clinic must show, and your regional office decides how a new rule applies to you. Readiness means knowing both what your unit looks like today and which version of the rules it is being measured against.</p>
{{cards:Key terms for this module|PTC::Permit to Construct, the DOH approval to build or substantially alter a facility before it operates.|Assessment tool::The checklist the regional licensing office uses during inspection. Ask for the current revision.|Tracer::Following one patient, machine, or process through the unit to test whether the system works as written.|Finding::A gap between a requirement and what the inspector, or you, observed.|Containment::The immediate step that stops a finding from harming anyone while the real fix is made.|Closure evidence::Objective proof that a corrective action works, checked by a named person on a named date.|PRDR::Philippine Renal Disease Registry, to which dialysis clinics report their patients.}}
""",
    "case": {"title": "Two machines and an empty bay", "html": """
<p>St. Lorenzo Renal Center, a ten-station freestanding unit in Bulacan, has a waiting list. The administrator, Ms. Grace Dizon, plans to move two machines into the adjacent storage bay and open them on Monday. The bay is not on the approved floor plan. One of the two machines came back from repair on Friday, and its maintenance record has no signed release.</p>
<p>&ldquo;The inspector already came last month,&rdquo; she says. &ldquo;We passed. Two more chairs will help eight patients on the list. Can you approve them today?&rdquo;</p>
""", "questions": ["What can you approve today, and what can you not?",
                  "What evidence would change your decision about each machine and the bay?",
                  "What will you ask the regional office, and how?"]},
    "sections": [
        ("rules", "The rules", "Which issuance answers which question", """
<p>The core licensing order for dialysis facilities sets out how hemodialysis clinics are licensed, who must head and staff them, what the physical plant needs, and what they must report, including registration of patients in the PRDR.[[doh2012]] A separate order governs the analysis, monitoring, and maintenance of dialysis water.[[dch_doh2013]] The DOH has also issued planning and design guidelines for dialysis clinics, which describe room relationships and controlled entry to the treatment area.[[dch_doh_design2025]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Where to look</th><th>Status of the evidence in this course</th></tr></thead>
<tbody>
<tr><td>What must a licensed hemodialysis clinic have and report?</td><td>DOH Administrative Order 2012-0001[[doh2012]]</td><td>Baseline order, in force</td></tr>
<tr><td>How is dialysis water tested and released?</td><td>DOH Administrative Order 2013-0003[[dch_doh2013]]</td><td>In force; see Module 5</td></tr>
<tr><td>How must the space be laid out?</td><td>DOH planning and design guidelines for dialysis clinics, 2025[[dch_doh_design2025]]</td><td>Posted by a regional office; confirm it is the edition your region applies</td></tr>
<tr><td>Have licensing rules for hemodialysis clinics changed?</td><td>DOH Department Circular 2026-0112, interim guidelines on licensing hemodialysis clinics[[dch_doh2026]]</td><td>Title confirmed; text not reviewed. Read it, with its annexes and transition clauses, before applying any earlier rule</td></tr>
<tr><td>How are applications filed?</td><td>Your regional office&rsquo;s current instructions, including any online licensing system</td><td>Varies by region and year</td></tr>
</tbody></table></div>
{{call:Stop and ask the Regulatory, Licensing and Enforcement Division (RLED) in writing whenever a change touches stations, rooms, location, services, or ownership. Hold the change until the written answer is in your file.}}
"""),
        ("change", "Changes", "Changes that need a decision before they happen", """
{{fig:dch02_change}}
<p>An approved floor plan is part of your license. Adding stations, opening a new room, relocating, adding a service such as hemodiafiltration, or changing owners can each require a regulatory step before the first patient is treated in the new arrangement. Moving a chair into an unapproved bay is not an interior-design decision.</p>
<p>A machine has its own gate. It returns to service only after the technical lead documents the checks and signs a release. Your signature, as clinical head, comes after theirs and answers a different question: is it safe to treat patients again?</p>
{{key:Ask before you move. A delay of a week is recoverable. Treating patients in an unapproved space puts the whole license at risk.}}
"""),
        ("tracer", "The tracer", "The three-source tracer", """
{{fig:dch02_tracer}}
<p>Inspectors do not only read binders. They pick a patient, a machine, or a shift and follow it. You should do the same, before they arrive, because the gaps that matter are usually between what is written and what is done.</p>
{{flow:Three tracers worth running every quarter|A shift::From the roster to the duty physician to the nurse&rsquo;s description of how she escalates a falling blood pressure.|A machine::From the inventory to its maintenance log, its release, its disinfection record, and its use today.|A patient::From acceptance to the current order, the last laboratory results, the access plan, and the PhilHealth record.}}
<p>For each discrepancy, write the requirement, what you observed, which patients were or could be exposed, the immediate containment, the owner, the due date, and the evidence that will close it. Bring high-risk or resource-dependent findings to the owner with a request, not only a report.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Requirement</td><td>Every machine returned from repair has a signed technical release before use</td></tr>
<tr><td>Observed</td><td>Machine 9 returned Friday; release unsigned</td></tr>
<tr><td>Exposure</td><td>None yet; machine not used</td></tr>
<tr><td>Containment</td><td>Tagged out of service by the head nurse at 08:10</td></tr>
<tr><td>Owner and due date</td><td>Biomedical lead, Tuesday</td></tr>
<tr><td>Closure evidence</td><td>Signed release, then a check one month later that every repaired machine had its release before first use</td></tr>
</tbody></table></div>
"""),
        ("closure", "Closing findings", "Closing a finding with proof", """
{{fig:dch02_closure}}
<p>A corrective action is done when it has been carried out. A finding is closed when someone has checked that the control works in practice. &ldquo;Staff retrained&rdquo; closes nothing until you have watched the step being done correctly, on more than one shift, some weeks later.</p>
<p>Give each controlled document a custodian and a review date. Withdraw obsolete versions from the floor and keep one archived copy. When an inspector asks for a policy, the version on the wall should match the version in the binder.</p>
{{formula:<strong>Scoring a finding, illustration only.</strong> Likelihood 3 of 5 &times; severity 4 of 5 = 12. In this course&rsquo;s teaching scale, a score of 15 or more, or any catastrophic consequence, goes to leadership. Use your facility&rsquo;s approved thresholds in practice. Calculator 4 does the arithmetic.}}
"""),
    ],
    "debrief": ["""
<p><strong>What can you approve today?</strong> Nothing that adds stations in the bay. Keep the bay closed and ask the RLED, in writing, what approval the change requires. The machine returned Friday stays tagged out until the biomedical lead signs a release. The second machine, if it has a valid release, can stay in an approved station where it already belongs.</p>
<p><strong>What evidence would change your decision?</strong> For the bay: a written regional answer that the change is permitted, and any required approvals in hand. For the repaired machine: a signed technical release. For both: confirmation that staffing and water capacity can support two more stations, which is Module 8&rsquo;s question.</p>
<p><strong>What do you ask, and how?</strong> A letter to the RLED describing the proposed change, the current approved plan, and the date you need an answer. Meanwhile, tell Ms. Dizon what the waiting-list patients need instead: their attending nephrologists should review urgency, and the unit can look for verified capacity elsewhere.</p>
"""],
    "skills": {"title": "Three-source tracer and finding record",
               "intro": "Run one shift tracer and one machine tracer on a real or simulated unit while a preceptor observes, and write up two findings.",
               "items": [
                   ("Identifies the facility type and the current assessment tool and submission route.", False),
                   ("Recognizes a change that needs a regulatory decision before implementation.", True),
                   ("Compares the document, the observed practice, and a staff interview for each tracer.", True),
                   ("Writes each finding with requirement, observation, exposure, containment, owner, and due date.", False),
                   ("Keeps an unverified area or machine out of use until approvals and releases are confirmed.", True),
                   ("Defines closure as evidence that the control works, with a named verifier and date.", True),
                   ("Assigns a custodian and review date to controlled documents.", False),
                   ("Brings resource-dependent findings to the owner with a specific request.", False),
               ],
               "placement": "Run the three quarterly tracers on your own unit. Present the findings and their closure criteria at your next quality meeting."},
    "quiz": [
        ("Which DOH order sets the baseline rules for licensing dialysis facilities?",
         ["AO 2013-0003", "AO 2012-0001", "PhilHealth Circular 2024-0023", "RA 10173"], 1,
         "AO 2013-0003 covers dialysis water."),
        ("What should you do before applying a 2026 interim licensing circular you have seen only by title?",
         ["Apply it from the title", "Read its full text, annexes, and transition clauses, and ask the RLED how it applies", "Ignore it", "Wait for an inspection"], 1,
         "A title is not a rule."),
        ("The administrator wants two chairs in an unapproved bay. What is your first step?",
         ["Approve if the room is clean", "Keep the bay closed and ask the RLED in writing", "Open one chair as a trial", "Ask the patients"], 1,
         "Changes to stations and rooms may need approval first."),
        ("A machine returned from repair has no signed release. Who closes that gap?",
         ["The clinical head by signing", "The designated technical lead by documenting checks and signing", "The administrator", "The nurse at that station"], 1,
         "Clinical authorization follows technical release."),
        ("What are the three sources in a tracer?",
         ["Owner, inspector, patient", "Document, observed practice, staff interview", "Budget, roster, invoice", "Policy, memo, email"], 1,
         "Gaps live between what is written and what is done."),
        ("A policy is signed but staff describe a different workflow. What completes the tracer?",
         ["Filing the policy again", "Observing practice and records, then recording the discrepancy", "Reprinting the policy", "Nothing"], 1,
         "The discrepancy is the finding."),
        ("Which of these closes a finding?",
         ["The action was carried out", "Objective evidence that the control works, checked by a named person on a date", "A memo to staff", "The owner&rsquo;s approval"], 1,
         "Completion is not effectiveness."),
        ("A finding last closed with &ldquo;staff retrained&rdquo; recurs. What does that suggest?",
         ["Bad luck", "The fix was weak and its effect was never checked", "The inspector was wrong", "More memos are needed"], 1,
         "Training alone fades; choose a stronger control and measure it."),
        ("What is containment?",
         ["The final fix", "The immediate step that prevents harm while the real fix is made", "A report to DOH", "A staff meeting"], 1,
         "Tagging a machine out of service is containment."),
        ("What should happen to obsolete versions of a controlled document?",
         ["Keep them on the floor", "Withdraw them from use and archive one copy", "Shred all copies", "Post them beside the new one"], 1,
         "The version in use should match the version in the binder."),
        ("Which registry must dialysis clinics report their patients to?",
         ["The PhilHealth Dialysis Database only", "The Philippine Renal Disease Registry", "The NPC registry", "None"], 1,
         "PRDR participation is part of the licensing order."),
        ("A finding scores likelihood 4 and severity 4 on the teaching scale. What happens?",
         ["Nothing; it is below 20", "It goes to leadership review because it is 16, above the teaching threshold of 15", "It is closed", "It is sent to PhilHealth"], 1,
         "Use your facility&rsquo;s own thresholds in practice."),
        ("Who should own an inspection finding that needs money to fix?",
         ["Nobody until funded", "A named owner, with the request escalated to the governing body", "The inspector", "The newest staff member"], 1,
         "Resource-dependent risks go to governance with a request."),
        ("Why walk the route from the entrance to a chair with the floor plan?",
         ["For exercise", "The walk shows which records to check and whether the space matches the approval", "To count chairs only", "To meet patients"], 1,
         "Space and records should describe the same unit."),
        ("What is the clinical head&rsquo;s role in an inspection?",
         ["To prepare every record personally", "To review the clinical criteria and make sure findings have owners and closure evidence", "To negotiate with the inspector", "None"], 1,
         "The compliance owner obtains forms; the head owns clinical criteria and follow-through."),
    ],
    "terms": [("Assessment tool", "The checklist the regional licensing office uses during inspection."),
              ("Tracer", "Following one patient, machine, or process through the unit."),
              ("Finding", "A gap between a requirement and observed practice."),
              ("Containment", "The immediate step that prevents harm while the fix is made."),
              ("Closure evidence", "Proof that a corrective action works, checked by a named person."),
              ("Controlled document", "A policy or form with a version, custodian, and review date."),
              ("PTC", "Permit to Construct."),
              ("PRDR", "Philippine Renal Disease Registry.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality assessment and performance improvement in dialysis units.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
