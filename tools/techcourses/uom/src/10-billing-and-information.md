# 10. PhilHealth claims, documentation, and privacy

## The big picture

{{plain:A PhilHealth claim is the last car of a train. In front of it are the eligibility check, the signed treatment record, the claim forms, the billing review, and the submission. If any car is missing, the claim is pulling air. The claim can only be as good as the record behind it.}}

The picture has a limit. A train runs one way. In billing, errors often start at the end, in a template or a batch upload, and then travel backward when someone "fixes" the chart to match the claim. The rule runs in one direction only: the claim follows the record, never the reverse.

This module covers how the PhilHealth hemodialysis package works, where claims fail, how to warn patients before they reach the annual cap, and how to handle the sensitive health information that every claim carries.

{{cards:Key terms for this module|PhilHealth Dialysis Database (PDD)::The registry a patient must be in before the outpatient hemodialysis package can be claimed.|Package rate::The fixed amount PhilHealth pays per covered session.|Session cap::The maximum number of covered sessions per calendar year.|Minimum standards::The services, medicines, and supplies a covered session must include.|No copay::The rule that patients are not charged for items within the minimum standards.|Denial::A claim PhilHealth will not pay.|PhilHealth Regional Office (PRO)::Your regional contact for accreditation and claims questions.|Data Protection Officer (DPO)::The person who handles privacy requests and breaches.}}

## Learning objectives

1. Explain the current PhilHealth maintenance hemodialysis package: eligibility, session cap, rate and covered bundle.
2. Trace one session from eligibility check to payment and identify where claims fail.
3. Track each patient's annual session use and warn early when the cap will be reached.
4. Handle health information under RA 10173, including access control and breach response.

## Field case: the denied batch

**Situation.** In March, a 16-station unit in Lucena City receives 40 of its February claims back from PhilHealth. The reason codes all point to the same problem: the signature dates on the claim documents come before the treatment dates.

The billing officer, Ms. Analyn Rosales, traces it quickly. To save time during a busy month, one attending nephrologist had signed the claim forms for all his patients' February sessions on February 1. The forms were then filled in as the sessions happened. Every session was delivered. Every form is still wrong.

**Before reading on, decide:**

- Why is a pre-signed form a problem if every session really happened?
- What must stop today, and who needs to know?
- How would you redesign the workflow so this cannot recur?

**Case review.**

**Why it matters.** A form signed before the session certifies something that had not yet happened. If a patient had been hospitalized on February 10 and missed her sessions, the pre-signed forms would have certified treatments that never occurred. That is a fraud risk, whatever the intention, and it puts the physician's license and the unit's accreditation in danger.

**Today.** The manager, Mr. Romeo Villareal, stops the practice immediately and informs the Medical Director, who speaks with the attending nephrologist. Mr. Villareal works with the PRO on the correction process for the 40 claims. He does not alter any date on any form.

**The redesign.** Claim forms are now signed at the end of each session or during the physician's rounds the same day. Before submission, billing compares every signature date with the treatment date. A random audit of 20 claims a month runs for six months. By the third month, no mismatches are found.

{{fig:uom10c}}

## The package: verify before you rely on it

As of this review, under PhilHealth Circular 2024-0023 (Revision 2) and related issuances:[[dch_philhealth2024]]

- **Eligibility:** PhilHealth members and qualified dependents with chronic kidney disease stage 5, registered in the PDD. Registration is free to the patient.
- **Cap:** up to **156 sessions per calendar year**, matching three sessions a week for 52 weeks.
- **Rate:** **6,350 pesos per session**, effective October 9, 2024, up from 4,000 pesos in July 2024 and 2,600 pesos before that. The maximum annual benefit is 990,600 pesos.[[dch_philhealth_news2024]]
- **Bundle:** the circular's minimum-standards table lists what the package covers, including the dialyzer, solutions and supplies, anticoagulation, erythropoiesis-stimulating agents according to the national formulary, and the use of machines, utilities, and staff time. Charges to patients for covered items must follow the no-copayment rules. Any charge to a patient needs review against the actual policy.

{{fig:uom10a}}

**Scale.** PhilHealth reported paying 27 billion pesos for more than 2 million hemodialysis claims in the first half of 2025 alone, nearly its total for all of 2024 (confirm the latest figures with PhilHealth). Dialysis is now one of the largest lines in the national insurer's budget. Scrutiny of claims will only increase.

**Things that change:** claim forms, electronic submission systems, filing windows, rules for inpatient and acute sessions, and exceptions. Confirm each with your PRO and the circular archive before training staff on them.

**Example.** A patient's son at a unit in Dumaguete asks why his mother was charged 1,800 pesos for "monthly laboratory tests." The billing officer checks the minimum-standards table and finds that the routine monthly panel is already part of the package. The charge is reversed with a dated note, and the manager reviews five more patients' statements. Two have the same charge. The billing template, not the officer, was the cause.

{{key:Coverage rules decide who pays. They never decide whether a patient is dialyzed today.}}

## The claim chain: where claims fail

| Step | Evidence | Common failure |
|---|---|---|
| 1. Eligibility | Membership status, PDD registration | Treatment before registration |
| 2. Session delivered | Signed treatment record with times | Missing nurse or physician signature |
| 3. Claim documents | Required forms signed after treatment by the patient and attending | Forms pre-signed in batches |
| 4. Internal review | Billing check against the treatment record | Session count does not match the record |
| 5. Submission | Electronic submission confirmation | Missed filing window |
| 6. Payment and reconciliation | Remittance advice matched to claims | Payments left unmatched |
| 7. Denial management | Reason code, correction, resubmission | Denials written off without analysis |

{{call:Hold any claim the treatment record does not support, and never change a record to match a claim. Report a suspected pattern of billing errors to the Medical Director and the licensee in writing.}}

## Calculator CALC-07: PhilHealth session-cap tracker

You need: sessions claimed this calendar year, today's date, prescribed sessions per week (usually three), the annual cap (156, editable), and the rate per session (6,350 pesos, editable).

{{formula:**Remaining covered sessions** = cap − sessions used.<br>**Weeks left in the year** = days from today to December 31 ÷ 7.<br>**Sessions needed to year end** = sessions per week × weeks left, rounded up.<br>**Shortfall** = sessions needed − remaining, if positive.<br>**Projected date the cap runs out** = today + (remaining ÷ sessions per week) weeks.}}

**Worked example.** On November 24, Mrs. Rosario Medina has claimed 150 sessions. She had nine extra sessions in July and August for fluid overload after a hospitalization. Remaining: 156 − 150 = 6. There are 37 days to December 31, or 5.3 weeks. At three a week, she needs 3 × 5.3 = 15.9, so 16 sessions. The shortfall is 10 sessions. At three sessions a week, her cap runs out in about two weeks, around December 8.

{{fig:uom10b}}

**Why it matters.** Patients rarely reach 156 before December unless they had extra sessions. When they do, they need to know weeks ahead, not at the counter on December 9. The social worker or billing officer counsels Mrs. Medina and her family in October about other assistance, such as the Malasakit Center or local government programs. The clinical team, not billing, decides whether her prescription can change. The cap must never silently reduce dialysis.

## Health information and RA 10173

Health data are **sensitive personal information** under the Data Privacy Act, Republic Act (RA) 10173.[[dch_ra10173]] In a dialysis unit, that means:

- **Need to know.** Staff see only what their role needs. Billing does not need full clinical notes; the driver does not need diagnoses.
- **No personal devices for patient data** unless the facility approves and secures them. No patient photos or results in staff group chats.
- **Rosters and whiteboards** show what is needed for care, never diagnoses that other patients and visitors can read.
- **Third-party requests** from employers, insurers, or relatives go through the DPO, with documented consent or a legal basis.
- **Disposal:** shred paper; wipe or destroy storage media.
- **Breach response:** a suspected exposure goes to the DPO immediately. National Privacy Commission rules require notification of qualifying breaches within 72 hours of knowledge;[[dch_npc1603]] the DPO decides whether a breach qualifies.

**Example.** A nurse in a unit in Taguig photographs a patient's laboratory results to send to the attending nephrologist on her personal messaging app, because the clinic computer is slow. It is quick, and it is well meant. It also puts a patient's hepatitis status on a phone that goes home, to the mall, and to the nurse's family. The manager does not discipline her. He asks the Medical Director to approve a secure channel for urgent results and has it set up within a week. Then the rule is enforced.

## Common failure modes

- **Two counts, never reconciled.** Billing and clinical session counts in separate systems.
- **Denials written off.** Returned claims not analyzed by reason.
- **Cap surprises.** Patients learning they have reached 156 only when charged.
- **Patient data on personal phones.** Convenient until the phone is lost.
- **Fixing the chart.** Changing a record to match a claim.

## Supervised practice

- [ ] Trace five synthetic sessions through all seven steps of the claim chain.
- [ ] Run CALC-07 for every patient in a fictional census in October and list those at risk.
- [ ] Analyze one quarter of denials by reason code and propose two fixes.
- [ ] Walk the unit and list every place patient information is visible to people without need to know.

## Question bank

**Q1.** What is the current PhilHealth maintenance HD session rate under PC 2024-0023 (verify locally)?
- [x] ₱6,350
- [ ] ₱2,600
- [ ] ₱4,000
- [ ] ₱10,000
> The rate rose to ₱6,350 effective October 9, 2024.

**Q2.** How many sessions per calendar year does the package cover?
- [x] Up to 156
- [ ] 90
- [ ] 144
- [ ] Unlimited
> 156 sessions match three a week for 52 weeks.

**Q3.** The maximum annual benefit at ₱6,350 × 156 is:
- [x] ₱990,600
- [ ] ₱405,600
- [ ] ₱624,000
- [ ] ₱1,560,000
> 6,350 × 156 = 990,600.

**Q4.** When should the attending and patient sign claim documents?
- [x] After the session is delivered
- [ ] At the start of the month for all sessions
- [ ] Before the patient arrives
- [ ] Only at year end
> Pre-signing creates fraud risk and claim denials.

**Q5.** PDD registration for the patient is:
- [x] Free and required for the outpatient package
- [ ] Optional
- [ ] Charged per session
- [ ] Only for hospital patients
> Registration establishes eligibility at no cost.

**Q6.** A patient has used 150 sessions by November 24. At three per week, roughly how many sessions are needed to December 31?
- [x] 16
- [ ] 6
- [ ] 3
- [ ] 50
> 5.3 weeks × 3 = 16 sessions.

**Q7.** In the example above, what is the shortfall?
- [x] 10 sessions
- [ ] 6 sessions
- [ ] 0 sessions
- [ ] 16 sessions
> 16 needed − 6 remaining = 10.

**Q8.** Who decides whether a patient's dialysis frequency changes near the cap?
- [x] The clinical team, not billing
- [ ] The billing officer
- [ ] The owner
- [ ] The patient's employer
> Financial limits must not silently reduce dialysis.

**Q9.** Under RA 10173, health data are classified as:
- [x] Sensitive personal information
- [ ] Public information
- [ ] Trade secrets
- [ ] Marketing data
> Sensitive information requires stricter protection.

**Q10.** A staff member posts a patient's photo in a staff group chat. This is:
- [x] A potential privacy breach to report to the DPO
- [ ] Acceptable among colleagues
- [ ] Required for handover
- [ ] Only a social media issue
> Patient images are personal data.

**Q11.** NPC rules require notification of qualifying breaches within:
- [x] 72 hours of knowledge
- [ ] 30 days
- [ ] One year
- [ ] No time limit
> The DPO determines whether notification applies.

**Q12.** Forty claims are denied for signature dates before treatment dates. The root cause is most likely:
- [x] Batch pre-signing of forms
- [ ] A PhilHealth system error only
- [ ] Too many patients
- [ ] Water contamination
> Workflow, not paperwork, caused the denials.

**Q13.** What should happen to denied claims?
- [x] Analysis by reason code, correction and resubmission where allowed
- [ ] Automatic write-off
- [ ] Charging patients the difference
- [ ] Ignoring them
> Denial patterns reveal fixable workflow gaps.

**Q14.** PhilHealth paid ₱27 billion for HD claims in the first half of 2025. The management implication is:
- [x] Increasing claims scrutiny and need for clean documentation
- [ ] Claims will no longer be reviewed
- [ ] Documentation matters less
- [ ] Rates will certainly fall
> Large spending attracts audit attention.

**Q15.** Which items must you verify with the PRO before training staff?
- [x] Current claim forms, submission system, filing windows and inpatient rules
- [ ] Staff birthdays
- [ ] Vendor prices
- [ ] Water test results
> Payer details change and need local confirmation.

## Sources

PH4, PH5, PH7, E20. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
