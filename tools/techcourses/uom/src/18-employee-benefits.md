# 18. Employee benefits, leave, and payroll remittances

## The big picture

{{plain:Every month, a small part of each staff member's pay goes into three savings jars kept by the government: the Social Security System (SSS), PhilHealth, and Pag-IBIG. The unit adds its own share. Those jars pay for a nurse's maternity leave, her hospital bill, her housing loan, and one day her pension. Your job is to make sure every peso deducted actually lands in the right person's jar.}}

The picture has a limit. A jar is something you can look into. These are not. A staff member usually discovers a missing contribution only when she applies for a loan or a benefit, months later, and is told her record shows nothing. By then the unit has already paid; the money went somewhere, but not to her. Reconciliation is how you look into the jar before she has to.

This module covers the current contribution rules, the leaves the law requires, 13th-month pay, and the monthly check that catches posting errors before a staff member does.

{{cards:Key terms for this module|Monthly salary credit (MSC)::The salary bracket SSS uses to compute contributions.|Employee share::The part of a contribution deducted from pay.|Employer share::The part the unit adds on top.|Remittance::Paying the deducted and employer shares to the agency.|Posting::The agency crediting the payment to each employee's record.|13th-month pay::One-twelfth of the basic salary earned in the year, paid by December 24.|Service incentive leave::Five days of paid leave a year after one year of service, for covered employees.|Final pay::Everything owed to an employee who leaves.}}

## Learning objectives

1. Build a benefits matrix by employment category covering statutory leaves, 13th-month pay and contributions.
2. Compute SSS, PhilHealth and Pag-IBIG employee and employer shares and 13th-month pay for a sample salary.
3. Reconcile payroll deductions and employer shares to remittance records and agency posting.
4. Process leave confidentially, without exposing diagnoses on rosters.

## Field case: deducted but not posted

**Situation.** Mr. Jayson Manalastas, a dialysis technician at a 14-station unit in Tarlac City, applies for an SSS salary loan in June to repair his roof before the rainy season. SSS tells him his record shows no contributions for January through April. His payslips show the deductions every month.

He comes to the manager, Ms. Rowena Dizon, upset and a little suspicious: "Ma'am, where did my money go?"

**Before reading on, decide:**

- What three records would you compare to find the answer?
- What should Ms. Dizon say to Mr. Manalastas today?
- How would you find out whether anyone else is affected?

**Case review.**

**Today.** Ms. Dizon does not guess and does not defend the unit. She says: "Your payslips show the deductions, so you are right to ask. I will find out where the money went and tell you by Friday."

**The records.** She compares three things: the payroll register (what was deducted and added), the payment confirmations (what was remitted), and the SSS employer report and posting record (what SSS credited to whom). The remittances were paid on time and in full. But Mr. Manalastas was hired in December, and his SSS number was typed into the employer report with two digits reversed. His contributions posted to a number that belongs to no one.

**The fix.** Payroll files the correction with SSS, with his ID and the payment records. His four months are posted within three weeks, and he gets his loan. Ms. Dizon then checks every employee's posting record, not just the totals, for the last 12 months. She finds one more error: a nurse whose PhilHealth record shows the wrong employer. It is fixed the same month.

**The system.** The monthly reconciliation now compares agency posting reports with the payroll register for every employee by name, and new hires' agency numbers are checked against their ID cards on their first day.

{{fig:uom18c}}

## The model: deduct, add, remit, reconcile

{{fig:uom18a}}

{{flow:Every month, for each agency|Deduct::Payroll deducts each employee's share.|Add::The unit adds the employer share.|Remit::Both shares are paid to the agency by its deadline.|Reconcile::What was remitted is checked against what the agency posted to each employee's record.}}

Any break in that chain becomes a staff member's complaint months later.

## Current statutory figures (confirm before each payroll year)

| Program | Rate and split | Base and limits | Source |
|---|---|---|---|
| SSS | 15% of the MSC: employer 10%, employee 5%; plus the employer's Employees' Compensation premium (10 pesos if the MSC is below 15,000, 30 pesos otherwise) | MSC from 5,000 to 35,000 pesos, in brackets | SSS schedule effective January 2025[[uom_sss2025]] |
| PhilHealth | 5% of monthly basic salary, shared equally | Floor 10,000 pesos (premium 500); ceiling 100,000 pesos (premium 5,000) | PhilHealth Advisory 2025-0002[[uom_ph_pa2025]] (reported unchanged for 2026; confirm) |
| Pag-IBIG | Employee 1% (pay of 1,500 pesos or less) or 2%; employer 2% | Maximum fund salary 10,000 pesos (200 pesos each) | Pag-IBIG Circular 460, effective February 2024[[uom_hdmf460]] |
| 13th-month pay | Basic salary earned in the calendar year ÷ 12, paid on or before December 24 | Rank-and-file private employees, whatever their designation or employment status, subject to listed exemptions | PD 851[[uom_pd851]] and the DOLE advisory for the year |
| Tax on 13th-month pay and other benefits | Exempt up to 90,000 pesos combined | The excess is taxable | Tax Reform for Acceleration and Inclusion (TRAIN) law (RA 10963) |

Contribution tables, rates, and limits change by law, circular, or board resolution. These figures are the November 2026 baseline.

## Statutory leaves (private sector; human resources confirms eligibility)

{{fig:uom18b}}

| Leave | Entitlement | Law |
|---|---|---|
| Service incentive leave | 5 paid days a year after one year of service, with exemptions such as establishments with fewer than 10 employees or workers already given at least 5 days of paid leave | Labor Code Art. 95 |
| Maternity leave | 105 paid days for a live birth, plus 15 days for solo mothers; up to 7 days can be given to the father or another caregiver; 60 days for miscarriage or emergency termination | RA 11210[[uom_ra11210]] |
| Paternity leave | 7 paid days for married male employees, for the first four deliveries of the legitimate spouse | RA 8187 |
| Solo parent leave | 7 working days a year after six months of service | RA 11861 |
| Special leave for women | Up to 2 months at full pay after surgery for gynecological disorders, with qualifying service | RA 9710 |
| Leave for victims of violence against women and children | Up to 10 paid days | RA 9262 |

Company policy and collective agreements may add vacation, sick, and emergency leave. **Government employees** follow Civil Service Commission leave rules and are covered by the Government Service Insurance System instead of SSS.

## Calculator CALC-11: statutory contributions and 13th-month pay

You need: monthly basic salary, basic salary earned so far this year (or months worked), employee category (private or government), and other non-taxable benefits already paid this year.

{{formula:**SSS MSC** = salary rounded to its 500-peso bracket, from 5,000 to 35,000 (use the official table for edge cases).<br>**SSS employee** = 5% × MSC. **SSS employer** = 10% × MSC + Employees' Compensation (10 or 30 pesos).<br>**PhilHealth total** = 5% × basic salary, kept between 10,000 and 100,000; each side pays half.<br>**Pag-IBIG employee** = 1% (if basic is 1,500 or less) or 2% × basic, up to 10,000. **Pag-IBIG employer** = 2% × basic, up to 10,000.<br>**13th-month pay** = basic salary earned in the year ÷ 12.<br>**Taxable part** = 13th-month pay + other benefits − 90,000, if positive.}}

**Worked example.** A nurse earns a monthly basic salary of 30,000 pesos and is employed all year.

- SSS: MSC 30,000; employee 1,500; employer 3,000 + 30 = 3,030 pesos
- PhilHealth: 5% × 30,000 = 1,500; employee 750; employer 750 pesos
- Pag-IBIG: employee 200; employer 200 pesos
- Total employee deductions before tax: 1,500 + 750 + 200 = 2,450 pesos
- Total employer share: 3,030 + 750 + 200 = 3,980 pesos
- 13th-month pay: 360,000 ÷ 12 = 30,000 pesos, fully within the 90,000-peso exemption if other benefits are small

**A budget note.** The employer share adds about 13% to this nurse's monthly cost, and the 13th month adds another 8.3% of annual basic pay. A staffing budget that uses basic salary alone understates the real cost by about one-fifth (Module 11).

{{key:Reconcile every employee by name, every month. Totals that match can hide a person whose money posted to no one.}}

## Remittance reconciliation

For each agency, every month:

1. Total employee deductions and employer shares from the payroll register.
2. The amount remitted, from the payment confirmation.
3. The amount posted, from the agency's employer report or portal, by employee.
4. Every difference explained and corrected. New hires and separations checked for the right start and end months.

Confirm current due dates and reporting systems, such as Pag-IBIG's electronic remittance requirements, with each agency for your employer type.

## Leave and confidentiality

Process leave through human resources with the documents the law or policy requires. The roster says "on leave," not "on leave for surgery" or a diagnosis. Medical certificates stay in human resources files with restricted access, under the Data Privacy Act (RA 10173).

**Example.** A unit in Malaybalay writes "SL – dengue" and "ML – CS delivery" on the roster board by the nurses' station, which patients and visitors pass all day. A patient's relative asks one nurse about her operation. The nurse, embarrassed, complains. The board now shows only "Leave," and the reason lives in the human resources file.

## Onboarding and separation

**Onboarding:** verify each agency number against the person's ID card, confirm enrollment, check that the first contribution month is correct, and explain benefits in writing.

**Separation:** the last contribution month; final pay (unpaid salary, prorated 13th-month pay, convertible leave, and other amounts due) computed and released within the period DOLE guidance sets, generally within 30 days unless a more favorable policy applies; a certificate of employment; the tax certificate (Bureau of Internal Revenue Form 2316); access removed and unit property returned.

{{call:When an employee reports a missing contribution or benefit, compare the payroll register, the remittance proof, and the agency posting record before responding, and give the employee a written answer with a date. If deductions were made but not remitted, notify the licensee in writing the same day.}}

## What the evidence shows

Benefit administration is a legal duty, not a clinical intervention. It touches care through trust and retention: unfairness and administrative failures recur in nurse turnover research, and turnover undermines competency (Module 15). The strongest evidence in this module is the law itself. Get the figures right, and keep the proof.

## Common failure modes

- **Totals only.** Individual posting errors hidden inside matching totals.
- **Basic-salary budgets.** Staff costs planned without employer shares and the 13th month.
- **Diagnoses on the board.** Medical reasons for leave visible to anyone walking by.
- **Final pay in months.** Departing staff waiting long after their last day.
- **Unchecked new-hire numbers.** One transposed digit, and four months of contributions vanish.

## Supervised practice

- [ ] Build a benefits matrix for three employment categories in your unit.
- [ ] Compute contributions and 13th-month pay for three sample salaries with CALC-11 and compare with payroll.
- [ ] Reconcile one month of remittances employee by employee for one agency.
- [ ] Review the roster and leave records for confidentiality.

## Question bank

**Q1.** The 2025 SSS contribution rate is:
- [x] 15% of MSC, 10% employer and 5% employee
- [ ] 12% shared equally
- [ ] 5% employee only
- [ ] 20% employer only
> RA 11199 reached its final step in January 2025.

**Q2.** The SSS maximum monthly salary credit from 2025 is:
- [x] ₱35,000
- [ ] ₱20,000
- [ ] ₱100,000
- [ ] ₱10,000
> The minimum MSC is ₱5,000.

**Q3.** PhilHealth premium for a ₱40,000 monthly basic salary at 5% is:
- [x] ₱2,000 total, ₱1,000 each
- [ ] ₱500 total
- [ ] ₱4,000 each
- [ ] ₱200 total
> 5% × 40,000 = 2,000, shared equally.

**Q4.** The maximum mandatory Pag-IBIG employee contribution is:
- [x] ₱200
- [ ] ₱100
- [ ] ₱1,000
- [ ] 2% of the full salary without cap
> 2% of the ₱10,000 maximum fund salary.

**Q5.** 13th-month pay equals:
- [x] Total basic salary earned in the year ÷ 12
- [ ] One month of gross pay including overtime
- [ ] Two weeks of pay
- [ ] Whatever the employer decides
> PD 851 uses basic salary.

**Q6.** 13th-month pay and other benefits are tax-exempt up to:
- [x] ₱90,000 combined
- [ ] ₱30,000
- [ ] ₱250,000
- [ ] No limit
> Excess is taxable under the TRAIN law.

**Q7.** Maternity leave for live birth under RA 11210 is:
- [x] 105 days paid
- [ ] 60 days
- [ ] 7 days
- [ ] 30 days
> Solo mothers receive 15 additional days.

**Q8.** Paternity leave under RA 8187 is:
- [x] 7 days paid
- [ ] 105 days
- [ ] 1 day
- [ ] 30 days
> For the first four deliveries of the legitimate spouse.

**Q9.** Service incentive leave is:
- [x] 5 days paid per year after one year of service, with exemptions
- [ ] 30 days per year
- [ ] Unpaid
- [ ] Only for managers
> Labor Code Art. 95.

**Q10.** Contributions were deducted but are not posted to an employee's SSS record. A likely cause is:
- [x] An error in the employee's identification number in the employer report
- [ ] The employee earning too much
- [ ] PhilHealth rules
- [ ] Water quality
> Individual posting checks catch these errors.

**Q11.** For a ₱30,000 salary, the SSS employer share including EC is:
- [x] ₱3,030
- [ ] ₱1,500
- [ ] ₱4,500
- [ ] ₱3,000
> 10% × 30,000 + ₱30 EC.

**Q12.** A roster should describe a staff member on medical leave as:
- [x] On leave
- [ ] On leave for surgery
- [ ] On leave with the diagnosis listed
- [ ] Absent without reason
> Health details are sensitive personal information.

**Q13.** Government dialysis staff are covered by:
- [x] GSIS and CSC leave rules under their appointment
- [ ] SSS and private Labor Code leaves
- [ ] No benefits
- [ ] PhilHealth leave only
> Public appointments follow public-sector rules.

**Q14.** Budgeting staff at basic salary alone underestimates cost because it omits:
- [x] Employer contributions and 13th-month pay
- [ ] Employee deductions
- [ ] Withholding tax
- [ ] Nothing
> Employer costs add roughly a fifth.

**Q15.** Remittance reconciliation should compare:
- [x] Payroll register, payments made and agency postings, employee by employee
- [ ] Only the bank total
- [ ] Only last year's totals
- [ ] Patient claims
> Totals can hide individual errors.

## Sources

HR1, HR2, HR3, HR4, PH10, PH11, PH12. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
