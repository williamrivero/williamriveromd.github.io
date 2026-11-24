# 08. Equipment, supplies, and procurement

## The big picture

{{plain:Every treatment uses a machine that must work and a box of supplies that must be safe. Think of each item as having a passport: where it came from, which lot it belongs to, when it expires, who checked it, and which patient it reached. When something goes wrong with a product, the passport lets you find every patient it touched within the hour.}}

The picture has a limit. Passports are checked at borders; supplies are rarely checked after the receiving dock. A box of dialyzers can sit for months in a hot stockroom, and a machine can be "fixed" by a vendor and put back into service without anyone signing that it passed its checks. The passport is only as good as the habit of writing in it.

This module covers the three things that keep a unit supplied and safe: an asset register that knows every machine's history, a stock system that never runs out and never uses expired items, and a purchasing process that no single person controls.

{{cards:Key terms for this module|Asset register::One list of every machine and major piece of equipment, with its history.|Preventive maintenance (PM)::Scheduled servicing done before something breaks.|First expiry, first out (FEFO)::Use the lot that expires first, regardless of when it arrived.|Lot traceability::Recording which lot each patient received, for high-risk items.|Reorder point::The stock level at which you must order to avoid running out.|Safety stock::Extra stock held to cover delays and surges.|Quarantine::Physically separating suspect stock so it cannot be used.|Three-way match::Paying only when the purchase order, the receiving report, and the invoice agree.}}

## Learning objectives

1. Maintain an asset register and preventive maintenance schedule for dialysis machines and the water system.
2. Calculate reorder points, safety stock and days-on-hand for critical supplies.
3. Trace a lot from receipt to patient and execute a recall or quarantine.
4. Run a transparent procurement that separates requesting, approving, receiving and paying.

## Field case: the cheaper dialyzer

**Situation.** At a 20-station unit in Batangas City, the finance officer, Mr. Rey Panganiban, brings the manager, Ms. Cheryl Mercado, a quotation. A new vendor offers a dialyzer 18% cheaper than the brand the unit has used for six years. With about 1,000 dialyzers a month, the savings would cover most of a nurse's salary. "Let's switch next month," he says. "A dialyzer is a dialyzer."

Ms. Mercado notices that the new dialyzer has a different membrane material and a smaller surface area. The unit reprocesses dialyzers for some patients.

**Before reading on, decide:**

- Who should decide whether to switch, and on what evidence?
- What could go wrong for patients if the switch happens without review?
- What should Ms. Mercado bring to that decision?

**Case review.**

**Who decides.** A dialyzer is part of the prescription. A change in membrane and surface area can change how much waste is cleared each session, and reprocessing compatibility may differ. This is a clinical product decision for the Medical Director, informed by cost, not driven by it.

**What she brings.** Ms. Mercado prepares a one-page comparison: Philippine Food and Drug Administration registration, membrane type, surface area and published clearance, price per unit and per month, the vendor's supply record and lead time, reprocessing compatibility, and service support.

**The decision.** The Medical Director approves a monitored trial: twelve patients for six weeks, with dialysis adequacy measured before and after, and the reprocessing team checking performance tests on each reused dialyzer. In week four, two patients' adequacy results fall below target, and the attending nephrologists adjust their prescriptions. The trial shows the new dialyzer works, but some patients need a longer session or a larger size. The final decision includes that cost. The record shows clinical review came before the cost decision.

{{fig:uom08c}}

## The operating model: assets, consumables, and traceability

{{fig:uom08a}}

**Assets** are the machines, the reverse osmosis system, chairs, the defibrillator, and reprocessing equipment. Each one has a life: acceptance testing, scheduled preventive maintenance, repairs, release back to service, and eventual retirement. Each has a unique identifier and a history you can read.

**Consumables** move: received, stored, issued, used. Two rules matter most.

- **First expiry, first out.** Use the earliest-expiring lot first. Not first in, first out, because a later delivery can carry an earlier expiry date.
- **Lot traceability.** Record which lot each patient received for high-risk items: dialyzers, bloodlines, concentrates, and injectable drugs. When a recall arrives, you need a list of patients within an hour, not a week.

**Reprocessed dialyzers** add a layer. Each reused dialyzer belongs to one patient and carries a label with the patient's identity and reuse number. Before each use it must pass a performance test (total cell volume or an equivalent) and a check that the germicide is present and then fully rinsed out. The reprocessing log is both a quality record and a traceability record. Follow your PSN and DOH-aligned reprocessing policy and the manufacturer's instructions.[[psn2024]]

**Example.** A stockroom in Legazpi receives bloodlines in March with an expiry date in September, and another delivery in May that expires in July. Under first in, first out, the March stock is used first, and in August the clerk finds 240 sets from the May delivery past their date. Under first expiry, first out, the May stock would have been used first, and nothing would have expired.

## What the evidence shows

**Equipment failures cause harm.** Alarm failures, air detector malfunctions, and conductivity errors are recognized causes of injury in dialysis. Scheduled preventive maintenance and documented release are established practice across international standards for hemodialysis equipment and, for the water system, ISO 23500.[[iso23500_1]] No trial compares maintenance intervals, so follow the manufacturer's schedule as the minimum.

**Dialyzer reuse depends on process control.** Some older United States analyses associated certain germicides and reuse practices with higher mortality. Others found no difference when reprocessing was well controlled. The defensible position is that the safety of reuse depends on validated methods, performance testing, germicide checks, and accurate records.

**Supply chains break.** Shortages of dialysis supplies, including bloodlines, have forced units in several countries to ration in recent years. Safety stock and a second supplier are the only defense.

## Calculator CALC-05: reorder point, days on hand, and machine availability

You need: average daily use, supplier lead time in days, safety stock days, current stock, and, for machines, scheduled treatment hours and hours lost to repair.

{{formula:**Safety stock** = safety stock days × average daily use.<br>**Reorder point** = (average daily use × lead time) + safety stock.<br>**Days on hand** = current stock ÷ average daily use.<br>**Machine availability** = (scheduled hours − hours down) ÷ scheduled hours × 100.}}

**Worked example.** A unit runs 45 sessions a day using new bloodlines. The supplier's lead time is 10 days. Because the supplier is a single importer, the Medical Director and administrator choose 14 days of safety stock.

- Safety stock = 14 × 45 = 630 sets
- Reorder point = 45 × 10 + 630 = 1,080 sets
- With 1,400 sets on hand, days on hand = 1,400 ÷ 45 = 31 days

Order when stock falls to 1,080. If the supplier warns of a delay at the port, raise the lead time in the calculator, and the reorder point rises with it.

**Machine example.** Fifteen machines × 18 scheduled hours a day × 26 days = 7,020 hours a month. If machines were down 210 hours, availability is (7,020 − 210) ÷ 7,020 = 97%. Track it per machine. One machine that keeps breaking is a retirement decision, not another repair.

## The asset register

| Asset ID | Type | Serial | Location | Accepted | PM interval | Last PM | Next PM | Repairs (12 months) | Status |
|---|---|---|---|---|---|---|---|---|---|
| M-07 | Dialysis machine | XXXX | Station 7 | 2021-03 | 6 months | 2026-09 | 2027-03 | 2 | In service |
| RO-01 | Reverse osmosis system | YYYY | Water room | 2019-11 | Per vendor | 2026-10 | 2026-12 | 1 | In service |

{{key:A machine returns to service only on a documented release by the biomedical technician, never because the vendor has left.}}

## Recall and quarantine

{{fig:uom08b}}

{{flow:A recall in one hour|Verify::Confirm the product, the lot, and the action required.|Quarantine::Physically separate the stock, label it, and log it.|Trace::Pull the usage record: which patients received the lot, and when.|Notify::Tell the Medical Director and head nurse. Clinical leads decide on patient follow-up.|Replace::Arrange replacement stock and record the vendor's return or credit.|File::Put the recall record in the evidence index (Module 2).}}

**Example.** At 10:00 on a Tuesday, a supplier emails a recall for a lot of acid concentrate with a labeling error in its potassium content. The manager in Ormoc finds four cartons of that lot in the stockroom and one on the floor. The lot log shows it was used for 22 treatments since Saturday. By 10:50 the stock is quarantined, the floor carton is removed, and the Medical Director has the list of 22 patients. The attending nephrologists order potassium checks for those still in the unit and call the others. Without lot records, the unit would have had to test every patient who dialyzed in five days.

{{call:When a recall or a suspected defective lot affects patients, quarantine the stock and give the Medical Director the patient list. Patient follow-up is a clinical decision.}}

## Procurement with internal controls

{{flow:Buying without risk|Requisition::The requesting area states the need, quantity, and specification.|Approval::Someone with budget authority approves, separate from the requester where possible.|Quotation::Comparable quotes per policy; document the reason for the choice: price, Food and Drug Administration registration, delivery reliability, service support.|Purchase order::Issued before delivery.|Receiving::Count, check lot, expiry, and condition; sign the receiving report.|Payment::Finance pays after the three-way match (Module 16).}}

A clinical product change, such as a new dialyzer brand or a different concentrate, needs Medical Director approval, not just a better price.

## Common failure modes

- **First in, first out.** Expired stock found at the back of the shelf.
- **No lot per patient.** Recalls become guesswork.
- **One person does everything.** The same person requests, approves, receives, and pays.
- **Silent return to service.** A machine back in use after repair with no release check.
- **Price before prescription.** A clinical product switched by finance.

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
