# Origins — 3D Photorealistic Stage Renders (E1–E8)

**For:** the "Origins" scroll sequence on `guides/kidney-physiology.html`.
**Used as:** 8 transparent PNGs stacked in a pinned layer, **cross-fading on scroll**
(stage 1 → stage 8) so the kidney appears to *develop* as the visitor scrolls.
**Save to:** `images/origins/` with the **exact filenames** below (`.png`). They replace
the earlier SVGs (same base names).
**Generator:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator

---

## ⚠️ House-rule override (read first)
The infographic skill normally forbids dark backgrounds and requires a baked
`williamriveromd.com` mark. For THIS set, because the frames are layered animation
cells on a near-black cinematic page:
- **Background MUST be fully TRANSPARENT (alpha PNG).** No white, no black, no box.
- **No baked-in attribution** on these frames (they stack; the page footer carries the
  credit). No text/labels of any kind.

## Shared style — paste at the TOP of every one of the 8 prompts
> **3D photorealistic medical render of embryonic/fetal kidney tissue, single subject,
> floating on a FULLY TRANSPARENT background (alpha, no backdrop, no box, no ground
> shadow plane).** Semi-glossy wet biological tissue with subtle subsurface scattering;
> soft studio key light from upper-left, a cool **teal rim light** and a warm **gold rim
> light** on the edges so it reads on a dark page. Restrained, premium, anatomically
> accurate — like a NEJM/Netter 3D medical visualization, not cartoon, not neon.
> **Identical camera for all frames:** 3/4 anterolateral view, subject centered, same
> distance and scale framing so the eight images line up when cross-faded. Square 1:1.
> Tissue palette: living kidney reds/pinks (#c8606a–#8d3f5f), pale translucent ducts,
> faint cyan/gold edge glow. **No text, no labels, no arrows, no watermark, no caption.**
> Photoreal, high detail, clean alpha edges.

**Aspect / size for all 8:** 1:1, **1254 × 1254 px**. (gpt-image / GPT Image Generator 2
can output transparent PNG — request "transparent background".)

**Critical consistency:** same camera, same lighting, same center, and a **growing scale**
across the set — the structure should look like ONE thing maturing, not eight separate
objects. Rough on-canvas size: E1 ≈ 22% → E2 ≈ 40% → E3 ≈ 45% → E4 ≈ 58% → E5 ≈ 66%
→ E6 ≈ 72% → E7 ≈ 84% → E8 ≈ 92% of the frame height.

---

## THE 8 PROMPTS (append each to the shared style above)

### `kp-dev-1-pronephros.png` — Pronephros · wk 3–4
A tiny, primitive structure: ~6–7 pale, semi-translucent **pronephric tubule** segments
arranged along a slender **nephric (Wolffian) duct** that runs vertically. Embryonic,
delicate, gel-like, minimal — the faintest beginning. Small in frame.

### `kp-dev-2-mesonephros.png` — Mesonephros · wk 4–8
An elongated vertical array of small **mesonephric tubules**, each ending in a tiny
rounded vesicle, draining into a continuous **Wolffian duct** beside them. More
developed and orderly than E1; clearly "grown downward." Still translucent embryonic tissue.

### `kp-dev-3-ureteric-bud.png` — Ureteric bud induction · wk 5–6
The lower **Wolffian duct** with a rounded **ureteric bud** sprouting from it and pushing
into a soft, rounded **cap of metanephric mesenchyme** (a pale pink blastema mass). Two
tissues meeting — the bud tip nestled into the cap. Gentle translucency.

### `kp-dev-4-branching.png` — Branching morphogenesis · wk 6–10
An early kidney mass in which the **ureteric tree branches** — a stalk dividing into ~3
generations of Y-shaped tubular branches (future pelvis → calyces → collecting ducts),
embedded in a translucent metanephric blastema. The organ is taking on a rounded form.

### `kp-dev-5-nephrogenesis.png` — Nephrogenesis · wk 7–36
A small developing kidney with a visible **cortex studded with forming nephrons** — tiny
spherical **glomeruli** and comma/S-shaped tubules near the surface, the branching
collecting tree faintly visible within. The filtering units are appearing across the surface.

### `kp-dev-6-ascent-rotation.png` — Ascent & rotation · wk 6–9
A small **fetal kidney bean**, tilted ~15–20° mid-rotation, with the **hilum turning to
face medially** and slender **renal vessels** emerging. A sense of motion/repositioning.
Smooth surface beginning to form.

### `kp-dev-7-fetal-kidney.png` — Mature fetal kidney · wk 10–birth
A nearly complete **fetal kidney with visible lobulation** (the cobblestone renunculi /
fetal lobules on the surface), defined **hilum**, **renal artery/vein and ureter** at the
hilum. Fuller, glossier, almost mature.

### `kp-dev-8-mature-kidney.png` — Mature kidney
A fully formed, smooth **adult kidney bean**: clean cortical surface, deep **hilum** with
**renal artery (red), renal vein (blue), and ureter** exiting, optional faint internal
hint of pelvis/calyces. The finished organ — largest and most resolved frame.

---

## Background motif — "the passage of time" (I build this in-page; not an image)
Rather than a static blob behind the kidney, the background becomes a subtle **gestational
timeline** that advances with the same scroll:
- **Option A (recommended):** the big background numeral shows the **gestational age** of
  the current stage ("WEEK 4" → "WEEK 8" → … → "BIRTH") instead of "E1…E8", and the gold
  vertical spine becomes a **week-3-to-birth timeline** that fills as you scroll.
- **Option B:** a faint, slowly rotating **clock / arc** behind the kidney that sweeps from
  empty to full across the 8 stages.
- **Option C:** faint concentric **growth rings** (like tree rings) expanding outward as
  development proceeds.

I'll wire **Option A** by default (it reuses the per-stage week data, stays subtle, and is
unmistakably "time"); say the word if you'd rather B or C.

---

## Checklist
- [ ] 8 PNGs, exact names above, in `images/origins/`
- [ ] **Transparent** alpha background, no box, no text, no watermark
- [ ] Same camera/lighting/center across all 8; size grows E1→E8
- [ ] 1254 × 1254
