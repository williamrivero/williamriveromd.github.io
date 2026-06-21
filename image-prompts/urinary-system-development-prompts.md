# Development of the Urinary System — Image Prompt Pack

**Guide:** `guides/kidney-physiology.html` (Origins scrollytelling)
**Purpose:** Regenerate the 11 `kp-dev-*` developmental-stage figures.
**Tool:** ChatGPT Image Generator (GPT‑image / GPT‑4o native image generation).
**Pipeline:** Stage 1 (prompt authoring) → generate → drop PNGs into `images/` with the exact filenames → rebuild WebP companions.

---

## ⚠️ Read first — the fixes that matter

These regenerations exist to correct two problems with the previous set:

1. **Transparent background.** Every figure must be a true **alpha PNG with a fully transparent background** — no white/peach plate, no panel, no ground shadow. The guide places these on a dark amber scene, so any baked background ruins the effect.
2. **No glow behind the label text.** The previous labels had a **white glow/halo** around the type that made them hard to read. **Forbid** any glow, halo, outline, stroke, drop‑shadow, or background plate behind or around label text. The type must sit **directly on transparency**, crisp and clean.

Because the background is transparent and the guide is dark, **label text must be a light warm off‑white** (≈ `#efe6d6`) so it reads on the dark scene — *not* dark text.

---

## GLOBAL STYLE — applies to (and is repeated inside) every prompt

> Realistic, semi‑3D medical illustration with soft, even studio lighting and gentle sub‑surface shading; clinically accurate; single subject centered; **fully transparent background (alpha PNG — no backdrop, no plate, no ground shadow)**; muted‑realistic tissue colors consistent across the whole series (same scale, same light direction).
> **Labels:** thin 1px straight leader lines in pale warm gray (`#cbb890`) each ending in a small dot exactly on the named structure; label text in **clean thin sans‑serif, warm off‑white `#efe6d6`, ~22px, perfectly legible**, arranged down the **left margin** with even spacing.
> **CRITICAL — no glow:** absolutely **no** white glow, halo, outline, stroke, drop‑shadow, blur, or background box behind/around any label text; type sits directly on transparency. Spell every label exactly as written; no gibberish or extra text.
> **Credit:** small semi‑transparent navy text `© williamriveromd.com` in the bottom‑right corner only.
> **Avoid:** white/colored background, panels behind labels, dark theme fills, heavy cartoon outlines, photoreal skin texture noise, clutter.
> **Framing:** 1536 × 1024 landscape (mature kidney 1024 × 1024), structure centered with room on the left for the labels.

---

## 1 · Embryo — Carnegie stage 10–12  →  `kp-dev--0-embryo-lateral-carnegie-10-12.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no ground shadow). Lateral view of a ~4-week human embryo (Carnegie stage 10–12), C-shaped and curled, showing the dorsal somite column, the closing neural tube, the heart bulge, pharyngeal arches, and the connecting stalk. Muted realistic tissue colors, soft even studio lighting.
Anatomical labels down the LEFT margin, each a thin 1px pale-warm-gray (#cbb890) leader line ending in a small dot on the structure, text in clean thin sans-serif warm off-white (#efe6d6) ~22px, crisp and legible: "Neural tube", "Somites", "Pharyngeal arches", "Heart bulge", "Connecting stalk".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or background box behind or around any label text — type sits directly on transparency. No background of any kind. Spell labels exactly; no other text. Small semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 2 · Trilaminar germ layers / mesoderm  →  `kp-dev--1-mesoderm.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). Transverse cross-section of the trilaminar embryo at the level of the closing neural tube. Clearly show three concentric germ layers — outer surface ectoderm, middle mesoderm (subdivided into paraxial, intermediate, and lateral plate), and inner endoderm (gut tube) — plus the neural tube, the neural crest, and the notochord. Emphasize the MIDDLE mesoderm layer (warm tone) so it reads as "the middle one". Muted realistic colors, soft lighting.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines with end dots on each structure, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Surface ectoderm", "Neural tube", "Neural crest", "Notochord", "Paraxial mesoderm", "Intermediate mesoderm", "Lateral plate mesoderm", "Endoderm (gut)".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around any label — text directly on transparency. No background. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 3 · Intermediate mesoderm / nephrogenic cord  →  `kp-dev-0-intermediate-mesoderm.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). Transverse cross-section highlighting the INTERMEDIATE MESODERM (the nephrogenic cord) as a paired longitudinal strip flanking the dorsal aorta, sitting between the paraxial somite and the lateral plate mesoderm; neural tube and notochord dorsally. Subtly highlight the intermediate mesoderm strip in warm tone. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines ending in dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Intermediate mesoderm (nephrogenic cord)", "Somite (paraxial mesoderm)", "Lateral plate mesoderm", "Dorsal aorta", "Neural tube", "Notochord".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, or box behind/around any label — text directly on transparency. No background. Exact spelling only. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 4 · Pronephros  →  `kp-dev-01-pronephros.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). The PRONEPHROS: a cranial cluster of segmented pronephric tubules on the left draining into a single curved pronephric (Wolffian) duct that runs caudally on the right toward the cloaca. Muted realistic tissue colors, soft even studio lighting, consistent scale with the series.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines with end dots on each structure, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Pronephric tubules", "Pronephric (Wolffian) duct", "Cloaca".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around label text — type directly on transparency. No background of any kind. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 5 · Mesonephros  →  `kp-dev-02-mesonephros.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). The MESONEPHROS: an elongated paired ridge of mesonephric tubules, several bearing small glomeruli, draining medially into the mesonephric (Wolffian) duct; a gonadal ridge runs alongside. Muted realistic colors, soft lighting, matching the series scale.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines ending in dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Mesonephric tubules", "Glomerulus", "Mesonephric (Wolffian) duct", "Gonadal ridge".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, or box behind/around any label — text directly on transparency. No background. Exact spelling only. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 6 · Ureteric bud induction  →  `kp-dev-03-ureteric-bud.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). URETERIC BUD INDUCTION: a single ureteric bud sprouting from the caudal mesonephric (Wolffian) duct and growing into a rounded cap of metanephric (cap) mesenchyme. Show the reciprocal induction at the bud tip. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines with end dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Ureteric bud", "Metanephric mesenchyme", "Mesonephric (Wolffian) duct".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around label text — type directly on transparency. No background. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 7 · Branching morphogenesis  →  `kp-dev-04-branching.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). BRANCHING MORPHOGENESIS: the ureteric bud repeatedly dividing into a dichotomous tree of collecting ducts, each ampullary tip capped by condensed cap mesenchyme. Muted realistic colors, soft even lighting, series-consistent scale.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines ending in dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Ureteric bud (branching)", "Collecting ducts", "Ampullary tip", "Cap mesenchyme".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, or box behind/around any label — text directly on transparency. No background. Exact spelling only. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 8 · Nephrogenesis (MET)  →  `kp-dev-05-nephrogenesis.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). NEPHROGENESIS / mesenchymal-to-epithelial transition: a sequence showing cap mesenchyme condensing into a renal vesicle, then a comma-shaped body, then an S-shaped body, maturing into a glomerulus with a capillary tuft and podocytes, connected to a collecting duct. Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines with end dots on each stage, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Renal vesicle", "Comma-shaped body", "S-shaped body", "Glomerulus", "Podocytes", "Collecting duct".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around label text — type directly on transparency. No background. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 9 · Ascent & rotation  →  `kp-dev-06-ascent-rotation.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). ASCENT & ROTATION of the metanephric kidneys: the kidneys shown climbing from the pelvis to the lumbar region while rotating ~90° so the hilum faces medially; their definitive renal arteries arising from the abdominal aorta, ureters descending to the bladder, adrenal (suprarenal) glands capping the upper poles. Subtle thin curved motion arrows for ascent and rotation (pale, unobtrusive). Muted realistic colors, soft even lighting.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines ending in dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Kidney (ascending)", "90° medial rotation", "Renal artery (definitive)", "Suprarenal (adrenal) gland", "Ureter", "Bladder".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, or box behind/around any label — text directly on transparency. No background. Exact spelling only. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 10 · Mature fetal kidney  →  `kp-dev-07-fetal-kidney.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). MATURE FETAL KIDNEY: a single kidney with the characteristic fetal surface lobulation, cut to reveal cortex, medullary pyramids, the renal pelvis, and the ureter. Muted realistic colors, soft even studio lighting, series-consistent scale.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines with end dots, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Fetal lobulation", "Cortex", "Medulla (pyramid)", "Renal pelvis", "Ureter".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around label text — type directly on transparency. No background. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1536×1024 landscape.
```

## 11 · Mature kidney  →  `kp-dev-8-mature-kidney.png`

```
Realistic semi-3D medical illustration on a FULLY TRANSPARENT background (alpha PNG, no backdrop, no plate, no shadow). MATURE (adult) KIDNEY, coronal section: outer cortex, medullary renal pyramids, renal columns, minor and major calyces, renal pelvis, the renal artery (red) and renal vein (blue) at the hilum, and the ureter. Muted realistic colors, soft even studio lighting, series-consistent scale.
Labels down the LEFT margin, thin 1px pale-warm-gray (#cbb890) leader lines ending in dots on each structure, clean thin sans-serif warm off-white (#efe6d6) ~22px: "Cortex", "Renal pyramid (medulla)", "Renal column", "Minor calyx", "Major calyx", "Renal pelvis", "Renal artery", "Renal vein", "Ureter".
CRITICAL: NO white glow, halo, outline, stroke, drop-shadow, blur, or box behind/around any label — text directly on transparency. No background of any kind. Exact spelling, no extra text. Semi-transparent navy "© williamriveromd.com" bottom-right. 1024×1024 square.
```

---

## After you generate

1. Save each PNG into `images/` using the **exact filename** in its heading (same names as the current set — the guide already points at them; no HTML changes needed).
2. Regenerate the WebP companions (the guide serves WebP via `<picture>`):
   ```bash
   python3 - <<'PY'
   from PIL import Image
   names=["kp-dev--0-embryo-lateral-carnegie-10-12","kp-dev--1-mesoderm","kp-dev-0-intermediate-mesoderm",
   "kp-dev-01-pronephros","kp-dev-02-mesonephros","kp-dev-03-ureteric-bud","kp-dev-04-branching",
   "kp-dev-05-nephrogenesis","kp-dev-06-ascent-rotation","kp-dev-07-fetal-kidney","kp-dev-8-mature-kidney"]
   for n in names:
       Image.open(f"images/{n}.png").convert("RGBA").save(f"images/{n}.webp","WEBP",quality=82,method=6)
   PY
   ```
   (or just tell me “process the replacements” and I’ll merge, regenerate WebP, and re-center each frame on its structure.)
3. Because the structures sit centered (labels flowing left), I’ll re-run the per-frame **structure-centering** offsets after the new images land.

## Notes
- This pack intentionally **overrides the skill’s default white background** → transparent, per the dark immersive guide.
- Label color is **light** (`#efe6d6`) because the figures sit on a dark scene; dark label text would be invisible.
- Keep lighting direction and subject scale uniform across all 11 so the scroll cross-fade reads as one continuous development.
