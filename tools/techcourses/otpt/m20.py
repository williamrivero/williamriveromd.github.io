# -*- coding: utf-8 -*-
"""OT/PT track, Module 20: Integrated Renal Rehabilitation Capstone. Written for this series from published sources."""

MODULE = {
    "image_alt": "An occupational therapist and a physical therapist presenting a case plan to a small team in a training room.",
    "objectives": [
        "Integrate authority, screening, access safety, assessment, intervention, documentation and benefits navigation in one case.",
        "Prioritize problems with the patient and family, and agree a single shared plan across OT and PT.",
        "Demonstrate your profession&rsquo;s six practical stations to the pass standard with no critical failure.",
        "Hand over the plan to the renal team with SBAR and measurable review points.",
        "Reflect on your own scope and the next steps in your development.",
    ],
    "big": """
{{plain:The capstone is a rehearsal for a real week. One patient arrives with several problems at once, the way patients do, and you have to decide what comes first, who does what, and how you will know it worked.}}
<p>The picture has a limit. A rehearsal can be stopped and repeated. Your patients&rsquo; weeks cannot. That is why the capstone is scored with critical failures that are never averaged away: proceeding past a red flag, compressing or pulling an access, changing a dialysis setting, unsafe lifting, or promising a benefit. Every other mistake is a lesson; those are stops.</p>
<p>The case below draws on every module. Work through it alone first, then with a partner from the other profession, then present it to your preceptor.</p>
{{cards:How the capstone is scored|Written plan::A shared OT and PT plan with prioritized problems, goals, measures and owners.|Six stations::Your profession&rsquo;s set of practical stations, 8 of 10 or better each, no critical failure.|Examination::20 questions, one from each module; pass 16.|Portfolio::Every module&rsquo;s artifact, deidentified.|Reflection::A one-page reflection on scope and next learning steps.}}
""",
    "case": {"title": "Mang Pedring&rsquo;s week", "html": """
<p><strong>Monday.</strong> Mr. Pedro &ldquo;Mang Pedring&rdquo; Salvador, 68, a retired fisherman from Bataan, has been on hemodialysis for 18 months (Monday, Wednesday, Friday mornings) and has type 2 diabetes. A new left forearm fistula was created four weeks ago; he still dialyzes through a right internal jugular catheter. Last Friday he nearly fell walking out of the unit after 3 kilograms of fluid removal. He is exhausted on dialysis afternoons and has stopped visiting his <em>kumpare</em> at the pier. His wife asks if PhilHealth will pay for &ldquo;therapy and a walker.&rdquo;</p>
<p>Findings at a non-dialysis-day assessment: SPPB 6; gait speed 0.62 m/s; five-times sit-to-stand 19 seconds; six-minute walk 245 meters; numb feet with a small blister on the left heel; recovery time &ldquo;until the next morning&rdquo;; PHQ-9 of 11 on the team&rsquo;s screen. He wants &ldquo;to walk to the pier again and sit with my friends on Saturdays.&rdquo; The pier is 400 meters from his house.</p>
""", "questions": ["What are the immediate safety issues, and who must hear about each today?",
                  "What is the prioritized shared plan, and who leads each part?",
                  "How will you answer his wife, and what will you send to whom?"]},
    "sections": [
        ("safety", "Safety first", "Step 1: the safety issues that come before any plan", """
<p>Before any goal, close the safety loops. Each has an owner.</p>
<div class="table-wrap"><table>
<thead><tr><th>Issue</th><th>Why it matters</th><th>Owner and action today</th></tr></thead>
<tbody>
<tr><td>Near fall after 3 kg removal</td><td>Post-dialysis hypotension plus neuropathy; fracture risk</td><td>Nurse and nephrologist informed; PT fall assessment; he waits until steady before leaving</td></tr>
<tr><td>Heel blister in a numb foot</td><td>A pre-ulcer in a person with diabetes on dialysis</td><td>Same-day nurse and physician review; foot-care referral; offload during training</td></tr>
<tr><td>PHQ-9 of 11</td><td>Possible depression; motivation</td><td>Physician and mental-health referral; ask about self-harm thoughts</td></tr>
<tr><td>New fistula (4 weeks) and a neck catheter</td><td>Maturing access; catheter infection risk</td><td>No pressure or loads on the left forearm; basic hand exercise only if the surgeon approves; catheter dressing kept dry</td></tr>
<tr><td>Long recovery time</td><td>Associated with worse outcomes in DOPPS</td><td>Reported to the nephrologist with the fluid removal data</td></tr>
</tbody></table></div>
"""),
        ("plan", "The shared plan", "Step 2: one shared plan, two professions", """
{{formula:<strong>Illustrative shared plan, agreed with Mang Pedring and his wife.</strong><br><strong>Goal:</strong> &ldquo;Walk to the pier (400 m) with one rest and sit with my friends on Saturdays, in 12 weeks.&rdquo;<br><strong>PT (lead: capacity).</strong> Non-dialysis days Tue, Thu, Sat: sit-to-stand, step-ups, ankle-weight knee extensions (no left forearm loading), balance progression; walking from 10 to 30 minutes at RPE 12 to 13 once the heel is cleared; a correctly fitted walker for distances, then a cane if balance allows. Intradialytic leg cycling in the first half of sessions when the nurse agrees.<br><strong>OT (lead: demand and participation).</strong> Energy budget: dialysis afternoons protected for rest; Saturday morning kept free for the pier. Seated bathing; footwear and daily foot checks with his wife; a folding stool for a rest point at the halfway mark to the pier; a plan for the tricycle home if tired.<br><strong>Measures:</strong> SPPB, gait speed, five-times sit-to-stand, 6MWT, recovery time, falls, PHQ-9 at 12 weeks; pier walk as the goal test.<br><strong>Review:</strong> 4, 8 and 12 weeks with the renal team.}}
{{fig:otpt20_shared_plan}}
{{key:One goal, one plan, two leads. The patient should be able to say who is doing what.}}
"""),
        ("handover", "Handover and benefits", "Step 3: handover, documentation and the PhilHealth question", """
{{formula:<strong>Illustrative SBAR to the renal team.</strong> <em>S:</em> Mang Pedring, 68, HD M-W-F, nearly fell after last Friday&rsquo;s session (3 kg UF), has a heel blister in a numb foot and a PHQ-9 of 11. <em>B:</em> Diabetes; left forearm AVF 4 weeks; right IJ catheter; recovery time until next morning. <em>A:</em> High fall risk on dialysis days; pre-ulcer; possible depression; moderate functional impairment (SPPB 6, gait 0.62 m/s, 6MWT 245 m). <em>R:</em> Please review fluid removal and post-dialysis pressure, the heel today, and refer for mood assessment. We propose a 12-week OT/PT plan (attached) and ask for exercise parameters and approval for intradialytic leg cycling.}}
<p>To his wife: &ldquo;I can&rsquo;t promise PhilHealth will pay. There is a rehabilitation and mobility device pathway with its own rules, a doctor&rsquo;s assessment and a contracted provider. I&rsquo;ll write up what he needs and why, and connect you with the person who can check.&rdquo; Then send a dated functional summary and the walker justification to the physiatrist and coordinator (Module 18).</p>
{{stop:Critical failures in the capstone and in practice: proceeding past an unresolved red flag; compressing or pulling an access, or loading the new fistula arm; changing any dialysis setting; unsafe lifting or moving without needed help; promising a benefit. Any one stops the station.}}
"""),
    ],
    "debrief": ["""
<p><strong>Immediate safety.</strong> The near fall (nurse and nephrologist today), the heel blister (same-day review), the PHQ-9 of 11 (physician and mental-health referral, with a question about self-harm), the new fistula and catheter precautions, and the long recovery time (nephrologist).</p>
<p><strong>The shared plan.</strong> One goal in his words, a PT capacity plan and an OT demand and participation plan, measures repeated under the same conditions, and reviews at 4, 8 and 12 weeks.</p>
<p><strong>His wife and the paperwork.</strong> No promise; an explanation of the pathway; a dated functional summary and walker justification to the physiatrist and authorized coordinator; an SBAR and the plan to the renal team. Then the stations: OT learners take OS01, OS02, OS03, OS04, OS05 and OS08; PT learners take OS01, OS02, OS03, OS06, OS07 and OS08, each scored 0 to 2 per item, pass 8 of 10, no critical failure.</p>
"""],
    "skills": {"title": "Integrated capstone",
               "intro": "Present the integrated case to your preceptor, then complete your profession&rsquo;s six practical stations (listed on the trainer page).",
               "items": [
                   ("Identifies every immediate safety issue and names its owner and same-day action.", True),
                   ("Agrees one patient-chosen goal and a shared OT/PT plan with named leads.", False),
                   ("Protects the new fistula and the catheter throughout simulation.", True),
                   ("Gives a complete SBAR and requests parameters and approvals instead of assuming them.", True),
                   ("Answers the benefits question without a promise and routes it correctly.", True),
                   ("Passes the six profession-specific stations at 8 of 10 or better with no critical failure.", True),
                   ("Submits a one-page reflection on scope and next learning steps.", False),
               ],
               "placement": "Complete the capstone with a real or simulated patient under supervision and submit the full portfolio."},
    "terms": [("Critical failure", "An unsafe action that fails a station regardless of the total score."),
              ("Shared plan", "One plan with OT and PT leads for different parts."), ("Portfolio", "The set of deidentified artifacts from every module.")],
    "readings": [("exercise-guide-ckd.html", "The patient guide to exercise in CKD."),
                 ("hemodialysis-elderly.html", "Older adults on dialysis.")],
    "calcs": ["calc-renal-rehabilitation-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["20"])
