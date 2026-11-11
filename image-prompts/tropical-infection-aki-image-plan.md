# Image Plan — `tropical-infection-aki.html`
### Fever and Kidney Injury in the Tropics: Scrub Typhus, Malaria, Leptospirosis and Dengue · renalcarematters.com

**Stage 1 prompt pack.** Each prompt was written with the matching house skill (`williamriveromd-hero-vignette`, `williamriveromd-infographic-skill`, `williamriveromd-simple-figure`, `williamriveromd-algorithm-generator-skill`, `williamriveromd-biomedical-mechanism-figure`, `williamriveromd-organ-crosstalk-sigil-graphic`) and is ready to paste into the [ChatGPT Image Generator GPT](https://chatgpt.com/). Generate at the stated size, save the PNG and a `.webp` twin to `images/`, then run Stage 2 (`williamriveromd-local-image-generator`) for manifests if wanted.

It replaces the earlier six-prompt pack and keeps the same six file names, so nothing in the HTML changes for those, and adds eleven new figures.

---

## 1. Design intent: one guide, readers of every educational level

The guide serves a farmer in Tarlac, a caregiver in Quezon City, a nursing student, and a nephrologist. The images are planned so that each reader gets the core message even if they read nothing else.

| Principle | How it shows up in the prompts |
|---|---|
| **Picture first, words second** | Patient figures carry their meaning in icons, scenes, and color, with labels of 6 words or fewer. A reader with limited English, or reading the Tagalog, Cebuano, or Kapampangan text, still understands the image. |
| **One idea per image** | Each figure answers one question ("How do I catch it?", "Where is the scab?", "What color is dangerous urine?"). No figure tries to teach two things. |
| **Never color alone** | Every color code is doubled with an icon, shape, or word, for color-blind readers and for black-and-white printing in clinics. |
| **Filipino and local** | Rice paddies, cogon grass, flooded barangay streets, Palawan forest, the barangay health worker, the salakot. People are varied (age, sex, build, skin tone, clothing), never a reused stock face. |
| **Escalating depth** | Patient tab: scenes and pictograms. Clinician tab: mechanism schematics, comparison card, algorithm. The comparison and algorithm also print well as ward posters. |
| **Clinical honesty in pictures** | Figures that show the acetaminophen adjunct label it "phase 2 evidence"; the eschar figure says "No scab? Still possible"; the malaria map is schematic, not cartographic. |
| **Data charts are built in HTML, not by AI** | Image models misdraw bar heights and numbers. The INTREST result and the pooled-AKI frequencies are better as inline SVG charts in the page (see §5), so they stay exact and translatable. |

### Language strategy
Patient figures use minimal English labels that are also common in Filipino clinical speech (e.g., "Dialysis", "Doxycycline"). The full four-language explanation lives in each `<figcaption class="fig-desc">`. If you later want fully localized versions, the label lists in each prompt are short enough to regenerate per language; add `-tl`, `-ceb`, `-kap` suffixes.

### House rules applied to every prompt
- **Light background only** (white, `#fafafa`, `#f3f4f6`, `#eef6f7`). Navy `#0f1e2e` and teal `#1a6b72` are type and accents, never fills.
- **Approved fonts only:** Inter, Nunito Sans, IBM Plex Sans, or Manrope. The font is named in each prompt.
- **Attribution on every figure except the hero vignette:** small semi-transparent `renalcarematters.com` (algorithm and mechanism skills use `© renalcarematters.com`), bottom-right; bottom-center on portrait.
- **Infection color key, used consistently across all figures:** Leptospirosis amber `#b8860b` (water drop icon), Dengue red `#b91c1c` (day mosquito), Scrub typhus green `#1f7a4d` (mite), Malaria purple `#6c3d8e` (night mosquito with moon). Kidney and clinical structure stay navy and teal.

---

## 2. Plan overview

| # | Placement (section anchor) | File (PNG + WebP twin) | Skill | What it teaches | Size | Priority | HTML slot |
|---|---|---|---|---|---|---|---|
| H | Hero vignette | `tropical-infection-aki-vignette-hero.png` | hero-vignette | Fever after field work deserves attention | 2048 × 2048 | **Core** | Wired |
| OG | `og:image` | `tropical-infection-aki-og.png` | infographic | Share card | 1200 × 630 | **Core** | Wired |
| 02 | `#fever-kidneys` | `tropical-infection-aki-02-four-mechanisms.png` | simple-figure | Four ways fever hurts the kidney | 1792 × 1024 | **Core** | Wired |
| 03 | `#scrub-typhus` | `tropical-infection-aki-03-eschar-sites.png` | simple-figure | Where to search for the eschar | 1024 × 1536 | **Core** | Wired |
| 04 | `#md-comparison` | `tropical-infection-aki-04-comparison.png` | infographic (reference card) | Four infections compared | 1792 × 1024 | **Core** | Wired |
| 05 | `#md-approach` | `tropical-infection-aki-05-first-24h-algorithm.png` | algorithm-generator (Mode C) | First-24-hour pathway | 1024 × 1536 | **Core** | Wired |
| 06 | `#four-infections` (top) | `tropical-infection-aki-06-how-you-catch-it.png` | infographic (multi-panel) | Four everyday exposure scenes | 1792 × 1024 | **Core** | Wired |
| 07 | `#tr-urgent` (after alert) | `tropical-infection-aki-07-warning-signs.png` | simple-figure (reference card) | Six go-to-hospital-today signs | 1024 × 1024 | **Core** | Wired |
| 08 | `#fever-kidneys` (after list) | `tropical-infection-aki-08-urine-color-guide.png` | simple-figure (comparison) | What urine color and amount mean | 1792 × 1024 | **Core** | Wired |
| 09 | `#scrub-typhus` (before eschar) | `tropical-infection-aki-09-chigger-to-fever.png` | simple-figure (step sequence) | How a chigger bite becomes fever | 1792 × 1024 | Recommended | Wired |
| 10 | `#malaria` (top) | `tropical-infection-aki-10-malaria-where-now.png` | simple-figure (schematic map) | Malaria now is mostly southern Palawan or travel | 1024 × 1024 | Recommended | Wired |
| 11 | `#malaria` (after first paragraph) | `tropical-infection-aki-11-knowlesi-sigil.png` | organ-crosstalk sigil | Monkey → mosquito → human | 1024 × 1024 | Optional | Wired |
| 12 | `#prevention` | `tropical-infection-aki-12-prevention-card.png` | infographic (multi-panel) | One protective action per infection | 1792 × 1024 | **Core** | Wired |
| 13 | `#recovery` | `tropical-infection-aki-13-recovery-timeline.png` | simple-figure (step sequence) | Follow-up from discharge to 3 months | 1792 × 1024 | Recommended | Wired |
| 14 | `#md-scrub-typhus` (pathophysiology) | `tropical-infection-aki-14-scrub-typhus-mechanism.png` | biomedical-mechanism | Endothelial infection → kidney injury → treatment | 1792 × 1024 | **Core** | Wired |
| 15 | `#md-scrub-typhus` (INTREST para) | `tropical-infection-aki-15-scrub-multiorgan-sigil.png` | organ-crosstalk sigil | One vasculitis, five organs | 1024 × 1024 | Optional | Wired |
| 16 | `#md-malaria` (mechanisms) | `tropical-infection-aki-16-malaria-aki-mechanism.png` | biomedical-mechanism | Sequestration and cell-free hemoglobin → ATN | 1792 × 1024 | **Core** | Wired |
| 17 | `#md-krt` | `tropical-infection-aki-17-krt-modality.png` | simple-figure (comparison) | Blood-based therapy vs acute PD | 1792 × 1024 | Recommended | Wired |

**Production order (biggest gain for least effort):** H → 07 → 06 → 08 → 03 → 02 → 12 → 05 → 04 → 16 → 14 → OG → 13 → 10 → 09 → 17 → 11 → 15.

**All 18 slots are already wired in the guide** with plain-language captions (four languages in the patient tab). Each `<img>` carries an `onerror` hook that hides its whole `<figure>` until the file exists, so missing images never show as broken boxes. Uploading `images/<file>.png` + `.webp` makes each figure appear automatically, with no HTML edit.

---

## 3. Patient-tab images

### H — Hero vignette (`williamriveromd-hero-vignette`)

```
FILE NAME: tropical-infection-aki-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: D Panorama — landscape dominates, one primary focal point
CAMERA: Wide-angle environmental scene from a slightly low rear three-quarter angle
HUMAN VARIATION (vs. previous guide, AL amyloidosis): rural outdoor setting instead of a clinic interior; male farmer in his early 50s; lean, wiry build; deeply sun-tanned brown skin; short gray-streaked crew cut; angular face with prominent cheekbones; faded salakot resting on his knee; sweat-damp long-sleeved olive work shirt; rolled trousers and rubber boots; seated on a bamboo bench; tired, feverish half-closed eyes; rear three-quarter wide framing; a young female barangay health worker (late 20s, hair in a low bun, rounded face, light-blue polo uniform) kneeling to check his temperature
AUDIENCE: patients and families
VISUAL GOAL: A feverish Filipino farmer being checked at the edge of the rice fields says "fever after field work deserves attention" at a glance.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: D Panorama. Camera: wide-angle environmental view from a slightly low rear three-quarter angle.

Subject: a lean, wiry Filipino farmer in his early 50s with deeply sun-tanned brown skin, a short gray-streaked crew cut, and angular cheekbones sits on a bamboo bench under a simple nipa-roofed shade hut at the edge of green rice paddies. He wears a sweat-damp long-sleeved olive work shirt, rolled trousers, and muddy rubber boots; a faded salakot rests on his knee. He looks tired and feverish, eyes half-closed, one hand resting on his forehead. Kneeling beside him, a young female barangay health worker in a light-blue polo uniform holds a digital thermometer near his temple, her expression attentive and calm. Behind them, rice paddies give way to tall cogon grass and bushy field edges, with distant hills under a soft, hazy late-morning sky.

Visual hierarchy: the farmer and health worker together occupy 60–70% of the circle in the lower and right portions; the paddies and grassland edge give 20–30% supporting context; reserve a 20–25% TITLE SAFE ZONE of open, softly blurred sky across the upper-left of the circle (no faces, objects, or details there).

Calm, reassuring, documentary-realistic color grade with soft natural daylight and gentle shallow depth of field; greens of the paddies harmonize with clinical teal #1a6b72 and navy #0f1e2e accents. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark or black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces. No visible skin lesions, blood, needles, or distress imagery.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped. One dominant scene, 20–25% empty sky as title-safe zone. Filipino rural context. Crops cleanly inside the circle with no text.
```

### 07 — Six warning signs (`williamriveromd-simple-figure`, Scaffold E)

```
FILE NAME: tropical-infection-aki-07-warning-signs.png
IMAGE TYPE: Scaffold E — square quick-look pictogram card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and families, including low-literacy readers
VISUAL GOAL: Six pictures a person can recognize without reading, each meaning "go to the hospital today."

PROMPT:
Clinical patient-safety pictogram card, white (#ffffff) background, font Nunito Sans. Bold navy (#0f1e2e) title at top: "Fever + Any of These = Hospital Today". A thin clinical red (#b91c1c) rule under the title. A 2 × 3 grid of six rounded cards on soft gray (#f3f4f6), each with one large, simple, friendly flat-line pictogram in navy with a single red accent, and a short label of at most four words beneath it:
1. A nearly empty urine cup with a small clock showing 12 hours — "Little or no urine"
2. A person's head with a swirl above it — "Confused or very sleepy"
3. A person holding the chest with short breath lines — "Hard to breathe"
4. A tooth-and-gum outline with a red drop — "Bleeding gums, nose, stool"
5. An eye with a yellow sclera beside a cup of cola-colored urine — "Yellow eyes, dark urine"
6. A small round black scab with a red rim on skin, plus a thermometer — "Black scab + high fever"
Each pictogram is drawn so its meaning is clear even with the label covered. Bottom band in pale red (#fdecec) with a navy hospital-cross icon and the words "Do not wait for the fever to break." Generous spacing, labels at least 14 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No photographs of real wounds or blood, no gore, no frightening faces. Avoid cartoon mascots, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Every pictogram understandable without its label; labels four words or fewer; readable on a phone; white background; attribution bottom-right.
```

### 06 — How you catch each infection (`williamriveromd-infographic-skill`, multi-panel)

```
FILE NAME: tropical-infection-aki-06-how-you-catch-it.png
IMAGE TYPE: Multi-panel educational infographic (4 photographic scenes)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Four everyday Filipino scenes let readers recognize their own exposure.
VISUAL MIX:
- photorealistic models: four small Filipino scenes, different people in each
- 2D infographic: colored header bands with icons, one-line captions
- 3D component graphics: none
- algorithm/flowchart: none

PROMPT:
Patient education infographic, landscape 16:9, white (#ffffff) background, font Inter. Title at top center in bold navy (#0f1e2e): "Four Infections, Four Ways In". Four equal rounded photo cards in a single row, each with a colored header band, a simple line icon, the infection name, and one caption line of at most seven words beneath the photo:
1. Amber (#b8860b) band, water-drop icon, "Leptospirosis": photorealistic scene of a teenage boy and his mother wading knee-deep through brown floodwater on a flooded barangay street after a typhoon, rubber slippers visible, overcast but bright light. Caption: "Floodwater, mud, and rice fields".
2. Red (#b91c1c) band, daytime-mosquito icon with a small sun, "Dengue": a bright urban home scene with a water drum and flower-pot saucer holding still water, a small Aedes mosquito with striped legs resting on the rim, a young girl doing homework in soft daylight in the background. Caption: "Daytime mosquitoes, standing water at home".
3. Green (#1f7a4d) band, tiny-mite icon, "Scrub typhus": a middle-aged woman farmer in a wide-brim hat and short sleeves cutting cogon grass at a field edge, sitting briefly on the grass, sunny afternoon. Caption: "Tall grass, bushes, farm edges".
4. Purple (#6c3d8e) band, night-mosquito icon with a small moon, "Malaria": a young man in his twenties at dusk setting up a hammock beside a forest trail in the foothills of southern Palawan, a mosquito net folded beside him. Caption: "Night bites, Palawan forests, or travel".
Below the row, a full-width soft gray (#f3f4f6) strip with a navy speech-bubble icon: "Tell your doctor where you have been." Each person is visibly different in age, sex, build, and clothing. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, no rats shown close-up, no dead animals, no injuries. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Four distinct, recognizable Filipino scenes; four different people; captions seven words or fewer; consistent infection color key; white background; attribution bottom-right.
```

### 08 — Urine color and amount guide (`williamriveromd-simple-figure`, Scaffold B variant)

```
FILE NAME: tropical-infection-aki-08-urine-color-guide.png
IMAGE TYPE: Scaffold B — comparison strip (five-step color scale)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Let anyone match their urine to a picture and know when to worry.

PROMPT:
Medical education comparison infographic, white (#ffffff) background, font Nunito Sans. Bold navy title at top: "What Your Urine Is Telling You During a Fever". Five identical clear plastic specimen cups in a horizontal row on a soft gray (#f3f4f6) shelf, each filled to a different level and color, with a short label and a small status icon below:
1. Pale straw, cup two-thirds full — green check icon (#1f7a4d) — "Normal".
2. Dark yellow, cup half full — amber drop icon (#b8860b) — "Drink fluids, watch".
3. Tea-brown, cup half full — red alert icon (#b91c1c) — "Muscle or blood damage: hospital".
4. Cola or black, cup one-third full — red alert icon — "Hospital today".
5. Nearly empty cup with only a few drops and a small clock showing 12 hours — red alert icon — "Very little urine: hospital today".
Above cups 3 to 5, a thin red bracket labeled "Danger zone". Bottom strip in navy text: "Amount matters as much as color. Some kidney injuries still make normal amounts of urine, so blood tests are needed too." Each status uses BOTH an icon shape and a color, never color alone. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No real bodily fluids photographed in a clinical toilet or unpleasant setting; keep the cups clean and clinical. Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, oversaturated colors that distort the urine shades. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Five shades clearly distinguishable, including for color-blind readers (icons differ); labels short; white background; attribution bottom-right.
```

### 02 — Four ways a fever infection hurts the kidney (`williamriveromd-simple-figure`, Scaffold C)

```
FILE NAME: tropical-infection-aki-02-four-mechanisms.png
IMAGE TYPE: Scaffold C — four converging causes
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Show in one glance the four overlapping ways a fever infection injures the kidney.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, font Inter. Title at top center in bold navy (#0f1e2e): "How a Fever Infection Hurts the Kidneys". Subtitle in clinical teal (#1a6b72): "Most patients have more than one at the same time". Four rounded cards in a single horizontal row on a very soft gray panel (#f3f4f6), each with a colored top accent band, one large simple line icon, a bold label, and two short lines:
1. Amber (#b8860b), icon of a water droplet shrinking with a downward arrow: "Not enough fluid" — "Fever, sweating, vomiting" / "Leaky blood vessels".
2. Red (#b91c1c), icon of a blood-pressure gauge pointing low: "Low blood pressure" — "Kidney loses blood flow first" / "Tube cells injured".
3. Purple (#6c3d8e), icon of a muscle fiber beside a burst red blood cell: "Pigments" — "Muscle breakdown" / "Burst red cells in malaria".
4. Teal (#1a6b72), icon of a kidney with small flame-like inflammation marks: "Inflammation inside" — "Germ or immune attack" / "Can continue after BP recovers".
Four thin navy arrows converge from the cards down to a single simple semi-photoreal kidney at bottom center labeled "Acute kidney injury (AKI)". Bottom strip, full width, soft gray: "Treat the germ, manage fluids carefully, and check the kidneys every day." Generous whitespace, labels at least 12 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable, four distinct icons, calm, white background, attribution bottom-right.
```

### 09 — From chigger bite to fever (`williamriveromd-simple-figure`, Scaffold C)

```
FILE NAME: tropical-infection-aki-09-chigger-to-fever.png
IMAGE TYPE: Scaffold C — horizontal four-step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Make an invisible bite understandable: tiny chigger, painless bite, scab, fever about 1 to 2 weeks later.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, font Manrope. Title at top center in bold navy: "How Scrub Typhus Starts". Four rounded cards in a row on soft gray (#f3f4f6), connected by bold navy right-pointing arrows, each with a renal green (#1f7a4d) top band:
1. "Chigger waits on grass" — a magnified, scientifically plausible illustration of an orange-red six-legged trombiculid mite larva on the tip of a grass blade, with a small scale bar labeled "smaller than a pinhead".
2. "Painless bite" — illustrated close-up of a waistband line on skin with a tiny dot, small text "Usually not felt".
3. "Black scab forms" — illustrated round black eschar with a red rim, about the size of a pencil eraser, small text "In a skin fold".
4. "Fever and headache" — simple illustrated person resting with a thermometer, small text "About 1 to 2 weeks after the bite".
Under the row, a teal (#1a6b72) banner with a capsule icon: "Doxycycline works fast when started early." Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Do not draw a tick, spider, or flea; the larva has six legs and is round-bodied. No gore, no nudity. Avoid cartoon mascots, clutter, tiny unreadable labels, AI gibberish text, HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mite anatomy plausible (six legs), four clear steps, short labels, white background, attribution bottom-right.
```

### 03 — Where to look for an eschar (`williamriveromd-simple-figure`, Scaffold D)

```
FILE NAME: tropical-infection-aki-03-eschar-sites.png
IMAGE TYPE: Scaffold D — single-panel illustrated body map (portrait)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: patients and families
VISUAL GOAL: Show where the painless scrub typhus scab hides so patients and families know where to look.

PROMPT:
Medical education illustration, clean flat-vector style with soft shading (not a clinical photograph), white (#ffffff) background, font Inter. Title at top in bold navy (#0f1e2e): "Scrub Typhus: Where to Look for the Scab". Subtitle in teal (#1a6b72): "Painless, black, often hidden in skin folds". Center: a neutral, non-sexualized adult body outline in light warm gray, front view with arms slightly raised, plus a smaller back-view outline beside it, both in simple plain underwear. Five renal green (#1f7a4d) target markers with leader lines to short labels: "Armpits", "Groin and buttock folds", "Waistband and belt line", "Behind the ears and neck", "Behind the knees". Lower-right inset in a rounded card with a thin teal border: a magnified illustrated eschar, a round black crust with a narrow red rim on light brown skin, labeled "Eschar: painless, 5–20 mm", with a pencil-eraser silhouette beside it for scale. Bottom strip, soft gray (#f3f4f6), navy text: "No scab? Scrub typhus is still possible. Tell the doctor about grass or farm work." Bottom-center: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No photographs of real skin lesions, no gore, no nudity, no sexualized depiction. Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Five sites clearly labeled, inset eschar recognizable with a familiar size reference, white background, attribution bottom-center.
```

### 10 — Malaria in the Philippines today (`williamriveromd-simple-figure`, Scaffold E)

```
FILE NAME: tropical-infection-aki-10-malaria-where-now.png
IMAGE TYPE: Scaffold E — square schematic map card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Show that local malaria is now concentrated in Palawan, and that travel is the other common source.

PROMPT:
Clean schematic reference card, white (#ffffff) background, font IBM Plex Sans. Bold navy title at top: "Where Malaria Comes From Today". Left two-thirds: a simplified, stylized outline of the Philippine archipelago in light gray (#e5e7eb) with thin slate outlines, drawn as a schematic, not a precise map. Palawan, the long narrow island in the west, is filled in soft purple (#6c3d8e at 40% opacity), with its southern half shaded darker and a small purple tree-and-mosquito icon. A short leader label: "Palawan: southern forests and foothills". All other islands remain plain light gray with a small green check icon and the label "Most provinces: malaria-free". Right third: a rounded card with an airplane icon and the label "Travel to Africa, South Asia, or other malaria areas", plus a navy line: "Fever up to months after travel? Mention it." Bottom strip in navy: "Source: Department of Health elimination reports." Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Do not attempt a precise or detailed geographic map; do not label other provinces or cities; no misspelled place names; no national flags. Avoid clutter, tiny labels, AI gibberish text, HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Palawan unmistakable as the highlighted western island; schematic, uncluttered; "Palawan" spelled correctly; white background; attribution bottom-right.
```

> Map caution: image models distort coastlines. Check that Palawan sits west and is long and narrow. If the outline is poor, ask for "only Palawan drawn large, with a small locator inset of the Philippines".

### 11 — Monkey malaria loop (`williamriveromd-organ-crosstalk-sigil-graphic`)

```
FILE NAME: tropical-infection-aki-11-knowlesi-sigil.png
IMAGE TYPE: Organ-crosstalk sigil (transmission loop variant)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and clinicians
VISUAL GOAL: A calm symbol of P. knowlesi spillover: macaque → mosquito → human.

PROMPT:
Create a simple medical crosstalk sigil illustration featuring three icons arranged in a balanced triangle: a long-tailed macaque head in profile at top center, an Anopheles mosquito at lower left, and a human figure at lower right. Show the transmission path with soft dotted curved arrows: macaque to mosquito, then mosquito to human, with a soft dotted arrow from the mosquito back to the macaque to close the natural forest cycle. No arrow from the human back to the mosquito. Small optional labels in Inter: "Macaque", "Mosquito", "Person", and a centered small caption "Plasmodium knowlesi" in italic-free plain sans-serif. Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with a single purple (#6c3d8e) accent on the mosquito, white background, generous whitespace, no photorealism, no 3D. Include a small semi-transparent "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, aggressive or frightening animal faces, excessive labels, dark background, neon colors, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons. Only Inter, Nunito Sans, IBM Plex Sans, or Manrope if text appears. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three icons, clear directional loop, calm and symbolic, white background, attribution bottom-right.
```

### 12 — One protective action per infection (`williamriveromd-infographic-skill`, multi-panel)

```
FILE NAME: tropical-infection-aki-12-prevention-card.png
IMAGE TYPE: Multi-panel educational infographic (four action scenes)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients, families, barangay health workers
VISUAL GOAL: One concrete, doable action per infection, shown rather than told, plus one shared "avoid" rule.
VISUAL MIX:
- photorealistic models: four short action scenes, different people
- 2D infographic: colored bands, check icons, one red "avoid" panel
- 3D component graphics: none
- algorithm/flowchart: none

PROMPT:
Patient education infographic, landscape 16:9, white (#ffffff) background, font Nunito Sans. Bold navy title: "Protect Yourself: One Habit for Each Infection". Four rounded photo cards in a row, each with the shared infection color band and icon, a green check badge (#1f7a4d), and a caption of at most six words:
1. Amber band, "Leptospirosis": an older man in rubber boots and long rubber gloves cleaning mud from a flooded house. Caption: "Boots and gloves in floodwater".
2. Red band, "Dengue": a mother and son tipping still water out of a flower-pot saucer into the drain. Caption: "Empty standing water every week".
3. Green band, "Scrub typhus": a young woman farmer with long sleeves and trousers tucked into socks spraying repellent on her trouser legs at a field edge. Caption: "Long sleeves, tucked pants, repellent".
4. Purple band, "Malaria": a family of three under a blue insecticide-treated bed net in a simple wooden house at night, soft warm lamp light, bright and calm. Caption: "Sleep under a treated net".
Below, a full-width pale red (#fdecec) panel with a red circle-slash icon over a generic pain-reliever blister pack: "During fever, avoid mefenamic acid and ibuprofen. Use paracetamol." Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No readable brand names on medicines, no dark night scenes (keep the bed-net scene warmly lit and bright), avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, generic stock-photo look. NEVER use dark backgrounds for the canvas. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Four clear actions, four different people, short captions, no readable brand names, white canvas, attribution bottom-right.
```

### 13 — Recovery and follow-up timeline (`williamriveromd-simple-figure`, Scaffold C)

```
FILE NAME: tropical-infection-aki-13-recovery-timeline.png
IMAGE TYPE: Scaffold C — horizontal timeline
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Make follow-up after discharge concrete: what to check, and when.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, font Inter. Bold navy title: "After the Hospital: Checking That Your Kidneys Recover". A horizontal teal (#1a6b72) timeline arrow across the canvas with four milestone dots and rounded cards above or below:
1. "Going home" (hospital-door icon): "Get your discharge creatinine. List every medicine."
2. "1–2 weeks" (blood-tube icon): "Creatinine and urine test."
3. "Within 1 month" (red-blood-cell icon, purple accent): "Blood count if you had malaria treatment."
4. "About 3 months" (kidney icon with green check #1f7a4d): "Creatinine, urine albumin, blood pressure. Recovered, or needs a kidney doctor?"
A thin dashed gray line beneath the timeline labeled "Blood pressure check at every visit". Small footer note in navy: "Most kidneys recover. Some do not, especially after leptospirosis or scrub typhus, so the checks matter." Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Four milestones in time order, labels short, white background, attribution bottom-right.
```

---

## 4. Clinician-tab images

### 05 — First-24-hour algorithm (`williamriveromd-algorithm-generator-skill`, Style Mode C)

```
FILE NAME: tropical-infection-aki-05-first-24h-algorithm.png
PIXEL DIMENSIONS: 1024 × 1536 (2:3 portrait)

Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. Use a white background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, and generous margins. The layout should be centered, top-to-bottom, and suitable for a clinician-facing nephrology guide and for printing as a ward poster.

Use these color conventions:
- Navy #0f1e2e for title, body text, and structural emphasis
- Teal #1a6b72 for decision diamonds and connector accents
- Green #1f7a4d for recommended treatment actions
- Amber #b8860b for caution nodes
- Clinical red #b91c1c for triage and escalation nodes
- Purple #6c3d8e for the malaria branch
- Soft gray for side notes

Content to render:
Title: "Fever + Acute Kidney Injury: The First 24 Hours"
Subtitle: "Philippine setting"
1. Red node: "Triage now: vitals, mental status, SpO2, urine output, glucose. KDIGO stage. Urgent KRT indication?"
2. Navy node: "3-week exposure history: floodwater · grass or farm · Palawan forest or travel · dengue contacts · NSAIDs"
3. Navy node: "Undress the patient and search for an eschar"
4. Teal node: "Send: CBC, creatinine, electrolytes, gas with base deficit and lactate, bilirubin, CK, urinalysis, blood cultures, dengue NS1/IgM, lepto PCR/IgM, scrub IgM/PCR, malaria smear + RDT"
5. Teal diamond: "Malaria test positive?" — right branch labeled "Yes" to a purple node: "Any WHO severe criterion → IV artesunate now (no renal dose change)"; downward branch labeled "No / pending" continues.
6. Green node: "Lepto or scrub typhus plausible → doxycycline (no renal dose change) ± ceftriaxone. Severe scrub typhus → IV doxycycline + azithromycin"
7. Gray side note attached to node 6: "Ceftriaxone does not cover Orientia"
8. Amber node: "Fluids to perfusion: small boluses, reassess. Avoid liberal fluids in plasma leak or severe malaria. Stop nephrotoxins."
9. Red node: "Reassess at 12–24 h. Rising creatinine, acidosis, or hypoxemia → nephrology + ICU, plan KRT (blood-based preferred; acute PD if nothing else)"

Design requirements:
- Clear title and subtitle
- Rounded rectangles for actions; one diamond for the malaria decision
- Consistent node widths and vertical spacing; no crossing arrows
- No dark background, no clutter, no photorealistic people, no icons inside nodes
- Make the diagram publication-grade and vector-like, with crisp typography, perfectly aligned nodes, consistent arrow lengths, and generous margins. Ensure all text is legible at full size and thumbnail size.
- Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-right corner in subtle gray medical-publication styling.
```

### 04 — Four infections compared (`williamriveromd-infographic-skill`, clinician reference card)

```
FILE NAME: tropical-infection-aki-04-comparison.png
IMAGE TYPE: Clinician reference card (comparison grid)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, nursing and medical students
VISUAL GOAL: A quick-look grid comparing leptospirosis, dengue, scrub typhus, and malaria at the kidney level.
VISUAL MIX:
- photorealistic models: none
- 2D infographic: grid, colored column headers, icons
- 3D component graphics: none
- algorithm/flowchart: none

PROMPT:
Clinical reference infographic card for clinicians, publication-grade nephrology design, white (#ffffff) background, font IBM Plex Sans. Bold navy (#0f1e2e) title: "Febrile AKI in the Tropics: Four Infections Compared". A grid of four columns, each headed by a colored band and a small line icon: Leptospirosis (amber #b8860b, water-drop icon), Dengue (red #b91c1c, day-mosquito icon), Scrub typhus (green #1f7a4d, mite icon), Malaria (purple #6c3d8e, night-mosquito icon). Row headers on soft gray (#f3f4f6) in teal (#1a6b72): "Exposure", "Bedside clue", "Kidney lesion", "Confirm with", "Treat with". Cell text, short:
Leptospirosis — Floodwater, rice fields / Calf pain, conjunctival suffusion / ATIN, ATN; non-oliguric, low K / PCR, IgM, MAT / Penicillin, ceftriaxone, or doxycycline.
Dengue — Aedes bites / Plasma leak at defervescence / ATN from shock, rhabdomyolysis / NS1, IgM / Supportive care.
Scrub typhus — Grass, scrub, farm edges / Eschar (about half) / ATN, ATIN, vasculitis / IgM ELISA, PCR / Doxycycline ± azithromycin.
Malaria — Palawan forest, travel / Periodic fever, pallor / ATN, hemoglobinuria / Smear, RDT, PCR / IV artesunate, then ACT.
Footer strip in teal: "Doxycycline covers leptospirosis and scrub typhus; ceftriaxone does not cover Orientia." Alternating white and very soft gray rows. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid misspelled organism names, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Every cell legible on a phone; organism and drug names spelled correctly (Orientia, Leptospira, Plasmodium, artesunate, azithromycin); white background; attribution bottom-right.
```

### 14 — Scrub typhus kidney mechanism (`williamriveromd-biomedical-mechanism-figure`)

```
FILE NAME: tropical-infection-aki-14-scrub-typhus-mechanism.png
PIXEL DIMENSIONS: 1792 × 1024 (16:9)

Create a publication-grade biomedical mechanism schematic about:

Topic: How scrub typhus injures the kidney
Disease context: Orientia tsutsugamushi infection (scrub typhus) with acute kidney injury
Central mechanism: Disseminated endothelial infection and vasculitis causing kidney injury through several simultaneous routes

Organ-level panel (left): A simplified human silhouette in light gray-blue with a small eschar marked at the waistline, thin red arrows showing spread through the bloodstream to the lungs, liver, heart, brain, and both kidneys. Disease label above: "Scrub typhus: systemic vasculitis". A small dashed connector box from the right kidney points to the magnified panel.

Magnified mechanism panel (center-right, inside a thin dashed border): A cross-section of renal cortex showing a peritubular capillary and adjacent proximal tubules (tubules in soft yellow). Callouts:
- "Orientia inside endothelial cells and monocytes" (small red dots within capillary lining)
- "Endothelial injury → capillary leak → ↓ renal perfusion" (prerenal)
- "Shock → acute tubular necrosis (ATN)" (pale, injured tubular cells with sloughed debris)
- "Mononuclear interstitial infiltrate → acute tubulointerstitial nephritis (ATIN)"
- Small side inset: "Muscle breakdown → myoglobin casts (rhabdomyolysis)"

Bottom summary flow:
Left pale-pink pathology box: "Fever, vomiting, capillary leak · Hypotension · Interstitial inflammation · Myoglobin → Acute kidney injury"
Center box (intervention): "Doxycycline or azithromycin; severe disease: IV doxycycline + azithromycin (INTREST trial)" with a small capsule icon; a gray footnote: "No renal dose adjustment"
Right pale-blue benefit box: "Faster defervescence · Resolution of organ dysfunction · Kidney recovery in most patients; follow up for CKD"
Arrows flow injury → intervention → benefit.

Use a white background, muted clinical colors, clean sans-serif labels set in Inter (never a serif font), thin dashed connector lines, and a review-article figure style. Avoid photorealism, dark backgrounds, decorative elements, and overcrowding. Keep all text legible at slide size. Do not invent pathways or numeric thresholds. Add small, semi-transparent navy text "© renalcarematters.com" in the bottom-right corner.
```

### 15 — One vasculitis, five organs (`williamriveromd-organ-crosstalk-sigil-graphic`)

```
FILE NAME: tropical-infection-aki-15-scrub-multiorgan-sigil.png
PIXEL DIMENSIONS: 1024 × 1024 (1:1)

Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- a small stylized blood vessel ring at the center (representing endothelium)
- lungs (top)
- liver (upper right)
- heart (upper left)
- brain (top center, above the lungs)
- both kidneys (bottom center)

RELATIONSHIP:
Show one shared disease process radiating from the central vessel ring to every organ with soft dotted curved arrows, the arrow to the kidneys drawn slightly bolder in teal to show the focus of this guide.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette, white background, clean rounded organ shapes, balanced radial sigil composition, generous whitespace, no photorealism, no 3D. Small labels set in Inter only: under each organ, its name and the INTREST trial involvement — "Lungs 62%", "Liver 54%", "Heart and circulation 42%", "Kidneys 30%", "Brain 20%" — and at the center "Scrub typhus vasculitis".

COMPOSITION:
Central vessel ring with five organs arranged around it in a gentle circle; kidneys at bottom center. Calm, symbolic, suitable for a nephrology website.

OUTPUT:
Square, clean margins, high-resolution. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.

NEGATIVE: photorealistic anatomy, surgical detail, extra labels, dark background, neon colors, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, serif fonts.
```

> Numbers on this sigil are organ involvement among 794 adults with severe scrub typhus in INTREST (Varghese 2023). Proofread every percentage after generation; regenerate if any figure is altered.

### 16 — Malaria AKI mechanism (`williamriveromd-biomedical-mechanism-figure`)

```
FILE NAME: tropical-infection-aki-16-malaria-aki-mechanism.png
PIXEL DIMENSIONS: 1792 × 1024 (16:9)

Create a publication-grade biomedical mechanism schematic about:

Topic: Malaria-associated acute kidney injury
Disease context: Severe Plasmodium falciparum or P. knowlesi malaria
Central mechanism: Sequestration of infected red cells plus cell-free hemoglobin oxidative injury converging on acute tubular necrosis

Organ-level panel (left): A simplified kidney cross-section in light gray-blue with a disease label "Severe malaria: AKI". A small inset shows red blood cells, some containing small purple ring-form parasites. A dashed connector leads to the magnified panel.

Magnified mechanism panel (center-right, dashed border): A peritubular capillary beside a proximal tubule (tubule in soft yellow).
- Inside the capillary: infected red cells adhering to the endothelium and to each other, labeled "Sequestration → ↓ microvascular flow → lactic acidosis".
- Free-floating burst red cells releasing hemoglobin, labeled "Intravascular hemolysis → cell-free hemoglobin".
- An arrow into the tubule cell: "Ferryl heme → lipid peroxidation → oxidative tubular injury".
- Tubule cells pale and detaching: "Acute tubular necrosis".
- Small side callouts: "Rhabdomyolysis", "Hyperbilirubinemia", "RAAS activation" in muted text.

Bottom summary flow:
Left pale-pink pathology box: "Sequestration · Hemolysis and cell-free hemoglobin · Oxidative stress · Acidosis → ATN"
Center box (intervention): "IV artesunate (no renal dose change) · Cautious fluids, not liberal · Early kidney replacement therapy". A separate small dashed sub-box labeled "Adjunct under study: acetaminophen (phase 2 trial evidence; creatinine endpoint)".
Right pale-blue benefit box: "Parasite clearance · Less oxidative injury (proposed) · Survival depends on timely dialysis when AKI is severe"
Arrows flow injury → intervention → benefit.

Use a white background, muted clinical colors, clean sans-serif labels set in Inter (never a serif font), thin dashed connector lines, review-article figure style. Avoid photorealism, dark backgrounds, decorative elements, overcrowding. Do not invent pathways or numeric thresholds. Add small, semi-transparent navy text "© renalcarematters.com" in the bottom-right corner.
```

### 17 — Choosing kidney replacement therapy (`williamriveromd-simple-figure`, Scaffold B)

```
FILE NAME: tropical-infection-aki-17-krt-modality.png
IMAGE TYPE: Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show when blood-based therapy is preferred and when acute PD is the right answer.

PROMPT:
Medical education comparison infographic, AJKD graphical-abstract style, white (#ffffff) background, font IBM Plex Sans. Title at top center in bold navy: "Kidney Replacement Therapy in Infection-Associated AKI". A soft dashed vertical divider splits two equal panels.
Left panel, header in teal (#1a6b72): "Blood-based therapy (hemofiltration or hemodialysis)". A simple schematic icon of a hollow-fiber filter cartridge drawn vertically, blood entering at the bottom end port and leaving at the top end port, with no extra tubing detail. Three short bullets: "Preferred when available", "Faster correction of acidosis and creatinine", "Vietnam RCT: mortality 15% vs 47% with PD".
Right panel, header in renal green (#1f7a4d): "Acute peritoneal dialysis (PD)". A simple schematic icon of a PD catheter entering a stylized abdomen outline with a fluid bag. Three short bullets: "Lifesaving where blood-based therapy is unavailable", "No anticoagulation needed", "Modern automated PD not yet tested in this setting".
Bottom strip spanning both panels, amber (#b8860b) caution icon: "Low platelets (dengue, leptospirosis, malaria, scrub typhus): heparin-free circuit or regional citrate; ultrasound-guided catheter." Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Do not draw a full dialysis circuit, pumps, pressure gauges, or numeric pressure settings; if any filter port detail appears, blood enters and exits through the two END ports only. Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two balanced panels, percentages exactly "15% vs 47%", no invented settings, white background, attribution bottom-right.
```

### OG — Social share card (`williamriveromd-infographic-skill`)

```
FILE NAME: tropical-infection-aki-og.png (export a WebP twin: tropical-infection-aki-og.webp — the page's og:image points to the .webp)
IMAGE TYPE: Photorealistic editorial OG card with title
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
AUDIENCE: mixed
VISUAL GOAL: A clean social card that reads "Fever and kidney injury in the tropics" at thumbnail size.

PROMPT:
Editorial social-share card, white-to-soft-mint (#eef6f7) background, font Inter. Left 55%: bold navy (#0f1e2e) title in two lines, "Fever and Kidney Injury in the Tropics", with a teal (#1a6b72) subtitle, "Scrub typhus · Malaria · Leptospirosis · Dengue". Under the subtitle, a row of four small circular line-icon badges in the house infection colors: amber water drop, red day mosquito, green mite, purple night mosquito. Right 45%: a soft-edged, bright photographic crop of green Philippine rice paddies meeting tall cogon grass under a hazy sky, blending into the light background with a gentle fade. Small "renalcarematters.com" in semi-transparent navy at bottom-right. Generous whitespace.

NEGATIVE INSTRUCTIONS:
No dark backgrounds, no clutter, no misspelled words, no faces, no logos other than the attribution, no serif fonts, no AI gibberish text.

QUALITY CHECK:
Exactly 1200 × 630; title legible at 300 px wide; light background; attribution present.
```

---

## 5. Charts built in HTML (not AI-generated) — done

These carry exact numbers, so they are inline SVG in the guide (built Nov 6, 2026): accurate, dark-mode aware, and screen-reader labeled. No image generation needed.

| Chart | Placement | Data |
|---|---|---|
| INTREST composite outcome, 3 bars | `#md-scrub-typhus` | Doxycycline 47%, azithromycin 48%, combination 33% (n = 794) |
| Kidney involvement by infection, horizontal bars | `#md-comparison` | Leptospirosis AKI 49.2% (dialysis 14.4%); malaria AKI in adults 26.5%; scrub typhus AKI 18–53% shown as a range bar; pediatric scrub typhus 13.7%. Footnote: different populations, not directly comparable. |
| Recovery at 3 months by infection | `#md-comparison` or `#recovery` | Dengue 85%, malaria 91%, leptospirosis 61%, scrub typhus 67% (Surya Prakash 2026, n = 149) |

Each chart has an accessible `<title>`/`<desc>` and a source note under it.

---

## 6. Captions for the new figure slots (already in the guide)

Each figure has a `<figcaption>` with `<p class="fig-desc">` (CLAUDE.md rule 11) and `<dl class="fig-abbrevs">` where the image shows acronyms. Patient-tab captions are wired in all four languages. The English text is listed here for reference when proofing the generated images.

| # | `fig-desc` (English) | `fig-abbrevs` |
|---|---|---|
| 06 | Four everyday ways in: floodwater and mud (leptospirosis), daytime mosquitoes around standing water (dengue), grass and farm edges (scrub typhus), and night mosquitoes in Palawan forests or abroad (malaria). | none |
| 07 | Six warning signs that, together with fever, mean going to a hospital the same day. | none |
| 08 | Urine color and amount during a fever. Tea- or cola-colored urine, or very little urine, needs same-day care; some kidney injuries still make normal amounts, so blood tests matter. | none |
| 09 | A chigger smaller than a pinhead bites painlessly, a black scab forms, and fever starts about one to two weeks later. | none |
| 10 | Schematic, not a precise map. Most Philippine provinces are malaria-free; remaining local cases are mainly in southern Palawan, and travel abroad is the other common source. | none |
| 11 | *Plasmodium knowlesi* passes from long-tailed macaques to people through mosquitoes. | none |
| 12 | One protective habit for each infection, and one rule for any fever: avoid mefenamic acid and ibuprofen. | none |
| 13 | Follow-up after discharge: creatinine at 1–2 weeks, a blood count within a month after malaria treatment, and a full kidney check at about 3 months. | none |
| 14 | Scrub typhus infects blood-vessel linings throughout the body. The kidney is injured by low perfusion, shock, interstitial inflammation, and muscle breakdown; doxycycline and azithromycin treat the cause. | ATN — Acute tubular necrosis; ATIN — Acute tubulointerstitial nephritis; IV — Intravenous; CKD — Chronic kidney disease |
| 15 | One vasculitis, five organs: organ involvement among 794 adults with severe scrub typhus in the INTREST trial. | none |
| 16 | In severe malaria, infected red cells clog small vessels and burst red cells release hemoglobin that oxidizes tubule cells, leading to acute tubular necrosis. Artesunate, cautious fluids, and timely dialysis are the core response; acetaminophen is an adjunct still under study. | AKI — Acute kidney injury; ATN — Acute tubular necrosis; RAAS — Renin-angiotensin-aldosterone system; IV — Intravenous |
| 17 | Blood-based kidney replacement therapy is preferred in infection-associated AKI when available; acute peritoneal dialysis saves lives where it is not. | PD — Peritoneal dialysis; RCT — Randomized controlled trial; AKI — Acute kidney injury |

---

## 7. Production checklist

1. Generate in production order (§2). For any figure with text, zoom to 100% and proofread every word and number before saving; regenerate on any error (organism names, drug names, percentages).
2. Save `images/<file>.png` plus `images/<file>.webp` (same stem).
3. For the hero, confirm nothing important sits in the upper-left title-safe zone.
4. For 10 (map) and 15 (sigil with numbers), apply the extra checks noted under each prompt.
5. Commit the images to `images/`. Each figure appears automatically. Then spot-check the page in light and dark mode on a phone.
6. Optional Stage 2: `williamriveromd-local-image-generator` for `image-manifest.csv/json`.
