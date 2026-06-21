# Development of the Urinary System — Image Prompt Pack (15 stages)

**Guide:** `guides/kidney-physiology.html` (Origins scrollytelling)
**Tool:** ChatGPT Image Generator (GPT‑image / GPT‑4o native image generation).
**Pipeline:** Stage 1 (prompt authoring) → generate → drop PNGs into `images/` → rebuild WebP companions → wire into the guide.

---

## ⚠️ Read first — non‑negotiable styling (the generator kept ignoring these)

1. **Transparent background** — true alpha PNG. **No** white/colored backdrop, **no** plate, **no** panel, **no** box, **no** ground shadow. The guide sits on a dark amber scene.
2. **Label text = PURE WHITE, UPRIGHT SANS‑SERIF.** Clean modern sans‑serif (Helvetica / Arial / DM‑Sans style), color **`#ffffff`**.
   - **Do NOT** use serif, **do NOT** use italic, **do NOT** use yellow/gold/red/black — **white only**.
3. **Leader/connector lines = white**, thin (1px), each ending in a small **white** dot on the structure.
4. **No glow.** Absolutely no glow, halo, outline, stroke, drop‑shadow, blur, or background plate behind/around any text. Type sits directly on transparency.
5. **Spelling.** Render every label **exactly** as written. (The last batch produced "Sornites" — it is **"Somites"**.) No extra or invented text.
6. **Consistency.** Same realistic semi‑3D style, scale, and light direction across all 15 so the scroll cross‑fade reads as one continuous development.
7. **Credit.** Small semi‑transparent navy `© williamriveromd.com` in the bottom‑right corner only.
8. **Framing.** 1536 × 1024 landscape unless noted. Center the structure; keep the **left margin clear** for the label column.

---

## GLOBAL STYLE — copy this into the top of every prompt (also embedded below)

> Realistic, semi‑3D medical illustration; soft even studio lighting; gentle sub‑surface shading; clinically accurate; **fully transparent background (alpha PNG — no backdrop/plate/box/shadow)**; muted‑realistic tissue colors, consistent scale and light direction across the series. **Labels down the LEFT margin: thin 1px WHITE leader lines, each ending in a small WHITE dot on the structure; label text in clean UPRIGHT SANS‑SERIF (Helvetica/Arial/DM‑Sans style), PURE WHITE `#ffffff`, ~24px, perfectly legible.** NO glow/halo/outline/stroke/drop‑shadow/blur/box behind or around text — directly on transparency. NEVER serif, italic, yellow, gold, red, or black text/lines — white only. Spell every label exactly; no other text. Small semi‑transparent navy `© williamriveromd.com` bottom‑right.

---

# SECTION A — Embryonic Foundations

## 1 · Early Embryo (Week 3–4)  →  `urinary-dev-01-embryo-overview.png`
**Shows:** trilaminar embryo · intermediate mesoderm highlighted · future nephrogenic cord location
**Teaching point:** *The urinary system begins from intermediate mesoderm.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop, plate, box, or shadow). Simplified dorsal/oblique view of an early trilaminar human embryo (week 3–4) with a small wedge cutaway revealing the three germ layers (ectoderm, mesoderm, endoderm); the paired INTERMEDIATE MESODERM strips highlighted in a warm tone running along the back as the future nephrogenic cord. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines each ending in a small WHITE dot on the structure; text in clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Ectoderm", "Mesoderm", "Endoderm", "Intermediate mesoderm", "Nephrogenic cord (future)".
NO glow/halo/outline/stroke/shadow/box behind or around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 2 · Intermediate Mesoderm Formation  →  `urinary-dev-02-intermediate-mesoderm.png`
**Shows:** neural tube · somites · intermediate mesoderm · lateral plate mesoderm
**Teaching point:** *Intermediate mesoderm gives rise to the kidneys and ureters.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). CIRCULAR, round transverse cut-section of the embryo drawn as a clean round disc of concentric tissue, showing: the dorsal neural tube and notochord; paired somites (paraxial mesoderm); the small paired INTERMEDIATE MESODERM strips (highlighted warm tone) flanking the dorsal aorta; the lateral plate mesoderm; and the ventral endoderm (gut). Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Neural tube", "Notochord", "Somite (paraxial mesoderm)", "Intermediate mesoderm", "Lateral plate mesoderm", "Dorsal aorta", "Endoderm (gut)".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling (it is "Somites", not "Sornites"); no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

---

# SECTION B — Three Successive Kidney Systems

## 3 · Pronephros  →  `urinary-dev-03-pronephros.png`
**Shows:** cervical pronephric tubules · pronephric duct
**Teaching point:** *First kidney system; nonfunctional and regresses.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). The PRONEPHROS: a cranial (cervical) cluster of segmented pronephric tubules draining into a single curved pronephric duct running caudally toward the cloaca; show the pronephros faded/regressing. Muted realistic colors, soft even lighting, series-consistent scale.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Pronephric tubules (cervical)", "Pronephric duct", "Cloaca".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 4 · Mesonephros  →  `urinary-dev-04-mesonephros.png`
**Shows:** mesonephric tubules · mesonephric (Wolffian) duct · primitive glomeruli
**Teaching point:** *Temporary functioning embryonic kidney.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). The MESONEPHROS: an elongated paired ridge of S-shaped mesonephric tubules, several bearing primitive glomeruli, draining medially into the mesonephric (Wolffian) duct. Muted realistic colors, soft even lighting, series-consistent scale.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Mesonephric tubules", "Primitive glomerulus", "Mesonephric (Wolffian) duct".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 5 · Mesonephric Duct Derivatives  →  `urinary-dev-05-mesonephric-duct-fate.png`
**Shows:** male pathway (epididymis, vas deferens, seminal vesicle) · female pathway (regression)
**Teaching point:** *The Wolffian duct becomes major male reproductive structures.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). Two side-by-side schematics of the fate of the mesonephric (Wolffian) duct: LEFT = MALE pathway, the duct persisting and forming the epididymis, vas deferens, and seminal vesicle; RIGHT = FEMALE pathway, the duct largely regressing (faded, small Gartner duct remnant). A small "Male" / "Female" caption over each in the same white sans-serif. Muted realistic colors, soft even lighting.
Labels with thin 1px WHITE leader lines and small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Mesonephric (Wolffian) duct", "Epididymis", "Vas deferens", "Seminal vesicle", "Regression (female)", "Gartner duct remnant".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

---

# SECTION C — Definitive Kidney (Metanephros)

## 6 · Ureteric Bud Emergence  →  `urinary-dev-06-ureteric-bud.png`
**Shows:** mesonephric duct · ureteric bud · metanephric mesenchyme
**Teaching point:** *The permanent kidney begins here.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). URETERIC BUD EMERGENCE: a single ureteric bud sprouting from the caudal mesonephric (Wolffian) duct and growing into a rounded cap of metanephric mesenchyme. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Mesonephric (Wolffian) duct", "Ureteric bud", "Metanephric mesenchyme".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 7 · Reciprocal Induction (signaling)  →  `urinary-dev-07-induction-signaling.png`
**Shows:** GDNF · RET · ureteric bud · metanephric mesenchyme
**Teaching point:** *Kidney development depends on molecular signaling.* (clinician-oriented)

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). RECIPROCAL INDUCTION close-up: the ureteric bud tip facing the metanephric mesenchyme; the mesenchyme secreting GDNF (small molecule icons) toward RET receptors on the bud tip; a faint reciprocal WNT signal back to the mesenchyme. Thin white arrows for signal direction. Muted realistic colors, soft even lighting.
Labels with thin 1px WHITE leader lines and small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Metanephric mesenchyme", "GDNF", "RET receptor", "Ureteric bud tip", "WNT (reciprocal)".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 8 · Branching Morphogenesis  →  `urinary-dev-08-branching-morphogenesis.png`
**Shows:** repeated ureteric bud branching · collecting system formation
**Teaching point:** *Produces the collecting ducts and calyces.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). BRANCHING MORPHOGENESIS: the ureteric bud repeatedly dividing into a dichotomous tree of collecting ducts, each ampullary tip capped by condensed cap mesenchyme; the earliest branches widening into the future renal pelvis and calyces. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Ureteric bud (branching)", "Ampullary tip", "Cap mesenchyme", "Collecting ducts", "Future renal pelvis / calyces".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 9 · Nephrogenesis  →  `urinary-dev-09-nephrogenesis.png`
**Shows:** cap mesenchyme → renal vesicle → comma body → S‑shaped body
**Teaching point:** *Nephrons arise from metanephric mesenchyme.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). NEPHROGENESIS sequence (left → right): cap mesenchyme condensing into a renal vesicle, then a comma-shaped body, then an S-shaped body, adjacent to a collecting-duct tip. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots on each stage; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Cap mesenchyme", "Renal vesicle", "Comma-shaped body", "S-shaped body".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 10 · Formation of the Mature Nephron  →  `urinary-dev-10-nephron-maturation.png`
**Shows:** glomerulus · proximal tubule · loop of Henle · distal tubule · collecting duct connection
**Teaching point:** *The functional nephron is assembled.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). A single MATURE NEPHRON: glomerulus in Bowman's capsule, proximal convoluted tubule, descending/ascending loop of Henle, distal convoluted tubule, joining a collecting duct. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Glomerulus", "Proximal convoluted tubule", "Loop of Henle", "Distal convoluted tubule", "Collecting duct".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

---

# SECTION D — Ascent and Vascularization

## 11 · Kidney Ascent  →  `urinary-dev-11-kidney-ascent.png`
**Shows:** sequential positions — pelvic · iliac · lumbar (with arrows)
**Teaching point:** *Kidneys ascend from the pelvis.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). KIDNEY ASCENT: posterior abdominal/pelvic view showing one kidney in three successive positions — pelvic (lowest, faded), iliac (mid, semi-faded), and lumbar (final, solid) — with thin WHITE upward arrows between them; ureter trailing down to the bladder. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Pelvic position", "Iliac position", "Lumbar (final) position", "Ureter", "Bladder".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 12 · Rotation & Arterial Changes  →  `urinary-dev-12-rotation-and-blood-supply.png`
**Shows:** 90° medial rotation · successive transient arteries · definitive renal artery
**Teaching point:** *Explains accessory renal arteries.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). KIDNEY ROTATION & BLOOD SUPPLY: a kidney rotating ~90° so the hilum turns medially (thin white curved rotation arrow); the abdominal aorta giving successive transient lower arteries (faded/degenerating) and the single definitive renal artery (solid). Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "90° medial rotation", "Hilum", "Abdominal aorta", "Transient arteries (degenerating)", "Definitive renal artery".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

---

# SECTION E — Bladder and Lower Tract

## 13 · Cloaca Partitioning  →  `urinary-dev-13-cloaca-partition.png`
**Shows:** cloaca · urorectal septum · rectum · primitive bladder
**Teaching point:** *The urinary and gastrointestinal tracts separate.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). CLOACA PARTITIONING: midline sagittal schematic of the cloaca being divided by the descending urorectal septum into a ventral urogenital sinus (primitive bladder) and a dorsal rectum; the allantois extending from the bladder apex. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Cloaca", "Urorectal septum", "Urogenital sinus (primitive bladder)", "Rectum", "Allantois".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 14 · Bladder & Urethra Development  →  `urinary-dev-14-bladder-urethra-development.png`
**Shows:** urogenital sinus · bladder · urethra · allantois → urachus
**Teaching point:** *Forms the lower urinary tract.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). BLADDER & URETHRA DEVELOPMENT: the urogenital sinus forming the bladder and urethra; the ureters opening into the bladder base (trigone); the allantois regressing into the fibrous urachus running to the umbilicus. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Urogenital sinus", "Bladder", "Trigone", "Ureter", "Urethra", "Allantois → Urachus".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 15 · Mature Urinary System  →  `urinary-dev-15-mature-urinary-system.png`
**Shows:** kidneys · ureters · bladder · urethra (adult)
**Teaching point:** *The completed urinary tract.*

```
Realistic semi-3D medical illustration, FULLY TRANSPARENT background (alpha PNG — no backdrop/plate/box/shadow). The COMPLETE ADULT URINARY SYSTEM, anterior view: paired kidneys with renal pelves, the ureters descending to the urinary bladder, the trigone at the bladder base, and the urethra exiting below; renal arteries (red) and veins (blue) at the hila. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px WHITE leader lines with small WHITE end dots; clean UPRIGHT SANS-SERIF, PURE WHITE #ffffff, ~24px: "Kidney", "Renal pelvis", "Ureter", "Bladder", "Trigone", "Urethra".
NO glow/halo/outline/stroke/shadow/box behind/around text — directly on transparency. NEVER serif/italic/yellow/gold/red/black — white only. Exact spelling, no other text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape (portrait 1024×1536 also fine for the full vertical tract).
```

---

## After you generate

1. Save each PNG into `images/` with the **exact filename** in its heading.
2. Say **"process the replacements"** and I will: regenerate WebP companions, **rewire the Origins section from 11 → 15 stages** (frames + timeline entries using these teaching points), and re‑center each frame on its structure.
3. This is a **new 15‑stage set** (`urinary-dev-*`, not the old `kp-dev-*`). The current `kp-dev-*` images stay live in the guide until the new set lands and I wire it in.

## Generation tips (the type kept coming out wrong)
- GPT image models often default to **serif/italic, colored** labels and add a **glow** — if a result is not‑white, serif, glowing, or misspelled, **regenerate** that one (the prompt forbids all of it) or paste the labels in your editor afterward.
- Generate **one stage at a time** for best text fidelity; reference a previously‑good image to keep subject scale and lighting consistent.
