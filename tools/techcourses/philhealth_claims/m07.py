# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 07: Returned Claims, Denials, and Escalation."""

MODULE = {
    "image_alt": "Two claims staff, seen from behind, pin a letter to a chronology board of linked cards.",
    "objectives": [
        "Distinguish a local validation error, a returned claim, a denial, and a payment dispute.",
        "Read the actual notice, verify its clock, and assign the deficiency to its source owner.",
        "Build a case chronology from service date to next follow-up, keeping the original record and notice intact.",
        "Investigate a duplicate-billing denial before accepting it.",
        "Write a short, specific request to the PhilHealth Regional Office through an authorized channel.",
    ],
    "big": """
{{plain:A returned claim is a form sent back with a sticky note: &ldquo;You missed a signature.&rdquo; Fix it and send it back through the same door. A denial is a decision: &ldquo;We will not pay this.&rdquo; Arguing with a decision needs a different door, a different clock, and someone with authority to sign.}}
<p>The picture has a limit. Notice labels and vendor screens do not always use the same words, and the same deficiency can be handled differently under different issuances. Always read the official notice, confirm the remedy and its deadline against the current issuance, and ask the PRO in writing when the route is unclear.</p>
{{fig:pc_fork}}
{{cards:Key terms for this module|Validation error::A problem your own system or the portal flags before acceptance.|Returned claim (RTH)::A claim sent back for correction or completion.|Denial::An adjudicated decision not to pay.|Motion for reconsideration::A formal request to review a denial, signed by an authorized person.|Chronology::The case&rsquo;s timeline from service to resolution.|Remedy::The action the notice and issuance allow, with its own deadline.}}
""",
    "case": {"title": "A return and a denial on the same morning", "html": """
<p>Two notices arrive on Monday. SIM-07A is returned: the agreement form for one session is incomplete. The verified response deadline is in twelve days. SIM-07B is denied as a &ldquo;duplicate claim.&rdquo; In the vendor screen, SIM-07B appears twice: one entry shows &ldquo;received,&rdquo; the other &ldquo;draft.&rdquo; The treatment records show two sessions on consecutive days.</p>
""", "questions": ["What are the two different routes, and their clocks?",
                  "How do you decide whether SIM-07B is really a duplicate?",
                  "What do you never do to the original notice or record?"]},
    "sections": [
        ("kinds", "Four different events", "Validation, return, denial, or payment?", """
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>What it means</th><th>First owner</th><th>Clock to verify</th></tr></thead>
<tbody>
<tr><td>Local validation error</td><td>The claim failed a check before acceptance</td><td>Claims officer</td><td>Your filing deadline</td></tr>
<tr><td>Returned claim</td><td>A deficiency to fix and refile through the linked process</td><td>Source owner of the deficiency</td><td>The response period on the notice</td></tr>
<tr><td>Denial</td><td>An adjudicated decision not to pay</td><td>Authorized reviewer</td><td>The remedy&rsquo;s period under the issuance</td></tr>
<tr><td>Payment dispute</td><td>Paid, but not the expected amount</td><td>Claims and finance together</td><td>The applicable remedy, if any</td></tr>
</tbody></table></div>
<p>Do not reuse the ordinary filing clock for a denial. Each remedy has its own period, which you confirm against the notice and the applicable issuance.[[pc_pc2024_0023]][[pc_pc2025_0019]] Returned claims are also a quality signal: twelve returns for the same missing signature mean a step in your process lets them out.</p>
"""),
        ("chronology", "The chronology", "Build the case chronology", """
<p>Every exception gets one chronology. It is the document that lets a reviewer, an auditor, or your successor understand the case in five minutes.</p>
{{fig:pc_chrono}}
<p>Record service dates, the initial submission and its receipt reference, the notice and when it was received, the owner and the verified deadline, each correction and approval, the refiling proof, and the next follow-up. Preserve the original record and notice; corrections are added with an audit trail, never written over.</p>
<p>A useful message to the PRO is short: the authorized claim reference, the dates, the notice reason, the facts, one precise question, and a secure return channel. Include only the identifiers the question needs.</p>
"""),
        ("duplicates", "Duplicates", "Is it really a duplicate?", """
<p>A duplicate denial can mean two different things. Either the same session was sent twice, often after a timeout (Module 6), or two distinct sessions were mistaken for one. The treatment records and the claim references decide which.</p>
{{flow:Investigating a duplicate denial|1. Match::The claim reference in the notice to the received record.|2. Compare::Treatment records for each session date.|3. Same session::Refer for authorized disposition; do not refile.|4. Distinct sessions::Assemble the chronology and evidence for the authorized reviewer, who decides on reconsideration or appeal.}}
{{call:Never turn a draft into a new claim to get around a notice, and never refile a received claim as if it were new. Correct the stated deficiency through the linked workflow.}}
"""),
    ],
    "debrief": ["""
<p><strong>Two routes.</strong> SIM-07A is a return: verify the notice receipt and the response deadline, send the incomplete agreement form to its documentation owner, review the corrected evidence, and refile through the linked process with an internal target several working days before the deadline. SIM-07B is a denial: capture the reason and receipt, then investigate before any action.</p>
<p><strong>Duplicate or distinct.</strong> Match the claim reference in the notice to the &ldquo;received&rdquo; entry. If the treatment records show two separate sessions on consecutive days, the denial may be wrong: build the chronology and evidence for the authorized reviewer, who decides whether reconsideration or appeal applies. If it is truly the same session, refer it for authorized disposition. Leave the &ldquo;draft&rdquo; entry alone.</p>
<p><strong>Never overwrite.</strong> Keep the original notice and record exactly as received.</p>
"""],
    "skills": {"title": "Notice triage and chronology",
               "intro": "Triage four fictional notices, build one chronology, and draft one message to the PRO.",
               "items": [
                   ("Classifies each notice as validation error, return, denial, or payment dispute.", False),
                   ("Verifies each remedy&rsquo;s clock against the notice and issuance.", True),
                   ("Routes each deficiency to its source owner.", False),
                   ("Investigates a duplicate denial using claim references and treatment records.", True),
                   ("Builds a chronology and preserves the original record and notice.", True),
                   ("Drafts a PRO message with minimum identifiers and one precise question.", False),
               ],
               "placement": "Review your unit&rsquo;s last ten returns with your claims lead and name the process step behind the most common reason."},
    "quiz": [
        ("Do you reuse the ordinary filing clock for every denial?",
         ["Yes", "No; verify the remedy-specific period against the notice and issuance", "Only for HD", "Only if late"], 1,
         "Each remedy has its own clock."),
        ("What should a useful PRO request include?",
         ["The whole chart", "Authorized claim reference, dates, notice reason, facts, one precise question, and a secure channel", "A complaint", "Nothing written"], 1,
         "Short and specific."),
        ("A return arrived October 10 with a verified October 22 deadline. What is a sensible internal target?",
         ["October 22", "Several working days earlier, for example October 17", "November 1", "No target needed"], 1,
         "Leave time for review."),
        ("Is a denial for &ldquo;duplicate&rdquo; automatically correct?",
         ["Yes", "No; compare claim references and treatment evidence first", "Only if PhilHealth says so twice", "Only on weekends"], 1,
         "Two distinct sessions can be mistaken for one."),
        ("Who signs a motion for reconsideration or an appeal?",
         ["The clerk", "The authorized signatory named in the facility adoption record", "The vendor", "The patient"], 1,
         "Authority is assigned in writing."),
        ("What must never be overwritten during a correction?",
         ["The chronology", "The original record and notice", "The internal target", "The ticket number"], 1,
         "Add corrections with an audit trail."),
        ("A returned claim is:",
         ["A decision not to pay", "A deficiency to fix and refile through the linked process", "A payment", "A privacy breach"], 1,
         "A denial is the decision."),
        ("Twelve claims are returned for the same missing signature. What is this?",
         ["Bad luck", "A process defect to fix at the step that let them out", "A reason to stop filing", "An audit finding"], 1,
         "Returns are a quality signal."),
        ("Which entry do you correct when a claim shows &ldquo;received&rdquo; and &ldquo;draft&rdquo;?",
         ["Make the draft a new claim", "Match the notice&rsquo;s claim reference to the received record and correct through the linked workflow", "Delete both", "Refile both"], 1,
         "Never turn a draft into a new claim."),
        ("A claim is paid, but less than expected. Who owns the first look?",
         ["The patient", "Claims and finance together", "The vendor", "The nurse"], 1,
         "Document the variance and review the remedy."),
        ("Where do you confirm the remedy and deadline when the notice is unclear?",
         ["A vendor forum", "Written guidance from the PRO and the applicable issuance", "A colleague&rsquo;s memory", "The patient"], 1,
         "Keep the written reply."),
        ("What is the first entry in a case chronology?",
         ["The refiling proof", "The service date or dates", "The ticket number", "The remittance"], 1,
         "Service comes first."),
        ("The same session was really sent twice after a timeout. What next?",
         ["Appeal", "Refer for authorized disposition; do not refile", "Send a third time", "Delete the receipt"], 1,
         "This is why Module 6 says check before resending."),
        ("Which identifiers go in a message to the PRO?",
         ["Everything you have", "Only those the question needs", "None", "The patient&rsquo;s whole history"], 1,
         "Minimum necessary data."),
        ("Why keep one chronology per case?",
         ["For decoration", "So anyone can understand the case quickly and the trail survives staff changes", "PhilHealth collects it daily", "To replace the claim"], 1,
         "It protects the claim and the facility."),
    ],
    "terms": [("Returned claim", "A claim sent back for correction or completion (RTH)."),
              ("Denial", "An adjudicated decision not to pay."),
              ("Motion for reconsideration", "A formal request to review a denial."),
              ("Chronology", "The case timeline from service to resolution."),
              ("Remedy", "The action allowed by the notice and issuance, with its own deadline."),
              ("RTH", "Return to hospital.")],
    "readings": [("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
