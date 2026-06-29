# Image Prompts — Prostate Cancer and CKD (`prostate-cancer-ckd.html`)
**Guide:** williamriveromd.com/guides/prostate-cancer-ckd.html
**Generated:** 2026-06-19
**Pipeline (Stage 1):** three prompt-authoring skills, one per figure type
- `williamriveromd-biomedical-mechanism-figure` → IMAGE 1 (mechanism schematic)
- `williamriveromd-infographic-skill` → IMAGES 2–5 (hero, OG card, algorithm, multi-panel infographic)
- `williamriveromd-simple-figure` → IMAGE 6 (PSA decision reference card)

**House rules (all images):** light background only (white/off-white/soft gray); navy `#0f1e2e` and teal `#1a6b72` are text/accent colors only; every image carries small semi-transparent navy `williamriveromd.com` attribution bottom-right (bottom-center for portrait).

**Next step (Stage 2):** feed this pack to `williamriveromd-local-image-generator` to build the folder/manifest and wire `og:image` tags. IMAGE 3 (OG card) replaces the currently-borrowed `prostate-enlargement-og-card.png` reference in the guide's meta tags.

| # | File | Skill | Type | Dimensions | Audience |
|---|------|-------|------|-----------|----------|
| 1 | `prostate-cancer-ckd-mechanism-poster.png` | mechanism-figure | Mechanism schematic | 1792 × 1024 | Mixed |
| 2 | `prostate-cancer-ckd-hero.png` | infographic | Editorial hero | 1254 × 1254 | Patients |
| 3 | `prostate-cancer-ckd-og-card.png` | infographic | OG share card | 1200 × 630 | Mixed |
| 4 | `prostate-cancer-ckd-management-algorithm.png` | infographic | Clinical algorithm | 1024 × 1536 | Clinicians |
| 5 | `prostate-cancer-ckd-kidney-protection-infographic.png` | infographic | Multi-panel infographic | 1792 × 1024 | Patients |
| 6 | `prostate-cancer-ckd-psa-reference-card.png` | simple-figure | Reference / decision card | 1536 × 1152 | Clinicians |

---

## IMAGE 1 — Mechanism Schematic
*(authored with `williamriveromd-biomedical-mechanism-figure`)*

SECTION PLACEMENT: "What is the Connection Between Prostate Cancer and CKD?" / "Direct Tumor Effects on Kidneys"
FILE NAME: `prostate-cancer-ckd-mechanism-poster.png`
ARCHETYPE: Review-article biomedical mechanism figure (organ panel → magnified inset → injury→intervention→benefit flow)
AUDIENCE: Mixed (clinician-leaning)
DIMENSIONS: 1792 × 1024 px (16:9)
PURPOSE: Explain at organ-to-tubular scale how prostate cancer and its treatments converge on kidney injury.
KEY CONCEPTS: Ureteral obstruction / hydronephrosis · nephrotoxic chemo/contrast/NSAID tubular injury · ADT-driven metabolic syndrome accelerating CKD.

COPY-READY PROMPT:

```
Create a publication-grade biomedical mechanism schematic in a scientific review-article style. White (#ffffff) background, flat vector illustration with soft semi-3D shading, muted clinical palette, thin dashed connector boxes, clean sans-serif labels, generous whitespace. Landscape 1792 × 1024.

Title (top, bold navy #0f1e2e): "How Prostate Cancer and Its Treatment Injure the Kidney". Subtitle in clinical teal (#1a6b72): "Three converging pathways to CKD".

LEFT PANEL — organ-level context:
Simplified light gray-blue urinary tract anatomy: two kidneys, two ureters, bladder, and prostate at the bladder outlet. Label the kidney "CKD". Show the prostate enlarged by tumor (muted red-pink) compressing the lower ureters; depict back-pressure with a swollen renal pelvis labeled "hydronephrosis". A thin dashed connector box points from the kidney to the magnified panel on the right.

RIGHT PANEL — magnified functional unit (inside a dashed border):
A single nephron schematic (glomerulus + proximal tubule + loop + distal/collecting segment). Highlight the proximal tubule in pale yellow. Concise callouts with directional arrows:
- Proximal tubule: "↓ tubular blood flow" and "↑ ROS / oxidative stress" (red) from nephrotoxins
- Glomerulus: "↓ renal perfusion" (NSAIDs constrict afferent arteriole)
- Tubular segment: "obstructive back-pressure → ↓ GFR"
Small red arteriole and blue venule along the vessel pole.

BOTTOM SUMMARY FLOW (left → center → right, bold arrows):
- Left pale-pink pathology box "INJURY DRIVERS":
  • Ureteral obstruction (tumor mass effect)
  • Nephrotoxins: cisplatin/carboplatin, iodinated contrast, NSAIDs
  • Androgen deprivation therapy → metabolic syndrome (↑ BP, ↑ glucose, ↑ lipids)
- Center box "INTERVENTION" (clinical teal): relieve obstruction · pre-hydration before contrast/chemo · eGFR-based dose adjustment · avoid NSAIDs · onco-nephrology co-management
- Right pale-blue benefit box "EXPECTED EFFECT":
  • Preserved eGFR
  • Fewer AKI episodes
  • More treatment options retained

Use red for arteries/injury/ROS, blue for veins/therapeutic effects, pale yellow for the affected tubule, pale pink for the pathology box, pale blue for the benefit box. Keep anatomy plausible, no invented pathways, no photorealism, no dark background, no decorative clutter. Bottom-right corner: small semi-transparent navy "© williamriveromd.com".
```

---

## IMAGE 2 — Editorial Hero (inline LCP)
*(authored with `williamriveromd-infographic-skill`)*

SECTION PLACEMENT: Patient-tab hero (replaces borrowed `prostate-enlargement-og-card.png` in-page hero)
FILE NAME: `prostate-cancer-ckd-hero.png`
ARCHETYPE: Photorealistic Editorial Hero
AUDIENCE: Patients, caregivers
VISUAL MIX:
- photorealistic models: Filipino nephrologist + older male patient
- 2D infographic: none
- 3D component graphics: subtle kidney model accent on side table
- algorithm/flowchart: none
PURPOSE: Build trust and frame the guide as a co-management story between patient and nephrologist.
KEY CONCEPTS: Shared decision-making, kidney protection during cancer treatment.
DIMENSIONS: 1254 × 1254 px (1:1)

COPY-READY PROMPT:

```
Photorealistic medical editorial hero image for a nephrology education guide. Square 1254 × 1254. Show a calm, reassuring consultation: a Filipino nephrologist in his 50s in a clean white coat seated beside an older Filipino male patient (late 60s) in a bright, airy outpatient clinic, reviewing lab results together on a tablet. Warm, trusting body language, calm facial expressions, natural Filipino skin texture. On a soft-focus side table sits a small semi-photorealistic 3D anatomical model of two kidneys as a subtle accent. Premium healthcare publication aesthetic, bright natural daylight from a window, light-toned background (white walls, soft daylight), shallow depth of field. Restrained navy (#0f1e2e) and teal (#1a6b72) accents in clothing and props. Preserve clean negative space at upper-left for a title overlay, mobile-safe centered crop. No embedded text except a small semi-transparent navy "williamriveromd.com" attribution in the bottom-right corner.

NEGATIVE: Avoid cartoon style, clutter, dark or moody lighting, dark/navy/charcoal/black backgrounds, unrealistic anatomy, overprocessed HDR, generic stock-photo look, AI gibberish text.
```

---

## IMAGE 3 — OG / Social Share Card
*(authored with `williamriveromd-infographic-skill`)*

SECTION PLACEMENT: `og:image` + `twitter:image` meta tags
FILE NAME: `prostate-cancer-ckd-og-card.png`
ARCHETYPE: Typographic OG card with 3D anatomy accent
AUDIENCE: Mixed (social share)
DIMENSIONS: **1200 × 630 px (1.91:1) — fixed, non-negotiable**
PURPOSE: Legible share thumbnail across Facebook, X, LinkedIn, iMessage.
KEY CONCEPTS: Prostate–kidney link, PSA + treatment + protection triad.

COPY-READY PROMPT:

```
Open Graph social share card, exactly 1200 × 630 px, pure white (#ffffff) background. Left two-thirds: bold condensed navy (#0f1e2e) headline "Prostate Cancer & Your Kidneys", with a clinical teal (#1a6b72) subhead beneath: "PSA testing · treatment risks · kidney protection". A thin teal rule separates headline from subhead, with small renal-green (#1f7a4d) and amber (#b8860b) accent dots. Right third: a clean semi-photorealistic 3D render of two teal-toned kidneys with a small prostate anatomy icon below them, connected by faint teal ductwork (ureters), floating on the white background with a soft natural drop shadow. Publication-grade nephrology editorial design, generous negative space, legible as a small mobile thumbnail. Small semi-transparent navy "williamriveromd.com" attribution in the bottom-right corner.

NEGATIVE: No dark/navy background fill, no clutter, no tiny unreadable text, no AI gibberish, no neon gradients.
META PAIRING: og:image:width="1200", og:image:height="630".
```

---

## IMAGE 4 — Management Algorithm
*(authored with `williamriveromd-infographic-skill`)*

SECTION PLACEMENT: "Management Algorithm" (clinician tab)
FILE NAME: `prostate-cancer-ckd-management-algorithm.png`
ARCHETYPE: Clinical Algorithm / Flowchart
AUDIENCE: Clinicians
VISUAL MIX:
- photorealistic models: none
- 2D infographic: rounded decision/action/escalation nodes
- 3D component graphics: small kidney + lab-tube node accents
- algorithm/flowchart: primary
PURPOSE: Give clinicians a top-to-bottom onco-nephrology co-management pathway.
KEY CONCEPTS: Baseline staging → treatment-specific monitoring → escalation triggers → coordinated endpoint.
DIMENSIONS: 1024 × 1536 px (2:3 portrait)

COPY-READY PROMPT:

```
Clinical nephrology algorithm infographic, premium KDIGO-style guideline flowchart aesthetic, white (#ffffff) background, top-to-bottom flow, portrait 1024 × 1536. Title in bold navy (#0f1e2e): "Prostate Cancer + CKD: Co-Management Pathway".

START node (navy): "New prostate cancer diagnosis in CKD" → "Baseline eGFR + urine protein + creatinine".

Branch by treatment type (four teal decision nodes side by side or stacked):
- "ADT (GnRH agonist)" → amber caution node: "Monitor metabolic syndrome — BP, glucose, lipids"
- "Chemotherapy" → amber node: "Dose-adjust carboplatin by eGFR; docetaxel = low renal risk"
- "Pelvic radiation" → amber node: "Watch ureteral stricture + scatter nephrotoxicity"
- "Contrast imaging" → amber node: "Pre-hydrate; avoid if avoidable; no NSAIDs"

MONITORING node (teal): "Creatinine, eGFR, urine protein every 3 months during treatment".

ESCALATION node (red): "Rising creatinine OR hydronephrosis / obstruction → urgent nephrology + urology referral; relieve obstruction (stent / nephrostomy)".

ENDPOINT node (renal green #1f7a4d): "Coordinated onco-nephrology care — kidney function preserved, treatment options retained".

Rounded nodes, navy structure lines, teal recommendation boxes, amber caution nodes, red escalation node, green optimal endpoint. Maximum 4 branching levels, no spaghetti, generous whitespace, mobile-readable labels. Bottom-center: small semi-transparent navy "williamriveromd.com".

NEGATIVE: No spaghetti flowchart, no dark background, no tiny labels, no AI gibberish.
```

---

## IMAGE 5 — Kidney Protection Multi-Panel Infographic
*(authored with `williamriveromd-infographic-skill`)*

SECTION PLACEMENT: "Protecting Your Kidneys During Treatment" (patient tab)
FILE NAME: `prostate-cancer-ckd-kidney-protection-infographic.png`
ARCHETYPE: Multi-Panel Educational Infographic
AUDIENCE: Patients
VISUAL MIX:
- photorealistic models: one small Filipino patient-and-nurse corner scene
- 2D infographic: six modular panels with icons
- 3D component graphics: IV saline bag, kidney icon
- algorithm/flowchart: none
PURPOSE: Give patients six concrete kidney-protection actions during cancer treatment.
KEY CONCEPTS: Monitoring, hydration, NSAID avoidance, dose adjustment, care coordination, warning signs.
DIMENSIONS: 1792 × 1024 px (16:9)

COPY-READY PROMPT:

```
Patient education infographic poster, landscape 16:9 (1792 × 1024), modern nephrology clinic aesthetic, clean white (#ffffff) background. Top hero header in bold navy (#0f1e2e): "Protecting Your Kidneys During Prostate Cancer Treatment".

Six rounded modular panels on a very soft gray (#f3f4f6) field, each with a clean icon, a bold label, and one short line:
1. "Monitor kidney function" — creatinine, eGFR, urine protein every 3 months (teal accent)
2. "Hydrate before contrast or chemo" — IV saline pre-hydration, with a small 3D saline-bag icon (teal accent)
3. "Avoid NSAIDs" — no ibuprofen, mefenamic acid, or naproxen for pain (amber #b8860b warning accent)
4. "Dose-adjust kidney-cleared drugs" — ask if your chemo dose fits your eGFR (teal accent)
5. "Coordinate your team" — oncologist + nephrologist together (renal green #1f7a4d accent)
6. "Know the warning signs" — less urine, swelling, severe back pain (clinical red #b91c1c accent)

Include one small photorealistic Filipino patient-and-nurse scene in a corner panel for warmth. Bottom full-width banner in soft gray with navy take-home text: "Healthy kidneys = more treatment options." Navy/teal/green palette, mobile-readable labels, not cluttered, generous whitespace. Small semi-transparent navy "williamriveromd.com" attribution in the bottom-right corner.

NEGATIVE: No cartoon style, no clutter, no dark background, no tiny unreadable labels, no AI gibberish text.
```

---

## IMAGE 6 — PSA-in-CKD Decision Reference Card
*(authored with `williamriveromd-simple-figure`, Scaffold E)*

FILE NAME: `prostate-cancer-ckd-psa-reference-card.png`
IMAGE TYPE: Scaffold E — Reference Table / Quick-Look Card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: Clinicians
VISUAL GOAL: One-glance mapping of a PSA value/trend to its CKD-specific consideration and recommended action.

PROMPT:

```
Clinical reference card, publication-grade nephrology design. White (#ffffff) background, 4:3 (1536 × 1152). Bold navy (#0f1e2e) title at top: "Interpreting PSA in CKD". Compact, well-organized three-column table with a header row and four data rows.

Column headers in clinical teal (#1a6b72) on a soft gray (#f3f4f6) band: "PSA Scenario" | "CKD Consideration" | "Recommended Action".

Rows (alternating white / very soft gray fills):
1. "PSA < 4 ng/mL" | "May still harbor cancer in advanced CKD" | "Annual DRE; free PSA if borderline"
2. "PSA 4–10 ng/mL (gray zone)" | "CKD can falsely elevate into this range" | "Free/total PSA ratio + MRI prostate"  — highlight this entire row with a soft amber (#b8860b) tint to flag the gray zone
3. "PSA > 10 ng/mL" | "More likely significant; CKD less likely the sole cause" | "Urgent urology referral; biopsy discussion"  — value cell emphasized in clinical red (#b91c1c)
4. "Rising PSA trend" | "More meaningful than a single value in CKD" | "Track PSA velocity; repeat in 3–6 months"

Small 3D blood-collection-tube accent icon near the title. Footer takeaway in navy: "In CKD, a single PSA number is not enough — trend and free/total ratio matter more." Mobile-readable, not cluttered, generous whitespace. Bottom-right corner: small semi-transparent navy "williamriveromd.com".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically plausible, visually calm, publication-grade, consistent with williamriveromd.com house style. White/light background only. williamriveromd.com attribution visible bottom-right.
```
