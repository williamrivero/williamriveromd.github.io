# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 10: Retention, Legal Holds, and Disposition. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer checking a retention schedule beside shelves of archived dialysis charts.",
    "objectives": [
        "State the Philippine default retention periods for outpatient and inpatient health records and their source.",
        "Identify the trigger event that starts the retention clock for a hemodialysis chart.",
        "Compute the date a chart becomes eligible for disposition review.",
        "Apply a legal hold to every copy of an affected record, including backups.",
        "Destroy only eligible, unheld, approved records, and keep a signed disposition record.",
    ],
    "big": """
{{plain:Records are like medicines in a pharmacy. Throw them out too early and someone who needs them will find the shelf empty. Keep them forever and the shelves overflow, the old stock gets mixed with the new, and some of it becomes dangerous. Every record needs an expiry date, and every expiry date needs a reason.}}
<p>The picture is useful, and it has one limit. An expired medicine is simply discarded. An expired record may still be needed if someone has started a lawsuit, a payer has opened an audit, or a patient has filed a privacy complaint. Expiry is the default, and holds override it.</p>
<p>Records kept too briefly can leave a patient, a physician, or the unit unable to prove what happened. Records kept forever pile up risk: every extra year is another year in which a box can flood, a storeroom can be broken into, or a server can be breached. The Data Privacy Act expects personal data to be kept only as long as their purpose and the law require.[[mro_npc_ao2020]] A retention schedule is the facility&rsquo;s answer to both problems, and the records officer keeps it.</p>
{{cards:Key terms for this module|Records disposition schedule::The approved table of how long each class of record is kept, and what happens to it afterward.|Trigger event::The event that starts the retention clock.|Eligibility date::The date a record becomes eligible for disposition review: trigger date plus retention period.|Legal hold::An instruction to preserve records regardless of the schedule.|National Archives of the Philippines (NAP)::The agency that approves records schedules and disposal for public entities.|Disposition record::The signed record of what was destroyed, how, by whom, and when.}}
""",
    "case": {"title": "The batch due next month", "html": """
<p>The storeroom at your freestanding unit is full. Mr. Nestor Villareal, the unit manager, asks you to &ldquo;clear out the old charts&rdquo; before new shelving arrives in December. Your archive list flags three closed charts.</p>
<ul>
<li>Mr. Lorenzo Pascual last dialyzed with you on June 30, 2019, then transferred to a unit in Batangas. His chart is under an active legal hold, recorded in the verified hold register, over a claim dispute with PhilHealth.</li>
<li>Mrs. Florencia Dimaculangan last dialyzed with you on June 30, 2019. She died in July 2019. No hold appears in the verified register.</li>
<li>Mr. Ricardo Soriano&rsquo;s chart was opened in 2015. He still dialyzes with you on Tuesday, Thursday, and Saturday.</li>
</ul>
<p>Your unit has no local schedule longer than the national default.</p>
""", "questions": ["When does each chart become eligible for disposition review?",
                  "What happens to Mr. Pascual&rsquo;s chart, and to its copies?",
                  "What has to happen before Mrs. Dimaculangan&rsquo;s chart is destroyed?"]},
    "sections": [
        ("default", "The default", "The Philippine default", """
<p>Department of Health (DOH) Department Circular (DC) 2021-0226, dated May 31, 2021, disseminated the revised Approved Records Disposition Schedule for health facilities. According to the DOH&rsquo;s own published answer, <strong>inpatient health records are kept for 10 years in total before disposal, and outpatient health records for 7 years after the last consultation</strong>. Other facility record classes are listed in its annexes.[[mro_doh2021rds]]</p>
<p>Maintenance hemodialysis is outpatient care. For a freestanding unit, the default trigger is the patient&rsquo;s <strong>last treatment encounter</strong> with the unit, after death, transfer, transplant, or recovery. It is not the date the chart was opened. A patient who has dialyzed with you for eleven years has a chart that is eleven years old and still has no trigger at all.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Trigger</th></tr></thead>
<tbody>
<tr><td>Patient still dialyzes with you</td><td>None yet; keep</td></tr>
<tr><td>Patient transferred out</td><td>The last session at your unit</td></tr>
<tr><td>Patient received a transplant</td><td>The last session at your unit</td></tr>
<tr><td>Patient recovered and stopped dialysis</td><td>The last session at your unit</td></tr>
<tr><td>Patient died</td><td>The last session at your unit</td></tr>
</tbody></table></div>
<h3>When two schedules apply</h3>
<p>A hospital-based unit may follow a hospital schedule approved by the National Archives of the Philippines (NAP) that sets longer periods. Public entities need NAP disposal authority before destroying anything.[[mro_ra9470]] If any applicable schedule is longer, the longer one governs.</p>
<p>You may read about other countries&rsquo; rules. The United States federal dialysis rule, for example, keeps records six years from discharge.[[dch_cfr494]] That is a comparison only. It is not a Philippine rule, and it cannot shorten a Philippine one.</p>
{{formula:<strong>Eligibility date</strong> = trigger date + retention period.<br>Last treatment June 30, 2019 + 7 years = disposition review from June 30, 2026.}}
<p>The toolkit&rsquo;s retention calculator does this arithmetic, including the longer-schedule and hold checks.</p>
"""),
        ("holds", "Holds", "Holds override schedules", """
{{fig:mro10_clock}}
<p>Eligibility is not permission. Before any chart is destroyed, check for holds.</p>
<p>Each of these triggers a hold:</p>
<ul>
<li>litigation, actual or reasonably anticipated;</li>
<li>a government investigation;</li>
<li>a PhilHealth audit or claim dispute;</li>
<li>a complaint to the National Privacy Commission (NPC);</li>
<li>a records request still in progress.</li>
</ul>
<p>When a hold arrives, confirm its scope in writing with counsel or the facility head: which patients, which record types, which dates. Then suspend disposition of every affected copy. That includes the paper chart, the scanned images, the electronic record, claims attachments, registry extracts, emailed copies, and backups. IT must be told about backups, because a backup tape rotated on schedule can destroy the one copy a court needs.</p>
<p>Record the acknowledgment of the hold. Review open holds periodically. Release a hold only in writing. When a hold ends, recheck the schedule, any other holds, and approvals before anything proceeds. The end of one hold does not make a chart eligible if another hold or a longer schedule still applies.</p>
{{call:Never destroy a record because the box is full. Eligibility comes from the schedule, permission comes from the approver, and holds come first. If a manager asks you to clear a shelf, the answer is a list of what is eligible, not a shredder.}}
"""),
        ("destroy", "Destruction", "Lawful, documented destruction", """
<p>Destroy only records that are eligible, unheld, and approved in writing. Use a secure method: cross-cut shredding or pulping for paper; certified wiping or physical destruction for electronic media. Throwing charts into the regular trash, selling them as scrap paper, or burning them in the back lot are all breaches waiting to happen. Paper sold as scrap does not stay private; it can turn up as packaging anywhere.</p>
<p>Keep a signed disposition record: what was destroyed, how many, the method, who witnessed it, and the date. Keep the disposition record itself under its own schedule. It is the proof that the destruction was lawful, and a unit that cannot show it may be unable to prove the records were not simply lost.</p>
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
{{key:Every copy counts. A chart shredded on paper but still sitting in a scanned folder, a claims attachment, and last year&rsquo;s backup has not been disposed of; it has been partly destroyed.}}
"""),
    ],
    "debrief": ["""
<p><strong>Eligibility.</strong> Mr. Pascual and Mrs. Dimaculangan: trigger June 30, 2019, eligible for review from June 30, 2026. Mr. Soriano: no trigger yet, however old his chart is. He is still a patient.</p>
<p><strong>Mr. Pascual.</strong> Eligible but held. His chart stays, together with its scans, claim attachments, electronic record, and backups, until counsel releases the hold in writing. Make sure IT knows. Then the hold is rechecked before anything happens.</p>
<p><strong>Mrs. Dimaculangan.</strong> Route the chart for disposition review and written approval by the facility head. After approval, destroy every copy by a secure method with a witness, and complete a signed disposition record.</p>
<p><strong>And Mr. Villareal&rsquo;s request?</strong> Give him the list: one chart eligible and approved for review, one held, one active. Clearing a shelf is a reasonable goal. Doing it by schedule, not by box, is what keeps the unit out of trouble.</p>
<p>Part of your role is to make sure the oldest box on the shelf is not the one that a court asks for next month.</p>
"""],
    "skills": {"title": "Retention schedule, hold, and disposition",
               "intro": "Compute eligibility and process a hold and a disposition request for fictional charts while your preceptor observes.",
               "items": [
                   ("States the outpatient and inpatient default periods and their source.", False),
                   ("Uses the correct trigger: last treatment encounter for an outpatient chart.", False),
                   ("Computes the eligibility date and applies the longer schedule when two apply.", False),
                   ("Suspends disposition of every copy under a hold, including backups.", True),
                   ("Responds to a request to clear shelves with an eligibility list, not destruction.", True),
                   ("Destroys nothing without written approval and keeps a signed disposition record.", True),
               ],
               "placement": "Find your unit&rsquo;s retention schedule. Check that it cites DC 2021-0226 and names a trigger for each class."},
    "terms": [("Records disposition schedule", "The approved table of retention periods."),
              ("Trigger event", "The event that starts the retention clock."), ("Eligibility date", "Trigger date plus retention period."),
              ("Legal hold", "An instruction to preserve records regardless of schedule."),
              ("NAP", "National Archives of the Philippines."), ("DC", "Department Circular."),
              ("Disposition record", "The signed record of what was destroyed, how, by whom, and when.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
