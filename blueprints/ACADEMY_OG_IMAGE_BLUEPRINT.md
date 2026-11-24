# Renal Care Academy — Open Graph (Share Card) Image Blueprint

**Scope:** 15 share cards — the Academy landing page plus all 14 tracks.
**Producer:** Image Generator GPT (art only). **Typesetting:** `build_academy_og.py` (all words).
**Attribution:** public site set → `renalcarematters.com` (set by the script, never painted by GPT).
**Prepared:** November 24, 2026

---

## 1. Why the tracks need new share images

The track pages currently share `images/og/<slug>-vignette-hero.jpg`: a 1200 × 1200 **square** circular vignette on white. Facebook, Messenger, LinkedIn, and X crop share images to about **1.91:1**, so the square loses the top and bottom thirds (heads and the machine are cut), and the white corners read as empty space. Nothing on the card says "Academy," names the role, or tells a new hire this is a course.

The new cards fix that with one system for all 15 pages: a wide illustrated scene on the right, and a typeset left panel that names the track, its group, and its size.

## 2. Two-layer architecture (read this before prompting)

| Layer | Made by | Contains |
|---|---|---|
| **Art layer** | Image Generator GPT | The illustrated scene only. **No words, letters, numbers, logos, or watermarks anywhere.** Left 45% is a quiet field. |
| **Type layer** | `build_academy_og.py` | Wordmark "RENAL CARE ACADEMY," group and tag line, track title, stats line, `renalcarematters.com/academy`, accent bar in the group color. |

Reason: GPT misspells long titles ("Hemodialysis Center Biomedical Technician," "PhilHealth Liaison, Claims Officer and Clerk") and drifts in font and size between images. Keeping words out of the art makes every card legible, correctly spelled, and identical in layout, and lets a title change without regenerating art.

## 3. Canvas and safe zones (art layer)

- **Generate at 1536 × 1024 (landscape, 3:2).** The script crops to 1.91:1, which trims about **110 px from the top and 110 px from the bottom**, then scales to 1200 × 630.
- **Quiet field — left 0–45% of width:** soft gradient, mint `#dcefe8` at far left blending to warm cream `#f5efdc`. A very soft, out-of-focus hint of the unit is acceptable at the 35–45% edge only. No faces, hands, equipment, or high-contrast detail in this zone; the script lays text over it.
- **Subject zone — right 48–96% of width:** people and equipment. Keep all heads and key hands between **15% and 85% of the height** so the crop never cuts them.
- **Right edge (96–100%):** allow the scene to bleed naturally; no hard border.

```
 0%                45%    48%                                    100%
 ┌──────────────────┬──────┬──────────────────────────────────────┐ ← trimmed (~110 px)
 │                  │ soft │                                      │
 │   QUIET FIELD    │ blur │      SUBJECT ZONE                    │
 │   mint → cream   │      │      people + equipment              │
 │   (text goes     │      │      heads/hands within 15–85% H     │
 │    here later)   │      │                                      │
 └──────────────────┴──────┴──────────────────────────────────────┘ ← trimmed (~110 px)
```

## 4. Style lock (paste once at the start of the GPT conversation)

> **STYLE LOCK — use for every image in this conversation.**
> Landscape 1536 × 1024. Semi-realistic editorial medical illustration with a soft painterly digital finish, warm natural light, gentle depth of field — the same look as a polished patient-education illustration, not a photograph and **not** flat vector art. Setting: a clean, modern hemodialysis unit or clinic in the Philippines. People are Filipino adults of varied ages and builds, with natural, warm, competent expressions; no one is a recognizable real person. Staff wear navy-blue scrubs (nurses, technicians), white coats over clinical wear (physicians), or neat business-casual (managers, claims, records staff), with ID lanyards that carry **blank** badges. Palette: teal `#1A6B72`, navy `#1F3864`, mint `#dcefe8`, cream `#f5efdc`, with a small warm accent drawn from the scene. **Composition rule:** the left 45% of the canvas is an empty, soft mint-to-cream gradient field with no people, objects, or detail; all subjects sit in the right half, with heads and hands between 15% and 85% of the image height. **Absolutely no text, letters, numbers, labels, logos, brand names, screen readouts, or watermarks** — monitors and screens show only soft abstract color blocks; papers show only gray lines.

## 5. Group color coding (applied by the script, reflected lightly in the art)

| Group | Tracks | Accent (bar + wordmark rule) | Art hint |
|---|---|---|---|
| Academy | Landing page | Teal `#1A6B72` | Ensemble, all roles |
| Nephrology Nursing | By specialization: Hemodialysis Nurse (core course), Peritoneal Dialysis Nurse, Transplant Nurse · By role: Head Nurse | Teal `#1A6B72` | Teal lanyards |
| Renal Care Physicians | Dialysis Clinical Head, Attending Nephrologist, Physician on Duty | Navy `#1F3864` | White coats, navy tones |
| Renal Technicians | Dialysis, Water Treatment, Biomedical Equipment Technician | Orange `#C55A11` | Warm orange tool or valve accents |
| Ancillary Staff | Renal Dietitian, Medical Records Officer and Custodian | Green `#2E6B3E` | Green accents: vegetables, folder tabs |
| Administrative Staff | Dialysis Unit Operations Manager, PhilHealth Liaison and Claims Officer | Purple `#4B3280` | Purple folder or binder accents |

## 6. Per-image prompts

Paste the style lock once, then send each prompt below as its own message. Save each result with the exact file name shown.

### 6.0 Academy landing page → `academy-index.png`
**Scene:** A small team of five kidney-care professionals standing together in a bright dialysis unit, as if at the start of a training day: a nurse in navy scrubs holding a tablet, a dialysis technician with a primed blood-line set over one arm, a physician in a white coat, a dietitian holding a plate-model food card, and a unit manager with a clipboard. They are turned slightly toward each other in an easy, welcoming huddle. Behind them, out of focus, two dialysis chairs and a hemodialysis machine.
**Mood:** Welcoming, team-based, "you belong here."
**Avoid:** Classroom desks, graduation caps, certificates (the Academy is not certification).

### 6.1 Hemodialysis Nurse — Nephrology Nursing core course → `nephrology-nursing.png`
**Scene:** A nurse in navy scrubs, gloved, seated beside a reclined patient in a hemodialysis chair, gently palpating the patient's **left forearm arteriovenous fistula** before the session; a stethoscope around the nurse's neck. The hemodialysis machine stands beside the chair with the blood lines not yet connected.
**Clinical accuracy:** Fistula on the forearm, visible as a gently raised vein; no needles yet; patient calm and awake.
**Avoid:** Blood spills, needles in the hand, a catheter and fistula on the same arm.

### 6.2 Peritoneal Dialysis Nurse → `peritoneal-dialysis-nurse.png`
**Scene:** A tidy home living room set up for peritoneal dialysis. A nurse wearing a mask coaches a seated adult patient, also masked, through a CAPD exchange: a clear fluid bag hangs from an IV pole above shoulder height, the drain bag rests on the floor below, a hand-sanitizer bottle and clean towel sit on a side table.
**Clinical accuracy:** Fill bag above, drain bag below; both people masked; the catheter connection held by the patient's own clean hands; clear (not cloudy) fluid.
**Avoid:** Visible abdomen or catheter exit site, cloudy effluent, open windows with a fan blowing toward the setup.

### 6.3 Transplant Nurse → `transplant-nurse.png`
**Scene:** A transplant clinic consultation room. A nurse in navy scrubs sits across a small table from a smiling adult kidney transplant recipient, pointing to a weekly pill organizer with morning and evening compartments. A home blood pressure cuff and a small notebook lie on the table; a window lets in soft daylight.
**Clinical accuracy:** Patient looks well; no surgical wound shown; the nurse is teaching, the patient is engaged.
**Avoid:** Medication labels or brand packaging, hospital gowns.

### 6.4 Dialysis Head Nurse → `dialysis-head-nurse.png`
**Scene:** At the nurses' station of a busy dialysis unit at the start of a shift, a senior nurse in navy scrubs leads a brief huddle with two staff — a nurse and a technician. She stands beside a wall-mounted roster board (shown only as a grid of colored blocks), one hand gesturing toward the unit floor where patients are settling into chairs.
**Mood:** Calm authority, organization, teamwork.
**Avoid:** Readable schedule text, raised voices or stressed faces.

### 6.5 Dialysis Clinical Head → `dialysis-clinical-head.png`
**Scene:** A physician leader in a white coat walks the dialysis unit with the head nurse during a safety round, holding a clipboard. Through a glass wall behind them, the water-treatment room is visible: blue pretreatment tanks and the reverse-osmosis unit with stainless pipes.
**Mood:** Oversight, stewardship, the whole service in view.
**Avoid:** Office desks or boardroom imagery (keep the leader on the floor).

### 6.6 Attending Nephrologist → `attending-nephrologist.png`
**Scene:** An intensive care unit bedside. A senior nephrologist in a white coat reviews a continuous renal replacement therapy (CRRT) machine with a nephrology fellow, both looking at the machine's screen (abstract color blocks only). The ICU patient lies sedated in bed in the background, a dialysis catheter dressing at the right side of the neck.
**Clinical accuracy:** CRRT machine with replacement-fluid bags hanging on its sides; catheter in the internal jugular position with a clean dressing.
**Avoid:** Visible blood leaks, readable monitor values.

### 6.7 Physician on Duty in the Dialysis Unit → `physician-on-duty.png`
**Scene:** Mid-session, a young physician in a white coat stands at the chairside of a patient whose chair has been reclined with legs raised, listening with a stethoscope. A nurse at the hemodialysis machine has a hand on the control panel, and a blood pressure cuff is on the patient's non-access arm.
**Clinical accuracy:** This depicts response to intradialytic low blood pressure — legs raised, head slightly lower, patient alert; the cuff is on the arm **without** the fistula and blood lines.
**Avoid:** Resuscitation, crash cart in action, a panicked atmosphere.

### 6.8 Dialysis Technician → `hemodialysis-technician.png`
**Scene:** A dialysis technician in navy scrubs, gloves, and a face shield primes the extracorporeal circuit on a hemodialysis machine: the dialyzer mounted vertically, the arterial and venous blood lines filled with clear saline, a saline bag hanging above. The chair beside the machine is empty and freshly made.
**Clinical accuracy:** Lines filled with clear fluid (priming, not blood); red-marked arterial and blue-marked venous line clamps.
**Avoid:** A patient connected while priming, blood in the lines.

### 6.9 Water Treatment System Technician → `water-treatment-technician.png`
**Scene:** Inside a dialysis water-treatment room, a technician in navy scrubs and gloves draws a water sample from a sampling port between two blue carbon tanks into a small test vial, holding a color-comparison test kit. Behind: the reverse-osmosis unit, pressure gauges, and labeled-looking (but text-free) stainless distribution pipes.
**Accent:** An orange valve handle or the technician's orange clipboard.
**Avoid:** Readable gauge numbers, puddles on the floor.

### 6.10 Hemodialysis Center Biomedical Technician → `dialysis-biomedical-technician.png`
**Scene:** A biomedical workshop. A technician wearing an antistatic wrist strap works on a hemodialysis machine standing on a service bench with its rear panel removed, revealing hydraulic tubing and circuit boards. He holds a calibrated meter probe to a test port; a tool roll and a second test instrument sit on the bench.
**Accent:** Orange-handled tools.
**Avoid:** Sparks, exposed live wiring hazards, readable meter numbers.

### 6.11 Renal Dietitian → `renal-dietitian.png`
**Scene:** A dietitian in neat clinical wear counsels an adult patient and a family member at a small consultation table. Between them sits a plate model of a kidney-friendly Filipino meal: a measured cup of white rice, a palm-sized portion of grilled fish, sautéed cabbage and chayote, and a small dish of calamansi. A food scale and measuring cups lie nearby.
**Clinical accuracy:** Modest portions; lower-potassium vegetables; no salty condiments in focus.
**Avoid:** Bananas, tomatoes, dried fish, instant noodles, soy sauce in the foreground; food packaging with labels.

### 6.12 Medical Records Officer and Custodian → `medical-records-officer.png`
**Scene:** A records room with locked, color-coded filing cabinets. A records officer in business-casual clothing files a patient chart folder while a laptop with a privacy screen rests on a counter beside a small key cabinet. Soft overhead light, orderly and secure.
**Accent:** Green and teal folder tabs (no writing on them).
**Avoid:** Open charts with readable content, cluttered paper piles.

### 6.13 Dialysis Unit Operations Manager → `dialysis-unit-manager.png`
**Scene:** A unit operations manager in business-casual clothing stands in a supply room doorway with a tablet, reviewing stock on tidy shelves of dialyzers, blood-line sets, and saline (packages shown as plain white boxes). Behind, out of focus, the busy dialysis floor with staff at work.
**Accent:** A purple binder on the top shelf.
**Avoid:** Cash, money imagery, readable inventory text.

### 6.14 PhilHealth Liaison, Claims Officer and Clerk → `philhealth-claims.png`
**Scene:** A claims officer seated at a tidy desk beside the dialysis unit's front office, reviewing a patient's session records against a checklist. Two neat stacks of folders, a document stamp, a computer monitor showing only abstract form-like gray blocks, and a desk calendar with blank squares. Through the doorway, a dialysis chair is just visible.
**Accent:** Purple folders.
**Avoid:** Any PhilHealth logo, peso bills, readable forms or patient names.

## 7. QA checklist (run on every image before the hand-back)

1. **No text anywhere** — screens, papers, badges, boxes, walls, machines. Any letter-like marks → regenerate.
2. **Left 45% quiet** — no faces, hands, or equipment detail in the text field.
3. **Crop-safe** — heads and key hands between 15% and 85% of the height.
4. **Clinical accuracy** — the per-image accuracy notes above hold (fistula arm, priming fluid clear, PD bag heights, cuff on the non-access arm, CRRT catheter position).
5. **Infection control** — gloves where hands touch access or circuit; masks in PD exchange and at cannulation; no bare-hand contact with sterile parts.
6. **People** — Filipino adults, natural anatomy (count fingers), no recognizable real person, no minors.
7. **No brands** — machines, bags, and boxes are generic.
8. **Style match** — painterly editorial illustration, not photo-real, not flat vector; consistent with the other 14 images.
9. **File** — PNG, 1536 × 1024, exact file name from Section 6.

If an image fails, note the failed item number and regenerate with: *"Same scene, same style lock. Fix: <item>."*

## 8. Hand-back and build

1. Drop all 15 PNGs in one folder (suggested: `/Volumes/Storage/Renal Care Academy/OG images`).
2. Claude audits each image against Section 7, then runs:
   `python3 build_academy_og.py --art "<folder>" --patch`
   → writes `images/og/academy/<slug>.jpg` (1200 × 630, ≤ 300 KB) and points each page's `og:image`, `twitter:image`, and `og:image:width/height/type` at it.
3. Test one link in the Facebook Sharing Debugger and a Messenger or Viber chat before pushing.
