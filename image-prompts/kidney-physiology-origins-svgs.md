# Origins — Developmental Stage SVGs (you generate, I wire)

**Where they go:** the "Origins" section of `guides/kidney-physiology.html`.
**How they're used:** 8 SVGs are stacked in a pinned layer and **cross-fade one into
the next as the visitor scrolls** (stage 1 → stage 8). Done right, the sequence reads
as a single kidney *developing*. So the 8 files must look like **one continuous
illustration that grows and reshapes** — same style, same framing, same line language.

**Deliver:** 8 standalone `.svg` files, uploaded to **`images/origins/`** with the exact
names below. Tell me when they're in and I'll wire the cross-fade + sync them to the
stage cards, numeral, and progress spine.

---

## GLOBAL SPEC — identical for all 8 (this is what makes the transition work)

- **Canvas / viewBox:** exactly `viewBox="0 0 1200 1200"` on every file. Same coordinate
  space so the shapes align when they cross-fade.
- **Background:** fully **transparent** — no `<rect>` fill, no white, no black.
- **Subject placement:** **horizontally centered**, vertically centered on ~`y=600`.
  Keep the center of mass in the same place across all 8 so it doesn't jump.
- **Scale progression (critical):** the structure should **grow** across the stages —
  small/sparse early, large/complete late. Target heights (of the 1200 canvas):
  E1 ≈ 18% · E2 ≈ 42% · E3 ≈ 40% · E4 ≈ 58% · E5 ≈ 62% · E6 ≈ 66% · E7 ≈ 82% · E8 ≈ 90%.
- **Style — luminous line-art on dark (the page canvas is `#02060a`):**
  - `fill:none` for structures (or very low-opacity glow fills only).
  - **Primary stroke:** off-white `#e8f4f8`.
  - **Accents:** gold `#d4af4f`, cyan `#7be3ff`, teal `#2c97a3`; use a soft red `#ff8a8a`
    only for arteries/blood if needed.
  - `stroke-width` **5–7** at this viewBox; `stroke-linecap="round"`, `stroke-linejoin="round"`.
  - Keep the **same stroke weight, palette, and level of detail in all 8** — consistency
    over flourish. (I add the outer glow + subtle breathing in CSS, so you don't have to.)
- **NO text / labels / titles / week-numbers / arrows-with-words** anywhere in the SVG.
  All wording lives in the HTML cards beside the art.
- **No `<style>` blocks; avoid internal `id`s** (gradients/filters). If you must use an
  `id`, prefix it uniquely per file (e.g. `e1-grad`) so 8 inlined SVGs don't collide.
  Plain stroked `<path>`/`<circle>`/`<g>` is ideal.
- **Optimize** (SVGO is fine) but keep paths readable. One artwork per file.

---

## THE 8 STAGES

> Anatomy notes are the *content*; render each in the shared luminous style above.
> Think of it as the same camera watching one structure grow.

### `images/origins/kp-dev-1-pronephros.svg` — Pronephros · wk 3–4  (~18%)
A small, sparse cluster near center: ~6–7 tiny paired tubule loops alongside a thin
vertical **duct line** beginning to extend downward. Faint, primitive, minimal.

### `images/origins/kp-dev-2-mesonephros.svg` — Mesonephros · wk 4–8  (~42%)
A taller **vertical column** of small tubules (each a little loop/comma) draining into a
single duct running top-to-bottom. Elongated and orderly — the structure has grown
downward from stage 1.

### `images/origins/kp-dev-3-ureteric-bud.svg` — Ureteric bud induction · wk 5–6  (~40%)
The duct from stage 2, now with a rounded **bud** sprouting from its lower end and
pushing into a soft **cap/cloud of mesenchyme** (a light, slightly dashed blob). Two
forms meeting. A couple of subtle cyan signal arrows (no text) between them are fine.

### `images/origins/kp-dev-4-branching.svg` — Branching morphogenesis · wk 6–10  (~58%)
The bud has become a **branching tree** — a stalk dividing into ~3 generations of
Y-branches (pelvis → calyces → ducts), inside a faint early kidney outline. Each tip
ends in a tiny node (future nephron). Tree drawn in off-white; outline faint.

### `images/origins/kp-dev-5-nephrogenesis.svg` — Nephrogenesis · wk 7–36  (~62%)
A forming **nephron** front-and-center: a **glomerulus** (small circle/coil) joined to an
**S-shaped tubule**, with the branching tree from stage 4 faint behind it. This is the
filter taking shape. Glomerulus can glow cyan/gold.

### `images/origins/kp-dev-6-ascent-rotation.svg` — Ascent & rotation · wk 6–9  (~66%)
A recognizable **bean-shaped kidney** now, **tilted ~15–20°** (mid-rotation), with a soft
upward **motion arc / trail** suggesting it is climbing into position. Internal tree faint.

### `images/origins/kp-dev-7-fetal-kidney.svg` — Mature fetal kidney · wk 10–birth  (~82%)
A fuller kidney bean with **gentle lobulation** (a few shallow scallops on the outer
edge — fetal lobulation), the collecting tree visible inside. Upright. Nearly complete.

### `images/origins/kp-dev-8-mature-kidney.svg` — Mature kidney  (~90%)
A clean, smooth **kidney bean** with a clear **hilum notch** on the medial side, the full
**collecting system** inside (pelvis → major/minor calyces) and a hint of vessels at the
hilum (one red artery line is okay). The finished organ — the largest, most resolved frame.

---

## DELIVERY CHECKLIST
- [ ] 8 files, exact names above, in `images/origins/`
- [ ] Every file `viewBox="0 0 1200 1200"`, transparent, centered, no text
- [ ] Same stroke weight + palette across all 8; size grows E1→E8 per the targets
- [ ] No internal `id` collisions (prefix per file if used)

When they're uploaded, ping me — I'll stack them in the pinned Origins layer, cross-fade
on scroll, and keep the stage card / "E1…E8" numeral / gold spine in sync. (Reduced-motion
and mobile will show the final mature-kidney frame, static.)

---

### Optional — if you'd rather have a *true* morph than a cross-fade
Only possible if every file is a **single `<path>` with the same number of points in the
same order** (so coordinates can be interpolated). That's hard to author by hand/AI, so
**cross-fade is the recommended default**. If your tool can export matched-node paths,
say so and I'll do a true point-interpolated morph instead.
