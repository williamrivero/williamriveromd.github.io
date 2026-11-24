# 12. Continuity during outages and disasters

## The big picture

{{plain:Every dialysis patient carries a clock. It starts when their last treatment ends and runs until potassium, fluid, and acid become dangerous, usually within a few days. A typhoon, an earthquake, or a three-day brownout does not stop the clock. Continuity planning is the work of making sure every patient gets treated before their clock runs out, even when the unit cannot open.}}

The picture has a limit. The clock does not tick at the same speed for everyone. A patient who ate lechon at a fiesta, or who has little remaining kidney function, runs faster than one who still makes urine. And the clock does not ring an alarm. Patients can feel fine until they do not. That is why continuity plans start days before the storm, not the morning after.

The Philippines sits in the typhoon belt and on the Ring of Fire. Every unit will face these events. The units that do well are not the ones with the biggest generators. They are the ones that planned, rehearsed, and knew where every patient was.

{{cards:Key terms for this module|Dependency::Anything a session cannot run without: power, water, staff, supplies, communications, transport.|Buffer::The backup for a dependency, and how long it lasts.|Binding constraint::The dependency that runs out first. It sets how long you can operate.|Autonomy::How many hours the unit can keep treating without outside help.|Early dialysis::A session moved earlier so patients start a disaster freshly treated.|Partner unit::A unit outside your hazard zone that has agreed in writing to take your patients.|Emergency information sheet::A one-page summary each patient carries: prescription, access, serology, contacts.}}

## Learning objectives

1. Identify the critical dependencies of a hemodialysis unit (power, water, staff, supplies, communications, transport) and their failure modes.
2. Calculate how long the unit can operate on generator fuel and stored treated water.
3. Write a phased plan for predictable hazards (typhoon) and sudden hazards (earthquake, grid failure).
4. Coordinate transfers to partner units and phased reopening after an event.

## Field case: the brownout that lasted

**Situation.** It is 08:00 on a Monday at a 15-station unit in Roxas City, Capiz. A provincial grid failure takes out power across the city. The generator starts within seconds, and the morning shift continues.

At 13:00, the water technician, Mr. Danilo Arceo, reports a problem. The reverse osmosis system is running at reduced pressure on generator power, and the treated-water storage tank is falling faster than it refills. The afternoon shift of 15 patients starts at 14:00. The power company says the grid may be back "tonight or tomorrow."

**Before reading on, decide:**

- Which will run out first, fuel or water? How would you find out?
- If you cannot treat all 15 afternoon patients, who decides which ones are treated?
- What happens to the patients who are not treated today?

**Case review.**

**The binding constraint.** The manager, Ms. Lorelie Bautista, runs the outage calculator with current figures. The fuel will last another 16 hours. The water, at full load, will last about two hours. Water is the binding constraint. Buying more diesel would not help.

**Who decides.** Ms. Bautista brings the numbers to the Medical Director and the head nurse. They reduce the afternoon shift to the eight highest-risk patients: those with the longest gap, the highest last potassium, and the heaviest weight gains. Ms. Bautista's job is to make the plan work, not to choose the patients.

**The other seven.** She calls the partner unit in Iloilo City, which can take seven patients on its evening shift. Each patient travels with an emergency information sheet: prescription, access type, serology, and PhilHealth Dialysis Database status. She arranges a van. She calls the water tanker under the standing contract.

**Recovery.** Power returns at 02:00. Before the morning shift, Mr. Arceo tests the water and the Medical Director's designee releases it. All 15 stations open at 06:00. Ms. Bautista adds a line to the plan: test the reverse osmosis output on generator power during the next generator load test, so this is known in advance.

{{fig:uom12c}}

## The model: dependencies and buffers

A hemodialysis session needs, all at once, electricity, treated water at the right quality and pressure, a trained team, supplies, a working machine, and a patient who can reach the unit. Losing any one stops the session. For each dependency, ask two questions: how long can we run without it, and what is our backup?

{{fig:uom12a}}

| Dependency | Typical failure | Buffer |
|---|---|---|
| Grid power | Brownout, typhoon damage | Generator sized for machines, reverse osmosis, and lighting; automatic transfer switch; fuel contract |
| Municipal water | Supply interruption, contamination after floods | Raw-water and treated-water storage; tanker agreement; testing after supply resumes |
| Staff | Cannot travel; families affected | Staff contact tree; map of who lives near; accommodation; mutual aid |
| Supplies | Road closure, port delays | Safety stock (Module 8); supplies pre-positioned before typhoon season |
| Communications | Mobile network failure | Landline, SIMs on a second network, radio if available; printed patient list |
| Patients | Flooded roads, evacuation centers | Early dialysis; emergency information sheet; partner-unit list |

## What the evidence shows

**Early dialysis before a predictable disaster is associated with better outcomes.** Before Hurricane Sandy, patients who received an early session had, in adjusted analyses, about 20% lower odds of an emergency department visit, 21% lower odds of hospitalization, and 28% lower odds of death within 30 days.[[dch_lurie2015]] The study was observational, but it fits the physiology of missed treatment (Module 4).

**Disasters disrupt care and increase harm.** Dialysis patients in areas hit by Sandy had more emergency department visits and hospitalizations, and a small rise in deaths, compared with patients in unaffected regions.[[uom_kelman2015]]

**The lessons are the same across Asia and the Pacific.** Reviews of earthquakes, tsunamis, and typhoons in the region, including the Philippines, describe the same priorities: tracking every patient, pre-agreed transfer arrangements, emergency supplies, and staff welfare.[[uom_gray2015]]

## Calculator CALC-12: outage autonomy

You need: usable generator fuel in liters, the generator's consumption per hour at expected load, the number of active machines, the dialysate flow rate, other treated-water use per hour (rinsing, reprocessing, reverse osmosis reject not recycled), and usable treated-water storage.

{{formula:**Generator runtime (hours)** = usable fuel ÷ consumption per hour.<br>**Treated-water demand (liters per hour)** = machines × dialysate flow (liters per minute) × 60 + other use.<br>**Water autonomy (hours)** = usable treated-water storage ÷ demand.<br>**Operating autonomy** = the smaller of the two. That is the binding constraint.<br>**Sessions possible** = operating autonomy ÷ session length × machines, rounded down.}}

**Worked example.** The unit has 400 liters of fuel and burns 22 liters an hour: about 18 hours. Fifteen machines at 500 milliliters a minute use 15 × 0.5 × 60 = 450 liters an hour, plus 100 liters an hour of other use, for 550 liters an hour. With 3,000 liters of storage, water lasts 3,000 ÷ 550 = about 5.5 hours. Water is the binding constraint: enough for one full shift of 4-hour sessions on all 15 machines, not two. The plan needs a water tanker agreement or fewer stations, not more diesel.

{{fig:uom12b}}

Check generator sizing with the biomedical technician. Consumption depends on load, and the reverse osmosis pumps add a lot of it.

{{key:Find the binding constraint first. Solving the wrong shortage wastes the hours you have.}}

## A phased typhoon plan

{{flow:Typhoon plan by phase|Season start (May to June)::Test the generator under load, confirm fuel and water contracts, update every patient's emergency information sheet, pre-position at least two weeks of supplies, refresh the staff contact tree, confirm partner units.|Advisory (72 hours before landfall)::Monitor PAGASA bulletins. The Medical Director decides on early dialysis. Notify patients of revised schedules. Top up fuel and water. Move records and equipment above flood level.|Imminent (24 hours)::Complete early sessions. Give each patient the emergency information sheet and the dietitian's emergency diet guidance. Confirm where each patient will shelter. Identify staff who will stay on site, with food and a place to sleep.|During::Close safely if travel is dangerous. Keep communication open. Record every patient contact.|Recovery::Inspect the building, power, and water. Have the water tested and released before treatment (Module 6). Reopen in phases, highest-risk patients first. Contact every patient. Arrange transfers for those who cannot reach the unit.}}

**Example.** With a Signal No. 3 typhoon forecast to make landfall in Eastern Samar on Thursday night, the manager of a unit in Borongan meets with the Medical Director on Tuesday. All Thursday and Friday patients are moved to Wednesday and early Thursday morning. By Thursday noon, every patient has been treated within the previous 36 hours and has a printed sheet in a plastic folder. The nurses call each patient on Saturday morning; 31 of 34 are reached. The barangay health workers find the other three in an evacuation center. The unit reopens on Sunday after the water is released, starting with the three patients whose families could not be reached.

{{call:When patients cannot reach the unit or the unit cannot open, the Medical Director or attending decides on transfers, early sessions, and changes to treatment. Your job is to know where every patient is and to make their decision happen.}}

## Partner units and transfer

Keep written memoranda of agreement with at least two partner units outside your likely hazard zone. Each agreement states how patients are referred, what records travel with them (prescription, serology, access type, PhilHealth Dialysis Database status), and how billing is handled. Test it once a year by sending one transient patient through the process.

## Common failure modes

- **The generator that was never loaded.** Tested every week with no machines running.
- **Power only.** Planning for electricity and forgetting water.
- **The list in the dead computer.** Patient contacts only in the electronic system that went down.
- **Paper partners.** Agreements signed and never used.
- **Late decisions.** Waiting for landfall to decide on early dialysis.

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
