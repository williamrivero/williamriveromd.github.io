#!/usr/bin/env python3
"""
patch_calc_cards.py
Inserts teal "Open Calculator →" cards into related guide HTML files,
placed just before <!-- DR CARD -->.

Usage:
  python3 patch_calc_cards.py              # apply to all mapped guides
  python3 patch_calc_cards.py --dry-run    # preview only
  python3 patch_calc_cards.py --guide understanding-ckd.html
"""

import re, sys, os, argparse

GUIDES_DIR = "guides"

MARKER_START = "<!-- CALC-CARDS-START -->"
MARKER_END   = "<!-- CALC-CARDS-END -->"

CSS_BLOCK = """\
/* ── CALC CARDS ── */
.calc-cards-wrap{margin:40px 0 8px;padding:0 var(--page-pad,20px);}
.calc-cards-label{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--teal);margin-bottom:12px;}
.calc-card{display:flex;align-items:center;gap:14px;background:rgba(26,107,114,.07);border:1px solid rgba(26,107,114,.2);border-radius:12px;padding:14px 16px;text-decoration:none;color:inherit;margin-bottom:10px;transition:border-color .18s,box-shadow .18s;}
.calc-card:hover{border-color:var(--teal);box-shadow:0 2px 14px rgba(26,107,114,.14);}
.calc-card-icon{width:36px;height:36px;flex:none;background:var(--teal);color:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;font-weight:700;line-height:1;}
.calc-card-body{flex:1;min-width:0;}
.calc-card-title{font-size:.88rem;font-weight:700;color:var(--teal);margin-bottom:2px;}
.calc-card-desc{font-size:.78rem;color:var(--text-mid,#4b5563);line-height:1.4;}
.calc-card-arrow{flex:none;font-size:.8rem;font-weight:700;color:var(--teal);white-space:nowrap;padding-left:8px;}"""

# Mapping: guide filename → list of (calc_href, calc_title, calc_desc)
CALC_MAP = {
    "understanding-ckd.html": [
        ("calc-egfr-ckd-epi.html",
         "eGFR Calculator — CKD-EPI 2021",
         "Enter creatinine ± cystatin C, age and sex to get your eGFR and CKD stage heatmap."),
        ("calc-kfre.html",
         "Kidney Failure Risk Equation (KFRE)",
         "Predicts your 2- and 5-year probability of reaching kidney failure — guides dialysis planning timing."),
        ("calc-ckd-progression-slope.html",
         "CKD Progression — eGFR Slope & Time to Kidney Failure",
         "Enter serial eGFR values to compute annual decline rate and projected time to dialysis."),
    ],
    "slowing-ckd-progression.html": [
        ("calc-kfre.html",
         "Kidney Failure Risk Equation (KFRE)",
         "Predicts 2- and 5-year kidney failure risk from age, sex, eGFR and UACR."),
        ("calc-ckd-progression-slope.html",
         "CKD Progression — eGFR Slope & Time to Kidney Failure",
         "Serial eGFR values → annual decline rate and projected time to dialysis."),
    ],
    "proteins-proteinuria.html": [
        ("calc-proteinuria-uacr.html",
         "Proteinuria & UACR Staging — KDIGO Calculator",
         "Stage albuminuria (A1–A3) from UACR or PCR — combined with eGFR for the full CKD risk grid."),
    ],
    "glomerulonephritis.html": [
        ("calc-igan-prediction.html",
         "International IgA Nephropathy Prediction Tool",
         "2- and 5-year ESKD risk from creatinine, proteinuria, BP and Oxford MEST-C score."),
    ],
    "anemia-management.html": [
        ("calc-iron-status-tsat.html",
         "Iron Status in CKD — TSAT & Ferritin Interpretation",
         "TSAT + ferritin → functional vs. absolute iron deficiency with KDIGO thresholds."),
        ("calc-esa-dose-adjustment.html",
         "ESA / EPO Dose Adjustment — CKD Anemia",
         "Dose-adjustment guide for EPO, darbepoetin and MIRCERA based on Hb response."),
        ("calc-iron-deficit-ganzoni.html",
         "Iron Deficit & IV Iron Dose — Ganzoni Equation",
         "Calculates total iron deficit and recommended IV iron repletion dose."),
    ],
    "ckd-mbd.html": [
        ("calc-ckd-mbd.html",
         "CKD-MBD Calculator — Ca×P Product, Corrected Ca & PTH Staging",
         "Computes Ca×P product, albumin-corrected calcium, and maps PTH against KDIGO targets by CKD stage."),
        ("calc-corrected-calcium.html",
         "Corrected Calcium for Albumin (Payne Formula)",
         "Adjusts serum calcium for low albumin — critical in CKD where hypoalbuminaemia is common."),
    ],
    "managing-kidney-stones.html": [
        ("calc-stone-passage-risk.html",
         "Kidney Stone Passage Risk — STONE Score",
         "5-variable score predicts spontaneous passage — guides tamsulosin (MET) vs. urological referral."),
        ("calc-stone-prevention-fluid.html",
         "Kidney Stone Prevention — Fluid Target & Dietary Risk",
         "Computes daily fluid intake to reach ≥2.5 L urine output; flags oxalate, purine and citrate risks."),
    ],
    "fluid-management-dialysis.html": [
        ("calc-idwg-fluid.html",
         "Interdialytic Weight Gain & Fluid Removal Calculator",
         "Converts IDWG to % of dry weight; computes required UF volume and flags safe vs. high UF rate."),
        ("calc-ultrafiltration-rate.html",
         "Ultrafiltration Rate Calculator",
         "UFR in mL/hr/kg — flags the KDOQI <13 mL/hr/kg cardiovascular safety threshold."),
    ],
    "lupus-nephritis.html": [
        ("calc-sledai.html",
         "SLEDAI-2K & SLICC/ACR Damage Index (Lupus)",
         "Scores SLE disease activity (SLEDAI-2K) and cumulative organ damage — guides treatment escalation."),
    ],
    "obesity-ckd.html": [
        ("calc-bmi-bsa-ibw.html",
         "BMI, BSA & Ideal Body Weight — Asian-Pacific Cutoffs",
         "BMI with Filipino/Asian cutoffs (overweight ≥23), BSA (Mosteller), IBW and adjusted BW for drug dosing."),
    ],
    "kidney-transplant.html": [
        ("calc-transplant-prom.html",
         "Transplant PROMs — Adherence (BAASIS), KTQ, PHQ-9 & GAD-7",
         "Medication adherence, kidney transplant quality of life, depression and anxiety screening tools."),
        ("calc-allograft-egfr-trend.html",
         "Kidney Allograft eGFR Trend & Time to Failure",
         "Serial post-transplant eGFR values → slope, half-life, and projected time to allograft failure."),
    ],
    "transplant-allograft-failure.html": [
        ("calc-allograft-egfr-trend.html",
         "Kidney Allograft eGFR Trend & Time to Failure",
         "Serial post-transplant eGFR values → slope, half-life, and projected time to allograft failure."),
    ],
    "acute-kidney-injury-on-ckd.html": [
        ("calc-aki-staging.html",
         "Acute Kidney Injury Staging — KDIGO, AKIN & RIFLE",
         "Stages AKI by creatinine rise or urine output using all three criteria sets."),
    ],
    "living-with-dialysis.html": [
        ("calc-dialysis-prom.html",
         "Dialysis PROMs — KDQOL-36, DSI & IPOS-Renal",
         "Three validated patient-reported outcome tools — symptom burden, kidney impact, palliative needs."),
    ],
    "metabolic-acidosis-ckd.html": [
        ("calc-bicarb-deficit.html",
         "Bicarbonate Deficit & Correction Calculator",
         "Calculates total bicarb deficit from serum HCO₃ and body weight with correction rate guidance."),
        ("calc-anion-gap-acid-base.html",
         "Anion Gap, Albumin-Corrected AG, Delta Ratio & Winter's Formula",
         "Full acid-base workup in one tool — AG, corrected AG, delta-delta, and Winter's expected PCO₂."),
    ],
    "diabetes-kidneys.html": [
        ("calc-dkd-risk.html",
         "Diabetic Kidney Disease — DKD Risk & SGLT2i Eligibility",
         "DKD risk staging from HbA1c, UACR and eGFR; flags SGLT2i eligibility and estimated average glucose."),
        ("calc-insulin-dose.html",
         "Insulin Dosing in CKD — Starting Dose, Correction Factor & Carb Ratio",
         "Weight-based starting insulin dose with CKD-adjusted correction factor and insulin:carb ratio."),
    ],
    "managing-hypertension.html": [
        ("calc-bp-map.html",
         "Blood Pressure — MAP, Pulse Pressure & CKD Target",
         "Calculates MAP and pulse pressure; flags the CKD BP target (≤120/80 per KDIGO 2024)."),
    ],
    "dyslipidemia-2026.html": [
        ("calc-lipid-panel.html",
         "Lipid Panel Interpreter — LDL, Non-HDL & Friedewald",
         "Calculates Friedewald LDL and non-HDL cholesterol; maps to ACC/AHA 2026 and KDIGO CKD targets."),
        ("calc-statin-intolerance.html",
         "Statin Intolerance & SAMS Management Aid",
         "Guides statin-associated muscle symptom (SAMS) evaluation — rechallenge, dose reduction or switch algorithm."),
    ],
    "gout-uric-acid.html": [
        ("calc-uric-acid.html",
         "Uric Acid Risk & Urate Target Calculator",
         "Estimates gout risk from serum uric acid; sets CKD-adjusted urate target and flags allopurinol dosing."),
        ("calc-gout-classification.html",
         "2015 ACR/EULAR Gout Classification Criteria",
         "Scores clinical, lab and imaging domains — ≥8 points classifies as gout when crystals are not confirmed."),
    ],
    "nutrition-kidney-patients.html": [
        ("calc-ckd-nutrition-rx.html",
         "CKD Nutrition Prescription — Protein, Energy, K, P, Na & Fluid Targets",
         "Body-weight–based CKD nutrition targets — protein, calories, potassium, phosphorus, sodium and fluid by CKD stage."),
        ("calc-nutrition-screening.html",
         "Malnutrition Screening in CKD — SNAQ, MIS & SGA",
         "Three validated nutritional screening tools — flags protein-energy wasting risk in CKD and dialysis patients."),
    ],
    "sodium-salt-reduction-ckd.html": [
        ("calc-sodium-intake.html",
         "Sodium Intake Estimator — Filipino Foods",
         "Estimates daily sodium from Filipino condiments and dishes — patis, toyo, bagoong, instant noodles."),
    ],
    "exercise-guide-ckd.html": [
        ("calc-exercise-hr-zones.html",
         "Exercise Target Heart-Rate Zones (Karvonen) & Energy",
         "Karvonen formula for 5 training zones using resting HR; calorie estimate per session for CKD patients."),
    ],
    "dialysis-adequacy.html": [
        ("calc-dialysis-adequacy-ktv.html",
         "Dialysis Adequacy Calculator — spKt/V & URR (Daugirdas)",
         "Calculates spKt/V using Daugirdas II equation and URR — with KDIGO 2024 adequacy target interpretation."),
    ],
    "dialysis-prescription.html": [
        ("calc-dialysis-prescription.html",
         "Dialysis Prescription Calculators — RKF, Kt/V, UFR, nPCR, PD Kt/V",
         "Full prescription toolkit — residual kidney function contribution, UFR safety check, nPCR, and PD adequacy."),
    ],
    "dengue-aki-kidney.html": [
        ("calc-dengue-aki-risk.html",
         "Dengue-Associated AKI Risk Estimator",
         "Estimates AKI risk and severity in dengue patients — guides monitoring frequency and nephrology referral."),
    ],
}


def build_cards_html(calcs):
    cards = ""
    for href, title, desc in calcs:
        cards += (
            f'    <a href="{href}" class="calc-card">\n'
            f'      <div class="calc-card-icon">⌬</div>\n'
            f'      <div class="calc-card-body">\n'
            f'        <div class="calc-card-title">{title}</div>\n'
            f'        <div class="calc-card-desc">{desc}</div>\n'
            f'      </div>\n'
            f'      <span class="calc-card-arrow">Open →</span>\n'
            f'    </a>\n'
        )
    label_en  = "Try the Calculator" if len(calcs) == 1 else "Try the Calculators"
    label_tl  = "Gamitin ang Calculator" if len(calcs) == 1 else "Gamitin ang mga Calculator"
    label_ceb = "Gamita ang Calculator" if len(calcs) == 1 else "Gamita ang mga Calculator"
    label_kap = "Gamitin ing Calculator" if len(calcs) == 1 else "Gamitin ing mga Calculator"
    return (
        f"{MARKER_START}\n"
        f'<div class="calc-cards-wrap">\n'
        f'  <div class="calc-cards-label">'
        f'<span data-lang="en">{label_en}</span>'
        f'<span data-lang="tl" class="lang-hidden">{label_tl}</span>'
        f'<span data-lang="ceb" class="lang-hidden">{label_ceb}</span>'
        f'<span data-lang="kap" class="lang-hidden">{label_kap}</span>'
        f'</div>\n'
        f'{cards}'
        f'</div>\n'
        f"{MARKER_END}\n"
    )


def patch_guide(path, calcs, dry_run=False):
    with open(path) as f:
        html = f.read()

    # Remove existing block
    html = re.sub(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END) + r"\n?",
        "", html, flags=re.DOTALL
    )

    cards_html = build_cards_html(calcs)

    # Insert before <!-- DR CARD -->
    if "<!-- DR CARD -->" in html:
        html = html.replace("<!-- DR CARD -->", cards_html + "<!-- DR CARD -->", 1)
    else:
        print(f"  WARNING: no <!-- DR CARD --> in {path} — skipping")
        return False

    # Inject CSS if missing
    if ".calc-card{" not in html:
        css_insert = "\n" + CSS_BLOCK + "\n"
        html = re.sub(r'(</style>)', css_insert + r'\1', html, count=1)

    if dry_run:
        print(f"  DRY RUN: {os.path.basename(path)} — {len(calcs)} card(s)")
        return True

    with open(path, "w") as f:
        f.write(html)
    print(f"  ✓  {os.path.basename(path)} — {len(calcs)} card(s)")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--guide", default=None)
    args = parser.parse_args()

    if args.guide:
        key = os.path.basename(args.guide)
        if key not in CALC_MAP:
            print(f"No calc mapping defined for {key}")
            sys.exit(1)
        targets = {key: CALC_MAP[key]}
    else:
        targets = CALC_MAP

    ok = err = 0
    for guide, calcs in targets.items():
        path = os.path.join(GUIDES_DIR, guide)
        if not os.path.exists(path):
            print(f"  MISSING: {path}")
            err += 1
            continue
        if patch_guide(path, calcs, dry_run=args.dry_run):
            ok += 1
        else:
            err += 1

    print(f"\n{'DRY RUN ' if args.dry_run else ''}Done — {ok} patched, {err} skipped/missing")


if __name__ == "__main__":
    main()
