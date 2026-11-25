# -*- coding: utf-8 -*-
"""Compile RTC-IMAGE-PROMPTS.md for the Renal Transplant Coordinator track (renalcarematters.com house style).
Skills applied: williamriveromd-hero-vignette (v3 circular heroes), williamriveromd-simple-figure (teaching figures),
williamriveromd-infographic-skill (tiles, OG / share cards). Run: python3 build_prompts.py <out.md>"""
import sys

HUB = "transplant-coordinator"
SLUGS = ["role-and-navigation", "philippine-governance", "referral-and-access", "recipient-workup", "compatibility-and-specimens",
         "donor-intake-and-protection", "donor-medical-evaluation", "legal-documents-and-consent", "ethics-and-safeguarding",
         "insurance-and-authorization", "claims-and-financial-protection", "waiting-list-and-deceased-donation", "offers-and-logistics",
         "readiness-and-handoff", "medicines-and-discharge", "urgent-triage-and-escalation", "longitudinal-navigation",
         "psychosocial-and-special-situations", "data-privacy-and-quality", "capstone-and-international-comparison"]
TITLES = ["The Coordinator as Navigator for Two People", "Philippine Regulation and Professional Scope", "Referral, Intake, and Equitable Access",
          "Recipient Workup and Multidisciplinary Decisions", "Compatibility and Safe Specimen Coordination", "Living Donor Intake and Protection",
          "Donor Medical Evaluation and Long-Term Risk", "Legal Documents and Informed Consent", "Ethics Committee Navigation and Safeguarding",
          "PhilHealth and Other Payers", "Claims Evidence, Denials, and Financial Protection", "The Waiting List and Deceased Donation",
          "Organ Offer Calls and Retrieval Logistics", "Final Readiness and Perioperative Handoff", "Medicines, Discharge, and Self-Management",
          "Symptoms, Graft Dysfunction, and Urgent Escalation", "Lifelong Follow-Up for Donor and Recipient", "Psychosocial Navigation and Special Situations",
          "Registries, Privacy, and Quality", "Integrated Capstone and International Practice"]

FONT = "Inter"
ATTR = "renalcarematters.com"
NEG_HERO = ("busy layouts; collage overload; more than four supporting scenes; dozens of icons; tiny unreadable labels; infographic clutter; "
            "duplicated people; repeated compositions; cropped circle; cropped objects; edge clipping; objects touching the circular border; "
            "important content inside the title safe zone; baked-in text, titles, captions, logos, watermarks; readable names, numbers, or "
            "identifiers on documents, screens, wristbands, or badges; rectangular borders, frames, banners; dark, charcoal, or black "
            "backgrounds; cartoon style, neon, HDR, over-saturation; distorted hands or faces; implausible anatomy or equipment; any "
            "suggestion of organ sale, money changing hands, pressure on a donor, or a guaranteed surgery.")
NEG_FIG = ("Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid misspelled words, avoid unrealistic "
           "anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds; light "
           "backgrounds only. Use ONLY the sans-serif font Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans); no serif, decorative, "
           "or handwritten typefaces. No real names, no legible personal identifiers, no logos of real agencies. Never omit the "
           "renalcarematters.com attribution. Spell every label exactly as written in quotation marks, in American English.")

# ── course + module heroes: (archetype, camera, scaffold, subject, supporting, safe zone, variation) ──
HEROES = [
    ("course", "H Clinical", "environmental portrait, eye level, slightly wide", "A",
     "a Filipina transplant coordinator in her early 40s (short layered black hair with a few gray strands, round face, rimless glasses, "
     "deep-teal scrub top under an open white cardigan, lanyard turned so no text shows) walking calmly along a bright hospital corridor between "
     "two open consultation-room doors; through the left door a seated adult kidney recipient (man in his 50s, gray polo) talks with a "
     "nephrologist; through the right door a seated adult living donor (woman in her 30s, mustard blouse) talks with a different clinician",
     "two separate rooms clearly apart, a potted plant, soft daylight from tall windows", "upper-left third: soft blurred corridor wall and window light",
     "course hero: clinician-led, two parallel rooms, corridor depth"),
    ("01", "J Environmental Storytelling", "over-the-shoulder from behind the coordinator", "A",
     "a male Filipino coordinator in his late 20s (buzz-cut hair, lean build, navy polo, wristwatch) standing at a large whiteboard drawing two "
     "separate colored pathway lines (one teal, one violet) with four simple gate symbols on each, while a seated woman in her 40s (shoulder-length "
     "wavy hair, coral blouse) watches attentively; the marks on the board are abstract shapes and arrows only, no readable words",
     "a coffee mug, a closed folder, a window with greenery", "upper-right: plain wall and soft light", "young male clinician, standing, rear view"),
    ("02", "I Object Hero", "top-down overhead", "B",
     "a neat stack of printed issuance documents fanned on a light oak desk, each with a different colored date tab and an empty calendar icon "
     "stamp, beside a pair of reading glasses and a fountain pen; all document text is blurred and unreadable",
     "a small Philippine flag desk pin, a cup of coffee, a sticky note with no writing", "top third: empty desk surface with soft gradient", "no people"),
    ("03", "E Lifestyle", "side profile, medium distance", "A",
     "an elderly Filipino man in his 70s (thin white hair, mustache, slim, short-sleeved checkered shirt) seated in a dialysis chair beside a "
     "machine (screen blank) while his wife (60s, bun hairstyle, floral duster) leans in, and a female coordinator in her 30s (ponytail, light-blue "
     "scrubs) kneels at eye level holding a simple illustrated leaflet with no readable text",
     "a window with morning light, a folded blanket", "upper-left: soft window glow", "elderly couple, kneeling clinician"),
    ("04", "H Clinical", "wide-angle from the table end", "A",
     "a multidisciplinary case conference: five clinicians of varied ages and genders (a female surgeon in a surgical cap, an older male "
     "cardiologist with gray beard, a young female social worker in a cardigan, a male nephrologist in his 40s, a female coordinator in teal "
     "scrubs presenting) around a light table with a wall screen showing an abstract chart with no text",
     "laptops, water glasses, natural daylight", "upper third: blurred screen glow and wall", "group scene, clinicians only"),
    ("05", "I Object Hero", "macro, shallow depth of field", "B",
     "a gloved hand holding a sealed blood specimen tube with a blank white label beside an open insulated transport box containing three more "
     "tubes in a rack and a small temperature indicator",
     "a request form with blurred unreadable lines, a pen", "upper-right: soft light-teal gradient", "hands-only"),
    ("06", "H Clinical", "close environmental portrait, three-quarter", "A",
     "a private consultation: a Filipino man in his mid-30s (curly short hair, stubble, broad shoulders, olive work jacket, silver ring) seated "
     "with hands clasped, listening, opposite a female coordinator in her 50s (cropped gray hair, burgundy blouse) who sits with an open "
     "posture; the door behind is closed",
     "a box of tissues, a glass of water, a small plant", "upper-left: plain warm wall", "younger male potential donor, older female coordinator"),
    ("07", "F Anatomy", "three-quarter view", "C",
     "a single healthy human kidney rendered semi-photoreal beside a faint outline of an empty space where a second kidney was, with a calm "
     "soft glow suggesting the remaining kidney adapting",
     "a subtle blood-pressure cuff silhouette and a urine cup silhouette in the background, very soft", "upper-right: empty soft background", "no people, anatomy"),
    ("08", "I Object Hero", "overhead at a slight angle", "B",
     "a tidy document packet fanned on a desk (civil registry certificates, an affidavit, a consent form) with all text blurred, a checklist "
     "card on top with checkmarks only, and a document scanner edge in the corner",
     "a notary-style embossed seal (no words), a ballpoint pen", "lower-left: empty desk surface", "no people"),
    ("09", "D Panorama", "wide, slightly elevated", "A",
     "a calm hospital meeting room with an oval table where six ethics committee members of mixed ages and genders sit in discussion, one "
     "elderly woman in a barong-inspired blouse chairing, a sealed case folder on the table",
     "tall windows with city view, water pitcher", "upper third: bright window light", "committee, wide shot"),
    ("10", "H Clinical", "over-the-shoulder from the patient side", "A",
     "a hospital billing counter where a Z Benefits coordinator (Filipina in her 30s, long straight hair, glasses, navy blazer) explains a printed "
     "cost plan (numbers blurred) to a man in his 40s (jeepney operator look: cap in hand, faded red shirt, tanned forearms) and his sister "
     "(40s, short bob, green blouse)",
     "a calculator, a queue number display with no digits visible", "upper-left: soft blurred wall", "siblings, over-the-shoulder"),
    ("11", "I Object Hero", "top-down", "B",
     "an open claim folder on a desk with a desk calendar showing a shaded 60-day span (no readable dates) and a checklist with ticks, a stamp pad, "
     "and two hands of a claims officer sorting pages",
     "a laptop edge, a highlighter", "upper-right: empty light surface", "hands-only, office"),
    ("12", "E Lifestyle", "environmental portrait, medium", "A",
     "a young woman in her late 20s (pixie haircut, small nose stud, denim jacket over a white tee) on a phone call on a balcony of a Cebu apartment "
     "with the sea in the distance, a small dialysis appointment card in her hand (no text)",
     "potted herbs, morning light", "upper-left: open sky", "young female patient, outdoor"),
    ("13", "H Clinical", "side profile, night", "A",
     "a male coordinator in his 40s (receding hairline, rectangular glasses, maroon scrubs) at a nurses' station at night on a desk phone, writing "
     "on a structured form with empty boxes, a wall clock with no readable numbers, bright but warm station lighting",
     "a mug, a corridor with soft night lighting (still light-toned, not dark)", "upper-right: soft lit wall", "night scene, single male clinician"),
    ("14", "G Infographic", "slightly elevated wide", "A",
     "a pre-operative huddle: a surgeon in scrubs and cap, an anesthesiologist, a scrub nurse, and a coordinator stand around a readiness board "
     "showing two rows of four round lights (seven green, one amber) with no text",
     "an operating room door with frosted glass, a gurney edge", "upper-left: frosted glass glow", "team standing, theater setting"),
    ("15", "A Editorial Portrait", "close portrait, eye level", "A",
     "a Filipino man in his early 40s (teacher look: neat side-part hair, thin mustache, white short-sleeved polo) holding a weekly pill organizer "
     "with colored compartments, explaining it back to a coordinator (only her hands and sleeve visible) while his wife in the background smiles",
     "colored stickers on two medicine boxes (no text), a glass of water", "upper-right: soft home-clinic wall", "teach-back moment, male recipient"),
    ("16", "H Clinical", "over-the-shoulder", "A",
     "a coordinator (Filipina in her 50s, silver bob, reading glasses on a chain, lavender scrubs) at a clinic desk on the phone, one hand on a "
     "structured urgent-call log (empty boxes), with a protocol card pinned beside her",
     "a window with daylight, a desk lamp", "upper-left: blurred window", "older female clinician, phone"),
    ("17", "E Lifestyle", "environmental portrait, eye level", "A",
     "a healthy man in his 50s (security-guard look: short gray crew cut, sturdy build, light-blue uniform shirt without insignia) greeted at a "
     "clinic reception by a smiling young male coordinator (20s, curly hair, teal scrubs), morning light",
     "a blood-pressure machine in the background, a potted plant", "upper-right: bright wall", "donor years later, male-male greeting"),
    ("18", "A Editorial Portrait", "close environmental portrait", "A",
     "a family room: a young man in his 30s (shaved head, tattoo sleeve partly visible, gray hoodie) on a video call on a tablet with a relative "
     "abroad (face blurred), a female social worker (40s, hijab in soft blue) seated beside him listening",
     "a box of tissues, a window with rain on the glass but bright light", "upper-left: soft window", "OFW video call, hijab social worker"),
    ("19", "I Object Hero", "three-quarter view", "B",
     "a monitor on a clean desk showing an abstract run chart with a falling line and a dotted median (no numbers or text), a padlock-shaped "
     "privacy icon on a sticky tab, and a locked drawer",
     "a plant, a coffee cup", "upper-right: soft gradient", "no people, data and privacy"),
    ("20", "B Journey", "high, slightly overhead", "A",
     "a training room where a coordinator (Filipino man in his 30s, man-bun hairstyle, maroon long-sleeve shirt) points at a long wall-mounted "
     "journey map with two parallel lanes and colored gate symbols (no text) while three colleagues of mixed ages watch",
     "a projector glow, notebooks", "upper-left: plain wall above the map", "teaching scene, journey map"),
]

# ── teaching figures (simple-figure scaffolds) ──
FIGURES = [
    ("rtc00_two_paths", "00-two-paths-four-gates", "Scaffold C — Horizontal step sequence (two parallel lanes)", "1792 × 1024", "16:9", "home and Module 1",
     "Title at top: \"Two People, Four Gates Each\". Two parallel horizontal lanes. Top lane in clinical teal (#1a6b72) labeled \"Recipient\"; bottom lane in soft purple (#6c3d8e) labeled \"Living donor\". Each lane passes through four rounded gate cards in order: \"Medical\", \"Legal\", \"Ethical\", \"Insurance\" (same order in both lanes, each gate card with a simple icon: stethoscope, document, balance scale, peso coin). The lanes converge only at a single navy card on the right labeled \"Readiness huddle\", then split again into two arrows labeled \"Recipient care for life\" and \"Donor care for life\". A small padlock icon between the lanes with the label \"Separate records\". Bottom strip: \"The paths meet at the operation. Records, rights, and choices stay separate.\""),
    ("rtc01_register", "01-barrier-register", "Scaffold E — Reference table", "1536 × 1152", "4:3", "Module 1",
     "Title: \"The Barrier Register\". A clean table with column headers in teal on soft gray: \"Person\", \"System\", \"Barrier\", \"Owner\", \"Next action\", \"Due\", \"Status\", \"Closure evidence\". Three example rows using fictional pseudonyms: Row 1 \"Recipient R-07 | Medical | Cardiology review | Dr. Cardio | Confirm appointment | Mar 27 | Closed | Visit note received\" (status cell green); Row 2 \"Donor D-07 | Ethical | Advocate meeting | Donor advocate | Private meeting | Today | Open\" (status amber); Row 3 \"Recipient R-07 | Insurance | Pre-authorization expiry | Z Benefits lead | Check validity | Aug 28 | Overdue\" (status red). A callout arrow to the last column: \"A row closes on evidence, never on a sent message.\""),
    ("rtc02_rulebooks", "02-who-issues-what", "Scaffold C — Radial reference card", "1792 × 1024", "16:9", "Module 2",
     "Title: \"Who Issues What\". Center: a desk icon labeled \"Your program\". Five surrounding rounded cards connected by thin navy lines: \"Congress — laws (RA 7170, RA 10364, RA 10173)\"; \"DOH — facility and donor safeguards (AO 2021-0059)\"; \"PhilHealth — Z Benefits rules (PC 2024-0035, PC 2026-0019)\"; \"Hospital — role charter and procedures\"; \"Professional bodies — guidance (KDIGO, PSN)\". Each card shows a small calendar icon. Bottom strip: \"Before acting: issuer, scope, effective date.\""),
    ("rtc03_steps", "03-steps-to-transplant", "Scaffold C — Staircase sequence", "1792 × 1024", "16:9", "Module 3",
     "Title: \"Eight Steps to a Transplant\". A clean ascending staircase of eight labeled steps from left to right: \"Medically suitable\", \"Interested\", \"Referred\", \"First visit\", \"Workup done\", \"Accepted\", \"Listed or donor found\", \"Transplant\". Small simple human figures standing on different steps; one is helped up a step by a coordinator figure in teal. Caption strip: \"In a randomized trial, navigated patients completed 3.5 steps vs 1.6 with usual care.\""),
    ("rtc04_questions", "04-workup-by-question", "Scaffold D — One-panel radial diagram", "1792 × 1024", "16:9", "Module 4",
     "Title: \"Organize the Workup by Question\". Center: a simple neutral person silhouette labeled \"Candidate\". Six question bubbles around it, each with an owner tag: \"Is the heart safe for surgery? — Cardiology\"; \"Any infection to treat first? — Infectious diseases\"; \"Any cancer to find first? — Transplant team\"; \"Can the medicines be taken every day? — Psychosocial review\"; \"Is there support at home? — Social work\"; \"Are vessels and bladder suitable? — Surgery\". Bottom strip: \"A normal test answers nothing until its owner reviews it.\""),
    ("rtc05_specimen", "05-specimen-chain", "Scaffold C — Horizontal step sequence", "1792 × 1024", "16:9", "Module 5",
     "Title: \"The Specimen Chain\". Six linked chain-link cards left to right: \"Request checked\", \"Labeled at bedside: 2 identifiers\", \"Packed as the lab instructs\", \"Courier log signed\", \"Lab receipt confirmed\", \"Result to the team\". Below the third link, a separate red broken link labeled \"Unlabeled tube = re-collect\". Small icons: form, tube, cooler box, clipboard, lab stamp, physician. Bottom strip: \"A sample is only as trustworthy as its weakest handoff.\""),
    ("rtc06_private", "06-private-door", "Scaffold B — Side-by-side comparison", "1792 × 1024", "16:9", "Module 6",
     "Title: \"The Private Door\". Left panel (renal green header \"Private intake\"): a closed door icon and two seated figures (donor and coordinator) with a speech bubble \"You may stop at any time.\" Right panel (red header \"Not a private intake\"): the same room with family members crowding in and answering for the donor, crossed out with a thin red X. Footer: \"The donor speaks for themself, in private, with a safe way to say no.\""),
    ("rtc07_risk", "07-donor-risk-in-numbers", "Scaffold B — Icon-array comparison", "1792 × 1024", "16:9", "Module 7",
     "Title: \"Donor Risk in Absolute Numbers\". Two icon arrays of small person icons, each representing 10,000 people (draw as a dense grid of tiny figures). Left array labeled \"Matched healthy nondonors\": about 4 icons highlighted in amber with label \"≈4 per 10,000 kidney failure in 15 years\". Right array labeled \"Living donors\": about 31 icons highlighted in amber, label \"≈31 per 10,000 kidney failure in 15 years\". A separate small strip: \"Surgical death within 90 days: ≈3 per 10,000 donors\". Bottom note: \"Large U.S. cohorts. Small, real, and different for each donor. Give relative and absolute risk together.\""),
    ("rtc08_packet", "08-legal-packet", "Scaffold E — Reference card", "1536 × 1152", "4:3", "Module 8",
     "Title: \"A Traceable Legal Packet\". A manifest table with headers: \"Document\", \"Proves\", \"Verified at\", \"By\", \"Date\". Rows: \"ID\" | \"Identity and age\"; \"PSA birth and marriage certificates\" | \"Relationship\"; \"Affidavit\" | \"Emotional ties\"; \"Deed of donation\" | \"Donor's intention\"; \"Consent record\" | \"Informed, voluntary choice\". Leave the Verified, By, Date cells with simple checkmarks and blank lines (no names). Footer: \"Trusted because it can be traced, not because it looks official.\""),
    ("rtc09_ethics", "09-support-not-persuasion", "Scaffold B — Side-by-side comparison", "1792 × 1024", "16:9", "Module 9",
     "Title: \"Support, Not Persuasion\". Left panel (green header \"Support\"): a coordinator icon offering a balanced scale and a clock, with short phrases \"Take your time\", \"Here are the risks, with numbers\", \"Your advocate is just for you\". Right panel (red header \"Pressure and reward\"): a hand pushing an envelope with a peso symbol and a speech bubble \"Everyone is counting on you\", crossed out. Footer: \"Pressure and reward are red flags to record and route, never to investigate alone.\""),
    ("rtc10_approvals", "10-three-approvals", "Scaffold C — Three-card sequence", "1792 × 1024", "16:9", "Module 10",
     "Title: \"Three Approvals, Three Owners\". Three large cards side by side, each with a stamp icon: \"Clinical clearance — transplant team\"; \"Ethics approval — HTEC\"; \"Pre-authorization — PhilHealth\", the last with a small clock labeled \"Valid 180 days\". A fourth smaller card: \"Consent — the person, with the surgeon\". Footer: \"A payment approval is never a clinical or ethical clearance.\""),
    ("rtc11_window", "11-claim-window", "Scaffold C — Timeline", "1792 × 1024", "16:9", "Module 11",
     "Title: \"The 60-Day Filing Window\". A horizontal timeline starting at \"Discharge (Day 0)\" with a shaded band to \"Day 60: filing deadline\"; weekly tick marks with a small checklist icon labeled \"Weekly packet check\". A claim folder passes through a gate labeled \"Complete? Registry? Mandatory services? Consistent data?\" then splits into two branches: amber \"Return — correct and resubmit\" and red \"Denial — reason and appeal route\". A side note: \"PhilHealth processes complete claims within 30 working days.\""),
    ("rtc12_databases", "12-three-lists", "Scaffold E — Three-column reference", "1792 × 1024", "16:9", "Module 12",
     "Title: \"Three Lists, Three Purposes\". Three filing-cabinet icons with cards beneath: \"National waiting list — DOH program — deceased-donor organs\"; \"PhilHealth KT Data Registry — required for pre-authorized patients from May 1, 2026\"; \"Hospital transplant list — local tracking\". Dotted lines link the three through a small checklist labeled \"Reconcile on a schedule\". Footer: \"Being on one list does not mean being on the others.\""),
    ("rtc13_offer", "13-offer-call-readback", "Scaffold A — Short flow", "1024 × 1536", "2:3 portrait", "Module 13",
     "Title: \"Read It Back\". Vertical flow of nodes: \"Caller and callback number\" → \"Candidate: 2 identifiers (read back)\" → \"Donor blood group (read back)\" → \"Times and storage (read back)\" → decision diamond \"Any discrepancy?\" with a red branch to a stop-sign node \"Stop. Escalate to transplant physician now.\" and a green branch to \"Decision maker decides acceptance\" → \"Log times as they happen\"."),
    ("rtc14_convergence", "14-readiness-convergence", "Scaffold E — Status board", "1792 × 1024", "16:9", "Module 14",
     "Title: \"Readiness Is a Convergence\". A clean board with two rows labeled \"Recipient\" and \"Donor\" and four columns \"Medical\", \"Legal\", \"Ethical\", \"Insurance\": seven round green lights and one amber light (Donor / Ethical) labeled \"Condition pending\". To the right, a surgeon icon with a raised palm and the label \"Hold until every gate closes\". Footer: \"Eight gates, closed by their owners, on current evidence.\""),
    ("rtc15_runway", "15-medicine-runway", "Scaffold C — Timeline", "1792 × 1024", "16:9", "Module 15",
     "Title: \"The Medicine Runway\". A runway drawn as a 10-day calendar strip with tablet icons decreasing each day (40 tablets, 4 per day). A blue marker before day 5 labeled \"Start refill (5 working days lead time)\"; the end of the runway labeled \"Run-out\". A small airplane labeled \"Refill\" lands before the end. Formula card: \"Days of supply = tablets on hand ÷ tablets per day\". Footer: \"Never stretch, skip, or switch brands. Supply problems go to the team.\""),
    ("rtc16_routing", "16-urgent-routing", "Scaffold A — Routing flow", "1024 × 1536", "2:3 portrait", "Module 16",
     "Title: \"Route by Protocol\". Top node: phone icon \"Urgent call: name, 2 identifiers, symptom, onset, callback\". Three branches: red \"Emergency now — breathing trouble, chest pain, confusion, no urine\"; amber \"Transplant clinician today — fever, less urine, graft pain, vomiting tablets, missed dose\"; green \"Routine — appointments, paperwork\". A loop arrow at the bottom: \"Close the loop: received, acted, understood, documented\". Small separate side box: \"Donor calls go to the donor's own team\"."),
    ("rtc17_two_plans", "17-two-care-plans", "Scaffold C — Two parallel timelines", "1792 × 1024", "16:9", "Module 17",
     "Title: \"Two Care Plans for Life\". Two parallel horizontal timelines extending to the right edge with arrowheads. Top (teal) \"Recipient\": icons for medicines, labs, vaccines, cancer screening, heart check at regular marks. Bottom (purple) \"Donor\": marks at \"6 months\", \"1 year\", \"2 years\", then \"every year\", each with icons for blood pressure, weight, kidney function, urine albumin. Footer: \"Recall the donor privately, never through the recipient.\""),
    ("rtc18_barriers", "18-making-barriers-speakable", "Scaffold D — One-panel scene diagram", "1792 × 1024", "16:9", "Module 18",
     "Title: \"Make Barriers Speakable\". A simple flat illustration of a family at a small table with a coordinator, surrounded by six soft speech-bubble icons labeled \"Money\", \"Work leave\", \"Travel\", \"Childcare\", \"Mood and fear\", \"Family abroad\". Arrows from each bubble to three routing cards on the right: \"Social worker\", \"Psychologist or psychiatrist\", \"Transplant clinician (same day if medicines changed)\". Footer: \"Thank, then route.\""),
    ("rtc19_quality", "19-quality-loop", "Circular loop diagram", "1024 × 1024", "1:1", "Module 19",
     "Title: \"Define Before You Count\". A circular loop with five nodes: \"Define (numerator, denominator, window)\", \"Measure\", \"Compare by group\", \"Change one thing\", \"Re-measure\". Center card: a small run chart with a falling line labeled \"Days from referral to first visit\" and a note \"15 of 20 = 75%, and so is 45 of 60 — the larger sample is more certain\"."),
    ("rtc20_journey", "20-whole-journey", "Scaffold C — Long journey map", "1792 × 1024", "16:9", "Module 20",
     "Title: \"The Whole Journey\". A long horizontal map with two lanes (teal \"Recipient\", purple \"Donor\") from \"Referral\" to \"Lifelong follow-up\", with numbered circular markers 1 to 20 placed along the route in order, and the four gate symbols (stethoscope, document, scale, peso coin) recurring along both lanes. A small legend: \"Safety first, deadlines second, everything else in the register.\""),
]

TILE_SCENES = {
    "course": "a calm coordinator walking between two separate consultation rooms, one with a recipient and one with a donor",
}


def hero_block(i, h):
    key, arch, cam, scaf, subject, support, safe, var = h
    slug = HUB if key == "course" else f"{HUB}-{key}-{SLUGS[int(key) - 1]}"
    title = "Course home" if key == "course" else f"Module {int(key)}: {TITLES[int(key) - 1]}"
    sc = {"A": "Scaffold A — people scene", "B": "Scaffold B — still-life / object", "C": "Scaffold C — calm 3D anatomy"}[scaf]
    kind = {"A": "photorealistic editorial photograph", "B": "photorealistic still-life", "C": "semi-photorealistic 3D medical illustration"}[scaf]
    return f"""### RTC-H{('00' if key == 'course' else key)} · {title}

```
FILE NAME: {slug}-vignette-hero.png  (also export {slug}-vignette-hero.webp)
IMAGE TYPE: Circular vignette hero v3 — {sc}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION: {var}; cast differs from every other hero in this track in age, sex, hair, face shape, clothing color, posture, and setting
AUDIENCE: transplant coordinators and coordination-support staff
PLACEMENT: hero disc of academy/{slug}.html; also the module page's og:image source

PROMPT:
Square 1:1 {kind} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
Subject: {subject}, in a clean, bright, modern Philippine transplant-center setting with soft natural daylight and gentle shallow depth of field.
Supporting elements (2–4 only): {support}.
Visual hierarchy: hero subject 60–70% of the circle; supporting context 20–30%; reserve a 20–25% TITLE SAFE ZONE ({safe}) with no faces, anatomy, icons, objects, or callouts inside it.
Calm, respectful, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on light tones; the scene conveys two separate, equally respected people and careful coordination. Soft edge falloff toward a slightly deeper neutral at the rim. No rectangular frames or banners.
Absolutely NO text of any kind: no title, caption, label, logo, readable document, screen text, badge, or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; nothing readable anywhere; no hint of payment, pressure, or a guaranteed operation.
```
"""


def fig_block(f):
    key, stem, scaf, dims, ratio, where, content = f
    return f"""### RTC-F{stem[:2]} · {stem[3:].replace('-', ' ').capitalize()}  (figure key `{key}`)

```
FILE NAME: {HUB}-{stem}.png  (export {HUB}-{stem}.webp for the page)
IMAGE TYPE: {scaf}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {dims}
AUDIENCE: transplant coordinators and coordination-support staff (mixed clinical and nonclinical)
PLACEMENT: {where} — teaching figure slot {{{{fig:{key}}}}} (tools/techcourses/rtc/figs.py)
VISUAL GOAL: turn the lesson's rule into a picture a learner can recall at the bedside.

PROMPT:
Clean clinical education figure in the renalcarematters.com house style. White (#ffffff) background with soft gray (#f3f4f6) and light teal (#eef6f7) card fills. Bold navy (#0f1e2e) title at top in {FONT}; all labels in {FONT}, mobile-readable (minimum 11 pt equivalent), short phrases only. Palette: clinical teal #1a6b72 (recipient, headings), soft purple #6c3d8e (donor), renal green #1f7a4d (safe / closed), amber #b8860b (pending / caution), clinical red #b91c1c (stop / danger). Rounded cards, thin navy connector lines, generous whitespace, no clutter.
{content}
Bottom-right corner: "{ATTR}" in small semi-transparent navy text (about 10–11 px, 70% opacity).

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Every label spelled exactly as quoted; light background only; readable on a phone; recipient teal and donor purple used consistently; attribution visible bottom-right (bottom-center if portrait).
```
"""


TILES = [("course", "Course tile (Academy cards and the course home grid)", f"{HUB}-card.webp",
          "a bright hospital corridor with a coordinator walking between two separate open consultation rooms, a recipient in one and a donor in the other, each with their own clinician")]
for n, (row_scene) in enumerate([
    "a coordinator drawing two separate colored pathways on a whiteboard for a seated recipient",
    "a coordinator and program manager reviewing printed issuances with colored date tabs",
    "a coordinator kneeling beside an older dialysis patient and his wife with a pathway leaflet",
    "a transplant case conference around a table with a blank wall screen",
    "a gloved hand checking a labeled specimen tube beside an open transport cooler",
    "a quiet private consultation between a coordinator and an adult potential donor, door closed",
    "a nephrologist showing a simple risk picture to an adult donor while a coordinator listens",
    "a coordinator checking certificates against a checklist beside a document scanner",
    "an ethics committee around an oval table receiving a sealed case folder",
    "a Z Benefits coordinator explaining a cost plan to a recipient and his sister at a billing counter",
    "a claims officer and coordinator comparing a checklist with a claim folder",
    "a coordinator on the phone updating a waiting-list record, wall calendar behind",
    "a coordinator at a nurses' station at night reading back details from a structured form",
    "a pre-operative huddle around a readiness board with green and amber lights",
    "a recipient doing teach-back with a colored pill organizer while his wife watches",
    "a coordinator at a clinic desk on an urgent call, writing on a structured log",
    "a coordinator greeting a healthy adult donor at clinic reception for a yearly check",
    "a social worker and coordinator with a worried family, one member on a video call",
    "a coordinator and quality officer reviewing a run chart on a monitor",
    "a coordinator presenting a two-lane journey map to colleagues in a training room"], 1):
    TILES.append((f"{n:02d}", f"Module {n}: {TITLES[n - 1]}", f"{HUB}-{n:02d}-{SLUGS[n - 1]}-card.webp", row_scene))


def tile_block(t):
    key, label, fname, scene = t
    return f"""### RTC-T{('00' if key == 'course' else key)} · {label}

```
FILE NAME: {fname.replace('.webp', '.png')}  → save as images/{fname} (640 × 360 WebP)
IMAGE TYPE: Photorealistic editorial tile (16:9)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1536 × 864 (export down to 640 × 360)
AUDIENCE: course browsers on the course home and Academy landing page
VISUAL GOAL: let a learner recognize the module's task in one glance at thumbnail size.

PROMPT:
Photorealistic premium healthcare editorial photograph, 16:9, of {scene}, in a bright, airy, modern Philippine transplant center with soft natural daylight. Filipino people of varied ages and builds, natural skin texture, calm and respectful mood; a cast and camera angle different from the module's circular hero. One clear focal action readable at thumbnail size; simple uncluttered background in light neutrals with teal #1a6b72 accents. No readable text on documents, screens, or badges.
Bottom-right corner: "{ATTR}" in very small semi-transparent navy text ({FONT}).

NEGATIVE INSTRUCTIONS:
No dark or moody lighting, no cartoon style, no clutter, no readable names or numbers, no logos, no money changing hands, no distressed or pressured donor, no distorted hands or faces.

QUALITY CHECK:
Reads clearly at 640 × 360; light background; nothing legible except the tiny attribution.
```
"""


OG = [
    ("RTC-OG1", "Course share card art (Academy share-card builder)", f"images/academy/og-art/{HUB}.png", "1536 × 1024", "3:2",
     "the build_academy_og.py share card for academy/transplant-coordinator.html (output images/og/academy/transplant-coordinator.jpg, 1200 × 630)",
     "Text-free photorealistic editorial art, 3:2, for an Open Graph share card. The LEFT 42% of the frame is a quiet, uncluttered light field (soft off-white wall with gentle teal-tinted gradient) because the site's script will set the title text there; keep every subject in the RIGHT 58%. Subject on the right: a Filipino transplant coordinator (woman in her late 30s, shoulder-length straight hair, teal scrubs) standing between two doorways, gesturing warmly toward a seated adult recipient on one side and an adult living donor on the other, each in their own space with their own clinician, bright daylight, calm and dignified.",
     "Absolutely no text, letters, logos, or watermark (the build script adds all words and the URL). No dark backgrounds. Nothing in the left 42%."),
    ("RTC-OG2", "Toolkit share card (complete card with words)", f"images/og/{HUB}-toolkit.png → convert to images/og/{HUB}-toolkit.jpg", "1200 × 630", "1.91:1",
     "og:image of guides/calc-transplant-coordinator-toolkit.html (already referenced in the page head)",
     f"Clean Open Graph share card, exactly 1200 × 630, white (#ffffff) background with a light teal (#eef6f7) panel on the right. Left side typography in {FONT}: small teal eyebrow \"RENAL CARE ACADEMY · TOOLKIT\"; large bold navy (#0f1e2e) title \"Transplant Coordinator Toolkit\"; navy subtitle \"7 planning tools: readiness gates, 180-day pre-authorization, 60-day claim window, cost gap, medicine runway, donor follow-up\". Right panel: a simple flat illustration of a tablet screen showing a two-row board of eight round lights (seven green, one amber) above a small calendar with a shaded 60-day band (no numbers). Bottom-right: \"{ATTR}\" in small semi-transparent navy text.",
     "No dark backgrounds, no serif fonts, no misspellings, no extra words beyond those quoted, no logos of PhilHealth or DOH."),
    ("RTC-OG3", "End-of-course check and trainer page share card", f"images/og/{HUB}-final-exam.png → convert to .jpg", "1200 × 630", "1.91:1",
     "og:image for academy/transplant-coordinator-final-exam.html and -trainer.html (set by patch_og_images.py or by hand)",
     f"Clean Open Graph share card, exactly 1200 × 630, off-white (#fafafa) background. Left typography in {FONT}: teal eyebrow \"RENAL TRANSPLANT COORDINATOR\"; bold navy title \"Check Your Navigation Skills\"; subtitle \"20 questions, one from each module · educator page · capstone\". Right side: a simple flat illustration of two parallel lanes (teal and purple) passing four small gate icons (stethoscope, document, balance scale, peso coin) and ending in a green checkmark. Bottom-right: \"{ATTR}\" in small semi-transparent navy text.",
     "No dark backgrounds, no certificates, seals, or badges implying certification or CPD units, no serif fonts, no misspellings."),
]


def og_block(o):
    code, label, fname, dims, ratio, place, prompt, neg = o
    return f"""### {code} · {label}

```
FILE NAME: {fname}
IMAGE TYPE: Open Graph / social share {'art' if code == 'RTC-OG1' else 'card'}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {dims}
PLACEMENT: {place}

PROMPT:
{prompt}

NEGATIVE INSTRUCTIONS:
{neg} Avoid cartoon style, clutter, AI gibberish text, HDR, and over-saturation.

QUALITY CHECK:
{'Left 42% empty and light; subjects only on the right; no text at all.' if code == 'RTC-OG1' else 'Exactly 1200 × 630; every word spelled as quoted; light background; attribution visible.'}
```
"""


PLAN = f"""# Renal Transplant Coordinator — Image Plan Blueprint and GPT Prompt Pack

Prepared November 25, 2026 for the Renal Care Academy track `academy/{HUB}.html` (20 modules). Prompts follow the renalcarematters.com house skills: **williamriveromd-hero-vignette v3** (circular heroes), **williamriveromd-simple-figure** (teaching figures), and **williamriveromd-infographic-skill** (tiles and share cards). Paste each prompt block into ChatGPT image generation (current GPT image model; do not use the retired "Image Generator" GPT link). Every case, name, and identifier in the images is fictional. American English throughout.

## 1. Why these images

The course teaches one hard idea: **two people, four gates each, kept separate, closed by their owners.** The images carry that idea so a learner can recall it at the bedside.

| Image family | Teaching job | Count |
|---|---|---|
| Teaching figures (F) | Turn each module's rule into a diagram: the two lanes and four gates, the barrier register, the risk icon array, the 180-day and 60-day clocks, the read-back call, the readiness board | 21 |
| Circular heroes (H) | Set the human tone of each module: private, respectful, Filipino, two equally valued people | 21 |
| Tiles (T) | Let browsers recognize each module at thumbnail size | 21 |
| Share cards (OG) | Make shared links look trustworthy and accurate, with no certification claims | 3 |
| Landing tile | Ancillary Staff Track card on the Academy landing page | 1 (reuse RTC-T00, see below) |

**Visual grammar used everywhere:** recipient = clinical teal `#1a6b72`; donor = soft purple `#6c3d8e`; closed / safe = renal green `#1f7a4d`; pending = amber `#b8860b`; stop = clinical red `#b91c1c`. The four gates always appear in the same order with the same icons: Medical (stethoscope), Legal (document), Ethical (balance scale), Insurance (peso coin). Light backgrounds only. Font: {FONT}.

**Safety rules for every image:** no money changing hands, no pressured or distressed donor, no implied guarantee of surgery or payment, no certificates or seals implying certification, no real agency logos, nothing legible on documents, screens, wristbands, or badges.

## 2. File map and placement

| Code | File (save in `images/`) | Size | Where it appears |
|---|---|---|---|
| RTC-H00 | `{HUB}-vignette-hero.png` + `.webp` | 2048² | Course home hero disc; course OG fallback |
| RTC-H01–H20 | `{HUB}-NN-<slug>-vignette-hero.png` + `.webp` | 2048² | Each module's hero disc and share image |
| RTC-F00–F20 | `{HUB}-NN-<name>.webp` (keys in `tools/techcourses/rtc/figs.py`) | per prompt | In-lesson figure slots; pages show them automatically once the file exists |
| RTC-T00 | `{HUB}-card.webp` | 640×360 | Course card (`branch_img`) |
| RTC-T00 (reuse) | `academy/landing/{HUB}.webp` | 960×540 | Academy landing Ancillary Staff card (add the `<img>` line to the card in `academy/index.html` once the file exists) |
| RTC-T01–T20 | `{HUB}-NN-<slug>-card.webp` | 640×360 | Module cards on the course home |
| RTC-OG1 | `academy/og-art/{HUB}.png` | 1536×1024 | Input to `build_academy_og.py` (entry already added) |
| RTC-OG2 | `og/{HUB}-toolkit.jpg` | 1200×630 | Toolkit page `og:image` (already referenced) |
| RTC-OG3 | `og/{HUB}-final-exam.jpg` | 1200×630 | Final check and trainer pages |

## 3. Production steps (after generating)

1. Save PNGs with the exact file names above.
2. Convert: `cwebp -q 82 in.png -o out.webp` (figures and heroes); tiles `cwebp -q 80 -resize 640 360`; landing `-resize 960 540`.
3. Share card: `python3 build_academy_og.py --art images/academy/og-art --only {HUB} --patch` (the script needs permission to delete its previous fingerprinted card; run it on your Mac).
4. Rebuild pages so figures and heroes are picked up: `python3 generate_tech_courses.py --course rtc --patch`, then `python3 generate_rg_thumbs.py && python3 patch_rg_card_thumbs.py`.
5. Open three pages in light and dark mode on a phone and check that every figure label is spelled correctly before publishing.

## 4. Order of production (highest teaching value first)

F00 two lanes and four gates → F07 donor risk icon array → F14 readiness board → F10 three approvals → F13 read-back call → F16 urgent routing → H00 course hero → OG1 → remaining figures → module heroes → tiles → OG2, OG3.

---

## 5. Teaching figures (RTC-F)

"""


def main(out):
    parts = [PLAN]
    parts += [fig_block(f) for f in FIGURES]
    parts.append("\n---\n\n## 6. Circular vignette heroes (RTC-H)\n\nEach hero uses a different cast, archetype, and camera. Generate in order and compare against the previous hero before accepting.\n\n")
    parts += [hero_block(i, h) for i, h in enumerate(HEROES)]
    parts.append("\n---\n\n## 7. Module and course tiles (RTC-T)\n\n")
    parts += [tile_block(t) for t in TILES]
    parts.append("\n---\n\n## 8. Share cards (RTC-OG)\n\nOG cards are always exactly 1200 × 630 at output. RTC-OG1 is text-free art that the Academy share-card script crops to 1200 × 630 and letters itself, so titles are always spelled right.\n\n")
    parts += [og_block(o) for o in OG]
    parts.append("\n---\n\n## 9. Checklist before publishing images\n\n- [ ] 21 figures, 21 heroes, 21 tiles, 3 share cards produced and named exactly as above\n- [ ] Every figure label checked letter by letter against the prompt\n- [ ] No legible names, numbers, or identifiers in any photo\n- [ ] Recipient teal and donor purple consistent across all figures\n- [ ] Light backgrounds in every image, including share cards\n- [ ] Attribution renalcarematters.com visible on figures, tiles, and complete share cards (heroes and OG1 art stay wordless by design)\n- [ ] Pages rebuilt and checked in light and dark mode\n")
    open(out, "w", encoding="utf-8").write("\n".join(parts))
    print("wrote", out)


if __name__ == "__main__":
    main(sys.argv[1])
