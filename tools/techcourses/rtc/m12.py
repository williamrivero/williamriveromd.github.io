# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 12: The Waiting List and Deceased Donation. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator on the phone updating a waiting-list record on a computer, with a wall calendar behind her.",
    "objectives": [
        "Distinguish the national waiting list, the PhilHealth KT Data Registry, and the hospital&rsquo;s own transplant list.",
        "Keep a wait-listed candidate &ldquo;ready to be called&rdquo;: contact details, readiness, and sensitizing events current.",
        "Explain why the period on the list matters to survival, with the evidence and its limits.",
        "State the boundary between transplant coordination and organ procurement, including who determines death.",
    ],
    "big": """
{{plain:Being on a waiting list is like being on a standby list for a flight. You only get the seat if the airline can find you the moment it opens up, if your documents are still valid, and if you are actually at the airport. Being on the list is not the same as being ready to board.}}
{{fig:rtc12_databases}}
<p>The picture has a limit. A standby list belongs to one airline. A Philippine transplant candidate may appear in three different databases, each with its own owner and purpose: the national waiting list for deceased-donor organs, set up under DOH policy;[[rtc_doh2023wait]] PhilHealth&rsquo;s KT Data Registry, mandatory for patients pre-authorized for the package;[[rtc_pa2026]] and the hospital&rsquo;s own list. Being on one does not put a person on the others.</p>
<p>And unlike a flight, waiting is not neutral time. In a large United States registry study, people on dialysis who were wait-listed had annual death rates of about 6.3 per 100 patient-years, and transplant recipients, after an early period of higher risk, had much lower death rates than those still waiting.[[rtc_wolfe1999]] The study was observational, so part of the difference reflects who gets transplanted. But it is a reason to treat waiting as active work: keep the person ready, reachable, and as healthy as possible.</p>
{{cards:Key terms for this module|National waiting list::The DOH-governed list of candidates for deceased-donor organs.|KT Data Registry::PhilHealth&rsquo;s registry for patients pre-authorized for the kidney transplant package.|Active status::Ready to receive an offer now.|Temporarily inactive::On the list but not able to accept an offer for a stated reason and period.|Philippine Network for Organ Sharing (PhilNOS)::The national program that coordinates deceased organ donation and sharing.|Organ procurement organization (OPO)::The service that manages deceased donors and organ retrieval.}}
""",
    "case": {"title": "The candidate who moved", "html": """
<p>Ms. Angelica Reyes, 36, has been on the national waiting list for 19 months and on hemodialysis for four years. Her husband was ruled out as a donor. Last month she moved to Cebu for work, changed her mobile number, and started dialysis at a new unit there. She had a blood transfusion during a hospital stay in Cebu three weeks ago.</p>
<p>The PhilHealth KT Data Registry shows her as &ldquo;registered.&rdquo; Her mother asks you, &ldquo;Since she&rsquo;s in the registry, she&rsquo;s next in line, right?&rdquo;</p>
<p>That evening, a family member of a brain-injured patient in your hospital&rsquo;s intensive care unit asks a nurse whether &ldquo;the transplant coordinator&rdquo; can tell them if their relative is dead.</p>
""", "questions": ["Which records need updating, and who owns each?",
                  "What is true and untrue in her mother&rsquo;s statement?",
                  "How do you answer the family in the intensive care unit?"]},
    "sections": [
        ("three", "Three databases, three purposes", "Which list is which", """
<div class="table-wrap"><table>
<thead><tr><th>Database</th><th>Owner</th><th>Purpose</th><th>What being on it does not mean</th></tr></thead>
<tbody>
<tr><td>National waiting list</td><td>DOH and its designated program, through authorized users</td><td>Candidates for deceased-donor organs</td><td>A guaranteed or imminent offer</td></tr>
<tr><td>PhilHealth KT Data Registry</td><td>PhilHealth and the reference facility</td><td>A package requirement; from May 1, 2026 all pre-authorized patients are registered electronically</td><td>Being on the national waiting list, or being pre-authorized</td></tr>
<tr><td>Hospital transplant list</td><td>The transplant program</td><td>Local tracking of candidates and status</td><td>Entry on either national system</td></tr>
</tbody></table></div>
<p>PhilHealth Advisory 2026-0026 made electronic KT registry registration mandatory for patients pre-authorized for the package from May 1, 2026, with manual forms accepted until April 30, 2026; registration is a condition of the benefit, and missing registration is a ground for claim denial.[[rtc_pa2026]][[rtc_ph2026]] Only trained, designated users enter data. Reconcile the three databases regularly: same person, same status, same contact details.</p>
{{key:Three lists, three owners. Confirm each entry separately and reconcile them on a schedule.}}
"""),
        ("active", "Waiting is active coordination", "Ready, reachable, and current", """
<p>An offer for a deceased-donor kidney leaves little time. A candidate who cannot be reached, or who is not ready, misses it. Keep a waiting-list contact at a regular interval your program sets, and use the same questions every time.</p>
<ul>
<li><strong>Reachable:</strong> current phone numbers (two if possible), address, dialysis unit and its contact, who may be told of an offer.</li>
<li><strong>Ready:</strong> any new illness, admission, infection, surgery, or change in medicines; any reason they could not come in today.</li>
<li><strong>Sensitizing events:</strong> transfusion, pregnancy, or surgery since the last contact (Module 5), reported the same day to the team and the HLA laboratory.</li>
<li><strong>Funding:</strong> pre-authorization status and validity, and any change in PhilHealth membership.</li>
</ul>
<p>Changes in readiness go to the transplant physician, who decides whether status changes. Results that expire while waiting (Module 4) are flagged before they lapse.</p>
{{scene:The number nobody updated|<p>Coordinator Ms. Rina Castillo does a quarterly contact with a wait-listed candidate and finds that his number has changed and that he started dialysis at a different unit after a move.</p>
<p>She updates the hospital list, asks the designated user to update the national entry, and gives the new dialysis unit her direct number for transfusions and admissions.</p>
<p class="tc-scene-take">The candidate had not missed an offer yet. The point of the call was to make sure he never would.</p>}}
{{key:On the list is not the same as ready. Contact, readiness, sensitizing events, and funding: check all four on every waiting-list call.}}
"""),
        ("boundary", "Know the procurement boundary", "What the transplant coordinator never does", """
<p>Deceased donation has its own law, rules, and people. The Organ Donation Act governs donation after death;[[rtc_ra7170]] DOH rules define the roles of procurement and clinical transplant coordinators, separately.[[rtc_doh2010b]] Three acts belong to others:</p>
<div class="table-wrap"><table>
<thead><tr><th>Act</th><th>Who does it</th><th>Why the transplant coordinator does not</th></tr></thead>
<tbody>
<tr><td>Determining and declaring death</td><td>Physicians authorized under the law and hospital protocol, independent of the transplant team</td><td>Separating death determination from transplantation protects public trust</td></tr>
<tr><td>Approaching the family about donation</td><td>Trained requesters or the procurement team, under protocol</td><td>A request from the recipient&rsquo;s side creates a conflict of interest</td></tr>
<tr><td>Managing the deceased donor and retrieval</td><td>The OPO or procurement team, with PhilNOS</td><td>A different role with its own training</td></tr>
</tbody></table></div>
<p>If a family in an intensive care unit asks you about death or donation, respond with compassion, do not discuss donation or the transplant waiting list, and connect them with the attending physician and, through protocol, with the procurement team.</p>
{{key:The transplant coordinator never determines death, never asks a grieving family for organs, and never mixes the recipient&rsquo;s interests into a donor family&rsquo;s decision.}}
"""),
        ("compare", "Allocation scores from elsewhere", "Know what you are looking at", """
<p>This site hosts calculators for the Kidney Donor Profile Index (KDPI) and the Estimated Post-Transplant Survival (EPTS) score. They are tools from United States allocation policy and are shown for comparison and learning.[[rtc_optn]] Philippine allocation follows Philippine rules; coordinators do not accept or rank offers by any score. If a family brings a score from the internet, explain gently that the team and the national program apply local rules.</p>
{{key:Foreign allocation scores are for learning, not for deciding Philippine offers.}}
"""),
    ],
    "debrief": ["""
<p><strong>Records.</strong> Update the hospital list (new number, new address, new dialysis unit). Ask the designated user to update the national waiting-list entry and the KT registry contact data as each system allows. Report the transfusion today to the transplant physician and the HLA laboratory; the team decides whether a new antibody sample is needed and whether her status changes. Give the Cebu unit your direct number.</p>
<p><strong>Her mother&rsquo;s statement.</strong> True: she is in PhilHealth&rsquo;s registry. Untrue: the registry is not the waiting list, and neither means &ldquo;next in line.&rdquo; Explain the difference kindly, and that offers depend on many factors the national program and the team apply.</p>
<p><strong>The family in the intensive care unit.</strong> Express sympathy, explain that the doctors caring for their relative are the ones who can answer, and help them reach the attending physician now. Do not mention donation or the waiting list; if donation is relevant, the procurement team approaches through protocol.</p>
"""],
    "skills": {"title": "Waiting-list contact and reconciliation",
               "intro": "Conduct a simulated waiting-list call and reconcile three mock database entries while your preceptor observes.",
               "items": [
                   ("Explains the difference between the national waiting list, the KT registry, and the hospital list.", True),
                   ("Asks about contact details, readiness, sensitizing events, and funding in one call.", False),
                   ("Reports a sensitizing event and a readiness change to the transplant physician the same day.", True),
                   ("Finds and routes a discrepancy between database entries to the designated user.", False),
                   ("Responds to a simulated grieving family without discussing donation, and routes to the attending physician.", True),
               ],
               "placement": "Reconcile ten candidates across your hospital list and the systems you can see; list every mismatch and its owner."},
    "terms": [("National waiting list", "DOH-governed list for deceased-donor organs."), ("KT Data Registry", "PhilHealth&rsquo;s registry for pre-authorized patients."),
              ("Active status", "Ready for an offer now."), ("PhilNOS", "Philippine Network for Organ Sharing."), ("OPO", "Organ procurement organization."),
              ("KDPI", "Kidney Donor Profile Index (US)."), ("EPTS", "Estimated Post-Transplant Survival (US).")],
    "readings": [("organ-donation-philippines.html", "Organ donation in the Philippines, for the public.")],
    "calcs": ["calc-kdpi-kdri.html", "calc-epts.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["12"])
