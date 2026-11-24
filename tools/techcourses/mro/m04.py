# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 04: Capture, Indexing, Authentication, and Corrections. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer feeding a treatment record into a document scanner and checking the page count on a monitor.",
    "objectives": [
        "Scan and index a source document against six metadata fields.",
        "Run a quality check before accepting a scan.",
        "Tell an indexing correction, which the records officer makes, from a clinical correction, which only the author makes.",
        "Handle late entries and copied text so that their origin stays visible.",
        "Track paper originals through custody.",
    ],
    "big": """
{{plain:A scanned page with no metadata is a photograph in a drawer. Metadata &mdash; who, which session, what kind of document, when, which version &mdash; turns an image into evidence.}}
<p>Corrections are where trust is won or lost. A chart that shows its edits honestly survives an audit; a chart that silently overwrites is presumed unreliable even where it is right.</p>
{{cards:Key terms for this module|Metadata::Data that describe a document: patient, encounter, type, date, author, version.|Authoritative copy::The version the facility treats as the official record.|Late entry::Documentation added after the time it describes.|Electronic health record (EHR)::Electronic health record.|Audit trail::The system log of who changed what, when, and why.}}
""",
    "case": {"title": "The order on the wrong day", "html": """
<p>While reviewing scans you find a signed physician order attached to the November 10 session of fictional patient SIM-041. The order is dated November 12 and changes the dialyzer. The same week, a two-page treatment record was uploaded twice, and in one copy page 2 is too faint to read. A nurse asks whether you can &ldquo;just fix&rdquo; a wrong weight she wrote on yesterday&rsquo;s run sheet.</p>
""", "questions": ["Which of these can you correct yourself, and which belong to someone else?",
                  "What must the system keep when you relink the order?",
                  "What will you do with the two uploads?"]},
    "sections": [
        ("capture", "Capture", "Six fields and a quality check", """
<p>Capture every document against six fields: patient identifier, encounter (session date and shift), document type, date of service, author, and version. Before accepting a scan, check legibility, page count against the source, orientation, signatures present, and patient match on every page. Incomplete scans go to a rescan queue, never to the chart with a note to fix later.</p>
<p>For each document class the records manual should declare whether the paper original or the electronic image is the authoritative copy. Track paper originals through check-out, return, and authorized transfer or disposition. A folder that leaves the records room without a check-out entry is a custody break.</p>
"""),
        ("two", "Two corrections", "Indexing correction or clinical correction", """
{{fig:mro04_corrections}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Indexing correction</th><th>Clinical correction</th></tr></thead>
<tbody>
<tr><td>Example</td><td>Order attached to the wrong session of the same patient</td><td>Wrong weight written on the run sheet</td></tr>
<tr><td>Who corrects</td><td>Records officer, through the authorized workflow</td><td>The author, or an authorized clinician</td></tr>
<tr><td>What is preserved</td><td>Before and after values, reason, actor, time</td><td>Original entry legible; new entry dated and signed</td></tr>
<tr><td>Your job</td><td>Make the change and check downstream copies</td><td>Log the request, route it, verify closure</td></tr>
</tbody></table></div>
<p>A late entry keeps <strong>two dates</strong>: the date of service it describes and the actual date and time it was written, with the author&rsquo;s authentication and a link to the original session. Backdating a late entry to look contemporaneous is falsification. On paper: a single line through the error, the original still legible, the correction nearby, with initials, date, and time; no correction fluid, overwriting, or torn-out pages.</p>
{{call:Never clean up a chart before an inspection by removing, rewriting, or backdating entries. An honest deficiency is a finding; an altered record is misconduct.}}
"""),
        ("copy", "Copied text", "Copy and paste in the electronic record", """
<p>Electronic health records (EHRs) make it easy to copy yesterday&rsquo;s note forward. A systematic review and safety-event analysis by a United States patient-safety partnership found that copy and paste can carry outdated or wrong information forward, and recommended that copied text be <strong>identifiable, attributable to its source, and reviewed</strong> before signing.[[mro_tsou2017]]</p>
<p>A practical audit signal: the same pre-dialysis weight and blood pressure on several consecutive run sheets. That pattern calls for clinical review; it is not proof of error. Route it to the Dialysis Clinical Head without accusation.</p>
{{key:After any correction, ask whether the document already traveled &mdash; to a claim, a registry extract, or a released copy. If it did, those copies need correcting too.}}
"""),
    ],
    "debrief": ["""
<p><strong>Who corrects what.</strong> The misattached order is an indexing correction you make through the authorized workflow, because it is the right patient and only the session link is wrong. The wrong weight is a clinical correction: the nurse corrects it herself through the clinical workflow, leaving the original legible.</p>
<p><strong>What the system keeps.</strong> The original association, the new one, the reason, who made the change, and when. Then check whether the November 10 session already went into a claims batch or registry extract.</p>
<p><strong>The uploads.</strong> Rescan the faint page, verify the page count against the paper source, accept the legible version, and mark the duplicate superseded with a reason. Keep the history.</p>
"""],
    "skills": {"title": "Capture, quality check, and correction routing",
               "intro": "Scan and correct a set of fictional records with a preceptor.",
               "items": [
                   ("Captures all six metadata fields and checks every page before accepting.", False),
                   ("Makes an indexing correction with before-and-after values, reason, actor, and time preserved.", False),
                   ("Routes a clinical correction to its author and does not edit clinical content.", True),
                   ("Keeps both dates on a late entry and refuses to backdate.", True),
                   ("Checks downstream copies after a correction.", False),
               ],
               "placement": "Pull five scans from last week and check them against the six fields and the page count."},
    "terms": [("Metadata", "Data that describe a document."), ("Authoritative copy", "The official version of a record."),
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
