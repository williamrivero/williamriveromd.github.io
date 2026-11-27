# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 02: The Dialysis Chart and the Evidence of Care. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer comparing a hemodialysis run sheet with a dialyzer reprocessing logbook at a desk.",
    "objectives": [
        "List what belongs in a longitudinal hemodialysis chart and how often key items must be renewed.",
        "Explain which document proves a session was authorized, which proves it was delivered, and which prove it was safe.",
        "Trace one session from its run sheet to its dialyzer, water, and machine records.",
        "Classify each expected item as present, deficient, unavailable, or not applicable, and give each gap an owner.",
        "Recognize a deficiency that must reach the clinical team before the next treatment.",
    ],
    "big": """
{{plain:Think of a delivered parcel. The order form shows someone asked for it. The delivery receipt shows it arrived. The warehouse log shows it was packed safely and sent to the right address. Lose any one of the three and you cannot prove the whole story. Every hemodialysis (HD) session is a parcel of the same kind, delivered three times a week, for years.}}
<p>The picture is useful, and it has one limit. A lost parcel can be replaced. A dialysis session cannot be repeated for yesterday. If the paperwork for a session is missing, no one can go back and gather it later. The evidence exists only if someone wrote it down at the time, and only if someone filed it where it can be found.</p>
<p>Every session must answer three questions. Was it authorized? Was it delivered? Was it safe? A different document answers each one, and an inspector, a payer such as the Philippine Health Insurance Corporation (PhilHealth), a lawyer, or a worried family member may ask all three. This module is about knowing which document answers which question, and noticing the moment one goes missing.</p>
{{cards:Key terms for this module|Longitudinal chart::The patient&rsquo;s record for as long as they dialyze with you, holding everything from intake onward.|Run sheet::The per-treatment flow sheet: weights, blood pressures, duration, events, medicines, dialyzer, signatures.|Standing order::The current dialysis prescription that applies to every session until a physician changes it.|Reprocessing::Cleaning, testing, and disinfecting a dialyzer so it can be reused by the same patient.|Deficiency::A required item that is unsigned, illegible, outdated, incomplete, or missing.|PhilHealth Dialysis Database (PDD)::The Philippine Health Insurance Corporation&rsquo;s registry of patients eligible for the hemodialysis package.}}
""",
    "case": {"title": "Reuse five, entry missing", "html": """
<p>It is Friday afternoon and you are doing the weekly chart audit. You open the chart of Mr. Ernesto Galang, 61, who dialyzes on Monday, Wednesday, and Friday mornings.</p>
<p>The November 18 run sheet is signed by the nurse, Ms. Joy Pangilinan. It shows a pre-dialysis weight of 64.2 kg, both blood pressures, and dialyzer D-044-07, reuse 5. The final weight box is blank.</p>
<p>You walk to the reprocessing room and open the logbook. Dialyzer D-044-07 shows reuse 4 on November 15. There is nothing after that. Mr. Galang&rsquo;s dialyzer issue record shows 26 dialyzers issued to him this calendar year.</p>
<p>His next session is Monday at 6 a.m.</p>
""", "questions": ["Which items are deficient, and who owns each one?",
                  "Why is the missing reprocessing entry more than a paperwork gap?",
                  "How many dialyzers remain in his annual allowance, and does anyone need to know before Monday?"]},
    "sections": [
        ("longitudinal", "The chart", "The longitudinal chart", """
<p>A hemodialysis patient is not a one-visit patient. Most dialyze two or three times a week for years, so their chart grows into a long record that many people read. The longitudinal chart is kept for as long as the patient dialyzes with you. It usually holds:</p>
<ul>
<li>intake demographics and identifiers;</li>
<li>the referral and the clinical abstract from the referring facility;</li>
<li>the initial physician assessment and problem list;</li>
<li>standing dialysis orders, which the posted Department of Health (DOH) assessment tool expects to be updated <strong>quarterly</strong>;</li>
<li>consent for hemodialysis, updated <strong>annually or as needed</strong>;</li>
<li>laboratory and imaging results;</li>
<li>the current medication list;</li>
<li>nutrition, patient-education, and social-work notes;</li>
<li>the vascular access history;</li>
<li>hospitalizations and their discharge summaries;</li>
<li>an advance directive, or a documented statement that none exists;</li>
<li>PhilHealth Dialysis Database (PDD) registration.[[dch_doh_rao_tool]]</li>
</ul>
<p>Two renewal dates on that list catch units out more than any others. A standing order signed in January is out of date by April. A consent signed last year needs renewal this year. Neither one announces itself. Build a calendar of renewal dates for every patient, and look ahead two weeks every Monday.</p>
<p>The laboratory section is not only clinical. The Philippine Health Insurance Corporation (PhilHealth) sets a minimum standard of care for the hemodialysis package that names scheduled laboratory tests, including serum albumin every three months and a hepatitis profile every six months as indicated.[[mro_ph2024ts]] A missing quarterly albumin is therefore a clinical gap, a quality gap, and a claims-evidence gap at the same time.</p>
{{key:Keep a renewal calendar for standing orders and consents. An order that expires quietly is an order the nurse may still be following on Monday.}}
{{scene:The consent that ran out|<p>Mrs. Natividad Ocampo signed her hemodialysis consent on October 3 last year. On October 10 this year, her chart still holds only that form. No one noticed, because nothing about her treatment changed.</p>
<p>The records officer&rsquo;s renewal calendar flags it two weeks ahead. The charge nurse brings the new form to her Monday session, the attending physician explains it again, and Mrs. Ocampo signs. The audit three months later finds every consent current.</p>
<p class="tc-scene-take">Renewal dates do not announce themselves. A calendar is the only reliable reminder.</p>}}
{{fig:mro02_fig_02_longitudinal_chart_contents}}
"""),
        ("layers", "Three layers", "Authorized, delivered, safe", """
{{fig:mro02_layers}}
<p>Think of the evidence for a session as three layers stacked on one another.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Main evidence</th><th>Who writes it</th><th>Weak substitutes</th></tr></thead>
<tbody>
<tr><td>Was it authorized?</td><td>The signed, current standing order</td><td>The physician</td><td>A verbal instruction no one countersigned</td></tr>
<tr><td>Was it delivered?</td><td>The signed run sheet and nursing notes</td><td>The nurse and the dialysis staff</td><td>The schedule, an attendance list, a text message</td></tr>
<tr><td>Was it safe?</td><td>The dialyzer reprocessing log, the water-quality log, the machine maintenance record</td><td>Technicians</td><td>&ldquo;We always do it&rdquo;</td></tr>
</tbody></table></div>
<p>The <strong>run sheet</strong> is the primary proof that care was delivered. It records the date and shift, the station and machine, the pre- and post-dialysis weights and blood pressures, the duration, events during the session, medicines given, the dialyzer and its reuse number, and the authenticating signatures. A schedule shows only that a session was planned. Patients miss sessions, arrive late, and stop early. Only the run sheet shows what happened.</p>
<p>The third layer lives outside the patient&rsquo;s folder, which is why it is so often forgotten. Technical staff own the technical logs. The records officer makes sure those logs are complete, dated, signed by the person who did the work, retrievable, and cross-referenced to sessions.</p>
<h3>The dialyzer log is an identity record</h3>
<p>PhilHealth&rsquo;s minimum standard allows up to 32 dialyzers per patient per calendar year, each reusable up to five times.[[mro_ph2024ts]] Every reuse must link to the right patient and show the reprocessing date, the germicide used and its contact time, the residual-germicide test, and a performance test such as fiber bundle volume.</p>
<p>Now picture what happens if the link breaks. A reprocessed dialyzer carries traces of one person&rsquo;s blood. Used on a different patient, it is a bloodborne-infection event, with hepatitis B, hepatitis C, and HIV among the risks. The reprocessing log is the only record that ties each dialyzer to exactly one person. That is why the records officer treats it as an <strong>identity</strong> record as much as a technical one.</p>
{{key:Order proves authorized. Run sheet proves delivered. Technical logs prove safe. A chart that holds only the first two cannot prove the third.}}
{{scene:The dialyzer with two owners|<p>During a weekly check, a technician notices that dialyzer D-117-03 appears in the reprocessing log under two patients with similar surnames, Mr. Dante Cruz and Mr. Danilo Cruz, on consecutive days.</p>
<p>He stops reprocessing it and tells the technical supervisor, who traces both run sheets. One entry was a transcription error: the dialyzer had always been Mr. Dante Cruz&rsquo;s. The supervisor corrects the log through the technical correction process and asks the nephrologist to review whether any clinical action is needed. The records officer adds both patients&rsquo; full middle names to the reprocessing labels.</p>
<p class="tc-scene-take">The reprocessing log is an identity record. A name error there is a safety event, not a typo.</p>}}
"""),
        ("trace", "Tracing a session", "Following one session through every record", """
<p>The best way to learn the three layers is to trace a single session from start to finish. Pick any session from last week and follow it.</p>
{{flow:Tracing one session|Schedule::Was the patient booked for this date and shift?|Standing order::Was a current, signed order in force on that date?|Run sheet::Is it signed, complete, and filed to the right patient and session?|Dialyzer log::Does the dialyzer number and reuse count on the run sheet match a reprocessing entry for this patient, dated before the session?|Water log::Was water quality tested and recorded for that day, as the technical procedure requires?|Machine record::Was the machine at that station in service and maintained?|Claim::If the session was claimed, does the claim match the run sheet?}}
<p>Most traces end cleanly. The ones that do not teach you where your unit&rsquo;s weak points are. A common pattern is a run sheet that lists a dialyzer number with no matching reprocessing entry, because the technician logged it at the end of a busy shift and forgot. Another is a machine number on the run sheet that does not exist in the maintenance record, because a machine was swapped mid-week and no one updated the station board.</p>
<p>Tracing is not an accusation. You are checking that the records agree, not that anyone did something wrong. When they disagree, the clinical or technical owner explains, and the explanation goes into the record.</p>
{{scene:A trace that found a machine|<p>Tracing one random session from last Wednesday, the records officer finds that the run sheet lists machine M-09 at station 9. The maintenance record shows M-09 was sent out for repair on Monday.</p>
<p>The charge nurse explains: M-12 was moved to station 9 on Monday, but the station board still said M-09. The run sheets for that week are corrected by their authors, the board is fixed, and the technical supervisor adds &ldquo;update the station board&rdquo; to the machine-swap checklist.</p>
<p class="tc-scene-take">The trace did not find a wrong treatment. It found a habit that would eventually have hidden one.</p>}}
{{fig:mro02_fig_02_one_session_trace}}
"""),
        ("deficiency", "Deficiencies", "Four states, one owner each", """
<p>When you audit a chart, mark every expected item as one of four states.</p>
<div class="table-wrap"><table>
<thead><tr><th>State</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Present</td><td>Exists, current, complete, authenticated</td><td>A signed standing order within the quarter</td></tr>
<tr><td>Deficient</td><td>Exists but is unsigned, illegible, outdated, or incomplete</td><td>A run sheet with a blank final weight</td></tr>
<tr><td>Unavailable</td><td>Should exist but cannot be found</td><td>A reprocessing entry for a reuse logged on the run sheet</td></tr>
<tr><td>Not applicable</td><td>Excluded under a written applicability rule</td><td>A transplant work-up section for a patient whose physician has documented that work-up is not being pursued</td></tr>
</tbody></table></div>
<p>&ldquo;Not applicable&rdquo; needs a written rule behind it. Without one, it becomes a convenient label for anything that is hard to find, and the audit stops measuring anything.</p>
<p>Each deficiency gets three things: an owner, a due date, and closure evidence. The owner is the person who can fix it, which is almost never you. The due date depends on risk. The closure evidence is what you will look at to confirm it was fixed: the signed late entry, the found document, the new order.</p>
<h3>The deficiencies that cannot wait</h3>
<p>Most deficiencies can wait for the weekly round. A few cannot, because they could change what happens to the patient at the next session.</p>
<div class="table-wrap"><table>
<thead><tr><th>Deficiency</th><th>Why it cannot wait</th></tr></thead>
<tbody>
<tr><td>Standing order expired</td><td>The nurse has no current prescription to follow</td></tr>
<tr><td>A dose change written on a progress note but no signed order</td><td>Two versions of the prescription now exist</td></tr>
<tr><td>A dialyzer that cannot be traced to its patient</td><td>It may be used on the wrong person</td></tr>
<tr><td>A new positive hepatitis result not reflected in the station assignment record</td><td>Isolation may be wrong today</td></tr>
<tr><td>A document filed to the wrong patient</td><td>Someone may act on it</td></tr>
</tbody></table></div>
{{call:Anything that could affect the next treatment goes to the charge nurse and the clinical team before that session, not to the weekly deficiency round. Never fill a clinical field yourself, even when the value seems obvious from another document. When in doubt about clinical risk, ask the attending nephrologist and follow your unit&rsquo;s protocol.}}
{{scene:Not applicable, or not found?|<p>An audit sheet comes back from a relief clerk with 14 items marked &ldquo;N/A&rdquo; across ten charts, including three advance-directive sections.</p>
<p>The records officer checks the written applicability rule. Advance-directive status is required for every patient: either a directive or a documented statement that none exists. The three charts had neither. She reclassifies them as deficient, assigns them to the attending physician, and adds one line to the audit instructions: &ldquo;N/A only where the written rule says so.&rdquo;</p>
<p class="tc-scene-take">&ldquo;Not applicable&rdquo; without a rule behind it hides the very gaps an audit is meant to find.</p>}}
"""),
        ("habits", "Floor habits", "Usual office habits that change here", """
<p>Many records habits come from hospital wards or general clinics. Some of them do not fit a dialysis unit.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual habit</th><th>In a dialysis unit</th><th>Why</th></tr></thead>
<tbody>
<tr><td>&ldquo;File the chart when the patient is discharged&rdquo;</td><td>The patient is never discharged; file every session</td><td>The chart grows three times a week for years</td></tr>
<tr><td>&ldquo;The schedule shows who came&rdquo;</td><td>Only the run sheet shows who was treated</td><td>Patients skip, arrive late, and stop early</td></tr>
<tr><td>&ldquo;Technical logs are not medical records&rdquo;</td><td>They are evidence of safe care and must be retrievable</td><td>Reprocessing ties a dialyzer to one person</td></tr>
<tr><td>&ldquo;Audit once a year&rdquo;</td><td>Audit weekly, in small samples</td><td>Gaps compound with every session</td></tr>
<tr><td>&ldquo;Fill obvious blanks to save time&rdquo;</td><td>Never; route to the author</td><td>A blank honestly recorded is better than a value invented later</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Which items are deficient, and who owns them?</strong> Two. The blank final weight belongs to Ms. Pangilinan, who signed the run sheet. She reviews whatever contemporaneous evidence exists, such as the machine display log or her own notes, and makes an attributed late entry if appropriate, with both the service date and the date she wrote it. The missing reprocessing entry for reuse 5 belongs to the reprocessing technician and the technical supervisor. Both go on the deficiency log with today&rsquo;s date.</p>
<p><strong>Why is the missing entry more than paperwork?</strong> Without it, no one can show that the dialyzer used on November 18 was cleaned, tested, and belonged to Mr. Galang. That is a possible identity and infection risk. Tell the technical supervisor today, not on Monday. Do not create the entry yourself, even if the technician says, &ldquo;I definitely did it.&rdquo; The technician writes it, as a late entry, if they can support it.</p>
<p><strong>The allowance.</strong> 32 minus 26 leaves 6 dialyzers for the rest of the year. Whether D-044-07 can be used again on Monday is a technical and clinical decision, not a records one. Make sure the supervisor and the charge nurse know about the gap before 6 a.m. Monday.</p>
<p>The blank weight is the gap most people would notice first. The missing logbook line in another room is the one that could hurt someone. Part of your role is to look in the other room.</p>
"""],
    "skills": {"title": "Chart and technical-log audit",
               "intro": "Audit three fictional charts and trace one session to its technical records while your preceptor observes.",
               "items": [
                   ("Lists the contents of a longitudinal chart and the renewal interval of standing orders and consents.", False),
                   ("Marks each expected item present, deficient, unavailable, or not applicable under a written rule.", False),
                   ("Routes every clinical deficiency to its author without filling any clinical field.", True),
                   ("Escalates a deficiency that could affect the next treatment before that session.", True),
                   ("Traces a session from the run sheet to its dialyzer reprocessing entry, water log, and machine record.", False),
                   ("Treats an untraceable dialyzer as an identity risk and escalates it the same day.", True),
                   ("Computes the remaining dialyzer allowance for the year.", False),
                   ("Retrieves the current standing order and its superseded version.", False),
               ],
               "placement": "Pick one session from last week and trace it from run sheet to dialyzer, water, and machine records. Write down every place the records disagreed."},
    "terms": [("Run sheet", "The per-treatment flow sheet."), ("Standing order", "The current dialysis prescription."),
              ("Reprocessing", "Cleaning, testing, and disinfecting a dialyzer for reuse by the same patient."),
              ("Deficiency", "A required item that is unsigned, illegible, outdated, incomplete, or missing."),
              ("Longitudinal chart", "The record kept for as long as the patient dialyzes with the unit."),
              ("PDD", "PhilHealth Dialysis Database.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["02"])
