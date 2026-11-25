# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 19: Registries, Privacy, and Quality. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator and a quality officer reviewing a run chart on a monitor in a quiet office.",
    "objectives": [
        "Explain the purpose, owner, and authorized users of each registry and report a transplant program feeds.",
        "Protect the restricted donor record and apply Data Privacy Act principles to everyday coordination.",
        "Define a quality measure with numerator, denominator, time window, and exclusions before counting.",
        "Report a rate with its uncertainty and compare it across groups for equity.",
    ],
    "big": """
{{plain:Data in a transplant program are like the instruments in a cockpit. The national registry, the PhilHealth registry, and the program&rsquo;s own logs each show something different. If the instruments are wrong, the pilot flies confidently in the wrong direction. If too many people can see and touch the instruments, someone eventually bumps a switch.}}
{{fig:rtc19_quality}}
<p>The picture has a limit. Cockpit instruments measure the plane. A transplant program&rsquo;s data describe people who trusted it with very private facts: a donor&rsquo;s reasons for stopping, a recipient&rsquo;s depression, a family&rsquo;s debts. So this module has two halves that support each other. Privacy keeps the data safe enough that people keep telling the truth. Good measurement makes the data accurate enough to improve the service.</p>
<p>The Data Privacy Act treats health information as sensitive personal information, with stricter rules for collecting, sharing, and keeping it.[[rtc_ra10173]] Registries have their own legal bases and owners: PhilHealth&rsquo;s KT Data Registry for pre-authorized patients,[[rtc_pa2026]] the national waiting list,[[rtc_doh2023wait]] and the DOH annual reporting of transplant facilities.[[rtc_doh2023annual]] Your job is to enter only what is needed, through authorized users, and to turn the program&rsquo;s own logs into honest measures.</p>
{{cards:Key terms for this module|Registry::A database kept for a defined purpose by a defined owner.|Authorized user::A person trained and designated to enter or view data in a system.|Restricted record::The part of a record open only to those who need it, such as a donor&rsquo;s private reasons.|Numerator and denominator::The count of events and the count of people who could have had them.|Confidence interval::A range that shows how uncertain a rate is.|Equity review::Comparing measures across groups to find unfair gaps.}}
""",
    "case": {"title": "The dashboard and the drawer", "html": """
<p>The program director asks you for a dashboard for the annual review. She wants &ldquo;donor follow-up rate,&rdquo; &ldquo;time from referral to first visit,&rdquo; and &ldquo;how many claims were denied.&rdquo;</p>
<p>While gathering data, you notice that the shared drive folder &ldquo;Transplant 2026&rdquo; holds scanned donor psychiatric reports, open to everyone in the department, including billing staff. In a desk drawer at the nurses&rsquo; station you find a printed list of wait-listed candidates with phone numbers and blood groups.</p>
<p>Your first count shows &ldquo;donor follow-up: 15 of 20 (75%)&rdquo; for one year, but you are not sure whether donors who moved abroad were included.</p>
""", "questions": ["What privacy problems do you see, and what do you do today?",
                  "How should &ldquo;donor follow-up rate&rdquo; be defined before you count?",
                  "How do you report 15 of 20 honestly, and what equity check would you add?"]},
    "sections": [
        ("registries", "Registries and their purposes", "Enter what is needed, through the right person", """
<div class="table-wrap"><table>
<thead><tr><th>System</th><th>Purpose</th><th>Who enters data</th></tr></thead>
<tbody>
<tr><td>PhilHealth KT Data Registry</td><td>A package requirement for all pre-authorized patients; electronic from May 1, 2026</td><td>Trained, designated facility users[[rtc_pa2026]]</td></tr>
<tr><td>National waiting list</td><td>Candidates for deceased-donor organs</td><td>Authorized program users[[rtc_doh2023wait]]</td></tr>
<tr><td>DOH annual facility reporting</td><td>Regulatory reporting of transplant activity</td><td>The facility&rsquo;s designated reporter[[rtc_doh2023annual]]</td></tr>
<tr><td>Program logs (referrals, register, claims, recalls)</td><td>Running and improving the service</td><td>Coordinators and program staff</td></tr>
</tbody></table></div>
<p>Each system has its own owner and its own definitions. Reconcile them on a schedule (Module 12), correct errors through each system&rsquo;s process, and never share login credentials: one person, one account, so the audit trail means something.</p>
{{key:Each registry has a purpose, an owner, and authorized users. Enter only what that purpose needs, under your own account.}}
"""),
        ("privacy", "Protect the restricted donor record", "Privacy in everyday coordination", """
<p>Most privacy failures are ordinary: a shared folder with the wrong permissions, a printed list left in a drawer, a group chat used for patient details, a family member told something the person did not authorize.</p>
<div class="table-wrap"><table>
<thead><tr><th>Principle</th><th>What it means for a coordinator</th></tr></thead>
<tbody>
<tr><td>Purpose</td><td>Collect and use information only for the reason it was given</td></tr>
<tr><td>Minimum necessary</td><td>Share only what the receiver needs; the billing office does not need psychiatric reports</td></tr>
<tr><td>Access control</td><td>The restricted donor record is open only to named roles; access is reviewed</td></tr>
<tr><td>Security</td><td>Approved systems only; no personal messaging apps for patient details; locked storage for paper</td></tr>
<tr><td>Incidents</td><td>Report a possible breach to the data protection officer at once and preserve evidence</td></tr>
</tbody></table></div>
{{call:If personal information has been exposed &mdash; a misdirected message, an open folder, a lost list &mdash; report it to the data protection officer within the hour of discovery, contain what you can (for example, ask IT to restrict the folder), and do not delete evidence. The controller decides on any notification.}}
{{key:Minimum necessary, named access, approved systems, and an immediate report when something leaks.}}
"""),
        ("measure", "Define before you count", "A measure is a definition first", """
<p>&ldquo;Donor follow-up rate&rdquo; sounds simple until you ask who counts. Write the definition before touching the data.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Example: donor follow-up at 1 year</th></tr></thead>
<tbody>
<tr><td>Numerator</td><td>Donors with a recorded blood pressure, kidney function, and urine albumin within 10 to 14 months after donation</td></tr>
<tr><td>Denominator</td><td>All donors who donated 10 to 14 months before the review date</td></tr>
<tr><td>Exclusions</td><td>Donors who died (reported separately); stated in advance</td></tr>
<tr><td>Special handling</td><td>Donors who moved abroad stay in the denominator; results from their own doctor count if received</td></tr>
<tr><td>Data source</td><td>The donor follow-up log, checked against clinic records</td></tr>
</tbody></table></div>
<p>Report every rate with its numerator and denominator, and with its uncertainty. Fifteen of 20 is 75%, and so is 45 of 60, but the first is much less certain; with 20 donors, the true rate could plausibly be anywhere from the low 50s to around 90 percent. A small program should be cautious about month-to-month changes and should prefer run charts over single numbers.</p>
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Days from referral receipt to first visit</td><td>Access and loop closure (Module 3)</td></tr>
<tr><td>Donor follow-up completeness at 1 year</td><td>The program&rsquo;s duty to donors (Module 17)</td></tr>
<tr><td>Pre-authorizations that expired before surgery</td><td>Coordination of clocks (Module 10)</td></tr>
<tr><td>Claims returned or denied, by reason</td><td>Evidence that follows care (Module 11)</td></tr>
<tr><td>Barrier register rows overdue</td><td>Follow-through (Module 1)</td></tr>
</tbody></table></div>
{{key:Define the numerator, denominator, window, and exclusions first. Report the count and the uncertainty with every rate.}}
"""),
        ("equity", "Compare across groups", "Fairness you can measure", """
<p>An overall average can look fair while one group falls behind. Once a year at least, split the main access measures by sex, age group, province or distance, income proxy (for example, PhilHealth membership category), and language. If people from far provinces take twice as long to reach a first visit, or women make up most of your donors but few of your recipients, that is a finding to act on (Module 3).</p>
<p>Then close the loop on your own improvement work: define, measure, compare, change one thing, and measure again with the same definition.</p>
{{scene:The province that waited longest|<p>A program&rsquo;s median time from referral to first visit is 21 days. Split by province, it is 14 days for Metro Manila referrals and 49 days for referrals from two northern provinces, where letters were carried by patients.</p>
<p>The program asks those dialysis units to send referrals by secure email with a same-day acknowledgment. Six months later, the northern median is 20 days.</p>
<p class="tc-scene-take">The average hid the gap; the split found it; the same definition proved the fix worked.</p>}}
{{key:Split every access measure by group at least once a year, act on the gaps, and re-measure with the same definition.}}
"""),
    ],
    "debrief": ["""
<p><strong>Privacy today.</strong> Report the open folder of donor psychiatric reports to the data protection officer within the hour and ask IT to restrict access to the named roles; do not delete anything. Secure the printed wait-list in locked storage or return it to the system owner for proper disposal, and report it as well. Remind the team that patient details belong only in approved systems.</p>
<p><strong>Defining the rate.</strong> Write the definition first: numerator, denominator, time window, exclusions stated in advance, and how donors abroad are handled (kept in the denominator; results from their own doctor count if received). Then recount.</p>
<p><strong>Reporting.</strong> Report &ldquo;15 of 20 (75%)&rdquo; with a note that, with 20 donors, the uncertainty is wide, and show the trend over time rather than one number. Add an equity split for donors living far from the center or abroad, since distance is a common barrier to follow-up.</p>
"""],
    "skills": {"title": "Privacy check and a defined measure",
               "intro": "Audit a mock program folder for privacy problems and build one defined measure while your preceptor observes.",
               "items": [
                   ("Identifies minimum-necessary and access-control failures in a mock shared folder.", True),
                   ("Reports a simulated privacy incident to the data protection officer within the hour without deleting evidence.", True),
                   ("Writes a measure definition with numerator, denominator, window, and exclusions before counting.", True),
                   ("Reports a rate with counts and a statement of uncertainty.", False),
                   ("Splits a measure by at least two groups and states one finding.", False),
               ],
               "placement": "Run an access review of your program&rsquo;s restricted donor records with the data protection officer."},
    "terms": [("Registry", "A database for a defined purpose with a defined owner."), ("Authorized user", "A trained, designated person with their own account."),
              ("Restricted record", "Information open only to those who need it."), ("Numerator", "The count of events."),
              ("Denominator", "The count of people who could have had the event."), ("Confidence interval", "A range showing a rate&rsquo;s uncertainty."),
              ("Equity review", "Comparing measures across groups.")],
    "readings": [("philhealth-z-packages.html", "The patient guide to PhilHealth&rsquo;s packages, including registry requirements.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["19"])
