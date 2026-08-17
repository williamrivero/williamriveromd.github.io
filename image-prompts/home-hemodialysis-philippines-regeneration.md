# Image Regeneration Prompts — Home Hemodialysis in the Philippines

**For:** ChatGPT Image Generator GPT (https://chatgpt.com/g/g-pmuQfob8d-image-generator)
**Guide:** `guides/home-hemodialysis-philippines.html` (live)
**Date:** 2026-08-17
**Replaces:** 5 of the 8 delivered figures. Same filenames, so the guide's
`<picture>` markup, alt text and figcaptions need no edit — only the pixels change.

**Why:** The delivered set was generated from the image plan *before* commit
`d7d99bad`, which converted the guide to American English and added the portable-RO
water strategy. Three defect classes resulted:

1. **British spellings baked into the artwork** while the surrounding prose is American English.
2. **A retired domain in the attribution** — every text-bearing image reads `williamriveromd.com`. That domain is retired and 301-redirects; the house skills now specify `renalcarematters.com` (49 occurrences, zero of the old one).
3. **`water-exposure` contradicts `failure-modes` on dialyzer flow direction** — one shows countercurrent, the other reads as co-current. Two figures in one guide disagreeing on the same anatomy is worse than either being wrong alone.

---

## House rules applied to every prompt (do not remove)

- **Light background only** — white `#ffffff`, off-white `#fafafa`, or soft gray `#f3f4f6`. **Never** navy/black/charcoal.
- Palette: navy `#0f1e2e` (text and lines only), teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`, clinical red `#b91c1c`.
- Fonts: **Inter** (or Nunito Sans / IBM Plex Sans / Manrope) — sans-serif only, never serif or decorative.
- Attribution reads exactly **`renalcarematters.com`** — small, semi-transparent navy, bottom-right (bottom-center for portrait). **Do not write `williamriveromd.com`.**
- **Keep the exact pixel dimensions listed.** These are the sizes actually delivered last time, and the guide's markup already declares them; matching them means zero layout shift and no re-wiring.
- Save both `<name>.png` and a `<name>.webp` companion.

### American English is mandatory — this is the main reason for the rerun

The previous prompts did not forbid British spellings, and the generator produced
them. Every prompt below carries an explicit instruction. Enforce these exact forms
in the rendered artwork:

| Write this | Never this |
|---|---|
| dialyze, dialyzing, dialyzed | dialyse, dialysing, dialysed |
| liter, liters | litre, litres |
| hemolysis, hemoglobin | haemolysis, haemoglobin |
| aluminum | aluminium |
| center, in-center | centre, in-centre |
| authorized, authorization | authorised, authorisation |
| license (noun and verb) | licence |
| enrollment | enrolment |
| hospitalization | hospitalisation |
| favored | favoured |
| labeled, labeling | labelled, labelling |

`dialyzer`, `dialysate` and `dialysis` are already correct in both. Leave the
standard's own title alone if it appears — ISO 23500 is officially spelled
"haemodialysis" — but it does not appear in any figure below.

---

## R3 — `home-hemodialysis-philippines-failure-modes.png`

- **IMAGE TYPE:** Biomedical mechanism schematic, review-article style · **RATIO:** 16:9 · **DIMENSIONS:** 1659 × 948 · **AUDIENCE:** clinicians, dialysis nurses, policymakers
- **DEFECTS BEING FIXED:** `haemolysis` → hemolysis; `aluminium` → aluminum; attribution domain; malformed vertical "COUNTERCURRENT" letterforms.
- **PRESERVE:** the dialyzer port topology, which was **correct** in the delivered version and must not be redrawn from scratch. Verify it against the spec below before accepting.
- **VISUAL GOAL:** Show that the three physiologic failure modes of hemodialysis are unchanged by moving treatment home — only the containment around them moves.
- **PROMPT:**

> Publication-grade biomedical mechanism schematic, scientific review-article style, white `#ffffff` background, flat vector with soft semi-3D shading, thin dashed boxes around magnified panels, generous whitespace, all labels in **Inter**. Muted clinical palette: light gray-blue anatomy, red `#b91c1c` for injury pathways, blue for protective/containment effects, pale pink for the pathology summary box, pale blue for the benefit box.
>
> Title across the top in bold navy `#0f1e2e`: "Why hemodialysis is physiologically demanding wherever it is performed".
>
> LEFT PANEL, labeled "HOME HEMODIALYSIS — chronic intermittent": a seated patient in a simply-drawn domestic room connected to a dialysis machine. Annotate the blood path "300–400 mL/min · ~70–100 L per 4-hour treatment". A thin dashed connector runs from the machine's filter to the magnified panel.
>
> CENTER PANEL, inside a dashed border — a cutaway hollow-fiber dialyzer drawn vertically, fine parallel lines inside suggesting the fiber bundle. **Port topology exactly as follows, do not alter:** ARTERIAL port, blood IN, at the BOTTOM end cap; VENOUS port, blood OUT, at the TOP end cap; DIALYSATE IN as a side port set back from the TOP (venous) end; EFFLUENT OUT as a side port set back from the BOTTOM (arterial) end. Draw a red arrow for blood flowing UP and a blue arrow for dialysate flowing DOWN, and set the word "COUNTERCURRENT" **horizontally** in a small clean label beside them — not rotated vertically, because rotated text rendered with malformed letterforms last time. Annotate "Membrane 1.5–2.1 m² surface area" and "Shell ~500 mL/min · ~120 L dialysate per treatment".
>
> RIGHT COLUMN, three red-bordered warning cards: (1) "VENOUS NEEDLE DISLODGEMENT — blood loss at pump speed; venous-pressure alarm may not detect it"; (2) "DIALYSATE-BORNE EXPOSURE — no gut barrier, no first-pass liver; chloramine → hemolysis, aluminum → CNS and bone, endotoxin → inflammation"; (3) "ULTRAFILTRATION > PLASMA REFILL — intravascular volume falls despite total-body fluid excess → hypotension, myocardial / gut / cerebral stunning".
>
> BOTTOM, three boxes joined by bold arrows: left, pale pink, "Three failure modes" — circuit risks, dialysate risks, volume risks. Center, white with teal border, "What a clinic supplies as a building" — trained staff and immediate response, ISO 23500 water system and routine testing, supervised ultrafiltration and clinical oversight. Right, pale blue, "What must be rebuilt as a service at home" — competency training and ongoing assessment, 24/7 escalation, home water service and testing to ISO 23500, remote monitoring and data review. Close with a full-width line in red-tinted panel: "Moving treatment home does not remove the failure modes — it relocates the containment."
>
> **American English only** — write hemolysis, not haemolysis; aluminum, not aluminium; center, not centre. Attribution "renalcarematters.com", small semi-transparent navy, bottom-right.

- **NEGATIVE:** No replacement-fluid bag, no citrate or anticoagulant line, no CVVH/CRRT components — this is intermittent hemodialysis. Do not place both side ports at the same end, do not swap dialysate and effluent, do not draw dialysate flowing the same direction as blood. No rotated/vertical body text. No needles entering skin, no blood spillage, no distressed patient. No invented pressure or alarm thresholds. No dark backgrounds, no serif fonts, no `williamriveromd.com`.

---

## R4 — `home-hemodialysis-philippines-water-exposure.png`

- **IMAGE TYPE:** Side-by-side comparison · **RATIO:** 16:9 · **DIMENSIONS:** 1659 × 948 · **AUDIENCE:** patients, families, clinicians
- **DEFECTS BEING FIXED:** `dialyse` **in the title**, `litres`, `DIALYSING`, `Aluminium`; attribution domain; **dialyzer drawn co-current, contradicting R3**; missing portable-RO line.
- **VISUAL GOAL:** Make it immediately obvious why water safe to drink is not automatically safe to dialyze with — and that the standard does not relax for a smaller machine.
- **PROMPT:**

> Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white `#ffffff` background, all type in **Inter**. Title centered at top in bold navy `#0f1e2e`: "Safe to drink is not safe to dialyze with". Subtitle in teal `#1a6b72`: "The same water meets two completely different standards". A soft dashed vertical divider splits the canvas into two panels.
>
> LEFT PANEL, header band in renal green `#1f7a4d`, label "DRINKING — about 2 liters a day": a flat-vector drinking glass, then a downward flow through two rounded cards — "GUT WALL — a selective barrier that admits some substances and refuses others", then "LIVER — first-pass clearance before the bloodstream" — ending at a card reading "Standard: household drinking-water quality".
>
> RIGHT PANEL, header band in amber `#b8860b`, label "DIALYZING — about 120 liters per treatment": a flat-vector cutaway hollow-fiber dialyzer. **Draw it countercurrent, matching the companion mechanism figure in this guide:** blood IN at the bottom end, blood OUT at the top end, dialysate IN as a side port near the TOP, effluent OUT as a side port near the BOTTOM, with a red arrow up for blood and a blue arrow down for dialysate. Beside it, two gray cards struck through with a red diagonal — "NO GUT BARRIER" and "NO FIRST-PASS LIVER". Below, three red-accented chips: "Chloramine → red-cell damage", "Aluminum → bone and brain", "Endotoxin fragments → inflammation". End at a teal card: "Standard: ISO 23500 dialysis fluid quality — treated, tested on a schedule, signed off by a technician". Directly beneath that card, one smaller navy line: **"Same standard whether the water comes from a fixed plant or a portable RO unit — a smaller machine treats less water, not dirtier water."**
>
> Centered low between the panels, one bold navy annotation: "≈ 60× the volume, straight past the blood, with neither barrier in between".
>
> Full-width bottom strip on soft gray `#f3f4f6`, one navy sentence: "A clean-tasting tap, a trusted refilling station, or a home filter cannot answer this question on their own."
>
> **American English only** — the title must read "dialyze", the header must read "DIALYZING", quantities in "liters", the metal is "aluminum". Attribution "renalcarematters.com", small semi-transparent navy, bottom-right.

- **NEGATIVE:** Do not draw blood and dialysate flowing the same direction; do not place dialysate IN near the blood-IN end. No photorealistic organs — flat vector only. Do not imply Philippine tap water is unsafe to drink; the comparison is about dialysis standards, not drinking-water safety. Do not show a portable RO unit connected to a bottled-water jug or dispenser. No blood, no needles in skin. No dark backgrounds, no serif fonts, no `williamriveromd.com`.

---

## R5 — `home-hemodialysis-philippines-six-layers.png`

- **IMAGE TYPE:** Multi-panel educational infographic · **RATIO:** 16:9 · **DIMENSIONS:** 1659 × 948 · **AUDIENCE:** patients, families, health journalists
- **DEFECTS BEING FIXED:** `authorised` → authorized; attribution domain; TECHNICAL panel does not name the three water strategies.
- **VISUAL GOAL:** The machine is the smallest part — six systems have to cross the front door, and each must keep working on a bad day.
- **PROMPT:**

> Patient-education infographic poster, landscape, modern nephrology clinic aesthetic, white `#ffffff` background, type in **Inter**. Title top-left in bold navy `#0f1e2e`: "Six things have to cross the front door". Subtitle in teal `#1a6b72`: "The machine is the smallest of them".
>
> LEFT THIRD: a flat-vector elevation of a modest Filipino house with an open front door and a small Philippine flag on a pole. A dialysis machine visible just inside the doorway, drawn deliberately **no larger than the panel icons** — its small size is the message. Six thin navy arrows fan out toward the panel grid.
>
> RIGHT TWO THIRDS: a clean 3 × 2 grid of six equal rounded panels on soft gray `#f3f4f6`, each with a teal `#1a6b72` header bar in white text, one simple flat icon, and at most two lines of navy body text:
> 1. CLINICAL — "Nephrologist oversight, the prescription, vascular-access care, lab monitoring."
> 2. TRAINING — "Weeks of supervised teaching, tested on real competence, then refreshed."
> 3. TECHNICAL — **"A machine authorized for home use and its water arrangement — a fixed treatment plant, a portable RO unit, or pre-made dialysate bags — plus safe wiring, drainage and maintenance."**
> 4. REMOTE SUPPORT — "Someone to call at any hour, records that reach the team, missed treatments noticed."
> 5. EMERGENCY NETWORK — "A plan for power and water failure, a route to hospital, a guaranteed backup slot."
> 6. GOVERNANCE — "Informed choice, home assessment, infection control, incident reporting, who pays for what."
>
> Full-width footer banner in teal `#1a6b72`, white Inter text: "Every layer has to keep working on a bad day — a brownout, a typhoon, a fever at 2 a.m."
>
> **American English only** — write "authorized", not "authorised". Attribution "renalcarematters.com", small semi-transparent navy, just above the teal footer on the right.

- **NEGATIVE:** Do not draw the dialysis machine larger or more prominent than the six panels. No uneven grid, no mismatched panel sizes, no missing teal header bars. No fear imagery, storm damage or alarm symbols. No text walls, no gibberish micro-text. No dark backgrounds, no serif fonts, no `williamriveromd.com`.

---

## R7 — `home-hemodialysis-philippines-trial-evidence.png`

- **IMAGE TYPE:** Clinician reference card / comparison table · **RATIO:** 4:3 · **DIMENSIONS:** 1448 × 1086 · **AUDIENCE:** clinicians, policymakers, payers
- **DEFECTS BEING FIXED:** `IN-CENTRE` ×2, `in-centre` ×2, `favoured`, `haemoglobin` ×2; attribution domain.
- **PRESERVE EXACTLY:** every trial value below is verified against PubMed and was rendered **correctly** last time. This is the guide's most load-bearing figure — it carries the correction to the source blueprint. Proofread character by character before accepting; do not let the generator round, rephrase or "improve" any number.
- **VISUAL GOAL:** Separate what intensified hemodialysis reliably moves (surrogates) from what it has not been shown to move (quality of life, hard outcomes), and flag that the only randomized trial of home delivery was null.
- **PROMPT:**

> Clinical reference infographic card, publication-grade nephrology design, white `#ffffff` background, type in **Inter**. Title in bold navy `#0f1e2e`: "Intensified hemodialysis: what the randomized trials actually showed". Subtitle in teal `#1a6b72`: "Surrogates move. Quality of life and hard outcomes have not been shown to."
>
> A three-row, four-column table. Column headers in white on a teal `#1a6b72` band: "Trial", "Design", "Primary result", "Read it as". Alternating row fills, white and very soft gray `#f3f4f6`. Reproduce the following text exactly:
>
> Row 1 — **FHN Daily Trial (NEJM 2010)** | 245 patients, 6×/week vs 3×/week, IN-CENTER, 12 months | Both coprimary composites favored frequent HD: death or increase in LV mass HR 0.61 (95% CI 0.46–0.82); death or decline in physical-health score HR 0.70 (95% CI 0.53–0.92). Vascular-access interventions increased, HR 1.71 (95% CI 1.08–2.73). | Composites anchored on a SURROGATE (LV mass on MRI). Conducted in-center — evidence about FREQUENCY, not about the home.
>
> Row 2 — **FHN Nocturnal Trial (Kidney Int 2011)** | 87 patients, 6×/week HOME nocturnal vs 3×/week conventional | NEGATIVE on both coprimary outcomes: death or change in LV mass HR 0.68; death or change in physical-health composite HR 0.91 — neither significant. Phosphate and BP control improved. | The only randomized trial of HOME nocturnal HD. Small and underpowered — a failure to demonstrate benefit, not a demonstration of no benefit.
>
> Row 3 — **ACTIVE Dialysis (JASN 2017)** | 200 patients, ≥24 h/week vs 12–15 h/week, in-center and home, 12 months | NO difference in EQ-5D quality of life: mean difference 0.04 (95% CI −0.03 to 0.11), p = 0.29. LV mass substudy null. Lower phosphate and potassium, higher hemoglobin, fewer BP and phosphate-binder medications. | The autonomy argument's own primary endpoint was not met. Medication burden fell — an intermediate outcome.
>
> Beneath the table, three summary chips in one row: renal green `#1f7a4d` "RELIABLY IMPROVES — phosphate, blood pressure, medication burden, hemoglobin (all surrogates or intermediate outcomes)"; amber `#b8860b` "NOT DEMONSTRATED — generic quality of life; benefit of home delivery specifically"; clinical red `#b91c1c` "CONSISTENT COST — vascular-access interventions".
>
> Full-width bottom strip, navy: "A business case built on superior hard outcomes rests on evidence that does not exist. One built on autonomy and eliminated travel rests on something real."
>
> **American English only** — write IN-CENTER and in-center, "favored", "hemoglobin". Attribution "renalcarematters.com", small semi-transparent navy, bottom-right.

- **NEGATIVE:** Do not alter, round or invent any numeric value, confidence interval, sample size, journal or year. Do not drop the word SURROGATE from row 1 or NEGATIVE from row 2. Do not add a fourth trial. **Do not render this as a bar chart or forest plot** — these hazard ratios come from different composite endpoints and must not share an axis. No green checkmarks or red crosses implying an overall verdict on home dialysis. No dark backgrounds, no serif fonts, no `williamriveromd.com`.

---

## R8 — `home-hemodialysis-philippines-readiness-gates.png`

- **IMAGE TYPE:** Gated pathway / vertical algorithm · **RATIO:** 2:3 portrait · **DIMENSIONS:** 1024 × 1536 · **AUDIENCE:** policymakers, regulators, payers, provider leadership
- **DEFECTS BEING FIXED:** `licence`, `authorisation`, `enrolment`, `hospitalisation`; attribution domain.
- **VISUAL GOAL:** A Philippine program has an order of operations, and national clarification is Gate 0 — before any patient is enrolled.
- **PROMPT:**

> Clinical nephrology algorithm, KDIGO guideline flowchart aesthetic, portrait orientation, white `#ffffff` background, type in **Inter**. Title in bold navy `#0f1e2e`: "Five gates before a Philippine home hemodialysis program is ready". Subtitle in teal `#1a6b72`, italic: "A staged policy argument — not an operating blueprint".
>
> Five stacked wide rounded cards joined by bold navy downward arrows, each pair separated by a small teal bar labeled "GATE". Each card has a colored left edge, a bold gate label, and two or three short navy bullets.
>
> GATE 0 — NATIONAL CLARIFICATION, left edge clinical red `#b91c1c`: "Written DOH-HFSRB position: **license** holder, home-site status, device **authorization**, personnel scope, inspection, reporting." · "Written PhilHealth position or a dedicated package." · "PSN-led clinical and program standard aligned to ISO 23500 and manufacturer IFU." Beside this card, a small red-outlined note: "Nothing below this line should begin until Gate 0 is answered in writing."
>
> GATE 1 — SPONSOR AND NETWORK READINESS, amber `#b8860b` edge: an accountable licensed parent hemodialysis clinic or hospital named in writing; named clinical, nursing, technical, supply, data, legal and emergency leads; 24/7 support and contracted backup clinic capacity.
>
> GATE 2 — CONTROLLED PILOT, teal `#1a6b72` edge: small, ethically governed cohort with transparent inclusion and exclusion logic; independent home and social assessment separate from the enrolling provider; predefined stop rules, incident review, guaranteed backup treatment.
>
> GATE 3 — MEASURE BEFORE SCALING, teal edge: "Publish the **enrollment** denominator AND the reasons for non-entry." · "Adverse events, **hospitalization**, technique survival, water and technical failures." · "Household cost, care-partner strain, and equity by income, region and disability."
>
> GATE 4 — SCALE THROUGH HUBS, renal green `#1f7a4d` edge: regional hubs supporting spoke facilities with shared training, pooled procurement, technical coverage and quality dashboards; scale only after safety, affordability, equity and continuity thresholds are met and published.
>
> Bottom strip on soft gray `#f3f4f6`, navy: "No patient should be charged experimental or unclear costs without fully informed agreement and regulatory approval."
>
> **American English only** — write license, authorization, enrollment, hospitalization. Attribution "renalcarematters.com", small semi-transparent navy, bottom-center.

- **NEGATIVE:** No branching paths, decision diamonds, loops or a sixth gate — strictly linear. Do not imply any gate has been cleared in the Philippines: no checkmarks, progress bars, percentages or completion indicators anywhere. No dates, timelines or duration estimates — none are stated in the source. No dark backgrounds, no serif fonts, no `williamriveromd.com`.

---

## Still outstanding after this batch

Regenerating these five leaves the guide internally inconsistent on one point, so
it is worth deciding now rather than later:

| Image | Issue | Recommendation |
|---|---|---|
| 2 `og` | Attribution reads `williamriveromd.com`. Otherwise clean, and it is the social share card — the most publicly visible asset in the set. | Regenerate for the domain alone. Keep 1200 × 630 exactly; the meta tags declare it. |
| 6 `household` | Attribution reads `williamriveromd.com`, and the WATER callout still omits the portable-RO line the guide's prose now carries. | Regenerate with both fixes: "Availability and dialysis suitability are different questions. Some systems use a portable RO unit on an ordinary tap instead of fixed plumbing — often what makes a rented home workable." |
| 1 `vignette-hero` | None. It is wordless by the vignette spec, so it carries no domain and no spelling. | Leave alone. |
| 9 `water-strategies` | Never generated. Its prompt is ready in `image-prompts/home-hemodialysis-philippines.md` under IMAGE 9. | Generate; it is the only figure that carries the three-water-strategy distinction. |

Doing 2, 6 and 9 alongside these five would bring every image in the guide onto the
current domain and the current water-strategy framing in a single pass — eight
regenerations total, which is two batches under the 5-per-60-seconds limit.

## Wiring after generation

Drop the new PNGs into `images/` at the same filenames and save a `.webp`
companion for each. Then:

```bash
python3 patch_img_dimensions.py
python3 generate_latest_guides.py
```

The first confirms the declared `width`/`height` still match the files — if the
generator returns different canvas sizes than the ones listed above, this is what
catches it. The second refreshes the Latest-guides thumbnail if the OG card was
among those regenerated. Alt text and figcaptions are already correct and describe
content that is not changing, so no HTML edit is needed beyond those two scripts.
