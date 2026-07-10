# Image Plan — Low-Carb & Keto: Fad, Fix, or Hazard for Your Kidneys?

**Guide:** `guides/low-carb-diet-kidney.html`
**Canonical:** https://renalcarematters.com/guides/low-carb-diet-kidney.html
**Generated with:** `williamriveromd-hero-vignette`, `williamriveromd-infographic-skill`, `williamriveromd-biomedical-mechanism-figure`, `williamriveromd-simple-figure`
**Target GPT:** ChatGPT Image Generator — https://chatgpt.com/g/g-pmuQfob8d-image-generator

10 assets: 1 circular-vignette hero (patient), 1 OG share card, 8 in-body figures.
Every figure carries the `renalcarematters.com` attribution; every background is light;
all on-image type uses Inter / Nunito Sans / IBM Plex Sans / Manrope only. In-body
figures include a **suggested `<figcaption>`** (plain-language `fig-desc` + `fig-abbrevs`)
so the lightbox caption panel is populated per CLAUDE.md rule 11.

> **Placement note:** the guide currently ships without inline `<figure>` blocks
> (image pass was deferred per blueprint §A8). Insert each in-body figure into the
> section listed below, wrapped in `<figure> … <figcaption>` using the caption text
> provided, then run `patch_hero_fetchpriority.py` / `patch_hero_fullwidth.py` /
> `patch_hero_maxwidth.py` on the guide.

---

## 0 — CIRCULAR VIGNETTE HERO (patient)

```
FILE NAME: low-carb-diet-kidney-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: top-down (flat-lay), slight natural daylight rake
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: patients (mixed)
VISUAL GOAL: at a glance — a balanced Filipino plate (controlled rice, vegetables, fish) is the calm centre; the extreme all-meat keto option sits as a small, less inviting counterpoint, framing "balanced beats extreme."

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE
BORDER around the full circle (the circle must never touch the canvas edges). Composition
archetype: I Object Hero. Camera: top-down flat-lay with soft natural daylight.

Subject: one large, beautifully plated Filipino kidney-friendly meal as the dominant hero
object — a modest half-cup portion of steamed brown rice, grilled bangus (milkfish),
blanched pechay and kalabasa, a small kamote wedge, and a wedge of fresh papaya — arranged
on a clean matte off-white plate on a soft teal-tinted linen surface. As a smaller
supporting counterpoint set lower and to one side, a plain, austere little plate holding
only slabs of fatty meat and butter (the "keto extreme"), rendered deliberately less
appetizing and less lit. 2–4 quiet supporting props: a sprig of fresh herbs, a halved
calamansi, a simple water glass.

Visual hierarchy: the balanced plate occupies 60–70% of the circle; the austere meat plate
and small props 20–30%; reserve a clean 20–25% TITLE SAFE ZONE of empty soft teal-tinted
surface in the upper-left (no objects, food, icons, or labels inside that zone) so the HTML
title can sit beside the disc. Soft edge falloff toward a slightly deeper neutral at the rim.
Light, calm, appetizing-but-clinical colour grade harmonizing with clinical teal #1a6b72 and
renal green #1f7a4d on a bright background.

Absolutely NO readable text or labels on any object (no packaging copy), no titles, no logos,
no watermark. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny
unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped
circle, cropped objects, edge clipping, objects touching the circular border, important content
inside the title safe zone, baked-in text/titles/captions/logos/watermarks, rectangular
borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR,
over-saturation, distorted anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped.
ONE dominant hero object (the balanced plate) at 60–70%, 2–4 supporting elements, 20–25% empty
title-safe zone reserved (soft teal surface — no food, icons, or callouts inside). Filipino
food context. Crops cleanly inside the circle with no subject lost at the edges. No text.
```

---

## 1 — OG / SOCIAL SHARE CARD

```
FILE NAME: low-carb-diet-kidney-og.png
IMAGE TYPE: OG / social share card (baked title)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (fixed — never change)
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: a scroll-stopping share card that poses the guide's two questions — worth it? safe for kidneys? — over a balanced-plate vs keto motif.

PROMPT:
Open Graph social share card, 1200×630, premium nephrology education house style, off-white
(#fafafa) background. Left two-thirds: bold condensed sans-serif title in navy #0f1e2e set in
Inter — "Low-Carb & Keto: Fad, Fix, or Hazard?" — with a clinical-teal #1a6b72 subtitle beneath
in Inter — "A kidney doctor's honest guide". A slim renal-green #1f7a4d underline accent below
the title. Right third: a clean, bright, semi-photorealistic still-life split — the upper half a
balanced Filipino plate (controlled brown rice, grilled fish, vegetables), the lower half a small
austere all-meat/butter keto plate — separated by a soft dashed teal divider, gently implying
"balanced vs extreme". A tiny navy kidney glyph accent near the subtitle. Generous negative space,
strong hierarchy, mobile-legible. Bottom-right: "renalcarematters.com" in small semi-transparent
navy text (70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid
unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY
Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif, decorative, or handwritten fonts. Never
omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Mobile-readable title, calm publication-grade look, light background, teal/navy/
green accents only. renalcarematters.com visible bottom-right. Pair with og:image:width="1200"
og:image:height="630".
```

---

## 2 — CARBOHYDRATE-RESTRICTION SPECTRUM BAR

**Section:** Clinician → Definitions (`#md-definitions`) · Patient → What low-carb means (`#pt-what`)

```
FILE NAME: low-carb-diet-kidney-01-spectrum.png
IMAGE TYPE: Simple figure — horizontal spectrum bar (Scaffold C variant)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: show that "low-carb" is a spectrum, not one diet — from balanced to therapeutic keto — with the grams/day and where ketosis begins.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top center in bold navy
(#0f1e2e), Inter font: "Low-Carb Is a Spectrum, Not One Diet". A single wide horizontal gradient
band running left→right, cool renal-green #1f7a4d on the left shifting through teal #1a6b72 and amber
#b8860b to clinical-red #b91c1c on the right, sitting on a very soft gray panel (#f3f4f6). Five
evenly spaced rounded marker cards sit above/below the band, each with a bold sans-serif label and a
small grams-per-day chip:
  1. "Standard / Balanced" — 45–55% energy · ~225–275 g/day · no ketosis (green)
  2. "Moderate-carb" — 26–44% energy · ~130–225 g/day · no ketosis (teal)
  3. "Low-carb (LCD)" — <26% energy · <130 g/day · usually no ketosis (amber)
  4. "Very-low-carb / Keto (VLCKD)" — <10% energy · <50 g/day · nutritional ketosis (deep amber/red)
  5. "Therapeutic keto" — ~20–30 g/day · deep ketosis (red)
A slim dashed vertical "ketosis begins" marker crosses the band at the ~50 g/day point, labeled in
navy. Bottom strip on soft gray: brief navy summary — "The stricter the cut, the more it matters
whether the kidneys are healthy." Generous whitespace, mobile-readable ≥11pt labels, Inter
throughout. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid
overprocessed HDR, avoid excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light
only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit renalcarematters.com.

QUALITY CHECK:
Mobile-readable, five clean markers, one gradient band, a single "ketosis begins" divider, light
background, calm palette, attribution bottom-right.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">"Low-carb" is a sliding scale, not one diet — from a balanced 45–55% carbohydrate pattern, through moderate- and low-carb, to very-low-carb/ketogenic (under ~50 g/day, where the body enters ketosis) and therapeutic keto. The stricter the cut, the more kidney health matters.</p>
  <dl class="fig-abbrevs">
    <dt>LCD</dt><dd>Low-carbohydrate diet (usually &lt;130 g/day)</dd>
    <dt>VLCKD</dt><dd>Very-low-carbohydrate ketogenic diet (usually &lt;50 g/day)</dd>
  </dl>
</figcaption>
```

---

## 3 — KETOSIS / INSULIN MECHANISM (what carb restriction does)

**Section:** Clinician → Fad vs Physiology (`#md-fad`, Mechanism expander) · Patient → Is it a fad? (`#pt-fad`)

```
FILE NAME: low-carb-diet-kidney-02-ketosis-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (readable by patients)
VISUAL GOAL: the real short-term physiology of carbohydrate restriction — low insulin → hepatic ketogenesis, plus the early water-weight diuresis and satiety — shown honestly as a genuine lever, not magic.

PROMPT:
Create a publication-grade biomedical mechanism schematic, scientific review-article style, flat
vector illustration with soft semi-3D shading, white background, thin dashed connector boxes, muted
clinical palette (light gray-blue anatomy, soft yellow highlights, red for activating pathways, blue
for protective/metabolic effects), clean Inter sans-serif labels, generous whitespace.

Topic: What carbohydrate restriction physiologically does (short-term).
Left panel — organ-level context: a simplified human torso showing the LIVER (highlighted) with a
small stomach/gut and a kidney silhouette; label "Carbohydrate intake ↓ (<50–130 g/day)". A dashed
connector points to the magnified hepatocyte panel.
Center/right panel — magnified functional unit in a dashed box: a hepatocyte with mitochondria.
Concise callouts with arrows:
  • ↓ Postprandial glucose → ↓ Insulin
  • ↑ Hepatic β-oxidation
  • ↑ Ketogenesis → β-hydroxybutyrate, acetoacetate, acetone
A small secondary dashed inset: a kidney + glycogen icon labeled "Early natriuretic / glycogen-water
diuresis → 'week-one' weight is largely WATER".
Bottom summary flow (arrows left→right):
  Left pale-pink box — "Drivers": ↓ insulin, glycogen depletion, substrate switch to fat.
  Center pale-blue box — "Effects": nutritional ketosis (BHB 0.5–3 mmol/L); appetite suppression;
    improved insulin sensitivity.
  Right pale-blue box — "Honest framing": a real short-term metabolic lever — NOT permanent, universal,
    or risk-free.
White background, no photorealism, no dark theme, no decorative effects. Bottom-right: small
semi-transparent navy "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark/navy/black backgrounds, decorative effects, overcrowding, cartoonish styling,
gibberish text, invented numeric thresholds beyond those given. Use ONLY Inter/Nunito Sans/IBM Plex
Sans/Manrope. Keep © renalcarematters.com bottom-right.

QUALITY CHECK:
Organ panel → dashed hepatocyte inset → injury/effect/framing flow. Muted palette, legible labels,
water-weight point clearly shown, honest (non-hype) framing box. Attribution present.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">Cutting carbohydrate lowers insulin, shifts the liver to burning fat, and makes ketones — a real short-term effect. It also flushes out stored carbohydrate and its attached water, which is why the dramatic first-week weight drop is mostly water, not fat.</p>
  <dl class="fig-abbrevs">
    <dt>BHB</dt><dd>β-hydroxybutyrate — the main ketone body measured in nutritional ketosis</dd>
  </dl>
</figcaption>
```

---

## 4 — U-SHAPED CARBOHYDRATE–MORTALITY CURVE

**Section:** Clinician → The Honest Ledger (`#md-ledger`, mortality) · Patient → Does it work? (`#pt-works`)

```
FILE NAME: low-carb-diet-kidney-03-u-curve.png
IMAGE TYPE: Simple figure — single data chart / one-panel poster (Scaffold D variant)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: mortality is lowest in the middle (~50–55% carbohydrate) and rises at both extremes — and the direction depends on what replaces the carbs (animal worse, plant better).

PROMPT:
Medical education chart infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background.
Title at top in bold navy (#0f1e2e), Inter: "Carbohydrate Intake & Mortality: A U-Shaped Curve".
Subtitle in clinical teal (#1a6b72), Inter: "Observational (ARIC + meta-analysis, n≈432,000)". Central
clean line chart on a soft gray plot area: X-axis "% of energy from carbohydrate" (low → high),
Y-axis "relative mortality risk". A smooth symmetric U-shaped curve with its lowest point highlighted
by a renal-green #1f7a4d marker and callout chip "Lowest risk ≈ 50–55%". Both tails rise; the left
(very-low-carb) and right (very-high-carb) ends flagged in amber #b8860b. Two small annotation cards to
the side: a red-accent card "Replace carbs with ANIMAL fat/protein → higher mortality (↑)" and a
green-accent card "Replace carbs with PLANT fat/protein → lower mortality (↓)". A slim italic navy
footnote: "Observational and confounded — direction consistent: what you replace carbs with is the
outcome-defining variable." Generous whitespace, mobile-readable, Inter throughout. Bottom-right:
"renalcarematters.com" small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, fabricated precise numbers
beyond those given, overprocessed HDR, excessive saturation. NEVER dark/navy/charcoal/black backgrounds.
Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope. Never omit renalcarematters.com.

QUALITY CHECK:
One clean U-curve, green nadir at ~50–55%, amber tails, two substitution annotation cards, light
background, legible axes, attribution bottom-right.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">Across large observational studies, deaths were lowest for people eating a middling amount of carbohydrate (about 50–55% of calories) and higher at both extremes. What you swap the carbohydrate for matters: replacing it with animal fat and protein tracked with higher mortality, while plant sources tracked with lower mortality.</p>
  <dl class="fig-abbrevs">
    <dt>ARIC</dt><dd>Atherosclerosis Risk in Communities — the large U.S. cohort study</dd>
  </dl>
</figcaption>
```

---

## 5 — PROTEIN → GLOMERULAR HYPERFILTRATION → PROGRESSION

**Section:** Clinician → Protein Hazard (`#md-protein`, Mechanism) · Patient → If you have CKD (`#pt-kidney`)

```
FILE NAME: low-carb-diet-kidney-04-hyperfiltration.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (readable by patients)
VISUAL GOAL: high protein raises single-nephron pressure — adaptive briefly, damaging when sustained on a reduced-nephron kidney — the core CKD hazard of most low-carb execution.

PROMPT:
Create a publication-grade biomedical mechanism schematic, scientific review-article style, flat vector
illustration with soft semi-3D shading, white background, thin dashed connector boxes, muted clinical
palette (light gray-blue anatomy, soft yellow highlighted segments, red for arteries/injury, blue for
protective effects), clean Inter sans-serif labels.

Topic: High dietary protein and glomerular hyperfiltration in CKD.
Left panel — organ-level context: a simplified kidney cross-section labeled "Reduced nephron mass (CKD)",
with fewer functioning nephrons drawn; a dashed connector box points to the magnified glomerulus.
Center/right panel — magnified GLOMERULUS inside a dashed box: afferent and efferent arterioles, capillary
tuft, Bowman's capsule. Highlight the AFFERENT arteriole dilated (red). Concise callouts with arrows:
  • High protein load → afferent arteriolar VASODILATION
  • ↑ Single-nephron GFR · ↑ intraglomerular pressure
  • ↑ Albuminuria (protein leaking into Bowman's space, small yellow dots)
A small secondary dashed inset showing progressive glomerulosclerosis (scarred tuft).
Bottom summary flow (arrows left→right):
  Left pale-pink box — "Driver": sustained high protein 1.2–2.0+ g/kg/day (typical keto/low-carb).
  Center box — "Mechanism": glomerular hyperfiltration & intraglomerular hypertension.
  Right pale-pink box — "Outcome": faster eGFR decline, albuminuria, glomerulosclerosis → progression.
A slim navy note bar: "Guideline ceiling in CKD 3–5 ND: 0.55–0.8 g/kg/day — the opposite direction."
White background, no photorealism, no dark theme, no decorative effects, generous whitespace. Bottom-right:
small semi-transparent navy "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark/navy/black backgrounds, decorative effects, overcrowding, cartoonish styling,
gibberish text, invented numeric thresholds beyond those given. Anatomy must be plausible (afferent vs
efferent arteriole correct). Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope. Keep © renalcarematters.com.

QUALITY CHECK:
Kidney panel → dashed glomerulus inset (afferent dilation highlighted) → driver/mechanism/outcome flow.
Guideline-ceiling note present. Muted palette, legible labels, attribution present.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">A high-protein diet makes each surviving nephron work at higher pressure. On a healthy kidney that is a brief, harmless adjustment; on a kidney with reduced nephron mass it drives protein leak, scarring, and faster loss of function — which is why guidelines lower protein in CKD, the opposite of most low-carb diets.</p>
  <dl class="fig-abbrevs">
    <dt>GFR</dt><dd>Glomerular filtration rate — the measure of kidney filtering capacity</dd>
    <dt>ND</dt><dd>Non-dialysis (CKD not yet on dialysis)</dd>
  </dl>
</figcaption>
```

---

## 6 — DIETARY-ACID-LOAD FOOD MAP

**Section:** Clinician → Fat / Acid / Minerals (`#md-fat-acid`) · Patient → If you have CKD (`#pt-kidney`)

```
FILE NAME: low-carb-diet-kidney-05-acid-load.png
IMAGE TYPE: Food matrix / nutrition infographic
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: mixed
VISUAL GOAL: animal protein raises dietary acid; fruits and vegetables are the natural base — and keto's removal of produce strips out the diet's main alkali source.

PROMPT:
CKD nutrition infographic, clean educational food matrix, white (#ffffff) background. Title at top in
bold navy (#0f1e2e), Inter: "Dietary Acid Load in CKD: Meat vs Produce". A soft dashed vertical divider
splits the canvas into two panels. LEFT panel header in clinical red (#b91c1c), Inter: "Acid-forming —
higher net acid": realistic clean renderings of pork, beef, chicken, eggs, cheese, and processed meats,
each on a small rounded card, with a small caption "sulfur-containing amino acids → net endogenous acid".
RIGHT panel header in renal green (#1f7a4d): "Base-forming — the natural antidote": realistic fresh
fruits and vegetables relevant to Filipino diets — kangkong, pechay, kalabasa, banana, papaya, kamote —
on rounded cards, caption "fruits & vegetables → base, buffer acid". A center vertical gauge/arrow
tinted red at top → green at bottom labeled "net acid load". A bottom full-width soft-gray strip with a
navy take-home in Inter: "As GFR falls, acid excretion falls too — a meat-heavy, low-produce (keto) plate
raises acid exactly when the kidney can least handle it. Base-producing fruits & vegetables slow
progression." Realistic food rendering, rounded category cards, mobile-readable ≥11pt, Inter throughout.
Bottom-right: "renalcarematters.com" small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic food, overprocessed
HDR, excessive saturation. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito
Sans/IBM Plex Sans/Manrope. Never omit renalcarematters.com.

QUALITY CHECK:
Two clean panels (red acid / green base), Filipino-relevant produce, a net-acid gauge, a take-home strip,
light background, mobile-readable, attribution bottom-right.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">Animal protein leaves behind acid the body must excrete; fruits and vegetables are base-forming and buffer it. As kidney function falls, acid clears more slowly — so a meat-heavy, low-produce keto plate raises acid load just when the kidney can least handle it, while produce (or bicarbonate) helps slow decline.</p>
  <dl class="fig-abbrevs">
    <dt>GFR</dt><dd>Glomerular filtration rate — the measure of kidney function</dd>
  </dl>
</figcaption>
```

---

## 7 — EUGLYCEMIC-DKA DANGER TRIAD (keto + SGLT2i)

**Section:** Clinician → Special Situations 10.1 (`#md-special`) · Patient → If you have CKD (`#pt-kidney`)

```
FILE NAME: low-carb-diet-kidney-06-eudka-triad.png
IMAGE TYPE: Simple figure — mechanism/warning triad (Scaffold D variant)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (safety-critical)
VISUAL GOAL: SGLT2 inhibitor + ketogenic/very-low-carb diet + a trigger (fasting, illness) can cause dangerous ketoacidosis at NORMAL blood sugar — easily missed.

PROMPT:
Medical safety infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background. Title at top
in bold navy (#0f1e2e), Inter: "Euglycemic DKA: The Silent Danger of Keto + SGLT2 Inhibitors". Three
overlapping rounded circles (a clean Venn) in the upper two-thirds, each a distinct restrained tint:
  • Teal circle: "SGLT2 inhibitor (empagliflozin / dapagliflozin) → promotes ketogenesis"
  • Amber circle: "Very-low-carb / ketogenic diet → high ketones"
  • Red circle: "Trigger: fasting, illness, alcohol, surgery"
Their central overlap glows red and is labeled boldly "Euglycemic DKA". Below, a slim horizontal alert
band split in two: left renal-green chip "Glucose: NORMAL / near-normal" and right clinical-red chip
"Ketones/acid: DANGEROUSLY HIGH", joined by a navy "→ easily missed" note. A bottom soft-gray strip with
a navy clinical rule in Inter: "Do NOT combine keto/very-low-carb with an SGLT2 inhibitor. Teach sick-day
rules — hold the SGLT2i during illness, fasting, or before surgery; check ketones with symptoms even if
glucose is normal." Generous whitespace, mobile-readable, Inter throughout. Bottom-right:
"renalcarematters.com" small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive
saturation. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex
Sans/Manrope. Never omit renalcarematters.com.

QUALITY CHECK:
Clean three-circle Venn with a red central "Euglycemic DKA", the normal-glucose / high-ketones contrast
band, and the sick-day clinical rule. Light background, mobile-readable, attribution bottom-right.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">SGLT2 inhibitors already nudge the body toward making ketones. Add a ketogenic/very-low-carb diet and a trigger like fasting or illness, and a patient can develop dangerous ketoacidosis while their blood sugar still looks normal — so it is easily missed. The rule: don't combine keto with an SGLT2 inhibitor, and learn sick-day rules.</p>
  <dl class="fig-abbrevs">
    <dt>DKA</dt><dd>Diabetic ketoacidosis; "euglycemic" means it happens at normal blood sugar</dd>
    <dt>SGLT2i</dt><dd>Sodium-glucose co-transporter-2 inhibitor (empagliflozin, dapagliflozin)</dd>
  </dl>
</figcaption>
```

---

## 8 — ADPKD: "CYSTS DISLIKE KETOSIS" (investigational)

**Section:** Clinician → Special Situations 10.2 (`#md-special`) · Patient → If you have CKD (`#pt-kidney`)

```
FILE NAME: low-carb-diet-kidney-07-adpkd-keto.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style, EXPERIMENTAL-flagged)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (readable by patients)
VISUAL GOAL: the promising, mechanistically distinct exception — cyst epithelium is metabolically inflexible and disfavored by ketosis — framed clearly as INVESTIGATIONAL, specialist-supervised.

PROMPT:
Create a publication-grade biomedical mechanism schematic, scientific review-article style, flat vector
illustration with soft semi-3D shading, white background, thin dashed connector boxes, muted clinical
palette (light gray-blue anatomy, soft yellow highlights, blue for protective/therapeutic effects), clean
Inter sans-serif labels. Add a small amber "EXPERIMENTAL / INVESTIGATIONAL" ribbon-tag near the title.

Topic: Ketogenic metabolic therapy in ADPKD (proposed mechanism).
Left panel — organ-level context: a simplified polycystic kidney with multiple cysts, labeled "ADPKD".
A dashed connector box points to the magnified cyst-lining cell.
Center/right panel — magnified CYST EPITHELIAL CELL inside a dashed box, with mitochondria. Concise
callouts with arrows:
  • Cyst epithelium relies on glucose/glycolysis — "metabolically inflexible"
  • Ketosis (β-hydroxybutyrate) ↓ available glucose substrate
  • Proposed: ↓ cyst cell proliferation
Bottom summary flow (arrows left→right):
  Left box — "Preclinical (Weimbs lab)": cyst growth disfavored by ketosis (animal models).
  Center pale-blue box — "Human studies": RESET-PKD (pilot) & KETO-ADPKD (RCT) — feasible, well-tolerated,
    potent ketosis; liver volume responded, kidney-volume signal early.
  Right pale-blue box — "Status": PROPOSED / INVESTIGATIONAL — specialist-supervised only; not a general
    endorsement of keto in CKD.
White background, no photorealism, no dark theme, generous whitespace. Bottom-right: small semi-transparent
navy "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark/navy/black backgrounds, decorative effects, overcrowding, cartoonish styling,
gibberish text, invented numbers. Must visibly flag the therapy as experimental/investigational (do not
imply routine clinical care). Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope. Keep © renalcarematters.com.

QUALITY CHECK:
Polycystic-kidney panel → dashed cyst-cell inset → preclinical/human/status flow, with a clear
EXPERIMENTAL tag and a "not a general keto endorsement" caveat. Muted palette, legible, attribution present.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">In polycystic kidney disease, the cells lining the cysts lean heavily on glucose and appear "metabolically inflexible," so ketosis may disfavour their growth. Early human trials (RESET-PKD, KETO-ADPKD) found supervised ketogenic therapy feasible and well-tolerated — but this is investigational, specialist-only, and not a general endorsement of keto in kidney disease.</p>
  <dl class="fig-abbrevs">
    <dt>ADPKD</dt><dd>Autosomal dominant polycystic kidney disease</dd>
    <dt>RCT</dt><dd>Randomized controlled trial</dd>
  </dl>
</figcaption>
```

---

## 9 — BALANCED FILIPINO PLATE MODEL (the durable default)

**Section:** Patient → Can you keep it up? (`#pt-sustain`) · Clinician → Verdict (`#md-verdict`)

```
FILE NAME: low-carb-diet-kidney-08-balanced-plate.png
IMAGE TYPE: Food matrix / plate-model infographic
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients (mixed)
VISUAL GOAL: the doable, sustainable default — a balanced, plant-forward Filipino plate with controlled rice, vegetables and protein first — beats a perfect keto diet you quit.

PROMPT:
CKD/nutrition plate-model infographic, clean educational design, white (#ffffff) background. Title at top
in bold navy (#0f1e2e), Inter: "The Balanced Filipino Plate — the Diet You Can Keep". Center: a large
top-down semi-photorealistic dinner plate divided into clear portions with thin navy rules:
  • Half the plate — non-starchy vegetables (kangkong, pechay, kalabasa, sitaw), labeled green #1f7a4d
    "½ plate: vegetables — fill up first".
  • One quarter — lean protein (grilled bangus/tilapia, tofu, small chicken portion), labeled teal
    #1a6b72 "¼ plate: protein — appropriate amount".
  • One quarter — a controlled portion of rice, ideally brown/lower-GI, labeled amber #b8860b
    "¼ plate: rice — halve it, upgrade quality".
Three small supporting tip cards around the plate: "Vegetables & protein BEFORE rice (meal sequencing)",
"Cut sugary drinks & refined snacks", "Water or calamansi, not soda". A bottom soft-gray strip with a navy
take-home in Inter: "Moderate-carb, plant-forward, protein-appropriate — a balanced plate with controlled
rice beats a perfect keto diet you quit in two months." Realistic appetizing-but-clinical food rendering,
rounded cards, mobile-readable ≥11pt, Inter throughout. Bottom-right: "renalcarematters.com" small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic food, overprocessed
HDR, excessive saturation. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito
Sans/IBM Plex Sans/Manrope. Never omit renalcarematters.com.

QUALITY CHECK:
Clear ½ vegetables / ¼ protein / ¼ controlled rice plate model, Filipino foods, three tip cards, take-home
strip, light background, mobile-readable, attribution bottom-right.
```

**Suggested `<figcaption>`:**
```html
<figcaption>
  <p class="fig-desc">The sustainable default: fill half the plate with vegetables, a quarter with an appropriate amount of protein, and a quarter with a controlled portion of (ideally brown or lower-GI) rice — vegetables and protein before the rice. A balanced, plant-forward plate you can keep beats a perfect keto diet you quit.</p>
  <dl class="fig-abbrevs">
    <dt>GI</dt><dd>Glycemic index — how quickly a food raises blood sugar</dd>
  </dl>
</figcaption>
```

---

## Build checklist (Stage 2)

- [ ] Generate all 10 assets in the ChatGPT Image Generator GPT (paste each PROMPT block).
- [ ] Save each as `images/<file-name>.png` **and** a WebP twin `images/<file-name>.webp`.
- [ ] Hero + OG already wired in the guide `<head>` / hero (paths match these filenames).
- [ ] Insert figures 2–9 into their sections wrapped in `<figure><picture>… <figcaption>…</figcaption></figure>` using the suggested captions above.
- [ ] Run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, then `patch_image_lightbox.py` on the guide.
- [ ] Optionally append `og:image:alt` / dimensions via `williamriveromd-local-image-generator`.
- [ ] Re-check WCAG contrast of any on-image text remains ≥ 4.5:1 (all captions are dark-on-light).
