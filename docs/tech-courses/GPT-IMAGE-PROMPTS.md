# GPT image prompts — Renal Care Academy technician tracks

**Site:** renalcarematters.com · **Prepared:** November 23, 2026 · **Images:** 135 (100 core ★, 35 optional ○; 26 heroes, 3 circuit figures)

This file is self-contained. Each gray block is one complete Constitution v1.0 prompt: paste it into a fresh ChatGPT image chat, generate, then run its Layer G checklist before saving under the filename on the entry.

## How to produce

1. One figure per chat. Ask for the canvas size on the entry.
2. Check text first: compare every label with the verbatim list. If one word is wrong, ask for that word to be fixed, not for a new image.
3. Reject an image with an invented number, a brand, a dark background, flat clip-art rendering, or a missing or altered footer (`© renalcarematters.com`). Heroes are the exception: they carry no text at all.
4. Circuit figures (marked in the list) are generated with the `dialysis-circuit-schematic` skill, not from a prompt in this file.
5. Save as PNG under the exact filename into `images/`, then run `python3 tools/techcourses/prep_assets.py` and `python3 generate_tech_courses.py --patch`. Hemodialysis Technician figure A of each module replaces the flat teaching diagram automatically; other figures appear once they are added to `tools/techcourses/figs.py` and placed with a `{{fig:key}}` macro in the module.
6. Production order: core figures first, track by track; optional figures last.
7. Every figure needs Dr. Rivero's review before publication. Numbers appear only where the lesson states them.

## Production list

| # | ID | Figure | File | Type |
|---|---|---|---|---|
| 1 | HD-01-A ★ | Map of a dialysis unit | `images/hemodialysis-technician-01-unit-map.png` | aid |
| 2 | HD-01-B ★ | Who decides what | `images/hemodialysis-technician-01-team-roles.png` | aid |
| 3 | HD-01-C ○ | SBAR handoff card | `images/hemodialysis-technician-01-sbar-card.png` | card |
| 4 | HD-02-A ★ | From blood to urine, and four kidney jobs | `images/hemodialysis-technician-02-kidneys-kidney-failure-teaching-diagram.png` | aid |
| 5 | HD-02-B ★ | What builds up when kidneys fail | `images/hemodialysis-technician-02-what-builds-up.png` | aid |
| 6 | HD-02-C ○ | Reading a weight trend | `images/hemodialysis-technician-02-weight-trend.png` | card |
| 7 | HD-03-A ★ | Five treatment pathways | `images/hemodialysis-technician-03-treatment-options-living-with-kidney-failure-teaching-diagram.png` | aid |
| 8 | HD-03-B ★ | Teach-back in four steps | `images/hemodialysis-technician-03-teach-back.png` | flow |
| 9 | HD-03-C ○ | Home dialysis equipment at a glance | `images/hemodialysis-technician-03-home-equipment.png` | aid |
| 10 | HD-04-A ★ | Diffusion and ultrafiltration across the membrane | `images/hemodialysis-technician-04-principles-of-hemodialysis-teaching-diagram.png` | aid |
| 11 | HD-04-B ★ | Tea bag, coffee press, river | `images/hemodialysis-technician-04-everyday-pictures.png` | aid |
| 12 | HD-04-C ★ | Four fluid numbers that are not the same | `images/hemodialysis-technician-04-fluid-numbers.png` | card |
| 13 | HD-04-D ○ | The hemodialysis blood circuit | `images/hemodialysis-technician-04-blood-circuit.png` | circuit |
| 14 | HD-05-A ★ | Station turnover sequence | `images/hemodialysis-technician-05-infection-prevention-waste-management-teaching-diagram.png` | flow |
| 15 | HD-05-B ★ | Clean and used never cross | `images/hemodialysis-technician-05-clean-used-zones.png` | aid |
| 16 | HD-05-C ○ | Sorting waste at the point of use | `images/hemodialysis-technician-05-waste-sorting.png` | card |
| 17 | HD-06-A ★ | Two circuits that meet at the dialyzer | `images/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit-teaching-diagram.png` | circuit |
| 18 | HD-06-B ★ | What each safeguard watches and cannot see | `images/hemodialysis-technician-06-safeguards.png` | aid |
| 19 | HD-06-C ○ | When a machine fails a check | `images/hemodialysis-technician-06-failed-check.png` | flow |
| 20 | HD-07-A ★ | From tap to station | `images/hemodialysis-technician-07-water-treatment-concentrates-dialysate-teaching-diagram.png` | aid |
| 21 | HD-07-B ★ | Which test answers which question | `images/hemodialysis-technician-07-which-test.png` | card |
| 22 | HD-07-C ○ | How the machine makes dialysate | `images/hemodialysis-technician-07-making-dialysate.png` | aid |
| 23 | HD-08-A ★ | Three types of hemodialysis access | `images/hemodialysis-technician-08-vascular-access-recognition-protection-teaching-diagram.png` | aid |
| 24 | HD-08-B ★ | Look, listen, feel | `images/hemodialysis-technician-08-look-listen-feel.png` | aid |
| 25 | HD-08-C ○ | Protecting the access arm | `images/hemodialysis-technician-08-protect-access.png` | card |
| 26 | HD-09-A ★ | One session, three phases | `images/hemodialysis-technician-09-the-hemodialysis-session-teaching-diagram.png` | flow |
| 27 | HD-09-B ★ | What to look at on every round | `images/hemodialysis-technician-09-every-round.png` | aid |
| 28 | HD-09-C ○ | Checking an unexpected weight | `images/hemodialysis-technician-09-unexpected-weight.png` | flow |
| 29 | HD-10-A ★ | Your first thirty seconds | `images/hemodialysis-technician-10-complications-emergency-response-teaching-diagram.png` | flow |
| 30 | HD-10-B ★ | Signs that need help immediately | `images/hemodialysis-technician-10-red-flags.png` | card |
| 31 | HD-10-C ○ | When water or power fails | `images/hemodialysis-technician-10-utility-failure.png` | flow |
| 32 | HD-11-A ★ | Traceability: release or hold | `images/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality-teaching-diagram.png` | flow |
| 33 | HD-11-B ★ | What a dialyzer label must tell you | `images/hemodialysis-technician-11-dialyzer-label.png` | aid |
| 34 | HD-11-C ○ | From fault to return to service | `images/hemodialysis-technician-11-return-to-service.png` | flow |
| 35 | HD-12-A ★ | Five practical stations | `images/hemodialysis-technician-12-integrated-practice-competency-assessment-teaching-diagram.png` | aid |
| 36 | HD-12-B ★ | Verify, pause, report, confirm, record, release | `images/hemodialysis-technician-12-six-habits.png` | flow |
| 37 | HD-12-C ○ | Observed, supervised, signed off | `images/hemodialysis-technician-12-three-levels.png` | card |
| 38 | WATER-H0 ★ | Hub hero | `images/water-treatment-technician-vignette-hero.png` | hero |
| 39 | WATER-01-H ★ | M1 hero | `images/water-treatment-technician-01-why-dialysis-water-is-different-vignette-hero.png` | hero |
| 40 | WATER-01-A ★ | A glass of water and a week of dialysis | `images/water-treatment-technician-01-exposure-volume.png` | aid |
| 41 | WATER-01-B ★ | Three groups of contaminants | `images/water-treatment-technician-01-contaminant-groups.png` | aid |
| 42 | WATER-01-C ○ | Three levels of purity | `images/water-treatment-technician-01-purity-levels.png` | card |
| 43 | WATER-02-H ★ | M2 hero | `images/water-treatment-technician-02-source-water-system-design-vignette-hero.png` | hero |
| 44 | WATER-02-A ★ | Three sources, three problems | `images/water-treatment-technician-02-source-comparison.png` | aid |
| 45 | WATER-02-B ★ | Reading the system drawing | `images/water-treatment-technician-02-system-drawing.png` | aid |
| 46 | WATER-02-C ○ | Sizing for the busiest, coldest hour | `images/water-treatment-technician-02-sizing.png` | flow |
| 47 | WATER-03-H ★ | M3 hero | `images/water-treatment-technician-03-sediment-filtration-softening-vignette-hero.png` | hero |
| 48 | WATER-03-A ★ | Reading the pressure drop | `images/water-treatment-technician-03-pressure-drop.png` | aid |
| 49 | WATER-03-B ★ | The softener cycle | `images/water-treatment-technician-03-softener-cycle.png` | flow |
| 50 | WATER-03-C ○ | Inside the brine tank | `images/water-treatment-technician-03-brine-tank.png` | aid |
| 51 | WATER-04-H ★ | M4 hero | `images/water-treatment-technician-04-carbon-tanks-chlorine-control-vignette-hero.png` | hero |
| 52 | WATER-04-A ★ | Worker and polisher | `images/water-treatment-technician-04-worker-polisher.png` | aid |
| 53 | WATER-04-B ★ | Empty-bed contact time | `images/water-treatment-technician-04-ebct.png` | card |
| 54 | WATER-04-C ★ | Acting on the chlorine result | `images/water-treatment-technician-04-chlorine-decision.png` | flow |
| 55 | WATER-05-H ★ | M5 hero | `images/water-treatment-technician-05-reverse-osmosis-vignette-hero.png` | hero |
| 56 | WATER-05-A ★ | Inside a spiral-wound membrane | `images/water-treatment-technician-05-ro-membrane.png` | aid |
| 57 | WATER-05-B ★ | Rejection and recovery | `images/water-treatment-technician-05-rejection-recovery.png` | card |
| 58 | WATER-05-C ○ | Reading the changes | `images/water-treatment-technician-05-ro-trends.png` | aid |
| 59 | WATER-06-H ★ | M6 hero | `images/water-treatment-technician-06-distribution-loop-storage-filters-vignette-hero.png` | hero |
| 60 | WATER-06-A ★ | A loop that never stops | `images/water-treatment-technician-06-loop-layout.png` | aid |
| 61 | WATER-06-B ★ | Dead legs | `images/water-treatment-technician-06-dead-legs.png` | aid |
| 62 | WATER-06-C ○ | Storage tank done right | `images/water-treatment-technician-06-storage-tank.png` | aid |
| 63 | WATER-07-H ★ | M7 hero | `images/water-treatment-technician-07-concentrates-central-delivery-vignette-hero.png` | hero |
| 64 | WATER-07-A ★ | Two concentrates, one dialysate | `images/water-treatment-technician-07-two-concentrates.png` | aid |
| 65 | WATER-07-B ★ | Mixing bicarbonate safely | `images/water-treatment-technician-07-bicarbonate-mixing.png` | flow |
| 66 | WATER-07-C ○ | Central concentrate delivery | `images/water-treatment-technician-07-central-delivery.png` | aid |
| 67 | WATER-08-H ★ | M8 hero | `images/water-treatment-technician-08-daily-monitoring-logs-trends-vignette-hero.png` | hero |
| 68 | WATER-08-A ★ | The start-of-day round | `images/water-treatment-technician-08-daily-round.png` | flow |
| 69 | WATER-08-B ★ | A log that can be trusted | `images/water-treatment-technician-08-good-log.png` | card |
| 70 | WATER-08-C ○ | Trends before alarms | `images/water-treatment-technician-08-trend-chart.png` | aid |
| 71 | WATER-09-H ★ | M9 hero | `images/water-treatment-technician-09-chemical-microbiological-sampling-vignette-hero.png` | hero |
| 72 | WATER-09-A ★ | Collecting a sample | `images/water-treatment-technician-09-sampling-steps.png` | flow |
| 73 | WATER-09-B ★ | Where to sample | `images/water-treatment-technician-09-sample-points.png` | aid |
| 74 | WATER-09-C ○ | Limit and action level | `images/water-treatment-technician-09-action-level.png` | card |
| 75 | WATER-10-H ★ | M10 hero | `images/water-treatment-technician-10-disinfection-biofilm-control-vignette-hero.png` | hero |
| 76 | WATER-10-A ★ | How biofilm forms | `images/water-treatment-technician-10-biofilm.png` | aid |
| 77 | WATER-10-B ★ | Chemical disinfection, start to release | `images/water-treatment-technician-10-disinfection-cycle.png` | flow |
| 78 | WATER-10-C ○ | Heat or chemical | `images/water-treatment-technician-10-heat-vs-chemical.png` | card |
| 79 | WATER-11-H ★ | M11 hero | `images/water-treatment-technician-11-maintenance-replacement-validation-vignette-hero.png` | hero |
| 80 | WATER-11-A ★ | The maintenance calendar | `images/water-treatment-technician-11-maintenance-calendar.png` | aid |
| 81 | WATER-11-B ★ | After every change, re-test | `images/water-treatment-technician-11-post-change-tests.png` | card |
| 82 | WATER-11-C ○ | Before the service engineer leaves | `images/water-treatment-technician-11-service-handover.png` | flow |
| 83 | WATER-12-H ★ | M12 hero | `images/water-treatment-technician-12-failures-emergencies-capstone-vignette-hero.png` | hero |
| 84 | WATER-12-A ★ | Stop, hold, report | `images/water-treatment-technician-12-stop-hold-report.png` | flow |
| 85 | WATER-12-B ★ | Four failures, first response | `images/water-treatment-technician-12-four-failures.png` | card |
| 86 | WATER-12-C ○ | After a flood or long outage | `images/water-treatment-technician-12-after-flood.png` | flow |
| 87 | BIOMED-H0 ★ | Hub hero | `images/dialysis-biomedical-technician-vignette-hero.png` | hero |
| 88 | BIOMED-01-H ★ | M1 hero | `images/dialysis-biomedical-technician-01-role-and-safe-working-vignette-hero.png` | hero |
| 89 | BIOMED-01-A ★ | Before you open a machine | `images/dialysis-biomedical-technician-01-before-opening.png` | flow |
| 90 | BIOMED-01-B ★ | Four hazards | `images/dialysis-biomedical-technician-01-four-hazards.png` | aid |
| 91 | BIOMED-01-C ○ | The life of a fault | `images/dialysis-biomedical-technician-01-life-of-a-fault.png` | flow |
| 92 | BIOMED-02-H ★ | M2 hero | `images/dialysis-biomedical-technician-02-electrical-electronic-fundamentals-vignette-hero.png` | hero |
| 93 | BIOMED-02-A ★ | Sensor, controller, actuator | `images/dialysis-biomedical-technician-02-control-loop.png` | aid |
| 94 | BIOMED-02-B ★ | Power path and protective earth | `images/dialysis-biomedical-technician-02-power-path.png` | aid |
| 95 | BIOMED-02-C ○ | Multimeter safely | `images/dialysis-biomedical-technician-02-multimeter.png` | card |
| 96 | BIOMED-03-H ★ | M3 hero | `images/dialysis-biomedical-technician-03-dialysate-water-heating-degassing-vignette-hero.png` | hero |
| 97 | BIOMED-03-A ★ | From inlet to degassed warm water | `images/dialysis-biomedical-technician-03-inlet-heat-degas.png` | aid |
| 98 | BIOMED-03-B ★ | Why bubbles matter | `images/dialysis-biomedical-technician-03-bubbles.png` | aid |
| 99 | BIOMED-03-C ○ | A scaled heater | `images/dialysis-biomedical-technician-03-scaled-heater.png` | aid |
| 100 | BIOMED-04-H ★ | M4 hero | `images/dialysis-biomedical-technician-04-proportioning-conductivity-bypass-vignette-hero.png` | hero |
| 101 | BIOMED-04-A ★ | Mixing and checking dialysate | `images/dialysis-biomedical-technician-04-proportioning.png` | aid |
| 102 | BIOMED-04-B ★ | Bypass: the safe state | `images/dialysis-biomedical-technician-04-bypass.png` | aid |
| 103 | BIOMED-04-C ○ | The total, not the recipe | `images/dialysis-biomedical-technician-04-total-not-recipe.png` | card |
| 104 | BIOMED-05-H ★ | M5 hero | `images/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration-vignette-hero.png` | hero |
| 105 | BIOMED-05-A ★ | The balancing chamber | `images/dialysis-biomedical-technician-05-balancing-chamber.png` | aid |
| 106 | BIOMED-05-B ★ | Silent errors | `images/dialysis-biomedical-technician-05-silent-errors.png` | aid |
| 107 | BIOMED-05-C ○ | Checking ultrafiltration accuracy | `images/dialysis-biomedical-technician-05-uf-check.png` | flow |
| 108 | BIOMED-06-H ★ | M6 hero | `images/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump-vignette-hero.png` | hero |
| 109 | BIOMED-06-A ★ | The blood circuit and its monitoring points | `images/dialysis-biomedical-technician-06-blood-circuit-monitoring.png` | circuit |
| 110 | BIOMED-06-B ★ | Inside the roller pump | `images/dialysis-biomedical-technician-06-roller-pump.png` | aid |
| 111 | BIOMED-06-C ○ | Reading the pressures | `images/dialysis-biomedical-technician-06-pressures.png` | card |
| 112 | BIOMED-07-H ★ | M7 hero | `images/dialysis-biomedical-technician-07-protective-systems-alarm-testing-vignette-hero.png` | hero |
| 113 | BIOMED-07-A ★ | The air protection chain | `images/dialysis-biomedical-technician-07-air-chain.png` | flow |
| 114 | BIOMED-07-B ★ | The blood leak detector | `images/dialysis-biomedical-technician-07-blood-leak-detector.png` | aid |
| 115 | BIOMED-07-C ○ | Sense, act, tell | `images/dialysis-biomedical-technician-07-sense-act-tell.png` | card |
| 116 | BIOMED-08-H ★ | M8 hero | `images/dialysis-biomedical-technician-08-preventive-maintenance-program-vignette-hero.png` | hero |
| 117 | BIOMED-08-A ★ | From manual to calendar | `images/dialysis-biomedical-technician-08-pm-calendar.png` | flow |
| 118 | BIOMED-08-B ★ | A staggered year | `images/dialysis-biomedical-technician-08-staggered-year.png` | aid |
| 119 | BIOMED-08-C ○ | What is in a maintenance kit | `images/dialysis-biomedical-technician-08-pm-kit.png` | aid |
| 120 | BIOMED-09-H ★ | M9 hero | `images/dialysis-biomedical-technician-09-calibration-test-equipment-vignette-hero.png` | hero |
| 121 | BIOMED-09-A ★ | Calibrating one parameter | `images/dialysis-biomedical-technician-09-calibration-steps.png` | flow |
| 122 | BIOMED-09-B ★ | Who checks the checker | `images/dialysis-biomedical-technician-09-traceability-chain.png` | aid |
| 123 | BIOMED-09-C ○ | Five things calibrated | `images/dialysis-biomedical-technician-09-calibrated-parameters.png` | card |
| 124 | BIOMED-10-H ★ | M10 hero | `images/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene-vignette-hero.png` | hero |
| 125 | BIOMED-10-A ★ | Three deposits, three answers | `images/dialysis-biomedical-technician-10-deposits.png` | aid |
| 126 | BIOMED-10-B ★ | A disinfection cycle with proof | `images/dialysis-biomedical-technician-10-machine-disinfection.png` | flow |
| 127 | BIOMED-10-C ○ | The filter at the machine | `images/dialysis-biomedical-technician-10-machine-filter.png` | aid |
| 128 | BIOMED-11-H ★ | M11 hero | `images/dialysis-biomedical-technician-11-electrical-safety-facility-utilities-vignette-hero.png` | hero |
| 129 | BIOMED-11-A ★ | Protective earth: the path that saves | `images/dialysis-biomedical-technician-11-earth-path.png` | aid |
| 130 | BIOMED-11-B ★ | An electrical safety test | `images/dialysis-biomedical-technician-11-safety-test.png` | flow |
| 131 | BIOMED-11-C ○ | Utilities at the station | `images/dialysis-biomedical-technician-11-station-utilities.png` | aid |
| 132 | BIOMED-12-H ★ | M12 hero | `images/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone-vignette-hero.png` | hero |
| 133 | BIOMED-12-A ★ | A method for any fault | `images/dialysis-biomedical-technician-12-fault-method.png` | flow |
| 134 | BIOMED-12-B ★ | One machine or several | `images/dialysis-biomedical-technician-12-shared-causes.png` | aid |
| 135 | BIOMED-12-C ○ | The life of a machine | `images/dialysis-biomedical-technician-12-machine-life-cycle.png` | aid |

# Hemodialysis Technician


## Module 1 — The Dialysis Unit and the Technician's Role

### HD-01-A ★ — Map of a dialysis unit

**File:** `images/hemodialysis-technician-01-unit-map.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part1`

**Job:** U: the learner can point to clean supply, treatment, used-item, and emergency areas and say what moves in which direction.

**Alt:** Overhead plan of a small dialysis unit with labeled clean supply room, treatment stations, isolation room, waste route, water room, emergency cart, and exit.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Map of a dialysis unit · academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Fictional floor plan. Clean supplies and used items never share a route. Each treatment station holds one chair, one machine, one patient. The water room and reprocessing room are separate rooms, not part of the treatment floor.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: the learner can point to clean supply, treatment, used-item, and emergency areas and say what moves in which direction.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Clean supply room
  • Treatment stations
  • Nurses' station
  • Isolation room
  • Used-item and waste route
  • Water room
  • Emergency cart
  • Exit
  • One station = one chair, one machine, one patient
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No real facility name or logo
✗ no patient faces
✗ no arrows that send used items through the clean supply room
✗ no more than eight stations
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Clean supply room" present and spelled exactly — confirmed
□ Label "Treatment stations" present and spelled exactly — confirmed
□ Label "Nurses' station" present and spelled exactly — confirmed
□ Label "Isolation room" present and spelled exactly — confirmed
□ Label "Used-item and waste route" present and spelled exactly — confirmed
□ Label "Water room" present and spelled exactly — confirmed
□ Label "Emergency cart" present and spelled exactly — confirmed
□ Label "Exit" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-01-B ★ — Who decides what

**File:** `images/hemodialysis-technician-01-team-roles.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part2`

**Job:** U: distinguishes the technician's tasks from nursing, prescribing, and equipment-service decisions.

**Alt:** Four team members in a row, each with a short label of what they decide: technician, dialysis nurse, nephrologist, and biomedical and water staff.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Who decides what · academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four roles in four equal columns. Technician: prepares, checks, observes, records, reports. Nurse: assesses the patient, directs care, delegates. Nephrologist: prescribes. Biomedical and water staff: repair and release equipment. No role is drawn larger or higher than another.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: distinguishes the technician's tasks from nursing, prescribing, and equipment-service decisions.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Technician: prepares, checks, reports
  • Dialysis nurse: assesses and directs care
  • Nephrologist: prescribes
  • Biomedical and water staff: repair and release
  • Report up, never decide alone
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No needles or syringes in the technician's hands
✗ no hierarchy pyramid
✗ no medication labels
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Technician: prepares, checks, reports" present and spelled exactly — confirmed
□ Label "Dialysis nurse: assesses and directs care" present and spelled exactly — confirmed
□ Label "Nephrologist: prescribes" present and spelled exactly — confirmed
□ Label "Biomedical and water staff: repair and release" present and spelled exactly — confirmed
□ Label "Report up, never decide alone" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-01-C ○ — SBAR handoff card

**File:** `images/hemodialysis-technician-01-sbar-card.png` · **Canvas:** 1024 × 1536, 2:3 portrait · **Placement:** academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part3`

**Job:** A: gives a structured report and confirms the instruction with check-back.

**Alt:** Reference card with the four SBAR steps and a final check-back step.

```text
Reference card · 1024 × 1536, 2:3 portrait · SBAR handoff card · academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four stacked steps in order S, B, A, R, followed by a fifth strip for check-back. Example text is the fictional identification mismatch from the lesson. No clinical values.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1024 × 1536, 2:3 portrait. Steps read top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: gives a structured report and confirms the instruction with check-back.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • S Situation: what is happening now
  • B Background: the facts that explain it
  • A Assessment: what does not match
  • R Recommendation: what I need from you
  • Check-back: repeat the instruction, wait for yes
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No patient name, date of birth, or record number
✗ no letters other than S B A R as the step initials
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "S Situation: what is happening now" present and spelled exactly — confirmed
□ Label "B Background: the facts that explain it" present and spelled exactly — confirmed
□ Label "A Assessment: what does not match" present and spelled exactly — confirmed
□ Label "R Recommendation: what I need from you" present and spelled exactly — confirmed
□ Label "Check-back: repeat the instruction, wait for yes" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 2 — Kidneys and Kidney Failure

### HD-02-A ★ — From blood to urine, and four kidney jobs

**File:** `images/hemodialysis-technician-02-kidneys-kidney-failure-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part1`

**Job:** U: traces filtrate from glomerulus through tubule to urine and names four kidney functions.

**Alt:** Enlarged nephron showing filtration, reabsorption, and urine formation, beside four icons for the kidney's main jobs, with a small locator kidney.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · From blood to urine, and four kidney jobs · academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
KIDNEY MASTER RULES apply to the small locator kidney (convex border lateral, hilum medial, pelvis at the hilum, calyces drain inward). The nephron is a standalone enlarged diagram, not drawn inside the kidney at organ scale. Glomerulus filters; tubule reclaims and secretes; collecting duct leads to the renal pelvis. Four functions: waste removal, fluid and salt balance, acid balance, hormones (erythropoietin and vitamin D activation).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: traces filtrate from glomerulus through tubule to urine and names four kidney functions.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Glomerulus (the filter)
  • Tubule (takes back what the body needs)
  • Collecting duct
  • Urine
  • Waste removal
  • Fluid and salt balance
  • Acid balance
  • Hormones: red blood cells and bones
  • NOT TO SCALE
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No nephron drawn at organ scale inside the kidney
✗ no transporter names
✗ no laboratory values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Glomerulus (the filter)" present and spelled exactly — confirmed
□ Label "Tubule (takes back what the body needs)" present and spelled exactly — confirmed
□ Label "Collecting duct" present and spelled exactly — confirmed
□ Label "Urine" present and spelled exactly — confirmed
□ Label "Waste removal" present and spelled exactly — confirmed
□ Label "Fluid and salt balance" present and spelled exactly — confirmed
□ Label "Acid balance" present and spelled exactly — confirmed
□ Label "Hormones: red blood cells and bones" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-02-B ★ — What builds up when kidneys fail

**File:** `images/hemodialysis-technician-02-what-builds-up.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part2`

**Job:** P: links each lost function to a finding the technician may see or hear about.

**Alt:** Body outline with four callouts for waste buildup, fluid buildup, potassium buildup, and anemia.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What builds up when kidneys fail · academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Outline of an adult torso, opaque skin, no internal organs visible except in one small inset. Four callouts: wastes build up (nausea, itching, tiredness); fluid builds up (weight gain, swelling, breathlessness); potassium builds up (often no symptoms); fewer red blood cells (tiredness, pallor).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — P: links each lost function to a finding the technician may see or hear about.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Wastes build up
  • Fluid builds up
  • Potassium builds up: often silent
  • Fewer red blood cells
  • Report changes; the clinical team finds the cause
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No anatomy visible through skin
✗ no numbers
✗ no frightening imagery
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Wastes build up" present and spelled exactly — confirmed
□ Label "Fluid builds up" present and spelled exactly — confirmed
□ Label "Potassium builds up: often silent" present and spelled exactly — confirmed
□ Label "Fewer red blood cells" present and spelled exactly — confirmed
□ Label "Report changes; the clinical team finds the cause" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-02-C ○ — Reading a weight trend

**File:** `images/hemodialysis-technician-02-weight-trend.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part4`

**Job:** A: calculates weight change between sessions and reports both source values.

**Alt:** Two scale readings with the calculated difference of 2.2 kilograms and a reminder of what to report.

```text
Reference card · 1672 × 941, 16:9 landscape · Reading a weight trend · academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two scale readings side by side: last post-treatment weight 67.2 kg and today's pre-treatment weight 69.4 kg, difference 2.2 kg, exactly as in the lesson case. A third panel shows the handoff: value, unit, time, baseline.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: calculates weight change between sessions and reports both source values.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Last weight after treatment: 67.2 kg
  • Today's weight before treatment: 69.4 kg
  • Change: 2.2 kg
  • Report: value, unit, time, baseline
  • The fluid goal is a separate decision
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ no fluid-removal setting
✗ no patient name
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Last weight after treatment: 67.2 kg" present and spelled exactly — confirmed
□ Label "Today's weight before treatment: 69.4 kg" present and spelled exactly — confirmed
□ Label "Change: 2.2 kg" present and spelled exactly — confirmed
□ Label "Report: value, unit, time, baseline" present and spelled exactly — confirmed
□ Label "The fluid goal is a separate decision" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 3 — Treatment Options and Living with Kidney Failure

### HD-03-A ★ — Five treatment pathways

**File:** `images/hemodialysis-technician-03-treatment-options-living-with-kidney-failure-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part1`

**Job:** U: compares the five pathways by where treatment happens and who does it.

**Alt:** Five panels comparing in-center hemodialysis, home hemodialysis, peritoneal dialysis, kidney transplant, and conservative kidney management.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Five treatment pathways · academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five equal panels: in-center hemodialysis (external dialyzer, staff-run), home hemodialysis (external dialyzer, at home after training), peritoneal dialysis (fluid in the abdomen, peritoneal membrane is the filter; catheter exits the abdomen pointing downward), kidney transplant (donor kidney placed low in the front of the abdomen, not in the flank), conservative kidney management (active symptom care without dialysis).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: compares the five pathways by where treatment happens and who does it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • In-center hemodialysis
  • Home hemodialysis
  • Peritoneal dialysis
  • Kidney transplant
  • Conservative kidney management
  • The care team and patient choose together
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No transplant kidney drawn in the native flank position
✗ no peritoneal catheter in the bladder
✗ no ranking of options as best or worst
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "In-center hemodialysis" present and spelled exactly — confirmed
□ Label "Home hemodialysis" present and spelled exactly — confirmed
□ Label "Peritoneal dialysis" present and spelled exactly — confirmed
□ Label "Kidney transplant" present and spelled exactly — confirmed
□ Label "Conservative kidney management" present and spelled exactly — confirmed
□ Label "The care team and patient choose together" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-03-B ★ — Teach-back in four steps

**File:** `images/hemodialysis-technician-03-teach-back.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part4`

**Job:** A: uses teach-back to confirm understanding and repeats when needed.

**Alt:** Four-step loop showing a technician and patient using teach-back.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Teach-back in four steps · academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Loop of four steps between a seated patient and a technician at eye level: explain one or two points, ask the patient to say it in their own words, listen for gaps, explain again differently.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: uses teach-back to confirm understanding and repeats when needed.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Explain
  • Ask: tell me in your own words
  • Listen
  • Explain again
  • Repeat until clear
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No standing-over posture
✗ no clipboard hiding the face
✗ no medical jargon in speech bubbles
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Explain" present and spelled exactly — confirmed
□ Label "Ask: tell me in your own words" present and spelled exactly — confirmed
□ Label "Listen" present and spelled exactly — confirmed
□ Label "Explain again" present and spelled exactly — confirmed
□ Label "Repeat until clear" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-03-C ○ — Home dialysis equipment at a glance

**File:** `images/hemodialysis-technician-03-home-equipment.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part2`

**Job:** U: recognizes a home hemodialysis machine, peritoneal dialysis solution bags, and a cycler.

**Alt:** Three panels showing a home hemodialysis machine, a manual peritoneal dialysis exchange set, and a cycler.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Home dialysis equipment at a glance · academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three recognition panels with generic, unbranded equipment in a Filipino home setting: compact home hemodialysis machine; manual exchange set with solution bag hanging above and drain bag below; cycler on a bedside table with bags.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: recognizes a home hemodialysis machine, peritoneal dialysis solution bags, and a cycler.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Home hemodialysis machine
  • Manual exchange: bag above, drain bag below
  • Cycler for overnight exchanges
  • The home program trains the patient
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No brand names
✗ no connection steps
✗ no needles
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Home hemodialysis machine" present and spelled exactly — confirmed
□ Label "Manual exchange: bag above, drain bag below" present and spelled exactly — confirmed
□ Label "Cycler for overnight exchanges" present and spelled exactly — confirmed
□ Label "The home program trains the patient" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 4 — Principles of Hemodialysis

### HD-04-A ★ — Diffusion and ultrafiltration across the membrane

**File:** `images/hemodialysis-technician-04-principles-of-hemodialysis-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `part1`

**Job:** U: distinguishes concentration-driven solute movement from pressure-driven water movement.

**Alt:** Two magnified views of a dialyzer membrane showing diffusion of wastes and pressure-driven removal of water.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Diffusion and ultrafiltration across the membrane · academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two side-by-side magnified views of one hollow-fiber wall. Left, diffusion: many urea dots on the blood side, few on the dialysate side, net arrows from blood to dialysate; blood cells and large proteins stay on the blood side. Right, ultrafiltration: pressure arrow on the blood side, water droplets crossing to the dialysate side. Blood and dialysate flow in opposite directions.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: distinguishes concentration-driven solute movement from pressure-driven water movement.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Blood side
  • Dialysate side
  • Membrane
  • Diffusion: wastes move from crowded to less crowded
  • Ultrafiltration: pressure pushes water out
  • Blood cells and proteins stay
  • Opposite flow directions
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No red blood cells crossing the membrane
✗ no arrows showing urea moving into blood
✗ no flow in the same direction on both sides
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Blood side" present and spelled exactly — confirmed
□ Label "Dialysate side" present and spelled exactly — confirmed
□ Label "Membrane" present and spelled exactly — confirmed
□ Label "Diffusion: wastes move from crowded to less crowded" present and spelled exactly — confirmed
□ Label "Ultrafiltration: pressure pushes water out" present and spelled exactly — confirmed
□ Label "Blood cells and proteins stay" present and spelled exactly — confirmed
□ Label "Opposite flow directions" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-04-B ★ — Tea bag, coffee press, river

**File:** `images/hemodialysis-technician-04-everyday-pictures.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `bigpicture`

**Job:** U: anchors diffusion, ultrafiltration, and convection to everyday pictures.

**Alt:** Three everyday pictures, a tea bag, a coffee press, and a river, each matched to a dialysis transport process.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Tea bag, coffee press, river · academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `bigpicture`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three panels pairing an everyday object with its dialysis meaning: tea bag coloring water (diffusion), coffee press plunger forcing water through a mesh (ultrafiltration), river current carrying sand (convection).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: anchors diffusion, ultrafiltration, and convection to everyday pictures.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Tea bag = diffusion
  • Coffee press = ultrafiltration
  • River carrying sand = convection
  • Concentration does the work
  • Pressure does the work
  • Moving water carries solutes
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No brand names on cups or presses
✗ no steam obscuring labels
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Tea bag = diffusion" present and spelled exactly — confirmed
□ Label "Coffee press = ultrafiltration" present and spelled exactly — confirmed
□ Label "River carrying sand = convection" present and spelled exactly — confirmed
□ Label "Concentration does the work" present and spelled exactly — confirmed
□ Label "Pressure does the work" present and spelled exactly — confirmed
□ Label "Moving water carries solutes" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-04-C ★ — Four fluid numbers that are not the same

**File:** `images/hemodialysis-technician-04-fluid-numbers.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `part3`

**Job:** A: distinguishes weight gain, target weight, pre-to-target difference, and the ordered ultrafiltration goal.

**Alt:** Four tiles separating interdialytic weight gain, target weight, the difference from target, and the ordered fluid goal.

```text
Reference card · 1672 × 941, 16:9 landscape · Four fluid numbers that are not the same · academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four tiles using only the lesson case values: post-weight 64.8 kg, pre-weight 67.1 kg, target 65.4 kg. Weight gain 2.3 kg; pre-to-target difference 1.7 kg; ordered goal shown as a blank box labeled 'confirm with the nurse'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: distinguishes weight gain, target weight, pre-to-target difference, and the ordered ultrafiltration goal.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Weight gain between sessions: 2.3 kg
  • Target weight: 65.4 kg
  • Today minus target: 1.7 kg
  • Ordered fluid goal: confirm with the nurse
  • Different numbers answer different questions
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No number in the ordered-goal box
✗ no ultrafiltration rate value
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Weight gain between sessions: 2.3 kg" present and spelled exactly — confirmed
□ Label "Target weight: 65.4 kg" present and spelled exactly — confirmed
□ Label "Today minus target: 1.7 kg" present and spelled exactly — confirmed
□ Label "Ordered fluid goal: confirm with the nurse" present and spelled exactly — confirmed
□ Label "Different numbers answer different questions" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-04-D ○ — The hemodialysis blood circuit

**File:** `images/hemodialysis-technician-04-blood-circuit.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `part1`

**Job:** U: follows blood from the access through the pump and dialyzer and back.

**Alt:** Hemodialysis blood circuit from the access through the blood pump, dialyzer, and air trap back to the patient, with dialysate flowing the opposite way.

> **Circuit figure.** Do not write a new layout. Generate this prompt with the `dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, flow directions, and pressure points. Emphasis for this figure: Intermittent hemodialysis on an arteriovenous fistula. Use the dialysis-circuit-schematic skill unchanged; modality hemodialysis; show the hollow-fiber cutaway and countercurrent dialysate flow.


## Module 5 — Dialysis Infection Prevention and Waste Management

### HD-05-A ★ — Station turnover sequence

**File:** `images/hemodialysis-technician-05-infection-prevention-waste-management-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part2`

**Job:** A: performs turnover in order and holds the station until contact time is met.

**Alt:** Four-step station turnover: patient leaves, used items removed, surfaces disinfected and kept wet, and release after the full contact time.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Station turnover sequence · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four numbered panels at one unoccupied station: patient has left; used items removed and separated; surfaces cleaned and disinfected, visibly wet; timer running for the label contact time, then release. A used blood pressure cuff is shown going to the used area, not to the next station.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: performs turnover in order and holds the station until contact time is met.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Patient has left
  • 2 Remove and separate used items
  • 3 Clean and disinfect: keep surfaces wet
  • 4 Wait the full label time, then release
  • If it dried early, wet it again
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No contact time in minutes
✗ no patient in the chair
✗ no product brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Patient has left" present and spelled exactly — confirmed
□ Label "2 Remove and separate used items" present and spelled exactly — confirmed
□ Label "3 Clean and disinfect: keep surfaces wet" present and spelled exactly — confirmed
□ Label "4 Wait the full label time, then release" present and spelled exactly — confirmed
□ Label "If it dried early, wet it again" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-05-B ★ — Clean and used never cross

**File:** `images/hemodialysis-technician-05-clean-used-zones.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part2`

**Job:** U: keeps clean supplies and used items on separate paths.

**Alt:** Diagram of a one-way path from clean supplies to the patient station to used items and waste.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Clean and used never cross · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Split scene: left a clean supply cart and clean-hands area; right the used-item bin, sharps container, and waste bags. A bold divider between them; arrows only flow from clean to patient to used, never back.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: keeps clean supplies and used items on separate paths.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Clean supplies
  • Patient station
  • Used items and waste
  • One direction only
  • Nothing used returns to the clean area
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No return arrow from used to clean
✗ no open sharps
✗ no blood splatter
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Clean supplies" present and spelled exactly — confirmed
□ Label "Patient station" present and spelled exactly — confirmed
□ Label "Used items and waste" present and spelled exactly — confirmed
□ Label "One direction only" present and spelled exactly — confirmed
□ Label "Nothing used returns to the clean area" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-05-C ○ — Sorting waste at the point of use

**File:** `images/hemodialysis-technician-05-waste-sorting.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part3`

**Job:** A: places each item in the right container at the moment it becomes waste.

**Alt:** Three waste containers for sharps, infectious waste, and general waste with examples of each.

```text
Reference card · 1672 × 941, 16:9 landscape · Sorting waste at the point of use · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three containers with generic color coding left unspecified in text (colors follow the facility): sharps container (needles), infectious waste (blood-soaked items, used bloodlines and dialyzers), general waste (clean packaging).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: places each item in the right container at the moment it becomes waste.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Sharps container: needles
  • Infectious waste: blood-contaminated items
  • General waste: clean packaging
  • Follow your facility's color code
  • Never recap needles
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No specific bag colors named in labels
✗ no hands near an open sharps opening
✗ no overfilled container
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Sharps container: needles" present and spelled exactly — confirmed
□ Label "Infectious waste: blood-contaminated items" present and spelled exactly — confirmed
□ Label "General waste: clean packaging" present and spelled exactly — confirmed
□ Label "Follow your facility's color code" present and spelled exactly — confirmed
□ Label "Never recap needles" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 6 — Machines, Dialyzers, and the Extracorporeal Circuit

### HD-06-A ★ — Two circuits that meet at the dialyzer

**File:** `images/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `part1`

**Job:** U: traces the blood path and the dialysate path and sees that they meet only at the dialyzer.

**Alt:** Blood path and dialysate path of a hemodialysis machine, meeting only at the dialyzer.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

> **Circuit figure.** Do not write a new layout. Generate this prompt with the `dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, flow directions, and pressure points. Emphasis for this figure: Intermittent hemodialysis. Use the dialysis-circuit-schematic skill unchanged; emphasize the separate dialysate path (fresh dialysate in, used dialysate to drain) in teal.

### HD-06-B ★ — What each safeguard watches and cannot see

**File:** `images/hemodialysis-technician-06-safeguards.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `part2`

**Job:** U: names what each monitor detects and its blind spot.

**Alt:** Dialysis machine front with four safety monitors, each labeled with what it watches and what it cannot detect.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What each safeguard watches and cannot see · academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic unbranded machine front, four callouts each with a 'watches' line and a 'cannot see' line: pressure monitors (cannot reliably see a dislodged needle); air detector and clamp (only at one point on the return line); blood leak detector (only blood in used dialysate); conductivity and temperature (not which concentrate is connected).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: names what each monitor detects and its blind spot.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Pressure monitors
  • Air detector and clamp
  • Blood leak detector
  • Conductivity and temperature
  • Watches
  • Cannot see
  • Your eyes are the last safeguard
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No alarm limit values
✗ no brand or model
✗ no patient connected
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Pressure monitors" present and spelled exactly — confirmed
□ Label "Air detector and clamp" present and spelled exactly — confirmed
□ Label "Blood leak detector" present and spelled exactly — confirmed
□ Label "Conductivity and temperature" present and spelled exactly — confirmed
□ Label "Watches" present and spelled exactly — confirmed
□ Label "Cannot see" present and spelled exactly — confirmed
□ Label "Your eyes are the last safeguard" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-06-C ○ — When a machine fails a check

**File:** `images/hemodialysis-technician-06-failed-check.png` · **Canvas:** 1024 × 1536, 2:3 portrait · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `part4`

**Job:** A: holds, records, reports, and waits for release.

**Alt:** Five-step response when a machine fails a required check.

```text
Process or decision figure · 1024 × 1536, 2:3 portrait · When a machine fails a check · academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps top to bottom: hold and tag the machine; record the machine number and exact message; report to the nurse and biomedical contact; a replacement machine gets its own full checks; only a designated person releases.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1024 × 1536, 2:3 portrait. Steps read top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: holds, records, reports, and waits for release.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Hold and tag
  • Record the exact message
  • Report: nurse and biomedical contact
  • Replacement needs its own checks
  • Release by the designated person only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No restart-and-use shortcut arrow
✗ no specific error code
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Hold and tag" present and spelled exactly — confirmed
□ Label "Record the exact message" present and spelled exactly — confirmed
□ Label "Report: nurse and biomedical contact" present and spelled exactly — confirmed
□ Label "Replacement needs its own checks" present and spelled exactly — confirmed
□ Label "Release by the designated person only" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 7 — Water Treatment, Concentrates, and Dialysate

### HD-07-A ★ — From tap to station

**File:** `images/hemodialysis-technician-07-water-treatment-concentrates-dialysate-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part1`

**Job:** U: traces water through pretreatment, carbon, and reverse osmosis to the loop and names what each stage removes.

**Alt:** Water treatment train from feed water through filter, softener, two carbon tanks, and reverse osmosis to the distribution loop and station.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · From tap to station · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left-to-right train: feed water, sediment filter (particles), softener (hardness), two carbon tanks in series (chlorine and chloramine) with a sample port after each, reverse osmosis (most dissolved salts, bacteria, endotoxin) with reject to drain, distribution loop returning to its start, station. Component order may vary by installation and the caption says so.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: traces water through pretreatment, carbon, and reverse osmosis to the loop and names what each stage removes.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Feed water
  • Sediment filter: particles
  • Softener: hardness
  • Carbon tank 1 (worker)
  • Carbon tank 2 (polisher)
  • Sample port
  • Reverse osmosis
  • Reject to drain
  • Distribution loop
  • Dialysis station
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No single carbon tank
✗ no loop that dead-ends at the last station
✗ no numeric limits
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Feed water" present and spelled exactly — confirmed
□ Label "Sediment filter: particles" present and spelled exactly — confirmed
□ Label "Softener: hardness" present and spelled exactly — confirmed
□ Label "Carbon tank 1 (worker)" present and spelled exactly — confirmed
□ Label "Carbon tank 2 (polisher)" present and spelled exactly — confirmed
□ Label "Sample port" present and spelled exactly — confirmed
□ Label "Reverse osmosis" present and spelled exactly — confirmed
□ Label "Reject to drain" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-07-B ★ — Which test answers which question

**File:** `images/hemodialysis-technician-07-which-test.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part2`

**Job:** U: matches each water check to what it proves.

**Alt:** Five water tests, each paired with the one question it answers.

```text
Reference card · 1672 × 941, 16:9 landscape · Which test answers which question · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Grid of five checks, each with one line 'answers': total chlorine (is the carbon working), hardness (is the softener working), conductivity and rejection (is the membrane separating salts), culture (how many bacteria), endotoxin (bacterial fragments).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: matches each water check to what it proves.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Total chlorine
  • Hardness
  • Conductivity
  • Culture
  • Endotoxin
  • Each test answers one question only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No limit values
✗ no brand test kits
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Total chlorine" present and spelled exactly — confirmed
□ Label "Hardness" present and spelled exactly — confirmed
□ Label "Conductivity" present and spelled exactly — confirmed
□ Label "Culture" present and spelled exactly — confirmed
□ Label "Endotoxin" present and spelled exactly — confirmed
□ Label "Each test answers one question only" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-07-C ○ — How the machine makes dialysate

**File:** `images/hemodialysis-technician-07-making-dialysate.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part3`

**Job:** U: sees that treated water plus two concentrates become dialysate, checked by conductivity.

**Alt:** Treated water and two concentrates mixing inside the machine, with a conductivity check before the dialyzer.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · How the machine makes dialysate · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three streams entering a mixing point inside a generic machine: treated water (large), acid concentrate (small), bicarbonate concentrate (small). After mixing, a conductivity and temperature check, then to the dialyzer or to bypass.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees that treated water plus two concentrates become dialysate, checked by conductivity.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Treated water
  • Acid concentrate
  • Bicarbonate concentrate
  • Mixing
  • Conductivity and temperature check
  • To dialyzer
  • Bypass to drain if wrong
  • Read the label as well as the display
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No mixing ratio numbers
✗ no potassium or calcium values
✗ no brand jugs
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Treated water" present and spelled exactly — confirmed
□ Label "Acid concentrate" present and spelled exactly — confirmed
□ Label "Bicarbonate concentrate" present and spelled exactly — confirmed
□ Label "Mixing" present and spelled exactly — confirmed
□ Label "Conductivity and temperature check" present and spelled exactly — confirmed
□ Label "To dialyzer" present and spelled exactly — confirmed
□ Label "Bypass to drain if wrong" present and spelled exactly — confirmed
□ Label "Read the label as well as the display" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 8 — Vascular Access Recognition and Protection

### HD-08-A ★ — Three types of hemodialysis access

**File:** `images/hemodialysis-technician-08-vascular-access-recognition-protection-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part1`

**Job:** U: distinguishes a fistula, a graft, and a central venous catheter.

**Alt:** Three panels showing an arteriovenous fistula, an arteriovenous graft, and a central venous dialysis catheter.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Three types of hemodialysis access · academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three panels. Fistula: the patient's own vein joined directly to an artery at a side junction, no synthetic material. Graft: a synthetic tube with one end on an artery and the other on a vein. Catheter: one catheter body with two channels lying in a large central vein, with an external segment. Arteries drawn with thick muscular walls and round lumens; veins thin-walled and larger.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: distinguishes a fistula, a graft, and a central venous catheter.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • AV fistula (direct join)
  • Artery
  • Vein
  • Anastomosis (the join)
  • AV graft (tube between vessels)
  • Synthetic graft
  • Central venous catheter (tube in a large vein)
  • Two channels, one catheter
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No graft in the fistula panel
✗ no graft joined to two veins or two arteries
✗ no catheter in an artery
✗ no needles or cannulation steps
✗ no maturation numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "AV fistula (direct join)" present and spelled exactly — confirmed
□ Label "Artery" present and spelled exactly — confirmed
□ Label "Vein" present and spelled exactly — confirmed
□ Label "Anastomosis (the join)" present and spelled exactly — confirmed
□ Label "AV graft (tube between vessels)" present and spelled exactly — confirmed
□ Label "Synthetic graft" present and spelled exactly — confirmed
□ Label "Central venous catheter (tube in a large vein)" present and spelled exactly — confirmed
□ Label "Two channels, one catheter" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-08-B ★ — Look, listen, feel

**File:** `images/hemodialysis-technician-08-look-listen-feel.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part3`

**Job:** A: recognizes a change from the patient's usual findings and reports it.

**Alt:** Three panels showing looking at, listening to, and feeling a fistula, with a reminder to report any change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Look, listen, feel · academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three panels on a bare forearm with a fistula, opaque skin: look (redness, swelling, drainage), listen (stethoscope, continuous whoosh), feel (two fingers, continuous buzz). A fourth strip: 'Changed or absent: tell the nurse now, do not use the access'. Only authorized staff perform the checks.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: recognizes a change from the patient's usual findings and reports it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Look
  • Listen: the whoosh (bruit)
  • Feel: the buzz (thrill)
  • Changed or absent: tell the nurse now
  • Do not use the access
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No needles
✗ no vessels visible through skin
✗ no blood pressure cuff on the access arm
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Look" present and spelled exactly — confirmed
□ Label "Listen: the whoosh (bruit)" present and spelled exactly — confirmed
□ Label "Feel: the buzz (thrill)" present and spelled exactly — confirmed
□ Label "Changed or absent: tell the nurse now" present and spelled exactly — confirmed
□ Label "Do not use the access" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-08-C ○ — Protecting the access arm

**File:** `images/hemodialysis-technician-08-protect-access.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part2`

**Job:** P: applies everyday protections for the access arm.

**Alt:** Four reminders for protecting a dialysis access arm and catheter dressing.

```text
Reference card · 1672 × 941, 16:9 landscape · Protecting the access arm · academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four icon tiles around an arm with an access: no blood pressure cuff, no needle sticks or blood draws, no tight clothing or bags on the arm, keep a catheter dressing clean and dry.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — P: applies everyday protections for the access arm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • No blood pressure on this arm
  • No needle sticks on this arm
  • Nothing tight on this arm
  • Catheter dressing: clean and dry
  • Report damage or a loose dressing
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No red X over the patient's face
✗ no blood
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "No blood pressure on this arm" present and spelled exactly — confirmed
□ Label "No needle sticks on this arm" present and spelled exactly — confirmed
□ Label "Nothing tight on this arm" present and spelled exactly — confirmed
□ Label "Catheter dressing: clean and dry" present and spelled exactly — confirmed
□ Label "Report damage or a loose dressing" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 9 — The Hemodialysis Session

### HD-09-A ★ — One session, three phases

**File:** `images/hemodialysis-technician-09-the-hemodialysis-session-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part1`

**Job:** U: sees the technician's and the nurse's tasks across pre-treatment, treatment, and post-treatment.

**Alt:** Swimlane chart of technician and nurse tasks before, during, and after a hemodialysis session.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · One session, three phases · academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two swimlanes (Technician, Nurse) across three phases. Technician: verify identity and readiness, measure and report; observe and record; measure, hand off, turn over. Nurse: assess and authorize; evaluate and direct; evaluate completion and stability.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: sees the technician's and the nurse's tasks across pre-treatment, treatment, and post-treatment.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Before treatment
  • During treatment
  • After treatment
  • Technician
  • Nurse
  • Verify, measure, report
  • Observe and record
  • Hand off and turn over
  • Assess and authorize
  • Evaluate and direct
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No machine settings
✗ no arrows showing the technician changing the prescription
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Before treatment" present and spelled exactly — confirmed
□ Label "During treatment" present and spelled exactly — confirmed
□ Label "After treatment" present and spelled exactly — confirmed
□ Label "Technician" present and spelled exactly — confirmed
□ Label "Nurse" present and spelled exactly — confirmed
□ Label "Verify, measure, report" present and spelled exactly — confirmed
□ Label "Observe and record" present and spelled exactly — confirmed
□ Label "Hand off and turn over" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-09-B ★ — What to look at on every round

**File:** `images/hemodialysis-technician-09-every-round.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part3`

**Job:** A: checks patient, access, lines, machine, and record on each round.

**Alt:** Patient in a dialysis chair with five numbered things to check on each round.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What to look at on every round · academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene of a patient in a dialysis chair with the access arm uncovered and visible, five numbered callouts: the patient, the access, the lines, the machine, the record. Screen values indistinct.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: checks patient, access, lines, machine, and record on each round.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 The patient
  • 2 The access: visible and dry
  • 3 The lines: no kinks
  • 4 The machine
  • 5 The record: real numbers, at the time
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No blanket covering the access
✗ no readable numbers on the screen
✗ no needle close-up
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 The patient" present and spelled exactly — confirmed
□ Label "2 The access: visible and dry" present and spelled exactly — confirmed
□ Label "3 The lines: no kinks" present and spelled exactly — confirmed
□ Label "4 The machine" present and spelled exactly — confirmed
□ Label "5 The record: real numbers, at the time" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-09-C ○ — Checking an unexpected weight

**File:** `images/hemodialysis-technician-09-unexpected-weight.png` · **Canvas:** 1024 × 1536, 2:3 portrait · **Placement:** academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part2`

**Job:** A: verifies an unexpected measurement before reporting it.

**Alt:** Six-step check for an unexpected pre-treatment weight.

```text
Process or decision figure · 1024 × 1536, 2:3 portrait · Checking an unexpected weight · academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Decision strip: same patient? same scale and units? shoes, bag, wheelchair? repeat as directed; report both readings; hold setup until the nurse confirms.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1024 × 1536, 2:3 portrait. Steps read top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: verifies an unexpected measurement before reporting it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Right patient?
  • Right units and scale?
  • Anything extra on the scale?
  • Repeat as directed
  • Report both readings
  • Hold setup until confirmed
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No weight values
✗ no instruction to adjust the fluid goal
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Right patient?" present and spelled exactly — confirmed
□ Label "Right units and scale?" present and spelled exactly — confirmed
□ Label "Anything extra on the scale?" present and spelled exactly — confirmed
□ Label "Repeat as directed" present and spelled exactly — confirmed
□ Label "Report both readings" present and spelled exactly — confirmed
□ Label "Hold setup until confirmed" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 10 — Complications and Emergency Response

### HD-10-A ★ — Your first thirty seconds

**File:** `images/hemodialysis-technician-10-complications-emergency-response-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-10-complications-emergency-response.html, section `part2`

**Job:** A: summons help, reports, takes an assigned task, and closes the loop.

**Alt:** Four-step emergency role card for a dialysis technician.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Your first thirty seconds · academy/hemodialysis-technician-10-complications-emergency-response.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Role card in four steps: call for help now; say where you are and what you saw; take the task you are given; repeat it back and report when done. Team lead directs treatment and circuit decisions.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: summons help, reports, takes an assigned task, and closes the loop.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Call for help now
  • Say where and what you saw
  • Take your assigned task
  • Repeat back, report when done
  • The team lead decides treatment
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No chest compressions depicted
✗ no drug names
✗ no defibrillator pads on a patient
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Call for help now" present and spelled exactly — confirmed
□ Label "Say where and what you saw" present and spelled exactly — confirmed
□ Label "Take your assigned task" present and spelled exactly — confirmed
□ Label "Repeat back, report when done" present and spelled exactly — confirmed
□ Label "The team lead decides treatment" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-10-B ★ — Signs that need help immediately

**File:** `images/hemodialysis-technician-10-red-flags.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-10-complications-emergency-response.html, section `part1`

**Job:** A: recognizes findings that require immediate escalation.

**Alt:** Six warning signs during dialysis that need immediate help.

```text
Reference card · 1672 × 941, 16:9 landscape · Signs that need help immediately · academy/hemodialysis-technician-10-complications-emergency-response.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Grid of six red-bordered tiles with simple icons: chest pain or breathlessness; collapse or cannot be woken; heavy bleeding or a needle out; sudden wheeze, swelling, or hives; fever with chills; several patients unwell at once.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: recognizes findings that require immediate escalation.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Chest pain or breathlessness
  • Collapse
  • Bleeding or a needle out
  • Wheeze, swelling, hives
  • Fever and chills
  • Several patients unwell at once
  • Call first, measure after
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No graphic blood
✗ no distressed faces in close-up
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Chest pain or breathlessness" present and spelled exactly — confirmed
□ Label "Collapse" present and spelled exactly — confirmed
□ Label "Bleeding or a needle out" present and spelled exactly — confirmed
□ Label "Wheeze, swelling, hives" present and spelled exactly — confirmed
□ Label "Fever and chills" present and spelled exactly — confirmed
□ Label "Several patients unwell at once" present and spelled exactly — confirmed
□ Label "Call first, measure after" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-10-C ○ — When water or power fails

**File:** `images/hemodialysis-technician-10-utility-failure.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-10-complications-emergency-response.html, section `part4`

**Job:** A: holds new starts, reports connected-patient status, and waits for authorized release.

**Alt:** Flow for water or power failure: hold new starts, report, follow the incident lead, and wait for clearance.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · When water or power fails · academy/hemodialysis-technician-10-complications-emergency-response.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two columns (water problem, power problem) converging on the same four steps: hold new starts; report which stations and who is connected; follow the incident lead; return to service only when cleared.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: holds new starts, reports connected-patient status, and waits for authorized release.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Water problem
  • Power problem
  • Hold new starts
  • Report who is connected
  • Follow the incident lead
  • Cleared by the designated leads
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No instruction to disconnect patients
✗ no generator specifications
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Water problem" present and spelled exactly — confirmed
□ Label "Power problem" present and spelled exactly — confirmed
□ Label "Hold new starts" present and spelled exactly — confirmed
□ Label "Report who is connected" present and spelled exactly — confirmed
□ Label "Follow the incident lead" present and spelled exactly — confirmed
□ Label "Cleared by the designated leads" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 11 — Dialyzer Reprocessing and Equipment Quality

### HD-11-A ★ — Traceability: release or hold

**File:** `images/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part2`

**Job:** A: releases a reprocessed dialyzer only when identity, records, and checks all pass.

**Alt:** Decision diagram with three checks leading to release or to hold and report.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Traceability: release or hold · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Decision diagram with three gates in sequence: identity matches the same patient; processing and storage records complete; pre-use checks passed including residual disinfectant test. All yes leads to release by the designated person; any no leads to hold, segregate, and report.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: releases a reprocessed dialyzer only when identity, records, and checks all pass.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Same patient?
  • Records complete?
  • Pre-use checks passed?
  • Release by the designated person
  • Hold, separate, report
  • A passed test never fixes a failed identity check
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No patient names on the label
✗ no numeric acceptance limits
✗ no use count
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Same patient?" present and spelled exactly — confirmed
□ Label "Records complete?" present and spelled exactly — confirmed
□ Label "Pre-use checks passed?" present and spelled exactly — confirmed
□ Label "Release by the designated person" present and spelled exactly — confirmed
□ Label "Hold, separate, report" present and spelled exactly — confirmed
□ Label "A passed test never fixes a failed identity check" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-B ★ — What a dialyzer label must tell you

**File:** `images/hemodialysis-technician-11-dialyzer-label.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part2`

**Job:** U: reads the fields that make a dialyzer traceable.

**Alt:** Reprocessed dialyzer with a label showing the fields needed for traceability.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What a dialyzer label must tell you · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part2`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Close-up of a generic reprocessed dialyzer with a mock label whose fields are blank lines with field names only: patient identifiers, dialyzer identifier, number of uses, date processed, tests passed, processed by.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: reads the fields that make a dialyzer traceable.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Patient identifiers
  • Dialyzer identifier
  • Number of uses
  • Date processed
  • Tests passed
  • Processed by
  • Unreadable label = hold
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No filled-in names, dates, or numbers
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Patient identifiers" present and spelled exactly — confirmed
□ Label "Dialyzer identifier" present and spelled exactly — confirmed
□ Label "Number of uses" present and spelled exactly — confirmed
□ Label "Date processed" present and spelled exactly — confirmed
□ Label "Tests passed" present and spelled exactly — confirmed
□ Label "Processed by" present and spelled exactly — confirmed
□ Label "Unreadable label = hold" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-C ○ — From fault to return to service

**File:** `images/hemodialysis-technician-11-return-to-service.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part4`

**Job:** A: distinguishes repair completion from authorized release.

**Alt:** Five steps from an equipment fault to documented return to service.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · From fault to return to service · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps: fault noticed and recorded; hold and tag; repair by authorized staff; post-service checks documented; release signed by the designated person. A normal screen is shown crossed out as 'not a release'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: distinguishes repair completion from authorized release.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Fault recorded
  • Hold and tag
  • Repair
  • Post-service checks
  • Signed release
  • A normal screen is not a release
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No work order numbers
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Fault recorded" present and spelled exactly — confirmed
□ Label "Hold and tag" present and spelled exactly — confirmed
□ Label "Repair" present and spelled exactly — confirmed
□ Label "Post-service checks" present and spelled exactly — confirmed
□ Label "Signed release" present and spelled exactly — confirmed
□ Label "A normal screen is not a release" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 12 — Integrated Practice and Competency Assessment

### HD-12-A ★ — Five practical stations

**File:** `images/hemodialysis-technician-12-integrated-practice-competency-assessment-teaching-diagram.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `part4`

**Job:** U: sees the five capstone stations and what each assesses.

**Alt:** Map of the five capstone assessment stations.

**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Five practical stations · academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Map of five stations in a simulation room, each with an icon: station turnover; equipment readiness; water quality; patient and access handoff; emergency response. An assessor with a checklist stands at one. Mannequin only, no real patients.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees the five capstone stations and what each assesses.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Station turnover
  • 2 Equipment readiness
  • 3 Water quality
  • 4 Patient and access handoff
  • 5 Emergency response
  • Critical steps must all be satisfactory
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No scores or pass marks
✗ no real patients
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Station turnover" present and spelled exactly — confirmed
□ Label "2 Equipment readiness" present and spelled exactly — confirmed
□ Label "3 Water quality" present and spelled exactly — confirmed
□ Label "4 Patient and access handoff" present and spelled exactly — confirmed
□ Label "5 Emergency response" present and spelled exactly — confirmed
□ Label "Critical steps must all be satisfactory" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-12-B ★ — Verify, pause, report, confirm, record, release

**File:** `images/hemodialysis-technician-12-six-habits.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `bigpicture`

**Job:** U: recalls the pattern behind every module.

**Alt:** Six-step loop: verify, pause, report, confirm, record, release.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Verify, pause, report, confirm, record, release · academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `bigpicture`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six-step loop with simple icons. Release is visually distinct and assigned to 'the designated person'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: recalls the pattern behind every module.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Verify
  • Pause
  • Report
  • Confirm
  • Record
  • Release: designated person only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No extra steps
✗ no numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Verify" present and spelled exactly — confirmed
□ Label "Pause" present and spelled exactly — confirmed
□ Label "Report" present and spelled exactly — confirmed
□ Label "Confirm" present and spelled exactly — confirmed
□ Label "Record" present and spelled exactly — confirmed
□ Label "Release: designated person only" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-12-C ○ — Observed, supervised, signed off

**File:** `images/hemodialysis-technician-12-three-levels.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `part4`

**Job:** U: distinguishes observation, supervised practice, and sign-off.

**Alt:** Three steps of learning a skill: observed, supervised practice, and signed off.

```text
Reference card · 1672 × 941, 16:9 landscape · Observed, supervised, signed off · academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `part4`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three ascending steps with a learner figure: watching a preceptor; performing while the preceptor watches; preceptor signing a form.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: distinguishes observation, supervised practice, and sign-off.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Observed: you watched
  • Supervised practice: you did it, watched
  • Signed off: recorded as competent
  • Only then is it your assigned task
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No certificate imagery
✗ no government seal
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Observed: you watched" present and spelled exactly — confirmed
□ Label "Supervised practice: you did it, watched" present and spelled exactly — confirmed
□ Label "Signed off: recorded as competent" present and spelled exactly — confirmed
□ Label "Only then is it your assigned task" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


# Water Treatment System Technician

## WATER-H0 — Hub hero

**File:** `images/water-treatment-technician-vignette-hero.png` · **Alt:** A water treatment technician records a gauge reading in a dialysis water room.

```text
Circular vignette hero · 2048 × 2048, 1:1 · hub page academy/water-treatment-technician.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A Filipino water treatment technician in a clean dialysis water room reading a pressure gauge on a reverse osmosis unit and writing on a clipboard log; carbon tanks and blue pipework behind.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A water treatment technician records a gauge reading in a dialysis water room." — confirmed
```


## Module 1 — Why Dialysis Water Is Different

### WATER-01-H — Module hero

**File:** `images/water-treatment-technician-01-why-dialysis-water-is-different-vignette-hero.png` · **Alt:** A technician holding a glass of clear tap water beside a dialyzer on a bench, looking from one to the other.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-01-why-dialysis-water-is-different.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician holding a glass of clear tap water beside a dialyzer on a bench, looking from one to the other.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician holding a glass of clear tap water beside a dialyzer on a bench, looking from one to the other." — confirmed
```

### WATER-01-A ★ — A glass of water and a week of dialysis

**File:** `images/water-treatment-technician-01-exposure-volume.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `exposure`

**Job:** U: grasps why the same water is safe to drink and unsafe to dialyze with.

**Alt:** Comparison of drinking about 14 liters of water a week with dialysis exposure of more than 300 liters across a thin membrane.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · A glass of water and a week of dialysis · academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `exposure`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left: a person drinking; gut wall shown as a thick protective barrier in a small inset; label about 14 liters a week. Right: dialyzer fiber with a thin membrane between dialysate and blood; label more than 300 liters a week. Volumes are those stated in the lesson.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: grasps why the same water is safe to drink and unsafe to dialyze with.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Drinking: about 14 liters a week
  • The gut is a thick barrier
  • Dialysis: more than 300 liters a week
  • Only a thin membrane
  • Small chemicals cross directly into blood
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other volumes
✗ no anatomy visible through skin outside the inset
✗ no brand bottles
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Drinking: about 14 liters a week" present and spelled exactly — confirmed
□ Label "The gut is a thick barrier" present and spelled exactly — confirmed
□ Label "Dialysis: more than 300 liters a week" present and spelled exactly — confirmed
□ Label "Only a thin membrane" present and spelled exactly — confirmed
□ Label "Small chemicals cross directly into blood" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-01-B ★ — Three groups of contaminants

**File:** `images/water-treatment-technician-01-contaminant-groups.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `contaminants`

**Job:** U: sorts contaminants into added chemicals, ground and pipe chemicals, and living contaminants with the main barrier for each.

**Alt:** Three columns of dialysis water contaminants with the main barrier against each.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Three groups of contaminants · academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `contaminants`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three columns. Added on purpose: chlorine, chloramine, fluoride; barrier carbon tanks (for chlorine and chloramine). From ground and pipes: calcium, magnesium, aluminum, nitrate, metals; barrier softener and reverse osmosis. Living: bacteria and endotoxin; barrier reverse osmosis, ultrafilters, disinfection.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sorts contaminants into added chemicals, ground and pipe chemicals, and living contaminants with the main barrier for each.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Added on purpose
  • From the ground and pipes
  • Living contaminants
  • Chlorine and chloramine
  • Calcium and magnesium
  • Aluminum and metals
  • Bacteria and endotoxin
  • Main barrier
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numeric limits
✗ no skull-and-crossbones
✗ no claim that reverse osmosis removes chlorine
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Added on purpose" present and spelled exactly — confirmed
□ Label "From the ground and pipes" present and spelled exactly — confirmed
□ Label "Living contaminants" present and spelled exactly — confirmed
□ Label "Chlorine and chloramine" present and spelled exactly — confirmed
□ Label "Calcium and magnesium" present and spelled exactly — confirmed
□ Label "Aluminum and metals" present and spelled exactly — confirmed
□ Label "Bacteria and endotoxin" present and spelled exactly — confirmed
□ Label "Main barrier" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-01-C ○ — Three levels of purity

**File:** `images/water-treatment-technician-01-purity-levels.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `tiers`

**Job:** U: orders dialysis water, standard dialysis fluid, and ultrapure dialysis fluid.

**Alt:** Three steps of fluid purity with bacteria and endotoxin limits.

```text
Reference card · 1672 × 941, 16:9 landscape · Three levels of purity · academy/water-treatment-technician-01-why-dialysis-water-is-different.html, section `tiers`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three ascending steps. Limits exactly as in the lesson table: dialysis water <100 CFU/mL and <0.25 EU/mL; standard dialysis fluid <100 CFU/mL and <0.5 EU/mL; ultrapure <0.1 CFU/mL and <0.03 EU/mL.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: orders dialysis water, standard dialysis fluid, and ultrapure dialysis fluid.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Dialysis water
  • Standard dialysis fluid
  • Ultrapure dialysis fluid
  • Bacteria
  • Endotoxin
  • <100 CFU/mL
  • <0.25 EU/mL
  • <0.5 EU/mL
  • <0.1 CFU/mL
  • <0.03 EU/mL
  • Check your facility's written limits
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ no swapped units
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Dialysis water" present and spelled exactly — confirmed
□ Label "Standard dialysis fluid" present and spelled exactly — confirmed
□ Label "Ultrapure dialysis fluid" present and spelled exactly — confirmed
□ Label "Bacteria" present and spelled exactly — confirmed
□ Label "Endotoxin" present and spelled exactly — confirmed
□ Label "<100 CFU/mL" present and spelled exactly — confirmed
□ Label "<0.25 EU/mL" present and spelled exactly — confirmed
□ Label "<0.5 EU/mL" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 2 — Source Water and System Design

### WATER-02-H — Module hero

**File:** `images/water-treatment-technician-02-source-water-system-design-vignette-hero.png` · **Alt:** A technician and an engineer looking at a system drawing spread on a table in a water room.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-02-source-water-system-design.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician and an engineer looking at a system drawing spread on a table in a water room.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician and an engineer looking at a system drawing spread on a table in a water room." — confirmed
```

### WATER-02-A ★ — Three sources, three problems

**File:** `images/water-treatment-technician-02-source-comparison.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-02-source-water-system-design.html, section `sources`

**Job:** U: predicts the main contaminant load from each source.

**Alt:** Three water sources and the main problem each brings.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Three sources, three problems · academy/water-treatment-technician-02-source-water-system-design.html, section `sources`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three columns: city water (disinfectant, changes after pipe work), deep well (hardness, iron, minerals, no disinfectant), tanker delivery (varies load to load, unknown history).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: predicts the main contaminant load from each source.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • City water
  • Deep well
  • Tanker delivery
  • Disinfectant varies
  • Hard, mineral-rich
  • Varies every load
  • Test a new source before use
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No utility company names
✗ no numeric values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "City water" present and spelled exactly — confirmed
□ Label "Deep well" present and spelled exactly — confirmed
□ Label "Tanker delivery" present and spelled exactly — confirmed
□ Label "Disinfectant varies" present and spelled exactly — confirmed
□ Label "Hard, mineral-rich" present and spelled exactly — confirmed
□ Label "Varies every load" present and spelled exactly — confirmed
□ Label "Test a new source before use" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-02-B ★ — Reading the system drawing

**File:** `images/water-treatment-technician-02-system-drawing.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-02-source-water-system-design.html, section `drawing`

**Job:** A: follows a simplified piping drawing and finds valves, gauges, and sample ports.

**Alt:** Simplified piping drawing of a dialysis water system with a symbol legend.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Reading the system drawing · academy/water-treatment-technician-02-source-water-system-design.html, section `drawing`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Clean engineering-style drawing of a generic single-pass system with standard symbols and a legend: valve, gauge, sample port, pump, flow direction arrows. Flow left to right, loop returning.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: follows a simplified piping drawing and finds valves, gauges, and sample ports.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Legend
  • Valve
  • Pressure gauge
  • Sample port
  • Pump
  • Flow direction
  • Loop return
  • Drain
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No manufacturer title block
✗ no dimensions
✗ no dead-end branches
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Legend" present and spelled exactly — confirmed
□ Label "Valve" present and spelled exactly — confirmed
□ Label "Pressure gauge" present and spelled exactly — confirmed
□ Label "Sample port" present and spelled exactly — confirmed
□ Label "Pump" present and spelled exactly — confirmed
□ Label "Flow direction" present and spelled exactly — confirmed
□ Label "Loop return" present and spelled exactly — confirmed
□ Label "Drain" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-02-C ○ — Sizing for the busiest, coldest hour

**File:** `images/water-treatment-technician-02-sizing.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-02-source-water-system-design.html, section `sizing`

**Job:** U: sees that capacity is set by peak demand and the coldest feed water.

**Alt:** Four steps for sizing a water system for peak demand and cold feed water.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Sizing for the busiest, coldest hour · academy/water-treatment-technician-02-source-water-system-design.html, section `sizing`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four steps: count stations and other users of water; find peak demand; add a design margin; check output at the coldest expected feed water temperature. A thermometer icon shows output falling as water cools.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: sees that capacity is set by peak demand and the coldest feed water.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Count every water user
  • Find peak demand
  • Add a margin
  • Check at the coldest water
  • Cold water lowers output
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No liters-per-minute values
✗ no percent figures
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Count every water user" present and spelled exactly — confirmed
□ Label "Find peak demand" present and spelled exactly — confirmed
□ Label "Add a margin" present and spelled exactly — confirmed
□ Label "Check at the coldest water" present and spelled exactly — confirmed
□ Label "Cold water lowers output" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 3 — Sediment Filtration and Softening

### WATER-03-H — Module hero

**File:** `images/water-treatment-technician-03-sediment-filtration-softening-vignette-hero.png` · **Alt:** A technician checking the salt level in a softener brine tank.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-03-sediment-filtration-softening.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician checking the salt level in a softener brine tank.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician checking the salt level in a softener brine tank." — confirmed
```

### WATER-03-A ★ — Reading the pressure drop

**File:** `images/water-treatment-technician-03-pressure-drop.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-03-sediment-filtration-softening.html, section `filters`

**Job:** A: calculates pressure drop across a filter and recognizes loading.

**Alt:** Cutaway filter with gauges before and after showing an 8 psi pressure drop.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Reading the pressure drop · academy/water-treatment-technician-03-sediment-filtration-softening.html, section `filters`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Cutaway of a sediment filter with layered media, a gauge before and a gauge after. Example exactly as the lesson: 60 psi before, 52 psi after, drop 8 psi.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: calculates pressure drop across a filter and recognizes loading.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Pressure before: 60 psi
  • Pressure after: 52 psi
  • Pressure drop: 8 psi
  • Rising drop = filter loading
  • Record both gauges daily
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other values
✗ no gauges reading equal
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Pressure before: 60 psi" present and spelled exactly — confirmed
□ Label "Pressure after: 52 psi" present and spelled exactly — confirmed
□ Label "Pressure drop: 8 psi" present and spelled exactly — confirmed
□ Label "Rising drop = filter loading" present and spelled exactly — confirmed
□ Label "Record both gauges daily" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-03-B ★ — The softener cycle

**File:** `images/water-treatment-technician-03-softener-cycle.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-03-sediment-filtration-softening.html, section `softener`

**Job:** U: follows service, backwash, brine draw, rinse, and return to service.

**Alt:** Five stages of the softener cycle with resin tank and brine tank.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The softener cycle · academy/water-treatment-technician-03-sediment-filtration-softening.html, section `softener`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five-stage cycle around a softener tank cutaway showing resin beads; brine tank beside it. Service: hard water in, soft water out. Regeneration stages send flow to drain.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: follows service, backwash, brine draw, rinse, and return to service.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Service
  • Backwash
  • Brine draw
  • Rinse
  • Back in service
  • Resin beads
  • Brine tank
  • To drain
  • Never during treatment hours
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No brine flowing to the reverse osmosis unit
✗ no clock times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Service" present and spelled exactly — confirmed
□ Label "Backwash" present and spelled exactly — confirmed
□ Label "Brine draw" present and spelled exactly — confirmed
□ Label "Rinse" present and spelled exactly — confirmed
□ Label "Back in service" present and spelled exactly — confirmed
□ Label "Resin beads" present and spelled exactly — confirmed
□ Label "Brine tank" present and spelled exactly — confirmed
□ Label "To drain" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-03-C ○ — Inside the brine tank

**File:** `images/water-treatment-technician-03-brine-tank.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-03-sediment-filtration-softening.html, section `softener`

**Job:** A: checks salt level and recognizes a salt bridge.

**Alt:** Two brine tank cutaways comparing normal salt with a salt bridge.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Inside the brine tank · academy/water-treatment-technician-03-sediment-filtration-softening.html, section `softener`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two brine tank cutaways: normal (salt resting in water) and salt bridge (hard crust with an empty gap beneath).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: checks salt level and recognizes a salt bridge.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Normal: salt in water
  • Salt bridge: crust with a gap below
  • Break the bridge by the unit's method
  • Check the clock every morning
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No tools shown puncturing the tank
✗ no numeric salt levels
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Normal: salt in water" present and spelled exactly — confirmed
□ Label "Salt bridge: crust with a gap below" present and spelled exactly — confirmed
□ Label "Break the bridge by the unit's method" present and spelled exactly — confirmed
□ Label "Check the clock every morning" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 4 — Carbon Tanks and Chlorine Control

### WATER-04-H — Module hero

**File:** `images/water-treatment-technician-04-carbon-tanks-chlorine-control-vignette-hero.png` · **Alt:** Close view of a technician's gloved hands holding a chlorine test vial up to a color comparator beside a sample port.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: Close view of a technician's gloved hands holding a chlorine test vial up to a color comparator beside a sample port.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "Close view of a technician's gloved hands holding a chlorine test vial up to a color comparator beside a sample port." — confirmed
```

### WATER-04-A ★ — Worker and polisher

**File:** `images/water-treatment-technician-04-worker-polisher.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `carbon`

**Job:** U: understands two tanks in series and where each sample port is.

**Alt:** Two carbon tanks in series with a sample port after each.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Worker and polisher · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `carbon`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two carbon tank cutaways in series, flow left to right. Sample port after tank 1 and after tank 2. Chlorine dots dense entering tank 1, sparse after it, none after tank 2.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands two tanks in series and where each sample port is.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Carbon tank 1: the worker
  • Carbon tank 2: the polisher
  • Sample port 1
  • Sample port 2
  • Chlorine and chloramine in
  • Chlorine-free water out
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No single-tank layout
✗ no parallel arrangement
✗ no numeric limits
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Carbon tank 1: the worker" present and spelled exactly — confirmed
□ Label "Carbon tank 2: the polisher" present and spelled exactly — confirmed
□ Label "Sample port 1" present and spelled exactly — confirmed
□ Label "Sample port 2" present and spelled exactly — confirmed
□ Label "Chlorine and chloramine in" present and spelled exactly — confirmed
□ Label "Chlorine-free water out" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-04-B ★ — Empty-bed contact time

**File:** `images/water-treatment-technician-04-ebct.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `carbon`

**Job:** A: calculates contact time from bed volume and flow.

**Alt:** Formula and worked example for empty-bed contact time.

```text
Reference card · 1672 × 941, 16:9 landscape · Empty-bed contact time · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `carbon`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Formula card with the lesson example: 300 liters of carbon, 30 liters per minute, 10 minutes. Tank cutaway with a stopwatch icon.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: calculates contact time from bed volume and flow.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Contact time = bed volume ÷ flow
  • 300 liters ÷ 30 liters per minute = 10 minutes
  • Slower flow or more carbon = more contact time
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Contact time = bed volume ÷ flow" present and spelled exactly — confirmed
□ Label "300 liters ÷ 30 liters per minute = 10 minutes" present and spelled exactly — confirmed
□ Label "Slower flow or more carbon = more contact time" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-04-C ★ — Acting on the chlorine result

**File:** `images/water-treatment-technician-04-chlorine-decision.png` · **Canvas:** 1024 × 1536, 2:3 portrait · **Placement:** academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `chlorine-test`

**Job:** A: takes the correct action for each total chlorine result.

**Alt:** Decision tree for total chlorine results after each carbon tank.

```text
Process or decision figure · 1024 × 1536, 2:3 portrait · Acting on the chlorine result · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `chlorine-test`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Decision tree: test after tank 1. At or below limit: record and release. Above limit: test after tank 2 now. After tank 2 at or below limit: report, plan replacement, test more often. After tank 2 above limit: STOP, no treatments, tell nurse and medical director.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1024 × 1536, 2:3 portrait. Steps read top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: takes the correct action for each total chlorine result.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Test after tank 1
  • At or below the limit: record and release
  • Above the limit: test after tank 2 now
  • Tank 2 within limit: report, replace the worker, test more often
  • Tank 2 above limit: STOP and report
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numeric limit printed
✗ no path that continues treatment after a tank 2 failure
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Test after tank 1" present and spelled exactly — confirmed
□ Label "At or below the limit: record and release" present and spelled exactly — confirmed
□ Label "Above the limit: test after tank 2 now" present and spelled exactly — confirmed
□ Label "Tank 2 within limit: report, replace the worker, test more often" present and spelled exactly — confirmed
□ Label "Tank 2 above limit: STOP and report" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 5 — Reverse Osmosis

### WATER-05-H — Module hero

**File:** `images/water-treatment-technician-05-reverse-osmosis-vignette-hero.png` · **Alt:** A technician reading flow meters on the front of a reverse osmosis unit.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-05-reverse-osmosis.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician reading flow meters on the front of a reverse osmosis unit.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician reading flow meters on the front of a reverse osmosis unit." — confirmed
```

### WATER-05-A ★ — Inside a spiral-wound membrane

**File:** `images/water-treatment-technician-05-ro-membrane.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-05-reverse-osmosis.html, section `ro`

**Job:** U: sees feed water splitting into product and reject across the membrane.

**Alt:** Cutaway of a spiral-wound reverse osmosis membrane showing feed, product, and reject.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Inside a spiral-wound membrane · academy/water-treatment-technician-05-reverse-osmosis.html, section `ro`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Cutaway of a spiral-wound element partly unrolled: feed enters one end, water passes through membrane sheets into the central product tube, concentrated reject exits the far end. Salts, bacteria, and endotoxin held back.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees feed water splitting into product and reject across the membrane.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Feed water in
  • Membrane sheets
  • Product water (permeate)
  • Reject water (concentrate)
  • Pressure from the pump
  • Salts, bacteria, and endotoxin held back
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No product leaving from the reject end
✗ no claim of 100 percent removal
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Feed water in" present and spelled exactly — confirmed
□ Label "Membrane sheets" present and spelled exactly — confirmed
□ Label "Product water (permeate)" present and spelled exactly — confirmed
□ Label "Reject water (concentrate)" present and spelled exactly — confirmed
□ Label "Pressure from the pump" present and spelled exactly — confirmed
□ Label "Salts, bacteria, and endotoxin held back" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-05-B ★ — Rejection and recovery

**File:** `images/water-treatment-technician-05-rejection-recovery.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-05-reverse-osmosis.html, section `numbers`

**Job:** A: calculates percent rejection and percent recovery.

**Alt:** Formulas and worked examples for percent rejection and percent recovery.

```text
Reference card · 1672 × 941, 16:9 landscape · Rejection and recovery · academy/water-treatment-technician-05-reverse-osmosis.html, section `numbers`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two formula tiles with the lesson examples: rejection (400 − 8) ÷ 400 × 100 = 98%; recovery 6 ÷ 10 × 100 = 60%.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: calculates percent rejection and percent recovery.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Percent rejection = (feed − product) ÷ feed × 100
  • Feed 400, product 8: 98%
  • Percent recovery = product flow ÷ feed flow × 100
  • Product 6, feed 10: 60%
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ no units on conductivity beyond the lesson
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Percent rejection = (feed − product) ÷ feed × 100" present and spelled exactly — confirmed
□ Label "Feed 400, product 8: 98%" present and spelled exactly — confirmed
□ Label "Percent recovery = product flow ÷ feed flow × 100" present and spelled exactly — confirmed
□ Label "Product 6, feed 10: 60%" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-05-C ○ — Reading the changes

**File:** `images/water-treatment-technician-05-ro-trends.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-05-reverse-osmosis.html, section `numbers`

**Job:** A: links a trend to its likely cause.

**Alt:** Four trend sketches for a reverse osmosis unit with likely causes.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Reading the changes · academy/water-treatment-technician-05-reverse-osmosis.html, section `numbers`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four small trend sketches without axis numbers: rejection falling; product flow falling; pressure drop rising; sudden change after service. Each with one likely cause line.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: links a trend to its likely cause.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Rejection falling: damage, leak, or scale
  • Flow falling: fouling or cold water
  • Pressure drop rising: plugging
  • Sudden change after service: check the work
  • Report trends before alarms
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No axis values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Rejection falling: damage, leak, or scale" present and spelled exactly — confirmed
□ Label "Flow falling: fouling or cold water" present and spelled exactly — confirmed
□ Label "Pressure drop rising: plugging" present and spelled exactly — confirmed
□ Label "Sudden change after service: check the work" present and spelled exactly — confirmed
□ Label "Report trends before alarms" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 6 — The Distribution Loop, Storage, and Final Filters

### WATER-06-H — Module hero

**File:** `images/water-treatment-technician-06-distribution-loop-storage-filters-vignette-hero.png` · **Alt:** A technician tracing ceiling-level loop pipework down to a wall outlet at a dialysis station.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-06-distribution-loop-storage-filters.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician tracing ceiling-level loop pipework down to a wall outlet at a dialysis station.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician tracing ceiling-level loop pipework down to a wall outlet at a dialysis station." — confirmed
```

### WATER-06-A ★ — A loop that never stops

**File:** `images/water-treatment-technician-06-loop-layout.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `loop`

**Job:** U: follows product water around the loop and back.

**Alt:** Plan of a distribution loop passing each station and returning to its start.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · A loop that never stops · academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `loop`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Plan view: reverse osmosis unit feeding a loop past six stations and returning to its start; short drops to each station; sample ports at loop start and loop return.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows product water around the loop and back.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • From reverse osmosis
  • Loop supply
  • Stations
  • Loop return
  • Sample port: start
  • Sample port: return
  • Water keeps moving
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No loop ending at the last station
✗ no long branches
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "From reverse osmosis" present and spelled exactly — confirmed
□ Label "Loop supply" present and spelled exactly — confirmed
□ Label "Stations" present and spelled exactly — confirmed
□ Label "Loop return" present and spelled exactly — confirmed
□ Label "Sample port: start" present and spelled exactly — confirmed
□ Label "Sample port: return" present and spelled exactly — confirmed
□ Label "Water keeps moving" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-06-B ★ — Dead legs

**File:** `images/water-treatment-technician-06-dead-legs.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `loop`

**Job:** A: recognizes a dead leg.

**Alt:** Comparison of a correct short branch with a dead leg where water stagnates.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Dead legs · academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `loop`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Side-by-side: correct short branch with flowing loop; incorrect long capped branch with still water and biofilm on the wall.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: recognizes a dead leg.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Short branch: correct
  • Long capped branch: dead leg
  • Still water
  • Biofilm grows here
  • Report unused branches
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No dimensions
✗ no brand fittings
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Short branch: correct" present and spelled exactly — confirmed
□ Label "Long capped branch: dead leg" present and spelled exactly — confirmed
□ Label "Still water" present and spelled exactly — confirmed
□ Label "Biofilm grows here" present and spelled exactly — confirmed
□ Label "Report unused branches" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-06-C ○ — Storage tank done right

**File:** `images/water-treatment-technician-06-storage-tank.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `storage`

**Job:** U: names the features that keep a storage tank clean.

**Alt:** Cutaway of a dialysis water storage tank with its hygienic design features.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Storage tank done right · academy/water-treatment-technician-06-distribution-loop-storage-filters.html, section `storage`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Tank cutaway: tight lid, filtered air vent, conical base draining fully from the lowest point, spray ball for disinfection, ultraviolet lamp and ultrafilter downstream.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: names the features that keep a storage tank clean.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Tight lid
  • Filtered vent
  • Sloped base, drains fully
  • Spray ball
  • Ultraviolet lamp
  • Ultrafilter after the lamp
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No flat-bottom tank
✗ no open top
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Tight lid" present and spelled exactly — confirmed
□ Label "Filtered vent" present and spelled exactly — confirmed
□ Label "Sloped base, drains fully" present and spelled exactly — confirmed
□ Label "Spray ball" present and spelled exactly — confirmed
□ Label "Ultraviolet lamp" present and spelled exactly — confirmed
□ Label "Ultrafilter after the lamp" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 7 — Concentrates and Central Delivery

### WATER-07-H — Module hero

**File:** `images/water-treatment-technician-07-concentrates-central-delivery-vignette-hero.png` · **Alt:** A technician reading the label on a concentrate container against an order sheet.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-07-concentrates-central-delivery.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician reading the label on a concentrate container against an order sheet.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician reading the label on a concentrate container against an order sheet." — confirmed
```

### WATER-07-A ★ — Two concentrates, one dialysate

**File:** `images/water-treatment-technician-07-two-concentrates.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-07-concentrates-central-delivery.html, section `concentrates`

**Job:** U: knows what each concentrate supplies.

**Alt:** Acid and bicarbonate concentrates combining with treated water in the machine.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Two concentrates, one dialysate · academy/water-treatment-technician-07-concentrates-central-delivery.html, section `concentrates`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two containers and a machine mixing point. Acid concentrate: most salts including potassium and calcium, formula varies. Bicarbonate concentrate: the buffer; short use time once mixed.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: knows what each concentrate supplies.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Acid concentrate: salts, potassium, calcium
  • Bicarbonate concentrate: the buffer
  • Treated water
  • Machine mixes in a fixed ratio
  • Label must match the order
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No ratio numbers
✗ no electrolyte values
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Acid concentrate: salts, potassium, calcium" present and spelled exactly — confirmed
□ Label "Bicarbonate concentrate: the buffer" present and spelled exactly — confirmed
□ Label "Treated water" present and spelled exactly — confirmed
□ Label "Machine mixes in a fixed ratio" present and spelled exactly — confirmed
□ Label "Label must match the order" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-07-B ★ — Mixing bicarbonate safely

**File:** `images/water-treatment-technician-07-bicarbonate-mixing.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-07-concentrates-central-delivery.html, section `bicarb`

**Job:** A: mixes, labels, verifies, and discards on time.

**Alt:** Steps for mixing, verifying, and labeling bicarbonate concentrate.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Mixing bicarbonate safely · academy/water-treatment-technician-07-concentrates-central-delivery.html, section `bicarb`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps: clean hands and container; treated water to the mark; add the powder; mix gently, no foaming; verify by the unit's test; label with date, time, and name; discard at the stated time.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: mixes, labels, verifies, and discards on time.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Clean container
  • Treated water to the mark
  • Add powder
  • Mix gently
  • Verify
  • Label: date, time, name
  • Discard on time
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No hours stated
✗ no vigorous shaking
✗ no tap water
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Clean container" present and spelled exactly — confirmed
□ Label "Treated water to the mark" present and spelled exactly — confirmed
□ Label "Add powder" present and spelled exactly — confirmed
□ Label "Mix gently" present and spelled exactly — confirmed
□ Label "Verify" present and spelled exactly — confirmed
□ Label "Label: date, time, name" present and spelled exactly — confirmed
□ Label "Discard on time" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-07-C ○ — Central concentrate delivery

**File:** `images/water-treatment-technician-07-central-delivery.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-07-concentrates-central-delivery.html, section `central`

**Job:** U: follows concentrate from tank to station outlet.

**Alt:** Central acid and bicarbonate concentrate tanks feeding separate lines to station outlets.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Central concentrate delivery · academy/water-treatment-technician-07-concentrates-central-delivery.html, section `central`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Schematic: labeled acid tank and bicarbonate tank, separate color-keyed lines, wall outlets with different connectors for acid and bicarbonate at a station.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows concentrate from tank to station outlet.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Acid tank
  • Bicarbonate tank
  • Separate lines
  • Station outlets
  • Different connectors prevent mix-ups
  • Bicarbonate system is disinfected on schedule
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No shared line for both concentrates
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Acid tank" present and spelled exactly — confirmed
□ Label "Bicarbonate tank" present and spelled exactly — confirmed
□ Label "Separate lines" present and spelled exactly — confirmed
□ Label "Station outlets" present and spelled exactly — confirmed
□ Label "Different connectors prevent mix-ups" present and spelled exactly — confirmed
□ Label "Bicarbonate system is disinfected on schedule" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 8 — Daily Monitoring, Logs, and Trends

### WATER-08-H — Module hero

**File:** `images/water-treatment-technician-08-daily-monitoring-logs-trends-vignette-hero.png` · **Alt:** A technician writing numbers on a water room log sheet clipped beside a gauge panel.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician writing numbers on a water room log sheet clipped beside a gauge panel.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician writing numbers on a water room log sheet clipped beside a gauge panel." — confirmed
```

### WATER-08-A ★ — The start-of-day round

**File:** `images/water-treatment-technician-08-daily-round.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `checks`

**Job:** A: performs the daily checks in order and releases the system.

**Alt:** Six-stop start-of-day round ending with release to the nurse.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The start-of-day round · academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `checks`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six stops along a system outline: system running and stable; chlorine; pretreatment pressures, softener clock, salt; reverse osmosis readings; loop readings; sign and release.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: performs the daily checks in order and releases the system.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 System stable
  • 2 Total chlorine
  • 3 Pretreatment
  • 4 Reverse osmosis
  • 5 Loop
  • 6 Sign and tell the nurse: released
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No values
✗ no skipped stop
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 System stable" present and spelled exactly — confirmed
□ Label "2 Total chlorine" present and spelled exactly — confirmed
□ Label "3 Pretreatment" present and spelled exactly — confirmed
□ Label "4 Reverse osmosis" present and spelled exactly — confirmed
□ Label "5 Loop" present and spelled exactly — confirmed
□ Label "6 Sign and tell the nurse: released" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-08-B ★ — A log that can be trusted

**File:** `images/water-treatment-technician-08-good-log.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `records`

**Job:** A: writes entries with numbers, units, times, and names.

**Alt:** Comparison of a weak water log entry with a complete one.

```text
Reference card · 1672 × 941, 16:9 landscape · A log that can be trusted · academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `records`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two mock log rows side by side: weak (ticks, 'OK', blanks) crossed in amber; strong (number with unit, port, time, name; a single-line correction with initials). Mock data only.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: writes entries with numbers, units, times, and names.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Ticks and OK: not evidence
  • Number, unit, port, time, name
  • Correct with one line and initials
  • No blanks: write why
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No real names
✗ no illegible handwriting
✗ values only as generic placeholders shown as dashes
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Ticks and OK: not evidence" present and spelled exactly — confirmed
□ Label "Number, unit, port, time, name" present and spelled exactly — confirmed
□ Label "Correct with one line and initials" present and spelled exactly — confirmed
□ Label "No blanks: write why" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-08-C ○ — Trends before alarms

**File:** `images/water-treatment-technician-08-trend-chart.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `trends`

**Job:** A: spots a drift before a limit is reached.

**Alt:** Run chart with results rising toward an action level and a flag to report the trend.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Trends before alarms · academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `trends`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
One run chart, unlabeled units, with a limit line and an action-level line; points creeping upward but still below the action level; a flag 'report now'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: spots a drift before a limit is reached.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Limit
  • Action level
  • Today
  • Report the trend now
  • Planned fix beats emergency
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numbers on axes
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Limit" present and spelled exactly — confirmed
□ Label "Action level" present and spelled exactly — confirmed
□ Label "Today" present and spelled exactly — confirmed
□ Label "Report the trend now" present and spelled exactly — confirmed
□ Label "Planned fix beats emergency" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 9 — Chemical Analysis and Microbiological Sampling

### WATER-09-H — Module hero

**File:** `images/water-treatment-technician-09-chemical-microbiological-sampling-vignette-hero.png` · **Alt:** Gloved hands collecting water from a sample port into a sterile container.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-09-chemical-microbiological-sampling.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: Gloved hands collecting water from a sample port into a sterile container.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "Gloved hands collecting water from a sample port into a sterile container." — confirmed
```

### WATER-09-A ★ — Collecting a sample

**File:** `images/water-treatment-technician-09-sampling-steps.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `sampling`

**Job:** A: collects a culture and endotoxin sample without contaminating it.

**Alt:** Six steps for collecting a water sample aseptically.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Collecting a sample · academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `sampling`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six panels: label the container first; clean hands and gloves; open the port and flush; fill without touching the inside of cap or container; close at once; keep cold and send.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: collects a culture and endotoxin sample without contaminating it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Label first
  • 2 Hand hygiene, gloves
  • 3 Flush the port
  • 4 Fill, touch nothing inside
  • 5 Close at once
  • 6 Keep cold, send promptly
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No bleach on the port
✗ no fingers inside the cap
✗ no flush time in seconds
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Label first" present and spelled exactly — confirmed
□ Label "2 Hand hygiene, gloves" present and spelled exactly — confirmed
□ Label "3 Flush the port" present and spelled exactly — confirmed
□ Label "4 Fill, touch nothing inside" present and spelled exactly — confirmed
□ Label "5 Close at once" present and spelled exactly — confirmed
□ Label "6 Keep cold, send promptly" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-09-B ★ — Where to sample

**File:** `images/water-treatment-technician-09-sample-points.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `points`

**Job:** U: knows the usual sample points and why the loop return matters most.

**Alt:** System outline marking the usual microbiological sample points.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Where to sample · academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `points`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
System outline with pins: after reverse osmosis (loop start), loop return (highest counts), storage tank outlet if present, selected machines for dialysis fluid. Note: sample before disinfection.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: knows the usual sample points and why the loop return matters most.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Loop start
  • Loop return: usually highest
  • Tank outlet
  • Machines in rotation
  • Sample before disinfection, not after
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No frequency numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Loop start" present and spelled exactly — confirmed
□ Label "Loop return: usually highest" present and spelled exactly — confirmed
□ Label "Tank outlet" present and spelled exactly — confirmed
□ Label "Machines in rotation" present and spelled exactly — confirmed
□ Label "Sample before disinfection, not after" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-09-C ○ — Limit and action level

**File:** `images/water-treatment-technician-09-action-level.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `limits`

**Job:** A: acts at the action level instead of waiting for the limit.

**Alt:** Gauge showing the bacteria limit and action level for dialysis water.

```text
Reference card · 1672 × 941, 16:9 landscape · Limit and action level · academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `limits`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Vertical gauge for dialysis water bacteria: green zone to the action level 50 CFU/mL, amber from 50 to the limit 100 CFU/mL, red above. Values exactly as the lesson.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: acts at the action level instead of waiting for the limit.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Limit: 100 CFU/mL
  • Typical action level: 50 CFU/mL
  • Below: continue
  • Between: act now
  • Above: hold and report
  • Use your facility's written values
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Limit: 100 CFU/mL" present and spelled exactly — confirmed
□ Label "Typical action level: 50 CFU/mL" present and spelled exactly — confirmed
□ Label "Below: continue" present and spelled exactly — confirmed
□ Label "Between: act now" present and spelled exactly — confirmed
□ Label "Above: hold and report" present and spelled exactly — confirmed
□ Label "Use your facility's written values" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 10 — Disinfection and Biofilm Control

### WATER-10-H — Module hero

**File:** `images/water-treatment-technician-10-disinfection-biofilm-control-vignette-hero.png` · **Alt:** A technician in gloves, apron, and eye protection hanging a 'disinfection in progress' sign at an empty treatment station.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-10-disinfection-biofilm-control.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician in gloves, apron, and eye protection hanging a 'disinfection in progress' sign at an empty treatment station.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician in gloves, apron, and eye protection hanging a 'disinfection in progress' sign at an empty treatment station." — confirmed
```

### WATER-10-A ★ — How biofilm forms

**File:** `images/water-treatment-technician-10-biofilm.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `biofilm`

**Job:** U: follows attachment, growth, maturity, and shedding.

**Alt:** Four stages of biofilm forming on a pipe wall.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · How biofilm forms · academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `biofilm`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four-stage cross-section of a pipe wall: few bacteria attach; they multiply and build slime; mature layer resists disinfectant; fragments and endotoxin shed downstream.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows attachment, growth, maturity, and shedding.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Attachment
  • Growth
  • Mature biofilm
  • Shedding bacteria and endotoxin
  • Easier to prevent than to remove
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No cartoon faces on bacteria
✗ no magnification figures
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Attachment" present and spelled exactly — confirmed
□ Label "Growth" present and spelled exactly — confirmed
□ Label "Mature biofilm" present and spelled exactly — confirmed
□ Label "Shedding bacteria and endotoxin" present and spelled exactly — confirmed
□ Label "Easier to prevent than to remove" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-10-B ★ — Chemical disinfection, start to release

**File:** `images/water-treatment-technician-10-disinfection-cycle.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `disinfection`

**Job:** A: completes a chemical disinfection with proof at each step.

**Alt:** Six steps of a chemical disinfection ending with a negative residual test.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Chemical disinfection, start to release · academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `disinfection`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps: no patients, signs posted, protective equipment; dose and circulate; test that disinfectant reached the farthest point; dwell; rinse; residual test negative at every outlet, record, release.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: completes a chemical disinfection with proof at each step.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • No patients, signs up
  • Dose and circulate
  • Prove it reached the far end
  • Dwell
  • Rinse
  • Residual test negative at every outlet
  • Record and release
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No concentrations or times
✗ no patient in the scene
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "No patients, signs up" present and spelled exactly — confirmed
□ Label "Dose and circulate" present and spelled exactly — confirmed
□ Label "Prove it reached the far end" present and spelled exactly — confirmed
□ Label "Dwell" present and spelled exactly — confirmed
□ Label "Rinse" present and spelled exactly — confirmed
□ Label "Residual test negative at every outlet" present and spelled exactly — confirmed
□ Label "Record and release" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-10-C ○ — Heat or chemical

**File:** `images/water-treatment-technician-10-heat-vs-chemical.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `disinfection`

**Job:** U: compares the two methods.

**Alt:** Comparison of heat and chemical disinfection.

```text
Reference card · 1672 × 941, 16:9 landscape · Heat or chemical · academy/water-treatment-technician-10-disinfection-biofilm-control.html, section `disinfection`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two columns. Heat: hot water circulated, no chemical residue, system must be built for it. Chemical: agent circulated and left to dwell, must be rinsed and tested.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: compares the two methods.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Heat
  • Chemical
  • No residue
  • Needs rinse and residual test
  • System must be heat-rated
  • Follow the manufacturer's method
  • Never mix bleach and acid
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No temperatures
✗ no product names
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Heat" present and spelled exactly — confirmed
□ Label "Chemical" present and spelled exactly — confirmed
□ Label "No residue" present and spelled exactly — confirmed
□ Label "Needs rinse and residual test" present and spelled exactly — confirmed
□ Label "System must be heat-rated" present and spelled exactly — confirmed
□ Label "Follow the manufacturer's method" present and spelled exactly — confirmed
□ Label "Never mix bleach and acid" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 11 — Maintenance, Component Replacement, and Validation

### WATER-11-H — Module hero

**File:** `images/water-treatment-technician-11-maintenance-replacement-validation-vignette-hero.png` · **Alt:** A technician fitting a new filter cartridge into an open housing, old cartridge in a tray.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-11-maintenance-replacement-validation.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician fitting a new filter cartridge into an open housing, old cartridge in a tray.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician fitting a new filter cartridge into an open housing, old cartridge in a tray." — confirmed
```

### WATER-11-A ★ — The maintenance calendar

**File:** `images/water-treatment-technician-11-maintenance-calendar.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `schedule`

**Job:** U: sees maintenance as recurring tasks at different intervals.

**Alt:** Planner showing recurring maintenance tasks by interval.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The maintenance calendar · academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `schedule`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Wall-planner style graphic with rows for components and generic recurring markers at daily, weekly, monthly, and yearly columns; no dates.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees maintenance as recurring tasks at different intervals.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Daily
  • Weekly
  • Monthly
  • Yearly
  • Filters
  • Softener
  • Carbon
  • Reverse osmosis
  • Loop disinfection
  • Lamps and ultrafilters
  • Follow the manufacturer's intervals
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No specific intervals asserted as rules beyond the column heads
✗ no dates
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Daily" present and spelled exactly — confirmed
□ Label "Weekly" present and spelled exactly — confirmed
□ Label "Monthly" present and spelled exactly — confirmed
□ Label "Yearly" present and spelled exactly — confirmed
□ Label "Filters" present and spelled exactly — confirmed
□ Label "Softener" present and spelled exactly — confirmed
□ Label "Carbon" present and spelled exactly — confirmed
□ Label "Reverse osmosis" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-11-B ★ — After every change, re-test

**File:** `images/water-treatment-technician-11-post-change-tests.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `retest`

**Job:** A: matches a component change to the checks required before release.

**Alt:** Grid matching each component replacement to its post-change checks.

```text
Reference card · 1672 × 941, 16:9 landscape · After every change, re-test · academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `retest`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Grid: new cartridge (flush, pressure drop); new carbon (rinse until clear, total chlorine at both ports); regenerated or new resin (rinse, hardness); new membrane (flush, rejection, conductivity); pipe work (disinfect, culture).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: matches a component change to the checks required before release.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • New cartridge: flush, pressures
  • New carbon: rinse, chlorine at both ports
  • New resin: rinse, hardness
  • New membrane: flush, rejection
  • Pipe work: disinfect, culture
  • Release in writing
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No rinse times or volumes
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "New cartridge: flush, pressures" present and spelled exactly — confirmed
□ Label "New carbon: rinse, chlorine at both ports" present and spelled exactly — confirmed
□ Label "New resin: rinse, hardness" present and spelled exactly — confirmed
□ Label "New membrane: flush, rejection" present and spelled exactly — confirmed
□ Label "Pipe work: disinfect, culture" present and spelled exactly — confirmed
□ Label "Release in writing" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-11-C ○ — Before the service engineer leaves

**File:** `images/water-treatment-technician-11-service-handover.png` · **Canvas:** 1024 × 1536, 2:3 portrait · **Placement:** academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `service`

**Job:** A: verifies and documents a supplier service visit.

**Alt:** Five checks to complete before a service engineer leaves.

```text
Process or decision figure · 1024 × 1536, 2:3 portrait · Before the service engineer leaves · academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `service`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five checks: what was done and why; parts replaced; tests run and results; system back in normal position (valves, timers); signed report filed.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1024 × 1536, 2:3 portrait. Steps read top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: verifies and documents a supplier service visit.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • What was done?
  • Parts replaced?
  • Tests and results?
  • Valves and timers back to normal?
  • Signed report filed
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No company logos
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "What was done?" present and spelled exactly — confirmed
□ Label "Parts replaced?" present and spelled exactly — confirmed
□ Label "Tests and results?" present and spelled exactly — confirmed
□ Label "Valves and timers back to normal?" present and spelled exactly — confirmed
□ Label "Signed report filed" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 12 — Failures, Emergencies, and Capstone

### WATER-12-H — Module hero

**File:** `images/water-treatment-technician-12-failures-emergencies-capstone-vignette-hero.png` · **Alt:** A technician placing a red 'HOLD' tag on a water system control panel while speaking to a nurse.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/water-treatment-technician-12-failures-emergencies-capstone.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician placing a red 'HOLD' tag on a water system control panel while speaking to a nurse.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician placing a red 'HOLD' tag on a water system control panel while speaking to a nurse." — confirmed
```

### WATER-12-A ★ — Stop, hold, report

**File:** `images/water-treatment-technician-12-stop-hold-report.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `pattern`

**Job:** A: applies one response to any out-of-range result.

**Alt:** Six-step response to an out-of-range water result.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Stop, hold, report · academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `pattern`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps with the first three emphasized: stop, hold, report, investigate, correct and verify, release by the designated person.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: applies one response to any out-of-range result.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Stop
  • Hold
  • Report
  • Investigate
  • Correct and verify
  • Release: designated person, in writing
  • A better repeat test does not cancel the first
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Stop" present and spelled exactly — confirmed
□ Label "Hold" present and spelled exactly — confirmed
□ Label "Report" present and spelled exactly — confirmed
□ Label "Investigate" present and spelled exactly — confirmed
□ Label "Correct and verify" present and spelled exactly — confirmed
□ Label "Release: designated person, in writing" present and spelled exactly — confirmed
□ Label "A better repeat test does not cancel the first" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-12-B ★ — Four failures, first response

**File:** `images/water-treatment-technician-12-four-failures.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `failures`

**Job:** A: gives the first response for the four common failures.

**Alt:** Four water system failures with the technician's first response.

```text
Reference card · 1672 × 941, 16:9 landscape · Four failures, first response · academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `failures`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four tiles: chlorine above limit after tank 2; reverse osmosis failure; loss of feed water; suspected contamination. Each with 'technician does' and 'others decide'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: gives the first response for the four common failures.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Chlorine breakthrough
  • Reverse osmosis failure
  • Loss of supply
  • Suspected contamination
  • Technician: hold, report, record
  • Nurse and physician decide about patients
  • Sample before disinfecting
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No instruction to disconnect patients
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Chlorine breakthrough" present and spelled exactly — confirmed
□ Label "Reverse osmosis failure" present and spelled exactly — confirmed
□ Label "Loss of supply" present and spelled exactly — confirmed
□ Label "Suspected contamination" present and spelled exactly — confirmed
□ Label "Technician: hold, report, record" present and spelled exactly — confirmed
□ Label "Nurse and physician decide about patients" present and spelled exactly — confirmed
□ Label "Sample before disinfecting" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### WATER-12-C ○ — After a flood or long outage

**File:** `images/water-treatment-technician-12-after-flood.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `disaster`

**Job:** A: restarts a system safely after disruption.

**Alt:** Five steps for restarting a water system after an outage or flood.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · After a flood or long outage · academy/water-treatment-technician-12-failures-emergencies-capstone.html, section `disaster`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps: do not assume; check clocks and timers; flush the loop; run start-of-day tests; after a flood, inspect, disinfect, and culture before release.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: restarts a system safely after disruption.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Do not assume
  • Check clocks and timers
  • Flush
  • Test before any patient
  • After a flood: inspect, disinfect, culture
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No floodwater near patients
✗ no values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Do not assume" present and spelled exactly — confirmed
□ Label "Check clocks and timers" present and spelled exactly — confirmed
□ Label "Flush" present and spelled exactly — confirmed
□ Label "Test before any patient" present and spelled exactly — confirmed
□ Label "After a flood: inspect, disinfect, culture" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


# Hemodialysis Center Biomedical Technician

## BIOMED-H0 — Hub hero

**File:** `images/dialysis-biomedical-technician-vignette-hero.png` · **Alt:** A biomedical technician servicing a hemodialysis machine in a workshop.

```text
Circular vignette hero · 2048 × 2048, 1:1 · hub page academy/dialysis-biomedical-technician.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A Filipino biomedical technician in a workshop with a hemodialysis machine's rear panel open, holding a handheld meter, service manual open on the bench.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A biomedical technician servicing a hemodialysis machine in a workshop." — confirmed
```


## Module 1 — The Biomedical Technician's Role and Safe Working

### BIOMED-01-H — Module hero

**File:** `images/dialysis-biomedical-technician-01-role-and-safe-working-vignette-hero.png` · **Alt:** A technician in gloves and eye protection attaching an out-of-service tag to a hemodialysis machine.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-01-role-and-safe-working.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician in gloves and eye protection attaching an out-of-service tag to a hemodialysis machine.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician in gloves and eye protection attaching an out-of-service tag to a hemodialysis machine." — confirmed
```

### BIOMED-01-A ★ — Before you open a machine

**File:** `images/dialysis-biomedical-technician-01-before-opening.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `hazards`

**Job:** A: prepares a machine safely for service.

**Alt:** Five steps to prepare a dialysis machine for service.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Before you open a machine · academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `hazards`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Five steps: confirm no patient and tag out; disinfect; switch off, unplug, close water, lock out; gloves and eye protection, dry floor; open the correct service manual.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: prepares a machine safely for service.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Confirm status, tag out
  • 2 Disinfect
  • 3 Unplug, close water, lock out
  • 4 Protect yourself
  • 5 Work by the manual
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No patient connected
✗ no open panel while plugged in
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Confirm status, tag out" present and spelled exactly — confirmed
□ Label "2 Disinfect" present and spelled exactly — confirmed
□ Label "3 Unplug, close water, lock out" present and spelled exactly — confirmed
□ Label "4 Protect yourself" present and spelled exactly — confirmed
□ Label "5 Work by the manual" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-01-B ★ — Four hazards

**File:** `images/dialysis-biomedical-technician-01-four-hazards.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `hazards`

**Job:** U: names the four hazards and the control for each.

**Alt:** Four hazards of dialysis equipment service with the control for each.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Four hazards · academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `hazards`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Four quadrants around an opened machine: blood and body fluids (disinfect, gloves); electricity (unplug, lock out); hot water and pressure (cool, depressurize); chemicals (safety data sheet, never mix).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: names the four hazards and the control for each.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Blood and body fluids
  • Electricity
  • Hot water and pressure
  • Chemicals
  • Disinfect first
  • Unplug and lock out
  • Let it cool
  • Read the safety data sheet
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No sparks or injury imagery
✗ no chemical brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Blood and body fluids" present and spelled exactly — confirmed
□ Label "Electricity" present and spelled exactly — confirmed
□ Label "Hot water and pressure" present and spelled exactly — confirmed
□ Label "Chemicals" present and spelled exactly — confirmed
□ Label "Disinfect first" present and spelled exactly — confirmed
□ Label "Unplug and lock out" present and spelled exactly — confirmed
□ Label "Let it cool" present and spelled exactly — confirmed
□ Label "Read the safety data sheet" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-01-C ○ — The life of a fault

**File:** `images/dialysis-biomedical-technician-01-life-of-a-fault.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `tagging`

**Job:** U: follows a fault from report to release.

**Alt:** Six steps from a fault report to formal release.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The life of a fault · academy/dialysis-biomedical-technician-01-role-and-safe-working.html, section `tagging`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps: reported, tagged, diagnosed and repaired, tested, disinfected, released and accepted by the charge nurse.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: follows a fault from report to release.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Reported
  • Tagged out
  • Repaired by the manual
  • Tested
  • Disinfected
  • Released and accepted
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No work order numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Reported" present and spelled exactly — confirmed
□ Label "Tagged out" present and spelled exactly — confirmed
□ Label "Repaired by the manual" present and spelled exactly — confirmed
□ Label "Tested" present and spelled exactly — confirmed
□ Label "Disinfected" present and spelled exactly — confirmed
□ Label "Released and accepted" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 2 — Electrical and Electronic Fundamentals for Dialysis Equipment

### BIOMED-02-H — Module hero

**File:** `images/dialysis-biomedical-technician-02-electrical-electronic-fundamentals-vignette-hero.png` · **Alt:** A technician holding multimeter probes over a training circuit board on an antistatic mat, wrist strap on.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician holding multimeter probes over a training circuit board on an antistatic mat, wrist strap on.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician holding multimeter probes over a training circuit board on an antistatic mat, wrist strap on." — confirmed
```

### BIOMED-02-A ★ — Sensor, controller, actuator

**File:** `images/dialysis-biomedical-technician-02-control-loop.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `blocks`

**Job:** U: understands every machine function as sense, decide, act.

**Alt:** Block diagram of a control loop with a sensor, controller, actuator, and an independent protective sensor.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Sensor, controller, actuator · academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `blocks`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Block diagram of one loop using dialysate temperature as the example: temperature sensor, control board, heater, and a second independent sensor that can trigger an alarm.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands every machine function as sense, decide, act.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Sensor: measures
  • Controller: decides
  • Actuator: acts
  • Heater
  • Independent protective sensor
  • Alarm and safe state
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No circuit values
✗ no brand boards
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Sensor: measures" present and spelled exactly — confirmed
□ Label "Controller: decides" present and spelled exactly — confirmed
□ Label "Actuator: acts" present and spelled exactly — confirmed
□ Label "Heater" present and spelled exactly — confirmed
□ Label "Independent protective sensor" present and spelled exactly — confirmed
□ Label "Alarm and safe state" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-02-B ★ — Power path and protective earth

**File:** `images/dialysis-biomedical-technician-02-power-path.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `power`

**Job:** U: follows mains power into the machine and sees the earth path.

**Alt:** Mains power path into a dialysis machine with the protective earth bonded to the case.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Power path and protective earth · academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `power`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Wall outlet with three conductors, power cord, fuse, power supply, low-voltage boards. Earth wire bonded to the metal chassis. Colors by role with a legend; wire colors not asserted as a wiring code.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows mains power into the machine and sees the earth path.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Outlet
  • Live
  • Neutral
  • Protective earth
  • Fuse
  • Power supply
  • Low-voltage electronics
  • Earth bonded to the metal case
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No voltage numbers
✗ no wire color code claims
✗ no exposed live parts being touched
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Outlet" present and spelled exactly — confirmed
□ Label "Live" present and spelled exactly — confirmed
□ Label "Neutral" present and spelled exactly — confirmed
□ Label "Protective earth" present and spelled exactly — confirmed
□ Label "Fuse" present and spelled exactly — confirmed
□ Label "Power supply" present and spelled exactly — confirmed
□ Label "Low-voltage electronics" present and spelled exactly — confirmed
□ Label "Earth bonded to the metal case" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-02-C ○ — Multimeter safely

**File:** `images/dialysis-biomedical-technician-02-multimeter.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `meter`

**Job:** A: selects the function and measures safely.

**Alt:** Multimeter with safe-use reminders.

```text
Reference card · 1672 × 941, 16:9 landscape · Multimeter safely · academy/dialysis-biomedical-technician-02-electrical-electronic-fundamentals.html, section `meter`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic multimeter with three callouts: choose the function before connecting; test the meter on a known source; one hand, insulated probes, de-energize for resistance and continuity.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: selects the function and measures safely.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Choose the function first
  • Test on a known source
  • De-energize for resistance
  • Insulated probes
  • In-date calibration label
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No readings on the display
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Choose the function first" present and spelled exactly — confirmed
□ Label "Test on a known source" present and spelled exactly — confirmed
□ Label "De-energize for resistance" present and spelled exactly — confirmed
□ Label "Insulated probes" present and spelled exactly — confirmed
□ Label "In-date calibration label" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 3 — Dialysate Side I: Water Inlet, Heating, and Degassing

### BIOMED-03-H — Module hero

**File:** `images/dialysis-biomedical-technician-03-dialysate-water-heating-degassing-vignette-hero.png` · **Alt:** A technician holding a reference thermometer probe at a dialysate sample point on a machine.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician holding a reference thermometer probe at a dialysate sample point on a machine.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician holding a reference thermometer probe at a dialysate sample point on a machine." — confirmed
```

### BIOMED-03-A ★ — From inlet to degassed warm water

**File:** `images/dialysis-biomedical-technician-03-inlet-heat-degas.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

**Job:** U: traces water through regulator, heat exchanger, heater, and degassing.

**Alt:** Schematic of water inlet, heating, and degassing in a dialysis machine.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · From inlet to degassed warm water · academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Left-to-right hydraulic schematic: water inlet, pressure regulator, heat exchanger warmed by outgoing used dialysate, heater, degassing chamber with pump and air vent, two temperature sensors.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: traces water through regulator, heat exchanger, heater, and degassing.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Water inlet
  • Pressure regulator
  • Heat exchanger
  • Heater
  • Degassing pump and chamber
  • Air vented
  • Control temperature sensor
  • Protective temperature sensor
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No temperatures
✗ no concentrates before degassing
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Water inlet" present and spelled exactly — confirmed
□ Label "Pressure regulator" present and spelled exactly — confirmed
□ Label "Heat exchanger" present and spelled exactly — confirmed
□ Label "Heater" present and spelled exactly — confirmed
□ Label "Degassing pump and chamber" present and spelled exactly — confirmed
□ Label "Air vented" present and spelled exactly — confirmed
□ Label "Control temperature sensor" present and spelled exactly — confirmed
□ Label "Protective temperature sensor" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-03-B ★ — Why bubbles matter

**File:** `images/dialysis-biomedical-technician-03-bubbles.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

**Job:** U: links poor degassing to three downstream errors.

**Alt:** Three effects of air bubbles in dialysate.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Why bubbles matter · academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three panels: bubbles on a conductivity cell (false reading); bubbles in the balancing chamber (fluid error); bubbles on dialyzer fibers (less exchange).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: links poor degassing to three downstream errors.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • False conductivity reading
  • Fluid balance error
  • Less membrane in use
  • Degas before mixing
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "False conductivity reading" present and spelled exactly — confirmed
□ Label "Fluid balance error" present and spelled exactly — confirmed
□ Label "Less membrane in use" present and spelled exactly — confirmed
□ Label "Degas before mixing" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-03-C ○ — A scaled heater

**File:** `images/dialysis-biomedical-technician-03-scaled-heater.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

**Job:** U: recognizes scale and its effect.

**Alt:** Clean heater element beside a scaled one.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · A scaled heater · academy/dialysis-biomedical-technician-03-dialysate-water-heating-degassing.html, section `prep`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two heater elements: clean, and coated with pale chalky scale; note slow warm-up and temperature alarms.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: recognizes scale and its effect.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Clean heater
  • Scaled heater
  • Scale insulates
  • Slow warm-up, temperature alarms
  • Descale on schedule
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No brand part
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Clean heater" present and spelled exactly — confirmed
□ Label "Scaled heater" present and spelled exactly — confirmed
□ Label "Scale insulates" present and spelled exactly — confirmed
□ Label "Slow warm-up, temperature alarms" present and spelled exactly — confirmed
□ Label "Descale on schedule" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 4 — Dialysate Side II: Proportioning, Conductivity, and Bypass

### BIOMED-04-H — Module hero

**File:** `images/dialysis-biomedical-technician-04-proportioning-conductivity-bypass-vignette-hero.png` · **Alt:** A technician dipping a reference conductivity meter probe into a dialysate sample beside a machine display.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician dipping a reference conductivity meter probe into a dialysate sample beside a machine display.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician dipping a reference conductivity meter probe into a dialysate sample beside a machine display." — confirmed
```

### BIOMED-04-A ★ — Mixing and checking dialysate

**File:** `images/dialysis-biomedical-technician-04-proportioning.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

**Job:** U: follows three streams to a checked mix.

**Alt:** Schematic of proportioning with control and protective conductivity cells.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Mixing and checking dialysate · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Treated water, acid concentrate pump, bicarbonate concentrate pump, mixing chambers, control conductivity cell, independent protective conductivity cell, to dialyzer.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows three streams to a checked mix.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Treated water
  • Acid pump
  • Bicarbonate pump
  • Mixing
  • Control conductivity cell
  • Protective conductivity cell
  • To dialyzer
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No ratios
✗ no millisiemens values
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Treated water" present and spelled exactly — confirmed
□ Label "Acid pump" present and spelled exactly — confirmed
□ Label "Bicarbonate pump" present and spelled exactly — confirmed
□ Label "Mixing" present and spelled exactly — confirmed
□ Label "Control conductivity cell" present and spelled exactly — confirmed
□ Label "Protective conductivity cell" present and spelled exactly — confirmed
□ Label "To dialyzer" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-04-B ★ — Bypass: the safe state

**File:** `images/dialysis-biomedical-technician-04-bypass.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `bypass`

**Job:** U: sees dialysate diverted to drain when out of limits.

**Alt:** Normal flow and bypass flow of dialysate compared.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Bypass: the safe state · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `bypass`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two states of the same schematic: normal (dialysate through dialyzer) and bypass (valve diverts to drain; dialyzer isolated; blood side still circulating).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees dialysate diverted to drain when out of limits.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Normal: through the dialyzer
  • Bypass: straight to drain
  • Out-of-range conductivity or temperature
  • Blood keeps circulating
  • Prove this at every maintenance
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No dialysate reaching the dialyzer in the bypass panel
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Normal: through the dialyzer" present and spelled exactly — confirmed
□ Label "Bypass: straight to drain" present and spelled exactly — confirmed
□ Label "Out-of-range conductivity or temperature" present and spelled exactly — confirmed
□ Label "Blood keeps circulating" present and spelled exactly — confirmed
□ Label "Prove this at every maintenance" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-04-C ○ — The total, not the recipe

**File:** `images/dialysis-biomedical-technician-04-total-not-recipe.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

**Job:** U: understands the limit of conductivity.

**Alt:** Two different concentrates producing the same conductivity reading.

```text
Reference card · 1672 × 941, 16:9 landscape · The total, not the recipe · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two containers with different labels giving the same gauge reading; caption that conductivity measures the total salts only.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: understands the limit of conductivity.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Different recipes
  • Same reading
  • Conductivity = total salts
  • Read the label
  • Verify the sensor against a reference meter
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No formulas or numbers on labels
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Different recipes" present and spelled exactly — confirmed
□ Label "Same reading" present and spelled exactly — confirmed
□ Label "Conductivity = total salts" present and spelled exactly — confirmed
□ Label "Read the label" present and spelled exactly — confirmed
□ Label "Verify the sensor against a reference meter" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 5 — Fluid Balance and Ultrafiltration Control

### BIOMED-05-H — Module hero

**File:** `images/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration-vignette-hero.png` · **Alt:** A technician reading the level in a glass measuring cylinder beside a dialysis machine.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician reading the level in a glass measuring cylinder beside a dialysis machine.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician reading the level in a glass measuring cylinder beside a dialysis machine." — confirmed
```

### BIOMED-05-A ★ — The balancing chamber

**File:** `images/dialysis-biomedical-technician-05-balancing-chamber.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

**Job:** U: sees equal volumes in and out and the separate ultrafiltration pump.

**Alt:** Balancing chamber with equal volumes of fresh and used dialysate and a separate ultrafiltration pump.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The balancing chamber · academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Chamber divided by a flexible membrane: fresh dialysate fills one side, pushing an equal volume of used dialysate out the other; valves alternate. A separate ultrafiltration pump draws from the closed loop.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees equal volumes in and out and the separate ultrafiltration pump.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Fresh dialysate in
  • Used dialysate out
  • Flexible membrane
  • Equal volumes
  • Closed loop
  • Ultrafiltration pump
  • Extra volume comes from the patient
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No volumes
✗ no single undivided chamber
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Fresh dialysate in" present and spelled exactly — confirmed
□ Label "Used dialysate out" present and spelled exactly — confirmed
□ Label "Flexible membrane" present and spelled exactly — confirmed
□ Label "Equal volumes" present and spelled exactly — confirmed
□ Label "Closed loop" present and spelled exactly — confirmed
□ Label "Ultrafiltration pump" present and spelled exactly — confirmed
□ Label "Extra volume comes from the patient" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-05-B ★ — Silent errors

**File:** `images/dialysis-biomedical-technician-05-silent-errors.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

**Job:** U: names three causes of fluid error without alarm.

**Alt:** Three hidden causes of fluid removal error in a balancing loop.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Silent errors · academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Closed loop with three callouts: a slightly leaking valve, air in the loop, an ultrafiltration pump delivering less than it reports.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: names three causes of fluid error without alarm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Leaking valve
  • Air in the loop
  • Pump delivers less than shown
  • No alarm
  • Patient weights are the clue
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Leaking valve" present and spelled exactly — confirmed
□ Label "Air in the loop" present and spelled exactly — confirmed
□ Label "Pump delivers less than shown" present and spelled exactly — confirmed
□ Label "No alarm" present and spelled exactly — confirmed
□ Label "Patient weights are the clue" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-05-C ○ — Checking ultrafiltration accuracy

**File:** `images/dialysis-biomedical-technician-05-uf-check.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

**Job:** A: outlines the volumetric check.

**Alt:** Four steps of a volumetric ultrafiltration accuracy check.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Checking ultrafiltration accuracy · academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four steps: set up by the manual; collect the pump output in a measuring cylinder for the stated time; compare with the displayed volume; adjust or repair if outside tolerance, then repeat.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: outlines the volumetric check.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Set up by the manual
  • Collect in a measuring cylinder
  • Compare with the display
  • Outside tolerance: correct and repeat
  • Record as found and as left
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No tolerance figures
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Set up by the manual" present and spelled exactly — confirmed
□ Label "Collect in a measuring cylinder" present and spelled exactly — confirmed
□ Label "Compare with the display" present and spelled exactly — confirmed
□ Label "Outside tolerance: correct and repeat" present and spelled exactly — confirmed
□ Label "Record as found and as left" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 6 — The Blood Side: Pump, Pressures, and Heparin Pump

### BIOMED-06-H — Module hero

**File:** `images/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump-vignette-hero.png` · **Alt:** A technician fitting a training pump segment into an open roller blood pump, no patient present.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician fitting a training pump segment into an open roller blood pump, no patient present.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician fitting a training pump segment into an open roller blood pump, no patient present." — confirmed
```

### BIOMED-06-A ★ — The blood circuit and its monitoring points

**File:** `images/dialysis-biomedical-technician-06-blood-circuit-monitoring.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, section `pump`

**Job:** U: locates pump, pressure points, air trap, and clamp.

**Alt:** Hemodialysis blood circuit with pressure monitoring points, air trap, and venous clamp.

> **Circuit figure.** Do not write a new layout. Generate this prompt with the `dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, flow directions, and pressure points. Emphasis for this figure: Intermittent hemodialysis. Use the dialysis-circuit-schematic skill unchanged; emphasize pressure monitoring points and the venous clamp.

### BIOMED-06-B ★ — Inside the roller pump

**File:** `images/dialysis-biomedical-technician-06-roller-pump.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, section `pump`

**Job:** U: understands occlusion.

**Alt:** Roller blood pump cutaway with correct, loose, and tight occlusion.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Inside the roller pump · academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, section `pump`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Cutaway of a two-roller pump head with the pump segment in the track. Three small states: correct occlusion; too loose (backflow); too tight (crushing).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands occlusion.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Rollers
  • Pump segment
  • Track
  • Correct occlusion
  • Too loose: flow lower than shown
  • Too tight: damages blood cells
  • Flow is calculated, not measured
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No rpm or mL/min values
✗ no blood splatter
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Rollers" present and spelled exactly — confirmed
□ Label "Pump segment" present and spelled exactly — confirmed
□ Label "Track" present and spelled exactly — confirmed
□ Label "Correct occlusion" present and spelled exactly — confirmed
□ Label "Too loose: flow lower than shown" present and spelled exactly — confirmed
□ Label "Too tight: damages blood cells" present and spelled exactly — confirmed
□ Label "Flow is calculated, not measured" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-06-C ○ — Reading the pressures

**File:** `images/dialysis-biomedical-technician-06-pressures.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, section `pressure`

**Job:** U: reads the sign and meaning of each pressure.

**Alt:** Three pressure gauges with what a change in each may mean.

```text
Reference card · 1672 × 941, 16:9 landscape · Reading the pressures · academy/dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump.html, section `pressure`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three gauges: arterial (negative), venous (positive), transmembrane (calculated). One line each on what a change may mean. A warning tile about needle dislodgement.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: reads the sign and meaning of each pressure.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Arterial: negative
  • Venous: positive
  • Transmembrane: calculated
  • More negative: poor inflow
  • Higher venous: return-side obstruction
  • A dislodged needle may not alarm
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No mmHg values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Arterial: negative" present and spelled exactly — confirmed
□ Label "Venous: positive" present and spelled exactly — confirmed
□ Label "Transmembrane: calculated" present and spelled exactly — confirmed
□ Label "More negative: poor inflow" present and spelled exactly — confirmed
□ Label "Higher venous: return-side obstruction" present and spelled exactly — confirmed
□ Label "A dislodged needle may not alarm" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 7 — Protective Systems and Alarm Testing

### BIOMED-07-H — Module hero

**File:** `images/dialysis-biomedical-technician-07-protective-systems-alarm-testing-vignette-hero.png` · **Alt:** A technician observing the venous clamp on a machine front during a test with a training tubing set.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician observing the venous clamp on a machine front during a test with a training tubing set.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician observing the venous clamp on a machine front during a test with a training tubing set." — confirmed
```

### BIOMED-07-A ★ — The air protection chain

**File:** `images/dialysis-biomedical-technician-07-air-chain.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `air`

**Job:** U: follows sense, stop, clamp, alarm.

**Alt:** Air detector, blood pump stop, venous clamp, and alarm as a linked chain.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The air protection chain · academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `air`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Venous chamber, ultrasonic air detector below it, venous clamp, blood pump. Four linked steps.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: follows sense, stop, clamp, alarm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Ultrasonic air detector
  • Blood pump stops
  • Venous clamp closes
  • Alarm
  • Tubing must be seated correctly
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No patient
✗ no air volume figures
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Ultrasonic air detector" present and spelled exactly — confirmed
□ Label "Blood pump stops" present and spelled exactly — confirmed
□ Label "Venous clamp closes" present and spelled exactly — confirmed
□ Label "Alarm" present and spelled exactly — confirmed
□ Label "Tubing must be seated correctly" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-07-B ★ — The blood leak detector

**File:** `images/dialysis-biomedical-technician-07-blood-leak-detector.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `leak`

**Job:** U: understands optical detection in used dialysate.

**Alt:** Optical blood leak detector on the used dialysate line.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The blood leak detector · academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `leak`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Cutaway of the used-dialysate line passing between a light source and a photodetector; a broken fiber in the dialyzer inset releasing blood into dialysate; dirty window as a failure cause.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands optical detection in used dialysate.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Light source
  • Photodetector
  • Used dialysate
  • Blood absorbs light
  • Broken fiber
  • Dirty window: false or missed alarms
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No sensitivity values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Light source" present and spelled exactly — confirmed
□ Label "Photodetector" present and spelled exactly — confirmed
□ Label "Used dialysate" present and spelled exactly — confirmed
□ Label "Blood absorbs light" present and spelled exactly — confirmed
□ Label "Broken fiber" present and spelled exactly — confirmed
□ Label "Dirty window: false or missed alarms" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-07-C ○ — Sense, act, tell

**File:** `images/dialysis-biomedical-technician-07-sense-act-tell.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `testing`

**Job:** A: tests every protective system against three questions.

**Alt:** Three questions for testing any protective system.

```text
Reference card · 1672 × 941, 16:9 landscape · Sense, act, tell · academy/dialysis-biomedical-technician-07-protective-systems-alarm-testing.html, section `testing`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three tiles: does it sense, does it act, does it tell. Banner: never bypass a protective system.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: tests every protective system against three questions.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Does it sense?
  • Does it act?
  • Does it tell?
  • Test by the manual
  • Never bypass a protective system
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No jumper wires shown
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Does it sense?" present and spelled exactly — confirmed
□ Label "Does it act?" present and spelled exactly — confirmed
□ Label "Does it tell?" present and spelled exactly — confirmed
□ Label "Test by the manual" present and spelled exactly — confirmed
□ Label "Never bypass a protective system" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 8 — The Preventive Maintenance Program

### BIOMED-08-H — Module hero

**File:** `images/dialysis-biomedical-technician-08-preventive-maintenance-program-vignette-hero.png` · **Alt:** A technician marking a wall planner of machine maintenance visits.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician marking a wall planner of machine maintenance visits.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician marking a wall planner of machine maintenance visits." — confirmed
```

### BIOMED-08-A ★ — From manual to calendar

**File:** `images/dialysis-biomedical-technician-08-pm-calendar.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

**Job:** A: turns the manufacturer's schedule into a staggered calendar.

**Alt:** Six steps from the service manual to a maintenance calendar.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · From manual to calendar · academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps: list every machine; read the schedule; spread the visits; stock kits; do and record; review overdue.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: turns the manufacturer's schedule into a staggered calendar.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • List every machine
  • Read the schedule
  • Spread the visits
  • Stock the kits
  • Do and record
  • Review what is overdue
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No interval numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "List every machine" present and spelled exactly — confirmed
□ Label "Read the schedule" present and spelled exactly — confirmed
□ Label "Spread the visits" present and spelled exactly — confirmed
□ Label "Stock the kits" present and spelled exactly — confirmed
□ Label "Do and record" present and spelled exactly — confirmed
□ Label "Review what is overdue" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-08-B ★ — A staggered year

**File:** `images/dialysis-biomedical-technician-08-staggered-year.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

**Job:** U: sees visits spread so few machines are out at once.

**Alt:** Year grid showing staggered maintenance visits for twelve machines.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · A staggered year · academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Twelve-month grid for twelve generic machines with two markers per machine, evenly spread; one overdue marker in red.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees visits spread so few machines are out at once.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Machines 1 to 12
  • Months
  • Scheduled visit
  • Done
  • Overdue: report it
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No calendar year
✗ no dates
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Machines 1 to 12" present and spelled exactly — confirmed
□ Label "Months" present and spelled exactly — confirmed
□ Label "Scheduled visit" present and spelled exactly — confirmed
□ Label "Done" present and spelled exactly — confirmed
□ Label "Overdue: report it" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-08-C ○ — What is in a maintenance kit

**File:** `images/dialysis-biomedical-technician-08-pm-kit.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

**Job:** U: recognizes typical wearing parts.

**Alt:** Typical contents of a preventive maintenance kit.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What is in a maintenance kit · academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Flat lay of generic parts on a mat: seals and O-rings, filters, valve membranes, tubing segments, checklist.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: recognizes typical wearing parts.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Seals and O-rings
  • Filters
  • Valve membranes
  • Tubing
  • Checklist
  • Approved parts only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No part numbers
✗ no brand packaging
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Seals and O-rings" present and spelled exactly — confirmed
□ Label "Filters" present and spelled exactly — confirmed
□ Label "Valve membranes" present and spelled exactly — confirmed
□ Label "Tubing" present and spelled exactly — confirmed
□ Label "Checklist" present and spelled exactly — confirmed
□ Label "Approved parts only" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 9 — Calibration and Test Equipment

### BIOMED-09-H — Module hero

**File:** `images/dialysis-biomedical-technician-09-calibration-test-equipment-vignette-hero.png` · **Alt:** A technician comparing a handheld reference meter reading with a machine display.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician comparing a handheld reference meter reading with a machine display.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician comparing a handheld reference meter reading with a machine display." — confirmed
```

### BIOMED-09-A ★ — Calibrating one parameter

**File:** `images/dialysis-biomedical-technician-09-calibration-steps.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `calibration`

**Job:** A: follows the six calibration steps.

**Alt:** Six steps of calibrating one parameter.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Calibrating one parameter · academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `calibration`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps: stabilize; measure as found; compare with tolerance; adjust; measure as left; record with the instrument's identity.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: follows the six calibration steps.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Stabilize
  • Measure as found
  • Compare with tolerance
  • Adjust
  • Measure as left
  • Record
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No tolerance values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Stabilize" present and spelled exactly — confirmed
□ Label "Measure as found" present and spelled exactly — confirmed
□ Label "Compare with tolerance" present and spelled exactly — confirmed
□ Label "Adjust" present and spelled exactly — confirmed
□ Label "Measure as left" present and spelled exactly — confirmed
□ Label "Record" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-09-B ★ — Who checks the checker

**File:** `images/dialysis-biomedical-technician-09-traceability-chain.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `reference`

**Job:** U: understands traceability.

**Alt:** Chain linking a machine sensor to a national standard through calibrated references.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Who checks the checker · academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `reference`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Chain of four links: machine sensor, facility reference meter, accredited laboratory standard, national standard. Each link has a certificate icon.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands traceability.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Machine sensor
  • Reference meter
  • Accredited laboratory
  • National standard
  • Each link has a certificate
  • A wrong reference makes every machine wrong
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No agency logos
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Machine sensor" present and spelled exactly — confirmed
□ Label "Reference meter" present and spelled exactly — confirmed
□ Label "Accredited laboratory" present and spelled exactly — confirmed
□ Label "National standard" present and spelled exactly — confirmed
□ Label "Each link has a certificate" present and spelled exactly — confirmed
□ Label "A wrong reference makes every machine wrong" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-09-C ○ — Five things calibrated

**File:** `images/dialysis-biomedical-technician-09-calibrated-parameters.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `calibration`

**Job:** U: lists the parameters and why each matters.

**Alt:** Five calibrated parameters with the consequence of each being wrong.

```text
Reference card · 1672 × 941, 16:9 landscape · Five things calibrated · academy/dialysis-biomedical-technician-09-calibration-test-equipment.html, section `calibration`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five tiles: conductivity, temperature, pressures, flows and pump speed, ultrafiltration volume, each with a one-line patient consequence.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: lists the parameters and why each matters.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Conductivity
  • Temperature
  • Pressures
  • Flows
  • Ultrafiltration volume
  • Wrong salts
  • Chilling or cell damage
  • Missed alarms
  • Less cleaning
  • Wrong fluid removal
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Conductivity" present and spelled exactly — confirmed
□ Label "Temperature" present and spelled exactly — confirmed
□ Label "Pressures" present and spelled exactly — confirmed
□ Label "Flows" present and spelled exactly — confirmed
□ Label "Ultrafiltration volume" present and spelled exactly — confirmed
□ Label "Wrong salts" present and spelled exactly — confirmed
□ Label "Chilling or cell damage" present and spelled exactly — confirmed
□ Label "Missed alarms" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 10 — Disinfection, Descaling, and Machine Fluid Hygiene

### BIOMED-10-H — Module hero

**File:** `images/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene-vignette-hero.png` · **Alt:** A technician reading a residual test strip against its color chart beside a machine.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician reading a residual test strip against its color chart beside a machine.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician reading a residual test strip against its color chart beside a machine." — confirmed
```

### BIOMED-10-A ★ — Three deposits, three answers

**File:** `images/dialysis-biomedical-technician-10-deposits.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `why`

**Job:** U: matches scale, organic film, and biofilm to the agent that removes each.

**Alt:** Three kinds of deposit inside a machine and what removes each.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Three deposits, three answers · academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `why`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three pipe cross-sections: chalky scale (acid descaler); protein and fat film (bleach or peracetic acid by the manual); biofilm (disinfection). Warning strip: bleach and acid never together.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: matches scale, organic film, and biofilm to the agent that removes each.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Scale
  • Organic film
  • Biofilm
  • Acid descales
  • Bleach cleans and disinfects
  • Heat disinfects
  • Never mix bleach and acid
  • Use approved agents only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No concentrations
✗ no brands
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Scale" present and spelled exactly — confirmed
□ Label "Organic film" present and spelled exactly — confirmed
□ Label "Biofilm" present and spelled exactly — confirmed
□ Label "Acid descales" present and spelled exactly — confirmed
□ Label "Bleach cleans and disinfects" present and spelled exactly — confirmed
□ Label "Heat disinfects" present and spelled exactly — confirmed
□ Label "Never mix bleach and acid" present and spelled exactly — confirmed
□ Label "Use approved agents only" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-10-B ★ — A disinfection cycle with proof

**File:** `images/dialysis-biomedical-technician-10-machine-disinfection.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `programs`

**Job:** A: completes the cycle and proves the rinse.

**Alt:** Five-step machine disinfection cycle ending with a negative residual test.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · A disinfection cycle with proof · academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `programs`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps: draw in the agent; circulate and dwell; rinse; residual test at the stated outlet; record.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: completes the cycle and proves the rinse.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Draw in
  • Circulate and dwell
  • Rinse
  • Residual test: negative
  • Record
  • No strips, no treatment
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Draw in" present and spelled exactly — confirmed
□ Label "Circulate and dwell" present and spelled exactly — confirmed
□ Label "Rinse" present and spelled exactly — confirmed
□ Label "Residual test: negative" present and spelled exactly — confirmed
□ Label "Record" present and spelled exactly — confirmed
□ Label "No strips, no treatment" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-10-C ○ — The filter at the machine

**File:** `images/dialysis-biomedical-technician-10-machine-filter.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `programs`

**Job:** U: locates the endotoxin-retentive filter and knows it has a life.

**Alt:** Endotoxin-retentive filter on a dialysis machine with a replacement tag.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The filter at the machine · academy/dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene.html, section `programs`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine; no manufacturer shapes, logos, or model names. Rear view with the dialysate filter housing highlighted; tag showing 'installed' and 'replace by' as blank fields.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: locates the endotoxin-retentive filter and knows it has a life.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Dialysate filter
  • Retains bacteria and endotoxin
  • Installed: ___
  • Replace by: ___
  • Replace on schedule
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No dates
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Dialysate filter" present and spelled exactly — confirmed
□ Label "Retains bacteria and endotoxin" present and spelled exactly — confirmed
□ Label "Installed: ___" present and spelled exactly — confirmed
□ Label "Replace by: ___" present and spelled exactly — confirmed
□ Label "Replace on schedule" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 11 — Electrical Safety Testing and Facility Utilities

### BIOMED-11-H — Module hero

**File:** `images/dialysis-biomedical-technician-11-electrical-safety-facility-utilities-vignette-hero.png` · **Alt:** A technician connecting an electrical safety analyzer to a machine's power cord on a bench.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician connecting an electrical safety analyzer to a machine's power cord on a bench.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician connecting an electrical safety analyzer to a machine's power cord on a bench." — confirmed
```

### BIOMED-11-A ★ — Protective earth: the path that saves

**File:** `images/dialysis-biomedical-technician-11-earth-path.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `electrical`

**Job:** U: sees fault current leaving by the earth wire.

**Alt:** Fault current with an intact protective earth compared with a broken earth.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Protective earth: the path that saves · academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `electrical`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two panels: intact earth (fault current flows down the earth wire, fuse opens, case safe); broken earth (case becomes live, current path through a person shown only as a dashed line to a generic figure's hand).
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees fault current leaving by the earth wire.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Fault inside the machine
  • Earth wire carries the current
  • Fuse opens
  • Broken earth: case becomes live
  • Test the earth path on schedule
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No injury imagery
✗ no voltage or current values
✗ no patient
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Fault inside the machine" present and spelled exactly — confirmed
□ Label "Earth wire carries the current" present and spelled exactly — confirmed
□ Label "Fuse opens" present and spelled exactly — confirmed
□ Label "Broken earth: case becomes live" present and spelled exactly — confirmed
□ Label "Test the earth path on schedule" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-11-B ★ — An electrical safety test

**File:** `images/dialysis-biomedical-technician-11-safety-test.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `electrical`

**Job:** A: performs the test sequence.

**Alt:** Five-step electrical safety test.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · An electrical safety test · academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `electrical`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps with a generic analyzer: inspect plug, cord, case; measure protective earth resistance; measure leakage current; function check; record with limits and analyzer identity. The 0.3 ohm limit from the lesson appears once.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: performs the test sequence.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Inspect
  • Protective earth resistance: limit 0.3 ohm with a detachable cord
  • Leakage current: limits from the standard and manual
  • Function check
  • Record
  • Fail = out of service
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No leakage current numbers
✗ no brand analyzer
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Inspect" present and spelled exactly — confirmed
□ Label "Protective earth resistance: limit 0.3 ohm with a detachable cord" present and spelled exactly — confirmed
□ Label "Leakage current: limits from the standard and manual" present and spelled exactly — confirmed
□ Label "Function check" present and spelled exactly — confirmed
□ Label "Record" present and spelled exactly — confirmed
□ Label "Fail = out of service" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-11-C ○ — Utilities at the station

**File:** `images/dialysis-biomedical-technician-11-station-utilities.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `utilities`

**Job:** U: names the utilities each station needs.

**Alt:** Station wall showing power, water, drain, and concentrate connections.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Utilities at the station · academy/dialysis-biomedical-technician-11-electrical-safety-facility-utilities.html, section `utilities`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Wall behind a dialysis chair: grounded power outlet, treated water outlet, drain with an air gap, concentrate outlets if central; a tag 'outlet grounding verified'.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: names the utilities each station needs.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Grounded outlet
  • Treated water
  • Drain with air gap
  • Concentrate outlets
  • Backup power: know what it supplies
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No extension cords
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Grounded outlet" present and spelled exactly — confirmed
□ Label "Treated water" present and spelled exactly — confirmed
□ Label "Drain with air gap" present and spelled exactly — confirmed
□ Label "Concentrate outlets" present and spelled exactly — confirmed
□ Label "Backup power: know what it supplies" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 12 — Troubleshooting, Life Cycle, and Capstone

### BIOMED-12-H — Module hero

**File:** `images/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone-vignette-hero.png` · **Alt:** A technician and a charge nurse signing a return-to-service form beside a machine.

```text
Circular vignette hero · 2048 × 2048, 1:1 · module page academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, hero

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: A technician and a charge nurse signing a return-to-service form beside a machine.
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "A technician and a charge nurse signing a return-to-service form beside a machine." — confirmed
```

### BIOMED-12-A ★ — A method for any fault

**File:** `images/dialysis-biomedical-technician-12-fault-method.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `method`

**Job:** A: applies the seven-step method.

**Alt:** Seven-step fault-finding method.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · A method for any fault · academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `method`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Seven steps: gather; reproduce; simple things first; divide; test one idea; repair; verify and release.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: applies the seven-step method.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Gather
  • Reproduce
  • Simple things first
  • Divide
  • Test one idea
  • Repair
  • Verify and release
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No fault codes
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Gather" present and spelled exactly — confirmed
□ Label "Reproduce" present and spelled exactly — confirmed
□ Label "Simple things first" present and spelled exactly — confirmed
□ Label "Divide" present and spelled exactly — confirmed
□ Label "Test one idea" present and spelled exactly — confirmed
□ Label "Repair" present and spelled exactly — confirmed
□ Label "Verify and release" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-12-B ★ — One machine or several

**File:** `images/dialysis-biomedical-technician-12-shared-causes.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `method`

**Job:** A: looks for a shared cause when several machines alarm.

**Alt:** Several machines alarming on one shared concentrate line.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · One machine or several · academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `method`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Row of machines fed by shared water, concentrate, and power lines; three alarming machines share one concentrate branch, highlighted.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: looks for a shared cause when several machines alarm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Shared water
  • Shared concentrate
  • Shared power
  • Several alarms at once: check what they share
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No sensor replacement shown
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Shared water" present and spelled exactly — confirmed
□ Label "Shared concentrate" present and spelled exactly — confirmed
□ Label "Shared power" present and spelled exactly — confirmed
□ Label "Several alarms at once: check what they share" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### BIOMED-12-C ○ — The life of a machine

**File:** `images/dialysis-biomedical-technician-12-machine-life-cycle.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `records`

**Job:** U: sees the records from acceptance to retirement.

**Alt:** Timeline of a dialysis machine from acceptance to retirement.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The life of a machine · academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `records`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Timeline: selection, installation and acceptance tests, routine use, maintenance and repairs, safety notices, retirement decision.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees the records from acceptance to retirement.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Acceptance tests
  • In service
  • Maintenance and repairs
  • Safety notices
  • Retirement
  • One file for the whole life
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No years
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Acceptance tests" present and spelled exactly — confirmed
□ Label "In service" present and spelled exactly — confirmed
□ Label "Maintenance and repairs" present and spelled exactly — confirmed
□ Label "Safety notices" present and spelled exactly — confirmed
□ Label "Retirement" present and spelled exactly — confirmed
□ Label "One file for the whole life" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```
