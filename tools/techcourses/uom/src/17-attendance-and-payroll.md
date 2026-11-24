# 17. Attendance, timekeeping, and salary controls

## The big picture

{{plain:A payslip is a story about a nurse's month: the shifts she was scheduled for, the hours she actually worked, the swaps and overtime someone approved, and the corrections made when the biometric missed her thumb. If any part of that story is lost or rewritten, the payslip is wrong, and she will know it before you do.}}

The picture has a limit. A story can be retold; time records should not be. Once the actual hours are recorded, they stay as recorded. A mistake is fixed by adding a correction with evidence, not by quietly changing the original. That is what makes the payslip something staff can check and auditors can trust.

Pay is not a clinical topic, but it is a safety topic. Nurses who are underpaid for holiday shifts stop volunteering for them. Units that cannot fill holiday shifts close them, and patients go longer between treatments (Module 4). This module keeps that chain from breaking.

{{cards:Key terms for this module|Roster::The published schedule: what was planned.|Actual time::Biometric or logbook entries of time in and out.|Approved change::A swap, leave, or overtime authorized before, or promptly after.|Correction::A new entry that fixes an error, with evidence and sign-off. Never an overwrite.|Premium pay::Extra pay for overtime, night hours, rest days, and holidays.|Night differential::An extra 10% for each hour worked between 10 PM and 6 AM.|Wage order::The regional minimum wage set by the regional wage board.|Payroll register::The list of every employee's gross pay, deductions, and net pay for the period.}}

## Learning objectives

1. Keep the published roster, actual time, approved leave and corrections as separate, auditable records.
2. Compute overtime, night differential, rest-day and holiday premiums for covered private employees.
3. Apply the correct regional wage order and identify which workers the hours-of-work rules cover.
4. Reconcile an approved payroll register to time records, headcount, bank disbursement and the ledger.

## Field case: the holiday that crossed midnight

**Situation.** At a 15-station unit in Imus, Cavite, Nurse Cherry Mae Aquino works the extended Christmas Eve shift, from 18:00 on December 24 to 02:00 on December 25. She volunteered so that patients would not miss their sessions over the holiday.

On January 10, her payslip shows the whole eight hours at her ordinary rate. She brings it to the manager, Mr. Paolo Esguerra, and says quietly: "Sir, I don't think this is right. And I don't think I will volunteer next year."

**Before reading on, decide:**

- Which rules apply to which hours of her shift?
- Who should recompute it, and what should Nurse Aquino receive in writing?
- How would you make sure the system gets it right next year?

**Case review.**

**The hours.** Pay rules follow the calendar date of each hour, not the date the shift started. December 24 is often declared a special non-working day, and December 25 is a regular holiday; check the Department of Labor and Employment (DOLE) holiday advisory for that year. The six hours on December 24 take that day's rate. The two hours on December 25 take the regular holiday rate, 200%. The four hours from 22:00 to 02:00 also earn night differential.

**The correction.** Mr. Esguerra sends the time record and the advisory to payroll. Payroll recomputes with Calculator CALC-10 and issues an adjustment in the next payroll, with a written breakdown showing each component. Nurse Aquino can check every line.

**The system.** The payroll software split shifts by start date. The cutoff review (below) now includes a specific check for shifts that cross midnight on or near holidays. In December, Mr. Esguerra sends staff the holiday rates in advance. Nurse Aquino volunteers again.

{{fig:uom17c}}

## The model: four records, never merged

{{fig:uom17a}}

1. **Published roster:** what was planned.
2. **Actual time:** biometric or logbook entries of time in and out, with breaks.
3. **Approved changes:** shift swaps, leave, and overtime, each approved before, or promptly after.
4. **Corrections:** missing punches or errors, with evidence, the employee's acknowledgment, and a reviewer's sign-off.

Payroll is computed from actual time plus approved changes and corrections, never from the roster alone. The originals are kept. A correction is a new entry, not an overwrite.

**Keep coverage and pay decisions apart.** The head nurse decides who covers a shift. Human resources and payroll decide how it is paid, under policy and law. Mixing the two invites complaints of favoritism.

{{key:Pay from what happened, not from what was planned. Fix errors by adding, never by overwriting.}}

## The legal frame (private sector; confirm each item with human resources)

**Who is covered.** Book III of the Labor Code on hours of work covers rank-and-file employees. Managerial employees and certain officers are excluded from the hours-of-work and premium provisions (Article 82).[[uom_laborcode]] Human resources classifies each position.

**Health personnel.** Under Article 83, health personnel in cities and municipalities of at least one million people, or in hospitals and clinics of at least 100 beds, normally work eight hours a day, five days a week. When service needs require a sixth day, they are entitled to at least 30% additional pay for that day. Human resources confirms whether your facility and each worker fall under this rule.

**Minimum wage.** Regional wage boards set minimum wages. In the National Capital Region, Wage Order NCR-28 raised the non-agricultural daily minimum from 695 to 755 pesos, effective September 26, 2026, while the earlier Wage Order NCR-27 remained under litigation.[[uom_wo_ncr28]] Units in Central Luzon or elsewhere follow their own regional order. Check the National Wages and Productivity Commission before each payroll that crosses a change.

**Premiums for covered employees (standard Labor Code rules):**

| Situation | Pay for the first 8 hours | Overtime hourly rate |
|---|---|---|
| Ordinary workday | 100% | 125% of the hourly rate |
| Rest day or special non-working day, worked | 130% | 130% of the day's hourly rate (169% of basic) |
| Special day falling on a rest day, worked | 150% | 130% of the day's hourly rate (195% of basic) |
| Regular holiday, worked | 200% | 130% of the day's hourly rate (260% of basic) |
| Regular holiday falling on a rest day, worked | 260% | 130% of the day's hourly rate (338% of basic) |
| Regular holiday, not worked (covered employee) | 100% | Not applicable |
| Night differential (10 PM to 6 AM) | An extra 10% of the applicable hourly rate for each night hour | |

Collective agreements and company policy may be more generous, never less. DOLE publishes a holiday pay advisory each year with the list of regular and special days.

**Government units** follow Civil Service Commission and Department of Budget and Management rules, salary grades, and agency policy, not this table. Confirm with the agency's human resources office.

## Calculator CALC-10: premium pay

You need: the daily basic rate, regular hours per day (usually 8), the day type, hours worked, overtime hours, hours worked between 10 PM and 6 AM, and whether the sixth-day rule for health personnel applies.

{{formula:**Hourly rate** = daily rate ÷ 8.<br>**Day multiplier**: ordinary 1.00; rest day or special day 1.30; special day on a rest day 1.50; regular holiday 2.00; regular holiday on a rest day 2.60.<br>**Regular pay** = hourly rate × multiplier × regular hours (up to 8).<br>**Overtime pay** = hourly rate × multiplier × overtime factor × overtime hours (factor 1.25 on an ordinary day, 1.30 on other days).<br>**Night differential** = 10% × hourly rate × multiplier × night hours.<br>**Sixth-day addition for health personnel** = 30% × daily rate, if it applies.}}

**Worked example.** A daily rate of 800 pesos gives an hourly rate of 100 pesos.

- Ordinary day, 2 hours of overtime: 2 × 100 × 1.25 = 250 pesos
- Four night hours on an ordinary day, 10 PM to 2 AM: 4 × 100 × 0.10 = 40 pesos
- Regular holiday, 8 hours worked: 8 × 100 × 2.00 = 1,600 pesos
- Rest day, 8 hours worked: 8 × 100 × 1.30 = 1,040 pesos

The calculator shows each component separately so that staff can check their own payslips.

## Cutoff review

{{fig:uom17b}}

{{flow:Before each payroll cutoff|Compare::Actual time against the roster for every staff member.|Resolve::Missing punches with evidence, not memory.|Verify::Overtime against approvals.|Confirm::Leave against approved requests and balances.|Date::Shifts that cross midnight, especially near holidays, split by the calendar date of each hour.|Escalate::Unresolved items go to human resources before cutoff, not after payment.}}

**Example.** During a cutoff review at a unit in Bulacan, the manager finds that a technician has 22 hours of overtime with no approval on file, all on Saturdays. The technician is not hiding anything. The Saturday water disinfection takes three hours longer than the shift allows, and he has been staying to finish it. The overtime is approved retroactively with a note, and the biomedical lead adjusts the disinfection schedule so the work fits the shift. The review found a planning problem, not a pay problem.

## Payroll register reconciliation

Gross pay minus authorized employee deductions (Social Security System, PhilHealth, and Pag-IBIG employee shares, withholding tax, approved loans) equals net pay. Then reconcile:

- register headcount against the active employee list, so there are no ghost employees;
- total hours against the time records;
- the net pay total against the bank disbursement file;
- employer shares and payroll cost against the ledger (Module 18 covers remittances);
- this period against the last, explaining material changes.

Keep preparation, approval, and release of payroll with different people.

{{call:When a payroll error affects a staff member's pay, correct it in the next payroll at the latest and give the employee a written breakdown. When you suspect a ghost employee or altered time records, secure the records and notify the licensee and the accountant in writing.}}

## What the evidence shows

Payroll controls are legal and accounting requirements, not clinical interventions. The link to care is indirect but real: fair, accurate pay supports retention, and turnover is associated with weaker competency and safety (Module 15). Nurse burnout studies consistently list perceived unfairness and workload among its drivers.[[uom_li2024]]

## Common failure modes

- **Paying the plan.** Pay computed from the roster instead of actual time.
- **Overwriting.** Time records changed instead of corrected.
- **Last year's wage.** An old wage order applied after a new one took effect.
- **"Supervisors don't get overtime."** Positions treated as exempt without classification.
- **Midnight blindness.** Holiday shifts split by start date instead of by the hour.

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
