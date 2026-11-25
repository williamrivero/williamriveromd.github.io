# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 17: Lifelong Follow-Up for Donor and Recipient. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator greeting a healthy adult donor at a clinic reception for a yearly check-up, smiling.",
    "objectives": [
        "Build two continuing-care plans, one for the recipient and one for the donor, each with schedule, tests, funding, and contact.",
        "Explain why a donor&rsquo;s yearly check-up matters, using the long-term risk evidence.",
        "Run a respectful recall when a donor or recipient misses follow-up.",
        "Navigate graft failure early: dialysis access, retransplant evaluation, and support, led by the team.",
    ],
    "big": """
{{plain:A transplant is not a finish line; it is the start of a long road trip with two cars. Both cars need regular servicing. The recipient&rsquo;s car is obviously working hard, so nobody forgets its oil changes. The donor&rsquo;s car looks perfect, and that is exactly why its servicing gets skipped.}}
{{fig:rtc17_two_plans}}
<p>The picture has a limit. A car that skips a service usually tells you with a noise. A donor whose blood pressure creeps up, or whose urine starts to leak albumin, feels nothing. Those quiet changes are exactly what yearly checks are designed to catch, because a donor has less kidney reserve (Module 7) and long-term risks that are small but real: in a large US cohort, kidney failure within 15 years was 30.8 per 10,000 donors against 3.9 per 10,000 matched healthy nondonors.[[rtc_muzaale2014]]</p>
<p>KDIGO&rsquo;s living donor guideline asks programs to provide lifelong post-donation care, centered on blood pressure, body weight, kidney function, and albumin in the urine, and the DOH living-donor order makes lifetime monitoring part of the donor&rsquo;s protection.[[rtc_kdigo2017]][[rtc_doh2021]] PhilHealth&rsquo;s post-transplant packages list living donor monitoring among their services.[[rtc_ph2025a]] For the recipient, KDIGO&rsquo;s recipient guideline sets out monitoring and prevention for life: kidney function, drug levels, infections, cancer screening, cardiovascular risk, and bone health.[[rtc_kdigo2009]] Your job is to keep both plans running.</p>
{{cards:Key terms for this module|Continuing-care plan::A person&rsquo;s written schedule of follow-up, tests, funding, and contacts.|Recall::Contacting a person who is due or overdue for follow-up.|Albuminuria::Albumin in the urine; an early sign of kidney stress.|Graft failure::A transplanted kidney that is no longer working well enough.|Retransplant::A second (or later) transplant.}}
""",
    "case": {"title": "Five years later", "html": """
<p>It is five years after Mrs. Gina Torres, 45, received a kidney from her husband, Mr. Ramon Torres, 50. Mrs. Torres comes to clinic every three months; her kidney works well.</p>
<p>Mr. Torres came for his checks at 6 months and 1 year, and then stopped. His last recorded blood pressure, four years ago, was 138/88. He now works night shifts as a security guard and says clinic hours are impossible.</p>
<p>At her visit, Mrs. Torres asks you to &ldquo;remind Ramon to come&rdquo; and offers to bring his urine sample herself. Separately, another recipient, Mr. Oscar Lim, 60, has a creatinine that has risen steadily for a year; his nephrologist says the graft is failing.</p>
""", "questions": ["What is the respectful way to recall Mr. Torres?",
                  "Why not accept Mrs. Torres&rsquo;s offer?",
                  "What does navigation look like for Mr. Lim?"]},
    "sections": [
        ("plans", "Build two continuing-care plans", "Each person, their own plan", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Recipient</th><th>Donor</th></tr></thead>
<tbody>
<tr><td>Who leads</td><td>Transplant nephrology</td><td>Donor team or the clinician the program designates</td></tr>
<tr><td>Typical focus</td><td>Kidney function, drug levels, infection prevention and vaccines, cancer screening, heart and bone health, medicine supply</td><td>Blood pressure, weight, kidney function, urine albumin, general health, wellbeing</td></tr>
<tr><td>Frequency</td><td>Frequent early, then regular for life, as the team sets</td><td>An early post-operative schedule, then at least yearly for life, as the program sets</td></tr>
<tr><td>Funding</td><td>Post-transplant package and other sources</td><td>Not charged to the donor for donation-related follow-up; package lists donor monitoring</td></tr>
<tr><td>Contact</td><td>Recipient&rsquo;s named coordinator</td><td>Donor&rsquo;s named contact</td></tr>
</tbody></table></div>
<p>The <a href="calc-transplant-coordinator-toolkit.html#tool-7">donor follow-up planner</a> drafts an example schedule from the donation date (for example, 6 months, 1 year, 2 years, then yearly). Align it with your program&rsquo;s protocol; schedules used in other countries, such as the United States reporting points, are comparisons, not Philippine rules.[[rtc_optn]]</p>
{{key:Two people, two plans, two contacts. The donor&rsquo;s plan is the program&rsquo;s responsibility as much as the recipient&rsquo;s.}}
"""),
        ("recall", "Recall with respect", "Make it easy to come back", """
<p>People miss follow-up for ordinary reasons: work, distance, cost, feeling well, or not knowing why it matters. A recall that scolds or goes through the family does more harm than good.</p>
{{flow:A respectful recall|Check the record::Due date, last results, preferred contact channel, and who may be contacted.|Contact privately::Through the person&rsquo;s preferred channel, not through the recipient or family.|Explain why::One sentence: &ldquo;We check every donor&rsquo;s blood pressure and kidneys each year because problems are silent and easier to treat early.&rdquo;|Solve the barrier::Evening or weekend slots, a nearer laboratory, results shared by the person&rsquo;s own doctor, help with fare.|Record the outcome::Booked, declined, or unreachable after the program&rsquo;s set attempts; never just close the file.}}
<p>If a donor declines follow-up, respect it, record it, and leave the door open: tell them how to come back at any time.</p>
{{key:Recall privately, explain why in one sentence, solve the barrier, and record the outcome. Never recall a donor through the recipient.}}
"""),
        ("failure", "Navigate changing goals", "When the graft is failing", """
<p>Transplanted kidneys do not always last a lifetime. When a graft is failing, the worst outcome is a person who arrives at an emergency needing dialysis without an access and without a plan. Navigation means starting the conversation early, led by the team: options (dialysis, retransplant, conservative care), preparation (dialysis access, retransplant evaluation, a possible new living donor), medicines (decided by the team), feelings (grief, guilt, and fear are common), and funding (which packages apply next).</p>
<p>The site&rsquo;s guide on allograft failure covers the clinical side for patients and clinicians. Your part is the map: who owns each step, by when, and how the person hears about it.</p>
{{scene:Planning before the crash|<p>A recipient&rsquo;s graft function has fallen steadily for a year. The nephrologist asks coordinator Ms. Liza Reyes to start a transition plan.</p>
<p>She books a modality education session, a vascular access consultation, and a retransplant evaluation visit, and checks the dialysis package enrollment. Four months later the patient starts dialysis through a working fistula, as a planned outpatient.</p>
<p class="tc-scene-take">The difference between an emergency start and a planned one was a plan made months earlier.</p>}}
{{key:Start graft-failure planning while there is time: access, options, support, and funding, led by the team.}}
"""),
        ("respect", "Keep the two journeys separate for life", "Years later, the same rules", """
<p>Separation does not expire. Five years later, the recipient still may not receive the donor&rsquo;s results, and the donor&rsquo;s follow-up is still not arranged through the recipient. A recipient offering to carry the donor&rsquo;s urine sample, or to &ldquo;remind&rdquo; the donor, means well; thank them, and contact the donor directly. A donor&rsquo;s sample must be collected under the program&rsquo;s procedure, with identity confirmed, to be trustworthy.</p>
{{key:The rules of Module 1 last for life: separate records, separate contacts, separate consent.}}
"""),
    ],
    "debrief": ["""
<p><strong>Recalling Mr. Torres.</strong> Contact him directly, through his preferred channel. Explain in one sentence why donors are checked every year. Offer a slot that fits night shifts (early morning after his shift, or a weekend), or a nearer laboratory with results sent to the program. Confirm that donation-related follow-up is not charged to him. Record the outcome.</p>
<p><strong>Mrs. Torres&rsquo;s offer.</strong> Thank her warmly and decline. His follow-up and results are his, and a sample carried by someone else cannot be verified as his. Recalling a donor through the recipient also risks pressure in both directions.</p>
<p><strong>Mr. Lim.</strong> With his nephrologist, start the transition plan now: modality education, dialysis access, retransplant evaluation (including whether a new living donor wishes to come forward privately), psychological support, and the funding route for what comes next. Put each step in the register with an owner and date.</p>
"""],
    "skills": {"title": "Two follow-up plans and a recall",
               "intro": "Draft follow-up plans for a fictional pair and carry out a simulated donor recall while your preceptor observes.",
               "items": [
                   ("Drafts separate recipient and donor follow-up plans with schedule, tests, funding, and contact.", False),
                   ("Explains to a simulated donor why yearly checks matter, in one sentence, with honest risk.", False),
                   ("Recalls a donor privately, without going through the recipient.", True),
                   ("Offers at least two practical solutions to a follow-up barrier.", False),
                   ("Records the recall outcome; does not close a file for nonattendance.", True),
                   ("Lists the steps of a graft-failure transition plan with owners.", False),
               ],
               "placement": "Pull the list of donors who donated 1 to 5 years ago. Calculate how many had a recorded check in the last 12 months."},
    "terms": [("Continuing-care plan", "Written follow-up schedule, tests, funding, and contacts."), ("Recall", "Contacting someone due or overdue for follow-up."),
              ("Albuminuria", "Albumin in the urine."), ("Graft failure", "A transplanted kidney no longer working well enough."),
              ("Retransplant", "A second or later transplant.")],
    "readings": [("transplant-allograft-failure.html", "When a transplanted kidney is failing.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-7", "calc-allograft-egfr-trend.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["17"])
