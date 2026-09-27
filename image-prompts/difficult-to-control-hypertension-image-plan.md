# Image Plan — *When Blood Pressure Stays High* (`difficult-to-control-hypertension.html`)

**Guide:** Difficult-to-control and resistant hypertension in Filipinos — dual-mode (Patients & Families / Clinicians), Philippine context
**Prepared:** 2026-09-27 · **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the
ChatGPT **Image Generator** GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` ·
`williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` ·
`williamriveromd-algorithm-generator-skill`

---

## House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff` / off-white `#fafafa` / soft gray `#f3f4f6` / pale teal `#eef6f7`).
  Never navy, charcoal, or black. Navy is for text and accents only.
- **Fonts:** on-image type is one of **Inter · Nunito Sans · IBM Plex Sans · Manrope**. No serif, no decorative type.
- **Palette:** navy `#0f1e2e` (text), clinical teal `#1a6b72` (headings, decisions), renal green `#1f7a4d`
  (safe/do this), amber `#b8860b` (caution), red `#b91c1c` (urgent), soft purple `#6c3d8e` (specialist/add-on).
- **Attribution:** small semi-transparent `renalcarematters.com` (algorithm and mechanism figures:
  `© renalcarematters.com`) bottom-right on landscape/square images, bottom-center on the portrait algorithm.
  **Exception:** the wordless vignette hero carries no text at all.
- **American English** on every label (e.g., "color," "organizer," "labeled").
- **Save each asset** as `.png` **and** a matching `.webp` twin under `images/`, using the exact FILE NAME below
  (the guide HTML already references `../images/<name>.webp` + `.png`).

### Clinical guardrails for THIS guide (must hold in every graphic)
- **No blame.** Patient figures never say "you failed," "noncompliant," or "lazy." Use "medicines not taken as
  prescribed," "refills hard to get," "hidden salt." Access and cost are system problems, not character flaws.
- **Apparent before true.** Every clinician graphic checks measurement, white-coat effect, adherence/access, and
  regimen *before* labeling resistance "true." Out-of-office BP (HBPM/ABPM) is the gatekeeper.
- **Generic names only.** No brand names, no doses, no mg strengths on any drug graphic.
- **ACE inhibitor OR ARB — never both.** Draw it as a choice, never a combination.
- **Spironolactone thresholds are guideline-attributed**, never invented: AHA/ACC eGFR ≥45; ESC eGFR ≥30 and
  K⁺ ≤4.5 mmol/L. Label potassium and kidney-function monitoring after starting.
- **Investigational means investigational.** Aldosterone synthase inhibitors (baxdrostat, lorundrostat) are labeled
  "investigational"; aprocitentan and renal denervation are "specialist / limited availability," not routine care.
- **No precise per-item sodium numbers** on the food figure. The only number is the WHO adult goal
  (<2,000 mg sodium/day ≈ 5 g salt ≈ 1 teaspoon, from all sources).
- **Potassium salt substitute caveat** always appears: people with kidney disease ask first.
- **No fear imagery.** No clutching-chest scenes, no exploding gauges, no red "danger" BP dials in patient art.

## Asset roster

| # | File (`images/…`) | Skill | Aspect | Size (px) | Audience |
|---|---|---|---|---|---|
| 1 | `difficult-to-control-hypertension-vignette-hero` | hero-vignette (Scaffold A) | 1:1 | 2048 × 2048 | mixed |
| 2 | `difficult-to-control-hypertension-01-why-bp-stays-high` | infographic (Archetype 4) | 4:3 | 1536 × 1152 | patients |
| 3 | `difficult-to-control-hypertension-02-home-bp-technique` | infographic (Archetype 4, numbered steps) | 4:3 | 1536 × 1152 | patients |
| 4 | `difficult-to-control-hypertension-03-apparent-vs-true-resistance` | simple-figure (Scaffold D, funnel) | 16:9 | 1792 × 1024 | clinicians |
| 5 | `difficult-to-control-hypertension-04-volume-aldosterone-mechanism` | biomedical-mechanism | 16:9 | 1792 × 1024 | clinicians |
| 6 | `difficult-to-control-hypertension-05-consultation-algorithm` | algorithm (Style Mode A, AHA) | 3:4 portrait | 1152 × 1536 | clinicians |
| 7 | `difficult-to-control-hypertension-06-ph-medication-ladder` | simple-figure (Scaffold C, ladder) | 16:9 | 1792 × 1024 | clinicians |
| 8 | `difficult-to-control-hypertension-07-filipino-sodium-swaps` | infographic (Archetype 6, food matrix) | 4:3 | 1536 × 1152 | patients |
| 9 | `difficult-to-control-hypertension-og` | infographic (OG / editorial poster) | 1.91:1 | 1200 × 630 (FIXED) | mixed |

> **After generating:** save PNG + WebP twins, then run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`,
> `patch_hero_maxwidth.py`, and `patch_image_lightbox.py` on the guide. Pair the OG card with
> `og:image:width="1200"` and `og:image:height="630"`. Each figure's `alt`, `fig-desc`, and `fig-abbrevs`
> lines below are ready to paste into its `<img alt>` and `<figcaption>`.

---

## 1 · Circular vignette hero

**alt:** A Filipino woman in her late 50s sits upright at a sunlit kitchen table with her arm resting on the table, measuring her blood pressure with an upper-arm cuff while her adult son sits beside her with a notebook and a weekly pill organizer.
**fig-desc:** *(hero — no figcaption; wordless image)*
**fig-abbrevs:** none

```
FILE NAME: difficult-to-control-hypertension-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A clinical people scene
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling (one cohesive home scene, no floating panels)
CAMERA: side profile at seated eye level, slightly over the table, shallow depth of field
HUMAN VARIATION (vs. previous guide): late-50s Filipino woman (not a clinician, not eating) with shoulder-length
  wavy hair tied loosely at the nape and a few silver strands, medium-tan skin, oval face, softly defined
  cheekbones, straight dark eyebrows, slim reading glasses pushed up on her head, small gold stud earrings,
  sleeveless-cardigan-over-sleeveless-top in muted coral and cream (upper arm bare for the cuff), average build;
  her son in his early 30s — lean, clean-shaven, short textured undercut, light olive gray t-shirt, wristwatch —
  sits beside her writing in a notebook. Home kitchen (not a clinic), side-profile framing (not a three-quarter
  seated portrait), calm focused expression rather than a posed smile; no teal polo, no beige blouse, no plated
  meal — at least 12 traits differ from the previous guide's cast.
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: "Checking BP at home, done right and done together" — a hopeful, capable, unhurried home scene.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR
vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle
must never touch the canvas edges). Composition archetype: Environmental Storytelling — one cohesive scene, no
floating panels. Camera: side profile at seated eye level, looking slightly across the tabletop, gentle shallow
depth of field.

Subject: a Filipino woman in her late 50s, shoulder-length wavy dark hair with a few silver strands tied loosely
at the nape, medium-tan skin, reading glasses resting on her head, muted coral cardigan open over a cream
sleeveless top, seated CORRECTLY for a home blood-pressure reading in a bright, clean Philippine home kitchen:
back resting against a chair with a supportive backrest, both feet flat on the floor, legs uncrossed, her left
forearm relaxed and supported on a pale laminate table so the upper arm is at heart level, a snug upper-arm BP
cuff wrapped on her BARE upper arm about two finger-widths above the elbow crease, a compact automatic
upper-arm monitor on the table (its display softly out of focus, no readable digits). Her expression is calm
and quietly focused; she is not talking. Beside her, her son in his early 30s (lean, short textured undercut,
olive-gray t-shirt) sits close and writes in an open paper notebook — the BP log — with a pen. On the table in
the foreground: a seven-day plastic pill organizer with small colored compartments and a glass of water.
Soft natural morning daylight from a side window with light sheer curtains, a few potted herbs on the sill.

Visual hierarchy: the woman, cuff, and monitor occupy 60–70% of the circle; 2–3 supporting elements (the son
with the notebook, the pill organizer, the window light) fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft
out-of-focus pale kitchen wall and diffuse daylight in the upper-left of the circle (no faces, hands, objects,
or text inside that zone). Warm, hopeful, documentary-realistic color grade harmonizing with clinical teal
#1a6b72 and navy #0f1e2e on a light background; gentle edge falloff toward a slightly deeper neutral at the
rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable monitor digits, readable
notebook handwriting, readable pill-box letters, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels,
infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy,
edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in
text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black
backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy.
Also avoid: cuff over a sleeve or on the forearm or wrist, arm dangling below heart level, crossed legs,
feet off the floor, person talking or on a phone, coffee cup or cigarette in view, worried or distressed
expression, hospital setting, white coat, plated meal, wooden dining table identical to other guides.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero
subject (the woman measuring correctly) at 60–70% of the circle, 2–3 supporting elements, 20–25% empty
upper-left title-safe zone. Posture is textbook-correct (back supported, feet flat, legs uncrossed, arm
supported at heart level, cuff on bare upper arm). Filipino home context, ≥12 traits visibly different from the
last guide. Camera framing (side profile) not repeated from the previous guide. Wordless; crops cleanly inside
the circle.
```

---

## 2 · Why BP can stay high — six common reasons (patient)

**alt:** Six rounded tiles explaining why blood pressure can stay high: measurement problems, the white-coat effect, medicines not taken as prescribed or refills hard to get, hidden salt in Filipino foods, medicines or products that raise BP, and another hidden condition such as aldosterone excess, sleep apnea, or kidney disease.
**fig-desc:** Blood pressure that stays high is usually a puzzle with fixable pieces. The six tiles show the most common reasons — how the reading is taken, nervousness at the clinic, trouble getting or taking medicines, hidden salt, products that push BP up, and a second condition your doctor can test for.
**fig-abbrevs:** BP — Blood pressure · NSAIDs — Nonsteroidal anti-inflammatory drugs (pain relievers such as ibuprofen, naproxen, mefenamic acid) · CKD — Chronic kidney disease

```html
<figcaption>
  <p class="fig-desc">Blood pressure that stays high is usually a puzzle with fixable pieces. The six tiles show the most common reasons — how the reading is taken, nervousness at the clinic, trouble getting or taking medicines, hidden salt, products that push BP up, and a second condition your doctor can test for.</p>
  <dl class="fig-abbrevs">
    <dt>BP</dt><dd>Blood pressure</dd>
    <dt>NSAIDs</dt><dd>Nonsteroidal anti-inflammatory drugs (pain relievers such as ibuprofen, naproxen, mefenamic acid)</dd>
    <dt>CKD</dt><dd>Chronic kidney disease</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-01-why-bp-stays-high.png
IMAGE TYPE: Multi-panel patient education infographic (Archetype 4) — 6-tile grid
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: Six friendly, blame-free tiles that name the common, fixable reasons BP stays high.

PROMPT:
Patient education infographic, 4:3 landscape, 1536×1152, clean WHITE (#ffffff) background, modern nephrology
clinic aesthetic, calm and reassuring. All text set in Inter (titles bold) and Nunito Sans (body), navy #0f1e2e.

Header band (soft pale teal #eef6f7, rounded): title in bold Inter navy "Why BP can stay high", subtitle in teal
#1a6b72 "Six common reasons — most can be fixed".

Body: a balanced 3 × 2 grid of SIX equal rounded cards on very soft gray #f3f4f6, each with a thin teal top
accent bar, one simple flat or softly semi-3D icon, a bold short heading, and 1–2 short plain-language lines:

1) Icon: upper-arm BP cuff and a small ruler. Heading "How it's measured". Lines: "Cuff too small or too loose ·
   arm hanging down · talking during the reading."
2) Icon: a clinic door with a small heartbeat line. Heading "White-coat effect". Lines: "BP rises at the clinic
   from nerves. Home readings show the real picture."
3) Icon: a weekly pill organizer and a pharmacy bag. Heading "Medicines not taken as prescribed". Lines:
   "Doses missed, cost, side effects, or refills hard to get — tell your doctor, there are options."
4) Icon: small realistic Filipino condiments — a bottle of patis, a bottle of toyo, a small jar of bagoong, and an
   instant-noodle pack (generic, NO brand logos or readable labels). Heading "Hidden salt in food". Lines:
   "Patis, toyo, bagoong, instant noodles, and processed foods add up fast."
5) Icon: a blister pack, a nasal decongestant box, and a small herbal-product bottle (all generic, unlabeled).
   Heading "Products that raise BP". Lines: "Pain relievers (NSAIDs), decongestants, some herbal products."
6) Icon: a simple kidney, an adrenal gland on top of the kidney, and a sleeping person with a soft snore wave.
   Heading "Another hidden condition". Lines: "Aldosterone excess, sleep apnea, kidney disease — tests can find
   them."

Footer strip (renal green #1f7a4d text on pale green-white): "Bring your home BP log and ALL your medicines and
supplements to your next visit." Use calm color logic — teal and green accents, one amber accent only on tile 5;
no red. Generous whitespace, rounded corners, mobile-readable labels (never smaller than ~11pt equivalent).
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No brand
names or logos on any product. No blaming words ("noncompliant," "failed," "lazy"), no red danger gauges, no
distressed faces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Exactly six equal tiles with the headings above, spelled correctly
(patis, toyo, bagoong). Blame-free wording. Mobile-readable. renalcarematters.com visible bottom-right.
```

---

## 3 · Home BP — how to measure it right (patient)

**alt:** Seven numbered steps for home blood pressure: use a validated upper-arm device, choose the right cuff size at heart level, sit quietly for 5 minutes with back supported and feet flat, avoid caffeine, exercise, and smoking for 30 minutes, take 2 readings 1 minute apart morning and evening, write every reading down, and measure for about 7 days before a visit.
**fig-desc:** A correct home reading is the most useful BP number your doctor can have. Follow the seven steps — right device, right cuff, right posture, quiet rest, two readings twice a day, a written log, and about a week of readings before your visit.
**fig-abbrevs:** BP — Blood pressure

```html
<figcaption>
  <p class="fig-desc">A correct home reading is the most useful BP number your doctor can have. Follow the seven steps — right device, right cuff, right posture, quiet rest, two readings twice a day, a written log, and about a week of readings before your visit.</p>
  <dl class="fig-abbrevs">
    <dt>BP</dt><dd>Blood pressure</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-02-home-bp-technique.png
IMAGE TYPE: Multi-panel patient education infographic (Archetype 4) — numbered step sequence with central posture figure
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: A single glance teaches correct home BP technique — posture in the center, seven numbered steps around it.

PROMPT:
Patient education infographic, 4:3 landscape, 1536×1152, clean WHITE (#ffffff) background, calm modern clinic
aesthetic. All text in Inter (bold headings) and Nunito Sans (short body lines), navy #0f1e2e.

Title at top in bold Inter navy: "Home BP: how to measure it right". Subtitle in teal #1a6b72: "Good readings =
better decisions".

CENTER: a clean, semi-photorealistic illustration of a Filipino adult (middle-aged man, short gray-flecked hair,
light polo shirt, sleeve rolled up) seated correctly at a small table — back against the chair, both feet flat on
the floor, legs uncrossed, left forearm resting on the table so the cuff sits at heart level, snug upper-arm cuff
on the bare arm, mouth closed (not talking). Thin teal leader callouts point to: "Back supported", "Feet flat,
legs uncrossed", "Cuff at heart level", "Bare upper arm". The monitor display shows no readable numbers.

Around the central figure, SEVEN numbered rounded step cards (teal number badges 1–7, soft gray #f3f4f6 cards,
one small flat icon each), reading clockwise from top-left:
1) "Use a validated upper-arm device" (icon: upper-arm monitor with a small checkmark seal; note: "Wrist and
   finger devices are less reliable").
2) "Right cuff size, at heart level" (icon: three cuffs small / regular / large).
3) "Sit quietly for 5 minutes first" (icon: chair and a 5-minute timer). Line: "Back supported, feet flat, legs
   uncrossed, no talking."
4) "30 minutes before: no coffee, exercise, or smoking" (icon: coffee cup, running shoe, cigarette, each with a
   soft strike-through in amber #b8860b).
5) "2 readings, 1 minute apart — morning and evening" (icon: sun and moon). Line: "Morning: before your medicines
   and before breakfast."
6) "Write every reading down" (icon: paper log and pen). Line: "Even the high ones and the low ones."
7) "About 7 days before your visit" (icon: small 7-day calendar strip). Line: "Bring the log to your doctor."

Footer strip in renal green #1f7a4d on a pale green-white band: "Keep every reading — your doctor needs the
whole week, not just the best one." Generous whitespace, balanced layout, mobile-readable labels.
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Do NOT show a
wrist cuff as the recommended device, a cuff over clothing, an arm hanging down, crossed legs, or a person
talking. No readable numbers on the monitor, no brand names. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Posture in the central figure is correct in every detail. Exactly seven
numbered steps with the wording above ("5 minutes," "30 minutes," "2 readings, 1 minute apart," "7 days").
Mobile-readable. renalcarematters.com visible bottom-right.
```

---

## 4 · Apparent vs. true resistant hypertension — the funnel (clinician)

**alt:** A funnel diagram. At the top, uncontrolled office BP on three drugs; five filters narrow the funnel — measurement error, white-coat effect checked with home or ambulatory BP, nonadherence or access barriers, a suboptimal regimen or no diuretic, and interfering substances. At the narrow bottom, true resistant hypertension leads to screening for primary aldosteronism, obstructive sleep apnea, CKD, and renovascular disease.
**fig-desc:** Most "resistant" hypertension is apparent, not true. Each filter removes a common, correctable cause of pseudoresistance; only patients who pass through all five have true resistant hypertension and warrant a structured search for secondary causes.
**fig-abbrevs:** BP — Blood pressure · HBPM — Home blood pressure monitoring · ABPM — Ambulatory blood pressure monitoring · NSAIDs — Nonsteroidal anti-inflammatory drugs · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease · PA — Primary aldosteronism

```html
<figcaption>
  <p class="fig-desc">Most "resistant" hypertension is apparent, not true. Each filter removes a common, correctable cause of pseudoresistance; only patients who pass through all five have true resistant hypertension and warrant a structured search for secondary causes.</p>
  <dl class="fig-abbrevs">
    <dt>BP</dt><dd>Blood pressure</dd>
    <dt>HBPM</dt><dd>Home blood pressure monitoring</dd>
    <dt>ABPM</dt><dd>Ambulatory blood pressure monitoring (24-hour)</dd>
    <dt>NSAIDs</dt><dd>Nonsteroidal anti-inflammatory drugs</dd>
    <dt>PA</dt><dd>Primary aldosteronism</dd>
    <dt>OSA</dt><dd>Obstructive sleep apnea</dd>
    <dt>CKD</dt><dd>Chronic kidney disease</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-03-apparent-vs-true-resistance.png
IMAGE TYPE: Simple figure — Scaffold D single-concept poster (vertical funnel with side filter labels)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show that pseudoresistance is filtered out step by step before anyone is labeled "true resistant."

PROMPT:
Clinical education figure, AJKD/NEJM graphical-abstract style, landscape 16:9, 1792×1024, clean WHITE (#ffffff)
background. Title at top-left in bold Inter navy #0f1e2e: "Apparent vs. true resistant hypertension".
Subtitle in teal #1a6b72 IBM Plex Sans: "Filter out pseudoresistance first".

CENTER: a large, clean, flat-vector funnel drawn with thin navy outlines and a soft pale teal (#eef6f7) fill,
wide at the top and narrowing to a small outlet at the bottom. At the funnel mouth, a wide rounded navy-outlined
entry card: "Uncontrolled office BP on 3 drugs".

Five horizontal filter bands cross the funnel from top to bottom, each band slightly narrower than the one above,
each with a small flat icon on the left edge and a label card to the right of the funnel connected by a thin
dashed teal leader. On the LEFT side of each band, a small amber (#b8860b) arrow exits the funnel with a short
gray note "apparent — correct & recheck":
Filter 1 — icon: cuff and ruler — "Measurement error" · note: "cuff size, posture, technique".
Filter 2 — icon: small clock with a home — "White-coat effect" · note: "confirm with HBPM or ABPM".
Filter 3 — icon: pill organizer and a pharmacy bag — "Nonadherence / access" · note: "cost, supply, side effects,
  complexity".
Filter 4 — icon: three stacked pill shapes — "Suboptimal regimen" · note: "no diuretic, doses not optimized,
  short-acting agents".
Filter 5 — icon: blister pack and small herbal bottle — "Interfering substances" · note: "NSAIDs, decongestants,
  alcohol, some herbal products".

BOTTOM OUTLET: a rounded renal-green (#1f7a4d) outlined card: "True resistant hypertension", with a thin arrow
into a pale-blue (#eef6f7) rounded box titled "Screen for secondary causes" listing four short items with small
icons: "Primary aldosteronism (PA)" · "Obstructive sleep apnea (OSA)" · "CKD" · "Renovascular disease".

Generous whitespace, perfectly aligned bands, muted clinical palette; mobile-readable labels (≥11pt equivalent).
Small semi-transparent navy "© renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No percentages or prevalence
numbers anywhere on the figure, no drug names or doses. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Entry card, five filters in the stated order, amber "apparent" exits, green
true-resistance outlet, four secondary causes. Mobile-readable, publication-grade. © renalcarematters.com visible
bottom-right.
```

---

## 5 · Volume and aldosterone — the mechanism behind resistance (clinician)

**alt:** Mechanism schematic. Left: organ panel showing the adrenal gland releasing aldosterone onto the kidney, with inputs of high sodium intake, obstructive sleep apnea, and CKD. Center-right: a dashed magnified inset of a collecting-duct principal cell showing aldosterone binding the mineralocorticoid receptor, more ENaC channels absorbing sodium, and ROMK secreting potassium. Bottom: a flow from sodium and aldosterone excess, through spironolactone, a thiazide-like diuretic, and sodium restriction, to lower BP; aldosterone synthase inhibitors are marked investigational upstream at CYP11B2.
**fig-desc:** In many people with resistant hypertension, BP stays high because the body holds on to too much sodium and fluid, often driven by excess aldosterone. Aldosterone acts on the collecting duct to open sodium channels and push out potassium. Blocking the receptor (spironolactone), adding a thiazide-like diuretic, and cutting dietary sodium each target this loop; aldosterone synthase inhibitors, which block aldosterone production upstream, remain investigational.
**fig-abbrevs:** BP — Blood pressure · MR — Mineralocorticoid receptor · ENaC — Epithelial sodium channel · ROMK — Renal outer medullary potassium channel · CYP11B2 — Aldosterone synthase gene/enzyme · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease · RAAS — Renin–angiotensin–aldosterone system · Na⁺ / K⁺ — Sodium / potassium ions

```html
<figcaption>
  <p class="fig-desc">In many people with resistant hypertension, BP stays high because the body holds on to too much sodium and fluid, often driven by excess aldosterone. Aldosterone acts on the collecting duct to open sodium channels and push out potassium. Blocking the receptor (spironolactone), adding a thiazide-like diuretic, and cutting dietary sodium each target this loop; aldosterone synthase inhibitors, which block aldosterone production upstream, remain investigational.</p>
  <dl class="fig-abbrevs">
    <dt>MR</dt><dd>Mineralocorticoid receptor</dd>
    <dt>ENaC</dt><dd>Epithelial sodium channel</dd>
    <dt>ROMK</dt><dd>Renal outer medullary potassium channel</dd>
    <dt>CYP11B2</dt><dd>Aldosterone synthase — the enzyme that makes aldosterone in the adrenal gland</dd>
    <dt>RAAS</dt><dd>Renin–angiotensin–aldosterone system</dd>
    <dt>OSA</dt><dd>Obstructive sleep apnea</dd>
    <dt>CKD</dt><dd>Chronic kidney disease</dd>
    <dt>Na⁺ / K⁺</dt><dd>Sodium / potassium ions</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-04-volume-aldosterone-mechanism.png
IMAGE TYPE: Biomedical mechanism figure — organ panel → dashed magnified principal-cell inset → bottom injury → intervention → benefit flow
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Make sodium/volume excess and aldosterone excess visible as the shared engine of resistant hypertension, and show where each therapy acts.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 16:9 landscape, 1792×1024, WHITE background,
scientific review-article style: flat vector illustration with soft semi-3D shading, thin dashed boxes for
magnified panels, muted clinical palette (light gray-blue anatomy, soft yellow highlighted tubular segment, red
for injury drivers, blue for protective/therapeutic effects, pale pink pathology box, pale blue benefit box).
All labels in clean sans-serif IBM Plex Sans (bold only for key terms), navy text.

Topic: Volume and aldosterone in resistant hypertension.
Title top-left in bold IBM Plex Sans navy: "Sodium, volume, and aldosterone: why BP resists treatment".

LEFT PANEL — organ-level context: a simplified kidney in coronal section with renal artery (red) and vein (blue),
the adrenal gland sitting on its upper pole highlighted in soft amber, a small label "Adrenal gland (zona
glomerulosa)" and a curved red arrow "Aldosterone ↑" from adrenal to the kidney. Three small driver icons feed
into the panel with thin red arrows, each with a short label:
- a salt shaker: "High sodium intake"
- a sleeping head with an airway narrowing: "OSA — sympathetic surges, aldosterone ↑"
- a small scarred kidney outline: "CKD — less sodium excretion"
A small dashed connector box on the kidney's medulla points to the magnified inset.

CENTER-RIGHT PANEL — dashed magnified inset "Collecting duct — principal cell": one large epithelial cell drawn
between a tubular lumen (left, labeled "Tubular lumen — urine side") and the peritubular blood side (right,
labeled "Blood side"). Inside the cell: aldosterone (small hexagon icon) entering from the blood side and binding
the "Mineralocorticoid receptor (MR)" in the cytoplasm, arrow to the nucleus "↑ gene transcription". On the
apical (lumen) membrane: multiple "ENaC" channels with Na⁺ arrows moving INTO the cell ("Na⁺ reabsorption ↑")
and a "ROMK" channel with a K⁺ arrow moving OUT into the lumen ("K⁺ secretion ↑"). On the basolateral membrane:
a "Na⁺/K⁺-ATPase" pump moving Na⁺ to blood and K⁺ into the cell. Small callouts on the right edge:
"↑ Na⁺ and water retention", "↑ plasma volume", "↑ BP", "↓ serum K⁺ (may be normal)".
Highlight the principal cell in soft yellow.

UPSTREAM NOTE (small, above the adrenal in the left panel): a pale purple (#6c3d8e outline) tag attached to the
adrenal: "CYP11B2 (aldosterone synthase) — blocked by aldosterone synthase inhibitors (baxdrostat,
lorundrostat): INVESTIGATIONAL". Keep it clearly separate and labeled investigational.

BOTTOM SUMMARY FLOW (three boxes left → right joined by arrows):
Left, pale pink box "Drivers": "Sodium / volume excess" · "Aldosterone excess (primary aldosteronism or
secondary)" · "OSA, CKD" · bold final line "**Volume-dependent hypertension**".
Center, white box with three small therapy icons, each labeled with its site of action:
"Spironolactone — blocks MR (monitor K⁺ and kidney function)" · "Thiazide-like diuretic — distal Na⁺
excretion" · "Sodium restriction — less Na⁺ load".
Right, pale blue box "Benefit": "↓ Na⁺ and fluid retention" · "↓ plasma volume" · bold final line "**Lower BP**".

Thin dashed connector lines, generous whitespace, no overcrowding, all labels legible at slide size.
Small semi-transparent navy "© renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, shadows, cartoonish styling, excessive icons,
overcrowding, gibberish text. NEVER use a navy, charcoal, or black background. Use ONLY Inter, Nunito Sans,
IBM Plex Sans, or Manrope — never a serif font. Do not place ENaC or ROMK on the basolateral side, do not place
the Na⁺/K⁺-ATPase on the apical side, do not draw aldosterone synthase inhibitors as approved routine therapy,
do not print drug doses or any numeric lab thresholds, no brand names. Never omit the © renalcarematters.com
attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Organ panel → dashed principal-cell inset → pink/white/blue bottom flow.
ENaC and ROMK apical, Na⁺/K⁺-ATPase basolateral, MR intracellular. CYP11B2 inhibitors clearly labeled
investigational. Labels medically precise and legible. © renalcarematters.com visible bottom-right.
```

---

## 6 · Consultation algorithm — persistently high BP (clinician)

**alt:** A vertical algorithm for persistently high blood pressure. Two early exits: urgent symptoms or acute organ injury route to the emergency department, and pregnancy or postpartum route to obstetric care. The main path then verifies measurement with home or ambulatory BP, reconciles the actual regimen and access, addresses contributors, screens for secondary causes, optimizes a RAS blocker plus a long-acting calcium channel blocker plus a thiazide-like diuretic, adds spironolactone if kidney function and potassium allow, and refers to a hypertension specialist or nephrology if BP remains uncontrolled.
**fig-desc:** A stepwise consultation for BP that stays high. Emergencies and pregnancy leave the pathway first; then the true BP is confirmed out of the office, the real-world regimen is checked, contributors and secondary causes are addressed, and only then is therapy escalated — with spironolactone when kidney function and potassium allow, and specialist referral if control is still not reached.
**fig-abbrevs:** BP — Blood pressure · HBPM — Home blood pressure monitoring · ABPM — Ambulatory blood pressure monitoring · NSAIDs — Nonsteroidal anti-inflammatory drugs · PA — Primary aldosteronism · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease · RAS — Renin–angiotensin system · CCB — Calcium channel blocker · eGFR — Estimated glomerular filtration rate · K⁺ — Serum potassium · AHA/ACC — American Heart Association / American College of Cardiology · ESC — European Society of Cardiology

```html
<figcaption>
  <p class="fig-desc">A stepwise consultation for BP that stays high. Emergencies and pregnancy leave the pathway first; then the true BP is confirmed out of the office, the real-world regimen is checked, contributors and secondary causes are addressed, and only then is therapy escalated — with spironolactone when kidney function and potassium allow, and specialist referral if control is still not reached.</p>
  <dl class="fig-abbrevs">
    <dt>BP</dt><dd>Blood pressure</dd>
    <dt>HBPM</dt><dd>Home blood pressure monitoring</dd>
    <dt>ABPM</dt><dd>Ambulatory blood pressure monitoring (24-hour)</dd>
    <dt>NSAIDs</dt><dd>Nonsteroidal anti-inflammatory drugs</dd>
    <dt>PA</dt><dd>Primary aldosteronism</dd>
    <dt>OSA</dt><dd>Obstructive sleep apnea</dd>
    <dt>CKD</dt><dd>Chronic kidney disease</dd>
    <dt>RAS</dt><dd>Renin–angiotensin system (ACE inhibitor or ARB)</dd>
    <dt>CCB</dt><dd>Calcium channel blocker</dd>
    <dt>eGFR</dt><dd>Estimated glomerular filtration rate</dd>
    <dt>K⁺</dt><dd>Serum potassium</dd>
    <dt>AHA/ACC</dt><dd>American Heart Association / American College of Cardiology</dd>
    <dt>ESC</dt><dd>European Society of Cardiology</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-05-consultation-algorithm.png
IMAGE TYPE: Clinical algorithm — Style Mode A (AHA provider-algorithm aesthetic), portrait
ASPECT RATIO: 3:4 portrait
PIXEL DIMENSIONS: 1152 × 1536
AUDIENCE: clinicians
VISUAL GOAL: A single top-to-bottom consultation pathway that exits emergencies and pregnancy early and only escalates drugs after verification.

PROMPT:
Create a polished medical guideline algorithm flowchart in the style of an American Heart Association provider
algorithm, portrait 3:4, 1152×1536. Use a white background, clean sans-serif typography set in Inter (bold
black/navy titles, regular body), thin black arrows, pastel rounded boxes, and pink decision diamonds. Layout
portrait, centered, spacious, and easy to read.

Visual conventions:
- Peach/orange rounded boxes for initial assessment steps
- Pink diamond boxes for decision questions
- Blue rounded boxes for active treatment steps
- Green rounded boxes for verification, monitoring, and supportive steps
- Gray capsule boxes for transitional steps
- Red bold labels beside arrows for emergency branches
- A dashed horizontal divider separating "Verify & correct" (upper) from "Treat & escalate" (lower)

Title at top-left in bold Inter: "Persistently high BP: consultation algorithm".

Content to render (top to bottom):
1. Peach box: "Persistently high BP"
2. Pink diamond: "Urgent symptoms or acute organ injury?" → right branch, red bold label "YES" → red-outlined
   box "Emergency care now" (small note: "chest pain, breathlessness, neurologic deficit, vision change,
   confusion"). Down arrow "NO".
3. Pink diamond: "Pregnant or postpartum?" → left branch, red bold label "YES" → rounded box "Obstetric /
   maternal-medicine pathway". Down arrow "NO".
4. Green box: "Verify measurement + out-of-office BP (HBPM or ABPM)" · note: "correct cuff & technique; exclude
   white-coat effect".
5. Green box: "Reconcile the ACTUAL regimen & access" · note: "what is taken, cost, supply, side effects".
6. Green box: "Address contributors" · note: "sodium · alcohol · NSAIDs/decongestants · sleep".
7. Gray capsule: "Screen secondary causes" with four short bullets: "PA (aldosterone/renin)" · "OSA" ·
   "CKD / albuminuria" · "Renovascular".
   — dashed horizontal divider here —
8. Blue box: "Optimize: RAS blocker (ACE inhibitor OR ARB) + long-acting CCB + thiazide-like diuretic".
9. Pink diamond: "Still uncontrolled?" → side branch "NO" → green box "Continue & monitor". Down arrow "YES".
10. Blue box: "Add spironolactone if eGFR & K⁺ allow" · small gray note beneath in Nunito Sans:
    "AHA/ACC: eGFR ≥45 · ESC: eGFR ≥30 and K⁺ ≤4.5 · recheck K⁺ and creatinine".
11. Pink diamond: "Still uncontrolled?" → "YES" →
12. Purple-outlined box (#6c3d8e): "Refer: hypertension specialist / nephrology" · note: "renal denervation only at
    expert centers".

Design requirements: title at top; no decorative icons; no photos; no 3D; no dark background; no excessive
shadows; short readable text in every box; strict alignment and consistent spacing; maximum branch depth kept
tidy with side exits returning cleanly. Include a small professional footer reading "© renalcarematters.com"
positioned at the bottom-center in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, spaghetti arrows, overlapping branches.
NEVER use a dark, navy, charcoal, or black background. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope —
no serif fonts. No brand names, no doses, no ACE-inhibitor-plus-ARB combination. Never omit the
© renalcarematters.com footer.

QUALITY CHECK:
3:4, 1152×1536, white background. Emergency and pregnancy exits come BEFORE verification; verification,
regimen, contributors, and secondary causes come BEFORE drug escalation. Spironolactone thresholds attributed to
AHA/ACC and ESC exactly as written. © renalcarematters.com visible bottom-center.
```

---

## 7 · Philippine medication ladder (clinician)

**alt:** A rising staircase of blood pressure treatment steps. Level 0 fixes the reason first; Level 1 is an ACE inhibitor or ARB, never both, plus amlodipine; Level 2 adds a thiazide-like diuretic, with a CKD overlay for furosemide; Level 3 adds spironolactone, with eplerenone or amiloride as Level 3A if not tolerated; Level 4 adds bisoprolol or carvedilol; Level 5 is clonidine with a rebound caution; Level 6 is specialist care with doxazosin, hydralazine, minoxidil, renal denervation, and emerging agents.
**fig-desc:** A practical, stepwise medicine ladder built for what is usually available in the Philippines. The first step is always fixing the reason BP is high; drugs are then added one level at a time, with a kidney-disease overlay for loop diuretics and a specialist tier for the last-line and emerging options. Generic names only; doses are set by your doctor.
**fig-abbrevs:** BP — Blood pressure · ACE — Angiotensin-converting enzyme · ARB — Angiotensin II receptor blocker · SR — Sustained release · HCTZ — Hydrochlorothiazide · CKD — Chronic kidney disease · K⁺ — Serum potassium

```html
<figcaption>
  <p class="fig-desc">A practical, stepwise medicine ladder built for what is usually available in the Philippines. The first step is always fixing the reason BP is high; drugs are then added one level at a time, with a kidney-disease overlay for loop diuretics and a specialist tier for the last-line and emerging options. Generic names only; doses are set by your doctor.</p>
  <dl class="fig-abbrevs">
    <dt>BP</dt><dd>Blood pressure</dd>
    <dt>ACE</dt><dd>Angiotensin-converting enzyme</dd>
    <dt>ARB</dt><dd>Angiotensin II receptor blocker</dd>
    <dt>SR</dt><dd>Sustained release</dd>
    <dt>HCTZ</dt><dd>Hydrochlorothiazide</dd>
    <dt>CKD</dt><dd>Chronic kidney disease</dd>
    <dt>K⁺</dt><dd>Serum potassium</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-06-ph-medication-ladder.png
IMAGE TYPE: Simple figure — Scaffold C step sequence rendered as an ascending staircase ladder
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: One glance shows the escalation order — fix the reason first, then add one class per step — adapted to Philippine availability.

PROMPT:
Clean clinical education infographic, landscape 16:9, 1792×1024, WHITE (#ffffff) background, publication-grade
nephrology design. Title at top-left in bold Inter navy #0f1e2e: "Resistant hypertension: a Philippine
medication ladder". Subtitle in teal #1a6b72: "Generic names · one step at a time · no doses shown".

Draw an ascending STAIRCASE of eight rounded step cards rising from bottom-left to top-right, each card resting on
the step below and connected by a thin navy up-arrow, each with a colored top accent band, a bold level badge,
and 1–3 short lines in Nunito Sans:

Level 0 (green #1f7a4d band) — "Fix the reason": "measurement · adherence · access · secondary causes".
Level 1 (teal #1a6b72 band) — "ACE inhibitor OR ARB + amlodipine". Small red (#b91c1c) note: "never ACE inhibitor
  + ARB together".
Level 2 (teal band) — "Add thiazide-like diuretic": "indapamide SR" · "HCTZ in combination (access
  alternative)" · "chlorthalidone only if locally available".
  Attached below Level 2 as a small side tag with a dashed outline in amber #b8860b: "CKD overlay: loop
  diuretic (furosemide) for volume overload or advanced CKD".
Level 3 (teal band) — "Add spironolactone": "check K⁺ and kidney function first and after".
Level 3A (amber band, drawn as a small side step off Level 3) — "If spironolactone not tolerated":
  "eplerenone or amiloride — verify local supply".
Level 4 (teal band) — "Add bisoprolol or carvedilol": "earlier if a compelling indication (heart failure,
  coronary disease, rate control)".
Level 5 (amber band) — "Clonidine": "use carefully — rebound BP if stopped abruptly".
Level 6 (soft purple #6c3d8e band, top step) — "Specialist": "doxazosin · hydralazine · minoxidil · renal
  denervation (expert centers)" · small italic gray line "Emerging: aprocitentan, aldosterone synthase
  inhibitors (investigational)".

Cards on very soft gray (#f3f4f6), generous whitespace, balanced diagonal composition, mobile-readable labels
(≥11pt equivalent). Bottom strip, full width, soft gray: navy text "Move up only after confirming true BP and
adherence at the current step." Small semi-transparent navy "renalcarematters.com" attribution in the
bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed
HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no
decorative or handwritten typefaces. No brand names, no doses, no mg strengths, no pill photos with imprints.
Do not show ACE inhibitor and ARB combined. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Eight steps in order 0 → 1 → 2 (+CKD overlay) → 3 → 3A (side) → 4 → 5 → 6.
Generic names spelled correctly (indapamide, hydrochlorothiazide, chlorthalidone, furosemide, spironolactone,
eplerenone, amiloride, bisoprolol, carvedilol, clonidine, doxazosin, hydralazine, minoxidil, aprocitentan).
Investigational items labeled. renalcarematters.com visible bottom-right.
```

---

## 8 · Filipino sodium swaps (patient)

**alt:** A food matrix pairing common high-sodium Filipino items — patis, toyo, bagoong, seasoning cubes, instant noodles, tuyo and daing, and processed meats such as hotdog, longganisa, and corned beef — with lower-sodium swaps such as calamansi, garlic, onion, ginger, fresh fish and vegetables, using half the noodle seasoning packet, and rinsing canned goods. A goal bar shows the WHO adult limit of less than 2,000 mg sodium a day, about 5 g of salt or 1 teaspoon, and a caution panel advises people with kidney disease to ask before using potassium-based salt substitutes.
**fig-desc:** Most of the salt Filipinos eat comes from condiments, dried fish, instant noodles, and processed meats rather than the salt shaker. Each high-salt item is paired with an easy swap. The daily goal for adults is less than 2,000 mg of sodium from all sources — about one teaspoon of salt in total. If you have kidney disease, ask your doctor before using a "lite" or potassium-based salt substitute.
**fig-abbrevs:** WHO — World Health Organization · mg — milligrams · g — grams

```html
<figcaption>
  <p class="fig-desc">Most of the salt Filipinos eat comes from condiments, dried fish, instant noodles, and processed meats rather than the salt shaker. Each high-salt item is paired with an easy swap. The daily goal for adults is less than 2,000 mg of sodium from all sources — about one teaspoon of salt in total. If you have kidney disease, ask your doctor before using a "lite" or potassium-based salt substitute.</p>
  <dl class="fig-abbrevs">
    <dt>WHO</dt><dd>World Health Organization</dd>
    <dt>mg</dt><dd>Milligrams</dd>
    <dt>g</dt><dd>Grams</dd>
  </dl>
</figcaption>
```

```
FILE NAME: difficult-to-control-hypertension-07-filipino-sodium-swaps.png
IMAGE TYPE: Food matrix / nutrition infographic (Archetype 6) — "instead of → try" swap grid
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: Make hidden Filipino sodium sources recognizable and each one paired with a realistic, tasty swap.

PROMPT:
CKD and hypertension nutrition infographic, clean educational food matrix, 4:3 landscape, 1536×1152, WHITE
(#ffffff) background. All text in Inter (bold headings) and Nunito Sans (body), navy #0f1e2e.

Title at top in bold Inter navy: "Cut the hidden salt — Filipino swaps". Subtitle in teal #1a6b72: "Flavor stays.
Sodium goes down."

GOAL BAR directly under the title, a soft pale-teal rounded band with a simple teaspoon icon: "Adult goal (WHO):
less than 2,000 mg sodium a day ≈ 5 g salt ≈ 1 teaspoon — from ALL food and condiments combined."

MAIN GRID: two columns joined by small green right-arrows. Left column header in amber #b8860b "Instead of…",
right column header in renal green #1f7a4d "Try…". Seven rows, each with realistic, appetizing small food
renders (generic, NO brand logos or readable labels):
1) Patis (fish sauce bottle) → calamansi squeeze, garlic, and a little patis only at the table, not in the pot.
2) Toyo (soy sauce bottle) → calamansi, garlic, onion, and a splash of vinegar.
3) Bagoong (small jar) → a small side portion shared, with fresh green mango or vegetables.
4) Seasoning cubes / powdered seasoning → garlic, onion, ginger, tanglad (lemongrass), and black pepper.
5) Instant noodles (generic cup and pack) → cook with HALF the seasoning packet and add fresh vegetables and egg.
6) Tuyo and daing (dried salted fish) → fresh fish — grilled, steamed, or sinigang with plenty of vegetables.
7) Processed meats — hotdog, longganisa, corned beef (can) → fresh chicken or pork; if using canned goods,
   rinse and drain them first.
Show NO sodium numbers on any individual food item.

CAUTION PANEL at bottom-right, pale amber rounded box with a small kidney icon and amber accent: "Kidney disease?
Ask your doctor before using 'lite' or potassium-based salt substitutes — they can raise potassium."

FOOTER strip, soft gray, navy text: "Taste food before salting · read labels · keep condiments off the table."
Rounded category cards, generous whitespace, mobile-readable labels. Small semi-transparent navy
"renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed
HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No brand names or readable
packaging, no per-food sodium milligram values, no shaming words ("bad food," "forbidden"). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Seven instead-of → try rows with Filipino items spelled correctly (patis, toyo,
bagoong, tuyo, daing, longganisa, calamansi, tanglad). The only number is the WHO goal. Potassium-substitute
caution present. Mobile-readable. renalcarematters.com visible bottom-right.
```

---

## 9 · OG / social share card

**alt:** Social share card for "When Blood Pressure Stays High": a Filipino woman measuring her blood pressure at home with an upper-arm cuff on the left, and the title with the subtitle "Difficult-to-control & resistant hypertension · A guide for Filipino patients and clinicians" on the right.
**fig-desc:** *(OG card — not placed in a figure; no figcaption)*
**fig-abbrevs:** none

```
FILE NAME: difficult-to-control-hypertension-og.png
IMAGE TYPE: Editorial hero + title OG / social share card (Archetype 1, with baked title text)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (FIXED — never any other size for an OG card)
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: One glance says "high BP that won't come down has fixable reasons" — calm home measurement scene plus a clear, legible title.

PROMPT:
Photorealistic medical editorial OG / social share card, exactly 1200×630 px, for a nephrology and hypertension
education guide, on a clean WHITE / off-white (#fafafa) background. Split composition:

LEFT ~52%: a bright, naturally lit, photorealistic scene of a Filipino woman in her late 50s seated correctly at a
light kitchen table — back supported, feet flat, forearm resting on the table, snug upper-arm BP cuff on her bare
upper arm, a compact automatic monitor with no readable digits, a seven-day pill organizer and an open paper
notebook beside her — calm, hopeful, documentary-realistic, soft daylight. The scene fades softly into the white
background on its right edge (no hard border).

RIGHT ~48%: a clean off-white panel carrying the text, left-aligned, with a thin teal #1a6b72 vertical accent rule:
- Small teal label in Manrope uppercase tracking: "renalcarematters.com guide"
- Title in bold Inter, navy #0f1e2e, large and mobile-legible, on two lines: "When Blood Pressure Stays High"
- Subtitle in Nunito Sans, teal #1a6b72, medium weight: "Difficult-to-control & resistant hypertension · A guide
  for Filipino patients and clinicians"
- A tiny row of three simple flat line icons in teal and renal green #1f7a4d below the subtitle: upper-arm cuff,
  salt shaker with a downward arrow, pill organizer.

Strong hierarchy, generous negative space, rounded soft panel edges, publication-grade editorial look. Keep all
text within a safe margin of at least 48 px from every edge so social-platform cropping never clips it. Small
semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No red BP
gauge, no alarm imagery, no clutching-chest pose, no readable monitor numbers, no brand logos. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title "When Blood Pressure Stays High" and the subtitle spelled exactly as given, legible at
thumbnail size. Light background, calm Filipino home-measurement scene with correct posture. renalcarematters.com
visible bottom-right. Pair with og:image:width="1200" og:image:height="630".
```

---

## Final checklist before wiring
1. Every file saved as `.png` + `.webp` under `images/` with the exact names above.
2. Every in-body figure's `<img>` carries the `alt` above, the stated `width`/`height`, and a `<figcaption>` with
   `p.fig-desc` + `dl.fig-abbrevs` (rule 11); every acronym in the figure also appears in the guide's Glossary
   (rule 12).
3. Spot-check each generated image for: American spelling, correct Filipino food names, no brand names, no doses,
   ACE inhibitor OR ARB (never both), investigational labels intact, correct ENaC/ROMK/pump sidedness, and the
   renalcarematters.com attribution.
4. Re-run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, and
   `patch_image_lightbox.py` on `guides/difficult-to-control-hypertension.html`.
