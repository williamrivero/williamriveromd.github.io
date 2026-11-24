# 17. Attendance, timekeeping and salary controls

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-17 (Understand) · FIG-17B (Apply) · FIG-17C (Appreciate) · **Calculator:** CALC-10 Premium pay (overtime, night differential, rest day and holiday)

> **Why this matters.** Dialysis units run early mornings, late evenings, Sundays and holidays, often across midnight. That makes the payroll unusually complex: overtime, night differential, rest-day and holiday premiums can all apply to one shift. Underpay staff and you lose them and face labor complaints. Overpay through errors and you erode the budget that funds safe staffing. Accurate timekeeping is a retention tool.

## Learning objectives

1. Keep the published roster, actual time, approved leave and corrections as separate, auditable records.
2. Compute overtime, night differential, rest-day and holiday premiums for covered private employees.
3. Apply the correct regional wage order and identify which workers the hours-of-work rules cover.
4. Reconcile an approved payroll register to time records, headcount, bank disbursement and the ledger.

## The model: four records, never merged

1. **Published roster:** what was planned.
2. **Actual time:** biometric or log entries of time in and out, with breaks.
3. **Approved changes:** shift swaps, leave, overtime authorizations, each approved before or promptly after.
4. **Corrections:** missing punches or errors, with evidence, employee acknowledgment and reviewer sign-off.

Payroll computes from actual time plus approved changes and corrections, never from the roster alone. The original records are preserved. A correction is a new entry, not an overwrite.

**Separate coverage decisions from pay decisions.** The head nurse decides who covers a shift. HR and payroll decide how it is paid under policy and law. Mixing them invites favoritism complaints.

## The legal frame (private sector; verify each item with HR)

**Coverage.** Book III of the Labor Code on hours of work covers rank-and-file employees. Managerial employees and certain officers are excluded from the hours-of-work and premium provisions (Art. 82). HR classifies each position.

**Health personnel.** Under Art. 83, health personnel in cities and municipalities of at least one million people, or in hospitals and clinics of at least 100 beds, normally work eight hours a day, five days a week. Where service needs require a sixth day, they are entitled to at least 30% additional compensation for the sixth day. HR confirms whether your facility and each worker fall under this rule.

**Minimum wage.** Regional wage boards set minimum wages. In the National Capital Region, Wage Order NCR-28 raised the non-agricultural daily minimum from ₱695 to ₱755, effective September 26, 2026, while the earlier Wage Order NCR-27 remained under litigation. Units in Central Luzon or elsewhere follow their own regional order. Check the National Wages and Productivity Commission for the current order and effective date before each payroll that crosses a change.

**Premiums (standard Labor Code rules for covered employees):**

| Situation | Pay for first 8 hours | Overtime hourly rate |
|---|---|---|
| Ordinary workday | 100% | 125% of hourly rate |
| Rest day or special non-working day, worked | 130% | 130% of the day's hourly rate (169% of basic) |
| Special day falling on rest day, worked | 150% | 130% of the day's hourly rate (195% of basic) |
| Regular holiday, worked | 200% | 130% of the day's hourly rate (260% of basic) |
| Regular holiday falling on rest day, worked | 260% | 130% of the day's hourly rate (338% of basic) |
| Regular holiday, not worked (covered employee) | 100% | — |
| Night differential (10 PM to 6 AM) | +10% of the applicable hourly rate for each night hour | |

Collective agreements and company policy may be more generous, never less. DOLE publishes a holiday pay advisory each year with the list of regular and special days.

**Government units** follow Civil Service Commission and DBM rules, salary grades and agency policy, not the Labor Code premium table. Confirm with the agency's HR.

## Calculator CALC-10: premium pay

**Inputs:** daily basic rate, regular hours per day (default 8), day type (ordinary, rest day, special day, special on rest day, regular holiday, regular holiday on rest day), hours worked, overtime hours, hours worked between 10 PM and 6 AM, sixth-day health-personnel flag.

**Formulas**

- Hourly rate = daily rate ÷ 8
- Day multiplier (m) from the table above (ordinary 1.00; rest or special 1.30; special on rest day 1.50; regular holiday 2.00; regular holiday on rest day 2.60)
- Regular pay for the day = hourly rate × m × regular hours worked (up to 8)
- Overtime pay = hourly rate × m × OT factor × OT hours, where OT factor is 1.25 on an ordinary day and 1.30 on other days
- Night differential = 10% × (hourly rate × m) × night hours (applied to the overtime rate for night overtime hours)
- Health-personnel sixth-day addition = 30% × daily rate, if applicable

**Worked example.** Daily rate ₱800 (hourly ₱100).
- Ordinary day, 2 hours overtime: 2 × 100 × 1.25 = ₱250
- Four night hours on an ordinary day (10 PM to 2 AM): 4 × 100 × 0.10 = ₱40
- Regular holiday, 8 hours worked: 8 × 100 × 2.00 = ₱1,600
- Rest day, 8 hours worked: 8 × 100 × 1.30 = ₱1,040

The calculator shows each component separately so that staff can check their payslips.

## Cutoff review

Before each payroll cutoff:

1. Compare actual time to roster for every staff member.
2. Resolve missing punches with evidence, not memory.
3. Verify overtime against approvals.
4. Confirm leave against approved requests and balances.
5. Check cross-midnight shifts are dated correctly (night differential and holiday rules depend on the calendar date of each hour).
6. Send unresolved items to HR before cutoff, not after payment.

## Payroll register reconciliation

Gross pay − authorized employee deductions (SSS, PhilHealth, Pag-IBIG employee shares, withholding tax, approved loans) = net pay. Then reconcile:

- register headcount to active employee list (no ghost employees);
- total hours to time records;
- net pay total to the bank disbursement file;
- employer shares and payroll cost to the ledger (Module 18 covers remittances);
- this period to last period, explaining material changes.

Separate preparation, approval and release of payroll.

## What the evidence shows

Payroll controls are legal and accounting requirements rather than clinical interventions. The link to care is indirect but real: fair, accurate pay supports retention, and turnover is associated with weaker competency and safety (Module 15). Nurse burnout meta-analyses consistently list perceived unfairness and workload among its drivers (Li et al., *JAMA Network Open* 2024).

## Field case: the holiday that crossed midnight

**Situation.** A nurse works 6:00 PM on December 24 to 2:00 AM on December 25. Payroll pays the whole shift at ordinary rates.

**Correct treatment.** December 24 is often declared a special non-working day, and December 25 is a regular holiday. Hours on each date take that date's multiplier. Hours from 10 PM to 2 AM also earn night differential. The manager reviews the DOLE holiday advisory for that year, recomputes with CALC-10, and has payroll issue an adjustment with a written explanation to the nurse.

## Common failure modes

- Paying from the roster rather than actual time.
- Overwriting time records instead of adding corrections.
- Applying last year's wage order after a new one took effect.
- Treating supervisors as exempt without HR classification.

## Supervised practice

- [ ] Audit one cutoff period: roster versus actual time versus approvals for five staff.
- [ ] Recompute three holiday or night shifts with CALC-10 and compare with payroll.
- [ ] Confirm the current wage order and effective date for your region.
- [ ] Reconcile one payroll register to the bank file and the ledger.

## Question bank

**Q1.** Payroll should be computed from:
- [x] Actual time plus approved changes and corrections
- [ ] The published roster alone
- [ ] Staff estimates at month-end
- [ ] Last month's payroll
> The roster is a plan, not a record of work.

**Q2.** Hourly rate ₱100; 3 overtime hours on an ordinary day. Overtime pay?
- [x] ₱375
- [ ] ₱300
- [ ] ₱390
- [ ] ₱600
> 3 × 100 × 1.25 = 375.

**Q3.** Night differential applies to hours worked:
- [x] Between 10 PM and 6 AM
- [ ] Between 6 PM and midnight
- [ ] On weekends only
- [ ] Only on holidays
> Art. 86 defines the night period.

**Q4.** Hourly ₱100; four night hours on an ordinary day. Night differential?
- [x] ₱40
- [ ] ₱400
- [ ] ₱10
- [ ] ₱125
> 4 × 100 × 0.10 = 40.

**Q5.** Pay for 8 hours worked on a regular holiday at a daily rate of ₱800 is:
- [x] ₱1,600
- [ ] ₱800
- [ ] ₱1,040
- [ ] ₱2,080
> 200% of the daily rate.

**Q6.** Pay for 8 hours worked on a rest day at ₱800 a day is:
- [x] ₱1,040
- [ ] ₱800
- [ ] ₱1,600
- [ ] ₱1,200
> 130% of the daily rate.

**Q7.** Under Wage Order NCR-28, the NCR non-agricultural daily minimum wage became:
- [x] ₱755, effective September 26, 2026
- [ ] ₱695
- [ ] ₱645
- [ ] ₱1,000
> Confirm current orders before each payroll.

**Q8.** Health personnel covered by Art. 83 who work a sixth day are entitled to:
- [x] At least 30% additional compensation for the sixth day
- [ ] No additional pay
- [ ] Double pay for the whole week
- [ ] A day off only
> HR confirms coverage by facility and worker.

**Q9.** A missing time punch should be corrected:
- [x] With evidence, employee acknowledgment and reviewer sign-off as a new entry
- [ ] By overwriting the record from memory
- [ ] By deleting the day
- [ ] By paying nothing
> Corrections must be auditable.

**Q10.** Managerial employees are generally:
- [x] Excluded from Labor Code hours-of-work and premium provisions
- [ ] Entitled to double premiums
- [ ] Paid hourly only
- [ ] Covered by PhilHealth rates
> HR classifies positions under Art. 82.

**Q11.** A shift runs from December 24, 6 PM, to December 25, 2 AM. Premiums are applied:
- [x] According to the calendar date of each hour worked
- [ ] Using the start date for the whole shift
- [ ] Using the end date for the whole shift
- [ ] Not at all
> Each hour takes that date's multiplier.

**Q12.** A ghost employee is detected by reconciling:
- [x] Register headcount to the active employee list
- [ ] Water logs to machine logs
- [ ] Patient lists to claims
- [ ] Budget to rent
> Every paid person must be an active employee.

**Q13.** Who decides who covers a shift, and who decides pay?
- [x] Nursing lead decides coverage; HR and payroll decide pay under policy
- [ ] The owner decides both
- [ ] The staff member decides both
- [ ] Payroll decides coverage
> Separating them reduces favoritism disputes.

**Q14.** Government dialysis staff premiums are determined by:
- [x] CSC, DBM and agency rules under their appointment
- [ ] The private-sector Labor Code table
- [ ] PhilHealth circulars
- [ ] Vendor contracts
> Public-sector rules differ.

**Q15.** Gross pay minus authorized employee deductions equals:
- [x] Net pay
- [ ] Employer cost
- [ ] Overtime
- [ ] Taxable income
> Employer shares are tracked separately.

## Sources

HR1, HR2, HR3, HR4, PH9, E13. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
