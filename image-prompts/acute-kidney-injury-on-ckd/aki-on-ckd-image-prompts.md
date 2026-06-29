# AKI-on-CKD Guide — Image Generation Prompt Pack

**Guide:** `guides/acute-kidney-injury-on-ckd.html`
**Live URL:** https://www.williamriveromd.com/guides/acute-kidney-injury-on-ckd
**Excluded:** `images/acute-kidney-injury-on-ckd-vignette-hero.webp` (keep as-is)

**Stage 1 authoring skills used:**
- `williamriveromd-infographic-skill` (multi-panel + 3D component archetypes)
- `williamriveromd-simple-figure` (single comparison / mechanism / reference card)
- `williamriveromd-algorithm-generator-skill` (clinical algorithm — Style Mode C)

**Paste destination:** https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Save to:** `images/` (deliver both `.png` and `.webp` twins).

House rules every prompt enforces:
- Light background only — white `#ffffff`, off-white `#fafafa`, or soft gray `#f3f4f6`. No navy/charcoal/black fills.
- Approved sans-serif fonts only — Inter, Nunito Sans, IBM Plex Sans, or Manrope. No serif/decorative faces.
- Mandatory footer `williamriveromd.com` — small, semi-transparent navy text, bottom-right (bottom-center for portrait).
- No journal/guideline brand names baked into the image (AJKD, NEJM, KDIGO acronym is fine as guideline terminology).
- Mobile-readable, publication-grade, restrained palette: navy `#0f1e2e`, teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`, red `#b91c1c`, soft purple `#6c3d8e`.

---

## IMAGE 1 — `aki-on-ckd-impact-infographic.png`

```
FILE NAME: aki-on-ckd-impact-infographic.png
IMAGE TYPE: Single-panel comparison poster (Scaffold B Side-by-Side, square crop)
ARCHETYPE: Pathophysiology Mechanism Poster (comparison variant)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Show at a glance why the same AKI insult devastates a CKD kidney compared with a healthy one.

PROMPT:
Create a clean publication-grade medical comparison infographic on a pure white #ffffff background, square 1024 × 1024. Bold condensed sans-serif title centered at the top in navy #0f1e2e set in Inter: "Same Insult, Very Different Outcome — AKI on a Healthy vs CKD Kidney." A short subtitle below in clinical teal #1a6b72 set in Manrope: "Reduced reserve = catastrophic loss of function."

Divide the canvas vertically with a soft dashed gray rule into two equal panels. Each panel sits on a rounded soft-gray #f3f4f6 card with generous whitespace.

LEFT PANEL — label band at top in renal green #1f7a4d reading "Healthy Kidney (≈1,000,000 nephrons)". Centered semi-photorealistic 3D illustration of a single healthy left kidney with vivid normal cortex, normal renal artery and vein. A small caption inside the panel: "Baseline creatinine 1.0 mg/dL." Below the kidney, a small horizontal flow diagram with three pastel pills in a row: a soft amber pill icon labeled "AKI insult (sepsis / dehydration / NSAID)" → a thin teal arrow → a green pill labeled "Recovers fully to baseline." Beneath, a short bullet line in navy: "Large nephron reserve absorbs the hit."

RIGHT PANEL — label band at top in clinical red #b91c1c reading "CKD Kidney (≈250,000 nephrons left)". Centered semi-photorealistic 3D illustration of a shrunken pale CKD kidney with patchy cortical scarring, thinned cortex, and slightly atrophic appearance — anatomically accurate, not cartoonish. Caption inside the panel: "Baseline creatinine 3.0 mg/dL." Below the kidney, the same row layout — an amber pill labeled "Same AKI insult" → red arrow → a deep-red pill labeled "Severe AKI, may not recover." Beneath, navy bullet line: "No reserve — small loss = big effect."

Bottom strip across the full width: a soft teal-tinted #eef6f7 bar containing one centered sentence in navy: "A creatinine rise from 1.0 → 3.0 mg/dL is very different from 3.0 → 5.0 mg/dL." Below it, a small attribution in semi-transparent navy text (≈11px, 70% opacity), bottom-right corner: "williamriveromd.com".

Use only Inter for titles and Manrope for body. Restrained palette: navy #0f1e2e, teal #1a6b72, renal green #1f7a4d, amber #b8860b, red #b91c1c, soft grays. Ample negative space, rounded panel corners, no clutter, no icons that touch labels, no shadows beyond a hair of soft drop on the 3D kidneys.

NEGATIVE INSTRUCTIONS:
No dark, navy, charcoal, or black background. No cartoon or stocky look. No serif or decorative fonts. No fake numbers other than those specified. No watermark other than the small williamriveromd.com attribution. No journal or brand names.

QUALITY CHECK:
Mobile-readable, clinically plausible kidney anatomy, calm and balanced two-column composition, generous whitespace, attribution visible bottom-right.
```

---

## IMAGE 2 — `aki-staging-kdigo-ckd-criteria.png`

```
FILE NAME: aki-staging-kdigo-ckd-criteria.png
IMAGE TYPE: Three-stage reference card (Scaffold E Reference Card, square)
ARCHETYPE: Clinician Reference Card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1254 × 1254
AUDIENCE: clinicians (also readable for patients)
VISUAL GOAL: Communicate KDIGO AKI staging applied to a CKD patient — creatinine + urine-output criteria + action per stage.

PROMPT:
Create a publication-grade clinical reference card on a pure white #ffffff background, square 1254 × 1254. Title centered at the top in bold condensed Inter, navy #0f1e2e: "AKI Staging in a CKD Patient — KDIGO Criteria." Subtitle just under it in Manrope, clinical teal #1a6b72: "Always staged against the patient's own baseline creatinine — not normal ranges."

Body is a vertical stack of three equal-height rounded cards on a very soft gray #f3f4f6 background panel, separated by 24px gaps.

CARD 1 — left accent band in amber #b8860b, label "AKI Stage 1 — Mild." Inside the card, three short rows in Manrope, navy text: "Creatinine ≥ 0.3 mg/dL rise within 48 hr" — "Or 1.5–1.9× baseline within 7 days" — "Or urine output < 0.5 mL/kg/hr × 6–12 hr." Right side of the card, a small rounded teal action chip reading: "Admit. Stop nephrotoxins. Hold ACE/ARB. Avoid NSAIDs and contrast."

CARD 2 — left accent band in red-orange #d65a31, label "AKI Stage 2 — Moderate." Rows: "Creatinine 2.0–2.9× baseline within 7 days" — "Or UO < 0.5 mL/kg/hr × ≥ 12 hr." Right action chip in teal: "Hospital mandatory. Nephrology urgent. Cautious volume — watch overload."

CARD 3 — left accent band in deep crimson #8c1a1a, label "AKI Stage 3 — Severe / RRT." Rows: "Creatinine ≥ 3.0× baseline" — "Or creatinine ≥ 4.0 mg/dL" — "Or UO < 0.3 mL/kg/hr × ≥ 24 hr / anuria ≥ 12 hr" — "Or requires renal replacement therapy." Right action chip in teal: "ICU. Emergent RRT review. Many will not return to pre-AKI baseline."

Below the cards, a single full-width soft teal-tinted #eef6f7 strip with a short navy take-home line in Manrope: "Even Stage 1 in a CKD patient deserves urgent evaluation — reduced reserve = rapid progression." Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Typography: Inter for titles and stage labels, Manrope for body lines. Strong hierarchy: large stage labels, mid-weight criteria, small action chips. No icons. No 3D. No clutter.

NEGATIVE INSTRUCTIONS:
No dark background. No serif or display fonts. No cartoon icons. No journal or guideline brand logos. No invented criteria — render only what is written above. No watermark other than the attribution.

QUALITY CHECK:
Crisp three-stage hierarchy, color band escalation reads at thumbnail size, all text mobile-readable, attribution visible bottom-right.
```

---

## IMAGE 3 — `aki-causes-triple-whammy-infographic.png`

```
FILE NAME: aki-causes-triple-whammy-infographic.png
IMAGE TYPE: Three-category classification + warning panel (Multi-panel Educational, square)
ARCHETYPE: Multi-panel Educational Infographic
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Classify AKI causes into pre-renal, intrarenal, post-renal — and flag the "triple whammy" as the most preventable iatrogenic cause in CKD.

PROMPT:
Create a clean educational infographic on a pure white #ffffff background, square 1024 × 1024. Top title centered, bold Inter, navy #0f1e2e: "Causes of AKI in a CKD Patient." Subtitle below in Manrope, clinical teal #1a6b72: "Where in the kidney did the injury start?"

Top two-thirds: three equal rounded cards in a single horizontal row on a very soft gray #f3f4f6 panel.

CARD A — top accent band in clinical teal #1a6b72, header "PRE-RENAL." Small icon: a simple flat line drawing of a blood-vessel droplet flowing toward a kidney silhouette. Two-line caption in Manrope navy: "Low perfusion. Dehydration, sepsis, heart failure, NSAID-blunted autoregulation. Reversible if caught early."

CARD B — top accent band in soft purple #6c3d8e, header "INTRARENAL." Icon: a simple flat 3D-styled kidney cross-section with a small magnifier showing damaged tubules. Caption: "Direct nephron injury. Contrast dye, aminoglycosides, rhabdomyolysis (myoglobin), interstitial nephritis."

CARD C — top accent band in renal green #1f7a4d, header "POST-RENAL." Icon: a small line drawing of a kidney with an obstructed ureter / bladder outlet. Caption: "Obstruction. BPH (often silent), stones, retained catheter, pelvic tumor."

Bottom one-third: a single full-width alert panel with soft red-tinted #fdecec background and a thin crimson #b91c1c left bar, rounded corners. Inside, top line in Inter bold navy: "⚠ The Triple Whammy — the most preventable AKI in CKD." Then a single line of three medication chips on a soft white pill background, separated by bold red plus signs: "ACE/ARB" + "Diuretic" + "NSAID." Below them a red arrow pointing down and the line in Manrope navy: "+ dehydration from illness → severe AKI." A small footer line under that in teal: "Sick-day rule: hold ACE/ARB and diuretic, avoid NSAIDs, drink fluids, call your nephrologist within 24 hours."

Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Use only Inter for headers and Manrope for body. Restrained colors only. Generous whitespace, no clutter, no cartoon style.

NEGATIVE INSTRUCTIONS:
No dark or navy background. No realistic photos of pills (use simple flat chip shapes). No serif fonts. No brand or journal names. No unrelated drug names beyond ACE/ARB, diuretic, NSAID.

QUALITY CHECK:
Three-card classification reads at a glance, triple-whammy panel pops as a clear warning, attribution visible.
```

---

## IMAGE 4 — `aki-triple-whammy-ace-arb-diuretic-nsaid.png`

```
FILE NAME: aki-triple-whammy-ace-arb-diuretic-nsaid.png
IMAGE TYPE: Single mechanism poster + patient action panel (Scaffold D Mechanism, landscape)
ARCHETYPE: Pathophysiology Mechanism Poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Show how three common medications combine with dehydration to drop glomerular perfusion and cause AKI in a CKD patient — and the concrete patient action plan.

PROMPT:
Create a clean publication-grade pathophysiology infographic on a pure white #ffffff background, landscape 1536 × 1024. Title at top-left in bold Inter, navy #0f1e2e: "The Triple Whammy in a CKD Patient." Subtitle in Manrope, clinical teal #1a6b72: "Three everyday drugs + one sick day → severe AKI."

Left two-thirds — mechanism panel.
At the center, a clean semi-photorealistic 3D-rendered glomerulus with a clearly visible afferent arteriole on the left and efferent arteriole on the right, normal palette, anatomically correct. Around the glomerulus, three labeled medication "chips" on a soft gray #f3f4f6 background, each connected to its target arteriole with a thin teal arrow:

- TOP-LEFT chip in soft red #fdecec with crimson label "NSAID (mefenamic acid / ibuprofen / naproxen)." Arrow points to the afferent arteriole with the small caption "↓ prostaglandins → constricts afferent."
- BOTTOM-LEFT chip in soft amber #fdf6e3 with amber #b8860b label "Diuretic (furosemide / HCTZ)." Arrow points to a small water-droplet icon next to the glomerulus with caption "↓ intravascular volume."
- RIGHT chip in soft teal #eef6f7 with teal label "ACE inhibitor / ARB." Arrow points to the efferent arteriole with caption "Blocks efferent constriction → ↓ glomerular pressure."

Below the glomerulus, a single horizontal flow strip: a navy capsule "Dehydration (vomiting / diarrhea / fever)" → red arrow → a red capsule "Glomerular filtration collapses" → red arrow → a deep-red rounded box "Severe AKI on CKD."

Right one-third — patient action panel on a rounded soft renal-green #eaf4ee card.
Header in Inter, renal green #1f7a4d: "If you have vomiting, diarrhea, or fever:" followed by five short numbered lines in Manrope navy, each preceded by a small green dot:

1. Hold your ACE inhibitor / ARB.
2. Hold your diuretic.
3. Avoid all NSAIDs.
4. Drink water or oral rehydration salts (ORS).
5. Call your nephrologist within 24 hours.

Bottom strip across the full width — a soft teal-tinted #eef6f7 thin bar with one sentence in Manrope navy: "Restart medications only after you feel better and are eating normally — confirm with your nephrologist."

Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Typography: Inter for headers and chip labels, Manrope for body. Restrained palette only. Realistic anatomy on the glomerulus, no cartoon. Generous whitespace; no clutter; no extra drug names beyond those listed.

NEGATIVE INSTRUCTIONS:
No dark background. No photorealistic pill bottles. No serif fonts. No brand names (use generic drug-class chips). No invented mechanism arrows. No watermark other than the attribution.

QUALITY CHECK:
Glomerular anatomy correct (afferent left, efferent right). Three medications clearly map to their targets. Patient action panel is scannable. Attribution visible bottom-right.
```

---

## IMAGE 5 — `aki-dialysis-modality-crrt-ihd-sled.png`

```
FILE NAME: aki-dialysis-modality-crrt-ihd-sled.png
IMAGE TYPE: Clinical decision tree (Algorithm-Generator Style Mode C, williamriveromd.com house style)
ARCHETYPE: Clinical Algorithm / Flowchart
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A clean top-to-bottom decision flowchart for choosing CRRT vs IHD vs SLED in AKI-on-CKD based on hemodynamic stability and dominant indication.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart on a pure white #ffffff background, landscape 1536 × 1024, in the williamriveromd.com house style. Title at top center in bold Inter, navy #0f1e2e: "Choosing the Dialysis Modality in AKI-on-CKD." Subtitle in Manrope, clinical teal #1a6b72: "Driven by hemodynamic stability and dominant indication."

Top entry node — rounded teal #1a6b72 rectangle, white text in Inter: "AKI-on-CKD with RRT indication (AEIOU)." From it, a thin navy arrow drops to a soft-amber #fdf6e3 diamond decision node in Inter, amber #b8860b text: "Hemodynamically stable? (MAP ≥ 65 mmHg, no vasopressors)."

Two branches:

LEFT branch labeled "No — unstable / shock" in red bold:
- Down arrow to a teal-bordered rounded rectangle on soft teal #eef6f7 background: "CRRT (CVVHDF preferred)." Inside the box, three short Manrope navy bullets: "Slow continuous solute and fluid removal" — "Best for septic shock, multi-organ failure" — "Typical: 20–25 mL/kg/hr effluent."
- Below it, a soft-gray side note in Manrope: "Re-evaluate daily — transition to IHD when stable."

RIGHT branch labeled "Yes — stable" in renal green bold:
- Down arrow to a second smaller amber diamond: "Severe hyperkalemia or rapid toxin removal needed?"
  - Sub-branch LEFT "Yes" in red, down arrow to a teal rectangle "IHD (Intermittent HD)" with Manrope bullets: "Fastest K+ correction" — "3–4 hr session, 3×/week" — "Reduce K+ gradient to avoid arrhythmia."
  - Sub-branch RIGHT "No / cautious" in amber, down arrow to a teal rectangle "SLED (Sustained Low-Efficiency Dialysis)" with bullets: "Hybrid — 6–12 hr daily" — "Gentler than IHD, simpler than CRRT" — "Good for marginal stability."

Bottom common endpoint — a renal-green rounded rectangle on soft green #eaf4ee: "Goal: optimize for renal recovery — 30–40% of AKI-on-CKD patients can be weaned off dialysis." Connect from CRRT, IHD, and SLED boxes with thin teal arrows.

Soft gray side note bottom-left in Manrope: "Avoid contrast, NSAIDs, and nephrotoxins throughout."

Use only Inter for node titles and Manrope for body bullets. Thin teal connectors, rounded boxes, diamonds for decisions. Generous whitespace, balanced left-right tree. Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

NEGATIVE INSTRUCTIONS:
No dark background. No 3D elements or icons in nodes. No serif fonts. No brand or machine names (no "Prismaflex", no "Fresenius"). No spaghetti arrows. No invented modalities.

QUALITY CHECK:
Top-down decision logic clear at a glance. Hemodynamic-stability split is the dominant branch. Endpoints converge on recovery. Attribution visible bottom-right.
```

---

## IMAGE 6 — `aki-ckd-recovery-outcomes-infographic.png`

```
FILE NAME: aki-ckd-recovery-outcomes-infographic.png
IMAGE TYPE: Three-outcome breakdown (Scaffold C Step Sequence, square)
ARCHETYPE: Multi-panel Educational Infographic (outcomes variant)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Convey the three outcome groups after AKI on a CKD background — 30% full recovery, 40% partial recovery at a lower baseline, 30% direct progression to ESKD.

PROMPT:
Create a publication-grade outcomes infographic on a pure white #ffffff background, square 1024 × 1024. Title centered top, bold Inter, navy #0f1e2e: "After AKI-on-CKD — Three Possible Outcomes." Subtitle in Manrope, clinical teal #1a6b72: "Only one in three returns to the pre-AKI baseline."

Center top — a horizontal segmented bar 70% of the canvas width, height ~32px, rounded ends, three contiguous color segments labeled below: 30% renal green #1f7a4d (left), 40% amber #b8860b (middle), 30% clinical red #b91c1c (right). Above each segment, a small percentage label in Inter bold matching the segment color.

Below the bar, three equal-width rounded cards on a very soft gray #f3f4f6 panel, separated by 24px gaps.

CARD 1 — left accent band in renal green #1f7a4d. Header in Inter: "30% — Full Recovery." Sub-line in Manrope navy: "Returns to pre-AKI baseline." Icon: simple flat line illustration of a healthy kidney with a small green up-arrow. Two short Manrope bullets: "Mild AKI (Stage 1–2) caught early" — "Pre-renal cause reversed quickly."

CARD 2 — left accent band in amber #b8860b. Header: "40% — Partial Recovery." Sub-line: "Stable but at a lower new baseline." Icon: flat kidney silhouette with a small horizontal arrow stepping down to a new level. Bullets: "Some nephron loss is permanent" — "New baseline becomes the patient's reference."

CARD 3 — left accent band in clinical red #b91c1c. Header: "30% — Progression to ESKD." Sub-line: "Permanent dialysis required." Icon: a flat kidney with a small red downward arrow into a stylized dialysis-machine silhouette. Bullets: "Most common when AKI Stage 3 + advanced CKD" — "Each AKI episode raises ESKD risk further."

Bottom strip — a full-width soft teal-tinted #eef6f7 bar with a single Manrope navy line: "Prevention of the next AKI episode is the single most important post-discharge goal."

Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Use only Inter for headers and Manrope for body. Restrained palette only. Strict alignment, clean rounded cards, no cartoon icons.

NEGATIVE INSTRUCTIONS:
No dark background. No serif fonts. No pie chart — use the horizontal segmented bar exactly as specified. No invented statistics other than the 30 / 40 / 30 split. No brand or guideline logos.

QUALITY CHECK:
Bar segments read at thumbnail size. Color escalation (green → amber → red) matches recovery quality. Cards aligned. Attribution visible.
```

---

## IMAGE 7 — `ckd-sick-day-rules-filipino-patient.png`

```
FILE NAME: ckd-sick-day-rules-filipino-patient.png
IMAGE TYPE: Photorealistic editorial + 2D infographic overlay (mixed media, landscape)
ARCHETYPE: Multi-panel Educational Infographic
ASPECT RATIO: 5:4
PIXEL DIMENSIONS: 1402 × 1122
AUDIENCE: patients (Filipino CKD patients, their families)
VISUAL GOAL: A warm, authentic Filipino home scene of a patient correctly following the sick-day rules, paired with a clean side-panel checklist.

PROMPT:
Create a premium patient-education infographic on a pure white #ffffff background, landscape 1402 × 1122. Title at top-left in bold Inter, navy #0f1e2e: "Sick-Day Rules for CKD." Subtitle in Manrope, clinical teal #1a6b72: "When you have vomiting, diarrhea, or fever — do these five things."

Left two-thirds — a single photorealistic editorial photograph of a middle-aged Filipina woman with a calm, focused expression, seated at a clean Filipino dining table beside a softly lit window. She is gently holding a glass of clear oral rehydration salts (ORS) solution. On the table next to her: a weekly pill organizer with one compartment clearly marked with a small red "DO NOT TAKE TODAY" sticker on the lid, a paper sheet with the printed sick-day rules visible but not legible, and a smartphone open in her other hand mid-call (slight motion blur on the phone is fine). Soft natural daylight, bright airy interior, soft beige walls, simple Filipino home aesthetic, shallow depth of field, no clinical equipment in view. Realistic Filipino skin tone and features, mid-50s, hair in a soft low bun, simple cotton blouse. Documentary tone, not stocky.

Right one-third — a clean infographic side panel on a soft renal-green #eaf4ee rounded card with a thin renal green #1f7a4d left bar. Header in Inter, renal green: "5 things to do today." Then five numbered rows in Manrope navy, each row preceded by a small green check icon, ample spacing:

1. STOP your ACE inhibitor or ARB.
2. STOP your diuretic (furosemide / HCTZ).
3. NEVER take NSAIDs (mefenamic acid, ibuprofen, naproxen).
4. Drink extra water or ORS.
5. Call your nephrologist within 24 hours.

Bottom strip across the full width — a thin soft teal-tinted #eef6f7 band with one Manrope navy sentence: "Restart your medications only when you feel better and are eating normally — confirm with your nephrologist."

Attribution bottom-right in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Typography: Inter for headers, Manrope for body and the side-panel checklist. Bright, airy, warm Filipino home palette harmonizing with renal green and teal accents. The photograph should feel authentic and reassuring, not staged. The infographic side panel sits cleanly over white space and does not overlap the patient.

NEGATIVE INSTRUCTIONS:
No dark, dim, or moody lighting. No hospital or clinical setting — this is a home scene. No clutter on the table. No legible product brand names on the pill organizer or paper. No serif fonts. No cartoon icons in the side panel — simple flat checks only. No watermark other than the attribution.

QUALITY CHECK:
Filipino patient looks authentic mid-50s, hands and face well-rendered, light bright airy mood, side panel checklist scannable, attribution visible bottom-right.
```

---

## IMAGE 8 — `aki-medication-safety-hold-adjust.png`

```
FILE NAME: aki-medication-safety-hold-adjust.png
IMAGE TYPE: Two-column drug-safety reference card (Scaffold E Reference Table, portrait)
ARCHETYPE: Clinician Reference Card
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians (also useful for informed patients)
VISUAL GOAL: A clean two-column reference: drugs to STOP immediately in AKI vs drugs needing DOSE ADJUSTMENT, with a short footer on safe pain control.

PROMPT:
Create a publication-grade clinical reference card on a pure white #ffffff background, portrait 1024 × 1536. Title centered at top in bold Inter, navy #0f1e2e: "Medication Safety in AKI-on-CKD." Subtitle in Manrope, clinical teal #1a6b72: "What to stop. What to dose-adjust."

Body — two equal-width vertical columns on a very soft gray #f3f4f6 background panel, separated by a thin dashed gray rule.

LEFT COLUMN — header band in clinical red #b91c1c, white Inter text: "STOP IMMEDIATELY." Below the header, a vertical list of rounded white cards, each with a small red dot on the left and a Manrope navy drug-class entry. Items, in order:

- NSAIDs (mefenamic acid, ibuprofen, naproxen) — permanent avoidance in CKD.
- Metformin — risk of lactic acidosis when eGFR drops further.
- ACE inhibitors / ARBs — hold during illness; restart when stable.
- SGLT2 inhibitors — pause during acute illness with reduced intake.
- LMWH (enoxaparin) at therapeutic dose — bleeding risk in AKI; reassess.
- Aminoglycosides without monitoring — direct tubular injury.
- IV contrast without hydration — direct nephrotoxicity.
- Herbal remedies, aristolochic-acid–containing preparations — irreversible injury.

RIGHT COLUMN — header band in amber #b8860b, white Inter text: "DOSE-ADJUST." Vertical list of rounded white cards with a small amber dot on the left and Manrope navy entries:

- Furosemide — titrate to urine output, watch electrolytes.
- Gentamicin / amikacin — extended interval, trough-guided, monitor.
- Digoxin — lower dose; check level.
- Insulin — reduce dose; renal clearance falls in AKI.
- Direct oral anticoagulants (apixaban, rivaroxaban) — recheck CrCl-based dosing.
- Most antibiotics — adjust per eGFR (cefepime, vancomycin, piperacillin-tazobactam).
- Opioids — avoid morphine and codeine; prefer fentanyl or hydromorphone.
- Allopurinol — reduce dose; monitor for hypersensitivity.

Bottom strip across the full width — a soft teal-tinted #eef6f7 rounded panel with two short Manrope navy lines:
- "For pain: paracetamol 500–1000 mg up to 4× daily is safe."
- "All medication changes should be guided by your nephrologist."

Attribution bottom-center in semi-transparent navy (≈11px, 70% opacity): "williamriveromd.com".

Typography: Inter for headers and column titles; Manrope for all drug entries and footer lines. Strict alignment — every card the same width and spacing. Restrained color palette only. No icons inside cards beyond the small dot.

NEGATIVE INSTRUCTIONS:
No dark background. No serif fonts. No fake or extra drugs beyond those listed. No brand names beyond the generic names specified. No pictures of pills. No watermark other than the attribution.

QUALITY CHECK:
Two-column hierarchy reads cleanly. Red vs amber color coding is instantly recognizable. Every line is legible at mobile width. Attribution visible bottom-center.
```

---

## Wiring notes (Stage 2)

After generation in the ChatGPT Image Generator GPT, save each output to the
project's `images/` folder as both `.png` and `.webp` using the file names above.
All eight `<img>` references in
`guides/acute-kidney-injury-on-ckd.html` already point at these file names —
no HTML edits are required. The og:image (`aki-staging-kdigo-ckd-criteria.png`)
will refresh automatically once the new file lands at the same path.

The vignette-hero (`acute-kidney-injury-on-ckd-vignette-hero.webp`) is
intentionally untouched per the request.
