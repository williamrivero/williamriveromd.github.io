# PhilHealth Claims track — Part 6 (HMO claims and collections) image prompt pack

Added November 26, 2026 for Modules 12–14. Same visual system as images 013–033 of the track
(illustrated vignette, bright natural light, Filipino staff and families, dialysis unit, warm palette
anchored on the site colors NAVY #1F3864, TEAL #1A6B72, ORANGE #C55A11, GREEN #2E6B3E, RED #C00000,
PURPLE #4B3280). Illustrated, GPT-rendered — not flat vector. Every HMO name, card, and document is
fictional: no real HMO logos, brand colors, or wordmarks. No legible text in heroes and cards; figures
may carry short labels (American English, spelled exactly as given).

Save PNGs under the exact filenames into `images/`, run `python3 tools/techcourses/prep_assets.py`,
then `python3 generate_tech_courses.py --course philhealth_claims --patch`.

## Heroes (1536 × 1024, text-free, left 40% quiet)

**H12 · `philhealth-claims-12-hmo-accreditation-vignette-hero.png`**
Illustrated vignette, bright natural light, a Filipino claims officer in her thirties pinning four
color-coded payer folders (teal, orange, green, purple, each with a plain unbranded card icon) to a
corkboard beside a thick signed contract with a ribbon bookmark. Through a glass window behind her, a
nurse tends a patient in a dialysis chair. Calm, orderly mood. No text, no logos.

**H13 · `philhealth-claims-13-hmo-loa-and-claims-vignette-hero.png`**
Illustrated vignette at a dialysis intake desk: a young Filipino clerk reads an approval code on a
laptop (screen shown as abstract blocks, no readable text) while a woman in her late fifties waits
with a plain health card and an ID. Behind them a nurse prepares a dialysis chair. A desk calendar
shows one day softly highlighted in amber. No text, no logos.

**H14 · `philhealth-claims-14-hmo-collections-vignette-hero.png`**
Illustrated vignette in a small finance office: a Filipino claims officer and a finance officer review
a large wall screen of horizontal bars in three colors, one bar much longer than the others, with a
neat stack of letters and a stamped receipt on the desk. A window shows the dialysis floor in soft
focus. Serious but steady mood. No text, no logos.

## Module cards (1280 × 720, text-free; saved as `.png`, prep_assets makes the `.webp`)

- `philhealth-claims-12-card.png` — four unbranded payer folders fanned on a desk beside a contract and a pen.
- `philhealth-claims-13-card.png` — a single approval slip with a highlighted date field beside a health card (blank) and an ID (blank).
- `philhealth-claims-14-card.png` — horizontal aging bars on a tablet beside a stack of dated letters.

## Figures (1536 × 1024 or 1024 × 1024; short labels allowed)

**F12a · `philhealth-claims-12-many-payers-one-desk.png`** (key `pc_hmo_payers`)
A claims desk at the center with four color-coded payer folders around it; each folder has its own
small clock, form, and rule card. Labels: "Payer A", "Payer B", "Payer C", "Payer D", "Claims desk".
Behind the desk, a patient in a dialysis chair with a nurse, labeled "Treatment continues".

**F12b · `philhealth-claims-12-payer-profile.png`** (key `pc_hmo_profile`)
A one-page card titled "Payer profile" with eight rows, each joined by a thin thread to a clause in a
signed contract: "Services and rates", "Approvals (LOA)", "PhilHealth first", "Filing period",
"Payment term", "Professional fees", "Appeals", "Termination". A small "Checked: date / name" box.

**F13a · `philhealth-claims-13-reading-the-loa.png`** (key `pc_hmo_loa`)
A magnified letter of authorization with five highlighted fields: "Member", "Service",
"Valid dates", "Approved amount", "Approval code". A calendar strip shows "Fri: last valid day" and
"Mon: next session" in amber, with a small dialysis chair icon labeled "Session goes ahead".

**F13b · `philhealth-claims-13-claim-batch.png`** (key `pc_hmo_batch`)
A stack of claims under a sheet labeled "Transmittal" with "Control total" at the bottom. Each claim
shows an LOA code, an itemized statement with three colored lines labeled "PhilHealth", "HMO",
"Patient", and a signed form. At the end, a stamp labeled "Proof of receipt".

**F14 · `philhealth-claims-14-aging-by-payer.png`** (key `pc_hmo_aging`)
Horizontal aging bars for "Payer A", "Payer B", "Payer C" across buckets "0–30", "31–60", "61–90",
"Over 90", each bar with a vertical marker labeled "Term". Payer C's bar runs far past its marker. To
the right, a five-step ladder: "Statement", "Reminder", "Provider relations", "Demand letter",
"Insurance Commission".

## QA before placement
- No real HMO names, logos, or brand colors; no readable patient data.
- Labels spelled exactly as above; American English.
- Illustrated (not flat vector) style matching images 013–033.
- Attribution per site convention for the public set.
