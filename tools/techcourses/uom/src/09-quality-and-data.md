# 09. Quality measurement and improvement

## The big picture

{{plain:A unit's quality numbers are like a patient's vital signs. One reading tells you little; a series tells you a lot. A single high blood pressure might be a nervous patient. Six rising readings in a row is a trend that needs action. Quality work is the habit of reading the series, not reacting to the single reading.}}

The picture has a limit. A patient's blood pressure is measured the same way every time. A unit's indicators often are not. If someone quietly changes who is counted in the denominator, the number moves even though nothing in the unit changed. So quality measurement has two parts: defining each number so tightly that it means the same thing every month, and then reading the series with rules that separate real change from noise.

You do not need statistics training for this module. You need a ruler, a pencil, and the discipline to ask "what exactly are we counting?" before anyone celebrates or panics.

{{cards:Key terms for this module|Indicator::A number tracked over time to show how well the unit is doing.|Numerator and denominator::Who is counted as meeting the indicator, and who is eligible to be counted.|Data dictionary::The written definition of each indicator, so it never drifts.|Surrogate::A laboratory or process measure that stands in for an outcome patients feel.|Run chart::A line graph of an indicator over time, with its median drawn across.|Shift::Six or more points in a row on the same side of the median.|Trend::Five or more points in a row all going up, or all going down.|Plan-Do-Study-Act (PDSA)::A small, documented test of a change.}}

## Learning objectives

1. Choose a balanced set of indicators covering adequacy, access, anemia, mineral metabolism, infection, hospitalization, attendance and patient experience.
2. Write an indicator data dictionary that removes ambiguity.
3. Read a run chart using standard signal rules instead of reacting to single points.
4. Run a Plan-Do-Study-Act (PDSA) cycle with a measurable aim.

## Field case: the improving number that was not real

**Situation.** At the monthly quality assessment and performance improvement (QAPI) meeting of a 24-station hospital unit in Iloilo City, the dashboard shows fistula use jumping from 48% to 61% in a single month. The vascular access nurse, Ms. Rowena Tan, is congratulated. The Medical Director suggests presenting the result at the hospital's quality forum.

The manager, Mr. Jose Ledesma, is pleased too, but something bothers him. Nothing new happened in access referrals that month. The vascular surgeon was on leave for two weeks.

**Before reading on, decide:**

- What should Mr. Ledesma check before the result is presented anywhere?
- If the definition changed, what happens to the earlier months?
- How would you prevent this from happening again?

**Case review.**

**The check.** Mr. Ledesma opens the data dictionary entry and compares it with how the number was calculated this month. A new data clerk, trying to tidy the report, had excluded patients in their first 90 days of dialysis from the denominator. Many of those patients still have catheters while their fistulas mature. Removing them made fistula use jump without a single new fistula.

**The correction.** The original definition is restored, and the month is recalculated: 49%. The earlier months were calculated correctly and stand. Mr. Ledesma tells the meeting plainly and without blame, and the Medical Director withdraws the presentation.

**The lock.** The dictionary is locked with a change log. Any change to a definition needs the Medical Director's approval and is noted on the chart. Then the team starts a real improvement project on the time from referral to the vascular surgeon. Six months later, fistula use reaches 56%, and this time the run chart shows a genuine shift.

{{fig:uom09c}}

## The model: what to measure and why

Indicators should track what patients experience, such as death, hospitalization, infection, and symptoms, and the processes that lead to those outcomes.

{{fig:uom09a}}

| Domain | Example indicator | Why it matters |
|---|---|---|
| Adequacy | Percentage of patients with single-pool Kt/V of at least 1.2 | KDOQI (2015) sets a target of 1.4 per thrice-weekly session and a minimum delivered dose of 1.2 |
| Vascular access | Percentage using an arteriovenous fistula; percentage with a catheter beyond 90 days | Catheters drive infection and hospitalization (Module 5) |
| Anemia | Percentage with hemoglobin in the unit's target range | KDIGO advises against routinely targeting high hemoglobin with ESAs because of cardiovascular and stroke risk |
| Mineral metabolism | Percentage with phosphate in the target range | High phosphate is associated with vascular calcification and death |
| Infection | Bloodstream infections per 100 patient-months | Preventable harm |
| Attendance | Missed and shortened sessions per 100 scheduled | Linked to death (Module 4) |
| Hospitalization | Admissions per patient-year | An outcome patients feel |
| Experience | Patient-reported experience score | Captures what laboratory values miss |

**A warning about surrogates.** Kt/V, hemoglobin, and phosphate are surrogates. Meeting them is necessary but not enough. The HEMO trial (2002) showed that pushing dialysis dose above the standard did not improve survival. A unit can have perfect Kt/V and still harm patients through infections or missed sessions. That is why the dashboard includes hard outcomes.

{{key:A laboratory target met is not the same as a patient helped. Keep at least one outcome patients feel on every dashboard.}}

## The data dictionary

Vague definitions produce false trends. Each indicator needs:

{{fig:uom09b}}

- **Numerator:** exactly who counts, for example, patients with a single-pool Kt/V of at least 1.2 on the monthly sample.
- **Denominator:** who is eligible, for example, patients on maintenance hemodialysis in the unit for at least 30 days who were sampled that month.
- **Exclusions:** stated in advance, for example, patients dialyzed fewer than three times in the month.
- **Data source and owner:** where it comes from and who extracts it.
- **Frequency and due date.**
- **Change log:** every change to the definition, with the date and the approver.

## What the evidence shows about improvement methods

**Run charts beat month-to-month comparison.** Standard rules separate real change from noise.[[uom_perla2011]] A shift is six or more consecutive points above or below the median. A trend is five or more consecutive points all rising or all falling. Too few or too many runs, or an obvious outlier, also signal something non-random. These are statistical conventions with strong methodological support.

**Measurement plus feedback improves outcomes.** The Centers for Disease Control and Prevention bloodstream infection collaborative paired monthly surveillance and feedback with practice changes and saw large reductions.[[dch_patel2013]]

**PDSA quality varies.** Reviews of PDSA use in healthcare find that many projects skip the "study" step or test changes that are too large. Small, documented, sequential cycles work better. This is reasonable inference from implementation research.

## Calculator CALC-06: missed-treatment rate and run-chart signal checker

You need: scheduled sessions, missed sessions, shortened sessions (delivered time shorter than prescribed by more than a set threshold, such as 15 minutes), and the last 12 to 24 monthly values of any indicator.

{{formula:**Missed sessions per 100 scheduled** = missed ÷ scheduled × 100.<br>**Shortened sessions per 100 delivered** = shortened ÷ delivered × 100.<br>**Signals:** find the median of the series. A **shift** is six or more consecutive points on one side of the median, ignoring points on it. A **trend** is five or more consecutive increases or decreases.}}

**Worked example.** In a month with 1,080 scheduled sessions, 27 were missed: 27 ÷ 1,080 × 100 = 2.5 per 100. Over 12 months the rate was 3.1, 3.4, 2.9, 3.3, 3.0, 3.2, 2.6, 2.4, 2.5, 2.3, 2.6, 2.5. Sorted, the middle two values are 2.6 and 2.9, so the median is 2.75. The last six points all fall below it: a shift. Something real changed in month 7.

Month 7 was when the unit started calling patients the evening before each session. The timing supports the calls as the cause, provided nothing else changed that month, such as a new shift pattern or a barangay transport program. Ask before you claim it.

## Running a PDSA cycle

**Aim:** "Reduce missed sessions from 3.1 to below 2.0 per 100 scheduled by June 30." Specific, measurable, and with a deadline.

{{flow:One PDSA cycle|Plan::Predict what will happen. "If the shift nurse calls patients with two or more misses last month, the evening before, at least half will attend."|Do::Test it with 10 patients for two weeks.|Study::Compare the result with the prediction. What surprised you?|Act::Adopt, adapt, or abandon, then test the next change.}}

**Example.** A unit in Cagayan de Oro tests evening reminder calls with ten patients. Seven attend every session in two weeks, up from four. But the study step surfaces a surprise: three of the ten said they missed sessions because the jeepney route changed, not because they forgot. The next cycle tests a shared tricycle arrangement with the barangay for those three. A reminder call alone would never have fixed their problem.

## The QAPI meeting

- Chaired by the Medical Director, with nursing, technical, dietitian, social worker (where present), and operations.
- The dashboard is shown as run charts, not tables.
- Each signal gets an owner, an action, and a due date.
- The minutes record decisions and the follow-up from the last meeting.
- Patient identifiers stay out of shared slides.

{{call:If an indicator's definition, source, or calculation changed, flag it on the chart and tell the Medical Director before the result is used or presented. Never let a definition change pass as an improvement.}}

## Common failure modes

- **Chasing every wiggle.** Reacting to each monthly rise or fall.
- **Silent definition changes.** The denominator moves, and the trend lies.
- **Aims without numbers.** Projects with no target or deadline.
- **Surrogates only.** Dashboards full of laboratory targets and no outcomes patients feel.
- **Meetings without owners.** Signals discussed, no one assigned.

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
