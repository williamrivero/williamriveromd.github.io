# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 01: Roles, Authority, and Policy. Written for this series from the handoff blueprint (files 01-04)."""

MODULE = {
    "image_alt": "Three pairs of hands passing a manila claim folder along a desk, left to right, like a relay baton.",
    "objectives": [
        "Name the owner of each common decision on a dialysis claim: clinical, coding, release, financial, delegation, and privacy.",
        "Explain why claims staff route questions instead of deciding them, using the relay picture.",
        "Rank evidence types from law to job posting, and check the four dates that decide which rule applies.",
        "Resolve a conflict between a vendor screen, an SOP, and a PhilHealth issuance, and record the decision.",
        "Write a hold note that names the issue, the source, the owner, the due date, and the next action.",
    ],
    "big": """
{{plain:A claim is a relay race. It passes from the front desk to the nurse, to the coder, to the claims officer, to PhilHealth, and back to finance. A claim is safe only while someone is holding it. The commonest failure is not a wrong answer; it is a dropped baton, a question nobody owns.}}
<p>The picture has a limit. In a relay, any runner may carry the baton. In a claims office, some decisions belong to one person only. A clerk may notice that a diagnosis looks wrong, but only the treating clinician may change it. A claims officer may prepare a refund, but only finance releases money. The skill this module teaches is knowing where your authority starts and stops, and leaving a written trail every time you hand something on.</p>
{{fig:pc_roles}}
{{cards:Key terms for this module|Issuance::Any official PhilHealth document: a circular sets rules; an advisory explains, reminds, or sets dates.|Effective date::The day a rule starts to apply. It can differ from the day it was signed or published.|Service date::The day the patient was treated. The rule in force on that day usually governs the claim.|SOP::Standard operating procedure: your facility&rsquo;s written steps for applying the rules.|Hold::A claim kept from release until a named owner resolves a named issue.|PRO::PhilHealth Regional Office, the source of written guidance when instructions conflict.}}
""",
    "case": {"title": "The batch that needed a different diagnosis", "html": """
<p>It is Thursday afternoon at a freestanding dialysis center in Quezon City. A batch of twelve claims is due for release tomorrow. The clerk, Ms. Joy Ramos, notices that one discharge summary from a partner hospital, for a fictional patient coded SIM-01A, describes <em>acute kidney injury</em> and a temporary dialysis course. Every other claim in the batch is for chronic kidney disease stage 5 on maintenance hemodialysis.</p>
<p>The supervisor looks over her shoulder. &ldquo;Just label it stage 5 like the others so the batch goes out together. It&rsquo;s the same machine, the same session.&rdquo; On the shelf behind the desk, a printed binder from 2024 still lists the hemodialysis package at 4,000 pesos.</p>
""", "questions": ["Who may decide the diagnosis for SIM-01A, and what do you do with the claim today?",
                  "How do you respond to the supervisor, and to whom does the request go?",
                  "Which document tells you the current package rate, and how do you check it?"]},
    "sections": [
        ("owners", "Who owns what", "Every decision has an owner", """
<p>The handoff from patient to payment passes through many hands. The table below is the map this track uses. Your facility may combine roles in one person, but each decision still needs a named owner and a named backup.[[dch_philhealth2023acc]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Owner</th><th>What claims staff do</th></tr></thead>
<tbody>
<tr><td>The diagnosis and the treatment record</td><td>Treating clinician and nurse</td><td>Ask for clarification in neutral words; never edit</td></tr>
<tr><td>Code selection</td><td>Coder or designated reviewer</td><td>Flag a code that does not match the documentation</td></tr>
<tr><td>Explaining the agreement form to the patient</td><td>Liaison or designated staff</td><td>Use the patient&rsquo;s language and teach-back</td></tr>
<tr><td>Releasing and transmitting a claim</td><td>Authorized claims officer</td><td>Prepare, check, and hold anything unsupported</td></tr>
<tr><td>Signing a motion for reconsideration or appeal</td><td>Authorized signatory named by the facility</td><td>Assemble the chronology and evidence</td></tr>
<tr><td>Refunds, ledger postings, professional-fee release</td><td>Finance</td><td>Document the variance and route it</td></tr>
<tr><td>Delegation and formal sign-off</td><td>Facility head</td><td>Keep the delegation record current</td></tr>
<tr><td>Deciding whether a privacy breach is reportable</td><td>Data Protection Officer, for the facility</td><td>Report immediately and preserve the timeline</td></tr>
</tbody></table></div>
<p>A useful sentence for asking a clinician about a record: &ldquo;Please confirm the diagnosis documented for the session on September 7.&rdquo; It asks for the source to be checked without suggesting an answer.</p>
{{key:Claims staff surface and route. Owners decide. When you are unsure who owns a question, that uncertainty is itself something to escalate.}}
"""),
        ("sources", "Which rule applies", "When two sources disagree", """
<p>Claims staff receive instructions from many places: a circular, an advisory, a regional office email, the facility SOP, a vendor&rsquo;s help page, even a job posting describing the work. They are not equal. The higher source governs, and a lower source can only explain how to carry out a higher one.</p>
{{fig:pc_sources}}
<p>Before you apply any rule, check four dates. The <strong>publication date</strong> tells you when it became public. The <strong>effective date</strong> tells you when it starts to apply. The <strong>service date</strong> of the claim decides which version governs. And an <strong>amendment</strong> may have changed it since. A rule that was right last year may be wrong today, and a rule that took effect last month may not apply to a session delivered before it.</p>
{{flow:Resolving a conflict|1. Identify::The service date and the package (here, maintenance hemodialysis).|2. Open::The governing issuance and any later amendment or advisory.|3. Compare::Scope, service date, effective date, and amendments.|4. Record::The governing provision, its date, and the decision in the policy register.|5. Ask::For written guidance from the PRO when the conflict stays unresolved.}}
<p>For example, a vendor screen that still says a PDF statement of account is acceptable is overridden by PhilHealth Advisory 2026-0022, which says PDF submissions are no longer accepted and the claim will be returned.[[pc_pa2026_0022]] The advisory governs. Log the conflict, follow the advisory, and tell the vendor.</p>
"""),
        ("rate", "Old rates in old binders", "Why a binder can show the wrong rate", """
<p>The hemodialysis package changed three times in 2024. It rose from 2,600 to 4,000 pesos per session in July (3,650 for the facility and 350 for the professional), then to 6,350 pesos under PhilHealth Circular 2024-0023, Revision 2, effective October 9, 2024 (6,000 for the facility and 350 for the professional).[[pc_pc2024_0023]][[pc_news2024]] A binder printed between July and October 2024 is not wrong for its time; it is out of date for today.</p>
<p>The circular&rsquo;s transition clause decides which rate applies to a session near the change: services before the revision follow the earlier circular. For a qualifying session in September 2026, the rate under Circular 2024-0023 is 6,350 pesos.</p>
{{formula:<strong>Reading a binder safely.</strong> Note the issuance and effective date printed on it. Compare it with the current circular list on PhilHealth&rsquo;s website. If a newer issuance exists, mark the binder page &ldquo;superseded on [date] by [issuance]&rdquo; rather than throwing it away; old claims may still need it.}}
"""),
        ("holdnote", "The hold note", "Leaving a traceable handoff", """
<p>Every time a claim stops, someone must know why, who owns it, and when it will move again. A hold without an owner or a date is how filing periods lapse without anyone noticing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Example (fictional)</th></tr></thead>
<tbody>
<tr><td>Case reference</td><td>SIM-01A, session September 7</td></tr>
<tr><td>Issue</td><td>Discharge summary documents acute kidney injury; batch is chronic kidney disease stage 5</td></tr>
<tr><td>Source evidence</td><td>Discharge summary, page 2; treatment sheet September 7</td></tr>
<tr><td>Owner</td><td>Treating nephrologist (diagnosis); coder (package validation)</td></tr>
<tr><td>Due date</td><td>Monday, before the internal filing target</td></tr>
<tr><td>Next action</td><td>Clinician confirms diagnosis; claim routed to the correct pathway (Module 10)</td></tr>
</tbody></table></div>
{{call:A request to change a diagnosis, a date, or a signature to make a claim fit is a request to misrepresent the record. Hold the claim, preserve the source, and escalate the request to the facility compliance lead according to your SOP. Do not argue it at the desk.}}
"""),
    ],
    "debrief": ["""
<p><strong>Who decides the diagnosis.</strong> The treating clinician. Hold SIM-01A, keep the discharge summary and treatment sheet as they are, ask the clinician to confirm the documented diagnosis, and send the package question to the coder. If acute kidney injury is confirmed, the claim belongs to the hospital&rsquo;s acute pathway, not the maintenance hemodialysis package (Module 10). Release the other eleven claims if they are ready.</p>
<p><strong>The supervisor&rsquo;s request.</strong> Say calmly that you cannot change the diagnosis and that the claim is on hold for the clinician. Record the request in the hold note and escalate it to the compliance lead as your SOP directs. Labeling an acute case as stage 5 to fit a batch would misrepresent the record and could make the claim, and the batch, subject to denial and audit.</p>
<p><strong>The binder.</strong> The current rate comes from Circular 2024-0023, checked against PhilHealth&rsquo;s circular list: 6,350 pesos per qualifying session. Mark the binder page as superseded rather than discarding it.</p>
"""],
    "skills": {"title": "Routing and the hold note",
               "intro": "Using three fictional claims with planted problems, route each question to its owner and write a hold note for one of them.",
               "items": [
                   ("Names the correct owner for a diagnosis, a code, a release, a refund, and a privacy question.", False),
                   ("Declines to edit a clinical record and asks for clarification in neutral words.", True),
                   ("Identifies the governing issuance and checks publication, effective, service, and amendment dates.", False),
                   ("Records a source conflict and its resolution in the policy register.", False),
                   ("Writes a hold note with issue, source, owner, due date, and next action.", True),
                   ("Escalates a request to misrepresent a record to the compliance lead.", True),
               ],
               "placement": "Shadow your claims lead for one batch release. List every decision you saw and name its owner."},
    "quiz": [
        ("Who may change the diagnosis recorded for a dialysis session?",
         ["The claims officer", "The authorized treating clinician", "The clerk, if the batch needs it", "PhilHealth"], 1,
         "An administrative edit would change the clinical evidence."),
        ("An SOP conflicts with a later PhilHealth circular. What goes in the policy register?",
         ["Nothing; follow the SOP", "The workflow affected, the later source and its effective date, the owner, and the decision", "Only the SOP number", "The vendor&rsquo;s opinion"], 1,
         "The register records which source governs and who decided."),
        ("Which date usually decides which version of a rule governs a claim?",
         ["The date the binder was printed", "The service date", "The filing date", "The remittance date"], 1,
         "Read it against the effective date and transition clauses."),
        ("Which source governs when a vendor help page conflicts with a PhilHealth advisory?",
         ["The vendor help page", "The advisory", "Whichever is newer", "The job posting"], 1,
         "A vendor page explains steps; it cannot override an issuance."),
        ("What is the risk of a hold note without a due date?",
         ["None", "No one owns the clock, so a filing period can lapse unnoticed", "PhilHealth rejects it", "It becomes a denial"], 1,
         "Holds need an owner and a date."),
        ("Who releases a refund to a patient?",
         ["The clerk", "Finance, through the approved process", "The liaison", "The nurse"], 1,
         "Claims staff document the variance and route it."),
        ("What is the current hemodialysis package per qualifying session under Circular 2024-0023?",
         ["2,600 pesos", "4,000 pesos", "6,350 pesos", "990,600 pesos"], 2,
         "990,600 pesos is the annual maximum for 156 sessions."),
        ("How is the 6,350-peso package split?",
         ["5,000 facility and 1,350 professional", "6,000 facility and 350 professional", "3,650 facility and 350 professional", "It is not split"], 1,
         "3,650 and 350 was the July 2024 split of the 4,000-peso rate."),
        ("A supervisor asks you to relabel an acute kidney injury discharge as stage 5 to fit a batch. What do you do?",
         ["Relabel it", "Hold the claim, preserve the source, route the diagnosis question, and escalate the request", "Delete the claim", "Submit it separately as stage 5"], 1,
         "A request to misrepresent the record is escalated, not argued."),
        ("Where do you get written resolution when instructions stay unclear?",
         ["A social media group", "The PhilHealth Regional Office", "The vendor", "Another clinic"], 1,
         "Keep the written reply in the policy register."),
        ("Which phrase is the best way to ask a clinician about a record?",
         ["&ldquo;Please change this to stage 5.&rdquo;", "&ldquo;Please confirm the diagnosis documented for the session on September 7.&rdquo;", "&ldquo;Everyone codes it like this.&rdquo;", "&ldquo;PhilHealth wants stage 5.&rdquo;"], 1,
         "Neutral wording asks for the source to be checked."),
        ("An old binder shows 4,000 pesos per session. What do you do with it?",
         ["Throw it away", "Mark the page superseded with the newer issuance and date", "Keep using it", "Send it to PhilHealth"], 1,
         "Old claims may still need the older rule."),
        ("What does a circular do that an advisory usually does not?",
         ["Sets rules", "Announces holidays only", "Replaces the law", "Nothing different"], 0,
         "Advisories usually explain, remind, or set dates under existing rules."),
        ("Who owns code selection?",
         ["The clerk", "The coder or designated reviewer", "The patient", "The liaison"], 1,
         "Claims staff flag a mismatch; coders decide."),
        ("Why must every role have a named backup?",
         ["For payroll", "So a decision never waits on an absent person while a clock runs", "PhilHealth requires two signatures", "To share credit"], 1,
         "Clocks keep running when people are on leave."),
    ],
    "terms": [("Issuance", "An official PhilHealth document, such as a circular or an advisory."),
              ("Effective date", "The day a rule starts to apply."),
              ("Service date", "The day the patient was treated."),
              ("Hold", "A claim kept from release until a named owner resolves a named issue."),
              ("Policy register", "The facility&rsquo;s record of which rule governs each workflow, from when, and who decided."),
              ("PRO", "PhilHealth Regional Office.")],
    "readings": [("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
