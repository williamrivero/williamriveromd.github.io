# 04. Capacity, access and patient flow

**Core** · 40 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-04 (Understand) · FIG-04B (Apply) · FIG-04C (Appreciate) · **Calculator:** CALC-02 Capacity, utilization and waitlist planner

> **Why this matters.** For a patient on maintenance hemodialysis, a missed session is not a scheduling inconvenience. Potassium, fluid and acid keep accumulating whether or not a chair is free. Every capacity decision you make, from how many shifts to run to who gets the last slot on a holiday, has a physiology attached to it.

## Learning objectives

1. Calculate weekly station capacity, patient slots and utilization for your unit.
2. Explain the physiology that makes missed, shortened and delayed sessions dangerous, and cite the evidence.
3. Run a fair, documented waitlist and referral acceptance process.
4. Reschedule patients after a disruption while keeping each within a clinically acceptable window.

## The physiology behind the schedule

Healthy kidneys work 168 hours a week. Thrice-weekly hemodialysis replaces that with about 12 hours, delivered in pulses. Between sessions, three things build up:

- **Potassium.** Dietary potassium enters the blood and, without kidney excretion, raises serum levels. Hyperkalemia slows cardiac conduction and can cause fatal arrhythmia without warning symptoms.
- **Fluid.** Every glass of water and every salty meal adds volume that the patient cannot excrete. Volume expands the blood compartment, raises blood pressure and, if large enough, floods the lungs.
- **Acid.** Metabolism produces hydrogen ions daily. Without renal excretion, bicarbonate is consumed and the patient becomes acidemic.

The **long interdialytic interval** (the two-day gap over the weekend in a Monday-Wednesday-Friday schedule) lets all three accumulate the longest. That is why the day after the long gap carries the highest risk, and why skipping a session effectively turns a two-day gap into a four-day gap.

## What the evidence shows

- **Missed sessions are associated with death.** In the international DOPPS cohort, skipping one or more sessions per month was associated with a 30% higher mortality risk (RR 1.30) (Saran et al., *Kidney International* 2003). Observational: patients who skip may differ in other ways, but the physiology makes the association plausible.
- **The long gap is dangerous.** In a large US cohort, deaths and cardiovascular hospitalizations clustered on the day after the long interdialytic interval (Foley et al., *NEJM* 2011).
- **Rescheduling helps, but only partly.** In a matched US cohort, a missed session was associated with a 2.09-fold higher hospitalization rate over the next 7 days. Attending a rescheduled session the next day lowered that excess to 1.68-fold but did not remove it (Cohen et al., *Kidney Medicine* 2020).
- **Shortened sessions matter too.** In DOPPS, treatment time longer than 240 minutes was associated with lower mortality (RR 0.81), and ultrafiltration rates above 10 mL/kg/h were associated with more intradialytic hypotension (Saran et al., *Kidney International* 2006). Observational again, but it tells you that "we'll just cut everyone to three hours today" is a clinical decision, not an operational one. It belongs to the attending nephrologist.

**Management translation:** your capacity plan should protect against skipped sessions first, long gaps second and shortened sessions third. Shortening a prescription is never your call.

## Philippine context

PhilHealth covers up to 156 maintenance HD sessions per calendar year for eligible, PDD-registered CKD stage 5 patients, explicitly based on three sessions a week for 52 weeks. Capacity planning that cannot deliver thrice-weekly treatment for every enrolled patient leaves benefits unused and patients under-dialyzed. Reported dialysis numbers rose from about 53,300 in 2023 to about 64,800 in 2024 (PRDR data as reported by NKTI; confirm the latest figures with the registry). Demand is growing faster than most units can add stations.

## Calculator CALC-02: capacity, utilization and waitlist

**Inputs:** stations (S), shifts per day (H), operating days per week (D), sessions per patient per week (default 3), sessions actually delivered last month, isolation stations reserved, patients on waitlist.

**Formulas**

- Weekly station-sessions available = S × H × D
- Patient slots at thrice weekly = floor(available ÷ 3)
- Utilization (%) = delivered sessions ÷ available station-sessions × 100
- Open slots = patient slots − current enrolled patients
- Weeks to clear waitlist = waitlist ÷ (expected new openings per week)

**Worked example.** Fifteen stations, three shifts, six days: 270 station-sessions per week, or 90 patient slots at three sessions each. With 84 enrolled patients, there are six open slots. If one isolation station is reserved and used only for two HBsAg-positive patients (six sessions a week out of 18 possible), 12 isolation station-sessions sit idle. That idle capacity is a design choice, so state it openly rather than counting it as available.

A utilization above about 95% leaves no room for make-up sessions after an outage. Plan a buffer.

## The waitlist and referral process

A fair waitlist is written, dated and ordered by criteria that the Medical Director approves, for example urgency (new start from hospital, catheter-dependent), date of request and continuity (existing patient changing shift). Record every referral with:

- date and time received, referring facility and contact;
- clinical summary and serology status (needed to decide isolation placement);
- PDD and payer status;
- decision, decision-maker and date;
- if declined, the reason and the alternative offered.

A unit that accepts patients informally, through personal connections, will eventually face a complaint it cannot defend.

## Rescheduling after a disruption

1. List affected patients and their last completed session.
2. Prioritize by risk: patients coming off the long gap, those with high potassium or heavy weight gain on the last session, catheter users and new starts.
3. Offer the earliest available slot. Run an extra shift if staffing allows.
4. For patients you cannot place within the clinical window, the POD or attending decides on transfer to a partner unit or a hospital.
5. Document every offer, acceptance and refusal.

## Field case: the holiday week

**Situation.** Christmas Day and New Year's Day fall on Fridays. Half the staff request leave. The owner proposes closing both Fridays.

**Problem.** Closing Friday gives Monday-Wednesday-Friday patients a gap from Wednesday to Monday, five days. Several have potassium values that were high-normal after a two-day gap.

**Solution.** The manager shifts the Friday patients to Thursday and Saturday the same week, runs an extended Saturday, offers holiday premium pay (see Module 17) to volunteers, and has the attending review the three highest-risk patients. No patient goes more than three days without treatment. The plan and patient notifications are sent two weeks in advance.

## Common failure modes

- Capacity counted in stations rather than station-sessions.
- Holiday closures planned by finance without clinical review.
- Referrals accepted by whoever answers the phone.
- "Short treatments for everyone" decided by the operations team.

## Supervised practice

- [ ] Run CALC-02 for your unit and present utilization, open slots and isolation capacity.
- [ ] Audit last month's missed sessions: count, reasons and whether each was rescheduled.
- [ ] Rebuild a holiday schedule so that no patient exceeds a three-day gap.
- [ ] Review five referrals against the written acceptance criteria.

## Question bank

**Q1.** Why is the day after the long interdialytic interval the riskiest?
- [x] Potassium, fluid and acid have accumulated for the longest time
- [ ] Staff are more tired on Mondays
- [ ] Machines need more maintenance on Mondays
- [ ] Patients eat less on weekends
> The two-day gap allows the largest buildup of solutes and volume.

**Q2.** In DOPPS, skipping at least one session a month was associated with:
- [x] About 30% higher mortality risk
- [ ] Lower mortality
- [ ] No difference
- [ ] A tenfold mortality increase
> RR 1.30 in an observational cohort.

**Q3.** A unit has 12 stations, 3 shifts and 6 days. How many weekly station-sessions are available?
- [x] 216
- [ ] 72
- [ ] 108
- [ ] 36
> 12 × 3 × 6 = 216.

**Q4.** How many thrice-weekly patients can 216 station-sessions support?
- [x] 72
- [ ] 216
- [ ] 36
- [ ] 108
> 216 ÷ 3 = 72.

**Q5.** Who decides to shorten a patient's treatment time?
- [x] The attending nephrologist
- [ ] The operations manager
- [ ] The billing officer
- [ ] The patient's relative
> Treatment time is part of the prescription.

**Q6.** What did research show about rescheduling a missed session to the next day?
- [x] It reduced but did not fully eliminate the excess risk
- [ ] It removed all risk
- [ ] It increased risk
- [ ] It was never studied
> Next-day treatment helps, but the missed session still carries harm.

**Q7.** Utilization is 98%. What is the main operational concern?
- [x] No buffer for make-up sessions after an outage
- [ ] Too many idle machines
- [ ] Excess staff
- [ ] Lower PhilHealth rates
> Very high utilization leaves no slack for disruptions.

**Q8.** PhilHealth's 156-session annual cap is based on:
- [x] Three sessions a week for 52 weeks
- [ ] Two sessions a week
- [ ] Monthly averages from 2015
- [ ] The number of stations per unit
> The package was set to match thrice-weekly dialysis.

**Q9.** Which detail is essential before placing a referred patient on a station?
- [x] Serology status, to decide whether isolation is needed
- [ ] Their favorite television program
- [ ] The referring doctor's hobbies
- [ ] Their home's floor area
> Bloodborne virus status determines station and staff assignment.

**Q10.** In DOPPS, treatment times longer than 240 minutes were associated with:
- [x] Lower mortality
- [ ] Higher mortality
- [ ] More infections
- [ ] No association
> RR 0.81, observational data.

**Q11.** A holiday closure would create a five-day gap for some patients. The best response is to:
- [x] Move their sessions to adjacent days so no gap exceeds three days
- [ ] Close and advise patients to drink less
- [ ] Shorten sessions all week
- [ ] Ask patients to go to the emergency room
> Rescheduling keeps the interval clinically acceptable.

**Q12.** Which patients get first priority after an outage?
- [x] Those coming off the long gap, with high potassium, or catheter-dependent
- [ ] Those with the most visitors
- [ ] Those who complain most
- [ ] Those with private insurance
> Prioritize by physiologic risk.

**Q13.** Why should referral decisions be documented with reasons?
- [x] To make acceptance fair and defensible
- [ ] To increase paperwork
- [ ] Only for public units
- [ ] Because PhilHealth pays per page
> Written criteria protect patients and the unit.

**Q14.** An isolation station used for only two patients represents:
- [x] Idle capacity that should be stated openly in planning
- [ ] Capacity available for any patient
- [ ] A licensing violation
- [ ] A billing error
> Isolation capacity is reserved by design and should not be counted as open.

**Q15.** Ultrafiltration rates above 10 mL/kg/h were associated in DOPPS with:
- [x] More intradialytic hypotension
- [ ] Better blood pressure control
- [ ] Lower mortality
- [ ] Fewer cramps
> Fast fluid removal outpaces vascular refilling.

## Sources

PH1, PH4, PH8, E3, E4, E5, E6, E19. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
