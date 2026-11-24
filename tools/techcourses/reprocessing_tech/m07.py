# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 07: Identity and Chain of Custody. v0.1 RT07."""

MODULE = {
    "image_alt": "Two reprocessed dialyzers side by side on a storage rack, with similar labels, and a technician comparing them against a printed list.",
    "objectives": [
        "Explain why a wrong-patient dialyzer is a serious event, even when the dialyzer is clean.",
        "Label a dialyzer with two identifiers and the fields the program requires, before its first use.",
        "Use two identifiers and read-back at every hand-over.",
        "Recognize the risk of similar names and use the unit&rsquo;s alert system.",
        "Keep the use count and history continuous: never reset, never transfer a label.",
    ],
    "big": """
{{plain:Think of the claim stub at a shoe repair shop. You hand over your shoes, get a numbered stub, and the shop ties the same number to the shoes. When you return, the stub and the tag must match, or you walk out in someone else&rsquo;s shoes.}}
<p>The picture has a limit. Shoes that are not yours are a nuisance. A dialyzer that is not yours carries traces of another person&rsquo;s blood and has been tested against another person&rsquo;s baseline. The United States federal rule restricts reuse to the same patient;[[rt_cfr494]] every program does. So identity is not one check. It is a chain of checks, and a break anywhere makes every later check meaningless.</p>
{{cards:Key terms for this module|Two identifiers::Two independent facts that identify a patient, such as full name and date of birth, or name and unit number.|Read-back::Repeating information aloud so the other person can confirm it.|Chain of custody::The record of every person who held the dialyzer, when, and what they checked.|Name alert::A marker the unit uses when two patients have similar names.|Use count::The number of treatments the dialyzer has been used for, including the first.|Traceability::Being able to follow one dialyzer&rsquo;s whole history from first use to discard.}}
<p>Your job is to make it impossible for a dialyzer to reach the wrong patient without someone noticing, and to keep its history whole from first use to discard.</p>
""",
    "case": {"title": "Two Santoses", "html": """
<p>At 11:40 on a Thursday, the reuse room at a unit in Batangas holds two processed dialyzers on the same shelf. One belongs to Mr. Ramon Santos, 61, on the 1 p.m. shift. The other belongs to Mr. Ramil Santos, 45, on the 5 p.m. shift. Both are the same model. Their labels are handwritten.</p>
<p>The relief technician, Mr. Paolo Garcia, is asked by a nurse to bring &ldquo;Santos&rsquo;s dialyzer&rdquo; for the 1 p.m. shift. He picks the one at the front of the shelf. The nurse is in a hurry and says she will check it at the chair.</p>
""", "questions": ["Where can this chain break?",
                  "What should Mr. Garcia do before the dialyzer leaves the room?",
                  "What could the unit change permanently?"]},
    "sections": [
        ("why", "Why identity matters", "Why identity is the first gate", """
<p>A dialyzer used on the wrong patient exposes that patient to another person&rsquo;s blood residue and to any bloodborne virus that person carries. It also breaks every test result, because the volume test compares this dialyzer with its own baseline and the history belongs to someone else. Programs therefore treat a wrong-patient dialyzer as a serious event, report it, and assess the exposed patient for bloodborne infection.</p>
<p>Wrong-patient errors usually come from ordinary moments: similar names, a rushed hand-over, a label that is smudged, a dialyzer picked by position on a shelf. Each is preventable by a habit.</p>
{{key:Identity is the first gate. If it fails, nothing else about the dialyzer matters.}}
"""),
        ("label", "The label", "The label and what it carries", """
{{fig:rt07_label}}
<p>The label is applied before the first use, while the dialyzer is still sealed and the patient is present. It stays on the dialyzer until discard. The program decides the exact fields; most include these.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Patient full name and a second identifier</td><td>Two identifiers prevent confusion between similar names</td></tr>
<tr><td>Date of first use</td><td>Anchors the history and any time limit</td></tr>
<tr><td>Use number, updated each cycle</td><td>Prevents a sixth use</td></tr>
<tr><td>Date and time of the last processing</td><td>Links to storage time and expiry</td></tr>
<tr><td>Initials of the person who processed it</td><td>Accountability and traceability</td></tr>
</tbody></table></div>
<p>The federal rule in the United States requires labeling suitable for multiple reuse, and its surveyors check it.[[rt_cfr494]][[rt_cms_somh]] Labels must survive water and germicide; a label that fades is a label that fails. Do not write infection status on a label that other patients can read.</p>
{{stop:A label that is missing, unreadable, or does not match the record makes the dialyzer unidentified. Quarantine it. Never relabel from memory.}}
"""),
        ("custody", "Chain of custody", "The chain of custody", """
{{fig:rt07_custody}}
<p>Every time the dialyzer changes hands, the person giving and the person receiving check identity together. The record shows who, when and what was checked.</p>
{{flow:One dialyzer, one day|At the chair, end of treatment::Nurse confirms the label against the patient and closes the dialyzer for transport as the procedure directs.|Transport::In a covered, leak-proof tray to the dirty receiving area, never with clean items.|Receiving::Technician checks label against the receiving log and the eligibility list; notes time received.|Processing::Reprocessor record links to the dialyzer&rsquo;s identifier.|Storage::Placed in the patient&rsquo;s labeled slot, not by position or color alone.|Release to the nurse::Two people read the label against the patient record and, at the chair, the wristband (Module 10).}}
{{key:Pick by label and two identifiers, never by shelf position. Read it back, every time.}}
"""),
        ("names", "Similar names", "Similar names and other traps", """
<div class="table-wrap"><table>
<thead><tr><th>Trap</th><th>Habit that prevents it</th></tr></thead>
<tbody>
<tr><td>Same or similar surnames, especially common Filipino surnames</td><td>Name alert marker on labels and records; separate storage positions; always two identifiers</td></tr>
<tr><td>Same model of dialyzer</td><td>Never rely on model or color to identify</td></tr>
<tr><td>Verbal requests such as &ldquo;Santos&rsquo;s dialyzer&rdquo;</td><td>Ask for the full name and second identifier; read back</td></tr>
<tr><td>Handwritten, smudged labels</td><td>Printed or water-resistant labels; quarantine any unreadable label</td></tr>
<tr><td>Patients who change shift</td><td>Update the storage map the same day</td></tr>
</tbody></table></div>
"""),
        ("history", "One continuous history", "One continuous history", """
<p>The dialyzer&rsquo;s use count and history follow it from first use to discard. They are never reset, not after a failed cycle that was later passed, not after a repair of the record, and not after a transfer. A label is never moved from one dialyzer to another.</p>
<p>If the history is broken, for example a missing processing record or two labels that disagree, the dialyzer cannot be traced. An untraceable dialyzer is discarded under the program&rsquo;s procedure, and the break is reported so the cause can be found.</p>
{{key:A history that is reset or patched from memory is not a history. When in doubt, discard and report.}}
"""),
    ],
    "debrief": ["""
<p><strong>Where can the chain break?</strong> At the verbal request (&ldquo;Santos&rdquo; without a first name or second identifier), at the pick (front of the shelf rather than by label), at the hand-over (the nurse defers checking to the chair), and at the chair if the check there is rushed too. Each break alone could deliver the wrong dialyzer.</p>
<p><strong>What should Mr. Garcia do?</strong> Ask for the patient&rsquo;s full name and second identifier, find the dialyzer by its label, read the label aloud with the nurse against the patient record, and log the release time. If the labels are hard to read, he quarantines the doubtful dialyzer rather than guessing.</p>
<p><strong>What could the unit change?</strong> A name alert for the two Santoses, separate storage positions on different shelves, printed water-resistant labels, and a rule that no dialyzer leaves the room without a two-person read-back. Changing one patient&rsquo;s shift would also separate them in time.</p>
"""],
    "skills": {"title": "Labeling and hand-over drill",
               "intro": "Use synthetic patients with similar names and training dialyzers.",
               "items": [
                   ("Labels a new dialyzer with two identifiers and the required fields before first use.", True),
                   ("Checks a received dialyzer against the receiving log and eligibility list.", True),
                   ("Picks a dialyzer from storage by label and two identifiers, not by position.", True),
                   ("Asks for the full name and second identifier when given a surname only.", True),
                   ("Performs a two-person read-back at release.", True),
                   ("Quarantines a dialyzer with an unreadable label.", True),
                   ("States why a use count is never reset.", False),
               ],
               "placement": "Map every pair of similar names in your unit and check that each has a name alert and separate storage."},
    "quiz": [
        ("Why is a wrong-patient dialyzer serious even if it was perfectly cleaned?",
         ["It is not serious if it is clean", "It exposes the patient to another person&rsquo;s blood residue and makes every test result meaningless", "It only wastes money", "It changes the dialysis prescription"], 1,
         "Identity failure exposes the patient and invalidates the history."),
        ("A nurse asks for &ldquo;Santos&rsquo;s dialyzer.&rdquo; What do you do?",
         ["Bring the first Santos you find", "Ask for the full name and second identifier, then read back", "Bring both", "Ask the patient later"], 1,
         "A surname alone is not identification."),
        ("When should the label be applied?",
         ["After the first processing", "Before the first use, while the dialyzer is sealed and the patient is present", "At discard", "Only when there are similar names"], 1,
         "Labeling before first use anchors the history."),
        ("A label is smudged and you cannot read the second identifier. What do you do?",
         ["Rewrite it from memory", "Quarantine the dialyzer", "Use it if the first name is readable", "Move a label from another dialyzer"], 1,
         "Unidentified dialyzers are quarantined."),
        ("How should a dialyzer be picked from storage?",
         ["By shelf position", "By model and color", "By label and two identifiers", "By the date on the rack"], 2,
         "Position and model are not identity."),
        ("What should never appear on a label that other patients can read?",
         ["The patient&rsquo;s name", "The use number", "The patient&rsquo;s infection diagnosis", "The processing date"], 2,
         "Protect privacy; use a coded marker only if the program requires one."),
        ("A dialyzer&rsquo;s use count is unclear after a record error. What is the safest course?",
         ["Reset it to 1", "Guess the count", "Treat the history as broken: discard under the program and report", "Use it once more"], 2,
         "A broken history cannot prove eligibility."),
        ("Why does the record show who received the dialyzer at each step?",
         ["For payroll", "So the dialyzer can be traced and accountability is clear", "To count steps", "Because the patient asks"], 1,
         "Traceability depends on a named person at every hand-over."),
        ("Which practice best protects patients with similar names?",
         ["Storing their dialyzers side by side", "A name alert plus separate storage and two identifiers", "Using different dialyzer colors", "Remembering who is who"], 1,
         "Several layers together prevent mix-ups."),
        ("Under the United States federal rule, dialyzer reuse is limited to:",
         ["Any patient on the same shift", "The same patient", "Patients of the same blood type", "Family members"], 1,
         "Same-patient reuse is required."),
        ("May a label be moved from a cracked dialyzer to a new one of the same model?",
         ["Yes, if done carefully", "No; a new dialyzer starts a new history with a new label", "Yes, if the nurse agrees", "Yes, if the use count is copied"], 1,
         "Labels never move between devices."),
        ("How should used dialyzers travel to the reuse room?",
         ["In a pocket", "In a covered, leak-proof tray, separate from clean items", "With clean dialyzers to save trips", "Open on a cart"], 1,
         "Transport contains blood and keeps clean and dirty apart."),
    ],
    "terms": [("Two identifiers", "Two independent facts that identify a patient."),
              ("Read-back", "Repeating information aloud so the other person can confirm it."),
              ("Chain of custody", "The record of who held the dialyzer, when, and what they checked."),
              ("Name alert", "A marker used when two patients have similar names."),
              ("Traceability", "Being able to follow one dialyzer&rsquo;s history from first use to discard."),
              ("Wrong-patient event", "Use of a dialyzer on a patient it does not belong to.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "Labeling and records in a reuse program.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
