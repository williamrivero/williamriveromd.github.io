# -*- coding: utf-8 -*-
"""OT/PT track, Module 05: Assess Function and Agree Measurable Goals. Written for this series from published sources."""

MODULE = {
    "image_alt": "A therapist timing a patient's walk along a taped four-meter course in a bright corridor.",
    "objectives": [
        "Explain why performance measures add information that self-report and laboratory tests do not.",
        "Administer and score gait speed, the five-times sit-to-stand, the Short Physical Performance Battery and the six-minute walk test in a standard way.",
        "Calculate percent-predicted six-minute walk distance and interpret it with its limits.",
        "Combine performance results with an occupational interview to build a functional problem list.",
        "Write shared, measurable goals in the patient&rsquo;s own words, with a review date.",
    ],
    "big": """
{{plain:A bathroom scale only helps if you stand on the same scale, at the same time of day, in the same clothes. Change any of those and the number moves for reasons that have nothing to do with your weight.}}
<p>The picture has a limit. A scale measures one thing. Function has many parts, and a person can improve in one and decline in another. So you choose a small battery that covers the parts that matter for this person, and you run it the same way every time: same chair height, same course length, same instructions, same point in the dialysis week. Without standard conditions, a change in the number means nothing.</p>
<p>Why bother measuring at all, when you can see that a patient is weak? Because performance tests carry information that neither the patient&rsquo;s report nor the chart gives. In the study that built the Short Physical Performance Battery (SPPB), performance scores still separated people by later risk of death and nursing-home admission even among those who reported almost no disability.[[otpt_guralnik1994]] In a pooled analysis of 34,485 older adults, each 0.1 meter per second of gait speed was associated with lower mortality (hazard ratio 0.88).[[otpt_studenski2011]] In CKD, gait speed predicted three-year mortality better than kidney function did.[[otpt_roshanravan2013]] These are associations; they tell you what to watch, not that raising the number will change survival.</p>
{{fig:otpt05_battery}}
{{cards:Key terms for this module|Performance measure::A timed or counted test the person does in front of you.|Self-report::What the person says they can do; useful, but different.|Standard conditions::The same equipment, instructions and timing every time.|Percent predicted::A result compared with healthy people of the same age, sex and size.|Shared goal::A change the person wants, written so you both can tell when it is met.}}
""",
    "case": {"title": "A baseline for Mr. Villanueva", "html": """
<p><strong>Thursday, 9:00 a.m., a non-dialysis day.</strong> With parameters from Dr. Uy in the chart, PT Carlo Dizon and OT Bea Santiago assess Mr. Ernesto Villanueva, 64, height 165 centimeters, dry weight 68 kilograms.</p>
<p>Carlo&rsquo;s results: 4-meter usual walk 5.9 seconds; side-by-side and semi-tandem stands held 10 seconds each, tandem held 4 seconds; five chair rises (arms crossed, standard 46-centimeter chair) 17.5 seconds; six-minute walk 290 meters with one standing rest. Bea&rsquo;s interview: he wants to watch his grandson&rsquo;s weekend basketball games at the barangay court, about 250 meters from home, and to bathe himself again.</p>
""", "questions": ["What are his gait speed, SPPB score and percent-predicted six-minute walk distance?",
                  "What do these numbers mean for the goals he named?",
                  "Write two shared goals, one led by each profession."]},
    "sections": [
        ("battery", "The battery", "A practical baseline battery", """
<p>Choose tests that fit the person, the space you have, and the question. For most adults on dialysis who can walk, four tests cover the main accounts.</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>How</th><th>What it reflects</th></tr></thead>
<tbody>
<tr><td>Gait speed</td><td>Usual pace over 4 meters, timed from a standing start (or with a short run-in, but always the same way)</td><td>Overall mobility; a strong prognostic signal</td></tr>
<tr><td>Five-times sit-to-stand</td><td>Five full rises from a standard chair, arms crossed, timed</td><td>Leg strength and power</td></tr>
<tr><td>SPPB</td><td>Three balance stands, the 4-meter walk, and five chair rises, each scored 0 to 4; total 0 to 12</td><td>Lower-limb function across balance, gait and strength</td></tr>
<tr><td>Six-minute walk test (6MWT)</td><td>Walk as far as possible in 6 minutes on a flat measured course with standard encouragement; rests allowed, clock keeps running</td><td>Functional endurance</td></tr>
<tr><td>60-second sit-to-stand (STS60)</td><td>Full rises in one minute</td><td>Leg endurance and strength; the main outcome of the largest dialysis exercise trial</td></tr>
</tbody></table></div>
<p>If the person cannot walk, use transfers, sitting balance and a task observation instead. Never test in the hours after a session with a large fluid removal unless the purpose is to measure that.</p>
{{key:Same chair, same course, same words, same day of the dialysis week. Write the conditions next to the number.}}
"""),
        ("numbers", "Working the numbers", "Worked example: turning times into meaning", """
<p>Here is how Carlo turns Mr. Villanueva&rsquo;s times into results he can track and explain.</p>
{{formula:<strong>Gait speed.</strong> 4 meters &divide; 5.9 seconds = <strong>0.68 m/s</strong>.<br><strong>SPPB (widely used 4-meter scoring).</strong> Balance: side-by-side 10 s (1) + semi-tandem 10 s (1) + tandem 4 s (1) = 3. Gait: 5.9 s = 3 points (4.82 to 6.20 s). Chair stands: 17.5 s = 1 point (16.70 s or longer). Total <strong>7 of 12</strong>.<br><strong>Six-minute walk, percent predicted.</strong> The Enright&ndash;Sherrill equation for men: (7.57 &times; height cm) &minus; (5.02 &times; age) &minus; (1.76 &times; weight kg) &minus; 309.[[otpt_enright1998]] = (7.57 &times; 165) &minus; (5.02 &times; 64) &minus; (1.76 &times; 68) &minus; 309 = 1,249 &minus; 321 &minus; 120 &minus; 309 &asymp; <strong>499 m predicted</strong>. He walked 290 m: 290 &divide; 499 &asymp; <strong>58 percent of predicted</strong>.}}
<p>The <a href="calc-renal-rehabilitation-toolkit.html">Renal Rehabilitation Toolkit</a> does these calculations. Use the numbers with their limits. The Enright&ndash;Sherrill equations came from healthy American adults aged 40 to 80; they are a reference point, not a Filipino norm, so the most useful comparison is with the person&rsquo;s own baseline. The SPPB cut points come from older community-dwelling adults.</p>
{{fig:otpt05_gait_speed}}
<p>What do the numbers mean for his goals? A gait speed of 0.68 m/s and 290 meters in six minutes with a rest suggest that walking 250 meters to the court, then standing or sitting on bleachers, is near the edge of what he can do now. The chair-stand time tells Carlo that leg strength, not only endurance, is limiting; that matters for rising from bleachers and from a low toilet.</p>
{{key:Every number earns its place by answering a question about a goal the person cares about.}}
"""),
        ("occupation", "The occupational picture", "Adding the occupational picture", """
<p>Performance tests describe the body. They do not tell you which tasks matter, how the person does them now, or what the setting demands. The OT adds that picture through an interview about roles and routines and through observing a real task.</p>
<p>For Mr. Villanueva, Bea asks him to talk through a bathing day: where the bathroom is, whether there is a step, whether he sits or stands, how warm the water is, how long it takes, and when in the dialysis week he bathes. She learns that he bathes standing, with a <em>tabo</em> and pail, in a bathroom with a 15-centimeter step and no rail, usually right after he comes home from dialysis. That one interview reveals three targets: the timing (after fluid removal), the posture (standing, with dizziness), and the environment (a step without a rail).</p>
{{key:Ask the person to walk you through the task, step by step, in their own setting. The problem is often in the sequence, not the muscles.}}
"""),
        ("goals", "Shared goals", "Goals the person chose, written so you can tell when they are met", """
<p>A useful goal states what the person will do, in what setting, with what help, by when, in words they would recognize as their own. SMART goals (specific, measurable, achievable, relevant and time-bound) are one format; the essentials are that the patient chose it and that you will both know when it is met.</p>
{{formula:<strong>Illustrative shared goals for Mr. Villanueva (review in 8 weeks).</strong><br>PT-led: &ldquo;Walk to the barangay court (250 m) with no more than one short rest, and rise from the bleachers without help, in time for the league finals.&rdquo; Measures: 6MWT, five-times sit-to-stand, gait speed.<br>OT-led: &ldquo;Bathe myself seated, on non-dialysis evenings, with my wife nearby but not helping.&rdquo; Measures: observed bathing task, assistance level, dizziness episodes logged.}}
<p>Agree the goals with the patient and family, share them with the renal team, and record the review date. Goals are reassessed, not abandoned, when a bad week or a hospital stay interrupts progress.</p>
{{key:A goal that the patient did not choose is your goal, not theirs. Ask what they want back.}}
"""),
    ],
    "debrief": ["""
<p><strong>The numbers.</strong> Gait speed 0.68 m/s; SPPB 7 of 12 (balance 3, gait 3, chair stands 1); predicted six-minute walk about 499 meters, so 290 meters is about 58 percent of predicted.</p>
<p><strong>What they mean.</strong> He has moderate lower-limb impairment, with leg strength the weakest component and endurance limited. Walking 250 meters and rising from bleachers are realistic but currently near his limit. Because of his neuropathy and earlier fracture, the tandem stand needed close guarding.</p>
<p><strong>Two shared goals.</strong> As written above: a PT-led walking and bleacher-rise goal, and an OT-led seated bathing goal timed for non-dialysis evenings. Both are reviewed in eight weeks using the same tests under the same conditions.</p>
"""],
    "skills": {"title": "Baseline battery and goal setting",
               "intro": "Administer a baseline battery to a colleague or a consenting patient, then agree two goals while your preceptor observes.",
               "items": [
                   ("Completes the pre-session screen and confirms the test day and timing relative to dialysis.", True),
                   ("Sets up standard conditions: chair height, measured course, standard instructions.", False),
                   ("Guards closely during balance and walking tests, protecting the access arm.", True),
                   ("Scores gait speed, five-times sit-to-stand and SPPB correctly.", False),
                   ("Calculates percent-predicted six-minute walk distance and states the equation&rsquo;s limits.", False),
                   ("Obtains the occupational picture through interview or task observation (OT) or reviews the OT findings (PT).", False),
                   ("Writes two shared, measurable goals with the patient, with a review date.", False),
               ],
               "placement": "Complete baselines for three patients and repeat one test on two separate days under the same conditions to see how much the result varies without any real change."},
    "terms": [("Gait speed", "Distance walked divided by time, in meters per second."),
              ("SPPB", "A 0 to 12 score from balance, walking and chair rises."),
              ("Percent predicted", "A result compared with a reference population."),
              ("Shared goal", "A goal the patient chose, written so it can be checked.")],
    "readings": [("exercise-guide-ckd.html", "How patients are told about exercise testing and progress."),
                 ("hemodialysis-elderly.html", "Older adults on dialysis and the value of function.")],
    "calcs": ["calc-renal-rehabilitation-toolkit.html#tool-1", "calc-renal-rehabilitation-toolkit.html#tool-2",
              "calc-renal-rehabilitation-toolkit.html#tool-3"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
