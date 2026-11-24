# 03. Staffing, rostering and competency

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-03 (Understand) · FIG-03B (Apply) · FIG-03C (Appreciate) · **Calculator:** CALC-01 Station staffing and FTE planner

> **Why this matters.** A roster is a safety device that happens to look like a spreadsheet. The ratio printed in the regulation is a ceiling, not a target. What actually keeps patients safe is having the right person, with a signed competency for the task in front of them, at the station when the alarm sounds, and a relief plan for the day someone does not come.

## Learning objectives

1. Convert stations, shifts and operating days into required positions per shift and full-time equivalents (FTEs) using a relief factor.
2. Explain why the DOH 1:4 nurse-to-station and 1:15 POD-to-station figures are ceilings, and list the conditions that require more cover.
3. Build a competency matrix that links each staff member to signed skills, restrictions and reassessment dates.
4. Reallocate a roster after an absence without breaching ratio, competency or rest limits.

## The operating model: positions, people and proof

Staffing has three layers, and most units manage only the first.

**Positions** are the slots the shift needs: so many nurses, one POD, technicians, a water operator. You derive them from stations in use and from acuity.

**People** fill positions. A person counts toward a position only if they are present, rested, credentialed and competent for that position's tasks.

**Proof** is the competency record: a signed, dated checklist showing that the person was observed doing the skill correctly. Under pressure, units fill positions with people who lack proof. That is how a newly hired nurse ends up cannulating a fresh fistula alone on her second day.

### Why the ratio is a ceiling

DOH AO 2012-0001 sets ceilings of one nurse to four HD stations and one POD to fifteen HD stations. The ratio assumes stable patients and a functioning unit. Each of the following needs extra cover:

- **Isolation stations** (for example HBsAg-positive patients), where staff should not move freely between isolated and non-isolated patients.
- **New starts and first-week patients**, who have higher rates of hypotension, access problems and anxiety.
- **Catheter-dependent patients**, whose connection and disconnection require more nurse time and aseptic attention.
- **Breaks**, when one nurse covers another's patients.
- **Turnover periods**, when one shift ends and the next begins and disinfection, reprocessing and setup overlap.
- **Concurrent services**, such as an acute bedside treatment pulling a nurse away.

## What the evidence shows

- **Staffing burden is associated with outcomes.** In a US Renal Data System cohort of 236,126 patients starting in-center hemodialysis, facilities in the highest versus lowest quartile of patients per patient care technician had a 7% higher mortality rate (IRR 1.07; 95% CI 1.02–1.12), a 5% higher hospitalization rate, and an 8% higher rate of sepsis-related hospitalization (Plantinga et al., *JAMA Network Open* 2024). This is **observational**: facilities with heavy staffing burden may differ in other ways. It **is associated with** worse outcomes. It does not prove that adding staff alone fixes them.
- **Staffing varies widely, and ownership matters.** US facility surveys found registered nurse ratios 35% lower and technician ratios 16% higher in for-profit than nonprofit units after adjustment (Yoder et al., *AJKD* 2013). Staffing mix is a management choice, not a fixed fact.
- **Burnout is a safety variable.** A 2024 meta-analysis of 85 studies (288,581 nurses) linked nurse burnout to lower safety climate, more healthcare-associated infections, falls and medication errors, and lower patient satisfaction (Li et al., *JAMA Network Open* 2024). Chronic short-staffing produces burnout, which in turn degrades care. Again, this is association, but it is consistent across settings.

## Philippine rules that change the decision

| Rule | Implication | Verify |
|---|---|---|
| AO 2012-0001 §V.B.2 | 1:4 nurse and 1:15 POD ceilings; POD present during operating hours | CHD interpretation for mixed or acute services |
| Labor Code Art. 83 | Health personnel in cities of at least one million people, or in hospitals and clinics of at least 100 beds, work 40 hours a week (generally five days of eight hours). Elsewhere the normal workday is eight hours | HR classification of your facility and each worker |
| Labor Code rest-day rules | At least 24 consecutive hours of rest after six consecutive workdays | Employer policy, collective agreement |
| PSN guidelines | Training expectations for POD and staff | Current PSN requirements |

## Calculator CALC-01: station staffing and FTE planner

**Inputs:** stations in use per shift (S), isolation stations (I), shifts per day, operating days per week, paid hours per shift, contracted hours per FTE per week, non-productive fraction (leave, holidays, training, sick time).

**Formulas**

- Nurse positions per shift = ceiling((S − I) ÷ 4) + I × (isolation staffing per local policy, default one dedicated nurse per isolation area)
- POD positions per shift = ceiling(S ÷ 15)
- Weekly nurse hours = nurse positions × shifts per day × days per week × paid hours per shift
- Base FTE = weekly nurse hours ÷ contracted hours per FTE
- Relief factor = 1 ÷ (1 − non-productive fraction)
- Required FTE = base FTE × relief factor

**Worked example.** Fifteen stations, one isolation area with one station, three shifts a day, six days a week, six paid hours per shift, 40 contracted hours, 12% non-productive time.
- Nurse positions = ceiling(14 ÷ 4) + 1 = 4 + 1 = 5 per shift
- Weekly hours = 5 × 3 × 6 × 6 = 540
- Base FTE = 540 ÷ 40 = 13.5
- Relief factor = 1 ÷ 0.88 = 1.136
- Required FTE = 15.3, so plan to hire 16 nurses

If you hire only 13.5 FTE, every leave day becomes either overtime or a breached ratio. The calculator makes that visible to finance before the first month goes wrong.

## The competency matrix

| Staff | Role | License expiry | Cannulation AVF | CVC care | Isolation | Machine setup | Emergency response | Restrictions | Reassess |
|---|---|---|---|---|---|---|---|---|---|
| RN A | Staff nurse | 2027-06 | Signed | Signed | Signed | Signed | BLS 2026-08 | None | 2027-01 |
| RN B | New hire | 2028-02 | Supervised only | Signed | Not yet | Signed | BLS 2026-10 | No solo new fistula | 2026-12 |

Rules: a skill counts only when signed by a qualified assessor with a date. "Supervised only" means the person needs a named supervisor on that shift. Restrictions appear on the daily roster, not just in the HR file.

## Doing it on Monday: reallocating after an absence

1. Recompute positions for each shift with the absent person removed.
2. Check who is available: off-duty staff who have had adequate rest, part-timers, a float pool or an agency with verified credentials.
3. Match competencies to the stations that need cover. The isolation area and new patients need your strongest available people.
4. If you still cannot meet the ceiling, reduce stations for that shift and reschedule patients within the treatment window (see Module 04). Do not stretch the ratio.
5. Record the change, the approver (nursing lead) and the time.

## Field case: the competent but exhausted nurse

**Situation.** Saturday evening shift. One nurse is ill. The only available replacement has just finished a 12-hour hospital shift elsewhere and offers to stay.

**Problem.** She is competent but has not rested. Fatigue degrades vigilance in ways the person cannot self-assess.

**Solution.** The head nurse declines the offer, reduces the evening shift from 12 to 8 stations, and moves four stable patients to Sunday morning with their attending's agreement. The manager logs the gap and presents a float-pool proposal at the next budget meeting, with the CALC-01 output showing the unit was staffed at 13.5 FTE against a requirement of 15.3.

## Common failure modes

- Counting a person as "staff" because they are in the building, not because they are competent for that station.
- Planning FTEs with no relief factor, which guarantees chronic overtime.
- Competency records kept by HR but invisible on the floor.
- Treating 1:4 as the goal rather than the limit.

## Supervised practice

- [ ] Run CALC-01 for your unit and compare the result with your actual headcount.
- [ ] Build the competency matrix for every clinical staff member, with restrictions shown on the roster.
- [ ] Reallocate a fictional roster after two absences, with the nursing lead approving.
- [ ] Identify which shifts in the past month exceeded the ratio or relied on unrested staff.

## Question bank

**Q1.** The DOH nurse-to-station figure of 1:4 is best understood as:
- [x] A ceiling that must be tightened for acuity, isolation and breaks
- [ ] The ideal target for every shift
- [ ] A suggestion with no regulatory weight
- [ ] Applicable only to hospital units
> The figure sets the minimum cover. Real conditions often require more.

**Q2.** Fifteen stations are in use. How many POD positions does the 1:15 ceiling require at minimum?
- [x] One
- [ ] Two
- [ ] Three
- [ ] None if the attending is reachable by phone
> ceiling(15 ÷ 15) = 1. A POD must be present during operating hours.

**Q3.** What does a relief factor account for?
- [x] Leave, holidays, training and sick time that reduce productive hours
- [ ] Overtime premiums
- [ ] Patient no-shows
- [ ] Machine downtime
> Relief converts positions into the number of people needed to fill them reliably.

**Q4.** Non-productive time is 20%. What is the relief factor?
- [x] 1.25
- [ ] 1.20
- [ ] 0.80
- [ ] 1.50
> 1 ÷ (1 − 0.20) = 1.25.

**Q5.** In the 2024 US cohort study, the highest quartile of patient-to-technician ratio was associated with:
- [x] About 7% higher mortality and 5% higher hospitalization
- [ ] Lower mortality
- [ ] No change in any outcome
- [ ] Doubling of mortality
> IRR 1.07 for mortality and 1.05 for hospitalization, observational data.

**Q6.** Why can't the staffing study prove that adding staff improves survival?
- [x] It is observational, so other facility differences may explain the association
- [ ] It was too small
- [ ] It measured only costs
- [ ] It studied pediatric patients
> Association is not causation. Confounding cannot be fully excluded.

**Q7.** A new nurse's cannulation competency is marked "supervised only." On the roster you must:
- [x] Assign a named qualified supervisor on the same shift
- [ ] Let her cannulate alone if busy
- [ ] Hide the restriction to avoid embarrassment
- [ ] Remove her from all patient care
> Restrictions must be visible and supervised.

**Q8.** Who approves a reallocated nursing roster?
- [x] The nursing lead
- [ ] The billing clerk
- [ ] The vendor
- [ ] Any staff nurse
> Nursing assignment requires nursing authority.

**Q9.** Which patients need your strongest available staff after an absence?
- [x] Isolation patients and new starts
- [ ] The most talkative patients
- [ ] Patients with the longest dialysis vintage
- [ ] Those who arrive first
> These groups carry the highest procedural and clinical risk.

**Q10.** A tired nurse offers to work a second shift. The best decision is usually to:
- [x] Decline and reduce stations or reschedule safely
- [ ] Accept, since she is competent
- [ ] Accept, but give her the isolation area
- [ ] Ask her to sign a waiver
> Fatigue impairs performance in ways the person may not notice.

**Q11.** Under Labor Code Art. 83, health personnel in large cities or large facilities normally work:
- [x] 40 hours a week
- [ ] 48 hours a week in all settings
- [ ] 60 hours a week
- [ ] Unlimited hours
> HR must confirm which workers and facilities are covered.

**Q12.** A meta-analysis of 85 studies associated nurse burnout with:
- [x] More infections, falls and medication errors, and lower patient satisfaction
- [ ] Better patient safety
- [ ] No measurable effect
- [ ] Only lower salaries
> Burnout is consistently associated with worse safety and quality.

**Q13.** Fourteen non-isolation stations at 1:4 need how many nurse positions?
- [x] Four
- [ ] Three
- [ ] Five
- [ ] Two
> ceiling(14 ÷ 4) = 4.

**Q14.** When a competency counts on the matrix, it must be:
- [x] Signed and dated by a qualified assessor
- [ ] Claimed by the staff member
- [ ] Listed on the resume
- [ ] Approved by the owner
> Observed and signed skills are the proof.

**Q15.** If the ratio cannot be met even after calling replacements, you should:
- [x] Reduce stations for that shift and reschedule within the treatment window
- [ ] Run all stations at 1:6
- [ ] Ask patients to monitor each other
- [ ] Skip documentation to save time
> Capacity follows safe staffing, never the other way around.

## Sources

PH1, PH6, HR1, INT1, E1, E2, E13. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
