# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 10: Distress, Depression, Anxiety, and Stepped Support. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker sitting beside a man in a dialysis chair, listening closely, a nurse in the background.",
    "objectives": [
        "State how common depression is among people on dialysis, and why rating scales give higher numbers than clinical interviews.",
        "Screen in two steps (the two PHQ-2 questions, then the PHQ-9) and interpret the score in light of symptoms that kidney failure also causes.",
        "Describe what the evidence shows for talking therapies, exercise, and antidepressants in dialysis, and how strong it is.",
        "Match support to need using stepped care, from listening and practical help to referral to the mental health team.",
        "Keep the safety question (PHQ-9 item 9) open at every step, and act on any positive answer.",
    ],
    "big": """
{{plain:Distress in kidney failure is like water in the hull of a boat. A little is normal on any voyage and you bail it out with ordinary effort: a good conversation, a solved fare problem, a friend in the next chair. When the water keeps rising despite bailing, something has opened below the waterline, and the crew needs help from someone with the right tools.}}
{{fig:sw10_stepped}}
<p>The picture has a limit. In a boat, water is water. In kidney failure, the body itself produces some of what looks like depression: uremia, anemia, poor sleep from itch or breathlessness, and medicines can cause tiredness, poor appetite, and poor concentration. Grief over lost work and roles is normal and is not an illness. And sometimes what looks like low mood is a clear-eyed view of a hard situation. So your task is not to decide who is &ldquo;depressed.&rdquo; It is to notice, to screen honestly, to support, and to make sure the people who can diagnose and treat get involved when the water keeps rising.</p>
<p>Depression matters because it is common, because people suffer from it, and because it travels with other harms. By clinical interview, about one in five people on dialysis has depression; rating scales give higher numbers.[[palmer2013]] The DOPPS cohort linked depressive symptoms to missed treatments.[[alsalmi2018]] Suicide is rare in absolute terms but more frequent than in the general population.[[kurella2005]]</p>
{{cards:Key terms for this module|Depression::Persistent low mood or loss of interest, with changes in sleep, appetite, energy, or thinking, for at least two weeks; diagnosed by a clinician.|Distress::Emotional suffering of any kind; common and often a normal response to loss.|PHQ-2::The first two questions of the PHQ-9 (interest and mood), used as a quick first screen.|PHQ-9::Nine questions on the past two weeks, each scored 0 to 3, total 0 to 27. A screen, not a diagnosis.|Item 9::The PHQ-9 question about thoughts of being better off dead or of self-harm. Any positive answer starts the safety pathway.|Stepped care::Matching the intensity of support to the level of need, and stepping up when needed.}}
""",
    "case": {"title": "Mang Romeo&rsquo;s PHQ-9 of 16", "html": """
<p>Monday, 10:00 a.m., hour one of his session. Mr. Romeo Dizon, 58, on hemodialysis for three years, tells the nurse he &ldquo;does not see the point anymore&rdquo; and wants to talk to someone. He missed last Wednesday&rsquo;s session.</p>
<p>You sit with him. He describes weeks of waking at 3:00 a.m. with worry, no appetite, and no interest in the chess games he used to play with other patients. His wife, Aling Nena, stopped selling at the market to bring him to dialysis, and the household income has halved. He feels he has become a burden.</p>
<p>With his agreement you complete the PHQ-9 together. His item scores are: interest 2, mood 2, sleep 3, energy 3, appetite 2, feeling a failure 2, concentration 1, slowness 1, item 9 (thoughts of being better off dead or self-harm) 0.</p>
""", "questions": ["What is his total, and what does it mean and not mean?",
                  "What would you say to the attending nephrologist, and what would you offer him?",
                  "What else do you notice that needs attention?"]},
    "sections": [
        ("common", "How common, and how it looks", "Numbers and overlap", """
<p>Palmer and colleagues pooled 249 study populations with 55,982 participants. By clinical interview, depression affected 22.8% of patients on dialysis; by rating scales, 39.3%. The authors concluded that scales may overestimate depression in dialysis.[[palmer2013]] Both figures come from observational studies of varying quality. The gap between them is the overlap problem: kidney failure itself causes many symptoms the scales count.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Also caused by</th><th>Leans toward depression when&hellip;</th></tr></thead>
<tbody>
<tr><td>Tiredness, low energy</td><td>Anemia, uremia, post-dialysis fatigue</td><td>It comes with loss of interest and hopelessness</td></tr>
<tr><td>Poor sleep</td><td>Itch, restless legs, breathlessness, pain</td><td>The person wakes early with worry or sadness</td></tr>
<tr><td>Poor appetite</td><td>Uremia, nausea, diet restrictions</td><td>Food stops giving any pleasure at all</td></tr>
<tr><td>Poor concentration</td><td>Uremia, medicines, sleep loss</td><td>It comes with guilt and feeling a failure</td></tr>
</tbody></table></div>
<p>Anxiety is common too: worry about money, the next session, needles, the future. It often travels with depression and responds to the same practical and talking support.</p>
{{key:Many symptoms of kidney failure look like depression. Loss of interest, low mood, guilt, and hopelessness are the parts the kidneys do not explain.}}
"""),
        ("screen", "Screening honestly", "Two steps, and item 9 every time", """
<p>Screen in two steps. First the two questions of the Patient Health Questionnaire-2 (PHQ-2): over the last two weeks, how often have you been bothered by little interest or pleasure in doing things, and by feeling down, depressed, or hopeless? If either answer is positive, complete the full Patient Health Questionnaire-9 (PHQ-9) with the person.</p>
{{fig:sw10b_two_step}}
<p>The PHQ-9 was validated in 6,000 primary care and obstetric patients: a score of 10 or more had sensitivity and specificity of 88% for major depression, and scores of 5, 10, 15, and 20 marked mild, moderate, moderately severe, and severe.[[kroenke2001]] In 62 patients on dialysis compared with a structured psychiatric interview, a score of 10 or more had sensitivity 92%, specificity 92%, positive predictive value 71%, and negative predictive value 98%.[[watnick2005]] The dialysis study was small and single-center. A negative screen is reassuring; a positive screen means &ldquo;look closer&rdquo;: about three in ten positives did not have depression on interview.</p>
<div class="table-wrap"><table>
<thead><tr><th>PHQ-9 total</th><th>Band (primary care)</th><th>Dialysis caveat</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>0&ndash;4</td><td>Minimal</td><td>&mdash;</td><td>Record; rescreen at the agreed interval</td></tr>
<tr><td>5&ndash;9</td><td>Mild</td><td>Points may come from uremic symptoms</td><td>Support, practical help, rescreen in a month</td></tr>
<tr><td>10&ndash;14</td><td>Moderate</td><td>Check which items carry the score</td><td>Tell the nephrologist; offer structured support or referral</td></tr>
<tr><td>15&ndash;19</td><td>Moderately severe</td><td>Usually more than kidney symptoms</td><td>Tell the nephrologist today; referral to the mental health team</td></tr>
<tr><td>20&ndash;27</td><td>Severe</td><td>&mdash;</td><td>Same day: nephrologist and urgent mental health review</td></tr>
<tr><td>Item 9 any answer above 0</td><td>&mdash;</td><td>&mdash;</td><td>Safety pathway now, whatever the total (Module 11)</td></tr>
</tbody></table></div>
<p>The bands come from primary care.[[kroenke2001]] The dialysis caveat is reasoning from shared symptoms, not a tested correction. The site&rsquo;s <a href="calc-phq9.html">PHQ-9 calculator</a> adds the items. A score is never a diagnosis; diagnosis belongs to the mental health clinician.</p>
{{formula:<strong>Worked example, illustrative.</strong> PHQ-9 total = sum of nine items, each 0 to 3.[[kroenke2001]]<br>Interest 2 + mood 2 + sleep 3 + energy 3 + appetite 2 + feeling a failure 2 + concentration 1 + slowness 1 + item 9 0 = 16.<br>Above the dialysis-validated cutoff of 10.[[watnick2005]] Sleep, energy, and appetite (8 of the 16 points) overlap uremic symptoms; interest, mood, and feeling a failure (6 points) do not.<br>What the number tells you: depression is likely enough to report and refer. What it does not tell you: the diagnosis, the cause, or the treatment.}}
{{key:Ask item 9 in person, every time, whatever the total. A positive answer starts the safety pathway now.}}
"""),
        ("helps", "What helps, and how well", "Talking, moving, medicine", """
<p>Know the evidence well enough to offer options honestly and to answer &ldquo;Will it help?&rdquo;</p>
{{cards:What the studies tested and found|Talking therapy (CBT)::A Cochrane review of psychosocial interventions in dialysis found that cognitive behavioral therapy (CBT) probably improves depressive symptoms (Beck Depression Inventory, 4 studies, 230 participants, mean difference &minus;6.10 points) and quality of life, with moderate-certainty evidence.[[sw_natale2019]]|Counseling::Counseling may slightly reduce depressive symptoms (3 studies, 99 participants, mean difference &minus;3.84 points); low-certainty evidence.[[sw_natale2019]]|Exercise::Exercise may reduce major depression (3 studies, 108 participants, risk ratio 0.47); low certainty.[[sw_natale2019]]|Chairside CBT trial::A randomized crossover trial of 65 patients at two centers found benefit from CBT delivered during dialysis.[[cukor2014]]|Sertraline versus CBT (ASCEND)::120 patients, 41 United States units, 12 weeks, open label. Clinician-rated scores were modestly lower with sertraline, with more side effects; there was no placebo group.[[mehrotra2019]]|Antidepressant versus placebo::Few, small trials; benefit in dialysis is uncertain.[[palmer_cochrane2016]][[friedli2017]]}}
<p>All these outcomes are rating-scale scores, surrogates for how a person feels and functions. None of these studies was designed to show an effect on survival, hospital stays, or suicide. What they do support is that talking therapies, counseling, and exercise are reasonable to offer and that medicine is an option for the mental health team and nephrologist to weigh. Medicine decisions are never yours: you refer, support, and follow up.</p>
<p>Much of what you do every day also counts. Solving the fare problem, arranging a caregiver&rsquo;s rest, reconnecting a man with his chess partner: practical help reduces the load that feeds distress, even though trials rarely measure it.</p>
{{key:Offer what has evidence (talking therapy, counseling, exercise) and refer for medicine decisions. Say honestly that the trials measured symptoms, not survival.}}
"""),
        ("stepped", "Stepped care and referral", "Match the help to the need", """
<p>Stepped care means everyone gets the basics, and help steps up as need rises. It also means you step back down when things improve.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Who</th><th>What you offer</th></tr></thead>
<tbody>
<tr><td>1 Everyone</td><td>All patients</td><td>Listening, information, practical help with barriers, screening at agreed intervals</td></tr>
<tr><td>2 Some</td><td>Mild to moderate distress</td><td>Structured support: problem solving, behavioral activation (planning small pleasant activities), peer support, exercise with the team&rsquo;s agreement</td></tr>
<tr><td>3 Fewer</td><td>Moderate to severe depression or anxiety</td><td>Referral to a psychologist or psychiatrist for assessment and therapy or medicine; you keep following up</td></tr>
<tr><td>4 A few</td><td>Severe, or any safety risk</td><td>Urgent psychiatric review through the attending physician and the crisis route (Module 11)</td></tr>
</tbody></table></div>
<p>A referral to mental health is a referral like any other (Module 6): it is not done when sent. Many people decline or never attend. In ASCEND, a structured engagement interview did not raise treatment uptake (66% against 64%).[[mehrotra2019]] Patients decide for their own reasons. Your role is to make the offer, record the answer, keep the door open, and screen again.</p>
{{key:Everyone gets step 1. Step up when need rises, follow every referral to an outcome, and step down when things improve.}}
{{scene:The chess table|<p>Social worker Mr. Luis Bautista notices that three men on the Tuesday-Thursday-Saturday shift used to play chess in the waiting area before a renovation removed the table.</p>
<p>He asks the unit head for a small table in the waiting area. Two of the men tell him a month later that the mornings are &ldquo;less heavy.&rdquo;</p>
<p class="tc-scene-take">Not every intervention needs a referral form. Some just need a table.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The total.</strong> 2 + 2 + 3 + 3 + 2 + 2 + 1 + 1 + 0 = 16, the pattern of the worked example. That is above the dialysis-validated cutoff of 10, so depression is likely enough to report and refer. Sleep, energy, and appetite (8 points) may partly reflect kidney failure; interest, mood, and feeling a failure (6 points) do not. Item 9 is 0, so no safety pathway today, but you asked it in person and you will ask again. The score is not a diagnosis.</p>
<p><strong>To the nephrologist.</strong> Situation: &ldquo;Mr. Romeo Dizon, 58, said he does not see the point anymore; PHQ-9 16, item 9 zero.&rdquo; Background: &ldquo;Weeks of early waking with worry, poor appetite, missed Wednesday. Wife stopped work; income halved.&rdquo; Request: &ldquo;Please review possible physical causes of the sleep and appetite changes, and agree a referral to the mental health team.&rdquo; Offer Mr. Dizon a choice of next steps: structured support with you, a referral for talking therapy or a psychiatric assessment, and practical help with the money.</p>
<p><strong>What else.</strong> &ldquo;Does not see the point&rdquo; can also mean thoughts of stopping dialysis; ask what he means, and if he wants to stop, the nephrologist leads that conversation (Module 16). The missed session and the income loss are access problems (Modules 8 and 9). Aling Nena, who gave up her work, needs her own conversation about how she is coping (Module 13).</p>
"""],
    "skills": {"title": "A two-step screen with the safety question",
               "intro": "In a role-play with a simulated patient in the dialysis chair, screen for depression and agree next steps while your supervisor observes.",
               "items": [
                   ("Sets a private moment at the chair and asks the two PHQ-2 questions.", False),
                   ("Completes the PHQ-9 with the person and computes the total correctly.", False),
                   ("Asks item 9 in person in plain words, whatever the total.", True),
                   ("Interprets the score with the dialysis caveat and states that it is not a diagnosis.", False),
                   ("Starts the safety pathway on any positive item 9 answer.", True),
                   ("Explains the options and the strength of their evidence without promising a cure.", False),
                   ("Reports to the attending nephrologist in SBAR and follows the mental health referral to an outcome.", False),
               ],
               "placement": "With supervision, screen three patients (with consent) using the two-step approach and discuss each result with your supervisor."},
    "terms": [("Depression", "Persistent low mood or loss of interest for at least two weeks, diagnosed by a clinician."),
              ("PHQ-2", "The first two PHQ-9 questions."),
              ("PHQ-9", "Nine questions, total 0 to 27; a screen, not a diagnosis."),
              ("Item 9", "The PHQ-9 question about thoughts of death or self-harm."),
              ("Stepped care", "Matching support to need and stepping up when needed."),
              ("Behavioral activation", "Planning small, achievable, pleasant or meaningful activities to lift mood.")],
    "readings": [("ckd-mental-health-sleep.html", "The patient guide to mood and sleep in kidney disease.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
