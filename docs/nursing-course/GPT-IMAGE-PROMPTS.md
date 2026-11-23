# GPT image prompts — Nephrology Nursing & Hemodialysis course

**Site:** renalcarematters.com · **Prepared:** November 23, 2026 · **Figures:** 45 (40 core, 5 optional ○)

This file is self-contained. Each prompt in a gray block is complete on its own: paste one block into a fresh ChatGPT image chat, generate, then run the QA list under it before saving. The module heroes already exist and are not repeated here; this file adds the hub hero and the teaching figures inside the lessons.

**What the figures are for.** Every figure does at least one job, marked on its *Job* line: **U** helps the reader understand a mechanism or structure, **A** turns knowledge into a bedside decision or sequence, **P** shows why it matters to the patient, the team, or the unit.

## How to produce

1. **Generate one figure per chat.** Start a new chat for each prompt so earlier images do not bleed into the next. Ask for the canvas size given on the entry.
2. **Attach when told.** Only figure 04-D needs an attachment: `catheter-hub-connection-reference.png` (provided with this file). Attach it with the prompt.
3. **Check text first.** Image generators misspell small text more than anything else. Compare every label against the verbatim label list inside the prompt. If one word is wrong, ask ChatGPT to fix that word only, rather than regenerating.
4. **Run the QA list** under the prompt. Reject any image with an invented number, a missing or altered footer (`© renalcarematters.com`), a dark background, or wrong anatomy.
5. **Clinical review before publishing.** Entries with anything other than "none" on *Reviewer flags* need Dr. Rivero's (or the named reviewer's) check before the image goes on the site.
6. **Save** under the exact filename on the entry (PNG). Conversion to WebP, responsive sizes, and placement in the page are done at install.
7. **Production order.** Core figures first (★ in the plan), module by module; optional figures (○) last. If a dense figure keeps garbling text (H-1 and 02-A are the likeliest), say so: it can be built as an HTML figure instead.

## Standing rules (already written into every prompt)

- Light background only (#ffffff or #fafafa). Navy #0f1e2e for text; clinical teal #1a6b72 accent. Circuit figures use the locked blood-path colors: arterial red #C00000, venous blue #1F6FC0, replacement green #2E6B3E, dialysate and effluent teal #1A6B72.
- One sans-serif font, Inter. Never serif.
- Footer on every figure except the hero: `© renalcarematters.com`, bottom right, small, semi-transparent navy. The hero carries no text at all.
- American English. Short labels, every label written out verbatim in the prompt, and "render no other text".
- No number appears unless the lesson states it. No drug doses, alarm limits, contact times, or product values; figures say "per order" or "per unit protocol".

## Production checklist

| # | ID | Figure | File | Canvas | Placement | Reviewer flag |
|---|---|---|---|---|---|---|
| 1 | H-0 | Hub hero: the educator and the next generation | `nephrology-nursing-vignette-hero.png` | 2048 × 2048, 1:1 | Hub page `guides/nephrology-nursing.html`, hero circular vignette (`figure.hero-figure > .hero-vignette`) | yes |
| 2 | H-1 | Two paths through twelve modules | `nephrology-nursing-learning-paths.png` | 1792 × 1024, 16:9 | Hub page, section `paths` (Choose the path that matches your work) | yes |
| 3 | H-2 | How every module teaches | `nephrology-nursing-teaching-cycle.png` | 1792 × 1024, 16:9 | Educator page `guides/nephrology-nursing-educator.html`, section `structure` (Proposed structure). The plan's heading "How each module teaches" does not yet exist on the page; see reviewer flags. | yes |
| 4 | 01-A | The nephron, segment by segment | `nephrology-nursing-01-nephron-map.png` | 1792 × 1024, 16:9 | Module 1 page, section `nephron` (The nephron, segment by segment) | yes |
| 5 | 01-B | Two tests, two questions | `nephrology-nursing-01-two-kidney-tests.png` | 1792 × 1024, 16:9 | Module 1 page, section `tests` (Reading kidney tests without being misled); also suits `evidence` (Why two tests, not one) | — |
| 6 | 01-C | The focused renal assessment, in priority order | `nephrology-nursing-01-focused-renal-assessment.png` | 1792 × 1024, 16:9 | Module 1 page, section `bedside` (The focused renal assessment) | yes |
| 7 | 01-D ○ | Four balances the kidney keeps | `nephrology-nursing-01-four-balances.png` | 1536 × 1152, 4:3 | Module 1 page, section `balance` (Water, sodium, potassium, and acid: four balances) | yes |
| 8 | 02-A | The risk grid: how often to check | `nephrology-nursing-02-kdigo-risk-grid.png` | 1536 × 1152, 4:3 | Module 2 page, section `causes` (Cause, risk, and how often to look) | yes |
| 9 | 02-B | Six pillars that slow kidney disease | `nephrology-nursing-02-slowing-progression-pillars.png` | 1792 × 1024, 16:9 | Module 2 page, section `slowing` (The plan that slows progression, and the nursing checks for each part) | yes |
| 10 | 02-C | Staging at the desk | `nephrology-nursing-02-staging-at-the-desk.png` | 1024 × 1536, 2:3 portrait | Module 2 page, section `bedside` (Staging and reconciling at the desk) | yes |
| 11 | 03-A | When the fine-tuning fails: four disturbances | `nephrology-nursing-03-four-disturbances.png` | 1792 × 1024, 16:9 | Module 3 page, section `physiology` (Four disturbances and their causes) | yes |
| 12 | 03-B | The mineral and bone loop, with treatment entry points | `nephrology-nursing-03-mineral-bone-loop.png` | 1792 × 1024, 16:9 | Module 3 page, section `mbd-care` (Mineral and bone disorder: the treatments compared) | yes |
| 13 | 03-C | Filipino food guide: potassium, phosphate, protein | `nephrology-nursing-03-filipino-food-guide.png` | 1792 × 1024, 16:9 | Module 3 page, section `diet` (Nutrition by stage, in food terms) | yes |
| 14 | 03-D ○ | Anemia check and the iron decision | `nephrology-nursing-03-anemia-iron-decision.png` | 1024 × 1536, 2:3 portrait | Module 3 page, section `anemia-care` (Treating anemia: iron, stimulating agents, and what to watch) | yes |
| 15 | 04-A | Before, inside, or after the filter | `nephrology-nursing-04-aki-three-causes.png` | 1792 × 1024, 16:9 | Module 4, section `physiology` (Criteria and the three categories of cause); the mental model is in `model` (Before, inside, or after the filter) | yes |
| 16 | 04-B | KDIGO 2012 AKI staging card | `nephrology-nursing-04-aki-staging-card.png` | 1536 × 1152, 4:3 | Module 4, section `staging` (Staging, and who is at risk) | yes |
| 17 | 04-C | Hyperkalemia: the nurse's sequence | `nephrology-nursing-04-hyperkalemia-sequence.png` | 1024 × 1536, 2:3 portrait | Module 4, section `evidence` (What cannot wait); companion to the treatment table in `management` | yes |
| 18 | 04-D ○ | Continuous therapy circuit (CVVH) | `nephrology-nursing-04-crrt-circuit.png` | 1672 × 941, 16:9 | Module 4, section `acute-krt` (Nursing care during acute hemodialysis and continuous therapy) | yes |
| 19 | 05-A | Four roads: the pathways compared | `nephrology-nursing-05-four-roads.png` | 1792 × 1024, 16:9 | Module 5, section `compare` (The pathways compared, in the terms patients ask about); the mental model is in `model` (Four roads, one traveler) | — |
| 20 | 05-B | Preparation timeline as kidney function falls | `nephrology-nursing-05-preparation-timeline.png` | 1792 × 1024, 16:9 | Module 5, section `timing` (When treatment starts, and how far ahead to prepare) | yes |
| 21 | 05-C | Structuring the shared-decision conversation | `nephrology-nursing-05-shared-decision.png` | 1792 × 1024, 16:9 | Module 5, section `sdm` (Structuring the conversation) | yes |
| 22 | 06-A | Three transport processes | `nephrology-nursing-06-transport-processes.png` | 1792 × 1024, 16:9 | Module 6, section `physiology` (Three transport processes); analogy introduced in `model` (A tea bag and a press) | yes |
| 23 | 06-B | The hemodialysis blood circuit on an arteriovenous fistula | `nephrology-nursing-06-hd-circuit-fistula.png` | 1672 × 941, 16:9 | Module 6, section `circuit` (The blood circuit, step by step, and what each pressure means); cutaway supports `dialyzer` (Inside the dialyzer) | yes |
| 24 | 06-C | Pressure alarm first checks | `nephrology-nursing-06-pressure-alarms.png` | 1024 × 1536, 2:3 portrait | Module 6, section `circuit` (The blood circuit, step by step, and what each pressure means), beside the alarm table | yes |
| 25 | 06-D ○ | Dialysate components: what each does and what goes wrong | `nephrology-nursing-06-dialysate-components.png` | 1536 × 1152, 4:3 | Module 6, section `dialysate` (Dialysate: what each component does and what goes wrong) | yes |
| 26 | 07-A | Fistula, graft, catheter | `nephrology-nursing-07-access-types.png` | 1792 × 1024, 16:9 | Module 7, section `physiology` (Fistula, graft, catheter) | yes |
| 27 | 07-B | Look, feel, listen | `nephrology-nursing-07-look-feel-listen.png` | 1792 × 1024, 16:9 | Module 7, section `exam` (Physical examination in depth: finding the problem before it closes the access) | yes |
| 28 | 07-C | Where the needles go | `nephrology-nursing-07-cannulation-techniques.png` | 1792 × 1024, 16:9 | Module 7, section `cannulation` (Cannulation technique: where the needles go and why) | yes |
| 29 | 07-D ○ | Catheter connection and exit-site care ( optional) | `nephrology-nursing-07-catheter-care-sequence.png` | 1792 × 1024, 16:9 | Module 7, section `catheters` (Catheters in depth: care, dysfunction, and infection) | — |
| 30 | 08-A | Water treatment train | `nephrology-nursing-08-water-treatment-train.png` | 1792 × 1024, 16:9 | Module 8, section `components` (What each component does, how it fails, and what shows the failure) | yes |
| 31 | 08-B | From contaminant to bedside: the cluster rule | `nephrology-nursing-08-contaminant-syndromes.png` | 1536 × 1152, 4:3 | Module 8, section `syndromes` (From contaminant to bedside: syndromes and the cluster rule) | yes |
| 32 | 08-C | Reprocessed dialyzer: six checks before use | `nephrology-nursing-08-reprocessing-checkpoints.png` | 1792 × 1024, 16:9 | Module 8, section `disinfect-reuse` (Machine disinfection and dialyzer reprocessing) | yes |
| 33 | 09-A | One session: before, during, after | `nephrology-nursing-09-session-three-phases.png` | 1792 × 1024, 16:9 | Module 9, section `physiology` (Before, during, after) | yes |
| 34 | 09-B | Intradialytic hypotension: first response | `nephrology-nursing-09-idh-algorithm.png` | 1024 × 1536, 2:3 portrait | Module 9, section `bedside` (First actions while help is coming); cross-reference from `idh-prevention` | yes |
| 35 | 09-C | Emergencies at the chair | `nephrology-nursing-09-chairside-emergencies.png` | 1536 × 1152, 4:3 | Module 9, section `bedside` (First actions while help is coming); disequilibrium content from `predialysis` | yes |
| 36 | 10-A | The peritoneal membrane and transport type | `nephrology-nursing-10-pd-membrane.png` | 1792 × 1024, 16:9 | Module 10, section `membrane` (The membrane in depth: why the same bag behaves differently in different people) | yes |
| 37 | 10-B | The exchange: the reason behind each step | `nephrology-nursing-10-pd-exchange.png` | 1792 × 1024, 16:9 | Module 10, section `exchange` (The exchange: the reason behind each step) | yes |
| 38 | 10-C | Cloudy fluid or abdominal pain: the peritonitis pathway | `nephrology-nursing-10-peritonitis-algorithm.png` | 1024 × 1536, 2:3 portrait | Module 10, section `infection` (Infection in depth: exit site, tunnel, and peritonitis) | yes |
| 39 | 11-A | Where the new kidney sits, and what can go wrong there | `nephrology-nursing-11-transplant-anatomy.png` | 1792 × 1024, 16:9 | Module 11, section `physiology` (From referral to the first week) | yes |
| 40 | 11-B | Infection after transplant: a timeline | `nephrology-nursing-11-transplant-infection-timeline.png` | 1792 × 1024, 16:9 | Module 11, section `complications` (Complications: surgical, immune, and infectious) | yes |
| 41 | 11-C | Immunosuppressants: what to ask, what to guard against | `nephrology-nursing-11-immunosuppressant-card.png` | 1536 × 1152, 4:3 | Module 11, section `drugs` (The immunosuppressants: what to ask about and what to guard against) | yes |
| 42 | 12-A | A worked Plan–Do–Study–Act cycle | `nephrology-nursing-12-pdsa-cycle.png` | 1792 × 1024, 16:9 | Module 12, section `dashboard` (Infection surveillance, the unit dashboard, and improvement methods) | yes |
| 43 | 12-B | The unit quality dashboard | `nephrology-nursing-12-quality-dashboard.png` | 1536 × 1152, 4:3 | Module 12, section `dashboard` (Infection surveillance, the unit dashboard, and improvement methods) | — |
| 44 | 12-C | Typhoon readiness: before, during, after | `nephrology-nursing-12-typhoon-readiness.png` | 1792 × 1024, 16:9 | Module 12, section `readiness` (Disaster and disruption readiness in depth) | yes |
| 45 | 12-D | Delegation: tasks you may hand over, judgments you keep | `nephrology-nursing-12-delegation.png` | 1792 × 1024, 16:9 | Module 12, section `teamwork` (The dialysis team, delegation, and accountability) | yes |

---

# Part 1 — The image plan

Purpose: every figure must do at least one of three jobs, named on its line below:
**U** = understand (makes a mechanism or structure visible), **A** = apply (turns knowledge into a bedside decision or sequence), **P** = appreciate (shows why it matters to the patient, team, or system).

Status: 12 module heroes are already produced and installed. The hub page has no hero yet. Everything else below is new.

## Figure types and the skill that governs each

| Code | Type | Governing skill | Canvas |
|---|---|---|---|
| HERO | Circular-vignette editorial hero | williamriveromd-hero-vignette v3 | 2048 × 2048 |
| MECH | Organ → magnified unit → consequence schematic | williamriveromd-biomedical-mechanism-figure (+ Constitution v1.0 Layer A anatomy rules) | 1792 × 1024 |
| ALGO | Decision algorithm (AHA / journal style) | williamriveromd-algorithm-generator-skill | 1024 × 1536 portrait |
| SEQ | Horizontal step sequence or timeline | williamriveromd-simple-figure | 1792 × 1024 |
| COMP | Side-by-side comparison | williamriveromd-simple-figure | 1792 × 1024 |
| CARD | Reference card / grid | williamriveromd-simple-figure or williamriveromd-infographic-skill | 1536 × 1152 or 1024 × 1024 |
| CIRC | Extracorporeal circuit schematic | dialysis-circuit-schematic (locked topology) | 1672 × 941 |
| INFO | Multi-panel educational infographic | williamriveromd-infographic-skill | 1792 × 1024 |

## House rules that apply to every figure

- Light background only (#ffffff or #fafafa); navy #0f1e2e text; clinical teal #1a6b72 accent; restrained clinical colors. Blood-path colors in circuit figures follow the circuit skill (arterial red #C00000, venous blue #1F6FC0, replacement green #2E6B3E, dialysate/effluent teal #1A6B72).
- One approved sans-serif font, named in the prompt: Inter (default), Nunito Sans, IBM Plex Sans, or Manrope. Never serif.
- Footer on every figure, exactly `© renalcarematters.com`, bottom right, small, semi-transparent navy. Heroes carry no text at all, so no footer.
- American English in every label.
- Every number and threshold in a figure is copied from the module text. If the module does not state it, the figure does not show it. Doses, alarm limits, contact times, and product-specific values never appear; the figure says "per order" or "per unit protocol" instead.
- Every medical term carries a plain-English gloss where space allows (nurse audience, but patients will see the pages).
- Filenames: `images/nephrology-nursing-NN-<short-name>.png` (webp derived at install). Hub: `images/nephrology-nursing-<short-name>.png`.

## Hub and educator pages

| ID | Type | Placement | Job | What it must show |
|---|---|---|---|---|
| H-0 | HERO | Hub hero | P | A senior Filipino nurse educator mentoring two or three newer nurses of different ages and sexes at a teaching station inside a bright hemodialysis unit; machines softly blurred behind; warm, collegial, unstaged. No screens with readable text. |
| H-1 | SEQ | Hub, "Choose your path" | A | The two learner paths as two parallel lanes across 12 module tiles, using PATH_ORDER: nephrology path 01→12 in order; hemodialysis path 01, 06, 07, 08, 09, 02, 03, 04, 05, 10, 11, 12. Module tiles carry plain titles, no acronyms. Capstone (12) marked as the shared finish. |
| H-2 | CIRC-style cycle (simple figure) | Educator page, "How each module teaches" | U | The four-stage teaching cycle used in every module — mental picture → physiology → evidence → bedside — feeding the bedside frame Assess, Communicate, Teach, Escalate, then the self-check. |

## Module figures

Each module gets three core figures (★) and, where noted, one optional figure (○). Placement is the section id in the module page.

### Module 1 — Kidney function and renal assessment
| ID | Type | Section | Job | Content |
|---|---|---|---|---|
| 01-A ★ | MECH | nephron | U | Standalone enlarged nephron (glomerulus, proximal tubule, loop, distal tubule, collecting duct) with what each segment reclaims or secretes and which hormone acts there, from the module's segment table; kidney orientation inset ≤12%. |
| 01-B ★ | COMP | evidence / tests | U | "Two tests, two questions": eGFR (how much filtering) beside urine albumin-to-creatinine ratio (how much leaking), with the laboratory pitfalls from the module's pitfall table shown as small caution tags. |
| 01-C ★ | SEQ | bedside | A | The focused renal assessment as a sequence: history → fluid status (weight, edema, lungs, orthostatic pressure) → urine → medicines → laboratory review → escalate. |
| 01-D ○ | CARD | balance | U | The four balances (water, sodium, potassium, acid): what the kidney controls, what goes wrong, the bedside sign. |

### Module 2 — CKD identification and staging
| 02-A ★ | CARD | causes | U/A | The KDIGO risk grid (G categories × A categories) with color bands and monitoring frequency per year, copied cell by cell from the module's risk-grid table. |
| 02-B ★ | INFO | slowing | A | The progression-slowing plan as pillars (blood pressure, renin–angiotensin inhibitor, SGLT2 inhibitor, statin, diet and sodium, avoiding nephrotoxins), each with its one nursing check. |
| 02-C ★ | ALGO | bedside | A | Staging at the desk: two results ≥3 months apart → assign G and A → read risk and monitoring frequency → reconcile medicines → referral trigger (kidney failure risk thresholds from module). |

### Module 3 — CKD complications, nutrition, medicines
| 03-A ★ | MECH | physiology | U | Falling nephron mass → four disturbances (anemia, mineral and bone disorder, acidosis, potassium and fluid) → organ consequences (heart, bone, vessels, muscle). |
| 03-B ★ | MECH | mbd-care | U | Mineral and bone loop: phosphate retention, FGF-23 rise, active vitamin D fall, PTH rise, bone and vascular consequences; treatment entry points marked. |
| 03-C ★ | INFO | diet | A/P | Filipino food guide for potassium and phosphate: higher choices and swaps, using only foods named in the module; protein message per stage. |
| 03-D ○ | ALGO | anemia-care | A | Anemia evaluation and iron decision using only module thresholds (withhold when ferritin >700 ng/mL or TSAT ≥40%; suspend during active infection). |

### Module 4 — AKI and acute kidney support
| 04-A ★ | MECH | model / physiology | U | "Before, inside, after the filter": prerenal, intrinsic, postrenal causes on one kidney-and-tract schematic with typical examples. |
| 04-B ★ | CARD | staging | A | KDIGO 2012 AKI staging card: creatinine and urine-output criteria for stages 1–3, copied from the module. |
| 04-C ★ | ALGO | evidence | A | Hyperkalemia — the nurse's sequence: recognize (level, ECG) → continuous monitoring → immediate call → prepare ordered treatments (stabilize, shift, remove) → recheck. Severity grid from the module. |
| 04-D ○ | CIRC | acute-krt | U | Continuous therapy circuit (CVVH default per the circuit skill). |

### Module 5 — Kidney failure treatment choices
| 05-A ★ | COMP | compare | U/P | Four roads: in-center hemodialysis, home peritoneal dialysis, transplantation, conservative kidney management — where, how often, what it replaces, what daily life looks like. |
| 05-B ★ | SEQ | timing | A | Preparation timeline as kidney function falls: education, access planning, transplant referral window, start decision — milestones from the module only. |
| 05-C ★ | SEQ | sdm | A | The structure of the shared-decision conversation from the module (elicit values → explain options → deliberate → decide and document). |

### Module 6 — HD principles, prescription, adequacy
| 06-A ★ | MECH | physiology | U | Three transport processes: diffusion, convection, ultrafiltration — paired with the tea-bag-and-press analogy and walked back to the membrane. |
| 06-B ★ | CIRC | circuit | U | Chronic hemodialysis circuit (IHD, diffusive, countercurrent) on an arteriovenous fistula: arterial needle → arterial pressure (negative) → blood pump → heparin line → dialyzer → venous chamber and pressure → air detector → venous needle. |
| 06-C ★ | ALGO | circuit | A | Pressure alarm first checks: arterial too negative, venous high, venous low (may not alarm on needle dislodgement), transmembrane pressure high — first look, then escalate. |
| 06-D ○ | CARD | dialysate | U | Dialysate components dial: sodium, potassium, calcium, bicarbonate, magnesium, glucose, temperature — risk if too high or too low; calcium range as stated in the module. |

### Module 7 — Vascular access and infection prevention
| 07-A ★ | COMP | physiology | U/P | Fistula, graft, catheter side by side: anatomy, maturation, infection risk, lifespan — Constitution AV fistula rules apply. |
| 07-B ★ | INFO | exam | A | Look–Feel–Listen: normal findings and warning findings (outflow narrowing, inflow problem, steal, infection, aneurysm with thin shiny skin) with the action for each. |
| 07-C ★ | COMP | cannulation | A | Rope-ladder vs area puncture vs buttonhole; needle direction relative to flow; keeping needles apart. |
| 07-D ○ | SEQ | catheters | A | Catheter connection and exit-site care as a clean-technique sequence (no products or times). |

### Module 8 — Equipment, water, dialysate safety
| 08-A ★ | INFO | physiology / components | U | Water treatment train from source to machine with each component's job, failure mode, and the monitor that shows failure; carbon sampling point per unit policy. |
| 08-B ★ | CARD | syndromes | A | Contaminant → syndrome map with the cluster rule at center ("two patients, same shift, same symptom: stop and investigate together"). |
| 08-C ★ | SEQ | disinfect-reuse | A | Dialyzer reprocessing safety checkpoints: label, two-person identity check, volume and leak tests, germicide present, germicide absent before priming. |

### Module 9 — HD session and complication response
| 09-A ★ | SEQ | physiology | A | The session in three phases (before, during, after) with the nursing checkpoints and "call before starting" triggers from the module. |
| 09-B ★ | ALGO | bedside / idh-prevention | A | Intradialytic hypotension: recognize → position and reduce fluid removal per protocol → notify → find the cause; prevention strategies as a side panel. |
| 09-C ★ | CARD | monitoring / bedside | A | Emergencies at the chair: air embolism, hemolysis (do not return blood), disequilibrium, needle dislodgement, reaction — signs and first action. |

### Module 10 — PD and home dialysis
| 10-A ★ | MECH | membrane | U | Peritoneal membrane: capillary → interstitium → mesothelium; glucose gradient drawing water; fast versus slow transporter dwell curves (shape only, no numbers). |
| 10-B ★ | SEQ | exchange | A | The exchange: connect → drain → flush → fill → disconnect, with the reason for each step; Tenckhoff anatomy per Constitution rules. |
| 10-C ★ | ALGO | infection | A | Cloudy fluid or abdominal pain: suspect peritonitis → sample per program → notify → intraperitoneal antibiotics per protocol → follow-up; when catheter removal is discussed (module wording). |

### Module 11 — Transplantation and special populations
| 11-A ★ | MECH | physiology / periop | U | Transplant anatomy: graft in the iliac fossa, renal artery to external iliac artery, renal vein to external iliac vein, ureter to bladder with stent, native kidneys left in place. |
| 11-B ★ | SEQ | complications | A | Infection timeline after transplant: first month, months 1–6, after 6 months — typical infections per window; "fever is always reported". |
| 11-C ★ | CARD | drugs | A/P | Immunosuppressants: what each does in a phrase, what to ask about, interactions to guard (azathioprine with allopurinol or febuxostat; grapefruit and pomelo). No doses or levels. |

### Module 12 — Philippine practice, quality, capstone
| 12-A ★ | SEQ (cycle) | dashboard | A | Plan–Do–Study–Act worked example from the module, labeled "illustrative figures". |
| 12-B ★ | CARD | dashboard | P | Unit quality dashboard domains with example measures; no targets. |
| 12-C ★ | SEQ | readiness | A/P | Typhoon readiness: before, during, after — patient list, early dialysis when ordered, backup unit, water recommissioning, accounting for every patient. |
| 12-D ○ | COMP | teamwork | A | Delegation: what a registered nurse may delegate and what stays with the nurse (assessment, decision to start, response). |

Totals: 2 hub figures + 1 educator figure + 36 core module figures + 6 optional.


---

# Part 2 — Production prompts

## Hub and educator pages

### H-0 — Hub hero: the educator and the next generation
- **File:** images/nephrology-nursing-vignette-hero.png
- **Placement:** Hub page `guides/nephrology-nursing.html`, hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees that the course carries forward bedside know-how from experienced nurses to new ones.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** Senior Filipino nurse educator explains an unconnected dialyzer to two newer nurses inside a bright hemodialysis unit.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** IMAGE-PLAN.md H-0; docs/nursing-course/GPT-IMAGE-BRIEF.md (art direction, casts and cameras of the 12 module heroes, so this one does not repeat them). No clinical values.
- **Reviewer flags:** Confirm the cast does not look like any of the 12 module-hero casts (Module 9 already uses a trio around a mannequin; Module 12 a standing huddle; Module 6 a woman in her 50s at a machine). Confirm the dialyzer and lines are dry and unconnected.

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: A (Editorial Portrait): one large subject plus two supporting people. Camera: eye-level medium shot across a small teaching table, the educator turned three-quarters toward the camera, the two learners in partial profile. Shallow depth of field.

SCENE
A senior Filipino nurse educator teaches two newer nurses at a small teaching station inside a bright, modern Philippine hemodialysis unit. He holds a clean, dry, unconnected dialyzer cartridge (a plain white cylinder with no printing) in both hands, tilted toward the learners, and is explaining it with a calm, warm expression. A neatly coiled, empty, unconnected bloodline lies on the table beside a closed binder. The two learners lean in, attentive and relaxed: one is mid-question with an open hand, the other is writing in a small notebook. The mood is collegial and unstaged: a real moment of teaching, not a posed group photo.

CAST (unique to this image; must not resemble any other image in the series)
- Educator (hero subject): man, late 50s, lean build, salt-and-pepper hair cut short and combed back, neat gray mustache, warm brown skin, deep smile lines, white nurse tunic with teal piping at the collar, plain wristwatch, no other jewelry.
- Learner 1: woman, early 20s, petite, wearing a plain light-gray hijab and soft lavender scrubs, round face, wide-set eyes, holding the notebook.
- Learner 2: man, late 30s (a career-shift nurse), tall and broad-shouldered, buzz-cut black hair, darker brown skin, olive-green scrubs, sleeves to the elbow, one hand raised mid-question.
Hair tied back or short; closed shoes; no logos on clothing.

SETTING
Hemodialysis treatment floor in soft background blur: a row of generic, unbranded dialysis machines and reclining treatment chairs, softly out of focus, chairs empty. Daylight from tall windows, pale walls, a potted plant. Machine screens are dark or a soft indistinct glow with nothing readable.

VISUAL HIERARCHY
The educator and the dialyzer in his hands occupy 60–70% of the circle, positioned right of center. The two learners and the blurred unit form 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft-focus pale wall and window light, with no faces, hands, equipment, or objects in it.

STYLE
Bright, airy, natural daylight; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; matches a set of calm documentary nursing images. Correct hands with five fingers; plausible equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, readable screen, readable binder, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No readable monitors, machine screens, charts, binders, or name badges
✗ No patient connected to a machine, no blood in any line, no needles, no cannulation
✗ No training mannequin and no simulated emergency (another image in the series already shows this)
✗ No standing huddle in a half-circle; no group posed facing the camera
✗ No dark, moody, charcoal, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands or faces; no duplicated people
✗ No branded equipment or printed cartridge labels

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere (heroes carry no footer)
□ Educator is the clear hero subject, right of center; left 20–25% is empty soft wall or window light
□ Exactly three people: older man educator, young woman in hijab, tall man in his late 30s
□ None of the three resembles a person in the 12 module heroes (compare side by side)
□ Dialyzer is plain, dry, and unconnected; bloodline coiled and empty; no blood, needles, or patient connection
□ Machine screens dark or indistinct; nothing readable on binder, badges, or screens
□ No mannequin and no emergency scene
□ Hands have five fingers; faces natural; posture relaxed and collegial
□ Light, bright color grade consistent with the module heroes; no dark background

---

### H-1 — Two paths through twelve modules
- **File:** images/nephrology-nursing-learning-paths.png
- **Placement:** Hub page, section `paths` (Choose the path that matches your work)
- **Job:** A — the learner sees at a glance which order to study in and which modules deserve the most time on their path.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal step sequence, two lanes)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Two lanes of twelve module tiles: the Nephrology Nursing path in numerical order and the Hemodialysis Nursing path in its own order, both ending at Module 12.
- **Caption:** Both paths use the same twelve modules. The Hemodialysis Nursing path moves to the dialysis modules (6 to 9) right after Module 1, and both paths finish with the Module 12 capstone.
- **Source of truth:** common.py `PATH_ORDER` — neph: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12; hd: 01, 06, 07, 08, 09, 02, 03, 04, 05, 10, 11, 12. `MODULES` role columns — Nephrology path "core": 01, 02, 03, 04, 05, 10, 11, 12; "foundation": 06, 07, 08, 09. Hemodialysis path "core": 01, 06, 07, 08, 09, 12; "foundation": 02, 03, 04, 05, 10, 11. Path names and role labels ("Emphasized on this path", "Foundation") copied from the live hub section `paths`. Tile titles are acronym-free short forms of the `MODULES` titles.
- **Reviewer flags:** Tile titles are shortened, acronym-free versions of the official titles (for example "Chronic Kidney Disease Staging" for "CKD Identification, Staging, and Progression"); confirm the editor accepts them. 24 tile titles is a heavy text load for a generator; if garbling persists, consider an HTML version.

```text
Clean clinical education figure, landscape 1792 × 1024 px (16:9). Subject: two learner paths through the same twelve course modules, shown as two parallel horizontal lanes. Publication-grade, vector-flat infographic look, mobile-readable.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e. Accent teal #1a6b72.

TITLE (top left, bold navy, large)
"Two paths, twelve modules"

LAYOUT
Two horizontal lanes stacked one above the other, each a soft rounded band (#f3f4f6), each holding 12 small rounded square tiles in one row, connected left to right by thin navy arrows. At the far right, both lanes converge into the final tile.
Each tile shows a large module number at the top and a short title beneath in two lines at most.
Tile style: tiles marked EMPHASIZED are filled solid teal #1a6b72 with white text; tiles marked FOUNDATION are white with a thin teal outline and navy text.

TOP LANE — lane label at its left end, bold teal: "Nephrology Nursing"
Tiles in this exact order (number — title — style):
1 — Kidney Function and Assessment — EMPHASIZED
2 — Chronic Kidney Disease Staging — EMPHASIZED
3 — Kidney Disease Complications — EMPHASIZED
4 — Acute Kidney Injury — EMPHASIZED
5 — Kidney Failure Treatment Choices — EMPHASIZED
6 — Hemodialysis Principles — FOUNDATION
7 — Vascular Access and Infection — FOUNDATION
8 — Equipment, Water, and Dialysate — FOUNDATION
9 — The Hemodialysis Session — FOUNDATION
10 — Peritoneal and Home Dialysis — EMPHASIZED
11 — Transplantation — EMPHASIZED
12 — Practice, Quality, and Capstone — EMPHASIZED

BOTTOM LANE — lane label at its left end, bold teal: "Hemodialysis Nursing"
Tiles in this exact order (number — title — style):
1 — Kidney Function and Assessment — EMPHASIZED
6 — Hemodialysis Principles — EMPHASIZED
7 — Vascular Access and Infection — EMPHASIZED
8 — Equipment, Water, and Dialysate — EMPHASIZED
9 — The Hemodialysis Session — EMPHASIZED
2 — Chronic Kidney Disease Staging — FOUNDATION
3 — Kidney Disease Complications — FOUNDATION
4 — Acute Kidney Injury — FOUNDATION
5 — Kidney Failure Treatment Choices — FOUNDATION
10 — Peritoneal and Home Dialysis — FOUNDATION
11 — Transplantation — FOUNDATION
12 — Practice, Quality, and Capstone — EMPHASIZED

FINISH
The two number-12 tiles are joined by a thin teal bracket at the far right, with a small flag icon and the label "Shared finish".
Both number-1 tiles are joined by a thin teal bracket at the far left with the label "Shared start".

LEGEND (bottom left, small)
A solid teal square with the label "Emphasized on this path"; an outlined square with the label "Foundation".

FOOTER
The exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px at full size), Inter Regular, navy #0f1e2e at 70% opacity, clear of all tiles and arrows.

LABEL RULES
Labels are short on purpose. Render every label exactly as written above, letter for letter. Do not add subtitles, descriptions, dates, hours, or weeks. Do not abbreviate any title (no CKD, AKI, HD, PD).

NEGATIVE CONSTRAINTS
✗ No tile out of the order listed; the bottom lane must read 1, 6, 7, 8, 9, 2, 3, 4, 5, 10, 11, 12
✗ No missing or duplicated module numbers in either lane (each lane has exactly 12 tiles)
✗ No acronyms in tile titles
✗ No extra text, week numbers, durations, or percentages
✗ No people, photos, or 3D objects
✗ No dark, navy, or charcoal background; navy is for text only
✗ No serif, script, or decorative fonts
✗ No garbled or invented words
✗ No footer variant such as "www.renalcarematters.com" or "Renal Care Matters"
✗ No crossing or tangled arrows between lanes

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every tile title and label spelled exactly as listed
□ Top lane reads 1 through 12 in order; bottom lane reads 1, 6, 7, 8, 9, 2, 3, 4, 5, 10, 11, 12
□ Fill style matches roles: top lane outlined only at 6, 7, 8, 9; bottom lane solid only at 1, 6, 7, 8, 9, 12
□ "Shared start" and "Shared finish" brackets present
□ Legend labels read "Emphasized on this path" and "Foundation"
□ No acronyms in tile titles; no invented numbers, weeks, or hours
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif; no serif type
□ Readable at phone width when scaled to 100% of a content column

---

### H-2 — How every module teaches
- **File:** images/nephrology-nursing-teaching-cycle.png
- **Placement:** Educator page `guides/nephrology-nursing-educator.html`, section `structure` (Proposed structure). The plan's heading "How each module teaches" does not yet exist on the page; see reviewer flags.
- **Job:** U — the educator sees the fixed teaching sequence inside every module and where the case and self-check fit.
- **Governing skill:** williamriveromd-simple-figure (circular loop diagram feeding a sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Four-stage teaching cycle (mental model, physiology, evidence, bedside) feeding a nursing case framed as Assess, Communicate, Teach, Escalate, then a self-check.
- **Caption:** Every module moves from a plain-language picture to physiology, evidence, and bedside practice, then applies it in a nursing case (Assess, Communicate, Teach, Escalate) and ends with a self-check quiz with answer rationales.
- **Source of truth:** Module structure in m01.py (section tags "Intuition", "Physiology", "Evidence", "Clinical application"; nav "Mental model", "At the bedside"; case `acte` keys "Assess", "Communicate", "Teach", "Escalate"; then `quiz`). common.py `card_teaser`: "a nursing case and a self-assessment with answer rationales". common.py `SCOPE_NOTE`: practice competencies signed off by a preceptor (used for the small closing note).
- **Reviewer flags:** No section on the educator page is titled "How each module teaches"; placement in `structure` is provisional. Canvas is landscape 1792 × 1024 (the plan's type "CIRC-style cycle" has no fixed size; 1672 × 941 is reserved for circuit schematics).

```text
Clean educational systems diagram, landscape 1792 × 1024 px (16:9). Subject: the teaching sequence used in every module of a nursing course. Flat, publication-grade vector look; calm and uncluttered.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; accent teal #1a6b72.

TITLE (top left, bold navy): "How every module teaches"

LAYOUT: three zones from left to right, joined by thick teal arrows.

ZONE 1 (left 40%): A CYCLE of four rounded cards arranged clockwise on a circle, with curved teal arrows between them. Center of the circle: a small open-book line icon. Cards, clockwise from the top:
- Card 1 (top), small number badge "1": heading "Mental model"; subline "A plain-language picture"
- Card 2 (right), badge "2": heading "Physiology"; subline "Normal first, then what fails"
- Card 3 (bottom), badge "3": heading "Evidence"; subline "What the guidelines show"
- Card 4 (left), badge "4": heading "Bedside"; subline "What the nurse does"
Card fills: very light teal #eef6f7 with a teal top accent band.

ZONE 2 (center 35%): A thick teal arrow leaves card 4 and enters one larger rounded panel headed "Nursing case". Inside it, a 2 × 2 grid of four equal tiles, each with a simple line icon:
- Top left: "Assess" (stethoscope icon), tile band navy #0f1e2e
- Top right: "Communicate" (speech-bubble icon), tile band teal #1a6b72
- Bottom left: "Teach" (person-and-page icon), tile band renal green #1f7a4d
- Bottom right: "Escalate" (upward-arrow alert icon), tile band clinical red #b91c1c
Tile bodies white with navy text.

ZONE 3 (right 25%): A thick teal arrow leads to a rounded card with a checklist icon, headed "Self-check", subline "Quiz with answer rationales". Below it, a small soft-gray (#f3f4f6) note card: "Skills signed off by a preceptor".

Thin dashed teal return arrow from "Self-check" curving back over the top to card 1, labeled small: "Next module".

FOOTER
The exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px at full size), Inter Regular, navy #0f1e2e at 70% opacity, clear of all cards and arrows.

LABEL RULES
Labels are deliberately short. Render each label exactly as written, letter for letter. Complete label list: "How every module teaches", "1", "Mental model", "A plain-language picture", "2", "Physiology", "Normal first, then what fails", "3", "Evidence", "What the guidelines show", "4", "Bedside", "What the nurse does", "Nursing case", "Assess", "Communicate", "Teach", "Escalate", "Self-check", "Quiz with answer rationales", "Skills signed off by a preceptor", "Next module", "© renalcarematters.com".

NEGATIVE CONSTRAINTS
✗ No change to the order Mental model → Physiology → Evidence → Bedside
✗ No fifth stage added to the cycle; no extra tiles in the case panel
✗ No reordering of Assess, Communicate, Teach, Escalate
✗ No people, photos, or 3D renders
✗ No numbers, percentages, hours, or durations beyond the four badge numbers
✗ No dark background; navy only for text and one tile band
✗ No serif, script, or decorative fonts
✗ No garbled words or invented labels
✗ No crossing or tangled arrows
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as in the label list
□ Cycle order clockwise: Mental model, Physiology, Evidence, Bedside
□ Case panel shows exactly four tiles: Assess, Communicate, Teach, Escalate, with their assigned colors
□ "Self-check" card and the preceptor note present; dashed "Next module" return arrow present
□ No invented numbers besides badges 1 to 4
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ Arrows flow cleanly left to right with no tangles

---


---

## Module 1 — Kidney Function and Renal Assessment

### 01-A — The nephron, segment by segment
- **File:** images/nephrology-nursing-01-nephron-map.png
- **Placement:** Module 1 page, section `nephron` (The nephron, segment by segment)
- **Job:** U — the learner can point to each nephron segment and say what it reclaims or controls and which hormone acts there.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure, with Constitution v1.0 Layer A anatomy rules
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Enlarged nephron with five labeled segments showing what each reclaims or controls, aldosterone and antidiuretic hormone at the collecting duct, and a small kidney locator.
- **Caption:** Each nephron filters first, then reclaims most of what it filtered. The table on this page adds the medicines that act at each segment.
- **Source of truth:** m01_x.py `nephron` table — Glomerulus: filters plasma, holds back cells and protein. Proximal tubule: reclaims about two thirds of filtered sodium and water, nearly all glucose, amino acids, phosphate, and bicarbonate; secretes many drugs; activates vitamin D. Loop of Henle: reclaims about a quarter of filtered sodium; builds the salt gradient that lets the kidney concentrate urine. Distal convoluted tubule: fine-tunes sodium and calcium. Collecting duct: final control of sodium and potassium under aldosterone, of water under antidiuretic hormone, and of acid. "Roughly one million nephrons" per kidney. m01.py `physiology`: about 99% of filtered water and sodium reabsorbed; potassium mainly excreted by secretion in the distal nephron. m01.py `model`: three losses (filtration falls, wastes rise; reclaiming fails, salt, water, potassium, acid build; hormonal work fails, anemia and bone disease).
- **Reviewer flags:** Medicine column of the source table deliberately left out to keep labels manageable (the module flags it as orientation, not prescribing). Renin and erythropoietin are not placed on the nephron because the module does not name their segment.

```text
Publication-grade biomedical mechanism schematic, landscape 1792 × 1024 px (16:9). Subject: one human nephron shown as a standalone, enlarged diagram, with what each segment does. Review-article style (flat vector with soft semi-3D shading), white background, restrained clinical colors.

════ LAYER A: ANATOMICAL TRUTH BLOCK (overrides all style instructions) ════
- The nephron is a STANDALONE ENLARGED DIAGRAM, never drawn at organ scale inside a kidney.
- Kidney orientation inset occupies 12% of the canvas or less, top left, in a thin dashed box: coronal section, convex border LATERAL (left), hilum MEDIAL (right); outer cortex pink-brown; triangular medullary pyramids with apices (papillae) pointing INWARD toward minor calyces; calyces drain INWARD to a funnel-shaped renal pelvis that exits at the MEDIAL hilum only. A tiny box on the inset straddles cortex and medulla, joined by a dashed connector line to the enlarged nephron. Inset label: "Location in kidney".
- In the enlarged nephron, a faint horizontal band marks "Cortex" above and "Medulla" below.
- Glomerulus: a tuft of capillaries inside a cup-shaped Bowman's capsule, in the CORTEX, with a thicker afferent arteriole entering and a thinner efferent arteriole leaving at the same pole (arterioles red #c00000 with a visible muscular wall).
- Proximal tubule: coiled, in the cortex, leaving the capsule.
- Loop of Henle: descends straight into the MEDULLA, hairpin turn, ascends back to the cortex.
- Distal convoluted tubule: coiled, in the cortex, passing back close to its own glomerulus.
- Collecting duct: receives the distal tubule and runs straight DOWN through the medulla toward the papilla tip at the bottom.
- Flow arrows inside the tubule go one way only: glomerulus → proximal → loop → distal → collecting duct → urine.

════ LAYOUT AND LABELS ════
Title (top center, bold navy #0f1e2e): "The nephron, segment by segment"
Subtitle (teal #1a6b72): "About one million per kidney"

Five segments, each tinted a soft distinct color (glomerulus pale red, proximal tubule pale yellow, loop pale blue, distal tubule pale green, collecting duct pale purple), each with a numbered teal badge and a rounded callout card joined by a thin leader line. Callout text exactly:
1. "Glomerulus" — "Filters plasma" / "Holds back cells and protein"
2. "Proximal tubule" — "Reclaims two thirds of sodium, water" / "Nearly all glucose, amino acids" / "Phosphate and bicarbonate" / "Secretes many drugs" / "Activates vitamin D"
3. "Loop of Henle" — "Reclaims a quarter of sodium" / "Builds gradient to concentrate urine"
4. "Distal convoluted tubule" — "Fine-tunes sodium and calcium"
5. "Collecting duct" — "Final sodium, potassium, water, acid" / "Secretes potassium"
Hormone tags (small rounded pills, soft purple #6c3d8e outline, pointing at the collecting duct): "Aldosterone: sodium and potassium" and "Antidiuretic hormone: water"
Arrow label at the bottom of the collecting duct: "Urine"

Bottom summary strip: three rounded boxes in a row with thin arrows between, pale pink fill (#fbe9e9), navy text, heading at left "When kidneys fail":
- "Filtration falls: wastes rise"
- "Reclaiming fails: salt, water, potassium, acid build"
- "Hormones fail: anemia, bone disease"

Typography: Inter for every label; never serif. Labels are short on purpose; do not lengthen or paraphrase them.

FOOTER: the exact text "© renalcarematters.com" bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of all anatomy and labels.

════ NEGATIVE CONSTRAINTS ════
✗ No nephron drawn inside a full-size kidney; the kidney appears only as the small inset
✗ No calyces pointing outward; no renal pelvis floating in the center or on the convex border
✗ No glomerulus in the medulla; no loop of Henle staying in the cortex
✗ No collecting duct running upward or ending in the cortex
✗ No backward or two-way flow arrows in the tubule
✗ No medicine names, doses, or percentages other than those written above
✗ No renin or erythropoietin labels
✗ No extra segments (no "connecting tubule" or "macula densa" labels)
✗ No cartoon style, no dark background, no photorealism
✗ No serif fonts; no garbled text; no prompt text visible
✗ No footer missing, enlarged, recolored, or altered

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as written; no extra labels
□ Nephron is standalone and enlarged; kidney inset ≤12% of canvas with calyces draining inward and pelvis at the medial hilum
□ Glomerulus, proximal and distal tubules in the cortex; loop dips into the medulla; collecting duct descends to the papilla
□ Afferent and efferent arterioles at the same pole of Bowman's capsule
□ Flow arrows run one way to "Urine"
□ Aldosterone and antidiuretic hormone tags point to the collecting duct
□ No invented numbers (only "one million", "two thirds", "a quarter" appear)
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif; no serif type

---

### 01-B — Two tests, two questions
- **File:** images/nephrology-nursing-01-two-kidney-tests.png
- **Placement:** Module 1 page, section `tests` (Reading kidney tests without being misled); also suits `evidence` (Why two tests, not one)
- **Job:** U — the learner understands that eGFR and urine albumin answer different questions and knows what can mislead each.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, side-by-side comparison)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Side-by-side panels: estimated filtration rate measures how much the kidneys filter; urine albumin-to-creatinine ratio measures leaking, each with caution tags.
- **Caption:** Estimated glomerular filtration rate (eGFR) shows how much the kidneys filter; the urine albumin-to-creatinine ratio (ACR) shows how much albumin leaks through. Each predicts risk on its own, so a kidney check needs both.
- **Source of truth:** m01.py `evidence` — KDIGO 2024 classifies CKD by cause, GFR category, and albuminuria category; eGFR and urine ACR each predict kidney failure, cardiovascular events, and death independently; a kidney check without urine albumin is incomplete. m01.py `physiology` — eGFR calculated from serum creatinine, age, and sex; no race term. m01_x.py `tests` table — eGFR: valid only when creatinine is stable; unreliable in acute kidney injury, amputees, pregnancy, extremes of body size; cystatin C can be added. Creatinine: low in small, frail, or malnourished people; raised by large muscle mass, a cooked-meat meal, creatine supplements. Urine ACR: first-morning sample preferred; temporarily raised by fever, urinary tract infection, heavy exercise in the previous day, menstruation, uncontrolled blood sugar or heart failure; abnormal result repeated before it is acted on.
- **Reviewer flags:** none

```text
Medical education comparison figure, landscape 1792 × 1024 px (16:9), AJKD-style graphical abstract. Subject: the two core kidney tests and what can mislead each. Calm, flat vector illustration with light semi-3D icons.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; headings teal #1a6b72.

TITLE (top center, bold navy): "Two tests, two questions"

LAYOUT
Two equal rounded panels side by side, separated by a soft dashed vertical divider. A small centered teal banner bridges the divider near the top of the panels: "Each predicts risk on its own".

LEFT PANEL (fill very light teal #eef6f7)
- Heading: "eGFR: how much filtering"
- Subheading: "Estimated glomerular filtration rate"
- Central illustration: a simple stylized glomerulus (capillary tuft in a cup-shaped capsule) with fluid droplets passing through the filter into the tubule, and a small blood-tube icon labeled "Blood test".
- Small gray line: "From creatinine, age, and sex"
- Caution tags (small amber #b8860b outlined pills with a small triangle icon), exactly:
  "Needs stable creatinine"
  "Unreliable in acute kidney injury"
  "Amputation, pregnancy, extreme body size"
  "Low muscle hides loss"
  "Raised by muscle, meat, creatine"
- Teal note at the bottom: "Cystatin C can refine it"

RIGHT PANEL (fill very light warm cream #f8f5f0)
- Heading: "Urine ACR: how much leaking"
- Subheading: "Urine albumin-to-creatinine ratio"
- Central illustration: the same stylized glomerulus with a few small albumin particles slipping through a leaky barrier, and a small urine-cup icon labeled "First-morning urine".
- Caution tags (same amber style), exactly:
  "Fever"
  "Urinary infection"
  "Heavy exercise the day before"
  "Menstruation"
  "High blood sugar or heart failure"
- Teal note at the bottom: "Repeat before acting"

BOTTOM STRIP (full width, soft gray #f3f4f6, navy text): "A kidney check without urine albumin is incomplete"

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of the panels.

LABEL RULES
Short labels on purpose. Render each exactly as written. Complete label list: "Two tests, two questions", "Each predicts risk on its own", "eGFR: how much filtering", "Estimated glomerular filtration rate", "Blood test", "From creatinine, age, and sex", "Needs stable creatinine", "Unreliable in acute kidney injury", "Amputation, pregnancy, extreme body size", "Low muscle hides loss", "Raised by muscle, meat, creatine", "Cystatin C can refine it", "Urine ACR: how much leaking", "Urine albumin-to-creatinine ratio", "First-morning urine", "Fever", "Urinary infection", "Heavy exercise the day before", "Menstruation", "High blood sugar or heart failure", "Repeat before acting", "A kidney check without urine albumin is incomplete", "© renalcarematters.com".

NEGATIVE CONSTRAINTS
✗ No numeric values, cutoffs, units, or reference ranges anywhere
✗ No stage or category labels (no G1–G5, no A1–A3)
✗ No race, ethnicity, or skin-color terms
✗ No dipstick color chart (this figure is about the ratio, not the dipstick)
✗ No people or photographs
✗ No red "danger" styling on the caution tags; amber only
✗ No dark background; no serif fonts
✗ No garbled or invented words; no extra tags
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as in the label list; no extra tags
□ Left panel is about filtering (blood test); right panel about leaking (urine)
□ Five caution tags per side, amber, matching the lists
□ No numbers, units, or category labels anywhere
□ Banner "Each predicts risk on its own" bridges both panels
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ Glomerulus drawings plausible (tuft inside a capsule), identical in both panels except for the leak

---

### 01-C — The focused renal assessment, in priority order
- **File:** images/nephrology-nursing-01-focused-renal-assessment.png
- **Placement:** Module 1 page, section `bedside` (The focused renal assessment)
- **Job:** A — the learner can run the eight-step assessment in the right order and end with a judgment and action.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, step sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Eight-step renal assessment from breathing to access site, ending in three judgments: stable, needs review today, or urgent escalation now.
- **Caption:** Start with breathing, because pulmonary congestion cannot wait. Weight is the most useful single number for fluid, and the assessment is complete only when it ends in a judgment and an action.
- **Source of truth:** m01.py `bedside` table — 1 Breathing (respiratory rate, oxygen saturation, work of breathing, ability to lie flat, lung sounds; the finding that cannot wait); 2 Weight (same scale, same time of day, similar clothing; compare with the last 3 to 7 days; a gain of a kilogram or more over a few days is fluid until proven otherwise); 3 Blood pressure and pulse (standardized technique; standing pressure if dizzy); 4 Volume signs (edema of legs, sacrum, around the eyes; neck veins; mucous membranes); 5 Intake and output (urine volume, color, foaming, catheter patency; oral and intravenous intake); 6 Symptoms (nausea, poor appetite, itch, cramps, sleepiness, confusion); 7 Medicines and exposures (pain relievers, herbal products, recent contrast or antibiotics); 8 Access (fistula, graft, or catheter site). "One liter of retained water weighs one kilogram." Ends in "stable, needs review today, or needs urgent escalation now."
- **Reviewer flags:** The plan listed the order history → fluid status → urine → medicines → laboratory review → escalate. The module's own table starts with breathing and has eight steps without a laboratory step; the figure follows the module. Laboratory review is covered by 01-B.

```text
Clean clinical education step-sequence figure, landscape 1792 × 1024 px (16:9). Subject: the focused renal assessment as eight ordered steps ending in a nursing judgment. Flat vector cards with simple line icons; calm and mobile-readable.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; accents teal #1a6b72.

TITLE (top left, bold navy): "The focused renal assessment"
SUBTITLE (teal): "Most dangerous findings first"

LAYOUT
Eight rounded cards in two rows of four on a soft gray panel (#f3f4f6), read left to right, then the second row left to right, joined by bold navy arrows (a curved arrow links card 4 to card 5). Each card: a numbered circle badge, a small line icon, a bold step name, and one short detail line. Card 1 has a clinical red #b91c1c top band; cards 2 to 8 have teal top bands.

ROW 1
1. Icon lungs — "Breathing" — "Rate, saturation, lying flat, lung sounds". Small red tag on this card: "Cannot wait"
2. Icon scale — "Weight" — "Same scale, time, clothing; 3–7 days". Small teal tag: "1 liter retained = 1 kilogram"
3. Icon cuff — "Blood pressure and pulse" — "Standardized; standing if dizzy"
4. Icon leg with swelling — "Volume signs" — "Edema, neck veins, mucous membranes"

ROW 2
5. Icon urine bag — "Intake and output" — "Urine volume, color, catheter"
6. Icon person — "Symptoms" — "Nausea, itch, cramps, confusion"
7. Icon pill bottle and leaf — "Medicines and exposures" — "Pain relievers, herbals, contrast"
8. Icon forearm — "Access" — "Fistula, graft, or catheter site"

JUDGMENT (right side, spanning both rows)
A bold navy arrow from card 8 leads to a tall rounded panel headed "Judgment and action", containing three stacked pills:
- Renal green #1f7a4d pill: "Stable"
- Amber #b8860b pill: "Needs review today"
- Clinical red #b91c1c pill: "Urgent escalation now"

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, below and clear of the judgment panel.

LABEL RULES
Labels are short on purpose. Render each exactly as written. Complete label list: "The focused renal assessment", "Most dangerous findings first", "1"–"8", "Breathing", "Rate, saturation, lying flat, lung sounds", "Cannot wait", "Weight", "Same scale, time, clothing; 3–7 days", "1 liter retained = 1 kilogram", "Blood pressure and pulse", "Standardized; standing if dizzy", "Volume signs", "Edema, neck veins, mucous membranes", "Intake and output", "Urine volume, color, catheter", "Symptoms", "Nausea, itch, cramps, confusion", "Medicines and exposures", "Pain relievers, herbals, contrast", "Access", "Fistula, graft, or catheter site", "Judgment and action", "Stable", "Needs review today", "Urgent escalation now", "© renalcarematters.com".

NEGATIVE CONSTRAINTS
✗ No change to the step order; Breathing is always step 1
✗ No vital-sign values, oxygen targets, blood pressure numbers, or weight thresholds other than "3–7 days" and "1 liter retained = 1 kilogram"
✗ No laboratory step and no lab values
✗ No drug names or doses
✗ No photographs of people; icons only
✗ No needles or blood in the access icon
✗ No dark background; no serif fonts
✗ No garbled or invented words; no extra cards
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as in the label list
□ Eight cards in order 1 to 8; Breathing first with a red band and "Cannot wait" tag
□ Weight card carries "1 liter retained = 1 kilogram"
□ Judgment panel has exactly three pills in green, amber, red with the exact wording
□ No invented numbers (only 1–8, "3–7 days", "1 liter", "1 kilogram")
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ Arrows read clearly left to right, row 1 then row 2

---

### 01-D ○ — Four balances the kidney keeps
- **File:** images/nephrology-nursing-01-four-balances.png
- **Placement:** Module 1 page, section `balance` (Water, sodium, potassium, and acid: four balances)
- **Job:** U — the learner can separate sodium (volume) from water (concentration) and link each balance to a bedside clue.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference grid for water, sodium, potassium, and acid balance: what the kidney controls, what goes wrong in kidney failure, and the clue to notice.
- **Caption:** Sodium sets the volume of fluid; water sets the sodium concentration. A swollen patient can have a low serum sodium, and deep, rapid breathing with clear lungs is a reason to check bicarbonate.
- **Source of truth:** m01_x.py `balance` — sodium content determines fluid outside cells; too much appears as edema, weight gain, hypertension, not a high sodium level; serum sodium concentration reflects water balance (low = too much water, high = too little); antidiuretic hormone makes the collecting duct reabsorb water; renin–angiotensin–aldosterone system retains sodium; natriuretic peptides push sodium excretion; in kidney failure sodium is retained. Potassium: about 2% outside cells, sets the electrical stability of the heart; shifts in minutes, excretion over hours; in failure excretion is lost, patient depends on shifts and intake; missed dialysis, potassium-rich meal, constipation, stored red-cell transfusion tip the balance. Acid: kidneys remove remaining acid and rebuild bicarbonate; serum bicarbonate falls; deep, rapid breathing; check bicarbonate, not only oxygen saturation. m01_x.py `nephron`: aldosterone controls potassium at the collecting duct.
- **Reviewer flags:** The module does not name a bedside sign for water imbalance; the card shows the serum sodium level as the clue. Confirm this wording.

```text
Clinical reference card, 1536 × 1152 px (4:3). Subject: four balances the kidney maintains. Publication-grade grid, flat vector, calm and readable.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; column headers teal #1a6b72 on soft gray #f3f4f6.

TITLE (top, bold navy): "Four balances the kidney keeps"
BANNER under the title (light teal #eef6f7 strip, bold teal text): "Sodium sets volume. Water sets concentration."

GRID: 4 rows × 3 content columns, plus a row-label column at left with a simple icon per row. Alternating row fills white / very soft gray. Rounded outer corners.

Column headers exactly: "What the kidney controls" | "What goes wrong" | "What to notice"

Row 1 — icon water drop — row label "Water"
- "Sodium concentration, via antidiuretic hormone"
- "Too much water: low sodium" / "Too little water: high sodium"
- "Serum sodium level"

Row 2 — icon salt shaker — row label "Sodium"
- "Fluid volume outside cells"
- "Sodium retained in kidney failure"
- "Edema, weight gain, high blood pressure"

Row 3 — icon heart with rhythm line — row label "Potassium"
- "Excretion over hours; shifts in minutes"
- "Excretion lost; intake and shifts decide"
- "Heart rhythm at risk; check potassium"

Row 4 — icon lungs with breath arrows — row label "Acid"
- "Removes daily acid; rebuilds bicarbonate"
- "Bicarbonate falls"
- "Deep, rapid breathing; check bicarbonate"

In the "What to notice" column, the Sodium, Potassium, and Acid cells carry a small amber #b8860b dot; the Potassium cell text is clinical red #b91c1c.

BOTTOM STRIP (soft gray, navy text): "Swollen with fluid can still mean low sodium"

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of the grid.

LABEL RULES
Labels are short on purpose. Render each exactly as written, including punctuation. Do not add extra rows, numbers, or examples.

NEGATIVE CONSTRAINTS
✗ No numeric values, normal ranges, or units (no mmol/L, no percentages)
✗ No drug names or doses
✗ No statement that edema means high serum sodium
✗ No arterial blood gas values
✗ No people or photographs
✗ No dark background; no serif fonts
✗ No garbled or invented words; no fifth row
✗ No mixing of rows (each cell stays in its row)
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as written
□ Four rows in order Water, Sodium, Potassium, Acid; three columns with exact headers
□ Banner reads "Sodium sets volume. Water sets concentration."
□ Water row shows low and high sodium correctly matched (too much water: low; too little: high)
□ No numbers, units, or ranges anywhere
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ Grid readable at 4:3 on a phone

---


---

## Module 2 — Chronic Kidney Disease: Identification, Staging, and Progression

### 02-A — The risk grid: how often to check
- **File:** images/nephrology-nursing-02-kdigo-risk-grid.png
- **Placement:** Module 2 page, section `causes` (Cause, risk, and how often to look)
- **Job:** U/A — the learner reads risk and the yearly number of checks from a patient's G and A categories and spots overdue follow-up.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Color-coded grid of filtration by albuminuria categories showing risk level and suggested minimum kidney checks per year in each cell.
- **Caption:** Each cell gives the risk level and the suggested minimum number of kidney-function and albuminuria checks per year (KDIGO 2024). Sicker or less stable patients are seen more often.
- **Source of truth:** m02_x.py `causes` risk-grid table, copied cell by cell:
  - G1 and G2 (60 or higher): A1 Low risk if no other marker of damage, check yearly | A2 Moderately increased, yearly | A3 High, about 3 times a year
  - G3a (45 to 59): A1 Moderately increased, yearly | A2 High, twice a year | A3 Very high, 3 times a year
  - G3b (30 to 44): A1 High, twice a year | A2 Very high, 3 times a year | A3 Very high, 3 times a year
  - G4 (15 to 29): A1 Very high, 3 times a year | A2 Very high, 3 times a year | A3 Very high, 4 or more times a year
  - G5 (below 15): A1 Very high, 4 or more | A2 Very high, 4 or more | A3 Very high, 4 or more
  - Column headers: A1 (below 30 mg/g), A2 (30 to 300 mg/g), A3 (above 300 mg/g). "The frequencies are guides, and sicker or less stable patients are seen more often."
- **Reviewer flags:** The module names risk levels but not colors; colors follow the conventional KDIGO scheme (green, yellow, orange, red). The module merges G1 and G2 into one row; the figure does the same. The module file flags these frequencies for confirmation against KDIGO 2024 before publication. GPT-IMAGE-BRIEF.md says Module 2 tables "must stay as HTML"; this figure supplements the HTML table and should not replace it.

```text
Clinical reference card, 1536 × 1152 px (4:3). Subject: a color-coded chronic kidney disease risk grid showing risk level and how many kidney checks per year are suggested. Publication-grade, flat, highly legible table graphic.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; headers teal #1a6b72 on soft gray #f3f4f6.

TITLE (top left, bold navy): "Chronic kidney disease risk grid"
SUBTITLE (teal): "Kidney checks per year, by category"

GRID STRUCTURE
A table of 5 rows × 3 columns of colored cells, with a header row on top and a header column at left.
- Top axis title above the header row: "Albuminuria category (urine albumin-to-creatinine ratio)"
- Left axis title, rotated vertically: "Filtration category (eGFR, mL/min/1.73 m²)"
- Column headers, left to right: "A1: below 30 mg/g" | "A2: 30 to 300 mg/g" | "A3: above 300 mg/g"
- Row headers, top to bottom: "G1 and G2: 60 or higher" | "G3a: 45 to 59" | "G3b: 30 to 44" | "G4: 15 to 29" | "G5: below 15"

CELL COLORS (fill by risk level; text navy, bold risk word on line 1, frequency on line 2)
- Low = green #8fcf9f
- Moderately increased = yellow #f7e07a
- High = orange #f2a65a
- Very high = red #e06666

CELLS, EXACTLY (row by row; write line 1 / line 2):
Row G1 and G2:
- A1: green — "Low*" / "Yearly"
- A2: yellow — "Moderately increased" / "Yearly"
- A3: orange — "High" / "About 3 times a year"
Row G3a:
- A1: yellow — "Moderately increased" / "Yearly"
- A2: orange — "High" / "Twice a year"
- A3: red — "Very high" / "3 times a year"
Row G3b:
- A1: orange — "High" / "Twice a year"
- A2: red — "Very high" / "3 times a year"
- A3: red — "Very high" / "3 times a year"
Row G4:
- A1: red — "Very high" / "3 times a year"
- A2: red — "Very high" / "3 times a year"
- A3: red — "Very high" / "4 or more a year"
Row G5:
- A1: red — "Very high" / "4 or more a year"
- A2: red — "Very high" / "4 or more a year"
- A3: red — "Very high" / "4 or more a year"

That is 15 cells total: 1 green, 2 yellow, 3 orange, 9 red.

LEGEND (below the grid, one row): four small swatches with labels "Low", "Moderately increased", "High", "Very high".
FOOTNOTE (small, navy, below legend): "*Low risk if no other marker of kidney damage"
NOTE (small teal): "Sicker or less stable patients: check more often"

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of the grid and legend.

LABEL RULES
Render every label and cell exactly as written, letter for letter, in the exact cell given. Do not add, merge, or split rows. Do not add a separate G1 row and G2 row; they share one row.

NEGATIVE CONSTRAINTS
✗ No cell color or frequency different from the list above (check: 1 green, 2 yellow, 3 orange, 9 red)
✗ No separate rows for G1 and G2; exactly five rows
✗ No mg/mmol units, percentages, or extra numbers not listed
✗ No stage names such as "Stage 3"
✗ No dark-red sixth color or gradient fills
✗ No people, icons inside cells, or decorative graphics
✗ No dark background; no serif fonts
✗ No garbled or invented words
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every header, cell, and legend label spelled exactly as written
□ Five rows (G1 and G2 merged, G3a, G3b, G4, G5) and three columns (A1, A2, A3)
□ Cell-by-cell check against the source list: colors 1 green, 2 yellow, 3 orange, 9 red, in the right places
□ Frequencies match exactly, including "About 3 times a year" at G1–G2/A3 and "4 or more a year" in all three G5 cells and G4/A3
□ Axis titles and units ("mL/min/1.73 m²", "mg/g") correct
□ Footnote "*Low risk if no other marker of kidney damage" present
□ No invented numbers
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif

---

### 02-B — Six pillars that slow kidney disease
- **File:** images/nephrology-nursing-02-slowing-progression-pillars.png
- **Placement:** Module 2 page, section `slowing` (The plan that slows progression, and the nursing checks for each part)
- **Job:** A — the learner links each part of the treatment plan to the one nursing check that goes with it.
- **Governing skill:** williamriveromd-infographic-skill (multi-panel educational infographic)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Six pillars holding up kidney protection: blood pressure, renin–angiotensin inhibitor, SGLT2 inhibitor, statin, sodium, and avoiding kidney harm, each with one nursing check.
- **Caption:** Nurses rarely prescribe these treatments, but they check whether each one is in place, tolerated, and restarted after an illness. A creatinine rise of up to 30% after starting a renin–angiotensin inhibitor is expected and is reported, not a reason to stop on its own.
- **Source of truth:** m02_x.py `slowing` table — Blood pressure: systolic target below 120 mmHg when tolerated; check: measure correctly every visit, ask about dizziness and falls. Renin–angiotensin system inhibitor: highest tolerated dose; check: creatinine and potassium within 2 to 4 weeks of starting or increasing; creatinine rise up to 30% accepted. SGLT2 inhibitor: started when eGFR is 20 or higher; check: genital hygiene, prescriber's written plan for pausing during illness, report nausea, vomiting, abdominal pain. Lipids: statin for adults aged 50 and older with CKD not on dialysis; check: adherence, muscle symptoms. Sodium: less than 2 g of sodium (5 g of salt) a day; check: identify main sources (fish sauce, soy sauce, shrimp paste, bouillon cubes, instant noodles…); calamansi, vinegar, garlic, onion, ginger for flavor. m02.py `evidence` and `bedside`: NSAIDs most often implicated; ask what the patient takes for headache, joint pain, fever, or menstrual pain; flag for prescriber review; blood pressure, glucose control, and avoidance of further kidney injury complete the plan.
- **Reviewer flags:** "Highest tolerated dose" is shown as a principle, not a dose. Glucose control, protein, other diabetes agents, and activity rows from the table are left out to keep six pillars (plan scope).

```text
Patient-and-nurse education infographic, landscape 1792 × 1024 px (16:9). Subject: six treatment pillars that slow chronic kidney disease, each paired with one nursing check. Clean modular design, flat vector with light semi-3D pillar forms.

BACKGROUND AND TYPE
Off-white #fafafa canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; accents teal #1a6b72.

COMPOSITION
A classical portico: a wide teal roof slab across the top, six evenly spaced columns, and a base slab. Each column has a simple line icon near its top, a bold name, one teal "Advice" line, and below the column a white rounded card with a small clipboard icon and the "Nurse checks" line.

ROOF (white bold text on teal #1a6b72): "Slowing chronic kidney disease"
BASE (navy text on soft gray #f3f4f6): "Protect the kidney function that remains"

COLUMNS, left to right (name — advice line — nurse-check card):
1. Icon blood-pressure cuff — "Blood pressure" — "Systolic below 120 if tolerated" — "Measure correctly; ask about dizziness, falls"
2. Icon kidney with shield — "Renin–angiotensin inhibitor" — "Highest tolerated dose" — "Creatinine, potassium in 2–4 weeks; up to 30% rise expected"
3. Icon tablet with drop — "SGLT2 inhibitor" — "Start when eGFR 20 or higher" — "Teach sick-day plan, genital hygiene"
4. Icon heart with vessel — "Statin" — "Adults 50 and older, not on dialysis" — "Adherence; muscle symptoms"
5. Icon salt shaker with calamansi — "Low sodium" — "Under 2 g sodium (5 g salt) daily" — "Find salty sources; flavor with calamansi"
6. Icon pill crossed by a caution triangle — "Avoid kidney harm" — "Avoid nonsteroidal anti-inflammatory drugs" — "Ask: what do you take for pain?"

Small gray gloss under column 3 name: "sodium-glucose cotransporter-2"

Column colors: columns are soft light gray with a thin teal outline; nurse-check cards have a renal green #1f7a4d left edge. Column 6 has an amber #b8860b top cap to signal caution.

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of the base slab and cards.

LABEL RULES
Labels are short on purpose. Render each exactly as written. Complete label list: "Slowing chronic kidney disease", "Protect the kidney function that remains", "Blood pressure", "Systolic below 120 if tolerated", "Measure correctly; ask about dizziness, falls", "Renin–angiotensin inhibitor", "Highest tolerated dose", "Creatinine, potassium in 2–4 weeks; up to 30% rise expected", "SGLT2 inhibitor", "sodium-glucose cotransporter-2", "Start when eGFR 20 or higher", "Teach sick-day plan, genital hygiene", "Statin", "Adults 50 and older, not on dialysis", "Adherence; muscle symptoms", "Low sodium", "Under 2 g sodium (5 g salt) daily", "Find salty sources; flavor with calamansi", "Avoid kidney harm", "Avoid nonsteroidal anti-inflammatory drugs", "Ask: what do you take for pain?", "© renalcarematters.com".

NEGATIVE CONSTRAINTS
✗ No drug brand names or generic drug names (no dapagliflozin, no losartan, no atorvastatin)
✗ No doses in milligrams or tablet counts
✗ No numbers other than 120, 2–4, 30%, 20, 50, 2 g, 5 g
✗ No seventh pillar; no reordering
✗ No people or photographs
✗ No packaged food with readable labels
✗ No dark background; no serif fonts
✗ No garbled or invented words
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as in the label list
□ Six columns in order: Blood pressure, Renin–angiotensin inhibitor, SGLT2 inhibitor, Statin, Low sodium, Avoid kidney harm
□ Each column has one advice line and one nurse-check card
□ Numbers limited to 120, 2–4 weeks, 30%, 20, 50, 2 g, 5 g; no doses, no drug names
□ SGLT2 gloss "sodium-glucose cotransporter-2" present
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ Light background; Inter or another approved sans-serif
□ Pillar structure reads clearly at phone width

---

### 02-C — Staging at the desk
- **File:** images/nephrology-nursing-02-staging-at-the-desk.png
- **Placement:** Module 2 page, section `bedside` (Staging and reconciling at the desk)
- **Job:** A — the learner follows the desk routine from dated results to staging, monitoring, medicine reconciliation, and referral.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, renalcarematters.com house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Flowchart: confirm two abnormal results three months apart, check urine albumin, stage, read the risk grid, reconcile medicines, then check referral triggers.
- **Caption:** One low result is not chronic kidney disease; two abnormal results at least 3 months apart are. Kidney Failure Risk Equation thresholds are KDIGO 2024 practice points, and local referral criteria may differ.
- **Source of truth:** m02.py `bedside` — four parts: list every creatinine and eGFR with date; note whether two results at least 3 months apart are abnormal; check urine ACR exists and is recent; record the cause; reconcile medicines (prescription, over-the-counter pain relievers, herbal products and supplements, occasional medicines) by name, dose, and frequency; flag NSAID exposure, duplicate brands, and kidney-dosed medicines for prescriber or pharmacist review; do not advise stopping a prescribed medicine. m02.py `physiology` — reduced eGFR present less than 3 months may be AKI or AKD. m02.py `evidence` — KFRE 5-year risk of 3% to 5% is a suggested threshold for nephrology referral; 2-year risk above 10% for multidisciplinary care; referral also for sustained fall in eGFR, heavy or rising albuminuria, persistent unexplained blood in the urine, resistant hypertension, persistent potassium abnormalities, hereditary kidney disease. m02_x.py `causes` — risk grid gives checks per year.
- **Reviewer flags:** Module flag: KFRE thresholds are practice points; local referral criteria may differ. The flowchart order of the urine-albumin check after chronicity is a teaching layout; the module lists it as the second of four parts.

```text
Clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style, portrait 1024 × 1536 px (2:3). Subject: staging chronic kidney disease and reviewing medicines at the clinic desk. Top-to-bottom logic, generous margins, vector-flat.

BACKGROUND, TYPE, COLORS
White #ffffff background. All text in Inter (clean sans-serif); never serif. Navy #0f1e2e for title and text; teal #1a6b72 for decision diamonds and connector arrows; renal green #1f7a4d for endpoints; amber #b8860b for caution nodes; soft gray #f3f4f6 for side notes.

TITLE (top center, bold navy): "Staging at the desk"
SUBTITLE (teal): "Chronic kidney disease: confirm, stage, review"

MAIN TRUNK (top to bottom)
1. Rounded navy-outlined box: "Low eGFR or albuminuria found"
2. Rounded box: "List every creatinine and eGFR with date"
3. Teal diamond: "Two abnormal results 3 or more months apart?"
   - Branch right, labeled "No" → amber box: "Not yet chronic: may be acute kidney injury" → small gray box below it: "Find older results or repeat in 3 months"
   - Branch down, labeled "Yes"
4. Teal diamond: "Recent urine albumin-to-creatinine ratio?"
   - Branch right, labeled "No" → amber box: "Ask for the urine albumin test" (thin arrow returns to the trunk below)
   - Branch down, labeled "Yes"
5. Rounded box: "Record cause, G category, A category"
   Small gray example pill beside it: "Example: G3a/A2"
6. Rounded box: "Read risk color and checks per year"
7. Rounded box: "Reconcile medicines: name, dose, frequency"
   Gray side note to its left: "Ask what they take for pain, fever, headache"
8. Amber box: "Flag nonsteroidal anti-inflammatory drugs, duplicates, kidney-dosed drugs"
   Small amber caution note: "Do not stop prescribed medicines yourself"
9. Teal diamond: "Referral trigger present?"
   - Right side panel (soft gray, titled "Referral triggers"), items as short lines:
     "Kidney Failure Risk Equation:"
     "5-year risk 3% to 5%: nephrology referral"
     "2-year risk above 10%: multidisciplinary care"
     "Sustained eGFR fall"
     "Heavy or rising albuminuria"
     "Unexplained blood in urine"
     "Treatment-resistant hypertension"
     "Persistent potassium abnormality"
     "Hereditary kidney disease"
   - Down, labeled "Yes" → green endpoint: "Flag to prescriber with structured handoff"
   - Left, labeled "No" → green endpoint: "Monitor at grid frequency"

FOOTER: the exact text "© renalcarematters.com" small (about 11 px), Inter, navy #0f1e2e at 70% opacity, at the bottom-right corner, clear of all nodes and arrows.

LABEL RULES
Labels are short on purpose. Render every label exactly as written above, letter for letter, including "3% to 5%" and "above 10%". Do not add nodes.

NEGATIVE CONSTRAINTS
✗ No risk percentages other than "3% to 5%" (5-year) and "above 10%" (2-year)
✗ No eGFR cutoffs or ACR numbers in the flowchart
✗ No drug names, brand names, or doses
✗ No instruction for the nurse to stop, start, or change a medicine
✗ No more than 4 branching levels; no spaghetti arrows
✗ No people, photos, or 3D elements
✗ No dark background; no serif fonts
✗ No garbled or invented words
✗ No footer inside a node; no footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every node and side-panel label spelled exactly as written
□ Chronicity diamond reads "3 or more months apart"; "No" branch says may be acute kidney injury
□ Referral panel shows "5-year risk 3% to 5%: nephrology referral" and "2-year risk above 10%: multidisciplinary care" exactly
□ "Do not stop prescribed medicines yourself" caution present
□ No invented numbers; no drug names or doses
□ Decisions are teal diamonds; endpoints green; cautions amber
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ Flow reads top to bottom without crossing arrows

---


---

## Module 3 — Chronic Kidney Disease: Complications, Nutrition, and Medicines

### 03-A — When the fine-tuning fails: four disturbances
- **File:** images/nephrology-nursing-03-four-disturbances.png
- **Placement:** Module 3 page, section `physiology` (Four disturbances and their causes)
- **Job:** U — the learner traces each complication from fewer working nephrons to its effect on blood, bone, vessels, heart, and muscle.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure, with Constitution v1.0 Layer A anatomy rules
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Fewer working nephrons lead to anemia, mineral and bone disorder, potassium and acid retention, and poor nutrition, each linked to its body consequence.
- **Caption:** None of these disturbances announces itself with a dramatic symptom, so they are found by scheduled testing and by asking the right questions at every visit.
- **Source of truth:** m03.py `physiology` — Anemia: falling erythropoietin output; inflammation raises hepcidin, locking iron in storage; blood loss from testing and the dialysis circuit. Mineral and bone disorder: phosphate retained, less calcitriol, calcium tends to fall, more PTH, calcium and phosphate pulled from bone; weak bone and calcium in blood vessels. Potassium and acid: capacity to excrete a potassium load and the daily acid load shrinks; chronic acidosis promotes muscle and bone breakdown. Nutrition: uremia blunts appetite and alters taste; acidosis and inflammation accelerate protein breakdown; protein-energy wasting associated with higher mortality in observational studies. m03.py `model`: found by scheduled testing. m03.py `bedside`: ask about fatigue, breathlessness on exertion. m01_x.py `balance`: potassium sets the electrical stability of the heart.
- **Reviewer flags:** The plan named the four disturbances as anemia, mineral and bone disorder, acidosis, and potassium and fluid. The module's own four are anemia, mineral and bone disorder, potassium and acid, and nutrition; the figure follows the module. Fluid is not covered in the module 3 physiology section. "Heart rhythm risk" for potassium is sourced from Module 1.

```text
Publication-grade biomedical mechanism schematic, landscape 1792 × 1024 px (16:9). Subject: how loss of working nephrons in chronic kidney disease produces four disturbances and their body consequences. Review-article style, flat vector with soft semi-3D shading, white background, muted clinical palette.

════ LAYER A: ANATOMICAL TRUTH BLOCK ════
- Left organ panel: one kidney in coronal section, convex border LATERAL (left), hilum MEDIAL (right); thin pink-brown cortex; triangular medullary pyramids with papillae pointing INWARD; calyces drain INWARD to a renal pelvis exiting at the MEDIAL hilum; renal vein anterior (blue), renal artery (red, thick muscular wall), ureter posterior and exiting downward (pale yellow).
- The kidney is drawn slightly smaller with a scarred, irregular surface to signal chronic disease; it is not shown inside a body.
- A small dashed magnified circle beside it shows a cluster of nephrons: a few healthy (pale yellow) among many faded gray ones.
- Consequence icons are simple, correct anatomy: a bone with thinned inner structure; an artery cross-section with a thick muscular wall, circular lumen, and white calcium flecks in the wall; a heart with a rhythm line; a skeletal muscle bundle; a few red blood cells.

════ LAYOUT AND LABELS ════
Title (top left, bold navy #0f1e2e): "When the fine-tuning fails"
Subtitle (teal #1a6b72): "Four disturbances of chronic kidney disease"

Left panel (about 22% width): the kidney and dashed nephron circle. Label: "Fewer working nephrons".

Center (about 43% width): four stacked rounded cards, each joined from the kidney by a thin teal arrow. Each card: bold heading, then two or three short lines.
1. Card, pale red tint: "Anemia" — "Less erythropoietin" / "Hepcidin locks iron away" / "Blood loss: tests, dialysis"
2. Card, pale yellow tint: "Mineral and bone disorder" — "Phosphate retained" / "Less active vitamin D" / "Parathyroid hormone rises"
3. Card, pale blue tint: "Potassium and acid" — "Less potassium excreted" / "Daily acid retained"
4. Card, pale green tint: "Nutrition" — "Poor appetite, altered taste" / "Faster protein breakdown"

Right (about 35% width): consequence boxes, each with its icon, joined by arrows from the matching card:
- From Anemia → red cells icon: "Fatigue, breathless on exertion"
- From Mineral and bone disorder → bone icon: "Weak bone"; artery icon: "Calcium in blood vessels"
- From Potassium and acid → heart icon: "Heart rhythm risk"; muscle icon: "Muscle and bone breakdown"
- From Nutrition → muscle icon (shared): "Protein-energy wasting"; small gray note: "Linked to higher mortality"

Bottom strip (pale blue #e8f1f8 box, navy text): "Found by scheduled testing, not symptoms"

Typography: Inter for every label; never serif.

FOOTER: the exact text "© renalcarematters.com" bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of anatomy and labels.

LABEL RULES: Short labels on purpose; render each exactly as written. No other words.

════ NEGATIVE CONSTRAINTS ════
✗ No laboratory values, targets, or thresholds
✗ No drug names or doses
✗ No calyces pointing outward; no renal pelvis floating centrally or on the convex border
✗ No artery drawn thin-walled like a ureter
✗ No kidney placed inside a human body outline
✗ No FGF-23 label (not part of this module)
✗ No "causes death" wording; mortality is an association only
✗ No fifth disturbance (no fluid card)
✗ No cartoon style, dark background, or photorealism
✗ No serif fonts; no garbled text; no prompt text in the image
✗ No footer missing, enlarged, recolored, or altered

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as written
□ Kidney orientation correct: convex lateral, hilum medial, calyces draining inward
□ Artery icon has a thick muscular wall and round lumen
□ Four disturbance cards in order: Anemia, Mineral and bone disorder, Potassium and acid, Nutrition
□ Each consequence connects to the right card
□ "Linked to higher mortality" (not "causes") appears with protein-energy wasting
□ No numbers, no FGF-23, no drug names
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif

---

### 03-B — The mineral and bone loop, with treatment entry points
- **File:** images/nephrology-nursing-03-mineral-bone-loop.png
- **Placement:** Module 3 page, section `mbd-care` (Mineral and bone disorder: the treatments compared)
- **Job:** U — the learner sees how phosphate, active vitamin D, calcium, and parathyroid hormone push on each other and where each treatment acts.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure, with Constitution v1.0 Layer A anatomy rules
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Loop showing retained phosphate and low active vitamin D lowering calcium, raising parathyroid hormone, and drawing minerals from bone, with six treatment entry points.
- **Caption:** Phosphate binders act in the gut and only work when taken with food. Trials show these treatments improve laboratory values more consistently than fractures or survival.
- **Source of truth:** m03.py `physiology` — phosphate retained, kidney makes less calcitriol, blood calcium tends to fall, parathyroid glands release more PTH, which pulls calcium and phosphate out of bone; over years weak bone and calcium deposited in blood vessels; binders attach to phosphate in food in the gut. m03.py `evidence` — KDIGO 2017 weak recommendations; trials changed lab values more consistently than fractures or survival; limit calcium-based binders. m03_x.py `mbd-care` table — dietary phosphate control (processed food phosphate absorbed almost completely); calcium-based binders (limit total calcium load); non-calcium binders with meals; active vitamin D suppresses PTH (raises calcium and phosphate); calcimimetic makes the parathyroid more sensitive to calcium; parathyroidectomy removes overactive gland tissue; longer or more frequent dialysis removes more phosphate.
- **Reviewer flags:** The plan listed "FGF-23 rise"; FGF-23 does not appear anywhere in the Module 3 text, so it is left out. Nutritional vitamin D (cholecalciferol) is left out to avoid confusion with active vitamin D; the page table covers it.

```text
Publication-grade biomedical mechanism schematic, landscape 1792 × 1024 px (16:9). Subject: the chronic kidney disease–mineral and bone disorder loop, with numbered treatment entry points. Review-article style, flat vector with soft semi-3D shading, white background, muted clinical palette.

════ LAYER A: ANATOMICAL TRUTH BLOCK ════
- Kidney (left of center): coronal section, convex border LATERAL, hilum MEDIAL; cortex outer and pink-brown; pyramids with papillae pointing INWARD; calyces drain INWARD to a pelvis exiting at the MEDIAL hilum only. Slightly shrunken outline to show chronic disease.
- Parathyroid glands (top center): FOUR small oval glands on the POSTERIOR surface of the thyroid, shown in a posterior view of the thyroid lobes; glands enlarged and darker to show overactivity.
- Gut (bottom left): a simple segment of small intestine with food particles in the lumen.
- Bone (right): a long-bone segment cut lengthwise, showing outer cortical bone and inner spongy bone becoming thinner and more porous.
- Blood vessel (bottom right): artery cross-section with a THICK muscular media (pink-red), circular lumen, and white calcium deposits in the vessel wall.
- Blood pool (center): a soft circular "Blood" zone where the four minerals and hormones are tracked.

════ LAYOUT AND LABELS ════
Title (top left, bold navy #0f1e2e): "The mineral and bone loop"
Subtitle (teal #1a6b72): "Chronic kidney disease–mineral and bone disorder"

Mechanism arrows (thin, navy for normal flow; red #c00000 for harmful change), with short labels and up/down arrows exactly:
- From kidney to blood: "↑ Phosphate retained"
- From kidney to blood: "↓ Active vitamin D (calcitriol)"
- Within blood: "↓ Calcium tends to fall"
- Blood to parathyroid glands: "Low calcium signals glands"
- Parathyroid glands to blood: "↑ Parathyroid hormone"
- Parathyroid hormone to bone: "Pulls calcium, phosphate from bone"
- Bone outcome label: "Weak bone"
- Vessel outcome label: "Calcium in blood vessels"
- A curved red arrow from bone back into the blood zone closes the loop.

Treatment entry points: six teal numbered circles, each pinned to where it acts, with a short label in a white rounded tag:
1. At the gut: "Cut processed phosphate"
2. At the gut: "Binders with meals"
3. At the kidney/blood: "Longer or more frequent dialysis"
4. At the parathyroid arrow: "Active vitamin D lowers hormone"
5. At the parathyroid glands: "Calcimimetic: gland senses calcium"
6. At the parathyroid glands: "Parathyroidectomy"
Small amber caution tag near entry point 2: "Limit calcium-based binders"
Small amber caution tag near entry point 4: "Watch calcium and phosphate"

Bottom strip (pale blue #e8f1f8, navy text): "Lab values improve; outcomes less certain"

Typography: Inter for every label; never serif.

FOOTER: the exact text "© renalcarematters.com" bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of anatomy and labels.

LABEL RULES: Short labels on purpose; render each exactly as written, including the arrows ↑ and ↓. No other words.

════ NEGATIVE CONSTRAINTS ════
✗ No FGF-23, klotho, or any hormone not listed
✗ No laboratory values, target ranges, or units
✗ No drug brand names and no doses
✗ No parathyroid glands on the front of the thyroid or inside the thyroid
✗ No artery with a thin wall or slit-like lumen
✗ No calyces pointing outward; no pelvis on the convex border
✗ No arrow showing parathyroid hormone lowering phosphate retention or raising vitamin D
✗ No binder shown acting in the blood (binders act in the gut only)
✗ No cartoon style, dark background, or photorealism
✗ No serif fonts; no garbled text; no prompt text in the image
✗ No footer missing, enlarged, recolored, or altered

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every label spelled exactly as written, with correct ↑ and ↓ symbols
□ Chain reads: phosphate retained and low active vitamin D → calcium falls → parathyroid hormone rises → minerals pulled from bone → weak bone and calcium in vessels
□ Four parathyroid glands on the posterior thyroid
□ Binders pinned to the gut, not the blood
□ Six numbered entry points, each at the right site; two amber caution tags present
□ No FGF-23 and no invented numbers
□ Kidney orientation correct; artery has a thick muscular media with wall calcification
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif

---

### 03-C — Filipino food guide: potassium, phosphate, protein
- **File:** images/nephrology-nursing-03-filipino-food-guide.png
- **Placement:** Module 3 page, section `diet` (Nutrition by stage, in food terms)
- **Job:** A/P — the learner can counsel from familiar Filipino foods, adjusting portions and preparation instead of issuing blanket bans.
- **Governing skill:** williamriveromd-infographic-skill (food matrix / nutrition infographic)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Filipino foods higher and lower in potassium, processed foods high in absorbed phosphate, a four-step potassium-lowering method, and protein advice by stage.
- **Caption:** These are counseling examples, not a complete table; portions and preparation are adjusted to each patient's own potassium and phosphate results. Unintentional weight loss calls for a dietitian, not more restriction.
- **Source of truth:** m03_x.py `diet` — Potassium higher: banana, coconut water, avocado, ripe mango in large portions, dried fruit, tomato sauce, root crops such as sweet potato and taro, leafy tops, mung beans, chocolate drinks. Lower: apple, pineapple, pear, grapes, cabbage, sayote, upo, cucumber, string beans in ordinary portions. Root crops and some vegetables lose potassium when peeled, cut small, soaked, and boiled in plenty of water that is discarded. Blanket bans no longer advised. Protein: stages 3 to 5 not on dialysis moderate, avoid excess, lower targets only with dietitian supervision; hemodialysis 1.0 to 1.2 g/kg per day; peritoneal dialysis 1.0 to 1.2 g/kg per day. m03_x.py `mbd-care` — phosphate added to processed food absorbed almost completely; biggest gains: cola drinks, processed and cured meats (hot dogs, tocino, longganisa, canned meat), instant noodles, processed cheese; do not restrict fresh protein foods to the point of malnutrition. m03.py `bedside` — unintentional weight loss is a reason for dietitian referral, not more restriction.
- **Reviewer flags:** The plan asked for "swaps"; the module gives higher and lower lists, not one-to-one swaps, so the figure shows two lists side by side. Module flag: food lists are examples for counseling, not a complete table. Protein g/kg values are nutrition targets from KDOQI 2020 as stated in the module, not drug doses.

```text
CKD nutrition infographic, clean educational food matrix, landscape 1792 × 1024 px (16:9). Subject: everyday Filipino foods grouped by potassium and phosphate, plus protein advice by stage. Realistic, appetizing food renderings in small round vignettes on clean cards; calm and uncluttered.

BACKGROUND AND TYPE
White #ffffff canvas. All text in Inter (clean sans-serif); never serif. Text navy #0f1e2e; headings teal #1a6b72.

TITLE (top left, bold navy): "Filipino food guide for kidney disease"
BANNER beside title (teal pill, white text): "Adjust portions, not blanket bans"

LAYOUT: three columns of cards, then a full-width bottom strip.

COLUMN 1 (left, about 40%): POTASSIUM
Heading: "Potassium"
Two sub-cards side by side:
- Amber-edged card (#b8860b): "Higher" — food vignettes, each labeled exactly: "Banana", "Coconut water", "Avocado", "Ripe mango, large portion", "Dried fruit", "Tomato sauce", "Sweet potato", "Taro", "Leafy tops", "Mung beans", "Chocolate drinks"
- Green-edged card (#1f7a4d): "Lower, ordinary portions" — food vignettes, each labeled exactly: "Apple", "Pineapple", "Pear", "Grapes", "Cabbage", "Sayote", "Upo", "Cucumber", "String beans"
Under both: a four-icon row with tiny arrows, heading "Lower the potassium in root crops": "Peel" → "Cut small" → "Soak" → "Boil, discard water"

COLUMN 2 (center, about 30%): PHOSPHATE
Heading: "Phosphate"
Red-edged card (#b91c1c): "Processed: absorbed almost completely" — vignettes labeled exactly: "Cola drinks", "Hot dogs", "Tocino", "Longganisa", "Canned meat", "Instant noodles", "Processed cheese"
Green note below: "Keep fresh protein foods"

COLUMN 3 (right, about 30%): PROTEIN BY STAGE
Heading: "Protein"
Three stacked rounded rows with small icons:
- Kidney icon: "Stages 3 to 5, no dialysis" — "Moderate; avoid excess"
- Dialysis-machine icon: "Hemodialysis" — "1.0 to 1.2 g/kg per day"
- Abdomen-with-bag icon: "Peritoneal dialysis" — "1.0 to 1.2 g/kg per day"
Gray note: "Lower targets only with a dietitian"

BOTTOM STRIP (full width, soft gray #f3f4f6, navy text, small person-and-scale icon): "Losing weight without trying? Refer to the dietitian"

FOOD RENDERING
Ordinary Filipino home and market forms: banana as a small bunch of lakatan-type bananas, coconut water in a green coconut, taro and sweet potato whole and unpeeled, sayote and upo whole, string beans in a bundle, tocino and longganisa cooked on a plate, canned meat as a plain unlabeled can. No packaging text, no brand marks.

FOOTER: the exact text "© renalcarematters.com" in the bottom-right corner, small (about 11 px), Inter, navy #0f1e2e at 70% opacity, clear of the bottom strip text.

LABEL RULES
Labels are short on purpose. Render each food name and label exactly as written above, letter for letter. No food may appear that is not listed.

NEGATIVE CONSTRAINTS
✗ No food not in the lists above (no salt, fish sauce, rice, or meat dishes beyond those named)
✗ No milligram values, portion weights, or potassium or phosphate numbers
✗ No numbers other than "3 to 5" and "1.0 to 1.2 g/kg per day"
✗ No red X marks, crossed-out foods, or "forbidden" symbols
✗ No branded packaging or readable labels on food
✗ No people eating; no photographs of patients
✗ No dark background; no serif fonts
✗ No garbled food names; Filipino names "Sayote", "Upo", "Tocino", "Longganisa" spelled exactly
✗ No footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every food name and label spelled exactly as written (including Sayote, Upo, Tocino, Longganisa)
□ Higher-potassium card has 11 foods; lower card has 9; phosphate card has 7; no extra foods
□ Each food image matches its label (taro is not shown as sweet potato, upo is not shown as cucumber)
□ Four-step leaching row reads Peel, Cut small, Soak, Boil, discard water
□ Protein rows: "Moderate; avoid excess" for stages 3 to 5; "1.0 to 1.2 g/kg per day" for both dialysis types
□ No red X marks; no other numbers
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif
□ No brand names or readable packaging

---

### 03-D ○ — Anemia check and the iron decision
- **File:** images/nephrology-nursing-03-anemia-iron-decision.png
- **Placement:** Module 3 page, section `anemia-care` (Treating anemia: iron, stimulating agents, and what to watch)
- **Job:** A — the learner knows which tests to gather and the two situations in which iron is held.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, renalcarematters.com house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Flowchart: gather blood count, reticulocytes, ferritin, and TSAT; suspend iron during infection; withhold iron when ferritin exceeds 700 or TSAT reaches 40%.
- **Caption:** Iron is held when ferritin is above 700 ng/mL or transferrin saturation (TSAT) is 40% or higher, and suspended during active infection (KDIGO 2026). Thresholds for starting iron differ by setting and follow the prescriber and unit protocol.
- **Source of truth:** m03.py `evidence` — KDIGO 2026: CBC, reticulocyte count, ferritin, and TSAT when anemia is evaluated; non-dialysis algorithm treats iron deficiency before considering an ESA; withhold iron when ferritin exceeds 700 ng/mL or TSAT reaches 40%; suspend iron during active infection; same withholding rule in the hemodialysis algorithm; starting thresholds differ by setting, applied by prescriber and unit protocol; targets deliberately below normal. m03.py `physiology` — ferritin reflects stored iron; TSAT reflects iron available. m03_x.py `anemia-care` — check blood pressure before each ESA dose; poor-response causes in order: iron deficiency, infection or inflammation, blood loss, inadequate dialysis, severe hyperparathyroidism, missed doses; intravenous iron: watch for reaction and stop at once.
- **Reviewer flags:** Module flag: these thresholds are from the KDIGO 2026 non-dialysis algorithm; the module states the withholding rule is the same in the hemodialysis algorithm. The order "infection first, then iron indices" is a teaching layout, not stated in the module.

```text
Clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style, portrait 1024 × 1536 px (2:3). Subject: evaluating anemia in chronic kidney disease and deciding whether iron can be given. Top-to-bottom logic, generous margins, vector-flat.

BACKGROUND, TYPE, COLORS
White #ffffff background. All text in Inter (clean sans-serif); never serif. Navy #0f1e2e for title and text; teal #1a6b72 for decision diamonds and arrows; renal green #1f7a4d for go-ahead nodes; amber #b8860b for caution; clinical red #b91c1c for hold nodes; soft gray #f3f4f6 for side notes.

TITLE (top center, bold navy): "Anemia check and the iron decision"
SUBTITLE (teal): "Chronic kidney disease"

MAIN TRUNK (top to bottom)
1. Rounded box: "Low hemoglobin found"
2. Rounded box headed "Gather four tests", listing:
   "Complete blood count"
   "Reticulocyte count"
   "Ferritin: stored iron"
   "TSAT: iron available"
   Gray gloss beside: "TSAT = transferrin saturation"
3. Teal diamond: "Active infection?"
   - Right, labeled "Yes" → red box: "Suspend iron"
   - Down, labeled "No"
4. Teal diamond: "Ferritin above 700 ng/mL or TSAT 40% or higher?"
   - Right, labeled "Yes" → red box: "Withhold iron"
   - Down, labeled "No"
5. Green box: "Iron deficiency treated first"
   Gray note beside: "Start thresholds: prescriber and unit protocol"
6. Rounded box: "Then consider a stimulating agent (ESA)"
   Gray gloss: "ESA = erythropoiesis-stimulating agent"
7. Green endpoint: "Hemoglobin range kept below normal"

SIDE PANELS (soft gray cards, right side, lower half)
Card A, headed "Nurse checks":
   "Blood pressure before each ESA dose"
   "Intravenous iron: watch for reaction"
   "Reaction: stop the infusion at once"
Card B, headed "Poor response? Look for":
   "Iron deficiency"
   "Infection or inflammation"
   "Blood loss"
   "Inadequate dialysis"
   "Severe hyperparathyroidism"
   "Missed doses"

FOOTER: the exact text "© renalcarematters.com" small (about 11 px), Inter, navy #0f1e2e at 70% opacity, at the bottom-right corner, clear of all nodes and arrows.

LABEL RULES
Labels are short on purpose. Render every label exactly as written above, letter for letter, including "above 700 ng/mL" and "40% or higher". Do not add nodes.

NEGATIVE CONSTRAINTS
✗ No numbers other than "700 ng/mL" and "40%"
✗ No hemoglobin target values or start thresholds for iron
✗ No iron or ESA product names, routes beyond "Intravenous iron", or doses
✗ No observation times or infusion rates
✗ No transfusion node
✗ No more than 4 branching levels; no spaghetti arrows
✗ No people, photos, or 3D elements
✗ No dark background; no serif fonts
✗ No garbled or invented words
✗ No footer inside a node; no footer variant other than © renalcarematters.com

Render all text exactly as written in quotation marks above and no other text.
```

**QA after generation:**
□ Every node and side-panel label spelled exactly as written
□ Withhold diamond reads exactly "Ferritin above 700 ng/mL or TSAT 40% or higher?"
□ "Active infection?" Yes branch leads to "Suspend iron"
□ Only two numbers appear: 700 ng/mL and 40%
□ Poor-response list in the module's order (iron deficiency first, missed doses last)
□ No product names, doses, rates, or observation times
□ Hold nodes red, go-ahead nodes green, decisions teal diamonds
□ Footer reads exactly © renalcarematters.com, bottom right, small, semi-transparent navy
□ White background; Inter or another approved sans-serif


---

## Module 4 — Acute Kidney Injury and Acute Kidney Support

### 04-A — Before, inside, or after the filter
- **File:** images/nephrology-nursing-04-aki-three-causes.png
- **Placement:** Module 4, section `physiology` (Criteria and the three categories of cause); the mental model is in `model` (Before, inside, or after the filter)
- **Job:** U — the learner sorts any AKI into supply, filter, or outflow and links each bedside clue to one of the three.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure (+ Constitution v1.0 Layer A kidney, ureter, and hilar rules)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Kidney and urinary tract schematic dividing acute kidney injury causes into reduced blood supply, kidney tissue damage, and blocked urine outflow, with examples.
- **Caption:** Acute kidney injury is sorted like a slow household tap: the supply, the filter, or the outflow pipe. Reduced perfusion and obstruction are often reversible within hours if someone notices, so check them first.
- **Source of truth:** m04.py `model` (tap analogy: supply, filter, outflow; "the first and third are often reversible within hours"); m04.py `physiology` (reduced perfusion most common in hospitalized patients; volume loss from vomiting, diarrhea, bleeding; low cardiac output; sepsis; NSAID narrows the vessel entering the glomerulus; renin–angiotensin blocker relaxes the vessel leaving it; acute tubular injury from prolonged poor perfusion, sepsis, toxins such as aminoglycosides and contrast media; inflammation of glomeruli or interstitium; leptospirosis and severe dengue in the Philippines; obstruction must affect both kidneys, a single functioning kidney, or the bladder outlet; enlarged prostate, blocked urinary catheter, stones, pelvic tumors). m04_x.py `management` (bedside bladder scan; kidney ultrasound to exclude obstruction). No numbers used.
- **Reviewer flags:** Leptospirosis and dengue are uncited in the module (existing module flag); they appear here only as named examples. Confirm the afferent/efferent arteriole inset is wanted at nurse level.
- **Attach when generating:** none

```text
Publication-grade biomedical mechanism schematic, 1792 × 1024 landscape (16:9). Subject: the three categories of acute kidney injury (AKI) — before the kidney (reduced perfusion), inside the kidney (intrinsic damage), after the kidney (obstruction) — on ONE kidney-and-urinary-tract schematic. Review-article style, flat vector with soft semi-3D shading, white #ffffff background.

ANATOMICAL TRUTH (overrides style):
- Anterior view: patient's right kidney on IMAGE LEFT, sitting slightly LOWER than the left kidney.
- Each kidney: convex border LATERAL, hilum MEDIAL facing the spine; renal pelvis exits only at the medial hilum; calyces drain inward toward the pelvis.
- Aorta (red, thick-walled) and inferior vena cava (blue, thin-walled) run vertically in the midline; one renal artery and one renal vein to each kidney.
- Two ureters: thin-walled, descend medially, enter the bladder posterolaterally at its base. Bladder in the pelvis, prostate as a small rounded gland just below the bladder neck surrounding the urethra, a urinary catheter entering through the urethra into the bladder with its drainage tube leading down to a bag below.
- No anatomy drawn inside a patient silhouette; this is a standalone organ schematic.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "Acute kidney injury: three places to look"
- Subtitle, teal #1a6b72: "Before, inside, or after the filter"
- Small analogy strip under the subtitle (three tiny line icons, gray-navy): tap supply pipe → water filter → outflow drain, labeled "Supply", "Filter", "Outflow".
- Center-left (about 55% of width): the anatomical schematic with three colored zone brackets:
  1. Zone BEFORE, amber #b8860b bracket around the aorta and renal arteries, label "1 · Before the kidney: reduced perfusion"
  2. Zone INSIDE, clinical red #b91c1c bracket around one kidney's tissue, label "2 · Inside the kidney: tissue damage"
  3. Zone AFTER, teal #1a6b72 bracket around both ureters, bladder, prostate, and catheter, label "3 · After the kidney: obstruction"
- Dashed magnified inset (thin dashed gray border, upper center-right, about 18% of canvas) connected by a dashed leader to the kidney: one glomerulus with its incoming and outgoing arterioles and the first part of the tubule. Labels inside the inset:
  - "Inflow vessel narrowed by NSAID" (arrow at the afferent arteriole, amber)
  - "Outflow vessel relaxed by RAS blocker" (arrow at the efferent arteriole, amber)
  - "Tubule injury" (red speckle on tubular cells)
- Right column (about 30% of width): three stacked rounded cards, each with a colored top band matching its zone:
  Card 1 (amber) "Reduced perfusion — most common in hospital": "Vomiting, diarrhea, bleeding" · "Low cardiac output" · "Sepsis" · "NSAID or RAS blocker"
  Card 2 (red) "Intrinsic damage": "Acute tubular injury" · "Prolonged poor perfusion, sepsis" · "Aminoglycosides, contrast media" · "Glomerular or interstitial inflammation" · "Leptospirosis, severe dengue"
  Card 3 (teal) "Obstruction": "Both kidneys, single kidney, or bladder outlet" · "Enlarged prostate" · "Blocked urinary catheter" · "Stones, pelvic tumors"
- Bottom strip, full width, soft gray #f3f4f6, navy text: "Ask in this order: 1 → 2 → 3" and, separated by a thin divider, "1 and 3 are often reversible within hours" and "Bedside check: catheter, bladder scan".

Every label verbatim (render exactly these and nothing else): "Acute kidney injury: three places to look"; "Before, inside, or after the filter"; "Supply"; "Filter"; "Outflow"; "1 · Before the kidney: reduced perfusion"; "2 · Inside the kidney: tissue damage"; "3 · After the kidney: obstruction"; "Inflow vessel narrowed by NSAID"; "Outflow vessel relaxed by RAS blocker"; "Tubule injury"; "Reduced perfusion — most common in hospital"; "Vomiting, diarrhea, bleeding"; "Low cardiac output"; "Sepsis"; "NSAID or RAS blocker"; "Intrinsic damage"; "Acute tubular injury"; "Prolonged poor perfusion, sepsis"; "Aminoglycosides, contrast media"; "Glomerular or interstitial inflammation"; "Leptospirosis, severe dengue"; "Obstruction"; "Both kidneys, single kidney, or bladder outlet"; "Enlarged prostate"; "Blocked urinary catheter"; "Stones, pelvic tumors"; "Ask in this order: 1 → 2 → 3"; "1 and 3 are often reversible within hours"; "Bedside check: catheter, bladder scan"; small anatomical labels "Aorta", "Kidney", "Ureter", "Bladder", "Prostate", "Urinary catheter".

Colors: navy #0f1e2e text; teal #1a6b72; amber #b8860b; clinical red #b91c1c; anatomy in light gray-blue; arteries red, veins blue; card fills #f3f4f6. Typeface: Inter for all text. Thin leader lines, generous whitespace.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

DO NOT:
✗ No mirrored kidneys; right kidney on image left and lower.
✗ No hilum on the lateral convex border; no renal pelvis floating in the middle of the kidney.
✗ No ureter drawn thick-walled like an artery; no artery drawn thin like a ureter.
✗ No single blocked ureter shown as the cause of AKI with a normal opposite kidney.
✗ No stone drawn inside the kidney tissue labeled as "intrinsic".
✗ No numbers, creatinine values, doses, or percentages anywhere.
✗ No drug brand names; no extra drugs beyond NSAID, RAS blocker, aminoglycosides, contrast media.
✗ No patient body silhouette with organs visible through skin.
✗ No cartoon style, no dark background, no serif font, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ All labels spelled exactly as listed; no extra words or invented text
□ No numbers anywhere in the figure
□ Right kidney on image left and lower; hilum medial; pelvis at hilum
□ Ureters thin, entering bladder base; prostate below bladder neck; catheter in urethra to bladder
□ Three zone brackets in amber (before), red (inside), teal (after), matching card colors
□ Inset shows NSAID at the inflow (afferent) vessel and RAS blocker at the outflow (efferent) vessel, not reversed
□ Obstruction card says both kidneys, single kidney, or bladder outlet
□ Bottom strip states order 1 → 2 → 3 and reversibility of 1 and 3
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 04-B — KDIGO 2012 AKI staging card
- **File:** images/nephrology-nursing-04-aki-staging-card.png
- **Placement:** Module 4, section `staging` (Staging, and who is at risk)
- **Job:** A — the learner applies the creatinine and urine-output criteria at the bedside and assigns the highest stage reached.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card of KDIGO 2012 acute kidney injury definition and stages 1 to 3 by serum creatinine and urine output, with a 60 kg worked example.
- **Caption:** Any one definition criterion is enough to diagnose acute kidney injury, and the patient is placed in the highest stage reached by either creatinine or urine output. Even stage 1 is reported.
- **Source of truth:** m04.py `physiology`: definition — rise in serum creatinine of 0.3 mg/dL (26.5 µmol/L) or more within 48 hours; rise to 1.5 times baseline or more, known or presumed to have occurred within the prior 7 days; urine volume below 0.5 mL/kg per hour for 6 hours. m04_x.py `staging` table: Stage 1 — 1.5 to 1.9 times baseline, or a rise of 0.3 mg/dL or more / Below 0.5 mL/kg per hour for 6 to 12 hours; Stage 2 — 2.0 to 2.9 times baseline / Below 0.5 mL/kg per hour for 12 hours or more; Stage 3 — 3.0 times baseline or more, or 4.0 mg/dL or higher, or start of kidney replacement / Below 0.3 mL/kg per hour for 24 hours or more, or no urine for 12 hours. "The patient is placed in the highest stage reached by either criterion." Worked example: 60 kg adult, 0.5 mL/kg per hour = 30 mL per hour = 180 mL over 6 hours; "a single low hour after a catheter change is not AKI, but six in a row is." "Even stage 1 is reported."
- **Reviewer flags:** KDIGO 2026 AKI/AKD guideline was a public-review draft; recheck this card when the final version is published (existing module flag).
- **Attach when generating:** none

```text
Clinical reference card, 1536 × 1152 landscape (4:3). Subject: KDIGO 2012 acute kidney injury (AKI) definition and staging. Publication-grade nephrology reference design, white #ffffff background, flat vector, no illustrations except two tiny line icons (a blood tube and a urine collection bag) in the column headers.

LAYOUT (top to bottom):
1. Title, top left, bold navy #0f1e2e: "Acute kidney injury: definition and stages"
   Subtitle, teal #1a6b72: "KDIGO 2012 criteria"
2. Definition band, rounded rectangle, light teal fill #eef6f7, teal left border. Heading: "AKI is present if ANY ONE is met:" then three short rows, each with a small teal check circle:
   - "Creatinine rise of 0.3 mg/dL (26.5 µmol/L) or more within 48 hours"
   - "Creatinine 1.5 times baseline or more, known or presumed within the prior 7 days"
   - "Urine below 0.5 mL/kg per hour for 6 hours"
3. Main staging table, three columns, three body rows. Column headers on soft gray #f3f4f6 in teal: "Stage" | "Serum creatinine" (blood tube icon) | "Urine output" (urine bag icon). Each Stage cell is a solid colored badge with a white numeral; the row has a very light tint of the same color.
   Row 1 — badge amber #b8860b, "1"
     Serum creatinine: "1.5 to 1.9 times baseline, or a rise of 0.3 mg/dL or more"
     Urine output: "Below 0.5 mL/kg per hour for 6 to 12 hours"
   Row 2 — badge orange #C55A11, "2"
     Serum creatinine: "2.0 to 2.9 times baseline"
     Urine output: "Below 0.5 mL/kg per hour for 12 hours or more"
   Row 3 — badge clinical red #b91c1c, "3"
     Serum creatinine: "3.0 times baseline or more, or 4.0 mg/dL or higher, or start of kidney replacement"
     Urine output: "Below 0.3 mL/kg per hour for 24 hours or more, or no urine for 12 hours"
4. Rule banner directly under the table, navy text on white with a navy outline: "Assign the HIGHER stage reached by either column."
5. Bottom row, two side-by-side rounded cards on #f3f4f6:
   Left card, heading "Worked example: 60 kg adult": "0.5 mL/kg per hour = 30 mL per hour" and "= 180 mL over 6 hours"
   Right card, heading "Bedside rules": "One low hour after a catheter change: not AKI" · "Six low hours in a row: AKI" · "Even stage 1 is reported"

Every label verbatim (render exactly these and nothing else): all strings in quotation marks above, exactly as written, including the units "mg/dL", "µmol/L", and "mL/kg per hour".

Colors: navy #0f1e2e text; teal #1a6b72 headers; amber #b8860b, orange #C55A11, clinical red #b91c1c for stage badges only; card fills #f3f4f6 and #eef6f7. Typeface: Inter throughout; table text at least 13 pt equivalent; numbers in tabular figures so decimals align. Generous cell padding, thin gray row dividers.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the bottom cards and clear of them.

DO NOT:
✗ No changed numbers: not "1.5–2.0", not "2–3 times", not "≥ 4.0 mg/dL" rewritten differently, not "0.5 mL/kg/h for 6 hours" in stage 2.
✗ No "RIFLE" or "AKIN" labels, no "Risk/Injury/Failure" words.
✗ No µmol/L conversions other than the single "26.5 µmol/L" shown.
✗ No biomarkers, no eGFR column, no urine sodium.
✗ No AKD (acute kidney disease) row.
✗ No green "normal" row and no stage 0.
✗ No arrows implying stage 1 always progresses to stage 3.
✗ No dark background, no serif font, no cartoon icons, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Every table cell matches the module text character for character (check each of the six cells)
□ Definition band has three criteria including "26.5 µmol/L", "48 hours", "prior 7 days", "6 hours"
□ Stage 3 urine cell says "0.3" (not 0.5) and "no urine for 12 hours"
□ Stage badges amber 1, orange 2, red 3
□ Rule "Assign the HIGHER stage reached by either column" present
□ Worked example reads 30 mL per hour and 180 mL over 6 hours
□ No invented numbers, no extra classification systems
□ Label spelling correct throughout; units rendered correctly (µ symbol present)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 04-C — Hyperkalemia: the nurse's sequence
- **File:** images/nephrology-nursing-04-hyperkalemia-sequence.png
- **Placement:** Module 4, section `evidence` (What cannot wait); companion to the treatment table in `management`
- **Job:** A — the learner knows the order of nursing actions for hyperkalemia: recognize, monitor, call, prepare ordered treatments, recheck.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, house style, with Mode A emergency color logic)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Algorithm showing nursing steps for hyperkalemia: recognize level and ECG, continuous monitoring, immediate SBAR call, prepare ordered treatments, recheck potassium.
- **Caption:** Emergency hyperkalemia treatment is prescribed; the nurse's time-critical work is recognition, continuous cardiac monitoring, an immediate call, and having ordered treatments ready. Because shifting treatments wear off, a repeat potassium is part of the plan.
- **Source of truth:** m04.py `evidence`: KDIGO potassium conference (clase2020) — potassium 6.5 mmol/L or higher is severe whether or not the ECG has changed; 6.0 mmol/L or higher with ECG changes is also severe; peaked T waves → widened QRS → cardiac arrest; fixed logic: IV calcium to stabilize, insulin with glucose and inhaled beta-agonist to shift, then removal (dialysis if kidneys cannot); "these are prescribed treatments; the nurse's time-critical tasks are recognition, continuous cardiac monitoring, an immediate call, and having the treatments ready." Cardiac arrest branch: "standard resuscitation takes priority" (aha2025special — arrest branch only, not cited in the figure). m04.py `case` ACTE: "Do not wait for a repeat sample to call. Widening QRS, slow heart rate, or loss of consciousness: activate the cardiac arrest team"; SBAR. m04_x.py `management` table nursing monitoring: calcium — continuous ECG, secure patent vein, repeat ECG after the dose; insulin with glucose — blood glucose before, then hourly for several hours, hypoglycemia common and can be delayed; beta-agonist — heart rate and tremor; removal (diuretic if urine is being made, potassium binder, dialysis) — repeat potassium as ordered, prepare for dialysis; "the first three steps wear off, potassium rebounds unless removal follows." Effect timings in the table are deliberately not shown.
- **Reviewer flags:** Module flag: emergency sequence by physician order or hospital protocol; nephrologist review required. Sodium bicarbonate row ("mainly when acidosis is present") omitted for simplicity; add if reviewer wants it. Only the "severe" grades are stated in the module, so no mild or moderate tiers are shown.
- **Attach when generating:** none

```text
Clinical algorithm flowchart, 1024 × 1536 portrait (2:3). Subject: the nurse's sequence for hyperkalemia (high blood potassium). renalcarematters.com house style with emergency color logic. White #ffffff background, clean vector, centered top-to-bottom trunk, thin navy arrows, rounded rectangles for actions, one diamond for the decision.

TITLE BLOCK (top):
- Title, bold navy #0f1e2e: "Hyperkalemia: the nurse's sequence"
- Subtitle, teal #1a6b72: "Treatments are prescribed. The nurse recognizes, monitors, calls, prepares."

SEVERITY BOX (top right, beside step 1, outlined clinical red #b91c1c, very light red fill):
Heading: "Severe hyperkalemia"
Row: "Potassium 6.5 mmol/L or higher — with or without ECG changes"
Row: "Potassium 6.0 mmol/L or higher — with ECG changes"
Small gray source line: "KDIGO potassium conference"

MAIN TRUNK (numbered nodes, each with a short bold verb heading):
1. Peach/orange node #f6d5bf with navy text — "1 · RECOGNIZE": "High potassium result" · "Check ECG: peaked T waves, wide QRS"
2. Pink-red diamond #f4c7c7, red outline — "Wide QRS, slow heart rate, or unconscious?"
   - YES arrow to the RIGHT, bold red branch label "YES", into a solid clinical red node #b91c1c with white text: "Activate cardiac arrest team" · "Standard resuscitation takes priority"
   - NO arrow DOWN, label "NO"
3. Pale green node #d9efe3 — "2 · MONITOR": "Continuous cardiac monitoring" · "12-lead ECG"
4. Amber-outlined node, light amber fill — "3 · CALL NOW": "Immediate SBAR call" · "Do not wait for a repeat sample"
5. Wide pale blue node #dbe8f5 spanning most of the width — "4 · PREPARE ORDERED TREATMENTS" with a small navy tag in its top-right corner reading "By order or approved protocol". Inside, three equal sub-columns separated by thin dividers, each with a heading and a nurse-monitoring line beneath it in smaller teal text:
   - "STABILIZE the heart" / "IV calcium" / monitoring: "Continuous ECG; secure vein; repeat ECG"
   - "SHIFT potassium into cells" / "Insulin with glucose" and "Inhaled beta-agonist" / monitoring: "Glucose before, then hourly" and "Heart rate, tremor"
   - "REMOVE from the body" / "Diuretic, potassium binder, dialysis" / monitoring: "Prepare for dialysis"
6. Pale green node — "5 · RECHECK": "Repeat potassium as ordered" · "Shift wears off: potassium rebounds"

BOTTOM NOTE (soft gray #f3f4f6 strip): "Hypoglycemia after insulin is common and can be delayed."

Every label verbatim (render exactly these and nothing else): "Hyperkalemia: the nurse's sequence"; "Treatments are prescribed. The nurse recognizes, monitors, calls, prepares."; "Severe hyperkalemia"; "Potassium 6.5 mmol/L or higher — with or without ECG changes"; "Potassium 6.0 mmol/L or higher — with ECG changes"; "KDIGO potassium conference"; "1 · RECOGNIZE"; "High potassium result"; "Check ECG: peaked T waves, wide QRS"; "Wide QRS, slow heart rate, or unconscious?"; "YES"; "NO"; "Activate cardiac arrest team"; "Standard resuscitation takes priority"; "2 · MONITOR"; "Continuous cardiac monitoring"; "12-lead ECG"; "3 · CALL NOW"; "Immediate SBAR call"; "Do not wait for a repeat sample"; "4 · PREPARE ORDERED TREATMENTS"; "By order or approved protocol"; "STABILIZE the heart"; "IV calcium"; "Continuous ECG; secure vein; repeat ECG"; "SHIFT potassium into cells"; "Insulin with glucose"; "Inhaled beta-agonist"; "Glucose before, then hourly"; "Heart rate, tremor"; "REMOVE from the body"; "Diuretic, potassium binder, dialysis"; "Prepare for dialysis"; "5 · RECHECK"; "Repeat potassium as ordered"; "Shift wears off: potassium rebounds"; "Hypoglycemia after insulin is common and can be delayed."

Colors: navy #0f1e2e text and arrows; teal #1a6b72 subtitle and monitoring lines; clinical red #b91c1c for severity box and arrest branch only; amber #b8860b for the call node outline; pastel fills as specified. Typeface: Inter throughout; node text at least 13 pt equivalent. Generous margins, consistent node widths, no icons except an optional tiny ECG trace line in step 1.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside every node and arrow.

DO NOT:
✗ No drug doses, units, routes beyond "IV" and "inhaled", or infusion rates.
✗ No onset or duration times for any treatment.
✗ No mild or moderate potassium tiers and no potassium numbers other than 6.5 and 6.0.
✗ No wording that has the nurse "give", "start", or "order" treatment on their own; treatments sit only inside the "PREPARE ORDERED TREATMENTS" node.
✗ No "AHA 2025" or any guideline citation on the non-arrest sequence.
✗ No sodium bicarbonate, no dextrose-only box, no oral binder shown as emergency first step.
✗ No reversed order: stabilize, shift, remove must read left to right in that order.
✗ No realistic ECG strip with measurable intervals or numbers.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Severity box shows exactly two rows: 6.5 or higher with or without ECG changes; 6.0 or higher with ECG changes
□ Arrest branch exits the decision diamond to "Activate cardiac arrest team" and "Standard resuscitation takes priority"
□ Sequence reads Recognize → Monitor → Call now → Prepare ordered treatments → Recheck
□ "By order or approved protocol" tag visible on the treatment node; nothing reads as nurse-initiated prescribing
□ Stabilize, shift, remove in that order, each with its monitoring line
□ No doses, no onset/duration times, no invented numbers
□ No AHA citation anywhere
□ Label spelling correct (hyperkalemia, beta-agonist, hypoglycemia)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 04-D ○ — Continuous therapy circuit (CVVH)
- **File:** images/nephrology-nursing-04-crrt-circuit.png
- **Placement:** Module 4, section `acute-krt` (Nursing care during acute hemodialysis and continuous therapy)
- **Job:** U — the learner can trace blood and fluid through a continuous therapy circuit and connect each part to what the nurse watches each hour.
- **Governing skill:** dialysis-circuit-schematic (locked topology; CVVH default)
- **Canvas:** 1672 × 941, 16:9
- **Alt text:** Continuous hemofiltration circuit from a right internal jugular dialysis catheter through blood pump and filter, replacement fluid route choice, effluent bag, and nursing watch points.
- **Caption:** In continuous hemofiltration, blood leaves through the red limb, is pumped up through the filter, and returns through the blue limb; replacement fluid joins the blood line, never the filter's side port. The nurse watches fluid balance, pressure trends, anticoagulation, temperature, electrolytes, and downtime around the clock.
- **Source of truth:** m04_x.py `acute-krt`: temporary non-tunneled dialysis catheter; site preference right internal jugular, then femoral, then left internal jugular, subclavian avoided; catheter for dialysis only; CRRT watch table — hourly fluid balance against prescribed net removal; circuit pressures and their trend (rising pressure across the filter warns of clotting; sudden access-pressure alarm suggests kinked or malpositioned catheter); anticoagulation (heparin or regional citrate); temperature (blood cools in the circuit; hypothermia; can hide a fever); electrolytes (potassium, phosphate, magnesium removed); medicines and nutrition; downtime recorded. m04.py `bedside`: CRRT = continuous renal replacement therapy, 24 hours a day, slow and steady, unstable circulation. Topology, port rules, colors, and catheter course from the dialysis-circuit-schematic skill. Removed from the skill template because the module does not state them: effluent dose 20–25 mL/kg/h, ~15% clearance loss with pre-dilution, filtration fraction 20–25%, IHD ~500 mL/min, blood pump "mL/min" label, and the five-modality legend.
- **Reviewer flags:** The module does not name CVVH or any CRRT sub-modality; the figure uses the circuit skill's CVVH default. Pre-/post-dilution and filtration fraction are not in the module; they are shown qualitatively only (no numbers) because the circuit skill locks them. Anticoagulation line (heparin or citrate) is deliberately not drawn, to keep the locked topology clean; confirm that is acceptable. The catheter tip at the SVC–right atrial junction is a circuit-skill anatomy rule, not module text.
- **Attach when generating:** /root/.claude/skills/synced/e7f3cdd9-a361-44a3-a710-a92e74c17604_d5a9b0e0-f0c3-4377-8b81-f15e9ba9cc14/dialysis-circuit-schematic/assets/catheter-hub-connection-reference.png (CORRECT-vs-WRONG hub connection reference; attach it to the ChatGPT message together with the prompt)

```text
Flat 2D medical schematic, 1672 × 941 landscape (16:9) — continuous renal replacement therapy (CRRT) circuit, shown as CVVH (continuous veno-venous hemofiltration). Two panels plus a bottom strip: (L) whole-circuit blood and replacement-fluid path, (R) hollow-fiber cutaway showing convective clearance, (bottom) what the nurse watches. White #ffffff background. An attached reference image shows correct versus wrong catheter hub connections; follow the CORRECT example.

════════════════════════════════════
LAYER A — CIRCUIT TRUTH BLOCK (supreme override)
- MODALITY IS CVVH: convective clearance. ONE replacement-fluid bag. NO dialysate bag anywhere. Both panels teach convection.
- Red = blood leaving the patient (arterial/access). Blue = blood returning (venous/return). Red and blue are used for blood only.
- REPLACEMENT FLUID (GREEN #2E6B3E): bag → replacement pump → THREE-WAY SELECTOR → EITHER the pre-dilution tee (red line, between blood pump and filter inlet) OR the post-dilution tee (blue line, just after the filter outlet). ONE ROUTE AT A TIME. Badge the selector "OR — select one route"; give both branches equal visual weight. Replacement NEVER enters a side port of the filter.
- AN INFUSION JOINS A LINE, IT DOES NOT REROUTE IT. Each green branch ends at its tee as a SHORT STUB meeting the blood line at a T. The blue line stays blue and unbroken from the filter's top cap to the blue hub; the red line stays red and unbroken from the red hub to the filter's bottom cap.
- EFFLUENT (TEAL #1A6B72): filter's LOWER SIDE PORT → effluent pump → waste bag. In CVVH the effluent is pure ultrafiltrate.
- UPPER SIDE PORT drawn CAPPED, labeled "Dialysate port — capped, not used here".
- ENDS ARE FOR BLOOD, SIDES ARE FOR FLUID. Bottom END CAP (red) = blood inlet; top END CAP (blue) = blood outlet. Side ports carry fluid only. The red line approaches the bottom cap FROM BELOW along the filter axis; the blue line leaves the top cap UPWARD along the same axis.
- CATHETER: temporary, non-tunneled, dual-lumen, in the RIGHT internal jugular vein — ONE catheter bifurcating into TWO limbs, each ending in a luer hub with a colored terminal cap (one RED, one BLUE), a clamp on each limb. Intravascular course translucent: internal jugular → brachiocephalic vein → superior vena cava, tip at the SVC–right atrial junction. Only the bifurcation and hubs sit outside the skin.
- Lines connect END-TO-END at the hub tips: one continuous tube of constant width, no gap, no side attachment, NO ARROWHEAD STANDING IN FOR A CONNECTION. No hub-tip zoom inset.
- HUB HEIGHTS MATCH LINE HEIGHTS: BLUE hub HIGH, level with the venous line along the top; RED hub LOW, level with the arterial line along the bottom. Same tubing style on both sides of each hub.
- FLIPPED LAYOUT: red arterial half along the BOTTOM, blue venous half along the TOP; blood ascends the filter.
- Blood path order (mandatory): patient (RED hub, low) → red line (bottom) → ACCESS PRESSURE (negative) → BLOOD PUMP (roller) → PRE-DILUTION TEE → PRE-FILTER PRESSURE → FILTER bottom cap → up inside fibers → top cap → blue line (top) → POST-DILUTION TEE → VENOUS PRESSURE → AIR DETECTOR → patient (BLUE hub, high).
- Anchor to landmarks: the venous pressure gauge sits immediately at the filter's blood outlet side, right after the post-dilution tee; the air detector sits immediately beside the patient's BLUE hub, the last thing blood passes. Nothing between the air detector and the blue hub.
- Blood pump on the RED side only. Pre-filter pressure tapped INLINE between pump and filter inlet.
- Arrows: red arrows patient → machine; blue arrows machine → patient.

════════════════════════════════════
LAYER B — SPATIAL ORIENTATION
- Left panel (about 62% width): patient head, neck, and upper chest at far left in simple light-gray outline, catheter in the right side of the neck with limbs splayed (blue hub high, red hub low). Red line along the bottom to the vertical filter at the right of the panel; blue line returns along the top. Replacement bag upper right with green line → replacement pump → selector → one tee. Effluent bag lower right.
- Right panel (about 38% width): standalone vertical filter cutaway, blood bottom → top, same orientation as the left-panel filter.
- Bottom strip (full width, about 14% height, soft gray #f3f4f6): six small icon-and-label chips.

════════════════════════════════════
LAYER C — RENDER SPECIFICATIONS
Component labels (medical term + plain-English gloss), verbatim:
- "Dialysis catheter, right internal jugular (temporary)"
- "Access pressure (suction on the draw line)"
- "Blood pump (moves blood through the circuit)"
- "Pre-filter pressure"
- "Hemofilter (hollow-fiber filter)"
- "Blood inlet" (bottom cap) and "Blood outlet" (top cap)
- "Dialysate port — capped, not used here"
- "Effluent (ultrafiltrate) out"
- "Venous pressure (push on the return line)"
- "Air detector (last guard before the patient)"
- "Replacement fluid"
- "Replacement pump"
- "OR — select one route"
- "Pre-dilution: longer filter life, less clearance"
- "Post-dilution: more clearance, more clotting"
- "Effluent pump (sets fluid removed)"
- "Waste bag"
- Small note near the filter, teal outline box: "Same filter, same machine: the port used decides the therapy."
Right panel cutaway labels, verbatim:
- Title: "Inside the filter: convection"
- "Blood rises inside the fibers"
- "Pressure pushes water across the wall"
- "Water drags solutes with it"
- "Cells and albumin stay in the blood"
- "Effluent (ultrafiltrate) out"
Arrows in the cutaway cross the fiber wall OUTWARD, perpendicular to blood flow; ultrafiltrate collects outside the fibers and drains to the lower side port. No fluid descending outside the fibers.
Bottom strip title: "What the nurse watches, every hour". Six chips, verbatim:
- "Hourly fluid balance vs prescribed removal"
- "Pressure trends: rising across filter = clotting"
- "Anticoagulation checks as ordered"
- "Temperature: blood cools in the circuit"
- "Electrolytes: potassium, phosphate, magnesium"
- "Downtime recorded"
Panel heading, top left: "Continuous kidney support (CRRT) circuit". Typeface: Inter for all text. Leader lines thin navy. Text navy #0f1e2e.
Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all structures and labels.

════════════════════════════════════
LAYER D — IMAGING PHYSICS
Not applicable — schematic.

════════════════════════════════════
LAYER E — NEGATIVE CONSTRAINTS
✗ No dialysate bag, dialysate line, or dialysate pump anywhere — this is CVVH.
✗ No countercurrent dialysate stream in the cutaway.
✗ No replacement fluid entering a side port of the filter.
✗ No permanently forked green line feeding both tees at once; no selector without the "OR — select one route" badge.
✗ No green segment replacing any stretch of blood line; no green continuing past a tee.
✗ No replacement line drawn teal; no effluent line drawn green.
✗ No blood line touching the side of the filter; no fluid line on an end cap.
✗ No arterial line meeting the filter at mid-height; it enters the bottom cap from below.
✗ No air detector before the venous pressure gauge, and nothing between the detector and the blue hub.
✗ No blood pump on the return side; no missing access, pre-filter, or venous pressure points; no pre-filter gauge on a side branch.
✗ No filter with blood descending.
✗ No line attached to the side of a hub; no arrowhead in place of a connection; no hub-tip zoom inset.
✗ No both hubs at mid-height; blue hub high, red hub low.
✗ No catheter tip in the neck, mid-SVC, or ventricle; no two separate catheters; no subclavian or femoral catheter.
✗ No numbers anywhere: no flow rates, doses, mL/kg/h, percentages, pressures, or filtration-fraction values.
✗ No modality legend listing CVVHD, CVVHDF, SCUF, or IHD.
✗ No anticoagulant or citrate line, no calcium line, no sampling port.
✗ No kidney drawn in the circuit; no red or blue on anything but blood.
✗ No dark background, no 3D render, no DM Sans, no serif font, no cartoon style, no garbled or placeholder text, no prompt text in the image.
✗ No missing or altered footer.

════════════════════════════════════
LAYER F — STYLE REFERENCE
Daugirdas Handbook of Dialysis; KDIGO 2012 AKI guideline. Flat vector schematic, white background, leader-line labels. Palette: navy #0f1e2e text; arterial red #C00000; venous blue #1F6FC0; replacement green #2E6B3E; effluent teal #1A6B72; card fill #f3f4f6. Typeface Inter. Footer "© renalcarematters.com".

════════════════════════════════════
LAYER G — QA (self-check before rendering)
□ No dialysate bag; cutaway shows outward convection
□ Green line: pump → selector → one tee, short stub, badge present
□ Blue continuous from top cap to blue hub; red continuous from red hub to bottom cap
□ Air detector last before the blue hub, after venous pressure
□ Blood pump on red side; pre-filter pressure inline
□ Blue hub high, red hub low; no arrowhead connections
□ Footer exactly "© renalcarematters.com"

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Header, bags, and cutaway agree: CVVH, no dialysate bag, outward convection arrows
□ Replacement fluid reaches the blood line only; selector badge "OR — select one route" present; both branches equal weight
□ Green branch is a short stub at the tee; no green replaces blood line or continues past a tee
□ Replacement green and effluent teal visually distinct
□ Upper side port capped and labeled "Dialysate port — capped, not used here"
□ Exactly four filter connections: two end caps (blood), two side ports (upper capped, lower effluent)
□ Arterial line enters the bottom cap from below; venous line leaves the top cap upward
□ Blood path order: access pressure → blood pump → pre-dilution tee → pre-filter pressure → filter → post-dilution tee → venous pressure → air detector → blue hub
□ Air detector is the last component before the patient
□ Blood pump on the red side only; three pressure points present and inline
□ Blue hub high, red hub low; trace each line hub to filter without a gap or arrowhead substitute
□ Catheter in the right internal jugular, course to the SVC–right atrial junction, red and blue terminal caps, clamps
□ Red arrows patient → machine; blue arrows machine → patient
□ Bottom strip shows all six watch items, verbatim
□ No numbers anywhere (no rates, doses, percentages, pressures)
□ No modality legend and no anticoagulant line
□ Label spelling correct throughout; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---


---

## Module 5 — Kidney Failure Treatment Choices

### 05-A — Four roads: the pathways compared
- **File:** images/nephrology-nursing-05-four-roads.png
- **Placement:** Module 5, section `compare` (The pathways compared, in the terms patients ask about); the mental model is in `model` (Four roads, one traveler)
- **Job:** U/P — the learner can describe all four pathways with equal weight, in the terms patients ask about, and sees that none is the default.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, extended to four equal columns)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Four equal columns comparing in-center hemodialysis, peritoneal dialysis, kidney transplant, and conservative kidney management by where, how often, who does the work, and daily life.
- **Caption:** Each pathway has its own toll, and none is right for everyone; the nurse's job is to make all four visible in the same level of detail. People often move between pathways over a lifetime.
- **Source of truth:** m05.py `model` (four roads, one traveler; none is right for everyone; nurse is the guide). m05.py `physiology` (dialysis removes water and small wastes and corrects potassium and acid but does not make erythropoietin or activate vitamin D; transplant — a donor kidney takes over all kidney functions; CKM — no dialysis, active treatment of symptoms and complications; often misunderstood as "doing nothing"). m05_x.py `compare` table: HD — at a unit, usually 3 times a week, about 4 hours each; nurses and technicians; strictest limits on fluid, potassium, and phosphate; tied to the unit schedule. PD — at home, every day; 3 to 5 manual exchanges or overnight by machine; the patient or a caregiver; usually more liberal; flexible, supplies travel with the patient. Transplant — one operation; clinic visits, frequent at first; the patient, taking medicines daily for life; close to normal, with food-safety rules; most freedom once stable. CKM — clinic or home visits as needed; the patient and family, with the care team; adjusted for comfort and symptoms; no treatment schedule. "The pathways are not exclusive or permanent."
- **Reviewer flags:** none
- **Attach when generating:** none

```text
Medical education comparison infographic, 1792 × 1024 landscape (16:9). Subject: the four treatment pathways for kidney failure, compared with EQUAL visual weight. AJKD-style graphical abstract, flat vector with simple line icons, white #ffffff background.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "Four roads, one traveler"
- Subtitle, teal #1a6b72: "Kidney failure treatment pathways, in the terms patients ask about"
- Below: four columns of IDENTICAL width and height, rounded cards on soft gray #f3f4f6, separated by even gutters. Each card has a thin colored top band (all four bands in the SAME teal #1a6b72 so no column looks preferred), a simple line icon, a bold column title, and five labeled rows. Row labels appear at the far left of the canvas as a thin navy row-header column, aligned across all four cards.
- Row headers (left margin, small caps navy): "Where and how often", "What it does", "Who does the work", "Diet and fluid", "Travel and work"

Column 1 — icon: reclining dialysis chair with a dialysis machine. Title: "In-center hemodialysis"
  Where and how often: "At a unit, usually 3 times a week, about 4 hours each"
  What it does: "Cleans blood through a dialyzer"
  Who does the work: "Nurses and technicians"
  Diet and fluid: "Strictest limits on fluid, potassium, phosphate"
  Travel and work: "Tied to the unit schedule"

Column 2 — icon: house with a fluid bag on a stand. Title: "Peritoneal dialysis"
  Where and how often: "At home, every day; 3 to 5 manual exchanges or overnight by machine"
  What it does: "Abdominal lining acts as the filter"
  Who does the work: "The patient or a caregiver"
  Diet and fluid: "Usually more liberal"
  Travel and work: "Flexible; supplies travel with you"

Column 3 — icon: kidney with a small medicine bottle. Title: "Kidney transplant"
  Where and how often: "One operation; clinic visits, frequent at first"
  What it does: "Donor kidney takes over all functions"
  Who does the work: "The patient, medicines daily for life"
  Diet and fluid: "Close to normal, with food-safety rules"
  Travel and work: "Most freedom once stable"

Column 4 — icon: house with a family member and a clinician beside a seated older person. Title: "Conservative kidney management"
  Small teal pill tag under the title: "Active care, not “doing nothing”"
  Where and how often: "Clinic or home visits as needed"
  What it does: "No dialysis; treats symptoms and complications"
  Who does the work: "Patient and family, with the care team"
  Diet and fluid: "Adjusted for comfort and symptoms"
  Travel and work: "No treatment schedule"

- Thin note spanning columns 1 and 2 beneath them, gray-navy italic: "Dialysis does not make erythropoietin or activate vitamin D"
- Bottom strip, full width, light teal #eef6f7, navy text, with a small two-way arrow icon: "Not exclusive or permanent: many people move between roads."

Every label verbatim (render exactly these and nothing else): all strings in quotation marks above, exactly as written.

Colors: navy #0f1e2e text; teal #1a6b72 bands, tag, and accents; card fill #f3f4f6; bottom strip #eef6f7. No green "good" or red "bad" coding of any column. Typeface: Inter throughout; body text at least 12 pt equivalent. Generous whitespace.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the bottom strip and clear of it.

DO NOT:
✗ No column larger, brighter, first-highlighted, or labeled "recommended" or "best".
✗ No ranking, stars, check marks, or traffic-light colors across columns.
✗ No survival percentages, costs, peso amounts, PhilHealth figures, or waiting times.
✗ No numbers other than "3 times a week", "about 4 hours", and "3 to 5".
✗ No "hospice" or "end of life" wording on the conservative column.
✗ No photorealistic people, no patients in distress, no needles or blood.
✗ No hemodiafiltration, plasma exchange, or home hemodialysis column.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Four columns identical in size, color, and emphasis; no column reads as default
□ HD cell reads "usually 3 times a week, about 4 hours each"; PD cell reads "3 to 5 manual exchanges or overnight by machine"
□ Conservative column carries the "Active care, not “doing nothing”" tag
□ Row headers aligned across all four columns
□ Erythropoietin/vitamin D note sits under the two dialysis columns only
□ Bottom strip states roads are not exclusive or permanent
□ No invented numbers, costs, or survival figures
□ Label spelling correct (hemodialysis, peritoneal, erythropoietin)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 05-B — Preparation timeline as kidney function falls
- **File:** images/nephrology-nursing-05-preparation-timeline.png
- **Placement:** Module 5, section `timing` (When treatment starts, and how far ahead to prepare)
- **Job:** A — the learner knows what to prepare, and how far ahead, so the start is planned rather than an emergency.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal sequence adapted to a timeline)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Timeline from stage 3 to the start of kidney replacement showing education, vein preservation, transplant referral, fistula, PD catheter, hepatitis B vaccination, and social work.
- **Caption:** Starting dialysis is a clinical decision made on symptoms and complications, not on a single number, so preparation happens early. An unplanned start through a temporary catheter is associated with more infections, longer hospital stays, and worse early survival.
- **Source of truth:** m05_x.py `timing`: start "when symptoms or complications attributable to kidney failure appear" (persistent nausea and weight loss, fluid overload or uncontrolled blood pressure, itching, cognitive slowing, pericarditis); "Starting is a clinical decision, not a number." Preparation table — Education about all pathways: from stage 4; Transplant referral: 6 to 12 months before dialysis is expected (txcand2020); Vein preservation: from stage 3 or 4, for life; Fistula creation: several months before expected start (needs weeks to months to mature); PD catheter: at least 2 weeks before use where possible; Hepatitis B vaccination: as early as possible; Social work and benefits assessment: before the start. Unplanned start through a temporary catheter associated with more infections, longer hospital stays, worse early survival.
- **Reviewer flags:** The module also states that start "in practice is often when estimated filtration is between 5 and 10 mL/min/1.73 m²"; deliberately left off the figure so it does not read as a trigger threshold. Add only if the reviewer wants it. The timeline is drawn not to scale.
- **Attach when generating:** none

```text
Clinical education timeline infographic, 1792 × 1024 landscape (16:9). Subject: preparing for kidney failure treatment as kidney function falls. Flat vector, white #ffffff background, clean horizontal timeline with milestone bars, simple line icons.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "Prepare early, start on purpose"
- Subtitle, teal #1a6b72: "What to prepare as kidney function falls"
- A long horizontal axis arrow across the middle of the canvas, running left to right, drawn as a gradient band from light teal #eef6f7 to deeper teal #1a6b72. Above the axis, small labels at evenly spaced points: "Stage 3", "Stage 4", "Stage 5", and at the far right end a navy flag icon labeled "Planned start". Axis caption under the left end: "Kidney function falling →". Small gray tag at the right end of the axis: "Not to scale".
- Seven milestone bars stacked in rows above and below the axis (like a Gantt chart), each a rounded bar with a small icon at its left end, a bold label, and its lead time in teal. Positions:
  1. Bar starting at the far left (before Stage 3), short, syringe icon: "Hepatitis B vaccination" / "As early as possible"
  2. Long bar starting between Stage 3 and Stage 4 and running past "Planned start" off the right edge with an arrowhead, arm icon: "Vein preservation" / "From stage 3 or 4, for life"
  3. Bar starting at Stage 4 and running to Planned start, speech-bubble icon: "Education about all pathways" / "From stage 4"
  4. Bar beginning in mid Stage 4–5 region, kidney icon: "Transplant referral" / "6 to 12 months before dialysis expected"
  5. Bar in late Stage 5 region, vessel icon: "Fistula creation" / "Several months before start"
  6. Short bar just before Planned start, catheter icon: "PD catheter" / "At least 2 weeks before use"
  7. Bar ending at Planned start, people icon: "Social work and benefits" / "Before the start"
- Right side panel (about 22% width), rounded card, navy outline, heading "When does treatment start?": "On symptoms or complications, not a number" then four small bullet chips: "Persistent nausea, weight loss" · "Fluid overload or uncontrolled blood pressure" · "Itching, cognitive slowing" · "Pericarditis"
- Bottom strip, full width, split in two:
  Left half, light teal #eef6f7, green check icon: "Planned start: access ready, choice made"
  Right half, very light red tint, red caution icon #b91c1c: "Unplanned start via temporary catheter: more infections, longer stays"

Every label verbatim (render exactly these and nothing else): "Prepare early, start on purpose"; "What to prepare as kidney function falls"; "Stage 3"; "Stage 4"; "Stage 5"; "Planned start"; "Kidney function falling →"; "Not to scale"; "Hepatitis B vaccination"; "As early as possible"; "Vein preservation"; "From stage 3 or 4, for life"; "Education about all pathways"; "From stage 4"; "Transplant referral"; "6 to 12 months before dialysis expected"; "Fistula creation"; "Several months before start"; "PD catheter"; "At least 2 weeks before use"; "Social work and benefits"; "Before the start"; "When does treatment start?"; "On symptoms or complications, not a number"; "Persistent nausea, weight loss"; "Fluid overload or uncontrolled blood pressure"; "Itching, cognitive slowing"; "Pericarditis"; "Planned start: access ready, choice made"; "Unplanned start via temporary catheter: more infections, longer stays".

Colors: navy #0f1e2e text; teal #1a6b72 lead times and axis; milestone bars in soft teal #cfe6e8 with navy text; renal green #1f7a4d only for the planned-start check; clinical red #b91c1c only for the unplanned caution icon. Typeface: Inter throughout. Generous whitespace; bars must not overlap text.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the bottom strip.

DO NOT:
✗ No eGFR numbers, no mL/min values, no "start at 15" or any start threshold.
✗ No month or week tick marks on the axis; only the stage labels shown.
✗ No lead times other than those written above.
✗ No vein preservation bar that ends before the right edge — it continues "for life".
✗ No calendar dates, ages, or costs.
✗ No photographs, no needles in skin, no surgery scenes.
✗ No implication that one pathway is required; no "dialysis" as the only end point label.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ All seven milestones present with their exact lead times
□ Transplant referral reads "6 to 12 months before dialysis expected"; PD catheter reads "At least 2 weeks before use"
□ Vein preservation bar runs past the planned start and off the edge
□ Axis carries only Stage 3, Stage 4, Stage 5, Planned start, and "Not to scale"
□ Start panel says "On symptoms or complications, not a number" with the four symptom chips
□ No eGFR or start-threshold numbers anywhere
□ Planned vs unplanned contrast strip present
□ Label spelling correct (hepatitis, pericarditis, preservation)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 05-C — Structuring the shared-decision conversation
- **File:** images/nephrology-nursing-05-shared-decision.png
- **Placement:** Module 5, section `sdm` (Structuring the conversation)
- **Job:** A — the learner can run the three-step conversation, with the nursing task and a usable phrase for each step.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal step sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three-step shared decision conversation: introduce the choice, describe the options, help the patient weigh them, with nurse phrases and common fears.
- **Caption:** Shared decision-making runs in three steps, and the decision does not have to be made in one visit. Ask the patient early and privately how much they want to know and who they want involved.
- **Source of truth:** m05_x.py `sdm`: three steps — 1 Introduce the choice (there is a decision to make, more than one reasonable option, the patient's priorities guide it; many patients do not realize they have a say); 2 Describe the options (same headings for each; check understanding with teach-back; pictures, a unit visit, or talking with a patient on that treatment); 3 Help the patient weigh them (what a good day looks like, what they most want to keep doing, what they most want to avoid; reflect back "It sounds as though staying at home matters more to you than avoiding daily tasks"; give time; a decision does not have to be made in one visit). Filipino families: ask the patient directly, early and privately, how much they want to know and who they want involved; "Tell my daughter and she will decide" is the patient's choice and is documented. Common fears: "Dialysis is a death sentence." "I will be a burden." "The needles." "We cannot afford it." "If I choose no dialysis, the doctors will abandon me." m05.py `bedside`: teach-back prompt "To check that I explained it clearly, can you tell me in your own words…"; nurse documents what is said. m05.py `practice`: documents the conversation including what the patient said in their own words.
- **Reviewer flags:** The image plan described four stages (elicit values → explain options → deliberate → decide and document); the module text has three steps, so the figure follows the module. "Document in the patient's own words" is drawn from the `bedside` and `practice` sections as a closing band.
- **Attach when generating:** none

```text
Clinical education step-sequence infographic, 1792 × 1024 landscape (16:9). Subject: how a nurse structures a shared decision-making conversation about kidney failure treatment. Flat vector, white #ffffff background, warm and calm, simple line icons, no photographs.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "The shared decision conversation"
- Subtitle, teal #1a6b72: "Three steps, each with a nursing task"
- Opening band (full width, thin, light teal #eef6f7, small icon of two chairs at eye level): "First, ask privately: how much to know, who to involve?"
- Three large rounded step cards in one horizontal row on a soft gray #f3f4f6 panel, joined by bold navy right-pointing arrows. Each card: a teal numbered circle, a bold step title, a small icon, a "Nurse task" line, and one speech bubble with an example phrase in navy italic.
  Card 1 — icon: signpost with several arrows. Title: "1 · Introduce the choice"
    Nurse task: "There is a decision; your priorities guide it"
    Speech bubble: "More than one option is reasonable."
  Card 2 — icon: four equal tiles. Title: "2 · Describe the options"
    Nurse task: "Same headings for every option"
    Second line: "Check with teach-back"
    Speech bubble: "Can you tell me in your own words?"
  Card 3 — icon: balance scale. Title: "3 · Help them weigh it"
    Nurse task: "Ask, then reflect back"
    Three small prompt chips: "What does a good day look like?" · "What do you want to keep doing?" · "What do you most want to avoid?"
    Speech bubble: "It sounds as though staying at home matters most."
- Closing band (full width, light teal #eef6f7) with two parts separated by a divider: clock icon "Give time: not one visit" and pen icon "Document the patient's own words"
- Bottom strip, soft amber tint, heading in amber #b8860b: "Fears worth naming" followed by five small rounded quote chips in navy: "Dialysis is a death sentence." · "I will be a burden." · "The needles." · "We cannot afford it." · "The doctors will abandon me."

Every label verbatim (render exactly these and nothing else): "The shared decision conversation"; "Three steps, each with a nursing task"; "First, ask privately: how much to know, who to involve?"; "1 · Introduce the choice"; "There is a decision; your priorities guide it"; "More than one option is reasonable."; "2 · Describe the options"; "Same headings for every option"; "Check with teach-back"; "Can you tell me in your own words?"; "3 · Help them weigh it"; "Ask, then reflect back"; "What does a good day look like?"; "What do you want to keep doing?"; "What do you most want to avoid?"; "It sounds as though staying at home matters most."; "Give time: not one visit"; "Document the patient's own words"; "Fears worth naming"; "Dialysis is a death sentence."; "I will be a burden."; "The needles."; "We cannot afford it."; "The doctors will abandon me."; "Nurse task" (as the small label before each task line).

Colors: navy #0f1e2e text and arrows; teal #1a6b72 step numbers and subtitle; card fills white on a #f3f4f6 panel; bands #eef6f7; amber #b8860b only for the fears heading. Typeface: Inter throughout; step titles bold, at least 18 pt equivalent. Generous whitespace.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the fears strip.

DO NOT:
✗ No fourth step card; exactly three numbered steps.
✗ No "Decide" box that implies the nurse makes the choice.
✗ No yes/no question bubbles such as "Do you understand?".
✗ No names of specific treatments ranked or recommended.
✗ No numbers, percentages, survival figures, or costs.
✗ No photographs, no faces with distress, no dialysis machines.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Exactly three step cards, titled Introduce the choice, Describe the options, Help them weigh it
□ Opening band about asking privately is present before step 1
□ Teach-back phrase is open ("in your own words"), not yes/no
□ Step 3 shows the three prompt chips and the reflect-back bubble
□ Closing band shows "Give time: not one visit" and "Document the patient's own words"
□ Five fear chips present, spelled exactly
□ No invented numbers and no treatment ranking
□ Label spelling correct throughout
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---


---

## Module 6 — Hemodialysis Principles, Prescription, and Adequacy

### 06-A — Three transport processes
- **File:** images/nephrology-nursing-06-transport-processes.png
- **Placement:** Module 6, section `physiology` (Three transport processes); analogy introduced in `model` (A tea bag and a press)
- **Job:** U — the learner names the driving force of diffusion, ultrafiltration, and convection and sees each analogy walked back to the dialyzer membrane.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three panels showing diffusion as a tea bag, ultrafiltration as a coffee press, and convection, each mapped to the dialyzer membrane with driving force and what moves.
- **Caption:** Diffusion removes urea and potassium down a concentration gradient; ultrafiltration removes water by pressure; convection carries larger solutes along with that water. In the dialyzer, fresh dialysate flows opposite to the blood, so the gradient never runs out.
- **Source of truth:** m06.py `model` (tea bag in water — difference in concentration does the work = diffusion, removes urea and potassium; coffee press — pressure does the work = ultrafiltration, removes water; correction: fresh dialysis fluid flows continuously in the opposite direction to the blood so the concentration difference is maintained along the whole length of the fibers). m06.py `physiology` table: Diffusion — concentration gradient; small solutes: urea, creatinine, potassium; bicarbonate moves into the blood; increased by higher blood and dialysate flow, larger membrane, longer time. Ultrafiltration — pressure gradient across the membrane; plasma water; higher transmembrane pressure, more permeable membrane. Convection — solutes carried along with ultrafiltered water; larger "middle" molecules; larger ultrafiltration volumes, as in hemodiafiltration. Dialysate: no urea, potassium below the patient's, bicarbonate above. Water removal ceiling: refilling from tissues is limited; risk depends on rate per kilogram. No numbers used.
- **Reviewer flags:** The module gives no everyday analogy for convection; the convection panel uses a plain picture ("water drags solutes along") rather than an invented analogy.
- **Attach when generating:** none

```text
Publication-grade biomedical mechanism schematic, 1792 × 1024 landscape (16:9). Subject: the three transport processes of hemodialysis — diffusion, ultrafiltration, convection — each paired with an everyday picture and walked back to the dialyzer membrane. Review-article style, flat vector with soft semi-3D shading, white #ffffff background.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "How a dialyzer moves solutes and water"
- Subtitle, teal #1a6b72: "Three processes, three driving forces"
- Three equal vertical columns. Each column has three tiers:
  TOP tier — everyday picture in a small rounded frame;
  MIDDLE tier — a dashed magnified box showing a short section of semipermeable membrane drawn as a vertical wall with pores, BLOOD SIDE on the left (light red tint, label "Blood side") and DIALYSATE SIDE on the right (light teal tint, label "Dialysate side");
  BOTTOM tier — three compact label rows: "Force:", "Moves:", "Increased by:".

Column 1 — heading "Diffusion"
  Top picture: a tea bag in a clear cup, color spreading from the bag into the water. Caption: "Tea bag: color spreads on its own"
  Middle membrane: small navy dots labeled "Urea" and small purple dots labeled "Potassium" crossing from blood side to dialysate side through pores (arrows left → right); small teal dots labeled "Bicarbonate" crossing from dialysate side into blood (arrow right → left). Tiny note on the dialysate side: "No urea, less potassium, more bicarbonate"
  Force: "Concentration gradient"
  Moves: "Urea, creatinine, potassium out"
  Increased by: "Flow, membrane size, time"

Column 2 — heading "Ultrafiltration"
  Top picture: a coffee press with the plunger being pushed down, water forced through the mesh. Caption: "Coffee press: pressure pushes water"
  Middle membrane: a wide navy pressure arrow on the blood side labeled "Pressure", small blue water droplets crossing left → right labeled "Plasma water"
  Force: "Pressure across the membrane"
  Moves: "Plasma water"
  Increased by: "Higher transmembrane pressure"

Column 3 — heading "Convection"
  Top picture: plain diagram of a stream of water droplets carrying a few larger particles with it through a mesh. Caption: "Water drags solutes along"
  Middle membrane: water droplets crossing left → right, with larger orange particles labeled "Middle molecules" riding along with the water through larger pores
  Force: "Solutes carried with water"
  Moves: "Larger “middle” molecules"
  Increased by: "Larger ultrafiltration volumes"

- Bottom strip, full width, light teal #eef6f7, split in two:
  Left: small schematic of one hollow fiber with a red arrow pointing right inside the fiber and a teal arrow pointing left outside it, labeled "Countercurrent: dialysate flows opposite to blood" and, beneath, "The gradient never runs out"
  Right: small icon of a draining beaker refilled by a thinner arrow, labeled "Water removal has a ceiling" and, beneath, "Tissues refill blood at a limited rate"

Every label verbatim (render exactly these and nothing else): all strings in quotation marks above, exactly as written.

Colors: navy #0f1e2e text; teal #1a6b72 headings and dialysate tint; blood side light red tint with red #C00000 accents; purple #6c3d8e potassium dots; orange #C55A11 middle molecules; blue #1F6FC0 water droplets. Typeface: Inter throughout. Thin dashed gray borders on the magnified boxes, generous whitespace.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of the bottom strip content.

DO NOT:
✗ No arrows showing urea moving into the blood or bicarbonate leaving the blood.
✗ No same-direction (co-current) arrows in the countercurrent schematic.
✗ No osmosis label and no "glucose draws water" message (that is peritoneal dialysis).
✗ No red blood cells or albumin crossing the membrane.
✗ No numbers: no flow rates, pore sizes, pressures, mL/kg/h, or molecular weights.
✗ No convection analogy involving tea or coffee; convection uses only the plain stream picture.
✗ No dialysis machine or full circuit in this figure.
✗ No dark background, no serif font, no cartoon faces on molecules, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Diffusion arrows: urea, creatinine/potassium blood → dialysate; bicarbonate dialysate → blood
□ Ultrafiltration shows a pressure arrow and water crossing; no solute emphasis
□ Convection shows larger "middle molecules" carried with water through the membrane
□ Each column has Force, Moves, Increased by rows with the exact text
□ Blood side and dialysate side labeled correctly in every membrane box
□ Countercurrent schematic shows opposite arrows inside and outside the fiber
□ "Water removal has a ceiling" note present
□ No invented numbers; label spelling correct (ultrafiltration, bicarbonate, transmembrane)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 06-B — The hemodialysis blood circuit on an arteriovenous fistula
- **File:** images/nephrology-nursing-06-hd-circuit-fistula.png
- **Placement:** Module 6, section `circuit` (The blood circuit, step by step, and what each pressure means); cutaway supports `dialyzer` (Inside the dialyzer)
- **Job:** U — the learner can trace blood from arterial needle to venous needle, place each pressure sensor relative to the pump, and see countercurrent flow in the dialyzer.
- **Governing skill:** dialysis-circuit-schematic (IHD, diffusive, countercurrent; adapted from catheter to arteriovenous fistula); Constitution v1.0 Layer A AV fistula rules
- **Canvas:** 1672 × 941, 16:9
- **Alt text:** Hemodialysis circuit from forearm fistula arterial needle through pressure sensor, blood pump, heparin line, dialyzer, venous chamber, air detector, to venous needle, with countercurrent cutaway.
- **Caption:** Everything before the blood pump is pulled, so arterial pressure reads below zero; everything after is pushed, so venous pressure reads above zero. Blood and dialysate run in opposite directions through the dialyzer, and the air detector is the last guard before blood returns.
- **Source of truth:** m06_x.py `circuit`: one pump; before the pump pressure below zero, after the pump above zero; order — 1 arterial needle (blood leaves; "arterial" names direction, not vessel); 2 arterial (pre-pump) pressure monitor, reads negative; 3 blood pump (roller), displayed flow calculated from pump speed; 4 dialyzer, blood inside hollow fibers, dialysate around them, anticoagulant when ordered usually infused before the dialyzer; 5 venous drip chamber (traps air and clots), air detector below it that stops the pump and closes the venous clamp, never bypassed; 6 venous pressure monitor measured at the drip chamber, positive, mostly from needle resistance; venous needle. Transmembrane pressure is calculated, not measured at one point. m06_x.py `dialyzer`: blood enters and leaves through end caps; dialysate through two side ports; countercurrent; co-current connection lowers clearance without any alarm; thousands of hollow fibers. m06.py `bedside`: needles placed too close together or reversed lines cause recirculation. m06_x.py `measuring`: needles well apart and correctly oriented limit recirculation. m06.py `quiz`/m06_x.py `QUIZ`: forearm fistula. Circuit-skill invariants: blood pump on arterial side; end caps blood, side ports dialysate; dialysate in at the side port nearest the blood outlet; air detector last before the venous needle; flipped layout. No flows, pressures, or numbers.
- **Reviewer flags:** The module lists the venous drip chamber, air detector, and venous clamp together, with venous pressure measured at the chamber; the figure places the pressure transducer on the chamber and the air detector plus clamp below it as the last component before the venous needle. No pre-dialyzer pressure monitor is drawn because the module does not describe one. Arterial needle tip direction is not stated in Module 6; the figure fixes position (nearer the anastomosis, needles well apart) and leaves arterial bevel direction to Module 7 and unit practice; confirm.
- **Attach when generating:** none. The bundled catheter-hub reference applies to catheter circuits only; this circuit uses fistula needles.

```text
Flat 2D medical schematic, 1672 × 941 landscape (16:9) — chronic intermittent hemodialysis (IHD) circuit on a forearm arteriovenous fistula. Diffusive therapy with countercurrent dialysate. Two panels: (L) whole blood circuit from arterial needle to venous needle, (R) dialyzer cutaway showing countercurrent diffusion. White #ffffff background.

════════════════════════════════════
LAYER A — CIRCUIT AND ANATOMY TRUTH BLOCK (supreme override)
- MODALITY IS IHD: diffusion with countercurrent dialysate. ONE dialysate supply line in, ONE spent-dialysate line out to drain. NO replacement-fluid bag, NO replacement pump, NO pre- or post-dilution tee anywhere.
- ACCESS IS A FOREARM ARTERIOVENOUS FISTULA, NOT A CATHETER. Draw the patient's forearm VERTICALLY at the far left of the panel: hand and wrist at the BOTTOM, elbow toward the TOP (the heart is upward). At the wrist, a radial artery (red, thick-walled) joins a cephalic vein side-to-end at a small labeled anastomosis. The arterialized vein (wider, slightly bluish-purple, thin-walled) runs UP the forearm toward the elbow; blood in the fistula flows upward, shown by small arrows inside the vein.
- TWO NEEDLES in the fistula vein, WELL APART:
  · ARTERIAL needle LOWER, closer to the anastomosis (upstream). Its tubing is RED.
  · VENOUS needle HIGHER, toward the elbow (downstream), its tip pointing UP toward the heart, in the direction of fistula flow. Its tubing is BLUE.
- HEIGHTS MATCH LINES: the arterial needle (low) connects to the red line running along the BOTTOM; the venous needle (high) connects to the blue line running along the TOP. Each needle's tubing joins its line as one continuous tube of constant width, no gap, no arrowhead standing in for a connection.
- Red = blood leaving the patient. Blue = blood returning. Red and blue are used for blood only.
- FLIPPED LAYOUT: red half along the BOTTOM, blue half along the TOP; blood ASCENDS the dialyzer.
- Blood path order (mandatory): ARTERIAL NEEDLE (low) → red line (bottom) → ARTERIAL PRESSURE monitor (pre-pump, negative) → BLOOD PUMP (roller) → HEPARIN LINE joining as a short stub from a small syringe pump → DIALYZER bottom end cap → up inside the fibers → top end cap → blue line (top) → VENOUS DRIP CHAMBER with VENOUS PRESSURE transducer on top of it → AIR DETECTOR with VENOUS CLAMP directly below the chamber → VENOUS NEEDLE (high).
- Anchor to landmarks: the arterial pressure monitor sits immediately beside the arterial needle's tubing, before the pump; the drip chamber sits immediately after the dialyzer's top cap; the air detector and clamp sit immediately beside the venous needle, the last thing blood passes. Nothing between the air detector/clamp and the venous needle.
- Blood pump on the RED (arterial) side only. Heparin joins AFTER the pump and BEFORE the dialyzer.
- ENDS ARE FOR BLOOD, SIDES ARE FOR DIALYSATE. Bottom END CAP (red) = blood in; top END CAP (blue) = blood out. Red line approaches the bottom cap FROM BELOW along the dialyzer axis; blue line leaves the top cap UPWARD.
- COUNTERCURRENT: fresh dialysate ENTERS at the UPPER side port (nearest the blood outlet) and EXITS at the LOWER side port (nearest the blood inlet). Dialysate flows DOWN outside the fibers while blood flows UP inside them. Dialysate lines are TEAL.
- Transmembrane pressure is CALCULATED, shown as a small bracket spanning the membrane, not as a gauge on any line.
- Arrows: red arrows patient → machine; blue arrows machine → patient; teal arrows along dialysate lines.

════════════════════════════════════
LAYER B — SPATIAL ORIENTATION
- Left panel (about 64% width): forearm vertical at far left; red line along the bottom from the arterial needle to the dialyzer, which stands vertically at the right of the panel; blue line along the top from the dialyzer back to the venous needle. A soft pale-red tint behind the segment from arterial needle to blood pump labeled "Pulled: pressure below zero"; a soft pale-blue tint behind the segment from blood pump onward labeled "Pushed: pressure above zero". Dialysate supply enters from a machine box at the upper right; drain line leaves at the lower right.
- Right panel (about 36% width): standalone vertical dialyzer cutaway, same orientation, a few representative hollow fibers enlarged.

════════════════════════════════════
LAYER C — RENDER SPECIFICATIONS
Left-panel labels (medical term + plain gloss), verbatim:
- "Forearm fistula"
- "Anastomosis (artery joined to vein)"
- "Arterial needle (blood leaves)"
- "Venous needle (blood returns)"
- "Needles well apart"
- "Arterial pressure (before pump: negative)"
- "Blood pump (roller)"
- "Heparin line (when ordered)"
- "Dialyzer"
- "Venous drip chamber (traps air, clots)"
- "Venous pressure (positive)"
- "Air detector and clamp (never bypassed)"
- "Fresh dialysate in"
- "Spent dialysate to drain"
- "Transmembrane pressure (calculated)"
- "Pulled: pressure below zero"
- "Pushed: pressure above zero"
- Small gray note under the forearm: "“Arterial” means away from the patient"
Right-panel labels, verbatim:
- Title: "Inside the dialyzer: countercurrent"
- "Blood in (end cap)" at the bottom red cap; "Blood out (end cap)" at the top blue cap
- "Dialysate in (side port)" at the upper side port; "Dialysate out (side port)" at the lower side port
- "Blood flows up inside fibers"
- "Dialysate flows down outside"
- Inside one enlarged fiber wall: small dots "Urea" and "Potassium" crossing outward; "Bicarbonate" crossing inward
- Caution chip at the bottom of the panel, amber outline: "Same-direction connection: less clearance, no alarm"
Panel heading, top left: "Hemodialysis blood circuit". Typeface: Inter for all text. Thin navy leader lines. Text navy #0f1e2e.
Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all structures and labels.

════════════════════════════════════
LAYER D — IMAGING PHYSICS
Not applicable — schematic.

════════════════════════════════════
LAYER E — NEGATIVE CONSTRAINTS
✗ No catheter, no neck line, no hub caps — the access is a forearm fistula with two needles.
✗ No replacement-fluid bag, green line, pre-dilution or post-dilution tee.
✗ No blood pump on the blue return side.
✗ No heparin line joining before the pump or into the blue line.
✗ No air detector before the drip chamber, and nothing between the air detector/clamp and the venous needle.
✗ No air detector on the red line.
✗ No blood line touching the side of the dialyzer; no dialysate line on an end cap.
✗ No dialysate entering at the lower side port; no dialysate flowing in the same direction as blood.
✗ No blood descending in the dialyzer; bottom cap red, top cap blue.
✗ No needles placed side by side or touching; no venous needle below the arterial needle.
✗ No venous needle pointing toward the wrist or anastomosis.
✗ No fistula drawn as an artery-to-artery or vein-to-vein loop; artery thick-walled red, vein wide and thin-walled.
✗ No pre-dialyzer pressure gauge and no transmembrane pressure gauge on a line.
✗ No numbers anywhere: no blood flow, dialysate flow, pressure values, mmHg, alarm limits, needle gauges, or times.
✗ No arrowhead substituting for a tube connection; no dangling line ends.
✗ No red or blue on anything but blood; no teal on blood lines.
✗ No kidney drawn anywhere; no realistic machine screen with readable text.
✗ No dark background, no 3D render, no DM Sans, no serif font, no cartoon style, no garbled or placeholder text, no prompt text in the image.
✗ No missing or altered footer.

════════════════════════════════════
LAYER F — STYLE REFERENCE
Daugirdas Handbook of Dialysis; KDOQI 2015 hemodialysis adequacy update. Flat vector schematic, white background, leader-line labels. Palette: navy #0f1e2e text; arterial red #C00000; venous blue #1F6FC0; dialysate teal #1A6B72; amber #b8860b caution chip; zone tints very pale red and very pale blue. Typeface Inter. Footer "© renalcarematters.com".

════════════════════════════════════
LAYER G — QA (self-check before rendering)
□ Forearm vertical; arterial needle low near anastomosis, venous needle high, tip toward heart, needles apart
□ Pump on red side; heparin after pump, before dialyzer
□ Drip chamber with venous pressure, then air detector and clamp, then venous needle
□ Blood up inside fibers; dialysate in upper side port, out lower side port
□ No numbers; footer exactly "© renalcarematters.com"

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Access is a forearm fistula with two needles; no catheter anywhere
□ Anastomosis at the wrist; fistula vein runs up toward the elbow with upward flow arrows
□ Arterial needle lower (nearer the anastomosis), venous needle higher; needles clearly apart
□ Venous needle tip points toward the heart
□ Red line along the bottom from arterial needle; blue line along the top to venous needle; both continuous, no arrowhead substitutes
□ Arterial pressure sits before the pump and is labeled negative
□ Blood pump on the red side only
□ Heparin line joins after the pump and before the dialyzer, as a short stub
□ Venous drip chamber right after the dialyzer outlet, venous pressure labeled positive at the chamber
□ Air detector and clamp are the last component before the venous needle
□ Dialyzer: blood enters bottom end cap, exits top end cap; no blood line on a side wall
□ Dialysate enters the upper side port (near blood outlet) and leaves the lower side port; teal lines
□ Cutaway shows blood up inside fibers, dialysate down outside; urea and potassium out, bicarbonate in
□ "Pulled: pressure below zero" and "Pushed: pressure above zero" zones split at the pump
□ Transmembrane pressure shown as calculated bracket, not a gauge
□ No replacement fluid, no pre-dialyzer gauge, no numbers
□ Label spelling correct throughout; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 06-C — Pressure alarm first checks
- **File:** images/nephrology-nursing-06-pressure-alarms.png
- **Placement:** Module 6, section `circuit` (The blood circuit, step by step, and what each pressure means), beside the alarm table
- **Job:** A — the learner responds to each pressure alarm by looking at the patient and access first, reasoning from the pump, then escalating.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Algorithm for hemodialysis pressure alarms: arterial too negative, venous high, venous low, transmembrane high, with first checks and a warning that needle dislodgement may not alarm.
- **Caption:** Find which side of the pump the sensor is on, then look at the patient and the access before touching the machine. The venous pressure alarm cannot be relied on to detect venous needle dislodgement, so the access stays visible for the whole treatment.
- **Source of truth:** m06_x.py `circuit` alarm table: Arterial pressure more negative than the limit — pump asking for more blood than the access delivers; causes needle against vessel wall or poorly placed, bent arm, kinked or clamped arterial line, clot in needle or catheter limb, low blood pressure or volume depletion, pump speed too high for needle size, inflow narrowing; first checks — look at the patient first (blood pressure and symptoms), follow the line from access to pump for kinks and clamps, check arm position and needle site, reduce pump speed as the unit procedure allows. High venous pressure — something resisting return; kinked or clamped venous line, lying on line or bending arm, clot in venous chamber or needle, needle against wall or infiltrated (swelling, pain), outflow narrowing especially if readings rise session to session; checks — line and arm position, needle site for swelling or pain, venous chamber for clots, stop the pump and call for help if infiltration suspected. Low venous pressure — less resistance or less flow; line separation or needle dislodgement, pump stopped or slowed, fall in blood flow from an arterial problem, dialyzer clotting upstream of the sensor; checks — look at the access and every connection before touching the machine; blood on the floor, sheet, or chair checked immediately. High transmembrane pressure — more force needed to remove the set fluid; fluid goal or time entered incorrectly, hourly rate too high for the dialyzer, fiber clotting, kinked dialysate line; checks — recheck fluid goal and time against the order, inspect dialyzer for dark streaks, confirm anticoagulation given as ordered, report. Rules: alarm silenced only after its cause is looked for; resetting repeatedly or widening limits removes the warning without removing the problem; venous pressure alarm cannot be relied on to detect venous needle dislodgement (vnd2008) — reading may fall only slightly; access and connections stay visible. Module flag: limits are machine- and policy-specific. No numbers used.
- **Reviewer flags:** Module flag: alarm limits, permitted pump-speed changes, and restart steps are machine- and policy-specific; the figure shows reasoning only. The escalation footer ("unresolved, symptomatic, bleeding, or infiltration → call for help, report") is a synthesis of the table's "call for help" and "report" actions.
- **Attach when generating:** none

```text
Clinical algorithm flowchart, 1024 × 1536 portrait (2:3). Subject: first checks for hemodialysis pressure alarms. renalcarematters.com house style. White #ffffff background, clean vector, thin navy arrows, rounded rectangles, generous margins.

TITLE BLOCK (top):
- Title, bold navy #0f1e2e: "Pressure alarm? Look first, then act"
- Subtitle, teal #1a6b72: "Reason from the pump"

STEP 0 — two linked nodes across the top:
- Teal node #d6eaec: "Before the pump: pulled (negative)" beside a matching node "After the pump: pushed (positive)", with a tiny roller-pump icon between them.
- Below, one wide peach node #f6d5bf with navy text: "FIRST: look at the patient and the access" · "Blood pressure, symptoms, needle sites, connections"
- Arrow down into a teal decision diamond: "Which alarm?" with four arrows fanning to a 2 × 2 grid of cards.

FOUR CARDS (2 × 2 grid, equal size; each card has a colored header band, a "Means" line, a "Look for" list, and a "First checks" list):

Card A — header pale blue #dbe8f5: "Arterial too negative"
  Means: "Pump asks more than access gives"
  Look for: "Needle against wall" · "Bent arm, kinked or clamped line" · "Clot in needle" · "Low blood pressure, low volume" · "Pump too fast for needle"
  First checks: "Patient first: blood pressure, symptoms" · "Trace line access to pump" · "Arm position, needle site" · "Slow pump per unit procedure"

Card B — header pale blue #dbe8f5: "Venous high"
  Means: "Return of blood is resisted"
  Look for: "Kinked or clamped line" · "Lying on line, bent arm" · "Clot in chamber or needle" · "Infiltration: swelling, pain" · "Rising session to session"
  First checks: "Line and arm position" · "Needle site: swelling, pain" · "Venous chamber: clots"
  Red sub-box: "Infiltration? Stop pump, call for help"

Card C — header clinical red #b91c1c with white text: "Venous low"
  Means: "Less resistance or less flow"
  Look for: "Needle out or line separated" · "Pump stopped or slowed" · "Arterial-side problem" · "Dialyzer clotting"
  First checks: "Access and every connection first" · "Blood on floor, sheet, chair?"

Card D — header pale amber, amber #b8860b text: "Transmembrane pressure high"
  Means: "More force needed to remove fluid"
  Look for: "Fluid goal or time entered wrong" · "Rate too high for dialyzer" · "Fibers clotting" · "Kinked dialysate line"
  First checks: "Recheck goal and time vs order" · "Dialyzer: dark streaks?" · "Anticoagulation given as ordered?" · "Report"

WARNING BANNER (full width, under the grid, bold, white text on clinical red #b91c1c, small warning-triangle icon):
"Needle dislodgement may NOT trigger the venous alarm" and a second line "Keep the access visible all treatment"

RULES STRIP (soft gray #f3f4f6, two navy rows with small icons):
"Silence only after the cause is found" · "Never widen limits to stop an alarm"

ESCALATE NODE (bottom, solid amber outline, light amber fill):
"Unresolved, symptomatic, bleeding, or infiltration: call for help and report"
Small gray note under it: "Limits and restart steps: machine manual and unit procedure"

Every label verbatim (render exactly these and nothing else): all strings in quotation marks above, exactly as written, plus the small card sub-labels "Means", "Look for", "First checks".

Colors: navy #0f1e2e text and arrows; teal #1a6b72 decision diamond and subtitle; clinical red #b91c1c for the venous-low header, infiltration sub-box, and warning banner only; amber #b8860b for TMP header and escalate node; pastel fills as specified. Typeface: Inter throughout; card text at least 12 pt equivalent, short lines. Consistent card sizes, wide margins.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside every node.

DO NOT:
✗ No mmHg values, alarm-limit numbers, pump speeds, blood flows, or needle gauges.
✗ No step that resets, silences, or widens a limit before looking for the cause.
✗ No suggestion that a quiet venous alarm means the needle is in place.
✗ No machine screen with readable numbers.
✗ No "increase pump speed" for any alarm.
✗ No catheter-specific steps beyond "clot in needle"; no drug doses.
✗ No more than four alarm cards; no air-detector or blood-leak alarm cards.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Pump reasoning nodes present: before pump negative, after pump positive
□ "FIRST: look at the patient and the access" precedes all four cards
□ Four cards: arterial too negative, venous high, venous low, transmembrane pressure high
□ Venous high card includes "Infiltration? Stop pump, call for help"
□ Red banner: "Needle dislodgement may NOT trigger the venous alarm" and "Keep the access visible all treatment"
□ Rules strip: silence only after cause found; never widen limits
□ Escalate node and "machine manual and unit procedure" note present
□ No invented numbers (no mmHg, flows, limits)
□ Label spelling correct (transmembrane, infiltration, anticoagulation, dislodgement)
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 06-D ○ — Dialysate components: what each does and what goes wrong
- **File:** images/nephrology-nursing-06-dialysate-components.png
- **Placement:** Module 6, section `dialysate` (Dialysate: what each component does and what goes wrong)
- **Job:** U — the learner sees dialysate as a prescribed drug and links each component to its risk if set too low or too high.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card of seven dialysate components, sodium to temperature, with what each does and the risks if set too low or too high, including the calcium range.
- **Caption:** Dialysate is a prescribed drug delivered by the liter: the level set in the bath decides where the patient's blood level ends up. A wrong concentrate on the machine is a medication error and is reported as one.
- **Source of truth:** m06_x.py `dialysate` table: Sodium — sets the main osmotic balance; low: cramps, headache, nausea, low blood pressure; high: thirst, larger weight gain, higher blood pressure. Potassium — controls how fast and how far blood potassium falls; low: rapid or excessive fall, observational association with arrhythmia and sudden death; high: too little removal, hyperkalemia persists. Calcium — gain or loss in the session, heart contraction and vessel tone; low: low blood pressure, cramps, tingling, rhythm disturbance, stimulates parathyroid hormone over time; high: calcium loading, concern about vessel deposition. Bicarbonate — replaces buffer; low: acidosis not corrected, muscle and bone loss; high: alkalosis, cramps, tingling, lower ionized calcium and potassium, rhythm disturbance. Magnesium — nerve, muscle, heart rhythm; low: cramps, arrhythmia; high: weakness, low blood pressure, uncommon. Glucose — prevents glucose loss; low: hypoglycemia during treatment; high: higher blood glucose. Temperature — vessel tone, heat balance; low: shivering, discomfort; high: skin vessels dilate, blood pressure falls, overheated dialysate damages red cells. Calcium range "between 1.25 and 1.50 mmol/L", weak recommendation, limited evidence (mbd2017, KDIGO 2017). "Dialysate is best thought of as a prescribed drug delivered by the liter"; wrong concentrate is a medication error; confirm acid and bicarbonate concentrates match the order and each other; conductivity alarm means mixture wrong, dialysate diverted away from the dialyzer. Temperature changed only by order or unit protocol.
- **Reviewer flags:** Module flags: very low dialysate potassium and arrhythmia statement is observational and not tied to a listed reference; calcium range 1.25 to 1.50 mmol/L is the KDIGO 2017 suggestion and should be checked against stocked concentrates. The plan called this a "dial"; it is drawn as a central dial graphic with a seven-row table for legibility.
- **Attach when generating:** none

```text
Clinical reference card, 1536 × 1152 landscape (4:3). Subject: the seven dialysate components, what each does, and the direction of risk if set too low or too high. Publication-grade nephrology design, white #ffffff background, flat vector.

LAYOUT:
- Title, top left, bold navy #0f1e2e: "Dialysate: a prescribed drug by the liter"
- Subtitle, teal #1a6b72: "What each component does, and what goes wrong"
- Top-right corner: a small round dial graphic (like a control knob) with seven evenly spaced segment labels around its rim: "Na", "K", "Ca", "HCO3", "Mg", "Glucose", "Temp". Center of the dial: a small dialysate drop icon. Purely decorative index; no needle, no numbers on the dial.
- Main table, four columns, seven body rows. Header row on soft gray #f3f4f6 in teal: "Component" | "What it does" | "If too low" (header with a small down-arrow icon, amber #b8860b) | "If too high" (header with a small up-arrow icon, clinical red #b91c1c). Alternating row fills white and #fafafa. Component cells bold navy.
  Row 1: "Sodium" | "Sets osmotic balance" | "Cramps, headache, nausea, low blood pressure" | "Thirst, bigger weight gain, higher blood pressure"
  Row 2: "Potassium" | "Sets how far potassium falls" | "Fast potassium fall; arrhythmia risk" | "Too little removal; high potassium persists"
  Row 3: "Calcium" | "Calcium gain or loss; heart and vessel tone" | "Low blood pressure, cramps, tingling, rhythm problems" | "Calcium loading; vessel deposits"
       Under the calcium row, a highlighted teal pill spanning the row: "Suggested range: 1.25 to 1.50 mmol/L (KDIGO 2017, weak)"
  Row 4: "Bicarbonate" | "Replaces used-up buffer" | "Acidosis persists; muscle, bone loss" | "Alkalosis: cramps, tingling, rhythm problems"
  Row 5: "Magnesium" | "Nerve, muscle, rhythm stability" | "Cramps, arrhythmia" | "Weakness, low blood pressure (uncommon)"
  Row 6: "Glucose" | "Prevents glucose loss" | "Low blood sugar during treatment" | "Higher blood sugar"
  Row 7: "Temperature" | "Vessel tone, heat balance" | "Shivering, discomfort" | "Blood pressure falls; overheating damages red cells"
- Bottom row, three small rounded cards on #f3f4f6 with navy text and small icons:
  Card 1 (clipboard icon): "Match concentrate to today's order"
  Card 2 (warning icon, amber): "Wrong concentrate = medication error"
  Card 3 (gauge icon): "Conductivity alarm: mixture wrong, flow diverted"

Every label verbatim (render exactly these and nothing else): all strings in quotation marks above, exactly as written, including "1.25 to 1.50 mmol/L".

Colors: navy #0f1e2e text; teal #1a6b72 headers and calcium pill; amber #b8860b for the too-low column header; clinical red #b91c1c for the too-high column header; fills #f3f4f6 and #fafafa. Body cells stay navy on white; do not color whole columns. Typeface: Inter throughout; table text at least 12 pt equivalent. Thin gray row dividers, generous padding.

Footer: "© renalcarematters.com" in the bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the bottom cards.

DO NOT:
✗ No numbers other than "1.25 to 1.50 mmol/L" and "2017": no sodium, potassium, bicarbonate, magnesium, glucose, or temperature values.
✗ No numbers on the dial graphic and no dial needle pointing at a setting.
✗ No "normal range" or "target" for any component except the calcium range as written.
✗ No product, brand, or concentrate names.
✗ No sodium profiling recommendation or cooling instruction.
✗ No mEq/L units; no °C or °F values.
✗ No swapped columns: "If too low" left of "If too high".
✗ No dark background, no serif font, no cartoon icons, no garbled or placeholder text.
✗ No missing or altered footer.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Seven rows in order: sodium, potassium, calcium, bicarbonate, magnesium, glucose, temperature
□ Too-low and too-high cells match the listed text for every row (spot-check potassium and temperature)
□ Calcium pill reads exactly "Suggested range: 1.25 to 1.50 mmol/L (KDIGO 2017, weak)"
□ No other numbers anywhere; dial has labels only
□ Column order: What it does, If too low, If too high
□ Bottom cards present: match order, medication error, conductivity alarm
□ Label spelling correct (bicarbonate, arrhythmia, conductivity, concentrate)
□ "HCO3" renders cleanly or is legible
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy


---

## Module 7 — Hemodialysis Vascular Access and Infection Prevention

### 07-A — Fistula, graft, catheter

- **File:** images/nephrology-nursing-07-access-types.png
- **Placement:** Module 7, section `physiology` (Fistula, graft, catheter)
- **Job:** U/P. The learner sees the three access types side by side and why the fistula is preferred: lowest infection risk, at the cost of a longer wait.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, three-panel variant) + Constitution v1.0 Layer A (AV fistula rules)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three panels compare an arteriovenous fistula, a graft, and a tunneled catheter by readiness, infection risk, and typical failure.
- **Caption:** A fistula takes weeks to months to mature but carries the lowest infection risk. A graft is ready sooner, and a tunneled catheter works immediately but has the highest rate of bloodstream infection. The "rule of 6s" is a traditional memory aid, not a test the access must pass.
- **Source of truth:** m07.py `physiology` table: Ready for use: fistula "weeks to months"; graft "about 2 to 4 weeks for standard grafts"; tunneled catheter "immediately". Infection risk: lowest, intermediate, highest. Typical failure: fistula "fails to mature; later narrowing"; graft "narrowing at the vein end; clotting"; catheter "infection; poor flow; central vein narrowing". Catheter is tunneled under the skin with a cuff. m07_x.py `maturation`: rule of 6s, "a widely taught rule of thumb", about 6 weeks, about 600 mL/min, about 6 mm diameter, no more than about 6 mm below the skin; "an aid to memory, not a test". m07_x.py `catheters`: right internal jugular preferred; subclavian avoided. m07.py case: left forearm fistula.
- **Reviewer flags:** The plan asked for "lifespan", but the module gives no lifespan figures. The figure uses the module's "typical failure" row instead. Rule of 6s wording is flagged in m07_x FLAGS for clinical reviewer confirmation.

```text
Medical education comparison figure, 1792 × 1024 px landscape (16:9), flat clean vector schematic in AJKD/NEJM graphical-abstract style, for a nursing course on renalcarematters.com. Subject: the three hemodialysis vascular accesses side by side.

ANATOMICAL TRUTH BLOCK (overrides style):
- Fistula: a surgical join (anastomosis) between an artery and a vein in the LEFT FOREARM near the wrist. The vein above the join is wide and slightly tortuous (matured). Blood flows from the artery through the join and UP the vein toward the elbow and heart. Arteries have a thick muscular wall and a round lumen; veins have a thin wall and a larger caliber.
- Graft: a smooth synthetic tube, visibly different in texture from native vessels, placed under the forearm skin in a loop. One end is sewn to an artery and the other end to a vein.
- Tunneled catheter: enters the RIGHT INTERNAL JUGULAR VEIN in the neck and travels under the chest skin through a tunnel. A small fabric cuff sits inside the tunnel, and the catheter leaves the skin at an exit site on the upper chest. Two external limbs end in hubs with caps: one red #C00000 (arterial) and one blue #1F6FC0 (venous). Draw ONE catheter with two limbs. The catheter does not enter the subclavian vein.
- Skin is drawn as a pale translucent schematic outline so the vessels can be seen. This is a diagram, not a photograph. No organs are shown.

LAYOUT: White #ffffff background. Title at the top center in bold navy #0f1e2e: "Fistula, graft, catheter". Three equal vertical panels on very soft gray cards (#f3f4f6), separated by thin dashed dividers. Each panel has an illustration in its upper 55% and a three-row comparison strip below. Row headers sit at the far left of the strips in teal #1a6b72.

PANEL 1 header (renal green #1f7a4d): "Arteriovenous fistula". Illustration: left forearm, palm up. Callouts: "Artery", "Join (anastomosis)", "Matured vein". Small navy arrows show flow up the vein, labeled "Flow toward heart". Inset box at the lower right of the illustration, outlined in amber #b8860b, titled "Rule of 6s: a rule of thumb", with four lines: "About 6 weeks after creation" / "Flow about 600 mL/min" / "Diameter about 6 mm" / "No more than about 6 mm deep". Under them in small italic: "Memory aid, not a pass test".

PANEL 2 header (amber #b8860b): "Arteriovenous graft". Illustration: forearm loop graft. Callouts: "Synthetic tube", "Artery end", "Vein end".

PANEL 3 header (clinical red #b91c1c): "Tunneled catheter". Illustration: neck and upper chest with translucent skin. Callouts: "Right internal jugular vein", "Tunnel under skin", "Cuff", "Exit site", "Red and blue hubs".

COMPARISON STRIP (three rows, aligned across all panels):
Row header "Ready for use": "Weeks to months" | "About 2–4 weeks (standard)" | "Immediately"
Row header "Infection risk": a short three-step bar in each panel, with text "Lowest" (green bar) | "Intermediate" (amber bar) | "Highest" (red bar)
Row header "Typical failure": "Fails to mature; later narrowing" | "Vein-end narrowing; clotting" | "Infection; poor flow; central narrowing"

Bottom strip, full width, soft teal tint #eef6f7, navy text: "The right access for the right patient at the right time".

TYPOGRAPHY: Inter only, sans-serif. Bold Inter for headers, regular for labels, minimum 11 pt equivalent. Labels sit in floating callout boxes with thin leader lines.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, reading exactly: © renalcarematters.com. It must not overlap the bottom strip or any panel.

NEGATIVE CONSTRAINTS:
✗ No fistula on the right arm; no flow arrows pointing toward the hand
✗ No artery drawn thin-walled or like a ureter; no vein drawn thick-walled
✗ No graft that looks like a native vein; it must look synthetic
✗ No catheter in the subclavian vein, no femoral catheter, no second catheter
✗ No needles, blood spray, bandages, or wounds in any panel
✗ No numbers other than those in the Rule of 6s box and "2–4 weeks"
✗ No lifespan figures, percentages, or infection rates
✗ No internal organs, heart chambers, or bones drawn in detail
✗ No cartoon style, no photoreal people, no faces
✗ No dark background, no serif font, no garbled or invented words
✗ No prompt text, hex codes, or metadata visible in the image

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Fistula is on the left forearm, the join is near the wrist, and flow arrows point up toward the elbow
□ The graft looks synthetic and joins an artery end and a vein end
□ The catheter enters the right internal jugular, with tunnel, cuff, and exit site labeled; one catheter, red and blue hubs
□ Infection bars run green, amber, red: "Lowest / Intermediate / Highest"
□ Rule of 6s box reads exactly as specified, including "Memory aid, not a pass test"
□ No numbers other than 6 weeks, 600 mL/min, 6 mm, 6 mm, and 2–4 weeks
□ All labels spelled correctly ("anastomosis", "Arteriovenous", "Tunneled")
□ Inter (or another approved sans-serif) throughout; no serif
□ White background; cards are light gray only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy, not overlapping content

---

### 07-B — Look, feel, listen

- **File:** images/nephrology-nursing-07-look-feel-listen.png
- **Placement:** Module 7, section `exam` (Physical examination in depth: finding the problem before it closes the access)
- **Job:** A. The learner matches what they see, feel, and hear at the access to a likely problem and the action for it, before every cannulation.
- **Governing skill:** williamriveromd-infographic-skill (Archetype 4, multi-panel educational infographic; Archetype 9 access conventions)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Infographic of normal fistula findings by look, feel, and listen, with six warning patterns, each paired with the nurse's action.
- **Caption:** A healthy fistula is soft, with a continuous thrill and a low-pitched continuous bruit. Each warning pattern points to a likely problem and an action, almost always to report it. A newly absent thrill and bruit means do not cannulate and notify the nephrologist promptly.
- **Source of truth:** m07.py `bedside`: look for redness, swelling, drainage, skin thinning or shiny skin over an aneurysm, cold or pale hand; newly absent thrill and bruit means do not cannulate, no tourniquet or pressure "to check", notify the nephrologist promptly. m07.py `physiology`: soft continuous thrill; low-pitched continuous bruit; hard pulse or high-pitched or systolic-only bruit suggests narrowing downstream. m07_x.py `exam`: healthy fistula is soft and easily compressed, with the thrill strongest at the join and fading upward; arm elevation (normal partial collapse); pulse augmentation (weak increase means inflow problem). Findings table, seven rows: prolonged bleeding / rising venous pressures → outflow narrowing; difficult cannulation, clots, very negative arterial pressure → inflow problem; whole-arm, shoulder, breast, neck, or face swelling and new chest-wall veins → central vein narrowing; cold, pale, or bluish hand, pain or numbness worse during dialysis, fingertip wounds → steal; redness, warmth, tenderness, swelling, pus, fever → infection; aneurysm with thin, shiny, or discolored skin, scab, ulcer, or rapid enlargement → risk of life-threatening bleeding. Actions as in the table.
- **Reviewer flags:** Central vein narrowing is added beyond the plan's list because the module table includes it. Bedside tests (arm elevation, pulse augmentation) are for trained staff per m07_x FLAGS.

```text
Dialysis access education infographic, 1792 × 1024 px landscape (16:9), clean 2D modular infographic with one restrained semi-realistic forearm illustration, for a nursing course on renalcarematters.com. Subject: examining an arteriovenous fistula by looking, feeling, and listening.

ANATOMICAL TRUTH BLOCK: The illustration shows a LEFT forearm, palm up, with a matured fistula. The join (anastomosis) is near the wrist, and the enlarged vein runs up toward the elbow. Flow goes from the join toward the heart. Skin is intact. Gloved fingertips rest lightly on the vein, and a stethoscope bell sits on the vein a little higher. No needles, no tubing, no blood.

LAYOUT: White #fafafa background. Title at the top left in bold navy #0f1e2e: "Look, feel, listen". Subtitle in teal #1a6b72: "Before every cannulation".

Top banner, full width, clinical red #b91c1c outline on a pale red tint, bold: "No thrill, no bruit: do not cannulate". Second line: "No tourniquet or pressure · notify nephrologist now".

LEFT COLUMN (about 32% width), card header in renal green #1f7a4d: "Normal findings". The forearm illustration sits on top. Below it, three icon rows:
- eye icon, "Look": "Skin intact, hand warm and pink"
- hand icon, "Feel": "Soft, continuous thrill" / "Strongest at the join"
- stethoscope icon, "Listen": "Low-pitched, continuous bruit"
A small gray note: "Arm raised: vein partly collapses"

RIGHT AREA (about 68% width): a 3 × 2 grid of six warning cards. Each card has an amber #b8860b or red #b91c1c top band with the problem name, two or three short "You find" lines, and a bold navy "Action" line on a soft teal tint #eef6f7.

Card 1 (amber) "Outflow narrowing". You find: "Hammering pulse, high-pitched bruit" / "Bleeding longer, several sessions" / "Venous pressures rising". Action: "Chart the trend; report".
Card 2 (amber) "Inflow problem". You find: "Weak pulse augmentation" / "Hard cannulation, clots drawn" / "Very negative arterial pressure". Action: "Report; don't just lower flow".
Card 3 (amber) "Central vein narrowing". You find: "Arm, neck, or face swelling" / "New veins on chest wall". Action: "Report for imaging".
Card 4 (red) "Steal". You find: "Cold, pale, or bluish hand" / "Pain or numbness on dialysis" / "Fingertip wounds". Action: "Report promptly; urgent if tissue loss".
Card 5 (red) "Infection". You find: "Redness, warmth, swelling, pus" / "Fever". Action: "Don't cannulate area; notify physician".
Card 6 (red) "Aneurysm at risk". You find: "Thin, shiny, discolored skin" / "Scab, ulcer, rapid growth". Action: "Don't cannulate there; notify same session". Add a small line: "Teach direct pressure at home".

Bottom strip, soft gray #f3f4f6, navy text: "A trend across three sessions beats one number".

TYPOGRAPHY: Inter only, sans-serif. Bold for headers, regular for body, minimum 11 pt equivalent. Short phrases, no paragraphs.

COLORS: navy #0f1e2e text; teal #1a6b72 accents; green #1f7a4d normal; amber #b8860b caution; red #b91c1c urgent.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the bottom strip and cards.

NEGATIVE CONSTRAINTS:
✗ No needles, tourniquet, cannulation, or blood in the illustration
✗ No fistula on the right arm; no flow drawn toward the hand
✗ No grotesque or exaggerated aneurysm, ulcer, or pus imagery; icons only for warning cards
✗ No numbers, pressure values, or mmHg figures anywhere
✗ No drug names, antibiotics, or doses
✗ No action that implies the nurse decides treatment alone; actions are report or notify
✗ No stethoscope placed on the hand or wrist bones; it sits on the vein
✗ No cartoon style, no faces, no photoreal patient portrait
✗ No dark background, no serif font, no garbled text
✗ No prompt text or hex codes visible

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Red banner reads "No thrill, no bruit: do not cannulate" and its second line is exact
□ Normal column shows soft continuous thrill, strongest at the join, and a low-pitched continuous bruit
□ All six warning cards are present, with the exact titles: Outflow narrowing, Inflow problem, Central vein narrowing, Steal, Infection, Aneurysm at risk
□ Every action line is report or notify; none prescribes treatment
□ No numbers or pressure values appear
□ Left forearm, join near the wrist, no needles or blood
□ Aneurysm card uses an icon, not graphic skin damage
□ Spelling checked: "cannulate", "augmentation", "anastomosis"
□ Inter font, white background
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 07-C — Where the needles go

- **File:** images/nephrology-nursing-07-cannulation-techniques.png
- **Placement:** Module 7, section `cannulation` (Cannulation technique: where the needles go and why)
- **Job:** A. The learner sees why rotating sites protects the vein, how area puncture causes aneurysms, when buttonhole is used, and which way each needle points.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, three-panel variant) + Constitution v1.0 Layer A (AV fistula: venous needle points away from the anastomosis, toward the heart)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three panels compare rope-ladder, area puncture, and buttonhole cannulation, with a strip showing needle direction and spacing along a fistula.
- **Caption:** Rope-ladder rotation spreads wear evenly and is the default for fistulas and the only technique for grafts. Area puncture balloons the vein into aneurysms. Buttonhole carries a higher infection risk and is limited to selected situations. The venous needle always points with the flow, toward the heart, and the two tips are kept well apart.
- **Source of truth:** m07_x.py `cannulation` table. Rope-ladder: default for fistulas, only acceptable technique for grafts. Area puncture: wall weakens and balloons into aneurysms, overlying skin thins, narrowings form between bulges; "not a recognized technique, but the commonest pattern". Buttonhole: same hole, angle, and depth; blunt needle after scab removal; higher rate of access infection; limited to selected situations such as a very short usable segment or self-cannulation, with strict technique; never used in grafts. Needle direction: venous needle always points in the direction of flow, toward the heart; arterial needle with or against flow per unit practice, upstream of the venous needle and far enough from the join; tips kept well apart because recirculation lowers the dose without any alarm; minimum distances per unit procedure. m07.py `bedside`: rotate sites unless another technique is prescribed.
- **Reviewer flags:** No distances are shown, per m07_x FLAGS. The arterial needle is drawn with an "either direction, per unit practice" double-headed note so neither direction is implied as the rule.

```text
Medical education comparison figure, 1792 × 1024 px landscape (16:9), flat clean vector schematic in AJKD/NEJM graphical-abstract style, for a nursing course on renalcarematters.com. Subject: three cannulation patterns on an arteriovenous fistula, plus needle direction.

ANATOMICAL TRUTH BLOCK (overrides style):
- Every panel shows the same LEFT forearm fistula, drawn horizontally: the wrist and the join (anastomosis) at image LEFT, the elbow at image RIGHT. Blood flows left to right, from the join toward the heart. Navy flow arrows inside the vein point RIGHT.
- Venous (return) needle, blue #1F6FC0: its bevel tip ALWAYS points RIGHT, with the flow and away from the join, toward the heart. It sits farther from the join than the arterial needle.
- Arterial needle, red #C00000: sits UPSTREAM of the venous needle (closer to the join), yet well away from the join itself.
- The two needle tips are clearly separated.

LAYOUT: White #ffffff background. Title at the top center in bold navy #0f1e2e: "Where the needles go". Three equal panels on soft gray cards #f3f4f6 occupy the upper 62%. A full-width needle-direction strip occupies the lower 30%.

PANEL 1 header band renal green #1f7a4d: "Rope-ladder (site rotation)". Drawing: the vein with small dot marks spread evenly along its full length, in rows like ladder rungs, with faint numbers 1–6 showing order. Vein caliber stays even. Labels: "Sites spread along full length", "Wear spread evenly". Badge: "Default for fistulas" and "Only technique for grafts".

PANEL 2 header band clinical red #b91c1c: "Area puncture". Drawing: dots crowded in two small zones; at each zone the vein balloons into an aneurysm with thin, shiny skin over it, and a narrowing between the two bulges. Labels: "Same small zones", "Aneurysm", "Thin skin", "Narrowing between bulges". Badge: "Not a recognized technique".

PANEL 3 header band amber #b8860b: "Buttonhole (constant site)". Drawing: two single fixed holes, each with a short tunnel track under the skin, and a blunt-tipped needle entering one track. Labels: "Same hole, angle, depth", "Blunt needle in track". Amber badge: "Higher infection risk". Lines below: "Selected situations only" / "Strict technique · never in grafts".

NEEDLE-DIRECTION STRIP (soft teal tint #eef6f7): one larger horizontal fistula, join at left labeled "Join", flow arrows rightward labeled "Flow toward heart". Red needle near the left-middle labeled "Arterial needle" with a small double-headed arrow note: "With or against flow, per unit". Blue needle farther right, tip pointing right, labeled "Venous needle: points with flow". A bracket between the two tips labeled "Keep tips well apart". A small callout: "Too close = recirculation, no alarm". A gray note: "Distances per unit procedure".

TYPOGRAPHY: Inter only, sans-serif. Bold for headers, regular for labels, minimum 11 pt equivalent.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the strip contents.

NEGATIVE CONSTRAINTS:
✗ No venous needle pointing toward the join or the hand; it points toward the elbow and heart
✗ No arterial needle downstream of (to the right of) the venous needle
✗ No needles touching or overlapping each other
✗ No distances, centimeters, needle gauges, or angles in degrees
✗ No buttonhole shown as the preferred or default method; no green color for buttonhole
✗ No rope-ladder vein with bulges; the vein caliber stays even in panel 1
✗ No graft drawn in any panel; all three are native fistulas
✗ No blood spray, no gore, no hands holding needles
✗ No right arm, no mirrored layout
✗ No cartoon style, no dark background, no serif font, no garbled text, no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ The join is at image left and flow arrows point right in all four drawings
□ The blue venous needle tip points right (with flow, toward the heart)
□ The red arterial needle is upstream of the venous needle, and the tips are visibly apart
□ "With or against flow, per unit" appears beside the arterial needle
□ Area puncture shows aneurysms, thin skin, and a narrowing between bulges
□ Buttonhole has an amber "Higher infection risk" badge and "Selected situations only"
□ Rope-ladder badges read "Default for fistulas" and "Only technique for grafts"
□ No distances, gauges, or angles anywhere
□ Spelling checked: "Rope-ladder", "recirculation", "Buttonhole"
□ Inter font, white background; footer exactly "© renalcarematters.com" bottom right, semi-transparent navy

---

### 07-D — Catheter connection and exit-site care (○ optional)

- **File:** images/nephrology-nursing-07-catheter-care-sequence.png
- **Placement:** Module 7, section `catheters` (Catheters in depth: care, dysfunction, and infection)
- **Job:** A. The learner follows a closed, clean catheter sequence and knows exactly what to do when a connector is contaminated.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal step sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Six-step sequence for tunneled catheter care, from masking to capping, with a red branch for a contaminated connector: stop, do not connect.
- **Caption:** Organisms reach the blood mainly through the inside of the catheter, so hub care matters most. If a hub or connector touches a non-sterile surface, stop and do not connect: clamp, scrub again or replace as the procedure directs, and report. Antiseptic, scrub time, and lock solution follow unit procedure and the order.
- **Source of truth:** m07.py `bedside`: nurse and patient both masked; scrub each hub for the time the procedure specifies before opening and again before connecting; never leave an open hub exposed to air; if contaminated, "stop. Do not connect. Clamp, scrub the hub again or replace the contaminated component as your procedure directs"; reporting is part of the correction; PPE is clean gloves, mask, and eye protection. m07_x.py `catheters`: remove old dressing; inspect for redness, crusting, drainage, tenderness along the tunnel, visible cuff; clean with unit antiseptic, allow to dry, sterile dressing; ointment per unit policy; visible cuff or outward movement reported before use; lock withdrawn and discarded before use as the procedure directs; lock instilled to exactly the volume printed on each limb; lock chosen by order; catheter for dialysis only. m09_x.py `ending`: clamps closed before the syringe is removed; new sterile caps.
- **Reviewer flags:** None. No products, times, or volumes are shown.

```text
Clean clinical education step-sequence infographic, 1792 × 1024 px landscape (16:9), flat vector style with simple line icons, for a nursing course on renalcarematters.com. Subject: tunneled dialysis catheter connection and exit-site care as a closed, clean technique.

DEVICE TRUTH BLOCK: One tunneled catheter exits the skin on the upper right chest. Two limbs, each with a clamp and a hub: arterial limb cap red #C00000, venous limb cap blue #1F6FC0. Icons show gloved, masked hands only; no faces in detail. No blood visible.

LAYOUT: White #ffffff background. Title at the top center in bold navy #0f1e2e: "Catheter care: closed and clean". Subtitle in teal #1a6b72: "Every session · nurse and patient masked". Six rounded cards in one horizontal row on a soft gray panel #f3f4f6, joined by bold navy right-pointing arrows. Each card has a teal top band with a step number, a simple line icon, a bold step label, and one or two short detail lines.

Card 1 "Mask and clean hands". Details: "Nurse and patient masked" / "Hand hygiene, gloves, eye protection".
Card 2 "Inspect exit site". Details: "Redness, crusting, drainage" / "Tunnel tenderness, visible cuff".
Card 3 "Clean and dress". Details: "Unit antiseptic; let it dry" / "Sterile dressing".
Card 4 "Scrub each hub". Details: "Before opening, per procedure" / "Never leave hub open".
Card 5 "Remove lock, connect". Details: "Discard lock as directed" / "Scrub again before connecting".
Card 6 "Lock, clamp, cap". Details: "Volume printed on each limb" / "Clamp, then new sterile cap".

STOP BRANCH: below cards 4 and 5, a red #b91c1c outlined box with a downward arrow from card 5 labeled "Hub touched non-sterile surface?". Box title, bold red: "Stop. Do not connect." Lines: "Clamp; re-scrub or replace" / "Per unit procedure" / "Report: part of the fix".

REPORT-FIRST NOTE: below cards 2 and 3, an amber #b8860b outlined small box: "Cuff visible or catheter moved out?" / "Report before use".

Bottom strip, full width, soft teal tint #eef6f7, navy text: "Dialysis only: no other use without nephrologist order".

TYPOGRAPHY: Inter only, sans-serif. Bold for labels, regular for details, minimum 11 pt equivalent. No paragraphs.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No antiseptic brand, product name, or chemical concentration
✗ No scrub times, seconds, minutes, or dressing-change intervals
✗ No lock solution name, volume in mL, or heparin dose
✗ No open hub drawn uncapped and unattended in the air
✗ No bare hands touching the hub; gloves throughout
✗ No catheter on the left side of the neck, no subclavian entry, and no groin (femoral) site — the catheter is in the RIGHT internal jugular vein only
✗ No blood, pus, or wound imagery
✗ No syringe connected with an open clamp in card 6; the clamp is closed before the syringe is removed
✗ No cartoon characters, no faces, no dark background, no serif font
✗ No garbled text and no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Six cards in order: Mask and clean hands → Inspect exit site → Clean and dress → Scrub each hub → Remove lock, connect → Lock, clamp, cap
□ Red stop box reads "Stop. Do not connect." and its three lines are exact
□ Amber note about cuff or outward movement is present
□ No times, product names, volumes in mL, or concentrations
□ Hubs are capped red and blue; gloves on in every icon
□ Bottom strip reads "Dialysis only: no other use without nephrologist order"
□ Spelling checked: "non-sterile", "antiseptic", "nephrologist"
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---


---

## Module 8 — Hemodialysis Equipment, Water, and Dialysate Safety

### 08-A — Water treatment train

- **File:** images/nephrology-nursing-08-water-treatment-train.png
- **Placement:** Module 8, section `components` (What each component does, how it fails, and what shows the failure)
- **Job:** U. The learner traces water from source to machine and can say what each component does, how it fails, and which reading shows the failure.
- **Governing skill:** williamriveromd-infographic-skill (Archetype 4, multi-panel educational infographic)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Water treatment train from supply through filters, softener, two carbon tanks, reverse osmosis, and distribution loop to the dialysis machine, with failures and monitors.
- **Caption:** Carbon is the only barrier against chlorine and chloramine, and it gives no warning when exhausted, so total chlorine is tested after the carbon every treatment day. A machine showing normal conductivity and temperature can still be running on unsafe water. Sampling points and limits follow the unit water plan.
- **Source of truth:** m08.py `physiology` stage table, in order: sediment filter (removes particles; downstream clogs); softener (exchanges calcium and magnesium for sodium; hard water scales membrane); carbon tanks, two in series (adsorb chlorine and chloramine; hemolysis, membrane damage); reverse osmosis (rejects dissolved salts, metals, bacteria, endotoxin; contaminants reach dialysate); distribution loop (delivers to each station; stagnant sections grow biofilm); dialysis machine (mixes with acid and bicarbonate concentrates; warms, degasses, monitors; wrong composition or temperature). Machine sensors cannot detect chloramine, bacteria, endotoxin, or trace chemicals. m08_x.py `components`: sediment, pressure difference widens; softener, brine tank salt, regeneration outside treatment hours, hardness test (end of day most informative); carbon worker and polisher, sampling ports after each, "which port is tested at which time... written in the unit's water policy"; RO, product conductivity or TDS, percent rejection, intact membrane "well over 90%", falling rejection is an early warning; loop, no dead legs, continuous flow. m08.py `bedside`: test after carbon before treatment each day. m08_x.py `micro`: bacteriological testing at least monthly. Component order cross-checked with guides/dialysis-water-treatment-systems.html (feed → sediment → softener → carbon → RO → loop → machine).
- **Reviewer flags:** The "≤0.1 mg/L" total chlorine limit (m08.py `evidence`) is deliberately not shown. The figure says "Above unit action level = hold", because the module frames numeric limits as orientation only and the brief asks for the carbon sampling point "per unit water plan". No contact time is shown. UV/endotoxin filters and deionization tanks ("where used") are omitted for clarity; the guide places a microfilter and UF that the module does not.

```text
Educational water-system infographic, 1792 × 1024 px landscape (16:9), clean flat vector schematic with light 3D shading on the tanks, for a nursing course on renalcarematters.com. Subject: the hemodialysis water treatment train from supply to machine.

SYSTEM TRUTH BLOCK (order is mandatory, left to right): Water supply → Sediment filter → Softener (with a separate small brine tank beside it) → Carbon tank 1 → Carbon tank 2 → Reverse osmosis unit → Distribution loop → Dialysis machine. The two carbon tanks are side by side IN SERIES, joined by one pipe. Carbon comes BEFORE reverse osmosis. The distribution loop leaves the RO unit, passes the machine stations, and RETURNS to the start of the loop, with no capped dead-end branches.

LAYOUT: White #ffffff background. Title at the top left in bold navy #0f1e2e: "From supply to dialyzer". Subtitle in teal #1a6b72: "What each step does, how it fails". A horizontal pipeline runs across the middle third with water-flow arrows in teal. Above each component, a short white card labeled "Job". Below each component, two stacked mini-cards: "If it fails" (amber #b8860b band) and "Shows as" (navy band).

Component labels and cards:
1. "Water supply". Job: "Municipal or deep well".
2. "Sediment filter". Job: "Removes particles". If it fails: "Clogs downstream". Shows as: "Pressure drop widens".
3. "Softener" + small "Brine tank". Job: "Swaps calcium, magnesium for sodium". If it fails: "Hard water scales RO". Shows as: "Hardness test, end of day".
4–5. "Carbon tank 1 (worker)" and "Carbon tank 2 (polisher)", one shared card. Job: "Removes chlorine, chloramine". If it fails (red #b91c1c band instead of amber): "Hemolysis in patients". Shows as: "Total chlorine test, every treatment day". Two small sampling-tap icons, one after each tank, with one shared callout: "Sampling point: per unit water plan". A red badge near tank 2: "No warning when exhausted".
6. "Reverse osmosis". Job: "Rejects salts, metals, bacteria, endotoxin". If it fails: "Contaminants reach dialysate". Shows as: "Product conductivity · % rejection". Small note: "Intact: well over 90% rejection".
7. "Distribution loop". Job: "Delivers to every station". If it fails: "Stagnant water grows biofilm". Shows as: "Cultures, at least monthly". Small note: "No dead legs".
8. "Dialysis machine". Job: "Mixes concentrates, warms, monitors". If it fails: "Wrong mix or temperature". Shows as: "Conductivity, temperature alarms".

Callout box beside the machine, red outline: "Green screen ≠ safe water". Lines: "Cannot detect chloramine" / "or bacteria, endotoxin, trace chemicals".

Bottom strip, soft gray #f3f4f6, navy text: "Test after carbon fails or missing: hold treatment, escalate".

TYPOGRAPHY: Inter only, sans-serif. Bold for component names, regular for cards, minimum 11 pt equivalent.

COLORS: navy #0f1e2e text; teal #1a6b72 pipes and arrows; amber #b8860b fail bands; red #b91c1c for the carbon fail band and safety callouts; tanks in soft neutral grays.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No carbon tanks placed after reverse osmosis; carbon is always before RO
✗ No single carbon tank; exactly two in series
✗ No chlorine limit in mg/L, no contact time, no flow rate, no pressure numbers
✗ No CFU or EU values, no endotoxin numbers
✗ No percentage other than "well over 90%"
✗ No dead-end branch on the loop; the loop returns
✗ No brand names, logos, or readable gauge faces
✗ No dialysis patient in the image; equipment only
✗ No dark background, no serif font, no cartoon style
✗ No garbled labels and no prompt text visible

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Order is exact: supply → sediment → softener (+ brine tank) → carbon 1 → carbon 2 → RO → loop → machine
□ Two carbon tanks in series, both before RO
□ Carbon fail band is red and reads "Hemolysis in patients"; "No warning when exhausted" badge present
□ The sampling callout reads exactly "Sampling point: per unit water plan"
□ The only number is "well over 90%" (plus "monthly"); no mg/L, CFU, EU, or contact time
□ "Green screen ≠ safe water" callout present and exact
□ The loop returns with no dead legs
□ Spelling checked: "chloramine", "endotoxin", "polisher", "Reverse osmosis"
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 08-B — From contaminant to bedside: the cluster rule

- **File:** images/nephrology-nursing-08-contaminant-syndromes.png
- **Placement:** Module 8, section `syndromes` (From contaminant to bedside: syndromes and the cluster rule)
- **Job:** A. The learner links a patient's symptom back to a possible water contaminant and, above all, acts on a cluster: two or more patients with the same new symptom on one shift.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card, radial variant)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card with the cluster rule at center, surrounded by nine water contaminants and the symptoms each causes in patients.
- **Caption:** The nurse never sees a contaminant, only a patient with a symptom. One patient with chills usually has a patient-level cause. Two or more patients on the same shift with the same new symptom share an exposure, so stop connecting patients and investigate the common source first.
- **Source of truth:** m08_x.py `syndromes` table, nine rows: chloramine/chlorine (hemolysis: chest or back pain, breathlessness, dark or translucent blood in lines; falling hemoglobin); aluminum (over months: speech disturbance, muscle jerks, seizures, dementia; bone pain, fractures; small-cell anemia); fluoride (itching, nausea, headache, chest pain, then fatal rhythm disturbance; exhausted deionization resin); calcium and magnesium ("hard water syndrome": nausea, vomiting, headache, flushing, high BP, weakness); copper, zinc (hemolysis, nausea, chills, fever); nitrate (methemoglobinemia: bluish or gray color, brownish blood, low BP, nausea); sulfate (nausea, vomiting, metabolic acidosis); bacteria and endotoxin (chills, fever, muscle aches, low BP; bloodstream infection); cyanobacterial toxin (visual disturbance, nausea, vomiting, then liver failure). Cluster rule: "Two or more patients on the same shift with the same new symptom"; say it aloud to the charge nurse; do not connect further patients; assess and stop or continue as protocol and physician direct; if hemolysis is suspected, blood not returned; notify nephrologist, technician, medical director; keep evidence (dialyzers, lines, concentrate lots, samples); record station, machine, dialyzer type and reuse number, concentrate lots, time of onset.
- **Reviewer flags:** The center wording uses the module's phrasing ("2 or more · same shift · same new symptom"), not the plan's paraphrase.

```text
Clinical reference card, 1536 × 1152 px (4:3), publication-grade flat vector design, for a nursing course on renalcarematters.com. Subject: water contaminants and the bedside syndromes they cause, organized around the cluster rule.

LAYOUT: White #ffffff background. Title at the top left in bold navy #0f1e2e: "From contaminant to bedside". Subtitle in teal #1a6b72: "You see the symptom, not the contaminant".

CENTER (the focal element, about 30% of the canvas): a large rounded hexagon or circle with a bold clinical red #b91c1c border on a pale red tint. Heading, bold red, large: "The cluster rule". Subheading, bold navy: "2 or more patients" / "Same shift · same new symptom". Below, a short numbered list in navy:
1 "Say it aloud to charge nurse"
2 "Stop connecting new patients"
3 "Assess; stop or continue per protocol"
4 "Hemolysis suspected: blood not returned"
5 "Notify nephrologist, technician, director"
6 "Keep dialyzers, lines, lots, samples"
7 "Record station, machine, onset time"

SURROUNDING RING: nine compact contaminant tiles arranged evenly around the center, each joined to it by a thin teal spoke line. Each tile has a teal header band with the contaminant name and two or three short symptom lines in navy. Tiles whose symptoms include hemolysis or a fatal outcome get a small red corner marker.

Tile "Chloramine, chlorine" (red marker): "Hemolysis: chest, back pain" / "Breathless; translucent blood in lines" / "Falling hemoglobin".
Tile "Aluminum": "Over months: speech change, jerks" / "Seizures, dementia" / "Bone pain, fractures, anemia".
Tile "Fluoride" (red marker): "Itching, nausea, headache" / "Chest pain, then fatal rhythm".
Tile "Calcium, magnesium": "Hard water syndrome" / "Nausea, vomiting, headache, flushing" / "High blood pressure, weakness".
Tile "Copper, zinc" (red marker): "Hemolysis" / "Nausea, chills, fever".
Tile "Nitrate": "Bluish or gray color" / "Brownish blood, low blood pressure".
Tile "Sulfate": "Nausea, vomiting" / "Metabolic acidosis".
Tile "Bacteria, endotoxin": "Chills, fever, muscle aches" / "Low blood pressure on dialysis" / "Bloodstream infection".
Tile "Cyanobacterial toxin" (red marker): "Visual disturbance, vomiting" / "Then liver failure".

Bottom strip, soft gray #f3f4f6, navy text: "One patient: look at the patient. Two: look at what they share."

TYPOGRAPHY: Inter only, sans-serif. Bold for headers, regular for symptoms, minimum 11 pt equivalent.

COLORS: navy #0f1e2e text; teal #1a6b72 headers and spokes; red #b91c1c center and markers; tile fills #f3f4f6.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of all tiles and the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No contaminant limits, mg/L values, CFU, EU, or any numbers except "2"
✗ No contaminant names other than the nine listed
✗ No drug treatments, antidotes, or doses
✗ No center text that tells the nurse to treat; actions are escalate, hold, preserve, record
✗ No cluster rule shrunk to a corner; it must be the largest, central element
✗ No photographs of sick patients, no blood imagery, no skulls or death symbols
✗ No molecule diagrams or chemical formulas
✗ No cartoon style, no dark background, no serif font
✗ No garbled text, no prompt text, no hex codes visible

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ The cluster rule is central and the largest element, with a red border
□ The center reads "2 or more patients" / "Same shift · same new symptom", and all seven actions are present
□ "Hemolysis suspected: blood not returned" appears exactly
□ All nine tiles are present, with names exactly as listed
□ Red markers only on chloramine, fluoride, copper/zinc, and cyanobacterial toxin
□ No numbers other than "2"
□ Spelling checked: "Chloramine", "Cyanobacterial", "endotoxin", "Metabolic acidosis"
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 08-C — Reprocessed dialyzer: six checks before use

- **File:** images/nephrology-nursing-08-reprocessing-checkpoints.png
- **Placement:** Module 8, section `disinfect-reuse` (Machine disinfection and dialyzer reprocessing)
- **Job:** A. The learner verifies a reprocessed dialyzer at the station in the correct order and keeps the two germicide tests apart (presence before rinsing, absence before priming).
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal step sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Six safety checkpoints for a reprocessed dialyzer, from label and two-person identity check to the germicide absence test before priming.
- **Caption:** Each check answers a specific hazard. Germicide presence before rinsing proves disinfection happened, and germicide absence after rinsing proves the patient will not receive it. Any failed or missing check means the dialyzer is not used and the event is reported.
- **Source of truth:** m08_x.py `disinfect-reuse` table: permanent label with full name, second identifier, and reuse count; two people check, the patient one of them whenever able; fiber-bundle volume test, retired below 80% of original; pressure or leak test, recorded pass; germicide presence test positive before rinsing, storage time within unit procedure; rinse and priming, germicide absence test negative after rinsing, recorded with the tester's name; inspection (cracks, clots, discoloration, loose caps; if in doubt, discard); maximum number of uses within unit policy. Same patient only. HBsAg-positive patients excluded from reuse. m08_x QUIZ: a mismatch or a missing absence test, either is sufficient to stop; quarantine, report.
- **Reviewer flags:** "80%" is shown as the module states it (also matches the site reuse guide per m08_x FLAGS). Maximum reuse number is unit policy and is not shown.

```text
Clean clinical education step-sequence infographic, 1792 × 1024 px landscape (16:9), flat vector style with simple line icons, for a nursing course on renalcarematters.com. Subject: safety checkpoints before a reprocessed dialyzer is used.

DEVICE TRUTH BLOCK: The dialyzer is a clear cylindrical cartridge with fine parallel hollow fibers visible inside. It has two END ports for blood (red cap #C00000 at one end, blue cap #1F6FC0 at the other) and two SIDE ports for dialysate near the ends, all capped. A white permanent label on the cartridge shows blurred, unreadable placeholder lines (no legible name). No bloodlines are connected.

LAYOUT: White #ffffff background. Title at the top center in bold navy #0f1e2e: "Reprocessed dialyzer: six checks". Subtitle in teal #1a6b72: "Same patient only · any fail = do not use". Six rounded cards in one horizontal row on soft gray #f3f4f6, joined by bold navy arrows. Each card has a numbered teal top band, an icon, a bold label, a "Checks" line, and a small gray "Prevents" line.

Card 1 "Label". Checks: "Full name, second identifier, reuse count". Prevents: "Wrong patient's blood".
Card 2 "Two-person identity check". Checks: "Patient is one, when able". Prevents: "Wrong-patient use". Icon: two people and a dialyzer.
Card 3 "Volume and leak tests". Checks: "Fiber volume ≥80% of original" / "Leak test passed". Prevents: "Low clearance, blood leak".
Card 4 "Germicide PRESENT". A green #1f7a4d "+" test-strip icon. Checks: "Positive before rinsing". Prevents: "Surviving bacteria".
Card 5 "Inspect and count". Checks: "No cracks, clots, loose caps" / "Uses within unit policy". Prevents: "Damaged or fatigued membrane".
Card 6 "Germicide ABSENT". A strip icon with "−" and a check mark. Checks: "Negative after rinse, before priming" / "Tester's name recorded". Prevents: "Germicide reaching patient".

Make "PRESENT" (card 4) and "ABSENT" (card 6) visually contrasted: card 4 band in renal green #1f7a4d, card 6 band in deep teal #1a6b72, each word in bold capitals.

STOP BAR below the row, clinical red #b91c1c outline: "Any check fails or missing:" / "Set aside · do not use · report".

Side note at the lower left, amber #b8860b outline: "HBsAg positive: no reuse".

Bottom strip, soft teal tint #eef6f7, navy text: "Present proves disinfection. Absent protects the patient."

TYPOGRAPHY: Inter only, sans-serif. Bold for labels, regular for details, minimum 11 pt equivalent.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No germicide names, concentrations, or dwell or storage times
✗ No maximum reuse number
✗ No percentage other than "80%"
✗ No legible patient name on the label
✗ No PRESENT and ABSENT tests shown at the same step or in reversed order
✗ No dialyzer with blood-colored contents; it is clear or pale
✗ No dialysate ports on the end caps; the end caps carry blood ports only
✗ No connected patient, no needles, no blood
✗ No cartoon style, no dark background, no serif font
✗ No garbled text and no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Card order: Label → Two-person identity check → Volume and leak tests → Germicide PRESENT → Inspect and count → Germicide ABSENT
□ PRESENT reads "Positive before rinsing"; ABSENT reads "Negative after rinse, before priming"
□ "≥80% of original" is the only numeric value
□ Red stop bar reads "Set aside · do not use · report"
□ "HBsAg positive: no reuse" note present
□ Dialyzer: blood ports at the end caps, dialysate ports on the sides, label unreadable
□ Spelling checked: "Germicide", "identifier", "priming"
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---


---

## Module 9 — The Hemodialysis Session and Complication Response

### 09-A — One session: before, during, after

- **File:** images/nephrology-nursing-09-session-three-phases.png
- **Placement:** Module 9, section `physiology` (Before, during, after)
- **Job:** A. The learner carries one fixed set of checkpoints through every session and knows which pre-treatment findings mean calling the physician before connecting.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, three-phase sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three-phase timeline of a dialysis session with nursing checks before, during, and after, plus findings that require a call before connecting.
- **Caption:** The pre-treatment assessment ends in one decision: start as prescribed, or call the physician first. During treatment, a half-minute round at each station checks the face, the access, the lines, and the machine. A patient leaves only when the discharge checks are met. All numeric thresholds come from unit policy or standing orders.
- **Source of truth:** m09.py `physiology` table. Before: identity, weight and gain, BP sitting and standing if dizzy, temperature, breathing, edema, access exam, bleeding or falls, medicines taken or held. During: BP and pulse at the ordered interval and with symptoms; appearance and responsiveness; access and connections in view; arterial and venous pressures; UF progress; blood color. After: BP sitting and standing, weight against target, hemostasis or catheter care, symptoms, walks safely. m09_x.py `predialysis` call-first table: fever or chills; chest pain, palpitations, fainting; breathlessness at rest, low oxygen saturation; BP above or below unit thresholds; new confusion, one-sided weakness, slurred speech; access problem; bleeding, fall, procedure; weight gain far above usual; weight at or below target, vomiting, diarrhea; missed sessions. m09_x.py `monitoring`: half-minute round (face and speech, access, lines and chambers, machine). m09_x.py `ending`: ready to leave when BP is acceptable without significant fall, sites dry with thrill or catheter capped, no chest pain or breathlessness or confusion or bleeding, walks as usual, glucose checked if diabetic.
- **Reviewer flags:** No thresholds shown, per m09_x FLAGS ("numeric thresholds... from unit policy or standing orders").

```text
Clean clinical education timeline infographic, 1792 × 1024 px landscape (16:9), flat vector style with simple line icons, for a nursing course on renalcarematters.com. Subject: one hemodialysis session in three phases, with nursing checkpoints.

LAYOUT: White #ffffff background. Title at the top left in bold navy #0f1e2e: "One session: before, during, after". Subtitle in teal #1a6b72: "Thresholds per unit policy or standing orders". A thick horizontal teal timeline arrow runs left to right across the middle, divided into three segments labeled on the arrow: "Before", "During", "After". Each segment has a large rounded card on soft gray #f3f4f6 above the arrow.

BEFORE card (teal band). Heading: "Before connecting". Bullets:
"Identity; how since last session"
"Weight and gain"
"Blood pressure; temperature; breathing"
"Edema; access exam"
"Bleeding, falls, procedures"
"Medicines taken or held today"

DURING card (teal band). Heading: "Every round, about 30 seconds". Four icon rows:
face icon "Face and speech: color, rousable"
arm icon "Access visible, tape intact"
tube icon "Lines: kinks, clots, blood color"
monitor icon "Pressures trend; fluid removed"
Line below: "Blood pressure, pulse: interval ordered".

AFTER card (green #1f7a4d band). Heading: "Safe to leave?". Check-mark bullets:
"Blood pressure OK standing"
"Weight against target"
"Sites dry, thrill present"
"No chest pain, breathlessness, confusion"
"Walks as usual or escorted"
"Diabetes: glucose checked if indicated"

CALL-FIRST PANEL: below the Before segment of the timeline, a red #b91c1c outlined panel with a downward branch arrow from the Before card. Title, bold red: "Call physician before starting". Two compact columns of short items:
"Fever or chills"
"Chest pain, palpitations, fainting"
"Breathless at rest, low oxygen"
"Blood pressure outside unit limits"
"New confusion, weakness, slurred speech"
"Access problem"
"Bleeding, fall, recent procedure"
"Weight gain far above usual"
"At or below target; vomiting"
"Missed sessions"

Under the After card, a small amber #b8860b note: "Not ready: stays, physician told".

Bottom strip, soft teal tint #eef6f7, navy text: "Alarms detect pressures. Nurses detect patients."

TYPOGRAPHY: Inter only, sans-serif. Bold for headings, regular for bullets, minimum 11 pt equivalent.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No blood pressure numbers, temperatures, oxygen saturation values, or weight-gain limits
✗ No minute intervals for vital signs; "interval ordered" only
✗ No blood flow, ultrafiltration rate, or session-length numbers (only "30 seconds" for the round)
✗ No drug names or doses
✗ No photoreal patient or readable machine screen
✗ No covered access in any icon; the access is visible
✗ No call-first items attached to the During or After phases
✗ No cartoon style, no dark background, no serif font
✗ No garbled text and no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Three phases in order on the timeline: Before, During, After
□ Red call-first panel branches from Before only; all ten items present and spelled correctly
□ During card lists face, access, lines, and pressures, plus "interval ordered"
□ After card has all six discharge checks
□ The only number is "30 seconds"
□ Bottom strip reads "Alarms detect pressures. Nurses detect patients."
□ Access is visible in the icons
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 09-B — Intradialytic hypotension: first response

- **File:** images/nephrology-nursing-09-idh-algorithm.png
- **Placement:** Module 9, section `bedside` (First actions while help is coming); cross-reference from `idh-prevention`
- **Job:** A. The learner performs the first actions for symptomatic hypotension in order, knows when it is no longer ordinary hypotension, and sees the prevention strategies that change the next session.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, renalcarematters.com house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Algorithm for hypotension during dialysis: recognize, stop fluid removal, position, assess, notify, then escalate if no prompt recovery; prevention strategies alongside.
- **Caption:** Stopping fluid removal and raising the legs address the usual mechanism, and every further step follows protocol or order. Hypotension that does not correct promptly, or that comes with chest pain, arrhythmia, or altered consciousness, is treated as an emergency. A recurring pattern is a prescription problem to report.
- **Source of truth:** m09.py `bedside`, symptomatic hypotension row: recognize (dizziness, yawning, nausea, cramps, pallor, sweating, falling BP, reduced responsiveness); stop or minimize UF; recline with legs raised if not breathless; check BP, responsiveness, access for bleeding; fluid or oxygen as protocol or order allows; notify physician; no prompt recovery or chest pain, arrhythmia, altered consciousness = emergency (cardiac, bleeding, sepsis). "Call for help early, stay with the patient, note the time." m09_x.py `idh-prevention`: reassess target weight; limit weight gain mainly by restricting salt; longer or additional sessions; cooler dialysate (individual, as ordered); avoid meals during treatment; review timing of BP medicines; treat anemia; look for heart disease and other causes; review dialysate composition; sodium profiling not routine; report the pattern. m09_x.py `monitoring`: "Hypotension that does not correct promptly is not ordinary IDH."
- **Reviewer flags:** No fluid volumes or oxygen rates (m09.py quiz flag: "by unit protocol or physician order").

```text
Clinical algorithm flowchart, 1024 × 1536 px portrait (2:3), publication-ready renalcarematters.com house style, for a nursing course. Subject: first response to symptomatic intradialytic hypotension (low blood pressure during dialysis), with a prevention side panel.

LAYOUT: White #ffffff background. Title at the top center in bold navy #0f1e2e: "Low blood pressure during dialysis". Subtitle in teal #1a6b72: "Intradialytic hypotension: first response". Under the subtitle, a thin gray capsule: "Call for help early · stay · note the time". The main pathway runs top to bottom down the left 62% of the canvas. A prevention side panel occupies the right 34%. Thin teal connector arrows throughout.

MAIN PATHWAY NODES (rounded rectangles unless stated):
1. Peach/amber-tint node, heading "Recognize". Lines: "Dizziness, yawning, nausea, cramps" / "Pale, sweating, less responsive" / "Blood pressure falling".
2. Navy-outlined action node: "Stop or minimize fluid removal".
3. Navy-outlined action node: "Recline, legs raised" with a small gray qualifier beneath: "If not breathless".
4. Navy-outlined action node: "Check blood pressure, responsiveness" / "Look at access for bleeding".
5. Soft gray node: "Fluid or oxygen" / "As protocol or order allows".
6. Teal action node: "Notify the physician".
7. Teal diamond decision: "Prompt recovery?" A secondary line inside or beside it: "No chest pain, arrhythmia, confusion".
Branch YES (arrow down-left, green label "Yes"): green #1f7a4d node "Continue; monitor closely" / "Document; report if recurring".
Branch NO (arrow down-right, red bold label "No"): red #b91c1c bordered node "Treat as emergency" / "Consider cardiac, bleeding, sepsis".

PREVENTION SIDE PANEL: soft teal tint #eef6f7 rounded panel, heading bold navy "Prevent the next one", subheading teal "Prescriber decides; nurse reports". Nine short items with small line icons:
"Reassess target weight"
"Less weight gain: limit salt"
"Longer or extra sessions"
"Cooler dialysate, if ordered"
"No meals during treatment"
"Review blood pressure medicine timing"
"Treat anemia"
"Look for heart disease"
"Confirm prescribed dialysate"
At the bottom of the panel, an amber #b8860b outlined note: "Same hour every session?" / "Report the pattern".

TYPOGRAPHY: Inter only, sans-serif, crisp navy text, minimum 11 pt equivalent, consistent node widths and spacing.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Never inside a node, never overlapping arrows.

NEGATIVE CONSTRAINTS:
✗ No blood pressure thresholds or mmHg values
✗ No fluid bolus volumes, saline mL, or oxygen flow rates
✗ No drug names (no midodrine, no vasopressors), no doses
✗ No dialysate temperature numbers or sodium values
✗ No "increase ultrafiltration" or "finish faster" node
✗ No sodium profiling shown as a prevention strategy
✗ No node that has the nurse change the prescription alone; side panel is labeled "Prescriber decides; nurse reports"
✗ No patient photographs, no machine screens, no 3D elements
✗ No dark background, no serif font, no cartoon icons
✗ No garbled text and no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Node order: Recognize → Stop or minimize fluid removal → Recline, legs raised (if not breathless) → Check BP/access → Fluid or oxygen as protocol allows → Notify → Prompt recovery?
□ The "No" branch reads "Treat as emergency" / "Consider cardiac, bleeding, sepsis" in red
□ No numbers anywhere
□ Prevention panel has nine items and "Prescriber decides; nurse reports"
□ No sodium profiling and no drug names
□ Spelling checked: "Intradialytic", "hypotension", "arrhythmia", "dialysate"
□ Portrait 2:3, white background, Inter font
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy, outside nodes

---

### 09-C — Emergencies at the chair

- **File:** images/nephrology-nursing-09-chairside-emergencies.png
- **Placement:** Module 9, section `bedside` (First actions while help is coming); disequilibrium content from `predialysis`
- **Job:** A. The learner recognizes five time-critical dialysis emergencies and knows the first actions for each, especially the ones where blood must not be returned.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card of five dialysis emergencies (air entry, hemolysis, needle dislodgement, dialyzer reaction, disequilibrium), each with signs and first actions.
- **Caption:** In every emergency, call for help early, stay with the patient, and note the time. In hemolysis and dialyzer reactions the blood in the circuit is not returned, and blood is never returned through a line that contains air. All further steps follow the unit protocol and physician orders.
- **Source of truth:** m09.py `bedside` table. Needle dislodgement: visible blood, wet clothing or bedding, sudden hypotension, alarm may or may not sound; stop pump and clamp, firm direct pressure, call for help, assess, lay flat, estimate loss; further steps per protocol. Hemolysis: translucent, cherry-red, or dark "port-wine" blood in venous line; chest, back, or abdominal pain; breathlessness; several patients suggests water or dialysate; stop dialysis and clamp; do not return the blood; keep circuit and dialysate; monitor heart rhythm; call physician; prepare for urgent potassium and hemoglobin tests; check other patients on the same supply. Air: air alarm, visible air or foam, sudden cough, chest tightness, breathlessness, collapse; machine clamps and stops the pump, do not override; never return blood through a line with air; if air may have entered, left side with head down, high-flow oxygen as protocol allows, call emergency help. Reaction: within the first minutes, itching, hives, flushing, wheeze, throat tightness, chest or back pain, hypotension; stop, clamp, do not return blood; emergency help; anaphylaxis under protocol; keep dialyzer, record type and batch. m09_x.py `predialysis`, disequilibrium: first or early treatments, very high urea; headache, nausea and vomiting, restlessness, blurred vision, cramps, then disorientation, seizures; slow or stop per unit protocol, keep safe, check BP and blood sugar, notify physician at once; medicines only on order.
- **Reviewer flags:** Left-lateral head-down positioning is "traditional consensus practice; confirm against unit protocol" (m09 FLAGS).

```text
Clinical reference card, 1536 × 1152 px (4:3), publication-grade flat vector design, for a nursing course on renalcarematters.com. Subject: five emergencies at the dialysis chair, with signs and first actions.

LAYOUT: White #ffffff background. Title at the top left in bold navy #0f1e2e: "Emergencies at the chair". Directly under it, a full-width clinical red #b91c1c banner with white bold text: "Call for help early · stay · note the time". Below, a grid of five cards (three on the top row, two on the bottom row, centered). Each card has a colored header band with the event name and a small line icon, a "Signs" block (gray label) and a "First actions" block (navy label, numbered). Where blood must not be returned, include a bold red pill badge inside the card.

Card 1 header (red band) "Air entry". Icon: bubble in a tube. Signs: "Air alarm; air or foam in line" / "Sudden cough, chest tightness, collapse". First actions: "1 Machine clamps: do not override" / "2 Never return blood with air" / "3 Left side, head down" / "4 High-flow oxygen per protocol" / "5 Call emergency help". Red pill: "No return through air".

Card 2 header (red band) "Hemolysis". Icon: red cell breaking. Signs: "Translucent, cherry-red, or port-wine blood" / "Chest, back, abdominal pain" / "Breathless; several patients affected". First actions: "1 Stop and clamp lines" / "2 Do NOT return blood" / "3 Keep circuit and dialysate" / "4 Heart rhythm; call physician" / "5 Check other patients, same supply". Red pill: "Do NOT return blood".

Card 3 header (red band) "Needle dislodgement". Icon: needle and drop. Signs: "Visible blood, wet bedding" / "Sudden low blood pressure" / "Alarm may not sound". First actions: "1 Stop pump, clamp lines" / "2 Firm direct pressure" / "3 Call for help" / "4 Lay flat; assess; estimate loss".

Card 4 header (amber #b8860b band) "Dialyzer reaction". Icon: dialyzer with an alert mark. Signs: "First minutes: itching, hives, flushing" / "Wheeze, throat tightness, low blood pressure". First actions: "1 Stop and clamp lines" / "2 Do NOT return blood" / "3 Emergency help; anaphylaxis protocol" / "4 Keep dialyzer; record type, batch". Red pill: "Do NOT return blood".

Card 5 header (teal #1a6b72 band) "Disequilibrium". Icon: head outline. Signs: "First treatments, very high urea" / "Headache, vomiting, restlessness, blurred vision" / "Then confusion, seizures". First actions: "1 Slow or stop per protocol" / "2 Keep safe" / "3 Check blood pressure, blood sugar" / "4 Notify physician at once".

Bottom strip, soft gray #f3f4f6, navy text: "Every further step: unit protocol and physician orders".

TYPOGRAPHY: Inter only, sans-serif. Bold for headers and badges, regular for signs and actions, minimum 11 pt equivalent.

COLORS: navy #0f1e2e text; red #b91c1c banner, headers, and pills; amber #b8860b; teal #1a6b72; card fills #f3f4f6.

FOOTER: bottom-right corner, small (10–11 px), semi-transparent navy #0f1e2e at about 70% opacity, exactly: © renalcarematters.com. Clear of all cards and the bottom strip.

NEGATIVE CONSTRAINTS:
✗ No "return blood" or "rinse back" action in the hemolysis, reaction, or air cards
✗ No "Do NOT return blood" pill on the needle-dislodgement card (blood return there is per protocol)
✗ No air-entry positioning on the right side or head up; left side, head down only
✗ No drug names (no epinephrine, mannitol, antihistamine), no doses
✗ No oxygen flow rates, potassium values, or any numbers in the actions
✗ No patient photographs, blood pools, or gore; icons only
✗ No more or fewer than five cards
✗ No cartoon style, no dark background, no serif font
✗ No garbled text and no prompt text

Render all text exactly as written above, in American English, and add no other text.
```

**QA after generation:**
□ Red banner reads exactly "Call for help early · stay · note the time"
□ Five cards: Air entry, Hemolysis, Needle dislodgement, Dialyzer reaction, Disequilibrium
□ Hemolysis card reads "Do NOT return blood" and "Check other patients, same supply"
□ Air card: "Machine clamps: do not override", "Left side, head down", "Never return blood with air"
□ Needle dislodgement card has no do-not-return pill
□ No drug names and no numbers
□ Spelling checked: "Hemolysis", "Disequilibrium", "anaphylaxis", "dislodgement"
□ Inter font, white background
□ Footer exactly "© renalcarematters.com", bottom right, small, semi-transparent navy


---

## Module 10 — Peritoneal Dialysis and Home Dialysis Nursing

### 10-A — The peritoneal membrane and transport type
- **File:** images/nephrology-nursing-10-pd-membrane.png
- **Placement:** Module 10, section `membrane` (The membrane in depth: why the same bag behaves differently in different people)
- **Job:** U. The learner sees that the capillary wall is the real filter, why the glucose pull fades during a dwell, and why fast and slow transporters need different prescriptions.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure (+ Constitution v1.0 Layer A, Tenckhoff rules)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Diagram of the peritoneal capillary wall with two kinds of opening, the fading glucose pull, and the shapes of fast and slow transporter curves.
- **Caption:** Water and small solutes cross the peritoneal capillary wall through gaps between cells, and water alone crosses through tiny water-only channels. Glucose leaks back into the blood, so the pull on water fades. This happens sooner in fast transporters, which is why they do better with short dwells.
- **Source of truth:** m10_x.py `membrane`: the capillary wall is the real filter; gaps between lining cells let water and small solutes (urea, creatinine, potassium, glucose) pass; much smaller water-only channels through the cells; small solutes diffuse quickly at first, then more slowly; the pull on water is strongest early and then fades; if the dwell continues after the gradient is gone, fluid is reabsorbed and drain is less than fill. Fast transporter: equilibrates quickly; gradient lost early; water removal poor on long dwells; typical problem fluid overload, low drain volumes after long dwells; suits short dwells, often automated overnight, icodextrin for the long dwell. Slow transporter: equilibrates slowly; gradient kept longer; water removal sustained; typical problem solute removal too low if dwells are short; suits longer dwells, as in manual daytime exchanges. m10.py `physiology`: peritoneum lines the abdomen and is rich in small blood vessels. m10_x.py `catheter`: catheter segment with side holes lies low in the pelvis.
- **Reviewer flags:** The plan's layers "interstitium" and "mesothelium" do not appear in the module text, so they are left out. The module uses the capillary wall model only. Curves are drawn as shapes only, with no numbers on the axes.

```text
Publication-grade biomedical mechanism schematic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: how the peritoneal membrane moves solutes and water during a peritoneal dialysis dwell, and why fast and slow transporters behave differently. Review-article vector style with soft semi-3D shading on a white (#ffffff) background.

ANATOMICAL TRUTH BLOCK (overrides all style choices)
- Peritoneal dialysis catheter (Tenckhoff), if drawn: the tip with side holes lies low in the pelvis, in the deepest pelvic pouch behind the bladder. It is never inside the bladder or the colon. The catheter passes through the abdominal wall with a deep cuff inside the wall and a superficial cuff under the skin a short distance from the exit site. The exit site points downward.
- Capillary: arterial end red #C00000, venous end blue #1F6FC0, blood flowing from red to blue. Its wall is a single layer of lining cells.
- The dialysis solution sits in the peritoneal cavity, outside the capillary.

LAYOUT
Title at top left in bold navy #0f1e2e: "The filter is the capillary wall". Subtitle in teal #1a6b72: "Why the same bag behaves differently".
Left panel (28% width): simplified front view of an adult abdomen outline with a pale teal (#eef6f7) fluid-filled peritoneal cavity and a slim catheter that follows the truth block. A small dashed square on the peritoneal lining connects through a dashed line to the center panel. Labels: "Dialysis solution in abdomen", "Peritoneum (abdominal lining)", "Catheter tip low in pelvis".
Center panel (40% width), inside a thin dashed border: a magnified cross-section of one capillary wall. Blood side on the left, dialysis solution side on the right. Show two kinds of opening:
 1. Wide gaps between lining cells. Arrows carry water drops plus small colored dots (urea, creatinine, potassium) from blood to solution, and a single amber glucose dot travelling back from solution to blood. Label: "Gaps between cells: water + small solutes".
 2. Very small channels through the cells, with water drops only. Label: "Water-only channels".
 Arrow labels: "Small solutes diffuse out", "Glucose leaks back to blood", "Glucose pulls water in".
Right panel (32% width): two small stacked line graphs with no numbers, no tick values and no units. The axes are labeled only "Dwell time →" (x) and "Water drawn in" (y).
 - Top graph: two smooth curves. Teal curve "Fast transporter" rises early, peaks early, then falls (fluid reabsorbed). Navy curve "Slow transporter" rises more slowly and stays up longer.
 - Bottom graph, y axis labeled "Solutes in fluid": the teal fast curve climbs steeply to a plateau, and the navy slow curve climbs gradually.
Bottom strip (full width), three rounded boxes joined by arrows:
 - Pale pink box "Fast transporter": "Gradient lost early" / "Low drain after long dwells" / "Suits: short dwells, icodextrin long dwell".
 - Center pale teal box "Glucose gradient fades": "Long dwell after pull fades → fluid reabsorbed".
 - Pale blue box "Slow transporter": "Gradient kept longer" / "Low solute removal if dwells short" / "Suits: longer dwells".

LABELS (render exactly, nothing else): The filter is the capillary wall · Why the same bag behaves differently · Dialysis solution in abdomen · Peritoneum (abdominal lining) · Catheter tip low in pelvis · Blood · Dialysis solution · Gaps between cells: water + small solutes · Water-only channels · Small solutes diffuse out · Glucose leaks back to blood · Glucose pulls water in · Urea · Creatinine · Potassium · Glucose · Dwell time → · Water drawn in · Solutes in fluid · Fast transporter · Slow transporter · Gradient lost early · Low drain after long dwells · Suits: short dwells, icodextrin long dwell · Glucose gradient fades · Long dwell after pull fades → fluid reabsorbed · Gradient kept longer · Low solute removal if dwells short · Suits: longer dwells · © renalcarematters.com

COLORS: navy #0f1e2e text, teal #1a6b72 headings and fast curve, red #C00000 arterial blood, blue #1F6FC0 venous blood, amber #b8860b glucose, pale teal #eef6f7 solution, soft gray #f3f4f6 panels.
FONT: Inter only, bold for titles and regular for labels, at least 11 pt equivalent.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity, clear of every element.

NEGATIVE CONSTRAINTS
✗ No numbers, percentages, hours, mL or tick values on either graph
✗ No glucose strengths, doses or dwell times anywhere
✗ No catheter tip in the bladder, colon or upper abdomen, and no exit site pointing upward
✗ No water-only channels drawn letting solutes through
✗ No glucose arrow pointing only into the solution; glucose must also leak back to the blood
✗ No kidney drawn inside the abdomen panel
✗ No cartoon style, no dark background, no serif font
✗ No garbled text, no extra labels, no prompt text visible
✗ No footer variant such as "www", "Renal Care Matters" or another domain

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ Two opening types are shown, and only water passes through the water-only channels
□ The glucose dot crosses back toward the blood
□ Both graphs carry no numbers or units, only the text axis labels
□ The fast curve peaks early and falls; the slow curve stays up longer
□ The catheter tip is low in the pelvis and not in the bladder or colon; the exit site points down
□ Capillary color runs red to blue in the direction of flow
□ "Icodextrin" and "transporter" are spelled correctly; no stray words appear
□ No dose, glucose strength or time value appears
□ The background is white or light gray only, and all text is in Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right, small and semi-transparent navy

---

### 10-B — The exchange: the reason behind each step
- **File:** images/nephrology-nursing-10-pd-exchange.png
- **Placement:** Module 10, section `exchange` (The exchange: the reason behind each step)
- **Job:** A. The learner can teach and audit a twin-bag exchange in the right order and say why each step exists, especially the flush before the fill.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C) + Constitution v1.0 Tenckhoff rules
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Five-step peritoneal dialysis exchange (connect, drain, flush, fill, disconnect) with the reason for each step and a small catheter anatomy inset.
- **Caption:** The flush comes before the fill because it carries any organisms picked up at the connection away to the drain bag before fluid flows toward the abdomen. Net fluid removal equals the volume drained minus the volume filled.
- **Source of truth:** m10_x.py `exchange`: prepare the room (door and windows closed, fan off or directed away, pets out, surface wiped); mask if the program requires it; hand hygiene (thorough washing and drying, or alcohol hand rub); check the bag (strength, volume, expiry, clear fluid, leaks, seals); warm with dry heat, never immersion; connect, with connector tips touching nothing; drain; flush (a small amount of fresh solution runs straight into the drain bag, carrying organisms from the connection away); fill (drain line clamped, abdomen filled); inspect the drain (clear enough to read print through the bag, pale yellow, volume by weight); record; disconnect (new sterile cap applied without touching the tip). Net fluid removal = volume drained minus volume filled; positive means water was removed. m10.py `physiology`: drain flows out by gravity. m10_x.py `catheter`: segment with many side holes low in the pelvis; deep cuff in the abdominal wall muscle; superficial cuff under the skin a short distance from the exit site; exit site points downward or sideways.
- **Reviewer flags:** The module puts the deep cuff "in the abdominal wall muscle", while the Constitution says "preperitoneal". The label follows the module, and the drawing places the cuff deep in the wall just outside the peritoneum. The module gives no distance in centimeters for the superficial cuff, so none is labeled. Fill volume (about 2 L) is left out because it is not needed.

```text
Clean clinical education step sequence, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: one twin-bag peritoneal dialysis exchange, step by step, with the reason for each step. Flat vector style with soft shading on a white (#ffffff) background.

ANATOMICAL TRUTH BLOCK (catheter inset)
- Tenckhoff catheter: the intra-abdominal segment has many side holes, and its tip lies low in the pelvis in the deepest pouch behind the bladder. It is never in the bladder or colon.
- Deep cuff: inside the abdominal wall muscle, just outside the peritoneum. Superficial cuff: under the skin a short distance from the exit site.
- Tunnel runs obliquely, and the exit site on the skin points DOWNWARD.
- No organs are visible through skin in the step cards. Anatomy appears only in the inset.

LAYOUT
Title at top center in bold navy #0f1e2e: "The exchange: why each step matters".
Top strip (narrow, soft gray #f3f4f6), "Before you connect", with four small icon chips: "Room closed, fan off, pets out" · "Mask if program requires" · "Wash and dry hands" · "Check bag: strength, expiry, leaks" · "Warm with dry heat only".
Main row: five rounded cards joined by bold navy right-pointing arrows. Each card has a colored top band, a step number, a bold step name, a small line schematic of the twin-bag set with an arrow showing which way fluid flows, and a one-line reason.
 1. Teal band. "1 Connect": schematic of the transfer set joined to the new twin-bag set. Reason: "Tips touch nothing".
 2. Navy band. "2 Drain": arrow from abdomen down to the drain bag on the floor. Reason: "Used fluid out by gravity".
 3. Amber band #b8860b, visually emphasized with a slightly larger card. "3 Flush": arrow from the new bag straight into the drain bag, bypassing the abdomen. Reason: "Washes connection germs to drain bag".
 4. Green band #1f7a4d. "4 Fill": drain line clamped (clamp icon), arrow from the raised new bag into the abdomen. Reason: "Fresh solution in, after flush".
 5. Teal band. "5 Disconnect": new sterile cap on the transfer set. Reason: "New cap, tip untouched".
Under cards 2 and 4, a small note: "Inspect drain: clear enough to read print" and "Record: drained − filled = net removal".
Right inset (≤15% of canvas), dashed border, titled "The catheter": side-view cross-section of the lower abdominal wall following the truth block. Labels: "Deep cuff (in wall muscle)", "Superficial cuff (under skin)", "Exit site points down", "Side holes low in pelvis".
Bottom strip (full width, soft gray): "Never fill before the flush."

LABELS (render exactly, nothing else): The exchange: why each step matters · Before you connect · Room closed, fan off, pets out · Mask if program requires · Wash and dry hands · Check bag: strength, expiry, leaks · Warm with dry heat only · 1 Connect · Tips touch nothing · 2 Drain · Used fluid out by gravity · 3 Flush · Washes connection germs to drain bag · 4 Fill · Fresh solution in, after flush · 5 Disconnect · New cap, tip untouched · Inspect drain: clear enough to read print · Record: drained − filled = net removal · The catheter · Deep cuff (in wall muscle) · Superficial cuff (under skin) · Exit site points down · Side holes low in pelvis · Never fill before the flush. · © renalcarematters.com

COLORS: navy #0f1e2e, teal #1a6b72, amber #b8860b, green #1f7a4d, pale teal #eef6f7 fluid, soft gray #f3f4f6 strips. Fresh solution clear and pale; drained fluid pale yellow.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No step order other than connect → drain → flush → fill → disconnect
✗ No flush arrow going into the abdomen; the flush goes new bag → drain bag only
✗ No fill shown while the drain line is open
✗ No bag warmed in water or in a microwave
✗ No catheter tip in the bladder, colon or upper abdomen; no exit site pointing upward
✗ No volumes, dwell times, glucose strengths or brand names
✗ No cloudy drain fluid
✗ No bare-handed touching of connector tips
✗ No cartoon style, dark background, serif font, garbled text or extra words

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The five steps appear in the correct order, with flush (step 3) visually emphasized
□ The flush arrow runs from the new bag to the drain bag and bypasses the abdomen
□ The drain line is clamped in the fill card
□ The inset shows two cuffs, the exit site pointing down, and the tip low in the pelvis (not in bladder or colon)
□ No volumes, times, strengths or brands appear
□ The drain fluid is clear pale yellow and not cloudy
□ "Superficial", "expiry" and "disconnect" are spelled correctly
□ The net removal line reads "drained − filled" in that order
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 10-C — Cloudy fluid or abdominal pain: the peritonitis pathway
- **File:** images/nephrology-nursing-10-peritonitis-algorithm.png
- **Placement:** Module 10, section `infection` (Infection in depth: exit site, tunnel, and peritonitis)
- **Job:** A. The learner knows what to do, in order, from the phone call about cloudy fluid through specimen collection, treatment and follow-up, and when catheter removal comes up.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Portrait algorithm for suspected PD peritonitis: same-day assessment, specimens before antibiotics, treatment per protocol, daily follow-up, and when catheter removal is discussed.
- **Caption:** Cloudy effluent, with or without pain, means same-day assessment and the cloudy bag comes too. Specimens are collected before the first antibiotic dose, and treatment follows the program protocol. Refractory, relapsing or fungal peritonitis leads to a discussion of catheter removal.
- **Source of truth:** m10.py `bedside`: come to the PD unit or emergency department the same day and bring the cloudy bag; do not advise waiting; notify the PD team; assess the exit site and tunnel; ask about recent contamination, constipation or diarrhea, and procedures. m10.py `case` Escalate: severe pain, vomiting, high fever or low blood pressure means the emergency department without delay. m10.py `evidence` (ISPD 2022): at least two of (1) abdominal pain and/or cloudy effluent, (2) effluent white cell count above 100 per microliter after a dwell of at least 2 hours with more than 50% neutrophils, (3) positive effluent culture; send cell count, differential, Gram stain and culture; start antibiotics as soon as possible after specimens, preferably into the peritoneum. m10_x.py `infection`: the first cloudy bag is the best specimen; if the abdomen is empty, run solution in and dwell at least 2 hours before sampling; blood-culture bottles preferred; label with dwell time; collect before the first antibiotic dose; the antibiotic bag is not drained early; antifungal prophylaxis whenever antibiotics are given; improvement expected within about two to three days; track clarity daily; repeat cell counts; refractory = not cleared after 5 days of appropriate antibiotics; relapsing = new episode within 4 weeks of finishing treatment with the same organism or no growth; fungal; in these cases the guideline recommends catheter removal with temporary hemodialysis; every episode investigated and technique observed again.
- **Reviewer flags:** FOR CLINICIAN REVIEW. The ">100/µL", ">50% neutrophils", "≥2 hours", "5 days" (refractory), "4 weeks" (relapsing) and "2–3 days" values were written from recall and are flagged in the module (FLAGS line 1); confirm them against the ISPD 2022 text. The ISPD unit rate targets (≤0.40 episodes per patient-year; culture-negative <15%) are in the module but are left off the image because they are a program standard, not a bedside step. Treatment is shown only as "per program protocol", with no drug names.

```text
Publication-ready clinical algorithm flowchart, portrait 1024 × 1536 (2:3), in the renalcarematters.com house style, for a nursing course. Subject: the nurse's pathway when a peritoneal dialysis patient reports cloudy fluid or abdominal pain. Bright white (#ffffff) background, centered top-to-bottom flow, thin teal (#1a6b72) connector arrows, generous margins, flat vector look with no icons except a small bag symbol at the top.

TITLE (top center, bold navy #0f1e2e): "Cloudy fluid or abdominal pain"
SUBTITLE (teal): "Suspect peritonitis until tested"

NODES, top to bottom:
1. Amber (#b8860b outline, pale amber fill) start node: "Patient reports cloudy bag or pain"
2. Red (#b91c1c) escalation node: "Come in today. Bring the cloudy bag." Below it, small text: "Do not wait for the next bag to clear."
   Side branch to the right, red outline box: "Severe pain, vomiting, high fever, low BP → emergency department now".
3. Navy action node: "Notify PD team". Small text: "Check exit site and tunnel. Ask: contamination, bowel habit, procedures."
4. Navy action node: "Collect specimens before first antibiotic". Small bullets: "First cloudy bag is best" · "Empty abdomen: fill, dwell ≥2 h, then sample" · "Cell count, differential, Gram stain, culture" · "Culture in blood-culture bottles" · "Label with dwell time".
5. Teal diamond decision: "At least 2 of 3?". Three small side tags around the diamond: "Pain and/or cloudy fluid" · "White cells >100/µL, >50% neutrophils" · "Positive culture".
6. Green (#1f7a4d) action node: "Antibiotics into peritoneum, per program protocol". Small text: "Start once specimens taken. Antibiotic bag not drained early. Ask about antifungal prophylaxis."
7. Navy monitoring node: "Follow daily: pain, bag clarity". Small text: "Expect improvement in about 2–3 days. Repeat cell counts."
8. Teal diamond decision: "Not clearing?". Three small side tags: "Refractory: not clear after 5 days" · "Relapsing: back within 4 weeks" · "Fungal".
   Arrow "Yes" leads to a red node: "Catheter removal discussed. Temporary hemodialysis."
   Arrow "No" leads to a green node: "Complete treatment as ordered".
9. Soft gray bottom node spanning the width: "Every episode: find the cause, observe technique, retrain".

LABELS (render exactly, nothing else): Cloudy fluid or abdominal pain · Suspect peritonitis until tested · Patient reports cloudy bag or pain · Come in today. Bring the cloudy bag. · Do not wait for the next bag to clear. · Severe pain, vomiting, high fever, low BP → emergency department now · Notify PD team · Check exit site and tunnel. Ask: contamination, bowel habit, procedures. · Collect specimens before first antibiotic · First cloudy bag is best · Empty abdomen: fill, dwell ≥2 h, then sample · Cell count, differential, Gram stain, culture · Culture in blood-culture bottles · Label with dwell time · At least 2 of 3? · Pain and/or cloudy fluid · White cells >100/µL, >50% neutrophils · Positive culture · Antibiotics into peritoneum, per program protocol · Start once specimens taken. Antibiotic bag not drained early. Ask about antifungal prophylaxis. · Follow daily: pain, bag clarity · Expect improvement in about 2–3 days. Repeat cell counts. · Not clearing? · Refractory: not clear after 5 days · Relapsing: back within 4 weeks · Fungal · Yes · No · Catheter removal discussed. Temporary hemodialysis. · Complete treatment as ordered · Every episode: find the cause, observe technique, retrain · © renalcarematters.com

COLORS: navy #0f1e2e text, teal #1a6b72 decisions and arrows, green #1f7a4d treatment, amber #b8860b start, red #b91c1c urgent, soft gray #f3f4f6 notes.
FONT: Inter only, crisp, at least 11 pt equivalent.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity, outside every node.

NEGATIVE CONSTRAINTS
✗ No antibiotic, antifungal or heparin names, doses or durations
✗ No dwell time for the antibiotic bag
✗ No peritonitis rate targets or percentages other than those listed
✗ No "wait and see" or "call back tomorrow" wording
✗ No antibiotics shown before specimen collection
✗ No changed numbers: keep >100/µL, >50%, ≥2 h, 2–3 days, 5 days, 4 weeks exactly
✗ No spaghetti arrows; at most two side branches
✗ No photos, people, cartoon style, dark background or serif font
✗ No garbled text and no added labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The same-day instruction and "bring the cloudy bag" are near the top, in red
□ Specimen collection comes before the antibiotic node
□ Exactly these numbers appear: ≥2 h, >100/µL, >50%, 2–3 days, 5 days, 4 weeks
□ No drug names, doses or antibiotic dwell time appear
□ "Refractory", "Relapsing" and "Gram stain" are spelled correctly
□ The red emergency side branch lists severe pain, vomiting, high fever and low BP
□ "Catheter removal discussed" is attached to the "Yes" branch only
□ The flow is top to bottom and readable on a phone
□ The background is white, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---


---

## Module 11 — Transplantation and Special Populations

### 11-A — Where the new kidney sits, and what can go wrong there
- **File:** images/nephrology-nursing-11-transplant-anatomy.png
- **Placement:** Module 11, section `physiology` (From referral to the first week)
- **Job:** U. The learner pictures the graft joined to the pelvic vessels and bladder, and links each join to the complication and bedside sign it can produce.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure (+ Constitution v1.0 Layer A vessel and ureter rules)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Lower-abdomen diagram of a transplanted kidney joined to a pelvic artery, pelvic vein and bladder with a stent, labeled with each site's warning sign.
- **Caption:** The new kidney is placed in the lower abdomen and joined to the pelvic vessels and the bladder. Each join has its own complication. Because the graft has no nerve supply, a blocked ureter is often painless, and a clot in the artery can stop urine abruptly.
- **Source of truth:** m11.py `physiology`: the new kidney is placed in the lower abdomen and joined to the pelvic vessels and bladder; urine output is measured hourly. m11_x.py `periop`: the ureteral stent is removed by a minor procedure at the time the surgeon sets; a forgotten stent causes infection and stones; urinary catheter clots. m11_x.py `complications`: bleeding (rising pulse, falling BP, blood in the drain); clot in the artery (urine stops abruptly, often without pain); clot in the vein (sudden swollen, painful graft, blood in the urine); urine leak (falling urine output, rising drain output); ureter obstruction (falling output, usually painless because the graft has no nerve supply); lymphocele (collection of lymph beside the graft, swelling of the leg on the same side). m11_x.py `donors`: "the pelvic arteries where the kidney will be joined".
- **Reviewer flags:** The module does not name the iliac fossa, the right side, the external iliac artery or vein, or whether the native kidneys stay in place. The labels therefore say "pelvic artery", "pelvic vein" and "lower abdomen", and the view is cropped below the native kidneys so the image makes no claim about them. The drawing shows standard anatomy (right iliac fossa, external iliac vessels). If Dr. Rivero wants those terms on the image, add a sentence to `physiology` first.

```text
Publication-grade biomedical anatomy schematic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: a transplanted kidney in the lower abdomen and the warning sign linked to each surgical join. Netter-inspired clean vector style with soft semi-3D shading on a white (#ffffff) background.

ANATOMICAL TRUTH BLOCK (overrides style)
- Front view of the lower abdomen and pelvis only, cropped at the level of the umbilicus. No native kidneys appear in the frame.
- The graft kidney lies extraperitoneally in the patient's right lower abdomen (image left), just above the pelvic brim, with its hilum facing medially toward the pelvic vessels. The convex border faces laterally. The renal pelvis exits at the hilum only.
- Graft renal artery (red #C00000, thick muscular wall, round lumen) joins the side of the large pelvic artery running along the pelvic brim.
- Graft renal vein (blue #1F6FC0, thin wall, wider caliber) joins the side of the large pelvic vein beside that artery.
- Graft ureter (pale yellow, thin-walled) runs a short course down and medially and enters the dome of the bladder. A thin dashed tube inside it marks the temporary stent, coiled at both ends (one coil in the renal pelvis, one in the bladder).
- Bladder in the midline pelvis, with a urinary catheter leaving through the urethra.
- Wound drain: a slim tube from beside the graft exiting the skin.
- Arteries are never thin like the ureter, and the ureter is never thick like an artery.

LAYOUT
Title at top left in bold navy #0f1e2e: "The new kidney: joins and warning signs". Subtitle in teal #1a6b72: "A graft has no nerve supply, so trouble is often painless".
Center (60% width): the anatomy described above, labeled with thin leader lines.
Anatomy labels: "Transplanted kidney (graft)", "Graft artery joined to pelvic artery", "Graft vein joined to pelvic vein", "Ureter joined to bladder", "Temporary stent", "Bladder", "Urinary catheter", "Wound drain".
Around the anatomy, six small rounded warning cards (pale pink #fdecec, red #b91c1c heading). Each points with a dashed line to its site:
 - at the artery: "Artery clot" / "Urine stops abruptly, often painless"
 - at the vein: "Vein clot" / "Swollen painful graft, blood in urine"
 - at the ureter–bladder join: "Urine leak" / "Less urine, more drain fluid"
 - along the ureter: "Ureter blocked" / "Falling output, usually painless"
 - beside the graft: "Lymphocele" / "Same-side leg swelling"
 - at the wound and drain: "Bleeding" / "Rising pulse, falling BP"
Bottom strip (soft gray #f3f4f6, full width), navy text: "Measure urine hourly. A sudden fall is reported now." A small teal tag at the right of the strip: "Stent removal date is tracked".

LABELS (render exactly, nothing else): The new kidney: joins and warning signs · A graft has no nerve supply, so trouble is often painless · Transplanted kidney (graft) · Graft artery joined to pelvic artery · Graft vein joined to pelvic vein · Ureter joined to bladder · Temporary stent · Bladder · Urinary catheter · Wound drain · Artery clot · Urine stops abruptly, often painless · Vein clot · Swollen painful graft, blood in urine · Urine leak · Less urine, more drain fluid · Ureter blocked · Falling output, usually painless · Lymphocele · Same-side leg swelling · Bleeding · Rising pulse, falling BP · Measure urine hourly. A sudden fall is reported now. · Stent removal date is tracked · © renalcarematters.com

COLORS: arteries red #C00000, veins blue #1F6FC0, ureter pale yellow, kidney soft pink-brown, navy #0f1e2e text, teal #1a6b72 accents, red #b91c1c warning headings.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No native kidneys in the frame and no label about them
✗ No graft in the flank or behind the peritoneum at kidney level; it sits in the lower abdomen
✗ No artery joined to the vein, and no vessels joined to the aorta or vena cava
✗ No ureter entering the renal vein or skipping the bladder
✗ No hilum on the lateral (convex) border
✗ No thin-walled artery and no thick-walled ureter
✗ No stent drawn outside the ureter
✗ No visible skin with anatomy shown through it as a photo; the schematic is cut away
✗ No drug names, creatinine values or urine volumes
✗ No cartoon style, dark background, serif font, garbled text or extra labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The graft is in the right lower abdomen (image left), with the hilum facing medially
□ The graft artery (red, thick wall) joins a pelvic artery, and the graft vein (blue, thin wall) joins a pelvic vein
□ The ureter enters the bladder, and the stent lies inside it with coils at both ends
□ No native kidneys are visible
□ All six warning cards point to the correct sites
□ No numbers appear anywhere except in the footer
□ "Lymphocele" and "Transplanted" are spelled correctly
□ The bottom strip reads exactly as written
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 11-B — Infection after transplant: a timeline
- **File:** images/nephrology-nursing-11-transplant-infection-timeline.png
- **Placement:** Module 11, section `complications` (Complications: surgical, immune, and infectious)
- **Job:** A. The learner matches the months since transplant to the infections to expect and the nursing focus for that window, and remembers that fever is always reported.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, timeline)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three-window timeline of infections after kidney transplant (first month, months 1 to 6, after 6 months) with the nursing focus for each window.
- **Caption:** Infection risk follows the level of immunosuppression. Opportunistic infections peak in months 1 to 6 and come back whenever immunosuppression is increased to treat rejection. Fever in a recipient is always reported the same day.
- **Source of truth:** m11_x.py `complications` infection table. First month: wound, urinary tract, pneumonia, catheter and line infections; occasionally infection carried in the donor kidney; focus: remove lines and catheters as soon as ordered, wound care, hand hygiene, early walking. Months 1 to 6: opportunistic infections at peak immunosuppression (cytomegalovirus, Pneumocystis pneumonia, BK virus, fungal infection, reactivation of latent infection such as tuberculosis); focus: adherence to preventive medicines, screening blood tests, low threshold for reporting fever, cough, breathlessness, diarrhea. After 6 months: mostly community infections (influenza, pneumonia, urinary tract infection); opportunistic infections return when immunosuppression is increased to treat rejection; focus: vaccination, food and water safety, prompt reporting. Also: urinary tract infection is the most common bacterial infection after kidney transplantation; BK virus causes no symptoms and is found by screening blood tests; "Fever in a recipient is always reported the same day"; steroids blunt fever.
- **Reviewer flags:** The module notes that this is the conventional teaching framework and that programs differ in prophylaxis and screening schedules. No prophylaxis agents or durations are shown.

```text
Clean clinical education timeline infographic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: which infections to expect after a kidney transplant, by time since surgery, and what the nurse focuses on in each window. Flat vector style on a white (#ffffff) background.

LAYOUT
Title at top center in bold navy #0f1e2e: "Infection after transplant follows a timeline". Subtitle in teal #1a6b72: "Risk tracks the strength of immunosuppression".
A horizontal arrow-shaped timeline runs across the middle third, starting at a small kidney icon labeled "Transplant". It is divided into three segments of equal width with labels on the bar: "First month" · "Months 1–6" · "After 6 months". Above the bar, a soft shaded band labeled "Immunosuppression" is low-moderate over the first segment, tallest over months 1–6 and lower after 6 months, with a small upward bump in the last segment tagged "Rises if rejection treated". The band is qualitative only, with no axis numbers.
Below each segment is a tall rounded card on soft gray #f3f4f6 with a colored top band and two parts:
 Card 1 (teal band), title "Surgical-type infections". "Expect:" "Wound" · "Urinary tract" · "Pneumonia" · "Line and catheter" · "Rarely, from donor kidney". "Nurse focus:" "Remove lines when ordered" · "Wound care, hand hygiene" · "Early walking".
 Card 2 (red #b91c1c band, slightly emphasized), title "Opportunistic infections". "Expect:" "Cytomegalovirus" · "Pneumocystis pneumonia" · "BK virus (silent, found by blood test)" · "Fungal infection" · "Tuberculosis reactivation". "Nurse focus:" "Preventive medicines taken" · "Screening blood tests kept" · "Report fever, cough, breathlessness, diarrhea".
 Card 3 (green #1f7a4d band), title "Community infections". "Expect:" "Influenza" · "Pneumonia" · "Urinary tract infection" · "Opportunistic, if rejection treated". "Nurse focus:" "Vaccination" · "Food and water safety" · "Prompt reporting".
Bottom banner (full width, pale red #fdecec with red #b91c1c border, bold navy text, thermometer icon): "Fever is always reported the same day". Small text under it: "Steroids blunt fever: a mild temperature can mean serious infection."
Small side tag at the bottom left in teal: "Most common bacterial infection: urinary tract".

LABELS (render exactly, nothing else): Infection after transplant follows a timeline · Risk tracks the strength of immunosuppression · Transplant · First month · Months 1–6 · After 6 months · Immunosuppression · Rises if rejection treated · Surgical-type infections · Opportunistic infections · Community infections · Expect: · Nurse focus: · Wound · Urinary tract · Pneumonia · Line and catheter · Rarely, from donor kidney · Remove lines when ordered · Wound care, hand hygiene · Early walking · Cytomegalovirus · Pneumocystis pneumonia · BK virus (silent, found by blood test) · Fungal infection · Tuberculosis reactivation · Preventive medicines taken · Screening blood tests kept · Report fever, cough, breathlessness, diarrhea · Influenza · Urinary tract infection · Opportunistic, if rejection treated · Vaccination · Food and water safety · Prompt reporting · Fever is always reported the same day · Steroids blunt fever: a mild temperature can mean serious infection. · Most common bacterial infection: urinary tract · © renalcarematters.com

COLORS: navy #0f1e2e, teal #1a6b72, red #b91c1c, green #1f7a4d, soft gray #f3f4f6, pale red #fdecec.
FONT: Inter only, with italic allowed only for "Pneumocystis".
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No drug names, prophylaxis durations or vaccine schedules
✗ No numbers on the immunosuppression band
✗ No time windows other than first month, months 1–6 and after 6 months
✗ No infections moved to the wrong window (CMV and Pneumocystis belong in months 1–6)
✗ No live-vaccine imagery such as syringes labeled with vaccine names
✗ No patient photos, microbes drawn as cartoon monsters, or alarming imagery
✗ No dark background and no serif font
✗ No garbled or misspelled organism names and no extra labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ Exactly three windows appear, labeled first month, months 1–6 and after 6 months
□ Cytomegalovirus, Pneumocystis, BK virus, fungal infection and tuberculosis appear only in the months 1–6 card
□ The immunosuppression band peaks over months 1–6 and carries no numbers
□ "Cytomegalovirus", "Pneumocystis" and "Tuberculosis" are spelled correctly
□ The fever banner is prominent and worded exactly
□ No drug names or durations appear
□ The urinary tract side tag is present
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 11-C — Immunosuppressants: what to ask, what to guard against
- **File:** images/nephrology-nursing-11-immunosuppressant-card.png
- **Placement:** Module 11, section `drugs` (The immunosuppressants: what to ask about and what to guard against)
- **Job:** A/P. The learner can ask about the right side effects for each agent and catch the dangerous interactions, especially azathioprine with allopurinol or febuxostat, and grapefruit or pomelo with tacrolimus-class drugs.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card of six transplant immunosuppressants showing what each does, side effects to ask about, and interactions to guard against. Shows no doses or levels.
- **Caption:** A vigilance card, not a prescribing guide. Doses and blood levels are set by the transplant team, and no new medicine, supplement or herbal product is started until the team has checked it.
- **Source of truth:** m11_x.py `drugs` table. Tacrolimus: blocks T-lymphocyte activation; tremor, headache, high blood sugar and new diabetes, high potassium, low magnesium, high blood pressure; level raised by some antifungals, some antibiotics, diltiazem and verapamil, grapefruit and pomelo; lowered by rifampin, some anticonvulsants, St. John's wort; immediate- and extended-release not interchangeable; trough level. Cyclosporine: same class and action; gum overgrowth, increased body and facial hair, tremor, high BP, high potassium, gout; same interactions as tacrolimus. Mycophenolate: slows the multiplication of lymphocytes; diarrhea, nausea, low white cell count, anemia; causes miscarriage and birth defects, reliable contraception required; magnesium or aluminum antacids reduce absorption. Azathioprine: slows the multiplication of lymphocytes; low blood counts, liver injury, skin cancer with long use; allopurinol and febuxostat can cause life-threatening bone marrow failure. Corticosteroids: broad suppression of inflammation and immunity; high blood sugar, weight gain, mood change, bone loss, slow wound healing; never stopped abruptly after long use. Sirolimus, everolimus: block a growth signal lymphocytes need; mouth ulcers, slow wound healing, high cholesterol, protein in urine; same interactions as tacrolimus; avoided in pregnancy. General: "no new medicine, supplement, or herbal product ... until the transplant team has checked it"; rifampin (tuberculosis treatment) lowers levels profoundly; pomelo (suha) raises levels.
- **Reviewer flags:** FOR PHARMACIST AND TRANSPLANT PHYSICIAN REVIEW (whole card), per module FLAGS 3 and 4. The cited KDIGO guideline may not be the primary source for the azathioprine and allopurinol/febuxostat interaction. Side-effect lists are shortened selections from the module table, with nothing added. No doses or target levels appear.

```text
Clinical reference card, 1536 × 1152 (4:3), publication-grade, for a nursing course on renalcarematters.com. Subject: transplant immunosuppressants, covering what each does, the side effects a nurse asks about, and the interactions to guard against. No doses and no levels. White (#ffffff) background, compact table with generous padding.

LAYOUT
Title at top left in bold navy #0f1e2e: "Transplant immunosuppressants: a nurse's vigilance card". Subtitle in teal #1a6b72: "What to ask about and what to guard against".
Top-right badge, amber (#b8860b) outline with pale amber fill and bold navy text, always visible: "Doses and levels set by the transplant team".
Table with 4 columns and 6 rows. The header row is teal #1a6b72 text on soft gray #f3f4f6: "Medicine" · "What it does" · "Ask about" · "Guard against". Rows alternate white and very soft gray.
Row 1 "Tacrolimus" | "Blocks T-cell activation" | "Tremor, headache · High sugar, high potassium · Low magnesium, high BP" | "Raised by grapefruit, pomelo, some antifungals and antibiotics · Lowered by rifampin, St. John's wort · Release forms not interchangeable"
Row 2 "Cyclosporine" | "Same class as tacrolimus" | "Gum overgrowth, extra hair · Tremor, high BP · High potassium, gout" | "Same interactions as tacrolimus"
Row 3 "Mycophenolate" | "Slows lymphocyte multiplication" | "Diarrhea, nausea · Low white cells, anemia" | "Causes miscarriage and birth defects: reliable contraception · Mg/Al antacids reduce absorption"
Row 4, highlighted with a red #b91c1c left border and pale red #fdecec fill: "Azathioprine" | "Slows lymphocyte multiplication" | "Low blood counts · Liver injury · Skin cancer with long use" | in bold red: "Allopurinol or febuxostat: life-threatening marrow failure"
Row 5 "Corticosteroids" | "Broad immune suppression" | "High sugar, weight gain · Mood change, bone loss · Slow wound healing" | "Never stop abruptly after long use"
Row 6 "Sirolimus, everolimus" | "Block a lymphocyte growth signal" | "Mouth ulcers, slow healing · High cholesterol · Protein in urine" | "Same interactions as tacrolimus · Avoided in pregnancy"
Bottom banner (full width, teal #1a6b72 border, pale teal #eef6f7 fill, bold navy text): "No new medicine, supplement, or herbal product until the transplant team checks it". Two small icon tags inside the banner at the right: a pomelo half with "Pomelo (suha) and grapefruit raise levels", and a pill with "Rifampin for TB lowers levels".

LABELS (render exactly, nothing else): Transplant immunosuppressants: a nurse's vigilance card · What to ask about and what to guard against · Doses and levels set by the transplant team · Medicine · What it does · Ask about · Guard against · plus every row text above, verbatim · No new medicine, supplement, or herbal product until the transplant team checks it · Pomelo (suha) and grapefruit raise levels · Rifampin for TB lowers levels · © renalcarematters.com

COLORS: navy #0f1e2e text, teal #1a6b72 headers, amber #b8860b badge, red #b91c1c azathioprine warning, soft gray #f3f4f6, pale teal #eef6f7.
FONT: Inter only, at least 11 pt equivalent. Use bold only for drug names, headers and the azathioprine warning.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity, below the banner.

NEGATIVE CONSTRAINTS
✗ No doses, mg values, target or trough numbers, or dosing times
✗ No brand names and no pill packaging with readable text
✗ No drugs other than the six rows listed
✗ No side effects or interactions not written above
✗ No missing "Doses and levels set by the transplant team" badge
✗ No azathioprine warning softened or moved out of the red row
✗ No spelling drift (tacrolimus, mycophenolate, azathioprine, febuxostat, everolimus)
✗ No dark background, serif font, cartoon icons or clutter
✗ No garbled text and no extra words

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The badge "Doses and levels set by the transplant team" is visible at the top right
□ There are exactly six rows; the azathioprine row is red-highlighted with the allopurinol or febuxostat warning
□ Grapefruit and pomelo appear in the tacrolimus row and in the banner
□ No doses, levels or brand names appear anywhere
□ All drug names are spelled correctly (check each of the six)
□ "Never stop abruptly after long use" is in the corticosteroid row
□ The mycophenolate pregnancy warning is present
□ No side effect appears that is not in the module table
□ The background is white, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---


---

## Module 12 — Philippine Practice, Quality Improvement, and the Capstone

### 12-A — A worked Plan–Do–Study–Act cycle
- **File:** images/nephrology-nursing-12-pdsa-cycle.png
- **Placement:** Module 12, section `dashboard` (Infection surveillance, the unit dashboard, and improvement methods)
- **Job:** A. The learner sees a whole PDSA cycle, from aim and measure through the decision to adopt, on a problem every unit knows: sessions that end early.
- **Governing skill:** williamriveromd-simple-figure (circular sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Four-part Plan–Do–Study–Act cycle on early-ending afternoon sessions, with aim, measure and decision. All figures are labeled illustrative.
- **Caption:** A worked example with invented figures. One small change was tested on one shift for two weeks, measured weekly, and then kept and extended, and a second cycle began on cramps.
- **Source of truth:** m12_x.py `dashboard`, "A worked PDSA cycle. The figures are invented for illustration." Aim: reduce the proportion of afternoon-shift sessions that end more than 15 minutes early from 18% to under 10% within eight weeks. Measure: sessions ending more than 15 minutes early ÷ all sessions on that shift, counted weekly, with the reason recorded. Plan: two weeks of reasons show most early ends are requested by patients whose shared transport leaves at a fixed time, and the shift often starts late because stations are not ready. Do: for two weeks, on one shift only, the first four stations are prepared before patients arrive and patients with fixed transport are connected first. Study: the weekly proportion falls to 11%; patients connected first rarely leave early; early ends for cramps are unchanged. Act: keep the change and extend it to other shifts; begin a second cycle on cramps with the nephrologists. m12.py `evidence`: adopt, adapt, or abandon.
- **Reviewer flags:** The "Illustrative figures" label must appear on the image (module FLAGS: invented figures).

```text
Clean clinical quality-improvement infographic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: one worked Plan–Do–Study–Act cycle in a dialysis unit. Flat vector style on a white (#ffffff) background.

LAYOUT
Title at top left in bold navy #0f1e2e: "One PDSA cycle, worked through". Subtitle in teal #1a6b72: "Problem: afternoon sessions ending early".
Top-right tag (amber #b8860b outline, pale amber fill, bold navy text, clearly visible): "Illustrative figures".
Left column (25% width), two stacked rounded cards on soft gray #f3f4f6:
 Card "Aim" (teal heading): "Sessions ending >15 min early: 18% → under 10% in 8 weeks"
 Card "Measure" (teal heading): "Early ends ÷ all shift sessions, weekly, with reason"
Center (45% width): a large circle split into four equal quadrants, joined by curved clockwise arrows, each quadrant with its own color band and a small simple icon:
 Top-left "PLAN" (teal #1a6b72): "Two weeks of reasons:" · "Fixed-time shared transport" · "Stations not ready, late start"
 Top-right "DO" (navy #0f1e2e): "One shift, two weeks:" · "First four stations prepared early" · "Fixed-transport patients connected first"
 Bottom-right "STUDY" (amber #b8860b): "Weekly early ends: 11%" · "Connected-first patients rarely leave early" · "Cramp-related early ends unchanged"
 Bottom-left "ACT" (green #1f7a4d): "Keep the change" · "Extend to other shifts"
 Center hub: "Adopt · Adapt · Abandon"
Right column (25% width): a small mini bar pair labeled "Before 18%" and "After 11%" with a dashed line labeled "Aim: under 10%". There is no axis scale beyond these three labels. Below it, an arrow out of the ACT quadrant leads to a green outlined card: "Next cycle: cramps, with the nephrologists".
Bottom strip (soft gray): "Small change, small scale, measured, then decide."

LABELS (render exactly, nothing else): One PDSA cycle, worked through · Problem: afternoon sessions ending early · Illustrative figures · Aim · Sessions ending >15 min early: 18% → under 10% in 8 weeks · Measure · Early ends ÷ all shift sessions, weekly, with reason · PLAN · Two weeks of reasons: · Fixed-time shared transport · Stations not ready, late start · DO · One shift, two weeks: · First four stations prepared early · Fixed-transport patients connected first · STUDY · Weekly early ends: 11% · Connected-first patients rarely leave early · Cramp-related early ends unchanged · ACT · Keep the change · Extend to other shifts · Adopt · Adapt · Abandon · Before 18% · After 11% · Aim: under 10% · Next cycle: cramps, with the nephrologists · Small change, small scale, measured, then decide. · © renalcarematters.com

COLORS: navy #0f1e2e, teal #1a6b72, amber #b8860b, green #1f7a4d, soft gray #f3f4f6.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No missing or tiny "Illustrative figures" tag
✗ No numbers other than 15 min, 18%, 10%, 8 weeks, 11%, "two weeks" and "four"
✗ No quadrant order other than Plan → Do → Study → Act, clockwise
✗ No claim that the aim was met (11% is above the aim)
✗ No patient names, faces, unit names or logos
✗ No graph axes with invented scales or extra data points
✗ No dark background, serif font or cartoon style
✗ No garbled text and no extra labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The "Illustrative figures" tag is clearly legible
□ The quadrants run clockwise in PDSA order
□ All numbers match: >15 min, 18%, under 10%, 8 weeks, 11%, two weeks, four stations
□ The mini bars show 11% still above the 10% aim line
□ The "Next cycle: cramps" card is present
□ "Abandon" and "nephrologists" are spelled correctly
□ No extra numbers or axis scales appear
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 12-B — The unit quality dashboard
- **File:** images/nephrology-nursing-12-quality-dashboard.png
- **Placement:** Module 12, section `dashboard` (Infection surveillance, the unit dashboard, and improvement methods)
- **Job:** P. The learner sees that bedside records feed ten quality domains the unit reviews monthly, and that targets come from the medical director, not from this course.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Grid of ten dialysis-unit quality domains, each with example measures and no targets, plus the infection rate formula per 100 patient-months.
- **Caption:** A unit dashboard tracks a small set of measures every month. Each target comes from the guideline the unit has adopted and is set by the medical director. Accurate nursing records are where these reports begin.
- **Source of truth:** m12_x.py `dashboard` table. Dialysis dose: share reaching the unit's urea-clearance target; share of sessions delivering prescribed time. Anemia: hemoglobin in prescribed range; iron studies on schedule. Mineral metabolism: phosphate and calcium in the unit's range; PTH measured on schedule. Vascular access: share using fistula, graft or catheter; catheters in place longer than the unit's threshold. Infection: positive blood cultures and IV antibiotic starts per 100 patient-months by access type; seroconversions; vaccination coverage. Fluid and BP: sessions where hourly fluid removal exceeded the unit's limit; sessions with a symptomatic fall in BP. Hospitalization: admissions per 100 patient-months, with reason. Patient experience: short periodic survey; complaints received and resolved. Water and equipment: required water checks logged; results outside limits. Staffing and training: shifts meeting the required nurse-to-station ratio; staff with current life-support training. Text: "This course gives no targets: each target comes from the guideline the unit has adopted for that domain, and the medical director sets it." Formula: Rate per 100 patient-months = events in the month ÷ patients on census that month × 100. Reviewed monthly.
- **Reviewer flags:** None. No targets appear, by design (module FLAGS).

```text
Clinical reference card, 1536 × 1152 (4:3), publication-grade, for a nursing course on renalcarematters.com. Subject: the ten domains of a dialysis unit's monthly quality dashboard, with example measures and no targets. White (#ffffff) background, a calm grid of tiles.

LAYOUT
Title at top left in bold navy #0f1e2e: "The unit quality dashboard". Subtitle in teal #1a6b72: "Reviewed monthly. Built from nursing records."
Top-right badge (amber #b8860b outline, pale amber fill, navy text): "Targets: set by the medical director from the adopted guideline".
Grid of 10 rounded tiles in 2 rows of 5 on soft gray #f3f4f6. Each tile has a simple teal line icon, a bold navy domain name, and two short measures in regular navy. There are no numbers, no gauges and no target lines.
 1 "Dialysis dose": "Reaching urea-clearance target" · "Prescribed time delivered"
 2 "Anemia": "Hemoglobin in prescribed range" · "Iron studies on schedule"
 3 "Mineral metabolism": "Phosphate, calcium in range" · "PTH on schedule"
 4 "Vascular access": "Fistula, graft, or catheter" · "Catheters past unit threshold"
 5 "Infection": "Blood cultures, IV antibiotic starts" · "Seroconversions, vaccination"
 6 "Fluid and BP": "Hourly removal over unit limit" · "Symptomatic BP falls"
 7 "Hospitalization": "Admissions, with reason"
 8 "Patient experience": "Short periodic survey" · "Complaints resolved"
 9 "Water and equipment": "Required water checks logged" · "Results outside limits"
 10 "Staffing and training": "Nurse-to-station ratio met" · "Current life-support training"
Bottom band (full width, pale teal #eef6f7, teal border), formula in bold navy: "Rate per 100 patient-months = events in month ÷ patients on census × 100". Small text below it: "Count infections by access type."
A thin arrow from a small clipboard icon at the far left of the bottom band points up into the grid, labeled "Nursing records".

LABELS (render exactly, nothing else): The unit quality dashboard · Reviewed monthly. Built from nursing records. · Targets: set by the medical director from the adopted guideline · Dialysis dose · Reaching urea-clearance target · Prescribed time delivered · Anemia · Hemoglobin in prescribed range · Iron studies on schedule · Mineral metabolism · Phosphate, calcium in range · PTH on schedule · Vascular access · Fistula, graft, or catheter · Catheters past unit threshold · Infection · Blood cultures, IV antibiotic starts · Seroconversions, vaccination · Fluid and BP · Hourly removal over unit limit · Symptomatic BP falls · Hospitalization · Admissions, with reason · Patient experience · Short periodic survey · Complaints resolved · Water and equipment · Required water checks logged · Results outside limits · Staffing and training · Nurse-to-station ratio met · Current life-support training · Rate per 100 patient-months = events in month ÷ patients on census × 100 · Count infections by access type. · Nursing records · © renalcarematters.com

COLORS: navy #0f1e2e, teal #1a6b72 icons and headings, amber #b8860b badge, soft gray #f3f4f6 tiles, pale teal #eef6f7 band. No red or green traffic-light coding.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No targets, thresholds, percentages, Kt/V values, hemoglobin numbers or ratios such as 1:4
✗ No gauges, speedometers, progress bars or traffic-light colors implying a target
✗ No charts with data points
✗ No domains other than the ten listed
✗ No patient names, unit names or logos
✗ No dark "dashboard screen" look; light background only
✗ No serif font, cartoon icons or clutter
✗ No garbled text and no extra labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ Exactly ten tiles appear with the domain names as written
□ No target, number or traffic-light coding appears in any tile
□ The amber badge about targets is present and legible
□ The formula reads exactly, including "× 100"
□ "Hemoglobin", "Seroconversions" and "Hospitalization" use American spelling and are spelled correctly
□ No gauges or progress bars appear
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 12-C — Typhoon readiness: before, during, after
- **File:** images/nephrology-nursing-12-typhoon-readiness.png
- **Placement:** Module 12, section `readiness` (Disaster and disruption readiness in depth)
- **Job:** A/P. The learner knows the nurse's part in each phase of a disaster, and that the first task afterward is accounting for every patient.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, phased sequence)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Three-phase typhoon readiness sequence for a dialysis unit (before, during, after) with the nurse's tasks and patient teaching for missed dialysis.
- **Caption:** Survival after a disaster is mostly arranged before it. Patients are dialyzed early when the nephrologist orders it, every patient is accounted for by name afterward, and treatment restarts only after the water system has been recommissioned and tested.
- **Source of truth:** m12_x.py `readiness` table. Before, at all times: patient list with at least two contact numbers, on paper as well as on a device; contact tree; written backup-unit arrangements; generator, fuel, supplies; staff call-in plan; the nurse updates contacts and takes part in drills, including manual blood return. Each patient: card with diagnosis, prescription, dry weight, access, serology, medicines, allergies, phone numbers; kept in a waterproof bag. Typhoon forecast: sessions rescheduled earlier on the nephrologist's order; backup units confirmed; the nurse calls patients and identifies flood-prone or isolated patients. During: end treatments safely if utilities fail; record delivered treatment for each patient; no unsafe journeys against the call-in plan. After: account for every patient by name; restart only when the water system is recommissioned and tested (Module 8); backup units meanwhile; report those not reached; patients most overdue placed first. Patient teaching: stricter fluid limit; as little salt as possible (relief goods are salty); avoid high-potassium foods and salt substitutes; keep medicines; keep the catheter dressing dry; go to the ED for breathlessness, chest pain, palpitations, marked weakness, confusion, fever with chills, or access bleeding; say "I am a dialysis patient and I have missed treatment." m12.py `bedside`: closure message has three parts (treatment delivered today, condition and emergency symptoms, where and when the next dialysis is).
- **Reviewer flags:** The module gives no quantities for fluid, potassium or reserve supply, and none are shown. Back-up unit arrangements follow each unit's plan.

```text
Clean clinical preparedness infographic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: what a Philippine dialysis unit and its nurses do before, during and after a typhoon. Flat vector style on a white (#ffffff) background, calm and not alarming.

LAYOUT
Title at top left in bold navy #0f1e2e: "Typhoon readiness for a dialysis unit". Subtitle in teal #1a6b72: "Survival is mostly arranged before the storm".
Main row: three wide rounded columns joined by bold navy right-pointing arrows. Each has a colored top band, a simple line icon and short bullet lines on soft gray #f3f4f6.
 Column 1, "BEFORE" (teal band #1a6b72, cloud-and-calendar icon). Three mini-sections with small bold subheads:
  "Always": "Patient list on paper and device" · "Two contact numbers each" · "Contact tree and backup units" · "Drills, including manual blood return"
  "Each patient": "Card: prescription, dry weight, access, serology, medicines" · "Kept in a waterproof bag"
  "Typhoon forecast": "Early sessions when nephrologist orders" · "Call patients with new schedule" · "Flag flood-prone and isolated patients"
 Column 2, "DURING" (amber band #b8860b, lightning-and-plug icon):
  "End treatments safely if power or water fails" · "Record delivered time and fluid" · "No unsafe journeys to work"
  A boxed three-line inset titled "Before anyone leaves:" reading "1 Treatment delivered today" · "2 Condition and danger signs" · "3 Where and when next dialysis"
 Column 3, "AFTER" (green band #1f7a4d, checklist icon):
  Emphasized first line in bold: "Account for every patient by name" · "Report anyone not reached" · "Most overdue dialyzed first" · "Backup units meanwhile" · "Restart only after water is recommissioned and tested"
Bottom panel (full width, pale teal #eef6f7), titled "Teach patients for days without dialysis", in two halves:
 Left half: "Stricter fluid limit" · "Least salt: relief goods are salty" · "No high-potassium foods or salt substitutes" · "Keep medicines; keep dressing dry"
 Right half, red #b91c1c heading "Go to the ER now:": "Breathlessness · chest pain · palpitations" · "Marked weakness · confusion" · "Fever with chills · access bleeding". Below it, a quote line in a speech bubble: "I am a dialysis patient and I have missed treatment."

LABELS (render exactly, nothing else): Typhoon readiness for a dialysis unit · Survival is mostly arranged before the storm · BEFORE · Always · Patient list on paper and device · Two contact numbers each · Contact tree and backup units · Drills, including manual blood return · Each patient · Card: prescription, dry weight, access, serology, medicines · Kept in a waterproof bag · Typhoon forecast · Early sessions when nephrologist orders · Call patients with new schedule · Flag flood-prone and isolated patients · DURING · End treatments safely if power or water fails · Record delivered time and fluid · No unsafe journeys to work · Before anyone leaves: · 1 Treatment delivered today · 2 Condition and danger signs · 3 Where and when next dialysis · AFTER · Account for every patient by name · Report anyone not reached · Most overdue dialyzed first · Backup units meanwhile · Restart only after water is recommissioned and tested · Teach patients for days without dialysis · Stricter fluid limit · Least salt: relief goods are salty · No high-potassium foods or salt substitutes · Keep medicines; keep dressing dry · Go to the ER now: · Breathlessness · chest pain · palpitations · Marked weakness · confusion · Fever with chills · access bleeding · I am a dialysis patient and I have missed treatment. · © renalcarematters.com

COLORS: navy #0f1e2e, teal #1a6b72, amber #b8860b, green #1f7a4d, red #b91c1c (ER heading only), soft gray #f3f4f6, pale teal #eef6f7.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No fluid amounts, potassium limits, supply day counts or session lengths
✗ No typhoon signal numbers or wind speeds
✗ No dramatic disaster imagery (no flooded bodies, no destroyed buildings, no injured people)
✗ No step suggesting restart before water testing
✗ No real place names, agency logos or phone numbers
✗ No phases in any order other than before → during → after
✗ No dark stormy background; light background only
✗ No serif font, cartoon style or garbled text, and no extra labels

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ Three phases appear in order, with "Account for every patient by name" emphasized in AFTER
□ The three-part closure message appears in DURING
□ The water recommissioning line is present in AFTER
□ No quantities, signal numbers or phone numbers appear
□ The patient quote line is exact
□ "Recommissioned", "serology" and "palpitations" are spelled correctly
□ The imagery is calm, with no disaster casualties
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right

---

### 12-D — Delegation: tasks you may hand over, judgments you keep
- **File:** images/nephrology-nursing-12-delegation.png
- **Placement:** Module 12, section `teamwork` (The dialysis team, delegation, and accountability)
- **Job:** A. The learner can tell a delegable task from a nursing judgment and knows the four conditions for safe delegation.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, comparison)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Side-by-side comparison of tasks a nurse may delegate in a dialysis unit and the three judgments that always stay with the registered nurse.
- **Caption:** A nurse may hand a task to a trained technician or assistant, but not a judgment. Assessment, the decision to start, and evaluation of the response stay with the nurse, and so does the signature.
- **Source of truth:** m12_x.py `teamwork`: a nurse may hand a task to a technician or assistant when the task is within that person's training and the unit's policy, the patient is stable, the instruction is clear, and the nurse remains available to supervise. Tasks named: measuring weight or blood pressure, priming a circuit, cleaning a station. Three things cannot be handed over: the assessment of the patient, the decision that it is safe to start treatment, and the evaluation of how the patient is responding. "A blood pressure reading taken by an assistant is data. Deciding what the reading means for this patient today is the nurse's work, and so is the signature beneath it." m12_x.py QUIZ 1: signing for an assessment not performed creates a false record.
- **Reviewer flags:** Which tasks may be delegated, including priming, is set by facility policy and PRC Board of Nursing issuances (module FLAGS 2). The figure says "per unit policy".

```text
Medical education comparison infographic, landscape 1792 × 1024 (16:9), for a nursing course on renalcarematters.com. Subject: what a registered nurse in a dialysis unit may delegate, and what stays with the nurse. Clean flat vector style on a white (#ffffff) background.

LAYOUT
Title at top center in bold navy #0f1e2e: "Delegate the task, keep the judgment". Subtitle in teal #1a6b72: "Registered nurse accountability in the dialysis unit".
A soft dashed vertical divider splits the canvas into two equal rounded panels.
LEFT panel, heading in green #1f7a4d: "May delegate (per unit policy)". Three task cards, each with a simple line icon:
 - scale icon: "Measure weight"
 - BP cuff icon: "Measure blood pressure"
 - circuit-line icon: "Prime a circuit"
 - spray-and-cloth icon: "Clean a station"
 Beneath them, a small gray-bordered box titled "Only when:" with four check marks: "Within their training and policy" · "Patient is stable" · "Instruction is clear" · "Nurse available to supervise"
RIGHT panel, heading in teal #1a6b72 with a small lock icon: "Stays with the nurse". Three larger cards with navy borders:
 - "Assess the patient"
 - "Decide it is safe to start"
 - "Evaluate the response"
 Beneath them, a pen icon with the line: "Your signature means you did it"
Bridge element across the divider at mid-height: on the left a small BP reading icon labeled "Assistant's reading = data", an arrow crossing the divider, and on the right a nurse silhouette icon (no face detail) labeled "Nurse decides what it means".
Bottom strip (soft gray #f3f4f6, full width), navy text: "Never sign an assessment you did not perform."

LABELS (render exactly, nothing else): Delegate the task, keep the judgment · Registered nurse accountability in the dialysis unit · May delegate (per unit policy) · Measure weight · Measure blood pressure · Prime a circuit · Clean a station · Only when: · Within their training and policy · Patient is stable · Instruction is clear · Nurse available to supervise · Stays with the nurse · Assess the patient · Decide it is safe to start · Evaluate the response · Your signature means you did it · Assistant's reading = data · Nurse decides what it means · Never sign an assessment you did not perform. · © renalcarematters.com

COLORS: navy #0f1e2e text, green #1f7a4d left heading, teal #1a6b72 right heading and lock, soft gray #f3f4f6 panels, white cards.
FONT: Inter only.
FOOTER: "© renalcarematters.com" at the bottom right, small, navy #0f1e2e at 70% opacity.

NEGATIVE CONSTRAINTS
✗ No cannulation, medicine administration or needle insertion listed as delegable
✗ No tasks on the left beyond the four listed
✗ No red "forbidden" crosses over people, and no blame imagery
✗ No law numbers, PRC logos or legal citations on the image
✗ No photorealistic people; simple icons only
✗ No dark background and no serif font
✗ No garbled text and no extra labels
✗ No change to the wording of the three judgments

Render all text exactly as written above in Inter, and add no other text.
```

**QA after generation:**
□ The left panel lists only weight, blood pressure, priming and station cleaning, with "(per unit policy)"
□ All four "Only when" conditions are present
□ The right panel shows exactly the three judgments, worded as written
□ The bridge line distinguishes "data" from what the nurse decides
□ No cannulation or medicines appear as delegable
□ No legal citations or logos appear
□ The background is light, and the font is Inter
□ The footer reads exactly "© renalcarematters.com" at the bottom right


---

Prepared for renalcarematters.com. Figures are teaching aids for the self-study course; they do not replace orders, unit procedures, or manufacturer instructions. © renalcarematters.com
