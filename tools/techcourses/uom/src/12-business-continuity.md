# 12. Continuity during outages and disasters

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-12 (Understand) · FIG-12B (Apply) · FIG-12C (Appreciate) · **Calculator:** CALC-12 Outage autonomy (generator and treated-water storage)

> **Why this matters.** The Philippines sits in the typhoon belt and on the Pacific Ring of Fire. Floods, brownouts, earthquakes and water interruptions are not rare events for a dialysis unit here. They are seasonal. Patients cannot postpone dialysis for a week while roads clear. Continuity planning is how a unit keeps its promise of three treatments a week through the worst week of the year.

## Learning objectives

1. Identify the critical dependencies of a hemodialysis unit (power, water, staff, supplies, communications, transport) and their failure modes.
2. Calculate how long the unit can operate on generator fuel and stored treated water.
3. Write a phased plan for predictable hazards (typhoon) and sudden hazards (earthquake, grid failure).
4. Coordinate transfers to partner units and phased reopening after an event.

## The model: dependencies and buffers

A hemodialysis session needs, at the same time: electricity, treated water at the right quality and pressure, a trained team, supplies, a working machine and a patient who can reach the unit. Losing any one stops the session. Continuity planning asks for each dependency: **How long can we run without it, and what is our backup?**

| Dependency | Typical failure | Buffer |
|---|---|---|
| Grid power | Brownout, typhoon damage | Generator sized for machines plus RO plus lighting; automatic transfer switch; fuel contract |
| Municipal water | Supply interruption, contamination after floods | Raw-water storage; treated-water storage; tanker arrangement; testing after resumption |
| Staff | Cannot travel; affected families | Staff contact tree; local staff map; accommodation; mutual aid |
| Supplies | Road closure, port delays | Safety stock (Module 08); pre-positioned stock before typhoon season |
| Communications | Cellular failure | Landline, alternate network SIMs, radio if available; printed patient list |
| Patients | Flooded roads, evacuation centers | Early dialysis; emergency information sheet; partner-unit list |

## What the evidence shows

- **Early dialysis before a predictable disaster is associated with better outcomes.** Before Hurricane Sandy, patients who received an early session had lower adjusted odds of emergency visits (about 20%), hospitalization (about 21%) and 30-day death (about 28%) (Lurie et al., *AJKD* 2015). Observational, but strongly consistent with the physiology of missed treatment (Module 04).
- **Disasters disrupt care and increase harm.** Patients in Sandy-affected areas had more emergency department visits and hospitalizations and a small rise in mortality compared with unaffected regions (Kelman et al., *AJKD* 2015).
- **Asia-Pacific experience.** Reviews of earthquakes, tsunamis and typhoons across the region, including the Philippines, describe the same lessons: patient tracking, pre-agreed transfer arrangements, emergency supplies and staff welfare (Gray et al., *Nephrology* 2015).

## Calculator CALC-12: outage autonomy

**Inputs:** usable generator fuel (L), generator consumption at expected load (L/h), active machines, dialysate flow rate (mL/min), additional treated-water use per hour (rinse, reprocessing, RO reject not recycled), usable treated-water storage (L).

**Formulas**

- Generator runtime (h) = usable fuel ÷ consumption per hour
- Treated-water demand (L/h) = machines × dialysate flow (L/min) × 60 + additional use
- Water autonomy (h) = usable treated-water storage ÷ demand
- Operating autonomy = the smaller of the two (the binding constraint)
- Sessions possible = operating autonomy ÷ session length × machines (rounded down)

**Worked example.** Fuel 400 L at 22 L/h: about 18 hours. Fifteen machines at 500 mL/min: 15 × 0.5 × 60 = 450 L/h, plus 100 L/h other use = 550 L/h. Storage 3,000 L: about 5.5 hours. **Water is the binding constraint**, enough for one full shift of 4-hour sessions on all 15 machines, not two. The plan therefore needs a water tanker agreement or reduced stations, not more diesel.

Check generator sizing with the biomedical technician; consumption depends on load, and the RO system's pumps add significant demand.

## A phased typhoon plan

**Season start (May to June):** test generator under load, confirm fuel and water contracts, update patient emergency information sheets, pre-position supplies for at least two weeks, refresh staff contact tree, confirm partner units.

**Advisory (72 hours before landfall):** monitor PAGASA bulletins; the Medical Director decides on early dialysis; notify patients of revised schedules; top up fuel and water; secure records and equipment above flood level.

**Imminent (24 hours):** complete early sessions; give patients their emergency information sheet and the dietitian's emergency diet guidance; confirm where each patient will shelter; staff who will stay on site are identified with food and accommodation.

**During:** close safely if conditions make travel dangerous; maintain communication; record patient contacts.

**Recovery:** inspect building, power and water; have the water system tested and released before treatment (Module 06); reopen in phases, highest-risk patients first; contact every patient; arrange transfers for those who cannot reach the unit.

## Partner units and transfer

Maintain written agreements (memoranda of agreement) with at least two partner units outside your likely hazard zone. Each agreement states how patients are referred, what records travel with them (prescription, serology, access type, PDD status) and how billing is handled. Test it once a year by sending one transient patient through the process.

## Field case: the brownout that lasted

**Situation.** A provincial grid failure starts at 08:00 on a Monday. The generator starts. At 13:00 the water technician reports that treated-water storage is falling faster than RO output because the RO is running at reduced pressure.

**Response.** The manager runs CALC-12 with current figures: about 2 hours of water at full load. With the Medical Director and head nurse, the afternoon shift is reduced to the eight highest-risk patients. Seven stable patients are transferred to a partner unit with records. A water tanker is called under the standing contract. Treatment resumes at full capacity the next morning after the technician confirms water quality.

## Common failure modes

- Generator tested without load.
- Planning only for power, forgetting water.
- Patient contact lists only in the electronic system that went down.
- Partner agreements that exist on paper but have never been used.

## Supervised practice

- [ ] Map your unit's dependencies and buffers using the table above.
- [ ] Run CALC-12 with your actual generator and storage figures.
- [ ] Write the four-phase typhoon plan for your location.
- [ ] Test one partner-unit transfer with complete records.

## Question bank

**Q1.** Before a forecast typhoon, early dialysis was associated in the Sandy study with:
- [x] Lower odds of death within 30 days
- [ ] Higher mortality
- [ ] No effect
- [ ] More emergency visits
> About 28% lower adjusted odds of 30-day death.

**Q2.** Fuel 300 L, consumption 20 L/h. Generator runtime?
- [x] 15 hours
- [ ] 6 hours
- [ ] 320 hours
- [ ] 60 hours
> 300 ÷ 20 = 15.

**Q3.** Twelve machines at 500 mL/min dialysate flow need how much treated water per hour (before other uses)?
- [x] 360 L
- [ ] 6 L
- [ ] 6,000 L
- [ ] 36 L
> 12 × 0.5 L/min × 60 = 360 L/h.

**Q4.** Generator runtime 18 hours, water autonomy 5 hours. Operating autonomy?
- [x] 5 hours
- [ ] 18 hours
- [ ] 23 hours
- [ ] 13 hours
> The smaller value binds.

**Q5.** After a flood, before resuming treatment, you must:
- [x] Have the water system tested and released
- [ ] Start immediately to clear the backlog
- [ ] Rely on bottled drinking water
- [ ] Skip testing if the water looks clear
> Floods can contaminate water and damage treatment components.

**Q6.** A partner-unit agreement should specify:
- [x] Referral process, records that travel and billing arrangements
- [ ] Only the partner's phone number
- [ ] Staff salaries
- [ ] Vendor discounts
> Complete terms make transfers work under pressure.

**Q7.** Which record must travel with a transferred patient?
- [x] Prescription, serology, access type and PDD status
- [ ] Only the patient's name
- [ ] The unit's budget
- [ ] Staff schedules
> The receiving unit needs these to treat safely.

**Q8.** Generator testing should be done:
- [x] Under load, on schedule
- [ ] Only when the grid fails
- [ ] Without load to save fuel
- [ ] Once at installation
> No-load tests miss failures that appear under demand.

**Q9.** Why keep a printed patient contact list?
- [x] Electronic systems may be unavailable during outages
- [ ] Printing is required by PhilHealth
- [ ] It is cheaper
- [ ] Patients prefer paper
> Redundant communication tools are essential.

**Q10.** When should typhoon season preparation begin?
- [x] Before the season, with generator, fuel, water and supply checks
- [ ] When the storm signal is raised
- [ ] After landfall
- [ ] Never; storms are unpredictable
> Most preparation cannot be done in the last 24 hours.

**Q11.** During recovery, which patients are treated first?
- [x] Those at highest clinical risk, as decided by clinical leads
- [ ] Those living closest
- [ ] Those who call first
- [ ] Those with private payers
> Prioritize by physiology.

**Q12.** In the brownout case, the binding constraint was:
- [x] Treated water
- [ ] Diesel fuel
- [ ] Number of nurses
- [ ] Number of chairs
> Water ran out before fuel.

**Q13.** Asia-Pacific disaster reviews emphasized:
- [x] Patient tracking, transfer arrangements, emergency supplies and staff welfare
- [ ] Closing units for a month
- [ ] Avoiding all planning
- [ ] Using only home dialysis
> Lessons repeat across disasters in the region.

**Q14.** Who decides whether to provide early dialysis before a typhoon?
- [x] The Medical Director and clinical team
- [ ] The billing officer
- [ ] The landlord
- [ ] The generator vendor
> It is a clinical decision supported by operations.

**Q15.** A partner-unit agreement is best validated by:
- [x] Sending a transient patient through the full process annually
- [ ] Filing it in a drawer
- [ ] Discussing it at a party
- [ ] Waiting for a disaster
> A tested agreement works under pressure.

## Sources

PH1, PH6, INT1, INT2, E11, E18. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
