# 09. Quality measurement and improvement

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-09 (Understand) · FIG-09B (Apply) · FIG-09C (Appreciate) · **Calculator:** CALC-06 Missed-treatment rate and run-chart signal checker

> **Why this matters.** Every unit says it gives quality care. The difference between a unit that improves and one that stays the same is whether it measures the right things the same way every month, looks at the trend rather than last month's number, and tests changes small and fast. Quality assessment and performance improvement (QAPI) is the Medical Director's program. Making its data honest and its meetings productive is largely your work.

## Learning objectives

1. Choose a balanced set of indicators covering adequacy, access, anemia, mineral metabolism, infection, hospitalization, attendance and patient experience.
2. Write an indicator data dictionary that removes ambiguity.
3. Read a run chart using standard signal rules instead of reacting to single points.
4. Run a Plan-Do-Study-Act (PDSA) cycle with a measurable aim.

## The model: what to measure and why

Indicators should track what patients experience (death, hospitalization, infection, symptoms) and the processes that drive those outcomes. A balanced dashboard for a maintenance HD unit:

| Domain | Example indicator | Why it matters |
|---|---|---|
| Adequacy | % of patients with single-pool Kt/V ≥ 1.2 | KDOQI (2015) sets a target spKt/V of 1.4 per thrice-weekly session and a minimum delivered dose of 1.2 |
| Vascular access | % using an arteriovenous fistula; % catheter-dependent > 90 days | Catheters drive infection and hospitalization (Module 05) |
| Anemia | % with hemoglobin in the unit's target range | KDIGO advises against routinely targeting high hemoglobin with ESAs because of cardiovascular and stroke risk |
| Mineral metabolism | % with phosphate in target range | Hyperphosphatemia is associated with vascular calcification and mortality |
| Infection | BSI per 100 patient-months | Preventable harm |
| Attendance | Missed and shortened sessions per 100 scheduled | Linked to mortality (Module 04) |
| Hospitalization | Admissions per patient-year | Patient-important outcome |
| Experience | Patient-reported experience survey score | Captures what laboratory values miss |

**Surrogate warning.** Kt/V, hemoglobin and phosphate are **surrogate** measures. Hitting them is necessary but not sufficient. The HEMO trial (2002) showed that pushing dose higher than the standard did not improve survival. A unit can have perfect Kt/V and still harm patients through infections or missed sessions, which is why the dashboard includes hard outcomes.

## The data dictionary

Ambiguous definitions produce false trends. Each indicator needs:

- **Numerator:** exactly who counts (for example, patients with spKt/V ≥ 1.2 on the monthly sample).
- **Denominator:** who is eligible (for example, patients on maintenance HD in the unit for at least 30 days, sampled that month).
- **Exclusions:** stated in advance (for example, patients dialyzed fewer than three times in the month).
- **Data source and owner:** where it comes from and who extracts it.
- **Frequency and due date.**

## What the evidence shows about improvement methods

- **Run charts beat month-to-month comparison.** Standard rules distinguish real change from noise (Perla, Provost and Murray, *BMJ Quality & Safety* 2011): a **shift** is six or more consecutive points above or below the median; a **trend** is five or more consecutive points all increasing or all decreasing; too few or too many runs, or an obvious outlier, also signal non-random variation. These are statistical conventions with **established** methodological support.
- **Bundles plus measurement plus feedback improve dialysis outcomes.** The CDC BSI collaborative paired monthly surveillance and feedback with practice changes and saw large reductions (Patel et al., *AJKD* 2013).
- **PDSA quality varies.** Systematic reviews of PDSA use in healthcare find that many projects skip the "study" step or test changes that are too large. Small, documented, sequential cycles work better. This is **evidence-supported inference** from implementation research.

## Calculator CALC-06: missed-treatment rate and run-chart signal checker

**Inputs:** scheduled sessions, missed sessions, shortened sessions (delivered time less than prescribed by more than a set threshold, for example 15 minutes), and the last 12 to 24 monthly values of any indicator.

**Formulas**

- Missed sessions per 100 scheduled = missed ÷ scheduled × 100
- Shortened sessions per 100 delivered = shortened ÷ delivered × 100
- Median of the series; flag a **shift** (≥ 6 consecutive points on one side of the median, ignoring points on the median) and a **trend** (≥ 5 consecutive increases or decreases)

**Worked example.** 1,080 scheduled sessions, 27 missed: 2.5 per 100. Over 12 months the rate was 3.1, 3.4, 2.9, 3.3, 3.0, 3.2, 2.6, 2.4, 2.5, 2.3, 2.6, 2.5 (median 2.75). The last six points all fall below the median: a shift. Something real changed in month 7, which was when the unit started reminder calls the evening before each session. The timing supports the change as the cause, provided nothing else changed that month (a new shift pattern, a transport program). Ask before you claim it.

## Running a PDSA cycle

**Aim** (specific, measurable, time-bound): "Reduce missed sessions from 3.1 to below 2.0 per 100 scheduled by June 30."

1. **Plan:** predict what will happen. "If the shift nurse calls patients with two or more misses last month, the evening before, at least half will attend."
2. **Do:** test with 10 patients for two weeks.
3. **Study:** compare results with the prediction. What surprised you?
4. **Act:** adopt, adapt or abandon. Then test the next change.

## The QAPI meeting

- Chaired by the Medical Director, with nursing, technical, dietitian, social worker (where present) and operations.
- Review the dashboard as run charts, not tables.
- For each signal: owner, action, due date.
- Minutes record decisions and follow-up from the last meeting.
- Keep patient identifiers out of shared slides.

## Field case: the improving number that was not real

**Situation.** Fistula use rose from 48% to 61% in one month. The team celebrated.

**Problem.** The data dictionary was checked. The extractor had changed the denominator to exclude patients in their first 90 days, which removed many catheter users.

**Solution.** The definition was restored, the series recalculated (fistula use was 49%), and the dictionary was locked with a change log. A real improvement project then began on referral time to the vascular surgeon.

## Common failure modes

- Reacting to every monthly up or down.
- Changing definitions without recording it.
- Projects with no numeric aim or deadline.
- Dashboards with only surrogate laboratory targets and no outcomes.

## Supervised practice

- [ ] Write data dictionary entries for five indicators.
- [ ] Build a 12-month run chart for missed sessions using CALC-06 and identify any signals.
- [ ] Plan and run one PDSA cycle with a written prediction.
- [ ] Prepare the operations section of a QAPI meeting.

## Question bank

**Q1.** What minimum delivered spKt/V per thrice-weekly session does KDOQI (2015) set?
- [x] 1.2
- [ ] 0.8
- [ ] 2.0
- [ ] 1.0
> The target is 1.4, the minimum delivered dose 1.2.

**Q2.** Why is Kt/V called a surrogate?
- [x] It is a laboratory-derived process measure, not a patient-experienced outcome
- [ ] It measures mortality directly
- [ ] It is never measured
- [ ] It is a survey score
> Surrogates must be paired with hard outcomes.

**Q3.** What did the HEMO trial show?
- [x] A dose higher than standard did not improve survival
- [ ] Higher dose halved mortality
- [ ] Dialysis dose does not matter at all
- [ ] Lower dose is better
> More is not always better once adequacy is achieved.

**Q4.** Under run-chart rules, a shift is:
- [x] Six or more consecutive points on one side of the median
- [ ] One point above the mean
- [ ] Two points that differ by 10%
- [ ] Any change from last month
> Shifts signal non-random change.

**Q5.** A trend on a run chart is:
- [x] Five or more consecutive increases or decreases
- [ ] Three random points
- [ ] Any line going up
- [ ] A single outlier
> Standard conventions reduce false alarms.

**Q6.** 1,200 scheduled sessions and 30 missed. Rate per 100?
- [x] 2.5
- [ ] 25
- [ ] 0.25
- [ ] 40
> 30 ÷ 1,200 × 100 = 2.5.

**Q7.** What belongs in a data dictionary entry?
- [x] Numerator, denominator, exclusions, source, owner and frequency
- [ ] Only the indicator name
- [ ] Staff salaries
- [ ] Patient names
> Clear definitions make trends trustworthy.

**Q8.** Fistula use jumps 13 points in a month. The first step is to:
- [x] Check whether the definition or data extraction changed
- [ ] Announce success publicly
- [ ] Ignore it
- [ ] Reduce audits
> Sudden jumps often reflect measurement changes.

**Q9.** Which aim statement is best?
- [x] Reduce missed sessions from 3.1 to below 2.0 per 100 by June 30
- [ ] Improve attendance
- [ ] Try harder with patients
- [ ] Have fewer problems
> Aims need a measure, target and deadline.

**Q10.** Who chairs the QAPI program under DOH AO 2012-0001?
- [x] The Medical Director
- [ ] The vendor
- [ ] The billing clerk
- [ ] An external consultant only
> QAPI is a Medical Director function.

**Q11.** In PDSA, the "Study" step involves:
- [x] Comparing results with the prediction
- [ ] Reading textbooks
- [ ] Hiring more staff
- [ ] Skipping to the next change
> Learning comes from prediction versus result.

**Q12.** Why does KDIGO caution against routinely targeting high hemoglobin with ESAs?
- [x] Higher targets have been associated with cardiovascular and stroke harm
- [ ] ESAs are not available
- [ ] Hemoglobin cannot be measured in dialysis
- [ ] Anemia improves on its own
> Trials showed harm at high targets.

**Q13.** The last six monthly values all sit below the median after a new reminder system. This suggests:
- [x] A real improvement linked to the change
- [ ] Random noise
- [ ] A data error, always
- [ ] The median is wrong
> A shift after a change supports its effect.

**Q14.** Why include hospitalization in a quality dashboard?
- [x] It is a patient-important outcome that surrogates may miss
- [ ] It is easy to hide
- [ ] It is not related to dialysis
- [ ] PhilHealth forbids other indicators
> Outcomes anchor process measures to what matters.

**Q15.** A common failure in PDSA projects is:
- [x] Testing changes too large and skipping the Study step
- [ ] Making predictions
- [ ] Using small samples
- [ ] Recording results
> Small, documented cycles work better.

## Sources

PH1, PH5, PH6, INT1, E7, E14, E15, E17, E21, E22. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
