# Image Generation Prompts — `dialysis-machine-assignment.html`
**Guide:** Hemodialysis Machine Assignment — HBV, HCV & HIV Guide  
**Site:** williamriveromd.com  
**Audience:** Clinicians & nursing staff (English-only, clinician-facing)  
**Date prepared:** 2026-05-27  
**Tool:** ChatGPT Image Generator GPT (GPT-4o native image generation)  
**Total images:** 5

---

## IMAGE 1 — OG / Hero Image

**IMAGE NUMBER:** 1  
**SECTION PLACEMENT:** `<og:image>` + page hero banner background  
**FILE NAME:** `dialysis-machine-assignment-hero.jpg`  
**ARCHETYPE:** Photorealistic Editorial Hero  
**AUDIENCE:** Clinicians, HD nurses  
**DIMENSIONS:** **1080 × 1080 px — 1:1 square (required for OG tag)**  
**VISUAL MIX:**
- Photorealistic Filipino medical models: primary
- 2D infographic overlay: secondary (minimal — four color-coded machine badge icons at bottom)
- 3D component graphics: supporting (dialysis machine silhouette)
- Algorithm/flowchart: none

**PURPOSE:** OG share card and guide hero — instantly communicates "hemodialysis machine allocation by serology" at a glance, with clinical authority and Filipino context.

**KEY CONCEPTS:** Four machine categories (green/amber/red/amber-dark), serology-based allocation, infection control, Philippine nephrology unit.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME:
dialysis-machine-assignment-hero.jpg

IMAGE TYPE:
Photorealistic Editorial Hero — OG card and guide hero, square 1:1 format

ASPECT RATIO:
1:1 (1080 × 1080 px)

AUDIENCE:
Clinicians and hemodialysis nursing staff

VISUAL GOAL:
Communicate hemodialysis machine allocation by serology — four machine categories, strict infection control, Philippine clinical setting — with authority and immediate visual clarity.

PROMPT:
Photorealistic medical editorial hero image, square 1:1 format (1080 × 1080 px). Scene: a clean, modern Philippine hemodialysis unit interior with four hemodialysis machines arranged in a row, each subtly differentiated by a color-coded vertical accent stripe on the front panel — forest green (#166534) for the first (Non-Isolation), warm amber (#92400e) for the second (Unknown/New), deep red (#b91c1c) for the third (HBV-Isolation), and dark amber-ochre for the fourth (HCV-Isolation). Each machine has a small laminated label card on its front panel with the category name in bold sans-serif type. A Filipino nephrologist — male, early 40s, dark hair, white coat with stethoscope — stands at mid-frame reviewing a printed serology result sheet, facing slightly left, calm and focused expression. Soft diffused fluorescent overhead lighting typical of a Philippine government or private HD unit. Clean tiled floor, privacy curtains partially visible. In the lower quarter of the image, four small horizontal badge chips — green, amber, red, amber-dark — with machine category names in white DM Sans font: NON-ISOLATION · UNKNOWN · HBV-ISOLATION · HCV-ISOLATION. Top third of image has ample dark navy negative space for title overlay. Mood: authoritative, trustworthy, clinical precision. Color palette: navy (#1f3864), clinical teal (#1a6b72), white coats, soft warm interior light. Premium healthcare editorial photography aesthetic, cinematic but restrained, realistic skin texture, shallow depth of field on background machines, no HDR, no oversaturation, no stock-photo blandness, no text except the four badge chips.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, avoid Western/non-Filipino models.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Badge chips must be readable at 300 px width.
```

---

## IMAGE 2 — Four Machine Categories Visual Card

**IMAGE NUMBER:** 2  
**SECTION PLACEMENT:** Section 2 — "The Four Standard Machine Categories" (`#machines`)  
**FILE NAME:** `dialysis-machine-categories.jpg`  
**ARCHETYPE:** Clinician Reference Card / 2D Infographic  
**AUDIENCE:** Clinicians, HD nurses  
**DIMENSIONS:** 1200 × 675 px — 16:9 landscape  
**VISUAL MIX:**
- Photorealistic models: none
- 2D infographic: primary — four color-coded modular cards
- 3D component graphics: supporting — one small semi-realistic dialysis machine icon per card
- Algorithm/flowchart: none

**PURPOSE:** One-glance reference showing the four machine categories, who uses each, and the critical rule for each — color-coded to match the guide's machine-box CSS.

**KEY CONCEPTS:** Non-isolation (green), Unknown/New (amber), HBV-Isolation (red), HCV-Isolation (dark amber); who uses each; critical rules; PSN 2024 / DOH AO 2012-0001.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME:
dialysis-machine-categories.jpg

IMAGE TYPE:
Clinician Reference Card — four-panel 2D infographic

ASPECT RATIO:
16:9 (1200 × 675 px)

AUDIENCE:
Clinicians and hemodialysis nurses

VISUAL GOAL:
One-glance reference for the four hemodialysis machine categories — who uses each and the critical rule — color-coded for instant recall.

PROMPT:
Premium clinician reference infographic, 16:9 landscape. Clean white background (#f9fafb). Bold navy header bar at top: "Hemodialysis Machine Categories" in large condensed white sans-serif, with sub-label "PSN 2024 · DOH AO 2012-0001 · Philippines" in small gold (#b8962e) text. Below header: four equal-width vertical cards arranged side by side, each with a distinct left-border accent, a small semi-photorealistic 3D dialysis machine icon at top, and three content zones:

CARD 1 — Non-Isolation Machine: left-border color forest green (#166534), card background very soft mint (#f0fdf4). Machine icon in green tones. Bold heading: "NON-ISOLATION". Sub-label in small caps: "All serology negative". Three key bullet points in 14px sans-serif: "HBsAg − / Anti-HCV − / HIV −", "Anti-HBs ≥10 mIU/mL preferred", "Re-screen every 3 months". Bottom rule chip in green: "Transfer immediately if any result turns reactive".

CARD 2 — Unknown / New Patient Machine: left-border warm amber (#92400e), card background soft cream (#fffbeb). Machine icon in amber tones. Bold heading: "UNKNOWN / NEW". Sub-label: "Pending serology". Bullets: "Incomplete results only", "Temporary — reassign in 1–2 sessions", "Treat as potentially infectious". Bottom rule chip in amber: "Do NOT use for known seropositive patients".

CARD 3 — HBV-Isolation Machine: left-border deep red (#b91c1c), card background soft red (#fff0f0). Machine icon in red tones. Bold heading: "HBV-ISOLATION". Sub-label: "HBsAg+ OR window period". Bullets: "HBsAg positive patients", "Anti-HBc IgM+ (window period)", "HBV + HIV co-infected". Bottom rule chip in red: "Dedicated machine AND dedicated nursing staff".

CARD 4 — HCV-Isolation Machine: left-border dark amber-ochre (#78350f), card background pale amber (#fef3c7). Machine icon in ochre tones. Bold heading: "HCV-ISOLATION". Sub-label: "Anti-HCV reactive". Bullets: "Anti-HCV reactive (confirmed or pending)", "Assignment persists for life once reactive", "HCV + HIV co-infected". Bottom rule chip in dark amber: "Separate from HBV-isolation machines".

Footer strip: small navy text "williamriveromd.com — Dialysis Machine Assignment Guide". All text high-contrast, minimum 14px equivalent. Rounded card corners (12px). Clean thin dividing lines between cards. No clutter, strong visual hierarchy, publication-grade nephrology infographic aesthetic.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, avoid Canva-style templates.

QUALITY CHECK:
Must be mobile-readable at 600 px width, clinically plausible, visually calm, publication-grade, consistent with williamriveromd.com. All four card labels must be readable at thumbnail size.
```

---

## IMAGE 3 — HBV Serology Interpretation Flowchart

**IMAGE NUMBER:** 3  
**SECTION PLACEMENT:** Section 3 — "Required Laboratory Tests" (`#tests`) / Section 10 — "IgM vs IgG" (`#igm-igg`)  
**FILE NAME:** `dialysis-hbv-serology-flowchart.jpg`  
**ARCHETYPE:** Clinical Algorithm / Flowchart  
**AUDIENCE:** Clinicians, HD nurses  
**DIMENSIONS:** 900 × 1200 px — portrait (tall algorithm)  
**VISUAL MIX:**
- Photorealistic models: none
- 2D infographic: supporting
- 3D component graphics: none
- Algorithm/flowchart: primary

**PURPOSE:** Step-by-step visual decision tree resolving the most confusing HBV serology combinations — from HBsAg result through Anti-HBc IgM — to a machine assignment outcome, including the window period trap.

**KEY CONCEPTS:** HBsAg → positive/negative branch; if negative → Anti-HBc IgM check; IgM+ = window period = HBV-Isolation; IgM− → Anti-HBc Total → isolated pattern → HBV DNA; Anti-HCV; HIV; final machine assignment nodes in guide colors.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME:
dialysis-hbv-serology-flowchart.jpg

IMAGE TYPE:
Clinical Algorithm / Flowchart — HBV serology interpretation for machine assignment

ASPECT RATIO:
Portrait — 900 × 1200 px

AUDIENCE:
Clinicians and HD nurses

VISUAL GOAL:
Step-by-step visual decision tree from HBsAg result through Anti-HBc IgM to machine assignment, highlighting the window-period trap that causes the most allocation errors.

PROMPT:
Premium clinical nephrology algorithm flowchart, portrait orientation (900 × 1200 px). White/near-white background (#fafafa). Top header block: navy (#1f3864) rounded rectangle, white bold condensed title "HBV Serology → Machine Assignment" in 24px, subtitle "PSN 2024 · DOH AO 2012-0001" in gold 14px. Clean top-to-bottom flowchart with the following node structure:

START NODE (navy rounded rectangle, white text): "New HD Patient: Order Full HBV Panel"
Arrow down → DIAMOND DECISION NODE (navy outline): "HBsAg Result?"
→ RIGHT BRANCH (red arrow): "REACTIVE / POSITIVE" → RED ENDPOINT BOX: "HBV-ISOLATION MACHINE — Immediately. Dedicated staff required." (deep red #b91c1c background, white text, bold)
→ LEFT/DOWN BRANCH (teal arrow): "NEGATIVE" → DIAMOND: "Anti-HBc IgM Result?"
  → RIGHT BRANCH (red arrow): "POSITIVE" → RED WARNING BOX: "⚠ WINDOW PERIOD — Patient is infectious. HBsAg may still be negative. → HBV-ISOLATION MACHINE immediately." Red left border, soft red background, bold warning text.
  → DOWN BRANCH (green arrow): "NEGATIVE" → DIAMOND: "Anti-HBc Total Result?"
    → RIGHT BRANCH (amber arrow): "POSITIVE (Isolated pattern)" → AMBER BOX: "Isolated Anti-HBc. Order HBV DNA. Consult nephrologist. Pending result → Unknown Machine."
    → DOWN BRANCH (green arrow): "NEGATIVE" → DIAMOND: "Anti-HCV Reactive?"
      → RIGHT BRANCH (amber-dark arrow): "YES" → AMBER-DARK BOX: "HCV-ISOLATION MACHINE"
      → DOWN BRANCH (green arrow): "NO" → DIAMOND: "HIV Reactive?"
        → RIGHT BRANCH (teal arrow): "YES" → TEAL BOX: "Non-isolation machine with HIV standard precautions per RA 11166"
        → DOWN BRANCH (green arrow): "NO → All serology negative + Anti-HBs ≥10" → GREEN ENDPOINT: "NON-ISOLATION MACHINE ✓"

Node style: rounded rectangles for actions/endpoints (12px radius), diamonds for decisions, consistent arrow weight (2px), short directional labels (YES/NO/REACTIVE/NEGATIVE) in bold 12px beside each arrow. Endpoint boxes: color-filled with white bold text. Color coding matches guide: green for non-isolation, amber for unknown, red for HBV, amber-dark for HCV. Small footer: "williamriveromd.com" in 10px muted text. Maximum 3-column width, clean whitespace between nodes, no spaghetti routing, all text ≥12px equivalent, publication-grade KDIGO flowchart aesthetic.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid spaghetti routing, avoid crossing arrows, avoid overprocessed HDR, avoid generic stock look.

QUALITY CHECK:
Must be readable on mobile at 400 px width. Decision nodes must be clearly distinguishable from action nodes. Window-period warning must be visually prominent — most critical clinical point.
```

---

## IMAGE 4 — Seroconversion Protocol Timeline Infographic

**IMAGE NUMBER:** 4  
**SECTION PLACEMENT:** Section 8 — "When a Patient Seroconverts" (`#seroconversion`)  
**FILE NAME:** `dialysis-seroconversion-timeline.jpg`  
**ARCHETYPE:** Multi-Panel Educational Infographic / Clinical Algorithm  
**AUDIENCE:** HD nurses, nephrologists, HD unit supervisors  
**DIMENSIONS:** 1200 × 675 px — 16:9 landscape  
**VISUAL MIX:**
- Photorealistic models: minimal — small icon-scale Filipino nurse figure at Day 0
- 2D infographic: primary — horizontal timeline with phase panels
- 3D component graphics: supporting — small syringe icon (HBIG/vaccine), lab tube icon (re-screening)
- Algorithm/flowchart: supporting — sequential phase structure

**PURPOSE:** Horizontal timeline showing the four phases of seroconversion response — Day 0 (immediate actions), 48 h (notifications), Week 1 (contact tracing), Week 4–16 (re-screening) — as a scannable clinical reference.

**KEY CONCEPTS:** Day 0 immediate actions; 48 h nephrologist/director notification; DOH cluster notification trigger (≥2 cases/90 days); Week 1 machine disinfection + contact list; HBIG + vaccine within 24 h; Week 4–16 re-screen contacts.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME:
dialysis-seroconversion-timeline.jpg

IMAGE TYPE:
Horizontal timeline infographic — four-phase seroconversion response protocol

ASPECT RATIO:
16:9 (1200 × 675 px)

AUDIENCE:
HD nurses, nephrologists, HD unit supervisors

VISUAL GOAL:
Scannable four-phase seroconversion protocol timeline — Day 0 through Week 16 — showing who does what, when, in the correct sequence after a new HBV or HCV positive result in an HD unit.

PROMPT:
Premium clinical nephrology timeline infographic, 16:9 landscape. White background. Bold navy header bar at top full width: "Seroconversion Response Protocol" large white condensed sans-serif, with subtitle "New HBsAg+ or Anti-HCV reactive result in an HD patient" in gold (#b8962e) 14px. Below header: a horizontal left-to-right timeline with a thick navy centerline and four evenly spaced phase nodes. Each node expands into a vertical card above or below the centerline (alternating: above/below/above/below), connected by short vertical stems.

PHASE 1 NODE — "DAY 0 — SAME SESSION": Deep red circle node. Card ABOVE timeline. Red top-border card. Bold heading: "Immediate Actions". Bullet list in 12px: "Transfer to HBV/HCV-Isolation machine", "Notify nephrologist today", "Complete enhanced machine disinfection", "File Seroconversion Incident Report", "Notify HD Supervisor + Infection Control Officer". Small icon: red alert bell.

PHASE 2 NODE — "48 HOURS": Amber circle node. Card BELOW timeline. Amber top-border card. Heading: "Escalation & PEP". Bullets: "Notify HD Medical Director within 48 h", "If cluster (≥2 cases/90 days): DOH notification within 24 h", "Unvaccinated contacts: HBIG 0.06 mL/kg IM + first HBV vaccine dose ASAP". Small icons: syringe (HBIG/vaccine), phone (notification).

PHASE 3 NODE — "WEEK 1": Teal circle node. Card ABOVE timeline. Teal top-border card. Heading: "Investigation". Bullets: "Review machine usage log (past 3–6 months)", "Build contact tracing list — all patients on same machine", "Audit staff glove-change compliance", "Review disinfection logs, water records". Small icon: clipboard/checklist.

PHASE 4 NODE — "WEEKS 4 – 16": Green circle node. Card BELOW timeline. Green top-border card. Heading: "Re-screening Contacts". Bullets: "HBV exposure: HBsAg + Anti-HBc IgM at 2–4 wks; repeat at 8 and 16 wks", "HCV exposure: Anti-HCV + HCV RNA at 2–4 wks; repeat at 8 and 16 wks", "Staff re-training session; document attendance", "Submit final incident report to DOH if cluster". Small icon: lab tube (blood draw).

Footer strip full width: soft gray bar. Left: "williamriveromd.com". Right: "PSN HD Guidelines 3rd Ed. 2024 · DOH AO 2012-0001". All text minimum 12px equivalent. Rounded card corners. Publication-grade clean infographic. No clutter, strong hierarchy, mobile-readable.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid crossing arrows, avoid overprocessed HDR, avoid Canva-style templates, avoid excessive color.

QUALITY CHECK:
Must be readable on mobile at 500 px width. Phase nodes must be visually distinct and sequentially clear. Day 0 red urgency must stand out against the calmer later phases.
```

---

## IMAGE 5 — Superimposed Infection Protocol Diagram

**IMAGE NUMBER:** 5  
**SECTION PLACEMENT:** Section 9 — "Superimposed Contagious Infections" (`#coinfection`)  
**FILE NAME:** `dialysis-coinfection-protocol.jpg`  
**ARCHETYPE:** Clinical Algorithm / Two-Axis Decision Matrix  
**AUDIENCE:** Clinicians, HD nurses  
**DIMENSIONS:** 1200 × 800 px — 3:2 landscape  
**VISUAL MIX:**
- Photorealistic models: none
- 2D infographic: primary — two-axis matrix + three precaution tier cards
- 3D component graphics: supporting — N95 respirator icon, surgical mask icon, dialysis machine silhouette
- Algorithm/flowchart: supporting — two-decision framework

**PURPOSE:** Visualize the two-decision framework for patients with superimposed infections — Decision 1 (machine = serology-based, never changes) and Decision 2 (location/timing = infection type: airborne, droplet, contact) — as a scannable matrix.

**KEY CONCEPTS:** Two independent decisions; airborne (PTB) = isolated room + N95 + last shift; droplet (influenza/COVID) = last shift + surgical mask + physical separation; contact (MRSA) = gloves + gown; machine assignment is unchanged by superimposed infection.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME:
dialysis-coinfection-protocol.jpg

IMAGE TYPE:
Two-axis clinical decision matrix — superimposed infection protocol

ASPECT RATIO:
3:2 (1200 × 800 px)

AUDIENCE:
HD nurses and nephrologists

VISUAL GOAL:
Communicate that superimposed infections require two simultaneous independent decisions — machine (serology, never changes) and location/timing (infection type) — as a scannable visual matrix.

PROMPT:
Premium clinical nephrology infographic, 3:2 landscape. White/near-white background (#fafafa). 

HEADER: Full-width navy bar. White bold: "Superimposed Infections in HD Patients: Two Independent Decisions". Gold subtitle: "Machine ≠ Location — Both Must Be Addressed Separately".

MAIN BODY: Two-column layout with a narrow navy vertical divider labeled "AND" in white at center.

LEFT COLUMN — "DECISION 1: WHICH MACHINE?" (teal top-border panel, soft teal background). Large teal heading. Sub-heading in bold: "Determined by serology only." Three rows in compact table format: Row 1: green chip "HBsAg − / Anti-HCV − / HIV −" → "Non-Isolation"; Row 2: amber chip "Pending results" → "Unknown Machine"; Row 3: red chip "HBsAg+ or IgM+" → "HBV-Isolation"; Row 4: dark amber chip "Anti-HCV+" → "HCV-Isolation". Bold footer rule in teal box: "A superimposed infection NEVER changes the machine assignment." Icon: small dialysis machine silhouette.

RIGHT COLUMN — "DECISION 2: WHERE & WHEN?" (amber top-border panel, soft amber background). Large amber heading. Sub-heading: "Determined by the superimposed infection type." Three stacked precaution tier cards:

TIER 1 — AIRBORNE (deep red left-border card): Icon: N95 respirator line drawing. Bold: "Active PTB (AFB smear+, GeneXpert+)". Details: "Isolated room with airborne precautions | Last shift if no isolation room available | N95 for all entering staff | Patient wears surgical mask | Negative pressure or open windows".

TIER 2 — DROPLET (amber left-border card): Icon: surgical mask line drawing. Bold: "Influenza, COVID-19, bacterial pneumonia". Details: "Physical separation ≥1 m from other patients | Last shift or end of shift | Surgical mask for patient | Surgical mask + eye shield for staff | Standard precautions otherwise".

TIER 3 — CONTACT (green left-border card): Icon: gloved hand line drawing. Bold: "MRSA, VRE, C. difficile, wound infection". Details: "Gloves + gown for all staff contact | Dedicated equipment (stethoscope, BP cuff) | Standard session timing acceptable | Clean machine after session per protocol".

FOOTER: Soft gray bar. Left: "williamriveromd.com". Right: "PSN 2024 · DOH AO 2012-0001 · RA 11166". All text minimum 12px equivalent. Rounded card corners. Strong visual separation between two columns. Publication-grade clinical infographic.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed HDR, avoid generic stock look, avoid Canva-style templates, avoid crossing arrows.

QUALITY CHECK:
Must be readable on mobile at 500 px width. The two-column separation must be immediately obvious. The "machine never changes" rule must be visually anchored. Precaution tiers must be scannable in under 10 seconds.
```

---

## File Naming Summary

| # | File name | Dimensions | Section |
|---|-----------|------------|---------|
| 1 | `dialysis-machine-assignment-hero.jpg` | 1080 × 1080 (1:1) | OG tag + hero banner |
| 2 | `dialysis-machine-categories.jpg` | 1200 × 675 (16:9) | Section 2 — Four Categories |
| 3 | `dialysis-hbv-serology-flowchart.jpg` | 900 × 1200 (portrait) | Section 3 / Section 10 |
| 4 | `dialysis-seroconversion-timeline.jpg` | 1200 × 675 (16:9) | Section 8 — Seroconversion |
| 5 | `dialysis-coinfection-protocol.jpg` | 1200 × 800 (3:2) | Section 9 — Co-infections |

## Placement instructions once images are received

1. Copy all five `.jpg` files to `/images/` in the site root.
2. Image 1 (`dialysis-machine-assignment-hero.jpg`) is already referenced in `og:image` and `twitter:image` in the guide `<head>` — no HTML edit needed.
3. Images 2–5: insert `<figure>` blocks in the relevant guide sections using the pattern:
```html
<figure style="margin:32px 0;">
  <img src="/images/[filename].jpg"
       alt="[descriptive alt text]"
       width="1200" height="675"
       loading="lazy"
       style="width:100%;height:auto;display:block;border-radius:10px;">
</figure>
```
4. For Image 3 (portrait flowchart), use `max-width:600px;margin:32px auto;`.
5. Run `python3 patch_hero_fetchpriority.py --guide dialysis-machine-assignment.html` after adding Image 1 to set `fetchpriority="high" loading="eager"` on the hero.
