#!/usr/bin/env python3
"""
El Niño Heat & Dialysis — Image Generation Pipeline
Runs locally on your Mac. Calls OpenAI gpt-image-1 API to generate all
6 guide images, saves them as JPG in ./generated_images/

Usage:
    python3 generate_el_nino_images.py

Requirements:
    pip install openai pillow
"""

import os, sys, base64, json
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Installing openai...")
    os.system("pip install openai pillow -q")
    from openai import OpenAI

# ── Load key from .env or environment ──────────────────────────────────────
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            os.environ["OPENAI_API_KEY"] = line.split("=", 1)[1].strip()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found. Add it to .env or set it in your shell.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

OUT = Path("generated_images")
OUT.mkdir(exist_ok=True)

# ── Image definitions ───────────────────────────────────────────────────────
IMAGES = [
    {
        "filename": "el-nino-heat-dialysis-hero",
        "size": "1536x1024",
        "prompt": """Photorealistic medical editorial hero image for a Philippine nephrology patient-education guide. Split-scene composition, two atmospheric zones bleeding together through a heat-haze transition.

LEFT ZONE (45% of frame): Filipino urban street at blazing noon El Niño season. Cracked concrete pavement, blinding white sky, shimmer heat-haze lines rising off asphalt. A motionless ceiling fan on an exterior wall — power is out. LED weather signboard in background showing "42.5°C HEAT INDEX >42°C". Bleached amber, burnt orange, dusty off-white palette. No people.

RIGHT ZONE (55% of frame): Interior of a modest clean Filipino home. A Filipino male patient, 55–65 years old, seated in a padded medical recliner chair, light short-sleeve shirt. Left forearm rests on chair arm, AV fistula naturally visible — slight vessel prominence, small teal bandage detail. Dialysis tubing line from IV stand nearby. Side table: a single small 300ml sealed water bottle, blood pressure cuff, digital weighing scale, thermometer. Patient expression: calm, watchful, prepared. A Filipino female caregiver (wife, 40s–50s) stands beside him holding a handwritten fluid log notepad, looking attentively at the patient. Louvered window with warm-striped light. Ceiling fan overhead — motionless.

TRANSITION: Heat-haze shimmer gradient between zones — outdoor amber-heat bleeds into clinical interior.

LIGHTING: Cinematic but restrained editorial photography. Shallow depth of field: patient and caregiver sharp, outdoor zone atmospheric blur. Realistic Filipino skin texture. Color temperature contrast: warm bleached exterior, cooler interior. Light film-grain texture.

NEGATIVE SPACE: Clean semi-dark band across upper-left 20–25% of frame for title text overlay.

Style: Premium Philippine healthcare editorial photography. NEJM/Lancet feature image quality. No text embedded in image. No cartoon elements. No Western hospital setting."""
    },
    {
        "filename": "el-nino-eskd-thermoregulation-pathophys",
        "size": "1536x1024",
        "prompt": """Medical pathophysiology infographic poster, AJKD/NEJM graphical abstract style. White background with soft gray section panels. Navy (#1f3864) and teal (#1a6b72) headers, amber (#b8962e) caution callouts, red (#b91c1c) danger indicators.

TITLE BAR (navy background, white text): "Why Heat Is Dangerous in Dialysis — The ESKD Thermoregulation Crisis"

THREE-COLUMN LAYOUT:

COLUMN 1 — "Healthy Person" (teal border): Semi-realistic cross-section of a functioning kidney, normal cortex. Arrow flow: Heat exposure → sweating (sweat gland cross-section) → fluid lost → person drinks → kidneys excrete urine → balance restored. All arrows green. Label: "Balance maintained."

COLUMN 2 — "Dialysis Patient" (red border): Scarred contracted kidney, non-functioning, fibrotic texture. Arrow flow: Heat → sweating → thirsty → drinks water → NO urine output (red X) → fluid accumulates in lungs/ankles (amber schematic) → weight gain, breathlessness. Arrows amber/red. Label: "Fluid overload before next session."

COLUMN 3 — "Compounding Risks" (amber border): Four stacked amber cards:
1. HYPERKALEMIA: K+ ion icon. "Muscle breakdown in heat releases K+. No excretion route. Arrhythmia risk."
2. HYPOTENSION: BP cuff icon. "Excessive UF in heat amplifies intradialytic hypotension. Dialysate cooling first line."
3. HEAT STROKE: Brain+thermometer icon. "Impaired autonomic thermoregulation in ESKD blunts early warning signs."
4. MISSED SESSION: Dialysis machine icon. "One missed session + increased fluid intake = compounded risk."

BOTTOM BAND (navy, white text): "Standard heat advice ('drink more water') is dangerous for dialysis patients."

Style: Publication-grade AJKD/NEJM. Modular clean layout. Semi-photorealistic 3D kidney rendering. No paragraph text — all concise 1–2 line statements. Highly readable."""
    },
    {
        "filename": "el-nino-four-heat-emergencies-patient",
        "size": "1536x1024",
        "prompt": """Patient education infographic poster, landscape 16:9. Modern Philippine nephrology clinic aesthetic. Clean white background, rounded card panels, navy (#1f3864) headers, teal (#1a6b72) action boxes, amber (#b8962e) warning, red (#b91c1c) emergency.

TOP HEADER (navy, full width): White bold title: "4 HEAT EMERGENCIES — RECOGNIZE FAST, ACT FAST" Teal subtitle: "For dialysis patients and families · El Niño Season"

FOUR PANELS (2×2 grid):

PANEL 1 — HEAT EXHAUSTION (amber border): Signs: heavy sweating, cool pale skin, fast weak pulse, nausea, muscle cramps, dizziness. Action box (teal): Move to cool area, cool wet cloth to neck/armpits, do NOT give extra fluids, call dialysis center. Small inset: Filipino patient under fan, caregiver nearby.

PANEL 2 — HEAT STROKE (red border): "EMERGENCY — Call 911 now." Signs: hot dry/wet skin, very high temp, confusion, loss of consciousness. Action box (red): Call emergency immediately, ice packs cervical/groin/axilla, lay flat, do not give fluids by mouth. Small 3D thermometer showing extreme temperature.

PANEL 3 — SEVERE HYPERKALEMIA (amber-red border): Signs: muscle weakness, palpitations, numbness/tingling, nausea. Small ECG strip with peaked T waves. Risk trigger: "Missed session + high-K+ foods in heat." Action: Call dialysis center NOW, do not eat, go to ER if worsening.

PANEL 4 — INTRADIALYTIC HYPOTENSION (amber border): Signs during session: sudden BP drop, dizziness, leg cramps, nausea, sweating. Heat note: "More common in extreme heat — UF rate may exceed safe limits." Action: Tell nurse immediately, lie flat, small saline bolus. Small 3D blood pressure gauge.

FOOTER (navy): "When in doubt — call your dialysis center. Go to ER if: confusion, chest pain, loss of consciousness."

Style: Clean modular. Filipino patient thumbnails. Emergency color hierarchy clear. Mobile-readable. Print-ready A4."""
    },
    {
        "filename": "el-nino-clinician-rapid-heat-protocol",
        "size": "1024x1536",
        "prompt": """Clinical nephrology reference card, portrait orientation. White background. Navy (#1f3864) section headers, teal (#1a6b72) recommendation boxes, amber (#b8962e) caution nodes, red (#b91c1c) escalation, green (#166534) optimal pathway.

CARD HEADER (navy band): White bold: "RAPID HEAT PROTOCOL — HD UNIT · EL NIÑO SEASON" Teal: "Pre-session screen · Intradialytic adjustments · Emergency triage"

SECTION 1 — PRE-DIALYSIS SCREEN (teal left border): Four assessment rows:
- Pre-session weight: target ≤0.5 kg/day; amber trigger >1.0 kg/day
- Pre-session BP: target SBP 130–160; amber <110 or >180
- Temperature: afebrile; red trigger >38.5°C
- Serum K+: target <5.5; red trigger >6.0
Small 3D lab tube in margin.

SECTION 2 — INTRADIALYTIC ADJUSTMENTS (teal header): Three protocol boxes:
Green box: "Dialysate Temperature: 35.0–35.5°C" with 3D dialysis machine dial at 35°C
Green box: "UF Rate Cap: ≤10 mL/kg/hour" with UF gauge in safe zone
Amber box: "Avoid high-sodium dialysate — amplifies thirst and interdialytic weight gain"

SECTION 3 — HEAT EMERGENCY TRIAGE (red left border): Three-level triage ladder:
Level 1 HEAT EXHAUSTION (amber node): Reduce UF, cool saline, monitor BP q5min, do not terminate
Level 2 HEAT STROKE (red node): TERMINATE SESSION, call emergency services, ice packs, IV access
Level 3 SEVERE HYPERKALEMIA (red node): Emergency dialysis, calcium gluconate, bicarb, glucose+insulin

SECTION 4 — SPECIAL POPULATIONS (amber border, compact 2×2 grid):
- Diabetic autonomic neuropathy: monitor core temp actively
- Cardiorenal syndrome: start at 35°C dialysate
- Elderly >70: pre-cool dialysis room
- PD patients: review exchange volume

FOOTER (navy): "PAGASA El Niño 2026 · 79% probability July–September 2026 · williamriveromd.com"

Style: KDIGO guideline reference card. Clean large readable values. Vertical flow. No spaghetti. Print-ready A4 portrait."""
    },
    {
        "filename": "el-nino-brownout-water-rationing-dialysis",
        "size": "1536x1024",
        "prompt": """Patient education infographic poster, landscape 16:9. Clean white background. Navy (#1f3864) and amber (#b8962e) headers, teal (#1a6b72) action boxes, red (#b91c1c) danger callouts. Modern Philippine clinic aesthetic, rounded cards.

TOP HEADER (navy, full width): White bold: "SURVIVING BROWNOUTS & WATER RATIONING ON DIALYSIS" Teal: "Practical steps for HD and PD patients — El Niño 2026" Inset right: small photorealistic Filipino family (parents + adult child) with generator and water storage container, calm and organized. Circle crop thumbnail.

THREE PANELS (horizontal thirds):

PANEL 1 — POWER BROWNOUT SURVIVAL (amber header, lightning icon):
HD patients timeline card:
• <1 hour: center likely has generator — call ahead
• 1–4 hours: most centers complete session on backup
• >4 hours: session may cancel — never miss >1 session without a plan

PD patients (teal card): CAPD continues without power. APD cycler needs power — switch to manual CAPD 4×2L if >2 hour outage.

Medication cold chain (red callout): 3D insulated bag with cool pack and insulin pen. "Move insulin + EPO to insulated bag within 30 min of outage. Replace cool packs every 4–6 hours."

PANEL 2 — WATER RATIONING (teal header, water drop icon):
Priority pyramid (navy, 3 tiers):
TOP (red): Access site cleaning — non-negotiable daily even in severe rationing
MIDDLE (amber): Drinking water — boil all tap water 1 full minute. Store 3 days' supply.
BOTTOM (green): Bathing — reduce to once daily if needed

PD special note (teal card): 3D PD dialysate bag stack. "RO water for dialysate prepared at center. If rationing affects your PD facility — call nurse immediately."

PANEL 3 — PREPARATION CHECKLIST (green header, checkmark icon):
Checklist with checkbox items:
□ Know dialysis center's generator policy
□ 48-hour backup medication supply at home
□ Insulated bag + 4 cool packs ready
□ 3-day water storage ready
□ Center's brownout cancellation protocol
□ Nephrologist's emergency number saved
□ PD patients: know manual CAPD procedure
□ Written medication list for ER visits

Amber callout: "Each item checked = one less crisis during the brownout."

FOOTER (navy): "Preparation before June = survival through September. williamriveromd.com"

Style: Practical action-oriented. Filipino family thumbnail. Three 3D objects ground advice. Mobile-readable. Print-ready A4."""
    },
    {
        "filename": "el-nino-fluid-management-heat-paradox",
        "size": "1536x1024",
        "prompt": """Patient education infographic poster, landscape 16:9. White background. Warm amber (#b8962e) and red (#b91c1c) on danger side, teal (#1a6b72) and green (#166534) on safe strategy side. Navy (#1f3864) structural headers. Rounded card panels.

TOP HEADER (navy, full width): White bold: "THE HEAT PARADOX — You Are Thirsty AND Fluid-Overloaded" Teal: "How to cool down without endangering yourself · Fluid management in extreme heat"

CENTER MECHANISM DIAGRAM (full-width strip, 28% of frame height):
Two parallel lanes left to right:

Top lane (amber, label "WHAT HEAT DOES TO YOU"):
Heat sun icon → sweating figure → thirst signal (brain icon) → patient reaching for water → water enters body → fluid pool grows (amber→red) → legs swell, lungs fill (red warning icon)

Bottom lane (teal, label "WHAT YOUR KIDNEYS CANNOT DO"):
Water glass → scarred kidney with red X → "No urine output" text → all fluid stays → interdialytic weight scale showing +0.5, +1.0, +2.0 kg progression getting darker red

CENTER CONNECTOR (navy callout box between lanes):
"PARADOX: Thirsty + Fluid Overloaded at the same time. Following normal heat advice makes the bottom lane worse."

Small inset circle: Filipino male patient, 60s, thoughtful expression, small water bottle in hand.

TWO LOWER PANELS:

PANEL LEFT — "YOUR DAILY FLUID ALLOWANCE" (teal border):
Four teal cards:
• "Know your limit — most HD patients: 700–1000 mL/day"
• "Count EVERYTHING — soup, ice cream, gelatin, high-water fruits"
• "Spread it out — save some allowance for afternoon heat peak"
• "Weigh daily — gain >0.5 kg/day = too much fluid. Call center."

PANEL RIGHT — "COOL DOWN WITHOUT DRINKING MORE" (green border):
Four illustrated 2×2 mini-tiles:
Tile 1 (green): 3D ice cube cluster. "Suck on small ice chips — same cooling, far less fluid volume"
Tile 2 (green): Cool folded cloth. "Cold damp cloth to neck, forehead, inner wrists"
Tile 3 (green): Cup with swish motion. "Rinse mouth with cold water — spit it out. Tricks thirst sensors"
Tile 4 (green): Fan with mist spray. "Electric fan + light skin mist = evaporative cooling, zero fluid intake"

AMBER WARNING STRIP (between panels):
"⚠️ Signs of TRUE dehydration: extreme dizziness, confusion, very dry mouth. Call your nephrologist — do not self-treat with extra water."

FOOTER (navy): Left: "The goal: stay cool AND stay within your limit." Right (teal): "Fluid log + daily weight = your two essential tools."

Style: Clean practical patient-centered. Central paradox diagram is visual anchor. Warm/cool color coding intuitive. No walls of text. Short active-voice statements. Mobile-readable 375px. Print-ready A4."""
    }
]

# ── Generation loop ─────────────────────────────────────────────────────────
print(f"\nGenerating {len(IMAGES)} images via gpt-image-1...\n")

for i, img in enumerate(IMAGES, 1):
    out_jpg = OUT / f"{img['filename']}.jpg"
    out_png = OUT / f"{img['filename']}.png"

    if out_jpg.exists():
        print(f"[{i}/{len(IMAGES)}] SKIP (already exists): {out_jpg.name}")
        continue

    print(f"[{i}/{len(IMAGES)}] Generating: {img['filename']} ({img['size']})...")

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=img["prompt"],
            size=img["size"],
            quality="high",
            n=1,
        )

        # gpt-image-1 returns base64 by default
        image_data = response.data[0].b64_json
        if image_data:
            img_bytes = base64.b64decode(image_data)
            out_png.write_bytes(img_bytes)
            # Convert PNG to JPG
            from PIL import Image as PILImage
            with PILImage.open(out_png) as pil_img:
                rgb = pil_img.convert("RGB")
                rgb.save(out_jpg, "JPEG", quality=92, optimize=True)
            out_png.unlink()  # remove intermediate PNG
            print(f"   ✓ Saved: {out_jpg} ({out_jpg.stat().st_size // 1024} KB)")
        else:
            # Fallback: URL response
            url = response.data[0].url
            import urllib.request
            urllib.request.urlretrieve(url, out_jpg)
            print(f"   ✓ Saved via URL: {out_jpg}")

    except Exception as e:
        print(f"   ✗ Error on {img['filename']}: {e}")
        continue

print(f"\nDone. Images saved to: {OUT.resolve()}")
print("\nNext step: drop all files from generated_images/ into the")
print("images/ folder of the repo via the Claude Code file panel.")
print("Claude will handle WebP conversion + HTML injection automatically.")
