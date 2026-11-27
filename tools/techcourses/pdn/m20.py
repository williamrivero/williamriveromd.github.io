# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 20: Philippine requirements, records, quality and capstone. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Name who governs what in a Philippine pediatric dialysis service, with the issuer and date of each rule.",
        "Keep records that show actual care, distinguish prescribed from delivered treatment, and protect privacy.",
        "Calculate infection rates and interpret them with small denominators and case mix in mind.",
        "Assemble a capstone portfolio and one measurable improvement proposal.",
    ],
    "big": """
<p>A pediatric dialysis service sits under several authorities at once, and each asks a different question. Nurses meet these rules in forms, audits and claims, often without seeing the whole map. The map matters: it tells you which rule a document serves, and which office can answer a question about it.</p>
<p>Your work in this module is to know the map, to keep records that tell the truth, to count infections correctly, and to finish the track with a portfolio that shows what you can do.</p>
{{plain:Think of the rules as different keys on one ring. The PRC key opens your practice, the Department of Health key opens the facility, the PhilHealth key opens payment, and the hospital&rsquo;s key opens your unit. Each key opens one door only.}}
<p>The picture has a limit. Keys do not change; rules do. Circulars are amended, pilots expire and checklists are revised. Every rule you rely on needs its issuer and date checked, and a copy saved with the date you checked it.</p>
{{cards:Key terms for this module|Issuer::The body that wrote a rule and can interpret it.|Effective date::When a rule took effect, and when it ends if it is a pilot.|Delivered treatment::What actually happened, as opposed to what was prescribed.|Rate::Events divided by time at risk, such as episodes per patient-year.|Improvement aim::A specific, measurable target with a date.}}
""",
    "case": {"title": "The rate that doubled", "html": """
<p>A small pediatric PD program has eight children. Last year it had 2 peritonitis episodes; this year it had 4, and a manager says &ldquo;our infection rate doubled; the nurses must be careless&rdquo;. <strong>Nurse Liza</strong>, the program&rsquo;s PD nurse, is asked to present the numbers. The children spent a total of 90 patient-months on PD this year.</p>
""", "questions": ["What is this year&rsquo;s peritonitis rate, and how does it compare with the ISPD 2024 benchmark?",
                  "Does &ldquo;doubled&rdquo; mean what the manager thinks?",
                  "What should Liza propose instead of blame?"]},
    "sections": [
        ("who-governs-what", "Who governs", "Who governs what", """
<p>Read every rule for its issuer, its scope and its date.</p>
{{fig:pdn20_a}}
<div class="table-wrap"><table>
<thead><tr><th>Issuer</th><th>Governs</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Professional Regulation Commission and Board of Nursing</td><td>The nurse&rsquo;s license and scope</td><td>Philippine Nursing Act of 2002 (RA 9173)[[pd_ra9173]]</td></tr>
<tr><td>Department of Health</td><td>The facility&rsquo;s license, staffing and water</td><td>AO 2012-0001 on dialysis facilities; AO 2013-0003 on dialysis water[[doh2012]][[doh_ao2013_0003]]</td></tr>
<tr><td>Philippine Society of Nephrology</td><td>Professional guidelines</td><td>Hemodialysis guidelines for nephrologists, 2024[[psn2024]]</td></tr>
<tr><td>PhilHealth</td><td>Benefits and provider contracting</td><td>PD Z-benefit Circular 2024-0036; PD First self-assessment tool; pediatric automated PD pilot advisories 2025-0074 and 2026-0013; pediatric post-transplant Z benefit Circular 2025-0011[[pd_ph_pc2024]][[pd_ph_sat]][[pc_pa2025_0074]][[pd_ph_pa2026]][[rtc_ph2025c]]</td></tr>
<tr><td>National Privacy Commission</td><td>Personal and health data</td><td>Data Privacy Act of 2012 (RA 10173)[[ra10173]]</td></tr>
<tr><td>Congress (child protection)</td><td>Protection of children</td><td>RA 7610[[pdn_ra7610]]</td></tr>
<tr><td>The hospital</td><td>Privileges, procedures and competency records</td><td>Unit policies and job descriptions</td></tr>
</tbody></table></div>
<p>The review behind this track, in November 2026, found no separate pediatric dialysis nurse license or pediatric nurse-to-patient ratio, and could not verify the status of the pediatric automated PD pilot after July 31, 2026. These are bounded findings; check for later issuances.</p>
{{key:Every rule has an issuer and a date. Save the version you checked and the date you checked it.}}
"""),
        ("the-record", "The record", "Records that tell the truth", """
<p>A dialysis record is a clinical, legal and financial document. In pediatrics it must show the child&rsquo;s size as well as the treatment.</p>
<ul>
<li><strong>Prescribed versus delivered:</strong> record what actually happened (time on treatment, fluid removed, exchanges completed, missed therapy), not only what was ordered.</li>
<li><strong>Size and conditions:</strong> weight with its conditions, height, BSA where used, PD fill state.</li>
<li><strong>Events:</strong> alarms, contaminations, interventions and calls, each with a time.</li>
<li><strong>Consent and assent:</strong> who consented, whether the child assented, and any refusal.</li>
<li><strong>Corrections:</strong> never erase; correct per policy with date, time and initials.</li>
<li><strong>Privacy:</strong> health data are sensitive personal information; share only for care, and never on personal phones or group chats outside approved systems.[[ra10173]]</li>
</ul>
{{key:Write what happened, when, to which size of child. A record that matches the order perfectly every time is a record to question.}}
"""),
        ("measuring-quality", "Quality", "Measuring quality honestly", """
<p>The ISPD 2024 pediatric benchmark for overall peritonitis is no more than 0.4 episodes per year at risk, with culture-negative peritonitis under 15% and post-insertion peritonitis within 30 days after fewer than 5% of insertions (not graded).[[pdn_warady2024]] For hemodialysis catheters, the SCOPE collaborative reported infections per 100 patient-months.[[pdn_marsenic2020]]</p>
{{fig:pdn20_b}}
{{formula:Peritonitis rate = episodes &divide; (patient-months at risk &divide; 12)<br>This year: 4 &divide; (90 &divide; 12) = 4 &divide; 7.5 = 0.53 per patient-year<br>CA-BSI per 100 patient-months = episodes &divide; catheter patient-months &times; 100}}
<p>Small programs have small denominators. With eight children, one or two extra episodes move the rate a great deal, and a confidence interval around 0.53 would be wide. Compare rates over several years or as a run chart, look at each episode&rsquo;s apparent cause, and interpret infections with case mix in mind: infants, ostomies and new caregivers carry more risk. Do not use small-number infection rates to rank individual nurses.</p>
{{key:Rates need time at risk in the denominator. In a small program, look at causes and trends, not one year&rsquo;s number.}}
"""),
        ("capstone", "Capstone", "The capstone", """
<p>The capstone brings the track together. Your portfolio, assessed by a nurse educator, contains:</p>
<ul>
<li>Your learning agreement and supervision record (Module 1).</li>
<li>One communication and assent plan for a fictional child (Module 3).</li>
<li>A reconciled chart with weight-based arithmetic and an independent check (Module 4).</li>
<li>A PD order review with fill volume in mL/m&sup2; and an HD time-out with the extracorporeal-volume share (Modules 7 and 13).</li>
<li>A cloudy-bag SBAR and a hemodialysis emergency handoff (Modules 11 and 15).</li>
<li>A caregiver readiness record with retraining plan and a home emergency plan (Module 18).</li>
<li>A transition summary (Module 19).</li>
<li>One improvement proposal: a measurable aim, the measure, a baseline, one change to test and a date.</li>
</ul>
<p>The eight simulation stations on the trainer page are assessed separately, and facility authorization remains the facility&rsquo;s decision. Completing the Academy track is an educational record only.</p>
{{scene:Liza presents the numbers|<p>Liza shows that this year&rsquo;s rate is 4 &divide; 7.5 = 0.53 per patient-year, above the 0.4 benchmark; last year&rsquo;s was 2 episodes over a similar number of months. She explains that with eight children, two extra episodes double the count. Her apparent cause analyses show three of the four episodes followed a new substitute caregiver. She proposes an aim: every new caregiver completes a return demonstration before independent exchanges, from next month, measured monthly.</p><p class="tc-scene-take">Turn a frightening number into a cause and a testable change.</p>}}
{{key:Finish with evidence of what you can do and one change you will test. Study is the start of authorization, never the end.}}
"""),
    ],
    "debrief": ["""
<p><strong>The rate.</strong> 4 episodes &divide; (90 &divide; 12) = 0.53 per patient-year, above the ISPD 2024 pediatric benchmark of 0.4.</p>
<p><strong>&ldquo;Doubled.&rdquo;</strong> In a program of eight children, a change from 2 to 4 episodes is within the range that chance and case mix can produce. It deserves investigation, not blame.</p>
<p><strong>Instead of blame.</strong> Apparent cause analysis of each episode, a run chart over several years, and one measurable improvement aim tied to the cause found, here verified training of every new caregiver.</p>
"""],
    "skills": {"title": "Records, rates and the capstone", "intro": "Use fictional program data.",
               "items": [("Names the issuer and date of five rules affecting the service", False),
                         ("Documents delivered treatment, size and events with times in a fictional record", True),
                         ("Calculates a peritonitis rate per patient-year and a CA-BSI rate per 100 patient-months", True),
                         ("Explains why small denominators limit interpretation", False),
                         ("Writes one measurable improvement aim with measure, baseline, change and date", False)],
               "placement": "Assemble the capstone portfolio and present it to your nurse educator."},
    "quiz": [
        ('Which body governs the nurse&rsquo;s license?',
         ['The PRC and Board of Nursing', 'PhilHealth', 'The DOH', 'PSN'], 0,
         'Each issuer governs one door.'),
        ('DOH AO 2012-0001 governs:',
         ['Benefits', 'Licensing of dialysis facilities', 'Nursing licenses', 'Data privacy'], 1,
         'Facility license and standards.'),
        ('Which issuance covers the pediatric automated PD pilot extension?',
         ['RA 9173', 'AO 2013-0003', 'PhilHealth Advisory 2026-0013', 'RA 7610'], 2,
         'Extended to July 31, 2026; later status unverified.'),
        ('Health data under the Data Privacy Act are:',
         ['Public', 'Only for PhilHealth', 'Shareable in group chats', 'Sensitive personal information'], 3,
         'Share only for care in approved systems.'),
        ('Why record delivered as well as prescribed treatment?',
         ['The gap shows what actually happened and what to fix', 'Habit', 'For billing only', 'It does not matter'], 0,
         'Records must tell the truth.'),
        ('How is a record error corrected?',
         ['Erase it', 'Correct per policy with date, time and initials', 'Use correction fluid', 'Rewrite the page'], 1,
         'Never erase.'),
        ('4 episodes over 90 patient-months equals:',
         ['0.04', '4.0', '0.53 per patient-year', '22.5'], 2,
         '90 &divide; 12 = 7.5; 4 &divide; 7.5.'),
        ('The ISPD 2024 pediatric peritonitis benchmark is:',
         ['1.0', '0.1', 'None', '0.4 or fewer per patient-year'], 3,
         'Not graded.'),
        ('SCOPE reported HD catheter infections per:',
         ['100 patient-months', 'Patient', 'Year only', 'Nurse'], 0,
         'Use time at risk.'),
        ('In a program of eight children, a rise from 2 to 4 episodes:',
         ['Proves carelessness', 'Can arise from chance and case mix and needs investigation', 'Is impossible', 'Means stop PD'], 1,
         'Small denominators.'),
        ('Infection rates should not be used to:',
         ['Track trends', 'Guide improvement', 'Rank individual nurses with small numbers', 'Compare years'], 2,
         'Interpret with case mix.'),
        ('An improvement aim must be:',
         ['Vague', 'Secret', 'Only verbal', 'Specific, measurable, with a date'], 3,
         'So you can tell if it worked.'),
        ('Completing the Academy track gives:',
         ['An educational record only', 'Clinical privileges', 'A PRC license', 'PhilHealth credit'], 0,
         'Authorization is the facility&rsquo;s.'),
        ('A record that matches the order perfectly every time should be:',
         ['Praised', 'Questioned', 'Copied', 'Ignored'], 1,
         'Real care varies.'),
        ('Why save the version and date of each rule you rely on?',
         ['Tradition', 'For decoration', 'Rules change, and pilots expire', 'No reason'], 2,
         'Check issuer and date.'),
    ],
    "terms": [("Issuer", "The body that wrote a rule and can interpret it."),
              ("Effective date", "When a rule took effect or ends."),
              ("Delivered treatment", "What actually happened, compared with what was prescribed."),
              ("Patient-year at risk", "Time patients were on the therapy and at risk of the event, in years."),
              ("Run chart", "A chart of a measure over time used to see trends."),
              ("Apparent cause analysis", "A structured review of how an event probably happened.")],
    "readings": [("philhealth-z-packages.html", "PhilHealth benefits for HD, PD and kidney transplant."),
                 ("dialysis-qapi-vs-cqi.html", "Quality improvement in dialysis.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-access-infection-rate.html"],
}
