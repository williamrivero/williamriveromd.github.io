# Dialysis Nurse Assistant / PCA · Image plan blueprint

Renal Care Academy → Nephrology Nursing Track → By Role → Dialysis Nurse Assistant / Patient Care Assistant (PCA). Prepared 25 November 2026 to accompany Blueprint v2.

## Aim

Every image must help a supervised assistant do one of three things better:

- **Understand** the reason behind a task: a mechanism the learner can redraw from memory (what the dialyzer does, how unseen blood travels, why the alarm may stay quiet, why standing after dialysis makes people dizzy, why the scale decides the fluid goal).
- **Apply** the task correctly: a step sequence, an algorithm, a technique strip, a worked example with the same numbers as the text and the toolkit, or a one-glance reference card.
- **Appreciate** why it matters: the evidence made visible (skill mix, staff CPR, label errors), and the dignity and skill of the work.

Readers are new to clinical work, often on a phone, often between patients. So: one idea per image, short labels, real objects rather than abstractions, Filipino people in Philippine units, numbers only where the module text already states them, and the semi-photorealistic renalcarematters.com house style instead of flat clip art.

## Skills used

| Skill | Used for |
|---|---|
| williamriveromd-hero-vignette (v3) | 13 circular heroes (course home + 12 modules); module tiles and share images are cut from them |
| williamriveromd-simple-figure (Scaffolds B–E) | comparisons, step sequences, teaching posters and reference cards |
| williamriveromd-algorithm-generator-skill | exposure response, alarm or blood, and warning-sign algorithms |
| williamriveromd-biomedical-mechanism-figure | dialyzer, blood transmission, needle dislodgement, weight as water, standing dizziness |
| williamriveromd-organ-crosstalk-sigil-graphic | kidney, heart and lungs fluid loop |
| williamriveromd-infographic-skill | instructional photo strips, the calculator OG card, the 1200 × 630 rule |
| williamriveromd-local-image-generator (Stage 2) | optional: validate this pack and stage the folders |

## Guardrails carried into every prompt

- Nobody is shown cannulating, touching needles, catheter hubs, bloodlines or machine controls, giving medicine or disconnecting a patient. Machine parts appear only with a 'never' or 'not your role' marker.
- The access arm is always uncovered and untouched in patient scenes (this is the Module 7 teaching point).
- Numbers appear only as the module states them (63.4 kg worked example, 132/74 to 104/62, 81.4%, 1 in 3,046, 21% higher odds). No generic contact times, dilutions or waste colors: those come from the unit's own labels and charts.
- The dialyzer follows the house reference anatomy: blood in and out at the end caps, dialysate in near the blood-out end and out near the blood-in end (countercurrent).
- No real patients, readable patient data, brands, logos or facility names. Light backgrounds only, Inter typeface, American English, © renalcarematters.com bottom-right on every figure.
- Heroes rotate archetype, camera and cast so no two pages share a model look; the OG art and landing tile use a third, distinct cast.

## Inventory

- **13 circular heroes** (2048 × 2048). The end-of-course check reuses the course-home hero.
- **37 in-body figures**: Algorithm 3, Comparison 6, Step sequence 6, Teaching poster 9, Reference card 5, Mechanism figure 5, Photo strip 2, Crosstalk sigil 1.
- Teaching purpose: Understand 11, Apply 21, Appreciate 5.
- **Share (OG) cards**: (1) the track card art, text-free 1536 × 1024, which `build_academy_og.py` turns into a 1200 × 630 branded card for the course home and the knowledge check; (2) the calculator card, 1200 × 630 with its title; (3) every module's share image is made from its hero by `patch_og_images.py`, so no separate prompt is needed.
- **Tiles**: (1) the Academy landing tile (By Role column), 960 × 540; (2) twelve module tiles (640 × 360) and the Related Guides thumbnails, cut automatically from the heroes; (3) the role card on the parent nursing course uses the course-home hero card (`dialysis-nurse-assistant-card.webp`).

## Figure map

| ID | Module · section | Type | Purpose | What it teaches | File |
|---|---|---|---|---|---|
| DNA01-F1 | M1 · `delegation` | Step sequence | Apply | Delegation is a loop: clarify, repeat back, do only what you are signed off for, and report to the RN, who keeps the clinical judgment. | `dialysis-nurse-assistant-01-delegation-loop.png` |
| DNA01-F2 | M1 · `refusal` | Reference card | Apply | The whole role on one card: what you do after sign-off, what you report at once, and what you never do. | `dialysis-nurse-assistant-01-role-traffic-light.png` |
| DNA01-F3 | M1 · `why` | Teaching poster | Appreciate | In a large European study, replacing one registered nurse with one assistant per 25 patients was associated with 21% higher odds of death; assistants add to nurses, never replace them. | `dialysis-nurse-assistant-01-assistants-add-not-replace.png` |
| DNA02-F1 | M2 · `how` | Mechanism figure | Understand | Inside the dialyzer, waste diffuses from blood into dialysate flowing the opposite way, and water is squeezed out by ultrafiltration; the prescription sets the amount. | `dialysis-nurse-assistant-02-inside-the-dialyzer.png` |
| DNA02-F2 | M2 · `gap` | Teaching poster | Understand | Fluid and potassium build up between sessions; the weekend gap and any missed session carry the highest risk, so missed sessions are reported the same day. | `dialysis-nurse-assistant-02-weekend-gap.png` |
| DNA02-F3 | M2 · `gap` | Crosstalk sigil | Understand | When the kidneys cannot remove fluid and potassium, the heart is strained and fluid backs up into the lungs; dialysis breaks the loop part-time. | `dialysis-nurse-assistant-02-kidney-heart-lungs-sigil.png` |
| DNA02-F4 | M2 · `paths` | Comparison | Appreciate | Hemodialysis, peritoneal dialysis, transplant and supportive care are different paths chosen with the clinical team; the assistant listens and passes questions to the RN. | `dialysis-nurse-assistant-02-four-paths.png` |
| DNA03-F1 | M3 · `permission` | Photo strip | Apply | Introduce yourself, explain the task, ask permission and protect privacy; if a patient refuses, stop, keep them safe and tell the RN. | `dialysis-nurse-assistant-03-respect-at-the-chair.png` |
| DNA03-F2 | M3 · `language` | Comparison | Understand | Professional interpreters are associated with better communication and care than relatives or untrained staff; use the unit's approved route. | `dialysis-nurse-assistant-03-interpreter-or-relative.png` |
| DNA03-F3 | M3 · `privacy` | Reference card | Apply | Privacy habits for assistants: open only what you need, move private talk away from others, no personal-phone photos, nothing identifiable in chats. | `dialysis-nurse-assistant-03-privacy-do-and-never.png` |
| DNA04-F1 | M4 · `how` | Mechanism figure | Understand | Invisible blood travels on gloves, shared items and surfaces from one station to the next; hand hygiene, fresh gloves, dedicated items and full contact time break the chain. | `dialysis-nurse-assistant-04-how-blood-travels.png` |
| DNA04-F2 | M4 · `hands` | Reference card | Apply | The five moments for hand hygiene at the dialysis chair; every glove removal is followed by hand hygiene because gloves give false confidence. | `dialysis-nurse-assistant-04-five-moments-at-the-chair.png` |
| DNA04-F3 | M4 · `exposure` | Algorithm | Apply | After a blood exposure: first aid, report immediately through the exposure route, clinician assessment and PEP decision, then a factual report. | `dialysis-nurse-assistant-04-exposure-response.png` |
| DNA05-F1 | M5 · `weight` | Teaching poster | Apply | A wheelchair weight is only true when the chair is weighed: 78.6 minus 15.2 is 63.4 kg, up 5.4 kg; report the weight and any symptom, and let the RN decide. | `dialysis-nurse-assistant-05-wheelchair-weight-worked-example.png` |
| DNA05-F2 | M5 · `weight` | Mechanism figure | Understand | Weight gained between sessions is almost all water, so a scale or tare error becomes a fluid-removal error that can drop blood pressure or leave fluid in the lungs. | `dialysis-nurse-assistant-05-why-weight-is-water.png` |
| DNA05-F3 | M5 · `vitals` | Photo strip | Apply | Accurate blood pressure needs the right cuff size, a supported seated patient, bare skin and no talking, and never the access arm. | `dialysis-nurse-assistant-05-blood-pressure-done-right.png` |
| DNA06-F1 | M6 · `supplies` | Step sequence | Apply | Every supply is checked for identity, integrity, expiry, storage and traceability; anything that fails is held and reported, never substituted. | `dialysis-nurse-assistant-06-the-supply-check.png` |
| DNA06-F2 | M6 · `machine` | Comparison | Apply | Around the machine the assistant gathers items, keeps the station ready and reports faults, but never primes, sets, connects, mixes, overrides or removes a quarantine tag. | `dialysis-nurse-assistant-06-assist-or-never.png` |
| DNA07-F1 | M7 · `model` | Mechanism figure | Understand | If the venous needle slips out, the pump can keep pushing blood out while line pressure stays high enough that the alarm may not sound; your eyes are the second safety system. | `dialysis-nurse-assistant-07-why-the-alarm-may-stay-quiet.png` |
| DNA07-F2 | M7 · `visible` | Comparison | Apply | Keep patients warm with the blanket on the body while the access arm stays uncovered and visible. | `dialysis-nurse-assistant-07-covered-or-visible.png` |
| DNA07-F3 | M7 · `types` | Reference card | Understand | Fistula, graft and catheter each need protection; the assistant watches and reports but never handles the access. | `dialysis-nurse-assistant-07-access-types.png` |
| DNA07-F4 | M7 · `alarm` | Algorithm | Apply | At an alarm or visible blood: look at the patient, call the RN (or the emergency route for major bleeding), stay with the access in view, and never touch the circuit. | `dialysis-nurse-assistant-07-alarm-or-blood.png` |
| DNA08-F1 | M8 · `why` | Algorithm | Apply | Warning signs such as chest pain, breathlessness, confusion or fainting mean call now; an unresponsive patient who is not breathing normally means the emergency call, the AED and your BLS role. | `dialysis-nurse-assistant-08-smoke-before-fire.png` |
| DNA08-F2 | M8 · `activate` | Step sequence | Apply | In an emergency the assistant calls, brings equipment, clears space, relays facts, repeats instructions and records times, and never touches medicines or the circuit. | `dialysis-nurse-assistant-08-your-role-in-a-code.png` |
| DNA08-F3 | M8 · `cpr` | Teaching poster | Appreciate | In 398 dialysis clinic arrests, staff began CPR in 81.4%, and staff CPR was associated with about three times the odds of surviving with good brain function; BLS must be learned hands-on. | `dialysis-nurse-assistant-08-staff-cpr-saves-lives.png` |
| DNA09-F1 | M9 · `model` | Mechanism figure | Understand | After fluid removal, standing pools blood in the legs and weak reflexes cannot correct it fast enough, so the brain gets less blood; sit first, stand slowly and stay close. | `dialysis-nurse-assistant-09-why-standing-makes-people-dizzy.png` |
| DNA09-F2 | M9 · `falls` | Teaching poster | Apply | A fall of at least 20 systolic or 10 diastolic within 3 minutes of standing meets the definition; seat a dizzy patient first, then report the numbers to the RN. | `dialysis-nurse-assistant-09-standing-check-worked-example.png` |
| DNA09-F3 | M9 · `departure` | Step sequence | Apply | Departure is a handover: observe, ask, report, let the RN decide readiness, then hand over to whoever takes the patient home. | `dialysis-nurse-assistant-09-departure-is-a-handover.png` |
| DNA10-F1 | M10 · `model` | Teaching poster | Understand | A disinfectant works only while the surface stays wet for the label's full contact time; rewet surfaces that dry early and never wipe dry to save time. | `dialysis-nurse-assistant-10-wet-time-is-the-dose.png` |
| DNA10-F2 | M10 · `sequence` | Teaching poster | Apply | Clean a station top to bottom from cleaner to dirtier surfaces; arm undersides, the recline lever and the cuff are the spots most often missed. | `dialysis-nurse-assistant-10-high-touch-surfaces.png` |
| DNA10-F3 | M10 · `release` | Comparison | Appreciate | External cleaning ends with 'environmental cleaning complete'; internal disinfection, water safety and release belong to authorized staff. | `dialysis-nurse-assistant-10-clean-is-not-released.png` |
| DNA11-F1 | M11 · `records` | Comparison | Apply | An honest record states what was measured, when, how and whom you told, or that it was not obtained; a number you did not take is a false record. | `dialysis-nurse-assistant-11-honest-record.png` |
| DNA11-F2 | M11 · `specimens` | Teaching poster | Appreciate | Wrong-blood-in-tube errors occurred in about 1 in 3,046 manually identified samples and about 1 in 28 samples rejected for minor label errors; never fix a label, return it. | `dialysis-nurse-assistant-11-why-label-errors-matter.png` |
| DNA11-F3 | M11 · `specimens` | Step sequence | Apply | Carry a specimen by matching it to the request, checking the seal, carrying it directly and handing it to a named receiver; never open or relabel it. | `dialysis-nurse-assistant-11-specimen-handover.png` |
| DNA12-F1 | M12 · `quality` | Teaching poster | Apply | A weekly audit of 10 de-identified entries, plotted on a run chart, shows whether a change helps; small samples need continued measurement and are never used to blame individuals. | `dialysis-nurse-assistant-12-documentation-audit-run-chart.png` |
| DNA12-F2 | M12 · `disasters` | Reference card | Apply | In outages and disasters the assistant tells the RN, stays with patients, follows the leader and passes on questions, and never disconnects, restarts or promises schedules. | `dialysis-nurse-assistant-12-your-role-in-interruptions.png` |
| DNA12-F3 | M12 · `stations` | Step sequence | Understand | The capstone has six stations covering the whole role, and every critical step must be shown without a prompt. | `dialysis-nurse-assistant-12-six-capstone-stations.png` |

## Heroes

| Page | Archetype | Camera | File |
|---|---|---|---|
| Course home | A Environmental Portrait | environmental portrait, eye level | `dialysis-nurse-assistant-vignette-hero.png` |
| Module 1 | H Clinical | over-the-shoulder from behind the nurse | `dialysis-nurse-assistant-01-role-scope-teamwork-vignette-hero.png` |
| Module 2 | J Environmental Storytelling | wide-angle, slightly elevated | `dialysis-nurse-assistant-02-kidney-care-foundations-vignette-hero.png` |
| Module 3 | A Editorial Portrait | close portrait, side profile | `dialysis-nurse-assistant-03-dignity-communication-vignette-hero.png` |
| Module 4 | I Object Hero | macro, hands only | `dialysis-nurse-assistant-04-infection-prevention-vignette-hero.png` |
| Module 5 | I Object Hero | top-down overhead | `dialysis-nurse-assistant-05-arrival-observations-weights-vignette-hero.png` |
| Module 6 | C Radial | 45-degree overhead | `dialysis-nurse-assistant-06-station-supplies-preparation-vignette-hero.png` |
| Module 7 | H Clinical | three-quarter view from the foot of the chair | `dialysis-nurse-assistant-07-access-protection-monitoring-vignette-hero.png` |
| Module 8 | J Environmental Storytelling | wide shot, low angle | `dialysis-nurse-assistant-08-deterioration-emergencies-vignette-hero.png` |
| Module 9 | A Editorial Portrait | rear three-quarter view | `dialysis-nurse-assistant-09-comfort-mobility-discharge-vignette-hero.png` |
| Module 10 | I Object Hero | side profile, macro-to-mid | `dialysis-nurse-assistant-10-cleaning-waste-environment-vignette-hero.png` |
| Module 11 | H Clinical | over-the-shoulder at a laboratory window | `dialysis-nurse-assistant-11-records-specimens-benefits-vignette-hero.png` |
| Module 12 | D Panorama | wide panorama, eye level | `dialysis-nurse-assistant-12-capstone-quality-disasters-vignette-hero.png` |

## Share cards and tiles

| Asset | Size | Made from | Where it appears |
|---|---|---|---|
| Track share card | 1200 × 630 | `images/academy/og-art/dialysis-nurse-assistant.png` via `build_academy_og.py` | Course home and knowledge check links |
| Calculator share card | 1200 × 630 | `images/calc-dialysis-nurse-assistant-toolkit-og.png` | Toolkit link previews, Latest calculators carousel |
| Module share images | ≤ 1200 wide, ≤ 300 KB | each module hero via `patch_og_images.py` | Module link previews |
| Landing tile | 960 × 540 | `dialysis-nurse-assistant-landing-tile.png` | Academy home, By Role column |
| Module tiles | 640 × 360 | each hero via `prep_assets.card()` | Course-home module grid |
| Related Guides thumbnails | auto | heroes via `generate_rg_thumbs.py` | Every Academy page's Related Guides block |

## Production workflow

1. Open GPT-IMAGE-PROMPTS.md and paste one block at a time into ChatGPT image generation.
2. Save each PNG under its exact FILE NAME into one folder.
3. Audit each image against its QUALITY CHECK and the guardrails: spelling, numbers exactly as given, no excluded task shown, the access arm visible, correct dialyzer and fistula anatomy, Filipino context, light background, attribution present. Failures go into a corrected-prompt list with the reason.
4. Run `python3 tools/dialysis_nurse_assistant/process_images.py "<folder>"`. It copies heroes and figures into `images/` with WebP twins, cuts the 640 × 360 module tiles, places the OG art and builds the track card, places the calculator card, and makes the landing tile.
5. Run `python3 generate_dialysis_nurse_assistant.py --calc --patch`, then `python3 generate_rg_thumbs.py`, `python3 patch_rg_card_thumbs.py` and `python3 patch_og_images.py`. Figures appear at the end of their sections automatically; alt text and plain-language captions are already written.
