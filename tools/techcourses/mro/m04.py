# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 04: Capture, Indexing, Late Entries, and Corrections. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer scanning a run sheet and checking the scanned image against the paper original.",
    "objectives": [
        "Capture a document against six metadata fields and a page-by-page quality check.",
        "Tell an indexing correction from a clinical correction, and name who may make each.",
        "Record a late entry with both of its dates and explain why backdating is falsification.",
        "Recognize risky copy-and-paste patterns in an electronic record and route them without accusation.",
        "Check every downstream copy after a correction.",
    ],
    "big": """
{{plain:A scanned page with no label is a photograph in a drawer. You know it is important, but not whose it is, which visit it belongs to, or whether a newer version exists. Labels turn a picture into evidence.}}
<p>The picture is useful, and it has one limit. A photograph in a drawer at least stays the same. Records change. A nurse corrects a weight. A physician amends an order. A page is rescanned because the first copy was faint. Each change is legitimate, and each one can also be made in a way that destroys trust in the whole chart.</p>
<p>Corrections are where trust is won or lost. A chart that shows its edits honestly survives an audit, even when it contains mistakes. A chart that silently overwrites is presumed unreliable, even where it happens to be right. This module is about capturing documents so they can be found, and correcting them so that anyone can see what changed, who changed it, and why.</p>
{{cards:Key terms for this module|Metadata::Data that describe a document: patient, encounter, type, date, author, version.|Indexing::Attaching a document to the right patient, encounter, and document type.|Authoritative copy::The version the facility treats as the official record.|Late entry::Documentation added after the time it describes, carrying both dates.|Electronic health record (EHR)::A digital record of a patient&rsquo;s health information kept and shared across a facility or system.|Audit trail::The system log of who viewed or changed what, when, and why.}}
""",
    "case": {"title": "The order on the wrong day", "html": """
<p>It is Thursday and you are working through the week&rsquo;s scans. Three things land on your desk within an hour.</p>
<p>First, in the chart of Mrs. Rosario Medina, 67, you find a physician order signed by Dr. Antonio Bautista, dated November 12, that changes her dialyzer to a larger size. It is attached to her November 10 session.</p>
<p>Second, the two-page treatment record for Mr. Danilo Cruz&rsquo;s Tuesday session was uploaded twice. In one copy, page 2 is too faint to read.</p>
<p>Third, Nurse Liza Fernandez stops at your door. &ldquo;I wrote 58.4 for Mrs. Medina&rsquo;s post-weight yesterday. It should be 57.4. Can you just fix it in the system? You have access.&rdquo;</p>
""", "questions": ["Which of these can you correct yourself, and which belong to someone else?",
                  "What must the system keep when you relink the order?",
                  "What will you do with the two uploads?",
                  "What do you say to Nurse Fernandez?"]},
    "sections": [
        ("capture", "Capture", "Six fields and a quality check", """
<p>Capture every document against six fields.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Example</th><th>What goes wrong without it</th></tr></thead>
<tbody>
<tr><td>Patient identifier</td><td>Full name, date of birth, patient number</td><td>The page is filed to the wrong person (Module 3)</td></tr>
<tr><td>Encounter</td><td>Session date and shift</td><td>An order is read as applying to the wrong session</td></tr>
<tr><td>Document type</td><td>Run sheet, order, laboratory result, consent</td><td>No one can find it when asked</td></tr>
<tr><td>Date of service</td><td>November 18, 2026</td><td>A late entry looks contemporaneous, or the reverse</td></tr>
<tr><td>Author</td><td>The nurse or physician who wrote it</td><td>Queries go to the wrong person</td></tr>
<tr><td>Version</td><td>Original, amended, superseded</td><td>Two versions are read as equally current</td></tr>
</tbody></table></div>
<p>Before accepting any scan, check it page by page: legible, the page count matching the paper source, the right way up, signatures present, and the patient matching on every page. A two-page run sheet scanned as one page is not &ldquo;mostly captured.&rdquo; Incomplete or poor scans go to a rescan queue, never to the chart with a sticky note promising to fix them later.</p>
<h3>Paper originals</h3>
<p>For each document class, the records manual should say whether the paper original or the electronic image is the authoritative copy. Write it down; do not leave staff to guess. If paper is kept, track it like any valuable object: checked out, returned, transferred, or disposed of only with a record of who, when, and why. A folder that leaves the records room without a check-out entry is a custody break, even if it comes back the same afternoon.</p>
{{scene:Page two of two|<p>A scanned run sheet for Mrs. Lydia Panganiban looks complete: one page, signed, legible. The paper original, still in the tray, has a second page with the nurse&rsquo;s note about a hypotensive episode and the saline given.</p>
<p>The clerk rejects the scan and rescans both pages. A month later, when the attending physician reviews why Mrs. Panganiban&rsquo;s dry weight was changed, the note is there.</p>
<p class="tc-scene-take">A page count check takes three seconds and catches the one page that explains everything else.</p>}}
"""),
        ("two", "Two corrections", "Indexing correction or clinical correction", """
{{fig:mro04_corrections}}
<p>Every correction falls into one of two kinds, and the difference decides who may make it.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Indexing correction</th><th>Clinical correction</th></tr></thead>
<tbody>
<tr><td>What is wrong</td><td>Where the document is filed</td><td>What the document says</td></tr>
<tr><td>Example</td><td>An order attached to the wrong session of the same patient</td><td>A wrong weight written on the run sheet</td></tr>
<tr><td>Who corrects</td><td>The records officer, through the authorized workflow</td><td>The author, or an authorized clinician</td></tr>
<tr><td>What is preserved</td><td>Before and after values, reason, actor, time</td><td>The original entry, still legible; the new entry dated and signed</td></tr>
<tr><td>Your job</td><td>Make the change and check downstream copies</td><td>Log the request, route it, and verify closure</td></tr>
</tbody></table></div>
<p>A useful test: would the correction change any clinical fact a reader relies on? If yes, it is clinical, and it belongs to the author, even when you have system access to change it. Having the access is not the same as having the authority.</p>
<p>Note one boundary case. Moving a document between two different patients&rsquo; charts is not a simple indexing fix. It is an identity correction, and it follows the stricter resolution steps in Module 3.</p>
<h3>Late entries keep two dates</h3>
<p>A late entry is documentation added after the time it describes. It is legitimate and common: a nurse who was managing a falling blood pressure writes her note after the patient is stable. A late entry carries <strong>two dates</strong>: the date of service it describes, and the actual date and time it was written. It carries the author&rsquo;s signature and links to the original session.</p>
<p>Backdating a late entry, so that it looks as if it were written at the time, is falsification. It does not matter that the content is true. The date is a statement too, and a false date makes the entry false.</p>
<h3>On paper</h3>
<p>On a paper record, correct with a single line through the error, leaving the original legible. Write the correction nearby with initials, date, and time. No correction fluid, no overwriting, no torn-out or rewritten pages, no pasted labels covering the original.</p>
{{call:Never clean up a chart before an inspection by removing, rewriting, or backdating entries. An honest deficiency is a finding the unit can fix. An altered record is misconduct, and it makes every other page in the chart suspect.}}
{{scene:Same patient, wrong session|<p>A records officer finds a potassium bath order dated November 12 filed under Mr. Edwin Salonga&rsquo;s November 10 session. She relinks it to November 12 through the indexing workflow, and the system records the original link, the new one, the reason, and her name.</p>
<p>She then asks the charge nurse whether anyone read the order on November 10. No one had; the nurse on that day followed the standing order. Nothing clinical needs to change, and that answer goes into the correction note.</p>
<p class="tc-scene-take">An indexing correction is yours to make. Whether it mattered clinically is a question for the clinical team.</p>}}
"""),
        ("copy", "Copied text", "Copy and paste in the electronic record", """
<p>Electronic health records (EHRs) make it easy to copy yesterday&rsquo;s note forward. For a patient who dialyzes three times a week, the temptation is strong: much of today really is the same as Monday.</p>
<p>A systematic review and analysis of safety events, carried out by a United States patient-safety partnership, found that copy and paste can carry outdated or wrong information forward. The partnership recommended that copied text be <strong>identifiable, attributable to its source, and reviewed</strong> before signing.[[mro_tsou2017]] Copying is not forbidden. Copying without reading is the problem.</p>
<p>Records staff are well placed to notice one pattern: the same pre-dialysis weight and blood pressure on several consecutive run sheets. Real patients do not weigh exactly 61.0 kg with a blood pressure of 140/80 on six sessions in a row. The pattern calls for clinical review. It is not proof of error, because some patients really are stable and some machines round values. Route it to the Dialysis Clinical Head with the sessions listed, without accusation, and let the clinical team explain.</p>
<p>The same discipline applies to coded fields. Module 5 covers diagnosis codes from the International Classification of Diseases, 10th Revision (ICD-10), and how to question a note rather than correct it.</p>
{{key:After any correction, ask whether the document already traveled: to a claim, a registry extract, a released copy, or a transfer packet. If it did, those copies need correcting too.}}
{{scene:Six sessions at 61.0|<p>Reviewing run sheets for Mr. Florencio Abad, the records officer sees the same pre-dialysis weight, 61.0 kg, and blood pressure, 130/80, on six sessions in a row.</p>
<p>She lists the dates and sends them to the Dialysis Clinical Head with a neutral note: &ldquo;Identical values on six consecutive sessions, for review.&rdquo; The review finds the scale at station 3 had stopped updating its display, and a nurse had been copying the screen. The scale is replaced, and the clinical team rechecks Mr. Abad&rsquo;s actual weight trend.</p>
<p class="tc-scene-take">The pattern was not anyone&rsquo;s dishonesty. It was a broken scale, found because someone looked at the record.</p>}}
"""),
        ("why", "Why it matters", "What a correction trail protects", """
<p>It can feel fussy to preserve the original of a simple mistake. Consider who relies on the trail.</p>
<ul>
<li><strong>The patient.</strong> If a weight was wrong, the next session&rsquo;s fluid removal may have been planned on it. The trail shows what the team knew at the time.</li>
<li><strong>The nurse.</strong> An honest, dated correction shows she caught her own error. A silent overwrite makes it look as if she hid one.</li>
<li><strong>The unit.</strong> In a dispute, a payer audit, or a complaint, a chart with visible corrections is believed. A chart with invisible ones is not.</li>
</ul>
<p>The trail protects the people who make honest mistakes. That is the point to make when a colleague asks you to &ldquo;just fix it.&rdquo;</p>
"""),
    ],
    "debrief": ["""
<p><strong>Who corrects what?</strong> The misattached order is an indexing correction. It is the right patient, Mrs. Medina, and only the session link is wrong, so you relink it to November 12 through the authorized workflow. The wrong weight is a clinical correction. It belongs to Nurse Fernandez.</p>
<p><strong>What must the system keep?</strong> The original association with November 10, the new one with November 12, the reason, who made the change, and when. Then check whether the November 10 session already went into a claims batch or a registry extract with the order attached, and whether anyone acted on a dialyzer change before November 12.</p>
<p><strong>The uploads.</strong> Rescan the faint page from the paper original, check the page count, accept the complete legible version, and mark the duplicate as superseded with a reason. Keep the history; do not delete the earlier upload.</p>
<p><strong>What do you say to Nurse Fernandez?</strong> Something like: &ldquo;Thank you for catching it. I can&rsquo;t change your entry, but you can, and it&rsquo;s quick. Correct it through the clinical correction workflow so your original stays visible with your correction next to it. Then it&rsquo;s clear you caught your own mistake.&rdquo; Log her request and check that it is closed. If Mrs. Medina&rsquo;s next session has been planned from 58.4 kg, the charge nurse should know today.</p>
<p>Part of your role is to say no to a kind request in a way that leaves the colleague feeling helped rather than refused.</p>
"""],
    "skills": {"title": "Capture, quality check, and correction routing",
               "intro": "Scan and correct a set of fictional records while your preceptor observes.",
               "items": [
                   ("Captures all six metadata fields for each document.", False),
                   ("Checks every page for legibility, count, orientation, signatures, and patient match before accepting.", False),
                   ("Makes an indexing correction with before-and-after values, reason, actor, and time preserved.", False),
                   ("Routes a clinical correction to its author and does not edit clinical content, even with system access.", True),
                   ("Keeps both dates on a late entry and refuses to backdate.", True),
                   ("Identifies a repeated-value pattern and routes it for clinical review without accusation.", False),
                   ("Checks downstream copies after a correction.", False),
               ],
               "placement": "Pull five scans from last week and check them against the six fields and the page count. Note every one that would fail."},
    "terms": [("Metadata", "Data that describe a document."), ("Indexing", "Attaching a document to the right patient, encounter, and type."),
              ("Authoritative copy", "The official version of a record."),
              ("Late entry", "Documentation added after the time it describes."), ("EHR", "Electronic health record."),
              ("Audit trail", "The log of who changed what, when, and why.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["04"])
