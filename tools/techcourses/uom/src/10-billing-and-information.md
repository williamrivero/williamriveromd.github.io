# 10. PhilHealth claims, documentation and privacy

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-10 (Understand) · FIG-10B (Apply) · FIG-10C (Appreciate) · **Calculator:** CALC-07 PhilHealth session-cap tracker

> **Why this matters.** A dialysis session that is delivered but cannot be claimed is a session the unit paid for twice: once in supplies and staff, again in lost revenue. A claim filed without the evidence that the session happened is worse: it is a compliance risk. The claim is simply the last page of the clinical record. If the record is complete, the claim follows.

## Learning objectives

1. Explain the current PhilHealth maintenance hemodialysis package: eligibility, session cap, rate and covered bundle.
2. Trace one session from eligibility check to payment and identify where claims fail.
3. Track each patient's annual session use and warn early when the cap will be reached.
4. Handle health information under RA 10173, including access control and breach response.

## The package (verify before you rely on it)

As of this review, under PhilHealth Circular 2024-0023 (Revision 2) and related issuances:

- **Eligibility:** PhilHealth members and qualified dependents with CKD stage 5, registered in the PhilHealth Dialysis Database (PDD). PDD registration is free to the patient.
- **Cap:** up to **156 sessions per calendar year**, set to match three sessions a week for 52 weeks (first institutionalized by PC 2023-0009).
- **Rate:** **₱6,350 per session**, effective October 9, 2024 (up from ₱4,000 in July 2024 and ₱2,600 before that). The maximum annual benefit is therefore ₱990,600.
- **Bundle:** the circular's minimum-standards table lists what the package covers, including dialyzer, solutions and supplies, anticoagulation, erythropoiesis-stimulating agents per the national formulary, and use of machines, utilities and staff time. Charges to patients for covered items must follow the circular's no-copayment rules; any patient charge needs review against the actual policy and documentation.

**Scale.** PhilHealth reported paying ₱27 billion for more than 2 million hemodialysis claims in the first half of 2025 alone, nearly its total for all of 2024. Dialysis is now one of the largest lines in the national insurer's budget, which means scrutiny of claims will only increase.

**Things that change:** claim forms, electronic submission systems, filing windows, treatment of inpatient and acute sessions, and exceptional cases. Verify each with your PhilHealth Regional Office (PRO) and the circular archive before training staff on them.

## The claim chain: where claims fail

| Step | Evidence | Common failure |
|---|---|---|
| 1. Eligibility | Membership status, PDD registration | Treatment before registration |
| 2. Session delivered | Signed treatment record with times | Missing nurse or physician signature |
| 3. Claim documents | Required claim forms signed **after** treatment by the patient and attending | Forms pre-signed in batches |
| 4. Internal review | Billing check against treatment record | Session count mismatched with record |
| 5. Submission | Electronic submission confirmation | Missed filing window |
| 6. Payment and reconciliation | Remittance advice matched to claims | Unmatched payments left unapplied |
| 7. Denial management | Reason code, correction, resubmission | Denials written off without analysis |

**Never pre-sign.** Physicians and patients sign claim documents only after the session is delivered. Pre-signed forms for sessions that later did not happen are a fraud risk, whatever the intention.

## Calculator CALC-07: PhilHealth session-cap tracker

**Inputs:** sessions claimed this calendar year (U), today's date, prescribed sessions per week (default 3), annual cap (default 156; editable), rate per session (default ₱6,350; editable).

**Formulas**

- Remaining covered sessions = cap − U
- Weeks left in the year = days from today to December 31 ÷ 7
- Sessions needed to year end = prescribed per week × weeks left (rounded up)
- Shortfall = sessions needed − remaining (if positive)
- Estimated uncovered amount = shortfall × the unit's self-pay charge (entered by the user)
- Projected cap-exhaustion date = today + (remaining ÷ prescribed per week) weeks

**Worked example.** On November 24 a patient has claimed 150 sessions. Remaining: 6. Weeks left: 37 days ÷ 7 = 5.3. Sessions needed at three a week: 16. Shortfall: 10 sessions. At thrice-weekly treatment, the cap runs out in about two weeks, around December 8.

**Why it matters.** Patients rarely reach 156 by December unless they had extra sessions (for example, added treatments for fluid overload). When they do, they need to know weeks in advance, not at the counter. The social worker or billing officer counsels the patient on other assistance programs. The clinical team, not billing, decides whether the prescription can change. Never let the cap silently reduce dialysis.

## Health information and RA 10173

Health data are **sensitive personal information** under the Data Privacy Act. What that means in a dialysis unit:

- **Need to know.** Staff access only the records they need for their role. Billing does not need full clinical notes; transport does not need diagnoses.
- **No personal devices for patient data** unless the facility approves and secures them. No patient photos in staff group chats.
- **Rosters and whiteboards** show what is needed for care, not diagnoses visible to other patients and visitors.
- **Requests from third parties** (employers, insurers, relatives) go through the Data Protection Officer (DPO) process with documented consent or legal basis.
- **Disposal:** shred paper; wipe or destroy storage media.
- **Breach response:** suspected exposure goes to the DPO immediately. National Privacy Commission rules require notification of qualifying breaches within 72 hours of knowledge; your DPO decides whether a breach qualifies.

## Field case: the denied batch

**Situation.** Forty claims from one month are returned. The reason codes point to signature dates on claim documents that precede treatment dates.

**Root cause.** To save time, the attending had signed forms for the whole month on the first day.

**Response.** The manager stops the practice immediately, informs the Medical Director, works with the PRO on the correction process for the affected claims and redesigns the workflow: forms are signed at the end of each session or during the physician's rounds the same day, and billing checks signature dates against treatment dates before submission. A monthly audit of 20 random claims follows for six months.

## Common failure modes

- Billing and clinical counts kept in separate systems that never reconcile.
- Denials written off rather than analyzed by reason.
- Patients learning they have reached the cap only when charged.
- Patient data in personal messaging apps.

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
