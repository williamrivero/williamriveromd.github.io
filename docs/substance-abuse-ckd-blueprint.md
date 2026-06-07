# Guide Blueprint — Substance Use & Chronic Kidney Disease

**Working filename:** `guides/substance-abuse-ckd.html`
**Slug:** `substance-abuse-ckd`
**Type:** Dual-mode guide (Patient/Family tab + Clinician tab), 4-language (EN/TL/CEB/KAP)
**Status:** Plan / blueprint — not yet built
**Author:** W. G. M. Rivero, MD, FPCP, DPSN
**Target review tag:** 2026 · KDIGO 2024 · ASAM 2024 · DOH PH advisories

---

## 1. Purpose & positioning

A single, comprehensive, non-judgmental guide on how **substances of use and misuse damage the
kidney** — and how patients who already have CKD can protect what kidney function remains. The site
already has a strong, standalone `alcohol-ckd.html`; this guide is the **umbrella reference** that
covers everything else and *cross-links* to alcohol rather than repeating it.

**Editorial stance:** harm-reduction, Filipino context, stigma-free. Substance use disorder is framed
as a treatable medical condition, not a moral failing. Every "what to avoid" is paired with a "what
to do instead / where to get help."

**Scope decision (avoid duplication):**

| Topic | Covered here | Defer to |
|---|---|---|
| Alcohol | Brief recap + nephrotoxicity table row, then link out | `alcohol-ckd.html` |
| NSAID / analgesic abuse | Yes — analgesic nephropathy is core | links to `nsaid-kidney-injury.html` |
| Opioids (incl. tramadol) | Yes | links to `pain-management-ckd.html` |
| Tobacco / vaping / nicotine | Yes — **no existing guide**, this fills the gap | — |
| Stimulants (shabu/methamphetamine, cocaine, "party drugs") | Yes — core | — |
| Cannabis / synthetic cannabinoids | Yes | — |
| Inhalants / solvents ("rugby") | Yes — Filipino public-health relevance | — |
| Herbal / "pampatunaw" / weight-loss & body-building supplements | Brief + link | `herbal-nephropathy.html`, `muscle-building-supplements-ckd.html`, `natural-supplements-kidney.html` |
| Caffeine / energy drinks | Brief + link | `caffeine-ckd.html` |
| Mental health, sleep, substance as coping | Brief + link | `ckd-mental-health-sleep.html` |

---

## 2. Title, meta & SEO

**Patient hero `<h1>` (EN):** "Substance Use & Your Kidneys — *Protecting What You Have*"
**Clinician hero `<h1>` (EN):** "Substance Use Disorders in CKD: *Clinical Management Guide*"

**`<title>`:** `Substance Use & Chronic Kidney Disease: Drugs, Tobacco & Recovery · W. G. M. Rivero, MD`

**Meta description (EN):** "How tobacco, stimulants (shabu), opioids, inhalants, and misused
painkillers and supplements injure the kidneys — and a stigma-free, evidence-based recovery roadmap
for Filipino patients with CKD. Patient and clinician views."

**Keywords:** substance abuse kidney disease, shabu kidney damage, methamphetamine nephropathy,
smoking CKD, opioid CKD, analgesic nephropathy, inhalant kidney, drug-induced AKI, recovery CKD
Philippines.

**Hero subtitle (EN):** "A judgment-free, evidence-based guide for Filipino patients — what each
substance does to your kidneys, the warning signs of kidney injury, drug interactions on dialysis,
and where to get help (DOH, free rehab, hotlines)."

**JSON-LD:** `MedicalWebPage`, `audienceType: "patient"`, `dateModified`/`datePublished` filled by
`patch_last_reviewed.py`. (Do not hand-write; the patch script owns this.)

---

## 3. Page architecture (matches house dual-mode skeleton)

```
<header class="site-header">           HOME · ← All Guides
<div class="guide-lang-bar">           EN / TL / CEB / KAP  (ids glb-en…glb-kap)
<div class="guide-toggle-bar">         Dark · Desktop
<div class="audience-tabs">            🧑‍⚕️ For Patients & Families | 🩺 For Clinicians
                                       (tab-pt active by default, tab-md)

<div class="mode-patient">             ← TEAL hero gradient
   <section class="hero">  +  hero <figure>/<picture> (fetchpriority high)
   <nav class="nav-strip"> patient pills
   <main class="container"> … patient sections …
</div>

<div class="mode-physician">           ← NAVY hero gradient (#0f1e2e→#1a2e4a), gold accent #d4af4f
   <section class="hero"> + clin-badges
   <nav class="nav-strip"> clinician pills
   <main class="container"> … clinician sections …
</div>

<!-- DR CARD -->  <div class="dr-card-wrap"> … </div>
<!-- RELATED-GUIDES-START --> <div class="related-guides"> … <!-- RELATED-GUIDES-END -->
<footer class="guide-footer"> … references …
```

**Critical conventions (from CLAUDE.md):**
- Start in **patient mode** (default CSS state). **Never** add a restore-on-load IIFE — `patch_mode_cls.py` strips it (CLS fix). `setMode()` may still write to `localStorage`.
- `dr-card-wrap` → `related-guides` → `footer` must be the last blocks, **outside** `<main>`, nothing between them. Enforced by `patch_signature_position.py`.
- Do **not** write CSS into the guide's master `<style>` — master CSS is owned by `patch_master_css.py`. Per-guide tweaks go in a second `<style>` block only.
- Every translatable string needs all four sibling `data-lang` spans (en/tl/ceb/kap). Missing one = blank content in that language.

---

## 4. PATIENT TAB — section outline

Nav pills: **Overview · How drugs hurt kidneys · Tobacco · Stimulants (shabu) · Opioids & painkillers · Inhalants · Cannabis · If you're on dialysis · Warning signs · Getting help**

1. **Overview — "Your kidneys filter everything you take in"**
   Plain-language framing. Kidneys + liver process every substance; CKD kidneys are already
   working with less reserve, so the margin for harm is smaller. Stigma-free promise.

2. **How substances injure kidneys (the 6 pathways)** — visual/infographic candidate:
   - Direct toxicity to tubules (e.g., solvents, contaminated stimulants)
   - Dehydration + heat (stimulants, all-night use) → AKI
   - Rhabdomyolysis (stimulants, immobility, seizures) → myoglobin AKI
   - Blood-pressure spikes & blood-vessel damage (stimulants, nicotine)
   - Infections from injecting (HIV, HBV, HCV) → kidney inflammation (HIVAN, cryoglobulinemia)
   - Risky combinations & adulterants (unknown contents of street drugs)

3. **Tobacco, vaping & nicotine** (fills site gap)
   - Smoking accelerates CKD progression and doubles risk of kidney failure; harms diabetic & hypertensive kidneys most.
   - Vaping ≠ safe; nicotine raises BP and constricts kidney blood vessels.
   - **Quitting works** — kidney decline slows even in established CKD. Link to local quit lines.

4. **Stimulants — shabu (methamphetamine), cocaine, "party drugs"**
   - Acute: severe hypertension, AKI, rhabdomyolysis, malignant hypertension → fast kidney failure.
   - Chronic: scarred blood vessels, proteinuria, accelerated CKD.
   - Heat + dehydration danger (esp. with PH climate / raves).

5. **Opioids & misused painkillers**
   - Tramadol/codeine misuse, and the big Filipino issue: **NSAID/analgesic overuse** (mefenamic
     acid for hangover/pain) → analgesic nephropathy & AKI. Cross-link `nsaid-kidney-injury.html`.
   - Overdose → low BP/oxygen → AKI. Naloxone awareness.
   - Pain *can* be managed safely in CKD → `pain-management-ckd.html`.

6. **Inhalants / solvents ("rugby", contact cement)**
   - Direct tubular toxicity, distal renal tubular acidosis, low potassium, muscle weakness, AKI.
   - Especially relevant for youth / street-connected populations.

7. **Cannabis & synthetic cannabinoids ("spice")**
   - Cannabis: smoking harms; hyperemesis → dehydration AKI; drug interactions.
   - Synthetic cannabinoids: reported AKI clusters — genuinely dangerous.

8. **Supplements & "natural" products that aren't kidney-safe** (short, link-out)
   - Body-building/weight-loss/"pampagana"/herbal pills with hidden steroids, NSAIDs, heavy metals,
     aristolochic acid. Link `muscle-building-supplements-ckd.html`, `herbal-nephropathy.html`,
     `natural-supplements-kidney.html`.

9. **If you're already on dialysis or CKD**
   - Substances alter how dialysis clears drugs; missed sessions; access infection from injecting;
     interaction with BP meds, phosphate binders, ESAs. Be honest with your nephrologist — it
     changes dosing, not their respect for you.

10. **Warning signs to seek care** (red-flag list)
    Less/dark urine, swelling, severe BP, chest pain, confusion, muscle pain + cola-colored urine
    (rhabdo), fever at injection site.

11. **Getting help — Filipino resources** (action-oriented, hopeful close)
    - DOH substance-use / mental-health resources, NCMH crisis hotline (1553 / 0966-351-4518),
      DOH Treatment & Rehabilitation Centers (free/subsidized), Dangerous Drugs Board, barangay
      anti-drug help desks, "Yakap" / community reintegration. (Verify exact numbers at build time.)
    - Talk to your nephrologist; recovery + kidney protection go together.
    - **Encouraging message:** stopping at any stage helps the kidneys.

**Patient interactive idea (optional):** a small "Substance → Kidney Risk" reference table /
self-check (not a diagnostic calculator) styled like other guides' info cards.

---

## 5. CLINICIAN TAB — section outline

Clin badges: `KDIGO 2024 Aligned` · `AKI · CKD` · `Tox screen` · `Drug-Induced Nephrotoxicity` ·
`Harm Reduction` · `Dialysis dosing`

Nav pills: **Overview · Screening (SBIRT) · Nephrotoxicity by agent · AKI workup · Rhabdomyolysis · BP/vascular · Infectious (HIV/HBV/HCV) · Dialysis & dosing · Comorbid pain/MH · Referral & MAT · Algorithms · Cases · Evidence**

1. **Clinical overview** — epidemiology, substance use as under-recognized driver of AKI-on-CKD;
   stigma reduces disclosure → standardize screening for all.

2. **Screening & brief intervention** — SBIRT model; validated tools (AUDIT-C, DAST-10, single-item
   screens); non-stigmatizing language; documentation.

3. **Nephrotoxicity by agent** — master reference table (the centerpiece infographic):

   | Agent | Acute renal syndrome | Chronic | Key mechanism |
   |---|---|---|---|
   | Methamphetamine/cocaine | AKI, malignant HTN, rhabdo | accelerated CKD, FSGS | sympathetic surge, vasoconstriction, ischemia |
   | Opioids | overdose ATN, ↑ with rhabdo | — | hypotension/hypoxia |
   | NSAIDs (analgesic abuse) | hemodynamic AKI, AIN | analgesic nephropathy, papillary necrosis | PG inhibition |
   | Tobacco/nicotine | — | progression, proteinuria, vascular | endothelial, sympathetic |
   | Inhalants (toluene) | AKI, distal RTA, hypokalemia | tubular | direct tubular toxicity |
   | Synthetic cannabinoids | AKI (ATN/AIN clusters) | — | direct/idiosyncratic |
   | Anabolic steroids | — | FSGS, proteinuria | glomerular hyperfiltration |
   | Heroin (historical) | — | heroin-associated nephropathy (FSGS) | immune/adulterant |
   | IVDU (any injected) | — | HIVAN, HCV cryoglobulinemic GN, AA amyloid | infection/immune |

4. **AKI workup in suspected substance use** — UA + sediment, CK, urine tox, CMP, urine
   electrolytes, anion/osmolar gaps (toxic alcohols), CK-driven rhabdo protocol.

5. **Rhabdomyolysis management** — fluids, monitoring, when RRT.

6. **BP & vascular emergencies** — stimulant hypertensive crisis (avoid β-blocker monotherapy in
   cocaine; benzodiazepine-first), management of malignant HTN with renal involvement.

7. **Infectious nephropathies** — screen/treat HIV (HIVAN, ART + nephro dosing), HBV/HCV
   (cryoglobulinemic & membranous GN); harm-reduction (clean supplies, vaccination).

8. **Dialysis patients & drug dosing** — dialyzability, dosing adjustments, MAT in ESKD
   (buprenorphine/methadone considerations), access-site infection, adherence.

9. **Comorbid pain & mental health** — opioid-sparing analgesia in CKD (link
   `pain-management-ckd.html`), depression/anxiety (link `ckd-mental-health-sleep.html`).

10. **Referral pathways & MAT** — when to refer to addiction medicine; DOH/DDB rehab pathways;
    integrating MAT with nephrology care.

11. **Algorithms** — (a) suspected drug-induced AKI; (b) stimulant chest pain/HTN crisis;
    (c) screening → brief intervention → referral.

12. **Case snapshots** — e.g. shabu + rhabdo AKI; chronic NSAID papillary necrosis; HCV
    cryoglobulinemic GN in PWID.

13. **Evidence & guidelines** — KDIGO 2024 (AKI/CKD), ASAM 2024, DOH/DDB PH, key nephrology
    literature.

---

## 6. Images / visual assets

Use the `williamriveromd-infographic-skill` to generate prompts. Candidate assets:

1. **Hero (patient):** editorial, hopeful — a person at a window / supportive hands; teal house
   palette. 1024×1024, capped at 600px by `patch_hero_maxwidth.py`.
2. **"6 pathways of kidney injury"** multi-panel pathophysiology infographic.
3. **Nephrotoxicity-by-agent matrix** (clinician) — reference-card style.
4. **Suspected drug-induced AKI algorithm** flowchart (clinician).
5. **"Where to get help in the Philippines"** resource card (patient).

Hero needs `fetchpriority="high" loading="eager"`, full-width `<figure>`, `<img>` capped at
`max-width:600px` centered. Each `<figure>` gets a `<figcaption>` with `<p class="fig-desc">`.
Add og:image tags via `williamriveromd-local-image-generator` once images exist.

---

## 7. Cross-linking — `related_guides.json`

Add the new entry:

```json
"substance-abuse-ckd.html": [
  "alcohol-ckd.html",
  "nsaid-kidney-injury.html",
  "pain-management-ckd.html",
  "ckd-mental-health-sleep.html",
  "herbal-nephropathy.html",
  "managing-hypertension.html"
]
```

Add `substance-abuse-ckd.html` *into the arrays of* the reverse-linked guides so the relationship is
bidirectional: `alcohol-ckd.html`, `nsaid-kidney-injury.html`, `pain-management-ckd.html`,
`ckd-mental-health-sleep.html`, `caffeine-ckd.html`, `muscle-building-supplements-ckd.html`.

---

## 8. Build / patch workflow (after authoring the HTML)

Author the file by copying the dual-mode skeleton from a recent guide (e.g. `alcohol-ckd.html`),
then run, in order (or just run `/setup-guide substance-abuse-ckd.html`):

```bash
python3 patch_master_css.py        --guide substance-abuse-ckd.html
python3 patch_hero_fetchpriority.py --guide substance-abuse-ckd.html
python3 patch_hero_fullwidth.py     --guide substance-abuse-ckd.html
python3 patch_hero_maxwidth.py      --guide substance-abuse-ckd.html
python3 patch_mode_cls.py           --guide substance-abuse-ckd.html
python3 patch_signature_position.py --guide substance-abuse-ckd.html
python3 patch_last_reviewed.py      --guide substance-abuse-ckd.html
python3 generate_sitemap.py
# then edit related_guides.json (section 7) and run the related-guides injector
```

Each script is idempotent and supports `--dry-run`. Commit the guide + `sitemap.xml` +
`related_guides.json` to `main` (per CLAUDE.md normal workflow).

---

## 9. Authoring checklist

- [ ] Dual-mode skeleton copied; `mode-patient` default, navy `mode-physician`.
- [ ] All translatable strings have en/tl/ceb/kap sibling spans.
- [ ] No restore-on-load IIFE; page paints in patient mode.
- [ ] `dr-card-wrap` → `related-guides` → `footer` last, outside `<main>`.
- [ ] Hero patched (fetchpriority/fullwidth/maxwidth).
- [ ] Figures have figcaption + fig-desc; image-lightbox script before `</body>`.
- [ ] `related_guides.json` updated both directions.
- [ ] `sitemap.xml` regenerated.
- [ ] Filipino crisis/rehab hotlines verified current at build time.
- [ ] Tone: stigma-free, harm-reduction, hopeful close.
- [ ] References block: KDIGO 2024 · ASAM 2024 · DOH/DDB PH.

---

## 10. Editorial guardrails

- **Not** a how-to-use-drugs resource; **not** detection-evasion. This is patient education and
  clinical management for kidney protection and recovery.
- Always pair risk info with a help pathway.
- Defer dosing/medical decisions to "talk with your nephrologist."
- Keep alcohol content thin — `alcohol-ckd.html` is the canonical alcohol guide.
