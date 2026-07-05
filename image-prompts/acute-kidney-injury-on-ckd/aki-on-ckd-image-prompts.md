# AKI-on-CKD Guide — Image Prompt Pack v2 (Mechanism-Figure Style)

**Guide:** `guides/acute-kidney-injury-on-ckd.html`
**Live URL:** https://renalcarematters.com/guides/acute-kidney-injury-on-ckd
**Excluded:** `images/acute-kidney-injury-on-ckd-vignette-hero.webp` (keep as-is)
**Authored with:** `williamriveromd-biomedical-mechanism-figure`

## House aesthetic — non-negotiable across all eight figures

A single visual system, as if every figure came from the same review article:

- **Layout:** organ-level panel on the left → dashed magnified inset(s) in the
  center/right → bottom three-box flow (injury drivers → mechanism / intervention
  → benefit / outcome).
- **Style:** flat vector medical illustration with soft semi-3D shading, white
  background, thin dashed connector lines, generous whitespace, no photorealism,
  no decorative effects, no shadows beyond a faint shading on anatomy.
- **Palette (only these):** light gray-blue `#cdd9e5` for normal anatomy, soft
  yellow `#f5e6a3` to highlight affected segments, brick red `#b91c1c` for
  arteries / injury / oxidative stress, soft blue `#5a8fb0` for veins / protective
  effects, pale pink `#fde8ec` for pathology summary boxes, pale blue `#e3eef5`
  for treatment/benefit summary boxes, navy `#0f1e2e` for text only, clinical
  teal `#1a6b72` for headings only.
- **Typography:** Inter for titles, IBM Plex Sans for anatomy labels, Manrope
  for body. No serif, no display, no decorative type. Explicitly stated in each
  prompt.
- **Attribution:** `© williamriveromd.com` in semi-transparent navy, ~10–11px,
  bottom-right (bottom-center for portrait). The only mark permitted.
- **Mechanism over decoration:** every callout teaches something — directional
  arrows (↓ GFR, ↑ ROS, ↓ ATP), not generic icons.

The set should read as a coherent review-article figure series — Figs 1–8 of an
imaginary "Acute Kidney Injury in Chronic Kidney Disease — Pathophysiology and
Management" review.

---

## FIGURE 1 — `aki-on-ckd-impact-infographic.png`  ·  Nephron reserve hypothesis

```
Create a publication-grade biomedical mechanism schematic about:

Topic: Why the same AKI insult devastates a CKD kidney — the nephron-reserve hypothesis.

Disease context: Acute kidney injury superimposed on chronic kidney disease (AKI-on-CKD).

Central mechanism: Loss of functional nephron reserve in CKD means the same injury produces a disproportionately larger drop in glomerular filtration rate and a far smaller probability of complete recovery.

Layout: Square 1024 × 1024, white background, review-article schematic. Two parallel "organ → nephron → outcome" tracks, stacked top and bottom, separated by a thin dashed gray rule with the central label "Same AKI insult" written along it in IBM Plex Sans, navy #0f1e2e.

TOP TRACK — "Healthy Kidney (≈ 1,000,000 nephrons, baseline Cr 1.0 mg/dL)" label on the left in Inter, teal #1a6b72.
- Organ panel (left): a simplified left kidney cross-section in light gray-blue #cdd9e5 with normal cortex thickness, normal renal artery in brick red #b91c1c, vein in soft blue #5a8fb0. A thin dashed connector points right to:
- Magnified inset (dashed border): a small population schematic showing a tight cluster of ~30 healthy nephron icons in light gray-blue with three of them softly highlighted in pale yellow #f5e6a3 labeled "injured nephrons (~10%)" and an arrow note "↓ GFR transient." A small mini-callout shows one functional nephron close-up with a simple glomerulus + proximal tubule + loop + distal/collecting in light gray-blue.
- Outcome chip (right): pale blue #e3eef5 rounded box, "Full recovery — large reserve absorbs the hit."

BOTTOM TRACK — "CKD Kidney (≈ 250,000 nephrons, baseline Cr 3.0 mg/dL)" label in Inter, teal.
- Organ panel (left): the same kidney silhouette but smaller and slightly contracted, light gray-blue with patchy soft-yellow cortical scarring overlay, thinned cortex, the same red artery and blue vein but visibly narrower. Dashed connector to:
- Magnified inset (dashed border): a sparser nephron population — only ~8 nephron icons, with three of them softly highlighted in pale yellow labeled "injured nephrons (same absolute number, ~40% of remaining)" and an arrow note "↓↓ GFR collapse." Close-up nephron callout shows tubular atrophy hatching.
- Outcome chip (right): pale pink #fde8ec rounded box, "Severe AKI — incomplete recovery, ↑ ESKD risk."

Bottom three-box flow (full width, separated by thin teal arrows in IBM Plex Sans labels):
- Left pink #fde8ec pathology box "Injury drivers": "Sepsis · Dehydration · Nephrotoxins · NSAIDs."
- Center white box with dashed outline "Mechanism": "Loss of autoregulation · ↓ Tubular repair · Chronic inflammation · Reduced reserve."
- Right blue #e3eef5 benefit/outcome box "Outcome in CKD": "Larger ΔCr per unit injury · ↑ Time to recovery · ↑ Progression to ESKD."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connector lines. Generous whitespace. No photorealism, dark backgrounds, decorative elements, or overcrowding.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px, not obscuring any figure element.
```

---

## FIGURE 2 — `aki-staging-kdigo-ckd-criteria.png`  ·  Anatomy of KDIGO staging

```
Create a publication-grade biomedical mechanism schematic about:

Topic: KDIGO AKI staging applied to a CKD kidney — anatomical and biochemical correlates of each stage.

Disease context: AKI-on-CKD with depleted nephron reserve, where staging must be referenced to the patient's own baseline creatinine.

Central mechanism: Stepwise loss of tubular function (Stage 1 sublethal injury → Stage 2 widespread tubular dysfunction → Stage 3 tubular necrosis ± collapse of solute clearance) with parallel rises in serum creatinine and falls in urine output.

Layout: Square 1254 × 1254, white background, review-article schematic. A central kidney organ panel on the left flowing into three vertically stacked dashed nephron insets on the right, each corresponding to one KDIGO stage. A small criteria column sits to the right of each inset.

Organ panel (left, full height): a single anatomically simple kidney cross-section in light gray-blue #cdd9e5 showing cortex, medulla, papilla, ureter. Three thin dashed connectors emerge from the cortex pointing right to the three nephron insets, labeled "Stage 1", "Stage 2", "Stage 3" in IBM Plex Sans, navy #0f1e2e.

Magnified mechanism insets (three dashed boxes, stacked top-to-bottom):

Top inset — "STAGE 1 — Mild" in Inter, amber-orange tone applied only to the label (#b8860b). Schematic of a single nephron in light gray-blue with the proximal tubule lightly tinted soft yellow #f5e6a3 to denote sublethal injury. Small callouts inside the inset: "Brush-border loss" · "Mitochondrial stress (↓ ATP)" · "Reversible."
Right-side criteria card (pale gray rounded panel, navy Manrope text):
"↑ Cr ≥ 0.3 mg/dL within 48 hr · or 1.5–1.9 × baseline within 7 d · or UO < 0.5 mL/kg/hr × 6–12 hr."
Below the card a thin teal action line: "Admit · stop nephrotoxins · hold ACE/ARB."

Middle inset — "STAGE 2 — Moderate" label in deeper amber-red #d65a31. Same nephron with proximal tubule fully soft-yellow plus the thick ascending limb of Henle tinted soft yellow. Callouts: "Tubular dysfunction" · "↑ ROS" · "Cast formation begins."
Criteria card: "Cr 2.0–2.9 × baseline within 7 d · or UO < 0.5 mL/kg/hr × ≥ 12 hr."
Action line: "Mandatory admission · cautious volume · nephrology urgent."

Bottom inset — "STAGE 3 — Severe / RRT" label in deep crimson #8c1a1a. Same nephron with proximal tubule, loop of Henle, and distal tubule all heavily soft-yellow with brick-red #b91c1c hatching to denote tubular necrosis; a faint dashed outline shows nephron dropout. Callouts: "Tubular necrosis" · "Loss of glomerular filtration" · "Many do not return to baseline."
Criteria card: "Cr ≥ 3.0 × baseline · or Cr ≥ 4.0 mg/dL · or UO < 0.3 mL/kg/hr × ≥ 24 hr · or anuria ≥ 12 hr · or requires RRT."
Action line: "ICU · emergent RRT review · goals-of-care discussion if frail."

Bottom three-box flow:
- Left pink #fde8ec pathology box "Substrate": "Reduced nephron reserve · Lower baseline GFR · Less repair capacity."
- Center white dashed box "Why staging is relative": "Use the patient's own recent baseline Cr — normal reference ranges underestimate AKI severity."
- Right blue #e3eef5 benefit box "Clinical value": "Earlier admission · earlier nephrology · earlier RRT planning improves recovery odds."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connectors. Generous whitespace. No photorealism, dark backgrounds, or overcrowding.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 3 — `aki-causes-triple-whammy-infographic.png`  ·  Three sites of injury

```
Create a publication-grade biomedical mechanism schematic about:

Topic: The three anatomical sites of AKI injury in a CKD kidney — pre-renal, intrarenal, post-renal — and the iatrogenic "triple whammy" that drives most preventable cases.

Disease context: AKI-on-CKD in adults.

Central mechanism: Each anatomical compartment fails through a distinct mechanism: pre-renal = hypoperfusion, intrarenal = direct nephron toxicity, post-renal = obstruction. The triple whammy of ACE inhibitor/ARB + diuretic + NSAID converges on pre-renal hypoperfusion in an already low-reserve kidney.

Layout: Square 1024 × 1024, white background, review-article schematic. A single large kidney cross-section anchors the left two-thirds of the image. Three dashed magnified insets surround it — one per anatomical site — with thin dashed connectors back to the relevant anatomy.

Organ panel (center-left, taking ~60% of canvas): an anatomically simple kidney in light gray-blue #cdd9e5 with cortex, medulla, renal pelvis, ureter, renal artery in brick red #b91c1c, renal vein in soft blue #5a8fb0. Three small numbered markers on the anatomy: ① on the renal artery / afferent territory, ② in the cortical tubular region, ③ on the renal pelvis / ureter.

Magnified mechanism insets (three dashed boxes, arranged around the kidney):

Inset ① TOP-RIGHT — "PRE-RENAL" in Inter, teal #1a6b72. Schematic of an afferent and efferent arteriole feeding a glomerulus; the afferent is constricted (narrowed lumen) in brick red. Small callouts: "↓ Perfusion pressure" · "↓ GFR (functional, reversible)" · "Triggers: dehydration · sepsis · heart failure · NSAID-blunted autoregulation."

Inset ② MIDDLE-RIGHT — "INTRARENAL" in Inter, deep crimson #8c1a1a. Magnified proximal tubule cell with soft-yellow #f5e6a3 cytoplasm and brick-red hatching on the brush border; a small inset shows a mitochondrion with red ROS dots. Callouts: "Direct tubular injury" · "Contrast · aminoglycosides · myoglobin (rhabdo)" · "Acute tubular necrosis."

Inset ③ BOTTOM-RIGHT — "POST-RENAL" in Inter, soft blue #5a8fb0. A schematic of a dilated renal pelvis with hydronephrosis (calyces ballooned, light gray-blue) and a stylized obstruction in the ureter (small soft-yellow blockade). Callouts: "Obstruction" · "BPH (often silent) · stones · catheter · pelvic mass" · "Reversed by relief."

Bottom three-box flow (full width):
- Left pink #fde8ec pathology box "The triple whammy (iatrogenic pre-renal AKI)": three rounded pill chips in a row — "ACE inhibitor / ARB" + "Diuretic" + "NSAID" — connected by red plus signs, with a small arrow note "+ dehydration from illness."
- Center white dashed box "Mechanism convergence": "↓ Efferent tone (ACE/ARB) · ↓ Intravascular volume (diuretic) · ↓ Afferent prostaglandins (NSAID) → glomerular pressure collapses."
- Right blue #e3eef5 benefit/outcome box "Prevention": "Sick-day rules · Hold ACE/ARB and diuretic · Avoid NSAIDs · Hydrate · Call nephrology within 24 hr."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connector lines. Generous whitespace. No photorealism, no dark backgrounds, no decorative elements.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 4 — `aki-triple-whammy-ace-arb-diuretic-nsaid.png`  ·  Glomerular mechanism of the triple whammy

```
Create a publication-grade biomedical mechanism schematic about:

Topic: How ACE inhibitor / ARB + diuretic + NSAID, layered on dehydration, collapse glomerular filtration in a CKD patient.

Disease context: Iatrogenic pre-renal AKI on a background of CKD — the single most preventable cause of AKI hospitalization in CKD.

Central mechanism: Each drug class disables one of the three compensatory mechanisms that defend GFR when perfusion falls. With all three blocked simultaneously, even mild dehydration drops filtration fraction below the threshold for adequate clearance.

Layout: Landscape 1536 × 1024, white background, review-article schematic. Left third = organ-level panel; center two-thirds = magnified glomerular mechanism inset; bottom = three-box summary flow.

Organ panel (left): an anatomically simple kidney in light gray-blue #cdd9e5 with renal cortex highlighted and a single afferent arteriole visible at cortical level. A thin dashed connector with a small magnifier icon points right into the central inset, labeled "Cortical nephron" in IBM Plex Sans.

Magnified mechanism panel (center, dashed border, large): a single glomerulus rendered as a clean review-figure schematic — Bowman's capsule in light gray-blue, glomerular tuft as a soft pale yellow loop, afferent arteriole entering from the left in brick red #b91c1c, efferent arteriole exiting to the right in soft blue #5a8fb0, and proximal tubule emerging on the lower right. Three drug-action arrows, each labeled with a small rounded chip:

- NSAID chip (top-left of glomerulus) in pale pink #fde8ec, brick-red label "NSAID — mefenamic acid · ibuprofen · naproxen." Red arrow points to the afferent arteriole with annotation "↓ Prostaglandin-mediated vasodilation → afferent constriction."
- DIURETIC chip (bottom-left) in pale amber #fdf6e3 with amber #b8860b label "Diuretic — furosemide · HCTZ." Amber arrow points to a small water-droplet icon next to the afferent vessel with annotation "↓ Intravascular volume → ↓ Renal perfusion."
- ACE/ARB chip (top-right) in pale blue #e3eef5 with soft-blue label "ACE inhibitor / ARB." Blue arrow points to the efferent arteriole with annotation "Blocks Ang II → ↓ Efferent tone → ↓ Glomerular pressure."

A small dotted line frames the glomerulus and labels: "Net effect: filtration fraction collapses." Underneath the glomerulus, a thin gauge graphic in soft red showing "GFR ↓↓".

To the lower-right of the inset, a second small dashed inset shows the same glomerulus after the sick-day rules are applied — afferent vessel widened back to normal, efferent vessel slightly contracted, soft-yellow tuft restored — labeled "After hold + hydration."

Bottom three-box flow:
- Left pink #fde8ec pathology box "Injury drivers": "Vomiting · diarrhea · fever · poor oral intake on a CKD baseline."
- Center white dashed box "Intervention — sick-day rules": numbered Manrope list (1) Hold ACE/ARB · (2) Hold diuretic · (3) Avoid all NSAIDs · (4) Drink water or ORS · (5) Call nephrology within 24 hr.
- Right blue #e3eef5 benefit box "Outcome": "Restored efferent tone · Restored perfusion · Avoided hospitalization · Preserved nephron mass."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connectors. Anatomically accurate glomerular geometry. Generous whitespace.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 5 — `aki-dialysis-modality-crrt-ihd-sled.png`  ·  Solute clearance kinetics by modality

```
Create a publication-grade biomedical mechanism schematic about:

Topic: Choosing between CRRT, IHD, and SLED in AKI-on-CKD — the mechanism behind each modality's solute and fluid removal kinetics.

Disease context: AKI-on-CKD patients meeting an "AEIOU" indication for renal replacement therapy: Acidosis, Electrolytes (hyperkalemia), Intoxications, Overload, Uremia.

Central mechanism: All three modalities clear solute by diffusion across a semipermeable dialyzer membrane, but they differ in time on therapy, blood-flow rate, and dialysate flow — producing different solute-removal curves and different effects on hemodynamics.

Layout: Landscape 1536 × 1024, white background, review-article schematic. Left third = patient + circuit organ panel; center two-thirds = three side-by-side dashed insets of a dialyzer membrane showing the modality-specific solute gradient and a small kinetic curve under each; bottom = three-box summary flow keyed to hemodynamic stability.

Organ panel (left): a simplified seated CKD patient silhouette in light gray-blue #cdd9e5 with a tunneled internal-jugular dialysis catheter, connected by stylized arterial (brick red #b91c1c) and venous (soft blue #5a8fb0) lines to a generic dialyzer rectangle. The kidney behind the patient is shown small and dim with a soft-yellow injury overlay, labeled "AKI on CKD." A dashed connector from the dialyzer points right into the three magnified insets.

Magnified mechanism panels (three dashed boxes side by side):

LEFT inset — "CRRT (CVVHDF)" in Inter, teal #1a6b72. A dialyzer cross-section in light gray-blue with hollow fibers shown as parallel tubes. Blood (brick red) on one side, dialysate (soft blue) on the opposite side, slow countercurrent arrows. Small soft-yellow solute dots cross the membrane at a low, steady rate. Below the schematic, a tiny line graph showing blood-urea concentration falling slowly and smoothly over 24 hours. Callouts: "Q_blood ≈ 150–200 mL/min" · "Effluent ≈ 20–25 mL/kg/hr" · "Continuous · gentle · minimal BP swings."

CENTER inset — "IHD (Intermittent HD)" in Inter, teal. Same dialyzer schematic but with brick-red blood flow shown faster and a steep solute gradient — many soft-yellow solute dots crossing at once. Line graph shows a steep urea drop within 3–4 hours, then plateau. Callouts: "Q_blood ≈ 300–400 mL/min" · "Session 3–4 hr, 3×/week" · "Fastest K⁺ correction; can cause BP drops."

RIGHT inset — "SLED" in Inter, teal. Dialyzer schematic with moderate blood flow and a gentler solute gradient than IHD; intermediate density of solute dots. Line graph shows a smooth urea descent over 6–12 hours. Callouts: "Q_blood ≈ 200 mL/min" · "Hybrid 6–12 hr daily" · "For marginal stability."

Bottom three-box flow (full width):
- Left pink #fde8ec pathology box "Indication (AEIOU)": "Acidosis · Electrolytes (K⁺) · Intoxications · Overload · Uremia."
- Center white dashed box "Decision driver — hemodynamic stability": short flow line "Unstable / shock → CRRT" arrow "Stable + rapid clearance needed → IHD" arrow "Marginal stability → SLED" in Manrope navy.
- Right blue #e3eef5 benefit/outcome box "Goal": "Bridge to renal recovery — 30–40 % of AKI-on-CKD patients can be weaned off dialysis."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connectors. No brand or machine names. Generous whitespace.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 6 — `aki-ckd-recovery-outcomes-infographic.png`  ·  Three repair trajectories

```
Create a publication-grade biomedical mechanism schematic about:

Topic: Three possible cellular trajectories after AKI on a CKD background — full repair, maladaptive repair, or failed repair leading to ESKD.

Disease context: Post-AKI recovery in patients with pre-existing CKD; quantitative outcomes (~30 % full / ~40 % partial / ~30 % progression to ESKD).

Central mechanism: Surviving proximal tubular cells dedifferentiate, proliferate, and either redifferentiate (full repair) or arrest in a pro-fibrotic, senescent state that drives interstitial fibrosis and ongoing nephron loss (maladaptive repair), or fail entirely with nephron dropout (failed repair).

Layout: Square 1024 × 1024, white background, review-article schematic. A small organ panel anchors the top-left. Below it, three dashed magnified mechanism insets stacked vertically — each shows a proximal tubule and an outcome chip on the right. A horizontal proportion bar runs across the bottom encoding 30 / 40 / 30 % outcomes.

Organ panel (top-left, small): a kidney cross-section in light gray-blue #cdd9e5 post-AKI, with soft-yellow patches representing recovering tubules. A small inset of a proximal tubular cell beside it, labeled "Surviving PT cell" in IBM Plex Sans. A thin dashed connector points down into the three insets.

Magnified mechanism insets (three dashed boxes, stacked):

Inset A — "Full repair (~30 %)" header in Inter, soft blue #5a8fb0. A proximal tubule cross-section in light gray-blue with a healthy brush border restored; small arrows showing "Dedifferentiation → proliferation → redifferentiation." Callouts: "Brush-border restored" · "Mitochondrial recovery (↑ OXPHOS)" · "No interstitial fibrosis." Outcome chip on the right (pale blue #e3eef5): "Cr returns to pre-AKI baseline."

Inset B — "Maladaptive repair (~40 %)" header in Inter, amber-orange #b8860b. Same tubule but with patchy brush-border loss, a soft-yellow fibrotic interstitial collar around the tubule, scattered red dots labeled "↑ TGF-β · ↑ ROS · senescent cells." Callouts: "Incomplete redifferentiation" · "Pro-fibrotic signaling" · "Ongoing nephron loss." Outcome chip (pale pink #fde8ec): "Stable but at a lower new baseline."

Inset C — "Failed repair (~30 %)" header in Inter, deep crimson #8c1a1a. Tubule with collapsed lumen, no brush border, brick-red hatching, surrounded by dense soft-yellow fibrosis; an adjacent nephron icon faded to dashed outline labeled "Nephron dropout." Callouts: "Apoptosis · necrosis" · "Atubular glomeruli" · "Progression to ESKD." Outcome chip (deeper pink): "Permanent dialysis required."

Bottom horizontal proportion bar (full width, ~24 px tall, rounded ends): three contiguous segments — soft blue 30 % (Inset A color), amber 40 %, deep crimson 30 % — with the percentages labeled above each segment in Inter bold matching the segment color.

Below the bar, a thin teal note in Manrope navy: "Each AKI episode raises the probability of moving down this trajectory next time — prevention is the single most important post-discharge goal."

Bottom three-box flow (above the proportion bar):
- Left pink #fde8ec pathology box "Predictors of poor recovery": "eGFR < 30 pre-AKI · Age > 65 · Diabetes · Stage 3 AKI · Oliguria > 72 hr · Repeat AKI."
- Center white dashed box "Post-AKI window (first 3 months)": "Cr at 1 / 4 / 12 wk · UACR at 3 mo · Cautious ACE/ARB restart when stable."
- Right blue #e3eef5 benefit box "Modifiable levers": "Avoid recurrent insults · Sick-day rules · No NSAIDs · Pre-procedure hydration · Tight BP and glycemic control."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connectors. Generous whitespace. No photorealism, no dark backgrounds.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 7 — `ckd-sick-day-rules-filipino-patient.png`  ·  Sick-day rules as intervention

```
Create a publication-grade biomedical mechanism schematic about:

Topic: The sick-day rules as a mechanistic intervention that interrupts the triple-whammy cascade in CKD.

Disease context: A CKD patient developing an acute illness with vomiting, diarrhea, or fever — the trigger for the most preventable AKI-on-CKD admissions.

Central mechanism: Acute volume depletion superimposed on already-blocked GFR-defending pathways (ACE/ARB blocking efferent tone, diuretic blocking volume, NSAID blocking afferent vasodilation) collapses glomerular pressure. Temporarily withdrawing the three drug classes and replacing volume restores autoregulation before tubular injury occurs.

Layout: 5:4 landscape 1402 × 1122, white background, review-article schematic with a humane, calm tone. Left two-thirds = organ + glomerulus mechanism panel illustrating risk → intervention; right one-third = a clean numbered action card.

Organ panel (left): a simplified Filipino patient silhouette in soft blue #5a8fb0 (head and shoulders, neutral; no facial features so the image stays mechanism-focused) holding a glass of clear oral rehydration solution. Behind the patient, a kidney cross-section in light gray-blue #cdd9e5 with a thin dashed line magnifying outward to a glomerular inset.

Magnified mechanism inset (center, dashed border, large): a split glomerulus diagram — left half "WITHOUT sick-day rules" and right half "WITH sick-day rules."

- LEFT half: afferent arteriole constricted (red), efferent dilated (light blue), glomerular tuft pale yellow with a small soft-red "↓ GFR" gauge underneath. Three small drug-class chips at the perimeter — NSAID (pale pink), Diuretic (pale amber), ACE/ARB (pale blue) — each with a red "×" denoting the blocked compensatory pathway. Label "Triple whammy + dehydration."

- RIGHT half: afferent vessel widened back to normal, efferent partially restored, tuft restored to soft yellow, gauge restored to "GFR ↗." The same three drug chips appear with a clear "hold" cross-hatch and a small water-droplet icon labeled "ORS." Label "Sick-day rules applied."

A short curved arrow between the two halves labels the transition: "Withdraw drugs + restore volume → restore autoregulation."

Right action card (one-third of canvas, rounded pale blue #e3eef5 panel with thin teal #1a6b72 border): header in Inter, teal "Sick-day rules — what to do today." Then a numbered list in Manrope navy, ample spacing, each step preceded by a small teal dot:

1. STOP your ACE inhibitor or ARB.
2. STOP your diuretic (furosemide / HCTZ).
3. NEVER take NSAIDs (mefenamic acid · ibuprofen · naproxen).
4. Drink water or oral rehydration salts.
5. Call your nephrologist within 24 hours.

A small teal sub-note at the bottom of the card: "Restart only when feeling better and eating normally — confirm with your nephrologist."

Bottom three-box flow (across the full width, below the main panel):
- Left pink #fde8ec pathology box "Trigger": "Vomiting · diarrhea · fever · poor oral intake."
- Center white dashed box "Mechanism interrupted": "Hold the three classes · replace volume · restore prostaglandin-mediated afferent dilation and Ang-II-mediated efferent tone."
- Right blue #e3eef5 benefit box "Benefit": "Prevents pre-renal AKI · avoids hospitalization · preserves nephron mass."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. The patient silhouette must remain symbolic and faceless to keep the figure mechanism-focused (no photorealism). Thin dashed connectors. Generous whitespace.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-right corner in navy, ~10–11px.
```

---

## FIGURE 8 — `aki-medication-safety-hold-adjust.png`  ·  Two pharmacologic injury modes

```
Create a publication-grade biomedical mechanism schematic about:

Topic: Two mechanisms by which medications harm the kidney in AKI-on-CKD — direct nephrotoxicity (drugs to STOP) versus reduced renal clearance with accumulation (drugs to DOSE-ADJUST).

Disease context: AKI superimposed on CKD, during which both glomerular filtration and tubular handling are compromised.

Central mechanism: STOP-list drugs damage the kidney by direct tubular toxicity, hemodynamic blockade, or osmotic/oxidative injury and must be withdrawn entirely. ADJUST-list drugs are renally cleared and accumulate to toxic levels when GFR falls — they remain useful, but only at GFR-indexed doses.

Layout: Portrait 1024 × 1536, white background, review-article schematic. Top half = organ-level panel + magnified tubular cell inset (single dashed box) illustrating the two injury modes; bottom half = two columns of drug entries — STOP on the left, ADJUST on the right — each entry tagged with the matching mechanism.

Organ panel (top, narrow strip): kidney cross-section in light gray-blue #cdd9e5 with renal artery (brick red #b91c1c) and renal vein (soft blue #5a8fb0). Two thin dashed connectors emerge: one from the cortex labeled "Direct nephrotoxin entry," one from the efferent / outflow side labeled "Reduced clearance — drug accumulation." Both connectors converge on a central magnified inset below.

Magnified mechanism inset (dashed border, full-width below the organ): a single proximal tubular cell rendered as a simple block — apical brush border (soft yellow #f5e6a3 ridge), nucleus, basolateral membrane. Two color-coded arrows enter the cell:

- LEFT arrow in brick red #b91c1c labeled "Direct injury" — points to the apical brush border. Small callouts: "Tubular toxicity · brush-border loss · oxidative stress · ↑ ROS · apoptosis."
- RIGHT arrow in amber #b8860b labeled "Accumulation" — points to a small storage motif inside the cytoplasm. Callouts: "Renal clearance ↓ → drug levels ↑ → systemic toxicity (e.g. lactic acidosis, ototoxicity, bleeding)."

Below the inset, a horizontal teal divider with the label "Two questions for every drug: Does it directly injure the kidney? Is it renally cleared?"

Two-column drug list (bottom half):

LEFT column header in clinical red #b91c1c, white background, Inter: "STOP IMMEDIATELY (direct injury / hemodynamic block)." Vertical list of rounded white pill cards on a very pale gray #f3f4f6 panel; each card has a small red dot and a short Manrope navy label + a one-line mechanism tag in lighter gray:

- NSAIDs (mefenamic acid · ibuprofen · naproxen) — afferent vasoconstriction.
- Metformin — lactic acidosis risk in AKI.
- ACE inhibitors / ARBs — efferent vasodilation, ↓ glomerular pressure.
- SGLT2 inhibitors — euvolemic hypovolemia in acute illness.
- LMWH at therapeutic dose — bleeding from accumulation.
- Aminoglycosides without monitoring — direct tubular toxicity.
- IV contrast without hydration — osmotic + oxidative tubular injury.
- Aristolochic-acid herbals — irreversible tubulointerstitial injury.

RIGHT column header in amber #b8860b, white background, Inter: "DOSE-ADJUST (renally cleared)." Same card style with a small amber dot:

- Furosemide — titrate to urine output.
- Gentamicin / amikacin — extended interval, trough-guided.
- Digoxin — lower dose; check level.
- Insulin — reduce dose (clearance ↓).
- DOACs (apixaban · rivaroxaban) — CrCl-based dosing.
- Cefepime · vancomycin · piperacillin-tazobactam — eGFR-adjusted.
- Opioids — avoid morphine / codeine; prefer fentanyl or hydromorphone.
- Allopurinol — reduce dose; monitor hypersensitivity.

Bottom three-box flow (across the full width):
- Left pink #fde8ec pathology box "Injury drivers": "Direct tubular toxicity · hemodynamic block · drug accumulation."
- Center white dashed box "Intervention rule": "STOP the directly injurious; DOSE-ADJUST the renally cleared; use paracetamol 500–1000 mg up to 4×/day for pain."
- Right blue #e3eef5 benefit box "Benefit": "Avoids second AKI hit · preserves residual nephrons · all changes guided by nephrology."

Use white background, muted clinical colors, clean sans-serif labels set in Inter (titles), IBM Plex Sans (anatomy labels), and Manrope (body) — never a serif font. Thin dashed connectors. Strict column alignment. Generous whitespace. No photorealism, no dark backgrounds.

Add a small, semi-transparent © williamriveromd.com attribution in the bottom-center in navy, ~10–11px.
```

---

## Stage 2 — wiring notes

After generation in the ChatGPT Image Generator GPT, save each output to the
project's `images/` folder as both `.png` and `.webp` using the file names above.
All eight `<img>` references in `guides/acute-kidney-injury-on-ckd.html` already
point to these file names — **no HTML edits are required**. The og:image
(`aki-staging-kdigo-ckd-criteria.png`) refreshes automatically.

The vignette-hero (`acute-kidney-injury-on-ckd-vignette-hero.webp`) stays
untouched per the request.
