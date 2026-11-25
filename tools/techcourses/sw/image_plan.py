# -*- coding: utf-8 -*-
"""Renal Social Worker track: image plan blueprint and GPT prompt book (Stage 1 of the two-stage image pipeline).

  python3 tools/techcourses/sw/image_plan.py            # write the prompt book (repo copy + working folder copy)
  python3 tools/techcourses/sw/image_plan.py --wire     # also add the B figures to figs.py and their {{fig:}} macros to the modules

Skills applied: williamriveromd-hero-vignette v3 (heroes), williamriveromd-infographic-skill v5 (teaching figures, tiles, OG cards),
williamriveromd-simple-figure (single-idea figures), williamriveromd-algorithm-generator-skill (the safety pathway and two-step
screen). Every number on an image is already in the module text and verified against its source."""
import argparse, html, importlib.util, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HUB = "social-worker"
WORKDIRS = [Path("/Volumes/Storage/Renal Care Academy/Social Worker"), Path.home() / "mnt" / "Social Worker"]


def _ld(n):
    s = importlib.util.spec_from_file_location("swplan_" + n, HERE / (n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


_C = _ld("course")
SLUGS = {m["id"]: m["slug"] for m in _C.MODULES}
TITLES = {m["id"]: m["title"] for m in _C.MODULES}
FIGS = _ld("figs").FIGS

FONT = "Inter"
STYLE = (f"Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); "
         f"navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber "
         f"#b8860b for caution or pending, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist or referral steps. Typeface: "
         f"{FONT} only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown, "
         f"Filipino patients, families and staff. Generous whitespace. Bottom-right corner: \"© renalcarematters.com\" in small "
         f"semi-transparent navy text (about 70% opacity).")
FIG_NEG = ("Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, "
           "generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif "
           "fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or "
           "documents with readable personal data. Do not invent numbers, amounts, rates or thresholds that are not written in this prompt. "
           "No visible blood, needles in skin, self-harm imagery, injuries beyond a small described bruise, or distressing faces. American "
           "English on every label. Never omit the renalcarematters.com attribution.")
FIG_QC = ("Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, "
          "publication-grade, white or soft light-gray background; no legible personal data; © renalcarematters.com visible bottom-right.")
SIZES = {"land": ("16:9 landscape", "1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)"),
         "port": ("2:3 portrait", "1024 × 1536")}
HERO_NEG = ("busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, "
            "repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, "
            "baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, "
            "dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, visible blood, needles in skin, "
            "distressing or tearful close-ups")
PH, ST = "photorealistic editorial photograph", "photorealistic still-life"

# ───────────────────────── heroes (21) ─────────────────────────
# (id or "hub", style, archetype, camera, safe side, subject, audience, goal)
H = [
 ("hub", PH, "J Environmental Storytelling", "wide environmental portrait, eye level", "upper-left",
  "a Filipina renal social worker in her early 40s with a round face, shoulder-length wavy black hair tucked behind one ear, and a "
  "mustard-yellow cardigan over a white blouse, seated on a low stool at eye level beside an older man in a dialysis recliner, listening "
  "with a small notebook closed on her knee; his wife sits close on his other side holding a tote bag; a nurse works at the next station, "
  "softly blurred, in a bright modern Philippine hemodialysis unit", "Mixed", "Kidney failure lands on a household; the social worker sits with all of it."),
 ("01", PH, "H Clinical", "over-the-shoulder, slightly high", "right",
  "a young Filipino social worker in his late 20s with a narrow face, neat undercut, thin-framed glasses and a sage-green polo, holding a "
  "small blank role card toward a middle-aged couple seated in a quiet corner of a dialysis unit; the wife leans in, the husband nods",
  "Mixed", "Say who you are and what you do before anything else."),
 ("02", PH, "H Clinical", "side profile, medium distance", "upper-right",
  "a Filipina dialysis nurse in her 50s with a short pixie cut and navy scrubs pointing at a hemodialysis machine while a younger social "
  "worker with a long braid and a lilac blouse watches and listens; a wall whiteboard with three shaded blocks (no writing) behind them",
  "Mixed", "The social worker learns the dialysis week from the people who run it."),
 ("03", PH, "A Editorial Portrait", "environmental portrait, low angle", "upper-left",
  "a Filipino dialysis unit head in his 60s with a broad face, gray side-parted hair and a barong-style white shirt, reviewing a binder with "
  "colored date tabs beside a social worker in her 30s with a high ponytail and a teal blazer, in a small bright hospital office",
  "Clinicians and managers", "Every rule has an issuer and a date."),
 ("04", PH, "H Clinical", "eye-level two-shot, close", "upper-right",
  "an 80-year-old Filipina grandmother with short white permed hair, a floral duster and a wooden cane, seated knee to knee with a "
  "social worker in her 30s with a short bob and a coral blouse who holds a simple picture card toward her; a closed door, a glass of water",
  "Mixed", "Privacy, her language, and her permission come first."),
 ("05", PH, "H Clinical", "three-quarter view, medium", "left",
  "a Filipino construction worker in his late 30s with a weathered angular face, a buzz cut and a gray work shirt, talking with his hands "
  "while a social worker in her 50s with salt-and-pepper hair in a clip and a maroon blouse writes on a clipboard in a hospital social "
  "service office", "Mixed", "The assessment looks for the reason behind the label."),
 ("06", PH, "I Object Hero", "close desk-level shot, hands only", "upper-left",
  "a social worker&rsquo;s hands on a desk: one hand holding a phone to an unseen ear, the other ticking a printed care-plan grid with columns "
  "(only blurred marks, no legible words), a small calendar and a pen beside it", "Mixed", "A referral is closed by a phone call, not a form."),
 ("07", PH, "H Clinical", "over-the-shoulder from the daughter", "right",
  "a Filipina woman in her mid-60s with silver hair in a low bun and a pastel-blue blouse, and her daughter in her 30s with a ponytail and "
  "office lanyard (blank card), at a hospital help desk while a male social worker in his 40s with a goatee and a white polo points to "
  "a printed sheet (only blurred marks)", "Mixed", "Explain the benefit by its rule and date, never by rumor."),
 ("08", PH, "E Lifestyle", "slightly overhead", "upper-right",
  "a Filipina wife in her early 40s with shoulder-length straight hair and a denim shirt sorting documents into three colored folders on "
  "a table at a government hospital assistance desk, a social worker in her 50s with short gray hair and reading glasses helping; "
  "folders show only blurred marks", "Mixed", "One strong application beats seven thin ones."),
 ("09", PH, "D Panorama", "wide-angle, early-morning street level", "upper-left",
  "a Filipino man in his early 50s with a lean face, a faded cap and a windbreaker stepping out of a tricycle at the entrance of a "
  "dialysis unit at dawn, his wife paying the driver, a social worker in a light-blue uniform greeting them at the door; soft sunrise light",
  "Mixed", "Getting to dialysis is a cost the household pays thirteen times a month."),
 ("10", PH, "A Editorial Portrait", "close portrait at the chair, eye level", "upper-right",
  "a Filipino man in his late 50s with a round face, thinning gray hair and a checked shirt, seated in a dialysis recliner looking toward a "
  "social worker in her late 20s with a pixie cut and a sage cardigan who sits beside him, listening; the dialysis machine softly blurred",
  "Mixed", "Notice, ask, and listen before you score anything."),
 ("11", PH, "H Clinical", "rear three-quarter view of the social worker", "left",
  "a calm private consultation room with the door closed; an older Filipina woman with long gray hair in a braid and a cardigan sits with "
  "hands folded while a male social worker in his 40s with a shaved head and a navy polo sits angled toward her, leaning in; a box of "
  "tissues and a glass of water on a small table", "Mixed", "Safety conversations happen in private and at an unhurried pace."),
 ("12", PH, "E Lifestyle", "side profile two-shot", "upper-left",
  "a Filipino man in his early 30s with tattooed forearms, a mechanic&rsquo;s cap turned backward and a gray T-shirt, leaning forward and "
  "laughing in a dialysis waiting area with a male social worker in his 30s with curly hair and a white shirt; a wall clock and a backpack",
  "Mixed", "Walk beside the person; do not push."),
 ("13", PH, "A Editorial Portrait", "environmental portrait, soft window light", "upper-right",
  "a tired Filipina caregiver in her mid-50s with graying hair in a loose bun and a faded floral blouse, holding a medicine pouch on her "
  "lap in a hospital family room, a social worker in her 40s with a short side-swept bob and a green blouse seated beside her",
  "Mixed", "See the person beside the chair."),
 ("14", PH, "J Environmental Storytelling", "wide-angle, doorway view", "upper-left",
  "a peritoneal dialysis nurse in her 40s with a long ponytail and white scrubs and a social worker in his 30s with a crew cut and a "
  "beige polo standing in a modest, clean Filipino home, looking at a corner with a raised shelf; a young woman in office wear shows them "
  "the space; no boxes with readable labels", "Mixed", "Feasibility is decided in the home, not only in the clinic."),
 ("15", PH, "H Clinical", "eye-level, across a small table", "right",
  "a Filipino man in his mid-20s with a lean build, a short fade haircut and a plain dark-green shirt, seated alone across from a female "
  "social worker in her 40s with chin-length hair and a gray blazer in a small private room with the door closed",
  "Mixed", "The donor is seen alone, and free to say no."),
 ("16", PH, "E Lifestyle", "slightly high wide shot", "upper-left",
  "a family meeting around a small round table: an 81-year-old Filipino retired fisherman with deep sun lines and a white cotton shirt, "
  "his wife with silver hair, their daughter in her 40s, a nephrologist in a white coat and a social worker; a laptop shows a blurred "
  "video call; a window with soft sea-blue light", "Mixed", "Advance care planning is a conversation, not a form."),
 ("17", PH, "D Panorama", "wide-angle through a rain-streaked window", "upper-right",
  "a female social worker in her 30s with a high bun and a navy rain jacket on the phone at a dialysis unit desk during heavy rain, a "
  "printed checklist in hand; through the window, flooded street and swaying palm trees in soft gray light", "Mixed",
  "Continuity means every patient dialyzed somewhere, even in a typhoon."),
 ("18", ST, "I Object Hero", "three-quarter desk view", "upper-left",
  "a secure office workstation: a monitor with a privacy screen showing only blurred shapes, a closed folder with a small lock icon, a "
  "phone placed face down, and a pen on a notepad with blurred marks; soft daylight on a clean desk", "Mixed",
  "Least information, right recipient, documented reason."),
 ("19", PH, "H Clinical", "over-the-shoulder at a monitor", "right",
  "a social worker in her late 20s with long straight hair and a plum blouse and her supervisor, a Filipina in her 60s with short "
  "silver hair and glasses, reviewing a simple run chart (line with dots, no legible numbers) on a monitor in a small office",
  "Mixed", "Measure what matters, and think it through in supervision."),
 ("20", PH, "J Environmental Storytelling", "wide-angle conference room", "upper-left",
  "a multidisciplinary case conference: a male social worker in his 40s with a neat mustache and a light-blue barong-style shirt points to "
  "a whiteboard timeline of colored blocks (no writing) while a nephrologist, a nurse and a dietitian listen around a table",
  "Mixed", "One family, one plan, every owner named."),
]

# ───────────────────────── teaching figures ─────────────────────────
# A figures already declared in figs.py; B figures added by --wire. (key, module, section to place B in, skill, scaffold, size, title, body)
FA = {
 "sw00_household": ("simple-figure", "Radial infographic", "Kidney failure lands on a household",
   "Center: a semi-photoreal Filipino man in his 50s seated in a dialysis recliner. Around him, seven concentric soft rings, each with one "
   "small icon and one label: \"Body\" (kidney icon), \"Household\" (house), \"Money\" (peso coin), \"Transport\" (tricycle), \"Work\" (tool "
   "bag), \"Family roles\" (three figures), \"Community services\" (barangay hall). A social worker figure stands just outside the outer "
   "ring holding a notebook, with a thin teal dotted line touching every ring. Footer line: \"See every ring, not only the body.\""),
 "sw01_who_decides": ("infographic-skill", "Role map infographic", "Who decides what",
   "Center: a patient and family pictogram. Six rounded tiles around it, each with an icon, the role, and what it owns: \"Nephrologist — "
   "treatment\", \"Nurse — bedside care\", \"Claims officer — benefit paperwork\", \"Social worker — assessment, plan, advocacy\" (teal "
   "highlight), \"Mental health clinician — diagnosis and therapy\" (purple), \"Supervisor — coverage and review\". A small amber footer "
   "chip: \"A navigator prepares; only the registered social worker signs.\""),
 "sw02_dialysis_week": ("simple-figure", "Timeline and physiology chart", "The dialysis week",
   "Top: a seven-day strip Monday to Sunday with three teal 4-hour blocks on Monday, Wednesday, Friday, each with a lighter travel band "
   "before and after. Bottom: one smooth sawtooth line labeled \"Body water and potassium\" rising between sessions and dropping during "
   "them, highest on Monday morning; the Friday-to-Monday gap shaded amber and labeled \"Long gap: 2 days\". A small red marker on the "
   "Monday peak: \"Skip Friday = 4 days\". No other numbers."),
 "sw03_rulebooks": ("infographic-skill", "Multi-panel educational infographic", "Who issues what",
   "Five cards on a desk, each with a small calendar icon labeled \"Effective date\": \"Congress + PRC — who may practice (RA 4373, RA "
   "10847)\", \"DOH — facility licensing (AO 2012-0001)\", \"PhilHealth — benefit circulars\", \"DSWD · PCSO · LGU — assistance "
   "programs\", \"Your hospital — job description and procedures\". Bottom banner: \"Tag every rule: issuer · scope · version · date.\""),
 "sw04_first_minutes": ("simple-figure", "Step sequence", "The first five minutes",
   "Four numbered panels left to right, semi-photoreal: 1 \"Set the room\" (closed door, two chairs angled, water glass); 2 \"Ask her "
   "language\" (speech bubble with three small flag-free language bubbles labeled \"Filipino\", \"Ilocano\", \"Cebuano\"); 3 \"Say your "
   "role and the limits of confidentiality\" (social worker with a role card); 4 \"Ask who may join\" (a relative waiting outside a "
   "door, a check mark). Footer: \"Every first interview, every time.\""),
 "sw05_domains": ("infographic-skill", "Radial infographic", "Psychosocial assessment domains",
   "A circular map of eight equal segments with one label each: \"Goals and values\", \"Understanding of illness\", \"Mood, coping, "
   "safety\", \"Family and caregivers\", \"Money and benefits\", \"Transport and housing\", \"Work, school, roles\", \"Substances, legal, "
   "other\". In each segment a small green strength icon (star) and a small amber barrier icon (stone). Center: \"Strengths beside "
   "barriers\"."),
 "sw05_formulation": ("simple-figure", "Left-to-right flow", "From facts to formulation to plan",
   "Left: five scattered fact cards, each with a tiny source tag (\"patient\", \"wife\", \"nurse\", \"chart\", \"claims\"). Middle: the "
   "cards grouped into a four-part box labeled \"Predisposing · Precipitating · Perpetuating · Protective\". Then one sentence card "
   "labeled \"Formulation\" (blurred lines). Right: a plan card with three rows \"Action · Owner · Date\". A curved arrow from the plan "
   "back to the facts labeled \"Review\"."),
 "sw06_referral_loop": ("simple-figure", "Circular workflow", "The referral loop",
   "Five stations on a loop: \"Sent\", \"Received and accepted\", \"Decided\", \"Delivered\", \"Confirmed with the person\". The first two "
   "stations amber with the tag \"Action\"; the last station green with a check and the tag \"Loop closed\". A small side card: "
   "\"Declined, with a reason, also closes the loop.\""),
 "sw07_philhealth": ("infographic-skill", "Three-panel comparison", "Reading a PhilHealth rule",
   "Three vertical panels: \"Hemodialysis — PC 2024-0023 — up to 156 sessions a year\", \"Peritoneal dialysis — PC 2024-0036 — Z "
   "Benefits through contracted providers\", \"Kidney transplant — PC 2026-0019 — published Nov 21, 2026; check effectivity\". Over the "
   "bottom of all three, a magnifying glass on a date tab: \"Check: circular · version · effective date · case date\"."),
 "sw08_assistance": ("infographic-skill", "Radial map with status chips", "Mapping assistance",
   "Center: a simple house icon with a family. Around it five source cards with icons: \"DSWD crisis assistance (AICS)\", \"PCSO Medical "
   "Access Program\", \"Malasakit Center (DOH and designated hospitals)\", \"Local government\", \"Employer, SSS or GSIS, community\". "
   "Each card has a status chip: amber \"Submitted\", teal \"Decided\", green \"Received\". Footer: \"Count what reached the household.\""),
 "sw09_access": ("simple-figure", "Stacked bar", "The access equation",
   "One tall stacked bar labeled \"One dialysis visit\" with five segments: \"Fare out\", \"Fare back\", \"Companion&rsquo;s fares\", "
   "\"Food\", \"Companion&rsquo;s lost wages\". An arrow to a row of thirteen small identical bars labeled \"× 13 visits a month\". A "
   "side card: \"Gap = total − confirmed support\". No peso amounts."),
 "sw10_stepped": ("simple-figure", "Staircase infographic", "Stepped psychosocial care",
   "Four ascending steps: \"1 Everyone — listening, information, practical help\", \"2 Some — structured support, problem solving\", "
   "\"3 Fewer — talking therapy or medicine through the mental health team\" (purple), \"4 A few — urgent psychiatric care\" (red). A "
   "thin red lane running alongside all steps labeled \"Safety question (item 9) open at every step\"."),
 "sw11_safety": ("algorithm-generator-skill (Style Mode C)", "Clinical algorithm flowchart", "The safety pathway",
   "Top box: \"A signal: 'better off gone', 'want to stop', 'what's the point'\". Arrow to diamond: \"Ask directly: thoughts of ending "
   "your life?\". YES branch (red) to stacked boxes: \"Stay with the person\" → \"Make the space safer (with the nurse)\" → \"Call the "
   "attending physician and the crisis route now\" → \"Warm handover\" → \"Document exact words, calls, plan\". NO or UNSURE branch (teal) "
   "to: \"Record, tell the nephrologist today, plan follow-up, ask again\". Small footer note: \"Asking does not plant the idea.\""),
 "sw12_oars": ("simple-figure", "Conversation illustration", "OARS in a conversation",
   "A semi-photoreal social worker and a younger man in a dialysis chair talking. Four speech-bubble icons around them: \"Open question\", "
   "\"Affirmation\", \"Reflection\", \"Summary\". Below, a small balance scale: left pan \"Reasons to change\", right pan \"Reasons to stay "
   "the same\". Footer: \"Draw out his reasons; do not argue for change.\""),
 "sw13_caregiver": ("simple-figure", "Comparison illustration", "Caregiver load and backup",
   "Left: a semi-photoreal Filipina caregiver carrying an overloaded tray of task tiles: \"Transport\", \"Medicines\", \"Meals\", \"Money\", "
   "\"Night care\", \"Her own job\". Right: the same tasks spread across three people (the caregiver, a backup relative, the patient "
   "himself with \"Medicines\") on lighter trays. A small scale: \"Tasks vs capacity\". Footer: \"Every essential task has a backup.\""),
 "sw14_modality": ("infographic-skill", "Three-panel comparison", "What each treatment asks of a household",
   "Three panels with a small home illustration each: \"In-center hemodialysis — travel 3 times a week, a companion\"; \"Peritoneal "
   "dialysis at home — a clean corner, storage for boxes, a trained person, a backup\"; \"Conservative kidney management — symptom care "
   "at home, regular team contact, a family ready\". Footer: \"Feasibility is a social question too.\""),
 "sw15_donor": ("simple-figure", "Two-pathway diagram", "The donor's separate path",
   "Two parallel paths: teal \"Transplant candidate\" and violet \"Living donor\", each passing a private interview room icon and its own "
   "team member icon, meeting only at \"Operation\". On the donor path, an open green door labeled \"Withdraw safely at any time\". A "
   "small lock icon on the donor path: \"Separate record\"."),
 "sw16_acp": ("simple-figure", "Conversation card illustration", "Advance care planning",
   "A semi-photoreal family meeting at a small table (older man, wife, daughter, nephrologist, social worker). Above the table, one simple "
   "card with three lines: \"What matters most?\", \"Who will speak for me?\", \"What do I want if I get sicker?\". A small circular arrow "
   "icon: \"Revisit when things change\"."),
 "sw17_continuity": ("infographic-skill", "Workflow map", "Continuity in a typhoon",
   "A simple map strip of a Philippine coastline with a typhoon symbol. Left: \"Home unit — closed\" with an amber flood icon. Right: "
   "\"Receiving unit — open\". Between them a handoff arrow carrying a folder labeled \"Order · serologies · medicines · contacts\". At the "
   "receiving end a green check: \"Arrival confirmed\". A side card: \"Not confirmed in 2 days → trace and alert the nephrologist\"."),
 "sw18_privacy": ("simple-figure", "Funnel diagram", "Minimum necessary disclosure",
   "A funnel: top \"Full record\", narrowing through three filters labeled \"Purpose\", \"Lawful basis\", \"Minimum needed\", to a small "
   "output card \"What this recipient needs\". A lock icon on the side: \"Approved channel\". A small log card: \"Who · what · why · "
   "when\"."),
 "sw19_measure": ("simple-figure", "Measure card and run chart", "A measure that means something",
   "Left: a measure card with \"Numerator: referrals with a confirmed outcome\" over \"Denominator: eligible referrals\", \"Period: month\", "
   "and the worked line \"10 / 12 = 83.3%\". Right: a simple run chart of monthly dots with a dashed median line (no other numbers). Below: "
   "a note card \"What it cannot show: whether the outcome helped\"."),
 "sw20_timeline": ("infographic-skill", "Horizontal timeline", "One family, start to finish",
   "A horizontal timeline January to December with nine milestones as small icons: \"Emergency start\", \"Missed sessions (fares)\", "
   "\"Depression screen\", \"Caregiver plan\", \"Session balance alert\", \"Typhoon transfer\", \"Peritoneal dialysis question\", "
   "\"Transplant and donor question\", \"Case conference\". A small social worker figure appears under each milestone. No dates beyond "
   "month names."),
}

FB = {  # key: (module, section id, skill, scaffold, title, file descriptor, alt, caption, body)
 "sw01b_confidentiality": ("01", "ethics", "simple-figure", "Reference card", "Before the person speaks", "before-the-person-speaks",
   "A card with four items a social worker says before an interview: who I am, why I am asking, who may see it, and the limits of confidentiality.",
   "Say these four things before the first personal question.",
   "A clean reference card with four numbered rows and icons: \"1 Who I am and what a social worker does here\", \"2 Why I am asking\", "
   "\"3 Who may see what you tell me\", \"4 The limits: immediate risk to life, legal duty to report\". Footer: \"Then ask: whom do you want "
   "in the room?\""),
 "sw02b_jobs": ("02", "kidneys", "simple-figure", "Comparison table graphic", "What kidneys do, what dialysis replaces", "what-dialysis-replaces",
   "A two-column comparison of kidney jobs and how much dialysis replaces each: water and salt, potassium, wastes partly; red-cell hormone and active vitamin D not.",
   "Dialysis replaces part of the cleaning, not the kidney&rsquo;s hormones.",
   "Left column: a semi-photoreal kidney labeled \"Healthy kidneys: 168 hours a week\". Right column: a dialysis machine labeled "
   "\"Hemodialysis: about 12 hours a week\". Five rows between them with check or cross icons: \"Remove water and salt — partly\", "
   "\"Balance potassium — partly\", \"Remove wastes — partly\", \"Make the red-cell hormone — no (injections needed)\", \"Activate vitamin "
   "D — no (medicines needed)\"."),
 "sw03b_charter": ("03", "charter", "simple-figure", "One-page document mockup", "A one-page service charter", "one-page-service-charter",
   "A one-page service charter with six labeled blocks: purpose, who is referred, how fast, who covers, how we measure, what we do not do.",
   "The service charter fits on one page.",
   "A clean single page mockup with six labeled blocks: \"Purpose\", \"Who is referred\", \"How fast (immediate · same day · 2 days to "
   "acknowledge · 10 days to assess)\", \"Who covers\", \"How we measure\", \"What we do not do\". A small amber tag on \"How fast\": "
   "\"Local targets, not national deadlines\"."),
 "sw04b_teachback": ("04", "literacy", "simple-figure", "Circular workflow", "Teach-back", "teach-back-loop",
   "A four-step loop: explain one idea, ask for it back, listen for gaps, explain again differently.",
   "Teach-back checks the explanation, not the person.",
   "A circular loop of four semi-photoreal steps between a social worker and an older woman: \"Explain one idea\", \"Ask for it back in "
   "her own words\", \"Listen for gaps\", \"Explain again differently (picture, calendar)\". Center: a speech bubble \"Opo\" crossed out "
   "lightly with the label \"Not proof of understanding\"."),
 "sw06b_goals": ("06", "goals", "simple-figure", "Before-and-after comparison", "Goals that belong to the person", "goals-in-her-words",
   "A comparison of weak and strong care plan goals, rewritten in the person&rsquo;s words with a time.",
   "Rewrite the worker&rsquo;s goal in the person&rsquo;s words.",
   "Two columns. Left, gray, labeled \"Worker&rsquo;s goal\": \"Address financial concerns\", \"Improve compliance\". Right, teal, labeled "
   "\"Her goal\": \"Stop borrowing to pay for transport by January\", \"Keep my job and attend all three sessions\". A small SMART badge "
   "with five letters spelled out: \"Specific · Measurable · Achievable · Relevant · Time-bound\"."),
 "sw07b_four_checks": ("07", "reading", "simple-figure", "Checklist card", "Four checks before you explain a benefit", "four-benefit-checks",
   "A checklist card of four checks before explaining a PhilHealth benefit: current circular and version, effective date, case date, transition rules.",
   "Check four things before you explain any benefit.",
   "A clean clipboard checklist with four green check boxes: \"Which circular and version?\", \"When did it take effect?\", \"What is "
   "the case date?\", \"Any transition rules?\". Beside it a small amber card: \"A social media post is not a source\"."),
 "sw10b_two_step": ("10", "screen", "algorithm-generator-skill (Style Mode C)", "Clinical algorithm flowchart", "The two-step depression screen", "two-step-screen",
   "A flowchart: two PHQ-2 questions, then the full PHQ-9 if either is positive, with item 9 asked in person and a branch to the safety pathway.",
   "Two questions first, the full PHQ-9 if either is positive, and item 9 every time.",
   "Top: \"PHQ-2: little interest? feeling down?\". If both \"not at all\" → teal box \"Record a negative screen; rescreen at the agreed "
   "interval\". If either positive → \"Complete the PHQ-9 with the person\" → diamond \"Item 9 above 0?\" YES (red) → \"Safety pathway "
   "now\"; NO → \"Total 10 or more: tell the nephrologist; offer support or referral\" and \"Below 10: support and rescreen\". Footer: "
   "\"A score is a screen, not a diagnosis.\""),
 "sw11b_signs": ("11", "elder", "simple-figure", "Four-panel reference card", "Signs of abuse and exploitation", "signs-of-exploitation",
   "Four panels showing signs of financial exploitation, neglect, physical abuse and psychological abuse in an older person on dialysis.",
   "Dependence creates vulnerability; ask privately.",
   "Four soft panels with simple icons: \"Financial — a relative holds the ATM or pension card\", \"Neglect — weight loss, no food at "
   "home, missed medicines\", \"Physical — a bruise with a changing explanation\" (a small bruise on an upper arm, nothing graphic), "
   "\"Psychological — fear and silence when a relative is present\". Footer: \"Ask privately. Offer options that keep dialysis going.\""),
 "sw12b_talk": ("12", "talk", "simple-figure", "Comparison panel", "Change talk and sustain talk", "change-talk",
   "Two columns of speech bubbles: change talk (desire, ability, reasons, need, commitment) and sustain talk, with the advice to reflect both without arguing.",
   "Strengthen change talk; reflect sustain talk without arguing.",
   "Left column, green, \"Change talk\": five bubbles \"I want…\", \"I could…\", \"Because my son…\", \"I have to…\", \"I will…\". Right "
   "column, amber, \"Sustain talk\": \"I cannot lose a day&rsquo;s pay.\" Between them a social worker icon with the label \"Reflect both; "
   "ask for more change talk; never argue\"."),
 "sw14b_feasible": ("14", "feasible", "simple-figure", "Problem-to-solution table", "Solve before you rule out", "solve-before-ruling-out",
   "A table of home peritoneal dialysis findings paired with possible solutions: storage, a shared room, flooding, water, no helper.",
   "Treat each home-visit finding as a problem to solve first.",
   "Five rows, each with an amber finding icon and an arrow to a green solution: \"No storage → smaller deliveries, a raised shelf, a "
   "relative&rsquo;s house\", \"Shared small room → a curtained clean corner\", \"Floods in heavy rain → supplies stored high, typhoon "
   "plan\", \"Unreliable water → stored clean water and sanitizer\", \"No helper → train a family member\". Footer: \"The clinical team "
   "decides; you bring solutions.\""),
 "sw15b_signals": ("15", "coercion", "simple-figure", "Reference card", "Signals to route, not to judge", "donor-signals",
   "A card listing signals of possible donor inducement or a false relationship, with the instruction to route them through the protected pathway.",
   "A signal is not proof; route it through the protected pathway.",
   "A clean card with five amber rows and small icons: \"Knows little about the recipient&rsquo;s family\", \"Promised money, a job or a "
   "business\", \"Recent arrival; housing paid by the recipient&rsquo;s family\", \"Hurry; rehearsed answers; a third party always "
   "present\", \"In debt or crisis\". A purple arrow at the bottom: \"Report to the donor advocate and ethics committee; do not confront "
   "the family\"."),
 "sw16b_bereavement": ("16", "grief", "simple-figure", "Timeline", "Bereavement follow-up", "bereavement-follow-up",
   "A timeline of bereavement contacts after a death: practical help at the death, a call in the first weeks, a check-in at three to six months, referral if grief does not ease.",
   "Stay with the family after a death.",
   "A gentle horizontal timeline with four soft markers: \"At the death — documents, the wake\", \"First weeks — a call or card\", \"3 to 6 "
   "months — a check-in\", \"Grief not easing → referral to the mental health team\". A small candle icon at the start. Calm pastel tones."),
 "sw17b_plan": ("17", "prepare", "simple-figure", "Checklist card", "The personal emergency plan", "personal-emergency-plan",
   "A personal dialysis emergency plan card: two alternative units, contacts, documents to bring, emergency diet advice, medicines.",
   "Every patient has a written plan before the rainy season.",
   "A laminated-looking card with a small umbrella icon and five rows: \"Two other units (name, address, number)\", \"Two contacts and a "
   "neighbor\", \"Bring: dialysis order, serologies, medicine list, PhilHealth details, ID\", \"Emergency diet advice from the "
   "dietitian\", \"A few days of medicines, kept dry\". All fields blank lines only."),
 "sw18b_release": ("18", "release", "algorithm-generator-skill (Style Mode C)", "Decision flowchart", "Releasing information", "release-decision",
   "A decision flow for a release request: who is asking, why, on what basis, what is the minimum, and record the release; a relationship alone is not authorization.",
   "A relationship is not authorization.",
   "Top: \"Request for information\". Four stacked diamonds: \"Who is asking?\", \"Why (purpose)?\", \"On what lawful basis?\", \"What is the "
   "minimum needed?\". If any answer is unclear → amber \"Route to the records officer or DPO\". If all clear → green \"Release the "
   "minimum, record who, what, why, when\". Side note: \"Spouse or relative ≠ authorization\"."),
 "sw20b_presentation": ("20", "conference", "simple-figure", "Step sequence", "A five-minute case presentation", "five-minute-presentation",
   "Five steps of a case presentation: the person&rsquo;s goal, formulation, what has been done, current risks, specific requests.",
   "Open with the person&rsquo;s goal; close with requests to named people.",
   "Five numbered blocks left to right with a small clock icon \"5 minutes\": \"1 Who and what matters (in their words)\", \"2 "
   "Formulation\", \"3 What has been done\", \"4 Current risks\", \"5 Requests: person · decision · date\"."),
 "sw09b_options": ("09", "work", "simple-figure", "Option cards", "Keeping a livelihood", "keeping-a-livelihood",
   "Five option cards for keeping work alongside dialysis: shift change, employer letter, SSS or GSIS benefits, new work, peritoneal dialysis to free daytime.",
   "Ask about work in the first month.",
   "Five rounded option cards with icons and the owner in small text: \"Change the dialysis shift — head nurse, nephrologist\", "
   "\"Employer letter (with consent, minimum detail) — employer\", \"Sickness or disability benefits — SSS or GSIS\", \"Work that fits "
   "treatment — DOLE or local livelihood programs\", \"Peritoneal dialysis to free daytime — the person and the nephrologist\"."),
 "sw13b_young_carer": ("13", "roles", "simple-figure", "Comparison illustration", "Protecting a young carer", "young-carer",
   "A teenage girl&rsquo;s week before and after a caregiver plan: missed school days replaced by adult backup on dialysis days.",
   "A child&rsquo;s schooling is not a backup plan.",
   "Two weekly calendars side by side for a 15-year-old girl (semi-photoreal, school uniform, backpack). Left \"Before\": two school days "
   "crossed out amber with a small dialysis-unit icon. Right \"After\": all school days green; dialysis-day transport covered by an adult "
   "backup icon. Footer: \"Protect schooling; move adult tasks to adults.\""),
}

# ───────────────────────── course tiles (no text) ─────────────────────────
T = {
 "card": "a social worker&rsquo;s notebook and a small compass resting on a bright dialysis unit side table beside a folded blanket, soft daylight",
 "01": "a blank role card and a lanyard on a light desk beside two chairs angled toward each other",
 "02": "a desk calendar with three days circled in teal beside a small model of a kidney",
 "03": "a neat binder with colored date tabs and a small desk calendar",
 "04": "two chairs angled toward each other with a glass of water and a picture card on a small table",
 "05": "an open notebook with a circular diagram of blurred segments and a pen",
 "06": "a phone and a printed grid with check marks (blurred) on a desk",
 "07": "a magnifying glass over a calendar date tab on a stack of papers (no legible text)",
 "08": "three colored folders (teal, amber, green) neatly stacked",
 "09": "a tricycle parked outside a clean clinic entrance at sunrise",
 "10": "an empty dialysis recliner with a folded blanket and a small stool beside it",
 "11": "a closed consultation room door with a soft light beneath it",
 "12": "two coffee cups on a small waiting-room table, angled toward each other",
 "13": "a medicine pouch and a set of house keys on a family-room chair",
 "14": "a raised clean shelf in a modest home corner with a curtain partly drawn",
 "15": "two separate doors in a bright corridor, one slightly open",
 "16": "a small round table with four chairs and a cup of tea near a window with sea-blue light",
 "17": "a rain-streaked window with a phone and a checklist on the sill",
 "18": "a locked folder and a phone placed face down on a clean desk",
 "19": "a printed run chart (dots and a dashed line, no numbers) on a clipboard",
 "20": "a whiteboard with colored blocks in a row (no writing) and markers on the ledge",
}


def hero_prompt(i, style, arch, cam, safe, subj, aud, goal):
    slug = HUB if i == "hub" else f"{HUB}-{i}-{SLUGS[i]}"
    scaf = "Scaffold A people" if style == PH else "Scaffold B still-life"
    p = (f"Square 1:1 {style} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas "
         f"diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: "
         f"{arch}. Camera: {cam}. Subject: {subj}, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject "
         f"60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the {safe} side of soft "
         f"gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade "
         f"harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text "
         f"of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.")
    human = ("No people" if style == ST else "Hands only; skin tone and hand position differ from the previous image" if "hands only" in cam
             else "Changed from the previous hero in this track: age, sex, face shape, jawline, hairstyle, hair length, hair color, clothing "
                  "style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle")
    return slug, (f"FILE NAME: images/{slug}-vignette-hero.png\nIMAGE TYPE: Circular vignette hero v3 ({scaf})\n"
                  f"ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)\nPIXEL DIMENSIONS: 2048 × 2048\n"
                  f"COMPOSITION ARCHETYPE: {arch}\nCAMERA: {cam}\nHUMAN VARIATION: {human}\nAUDIENCE: {aud}\nVISUAL GOAL: {goal}\n\n"
                  f"PROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid {HERO_NEG}.\n\nQUALITY CHECK:\nSquare 2048×2048; circle 85–90% of canvas "
                  f"with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the {safe} side; Filipino "
                  f"setting; no text or legible personal data; a different cast and camera from the previous hero.")


def fig_prompt(stem, skill, scaf, size, title, body, aud="Social workers and the kidney care team"):
    ratio, px = SIZES[size]
    return (f"FILE NAME: images/{stem}.png\nSKILL: williamriveromd-{skill.split(' ')[0]}{skill[len(skill.split(' ')[0]):]}\nIMAGE TYPE: {scaf}\n"
            f"ASPECT RATIO: {ratio}\nPIXEL DIMENSIONS: {px}\nAUDIENCE: {aud}\n\nPROMPT:\nTitle at top in bold navy: \"{title}\". {body} "
            f"{STYLE}\n\nNEGATIVE INSTRUCTIONS:\n{FIG_NEG}\n\nQUALITY CHECK:\n{FIG_QC}")


def tile_prompt(i):
    name = f"images/{HUB}-card.png" if i == "card" else f"images/{HUB}-{i}-card.png"
    p = (f"16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: {T[i]}. One bold, "
         f"instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale "
         f"teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal "
         f"#1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.")
    return (f"FILE NAME: {name} (generate at 1536 × 1024; prep script exports 640 × 360 WebP"
            f"{'; the course tile also writes images/academy/landing/social-worker.webp 960 × 540' if i == 'card' else ''})\n"
            f"IMAGE TYPE: Course tile (16:9, no text)\nVISUAL GOAL: Recognizable at thumbnail size; signals the {'track' if i == 'card' else 'module'}&rsquo;s one idea.\n\n"
            f"PROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid clutter, small details, faces, text of any kind, dark backgrounds, cartoon style, HDR.\n\n"
            f"QUALITY CHECK:\nReadable at 320 px; one subject; light background; no text.")


def og_prompt(i):
    if i == "hub":
        slug, title, sub, bg = HUB, "Renal Social Worker", "20 modules · assessment, support, and access to care", T["card"]
    elif i == "toolkit":
        slug, title, sub, bg = "social-worker-toolkit", "Social Worker Toolkit", "6 planning tools · access cost · session balance · workload", \
            "a calculator, a small peso coin stack, a desk calendar and a clipboard with a blurred grid"
    else:
        slug, title, sub, bg = f"{HUB}-{i}-{SLUGS[i]}", TITLES[i], f"Renal Social Worker · Module {int(i)} of 20", T[i]
    out = f"images/og/{slug}.jpg" if i == "toolkit" else f"images/og/{slug}-og.jpg"
    p = (f"Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; "
         f"generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. "
         f"Left 55%: text block in {FONT}. Small chip at top in renal green #2e6b3e with white text \"RENAL CARE ACADEMY · ANCILLARY STAFF "
         f"TRACK\". Title in bold navy #0f1e2e, three lines at most: \"{title}\". Subtitle in teal #1a6b72: \"{sub}\". A thin teal rule under "
         f"the title. Right 45%: a clean photorealistic still-life on a light surface: {bg}, softly lit, no faces. Bottom-right: "
         f"\"© renalcarematters.com\" in small semi-transparent navy text. Spell every word exactly as given, American English.")
    return out, (f"FILE NAME: {out.replace('.jpg', '.png')} (prep script exports {out} 1200 × 630 JPEG ≤ 300 KB)\nIMAGE TYPE: OG / social share card\n"
                 f"ASPECT RATIO: 1.91:1\nPIXEL DIMENSIONS: 1200 × 630 (final)\nAUDIENCE: Social workers and kidney care teams\n"
                 f"VISUAL GOAL: A share preview that names the page and shows its one idea.\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\n"
                 f"Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or "
                 f"decorative fonts, more than one subject. Never omit renalcarematters.com.\n\nQUALITY CHECK:\nTitle readable at 600 px "
                 f"wide; text only in the left 55%; spelling exact; light background.")


def fb_file(k):
    m, sec, skill, scaf, title, desc, *_ = FB[k]
    return f"{HUB}-{m}-{desc}.webp"


def wire():
    """Add the B figures to figs.py and place their {{fig:}} macros after the first paragraph of their section."""
    fp = HERE / "figs.py"; s = fp.read_text(encoding="utf-8"); added = 0
    for k, (m, sec, skill, scaf, title, desc, alt, cap, body) in FB.items():
        if f'"{k}"' in s:
            continue
        entry = (f'    "{k}": (_P + "{m}-{desc}.webp",\n        "{alt}",\n        "{cap}"),\n')
        s = s.rstrip().rstrip("}").rstrip() + "\n" + entry + "}\n"; added += 1
    fp.write_text(s, encoding="utf-8")
    placed = 0
    for k, (m, sec, *_r) in FB.items():
        p = HERE / f"m{m}.py"; t = p.read_text(encoding="utf-8")
        macro = "{{fig:" + k + "}}"
        if macro in t:
            continue
        mm = re.search(r'\(\s*"' + re.escape(sec) + r'",\s*"[^"]*",\s*"[^"]*",\s*"""', t)
        if not mm:
            raise SystemExit(f"section {sec} not found in m{m}.py")
        e = t.find("</p>", mm.end())
        t = t[:e + 4] + "\n" + macro + t[e + 4:]
        p.write_text(t, encoding="utf-8"); placed += 1
    print(f"figs.py: {added} B figures added; {placed} macros placed")


def book():
    nA, nB = len(FA), len(FB)
    total = 21 + nA + nB + 21 + 21 + 1 + 1
    o = ["# Renal Social Worker track: image plan blueprint and GPT prompt pack", "",
         "Renal Care Academy → Ancillary Staff Track → Renal Social Worker. Prepared November 25, 2026. American English throughout. "
         "Stage 1 of the two-stage image pipeline: generate in ChatGPT image generation, then run the prep script (Stage 2).", "",
         "## 1. Why these images", "",
         "Every image has one job: make a social work decision easier to understand, apply, or appreciate. The track teaches judgment "
         "about people, money, risk, and rules, so the images show people and processes rather than anatomy, and every teaching figure turns "
         "one paragraph of the module into one picture a learner can recall on shift.", "",
         "| Image | Learning purpose | Where it appears | Count |", "| --- | --- | --- | --- |",
         "| **Circular vignette hero** | Appreciation: who is involved, where, and what is at stake | Top of the course home and each module | 21 |",
         f"| **Teaching figure A** | Understanding: the module&rsquo;s central idea | Already wired into the module text (`figs.py`) | {nA} |",
         f"| **Teaching figure B** | Application: a decision tool, checklist, or flow to use on shift | Wired after the first paragraph of its section | {nB} |",
         "| **Course tile** | Navigation: recognition on the syllabus cards and module tiles | Course home module cards; Related Guides thumbnails | 21 |",
         "| **OG share card** | Reach: a share preview that names the page | `og:image` for the course home and each module (`images/og/<slug>-og.jpg`, picked up automatically) | 21 |",
         "| **Toolkit OG card** | Reach for the calculator page | `og:image` of `guides/calc-social-worker-toolkit.html` | 1 |",
         "| **Track share-card art** | Background for the Academy composited track card (text set by `build_academy_og.py`) | `images/academy/og-art/social-worker.webp` | 1 |",
         "| **Landing tile** | The Renal Social Worker card on `academy/index.html` | `images/academy/landing/social-worker.webp` | made from the course tile |", "",
         f"**Total: {total} prompts.**", "",
         "## 2. Rules for every image", "",
         "- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e; the Ancillary track accent is green #2e6b3e.",
         "- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.",
         "- **Attribution:** teaching figures and OG cards carry `© renalcarematters.com` bottom-right. Heroes and tiles carry no text at all.",
         "- **Privacy and dignity:** fictional people only; no legible names, ID numbers, PhilHealth numbers, documents, or screens; no self-harm imagery; no tears in close-up; violence and abuse shown only as a small described bruise or as icons.",
         "- **Numbers:** an image carries only the numbers written in its prompt, each already in the module and verified (156 sessions; 10/12 = 83.3%; 2-day gap; 3 to 6 months).",
         "- **People:** Filipino patients, families and staff; a different cast, camera and setting in each hero (hero-vignette v3 human-variation rule).",
         "- **Skills used:** `williamriveromd-hero-vignette` v3 (heroes), `williamriveromd-infographic-skill` v5 (figures, tiles, OG cards), `williamriveromd-simple-figure` (single-idea figures), `williamriveromd-algorithm-generator-skill` Style Mode C (the safety pathway, the two-step screen, the release decision).", "",
         "## 3. Production workflow", "",
         "1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `images/incoming/social-worker/` in the repo (track art in a subfolder `og-art/`). You can also drop them in `/Volumes/Storage/Renal Care Academy/Social Worker/images/` first for audit.",
         "2. Run `python3 tools/techcourses/sw/prep_images.py` (`--report` lists what is still missing). It writes heroes to `images/<slug>-vignette-hero.png` + `.webp`, figures to `images/<stem>.webp` + `.png`, tiles to 640 × 360 WebP (the course tile also to `images/academy/landing/social-worker.webp` 960 × 540), OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`, and the track art to `images/academy/og-art/social-worker.webp`.",
         "3. Rebuild: `python3 generate_tech_courses.py --course sw --patch`; `python3 build_academy_og.py --art images/academy/og-art --only social-worker --patch` and `--only academy-index`; `python3 generate_rg_thumbs.py`; `python3 patch_rg_card_thumbs.py`.",
         "4. Add `<img class=\"nc-fig-img\" src=\"../images/academy/landing/social-worker.webp\" …>` to the Renal Social Worker card on `academy/index.html` once the landing tile exists (the card is in place without an image).",
         "5. Audit each image against its QUALITY CHECK, check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger.", "",
         "## 4. Image map by module", "", "| Module | Hero idea | Figure A (understand) | Figure B (apply) |", "| --- | --- | --- | --- |"]
    amap = {}
    for k in FA:
        f = FIGS[k][0]; mm = re.match(r"social-worker-(\d\d)-", f); amap.setdefault(mm.group(1), []).append(FA[k][2])
    bmap = {}
    for k, v in FB.items():
        bmap.setdefault(v[0], []).append(v[4])
    for h in H[1:]:
        i = h[0]
        o.append(f"| {int(i)}. {TITLES[i]} | {h[7]} | {'; '.join(amap.get(i, ['—']))} | {'; '.join(bmap.get(i, ['—']))} |")
    o += ["", "## 5. Track-level images", ""]
    slug, txt = hero_prompt(*H[0])
    o += ["### Course home hero", "", "```", txt, "```", ""]
    o += ["### Course home figure A (also used in Module 1)", "", "```", fig_prompt(FIGS["sw00_household"][0][:-5], *FA["sw00_household"][:2], "land", *FA["sw00_household"][2:]), "```", "",
          f"*On-page caption:* {FIGS['sw00_household'][2]}", f"*Alt text:* {FIGS['sw00_household'][1]}", ""]
    o += ["### Course tile and Academy landing tile", "", "```", tile_prompt("card"), "```", ""]
    o += ["### Course home OG card", "", "```", og_prompt("hub")[1], "```", ""]
    o += ["### Toolkit OG card", "", "```", og_prompt("toolkit")[1], "```", ""]
    o += ["### Track share-card art (Academy composited card)", "", "```",
          "FILE NAME: images/incoming/social-worker/og-art/social-worker.png (prep script writes images/academy/og-art/social-worker.webp)\n"
          "IMAGE TYPE: Background art for build_academy_og.py (the script sets every word)\nPIXEL DIMENSIONS: 1536 × 1024\n\nPROMPT:\n"
          "3:2 landscape photorealistic editorial photograph on a light background: in a bright Philippine hemodialysis unit, a Filipina "
          "social worker in her 40s with shoulder-length wavy hair and a mustard cardigan sits at eye level beside an older man in a "
          "dialysis recliner while his wife sits close; a nurse softly blurred in the background. Place the people in the RIGHT 55%; keep "
          "the LEFT 45% as clean, light, empty negative space (soft wall and window light) where the builder sets the track title, group "
          "label and stats. Soft daylight, gentle depth of field, colors harmonizing with green #2e6b3e, teal #1a6b72 and navy #0f1e2e. "
          "Absolutely NO text, logos or watermark; no legible screens or papers.\n\nNEGATIVE INSTRUCTIONS:\nAvoid text, clutter, dark "
          "backgrounds, distressing expressions, legible documents, people in the left 45%.\n\nQUALITY CHECK:\nLeft 45% empty and light; "
          "subjects on the right; no text.", "```", ""]
    o += ["## 6. Module prompts", ""]
    for h in H[1:]:
        i = h[0]
        o += [f"### Module {int(i)}: {TITLES[i]}", ""]
        slug, txt = hero_prompt(*h)
        o += ["**Hero (circular vignette)**", "", "```", txt, "```", ""]
        for k, (skill, scaf, title, body) in FA.items():
            f, alt, cap = FIGS[k]
            if k == "sw00_household" or not f.startswith(f"{HUB}-{i}-"):
                continue
            o += [f"**Figure A: {title}**  ·  skill `{skill}`", "", "```", fig_prompt(f[:-5], skill, scaf, "land", title, body), "```", "",
                  f"*On-page caption:* {cap}", f"*Alt text:* {alt}", ""]
        for k, (m, sec, skill, scaf, title, desc, alt, cap, body) in FB.items():
            if m != i:
                continue
            o += [f"**Figure B: {title}**  ·  skill `{skill}`  ·  placed in section `{sec}`", "", "```",
                  fig_prompt(fb_file(k)[:-5], skill, scaf, "land", title, body), "```", "", f"*On-page caption:* {cap}", f"*Alt text:* {alt}", ""]
        o += ["**Course tile**", "", "```", tile_prompt(i), "```", ""]
        o += ["**OG share card**", "", "```", og_prompt(i)[1], "```", ""]
    o += ["## 7. Audit checklist before publishing", "",
          "- [ ] Every label spelled exactly as in the prompt (compare letter by letter; GPT often misspells).",
          "- [ ] No number on an image that is not in its prompt.",
          "- [ ] No legible names, ID numbers, documents, or screens; no self-harm imagery.",
          "- [ ] Heroes: circle with white margin, title-safe zone empty, a different cast from the previous hero, no text.",
          "- [ ] Figures and OG cards: light background, Inter, © renalcarematters.com bottom-right.",
          "- [ ] OG cards: text only in the left 55%, nothing important outside the 1.91:1 band.",
          "- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.", ""]
    return html.unescape("\n".join(o))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--wire", action="store_true"); a = ap.parse_args()
    if a.wire:
        wire()
    md = book()
    out = ROOT / "docs" / "tech-courses" / "social-worker-image-prompts.md"
    out.write_text(md, encoding="utf-8"); print("wrote", out)
    for w in WORKDIRS:
        if w.exists():
            (w / "SOCIAL-WORKER-IMAGE-PROMPTS.md").write_text(md, encoding="utf-8"); print("wrote", w / "SOCIAL-WORKER-IMAGE-PROMPTS.md"); break


if __name__ == "__main__":
    main()
