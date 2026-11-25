# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 15: Medicines, Discharge, and Self-Management. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator doing teach-back with a recipient holding a labeled pill organizer while his wife watches.",
    "objectives": [
        "Explain why continuous immunosuppression matters, using the mechanism and the evidence on nonadherence.",
        "Confirm that a recipient has an actual medicine supply, a refill route, and a funding route before discharge.",
        "Use teach-back to confirm that a person can do each self-care action, not just name it.",
        "Calculate a medicine supply runway and plan refills before supply runs out.",
        "Confirm that the donor leaves with a recovery plan and follow-up contact of their own.",
    ],
    "big": """
{{plain:Immunosuppressant medicines are like a guard dog&rsquo;s leash. The immune system will always see the new kidney as foreign. The medicines do not make it forget; they hold it back. Drop the leash for a day or two and the dog lunges. That is why the medicines are taken every day, at the right times, for as long as the kidney works.}}
{{fig:rtc15_runway}}
<p>The picture has a limit. A dog lunges at once; rejection usually builds silently over days to weeks, often without symptoms, and shows up first as a change in blood tests. That silence is the danger: a recipient who feels well may decide the medicines are no longer needed, or may run out over a holiday and think a few missed days are harmless.</p>
<p>The evidence says nonadherence is common and dangerous. A meta-analysis of 147 studies found that immunosuppressant nonadherence was highest among kidney recipients, about 36 cases per 100 patient-years.[[rtc_dew2007]] A systematic review found a median of 22% of kidney recipients nonadherent, that a median of 36% of graft losses were associated with prior nonadherence, and that the odds of graft failure were about sevenfold higher in nonadherent recipients.[[rtc_butler2004]] These are observational findings, and adherence was often self-reported, but the direction is consistent. Your job is to make adherence possible: supply, money, understanding, and a plan for the days things go wrong.</p>
{{cards:Key terms for this module|Immunosuppressant::A medicine that holds back the immune response to the transplanted kidney.|Adherence::Taking medicines as agreed with the team: right dose, right time, every day.|Teach-back::The person explains or shows what they will do, in their own words.|Supply runway::How many days a person&rsquo;s medicine on hand will last.|Drug-level monitoring::Blood tests that measure some immunosuppressants, interpreted by the team.}}
""",
    "case": {"title": "Discharge on a Friday before a long weekend", "html": """
<p>Mr. Jose Ramos, 42, a public school teacher, is being discharged on the Friday before a four-day holiday weekend, eight days after his transplant. His wife, Mrs. Elena Ramos, donated the kidney and was discharged two days earlier.</p>
<p>Mr. Ramos has 40 tablets of one immunosuppressant and takes 4 a day. The outpatient pharmacy that dispenses under the post-transplant package needs 5 working days to restock and is closed for the holiday.</p>
<p>When you ask whether he understands his medicines, he says, &ldquo;Yes, the nurse explained.&rdquo; Asked to show you which tablets he takes at 8 p.m., he picks up the wrong box. Mrs. Ramos has not had a follow-up appointment booked.</p>
""", "questions": ["How long will his supply last, and what must happen before he leaves?",
                  "How do you confirm he can take his medicines correctly?",
                  "What is missing for Mrs. Ramos?"]},
    "sections": [
        ("continuity", "Continuity starts before leaving", "Supply, refill, funding, contact", """
<p>A discharge plan that lists medicines but does not confirm where the next box comes from is a plan to run out. Check four things before discharge, and write them on the discharge plan.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Question</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td>Supply</td><td>How many days of each medicine are on hand?</td><td>Counted, and the runway calculated</td></tr>
<tr><td>Refill route</td><td>Where will the next supply come from, and how long does it take?</td><td>Named pharmacy, lead time, and opening days</td></tr>
<tr><td>Funding</td><td>Who pays for the next supply?</td><td>The post-transplant package or other source confirmed[[rtc_ph2025a]]</td></tr>
<tr><td>Contact</td><td>Whom does the recipient call when supply is at risk?</td><td>A named number, including after hours</td></tr>
</tbody></table></div>
{{formula:Days of supply = tablets on hand &divide; tablets per day. Refill must start by: run-out date &minus; lead time (in working days, around closures).}}
<p>The <a href="calc-transplant-coordinator-toolkit.html#tool-6">medicine supply runway tool</a> does this arithmetic. The coordinator never changes doses or substitutes brands; switching between products of the same immunosuppressant can change blood levels, so any switch goes through the team.</p>
{{key:No discharge without a counted supply, a refill route, a funding route, and a named contact.}}
"""),
        ("teach", "Teach actions, not names", "Show me, do not tell me", """
<p>&ldquo;Do you understand?&rdquo; invites a polite yes. Teach-back asks the person to show what they will actually do: pick the 8 p.m. tablets, set an alarm, say what they will do if they vomit a dose, say whom they will call. If they cannot, the fault is in the teaching, not in the person; teach again, differently, and check again.</p>
<ul>
<li>Use the person&rsquo;s own medicine boxes and a pill organizer, not a leaflet alone.</li>
<li>Use the language the person thinks in.</li>
<li>Include the caregiver, with the recipient&rsquo;s permission.</li>
<li>Teach the &ldquo;bad day&rdquo; plan: a missed dose, vomiting, diarrhea, a fever, running low.</li>
</ul>
<p>Clinical coordinators may do medicine teaching if assigned. Support staff arrange it with the pharmacist or nurse and check that it happened.</p>
{{scene:The two white boxes|<p>A recipient has two immunosuppressants in similar white boxes. At teach-back he confuses them. Coordinator Ms. Karen Dela Cruz, with the pharmacist, puts a colored sticker on each box matching a column in his written schedule.</p>
<p>He repeats the teach-back correctly twice, and his daughter repeats it once.</p>
<p class="tc-scene-take">The fix was not more explaining. It was making the right action easy to see.</p>}}
{{key:Teach-back is the person doing the action correctly. A yes is not evidence.}}
"""),
        ("feasible", "Discharge must be feasible", "A plan the person can actually follow", """
<p>A discharge plan has to fit the person&rsquo;s life: clinic visits and blood tests often several times a week at first, transport, cost, work, and family. Ask what will make the first month hard, and solve what you can before they leave.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Confirm before discharge</th></tr></thead>
<tbody>
<tr><td>First clinic and laboratory visits</td><td>Dates, times, place, and transport</td></tr>
<tr><td>Drug-level tests</td><td>When to take the blood test in relation to the dose, as the team instructs</td></tr>
<tr><td>Urgent symptoms</td><td>What to watch for and whom to call (Module 16)</td></tr>
<tr><td>Holiday and weekend coverage</td><td>Pharmacy, laboratory, and contact numbers that work on those days</td></tr>
<tr><td>Transfers</td><td>If care continues elsewhere, an accepted handoff to that service</td></tr>
</tbody></table></div>
<p>The site&rsquo;s <a href="calc-tacrolimus-level-check.html">tacrolimus level check</a> is a clinician tool; coordinators make sure the level is drawn at the right time and the result reaches the team.</p>
{{key:Plan the first month with the person, including holidays. A plan that cannot be followed is not a plan.}}
"""),
        ("donor", "The donor goes home too", "A separate recovery plan", """
<p>Donors are often discharged first, quietly, while attention is on the recipient. Before a donor leaves, confirm their own plan: wound care, pain relief, activity limits, warning signs, their own follow-up appointment, the donor team&rsquo;s contact number, and that donation-related care will not be charged to them.[[rtc_doh2021]] The long-term follow-up plan begins here (Module 17).</p>
{{key:Every donor leaves with their own appointment and their own contact number, separate from the recipient&rsquo;s.}}
"""),
    ],
    "debrief": ["""
<p><strong>The runway.</strong> 40 tablets &divide; 4 a day = 10 days. With a 5-working-day lead time and a four-day closure, the refill must be arranged before he leaves. Ask the team and pharmacy for an adequate discharge supply or a dispensing arrangement that covers the holiday, confirm the funding route under the post-transplant package, and write the next refill date on his plan. Never suggest skipping or stretching doses.</p>
<p><strong>Teach-back.</strong> He picked the wrong box, so he cannot yet take his medicines safely. Re-teach with his own boxes, a pill organizer, and visual cues; include a caregiver with his consent; repeat teach-back until he does it correctly. If he is not ready, tell the discharging physician before he goes.</p>
<p><strong>Mrs. Ramos.</strong> She has no follow-up appointment. Book it with the donor team, give her the donor team&rsquo;s contact number, confirm she has not been charged for donation-related care, and start her long-term follow-up plan.</p>
"""],
    "skills": {"title": "Discharge readiness and teach-back",
               "intro": "Prepare a simulated recipient and donor for discharge while your preceptor observes.",
               "items": [
                   ("Calculates the supply runway and the latest safe refill date, accounting for closures.", True),
                   ("Confirms refill route, funding route, and a named contact before discharge.", True),
                   ("Uses teach-back with the person&rsquo;s own medicines and repeats until correct.", True),
                   ("Teaches the bad-day plan: missed dose, vomiting, fever, running low.", False),
                   ("Never changes doses or substitutes brands; routes any supply problem to the team.", True),
                   ("Confirms the donor&rsquo;s own follow-up appointment and contact.", False),
               ],
               "placement": "Audit three recent discharges: was a supply runway recorded, and did each donor leave with an appointment?"},
    "terms": [("Immunosuppressant", "A medicine that holds back the immune response to the kidney."), ("Adherence", "Taking medicines as agreed."),
              ("Teach-back", "The person shows what they will do."), ("Supply runway", "Days of medicine on hand."),
              ("Drug-level monitoring", "Blood levels of some immunosuppressants, interpreted by the team.")],
    "readings": [("kidney-transplant.html", "The patient guide&rsquo;s section on life after transplant."),
                 ("viral-infections-vaccinations-ckd.html", "Infections and vaccinations in kidney disease, including after transplant.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-6", "calc-tacrolimus-level-check.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["15"])
