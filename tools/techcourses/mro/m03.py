# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 03: Patient Identity, Intake, and the Master Patient Index. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer at an intake desk comparing a referral letter with a patient's identification card.",
    "objectives": [
        "Identify a patient with two person-level identifiers and explain why a chair or shift number never counts.",
        "Search the master patient index with name variants before creating a chart.",
        "Describe how duplicate records and wrong-patient errors usually happen, using published evidence.",
        "Quarantine a contested document and resolve it through an independently verified channel.",
        "List every downstream record that must be checked after an identity correction.",
    ],
    "big": """
{{plain:A misfiled document is like a letter put in the wrong mailbox. The letter itself is correct. The address on the envelope is wrong. Whoever opens it next will read it, believe it, and act on it, because nothing inside the letter says it was meant for someone else.}}
<p>The picture is useful, and it has one limit. A wrong letter is usually noticed and returned. A wrong page in a dialysis chart often is not. It looks exactly like a right page. Every later step, from the claim to the registry row to the transfer packet, inherits whatever identity the page was filed under. Attach the wrong person at intake and every later step is wrong in a way that looks right.</p>
<p>Dialysis units carry particular risk. The same patients return three times a week for years, so staff feel they know everyone and stop checking. Relatives with the same surname often dialyze on the same shift. Filipino naming habits add variety: a maternal surname used as a middle name, a married surname, a nickname such as &ldquo;Jun&rdquo; or &ldquo;Baby&rdquo; that everyone uses but no document shows. And reprocessed dialyzers must return to exactly one person.</p>
{{cards:Key terms for this module|Master patient index (MPI)::The unit&rsquo;s list that links each person to exactly one chart number.|Person-level identifier::A fact about who the patient is, such as full name and date of birth, never where they sit.|Duplicate::Two records for one person.|Misfile::A correct document placed in the wrong patient&rsquo;s chart.|Overlay::One person&rsquo;s information written into another person&rsquo;s record, so two people share one chart.|Merge::Combining two records that belong to one person, through a controlled, authorized workflow.|PhilHealth Identification Number (PIN)::The member number issued by the Philippine Health Insurance Corporation.}}
""",
    "case": {"title": "Two Marias", "html": """
<p>At 9:40 a.m. a fax arrives from a hospital in Quezon City. It is a referral for &ldquo;Maria Reyes,&rdquo; born 1972, with no full birth date, asking you to schedule her for dialysis and attaching a hepatitis B surface antigen result marked <em>reactive</em>.</p>
<p>Your master patient index has two candidates. Maria Lourdes Reyes, born February 4, 1972, dialyzes on Monday, Wednesday, and Friday afternoons. Maria Luisa Reyes, born May 8, 1972, dialyzes on Tuesday, Thursday, and Saturday mornings. Both are hepatitis B negative on file.</p>
<p>The phone number printed on the fax does not match the hospital&rsquo;s number in your verified directory. It is Wednesday. Maria Lourdes Reyes is due at 1 p.m.</p>
""", "questions": ["Where does the referral go right now?",
                  "How will you verify which Maria it belongs to, and through which channel?",
                  "Who else needs to know before 1 p.m., and why?"]},
    "sections": [
        ("two", "Two identifiers", "Two identifiers, both about the person", """
<p>Use two approved person-level identifiers every time a document is filed, a chart is pulled, or a copy is released. Typically these are the full name and the date of birth, with the institutional patient number or the PhilHealth Identification Number (PIN) where your policy allows.</p>
<p>A station number, chair, shift, bed, or room describes <em>where</em> the patient is today. It does not describe <em>who</em> they are. Patients change chairs. Staff say &ldquo;the patient in chair 7&rdquo; and mean two different people on two different shifts. A location never counts as an identifier.</p>
<div class="table-wrap"><table>
<thead><tr><th>Acceptable identifiers</th><th>Never identifiers</th></tr></thead>
<tbody>
<tr><td>Full name, as written on a government ID</td><td>Station, chair, bed, or room number</td></tr>
<tr><td>Date of birth</td><td>Shift or day pattern (&ldquo;the MWF morning lady&rdquo;)</td></tr>
<tr><td>Institutional patient number</td><td>Nickname alone</td></tr>
<tr><td>PIN, where policy allows</td><td>&ldquo;The one with the fistula on the left&rdquo;</td></tr>
</tbody></table></div>
<h3>Search before you create</h3>
<p>Before assigning a new chart number, search the master patient index (MPI) with name variants. A patient who has dialyzed with you before, or whose records arrived from an earlier referral, may already exist under a slightly different name.</p>
<ul>
<li>Maiden and married surnames (Maria Santos-Reyes, Maria Santos, Maria Reyes)</li>
<li>Middle name present, absent, or reduced to an initial</li>
<li>Swapped first and last names</li>
<li>Spelling variants (Ma. and Maria; Jr. present or absent; Dela Cruz, de la Cruz, Delacruz)</li>
<li>Nicknames (Jun, Boy, Baby, Inday) written as the first name</li>
<li>Date of birth with day and month swapped (04/02 and 02/04)</li>
</ul>
<p>Record every alias and previous identifier you find, with its source. An alias written in the chart today saves the next records officer from creating a duplicate next year.</p>
{{fig:mro03_duplicates}}
"""),
        ("evidence", "The evidence", "How duplicates and wrong-patient errors really happen", """
<p>It is tempting to assume that duplicate records come from complicated system failures. The evidence says they mostly come from ordinary typing.</p>
<p>In a multisite study of 398,939 confirmed duplicate record pairs, the most frequently mismatched field was the middle name, in 58.3% of pairs. Most name mismatches were plain misspellings or swapped name order.[[mro_just2016]] Duplicates are mostly made at the front desk, by people in a hurry. The controls that prevent them are equally ordinary:</p>
<ul>
<li>a written naming convention (full middle name, never an initial when the full name is known; hyphenated surnames written one agreed way);</li>
<li>a required search routine before any new chart number is issued;</li>
<li>a monthly duplicate report, reviewed by a second person.</li>
</ul>
<h3>Some intuitive controls fail when tested</h3>
<p>One idea for preventing wrong-patient orders in an electronic record is to let staff open only one patient&rsquo;s record at a time. It sounds sensible. A randomized trial of 3,356 clinicians and 12.1 million orders tested it. Limiting users to one open record did not reduce wrong-patient orders compared with allowing four: 90.7 compared with 88.0 per 100,000 order sessions (odds ratio 1.03, 95% confidence interval 0.90 to 1.20).[[mro_adelman2019]] This was a large, well-designed trial, and it found no benefit. Good intentions are not evidence.</p>
<p>Other controls look more promising. In a large emergency-department cohort, showing the patient&rsquo;s photograph in the record banner was associated with fewer wrong-patient orders (adjusted odds ratio 0.57).[[mro_salmasian2020]] The study was observational, so it suggests benefit but does not prove it; units that adopted photographs may also have differed in other ways. A photograph is also personal information. Under the Data Privacy Act, it needs a documented lawful basis and a consent process before you start taking pictures at intake.</p>
<p>Closer to home, nursing teams in hemodialysis clinics name patient-identification errors as their main gap against the international patient-safety goals.[[mro_lima2023]] In other words, the people who work chairside already know this is where things go wrong.</p>
{{key:Verify identity at the point of action. Search before you create. Neither step takes more than a minute, and either can prevent a wrong-patient error that takes weeks to unwind.}}
"""),
        ("types", "Three kinds of error", "Duplicate, misfile, overlay", """
<p>Identity errors come in three kinds, and they are not equally dangerous.</p>
<div class="table-wrap"><table>
<thead><tr><th>Error</th><th>What happened</th><th>Main risk</th><th>How hard to undo</th></tr></thead>
<tbody>
<tr><td>Duplicate</td><td>One person has two charts</td><td>Half the history is invisible; tests are repeated; allergies are missed</td><td>Moderate: merge through the controlled workflow</td></tr>
<tr><td>Misfile</td><td>One page is in the wrong person&rsquo;s chart</td><td>Someone acts on another person&rsquo;s result</td><td>Moderate: move the page, then check where it traveled</td></tr>
<tr><td>Overlay</td><td>Two people now share one chart</td><td>Both patients&rsquo; care is built on mixed facts</td><td>Hard: every entry since the overlay must be sorted, author by author</td></tr>
</tbody></table></div>
<p>An overlay usually starts with a confident merge. Someone sees two charts for &ldquo;Rodel Santos&rdquo; with the same birth year, decides they must be the same man, and combines them. If they are two men, both now share one chart. That is why the rule below is so strict.</p>
"""),
        ("resolve", "Resolving", "Suspected duplicate or misfile", """
{{flow:Safe resolution|Stop::Halt further routing of the contested document.|Quarantine::Place it in a protected exception queue, filed to neither chart.|Notify::Tell health information management (HIM) and the clinical owner.|Verify independently::Use a trusted directory number, not the number printed on the suspicious document.|Resolve through the controlled workflow::Merge or reassign only with authorization, preserving both original identifiers.|Check downstream::Claims, registry rows, the dialyzer log, and any released copies.}}
<p>Two steps deserve more detail.</p>
<p><strong>Verify independently.</strong> If a document might be wrong, the contact details printed on it might be wrong too. A fax with a mistyped name may also carry a mistyped return number. In rare cases a request is deliberately false. Look up the sender in your own verified directory, or call the facility&rsquo;s main switchboard, and ask for the records office. Ask them to read <em>you</em> the identifiers. Do not read your candidates&rsquo; details to them.</p>
<p><strong>Check downstream.</strong> A document filed to the wrong chart may already have traveled. List every place it could have gone: a claim batch, a registry extract, a released copy, a transfer packet, the station assignment board. Each one needs the same correction.</p>
{{call:Never merge on a likely match. &ldquo;Probably the same person&rdquo; is the exact belief that produces an overlay, which is far harder to undo than a duplicate. If either candidate is scheduled today, alert the charge nurse now, so identity is checked at the bedside while you resolve the record. When the contested document carries a clinically important result, such as a reactive hepatitis test, the attending nephrologist needs to know too.}}
"""),
    ],
    "debrief": ["""
<p><strong>Where does the referral go?</strong> Into the protected exception queue, marked &ldquo;pending identity match,&rdquo; filed to neither Maria&rsquo;s chart. Do not schedule either Maria on the strength of it.</p>
<p><strong>How will you verify?</strong> Call the Quezon City hospital through the switchboard number in your verified directory, not the number on the fax. Ask for the records office, and ask them to give you the patient&rsquo;s full name, full date of birth, and a second identifier such as the hospital number or PIN. Do not read either Maria&rsquo;s details to the caller. Write down who confirmed, when, and how.</p>
<p><strong>Who else needs to know?</strong> The charge nurse, before 1 p.m. Maria Lourdes Reyes dialyzes this afternoon. If the reactive hepatitis B result turns out to be hers, her station assignment and the unit&rsquo;s infection-control precautions may need to change today. That is a clinical decision, so the charge nurse and the attending nephrologist need the facts now, labeled clearly as unverified. If the result belongs to neither Maria, the referral is for a new patient, and a new chart is created only after an MPI search confirms she is not already on file.</p>
<p><strong>And afterward?</strong> Leave a dated resolution note on whichever chart receives the document, and record both Marias&rsquo; full middle names as the way they are always to be filed.</p>
<p>One misfiled hepatitis result could have moved the wrong woman to an isolation station, or left the right woman on a shared machine. Part of your role is to stop a document before it reaches either chart.</p>
"""],
    "skills": {"title": "Identity verification and exception handling",
               "intro": "Process a fictional intake and a suspected misfile while your preceptor observes.",
               "items": [
                   ("Uses two person-level identifiers and rejects location-based identifiers.", True),
                   ("Searches the MPI with at least four name variants before creating a chart.", True),
                   ("Explains the difference between a duplicate, a misfile, and an overlay.", False),
                   ("Quarantines a contested document and files it to neither chart.", True),
                   ("Verifies through an independently trusted channel without disclosing either candidate&rsquo;s details.", True),
                   ("Alerts the charge nurse in parallel when treatment is imminent.", True),
                   ("Lists every downstream place a corrected record must be checked.", False),
               ],
               "placement": "Run your unit&rsquo;s duplicate report for last month, or ask IT for one, and review three pairs with your supervisor."},
    "terms": [("MPI", "Master patient index."), ("PIN", "PhilHealth Identification Number."),
              ("Duplicate", "Two records for one person."), ("Misfile", "A correct document in the wrong chart."),
              ("Overlay", "Two people&rsquo;s information combined into one record."),
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
