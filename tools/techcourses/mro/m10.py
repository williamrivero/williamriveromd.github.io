# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 10: Retention, Holds, and Lawful Disposition. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer labeling archive boxes on metal shelving in a clean, well-lit records storage room.",
    "objectives": [
        "Classify a record under the approved disposition schedule.",
        "Compute its eligibility date from the correct trigger event.",
        "Stop disposal when a hold applies, for every copy.",
        "Carry out and document authorized destruction.",
    ],
    "big": """
{{plain:Records kept too briefly can leave a patient, a physician, or the unit unable to prove what happened. Records kept forever pile up risk: every extra year is another year in which a box can flood or a server can be breached.}}
<p>The Data Privacy Act expects personal data to be kept only as long as their purpose and the law require.[[mro_npc_ao2020]] A retention schedule is the facility&rsquo;s answer to both problems, and the records officer keeps it.</p>
{{cards:Key terms for this module|Records disposition schedule::The approved table of how long each record class is kept.|Trigger event::The event that starts the retention clock.|Legal hold::An instruction to preserve records regardless of schedule.|National Archives of the Philippines (NAP)::National Archives of the Philippines.|Department circular (DC)::Department Circular.}}
""",
    "case": {"title": "The batch due next month", "html": """
<p>Your freestanding unit&rsquo;s archive list flags three closed charts. Fictional patient SIM-061 last dialyzed with you on June 30, 2019 before transferring out and is under an active legal hold over a claim dispute. SIM-062 last dialyzed on June 30, 2019 and died; no hold appears in the verified register. SIM-063 still dialyzes. The unit has no longer local schedule.</p>
""", "questions": ["When does each chart become eligible for disposition review?",
                  "What happens to SIM-061?",
                  "What has to happen before SIM-062 is destroyed?"]},
    "sections": [
        ("default", "The default", "The Philippine default", """
<p>DOH Department Circular (DC) 2021-0226, dated May 31, 2021, disseminated the revised Approved Records Disposition Schedule for health facilities. Per the DOH&rsquo;s own published answer, <strong>inpatient health records are kept for 10 years in total before disposal, and outpatient health records for 7 years after the last consultation</strong>; other facility record classes are listed in its annexes.[[mro_doh2021rds]]</p>
<p>Maintenance hemodialysis is outpatient care. For a freestanding unit, the default trigger is the patient&rsquo;s <strong>last treatment encounter</strong> with the unit &mdash; after death, transfer, transplant, or recovery &mdash; not the date the chart was opened.</p>
<p>A hospital&rsquo;s schedule approved by the National Archives of the Philippines (NAP) may set longer periods, and public entities need NAP disposal authority before destroying anything.[[mro_ra9470]] If any applicable schedule is longer, the longer one governs. The United States federal dialysis rule of six years from discharge is a comparison only, not a Philippine rule.[[dch_cfr494]]</p>
{{formula:Eligibility date = trigger date + retention period. Last treatment June 30, 2019 + 7 years = disposition review from June 30, 2026.}}
"""),
        ("holds", "Holds", "Holds override schedules", """
{{fig:mro10_clock}}
<p>Litigation, actual or reasonably anticipated; a government investigation; a PhilHealth audit or claim dispute; an NPC complaint; a records request in progress &mdash; each triggers a hold. Confirm the scope with counsel or the facility head, suspend disposition of every affected copy, including exports and backups through IT, record the acknowledgment, review the hold periodically, and release it only in writing. When a hold ends, recheck retention, other holds, and approvals before anything proceeds.</p>
{{call:Never destroy a record because the box is full. Eligibility comes from the schedule, permission comes from the approver, and holds come first.}}
"""),
        ("destroy", "Destruction", "Lawful, documented destruction", """
<p>Destroy only records that are eligible, unheld, and approved in writing. Use a secure method &mdash; cross-cut shredding or pulping for paper; certified wiping or physical destruction for media &mdash; and keep a signed disposition record: what, how many, the method, who witnessed, and the date. Keep the disposition record itself under its own schedule; it is the proof the destruction was lawful.</p>
<div class="table-wrap"><table>
<thead><tr><th>Schedule column</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Record class</td><td>Outpatient hemodialysis chart</td></tr>
<tr><td>Authority and version</td><td>DOH DC 2021-0226</td></tr>
<tr><td>Systems covered</td><td>Paper, electronic record, scans, downtime copies, claims attachments, backups</td></tr>
<tr><td>Trigger</td><td>Last treatment encounter</td></tr>
<tr><td>Period</td><td>7 years</td></tr>
<tr><td>Owner and method</td><td>Records officer; cross-cut shredding with witness</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Eligibility.</strong> SIM-061 and SIM-062: trigger June 30, 2019, eligible for review from June 30, 2026. SIM-063: no trigger yet.</p>
<p><strong>SIM-061.</strong> Stays under hold, including its claim attachments, scans, and backups, until counsel releases the hold in writing.</p>
<p><strong>SIM-062.</strong> Route for disposition review and written approval, then secure destruction with a signed, witnessed disposition record.</p>
"""],
    "skills": {"title": "Retention schedule, hold, and disposition",
               "intro": "Compute eligibility and process a hold and a disposition request for fictional charts with a preceptor.",
               "items": [
                   ("Uses the correct trigger: last treatment encounter for an outpatient chart.", False),
                   ("Applies the longer schedule when two apply.", False),
                   ("Suspends disposition of every copy under a hold.", True),
                   ("Destroys nothing without written approval and keeps a signed disposition record.", True),
               ],
               "placement": "Find your unit&rsquo;s retention schedule. Check that it cites DC 2021-0226 and names a trigger for each class."},
    "terms": [("Records disposition schedule", "The approved table of retention periods."),
              ("Trigger event", "The event that starts the retention clock."), ("Legal hold", "An instruction to preserve records regardless of schedule."),
              ("NAP", "National Archives of the Philippines."), ("DC", "Department Circular.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
