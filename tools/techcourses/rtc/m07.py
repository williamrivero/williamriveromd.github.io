# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 07: Donor Medical Evaluation and Long-Term Risk. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nephrologist explaining a simple risk chart to an adult donor while a coordinator takes notes beside them.",
    "objectives": [
        "Explain the questions a donor evaluation answers and who answers them.",
        "State the best available numbers for surgical death, complications, and long-term kidney failure after donation, in absolute terms.",
        "Distinguish a relative risk from an absolute risk when a donor asks &ldquo;how dangerous is it?&rdquo;",
        "Keep the donor&rsquo;s medical and ethics gates visible and separate from the recipient&rsquo;s schedule.",
        "Start the donor&rsquo;s long-term follow-up plan before discharge.",
    ],
    "big": """
{{plain:Two healthy kidneys are like two engines on an airplane. One engine can fly the plane, and after a donation the remaining kidney works harder to make up much of the lost capacity. But a plane with one engine has less in reserve if something else goes wrong later in life, such as high blood pressure, diabetes, or an injury to the remaining kidney.}}
<p>The picture has a limit. An engine does not grow. A remaining kidney does: in the months after donation, its filtration rises as its nephrons adapt, so a donor typically keeps well over half of their pre-donation kidney function. What the donor loses is reserve. That is why the donor evaluation asks two different questions &mdash; is surgery safe now, and is this person likely to stay healthy with one kidney for the rest of their life &mdash; and why the donor needs follow-up long after the wound heals.</p>
<p>The job of this module is to help the donor hear honest numbers. KDIGO&rsquo;s 2017 living donor guideline asks programs to estimate each donor&rsquo;s risk using the best available evidence and to communicate it in a way the donor understands, then to plan lifelong care.[[rtc_kdigo2017]] The donor&rsquo;s clinicians give the numbers; you make sure the conversation happens, is understood, and is followed up.</p>
{{cards:Key terms for this module|Donor evaluation::The tests and reviews that answer whether donation is safe now and over a lifetime.|Absolute risk::How many people out of a number have the event, such as 3 per 10,000.|Relative risk::How many times more likely the event is in one group than another. Easy to misread without the absolute numbers.|Kidney reserve::Extra filtering capacity the body can call on when the kidney is stressed.|Clavien grade::A scale of how serious a surgical complication is; grade IV is life-threatening.}}
""",
    "case": {"title": "&ldquo;Am I safe for life?&rdquo;", "html": """
<p>Ms. Daisy Navarro, 29, a call-center agent in Pasig, is being evaluated as a donor for her mother, Mrs. Teodora Navarro, 58. Her tests so far look normal. Her blood pressure was 132/84 at one visit.</p>
<p>After the nephrologist&rsquo;s risk discussion, she finds you in the corridor. &ldquo;The doctor said my risk of kidney failure is 8 times higher after donating. Eight times! But then she said it was small. Which is it? Am I safe for life?&rdquo;</p>
<p>Mrs. Navarro&rsquo;s surgeon would like to schedule the operation in three weeks, &ldquo;before Christmas, while the OR is free.&rdquo; Ms. Navarro&rsquo;s 24-hour blood pressure monitoring has not been done.</p>
""", "questions": ["How do you help Ms. Navarro understand &ldquo;8 times higher&rdquo; and &ldquo;small&rdquo; at the same time?",
                  "Which donor gate is still open, and who decides it?",
                  "What does &ldquo;safe for life&rdquo; require the program to do?"]},
    "sections": [
        ("questions", "Understand the questions", "What the donor evaluation asks", """
<p>The donor evaluation follows KDIGO&rsquo;s framework: kidney function, albumin in the urine, blood pressure, metabolic health (weight, glucose), kidney stones, infections that could pass to the recipient, cancer, psychosocial readiness, and a family history of kidney disease, among others.[[rtc_kdigo2017]] Each finding feeds two questions: is surgery safe now, and what is this person&rsquo;s lifetime risk with one kidney?</p>
<p>That lifetime risk starts before donation. A large analysis of seven cohorts (4.9 million people) projected that a healthy 40-year-old similar to typical donors had a 15-year risk of kidney failure, without donating, of 0.04% to 0.24% depending on race and sex, and that the risk rose with lower kidney function, more albumin in the urine, high blood pressure, smoking, diabetes, and obesity.[[rtc_grams2016]] This is why a single blood pressure of 132/84 in a young donor matters: it may prompt more measurement, and the clinicians decide what it means.</p>
<p>The site&rsquo;s <a href="calc-donor-esrd-risk.html">donor kidney failure risk calculator</a> is a clinician tool. You may collect the inputs the clinician asks for; you do not use the output to clear or exclude anyone.</p>
{{key:A donor evaluation asks two questions: safe now, and safe for a lifetime with one kidney. Clinicians answer both.}}
"""),
        ("numbers", "Honest numbers", "Absolute risks, from the best data we have", """
{{fig:rtc07_risk}}
<p>Donors deserve numbers they can picture. The strongest data come from large United States cohorts; Philippine data are limited, so treat these as the best available estimates, not local guarantees.</p>
<div class="table-wrap"><table>
<thead><tr><th>Outcome</th><th>Best available estimate</th><th>Source and limit</th></tr></thead>
<tbody>
<tr><td>Death within 90 days of surgery</td><td>3.1 per 10,000 donors (95% CI 2.0 to 4.6); 36.7 per 10,000 in donors with hypertension vs 1.3 without</td><td>80,347 US donors, 1994 to 2009[[rtc_segev2010]]</td></tr>
<tr><td>Any perioperative complication</td><td>16.8%; most often gastrointestinal, bleeding, or respiratory</td><td>14,964 donors, 97 US centers, 2008 to 2012[[rtc_lentine2016]]</td></tr>
<tr><td>Major (Clavien grade IV or higher) complication</td><td>2.5%; lower in centers doing more than 50 donations a year</td><td>Same study[[rtc_lentine2016]]</td></tr>
<tr><td>Kidney failure within 15 years</td><td>30.8 per 10,000 donors vs 3.9 per 10,000 matched healthy nondonors</td><td>96,217 US donors[[rtc_muzaale2014]]</td></tr>
<tr><td>Long-term death and kidney failure</td><td>Hazard ratios 1.30 (death), 1.40 (cardiovascular death), 11.38 (kidney failure) vs eligible nondonors; kidney failure 302 per million overall</td><td>1,901 Norwegian donors, median 15 years[[rtc_mjoen2014]]</td></tr>
</tbody></table></div>
<p>Now the arithmetic that confused Ms. Navarro. Thirty-one per 10,000 is about eight times 3.9 per 10,000: that is the <strong>relative</strong> risk. The <strong>absolute</strong> difference is about 27 extra cases of kidney failure per 10,000 donors over 15 years &mdash; roughly 1 in 370. Both statements are true. The first tells you the direction and size of the change; the second tells you how often it actually happens. Never give a donor one without the other.</p>
<p>These studies were observational. Donors and comparison groups differ in ways no matching fully removes, and the Norwegian study suggested that many donors who later developed kidney failure had an immunological kidney disease, sometimes possibly inherited &mdash; a reason the family history and the relationship matter in the evaluation.[[rtc_mjoen2014]]</p>
{{key:Give every donor both numbers: how many times more likely, and how many out of 10,000. Relative risk alone frightens; absolute risk alone can mislead.}}
"""),
        ("gates", "Keep the donor&rsquo;s gates visible", "The recipient&rsquo;s schedule does not set the donor&rsquo;s pace", """
<p>The commonest pressure on a donor evaluation is not a person. It is a calendar: an operating room slot, a holiday, a recipient getting sicker. The donor&rsquo;s medical gate closes only when the donor&rsquo;s evaluating clinicians have reviewed every result and written their decision. The ethics gate closes only when the HTEC has decided (Module 9). Neither may be closed to fit the recipient&rsquo;s schedule.</p>
<div class="table-wrap"><table>
<thead><tr><th>Donor gate</th><th>Owner</th><th>Closed by</th></tr></thead>
<tbody>
<tr><td>Medical suitability</td><td>Donor&rsquo;s evaluating clinicians</td><td>A written decision on current results</td></tr>
<tr><td>Psychosocial readiness</td><td>Psychiatrist or clinical psychologist; social worker</td><td>Reports received and reviewed</td></tr>
<tr><td>Advocate review</td><td>Designated donor advocate</td><td>The advocate&rsquo;s documented review</td></tr>
<tr><td>Ethics</td><td>HTEC</td><td>Written decision; conditions closed</td></tr>
<tr><td>Consent</td><td>Surgeon, with independent witnessing</td><td>Consent record (Module 8)</td></tr>
</tbody></table></div>
{{scene:The Christmas slot|<p>A surgeon asks coordinator Mr. Leo Bautista to book a living-donor transplant for December 18 &ldquo;while the OR is free.&rdquo; The donor&rsquo;s 24-hour blood pressure monitoring and psychiatric report are still pending.</p>
<p>Mr. Bautista replies with an SBAR listing the two open donor gates and their owners, and books the earliest monitoring slot. The surgeon agrees to a provisional January date.</p>
<p class="tc-scene-take">A free operating room is a resource, not a gate. The donor&rsquo;s pace is set by the donor&rsquo;s evaluation.</p>}}
{{key:Never let the recipient&rsquo;s calendar close a donor gate. Show the open donor gates, with owners, to anyone who proposes a date.}}
"""),
        ("beyond", "Plan beyond discharge", "Safe for life means followed for life", """
<p>&ldquo;Safe for life&rdquo; is not a promise anyone can make. What a program can promise is to watch for problems for life, so they are found early. KDIGO&rsquo;s donor guideline asks programs to provide a personalized post-donation care plan and long-term follow-up, and the DOH order makes lifetime monitoring part of the donor&rsquo;s protection.[[rtc_kdigo2017]][[rtc_doh2021]] PhilHealth&rsquo;s post-transplant packages list living donor monitoring among their covered services.[[rtc_ph2025a]]</p>
<p>Start the follow-up plan before the donor leaves hospital: the schedule, the tests (blood pressure, weight, kidney function, urine albumin), where they will be done, who pays, and how the donor will be reminded. The <a href="calc-transplant-coordinator-toolkit.html#tool-7">donor follow-up planner</a> drafts an example schedule to align with your protocol. Module 17 covers recall.</p>
{{key:Before discharge, the donor leaves with a dated follow-up plan, a named contact, and a funding route.}}
"""),
    ],
    "debrief": ["""
<p><strong>&ldquo;Eight times&rdquo; and &ldquo;small.&rdquo;</strong> Both are true. Draw it: out of 10,000 healthy people like her, about 4 would develop kidney failure over 15 years without donating; out of 10,000 donors, about 31 would. That is about eight times as many, but about 27 more people out of 10,000, roughly 1 in 370. Then encourage her to bring her questions back to her nephrologist, who can tailor the numbers to her.</p>
<p><strong>The open gate.</strong> Her medical gate is open: the 24-hour blood pressure monitoring is pending, and a borderline reading in a 29-year-old matters for lifetime risk. Her evaluating clinicians decide. Tell the surgeon, by SBAR, which donor gates are open and who owns them; the recipient&rsquo;s schedule does not close them.</p>
<p><strong>&ldquo;Safe for life.&rdquo;</strong> No one can promise it. The program can promise yearly checks of blood pressure, weight, kidney function, and urine albumin for life, with a named contact and a funding route, starting before she leaves hospital.</p>
"""],
    "skills": {"title": "Donor risk conversation support",
               "intro": "Support a simulated donor risk discussion and draft a follow-up plan while your preceptor observes.",
               "items": [
                   ("Explains the two questions of donor evaluation: safe now, and safe for a lifetime.", False),
                   ("Converts a relative risk into an absolute difference per 10,000 correctly.", True),
                   ("Uses a picture (an icon array or a drawing) to explain risk without giving clinical advice.", False),
                   ("Lists the donor&rsquo;s open gates with owners in an SBAR when a date is proposed.", True),
                   ("Drafts a post-donation follow-up plan with schedule, tests, place, funding, and contact.", True),
               ],
               "placement": "Sit in on one donor risk discussion (with consent). Afterward, write down the numbers the donor heard and check that both relative and absolute risk were given."},
    "terms": [("Absolute risk", "Events per number of people, such as 3 per 10,000."),
              ("Relative risk", "How many times more likely in one group than another."),
              ("Kidney reserve", "Spare filtering capacity."), ("Clavien grade", "A scale of surgical complication severity.")],
    "readings": [("kidney-transplant.html", "The patient guide, including what donors are told.")],
    "calcs": ["calc-donor-esrd-risk.html", "calc-transplant-coordinator-toolkit.html#tool-7"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
