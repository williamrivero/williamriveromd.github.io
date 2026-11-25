# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 23: Supervision, evidence appraisal and quality improvement.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. FLOW figures, the CDC collaborative and the run-chart rules checked against PubMed."""

MODULE = {'image_alt': "An attending watches a nephrology fellow examine a patient's fistula.",
 'objectives': ['Give behavior-specific feedback and match supervision to entrustment.',
                'Appraise trials with absolute effects and applicability.',
                'Design a quality improvement (QI) project with a defined denominator, baseline and balancing measure.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you stay in active management with the physician on duty and the nurse on '
        'duty (b7).[[an01_1]] Teaching them well is part of that duty.</div>\n'
        '{{plain:Think of a weighing scale in the market. A vendor can make a kilo look like more by leaning on the pan, or a buyer can '
        'be fooled by a scale that reads high. Teaching, reading trials and measuring a unit&rsquo;s progress are all about honest '
        'scales.}}\n'
        '<p>The picture has a limit. A scale weighs one thing at a time. Your three scales are harder: a learner&rsquo;s skill on a '
        'given task, the true size of a drug&rsquo;s benefit for your patient, and whether a unit you do not own is really getting '
        'safer. Each one needs a clear definition before you read it, or you will believe the number that pleases you.</p>\n'
        '{{cards:Key numbers|Number needed to treat (NNT)::NNT = 1 / absolute risk reduction (ARR)|FLOW example::ARR about 4.5 '
        'percentage points over 3.4 years, NNT about 22|Run chart shift rule::6 or more consecutive points on one side of the median}}\n'
        '<p>In Philippine practice you supervise people you do not employ: the unit&rsquo;s physicians on duty, its nurses, and the '
        'fellows who rotate with you. Your work in this module is to give them feedback they can act on, to read evidence in absolute '
        'terms, and to help the unit measure improvement honestly.</p>\n',
 'case': {'title': 'Fewer infections, or fewer catheters?',
          'html': '<p>At the unit&rsquo;s quarterly quality meeting, which the clinical head chairs and the attending nephrologists are '
                  'invited to, the infection-control nurse presents a slide in green: &ldquo;Access infections down by half! 3 this '
                  'quarter, 6 last quarter.&rdquo; The administrator wants to put it on the unit&rsquo;s Facebook page. A new nephrology '
                  'fellow rotating with you, Dr. Cruz, asks you afterwards whether that proves the new catheter-care bundle works.</p>\n'
                  '<p>You look at the census. Last quarter the unit had about 2,400 catheter-days. This quarter, after many patients moved '
                  'to fistulas, it had about 1,000.</p>\n',
          'questions': ['Did infections fall?',
                        'What would you teach Dr. Cruz from this slide?',
                        'How would you test whether the bundle works?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p><strong>Supervision.</strong> Entrustment is graded and task by task. A learner moves from observing, to acting under '
               'direct supervision, to acting under indirect supervision, to working alone. A fellow may be trusted alone with a routine '
               'prescription and not yet with a hyperkalemia call at night.</p>\n'
               '<p><strong>Appraisal.</strong> Across patients at different baseline risk, the relative effect of a treatment often stays '
               'roughly constant. The absolute benefit does not: the same relative reduction removes more events where more events were '
               'going to happen. That is why the same drug helps a high-risk patient more in absolute terms.</p>\n'
               '<p><strong>Measurement.</strong> A rate needs a numerator, a denominator that reflects exposure, a baseline, and enough '
               'points in time to separate signal from noise. On a run chart, six or more consecutive points on one side of the median '
               'signal a shift; points on the median are skipped.[[an23_7]]</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Scale</th><th>What distorts it</th><th>What you check</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>A learner&rsquo;s skill</td><td>Vague praise, or judging from a chart note alone</td><td>A real task, observed, '
               'and the learner&rsquo;s reasoning</td></tr>\n'
               '<tr><td>A trial&rsquo;s benefit</td><td>A relative reduction quoted alone; a surrogate outcome</td><td>Event rates in both '
               'arms, the outcome patients feel, and who was studied</td></tr>\n'
               '<tr><td>A unit&rsquo;s progress</td><td>Counts without denominators; one good quarter</td><td>Rates per exposure, a '
               'baseline, a run chart</td></tr>\n'
               '</tbody></table></div>\n'
               '<div class="tc-scene"><span class="tc-lab">Teaching the number needed to treat &middot; fictional</span><p>Dr. Cruz, the '
               'rotating fellow, says a new drug &ldquo;cuts kidney events by 24%.&rdquo; You ask what the event rate was in the placebo '
               'group.</p><p>In FLOW it was 23.2%, and 18.7% with semaglutide.[[an23_6]] The absolute difference is about 4.5 percentage '
               'points over a median of 3.4 years, so about 22 patients are treated for one to avoid a major kidney event. For a patient '
               'at lower risk, the same 24% would mean a much smaller absolute gain.</p><p class="tc-scene-take"><b>What this shows.</b> '
               'Relative effects stay roughly constant; absolute benefit depends on baseline risk.</p></div>\n'
               '{{key:Before you believe any number, ask what it is divided by.}}\n'
               '\n'
               '{{fig:an23_b}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Training.</strong> Specialist programs such as the United Kingdom General Medical Council (GMC) renal medicine '
               'curriculum and the Royal Australasian College of Physicians (RACP) nephrology advanced training build assessment on '
               'observed work, not on examinations alone.[[an23_4]][[an23_5]] These are curriculum designs, not trial results.</p>\n'
               '<p><strong>Quality improvement in dialysis.</strong> In a collaborative sponsored by the Centers for Disease Control and '
               'Prevention (CDC), 17 United States outpatient units adopted a package of chlorhexidine exit-site care, staff training, '
               'hand-hygiene and access-care audits, and feedback of rates. Pooled bloodstream infections fell from 1.09 to 0.89 per 100 '
               'patient-months, and access-related bloodstream infections from 0.73 to 0.42. The units volunteered, and there was no '
               'control arm, so the design supports, but does not prove, that the package caused the fall.[[an23_8]] CDC keeps these '
               'interventions as its core dialysis safety resources.[[an23_3]] PhilHealth&rsquo;s quality standards for maintenance '
               'hemodialysis give units a local reference for what to measure.[[an23_2]]</p>\n'
               '<p><strong>Appraisal arithmetic.</strong> NNT = 1 / ARR. For FLOW, an ARR of about 4.5 percentage points over a median '
               '3.4 years gives an NNT of about 22.[[an23_6]] Guideline grades come from systems like the Kidney Disease: Improving Global '
               'Outcomes (KDIGO) library; quote them in the guideline&rsquo;s own words, never translated between systems.[[an23_1]]</p>\n'
               '{{key:A before-and-after improvement is encouraging, not conclusive. Say so when you present it.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Supervising people you do not employ.</strong> Tell the physician on duty or the fellow what they may do alone '
               'and when they must call you. Observe a real task, ask for their reasoning, and agree one specific behavior to repeat. When '
               'a concern is about the unit&rsquo;s system rather than one person, raise it with the clinical head or the head nurse, who '
               'manage the staff.</p>\n'
               '<p><strong>Appraising a trial.</strong> Ask who was studied, whether the outcome is one patients feel or a surrogate, what '
               'the absolute effect was, and whether it applies to your patient and your setting: the cost to a patient paying out of '
               'pocket, and the monitoring he can afford.</p>\n'
               '<p><strong>Quality improvement in a unit you do not own.</strong> Bring a project to the unit&rsquo;s quality meeting, not '
               'around it. Write a SMART (specific, measurable, achievable, relevant, time-bound) aim, define the numerator and denominator, '
               'collect a baseline, test one small change, track a process and a balancing measure, and review at a fixed date. Start '
               'with your own patients if the unit is not ready.</p>\n'
               '\n'
               '{{fig:an23_c}}\n'
               '<div class="tc-scene"><span class="tc-lab">The first test of change &middot; fictional</span><p>For your own patients on '
               'catheters, you and the head nurse set an aim: reduce catheter infections from 3.0 to below 1.5 per 1,000 catheter-days by '
               'June. Measures: the infection rate, checklist completion, and minutes of delay to session start.</p><p>In month one, '
               'checklist completion is 60% and start times are unchanged. You shorten the checklist from twelve items to six and test it '
               'again in month two.</p><p class="tc-scene-take"><b>What this shows.</b> Test one small change, measure it honestly, and '
               'adjust.</p></div>\n'
               '{{key:Test one small change, measure it with a denominator, and add a balancing measure for any change that adds '
               'work.}}\n'
               '{{call:<ul><li>Relative risk reduction quoted without absolute effect</li><li>Rates compared with different '
               'denominators</li><li>Improvement claimed from a single data point</li><li>No balancing measure for a change that adds '
               'work</li></ul>}}\n')],
 'debrief': ['<p><strong>Did infections fall?</strong> No. Counts mislead when exposure changes. Last quarter: 6 &divide; 2,400 &times; '
             '1,000 = 2.5 infections per 1,000 catheter-days. This quarter: 3 &divide; 1,000 &times; 1,000 = 3.0. The rate rose. The good '
             'news on the slide is real, but it is a different success: fewer patients on catheters.</p>\n'
             '<p><strong>What to teach.</strong> A rate needs a numerator, a denominator that reflects exposure, and a baseline. Ask Dr. '
             'Cruz to recalculate it himself, then present the corrected version at the next meeting. That is entrustment in practice: you '
             'observe a real task, ask for his reasoning, and agree on one behavior to repeat. Here the behavior is never to compare '
             'counts without denominators. The same habit applies when he reads a trial: a relative reduction without the absolute effect '
             'is half the story.</p>\n'
             '<p><strong>Testing the bundle.</strong> Suggest it to the clinical head as the unit&rsquo;s project, not yours alone. Check '
             'case definitions and data completeness first. Then run one small test of change, such as an audited catheter-care checklist '
             'on every shift. Track a process measure (checklist completion), the outcome (infections per 1,000 catheter-days), and a '
             'balancing measure (delayed or shortened treatments). Plot the rate monthly on a run chart. Six or more consecutive points on '
             'one side of the median signal a real change. One good quarter does not. And ask the administrator to hold the Facebook post '
             'until the corrected rate is ready.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Defines numerator and denominator', False),
                      ('Gives behavior-specific feedback', False),
                      ('Drafts a measurement plan with a balancing measure', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which comparison supports assessment of the apparent improvement?',
           ['Raw counts only',
            'Rates based on comparable catheter exposure',
            'A comparison of staff head counts',
            'Patient satisfaction alone'],
           1,
           'The exposure denominator accounts for a changing population at risk.'),
          ('What is an example of a balancing measure in a catheter-reduction project?',
           ['Missed or delayed treatments associated with the change',
            'The catheter infection numerator alone',
            'The number of meeting invitations',
            'The QI team&rsquo;s attendance'],
           0,
           'Balancing measures detect new harms introduced by an improvement.'),
          ('A trial shows event rates of 20% vs 15%. What is the NNT?',
           ['33', '5', '15', '20'],
           3,
           'ARR = 5 percentage points; NNT = 1 / 0.05 = 20.'),
          ('Why does the same relative risk reduction yield more benefit in high-risk patients?',
           ['High-risk patients adhere better',
            'Relative risk rises with age',
            'Absolute risk reduction scales with baseline risk',
            'Statistical significance is easier to reach'],
           2,
           'A constant relative effect applied to a larger baseline risk removes more events.'),
          ('Which feedback is most useful to a learner?',
           ['&lsquo;Good job overall&rsquo;',
            '&lsquo;Next time, read back the potassium order before ending the call&rsquo;',
            '&lsquo;Be more careful&rsquo;',
            '&lsquo;You need to improve communication&rsquo;'],
           1,
           'Specific, behavior-focused feedback gives a repeatable action.')],
 'terms': [('QI', 'Quality improvement'), ('ARR', 'Absolute risk reduction'), ('NNT', 'Number needed to treat'),
           ('PSN', 'Philippine Society of Nephrology'), ('GMC', 'General Medical Council'),
           ('RACP', 'Royal Australasian College of Physicians'), ('CDC', 'Centers for Disease Control and Prevention'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'), ('SMART', 'Specific, measurable, achievable, relevant, time-bound')],
 'readings': [('dialysis-qapi-vs-cqi.html', 'Dialysis Center QAPI vs. CQI: A Quality Management Field Manual')],
 'calcs': ['calc-access-infection-rate.html',
           'calc-qapi-run-chart-spc.html',
           'calc-qapi-cqi-toolkit.html',
           'calc-dialysis-qapi-scorecard.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
