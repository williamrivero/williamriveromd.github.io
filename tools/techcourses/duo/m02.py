# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 2: Kidney care and the patient journey. Written for this course from published sources."""

MODULE = {
    "image_alt": "A pair of human kidneys, one cut to show its inner structure, beside a small dialyzer cartridge.",
    "objectives": [
        "Explain in plain language what healthy kidneys do and how much of that work hemodialysis replaces.",
        "Explain why patients dialyze three times a week and why the long weekend gap carries extra risk.",
        "Describe what the evidence associates with missed and shortened sessions, and why make-up slots are a safety control.",
        "Place the unit inside the whole patient journey, including referral for transplant, home dialysis, and conservative care.",
    ],
    "big": """
{{plain:Healthy kidneys are like a water-treatment plant that never closes. Every hour of every day they clean the blood, remove extra water, and keep the body&rsquo;s salts in balance. Hemodialysis is a powerful plant that opens for about four hours, three times a week. Between openings, everything the kidneys would have cleared builds up.}}
<p>The picture has a limit. Kidneys do more than clean. They make the hormone that tells the bone marrow to make red cells, they activate vitamin D, and they help control blood pressure. Dialysis replaces only part of the cleaning and none of the hormones, which is why patients also need medicines, a diet, and a doctor who sees the whole person.</p>
{{cards:Key terms for this module|Kidney failure::Kidney function so low that dialysis, a transplant, or supportive care is needed to live well.|Interdialytic gap::The time between the end of one session and the start of the next.|Long gap::The roughly two-day gap over the weekend, for example Friday to Monday.|Dry weight::The weight a patient should reach at the end of a session, without extra fluid.|Conservative care::Care that manages symptoms and quality of life without dialysis, chosen with the patient.}}
<p>You do not need to treat patients to govern a unit well. You do need to understand why a schedule, a staffing gap, or a slow referral reaches a patient&rsquo;s heart. This module gives you that picture.</p>
""",
    "case": {"title": "The Monday-only slot", "html": """
<p>Mr. Arnel Cruz owns a unit in Cabanatuan. To reduce weekend overtime, his manager proposes closing on Saturdays and moving the Tuesday-Thursday-Saturday patients to Monday-Wednesday-Friday afternoons, with a new evening shift. Twenty patients would then dialyze Monday, Wednesday, and Friday, and the unit would have no free chairs left for make-up sessions.</p>
<p>The proposal saves about 45,000 pesos a month in overtime. The clinical head, Dr. Marissa Ocampo, asks for ten minutes at the next board meeting before anyone votes.</p>
""", "questions": ["What will Dr. Ocampo most likely say about the weekend gap?", "What happens to a patient who misses a Monday session under the new plan?",
                  "What would you ask for before you approve the change?"]},
    "sections": [
        ("kidney", "What kidneys do", "What kidneys do, and what dialysis replaces", """
<p>Each kidney holds about a million tiny filters. Together they filter the whole blood plasma many times a day, then take back almost everything the body needs and let the rest leave as urine. That is how they remove the wastes of protein breakdown, extra salt and water, and acid, and keep potassium in a narrow safe range.</p>
<p>When the kidneys fail, those wastes, water, potassium, and acid build up. Too much water raises blood pressure and floods the lungs. Too much potassium can stop the heart. Hemodialysis pumps blood through a filter, the dialyzer, where it meets a carefully made fluid, the dialysate. Wastes and potassium move across the membrane into the dialysate, and the machine pulls off extra water.</p>
<p>Dialysis is efficient for a few hours, but it is not a kidney. It is intermittent, it replaces none of the hormones, and it asks a great deal of the heart, because the water a kidney would have removed slowly over two days comes off in four hours.</p>
{{key:Dialysis replaces part of the kidney&rsquo;s cleaning for a few hours at a time. The rest of the week, the patient carries the load.}}
"""),
        ("week", "The dialysis week", "Why three sessions a week, and why the long gap matters", """
{{fig:duo02a}}
<p>Picture the week as a sawtooth. Fluid and wastes rise between sessions and fall during them. With three sessions a week, two gaps are about a day and a half and one gap, over the weekend, is about two and a half days. That long gap produces the highest peak.</p>
<p>The peak matters. In a study of 32,065 United States patients dialyzing three times a week, Foley and colleagues found that deaths from all causes, and especially from heart problems, were higher on the day after the long gap than on other days.[[dch_foley2011]] The study was observational, so it shows an association, but the pattern fits the physiology: more fluid and more potassium at the end of the longest gap.</p>
<p>Missing a session turns a short gap into a long one and a long gap into a very long one. Missed and shortened treatments are associated with more hospital stays and more deaths.[[pc_obialo2012]] In the international Dialysis Outcomes and Practice Patterns Study (DOPPS), the share of patients who missed at least one session in four months ranged from under 1% to 24% across countries, and missing was associated with higher mortality.[[dch_alsalmi2018]] In a large United States provider, rescheduling a missed session was associated with fewer hospitalizations than not rescheduling it.[[uom_cohen2020]]</p>
<p>Two other findings help an owner resist a tempting shortcut. Longer session times were associated with lower mortality in DOPPS, an observational finding.[[uom_saran2006]] And in the randomized Hemodialysis (HEMO) Study, a higher dose within the usual three-times-weekly schedule did not improve survival.[[uom_eknoyan2002]] Together they say that time and frequency matter, and that a faster session is not a free substitute for a longer one.</p>
{{key:A full schedule with no make-up chairs turns every missed session into a longer gap. Keep chairs free on purpose.}}
"""),
        ("journey", "The journey", "The patient journey your unit serves", """
{{fig:duo02b}}
<p>A patient reaches your unit after months or years of chronic kidney disease (CKD) care, ideally prepared: a working fistula in the arm, a plan, and a family that understands. Many arrive in crisis instead, through an emergency room with a temporary catheter in the neck. From the first session, the unit is part of a longer journey with several possible next steps: a kidney transplant, home or peritoneal dialysis (PD), or supportive conservative care for patients who choose it.</p>
<p>Philippine patients face gaps along this road, from late referral to the cost of care outside the PhilHealth package.[[pc_pajimna2023]] An owner cannot fix the health system, but the unit can make sure no patient is held back from the next step by the unit&rsquo;s own interests.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What the unit owes the patient</th><th>What the owner funds or protects</th></tr></thead>
<tbody>
<tr><td>Starting dialysis</td><td>Safe first sessions, teaching, an access plan</td><td>Time for teaching; a link with an access surgeon</td></tr>
<tr><td>Living on dialysis</td><td>Every scheduled session, make-up slots, monthly review</td><td>Staff and chairs that allow make-up sessions</td></tr>
<tr><td>Transplant</td><td>Information, referral, and the tests the program needs</td><td>No penalty, target, or delay for referring</td></tr>
<tr><td>Home or peritoneal dialysis</td><td>Honest information about every option</td><td>A referral pathway, even to another provider</td></tr>
<tr><td>Supportive care</td><td>Respect for the patient&rsquo;s choice and comfort care</td><td>Time for conversations, not only treatments</td></tr>
</tbody></table></div>
{{key:Your unit is one stage of the patient&rsquo;s journey, not the destination.}}
"""),
        ("referral", "Referral", "Referral is part of good service, not lost revenue", """
<p>A patient who receives a transplant stops dialyzing at your unit. That is a success, and the incentives can make it look like a loss. The evidence shows the risk is real. In a United States cohort of 3,569 patients, care at for-profit facilities was associated with 20% higher mortality and a 26% lower rate of placement on the transplant waiting list (adjusted hazard ratio 0.74) compared with nonprofit facilities.[[duo_garg1999]] A 2024 study of adolescents and young adults found that facilities with more patients per staff member had lower access to the transplant waiting list.[[dch_bicki2024]]</p>
<p>Both studies are observational and from another country, and many for-profit units refer well. The lesson is not about ownership type. It is about incentives: whatever the unit is paid for, and whatever its staff are too busy to do, shapes what happens to patients.</p>
<p>An owner can make referral safe and normal. Put transplant and home-dialysis information into every new patient&rsquo;s first month, give the clinical head time and a coordinator to complete work-ups, and report referrals to the board as a quality measure, never as lost revenue.</p>
{{key:Measure referrals as a quality indicator. If no one on your census has been referred in a year, ask why.}}
"""),
    ],
    "debrief": ["""
<p><strong>What Dr. Ocampo will say.</strong> Moving everyone to Monday-Wednesday-Friday keeps the weekend gap but removes every free chair. A patient who misses Monday now waits until Wednesday, a gap of about four and a half days, with rising fluid and potassium. The physiology and the observational evidence both point to higher risk.</p>
<p><strong>What to ask for.</strong> Ask the manager to show the plan on the safe-capacity calculator with make-up slots held back, and ask Dr. Ocampo which patients cannot tolerate the change. Compare the 45,000 pesos of overtime with the cost of one avoidable hospital admission and one lost patient. A better option may be to staff Saturday at lower cost, not to remove it.</p>
"""],
    "skills": {"title": "Patient journey map and referral safeguard",
               "intro": "With the clinical head, map one fictional patient&rsquo;s journey through your unit and write a referral safeguard policy.",
               "items": [("Explains the long gap and why make-up slots exist, in plain language.", False),
                         ("Reads the missed-session rate on the calculator and states the denominator.", False),
                         ("Keeps a set number of chairs free for make-up sessions in the schedule.", True),
                         ("Writes that no target, bonus, or delay may discourage referral for transplant or home dialysis.", True),
                         ("Names who gives transplant and home-dialysis information, and when.", False),
                         ("Adds referrals to the board&rsquo;s quality report.", False)],
               "placement": "Shadow a first-session teaching visit with the head nurse and note what the patient was told about other options."},
    "quiz": [
        ("Why does the weekend gap matter more than the midweek gaps?",
         ["Patients eat more on weekends", "It is the longest gap, so fluid and potassium build up the most", "Machines are less accurate on Mondays", "Staff are less experienced on Mondays"],
         1, "With three sessions a week, one gap is about two and a half days. The longer the gap, the higher the fluid and potassium peak."),
        ("In the study by Foley and colleagues, when were deaths highest?",
         ["During the dialysis session", "On the day after the long weekend gap", "On the day after a midweek session", "On public holidays"],
         1, "Deaths, especially cardiac deaths, were higher on the day after the long gap. The study was observational."),
        ("A schedule has no free chairs. What is the main safety problem?",
         ["Staff become bored", "A missed session cannot be made up, so the gap lengthens", "The water system runs too long", "PhilHealth will not pay"],
         1, "Make-up slots are a safety control. Without them, a missed session turns into a much longer gap."),
        ("The randomized HEMO Study tested a higher dose within the usual three-times-weekly schedule. What did it find?",
         ["A large survival benefit", "No survival benefit from the higher dose", "Higher mortality with the higher dose", "It was stopped for harm"],
         1, "The higher dose did not improve survival. Faster or more intense sessions are not a free substitute for time and frequency."),
        ("A patient on your census receives a kidney transplant. How should the board record this?",
         ["As lost revenue", "As a successful referral and part of the quality report", "It should not be recorded", "As a staffing problem"],
         1, "Referral for transplant is good care. Reporting it as a quality measure keeps incentives pointed at patients."),
        ("What did Garg and colleagues report about for-profit ownership in their United States cohort?",
         ["Higher waitlisting for transplant", "Lower mortality", "Higher mortality and lower placement on the transplant waiting list, as associations", "No difference in any outcome"],
         2, "Adjusted hazard ratios were 1.20 for death and 0.74 for waitlisting. The study was observational and from another health system."),
    ],
    "terms": [("Dialyzer", "The filter in which blood and dialysate meet across a membrane."),
              ("Dialysate", "The prepared fluid that draws wastes and extra salts out of the blood."),
              ("Waitlisting", "Placement on the list of people waiting for a kidney transplant.")],
    "readings": [("starting-dialysis-new-beginning.html", "What the first months on dialysis feel like for patients.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html#c6", "calc-dialysis-clinical-head-toolkit.html#c12"],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
