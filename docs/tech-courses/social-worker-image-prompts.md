# Renal Social Worker track: image plan blueprint and GPT prompt pack

Renal Care Academy → Ancillary Staff Track → Renal Social Worker. Prepared November 25, 2026. American English throughout. Stage 1 of the two-stage image pipeline: generate in ChatGPT image generation, then run the prep script (Stage 2).

## 1. Why these images

Every image has one job: make a social work decision easier to understand, apply, or appreciate. The track teaches judgment about people, money, risk, and rules, so the images show people and processes rather than anatomy, and every teaching figure turns one paragraph of the module into one picture a learner can recall on shift.

| Image | Learning purpose | Where it appears | Count |
| --- | --- | --- | --- |
| **Circular vignette hero** | Appreciation: who is involved, where, and what is at stake | Top of the course home and each module | 21 |
| **Teaching figure A** | Understanding: the module’s central idea | Already wired into the module text (`figs.py`) | 22 |
| **Teaching figure B** | Application: a decision tool, checklist, or flow to use on shift | Wired after the first paragraph of its section | 17 |
| **Course tile** | Navigation: recognition on the syllabus cards and module tiles | Course home module cards; Related Guides thumbnails | 21 |
| **OG share card** | Reach: a share preview that names the page | `og:image` for the course home and each module (`images/og/<slug>-og.jpg`, picked up automatically) | 21 |
| **Toolkit OG card** | Reach for the calculator page | `og:image` of `guides/calc-social-worker-toolkit.html` | 1 |
| **Track share-card art** | Background for the Academy composited track card (text set by `build_academy_og.py`) | `images/academy/og-art/social-worker.webp` | 1 |
| **Landing tile** | The Renal Social Worker card on `academy/index.html` | `images/academy/landing/social-worker.webp` | made from the course tile |

**Total: 104 prompts.**

## 2. Rules for every image

- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e; the Ancillary track accent is green #2e6b3e.
- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.
- **Attribution:** teaching figures and OG cards carry `© renalcarematters.com` bottom-right. Heroes and tiles carry no text at all.
- **Privacy and dignity:** fictional people only; no legible names, ID numbers, PhilHealth numbers, documents, or screens; no self-harm imagery; no tears in close-up; violence and abuse shown only as a small described bruise or as icons.
- **Numbers:** an image carries only the numbers written in its prompt, each already in the module and verified (156 sessions; 10/12 = 83.3%; 2-day gap; 3 to 6 months).
- **People:** Filipino patients, families and staff; a different cast, camera and setting in each hero (hero-vignette v3 human-variation rule).
- **Skills used:** `williamriveromd-hero-vignette` v3 (heroes), `williamriveromd-infographic-skill` v5 (figures, tiles, OG cards), `williamriveromd-simple-figure` (single-idea figures), `williamriveromd-algorithm-generator-skill` Style Mode C (the safety pathway, the two-step screen, the release decision).

## 3. Production workflow

1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `images/incoming/social-worker/` in the repo (track art in a subfolder `og-art/`). You can also drop them in `/Volumes/Storage/Renal Care Academy/Social Worker/images/` first for audit.
2. Run `python3 tools/techcourses/sw/prep_images.py` (`--report` lists what is still missing). It writes heroes to `images/<slug>-vignette-hero.png` + `.webp`, figures to `images/<stem>.webp` + `.png`, tiles to 640 × 360 WebP (the course tile also to `images/academy/landing/social-worker.webp` 960 × 540), OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`, and the track art to `images/academy/og-art/social-worker.webp`.
3. Rebuild: `python3 generate_tech_courses.py --course sw --patch`; `python3 build_academy_og.py --art images/academy/og-art --only social-worker --patch` and `--only academy-index`; `python3 generate_rg_thumbs.py`; `python3 patch_rg_card_thumbs.py`.
4. Add `<img class="nc-fig-img" src="../images/academy/landing/social-worker.webp" …>` to the Renal Social Worker card on `academy/index.html` once the landing tile exists (the card is in place without an image).
5. Audit each image against its QUALITY CHECK, check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger.

## 4. Image map by module

| Module | Hero idea | Figure A (understand) | Figure B (apply) |
| --- | --- | --- | --- |
| 1. The Renal Social Worker: Role, Ethics, and Boundaries | Say who you are and what you do before anything else. | Who decides what | Before the person speaks |
| 2. Kidney Care Literacy for Social Workers | The social worker learns the dialysis week from the people who run it. | The dialysis week | What kidneys do, what dialysis replaces |
| 3. Philippine Requirements and a Defensible Service Model | Every rule has an issuer and a date. | Who issues what | A one-page service charter |
| 4. Engagement, Language Access, and Cultural Safety | Privacy, her language, and her permission come first. | The first five minutes | Teach-back |
| 5. A Comprehensive Psychosocial Assessment | The assessment looks for the reason behind the label. | Psychosocial assessment domains; From facts to formulation to plan | — |
| 6. Care Plans, Referrals, and Case Management | A referral is closed by a phone call, not a form. | The referral loop | Goals that belong to the person |
| 7. PhilHealth Navigation and Financial Protection | Explain the benefit by its rule and date, never by rumor. | Reading a PhilHealth rule | Four checks before you explain a benefit |
| 8. Assistance Pathways and Resource Mobilization | One strong application beats seven thin ones. | Mapping assistance | — |
| 9. Transport, Work, Housing, Food, and Disability Access | Getting to dialysis is a cost the household pays thirteen times a month. | The access equation | Keeping a livelihood |
| 10. Distress, Depression, Anxiety, and Stepped Support | Notice, ask, and listen before you score anything. | Stepped psychosocial care | The two-step depression screen |
| 11. Immediate Safety, Safeguarding, Violence, and Exploitation | Safety conversations happen in private and at an unhurried pace. | The safety pathway | Signs of abuse and exploitation |
| 12. Motivational Conversations and Treatment Barriers | Walk beside the person; do not push. | OARS in a conversation | Change talk and sustain talk |
| 13. Families, Caregivers, Children, and Changing Life Roles | See the person beside the chair. | Caregiver load and backup | Protecting a young carer |
| 14. Modality Decisions, Home Therapy, and Practical Feasibility | Feasibility is decided in the home, not only in the clinic. | What each treatment asks of a household | Solve before you rule out |
| 15. Transplant Access, Psychosocial Preparation, and Donor Protection | The donor is seen alone, and free to say no. | The donor's separate path | Signals to route, not to judge |
| 16. Supportive Care, Treatment Decisions, Grief, and Bereavement | Advance care planning is a conversation, not a form. | Advance care planning | Bereavement follow-up |
| 17. Transfers, Disasters, and Continuity of Care | Continuity means every patient dialyzed somewhere, even in a typhoon. | Continuity in a typhoon | The personal emergency plan |
| 18. Documentation, Privacy, Telehealth, and Digital Boundaries | Least information, right recipient, documented reason. | Minimum necessary disclosure | Releasing information |
| 19. Quality Improvement, Supervision, and Workload | Measure what matters, and think it through in supervision. | A measure that means something | — |
| 20. Integrated Case Conference and Readiness for Practice | One family, one plan, every owner named. | One family, start to finish | A five-minute case presentation |

## 5. Track-level images

### Course home hero

```
FILE NAME: images/social-worker-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide environmental portrait, eye level
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Kidney failure lands on a household; the social worker sits with all of it.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide environmental portrait, eye level. Subject: a Filipina renal social worker in her early 40s with a round face, shoulder-length wavy black hair tucked behind one ear, and a mustard-yellow cardigan over a white blouse, seated on a low stool at eye level beside an older man in a dialysis recliner, listening with a small notebook closed on her knee; his wife sits close on his other side holding a tote bag; a nurse works at the next station, softly blurred, in a bright modern Philippine hemodialysis unit, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

### Course home figure A (also used in Module 1)

```
FILE NAME: images/social-worker-00-kidney-failure-lands-on-a-household.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Radial infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Kidney failure lands on a household". Center: a semi-photoreal Filipino man in his 50s seated in a dialysis recliner. Around him, seven concentric soft rings, each with one small icon and one label: "Body" (kidney icon), "Household" (house), "Money" (peso coin), "Transport" (tricycle), "Work" (tool bag), "Family roles" (three figures), "Community services" (barangay hall). A social worker figure stands just outside the outer ring holding a notebook, with a thin teal dotted line touching every ring. Footer line: "See every ring, not only the body." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Kidney failure is a medical event that lands on a household. The social worker looks at every ring, not only the body.
*Alt text:* A Filipino man on dialysis at the center of concentric rings labeled body, household, money, transport, work, family roles, and community services, with small icons on each ring and a social worker standing beside the rings with a notebook.

### Course tile and Academy landing tile

```
FILE NAME: images/social-worker-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP; the course tile also writes images/academy/landing/social-worker.webp 960 × 540)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the track’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a social worker’s notebook and a small compass resting on a bright dialysis unit side table beside a folded blanket, soft daylight. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

### Course home OG card

```
FILE NAME: images/og/social-worker-og.png (prep script exports images/og/social-worker-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Renal Social Worker". Subtitle in teal #1a6b72: "20 modules · assessment, support, and access to care". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a social worker’s notebook and a small compass resting on a bright dialysis unit side table beside a folded blanket, soft daylight, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Toolkit OG card

```
FILE NAME: images/og/social-worker-toolkit.png (prep script exports images/og/social-worker-toolkit.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Social Worker Toolkit". Subtitle in teal #1a6b72: "6 planning tools · access cost · session balance · workload". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a calculator, a small peso coin stack, a desk calendar and a clipboard with a blurred grid, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Track share-card art (Academy composited card)

```
FILE NAME: images/incoming/social-worker/og-art/social-worker.png (prep script writes images/academy/og-art/social-worker.webp)
IMAGE TYPE: Background art for build_academy_og.py (the script sets every word)
PIXEL DIMENSIONS: 1536 × 1024

PROMPT:
3:2 landscape photorealistic editorial photograph on a light background: in a bright Philippine hemodialysis unit, a Filipina social worker in her 40s with shoulder-length wavy hair and a mustard cardigan sits at eye level beside an older man in a dialysis recliner while his wife sits close; a nurse softly blurred in the background. Place the people in the RIGHT 55%; keep the LEFT 45% as clean, light, empty negative space (soft wall and window light) where the builder sets the track title, group label and stats. Soft daylight, gentle depth of field, colors harmonizing with green #2e6b3e, teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark; no legible screens or papers.

NEGATIVE INSTRUCTIONS:
Avoid text, clutter, dark backgrounds, distressing expressions, legible documents, people in the left 45%.

QUALITY CHECK:
Left 45% empty and light; subjects on the right; no text.
```

## 6. Module prompts

### Module 1: The Renal Social Worker: Role, Ethics, and Boundaries

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-01-role-and-professional-boundaries-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder, slightly high
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Say who you are and what you do before anything else.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder, slightly high. Subject: a young Filipino social worker in his late 20s with a narrow face, neat undercut, thin-framed glasses and a sage-green polo, holding a small blank role card toward a middle-aged couple seated in a quiet corner of a dialysis unit; the wife leans in, the husband nods, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Who decides what**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-01-who-decides-what.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Role map infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Who decides what". Center: a patient and family pictogram. Six rounded tiles around it, each with an icon, the role, and what it owns: "Nephrologist — treatment", "Nurse — bedside care", "Claims officer — benefit paperwork", "Social worker — assessment, plan, advocacy" (teal highlight), "Mental health clinician — diagnosis and therapy" (purple), "Supervisor — coverage and review". A small amber footer chip: "A navigator prepares; only the registered social worker signs." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Who decides what. You coordinate many decisions and own a few; name the owner of each.
*Alt text:* A role map with six labeled tiles around a patient and family: nephrologist (treatment), nurse (bedside care), claims officer (benefits paperwork), social worker (psychosocial assessment, plan, advocacy), mental health clinician (diagnosis and therapy), and supervisor (coverage and review).

**Figure B: Before the person speaks**  ·  skill `simple-figure`  ·  placed in section `ethics`

```
FILE NAME: images/social-worker-01-before-the-person-speaks.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Reference card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Before the person speaks". A clean reference card with four numbered rows and icons: "1 Who I am and what a social worker does here", "2 Why I am asking", "3 Who may see what you tell me", "4 The limits: immediate risk to life, legal duty to report". Footer: "Then ask: whom do you want in the room?" Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Say these four things before the first personal question.
*Alt text:* A card with four items a social worker says before an interview: who I am, why I am asking, who may see it, and the limits of confidentiality.

**Course tile**

```
FILE NAME: images/social-worker-01-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a blank role card and a lanyard on a light desk beside two chairs angled toward each other. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-01-role-and-professional-boundaries-og.png (prep script exports images/og/social-worker-01-role-and-professional-boundaries-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "The Renal Social Worker: Role, Ethics, and Boundaries". Subtitle in teal #1a6b72: "Renal Social Worker · Module 1 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a blank role card and a lanyard on a light desk beside two chairs angled toward each other, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 2: Kidney Care Literacy for Social Workers

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-02-kidney-care-literacy-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: side profile, medium distance
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: The social worker learns the dialysis week from the people who run it.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: side profile, medium distance. Subject: a Filipina dialysis nurse in her 50s with a short pixie cut and navy scrubs pointing at a hemodialysis machine while a younger social worker with a long braid and a lilac blouse watches and listens; a wall whiteboard with three shaded blocks (no writing) behind them, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The dialysis week**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-02-the-dialysis-week.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Timeline and physiology chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The dialysis week". Top: a seven-day strip Monday to Sunday with three teal 4-hour blocks on Monday, Wednesday, Friday, each with a lighter travel band before and after. Bottom: one smooth sawtooth line labeled "Body water and potassium" rising between sessions and dropping during them, highest on Monday morning; the Friday-to-Monday gap shaded amber and labeled "Long gap: 2 days". A small red marker on the Monday peak: "Skip Friday = 4 days". No other numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Dialysis is a schedule and a body. Fluid and potassium build up between sessions, most over the long weekend gap, which is why a missed session is dangerous.
*Alt text:* A seven-day week drawn as a calendar strip with three four-hour dialysis blocks and their travel time shaded, above a sawtooth line of body water and potassium that rises between sessions and falls during them, highest after the two-day weekend gap.

**Figure B: What kidneys do, what dialysis replaces**  ·  skill `simple-figure`  ·  placed in section `kidneys`

```
FILE NAME: images/social-worker-02-what-dialysis-replaces.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison table graphic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "What kidneys do, what dialysis replaces". Left column: a semi-photoreal kidney labeled "Healthy kidneys: 168 hours a week". Right column: a dialysis machine labeled "Hemodialysis: about 12 hours a week". Five rows between them with check or cross icons: "Remove water and salt — partly", "Balance potassium — partly", "Remove wastes — partly", "Make the red-cell hormone — no (injections needed)", "Activate vitamin D — no (medicines needed)". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Dialysis replaces part of the cleaning, not the kidney’s hormones.
*Alt text:* A two-column comparison of kidney jobs and how much dialysis replaces each: water and salt, potassium, wastes partly; red-cell hormone and active vitamin D not.

**Course tile**

```
FILE NAME: images/social-worker-02-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a desk calendar with three days circled in teal beside a small model of a kidney. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-02-kidney-care-literacy-og.png (prep script exports images/og/social-worker-02-kidney-care-literacy-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Kidney Care Literacy for Social Workers". Subtitle in teal #1a6b72: "Renal Social Worker · Module 2 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a desk calendar with three days circled in teal beside a small model of a kidney, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 3: Philippine Requirements and a Defensible Service Model

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-03-philippine-regulation-and-service-design-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: environmental portrait, low angle
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians and managers
VISUAL GOAL: Every rule has an issuer and a date.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: environmental portrait, low angle. Subject: a Filipino dialysis unit head in his 60s with a broad face, gray side-parted hair and a barong-style white shirt, reviewing a binder with colored date tabs beside a social worker in her 30s with a high ponytail and a teal blazer, in a small bright hospital office, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Who issues what**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-03-who-issues-what.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Multi-panel educational infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Who issues what". Five cards on a desk, each with a small calendar icon labeled "Effective date": "Congress + PRC — who may practice (RA 4373, RA 10847)", "DOH — facility licensing (AO 2012-0001)", "PhilHealth — benefit circulars", "DSWD · PCSO · LGU — assistance programs", "Your hospital — job description and procedures". Bottom banner: "Tag every rule: issuer · scope · version · date." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Who issues what. Read every rule for its issuer, its scope, and the date it took effect.
*Alt text:* Five labeled cards on a desk, each with a small calendar for its effective date: Congress and PRC (practice of social work), DOH (facility licensing), PhilHealth (benefit circulars), DSWD, PCSO and LGU (assistance programs), and the hospital or unit (job description and procedures).

**Figure B: A one-page service charter**  ·  skill `simple-figure`  ·  placed in section `charter`

```
FILE NAME: images/social-worker-03-one-page-service-charter.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: One-page document mockup
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "A one-page service charter". A clean single page mockup with six labeled blocks: "Purpose", "Who is referred", "How fast (immediate · same day · 2 days to acknowledge · 10 days to assess)", "Who covers", "How we measure", "What we do not do". A small amber tag on "How fast": "Local targets, not national deadlines". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The service charter fits on one page.
*Alt text:* A one-page service charter with six labeled blocks: purpose, who is referred, how fast, who covers, how we measure, what we do not do.

**Course tile**

```
FILE NAME: images/social-worker-03-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a neat binder with colored date tabs and a small desk calendar. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-03-philippine-regulation-and-service-design-og.png (prep script exports images/og/social-worker-03-philippine-regulation-and-service-design-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Philippine Requirements and a Defensible Service Model". Subtitle in teal #1a6b72: "Renal Social Worker · Module 3 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a neat binder with colored date tabs and a small desk calendar, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 4: Engagement, Language Access, and Cultural Safety

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-04-engagement-and-cultural-safety-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: eye-level two-shot, close
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Privacy, her language, and her permission come first.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: eye-level two-shot, close. Subject: an 80-year-old Filipina grandmother with short white permed hair, a floral duster and a wooden cane, seated knee to knee with a social worker in her 30s with a short bob and a coral blouse who holds a simple picture card toward her; a closed door, a glass of water, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The first five minutes**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-04-the-first-five-minutes.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The first five minutes". Four numbered panels left to right, semi-photoreal: 1 "Set the room" (closed door, two chairs angled, water glass); 2 "Ask her language" (speech bubble with three small flag-free language bubbles labeled "Filipino", "Ilocano", "Cebuano"); 3 "Say your role and the limits of confidentiality" (social worker with a role card); 4 "Ask who may join" (a relative waiting outside a door, a check mark). Footer: "Every first interview, every time." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The first five minutes. Privacy, the person's language, your role, and their permission before anyone else joins.
*Alt text:* A small private consultation room: a social worker seated at eye level with an older Filipino woman, chairs angled, door closed, a family member waiting outside, a printed visual card in Filipino on the table.

**Figure B: Teach-back**  ·  skill `simple-figure`  ·  placed in section `literacy`

```
FILE NAME: images/social-worker-04-teach-back-loop.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Circular workflow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Teach-back". A circular loop of four semi-photoreal steps between a social worker and an older woman: "Explain one idea", "Ask for it back in her own words", "Listen for gaps", "Explain again differently (picture, calendar)". Center: a speech bubble "Opo" crossed out lightly with the label "Not proof of understanding". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Teach-back checks the explanation, not the person.
*Alt text:* A four-step loop: explain one idea, ask for it back, listen for gaps, explain again differently.

**Course tile**

```
FILE NAME: images/social-worker-04-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two chairs angled toward each other with a glass of water and a picture card on a small table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-04-engagement-and-cultural-safety-og.png (prep script exports images/og/social-worker-04-engagement-and-cultural-safety-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Engagement, Language Access, and Cultural Safety". Subtitle in teal #1a6b72: "Renal Social Worker · Module 4 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two chairs angled toward each other with a glass of water and a picture card on a small table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 5: A Comprehensive Psychosocial Assessment

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-05-psychosocial-assessment-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: three-quarter view, medium
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: The assessment looks for the reason behind the label.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: three-quarter view, medium. Subject: a Filipino construction worker in his late 30s with a weathered angular face, a buzz cut and a gray work shirt, talking with his hands while a social worker in her 50s with salt-and-pepper hair in a clip and a maroon blouse writes on a clipboard in a hospital social service office, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Psychosocial assessment domains**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-05-psychosocial-assessment-domains.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Radial infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Psychosocial assessment domains". A circular map of eight equal segments with one label each: "Goals and values", "Understanding of illness", "Mood, coping, safety", "Family and caregivers", "Money and benefits", "Transport and housing", "Work, school, roles", "Substances, legal, other". In each segment a small green strength icon (star) and a small amber barrier icon (stone). Center: "Strengths beside barriers". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The psychosocial assessment covers every domain and records strengths beside barriers.
*Alt text:* A circular assessment map with eight segments (goals and values, understanding of illness, mood and coping, family and caregivers, money and benefits, transport and housing, work and school, safety) each pairing a strength icon and a barrier icon.

**Figure A: From facts to formulation to plan**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-05-from-facts-to-formulation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Left-to-right flow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "From facts to formulation to plan". Left: five scattered fact cards, each with a tiny source tag ("patient", "wife", "nurse", "chart", "claims"). Middle: the cards grouped into a four-part box labeled "Predisposing · Precipitating · Perpetuating · Protective". Then one sentence card labeled "Formulation" (blurred lines). Right: a plan card with three rows "Action · Owner · Date". A curved arrow from the plan back to the facts labeled "Review". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* From facts to formulation to plan. The formulation explains why; the plan says who does what by when.
*Alt text:* A left-to-right diagram: scattered fact cards with their sources, grouped into a pattern, summarized in one formulation sentence, and turned into a plan card with owners and dates, with a loop arrow back for review.

**Course tile**

```
FILE NAME: images/social-worker-05-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: an open notebook with a circular diagram of blurred segments and a pen. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-05-psychosocial-assessment-og.png (prep script exports images/og/social-worker-05-psychosocial-assessment-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "A Comprehensive Psychosocial Assessment". Subtitle in teal #1a6b72: "Renal Social Worker · Module 5 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: an open notebook with a circular diagram of blurred segments and a pen, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 6: Care Plans, Referrals, and Case Management

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-06-care-plans-and-case-management-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: close desk-level shot, hands only
HUMAN VARIATION: Hands only; skin tone and hand position differ from the previous image
AUDIENCE: Mixed
VISUAL GOAL: A referral is closed by a phone call, not a form.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: close desk-level shot, hands only. Subject: a social worker’s hands on a desk: one hand holding a phone to an unseen ear, the other ticking a printed care-plan grid with columns (only blurred marks, no legible words), a small calendar and a pen beside it, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The referral loop**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-06-the-referral-loop.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Circular workflow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The referral loop". Five stations on a loop: "Sent", "Received and accepted", "Decided", "Delivered", "Confirmed with the person". The first two stations amber with the tag "Action"; the last station green with a check and the tag "Loop closed". A small side card: "Declined, with a reason, also closes the loop." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* A referral sent is an action; an outcome confirmed is the result. Close the loop only on evidence.
*Alt text:* A loop of five stations: referral sent, received and accepted, decision made, outcome delivered, outcome confirmed with the person; the first two stations are marked as actions and the last as the only point where the loop closes.

**Figure B: Goals that belong to the person**  ·  skill `simple-figure`  ·  placed in section `goals`

```
FILE NAME: images/social-worker-06-goals-in-her-words.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Before-and-after comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Goals that belong to the person". Two columns. Left, gray, labeled "Worker’s goal": "Address financial concerns", "Improve compliance". Right, teal, labeled "Her goal": "Stop borrowing to pay for transport by January", "Keep my job and attend all three sessions". A small SMART badge with five letters spelled out: "Specific · Measurable · Achievable · Relevant · Time-bound". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Rewrite the worker’s goal in the person’s words.
*Alt text:* A comparison of weak and strong care plan goals, rewritten in the person’s words with a time.

**Course tile**

```
FILE NAME: images/social-worker-06-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a phone and a printed grid with check marks (blurred) on a desk. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-06-care-plans-and-case-management-og.png (prep script exports images/og/social-worker-06-care-plans-and-case-management-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Care Plans, Referrals, and Case Management". Subtitle in teal #1a6b72: "Renal Social Worker · Module 6 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a phone and a printed grid with check marks (blurred) on a desk, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 7: PhilHealth Navigation and Financial Protection

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-07-philhealth-navigation-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder from the daughter
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Explain the benefit by its rule and date, never by rumor.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder from the daughter. Subject: a Filipina woman in her mid-60s with silver hair in a low bun and a pastel-blue blouse, and her daughter in her 30s with a ponytail and office lanyard (blank card), at a hospital help desk while a male social worker in his 40s with a goatee and a white polo points to a printed sheet (only blurred marks), soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Reading a PhilHealth rule**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-07-reading-a-philhealth-rule.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Three-panel comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Reading a PhilHealth rule". Three vertical panels: "Hemodialysis — PC 2024-0023 — up to 156 sessions a year", "Peritoneal dialysis — PC 2024-0036 — Z Benefits through contracted providers", "Kidney transplant — PC 2026-0019 — published Nov 21, 2026; check effectivity". Over the bottom of all three, a magnifying glass on a date tab: "Check: circular · version · effective date · case date". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Read each benefit rule by its circular number, version, and effective date before you explain it.
*Alt text:* Three benefit pathways side by side for hemodialysis, peritoneal dialysis, and kidney transplant, each with a circular number and a date tab, and a magnifying glass over the date tab labeled check version and effective date.

**Figure B: Four checks before you explain a benefit**  ·  skill `simple-figure`  ·  placed in section `reading`

```
FILE NAME: images/social-worker-07-four-benefit-checks.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Checklist card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Four checks before you explain a benefit". A clean clipboard checklist with four green check boxes: "Which circular and version?", "When did it take effect?", "What is the case date?", "Any transition rules?". Beside it a small amber card: "A social media post is not a source". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Check four things before you explain any benefit.
*Alt text:* A checklist card of four checks before explaining a PhilHealth benefit: current circular and version, effective date, case date, transition rules.

**Course tile**

```
FILE NAME: images/social-worker-07-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a magnifying glass over a calendar date tab on a stack of papers (no legible text). One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-07-philhealth-navigation-og.png (prep script exports images/og/social-worker-07-philhealth-navigation-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "PhilHealth Navigation and Financial Protection". Subtitle in teal #1a6b72: "Renal Social Worker · Module 7 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a magnifying glass over a calendar date tab on a stack of papers (no legible text), softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 8: Assistance Pathways and Resource Mobilization

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-08-assistance-and-resource-mobilization-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: slightly overhead
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: One strong application beats seven thin ones.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: slightly overhead. Subject: a Filipina wife in her early 40s with shoulder-length straight hair and a denim shirt sorting documents into three colored folders on a table at a government hospital assistance desk, a social worker in her 50s with short gray hair and reading glasses helping; folders show only blurred marks, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Mapping assistance**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-08-mapping-assistance.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Radial map with status chips
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Mapping assistance". Center: a simple house icon with a family. Around it five source cards with icons: "DSWD crisis assistance (AICS)", "PCSO Medical Access Program", "Malasakit Center (DOH and designated hospitals)", "Local government", "Employer, SSS or GSIS, community". Each card has a status chip: amber "Submitted", teal "Decided", green "Received". Footer: "Count what reached the household." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Map before you apply. Track each request to its decision and to what actually reached the household.
*Alt text:* A map of assistance sources around a household: DSWD crisis assistance, PCSO medical access, the Malasakit Center desk in a government hospital, the local government office, and employer or community sources, each with a checklist and a status tag reading submitted, decided, or received.

**Course tile**

```
FILE NAME: images/social-worker-08-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: three colored folders (teal, amber, green) neatly stacked. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-08-assistance-and-resource-mobilization-og.png (prep script exports images/og/social-worker-08-assistance-and-resource-mobilization-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Assistance Pathways and Resource Mobilization". Subtitle in teal #1a6b72: "Renal Social Worker · Module 8 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: three colored folders (teal, amber, green) neatly stacked, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 9: Transport, Work, Housing, Food, and Disability Access

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-09-work-transport-and-social-determinants-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: D Panorama
CAMERA: wide-angle, early-morning street level
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Getting to dialysis is a cost the household pays thirteen times a month.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: D Panorama. Camera: wide-angle, early-morning street level. Subject: a Filipino man in his early 50s with a lean face, a faded cap and a windbreaker stepping out of a tricycle at the entrance of a dialysis unit at dawn, his wife paying the driver, a social worker in a light-blue uniform greeting them at the door; soft sunrise light, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The access equation**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-09-the-access-equation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Stacked bar
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The access equation". One tall stacked bar labeled "One dialysis visit" with five segments: "Fare out", "Fare back", "Companion’s fares", "Food", "Companion’s lost wages". An arrow to a row of thirteen small identical bars labeled "× 13 visits a month". A side card: "Gap = total − confirmed support". No peso amounts. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The access equation. Small costs per visit, multiplied by thirteen visits a month, decide whether a person can keep coming.
*Alt text:* A stacked bar showing the cost of one dialysis visit beyond the session itself: fare out, fare back, companion's fare, food, and the companion's lost day of wages, multiplied by thirteen visits a month.

**Figure B: Keeping a livelihood**  ·  skill `simple-figure`  ·  placed in section `work`

```
FILE NAME: images/social-worker-09-keeping-a-livelihood.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Option cards
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Keeping a livelihood". Five rounded option cards with icons and the owner in small text: "Change the dialysis shift — head nurse, nephrologist", "Employer letter (with consent, minimum detail) — employer", "Sickness or disability benefits — SSS or GSIS", "Work that fits treatment — DOLE or local livelihood programs", "Peritoneal dialysis to free daytime — the person and the nephrologist". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Ask about work in the first month.
*Alt text:* Five option cards for keeping work alongside dialysis: shift change, employer letter, SSS or GSIS benefits, new work, peritoneal dialysis to free daytime.

**Course tile**

```
FILE NAME: images/social-worker-09-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a tricycle parked outside a clean clinic entrance at sunrise. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-09-work-transport-and-social-determinants-og.png (prep script exports images/og/social-worker-09-work-transport-and-social-determinants-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Transport, Work, Housing, Food, and Disability Access". Subtitle in teal #1a6b72: "Renal Social Worker · Module 9 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a tricycle parked outside a clean clinic entrance at sunrise, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 10: Distress, Depression, Anxiety, and Stepped Support

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-10-distress-and-mental-health-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: close portrait at the chair, eye level
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Notice, ask, and listen before you score anything.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: close portrait at the chair, eye level. Subject: a Filipino man in his late 50s with a round face, thinning gray hair and a checked shirt, seated in a dialysis recliner looking toward a social worker in her late 20s with a pixie cut and a sage cardigan who sits beside him, listening; the dialysis machine softly blurred, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Stepped psychosocial care**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-10-stepped-psychosocial-care.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Staircase infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Stepped psychosocial care". Four ascending steps: "1 Everyone — listening, information, practical help", "2 Some — structured support, problem solving", "3 Fewer — talking therapy or medicine through the mental health team" (purple), "4 A few — urgent psychiatric care" (red). A thin red lane running alongside all steps labeled "Safety question (item 9) open at every step". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Stepped psychosocial care. Match the help to the need, and keep the safety question open at every step.
*Alt text:* A staircase of four steps: everyone (listening, information, practical help), some (structured support and problem solving), fewer (talking therapy or medicine through the mental health team), and a few (urgent psychiatric care), with a safety lane running beside all steps.

**Figure B: The two-step depression screen**  ·  skill `algorithm-generator-skill (Style Mode C)`  ·  placed in section `screen`

```
FILE NAME: images/social-worker-10-two-step-screen.png
SKILL: williamriveromd-algorithm-generator-skill (Style Mode C)
IMAGE TYPE: Clinical algorithm flowchart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The two-step depression screen". Top: "PHQ-2: little interest? feeling down?". If both "not at all" → teal box "Record a negative screen; rescreen at the agreed interval". If either positive → "Complete the PHQ-9 with the person" → diamond "Item 9 above 0?" YES (red) → "Safety pathway now"; NO → "Total 10 or more: tell the nephrologist; offer support or referral" and "Below 10: support and rescreen". Footer: "A score is a screen, not a diagnosis." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Two questions first, the full PHQ-9 if either is positive, and item 9 every time.
*Alt text:* A flowchart: two PHQ-2 questions, then the full PHQ-9 if either is positive, with item 9 asked in person and a branch to the safety pathway.

**Course tile**

```
FILE NAME: images/social-worker-10-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: an empty dialysis recliner with a folded blanket and a small stool beside it. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-10-distress-and-mental-health-og.png (prep script exports images/og/social-worker-10-distress-and-mental-health-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Distress, Depression, Anxiety, and Stepped Support". Subtitle in teal #1a6b72: "Renal Social Worker · Module 10 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: an empty dialysis recliner with a folded blanket and a small stool beside it, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 11: Immediate Safety, Safeguarding, Violence, and Exploitation

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-11-crisis-and-safeguarding-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: rear three-quarter view of the social worker
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Safety conversations happen in private and at an unhurried pace.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: rear three-quarter view of the social worker. Subject: a calm private consultation room with the door closed; an older Filipina woman with long gray hair in a braid and a cardigan sits with hands folded while a male social worker in his 40s with a shaved head and a navy polo sits angled toward her, leaning in; a box of tissues and a glass of water on a small table, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The safety pathway**  ·  skill `algorithm-generator-skill (Style Mode C)`

```
FILE NAME: images/social-worker-11-the-safety-pathway.png
SKILL: williamriveromd-algorithm-generator-skill (Style Mode C)
IMAGE TYPE: Clinical algorithm flowchart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The safety pathway". Top box: "A signal: 'better off gone', 'want to stop', 'what's the point'". Arrow to diamond: "Ask directly: thoughts of ending your life?". YES branch (red) to stacked boxes: "Stay with the person" → "Make the space safer (with the nurse)" → "Call the attending physician and the crisis route now" → "Warm handover" → "Document exact words, calls, plan". NO or UNSURE branch (teal) to: "Record, tell the nephrologist today, plan follow-up, ask again". Small footer note: "Asking does not plant the idea." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The safety pathway. Ask directly, never leave a person at immediate risk alone, and hand over in person.
*Alt text:* A clinical algorithm: ask directly about thoughts of self-harm; if yes, stay with the person, remove means where possible, call the attending clinician and the unit's crisis route, and document; if no, record and plan follow-up.

**Figure B: Signs of abuse and exploitation**  ·  skill `simple-figure`  ·  placed in section `elder`

```
FILE NAME: images/social-worker-11-signs-of-exploitation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Four-panel reference card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Signs of abuse and exploitation". Four soft panels with simple icons: "Financial — a relative holds the ATM or pension card", "Neglect — weight loss, no food at home, missed medicines", "Physical — a bruise with a changing explanation" (a small bruise on an upper arm, nothing graphic), "Psychological — fear and silence when a relative is present". Footer: "Ask privately. Offer options that keep dialysis going." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Dependence creates vulnerability; ask privately.
*Alt text:* Four panels showing signs of financial exploitation, neglect, physical abuse and psychological abuse in an older person on dialysis.

**Course tile**

```
FILE NAME: images/social-worker-11-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a closed consultation room door with a soft light beneath it. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-11-crisis-and-safeguarding-og.png (prep script exports images/og/social-worker-11-crisis-and-safeguarding-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Immediate Safety, Safeguarding, Violence, and Exploitation". Subtitle in teal #1a6b72: "Renal Social Worker · Module 11 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a closed consultation room door with a soft light beneath it, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 12: Motivational Conversations and Treatment Barriers

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-12-behavior-change-and-treatment-barriers-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: side profile two-shot
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Walk beside the person; do not push.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: side profile two-shot. Subject: a Filipino man in his early 30s with tattooed forearms, a mechanic’s cap turned backward and a gray T-shirt, leaning forward and laughing in a dialysis waiting area with a male social worker in his 30s with curly hair and a white shirt; a wall clock and a backpack, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: OARS in a conversation**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-12-oars-in-a-conversation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Conversation illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "OARS in a conversation". A semi-photoreal social worker and a younger man in a dialysis chair talking. Four speech-bubble icons around them: "Open question", "Affirmation", "Reflection", "Summary". Below, a small balance scale: left pan "Reasons to change", right pan "Reasons to stay the same". Footer: "Draw out his reasons; do not argue for change." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Motivational conversation. Draw out the person's own reasons; do not argue for change on their behalf.
*Alt text:* A social worker and a man in a dialysis chair talking, with four speech-bubble icons labeled open question, affirmation, reflection, and summary, and a small balance scale showing reasons to change and reasons to stay the same.

**Figure B: Change talk and sustain talk**  ·  skill `simple-figure`  ·  placed in section `talk`

```
FILE NAME: images/social-worker-12-change-talk.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison panel
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Change talk and sustain talk". Left column, green, "Change talk": five bubbles "I want…", "I could…", "Because my son…", "I have to…", "I will…". Right column, amber, "Sustain talk": "I cannot lose a day’s pay." Between them a social worker icon with the label "Reflect both; ask for more change talk; never argue". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Strengthen change talk; reflect sustain talk without arguing.
*Alt text:* Two columns of speech bubbles: change talk (desire, ability, reasons, need, commitment) and sustain talk, with the advice to reflect both without arguing.

**Course tile**

```
FILE NAME: images/social-worker-12-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two coffee cups on a small waiting-room table, angled toward each other. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-12-behavior-change-and-treatment-barriers-og.png (prep script exports images/og/social-worker-12-behavior-change-and-treatment-barriers-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Motivational Conversations and Treatment Barriers". Subtitle in teal #1a6b72: "Renal Social Worker · Module 12 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two coffee cups on a small waiting-room table, angled toward each other, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 13: Families, Caregivers, Children, and Changing Life Roles

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-13-family-caregivers-and-life-course-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: environmental portrait, soft window light
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: See the person beside the chair.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: environmental portrait, soft window light. Subject: a tired Filipina caregiver in her mid-50s with graying hair in a loose bun and a faded floral blouse, holding a medicine pouch on her lap in a hospital family room, a social worker in her 40s with a short side-swept bob and a green blouse seated beside her, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Caregiver load and backup**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-13-caregiver-load-and-backup.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Caregiver load and backup". Left: a semi-photoreal Filipina caregiver carrying an overloaded tray of task tiles: "Transport", "Medicines", "Meals", "Money", "Night care", "Her own job". Right: the same tasks spread across three people (the caregiver, a backup relative, the patient himself with "Medicines") on lighter trays. A small scale: "Tasks vs capacity". Footer: "Every essential task has a backup." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Caregiver load. List the tasks, the person's capacity, and the backup before strain becomes collapse.
*Alt text:* A Filipino woman carrying a tray of labeled tasks (transport, medicines, meals, money, night care, her own job) beside a smaller tray held by two backup helpers, with a scale showing tasks against her capacity.

**Figure B: Protecting a young carer**  ·  skill `simple-figure`  ·  placed in section `roles`

```
FILE NAME: images/social-worker-13-young-carer.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Protecting a young carer". Two weekly calendars side by side for a 15-year-old girl (semi-photoreal, school uniform, backpack). Left "Before": two school days crossed out amber with a small dialysis-unit icon. Right "After": all school days green; dialysis-day transport covered by an adult backup icon. Footer: "Protect schooling; move adult tasks to adults." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* A child’s schooling is not a backup plan.
*Alt text:* A teenage girl’s week before and after a caregiver plan: missed school days replaced by adult backup on dialysis days.

**Course tile**

```
FILE NAME: images/social-worker-13-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a medicine pouch and a set of house keys on a family-room chair. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-13-family-caregivers-and-life-course-og.png (prep script exports images/og/social-worker-13-family-caregivers-and-life-course-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Families, Caregivers, Children, and Changing Life Roles". Subtitle in teal #1a6b72: "Renal Social Worker · Module 13 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a medicine pouch and a set of house keys on a family-room chair, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 14: Modality Decisions, Home Therapy, and Practical Feasibility

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-14-modality-and-home-therapy-support-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide-angle, doorway view
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Feasibility is decided in the home, not only in the clinic.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide-angle, doorway view. Subject: a peritoneal dialysis nurse in her 40s with a long ponytail and white scrubs and a social worker in his 30s with a crew cut and a beige polo standing in a modest, clean Filipino home, looking at a corner with a raised shelf; a young woman in office wear shows them the space; no boxes with readable labels, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: What each treatment asks of a household**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-14-what-each-modality-asks-of-a-household.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Three-panel comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "What each treatment asks of a household". Three panels with a small home illustration each: "In-center hemodialysis — travel 3 times a week, a companion"; "Peritoneal dialysis at home — a clean corner, storage for boxes, a trained person, a backup"; "Conservative kidney management — symptom care at home, regular team contact, a family ready". Footer: "Feasibility is a social question too." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* What each modality asks of a household. Feasibility is a social question as much as a medical one.
*Alt text:* Three household panels: in-center hemodialysis (travel three times a week), peritoneal dialysis at home (clean space, storage for boxes of bags, a trained person), and conservative kidney management (symptom care at home with the team), each with a short list of what the household must provide.

**Figure B: Solve before you rule out**  ·  skill `simple-figure`  ·  placed in section `feasible`

```
FILE NAME: images/social-worker-14-solve-before-ruling-out.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Problem-to-solution table
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Solve before you rule out". Five rows, each with an amber finding icon and an arrow to a green solution: "No storage → smaller deliveries, a raised shelf, a relative’s house", "Shared small room → a curtained clean corner", "Floods in heavy rain → supplies stored high, typhoon plan", "Unreliable water → stored clean water and sanitizer", "No helper → train a family member". Footer: "The clinical team decides; you bring solutions." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Treat each home-visit finding as a problem to solve first.
*Alt text:* A table of home peritoneal dialysis findings paired with possible solutions: storage, a shared room, flooding, water, no helper.

**Course tile**

```
FILE NAME: images/social-worker-14-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a raised clean shelf in a modest home corner with a curtain partly drawn. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-14-modality-and-home-therapy-support-og.png (prep script exports images/og/social-worker-14-modality-and-home-therapy-support-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Modality Decisions, Home Therapy, and Practical Feasibility". Subtitle in teal #1a6b72: "Renal Social Worker · Module 14 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a raised clean shelf in a modest home corner with a curtain partly drawn, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 15: Transplant Access, Psychosocial Preparation, and Donor Protection

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-15-transplant-psychosocial-and-donor-protection-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: eye-level, across a small table
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: The donor is seen alone, and free to say no.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: eye-level, across a small table. Subject: a Filipino man in his mid-20s with a lean build, a short fade haircut and a plain dark-green shirt, seated alone across from a female social worker in her 40s with chin-length hair and a gray blazer in a small private room with the door closed, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The donor's separate path**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-15-the-donors-separate-path.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Two-pathway diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The donor's separate path". Two parallel paths: teal "Transplant candidate" and violet "Living donor", each passing a private interview room icon and its own team member icon, meeting only at "Operation". On the donor path, an open green door labeled "Withdraw safely at any time". A small lock icon on the donor path: "Separate record". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The donor's separate path. Private interviews, their own advocate, and a safe way to stop at any point.
*Alt text:* Two separate pathways, teal for the transplant candidate and violet for the living donor, each with its own private interview room and its own team member, meeting only at the operation, with an exit door on the donor's path labeled withdraw safely.

**Figure B: Signals to route, not to judge**  ·  skill `simple-figure`  ·  placed in section `coercion`

```
FILE NAME: images/social-worker-15-donor-signals.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Reference card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Signals to route, not to judge". A clean card with five amber rows and small icons: "Knows little about the recipient’s family", "Promised money, a job or a business", "Recent arrival; housing paid by the recipient’s family", "Hurry; rehearsed answers; a third party always present", "In debt or crisis". A purple arrow at the bottom: "Report to the donor advocate and ethics committee; do not confront the family". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* A signal is not proof; route it through the protected pathway.
*Alt text:* A card listing signals of possible donor inducement or a false relationship, with the instruction to route them through the protected pathway.

**Course tile**

```
FILE NAME: images/social-worker-15-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two separate doors in a bright corridor, one slightly open. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-15-transplant-psychosocial-and-donor-protection-og.png (prep script exports images/og/social-worker-15-transplant-psychosocial-and-donor-protection-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Transplant Access, Psychosocial Preparation, and Donor Protection". Subtitle in teal #1a6b72: "Renal Social Worker · Module 15 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two separate doors in a bright corridor, one slightly open, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 16: Supportive Care, Treatment Decisions, Grief, and Bereavement

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-16-supportive-care-grief-and-bereavement-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: slightly high wide shot
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Advance care planning is a conversation, not a form.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: slightly high wide shot. Subject: a family meeting around a small round table: an 81-year-old Filipino retired fisherman with deep sun lines and a white cotton shirt, his wife with silver hair, their daughter in her 40s, a nephrologist in a white coat and a social worker; a laptop shows a blurred video call; a window with soft sea-blue light, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Advance care planning**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-16-advance-care-planning-conversation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Conversation card illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Advance care planning". A semi-photoreal family meeting at a small table (older man, wife, daughter, nephrologist, social worker). Above the table, one simple card with three lines: "What matters most?", "Who will speak for me?", "What do I want if I get sicker?". A small circular arrow icon: "Revisit when things change". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Advance care planning is a series of conversations about what matters most and who speaks for the person.
*Alt text:* A family meeting around a small table: an older man with kidney failure, his wife and adult daughter, a nephrologist, and a social worker, with a simple card showing what matters most, who will speak for me, and what I want if I get sicker.

**Figure B: Bereavement follow-up**  ·  skill `simple-figure`  ·  placed in section `grief`

```
FILE NAME: images/social-worker-16-bereavement-follow-up.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Bereavement follow-up". A gentle horizontal timeline with four soft markers: "At the death — documents, the wake", "First weeks — a call or card", "3 to 6 months — a check-in", "Grief not easing → referral to the mental health team". A small candle icon at the start. Calm pastel tones. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Stay with the family after a death.
*Alt text:* A timeline of bereavement contacts after a death: practical help at the death, a call in the first weeks, a check-in at three to six months, referral if grief does not ease.

**Course tile**

```
FILE NAME: images/social-worker-16-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a small round table with four chairs and a cup of tea near a window with sea-blue light. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-16-supportive-care-grief-and-bereavement-og.png (prep script exports images/og/social-worker-16-supportive-care-grief-and-bereavement-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Supportive Care, Treatment Decisions, Grief, and Bereavement". Subtitle in teal #1a6b72: "Renal Social Worker · Module 16 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a small round table with four chairs and a cup of tea near a window with sea-blue light, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 17: Transfers, Disasters, and Continuity of Care

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-17-transfers-disasters-and-continuity-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: D Panorama
CAMERA: wide-angle through a rain-streaked window
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Continuity means every patient dialyzed somewhere, even in a typhoon.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: D Panorama. Camera: wide-angle through a rain-streaked window. Subject: a female social worker in her 30s with a high bun and a navy rain jacket on the phone at a dialysis unit desk during heavy rain, a printed checklist in hand; through the window, flooded street and swaying palm trees in soft gray light, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Continuity in a typhoon**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-17-continuity-in-a-typhoon.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Workflow map
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Continuity in a typhoon". A simple map strip of a Philippine coastline with a typhoon symbol. Left: "Home unit — closed" with an amber flood icon. Right: "Receiving unit — open". Between them a handoff arrow carrying a folder labeled "Order · serologies · medicines · contacts". At the receiving end a green check: "Arrival confirmed". A side card: "Not confirmed in 2 days → trace and alert the nephrologist". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Continuity of care. A transfer closes only when the receiving unit confirms the patient arrived and was treated.
*Alt text:* A Philippine map strip with a typhoon symbol, a home dialysis unit and a receiving unit in another town, linked by a handoff arrow carrying a folder with dialysis order, serologies, medicines, and contacts, and a check mark at the receiving end labeled arrival confirmed.

**Figure B: The personal emergency plan**  ·  skill `simple-figure`  ·  placed in section `prepare`

```
FILE NAME: images/social-worker-17-personal-emergency-plan.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Checklist card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "The personal emergency plan". A laminated-looking card with a small umbrella icon and five rows: "Two other units (name, address, number)", "Two contacts and a neighbor", "Bring: dialysis order, serologies, medicine list, PhilHealth details, ID", "Emergency diet advice from the dietitian", "A few days of medicines, kept dry". All fields blank lines only. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Every patient has a written plan before the rainy season.
*Alt text:* A personal dialysis emergency plan card: two alternative units, contacts, documents to bring, emergency diet advice, medicines.

**Course tile**

```
FILE NAME: images/social-worker-17-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a rain-streaked window with a phone and a checklist on the sill. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-17-transfers-disasters-and-continuity-og.png (prep script exports images/og/social-worker-17-transfers-disasters-and-continuity-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Transfers, Disasters, and Continuity of Care". Subtitle in teal #1a6b72: "Renal Social Worker · Module 17 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a rain-streaked window with a phone and a checklist on the sill, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 18: Documentation, Privacy, Telehealth, and Digital Boundaries

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-18-documentation-privacy-and-digital-practice-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: three-quarter desk view
HUMAN VARIATION: No people
AUDIENCE: Mixed
VISUAL GOAL: Least information, right recipient, documented reason.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: three-quarter desk view. Subject: a secure office workstation: a monitor with a privacy screen showing only blurred shapes, a closed folder with a small lock icon, a phone placed face down, and a pen on a notepad with blurred marks; soft daylight on a clean desk, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Minimum necessary disclosure**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-18-minimum-necessary-disclosure.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Funnel diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Minimum necessary disclosure". A funnel: top "Full record", narrowing through three filters labeled "Purpose", "Lawful basis", "Minimum needed", to a small output card "What this recipient needs". A lock icon on the side: "Approved channel". A small log card: "Who · what · why · when". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Least information, right recipient, documented reason.
*Alt text:* A funnel: the full chart at the top, narrowing to only the facts the recipient needs for the stated purpose, with a lock icon, the lawful basis, and a log entry of who received what and why.

**Figure B: Releasing information**  ·  skill `algorithm-generator-skill (Style Mode C)`  ·  placed in section `release`

```
FILE NAME: images/social-worker-18-release-decision.png
SKILL: williamriveromd-algorithm-generator-skill (Style Mode C)
IMAGE TYPE: Decision flowchart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "Releasing information". Top: "Request for information". Four stacked diamonds: "Who is asking?", "Why (purpose)?", "On what lawful basis?", "What is the minimum needed?". If any answer is unclear → amber "Route to the records officer or DPO". If all clear → green "Release the minimum, record who, what, why, when". Side note: "Spouse or relative ≠ authorization". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* A relationship is not authorization.
*Alt text:* A decision flow for a release request: who is asking, why, on what basis, what is the minimum, and record the release; a relationship alone is not authorization.

**Course tile**

```
FILE NAME: images/social-worker-18-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a locked folder and a phone placed face down on a clean desk. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-18-documentation-privacy-and-digital-practice-og.png (prep script exports images/og/social-worker-18-documentation-privacy-and-digital-practice-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Documentation, Privacy, Telehealth, and Digital Boundaries". Subtitle in teal #1a6b72: "Renal Social Worker · Module 18 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a locked folder and a phone placed face down on a clean desk, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 19: Quality Improvement, Supervision, and Workload

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-19-quality-supervision-and-workload-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder at a monitor
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Measure what matters, and think it through in supervision.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder at a monitor. Subject: a social worker in her late 20s with long straight hair and a plum blouse and her supervisor, a Filipina in her 60s with short silver hair and glasses, reviewing a simple run chart (line with dots, no legible numbers) on a monitor in a small office, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: A measure that means something**  ·  skill `simple-figure`

```
FILE NAME: images/social-worker-19-a-measure-that-means-something.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Measure card and run chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "A measure that means something". Left: a measure card with "Numerator: referrals with a confirmed outcome" over "Denominator: eligible referrals", "Period: month", and the worked line "10 / 12 = 83.3%". Right: a simple run chart of monthly dots with a dashed median line (no other numbers). Below: a note card "What it cannot show: whether the outcome helped". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* A measure that means something: a defined numerator, a defined denominator, a trend over time, and its limits stated.
*Alt text:* A measure card showing a numerator (referrals with a confirmed outcome) over a denominator (eligible referrals), a run chart of the monthly rate with a median line, and a note card listing what the measure cannot show.

**Course tile**

```
FILE NAME: images/social-worker-19-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a printed run chart (dots and a dashed line, no numbers) on a clipboard. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-19-quality-supervision-and-workload-og.png (prep script exports images/og/social-worker-19-quality-supervision-and-workload-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Quality Improvement, Supervision, and Workload". Subtitle in teal #1a6b72: "Renal Social Worker · Module 19 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a printed run chart (dots and a dashed line, no numbers) on a clipboard, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 20: Integrated Case Conference and Readiness for Practice

**Hero (circular vignette)**

```
FILE NAME: images/social-worker-20-integrated-case-and-readiness-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide-angle conference room
HUMAN VARIATION: Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: One family, one plan, every owner named.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide-angle conference room. Subject: a multidisciplinary case conference: a male social worker in his 40s with a neat mustache and a light-blue barong-style shirt points to a whiteboard timeline of colored blocks (no writing) while a nephrologist, a nurse and a dietitian listen around a table, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, distressing or tearful close-ups.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: One family, start to finish**  ·  skill `infographic-skill`

```
FILE NAME: images/social-worker-20-one-family-start-to-finish.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Horizontal timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "One family, start to finish". A horizontal timeline January to December with nine milestones as small icons: "Emergency start", "Missed sessions (fares)", "Depression screen", "Caregiver plan", "Session balance alert", "Typhoon transfer", "Peritoneal dialysis question", "Transplant and donor question", "Case conference". A small social worker figure appears under each milestone. No dates beyond month names. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* One family, start to finish. The integrated case brings every module together.
*Alt text:* A horizontal timeline of one fictional family across a year: referral, assessment, benefit navigation, depression screen, caregiver plan, modality discussion, transplant referral, typhoon transfer, and a case conference, with the social worker present at each point.

**Figure B: A five-minute case presentation**  ·  skill `simple-figure`  ·  placed in section `conference`

```
FILE NAME: images/social-worker-20-five-minute-presentation.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Social workers and the kidney care team

PROMPT:
Title at top in bold navy: "A five-minute case presentation". Five numbered blocks left to right with a small clock icon "5 minutes": "1 Who and what matters (in their words)", "2 Formulation", "3 What has been done", "4 Current risks", "5 Requests: person · decision · date". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, Filipino patients, families and staff. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Open with the person’s goal; close with requests to named people.
*Alt text:* Five steps of a case presentation: the person’s goal, formulation, what has been done, current risks, specific requests.

**Course tile**

```
FILE NAME: images/social-worker-20-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a whiteboard with colored blocks in a row (no writing) and markers on the ledge. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/social-worker-20-integrated-case-and-readiness-og.png (prep script exports images/og/social-worker-20-integrated-case-and-readiness-og.jpg 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Social workers and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in renal green #2e6b3e with white text "RENAL CARE ACADEMY · ANCILLARY STAFF TRACK". Title in bold navy #0f1e2e, three lines at most: "Integrated Case Conference and Readiness for Practice". Subtitle in teal #1a6b72: "Renal Social Worker · Module 20 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a whiteboard with colored blocks in a row (no writing) and markers on the ledge, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

## 7. Audit checklist before publishing

- [ ] Every label spelled exactly as in the prompt (compare letter by letter; GPT often misspells).
- [ ] No number on an image that is not in its prompt.
- [ ] No legible names, ID numbers, documents, or screens; no self-harm imagery.
- [ ] Heroes: circle with white margin, title-safe zone empty, a different cast from the previous hero, no text.
- [ ] Figures and OG cards: light background, Inter, © renalcarematters.com bottom-right.
- [ ] OG cards: text only in the left 55%, nothing important outside the 1.91:1 band.
- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.
