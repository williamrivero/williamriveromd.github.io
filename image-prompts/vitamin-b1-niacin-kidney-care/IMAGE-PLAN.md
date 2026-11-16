# Image Plan Blueprint — Vitamin B1 and Niacin in Kidney Care (v2)

**Guide:** `guides/vitamin-b1-niacin-kidney-care.html` (dual-mode: Patients & Families in EN/TL/CEB/KAP · Clinicians in EN)
**Asset path:** `images/vitamin-b1-niacin-kidney-care-*.{png,webp}` — all 15 figures are already wired into the guide (`<picture>`, alt text, four-language `fig-desc` on patient figures, `fig-abbrevs` where an image carries acronyms).
**Prompt pack:** `PROMPTS-gpt.md` · **Manifest:** `image-manifest.csv` / `image-manifest.json` (Stage 2 schema)
**Prepared:** November 16, 2026 · **Version:** 2.0 (v1 draft expanded: hero redesigned to meet the hero-vignette never-reuse list; five figures added: 09, 10, 11, 12, 13)

**Skills applied**
- `williamriveromd-hero-vignette` v3 — H (Scaffold A, archetype A Editorial Portrait, full human-variation brief)
- `williamriveromd-infographic-skill` v5 — OG (fixed 1200 × 630), 03 red-flag poster, 05 timeline, 07 surrogate-vs-outcome card, 08 flat-lay, 09 radial
- `williamriveromd-biomedical-mechanism-figure` — 02 (organ panel → magnified cell → injury · intervention · benefit)
- `williamriveromd-organ-crosstalk-sigil-graphic` — 10
- `williamriveromd-algorithm-generator-skill` Mode C — 04
- `williamriveromd-simple-figure` — 01 (Scaffold B), 06 (B variant), 11 (C), 12 (E), 13 (D variant)
- `williamriveromd-local-image-generator` (Stage 2) — manifest fields and schema validated (every prompt has IMAGE NUMBER through OG HEIGHT, a named approved font, and the attribution)

---

## 1. The teaching job

This guide is hard to read for four reasons. Each image answers one of them.

| Barrier | Why readers struggle | What the pictures do |
|---|---|---|
| **Invisible chemistry** | "Cofactor," "pyruvate," "lactate" mean nothing to most readers, and B1 deficiency has no visible lesion | One recurring symbol, a **gold key** that unlocks the cell's power plant (01, 02, 09, 10, OG); the analogy is shown next to the real enzyme so it never stands alone |
| **Symptoms that look ordinary** | Belly pain and poor appetite are dismissed; families do not know which signs are emergencies | Risk made personal (09: six recognizable situations) and a two-tier poster: *call* vs *go now* (03) |
| **"Vitamin B3" means three things** | Patients equate food niacin, gram-dose medicine and nicotinamide; clinicians conflate them in reconciliation | Three labeled containers, one caution profile each (06) |
| **Better numbers ≠ better outcomes** | The surrogate trap is the core of the niacin story and is abstract | Lab arrows beside near-equal event bars (07); an effect that fades over time (13); and a concrete alternative path (11) so the message is not only "stop" |

The emotional job matters as much: readers should finish feeling **able to act** — bring the bottle, ask the question, recognize the sign — not frightened. The hero shows a person taking part in his own care, not a sick patient.

## 2. Designing for every educational level

Readers range from people with elementary schooling reading on a phone, often with a family member translating aloud, to nephrologists, pharmacists and dietitians.

| Depth | Who | What they must get | How the image delivers it |
|---|---|---|---|
| **Glance (5 s)** | Everyone | One idea in a headline of ≤8 words | One focal subject; color plus shape carries meaning |
| **Grasp (30 s)** | Patients, caregivers | How the parts connect, and what to do | Arrows in reading order; labels ≤6 words; one consistent metaphor (gold key); a tell-back sentence per image |
| **Go deeper** | Clinicians | Mechanism, decision order, effect sizes | Clinician figures (02, 04, 05, 07, 10, 12, 13) with every on-image acronym defined in the guide's `fig-abbrevs` list |

**Rules every prompt enforces**
1. **One idea per image.** Two headlines means two images.
2. **Pictures before words.** Patient images carry ≤12 words per panel.
3. **The same thing always looks the same** (section 3).
4. **Plain verbs on patient labels** ("call," "go now," "bring"); no acronyms on patient images.
5. **Color plus shape plus word:** red triangle + "GO NOW," amber circle-bar + "CALL"/"CAUTION," green check + "EVERYDAY"/"OK" — meaning survives grayscale and color-vision deficiency.
6. **Phone first:** every label legible at 360 px wide; QC at 50% zoom.
7. **Translation lives in the caption:** images carry short English labels; the guide's four-language `fig-desc` under each patient image does the translating, so nothing is re-rendered per language.
8. **Read-aloud friendly:** every image has a one-sentence **tell-back** (in the prompt pack) that equals its caption.
9. **Filipino context:** monggo, rice, bayong, consult rooms and dialysis units that look local; people varied in age, sex, build and skin tone, calm and dignified.
10. **No blame, no fear:** show an untouched plate, not vomiting; a capped pen, not a needle; a crossed-out bottle, not a scolding.
11. **Numbers only from the guide**, listed in each prompt's Layer A; no doses on any image.

## 3. Shared visual vocabulary

| Element | Always drawn as | Color |
|---|---|---|
| Vitamin B1 (thiamine / TDP) | Small **gold key** or gold dot at the mitochondrial gate | Gold #D4A017 |
| B1 store | Small glass tank or droplet, never large | Gold fill |
| Lactate | Orange droplet with ↑ | Orange #C55A11 |
| Mitochondrion | Bean shape with inner folds | Gray-blue |
| Food niacin | Plate of fish, chicken, peanuts, rice | Green check |
| Nicotinic acid (medicine) | Amber bottle with a small red flush icon | Amber #C9A84C |
| Nicotinamide | Cream bottle with an "i" | Purple #4B3280 |
| Niacin as statin partner | Amber bottle crossed with a gray line | Gray |
| Go now / emergency | Triangle + "GO NOW" | Red #C00000 |
| Call your team / caution | Circle with a bar + "CALL" | Amber |
| Everyday / OK / proven | Check in a circle | Green #2E6B3E |
| Dialysis timing | Tag "PRE-HD" (teal) / "POST-HD" (gray) | Teal / gray |
| Text | Navy only | #1F3864 |

## 4. Story arc — one image per teaching step

| Section | Teaching step | Image |
|---|---|---|
| Hero | "I bring what I take, and I ask" | H |
| `#p-start` | Two vitamins, two different questions | 01 |
| `#p-b1` | Is this me? Who runs low | 09 |
| `#p-b1` | What it looks like; when to go now | 03 |
| `#p-b3` | Three things called B3 | 06 |
| `#p-statin` | If statins bother you: the real options | 11 |
| `#p-visit` | What to bring | 08 |
| `#md-physio` | The gate, the key, the lactate | 02 |
| `#md-physio` | Kidneys and gut fill and drain one small pool | 10 |
| `#md-urgent` | Recognition order | 04 |
| `#md-refeed` | Refeeding against the dialysis clock | 05 |
| `#md-addon` | Lipids moved, events did not | 07 |
| `#md-ckd` | Who with CKD gets LDL-lowering therapy | 12 |
| `#md-phos` | Nicotinamide: an effect that faded | 13 |
| OG / social | Instant recognition in a feed | OG |

Every patient section now has at least one picture, and the urgent message has its own poster.

## 5. Asset register

| ID | File (`images/`) | Size | Archetype | Skill | Anchor | Audience |
|---|---|---|---|---|---|---|
| H | `vitamin-b1-niacin-kidney-care-vignette-hero.png` | 2048 × 2048 | Circular vignette hero v3 | hero-vignette | Patient-tab hero disc (`figure.hero-figure.mode-patient > .hero-vignette`) | Dual (patients first) |
| OG | `vitamin-b1-niacin-kidney-care-og.png` | 1200 × 630 | OG social share card | infographic-skill | `og:image` / `twitter:image`; source for the Latest-guides thumbnail | Dual |
| 01 | `vitamin-b1-niacin-kidney-care-01-two-b-vitamins.png` | 1792 × 1024 | Side-by-side comparison | simple-figure | `#p-start` | Patients (both tabs can reuse) |
| 09 | `vitamin-b1-niacin-kidney-care-09-who-runs-low-on-b1.png` | 1024 × 1024 | Radial risk infographic | infographic-skill | `#p-b1` (after the risk list) | Patients and families |
| 03 | `vitamin-b1-niacin-kidney-care-03-low-b1-warning-signs.png` | 1024 × 1536 | Red-flag poster | infographic-skill | `#p-b1` | Patients and families |
| 06 | `vitamin-b1-niacin-kidney-care-06-three-forms-of-b3.png` | 1792 × 1024 | Three-column comparison | simple-figure | `#p-b3` | Both tabs |
| 11 | `vitamin-b1-niacin-kidney-care-11-if-statins-bother-you.png` | 1792 × 1024 | Step sequence (patient) | simple-figure | `#p-statin` | Patients (clinicians may reuse) |
| 08 | `vitamin-b1-niacin-kidney-care-08-bring-to-your-visit.png` | 1792 × 1024 | Flat-lay checklist | infographic-skill | `#p-visit` | Patients |
| 02 | `vitamin-b1-niacin-kidney-care-02-thiamine-energy-lactate.png` | 1792 × 1024 | Biomedical mechanism figure | biomedical-mechanism-figure | `#md-physio` | Clinicians (patients can read the top row) |
| 10 | `vitamin-b1-niacin-kidney-care-10-thiamine-crosstalk-sigil.png` | 1024 × 1024 | Organ-crosstalk sigil | organ-crosstalk-sigil-graphic | `#md-physio` (after "Why kidney patients are exposed") | Clinicians (shared concept) |
| 04 | `vitamin-b1-niacin-kidney-care-04-thiamine-recognition-algorithm.png` | 1024 × 1536 | Clinical algorithm | algorithm-generator-skill | `#md-urgent` | Clinicians |
| 05 | `vitamin-b1-niacin-kidney-care-05-refeeding-dialysis-timeline.png` | 1792 × 1024 | Timeline | infographic-skill | `#md-refeed` | Clinicians, dietitians, dialysis nurses |
| 07 | `vitamin-b1-niacin-kidney-care-07-lipids-moved-events-did-not.png` | 1792 × 1024 | Surrogate vs outcome infographic | infographic-skill | `#md-addon` | Clinicians |
| 12 | `vitamin-b1-niacin-kidney-care-12-ckd-ldl-eligibility-map.png` | 1536 × 1152 | Clinician reference card | simple-figure | `#md-ckd` | Clinicians |
| 13 | `vitamin-b1-niacin-kidney-care-13-nicotinamide-phosphate-fade.png` | 1792 × 1024 | Single data figure | simple-figure | `#md-phos` | Clinicians |

**Totals:** 15 images — 2 hero/social (H, OG), 6 patient (01, 09, 03, 06, 11, 08), 7 clinician (02, 10, 04, 05, 07, 12, 13).

## 6. Production order

H → OG → 03 → 01 → 09 → 06 → 11 → 08 → 02 → 04 → 05 → 07 → 10 → 12 → 13 — hero and share card first (they appear everywhere), then the patient safety poster, then the images most readers will see, then clinician figures.

## 7. QC rubric (every render, before it ships)

| Check | Pass standard |
|---|---|
| **5-second test** | A non-medical adult can state the single message |
| **Tell-back test** (patient images) | The reader can say the image's tell-back sentence in their own words |
| **Exact words** | Every label matches Layer B; regenerate rather than edit pixels |
| **Numbers** | Only those in Layer A; bars and intervals drawn to scale (07, 13) |
| **Science** | 02: PDH open (sufficient) vs closed (deficient), lactate only on the deficient side; 04: red-flag decision first, differential in parallel; 05: PRE/POST-HD tags only on dialysis days; 12: dialysis row splits "start" from "continue"; 13: week-52 interval crosses zero |
| **People** | Filipino, varied, calm, dignified; no needles in skin, no vomiting, no shame cues; hero not a person eating or a couple at a table |
| **Clinician images** | Every on-image abbreviation is in the figure's `fig-abbrevs` list (02: ATP, TDP, PDH, α-KGDH, LDH, NADH · 04: TDP, IV, WE, PD · 05: HD, PO₄, K, Mg · 07: HDL-C, TG · 10: B1 · 12: CKD, LDL, eGFR, ASCVD, KDIGO, ACC/AHA, PREVENT · 13: none beyond text) |
| **House style** | Light background, Inter/Manrope, attribution present and exact, no flat-vector look |
| **Files** | `.png` master + same-size `.webp` twin; OG exactly 1200 × 630 |

## 8. After images arrive (Stage 2)
1. Drop files into `images/`; run `python3 patch_hero_fetchpriority.py --guide vitamin-b1-niacin-kidney-care.html` and `patch_image_lightbox.py`.
2. Generate the related-guide thumb from the OG card as for other guides.
3. Update `image-manifest.csv` status from `pending` to `delivered`.
4. Clinical sign-off on 02, 04, 05, 12 and 13 rests with the guide author.
