# Understanding CKD — Mechanism Figure Prompt Pack

Generated with the **`williamriveromd-biomedical-mechanism-figure`** skill.

Replaces two retired images on `guides/understanding-ckd.html`:

| Retired image | New mechanism figure | Suggested filename |
|---|---|---|
| `ckd-understanding-overview.webp` | Figure 1 — CKD pathophysiology overview | `ckd-overview-mechanism.png` |
| `ckd-stages-egfr.webp` | Figure 2 — CKD stages by eGFR | `ckd-stages-mechanism.png` |

**Shared style (applies to every prompt below).** Flat vector illustration with
soft semi-3D shading, white background, generous whitespace, clean sans-serif
labels set in **Inter**, thin dashed connector lines separating magnified
panels. Muted clinical palette — light gray-blue anatomy, soft yellow for
highlighted nephron/tubular segments, red for arteries/injury/ROS, blue for
veins/protective/therapeutic effects, pale pink pathology summary box, pale
blue benefit summary box. No photorealism, no shadows, no dark background, no
cartoonish styling, no excessive icons, no gibberish text. Labels readable at
slide-viewing size. **Every figure carries a small semi-transparent navy
attribution `© williamriveromd.com` in the bottom-right corner**, not
obscuring any figure element (house convention, baked into each prompt below).

**Workflow.** Paste each block into the ChatGPT Image Generator (GPT-image /
GPT-4o). Save outputs as the suggested filenames into `images/`, then run the
companion-WebP step and update `understanding-ckd.html` to point at the new
files.

---

## 1. CKD pathophysiology overview
**Guide:** `guides/understanding-ckd.html` · **Suggested file:** `ckd-overview-mechanism.png`
**Replaces:** `ckd-understanding-overview.webp`
**Placement:** the lead hero illustration just after the hero block (first body figure).

```
Create a publication-grade biomedical mechanism schematic in a scientific
review-article style. Flat vector illustration, soft semi-3D shading, white
background, clean sans-serif labels in Inter, thin dashed connector lines,
generous whitespace. Muted clinical palette: light gray-blue anatomy, soft
yellow for highlighted tubular/affected segments, red for injury / arterial /
ROS cues, blue for therapeutic/protective effects, pale pink pathology box,
pale blue benefit box. No photorealism, no dark background, no shadows, no
clutter. Square 1:1 aspect (1024 × 1024). Bottom-right corner: small
semi-transparent navy text "© williamriveromd.com", ~11px, not obscuring the
figure.

TOPIC: How chronic kidney disease (CKD) develops — from systemic drivers to
nephron loss — and how modern therapy slows the trajectory.

DISEASE CONTEXT: Chronic kidney disease (CKD), patient education / clinician
overview.

CENTRAL MECHANISM: Chronic injury (hypertension, diabetes, NSAIDs, obesity,
smoking) → glomerular hyperfiltration and intraglomerular hypertension →
podocyte injury, glomerulosclerosis, tubulointerstitial fibrosis, peritubular
capillary rarefaction → progressive nephron dropout → falling eGFR. Modern
therapy (BP control, RAAS blockade, SGLT2 inhibitor, weight/diet, NSAID
avoidance) relieves intraglomerular pressure and slows decline.

ORGAN-LEVEL PANEL (top-left):
Two simplified kidney cross-sections side by side in light gray-blue, with
adrenal caps and major vessels — renal artery (red) and renal vein (blue).
- Left kidney labelled "HEALTHY": smooth cortex, intact medullary pyramids,
  full nephron mass.
- Right kidney labelled "CKD": shrunken, granular cortical surface, dilated
  renal pelvis from nephron dropout, attenuated cortex.
Small dashed connector arrow points from the CKD kidney to the magnified
nephron panel.

MAGNIFIED MECHANISM PANEL (right, dashed border):
A single nephron drawn at high magnification with anatomically correct
segments: glomerulus with afferent (red) and efferent (also red) arterioles,
proximal tubule, descending and ascending loop of Henle, distal tubule, and
collecting duct, all on a pale yellow background. Three concise callouts
labelled in Inter:
- "Glomerular hyperfiltration ↑" → glomerulus with bulging capillary tuft,
  thickened GBM, mesangial expansion, podocyte foot-process effacement
- "Tubulointerstitial fibrosis ↑" → interstitial collagen (faint hatched
  pattern) wrapping the tubules
- "Peritubular capillary rarefaction ↓" → thinned, dropped-out capillary
  network around the tubules
A small dashed callout near the glomerulus lists the canonical drivers in
short labels: "↑BP", "Diabetes (hyperglycemia)", "NSAIDs (PGE2 block)",
"Obesity", "Smoking (ROS)".

BOTTOM SUMMARY FLOW (full-width band, three boxes, left → right arrows):
- Left pathology box (pale pink): "INJURY DRIVERS — Hypertension · Diabetes ·
  Obesity · NSAIDs · Smoking · Chronic glomerular hypertension · Inflammation
  · Fibrosis"
- Center intervention box (white with navy border): "INTERVENTION — BP
  control · RAAS blockade (ACEi / ARB) · SGLT2 inhibitor · Weight & diet ·
  Avoid NSAIDs · Glycemic control"
- Right benefit box (pale blue): "BENEFIT — Slowed eGFR decline · Delayed
  kidney failure · Reduced albuminuria · Cardiovascular protection"
Use clear arrow flow from injury → intervention → benefit, with the
intervention box pointing to a small icon of a downward-trending eGFR curve
turning flatter under therapy.

Medical accuracy: keep segment labels anatomically plausible, do not invent
pathways, RAAS blockade and SGLT2i are standard of care (no "experimental"
flagging needed).
```

---

## 2. CKD stages by eGFR
**Guide:** `guides/understanding-ckd.html` · **Suggested file:** `ckd-stages-mechanism.png`
**Replaces:** `ckd-stages-egfr.webp`
**Placement:** in the "CKD stages" section directly below the overview figure.

```
Create a publication-grade biomedical mechanism schematic in a scientific
review-article style. Flat vector illustration, soft semi-3D shading, white
background, clean sans-serif labels in Inter, thin dashed connector lines,
generous whitespace. Muted clinical palette: light gray-blue anatomy with the
KDIGO heat-map gradient (green → yellow → orange → red) for the stage
indicators; pale pink pathology box, pale blue benefit box. No photorealism,
no dark background, no shadows, no clutter. Square 1:1 aspect (1024 × 1024).
Bottom-right corner: small semi-transparent navy text "© williamriveromd.com",
~11px, not obscuring the figure.

TOPIC: CKD severity along the eGFR spectrum — what each KDIGO stage looks
like inside the kidney and what management priorities apply at each stage.

DISEASE CONTEXT: CKD staging per KDIGO 2024.

CENTRAL MECHANISM: Progressive nephron loss reduces eGFR from ≥ 90 → < 15
mL/min/1.73 m². Glomerulosclerosis, tubulointerstitial fibrosis, and
peritubular capillary rarefaction accumulate stage by stage. Treatment focus
shifts from screening and lifestyle (early) → RAAS/SGLT2i and specialist
referral (mid) → preparation for kidney replacement therapy (late).

TOP LABEL BAND: "CKD STAGES BY eGFR — KDIGO 2024" in Inter, small caps.

ORGAN-LEVEL PANEL (top row, six kidney cross-sections in a horizontal strip):
Each kidney drawn in light gray-blue, with the KDIGO heat-map stage colour as
a thin tinted ring around it (Stage 1 green, Stage 2 light green-yellow,
Stage 3a yellow, Stage 3b orange, Stage 4 red-orange, Stage 5 deep red).
- Stage 1 — smooth cortex, intact medullary pyramids, full nephron mass
- Stage 2 — subtle cortical thinning
- Stage 3a — visible focal scarring
- Stage 3b — patchy atrophy, blurred corticomedullary junction
- Stage 4 — markedly shrunken, granular cortical surface
- Stage 5 — end-stage: severe atrophy, dilated pelvis, almost no functional cortex
Beneath each kidney, a tight caption block in Inter listing three lines:
1) "eGFR" band — Stage 1: "≥ 90"; Stage 2: "60–89"; Stage 3a: "45–59";
   Stage 3b: "30–44"; Stage 4: "15–29"; Stage 5: "< 15".
2) "% nephrons" remaining — Stage 1: "~100%"; Stage 2: "~75%"; Stage 3a:
   "~55%"; Stage 3b: "~40%"; Stage 4: "~25%"; Stage 5: "< 15%".
3) "Focus" — Stage 1: "Screen + lifestyle"; Stage 2: "Treat risk factors";
   Stage 3a: "RAAS + SGLT2i"; Stage 3b: "Refer to nephrology"; Stage 4:
   "Plan access / KRT"; Stage 5: "Dialysis or transplant".

MAGNIFIED MECHANISM PANEL (middle row, dashed border, single nephron drawn
six times, one per stage):
A single nephron at each stage with anatomically correct segments
(glomerulus, proximal tubule, loop of Henle, distal tubule, collecting duct)
on a pale yellow background. Show the progressive histology in concise
visual cues:
- Stage 1 — normal glomerulus, no fibrosis
- Stage 2 — early mesangial expansion
- Stage 3a — segmental glomerulosclerosis, early interstitial collagen
- Stage 3b — multifocal glomerulosclerosis, peritubular capillary rarefaction
- Stage 4 — global sclerosis in many glomeruli, dense interstitial fibrosis
- Stage 5 — widespread global sclerosis, tubular atrophy, sparse vasculature
A small dashed connector arrow links each kidney to its matching nephron
panel.

BOTTOM SUMMARY FLOW (full-width band, three boxes, left → right arrows):
- Left box (pale green): "EARLY (Stage 1–3a) — Annual eGFR + UACR · BP and
  glycemic control · Lifestyle · Avoid NSAIDs"
- Center box (pale yellow): "MID (Stage 3b–4) — Nephrology referral · RAAS
  blockade · SGLT2 inhibitor · Finerenone where indicated · Anemia / MBD
  workup · Vaccines · Vascular access planning"
- Right box (pale red): "LATE (Stage 5) — Dialysis prescription · Transplant
  evaluation · Conservative care if appropriate"

Medical accuracy: KDIGO 2024 thresholds are the standard reference;
percentages of remaining nephron mass are approximate teaching figures, label
them as such ("~"). All interventions named are standard of care; no
experimental flagging needed.
```

---

## Wiring after generation

Once both PNGs land in `images/`, run the WebP companion step and update
`guides/understanding-ckd.html`:

```bash
python3 -c "
from pathlib import Path
from PIL import Image
for stem in ['ckd-overview-mechanism', 'ckd-stages-mechanism']:
    p = Path('images') / f'{stem}.png'
    Image.open(p).convert('RGB').save(p.with_suffix('.webp'), 'webp', quality=85, method=6)
    print(f'  webp  {stem}')
"
```

Then in `understanding-ckd.html`, swap the two `<picture>` blocks so they
point at the new `ckd-overview-mechanism.png/.webp` and
`ckd-stages-mechanism.png/.webp` files; the old `ckd-understanding-overview.*`
and `ckd-stages-egfr.*` files can be removed once the wiring is verified.
