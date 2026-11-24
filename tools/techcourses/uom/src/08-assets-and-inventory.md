# 08. Equipment, supplies and procurement

**Core** · 40 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-08 (Understand) · FIG-08B (Apply) · FIG-08C (Appreciate) · **Calculator:** CALC-05 Reorder point, days-on-hand and machine availability

> **Why this matters.** Every session consumes a predictable bundle: a dialyzer (new or reprocessed), bloodlines, needles or catheter supplies, concentrates, saline, heparin, gloves, dressings and an erythropoiesis-stimulating agent for many patients. Run out of one item and the session does not happen. Use one recalled lot and you need to find every patient who received it, today. Inventory is clinical continuity measured in boxes.

## Learning objectives

1. Maintain an asset register and preventive maintenance schedule for dialysis machines and the water system.
2. Calculate reorder points, safety stock and days-on-hand for critical supplies.
3. Trace a lot from receipt to patient and execute a recall or quarantine.
4. Run a transparent procurement that separates requesting, approving, receiving and paying.

## The operating model: assets, consumables and traceability

**Assets** (machines, RO system, chairs, defibrillator, reprocessing equipment) have a lifecycle: acceptance testing, scheduled preventive maintenance, repair, release and eventual retirement. Each has a unique identifier and a history.

**Consumables** move: received, stored, issued, used. Two rules matter most:

- **First expiry, first out (FEFO):** use the earliest-expiring lot first. Not first in, first out, because a later delivery can carry an earlier expiry.
- **Lot traceability:** record which lot each patient received for high-risk items (dialyzers, bloodlines, concentrates, injectable drugs). When a recall arrives, you need a list of patients within an hour, not a week.

**Reprocessed dialyzers** add a layer. Each reused dialyzer belongs to one patient, carries a label with the patient's identity and reuse number, and must pass performance testing (total cell volume or equivalent) and germicide checks before each use. The reprocessing log is both a quality record and a traceability record. Follow your PSN and DOH-aligned reprocessing policy and the manufacturer's instructions.

## What the evidence shows

- **Equipment failures are a recognized source of harm** in dialysis, including alarm failures, air detector malfunction and conductivity errors. Structured preventive maintenance and documented release are **established practice** across international standards (for example, IEC 60601-2-16 for hemodialysis equipment safety and ISO 23500 for the water system). Outcome trials comparing maintenance intervals do not exist. Follow the manufacturer's schedule as the minimum.
- **Dialyzer reuse** has a mixed observational evidence base. Some older US analyses associated certain germicides and reuse practices with higher mortality, while others found no difference when reprocessing was well controlled. The defensible position is that **reuse safety depends on process control**: validated methods, performance testing, germicide verification and accurate records.
- **Supply-chain disruptions are real.** Global shortages of dialysis supplies (for example, bloodline shortages in several countries in recent years) have forced units to ration. Safety stock and alternative-supplier planning are the only defense.

## Calculator CALC-05: reorder point, days-on-hand and machine availability

**Inputs:** average daily usage (units/day), supplier lead time (days), safety stock days, current stock on hand; for machines: scheduled treatment hours and hours unavailable for repair.

**Formulas**

- Safety stock = safety stock days × average daily usage
- Reorder point = (average daily usage × lead time) + safety stock
- Days on hand = current stock ÷ average daily usage
- Machine availability (%) = (scheduled hours − unavailable hours) ÷ scheduled hours × 100

**Worked example.** A unit runs 45 sessions a day using new bloodlines. Supplier lead time is 10 days. The Medical Director and administrator choose 14 days of safety stock because the supplier is a single importer.
- Safety stock = 14 × 45 = 630 sets
- Reorder point = 45 × 10 + 630 = 1,080 sets
- With 1,400 sets on hand, days on hand = 31

Order when stock falls to 1,080. If the supplier warns of delays, raise the lead time in the calculator and the reorder point rises with it.

**Machine example.** 15 machines × 18 scheduled hours a day × 26 days = 7,020 hours a month. If machines were down 210 hours, availability is 97%. Track by machine: one unit that is down repeatedly is a retirement decision, not a repair.

## The asset register

| Asset ID | Type | Serial | Location | Acceptance date | PM interval | Last PM | Next PM | Repairs (12 months) | Status |
|---|---|---|---|---|---|---|---|---|---|
| M-07 | Dialysis machine | XXXX | Station 7 | 2021-03 | 6 months | 2026-09 | 2027-03 | 2 | In service |
| RO-01 | RO system | YYYY | Water room | 2019-11 | Per vendor | 2026-10 | 2026-12 | 1 | In service |

## Recall and quarantine

1. Receive the notice; verify product, lot and action required.
2. Physically quarantine affected stock with a clear label and log entry.
3. Pull the usage record: which patients received the lot and when.
4. Notify the Medical Director and head nurse; clinical leads decide on patient follow-up.
5. Arrange replacement stock; record the vendor's return or credit.
6. File the recall record in the evidence index.

## Procurement with internal controls

- **Requisition:** the requesting unit states need, quantity and specification.
- **Approval:** someone with budget authority approves, separate from the requester where possible.
- **Quotation:** obtain comparable quotes per policy; document the selection reason (price, registration with the Philippine FDA, delivery reliability, service support).
- **Purchase order:** issued before delivery.
- **Receiving:** count, check lot, expiry and condition; sign the receiving report.
- **Payment:** finance pays after matching purchase order, receiving report and invoice (the three-way match; see Module 16).

Clinical product changes (a new dialyzer brand, a different concentrate) need Medical Director approval, not just a better price.

## Field case: the cheaper dialyzer

**Situation.** A vendor offers a dialyzer 18% cheaper than the current brand. Finance wants to switch immediately.

**Problem.** Different membrane, surface area and clearance characteristics can change delivered dose. Reprocessing compatibility may differ.

**Solution.** The manager prepares a comparison (registration status, specifications, price, supply reliability, reprocessing compatibility) and sends it to the Medical Director. The Medical Director approves a monitored trial on a subset of patients with adequacy measurements before full conversion. The decision record shows clinical review preceded the cost decision.

## Common failure modes

- FIFO instead of FEFO, leaving expired stock at the back.
- No lot recorded per patient, making recalls guesswork.
- One person requests, approves, receives and pays.
- Machines returned to service after repair without a documented release check.

## Supervised practice

- [ ] Update the asset register and confirm the next preventive maintenance date for every machine.
- [ ] Run CALC-05 for the five highest-volume supplies and compare with current reorder practice.
- [ ] Conduct a mock recall: pick a dialyzer lot and produce the patient list within one hour.
- [ ] Map who requests, approves, receives and pays in your unit and identify any overlap.

## Question bank

**Q1.** What does FEFO mean?
- [x] First expiry, first out
- [ ] First entered, first ordered
- [ ] Final expiry, final order
- [ ] Fast entry, fast output
> Use the earliest-expiring lot first.

**Q2.** Daily usage 30, lead time 7 days, safety stock 10 days. What is the reorder point?
- [x] 510
- [ ] 300
- [ ] 210
- [ ] 37
> 30 × 7 + 30 × 10 = 210 + 300 = 510.

**Q3.** Stock on hand 600, daily usage 40. Days on hand?
- [x] 15
- [ ] 24
- [ ] 640
- [ ] 6
> 600 ÷ 40 = 15.

**Q4.** Why record the lot number of dialyzers and bloodlines per patient?
- [x] So affected patients can be identified quickly in a recall
- [ ] For marketing
- [ ] To increase storage space
- [ ] Because patients ask for it
> Traceability makes recalls fast and accurate.

**Q5.** A reprocessed dialyzer must:
- [x] Belong to one patient, be labeled and pass performance and germicide checks
- [ ] Be shared among patients with the same blood type
- [ ] Be used without testing if it looks clean
- [ ] Be reused indefinitely
> Process control defines reuse safety.

**Q6.** What is the evidence position on dialyzer reuse?
- [x] Mixed observational data; safety depends on process control
- [ ] Proven to improve survival
- [ ] Proven to double mortality in all settings
- [ ] Never studied
> Well-controlled reprocessing is the defensible standard.

**Q7.** A switch to a new dialyzer brand needs approval from:
- [x] The Medical Director, after clinical review
- [ ] Finance alone
- [ ] The vendor
- [ ] The storeroom clerk
> Membrane differences can affect delivered dose.

**Q8.** Scheduled machine hours 1,000; unavailable 50. Availability?
- [x] 95%
- [ ] 5%
- [ ] 50%
- [ ] 105%
> (1,000 − 50) ÷ 1,000 × 100 = 95%.

**Q9.** In a recall, what happens first after verifying the notice?
- [x] Physically quarantine and label the affected stock
- [ ] Use remaining stock quickly
- [ ] Wait for the next delivery
- [ ] Discard the notice
> Quarantine prevents further use.

**Q10.** The three-way match compares:
- [x] Purchase order, receiving report and invoice
- [ ] Three supplier quotes only
- [ ] Three patients' records
- [ ] Budget, salary and rent
> Payment follows a verified match.

**Q11.** Why choose a larger safety stock for a single-importer product?
- [x] A single source carries higher disruption risk
- [ ] Larger stock always lowers cost
- [ ] Regulation forbids small stocks
- [ ] It reduces expiry
> Safety stock buffers supply uncertainty.

**Q12.** After a machine repair, before returning it to service:
- [x] A trained technician documents a release check
- [ ] The vendor leaves and nurses resume use
- [ ] Patients test it themselves
- [ ] The manager signs without testing
> Documented release confirms safe function.

**Q13.** One machine has been repaired five times in six months. This most likely indicates:
- [x] A retirement or replacement decision
- [ ] Normal performance
- [ ] A billing issue
- [ ] Too much preventive maintenance
> Track repairs per asset to support lifecycle decisions.

**Q14.** Who should not be the same person in procurement, where possible?
- [x] The requester, approver, receiver and payer
- [ ] The patient and the nurse
- [ ] The doctor and the dietitian
- [ ] The guard and the driver
> Segregation of duties prevents error and fraud.

**Q15.** Supplier lead time increases from 10 to 20 days. The reorder point:
- [x] Rises by usage × 10 days
- [ ] Falls
- [ ] Stays the same
- [ ] Becomes zero
> Longer lead time requires ordering earlier.

## Sources

PH1, PH3, PH6, INT1, INT4, E10. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
