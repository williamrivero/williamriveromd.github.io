# 06. Water and dialysate readiness

## The big picture

{{plain:A person drinks about two liters of water a day, and the gut and liver filter what is in it. A dialysis patient's blood meets 120 to 150 liters of water-based dialysate in a single session, separated only by a thin membrane. Anything in that water that the membrane lets through goes straight into the blood. That is why water that is safe to drink can be dangerous to dialyze.}}

The picture has a limit. The membrane is a filter, but not a wall. Most bacteria cannot cross an intact membrane, yet their fragments, called endotoxins, can, and so can chemicals like chlorine and aluminum. The danger is not dramatic. Contaminated water rarely looks or smells different. It shows up as a patient who shivers and spikes a fever an hour into treatment, or as a cluster of patients with unexplained anemia weeks later.

You will not test water or decide whether a reverse osmosis membrane is failing. Your job is to make sure that every required test happens, is recorded, is read, and that no patient is dialyzed on water nobody has released.

{{cards:Key terms for this module|Dialysate::The fluid on the other side of the dialyzer membrane, made from treated water and concentrate.|Carbon bed::A tank of activated carbon that removes chlorine and chloramine.|Reverse osmosis (RO)::The membrane system that removes most salts, metals, and microbes.|Distribution loop::The pipes that carry treated water to each machine, where bacteria can regrow.|Colony-forming units (CFU)::The count of living bacteria in a water sample.|Endotoxin units (EU)::The measure of bacterial fragments that can cause fever and inflammation.|Action level::The early-warning line, usually half the maximum, that triggers disinfection and retesting.|Release::The signed decision that water is safe to use for treatment.}}

## Learning objectives

1. Explain why dialysis water must meet a far stricter standard than drinking water, using the volume and membrane argument.
2. Describe the treatment train (pretreatment, carbon, reverse osmosis, distribution loop) and where samples are drawn.
3. Verify that a water log is complete and traceable, and recognize a result above an action level.
4. Coordinate a safety hold, affected-scope assessment and documented release without making technical decisions outside your role.

## Field case: the copied value

**Situation.** It is 05:15 on a Wednesday at a 14-station unit in Cabanatuan, Nueva Ecija. The first shift starts at 06:00. The water log has every entry for the morning except one: total chlorine at the outlet of the first carbon bed, which must be tested before each shift.

The night technician, Mr. Arnel Bautista, finished at 05:00 and has gone home. The day technician arrives at 06:30. A staff nurse, trying to help, says to the manager, Ms. Kristine Pascual: "Ma'am, the result is always 0.02. Just copy yesterday's so we can start."

**Before reading on, decide:**

- What could happen if the carbon bed has failed and the value is copied?
- What can Ms. Pascual decide, and what must she leave to others?
- What would she fix after this morning is over?

**Case review.**

**Why not copy.** If the first carbon bed has broken through, chloramine reaches the dialysate within minutes of the first treatment. Chloramine damages red blood cells: patients can develop hemolysis, with back pain, chest tightness, and falling hemoglobin, sometimes in several patients at once. A copied value would hide the one test designed to catch that.

**What she decides.** Ms. Pascual says no, places the opening on hold, and calls Mr. Bautista back and the on-call biomedical lead. She tells the head nurse and the physician on duty there may be a delay. She does not run the test herself or judge the result.

**The release.** Mr. Bautista returns at 05:35, tests the outlet, and records 0.02 milligrams per liter, within the facility limit. He signs, and the Medical Director's designee releases the water. The first patients start 15 minutes late. Ms. Pascual explains the delay to the waiting patients without blaming anyone.

**The fix.** The real gap was the schedule: the night shift ended at 05:00, and no one was assigned the pre-opening test. The technician schedule now overlaps by 30 minutes, and the log has a mandatory "tested by" field before the opening line can be signed.

{{fig:uom06c}}

## The mechanism: why dialysis water is different

Dialyzer membranes let small molecules pass in both directions. Anything dissolved in the dialysate that is lower in the patient's blood moves into the patient. Three groups of contaminants matter.

{{fig:uom06a}}

**Chemicals.** Chlorine and chloramine, added by water suppliers to kill bacteria, damage red blood cells and cause hemolysis and methemoglobinemia. Aluminum once caused dialysis dementia and bone disease. Fluoride, copper, nitrates, and heavy metals have each caused clusters of harm.

**Microbes.** Bacteria rarely cross an intact membrane, but their fragments do. Endotoxin and other bacterial products can cross, especially with high-flux membranes, and trigger fever, chills, and chronic inflammation.

**Toxins.** In 1996, in Caruaru, Brazil, dialysis water drawn from a reservoir contaminated by blue-green algae carried microcystin toxins into patients. Dozens died of acute liver failure.[[dch_jochimsen1998]] Every safeguard in this module exists because something like that once happened somewhere.

### The treatment train

Each stage protects the next.

{{flow:The water treatment train|Pretreatment::Sediment filters and a softener remove particles, calcium, and magnesium that would scale the reverse osmosis membrane.|Carbon beds::Remove chlorine and chloramine. Usually two in series, so a breakthrough in the first is caught before the water moves on. Total chlorine is tested at the first bed's outlet before each shift.|Reverse osmosis::Removes most dissolved salts, metals, and microbes. Monitored by conductivity and rejection rate.|Storage and distribution loop::The most common site of bacterial regrowth and biofilm. Needs scheduled disinfection.|Point of use::The machine and, where used, endotoxin-retentive filters.}}

## What the standards say

The international standard for dialysis fluids is the International Organization for Standardization (ISO) 23500 series, second edition 2024.[[iso23500_1]] Its microbiological limits:

| Fluid | Living bacteria, maximum | Endotoxin, maximum | Action level |
|---|---|---|---|
| Dialysis water | Less than 100 CFU/mL | Less than 0.25 EU/mL | Usually half the maximum (50 CFU/mL; 0.125 EU/mL) |
| Standard dialysis fluid | Less than 100 CFU/mL | Less than 0.5 EU/mL | Usually half the maximum |
| Ultrapure dialysis fluid | Less than 0.1 CFU/mL | Less than 0.03 EU/mL | Set by the program |

The **action level** is the early-warning line. Reaching it means disinfect, investigate, and retest before you reach the maximum. United States Medicare regulations still refer to older, looser limits, which shows that authorities differ. **In the Philippines, DOH AO 2013-0003 and your facility's approved water program set the controlling numbers, sampling points, and frequencies.**[[dch_doh2013]] Know exactly where those are written in your unit.

**How strong is the evidence?** These limits are established standards, built from outbreak investigations, physiology, and expert consensus. Ultrapure dialysate is associated in observational studies with lower inflammatory markers, but whether it improves survival in routine hemodialysis is not established.

## Your role: completeness, hold, and release

You make sure that:

- the sampling schedule exists, and every scheduled test has a result;
- each result is linked to a time, a sampling point, an operator, and a reviewer;
- results above an action level trigger a documented response;
- a missing result triggers a hold, never an assumption;
- release after a hold is signed by the authorized technical and clinical owners.

{{key:You own the completeness of the water record. You never own the water release.}}

## Calculator CALC-04: water-result action-level checker

This is a teaching tool, not a release tool. You enter the fluid type, the bacterial count, the endotoxin result, and the facility's maximum and action levels (prefilled with ISO defaults, editable to match your program).

{{formula:**Below the action level:** within program limits; file with the reviewer's signature.<br>**At or above the action level but below the maximum:** notify the water technician and Medical Director; disinfect and retest according to the program.<br>**At or above the maximum:** start a hold and a review of which treatments may have been affected, according to policy.}}

**Worked example.** A loop sample shows 62 CFU/mL and 0.08 EU/mL, checked against the ISO defaults for dialysis water. The bacterial count is above the action level (50) but below the maximum (100). Endotoxin is below its action level (0.125). The result is an action-level response for bacteria: disinfect the loop, find out why, and retest.

The checker never says "release." Release is a signed decision by authorized people.

## Doing it on Monday: auditing a water log

{{fig:uom06b}}

Check every line for six things:

1. Date and time of the sample.
2. Sampling point, named and matching the map.
3. The test and its result, with units.
4. Operator initials.
5. Reviewer signature and date.
6. For any result out of range: the action taken, the retest result, and the release signature.

Then look for red flags: identical values day after day, a whole week of results in the same handwriting and ink, blank reviewer fields, and corrections without initials.

**Example.** A manager in Dagupan audits a month of logs and finds the endotoxin results for the distribution loop reported as "0.03" for 18 consecutive samples, including two days when the technician was on leave. The values may be real. They may also have been written in advance. She does not accuse anyone. She asks the technician to show her the laboratory reports for those 18 samples. Six cannot be found. The finding goes into a corrective action, and the Medical Director decides what retesting is needed.

{{call:Hold the affected loop or stations when a critical water result is missing, untraceable, or above the maximum. Call the water technician and the Medical Director. Treatment restarts only on a signed release.}}

## Dialyzer reprocessing and water

Units that reprocess dialyzers use treated water for rinsing and for preparing the germicide. That water must meet the same standard. Include the reprocessing points in your sampling map.

## Common failure modes

- **The old map.** A sampling map that no longer matches the pipes after a renovation.
- **Cultures sent, never read.** Monthly results received and filed without review.
- **Busy-month shortcuts.** Loop disinfection skipped in December.
- **The clock wins.** Pressure to open on time overriding a missing test.
- **Perfect numbers.** Values so consistent that no one asks whether they were measured.

## Supervised practice

- [ ] Walk the water system with the technician and mark every sampling point on the facility map.
- [ ] Audit one month of logs for the six required elements.
- [ ] Run CALC-04 on last quarter's culture and endotoxin results.
- [ ] Rehearse a hold notification and release sign-off with the technician and the Medical Director's designee.

## Question bank

**Q1.** Why must dialysis water be purer than drinking water?
- [x] Patients are exposed to over a hundred liters per session through a thin membrane
- [ ] Dialysis machines rust faster
- [ ] Drinking water is never tested
- [ ] Patients drink dialysate
> Volume and direct blood exposure make trace contaminants dangerous.

**Q2.** What do chlorine and chloramine cause if they reach a patient?
- [x] Hemolysis and methemoglobinemia
- [ ] Hypoglycemia
- [ ] Hair loss
- [ ] Bone fractures within hours
> Oxidants damage red blood cells.

**Q3.** Why are carbon beds usually installed in series?
- [x] So breakthrough in the first bed is caught before water moves on
- [ ] To double the water pressure
- [ ] To soften water
- [ ] To add minerals
> The second bed provides a safety margin.

**Q4.** The ISO maximum for viable microbes in dialysis water is:
- [x] Less than 100 CFU/mL
- [ ] Less than 1,000 CFU/mL
- [ ] Less than 0.1 CFU/mL
- [ ] There is no limit
> Ultrapure fluid has the 0.1 CFU/mL limit.

**Q5.** The ISO maximum endotoxin level for dialysis water is:
- [x] Less than 0.25 EU/mL
- [ ] Less than 2 EU/mL
- [ ] Less than 5 EU/mL
- [ ] Less than 0.0001 EU/mL
> Older US limits allowed 2 EU/mL.

**Q6.** What does reaching an action level mean?
- [x] Investigate, disinfect and retest before the maximum is reached
- [ ] Stop dialysis permanently
- [ ] Nothing until the maximum is exceeded
- [ ] Change the water supplier
> Action levels are early warnings.

**Q7.** Which part of the system most commonly develops bacterial regrowth?
- [x] Storage and distribution loop
- [ ] Softener salt tank only
- [ ] The electrical panel
- [ ] The waiting room tap
> Low flow and dead legs promote biofilm.

**Q8.** A morning chlorine result is missing. You should:
- [x] Hold the opening until the test is run and released
- [ ] Copy yesterday's value
- [ ] Open and test at noon
- [ ] Ask a patient to taste the water
> Missing evidence means the water is not released.

**Q9.** Who releases water after a hold?
- [x] The authorized technical and clinical owners, by signature
- [ ] The operations manager alone
- [ ] Any nurse
- [ ] The vendor by phone
> Release requires technical interpretation and clinical accountability.

**Q10.** What caused the 1996 Caruaru tragedy?
- [x] Cyanobacterial toxins in dialysis water
- [ ] Wrong dialysate potassium
- [ ] A power outage
- [ ] Machine software failure
> Microcystins caused acute liver failure and dozens of deaths.

**Q11.** Which result needs action under ISO defaults: 62 CFU/mL in dialysis water?
- [x] Above the action level, below the maximum
- [ ] Above the maximum
- [ ] Below the action level
- [ ] Not measurable
> Action level 50, maximum 100.

**Q12.** Which document sets the controlling numbers in a Philippine unit?
- [x] DOH AO 2013-0003 and the facility's approved water program
- [ ] A vendor brochure
- [ ] The patient handbook
- [ ] Social media posts
> Local regulation and the approved program govern.

**Q13.** A water log shows identical values every day for a month in the same handwriting. This suggests:
- [x] Possible copied or fabricated entries needing investigation
- [ ] Excellent stability
- [ ] Normal practice
- [ ] Equipment upgrade
> Real measurements vary. Uniformity is a red flag.

**Q14.** Is ultrapure dialysate proven to improve survival in routine hemodialysis?
- [x] Not established; observational data link it to lower inflammation
- [ ] Yes, by multiple large randomized trials
- [ ] It is proven harmful
- [ ] It has never been studied
> Benefit on hard outcomes remains unproven.

**Q15.** Why include dialyzer reprocessing in the water sampling map?
- [x] Reprocessing uses treated water that must meet the same standard
- [ ] Reprocessing does not use water
- [ ] It reduces the number of tests
- [ ] PhilHealth requires photos
> Contaminated rinse water contaminates reused dialyzers.

## Sources

PH1, PH3, PH6, INT2, E10. [Evidence and source register](../requirements.md#source-register-and-review-items).

[Module index](../syllabus.md#module-sequence) · [Trainer guide](../trainer.md)
