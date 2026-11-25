# -*- coding: utf-8 -*-
"""OT/PT track, Module 09: Design and Progress an Individualized Exercise Plan. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient doing seated knee extensions with an ankle weight while a physical therapist counts.",
    "objectives": [
        "Explain what aerobic and resistance training change in uremic muscle and the cardiovascular system, and on what time scale.",
        "State the KDIGO 2024 physical activity recommendation and its grade, and what the trial evidence shows.",
        "Write an individualized prescription using FITT-VP, with intensity set by effort rather than heart rate when appropriate.",
        "Progress the plan safely around the dialysis week and adjust it after missed sessions or illness.",
        "Identify when exercise must be paused and the plan reviewed by the physician.",
    ],
    "big": """
{{plain:Muscle is like a savings account that pays interest only if you keep making deposits. Each session is a small deposit. Skip deposits and the balance drains, faster in kidney failure than in health. Deposit too much at once and you can overdraw, with soreness, exhaustion or injury.}}
<p>The picture has a limit. Interest is not paid at once. In the first few weeks of strength training, most of the gain comes from the nervous system learning to recruit more muscle fibers; actual muscle growth follows over weeks to months. Endurance improves as muscle grows more capillaries and mitochondria and the heart pumps more per beat. So early gains are real but fragile, and the plan must last long enough for the slower changes to arrive.</p>
{{fig:otpt09_adaptation}}
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline recommends that people with CKD be advised to undertake moderate-intensity physical activity for a cumulative duration of at least 150 minutes per week, or to a level compatible with their cardiovascular and physical tolerance. It is graded 1D: a strong recommendation built on very low-certainty evidence.[[otpt_kdigo2024]] The strength reflects the low risk and the broad benefits of activity in the general population; the low certainty reflects how little CKD-specific outcome data exist. The UK Kidney Association&rsquo;s guideline also supports combined aerobic and resistance exercise across CKD, dialysis and transplantation.[[otpt_baker2022]]</p>
{{cards:Key terms for this module|FITT-VP::Frequency, intensity, time, type, volume and progression.|Rating of perceived exertion (RPE)::How hard the work feels, on the 6 to 20 Borg scale; 12 to 14 is &ldquo;somewhat hard.&rdquo;|Resistance training::Work against a load (body weight, bands, weights) to build strength.|Repetition maximum::The most a person can lift for a given number of repetitions.|Progression::A planned increase in load, time or difficulty.}}
""",
    "case": {"title": "Twelve weeks for Mang Jun", "html": """
<p><strong>Monday, 4:00 p.m.</strong> Mr. Junel &ldquo;Mang Jun&rdquo; Ramos, 52, a former construction foreman, has been on hemodialysis for a year (Tuesday, Thursday, Saturday mornings). He wants to return to light work in his cousin&rsquo;s hardware store, which means standing for hours and lifting boxes of nails and paint of up to 10 kilograms.</p>
<p>His baseline: five-times sit-to-stand 15.8 seconds, six-minute walk 380 meters, SPPB 9. He takes carvedilol. His nephrologist has set exercise parameters on the unit sheet and written &ldquo;cleared for moderate exercise; avoid fistula-arm loading; review if dizziness.&rdquo; Mang Jun says, &ldquo;Give me heavy work. I used to carry cement.&rdquo;</p>
""", "questions": ["What would you prescribe for weeks 1 to 4, using FITT-VP?",
                  "How will you set intensity, given carvedilol?",
                  "How do you progress to the 10-kilogram lift safely, and what would make you pause?"]},
    "sections": [
        ("evidence", "What exercise does", "The evidence: what changes, and how sure we are", """
<p>A Cochrane review of 45 randomized trials (1,863 participants) found that regular exercise in adults with CKD improved aerobic capacity (standardized mean difference &minus;0.56, favoring exercise), walking capacity, resting blood pressure, heart rate and health-related quality of life. Seventeen percent of trials had low risk of bias and 49 percent high, and most outcomes were measured over months, not years.[[otpt_heiwe2011]] Since then, larger trials have refined the picture (Module 10): long, supervised, combined training improved function; short, poorly attended programs did not.</p>
<p>What exercise has not shown is a reduction in death or kidney failure in a randomized trial. The physiological benefits are well established; the hard-outcome benefits are not yet proven. Say so honestly, then point to what patients feel: easier stairs, longer walks, less fatigue.</p>
{{key:Exercise in CKD improves fitness and function; it has not been shown to prolong life. Both statements are true, and patients deserve both.}}
"""),
        ("prescription", "Writing the prescription", "FITT-VP for a person on dialysis", """
{{fig:otpt09_fitt}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>Aerobic</th><th>Resistance</th></tr></thead>
<tbody>
<tr><td>Frequency</td><td>Most days, building toward the KDIGO aim of 150 minutes a week as tolerated</td><td>Two to three non-consecutive days a week is common practice</td></tr>
<tr><td>Intensity</td><td>Moderate: RPE 12 to 14, able to talk but not sing</td><td>A load the person can lift 10 to 15 times with good form, stopping one or two short of failure</td></tr>
<tr><td>Time</td><td>Start with what the person can do (even 5 to 10 minutes), in bouts if needed</td><td>One to two sets per exercise to start</td></tr>
<tr><td>Type</td><td>Walking, stationary or pedal cycling, step-ups</td><td>Sit-to-stand, step-ups, bands, ankle weights, wall push-ups; large leg muscles first</td></tr>
<tr><td>Volume</td><td>Minutes per week</td><td>Sets &times; repetitions &times; load</td></tr>
<tr><td>Progression</td><td>Time first, then intensity</td><td>Repetitions first, then load</td></tr>
</tbody></table></div>
<p><strong>Why effort, not heart rate.</strong> Beta-blockers such as carvedilol and metoprolol blunt the heart-rate response, and autonomic neuropathy does the same. A heart-rate target calculated from age may be unreachable or misleading. The Borg RPE and the talk test work regardless. If you use the site&rsquo;s <a href="calc-exercise-hr-zones.html">heart-rate zones calculator</a>, treat it as a cross-check in people not on rate-limiting drugs, never as the only guide.</p>
<p><strong>Dialysis-week rules.</strong> Plan the harder sessions on non-dialysis days or early in a session (Module 10). Keep the access arm free of loads unless the nurse and nephrologist approve. Hydration advice comes from the fluid plan, not from general sports advice.</p>
{{key:Start where the person is, set intensity by effort, progress time before intensity and repetitions before load.}}
"""),
        ("worked", "Worked plan", "Worked example: twelve weeks for Mang Jun", """
{{formula:<strong>Illustrative plan (non-dialysis days Mon, Wed, Fri; carvedilol, so RPE-based).</strong><br><strong>Weeks 1&ndash;4.</strong> Aerobic: walk 15 minutes at RPE 12 to 13 on Mon, Wed, Fri, plus 10 minutes on Sunday (55 minutes a week). Resistance (Mon, Fri): sit-to-stand 2 &times; 10; step-ups on a 15-centimeter step 2 &times; 10 each leg; band rows with the non-fistula arm 2 &times; 12; wall push-ups 2 &times; 10; ankle-weight knee extensions 1 kilogram 2 &times; 12.<br><strong>Weeks 5&ndash;8.</strong> Walk 20 to 25 minutes, RPE 13 (about 90 minutes a week). Add a third resistance day; sit-to-stand holding a 3-kilogram bag close to the body; step height 20 centimeters.<br><strong>Weeks 9&ndash;12.</strong> Walk 30 minutes on 5 days (150 minutes, RPE 13 to 14). Task practice: lift a box from a waist-height shelf to a table, 5 kilograms progressing to 10, held close, no twisting, both hands (fistula arm only if the nephrologist approves).<br><strong>Review at week 12:</strong> five-times sit-to-stand, six-minute walk, SPPB, and a simulated store task.}}
<p>The weekly activity tool in the <a href="calc-renal-rehabilitation-toolkit.html#tool-5">Renal Rehabilitation Toolkit</a> tracks his minutes against the 150-minute aim, and the <a href="calc-physical-activity-met.html">metabolic equivalent of task (MET) calculator</a> converts mixed activities into MET-minutes.</p>
{{scene:The missed week|<p>In week 6, Mang Jun is admitted for three days with a catheter-unrelated infection and misses five sessions. When he returns, PT Carlo Dizon does not restart at week 6. He screens, obtains a restart authorization from the nephrologist, and goes back to the week 3 level for one week before resuming progression.</p><p class="tc-scene-take">After illness, drop back, then build again. The savings account lost some balance; it did not close.</p>}}
{{call:Pause exercise and ask the physician to review if there is new chest pain, fainting, increasing breathlessness, new swelling or rapid weight gain, a new arrhythmia, an access problem, a fever or acute illness, or a hospital stay. Restart only with a documented authorization (Module 3).}}
"""),
    ],
    "debrief": ["""
<p><strong>Weeks 1 to 4.</strong> Moderate walking on non-dialysis days, building from about 55 minutes a week, plus two days of resistance work centered on the legs, one or two sets of 10 to 15 repetitions, with the fistula arm unloaded. Mang Jun&rsquo;s eagerness is welcome, but early overload risks injury and discouragement; Carlo explains that weeks 1 to 4 build the nervous-system gains that make heavier work safe later.</p>
<p><strong>Intensity.</strong> Carvedilol blunts heart rate, so Carlo uses RPE 12 to 14 and the talk test, and writes that in the plan.</p>
<p><strong>Progression and pauses.</strong> Time, then intensity for aerobic work; repetitions, then load for strength; task-specific lifting practice from week 9, held close without twisting. Pause for red-flag symptoms, illness or hospitalization, and restart only with authorization, dropping back to an earlier level.</p>
"""],
    "skills": {"title": "Exercise prescription and progression",
               "intro": "Write and teach a 12-week prescription for a simulated patient while your preceptor observes.",
               "items": [
                   ("Confirms the physician&rsquo;s parameters and restrictions and the access side before prescribing.", True),
                   ("Writes all FITT-VP elements for aerobic and resistance work.", False),
                   ("Sets intensity by RPE and talk test for a patient on a rate-limiting drug, and explains why.", True),
                   ("Teaches each exercise with correct form and an access-safe set-up.", True),
                   ("Places sessions sensibly in the dialysis week.", False),
                   ("States progression rules and the drop-back rule after missed sessions or illness.", False),
                   ("States the pause-and-review triggers.", True),
               ],
               "placement": "Prescribe and follow one patient for four weeks; log minutes, RPE and any pauses, and review progression with your preceptor."},
    "terms": [("RPE", "How hard work feels, 6 to 20 Borg scale."), ("Talk test", "Moderate intensity: can talk but not sing."),
              ("Progression", "A planned increase in time, load or difficulty."), ("Drop-back rule", "After a break, restart at an earlier level.")],
    "readings": [("exercise-guide-ckd.html", "The patient guide to exercise in CKD."),
                 ("physical-activity-sports-ckd.html", "Activity and sports with kidney disease.")],
    "calcs": ["calc-exercise-hr-zones.html", "calc-physical-activity-met.html", "calc-renal-rehabilitation-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["09"])
