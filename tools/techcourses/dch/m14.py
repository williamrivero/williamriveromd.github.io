# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 14: New Services, Handover, and Your First 90 Days. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician walking a newly installed hemodiafiltration station with a biomedical engineer before it is released for use.",
    "objectives": [
        "Frame a new technology as a question: population, intervention, comparison, and outcome.",
        "Appraise the evidence for hemodiafiltration, converting relative effects into absolute effects and numbers needed to treat.",
        "Check infrastructure, water, monitoring, staffing, and cost before committing to a new service.",
        "Plan a staged launch with stop criteria agreed in advance, and a review date for continuing, extending, or stopping.",
        "Give and receive a handover that lists every open item with an owner and a deadline.",
        "Build a 30-60-90 day plan that starts with the work people are already waiting for.",
    ],
    "big": """
{{plain:A new service is like adding a floor to a house. Before you build up, you check the foundations: the water supply, the wiring, the people who will live there, and whether the floor below is already cracked.}}
<p>The picture has a limit. A house does not change while you build. A dialysis unit does: patients arrive, staff leave, and the evidence for a technology can change between the day you decide and the day you open. Build a review date into every decision.</p>
{{cards:Key terms for this module|Hemodiafiltration (HDF)::Hemodialysis combined with convection: large volumes of fluid are filtered from the blood and replaced with ultrapure fluid, removing larger molecules more effectively.|Convection volume::The total volume filtered by convection in one session, usually in liters.|Relative risk reduction::The proportional fall in risk with a treatment.|Absolute risk reduction::The difference in risk between groups, in percentage points.|Number needed to treat (NNT)::How many patients must be treated for a given time to prevent one event.|Stop criterion::A condition agreed in advance that pauses or ends a pilot.}}
""",
    "case": {"title": "The night shift already announced", "html": """
<p>You start as clinical head of a twelve-station unit in Angeles City. In your first week you find a two-week backlog of new referrals, a disaster drill overdue by eight months, and two machines whose maintenance records stop in June. Your predecessor offers a ten-minute handover in the hallway.</p>
<p>The owner, Mr. Benjamin Lacson, has already announced a night shift starting next week. He also shows you a vendor brochure: &ldquo;Hemodiafiltration lowers mortality by 23%. Our competitor has it. I want it by March.&rdquo;</p>
""", "questions": ["What needs your attention this week?",
                  "What would you need to see before agreeing to the night shift?",
                  "How do you respond to the brochure&rsquo;s claim and the March deadline?"]},
    "sections": [
        ("question", "Framing the question", "Write the question before you buy the answer", """
{{fig:dch14_pico}}
<p>Every technology is an answer to a question. Write the question first: in which patients, compared with what, to improve which outcome? For hemodiafiltration: in adults on maintenance hemodialysis who can achieve high convection volumes, does high-volume hemodiafiltration, compared with high-flux hemodialysis, reduce death from any cause?</p>
<p>Then ask what alternatives would answer the same need, such as making the existing service more reliable: fewer catheters, fewer missed sessions, better delivered dose. A new machine does not fix a unit that cannot keep its current patients on schedule.</p>
"""),
        ("evidence", "The evidence", "What the hemodiafiltration evidence shows", """
<p>The CONVINCE trial randomized 1,360 adults across European centers to high-dose hemodiafiltration or continued high-flux hemodialysis. Over a median of 30 months, with a mean convection volume of 25.3 liters per session, death from any cause occurred in 17.3% of the hemodiafiltration group and 21.9% of the hemodialysis group (hazard ratio 0.77, 95% confidence interval 0.65 to 0.93).[[dch_blankestijn2023]]</p>
{{formula:<strong>From relative to absolute.</strong> A hazard ratio of 0.77 is the brochure&rsquo;s &ldquo;23% lower mortality.&rdquo; The absolute difference was 21.9% &minus; 17.3% = 4.6 percentage points over about 30 months. Number needed to treat = 1 &divide; 0.046 &asymp; 22 patients treated for about two and a half years to prevent one death. Calculator 9 does this for any trial.}}
{{fig:dch14_iconarray}}
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Finding</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>CONVINCE, randomized[[dch_blankestijn2023]]</td><td>Lower all-cause mortality with high-dose HDF</td><td>Strong for patients who can achieve high convection volume; not blinded; European centers with ultrapure water</td></tr>
<tr><td>EuDial consensus of the European Renal Association, 2025[[dch_battaglia2025]]</td><td>HDF appears associated with improved overall and cardiovascular survival, provided high convection volumes are achieved; generalizability depends on patients&rsquo; overall health</td><td>Consensus from meta-analyses and expert opinion; not a standard of care</td></tr>
<tr><td>International retrospective cohort, 71,669 patients[[dch_zhang2025]]</td><td>HDF associated with about 20% fewer hospital admissions and hospital days</td><td>Observational; residual confounding possible</td></tr>
<tr><td>H4RT, United Kingdom, randomized[[dch_caskey2022]]</td><td>Compares high-volume HDF with high-flux HD on non-cancer mortality or hospitalization with cardiovascular events or infection</td><td>Follow-up ended in May 2025; results were not found in the literature searched on November 24, 2026</td></tr>
</tbody></table></div>
<p>The benefit depends on dose. Patients who cannot achieve high convection volumes, often because of poor vascular access or low blood flow, may not gain it. The evidence supports offering high-volume HDF where the unit can deliver it reliably; it does not yet tell you that every patient must have it. Check whether H4RT has reported before you decide.</p>
<p>Modality and schedule can also be combined. In a Spanish randomized trial in patients starting dialysis with residual kidney function, twice-weekly incremental HDF gave clinical outcomes similar to thrice-weekly HDF with about 70 rather than 123 sessions a year; it was a small trial and needs confirmation.[[dch_fernandezlucas2025]]</p>
"""),
        ("readiness", "Readiness", "What a new service needs before day one", """
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>Question</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Permission</td><td>Does the change need a Department of Health (DOH) or PhilHealth decision first? (Modules 2 and 3)</td><td>Compliance lead</td></tr>
<tr><td>Water</td><td>Can the system deliver ultrapure water and the larger volumes HDF needs, with monitoring?[[dch_iso2024]]</td><td>Technical lead</td></tr>
<tr><td>Equipment</td><td>Are machines commissioned, released, and maintained under contract?</td><td>Biomedical lead</td></tr>
<tr><td>People</td><td>Are nurses trained and validated, and is the night shift staffed with the same competencies as the day?</td><td>Head nurse</td></tr>
<tr><td>Patients</td><td>Who is eligible, how will convection volume be measured, and how will patients consent?</td><td>Clinical head</td></tr>
<tr><td>Money</td><td>What do utilization and total cost look like under low and high uptake?</td><td>Finance</td></tr>
<tr><td>Continuity</td><td>Can the unit still meet its disaster and transfer obligations with the added service?</td><td>Operations</td></tr>
</tbody></table></div>
{{fig:dch14_stage}}
<p>Launch in stages, with stop criteria agreed before the first patient: for example, a water result above an action level, a convection volume target missed in most sessions, or a staffing shortfall on any night. Set a review date for continuing, extending, or stopping. If the decision is deferred, keep the original scope and model how demand will be met safely meanwhile.</p>
{{call:Stop any new service or shift that lacks required permissions, validated staff, released equipment, or verified water capacity, whatever date has been announced. Escalate the gap and the options to the owner in writing.}}
"""),
        ("first90", "Your first 90 days", "Handover and the first 90 days", """
<p>A handover is complete when the incoming lead has acknowledged, in writing, every open item: pending results, transfers in progress, complaints, corrective actions, workforce gaps, maintenance, and regulatory deadlines, each with an owner and a due date. What is not written is not handed over.</p>
{{fig:dch14_306090}}
{{flow:30-60-90|First 30 days::Reconcile your appointment, scope, and policy versions. Walk a shift. Trace a referral and a claim. Inspect water and machine evidence with the technical leads. Meet nursing, operations, and patient representatives.|Days 31 to 60::Complete a focused risk review and a continuity test.|Days 61 to 90::Present a small number of measurable improvements, budget decisions, and open issues to the owner.}}
{{key:Spend your first week finding the work people are already waiting for. A referral, a result, a repair, or a staffing decision each needs an owner before you plan the future.}}
<p>Distinguish containment from improvement. A machine with no maintenance record is a hold this week. A new quality dashboard can wait for day 60.</p>
"""),
    ],
    "debrief": ["""
<p><strong>This week.</strong> Ask for the handover in writing, with every open item, owner, and deadline. Hold the two machines without maintenance records until the biomedical lead releases them. Clear the referral backlog by giving each referral an owner and a date. Schedule the overdue disaster drill.</p>
<p><strong>Before the night shift.</strong> Written readiness criteria: any required permission, validated nurses and physician coverage at night equal to the day, released machines, verified water capacity for the extra hours, and transport for patients leaving late at night. Publish the criteria and a date to review them with Mr. Lacson. If they are not met, the start date moves.</p>
<p><strong>The brochure and March.</strong> The 23% is a relative reduction from CONVINCE. Explain the absolute difference, about 4.6 percentage points over two and a half years, or one death prevented for about every 22 patients treated, in patients who achieved high convection volumes. Offer to appraise HDF properly: eligible patients, water and machine requirements, staff training, cost under low and high uptake, and whether H4RT has reported. A staged pilot with stop criteria may be reasonable later in the year; a March deadline set before the water system has been assessed is not.</p>
"""],
    "skills": {"title": "Technology appraisal, go/no-go brief, and handover",
               "intro": "Prepare a go/no-go brief for a new service and a written handover, and defend them at a mock review where the board asks for immediate extra capacity.",
               "items": [
                   ("Writes the question as population, intervention, comparison, and outcome.", False),
                   ("Converts a relative effect into an absolute difference and number needed to treat.", False),
                   ("Identifies whether newer evidence, such as H4RT, has reported before deciding.", False),
                   ("Checks permissions, water, equipment, staff, patients, money, and continuity.", True),
                   ("Agrees stop criteria and a review date before launch.", True),
                   ("Holds a launch that lacks permission, validated staff, released equipment, or water capacity.", True),
                   ("Obtains a written handover with owners and deadlines for every open item.", False),
                   ("Separates this week&rsquo;s containment from improvements that can be sequenced.", False),
               ],
               "placement": "Write your own 30-60-90 day plan, or review the one you are living. Present it to your owner and ask for one decision you need to begin."},
    "quiz": [
        ("What should you write before evaluating a new technology?",
         ["The budget", "The question: population, intervention, comparison, outcome", "The press release", "The vendor list"], 1,
         "Every technology answers a question."),
        ("In CONVINCE, what was the hazard ratio for death with high-dose HDF?",
         ["0.50", "0.77", "1.00", "1.23"], 1,
         "95% confidence interval 0.65 to 0.93."),
        ("Deaths were 21.9% with HD and 17.3% with HDF. What is the absolute risk reduction?",
         ["23%", "4.6 percentage points", "17.3%", "0.77"], 1,
         "21.9 minus 17.3."),
        ("What is the number needed to treat for an absolute reduction of 4.6 percentage points?",
         ["About 5", "About 22", "About 77", "About 100"], 1,
         "1 divided by 0.046, over about 30 months."),
        ("A brochure says HDF lowers mortality by 23%. What is missing?",
         ["Nothing", "The absolute effect, the population, the convection volume achieved, and the time", "The color of the machine", "The price"], 1,
         "Relative effects alone overstate benefit."),
        ("Which patients may not gain the survival benefit of HDF?",
         ["All gain equally", "Those who cannot achieve high convection volumes", "Younger patients", "Patients with fistulas"], 1,
         "Benefit depends on dose."),
        ("What did the 2025 EuDial consensus conclude?",
         ["HDF is harmful", "HDF appears associated with improved survival provided high convection volumes are achieved", "HDF is the mandatory standard", "No conclusion"], 1,
         "Consensus, not a standard of care."),
        ("What is the status of the UK H4RT trial in this course?",
         ["Stopped for harm", "Follow-up ended in 2025; results not found in the literature searched", "Showed no benefit", "Not registered"], 1,
         "Check whether it has reported before deciding."),
        ("Which infrastructure question is specific to HDF?",
         ["Parking", "Whether the water system can deliver ultrapure water in larger volumes with monitoring", "Chair color", "Reception hours"], 1,
         "HDF uses the fluid as a replacement infused into the blood."),
        ("What is a stop criterion?",
         ["A deadline", "A condition agreed in advance that pauses or ends a pilot", "A budget cap", "A staff quota"], 1,
         "Agree it before you start."),
        ("The owner announced a night shift before readiness was checked. What do you do?",
         ["Open it as announced", "Publish readiness criteria and a review date; move the start if they are not met", "Refuse to discuss it", "Open with fewer patients without checks"], 1,
         "A launch that must be pulled back hurts more than a delay."),
        ("When is a handover complete?",
         ["After a conversation", "When the incoming lead acknowledges every open item, owner, and deadline in writing", "After a week", "When the predecessor leaves"], 1,
         "What is not written is not handed over."),
        ("What should your first week focus on?",
         ["Strategy", "Work people are already waiting for: referrals, results, repairs, staffing", "Branding", "New hires"], 1,
         "Give each an owner first."),
        ("Two machines have no maintenance records since June. When do you act?",
         ["Day 90", "This week: hold them until released", "At the next inspection", "Never"], 1,
         "Containment cannot wait for the plan."),
        ("What should a pilot&rsquo;s review decide?",
         ["Only the cost", "Whether to continue, extend, or stop, against agreed safety and performance criteria", "Who to blame", "Nothing"], 1,
         "Set the review date at the start."),
    ],
    "terms": [("Hemodiafiltration (HDF)", "Hemodialysis combined with high-volume convection and ultrapure replacement fluid."),
              ("Convection volume", "Total volume filtered by convection in one session."),
              ("Relative risk reduction", "The proportional fall in risk."),
              ("Absolute risk reduction", "The difference in risk in percentage points."),
              ("Number needed to treat", "Patients treated for a given time to prevent one event."),
              ("Stop criterion", "A pre-agreed condition that pauses or ends a pilot."),
              ("Handover", "Written transfer of open items, owners, and deadlines.")],
    "readings": [("hemodiafiltration-new-standard.html", "Is hemodiafiltration the new standard?"),
                 ("expanded-hemodialysis-hdx.html", "Expanded hemodialysis (HDx)."),
                 ("incremental-dialysis.html", "Incremental dialysis.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
