# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 04: Session Evidence, Utilization, and the Yearly Count."""

MODULE = {
    "image_alt": "A clipboard with a signed dialysis treatment sheet beside sealed red and blue bloodlines, with a weekly planner out of focus.",
    "objectives": [
        "Explain why a completed, attested treatment record, not a schedule, proves that a session happened.",
        "Build one ledger row per encounter with its source, status, utilization number, and disposition.",
        "Count emergency hemodialysis in chronic kidney disease stage 5 toward the 156, with the codes the circular specifies.",
        "Route shortened, unattested, duplicate, over-cap, and year-boundary entries to their owners.",
        "Project when a patient will reach the allocation and start the funding conversation early.",
    ],
    "big": """
{{plain:A schedule is a promise; a signed treatment record is a receipt. The schedule says a patient was expected at 6 AM on Monday. Only the nurse&rsquo;s record says the patient came, was connected, and finished.}}
<p>The picture has a limit. A receipt shows a purchase was complete; a dialysis session can be partly done. Sessions are sometimes stopped early because of low blood pressure, cramps, a clotted circuit, or an access problem. A treatment shortened by ten minutes or more is associated with worse outcomes in a large US network, which is one reason the nurse records exactly what was delivered.[[pc_obialo2012]] Claims staff never infer what was rendered from a machine log or a booking. They ask nursing.</p>
{{fig:pc_happen}}
{{cards:Key terms for this module|Attested::Signed by the nurse or clinician who delivered the treatment.|Encounter::One patient, one date, one service.|Ledger::One row per encounter, linked to its source record.|Utilization number::Where this session falls in the patient&rsquo;s 156 for the year.|Over cap::A session beyond the year&rsquo;s allocation.|Year boundary::Sessions near January 1, which start a new count.}}
""",
    "case": {"title": "Four rows near the cap", "html": """
<p>Ms. Lorna Castillo (fictional, SIM-04) has 154 sessions verified by PhilHealth for this calendar year. Your ledger for the last two weeks shows four more rows: an emergency hemodialysis session during a hospital stay for chronic kidney disease stage 5, dated and documented by the hospital; a cancelled session because of a typhoon; a completed and signed conventional session at your unit; and one more completed and signed session four days later.</p>
<p>The clerk also finds a 40-minute machine run on a fifth date with no nursing note at all.</p>
""", "questions": ["What utilization number does each row get?",
                  "What do you do with the 40-minute machine run?",
                  "What has to happen for the last completed session, and when should that conversation have started?"]},
    "sections": [
        ("ledger", "The ledger", "One row per encounter", """
<p>Start from completed, attested treatment records. A booking, a transport log, or a machine slot can help you <em>find</em> a record, but only nursing or clinical evidence establishes that treatment occurred. Build one ledger row per encounter, and compare each row against Claim Form 2 (CF2) Part III, the clinical record, the agreement form, and billing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Example (fictional)</th></tr></thead>
<tbody>
<tr><td>Case token and date</td><td>SIM-04 &middot; November 12</td></tr>
<tr><td>Site</td><td>This unit / hospital / other unit</td></tr>
<tr><td>Status</td><td>Completed and attested / scheduled only / cancelled / emergency / shortened</td></tr>
<tr><td>Source reference</td><td>Treatment sheet number or hospital record</td></tr>
<tr><td>Utilization number</td><td>#155 of 156</td></tr>
<tr><td>Agreement form</td><td>Signed / unsigned</td></tr>
<tr><td>Disposition</td><td>Ready for review / hold (owner) / no consumption / over cap</td></tr>
</tbody></table></div>
<p>Before any row goes forward, search active and archived batches for the same patient, date, and service. Two rows on one date may be a duplicate, or two distinct services; the source records decide which. Calculator 2 in the claims toolkit flags same-date rows automatically.</p>
"""),
        ("emergency", "Emergency sessions", "Emergency hemodialysis and the count", """
<p>A patient with chronic kidney disease stage 5 who needs emergency hemodialysis, for example during a hospital stay, uses a session from the same allocation. For documented emergency hemodialysis in stage 5 disease, Circular 2024-0023 calls for the RVS procedure code 90935 with the diagnosis code N18.5 on CF2, and the session counts toward the 156.[[pc_pc2024_0023]] The facility that rendered the session files it; if that was a hospital, your unit records it as consumed and keeps the hospital&rsquo;s claim reference.</p>
<p>Acute kidney injury is different. Dialysis for a sudden, possibly reversible injury goes through the hospital&rsquo;s own claim and coding review (Module 10), not the maintenance package. For eligible hospital confinement, transfusion, or catheter services in a stage 5 patient, check the separate filing rules in the circular and in each applicable package.</p>
{{key:The diagnosis on the record decides the pathway. Claims staff check that the codes match the documentation; they never choose the diagnosis.}}
"""),
        ("count", "The yearly count", "Counting toward the allocation", """
<p>Counted sessions run in date order from the PhilHealth-confirmed prior total. Cancelled and scheduled-only entries consume nothing. Unattested and shortened sessions are <em>projected</em> to count but stay on hold until their owners resolve them. Any counted session beyond 156 is over the cap: it needs a funding plan, and the patient&rsquo;s treatment continues.</p>
{{fig:pc_calendar}}
{{formula:<strong>Projecting the last covered session.</strong> With R sessions remaining and three sessions a week, the allocation runs out on the date of the R-th future scheduled session. Example: 6 remaining, Monday-Wednesday-Friday from Monday, November 2 = sessions on November 2, 4, 6, 9, 11, and 13; the last covered session is Friday, November 13. Calculator 2 does this for any schedule.}}
<p>Sessions on December 31 count against the current year; a session on January 2 is #1 of the new year. For a transfer that straddles the year, confirm the reset with your PRO in writing. Patients who needed extra sessions after a hospital stay, or who dialyzed elsewhere while traveling, are the ones who run short before December.</p>
"""),
        ("funding", "Over the cap", "Planning funding before the last session", """
<p>When a patient will exhaust the allocation before year-end, the conversation belongs in October or November, not on the day of the first uncovered session. The liaison explains what is confirmed and what is pending, links the family with the facility&rsquo;s social service and funding options, and agrees a callback date. Funding questions are never a reason to skip or shorten a session.</p>
{{call:A patient beyond the allocation is still dialyzed as prescribed. Route funding to billing and social service; never tell a patient a session is cancelled because it is not covered.}}
"""),
    ],
    "debrief": ["""
<p><strong>The numbers.</strong> The emergency session in stage 5 disease is #155, filed by the hospital with 90935 and N18.5; your unit records it as consumed and keeps the hospital&rsquo;s claim reference. The cancellation consumes nothing. The first completed session at your unit is #156. The next completed session is beyond the allocation: over cap, with funding follow-up. Check the emergency entry&rsquo;s codes and source before you rely on it.</p>
<p><strong>The 40-minute run.</strong> Hold it. A machine log is not proof of treatment. Ask nursing what was rendered, and verify claimability against the applicable guidance.</p>
<p><strong>The funding conversation.</strong> It should have started weeks earlier, when the projection showed the allocation running out. Start it now with the family, billing, and social service. Treatment continues.</p>
"""],
    "skills": {"title": "Session ledger and utilization",
               "intro": "From a fictional month of records for three patients, build the ledger, number every counted session, and route every exception.",
               "items": [
                   ("Uses only attested treatment records to establish that a session occurred.", True),
                   ("Builds one row per encounter with source, status, utilization number, and disposition.", False),
                   ("Counts documented emergency HD in stage 5 disease and checks its paired codes.", False),
                   ("Excludes cancelled and scheduled-only entries from the count.", False),
                   ("Holds shortened and unattested sessions and asks nursing what was rendered.", True),
                   ("Screens for duplicates across active and archived batches.", True),
                   ("Projects the allocation date and starts the funding conversation early.", False),
               ],
               "placement": "Reconcile one patient&rsquo;s calendar year of sessions at your unit against the PhilHealth-confirmed count."},
    "quiz": [
        ("Does an emergency HD session in a stage 5 patient consume a session?",
         ["No", "Yes; count it and check the paired codes in the circular", "Only if done at your unit", "Only half"], 1,
         "90935 with N18.5, and it counts toward the 156."),
        ("What do you do with a schedule entry that has no attested record?",
         ["Claim it", "Hold claim inclusion pending verification that care was rendered and documented", "Delete it", "Count it as half"], 1,
         "A schedule is a promise, not a receipt."),
        ("A 40-minute machine run has no nursing note. What is your step?",
         ["Claim it", "Hold and ask nursing what was rendered", "Count it as cancelled", "Ignore it"], 1,
         "Claimability follows the record."),
        ("A patient is at #156 on November 15. What should the liaison do now?",
         ["Wait for December", "Plan early: funding handoff, social service, and a clear explanation, with no interruption of treatment", "Cancel future sessions", "Ask PhilHealth for 20 more"], 1,
         "Treatment continues."),
        ("Two rows show the same patient, same date, at different branches. Next step?",
         ["Release both", "Investigate duplicate versus distinct service from source records before releasing either", "Delete one", "Release the larger one"], 1,
         "Source records decide."),
        ("Which code pair does the circular give for documented emergency HD in stage 5 disease?",
         ["N17.9 and 90935", "90935 and N18.5", "N18.6 and 90937", "Z49.1 and 90935"], 1,
         "RVS 90935 is the procedure; N18.5 is the diagnosis."),
        ("Does a cancelled session consume utilization?",
         ["Yes", "No", "Only if cancelled by the patient", "Only on Mondays"], 1,
         "Only rendered sessions count."),
        ("Who files the claim for an emergency session delivered at a hospital?",
         ["Your unit", "The hospital that rendered it", "The patient", "PhilHealth"], 1,
         "Your unit records it as consumed."),
        ("A session on January 2 is which number for the year?",
         ["#157", "#1 of the new year", "Not counted", "#156"], 1,
         "The allocation resets each calendar year."),
        ("Dialysis for acute kidney injury goes through:",
         ["The maintenance HD package", "The hospital&rsquo;s own claim and coding review", "The PD package", "No claim"], 1,
         "AKI is a different pathway."),
        ("What is associated with worse outcomes in a large US dialysis network?",
         ["Arriving early", "Missed and shortened treatments", "Weekend sessions only", "Using a schedule"], 1,
         "Obialo and colleagues, 2012; observational."),
        ("Six sessions remain, Monday-Wednesday-Friday from Monday, November 2. When is the last covered session?",
         ["November 11", "November 13", "November 9", "November 16"], 1,
         "November 2, 4, 6, 9, 11, 13."),
        ("Which document can locate a record but not prove treatment?",
         ["The nursing treatment sheet", "A booking or transport log", "The attested clinical record", "The physician&rsquo;s signed note"], 1,
         "Use it to find the record, not to replace it."),
        ("Why are patients who needed extra sessions after a hospital stay at risk?",
         ["They lose PDD registration", "Extra sessions come out of the same 156 and they run short before December", "They pay double", "They need a new PIN"], 1,
         "Project early."),
        ("What is the disposition of a completed session beyond the allocation?",
         ["Cancel it", "Over cap with funding follow-up; the patient is still dialyzed", "Claim it anyway", "Move it to next year"], 1,
         "Coverage never decides treatment."),
    ],
    "terms": [("Attested", "Signed by the person who delivered the treatment."),
              ("Encounter", "One patient, one date, one service."),
              ("Ledger", "One row per encounter, linked to its source record."),
              ("Utilization number", "Where a session falls in the year&rsquo;s 156."),
              ("Over cap", "A session beyond the year&rsquo;s allocation."),
              ("RVS", "Relative Value Scale, PhilHealth&rsquo;s procedure codes.")],
    "readings": [("hemodialysis-transfer-guide.html", "What patients and families need when they transfer to another dialysis unit.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
