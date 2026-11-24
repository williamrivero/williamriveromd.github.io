# Dialyzer Reprocessing Technician — Image Plan Blueprint and GPT Prompt Pack

Renal Care Academy · prepared November 25, 2026 · 13 heroes + 24 teaching figures + 2 derived assets

## 1. Purpose

Every image in this track does one of three jobs:

- **Understanding** — make an invisible mechanism visible (open versus clotted fibers, layered germicide, reverse ultrafiltration, the usable window).
- **Application** — turn a rule into something a technician can picture at the bench (ten padlocks, five uses not five reuses, the two-person handoff, the trace-back window).
- **Appreciation** — show the people and the stakes: a real Filipino reuse room, a patient at the chair, the team around one dialyzer.

## 2. House rules applied

| Rule | Source skill | Applied as |
|---|---|---|
| Circular vignette heroes, 2048 × 2048, white border, 20–25% title-safe zone, **no text**, rotating archetype, camera and people | `williamriveromd-hero-vignette` v3 | H00–H12; archetypes and cameras never repeat back to back; men and women, ages 20s–60s, varied builds and attire; three people-free heroes |
| Light backgrounds only; Inter typeface; attribution `renalcarematters.com` bottom-right at 70% navy | `williamriveromd-infographic-skill` v5 | All RT figures |
| Dialyzer anatomy: two end blood ports, two side dialysate ports near opposite ends, countercurrent flow | Infographic skill, hemofilter reference anatomy | Stated in every hero and every dialyzer figure |
| No invented numbers | Infographic skill; medical-teaching-standard | Only verified, cited numbers appear (80% TCV, 5 uses, 10 mg/L TDS, ISO 100 CFU/mL and 0.25 EU/mL, 1.4% vs 3.5% from the 1988 CDC case, HEMO 1–2% per 10 reuses). No germicide concentrations, contact times or storage limits anywhere |
| Algorithm style for decision flows | `williamriveromd-algorithm-generator-skill` | RT-11B |
| Attribution for public Academy images | Memory preference | `renalcarematters.com` (patient-specific documents use williamriveromd.com; not applicable here) |
| American English in rendered text | `american-english` | All labels |

## 3. Production workflow

1. Paste each prompt into ChatGPT image generation (current GPT image model). Generate at the stated size.
2. Save PNGs to `/Volumes/Storage/Renal Care Academy/Reprocessing Technician/images/` for audit.
3. Convert to WebP and place in `images/` of the site repo with the **same base name** (`.webp` for figures; heroes as both `.png` and `.webp`). The generator reads the file names in `tools/techcourses/reprocessing_tech/figs.py`; pages show an empty slot until the file exists.
4. Card thumbnails (`dialyzer-reprocessing-technician-card.webp`, `dialyzer-reprocessing-technician-NN-card.webp`, 640 × 360) are cut from the heroes with `tools/techcourses/prep_assets.py`. The landing image `images/academy/landing/dialyzer-reprocessing-technician.webp` (960 × 540) is cut from H00.
5. Re-run `python3 generate_tech_courses.py --course reprocessing_tech --patch`.
6. QA each image: correct dialyzer anatomy, no legible names or IDs, no invented numbers, attribution present (figures), no text (heroes), light background, Inter only, American spelling.

## 4. Image map

| Module | Hero | Figure A | Figure B |
|---|---|---|---|
| Track hub | H00 | — | — |
| 01 | H01 | RT-01A The life of a reused dialyzer | RT-01B Who decides what |
| 02 | H02 | RT-02A Open versus clotted fibers | RT-02B What the evidence shows |
| 03 | H03 | RT-03A The strictest rule wins | RT-03B Five uses, not five reuses |
| 04 | H04 | RT-04A Clean and dirty flow | RT-04B Protective equipment |
| 05 | H05 | RT-05A Water to the reuse outlet | RT-05B Limit and action level |
| 06 | H06 | RT-06A Poor mixing layers | RT-06B Germicide comparison |
| 07 | H07 | RT-07A Anatomy of a label | RT-07B Chain of custody |
| 08 | H08 | RT-08A Time to processing | RT-08B Rinse and reverse ultrafiltration |
| 09 | H09 | RT-09A Measuring total cell volume | RT-09B Every gate must pass |
| 10 | H10 | RT-10A Fill, contact, storage, expiry | RT-10B Two-person handoff |
| 11 | H11 | RT-11A Tracing back after a fault | RT-11B Incident decision flow |
| 12 | H12 | RT-12A Reading the room's numbers | RT-12B What a record proves |

## 5. Heroes

### H00 · Track hub
FILE NAME: dialyzer-reprocessing-technician-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: A Editorial Portrait. Camera: environmental portrait, eye level.
Subject: a Filipino reprocessing technician in her early thirties with hair tied back under a bouffant cap, a slim build, light-blue fluid-resistant gown, nitrile gloves and a clear face shield, holding a reprocessed hollow-fiber dialyzer at chest height and reading its blank patient label; behind her, softly out of focus, an automated dialyzer reprocessor and a rack of individually labeled storage slots; through a glass door, a hint of the dialysis floor, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H01 · Module 1 · The reuse room and your place in it
FILE NAME: dialyzer-reprocessing-technician-01-role-scope-and-the-team-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide-angle from the doorway.
Subject: at the threshold between a small reuse room and the dialysis floor, a stocky Filipino reprocessing technician in his forties with a shaved head and a navy scrub top under a gown hands a capped, labeled dialyzer in a clear tray to a young Filipina dialysis nurse with a short bob in white scrubs; a head nurse in her fifties with reading glasses watches from the nurses' station in the background, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H02 · Module 2 · The dialyzer and why reuse exists
FILE NAME: dialyzer-reprocessing-technician-02-dialyzer-science-and-evidence-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: I Object Hero. Camera: low-angle macro, three-quarter view.
Subject: no people; a single hollow-fiber dialyzer standing upright on a white laboratory bench, one half of its housing cut away to reveal thousands of fine parallel fibers, a few fibers in the cutaway faintly darkened with clot, morning light raking across the fiber bundle; a small magnifying glass and a folded journal reprint (text illegible) beside it, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H03 · Module 3 · The rules
FILE NAME: dialyzer-reprocessing-technician-03-rules-and-jurisdictions-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder.
Subject: over the shoulder of a Filipino medical director in his sixties with silver hair and a white coat, a Filipina reprocessing technician in her late twenties with a long braid and rectangular glasses points to a printed binder of regulations with colored tabs (text illegible) on a small desk; a labeled dialyzer and a germicide instruction leaflet lie beside the binder, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H04 · Module 4 · Infection prevention and protecting yourself
FILE NAME: dialyzer-reprocessing-technician-04-infection-and-occupational-protection-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: A Editorial Portrait. Camera: close portrait, slight side angle.
Subject: a Filipino reprocessing technician in his mid-twenties with short curly hair, a lean build, a fluid-resistant yellow gown, double nitrile gloves, a surgical mask and a clear face shield firmly down, rinsing a used dialyzer at a deep stainless sink with a gentle spray directed away from his face; a wall-mounted eye wash station and a hand hygiene dispenser visible at the edge of the frame, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H05 · Module 5 · Water for reprocessing
FILE NAME: dialyzer-reprocessing-technician-05-water-for-reprocessing-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: D Panorama. Camera: side profile, medium wide.
Subject: a Filipina technician in her forties with a short pixie cut and a teal scrub top under a gown fills a sterile sample bottle at a clearly marked stainless water outlet on the reuse-room wall; through a large window behind her, softly out of focus, the water treatment room with reverse-osmosis vessels and blue distribution piping, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H06 · Module 6 · Germicides and chemical safety
FILE NAME: dialyzer-reprocessing-technician-06-germicides-and-chemical-safety-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H Clinical. Camera: hands-and-forearms close-up, overhead three-quarter.
Subject: the gloved hands of a technician in chemical-resistant gloves and gown sleeves dipping a germicide potency test strip into a freshly mixed, clear solution in a graduated container under a stainless local-exhaust ventilation hood; safety goggles, a capped concentrate bottle with an unreadable label, and a safety data sheet binder at the edges, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H07 · Module 7 · Identity and chain of custody
FILE NAME: dialyzer-reprocessing-technician-07-identity-and-chain-of-custody-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: I Object Hero. Camera: top-down.
Subject: no people; top-down view of two identical reprocessed hollow-fiber dialyzers lying side by side on a pale teal tray, each with a white patient label whose writing is blurred, one label marked with a small colored name-alert dot; a printed checklist (illegible) and a pen beside them, generous empty tray surface on one side, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H08 · Module 8 · Receiving, rinsing and cleaning
FILE NAME: dialyzer-reprocessing-technician-08-receiving-and-cleaning-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: J Environmental Storytelling. Camera: medium shot from slightly behind.
Subject: an older Filipino reprocessing technician in his late fifties with a gray mustache, a sturdy build, gown, gloves and face shield connects a used dialyzer to the ports of an automated reprocessor; beside him a small stainless refrigerator with a temperature log clipboard and a covered transport tray of used dialyzers, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H09 · Module 9 · Performance testing and acceptance
FILE NAME: dialyzer-reprocessing-technician-09-testing-and-acceptance-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: G Infographic. Camera: close environmental, eye level with the screen.
Subject: a Filipina reprocessing technician in her thirties with shoulder-length wavy hair in a hairnet, gown and gloves, studies the screen of an automated reprocessor showing a simple volume bar and a pressure-hold curve (no readable digits), a dialyzer mounted vertically on the machine beside the screen, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H10 · Module 10 · Disinfect, store, rinse and hand off
FILE NAME: dialyzer-reprocessing-technician-10-disinfection-storage-and-handoff-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H Clinical. Camera: rear three-quarter view.
Subject: at a dialysis chair, a Filipino male nurse in his forties with a crew cut in navy scrubs and a Filipina reprocessing technician in her twenties in a gown read a dialyzer label together against a seated elderly Filipina patient's wristband (text blurred); on the tray, a residual test strip and a small digital timer, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H11 · Module 11 · Machines, faults and when things go wrong
FILE NAME: dialyzer-reprocessing-technician-11-equipment-incidents-and-continuity-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H Clinical. Camera: two-shot, eye level.
Subject: a Filipino biomedical technician in his thirties with a goatee, a gray work polo and an ID lanyard (text blurred) holds a calibrated reference pressure gauge beside an automated reprocessor while a Filipina reprocessing technician in her fifties with short gray hair and glasses compares readings on a clipboard; a red-bordered blank tag hangs on the machine, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

### H12 · Module 12 · Records, quality and the capstone
FILE NAME: dialyzer-reprocessing-technician-12-records-quality-and-capstone-vignette-hero.png · SIZE: 2048 × 2048
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: E Lifestyle. Camera: environmental portrait, seated.
Subject: in a bright small office next to the reuse room, a Filipina head nurse in her fifties with a neat bun and a Filipino reprocessing technician in his thirties with a side part review a simple bar chart on a laptop (no readable numbers) and a stack of processing logs (writing illegible); a potted plant and a window with daylight, in a clean, bright, modern Philippine hemodialysis unit reuse room with white walls and stainless steel, soft natural daylight and gentle shallow depth of field.
Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall, or blurred background (no faces, objects, icons, or callouts inside that zone).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Any dialyzer shown is anatomically correct: a clear cylindrical housing packed with fine parallel hollow fibers, one blood port at each end cap (red-capped arterial end, blue-capped venous end), and two side ports on the housing for dialysis fluid near opposite ends.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark. Any labels, logs, screens, ID cards, or folders must show only blurred or illegible marks; no real names, numbers, or identifiers.
Avoid: busy layouts, collage overload, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, dark or charcoal backgrounds, cartoon style, neon, HDR, oversaturation, distorted hands or faces, gloves missing during blood or chemical handling.
```

## 6. Teaching figures

### RT-01A · The life of a reused dialyzer
FILE NAME: dialyzer-reprocessing-technician-01-life-of-a-reused-dialyzer.png · ARCHETYPE: Circular workflow · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 1 · big picture
PURPOSE: Show the whole cycle once so every later module has a place on the map.
```
Circular workflow infographic on white #ffffff, Inter labels, landscape. Center: a semi-photoreal 3D hollow-fiber dialyzer (clear housing, visible fiber bundle, red-capped arterial end port, blue-capped venous end port, two side dialysate ports). Around it, eight rounded teal cards joined by clockwise navy arrows: "Treatment", "Transport (covered tray)", "Receiving: identity · eligibility · time", "Rinse and clean", "Test: volume · integrity · inspection", "Disinfect and store", "Rinse + residual test", "Two-person handoff". From every card, a thin red dashed arrow leads outward to a small red circle labeled "Discard". Bottom banner on light teal tint, navy text: "If you cannot prove it, do not release it."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-01B · Who decides what
FILE NAME: dialyzer-reprocessing-technician-01-who-decides-what.png · ARCHETYPE: Radial role map · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 1 · Who decides
PURPOSE: Make ownership of each decision visible so a technician can stop a dialyzer without arguing.
```
Radial infographic on off-white #fafafa, Inter. Center: a dialyzer on a shelf inside an amber dashed box labeled "Quarantine". Five rounded cards around it, each with a small photoreal Filipino staff portrait (faces natural, no names): navy card "Medical director — program and eligibility"; teal card "Nurse — use on the patient"; green card "Reprocessing technician — proves each gate"; gray card "Biomedical technician — equipment fitness"; purple-tinted card "Infection prevention — contamination response". Thin leader lines from each card to the center. Footer line: "Disagree? Quarantine first. Decide in writing."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-02A · Open versus clotted fibers
FILE NAME: dialyzer-reprocessing-technician-02-open-versus-clotted-fibers.png · ARCHETYPE: Mechanism poster · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 2 · What reuse does to the dose
PURPOSE: Connect clotting to falling TCV and lower clearance.
```
Landscape mechanism figure on white, Inter. Left: semi-photoreal 3D dialyzer in longitudinal cutaway; blood (red) entering the arterial end and flowing inside the fibers, dialysis fluid (pale blue) flowing outside the fibers in the opposite direction (countercurrent arrows), side ports correctly placed near opposite ends. A dashed magnifier circle on the fiber bundle opens to the right panel: a cross-section of about 30 fibers, most open with small purple urea dots crossing the walls outward, about 6 blocked by dark red clot and a few lined with a thin yellow protein coat. Far right: a simple vertical gauge labeled "Total cell volume (TCV)" with a falling marker and the caption "Fewer open fibers → less surface → less clearance". No numbers on the gauge.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-02B · What the evidence shows
FILE NAME: dialyzer-reprocessing-technician-02-what-the-evidence-shows.png · ARCHETYPE: Evidence ladder · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 2 · Does reuse change how patients do?
PURPOSE: Teach calibrated certainty and why execution is the technician's territory.
```
Landscape infographic on off-white, Inter. Left two-thirds: a four-rung ladder in navy outline. Rungs from top: "Established physiology — clotting closes fibers; germicides alter membranes"; "Measured in trials — urea clearance falls ~1–2% per 10 reuses (HEMO)"; "Associations — no consistent mortality difference (review of 14 studies); stopping PAA reuse associated with lower risk (before–after)"; "Hypotheses — more reuse may erode high-flux benefit". Each rung has a small teal certainty chip. Right third: a separate red-bordered panel titled "Documented harm: execution failures" with three icon rows: "Poorly mixed germicide → bacteremia", "Contaminated water → pyrogenic reactions", "Breaches → hepatitis C transmission". Bottom banner: "Weak evidence on outcomes. Strong evidence that sloppy reuse hurts."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-03A · The strictest rule wins
FILE NAME: dialyzer-reprocessing-technician-03-strictest-rule-wins.png · ARCHETYPE: Layered stack · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 3 · Which rulebook
PURPOSE: Show how several rulebooks apply at once.
```
Landscape infographic on white, Inter. Five translucent horizontal layers stacked above a single dialyzer, each a rounded band with an icon and one line: navy "Law and licensing — DOH AO 2012-0001 · AO 2013-0003"; green "Payer — PhilHealth PC 2024-0023 · 2024-0029"; purple-tinted "Professional guidance — PSN 2024"; teal "Instructions for use — dialyzer · germicide · reprocessor"; gray "Unit SOP — signed by the medical director". A thick amber arrow descends through all layers to the dialyzer with the label "Apply the strictest rule that applies". Small side note card: "Rules conflict or unclear → HOLD".
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-03B · Five uses, not five reuses
FILE NAME: dialyzer-reprocessing-technician-03-five-uses-not-five-reuses.png · ARCHETYPE: Timeline · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 3 · Counting uses
PURPOSE: Prevent the five-uses versus five-reuses error.
```
Horizontal timeline on off-white, Inter. Six dialysis-chair icons left to right labeled "Use 1 (new)", "Use 2", "Use 3", "Use 4", "Use 5", "Use 6". Between consecutive chairs, small circular reprocessing icons labeled "Reprocess 1" to "Reprocess 4" (between uses 1–5) and a fifth reprocessing icon before use 6 shown grayed. Use 6 is crossed out with a bold red X and the caption "Never eligible — even with a passing volume test". Above the first five chairs a green bracket: "Up to 5 total uses (PhilHealth package ceiling); a lower IFU or SOP limit applies first". Small note under the timeline: "A repeated processing cycle is not a use."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-04A · Clean and dirty flow
FILE NAME: dialyzer-reprocessing-technician-04-clean-and-dirty-flow.png · ARCHETYPE: Floor plan · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 4 · Clean and dirty flow
PURPOSE: Make one-way flow concrete.
```
Clean isometric floor plan of a small reuse room on white, Inter labels, semi-photoreal 3D fixtures. A one-way path of teal floor arrows: entry door from the floor → amber-tinted "Dirty receiving sink" zone → "Reprocessor" → green-tinted "Clean labeled storage" racks → separate exit door. Marked icons: "Hand hygiene" at the exit, "Eye wash" beside the sink, "Ventilation" arrows above the reprocessor, "Used-dialyzer refrigerator" in the dirty zone. A red crossed-out icon of a medicine tray and a cup with the label "No medicine preparation, food or drink". Banner: "Dirty in, clean out, never crossing."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-04B · Protective equipment
FILE NAME: dialyzer-reprocessing-technician-04-protective-equipment.png · ARCHETYPE: Annotated figure · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 4 · Protective equipment
PURPOSE: Teach correct PPE and its failure points.
```
Landscape figure on off-white, Inter. Center: a photoreal Filipina reprocessing technician, standing, in fluid-resistant gown, nitrile gloves, mask, clear face shield down, closed shoes, at a stainless sink. Five callout lines to her equipment: "Face shield down — splashes you do not expect", "Mask", "Fluid-resistant gown, closed at the back", "Chemical-compatible gloves — change between dirty and clean", "Closed shoes". Right side, three small risk cards with icons: "Splash", "Vapor", "Sharps". Bottom-left inset: eye wash station with "Flush first, report second, record third".
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-05A · Water to the reuse outlet
FILE NAME: dialyzer-reprocessing-technician-05-water-to-the-reuse-outlet.png · ARCHETYPE: Process diagram · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 5 · The water path
PURPOSE: Locate the reuse outlet in the water system and its sampling points.
```
Left-to-right process diagram on white, Inter, semi-photoreal 3D components: feed water tap → multimedia filter → softener → carbon tanks → reverse osmosis unit → storage tank → blue distribution loop with arrows → branch to a labeled stainless "Reprocessing outlet" feeding a small reprocessor icon, and a branch to two dialysis machines. Small droplet sampling markers: purple "Microbiology + endotoxin" at raw water, RO product and the reprocessing outlet; teal "Chemical analysis" at the point of use; green "Weekly TDS" at RO product. A small amber note at a pipe stub: "Dead leg → biofilm". Banner: "The reuse outlet is a point of use."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-05B · Limit and action level
FILE NAME: dialyzer-reprocessing-technician-05-limit-and-action-level.png · ARCHETYPE: Gauge · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 5 · Monitoring and limits
PURPOSE: Teach acting at the action level.
```
Landscape infographic on off-white, Inter. Left: a tall vertical thermometer-style gauge with three bands: green bottom "Below action level — continue routine monitoring", amber middle "At or above action level — investigate and correct now", red top "Above maximum limit — stop per program and escalate". A thin dashed line marks "Action level" and a solid line "Maximum". Right: two small cards: "ISO 23500-3 dialysis water: maximum 100 CFU/mL · 0.25 EU/mL; action levels usually half" and "DOH AO 2013-0003: weekly product-water TDS; corrective action above 10 mg/L". Footer: "Check figures against the edition your facility follows."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-06A · Poor mixing layers
FILE NAME: dialyzer-reprocessing-technician-06-poor-mixing-layers.png · ARCHETYPE: Side-by-side comparison · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 6 · Mixing and potency
PURPOSE: Make the invisible danger of layering visible.
```
Two-panel comparison on white, Inter. Left panel, amber header "Not mixed": a clear graduated container of diluted germicide showing a pale layer at the top and a denser, slightly tinted layer at the bottom, with two arrows: top "1.4%", bottom "3.5%" and a caption "Same container, different strength (CDC investigation, 1988)"; three dialyzers filled from different heights with small red, amber and green dots. Right panel, green header "Mixed and tested": a uniform clear solution, a gloved hand holding a potency test strip showing a pass color, dialyzers with green dots. Bottom banner: "Arithmetic predicts the strength. Only the potency test proves it."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-06B · Germicide comparison
FILE NAME: dialyzer-reprocessing-technician-06-germicide-comparison.png · ARCHETYPE: Reference card · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 6 · How germicides kill
PURPOSE: Compare germicides without implying universal settings.
```
Four-column reference card on off-white, Inter, each column with a small 3D icon at the top: "Peracetic acid mixture" (oxidizer icon), "Formaldehyde", "Glutaraldehyde", "Heat with citric acid" (thermometer). Rows: "How it kills" (oxidizes proteins / cross-links proteins / cross-links proteins / heat denatures), "Main staff hazard" (airway and eye irritant, corrosive / irritant, carcinogen, sensitizer / strong sensitizer, asthma / burns), "Before treatment" (residual test / residual test / residual test / cooling and method checks). Footer strip: "Concentration and contact time: from the product IFU and validated SOP only." No concentration numbers anywhere.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-07A · Anatomy of a label
FILE NAME: dialyzer-reprocessing-technician-07-anatomy-of-a-label.png · ARCHETYPE: Annotated object · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 7 · The label
PURPOSE: Teach what a label carries and when it fails.
```
Landscape figure on white, Inter. A semi-photoreal reprocessed dialyzer lying horizontally (correct ports), with a white water-resistant label on the housing magnified in a dashed circle to the right. Five callouts to label fields (all handwriting blurred and illegible): "Full name + second identifier", "Date of first use", "Use number", "Last processing date and time", "Technician initials". A small colored dot callout: "Name alert (similar names)". Red note card: "Unreadable or mismatched label → quarantine. Never relabel from memory."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-07B · Chain of custody
FILE NAME: dialyzer-reprocessing-technician-07-chain-of-custody.png · ARCHETYPE: Journey infographic · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 7 · Chain of custody
PURPOSE: Show custody as a chain of checked hand-overs.
```
Horizontal journey on off-white, Inter. Six photoreal vignettes connected by a chain-link line: "Nurse at the chair" → "Covered transport tray" → "Receiving technician" → "Reprocessor" → "Labeled storage slot" → "Two-person release". Under each vignette, a small green check and a clock icon with "Who · When · What checked". One link between storage and release is shown with a small amber caution icon and the note "Pick by label and two identifiers, never by shelf position." No legible names.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-08A · Time to processing
FILE NAME: dialyzer-reprocessing-technician-08-time-to-processing.png · ARCHETYPE: Two-path comparison · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 8 · Time and temperature
PURPOSE: Teach why the clock starts at end of treatment.
```
Landscape infographic on white, Inter. Center top: a used dialyzer with a large clock icon (no specific times). Left path, amber, "Warm hallway": a cart in a corridor, a magnified inset showing bacteria multiplying inside fibers and dried protein, ending in a red tag "Over the time limit → follow procedure (usually discard)". Right path, green, "Straight to the room or refrigerator": a small stainless refrigerator with a temperature log, ending in a green tag "Within limit → process". Footer: "Your procedure sets the time and temperature."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-08B · Rinse and reverse ultrafiltration
FILE NAME: dialyzer-reprocessing-technician-08-rinse-and-reverse-ultrafiltration.png · ARCHETYPE: Mechanism cutaway · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 8 · Rinsing and cleaning
PURPOSE: Show what each cleaning step removes and where.
```
Landscape mechanism figure on white, Inter. Semi-photoreal longitudinal cutaway of a dialyzer. Panel 1 "Rinse": clear water flushing red blood out of the fibers from end to end. Panel 2 "Reverse ultrafiltration": water entering through the side (dialysate) ports and pushing inward across the fiber walls (small blue arrows pointing into the lumens), lifting yellow protein flakes and tiny clots off the inner wall and out of the blood path. Panel 3 "Header cleaning": an end cap removed, a gloved hand and a gentle spray clearing clot from fiber openings, with a small face-shield icon and the note "Only if the IFU permits". Order arrows 1 → 2 → 3.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-09A · Measuring total cell volume
FILE NAME: dialyzer-reprocessing-technician-09-measuring-total-cell-volume.png · ARCHETYPE: Worked example · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 9 · Total cell volume
PURPOSE: Teach the formula and the edge cases.
```
Landscape infographic on off-white, Inter. Left: a dialyzer mounted vertically on a reprocessor with fluid displaced from its blood compartment into a clear graduated cylinder. Center: a worked example card in navy: "Baseline (this dialyzer, before first use): 100 mL" · "Measured after processing: 82 mL" · "Retained TCV = 82 ÷ 100 × 100 = 82%" with a green check "Meets the 80% floor — one gate only". Right: three small result tiles: red "79% — below floor", amber "104 mL vs 98 mL baseline — flag for review", gray "No baseline — HOLD". Footer: "Training example values."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-09B · Every gate must pass
FILE NAME: dialyzer-reprocessing-technician-09-every-gate-must-pass.png · ARCHETYPE: Gate graphic · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 9 · Every gate
PURPOSE: Make independent acceptance gates unforgettable.
```
Landscape infographic on white, Inter. A closed door labeled "Release" on the right. To its left, a horizontal row of ten semi-photoreal padlocks on a bar, each with a label underneath: "Identity", "Eligibility", "Uses left", "Inspection", "Volume", "Integrity", "Record", "Germicide", "Storage time", "Residual test". Nine padlocks are open and green; the "Integrity" padlock is closed and red. Caption under the bar: "One failed gate keeps the door shut, no matter how many others pass."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-10A · Fill, contact, storage, expiry
FILE NAME: dialyzer-reprocessing-technician-10-fill-contact-storage-expiry.png · ARCHETYPE: Timeline · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 10 · The usable window
PURPOSE: Show the usable window visually.
```
Horizontal timeline on off-white, Inter. Left marker "Germicide fill (record to the minute)" with a dialyzer icon filling with clear germicide. A red segment "Before minimum contact time — not yet disinfected". A green segment "Usable window". A red segment after a marker "Expiry" labeled "Outside the proven window — reprocess or discard". Small formula card above: "Earliest use = fill + contact time · Expiry = fill + maximum storage (both from the IFU)". No specific hours or days shown.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-10B · Two-person handoff
FILE NAME: dialyzer-reprocessing-technician-10-two-person-handoff.png · ARCHETYPE: Scene with callouts · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 10 · Two-person verification
PURPOSE: Teach a real independent double check.
```
Landscape figure on white, Inter. Photoreal scene at a dialysis chair: a Filipino nurse and a Filipina reprocessing technician each holding the same dialyzer label in view, an elderly seated patient showing a wristband (text blurred). Numbered callouts in teal circles: "1 Name + second identifier, read aloud", "2 Use number within limit", "3 Processing date within window", "4 Volume, integrity, presence passed", "5 Residual test read at the exact time, below threshold", "6 Both sign". Small inset of a residual strip next to a timer. Banner: "If either is unsure, it does not connect."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-11A · Tracing back after a fault
FILE NAME: dialyzer-reprocessing-technician-11-tracing-back-after-a-fault.png · ARCHETYPE: Timeline trace · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 11 · Tracing back
PURPOSE: Teach the trace-back window.
```
Landscape infographic on off-white, Inter. A horizontal timeline from a green marker "Last proven-good check" to a red marker "Fault found". Between them, a highlighted amber band "Trace-back window" containing a row of small dialyzer icons, each linked by a thin line downward to a patient silhouette card (no names) labeled "Review". To the right of the red marker, dialyzer icons in normal gray. Side card: "Quarantine stored dialyzers from the window · medical director decides · notify nurses · record." A small reprocessor icon with a red tag at the fault marker.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-11B · Incident decision flow
FILE NAME: dialyzer-reprocessing-technician-11-incident-decision-flow.png · ARCHETYPE: Clinical algorithm · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 11 · When patients react
PURPOSE: Give a simple, memorable incident pathway.
```
Top-to-bottom clinical algorithm on white, Inter, rounded nodes, maximum 4 levels. Start node (red): "Suspected problem: fever or chills in a patient · failed check · equipment fault · water failure". Then teal action nodes in sequence: "Stop and quarantine" → "Protect patients (new dialyzers; physician treats)" → "Preserve evidence (keep dialyzer and lines, capped and labeled)" → "Report (head nurse · medical director · infection prevention)" → "Investigate (records · germicide batch · water log · reprocessor)" → green endpoint "Written decision: release · reprocess · discard". Amber side branch from the first node: "Two or more patients the same day → possible cluster".
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-12A · Reading the room's numbers
FILE NAME: dialyzer-reprocessing-technician-12-reading-the-room-numbers.png · ARCHETYPE: Dashboard · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 12 · Reading the numbers
PURPOSE: Teach reading quality metrics without perverse incentives.
```
Landscape dashboard infographic on off-white, Inter. Left: a simple monthly run chart with two lines, "Average uses per dialyzer" rising and "Volume failures" falling to near zero, plus a small red marker "Reactions appeared". Right: three tiles: "Discards by reason" (small stacked bar: TCV, integrity, clot or visual, use limit, expiry, other), "Reactions per 1,000 treatments", "Records with a gap". A bold amber caution banner across the bottom: "Average uses is a result, not a target. Read the numbers together." Illustrative chart shapes only, no exact values.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### RT-12B · What a record proves
FILE NAME: dialyzer-reprocessing-technician-12-what-a-record-proves.png · ARCHETYPE: Annotated document · DIMENSIONS: 1672 × 941 · PLACEMENT: Module 12 · What a complete record proves
PURPOSE: Show the record as evidence.
```
Landscape figure on white, Inter. Center: a single processing record sheet on a clipboard (all handwriting blurred), with eleven lines highlighted. Each line connects by a thin teal leader to a small labeled chip on the sides: "Identity", "Eligibility", "Water", "Cleaning", "Volume", "Integrity", "Germicide", "Contact time", "Storage", "Rinse + residual", "Handoff". A small inset shows a correction made with a single line, date and initials, labeled "Correct, never erase". Banner: "A complete record lets someone who was not there prove every gate passed."
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

## 7. Derived assets

### OG-01 · Toolkit and track share card
FILE NAME: og/dialyzer-reprocessing-technician-vignette-hero.jpg (export from PNG) · DIMENSIONS: 1200 × 630 (fixed)
```
Social share card, exactly 1200×630, white #ffffff background. Left 55%: navy Inter title "Reprocessing Technician" over a teal subtitle "Renal Care Academy · 12 modules · 6 training calculators". Right 45%: a semi-photoreal hollow-fiber dialyzer standing upright with a cutaway showing fine fibers (correct ports: red-capped arterial end, blue-capped venous end, two side dialysate ports), a small green check badge beside it. Thin teal rule under the title. Generous whitespace.
Attribution "renalcarematters.com" small, bottom-right, 70% opacity navy, Inter.
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, legible real names or ID numbers, invented numeric chemical concentrations, overprocessed HDR, dark backgrounds. Use only Inter. Never omit the attribution.
```

### LAND-01 · Academy landing card
Cut from H00 at 960 × 540, centered on the technician and the dialyzer, then saved as `images/academy/landing/dialyzer-reprocessing-technician.webp`.

## 8. QA checklist (per image)

- [ ] Dialyzer anatomy correct (end blood ports, side dialysate ports, fiber bundle, countercurrent arrows where flow is shown)
- [ ] No legible patient names, numbers or identifiers
- [ ] No germicide concentration, contact time or storage limit shown
- [ ] Figures: Inter only, attribution `renalcarematters.com` bottom-right; heroes: no text at all
- [ ] Light background; gloves and face protection shown wherever blood or chemicals are handled
- [ ] People are Filipino, varied, and not repeated across heroes
- [ ] American English spelling in every label
