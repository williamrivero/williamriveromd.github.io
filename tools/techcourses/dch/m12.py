# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 12: When the System Goes Dark: Downtime and Privacy. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a nurse comparing a paper downtime record with a laptop screen at a dialysis nurses' station.",
    "objectives": [
        "List the systems your unit depends on for orders, documentation, results, inventory, contacts, and claims.",
        "Define the minimum verified information needed to treat a patient safely, and what to do when it cannot be recovered.",
        "Run a paper downtime process with a designated source record and protected offline rosters.",
        "Reconcile identities, orders, treatments, results, and claims after restoration, with a second checker.",
        "Recognize a personal data breach, contain it, and get it to the privacy lead in time for the 72-hour notification rule.",
        "Explain why information system outages are a patient-safety risk, not only an IT problem.",
    ],
    "big": """
{{plain:Downtime is like a power cut in a kitchen. You can still cook if you know where the matches are, which recipes need the oven, and who is keeping track of what has already been served.}}
<p>The picture has a limit. In a kitchen, a dish cooked twice is wasted food. In a dialysis unit, an order applied from memory, a session recorded twice, or a patient list sent to the wrong group chat can harm a patient or break the law. Downtime planning is about knowing, in advance, where the verified information lives when the screens go dark.</p>
{{cards:Key terms for this module|Downtime::A period when an information system is unavailable, planned or not.|Source record::The record designated as authoritative during downtime.|Minimum safe data set::The information you must verify before treating a patient.|Reconciliation::Matching paper and electronic records after restoration, entry by entry.|Personal data breach::A security incident leading to accidental or unlawful destruction, loss, alteration, or disclosure of personal data.|Privacy lead::The data protection officer or designated person who assesses breaches under the facility&rsquo;s policy.|NPC::National Privacy Commission.}}
""",
    "case": {"title": "The chart goes dark", "html": """
<p>At 07:40 on a Tuesday, the electronic record at your sixteen-station unit fails. IT says it may be down for the day. Two patients have new orders written yesterday afternoon that nobody printed. The receptionist, Ms. Daisy Cruz, proposes sending the full patient census, with names, phone numbers, and hepatitis status, to the staff&rsquo;s personal group chat so everyone can see who is coming.</p>
<p>When the system returns at 15:00, three patients appear twice for the same day, and one paper treatment record has no matching electronic entry.</p>
""", "questions": ["Which treatments can go ahead, and on what information?",
                  "What do you say to Ms. Cruz, and what do you do if the census has already been sent?",
                  "How will you check the paper records against the recovered system?"]},
    "sections": [
        ("why", "Why it matters", "Outages are a clinical risk", """
<p>Health systems are increasingly targets of ransomware and other attacks, and the harm spreads beyond the hospital attacked. After a ransomware attack on one United States health system, the census and ambulance arrivals at adjacent emergency departments rose sharply.[[dch_dameff2023]] At the same untargeted adjacent hospitals, cardiac arrests increased during the attack phase, and survival with good neurologic outcome after out-of-hospital arrest fell.[[dch_pham2024]] These are observational studies of single events, but they show that losing information systems changes care well beyond the computer room.</p>
<p>A dialysis unit depends on current orders, the last laboratory results, infection status, access details, and contact numbers. When those vanish, the risks are treatment from memory, missed results, and improvised sharing that breaks privacy law.</p>
{{key:Know where the verified information is before the network fails.}}
"""),
        ("minimum", "The minimum", "The minimum safe data set", """
{{fig:dch12_minimum}}
<p>Agree in advance what must be verified before any patient is treated during downtime: identity, the current signed order, dry weight, access type, allergies, infection status, the most recent key laboratory values, and an emergency contact. Keep this on a protected offline roster, printed or stored on an approved device, refreshed on a schedule, with old copies destroyed.</p>
{{call:Stop treatment for any patient whose current order cannot be verified. Ask the prescribing or covering physician to confirm the order directly and record it. Do not treat from memory or from an older order.}}
<p>Designate the source record during downtime, usually paper downtime forms, and assign owners: intake, orders, pending results, treatment entries, and a hold on claims for the affected period.</p>
"""),
        ("reconcile", "Reconciling", "Carrying the paper back across", """
{{fig:dch12_bridge}}
<p>When the system returns, every downtime entry must be carried back and checked, not retyped from memory. Reconcile patient identity, order versions, completed treatments, pending and resulted laboratory tests, transmissions to other systems, and duplicate encounters. Preserve the original timestamps and the fact that the entry was made from a downtime record. Use a second checker for any discrepancy with clinical or billing consequences.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Check</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Orders</td><td>The order used matches the signed order in force</td><td>Physician on duty</td></tr>
<tr><td>Treatments</td><td>Each paper record has one electronic entry, not zero or two</td><td>Head nurse</td></tr>
<tr><td>Results</td><td>Results received during downtime were seen and acted on</td><td>Named clinician</td></tr>
<tr><td>Claims</td><td>Claims for the downtime period held until treatments reconcile</td><td>Claims lead</td></tr>
</tbody></table></div>
<p>A cancer center in Ireland, hit by a national ransomware attack in May 2021, restored email on day 28 and cleared its reporting backlog only by day 210.[[dch_keogh2024]] Plan for downtime that lasts weeks, not hours.</p>
"""),
        ("privacy", "Privacy", "When personal data leak", """
<p>Health information is sensitive personal information under the Data Privacy Act.[[dch_ra10173]] Sending a census with names, numbers, and hepatitis status to a personal group chat is an unauthorized disclosure, however well meant. Under the National Privacy Commission&rsquo;s breach management rules, when notification is required, the NPC and affected individuals must be notified within 72 hours of knowledge or reasonable belief that a breach occurred.[[dch_npc1603]]</p>
{{fig:dch12_breach}}
{{flow:If it has already happened|Contain::Ask the sender to delete the message and the group members to delete copies, and record who confirmed.|Preserve::Keep a record of what was sent, to whom, and when.|Notify the privacy lead now::The privacy lead assesses whether notification is required and handles the NPC and patients.|Fix the cause::Provide an approved way to share the minimum information during downtime.}}
<p>The unit&rsquo;s job is to contain the problem and escalate it at once. The privacy lead&rsquo;s job is to assess and notify. Do not wait until the end of the shift; the clock starts at knowledge.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Which treatments go ahead?</strong> Patients whose identity, current order, and minimum safe data can be verified from the protected offline roster and paper records. The two patients with unprinted new orders wait until the prescriber confirms the orders directly; record the confirmation on the downtime form.</p>
<p><strong>Ms. Cruz and the census.</strong> Stop it before it is sent, and use the approved offline roster, sharing only what each person needs. If it has already been sent, ask for deletion, record who confirmed, and notify the privacy lead immediately; the 72-hour clock may already be running.</p>
<p><strong>Reconciliation.</strong> Assign a verifier and a second checker. Match each paper treatment to exactly one electronic entry, resolve the three duplicates and the one missing entry against the paper source, and hold claims for the period until the treatments reconcile. Review the event at the next quality meeting and schedule a downtime drill.</p>
"""],
    "skills": {"title": "Downtime treatment, reconciliation, and breach escalation",
               "intro": "Run a downtime simulation for one shift and a restoration with a preceptor and two role players.",
               "items": [
                   ("Treats only from verified identity, current orders, and the minimum safe data set.", True),
                   ("Holds treatment on an unverifiable order until the prescriber confirms it.", True),
                   ("Prevents unauthorized sharing of patient lists.", True),
                   ("Designates the downtime source record and owners for intake, orders, results, and claims.", False),
                   ("Reconciles each paper entry to exactly one electronic entry with a second checker.", False),
                   ("Holds claims for the downtime period until reconciled.", True),
                   ("Contains a suspected breach and notifies the privacy lead at once.", True),
               ],
               "placement": "Print your unit&rsquo;s offline roster, check that it is current and protected, and run a one-hour downtime drill on a quiet shift."},
    "quiz": [
        ("What happened at adjacent emergency departments after a ransomware attack on a nearby health system?",
         ["Nothing", "Census and ambulance arrivals rose sharply", "They closed", "They improved"], 1,
         "Harm spreads beyond the target."),
        ("At untargeted adjacent hospitals during the attack, what happened to cardiac arrests?",
         ["They fell", "They increased", "No change", "Not measured"], 1,
         "Observational, single event."),
        ("A new order written yesterday cannot be retrieved. What do you do?",
         ["Use yesterday&rsquo;s previous order", "Ask the prescriber to confirm directly before treatment", "Guess", "Skip the session without asking"], 1,
         "Treat only from verified information."),
        ("Which belongs in the minimum safe data set?",
         ["Billing code", "Current order, dry weight, access, allergies, infection status, last key results", "Insurance card number only", "Photograph"], 1,
         "What you must verify before treating."),
        ("Reception proposes sending the census to a personal group chat. What is it?",
         ["Efficient", "An unauthorized disclosure of sensitive personal information", "Allowed in emergencies", "Fine if deleted later"], 1,
         "Use the approved offline roster."),
        ("Within how many hours must the NPC be notified when notification is required?",
         ["24", "48", "72", "Within a month"], 2,
         "From knowledge or reasonable belief that a breach occurred."),
        ("Who assesses whether a breach requires notification?",
         ["The receptionist", "The designated privacy lead", "The IT vendor", "The patients"], 1,
         "The unit contains and escalates at once."),
        ("After restoration, three patients appear twice. What must happen before billing?",
         ["Submit both", "Reconcile against the paper source and hold claims for the period", "Delete one at random", "Nothing"], 1,
         "Duplicate claims are billing errors."),
        ("Why use a second checker during reconciliation?",
         ["Tradition", "Discrepancies with clinical or billing consequences need independent verification", "To slow things down", "IT requires it"], 1,
         "Two sets of eyes on consequential changes."),
        ("How should downtime entries be carried into the restored record?",
         ["Retyped from memory", "From the paper source, preserving original timestamps and provenance", "Summarized", "Ignored"], 1,
         "Provenance matters."),
        ("What makes an offline roster useful?",
         ["Size", "Current version, authorized access, necessary fields, and a tested retrieval process", "Color", "Being on a personal phone"], 1,
         "And destroy old copies."),
        ("How long might recovery from a major cyberattack take?",
         ["Hours", "Weeks to months", "A day", "Minutes"], 1,
         "A cancer center cleared its backlog by day 210."),
        ("Under the Data Privacy Act, health information is:",
         ["Public", "Sensitive personal information", "Unregulated", "Owned by the clinic"], 1,
         "It needs a lawful basis to be processed and shared."),
        ("The census was already sent. What first?",
         ["Wait to see if anyone complains", "Contain: ask for deletion and record confirmations, then notify the privacy lead", "Delete the group", "Inform the media"], 1,
         "Contain, preserve, escalate."),
        ("Who reconciles orders after downtime?",
         ["The receptionist", "The physician on duty or designated prescriber", "The vendor", "The patient"], 1,
         "Each item needs a named owner."),
    ],
    "terms": [("Downtime", "A period when an information system is unavailable."),
              ("Source record", "The authoritative record during downtime."),
              ("Minimum safe data set", "Information that must be verified before treatment."),
              ("Reconciliation", "Matching paper and electronic records after restoration."),
              ("Personal data breach", "Unauthorized loss, alteration, or disclosure of personal data."),
              ("Privacy lead", "The person who assesses breaches and notifications."),
              ("NPC", "National Privacy Commission.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
