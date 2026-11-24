# 06. Water and dialysate readiness

**Core** · 45 minutes study · 45 minutes supervised practice · Source review date: November 24, 2026
**Figures:** FIG-06 (Understand) · FIG-06B (Apply) · FIG-06C (Appreciate) · **Calculator:** CALC-04 Water-result action-level checker (educational)

> **Why this matters.** A person drinks about 2 liters of water a day, filtered by the gut and the liver before anything reaches the blood. A hemodialysis patient is exposed to roughly 120 to 200 liters of dialysate per session, separated from the blood only by a thin membrane, three times a week. Contaminants that would be harmless in drinking water become toxic at that volume. Water is the unit's most dangerous invisible drug, and you run the system that decides whether it is released.

## Learning objectives

1. Explain why dialysis water must meet a far stricter standard than drinking water, using the volume and membrane argument.
2. Describe the treatment train (pretreatment, carbon, reverse osmosis, distribution loop) and where samples are drawn.
3. Verify that a water log is complete and traceable, and recognize a result above an action level.
4. Coordinate a safety hold, affected-scope assessment and documented release without making technical decisions outside your role.

## The mechanism: why dialysis water is different

Dialyzer membranes let small molecules pass in both directions. Anything dissolved in dialysate that is lower in the patient's blood moves into the patient. Three groups of contaminants matter:

- **Chemical.** Chlorine and chloramine (added by municipal suppliers to kill bacteria) oxidize hemoglobin and cause hemolysis and methemoglobinemia. Aluminum historically caused dialysis encephalopathy and bone disease. Fluoride, copper, nitrates and heavy metals have each caused clusters of harm.
- **Microbiological.** Bacteria themselves rarely cross an intact membrane, but their fragments do. Endotoxin and other bacterial products can cross, especially with high-flux membranes, and trigger fever, chills and chronic inflammation.
- **Toxins.** In 1996, in Caruaru, Brazil, dialysis water drawn from a reservoir contaminated by cyanobacteria carried microcystins into patients. Dozens died of acute liver failure. Every safeguard in this module exists because something like that once happened.

### The treatment train

Each stage protects the next one:

1. **Pretreatment**: sediment filters, softener (removes calcium and magnesium that would scale the RO membrane).
2. **Carbon beds**: remove chlorine and chloramine. Usually two in series, because breakthrough in the first must be caught before the water moves on. Total chlorine is tested at the outlet of the first bed before each shift.
3. **Reverse osmosis (RO)**: removes most dissolved salts, metals and microbes. Monitored by conductivity and rejection rate.
4. **Storage and distribution loop**: the most common site of bacterial regrowth and biofilm. Requires scheduled disinfection.
5. **Point of use**: the machine and, where used, endotoxin-retentive filters.

## What the standards say

The international standard for dialysis fluids is the ISO 23500 series (second edition 2024). Its microbiological limits:

| Fluid | Viable microbes, maximum | Endotoxin, maximum | Action level |
|---|---|---|---|
| Dialysis water | < 100 CFU/mL | < 0.25 EU/mL | Typically 50% of the maximum (50 CFU/mL; 0.125 EU/mL) |
| Standard dialysis fluid | < 100 CFU/mL | < 0.5 EU/mL | Typically 50% of the maximum |
| Ultrapure dialysis fluid | < 0.1 CFU/mL | < 0.03 EU/mL | Set by program |

The **action level** is your early-warning line: reaching it means disinfect, investigate and retest before you reach the maximum. US Medicare regulations still reference older, looser limits (< 200 CFU/mL; < 2 EU/mL), which shows that standards differ between authorities. **In the Philippines, DOH AO 2013-0003 and your facility's approved water program set the controlling numbers, sampling points and frequencies.** Know where those are written.

**Evidence strength.** These limits are **established standards** built from outbreak investigations, physiology and expert consensus. Ultrapure dialysate is associated in observational studies with lower inflammatory markers, but whether it improves survival in routine hemodialysis is **not established**.

## Your role: completeness, hold and release

You do not interpret a chlorine test or decide whether an RO membrane is failing. The water technician and biomedical lead do that, with the Medical Director accountable. You make sure:

- the sampling schedule exists and every scheduled test has a result;
- each result is linked to time, sampling point, operator and reviewer;
- results above an action level trigger a documented response;
- missing results trigger a hold, not an assumption;
- release after a hold is signed by the authorized technical and clinical owners.

## Calculator CALC-04: water-result action-level checker (educational)

**Inputs:** fluid type (water, standard dialysate, ultrapure), viable count (CFU/mL), endotoxin (EU/mL), local maximum and action levels (prefilled with ISO defaults, editable to match the facility program).

**Logic**

- Below action level: "Within program limits. File with reviewer signature."
- At or above the action level and below the maximum: "Action level reached. Notify the water technician and Medical Director; disinfect and retest per program."
- At or above the maximum: "Exceeds maximum. Initiate hold and affected-scope review per policy."

**Worked example.** Loop sample 62 CFU/mL and 0.08 EU/mL against ISO water defaults: microbial count above action level (50) but below maximum (100); endotoxin below action level (0.125). Output: action-level response for microbial count.

**Guardrail.** The calculator never outputs "release." Release is a signed decision by authorized people.

## Doing it on Monday: auditing a water log

Check every line for:

1. Date and time of sample.
2. Sampling point (named, matching the map).
3. Test and result with units.
4. Operator initials.
5. Reviewer signature and date.
6. For any out-of-range result: the action taken, the retest result and release signature.

Red flags: identical values day after day, results entered in the same handwriting at the same time for a whole week, blank reviewer fields, corrections with no initials.

## Field case: the copied value

**Situation.** At 05:15 the morning total chlorine result is missing. A staff member says, "It's always the same, just copy yesterday's."

**Problem.** If the carbon bed has broken through, chloramine reaches patients within minutes of the first treatment. The copied value would hide it.

**Solution.** The manager declines, places the opening on hold, calls the water technician to run the test, and informs the head nurse and POD of a possible delay. The test is run at 05:35, the result is within limits, the technician signs and the Medical Director's designee releases. Patients start 15 minutes late. The manager then finds the root cause: the night technician's shift ended at 05:00 and no one was assigned the pre-opening test. The schedule is fixed.

## Dialyzer reprocessing and water

Units that reprocess dialyzers use treated water for rinsing and germicide preparation. That water must meet the same quality standard. Include reprocessing points in your sampling map.

## Common failure modes

- A sampling map that does not match the physical system after renovations.
- Monthly cultures sent but results never reviewed.
- Disinfection of the distribution loop skipped during busy months.
- Pressure to open on time overriding a missing test.

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
