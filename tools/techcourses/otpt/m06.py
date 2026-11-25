# -*- coding: utf-8 -*-
"""OT/PT track, Module 06: Manage Fatigue and Rebuild Daily Routines. Written for this series from published sources."""

MODULE = {
    "image_alt": "An occupational therapist and a middle-aged woman planning a week on a large paper calendar at a kitchen table.",
    "objectives": [
        "Explain the main contributors to fatigue in kidney failure and why it worsens after dialysis sessions.",
        "Ask about and record post-dialysis recovery time, and explain what it is associated with.",
        "Describe the deconditioning spiral and how pacing and graded activity interrupt it.",
        "Build an energy budget for a dialysis week that protects the activities the person values most.",
        "Recognize fatigue patterns that need medical review rather than a pacing plan.",
    ],
    "big": """
{{plain:Think of energy as a phone battery. A healthy person starts the day at 100 percent and charges overnight. A person on hemodialysis starts at 60 percent, loses a large chunk during a session, and charges slowly. If they spend the morning&rsquo;s charge on chores, there is nothing left for the evening with the grandchildren.}}
<p>The picture has a limit. A phone battery only drains. Human energy also grows with use: muscles that work become more efficient, and a heart that is trained delivers oxygen better. Resting all the time keeps the battery small. So the answer to fatigue is not simply rest; it is planned rest and planned activity, spent on what matters, with capacity built up over weeks.</p>
<p>Fatigue is the most common symptom in dialysis. A systematic review of 59 studies found a weighted average prevalence of 71 percent for fatigue, ahead of itch, pain and sleep problems.[[murtagh2007]] It is also what patients most want addressed. The OT leads this module, but the PT shapes the capacity side of the plan.</p>
{{fig:otpt06_energy}}
{{cards:Key terms for this module|Recovery time::How long after a dialysis session the person feels back to their usual self.|Deconditioning spiral::Fatigue leads to rest, rest to weakness, weakness to more fatigue.|Pacing::Spreading effort through the day and week, with planned rests before exhaustion.|Energy budget::A plan that places valued activities where energy is highest.|Graded activity::A slow, planned increase in activity over weeks.}}
""",
    "case": {"title": "Aling Rosa&rsquo;s Mondays", "html": """
<p><strong>Friday, 3:00 p.m.</strong> Aling Rosa Mendoza, 57, a former market vendor, has been on hemodialysis Monday, Wednesday and Friday mornings for three years. She tells OT Bea Santiago: &ldquo;On dialysis days I am useless. I sleep all afternoon. On the other days I try to do everything: laundry, the market, cooking for the week. By Sunday I am exhausted, and Monday is the worst.&rdquo;</p>
<p>She looks after two grandchildren after school. She used to sing in her parish choir on Thursday evenings and stopped a year ago. She says it takes her &ldquo;until night&rdquo; to recover after a session.</p>
""", "questions": ["What is driving her fatigue, and which parts need a medical review?",
                  "What does her recovery time tell you?",
                  "Sketch an energy budget for her week that brings back one valued activity."]},
    "sections": [
        ("why-tired", "Why so tired", "The physiology of fatigue in kidney failure", """
<p>Fatigue in kidney failure has many sources, and most patients have several at once.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>How it causes fatigue</th><th>Whose job</th></tr></thead>
<tbody>
<tr><td>Anemia</td><td>Less oxygen to muscle and brain</td><td>Renal team</td></tr>
<tr><td>Uremia and underdialysis</td><td>Retained toxins affect muscle and brain</td><td>Renal team</td></tr>
<tr><td>The session itself</td><td>Rapid fluid and solute shifts, falls in blood pressure, a long sitting period</td><td>Renal team; you report patterns</td></tr>
<tr><td>Depression and poor sleep</td><td>Low energy and motivation; broken nights</td><td>Shared; screen and refer (Module 16)</td></tr>
<tr><td>Deconditioning</td><td>Weaker muscles and heart need more effort for each task</td><td>Rehabilitation</td></tr>
<tr><td>Inefficient routines</td><td>Tasks done standing, in heat, all at once, at the wrong time</td><td>Rehabilitation (OT)</td></tr>
</tbody></table></div>
<p>The last two are where you make the difference. But a pacing plan that ignores untreated anemia or depression will fail, so share what you find with the renal team.</p>
{{key:Ask what else could be causing the fatigue before you plan around it. Rehabilitation treats the part that is deconditioning and routine.}}
"""),
        ("recovery", "Recovery time", "Recovery time: a question with outcome data", """
<p>Ask every patient: &ldquo;After a dialysis session, how long does it take you to feel like yourself again?&rdquo; In the international Dialysis Outcomes and Practice Patterns Study (DOPPS), about one patient in ten needed more than 12 hours to recover after a session. Longer recovery was associated with greater weight loss during dialysis, with hospital admission and with death.[[hn_rayner2014]] The study was observational, so recovery time is a marker of risk, not proof of cause. But a long or lengthening recovery time is worth reporting to the nephrologist, because fluid removal and session length can sometimes be adjusted.</p>
<p>Recovery time also tells you where energy is in the week. For Aling Rosa, &ldquo;until night&rdquo; means dialysis days are lost after noon, so the plan must use non-dialysis days well rather than cram them.</p>
{{key:Record recovery time at baseline and review. A change is information for the whole team.}}
"""),
        ("pacing", "Pacing and graded activity", "Breaking the spiral", """
<p>The deconditioning spiral runs like this: fatigue leads to rest; rest leads to weaker muscles; weaker muscles make every task cost more; tasks feel harder, so the person rests more. Breaking it needs two moves at once. The OT reduces the cost of tasks so the person has energy left; the PT builds capacity slowly so the same task costs less over time.</p>
<p>The OT&rsquo;s pacing tools are simple and powerful:</p>
<ul>
<li><strong>Prioritize:</strong> which activities matter most? Protect those first.</li>
<li><strong>Plan:</strong> spread heavy tasks across the week instead of one exhausting day.</li>
<li><strong>Position:</strong> sit for tasks that can be done sitting (preparing vegetables, ironing, bathing).</li>
<li><strong>Pace:</strong> rest before exhaustion, not after; break tasks into parts.</li>
<li><strong>Simplify:</strong> fewer steps, tools within reach, help for the heaviest part.</li>
</ul>
<p>On the capacity side, structured exercise improves fitness in CKD. A Cochrane review of 45 randomized trials found that regular exercise improved aerobic capacity, walking capacity and health-related quality of life, although many trials were small and half had a high risk of bias.[[otpt_heiwe2011]] In the EXCITE trial, a simple home walking program managed by dialysis staff improved the six-minute walk (328 to 367 meters versus no change in controls) and improved the cognitive function and social interaction scores of a kidney-specific quality-of-life questionnaire.[[otpt_manfredini2017]]</p>
{{key:Rest that is planned restores. Rest that is the only activity shrinks the battery.}}
"""),
        ("budget", "The energy budget", "Worked example: an energy budget for a dialysis week", """
{{formula:<strong>Illustrative energy budget for Aling Rosa (agreed with her).</strong><br><strong>Monday, Wednesday, Friday (dialysis mornings):</strong> light lunch, then a planned 1-hour rest; no chores; grandchildren for homework only, seated; early night.<br><strong>Tuesday:</strong> laundry split in two loads (morning and late afternoon), seated sorting; 10-minute walk with Carlo&rsquo;s plan.<br><strong>Thursday:</strong> light morning; rest after lunch; <strong>choir practice in the evening</strong>, with a chair available.<br><strong>Saturday:</strong> market with her daughter carrying the bags; cooking two dishes, seated preparation.<br><strong>Sunday:</strong> Mass, family, rest; no batch cooking.<br>Review in four weeks: recovery time, number of exhausted days, and whether she went to choir.}}
<p>The choir goes on Thursday because it follows a non-dialysis day and precedes another, the point in her week when the battery is fullest. The heavy cooking is spread across Saturday and helped by her daughter. Dialysis days are protected rather than wasted: a planned rest, then a valued, light role with the grandchildren.</p>
<p>The <a href="calc-renal-rehabilitation-toolkit.html#tool-5">weekly activity tool</a> in the toolkit helps you track minutes of planned activity alongside the budget, so you can see capacity work growing week by week.</p>
{{key:Put the activity the person values most where their energy is highest, and protect it.}}
"""),
    ],
    "debrief": ["""
<p><strong>What drives her fatigue.</strong> Likely contributors include the sessions themselves (a long recovery time), the boom-and-bust pattern on non-dialysis days, deconditioning, and possibly anemia, poor sleep or low mood after stopping choir. Bea shares the recovery time and the mood change with the nurse and nephrologist, and asks whether her anemia and dialysis adequacy have been reviewed recently; a depression screen may be appropriate (Module 16).</p>
<p><strong>Her recovery time.</strong> Recovering &ldquo;until night&rdquo; places her in the group with long recovery, which in DOPPS was associated with worse outcomes. It is worth reporting, and it tells Bea that dialysis afternoons should hold no demanding tasks.</p>
<p><strong>An energy budget.</strong> As above: spread the chores, sit for preparation, protect dialysis afternoons for rest, and place choir on Thursday evening. Carlo adds a short walking program on non-dialysis days. They review recovery time, exhausted days and choir attendance in four weeks.</p>
"""],
    "skills": {"title": "Fatigue assessment and energy budget",
               "intro": "Interview a simulated patient about fatigue and build an energy budget with them while your preceptor observes.",
               "items": [
                   ("Asks about recovery time after dialysis, daily pattern of fatigue, sleep, mood and valued activities.", False),
                   ("Identifies possible medical contributors and reports them to the renal team instead of treating them.", True),
                   ("Identifies the boom-and-bust pattern and explains the deconditioning spiral in plain language.", False),
                   ("Builds a weekly energy budget that places a valued activity at a high-energy point.", False),
                   ("Applies at least three pacing strategies to the person&rsquo;s actual tasks.", False),
                   ("Agrees a review date and two measures (for example, recovery time and number of exhausted days).", False),
               ],
               "placement": "For two patients, record recovery time and a one-week activity diary, then build and review an energy budget with each."},
    "terms": [("Recovery time", "Hours after a session until the person feels usual."),
              ("Deconditioning", "Loss of fitness from inactivity."), ("Pacing", "Planned spreading of effort with rests before exhaustion."),
              ("Boom and bust", "Overdoing on good days, then crashing.")],
    "readings": [("post-dialysis-fatigue.html", "Post-dialysis fatigue explained for patients."),
                 ("ckd-mental-health-sleep.html", "Mood and sleep in kidney disease.")],
    "calcs": ["calc-renal-rehabilitation-toolkit.html#tool-5", "calc-physical-activity-met.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
